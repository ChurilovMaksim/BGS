"""Finite direct controls of the fixed-m Gaussian frame variance formulas."""
import json
from pathlib import Path
import numpy as np
from frame_probe import hermitian_coordinates

SEED=202610092
rng=np.random.default_rng(SEED)


def frame(n,m,real):
    g=rng.normal(size=(n,m))
    if not real:
        g=(g+1j*rng.normal(size=(n,m)))/np.sqrt(2)
    a=g.conj().T@g/n
    ev,v=np.linalg.eigh(a)
    z=(g@(v*(1/np.sqrt(ev))[None,:])@v.conj().T)/np.sqrt(n)
    leverage=np.sum(np.abs(z)**2,axis=1)
    rows=z/np.sqrt(leverage[:,None])
    if real:
        coords=[rows[:,j]**2 for j in range(m)]
        coords.extend(np.sqrt(2)*rows[:,i]*rows[:,j] for i in range(m) for j in range(i+1,m))
        x=np.stack(coords,axis=1)
        size=m*(m+1)//2
        iv=np.r_[np.ones(m),np.zeros(size-m)]
        target=(2*np.eye(size)+np.outer(iv,iv))/(m+2)
    else:
        x=hermitian_coordinates(rows)
        size=m*m
        iv=np.r_[np.ones(m),np.zeros(size-m)]
        target=(np.eye(size)+np.outer(iv,iv))/(m+1)
    f=x.T@(leverage[:,None]*x)
    assert np.linalg.norm(z.conj().T@z-np.eye(m))<1e-10
    assert np.linalg.norm(f@iv-iv)<1e-10
    assert abs(np.trace(f)-m)<1e-10
    return float(n*np.linalg.norm(f-target)**2)


def main():
    results=[]
    for real in (False,True):
        for m in (2,4,8):
            for n in (512,2048):
                values=np.array([frame(n,m,real) for _ in range(48)])
                predicted=m*(m*m-1)/(m+4) if real else m*m*(m-1)/(m+2)
                r={'field':'real' if real else 'complex','m':m,'N':n,'samples':len(values),
                    'scaled_error_mean':float(values.mean()),'standard_error':float(values.std(ddof=1)/np.sqrt(len(values))),
                    'fixed_m_limit':predicted}
                results.append(r)
                print(json.dumps(r),flush=True)
    payload={'seed':SEED,'samples_total':576,'arithmetic':'complex128 / float64',
        'non_claim':'Finite N sample means need not equal the asymptotic coefficient; no test establishes an asymptotic theorem.',
        'results':results}
    Path(__file__).with_name('stiefel_probe_results.json').write_text(json.dumps(payload,indent=2)+'\n')


if __name__=='__main__':
    main()
