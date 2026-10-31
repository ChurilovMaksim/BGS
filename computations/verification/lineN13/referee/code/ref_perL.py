"""Referee (Grok Bot) independent check of N12b periodic-orbit lower bounds Gamma_per(1/8,L).
Own orbit iteration (x,y)->(y,6y-x) mod D, own box-run statistic, rates rho(prod)^(1/n) (normalised so fixed point (0,0) -> mu*)
with three operators: Line-F lifted 8V (default params as N12b), Line-F refined truncation, and the N12/N6 cert_core sector-4 op."""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code'); sys.path.insert(0,'/workspace/bgs-lineN/N12/code')
from lift import ops, wk1
import a_ops as A
def lineF(K0,r,K,beta,N0,a=4):
    ns=np.arange(-N0,N0+1); w0=wk1(2.0,a)
    B=np.stack([ops(lambda m,n=n:1.0 if m==n else 0.0,N0,K0,r,r,K,beta=beta)[0] for n in ns]); w=np.array([w0(int(n)) for n in ns])
    return lambda t: np.tensordot(w*np.exp(2j*np.pi*ns*t),B,1)
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); s=complex(z['s'])
MS=np.array(A.MS); NS=np.array(A.NS); C0=np.array(A.COEF0)
n12=lambda t: np.tensordot(C0*np.exp(2j*np.pi*NS*t),MS,1)
OPS={'lineF_default':lineF(3,1.2,20,2.5,10),'lineF_refined':lineF(4,1.2,32,2.5,14),'N12_core':n12}
def orbit(x,y,D):
    o=[(x,y)]
    while True:
        x,y=y,(6*y-x)%D
        if (x,y)==o[0]: return o
        o.append((x,y))
def dist(v): v=abs(v)%1.0; return min(v,1-v)
def run(o,D,TH=0.125):
    inb=[max(dist(a/D),dist(b/D))<=TH for a,b in o]
    if all(inb): return 10**6
    n=len(o); k0=inb.index(False); r=m=0
    for q in range(n):
        r=r+1 if inb[(k0+q)%n] else 0; m=max(m,r)
    return m
def rate(op,o,D,norm):
    P=None
    for a,_ in o:
        L=op(a/D); P=L if P is None else L@P
    return float(np.abs(np.linalg.eigvals(P)).max()**(1/len(o)))/norm
seeds=[(4,408,72,1152),(4,1128,984,1152),(5,6560,0,6724),(5,5740,984,6724),(5,410,82,6724),(3,28,0,196),(3,161,189,196),(6,280,280,39200),(6,0,560,39200)]
norms={k:float(np.abs(np.linalg.eigvals(op(0.0))).max()) for k,op in OPS.items()}
MU=1.9154712
res=[]
for n,x,y,D in seeds:
    o=orbit(x,y,D); r=dict(n=n,seed=[x,y,D],period=len(o),run=run(o,D),d0=min(max(dist(a/D),dist(b/D)) for a,b in o))
    for k,op in OPS.items(): r[k]=MU*rate(op,o,D,norms[k])
    res.append(r); print(r,flush=True)
json.dump(dict(norms_rho_at0=norms,MU=MU,rows=res),open('logs/ref_perL.json','w'),indent=1)
