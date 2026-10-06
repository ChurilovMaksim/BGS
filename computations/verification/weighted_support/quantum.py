"""Exact rational controls of the NEW algebra, not a proof of analytic limits.
Tests repeated endpoints at m=1,2, full Wick contractions, covariance
variation, literal-winding endpoint labels, and raw Weyl parity counting.
"""
from functools import lru_cache
import hashlib, json
from pathlib import Path
import sympy as s

def pairings(indices):
    if not indices:
        yield ()
        return
    a = indices[0]
    for j in range(1, len(indices)):
        for rest in pairings(indices[1:j] + indices[j + 1:]):
            yield (((a, indices[j]),) + rest)

def wick(indices, G):
    return sum((s.prod((G[a, b] for a, b in p)) for p in pairings(tuple(indices))), s.S.Zero)

def wick_prime_pairings(indices, G, DG):
    ans = s.S.Zero
    for p in pairings(tuple(indices)):
        for k, (a, b) in enumerate(p):
            ans += DG[a, b] * s.prod((G[c, d] for j, (c, d) in enumerate(p) if j != k))
    return ans

def wick_prime_price(indices, G, DG):
    ans = s.S.Zero
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            rem = tuple((v for k, v in enumerate(indices) if k not in (i, j)))
            ans += DG[indices[i], indices[j]] * wick(rem, G)
    return ans

def run():
    cases = []
    winding = []
    S = s.Matrix([[3, 4], [2, 3]])
    for m in range(1, 13):
        P = s.zeros(m)
        for j in range(m):
            P[j, (j + 1) % m] += 1
        K = (6 * s.eye(m) - P - P.T) / 4
        G = K.inv()
        if not all((sum((G[j, k] for k in range(m))) == 1 for j in range(m))):
            raise RuntimeError('Exact check failed at original line 47')
        xp = G[:, 0]
        delta = s.Matrix([xp[0], (xp[1 % m] - 3 * xp[0]) / 4])
        if not delta == (S ** m - s.eye(2)).inv() * s.Matrix([0, 1]):
            raise RuntimeError('Exact check failed at original line 50')
        if not delta[1] == -s.Rational(1, 2):
            raise RuntimeError('Exact check failed at original line 51')
        winding.append({'m': m, 'delta_q': str(delta[0]), 'delta_p': str(delta[1])})
        KP = s.zeros(m)
        for j in range(m):
            inds = [j, (j + 1) % m]
            local = s.Matrix([[s.Rational(2 * j + 1, 31), s.Rational(1, 37)], [s.Rational(1, 37), s.Rational(j + 3, 41)]]) / (j + 1)
            for a in range(2):
                for b in range(2):
                    KP[inds[a], inds[b]] += local[a, b] * (xp[j] + xp[(j + 1) % m])
        GP = -G * KP * G
        if not G * KP + GP * K == s.zeros(m):
            raise RuntimeError('Exact check failed at original line 63')
        samples = []
        for j in range(m):
            ends = (j, (j + 1) % m)
            samples += [(), (ends[0],) * 2, (ends[1],) * 4, (ends[0], ends[1])]
            for k in range(m):
                f = (k, (k + 1) % m)
                samples += [(ends[0], f[1]), (ends[0],) * 3 + (f[1],), (ends[0],) + (f[1],) * 3, (ends[0], ends[1], ends[1], f[0], f[0], f[1])]
        for indices in samples:
            if not wick_prime_pairings(indices, G, GP) == wick_prime_price(indices, G, GP):
                raise RuntimeError('Exact check failed at original line 75')
        cases.append({'m': m, 'wick_variation_checks': len(samples), 'Kprime_entry_l1': str(sum((abs(x) for x in KP))), 'Gprime_entry_l1': str(sum((abs(x) for x in GP)))})
    parity = 0
    for a in range(9):
        for v in range(9 - a):
            for p1 in range(9 - a - v):
                for p2 in range((8 - a - v - p1) // 2 + 1):
                    for p3 in range((8 - a - v - p1 - 2 * p2) // 3 + 1):
                        grade = a + v + p1 + 2 * p2 + 3 * p3
                        factors = v + p1 + p2 + p3
                        moments = a + 2 * v + 2 * p1 + 3 * p2 + 4 * p3
                        if not factors - moments == -grade:
                            raise RuntimeError('Exact check failed at original line 92')
                        parity += 1
    report = {'arithmetic': 'exact SymPy rational/integer', 'scope': 'm=1..12; repeated endpoint aliases retained; Weyl grades <=8 with phase grades <=3', 'nonclaims': 'Does not test the actual analytic amplitudes numerically or prove an asymptotic theorem, bounded classical mass, equidistribution, or the full signed sum.', 'weyl_parity_checks': parity, 'wick_variation_cases': cases, 'unit_winding_labels': winding, 'total_wick_checks': sum((c['wick_variation_checks'] for c in cases))}
    return report
