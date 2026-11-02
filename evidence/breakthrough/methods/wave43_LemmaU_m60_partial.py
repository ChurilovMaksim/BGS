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
    seen=set(); stack=[(ta,tb)]
    while stack:
        a,b = stack.pop()
        if (a,b) in seen: continue
        seen.add((a,b))
        stack.append((shift(a,1), shift(b,1)))
        stack.append((rev(a), rev(b)))
        stack.append((neg(a,pa), neg(b,pb)))
    return seen
def P_of(ta, tb, pa, pb):
    b0 = tuple(sorted((ta[k]*pb+tb[k]) for k in range(30)))
    b1 = tuple(sorted(((-ta[k] % pa)*pb + (-tb[k] % pb)) for k in range(30)))
    return tuple(sorted(b0 + b1))

for (pa,pb) in [(9,11),(9,19),(9,59),(11,19),(11,59),(19,59)]:
    ca, cb = cycles(pa), cycles(pb)
    groups = defaultdict(set)
    for A, ta in ca.items():
        for B, tb in cb.items():
            groups[P_of(ta,tb,pa,pb)].add((ta,tb))
    res = Counter(); bad = 0
    for P, cycs in groups.items():
        rem=set(cycs); orbs=[]
        while rem:
            c=next(iter(rem)); o=G_orbit(c[0],c[1],pa,pb)&cycs; orbs.append(o); rem-=o
        if len(orbs)==1: continue
        o1, o2 = orbs[0], orbs[1]
        c=next(iter(o1))
        moves = {
            'revA': (rev(c[0]), c[1]), 'revB': (c[0], rev(c[1])),
            'negA': (neg(c[0],pa), c[1]), 'negB': (c[0], neg(c[1],pb)),
        }
        found = [name for name, m in moves.items() if G_orbit(m[0],m[1],pa,pb)&cycs == o2]
        res[tuple(found)] += 1
        if not found: bad += 1
    print(f"pair ({pa},{pb}): multi-orbit groups explained by partial moves:")
    for k,v in sorted(res.items(), key=str): print("   ", k, "->", v)
    print("   unexplained:", bad)
