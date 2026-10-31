"""N7b [N]: slow time of level-c periodic orbits near the sector-4 fixed point z4 (constant twist 1/2).
slow(y) = #{i in [0,r): |tau_i - 1/2|, |tau_{i+1} - 1/2| < eps (mod 1)}, tau_i = Tr(beta lam^i)/c, r = ord_c(lam).
(The pair (tau_i,tau_{i+1}) is a linear coordinate of lam^i y on the torus, and z4 <-> (1/2,1/2).)
For iso lines at prime Q (all Q-1 points of a line, exact) and unit points (exact for c<=CFULL, else NU random).
Reports s_max per period, #windows of argmax, log_lam c.  Conjecture S(c) tested: s_max <= 2 log_lam c + C.  usage: d_slow.py PMAX QMAX"""
import sys, json, math, random, numpy as np
from sympy import factorint, sqrt_mod, primerange, n_order
PMAX=int(sys.argv[1]); QMAX=int(sys.argv[2]); EPS=1/16; CFULL=1500; NU=100000; LAM=3+2*math.sqrt(2)
random.seed(1); rng=np.random.default_rng(1)
out=open(f'/workspace/bgs-lineN/N7b/logs/d_slow_P{PMAX}_Q{QMAX}.jsonl','w')
def hpf(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
def lampows(r,c):
    xs=[];ys=[];x,y=1,0
    for i in range(r+1): xs.append(x%c); ys.append(y%c); x,y=(3*x+4*y)%c,(2*x+3*y)%c
    return np.array(xs,dtype=np.int64),np.array(ys,dtype=np.int64)
def order(c):
    x,y=3%c,2%c; r=1
    while not (x==1%c and y==0): x,y=(3*x+4*y)%c,(2*x+3*y)%c; r+=1
    return r
def slow_stats(G,c,r):   # G: (N, r+1) twist numerators mod c
    t=G.astype(np.float64)/c; d=np.abs(((t-0.5)+0.5)%1.0-0.5) < EPS
    sl=d[:,:-1]&d[:,1:]; s=sl.sum(1); k=int(np.argmax(s))
    row=sl[k]; wins=int(np.sum(row & ~np.roll(row,1))) if row.any() else 0
    if row.all(): wins=1
    return int(s[k]),wins,float(s.mean())
for p in primerange(5,PMAX+1):
    hp=hpf(p); K=4*hp*hp+3
    fh=factorint(hp,limit=QMAX); fk=factorint(K,limit=QMAX)
    cands=[(q,'h') for q in fh if q<=QMAX and q>7]+[(q,'K') for q in fk if q<=QMAX and q>7]
    for Q,src in cands:
        if not __import__('sympy').isprime(Q): continue
        r=order(Q); xs,ys=lampows(r,Q); lg=math.log(Q)/math.log(LAM)
        w=int(sqrt_mod(2,Q)); g=(2*(w*xs+2*ys))%Q
        smax=0;wbest=0;smean=0;N=0
        for s0 in range(1,Q,200000):
            s=np.arange(s0,min(Q,s0+200000),dtype=np.int64)[:,None]
            G=(s*g[None,:])%Q; a,b,mn=slow_stats(G,Q,r)
            if a>smax: smax,wbest=a,b
            smean+=mn*len(s); N+=len(s)
        rec=dict(p=p,c=Q,src=src,rank=r,type='iso',log_lam_c=lg,s_max=smax,windows=wbest,s_mean=smean/N,ratio=smax/lg)
        out.write(json.dumps(rec)+'\n'); out.flush()
        # unit points
        if Q<=CFULL:
            B=np.array([(x,y) for x in range(Q) for y in range(Q) if (x*x-2*y*y)%Q],dtype=np.int64)
        else:
            B=rng.integers(0,Q,size=(NU,2),dtype=np.int64); B=B[((B[:,0]*B[:,0]-2*B[:,1]*B[:,1])%Q)!=0]
        smax=0;wbest=0
        for i in range(0,len(B),100000):
            bb=B[i:i+100000]; G=(2*(bb[:,:1]*xs[None,:]+2*bb[:,1:]*ys[None,:]))%Q
            a,b,mn=slow_stats(G,Q,r)
            if a>smax: smax,wbest=a,b
        rec=dict(p=p,c=Q,src=src,rank=r,type='unit'+('_exact' if Q<=CFULL else '_sampled'),log_lam_c=lg,s_max=smax,windows=wbest,ratio=smax/(2*lg))
        out.write(json.dumps(rec)+'\n'); out.flush()
