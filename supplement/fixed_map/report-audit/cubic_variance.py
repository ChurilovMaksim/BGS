"""Exact chamber certificate and CUE variance for the cubic diagnostic.

The chamber coverage proof is in cubic_variance.md. The coefficients below
are computed symbolically over Q, not inferred by fitting sample values.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from fractions import Fraction as F
from itertools import permutations, product
import json
import math
from pathlib import Path

import numpy as np

from verify import partitions, cue_moment, vandermonde_moment


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def affine_cumulant(forms, witness):
    """Return coefficients of (dimension, variables...) in one chamber."""
    nvars = len(forms[0])
    zero = (0,) * nvars
    assert tuple(map(sum, zip(*forms))) == zero
    result = [F(0)] * (nvars + 1)
    N, *point = witness
    for p in partitions(len(forms)):
        ell = len(p)
        factor = F((-1)**(ell-1), ell)
        for ordered in permutations(p):
            positions = [zero]
            for block in ordered:
                step = tuple(sum(forms[j][i] for j in block) for i in range(nvars))
                positions.append(tuple(a+b for a, b in zip(positions[-1], step)))
            low = min(positions, key=lambda v: dot(v, point))
            high = max(positions, key=lambda v: dot(v, point))
            span = tuple(a-b for a, b in zip(high, low))
            if dot(span, point) < N:
                result[0] += factor
                for i, x in enumerate(span):
                    result[i+1] -= factor*x
    return tuple(result)


def chamber_certificate():
    assert len(partitions(6)) == 203
    assert sum(math.factorial(len(p)) for p in partitions(6)) == 4683
    forms6 = ((1,0,0,0),(0,1,0,0),(-1,-1,0,0),
              (0,0,-1,0),(0,0,0,-1),(0,0,1,1))
    records = []
    for sorted_point in ((72,73,76,78),(72,74,76,77)):
        for point in permutations(sorted_point):
            a,b,c,d = point
            sign = 1 if a+b>c+d else -1
            expected = (F(3),F(-1+sign),F(-1+sign),F(-1-sign),F(-1-sign))
            got = affine_cumulant(forms6, (100,)+point)
            assert got == expected, (point, got, expected)
            records.append({"witness": [100,*point], "coefficients": [str(x) for x in got]})
    forms4 = ((0,1,0),(-1,-1,0),(0,0,-1),(1,0,1))
    for point in permutations((72,75,78)):
        assert affine_cumulant(forms4, (100,)+point) == (F(-1),F(1),F(0),F(0))
    return records


def variance_exact(N, weights):
    """Rational variance formula for arbitrary rational nonnegative weights."""
    Q = sum(weights.values())
    conv = {}
    for a,qa in weights.items():
        assert F(2,3)*N<a<F(4,5)*N
        for b,qb in weights.items():
            conv[a+b] = conv.get(a+b,F(0)) + qa*qb
    six = sum(rs*rt*(3*N-2*min(s,t)) for s,rs in conv.items() for t,rt in conv.items())
    fourtwo = 4*Q**2*sum(a*qa**2*(a-N) for a,qa in weights.items())
    fourtwo += N*sum(rs**2*(N-s) for s,rs in conv.items())
    pairs = 2*N*sum(a*qa**2 for a,qa in weights.items())**2
    mean = 2*sum(a*qa for a,qa in weights.items())/(N*Q)-1
    return mean, (six+fourtwo+pairs)/(N*N*Q**4)


def independent_checks():
    # Direct Vandermonde integral, with no cumulant formula in this comparison.
    N = 4
    mean, variance = variance_exact(N, {3:F(1)})
    moment = vandermonde_moment(N, (3,3,-6,-3,-3,6))
    assert F(moment,N*N)-mean**2 == variance == F(13,4)
    # Two-mode weighted check against the unsimplified general moment formula.
    N, weights = 26, {19:F(1),20:F(2)}
    mean, variance = variance_exact(N, weights)
    second = F(0)
    for a,b,c,d in product(weights,repeat=4):
        second += weights[a]*weights[b]*weights[c]*weights[d]*cue_moment(N,(a,b,-a-b,-c,-d,c+d))
    second /= N*N*sum(weights.values())**4
    assert second-mean**2 == variance
    return {"direct_density_N4_mean": "1/2", "direct_density_N4_variance": "13/4",
            "two_mode_N26_mean": str(mean), "two_mode_N26_variance": str(variance)}


def calibrate():
    data = json.loads(Path(__file__).with_name('monodromy_experiment.json').read_text())
    assert data['status'] == 'completed'
    rows = []
    for row in data['rows']:
        N = row['N']
        a = np.arange(math.ceil(.71*N),math.floor(.79*N)+1,dtype=float)
        v = (a/N-.75)/.04
        q = np.zeros_like(v)
        interior = abs(v)<1
        q[interior] = np.exp(-1/(1-v[interior]**2))
        Q = q.sum()
        r = np.convolve(q,q)
        s = np.arange(2*a[0],2*a[-1]+1)
        six = np.sum(r[:,None]*r[None,:]*(3*N-2*np.minimum(s[:,None],s[None,:])))
        fourtwo = 4*Q**2*np.sum(a*q*q*(a-N))+N*np.sum(r*r*(N-s))
        pairs = 2*N*np.sum(a*q*q)**2
        variance = float((six+fourtwo+pairs)/(N*N*Q**4))
        value = complex(*row['smoothed_cubic'])
        difference = abs(value-row['cue_cubic_reference'])
        assert variance>0
        rows.append({"N":N,"kappa":row['kappa'],"cue_complex_variance":variance,
                     "cue_root_mean_square_fluctuation":math.sqrt(variance),
                     "observed_complex_distance_from_cue_mean":difference,
                     "distance_over_cue_rms":difference/math.sqrt(variance)})
    return rows


if __name__ == '__main__':
    cert = chamber_certificate()
    result = {"status":"completed", "exact_sixth_cumulant_chambers":cert,
              "independent_checks":independent_checks(),"finite_calibration":calibrate(),
              "scope":"CUE reference variance; ratios are not p-values or a proof of the deterministic model's law"}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"chambers":len(cert),"checks":result['independent_checks'],
                      "calibration":result['finite_calibration']},indent=2))
