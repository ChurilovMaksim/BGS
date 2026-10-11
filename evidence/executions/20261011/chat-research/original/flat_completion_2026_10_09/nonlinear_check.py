"""Independent floating controls of nonlinear bounds and source derivatives."""
import json
import math
import os
import platform
from pathlib import Path

os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")
import numpy as np
from scipy.linalg import block_diag, expm

SEED = 640139


def logabsdet(matrix):
    sign, value = np.linalg.slogdet(matrix)
    assert abs(sign) > .99
    return float(value)


def action(a, b, zeta=1.):
    eye = np.eye(len(a))
    return logabsdet(eye-zeta*b@a.conj().T)-logabsdet(eye-a@a.conj().T)


def source_derivative(zeta_ba, k):
    eye = np.eye(len(zeta_ba))
    inv = np.linalg.inv(eye-zeta_ba)
    # Exact Eulerian polynomials for D^k logdet, D=zeta*d/dzeta.
    coeff = {1: [1], 2: [1], 3: [1, 1], 4: [1, 4, 1]}[k]
    poly = sum(value*np.linalg.matrix_power(zeta_ba, j)
               for j, value in enumerate(coeff))
    return -np.trace(zeta_ba@poly@np.linalg.matrix_power(inv, k))


def main():
    rng = np.random.default_rng(SEED)
    controls = []
    min_gap_slack, min_reg_slack = math.inf, math.inf
    max_mobius_error, max_source_ratio = 0., 0.
    for n in [4, 8, 16]:
        for q in [1, 2, 3]:
            for radius in [.1, .7, .98, .999999]:
                for model in ["fourier", "haar"]:
                    if model == "fourier":
                        x = np.arange(n)
                        u = np.exp(2j*np.pi*x[:, None]*x[None, :]/n)/np.sqrt(n)
                    else:
                        u = np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]
                    p = np.abs(u)**2
                    eta = float(np.linalg.norm(p-1/n, 2))
                    blocks = []
                    for i in range(n):
                        z = rng.normal(size=(q,q))+1j*rng.normal(size=(q,q))
                        z *= radius/np.linalg.norm(z,2)
                        blocks.append(z)
                    a = block_diag(*blocks)
                    unitary = np.kron(u,np.eye(q))
                    b = unitary@a@unitary.conj().T
                    phi = action(a,b)
                    first = np.linalg.norm(a-b)**2/2
                    avg = np.mean(blocks,axis=0)
                    variance = float(sum(np.linalg.norm(z-avg)**2 for z in blocks))
                    gap_lower = (1-eta)*variance
                    min_gap_slack = min(min_gap_slack, phi-first, first-gap_lower)
                    assert phi >= first-1e-7
                    assert first >= gap_lower-1e-9
                    center = .13+.21j
                    identity = np.eye(len(a))

                    def transform(z):
                        return (z-center*identity)@np.linalg.inv(identity-center.conjugate()*z)

                    fa, fb = transform(a), transform(b)
                    mobius_error = abs(action(fa,fb)-phi)
                    max_mobius_error = max(max_mobius_error,mobius_error)
                    assert mobius_error < 3e-7
                    rho, angle = .97, .031
                    zeta = rho*np.exp(1j*angle)
                    aa = a@a.conj().T
                    vr = logabsdet(identity-rho*aa)-logabsdet(identity-aa)
                    regulated = action(a,b,zeta)
                    lower = vr+rho*np.linalg.norm(np.exp(1j*angle)*b-a)**2/2
                    mean_lower = vr+rho*(1-eta)*variance+rho*(1-np.cos(angle))*n*np.linalg.norm(avg)**2
                    slack = min(regulated-lower,lower-mean_lower)
                    min_reg_slack = min(min_reg_slack,slack)
                    assert slack > -1e-7
                    ratios = []
                    for k in range(1,5):
                        derivative = abs(source_derivative(zeta*b@a.conj().T,k))
                        bound = rho*math.factorial(k-1)/(1-rho)**k*vr
                        ratio = float(derivative/bound)
                        ratios.append(ratio)
                        max_source_ratio=max(max_source_ratio,ratio)
                        assert ratio <= 1+1e-7
                    controls.append({"N":n,"q":q,"radius":radius,"model":model,
                                     "eta":eta,"Phi":phi,"first_lower":first,
                                     "classical_lower":gap_lower,"mobius_error":mobius_error,
                                     "source_ratios_k1_to_4":ratios})
    # Near-constant fields, including a center close to the boundary.
    small_field_ratios=[]
    n=8
    x=np.arange(n)
    u=np.exp(2j*np.pi*x[:,None]*x[None,:]/n)/np.sqrt(n)
    field=rng.normal(size=n)+1j*rng.normal(size=n)
    field-=field.mean()
    for scale in [.1,.01,.001]:
        a=np.diag(scale*field)
        b=u@a@u.conj().T
        ratio=action(a,b)/(scale**2*np.linalg.norm(field)**2)
        small_field_ratios.append(float(ratio))
    assert abs(small_field_ratios[-1]-1)<1e-4
    matrix_source_controls=[]
    for n in [4,8]:
        for q in [2,3]:
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            unitary=np.kron(np.linalg.qr(raw)[0],np.eye(q))
            sources=[]
            delta=.7
            for sign in [1,-1]:
                x=rng.normal(size=(q,q))+1j*rng.normal(size=(q,q))
                hermitian=(x+x.conj().T)/2
                v=rng.normal(size=(q,q))+1j*rng.normal(size=(q,q))
                positive=delta*np.eye(q)+v@v.conj().T/q
                sources.append(hermitian+sign*1j*positive)
            left=np.kron(np.eye(n),expm(1j*sources[0]/n))
            right=np.kron(np.eye(n),expm(-1j*sources[1]/n))
            normleft=float(np.linalg.norm(left,2))
            normright=float(np.linalg.norm(right,2))
            assert max(normleft,normright)<=np.exp(-delta/n)+1e-12
            for fermion in [False,True]:
                blocks=[]
                for i in range(n):
                    v=rng.normal(size=(q,q))+1j*rng.normal(size=(q,q))
                    v*= (5. if fermion else .98)/np.linalg.norm(v,2)
                    blocks.append(v)
                a=block_diag(*blocks)
                b=left@unitary@a@unitary.conj().T@right
                identity=np.eye(len(a))
                if fermion:
                    logratio=logabsdet(identity+b@a.conj().T)-logabsdet(identity+a@a.conj().T)
                else:
                    logratio=logabsdet(identity-a@a.conj().T)-logabsdet(identity-b@a.conj().T)
                ratio=float(np.exp(logratio))
                assert ratio<=1+1e-10
                matrix_source_controls.append({"N":n,"q":q,"fermionic_body":fermion,
                    "left_source_norm":normleft,"right_source_norm":normright,
                    "body_modulus":ratio,"field_operator_norm":float(np.linalg.norm(a,2))})
    output={"seed":SEED,"finite_controls":len(controls),"controls":controls,
            "minimum_gap_slack":min_gap_slack,"minimum_regulator_slack":min_reg_slack,
            "maximum_mobius_error":max_mobius_error,"maximum_source_bound_ratio":max_source_ratio,
            "sharp_constant_ratios":small_field_ratios,
            "matrix_source_controls":matrix_source_controls,
            "environment":{"python":platform.python_version(),"numpy":np.__version__},
            "scope":"Complex128 finite controls of written proofs; no integration claim or BGS conclusion."}
    here=Path(__file__).resolve().parent
    path=here/"nonlinear_check_results.json"
    path.write_text(json.dumps(output,indent=2)+"\n")
    summary={key:value for key,value in output.items() if key!="controls"}
    print(json.dumps(summary,indent=2),flush=True)


if __name__=="__main__":
    main()
