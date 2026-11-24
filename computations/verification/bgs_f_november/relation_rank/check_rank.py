"""Verify finite ranks directly in a cyclotomic tensor basis."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from relation_rank.bgs_packet_check import REMOVAL
from split_law.bgs_packet_check import SELECTED, data_at
from spectrum.bgs_packet_check import COEFFICIENTS

PRIME = 101


def add_phase(row, n, exponent, tame, real, imag):
    """Insert (real+i*imag)*zeta_3^tame*zeta_n^exponent."""
    d = n//7
    exponent %= n
    tame %= 3
    coefficients_n = [(exponent,1)]
    if exponent >= 6*d:
        coefficients_n = [(exponent-6*d+j*d,-1) for j in range(6)]
    coefficients_tame = [(tame,1)] if tame!=2 else [(0,-1),(1,-1)]
    for (a, c) in coefficients_n:
        for (b, x) in coefficients_tame:
            key = 4*a+2*b
            row[key] += c*x*real
            row[key+1] += c*x*imag


def raw_slope(k, h, sign, phases):
    n = 7**k
    d = n//7
    row = defaultdict(int)
    for mode, (phase, hessian, tame, depth, _) in zip(SELECTED,phases):
        real,imag = COEFFICIENTS[mode]
        imag *= 1 if sign==0 else -1
        tame_exponent = h if tame==4 else 0
        # The conductor is k-depth. The quadratic Gauss sum contributes
        # 7 powers with a unit quadratic coefficient when the conductor is odd.
        conductor = k-depth
        if conductor%2:
            shifts = [d*(hessian*x*x%7) for x in range(7)]
        else:
            shifts = [0]
        scale = 7**(conductor//2+depth)
        for shift in shifts:
            exponent = phase+shift
            add_phase(row,n,exponent,tame_exponent,scale*real,scale*imag)
            add_phase(row,n,-exponent,-tame_exponent,scale*real,-scale*imag)
    return {j:x%PRIME for j,x in row.items() if x%PRIME}


def check(k):
    pivots = {}
    count = 0
    classes = {ell for ell,_ in REMOVAL}
    for base in range(3,7**(k-2),7):
        if base%49 not in classes:
            continue
        for u in range(6):
            ell = base+u*7**(k-2)
            phases = [data_at(mode,ell,k) for mode in SELECTED]
            for branch in range(5):
                row = raw_slope(k,branch//2,branch%2,phases)
                while row:
                    j = min(row)
                    factor = row[j]
                    if j not in pivots:
                        inv = pow(factor,-1,PRIME)
                        pivots[j] = {i:x*inv%PRIME for i,x in row.items()}
                        break
                    for i,x in pivots[j].items():
                        reduced = (row.get(i,0)-factor*x)%PRIME
                        if reduced:
                            row[i] = reduced
                        else:
                            row.pop(i,None)
                count += 1
    expected = 180*7**(k-4)
    assert len(pivots)==count==expected
    print(f"k={k}: direct rank {len(pivots)} over F_{PRIME}.")


if __name__=="__main__":
    for k in (4,5,6):
        check(k)
