"""Independent ECPP certificate checker (own implementation of the Atkin-Morain/Goldwasser-Kilian criterion,
pure Python big ints, affine arithmetic with honest unit checks). Also cross-checks with PARI primecertisvalid,
and recomputes h_m = (Tr S^m - 2)^{1/2}/2 from S=[[3,4],[2,3]] directly."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, ast, math, gmpy2
from math import gcd, isqrt
CERTDIR=__import__('os').path.normpath(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', 'ecpp'))
def hm(m):
    a,b,c,d=1,0,0,1
    for _ in range(m): a,b,c,d=3*a+2*b,4*a+3*b,3*c+2*d,4*c+3*d   # M*S
    D=a+d-2; r=isqrt(D); assert r*r==D and r%2==0; return r//2
class Fail(Exception): pass
def inv(a,N):
    a%=N; g=gcd(a,N)
    if g!=1: raise Fail('non-invertible denominator gcd=%d'%g)
    return pow(a,-1,N)
O=None
def add(P,Q,a,N):
    if P is O: return Q
    if Q is O: return P
    x1,y1=P; x2,y2=Q
    if (x1-x2)%N==0:
        if (y1+y2)%N==0: return O
        if (y1-y2)%N!=0: raise Fail('x equal, y neither equal nor opposite')
        l=(3*x1*x1+a)*inv(2*y1,N)%N
    else: l=(y2-y1)*inv(x2-x1,N)%N
    x3=(l*l-x1-x2)%N; return (x3,(l*(x1-x3)-y1)%N)
def mul(k,P,a,N):
    R=O; Q=P
    while k:
        if k&1: R=add(R,Q,a,N)
        Q=add(Q,Q,a,N); k>>=1
    return R
def bound_ok(q,N):   # q > (N^{1/4}+1)^2  <=>  (q^2+6q+1-N)^2 > 16(q+1)^2 q  with lhs base positive
    L=q*q+6*q+1-N
    return L>0 and L*L>16*(q+1)**2*q
def small_prime_proof(n):
    if n<2: return False
    if n<10**14:
        return all(n%p for p in range(2,isqrt(n)+1)) if n>3 else True
    # deterministic MR for n < 3.317e24 (Sorenson-Webster bases)
    assert n<3317044064679887385961981
    d=n-1; s=0
    while d%2==0: d//=2; s+=1
    for b in [2,3,5,7,11,13,17,19,23,29,31,37,41]:
        x=pow(b,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True
def check(cert,Nexp):
    assert cert[0][0]==Nexp, 'cert N != h_m'
    for i,(N,t,s,a4,P) in enumerate(cert):
        N,t,s,a4=int(N),int(t),int(s),int(a4); x,y=int(P[0]),int(P[1])
        if gcd(N,6)!=1: raise Fail('gcd(N,6)')
        mm=N+1-t
        if mm%s: raise Fail('s does not divide m')
        q=mm//s
        b=(y*y-x**3-a4*x)%N
        if gcd(4*a4**3+27*b*b,N)!=1: raise Fail('singular curve')
        if not bound_ok(q,N): raise Fail('q too small')
        Q=mul(s,(x%N,y%N),a4%N,N)
        if Q is O: raise Fail('[s]P = O')
        if mul(q,Q,a4%N,N) is not O: raise Fail('[q][s]P != O')
        nxt=cert[i+1][0] if i+1<len(cert) else None
        if nxt is not None and int(nxt)!=q: raise Fail('chain broken')
    last=q
    if not small_prime_proof(last): raise Fail('last q not prime')
    return len(cert), last
if __name__=='__main__':
    import cypari2; pari=cypari2.Pari(); pari.allocatemem(2*10**9)
    ms=[int(a) for a in sys.argv[1].split(',')]
    for m in ms:
        h=hm(m)
        cert=ast.literal_eval(open(f'{CERTDIR}/cert_h{m}.txt').read().strip())
        try: steps,last=check(cert,h); ok='VALID'
        except Fail as e: ok='INVALID: '+str(e); steps=last=None
        pv=pari.primecertisvalid(pari(str(cert)))
        bpsw=gmpy2.is_bpsw_prp(h)
        print(f'm={m} digits={len(str(h))} own_checker={ok} steps={steps} last_q={last} pari_primecertisvalid={pv} gmpy2_BPSW={bpsw}',flush=True)
    # negative control: tamper with one certificate
    cert=ast.literal_eval(open(f'{CERTDIR}/cert_h163.txt').read().strip())
    cert[2][4][0]=int(cert[2][4][0])+1
    try: check(cert,hm(163)); print('CONTROL tampered: accepted (BAD)')
    except Exception as e: print('CONTROL tampered cert rejected:',e)
    try: check([[hm(163)*3]+list(cert[0][1:])],hm(163)*3)
    except Exception as e: print('CONTROL composite N rejected:',e)
