"""Bounded reviewed arithmetic. All executable work is inside run(root); outputs stay in scratch. Original assertions are explicit RuntimeError checks, including under python -O. Original __debug__ preconditions are obsolete after this conversion."""

def run(scratch_root):
    __file__ = str(scratch_root / 'raw_coherent_check.py')
    'Exact cyclotomic coefficient verification of residual-25 coherent phases.\nArithmetic in Z[q]/Phi25; denominators are checked before division.\nAlso checks return representatives/holonomy valuations for a declared finite range.\n'
    import hashlib, json, time, platform
    from pathlib import Path
    from fractions import Fraction
    B = Path(__file__).resolve().parent
    start = time.monotonic()
    pass
    N = 25
    half = 13
    S = ((3, 4), (2, 3))
    J = ((0, 2), (1, 0))

    def mv(A, v):
        return tuple((sum((a * x for a, x in zip(row, v))) for row in A))

    def mm(A, B):
        return tuple((tuple((sum((A[i][k] * B[k][j] for k in range(2))) for j in range(2))) for i in range(2)))

    def mp(A, n, mod=None):
        C = ((1, 0), (0, 1))
        while n:
            if n & 1:
                C = mm(C, A)
                C = tuple((tuple((x % mod if mod else x for x in r)) for r in C))
            A = mm(A, A)
            A = tuple((tuple((x % mod if mod else x for x in r)) for r in A))
            n //= 2
        return C

    def omega(a, b):
        return a[0] * b[1] - a[1] * b[0]

    def Q(v):
        return 2 * v[1] ** 2 - v[0] ** 2

    def reduce(cs):
        out = list(cs) + [0] * (25 - len(cs))
        for k in range(24, 19, -1):
            a = out[k]
            out[k] = 0
            for off in [5, 10, 15, 20]:
                out[k - off] -= a
        return out[:20]

    def mono(e):
        c = [0] * 25
        c[e % 25] = 1
        return reduce(c)

    def sums(exps):
        c = [0] * 25
        for e in exps:
            c[e % 25] += 1
        return reduce(c)

    def phi(v, x):
        return v[1] * (x + half * v[0]) % 25 if (x + v[0]) % 5 == 0 else None
    labels = [(a, b) for a in range(5) for b in range(5)]
    for v in labels:
        sv = mv(S, v)
        r = tuple((a % 5 for a in sv))
        phase = -half * omega(r, sv) % 25
        for x in range(25):
            exps = [(-pow(8, -1, 25) * (3 * x * x - 2 * x * y + 3 * y * y) + phi(v, y)) % 25 for y in range(25) if phi(v, y) is not None]
            lhs = sums(exps)
            expected = phi(r, x)
            rhs = [0] * 20 if expected is None else [5 * z for z in mono(expected + phase)]
            if not lhs == rhs:
                raise RuntimeError('raw_coherent_check.py:44: lhs == rhs')
    for u in labels:
        for v in labels:
            exps = [phi(v, x) - phi(u, x) for x in range(25) if phi(u, x) is not None and phi(v, x) is not None]
            if not sums(exps) == ([5] + [0] * 19 if u == v else [0] * 20):
                raise RuntimeError('raw_coherent_check.py:49: sums(exps) == ([5] + [0] * 19 if u == v else [0] * 20)')
    for u in [(1, 0), (0, 1), (0, 5), (5, 0)]:
        for v in labels:
            w = tuple((u[k] + v[k] for k in range(2)))
            r = tuple((k % 5 for k in w))
            phase = half * (omega(u, v) - omega(r, w)) % 25
            for x in range(25):
                a = phi(v, (x + u[0]) % 25)
                b = phi(r, x)
                if not (a is None) == (b is None):
                    raise RuntimeError('raw_coherent_check.py:55: (a is None) == (b is None)')
                if a is not None:
                    if not mono(u[1] * (x + half * u[0]) + a) == mono(phase + b):
                        raise RuntimeError('raw_coherent_check.py:56: mono(u[1] * (x + half * u[0]) + a) == mono(phase + b)')
    circles = []
    for c in range(1, 5):
        y = next((v for v in labels if Q(v) % 5 == c))
        orbit = []
        phases = []
        for k in range(6):
            orbit.append(y)
            sy = mv(S, y)
            r = tuple((a % 5 for a in sy))
            phases.append(-half * omega(r, sy) % 25)
            y = r
        if not (y == orbit[0] and len(set(orbit)) == 6 and (sum(phases) % 25 == 5 * c % 25)):
            raise RuntimeError('raw_coherent_check.py:62: y == orbit[0] and len(set(orbit)) == 6 and (sum(phases) % 25 == 5 * c % 25)')
        circles.append({'norm': c, 'orbit': orbit, 'edge_phase_exponents_mod25': phases, 'holonomy_exponent_mod25': sum(phases) % 25, 'six_eigenvalues': 'q25^(5*c) * xi^t, t=0,...,5'})
    if not set(sum([z['orbit'] for z in circles], [])) == set(labels) - {(0, 0)}:
        raise RuntimeError("raw_coherent_check.py:64: set(sum([z['orbit'] for z in circles], [])) == set(labels) - {(0, 0)}")
    upper = [(1, b) for b in [0, 1, -1, 6, -6, 7, -7, 8, -8]]
    pairs = [(v, u) for v in upper for u in upper if Q(v) == Q(u)]
    records = []
    for j in range(2, 7):
        h = 5 ** j
        n = h * h * 25
        L = 6 * 5 ** (j - 1)
        a_star = Fraction(1, 4 * 5 ** j)
        A = mp(S, L * 5, n)
        for u in upper:
            for y in labels:
                x = tuple((u[k] + h * y[k] for k in range(2)))
                e = -pow(2, -1, n) * omega(x, mv(A, x)) % n
                if not (e % (5 * h) == 0 and e // (5 * h) % 5 == Q(u) % 5):
                    raise RuntimeError('raw_coherent_check.py:75: e % (5 * h) == 0 and e // (5 * h) % 5 == Q(u) % 5')
        Apr = mp(S, L // 5 * 5, n)
        for u in [(0, 5), (0, -5)]:
            for y in labels:
                x = tuple((u[k] + h * y[k] for k in range(2)))
                e = -pow(2, -1, n) * omega(x, mv(Apr, x)) % n
                if not (e % (25 * h) == 0 and e // (25 * h) % 5 == Q((u[0] // 5, u[1] // 5)) % 5):
                    raise RuntimeError('raw_coherent_check.py:80: e % (25 * h) == 0 and e // (25 * h) % 5 == Q((u[0] // 5, u[1] // 5)) % 5')
        power = ((1, 0), (0, 1))
        returns = {}
        for a in range(L):
            for v, u in pairs:
                if (v, u) in returns:
                    continue
                su = mv(power, u)
                if all(((v[k] + su[k]) % h == 0 for k in range(2))):
                    ca = tuple(((v[k] + su[k]) // h % 5 for k in range(2)))
                    if not (-2 * v[0] * ca[0] + 4 * v[1] * ca[1]) % 5 == 0:
                        raise RuntimeError('raw_coherent_check.py:88: (-2 * v[0] * ca[0] + 4 * v[1] * ca[1]) % 5 == 0')
                    returns[v, u] = {'v': v, 'u': u, 'a': a, 'c_mod5': ca}
            power = tuple((tuple((z % (5 * h) for z in row)) for row in mm(power, S)))
        if not len(returns) == 17:
            raise RuntimeError('raw_coherent_check.py:91: len(returns) == 17')
        records.append({'j': j, 'primitive_holonomy_conductor': j + 1, 'nonprimitive_holonomy_conductor': j, 'minimum_nonprimitive_normalized_valuation': str(2 - 4 * a_star), 'returns': list(returns.values())})
    result = {'scope': 'Exact residual25 raw kernel/coherent basis and bounded j=2..6 return controls; not the universal proof', 'cyclotomic_modulus': 'Phi25(q)=q^20+q^15+q^10+q^5+1', 'raw_cat_coherent_identity': True, 'coherent_gram_5I': True, 'four_weyl_generators': True, 'origin_fixed': True, 'circles': circles, 'return_controls': records, 'seconds': time.monotonic() - start, 'python': platform.python_version(), 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (B / 'raw_coherent_check.json').write_text(json.dumps(result, indent=2) + '\n')
    print('PASS exact Q(zeta25) raw coherent identity, circle holonomies, and j=2..6 controls; seconds', result['seconds'])
