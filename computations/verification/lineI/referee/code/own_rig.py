"""Referee (Line I audit): independent REST-mode certificate for one core Galerkin matrix (no use of rig_spec.py).
Claim certified: for L = lifted operator with core matrix A (mid+rad), comparison op T0' = [[A+0,0],[X,0]], perturbation
pert = delta1+delta2+Delta+||rad||_F, F = pert * G(R) < 1 with G(R) = (S(R)+1/R)(1+||X||/R)+1/R, S(R) >= sup_{|z|>=R}||(z-A)^{-1}||.
S(R) from the Neumann series: ||(z-A)^{-1}|| <= sum_{j<p} N_j |z|^{-j-1} / (1 - N_p |z|^{-p}),  N_j >= ||A^j||_2.
N_j: float powers M_j = fl(M_{j-1} A); |fl(XY)-XY| <= g ||X||_F ||Y||_F entrywise-Frobenius with g = sqrt2*gamma_{2n+2}
(covers any summation order / FMA for complex dot products of length n); M_j - A^j = sum_i E_i A^{j-i}, ||E_i|| <= g||M_{i-1}||_F||A||_F.
||M||_2 <= min(||M||_F, sqrt(||M||_1 ||M||_inf)).  All JSON-read floats padded up by (1+1e-12); computed float norms by (1+1e-6).
Usage: own_rig.py prefix j R_list p build.json out.json"""
import sys, json, time, numpy as np
from flint import arb, ctx
ctx.prec=128
pre,j,Rs,p,bj,outf=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),sys.argv[5],sys.argv[6]
t0=time.time(); u=arb(2)**-53
PADJ=arb('1.000000000001'); PADF=arb('1.000001')
J=lambda x: arb(float(x))*PADJ
up=lambda x: arb(float(x))*PADF
A=np.load(f'{pre}_b{j}_mid.npy'); rad=np.load(f'{pre}_b{j}_rad.npy'); n=A.shape[0]
assert np.isfinite(A).all() and (rad>=0).all()
epsA=up(np.sqrt((rad.astype(np.float64)**2).sum())); del rad
g=arb(2).sqrt()*((2*n+2)*u)/(1-(2*n+2)*u)
info=json.load(open(bj)); assert info['D']==n
fro=lambda M: up(np.sqrt(np.vdot(M,M).real))
def n2(M): return arb.min(fro(M),(up(np.abs(M).sum(0).max())*up(np.abs(M).sum(1).max())).sqrt())
nA=fro(A); N=[arb(1),n2(A)]; E=[None,None]; M=A.copy(); Mf=[None,nA]
for k in range(2,p+1):
    E.append(g*Mf[k-1]*nA)          # ||fl(M_{k-1}A) - M_{k-1}A||_F
    M=M@A; Mf.append(fro(M))
    err=sum((E[i]*N[k-i] for i in range(2,k+1)),arb(0))   # ||M_k - A^k|| <= sum_i ||E_i|| ||A^{k-i}||
    N.append(n2(M)+err)
    if k%4==0: print('k',k,float(N[k].upper()),float(err.upper()),round(time.time()-t0),flush=True)
pert=J(info['delta1'])+J(info['delta2'])+J(info['Delta'])+epsA
X=J(info['Xnorm'])
out=dict(D=n,epsA=float(epsA.upper()),g=float(g.upper()),pert=float(pert.upper()),N=[float(x.upper()) for x in N],res=[])
for R_ in Rs.split(','):
    R=arb(R_); q=N[p]/R**p; assert q<1
    S=sum((N[k]/R**(k+1) for k in range(p)),arb(0))/(1-q)
    G=(S+1/R)*(1+X/R)+1/R; F=pert*G
    out['res'].append(dict(R=R_,S=float(S.upper()),G=float(G.upper()),F=float(F.upper()),certified=bool(F<1),
        C_trace=float((4*J(info['trace_norm'])*G/(1-F)).upper()) if F<1 else None))
    print(out['res'][-1],flush=True)
out['secs']=round(time.time()-t0); json.dump(out,open(outf,'w'),indent=1); print('DONE',out['secs'])
