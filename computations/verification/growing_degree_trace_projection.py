#!/usr/bin/env python3
"""Exact finite FLOW-020 controls; no analytic/Ehrenfest certificate.

Rational Wick/Gram calculations, formal Mehler coefficients, actual clock,
identity and balanced-sign trace designs, and independent tensor Casimirs.
The integer composition budget checks bookkeeping, not packet propagation.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as R
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import platform
from itertools import product

from microscopic_noise_removal import neutral_words, partitions, trace_generator
from clock_structure_and_heat_projection import gram, positive_ldl


def multiply(left, right):
    out = defaultdict(R)
    for a, ca in left.items():
        for b, cb in right.items():
            out[tuple(sorted(a+b))] += ca*cb
    return {w: c for w, c in out.items() if c}


def wick_symbolic(m, a, b):
    return {tuple([-m]*(b-k)+[m]*(a-k)):
            R((-m)**k*factorial(k)*comb(a, k)*comb(b, k))
            for k in range(min(a, b)+1)}


def wick_word(word):
    counts = Counter(word)
    out, norm = {(): R(1)}, 1
    for m in sorted({abs(k) for k in word}):
        a, b = counts[m], counts[-m]
        out = multiply(out, wick_symbolic(m, a, b))
        norm *= m**(a+b)*factorial(a)*factorial(b)
    return out, R(norm)


def polynomial_gram(left, right):
    return sum(ca*cb*gram(a, b) for a, ca in left.items()
               for b, cb in right.items())


def solve(matrix, rhs):
    """Independent exact Gaussian elimination for the raw evaluation norm."""
    size = len(rhs)
    a = [list(row)+[x] for row, x in zip(matrix, rhs)]
    for i in range(size):
        pivot = a[i][i]
        assert pivot != 0
        a[i] = [x/pivot for x in a[i]]
        for j in range(size):
            if j != i:
                factor = a[j][i]
                a[j] = [x-factor*y for x, y in zip(a[j], a[i])]
    return [row[-1] for row in a]


def eval_word(word, traces):
    value = R(1)
    for m in word:
        value *= traces[abs(m)]
    return value


def eval_poly(polynomial, traces):
    return sum(c*eval_word(word, traces) for word, c in polynomial.items())


def complex_multiply(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def complex_power(z, n):
    out = (R(1), R(0))
    for _ in range(n):
        out = complex_multiply(out, z)
    return out


def wick_value(m, a, b, z):
    real, imag = R(0), R(0)
    for k in range(min(a, b)+1):
        value = complex_multiply(complex_power(z, a-k),
                                 complex_power((z[0], -z[1]), b-k))
        c = (-m)**k*factorial(k)*comb(a, k)*comb(b, k)
        real += c*value[0]
        imag += c*value[1]
    return real, imag


def mehler_coefficients(m, z, maximum):
    x = (z[0]**2+z[1]**2)/m
    exponential = [R(1)]
    for n in range(1, maximum+1):
        exponential.append(sum(k*2*x*(-1)**(k-1)*exponential[n-k]
                               for k in range(1, n+1))/n)
    return [sum(exponential[n-k] for k in range(0, n+1, 2))
            for n in range(maximum+1)]


def tensor_casimir(n, q):
    """Full U(N) tensor Casimir by swap/contraction, not trace-word D5."""
    labels = list(product(range(n), repeat=2*q))
    indices = {label: i for i, label in enumerate(labels)}
    size = len(labels)
    matrix = [[R(q) if i == j else R(0) for j in range(size)]
              for i in range(size)]
    for column, label in enumerate(labels):
        for a in range(2*q):
            for b in range(a+1, 2*q):
                if (a<q) == (b<q):
                    target = list(label)
                    target[a], target[b] = target[b], target[a]
                    matrix[indices[tuple(target)]][column] += R(1, n)
                elif label[a] == label[b]:
                    for r in range(n):
                        target = list(label)
                        target[a] = target[b] = r
                        matrix[indices[tuple(target)]][column] -= R(1, n)
    return matrix


def compositions(n):
    if n == 0:
        yield ()
    else:
        for r in range(1, n+1):
            for tail in compositions(n-r):
                yield (r,)+tail


def cycle_lengths(permutation):
    visited, sizes = set(), []
    for start in range(len(permutation)):
        if start in visited:
            continue
        current, size = start, 0
        while current not in visited:
            visited.add(current)
            current = permutation[current]
            size += 1
        sizes.append(size)
    return tuple(sorted(sizes))


def permutation_cut_join(lengths):
    """Enumerate actual right transpositions, independent of trace D5."""
    degree, offset = sum(lengths), 0
    permutation = list(range(degree))
    for length in lengths:
        for r in range(length):
            permutation[offset+r] = offset+(r+1) % length
        offset += length
    out = Counter()
    for a in range(degree):
        for b in range(a+1, degree):
            target = list(permutation)
            target[a], target[b] = target[b], target[a]
            out[cycle_lengths(target)] += 1
    return dict(out)


def formula_cut_join(lengths):
    out = defaultdict(R)
    for i, m in enumerate(lengths):
        rest = lengths[:i]+lengths[i+1:]
        for b in range(1, m):
            out[tuple(sorted(rest+(b, m-b)))] += R(m, 2)
    for i, m in enumerate(lengths):
        for j in range(i+1, len(lengths)):
            n = lengths[j]
            rest = tuple(x for k, x in enumerate(lengths) if k not in (i, j))
            out[tuple(sorted(rest+(m+n,)))] += m*n
    return dict(out)


def polynomial_generator(n, polynomial):
    out = defaultdict(R)
    for word, coefficient in polynomial.items():
        for target, value in trace_generator(n, word).items():
            out[target] += coefficient*value
    return {w: c for w, c in out.items() if c}


def top_permutation_generator(n, q, word):
    positive = tuple(m for m in word if m > 0)
    negative = tuple(-m for m in word if m < 0)
    out = defaultdict(R)
    for w, c in wick_word(word)[0].items():
        out[w] -= q*c
    for lengths, other, sign in ((positive, negative, 1),
                                  (negative, positive, -1)):
        for target, coefficient in permutation_cut_join(lengths).items():
            raw = tuple(sorted(tuple(sign*m for m in target)
                               +tuple(-sign*m for m in other)))
            for w, c in wick_word(raw)[0].items():
                out[w] -= R(coefficient, n)*c
    return {w: c for w, c in out.items() if c}


def semidefinite_ldl(matrix):
    """Exact PSD test with zero pivots and residual-column checks."""
    size = len(matrix)
    assert matrix == [list(row) for row in zip(*matrix)]
    lower = [[R(i == j) for j in range(size)] for i in range(size)]
    diagonal = []
    for i in range(size):
        pivot = matrix[i][i]-sum(lower[i][k]**2*diagonal[k] for k in range(i))
        assert pivot >= 0
        diagonal.append(pivot)
        for j in range(i+1, size):
            residual = matrix[j][i]-sum(lower[j][k]*lower[i][k]*diagonal[k]
                                       for k in range(i))
            if pivot:
                lower[j][i] = residual/pivot
            else:
                assert residual == 0
    return diagonal


def run():
    basis_rows, gram_entries = [], 0
    evaluation_cases, clock_cases, lower_cases = 0, 0, 0
    for degree in range(6):
        words = list(neutral_words(degree))
        basis = [wick_word(w) for w in words]
        for i, (left, norm) in enumerate(basis):
            for j, (right, _) in enumerate(basis):
                assert polynomial_gram(left, right) == (norm if i == j else 0)
                gram_entries += 1
        basis_rows.append({'Q': degree, 'dimension': len(words)})
        n = max(4, 2*degree)
        traces_list = [
            {m: R(0) for m in range(1, degree+1)},  # actual N-clock, Q<N
            {m: R(n) for m in range(1, degree+1)},  # actual identity
            {m: R(n if m % 2 == 0 else 0) for m in range(1, degree+1)},
        ]  # actual balanced +1/-1 spectrum: n is even
        raw_gram = [[gram(a, b) for b in words] for a in words]
        for design, traces in enumerate(traces_list):
            kernel = sum(eval_poly(pol, traces)**2/norm for pol, norm in basis)
            ell = (isqrt(1+4*degree)-1)//2
            assert kernel >= R(33, 32)**ell
            lower_cases += 1
            if degree <= 4:
                values = [eval_word(w, traces) for w in words]
                dual = solve(raw_gram, values)
                assert kernel == sum(v*c for v, c in zip(values, dual))
                evaluation_cases += 1
            if design == 0:
                expected = sum(sum(1 for _ in partitions(q)) for q in range(degree+1))
                assert kernel == expected
                clock_cases += 1

    mehler = 0
    for m in (1, 2, 5):
        for z in ((R(0), R(0)), (R(1, 3), R(0)),
                  (R(1), R(1, 2)), (R(2), R(-1, 3))):
            expected = mehler_coefficients(m, z, 12)
            for d in range(13):
                actual = R(0)
                for a in range(d+1):
                    b = d-a
                    real, imag = wick_value(m, a, b, z)
                    actual += (real*real+imag*imag)/(m**d*factorial(a)*factorial(b))
                assert actual == expected[d]
                mehler += 1

    casimir_rows = []
    for n, q in ((2, 1), (3, 1), (2, 2), (3, 2)):
        matrix = tensor_casimir(n, q)
        assert matrix == [list(row) for row in zip(*matrix)]
        size = len(matrix)
        gap = [[(R(2*q*q) if i == j else R(0))-matrix[i][j]
                for j in range(size)] for i in range(size)]
        pivots = positive_ldl(gap)
        casimir_rows.append({'N': n, 'q': q, 'tensor_dimension': size,
                             'upper_gap_min_pivot': str(min(pivots))})

    budget_cases = 0
    for ell in range(1, 9):
        for rs in compositions(ell):
            assert len(rs) <= ell and sum(r+2 for r in rs) <= 3*ell
            budget_cases += 1
    # Exact algebra of the interval certificate used in G13.
    for x in (R(3, 4), R(1), R(5, 4)):
        l2 = 1-2*x+x*x/2
        assert -R(7, 32)-l2 == (x-R(3, 4))*(R(13, 8)-x/2)
        assert (1-x)**2+l2*l2 >= R(1, 32)

    blind_entries = 0
    for degree in range(6):
        for m in range(degree+1, degree+5):
            n = 2*(m+degree)+1
            assert m+degree < n and 2*degree < n
            for word in neutral_words(degree):
                assert gram((m, -m), word)-m*gram((), word) == 0
                blind_entries += 1
    band_covariances = 0
    for m in range(1, 16):
        for n in range(1, 16):
            assert m+n <= 31
            covariance = gram((m, -m), (n, -n))-m*n
            assert covariance == (m*m if m == n else 0)
            band_covariances += 1

    permutation_cases = 0
    for q in range(1, 9):
        for lengths in partitions(q):
            actual = permutation_cut_join(lengths)
            assert actual == formula_cut_join(lengths)
            assert sum(actual.values()) == q*(q-1)//2
            permutation_cases += 1
    top_rows, top_images, top_gram_entries = [], 0, 0
    for q in range(1, 5):
        words = [w for w in neutral_words(q) if sum(m for m in w if m > 0) == q]
        basis = [wick_word(w) for w in words]
        for n in sorted({max(3, 2*q), 2*q+1}):
            images = []
            for word, (polynomial, _) in zip(words, basis):
                image = polynomial_generator(n, polynomial)
                assert image == top_permutation_generator(n, q, word)
                images.append(image)
                top_images += 1
            positive_casimir = [[-polynomial_gram(polynomial, image)
                                 for image in images] for polynomial, _ in basis]
            lower_rate = q-R(q*(q-1), n)
            upper_rate = q+R(q*(q-1), n)
            lower_gap = [[positive_casimir[i][j]-(lower_rate*basis[i][1] if i == j else 0)
                          for j in range(len(words))] for i in range(len(words))]
            upper_gap = [[(upper_rate*basis[i][1] if i == j else 0)-positive_casimir[i][j]
                          for j in range(len(words))] for i in range(len(words))]
            lower_pivots, upper_pivots = semidefinite_ldl(lower_gap), semidefinite_ldl(upper_gap)
            top_gram_entries += len(words)**2
            top_rows.append({'N': n, 'q': q, 'dimension': len(words),
                             'rate_interval': [str(lower_rate), str(upper_rate)],
                             'lower_zero_pivots': lower_pivots.count(R(0)),
                             'upper_zero_pivots': upper_pivots.count(R(0))})

    return {'status': 'PASS', 'wick_basis': basis_rows,
            'exact_wick_gram_entries': gram_entries,
            'exact_raw_vs_orthogonal_evaluation_cases': evaluation_cases,
            'exact_clock_partition_cases': clock_cases,
            'exact_actual_trace_design_lower_cases': lower_cases,
            'exact_mehler_coefficient_cases': mehler,
            'exact_tensor_casimirs': casimir_rows,
            'integer_packet_composition_cases': budget_cases,
            'exact_laguerre_interval_endpoint_cases': 3,
            'exact_sublinear_blind_gram_entries': blind_entries,
            'exact_stable_band_covariance_cases': band_covariances,
            'exact_permutation_cut_join_cases': permutation_cases,
            'exact_top_degree_generator_images': top_images,
            'exact_top_degree_casimir_gram_entries': top_gram_entries,
            'exact_top_degree_casimir_intervals': top_rows,
            'randomness': {'used': False, 'generator': '', 'seed': None},
            'arithmetic': 'Fraction exact rational real/imaginary pairs; no floating diagnostics',
            'non_claims': ['No analytic packet uniformity or asymptotic certificate',
                          'No original-map trajectory/large-N spectrum simulated',
                          'No analytic Lean, actual complementary estimate or BGS'],
            'python': platform.python_version(),
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    body = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(body)
    print(body, end='')


if __name__ == '__main__':
    main()
