#!/usr/bin/env python3
"""Independent finite tests of a noncommuting return-word coboundary.

The proof is analytic. Exact rational support certificates and free-word
identities are distinct from floating-point unitary and ODE falsifiers.
No finite residual is promoted to an all-orders convergence estimate.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction as F
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import platform
import subprocess
import time
import numpy as np
from scipy.linalg import eigh, expm, svdvals
from scipy.integrate import solve_ivp
S=np.array([[3,4],[2,3]],dtype=np.int64);T=S.T;R=1/96;Z=5/11
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def exact_geometry():
    r=F(1,96);z=(F(5,11),F(0));mat=((1,0),(0,1));tests=[]
    for k in range(1,4):
        mat=tuple(tuple(sum(int(S[i,l])*mat[l][j] for l in range(2)) for j in range(2)) for i in range(2));radii=tuple(r*(1+sum(abs(x) for x in row)) for row in mat);normals=((1,0),(0,1),(-mat[1][0],mat[0][0]),(-mat[1][1],mat[0][1]));rows=[];ranges=[]
        for sign in (-1,1):
            center=tuple(dot(mat[i],z)-sign*z[i] for i in range(2));bounds=[(math.ceil(center[i]-radii[i]),math.floor(center[i]+radii[i])) for i in range(2)];ranges.append({'sign':sign,'bounds':bounds})
            for n in product(*(range(lo,hi+1) for lo,hi in bounds)):
                delta=tuple(F(n[i])-center[i] for i in range(2));witnesses=[]
                for w in normals:
                    lhs=abs(dot(w,delta));rhs=r*(sum(abs(sum(w[i]*mat[i][j] for i in range(2))) for j in range(2))+sum(abs(x) for x in w))
                    if lhs>rhs:witnesses.append({'normal':w,'lhs':str(lhs),'rhs':str(rhs),'gap':str(lhs-rhs)})
                assert witnesses,(k,sign,n);rows.append({'sign':sign,'translate':n,**witnesses[0]})
        tests.append({'power':k,'matrix':mat,'candidate_ranges':ranges,'separations':rows})
    gap=min(2*z[0]%1,(-2*z[0])%1)-2*r;assert gap==F(37,528);assert sum(len(x['separations']) for x in tests)==30
    return {'center':['5/11','0'],'radius':'1/96','base_lobe_gap':str(gap),'four_level_area_bound':str(32*r*r),'tests':tests}
def beta(t):
    t=np.asarray(t,dtype=float);out=np.zeros_like(t);m=np.abs(t)<1;out[m]=np.exp(1-1/(1-t[m]**2));return out
def dbeta(t):
    t=np.asarray(t,dtype=float);out=np.zeros_like(t);m=np.abs(t)<1;u=t[m];out[m]=-2*u*beta(u)/(1-u*u)**2;return out
def wrap(x):return (np.asarray(x)+.5)%1-.5
def base_factors(q):
    u=wrap(np.asarray(q)-Z)/R;v=wrap(np.asarray(q)+Z)/R;a=beta(u)+beta(v);b=u*beta(u)-v*beta(v);da=(dbeta(u)+dbeta(v))/R;db=(beta(u)+u*dbeta(u)-beta(v)-v*dbeta(v))/R;return a,b,da,db
def gradients(z):
    aq,bq,da,db=base_factors(z[0]);p=wrap(z[1])/R;bp=beta(p);dp=dbeta(p)/R;return np.array([da*bp,aq*dp],float),np.array([db*bp,bq*dp],float)
def grad_at(z,j,which):
    sj=np.linalg.matrix_power(S,j);ga,gb=gradients(sj@z);return sj.T@(ga if which=='a' else gb)
def grad_f(z):return grad_at(z,0,'a')+grad_at(z,1,'b')-grad_at(z,1,'a')+grad_at(z,2,'a')-grad_at(z,2,'b')-grad_at(z,3,'a')
def field(grad):
    def f(z):v=grad(z);return np.array([v[1],-v[0]])
    return f
def ode_controls():
    def flow(grad,z,t):
        ans=solve_ivp(lambda _,x:field(grad)(x),(0,t),np.asarray(z,float),method='DOP853',rtol=2e-11,atol=2e-13,max_step=max(abs(t)/16,1e-9));assert ans.success,ans.message;return ans.y[:,-1]
    grads=[lambda z:grad_at(z,0,'a'),lambda z:grad_at(z,1,'b')-grad_at(z,1,'a'),lambda z:grad_at(z,1,'a'),lambda z:grad_at(z,2,'a')]
    def psi(z,t,inverse=False):
        order=grads if inverse else reversed(grads)
        for grad in order:z=flow(grad,z,-t if inverse else t)
        return z
    points=[]
    for j in range(4):
        sj=np.linalg.matrix_power(S,j)
        for off in ((.1,.3),):points.append(np.linalg.solve(sj,np.array([Z+R*off[0],R*off[1]])))
    rows=[]
    for kappa in (-2e-6,1e-6):
        for x in points:
            direct=S@flow(grad_f,x,-kappa);conj=psi(S@psi(x,kappa,True),kappa);err=float(np.max(abs(wrap(direct-conj))));assert err<4e-8,(kappa,x,err);rows.append({'kappa':kappa,'point':x.tolist(),'circle_error':err,'displacement':float(np.max(abs(wrap(direct-S@x))))})
    z=np.array([Z,R/2]);ga,gb=gradients(z);p=float(np.linalg.det(np.stack([ga,gb])));expected=float(-beta(.5)*dbeta(.5)/R**2);assert abs(p-expected)<1e-9 and p>1;assert max(row['displacement'] for row in rows)>.001
    return {'method':'DOP853 finite falsifiers, not interval-certified','nonzero_base_bracket':p,'explicit_bracket_value':expected,'rows':rows}
def cat(n):
    x=np.arange(n,dtype=np.int64);a=((3*x[:,None]**2-2*x[:,None]*x[None,:]+3*x[None,:]**2)*pow(8,-1,n))%n;return np.exp(2j*np.pi*a/n)/np.sqrt(n)
def weyl(n,a,b):
    x=np.arange(n,dtype=np.int64);out=np.zeros((n,n),complex);out[x,(x-b)%n]=np.exp(1j*np.pi*((2*a*x-a*b)%(2*n))/n);return out
def separable(n,a,b):
    x=np.arange(n);mid=(x[:,None]+x[None,:])/(2*n);diff=x[:,None]-x[None,:];bhat=np.fft.fft(b(np.arange(2*n)/(2*n)))/(2*n);return a(mid)*bhat[diff%(2*n)]+a(mid-.5)*bhat[(diff+n)%(2*n)]
def norm(a):return float(svdvals(a,check_finite=False)[0])
def exp_h(a,e):
    assert norm(a-a.conj().T)<1e-10;vals,vec=eigh((a+a.conj().T)/2,check_finite=False);return (vec*np.exp(1j*e*vals))@vec.conj().T
def nodal_controls():
    rows=[]
    for n in (7,9,17,31):
        aa={1:.5,-1:.5,3:.125j,-3:-.125j,n+2:.1,-n-2:.1};bb={2:.3,-2:.3,2*n+1:.2,-2*n-1:.2};af=lambda q:sum(c*np.exp(2j*np.pi*k*q) for k,c in aa.items());bf=lambda p:sum(c*np.exp(2j*np.pi*k*p) for k,c in bb.items());direct=sum(c*d*weyl(n,a,b) for a,c in aa.items() for b,d in bb.items());got=separable(n,af,bf);err=norm(got-direct);assert err<5e-13;x=np.arange(n);bad=af((x[:,None]+x[None,:])/(2*n))*(np.fft.fft(bf(x/n))/n)[(x[:,None]-x[None,:])%n];neg=norm(bad-direct);assert neg>.05;rows.append({'N':n,'two_grid_error':err,'one_grid_negative_control':neg})
    return rows
def block_controls():
    a=np.array([[1,.3-.2j],[.3+.2j,-.4]],complex);b=np.array([[.2,.8+.1j],[.8-.1j,.7]],complex);eye=np.eye(2);zero=np.zeros((2,2),complex);u=np.kron(np.roll(np.eye(4),1,axis=0),eye)
    def diag(xs):
        out=np.zeros((8,8),complex)
        for j,x in enumerate(xs):out[2*j:2*j+2,2*j:2*j+2]=x
        return out
    g=diag([a,b,a,zero]);cg=u@g@u.conj().T;assert norm(g@cg-cg@g)>.1;avg=sum(np.linalg.matrix_power(u,k)@(g@cg-cg@g)@np.linalg.matrix_power(u.conj().T,k) for k in range(4));assert norm(avg)<1e-14;rows=[]
    for e in (-3.,-.2,.7,2.5):
        x=expm(1j*e*a);y=expm(1j*e*(b-a));j=diag([x,y@x,x,eye]);v=expm(1j*e*(g-cg))@u;err=norm(v-j@u@j.conj().T);assert err<2e-14;linear=expm(1j*e*g);neg=norm(v-linear@u@linear.conj().T);assert neg>1e-3;rows.append({'exponent':e,'return_word_gauge_error':err,'linear_gauge_negative_control':neg})
    return rows
def matrix_case(n):
    start=time.monotonic();u=cat(n);a=separable(n,lambda q:base_factors(q)[0],lambda p:beta(wrap(p)/R));b=separable(n,lambda q:base_factors(q)[1],lambda p:beta(wrap(p)/R));assert norm(a-a.conj().T)<1e-12 and norm(b-b.conj().T)<1e-12;a=(a+a.conj().T)/2;b=(b+b.conj().T)/2
    def C(x):return u@x@u.conj().T
    aa=[a];bb=[b]
    for _ in range(3):aa.append(C(aa[-1]));bb.append(C(bb[-1]))
    hs=[aa[0],bb[1]-aa[1],aa[2]-bb[2],-aa[3]];f=sum(hs);g=aa[0]+bb[1]+aa[2];cg=C(g);assert norm(f-g+cg)<1e-12;maxcomm=0.
    for i in range(4):
        for j in range(i+1,4):
            for h in (aa[i],bb[i]-aa[i]):
                for k in (aa[j],bb[j]-aa[j]):maxcomm=max(maxcomm,norm(h@k-k@h))
    comm=norm(g@cg-cg@g);rows=[]
    for kappa in (-.002,.002,.02):
        e=2*math.pi*n*kappa;x=exp_h(a,e);y=exp_h(b-a,e);j=x@C(y@x)@C(C(x));v=exp_h(f,e)@u;err=norm(v-j@u@j.conj().T);bound=e*e*4**4*maxcomm;assert err<=bound+3e-10;linear=exp_h(g,e);negative=norm(v-linear@u@linear.conj().T);rows.append({'kappa':kappa,'exponent':e,'nonlinear_gauge_error':err,'conservative_cross_site_bound':bound,'linear_gauge_error':negative})
    return {'N':n,'principal_pair_commutator_norm':comm,'max_cross_site_commutator_norm':maxcomm,'rows':rows,'seconds':time.monotonic()-start}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);p.add_argument('--sizes',default='63,127,255,511');p.add_argument('--cpp',type=Path);args=p.parse_args();data={'status':'RUNNING','producer':'computations/verification/noncommuting_tower.py','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':platform.python_version(),'numpy':np.__version__,'scope':'Exact rational support separation; finite noncommuting block identity; exact-formula nodal matrices and floating ODE/unitary checks. No numerical proof of asymptotic order, priority, or BGS.'};data['geometry']=exact_geometry();data['nodal']=nodal_controls();data['blocks']=block_controls();data['classical']=ode_controls();data['matrices']=[]
    if args.cpp:
        other=json.loads(subprocess.check_output([str(args.cpp.resolve())],text=True,timeout=30));assert other['geometry_obligations']==30 and other['free_word_tests']==11;data['cpp']=other
    for n in (int(s) for s in args.sizes.split(',') if s):data['matrices'].append(matrix_case(n))
    data['status']='PASS';text=json.dumps(data,indent=2)+'\n'
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text)
    else:print(text)
if __name__=='__main__':main()
