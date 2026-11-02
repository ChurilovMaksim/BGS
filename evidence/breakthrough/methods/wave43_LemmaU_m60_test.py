# Exact Lemma-U test at m=60, pair (121, 361): q_a=11^2, q_b=19^2, f=1 both.
# C in R/p; traces s_{k+1} = 34 s_k - s_{k-1} mod p; block1 = -block0 (alpha^30 = -1).
# Group by sorted P = block0 union (-block0); conflict = two distinct unordered block pairs.
from collections import defaultdict, Counter

def cycles(p):
    # returns dict C=(a,b) -> tuple of 30 traces
    out = {}
    for a in range(p):
        for b in range(p):
            s0 = (2*a) % p
            s1 = (2*(17*a+24*b)) % p
            s = [s0, s1]
            for k in range(2, 30):
                s.append((34*s[-1] - s[-2]) % p)
            out[(a,b)] = tuple(s)
    return out

for (pa, pb) in [(11,19)]:
    ca, cb = cycles(pa), cycles(pb)
    groups = {}
    conflicts = 0
    for A, ta in ca.items():
        for B, tb in cb.items():
            b0 = tuple(sorted((ta[k], tb[k]) for k in range(30)))
            b1 = tuple(sorted((-ta[k] % pa, -tb[k] % pb) for k in range(30)))
            P = tuple(sorted(b0 + b1))
            bp = (b0, b1) if b0 <= b1 else (b1, b0)
            if P in groups:
                if groups[P][0] != bp:
                    conflicts += 1
                    if conflicts <= 5:
                        print("CONFLICT at", A, B, "prev pair:", groups[P][1])
                groups[P][1].append((A,B))
            else:
                groups[P] = (bp, [(A,B)])
    sizes = Counter(len(v[1]) for v in groups.values())
    print(f"pair ({pa},{pb}): points={pa*pa*pb*pb}, groups={len(groups)}, conflicts={conflicts}")
    print("  size histogram:", dict(sorted(sizes.items())))
    big = [(k, v) for k, v in groups.items() if len(v[1]) > 120]
    print(f"  groups > 120 (dihedral max 2m): {len(big)}")
    for k, v in big[:10]:
        print("   size", len(v[1]), "reps:", v[1][:6])
