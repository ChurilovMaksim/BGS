#!/usr/bin/env python3
"""Wave 46, task 2: Lemma U, L3 + degenerate locus.

Single-component L3 test: M(x) + M(x') = M(t) + M(-t) (multisets over Z/u)
  => {M(x), M(x')} = {M(t), M(-t)} ?
Plus: Dickson identity check P_x(X) = D_T(X,N) - Tr(C^T) (the proof's lemma),
multiplier groups {lam : lam*M = M}, and the m=30 scaling-block lemma scan:
  one-sided scaling lam preserves block0 iff sigma_lam(a) == a (mod g),
  g = gcd(T_a, T_b), sigma_lam = value permutation induced by lam.
Conventions (wave45_census_m110.cpp): R = Z[sqrt2] mod mod, alpha = (3,2),
beta = alpha^2, Tr(a+b sqrt2) = 2a, cycle[k] = Tr(C beta^k), k in Z/u.
"""
from collections import Counter

def rmul(x, y, mod):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % mod, (x[0]*y[1] + x[1]*y[0]) % mod)

def rpow(x, n, mod):
    r = (1 % mod, 0)
    while n:
        if n & 1: r = rmul(r, x, mod)
        x = rmul(x, x, mod); n >>= 1
    return r

def build(p, f, u):
    mod = p ** f
    alpha = (3 % mod, 2 % mod)
    assert rpow(alpha, u, mod) == (mod - 1, 0), f"not constraining p={p} f={f} u={u}"
    beta = rmul(alpha, alpha, mod)
    bp = [(1, 0)]
    for _ in range(1, u): bp.append(rmul(bp[-1], beta, mod))
    # order of beta
    ob = None
    for d in range(1, u + 1):
        if u % d == 0 and rpow(beta, d, mod) == (1 % mod, 0): ob = d; break
    cyc, per, norm = [], [], []
    for a in range(mod):
        for b in range(mod):
            C = (a, b)
            cy = [(2 * rmul(C, bp[k], mod)[0]) % mod for k in range(u)]
            T = u
            for d in range(1, u + 1):
                if u % d == 0 and all(cy[k] == cy[k % d] for k in range(u)): T = d; break
            cyc.append(tuple(cy)); per.append(T)
            norm.append((a*a - 2*b*b) % mod)
    return mod, beta, ob, cyc, per, norm

# ---- polynomials mod mod (coeffs lowest-first) ----
def pmul(A, B, mod):
    R = [0]*(len(A)+len(B)-1)
    for i, a in enumerate(A):
        for j, b in enumerate(B): R[i+j] = (R[i+j] + a*b) % mod
    return R
def dickson(T, N, mod):
    # D_0=2, D_1=X, D_{n+1} = X D_n - N D_{n-1}
    if T == 0: return [2 % mod]
    D0, D1 = [2 % mod], [0, 1 % mod]
    if T == 1: return D1
    for _ in range(2, T+1):
        D2 = [0] + D1[:]  # X*D1
        for i, c in enumerate(D0): D2[i] = (D2[i] - N*c) % mod
        D0, D1 = D1, D2
    return D1
def poly_of_values(vals, mod):
    P = [1 % mod]
    for v in vals: P = pmul(P, [(-v) % mod, 1 % mod], mod)
    return P

def component_report(p, f, u, label):
    mod, beta, ob, cyc, per, norm = build(p, f, u)
    n = len(cyc)
    print(f"== {label}: p={p} f={f} u={u} mod={mod} params={n} ord(beta)={ob}")
    # Dickson check on period values (nonsingular vs singular split).
    # f==1: evaluate both sides at T+1 points (conclusive over F_p).
    # f>=2: full polynomial comparison.
    from math import gcd
    dpass = dpass_ns = dtot_ns = dtot_sg = 0
    betaT1 = 0
    def peval(P, x):
        s = 0
        for c in reversed(P): s = (s*x + c) % mod
        return s
    for i in range(n):
        T, N = per[i], norm[i]
        vals = cyc[i][:T]
        a, b = divmod(i, mod)[0], i % mod
        Ct = rpow((a, b), T, mod)
        theta = (2 * Ct[0]) % mod
        if f == 1:
            D = dickson(T, N, mod)
            D[0] = (D[0] - theta) % mod
            ok = True
            for x in range(T + 1):
                lhs = 1
                for v in vals: lhs = lhs * ((x - v) % mod) % mod
                if lhs != peval(D, x): ok = False; break
        else:
            P = poly_of_values(vals, mod)
            D = dickson(T, N, mod)
            D[0] = (D[0] - theta) % mod
            ok = (len(P) == len(D) and all(x == y for x, y in zip(P, D)))
        ns = (gcd(N, mod) == 1)
        if ns: dtot_ns += 1; dpass_ns += ok
        else: dtot_sg += 1
        dpass += ok
        if rpow(beta, T, mod) == (1 % mod, 0): betaT1 += 1
    print(f"   Dickson: pass {dpass}/{n} (nonsingular {dpass_ns}/{dtot_ns}, "
          f"singular {dtot_sg} params); beta^T==1 for {betaT1}/{n}")
    # distinct multisets
    mset = {}
    for i in range(n): mset.setdefault(tuple(sorted(cyc[i])), []).append(i)
    r = len(mset)
    print(f"   distinct multisets: {r}")
    # L3 decomposition test
    keys = list(mset.keys())
    cnt = {k: Counter(k) for k in keys}
    neg = {k: tuple(sorted(((-v) % mod) for v in k)) for k in keys}
    keyset = set(keys)
    viol = []
    negsym = 0
    for t in keys:
        S = cnt[t] + cnt[neg[t]]
        if neg[t] == t: negsym += 1
        for x in keys:
            if any(cnt[x][v] > S[v] for v in cnt[x]): continue
            rem = S - cnt[x]
            remkey = tuple(sorted(rem.elements()))
            if remkey in keyset and {x, remkey} != {t, neg[t]}:
                viol.append((t, x, remkey))
    print(f"   negation-symmetric multisets: {negsym}")
    print(f"   L3 violations: {len(viol)}")
    for v in viol[:5]: print(f"     VIOL t={v[0]} x={v[1]} x'={v[2]}")
    # multiplier groups
    import math
    units = [lam for lam in range(mod) if math.gcd(lam, mod) == 1]
    maxmult = 0; nontriv = []
    for k in keys:
        mult = [lam for lam in units if tuple(sorted((lam*v) % mod for v in k)) == k]
        if len(mult) > maxmult: maxmult = len(mult)
        if any(lam not in (1 % mod, (mod-1) % mod) for lam in mult):
            nontriv.append((k, mult))
    print(f"   max multiplier group size: {maxmult}; multisets with lam not in {{+-1}}: {len(nontriv)}")
    for k, mult in nontriv[:5]: print(f"     MULT {k} -> {mult}")
    return mod, cyc, per, mset

def scaling_block_scan():
    """m=30: A-side mod 25 (u=15), B-side mod 29 (u=15). For each A-param with
    a nontrivial multiplier lam, and each B-param: predict collision iff
    sigma_lam(a) == a (mod g) for all a; compare with direct block union."""
    from math import gcd
    modA, betaA, obA, cycA, perA, normA = build(5, 2, 15)
    modB, betaB, obB, cycB, perB, normB = build(29, 1, 15)
    unitsA = [lam for lam in range(modA) if gcd(lam, modA) == 1]
    # distinct A multisets and their multipliers
    mA = {}
    for i in range(len(cycA)): mA.setdefault(tuple(sorted(cycA[i])), []).append(i)
    tested = agree = coll = coll_pred = 0
    bad = []
    for k, idxs in mA.items():
        mult = [lam for lam in unitsA if tuple(sorted((lam*v) % modA for v in k)) == k]
        for lam in mult:
            if lam == 1: continue
            # representative param + its period values (need distinct for sigma)
            i0 = idxs[0]; T_a = perA[i0]
            per_vals = cycA[i0][:T_a]
            if len(set(per_vals)) != T_a: continue  # sigma undefined
            pos = {v: j for j, v in enumerate(per_vals)}
            if any((lam*v) % modA not in pos for v in per_vals): continue
            sigma = [pos[(lam*v) % modA] for v in per_vals]
            for j in range(len(cycB)):
                T_b = perB[j]
                if len(set(cycB[j][:T_b])) != T_b: continue
                svals = set(cycB[j][:T_b])
                negfree = all(((-v) % modB) not in svals for v in svals)
                if not negfree: continue
                g = gcd(T_a, T_b)
                pred = all(sigma[a] % g == a % g for a in range(T_a))
                # direct: block0' = {(lam*t_k, s_k)}, block1' = -block0'
                t, s = cycA[i0], cycB[j]
                b0 = sorted(zip(t, s)); b1 = sorted((((-a) % modA, (-b) % modB) for a, b in zip(t, s)))
                b0p = sorted((((lam*a) % modA, b) for a, b in zip(t, s)))
                b1p = sorted((((-a) % modA, (-b) % modB) for a, b in b0p))
                actual = (sorted(b0p + b1p) == sorted(b0 + b1))
                tested += 1; agree += (pred == actual); coll += actual; coll_pred += pred
                if pred != actual: bad.append((i0, lam, j, pred, actual))
    print(f"== scaling-block scan m=30: tested={tested} agree={agree} "
          f"collisions={coll} predicted={coll_pred} disagreements={len(bad)}")
    for b in bad[:5]: print(f"     DISAGREE Aparam={b[0]} lam={b[1]} Bparam={b[2]} pred={b[3]} actual={b[4]}")

if __name__ == "__main__":
    component_report(53, 1, 27, "m=54 A-side")
    component_report(197, 1, 27, "m=54 B-side")
    component_report(5, 2, 15, "m=30 A-side (f=2)")
    scaling_block_scan()
