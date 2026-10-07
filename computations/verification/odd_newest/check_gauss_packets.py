#!/usr/bin/env python3
"""Independent exact Q(zeta_5) overlap and modular raw-cocycle controls.
No author finite-field, eigenspace or overlap code is imported.
Bounded assertions only; the all-depth bridge is in review.md.
"""

def main(argv=None):
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args(argv)
    output_dir = args.output_dir.resolve()
    repository = Path(__file__).resolve().parents[3]
    if output_dir == repository or repository in output_dir.parents:
        raise RuntimeError('Use a scratch output directory outside the proof overlay or repository')
    output_dir.mkdir(parents=True, exist_ok=True)
    import os
    import json, time
    from fractions import Fraction as F
    from pathlib import Path
    from itertools import product
    START = time.monotonic()
    Z = (F(0),) * 4
    O = (F(1), F(0), F(0), F(0))

    def add(a, b):
        return tuple((x + y for x, y in zip(a, b)))

    def neg(a):
        return tuple((-x for x in a))

    def sub(a, b):
        return add(a, neg(b))

    def smul(a, b):
        return tuple((b * x for x in a))

    def mul(a, b):
        c = [F(0)] * 7
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i + j] += x * y
        for i in range(6, 3, -1):
            for j in range(4):
                c[i - 4 + j] -= c[i]
        return tuple(c[:4])

    def power(a, n):
        b = O
        while n:
            if n & 1:
                b = mul(b, a)
            a = mul(a, a)
            n //= 2
        return b
    eta = (F(0), F(1), F(0), F(0))
    ep = [power(eta, j) for j in range(5)]

    def conj(a):
        b = Z
        for i, x in enumerate(a):
            b = add(b, smul(ep[-i % 5], x))
        return b

    def residue(a):
        if not all((x.denominator % 5 for x in a)):
            raise AssertionError(a)
        return sum((x.numerator * pow(x.denominator, -1, 5) for x in a)) % 5

    def matmul(A, B):
        return [[sumring((mul(x, y) for x, y in zip(row, col))) for col in zip(*B)] for row in A]

    def sumring(xs):
        r = Z
        for x in xs:
            r = add(r, x)
        return r

    def apply(A, v):
        return [sumring((mul(x, y) for x, y in zip(row, v))) for row in A]

    def inner(a, b):
        return sumring((mul(conj(x), y) for x, y in zip(a, b)))

    def weyl(a, b, v):
        return [mul(ep[b * (x + 3 * a) % 5], v[(x + a) % 5]) for x in range(5)]
    g = sumring((ep[x * x % 5] for x in range(5)))
    if not mul(g, g) == smul(O, 5):
        raise AssertionError('Verification failed: mul(g, g) == smul(O, 5)')
    I = [[O if i == j else Z for j in range(5)] for i in range(5)]
    C = [[smul(mul(g, ep[(-x * x - x * y - y * y) % 5]), F(1, 5)) for y in range(5)] for x in range(5)]
    pows = [I]
    for j in range(6):
        pows.append(matmul(pows[-1], C))
    if not pows[6] == I:
        raise AssertionError('Verification failed: pows[6] == I')
    for d, sign, alpha, beta in [(1, 1, -1, -1), (2, -1, 1, -1), (4, -1, -1, 1), (5, 1, 1, 1)]:
        expected = [[smul(mul(g, ep[(alpha * (x * x + y * y) + beta * x * y) % 5]), F(sign, 5)) for y in range(5)] for x in range(5)]
        if not pows[d] == expected:
            raise AssertionError('Verification failed: pows[d] == expected')
    if not pows[3] == [[neg(O) if (x + y) % 5 == 0 else Z for y in range(5)] for x in range(5)]:
        raise AssertionError('Verification failed: pows[3] == [[neg(O) if (x + y) % 5 == 0 else Z for y in range(5)] for x in range(5)]')
    counts = {'coordinate_nonparallel': 0, 'coordinate_parallel': 0, 'plane_nonparallel': 0, 'plane_parallel': 0}
    signs = [0, 1, -1, 0, -1, 1]
    for kind, r, d, a, b in product(['coordinate', 'plane'], range(5), range(6), range(5), range(5)):
        f = [g if x == r else Z for x in range(5)] if kind == 'coordinate' else [ep[r * x % 5] for x in range(5)]
        if not inner(f, f) == smul(O, 5):
            raise AssertionError('Verification failed: inner(f, f) == smul(O, 5)')
        overlap = mul(smul(g, F(1, 5)), inner(f, weyl(a, b, apply(pows[d], f))))
        target = signs[d] * (1 if kind == 'coordinate' else -1) % 5
        if not residue(overlap) == target:
            raise AssertionError((kind, r, d, a, b, overlap, target))
        if not all((x.denominator == 1 for x in overlap)):
            raise AssertionError('Verification failed: all((x.denominator == 1 for x in overlap))')
        counts[kind + ('_parallel' if d in [0, 3] else '_nonparallel')] += 1

    def omega(u, v):
        return u[0] * v[1] - u[1] * v[0]

    def S(u, m):
        return ((3 * u[0] + 4 * u[1]) % m, (2 * u[0] + 3 * u[1]) % m)

    def Q(u, m):
        return (2 * u[1] * u[1] - u[0] * u[0]) % m

    def raw(x, y, n):
        return -(3 * x * x - 2 * x * y + 3 * y * y) * pow(8, -1, n) % n

    def transphase(u, x, n):
        return u[1] * (x + u[0] * pow(2, -1, n)) % n
    cov_checks = 0
    for n in [5, 125]:
        for u in product(range(5), repeat=2):
            v = S(u, n)
            for x, y in product(range(n), repeat=2):
                lhs = (raw(x, (y - u[0]) % n, n) + transphase(u, (y - u[0]) % n, n)) % n
                rhs = (transphase(v, x, n) + raw((x + v[0]) % n, y, n)) % n
                if not lhs == rhs:
                    raise AssertionError((n, u, x, y))
                cov_checks += 1
    carry_checks = 0
    for h in [5, 25]:
        n = 5 * h * h
        for r in product(range(h), repeat=2):
            for delta in [(1, 0), (0, 1), (1, 8), (-1, -8), S(r, n)]:
                v = (r[0] + delta[0], r[1] + delta[1])
                rep = (v[0] % h, v[1] % h)
                d = ((v[0] - rep[0]) // h, (v[1] - rep[1]) // h)
                phase = -omega(rep, v) * pow(2, -1, n) % n
                for z in range(5 * h):
                    x = (-rep[0] + h * z) % n
                    lhs = transphase(v, x, n)
                    rhs = (transphase(rep, x, n) + phase + h * h * transphase(d, z % 5, 5)) % n
                    if not lhs == rhs:
                        raise AssertionError((h, r, delta, z, lhs, rhs))
                    carry_checks += 1
    intertwining_checks = 0
    for h in [5, 25]:
        n = 5 * h * h
        degree = 4 * n // 5
        step = n // 5

        def reduce_sparse(terms):
            v = {}
            for exp, coeff in terms:
                exp %= n
                if exp >= degree:
                    for j in range(4):
                        a = exp - degree + j * step
                        v[a] = v.get(a, 0) - coeff
                else:
                    v[exp] = v.get(exp, 0) + coeff
            return {a: c for a, c in v.items() if c}
        for x in range(n):
            for t in range(5):
                left = reduce_sparse(((raw(x, h * (t + 5 * j), n), 1) for j in range(h)))
                right = reduce_sparse([(h * h * raw(x // h % 5, t, 5), h)]) if x % h == 0 else {}
                if not left == right:
                    raise AssertionError((h, x, t, left, right))
                intertwining_checks += 1
    packet_records = []
    for l in range(1, 9):
        h = 5 ** l
        n = 5 * h * h
        L = 6 * 5 ** (l - 1)

        def mm(A, B, m):
            return tuple((tuple((sum((A[i][k] * B[k][j] for k in range(2))) % m for j in range(2))) for i in range(2)))
        A = ((3, 4), (2, 3))
        B = ((1, 0), (0, 1))
        k = L
        while k:
            if k & 1:
                B = mm(B, A, n)
            A = mm(A, A, n)
            k //= 2
        if not (B[0][0] == B[1][1] and (B[0][0] - 1) % (h * h) == 0):
            raise AssertionError('Verification failed: B[0][0] == B[1][1] and (B[0][0] - 1) % (h * h) == 0')
        if not (B[0][1] == 2 * B[1][0] % n and B[1][0] % h == 0 and (B[1][0] // h % 5 == 2)):
            raise AssertionError('Verification failed: B[0][1] == 2 * B[1][0] % n and B[1][0] % h == 0 and (B[1][0] // h % 5 == 2)')
        if l <= 3:
            circles = {}
            for y in product(range(h), repeat=2):
                if y[0] % 5 == y[1] % 5 == 0:
                    continue
                circles.setdefault(Q(y, h), set()).add(y)
            if not (len(circles) == 4 * h // 5 and all((c % 5 for c in circles))):
                raise AssertionError('Verification failed: len(circles) == 4 * h // 5 and all((c % 5 for c in circles))')
            for c, pts in circles.items():
                v = next(iter(pts))
                v0 = v
                orbit = []
                while v not in orbit:
                    orbit.append(v)
                    v = S(v, h)
                if not (v == v0 and len(orbit) == L and (set(orbit) == pts)):
                    raise AssertionError('Verification failed: v == v0 and len(orbit) == L and (set(orbit) == pts)')
            if not sum((5 * len(s) for s in circles.values())) == 24 * n // 25:
                raise AssertionError('Verification failed: sum((5 * len(s) for s in circles.values())) == 24 * n // 25')
            packet_records.append({'l': l, 'h': h, 'circles': len(circles), 'L': L, 'new_dimension': 24 * n // 25})
    result = {'status': 'passed', 'arithmetic': 'exact rational cyclotomic Q(eta_5), modular integers; no floating-point decisions', 'gauss_overlap_counts': counts, 'total_gauss_overlaps': sum(counts.values()), 'raw_covariance_entries': cov_checks, 'packet_carry_entries': carry_checks, 'raw_oldform_intertwining_entries': intertwining_checks, 'holonomy_valuation_depths': list(range(1, 9)), 'packet_records': packet_records, 'elapsed_seconds': time.monotonic() - START}
    (output_dir / (Path(__file__).stem + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()
