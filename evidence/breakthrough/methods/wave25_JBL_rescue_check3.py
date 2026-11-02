"""Wave 25, task 3 (round 3): test rescued rigidity = D-orbit + Ann + Shadow.

Round 2: m=8 passes with D-orbit + Ann; m=12 fails on 32/200 groups,
with escaping diffs (0,27), (0,54) mod 81 -- a mod-3 collapse shadow:
shifts of A by 27*D (D in R/3R) mod 81, 0 mod 128, preserve signatures
because the odd data sees A_1 = A/9 only mod 3 in the collapse regime.

Test at m=12: every signature group is contained in
  { c(A0)*alpha^j + z + w : j, c in {id, conj}, z in Ann, w in Shadow },
Shadow = {(27a, 27b) mod 81 : a, b in Z/3} x {(0,0) mod 128}.
Lookup is via the mod-81 orbit table (j mod 108) to stay fast.
Also re-check m=8 with Shadow = {(3a, 3b) mod 9} x {0 mod 512}
(the analogous one-digit shadow at q=9) to confirm it is trivial there
in the sense that it adds nothing beyond orbit+Ann.
Repository untouched; no Lean build.
"""

import math
from collections import defaultdict

ALPHA = (3, 2)


def mul(a, b, M):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % M,
            (a[0] * b[1] + a[1] * b[0]) % M)


def conj(a, M):
    return (a[0] % M, (-a[1]) % M)


def pw(a, n, M):
    r = (1, 0)
    for _ in range(n):
        r = mul(r, a, M)
    return r


def tr(a, M):
    return (2 * a[0]) % M


def genuine(M, m):
    d = pw(ALPHA, m, M)
    d = ((d[0] - 1) % M, d[1])
    return [(x, y) for x in range(M) for y in range(M)
            if mul(d, (x, y), M) == (0, 0)]


def ann_m(M, m):
    pows = [pw(ALPHA, n, M) for n in range(m)]
    return {(x, y) for x in range(M) for y in range(M)
            if all(tr(mul((x, y), p, M), M) == 0 for p in pows)}


def order(a, M):
    cur = (1, 0)
    for j in range(1, 100000):
        cur = mul(cur, a, M)
        if cur == (1, 0):
            return j
    raise RuntimeError("order")


def run(m, q2, q, shadow_q):
    t = math.gcd(m, 4)
    S = m // t
    alphas2 = [pw(ALPHA, r, q2) for r in range(t)]
    alphasq = [pw(ALPHA, r, q) for r in range(t)]
    betas2 = [pw(pw(ALPHA, t, q2), s, q2) for s in range(S)]
    betasq = [pw(pw(ALPHA, t, q), s, q) for s in range(S)]
    G2, Gq = genuine(q2, m), genuine(q, m)
    A2, Aq = ann_m(q2, m), ann_m(q, m)

    def signature(A2v, Aqv):
        sig = []
        for r in range(t):
            pairs = []
            for s in range(S):
                c2 = mul(mul(A2v, alphas2[r], q2), betas2[s], q2)
                cq = mul(mul(Aqv, alphasq[r], q), betasq[s], q)
                pairs.append((tr(c2, q2), tr(cq, q)))
            sig.append(tuple(sorted(pairs)))
        return tuple(sig)

    groups = defaultdict(list)
    for a2 in G2:
        for aq in Gq:
            groups[signature(a2, aq)].append((a2, aq))
    o2, oq = order(ALPHA, q2), order(ALPHA, q)
    L = o2 * oq // math.gcd(o2, oq)
    pow2 = [(1, 0)]
    for _ in range(L):
        pow2.append(mul(pow2[-1], ALPHA, q2))
    # Orbit tables mod q: value -> list of j mod oq giving it, per c.
    bad = []
    for sig, members in groups.items():
        A0 = members[0]
        tables = []
        for c in (0, 1):
            tab = defaultdict(list)
            base = conj(A0[1], q) if c else A0[1]
            cur = base
            for j in range(oq):
                tab[cur].append(j)
                cur = mul(cur, ALPHA, q)
            tables.append(tab)
        for A in members:
            ok = False
            for c in (0, 1):
                base2 = conj(A0[0], q2) if c else A0[0]
                for w in shadow_q:
                    # Need c(A0)*alpha^j == A_q - w (mod q) for some j.
                    target = ((A[1][0] - w[0]) % q, (A[1][1] - w[1]) % q)
                    for j0 in tables[c].get(target, []):
                        # Lift j0 mod oq to j mod L.
                        step = oq
                        j = j0
                        while j < L:
                            b2 = mul(base2, pow2[j], q2)
                            d2 = ((A[0][0] - b2[0]) % q2,
                                  (A[0][1] - b2[1]) % q2)
                            if d2 in A2:
                                ok = True
                                break
                            j += step
                        if ok:
                            break
                    if ok:
                        break
                if ok:
                    break
            if not ok:
                bad.append((A0, A))
                break
    print(f"m={m}: groups={len(groups)}, groups escaping "
          f"D-orbit + Ann + Shadow: {len(bad)}", flush=True)
    for A0, A in bad[:5]:
        print(f"  rep {A0} escapes, e.g. member {A}", flush=True)
    return bad


# m=12: shadow shifts by 27*D mod 81, D in R/3R.
shadow12 = {(27 * a % 81, 27 * b % 81) for a in range(3) for b in range(3)}
bad12 = run(12, 128, 81, shadow12)
# m=8: analogous one-digit shadow at q=9 (shifts by 3*D mod 9).
shadow8 = {(3 * a % 9, 3 * b % 9) for a in range(3) for b in range(3)}
bad8 = run(8, 512, 9, shadow8)
print("RESULT m=12 bad:", len(bad12))
print("RESULT m=8 bad:", len(bad8))
