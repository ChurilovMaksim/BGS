"""Exact fixtures for balanced rounding and the prescribed BGS-F pair test."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from fractions import Fraction as F
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent/"data"


def sin_cos_squared_sixth(k):
    # 4 cos^2(k*pi/6), periodic in k modulo six.
    return (4,3,1,0,1,3)[k%6]


def sin_cos_squared_half(k):
    return 4*(k%2==0)


def exact_root_trace(q, a_num, a_den, m):
    # With common denominator 2*a_den*q, the paired shifts are +/- a_num.
    den = 2*a_den*q
    residues = [0]+[(2*a_den*j+sgn*a_num)%den
                    for j in range(q) for sgn in (-1,1)]
    counts = [0]*den
    for x in residues:
        counts[m*x%den] += 1
    return counts


def compute():
    # Riemann-sum coefficients of the exact first pair witness.
    weights = [F(sin_cos_squared_sixth(k)-sin_cos_squared_half(k),4)
               for k in range(1,5)]
    assert weights == [F(3,4),F(-3,4),F(0),F(-3,4)]
    # Elementary enclosure e in (8/3, 11/4) from the exponential series.
    partial = sum(F(1,k) for k in (1,1,2,6,24,120))
    assert F(8,3)<partial and partial+F(7,6*720)<F(11,4)
    assert F(11,4)**4<64 and F(11,4)<F(3,2)**3
    convolution_minimum = F(1,2)*F(1,4)**2
    denominator_maximum = 4*(F(2)/F(8,3))**4
    # w=(phi*phi)^2/(4 I^4). A larger near-origin peak count covers
    # a uniform rational lower bound using only these elementary estimates.
    w_min = convolution_minimum**2 / 2
    assert w_min==F(1,2048) and denominator_maximum<2
    baseline_maximum = F(9,16)*F(3,2)
    q_stride = 32768
    peak_count = q_stride//4
    pair_margin = peak_count*w_min-baseline_maximum
    assert pair_margin == F(101,32)
    assert F(2,q_stride)==F(1,16384)

    # Match short trace roots exactly, as coefficients of finite Fourier
    # polynomials. Complete preimages in each orbit imply zero trace per orbit
    # for m not divisible by q, not just pointwise floating cancellation.
    finite = []
    for q in (5,7,11,19):
        for a_num,a_den in ((1,6),(1,2)):
            for m in range(1,q):
                n = 2*a_den*q
                for sign in (-1,1):
                    orbit = [(m*(2*a_den*j+sign*a_num))%n for j in range(q)]
                    stripe = {x% (2*a_den) for x in orbit}
                    if len(set(orbit))==q:
                        assert len(stripe)==1
                    else:
                        # The nontrivial q-cycle repeats its own subgroup
                        # equally often when gcd(m,q)>1.
                        assert len(set(orbit))>1 and q%len(set(orbit))==0
                    sums = {x:orbit.count(x) for x in set(orbit)}
                    assert len(set(sums.values()))==1
                assert sum(exact_root_trace(q,a_num,a_den,m))==2*q+1
            # Circular gap computation exactly on the common denominator.
            n = 2*a_den*q
            y = sorted({0}|{(2*a_den*j+sgn*a_num)%n
                            for j in range(q) for sgn in (-1,1)})
            assert len(y)==2*q+1
            gaps = [b-a for a,b in zip(y,y[1:]+[n])]
            assert min(gaps)==a_num and sum(y)%n==0
        finite.append({"N":2*q+1,"equal_trace_indices":q-1})

    # Sums needed for the absolute l2 trace-error estimate.
    budgets = []
    for k in (1,2,5,20,49):
        s2 = sum(m*m for m in range(1,k+1))
        s4 = sum(m**4 for m in range(1,k+1))
        assert s2<=k**3 and s4<=k**5
        budgets.append({"K":k,"fractional_coordinates_bound":2*k+1,
                        "sum_square":s2,"sum_fourth":s4})
    return {"lag_fraction_denominator":q_stride,
            "uniform_weight_lower":str(w_min),
            "CUE_baseline_upper":str(baseline_maximum),
            "BGS_pair_defect_lower":str(pair_margin),
            "occupancy_upper":str(F(2,q_stride)),
            "paired_grid_difference_coefficients":[str(x) for x in weights],
            "short_trace_fixtures":finite,"rounding_error_budgets":budgets}


if __name__=="__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true")
    args = parser.parse_args()
    path = DATA/"certificates.json"
    encoded = json.dumps(compute(),indent=2)+"\n"
    if args.verify:
        assert path.read_text()==encoded
        print("Exact BGS weight bounds, grid spectra and short-trace budgets verified.")
    else:
        path.write_text(encoded)
        print("Wrote",path)
