"""Finite phase-coherence identities and Haar variance controls.

Exact phase averaging is performed by grouping occupation vectors, avoiding
Monte Carlo error for the third form factor. Matrices use complex128.
"""
from itertools import product
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
SEED=101064271


def haar(n,rng):
    q,r=np.linalg.qr((rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2))
    diag=np.diag(r)
    return q*(diag/np.abs(diag))[None,:]


def occupation_average(u,n=3):
    amplitudes={}
    size=len(u)
    for word in product(range(size),repeat=n):
        occupation=tuple(word.count(j) for j in range(size))
        amplitude=np.prod([u[word[j],word[(j+1)%n]] for j in range(n)])
        amplitudes[occupation]=amplitudes.get(occupation,0)+amplitude
    return float(sum(abs(v)**2 for v in amplitudes.values()))


def third_formula(u):
    p=abs(u)**2
    q=u*u.T.conj()
    mixed=sum(p[i,i]*p[i,j]*p[j,i] for i in range(len(u)) for j in range(len(u)) if i!=j)
    return float((3*np.trace(p@p@p)+3*np.trace(q@q@q)
                  -5*np.sum(np.diag(p)**3)-9*mixed).real)


def bilinear_fourier(p,d,rank_two=True):
    vectors=np.array(list(product(range(p),repeat=d)),dtype=np.int64)
    b=np.eye(d,dtype=np.int64)
    if rank_two:
        b[0,1]=1
    u=np.exp(2j*np.pi*((vectors@b@vectors.T)%p)/p)/np.sqrt(p**d)
    q=u*u.T.conj()
    return u,q


def main():
    rng=np.random.default_rng(SEED)
    formulas=[]
    for n in [2,3,4,5,7]:
        for kind in ['Haar','identity','cyclic']:
            u=haar(n,rng) if kind=='Haar' else np.eye(n,dtype=complex)
            if kind=='cyclic':u=np.roll(u,1,axis=0)
            direct=occupation_average(u)
            formula=third_formula(u)
            error=abs(direct-formula)
            assert error<2e-12,(n,kind,error)
            formulas.append({'N':n,'kind':kind,'occupation_average':direct,'formula':formula,'error':error})
    bilinear=[]
    for p,d in [(3,2),(3,3),(3,4),(5,2)]:
        for rank_two in [False,True]:
            u,q=bilinear_fourier(p,d,rank_two)
            n=len(u);rank=2 if rank_two else 0
            unitary=np.linalg.norm(u@u.conj().T-np.eye(n),ord='fro')
            q3=np.linalg.norm(q@q@q-p**(-rank)*q,ord='fro')
            trace3=float(np.trace(q@q@q).real)
            qnorm=float(max(abs(np.linalg.eigvalsh(q))))
            k3=third_formula(u)
            target=3+3*p**(-rank)-9/n+4/n**2
            assert unitary<3e-12 and q3<3e-12
            assert abs(trace3-p**(-rank))<3e-12
            assert abs(qnorm-p**(-rank/2))<3e-12
            assert abs(k3-target)<3e-12
            if n<=27: assert abs(occupation_average(u)-target)<3e-11
            bilinear.append({'p':p,'d':d,'N':n,'antisymmetric_rank':rank,
                             'unitarity_error':unitary,'Q_cubic_error':q3,
                             'Q_norm':qnorm,'trace_Q_cubed':trace3,'third_form_factor':k3})
    # Adjacent independent implementations: exact character result and direct
    # samples of the explicit adjoint phase average sum |U_ii|^2-1.
    variances=[]
    for n in [2,4,8,16,32]:
        count=2400
        values=np.array([np.sum(abs(np.diag(haar(n,rng)))**2)-1 for _ in range(count)])
        second=float(np.mean(values**2))
        theory=1/(n+1)
        se=float(np.std(values**2,ddof=1)/np.sqrt(count))
        # Statistical reporting only. A random estimate is not an exact check.
        variances.append({'N':n,'samples':count,'sample_mean':float(values.mean()),
                          'mean_square':second,'exact_variance':theory,
                          'standard_error_mean_square':se,
                          'deviation_in_standard_errors':(second-theory)/se})
    result={'all_deterministic_checks_passed':True,'seed':SEED,
            'third_formula_cases':formulas,'bilinear_cases':bilinear,
            'Haar_adjoint_variance_samples':variances,
            'non_claims':['Finite tests do not prove the representation-theoretic theorem.',
                          'No form factor computation at n comparable to N.',
                          'Sampled Haar variances have Monte Carlo uncertainty.']}
    (ROOT/'phase_controls_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'formula_cases':len(formulas),'bilinear_cases':len(bilinear),
                      'max_formula_error':max(x['error'] for x in formulas),
                      'variance_samples':variances}))


if __name__=='__main__':main()
