"""Wave 28, task 3: verify lemma R** at ONE new case: m=36, q=243.

Method follows wave25_JBL_rescue_check3.py exactly, adapted:
  t = gcd(36,4) = 4, S = 36/4 = 9, q2 = 128 (v2(D36)=7), q = 243 = 3^5.
  Genuine B mod M: (alpha^36 - 1) B == 0 mod M.
  Signature of a pair (A2, Aq): for each class r, sorted multiset over
  s of (Tr(A2 alpha^r beta^s) mod 128, Tr(Aq alpha^r beta^s) mod 243),
  beta = alpha^4 (same-s pairing, as in check3).
  Coverage: every member A of a signature group satisfies
    A = c(A0) alpha^j + z + w  (mod 128 x mod 243),
  c in {id, conj}, z in Ann (Ann(243) trivial here), w in Shadow.
  Shadow candidates:
    ShadowA = {27D mod 243 : D in R/3R} (9 values) -- direct analogue
      of the m=12 shadow {27D mod 81}; shift of C = B/9 by 3D.
    ShadowBig = {(27a, 27b) mod 243 : a, b in Z/9} (81 values) --
      all multiples of 27, tested only if ShadowA leaves escapes.
Groups are identical-signature groups (pi = id), as in check3;
general pi reduces to pi = id by transport (wave25 note sec.1).
Repository untouched; no Lean build.
"""

import math
from collections import defaultdict

ALPHA = (3, 2)
M_CASE = 36
Q2, Q = 128, 243


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
    delta = ((d[0] - 1) % M, d[1])
    return [(x, y) for x in range(M) for y in range(M)
            if mul(delta, (x, y), M) == (0, 0)]


def ann_m(M, m):
    pows = [pw(ALPHA, n, M) for n in range(m)]
    return {(x, y) for x in range(M) for y in range(M)
            if all(tr(mul((x, y), p, M), M) == 0 for p in pows)}


def order(a, M):
    cur = (1, 0)
    for j in range(1, 1000000):
        cur = mul(cur, a, M)
        if cur == (1, 0):
            return j
    raise RuntimeError("order")


def main():
    m = M_CASE
    t = math.gcd(m, 4)
    S = m // t
    alphas2 = [pw(ALPHA, r, Q2) for r in range(t)]
    alphasq = [pw(ALPHA, r, Q) for r in range(t)]
    betas2 = [pw(pw(ALPHA, t, Q2), s, Q2) for s in range(S)]
    betasq = [pw(pw(ALPHA, t, Q), s, Q) for s in range(S)]
    G2, Gq = genuine(Q2, m), genuine(Q, m)
    A2, Aq = ann_m(Q2, m), ann_m(Q, m)
    print(f"m={m} t={t} S={S}: |G128|={len(G2)} |G243|={len(Gq)} "
          f"|Ann128|={len(A2)} |Ann243|={len(Aq)}", flush=True)
    print(f"beta mod 243 = {pw(ALPHA, t, Q)} (collapse: beta == 1 mod 3: "
          f"{pw(ALPHA, t, Q)[0] % 3 == 1 and pw(ALPHA, t, Q)[1] % 3 == 0})",
          flush=True)

    # Precompute per-element trace tables: tables[A] = tuple over r of
    # tuple over s of traces.
    def tables(G, M, alphas, betas):
        out = {}
        for A in G:
            tab = []
            for r in range(t):
                base = mul(A, alphas[r], M)
                tab.append(tuple(tr(mul(base, betas[s], M), M)
                                 for s in range(S)))
            out[A] = tuple(tab)
        return out

    T2 = tables(G2, Q2, alphas2, betas2)
    Tq = tables(Gq, Q, alphasq, betasq)
    print("tables precomputed", flush=True)

    groups = defaultdict(list)
    for a2 in G2:
        ptab = T2[a2]
        for aq in Gq:
            otab = Tq[aq]
            sig = tuple(tuple(sorted(zip(ptab[r], otab[r])))
                        for r in range(t))
            groups[sig].append((a2, aq))
    sizes = sorted(len(v) for v in groups.values())
    print(f"pairs={len(G2) * len(Gq)} groups={len(groups)} "
          f"group sizes: min={sizes[0]} max={sizes[-1]} "
          f"singletons={sum(1 for s in sizes if s == 1)}", flush=True)

    o2, oq = order(ALPHA, Q2), order(ALPHA, Q)
    L = o2 * oq // math.gcd(o2, oq)
    print(f"ord(alpha): mod128={o2} mod243={oq} joint period L={L}",
          flush=True)
    pow2 = [(1, 0)]
    for _ in range(L):
        pow2.append(mul(pow2[-1], ALPHA, Q2))

    def coverage(shadow_q, label):
        bad = []
        for sig, members in groups.items():
            A0 = members[0]
            tabs = []
            for c in (0, 1):
                tab = defaultdict(list)
                base = conj(A0[1], Q) if c else A0[1]
                cur = base
                for j in range(oq):
                    tab[cur].append(j)
                    cur = mul(cur, ALPHA, Q)
                tabs.append(tab)
            for A in members:
                ok = False
                for c in (0, 1):
                    base2 = conj(A0[0], Q2) if c else A0[0]
                    for w in shadow_q:
                        target = ((A[1][0] - w[0]) % Q,
                                  (A[1][1] - w[1]) % Q)
                        for j0 in tabs[c].get(target, []):
                            j = j0
                            while j < L:
                                b2 = mul(base2, pow2[j], Q2)
                                d2 = ((A[0][0] - b2[0]) % Q2,
                                      (A[0][1] - b2[1]) % Q2)
                                if d2 in A2:
                                    ok = True
                                    break
                                j += oq
                            if ok:
                                break
                        if ok:
                            break
                    if ok:
                        break
                if not ok:
                    bad.append((A0, A))
                    break
        print(f"{label}: groups escaping = {len(bad)} / {len(groups)}",
              flush=True)
        for A0, A in bad[:5]:
            print(f"  rep {A0} escapes, e.g. member {A}", flush=True)
        return bad

    bad0 = coverage({(0, 0)}, "D-orbit + Ann only")
    shadowA = {(27 * a % Q, 27 * b % Q) for a in range(3) for b in range(3)}
    badA = coverage(shadowA, "D-orbit + Ann + ShadowA (27*R/3R)")
    badB = None
    if badA:
        shadowBig = {(27 * a % Q, 27 * b % Q)
                     for a in range(9) for b in range(9)}
        badB = coverage(shadowBig, "D-orbit + Ann + ShadowBig (27*R/9R)")
    print(f"RESULT groups={len(groups)} orbit+Ann escapes={len(bad0)} "
          f"+ShadowA escapes={len(badA)}"
          + (f" +ShadowBig escapes={len(badB)}" if badB is not None
             else " (ShadowBig not needed)"), flush=True)


if __name__ == "__main__":
    main()
