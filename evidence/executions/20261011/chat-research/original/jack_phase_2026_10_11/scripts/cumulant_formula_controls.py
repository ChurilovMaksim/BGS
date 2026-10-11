"""Exact finite controls for known fourth cumulants and the critical CSE blocks.

All arithmetic uses Fraction; these are finite controls of the human proofs.
The trace-log and direct density routes come from pfaffian_controls.py.
"""
from collections import Counter
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import sys

from pfaffian_controls import (compositions, density, direct_moment,
                               log_coefficient, mean_formula)


def harmonic(N, r=1):
    return sum((F(2, 2*j+1)**r for j in range(N)), F())


def cse_fourth_formula(N, n):
    if n >= 2*N:
        return F(-N)
    if n >= N:
        return (F(N-n) - F(n, 4)*(harmonic(N)-harmonic(n-N))
                - F(n*n, 8)*(harmonic(N, 2)-harmonic(n-N, 2)))
    return (F(n, 8)*(2*harmonic(N-n)-harmonic(N)-harmonic(abs(N-2*n)))
            - F(n*n, 8)*(harmonic(N, 2)-harmonic(N-n, 2)))


def unweighted_trace(N, steps):
    positions = [0]
    for s in steps:
        positions.append(positions[-1]-s)
    if positions[-1] != 0:
        return 0
    return max(0, N-(max(positions)-min(positions)))


def cue_log_coefficient(N, n, a, b):
    result = F()
    for length in range(1, a+b+1):
        for word in compositions(a, b, length):
            weight = F((-1)**(length+1), length)
            for x, y in word:
                weight /= factorial(x)*factorial(y)
            steps = tuple((x-y)*n for x, y in word)
            result += weight*unweighted_trace(N, steps)
    return result


def polymul(p, q, limit):
    out = [F() for _ in range(limit+1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            if i+j <= limit:
                out[i+j] += a*b
    return out


def critical_block_log(N, r):
    A = [F(1, factorial(j)**2) for j in range(r+1)]
    C = [F(1, factorial(j)*factorial(j+1)) for j in range(r+1)]
    aa, cc = polymul(A, A, r), polymul(C, C, r)
    total = F()
    square_sum = F()
    largest = F()
    for q in range(1, 2*N, 2):
        c = F((q-N)**2, q*(2*N-q))
        square_sum += (1+c)**2
        largest = max(largest, 1+c)
        block = aa.copy()
        for j in range(1, r+1):
            block[j] += c*cc[j-1]
        block[0] -= 1
        power = [F(1)]+[F()]*r
        for length in range(1, r+1):
            power = polymul(power, block, r)
            total += F((-1)**(length+1), 2*length)*power[r]
    assert square_sum == F(N, 4)*harmonic(N)+F(N*N, 8)*harmonic(N, 2)
    assert largest <= N
    return total


def check_walk_multiplicity(r):
    count = 0
    for length in range(1, 2*r+1):
        for word in compositions(r, r, length):
            steps = [x-y for x, y in word if x != y]
            if not steps:
                continue
            assert sum(steps) == 0
            position = 0
            sources = []
            for step in steps:
                sources.append(position)
                position -= step
            assert position == 0
            assert max(Counter(sources).values()) <= r
            assert max(abs(s) for s in steps) <= r
            count += 1
    return count


def main(path):
    cse_cases = cue_cases = 0
    for N in range(2, 33):
        for n in range(1, 3*N+1):
            c2, _, _ = log_coefficient(N, n, 1, 1)
            c4, _, _ = log_coefficient(N, n, 2, 2)
            kappa = 4*c4
            assert c2 == mean_formula(N, n)
            assert kappa == cse_fourth_formula(N, n)
            assert kappa <= F(N, 8)*harmonic(N)
            if n >= N:
                assert kappa <= 0
            cse_cases += 1
            cue_mean = cue_log_coefficient(N, n, 1, 1)
            cue_kappa = 4*cue_log_coefficient(N, n, 2, 2)
            assert cue_mean == min(N, n)
            assert cue_kappa == -N+2*max(N-n, 0)-max(N-2*n, 0)
            assert 0 <= cue_mean**2+cue_kappa <= N*N-N
            cue_cases += 1
    block_cases = 0
    for N in range(2, 17):
        for r in (1, 2, 3):
            coefficient, _, _ = log_coefficient(N, N, r, r)
            assert coefficient == critical_block_log(N, r)
            block_cases += 1
    density_cases = 0
    records = []
    for N in (2, 3, 4):
        poly = density(N)
        for n in (N-1, N, N+1):
            m2 = mean_formula(N, n)
            k2 = cse_fourth_formula(N, n)
            c3, _, _ = log_coefficient(N, n, 3, 3)
            k3 = factorial(3)**2*c3
            m6 = direct_moment(N, n, 3, poly)
            assert m6 == 6*m2**3+9*m2*k2+k3
            records.append({"N":N, "n":n, "sixth_moment":str(m6),
                            "mixed_cumulant_33":str(k3)})
            density_cases += 1
    walks = {str(r):check_walk_multiplicity(r) for r in (2, 3)}
    result = {
        "all_passed":True,
        "arithmetic":"exact Fraction; finite formal coefficients",
        "cse_fourth_formula_cases":cse_cases,
        "cue_fourth_formula_cases":cue_cases,
        "range":"N=2..32, n=1..3N",
        "critical_block_coefficient_cases":block_cases,
        "critical_block_range":"N=2..16, balanced orders r=1,2,3",
        "sixth_moment_direct_density_cases":density_cases,
        "sixth_moment_density_range":"N=2,3,4; n=N-1,N,N+1",
        "nonzero_closed_words_checked":walks,
        "records":records,
        "non_claims":[
            "Finite checks do not prove the all-order cumulant theorem or CLT.",
            "Known fourth cumulants are not claimed to be novel.",
            "No deterministic chaotic propagator or BGS repository is inspected."]}
    Path(path).write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("records", "non_claims")}))


if __name__ == "__main__":
    main(sys.argv[1])
