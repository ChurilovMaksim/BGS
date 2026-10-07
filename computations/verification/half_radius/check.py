import sys

def main():
    """Independent bounded exact controls, authored for the half-radius review.
    No imports of author checks. Enumeration visits precisely the physical Hamming ball,
    not all word pairs; cyclotomic reduction, integer support projectors and Laurent
    coefficients provide separate exact representations. See contract.json for scope.
    """
    from collections import Counter, defaultdict
    from fractions import Fraction
    from itertools import product, combinations, combinations_with_replacement
    from math import comb, factorial, gcd
    from pathlib import Path
    import json, time
    import sympy
    T0 = time.monotonic()

    def cyclo_remainder(c, n):
        z = sympy.Symbol('z')
        phi = list(reversed([int(a) for a in sympy.Poly(sympy.cyclotomic_poly(n, z), z).all_coeffs()]))
        a = list(c)
        deg = len(phi) - 1
        for j in range(len(a) - 1, deg - 1, -1):
            v = a[j]
            if v:
                for k, p in enumerate(phi):
                    a[j - deg + k] -= v * p
        return a[:deg]

    def rational_character(c, n, den):
        rem = cyclo_remainder(c, n)
        if not all((v == 0 for v in rem[1:])):
            raise AssertionError((n, rem))
        return Fraction(rem[0], den)

    def literal_words(N, m, kind, n=None):
        """Trace R F C computed in the physical |x><y| basis.
        Set C e_i=e_(i-1) on slots so the closed path factor is U[x_i,x_(i+1)].
        Masks are evaluated on the basis word, which is invariant under slot cycling.
        """
        mod = N if kind == 'fourier' else n
        labels = list(product(range(n), repeat=2)) if kind == 'symplectic' else list(range(N))
        if kind == 'fourier':
            edge = lambda a, b: a * b % N
        else:
            edge = lambda a, b: (labels[a][0] * labels[b][1] - labels[a][1] * labels[b][0]) % n
        raw = [0] * mod
        balanced = [0] * mod
        examined = 0
        r = m // 2
        alternatives = [tuple((v for v in range(N) if v != u)) for u in range(N)]
        for x in product(range(N), repeat=m):
            nx = Counter(x)
            px = sum((edge(x[i], x[(i + 1) % m]) for i in range(m))) % mod
            for s in range(r + 1):
                for slots in combinations(range(m), s):
                    for repl in product(*(alternatives[x[i]] for i in slots)):
                        y = list(x)
                        for i, j in zip(slots, repl):
                            y[i] = j
                        py = sum((edge(y[i], y[(i + 1) % m]) for i in range(m))) % mod
                        phase = (px - py) % mod
                        raw[phase] += 1
                        examined += 1
                        if nx == Counter(y):
                            balanced[phase] += 1
        if not examined == N ** m * sum((comb(m, s) * (N - 1) ** s for s in range(r + 1))):
            raise AssertionError('Exact control failed')
        rt = rational_character(raw, mod, N ** m)
        bt = rational_character(balanced, mod, N ** m)
        ot = rt - bt
        if not rt == 2 * N - 1:
            raise AssertionError((kind, N, m, rt))
        if kind == 'fourier':
            if not ot >= Fraction(2 * (N - 1) ** 2, N):
                raise AssertionError('Exact control failed')
            if m == 4:
                if not ot == Fraction(2 * (N - 1) ** 2, N):
                    raise AssertionError('Exact control failed')
        elif not (m == 4 and ot == 2 * (N - 1) and (bt == 1)):
            raise AssertionError('Exact control failed')
        return {'kind': kind, 'N': N, 'm': m, 'r': r, 'examined_hamming_ball_pairs': examined, 'full_pair_universe': N ** (2 * m), 'raw_full_trace': str(rt), 'balanced_full_trace': str(bt), 'offcharge_full_trace': str(ot), 'raw_phase_counts': raw, 'balanced_phase_counts': balanced}

    def binary_patterns():
        rows = []
        for m in range(2, 17):
            eligible = 0
            survivors = []
            for a in product((0, 1), repeat=m):
                if sum(a) > m // 2:
                    continue
                eligible += 1
                if not any((a[i] == a[(i + 1) % m] == 0 for i in range(m))):
                    survivors.append(''.join(map(str, a)))
            if not survivors == (['01' * (m // 2), '10' * (m // 2)] if m % 2 == 0 else []):
                raise AssertionError('Exact control failed')
            rows.append({'m': m, 'patterns_tested': eligible, 'no_pp_survivors': survivors})
        return rows

    def full_support_trace():
        """N=2,m=4. Integer 2-scaled scalar/V local projectors and adjoint F2.
        Full sums over both physical input/output indices; no support reduction used.
        Trace R Q_S F A^tensor computed before grouping supports.
        """
        N = 2
        m = 4
        local = list(product(range(N), repeat=2))
        words = list(product(range(4), repeat=m))
        scalar = [[int(a == b and c == d) for c, d in local] for a, b in local]
        traceless = [[2 * int(i == j) - scalar[i][j] for j in range(4)] for i in range(4)]
        adj = [[(-1) ** (a * c + b * d) for c, d in local] for a, b in local]
        raw = [0] * (1 << m)
        bal = [0] * (1 << m)
        for v in words:
            xy = [local[i] for i in v]
            if sum((a != b for a, b in xy)) > 2:
                continue
            isbal = Counter((a for a, b in xy)) == Counter((b for a, b in xy))
            for u in words:
                ru = u[-1:] + u[:-1]
                a = 1
                for i in range(m):
                    a *= adj[v[i]][u[i]]
                for mask in range(1 << m):
                    coeff = a
                    for i in range(m):
                        coeff *= (traceless if mask >> i & 1 else scalar)[ru[i]][v[i]]
                    raw[mask] += coeff
                    if isbal:
                        bal[mask] += coeff
        rows = []
        for mask in range(1 << m):
            x = Fraction(raw[mask], 4 ** m)
            y = Fraction(bal[mask], 4 ** m)
            expected = (Fraction(1), Fraction(1)) if mask == 0 else (Fraction(2), Fraction(1)) if mask == 15 else (Fraction(0), Fraction(0))
            if not (x, y) == expected:
                raise AssertionError((mask, x, y))
            rows.append({'support': format(mask, '04b'), 'raw': str(x), 'balanced': str(y), 'offcharge': str(x - y)})
        return {'N': 2, 'm': 4, 'physical_double_indices': 4 ** (2 * m), 'support_masks': 16, 'rows': rows}

    def group(n, dim):
        return list(product(range(n), repeat=dim))

    def sub(u, k, n):
        return tuple(((a - b) % n for a, b in zip(u, k)))

    def edge_vector(u, k, labels, n):
        v = [0] * len(labels)
        index = {x: i for i, x in enumerate(labels)}
        v[index[u]] += 1
        v[index[sub(u, k, n)]] -= 1
        return tuple(v)

    def ordinary_moment(labels, k, n, q):
        N = len(labels)
        edges = [edge_vector(u, k, labels, n) for u in labels]
        survive = 0
        multisets = 0
        for xs in combinations_with_replacement(range(N), q):
            multisets += 1
            v = [0] * N
            for x in xs:
                for j, a in enumerate(edges[x]):
                    v[j] += a
            if not any(v):
                c = factorial(q)
                for a in Counter(xs).values():
                    c //= factorial(a)
                survive += c
        return (Fraction(survive, N ** q), multisets)

    def reflected_moment(labels, k, n, q):
        if not q % 2 == 0:
            raise AssertionError('Exact control failed')
        N = len(labels)
        s = q // 2
        edges = [edge_vector(u, k, labels, n) for u in labels]
        pol = Counter()
        for xs in product(range(N), repeat=s):
            v = tuple((sum((edges[x][j] for x in xs)) for j in range(N)))
            pol[v] += 1
        return Fraction(sum((c * c for c in pol.values())), N ** q)

    def cycle_formula(N, L, q):
        if q % L:
            return Fraction(0)
        h = N // L
        degree = q // L
        coeff = [Fraction(1)] + [Fraction(0)] * degree
        one = [Fraction(1, factorial(a) ** L) for a in range(degree + 1)]
        for _ in range(h):
            coeff = [sum((coeff[j] * one[d - j] for j in range(d + 1))) for d in range(degree + 1)]
        return factorial(q) * coeff[degree] / N ** q

    def phase_moments():
        f = []
        s = []
        for n in range(2, 8):
            labels = group(n, 1)
            for k in labels[1:]:
                for q in (2, 4, 6):
                    v = reflected_moment(labels, k, n, q)
                    if not 0 <= v <= Fraction(1, n):
                        raise AssertionError('Exact control failed')
                    if q == 2:
                        if not v == Fraction(1, n):
                            raise AssertionError('Exact control failed')
                    f.append({'N': n, 'k': k[0], 'q': q, 'E_abs_c_pow_q': str(v)})
        for n, ks, qs in [(3, [(1, 0)], (2, 3, 4, 6)), (5, [(1, 0)], (2, 3)), (9, [(3, 0), (1, 0)], (2, 3))]:
            labels = group(n, 2)
            N = n * n
            for k in ks:
                L = 1
                for v in k:
                    ell = n // gcd(v, n)
                    L = L * ell // gcd(L, ell)
                for q in qs:
                    v, count = ordinary_moment(labels, k, n, q)
                    expected = cycle_formula(N, L, q)
                    if not (v == expected and 0 <= v <= Fraction(1, N)):
                        raise AssertionError((n, k, q, v, expected))
                    if q == 2:
                        if not v == 0:
                            raise AssertionError('Exact control failed')
                    s.append({'n': n, 'N': N, 'k': k, 'order': L, 'q': q, 'E_a_pow_q': str(v), 'multisets_checked': count})
        return {'fourier_reflected': f, 'symplectic_unreflected': s}

    def symplectic_characters():
        rows = []
        for n in (3, 5, 9, 15):
            G = group(n, 2)
            N = n * n
            om = lambda x, y: (x[0] * y[1] - x[1] * y[0]) % n
            checks = 0
            triple_checks = 0
            if n == 3:
                for x in G:
                    for y in G:
                        for z in G:
                            if not (om(x, y) + om(y, z) - om(sub(x, z, n), y)) % n == 0:
                                raise AssertionError('Exact control failed')
                            triple_checks += 1
            for multiplier in (1, 2):
                for d in G:
                    c = [0] * n
                    for y in G:
                        c[multiplier * om(d, y) % n] += 1
                    if not rational_character(c, n, N) == int(d == (0, 0)):
                        raise AssertionError('Exact control failed')
                    checks += 1
            for x in G:
                for y in G:
                    if not (om(x, y) + om(y, x)) % n == 0:
                        raise AssertionError('Exact control failed')
            absolute_second = 0
            ordinary_second = 0
            for k in G[1:]:
                if n > 9:
                    break
                ac = oc = 0
                for u in G:
                    for v in G:
                        ac += Counter((u, sub(v, k, n))) == Counter((sub(u, k, n), v))
                        oc += Counter((u, v)) == Counter((sub(u, k, n), sub(v, k, n)))
                if not (ac == N and oc == 0):
                    raise AssertionError('Exact control failed')
                absolute_second += ac
                ordinary_second += oc
            rows.append({'n': n, 'N': N, 'character_difference_checks': checks, 'phase_antisymmetry_pairs': N * N, 'bilinear_triple_checks': triple_checks, 'absolute_second_survivors_all_k': absolute_second if n <= 9 else None, 'ordinary_second_survivors_all_k': ordinary_second if n <= 9 else None, 'frequency_multipliers': [1, 2]})
        G = group(2, 2)
        d = (1, 0)
        c = [0, 0]
        for y in G:
            c[2 * (d[0] * y[1] - d[1] * y[0]) % 2] += 1
        if not rational_character(c, 2, 4) == 1:
            raise AssertionError('Exact control failed')
        return {'odd_moduli': rows, 'even_n2_doubled_character_nonzero_for_nonzero_difference': True}
    results = {'arithmetic': 'exact integers, Fraction rationals, locally implemented cyclotomic remainder; no floating complex values', 'binary_patterns': binary_patterns()}
    print('Binary positional masks passed', flush=True)
    results['support_grading'] = full_support_trace()
    print('Full scalar/traceless support trace passed', flush=True)
    results['physical_word_traces'] = [literal_words(N, m, 'fourier') for N, m in [(2, 4), (2, 8), (3, 4), (4, 4), (5, 4)]]
    print('Fourier physical words passed', flush=True)
    results['physical_word_traces'].append(literal_words(9, 4, 'symplectic', 3))
    print('Symplectic physical words passed', flush=True)
    results['phase_moments'] = phase_moments()
    print('Ordinary/reflected phase moments passed', flush=True)
    results['symplectic_characters'] = symplectic_characters()
    print('Composite-modulus and reversed-kernel controls passed', flush=True)
    results['elapsed_seconds'] = time.monotonic() - T0
    results['nonclaims'] = ['Finite controls do not establish universal identities independently of the mathematical proof.', 'No actual frozen quantizer or BGS counterexample.', 'No verification of the separate fixed-fraction theorem or inherited actual parametrix.']
    Path(sys.argv[sys.argv.index('--output') + 1]).write_text(json.dumps(results, indent=2) + '\n')
    print('All independent exact controls passed', flush=True)

if __name__ == "__main__":
    main()
