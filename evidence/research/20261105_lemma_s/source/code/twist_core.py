"""research1105b [CA, exact integer arithmetic]: core-site statistics on every ideal line of norm h_p.
Line a (cyclic of order h): beta = j*beta0, twist at site i: tau_i(j) = j*t_i mod h / h, t_i = Tr(beta0 lam^i) mod h.
Core site: tau within delta of 0 or 1/2 (the two resonant backgrounds of the k1 kick).  For every j in [1,h) we compute
  C(j) = #core sites in one period (p sites),  R(j) = longest cyclic run of core sites.
Reports per line: max C, max R, histogram tail, and the seam prediction p - log_lam D, D = max(d_+, d_-).
usage: twist_core.py p [delta_num delta_den]"""
import sys, math, json, itertools, numpy as np
from sympy import factorint, sqrt_mod
LAM=3+2*math.sqrt(2)
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
def lines(p,h):
    qs=sorted(factorint(h)); loc=[]
    for q in qs:
        w=int(sqrt_mod(2,q)); opts=[]
        for s in (1,-1):
            # line L_s: x == s*w*y (mod q): beta = y*(s w + sqrt2); kernel of sqrt2 -> -s w ... eps^p sign under sqrt2 -> -s w
            e=(1-s*w)%q; v=pow(e,p,q); opts.append((s*w%q, 1 if v==1 else -1))
        loc.append((q,opts))
    out=[]
    for ch in itertools.product(*[o for q,o in loc]):
        W=0; M=1
        for (q,_),(sw,sg) in zip(loc,ch):
            W=W+M*(((sw-W)*pow(M,-1,q))%q); M*=q
        dplus=int(np.prod([q for (q,_),(sw,sg) in zip(loc,ch) if sg==1])); dminus=h//dplus
        out.append(dict(W=W,signs=[sg for sw,sg in ch],dplus=dplus,dminus=dminus))
    return out
def run(p,dn=1,dd=8):
    h=hp(p); res=dict(p=p,h=h,delta=f'{dn}/{dd}',lines=[])
    for L in lines(p,h):
        bx,by=L['W'],1                                    # beta0 = W + sqrt2  (x == W y), generates the line mod h
        t=[]; x,y=1,0
        for i in range(p):
            t.append((2*(bx*x+2*by*y))%h); x,y=(3*x+4*y)%h,(2*x+3*y)%h
        t=np.array(t,np.int64)
        maxC=0; maxR=0; hist=np.zeros(p+1,np.int64); histR=np.zeros(p+1,np.int64); argC=None
        CH=4_000_000
        for j0 in range(1,h,CH):
            j=np.arange(j0,min(h,j0+CH),dtype=np.int64)
            core=np.zeros((len(j),p),bool)
            for i in range(p):
                r=(j*t[i])%h                                # exact
                # distance to {0, h/2}: core iff min(r, h-r) < h*dn/dd  or |2r - h| < 2h dn/dd
                a=np.minimum(r,h-r)*dd < h*dn
                b=np.abs(2*r-h)*dd < 2*h*dn
                core[:,i]=a|b
            C=core.sum(1); hist+=np.bincount(C,minlength=p+1)
            # longest cyclic run
            cc=np.concatenate([core,core],1); run_=np.zeros(len(j),np.int64); best=np.zeros(len(j),np.int64)
            for i in range(2*p):
                run_=np.where(cc[:,i],run_+1,0); best=np.maximum(best,run_)
            best=np.minimum(best,p); histR+=np.bincount(best,minlength=p+1)
            k=int(np.argmax(C))
            if C[k]>maxC: maxC=int(C[k]); argC=int(j[k])
            maxR=max(maxR,int(best.max()))
        D=max(L['dplus'],L['dminus'])
        kind='binet' if len(set(L['signs']))==1 else 'cross'
        row=dict(signs=L['signs'],kind=kind,dplus=L['dplus'],dminus=L['dminus'],maxC=maxC,argmaxC=argC,maxR=maxR,
                 seam_pred=p-math.log(D)/math.log(LAM) if kind=='cross' else None,
                 histC_tail={int(k):int(v) for k,v in enumerate(hist) if k>=p//2 and v},
                 histR_tail={int(k):int(v) for k,v in enumerate(histR) if k>=p//4 and v})
        res['lines'].append(row); print(json.dumps(row),flush=True)
    return res
if __name__=='__main__':
    p=int(sys.argv[1]); dn,dd=(int(sys.argv[2]),int(sys.argv[3])) if len(sys.argv)>3 else (1,8)
    r=run(p,dn,dd); json.dump(r,open(f'/workspace/research1105b/logs/twist_core_p{p}_d{dn}_{dd}.json','w'),indent=1)
