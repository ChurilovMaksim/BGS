"""N10b [N]: float rate of the 4-fold collision automaton (rho -> rho*rho, letters w=v+v') at middle twist tau=0, vs the 2-fold one.
|A|_HS^4 <= Cpair^2 sum_{v,v'} prod rho(v_i)rho(v'_i) e(sum (v_i+v'_i) tau_i); integrating over y keeps exact collisions of w=v+v'."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N2/code')
from scipy.special import jv
AM=60; J=np.abs(jv(np.arange(AM+1),1.8))
def Jabs(a): a=abs(a); return J[a] if a<=AM else 0.0
def rho_d(d,tau): return sum(Jabs(a)*Jabs(a-d)*math.exp(tau*(abs(a)+abs(a-d))) for a in range(-AM,AM+1) if -AM<=a-d<=AM)
def mat(R,E):
    es=range(-E,E+1); st=[(a,b) for a in es for b in es]; idx={s:i for i,s in enumerate(st)}; T=np.zeros((len(st),)*2)
    for (a,b) in st:
        for e in es:
            d=e-6*b+a
            if d in R: T[idx[(a,b)],idx[(b,e)]]+=R[d]
    return T
for tau in (0.0,):
    R1={d:rho_d(d,tau) for d in range(-70,71)}
    R2={d:sum(R1.get(x,0)*R1.get(d-x,0) for x in range(-70,71)) for d in range(-120,121)}
    R3={d:sum(R2.get(x,0)*R1.get(d-x,0) for x in range(-120,121)) for d in range(-160,161)}
    for E in (6,10,14):
        for name,R in (('s2',R1),('s3?',R3),('s4',R2)):
            ev=max(abs(np.linalg.eigvals(mat(R,E))))
            print('tau',tau,'E',E,name,'rho=%.6f'%ev,'sumR=%.5f'%sum(R.values()),flush=True)
