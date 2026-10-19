"""Finite empirical discriminator, not an asymptotic universality assertion."""
import itertools
import json
import sys
from pathlib import Path
import numpy as np
from scipy.linalg import eigvals


def fourier(p,d,symmetric=False):
    vertices=np.array(list(itertools.product(range(p),repeat=2*d)),dtype=np.int64)
    if symmetric:
        exponent=vertices@vertices.T
    else:
        swapped=vertices.copy()
        swapped[:,0::2]=vertices[:,1::2]
        swapped[:,1::2]=-vertices[:,0::2]
        exponent=vertices@swapped.T
    n=len(vertices)
    return np.exp(2j*np.pi*(exponent%p)/p)/np.sqrt(n)


def main(destination):
    rng=np.random.Generator(np.random.PCG64(202610181650))
    specifications=[('symplectic',5,1,1200),('symplectic',3,2,800),
                    ('symplectic',11,1,400),('symmetric_excluded',5,1,800),
                    ('Haar_control',5,1,400)]
    records=[]
    for label,p,d,samples in specifications:
        n=p**(2*d)
        powers=sorted(set([1,2]+[max(1,round(alpha*n)) for alpha in (.125,.25,.5,.75,1,1.5,2,4)]))
        s=fourier(p,d,symmetric=(label=='symmetric_excluded'))
        unitarity=float(np.linalg.norm(s@s.conj().T-np.eye(n)))
        assert unitarity<1e-10
        intensities=[]
        max_radius_error=0.0
        max_trace_identity_error=0.0
        for _ in range(samples):
            if label=='Haar_control':
                g=(rng.standard_normal((n,n))+1j*rng.standard_normal((n,n)))/np.sqrt(2)
                q,r=np.linalg.qr(g)
                diagonal=np.diag(r)
                u=q*(diagonal/np.abs(diagonal))[None,:]
            else:
                phases=np.exp(2j*np.pi*rng.random(n))
                u=phases[:,None]*s
            eigen=eigvals(u,overwrite_a=True,check_finite=False)
            max_radius_error=max(max_radius_error,float(np.max(np.abs(np.abs(eigen)-1))))
            trace=np.array([np.sum(eigen**m) for m in powers])
            if label=='symplectic':
                error=float(abs(trace[powers.index(2)]-trace[powers.index(1)]**2))
                max_trace_identity_error=max(max_trace_identity_error,error)
            intensities.append(np.abs(trace)**2/n)
        values=np.array(intensities)
        assert max_radius_error<1e-10
        assert max_trace_identity_error<1e-7
        means=values.mean(axis=0)
        se=values.std(axis=0,ddof=1)/np.sqrt(samples)
        summary=[{'m':m,'m_over_N':m/n,'mean':float(means[j]),'standard_error':float(se[j]),
                  'CUE_reference':min(m,n)/n} for j,m in enumerate(powers)]
        records.append({'ensemble':label,'N':n,'samples':samples,'seed_stream':'single sequential PCG64 stream',
                        'unitarity_Frobenius_error':unitarity,'max_radius_error':max_radius_error,
                        'max_t2_identity_error':max_trace_identity_error,'summary':summary,
                        'raw_intensities':values.tolist()})
        print(json.dumps({'ensemble':label,'N':n,'samples':samples,
                          'at_half_time':min(summary,key=lambda r:abs(r['m_over_N']-.5)),
                          'at_Heisenberg_time':next(r for r in summary if r['m']==n)}),flush=True)
    result={'status':'passed','meaning_of_passed':'Construction checks only, not universality',
            'records':records,'scope':'Finite sampled numerical evidence at fixed N; no asymptotic conclusion'}
    Path(destination).parent.mkdir(parents=True,exist_ok=True)
    Path(destination).write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main(sys.argv[1])
