#!/usr/bin/env python3
"""Independent finite-field reconstruction: raw Fourier symbol -> Weyl sum,
chirp/Fourier kernel -> full idempotents -> column-image bases -> Newton traces.
No candidate code imported; no SymPy arithmetic used. Python integers handle
polynomials and scalar arithmetic. NumPy int64 matrix products are range-gated.
"""
import hashlib, json, math, platform, time
from pathlib import Path
from datetime import datetime, timezone
import numpy as np

ROOT = Path(__file__).resolve().parent
LIMIT = 2**63-1

def require(ok, message):
    if not ok: raise RuntimeError(message)

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def matrix_sha(a): return hashlib.sha256(json.dumps(a.tolist(),separators=(',',':')).encode()).hexdigest()

def factors(n):
    out=[]; k=2
    while k*k<=n:
        if n%k==0:
            out.append(k)
            while n%k==0: n//=k
        k+=1
    if n>1: out.append(n)
    return out

def prime(p): return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
def generator(p):
    for g in range(2,p):
        if all(pow(g,(p-1)//l,p)!=1 for l in factors(p-1)): return g
    raise RuntimeError('no generator')

def mul(a,b,p):
    require(a.dtype==b.dtype==np.int64, 'wrong matrix dtype')
    require(a.shape[1]*(p-1)**2 < LIMIT,'unsafe integer product')
    require(np.all((0<=a)&(a<p)) and np.all((0<=b)&(b<p)), 'unnormalized product input')
    return (a@b)%p

def add_poly(a,b,p):
    out=a.copy()
    for k,v in b.items(): out[k]=(out.get(k,0)+v)%p
    return {k:v for k,v in out.items() if v}

def scale_poly(a,c,p): return {k:v*c%p for k,v in a.items() if v*c%p}
def product_poly(a,b,p):
    out={}
    for k,v in a.items():
        for l,w in b.items(): out[k+l]=(out.get(k+l,0)+v*w)%p
    return {k:v for k,v in out.items() if v}

def raw_symbol(n,p,q,ii):
    half=pow(2,-1,p)
    cos1={1:half,-1:half}; cos7={7:half,-7:half}
    sin1={1:pow(2*ii%p,-1,p),-1:-pow(2*ii%p,-1,p)%p}
    r=product_poly(add_poly({0:1},scale_poly(cos7,-1,p),p),add_poly({0:1},cos1,p),p)
    diagonal=add_poly(add_poly(cos7,scale_poly(r,pow(10,-1,p),p),p),scale_poly(product_poly(r,sin1,p),pow(100,-1,p),p),p)
    diagonal=add_poly(diagonal,{0:-pow(10,-1,p)%p},p)
    terms={(0,k):v for k,v in diagonal.items()}
    for a,c in [(1,(-3-4*ii)*pow(1000,-1,p)),(-1,(-3+4*ii)*pow(1000,-1,p))]:
        for b,v in r.items(): terms[a,b]=v*c%p
    A=np.zeros((n,n),dtype=np.int64)
    for (a,b),v in terms.items():
        for x in range(n):
            y=(x+a)%n
            A[x,y]=(int(A[x,y])+v*pow(q,(b*(x+pow(2,-1,n)*a))%n,p))%p
    return A,terms

def cat(n,p,q):
    # D F D with the cross-frequency zeta=q^(1/4), not the author's
    # direct two-dimensional quadratic-form expression.
    u=[pow(q,(-3*pow(8,-1,n)*x*x)%n,p) for x in range(n)]
    zeta=pow(q,pow(4,-1,n),p)
    return np.array([[u[x]*pow(zeta,x*y,p)*u[y]%p for y in range(n)] for x in range(n)],dtype=np.int64)

def weyl(n,p,q,a,b):
    W=np.zeros((n,n),dtype=np.int64)
    for x in range(n): W[x,(x+a)%n]=pow(q,b*(x+pow(2,-1,n)*a)%n,p)
    return W

def pivot_columns(A,p):
    # Forward elimination only; used on P then on B^T. Not nullspace RREF.
    E=A.copy(); nr,nc=E.shape; r=0; piv=[]
    for j in range(nc):
        rows=np.where(E[r:,j]!=0)[0]
        if len(rows)==0: continue
        k=r+int(rows[0]); E[[r,k],:]=E[[k,r],:]
        E[r,:]=E[r,:]*pow(int(E[r,j]),-1,p)%p
        for k in range(r+1,nr):
            if E[k,j]: E[k,:]=(E[k,:]-int(E[k,j])*E[r,:])%p
        piv.append(j);r+=1
        if r==nr: break
    return piv

def inverse(A,p):
    n=len(A); E=np.concatenate([A.copy(),np.eye(n,dtype=np.int64)],axis=1)
    for j in range(n):
        ix=next((k for k in range(j,n) if E[k,j]),None)
        require(ix is not None,'singular inverse')
        E[[j,ix]]=E[[ix,j]]; E[j]=E[j]*pow(int(E[j,j]),-1,p)%p
        for k in range(n):
            if k!=j: E[k]=(E[k]-int(E[k,j])*E[j])%p
    B=E[:,n:]
    require(np.array_equal(mul(A,B,p),np.eye(n,dtype=np.int64)),'inverse identity')
    return B

def charpoly_newton(C,p):
    n=len(C); require(n<p,'Newton denominators')
    traces=[0]; power=np.eye(n,dtype=np.int64)
    for j in range(1,n+1):
        power=mul(power,C,p); traces.append(sum(int(power[k,k]) for k in range(n))%p)
    coeff=[1]
    for k in range(1,n+1):
        coeff.append((-sum(coeff[k-j]*traces[j] for j in range(1,k+1))*pow(k,-1,p))%p)
    # Independent postcondition: the resulting monic polynomial annihilates C.
    ev=np.eye(n,dtype=np.int64)
    for c in coeff[1:]: ev=(mul(ev,C,p)+c*np.eye(n,dtype=np.int64))%p
    require(not np.any(ev),'Cayley Hamilton fails')
    return coeff,traces[1:]

def trim(a):
    while a and a[-1]==0: a.pop()
    return a

def rem(a,b,p):
    a=trim(a.copy()); b=trim(b.copy()); require(bool(b),'zero polynomial divisor')
    while len(a)>=len(b):
        offset=len(a)-len(b); c=a[-1]*pow(b[-1],-1,p)%p
        for j,x in enumerate(b): a[j+offset]=(a[j+offset]-c*x)%p
        trim(a)
    return a

def gcd_poly(a,b,p):
    while b: a,b=b,rem(a,b,p)
    return [x*pow(a[-1],-1,p)%p for x in a] if a else []

def run(n,p,author):
    started=time.perf_counter(); require(prime(p),'nonprime')
    g=generator(p); require((p-1)%(4*n)==0,'not split')
    q=pow(g,(p-1)//n,p); ii=pow(g,(p-1)//4,p)
    require(pow(q,n,p)==1 and all(pow(q,n//l,p)!=1 for l in factors(n)), 'q order')
    require(ii*ii%p==p-1,'i square')
    A,terms=raw_symbol(n,p,q,ii); G=cat(n,p,q); I=np.eye(n,dtype=np.int64)
    Aconj,_=raw_symbol(n,p,pow(q,-1,p),-ii%p)
    Gconj=cat(n,p,pow(q,-1,p))
    require(np.array_equal(Aconj.T,A),'Hermitian involution')
    require(np.array_equal(mul(G,Gconj.T,p),n*I%p),'raw unitarity')
    S=np.array([[3,4],[2,3]],dtype=np.int64); T=np.eye(2,dtype=np.int64); R=0
    while True:
        R+=1;T=mul(T,S,n)
        if np.array_equal(T,np.eye(2,dtype=np.int64)): break
        require(R<=6*n,'order safety cap')
    for a,b in [(1,0),(0,1),(1,1),(-3,2)]:
        require(np.array_equal(mul(G,weyl(n,p,q,a,b),p),mul(weyl(n,p,q,3*a+4*b,2*a+3*b),G,p)), 'raw covariance')
    powers=[I]
    for j in range(R): powers.append(mul(powers[-1],G,p))
    c=int(powers[-1][0,0]);require(c!=0 and np.array_equal(powers[-1],c*I%p),'raw scalar power')
    roots=[x for x in range(1,p) if pow(x,R,p)==c];require(len(roots)==R and R%p!=0,'all simple cat roots')
    projectors=[];blocks=[];total=0; expected={b['lambda']:b for b in author['blocks']}
    for lam in roots:
        P=np.zeros((n,n),dtype=np.int64)
        for j in range(R): P=(P+pow(lam,-j,p)*powers[j])%p
        P=P*pow(R,-1,p)%p
        require(np.array_equal(mul(P,P,p),P),'projector idempotency')
        require(np.array_equal(mul(G,P,p),lam*P%p),'projector eigenrelation')
        projectors.append(P)
        columns=pivot_columns(P,p); d=len(columns);total+=d
        require(sum(int(P[k,k]) for k in range(n))%p==d%p,'projector trace rank')
        if not d:
            require(lam not in expected,'missing author block')
            continue
        B=P[:,columns];rows=pivot_columns(B.T.copy(),p)
        require(len(rows)==d,'image row rank')
        left=inverse(B[rows,:],p)
        C=mul(left,mul(P,mul(A,B,p),p)[rows,:],p)
        require(np.array_equal(mul(B,C,p),mul(P,mul(A,B,p),p)),'compression action')
        coeff,traces=charpoly_newton(C,p); asc=coeff[::-1]
        gcd=gcd_poly(asc,[j*asc[j]%p for j in range(1,len(asc))],p);gd=len(gcd)-1
        require(lam in expected and expected[lam]['multiplicity']==d,'author dimension discrepancy')
        require(expected[lam]['characteristic_coefficients_descending']==coeff,'author characteristic discrepancy')
        require(expected[lam]['derivative_gcd_degree']==gd,'author gcd discrepancy')
        if n!=7: require(gd==0,'nonsimple compression')
        blocks.append({'lambda':lam,'dimension':d,'image_columns':columns,'coordinate_rows':rows,'compression':C.tolist(),'charpoly_descending':coeff,'power_traces':traces,'gcd_ascending':gcd,'gcd_degree':gd,'projector_sha256':matrix_sha(P)})
    require(np.array_equal(sum(projectors)%p,I),'sum of all projectors')
    require(total==n,'dimension completeness')
    # The mixed projector relation follows from eigenrelations and distinct
    # lambdas; additionally test every pair by exact multiplication.
    for i in range(len(projectors)):
        for j in range(i): require(not np.any(mul(projectors[i],projectors[j],p)),'projector disjointness')
    require(len(expected)==len(blocks),'author extra blocks')
    if n==7:
        require(np.array_equal(A,(9*pow(10,-1,p)%p)*I%p),'N7 scalar control')
        require(sorted(b['gcd_degree'] for b in blocks)==[1,1,2],'N7 expected failure')
    rec={'N':n,'p':p,'g':g,'q':q,'i':ii,'R':R,'c':c,'raw_symbol_modes':len(terms),'A_sha256':matrix_sha(A),'G_sha256':matrix_sha(G),'root_count':len(roots),'zero_projector_roots':[x for x in roots if x not in expected],'nonzero_blocks':len(blocks),'dimensions':sorted([b['dimension'] for b in blocks]),'all_simple':all(b['gcd_degree']==0 for b in blocks),'matrix_product_bound':n*(p-1)**2,'blocks':blocks,'runtime_seconds':time.perf_counter()-started}
    print(json.dumps({k:v for k,v in rec.items() if k!='blocks'}),flush=True)
    return rec

def main():
    started=datetime.now(timezone.utc).isoformat(); before=time.perf_counter()
    author=json.loads((ROOT/'frozen/exact_projector_certificate.json').read_text())
    manifest=json.loads((ROOT/'frozen/candidate_manifest.json').read_text())
    for name,h in manifest['files'].items(): require(sha(ROOT/'frozen'/name)==h,'candidate hash mismatch '+name)
    results=[run(n,p,next(x for x in author['results'] if x['N']==n)) for n,p in [(7,337),(35,2521),(175,4201)]]
    output={'scope':'All raw-cat spectral compressions for N=35,175; N=7 failure control. No uniform-family conclusion.','method':'Independent raw Fourier Weyl sum, chirp-Fourier cat, complete projectors, projector-column image bases, Newton characteristic polynomial and Euclidean polynomial gcd','started_at':started,'runtime_seconds':time.perf_counter()-before,'python':platform.python_version(),'numpy':np.__version__,'script_sha256':sha(__file__),'candidate_sha256':manifest['files']['first_order_cat_split.md'],'results':results}
    (ROOT/'independent_results.json').write_text(json.dumps(output,indent=2)+'\n')

if __name__=='__main__': main()
