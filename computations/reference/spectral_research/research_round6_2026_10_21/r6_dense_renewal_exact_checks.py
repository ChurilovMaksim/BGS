#!/usr/bin/env python3
"""Exact finite checks for doubled-unitary renewal and bounded mismatch runs.

Only Python integers and rational fractions are used. Coordinate phases
in the rooted counting check are formal Laurent variables. Prime Gauss
checks are performed in Z[X]/(1+X+...+X^(p-1)), not floating point.
These finite checks are not an asymptotic spectral proof.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import prod
from pathlib import Path
import json


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    columns = transpose(B)
    return [[sum(a * b for a, b in zip(row, col))
             for col in columns] for row in A]


def madd(A, B):
    return [[a + b for a, b in zip(arow, brow)]
            for arow, brow in zip(A, B)]


def mscale(A, factor):
    return [[factor * value for value in row] for row in A]


def mpower(A, exponent):
    result = eye(len(A))
    for _ in range(exponent):
        result = matmul(result, A)
    return result


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def hs2(A):
    return sum(value * value for row in A for value in row)


def block(A, rows, cols):
    return [[A[i][j] for j in cols] for i in rows]


def rank(A):
    work = [[Fraction(value) for value in row] for row in A]
    nrows, ncols = len(work), len(work[0])
    pivotrow = 0
    for col in range(ncols):
        piv = next((i for i in range(pivotrow, nrows) if work[i][col]), None)
        if piv is None:
            continue
        work[pivotrow], work[piv] = work[piv], work[pivotrow]
        pivot = work[pivotrow][col]
        work[pivotrow] = [x / pivot for x in work[pivotrow]]
        for i in range(pivotrow + 1, nrows):
            factor = work[i][col]
            if factor:
                work[i] = [x - factor * y
                           for x, y in zip(work[i], work[pivotrow])]
        pivotrow += 1
        if pivotrow == nrows:
            break
    return pivotrow


def characteristic_coefficients(A):
    # det(I-s A) = sum c[k] s^k, by exact Newton identities.
    power = eye(len(A))
    traces = [len(A)]
    coefficients = [1]
    for k in range(1, len(A) + 1):
        power = matmul(power, A)
        traces.append(trace(power))
        numerator = -sum(coefficients[k - j] * traces[j]
                         for j in range(1, k + 1))
        assert numerator % k == 0
        coefficients.append(numerator // k)
    while coefficients[-1] == 0 and len(coefficients) > 1:
        coefficients.pop()
    return coefficients


def verify_blocks(numerator, denominator, signs, max_r=8):
    N = len(numerator)
    assert matmul(numerator, transpose(numerator)) == mscale(eye(N), denominator**2)
    scale = denominator**2
    pairs = list(product(range(N), repeat=2))
    W = [[signs[a] * signs[b] * numerator[a][c] * numerator[b][d]
          for c, d in pairs] for a, b in pairs]
    assert matmul(W, transpose(W)) == mscale(eye(N * N), scale**2)
    m_idx = [i for i, (a, b) in enumerate(pairs) if a == b]
    o_idx = [i for i, (a, b) in enumerate(pairs) if a != b]
    P = block(W, m_idx, m_idx)
    B = block(W, m_idx, o_idx)
    C = block(W, o_idx, m_idx)
    S = block(W, o_idx, o_idx)
    R = [eye(N)]
    F = [None, P]
    Wpower = eye(N * N)
    for r in range(1, max_r + 1):
        Wpower = matmul(Wpower, W)
        R.append(block(Wpower, m_idx, m_idx))
        if r >= 2:
            F.append(matmul(matmul(B, mpower(S, r - 2)), C))
        total = [[0] * N for _ in range(N)]
        for j in range(1, r + 1):
            total = madd(total, matmul(F[j], R[r - j]))
        assert total == R[r]
        assert all(sum(row) == scale**r for row in R[r])
        assert all(sum(col) == scale**r for col in transpose(R[r]))
        if r >= 2:
            assert all(sum(row) == 0 for row in F[r])
            assert all(sum(col) == 0 for col in transpose(F[r]))
    tail_checks = []
    for m in range(1, max_r):
        lhs = [[0] * N for _ in range(N)]
        for r in range(1, m + 2):
            lhs = madd(lhs, mscale(matmul(transpose(F[r]), F[r]),
                                  scale**(2 * (m + 1 - r))))
        survival = matmul(mpower(S, m), C)
        rhs = madd(mscale(eye(N), scale**(2 * (m + 1))),
                   mscale(matmul(transpose(survival), survival), -1))
        assert lhs == rhs
        prev = mpower(S, m)
        later = matmul(prev, S)
        assert hs2(matmul(prev, C)) == hs2(prev) * scale**2 - hs2(later)
        tail_checks.append(m)
    ranks = []
    for m in range(1, N):
        Spower = mpower(S, m)
        defect = madd(mscale(eye(len(S)), scale**(2 * m)),
                      mscale(matmul(transpose(Spower), Spower), -1))
        defect_rank = rank(defect)
        unit_singular_count = len(S) - defect_rank
        required = (N - 1) * (N - m)
        assert unit_singular_count >= required
        ranks.append({"m": m, "unit_singular_values": unit_singular_count,
                      "guaranteed": required})
    determinants = []
    for L in (1, 2, 3):
        dim = N + L * len(S)
        A = [[0] * dim for _ in range(dim)]
        for a in range(N):
            for b in range(N):
                A[a][b] = P[a][b]
            for b in range(len(S)):
                A[a][N + b] = B[a][b]
        for age in range(L):
            offset = N + age * len(S)
            for a in range(len(S)):
                for b in range(N):
                    A[offset + a][b] = C[a][b]
                if age + 1 < L:
                    for b in range(len(S)):
                        A[offset + a][offset + len(S) + b] = S[a][b]
        # Similar to scale times the small companion. The top blocks
        # are the integer numerators F_r, and the subdiagonal is I.
        small_dim = (L + 1) * N
        companion = [[0] * small_dim for _ in range(small_dim)]
        for r in range(1, L + 2):
            for a in range(N):
                for b in range(N):
                    companion[a][(r - 1) * N + b] = F[r][a][b]
        for age in range(1, L + 1):
            for a in range(N):
                companion[age * N + a][(age - 1) * N + a] = 1
        poly_A = characteristic_coefficients(A)
        poly_C = characteristic_coefficients(companion)
        assert poly_A == poly_C
        determinants.append({"L": L, "large_dim": dim,
                             "small_dim": small_dim,
                             "nonzero_determinant_degree": len(poly_A) - 1})
    return {"N": N, "signs": signs, "renewal_orders": max_r,
            "finite_energy_tail_checks": len(tail_checks),
            "isometric_rank_checks": ranks,
            "companion_determinants": determinants}


def trim(poly):
    return {key: value for key, value in poly.items() if value}


def padd(out, poly, multiplier=1):
    for key, value in poly.items():
        out[key] += multiplier * value


def pmul(left, right):
    out = defaultdict(int)
    for lkey, lvalue in left.items():
        for rkey, rvalue in right.items():
            key = tuple(a + b for a, b in zip(lkey, rkey))
            out[key] += lvalue * rvalue
    return trim(out)


def poly_matmul(A, B):
    out = [[defaultdict(int) for _ in B[0]] for _ in A]
    for i, row in enumerate(A):
        for k, left in enumerate(row):
            if left:
                for j, right in enumerate(B[k]):
                    if right:
                        padd(out[i][j], pmul(left, right))
    return [[trim(poly) for poly in row] for row in out]


def poly_trace(A):
    out = defaultdict(int)
    for i in range(len(A)):
        padd(out, A[i][i])
    return trim(out)


def bounded_run_transfer(numerator, L):
    N = len(numerator)
    states = [(a, a, 0) for a in range(N)]
    states += [(a, b, age) for age in range(1, L + 1)
               for a in range(N) for b in range(N) if a != b]
    matrix = [[{} for _ in states] for _ in states]
    for i, (a, b, age) in enumerate(states):
        exponent = [0] * (N + 1)
        exponent[a] += 1
        exponent[b] -= 1
        exponent[-1] = int(a != b)
        for j, (c, d, next_age) in enumerate(states):
            allowed = next_age == 0 or next_age == age + 1
            if allowed:
                matrix[i][j] = {tuple(exponent): numerator[a][c] * numerator[b][d]}
    return matrix


def max_cyclic_run(x, y):
    n = len(x)
    agreement = next((i for i in range(n) if x[i] == y[i]), None)
    if agreement is None:
        return None
    longest = current = 0
    for offset in range(1, n + 1):
        i = (agreement + offset) % n
        if x[i] == y[i]:
            current = 0
        else:
            current += 1
            longest = max(longest, current)
    return longest


def amplitude(H, word):
    return prod(H[word[i]][word[(i + 1) % len(word)]]
                for i in range(len(word)))


def direct_run_polynomial(H, n, L):
    N = len(H)
    out = defaultdict(int)
    counts = defaultdict(int)
    balanced = defaultdict(int)
    for x in product(range(N), repeat=n):
        ax = amplitude(H, x)
        for y in product(range(N), repeat=n):
            run = max_cyclic_run(x, y)
            if run is None or run > L:
                continue
            exponent = [0] * (N + 1)
            for a, b in zip(x, y):
                exponent[a] += 1
                exponent[b] -= 1
                exponent[-1] += int(a != b)
            key = tuple(exponent)
            out[key] += ax * amplitude(H, y)
            counts[exponent[-1]] += 1
            if not any(exponent[:-1]):
                balanced[exponent[-1]] += 1
    return trim(out), dict(counts), dict(balanced)


def verify_rooted_counting(H, denominator, L, max_n):
    A = bounded_run_transfer(H, L)
    Apower = A
    total_pairs = 0
    cases = []
    for n in range(1, max_n + 1):
        direct, counts, balanced = direct_run_polynomial(H, n, L)
        assert direct == poly_trace(Apower)
        total_pairs += sum(counts.values())
        cases.append({"n": n, "rooted_pairs": sum(counts.values()),
                      "balanced_by_mismatch_count": balanced})
        if n != max_n:
            Apower = poly_matmul(Apower, A)
    return {"N": len(H), "L": L, "max_n": max_n,
            "rooted_pairs_checked": total_pairs,
            "integer_numerator_denominator": denominator,
            "cases": cases}


def cyclo_canonical(a):
    # Vectors have length p. Subtract the coefficient of X^(p-1)
    # times the cyclotomic polynomial 1+...+X^(p-1).
    last = a[-1]
    return tuple(value - last for value in a)


def cyclo_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def cyclo_scale(a, scalar):
    return tuple(value * scalar for value in a)


def cyclo_mul(a, b):
    p = len(a)
    out = [0] * p
    for i, avalue in enumerate(a):
        if avalue:
            for j, bvalue in enumerate(b):
                if bvalue:
                    out[(i + j) % p] += avalue * bvalue
    return cyclo_canonical(out)


def cyclo_conjugate(a):
    p = len(a)
    return cyclo_canonical([a[(-i) % p] for i in range(p)])


def gauss_numerator(p, j, displacement):
    out = [0] * p
    for k in range(p):
        out[(j * k * k + displacement * k) % p] += 1
    return cyclo_canonical(out)


def circulant_product(A, B):
    p = len(A)
    result = []
    for r in range(p):
        entry = (0,) * p
        for s in range(p):
            entry = cyclo_add(entry, cyclo_mul(A[s], B[(r - s) % p]))
        result.append(entry)
    return result


def verify_prime_delay(p):
    constant = lambda value: (value,) + (0,) * (p - 1)
    original = [gauss_numerator(p, 1, r) for r in range(p)]
    power = [constant(int(r == 0)) for r in range(p)]
    gauss_checks = 0
    for j in range(1, 2 * p + 1):
        power = circulant_product(power, original)
        target = [gauss_numerator(p, j, r) for r in range(p)]
        assert power == [cyclo_scale(entry, p**(j - 1)) for entry in target]
        for r, entry in enumerate(target):
            square = cyclo_mul(entry, cyclo_conjugate(entry))
            required = p if j % p else p * p * int(r == 0)
            assert square == constant(required)
            gauss_checks += 1
    J = [[Fraction(1, p) for _ in range(p)] for _ in range(p)]
    I = eye(p)
    H = madd(I, mscale(J, -1))
    R = [I if n % p == 0 else J for n in range(3 * p + 1)]
    for n in range(1, len(R)):
        renewal = matmul(J, R[n - 1])
        if n >= p:
            renewal = madd(renewal, matmul(H, R[n - p]))
        assert renewal == R[n]
    total_energy = hs2(J) + hs2(H)
    weighted_energy = hs2(J) + p * hs2(H)
    assert total_energy == p
    assert weighted_energy == p * p - p + 1
    assert p * p - weighted_energy == p - 1
    # The tail formula recovers the exact singular-value energy.
    a = p * p - p
    singular_energies = [a]
    for m in range(1, 2 * p + 1):
        survival = p - 1 if m <= p - 1 else 0
        a -= survival
        required = (p - 1) * (p - m) if m <= p - 1 else p - 1
        assert a == required
        singular_energies.append(a)
    return {"p": p, "cyclotomic_gauss_modulus_checks": gauss_checks,
            "exact_power_orders": 2 * p,
            "renewal_orders": len(R) - 1,
            "return_support": [1, p],
            "total_energy": str(total_energy),
            "weighted_energy": str(weighted_energy),
            "dark_dimension": p - 1,
            "compressed_power_HS2": singular_energies}


def main():
    H2 = [[3, 4], [4, -3]]
    H3 = [[7, -4, -4], [-4, 1, -8], [-4, -8, 1]]
    blocks = [
        verify_blocks(H2, 5, [1, 1]),
        verify_blocks(H2, 5, [1, -1]),
        verify_blocks(H3, 9, [1, 1, 1]),
        verify_blocks(H3, 9, [1, -1, 1]),
    ]
    counting = [
        verify_rooted_counting(H2, 5, 1, 7),
        verify_rooted_counting(H2, 5, 2, 7),
        verify_rooted_counting(H2, 5, 3, 7),
        verify_rooted_counting(H3, 9, 2, 4),
    ]
    primes = [verify_prime_delay(p) for p in (3, 5, 7, 11, 13)]
    result = {
        "status": "ALL EXACT CHECKS PASSED",
        "arithmetic": "integers, fractions, formal Laurent polynomials, exact cyclotomic rings",
        "block_cases": blocks,
        "rooted_run_cases": counting,
        "rooted_pairs_checked_total": sum(case["rooted_pairs_checked"] for case in counting),
        "prime_delay_cases": primes,
        "gauss_modulus_checks_total": sum(case["cyclotomic_gauss_modulus_checks"] for case in primes),
        "scope": "finite identities only; no assertion of H_diag or a spectral limit",
    }
    target = Path(__file__).with_name("r6_dense_renewal_exact_checks_result.md")
    target.write_text(
        "# Exact renewal and bounded-run verification\n\n"
        "21 October 2026. All arithmetic was exact. Formal coordinate phase "
        "variables were retained in the rooted counting comparison, so no "
        "finite phase grid was substituted for Fourier extraction.\n\n"
        "The complete mathematical proofs are in "
        "r6_dense_renewal_long_return_obstruction.md. These tests check finite "
        "algebra and indexing only; they do not prove any spectral asymptotic.\n\n"
        "~~~json\n" + json.dumps(result, indent=2) + "\n~~~\n"
    )
    print(json.dumps({
        "status": result["status"],
        "block_cases": len(blocks),
        "rooted_pairs_checked": result["rooted_pairs_checked_total"],
        "gauss_modulus_checks": result["gauss_modulus_checks_total"],
        "result_file": str(target),
    }, indent=2))


if __name__ == "__main__":
    main()
