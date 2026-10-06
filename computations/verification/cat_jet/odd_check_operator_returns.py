"""Bounded exact reviewed arithmetic; writes only into caller-provided scratch root."""

def run(root, helpers=None):
    """Independent odd-depth boundary controls, exact modular/cyclotomic arithmetic.
All actual 32 modes, all 1024 pairs, all times for r=2,3. No candidate imports.
Checks the matrix-valued progression including its right-Weyl cocycle, weighted
geometric cancellation in the 25-dimensional Weyl basis, coefficient classes,
and k=0 deletion. Finite controls supplement the separate uniform proof.
"""
    from fractions import Fraction as Q
    from collections import defaultdict, Counter
    from math import gcd
    from pathlib import Path
    import json, time, platform
    ROOT = root

    def check(b, msg):
        if not b:
            raise RuntimeError(msg)
    rpoly = defaultdict(Q)
    for b, c in [(0, Q(1)), (7, Q(-1, 2)), (-7, Q(-1, 2))]:
        for d, f in [(0, Q(1)), (1, Q(1, 2)), (-1, Q(1, 2))]:
            rpoly[b + d] += c * f
    raw = defaultdict(lambda: [Q(0), Q(0)])

    def put(a, b, c, d=0):
        raw[a, b][0] += c
        raw[a, b][1] += d
    put(0, 7, Q(1, 2))
    put(0, -7, Q(1, 2))
    put(0, 0, Q(-1, 10))
    for b, c in rpoly.items():
        put(0, b, c / 10)
        put(0, b + 1, 0, -c / 200)
        put(0, b - 1, 0, c / 200)
        put(1, b, -3 * c / 1000, -4 * c / 1000)
        put(-1, b, -3 * c / 1000, 4 * c / 1000)
    coeff = {v: tuple((int(4000 * x) for x in c)) for v, c in raw.items() if any(c)}
    check(len(coeff) == 32 and (0, 0) not in coeff, 'actual support')
    check(all(((4000 * x).denominator == 1 for c in raw.values() for x in c)), 'coefficient integrality')

    def gaussval(c):
        a, b = c
        k = 0
        while (2 * a - b) % 5 == 0 and (a + 2 * b) % 5 == 0:
            a, b = ((2 * a - b) // 5, (a + 2 * b) // 5)
            k += 1
        return k
    vals = {v: gaussval(c) for v, c in coeff.items()}
    check(all((vals[v] == 0 for v in coeff if v[0] == 1)), 'upper valuations')
    check(all((vals[v] == 2 for v in coeff if v[0] == -1)), 'lower valuations')
    check(all((vals[v] >= 1 for v in coeff if v[0] == 0)), 'diagonal valuations')
    check([v for v in coeff if not (v[0] % 5 or v[1] % 5)] == [(0, 5), (0, -5)], 'nonprimitive modes')

    def pairmul(a, b, m):
        return ((a[0] * b[0] + 2 * a[1] * b[1]) % m, (a[0] * b[1] + a[1] * b[0]) % m)

    def Spower(k, m):
        a = (1, 0)
        b = (3, 2)
        while k:
            if k % 2:
                a = pairmul(a, b, m)
            b = pairmul(b, b, m)
            k //= 2
        return a

    def act(g, u, m):
        return ((g[0] * u[0] + 2 * g[1] * u[1]) % m, (g[1] * u[0] + g[0] * u[1]) % m)

    def omega(u, v):
        return u[0] * v[1] - u[1] * v[0]

    def norm(u):
        return 2 * u[1] ** 2 - u[0] ** 2

    def cyclozero(p, n):
        step = n // 5
        degree = 4 * step
        out = defaultdict(int)
        for e, c in p.items():
            if e < degree:
                out[e] += c
            else:
                for j in range(4):
                    out[e - degree + j * step] -= c
        return not any(out.values())
    start = time.time()
    runs = []
    for r in [2, 3]:
        h = 5 ** r
        n = 5 * h * h
        R = 6 * 5 ** (2 * r)
        L = 6 * 5 ** (r - 1)
        inv2 = pow(2, -1, n)
        check(Spower(R, n) == (1, 0), 'full order')
        check(all((Spower(R // p, n) != (1, 0) for p in [2, 3, 5])), 'exact full order')
        returns = {(v, u): [] for v in coeff for u in coeff}
        target = defaultdict(list)
        for v in coeff:
            target[-v[0] % h, -v[1] % h].append(v)
        rotated = {u: (u[0] % n, u[1] % n) for u in coeff}
        for k in range(R):
            for u, s in rotated.items():
                for v in target[s[0] % h, s[1] % h]:
                    c = ((v[0] + s[0]) // h % 5, (v[1] + s[1]) // h % 5)
                    E = omega(v, s) * inv2 % n
                    returns[v, u].append((k, E, c))
            rotated = {u: act((3, 2), s, n) for u, s in rotated.items()}
        counts = Counter()
        nonprimitive = []
        sumchecks = 0
        k0count = 0
        termcount = 0
        for (v, u), row in returns.items():
            cv = int(not (v[0] % 5 or v[1] % 5))
            cu = int(not (u[0] % 5 or u[1] % 5))
            expected = cv == cu and (norm(v) // 25 ** cv - norm(u) // 25 ** cu) % (h // 5 ** cv) == 0
            check(bool(row) == expected, 'return classification')
            if not row:
                continue
            period = L // 5 ** cv
            length = R // period
            a = row[0][0]
            check([z[0] for z in row] == [a + j * period for j in range(length)], 'full return class')
            check(0 <= a < period, 'minimal return')
            check(all((k % 3 == a % 3 for k, E, c in row)), 'seven factor constancy')
            g = Spower(period, n)
            su = act(g, u, n)
            zexp = -omega(u, su) * inv2 % n
            b = ((su[0] - u[0]) // h % 5, (su[1] - u[1]) // h % 5)
            ba = act(Spower(a, 5), b, 5)
            E0 = row[0][1]
            c0 = row[0][2]
            expected_order = 5 * h if cv == 0 else h
            check(n // gcd(zexp, n) == expected_order, 'scalar denominator order')
            check(length % expected_order == 0 and length % 5 == 0, 'matrix root identity')
            beta = g[1] // (h // 5 ** cv) % (5 * h)
            check(g[1] % (h // 5 ** cv) == 0 and beta % 5 == 2, 'off diagonal return coefficient')
            check((g[0] - 1) % (h // 5 ** cv) ** 2 == 0, 'diagonal return coefficient')
            check(zexp % (h * 5 ** cv) == 0, 'zeta power')
            if not cv:
                check(zexp // h % 5 == norm(u) % 5, 'primitive residue denominator')
            for j, (k, E, c) in enumerate(row):
                check(c == ((c0[0] + j * ba[0]) % 5, (c0[1] + j * ba[1]) % 5), 'operator Weyl label progression')
                rhs = (E0 + j * zexp + h * h * 3 * j * omega(c0, ba)) % n
                check(E == rhs, 'operator phase progression including cocycle')
            pol = {c: defaultdict(int) for c in [(a, b) for a in range(5) for b in range(5)]}
            for k, E, c in row:
                weight = R - 2 * k
                pol[c][E] += weight
                newc = ((c[0] + ba[0]) % 5, (c[1] + ba[1]) % 5)
                exp = (E + zexp + h * h * 3 * omega(c, ba)) % n
                pol[newc][exp] -= weight
            pol[c0][E0] -= 2 * R
            check(all((cyclozero(p, n) for p in pol.values())), 'exact weighted operator sum')
            delta = Q(1, 4 * h)
            denval = delta * (5 if cv else 1)
            check(denval < Q(1, 8), 'strict lattice margin')
            normalized = vals[v] + vals[u] + delta - denval
            if v[0] == u[0] == 1:
                check(norm(v) == norm(u) and normalized == 0, 'upper survivors')
                counts['upper_upper_survivors'] += 1
            else:
                check(normalized > 0, 'omitted coefficient class')
            if a == 0:
                check(E0 == 0, 'k0 scalar')
                check(delta + vals[v] + vals[u] > 0, 'k0 normalized vanishing')
                k0count += 1
            termcount += len(row)
            sumchecks += 1
            counts['nonprimitive' if cv else 'primitive'] += 1
            if cv:
                nonprimitive.append({'v': v, 'u': u, 'period': period, 'returns': length, 'z_order': expected_order, 'normalized_valuation': str(normalized), 'b_a': ba})
        check(counts['upper_upper_survivors'] == 17, 'all and only 17 survive')
        runs.append({'r': r, 'N': 7 * n, 'h': h, 'n': n, 'R': R, 'pair_count': 1024, 'mode_time_steps': 32 * R, 'return_counts': dict(counts), 'total_return_terms_including_k0': termcount, 'operator_geometric_checks': sumchecks, 'k0_classes': k0count, 'nonprimitive': nonprimitive})
    out = {'arithmetic': 'Integer modular arithmetic plus exact Q cyclotomic reduction; no numeric tolerance', 'coefficients': [{'v': v, 'd': c, 'gaussian_valuation': vals[v]} for v, c in sorted(coeff.items())], 'runs': runs, 'seconds': time.time() - start, 'python': platform.python_version()}
    (ROOT / 'operator_return_checks.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))
    return locals()
