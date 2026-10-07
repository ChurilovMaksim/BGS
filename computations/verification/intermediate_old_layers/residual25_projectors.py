"""Bounded reviewed arithmetic. All executable work is inside run(root); outputs stay in scratch. Original assertions are explicit RuntimeError checks, including under python -O. Original __debug__ preconditions are obsolete after this conversion."""

def run(scratch_root):
    __file__ = str(scratch_root / 'independent_residue.py')
    'Independent direct-product projector audit, F5[x]/(x^6+x+2).\nNo import of the proposed residue implementation or field arithmetic.\nUses 42-position space and order-six projectors rather than its entrywise dictionary.\nCharacteristic polynomials use subset-expansion determinants, no interpolation.\n'
    import hashlib, json, time, platform
    from pathlib import Path
    import numpy as np
    import sympy as sp
    BASE = Path(__file__).resolve().parent
    start = time.monotonic()
    pass
    MOD = [2, 1, 0, 0, 0, 0, 1]
    SIZE = 15625
    ORDER = 15624
    x = sp.symbols('x')
    if not sp.Poly(x ** 6 + x + 2, x, modulus=5).is_irreducible:
        raise RuntimeError('independent_residue.py:15: sp.Poly(x ** 6 + x + 2, x, modulus=5).is_irreducible')
    weights = 5 ** np.arange(6, dtype=np.int64)
    digits = np.arange(SIZE)[:, None] // weights % 5
    D3 = np.arange(125)[:, None] // 5 ** np.arange(3) % 5
    A3 = (D3[:, None, :] + D3[None, :, :]) % 5 @ 5 ** np.arange(3)
    N3 = -D3 % 5 @ 5 ** np.arange(3)

    def add(a, b):
        a = np.asarray(a)
        b = np.asarray(b)
        return A3[a % 125, b % 125] + 125 * A3[a // 125, b // 125]

    def neg(a):
        a = np.asarray(a)
        return N3[a % 125] + 125 * N3[a // 125]

    def sub(a, b):
        return add(a, neg(b))

    def slowmul(a, b):
        cc = np.convolve(digits[a], digits[b]).astype(int)
        for k in range(10, 5, -1):
            u = cc[k] % 5
            cc[k] -= u
            cc[k - 6] -= 2 * u
            cc[k - 5] -= u
        return int(cc[:6] % 5 @ weights)

    def slowpow(a, n):
        out = 1
        while n:
            if n & 1:
                out = slowmul(out, a)
            a = slowmul(a, a)
            n //= 2
        return out
    g = next((a for a in range(2, SIZE) if all((slowpow(a, ORDER // p) != 1 for p in [2, 3, 7, 31]))))
    EXP = np.zeros(ORDER, dtype=np.int64)
    u = 1
    for k in range(ORDER):
        EXP[k] = u
        u = slowmul(u, g)
    if not (u == 1 and len(set(EXP.tolist())) == ORDER):
        raise RuntimeError('independent_residue.py:40: u == 1 and len(set(EXP.tolist())) == ORDER')
    LOG = np.zeros(SIZE, dtype=np.int64)
    LOG[EXP] = np.arange(ORDER)

    def mul(a, b):
        a = np.asarray(a)
        b = np.asarray(b)
        return np.where((a == 0) | (b == 0), 0, EXP[(LOG[a] + LOG[b]) % ORDER])

    def power(a, n):
        a = int(a)
        if a == 0:
            if not n > 0:
                raise RuntimeError('independent_residue.py:47: n > 0')
            return 0
        return int(EXP[int(LOG[a]) * n % ORDER])

    def inv(a):
        if not np.all(np.asarray(a) != 0):
            raise RuntimeError('independent_residue.py:50: np.all(np.asarray(a) != 0)')
        return EXP[-LOG[a] % ORDER]

    def mm(A, B):
        C = np.zeros((A.shape[0], B.shape[1]), dtype=np.int64)
        for k in range(A.shape[1]):
            C = add(C, mul(A[:, k, None], B[k, None, :]))
        return C

    def matpow(A, n):
        C = np.eye(len(A), dtype=np.int64)
        while n:
            if n & 1:
                C = mm(C, A)
            A = mm(A, A)
            n //= 2
        return C

    def rref(A):
        A = A.copy()
        piv = []
        r = 0
        for c in range(A.shape[1]):
            ix = np.flatnonzero(A[r:, c])
            if not len(ix):
                continue
            k = r + int(ix[0])
            A[[r, k]] = A[[k, r]]
            A[r] = mul(A[r], inv(A[r, c]))
            f = A[:, c].copy()
            f[r] = 0
            A = sub(A, mul(f[:, None], A[r]))
            piv.append(c)
            r += 1
            if r == len(A):
                break
        return (A, piv)

    def inverse(A):
        n = len(A)
        C, piv = rref(np.concatenate([A, np.eye(n, dtype=np.int64)], axis=1))
        if not piv[:n] == list(range(n)):
            raise RuntimeError('independent_residue.py:70: piv[:n] == list(range(n))')
        if not np.array_equal(C[:, :n], np.eye(n, dtype=np.int64)):
            raise RuntimeError('independent_residue.py:70: np.array_equal(C[:, :n], np.eye(n, dtype=np.int64))')
        return C[:, n:]

    def polytrim(p):
        while len(p) > 1 and (not p[-1]):
            p.pop()
        return p

    def polyrem(a, b):
        a = a.copy()
        while len(a) >= len(b) and a != [0]:
            off = len(a) - len(b)
            factor = int(mul(a[-1], inv(b[-1])))
            a[off:] = sub(np.array(a[off:]), mul(factor, np.array(b))).tolist()
            polytrim(a)
        return a

    def gcd(a, b):
        while b != [0]:
            a, b = (b, polyrem(a, b))
        return mul(np.array(a), inv(a[-1])).tolist()

    def charpoly(C):
        n = len(C)
        dp = {0: np.array([1] + [0] * n, dtype=np.int64)}
        for row in range(n):
            nxt = {}
            for mask, p in dp.items():
                for col in range(n):
                    if mask >> col & 1:
                        continue
                    term = mul(neg(C[row, col]), p)
                    if row == col:
                        term = add(term, np.concatenate([[0], p[:-1]]))
                    if (mask >> col + 1).bit_count() % 2:
                        term = neg(term)
                    key = mask | 1 << col
                    nxt[key] = add(nxt.get(key, np.zeros(n + 1, dtype=np.int64)), term)
            dp = nxt
        out = dp[(1 << n) - 1].tolist()
        if not out[-1] == 1:
            raise RuntimeError('independent_residue.py:96: out[-1] == 1')
        return out

    def eval_poly(cs, a):
        y = 0
        for c in reversed(cs):
            y = int(add(mul(y, a), c))
        return y
    roots = [a for a in range(SIZE) if eval_poly([1, 0, 1, 3, 1, 0, 1], a) == 0]
    if not len(roots) == 6:
        raise RuntimeError('independent_residue.py:103: len(roots) == 6')
    root = roots[0]
    embedding = [eval_poly(d.tolist(), root) for d in digits]
    ref = json.loads((BASE / 'frozen/residual25_affine_residue.json').read_text())
    w0 = embedding[ref['w']]
    xi = embedding[ref['xi']]
    if not (power(w0, 7) == 1 and w0 != 1 and (power(xi, 6) == 1) and (power(xi, 3) != 1) and (power(xi, 2) != 1)):
        raise RuntimeError('independent_residue.py:107: power(w0, 7) == 1 and w0 != 1 and (power(xi, 6) == 1) and (power(xi, 3) != 1) and (power(xi, 2) != 1)')
    r4 = {0: 4, 1: 2, -1: 2, 6: -1, -6: -1, 7: -2, -7: -2, 8: -1, -8: -1}
    Q = lambda v: 2 * v[1] * v[1] - v[0] * v[0]
    S = np.array([[3, 4], [2, 3]], dtype=np.int64)
    spows = [np.eye(2, dtype=np.int64)]
    for k in range(1, 6):
        spows.append(spows[-1] @ S)
    upper = [(1, b) for b in r4]
    pairs = []
    for v in upper:
        for u in upper:
            if Q(v) != Q(u):
                continue
            aa = [a for a in range(6) if np.all((np.array(v) + spows[a] @ u) % 5 == 0)]
            if not len(aa) == 1:
                raise RuntimeError('independent_residue.py:120: len(aa) == 1')
            a = aa[0]
            dv = (-3 * r4[v[1]] + 2 * (-4 * r4[v[1]])) % 5
            du = (-3 * r4[u[1]] + 2 * (-4 * r4[u[1]])) % 5
            factor = 2 * dv * du * pow(Q(v) % 5, -1, 5) % 5
            pairs.append((v, u, a, factor))
    if not len(pairs) == 17:
        raise RuntimeError('independent_residue.py:124: len(pairs) == 17')
    records = []
    for root_index in range(1, 7):
        w = power(w0, root_index)
        wp = [power(w, k) for k in range(7)]
        G = np.array([[wp[(-3 * i * i + 2 * i * j - 3 * j * j) % 7] for j in range(7)] for i in range(7)], dtype=np.int64)
        tr = 0
        for k in range(7):
            tr = int(add(tr, G[k, k]))
        H = mul(G, inv(tr))
        if not np.array_equal(matpow(H, 3), np.eye(7, dtype=np.int64)):
            raise RuntimeError('independent_residue.py:132: np.array_equal(matpow(H, 3), np.eye(7, dtype=np.int64))')
        B7 = []
        for v, u, a, factor in pairs:
            su = spows[a] @ u
            A = int(v[0] + su[0])
            B = int(v[1] + su[1])
            om = int(v[0] * su[1] - v[1] * su[0])
            C = np.zeros((7, 7), dtype=np.int64)
            for row in range(7):
                C[row, (row + A) % 7] = wp[(4 * om + B * (row + 4 * A)) % 7]
            B7.append(C)
        for norm in range(1, 5):
            y0 = next((np.array([a, b]) for a in range(5) for b in range(5) if Q((a, b)) % 5 == norm))
            orbit = []
            y = y0.copy()
            for k in range(6):
                orbit.append(tuple(y.tolist()))
                y = S @ y % 5
            if not (len(set(orbit)) == 6 and np.array_equal(y, y0)):
                raise RuntimeError('independent_residue.py:142: len(set(orbit)) == 6 and np.array_equal(y, y0)')
            P = np.zeros((6, 6), dtype=np.int64)
            for k in range(6):
                P[(k + 1) % 6, k] = 1
            A = mul(H[:, None, :, None], P[None, :, None, :]).reshape(42, 42)
            if not np.array_equal(matpow(A, 6), np.eye(42, dtype=np.int64)):
                raise RuntimeError('independent_residue.py:146: np.array_equal(matpow(A, 6), np.eye(42, dtype=np.int64))')
            K = np.zeros((42, 42), dtype=np.int64)
            for (v, u, a, factor), B in zip(pairs, B7):
                R = np.array([[int((-2 * v[0] * (x[0] - y[0]) + 4 * v[1] * (x[1] - y[1])) % 5 == 0) for y in orbit] for x in orbit], dtype=np.int64)
                K = add(K, mul(factor, mul(B[:, None, :, None], R[None, :, None, :]).reshape(42, 42)))
            powers = [np.eye(42, dtype=np.int64)]
            for k in range(1, 6):
                powers.append(mm(powers[-1], A))
            for tame in range(6):
                lam = power(xi, tame)
                E = np.zeros_like(A)
                for k, Ak in enumerate(powers):
                    E = add(E, mul(power(lam, -k), Ak))
                E = mul(E, pow(6, -1, 5))
                if not np.array_equal(mm(E, E), E):
                    raise RuntimeError('independent_residue.py:158: np.array_equal(mm(E, E), E)')
                _, cols = rref(E)
                if not len(cols) == 7:
                    raise RuntimeError('independent_residue.py:159: len(cols) == 7')
                V = E[:, cols]
                _, rows = rref(V.T)
                if not len(rows) == 7:
                    raise RuntimeError('independent_residue.py:160: len(rows) == 7')
                left = inverse(V[rows, :])
                compressed = mm(left, mm(E, mm(K, V))[rows, :])
                cp = charpoly(compressed)
                deriv = polytrim([int(mul(i % 5, cp[i])) for i in range(1, 8)])
                gg = gcd(cp, deriv)
                if not len(gg) == 1:
                    raise RuntimeError('independent_residue.py:162: len(gg) == 1')
                matches = None
                if root_index == 1:
                    source = next((r for r in ref['records'] if r['norm_mod5'] == norm and r['tame_index'] == tame))
                    matches = cp == [embedding[v] for v in source['characteristic_ascending']]
                    if not matches:
                        raise RuntimeError('independent_residue.py:166: matches')
                records.append({'seventh_root_power': root_index, 'norm': norm, 'tame': tame, 'rank_projector': 7, 'cp_ascending': cp, 'gcd_degree': len(gg) - 1, 'author_field_embedding_match': matches, 'compression': compressed.tolist()})
        print('root', root_index, '24 squarefree; runtime', round(time.monotonic() - start, 3), flush=True)
    result = {'scope': '144 independently projected exact matrices; six primitive seventh roots, four norm circles, six tame labels', 'field_modulus_ascending': MOD, 'primitive_element': g, 'author_generator_image': root, 'w0': w0, 'xi': xi, 'pair_count': len(pairs), 'pairs': pairs, 'records': records, 'squarefree_count': len(records), 'all_author_polynomials_match': all((r['author_field_embedding_match'] for r in records if r['seventh_root_power'] == 1)), 'python': platform.python_version(), 'numpy': np.__version__, 'sympy': sp.__version__, 'seconds': time.monotonic() - start, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE / 'independent_residue.json').write_text(json.dumps(result, indent=2) + '\n')
    print('PASS', result['squarefree_count'], 'squarefree; all 24 author polynomials match', flush=True)
