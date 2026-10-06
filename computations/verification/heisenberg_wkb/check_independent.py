from fractions import Fraction as F
from itertools import product, permutations
from math import factorial, prod
import json
import sympy as s

def parts(n):
    if n == 0:
        yield []
    else:
        for p in parts(n - 1):
            yield (p + [[n - 1]])
            for j in range(len(p)):
                yield (p[:j] + [p[j] + [n - 1]] + p[j + 1:])

def mu(p):
    return prod(((-1) ** (len(b) - 1) * factorial(len(b) - 1) for b in p))

def main():
    N = 3
    e = s.Rational(1, 40)
    U = s.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    V = U + s.diag(e, 0, 0)
    if not V * V.T != V.T * V:
        raise RuntimeError('exact control failed: V * V.T != V.T * V')
    q = 1 / (1 - e)
    P = {n: V ** n for n in range(-12, 13)}
    TU = {n: s.trace(U ** n) for n in P}
    TL = {n: s.trace(P[n]) for n in P}
    TA = {n: s.trace(P[abs(n)]) for n in P}
    counts = {'trace_bounds': 0, 'inverse_telescope': 0, 'partition_products': 0, 'zero_blocks': 0, 'laurent_distinct': 0}
    for p in range(1, 13):
        rhs = s.zeros(N)
        for j in range(p):
            rhs += V ** (-j - 1) * (U - V) * U ** (-(p - j))
        if not rhs == V ** (-p) - U ** (-p):
            raise RuntimeError('exact control failed: rhs == V ** (-p) - U ** (-p)')
        counts['inverse_telescope'] += 1
    for T in [TL, TA]:
        for n in P:
            if not abs(T[n]) <= N * q ** abs(n):
                raise RuntimeError('exact control failed: abs(T[n]) <= N * q ** abs(n)')
            if not abs(T[n] - TU[n]) <= N * abs(n) * e * q ** abs(n):
                raise RuntimeError('exact control failed: abs(T[n] - TU[n]) <= N * abs(n) * e * q ** abs(n)')
            counts['trace_bounds'] += 1
    for k in range(2, 6):
        ps = list(parts(k))
        if not sum((abs(mu(p)) * N ** len(p) for p in ps)) == prod(range(N, N + k)):
            raise RuntimeError('exact control failed: sum((abs(mu(p)) * N ** len(p) for p in ps)) == prod(range(N, N + k))')
        for lead in product(range(-1, 2), repeat=k - 1):
            m = lead + (-sum(lead),)
            for p in ps:
                bsum = [sum((m[i] for i in b)) for b in p]
                sp = sum(map(abs, bsum))
                for T in [TL, TA]:
                    lhs = abs(prod((T[n] for n in bsum)) - prod((TU[n] for n in bsum)))
                    if not lhs <= e * N ** len(p) * sp * q ** sp:
                        raise RuntimeError('exact control failed: lhs <= e * N ** len(p) * sp * q ** sp')
                    counts['partition_products'] += 1
                    if 0 in bsum:
                        counts['zero_blocks'] += 1
    H = s.Matrix([[s.Rational(6, 5), s.Rational(1, 7), 0], [0, s.Rational(-3, 4), s.Rational(1, 9)], [0, 0, s.Rational(2, 3)]])
    if not H * H.T != H.T * H:
        raise RuntimeError('exact control failed: H * H.T != H.T * H')
    lam = [H[i, i] for i in range(N)]
    HT = {n: s.trace(H ** n) for n in range(-4, 5)}
    for k in range(2, 6):
        for lead in product(range(-1, 2), repeat=k - 1):
            m = lead + (-sum(lead),)
            d = sum((mu(p) * prod((HT[sum((m[i] for i in b))] for b in p)) for p in parts(k)))
            direct = sum((prod((lam[idx[a]] ** m[a] for a in range(k))) for idx in permutations(range(N), k)))
            if not d == direct:
                raise RuntimeError('exact control failed: d == direct')
            counts['laurent_distinct'] += 1
    r = s.Rational(6, 5)
    if not r * r - 1 == s.Rational(11, 25):
        raise RuntimeError('exact control failed: r * r - 1 == s.Rational(11, 25)')
    if not r * (1 / r) - 1 == 0:
        raise RuntimeError('exact control failed: r * (1 / r) - 1 == 0')
    D = s.Matrix([[2, 1], [0, 2]])
    for n in range(-8, 9):
        if not s.trace(D ** n) == 2 * s.Rational(2) ** n:
            raise RuntimeError('exact control failed: s.trace(D ** n) == 2 * s.Rational(2) ** n')
    counts['defective_trace_powers'] = 17
    print(json.dumps({'passed': True, 'arithmetic': 'exact rational SymPy', 'counts': counts}, indent=2))
if __name__ == '__main__':
    main()
