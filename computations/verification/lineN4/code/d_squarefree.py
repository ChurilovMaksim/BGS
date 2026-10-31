"""N4 (D) [N]: Wieferich-type check for N3-F8.  q | h_p (p odd prime) iff ord_q(lambda) = p (lambda = 3+2sqrt2 in (O/q)^*).
For every prime q < QMAX, q != 2, find ord_q(lambda); if it is an odd prime p <= PMAX, test q^2 | h_p via lambda^p mod q^2 (h_p = eps^-p (lambda^p - 1)/2).
Reports all such (p,q) with q < QMAX and whether q^2 | h_p."""
import sys, json
from sympy import primerange, factorint, isprime
QMAX=int(sys.argv[1]); PMAX=int(sys.argv[2])
def mul(a,b,M): return ((a[0]*b[0]+2*a[1]*b[1])%M,(a[0]*b[1]+a[1]*b[0])%M)
def pw(a,e,M):
    r=(1,0)
    while e:
        if e&1: r=mul(r,a,M)
        a=mul(a,a,M); e>>=1
    return r
L=(3,2); hits=[]; sq=[]
for q in primerange(3,QMAX):
    N= q-1 if pow(2,(q-1)//2,q)==1 else q+1      # split: order | q-1; inert: norm-1 elements have order | q+1
    o=N
    for f in factorint(N):
        while o%f==0 and pw(L,o//f,q)==(1,0): o//=f
    if o<=PMAX and o>2 and isprime(o):
        r=pw(L,o,q*q); div2 = (r==(1,0))   # lambda^p == 1 mod q^2  <=> q^2 | (lambda^p-1) = 2 h_p eps^p
        hits.append((o,q)); 
        if div2: sq.append((o,q))
res=dict(QMAX=QMAX,PMAX=PMAX,n_pairs=len(hits),square_hits=sq,first_pairs=sorted(hits)[:20])
print(json.dumps(res)); json.dump(res,open(f'logs/d_squarefree_{QMAX}_{PMAX}.json','w'),indent=1)
