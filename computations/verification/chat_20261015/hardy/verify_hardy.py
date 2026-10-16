#!/usr/bin/env python3
"""Finite verification of a sharp Hardy-space identity for unitary spectra.

No simulation of the physical fixed-coupling asymptotic limit is attempted.
All checks use explicit exceptions and remain active with python -O.
"""
from __future__ import annotations
import argparse
import json
import math
import time
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.linalg import eigh, schur


def require(ok: bool, message: str) -> None:
    if not bool(ok):
        raise AssertionError(message)


def poly_product(roots: list[sp.Expr]) -> list[sp.Expr]:
    out = [sp.Integer(1)]
    for root in roots:
        nxt = [sp.Integer(0)] * (len(out) + 1)
        for k, c in enumerate(out):
            nxt[k] += c
            nxt[k + 1] -= root * c
        out = [sp.simplify(c) for c in nxt]
    return out


def exact_gram(q: list[sp.Expr]) -> sp.Matrix:
    """Observability Gramian for the tail recurrence of n(z)/q(z)."""
    n = len(q) - 1
    A = sp.zeros(n)
    for j in range(n):
        A[0, j] = -q[j + 1]
    for j in range(1, n):
        A[j, j - 1] = 1
    L = sp.zeros(n * n)
    rhs = sp.zeros(n * n, 1)
    for i in range(n):
        for j in range(n):
            row = n * i + j
            L[row, row] = 1
            rhs[row] = int(i == 0 and j == 0)
            for a in range(n):
                for b in range(n):
                    L[row, n * a + b] -= sp.conjugate(A[a, i]) * A[b, j]
    sol = L.inv() * rhs
    S = sp.Matrix(n, n, list(sol))
    require(all(sp.simplify(x) == 0 for x in S - A.conjugate().T*S*A - sp.diag(1, *([0]*(n-1)))), 'Stein residual')
    return S


def exact_h2(num: list[sp.Expr], q: list[sp.Expr], S: sp.Matrix) -> sp.Expr:
    """Exact infinite H2 norm from a finite stable Stein equation."""
    n = len(q) - 1
    num = num + [sp.Integer(0)] * (n + 1 - len(num))
    coeff = []
    for j in range(n + 1):
        coeff.append(sp.simplify(num[j] - sum(q[k]*coeff[j-k] for k in range(1, min(j,n)+1))))
    x = sp.Matrix([coeff[n-j] for j in range(n)])
    ans = sum(c*sp.conjugate(c) for c in coeff[:n]) + (x.conjugate().T*S*x)[0]
    return sp.simplify(ans)



def exact_inner(num1: list[sp.Expr], num2: list[sp.Expr], q: list[sp.Expr], S: sp.Matrix) -> sp.Expr:
    n=len(q)-1
    def coefficients(num):
        num=num+[sp.Integer(0)]*(n+1-len(num)); out=[]
        for j in range(n+1):
            out.append(sp.simplify(num[j]-sum(q[k]*out[j-k] for k in range(1,min(j,n)+1))))
        return out
    c1=coefficients(num1); c2=coefficients(num2)
    x1=sp.Matrix([c1[n-j] for j in range(n)])
    x2=sp.Matrix([c2[n-j] for j in range(n)])
    return sp.simplify(sum(c1[j]*sp.conjugate(c2[j]) for j in range(n))+(x2.conjugate().T*S*x1)[0])


def exact_checks() -> dict:
    I=sp.I; Q=sp.Rational
    u=Q(3,5)+I*Q(4,5); v=Q(5,13)+I*Q(12,13)
    examples = [
        ('one', [sp.Integer(1)]),
        ('two_clock', [sp.Integer(1), -sp.Integer(1)]),
        ('two_distinct', [u, sp.conjugate(u)]),
        ('two_rotated', [I*u, I*sp.conjugate(u)]),
        ('three', [sp.Integer(1),u,sp.conjugate(u)]),
        ('three_cluster', [sp.Integer(1)]*3),
        ('four', [u,sp.conjugate(u),v,sp.conjugate(v)]),
        ('four_cluster', [sp.Integer(1)]*4),
    ]
    params=[(Q(3,4),Q(1,2)),(Q(4,5),Q(2,5)),(Q(2,3),Q(1,3))]
    records=[]; cross_count=0
    for name, roots in examples:
        p=poly_product(roots); n=len(roots)
        require(all(sp.simplify(p[n-k]-p[n]*sp.conjugate(p[k]))==0 for k in range(n+1)), 'self inverse coefficients')
        for a,b in params:
            q=[p[k]*b**k for k in range(n+1)]
            qs=[sp.conjugate(q[n-k]) for k in range(n+1)]
            S=exact_gram(q)
            x=a**n; y=b**n
            aa=(1-x*y)/(1-y*y); dd=(x-y)/(1-y*y)
            num=[p[k]*a**k for k in range(n+1)]
            rem=[sp.simplify(num[k]-aa*q[k]-p[n]*dd*qs[k]) for k in range(n+1)]
            require(rem[0]==0 and rem[-1]==0, 'remainder endpoints')
            for k in range(1,n):
                delta=a**k-aa*b**k-dd*b**(n-k)
                require(delta>0, 'strict interior weights')
                require(sp.simplify(rem[k]-p[k]*delta)==0,'weighted numerator')
            nf=exact_h2(num,q,S); ne=exact_h2(rem,q,S)
            floor=1+(x-y)**2/(1-y*y)
            require(sp.simplify(nf-floor-ne)==0,'exact radial Pythagoras')
            require(ne>=0,'nonnegative radial residual')
            is_clock=all(c==0 for c in p[1:-1])
            require((ne==0)==is_clock,'exact equality classification')
            # Independent derivative/Abel identity, at the radius b.
            anum=[sp.Rational(k,n)*q[k] for k in range(n+1)]
            arem=[sp.simplify(anum[k]+y*y/(1-y*y)*q[k]-p[n]*y/(1-y*y)*qs[k]) for k in range(n+1)]
            na=exact_h2(anum,q,S); nr=exact_h2(arem,q,S)
            require(sp.simplify(na-y*y/(1-y*y)-nr)==0,'exact Abel Pythagoras')
            require(nr>=0,'nonnegative Abel residual')
            records.append({'example':name,'N':n,'a':str(a),'b':str(b),'radial_excess':str(ne),'Abel_excess':str(nr)})
            ac=sp.Rational(1,5)+sp.I*sp.Rational(2,5)
            xc=ac**n
            aac=(1-xc*y)/(1-y*y); ddc=(xc-y)/(1-y*y)
            numc=[p[k]*ac**k for k in range(n+1)]
            remc=[sp.simplify(numc[k]-aac*q[k]-p[n]*ddc*qs[k]) for k in range(n+1)]
            cross=exact_inner(num,numc,q,S)
            r_cross=exact_inner(rem,remc,q,S)
            base=1+(x-y)*(sp.conjugate(xc)-y)/(1-y*y)
            require(sp.simplify(cross-base-r_cross)==0,'complex positive kernel identity')
            cross_count+=1
    return {'count':len(records),'complex_cross_identity_count':cross_count,'records':records}


def build_bgs(n: int, tau: float) -> tuple[np.ndarray, np.ndarray]:
    require(n>=3 and n%2==1,'odd size required')
    x=np.arange(n); q=x/n
    def profile(q):return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
    r=profile(q)
    diag=np.cos(14*np.pi*q)+r/10+r*np.sin(2*np.pi*q)/100-0.1
    A=np.diag(diag.astype(complex))
    edge=(-3-4j)/1000*profile(((x+pow(2,-1,n))%n)/n)
    for j in range(n):
        A[j,(j+1)%n]+=edge[j]
        A[(j+1)%n,j]+=edge[j].conjugate()
    P=(3*x[:,None]**2-2*x[:,None]*x[None,:]+3*x[None,:]**2)
    M=np.exp(2j*np.pi*((-pow(8,-1,n)*P)%n)/n)/np.sqrt(n)
    vals,V=eigh(A)
    Q=(V*np.exp(1j*tau*n*vals))@V.conj().T
    U=Q@M
    require(np.linalg.norm(A-A.conj().T)<1e-12,'Hermitian A')
    require(np.linalg.norm(U.conj().T@U-np.eye(n))<1e-10,'unitary U')
    return U,A


def grid_size(n:int,s:float,t:float,tolerance:float=1e-12)->tuple[int,float]:
    """Bound both radial and Abel remainder quadratures by H2 Cauchy tails.
    If analytic h has sup_{|z|=R}|h|<=H, the quadrature error of |h|^2 is
    <=2 H^2/[(1-R^-2)(R^M-1)]. Work in logs, with conservative padding.
    """
    eta=s/(2*n); R=math.exp(eta)
    a=math.exp(-s/n); b=math.exp(-t/n)
    x=math.exp(-s); y=math.exp(-t)
    aa=(1-x*y)/(1-y*y); dd=(x-y)/(1-y*y)
    lb_ratio=math.log((R-b)/(1-b*R))
    lr=math.log(math.exp(t-s)+aa+abs(dd)) + n*lb_ratio
    lb_abel=math.log((R-a)/(1-a*R))
    labase=math.log(1/math.expm1(eta)+x*x/(1-x*x)+x/(1-x*x))
    la=labase+n*lb_abel
    lh=max(lr,la)
    target=math.log(8)+2*lh-math.log(-math.expm1(-2*eta))-math.log(tolerance)
    m=1<<(max(1,math.ceil(target/eta))-1).bit_length()
    logerr=math.log(4)+2*lh-math.log(-math.expm1(-2*eta))-eta*m
    return m, logerr


def numerical_identity(phases:np.ndarray,s:float=1,t:float=2)->dict:
    n=len(phases); lam=np.exp(2j*np.pi*phases)
    a=math.exp(-s/n); b=math.exp(-t/n)
    x=math.exp(-s); y=math.exp(-t)
    aa=(1-x*y)/(1-y*y); dd=(x-y)/(1-y*y)
    cn=np.exp(1j*(math.pi*n+2*math.pi*phases.sum()))
    m,le=grid_size(n,s,t)
    sums=np.zeros(6,dtype=float); overlap=np.zeros(4,dtype=complex)
    for start in range(0,m,512):
        idx=np.arange(start,min(start+512,m))
        z=np.exp(2j*np.pi*idx/m)
        zz=lam[:,None]*z[None,:]
        logqb=np.log(1-b*zz).sum(axis=0)
        logqa=np.log(1-a*zz).sum(axis=0)
        f=np.exp(logqa-logqb)
        B=z**n*np.exp(-2j*logqb.imag)
        residual=f-aa-cn*dd*B
        fa=-(a*zz/(1-a*zz)).sum(axis=0)/n
        Ba=z**n*np.exp(-2j*logqa.imag)
        ra=fa+x*x/(1-x*x)-cn*x/(1-x*x)*Ba
        # Independent positive ratio computation (no complex logarithm ratio).
        u=np.sin(np.pi*(phases[:,None]+idx[None,:]/m))**2
        ca=math.sinh(s/(2*n))**2; cb=math.sinh(t/(2*n))**2
        positive=np.exp(np.log1p(-(cb-ca)/(cb+u)).sum(axis=0))
        sums += [np.sum(abs(f)**2),np.sum(abs(residual)**2),np.sum(abs(fa)**2),np.sum(abs(ra)**2),np.sum(positive),np.sum(abs(B)**2)]
        overlap += [residual.sum(),np.vdot(B,residual),ra.sum(),np.vdot(Ba,ra)]
    sums/=m; overlap/=m
    floor=1+(x-y)**2/(1-y*y); afloor=x*x/(1-x*x)
    er=abs(sums[0]-floor-sums[1]); ea=abs(sums[2]-afloor-sums[3])
    require(er<2e-9,'numerical radial identity')
    require(ea<2e-8,'numerical Abel identity')
    require(abs(sums[4]-math.exp(-(t-s))*sums[0])<2e-9,'positive ratio formula')
    require(np.max(abs(overlap))<2e-8,'orthogonality')
    require(abs(sums[5]-1)<1e-12,'inner norm')
    # No independent approximation of infinitely many traces is substituted.
    cue_inside=(a-b)**2/(1-b*b)*(1-x*x)/(1-a*a)
    return {'N':n,'s':s,'t':t,'grid_size':m,'analytic_quadrature_bound_log':le,
            'Z':sums[4],'Z_clock':math.exp(-(t-s))*floor,
            'hardy_excess':sums[1], 'hardy_excess_CUE_mean':cue_inside-(x-y)**2/(1-y*y),
            'Abel':sums[2], 'Abel_floor':afloor,'Abel_excess':sums[3],
            'radial_residual':er,'Abel_residual':ea,'orthogonality_residual':float(np.max(abs(overlap)))}


def numerical_checks()->dict:
    rng=np.random.default_rng(6151026); records=[]
    for n in [1,2,3,7,19,31]:
        examples=[('clock',np.arange(n)/n),('cluster',np.zeros(n)),('random',rng.uniform(0,1,n))]
        for name,ph in examples:
            out=numerical_identity(ph)
            out['type']=name
            if name=='clock': require(out['hardy_excess']<1e-20,'clock norm zero')
            records.append(out)
    for n,tau in [(19,.03),(31,.03),(31,.30),(63,.30),(127,.30)]:
        U,_=build_bgs(n,tau)
        T,V=schur(U,output='complex')
        require(np.linalg.norm(U@V-V@T)<2e-10,'Schur residual')
        ph=np.angle(np.diag(T))/(2*np.pi)
        out=numerical_identity(ph);out.update(type='BGS_proxy',tau=tau)
        records.append(out)
    return {'count':len(records),'records':records}


def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('--exact-only',action='store_true')
    ap.add_argument('--numeric-only',action='store_true');ap.add_argument('--output',default='verification.json')
    args=ap.parse_args();start=time.time();report={'status':'finite checks only; fixed-coupling BGS unproved'}
    if not args.numeric_only:report['exact']=exact_checks()
    if not args.exact_only:report['numerical']=numerical_checks()
    s=1.;t=2.;x=math.exp(-s);y=math.exp(-t)
    inside=(t-s)**2*(1-x*x)/(4*s*t)-(x-y)**2/(1-y*y)
    report['target_s1_t2']={'Z_clock':math.exp(-1)*(1+(x-y)**2/(1-y*y)),
        'Z_CUE_limit':math.exp(-1)*(1+(1-x*x)/8),'hardy_excess_CUE_limit':inside}
    report['elapsed_seconds']=time.time()-start
    Path(args.output).write_text(json.dumps(report,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['exact','numerical']},indent=2))
    if 'exact' in report:print('exact cases:',report['exact']['count'])
    if 'numerical' in report:
        print('numerical cases:',report['numerical']['count'])
        print('max radial error',max(r['radial_residual'] for r in report['numerical']['records']))
        print('max Abel error',max(r['Abel_residual'] for r in report['numerical']['records']))
        print('proxy rows:',[(r['N'],r.get('tau'),r['hardy_excess']) for r in report['numerical']['records'] if r['type']=='BGS_proxy'])

if __name__=='__main__':main()
