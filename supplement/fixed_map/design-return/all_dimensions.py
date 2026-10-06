"""Exact finite design construction checked in small composite dimensions.

The proof uses independent cube-root phases plus coordinate vectors.
The finite numerical checks also retain all repeated-eigenvalue pairs.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import itertools
import json
import numpy as np


def design(n):
    phases=np.array(list(itertools.product(range(3),repeat=n)))
    flat=np.exp(2j*np.pi*phases/3)/np.sqrt(n)
    vectors=np.concatenate((np.eye(n),flat))
    weights=np.r_[np.full(n,1/(n*(n+1))),np.full(len(flat),n/((n+1)*len(flat)))]
    return vectors,weights


def run(n):
    rng=np.random.default_rng(199+n)
    v,r=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
    v=v@np.diag(np.diag(r)/abs(np.diag(r)))
    vectors,weights=design(n)
    records=[]
    for repeated in (False,True):
        lam=(-1.)**np.arange(n) if repeated else np.exp(2j*np.pi*rng.uniform(size=n))
        u=(v*lam)@v.conj().T
        A=np.kron(u,u.conj())
        s=.7;mass=s/n;r=np.exp(-2*np.arcsinh(mass/2))
        resolvent=np.linalg.inv(np.eye(n*n)-r*A)
        C=[]
        for psi in vectors:
            rho=np.outer(psi,psi.conj()).reshape(-1)
            C.append(np.vdot(rho,resolvent@rho))
        recovered=(n*(n+1)*(2*np.real(weights@np.array(C))-1)/(1/r-r)-2*n/mass**2)/n**3
        gap=abs(lam[:,None]-lam[None,:])**2
        values=1/(mass**2+gap)
        np.fill_diagonal(values,0)
        direct=values.sum()/n**3
        assert abs(recovered-direct)<1e-11
        # This wrong expression discards distinct labels with equal phases.
        nonzero=gap>1e-12
        discarded=values[nonzero].sum()/n**3
        if repeated:
            multiplicity=((n+1)//2)**2+(n//2)**2
            assert abs((direct-discarded)-(multiplicity-n)/(s*s*n))<1e-12
        records.append(dict(repeated=repeated,energy=float(direct),
            reconstruction_error=float(abs(recovered-direct)),
            erroneous_all_invariants_removed=float(discarded)))
    return dict(N=n,probe_count=len(vectors),checks=records)


if __name__=='__main__':
    print(json.dumps([run(n) for n in (2,4,6)],indent=2))
