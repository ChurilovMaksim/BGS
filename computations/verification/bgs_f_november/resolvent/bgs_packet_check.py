"""Exact constants for resolvent transport and the two finite local tests."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from research.coefficients import raw_symbol

LOWER_PI = F(157, 50)
UPPER_PI = F(22, 7)
A_BOUND = F(593, 500)
PRIMITIVE_BOUND = F(1243, 160000)
NONPRIMITIVE_BOUND = F(567, 200)
TAU = F(1, 10**80)


def ln_interval(x, length=64):
    z = F(x-1, x+1)
    lower = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(length)), F(0))
    tail = 2*z**(2*length+1)/((2*length+1)*(1-z*z))
    return lower, lower+tail


def atan_interval(inverse, length=24):
    z = F(1, inverse)
    lower = sum(((-1)**j*z**(2*j+1)/F(2*j+1) for j in range(length)), F(0))
    return lower, lower+z**(2*length+1)/F(2*length+1)


def coefficients():
    grouped = defaultdict(list)
    nonprimitive = []
    box = raw_symbol()
    assert len(box) == 32
    assert F(sum(abs(a)+abs(b) for a, b in box.values()), 4000) == A_BOUND
    for (a,b), (real, imaginary) in box.items():
        norm = a*a-2*b*b
        val = real*real+imaginary*imaginary
        if a % 7 or b % 7:
            square = (a+3*b) % 7 in (1,2,4)
            assert (a+3*b) % 7 and (a-3*b) % 7
            grouped[norm, square].append(val)
        else:
            assert (a, b) in ((0,7),(0,-7))
            nonprimitive.append(val)
    assert max(q for q,_ in grouped)-min(q for q,_ in grouped) < 7**3
    assert len(grouped) == 22 and len(nonprimitive) == 2
    assert all(len(set(rows)) == 1 for rows in grouped.values())
    prim = F(sum(len(rows)**2*rows[0] for rows in grouped.values()), 4000**2)
    nonprim = F(7*sum(nonprimitive), 4000**2)
    assert prim == PRIMITIVE_BOUND and nonprim == NONPRIMITIVE_BOUND
    return prim, nonprim


def weighted_bound(t, n, near, far):
    return t*t*n*(PRIMITIVE_BOUND*sum(near)*sum(far)
                   +NONPRIMITIVE_BOUND*sum(a*b for a,b in zip(near, far)))


def verify_analysis_constants():
    a0,a1 = atan_interval(5)
    b0,b1 = atan_interval(239)
    # Machin's formula for pi.
    assert LOWER_PI < 16*a0-4*b1 and 16*a1-4*b0 < UPPER_PI
    log7_lower, log7_upper = ln_interval(7)
    log6_lower, _ = ln_interval(6)
    assert F(19, 10) < log7_lower and log7_upper < F(973,500)
    assert F(17,10) < log6_lower
    assert 61*log7_upper < 120 and 31*log7_upper < F(302,5)
    assert UPPER_PI**3 / 54 < F(3,5)


def full_circle(n):
    m = 3*n//7
    rad = F(1,5)
    t = TAU*n
    global_linear_error = F(44,1000)
    assert m > 1000 and F(3,70)+F(3,5*m) < global_linear_error
    # Corrections shown after the harmonic sums in the report.
    residue_zero = (1/rad+(121-F(19,10))/(7*LOWER_PI)
                    + global_linear_error+2*rad/(9*49))
    residue_other = (120/(7*LOWER_PI)+F(7,6)/(2*LOWER_PI)
                     - F(17,10)/(14*UPPER_PI)+global_linear_error+2*rad/9)
    assert residue_zero < F(1047,100) and residue_other < F(57,10)
    env = [F(1047,100)]+[F(57,10)]*6
    leading = weighted_bound(t,n,env,env)
    rem = m*n*((t*A_BOUND)**2/2)**2*(1/rad**2+F(4,9))
    assert leading < F(63,1000)**2
    assert rem < F(1,50000)**2
    beta = F(41,10000)
    assert (F(63,1000)+F(1,50000))**2 < beta
    missing = F(6,7)*(3*beta+F(1,294))+F(1,n)
    traces = [1-F(1,2)*(r*F(101,100)*rad)**2-2*missing for r in (1,2)]
    assert traces[0] > F(4763,5000) and traces[1] > F(4457,5000)
    pair_gap = (F(6854,100000)*traces[0]**2
                +F(1599,100000)*traces[1]**2-F(2067,100000)-F(2282,10000*n))
    assert pair_gap > F(54,1000)
    return {"N": n, "time":m, "bad_nodes_upper": beta, "unmatched_levels_upper": missing,
            "return_first_lower": traces[0], "return_second_lower": traces[1],
            "original_pair_test_lower": pair_gap}


def schur_circle(n):
    m = 3*n//7
    radius = F(7,20)
    t = TAU*n
    top = F(50)*t*m
    length = -(-top.numerator//top.denominator)
    end = (m-1)//2
    assert 1000 < length < end and length*length <= n and end*end <= length*length*n
    assert F(3,5)*length*(length+1)/m**2 < F(1,1000)
    log_bound = F(302, 5)
    zero_near = (1/radius+(1+log_bound-F(19,10))/(7*LOWER_PI)
                 +F(1,1000)+2*radius/(9*49))
    other_near = (log_bound/(7*LOWER_PI)+F(7,6)/(2*LOWER_PI)
                  -F(17,10)/(14*UPPER_PI)+F(1,1000)+2*radius/9)
    all_far = (log_bound/(7*LOWER_PI)+1/(LOWER_PI*length)
               +F(3,70)+F(3,5*m)+radius/(9*length))
    assert zero_near < F(557,100) and other_near < F(298,100)
    assert all_far < F(14,5)
    near = [F(557,100)]+[F(298,100)]*6
    far = [F(14,5)]*7
    x2 = weighted_bound(t,n,near,near)
    y2 = weighted_bound(t,n,near,far)
    assert t*A_BOUND*m/(4*length-radius) < F(1,100)
    assert m/radius*(t*A_BOUND)**2/2 < F(1,500)
    assert F(1,500)+F(101,99)*100*F(1,500)**2 < F(1,400)
    assert F(101,99) < F(103,100)
    beta = (F(5,8)*x2+F(103,100)*y2)/(1-F(1,400)-F(2,5))
    assert beta < F(8971,10000)
    assert F(101,100)*radius*7/(3*LOWER_PI) < F(27,100)
    observed = (1-beta)*F(3,7)*(F(9,5)-F(27,100))
    sine = 2*UPPER_PI**2/9*F(28,100)**3
    assert observed > F(675,10000)
    assert sine < F(482,10000)
    assert observed-sine > F(19,1000)
    return {"N": n,"time":m, "split_index":length,
            "near_hilbert_square_upper":x2,"cross_hilbert_square_upper":y2,
            "bad_nodes_upper":beta,"local_two_point_witness_lower":observed,
            "sine_witness_upper":sine,"witness_gap_lower":observed-sine}



def critical_strip():
    constant = PRIMITIVE_BOUND + NONPRIMITIVE_BOUND/7
    phi_square_upper = F(2619,1000)
    assert (2*phi_square_upper-3)**2 > 5
    beta = phi_square_upper*36*constant/(4*LOWER_PI**2)
    assert beta < F(987,1000)
    assert F(101,100)*F(1,10)*7/(3*LOWER_PI) < F(8,100)
    gap = (1-beta)*F(3,7)*(F(9,5)-F(8,100))-2*UPPER_PI**2*F(9,100)**3/9
    assert gap > F(8,1000)
    return {"constant":constant, "bad_node_limsup_upper":beta,
            "local_witness_gap_liminf_lower":gap}

def serialize(value):
    if isinstance(value,F):
        return {"rational":str(value), "approximation":float(value)}
    if isinstance(value,dict):
        return {key:serialize(item) for key,item in value.items()}
    return value


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify_analysis_constants()
    prim, nonprim = coefficients()
    summary = {"primitive_orbit_constant": prim, "nonprimitive_orbit_constant":nonprim,
               "k60":full_circle(7**60), "k61":full_circle(7**61),
               "k62":schur_circle(7**62), "weak_critical_strip":critical_strip()}
    data = json.dumps(serialize(summary), indent=2)+"\n"
    target = ROOT/"resolvent/data/certificates.json"
    if args.verify:
        assert data == target.read_text()
        print("Exact orbit weights, resolvent constants, and all three fixed-kick certificates agree.")
    else:
        target.write_text(data)
        print("Wrote",target)
