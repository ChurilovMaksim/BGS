#!/usr/bin/env python3
"""Exact Q(i) independent hook / rooted-word / Euler-flow checks. No Monte Carlo."""
from fractions import Fraction as F
from itertools import product, permutations, combinations
from math import factorial, gcd
from functools import reduce, lru_cache
import json, pathlib, sys, time, hashlib, platform
class G:
    __slots__=('r','i')
    def __init__(self,r=0,i=0): self.r,self.i=F(r),F(i)
    def __add__(a,b):
        if not isinstance(b,G):b=G(b)
        return G(a.r+b.r,a.i+b.i)
    __radd__=__add__
    def __neg__(a):return G(-a.r,-a.i)
    def __sub__(a,b):return a+-b if isinstance(b,G) else a+G(-b)
    def __mul__(a,b):
        if not isinstance(b,G):b=G(b)
        return G(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
    __rmul__=__mul__
    def __truediv__(a,b):
        if not isinstance(b,G): b=G(b)
        z=b.r*b.r+b.i*b.i
        return a*G(b.r/z,-b.i/z)
    def __pow__(a,n):
        out=G(1)
        while n:
            if n&1:out=out*a
            n//=2;a=a*a
        return out
    def __bool__(a):return bool(a.r or a.i)
    def __eq__(a,b):
        if not isinstance(b,G):b=G(b)
        return a.r==b.r and a.i==b.i
    def conj(a):return G(a.r,-a.i)
    def norm(a):return a.r*a.r+a.i*a.i
    def __repr__(a):return str(a.r) if not a.i else f'({a.r})+({a.i})i'
def require(t,msg):
    if not t:raise AssertionError(msg)
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def det(A):
    n=len(A)
    return sum((sign(p)*reduce(lambda a,i:a*A[i][p[i]],range(n),1) for p in permutations(range(n))),0)
def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),G()) for col in zip(*B)] for row in A]
def unitary(U):return mm(U,[[a.conj() for a in col]for col in zip(*U)])==[[G(int(i==j))for j in range(len(U))]for i in range(len(U))]
def clean(p):return {k:v for k,v in p.items() if v}
def add(a,b,scale=1):
    out=a.copy()
    for n,v in b.items():out[n]=out.get(n,G())+scale*v
    return clean(out)
def mul(a,b):
    out={}
    for n,v in a.items():
        for k,w in b.items():
            t=tuple(x+y for x,y in zip(n,k));out[t]=out.get(t,G())+v*w
    return clean(out)
def inner(a,b):return sum((v*b.get(n,G()).conj() for n,v in a.items()),G())
def hook_polys(U,m):
    N=len(U);e=[{(0,)*N:G(1)}]
    for j in range(1,N+1):
        q={}
        for S in combinations(range(N),j):
            n=tuple(int(i in S) for i in range(N));q[n]=det([[U[a][b]for b in S]for a in S])
        e.append(clean(q))
    h=[{(0,)*N:G(1)}]
    for d in range(1,m+1):
        t={}
        for j in range(1,min(d,N)+1):t=add(t,mul(e[j],h[d-j]),(-1)**(j+1))
        h.append(t)
    hooks=[]
    for k in range(min(m,N)):
        v={}
        for j in range(k+1):v=add(v,mul(h[m-k+j],e[k-j]),(-1)**j)
        hooks.append(v)
    signed={}
    for k,hk in enumerate(hooks):signed=add(signed,hk,(-1)**k)
    weighted={}
    for j in range(1,min(N,m)+1):weighted=add(weighted,mul(e[j],h[m-j]),(-1)**(j+1)*j)
    require(weighted==signed,'weighted Koszul / hooks')
    raw=sum(((-1)**(k+l)*inner(hk,hl) for k,hk in enumerate(hooks) for l,hl in enumerate(hooks)),G())
    require(raw==inner(signed,signed),'signed covariance')
    return signed,raw,e,h
@lru_cache(None)
def comps(m,n):
    if n==1:return ((m,),)
    return tuple((k,)+tail for k in range(m+1) for tail in comps(m-k,n-1))
def edge_count(w,N):
    E=[0]*(N*N)
    for a,b in zip(w,w[1:]+w[:1]):E[a*N+b]+=1
    return tuple(E)
def occupation(E,N):return tuple(sum(E[i*N:(i+1)*N])for i in range(N))
def transpose(E,N):return tuple(E[j*N+i]for i in range(N)for j in range(N))
def period(w):
    for d in range(1,len(w)+1):
        if len(w)%d==0 and all(w[i]==w[i%d]for i in range(len(w))):return d
    raise RuntimeError()
def achiral(w):
    rev=w[::-1]
    return any(rev==w[a:]+w[:a]for a in range(len(w)))
@lru_cache(None)
def flow_count(E,N):
    n=occupation(E,N);m=sum(n);S=[i for i in range(N)if n[i]]
    if tuple(sum(E[i*N+j]for i in range(N))for j in range(N))!=n:return 0
    if len(S)==1:tau=1
    else:
        S=S[:-1];tau=det([[n[i]*int(i==j)-E[i*N+j]for j in S]for i in S])
    z=F(m*tau*reduce(lambda a,k:a*factorial(k-1),[x for x in n if x],1),reduce(lambda a,k:a*factorial(k),E,1))
    require(z.denominator==1,'integral Euler count')
    return z.numerator
@lru_cache(None)
def mobius(n):
    out=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;out=-out
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:out=-out
    return out
@lru_cache(None)
def divisors(n):return tuple(d for d in range(1,n+1)if n%d==0)
@lru_cache(None)
def primitive(E,N):return sum(mobius(r)*flow_count(tuple(x//r for x in E),N)for r in divisors(reduce(gcd,E)))
@lru_cache(None)
def cyclic_count(E,N):
    m=sum(E)
    return sum((m//r)*primitive(tuple(x//r for x in E),N)for r in divisors(reduce(gcd,E)))
def monomial(U,E):return reduce(lambda a,ij:a*U[ij//len(U)][ij%len(U)]**E[ij],range(len(E)),G(1))
def direct_data(U,m):
    N=len(U);poly={};counts={};cyclic={};ach={};reflections={}
    for w in product(range(N),repeat=m):
        E=edge_count(w,N);n=occupation(E,N);v=G(1)
        for a,b in zip(w,w[1:]+w[:1]):v=v*U[a][b]
        poly[n]=poly.get(n,G())+v;counts[E]=counts.get(E,0)+1
        d=period(w);cyclic[E]=cyclic.get(E,0)+d
        if achiral(w):ach[E]=ach.get(E,0)+d
        rev=w[::-1];fix=sum(rev==w[a:]+w[:a]for a in range(m));reflections[E]=reflections.get(E,0)+fix
    return clean(poly),counts,cyclic,ach,reflections

def check(U,m,name):
    N=len(U);require(unitary(U),name+' unitary')
    hp,B,e,h=hook_polys(U,m)
    dp,dc,dcy,da,df=direct_data(U,m); require(hp==dp,name+' hook vs direct occupation polynomial')
    fp={};counts={};tree_bounds=0
    # Independent domain: every nonnegative N-by-N integer array of total m.
    for E in comps(m,N*N):
        c=flow_count(E,N)
        require(c==dc.get(E,0),name+' tree count vs rooted word')
        if not c:continue
        counts[E]=c;n=occupation(E,N);r=sum(x>0 for x in n)
        multi=F(reduce(lambda a,x:a*factorial(x),n,1),reduce(lambda a,x:a*factorial(x),E,1))
        require(0<F(c,multi)<=r,'tree-factor bound');tree_bounds+=1
        S=[i for i in range(N)if n[i]]
        tree_det=det([[F(int(i==j))-F(E[i*N+j],n[i])+F(n[j],m)for j in S]for i in S])
        require(F(c,multi)==tree_det,'stochastic matrix determinant factor')
        k=cyclic_count(E,N);require(k==dcy[E],'periodic cyclic correction')
        # Build lower-degree reflection counts directly, separately from inversion.
        lower={}
        for a in divisors(reduce(gcd,E)):
            if a==1:lower[a]=df
            else:
                lower[a]={}
                for w in product(range(N),repeat=m//a):
                    G0=edge_count(w,N);rev=w[::-1]
                    lower[a][G0]=lower[a].get(G0,0)+sum(rev==w[b:]+w[:b]for b in range(m//a))
        ainv=0
        for a in divisors(reduce(gcd,E)):
            E0=tuple(x//a for x in E)
            ap=sum(mobius(b)*b*lower[a*b].get(tuple(x//b for x in E0),0)for b in divisors(reduce(gcd,E0)))
            ainv+=(m//a)*ap
        require(ainv==da.get(E,0),'reflection inversion overlap')
        fp[n]=fp.get(n,G())+c*monomial(U,E)
    require(clean(fp)==hp,'tree vs hook occupation polynomial')
    cyc=sum((dcy[E]*monomial(U,E).norm()for E in dc),F())
    rev=sum((dcy[E]*monomial(U,E)*monomial(U,transpose(E,N)).conj()for E in dc),G())
    ach=sum((da.get(E,0)*monomial(U,E).norm()for E in dc),F())
    residual=G();zero_current=F()
    byn={}
    for E,c in counts.items():byn.setdefault(occupation(E,N),[]).append(E)
    for n,Es in byn.items():
        for E in Es:
            for H in Es:
                t=counts[E]*counts[H]-int(E==H)*dcy[E]-int(H==transpose(E,N))*dcy[E]+int(E==H)*da.get(E,0)
                require(t>=0,'nonnegative unmatched-pair count')
                residual+=t*monomial(U,E)*monomial(U,H).conj()
                if E==H:zero_current+=t*monomial(U,E).norm()
    require(G(cyc)+rev-G(ach)+residual==B,'cyclic reverse residual partition')
    return {'family':name,'N':N,'m':m,'B':str(B),'cyclic':str(cyc),'reverse':str(rev),'achiral':str(ach),'residual':str(residual),'zero_current':str(zero_current),'edge_types':len(counts),'nonzero_occupations':len(clean(fp)),'tree_bound_checks':tree_bounds,'top_fermion':str(N*N*inner(mul(e[N],h[m-N]),mul(e[N],h[m-N]))) if m>=N else 'absent'}

def givens(N,i,j,a,b):
    R=[[G(int(k==l))for l in range(N)]for k in range(N)]
    R[i][i]=R[j][j]=G(a);R[i][j]=G(b);R[j][i]=G(-b);return R

def fixtures():
    U2=[[G(F(3,5)),G(F(4,5))],[G(F(-4,5)),G(F(3,5))]]
    D=[[G(1),G(),G()],[G(),G(0,1),G()],[G(),G(),G(1)]]
    U3=mm(mm(mm(givens(3,0,1,F(3,5),F(4,5)),D),givens(3,1,2,F(5,13),F(12,13))),givens(3,0,2,F(8,17),F(15,17)))
    def H(a):return [[x/G(2) for x in row]for row in [[G(1),G(1),G(1),G(1)],[G(1),a,G(-1),-a],[G(1),G(-1),G(1),G(-1)],[G(1),-a,G(-1),a]]]
    return [('N1',[[G(0,1)]],6),('identity3',[[G(int(i==j))for j in range(3)]for i in range(3)],5),('rotation2',U2,8),('complex3',U3,6),('hadamard4_real',H(G(1)),5),('hadamard4_i',H(G(0,1)),5)]

def main():
    start=time.monotonic();out=[]
    for name,U,limit in fixtures():
        for m in range(1,limit+1):
            row=check(U,m,name);out.append(row);print(json.dumps(row),flush=True)
    real=next(r for r in out if r['family']=='hadamard4_real' and r['m']==4)
    imag=next(r for r in out if r['family']=='hadamard4_i' and r['m']==4)
    require(real['B']!=imag['B'],'same P phase discriminator must discriminate')
    require(any(r['zero_current']!='0' for r in out),'must retain distinct Euler tours with identical edge counts')
    # A cycle-level cancellation check independent of all polynomial code above.
    cycle_checks=0
    for m in range(1,7):
        for p in permutations(range(m)):
            seen=set();lengths=[]
            for i in range(m):
                if i in seen:continue
                j=i;ell=0
                while j not in seen:seen.add(j);ell+=1;j=p[j]
                lengths.append(ell)
            marked=sum((-1)**(sum(mask)+1)*sum(l*b for l,b in zip(lengths,mask))for mask in product((0,1),repeat=len(lengths)))
            require(marked==(m if len(lengths)==1 else 0),'cycle-marking cancellation')
            cycle_checks+=1
    summary={'cycle_marking_checks':cycle_checks,'status':'exact finite checks passed','arithmetic':'Q(i), fractions.Fraction; no floating arithmetic in assertions','cases':len(out),'rows':out,'elapsed_seconds':time.monotonic()-start,'python':platform.python_version(),'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'source_manifest_sha256':'d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba','negative_controls':['Same P=Q=J_4 but B_4 differs at a=1 and a=i','Nonzero same-edge residual at N=2,m=6 must not be discarded','N=3,m=5 top sector is 54 while complete covariance is 3','All-repeated N=1 powers rule out distinct-occupation truncation'],'nonclaims':['No asymptotic universality or improved uniform bound','No actual BGS operator evaluation']}
    pathlib.Path(__file__).with_name('check_results.json').write_text(json.dumps(summary,indent=2)+'\n')
if __name__=='__main__':main()
