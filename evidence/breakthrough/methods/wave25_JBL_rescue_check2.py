"""Wave 25, task 3 (round 2): test rescued rigidity = D-orbit + Ann.

Round 1 showed every signature group escapes a bare D-orbit (up to
trace kernel). The miss is additive: A and A+z can share a signature
when z is trace-invisible, i.e. Tr(z*alpha^n) = 0 for all n in Z/m
(the vector entries are exactly those traces). Kernel twists are
absorbed by Ann: Tr((kappa-1)*w*alpha^n) = 0 by the kernel property.

Test: signature(A') = signature(A) ==> A' - c(A)*alpha^j in Ann
for some j, c in {id, conj}, componentwise mod (q2, q).
Ann_m(M) is computed exactly by brute force over (x, y) mod M.

Cases: m=12 (q2=128, q=81) and m=8 (q2=512, q=9).
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
    """z mod M with Tr(z*alpha^n) = 0 mod M for n = 0..m-1."""
    pows = [pw(ALPHA, n, M) for n in range(m)]
    out = set()
    for x in range(M):
        for y in range(M):
            if all(tr(mul((x, y), p, M), M) == 0 for p in pows):
                out.add((x, y))
    return out


def run(m, q2, q):
    t = math.gcd(m, 4)
    S = m // t
    alphas2 = [pw(ALPHA, r, q2) for r in range(t)]
    alphasq = [pw(ALPHA, r, q) for r in range(t)]
    betas2 = [pw(pw(ALPHA, t, q2), s, q2) for s in range(S)]
    betasq = [pw(pw(ALPHA, t, q), s, q) for s in range(S)]
    G2, Gq = genuine(q2, m), genuine(q, m)
    A2, Aq = ann_m(q2, m), ann_m(q, m)
    print(f"m={m}: |G2|={len(G2)} |Gq|={len(Gq)} "
          f"|Ann({q2})|={len(A2)} |Ann({q})|={len(Aq)}", flush=True)

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
    print(f"m={m}: groups={len(groups)}", flush=True)

    # Powers of alpha up to a full period for both moduli.
    def order(a, M):
        cur = (1, 0)
        for j in range(1, 100000):
            cur = mul(cur, a, M)
            if cur == (1, 0):
                return j
        raise RuntimeError("order")
    L = order(ALPHA, q2) * order(ALPHA, q) // math.gcd(
        order(ALPHA, q2), order(ALPHA, q))
    pow2 = [(1, 0)]
    for _ in range(L):
        pow2.append(mul(pow2[-1], ALPHA, q2))
    powq = [(1, 0)]
    for _ in range(L):
        powq.append(mul(powq[-1], ALPHA, q))

    bad = []
    for sig, members in groups.items():
        A0 = members[0]
        ok_set = set()
        for j in range(L):
            for c in (0, 1):
                b2 = mul(conj(A0[0], q2) if c else A0[0], pow2[j], q2)
                bq = mul(conj(A0[1], q) if c else A0[1], powq[j], q)
                for z2 in A2:
                    for zq in Aq:
                        ok_set.add((((b2[0] + z2[0]) % q2,
                                      (b2[1] + z2[1]) % q2),
                                     ((bq[0] + zq[0]) % q,
                                      (bq[1] + zq[1]) % q)))
        outside = [A for A in members if A not in ok_set]
        if outside:
            bad.append((A0, outside[:3], len(outside), len(members)))
    print(f"m={m}: groups escaping D-orbit + Ann: {len(bad)}", flush=True)
    for A0, outs, n_out, n_mem in bad[:5]:
        print(f"  rep {A0}, {n_out}/{n_mem} outside, e.g. {outs}", flush=True)
        for o in outs[:2]:
            d2 = ((o[0][0] - A0[0][0]) % q2, (o[0][1] - A0[0][1]) % q2)
            dq = ((o[1][0] - A0[1][0]) % q, (o[1][1] - A0[1][1]) % q)
            print(f"    diff vs rep: mod {q2} {d2}, mod {q} {dq}", flush=True)
    return bad


bad12 = run(12, 128, 81)
bad8 = run(8, 512, 9)
print("RESULT m=12 bad:", len(bad12))
print("RESULT m=8 bad:", len(bad8))
