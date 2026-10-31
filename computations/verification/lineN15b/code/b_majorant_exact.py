"""N15b [N, exact enumeration]: E_G F and E_{H_d} F for the Prop-E majorant F = prod_{i<p} g(tau_i) (see a_majorant_ceiling.py),
over ALL beta mod h (no sampling). Also E over the p-periodic orbit structure is irrelevant (F is a function on beta).
c_maj(d) = log(E_H/E_G)/log d.  Prediction (perfect equidistribution mod the target ideal): E ~ g(0)^p / N_b, N_b ~ |H|/const,
so E_H/E_G ~ d, c_maj ~ 1.   usage: b_majorant_exact.py p"""
import sys, json, math, numpy as np, mpmath as mp
from sympy import factorint
p=int(sys.argv[1])
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
h=xy(p)[0]; fac=sorted(factorint(h))
u=np.array([float(abs(mp.besselj(a,1.8))) for a in range(-40,41)]); A=np.arange(-40,41)
GR=1<<16; tg=np.arange(GR)/GR; gg=np.abs(np.exp(2j*np.pi*np.outer(tg,A))@u)**2
LA=[1];LB=[0]
for i in range(p-1): a,b=LA[-1],LB[-1]; LA.append((3*a+4*b)%h); LB.append((2*a+3*b)%h)
B=np.arange(h,dtype=np.int64)
tot={'G':[0.0,0]}; 
for d in fac: tot[d]=[0.0,0]
for a in range(h):
    F=np.ones(h)
    for i in range(p):
        t=(2*(a*LA[i]+2*B*LB[i]))%h
        F*=gg[(t*GR)//h]
    if a==0: F[0]=0.0                      # exclude beta=0
    cnt=h-(1 if a==0 else 0)
    tot['G'][0]+=F.sum(); tot['G'][1]+=cnt
    if len(fac)>1:
        N=(a*a-2*B*B)%h
        for d in fac:
            ok=(N%d==0)&(N%(h//d)!=0)
            tot[d][0]+=F[ok].sum(); tot[d][1]+=int(ok.sum())
res=dict(p=p,h=h,factors=[int(q) for q in fac],g0p=float(gg[0]**p))
EG=tot['G'][0]/tot['G'][1]; res['E_G']=EG
for d in fac:
    if tot[d][1]:
        EH=tot[d][0]/tot[d][1]; res[f'E_H{d}']=EH; res[f'n_H{d}']=tot[d][1]; res[f'c_maj_{d}']=math.log(EH/EG)/math.log(d)
print(json.dumps(res)); json.dump(res,open(f'logs/b_majorant_exact_p{p}.json','w'),indent=1)
