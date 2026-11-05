"""research1105b [N]: low-norm truncation of the line sums X_line(a) = sum_{beta in a/hO, beta!=0} Zhat(beta)/Z0.
Enumerates gamma in the ideal a (norm h=h_p, sign pattern s_q per prime) with |N(gamma)| <= T*h, one representative per
<lam,-1>-orbit (fundamental domain 1 <= |g/g'| < lam^2, g>0 sign), beta = gamma mod h, orbit size 2p (Theorem 7 of grok47).
Reports the truncated sum, split by n = |N(gamma)|/h.  usage: lownorm.py p T [nproc]"""
import sys, math, json, itertools, time, numpy as np
sys.path.insert(0,'/workspace/research1105b/code'); from level import evaluate, canon
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import TW, Zbatch, nu_rho
from sympy import factorint, sqrt_mod
S2=math.sqrt(2); LAM=3+2*S2
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
def ideals(p,h):
    fac=sorted(factorint(h)); loc=[]
    for q in fac:
        w=int(sqrt_mod(2,q)); opts=[]
        for sg in (1,-1):
            ww=(sg*w)%q; s=pow((1+ww)%q,p,q); s=1 if s==1 else -1
            opts.append((ww,s))   # ideal: x == ww*y mod q  (sqrt2 -> -ww kills x+y sqrt2? check below)
        loc.append((q,opts))
    out=[]
    for ch in itertools.product(*[o for q,o in loc]):
        W=0; M=1
        for (q,_),(ww,s) in zip(loc,ch):
            W=W+M*(((ww-W)*pow(M,-1,q))%q); M*=q
        out.append((W,[s for ww,s in ch]))
    return out
def enum(h,W,T):
    # lattice {(x,y): x == W y mod h}; embed (x+y s2, x-y s2); want |N|<=T h, 1<=|g/g'|<lam^2
    B=np.array([[h,0],[W,1]],dtype=object)
    # Gauss-reduce in embedding norm
    def emb(v): return (float(v[0])+float(v[1])*S2, float(v[0])-float(v[1])*S2)
    def n2(v): a,b=emb(v); return a*a+b*b
    u,v=[int(h),0],[int(W),1]
    for _ in range(500):
        if n2(v)<n2(u): u,v=v,u
        a1,b1=emb(u); a2,b2=emb(v); mu=round((a1*a2+b1*b2)/(a1*a1+b1*b1))
        if mu==0: break
        v=[v[0]-mu*u[0],v[1]-mu*u[1]]
    R1=LAM*math.sqrt(T*h); R2=math.sqrt(T*h)
    # solve coefficients range: points c1 u + c2 v in box |g|<=R1, |g'|<=R2
    Mx=np.array([emb(u),emb(v)]).T; Minv=np.linalg.inv(Mx)
    corners=[Minv@np.array([sa*R1,sb*R2]) for sa in (1,-1) for sb in (1,-1)]
    c1m=int(max(abs(c[0]) for c in corners))+1; c2m=int(max(abs(c[1]) for c in corners))+1
    pts=[]
    for c1 in range(-c1m,c1m+1):
        for c2 in range(-c2m,c2m+1):
            x=c1*u[0]+c2*v[0]; y=c1*u[1]+c2*v[1]
            if x==0 and y==0: continue
            g=x+y*S2; gp=x-y*S2
            if g<=0: continue
            N=abs(x*x-2*y*y)
            if N>T*h: continue
            r=abs(g/gp)
            if not (1<=r<LAM*LAM): continue
            assert (x*x-2*y*y)%h==0
            pts.append((x,y,N//h))
    return pts
if __name__=='__main__':
    p=int(sys.argv[1]); T=float(sys.argv[2]); m=3*p; h=hp(p)
    hh,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); Z0=Zbatch(tw,np.zeros((1,m)))[0]
    res=dict(p=p,h=h,T=T,lines=[])
    for W,signs in ideals(p,h):
        t0=time.time(); pts=enum(h,W,T)
        # twist Tr(beta lam^i)/h is small iff beta/h is near the inverse different D^{-1}=(1/2sqrt2)O, so the short lift of beta
        # is gamma = 2sqrt2*beta (mod hO), gamma in a.  Hence beta = gamma*(2sqrt2)^{-1} = gamma*sqrt2*4^{-1} mod h.
        # The k1 kick ghat(n)=i^n J_n has a second resonant twist 1/2 (e(n/2) ghat(n) = conj-type), so twists near 1/2
        # (beta/h near (1/2)D^{-1}) are also 'core': include beta = gamma*(4sqrt2)^{-1} as well.
        i4=pow(4,-1,h); i8=pow(8,-1,h)
        bx=np.array([(2*y*i4)%h for x,y,n in pts]+[(2*y*i8)%h for x,y,n in pts],np.int64)
        by=np.array([(x*i4)%h for x,y,n in pts]+[(x*i8)%h for x,y,n in pts],np.int64)
        pts=pts+pts
        c=canon(bx,by,h,p); _,first=np.unique(c,return_index=True); dup=len(pts)-len(first)
        Zh=evaluate(m,nu0,h,bx[first],by[first]) if len(first) else np.zeros(0)
        # orbit under <lam,-1> has size 2p; canon also identifies conj -> other line, but conj of an element of a is in abar != a, so no merge within the line
        u=2*p*Zh/Z0; ns=np.array([pts[i][2] for i in first])
        byn={int(n):[float(u[ns==n].sum().real),float(u[ns==n].sum().imag),int((ns==n).sum())] for n in sorted(set(ns.tolist()))}
        kind='binet' if len(set(signs))==1 else 'cross'
        row=dict(signs=signs,kind=kind,npts=len(first),dups=dup,X_trunc=[float(u.sum().real),float(u.sum().imag)],abs_trunc=float(np.abs(u).sum()),
                 max_u=float(np.abs(Zh/Z0).max()) if len(Zh) else 0,by_n=byn,sec=round(time.time()-t0,1))
        res['lines'].append(row); print(json.dumps({k:v for k,v in row.items() if k!='by_n'}),flush=True)
    json.dump(res,open(f'/workspace/research1105b/logs/lownorm_p{p}_T{int(T)}.json','w'),indent=1)
