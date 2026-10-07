import sys

def main():
    if len(sys.argv) != 2:
        raise ValueError("Expected scratch output directory")
    """Independent raw packet and fiber checks in integral cyclic group rings.

    No author's modules imported. Fiber vectors are kept integral; no fraction
    arithmetic or closed-form cat-power kernels are used to construct them.
    """
    from pathlib import Path
    import json, time, hashlib, platform
    START = time.monotonic()
    B = Path(sys.argv[1])
    Z = (0,) * 5
    ONE = (1, 0, 0, 0, 0)

    def canon(v):
        return tuple((x - v[-1] for x in v))

    def add(a, b):
        return canon(tuple((x + y for x, y in zip(a, b))))

    def scale(a, n):
        return tuple((x * n for x in a))

    def divide(a, n):
        if not all((x % n == 0 for x in a)):
            raise AssertionError((a, n))
        return tuple((x // n for x in a))

    def mul(a, b):
        z = [0] * 5
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                z[(i + j) % 5] += x * y
        return canon(z)

    def con(a):
        return canon((a[0], a[4], a[3], a[2], a[1]))

    def total(xs):
        z = Z
        for x in xs:
            z = add(z, x)
        return z

    def root(k):
        v = [0] * 5
        v[k % 5] = 1
        return canon(v)

    def dot(a, b):
        return total((mul(con(x), y) for x, y in zip(a, b)))
    fiber_checks = 0
    fiber_records = []
    for root_choice in [1, 2, 3, 4]:
        eta = lambda k: root(root_choice * k)
        g = total((eta(x * x) for x in range(5)))
        if not mul(g, g) == scale(ONE, 5):
            raise AssertionError('Exact control failed')
        K = [[eta(-pow(8, -1, 5) * (3 * x * x - 2 * x * y + 3 * y * y)) for y in range(5)] for x in range(5)]

        def cat(v):
            return [divide(mul(g, total((mul(z, w) for z, w in zip(row, v)))), 5) for row in K]

        def weyl(v, a, b):
            return [mul(eta(b * (2 * x + a) * 3), v[(x + a) % 5]) for x in range(5)]
        roots = {eta(k) for k in range(5)}
        for kind in ['delta', 'fourier']:
            base = [[g if x == k else Z for x in range(5)] for k in range(5)] if kind == 'delta' else [[eta(k * x) for x in range(5)] for k in range(5)]
            states = [base]
            for k in range(6):
                states.append([cat(v) for v in states[-1]])
            if not states[6] == base:
                raise AssertionError('Exact control failed')
            for r in range(6):
                for s in range(6):
                    sign = [0, 1, -1, 0, -1, 1][(s - r) % 6] * (1 if kind == 'delta' else -1)
                    for a in range(5):
                        for b in range(5):
                            W = [weyl(v, a, b) for v in states[s]]
                            for k in range(5):
                                for l in range(5):
                                    ip = dot(states[r][k], W[l])
                                    if sign:
                                        normalized = divide(mul(g, ip), 5)
                                        if not scale(normalized, sign) in roots:
                                            raise AssertionError((root_choice, kind, r, s, a, b, k, l))
                                    else:
                                        normalized = divide(ip, 5)
                                        if not (normalized == Z or normalized in roots or scale(normalized, -1) in roots):
                                            raise AssertionError('Exact control failed')
                                    fiber_checks += 1
            fiber_records.append({'root_choice': root_choice, 'kind': kind, 'exact_identities': 22500})
        print('fiber root', root_choice, 'checks', fiber_checks, flush=True)

    def cyc125(terms):
        z = [0] * 125
        for e, c in terms:
            z[e % 125] += c
        return tuple((z[r + 25 * k] - z[r + 100] for r in range(25) for k in range(4)))
    S = ((3, 4), (2, 3))
    I = ((1, 0), (0, 1))

    def mm(A, B):
        return tuple((tuple((sum((A[i][k] * B[k][j] for k in range(2))) for j in range(2))) for i in range(2)))

    def power(A, n, mod=None):
        z = I
        while n:
            if n & 1:
                z = mm(z, A)
            A = mm(A, A)
            n //= 2
            if mod:
                z = tuple((tuple((x % mod for x in r)) for r in z))
                A = tuple((tuple((x % mod for x in r)) for r in A))
        return z

    def mv(A, y):
        return tuple((sum((a * b for a, b in zip(row, y))) for row in A))

    def om(v, w):
        return v[0] * w[1] - v[1] * w[0]
    Q = lambda y: 2 * y[1] ** 2 - y[0] ** 2
    labels = [(a, b) for a in range(5) for b in range(5)]

    def Tvec125(a, b, vector):
        return [None if vector[(x + a) % 125] is None else (b * (x + 63 * a) + vector[(x + a) % 125]) % 125 for x in range(125)]
    old = []
    for i in range(5):
        old.append([0 if x % 5 == 0 and x // 5 % 5 == i else None for x in range(125)])
    E = {y: [Tvec125(*y, v) for v in old] for y in labels}
    gram_checks = 0
    for y in labels:
        for z in labels:
            for i in range(5):
                for k in range(5):
                    lhs = cyc125([(b - a, 1) for a, b in zip(E[y][i], E[z][k]) if a is not None and b is not None])
                    if not lhs == cyc125([(0, 5)] if y == z and i == k else []):
                        raise AssertionError('Exact control failed')
                    gram_checks += 1
    cat_checks = 0
    weyl_checks = 0
    for y in labels:
        sy = mv(S, y)
        r = tuple((x % 5 for x in sy))
        d = tuple(((a - b) // 5 for a, b in zip(sy, r)))
        phase = -63 * om(r, sy)
        for i in range(5):
            for x in range(125):
                lhs = cyc125([(e - pow(8, -1, 125) * (3 * x * x - 2 * x * z + 3 * z * z), 1) for z, e in enumerate(E[y][i]) if e is not None])
                rhs = []
                for k in range(5):
                    if E[r][k][x] is None:
                        continue
                    l = (k + d[0]) % 5
                    e5 = d[1] * (k + 3 * d[0]) - pow(8, -1, 5) * (3 * l * l - 2 * l * i + 3 * i * i)
                    rhs.append((E[r][k][x] + phase + 25 * e5, 5))
                if not lhs == cyc125(rhs):
                    raise AssertionError((y, i, x))
                cat_checks += 1
        for u in labels:
            uy = tuple((a + b for a, b in zip(u, y)))
            r = tuple((x % 5 for x in uy))
            d = tuple(((a - b) // 5 for a, b in zip(uy, r)))
            ph = 63 * (om(u, y) - om(r, uy))
            for i in range(5):
                lhs = Tvec125(*u, E[y][i])
                k = (i - d[0]) % 5
                scalar = ph + 25 * d[1] * (k + 3 * d[0])
                rhs = [None if e is None else (e + scalar) % 125 for e in E[r][k]]
                if not lhs == rhs:
                    raise AssertionError((u, y, i))
                weyl_checks += 125
    print('packets', cat_checks, 'Gram', gram_checks, 'Weyl entries', weyl_checks, flush=True)
    S6 = power(S, 6)
    charsets = {}
    holonomies = 0
    for y in labels:
        if y == (0, 0):
            continue
        sy = mv(S6, y)
        d = tuple(((a - b) // 5 % 5 for a, b in zip(sy, y)))
        if not d == (4 * y[1] % 5, 2 * y[0] % 5):
            raise AssertionError('Exact control failed')
        e = -63 * om(y, sy) % 125
        if not e == 55 * Q(y) % 125:
            raise AssertionError('Exact control failed')
        for x in range(5):
            if not sum((d[1] * (x + r * d[0] + 3 * d[0]) for r in range(5))) % 5 == 0:
                raise AssertionError('Exact control failed')
        holonomies += 1
        c = Q(y) % 5
        chars = {(6 * Q(y) + 5 * k) % 25 for k in range(5)}
        if not chars == {r for r in range(25) if r % 5 == c}:
            raise AssertionError('Exact control failed')
        charsets[c] = sorted(chars)
    if not sum((len(x) * 6 for x in charsets.values())) == 120:
        raise AssertionError('Exact control failed')
    for c, rs in charsets.items():
        for r in rs:
            if not 30 * r % 25 == 5 * c % 25:
                raise AssertionError('Exact control failed')
    controls = []
    for j in range(2, 9):
        h = 5 ** j
        n = 125 * h * h
        L = 6 * 5 ** (j - 1)
        for content, ell in [(1, L), (5, L // 5)]:
            A = power(S, 5 * ell, n)
            for u0 in [(1, b) for b in [0, 1, -1, 6, -6, 7, -7, 8, -8]] if content == 1 else [(0, 1), (0, -1)]:
                u = tuple((content * x for x in u0))
                for y in labels:
                    x = tuple((a + h * b for a, b in zip(u, y)))
                    e = -pow(2, -1, n) * om(x, mv(A, x)) % n
                    scale_ = 5 * h if content == 1 else 25 * h
                    if not (e % scale_ == 0 and e // scale_ % 5 == Q(u0) % 5):
                        raise AssertionError('Exact control failed')
                    w = tuple(((a - b) // (5 * h) % 5 for a, b in zip(mv(A, x), x)))
                    if not w != (0, 0):
                        raise AssertionError('Exact control failed')
            controls.append({'j': j, 'content': content, 'conductor': j + 2 if content == 1 else j + 1})
    result = {'scope': 'Exact integral raw packet/fiber checks plus bounded conductor controls, not uniform proof', 'fiber_arithmetic': 'Integer cyclic convolution modulo sum eta^r; transported raw cat vectors remain integral', 'fiber_identity_count': fiber_checks, 'fiber_cases': fiber_records, 'all_four_primitive_fifth_roots': True, 'all_relative_and_absolute_cat_powers': True, 'epsilon_minus_one': 'Multiplying raw cat by -1 multiplies checked overlaps by (-1)^(s-r), exactly the declared tame shift', 'raw_cat_packet_entries': cat_checks, 'gram_entries': gram_checks, 'raw_weyl_entries': weyl_checks, 'all_primitive_packet_holonomies': holonomies, 'wild_character_classes': charsets, 'new_character_count': 120, 'j2_character_factor_retained': True, 'conductor_controls': controls, 'seconds': time.monotonic() - START, 'python': platform.python_version(), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (B / 'raw_rebuild.json').write_text(json.dumps(result, indent=2) + '\n')
    print('DONE', result['seconds'], flush=True)

if __name__ == "__main__":
    main()
