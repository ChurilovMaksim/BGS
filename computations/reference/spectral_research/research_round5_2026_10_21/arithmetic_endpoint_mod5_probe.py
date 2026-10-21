"""Exact finite-field discriminator for endpoint-minor valuation claims.

Builds F_(5^6) using a verified irreducible degree-six polynomial. Checks
primitive Nth-root order and evaluates actual seven-chain extreme Fourier
minors for N dividing 5^6-1. Zero reductions refute a proposed unit claim;
nonzero reductions certify only those specific Fourier minors.
"""
from functools import lru_cache
import argparse
import itertools
from arithmetic_endpoint_minor_probe import bounded_compositions, endpoint_sets

P = 5


def trim(v):
    v=[x%P for x in v]
    while v and v[-1]==0:
        v.pop()
    return tuple(v)


def padd(a,b):
    return trim([(a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0)
                 for j in range(max(len(a),len(b)))])


def psub(a,b):
    return padd(a,tuple(-x for x in b))


def prem(a,b):
    a=list(trim(a))
    b=trim(b)
    u=pow(b[-1],-1,P)
    while len(a)>=len(b):
        d=len(a)-len(b)
        v=a[-1]*u%P
        for j,c in enumerate(b):
            a[d+j]=(a[d+j]-v*c)%P
        a=list(trim(a))
    return tuple(a)


def pgcd(a,b):
    while b:
        a,b=b,prem(a,b)
    return trim([x*pow(a[-1],-1,P) for x in a])


def rawmul(a,b):
    if not a or not b:
        return ()
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return trim(c)


def ppow(a,n,mod):
    ans=(1,)
    while n:
        if n&1:
            ans=prem(rawmul(ans,a),mod)
        a=prem(rawmul(a,a),mod)
        n//=2
    return ans


def choose_modulus():
    x=(0,1)
    for a,b,c in itertools.product(range(5),range(5),range(1,5)):
        f=(c,b,a,0,0,0,1)
        if ppow(x,5**6,f)!=x:
            continue
        if pgcd(psub(ppow(x,5**3,f),x),f)!=(1,):
            continue
        if pgcd(psub(ppow(x,5**2,f),x),f)!=(1,):
            continue
        return f
    raise RuntimeError("No irreducible polynomial in the selected search.")


class Field:
    def __init__(self,modulus):
        self.f=modulus

    @lru_cache(None)
    def mul(self,a,b):
        return prem(rawmul(a,b),self.f)

    def power(self,a,n):
        ans=(1,)
        while n:
            if n&1:
                ans=self.mul(ans,a)
            a=self.mul(a,a)
            n//=2
        return ans

    @lru_cache(None)
    def inv(self,a):
        if not a:
            raise ZeroDivisionError
        z=self.power(a,5**6-2)
        assert self.mul(z,a)==(1,)
        return z

    def det(self,matrix):
        A=[list(row) for row in matrix]
        out=(1,)
        for j in range(len(A)):
            pivot=next((i for i in range(j,len(A)) if A[i][j]),None)
            if pivot is None:
                return ()
            if pivot!=j:
                A[pivot],A[j]=A[j],A[pivot]
                out=trim([-x for x in out])
            piv=A[j][j]
            out=self.mul(out,piv)
            iv=self.inv(piv)
            for i in range(j+1,len(A)):
                factor=self.mul(A[i][j],iv)
                if not factor:
                    continue
                for k in range(j+1,len(A)):
                    A[i][k]=psub(A[i][k],self.mul(factor,A[j][k]))
                A[i][j]=()
        return out


def prime_factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:
                n//=p
        p+=1
    if n>1:
        out.append(n)
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--n",type=int,default=3)
    parser.add_argument("--max-total",type=int,default=5)
    parser.add_argument("--limit",type=int,default=10)
    parser.add_argument("--embedding",type=int,default=1)
    args=parser.parse_args()
    n,N=args.n,7*args.n
    assert (5**6-1)%N==0
    F=Field(choose_modulus())
    z=None
    for coeff in itertools.product(range(5),repeat=6):
        a=trim(coeff)
        if not a:
            continue
        r=F.power(a,(5**6-1)//N)
        if F.power(r,N)==(1,) and all(F.power(r,N//p)!=(1,) for p in prime_factors(N)):
            z=r
            break
    assert z is not None
    z=F.power(z,args.embedding)
    assert F.power(z,N)==(1,) and all(F.power(z,N//p)!=(1,) for p in prime_factors(N))
    print("field_modulus_ascending =",F.f,"primitive_root =",z,flush=True)
    roots=[F.power(z,k) for k in range(N)]
    for k in range(1,args.max_total+1):
        tested=0
        zeros=[]
        for counts in bounded_compositions(k,7,n):
            I,J=endpoint_sets(n,counts)
            d=F.det([[roots[i*j%N] for j in J] for i in I])
            tested+=1
            if not d:
                zeros.append(counts)
        print("N =",N,"k =",k,"tested =",tested,"zero reductions =",len(zeros),
              "examples =",zeros[:args.limit],flush=True)


if __name__=="__main__":
    main()
