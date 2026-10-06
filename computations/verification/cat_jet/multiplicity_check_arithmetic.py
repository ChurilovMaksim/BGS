"""Bounded exact reviewed arithmetic; writes only into caller-provided scratch root."""

def run(root, helpers=None):
    """Independent exact controls for the stated cat-multiplicity proof.
No source imports, eigensolvers, floating point, or external theorem calls.
Bounded tests supplement the uniform proof in REPORT.md.
"""
    from pathlib import Path
    from math import gcd
    from functools import reduce
    import hashlib
    import json
    import subprocess
    import sys
    import time
    ROOT = root
    S = (3, 4, 2, 3)
    I = (1, 0, 0, 1)

    def require(test, message):
        if not test:
            raise RuntimeError(message)

    def mul(a, b, m=None):
        c = (a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3], a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3])
        return tuple((x % m for x in c)) if m else c

    def power(a, k, m=None):
        b = I
        while k:
            if k & 1:
                b = mul(b, a, m)
            a = mul(a, a, m)
            k //= 2
        return b

    def sub_i(a):
        return (a[0] - 1, a[1], a[2], a[3] - 1)

    def det(a):
        return a[0] * a[3] - a[1] * a[2]

    def kernel_size(a, m):
        d1 = reduce(gcd, a)
        if d1 == 0:
            return m * m
        d2 = det(a) // d1
        return gcd(m, d1) * gcd(m, d2)

    def brute_kernel(a, m):
        return sum(((a[0] * x + a[1] * y) % m == 0 and (a[2] * x + a[3] * y) % m == 0 for x in range(m) for y in range(m)))

    def vp5(x):
        require(x != 0, 'vp5 zero input')
        v = 0
        while x % 5 == 0:
            x //= 5
            v += 1
        return v

    def phase(m, x, y):
        return -pow(8, -1, m) * (3 * x * x - 2 * x * y + 3 * y * y) % m

    def cyclo_add(a, b):
        return tuple((x + y for x, y in zip(a, b)))

    def cyclo_scale(a, k):
        return tuple((k * x for x in a))

    def cyclo_mul(a, b):
        c = [0] * 11
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i + j] += x * y
        for k in range(10, 5, -1):
            lead = c[k]
            for j in range(7):
                c[k - 6 + j] -= lead
        return tuple(c[:6])
    Z = (0,) * 6
    ONE = (1, 0, 0, 0, 0, 0)

    def zeta(k):
        k %= 7
        if k == 6:
            return (-1,) * 6
        return tuple((int(i == k) for i in range(6)))

    def matrix_mul(a, b):
        n = len(a)
        out = []
        for i in range(n):
            row = []
            for j in range(n):
                t = Z
                for k in range(n):
                    t = cyclo_add(t, cyclo_mul(a[i][k], b[k][j]))
                row.append(t)
            out.append(row)
        return out
    start = time.monotonic()
    s6 = sub_i(power(S, 6))
    h = tuple((x // 5 for x in s6))
    require(h == (3920, 5544, 2772, 3920), 'S6 lift')
    require(det(h) % 5 == 2, 'Leading matrix not invertible')
    base = []
    for k in range(1, 7):
        b = sub_i(power(S, k))
        base.append({'k': k, 'S_power_mod5': [x % 5 for x in power(S, k)], 'det_difference_mod5': det(b) % 5})
        require((power(S, k, 5) == I) == (k == 6), 'Incorrect order modulo 5')
        if k < 6:
            require(det(b) % 5 != 0, 'Nonreturn has nontrivial 5-kernel')
    require(power(S, 3, 7) == I, 'Order 7 return')
    require(det(sub_i(S)) % 7 and det(sub_i(power(S, 2))) % 7, 'Nonreturn 7-kernel')
    rows = []
    brute_cases = 0
    for e in range(1, 8):
        n = 5 ** e
        R = 6 * 5 ** (e - 1)
        N = 7 * n
        a = I
        total_n = total_N = 0
        lead_checks = 0
        for k in range(R):
            b = sub_i(a)
            kn = kernel_size(b, n)
            kN = kernel_size(b, N)
            expected = n * n if k == 0 else 5 ** (2 * (1 + vp5(k // 6))) if k % 6 == 0 else 1
            require(kn == expected, f'Prime trace at e={e}, k={k}')
            require(kN == kn * (49 if k % 3 == 0 else 1), f'Composite trace at e={e}, k={k}')
            if k and k % 6 == 0:
                q = 5 ** (1 + vp5(k // 6))
                require(all((x % q == 0 for x in b)), 'Not divisible at matrix valuation')
                require(det(tuple((x // q for x in b))) % 5 != 0, 'Leading matrix singular')
                lead_checks += 1
            if e <= 2:
                require(kn == brute_kernel(b, n), 'Prime Smith/kernel disagreement')
                require(kN == brute_kernel(b, N), 'Composite Smith/kernel disagreement')
                brute_cases += 2
            total_n += kn
            total_N += kN
            a = mul(a, S, N)
            if k + 1 < R:
                require(tuple((x % n for x in a)) != I, 'Early prime return')
        require(a == I, 'Missing full return')
        require(total_n == R * n, 'Prime Parseval sum')
        require(total_N == R * (49 * n - 32), 'Full Parseval sum')
        exceptional = [4, 5, 5] if e % 2 else [3, 2, 2]
        sevens = n - (2 if e % 2 else 1)
        require(7 * sevens + sum(exceptional) == 7 * n, 'Distribution total dimension')
        require(49 * sevens + sum((x * x for x in exceptional)) == 49 * n - 32, 'Distribution square sum')
        rows.append({'e': e, 'n': n, 'N': N, 'R': R, 'sum_prime': total_n, 'sum_composite': total_N, 'prime_multiplicity_square_sum': total_n // R, 'composite_multiplicity_square_sum': total_N // R, 'leading_matrix_checks': lead_checks, 'size_seven_count': sevens, 'exceptional_sizes': exceptional})
    crt = []
    for e in range(1, 4):
        n = 5 ** e
        N = 7 * n
        t7 = pow(n, -1, 7)
        tn = pow(7, -1, n)
        count = 0
        for x in range(N):
            for y in range(N):
                lhs = phase(N, x, y)
                rhs = (n * t7 * phase(7, x % 7, y % 7) + 7 * tn * phase(n, x % n, y % n)) % N
                require(lhs == rhs, 'CRT phase mismatch')
                count += 1
        crt.append({'e': e, 'N': N, 'primitive_power_mod7': t7, 'primitive_power_mod_n': tn, 'matrix_entries_checked': count})
    n7 = []
    for t in range(1, 7):
        g = [[zeta(t * phase(7, x, y)) for y in range(7)] for x in range(7)]
        tr = Z
        for i in range(7):
            tr = cyclo_add(tr, g[i][i])
        require(cyclo_mul(tr, tr) == cyclo_scale(ONE, -7), 'N7 trace square')
        cube = matrix_mul(matrix_mul(g, g), g)
        for i in range(7):
            for j in range(7):
                require(cube[i][j] == (cyclo_scale(tr, -7) if i == j else Z), 'N7 cube')
        n7.append({'primitive_power': t, 'trace_coefficients': tr, 'cube_entries_checked': 49, 'trace_square': True})
    occupancy = []
    for mask in range(8):
        used = [j for j in range(3) if mask >> j & 1]
        weights = [sum(((3, 2, 2)[(j - r) % 3] for r in used)) for j in range(3)]
        deficit = 7 * sum(weights) - sum((x * x for x in weights))
        require(deficit == (32 if len(used) in (1, 2) else 0), 'Orbit deficit')
        occupancy.append({'subset': used, 'weights': weights, 'dimension': sum(weights), 'square_sum': sum((x * x for x in weights)), 'deficit': deficit})
    covariance = []
    for m in (5, 7, 25, 35, 125, 175):
        half = pow(2, -1, m)
        count = 0
        for u, v in ((1, 0), (0, 1)):
            up, vp = (3 * u + 2 * v, 4 * u + 3 * v)
            for x in range(m):
                for y in range(m):
                    lhs = (phase(m, x, y - v) + u * (y - half * v)) % m
                    rhs = (phase(m, x + vp, y) + up * (x + half * vp)) % m
                    require(lhs == rhs, 'Raw Weyl covariance phase mismatch')
                    count += 1
        covariance.append({'N': m, 'generator_phase_equalities_checked': count, 'primitive_root_extension': 'Multiplying either identical residue by any unit preserves equality.'})
    result = {'status': 'passed', 'arithmetic': 'Python exact integers; N7 exact Q[zeta_7] coefficient tuples', 'python': sys.version, 'seconds': round(time.monotonic() - start, 3), 'S6_minus_I_div5': h, 'leading_determinant_mod5': det(h) % 5, 'literal_entrywise_valuation_counterexample': {'k': 6, 'entry_valuations': [vp5(x) for x in s6]}, 'base_mod5': base, 'trace_controls': rows, 'brute_kernel_comparisons': brute_cases, 'CRT_controls': crt, 'primitive_N7_controls': n7, 'occupancy_controls': occupancy, 'raw_covariance_controls': covariance, 'non_claims': ['Bounded controls are not the uniform proof.', 'No kicked-U simplicity.', 'No simple compressed kick.', 'No BGS conclusion.']}
    (ROOT / 'arithmetic_checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'seconds': result['seconds'], 'trace_depths': len(rows), 'brute_kernel_comparisons': brute_cases, 'CRT_entries': sum((x['matrix_entries_checked'] for x in crt)), 'N7_primitive_powers': len(n7), 'covariance_equalities': sum((x['generator_phase_equalities_checked'] for x in covariance))}, indent=2))
    return locals()
