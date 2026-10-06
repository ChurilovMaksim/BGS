from fractions import Fraction as F
from math import factorial
import sympy as s
import json

def main():
    rows = []
    for m in range(1, 19):
        K = s.zeros(m)
        for j in range(m):
            k = (j + 1) % m
            K[j, j] += s.Rational(3, 4)
            K[k, k] += s.Rational(3, 4)
            K[j, k] -= s.Rational(1, 4)
            K[k, j] -= s.Rational(1, 4)
        G = K.inv()
        g0 = G[0, 0]
        if not all((sum((G[j, k] for k in range(m))) == 1 for j in range(m))):
            raise RuntimeError('exact control failed: all((sum((G[j, k] for k in range(m))) == 1 for j in range(m)))')
        for j in range(m):
            for k in range(m):
                d = min((j - k) % m, (k - j) % m)
                if not abs(G[j, k]) <= s.Rational(5, 4) * s.Rational(3, 7) ** d:
                    raise RuntimeError('exact control failed: abs(G[j, k]) <= s.Rational(5, 4) * s.Rational(3, 7) ** d')
        density = s.factor(g0 ** 2 / 4 + sum((G[0, k] ** 3 for k in range(m))) / 12)
        mean = 3 * m * g0 ** 2
        raw2 = sum((9 * g0 ** 4 + 72 * g0 ** 2 * G[j, k] ** 2 + 24 * G[j, k] ** 4 for j in range(m) for k in range(m)))
        conn2 = s.factor(raw2 - mean ** 2)
        local = s.factor(m * (72 * g0 ** 2 * sum((G[0, k] ** 2 for k in range(m))) + 24 * sum((G[0, k] ** 4 for k in range(m)))))
        if not conn2 == local:
            raise RuntimeError('exact control failed: conn2 == local')
        if not 0 < density <= s.Rational(1, 3):
            raise RuntimeError('exact control failed: 0 < density <= s.Rational(1, 3)')
        rows.append({'m': m, 'one_loop_density': str(density), 'quartic_second_cumulant_per_site': str(s.factor(conn2 / m))})
    rho = 3 - 2 * s.sqrt(2)
    limit = s.simplify(s.Rational(1, 8) + (1 + rho ** 3) / (1 - rho ** 3) / (24 * s.sqrt(2)))
    if not limit == s.Rational(13, 84):
        raise RuntimeError('exact control failed: limit == s.Rational(13, 84)')
    count = 0
    for k in range(1, 26):
        for r in range(1, 2 * k + 1):
            for E in range(0, k + r + 1):
                pairings = F(factorial(2 * E), 2 ** E * factorial(E))
                if not pairings / factorial(r) <= 2 ** (k + r) * (3 * k) ** k:
                    raise RuntimeError('exact control failed: pairings / factorial(r) <= 2 ** (k + r) * (3 * k) ** k')
                count += 1
    print(json.dumps({'arithmetic': 'exact rational/SymPy; no fixed-tau spectrum simulation', 'matrix_dimensions': list(range(1, 19)), 'homogeneous_one_loop_density_limit': str(limit), 'factorial_bound_checks': count, 'rows': rows}, indent=2))
if __name__ == '__main__':
    main()
