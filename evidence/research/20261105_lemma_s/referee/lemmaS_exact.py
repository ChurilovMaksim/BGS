# Independent referee check of Lemma S. Exact: G(x)=min_{a+b r = x mod h} |a|+sqrt2|b|  (height of a+b sqrt2 = |a|+sqrt2|b|)
import sys, math, itertools, json, numpy as np
from sympy import factorint, sqrt_mod
S2=math.sqrt(2)
def H(p):  # h_p = N(eps^p-1)/2 = (eps^p+epsbar^p)/2
    e=(1,1); x=(1,0)
    for _ in range(p): x=(x[0]+2*x[1], x[0]+x[1])
    return x[0]//1 if False else (x[0])  # x = eps^p = a+b sqrt2 ; Q_p/2 = a
def run(p):
    h=H(p); f=factorint(h); qs=sorted(f); assert all(v==1 for v in f.values())
    res=[]
    for ch in itertools.product(*[[int(sqrt_mod(2,q)), q-int(sqrt_mod(2,q))] for q in qs]):
        # line abar: kernel of sqrt2 -> r ; CRT r
        r=0;M=1
        for q,rq in zip(qs,ch): r=r+M*(((rq-r)*pow(M,-1,q))%q); M*=q
        assert (r*r-2)%h==0
        e=pow(1+r,p,h); sig=[1 if e%q==1 else (-1 if e%q==q-1 else 0) for q in qs]; assert 0 not in sig
        dp=math.prod(q for q,s in zip(qs,sig) if s==1); dm=h//dp; D=max(dp,dm)
        x=np.arange(h,dtype=np.int64)
        G=np.minimum(x,h-x).astype(float); b=0
        while S2*(b+1) < G.max()+1e-9:
            b+=1
            for sb in (b,-b):
                t=(x-sb*r)%h; G=np.minimum(G,S2*b+np.minimum(t,h-t))
        prim=np.ones(h,bool)
        for q in qs: prim&=(x%q!=0)
        Ge=G[(x*e)%h]
        pm=np.maximum(G,Ge); sm=G+Ge
        kind='binet' if len(set(sig))==1 else 'cross'
        k=int(np.argmin(np.where(prim,pm,np.inf)))
        row=dict(p=p,h=h,qs=qs,signs=sig,kind=kind,dplus=dp,dminus=dm,D=D,Bmax=b,maxG=float(G.max()),
                 Q=float(pm[prim].min()),Q_over_sqrtD=float(pm[prim].min()/math.sqrt(D)),argx=k,
                 minsum_over_sqrtD=float(sm[prim].min()/math.sqrt(D)),
                 lemma_ok=bool((sm[prim]**2 >= D*(1-1e-12)).all()),
                 min_sum_nonprim_nonzero=float(sm[(~prim)&(x!=0)].min()) if ((~prim)&(x!=0)).any() else None)
        res.append(row); print(json.dumps(row),flush=True)
    return res
if __name__=='__main__':
    out=[]
    for p in map(int,sys.argv[1:]): out+=run(p)
    json.dump(out,open(f'lemmaS_exact_{"_".join(sys.argv[1:])}.json','w'),indent=1)
