# Line N [N]: p^3-smooth part of h_{3p} (excluding 7) for primes p <= PMAX, by trial division over q = 1 mod 2p, q <= p^3.
# Every prime q != 7 dividing h_{3p} has rank p or 3p and q = +-1 mod 8, so q = 1 mod 2p (checked in n1 logs).
import sys, json, math, gmpy2
from gmpy2 import mpz
from sympy import primerange
def hseq(M):
    x,y=mpz(1),mpz(1); out={1:mpz(1)}
    for m in range(2,M+1):
        x,y=x+2*y,x+y
        if m%2: out[m]=x
    return out
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 1000
H=hseq(3*PMAX+3)
out=open(f'/workspace/bgs-lineN/logs/n4_smooth_P{PMAX}.jsonl','w')
for p in primerange(5,PMAX+1):
    N=H[3*p]; v7=0
    while N%7==0: N//=7; v7+=1
    logN=float(gmpy2.log(N)); small=[]
    B=p**3; q=2*p+1
    while q<=B:
        if N%q==0:
            e=0
            while N%q==0: N//=q; e+=1
            small.append((q,e))
        q+=2*p
    rec=dict(p=p,log_h_over7=logN,small_primes=[[int(a),b] for a,b in small],
             logfrac_smooth=1-float(gmpy2.log(N))/logN if N>1 else 1.0, p3_smooth=bool(N==1),
             n_le_p2=sum(1 for a,_ in small if a<=p*p), n_p2_p3=sum(1 for a,_ in small if a>p*p))
    out.write(json.dumps(rec)+"\n"); out.flush()
    print(p, rec['n_le_p2'], rec['n_p2_p3'], round(rec['logfrac_smooth'],4), rec['p3_smooth'], flush=True)
