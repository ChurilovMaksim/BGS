"""[P-check, arb 200 bits] of the inheritance identity W_{7q, qC} = (n_q/q^2) W_{7,C} (proof: CRT, REPORT_J3 §2), using exact integer
exponent histograms (Gauss sums as elements of Z[zeta_d]) evaluated in arb; also checks n_q against the member count formula."""
import sys, math, json, numpy as np
from flint import arb, acb, ctx
ctx.prec=200
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
exec(open("code/inherit7q.py").read().split("res={}")[0])   # definitions only (orbit, cls, members)
def hist(d,t,bx,by):
    g=np.arange(d); GX,GY=np.meshgrid(g,g,indexing='ij')
    return np.bincount(((-(t*(GX*GX-2*GY*GY)+2*(bx*GX+2*by*GY)))%d).ravel(),minlength=d)
def Wexact(m,a,d,proper,scale):
    ts=members(m,a,d,proper); out={}
    E=[acb(0,2*arb.pi()*k/d).exp() for k in range(d)]
    for c in cls:
        T=np.zeros(d,dtype=object)
        for t in ts:
            h0=hist(d,t,0,0); h0r=np.array([h0[(-k)%d] for k in range(d)],dtype=object)
            for (bx,by) in orbit(*map(int,c.split(':'))):
                hb=hist(d,t,(scale*bx)%d,(scale*by)%d).astype(object)
                cv=np.zeros(d,dtype=object)
                for i in np.nonzero(h0r)[0]: cv+=h0r[i]*np.roll(hb,i)
                T+=cv
        out[c]=sum((int(T[k])*E[k] for k in range(d) if T[k]),acb(0))/arb(d)**4
    return out,len(ts)
res={}; ok=True
for m,a,q in ((15,2,41),(15,-2,31),(33,2,23)):
    D=mdata(m); h=D['h']
    W7,_=Wexact(m,a,7,[1],1); Wd,nd=Wexact(m,a,7*q,[1,7,q],q)
    nq=q-2 if (h//(7*q))%q else q-1
    for c in cls:
        diff=abs(Wd[c]-arb(nq)/q**2*W7[c]); good=diff.upper()<1e-40; ok&=good
    res[f'{m},{a},{q}']=dict(n_q=nq,n_members_7q=nd,n_members_7=len(members(m,a,7,[1])),max_diff=max(float(abs(Wd[c]-arb(nq)/q**2*W7[c]).upper()) for c in cls))
    print(m,a,q,res[f'{m},{a},{q}'],flush=True)
print('ALL CHECKS PASSED' if ok else 'FAIL')
json.dump(res,open('logs/inherit_proof_check.json','w'),indent=1)
