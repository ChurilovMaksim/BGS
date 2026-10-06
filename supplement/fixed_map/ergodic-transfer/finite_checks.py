"""Finite diagnostics for ergodic_spectral_transfer.md.

Random unitaries are algebraic test fixtures, not a proof about a fixed map.
Cat fixtures deliberately include large eigenspace degeneracies. Exact
counterexamples distinguish needed assumptions from purely numerical fit.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json
from pathlib import Path
import sys
from fractions import Fraction as F
import numpy as np
from scipy.linalg import schur
from scipy.optimize import linear_sum_assignment
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'design-return'))
from frozen_sharp_return import coefficients
from sparse_orbit_checks import pell


def hs(a):return np.linalg.norm(a,'fro')/np.sqrt(a.shape[0])


def expi(a,t):
    w,v=np.linalg.eigh(a)
    return (v*np.exp(1j*t*w))@v.conj().T


def clock_angles(u):return np.angle(np.linalg.eigvals(u))/(2*np.pi)


def match(u,v,C):
    n=len(u);x=clock_angles(u);y=clock_angles(v)
    delta=n*((y[None,:]-x[:,None]+.5)%1-.5)
    costs=delta**2
    costs[np.abs(delta)>C/(2*np.pi)+2e-10]=np.inf
    rows,cols=linear_sum_assignment(costs)
    d=delta[rows,cols]
    return x*n,d


def pair(x):
    n=len(x);dist=(x[:,None]-x[None,:]+n/2)%n-n/2
    t=(dist-1)/.4
    values=np.zeros_like(t);inside=np.abs(t)<1
    values[inside]=np.exp(1-1/(1-t[inside]**2))
    np.fill_diagonal(values,0)
    return float(values.sum()/n)


def fixture(u,a,label,Tvalues,sharp_sigma=None):
    n=len(u);a=a-np.trace(a).real/n*np.eye(n)
    C=float(np.max(np.abs(np.linalg.eigvalsh(a))))
    v=expi(a,1/n)@u
    x,d=match(u,v,C)
    rms=float(np.sqrt(np.mean(d*d)))
    bounds=[]
    for T in Tvalues:
        term=a.copy();avg=np.zeros_like(a)
        for _ in range(T):
            avg+=term/T;term=u.conj().T@term@u
        vt=hs(avg)
        upper=(vt+C*C*(T-1)/n)/(2*np.pi)
        assert rms<=upper+1e-10
        # Orthogonal Schur vectors avoid a nonorthogonal eigenbasis inside
        # the degenerate cat eigenspaces.
        worst=0.
        for s in (0.,.37,1.):
            us=expi(a,s/n)@u
            tri,vec=schur(us,output='complex')
            assert np.linalg.norm(tri-np.diag(np.diag(tri)),'fro')<1e-10
            variance=float(np.mean(np.abs(np.diag(vec.conj().T@a@vec))**2))
            worst=max(worst,variance)
            assert variance<=(vt+C*C*(T-1)/n)**2+1e-10
        bounds.append(dict(T=T,time_average_HS=float(vt),RMS_upper=float(upper),
                           sampled_path_variance_max=worst))
    actual_pair_change=abs(pair(x+d)-pair(x))
    L=2*(1.4+2*C/(2*np.pi))
    distance=np.abs((x[:,None]-x[None,:]+n/2)%n-n/2)
    moment2=float(np.mean(np.sum(distance<=L,axis=1)**2))
    pair_bound=20*rms*np.sqrt(moment2)
    assert actual_pair_change<=pair_bound+1e-10
    result=dict(label=label,N=n,RMS_unfolded_displacement=rms,
                max_unfolded_displacement=float(np.max(np.abs(d))),
                allowed_max=C/(2*np.pi),bounds=bounds,
                pair_change=actual_pair_change,pair_transfer_upper=float(pair_bound))
    if sharp_sigma is not None:
        K,sigma=sharp_sigma
        result['Pell_first_order_RMS']=float(sigma/(2*np.pi*np.sqrt(K)))
        result['ratio_to_Pell_first_order']=float(rms/result['Pell_first_order_RMS'])
    return result


def cat(k):
    n,_=pell(k);x=np.arange(n);X=x[:,None];Y=x[None,:]
    m=np.exp(2j*np.pi*((-pow(8,-1,n)*(3*X*X-2*X*Y+3*Y*Y))%n)/n)/np.sqrt(n)
    den,coeff=coefficients();a=np.zeros((n,n),complex)
    for (p,q),(re,im) in coeff.items():
        a[x,(x+p)%n]+=(re+1j*im)/den*np.exp(2j*np.pi*((q*(x+p*pow(2,-1,n)))%n)/n)
    return fixture(m,a,'Pell cat with frozen centred observable',
                   sorted(set((1,2,k))),
                   sharp_sigma=(k,np.sqrt(1650797/4000000)))


def failure_controls():
    clustered=[]
    for m in (8,16,32):
        n=m*m;a=.2
        background=np.linspace(10,n-10,n-m)
        x=np.r_[np.zeros(m),background]
        d=np.r_[np.full(m//2,a),np.full(m//2,-a),np.zeros(n-m)]
        def nearzero(z):
            differences=np.abs((z[:,None]-z[None,:]+n/2)%n-n/2)
            # For these fixtures all supported differences are exactly zero.
            mask=(differences<a)&(~np.eye(n,dtype=bool))
            assert np.all(differences[mask]<1e-12)
            return int(mask.sum())
        before=F(nearzero(x),n);after=F(nearzero(x+d),n)
        assert before==1-F(1,m) and after==F(1,2)-F(1,m)
        assert before-after==F(1,2)
        clustered.append(dict(N=n,RMS_squared_exact=str(F(1,25*m)),
                              pair_before=str(before),pair_after=str(after),
                              cluster_third_factorial_mass=str(F(m*(m-1)*(m-2),n))))
    n=64;a=.2;x=np.arange(n,dtype=float);d=a*(-1.)**np.arange(n)
    assert abs(pair(x)-1)<1e-12 and abs(pair(x+d))<1e-12
    endpoint=[]
    for n0 in (32,64,128,512):
        alpha=np.pi/n0
        sigma=np.array([[0.,1.],[1.,0.]])
        block=np.diag(np.exp(1j*np.array([alpha,-alpha])))
        angles=np.sort(np.angle(np.linalg.eigvals(expi(sigma,1/n0)@block)))
        beta=np.arccos(np.cos(1/n0)*np.cos(alpha))
        assert np.max(np.abs(angles-np.array([-beta,beta])))<1e-12
        shift=(n0*beta-np.pi)/(2*np.pi)
        endpoint.append(dict(N=n0,initial_diagonal_variance=0,
                             RMS_displacement=float(shift),
                             T4_average_norm=float(abs(np.sin(4*alpha)/(4*np.sin(alpha))))))
    return dict(rare_clusters=clustered,zero_endpoint_variance=endpoint,
                endpoint_RMS_limit=float((np.sqrt(np.pi*np.pi+1)-np.pi)/(2*np.pi)),
                commuting_clock=dict(N=n,a=a,
                RMS=a,pair_before=pair(x),pair_after=pair(x+d),
                time_average_HS=2*np.pi*a))


def run():
    rng=np.random.default_rng(20260918);fixtures=[]
    for n in (31,63,127):
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        q,r=np.linalg.qr(z);u=q*(np.diag(r)/np.abs(np.diag(r)))
        x=np.arange(n)/n
        a=np.diag(np.cos(2*np.pi*x)+.3*np.sin(4*np.pi*x)).astype(complex)
        fixtures.append(fixture(u,a,'Seeded unitary finite fixture',(1,2,4,8,16)))
    fixtures.extend(cat(k) for k in (5,7))
    return dict(fixtures=fixtures,failure_controls=failure_controls(),
                scope='Finite checks only; analytic limit and comparison assumptions are in the proof')


if __name__=='__main__':print(json.dumps(run(),indent=2))
