"""Bounded reviewed arithmetic. All executable work is inside run(root); outputs stay in scratch. Original assertions are explicit RuntimeError checks, including under python -O. Original __debug__ preconditions are obsolete after this conversion."""

def run(scratch_root):
    __file__ = str(scratch_root / 'replay_position_residues.py')
    'Fresh F5^6 certificate, seven POSITION basis; no project imports.\nC=sum gamma^(kx-ky) H^(-kx) T H^ky; charpoly from eight determinant\nsamples and Vandermonde solve, so no eigenvectors or subset determinant.\n'
    from functools import lru_cache
    from pathlib import Path
    import json
    P = 5

    @lru_cache(None)
    def digits(a):
        return [a // 5 ** i % 5 for i in range(6)]

    def code(a):
        return sum((v % 5 * 5 ** i for i, v in enumerate(a)))

    @lru_cache(None)
    def add(a, b):
        return code([x + y for x, y in zip(digits(a), digits(b))])

    @lru_cache(None)
    def neg(a):
        return code([-x for x in digits(a)])

    def sub(a, b):
        return add(a, neg(b))

    @lru_cache(None)
    def mul(a, b):
        u = [0] * 7
        for i, x in enumerate(digits(a)):
            for j, y in enumerate(digits(b)):
                u[(i + j) % 7] += x * y
        return code([u[i] - u[6] for i in range(6)])

    def powe(a, n):
        n %= 15624
        o = 1
        while n:
            if n % 2:
                o = mul(o, a)
            a = mul(a, a)
            n //= 2
        return o

    def inv(a):
        if not a:
            raise RuntimeError('replay_position_residues.py:32: a')
        return powe(a, 15623)

    def mm(A, B):
        return [[sumf((mul(x, y) for x, y in zip(row, col))) for col in zip(*B)] for row in A]

    def sumf(it):
        s = 0
        for x in it:
            s = add(s, x)
        return s

    def ident(n):
        return [[int(i == j) for j in range(n)] for i in range(n)]

    def scal(A, s):
        return [[mul(s, x) for x in row] for row in A]

    def plus(A, B):
        return [[add(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]

    def elimination(A, b=None):
        A = [row[:] for row in A]
        rows = len(A)
        cols = len(A[0])
        rank = 0
        det = 1
        if b is not None:
            A = [row + [v] for row, v in zip(A, b)]
        for j in range(cols):
            k = next((k for k in range(rank, rows) if A[k][j]), None)
            if k is None:
                continue
            if k != rank:
                A[k], A[rank] = (A[rank], A[k])
                det = neg(det)
            t = A[rank][j]
            det = mul(det, t)
            A[rank] = [mul(x, inv(t)) for x in A[rank]]
            for k in range(rows):
                if k == rank:
                    continue
                t = A[k][j]
                A[k] = [sub(x, mul(t, y)) for x, y in zip(A[k], A[rank])]
            rank += 1
            if rank == rows:
                break
        if b is not None:
            if not rank == rows:
                raise RuntimeError('replay_position_residues.py:54: rank == rows')
            return [r[-1] for r in A]
        return (rank, det if rank == rows else 0)

    def cp(A, w):
        xs = [0] + [powe(w, j) for j in range(7)]
        ds = [elimination([[sub(x if i == j else 0, A[i][j]) for j in range(7)] for i in range(7)])[1] for x in xs]
        return elimination([[1] + [powe(x, j) if x else 0 for j in range(1, 8)] for x in xs], ds)

    def trim(a):
        while len(a) > 1 and (not a[-1]):
            a.pop()
        return a

    def gcd(a, b):
        while b != [0]:
            r = a[:]
            while len(r) >= len(b) and r != [0]:
                off = len(r) - len(b)
                s = mul(r[-1], inv(b[-1]))
                for i, x in enumerate(b):
                    r[off + i] = sub(r[off + i], mul(s, x))
                trim(r)
            a, b = (b, r)
        return len(a) - 1

    def run():
        xi = 1314
        if not (powe(xi, 3) == 4 and powe(xi, 2) != 1):
            raise RuntimeError('replay_position_residues.py:75: powe(xi, 3) == 4 and powe(xi, 2) != 1')
        result = []
        I = ident(7)
        for root in range(1, 7):
            w = powe(5, root)
            G = [[powe(w, -pow(8, -1, 7) * (3 * x * x - 2 * x * y + 3 * y * y)) for y in range(7)] for x in range(7)]
            tr = sumf((G[x][x] for x in range(7)))
            H = scal(G, inv(tr))
            Hs = [I, H, mm(H, H)]
            if not mm(Hs[2], H) == I:
                raise RuntimeError('replay_position_residues.py:81: mm(Hs[2], H) == I')
            omega = powe(xi, 2)
            dims = []
            for z in [1, omega, powe(omega, 2)]:
                projector = scal(plus(plus(I, scal(H, inv(z))), scal(Hs[2], powe(z, -2))), 2)
                if not mm(projector, projector) == projector:
                    raise RuntimeError('replay_position_residues.py:86: mm(projector, projector) == projector')
                dims.append(elimination(projector)[0])
            if not dims == [3, 2, 2]:
                raise RuntimeError('replay_position_residues.py:88: dims == [3, 2, 2]')
            T = {sgn: [[powe(w, sgn * 5 * x) if x == y else 0 for y in range(7)] for x in range(7)] for sgn in [1, -1]}
            for c in range(1, 5):
                v = next(((a, b) for a in range(5) for b in range(5) if (2 * b * b - a * a) % 5 == c))
                vs = []
                for k in range(6):
                    vs.append(v)
                    a, b = v
                    v = ((3 * a + 4 * b) % 5, (2 * a + 3 * b) % 5)
                if not (len(set(vs)) == 6 and v == vs[0]):
                    raise RuntimeError('replay_position_residues.py:94: len(set(vs)) == 6 and v == vs[0]')
                ix = {v: k for k, v in enumerate(vs)}
                for deep in [False, True]:
                    for t in range(6):
                        C = [[0] * 7 for _ in range(7)]
                        if not (deep and c == 3):
                            for ky, (a, b) in enumerate(vs):
                                for sign in [1, -1]:
                                    kx = ix.get((a, (b + sign) % 5))
                                    if kx is None:
                                        continue
                                    term = mm(Hs[-kx % 3], mm(T[sign], Hs[ky % 3]))
                                    C = plus(C, scal(term, mul(-2 * sign % 5, powe(xi, t * (kx - ky)))))
                        pol = cp(C, w)
                        rank = elimination(C)[0]
                        gd = gcd(pol, [mul(k % 5, pol[k]) for k in range(1, 8)])
                        if not gd == (6 if c == 1 or (deep and c == 3) else 0):
                            raise RuntimeError('replay_position_residues.py:106: gd == (6 if c == 1 or (deep and c == 3) else 0)')
                        if not rank == (0 if gd else 6):
                            raise RuntimeError('replay_position_residues.py:107: rank == (0 if gd else 6)')
                        result.append(dict(root=root, c_mod5=c, l_ge_2=deep, tame_index=t, characteristic_ascending=pol, gcd_degree=gd, rank=rank))
        supplied = json.loads((scratch_root / 'author/independent_residue.json').read_text())['records']
        for r in result:
            if r['root'] != 1:
                continue
            s = next((s for s in supplied if all((s[k] == r[k] for k in ['c_mod5', 'l_ge_2', 'tame_index']))))
            if not all((r[k] == s[k] for k in ['characteristic_ascending', 'gcd_degree', 'rank'])):
                raise RuntimeError("replay_position_residues.py:114: all((r[k] == s[k] for k in ['characteristic_ascending', 'gcd_degree', 'rank']))")
        out = {'arithmetic': 'exact F5[X]/Phi7, position-space spectral-projector construction', 'records': result, 'records_count': len(result), 'simple_count': sum((r['gcd_degree'] == 0 for r in result)), 'zero_count': sum((r['rank'] == 0 for r in result)), 'source_match_at_root_1': True}
        Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
        print(json.dumps({k: v for k, v in out.items() if k != 'records'}))
    run()
