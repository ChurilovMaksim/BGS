from collections import defaultdict, Counter

def cycles(p):
    out = {}
    for a in range(p):
        for b in range(p):
            s0 = (2*a) % p; s1 = (2*(17*a+24*b)) % p
            s = [s0, s1]
            for k in range(2, 30): s.append((34*s[-1] - s[-2]) % p)
            out[(a,b)] = tuple(s)
    return out

def shift(c, r): return tuple(c[(k+r) % 30] for k in range(30))
def rev(c): return tuple(c[(-k) % 30] for k in range(30))
def neg(c, p): return tuple((-x) % p for x in c)

def G_orbit(ta, tb, pa, pb):
    # generators on cycle-pairs: shift both, reverse both, negate both
    seen=set(); stack=[(ta,tb)]
    while stack:
        a,b = stack.pop()
        if (a,b) in seen: continue
        seen.add((a,b))
        stack.append((shift(a,1), shift(b,1)))
        stack.append((rev(a), rev(b)))
        stack.append((neg(a,pa), neg(b,pb)))
    return seen

for (pa,pb) in [(9,19),(9,59),(11,19),(11,59),(19,59)]:
    ca, cb = cycles(pa), cycles(pb)
    # group by P, keeping cycle-pairs (kernel translates collapse: same cycle-pair)
    groups = defaultdict(set)
    for A, ta in ca.items():
        for B, tb in cb.items():
            b0 = tuple(sorted((ta[k]*pb+tb[k]) for k in range(30)))
            b1 = tuple(sorted(((-ta[k] % pa)*pb + (-tb[k] % pb)) for k in range(30)))
            P = tuple(sorted(b0 + b1))
            groups[P].add((ta,tb))
    stats = Counter(); multi = []
    for P, cycs in groups.items():
        rem = set(cycs); norb = 0; sizes=[]
        while rem:
            c = next(iter(rem))
            o = G_orbit(c[0], c[1], pa, pb)
            # intersect with cycs (orbit may leave the group? it shouldn't: G preserves P)
            o &= cycs
            sizes.append(len(o)); rem -= o; norb += 1
        stats[(len(cycs), norb, tuple(sorted(sizes)))] += 1
        if norb >= 2: multi.append((P, cycs, sizes))
    print(f"pair ({pa},{pb}): groups={len(groups)}; (cycle-pairs, #G-orbits, orbit sizes) -> count")
    for k,v in sorted(stats.items()): print("   ", k, "->", v)
    print(f"   multi-orbit groups: {len(multi)}")
    for P, cycs, sizes in multi[:3]:
        print("    sizes", sizes, "example cycles:", sorted(cycs)[:2])
