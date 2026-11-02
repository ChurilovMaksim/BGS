"""Wave 33, task 1: is the m=60 COH counterexample pair D-related?

Exact integer arithmetic. Conventions follow wave32_COH_m60_verify.py:
parameters (a,b) = a + b*sqrt(2) mod q, alpha = (3,2),
trace window S(A)_i = Tr(A*alpha^i) = 2*Re(A*alpha^i) mod q, i in Z/60.
sigma(i) = 11*i+9 mod 60, with S'_i = S_{sigma(i)} (as verified in wave 32).

Checks:
 (A) genuineness of every component pair;
 (B) global pair (A, A') mod D_60 via CRT, and S' = sigma(S) globally;
 (C) JBL's actual conclusion (wave 20): a single pi in D_4 with
     J'^(q)_r = J^(q)_{pi(r)} for all r and all odd q, where
     J^(q)_r = multiset of (y_i mod 128, y_i mod q) for i = r mod 4;
 (D) D-relatedness in the R** sense: A' = c(A)*alpha^j + z + w (mod D_60),
     z in Ann(128) (computed exactly), w in Shadow(81) x Shadow(625),
     one (j, c) across all components; also the bare-orbit version.
"""
from math import gcd
from collections import Counter

M = 60
ALPHA = (3, 2)
SIGMA = [(11 * i + 9) % 60 for i in range(60)]

PAIRS = {
    128: ((0, 8), (32, 8)),
    81: ((9, 18), (72, 63)),
    625: ((0, 0), (0, 0)),
    49: ((0, 7), (0, 42)),
    121: ((11, 77), (110, 44)),
    841: ((29, 435), (29, 406)),
    1681: ((41, 861), (41, 820)),
    361: ((0, 0), (0, 0)),
    923521: ((0, 0), (0, 0)),
    3481: ((0, 0), (0, 0)),
    72361: ((0, 0), (0, 0)),
    361201: ((0, 0), (0, 0)),
    5202961: ((0, 0), (0, 0)),
}
PE = {81: 9, 625: 25, 49: 7, 121: 11, 361: 19, 841: 29,
      923521: 961, 1681: 41, 3481: 59, 72361: 269, 361201: 601,
      5202961: 2281}


def mul(a, b, q):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % q,
            (a[0] * b[1] + a[1] * b[0]) % q)


def conj(a):
    return (a[0], -a[1])


def tr_seq(A, q):
    out = []
    cur = A
    for _ in range(60):
        out.append((2 * cur[0]) % q)
        cur = mul(cur, ALPHA, q)
    return tuple(out)


def genuine(A, q):
    if q == 128:
        return A[0] % 16 == 0 and A[1] % 8 == 0
    return A[0] % PE[q] == 0 and A[1] % PE[q] == 0


def crt_pair(residues):
    """residues: list of (value, modulus) with coprime moduli. Returns (x, M)."""
    x, Mprod = 0, 1
    for v, m in residues:
        # solve x + Mprod*t = v (mod m)
        g = gcd(Mprod, m)
        assert (v - x) % g == 0
        p, q_ = Mprod // g, m // g
        inv = pow(p, -1, q_)
        t = ((v - x) // g * inv) % q_
        x = x + Mprod * t
        Mprod *= q_
        x %= Mprod
    return x, Mprod


def crt_param(pairs_by_q):
    """pairs_by_q: dict q -> (a,b). Returns (A, D) with A in R/DR."""
    ax, D = crt_pair([(pairs_by_q[q][0], q) for q in sorted(pairs_by_q)])
    bx, D2 = crt_pair([(pairs_by_q[q][1], q) for q in sorted(pairs_by_q)])
    assert D == D2
    return (ax, bx), D


def alpha_order(q):
    cur = (1, 0)
    for j in range(1, 10_000_000):
        cur = mul(cur, ALPHA, q)
        if cur == (1, 0):
            return j
    raise RuntimeError(f"order of alpha mod {q} exceeds cap")


def ann_128():
    """Ann_60(128) = {z mod 128 : Tr(z alpha^n) = 0 mod 128 for all n in Z/60}."""
    out = set()
    for x in range(128):
        for y in range(128):
            ok = True
            cur = (x, y)
            for _ in range(60):
                if (2 * cur[0]) % 128 != 0:
                    ok = False
                    break
                cur = mul(cur, ALPHA, 128)
            if ok:
                out.add((x, y))
    return out


def in_shadow(diff, q):
    if q == 81:
        return diff[0] % 27 == 0 and diff[1] % 27 == 0
    if q == 625:
        return diff[0] % 125 == 0 and diff[1] % 125 == 0
    return diff == (0, 0)


# ---- (A) genuineness ------------------------------------------------------
for q, (A, Ap) in sorted(PAIRS.items()):
    assert genuine(A, q), (q, "A not genuine", A)
    assert genuine(Ap, q), (q, "Ap not genuine", Ap)
print("(A) all 13 component pairs genuine: OK")

# ---- (B) global pair + sigma ----------------------------------------------
Aglob, D = crt_param({q: A for q, (A, _) in PAIRS.items()})
Apglob, D2 = crt_param({q: Ap for q, (_, Ap) in PAIRS.items()})
assert D == D2
print(f"(B) D_60 = {D}")
print(f"    global A  = {Aglob}")
print(f"    global A' = {Apglob}")
S = tr_seq(Aglob, D)
Sp = tr_seq(Apglob, D)
assert all(Sp[i] == S[SIGMA[i]] for i in range(60)), "sigma mismatch globally"
assert sorted(Sp) == sorted(S), "sorted global multisets differ"
print("(B) global windows satisfy S'_i = S_{sigma(i)}; sorted multisets equal: OK")

# ---- (C) JBL class-level conclusion ----------------------------------------
# J^(q)_r = multiset of (y_i mod 128, y_i mod q) for i = r mod 4.
DIH4 = [(eps, c) for eps in (1, -1) for c in range(4)]


def class_joint(A, q):
    win = tr_seq(A, D)
    out = {}
    for r in range(4):
        out[r] = Counter((win[i] % 128, win[i] % q)
                         for i in range(60) if i % 4 == r)
    return out


print("(C) JBL class-level conclusion, pi in D_4 (r -> eps*r + c):")
global_pi = []
for eps, c in DIH4:
    ok_all = True
    per_q = {}
    for q in sorted(PAIRS):
        if q == 128:
            continue
        J = class_joint(Aglob, q)
        Jp = class_joint(Apglob, q)
        ok_q = all(Jp[r] == J[(eps * r + c) % 4] for r in range(4))
        per_q[q] = ok_q
        ok_all = ok_all and ok_q
    print(f"    pi(r) = {eps}*r + {c} mod 4: {'HOLDS at all odd q' if ok_all else 'fails'}")
    if ok_all:
        global_pi.append((eps, c))
print(f"    global pi working at every odd q: {global_pi}")

# ---- (D) D-relatedness, R** sense -------------------------------------------
ANN = ann_128()
print(f"(D) Ann_60(128) computed exactly: {len(ANN)} elements: {sorted(ANN)}")


def component_residues(Aq, Apq, q, cfun, bare):
    """Set of j mod ord_q with Apq - cfun(Aq)*alpha^j in E_q."""
    if bare:
        def ok(diff):
            return diff == (0, 0)
    elif q == 128:
        def ok(diff):
            return diff in ANN
    elif q in (81, 625):
        def ok(diff):
            return in_shadow(diff, q)
    else:
        def ok(diff):
            return diff == (0, 0)
    ordq = alpha_order(q)
    base = cfun(Aq)
    cur = base
    res = set()
    for j in range(ordq):
        diff = ((Apq[0] - cur[0]) % q, (Apq[1] - cur[1]) % q)
        if ok(diff):
            res.add(j)
        cur = mul(cur, ALPHA, q)
    return res, ordq


def crt_merge(sets_with_mod):
    """sets_with_mod: list of (set of residues, modulus). Returns a residue
    mod lcm satisfying all, or None."""
    S, L = {0}, 1
    # start from first set directly
    first_set, first_mod = sets_with_mod[0]
    S, L = set(first_set), first_mod
    for T, mod in sets_with_mod[1:]:
        g = gcd(L, mod)
        newS = set()
        lcm = L // g * mod
        for r in S:
            for s in T:
                if (r - s) % g == 0:
                    # solve x = r (mod L), x = s (mod mod)
                    p, q_ = L // g, mod // g
                    inv = pow(p, -1, q_)
                    t = ((s - r) // g * inv) % q_
                    newS.add((r + L * t) % lcm)
        S, L = newS, lcm
        if not S:
            return None, L
    return (min(S) if S else None), L


for bare in (False, True):
    label = "bare dihedral orbit (no Ann/Shadow)" if bare else \
        "R** (orbit + Ann + Shadow)"
    for cname, cfun in (("id", lambda a: a), ("conj", conj)):
        per_q = {}
        impossible = None
        for q in sorted(PAIRS):
            Aq, Apq = PAIRS[q]
            res, ordq = component_residues(Aq, Apq, q, cfun, bare)
            per_q[q] = (len(res), ordq, sorted(res)[:6])
            if not res:
                impossible = q
                break
        if impossible is not None:
            print(f"(D) {label}, c={cname}: IMPOSSIBLE already at q={impossible} "
                  f"(no j works there)")
            continue
        merged, L = crt_merge([(component_residues(PAIRS[q][0], PAIRS[q][1],
                                                    q, cfun, bare)[0],
                                component_residues(PAIRS[q][0], PAIRS[q][1],
                                                    q, cfun, bare)[1])
                               for q in sorted(PAIRS)])
        if merged is None:
            print(f"(D) {label}, c={cname}: per-component j exist but "
                  f"NO common j (CRT merge empty)")
        else:
            print(f"(D) {label}, c={cname}: COMMON j EXISTS, e.g. j = {merged} "
                  f"(mod {L})")
        print(f"     per-component (#residues / ord_q): " +
              ", ".join(f"{q}:{n}/{o}" for q, (n, o, _) in per_q.items()))
print("DONE")
