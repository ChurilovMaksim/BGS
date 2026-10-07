"""Portable exact bounded replay; scientific logic retained from frozen source.
Every former assert is an explicit conditional raise and survives python -O.
Imports and the no-argument main are silent and do not write files.
"""
import itertools as it, json, time
from pathlib import Path
import sympy as s
I = s.I

def clean(A):
    return A.applyfunc(s.expand)

def mm(*args):
    z = args[0]
    for x in args[1:]:
        z = clean(z * x)
    return z

def tr(A):
    return s.expand(s.trace(A))

def zero(A):
    if not clean(A) == s.zeros(*A.shape):
        raise AssertionError('Exact check failed at original line 20')

def kron(xs):
    z = s.ones(1, 1)
    for x in xs:
        z = s.kronecker_product(z, x)
    return z

def cycle(d, m):
    ts = list(it.product(range(d), repeat=m))
    ix = {t: i for i, t in enumerate(ts)}
    R = s.zeros(len(ts))
    for j, t in enumerate(ts):
        R[ix[t[1:] + t[:1]], j] = 1
    return R

def local_ad(U):
    return clean(s.kronecker_product(U, s.conjugate(U)))

def local_comm(H):
    return s.kronecker_product(H, s.eye(H.rows)) - s.kronecker_product(s.eye(H.rows), H.T)

def sum_legs(A, m):
    d = A.rows
    return sum((kron([A if j == i else s.eye(d) for j in range(m)]) for i in range(m)), s.zeros(d ** m))

def haar_from_generators(N, m, B=None):
    """Literal common commutant of matrix units, not a permutation frame."""
    basis = []
    for a in range(N):
        for b in range(N):
            h = s.zeros(N)
            h[a, b] = 1
            basis.append(local_comm(h))
    if B is None:
        d = N * N
        G = s.eye(d ** m)
    else:
        g = B.conjugate().T * B
        left = g.inv() * B.conjugate().T
        basis = [clean(left * A * B) for A in basis]
        d = B.cols
        G = kron([g] * m)
    L = s.Matrix.vstack(*[sum_legs(h, m) for h in basis])
    ns = L.nullspace()
    Z = s.Matrix.hstack(*ns) if ns else s.zeros(d ** m, 0)
    H = mm(Z, (Z.conjugate().T * G * Z).inv(), Z.conjugate().T, G) if ns else s.zeros(d ** m)
    zero(mm(H, H) - H)
    zero(H.conjugate().T * G - G * H)
    zero(L * H)
    return (H, G, len(ns))

def range_projection(Y, G=None):
    G = s.eye(Y.rows) if G is None else G
    cols = Y.columnspace()
    if not cols:
        return s.zeros(Y.rows)
    Z = s.Matrix.hstack(*cols)
    return mm(Z, (Z.conjugate().T * G * Z).inv(), Z.conjugate().T, G)

def local_projections(N):
    d = N * N
    diag = [i * N + i for i in range(N)]
    E = s.zeros(d)
    for i in diag:
        for j in diag:
            E[i, j] = s.Rational(1, N)
    D = s.diag(*[int(a == b) for a in range(N) for b in range(N)])
    return (E, D - E, s.eye(d) - D)

def hamming_and_balance(N, m):
    pairs = list(it.product(range(N), repeat=2))
    ts = list(it.product(range(N * N), repeat=m))
    distances = []
    balanced = []
    for t in ts:
        charge = [0] * N
        dist = 0
        for j in t:
            a, b = pairs[j]
            charge[a] += 1
            charge[b] -= 1
            dist += int(a != b)
        distances.append(dist)
        balanced.append(int(not any(charge)))
    return (distances, s.diag(*balanced))

def unitary(N):
    if N == 2:
        return s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)], [-s.Rational(4, 5), s.Rational(3, 5)]])
    v = s.Matrix([1, 2, 3])
    Q = s.eye(3) - v * v.T / s.Integer(7)
    return s.diag(1, I, (3 + 4 * I) / 5) * Q

def full_end_controls():
    rows = []
    for N, m in [(2, 1), (2, 2), (2, 3), (3, 2)]:
        d = N * N
        dim = d ** m
        R = cycle(d, m)
        U = unitary(N)
        zero(U.conjugate().T * U - s.eye(N))
        C = kron([local_ad(U)] * m)
        H, G, hrank = haar_from_generators(N, m)
        ds, Pi = hamming_and_balance(N, m)
        zero(Pi * H - H)
        E, p, q = local_projections(N)
        V = s.eye(d) - E
        supports = []
        for flags in it.product([0, 1], repeat=m):
            supports.append((flags, kron([V if f else E for f in flags])))
        zero(s.Matrix([[tr(mm(R, C)) - s.expand(abs(tr(U ** m)) ** 2)]]))
        prev = s.zeros(dim)
        for r in range(m + 1):
            F = s.diag(*[int(x <= r) for x in ds])
            K = Pi * F
            O = F - K
            P = K + range_projection((s.eye(dim) - K) * H) - H
            Pt = F + range_projection((s.eye(dim) - F) * H) - H
            zero(P * ((s.eye(dim) - H) * K) - (s.eye(dim) - H) * K)
            zero(Pt * ((s.eye(dim) - H) * F) - (s.eye(dim) - H) * F)
            if dim <= 16:
                zero(P - range_projection((s.eye(dim) - H) * K))
                zero(Pt - range_projection((s.eye(dim) - H) * F))
            zero(Pt - P - O)
            zero(mm(P, P) - P)
            zero(mm(Pt, Pt) - Pt)
            zero(mm(O, O) - O)
            zero(P.conjugate().T - P)
            zero(Pt.conjugate().T - Pt)
            zero(H * Pt)
            zero(P * O)
            zero(Pi * P - P)
            zero(Pi * O)
            zero(R * Pt - Pt * R)
            Q = P - prev
            zero(Q * Q - Q)
            prev = P
            res = s.eye(dim) - H - Pt
            balres = Pi - H - P
            offres = s.eye(dim) - Pi - O
            zero(res - balres - offres)
            zero(res * res - res)
            zero(balres * offres)
            support_vanish = 0
            for flags, S in supports:
                zero(S * P - P * S)
                zero(S * Pt - Pt * S)
                zero(S * O - O * S)
                if sum(flags) < m:
                    for proj in [P, Pt, O]:
                        if not tr(mm(R, proj, C, S)) == 0:
                            raise AssertionError('Exact check failed at original line 117')
                    support_vanish += 1
            vals = {'N': N, 'm': m, 'r': r, 'raw_rank': int(tr(F)), 'balanced_raw_rank': int(tr(K)), 'haar_rank': hrank, 'balanced_centered_rank': int(tr(P)), 'all_centered_rank': int(tr(Pt)), 'offcharge_rank': int(tr(O)), 'balanced_trace': str(tr(mm(R, P, C))), 'all_trace': str(tr(mm(R, Pt, C))), 'offcharge_trace': str(tr(mm(R, O, C))), 'proper_and_empty_support_blocks_checked': support_vanish}
            if not tr(mm(R, Pt, C)) == tr(mm(R, P, C)) + tr(mm(R, O, C)):
                raise AssertionError('Exact check failed at original line 124')
            rows.append(vals)
    return rows

def top_gram_control():
    N, m, r = (2, 4, 2)
    B = s.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, -1]])
    H, G, hrank = haar_from_generators(N, m, B)
    left = (B.conjugate().T * B).inv() * B.conjugate().T
    A = clean(left * local_ad(unitary(N)) * B)
    C = kron([A] * m)
    R = cycle(3, m)
    ts = list(it.product(range(3), repeat=m))
    F = s.diag(*[int(sum((j != 2 for j in t)) <= r) for t in ts])
    Pi = s.diag(*[int(sum((1 if j == 0 else -1 if j == 1 else 0 for j in t)) == 0) for t in ts])
    K = F * Pi
    rows = []
    for name, L in [('balanced', K), ('all', F)]:
        ix = [i for i in range(3 ** m) if L[i, i]]
        HH = H.extract(ix, ix)
        CC = C.extract(ix, ix)
        RR = R.extract(ix, ix)
        Gram = s.eye(len(ix)) - HH
        det = Gram.det()
        if not det != 0:
            raise AssertionError('Exact check failed at original line 139')
        Y = (s.eye(3 ** m) - H)[:, ix]
        PP = range_projection(Y, G)
        literal = tr(mm(R, PP, C))
        formula = tr(mm(RR, Gram.inv(), CC - HH))
        if not literal == formula:
            raise AssertionError('Exact check failed at original line 141')
        wrong = tr(mm(R, L - H, C))
        if not wrong != literal:
            raise AssertionError('Exact check failed at original line 142')
        rows.append({'range': name, 'raw_top_rank': len(ix), 'haar_top_rank': hrank, 'gram_determinant': str(det), 'literal_trace': str(literal), 'gram_trace': str(formula), 'invalid_raw_minus_haar_trace': str(wrong)})
    return rows

def torus_controls():
    rows = []
    for N, m in [(2, 3), (3, 2)]:
        d = N * N
        E, p, q = local_projections(N)
        V = s.eye(d) - E
        ds, Pi = hamming_and_balance(N, m)
        top = kron([V] * m)
        phases = [1, I, -1, -I]
        avg = s.zeros(d ** m)
        for zrest in it.product(phases, repeat=N - 1):
            Dz = local_ad(s.diag(1, *zrest))
            avg += kron([Dz] * m)
        avg /= 4 ** (N - 1)
        zero(avg - Pi)
        for r in range(m + 1):
            F = s.diag(*[int(x <= r) for x in ds])
            Jsum = s.zeros(d ** m)
            Ksum = s.zeros(d ** m)
            nonzero = 0
            for S in it.chain.from_iterable((it.combinations(range(m), h) for h in range(r + 1))):
                J = kron([q if i in S else p for i in range(m)])
                Jsum += J
                Ksum += Pi * J
                nonzero += int(Pi * J != s.zeros(d ** m))
            zero(Jsum - top * F)
            zero(Ksum - top * Pi * F)
            rows.append({'N': N, 'm': m, 'r': r, 'position_blocks': sum((s.binomial(m, h) for h in range(r + 1))), 'nonzero_balanced_blocks': nonzero, 'rank_p': int(tr(p)), 'rank_q': int(tr(q)), 'exact_phase_samples': 4 ** (N - 1)})
    return rows

def network_controls():
    rows = []
    witness = None
    for N, m in [(2, 3), (3, 2)]:
        d = N * N
        E, p, q = local_projections(N)
        R = cycle(d, m)
        U0 = unitary(N)
        Z1 = s.diag(*[1, (3 + 4 * I) / 5] + ([I] if N == 3 else []))
        Z2 = s.diag(*[I, 1] + ([(5 + 12 * I) / 13] if N == 3 else []))
        Us = [U0, clean(Z1 * U0.T), clean(U0 * Z2 * U0)]
        As = [local_ad(u) for u in Us]
        Dz = [local_ad(z) for z in [Z1, Z2, clean(Z1 * Z2)]]
        if not mm(As[0], As[1]) != mm(As[1], As[0]):
            raise AssertionError('Exact check failed at original line 179')
        for k in [1, 2, 3]:
            sets = [{0}, {m - 1}, {0, m - 1}][:k]
            ps = [[q if i in S else p for i in range(m)] for S in sets]
            Xi = [mm(*list(it.chain.from_iterable(((ps[l][i], Dz[l], As[l]) for l in range(k))))) for i in range(m)]
            literal = tr(mm(R, kron(Xi)))
            local = tr(mm(*Xi))
            if not literal == local:
                raise AssertionError('Exact check failed at original line 183')
            factors = []
            wrong = []
            for i in range(m):
                for l in range(k):
                    dest = ps[l + 1][i] if l + 1 < k else ps[0][(i + 1) % m]
                    factors.append(mm(ps[l][i], Dz[l], As[l], dest))
                    wrong.append(mm(ps[l][i], Dz[l], As[l], ps[(l + 1) % k][i]))
            compressed = tr(mm(*factors))
            if not compressed == literal:
                raise AssertionError('Exact check failed at original line 190')
            bad = tr(mm(*wrong))
            if bad != literal and witness is None:
                witness = {'N': N, 'm': m, 'k': k, 'correct': str(literal), 'unshifted_seam': str(bad)}
            rows.append({'N': N, 'm': m, 'stages': k, 'literal_tensor_trace': str(literal), 'local_cycle_trace': str(local), 'duplicated_projection_trace': str(compressed), 'unshifted_seam_trace': str(bad)})
    if not witness is not None:
        raise AssertionError('Exact check failed at original line 194')
    Xs = [s.Matrix([[1, 2], [0, 1]]), s.Matrix([[0, 1], [2, 3]]), s.Matrix([[2, 0], [1, 4]])]
    R = cycle(2, 3)
    forward = tr(mm(R, kron(Xs)))
    backward = tr(mm(R.T, kron(Xs)))
    if not forward == tr(mm(*Xs)):
        raise AssertionError('Exact check failed at original line 198')
    if not backward == tr(mm(*Xs[::-1])):
        raise AssertionError('Exact check failed at original line 198')
    if not forward != backward:
        raise AssertionError('Exact check failed at original line 198')
    return {'stage_tests': rows, 'seam_failure_witness': witness, 'orientation': {'forward': str(forward), 'backward': str(backward)}}

def exact_offcharge_bound():
    rows = []
    B = s.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, -1]])
    left = (B.T * B).inv() * B.T
    U = unitary(2)
    A = clean(left * local_ad(U) * B)
    t = abs(2 * U[0, 0] ** 2 - 1)
    for m in range(1, 7):
        R = cycle(3, m)
        ts = list(it.product(range(3), repeat=m))
        for r in range(m // 2 + 1):
            val = 0
            count = 0
            for x in ts:
                y = x[-1:] + x[:-1]
                if sum((j != 2 for j in y)) > r or sum((1 if j == 0 else -1 if j == 1 else 0 for j in y)) == 0:
                    continue
                val += s.prod((A[y[i], x[i]] for i in range(m)))
                count += 1
            val = s.expand(val)
            n = m - 2 * r
            M = sum((s.binomial(m, h) for h in range(r + 1)))
            bound = 6 * M * t ** n
            if not abs(val) <= bound:
                raise AssertionError('Exact check failed at original line 219')
            rows.append({'m': m, 'r': r, 'n': n, 't': str(t), 'M': int(M), 'offcharge_trace': str(val), 'bound': str(bound), 'literal_basis_terms': count})
    return rows

def run_checks():
    data = {}
    for name, fn in [('full_end', full_end_controls), ('top_gram', top_gram_control), ('torus', torus_controls), ('network', network_controls), ('offcharge_bound', exact_offcharge_bound)]:
        data[name] = fn()
    return data


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--inject-failure', action='store_true')
    args = parser.parse_args(argv)
    if args.inject_failure:
        raise AssertionError('Deliberate portability failure control')
    if args.output is not None:
        result = run_checks()
        args.output.write_text(json.dumps(result, indent=2, default=str) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
