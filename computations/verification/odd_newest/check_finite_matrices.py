#!/usr/bin/env python3
"""Independent F_5[z]/Phi_7 field, raw 7-kernel eigenspaces, and division-free determinant.
No author arithmetic, nullspace or polynomial code is imported.
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
    import json, time, itertools, hashlib
    from pathlib import Path
    START = time.monotonic()
    P = 5
    Q = 5 ** 6
    ONE = 1
    D = [tuple((i // 5 ** j % 5 for j in range(6))) for i in range(Q)]

    def encode(a):
        return sum((x * 5 ** j for j, x in enumerate(a)))

    def add(a, b):
        return encode([(x + y) % 5 for x, y in zip(D[a], D[b])])

    def neg(a):
        return encode([-x % 5 for x in D[a]])

    def sub(a, b):
        return encode([(x - y) % 5 for x, y in zip(D[a], D[b])])

    def pmul(a, b):
        c = [0] * 11
        for i, x in enumerate(D[a]):
            for j, y in enumerate(D[b]):
                c[i + j] = (c[i + j] + x * y) % 5
        for i in range(10, 5, -1):
            for j in range(6):
                c[i - 6 + j] = (c[i - 6 + j] - c[i]) % 5
        return encode(c[:6])

    def ppow(a, k):
        b = 1
        while k:
            if k & 1:
                b = pmul(b, a)
            a = pmul(a, a)
            k //= 2
        return b
    if not len({pow(5, j, 7) for j in range(6)}) == 6:
        raise AssertionError('Verification failed: len({pow(5, j, 7) for j in range(6)}) == 6')
    GEN = next((a for a in range(2, Q) if all((ppow(a, (Q - 1) // p) != 1 for p in [2, 3, 7, 31]))))
    EXP = []
    LOG = [-1] * Q
    a = 1
    for j in range(Q - 1):
        if not LOG[a] == -1:
            raise AssertionError('Verification failed: LOG[a] == -1')
        LOG[a] = j
        EXP.append(a)
        a = pmul(a, GEN)
    if not (a == 1 and all((k >= 0 for k in LOG[1:]))):
        raise AssertionError('Verification failed: a == 1 and all((k >= 0 for k in LOG[1:]))')

    def mul(a, b):
        return EXP[(LOG[a] + LOG[b]) % (Q - 1)] if a and b else 0

    def inv(a):
        if not a:
            raise AssertionError('Verification failed: a')
        return EXP[-LOG[a] % (Q - 1)]

    def powf(a, k):
        if not (a or k > 0):
            raise AssertionError('Verification failed: a or k > 0')
        return EXP[LOG[a] * k % (Q - 1)] if a else 0

    def dot(a, b):
        r = 0
        for x, y in zip(a, b):
            r = add(r, mul(x, y))
        return r

    def mm(A, B):
        return [[dot(row, col) for col in zip(*B)] for row in A]

    def identity(n):
        return [[int(i == j) for j in range(n)] for i in range(n)]

    def elim(A):
        A = [r[:] for r in A]
        r = 0
        piv = []
        for j in range(len(A[0])):
            k = next((k for k in range(r, len(A)) if A[k][j]), None)
            if k is None:
                continue
            A[r], A[k] = (A[k], A[r])
            A[r] = [mul(inv(A[r][j]), x) for x in A[r]]
            for k in range(len(A)):
                if k != r:
                    s = A[k][j]
                    A[k] = [sub(x, mul(s, y)) for x, y in zip(A[k], A[r])]
            piv.append(j)
            r += 1
            if r == len(A):
                break
        return (A, piv)

    def nullspace(A):
        R, piv = elim(A)
        free = [j for j in range(len(A[0])) if j not in piv]
        out = []
        for j in free:
            v = [0] * len(A[0])
            v[j] = 1
            for k, c in enumerate(piv):
                v[c] = neg(R[k][j])
            out.append(v)
        return out

    def inverse(A):
        n = len(A)
        R, piv = elim([r + e for r, e in zip(A, identity(n))])
        if not [r[:n] for r in R] == identity(n):
            raise AssertionError('Verification failed: [r[:n] for r in R] == identity(n)')
        return [r[n:] for r in R]

    def padd(a, b):
        c = [0] * max(len(a), len(b))
        for j in range(len(c)):
            c[j] = add(a[j] if j < len(a) else 0, b[j] if j < len(b) else 0)
        return c

    def pscale(a, x):
        return [mul(v, x) for v in a]

    def trim(a):
        while len(a) > 1 and (not a[-1]):
            a.pop()
        return a

    def rem(a, b):
        a = trim(a[:])
        b = trim(b[:])
        while a != [0] and len(a) >= len(b):
            k = len(a) - len(b)
            s = mul(a[-1], inv(b[-1]))
            for j, v in enumerate(b):
                a[j + k] = sub(a[j + k], mul(s, v))
            trim(a)
        return a

    def gcd(a, b):
        while b != [0]:
            a, b = (b, rem(a, b))
        return pscale(a, inv(a[-1]))

    def charpoly(A):
        n = len(A)
        dp = {0: [1]}
        for r in range(n):
            nd = {}
            for mask, pol in dp.items():
                for c in range(n):
                    if mask >> c & 1:
                        continue
                    sign = 4 if (mask >> c + 1).bit_count() % 2 else 1
                    v = pscale(pol, mul(sign, neg(A[r][c])))
                    if r == c:
                        v = padd(v, [0] + pscale(pol, sign))
                    key = mask | 1 << c
                    nd[key] = padd(nd.get(key, []), v)
            dp = nd
        return trim(dp[(1 << n) - 1])
    w = 5
    if not (powf(w, 7) == 1 and w != 1):
        raise AssertionError('Verification failed: powf(w, 7) == 1 and w != 1')
    xi = powf(GEN, (Q - 1) // 6)
    om = powf(xi, 2)
    if not (powf(xi, 3) == 4 and powf(om, 3) == 1 and (om != 1)):
        raise AssertionError('Verification failed: powf(xi, 3) == 4 and powf(om, 3) == 1 and (om != 1)')
    wp = [powf(w, j) for j in range(7)]
    G = [[wp[-(3 * x * x - 2 * x * y + 3 * y * y) % 7] for y in range(7)] for x in range(7)]
    tr = 0
    for j in range(7):
        tr = add(tr, G[j][j])
    H = [[mul(inv(tr), x) for x in r] for r in G]
    if not mm(mm(H, H), H) == identity(7):
        raise AssertionError('Verification failed: mm(mm(H, H), H) == identity(7)')
    cols = []
    labels = []
    dimensions = []
    for z in [1, om, powf(om, 2)]:
        A = [[sub(H[i][j], z if i == j else 0) for j in range(7)] for i in range(7)]
        basis = nullspace(A)
        dimensions.append(len(basis))
        cols += basis
        labels += [z] * len(basis)
    if not dimensions == [3, 2, 2]:
        raise AssertionError('Verification failed: dimensions == [3, 2, 2]')
    V = list(map(list, zip(*cols)))
    Vi = inverse(V)
    if not mm(Vi, V) == identity(7):
        raise AssertionError('Verification failed: mm(Vi, V) == identity(7)')
    weights = {0: 4, 1: 2, -1: 2, 6: -1, -6: -1, 7: -2, -7: -2, 8: -1, -8: -1}
    actual_upper = {b: (-3 * k + 2 * (-4 * k)) % 5 for b, k in weights.items()}
    import importlib.util
    spec = importlib.util.spec_from_file_location('frozen_dictionary', Path(__file__).with_name('coefficients.py'))
    rawmod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rawmod)
    coeff = rawmod.coefficients()
    if not (len(coeff) == 32 and {v for v, (a, b) in coeff.items() if (a + 2 * b) % 5} == {(1, b) for b in actual_upper}):
        raise AssertionError('Verification failed: len(coeff) == 32 and {v for v, (a, b) in coeff.items() if (a + 2 * b) % 5} == {(1, b) for b in actual_upper}')
    if not all(((coeff[1, b][0] + 2 * coeff[1, b][1]) % 5 == d for b, d in actual_upper.items())):
        raise AssertionError('Verification failed: all(((coeff[1, b][0] + 2 * coeff[1, b][1]) % 5 == d for b, d in actual_upper.items()))')
    B = {}
    for b in actual_upper:
        T = [[wp[b * (x + 4) % 7] if y == (x + 1) % 7 else 0 for y in range(7)] for x in range(7)]
        B[b] = mm(Vi, mm(T, V))
    records = []
    signs = [0, 1, -1, 0, -1, 1]
    for c in range(1, 5):
        y = {1: (2, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0)}[c]
        orbit = []
        for k in range(6):
            orbit.append(y)
            y = ((3 * y[0] + 4 * y[1]) % 5, (2 * y[0] + 3 * y[1]) % 5)
        if not (y == orbit[0] and len(set(orbit)) == 6):
            raise AssertionError('Verification failed: y == orbit[0] and len(set(orbit)) == 6')
        index = {v: k for k, v in enumerate(orbit)}
        for t in range(6):
            gamma = [mul(powf(xi, t), inv(z)) for z in labels]
            C = [[0] * 7 for _ in range(7)]
            for b, d in actual_upper.items():
                for ky, y in enumerate(orbit):
                    dest = ((y[0] + 1) % 5, (y[1] + b) % 5)
                    if dest not in index:
                        continue
                    kx = index[dest]
                    s = signs[(ky - kx) % 6] * (1 if c in [1, 4] else -1) % 5
                    for i, j in itertools.product(range(7), repeat=2):
                        term = mul(mul(mul(d, s), B[b][i][j]), mul(powf(gamma[i], kx), powf(gamma[j], -ky)))
                        C[i][j] = add(C[i][j], term)
            pol = charpoly(C)
            if not (len(pol) == 8 and pol[-1] == 1):
                raise AssertionError('Verification failed: len(pol) == 8 and pol[-1] == 1')
            der = trim([mul(j % 5, pol[j]) for j in range(1, len(pol))])
            gd = gcd(pol, der)
            if not gd == [1]:
                raise AssertionError((c, t, pol, gd))
            R = [[0] * 7 for _ in range(7)]
            for a in reversed(pol):
                R = mm(R, C)
                for j in range(7):
                    R[j][j] = add(R[j][j], a)
            if not not any((x for row in R for x in row)):
                raise AssertionError('Verification failed: not any((x for row in R for x in row))')
            records.append({'norm_mod5': c, 'tame_index': t, 'characteristic_ascending': pol, 'gcd_degree': len(gd) - 1, 'cayley_hamilton': True})
    f63 = [1, 0, 1, 3, 1, 0, 1]

    def eval_coeff(coeff, a):
        v = 0
        for c in reversed(coeff):
            v = add(mul(v, a), c)
        return v
    alpha_roots = []
    for r in range(63):
        a = powf(GEN, (Q - 1) // 63 * r)
        if eval_coeff(f63, a) == 0 and powf(a, 9) == w:
            alpha_roots.append(a)
    if not len(alpha_roots) == 1:
        raise AssertionError('Verification failed: len(alpha_roots) == 1')
    alpha = alpha_roots[0]

    def map_author(v):
        return eval_coeff(D[v], alpha)
    author_xi = powf(map_author(9), (Q - 1) // 6)
    tame_multiplier = next((j for j in range(6) if powf(xi, j) == author_xi))
    if not tame_multiplier in [1, 5]:
        raise AssertionError('Verification failed: tame_multiplier in [1, 5]')
    author_path = Path(__file__).resolve().parents[3] / 'archive/evidence/odd_newest_20261007/author_expected.json'
    author = json.loads(author_path.read_text())['records']
    our = {(r['norm_mod5'], r['tame_index']): r for r in records}
    for r in author:
        target = our[r['norm_mod5'], tame_multiplier * r['tame_index'] % 6]
        if not [map_author(v) for v in r['characteristic_ascending']] == target['characteristic_ascending']:
            raise AssertionError("Verification failed: [map_author(v) for v in r['characteristic_ascending']] == target['characteristic_ascending']")
    result = {'status': 'all 24 matrices squarefree', 'field': 'F5[z]/(z^6+z^5+z^4+z^3+z^2+z+1), base-5 coefficient encoding', 'generator': GEN, 'seventh_root': w, 'sixth_root': xi, 'seven_dimensions': dimensions, 'actual_modes_checked': len(coeff), 'unit_upper_modes': len(actual_upper), 'author_polynomial_matches': len(author), 'author_field_root_image': alpha, 'author_tame_multiplier': tame_multiplier, 'characteristic_algorithm': 'division-free permutation-subset DP, independently checked by Cayley-Hamilton', 'records': records, 'elapsed_seconds': time.monotonic() - START}
    (output_dir / (Path(__file__).stem + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}, indent=2))
if __name__ == '__main__':
    main()
