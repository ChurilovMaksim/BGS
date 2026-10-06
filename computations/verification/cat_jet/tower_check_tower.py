"""Bounded exact reviewed arithmetic; writes only into caller-provided scratch root."""

def run(root, helpers=None):
    """Independent, exact finite controls for the oldform-tower audit.
No author implementation is imported. Integer cyclotomic reduction is exact.
This finite run supplements, and does not replace, the uniform proof.
"""
    from collections import defaultdict
    from fractions import Fraction as F
    from pathlib import Path
    import datetime, hashlib, json, platform, subprocess, sys, time
    ROOT = root
    START = datetime.datetime.now(datetime.timezone.utc).isoformat()
    T0 = time.monotonic()

    def require(test, what):
        if not test:
            raise RuntimeError(what)

    def digest(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()

    def clean(d):
        return {k: v for k, v in d.items() if v}

    def cyclo(n, terms):
        d = defaultdict(int)
        if n == 1:
            return {0: sum((c for p, c in terms))} if sum((c for p, c in terms)) else {}
        h = n // 5
        for p, c in terms:
            p %= n
            if p < 4 * h:
                d[p] += c
            else:
                for k in range(4):
                    d[p - 4 * h + k * h] -= c
        return clean(d)

    def Q(n, x, y):
        return 0 if n == 1 else -pow(8, -1, n) * (3 * x * x - 2 * x * y + 3 * y * y) % n

    def W(n, x, a, b):
        return 0 if n == 1 else b * (x + pow(2, -1, n) * a) % n

    def roots(n):
        if n <= 125:
            return [c for c in range(1, n) if c % 5]
        return sorted(set((c % n for c in [1, 2, 3, 4, 7, n - 1, pow(7, -1, n)] if c % n and c % 5)))
    kernel_count = norm_count = 0
    kernel_scopes = []
    for e in range(0, 7):
        n = 5 ** e
        for j in range(e // 2 + 1):
            q = 5 ** j
            m = n // (q * q)
            full = n <= 625 or (e == 5 and j == 2)
            xs = list(range(n)) if full else sorted(set([0, 1, q - 1, q, q + 1, n // 2, n - q, n - 1] + [q * t for t in [m - 1, m // 2] if q * t < n]))
            ts = list(range(m)) if full else sorted(set([0, 1 % m, m // 2, m - 1]))
            cs = [1] if n == 1 else roots(n)
            if j == 0:
                xs = sorted(set([0, 1 % n, n // 2, n - 1]))
                ts = sorted(set([0, 1 % m, m // 2, m - 1]))
                full = n == 1
            for c in cs:
                for x in xs:
                    for t in ts:
                        lhs = cyclo(n, [(c * Q(n, x, q * (t + m * l)), 1) for l in range(q)])
                        rhs = cyclo(n, [(q * q * (c % m) * Q(m, x // q % m, t), q)]) if x % q == 0 else {}
                        require(lhs == rhs, f'kernel {(e, j, c, x, t)}')
                        kernel_count += 1
            supports = [{q * (t + m * l) for l in range(q)} for t in range(m)]
            require(all((len(s) == q for s in supports)), f'norm {(e, j)}')
            seen = set()
            for s in supports:
                require(not seen.intersection(s), f'orthogonality {(e, j)}')
                seen.update(s)
            require(len(seen) == q * m, f'support size {(e, j)}')
            norm_count += m
            kernel_scopes.append({'e': e, 'j': j, 'n': n, 'm': m, 'primitive_powers': cs, 'x_scope': 'all' if full else xs, 't_scope': 'all' if full else ts, 'entries': len(cs) * len(xs) * len(ts)})
    trace_count = 0
    trace_scopes = []
    for e in range(2, 9):
        n = 5 ** e
        cs = roots(n) if e <= 6 else [1, pow(7, -1, n)]
        for j in range(1, e // 2 + 1):
            q = 5 ** j
            m = n // (q * q)
            for c in cs:
                lhs = cyclo(n, [(c * Q(n, x, x), 1) for x in range(n)])
                rhs = cyclo(n, [(q * q * (c % m) * Q(m, x, x), q) for x in range(m)])
                require(lhs == rhs, f'trace {(e, j, c)}')
                trace_count += 1
            trace_scopes.append({'e': e, 'j': j, 'primitive_powers': cs, 'summands_per_lhs': n, 'summands_per_rhs': m})

    def g(r=0, i=0):
        return (F(r), F(i))

    def ga(z, w):
        return (z[0] + w[0], z[1] + w[1])

    def gm(z, w):
        return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

    def gc(z):
        return (z[0], -z[1])

    def pclean(p):
        return {v: c for v, c in p.items() if c != g()}

    def pa(*ps):
        out = {}
        for p in ps:
            for v, c in p.items():
                out[v] = ga(out.get(v, g()), c)
        return pclean(out)

    def ps(p, s):
        return pclean({v: gm(c, s) for v, c in p.items()})

    def pm(p, q):
        out = {}
        for (a, b), c in p.items():
            for (d, e), f in q.items():
                v = (a + d, b + e)
                out[v] = ga(out.get(v, g()), gm(c, f))
        return pclean(out)
    unit = {(0, 0): g(1)}
    cos7 = {(0, 7): g(F(1, 2)), (0, -7): g(F(1, 2))}
    cos1 = {(0, 1): g(F(1, 2)), (0, -1): g(F(1, 2))}
    sin1 = {(0, 1): g(0, F(-1, 2)), (0, -1): g(0, F(1, 2))}
    cospa = {(1, 0): g(F(-3, 10), F(-2, 5)), (-1, 0): g(F(-3, 10), F(2, 5))}
    r = pm(pa(unit, ps(cos7, g(-1))), pa(unit, cos1))
    A = pa(cos7, ps(r, g(F(1, 10))), ps(pm(r, sin1), g(F(1, 100))), ps(pm(r, cospa), g(F(1, 100))), ps(unit, g(F(-1, 10))))
    require(len(A) == 32, '32 actual modes')
    require((0, 0) not in A, 'centering')
    require(all((abs(a) <= 1 and abs(b) <= 9 for a, b in A)), 'support bounds')
    require(all((A.get((-a, -b)) == gc(c) for (a, b), c in A.items())), 'Hermiticity')
    retained = {v: c for v, c in A.items() if v[0] % 5 == 0 and v[1] % 5 == 0}
    require(retained == {(0, 5): g(0, F(-1, 800)), (0, -5): g(0, F(1, 800))}, 'j=1 coefficients')
    require(not [v for v in A if v[0] % 25 == 0 and v[1] % 25 == 0], 'j=2 vanishing')
    require(pm(A, A)[0, 0] == g(F(66033, 160000)), 'A^2 scalar coefficient')
    weyl_count = 0
    weyl_scopes = []
    for e, j in [(2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (6, 1), (6, 2), (6, 3)]:
        n = 5 ** e
        q = 5 ** j
        m = n // (q * q)
        us = list(range(m)) if m <= 25 else [0, 1, m // 2, m - 1]
        labels = sorted(set(A) | {(a, b) for a in [-q, 0, q, 2 * q, q + 1] for b in [-q, 0, q, 2 * q, q + 1]})
        cs = roots(n) if e <= 4 else [1, pow(7, -1, n), n - 1]
        for c in cs:
            for a, b in labels:
                for u in us:
                    terms = defaultdict(list)
                    for h in range(q):
                        x = q * (u + m * h)
                        y = (x + a) % n
                        if y % q == 0:
                            terms[y // q % m].append((c * W(n, x, a, b), 1))
                    lhs = {v: cyclo(n, t) for v, t in terms.items() if cyclo(n, t)}
                    rhs = {}
                    if a % q == 0 and b % q == 0:
                        v = (u + a // q) % m
                        rhs[v] = cyclo(n, [(q * q * (c % m) * W(m, u, a // q, b // q), q)])
                    require(lhs == rhs, f'Weyl {(e, j, c, a, b, u)}')
                    weyl_count += 1
        weyl_scopes.append({'e': e, 'j': j, 'primitive_powers': cs, 'u_scope': 'all' if len(us) == m else us, 'labels': labels, 'row_comparisons': len(cs) * len(labels) * len(us)})
    crt_kernel_count = crt_weyl_count = crt_lower_count = 0
    crt_scopes = []
    for e in range(1, 6):
        n = 5 ** e
        N = 7 * n
        t7 = pow(n, -1, 7)
        tn = pow(7, -1, n)
        xs = list(range(N)) if e <= 4 else [0, 1, 2, 6, 7, 8, n - 1, n, n + 1, N // 2, N - 7, N - 1]
        ys = list(range(N)) if e <= 2 else [0, 1, 6, 7, n - 1, n, N - 1]
        for x in xs:
            for y in ys:
                rhs = (n * t7 * Q(7, x % 7, y % 7) + 7 * tn * Q(n, x % n, y % n)) % N
                require(Q(N, x, y) == rhs, f'CRT kernel {(e, x, y)}')
                crt_kernel_count += 1
            for a, b in A:
                rhs = (n * t7 * W(7, x % 7, a, b) + 7 * tn * W(n, x % n, a, b)) % N
                require(W(N, x, a, b) == rhs, f'CRT Weyl {(e, x, a, b)}')
                crt_weyl_count += 1
        crt_scopes.append({'e': e, 'x_scope': 'all' if e <= 4 else xs, 'y_scope': 'all' if e <= 2 else ys})
    for e in range(0, 10):
        n = 5 ** e
        for j in range(e // 2 + 1):
            q = 5 ** j
            m = n // (q * q)
            old = pow(n, -1, 7)
            small = pow(m, -1, 7)
            require((old * q * q - small) % 7 == 0, 'lower seven coefficient')
            for x in range(7):
                for y in range(7):
                    require((old * Q(7, q * x, q * y) - small * Q(7, x, y)) % 7 == 0, 'lower seven conjugation')
                    crt_lower_count += 1
            if m > 1:
                require(pow(7, -1, n) % m == pow(7, -1, m), 'lower five coefficient')
    omega = [(1, 0), (0, 1), (-1, -1)]

    def osum(s):
        return tuple((sum((omega[i][j] for i in s)) for j in range(2)))
    partial = [s for s in [set((i for i in range(3) if mask >> i & 1)) for mask in range(8)] if len(s) in (1, 2)]
    require(len({osum(s) for s in partial}) == 6, 'partial traces distinct within orbit')
    for s in partial:
        if len(s) == 1:
            require(osum(s) == omega[next(iter(s))], 'singleton trace')
        else:
            missing = next(iter(set(range(3)) - s))
            require(osum(s) == tuple((-x for x in omega[missing])), 'missing-point trace')
    support = set(A)
    reachable = {(0, 0)}
    power_checks = []
    for k in range(0, 14):
        if k:
            reachable = {(a + c, b + d) for a, b in reachable for c, d in support}
        require(all((abs(a) <= k and abs(b) <= 9 * k for a, b in reachable)), 'power box')
        for j in [0, 1, 2, 3]:
            q = 5 ** j
            if 9 * k < q:
                retained = sorted((v for v in reachable if v[0] % q == 0 and v[1] % q == 0))
                require(all((v == (0, 0) for v in retained)), 'direct power scalar support')
                power_checks.append({'k': k, 'j': j, 'q': q, 'retained_labels': retained})
    parity = []
    for e in range(4, 21):
        m = 5 ** (e - 4)
        dims = [3, 2, 2] if e % 2 == 0 else [4, 5, 5]
        seven_count = m - (1 if e % 2 == 0 else 2)
        require(seven_count >= 0 and 7 * seven_count + sum(dims) == 7 * m, 'parity total')
        parity.append({'e': e, 'm': m, 'seven_blocks': seven_count, 'exceptional_blocks': dims, 'dimension': 7 * m})
    input_hashes = {p.name: digest(p) for p in sorted((ROOT / 'inputs').glob('*'))}
    require(input_hashes['oldform_tower_compression.md'] == 'd359482763667a6707ed9a060a3874e951f95336561a4ac645df453022b085ae', 'target binding')
    require(input_hashes['uniform_cat_multiplicity_v2.md'] == 'b6e219832f094136f0ca80201ae61f80a9d2435bebc59dd2f18163e3444c8e1e', 'dependency binding')
    result = {'result': 'all exact finite controls passed', 'arithmetic': 'integers, Fraction Gaussian rationals, exact Q[zeta_(5^e)] polynomial reduction; no floats', 'input_sha256': input_hashes, 'kernel_intertwining': {'entries': kernel_count, 'scopes': kernel_scopes}, 'normalization': {'basis_vectors': norm_count}, 'trace_recurrence': {'identities': trace_count, 'scopes': trace_scopes}, 'actual_symbol': {'coefficients': [{'a': a, 'b': b, 'real': str(c[0]), 'imag': str(c[1])} for (a, b), c in sorted(A.items())], 'j1_coefficients': '(0,5): -i/800; (0,-5): +i/800', 'j_ge_2_survivors': 0, 'A2_constant': '66033/160000'}, 'weyl_compression': {'row_comparisons': weyl_count, 'scopes': weyl_scopes}, 'CRT': {'kernel_phase_identities': crt_kernel_count, 'Weyl_phase_identities': crt_weyl_count, 'lower_seven_conjugation_identities': crt_lower_count, 'scopes': crt_scopes}, 'partial_orbits': {'nonempty_proper_subsets_tested': 6, 'trace_rule': 'singleton=trace; missing doublet point=-trace'}, 'direct_power_support': {'max_k': 13, 'checks': power_checks}, 'parity_counts': parity, 'python': sys.version, 'platform': platform.platform(), 'run_started': START, 'runtime_seconds': time.monotonic() - T0}
    (ROOT / 'checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['result', 'runtime_seconds']}, indent=2))
    print('kernel entries', kernel_count, 'trace identities', trace_count, 'Weyl rows', weyl_count, 'CRT kernel', crt_kernel_count, 'CRT Weyl', crt_weyl_count)
    return locals()
