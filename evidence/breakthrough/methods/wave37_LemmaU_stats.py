"""Wave 37, task 3: fiber-size statistics for the Lemma U test.

Reuses build_component from wave37_LemmaU_test.py. For each case,
reports: total points, #P-groups, max group size, #singleton groups,
#groups with size >= 10 / >= 100, #groups with block0 == block1,
#groups whose P has a repeated pair (non-distinct case).
"""

import sys
from collections import Counter

sys.path.insert(0, ".")
from wave37_LemmaU_test import build_component


def stats(m, pa, fa, pb, fb):
    moda, _, seqs_a, tau_a = build_component(pa, fa, m)
    modb, _, seqs_b, tau_b = build_component(pb, fb, m)
    B = moda * modb
    groups = {}  # P-key -> [blockpair, count, blocks_equal, pairs_distinct]
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
            prev = groups.get(key)
            if prev is None:
                groups[key] = [bp, 1, e0 == e1, len(set(allp)) == len(allp)]
            else:
                assert prev[0] == bp, "CONFLICT (should not happen)"
                prev[1] += 1
    sizes = Counter(v[1] for v in groups.values())
    npts = sum(sizes.values()) and sum(k * v for k, v in sizes.items())
    print(f"m={m} ({pa}^{2*fa},{pb}^{2*fb}): points={npts} "
          f"groups={len(groups)} max_size={max(sizes)} "
          f"singletons={sizes[1]} ge10={sum(v for k, v in sizes.items() if k >= 10)} "
          f"ge100={sum(v for k, v in sizes.items() if k >= 100)} "
          f"blocks_equal_groups={sum(1 for v in groups.values() if v[2])} "
          f"nondistinct_P_groups={sum(1 for v in groups.values() if not v[3])}",
          flush=True)


if __name__ == "__main__":
    stats(30, 5, 2, 29, 1)
    stats(18, 5, 1, 197, 1)
