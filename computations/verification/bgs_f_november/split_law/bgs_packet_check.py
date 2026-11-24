"""Exact stationary-root certificates for the doublet displacement law."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from spectrum.bgs_packet_check import COEFFICIENTS, SQUARES, p_log, rho_at, split

P = 7
SELECTED = ((0,1),(0,8),(0,-6),(0,7))


def primitive_stationary_support():
    output = []
    for label, coefficient in sorted(COEFFICIENTS.items()):
        a,b = split(label,3,7)
        if a%7==0:
            assert label in ((0,7),(0,-7)) and b%7==0
            continue
        for x in sorted(SQUARES):
            y=(x+a)%7
            if y and (b*x*y-3*a)%7==0:
                assert y in SQUARES and (2*x+a)%7
                output.append((label,coefficient,x,y,y*pow(x,-1,7)%7))
    expected = set(SELECTED[:3])
    expected.update((-a,-b) for a,b in SELECTED[:3])
    assert {item[0] for item in output}==expected and len(output)==6
    assert all(item[4]==4 for item in output if item[0] in SELECTED[:3])
    a,b=split((0,1),3,7)
    assert [x for x in sorted(SQUARES) if b*x*x%7==3*a%7]==[2]
    assert [COEFFICIENTS[v] for v in SELECTED]==[
        (200,-20),(-100,10),(-100,10),(1800,0)]
    squares=[v[1]**2 for v in SELECTED]
    assert len(set(squares))==4
    return {"primitive_roots":output,"deep_root":2,"norm_factors":squares}


def data_at(label,ell,k):
    """Critical phase and Hessian after removal of the factor 7^depth."""
    modulus = P**k
    rho = rho_at(k)
    depth = int(label==(0,7))
    divisor = P**depth
    a,b = split(label,rho,modulus)
    a0,b0 = split(tuple(d//divisor for d in label),rho,modulus)
    q = lambda x: b0*x*(x+a)-ell*a0
    root, = [x for x in sorted(SQUARES)
             if (x+a)%P in SQUARES and q(x)%P==0]
    level=P
    for _ in range(1,k):
        level_after=P*level
        root, = [root+j*level for j in range(P) if q(root+j*level)%level_after==0]
        level=level_after
    y=(root+a)%modulus
    assert q(root)%modulus==0 and root%P in SQUARES and y%P in SQUARES
    midpoint=(root+a*pow(2,-1,modulus))%modulus
    phase=(b*midpoint+ell*(p_log(y,k)-p_log(root,k)))%modulus
    c=ell*a0*(2*root+a)*pow(2*root*root*y*y,-1,P)%P
    assert c and phase%divisor==0
    ratio=y*pow(root,-1,P)%P
    return phase,c,ratio,depth,root


def compute():
    support=primitive_stationary_support()
    sample={}
    for k in (2,3,4,5,6):
        rows={}
        for l in (3,10,17,24,3+P**(k-1)):
            rows[l]={}
            for label in SELECTED:
                data=data_at(label,l,k)
                rows[l][str(label)]=data
                lifted=data_at(label,l+P**(k-1),k)
                assert lifted[:4]==data[:4]
        sample[k]=rows
    return {"support":support,"sample":sample}


if __name__=="__main__":
    parser=ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    output=json.dumps(compute(),indent=2)+"\n"
    path=ROOT/"split_law/data/stationary.json"
    if args.verify:
        assert output==path.read_text()
        print("Stationary supports, coefficients, square roots, and phase reductions verified.")
    else:
        path.write_text(output)
        print("Wrote",path)
