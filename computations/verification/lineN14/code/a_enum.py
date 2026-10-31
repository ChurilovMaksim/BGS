"""N14 (A) pre-flight [N, float]: EXACT enumeration of all classes alpha in O mod +-eps^Z (fundamental domain 1<=|s1/s2|<lam, s1>0)
with |N(alpha)| < 2^Jmax.  Seed e = 2 alpha covers both backgrounds exactly once (bg 1/4: N(alpha) odd; bg 0: alpha in sqrt2 O).
Per class: window weights r_A, r_B (N12 float sector-4 operator, KK padding), |w| = |r_A r_B|^3, and the eps-chain digit word
(code/digits.py) -> max internal zero-run g.  Output jsonl one line per class."""
import sys, json, math, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code')
import fastops as F, digits as Dg
Jmin,Jmax,KK=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]); out=sys.argv[4]
r2=math.sqrt(2); lamf=3+2*r2
def reps(lo,hi):
    X1max=math.sqrt(hi*lamf); B=int(X1max/r2)+2; res=[]
    for b in range(-B,B+1):
        for a in range(-int(X1max)-2,int(X1max)+3):
            x1=a+b*r2; x2=a-b*r2
            if x1<=0 or x2==0: continue
            N=abs(a*a-2*b*b)
            if not (lo<=N<hi): continue
            if 1<=x1/abs(x2)<lamf*(1-1e-12): res.append((a,b,N))
    return res
f=open(out,'a'); t0=time.time()
for j in range(Jmin,Jmax+1):
    R=reps(2**j,2**(j+1)) if j>0 else reps(1,2)
    for i0 in range(0,len(R),64):
        chunk=R[i0:i0+64]; seqs=[]; words=[]
        for (a,b,N) in chunk:
            ea,eb=2*a,2*b
            zA,zB=Dg.seeds(ea,eb); seqs.append(Dg.core(zA,KK)); seqs.append(Dg.core(zB,KK))
            w,g,_=Dg.eps_digits(ea,eb,6); words.append((w,g))
        rr=F.weights_batch(seqs)
        for k,(a,b,N) in enumerate(chunk):
            rA,rB=rr[2*k],rr[2*k+1]; w,g=words[k]
            f.write(json.dumps(dict(j=j,a=a,b=b,N=N,rA=[rA.real,rA.imag],rB=[rB.real,rB.imag],absw=abs(rA*rB)**3,
                    rArB2=abs(rA*rB)**2,span=len(w),zr=g,word=[int(x) for x in w]))+'\n')
        f.flush()
    print(j,len(R),round(time.time()-t0,1),flush=True)
