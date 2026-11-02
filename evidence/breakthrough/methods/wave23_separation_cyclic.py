"""Wave 23, task 4: how much cyclic-order data must 152's separation step gain?

Question: mode sums S_k are symmetric => fiber-constant, so no function of
them separates orbits inside a fiber (wave 22, task 4). Adj(y) separates
all 762 split fibers on support at m=12 (wave 21), but Adj is cyclic-order
data, not mode-sum data. Here we test the middle ground: cyclic pair sums
C_f(y) = sum_i f(y_i, y_{i+1}) with f symmetric in its two arguments.
Such sums are dihedral-invariant (hence well-defined on orbits) but NOT
symmetric in coordinates (hence can vary inside a fiber). Do single
cyclic sums, or small families of them, separate the orbits?

Data: wave-18 census of the 762 split fibers fully in support at m=12.
Two separation levels:
  (A) all orbits within each of the 762 split fibers;
  (B) orbits within each of the 152 P_w-failing (fiber, w)-classes
      (orbits sharing sorted(w) inside a split fiber) -- the actual gap
      left after route (b).
All arithmetic exact integers. Repository untouched; no Lean build.
"""
import json
from itertools import combinations

M = 12
D = 1536796800  # D_12, from wave-21 script (asserted via H determinant there)

# Cyclic-sum kernels. For a cyclic sum C_f(y) = sum_i f(y_i, y_{i+1})
# to be well-defined on dihedral (Gamma) orbits, f MUST be symmetric in
# its two arguments: reversal sends each edge (a, b) to (b, a). A naive
# ascent count is NOT reflection-invariant (reversal swaps ascents and
# descents), so it is excluded; only reflection-invariant combinations
# (min/max of ascent/descent counts) are used. Note: sum of (a-b)^2
# over the cycle = 2*sum a^2 - 2*sum a*b, and sum a^2 is fiber-constant,
# so the (a-b)^2 sum carries exactly the same separating power as the
# ab sum; likewise a^2+b^2 sums are fiber-constant and useless.
FUNS = {
    "ab": lambda a, b: a * b,
    "absdiff": lambda a, b: abs(a - b),
    "a2b2": lambda a, b: (a * b) ** 2,
    "ab_a2pb2": lambda a, b: a * b * (a * a + b * b),
    "min": lambda a, b: min(a, b),
    "max": lambda a, b: max(a, b),
    "equal": lambda a, b: 1 if a == b else 0,
}


def cyclic_sums(y):
    out = {name: sum(f(y[i], y[(i + 1) % M]) for i in range(M))
           for name, f in FUNS.items()}
    # Reflection-invariant ascent/descent statistics (reversal swaps
    # ascents and descents; their min and their difference are fixed).
    asc = sum(1 for i in range(M) if y[i] < y[(i + 1) % M])
    desc = sum(1 for i in range(M) if y[i] > y[(i + 1) % M])
    out["asc_min"] = min(asc, desc)
    out["asc_diff"] = abs(asc - desc)
    return out


def dihedral_perms(y):
    """All 24 dihedral images of y (12 rotations x reversal)."""
    out = []
    for rev in (False, True):
        z = list(reversed(y)) if rev else list(y)
        for s in range(M):
            out.append([z[(i + s) % M] for i in range(M)])
    return out


def main():
    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    groups = cen["split_groups"]
    assert len(groups) == 762, len(groups)

    # Level B: failing (fiber, w)-classes = orbits sharing sorted(w) in
    # groups with pw_ok == False.
    fail_classes = []  # list of lists of reps
    for g in groups:
        if g["pw_ok"]:
            continue
        by_sw = {}
        for o in g["orbits"]:
            by_sw.setdefault(tuple(o["sorted_w"]), []).append(o["rep"])
        for sw, reps in by_sw.items():
            if len(reps) >= 2:
                fail_classes.append(reps)
    print(f"split fibers: {len(groups)}; failing (fiber,w)-classes: "
          f"{len(fail_classes)}", flush=True)

    # Per-orbit cyclic sums, level A (whole fiber) and level B (class).
    def separated(vals):
        return len(set(vals)) == len(vals)

    names = list(cyclic_sums(groups[0]["orbits"][0]["rep"]).keys())
    countA = {n: 0 for n in names}
    countB = {n: 0 for n in names}
    # For greedy family: which groups does each f separate?
    sepA = {n: set() for n in names}
    sepB = {n: set() for n in names}
    for gi, g in enumerate(groups):
        reps = [o["rep"] for o in g["orbits"]]
        cs = [cyclic_sums(r) for r in reps]
        for n in names:
            if separated([c[n] for c in cs]):
                countA[n] += 1
                sepA[n].add(gi)
    for bi, reps in enumerate(fail_classes):
        cs = [cyclic_sums(r) for r in reps]
        for n in names:
            if separated([c[n] for c in cs]):
                countB[n] += 1
                sepB[n].add(bi)
    print(f"\n{'kernel':<12} {'level A /762':>12} {'level B /nclass':>16}",
          flush=True)
    for n in names:
        print(f"{n:<12} {countA[n]:>12} {countB[n]:>16}", flush=True)

    # Greedy minimal family jointly separating all groups at each level.
    def greedy(sep, total, label):
        covered, fam = set(), []
        while len(covered) < total:
            best = max(names, key=lambda n: len(sep[n] - covered))
            gain = len(sep[best] - covered)
            if gain == 0:
                break
            fam.append(best)
            covered |= sep[best]
        print(f"greedy {label}: family {fam} covers {len(covered)}/{total}",
              flush=True)
        return fam

    greedy(sepA, len(groups), "level A (all split fibers)")
    greedy(sepB, len(fail_classes), "level B (failing classes)")

    # Gamma-invariance spot check: cyclic sums constant on dihedral
    # images of a few reps (structural for symmetric f, verified anyway).
    bad = 0
    for g in groups[:20]:
        for o in g["orbits"]:
            base = cyclic_sums(o["rep"])
            for img in dihedral_perms(o["rep"]):
                if cyclic_sums(img) != base:
                    bad += 1
    print(f"\ndihedral-invariance violations (first 20 fibers): {bad}",
          flush=True)

    # Wave-22 exhibit pair, independently rechecked.
    y1 = [1024531200, 475675200, 292723200, 1280664000, 1244073600,
          36590400, 512265600, 1500206400, 804988800, 256132800,
          731808000, 1061121600]
    y2 = [1244073600, 256132800, 292723200, 1500206400, 1024531200,
          36590400, 731808000, 1280664000, 804988800, 475675200,
          512265600, 1061121600]

    def Hvec(y):
        return [6 * y[i] - y[(i - 1) % M] - y[(i + 1) % M]
                for i in range(M)]

    def wvec(y):
        w = Hvec(y)
        assert all(v % D == 0 for v in w)
        return [v // D for v in w]

    def adj(y):
        return tuple(sorted(tuple(sorted((y[i], y[(i + 1) % M])))
                            for i in range(M)))

    print("\nexhibit pair checks:", flush=True)
    print(" same sorted multiset:", sorted(y1) == sorted(y2), flush=True)
    print(" same sorted(w):",
          sorted(wvec(y1)) == sorted(wvec(y2)), sorted(wvec(y1)), flush=True)
    print(" dihedral images of y1 containing y2:",
          sum(1 for img in dihedral_perms(y1) if img == y2), flush=True)
    from collections import Counter
    adjdiff = sum((Counter(adj(y1)) - Counter(adj(y2))).values()) + \
        sum((Counter(adj(y2)) - Counter(adj(y1))).values())
    print(" Adj differs:", adj(y1) != adj(y2),
          "multiset symmetric difference size:", adjdiff, flush=True)
    c1, c2 = cyclic_sums(y1), cyclic_sums(y2)
    for n in c1:
        print(f"  cyclic {n}: y1={c1[n]} y2={c2[n]} differ={c1[n] != c2[n]}",
              flush=True)


if __name__ == "__main__":
    main()
