"""N11: box-robust lower bound on |1+X|-1 in the gas-model form, rigorous given the model form:
w' in certified box Bw (N8 fam cert, sg=+1) enlarged by tail T, R' in box BR (near0/z0e4 certs) enlarged by T.
Cells of half-diagonal d_w, d_R; per cell: |1+X(center)|-1 - Lip-perturbation(d_w+T, d_R+T) (caseC formula with centre values).
Combined with caseA/caseB (phase-free, use box extremes). usage: r_robust_grid.py T nw nR"""
import sys, math, numpy as np, json
T=float(sys.argv[1]); nw=int(sys.argv[2]); nR=int(sys.argv[3])
Rew=(2.883691903314375e-4,3.987839237304488e-4); Imw=(1.3899304603258943e-4,2.5260246460933277e-4)
c0=complex(2.9866e-5,-6.599e-6); c4=complex(1.0413e-6,-3.1164e-6)
R0=2*(c0+c4); Rrad=3.973e-05
ReR=(R0.real-Rrad,R0.real+Rrad); ImR=(R0.imag-Rrad,R0.imag+Rrad)
lin1=8*(complex(3.43579708677916e-4,1.9579583160123678e-4)+c0).real
def cells(lo,hi,n): h=(hi-lo)/n; return lo+h*(np.arange(n)+0.5), h/2
wr,hwr=cells(*Rew,nw); wi,hwi=cells(*Imw,nw); rr_,hrr=cells(*ReR,nR); ri,hri=cells(*ImR,nR)
W=(wr[:,None]+1j*wi[None,:]).ravel(); RR=(rr_[:,None]+1j*ri[None,:]).ravel()
dw=math.hypot(hwr,hwi)+T; dR=math.hypot(hrr,hri)+T
worst=[];bad=[]
minrel=1e9; pmin=None
for p in range(3,40001,2):
    # phase-free bounds with box extremes
    a=2*p*(Rew[0]-T); A=2*math.exp(p*(ReR[0]-T))*(math.sinh(a)-1)-2 if a>0 else -1e9
    if A/(lin1*p)>=0.05 and p>5000:
        v=A/(lin1*p)
    else:
        Xc=2*(np.exp(p*RR)[:,None]*(np.sinh(2*p*W)[None,:]+1)-1)
        eR=np.exp(p*(RR.real+dR))[:,None]; ch=np.cosh(2*p*(W.real+dw))[None,:]
        pert=2*(eR*math.expm1(p*dR)*(ch+1)+eR*2*p*dw*ch)   # |e^{pR'}-e^{pRc}|<=e^{pReRc}(e^{p dR}-1) etc. (upper bounds)
        v=float((np.abs(1+Xc)-1-pert).min())/(lin1*p)
        v=max(v,A/(lin1*p))
    if v<minrel: minrel,pmin=v,p
    if v<=0: bad.append(p)
res=dict(T=T,nw=nw,nR=nR,min_rel=minrel,p_at_min=pmin,n_bad=len(bad),bad_range=[bad[0],bad[-1]] if bad else None)
print(json.dumps(res)); open('/workspace/bgs-lineN/N11/logs/r_robust_grid.jsonl','a').write(json.dumps(res)+'\n')
