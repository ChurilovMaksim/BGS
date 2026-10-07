"""Portable exact bounded replay; scientific logic retained from frozen source.
Every former assert is an explicit conditional raise and survives python -O.
Imports and the no-argument main are silent and do not write files.
"""
import itertools as it, json, math, sys, time
from pathlib import Path
from fractions import Fraction
import sympy as sp

def basis(N):
    mats = []
    charges = []
    off = []
    for k in range(1, N):
        mats.append(sp.diag(*[1] * k + [-k] + [0] * (N - k - 1)))
        charges.append((0,) * (N - 1))
        off.append(0)
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            E = sp.zeros(N)
            E[a, b] = 1
            mats.append(E)
            off.append(1)
            charges.append(tuple((int(j == a) - int(j == b) for j in range(N - 1))))
    return (mats, charges, off)

def adj_integer(U, bs):
    A = sp.Matrix([[sp.trace(x.T * U * y * U.T) / sp.trace(x.T * x) for y in bs] for x in bs])
    den = sp.ilcm(*[v.q for v in A])
    return ([[int(v * den) for v in row] for row in A.tolist()], int(den))

def local_data(N):
    bs, charges, off = basis(N)
    if N == 2:
        U = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)], [-sp.Rational(4, 5), sp.Rational(3, 5)]])
        V = sp.Matrix([[sp.Rational(5, 13), sp.Rational(12, 13)], [-sp.Rational(12, 13), sp.Rational(5, 13)]])
    else:
        u = sp.Matrix([1, 2, 3])
        v = sp.Matrix([2, 1, 2])
        U = sp.eye(N) - 2 * u * u.T / (u.T * u)[0]
        V = sp.eye(N) - 2 * v * v.T / (v.T * v)[0]
    if not U.T * U == V.T * V == sp.eye(N):
        raise AssertionError('Exact check failed at original line 33')
    A, da = adj_integer(U, bs)
    B, db = adj_integer(V, bs)
    return (A, B, da, db, charges, off)

def rotate(w):
    return w[-1:] + w[:-1]

def invrotate(w):
    return w[1:] + w[:1]

def selected_words(D, m, r, charges, off, balanced):
    return [w for w in it.product(range(D), repeat=m) if sum((off[i] for i in w)) <= r and (not balanced or all((sum((charges[i][j] for i in w)) == 0 for j in range(len(charges[0])))))]

def direct_trace(words, As):
    m = len(words[0])
    k = len(As)
    ans = 0
    if not k in (1, 2):
        raise AssertionError('Exact check failed at original line 46')
    for w in words:
        x = invrotate(w)
        if k == 1:
            ans += math.prod((As[0][a][b] for a, b in zip(x, w)))
        else:
            for v in words:
                ans += math.prod((As[0][a][b] for a, b in zip(x, v))) * math.prod((As[1][a][b] for a, b in zip(v, w)))
    return ans

def poly_trace(sets, As, charges, off, m, constant=True):
    """Trace of reverse-slot local product; exact multistage torus coefficient.
    Each polynomial term records row/column and separate total charge at each K.
    """
    k = len(As)
    D = len(As[0])
    nq = len(charges[0])
    zero = (0,) * (nq * k)
    terms = {(i, i, zero): 1 for i in range(D)}
    for pos in reversed(range(m)):
        for stage, A in enumerate(As):
            mark = int(pos in sets[stage])
            nxt = {}
            allowed = [b for b in range(D) if off[b] == mark]
            transitions = {b: [(c, val) for c, val in enumerate(A[b]) if val] for b in allowed}
            for (a, b, e), value in terms.items():
                if b not in transitions:
                    continue
                delta = charges[b]
                ee = list(e)
                for j, v in enumerate(delta):
                    ee[stage * nq + j] += v
                ee = tuple(ee)
                for c, val in transitions[b]:
                    key = (a, c, ee)
                    nxt[key] = nxt.get(key, 0) + value * val
            terms = {key: value for key, value in nxt.items() if value}
    if constant:
        return sum((value for (a, b, e), value in terms.items() if a == b and e == zero))
    return sum((value for (a, b, e), value in terms.items() if a == b))

def group_direct(sets, As, charges, off, m, balanced):
    D = len(As[0])
    groups = []
    for S in sets:
        alphabet = [[j for j in range(D) if off[j] == int(i in S)] for i in range(m)]
        ws = list(it.product(*alphabet))
        if balanced:
            ws = [w for w in ws if all((sum((charges[i][j] for i in w)) == 0 for j in range(len(charges[0]))))]
        groups.append(ws)
    total = 0
    for x in groups[0]:
        w = rotate(x)
        if len(As) == 1:
            total += math.prod((As[0][a][b] for a, b in zip(x, w)))
        else:
            for v in groups[1]:
                total += math.prod((As[0][a][b] for a, b in zip(x, v))) * math.prod((As[1][a][b] for a, b in zip(v, w)))
    return total

def range_projector(Y):
    piv = Y.rref()[1]
    if not piv:
        return sp.zeros(Y.rows)
    G = Y[:, list(piv)]
    return G * (G.T * G).inv() * G.T

def run_checks():
    cases = []
    N, m, r = (2, 5, 2)
    A, B, da, db, charges, off = local_data(N)
    D = len(A)
    As = [A, B]
    sets = [set(S) for k in range(r + 1) for S in it.combinations(range(m), k)]
    all_bal = all_raw = 0
    for S, T in it.product(sets, repeat=2):
        c = poly_trace([S, T], As, charges, off, m, True)
        raw = poly_trace([S, T], As, charges, off, m, False)
        if not c == group_direct([S, T], As, charges, off, m, True):
            raise AssertionError('Exact check failed at original line 103')
        if not raw == group_direct([S, T], As, charges, off, m, False):
            raise AssertionError('Exact check failed at original line 104')
        all_bal += c
        all_raw += raw
        if not sum((i not in S and i not in T for i in range(m))) >= m - 2 * r:
            raise AssertionError('Exact check failed at original line 106')
        if not sum((i not in T and (i - 1) % m not in S for i in range(m))) >= m - 2 * r:
            raise AssertionError('Exact check failed at original line 107')
    wbal = selected_words(D, m, r, charges, off, True)
    wraw = selected_words(D, m, r, charges, off, False)
    if not all_bal == direct_trace(wbal, As):
        raise AssertionError('Exact check failed at original line 109')
    if not all_raw == direct_trace(wraw, As):
        raise AssertionError('Exact check failed at original line 110')
    cases.append({'N': N, 'm': m, 'r': r, 'stages': 2, 'positional_count': len(sets), 'all_position_tuples': len(sets) ** 2, 'balanced_dimension': len(wbal), 'raw_dimension': len(wraw), 'balanced_trace': str(Fraction(all_bal, (da * db) ** m)), 'unbalanced_trace': str(Fraction(all_raw, (da * db) ** m))})
    N, m, r = (3, 5, 2)
    A, B, da, db, charges, off = local_data(N)
    D = len(A)
    As = [A, B]
    for ss in [((), ()), ((0, 1), (1, 2)), ((0, 2), (2, 4)), ((0, 4), (0, 1)), ((1, 3), ()), ((0,), (1,))]:
        S, T = map(set, ss)
        c = poly_trace([S, T], As, charges, off, m, True)
        raw = poly_trace([S, T], As, charges, off, m, False)
        if not c == group_direct([S, T], As, charges, off, m, True):
            raise AssertionError('Exact check failed at original line 120')
        if not raw == group_direct([S, T], As, charges, off, m, False):
            raise AssertionError('Exact check failed at original line 121')
        cases.append({'N': N, 'm': m, 'r': r, 'stages': 2, 'sets': ss, 'balanced_trace': str(Fraction(c, (da * db) ** m)), 'unbalanced_trace': str(Fraction(raw, (da * db) ** m))})
    N, m, r = (2, 4, 2)
    A, B, da, db, ch, off = local_data(N)
    Af = [[0] * 4 for _ in range(4)]
    Af[0][0] = da
    for i in range(3):
        for j in range(3):
            Af[i + 1][j + 1] = A[i][j]
    cf = [(0,)] + ch
    of = [0] + off
    wraw = selected_words(4, m, r, cf, of, False)
    wbal = selected_words(4, m, r, cf, of, True)
    wout = [w for w in wraw if w not in set(wbal)]
    trraw = direct_trace(wraw, [Af])
    trbal = direct_trace(wbal, [Af])
    trout = direct_trace(wout, [Af])
    if not trout == trraw - trbal:
        raise AssertionError('Exact check failed at original line 135')
    support_records = []
    for S in it.chain.from_iterable((it.combinations(range(m), k) for k in range(m + 1))):
        ws = [w for w in wout if tuple((j for j, t in enumerate(w) if t)) == S]
        value = direct_trace(ws, [Af]) if ws else 0
        if len(S) < m:
            if not value == 0:
                raise AssertionError('Exact check failed at original line 142')
        support_records.append({'support': S, 'trace': str(Fraction(value, da ** m))})
    top = [w for w in wout if all(w)]
    if not direct_trace(top, [Af]) == trout:
        raise AssertionError('Exact check failed at original line 144')
    cases.append({'N': N, 'm': m, 'r': r, 'stages': 1, 'full_offcharge_rank': len(wout), 'offcharge_trace': str(Fraction(trout, da ** m)), 'support_checks': support_records})
    N, m = (2, 3)
    physical = list(it.product(range(N), repeat=m))
    ix = {w: i for i, w in enumerate(physical)}
    nw = len(physical)
    columns = []
    for sig in it.permutations(range(m)):
        C = sp.zeros(nw)
        for j, w in enumerate(physical):
            C[ix[tuple((w[sig[i]] for i in range(m)))], j] = 1
        columns.append(sp.Matrix(C).reshape(nw * nw, 1))
    frame = sp.Matrix.hstack(*columns)
    piv = frame.rref()[1]
    F = frame[:, list(piv)]
    PH = F * (F.T * F).inv() * F.T
    Id = sp.eye(nw * nw)
    if not (PH * PH == PH and PH.T == PH):
        raise AssertionError('Exact check failed at original line 157')
    bal = [int(sorted(x) == sorted(y)) for x in physical for y in physical]
    Pi = sp.diag(*bal)
    if not Pi * PH == PH:
        raise AssertionError('Exact check failed at original line 159')
    split_records = []
    for r in range(m + 1):
        raw = [int(sum((a != b for a, b in zip(x, y))) <= r) for x in physical for y in physical]
        ir = [i for i, f in enumerate(raw) if f]
        ib = [i for i, f in enumerate(raw) if f and bal[i]]
        O = sp.diag(*[f * (1 - b) for f, b in zip(raw, bal)])
        P = range_projector((Id - PH)[:, ib])
        Pt = range_projector((Id - PH)[:, ir])
        if not (Pt == P + O and P * O == sp.zeros(nw * nw) and (PH * P == sp.zeros(nw * nw))):
            raise AssertionError('Exact check failed at original line 171')
        split_records.append({'N': N, 'm': m, 'r': r, 'haar_frame_columns': len(columns), 'haar_rank': len(piv), 'raw_rank': len(ir), 'balanced_raw_rank': len(ib), 'centered_raw_rank': int(sp.trace(Pt)), 'centered_balanced_rank': int(sp.trace(P)), 'offcharge_rank': int(sp.trace(O))})
    if not 5 ** 5 > 2916:
        raise AssertionError('Exact check failed at original line 176')
    if not 2 ** 50 < 10 ** 63:
        raise AssertionError('Exact check failed at original line 177')
    out = {'arithmetic': 'exact rational matrices, integer Laurent coefficient arithmetic; no Haar or torus quadrature', 'python': sys.version, 'sympy': sp.__version__, 'cases': cases, 'physical_range_split': split_records, 'entropy_certificates': {'one_sixth': '6 eta = log(3125/2916)>0', 'forty_nine_percent': '50 log 2 <63 log 10; h(49/100)<log 2'}, 'nonclaims': ['No asymptotic limit is inferred from bounded controls.', 'No new audit of inherited actual-map parametrix or Haar tail.', 'The full balanced/high-Hamming residual is not controlled.']}
    return out


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
