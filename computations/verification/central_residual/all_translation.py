def main():
    """Independent exact controls for the all-translation extension.
    No candidate verifier or repository module is imported. Tests are algebraic;
    fixed-tau norm convergence and actual-area mixing are not simulated.
    """
    from fractions import Fraction as F
    from collections import Counter
    from itertools import product
    from dataclasses import dataclass
    import json, sys
    C = Counter()

    def need(ok, name):
        if not ok:
            raise RuntimeError(name)
        C[name] += 1
    need('--inject-failure' not in sys.argv, 'fail_closed_guard')

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

        def conj(a):
            return Q(a.re, -a.im)

        def norm2(a):
            return a.re * a.re + a.im * a.im

        def __truediv__(a, b):
            b = Q.co(b)
            d = b.norm2()
            z = a * b.conj()
            return Q(z.re / d, z.im / d)
    Z = Q()
    O = Q(F(1))

    def eye(n):
        return [[O if i == j else Z for j in range(n)] for i in range(n)]

    def mm(a, b):
        return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Z) for j in range(len(b[0]))] for i in range(len(a))]

    def star(a):
        return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]

    def hs(a, b):
        return sum((a[i][j].conj() * b[i][j] for i in range(len(a)) for j in range(len(a))), Z) / len(a)

    def house(v):
        n = len(v)
        den = sum((a.norm2() for a in v), F(0))
        return [[(O if i == j else Z) - 2 * v[i] * v[j].conj() / den for j in range(n)] for i in range(n)]

    def unitary(n):
        a = house([Q(F(j + 1), F((j + 1) % 3)) for j in range(n)])
        d = eye(n)
        for j in range(n):
            d[j][j] = Q(F(3, 5), F(4, 5)) if j % 2 else Q(F(5, 13), F(-12, 13))
        return mm(a, d)

    def offset(a, c):
        n = len(a)
        return [[a[i][j] * a[(i + c) % n][(j + c) % n].conj() for j in range(n)] for i in range(n)]
    for n in range(3, 44, 2):
        inv2 = pow(2, -1, n)
        for c, b, j in product(range(-8, 9), range(-6, 7), range(n)):
            raw = F(b * c, 2) + F(b * (j + inv2 * c), n)
            ordinary = F(b * (2 * j + c), 2 * n)
            need((raw - ordinary).denominator == 1, 'raw_midpoint_all_parities')
    for n in range(3, 44, 2):
        inv8 = pow(8, -1, n)
        P = lambda x, y: 3 * x * x - 2 * x * y + 3 * y * y
        for a, b, j, k in product(range(-4, 5), range(-4, 5), [-1, 0, 1, n - 1, n], [-1, 0, 1, n - 1, n]):
            aa, bb = (3 * a + 4 * b, 2 * a + 3 * b)
            delta = -2 * inv8 * P(j, k - a) + 2 * b * k - b * a + 2 * inv8 * P(j + aa, k) - 2 * bb * j - bb * aa
            need(delta % (2 * n) == 0, 'raw_metaplectic_forward_G_intertwining')
    for n in [3, 5, 7]:
        a = unitary(n)
        need(mm(star(a), a) == eye(n), 'exact_unitarity')
        f = [Q(F(j - 2), F(j % 2)) for j in range(n)]
        g = [Q(F(2 * j + 1), F(1 - j)) for j in range(n)]
        for c in range(1, n):
            b = offset(a, c)
            bm = offset(a, -c)
            xf = [[f[j] if k == (j + c) % n else Z for k in range(n)] for j in range(n)]
            xg = [[g[j] if k == (j + c) % n else Z for k in range(n)] for j in range(n)]
            lhs = sum((f[i].conj() * b[i][j] * g[j] for i, j in product(range(n), repeat=2)), Z) / n
            rhs = hs(xf, mm(mm(a, xg), star(a)))
            need(lhs == rhs, 'normalized_HS_midpoint_sector_pairing')
            need(hs(xf, xf) == Q(sum((v.norm2() for v in f), F(0)) / n), 'sector_norm_normalization')
            p = q = eye(n)
            for ell in range(1, 5):
                p = mm(p, b)
                q = mm(q, bm)
                transformed = [[p[(i - c) % n][(j - c) % n].conj() for j in range(n)] for i in range(n)]
                need(q == transformed, 'negative_translation_power_conjugacy')
    for n in list(range(3, 102, 2)) + [129, 257, 509]:
        for ell in range(1, n // 2 + 1):
            total = F(1, n) + 2 * sum((min(F(1, n), F(1, ell * k)) for k in range(1, n)), F(0))
            H = sum((F(1, j) for j in range(1, ell + 1)), F(0))
            need(total <= F(1, n) + (4 + 4 * H) / ell, 'scaled_TTstar_harmonic_envelope')
            K = n // ell
            need(K >= F(n, 2 * ell), 'near_diagonal_cutoff_floor')
    cat = []
    for c in range(1, 100):
        branch_average = F(sum((-1 if c * r % 2 else 1 for r in range(4))), 4)
        need(branch_average == (0 if c % 2 else 1), 'cat_diagonal_branch_average')
        possible = [b for b in range(-150, 151) if 3 * c + 4 * b == c]
        need(possible == ([] if c % 2 else [-c // 2]), 'classical_cat_selected_momentum')
        if possible:
            b = possible[0]
            out = 2 * c + 3 * b
            need(out == c // 2 and 3 * c + 4 * out != c, 'classical_cat_square_zero')
        for n in [2 * c + 1, 4 * c + 1, 8 * c + 1]:
            h = pow(2, -1, n) * c % n
            need((2 * h - c) % n == 0, 'quantum_cat_rank_one_mode')
            if c % 2:
                need(h == (n + c) // 2, 'fixed_odd_c_escaping_alias')
            else:
                need(h == c // 2, 'fixed_even_c_low_mode')
        if c <= 4:
            cat.append({'c': c, 'classical_compression': 'zero' if c % 2 else 'rank one, norm one, square zero', 'quantum_cat_norm': 1, 'odd_c_high_frequency_alias': bool(c % 2)})
    for nx, ny in [(F(-3, 4), F(1, 4)), (F(1, 4), F(1, 4))]:
        need(nx + ny != 0 and abs(2 * (nx + ny)) == 1, 'scaled_nonzero_derivative_multiplier')

    def integrate_monomial_power(i, n, k):
        return (F(i + 1, n) ** (k + 1) - F(i, n) ** (k + 1)) / (k + 1)

    def hs_error(n):
        err = F(0)
        for i, j in product(range(n), repeat=2):
            x = F(i, n)
            y = F(j, n)
            const = x + 2 * y + x * y
            p = {(0, 0): const, (1, 0): F(-1), (0, 1): F(-2), (1, 1): F(-1)}
            for (a, b), v in p.items():
                for (c, d), w in p.items():
                    err += v * w * integrate_monomial_power(i, n, a + c) * integrate_monomial_power(j, n, b + d)
            kij = 1 + x + 2 * y + x * y
            need(n * (kij / n) == kij, 'embedded_matrix_kernel_factor_N')
        return err
    errors = []
    for n in [1, 3, 5, 9, 17]:
        er = hs_error(n)
        need(F(0) <= er <= F(25, n * n), 'piecewise_kernel_exact_HS_error')
        vals = [Q(F(j + 1), F(2 - j)) for j in range(n)]
        need(sum((v.norm2() * F(1, n) for v in vals), F(0)) == sum((v.norm2() for v in vals), F(0)) / n, 'J_isometry_normalization')
        errors.append({'N': n, 'exact_squared_HS_error': str(er)})
    for L in range(1, 65):
        for m in range(1, 257):
            q, r = divmod(m, L)
            need(0 <= r < L and m == q * L + r and (F(q) >= F(m, L) - 1), 'uniform_power_remainder_arithmetic')

    def comps(m, n):
        if n == 1:
            yield (m,)
            return
        for x in range(m + 1):
            for tail in comps(m - x, n - 1):
                yield ((x,) + tail)
    import math
    balanced = unbalanced_divisible = 0
    for n in [3, 5, 9]:
        for m in range(1, 10):
            for v in comps(m, n):
                for c in range(1, n):
                    d = n // math.gcd(c, n)
                    same = all((v[j] == v[(j + c) % n] for j in range(n)))
                    need(not same or m % d == 0, 'all_word_offcharge_mask')
                    if same:
                        balanced += 1
                    elif m % d == 0:
                        unbalanced_divisible += 1
            if m % n == 0:
                need(all((m % (n // math.gcd(c, n)) == 0 for c in range(1, n))), 'mask_empty_at_multiple_N')
    out = {'status': 'passed', 'arithmetic': 'exact integers, Fractions, Gaussian rational matrix arithmetic and exact polynomial integration', 'counts': dict(C), 'cat_escaping_alias_negative_controls': cat, 'piecewise_HS_errors': errors, 'balanced_cases_retained': balanced, 'unbalanced_cases_at_divisible_times_retained': unbalanced_divisible, 'scope': {'raw_odd_N_max': 43, 'midpoint_c_abs_max': 8, 'midpoint_b_abs_max': 6, 'rational_unitary_N': [3, 5, 7], 'negative_power_max': 4, 'Schur_N': 'all odd 3..101, plus129,257,509; every 1<=ell<=N/2', 'cat_c_max': 99, 'occupation_N': [3, 5, 9], 'occupation_mass_max': 9}, 'nonclaims': ['No fixed-tau operator norm is numerically approximated', 'No numerical computation certifies the Koopman limit or normalized-area mixing', 'No arbitrary products with changing offsets are controlled here']}
    if '--output' in sys.argv:
        with open(sys.argv[sys.argv.index('--output') + 1], 'w') as f:
            json.dump(out, f, indent=2)
            f.write('\n')
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
