"""Independent exact finite controls. No imports from author code. Q and all U in Q(i)."""
from itertools import product, permutations, combinations
from fractions import Fraction as F
from pathlib import Path
import sympy as S
import json, math, time
I = S.I

def compositions(m):
    if not m:
        yield ()
        return
    for x in range(1, m + 1):
        for tail in compositions(m - x):
            yield ((x,) + tail)

def perm(lens):
    out = []
    s = 0
    for q in lens:
        out.extend(list(range(s + 1, s + q)) + [s])
        s += q
    return out

def slot(p, n):
    words = list(product(range(n), repeat=len(p)))
    idx = {w: i for i, w in enumerate(words)}
    A = S.zeros(len(words))
    for j, w in enumerate(words):
        v = list(w)
        for a, b in enumerate(p):
            v[b] = w[a]
        A[idx[tuple(v)], j] = 1
    return A

def kron(A, m):
    R = S.ones(1)
    for _ in range(m):
        R = S.kronecker_product(R, A)
    return R

def fixture(n, complex_case=False):
    v = S.Matrix(list(range(1, n + 1)))
    w = S.Matrix(list(range(n, 0, -1)))
    A = S.eye(n) - 2 * v * v.T / (v.T * v)[0]
    B = S.eye(n) - 2 * w * w.T / (w.T * w)[0]
    U = A * B
    if complex_case:
        D = S.diag(*[(3 + 4 * I) / 5] + [1] * (n - 1))
        E = S.diag(*[1] * (n - 1) + [(5 + 12 * I) / 13])
        U = D * U * E
    if not S.simplify(U * U.H) == S.eye(n):
        raise RuntimeError('Exact check failed at original line 37')
    cyc = slot([(i + 1) % 1 for i in range(1)], n) if False else S.zeros(n)
    swap = S.eye(n)
    swap.row_swap(0, 1)
    for j in range(n):
        cyc[(j + 1) % n, j] = 1
    Q = (S.eye(n) + 2 * cyc + 3 * swap) / 6
    if not (list(Q * S.ones(n, 1)) == [1] * n and list(Q.T * S.ones(n, 1)) == [1] * n):
        raise RuntimeError('Exact check failed at original line 42')
    if n == 3:
        if not Q * Q.T != Q.T * Q:
            raise RuntimeError('Exact check failed at original line 43')
    return (U, Q)

def topology(p, q):
    sig, pi = (perm(p), perm(q))
    ends = sorted(set([sum(p[:j]) for j in range(1, len(p) + 1)] + [sum(q[:j]) for j in range(1, len(q) + 1)]))
    starts = [0] + ends[:-1]
    L = [e - s - 1 for e, s in zip(ends, starts)]
    alpha = [starts.index(sig[e - 1]) for e in ends]
    beta = [starts.index(pi[e - 1]) for e in ends]
    if not (sorted(alpha) == list(range(len(ends))) and sorted(beta) == list(range(len(ends)))):
        raise RuntimeError('Exact check failed at original line 49')
    edges = {x: sig[x] for x in range(sum(p)) if sig[x] == pi[x] and x + 1 not in ends}
    visited = set()
    for start, end in zip(starts, ends):
        x = start
        while True:
            if not x not in visited:
                raise RuntimeError('Exact check failed at original line 55')
            visited.add(x)
            if x not in edges:
                if not x == end - 1:
                    raise RuntimeError('Exact check failed at original line 56')
                break
            x = edges[x]
    if not visited == set(range(sum(p))):
        raise RuntimeError('Exact check failed at original line 58')
    return (L, alpha, beta)

def network(U, Q, p, q):
    n = U.rows
    L, a, b = topology(p, q)
    h = len(L)
    P = U.multiply_elementwise(U.conjugate())
    K = P * Q
    links = [K ** l for l in L]
    W = {(r, s, t): S.expand(sum((Q[x, t] * U[r, x] * S.conjugate(U[s, x]) for x in range(n)))) for r, s, t in product(range(n), repeat=3)}
    out = 0
    for v in product(range(n), repeat=h):
        for z in product(range(n), repeat=h):
            t = 1
            for j in range(h):
                t *= links[j][z[j], v[j]] * W[v[a[j]], v[b[j]], z[j]]
                if not t:
                    break
            out += t
    return S.expand(out)

def cycles(p):
    seen = set()
    ans = 0
    for x in range(len(p)):
        if x in seen:
            continue
        ans += 1
        while x not in seen:
            seen.add(x)
            x = p[x]
    return ans

def direct(U, Q, p, q):
    n = U.rows
    m = sum(p)
    T = kron(U, m)
    A = slot(perm(p), n) * T
    B = slot(perm(q), n) * T
    BR = A.multiply_elementwise(B.conjugate())
    return S.expand(S.trace(kron(Q, m) * BR))

def network_cases():
    out = []
    for n, cap in [(2, 4), (3, 3)]:
        U, Q = fixture(n)
        for m in range(1, cap + 1):
            for p in compositions(m):
                for q in compositions(m):
                    got = network(U, Q, p, q)
                    if not got == direct(U, Q, p, q):
                        raise RuntimeError('Exact check failed at original line 94')
                    sig, pi = (perm(p), perm(q))
                    rel = [sig[pi.index(i)] for i in range(m)]
                    J = S.ones(n) / n
                    uniform = network(U, J, p, q)
                    if not uniform == S.Rational(n) ** (cycles(rel) - m):
                        raise RuntimeError('Exact check failed at original line 96')
                    L, alpha, beta = topology(p, q)
                    h = len(L)
                    if not cycles(rel) - m == cycles([alpha[beta.index(j)] for j in range(h)]) - h:
                        raise RuntimeError('Exact check failed at original line 98')
                    C = n * max((x * x for x in U))
                    if not abs(got) <= C ** (2 * h - L.count(0)):
                        raise RuntimeError('Exact check failed at original line 99')
                    out.append({'N': n, 'positive': p, 'negative': q, 'h': h, 'zero_strings': L.count(0), 'Q_nonnormal': Q * Q.T != Q.T * Q, 'F_Q': str(got), 'F_J': str(uniform)})
    U, Q = fixture(3, True)
    p = (1, 2)
    q = (3,)
    if not network(U, Q, p, q) == direct(U, Q, p, q):
        raise RuntimeError('Exact check failed at original line 101')
    return {'cases': out, 'complex_rational_case': {'N': 3, 'positive': p, 'negative': q, 'F_Q': str(network(U, Q, p, q))}, 'count': len(out) + 1}

def full_gram(n, p, q, complex_case=False):
    U, Q = fixture(n, complex_case)
    m = sum(p)
    d = n ** m
    vec = lambda X: S.Matrix(X).reshape(d * d, 1)
    invs = [slot(x, n) for x in permutations(range(m))]
    cols = S.Matrix.hstack(*[vec(X) for X in invs])
    _, pivots = cols.rref()
    A = cols[:, list(pivots)]
    ga = (A.H * A).inv()
    diags = S.zeros(d * d, d)
    for j in range(d):
        diags[j * d + j, j] = 1
    Yraw = diags - A * ga * A.H * diags
    basis = S.zeros(d, d - 1)
    for j in range(d - 1):
        basis[j, j] = 1
        basis[d - 1, j] = -1
    Y = Yraw * basis
    G = Y.H * Y
    ginv = G.inv()
    if not G.det() != 0:
        raise RuntimeError('Exact check failed at original line 110')
    T = kron(U, m)
    Sig = slot(perm(p), n)
    Pi = slot(perm(q), n)
    action = lambda X: T * Sig * X * Pi.H * T.H
    CY = S.Matrix.hstack(*[vec(action(Y[:, j].reshape(d, d))) for j in range(d - 1)])
    direct_s = S.simplify(S.trace(ginv * Y.H * CY))
    H = diags.H * A * ga * A.H * diags
    P0 = S.ones(d) / d
    Hc = H - P0
    BR = (T * Sig).multiply_elementwise((T * Pi).conjugate())
    Rdiags = S.Matrix.hstack(*[vec(Sig * diags[:, j].reshape(d, d) * Pi.H) for j in range(d)])
    HR = diags.H * A * ga * A.H * Rdiags
    D = S.simplify(BR - HR)
    if not (D * S.ones(d, 1) == S.zeros(d, 1) and S.ones(1, d) * D == S.zeros(1, d)):
        raise RuntimeError('Exact check failed at original line 118')
    compression = S.simplify(S.trace((S.eye(d) - Hc).inv() * D))
    if not compression == direct_s:
        raise RuntimeError('Exact check failed at original line 119')
    partial = sum((S.trace(Hc ** j * D) for j in range(4)))
    tail = S.trace(Hc ** 4 * (S.eye(d) - Hc).inv() * D)
    if not S.simplify(partial + tail - direct_s) == 0:
        raise RuntimeError('Exact check failed at original line 120')
    for j in range(4):
        if not S.simplify(S.trace((H ** j - Hc ** j) * D)) == 0:
            raise RuntimeError('Exact check failed at original line 121')
    Pord_action = lambda Z: Y * ginv * Y.H * Z
    RY = S.Matrix.hstack(*[vec(Sig * Y[:, j].reshape(d, d) * Pi.H) for j in range(d - 1)])
    invariant = S.simplify(RY - Pord_action(RY)) == S.zeros(d * d, d - 1)
    return {'N': n, 'positive': p, 'negative': q, 'complex_rational': complex_case, 'Haar_rank': len(pivots), 'ordered_rank': d - 1, 'R_preserves_ordered_sector': invariant, 'exact_s_R': str(direct_s), 'exact_Gram_and_four_term_remainder': True}

def partitions(k):
    if not k:
        yield []
        return
    for p in partitions(k - 1):
        for j in range(len(p)):
            yield (p[:j] + [p[j] + [k - 1]] + p[j + 1:])
        yield (p + [[k - 1]])

def mobius_rank():
    counts = {}
    strata = 0
    allzero = 0
    for k in range(2, 8):
        ps = list(partitions(k))
        counts[k] = len(ps)
        for p in ps:
            b = len(p)
            rows = []
            for B in p:
                rows.append([int(j in B) - int(k - 1 in B) for j in range(k - 1)])
            if not S.Matrix(rows).rank() == b - 1:
                raise RuntimeError('Exact check failed at original line 140')
            allzero += 1
            for z in range(max(0, b - 1)):
                for selected in combinations(range(b), z):
                    if not (S.Matrix([rows[j] for j in selected]).rank() if z else 0) == z:
                        raise RuntimeError('Exact check failed at original line 143')
                    strata += 1
    examples = []
    U, _ = fixture(3)
    N = U.rows
    for k, m in [(2, (0, 0)), (2, (1, -1)), (3, (1, -1, 0)), (4, (1, 1, -1, -1)), (4, (0, 0, 0, 0))]:
        vals = [S.Rational(1), S.Rational(-1), I]
        trace = lambda a: sum((v ** a for v in vals))
        direct = sum((S.prod((vals[j] ** a for j, a in zip(indices, m))) for indices in permutations(range(N), k)))
        expanded = 0
        for p in partitions(k):
            mu = math.prod(((-1) ** (len(B) - 1) * math.factorial(len(B) - 1) for B in p))
            expanded += mu * S.prod((trace(sum((m[j] for j in B))) for B in p))
        if not S.simplify(direct - expanded) == 0:
            raise RuntimeError('Exact check failed at original line 154')
        examples.append({'k': k, 'm': m, 'value': str(S.simplify(direct))})
    return {'Bell_counts': counts, 'proper_zero_strata_checked': strata, 'all_zero_rank_cases': allzero, 'literal_Mobius_examples': examples}

def exact_haar_second():
    out = []
    for n in range(2, 9):
        EPP = S.Matrix(n, n, lambda a, b: S.Rational(2 if a == b else 1, n + 1))
        J = S.ones(n) / n
        if not EPP - J == (S.eye(n) - J) / (n + 1):
            raise RuntimeError('Exact check failed at original line 161')
        for j in range(8):
            if not S.Rational(n - 1, (n + 1) ** j) == (n - 1) * S.Rational(1, n + 1) ** j:
                raise RuntimeError('Exact check failed at original line 162')
        out.append({'N': n, 'full_mean_zero_covariance_verified': True, 'product_lengths_through': 7})
    return out

def run():
    start = time.monotonic()
    net = network_cases()
    grams = []
    for spec in [(2, (1,), (1,), False), (2, (1, 1), (2,), True), (3, (1, 1), (2,), False), (2, (1, 2), (3,), False), (3, (1, 2), (3,), False)]:
        grams.append(full_gram(*spec))
        print('Gram passed', spec, flush=True)
    result = {'status': 'all_passed', 'arithmetic': 'exact rational and Gaussian-rational; SymPy exact linear algebra', 'network': net, 'gram': grams, 'factorial': mobius_rank(), 'Haar_second': exact_haar_second(), 'seconds': time.monotonic() - start, 'nonclaims': 'Finite checks do not prove the universal theorem, actual-map flatness, or the residual BGS comparison.'}
    return result
