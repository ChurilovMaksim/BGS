"""Wave 27, task 5, checks 2: sanity + mechanism hunt for the W-mod lemma.

(a) Sanity: is y' a component-wise dihedral image of y mod q for the
    152 failing pairs? (Validates the dihedral convention against the
    wave-25 section 2 hypothesis.)
(b) W_d D-divisibility on ALL 762 split groups (broad version?).
(c) Stronger w-side test: is w' a dihedral image of w mod (D/q) for
    some dihedral map (per q)? If yes for all q, then (D/q) | dW_d
    for all q, and lcm{D/q} = D gives D | dW_d.
(d) Permutation structure: for each failing pair, find permutations
    tau with tau(w) = w' and report their cycle-type / position-mod
    patterns.

Exact integers throughout. Repository untouched; no Lean build.
"""
import json
from collections import defaultdict

M = 12
D = 1536796800
QS = [128, 81, 25, 49, 121]


def Hvec(y):
    return [6 * y[i] - y[(i - 1) % M] - y[(i + 1) % M] for i in range(M)]


def dihedral_images(w):
    imgs = []
    for s in range(M):
        imgs.append(tuple(w[(i + s) % M] for i in range(M)))
        imgs.append(tuple(w[(-i + s) % M] for i in range(M)))
    return imgs


def is_dihedral_mod(w1, w2, q):
    t2 = tuple(v % q for v in w2)
    for img in dihedral_images(w1):
        if tuple(v % q for v in img) == t2:
            return True
    return False


def Wd(w, d):
    return sum(w[i] * w[(i + d) % M] for i in range(M))


def perms_mapping(w1, w2):
    """All perms tau (as tuples of images of positions) with w2[i]=w1[tau(i)]?
    Brute force over position bijections is 12! -- instead return the
    set of possible images per position and whether a 'dihedral-like'
    pattern exists: positions grouped by value."""
    # positions of each value in w1 and w2
    from collections import defaultdict as dd
    p1, p2 = dd(list), dd(list)
    for i, v in enumerate(w1):
        p1[v].append(i)
    for i, v in enumerate(w2):
        p2[v].append(i)
    return p1, p2


def main():
    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    groups = cen["split_groups"]
    assert len(groups) == 762

    fail_classes = []
    all_pairs = []  # (reps) for all split groups
    for g in groups:
        reps = [o["rep"] for o in g["orbits"]]
        all_pairs.append(reps)
        if g["pw_ok"]:
            continue
        by_sw = defaultdict(list)
        for o in g["orbits"]:
            by_sw[tuple(o["sorted_w"])].append(o["rep"])
        for sw, rr in by_sw.items():
            if len(rr) >= 2:
                fail_classes.append(rr)
    assert len(fail_classes) == 152

    # (a) y-side component-wise dihedrality on failing pairs
    y_fail = defaultdict(int)
    y_pairs = 0
    for reps in fail_classes:
        for a in range(len(reps)):
            for b in range(a + 1, len(reps)):
                y_pairs += 1
                for q in QS:
                    if not is_dihedral_mod(reps[a], reps[b], q):
                        y_fail[q] += 1
    print(f"(a) failing pairs: {y_pairs}; y-side dihedral failures per q:",
          dict(y_fail), flush=True)

    # (b) W_d D-divisibility on ALL split groups
    tot = 0
    bad = 0
    bad_groups = 0
    for reps in all_pairs:
        ws = []
        for r in reps:
            hv = Hvec(r)
            assert all(v % D == 0 for v in hv)
            ws.append([v // D for v in hv])
        gbad = False
        for a in range(len(ws)):
            for b in range(a + 1, len(ws)):
                for d in range(M):
                    tot += 1
                    if (Wd(ws[b], d) - Wd(ws[a], d)) % D != 0:
                        bad += 1
                        gbad = True
        if gbad:
            bad_groups += 1
    print(f"(b) all split groups: (pair,d) tested {tot}, "
          f"not D-divisible {bad}, groups with a violation {bad_groups}",
          flush=True)

    # (c) w' dihedral mod (D/q)?
    c_fail = defaultdict(int)
    c_pairs = 0
    for reps in fail_classes:
        ws = []
        for r in reps:
            hv = Hvec(r)
            ws.append([v // D for v in hv])
        for a in range(len(ws)):
            for b in range(a + 1, len(ws)):
                c_pairs += 1
                for q in QS:
                    if not is_dihedral_mod(ws[a], ws[b], D // q):
                        c_fail[q] += 1
    print(f"(c) failing pairs: {c_pairs}; w-side dihedral-mod-(D/q) "
          f"failures per q:", dict(c_fail), flush=True)

    # (d) permutation structure of failing pairs: for each pair, check
    # whether some tau mapping w->w' preserves i mod 2, mod 3, mod 4,
    # or is an involution-free pattern; report counts of value
    # multiplicities and a few explicit taus via backtracking.
    import itertools
    tau_mod2 = 0
    tau_mod3 = 0
    tau_mod4 = 0
    tau_any = 0
    shown = 0
    for reps in fail_classes:
        ws = []
        for r in reps:
            hv = Hvec(r)
            ws.append([v // D for v in hv])
        for a in range(len(ws)):
            for b in range(a + 1, len(ws)):
                w1, w2 = ws[a], ws[b]
                # backtracking search for one tau with w2[i] = w1[tau[i]]
                used = [False] * M
                tau = [None] * M

                def bt(i):
                    if i == M:
                        return True
                    for j in range(M):
                        if not used[j] and w1[j] == w2[i]:
                            used[j] = True
                            tau[i] = j
                            if bt(i + 1):
                                return True
                            used[j] = False
                    return False

                assert bt(0)
                tau_any += 1
                if all((tau[i] % 2) == (i % 2) for i in range(M)):
                    tau_mod2 += 1
                if all((tau[i] % 3) == (i % 3) for i in range(M)):
                    tau_mod3 += 1
                if all((tau[i] % 4) == (i % 4) for i in range(M)):
                    tau_mod4 += 1
                if shown < 3:
                    print(f"(d) example tau (w2[i]=w1[tau[i]]): {tau} "
                          f"for w1={w1} w2={w2}", flush=True)
                    shown += 1
    print(f"(d) taus preserving mod 2: {tau_mod2}, mod 3: {tau_mod3}, "
          f"mod 4: {tau_mod4}, total pairs: {tau_any}", flush=True)


if __name__ == "__main__":
    main()
