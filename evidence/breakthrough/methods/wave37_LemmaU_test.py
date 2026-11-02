"""Wave 37, task 3: exact test of Lemma U.

Lemma U (wave 36, sec 4): the pair multiset
  P = T_pair(C^a, C^b) U T_pair(alpha^u C^a, alpha^u C^b)
determines the unordered block pair
  {T_pair(C^a, C^b), T_pair(alpha^u C^a, alpha^u C^b)}.

Setup: m = 2u, u odd, q = p^{2f} constraining (q | Tr(alpha^u)+2).
Kernel vectors at q are exactly y_i = p^f * Tr(C alpha^i mod p^f),
C in R/p^f R (R = Z[sqrt(2)]), because v_p(alpha^u + 1) = f and
alpha^u - 1 is a p-adic unit (p odd), so ker(alpha^m - 1) = p^f R/qR.
Working with reduced traces t_i = Tr(C alpha^i mod p^f) is equivalent
(all kernel values are divisible by p^f, blocks preserved).

Blocks: block0 = {(Tr(C^a beta^k), Tr(C^b beta^k)) : k in Z/u},
block1 = same with (alpha^u C^a, alpha^u C^b), beta = alpha^2.
P = block0 U block1 as a multiset (sorted concatenation).

Test: enumerate all (C^a, C^b), group by P, and report any P-group
containing two distinct unordered block pairs (an exact counterexample
to Lemma U). Also records, for conflicts, whether pairs are distinct
and whether block0 == block1.
"""

import sys


def rmul(x, y, mod):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % mod, (a * d + b * c) % mod)


def rpow(x, n, mod):
    r = (1 % mod, 0)
    while n:
        if n & 1:
            r = rmul(r, x, mod)
        x = rmul(x, x, mod)
        n >>= 1
    return r


def tr(x, mod):
    return (2 * x[0]) % mod


def build_component(p, f, m):
    mod = p ** f
    u = m // 2
    alpha = (3 % mod, 2 % mod)
    am = rpow(alpha, m, mod)
    assert am == (1 % mod, 0), ("alpha^m != 1", p, f, am)
    beta = rmul(alpha, alpha, mod)
    bpow = [(1 % mod, 0)]
    for _ in range(1, u):
        bpow.append(rmul(bpow[-1], beta, mod))
    assert rmul(bpow[-1], beta, mod) == (1 % mod, 0), "beta^u != 1"
    au = rpow(alpha, u, mod)
    Cs = [(a, b) for a in range(mod) for b in range(mod)]
    seqs = []
    for C in Cs:
        seqs.append(tuple(tr(rmul(C, bpow[k], mod), mod) for k in range(u)))
    idx = {C: i for i, C in enumerate(Cs)}
    tau = [idx[rmul(au, C, mod)] for C in Cs]
    # (Tr C, Tr alpha C) must determine C (p odd)
    sigs = set()
    for C in Cs:
        sigs.add((tr(C, mod), tr(rmul(alpha, C, mod), mod)))
    assert len(sigs) == len(Cs), "trace signature not injective"
    return mod, Cs, seqs, tau


def test(m, pa, fa, pb, fb, max_conflicts=5):
    moda, Csa, seqs_a, tau_a = build_component(pa, fa, m)
    modb, Csb, seqs_b, tau_b = build_component(pb, fb, m)
    u = m // 2
    B = moda * modb
    groups = {}  # P-key -> (blockpair, first point, count)
    conflicts = []
    npts = 0
    for ia, sa in enumerate(seqs_a):
        sa_t = seqs_a[tau_a[ia]]
        for ib, sb in enumerate(seqs_b):
            sb_t = seqs_b[tau_b[ib]]
            b0 = tuple(sorted(zip(sa, sb)))
            b1 = tuple(sorted(zip(sa_t, sb_t)))
            allp = sorted(b0 + b1)
            key = 0
            for (x, y) in allp:
                key = key * B + (x * modb + y)
            e0 = 0
            for (x, y) in b0:
                e0 = e0 * B + (x * modb + y)
            e1 = 0
            for (x, y) in b1:
                e1 = e1 * B + (x * modb + y)
            bp = (e0, e1) if e0 <= e1 else (e1, e0)
            npts += 1
            prev = groups.get(key)
            if prev is None:
                groups[key] = (bp, (ia, ib), 1)
            else:
                pbp, pfirst, cnt = prev
                groups[key] = (pbp, pfirst, cnt + 1)
                if pbp != bp and len(conflicts) < max_conflicts:
                    distinct = len(set(allp)) == len(allp)
                    conflicts.append({
                        "P": allp,
                        "first_point": (Csa[pfirst[0]], Csb[pfirst[1]]),
                        "first_blockpair": pbp,
                        "second_point": (Csa[ia], Csb[ib]),
                        "second_blockpair": bp,
                        "pairs_distinct": distinct,
                        "blocks_equal_first": pbp[0] == pbp[1],
                    })
            if npts % 200000 == 0:
                print(f"  ... {npts} points, {len(groups)} P-groups, "
                      f"{len(conflicts)} conflicts", flush=True)
    print(f"m={m} components=({pa}^{2*fa},{pb}^{2*fb}) points={npts} "
          f"P-groups={len(groups)} conflicts={len(conflicts)}", flush=True)
    for c in conflicts:
        print("CONFLICT:", c, flush=True)
    return conflicts


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "m30"):
        print("=== m=30, (625, 841) ===", flush=True)
        test(30, 5, 2, 29, 1)
    if which in ("all", "m18"):
        print("=== m=18, (25, 38809) ===", flush=True)
        test(18, 5, 1, 197, 1)
    if which in ("all", "m30b"):
        print("=== m=30, (625, 72361) ===", flush=True)
        test(30, 5, 2, 269, 1)
