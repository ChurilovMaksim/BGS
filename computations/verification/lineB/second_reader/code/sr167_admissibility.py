"""Second reader, BGS-TRACE-167 (automatic admissibility).  Fresh code (no project / referee code).
In O/hO with O=Z[lambda]=Z[sqrt8], lambda=3+sqrt8, h=h_m (odd m):
 (a) lambda^d is never k'/k (k != k' in K = support of the kick symbol, |k|<=9)  [as an element of F_h embedded diagonally]
 (b) lambda^a + lambda^b = 6 only for {a,b} = {1,-1} mod m.
Exhaustive check over d, a in Z/m (b found by lookup).  Also: 2 is a QR mod every prime p | h_m (so O/hO is always SPLIT
when h is prime), the four roots of t^2-6t+1 in F_h x F_h, and which roots have norm 1 (are in <lambda>).  Controls: m=3
(h=7 < 18) and composite h_m."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, json
from sympy import isprime, sqrt_mod, factorint
K=[1,2,5,6,7,8,9,-1,-2,-5,-6,-7,-8,-9]
def pell(m):
    x,y=1,0
    for _ in range(m): x,y=3*x+8*y,x+3*y
    return x,y
def hm(m):
    x,y=pell(m); D=2*(x-1); import math; h=math.isqrt(D//4); assert 4*h*h==D; return h
def check(m):
    h=hm(m); out=dict(m=m,h_digits=len(str(h)),h_prime=bool(isprime(h)))
    if h<10**12: out['h']=h
    s=sqrt_mod(8,h) if out['h_prime'] else None
    if s is None:
        out['note']='h not prime: skipped (lemma hypothesis fails)'; return out
    assert (s*s-8)%h==0
    l1,l2=(3+s)%h,(3-s)%h; assert l1*l2%h==1          # images of lambda, lambda^{-1}
    # order of lambda in (O/h)^x = order of l1 in F_h^x (l2=l1^{-1})
    pw=[1]; 
    for d in range(1,2*m+1): pw.append(pw[-1]*l1%h)
    ordl=min(d for d in range(1,2*m+1) if pw[d]==1); out['ord_lambda']=ordl
    inv=lambda a: pow(a,-1,h)
    R={(kp*inv(k%h))%h for k in K for kp in K if kp!=k and k%h}
    out['k_divisible_by_h']=[k for k in K if k%h==0]
    # (a)
    bad_a=[]
    for d in range(m):
        a1,a2=pw[d],inv(pw[d])
        if a1==a2 and a1 in R: bad_a.append(d)
    out['a_violations']=bad_a
    # diagonal powers of lambda (lambda^d in F_h) : must be only +-1
    out['diag_powers']=sorted({pw[d] if pw[d]<h//2 else pw[d]-h for d in range(m) if pw[d]==inv(pw[d])})
    # (b)
    idx={pw[d]:d for d in range(m)}
    sols=[]
    for a in range(m):
        u1,u2=pw[a],inv(pw[a]); v1,v2=(6-u1)%h,(6-u2)%h
        b=idx.get(v1)
        if b is not None and inv(pw[b])==v2: sols.append((a,b))
    out['b_solutions']=sols; out['b_ok']=sorted(sols)==sorted([(1,m-1),(m-1,1)])
    # roots of t^2-6t+1 in F_h x F_h and their norms u*sigma(u)
    roots=[(x,y) for x in (l1,l2) for y in (l1,l2)]
    out['roots_norm']={f'({ "l1" if x==l1 else "l2"},{ "l1" if y==l1 else "l2"})':(x*y)%h==1 for x,y in roots}
    out['a_ok']=not bad_a; return out
def qr2_all_prime_factors(m):
    h=hm(m); f=factorint(h); return {int(p):(pow(2,(p-1)//2,p)==1) for p in f}
if __name__=='__main__':
    res=[]
    for m in [3,5,7,19,29,47,59,163,257,421,937,947,1493]:
        r=check(m); res.append(r); print(json.dumps(r),flush=True)
    # controls with composite h: does (a) or (b) fail?  (no claim made there)
    for m in [9,11,13,15,21]:
        h=hm(m); f=factorint(h); print(json.dumps(dict(m=m,h=h,factors={str(k):v for k,v in f.items()},qr2=qr2_all_prime_factors(m))))
    # 2 is a QR mod every prime factor of h_m, odd m<=61 (=> O/pO split): analytic reason 2B^2 = h^2+1
    allqr=all(all(qr2_all_prime_factors(m).values()) for m in range(3,62,2) if len(str(hm(m)))<40)
    print('2 is QR mod every prime factor of h_m for odd m<=61 (h<1e40):',allqr)
    ok=[r for r in res if r.get('h_prime')]
    print('SUMMARY (a) holds for', [r['m'] for r in ok if r['a_ok']], ' fails for', [r['m'] for r in ok if not r['a_ok']])
    print('SUMMARY (b) holds for', [r['m'] for r in ok if r['b_ok']], ' fails for', [r['m'] for r in ok if not r['b_ok']])
    print('SUMMARY ord_h(lambda)=m for all:', all(r['ord_lambda']==r['m'] for r in ok))
