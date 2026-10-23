#!/usr/bin/env python3
"""Exact Gaussian polynomial/Haar contraction audit; no floating arithmetic.

Integer coefficient polynomials, complex Gaussian factorial norms, all 24
fourth-tensor sphere pairings. No assertions, so python -O preserves checks.
The algebra tests do not substitute for the general proof.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial, prod
from pathlib import Path
import hashlib
import json


def check(ok, *description):
    if not ok:
        raise RuntimeError(description)


def add(*ps):
    out = Counter()
    for p in ps:
        out.update(p)
    return dict(out)


def times(p, q):
    out = Counter()
    for a, x in p.items():
        for b, y in q.items():
            out[tuple(v + w for v, w in zip(a, b))] += x * y
    return dict(out)


def inner(p, q):
    return sum(a * q.get(nu, 0) * prod(factorial(v) for v in nu)
               for nu, a in p.items())


def norm(p):
    return inner(p, p)


def trace_poly(n, m):
    if m == 0:
        return {(0,) * (n * n): n}
    out = Counter()
    for x in product(range(n), repeat=m):
        nu = [0] * (n * n)
        for a, b in zip(x, x[1:] + x[:1]):
            nu[a * n + b] += 1
        out[tuple(nu)] += 1
    return dict(out)


def hessian(p):
    out = {}
    for nu, c in p.items():
        active = [i for i, v in enumerate(nu) if v]
        for e in active:
            for f in active:
                weight = nu[e] * (nu[f] - (e == f))
                if weight:
                    v = list(nu)
                    v[e] -= 1
                    v[f] -= 1
                    out.setdefault((e, f), Counter())[tuple(v)] += c * weight
    return out


def sphere_pairing(H, n, sigma):
    # Positive u positions a,c,f,h; negative u positions b,d,e,g.
    positive = (0, 2, 5, 7)
    negative = (1, 3, 4, 6)
    labels = [None] * 8
    for k, j in enumerate(sigma):
        labels[positive[k]] = k
        labels[negative[j]] = k
    total = 0
    for values in product(range(n), repeat=4):
        a, b, c, d, e, f, g, h = [values[j] for j in labels]
        total += inner(H.get((a * n + b, c * n + d), {}),
                       H.get((e * n + f, g * n + h), {}))
    cross = sum(j >= 2 for j in sigma[:2]) * 2
    return cross, total


def sixth_pairing(H, n, sigma):
    # In H_ab,cd conjugate(H_eb,gh), b is free and shared.
    # Positive sphere slots a,c,h; negative slots d,e,g.
    positive, negative = (0, 2, 7), (3, 4, 6)
    labels = [None] * 8
    labels[1] = labels[5] = 3
    for k, j in enumerate(sigma):
        labels[positive[k]] = k
        labels[negative[j]] = k
    total = 0
    for values in product(range(n), repeat=4):
        a, b, c, d, e, f, g, h = [values[j] for j in labels]
        total += inner(H.get((a * n + b, c * n + d), {}),
                       H.get((e * n + f, g * n + h), {}))
    return total


def hook_weight(n, k, j):
    return factorial(n + k - j - 1) // factorial(n - j - 1)


def closed_collision_mean(n, m):
    """Exact finite formula derived from all 24+6 tensor contractions."""
    def hc(k):
        weights = [hook_weight(n, k, j) for j in range(min(n, k))]
        return sum(weights), sum((k - 1 - 2*j)*w for j, w in enumerate(weights))
    hm, cm = hc(m)
    hp, cp = hc(m-1)
    un = hook_weight(n, m, 0) - (hook_weight(n, m, m-1) if m <= n else 0)
    energy, swap = m*(m-1)*hm, m*cm
    tn = m*m*(m-1)*hp
    sn = m*(n*hm+cm-un)
    cross = m*m*(n*hp+cp)
    joint = tn+sn+2*cross
    scalar = 4*m*m*sum((n+m-2-j)**2*hook_weight(n,m-2,j)
                      for j in range(min(n,m-2)))
    numerator = 2*(n*n+4*n+2)*(energy+swap)-4*joint+(n+2)*scalar
    return Fraction(numerator, 2*hm*n*(n+1)*(n+2)*(n+3))


def main():
    covered = []
    pairings_count = sixth_pairings_count = monomial_count = 0
    for n in range(2, 7):
        for m in range(3, 8):
            if n ** m > 9000:
                continue
            ps = [trace_poly(n, k) for k in range(m + 1)]
            hm = norm(ps[m])
            H = hessian(ps[m])
            monomial_count += len(ps[m])
            ht = sum(norm(p) for p in H.values())
            diag = sum(norm(H.get((a * n + a, a * n + a), {})) for a in range(n))
            off = sum(norm(H.get((a * n + b, a * n + b), {}))
                      for a in range(n) for b in range(n) if a != b)
            check(ht == m * (m - 1) * hm, 'Hessian degree energy', n, m)
            check(Fraction(off, hm) <= Fraction(4 * m * (m - 1), n * (n + 1)),
                  'off-diagonal sphere estimate', n, m)

            T = [add(*(H.get((a * n + a, c * n + d), {}) for a in range(n)))
                 for c in range(n) for d in range(n)]
            S = [add(*(H.get((a * n + b, c * n + a), {}) for a in range(n)))
                 for b in range(n) for c in range(n)]
            A = add(*(H.get((a * n + a, c * n + c), {})
                      for a in range(n) for c in range(n)))
            BH = add(*(H.get((a * n + b, b * n + a), {})
                       for a in range(n) for b in range(n)))
            tn, sn, an, bn = sum(map(norm, T)), sum(map(norm, S)), norm(A), norm(BH)
            check(tn == m * m * (m - 1) * norm(ps[m - 1]), 'T exact norm', n, m)
            check(an == m * m * (m - 1) ** 2 * norm(ps[m - 2]), 'A exact norm', n, m)
            cpoly = add(*(times(ps[a], ps[m - a]) for a in range(1, m)))
            lower = times(ps[1], ps[m - 1])
            check(sn == m * (n * hm + inner(ps[m], cpoly) - inner(ps[m], lower)),
                  'Fock S operator exact identity', n, m)
            check(inner(ps[m], lower) >= 0, 'positive subtracted Wick term', n, m)
            check(sn <= m * (n + m - 1) * hm, 'sharp S bound', n, m)

            # Hook identities are checked through their exact norms and overlaps.
            check(norm(cpoly) == sum((m - 1 - 2 * j) ** 2 * hook_weight(n, m, j)
                                     for j in range(min(m, n))),
                  'cut-join hook norm/signs', n, m)
            check(inner(ps[m], cpoly) == sum((m - 1 - 2 * j) * hook_weight(n, m, j)
                                             for j in range(min(m, n))),
                  'cut-join hook overlap/signs', n, m)
            swap = sum(inner(H.get((a * n + b, c * n + d), {}),
                             H.get((c * n + b, a * n + d), {}))
                       for a in range(n) for b in range(n)
                       for c in range(n) for d in range(n))
            check(swap == m * inner(ps[m], cpoly), 'exact partial-swap cut-join', n, m)
            symnorm = Fraction(ht + swap, 2)
            check(hm >= (n + 1) * norm(ps[m - 1]), 'h ratio one', n, m)
            check(hm >= (n + 1) ** 2 * norm(ps[m - 2]), 'h ratio two', n, m)

            denom = (n + 1) * (n + 2) * (n + 3)
            bound_num = 4 * ht + 8 * (tn + sn) + 2 * (an + bn)
            check(diag * denom <= bound_num, '24-contraction norm bound', n, m)

            if n <= 4 and m <= 5:
                bins = Counter()
                for sigma in permutations(range(4)):
                    cross, value = sphere_pairing(H, n, sigma)
                    bins[cross] += value
                    pairings_count += 1
                check(sum(bins.values()) == diag * denom, 'exact Haar sphere identity', n, m)
                check(bins[4] <= 4 * ht, 'four cross-link terms', n, m)
                check(bins[2] <= 8 * (tn + sn), 'sixteen two-cross terms', n, m)
                check(bins[0] <= 2 * (an + bn), 'four zero-cross terms', n, m)
                vnum = sum(sixth_pairing(H, n, sigma) for sigma in permutations(range(3)))
                sixth_pairings_count += 6
                vv = Fraction(vnum, n * (n + 1) * (n + 2))
                check(vv >= 0, 'sixth-sphere V positivity', n, m)
                check(vnum <= 2 * ht + 2 * (tn + sn), 'sixth-sphere contraction bound', n, m)
                check(off == Fraction(4 * symnorm, n * (n + 1)) - 4 * vv + Fraction(2 * diag, n),
                      'exact off-diagonal projection identity', n, m)

            gi = hm
            bi = sum(c * c for c in ps[m].values())
            collision_twice = sum(c * c * prod(factorial(v) for v in nu)
                                   * sum(v * (v - 1) for v in nu)
                                   for nu, c in ps[m].items())
            check(collision_twice == diag + off, 'marked-edge Hessian identity', n, m)
            check(4 * (gi - bi) <= diag + off, 'relative deficit Hessian reduction', n, m)
            collision_mean = Fraction(collision_twice, 2 * hm)
            check(collision_mean == closed_collision_mean(n,m),
                  'closed finite hook collision mean', n,m)
            if m >= n+2:
                rational_mean=Fraction(2*m*((n+5)*m*(m+1)-(n+2)*(n+3)),
                                       (n+1)*(n+2)*(n+3)*(m+2))
                check(collision_mean == rational_mean,
                      'closed rational mean in exact m>=N+2 range',n,m)
            general_bound = Fraction(2 * m * (m - 1), n * (n + 1)) + (
                4 * m * (m - 1) + Fraction(8 * m * m * (m - 1), n + 1)
                + 8 * m * (n + m - 1)
                + Fraction(2 * m * m * ((m - 1) ** 2 + (2 * n + m) ** 2), (n + 1) ** 2)
            ) / (2 * denom)
            check(collision_mean <= general_bound, 'all-m marked collision bound', n, m)
            # Jensen and n!<=2^binom(n,2), checked without decimal exponentials.
            ratio = Fraction(bi, gi)
            check(ratio ** collision_mean.denominator * 2 ** collision_mean.numerator >= 1,
                  'exact rational Jensen bound', n, m)
            if m <= n:
                upper = Fraction(m * (m - 1), n * (n + 1)) + Fraction(15 * m, n * n)
                check(Fraction(gi - bi, gi) <= upper, 'final theorem', n, m)
                check(Fraction(diag, hm) <= Fraction(60 * m, n * n),
                      'final diagonal bound', n, m)
            covered.append({'N': n, 'm': m, 'monomials': len(ps[m]),
                            'S_norm_over_h_m': str(Fraction(sn, hm)),
                            'collision_mean': str(Fraction(diag + off, 2 * hm))})

    # Exact hook-weight edge cases include m=N and all 1<=N<=40, 2<=m<=80.
    ratio_checks = 0
    for n in range(1, 41):
        for m in range(2, 81):
            hm = sum(hook_weight(n, m, j) for j in range(min(n, m)))
            hp = sum(hook_weight(n, m - 1, j) for j in range(min(n, m - 1)))
            check(hm >= (n + 1) * hp, 'large exact hook ratio', n, m)
            hook_mean = Fraction(sum(j * hook_weight(n, m, j) for j in range(min(n, m))), hm)
            check(hook_mean <= Fraction(n - 1, m), 'exact hook-mean geometric bound', n, m)
            ratio_checks += 1

    large_means = []
    for n in (64,128,256,512):
        for numerator, denominator in ((1,2),(1,1),(2,1)):
            m=n*numerator//denominator
            mean=closed_collision_mean(n,m)
            large_means.append({'N':n,'m':m,'mean_display':float(mean),
                                'limiting_reference_display':2*(m/n)**2,
                                'arithmetic':'exact Fraction evaluation; decimals are displays'})

    print(json.dumps({'status': 'PASS', 'arithmetic': 'integer Gaussian polynomial norms and rationals',
                      'covered_cases': covered, 'trace_monomials': monomial_count,
                      'explicit_eighth_sphere_pairings': pairings_count,
                      'explicit_sixth_sphere_pairings': sixth_pairings_count,
                      'hook_ratio_checks': ratio_checks,
                      'larger_exact_collision_means':large_means,
                      'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'scope': 'Finite algebra only; theorem proof is the accompanying Markdown.'}, indent=2))


if __name__ == '__main__':
    main()
