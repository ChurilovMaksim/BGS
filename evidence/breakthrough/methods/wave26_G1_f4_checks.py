"""Wave 26, task 1: G1 at f=4 — checks.
Exact integers, R = Z[sqrt2] as pairs (a,b) mod P.
1. Lemma 5 check at (36,3) mod 27 and (108,3) mod 81 (k=1 cases).
2. Full G1' check at (108,3) mod 81: all A, group by global multiset,
   per-class multisets D4-related?
3. (2,2) mechanism at p=13 mod 13^4: Lemma 5 shapes (2k=4=f, linear),
   v=1 coset invariance under Tr(eta0)=0 twist, v=2 singleton shift,
   pooled digit check on sampled full sequences (m=2366).
4. k / L0 checks for p=3,13.
"""
import random
from collections import Counter

def add(x, y, P): return ((x[0]+y[0]) % P, (x[1]+y[1]) % P)
def mul(x, y, P): return ((x[0]*y[0]+2*x[1]*y[1]) % P, (x[0]*y[1]+x[1]*y[0]) % P)
def tr(x, P): return (2*x[0]) % P
def pw(x, n, P):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, x, P)
        x = mul(x, x, P); n >>= 1
    return r

ALPHA = (3, 2)

def vp_int(n, p):
    v = 0
    while n % p == 0 and n != 0:
        n //= p; v += 1
    return v

def order_mod_p(p):
    # order of alpha mod p (inert/split both: work in R/p)
    cur = (1, 0); a = (3 % p, 2 % p)
    for n in range(1, 4*p+10):
        cur = mul(cur, a, p)
        if cur == (1, 0): return n
    return None

def k_inert(p, L0, P):
    # gamma = alpha^L0 mod P; k = min(vp(a), vp(b)) of gamma-1 (inert case)
    g = pw(ALPHA, L0, P)
    d = ((g[0]-1) % P, g[1] % P)
    # lift to integers 0..P-1; valuation = min vp of representatives
    # (valid since (p) inert: (p)^n = p^n * R)
    return min(vp_int(d[0], p), vp_int(d[1], p)), g

# ---- 0. k / L0 checks ----
for p, P in [(3, 81), (13, 13**4)]:
    L0 = order_mod_p(p)
    k, g = k_inert(p, L0, P)
    print(f"p={p}: L0={L0}, k={k}, gamma-1={((g[0]-1) % P, g[1] % P)}")

# ---- 1. Lemma 5 check ----
def lemma5_check(p, m, P, s, L0):
    # gamma = alpha^L0 mod P, u = (gamma-1)/p^k in R/p^(f-k)... use R/P with
    # division exact: gamma-1 = p^k * u as integers mod P (k from check above)
    k, g = k_inert(p, L0, P)
    # u mod P/p^k: represent u as pair with gamma-1 = p^k * u (mod P)
    # Since gamma-1 coefficients divisible by p^k as integers mod P, divide.
    u = (((g[0]-1) % P)//(p**k), ((g[1]) % P)//(p**k))
    # Note: (g[0]-1)%P divisible by p^k as integer? gamma-1 = p^k*u in R,
    # coefficients of gamma-1 mod P are p^k * (u coeffs mod p^(f-k)); the
    # representatives may wrap mod P, so instead compute u in R directly:
    # recompute gamma over integers? alpha^L0 is huge; instead work mod P*p^k
    # and divide. Simpler: compute gamma mod P*p^k then divide coefficients.
    Pbig = P * (p**k)
    gb = pw(ALPHA, L0, Pbig)
    ub = (((gb[0]-1) % Pbig)//(p**k), (gb[1] % Pbig)//(p**k))
    # u mod p^(f-k) = ub mod (P // p^k)
    umod = P // (p**k)
    u = (ub[0] % umod, ub[1] % umod)
    # F(C) for all C mod P
    gps = [pw(g, j, P) for j in range(p**s)]
    viol = 0; shapes = Counter(); total = 0
    examples = []
    for a in range(P):
        for b in range(P):
            C = (a, b)
            F = Counter(tr(mul(C, gj, P), P) for gj in gps)
            T1 = tr(mul(C, u, P), P)  # careful: u mod p^(f-k); lift to mod P
            # recompute T1 with u lifted: u coeffs mod umod; Tr(Cu) mod P needs
            # u mod P; ub gives u mod Pbig/p^k... use ub directly mod P:
            Cu = mul(C, (ub[0] % P, ub[1] % P), P)
            T1 = tr(Cu, P)
            v = vp_int(T1, p) if T1 != 0 else 99
            # Lemma 5 prediction: if v >= s: singleton; else coset step p^(k+v),
            # size p^(s-v), each value p^v times.
            if v >= s:
                pred_ok = (len(F) == 1)
            else:
                step = p**(k+v); size = p**(s-v)
                vals = set(F.keys())
                pred_ok = (len(vals) == size and all(c == p**v for c in F.values())
                           and all((x - tr(C, P)) % step == 0 for x in vals))
            total += 1
            if not pred_ok:
                viol += 1
                if len(examples) < 3:
                    examples.append((C, v, dict(F)))
            # shape signature: (v capped, sorted multiplicities)
            shapes[(min(v, s), tuple(sorted(Counter(F.values()).items())))] += 1
    print(f"Lemma5 check p={p} m={m} P={P} k={k} s={s}: total={total} violations={viol}")
    for e in examples:
        print("  example C,v,F:", e)
    print("  shapes (v, mult-pattern -> count):")
    for key, cnt in sorted(shapes.items(), key=lambda kv: str(kv[0])):
        print(f"    v={key[0]} mults={key[1]} count={cnt}")
    return viol

print("--- Lemma 5 at (36,3) mod 27 ---")
lemma5_check(3, 36, 27, 2, 4)
print("--- Lemma 5 at (108,3) mod 81 ---")
lemma5_check(3, 108, 81, 3, 4)

# ---- 2. Full G1' check at (108,3) mod 81 ----
def full_G1_check(p, m, P, t):
    # verify alpha^m == 1 mod P
    am = pw(ALPHA, m, P)
    print(f"full check: alpha^{m} mod {P} = {am} (need (1,0))")
    assert am == (1, 0)
    groups = {}
    for a in range(P):
        for b in range(P):
            A = (a, b)
            cur = A; ys = []
            for i in range(m):
                ys.append(tr(cur, P))
                cur = mul(cur, ALPHA, P)
            glob = tuple(sorted(ys))
            per = tuple(tuple(sorted(ys[i] for i in range(m) if i % t == r)) for r in range(t))
            groups.setdefault(glob, []).append(per)
    # D_t relatedness: perms r -> eps*r + bb mod t
    perms = [tuple((eps*r + bb) % t for r in range(t)) for eps in (1, -1) for bb in range(t)]
    bad = 0; ngroups = len(groups); maxsize = 0
    for glob, pers in groups.items():
        maxsize = max(maxsize, len(pers))
        base = pers[0]
        for per in pers[1:]:
            ok = any(tuple(base[sg[r]] for r in range(t)) == per for sg in perms)
            if not ok:
                bad += 1
                if bad <= 3: print("  BAD pair:", base, per)
    print(f"full G1' (m={m},p={p},P={P},t={t}): A-values={P*P} groups={ngroups} maxgroup={maxsize} bad={bad}")
    return bad

print("--- Full G1' at (108,3) mod 81 ---")
full_G1_check(3, 108, 81, 4)
