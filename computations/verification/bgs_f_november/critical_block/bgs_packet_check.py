"""Exact arithmetic for linking two consecutive selected doublets."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from spectrum.bgs_packet_check import COEFFICIENTS, SQUARES, p_log, rho_at, split
from split_law.bgs_packet_check import SELECTED, primitive_stationary_support

P = 7
STEP = 7


def alpha_at(k):
    modulus = P**k
    rho = rho_at(k+1)
    log_gamma = p_log(3+2*rho,k+1)
    assert log_gamma % P == 0 and (log_gamma//P)%P
    return -pow(3*(log_gamma//P),-1,modulus)%modulus


def delta_at(k):
    return STEP*alpha_at(k)%P**k


def cross_phase(label,ell,k,distance=1):
    modulus=P**k
    rho=rho_at(k)
    delta=distance*delta_at(k)
    a,b=split(label,rho,modulus)
    divisor=P if abs(label[1])==P else 1
    a0,b0=split(tuple(x//divisor for x in label),rho,modulus)
    reduced_delta=delta//divisor

    def polynomial(x):
        return b0*x*(x+a)+reduced_delta*x-ell*a0

    root,=[x for x in sorted(SQUARES) if (x+a)%P in SQUARES and polynomial(x)%P==0]
    level=P
    for _ in range(1,k):
        new_level=P*level
        root,=[root+j*level for j in range(P) if polynomial(root+j*level)%new_level==0]
        level=new_level
    y=(root+a)%modulus
    half=pow(2,-1,modulus)
    phase=(b*(root+a*half)+(ell+delta)*p_log(y,k)-ell*p_log(root,k))%modulus
    hessian=(b0*(2*root+a)+reduced_delta)*pow(2*root*y,-1,P)%P
    assert hessian
    return phase, hessian, root, y


def common_phase(ell,k,distance=1):
    modulus=P**k
    delta=distance*delta_at(k)
    return ((ell+delta)*p_log(ell+delta,k)-ell*p_log(ell,k)
            +delta*(p_log(2*rho_at(k),k)-1))%modulus


def branch_certificate():
    k=3
    modulus=P**k
    delta=delta_at(k)
    rho=rho_at(k)
    q=[rho*v[1]**2*pow(2,-1,modulus)%modulus for v in SELECTED]
    d0=[-a*pow(4,-1,modulus)%modulus for a in q]
    d1=[(b-delta)%modulus for b in d0]
    cross=[-(a+delta)**2*pow(4*a,-1,modulus)%modulus for a in q[:3]]
    assert len(set(d0+d1+cross))==11
    assert delta==168 and d0==[158,165,200,196] and d1==[333,340,32,28]
    assert cross==[172,179,214]
    return {"modulus":modulus,"delta":delta,"diagonal_0":d0,
            "diagonal_1":d1,"cross":cross}


def compute():
    primitive_stationary_support()
    assert alpha_at(2)%P==3
    assert delta_at(2)//P==3
    for x in range(1,P):
        for d in (1,-1):
            a,b=split((0,d),3,P)
            assert (b*x*x+3*x-3*a)%P!=0
    rcount=[]
    for distance in range(7):
        aa,bb=split((0,1),3,P)
        roots=[x for x in range(1,P)
               if (bb*x*x+(3*distance)*x-3*aa)%P==0]
        assert len(roots)==(2 if distance in (0,3,4) else 0)
        if roots:
            assert len(set(roots)&SQUARES)==1
        rcount.append(len(roots))
    second=Fraction(sum(re*re+im*im for re,im in COEFFICIENTS.values()),4000**2)
    assert second==Fraction(66033,160000)
    examples={}
    for k in (2,3,4,5):
        rows={}
        modulus=P**k
        for ell in (3,10,17,24):
            target=common_phase(ell,k)
            row=[]
            for v in SELECTED[:3]:
                neg=(-v[0],-v[1])
                a,c,x,y=cross_phase(v,ell,k)
                b,d,xn,yn=cross_phase(neg,ell,k)
                assert (a+b)%modulus==target
                assert (c+d)%P==0
                assert (x*xn)%P==(y*yn)%P==4
                assert cross_phase(v,ell+P**(k-1),k)[0]==a
                row.append([v,a,b,c,d])
            rows[ell]={"common":target,"stationary":row}
        examples[k]=rows
    deeper_checks=[]
    for distance in (0,3,4,7,10,11):
        for k in (3,4,5):
            for ell in (3,10,17,24):
                a,c,x,y=cross_phase((0,7),ell,k,distance)
                b,d,xn,yn=cross_phase((0,-7),ell,k,distance)
                assert (a+b)%P**k==common_phase(ell,k,distance)
                assert (-c*d)%P in SQUARES
                assert (x*xn)%P==(y*yn)%P==4
                deeper_checks.append([distance,k,ell,a,b])
    return {"branch_points":branch_certificate(),"kick_second_moment":str(second),
            "roots_at_depth_one_by_distance":rcount,
            "deeper_checks":deeper_checks,"sample":examples}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    content=json.dumps(compute(),indent=2)+"\n"
    data=ROOT/"critical_block/data/branches.json"
    if args.verify:
        assert content==data.read_text()
        print("Exact distinct branch points, common phases, and vanishing of the depth-one cross terms verified.")
    else:
        data.write_text(content)
        print("Wrote",data)
