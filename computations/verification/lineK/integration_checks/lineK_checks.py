"""Line K integration checks, written at integration from the definitions (independent of the author's and the referee's
scripts). Exact integer/rational arithmetic unless stated; mpmath (80 digits) only for A = arccos(0.84431)/pi.
Run from the repository root: python3 computations/verification/lineK/integration_checks/lineK_checks.py"""
from fractions import Fraction as Fr
from math import gcd
import json, mpmath
mpmath.mp.dps = 80
ok = True
def chk(name, cond):
    global ok; ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name)

# --- A and the 1/6 margin (Lemma K3)
A = mpmath.acos(mpmath.mpf('0.84431')) / mpmath.pi
print('   A = arccos(0.84431)/pi =', mpmath.nstr(A, 20))
chk('18001/100000 <= A (80-digit mpmath; the claim uses the arb bound)', mpmath.mpf(18001) / 100000 <= A)
chk('1/6 < 18001/100000', Fr(1, 6) < Fr(18001, 100000))
Alo = Fr(18001, 100000)

# --- Lemma K3(a), own implementation: maximal cyclic gap of V(b', r) for every unit r mod g' = gcd(56, b')
def maxgap(bp, g, r):
    vs = [v for v in range(bp) if v % g == r and gcd(v, bp) == 1]
    if not vs: return bp
    return max([vs[i + 1] - vs[i] for i in range(len(vs) - 1)] + [vs[0] + bp - vs[-1]])
fails = []; worst = Fr(0)
for bp in range(447, 2646):
    g = gcd(56, bp)
    m = max(maxgap(bp, g, r) for r in range(g) if gcd(r, g) == 1)
    if Fr(m, bp) >= Alo: fails.append(bp)
    elif Fr(m, bp) > worst: worst = Fr(m, bp)
chk('Lemma K3(a) on 447..2645: failures (gap >= A_low b\') exactly {504, 560, 616, 840}', fails == [504, 560, 616, 840])
chk('every other b\' in 447..2645 has max gap <= b\'/6', worst <= Fr(1, 6))

# --- Lemma K3(b) sieve enumeration over subsets of {3,5,11,13,17,19}
from itertools import combinations
P = [3, 5, 11, 13, 17, 19]; surv = []
for k in range(len(P) + 1):
    for S in combinations(P, k):
        F = Fr(1); R = 1
        for l in S: F *= Fr(2 * l, l - 1); R *= l
        if F + 1 >= Alo * R: surv.append((S, 56 * (F + 1) / Alo))
chk('9 sieve survivors exactly {}, {3}, {5}, {11}, {13}, {17}, {3,5}, {3,11}, {3,13}',
    sorted(s for s, _ in surv) == sorted([(), (3,), (5,), (11,), (13,), (17,), (3, 5), (3, 11), (3, 13)]))
chk('all survivors have 56(F+1)/A_low <= 2645', all(b <= 2645 for _, b in surv))
chk('l = 23 excluded: 2/22 < A_low - 1/23', Fr(2, 22) < Alo - Fr(1, 23))

# --- rational case: exceptional denominators vs the certified enclosure (J3 rat_excl)
E = json.load(open('computations/verification/lineJ/J3/logs/rat_excl.json'))
L, H = Fr(E['interval'][0]), Fr(E['interval'][1])
def has_frac(b): a = -(-L.numerator * b // L.denominator); return Fr(a, b) <= H
chk('no a/b in the certified enclosure for b in {1512, 560, 1680, 616, 1848, 2520}', not any(has_frac(b) for b in [1512, 560, 1680, 616, 1848, 2520]))
chk('least denominator with a fraction in the enclosure is 1339', min(b for b in range(1, 1400) if has_frac(b)) == 1339)
chk('candidate b for exceptional b\': b\' (if 3 does not divide b\') or 3b\'', sorted({x for bp in [504, 560, 616, 840] for x in ([bp] if bp % 3 else []) + [3 * bp]}) == [560, 616, 1512, 1680, 1848, 2520])

# --- Prop K2 / Theorem K constants
Lam = mpmath.log(mpmath.mpf('1.9154753')**2 / mpmath.mpf('2.4586893'))
chk('Lambda = log(mu^2/xi_lo) = 0.40030 (to 5 digits)', abs(Lam - mpmath.mpf('0.40030')) < mpmath.mpf('5e-6'))
rate = mpmath.log(1 + mpmath.sqrt(2))   # h_m ~ eps^m/2 with eps = 1+sqrt2, so log sqrt(h_m) ~ m log(eps)/2 = 0.4407 m
chk('K2 non-vacuity needs Lambda(1+eta) < log(eps)/2, i.e. eta < 0.4407/0.4003 - 1 = 0.1009 (3 digits)', abs((rate / 2) / Lam - 1 - mpmath.mpf('0.1009')) < mpmath.mpf('5e-4'))
for Kr in [Fr(1), Fr(1, 2), Fr(1, 10)]:   # K_min/K_j <= 1
    for d in [Fr(1, 100), Fr(1, 2)]:
        lhs = Fr(99, 200) - Fr(1, 200) * Kr - (1 - d) * Fr(98, 200)
        chk('Theorem K arithmetic: 0.99/2 - 0.01 (K_min/K_j)/2 - (1-delta) 0.98/2 >= 0.98 delta/2 (K_min/K_j = %s, delta = %s)' % (Kr, d), lhs >= Fr(98, 200) * d)
# --- Theorem W step 6 constants (W-F2)
chk('1.6677 * 1.4742 < xi_lo = 2.4586893', Fr(16677, 10**4) * Fr(14742, 10**4) < Fr(24586893, 10**7))
chk('1.6677 * 1.4743 > xi_lo (the withdrawn constant was false)', Fr(16677, 10**4) * Fr(14743, 10**4) > Fr(24586893, 10**7))
chk('mu_up * 1.28359 = 1.9154753 * 1.28359 < xi_lo', Fr(19154753, 10**7) * Fr(128359, 10**5) < Fr(24586893, 10**7))
# --- W2' constant: (1 - x)^(-1/x) <= e^2 for 0 < x <= 1/2 (x = 2k/m, m >= 4k); maximum at x = 1/2 is 4
xs = [mpmath.mpf(i) / 1000 for i in range(1, 501)]
chk("W2' constant: (1-x)^(-1/x) <= 4 <= e^2 on (0, 1/2]", max((1 - x)**(-1 / x) for x in xs) <= 4 + mpmath.mpf('1e-30') and 4 <= mpmath.e**2)
# --- Theorem K1 Gauss-sum sign: (2/q) = +1 iff q = +-1 mod 8, and q | h_m forces it (2 y'^2 = 1 mod q) for small m
def h(m):
    a, b = 1, 1
    for _ in range(m - 1): a, b = a + 2 * b, a + b
    return a
bad = []
for m in range(3, 61, 2):
    n = h(m); q = 3
    while q * q <= n and q < 20000:
        if n % q == 0 and q != 7 and q % 8 not in (1, 7): bad.append((m, q))
        q += 2
chk('every odd prime factor q != 7 (< 20000) of h_m, odd m < 61, has q = +-1 mod 8 (2 a square mod q)', not bad)
print('ALL_OK' if ok else 'SOME_FAIL')
