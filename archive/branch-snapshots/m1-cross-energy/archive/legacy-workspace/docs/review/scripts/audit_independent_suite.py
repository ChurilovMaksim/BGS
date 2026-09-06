"""
AUDIT SUITE - fully independent re-implementation (two-key rule).
No imports from BGS/src. Exact integer modular arithmetic throughout.

Verifies against paper/resonance_laws_catmaps.tex:
  V1  Thm core:      sol+-+-(H) = 2k^2-k (k odd) / 3k(k-1) (k even)
  V2  Lem zerocounts: Z2=p-1, Z3=(p-1)(p-2), Z4=(p-1)(p^2-3p+3)
  V3  Thm meanlaw:    sum over ALL labels (complete enumeration, small p)
                      of N3(a,b) equals k^3 * Z4^2; <N3>= k^3 Z4^2/(p-1)^8
  V4  Conj tight:     N3 <= floor(k^2/p)+2 for GENERIC patterns
                      (explicit genericity filter, fresh grid incl.
                       boundary zone frac(k^2/p) ~ 1)
  V5  Collision lemma C(u,v) <= 4
  V6  Prop r6strata:  [6]=k, [2,4]=9k(k-1) (both parities),
                      [2,2,2]_slotwise = 6k(k-1)(k-2) (odd k)
  V7  manual anchors: p=5,H={+-1} -> 6 solutions decomposing {ab:2,a:2,b:2}
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import json, math, sys, time
from itertools import product

OUT = {}

def prime_decs(n):
    d, fs = 2, []
    while d * d <= n:
        while n % d == 0:
            fs.append(d); n //= d
        d += 1
    if n > 1: fs.append(n)
    return fs

def tonelli(a, p):
    """sqrt mod p, p odd prime; None if non-residue."""
    a %= p
    if a == 0: return 0
    if pow(a, (p - 1) // 2, p) != 1: return None
    if p % 4 == 3: return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1: z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1: t2 = t2 * t2 % p; i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b % p * b % p, r * b % p
    return r

def subgroup(p, k):
    """elements of the order-k subgroup of F_p^x (assumes k | p-1)."""
    # find generator of F_p^x
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in prime_decs(p - 1)):
            break
    a = pow(g, (p - 1) // k, p)
    H, x = [], 1
    for _ in range(k):
        H.append(x); x = x * a % p
    return H

# ---------------- V1: matched identity ----------------
def sol4_matched_direct(p, H):
    """same by direct O(k^2) hash on (sum, invsum) without sign gymnastics"""
    inv = {h: pow(h, p - 2, p) for h in H}
    cnt = 0
    pair = {}
    for h1 in H:
        s1, t1 = h1 % p, inv[h1]
        for h3 in H:
            key = ((s1 + h3) % p, (t1 + inv[h3]) % p)
            pair[key] = pair.get(key, 0) + 1
    for h2 in H:
        s2, t2 = h2 % p, inv[h2]
        for h4 in H:
            key = ((s2 + h4) % p, (t2 + inv[h4]) % p)
            cnt += pair.get(key, 0)
    return cnt

def sol4_bruteforce(p, H):
    """literal O(k^4) enumeration - ground truth"""
    inv = {h: pow(h, p - 2, p) for h in H}
    c = 0
    for h1 in H:
        for h2 in H:
            for h3 in H:
                for h4 in H:
                    if (h1 - h2 + h3 - h4) % p == 0 and \
                       (inv[h1] - inv[h2] + inv[h3] - inv[h4]) % p == 0:
                        c += 1
    return c

def v1():
    res = []
    for p in (5, 7, 11, 13, 31, 41, 61, 101, 211, 401, 601):
        pk = prime_decs(p - 1)
        ks = sorted({d for d in range(2, p - 1) if (p - 1) % d == 0})
        for k in ks[:6]:
            H = subgroup(p, k)
            fast = sol4_matched_direct(p, H)
            pred = 3 * k * (k - 1) if k % 2 == 0 else 2 * k * k - k
            ok = (fast == pred)
            row = dict(p=p, k=k, counted=fast, formula=pred, ok=ok)
            if k <= 5:  # ground truth for tiny k
                bf = sol4_bruteforce(p, H)
                row["brute"] = bf
                ok = ok and bf == fast
            row["ok"] = bool(ok)
            res.append(row)
            if not ok:
                print("V1 FAIL", row)
    bad = [r for r in res if not r["ok"]]
    print(f"V1 matched identity: {len(res)-len(bad)}/{len(res)} pass")
    OUT["V1"] = dict(passed=len(res) - len(bad), total=len(res), rows=res)
    return not bad

def v7():
    p = 5
    H = subgroup(p, 2)  # {1,4} = {1,-1}
    inv = {h: pow(h, p - 2, p) for h in H}
    sols = [(h1, h2, h3, h4) for h1 in H for h2 in H for h3 in H for h4 in H
            if (h1 - h2 + h3 - h4) % p == 0 and
               (inv[h1] - inv[h2] + inv[h3] - inv[h4]) % p == 0]
    def typ(t):
        h1, h2, h3, h4 = t
        if h1 == h2 and h3 == h4: return "ab"
        if h1 == h4 and h2 == h3: return "ab"
        if h1 == h2 and h3 == h4: return "ab"
        if h2 == h1 and h4 == h3: return "ab"
        if h3 == -h1 % p and h4 == -h2 % p: return "S0"
        return "?"
    types = {}
    for t in sols:
        h1, h2, h3, h4 = t
        if (h1 == h2 and h3 == h4) or (h1 == h4 and h2 == h3):
            ty = "pairing"
        else:
            ty = "OTHER"
        types[ty] = types.get(ty, 0) + 1
    # k=2 is degenerate: H = {1,-1}, so every S=0 tuple already lies in
    # the pairing union; honest check is total == 3k(k-1) == 6, no OTHER.
    ok = len(sols) == 6 and types.get("OTHER", 0) == 0
    print(f"V7 anchor p=5,k=2: total={len(sols)} types={types} "
          f"{'PASS' if ok else 'FAIL'}")
    OUT["V7"] = dict(total=len(sols), types=types, ok=bool(ok))

# ---------------- V2: zero counts ----------------
def v2():
    from itertools import product
    res = []
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        G = list(range(1, p))

        def sols(cs):
            return sum(1 for t in product(G, repeat=len(cs))
                       if sum(ci * xi for ci, xi in zip(cs, t)) % p == 0)

        z2 = sols([1, 1])
        z3 = sols([1, 1, 1])
        z4 = sols([1, 1, 1, 1])
        e2, e3 = p - 1, (p - 1) * (p - 2)
        e4 = (p - 1) * (p * p - 3 * p + 3)
        # independence of coefficients: only for p where these are nonzero
        row = dict(p=p, z2=z2, z3=z3, z4=z4, e2=e2, e3=e3, e4=e4)
        if p > 11:
            c = [3, 5, 7, 11]
            z4c = sols([c[0], c[1], c[2], c[3]])
            row["z4_coeffs"] = z4c
            row["ok"] = bool(z2 == e2 and z3 == e3 and z4 == e4
                             and z4c == e4)
        else:
            row["ok"] = bool(z2 == e2 and z3 == e3 and z4 == e4)
        res.append(row)
        if not row["ok"]:
            print("V2 FAIL", row)
    npass = sum(r["ok"] for r in res)
    print(f"V2 zero counts: {npass}/{len(res)} pass")
    OUT["V2"] = dict(passed=npass, total=len(res), rows=res)
    return npass == len(res)

# ---------------- V3: mean law, complete enumeration ----------------
def v3():
    import numpy as np
    res = []
    for p in (5, 7):
        G = np.arange(1, p, dtype=np.int64)
        L = len(G) ** 8
        # build all label combos via meshgrid (memory-safe for p<=7)
        grids = np.meshgrid(*([G] * 8), indexing="ij")
        A1, A2, A3, A4, B1, B2, B3, B4 = [g.ravel() for g in grids]
        del grids
        tot = {}
        for k in range(2, p - 1):
            if (p - 1) % k: continue
            H = subgroup(p, k)
            invH = {h: pow(h, p - 2, p) for h in H}
            cnt = 0
            for x in H:
                ix = invH[x]
                for y in H:
                    iy = invH[y]
                    for z in H:
                        iz = invH[z]
                        m1 = (A1 - A2 * x + A3 * y - A4 * z) % p == 0
                        m2 = (B1 - B2 * ix + B3 * iy - B4 * iz) % p == 0
                        cnt += int(np.count_nonzero(m1 & m2))
            exact_sum = k ** 3 * ((p - 1) * (p * p - 3 * p + 3)) ** 2
            ok = cnt == exact_sum
            res.append(dict(p=p, k=k, enumerated_total=cnt,
                            formula_total=int(exact_sum), ok=bool(ok)))
            if not ok: print("V3 FAIL", res[-1])
            else: print(f"V3 p={p} k={k}: COMPLETE enum matches "
                        f"k^3*Z4^2 = {cnt}")
    OUT["V3"] = res
    return all(r["ok"] for r in res)

# ---------------- V4: tail bound, fresh grid ----------------
def generic_ok(p, a, b):
    if (a[0]*b[2] - a[2]*b[0]) % p == 0: return False
    if (a[1]*b[3] - a[3]*b[1]) % p == 0: return False
    for (i, j) in ((0, 1), (0, 3), (1, 2), (2, 3)):
        if (a[i]*b[j] - a[j]*b[i]) % p == 0: return False
    return True

def n3_mitm(p, H, a, b):
    """reduced count N3 over H^3 - independent MITM implementation."""
    Hl = list(H)
    inv = {h: pow(h, p - 2, p) for h in H}
    right = {}
    for u2 in Hl:
        iu2 = inv[u2]
        for u3 in Hl:
            iu3 = inv[u3]
            right.setdefault((b[1]*iu2 - b[2]*iu3) % p, []).append((u2, u3))
    cnt = 0
    ia4 = pow(a[3], p - 2, p)
    for u2 in Hl:
        iu2 = inv[u2]
        for u3 in Hl:
            iu3 = inv[u3]
            num = (a[0] - a[1]*u2 + a[2]*u3) % p
            u4 = num * ia4 % p
            if u4 not in inv: continue
            lhs = (b[0] - b[1]*iu2 + b[2]*iu3) % p
            rhs = b[3] * inv[u4] % p
            if lhs == rhs: cnt += 1
    return cnt

def v4(trials_per_cfg=400, seed=20260826):
    import random
    rng = random.Random(seed)
    res = []
    primes = [353, 503, 719, 1009, 1447, 2003, 2909, 3571, 4001, 5003]
    viol = 0
    checked = 0
    degenerate_skipped = 0
    for p in primes:
        ks = sorted({d for d in range(3, p) if (p - 1) % d == 0 and d <= 260})
        if not ks: continue
        # boundary zone: frac(k^2/p) close to 1, plus extreme divisors
        chosen = set([ks[0], ks[-1], ks[len(ks) // 2]] +
                     [k for k in ks if 0.85 < (k * k % p) / p][:2] +
                     ks[:2])
        for k in sorted(chosen)[:6]:
            H = subgroup(p, k)
            mx = 0
            for _ in range(trials_per_cfg):
                a = [rng.randrange(1, p) for _ in range(4)]
                b = [rng.randrange(1, p) for _ in range(4)]
                if not generic_ok(p, a, b):
                    degenerate_skipped += 1
                    continue
                n = n3_mitm(p, H, a, b)
                if n > mx: mx = n
            bound = k * k // p + 2
            ok = mx <= bound
            checked += 1
            if not ok: viol += 1
            res.append(dict(p=p, k=k, maxN3=mx, floor_plus2=bound,
                            kp2=round(k * k / p, 3), ok=bool(ok)))
            if not ok: print("V4 VIOLATION", res[-1])
    npass = sum(r["ok"] for r in res)
    print(f"V4 tail bound: {npass}/{len(res)} configs pass "
          f"(violations={viol}, degenerate patterns skipped="
          f"{degenerate_skipped})")
    OUT["V4"] = dict(passed=npass, total=len(res), violations=viol,
                     skipped_degenerate=degenerate_skipped, rows=res)
    return viol == 0

# ---------------- V5: collision lemma ----------------
def v5(seed=777):
    import random
    rng = random.Random(seed)
    worst = 0
    cases = 0
    for p in (101, 211, 401, 757, 1201):
        for k in (8, 12, 20, 24):
            if (p - 1) % k: continue
            H = subgroup(p, k)
            Hs = set(H)
            inv = {h: pow(h, p - 2, p) for h in H}
            # enumerate collision counts for all (u,v) arising from pairs
            cc = {}
            for h in H:
                ih = inv[h]
                for h2 in H:
                    u = (h - h2) % p
                    v = (ih - inv[h2]) % p
                    if u == 0 and v == 0: continue
                    cc[(u, v)] = cc.get((u, v), 0) + 1
            mx = max(cc.values())
            worst = max(worst, mx)
            cases += 1
            if mx > 4:
                print(f"V5 FAIL p={p} k={k} max={mx}")
    ok = worst <= 4
    print(f"V5 collision lemma: worst={worst} over {cases} (p,k) configs "
          f"({'PASS' if ok else 'FAIL'})")
    OUT["V5"] = dict(worst=worst, cases=cases, ok=bool(ok))
    return ok

# ---------------- V6: r=6 strata ----------------
def v6():
    res = []
    for p, k in ((11, 5), (11, 10), (31, 5), (31, 6), (31, 10), (41, 8),
                 (61, 6), (61, 10), (101, 10), (7, 3), (7, 6), (13, 4)):
        if (p - 1) % k: continue
        H = subgroup(p, k)
        inv = {h: pow(h, p - 2, p) for h in H}
        # enumerate all 6-tuples with signs +,-,+,-,+,-
        # group by value-multiset pattern
        from collections import Counter
        strata = Counter()
        total = 0
        # represent tuple as exponents 0..k-1
        for e1 in range(k):
            h1 = H[e1]
            for e2 in range(k):
                s1 = (h1 - H[e2]) % p
                t1 = (inv[h1] - inv[H[e2]]) % p
                for e3 in range(k):
                    s2 = (s1 + H[e3]) % p
                    t2 = (t1 + inv[H[e3]]) % p
                    for e4 in range(k):
                        s3 = (s2 - H[e4]) % p
                        t3 = (t2 - inv[H[e4]]) % p
                        for e5 in range(k):
                            s4 = (s3 + H[e5]) % p
                            t4 = (t3 + inv[H[e5]]) % p
                            for e6 in range(k):
                                if (s4 - H[e6]) % p: continue
                                if (t4 - inv[H[e6]]) % p: continue
                                vals = [H[i] for i in (e1, e2, e3, e4, e5, e6)]
                                c = Counter(vals)
                                patt = tuple(sorted(c.values(),
                                                    reverse=True))
                                strata[patt] += 1
                                total += 1
        row = dict(p=p, k=k, total=total,
                   S6=strata.get((6,), 0),
                   S24=strata.get((4, 2), 0) + strata.get((2, 4), 0),
                   S222=strata.get((2, 2, 2), 0),
                   e6=k, e24=9 * k * (k - 1),
                   e222=6 * k * (k - 1) * (k - 2))
        ok6 = row["S6"] == row["e6"]
        ok24 = row["S24"] == row["e24"]
        ok222 = (row["S222"] == row["e222"]) if k % 2 == 1 else True
        row["ok"] = bool(ok6 and ok24 and ok222)
        res.append(row)
        if not row["ok"]: print("V6 FAIL", row)
    npass = sum(r["ok"] for r in res)
    print(f"V6 r=6 strata: {npass}/{len(res)} pass")
    OUT["V6"] = dict(passed=npass, total=len(res), rows=res)
    return npass == len(res)

if __name__ == "__main__":
    t0 = time.time()
    def dump():
        with open(_BGS_ROOT + r"\artifacts\audit_independent_suite.json", "w") as f:
            json.dump(OUT, f, indent=1)
    v7(); dump()
    r1 = v1(); dump()
    r2 = v2(); dump()
    r3 = v3(); dump()
    r5 = v5(); dump()
    r6 = v6(); dump()
    r4 = v4(); dump()
    OUT["_runtime_s"] = round(time.time() - t0, 1)
    print("TOTAL runtime", OUT["_runtime_s"], "s")
    print("SUMMARY:", dict(V1=r1, V2=r2, V3=r3, V4=r4, V5=r5, V6=r6))
