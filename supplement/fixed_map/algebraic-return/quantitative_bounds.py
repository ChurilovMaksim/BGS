"""Exact conservative gap exponents; no evaluation of tiny floating gaps."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from fractions import Fraction as F
import json
from math import isqrt
from pathlib import Path
from exact_coefficients import frozen_coefficients


def phi(n):
    result, m, p = n, n, 2
    while p*p <= m:
        if m % p == 0:
            result -= result//p
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        result -= result//m
    return result


folder = Path(__file__).resolve().parent
certs = json.loads((folder/'certificates.json').read_text())['certificates']
C = sum(abs(re)+abs(im) for re, im in frozen_coefficients().values())
assert C == F(643, 500)
rows = []
for cert in certs:
    n, r, t = cert['N'], cert['period'], abs(cert['weight'])
    d, D = phi(4*n), 4000*r
    root = isqrt(n)+(isqrt(n)**2 != n)
    H0 = D*(root+t*C)
    assert H0.denominator == 1
    exponent = d*n*(n-1)//2-1
    assert d*n*(n-1) % 2 == 0 and exponent > 0
    L = len(str(D))+exponent*len(str(2*int(H0)))
    # epsilon=N/10^80 <= (4/R)10^-L/(18 C^2 t)
    # iff 10^(80-L) >= 18 R C^2 t N/4. Right side >1 here.
    rhs = F(18*r*t*n, 4)*C*C
    assert rhs > 1
    covered = L <= 80 and F(10**(80-L)) >= rhs
    rows.append({'N': n, 'ordinary_midpoint': cert['ordinary_midpoint'],
                 'R': r, 'weight': t, 'cyclotomic_degree': d,
                 'integral_scaling': D, 'all_conjugates_norm_bound': int(H0),
                 'min_gap_B_at_least_10_to_minus_L': L,
                 'frozen_epsilon_in_conservative_splitting_interval': covered,
                 'interpretation': 'A failed interval test does not mean the actual spectrum is degenerate'})
assert [x['N'] for x in rows if x['frozen_epsilon_in_conservative_splitting_interval']] == [3]
output = {'status': 'completed', 'operator_norm_bound': str(C), 'rows': rows,
          'scope': 'Quantitative finite-dimensional bound; no uniform BGS estimate'}
(folder/'quantitative_bounds.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
