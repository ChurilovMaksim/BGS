"""Actual circular-phase two-port scattering; basis rotations are paired controls."""
import itertools
import json
import math
import sys
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import solve

SEED=202610181811


def seed_matrix(p,d,symmetric=False):
    if symmetric:
        n=p**(2*d)
        x=np.arange(n)
        return np.exp(2j*np.pi*np.outer(x,x)/n)/math.sqrt(n)
    vertices=np.array(list(itertools.product(range(p),repeat=2*d)),dtype=np.int64)
    q=vertices[:,:d];v=vertices[:,d:]
    phase=(q@v.T-v@q.T)%p
    return np.exp(2j*np.pi*phase/p)/math.sqrt(len(vertices))


def stats(values):
    values=np.asarray(values)
    return {'mean':float(values.mean()),'standard_error':float(values.std(ddof=1)/math.sqrt(len(values)))}


def summarize(matrices,rotations):
    raw={}
    for name,w in rotations.items():
        changed=w[None,:,:]@matrices@w.conj().T[None,:,:]
        raw[name]=np.abs(changed[:,0,1])**2
    result={}
    for name,t in raw.items():
        centered=2*t-1
        result[name]={'T':stats(t),'T2':stats(t*t),'P2':stats((3*centered**2-1)/2),
                      'P3':stats((5*centered**3-3*centered)/2),
                      'paired_difference':stats(t-raw['identity']),
                      'raw_T':t.tolist()}
    return result


def main(destination):
    rng=np.random.Generator(np.random.PCG64(SEED))
    r=math.sqrt(.5)
    rotations={
        'identity':np.eye(2,dtype=complex),
        'real':np.array([[r,r],[-r,r]],dtype=complex),
        'complex':np.array([[r,1j*r],[1j*r,r]],dtype=complex),
        'generic':np.array([[math.cos(.37),np.exp(.83j)*math.sin(.37)],
                           [-np.exp(-.83j)*math.sin(.37),math.cos(.37)]])
    }
    records=[]
    cases=[(3,1,4000,False),(5,1,3000,False),(3,2,2400,False),
           (5,2,160,False),(3,3,160,False),(3,2,1200,True)]
    for p,d,samples,symmetric in cases:
        s=seed_matrix(p,d,symmetric)
        n=len(s)
        assert np.linalg.norm(s@s.conj().T-np.eye(n))<1e-9
        a=s[:2,:2];b=s[:2,2:];c=s[2:,:2];e=s[2:,2:]
        matrices=[];worst_unitarity=0.;worst_residual=0.
        for _ in range(samples):
            phase=np.exp(2j*np.pi*rng.random(n-2))
            coefficient=np.eye(n-2)-phase[:,None]*e
            rhs=phase[:,None]*c
            x=solve(coefficient,rhs,assume_a='gen',check_finite=False)
            f=a+b@x
            residual=float(np.linalg.norm(coefficient@x-rhs)/(1+np.linalg.norm(rhs)))
            error=float(np.linalg.norm(f@f.conj().T-np.eye(2)))
            worst_unitarity=max(worst_unitarity,error)
            worst_residual=max(worst_residual,residual)
            assert error<1e-7 and residual<1e-10
            matrices.append(f)
        matrices=np.array(matrices)
        if symmetric:assert np.max(np.abs(matrices-matrices.transpose(0,2,1)))<1e-7
        records.append({'N':n,'p':p,'d':d,'samples':samples,
                        'ensemble':'excluded_symmetric' if symmetric else 'actual_symplectic',
                        'unitarity_error_max':worst_unitarity,'linear_residual_max':worst_residual,
                        'statistics':summarize(matrices,rotations)})
    matrices=[]
    for _ in range(4000):
        g=(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)))/math.sqrt(2)
        q,rmat=np.linalg.qr(g)
        q=q*(np.diag(rmat)/np.abs(np.diag(rmat)))[None,:]
        matrices.append(q)
    records.append({'N':2,'samples':len(matrices),'ensemble':'haar_U2_control',
                    'statistics':summarize(np.array(matrices),rotations)})
    output={'status':'passed','seed':SEED,'generator':'NumPy PCG64',
            'versions':{'numpy':np.__version__,'scipy':scipy.__version__},
            'records':records,'rotations':{k:[[[float(z.real),float(z.imag)] for z in row] for row in w] for k,w in rotations.items()},
            'scope':'Construction checks and finite paired moments; no asymptotic counterexample or universality theorem from sampling'}
    Path(destination).write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':'passed','records':[
        {'N':r['N'],'ensemble':r['ensemble'],'samples':r['samples'],
         'T':{k:v['T'] for k,v in r['statistics'].items()},
         'P2':{k:v['P2'] for k,v in r['statistics'].items()}} for r in records]}))


if __name__=='__main__':main(sys.argv[1])
