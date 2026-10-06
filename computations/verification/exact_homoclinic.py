#!/usr/bin/env python3
"""Bounded exact H1–H10 controls; no analytic formalization.

Exact Fraction arithmetic and rational pairs for Q(sqrt(2)); j=0..64,
m=1..16, 32 actual Fourier modes, literal tau=10^-80 constants, and 11
frozen input hashes. No input-dependent unbounded loops or source writes.
Use --root for a canonical checkout and --overlay only for a staged overlay.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def run(root, overlay=None):
    checks=[]
    def check(name, condition, scope):
        if not condition:
            raise RuntimeError("Exact homoclinic check failed: " + name)
        checks.append({'name':name,'passed':True,'scope':scope})

    # Q(sqrt(2)) with exact rational arithmetic.
    def qa(x,y): return (x[0]+y[0],x[1]+y[1])
    def qn(x): return (-x[0],-x[1])
    def qm(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    def qs(x,c): return (x[0]*c,x[1]*c)
    def mat_vec(A,x): return [qa(qs(x[0],A[0][0]),qs(x[1],A[0][1])),qa(qs(x[0],A[1][0]),qs(x[1],A[1][1]))]
    def integer(x): return x[1]==0 and x[0].denominator==1
    S=[[3,4],[2,3]]; Si=[[3,-4],[-2,3]]
    lam=(F(3),F(2)); lami=(F(3),F(-2)); d=[(F(0),F(1,2)),(F(-1,2),F(0))]
    pos=d; neg=d; decay=(F(1),F(0)); a,b=1,0
    for j in range(0,65):
        expected=qs(decay,F(1,2))
        expectedq=qm(decay,(F(0),F(1,2)))
        check(f'homoclinic positive representative j={j}',pos==[expectedq,qn(expected)],'Exact equality in Q(sqrt(2))')
        if j:
            check(f'homoclinic negative representative j={j}',all(integer(qa(x,qn(y))) for x,y in zip(neg,[expectedq,expected])),'Congruence modulo Z^2, exact Q(sqrt(2))')
        kp=qa(qs(d[0],a),qs(d[1],2*b))
        kn=qa(qs(d[0],a),qs(d[1],-2*b))
        check(f'phase congruences j={j}',kp==expectedq and integer(qa(kn,qn(expectedq))),'Both Fourier time directions, exact field arithmetic')
        check(f'Pell identity j={j}',a*a-2*b*b==1,'Exact integer recurrence')
        if j: check(f'oriented support exclusion j={j}',2*b>=4,'Finite controls only; all-j monotonic proof in review')
        pos=mat_vec(S,pos);neg=mat_vec(Si,neg);decay=qm(decay,lami);a,b=3*a+4*b,2*a+3*b

    # Fourier coefficients represented as Gaussian rational pairs.
    def ca(x,y):return (x[0]+y[0],x[1]+y[1])
    def cm(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    def ps(P,c):return {k:cm(v,c) for k,v in P.items()}
    def pa(P,Q):
        R=dict(P)
        for k,v in Q.items():R[k]=ca(R.get(k,(F(0),F(0))),v)
        return {k:v for k,v in R.items() if v!=(0,0)}
    def pm(P,Q):
        R={}
        for (a,b),v in P.items():
            for (c,d),w in Q.items():
                k=(a+c,b+d);R[k]=ca(R.get(k,(F(0),F(0))),cm(v,w))
        return {k:v for k,v in R.items() if v!=(0,0)}
    one={(0,0):(F(1),F(0))}
    cos7={(7,0):(F(1,2),F(0)),(-7,0):(F(1,2),F(0))}
    cos1={(1,0):(F(1,2),F(0)),(-1,0):(F(1,2),F(0))}
    sin1={(1,0):(F(0),F(-1,2)),(-1,0):(F(0),F(1,2))}
    cospa={(0,1):(F(-3,10),F(-2,5)),(0,-1):(F(-3,10),F(2,5))}
    r=pm(pa(one,ps(cos7,(F(-1),F(0)))),pa(one,cos1))
    rshift={k:cm(v,(F((-1)**k[0]),F(0))) for k,v in r.items()}
    g=pa(pa(pa(pa(cos7,ps(r,(F(1,10),F(0)))),ps(pm(r,sin1),(F(1,100),F(0)))),ps(pm(rshift,cospa),(F(1,100),F(0)))),ps(one,(F(-1,10),F(0))))
    check('actual isolated coefficient',g[(1,0)]==(F(1,20),F(-1,200)),'Exact expansion of fixed_map_path_model symbol')
    check('actual support p range',all(abs(k[1])<=1 for k in g),'All actual Fourier coefficients enumerated from exact expression')
    check('actual support count',len(g)==32,'Exact Laurent multiplication')

    # Cyclic quadratic coefficients including self and repeated-neighbour cases.
    def addpoly(P,key,value):
        key=tuple(sorted(key));P[key]=P.get(key,F(0))+value
    for m in range(1,17):
        K=[[F(0) for _ in range(m)]for _ in range(m)]
        for i in range(m):
            K[i][i]+=F(3,2);K[i][(i+1)%m]-=F(1,4);K[i][(i-1)%m]-=F(1,4)
        lhs={};rhs={}
        for i in range(m):
            addpoly(lhs,(i,i),F(-3,4));addpoly(lhs,(i,(i+1)%m),F(1,4))
            for j in range(m):addpoly(rhs,(i,j),-K[i][j]/2)
        check(f'cyclic energy identity m={m}',lhs=={k:v for k,v in rhs.items() if v!=0},'Exact rational polynomial coefficients')

    # Full C^alpha remainder certificate at literal tau.
    t=F(1,10**80); eta=10**10*t+10**50*t*t
    check('literal eta bound',eta<=2*10**10*t,'Exact rational evaluation at tau=10^-80')
    M=4*10**10*t; B=2*10**20*t; L=7; F2=10**10
    first=2*F2*M+4*F2*M*(L+B)+2*F2*B
    A=5*10**49*t*t
    rem=A*(1+2*(L+B))
    quad=M*M+2*M*B
    check('full smooth displacement C^alpha cost',first<=10**33*t,'Supremum plus seminorm, explicit product estimate')
    check('full HJ composition C^alpha cost',rem<=10**53*t*t,'Supremum plus seminorm')
    check('full quadratic C^alpha cost',quad<=10**33*t*t,'Supremum plus seminorm')
    check('full V remainder literal bound',t*first+rem+quad<=10**60*t*t,'Actual fixed tau; no hidden O constant')
    beta=F(29,5)
    check('Fourier orbit factor',2*(1+2/(beta-1))<3,'Exact geometric majorant after 2^alpha<=2')
    check('nonzero actual orbit sum',t/F(160)-3*10**60*t*t>=t/F(1000),'Uses |c_v|>=1/20 and pi<4')
    # Exact rational enclosure of sqrt(2); the lambda-dependent bound is monotone.
    slo=F(1414213562373095,10**15);shi=F(1414213562373096,10**15)
    check('sqrt2 enclosure',slo*slo<2<shi*shi,'Integer/rational arithmetic')
    llo=3+2*slo;lhi=3+2*shi
    check('beta below lambda',beta<llo,'Exact rational enclosure')
    check('weighted Green Lbeta below 300',(lhi+beta)/(slo*(llo-beta))<300,'Conservative rational interval bound')
    check('Holder geometric split below 500',2*lhi/(llo-beta)+2*beta/(beta-1)<500,'Conservative rational interval bound')
    check('resolvent bound 301',300/(1-4200*eta)<=301,'Exact rational check')
    check('u Holder constant below 10^9',301*32*500*4<10**9,'Before integration in matching parameter s')
    binding_path = Path("evidence/homoclinic_20261006/source_binding.json")
    def resolve(rel):
        if overlay is not None and (overlay/rel).is_file():
            return overlay/rel
        return root/rel
    manifest = json.loads(resolve(binding_path).read_text())
    for item in manifest['files']:
        h = hashlib.sha256(resolve(Path(item['public_path'])).read_bytes()).hexdigest()
        check('source hash: '+item['path'], h == item['sha256'], 'Frozen dependency hash verification')
    return {'claim':'H1-H10 at literal fixed tau=10^-80',
            'scope':'Rational/field checks support the analytic audit; not nonlinear numerical proof or formal verification.',
            'checks':checks, 'total':len(checks), 'all_passed':all(c['passed'] for c in checks)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--overlay', type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.root, args.overlay), indent=2))


if __name__ == '__main__':
    main()
