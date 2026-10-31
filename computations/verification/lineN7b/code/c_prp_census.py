"""N7b (E) [N]: BPSW-PRP census of h_p and K'=K_p/7 = (4h_p^2+3)/7 for primes 5<=p<=PMAX (p!=7).  Records which p have
h_p PRP, K' PRP, both.  Heuristic comparison: expected counts sum_p e^gamma*log(2p)/log(h_p) etc. usage: c_prp_census.py PMAX"""
import sys, json, math, gmpy2
from sympy import primerange
PMAX=int(sys.argv[1]); out=open(f'/workspace/bgs-lineN/N7b/logs/c_prp_census_{PMAX}.jsonl','w')
eg=math.exp(0.5772156649); LAM=3+2*math.sqrt(2)
Eh=EK=Eb=0.0
for p in primerange(5,PMAX+1):
    x,y=gmpy2.mpz(1),gmpy2.mpz(1)
    for _ in range(p-1): x,y=x+2*y,x+y
    h=x; K=4*h*h+3; assert K%7==0; Kp=K//7
    if p==7: Kp//=7
    a=bool(gmpy2.is_bpsw_prp(h)); b=bool(gmpy2.is_bpsw_prp(Kp))
    # Wagstaff-type heuristic: Prob(prime) ~ e^gamma * log(2r)/log N for numbers whose factors are = 1 mod 2r (r=p or 3p)
    ph=min(1,eg*math.log(2*p)/(p/2*math.log(LAM))); pk=min(1,eg*math.log(6*p)/(p*math.log(LAM)))
    Eh+=ph; EK+=pk; Eb+=ph*pk
    out.write(json.dumps(dict(p=p,hp_prp=a,Kq_prp=b,Eh=Eh,EK=EK,Eboth=Eb))+'\n'); out.flush()
