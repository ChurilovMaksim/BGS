"""Exploratory echo traces of actual odd Pell propagators, not a proof."""
import json, math, sys, time
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'computations/verification'))
from pell_harmonic_returns import odd_operators
from pell_harmonic_transition import design

class Map:
    def __init__(self,k,a):
        self.k=k
        self.n,f,_,h=design(k)
        self.d=(self.n-1)//2
        x=np.arange(self.n,dtype=np.int64)
        q=-a*a*f % self.n
        c=q*pow(2,-1,self.n)%self.n
        self.chirp=np.exp(2j*np.pi*((c*((x*x)%self.n))%self.n)/self.n)[:,None]
        self.cos=(2*np.cos(2*np.pi*x/self.n))[:,None]
        self.perm=h*x%self.n
        self.inverse=pow(h,-1,self.n)*x%self.n
    def embed(self,z):
        v=np.zeros((self.n,z.shape[1]),complex)
        v[1:self.d+1]=z/math.sqrt(2)
        v[-self.d:]=-z[::-1]/math.sqrt(2)
        return v
    def kick(self,v,tau):
        e=tau/math.sqrt(2*self.k)
        return self.chirp*np.fft.ifft(np.exp(1j*e*self.cos)*np.fft.fft(v/self.chirp,axis=0),axis=0)
    def ret(self,v,tau,adjoint=False):
        for _ in range(self.k):
            v=self.kick(v,-tau)[self.inverse] if adjoint else self.kick(v[self.perm],tau)
        return v
    def echo(self,v,t,s):
        return self.ret(self.ret(v,s,True),t)

def controls():
    err=0
    for k,a in ((3,1),(5,2)):
        fast=Map(k,a)
        b,u=odd_operators(k,a)
        w,v=np.linalg.eigh(b)
        tau=.7
        dense=np.linalg.matrix_power((v*np.exp(1j*tau*w/math.sqrt(2*k)))@v.conj().T@u,k)
        basis=fast.embed(np.eye(fast.d))
        got=basis.conj().T@fast.ret(basis,tau)
        adj=basis.conj().T@fast.ret(basis,tau,True)
        err=max(err,float(np.max(abs(got-dense))),float(np.max(abs(adj-dense.conj().T))))
    assert err<1e-11
    return err

start=time.monotonic()
rng=np.random.default_rng(20260913)
rows=[]
for k in (7,11,13):
    n,_,_,_=design(k)
    allowed=np.array([a for a in range(1,math.isqrt(n)+1) if math.gcd(a,n)==1])
    aa=allowed if k==7 else rng.choice(allowed,size=8,replace=False)
    probes=8
    d=(n-1)//2
    for a in aa:
        op=Map(k,int(a))
        z=op.embed(rng.choice([1.,-1.,1j,-1j],size=(d,probes)))
        for t,s in ((1.,0.),(1.6,.6)):
            v=op.echo(z,t,s)
            first=np.sum(z.conj()*v,axis=0)/d
            second=np.sum(z.conj()*op.echo(v,t,s),axis=0)/d
            rows.append({'K':k,'N':n,'a':int(a),'tau':t,'sigma':s,
                         'first':[float(first.mean().real),float(first.mean().imag)],
                         'second':[float(second.mean().real),float(second.mean().imag)],
                         'trace_rms_bound':1/math.sqrt(d*probes)})
        print(k,int(a),flush=True)
result={'dense_control_max_error':controls(),'seed':20260913,'probes':8,
        'scope':'sampled harmonics and stochastic normalized trace, not interval-certified',
        'seconds':time.monotonic()-start,'rows':rows}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
for k in (7,11,13):
    for t in (1.,1.6):
        rr=[r for r in rows if r['K']==k and r['tau']==t]
        print(json.dumps({'K':k,'tau':t,'samples':len(rr),
              'mean_first':np.mean([r['first'] for r in rr],axis=0).tolist(),
              'mean_second':np.mean([r['second'] for r in rr],axis=0).tolist()}))
print('dense_control',result['dense_control_max_error'],'seconds',result['seconds'])
