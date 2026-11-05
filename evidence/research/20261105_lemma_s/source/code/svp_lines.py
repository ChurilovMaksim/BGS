"""research1105b [CA for lattice facts / N for SVP]: kernel lattices of the cyclotomic walk.
For an ideal a of O=Z[sqrt2] with N(a)=h | h_p (one prime ideal above each q | h), A(a) = {c in Z^p : sum c_i lam^i in a}.
By Theorem 6 of grok47/h5_xline.md, the line sum over the conjugate ideal is 1+X_line = h * W(A)/Z0, W(A) = sum of word weights
with cyclic image in A.  Binet ideals (eps^p == s at every q) contain eta_s = lam - 1 - 2 s lam^{(p+1)/2} (l1 = 4).
We compute, per ideal: membership of eta_+-, shortest vector (l2, after removing the all-ones null direction) by fpylll SVP/BKZ,
and the l1 norm of the shortest vectors found."""
import sys, json, math, itertools
from fpylll import IntegerMatrix, LLL, BKZ, GSO, Enumeration
from fpylll.fplll.bkz_param import BKZParam
from fpylll.fplll.bkz_param import BKZParam
from sympy import factorint, sqrt_mod
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
def lattice(p,h,r):
    # basis of {c in Z^p: sum c_i r^i == 0 mod h} intersected with sum c_i = 0 ? No: quotient by all-ones handled by adding p-th col weight.
    B=[[0]*p for _ in range(p)]
    B[0][0]=h
    for i in range(1,p):
        B[i][0]=(-pow(r,i,h))%h; B[i][i]=1
    return B
def reduce_null(v,p):
    # min over t of l2 of v - t*1 (real t rounded)
    best=None
    s=sum(v); t0=round(s/p)
    for t in (t0-1,t0,t0+1):
        w=[x-t for x in v]; n2=sum(x*x for x in w)
        if best is None or n2<best[0]: best=(n2,w)
    return best[1]
def analyse(p,maxdim_svp=46):
    h=hp(p); fac=sorted(factorint(h)); out=[]
    loc={}
    for q in fac:
        w=int(sqrt_mod(2,q)); opts=[]
        for sgn in (1,-1):
            ww=(sgn*w)%q; lamq=(3+2*ww)%q; epsq=(1+ww)%q; s=pow(epsq,p,q); s=1 if s==1 else (-1 if s==q-1 else None)
            opts.append((lamq,s))
        loc[q]=opts
    for choice in itertools.product(*[loc[q] for q in fac]):
        r=0; M=1
        for q,(lq,s) in zip(fac,choice):
            r=r+M*(((lq-r)*pow(M,-1,q))%q); M*=q
        signs=[s for (lq,s) in choice]
        kind='binet+' if all(s==1 for s in signs) else ('binet-' if all(s==-1 for s in signs) else 'cross')
        # eta membership
        k=(p+1)//2; eta={sg:(r-1-2*sg*pow(r,k,h))%h==0 for sg in (1,-1)}
        # lattice modulo the all-ones vector: add a big multiple column to penalise sum? use projection: append column W*(sum c_i)
        # we want min over t of ||c - t*1||: equivalently shortest vector of the projected lattice (orthogonal to 1).
        Bm=lattice(p,h,r)
        # project: c -> p*c - (sum c)*1  (integral, scaled by p)
        P=[[p*x-sum(row) for x in row] for row in Bm]+[[0]*p]
        A=IntegerMatrix.from_matrix([row for row in P[:-1]])
        LLL.reduction(A)
        rows=[list(A[i]) for i in range(A.nrows) if any(A[i])]
        A=IntegerMatrix.from_matrix(rows)
        BKZ.reduction(A,BKZParam(block_size=min(20,len(rows)),strategies=None,max_loops=4)); how='bkz20+enum' if p<=maxdim_svp else 'bkz20'
        rows=[list(A[i]) for i in range(A.nrows)]
        if p<=maxdim_svp:
            Mg=GSO.Mat(A); Mg.update_gso(); r2=min(sum(x*x for x in v) for v in rows)
            try:
                sol=Enumeration(Mg).enumerate(0,A.nrows,r2*1.0001,0)
                coeffs=[int(round(c)) for c in sol[0][1]]
                vv=[sum(coeffs[i]*rows[i][j] for i in range(len(rows))) for j in range(p)]
                rows.append(vv); how='bkz20+exact_enum'
            except Exception as e: how='bkz20(enum fail)'
        v=min(rows,key=lambda v:sum(x*x for x in v))
        l2=math.sqrt(sum(x*x for x in v))/p
        # recover an integer representative: lattice vector c with p*c - s*1 = v  => try candidate from LLL of original basis
        A2=IntegerMatrix.from_matrix(Bm); LLL.reduction(A2)
        if p<=maxdim_svp: pass
        cands=[reduce_null(list(A2[i]),p) for i in range(A2.nrows)]
        cands=[c for c in cands if any(c)]
        cmin=min(cands,key=lambda c:sum(abs(x) for x in c))
        out.append(dict(p=p,h=h,signs=signs,kind=kind,eta_plus=eta[1],eta_minus=eta[-1],shortest_l2_proj=l2,method=how,
                        lll_min_l1=sum(abs(x) for x in cmin),lll_min_vec=cmin if p<=31 else None,
                        gauss_heur_l2=math.sqrt((p-1)/(2*math.pi*math.e))*(h*math.sqrt(p))**(1/(p-1))/math.sqrt(1)))
        print(json.dumps({k:v for k,v in out[-1].items() if k!='lll_min_vec'}),flush=True)
    return out
if __name__=='__main__':
    allr=[]
    for p in map(int,sys.argv[1:]): allr+=analyse(p)
    json.dump(allr,open('/workspace/research1105b/logs/svp_lines.json','w'),indent=1)
