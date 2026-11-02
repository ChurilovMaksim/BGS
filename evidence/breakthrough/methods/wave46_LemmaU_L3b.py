#!/usr/bin/env python3
"""Wave 46, task 2, follow-up: split-prime L3 census, (5,2) Dickson failure
mode, lam=21 example, scaling-block breakdown + degenerate-B scan."""
import sys
sys.path.insert(0, '.')
from wave46_LemmaU_L3 import (rmul, rpow, build, dickson, poly_of_values,
                               component_report)
from collections import Counter
from math import gcd

# 1. scan split primes (p = +-1 mod 8, so 2 is QR mod p) for odd constraining u
print("== split-prime scan (odd u, alpha^u == -1 mod p)")
cands = []
for p in [7, 17, 23, 31, 41, 47, 71, 73, 79, 89, 97, 103, 113, 127, 137, 151, 167, 191, 193, 199, 233, 239]:
    if p % 8 not in (1, 7): continue
    al = (3 % p, 2 % p)
    for u in range(1, 400, 2):
        if rpow(al, u, p) == (p - 1, 0):
            cands.append((p, u)); print(f"   p={p} u={u} params={p*p}"); break
print("cands:", cands)

# 2. (5,2) Dickson failure mode for C=(0,1)
mod, beta, ob, cyc, per, norm = build(5, 2, 15)
i0 = 0 * mod + 1
T, N = per[i0], norm[i0]
vals = cyc[i0][:T]
P = poly_of_values(vals, mod)
Ct = rpow((0, 1), T, mod); theta = (2 * Ct[0]) % mod
D = dickson(T, N, mod); D[0] = (D[0] - theta) % mod
print(f"== (5,2) C=sqrt2: T={T} N={N} theta={theta} ord(beta)={ob}")
print(f"   P==D mod 25? {P == D}")
diff = [(k, P[k] if k < len(P) else 0, D[k] if k < len(D) else 0) for k in range(max(len(P), len(D))) if (P[k] if k < len(P) else 0) != (D[k] if k < len(D) else 0)]
print(f"   differing coeffs (k, P_k, D_k): {diff[:8]}")
P5 = [c % 5 for c in P]
# X^T - theta mod 5
X5 = [(-theta) % 5] + [0]*(T - 1) + [1]
print(f"   P == X^T - theta (mod 5)? {P5 == X5}")

# 3. lam=21 example at m=30
modA, betaA, obA, cycA, perA, normA = build(5, 2, 15)
modB, betaB, obB, cycB, perB, normB = build(29, 1, 15)
ia = 0 * modA + 1  # sqrt2
Ta = perA[ia]; pv = cycA[ia][:Ta]
pos = {v: j for j, v in enumerate(pv)}
lam = 21
sigma = [pos[(lam * v) % modA] for v in pv]
print(f"== lam=21 on sqrt2-cycle mod 25: T_a={Ta} distinct={len(set(pv)) == Ta}")
print(f"   period values: {pv}")
print(f"   sigma_21: {sigma}")
for (ba, bb) in [(1, 2), (0, 1), (2, 3)]:
    jb = ba * modB + bb; Tb = perB[jb]; g = gcd(Ta, Tb)
    viol = [a for a in range(Ta) if sigma[a] % g != a % g]
    t, s = cycA[ia], cycB[jb]
    b0 = sorted(zip(t, s)); b1 = sorted((((-a) % modA, (-b) % modB) for a, b in zip(t, s)))
    b0p = sorted((((lam * a) % modA, b) for a, b in zip(t, s)))
    b1p = sorted((((-a) % modA, (-b) % modB) for a, b in b0p))
    same = sorted(b0p + b1p) == sorted(b0 + b1)
    print(f"   B=({ba},{bb}): T_b={Tb} g={g} sigma-violations={viol} blocks-equal={same}")

# 4. scaling-block breakdown + degenerate-B scan
mA = {}
for i in range(len(cycA)): mA.setdefault(tuple(sorted(cycA[i])), []).append(i)
unitsA = [l for l in range(modA) if gcd(l, modA) == 1]
from collections import defaultdict
br = defaultdict(lambda: [0, 0])  # (g, kind) -> [tested, collisions]
dis = []
for k, idxs in mA.items():
    mult = [l for l in unitsA if tuple(sorted((l * v) % modA for v in k)) == k]
    for lam_ in mult:
        if lam_ == 1: continue
        i0_ = idxs[0]; Ta_ = perA[i0_]; pv_ = cycA[i0_][:Ta_]
        if len(set(pv_)) != Ta_: continue
        pos_ = {v: j for j, v in enumerate(pv_)}
        if any((lam_ * v) % modA not in pos_ for v in pv_): continue
        sig_ = [pos_[(lam_ * v) % modA] for v in pv_]
        for j in range(len(cycB)):
            Tb_ = perB[j]; g_ = gcd(Ta_, Tb_)
            sv = cycB[j][:Tb_]
            sdist = len(set(sv)) == Tb_
            svals = set(sv); sneg = all(((-v) % modB) not in svals for v in svals)
            pred = all(sig_[a] % g_ == a % g_ for a in range(Ta_))
            t_, s_ = cycA[i0_], cycB[j]
            b0_ = sorted(zip(t_, s_)); b1_ = sorted((((-a) % modA, (-b) % modB) for a, b in zip(t_, s_)))
            b0p_ = sorted((((lam_ * a) % modA, b) for a, b in zip(t_, s_)))
            b1p_ = sorted((((-a) % modA, (-b) % modB) for a, b in b0p_))
            act = sorted(b0p_ + b1p_) == sorted(b0_ + b1_)
            if sdist and sneg:
                kind = 'g1' if g_ == 1 else ('sigma-id' if all(x == a for a, x in enumerate(sig_)) else 'genuine')
                br[(g_, kind)][0] += 1; br[(g_, kind)][1] += act
                if pred != act: dis.append(('generic', i0_, lam_, j, pred, act))
            else:
                br[('degen', 'sdist' if sdist else 'srep', 'negfree' if sneg else 'negpair')][0] += 1
                br[('degen', 'sdist' if sdist else 'srep', 'negfree' if sneg else 'negpair')][1] += act
                if pred != act: dis.append(('degen', i0_, lam_, j, pred, act, sdist, sneg))
print("== breakdown (key -> [tested, collisions]):")
for kk in sorted(br, key=str): print(f"   {kk}: {br[kk]}")
print(f"   generic disagreements: {sum(1 for d in dis if d[0] == 'generic')}")
print(f"   degenerate disagreements: {sum(1 for d in dis if d[0] == 'degen')}")
for d in dis[:10]: print("     DIS", d)
