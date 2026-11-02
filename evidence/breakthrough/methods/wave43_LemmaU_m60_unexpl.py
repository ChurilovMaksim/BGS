from collections import defaultdict

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

pa, pb = 11, 19
ca, cb = cycles(pa), cycles(pb)
groups = defaultdict(set)
for A, ta in ca.items():
    for B, tb in cb.items():
        groups[P_of(ta,tb,pa,pb)].add((ta,tb))
n=0
for P, cycs in groups.items():
    rem=set(cycs); orbs=[]
    while rem:
        c=next(iter(rem)); o=G_orbit(c[0],c[1],pa,pb)&cycs; orbs.append(o); rem-=o
    if len(orbs)!=2: continue
    o1, o2 = orbs
    c=next(iter(o1))
    na=(neg(c[0],pa), c[1]); nb=(c[0], neg(c[1],pb))
    if G_orbit(na[0],na[1],pa,pb)&cycs == o2 or G_orbit(nb[0],nb[1],pa,pb)&cycs == o2:
        continue
    n+=1
    if n>2: continue
    print("=== unexplained group", n)
    c1=next(iter(o1)); c2=next(iter(o2))
    print("o1 ta:", c1[0][:12], " tb:", c1[1][:12])
    print("o2 ta:", c2[0][:12], " tb:", c2[1][:12])
    # try: is c2 = (shift(ta,r), shift(tb,s)) for some (r,s)?
    found=[]
    for r in range(30):
        for s in range(30):
            if (shift(c1[0],r), shift(c1[1],s)) in o2: found.append((r,s))
    print("independent-shift relations o1->o2:", found[:10])
    # try reversals mixed: (rev/shift combos)
    for r in range(30):
        for s in range(30):
            if (shift(rev(c1[0]),r), shift(c1[1],s)) in o2: found.append(('revA',r,s))
            if (shift(c1[0],r), shift(rev(c1[1]),s)) in o2: found.append(('revB',r,s))
    print("with reversals:", [f for f in found if isinstance(f[0],str)][:10])
    # block pairs
    def blocks(ta,tb):
        b0=tuple(sorted((ta[k],tb[k]) for k in range(30)))
        b1=tuple(sorted(((-ta[k]%pa),(-tb[k]%pb)) for k in range(30)))
        return (b0,b1) if b0<=b1 else (b1,b0)
    print("block pairs equal:", blocks(*c1)==blocks(*c2))
print("total unexplained:", n)
