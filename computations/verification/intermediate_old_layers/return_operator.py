"""Bounded reviewed arithmetic. All executable work is inside run(root); outputs stay in scratch. Original assertions are explicit RuntimeError checks, including under python -O. Original __debug__ preconditions are obsolete after this conversion."""

def run(scratch_root):
    __file__ = str(scratch_root / 'independent_checks.py')
    'Independent, bounded raw-Weyl/coherent-lattice audit; no canonical writes.'
    from pathlib import Path
    import json, time, hashlib, platform, itertools
    import numpy as np
    import sympy as sp
    RDIR = Path(__file__).resolve().parent
    FROZEN = RDIR / 'frozen/workspace/shared/bgs_intermediate_return_test'
    START = time.monotonic()

    def require(b, label):
        if not b:
            raise RuntimeError(label)

    def mm(A, B, p):
        return A @ B % p

    def mp(A, k, p):
        out = np.eye(len(A), dtype=np.int64)
        while k:
            if k & 1:
                out = out @ A % p
            A = A @ A % p
            k //= 2
        return out

    def tmul(A, B, d):
        return tuple((tuple((sum((A[i][k] * B[k][j] for k in range(2))) % d for j in range(2))) for i in range(2)))

    def tpow(k, d):
        a = ((3, 4), (2, 3))
        b = ((1, 0), (0, 1))
        while k:
            if k & 1:
                b = tmul(a, b, d)
            a = tmul(a, a, d)
            k //= 2
        return b

    def mv(A, u):
        return tuple((sum((A[i][k] * u[k] for k in range(2))) for i in range(2)))

    def om(u, v):
        return u[0] * v[1] - u[1] * v[0]

    def add(u, v):
        return tuple((a + b for a, b in zip(u, v)))

    def wy(d, q, u, p):
        A = np.zeros((d, d), dtype=np.int64)
        a, b = u
        for x in range(d):
            A[x, (x + a) % d] = pow(q, b * (x + a * pow(2, -1, d)) % d, p)
        return A

    def cat(d, q, p, sqrtd):
        return np.array([[pow(q, -pow(8, -1, d) * (3 * x * x - 2 * x * y + 3 * y * y) % d, p) * pow(sqrtd, -1, p) % p for y in range(d)] for x in range(d)], dtype=np.int64)

    def vp(x):
        if x == 0:
            return None
        t = 0
        while x % 5 == 0:
            x //= 5
            t += 1
        return t
    out = {'scope': 'Fresh raw matrix, modular phase, coherent cycle, and exact characteristic controls for the frozen return note; no residual25 continuation.', 'python': platform.python_version(), 'numpy': np.__version__, 'sympy': sp.__version__}
    original = json.loads((FROZEN / 'intermediate_return_control.json').read_text())
    replay = json.loads((RDIR / 'reproduce_control.json').read_text())
    a = json.loads(json.dumps(original))
    b = json.loads(json.dumps(replay))
    for obj in [a, b]:
        for c in obj['cases']:
            c.pop('seconds')
    require(a == b, 'Replay differs outside runtime')
    out['source_replay_matches_except_runtime'] = True
    cpresults = []
    for case in original['cases']:
        p = case['prime']
        rows = []
        for block in case['blocks']:
            mat = sp.Matrix(block['second_order_compression'])
            cs = [int(c) % p for c in mat.charpoly().all_coeffs()]
            require(cs == block['second_order_characteristic_descending'], 'Independent characteristic polynomial disagreement')
            z = sp.Symbol('z')
            poly = sp.Poly.from_list(cs, z, modulus=p)
            gd = sp.gcd(poly, poly.diff()).degree()
            require(gd == 0, 'Non-squarefree second-order block')
            rows.append({'lambda': block['lambda'], 'dimension': len(mat.tolist()), 'gcd_degree': gd})
        cpresults.append({'e': case['e'], 'j': case['j'], 'prime': p, 'blocks': rows})
    out['independent_characteristics'] = cpresults
    c = original['cases'][0]
    p = c['prime']
    n = 625
    m = 25
    h = 5
    qn = c['qn']
    qm = c['qm']
    Mn = cat(n, qn, p, 25)
    Mm = cat(m, qm, p, 5)
    J = np.zeros((n, m), dtype=np.int64)
    for x in range(n):
        if x % h == 0:
            J[x, x // h % m] = 1
    require(np.array_equal(Mn @ J % p, J @ Mm % p), 'Raw oldform intertwining')
    raw = []
    for u in [(1, 0), (1, 1), (0, 1), (0, 5)]:
        V = wy(n, qn, u, p) @ J % p
        for k in range(6):
            V = Mn @ V % p
        su = mv(tpow(6, n), u)
        b = tuple(((su[i] - u[i]) // h % m for i in range(2)))
        zz = pow(qn, -om(u, su) * pow(2, -1, n) % n, p)
        B = zz * (wy(m, qm, b, p) @ mp(Mm, 6, p) % p) % p
        require(np.array_equal(V, wy(n, qn, u, p) @ J % p @ B % p), 'Raw primitive/nonprimitive return identity')
        raw.append({'u': u, 'L': 6, 'raw_parent_dimension': n, 'identity_verified': True})
    for u, v in [((1, 0), (0, 1)), ((1, 1), (0, 5)), ((-1, 6), (1, -8))]:
        require(np.array_equal(wy(m, qm, u, p) @ wy(m, qm, v, p) % p, pow(qm, om(u, v) * pow(2, -1, m) % m, p) * wy(m, qm, add(u, v), p) % p), 'Weyl cocycle sign')
        require(np.array_equal(Mm @ wy(m, qm, u, p) % p, wy(m, qm, mv(((3, 4), (2, 3)), u), p) @ Mm % p), 'Cat covariance sign')
    out['raw_dense_return_checks'] = raw
    upper = [0, 1, -1, 6, -6, 7, -7, 8, -8]
    support = [(0, b) for a in [1, 2, 5, 6, 7, 8, 9] for b in [a, -a]] + [(a, b) for a in [1, -1] for b in upper]
    phase_rows = []
    for case in original['cases']:
        e = case['e']
        j = case['j']
        h = 5 ** j
        m = 25
        n = h * h * m
        R = case['R']
        ih = pow(2, -1, n)
        powers = []
        power = ((1, 0), (0, 1))
        for k in range(R):
            powers.append(power)
            power = tmul(power, ((3, 4), (2, 3)), n)
        total = 0
        primitive_pairs = 0
        nonprimitive_pairs = 0
        mixed_returns = 0
        for v in support:
            for u in support:
                prim = u[0] % 5 != 0 or u[1] % 5 != 0
                primv = v[0] % 5 != 0 or v[1] % 5 != 0
                ks = [k for k, A in enumerate(powers) if all((x % h == 0 for x in add(v, mv(A, u))))]
                if not ks:
                    continue
                require(prim == primv, 'Mixed-content return')
                if prim:
                    primitive_pairs += 1
                    L = 6 * 5 ** (j - 1)
                elif j >= 2:
                    nonprimitive_pairs += 1
                    L = 6 * 5 ** (j - 2)
                else:
                    nonprimitive_pairs += 1
                    L = 6
                classes = sorted(set((k % L for k in ks)))
                for a in classes:
                    sa = mv(powers[a], u)
                    ca = tuple(((v[i] + sa[i]) // h % m for i in range(2)))
                    theta = om(v, sa) * ih % n
                    for k in [z for z in ks if z % L == a]:
                        t = (k - a) // L
                        sl = mv(powers[L * t], u)
                        bt = tuple(((sl[i] - u[i]) // h % m for i in range(2)))
                        sab = mv(powers[a], bt)
                        exponent = (theta - om(u, sl) * ih + h * h * om(ca, sab) * pow(2, -1, m)) % n
                        actual = om(v, mv(powers[k], u)) * ih % n
                        require(exponent == actual, 'Raw class phase factor mismatch')
                        ck = tuple(((v[i] + mv(powers[k], u)[i]) // h % m for i in range(2)))
                        require(tuple(((ca[i] + sab[i]) % m for i in range(2))) == ck, 'Return translation mismatch')
                        require(tpow(k, 7) == tpow(a, 7), 'Seven-factor class variation')
                        total += int(k > 0)
        require(total == case['actual_rotated_return_terms'], 'Return enumeration count')
        phase_rows.append({'e': e, 'j': j, 'primitive_ordered_mode_pairs': primitive_pairs, 'nonprimitive_ordered_mode_pairs': nonprimitive_pairs, 'nonzero_k_terms': total, 'raw_phase_identity_verified': True})
    out['exhaustive_return_phase_checks'] = phase_rows
    cycles = []
    for j, ell in [(1, 1), (2, 1), (1, 2), (2, 2), (3, 2), (1, 3)]:
        h = 5 ** j
        H = 5 ** ell
        m = H * H
        n = h * h * m
        L = 6 * 5 ** (j - 1)
        S = tpow(L, n)
        half = pow(2, -1, n)
        for u in [(1, 0), (1, 1), (0, 1), (-1, 8)]:
            su = mv(S, u)
            b = tuple(((su[k] - u[k]) // h % m for k in range(2)))
            zexp = -om(u, su) * half % n
            rho_order = 5 ** max(2 * ell - j, 0)
            for rho_label in [0, 1, 2] if rho_order > 1 else [0]:
                rhoexp = n // rho_order * rho_label % n
                edges = {}
                for y in itertools.product(range(H), repeat=2):
                    sy = mv(S, y)
                    w = add(b, sy)
                    r = tuple((a % H for a in w))
                    exp = (zexp + rhoexp + h * h * (om(b, sy) - om(r, tuple((w[k] - r[k] for k in range(2))))) * pow(2, -1, m)) % n
                    edges[y] = (r, exp)
                remain = set(edges)
                hols = []
                while remain:
                    start = min(remain)
                    y = start
                    hol = 0
                    length = 0
                    while True:
                        require(y in remain, 'Cycle overlap')
                        remain.remove(y)
                        y, phase = edges[y]
                        hol = (hol + phase) % n
                        length += 1
                        if y == start:
                            break
                    require(length == H, 'Affine cycle length')
                    x = tuple((u[k] + h * start[k] for k in range(2)))
                    sx = mv(tpow(L * H, n), x)
                    expected = (-om(x, sx) * half + H * rhoexp) % n
                    require(hol == expected, 'Coherent holonomy discrepancy')
                    require(hol % (h * H) == 0 and hol // (h * H) % 5 == (2 * u[1] ** 2 - u[0] ** 2) % 5, 'Holonomy leading coefficient')
                    require(vp(hol) == j + ell, 'Holonomy order')
                    hols.append(hol)
                require(len(hols) == H, 'Cycle count')
                cycles.append({'j': j, 'ell': ell, 'u': u, 'rho_order': rho_order, 'rho_label': rho_label, 'cycle_count': len(hols), 'cycle_length': H, 'holonomy_order': h * H, 'leading_coefficient': (2 * u[1] ** 2 - u[0] ** 2) % 5, 'entry_valuation_denominator': 4 * 5 ** (j + ell - 1), 'naive_scaled_entry_valuation_numerator': 1 - H, 'naive_scaled_entry_valuation_denominator': 4 * 5 ** (j + 2 * ell - 1)})
    out['coherent_monomial_checks'] = cycles
    out['seconds'] = time.monotonic() - START
    out['result'] = 'All independent finite assertions passed; uniform claims require the separate proof audit.'
    (RDIR / 'independent_checks.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'result': out['result'], 'characteristic_blocks': sum((len(x['blocks']) for x in cpresults)), 'raw_dense_identities': len(raw), 'raw_return_terms': sum((x['nonzero_k_terms'] for x in phase_rows)), 'coherent_models': len(cycles), 'seconds': out['seconds']}))
