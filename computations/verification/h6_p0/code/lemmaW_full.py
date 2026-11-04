"""P4 (2) [N]: complete factorisations of h_p (p prime < 500) where sympy finishes within 120 s per p;
check every prime factor q = +-1 mod 2p. Primality of cofactors: sympy.isprime (BPSW; plus for q<2^64 deterministic)."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import os as _os
HERE=_os.path.dirname(_os.path.abspath(__file__)); LOGS=_os.path.join(_os.path.dirname(HERE),'logs')
import sympy, json, multiprocessing as mp
def hp(p):
    a,b=1,1
    for _ in range(p-1): a,b=b,2*b+a
    return b
def work(p):
    H=hp(p); f=sympy.factorint(H, use_ecm=True)
    return p,{int(q):e for q,e in f.items()}
if __name__=='__main__':
    out=[]
    with mp.Pool(6) as pool:
        jobs={p:pool.apply_async(work,(p,)) for p in sympy.primerange(3,500)}
        for p,j in jobs.items():
            try:
                _,f=j.get(timeout=120)
                prod=1
                for q,e in f.items(): prod*=q**e
                assert prod==hp(p)
                bad=[q for q in f if q%(2*p) not in (1,2*p-1)]
                sqfree=all(e==1 for e in f.values())
                allprime=all(sympy.isprime(q) for q in f)
                r=dict(p=p,full=True,factors=f,violations=bad,squarefree=sqfree,omega=len(f),digits=len(str(hp(p))),all_prime_BPSW=allprime)
            except mp.TimeoutError:
                r=dict(p=p,full=False,digits=len(str(hp(p))))
            out.append(r); print(json.dumps({k:(str(v) if k=='factors' else v) for k,v in r.items()}),flush=True)
    json.dump(out,open(LOGS+'/lemmaW_full.json','w'),default=str,indent=0)
