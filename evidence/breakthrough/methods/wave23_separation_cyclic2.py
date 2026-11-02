"""Wave 23, task 4, part 2: extended battery + residual groups + the
affine-permutation mechanism behind the exhibit pair.

1. Extended reflection-invariant kernels (triple statistics included):
   does any small family separate ALL 762 split fibers / 152 failing
   classes? Which groups resist the best pair {a2b2, absdiff}?
2. Exhibit pair mechanism: verify y2 = y1 under position permutation
   sigma(i) = 5i + 4 (mod 12), so y2's 1-step edges are y1's 5-step
   edges. Test whether k-step cyclic sums agree with 1-step sums for
   other census reps (structural Fix phenomenon?) or only this pair.
All arithmetic exact integers. Repository untouched; no Lean build.
"""
import json
from collections import Counter

M = 12


def edge_sums(y, kernels):
    return {n: sum(f(y[i], y[(i + 1) % M]) for i in range(M))
            for n, f in kernels.items()}


def triple_stats(y):
    prod = sum(y[i] * y[(i + 1) % M] * y[(i + 2) % M] for i in range(M))
    # Direction changes: reflection-invariant (reversal preserves the
    # set of turning points, only flips their orientation).
    dch = sum(1 for i in range(M)
              if (y[(i + 1) % M] - y[i]) * (y[(i + 2) % M] - y[(i + 1) % M]) < 0)
    return {"triple_prod": prod, "dir_changes": dch}


def all_stats(y):
    kernels = {
        "ab": lambda a, b: a * b,
        "absdiff": lambda a, b: abs(a - b),
        "a2b2": lambda a, b: (a * b) ** 2,
        "a3b3": lambda a, b: (a * b) ** 3,
        "ab_absdiff": lambda a, b: a * b * abs(a - b),
    }
    out = edge_sums(y, kernels)
    out.update(triple_stats(y))
    return out


def kstep_sum(y, k, f):
    return sum(f(y[i], y[(i + k) % M]) for i in range(M))


def main():
    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    groups = cen["split_groups"]

    fail_classes = []
    for g in groups:
        if g["pw_ok"]:
            continue
        by_sw = {}
        for o in g["orbits"]:
            by_sw.setdefault(tuple(o["sorted_w"]), []).append(o["rep"])
        for sw, reps in by_sw.items():
            if len(reps) >= 2:
                fail_classes.append(reps)

    names = list(all_stats(groups[0]["orbits"][0]["rep"]).keys())
    sepA = {n: set() for n in names}
    sepB = {n: set() for n in names}
    for gi, g in enumerate(groups):
        cs = [all_stats(o["rep"]) for o in g["orbits"]]
        for n in names:
            if len({c[n] for c in cs}) == len(cs):
                sepA[n].add(gi)
    for bi, reps in enumerate(fail_classes):
        cs = [all_stats(r) for r in reps]
        for n in names:
            if len({c[n] for c in cs}) == len(cs):
                sepB[n].add(bi)
    print(f"{'kernel':<14} {'A/762':>7} {'B/152':>7}", flush=True)
    for n in names:
        print(f"{n:<14} {len(sepA[n]):>7} {len(sepB[n]):>7}", flush=True)

    def greedy(sep, universe, label):
        covered, fam = set(), []
        while len(covered) < len(universe):
            best = max(names, key=lambda n: len(sep[n] - covered))
            if len(sep[best] - covered) == 0:
                break
            fam.append(best)
            covered |= sep[best]
        res = universe - covered
        print(f"greedy {label}: {fam} covers {len(covered)}/{len(universe)}; "
              f"residual: {sorted(res)[:20]}"
              f"{'...' if len(res) > 20 else ''}", flush=True)
        return fam, res

    famA, resA = greedy(sepA, set(range(len(groups))), "level A")
    famB, resB = greedy(sepB, set(range(len(fail_classes))), "level B")

    # Residual groups: what are they? (print sizes / orbit counts)
    for label, res, coll in (("A", resA, groups), ("B", resB, fail_classes)):
        for idx in sorted(res)[:10]:
            if label == "A":
                g = coll[idx]
                print(f"  residual {label}[{idx}]: {len(g['orbits'])} orbits, "
                      f"fiber_size {g['fiber_size']}, pw_ok {g['pw_ok']}",
                      flush=True)
            else:
                print(f"  residual {label}[{idx}]: {len(coll[idx])} orbits",
                      flush=True)

    # Exhibit pair mechanism.
    y1 = [1024531200, 475675200, 292723200, 1280664000, 1244073600,
          36590400, 512265600, 1500206400, 804988800, 256132800,
          731808000, 1061121600]
    y2 = [1244073600, 256132800, 292723200, 1500206400, 1024531200,
          36590400, 731808000, 1280664000, 804988800, 475675200,
          512265600, 1061121600]
    sig = [(5 * i + 4) % M for i in range(M)]
    print("\ny2[i] == y1[5i+4] for all i:",
          all(y2[i] == y1[sig[i]] for i in range(M)), flush=True)
    for k in (1, 5, 7, 11):
        print(f"  y1 {k}-step ab-sum == 1-step ab-sum:",
              kstep_sum(y1, k, lambda a, b: a * b)
              == kstep_sum(y1, 1, lambda a, b: a * b), flush=True)
    print("  exhibit ab_absdiff: y1 =", all_stats(y1)["ab_absdiff"],
          " y2 =", all_stats(y2)["ab_absdiff"],
          " differ =", all_stats(y1)["ab_absdiff"]
          != all_stats(y2)["ab_absdiff"], flush=True)
    # Gamma-invariance of ab_absdiff on a sample of reps (symmetric
    # kernel => structural, verified anyway).
    from wave23_separation_cyclic import dihedral_perms
    bad = 0
    for g in groups[:50]:
        for o in g["orbits"]:
            base = all_stats(o["rep"])["ab_absdiff"]
            for img in dihedral_perms(o["rep"]):
                if all_stats(img)["ab_absdiff"] != base:
                    bad += 1
    print("  ab_absdiff dihedral-invariance violations (first 50 fibers):",
          bad, flush=True)

    # Is k-step == 1-step agreement common across census reps?
    units = (5, 7, 11)
    agree = {k: 0 for k in units}
    tot = 0
    for g in groups[:100]:
        for o in g["orbits"]:
            r = o["rep"]
            tot += 1
            for k in units:
                if kstep_sum(r, k, lambda a, b: a * b) == \
                        kstep_sum(r, 1, lambda a, b: a * b):
                    agree[k] += 1
    print(f"k-step ab-sum == 1-step ab-sum over {tot} reps:",
          {k: agree[k] for k in units}, flush=True)


if __name__ == "__main__":
    main()
