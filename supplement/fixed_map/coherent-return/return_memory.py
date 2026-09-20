"""Exploratory exact-block checks. No claim of BGS or asymptotic evidence.

All computations live in ignored build/ until the main barrier is closed.
"""
import json
import numpy as np
from scipy.linalg import solve_discrete_lyapunov


def haar(n, rng):
    z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    v, r = np.linalg.qr(z)
    return v @ np.diag(np.diag(r)/abs(np.diag(r)))


def blocks(u):
    n = len(u)
    A = np.kron(u, u.conj())  # row-major vec, Ad_U
    ip = np.arange(n)*(n+1)
    iq = np.delete(np.arange(n*n), ip)
    return A, ip, iq, tuple(A[np.ix_(i, j)] for i,j in
                            ((ip,ip),(ip,iq),(iq,ip),(iq,iq)))


def checks(n, rng):
    v = haar(n, rng)
    phases = np.sort(rng.uniform(0, 2*np.pi, n))
    u = (v*np.exp(1j*phases))@v.conj().T
    A, ip, iq, (a,b,c,d) = blocks(u)
    I = np.eye(n)
    J = np.ones((n,n))/n
    D = abs(v)**2 @ (abs(v)**2).T
    idq = np.eye(len(iq))
    x = np.linalg.solve(idq-d, c)
    F1 = a+b@x
    Fprime = a+2*b@x+b@np.linalg.solve(idq-d, d@x)
    errors = dict(screening=float(np.linalg.norm(F1-I)),
        derivative_relative=float(np.linalg.norm(Fprime-np.linalg.inv(D))/
                                  np.linalg.norm(np.linalg.inv(D))))
    for z in (0.2+0.3j, np.exp(-1/n), np.exp(-0.1/n)):
        F = z*a+z*z*b@np.linalg.solve(idq-z*d,c)
        C = np.linalg.inv(np.eye(n*n)-z*A)[np.ix_(ip,ip)]
        err = np.linalg.norm(C-np.linalg.inv(I-F))/np.linalg.norm(C)
        errors['renewal_'+str(z)] = float(err)
        # Positive Herglotz lower bound from the invariant eigenspace.
        if np.isreal(z):
            Hreal = C+C.conj().T-I
            assert np.linalg.eigvalsh(Hreal-(1+z)/(1-z)*D).min() > -1e-9
    gram = solve_discrete_lyapunov(d,c@c.conj().T)
    errors['controllability_gramian'] = float(np.linalg.norm(gram-idq))
    mean = 1+np.trace(gram).real/n
    assert abs(mean-n) < 1e-8
    # Rank obstruction: A^j(diagonal) all contain the identity.
    power = idq.copy()
    singular_rows = []
    for k in range(n+1):
        sv = np.linalg.svd(power,compute_uv=False)
        lower = max(0,(n-1)*(n-k))
        exact_unit = np.sum(abs(sv-1)<1e-11)
        assert exact_unit >= lower
        assert np.vdot(power,power).real >= lower-1e-9
        singular_rows.append(dict(k=k,guaranteed_unit=lower,
                                 observed_unit=int(exact_unit)))
        power = power@d
    assert max(errors.values()) < 1e-8
    return dict(n=n,errors=errors,mean_return=float(mean),
                classical_gap=1-float(np.linalg.norm(a-J,2)),
                rank_checks=singular_rows)


def fourier_perturbation(n,rng):
    x=np.arange(n)
    F=np.exp(2j*np.pi*x[:,None]*x[None,:]/n)/np.sqrt(n)
    z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    h=(z+z.conj().T)/2
    h/=np.linalg.norm(h,2)
    ev,v=np.linalg.eigh(h)
    eps=n**-3
    u=((v*np.exp(1j*eps*ev))@v.conj().T)@F
    J=np.ones((n,n))/n
    assert np.linalg.norm(abs(u)**2-J,2) <= 2*eps+1e-12
    # Actual return probabilities through two monitored steps, without
    # forming N^2 by N^2 matrices.
    p1=np.sum(abs(u)**4)/n
    p2=0.
    for j in range(n):
        X=np.outer(u[:,j],u[:,j].conj())
        np.fill_diagonal(X,0)
        diag=np.diag(u@X@u.conj().T)
        p2+=np.vdot(diag,diag).real/n
    tail=max(0.,1-p1-p2)
    assert tail <= 16*eps**2+1e-12
    # Exact U=F has first-return p1=1/N and p2=1-1/N.
    # The generic perturbation has full cyclic space and mean N, so its
    # rare tail must carry almost all of that mean (not numerically summed).
    eigen=np.linalg.eigvals(u)
    times=np.arange(1,n+1)
    traces=np.array([np.sum(eigen**m) for m in times])
    window=(times>=n//2)
    weighted=np.sum(abs(traces[window])**2-times[window])/n**2
    return dict(n=n,epsilon=eps,classical_deviation=float(np.linalg.norm(abs(u)**2-J,2)),
        p1=float(p1),p2=float(p2),survival_past_two=tail,
        uniform_tail_bound=16*eps**2,
        diagnostic_box_window=float(weighted),
        tail_mean_lower_bound=(n-2)/(16*eps**2))


if __name__=='__main__':
    rng=np.random.default_rng(20260917)
    result=dict(random_checks=[checks(n,rng) for n in (2,3,5,8)],
        perturbed_fourier=[fourier_perturbation(n,rng) for n in (8,16,32,64)])
    print(json.dumps(result,indent=2))
