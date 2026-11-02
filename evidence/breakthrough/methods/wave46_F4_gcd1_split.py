# Mod-p reduction analysis: at p=41 (m=180) and p=239 (m=252), v_p(D_m)=2 and
# p does not divide m/ord, so ker(M^m - I) mod p^2 = p * (seeds mod p); every
# nonzero kernel sequence mod p^2 is p * (nonzero mod-p sequence), period = ord.
# Hence splitness at p^2 <=> splitness of the ord-tuples mod p.
from collections import defaultdict

def analyze(p, order, m):
    # enumerate seeds (y0,y1) in F_p^2, build order-tuple via recurrence
    fibers = defaultdict(list)  # sorted tuple -> list of tuples
    for y0 in range(p):
        for y1 in range(p):
            if y0 == 0 and y1 == 0:
                continue
            t = [y0, y1]
            for i in range(2, order):
                t.append((6*t[-1] - t[-2]) % p)
            t = tuple(t)
            # check closure: t must be order-periodic (M^order = I mod p)
            assert (6*t[-1] - t[-2]) % p == t[0] and (6*t[0] - t[-1]) % p == t[1], (p, t)
            fibers[tuple(sorted(t))].append(t)
    def canon(t):
        # dihedral canonical form of the cycle: rotations + reversed rotations
        rots = [tuple(t[(i+k) % order] for i in range(order)) for k in range(order)]
        rev = (t[0],) + tuple(t[order-1-i] for i in range(order-1))  # (t0, t_{o-1}, ..., t1)
        rrots = [tuple(rev[(i+k) % order] for i in range(order)) for k in range(order)]
        return min(rots + rrots)
    split = []
    for key, members in fibers.items():
        orbits = {}
        for t in members:
            orbits.setdefault(canon(t), []).append(t)
        if len(orbits) > 1:
            split.append((key, list(orbits.keys())))
    print(f"p={p} order={order} m={m}: nonzero seeds={p*p-1}, fibers={len(fibers)}, "
          f"split fibers={len(split)}")
    if split:
        key, reps = split[0]
        print(f"  FIBER-0 multiset={key} n_orbits={len(reps)} rep0={reps[0]}")
    else:
        # largest fiber sizes, to show the check is nontrivial
        sizes = sorted((len(v) for v in fibers.values()), reverse=True)[:5]
        print(f"  no split fibers; largest fiber sizes={sizes}")
    return split

s41 = analyze(41, 5, 180)
s239 = analyze(239, 7, 252)
