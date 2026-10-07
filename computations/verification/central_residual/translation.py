def main():
    """Independent bounded algebra audit; no imports from candidate or BGS.
    Exact rational complex arithmetic, no floating tolerance or asymptotic simulation.
    Only writes the requested JSON report. --inject-failure is a fail-closed test.
    """
    from fractions import Fraction as F
    from collections import defaultdict, Counter
    from itertools import product
    from dataclasses import dataclass
    import json, math, sys, time

    @dataclass(frozen=True)
    class Q:
        re: F = F(0)
        im: F = F(0)

        @staticmethod
        def co(x):
            return x if isinstance(x, Q) else Q(F(x))

        def __add__(a, b):
            b = Q.co(b)
            return Q(a.re + b.re, a.im + b.im)
        __radd__ = __add__

        def __neg__(a):
            return Q(-a.re, -a.im)

        def __sub__(a, b):
            return a + -Q.co(b)

        def __rsub__(a, b):
            return Q.co(b) + -a

        def __mul__(a, b):
            b = Q.co(b)
            return Q(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re)
        __rmul__ = __mul__

        def __truediv__(a, b):
            b = Q.co(b)
            n = b.re * b.re + b.im * b.im
            c = a * b.conj()
            return Q(c.re / n, c.im / n)

        def conj(a):
            return Q(a.re, -a.im)

        def norm2(a):
            return a.re * a.re + a.im * a.im

        def text(a):
            return {'real': str(a.re), 'imag': str(a.im)}
    Z = Q()
    ONE = Q(F(1))
    counts = Counter()

    def need(ok, label):
        if not ok:
            raise RuntimeError(label)
        counts[label] += 1

    def polyadd(a, b):
        d = dict(a)
        for k, v in b.items():
            d[k] = d.get(k, Z) + v
        return {k: v for k, v in d.items() if v != Z}

    def polymul(a, b):
        d = {}
        for k, v in a.items():
            for l, w in b.items():
                t = tuple((x + y for x, y in zip(k, l)))
                d[t] = d.get(t, Z) + v * w
        return {k: v for k, v in d.items() if v != Z}

    def scale(a, v):
        return {k: x * v for k, x in a.items() if x * v != Z}
    c7 = {(7, 0): Q(F(1, 2)), (-7, 0): Q(F(1, 2))}
    c1 = {(1, 0): Q(F(1, 2)), (-1, 0): Q(F(1, 2))}
    s1 = {(1, 0): Q(0, F(-1, 2)), (-1, 0): Q(0, F(1, 2))}
    r = polymul(polyadd({(0, 0): ONE}, scale(c7, -1)), polyadd({(0, 0): ONE}, c1))
    rhalf = {k: v * (1 if k[0] % 2 == 0 else -1) for k, v in r.items()}
    pmom = {(0, 1): Q(F(-3, 10), F(-2, 5)), (0, -1): Q(F(-3, 10), F(2, 5))}
    g = polyadd(polyadd(c7, scale(r, F(1, 10))), polyadd(scale(polymul(r, s1), F(1, 100)), scale(polymul(rhalf, pmom), F(1, 100))))
    g = polyadd(g, {(0, 0): Q(F(-1, 10))})
    need((0, 0) not in g and '--inject-failure' not in sys.argv, 'centered_symbol')
    need(g[0, 1] == Q(F(-3, 1000), F(-4, 1000)), 'witness_g01')
    need(g[1, 1] == Q(F(3, 2000), F(4, 2000)), 'witness_g11')
    need(all((g.get((-k, -l), Z) == v.conj() for (k, l), v in g.items())), 'real_symbol')
    weighted = sum(((abs(v.re) + abs(v.im)) * (k * k + l * l) for (k, l), v in g.items()))
    need(weighted == F(51451, 1000), 'weighted_symbol_bound')
    need(sum((abs(v.re) + abs(v.im) for v in g.values())) < 52, 'coarse_symbol_l1_bound')
    need(all((k * k + l * l < 100 and abs(l) <= 1 for k, l in g)), 'symbol_support')
    need(52 * 63 ** 4 < 10 ** 9, 'fourth_derivative_majorant')
    witness = []
    for k, target in [(0, F(3, 1600)), (1, F(1, 3200))]:
        f = (F(k) - F(3, 4), F(1, 4))
        z = g[k, 1] * (-2 * f[0] * f[1])
        need(z.norm2() == target * target, 'HJ_mixed_coefficient_over_pi')
        witness.append({'frequency': [str(v) for v in f], 'coefficient_over_pi': z.text(), 'modulus_over_pi': str(target)})
    X = {(1, 0, 0): ONE}
    Y = {(0, 1, 0): ONE}
    U = {(0, 0, 1): ONE}
    C = lambda r: {(0, 0, 0): Q(F(r))}
    add = polyadd
    mul = polymul
    S = lambda xx, yy, r: scale(add(add(scale(mul(xx, xx), 3), scale(mul(xx, add(yy, C(r))), -2)), scale(mul(add(yy, C(r)), add(yy, C(r))), 3)), F(-1, 8))

    def diff(p, axis):
        d = {}
        for k, v in p.items():
            if k[axis]:
                t = list(k)
                t[axis] -= 1
                d[tuple(t)] = v * k[axis]
        return d
    for r0 in range(-4, 8):
        need(S(X, Y, r0) == S(X, add(Y, C(r0)), 0), 'S_branch_y_shift')
        need(add(S(X, Y, r0 + 4), scale(S(X, Y, r0), -1)) == add(add(X, scale(Y, -3)), C(-3 * r0 - 6)), 'branch_plus4_gluing')
        need(add(S(add(X, C(1)), Y, r0), scale(S(X, Y, r0 - 3), -1)) == add(scale(Y, -2), C(-2 * r0 + 3)), 'x_plus1_gluing')
        need(S(X, add(Y, C(1)), r0) == S(X, Y, r0 + 1), 'y_plus1_gluing')
        need(add(S(add(X, C(4)), Y, r0), scale(S(X, Y, r0), -1)) == add(add(scale(X, -3), Y), C(r0 - 6)), 'x_period4_correction')
    for r0, s0 in product(range(4), repeat=2):
        p = add(S(X, Y, r0), scale(S(add(X, U), add(Y, U), s0), -1))
        need(diff(diff(p, 0), 1) == {}, 'initial_translation_phase_separable')

    def z8(exponent):
        k = exponent % 8
        return (k % 4, 1 if k < 4 else -1)

    def residue_sum(terms):
        out = [0] * 4
        for coefficient, e in terms:
            k, sgn = z8(e)
            out[k] += coefficient * sgn
        return out
    for n in [1, 3, 5, 7]:
        for t in range(8):
            need(residue_sum([(1, -3 * n * r0 * r0 + 2 * t * r0) for r0 in range(4)] + [(-2, -3 * n + 3 * n * t * t)]) == [0] * 4, 'all_Gauss_residue_cases')
    for n in range(3, 42, 2):
        h = pow(2, -1, n)
        h8 = pow(8, -1, n)
        need(((8 * h8 - 1) // n + n) % 8 == 0, 'odd_modular_inverse8')
        for (k0, l0), coefficient in g.items():
            for j0 in [-n, -1, 0, n - 1, n, 2 * n - 1]:
                difference = F(k0 * l0, 2) + F(k0 * (j0 + h * l0), n) - F(k0 * j0, n) - F(k0 * l0, 2 * n)
                need(difference.denominator == 1, 'raw_ordinary_halfshift_dictionary')
        for j, k, c in product([-n, -1, 0, 1, n - 1, n, 2 * n - 1], repeat=3):
            lhs = h8 * (3 * (j + c) ** 2 - 2 * (j + c) * (k + c) + 3 * (k + c) ** 2 - (3 * j * j - 2 * j * k + 3 * k * k))
            need((lhs - h * c * (j + k + c)) % n == 0, 'lifted_cat_product_congruence')
        for c in range(1, n):
            need((h * c * 2 - c) % n == 0, 'cat_square_character')
            need(c % n != 0 and c * n % n == 0, 'cat_geometric_sum_conditions')
    endpoint = []
    for u in [F(0), F(1)]:
        pairs = []
        for r0, s0 in product(range(4), repeat=2):
            a = F(s0 - r0, 4) - u / 2
            b = F(s0 - r0, 4) + u / 2
            if a.denominator == b.denominator == 1:
                pairs.append([r0, s0])
        endpoint.append({'u': str(u), 'simultaneously_zero_brackets': pairs})
        need(len(pairs) == 4, 'endpoint_degeneracies_retained')
    for den in range(2, 81):
        for num in range(1, den):
            u = F(num, den)
            for r0, s0 in product(range(4), repeat=2):
                a = F(s0 - r0, 4) - u / 2
                b = F(s0 - r0, 4) + u / 2
                need(b - a == u and (not (a.denominator == 1 and b.denominator == 1)), 'bounded_two_character_controls')
    tau = F(1, 10 ** 80)
    need(F(10 ** 50, 2) * tau * tau < F(3, 6400) * tau, 'literal_time_Fourier_margin_pi_lower3')
    need(2 * 10 ** 9 * tau + 10 ** 50 * tau * tau < F(1, 4), 'literal_time_alias_upper_bound')

    def ident(n):
        return [[ONE if i == j else Z for j in range(n)] for i in range(n)]

    def mm(a, b):
        return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Z) for j in range(len(b[0]))] for i in range(len(a))]

    def star(a):
        return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]

    def tr(a):
        return sum((a[i][i] for i in range(len(a))), Z)

    def house(v):
        n = len(v)
        d = sum((a.norm2() for a in v), F(0))
        return [[(ONE if i == j else Z) - 2 * v[i] * v[j].conj() / d for j in range(n)] for i in range(n)]

    def unitary(n):
        h1 = house([Q(F(j + 1), F(j % 2)) for j in range(n)])
        h2 = house([Q(F(2 - j), F(j + 1)) for j in range(n)])
        d = ident(n)
        for j in range(n):
            d[j][j] = Q(F(3, 5), F(4, 5)) if j % 2 else Q(F(5, 13), F(-12, 13))
        return mm(mm(h1, d), h2)

    def amp(u, w):
        a = ONE
        for j in range(len(w)):
            a = a * u[w[j]][w[(j + 1) % len(w)]]
        return a
    for n, maxm in [(3, 5), (5, 4), (7, 3)]:
        a = unitary(n)
        need(mm(star(a), a) == ident(n), 'exact_complex_unitarity')
        for c in range(n):
            b = [[a[i][j] * a[(i + c) % n][(j + c) % n].conj() for j in range(n)] for i in range(n)]
            for j in range(n):
                e = [[ONE if (i, k) == (j, (j + c) % n) else Z for k in range(n)] for i in range(n)]
                ae = mm(mm(a, e), star(a))
                need([ae[i][(i + c) % n] for i in range(n)] == [b[i][j] for i in range(n)], 'ordinary_HS_compression_entries')
            power = ident(n)
            for m in range(1, maxm + 1):
                power = mm(power, b)
                total = Z
                for w in product(range(n), repeat=m):
                    wp = tuple(((x + c) % n for x in w))
                    total = total + amp(a, w) * amp(a, wp).conj()
                need(total == tr(power), 'exact_rooted_trace_translation_identity')
        for m in range(1, min(maxm, 3) + 1):
            ws = list(product(range(n), repeat=m))
            aw = {w: amp(a, w) for w in ws}
            grouped = defaultdict(lambda: Z)
            for w in ws:
                grouped[tuple((w.count(j) for j in range(n)))] += aw[w]
            total = sum(aw.values(), Z).norm2()
            balanced = sum((a0.norm2() for a0 in grouped.values()), F(0))
            off = Z
            for w, v in product(ws, repeat=2):
                if sorted(w) != sorted(v):
                    off += aw[w] * aw[v].conj()
            need(off == Q(total - balanced), 'exact_offcharge_character_identity')

    def comps(m, n):
        if n == 1:
            yield (m,)
            return
        for k in range(m + 1):
            for tail in comps(m - k, n - 1):
                yield ((k,) + tail)
    balanced_count = 0
    for n in [3, 5, 9]:
        for m in range(0, 11):
            for occ in comps(m, n):
                for c in range(1, n):
                    d = n // math.gcd(c, n)
                    same = all((occ[j] == occ[(j + c) % n] for j in range(n)))
                    need(not same or m % d == 0, 'occupation_order_divisibility')
                    if d > m and m > 0:
                        need(not same, 'occupation_order_greater_m_offcharge')
                    balanced_count += same
    for n in [3, 5, 9]:
        for m in range(1, 5):
            for w in product(range(n), repeat=m):
                images = {tuple(((j + c) % n for j in w)) for c in range(n)}
                need(len(images) == n, 'rooted_translation_once_counting')
    report = {'status': 'passed', 'arithmetic': 'exact integer and Fraction-based Gaussian rationals; sparse polynomial convolution', 'asymptotic_claim': 'not numerically tested; analytic proof audited separately', 'counts': dict(counts), 'Fourier_witnesses': witness, 'weighted_symbol_sum': str(weighted), 'boundary_negative_controls': endpoint, 'balanced_occupation_vectors_retained': balanced_count, 'bounds': {'all_Gauss_mod8_cases': 32, 'cat_odd_N_max': 41, 'rational_denominator_max': 80, 'generic_unitary_N_m': [[3, 5], [5, 4], [7, 3]], 'occupation_N': [3, 5, 9], 'occupation_mass_max': 10, 'rooted_once_counting_N': [3, 5, 9], 'rooted_once_counting_m_max': 4}, 'nonclaims': ['No fixed-tau finite-N numerical norm simulation', 'No boundary-layer estimate', 'No higher-factorial or full-defect bound']}
    if '--output' in sys.argv:
        path = sys.argv[sys.argv.index('--output') + 1]
        with open(path, 'w') as f:
            json.dump(report, f, indent=2)
            f.write('\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
