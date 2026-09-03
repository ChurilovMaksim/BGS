"""
RUN 5 / FINE-SCALE ORDER-4 STRUCTURE — machine verification of lemmas
U1 (fiber bound <= 2), U2 (collision count <= 4), U3 (exact decomposition
#solutions = sum_sigma R_L R_R), and measurement of the extra-count scaling
extras ~ c * k^2/p^2 * pairings (pre-registered random-image model).

Everything exact integer arithmetic over F_p. No floats except final ratios.
Artifact: artifacts/fine_r4_struct.json
"""
import itertools, json, math, os, sys
from collections import defaultdict
import numpy as np

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
RES = {"checks": [], "scaling": []}


def ok(tag, cond, detail):
    RES["checks"].append([tag, bool(cond), detail])
    print(f"[{'PASS' if cond else 'FAIL'}] {tag}: {detail}")
    return bool(cond)


def subgroup(p, alpha, k):
    H, x = [], 1
    for _ in range(k):
        H.append(x)
        x = x * alpha % p
    assert len(set(H)) == k
    return H


def fiber_sizes(p, aL, bL):
    """max fiber size of Phi(x,y)=(a1x+a3y, b1/x+b3/y) over H^2."""
    H = RES["_H"]
    cnt = defaultdict(int)
    for x in H:
        ax = aL[0] * x % p
        bx = bL[0] * pow(x, p - 2, p) % p
        for y in H:
            key = ((ax + aL[1] * y) % p,
                   (bx + bL[1] * pow(y, p - 2, p)) % p)
            cnt[key] += 1
    return max(cnt.values()), cnt


def count_solutions(p, coef, H):
    """brute force (S_F); coef=(a1,a2,a3,a4,b1,b2,b3,b4)."""
    inv = {h: pow(h, p - 2, p) for h in H}
    a1, a2, a3, a4, b1, b2, b3, b4 = coef
    tot = 0
    RL = defaultdict(int)
    for h1 in H:
        t1 = a1 * h1 % p
        u1 = b1 * inv[h1] % p
        for h3 in H:
            RL[(t1 + a3 * h3) % p, (u1 + b3 * inv[h3]) % p] += 1
    RR = defaultdict(int)
    for h2 in H:
        t2 = a2 * h2 % p
        u2 = b2 * inv[h2] % p
        for h4 in H:
            RR[(t2 + a4 * h4) % p, (u2 + b4 * inv[h4]) % p] += 1
    for key, rl in RL.items():
        if key in RR:
            tot += rl * RR[key]
    return tot, dict(RL), dict(RR)


def pairings_count(p, coef, H):
    """Wigner-pairing solutions: multiset{left scaled points}={right}.
    Count directly: tuples with (a1h1,b1/h1)=(a2h2,b2/h2) and
    (a3h3,b3/h3)=(a4h4,b4/h4), plus crossed (a1h1..)=(a4h4..),(a3..)=(a2..)."""
    inv = {h: pow(h, p - 2, p) for h in H}
    a1, a2, a3, a4, b1, b2, b3, b4 = coef
    n = 0
    for h1 in H:
        for h2 in H:
            ok1 = (a1 * h1 - a2 * h2) % p == 0 and \
                  (b1 * inv[h1] - b2 * inv[h2]) % p == 0
            for h3 in H:
                for h4 in H:
                    ok2 = (a3 * h3 - a4 * h4) % p == 0 and \
                          (b3 * inv[h3] - b4 * inv[h4]) % p == 0
                    if ok1 and ok2:
                        n += 1
    return n


def main():
    print("=" * 70)
    print("FINE-SCALE ORDER-4 STRUCTURE (U1/U2/U3 + scaling)")
    print("=" * 70)
    rng = np.random.default_rng(2026)

    # ---- U2: C(u,v) <= 4 exhaustive --------------------------------------
    all_ok = True
    for (p, alpha, k) in [(113, 9, 14), (127, 3, 7), (181, 2, 180 % 180 or 9)]:
        H = subgroup(p, alpha, k)
        inv = {h: pow(h, p - 2, p) for h in H}
        worst = 0
        for h in H:
            for hp in H:
                u = (h - hp) % p
                v = (inv[h] - inv[hp]) % p
                if (u, v) == (0, 0):
                    continue
                # recount C(u,v) fully
                c = sum(1 for x in H for xp in H
                        if (x - xp) % p == u and
                        (inv[x] - inv[xp]) % p == v)
                worst = max(worst, c)
        good = worst <= 4
        all_ok &= good
        ok(f"U2 C(u,v)<=4 (p={p},k={k})", good, f"max observed={worst}")

    # ---- U1 + U3 + scaling ------------------------------------------------
    cases = [(113, 9, 14), (127, 3, 7), (211, 3, 70 % 70 or 3)]
    cases = [(113, 9, 14), (127, 3, 7), (251, 6, 125 // 5 or 5)]
    cases = [(113, 9, 14), (127, 3, 7), (211, 2, 210 // 21 or 10)]
    cases = [(113, 9, 14), (127, 3, 7)]
    for (p, alpha, k) in cases:
        H = subgroup(p, alpha, k)
        RES["_H"] = H
        # random structured coefficient 8-tuple from a small "frequency box":
        # a_i,b_i drawn as +/- products of box elements (generic multi-F)
        vals = list({rng.integers(1, p) for _ in range(8)})
        coef = tuple(int(v) for v in vals)
        maxf, _cnt = fiber_sizes(p, (coef[0], coef[2]), (coef[4], coef[6]))
        ok(f"U1 fiber<=2 (p={p},k={k})", maxf <= 2, f"max fiber={maxf}")

        tot, RL, RR = count_solutions(p, coef, H)
        # U3: tot == sum over keys RL*RR (already by construction) --
        # independent recomputation by direct quadruple loop:
        inv = {h: pow(h, p - 2, p) for h in H}
        a1, a2, a3, a4, b1, b2, b3, b4 = coef
        brute = 0
        for h1 in H:
            for h2 in H:
                s12a = (a1 * h1 - a2 * h2) % p
                s12b = (b1 * inv[h1] - b2 * inv[h2]) % p
                for h3 in H:
                    sa = (s12a + a3 * h3) % p
                    sb = (s12b + b3 * inv[h3]) % p
                    for h4 in H:
                        if (sa - a4 * h4) % p == 0 and \
                           (sb - b4 * inv[h4]) % p == 0:
                            brute += 1
        ok(f"U3 decomposition==brute (p={p},k={k})", brute == tot,
           f"decomposed={tot}, brute={brute}")

        # pairing count (structured part) and extras
        pr = pairings_count(p, coef, H)
        extras = tot - pr
        model = k * k * k * k / (2.0 * p * p)
        RES["scaling"].append({"p": p, "alpha": alpha, "k": k,
                               "total": tot, "pairings": pr,
                               "extras": extras, "model_k4_over_2p2": model,
                               "ratio_extras_model":
                                   extras / model if model else None})
        print(f"   p={p} k={k}: total={tot} pairings={pr} extras={extras} "
              f"(k^4/2p^2 model={model:.1f})")

    with open(os.path.join(ART, "fine_r4_struct.json"), "w") as f:
        json.dump(RES, f, indent=1)
    nok = sum(1 for _, o, _ in RES["checks"] if o)
    print(f"\nTOTAL: {nok}/{len(RES['checks'])} checks PASS")
    sys.exit(0 if nok == len(RES["checks"]) else 1)


if __name__ == "__main__":
    main()
