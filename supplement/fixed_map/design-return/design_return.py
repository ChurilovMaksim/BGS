"""Deterministic frame identities and a finite falsification experiment.

The periodic test matrices are NOT quantizations of the fixed Anosov map.
No asymptotic gap claim is inferred from the finite data.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json
import numpy as np


def bases(p):
    x=np.arange(p)[:,None]
    k=np.arange(p)[None,:]
    return [np.eye(p,dtype=complex)]+[
        np.exp(2j*np.pi*((a*x*x+x*k)%p)/p)/np.sqrt(p)
        for a in range(p)]


def haar(p,rng):
    q,r=np.linalg.qr(rng.normal(size=(p,p))+1j*rng.normal(size=(p,p)))
    return q@np.diag(np.diag(r)/abs(np.diag(r)))


def transfer(u,bs):
    p=len(u)
    # P_b here means the rank p-1 traceless diagonal subspace of basis b.
    # K_ab=||P_a Ad_U P_b||_HS^2/(p-1).
    return np.array([[(np.sum(abs(a.conj().T@u@b)**4)-1)/(p-1)
                      for b in bs] for a in bs])


def run(p,rng):
    bs=bases(p)
    mub_error=max(np.max(abs(abs(a.conj().T@b)**2-1/p))
                  for i,a in enumerate(bs) for b in bs[i+1:])
    assert mub_error<2e-13
    v=haar(p,rng)
    signs=(-1.)**np.arange(p)
    u=(v*signs)@v.conj().T
    K=transfer(u,bs)
    J=np.ones_like(K)/(p+1)
    assert np.min(K)>-1e-13
    assert max(np.max(abs(K.sum(0)-1)),np.max(abs(K.sum(1)-1)))<2e-12
    assert np.linalg.norm(K-K.T)<2e-12
    trace_errors=[]
    for m in (1,2,3,4):
        um=np.linalg.matrix_power(u,m)
        diag_sum=sum(np.sum(abs(np.diag(b.conj().T@um@b))**2) for b in bs)
        trace_errors.append(abs(diag_sum-(p+abs(np.trace(um))**2)))
    assert max(trace_errors)<1e-8
    # Verify the gap observable using a simple-spectrum generic perturbation
    # with the SAME eigenvectors, retaining the two narrow phase clusters.
    eps=p**-3
    theta=np.pi*np.arange(p)% (2*np.pi)+eps*rng.uniform(-1,1,p)
    u_simple=(v*np.exp(1j*theta))@v.conj().T
    K_simple=transfer(u_simple,bs)
    s=.7
    gap=abs(np.exp(1j*theta[:,None])-np.exp(1j*theta[None,:]))**2
    energy_weights=1/((s/p)**2+gap)
    np.fill_diagonal(energy_weights,0)
    frame_energy=0.
    frame_overlap=np.zeros((p,p))
    for b in bs:
        B=abs(b.conj().T@v)**2
        overlaps=B.T@B
        frame_overlap+=overlaps
        frame_energy+=np.sum(overlaps*energy_weights)
    # Off-diagonal weights sum to 1, diagonal weights to 2.
    frame_error=np.max(abs(frame_overlap-(np.ones((p,p))+np.eye(p))))
    assert frame_error<2e-12
    assert abs(frame_energy/energy_weights.sum()-1)<2e-12
    X=np.arange(p)[:,None];Y=np.arange(p)[None,:]
    cat=np.exp(2j*np.pi*((-pow(8,-1,p)*(3*X*X-2*X*Y+3*Y*Y))%p)/p)/np.sqrt(p)
    K_cat=transfer(cat,bs)
    assert np.max(abs(K_cat-np.round(K_cat)))<2e-12
    # Diagnose non-Markovian propagation: K(U^2)=I for the involution,
    # despite a rapidly mixing one-step coarse transition matrix.
    K2=transfer(u@u,bs)
    assert np.linalg.norm(K2-np.eye(p+1))<2e-10
    return dict(N=p,mub_error=float(mub_error),frame_error=float(frame_error),
        trace_identity_error=float(max(trace_errors)),
        gap_involution=1-float(np.linalg.norm(K-J,2)),
        gap_simple_two_clusters=1-float(np.linalg.norm(K_simple-J,2)),
        two_step_markov_defect=float(np.linalg.norm(K2-K@K,2)),
        regularized_pair_energy=float(frame_energy/p**3),
        cat_transition_is_permutation=True)


if __name__=='__main__':
    rng=np.random.default_rng(20260918)
    print(json.dumps([run(p,rng) for p in (5,11,23,43)],indent=2))
