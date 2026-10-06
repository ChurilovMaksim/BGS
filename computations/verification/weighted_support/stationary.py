from fractions import Fraction as F
from math import gcd

def run():
    S = lambda z, L: ((3 * z[0] + 4 * z[1]) % L, (2 * z[0] + 3 * z[1]) % L)
    a, b = (1, 0)
    rows = []
    for m in range(1, 7):
        a, b = (3 * a + 4 * b, 2 * a + 3 * b)
        U = gcd(a - 1, b)
        L = U if m % 2 else 2 * U
        G = [(x, y) for x in range(0, L, 1 if m % 2 else 2) for y in range(L)]
        D = 2 * (a - 1)
        if not len(G) == D:
            raise RuntimeError('Exact check failed at original arithmetic line 11')
        q = F(a + 1, 2 * b)
        p = F(-1, 2)
        if not ((q * L).denominator == 1 and (p * L).denominator == 1):
            raise RuntimeError('Exact check failed at original arithmetic line 14')
        pulse = (int(q * L) % L, int(p * L) % L)
        pos = set()
        d = pulse
        for j in range(m):
            pos.add(d)
            d = S(d, L)
        H = pos | {(-x % L, -y % L) for x, y in pos}

        def twice_pairing(d):
            n_p_num = b * d[0] + (a - 1) * d[1]
            if not n_p_num % L == 0:
                raise RuntimeError('Exact check failed at original arithmetic line 21')
            return n_p_num // L % 2
        if not all((twice_pairing(d) == 1 for d in H)):
            raise RuntimeError('Exact check failed at original arithmetic line 23')
        ccount = 0
        shortpoints = 0
        for z in G:
            orbit = set()
            y = z
            for j in range(m):
                orbit.add(y)
                y = S(y, L)
            if not y == z:
                raise RuntimeError('Exact check failed at original arithmetic line 28')
            ccount += len(orbit)
            shortpoints += len(orbit) < m
            for y in orbit:
                d = ((y[0] - z[0]) % L, (y[1] - z[1]) % L)
                if not (twice_pairing(d) == 0 and d not in H):
                    raise RuntimeError('Exact check failed at original arithmetic line 32')
        rows.append({'m': m, 'fixed_points': D, 'cyclic_ordered_pairs': ccount, 'proper_period_points': shortpoints, 'homoclinic_ordered_pairs': D * len(H), 'intersection': 0})
    z = (F(1, 7), F(0))
    zp = (F(3, 7), F(2, 7))
    d = (F(2, 7), F(2, 7))
    if not all(((7 * x).denominator == 1 for x in d)):
        raise RuntimeError('Exact check failed at original arithmetic line 37')
    if not d != (0, 0):
        raise RuntimeError('Exact check failed at original arithmetic line 38')
    if not all((x.denominator == 1 for x in (98 * z[0] + 140 * z[1], 70 * z[0] + 98 * z[1]))):
        raise RuntimeError('Exact check failed at original arithmetic line 40')
    res = {'arithmetic': 'exact integers and Fractions', 'scope': 'Exhaustive labels and cyclic pairs for m=1..6; all corresponding H displacement directions; literal torsion counterexample.', 'rows': rows, 'torsion_counterexample': {'m': 3, 'N': 7, 'z': ['1/7', '0'], 'z_prime': ['3/7', '2/7'], 'd': ['2/7', '2/7']}, 'nonclaims': 'No finite algebra sample proves the analytic ramp or asymptotic residual bound.'}
    return res
