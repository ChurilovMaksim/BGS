"""Referee: rigorous version of N13's 'coef read on a grid' step. Using N13's b3 bound formula (inputs = their arb-certified scalars),
evaluated in arb, and monotonicity of bound(t) in t, verify on a geometric partition 0<t_0<...<t_K=1/256:
   bound(t_{k+1}) <= 1 + c0 + C*t_k^2  for every k,   and  bound(t_0) <= 1 + c0   (covers [0,t_0]).
Then N_H(t) <= 1 + c0 + C t^2 on [0,1/256] rigorously (given the inputs)."""
import json
from flint import arb, ctx
ctx.prec=200
q=json.load(open('/workspace/bgs-lineN/N13/logs/b2_quad.json')); B=json.load(open('/workspace/bgs-lineN/N13/logs/b_arb.json'))
A=lambda x: arb(repr(float(x)))
eta=A(B['V2']['eta']); Lip=A(B['Lip_H']); L2=A(q['L2']); nP=A(q['nP']); nPl=A(q['nP_lo']); g=A(q['g']); ps=A(q['psi_dual']); om=A(q['one_minus_psiPhi'])
def norm2(a,b,c,d):  # spectral norm of real 2x2 [[a,b],[c,d]]: sqrt(largest eig of M^T M)
    p=a*a+c*c; r=b*b+d*d; s=a*b+c*d
    return ((p+r+((p-r)**2+4*s*s).sqrt())/2).sqrt()
def bound(t):
    da=A(q['da'])+t*A(q['eps0'])*(1+om)
    tau1=om*nP*(1+(1+eta)**2)+(1+eta)*A(q['MPhi_minus_Phi'])
    a=1+da; b=nP*(A(q['c1'])*t+A(q['psiM_minus_psi'])); c=(A(q['b1'])*t+tau1)/nPl; d=A(q['kapp'])+A(q['b2'])*t
    x1=nP*ps*L2*t*t/2; x2=(1+eta)*L2*t*t/2+(1+eta)*Lip*t*om*nP
    sX=norm2(a,b,c,d)*(1+2*g*ps).sqrt()+(x1*x1+x2*x2).sqrt()
    return sX/(1-2*g*ps).sqrt()
res={}
for C,c0 in [(4260,1.01e-12),(4253.4,1.005e-12)]:
    C=A(C); c0=A(c0); t=arb(1)/10**9; ok=bool(bound(t)<1+c0); worst=None; k=0
    while True:
        t2=min(t*arb('1.0005'),arb(1)/256)
        lhs=bound(t2); rhs=1+c0+C*t*t
        if not (lhs<rhs): ok=False; worst=float(t.mid()); break
        k+=1; t=t2
        if t2.upper()>=arb(1)/256-arb(1)/10**30 and float(t2.mid())>=1/256: break
    res[str(float(C.mid()))]=dict(c0=float(c0.mid()),ok=ok,cells=k,first_fail=worst)
    print(res,flush=True)
json.dump(res,open('logs/ref_quad_partition.json','w'),indent=1)
