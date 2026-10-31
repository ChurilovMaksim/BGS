# Line N [N]: sanity check of the explicit inequalities on real levels (p, q), q | h_{3p}, q small enough for a q x q FFT.
# S(a1,a2) = sum_{x mod tau} e((a1 l^x + a2 l^{-x})/q), l = image of lambda = 3+2sqrt2 in F_q (split prime).
# Exact J_k = q^{-2} sum_z |S(z)|^{2k}. Checks: J_2 <= 2tau^2, J_3 <= F_bound, and |S|_max(nondeg) vs (2,2),(2,3),(3,3), Weil.
import numpy as np, json, math, sys
from sympy import factorint, sqrt_mod, primerange
def hseq(M):
    x,y=1,1; out={1:1}
    for m in range(2,M+1):
        x,y=x+2*y,x+y
        if m%2: out[m]=x
    return out
H=hseq(250)
def lam_in_Fq(q):
    r=sqrt_mod(2,q)
    return [(3+2*r)%q,(3-2*r)%q]
res=[]
QMAX=int(sys.argv[1]) if len(sys.argv)>1 else 6000
for p in primerange(5,70):
    for q in sorted(set(factorint(H[3*p]).keys())):
        if q==7 or q>QMAX: continue
        l=lam_in_Fq(q)[0]
        tau=1; v=l
        while v!=1: v=v*l%q; tau+=1
        xs=[pow(l,i,q) for i in range(tau)]
        M=np.zeros((q,q)); 
        for u in xs: M[u, pow(u,q-2,q)]+=1
        S=np.fft.fft2(M).conj()   # S(a1,a2)=sum e(+(a1 u+a2 v)/q)
        A=np.abs(S)
        J2=float((A**4).sum()/q**2); J3=float((A**6).sum()/q**2)
        A[0,:]=0; A[:,0]=0          # keep nondegenerate a1 a2 != 0
        Smax=float(A.max())
        Fb=4*3**(4/3)*(q*tau/(q-1))**(2/3)*tau**3+3*tau**5*q/(q-1)**2+12*tau**3
        rec=dict(p=p,q=q,tau=tau,log_tau_q=math.log(q)/math.log(tau),Smax_over_tau=Smax/tau,
                 weil=2*math.sqrt(q)/tau,b22=(2*q/tau**2)**0.25,
                 b23=(q**2*tau**2*2*tau**2*Fb)**(1/12)/tau, b33=(q**2*tau**6*Fb**2)**(1/18)/tau,
                 J2=J2,J2_bound=2*tau**2-tau,J3=J3,J3_over_6tau3=J3/(6*tau**3),J3_bound=Fb)
        ok = (J2<=rec['J2_bound']+1e-6) and (J3<=Fb) and Smax/tau<=min(rec['b22'],rec['b23'],rec['b33'])+1e-9
        rec['ok']=bool(ok); res.append(rec); print(json.dumps({k:(round(v,4) if isinstance(v,float) else v) for k,v in rec.items()}),flush=True)
json.dump(res,open('/workspace/bgs-lineN/logs/n3_check.json','w'),indent=1)
print("all ok:",all(r['ok'] for r in res), "n=",len(res))
