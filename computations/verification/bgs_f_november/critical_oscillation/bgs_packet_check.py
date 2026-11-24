"""Exact certificates for the oscillating adjacent-doublet coupling."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from collections import defaultdict
from fractions import Fraction as F
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from critical_block.bgs_packet_check import alpha_at
from spectrum.bgs_packet_check import COEFFICIENTS, SQUARES, p_log, rho_at, split

P=7
STABLE_A=(1,0)
STABLE_B=(1,-7)
OTHER_B=(1,7)
ANCHOR=5


def depth(v):
    return int(v in ((0,7),(0,-7)))


def norm(v):
    return v[0]**2-2*v[1]**2


def ratio(k):
    n=P**k
    rho=rho_at(k)
    return ((1+7*rho)*pow(1-7*rho,-1,n))%n


def eta_exponent(k):
    return alpha_at(k)*p_log(ratio(k),k)%P**k


def support():
    groups=defaultdict(list)
    for v in COEFFICIENTS:
        a,b=split(v,3,P)
        for x in range(1,P):
            y=(x+a)%P
            if y and (b*x*y+3*x-5*a)%P==0:
                assert a and b and (b*(x+y)+3)%P
                pos=(x in SQUARES,y in SQUARES)
                groups[pos].append((v,x,y))
    assert groups[True,True]==[((1,0),1,2),((1,7),1,2),((1,-7),1,2)]
    assert groups[True,False]==[((1,0),2,3),((1,7),2,3),((1,-7),2,3)]
    assert set(groups[False,False])=={((-v[0],-v[1]),-x%P,-y%P)
                                     for v,x,y in groups[True,True]}
    assert set(groups[False,True])=={((-v[0],-v[1]),-x%P,-y%P)
                                    for v,x,y in groups[True,False]}
    return {str(key):value for key,value in groups.items()}


def critical_phase(v,ell,k,xmod):
    n=P**k
    a,b=split(v,rho_at(k),n)
    delta=alpha_at(k)
    f=lambda x: (b*x*(x+a)+delta*x-ell*a)
    x=xmod
    step=P
    for _ in range(1,k):
        x,=[x+step*s for s in range(P) if f(x+step*s)%(P*step)==0]
        step*=P
    assert f(x)%n==0
    y=(x+a)%n
    half=pow(2,-1,n)
    phase=(b*(x+a*half)+(ell+delta)*p_log(y,k)-ell*p_log(x,k))%n
    c=(b*(x+y)+delta)*pow(2*x*y,-1,P)%P
    assert c and c not in SQUARES
    return phase,c,x,y


def diagonal_groups(ell):
    groups=defaultdict(lambda:[0,0,0])
    degenerate=set()
    for v,c in COEFFICIENTS.items():
        d=depth(v)
        a,b=split(v,3,P)
        a0,b0=split(tuple(z//P**d for z in v),3,P)
        for x in range(1,P):
            y=(x+a)%P
            if not y or (b0*x*y-ell*a0)%P:
                continue
            if (2*x+a)%P==0:
                degenerate.add(norm(v))
                continue
            name=(x in SQUARES,y in SQUARES,norm(v),x*pow(a0,-1,P)%P)
            u=groups[name]
            u[0]+=c[0]
            u[1]+=c[1]
            u[2]=d
    coeff_sum=sum(P**d*(a*a+b*b) for a,b,d in groups.values())
    return groups,degenerate,F(49*coeff_sum,9*4000**2)


def exact_branches():
    k=4
    n=P**k
    rho=rho_at(k)
    delta=alpha_at(k)
    diag_0,deg_0,v0=diagonal_groups(5)
    diag_1,deg_1,v1=diagonal_groups(1)
    assert deg_0=={-97,1} and not deg_1
    norm_scale=pow(-2*rho,-1,n)
    for Q in deg_0:
        assert (-Q*norm_scale*pow(4,-1,n))%49==19
    families=[]
    for r,groups in enumerate((diag_0,diag_1)):
        for Q in sorted({g[2] for g in groups}):
            q=Q*norm_scale%n
            families.append((r,Q,(-q*pow(4,-1,n)-r*delta)%n))
    for v in (STABLE_A,STABLE_B):
        q=norm(v)*norm_scale%n
        families.append(("cross",norm(v),(-(q+delta)**2*pow(4*q,-1,n))%n))
    assert len(set(row[2] for row in families))==len(families)
    return {"modulus":n,"families":families,
            "diag_energy_from_rational_coefficients":[str(v0),str(v1)]}


def orbit_pairs():
    groups=defaultdict(list)
    for v,coeff in COEFFICIENTS.items():
        if not depth(v):
            a,_=split(v,3,P)
            assert a
            groups[norm(v),a in SQUARES].append((v,coeff))
    acc=defaultdict(int)
    for (q,_),group in groups.items():
        assert len(group) in (1,2)
        if len(group)==2:
            (v,c),(w,d)=group
            acc[q]+=2*(c[0]*d[0]+c[1]*d[1])
    assert dict(acc)=={-1:-112,-71:-28,-127:-28,-97:400}
    prim=F(sum(a*a+b*b for v,(a,b) in COEFFICIENTS.items()
               if not depth(v)),4000**2)
    assert prim==F(1233,160000)
    return {"cross_coefficients":dict(sorted(acc.items())),"primitive_constant":str(prim)}


def compute():
    branches=exact_branches()
    s=support()
    vals={}
    for k in (2,3,4,5,6):
        n=P**k
        al=alpha_at(k)
        rho=rho_at(k)
        vals[k]={"eta_exponent":eta_exponent(k),"cases":{}}
        for ell in (5,12,19,26):
            a=[critical_phase(STABLE_A,ell,k,x) for x in (1,2)]
            b=[critical_phase(STABLE_B,ell,k,x) for x in (1,2)]
            c=[critical_phase(OTHER_B,ell,k,x) for x in (1,2)]
            for r in range(2):
                assert (c[r][0]-b[r][0])%n==eta_exponent(k)
                assert b[r][1]==c[r][1]==a[r][1]
            assert (sum(item[0] for item in b)-sum(item[0] for item in a))%n==(-eta_exponent(k))%n
            common=((ell+al)*p_log(ell+al,k)-ell*p_log(ell,k)
                     +al*(p_log(-2*rho,k)-1))%n
            assert sum(item[0] for item in a)%n==common
            vals[k]["cases"][ell]=[a,b,c]
    assert 8*F(7,1200)**2*F(1,1568)==F(1,5_760_000)
    return {"support":s,"branches":branches,"orbit_formula":orbit_pairs(),"stationary_samples":vals}


if __name__=="__main__":
    parser=ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    path=ROOT/"critical_oscillation/data/certificates.json"
    content=json.dumps(compute(),indent=2)+"\n"
    if args.verify:
        assert path.read_text()==content
        print("Adjacent-node supports, phase identities, exact orbit weights, and oscillation constant verified.")
    else:
        path.write_text(content)
        print("Wrote",path)
