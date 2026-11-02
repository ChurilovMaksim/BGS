"""Wave 25, task 3: test multi-class (global) JBL rigidity exactly.

For genuine global parameters A mod (q2 * q), compute the signature
S(A) = (J_r(A))_{r mod t}, J_r = sorted multiset over s of
(Tr(B_r beta^s) mod q2, Tr(B_r beta^s) mod q), B_r = A alpha^r.
Test: every signature group (with pi = id) is contained in a single
D-orbit of a representative, up to trace-kernel slack mod q2:
A' = kappa * c(A) * alpha^j (mod q2), A' = c(A) * alpha^j (mod q),
same j and c in {id, conj}, kappa in the 8-element trace kernel.
Also verify transport: S(A alpha^j) is the permuted S(A).

Cases: m=12 (q2=128, q=81, t=4, s in Z/3) and m=8 (q2=512, q=9,
t=4, s in Z/2). All arithmetic exact integers in R = Z[sqrt2].
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
    """All (x, y) mod M with (alpha^m - 1) * (x + y*sqrt2) == 0 mod M."""
    d = pw(ALPHA, m, M)
    d = ((d[0] - 1) % M, d[1])
    out = []
    for x in range(M):
        for y in range(M):
            if mul(d, (x, y), M) == (0, 0):
                out.append((x, y))
    return out


def order(a, M):
    cur = (1, 0)
    for j in range(1, 100000):
        cur = mul(cur, a, M)
        if cur == (1, 0):
            return j
    raise RuntimeError("order not found")


def kernel(a):
    """8-element trace kernel mod 2^a: u = 1 mod 2^(a-1), v = 0 mod 2^(a-2)."""
    uvals = [1, 1 + 2 ** (a - 1)]
    vvals = [k * 2 ** (a - 2) for k in range(4)]
    return [(u % 2 ** a, v % 2 ** a) for u in uvals for v in vvals]


def run(m, q2, q, a_exp):
    t = math.gcd(m, 4)
    S = m // t
    beta2 = pw(ALPHA, t, q2)
    betaq = pw(ALPHA, t, q)
    alphas2 = [pw(ALPHA, r, q2) for r in range(t)]
    alphasq = [pw(ALPHA, r, q) for r in range(t)]
    betas2 = [pw(beta2, s, q2) for s in range(S)]
    betasq = [pw(betaq, s, q) for s in range(S)]
    G2 = genuine(q2, m)
    Gq = genuine(q, m)
    print(f"m={m}: genuine mod {q2}: {len(G2)}, mod {q}: {len(Gq)}, "
          f"total pairs: {len(G2) * len(Gq)}", flush=True)

    def signature(A2, Aq):
        sig = []
        for r in range(t):
            pairs = []
            for s in range(S):
                c2 = mul(mul(A2, alphas2[r], q2), betas2[s], q2)
                cq = mul(mul(Aq, alphasq[r], q), betasq[s], q)
                pairs.append((tr(c2, q2), tr(cq, q)))
            sig.append(tuple(sorted(pairs)))
        return tuple(sig)

    groups = defaultdict(list)
    for A2 in G2:
        for Aq in Gq:
            groups[signature(A2, Aq)].append((A2, Aq))
    print(f"m={m}: signature groups: {len(groups)}, "
          f"sizes: min {min(len(v) for v in groups.values())}, "
          f"max {max(len(v) for v in groups.values())}", flush=True)

    # Transport sanity: S(A*alpha) is the permuted S(A) (shift by 1).
    for A2, Aq in list(groups.values())[0][:1]:
        s0 = signature(A2, Aq)
        s1 = signature(mul(A2, ALPHA, q2), mul(Aq, ALPHA, q))
        assert s1 == tuple(s0[(r + 1) % t] for r in range(t)), "transport fails"
    print(f"m={m}: transport check passed", flush=True)

    # D-orbit test per group.
    o2, oq = order(ALPHA, q2), order(ALPHA, q)
    L = o2 * oq // math.gcd(o2, oq)
    K = kernel(a_exp)
    print(f"m={m}: ord alpha mod {q2} = {o2}, mod {q} = {oq}, L = {L}, "
          f"kernel size {len(K)}", flush=True)
    # Precompute alpha powers iteratively (pw() per j would be O(L^2)).
    pow2 = [(1, 0)]
    for _ in range(L):
        pow2.append(mul(pow2[-1], ALPHA, q2))
    powq = [(1, 0)]
    for _ in range(L):
        powq.append(mul(powq[-1], ALPHA, q))
    bad = []
    for sig, members in groups.items():
        A0 = members[0]
        orbit = set()
        for j in range(L):
            aj2, ajq = pow2[j], powq[j]
            for c in (0, 1):
                b2 = mul(conj(A0[0], q2) if c else A0[0], aj2, q2)
                bq = mul(conj(A0[1], q) if c else A0[1], ajq, q)
                for kap in K:
                    orbit.add((mul(kap, b2, q2), bq))
                orbit.add((b2, bq))
        outside = [A for A in members if A not in orbit]
        if outside:
            bad.append((sig, A0, outside[:3], len(outside), len(members)))
    print(f"m={m}: groups NOT contained in one D-orbit (up to kernel): "
          f"{len(bad)}", flush=True)
    for sig, A0, outs, n_out, n_mem in bad[:5]:
        print(f"  rep {A0}, {n_out}/{n_mem} outside, e.g. {outs}", flush=True)
    return bad


bad12 = run(12, 128, 81, 7)
bad8 = run(8, 512, 9, 9)
print("RESULT m=12 bad groups:", len(bad12))
print("RESULT m=8 bad groups:", len(bad8))
