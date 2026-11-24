"""Exact characteristic-two certificates for primitive doublets."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from spectrum.bgs_packet_check import COEFFICIENTS, SQUARES, exact_first_order, p_log, rho_at, split

P = 7
TAME_EXP = {pow(3, i, P): i%3 for i in range(6)}
ODD_MODES = tuple(v for v, (real, imaginary) in COEFFICIENTS.items() if (real+imaginary)%2)


def integer_square_terms():
    # T(a,b)T(c,d)=e_N((ad-bc)/2)T(a+c,b+d).
    terms = Counter()
    for a,b in ODD_MODES:
        for c,d in ODD_MODES:
            terms[a+c,b+d,a*d-b*c] ^= 1
    return sorted(v for v, bit in terms.items() if bit)


def prepared_terms(k, second):
    n = P**k
    rho = rho_at(k)
    half = pow(2,-1,n)
    digits = integer_square_terms() if second else [(*v,0) for v in ODD_MODES]
    return [(split((a,b),rho,n),half*integer_cocycle%n,a,b,integer_cocycle)
            for a,b,integer_cocycle in digits]


def stationary_certificate(k, classes):
    n = P**k
    half = pow(2,-1,n)
    logs = {x:p_log(x,k) for x in range(1,n) if x%P}
    row = defaultdict(list)
    for (a,b),c,v1,v2,c0 in prepared_terms(k,True):
        # a=0 mod 7 cannot change square class.
        if a%P==0:
            continue
        inverse = pow(a,-1,n)
        for x,log_x in logs.items():
            if x%P not in SQUARES:
                continue
            y = (x+a)%n
            if y%P==0 or y%P in SQUARES:
                continue
            ell = b*x*y*inverse%n
            if ell%P not in classes:
                continue
            exponent = (b*(x+half*a)+c+ell*(logs[y]-log_x))%n
            simple = (b*(2*x+a))%P != 0
            row[ell].append((exponent,v1,v2,c0,x,simple))
    witnesses = {}
    for ell in range(1,n):
        if ell%P not in classes:
            continue
        counts = Counter(t[0] for t in row[ell])
        candidates = sorted(t[:-1] for t in row[ell] if t[-1] and counts[t[0]]==1)
        witnesses[ell] = candidates[0] if candidates else None
    return witnesses


def direct_reductions(k, second):
    """Use F4[X]/(X^(3s)+X^s+1) with s=7^(k-1)."""
    n = P**k
    s = n//P
    half = pow(2,-1,n)
    logs = {x:p_log(x,k) for x in range(1,n) if x%P}
    terms = []
    for (a,b),c,_,_,_ in prepared_terms(k,second):
        for x,log_x in logs.items():
            y = (x+a)%n
            if x%P in SQUARES and y%P and y%P not in SQUARES:
                terms.append(((b*(x+half*a)+c)%n, (logs[y]-log_x)%n,
                              TAME_EXP[y%P]-TAME_EXP[x%P]))

    # y^3=y+1 modulo y^3+y+1. Values are bit vectors in basis 1,y,y^2.
    reduction = [1,2,4]
    for i in range(3,7):
        reduction.append(reduction[i-2]^reduction[i-3])
    assert reduction==[1,2,4,3,6,7,5]
    found = {}
    for ell in range(1,s):
        if ell%P==0:
            continue
        for h in range(3):
            result = [0]*(3*s)
            for phase,log,tame in terms:
                quotient,remainder = divmod((phase+ell*log)%n,s)
                coefficient = (1,2,3)[(h*tame)%3]  # w^2=w+1 over F2.
                for i in range(3):
                    if reduction[quotient]>>i&1:
                        result[remainder+i*s] ^= coefficient
            found[ell,h] = next(((i,v) for i,v in enumerate(result) if v),None)
    return found


def depth_two_refinement():
    rows = []
    for v in ((0,1),(0,-1)):
        a,b = split(v,3,7)
        for x in sorted(SQUARES):
            y = (x+a)%7
            if y and y not in SQUARES:
                ell = b*x*y*pow(a,-1,7)%7
                rows.append((v,x,y,ell,(2*x+a)%7!=0))
    assert rows==[((0,1),2,5,4,False),((0,-1),1,5,2,True),((0,-1),2,6,2,True)]
    ratio = Fraction(1,49)
    condition = (1 + Fraction(6,7)*Fraction(1,7)/2/(1-ratio))/6
    assert condition==Fraction(17,96)
    increment = Fraction(36,49)*ratio*condition
    assert increment==Fraction(51,19208)
    return rows, condition, increment


def compute():
    terms = integer_square_terms()
    assert len(ODD_MODES)==12 and len(terms)==108
    # Equal triples modulo 49 are already equal over the integers.
    assert all(abs(z)<=18 for v in terms for z in v)
    assert len({tuple(z%49 for z in v) for v in terms})==len(terms)
    witnesses = stationary_certificate(2,set(range(1,7)))
    success_counts = [sum(v is not None for ell,v in witnesses.items() if ell%7==a)
                      for a in range(1,7)]
    print("Stationary witness counts modulo 49:",success_counts)
    assert all(witnesses[ell][:4] == (11,0,10,0) for ell in range(4,49,7))
    levels = {}
    for k in (2,3):
        second = direct_reductions(k,True)
        first = direct_reductions(k,False)
        required = {4,6} if k==2 else {4}
        known_first = exact_first_order(k)
        assert all((failures>0)==(residue in required)
                   for residue,(failures,successes) in known_first.items())
        assert all(second[key] is not None for key in second if key[0]%7 in required)
        print(f"k={k}: checked every primitive doublet by first or second order.")
        levels[k] = {f"{ell}:{h}": [first[ell,h],second[ell,h]] for ell,h in second}

    old = Fraction(345,392)
    new = old + Fraction(36,49)*Fraction(13,96)
    assert new == Fraction(48,49)
    long_time = Fraction(64549,57624)- Fraction(36,49)*Fraction(13,96)
    assert long_time==Fraction(7352,7203)
    rows, fraction, increment = depth_two_refinement()
    assert new+increment==Fraction(18867,19208)
    assert long_time-increment==Fraction(58663,57624)
    return {"odd_modes":ODD_MODES, "square_terms":terms, "stationary_witnesses_mod_49":witnesses,
            "direct_finite_field":levels,
            "depth_two":{"support":rows,"new_split_fraction":str(fraction),"increase":str(increment)},
            "density_lower":str(new+increment), "long_time_upper":str(long_time-increment)}


if __name__=="__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args = parser.parse_args()
    path = ROOT/"exact_splitting/data/certificates.json"
    content = json.dumps(compute(),indent=2)+"\n"
    if args.verify:
        assert path.read_text()==content
        print("Exact characteristic-two certificates verified.")
    else:
        path.write_text(content)
        print("Wrote",path)
