"""Independent literal-permutation and rational arithmetic controls. No author imports."""
from itertools import product, permutations
from functools import reduce
from fractions import Fraction as F
from pathlib import Path
import json, time
import sympy as s
from sympy.polys.matrices import DomainMatrix

def mul(*mats):
    a = DomainMatrix.from_Matrix(mats[0]).convert_to(s.QQ_I)
    for b in mats[1:]:
        a = a.matmul(DomainMatrix.from_Matrix(b).convert_to(s.QQ_I))
    return a.to_Matrix()

def kron(*mats):
    return reduce(s.kronecker_product, mats, s.ones(1, 1))

def zero(A):
    return all((s.expand(x) == 0 for x in A))

def simp(A):
    return A.applyfunc(s.expand)

def perm_matrix(words, p):
    ix = {w: i for i, w in enumerate(words)}
    A = s.zeros(len(words))
    inv = [p.index(i) for i in range(len(p))]
    for j, w in enumerate(words):
        A[ix[tuple((w[inv[i]] for i in range(len(p))))], j] = 1
    return A

def physical(n, cycles, pi_cycles=None, complex_case=False):
    m = sum(cycles)
    words = list(product(range(n), repeat=m))
    D = len(words)

    def cyc(ls):
        p = list(range(m))
        a = 0
        for l in ls:
            for i in range(l):
                p[a + i] = a + (i + 1) % l
            a += l
        return p
    sigma = cyc(cycles)
    pi = cyc(pi_cycles or cycles)
    Cs = perm_matrix(words, sigma)
    Cp = perm_matrix(words, pi)
    perms = [perm_matrix(words, p) for p in permutations(range(m))]
    Zall = s.Matrix.hstack(*[P.reshape(D * D, 1) for P in perms])
    Sall = Zall.T * Zall
    inds = Sall.rref()[1]
    Z = Zall[:, list(inds)]
    Sinv = (Z.T * Z).inv()
    Di = s.zeros(D * D, D)
    for i in range(D):
        Di[i * D + i, i] = 1
    Db = Di[:, :D - 1] - Di[:, D - 1] * s.ones(1, D - 1)
    H = mul(Di.T, Z, Sinv, Z.T, Di)
    Y = Db - mul(Z, mul(Sinv, mul(Z.T, Db)))
    G = Y.T * Y
    if n == 2:
        U = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)], [-s.Rational(4, 5), s.Rational(3, 5)]])
    else:
        v = s.Matrix([1, 2, 3])
        w = s.Matrix([2, 3, 1])
        U = mul(s.eye(3) - 2 * v * v.T / (v.T * v)[0], s.eye(3) - 2 * w * w.T / (w.T * w)[0])
    if complex_case:
        U = U * s.diag(*[s.I ** i for i in range(n)])
    if not zero(mul(U.H, U) - s.eye(n)):
        raise RuntimeError('Exact check failed at original line 45')
    Ub = kron(*[U] * m)
    L = mul(Cs, Ub)
    B = mul(Cp, Ub)
    acted = s.Matrix.hstack(*[mul(L, Y[:, j].reshape(D, D), B.H).reshape(D * D, 1) for j in range(D - 1)])
    direct = s.expand(s.trace(mul(G.inv(), Y.H, acted)))
    BR = s.Matrix(D, D, lambda y, x: s.prod((U[words[y][sigma[j]], words[x][j]] * s.conjugate(U[words[y][pi[j]], words[x][j]]) for j in range(m))))
    RDi = s.Matrix.hstack(*[mul(Cs, Di[:, j].reshape(D, D), Cp.T).reshape(D * D, 1) for j in range(D)])
    HR = mul(Di.T, Z, Sinv, Z.T, RDi)
    Delta = BR - HR
    Hc = H - s.ones(D, D) / D
    compressed = s.expand(s.trace(mul((s.eye(D) - Hc).inv(), Delta)))
    if not direct == compressed:
        raise RuntimeError('Exact check failed at original line 52')
    if not zero(Delta * s.ones(D, 1)):
        raise RuntimeError('Exact check failed at original line 52')
    if not zero(s.ones(1, D) * Delta):
        raise RuntimeError('Exact check failed at original line 52')
    loc = [s.eye(n)]
    for k in range(1, n):
        loc.append(s.diag(*[1] * k + [-k] + [0] * (n - k - 1)))
    supports = {}
    for w in product(range(n), repeat=m):
        if not any(w):
            continue
        support = tuple((i for i, x in enumerate(w) if x))
        z = kron(*[loc[j] for j in w]).reshape(D * D, 1)
        supports.setdefault(support, []).append(z)
    support_sum = 0
    excluded = 0
    if sigma == pi:
        for support, vectors in supports.items():
            DbS = s.Matrix.hstack(*vectors)
            YS = DbS - mul(Z, mul(Sinv, mul(Z.T, DbS)))
            actS = s.Matrix.hstack(*[mul(L, YS[:, j].reshape(D, D), B.H).reshape(D * D, 1) for j in range(YS.cols)])
            val = s.expand(s.trace(mul((YS.H * YS).inv(), YS.H, actS)))
            fixed = tuple(sorted((sigma[j] for j in support))) == support
            if not fixed:
                if not val == 0:
                    raise RuntimeError('Exact check failed at original line 68')
                excluded += 1
            support_sum += val
        if not support_sum == direct:
            raise RuntimeError('Exact check failed at original line 70')
        if n == 2:
            t = s.expand(sum((abs(U[i, 0]) ** 2 * (-1) ** i for i in range(n))))
            total = 0
            for mask in product([0, 1], repeat=len(cycles)):
                if not any(mask):
                    continue
                q = sum((l for l, yes in zip(cycles, mask) if yes))
                hq = s.Rational(1, q + 1) if q % 2 == 0 else 0
                total += (t ** q - hq) / (1 - hq)
            if not s.expand(total - direct) == 0:
                raise RuntimeError('Exact check failed at original line 77')
    RY = s.Matrix.hstack(*[mul(Cs, Y[:, j].reshape(D, D), Cp.T).reshape(D * D, 1) for j in range(Y.cols)])
    outside = RY - mul(Y, mul(G.inv(), mul(Y.H, RY)))
    witness = None
    for i, j in product(range(outside.rows), range(outside.cols)):
        if outside[i, j] != 0:
            witness = {'row': i, 'column': j, 'entry': str(outside[i, j])}
            break
    if sigma != pi:
        if not witness is not None:
            raise RuntimeError('Exact check failed at original line 84')
    out = {'N': n, 'positive_cycles': cycles, 'negative_cycles': pi_cycles or cycles, 'complex_Qi': complex_case, 'physical_End_dimension': D * D, 'invariant_rank': len(inds), 'centered_Gram_rank': G.rank(), 'direct_trace': str(direct), 'exact_compression': True, 'zero_scalar_row_and_column': True, 'excluded_supports_zero': excluded if sigma == pi else None, 'noninvariance_witness': witness}
    print('PHYSICAL', out, flush=True)
    return out

def mm(A, B):
    return [[sum((x * y for x, y in zip(row, col))) for col in zip(*B)] for row in A]

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def power(A, k):
    return reduce(mm, [A] * k, eye(len(A)))

def refl(v):
    return [[F(i == j) - F(2 * v[i] * v[j], sum((x * x for x in v))) for j in range(len(v))] for i in range(len(v))]

def tr(A):
    return sum((A[i][i] for i in range(len(A))))

def transpose(A):
    return list(map(list, zip(*A)))

def ports(n, l, r, uniform=False):
    m = l + r
    U = mm(refl(list(range(1, n + 1))), refl([i * i + 1 for i in range(n)]))
    P = [[x * x for x in row] for row in U]
    swap = list(range(n))
    swap[0], swap[1] = (1, 0)
    Q = [[F(1, n) if uniform else F(i == j, 2) + F(i == (j + 1) % n, 3) + F(i == swap[j], 6) for j in range(n)] for i in range(n)]
    if not (all((sum(row) == 1 for row in Q)) and all((sum(col) == 1 for col in zip(*Q)))):
        raise RuntimeError('Exact check failed at original line 99')
    q_normal = mm(Q, transpose(Q)) == mm(transpose(Q), Q)
    if n >= 3 and (not uniform):
        if not not q_normal:
            raise RuntimeError('Exact check failed at original line 101')
    sigma = list(range(1, l)) + [0] + list(range(l + 1, m)) + [l]
    pi = list(range(1, m)) + [0]
    words = list(product(range(n), repeat=m))
    direct = F(0)
    for x in words:
        for y in words:
            z = F(1)
            for j in range(m):
                z *= Q[x[j]][y[j]] * U[y[sigma[j]]][x[j]] * U[y[pi[j]]][x[j]]
            direct += z
    K = mm(P, Q)
    T = [[K[i][j] - F(1, n) for j in range(n)] for i in range(n)]
    W = lambda a, c, b: sum((Q[x][b] * U[a][x] * U[c][x] for x in range(n)))
    for a, c in product(range(n), repeat=2):
        if not sum((W(a, c, b) for b in range(n))) == F(a == c):
            raise RuntimeError('Exact check failed at original line 111')

    def link(A, B, distinct=False):
        return sum((A[b][a] * B[d][c] * W(a, c, b) * W(c, a, d) for a, c, b, d in product(range(n), repeat=4) if not distinct or len({a, c, b, d}) == 4))
    cut = link(power(K, l - 1), power(K, r - 1))
    E = link(power(T, l - 1), power(T, r - 1))
    expanded = F(1, n) + tr(power(T, l)) / n + tr(power(T, r)) / n + E
    if not direct == cut == expanded:
        raise RuntimeError('Exact check failed at original line 115')
    if uniform:
        if not (direct == F(1, n) and E == 0):
            raise RuntimeError('Exact check failed at original line 116')
    out = {'N': n, 'l': l, 'r': r, 'Q_uniform': uniform, 'Q_normal': q_normal, 'P_normal': mm(P, transpose(P)) == mm(transpose(P), P), 'K_normal': mm(K, transpose(K)) == mm(transpose(K), K), 'direct': str(direct), 'error': str(E), 'exact_cut_and_decomposition': True, 'distinct_ports_only': str(link(power(K, l - 1), power(K, r - 1), True))}
    print('PORTS', out, flush=True)
    return out

def shared_moments():
    moment = lambda q: F(1, q + 1) if q % 2 == 0 else F(0)
    rows = []
    for ls in [(1, 1), (2, 2), (1, 2, 3), (2, 3), (2, 2, 2)]:
        q = sum(ls)
        coupled = moment(q)
        decoupled = reduce(lambda a, b: a * b, [moment(l) for l in ls], F(1))
        rows.append({'cycles': ls, 'one_shared_draw': str(coupled), 'independent_per_cycle': str(decoupled), 'two_shared_draws': str(coupled ** 2), 'distinguishes': coupled != decoupled})
    if not (rows[0]['one_shared_draw'] == '1/3' and rows[0]['independent_per_cycle'] == '0'):
        raise RuntimeError('Exact check failed at original line 128')
    A = s.Matrix([[1, 2], [3, 4]])
    B = s.Matrix([[0, 1], [-1, 2]])
    C = s.Matrix([[2, 0], [1, 1]])
    Z = mul(A, B, C)
    for ls in [(1, 1), (2, 2), (1, 2, 3)]:
        m = sum(ls)
        words = list(product(range(2), repeat=m))
        p = list(range(m))
        off = 0
        for l in ls:
            for j in range(l):
                p[off + j] = off + (j + 1) % l
            off += l
        lhs = s.trace(perm_matrix(words, p) * kron(*[Z] * m))
        rhs = s.prod((s.trace(Z ** l) for l in ls))
        if not lhs == rhs:
            raise RuntimeError('Exact check failed at original line 136')
    return rows
