"""Exact independent controls. No imports from author or canonical verifiers."""
from itertools import product, combinations
from pathlib import Path
import json, time, sys
import sympy as s
OUT = None
REPORT = {'arithmetic': 'exact QQ and QQ(i), SymPy', 'cases': []}

def record(name, **data):
    REPORT['cases'].append({'name': name, 'passed': True, **data})
    print(name, 'PASS', flush=True)

def kron(xs):
    z = s.ones(1, 1)
    for x in xs:
        z = s.kronecker_product(z, x)
    return s.Matrix(z)

def unit(n, i, j):
    x = s.zeros(n)
    x[i, j] = 1
    return x

def tensor_cycle(d, m, reverse=False):
    words = list(product(range(d), repeat=m))
    pos = {w: i for i, w in enumerate(words)}
    R = s.zeros(d ** m)
    for j, w in enumerate(words):
        v = w[-1:] + w[:-1] if reverse else w[1:] + w[:1]
        R[pos[v], j] = 1
    return R

def local_ad(U):
    return s.kronecker_product(U, U.conjugate())

def generator(n, a, b):
    e = unit(n, a, b)
    return s.kronecker_product(e, s.eye(n)) - s.kronecker_product(s.eye(n), e.T)

def haar_lie(n, m):
    d = n * n
    I = s.eye(d)
    generators = []
    for a in range(n):
        for b in range(n):
            if a == b == n - 1:
                continue
            g = generator(n, a, b)
            generators.append(sum((kron([g if q == j else I for q in range(m)]) for j in range(m)), s.zeros(d ** m)))
    basis = s.Matrix.vstack(*generators).nullspace()
    Z = s.Matrix.hstack(*basis)
    P = Z * (Z.T * Z).inv() * Z.T
    if not (P == P.T and P * P == P):
        raise AssertionError('Exact control failed')
    if not all((g * P == s.zeros(d ** m) for g in generators)):
        raise AssertionError('Exact control failed')
    return (P, len(basis))

def projector(Y):
    basis = Y.columnspace()
    if not basis:
        return s.zeros(Y.rows)
    Z = s.Matrix.hstack(*basis)
    return Z * (Z.conjugate().T * Z).inv() * Z.conjugate().T

def full_end(n, m):
    d = n * n
    dim = d ** m
    H, h_rank = haar_lie(n, m)
    localI = s.Matrix([int(a == b) for a, b in product(range(n), repeat=2)])
    eproj = localI * localI.T / n
    vproj = s.eye(d) - eproj
    R = tensor_cycle(d, m)
    if n == 2:
        U = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)], [-s.Rational(4, 5), s.Rational(3, 5)]])
    else:
        U = s.eye(3) - s.Matrix([1, 2, 3]) * s.Matrix([[1, 2, 3]]) / 7
    C = kron([local_ad(U)] * m)
    words = list(product(range(d), repeat=m))
    by_r = {}
    raw_ranks = {}
    centered_ranks = {}
    traces = {}
    for r in range(m + 1):
        ids = []
        for k, w in enumerate(words):
            x = tuple((v // n for v in w))
            y = tuple((v % n for v in w))
            if sorted(x) == sorted(y) and sum((a != b for a, b in zip(x, y))) <= r:
                ids.append(k)
        B = s.eye(dim)[:, ids]
        P = projector((s.eye(dim) - H) * B)
        if not (P == P.T and P * P == P and (H * P == s.zeros(dim))):
            raise AssertionError('Exact control failed')
        if not R * P == P * R:
            raise AssertionError('Exact control failed')
        if r:
            Q = P - by_r[r - 1]
            if not (Q * Q == Q and Q == Q.T):
                raise AssertionError('Exact control failed')
        contributions = {}
        for mask in range(1 << m):
            S = kron([vproj if mask >> q & 1 else eproj for q in range(m)])
            if not (S * P == P * S and S * H == H * S):
                raise AssertionError('Exact control failed')
            z = s.trace(S * R * P * C)
            contributions[str(mask)] = str(z)
            if mask != (1 << m) - 1:
                if not z == 0:
                    raise AssertionError('Exact control failed')
        if not s.trace(R * P * C) == s.sympify(contributions[str((1 << m) - 1)]):
            raise AssertionError('Exact control failed')
        by_r[r] = P
        raw_ranks[r] = len(ids)
        centered_ranks[r] = int(s.trace(P))
        traces[r] = str(s.trace(R * P * C))
    if not by_r[0] == by_r[1]:
        raise AssertionError('Exact control failed')
    Pi = s.diag(*[int(sorted(tuple((v // n for v in w))) == sorted(tuple((v % n for v in w)))) for w in words])
    if not (Pi * H == H and by_r[m] == Pi - H):
        raise AssertionError('Exact control failed')
    for r, P in by_r.items():
        Q = P - by_r[0]
        rem = Pi - H - P
        if not (Q * rem == s.zeros(dim) and rem * rem == rem):
            raise AssertionError('Exact control failed')
    record('literal_End', N=n, m=m, end_dimension=dim, haar_rank=h_rank, raw_ranks=raw_ranks, centered_ranks=centered_ranks, cyclic_traces=traces, invariant_construction='common exact Lie-generator kernel; no permutation Gram input')

def top_four():
    I = s.I
    paulis = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]

    def adj(U):
        return s.Matrix(3, 3, lambda i, j: s.trace(paulis[i] * U * paulis[j] * U.conjugate().T) / 2)
    U = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)], [-s.Rational(4, 5), s.Rational(3, 5)]])
    A = adj(U)
    m = 4
    D = 3
    ws = list(product(range(3), repeat=m))
    pairs = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    Z = s.Matrix([[int(all((w[a] == w[b] for a, b in p))) for p in pairs] for w in ws])
    H = Z * (Z.T * Z).inv() * Z.T
    gs = [unit(3, a, b) - unit(3, b, a) for a, b in combinations(range(3), 2)]
    GG = s.Matrix.vstack(*[sum((kron([g if i == j else s.eye(3) for i in range(m)]) for j in range(m)), s.zeros(81)) for g in gs])
    if not (GG.rank() == 78 and GG * Z == s.zeros(243, 3)):
        raise AssertionError('Exact control failed')
    off = [s.Matrix([1, I, 0]) / 2, s.Matrix([1, -I, 0]) / 2]
    diag = s.Matrix([0, 0, 1])
    cols = [kron([diag] * m)]
    labels = [()]
    for a, b in combinations(range(m), 2):
        for sign in range(2):
            cols.append(kron([off[sign] if j == a else off[1 - sign] if j == b else diag for j in range(m)]))
            labels.append((a, b, sign))
    Kbasis = s.Matrix.hstack(*cols)
    metric = Kbasis.conjugate().T * Kbasis
    K = Kbasis * metric.inv() * Kbasis.conjugate().T
    hc = metric.inv() * Kbasis.conjugate().T * H * Kbasis
    G = s.eye(len(cols)) - hc
    if not G.det() != 0:
        raise AssertionError('Exact control failed')
    Y = (s.eye(81) - H) * Kbasis
    P = Y * (metric * G).inv() * Y.conjugate().T
    if not (P == projector(Y) and P * P == P):
        raise AssertionError('Exact control failed')
    R = tensor_cycle(3, m)
    C = kron([A] * m)
    rr = metric.inv() * Kbasis.conjugate().T * R * Kbasis
    bc = metric.inv() * Kbasis.conjugate().T * C * Kbasis
    lhs = s.trace(R * P * C)
    rhs = s.trace(rr * G.inv() * (bc - hc))
    if not s.simplify(lhs - rhs) == 0:
        raise AssertionError('Exact control failed')
    rawsub = s.trace(R * (K - H) * C)
    if not s.simplify(lhs - rawsub) != 0:
        raise AssertionError('Exact control failed')
    record('nonvacuous_top_Gram_N2_m4_r2', dimension=81, raw_rank=13, haar_rank=3, gram_determinant=str(s.factor(G.det())), haar_compression_eigenvalues={str(k): v for k, v in hc.eigenvals().items()}, correct_trace=str(s.factor(lhs)), incorrect_raw_minus_H_trace=str(s.factor(rawsub)), note='m-2r=0: valid Gram-identity control, explicitly outside inequality (1) hypothesis')

def marker_enumeration():
    rows = []
    for n in (2, 3, 4):
        off = [(a, b) for a in range(n) for b in range(n) if a != b]
        counts = []
        for degree in range(5):
            c = 0
            for colors in product(off, repeat=degree):
                charge = [0] * n
                for a, b in colors:
                    charge[a] += 1
                    charge[b] -= 1
                c += all((q == 0 for q in charge))
            counts.append(c)
            if not c <= s.factorial(degree) * n ** degree:
                raise AssertionError('Exact control failed')
        if not counts[:3] == [1, 0, n * (n - 1)]:
            raise AssertionError('Exact control failed')
        rows.append({'N': n, 'b_0_through_4': counts})
    record('balanced_marker_counts', rows=rows)

def noncommutative_seam():
    I = s.I
    p = s.diag(0, 0, 1)
    plus = s.Matrix([1, I, 0])
    minus = plus.conjugate()
    qplus = plus * plus.conjugate().T / 2
    qminus = minus * minus.conjugate().T / 2
    P = [p, qplus, qminus]
    Ax = s.Matrix([[1, 0, 0], [0, s.Rational(7, 25), -s.Rational(24, 25)], [0, s.Rational(24, 25), s.Rational(7, 25)]])
    Az = s.Matrix([[s.Rational(119, 169), -s.Rational(120, 169), 0], [s.Rational(120, 169), s.Rational(119, 169), 0], [0, 0, 1]])
    Ay = s.Matrix([[s.Rational(527, 625), 0, s.Rational(336, 625)], [0, 1, 0], [-s.Rational(336, 625), 0, s.Rational(527, 625)]])
    mats = [Ax, Az, Ay]
    m = 3
    R = tensor_cycle(3, m)
    patterns = [(0, 0, 0)] + [w for w in product(range(3), repeat=m) if w.count(1) == 1 and w.count(2) == 1]
    K = sum((kron([P[x] for x in w]) for w in patterns), s.zeros(27))
    if not (K * K == K and len(patterns) == 7):
        raise AssertionError('Exact control failed')
    results = []
    found = None
    for stages in (1, 2, 3):
        As = mats[:stages]
        M = s.eye(27)
        for A in As:
            M = M * K * kron([A] * m)
        full = s.simplify(s.trace(R * M))
        summed = 0
        for choices in product(patterns, repeat=stages):
            blocks = []
            for slot in range(m):
                X = s.eye(3)
                for ell, A in enumerate(As):
                    X = (X * P[choices[ell][slot]] * A).applyfunc(s.expand)
                blocks.append(X)
            W = s.eye(3)
            for X in blocks:
                W = (W * X).applyfunc(s.expand)
            contracted = s.trace(W)
            compressed = s.eye(3)
            for slot in range(m):
                for ell, A in enumerate(As):
                    qnext = P[choices[ell + 1][slot]] if ell + 1 < stages else P[choices[0][(slot + 1) % m]]
                    compressed = (compressed * P[choices[ell][slot]] * A * qnext).applyfunc(s.expand)
            if not s.simplify(contracted - s.trace(compressed)) == 0:
                raise AssertionError('Exact control failed')
            summed = s.expand(summed + contracted)
            if stages == 1 and found is None:
                wrong = s.eye(3)
                for slot in range(m):
                    wrong = wrong * P[choices[0][slot]] * As[0] * P[choices[0][slot]]
                wt = s.trace(wrong)
                if s.simplify(contracted - wt) != 0:
                    found = {'pattern': choices, 'correct': str(s.simplify(contracted)), 'unshifted': str(s.simplify(wt))}
        if not s.simplify(full - summed) == 0:
            raise AssertionError('Exact control failed')
        results.append({'stages': stages, 'summands': len(patterns) ** stages, 'trace': str(s.simplify(full))})
    if not found is not None:
        raise AssertionError('Exact control failed')
    xs = [s.Matrix([[1, 2, 0], [0, 1, 3], [2, 0, 1]]), s.Matrix([[2, 0, 1], [1, 3, 0], [0, 2, 1]]), s.Matrix([[1, 1, 0], [2, 1, 1], [0, 3, 2]])]
    if not s.trace(R * kron(xs)) == s.trace(xs[0] * xs[1] * xs[2]):
        raise AssertionError('Exact control failed')
    if not s.trace(R.T * kron(xs)) == s.trace(xs[2] * xs[1] * xs[0]):
        raise AssertionError('Exact control failed')
    if not s.trace(xs[0] * xs[1] * xs[2]) != s.trace(xs[2] * xs[1] * xs[0]):
        raise AssertionError('Exact control failed')
    record('noncommutative_seam_and_full_color_sum', rows=results, wrong_seam_counterexample=found, orientations=[str(s.trace(R * kron(xs))), str(s.trace(R.T * kron(xs)))], note='Exact deterministic integrands, not Haar-moment sampling. Stages correspond to j+1 retained K factors.')
def main():
    global OUT
    if len(sys.argv) != 3 or sys.argv[1] != '--output':
        raise ValueError('Expected --output PATH')
    OUT = Path(sys.argv[2])
    start = time.time()
    full_end(2, 1)
    full_end(2, 3)
    full_end(3, 2)
    top_four()
    marker_enumeration()
    noncommutative_seam()
    REPORT['runtime_seconds'] = time.time() - start
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(REPORT, indent=2) + '\n')
    print('COMPLETE', str(OUT), REPORT['runtime_seconds'], flush=True)

if __name__ == '__main__':
    main()
