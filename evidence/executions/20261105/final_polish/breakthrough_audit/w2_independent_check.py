# independent: e(p)>=2 iff alpha^N == 1 mod p^2 (N/d coprime to p)
import sys
L=int(sys.argv[1])
s=bytearray([1])*(L+1); s[0]=s[1]=0
for i in range(2,int(L**.5)+1):
    if s[i]: s[i*i::i]=bytearray(len(range(i*i,L+1,i)))
def mul(x,y,m): return ((x[0]*y[0]+2*x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m)
def pw(b,e,m):
    r=(1,0)
    while e:
        if e&1: r=mul(r,b,m)
        b=mul(b,b,m); e>>=1
    return r
hits=[];cnt=0
for p in range(3,L+1,2):
    if not s[p]: continue
    cnt+=1
    N=p-1 if p%8 in (1,7) else p+1
    m=p*p
    if pw((3,2),N,m)==(1,0): hits.append(p)
print(L,'odd primes',cnt,'e>=2 at',hits)
