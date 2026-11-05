"""research1105b [N, exhaustive]: Lemma S check.  For every point c in O/abar (= Z/h) on each line, G(n) = min height
max(|rho|,|rho'|) of rho == c eps^n mod abar.  Lemma S [P]: on a cross line, for primitive c (c != 0 mod every q|h)
and every n:  G(n)+G(n+p) >= sqrt(max(d+,d-)) - small, so max(G(n),G(n+p)) >= sqrt(D)/2.
Here we report Q = min_{primitive c} min_n max(G(n),G(n+p)) / sqrt(D), and the same on Binet lines (no constraint)."""
import sys, math, json, numpy as np
from twist_core import hp, lines
from seam_profile import reduce2
S2=math.sqrt(2)
def run(p,R=3):
    h=hp(p); out=[]
    for L in lines(p,h):
        W=L['W']; bu,bv=reduce2((h,0),((-W)%h,1))
        M=np.array([[bu[0]+bu[1]*S2,bv[0]+bv[1]*S2],[bu[0]-bu[1]*S2,bv[0]-bv[1]*S2]]); Mi=np.linalg.inv(M)
        c=np.arange(h,dtype=np.int64); prim=np.ones(h,bool)
        from sympy import factorint
        for q in factorint(h): prim&=(c%q!=0)
        eW=(1+W)%h; G=np.zeros((2*p,h))
        ci=c.copy()
        for n in range(2*p):
            a=ci.astype(float); b=a.copy()          # rho = ci (rational integer rep), embeddings (ci, ci)
            z=np.round(Mi@np.vstack([a,b])); best=np.full(h,np.inf)
            for i in range(-R,R+1):
                for j in range(-R,R+1):
                    w=M@(z+np.array([[i],[j]])); best=np.minimum(best,np.maximum(np.abs(a-w[0]),np.abs(b-w[1])))
            G[n]=best; ci=(ci*eW)%h
        pm=np.minimum.reduce([np.maximum(G[n],G[(n+p)%(2*p)]) for n in range(2*p)])
        D=max(L['dplus'],L['dminus']); kind='binet' if len(set(L['signs']))==1 else 'cross'
        Q=float(pm[prim].min()); k=int(np.argmin(np.where(prim,pm,np.inf)))
        row=dict(p=p,signs=L['signs'],kind=kind,D=D,min_pairmax=Q,ratio_to_sqrtD=Q/math.sqrt(D),argc=k,
                 min_pairmax_nonprim=float(pm[~prim & (c!=0)].min()) if (~prim&(c!=0)).any() else None,
                 frac_pairmax_lt_10=float((pm[prim]<10).mean()))
        out.append(row); print(json.dumps(row),flush=True)
    return out
if __name__=='__main__':
    p=int(sys.argv[1]); r=run(p); json.dump(r,open(f'/workspace/research1105b/logs/lemmaS_p{p}.json','w'),indent=1)
