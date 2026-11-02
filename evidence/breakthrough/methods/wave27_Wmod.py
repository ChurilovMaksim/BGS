"""Wave 27, task 5: test the W-mod lemma.

Question: on the 152 failing (fiber,w)-classes at m=12 (orbits sharing
sorted(w) inside a split fiber, pw_ok=False), is w' a component-wise
dihedral image of w mod q for every prime power q || D?

If yes, the mod-D lemma (wave 25, section 2) applied to the
dihedral-invariant integer polynomials W_d = sum_i w_i w_{i+d} gives
D | W_d(w') - W_d(w) for all d; with |W_d| <= 25*12 = 300 < D this
forces exact constancy W_d(w') = W_d(w), and then S^(d) and A_d
constancy follow from the exact linear relations of wave 25 section 5.

Exact integers throughout. Repository untouched; no Lean build.
"""
import json
from collections import defaultdict
from math import gcd

M = 12
D = 1536796800


def Hvec(y):
    return [6 * y[i] - y[(i - 1) % M] - y[(i + 1) % M] for i in range(M)]


def prime_power_factorization(n):
    """Return list of prime powers q || n."""
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            q = 1
            while n % p == 0:
                n //= p
                q *= p
            out.append(q)
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out


def dihedral_images(w):
    """All 24 dihedral images of a 12-tuple (rotations + reflections)."""
    imgs = []
    for s in range(M):
        imgs.append(tuple(w[(i + s) % M] for i in range(M)))
        imgs.append(tuple(w[(-i + s) % M] for i in range(M)))
    return imgs


def is_dihedral_mod(w1, w2, q):
    """Is w2 mod q a dihedral image of w1 mod q?"""
    t2 = tuple(v % q for v in w2)
    for img in dihedral_images(w1):
        if tuple(v % q for v in img) == t2:
            return True
    return False


def main():
    qs = prime_power_factorization(D)
    prod = 1
    for q in qs:
        prod *= q
    print(f"D = {D}, prime powers: {qs}, product = {prod}", flush=True)
    assert prod == D

    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    groups = cen["split_groups"]
    assert len(groups) == 762, len(groups)

    fail_classes = []
    for g in groups:
        if g["pw_ok"]:
            continue
        by_sw = defaultdict(list)
        for o in g["orbits"]:
            by_sw[tuple(o["sorted_w"])].append(o["rep"])
        for sw, reps in by_sw.items():
            if len(reps) >= 2:
                fail_classes.append(reps)
    print(f"failing (fiber,w)-classes: {len(fail_classes)} (expect 152)",
          flush=True)
    assert len(fail_classes) == 152, len(fail_classes)

    # Per-class: for every pair of reps, check component-wise dihedrality
    # of w, and record which q fail.
    n_pairs = 0
    pair_fail = defaultdict(int)   # q -> # pairs failing at q
    pair_fail_any = 0
    class_fail = 0
    examples = []
    for reps in fail_classes:
        ws = []
        for r in reps:
            hv = Hvec(r)
            assert all(v % D == 0 for v in hv), "Hy not divisible by D"
            ws.append([v // D for v in hv])
        cls_bad = False
        for a in range(len(ws)):
            for b in range(a + 1, len(ws)):
                n_pairs += 1
                bad_qs = [q for q in qs
                          if not is_dihedral_mod(ws[a], ws[b], q)]
                if bad_qs:
                    pair_fail_any += 1
                    cls_bad = True
                    for q in bad_qs:
                        pair_fail[q] += 1
                    if len(examples) < 5:
                        examples.append((ws[a], ws[b], bad_qs))
        if cls_bad:
            class_fail += 1
    print(f"pairs tested: {n_pairs}", flush=True)
    print(f"pairs failing component-wise dihedrality at some q: "
          f"{pair_fail_any}", flush=True)
    print(f"classes with a failing pair: {class_fail} / 152", flush=True)
    for q in qs:
        print(f"  q = {q}: failing pairs = {pair_fail[q]}", flush=True)
    for (wa, wb, bad) in examples:
        print(f"  example failing at {bad}: w = {wa}, w' = {wb}",
              flush=True)

    # Also: global dihedrality of w (expect 0/152, per wave 25) and
    # W_d constancy + D-divisibility recheck on failing classes.
    glob_ok = 0
    wdiff_bad = 0
    for reps in fail_classes:
        ws = []
        for r in reps:
            hv = Hvec(r)
            ws.append([v // D for v in hv])
        for a in range(len(ws)):
            for b in range(a + 1, len(ws)):
                if tuple(ws[b]) in dihedral_images(ws[a]):
                    glob_ok += 1
                for d in range(M):
                    wd_a = sum(ws[a][i] * ws[a][(i + d) % M]
                               for i in range(M))
                    wd_b = sum(ws[b][i] * ws[b][(i + d) % M]
                               for i in range(M))
                    if (wd_b - wd_a) % D != 0:
                        wdiff_bad += 1
    print(f"pairs with w' a GLOBAL dihedral image of w: {glob_ok}",
          flush=True)
    print(f"(pair, d) with W_d diff NOT divisible by D: {wdiff_bad}",
          flush=True)


if __name__ == "__main__":
    main()
