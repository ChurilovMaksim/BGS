def main():
    """Independent exact Gaussian-integer scaled-unitary controls.

    No author verifier is imported. Arithmetic is Z[i] with explicit positive
    denominators. These finite unitary controls do not approximate actual U_N.
    """
    from collections import Counter, defaultdict
    from itertools import product
    from math import comb, gcd, prod
    from pathlib import Path
    import json, sys
    Z = (0, 0)
    O = (1, 0)

    def add(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def neg(a):
        return (-a[0], -a[1])

    def sub(a, b):
        return add(a, neg(b))

    def mul(a, b):
        return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

    def conj(a):
        return (a[0], -a[1])

    def scale(a, s):
        return (a[0] * s, a[1] * s)

    def norm2(a):
        return a[0] * a[0] + a[1] * a[1]

    def sm(xs):
        r = Z
        for x in xs:
            r = add(r, x)
        return r

    def eye(n, s=1):
        return [[(s if j == k else 0, 0) for k in range(n)] for j in range(n)]

    def adj(A):
        return [[conj(A[k][j]) for k in range(len(A))] for j in range(len(A[0]))]

    def mm(A, B):
        return [[sm((mul(A[i][k], B[k][j]) for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]

    def ms(A, s):
        return [[scale(a, s) for a in row] for row in A]

    def ma(A, B):
        return [[add(a, b) for a, b in zip(ar, br)] for ar, br in zip(A, B)]

    def mp(A, e):
        out = eye(len(A))
        for _ in range(e):
            out = mm(out, A)
        return out

    def tr(A):
        return sm((A[j][j] for j in range(len(A))))

    def pt(As, n):
        out = eye(n)
        for A in As:
            out = mm(out, A)
        return tr(out)

    def check(ok, what):
        if not ok:
            raise AssertionError(what)
    if '--inject-failure' in sys.argv:
        check(False, 'deliberately injected fail-closed control')

    def hh(v):
        q = sum((norm2(z) for z in v))
        return ([[sub((q if j == k else 0, 0), scale(mul(v[j], conj(v[k])), 2)) for k in range(len(v))] for j in range(len(v))], q)

    def unitary(n):
        v = [(j + 1, (-1) ** j * (j % 3)) for j in range(n)]
        w = [(n - j, 1 + j % 2) for j in range(n)]
        A, q = hh(v)
        B, r = hh(w)
        phases = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        AP = [[mul(A[j][k], phases[k % 4]) for k in range(n)] for j in range(n)]
        return (mm(AP, B), q * r, {'v': v, 'w': w, 'column_phases': phases, 'denominator': q * r})

    def sw(c):
        return sum((c[j] != c[(j + 1) % len(c)] for j in range(len(c))))

    def run_data(c):
        m = len(c)
        start = next((j for j in range(m) if c[j - 1] != c[j]))
        cyc = c[start:] + c[:start]
        runs = []
        for q in cyc:
            if not runs or runs[-1][0] != q:
                runs.append([q, 1])
            else:
                runs[-1][1] += 1
        return runs

    def encoded(z, den):
        from fractions import Fraction
        return {'real': str(Fraction(z[0], den)), 'imag': str(Fraction(z[1], den))}
    out = {'status': 'passed', 'arithmetic': 'exact Gaussian integers with explicit common denominators', 'cases': [], 'unitaries': [], 'negative_controls': []}
    total_pairs = total_words = 0
    zero_long = zero_short = complex_traces = wrong_conjugations = 0
    for n, mmax in [(3, 5), (5, 3)]:
        U, d, recipe = unitary(n)
        check(mm(U, adj(U)) == eye(n, d * d), 'U U*=I')
        check(mm(adj(U), U) == eye(n, d * d), 'U* U=I')
        check(all((a != Z for row in U for a in row)), 'dense control')
        out['unitaries'].append({'N': n, 'recipe': recipe, 'numerator': U})
        idx = [(c, j) for c in range(n) for j in range(n)]
        T = [[Z for _ in idx] for _ in idx]
        for col, (dc, k) in enumerate(idx):
            E = [[Z for _ in range(n)] for _ in range(n)]
            E[k][(k + dc) % n] = O
            UEU = mm(mm(U, E), adj(U))
            for row, (c, j) in enumerate(idx):
                T[row][col] = UEU[j][(j + c) % n]
        check(mm(adj(T), T) == eye(n * n, d ** 4), 'Ad(U) unitary on ordinary HS basis')
        B = {(c, dc): [[mul(U[j][k], conj(U[(j + c) % n][(k + dc) % n])) for k in range(n)] for j in range(n)] for c in range(n) for dc in range(n)}
        for c, dc in B:
            check(B[c, dc] == [[T[c * n + j][dc * n + k] for k in range(n)] for j in range(n)], 'compression indexing and conjugation')
        for dc in range(n):
            grams = [mm(adj(B[c, dc]), B[c, dc]) for c in range(n)]
            total = [[Z for _ in range(n)] for _ in range(n)]
            for G in grams:
                total = ma(total, G)
            check(total == eye(n, d ** 4), 'compression contraction Gram sum certificate')
        for c in range(1, n):
            check(all((sm(row) == Z for row in B[c, 0])), 'B_c0 kills right constant')
            check(all((sm((B[0, c][j][k] for j in range(n))) == Z for k in range(n))), 'B_0c kills left constant')
        check(all((sm(row) == (d * d, 0) for row in B[0, 0])), 'P row sum one')
        check(all((sm((B[0, 0][j][k] for j in range(n))) == (d * d, 0) for k in range(n))), 'P column sum one')
        Tp = [[sub(scale(T[i][j], n), (d * d if i < n and j < n else 0, 0)) for j in range(n * n)] for i in range(n * n)]
        expected = [[sub((n * n * d ** 4 if i == j else 0, 0), (n * d ** 4 if i < n and j < n else 0, 0)) for j in range(n * n)] for i in range(n * n)]
        check(mm(adj(Tp), Tp) == expected, 'global identity projector reduction')
        Bt = {key: ms(A, n) for key, A in B.items()}
        Bt[0, 0] = [[sub(z, (d * d, 0)) for z in row] for row in Bt[0, 0]]
        for m in range(1, mmax + 1):
            words = list(product(range(n), repeat=m))
            amps = {}
            for x in words:
                a = O
                for j in range(m):
                    a = mul(a, U[x[j]][x[(j + 1) % m]])
                amps[x] = a
            occup = {x: tuple((x.count(j) for j in range(n))) for x in words}
            direct = defaultdict(lambda: Z)
            hist = Counter()
            pairs_by_mask = Counter()
            direct_low = defaultdict(lambda: Z)
            phase_balanced = Z
            explicit_balanced = Z
            for x in words:
                for y in words:
                    c = tuple(((y[j] - x[j]) % n for j in range(m)))
                    term = mul(amps[x], conj(amps[y]))
                    direct[c] = add(direct[c], term)
                    balanced = occup[x] == occup[y]
                    chk = sum(c) % n
                    if chk:
                        check(not balanced, 'nonzero checksum implies occupation mismatch')
                    pairs_by_mask[('nonzero_checksum' if chk else 'zero_checksum') + ('_balanced' if balanced else '_offcharge')] += 1
                    if balanced:
                        explicit_balanced = add(explicit_balanced, term)
                    character_zero = all(((occup[x][j] - occup[y][j]) % (m + 1) == 0 for j in range(n)))
                    if character_zero:
                        phase_balanced = add(phase_balanced, term)
                    if chk:
                        for R in range(sw(c), m + 1):
                            direct_low[R] = add(direct_low[R], term)
                    total_pairs += 1
            check(phase_balanced == explicit_balanced, 'independent-coordinate character projector')
            checksum_low = defaultdict(lambda: Z)
            for c in words:
                matrices = [B[c[j], c[(j + 1) % m]] for j in range(m)]
                value = pt(matrices, n)
                check(value == direct[c], 'literal pair sum equals block trace')
                check(norm2(value) <= (n * d ** (2 * m)) ** 2, 'trace dimension factor N from contractions')
                if value[1]:
                    complex_traces += 1
                modified = pt([Bt[c[j], c[(j + 1) % m]] for j in range(m)], n)
                expected_difference = (n ** m * d ** (2 * m), 0) if all((q == 0 for q in c)) else Z
                check(sub(scale(value, n ** m), modified) == expected_difference, 'identity subtraction only changes all-zero word by one')
                r = sw(c)
                hist[r] += 1
                if r:
                    runs = run_data(c)
                    check(len(runs) == r, 'run count equals cyclic switch count')
                    check(sum((length - 1 for _, length in runs)) == m - r, 'exact internal step count')
                    runblocks = []
                    for k, (q, length) in enumerate(runs):
                        runblocks.extend([mp(Bt[q, q], length - 1), Bt[q, runs[(k + 1) % r][0]]])
                        if q == 0 and length >= 2:
                            zero_long += 1
                        if q == 0 and length == 1:
                            zero_short += 1
                    check(pt(runblocks, n) == modified, 'oriented cyclic run factorization including zero internal lengths')
                    for cut in range(m):
                        check(pt(matrices[cut:] + matrices[:cut], n) == value, 'cyclic cut invariance without multiplicity')
                if sum(c) % n:
                    for R in range(r, m + 1):
                        checksum_low[R] = add(checksum_low[R], value)
                total_words += 1
            check(hist[0] == n, 'r=0 exact count')
            for r in range(1, m + 1):
                exact = comb(m, r) * ((n - 1) ** r + (-1) ** r * (n - 1))
                check(hist[r] == exact, 'exact switch-word chromatic count')
                check(exact <= comb(m, r) * n ** r, 'author switch bound')
            check(hist[1] == 0, 'one switch impossible')
            check(direct_low == checksum_low, 'every low-switch threshold once counted')
            for c in range(1, n):
                check((m * c % n != 0) == (m % (n // gcd(c, n)) != 0), 'constant-translation overlap mask')
            for c in words[:min(10, len(words))]:
                wrong = pt([[[mul(U[j][k], U[(j + c[t]) % n][(k + c[(t + 1) % m]) % n]) for k in range(n)] for j in range(n)] for t in range(m)], n)
                wrong_conjugations += wrong != direct[c]
            out['cases'].append({'N': n, 'm': m, 'pairs': len(words) ** 2, 'difference_words': len(words), 'switch_histogram': dict(hist), 'mask_counts': dict(pairs_by_mask), 'safe_low_switch_sums': {str(R): encoded(checksum_low[R], d ** (2 * m)) for R in range(m + 1)}})
        if n == 3:
            c = (1, 2)
            examples = [((0, 1), (1, 0), 'balanced'), ((0, 0), (1, 2), 'offcharge')]
            records = []
            for x, y, label in examples:
                check(tuple(((y[j] - x[j]) % n for j in range(2))) == c, 'same zero-checksum word')
                a = mul(U[x[0]][x[1]], U[x[1]][x[0]])
                b = mul(U[y[0]][y[1]], U[y[1]][y[0]])
                term = mul(a, conj(b))
                check(term != Z, 'nonzero weighted checksum-zero witness')
                records.append({'x': x, 'y': y, 'classification': label, 'weight': encoded(term, d ** 4)})
            out['zero_checksum_same_fiber_examples'] = {'N': n, 'c': c, 'examples': records}
    count_coverage = []
    for n, mmax in [(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (9, 3)]:
        for m in range(1, mmax + 1):
            histogram = Counter((sw(c) for c in product(range(n), repeat=m)))
            check(histogram[0] == n, 'separate constant count')
            for r in range(1, m + 1):
                check(histogram[r] == comb(m, r) * ((n - 1) ** r + (-1) ** r * (n - 1)), 'separate exact switch enumeration')
            for c in range(1, n):
                check((m * c % n != 0) == (m % (n // gcd(c, n)) != 0), 'composite-order mask')
            count_coverage.append({'N': n, 'm': m, 'words': n ** m})
    ident_sum = 0
    for x in product(range(3), repeat=4):
        for y in product(range(3), repeat=4):
            c = tuple(((y[j] - x[j]) % 3 for j in range(4)))
            if sw(c) == 0 and sum(c) % 3:
                ident_sum += prod((int(x[j] == x[(j + 1) % 4]) for j in range(4))) * prod((int(y[j] == y[(j + 1) % 4]) for j in range(4)))
    check(ident_sum == 6, 'unitarity-only negative control computed literally')
    out['negative_controls'].append({'unitary': 'I_3', 'm': 4, 'nonzero_checksum_constant_family_sum': 6, 'meaning': 'Algebra alone cannot establish exponential decay; analytic power input is essential.'})
    check(complex_traces > 0 and wrong_conjugations > 0, 'complex control detects missing conjugation')
    check(zero_long > 0 and zero_short > 0, 'both zero-run boundary regimes exercised')
    out['coverage'] = {'pair_controls': total_pairs, 'full_difference_contractions': total_words, 'long_zero_charge_runs': zero_long, 'singleton_zero_charge_runs': zero_short, 'nonreal_full_contractions': complex_traces, 'detected_missing_conjugations': wrong_conjugations, 'separate_counting_cases': count_coverage}
    out['non_claims'] = ['No finite control approximates actual fixed-tau U_N.', 'No analytic diagonal power gap is established numerically.', 'No complete off-charge, plateau, or higher factorial bound follows.']
    dest = Path(sys.argv[sys.argv.index('--output') + 1])
    dest.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'status': out['status'], 'coverage': out['coverage']}, indent=2))

if __name__ == "__main__":
    main()
