import sys

def main():
    if len(sys.argv) != 2:
        raise ValueError("Expected scratch output directory")
    """Independent polynomial arithmetic/projector bases/Berkowitz certificate.

    Does not import or execute any author's arithmetic or matrix code.
    All primitive seven-root choices and both primitive sixth roots are rebuilt.
    """
    import json, time, hashlib, platform
    from pathlib import Path
    from functools import lru_cache
    START = time.monotonic()
    BASE = Path(sys.argv[1])
    FROZEN = Path(__file__).resolve().parents[3] / 'archive/evidence/residual125_20261007'
    MOD = (1, 0, 1, 3, 1, 0, 1)
    D = [tuple((n // 5 ** k % 5 for k in range(6))) for n in range(15625)]

    def enc(a):
        return sum((x * 5 ** k for k, x in enumerate(a)))

    def add(a, b):
        return enc([(x + y) % 5 for x, y in zip(D[a], D[b])])

    def neg(a):
        return enc([-x % 5 for x in D[a]])

    def sub(a, b):
        return add(a, neg(b))

    @lru_cache(None)
    def mul(a, b):
        p = [0] * 11
        for k, x in enumerate(D[a]):
            for l, y in enumerate(D[b]):
                p[k + l] += x * y
        for k in range(10, 5, -1):
            v = p[k] % 5
            for l in range(7):
                p[k - 6 + l] -= v * MOD[l]
        return enc([x % 5 for x in p[:6]])

    def power(a, n):
        if n < 0:
            return power(power(a, 15623), -n)
        z = 1
        while n:
            if n & 1:
                z = mul(z, a)
            a = mul(a, a)
            n //= 2
        return z

    def inv(a):
        if not a:
            raise AssertionError('Exact control failed')
        z = power(a, 15623)
        if not mul(a, z) == 1:
            raise AssertionError('Exact control failed')
        return z

    def total(xs):
        z = 0
        for x in xs:
            z = add(z, x)
        return z

    def eye(n):
        return [[int(i == j) for j in range(n)] for i in range(n)]

    def mm(A, B):
        return [[total((mul(a, b) for a, b in zip(row, col))) for col in zip(*B)] for row in A]

    def sm(s, A):
        return [[mul(s, x) for x in row] for row in A]

    def ma(A, B):
        return [[add(x, y) for x, y in zip(ar, br)] for ar, br in zip(A, B)]

    def inverse(A):
        n = len(A)
        B = [row[:] + eye(n)[i] for i, row in enumerate(A)]
        for c in range(n):
            r = next((r for r in range(c, n) if B[r][c]))
            B[c], B[r] = (B[r], B[c])
            z = inv(B[c][c])
            B[c] = [mul(z, x) for x in B[c]]
            for r in range(n):
                if r == c:
                    continue
                z = B[r][c]
                B[r] = [sub(x, mul(z, y)) for x, y in zip(B[r], B[c])]
        if not [r[:n] for r in B] == eye(n):
            raise AssertionError('Exact control failed')
        return [r[n:] for r in B]

    def rank(A):
        A = [r[:] for r in A]
        r = 0
        for c in range(len(A[0])):
            z = next((i for i in range(r, len(A)) if A[i][c]), None)
            if z is None:
                continue
            A[r], A[z] = (A[z], A[r])
            v = inv(A[r][c])
            A[r] = [mul(v, x) for x in A[r]]
            for k in range(r + 1, len(A)):
                v = A[k][c]
                A[k] = [sub(x, mul(v, y)) for x, y in zip(A[k], A[r])]
            r += 1
            if r == len(A):
                break
        return r

    def berkowitz(A):
        """Monic characteristic polynomial in descending order; division-free."""
        n = len(A)
        if n == 0:
            return [1]
        a = A[0][0]
        R = A[0][1:]
        C = [[row[0]] for row in A[1:]]
        M = [row[1:] for row in A[1:]]
        p = berkowitz(M)
        q = [1, neg(a)]
        for k in range(n - 1):
            q.append(neg(total((mul(x, row[0]) for x, row in zip(R, C)))))
            if k < n - 2:
                C = mm(M, C)
        return [total((mul(q[i - j], p[j]) for j in range(min(i, n - 1) + 1))) for i in range(n + 1)]

    def trim(p):
        while p and p[-1] == 0:
            p.pop()
        return p

    def rem(a, b):
        a = a[:]
        while len(a) >= len(b) and a:
            c = mul(a[-1], inv(b[-1]))
            d = len(a) - len(b)
            for i, x in enumerate(b):
                a[i + d] = sub(a[i + d], mul(c, x))
            trim(a)
        return a

    def gcd(a, b):
        while b:
            a, b = (b, rem(a, b))
        return [mul(inv(a[-1]), x) for x in a]

    def mv(A, u):
        return tuple((sum((x * y for x, y in zip(row, u))) for row in A))

    def m2(A, B):
        return tuple((tuple((sum((A[i][k] * B[k][j] for k in range(2))) for j in range(2))) for i in range(2)))
    S = ((3, 4), (2, 3))
    Sp = [((1, 0), (0, 1))]
    for k in range(5):
        Sp.append(m2(Sp[-1], S))
    Q = lambda v: 2 * v[1] ** 2 - v[0] ** 2
    UPPER = {(1, b): d for b, d in [(0, 4), (1, 2), (-1, 2), (6, -1), (-6, -1), (7, -2), (-7, -2), (8, -1), (-8, -1)]}
    PAIRS = []
    for v, dv in UPPER.items():
        for u, du in UPPER.items():
            if Q(v) != Q(u):
                continue
            a = next((k for k in range(6) if all(((x + y) % 5 == 0 for x, y in zip(v, mv(Sp[k], u))))))
            line = {(2 * k * v[1] % 5, k * v[0] % 5) for k in range(5)}
            PAIRS.append((v, u, a, 2 * dv * du * pow(Q(u) % 5, -1, 5) % 5, line))
    if not len(PAIRS) == 17:
        raise AssertionError('Exact control failed')
    ROOT = power(5, 9)
    XI = power(9, 15624 // 6)

    def prime_rem(a, b):
        a = a[:]
        while a and len(a) >= len(b):
            c = a[-1] * pow(b[-1], -1, 5) % 5
            d = len(a) - len(b)
            for k, x in enumerate(b):
                a[k + d] = (a[k + d] - c * x) % 5
            trim(a)
        return a

    def prime_gcd(a, b):
        while b:
            a, b = (b, prime_rem(a, b))
        return a
    if not power(5, 5 ** 6) == 5:
        raise AssertionError('Exact control failed')
    for exponent in [2, 3]:
        p = list(D[sub(power(5, 5 ** exponent), 5)])
        if not len(prime_gcd(list(MOD), trim(p))) == 1:
            raise AssertionError('Exact control failed')
    if not (power(ROOT, 7) == 1 and ROOT != 1):
        raise AssertionError('Exact control failed')
    if not (power(XI, 6) == 1 and power(XI, 3) != 1 and (power(XI, 2) != 1)):
        raise AssertionError('Exact control failed')
    author = json.loads((FROZEN / 'gauss_kernel_discriminator.json').read_text())
    if not (ROOT == author['w'] and XI == author['xi']):
        raise AssertionError('Exact control failed')
    refs = {(r['norm_mod5'], r['tame_index']): r['characteristic_ascending'] for r in author['records']}
    records = []
    reference_polys = {}
    for root_power in range(1, 7):
        w = power(ROOT, root_power)
        wp = [power(w, k) for k in range(7)]

        def T(v):
            a, b = v
            return [[wp[b * (x + 4 * a) % 7] if y == (x + a) % 7 else 0 for y in range(7)] for x in range(7)]
        G = [[wp[-(3 * x * x - 2 * x * y + 3 * y * y) % 7] for y in range(7)] for x in range(7)]
        tr = total((G[i][i] for i in range(7)))
        H = sm(inv(tr), G)
        I = eye(7)
        H2 = mm(H, H)
        if not mm(H2, H) == I:
            raise AssertionError('Exact control failed')
        for sixth_power in [1, 5]:
            xi = power(XI, sixth_power)
            om = power(xi, 2)
            labels = []
            columns = []
            for z in [1, om, power(om, 2)]:
                P = sm(2, ma(I, ma(sm(inv(z), H), sm(power(z, -2), H2))))
                if not mm(P, P) == P:
                    raise AssertionError('Exact control failed')
                chosen = []
                for k in range(6, -1, -1):
                    col = [row[k] for row in P]
                    test = chosen + [col]
                    if rank(list(map(list, zip(*test)))) > len(chosen):
                        chosen.append(col)
                if not len(chosen) == (3 if z == 1 else 2):
                    raise AssertionError('Exact control failed')
                columns += chosen
                labels += [z] * len(chosen)
            V = list(map(list, zip(*columns)))
            VI = inverse(V)
            if not mm(H, V) == [[mul(V[i][j], labels[j]) for j in range(7)] for i in range(7)]:
                raise AssertionError('Exact control failed')
            Bs = [mm(VI, mm(T(v), mm(T(tuple((x % 7 for x in mv(Sp[a], u)))), V))) for v, u, a, c, line in PAIRS]
            for norm, y0 in [(1, (2, 0)), (2, (0, 1)), (3, (0, 2)), (4, (1, 0))]:
                orbit = []
                y = y0
                for k in range(6):
                    orbit.append(y)
                    y = tuple((x % 5 for x in mv(S, y)))
                if not (y == y0 and len(set(orbit)) == 6 and all((Q(y) % 5 == norm for y in orbit))):
                    raise AssertionError('Exact control failed')
                for tame in range(6):
                    gammas = [mul(power(xi, tame), inv(z)) for z in labels]
                    gp = [[power(g, k) for k in range(6)] for g in gammas]
                    gn = [[power(g, -k) for k in range(6)] for g in gammas]
                    C = [[0] * 7 for i in range(7)]
                    for (v, u, a, coef, line), B in zip(PAIRS, Bs):
                        inds = [(r, s, [0, 1, -1, 0, -1, 1][(s - r) % 6] * (1 if norm in [1, 4] else -1) % 5) for r, x in enumerate(orbit) for s, y in enumerate(orbit) if ((x[0] - y[0]) % 5, (x[1] - y[1]) % 5) in line]
                        P = {}
                        for i in range(7):
                            for j in range(7):
                                key = (labels[i], labels[j])
                                if key not in P:
                                    P[key] = total((mul(wt, mul(gp[i][r], gn[j][s])) for r, s, wt in inds))
                                C[i][j] = add(C[i][j], mul(coef, mul(B[i][j], P[key])))
                    cp = berkowitz(C)[::-1]
                    derivative = trim([mul(k % 5, cp[k]) for k in range(1, len(cp))])
                    gg = gcd(cp, derivative)
                    if not len(gg) == 1:
                        raise AssertionError('Exact control failed')
                    if root_power == 1 and sixth_power == 1:
                        if not cp == refs[norm, tame]:
                            raise AssertionError('Exact control failed')
                        reference_polys[norm, tame] = cp
                    f = next((f for f in range(6) if pow(5, f, 7) == root_power))
                    t0 = tame * sixth_power * pow(pow(5, f, 6), -1, 6) % 6
                    expect = [power(x, 5 ** f) if x else 0 for x in reference_polys[norm, t0]]
                    if not cp == expect:
                        raise AssertionError((root_power, sixth_power, norm, tame))
                    records.append({'seventh_root_power': root_power, 'sixth_root_power': sixth_power, 'norm': norm, 'tame': tame, 'matrix': C, 'characteristic_ascending': cp, 'derivative_gcd_degree': len(gg) - 1})
            print('verified roots', root_power, sixth_power, 'matrices', len(records), flush=True)
    result = {'scope': 'Independent finite certificate for formula (19), not a uniform proof', 'arithmetic': 'Schoolbook polynomial multiplication modulo x^6+x^4+3x^3+x^2+1 over F5; no log tables', 'basis': 'Spectral projector columns, chosen from right to left', 'charpoly': 'Division-free recursive Berkowitz, not evaluation/interpolation', 'matrices': len(records), 'pair_count': 17, 'all_squarefree': True, 'all_author_polynomials_match': True, 'all_root_choices_match_frobenius': True, 'records': records, 'seconds': time.monotonic() - START, 'python': platform.python_version(), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE / 'residue_rebuild.json').write_text(json.dumps(result, indent=2) + '\n')
    print('DONE', len(records), 'seconds', result['seconds'], flush=True)

if __name__ == "__main__":
    main()
