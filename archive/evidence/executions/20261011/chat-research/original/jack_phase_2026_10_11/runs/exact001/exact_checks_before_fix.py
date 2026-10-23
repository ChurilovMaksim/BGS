"""Exact finite controls; independent alpha=1 comparison to C++ SSYT counts."""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
import json
from pathlib import Path
import sys

ALPHAS=(F(1,2),F(1),F(2),F(3),F(7,3))

def signatures(n,lo,hi):
    return sorted((tuple(reversed(x)) for x in combinations_with_replacement(
        range(lo,hi+1),n) if sum(x)==0),reverse=True)

def dominated(mu,lam):
    return sum(mu)==sum(lam) and all(
        sum(mu[:j])<=sum(lam[:j]) for j in range(1,len(mu)))

@lru_cache(None)
def orbit(mu):
    return tuple(sorted(set(permutations(mu)),reverse=True))

def energy(mu,alpha):
    n=len(mu)
    return F(sum(x*x for x in mu))+sum((n+1-2*(i+1))*x
        for i,x in enumerate(mu))/alpha

def clean(poly):
    return {e:c for e,c in poly.items() if c}

def interaction(poly,i,j,alpha):
    out=defaultdict(F)
    for e,c in poly.items():
        a,b=e[i],e[j]
        if a<=b:
            continue
        swapped=list(e); swapped[i],swapped[j]=b,a; swapped=tuple(swapped)
        assert poly.get(swapped,F())==c, "Input not pair-symmetric"
        gap=a-b
        out[e]+=c*gap/alpha
        out[swapped]+=c*gap/alpha
        for r in range(1,gap):
            nu=list(e); nu[i],nu[j]=a-r,b+r
            out[tuple(nu)]+=2*c*gap/alpha
    return clean(out)

def action_monomial(mu,alpha):
    poly={e:F(1) for e in orbit(mu)}
    out=defaultdict(F,{e:F(sum(x*x for x in e)) for e in poly})
    n=len(mu)
    for i in range(n):
        for j in range(i+1,n):
            for e,c in interaction(poly,i,j,alpha).items(): out[e]+=c
    by_signature={}
    for e,c in clean(out).items():
        nu=tuple(sorted(e,reverse=True))
        assert dominated(nu,mu)
        if nu in by_signature: assert by_signature[nu]==c
        by_signature[nu]=c
    assert by_signature[mu]==energy(mu,alpha)
    assert all(c>=0 for c in by_signature.values())
    return by_signature

def build_jack(lam,alpha):
    n=len(lam)
    basis=[mu for mu in signatures(n,lam[-1],lam[0]) if dominated(mu,lam)]
    assert basis[0]==lam
    actions={mu:action_monomial(mu,alpha) for mu in basis}
    coefficient={lam:F(1)}
    e=energy(lam,alpha)
    for idx,mu in enumerate(basis[1:],1):
        numerator=sum(coefficient[nu]*actions[nu].get(mu,F())
            for nu in basis[:idx])
        assert e>energy(mu,alpha)
        coefficient[mu]=numerator/(e-energy(mu,alpha))
    assert all(c>=0 for c in coefficient.values())
    lhs=defaultdict(F)
    for mu,c in coefficient.items():
        for nu,d in actions[mu].items(): lhs[nu]+=c*d
    assert clean(lhs)==clean({mu:e*c for mu,c in coefficient.items()})
    expanded={}
    for mu,c in coefficient.items():
        for exp in orbit(mu): expanded[exp]=c
    return coefficient,expanded

def multiply_variable(poly,i):
    out=defaultdict(F)
    for e,c in poly.items():
        nu=list(e);nu[i]+=1;out[tuple(nu)]+=c
    return out

def add_scaled(target,poly,scale):
    for e,c in poly.items():target[e]+=scale*c

def check_cleared_operator_identity(poly,alpha):
    # Independently compare the rational interaction after clearing x_i-x_j:
    # alpha*(x_i-x_j)*interaction(P) = (x_i+x_j)*(D_i-D_j)*P.
    n=len(next(iter(poly)))
    for i in range(n):
        for j in range(i+1,n):
            term=interaction(poly,i,j,alpha)
            left=defaultdict(F)
            add_scaled(left,multiply_variable(term,i),alpha)
            add_scaled(left,multiply_variable(term,j),-alpha)
            derivative={e:c*(e[i]-e[j]) for e,c in poly.items()}
            right=defaultdict(F)
            add_scaled(right,multiply_variable(derivative,i),F(1))
            add_scaled(right,multiply_variable(derivative,j),F(1))
            assert clean(left)==clean(right)

def weyl_dimension(weight):
    d=F(1)
    for i in range(len(weight)):
        for j in range(i+1,len(weight)):
            d*=F(weight[i]-weight[j]+j-i,j-i)
    assert d.denominator==1
    return d.numerator

def main(cpp_path,result_path):
    cpp=json.loads(Path(cpp_path).read_text())
    assert cpp["all_passed"]
    cpp_cases={(c["N"],tuple(c["lambda"])):c for c in cpp["cases"]}
    records=[]
    identity_pairs=0
    matched=0
    for n in range(2,6):
        # Include a genuinely broader coefficient range than the C++ control.
        bound=3 if n<=4 else 2
        for lam in signatures(n,-bound,bound):
            if lam==(0,)*n: continue
            for alpha in ALPHAS:
                coeff,poly=build_jack(lam,alpha)
                c0=poly.get((0,)*n,F())
                s=sum(poly.values())
                k=min(lam[0],-lam[-1]);e=energy(lam,alpha)
                root_sum=F()
                for j in range(1,k+1):
                    exp=(j,-j)+(0,)*(n-2)
                    root_sum+=j*poly.get(exp,F())
                assert e*c0==2*n*(n-1)*root_sum/alpha
                assert s>=c0*(1+alpha*e/(2*k))
                assert e>=2*k*k+2*(n-1)*k/alpha
                assert c0/s<=1/(n+alpha*k)<=1/(n+alpha)
                root=(1,)+(0,)*(n-2)+(-1,)
                assert (c0/s==1/(n+alpha))==(lam==root)
                check_cleared_operator_identity(poly,alpha)
                identity_pairs+=n*(n-1)//2
                key=(n,lam)
                if alpha==1 and key in cpp_cases:
                    c=cpp_cases[key]
                    assert c0==c["zero_weight"] and s==c["dimension"]
                    matched+=1
                records.append({"N":n,"alpha":str(alpha),"lambda":lam,
                    "constant":str(c0),"evaluation":str(s),"ratio":str(c0/s),
                    "sharp_mode":lam==root})
    assert matched==len(cpp_cases)
    dimension_records=[]
    for n in range(2,31):
        root=(1,)+(0,)*(n-2)+(-1,)
        coe=weyl_dimension(tuple(2*x for x in root))
        cse=weyl_dimension(tuple(x for x in root for _ in range(2)))
        assert coe==F(n*n*(n-1)*(n+3),4)
        assert cse==n*n*(2*n-3)*(2*n+1)
        for beta,alpha,dim in ((1,F(2),coe),(2,F(1),n*n-1),(4,F(1,2),cse)):
            f_at_i=n*n-alpha*n/(n-1+alpha)
            var=f_at_i*f_at_i/dim
            if beta==1:
                expected=F(4*(n-1)*(n+2)**2,(n+1)**2*(n+3))
            elif beta==2: expected=F(1)
            else: expected=F((n-1)**2*(2*n+1),(2*n-1)**2*(2*n-3))
            assert var==expected
            dimension_records.append({"N":n,"beta":beta,"dimension":dim,
                "variance":str(var),"averaged_variance":str(var/(n+alpha))})
    # Independent N=2 beta density: u^2 has Beta(1/2,(beta+1)/2).
    for beta in (1,2,4):
        mean=F(4,beta+2)
        fourth=F(48,(beta+2)*(beta+4))
        var=fourth-mean*mean
        assert var==F(32*(beta+1),(beta+2)**2*(beta+4))
        rec=next(r for r in dimension_records if r["N"]==2 and r["beta"]==beta)
        assert str(var)==rec["variance"]
    result={"all_passed":True,"arithmetic":"Python Fraction and C++ exact integer SSYT",
        "jack_cases":len(records),"cleared_pair_identities":identity_pairs,
        "independent_cpp_cases":matched,"dimension_variance_cases":len(dimension_records),
        "tested_N":[2,3,4,5],"signature_bounds":{"N<=4":[-3,3],"N=5":[-2,2]},
        "alphas":[str(a) for a in ALPHAS],"records":records,
        "dimension_controls":dimension_records,
        "non_claims":["Finite checks do not prove the theorem for arbitrary N or signature.",
                      "No simulation of a deterministic BGS system.",
                      "No Lean compilation or formal certificate."]}
    Path(result_path).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ("all_passed","jack_cases",
        "cleared_pair_identities","independent_cpp_cases","dimension_variance_cases")}))
if __name__=="__main__":
    main(*sys.argv[1:])

