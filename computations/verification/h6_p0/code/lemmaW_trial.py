"""P4 (2) [N, exact integer arithmetic]: for every odd prime p<500, find EVERY prime q<1e8 dividing h_p=(eps^p+epsbar^p)/2,
eps=1+sqrt2, by testing ALL primes q in [3,1e8) (no residue-class presieve, so the test does not presuppose Lemma W),
and check q = +-1 mod 2p. h_p mod q via (1+sqrt2)^p mod q in Z[sqrt2]/q, vectorised in int64 (q<1e8 -> products <1e16).
Each hit is re-confirmed with exact big-int h_p % q."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import os as _os
HERE=_os.path.dirname(_os.path.abspath(__file__)); LOGS=_os.path.join(_os.path.dirname(HERE),'logs')
import numpy as np, sympy, json, time
N=10**8
sieve=np.ones(N,dtype=bool); sieve[:2]=False
for i in range(2,int(N**.5)+1):
    if sieve[i]: sieve[i*i::i]=False
Q=np.nonzero(sieve)[0].astype(np.int64); Q=Q[Q>2]
def hp_exact(p):
    a,b=1,1  # h_n: h0=1,h1=1, h_n=2h_{n-1}+h_{n-2}
    for _ in range(p-1): a,b=b,2*b+a
    return b
def powmod(p):
    # (x+y sqrt2)^p mod Q, start (1,1)
    rx=np.ones_like(Q); ry=np.zeros_like(Q); bx=np.ones_like(Q); by=np.ones_like(Q); e=p
    while e:
        if e&1: rx,ry=(rx*bx+2*(ry*by%Q))%Q,(rx*by+ry*bx)%Q
        bx,by=(bx*bx+2*(by*by%Q))%Q,(2*(bx*by%Q))%Q
        e>>=1
    return rx  # h_p = rational part
out=[];viol=0;t0=time.time()
import sys
START=int(sys.argv[1]) if len(sys.argv)>1 else 3
for p in sympy.primerange(START,500):
    r=powmod(p); hits=Q[r==0]; H=hp_exact(p)
    hits=[int(q) for q in hits if H%int(q)==0]
    bad=[q for q in hits if (q%(2*p)) not in (1,2*p-1)]
    viol+=len(bad)
    out.append(dict(p=p,factors_below_1e8=hits,violations=bad,odd=H%2==1))
    print(p,hits,'VIOL' if bad else 'ok',flush=True)
json.dump(dict(N=N,primes_tested=int(len(Q)),results=out,total_violations=viol,sec=time.time()-t0),open(LOGS+"/lemmaW_trial.json" if START==3 else LOGS+"/lemmaW_trial_from%d.json"%START,"w"),indent=0)
print('total violations',viol)
