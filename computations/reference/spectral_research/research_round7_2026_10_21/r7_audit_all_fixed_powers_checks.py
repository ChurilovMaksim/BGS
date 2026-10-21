#!/usr/bin/env python3
"""Fresh exact checks accompanying an independent proof audit.

These finite algebra checks are not a substitute for the analytic proof.
No author checker or previous audit checker is imported.
"""

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_suffix(".md")
counts = defaultdict(int)


def check(condition, group):
    counts[group] += 1
    assert condition, (group, counts[group])


ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def ca(z, w):
    return z[0] + w[0], z[1] + w[1]


def cm(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def scale(p, c):
    c = c if isinstance(c, tuple) else (F(c), F(0))
    return {v: cm(z, c) for v, z in p.items() if cm(z, c) != ZERO}


def add(*ps):
    out = {}
    for p in ps:
        for v, z in p.items():
            out[v] = ca(out.get(v, ZERO), z)
    return {v: z for v, z in out.items() if z != ZERO}


def mul(p, q):
    out = {}
    for (k, l), z in p.items():
        for (u, v), w in q.items():
            lab = (k + u, l + v)
            out[lab] = ca(out.get(lab, ZERO), cm(z, w))
    return {v: z for v, z in out.items() if z != ZERO}


one = {(0, 0): ONE}
cos1 = {(1, 0): (F(1, 2), F(0)), (-1, 0): (F(1, 2), F(0))}
cos7 = {(7, 0): (F(1, 2), F(0)), (-7, 0): (F(1, 2), F(0))}
sin1 = {(1, 0): (F(0), F(-1, 2)), (-1, 0): (F(0), F(1, 2))}
cosp = {(0, 1): (F(-3, 10), F(-2, 5)),
        (0, -1): (F(-3, 10), F(2, 5))}
r = mul(add(one, scale(cos7, -1)), add(one, cos1))
v = add(cos7, scale(r, F(1, 10)),
        scale(mul(r, sin1), F(1, 100)), scale(one, F(-1, 10)))
original = add(v, scale(mul(r, cosp), F(1, 100)))
corrected = {lab: cm(z, (F(-1 if (lab[0] * lab[1]) % 2 else 1), F(0)))
             for lab, z in original.items()}
rshift = {lab: cm(z, (F(-1 if lab[0] % 2 else 1), F(0))) for lab, z in r.items()}
a_symbol = add(v, scale(mul(rshift, cosp), F(1, 100)))
check(corrected == a_symbol, "exact corrected Fourier symbol")
check(a_symbol[1, 0] == (F(1, 20), F(-1, 200)), "exact corrected Fourier symbol")
check(a_symbol[0, 1] == (F(-3, 1000), F(-1, 250)), "exact corrected Fourier symbol")
l1_bound = sum(abs(z[0]) + abs(z[1]) for z in a_symbol.values())
check(l1_bound == F(593, 500), "exact corrected Fourier symbol")
check(l1_bound < 2, "exact corrected Fourier symbol")
for (k, l), z in a_symbol.items():
    check(abs(k) + abs(l) <= 9 and abs(l) <= 1, "exact corrected Fourier symbol")
    check(a_symbol[-k, -l] == (z[0], -z[1]), "exact corrected Fourier symbol")

# Direct modular kernel covariance on full grids, without matrix floating point.
for N in range(3, 42, 2):
    ih = pow(2, -1, N)
    ie = pow(8, -1, N)
    iq = pow(4, -1, N)
    check((8 * ie) % N == 1, "finite modular covariance")
    for x in range(N):
        for y in range(N):
            check((((x - y) * iq) % N == 0) == (x == y),
                  "unitary Fourier coefficient")
    def kernel_exp(x, y):
        return (-ie * (3*x*x - 2*x*y + 3*y*y)) % N
    for l in range(-2, 3):
        for k in range(-2, 3):
            lp, kp = 3*l + 4*k, 2*l + 3*k
            check((lp*kp - l*k) % 2 == 0, "ordinary-half parity covariance")
            for x in range(N):
                check((2*k*(x + ih*l) - (2*k*x + k*l + N*k*l)) % (2*N) == 0,
                      "ordinary-half parity covariance")
                for y in range(N):
                    left = kernel_exp(x, y-l) + k*(y-l + ih*l)
                    right = kp*(x + ih*lp) + kernel_exp(x+lp, y)
                    check((left-right) % N == 0, "finite modular covariance")

S = (3, 4, 2, 3)


def mm(A, B):
    a, b, c, d = A
    e, f, g, h = B
    return a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h


powers = [(1, 0, 0, 1)]
for R in range(1, 257):
    powers.append(mm(powers[-1], S))
    a, b, c, aa = powers[-1]
    check(aa == a and a*a-b*c == 1 and b == 2*c, "integer iterate and deck lattice")
    check(a % 2 == 1 and b % 2 == c % 2 == 0, "integer iterate and deck lattice")
    check(gcd(a, b) == 1 and a > 0 and b > 0 and c > 0, "integer iterate and deck lattice")
    check((b, b*a-a*b) == (b, 0), "integer iterate and deck lattice")
    check((a, a*a-c*b) == (a, 1), "integer iterate and deck lattice")
    check(abs(-b) >= 3 and abs(a) >= 3, "surviving Fourier labels")
    for d in {1, b//2, b-1, max(1, b//3)}:
        check(0 < d < b, "nontrivial induced translations")
        check(F(d, b).denominator > 1 and F(a*d, b).denominator > 1,
              "nontrivial induced translations")
        L = b // gcd(b, d)
        check((L*d) % b == 0, "nontrivial induced translations")

# Check all deck and intertwining polynomial identities at rational probes.
for R in range(1, 33):
    a, b, c, _ = powers[R]
    def theta(q, s, m):
        return -(a*q*q-2*q*(s+m)+a*(s+m)*(s+m))/(2*b)
    for q in (F(-2, 5), F(0), F(1, 3)):
        for s in (F(-1, 7), F(0), F(2, 3)):
            for m in (-a, 0, 1, b-1, b+1):
                check(theta(q,s,m+b)-theta(q,s,m) == q-a*(s+m)-F(a*b,2),
                      "exact phase deck identities")
                check(theta(q+1,s,m)-theta(q,s,m-a) == -c*(s+m)+F(a*c,2),
                      "exact phase deck identities")
                check(theta(q,s+1,m) == theta(q,s,m+1), "exact phase deck identities")
    def quadratic(x, y):
        return a*x*x-2*x*y+a*y*y
    for x, y, N in ((-2, 3, 5), (0, 0, 9), (7, -3, 15), (1, 4, 35)):
        check(quadratic(x+N,y+a*N)-quadratic(x,y) == b*c*(2*y*N+a*N*N),
              "image-kernel polynomial intertwining")
        check(quadratic(x+a,y)-quadratic(x,y-1) == b*c*(2*x+a),
              "image-kernel polynomial intertwining")
        check(quadratic(x+b,y)-quadratic(x,y) == 2*b*(a*x+a*b//2-y),
              "image-kernel polynomial intertwining")

# Exact surviving differences in the image Gauss norm, including common divisors.
seen_g = set()
for R in range(1, 6):
    a, b, c, _ = powers[R]
    for N in range(3, 66, 2):
        g = gcd(N, b)
        seen_g.add(g)
        survivors = [h for h in range(b) if (N*h) % b == 0]
        check(survivors == [(b//g)*j for j in range(g)], "all-odd Gauss differences")
        check(g % 2 == 1 and (b//g) % 2 == 0, "all-odd Gauss differences")
        for j in range(g):
            check((a*(N//g)*(b//g)*j*j) % 2 == 0, "all-odd Gauss differences")
        for x, y in ((0,0), (1,0), (0,1), (N-1,N-1)):
            check((-c*y-c*N*(b-1)+F(a*c*N,2)).denominator == 1,
                  "wrapped-grid phases")
            check((x-a*y-a*N*(b-1)-F(a*b*N,2)).denominator == 1,
                  "wrapped-grid phases")

# Noncommutative factorization: full kicks K and an independent partial kick U.
def red(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return out


for R in range(1, 97):
    word = [1]*R
    for k in range(R):
        check(word == [1]*(R-k) + [2,1]*k, "every intermediate stage word")
        j = R-k-1
        partial = red([1]*j + [3] + [-1]*j + word)
        check(partial == [1]*j + [3,1] + [2,1]*k, "every intermediate stage word")
        word = red([1]*j + [2] + [-1]*j + word)
    check(word == [2,1]*R, "every intermediate stage word")

# All parameter inequalities are rational inequalities at the prescribed tau.
tau = F(1, 10**80)
eps = 14000*tau
check(0 < eps < F(1,2), "fixed-tau constants")
check(2000*tau < F(1,2), "fixed-tau constants")
check(4000*7 == 14000*2, "fixed-tau constants")
check(5**200 > 10**80, "fixed-tau constants")
check(20000*F(5,4)+200*100000+40*F(5,4) == 20025050, "fixed-tau constants")
check(20025050 < 30000000, "fixed-tau constants")
check(30000000*tau < F(1,800), "fixed-tau constants")
e1_sq = F(2,3) * (F(1,20)**2 + F(1,200)**2)
e2_sq = F(1,3) * (F(3,1000)**2 + F(1,250)**2)
check(e1_sq == F(101,60000), "surviving Fourier coefficients")
check(e2_sq == F(1,120000), "surviving Fourier coefficients")
check(e1_sq > F(1,400)**2 and e2_sq > F(1,400)**2, "surviving Fourier coefficients")

# Polynomial examples independently check the rectangular-cycle algebra.
# The analytic proof for all phases is given separately in the audit.
def pclean(p):
    return {v: c for v,c in p.items() if c}


def rect(i, j):
    p = defaultdict(int)
    for lab, coef in (((i,0,j,0),1), ((0,i,j,0),-1),
                      ((0,i,0,j),1), ((i,0,0,j),-1)):
        p[lab] += coef
    return pclean(p)


def deriv(p, idx):
    out = defaultdict(int)
    for lab, c in p.items():
        if lab[idx]:
            v = list(lab)
            v[idx] -= 1
            out[tuple(v)] += c*lab[idx]
    return pclean(out)


def ondiag(p, pair):
    out = defaultdict(int)
    for lab, c in p.items():
        v = list(lab)
        v[pair[0]] += v[pair[1]]
        v[pair[1]] = 0
        out[tuple(v)] += c
    return pclean(out)


for i in range(9):
    for j in range(9):
        p = rect(i,j)
        check((not p) == (i == 0 or j == 0), "rectangular-cycle algebra")
        check(not ondiag(p,(0,1)) and not ondiag(p,(2,3)), "rectangular-cycle algebra")
        check(all(sum(v) >= 2 for v in p), "rectangular-cycle algebra")
        expected = {(i-1,0,j-1,0): i*j} if i*j else {}
        check(deriv(deriv(p,0),2) == expected, "rectangular-cycle algebra")

source_names = (
    "research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md",
    "research_round6_2026_10_21/round6_main_report.md",
    "research_round2_2026_10_20/arithmetic_iterated_sector_covariance.md",
    "research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md",
)
hashes = {name: sha256((ROOT/name).read_bytes()).hexdigest() for name in source_names}
check(hashes[source_names[0]] == "46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527",
      "source pin")
script_hash = sha256(Path(__file__).read_bytes()).hexdigest()
lines = [
    "# Exact checks for the independent all-fixed-power audit", "",
    "21 October 2026. All computations use integers and exact rational arithmetic.",
    "No numerical flow, stationary-phase experiment, author checker, or prior audit checker is used.", "",
    f"**Result: {sum(counts.values()):,} assertions passed.**", "",
    "| Check group | Assertions |", "| --- | ---: |",
]
lines += [f"| {name} | {number:,} |" for name, number in counts.items()]
lines += [
    "", "## Scope", "",
    "Direct modular covariance was checked on every grid point for each odd dimension 3 through 41 and all shifts and multipliers from -2 through 2.",
    "Integer iterate and period-lattice identities were checked through R=256; every partial-stage noncommutative word was checked through R=96.",
    "The exact Fourier symbol was rebuilt from the original prescription before applying the modular-half correction.",
    "Image-phase identities and wrapped-grid phases use rational arithmetic; surviving Gauss differences include the common divisors listed below.",
    "Polynomial rectangular cycles through separate degrees eight check the elementary algebra only.",
    "The global analytic graph construction, no-translation theorem, decay of every Poisson alias, and the asymptotic WKB and return conclusions are proved analytically in the audit. These finite checks do not replace those proofs.",
    "", "Observed Gauss common divisors: " + ", ".join(map(str, sorted(seen_g))) + ".",
    "", "## Source provenance", "", "| Source | SHA-256 |", "| --- | --- |",
]
lines += [f"| {name} | {digest} |" for name, digest in hashes.items()]
lines += ["", "Checker SHA-256: " + script_hash, ""]
OUT.write_text("\n".join(lines))
print(json.dumps({"status":"passed", "assertions":sum(counts.values()),
                  "output":str(OUT), "script_sha256":script_hash}, indent=2))
