#!/usr/bin/env python3
"""Finite algebra controls for BGS-FLOW-004--006 and FM-013.

Deterministic complex128 basis checks, N<=13; seeded finite matrix-moment
controls; exact integer parity. No Monte Carlo, asymptotic certificate,
BGS simulation, original coboundary diffusion limit, or Lean proof.
Run from any directory; --output stores the complete JSON evidence.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.linalg import expm
from quadratic_coboundary_noise import hermitian_basis, parameters

def covariance(u, basis):
    n = len(u); us = u.conj().T; q = np.trace(u@u)/n
    tr = np.einsum('jk,akj->a', u@u, basis)
    applied = basis/n-(q*(us@basis@us)+q.conjugate()*(u@basis@u))/(2*n)
    applied += (tr[:, None, None]*(us@us)+tr.conj()[:, None, None]*(u@u))/(2*n*n)
    return np.einsum('ajk,bkj->ab', basis, applied).real

def check_coupling():
    worst = dict(commutator=0., relative_drift=0., matrix_variance=0., root_square=0.)
    rows = []
    for n in (2,3,4,5,7):
        bs = hermitian_basis(n, traceless=True); dim = len(bs)
        f = np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
        configurations = {
            'irregular': np.linspace(.1, 5., n)**1.13,
            'clock': 2*np.pi*np.arange(n)/n,
            'scalar': np.zeros(n),
            'antipodal': np.pi*(np.arange(n)%2),
            'clustered': (2*np.pi/3)*(np.arange(n)%3)+1e-4*np.arange(n),
        }
        v = expm(1j*(bs[0]+.3*bs[-1]))
        for name, theta in configurations.items():
            u = f@np.diag(np.exp(1j*theta))@f.conj().T
            c = covariance(u, bs); c = (c+c.T)/2
            eig, vec = np.linalg.eigh(c)
            assert min(eig)>-2e-13
            root = (vec*np.sqrt(np.maximum(eig,0)))@vec.T
            rooterr = np.max(abs(root@root-c))
            ka = np.einsum('ab,ajk->bjk', root, bs)
            ba = bs/np.sqrt(n); ea = ka-ba
            cross = np.einsum('ajk,akl->jl', ba, ea)
            commerr = np.max(abs(cross-cross.conj().T))
            qk = np.einsum('ajk,akl->jl',ka,ka)
            qe = np.einsum('ajk,akl->jl',ea,ea)
            qb = (1-1/n**2)*np.eye(n)
            m1 = np.trace(u)/n; q = np.trace(u@u)/n
            z = q*m1.conjugate()*u.conj().T
            qpred = np.eye(n)-(z+z.conj().T)/2
            qerr = np.max(abs(qk-qpred))
            # Ito drift of Z=V*U from product rule versus residual noise alone.
            mixed = np.einsum('ajk,akl->jl', ba, ka)
            direct = v.conj().T@(-.5*qb-.5*qk+mixed)@u
            expected = -.5*v.conj().T@qe@u
            drifterr = np.max(abs(direct-expected))
            energy = np.trace(qe).real
            bound = 2*n*abs(q)**2+2/n
            assert energy <= bound+1e-11
            assert np.linalg.eigvalsh(qe)[-1] <= 2*abs(q)**2+2/n**2+1e-11
            assert max(rooterr, commerr, qerr, drifterr)<1e-11
            # Independently exercise the global low-harmonic drift inequality.
            a=m1; b=q; c3=np.trace(np.linalg.matrix_power(u,3))/n
            la=-a/2+b*a.conjugate()/4+abs(b)**2*a/4
            lb=-b/2-a*a+(b*abs(a)**2+b.conjugate()*(a*c3+b*b))/2
            d1=2*np.real(a.conjugate()*la)
            d2=2*np.real(b.conjugate()*lb)
            assert d1<=1e-12
            assert d2<=3*abs(a)**2+abs(b)**2+1e-12
            for key,val in [('commutator',commerr),('relative_drift',drifterr),('matrix_variance',qerr),('root_square',rooterr)]:
                worst[key]=max(worst[key],float(val))
            rows.append((n,name,float(energy/bound)))
    return {'cases':len(rows),'max_errors':worst,'max_energy_to_bound':max(r[2] for r in rows)}

def check_traces():
    worst=dict(drift=0.,carr_conj=0.,carr_plain=0.,gradient=0.,corrected_drift=0.)
    cases=0
    for n in (3,4,5,7):
        bs=hermitian_basis(n, traceless=True)
        dft=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
        for theta in (np.linspace(.1,5.,n)**1.13,2*np.pi*np.arange(n)/n,np.zeros(n)):
            u=dft@np.diag(np.exp(1j*theta))@dft.conj().T
            us=u.conj().T
            powers={k:np.linalg.matrix_power(u,k) for k in range(-16,17)}
            p=lambda k:np.trace(powers[k])
            m=lambda k:p(k)/n
            q=m(2)
            tr=np.einsum('jk,akj->a',u@u,bs)
            applied=bs/n-(q*(us@bs@us)+q.conjugate()*(u@bs@u))/(2*n)
            applied+=(tr[:,None,None]*(us@us)+tr.conj()[:,None,None]*(u@u))/(2*n*n)
            c=np.einsum('ajk,bkj->ab',bs,applied).real
            c=(c+c.T)/2
            vals,vec=np.linalg.eigh(c)
            assert min(vals)>-1e-12
            root=(vec*np.sqrt(np.maximum(vals,0)))@vec.T
            ka=np.einsum('ab,ajk->bjk',root,bs)
            for k in range(1,7):
                direct=-k/2*sum(np.trace(a@powers[l]@a@powers[k-l]) for a in ka for l in range(k))
                pred=-k/(2*n)*sum(p(l)*p(k-l) for l in range(k))
                pred+=k/(4*n*n)*(p(2)*sum(p(l-1)*p(k-l-1) for l in range(k))+p(-2)*sum(p(l+1)*p(k-l+1) for l in range(k)))
                worst['drift']=max(worst['drift'],abs(pred-direct)); cases+=1
                cv=m(2)+m(1)**2/2; dv=m(2)*m(-1)/2
                val=cv*(us@us)+dv*us
                correction=-(val-val.conj().T)/(2j)
                delta_direct=1j*k*np.trace(correction@powers[k])
                delta_pred=-k/2*(cv*p(k-2)-cv.conjugate()*p(k+2)+dv*p(k-1)-dv.conjugate()*p(k+1))
                worst['corrected_drift']=max(worst['corrected_drift'],abs(delta_direct-delta_pred))
                dk=np.array([1j*k*np.trace(a@powers[k]) for a in ka])
                for l in range(1,7):
                    dl=np.array([1j*l*np.trace(a@powers[l]) for a in ka])
                    bil=lambda b: m(k+b)-(q*m(k+b-2)+q.conjugate()*m(k+b+2))/2-m(k)*m(b)+(m(b+2)*m(k-2)+m(b-2)*m(k+2))/2
                    worst['carr_conj']=max(worst['carr_conj'],abs(np.dot(dk,dl.conj())-k*l*bil(-l)))
                    worst['carr_plain']=max(worst['carr_plain'],abs(np.dot(dk,dl)+k*l*bil(l)))
            z=np.exp(1j*theta)
            grad=-np.imag((m(2)+m(1)**2/2)*z.conj()**2+(m(2)*m(-1)/2)*z.conj())
            def potential(th):
                z=np.exp(1j*th); p1=z.sum(); p2=(z*z).sum()
                return abs(p2)**2+(p2*p1.conjugate()**2).real/n
            step=1e-5
            num=np.array([(potential(theta+step*np.eye(n)[j])-potential(theta-step*np.eye(n)[j]))/(2*step) for j in range(n)])
            worst['gradient']=max(worst['gradient'],np.max(abs(grad+num/(4*n))))
    assert max(worst[k] for k in ('drift','carr_conj','carr_plain','corrected_drift'))<1e-10
    assert worst['gradient']<1e-9
    return {'drift_cases':cases,'max_errors':{k:float(v) for k,v in worst.items()}}

def check_reversibility():
    radial=second=full=0.
    for n in (2,3,4,7,13):
     t=np.linspace(.1,5.,n)**1.13;z,q,d,v,sig=parameters(t);m1=np.mean(z)
     mask=~np.eye(n,dtype=bool);cot=np.zeros_like(d);cot[mask]=1/np.tan(d[mask]/2)
     bx=.5*np.sum(v*cot,axis=1)
     corr=-np.imag((q+m1*m1/2)/z**2+q*np.conj(m1)/(2*z))
     div=np.zeros(n);h=1e-5
     for k in range(n):
      tp=t.copy();tm=t.copy();tp[k]+=h;tm[k]-=h
      div+=(parameters(tp)[4][:,k]-parameters(tm)[4][:,k])/(2*h)
     rev=.5*(div+sig@cot.sum(axis=1))
     err=np.max(abs(rev-bx-corr)); radial=max(radial,float(err))
     assert err<1e-9
    for n in (2,3,4,7,13):
     t=np.linspace(.1,5.,n)**1.13;z,q,d,v,sig=parameters(t);m=np.mean(z);p={r:sum(z**r) for r in (1,2,3,4)}
     corr=-np.imag((q+m*m/2)/z**2+q*np.conj(m)/(2*z))
     direct=sum(2j*z*z*corr)
     pred=-p[2]-p[1]**2/(2*n)-p[2]*abs(p[1])**2/(2*n*n)+np.conj(p[2])*p[4]/n+np.conj(p[1])**2*p[4]/(2*n*n)+np.conj(p[2])*p[1]*p[3]/(2*n*n)
     assert abs(direct-pred)<1e-12
     second=max(second,float(abs(direct-pred)))

    def cov_op(u,bs):
     n=len(u);q=np.trace(u@u)/n;us=u.conj().T
     tr=np.einsum('jk,akj->a',u@u,bs)
     return bs/n-(q*(us@bs@us)+q.conjugate()*(u@bs@u))/(2*n)-np.trace(bs,axis1=1,axis2=2)[:,None,None]*np.eye(n)/n**2+(tr[:,None,None]*(us@us)+tr.conj()[:,None,None]*(u@u))/(2*n*n)
    for n in (2,3,4):
     theta=np.linspace(.1,5.,n)**1.13
     f=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
     u=f@np.diag(np.exp(1j*theta))@f.conj().T;bs=hermitian_basis(n);co=np.zeros(len(bs));h=1e-5
     for a,ta in enumerate(bs):
      plus=cov_op(expm(1j*h*ta)@u,bs);minus=cov_op(expm(-1j*h*ta)@u,bs)
      co+=.5*np.einsum('jk,bkj->b',ta,(plus-minus)/(2*h)).real
     found=np.einsum('a,ajk->jk',co,bs);m=np.trace(u)/n;q=np.trace(u@u)/n;us=u.conj().T
     val=(q+m*m/2)*(us@us)+q*m.conjugate()*us/2
     expected=-(val-val.conj().T)/(2j)
     err=np.max(abs(found-expected));full=max(full,float(err));assert err<1e-8
    return {'radial_divergence':radial,'second_trace_drift':second,'full_matrix_divergence':full}

def check_moment_and_parity():
    rng=np.random.default_rng(20260929)
    worst=0.; cases=0
    for n in (2,3,5,9):
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); y=(z+z.conj().T)/2
        coeff=[]
        for _ in range(3):
            z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); coeff.append((z+z.conj().T)/2)
        v=np.linalg.eigvalsh(sum(a@a for a in coeff))[-1]
        for p in range(2,9):
            q=2*p-2; bound=v*np.trace(np.linalg.matrix_power(y,q)).real
            for i in range(q+1):
                term=sum(np.trace(np.linalg.matrix_power(y,i)@a@np.linalg.matrix_power(y,q-i)@a) for a in coeff)
                ratio=abs(term)/bound; worst=max(worst,float(ratio)); cases+=1
                assert ratio<=1+1e-12
    inv=np.array([[3,-4],[-2,3]],dtype=object)
    wedge=lambda a,b: a[0]*b[1]-a[1]*b[0]
    grid=[np.array([a,b],dtype=object) for a in range(-2,3) for b in range(-2,3)]
    count=0
    for j in (1,2,3):
        mat=np.linalg.matrix_power(inv,j)
        for n in grid:
            for k in grid:
                lk=mat@k; new=n+(mat-np.eye(2,dtype=object))@k
                phase2=wedge(n,lk)-wedge(k,n+lk)
                assert phase2%2==0 and (new[0]*new[1]-n[0]*n[1])%2==0
                count+=1
    return {'moment_terms':cases,'max_ratio':worst,'integer_parity_cases':count,
            'seed':20260929,'exclusion':'finite controls do not prove moment induction or source-to-model identification'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report={'status':'PASS','arithmetic':'numpy complex128; Python exact integers for parity',
            'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
            'resource_caps':{'max_basis_N':7,'max_radial_N':13,'max_trace_order':6,
                             'max_moment_order':8,'finite_difference_step':1e-5},
            'coupling':check_coupling(),'traces':check_traces(),
            'reversibility':check_reversibility(),'moment_and_parity':check_moment_and_parity(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Finite identities only; no asymptotic theorem certified by execution.'}
    data=json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(data)
    print(data,end='')

if __name__=='__main__':
    main()
