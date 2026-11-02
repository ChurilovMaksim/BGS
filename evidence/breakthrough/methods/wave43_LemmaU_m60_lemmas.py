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
def period(c):
    for d in range(1, 31):
        if all(c[k] == c[k % d] for k in range(30)): return d
    return 30
def multiset(c): return tuple(sorted(c))

pa, pb = 11, 19
ca, cb = cycles(pa), cycles(pb)
# --- period classification via beta^d - 1 norms (in R/p, field since 2 non-residue mod 11,19)
# beta = 17+12 sqrt2; compute beta^d - 1 and its norm mod p; C has period | d iff C*(beta^d-1)=0
def mulR(x,y,p): return ((x[0]*y[0]+2*x[1]*y[1])%p, (x[0]*y[1]+x[1]*y[0])%p)
def pwR(x,n,p):
    r=(1,0)
    while n:
        if n&1: r=mulR(r,x,p)
        x=mulR(x,x,p); n>>=1
    return r
beta=(17,12)
for p in (11,19):
    print(f"--- mod {p}: beta orders / beta^d-1 norms")
    for d in (1,2,3,5,6,10):
        bd = pwR(beta,d,p)
        diff = ((bd[0]-1)%p, bd[1]%p)
        norm = (diff[0]**2 - 2*diff[1]**2) % p
        print(f"   d={d}: beta^d-1={diff}, norm={norm} ({'unit' if norm%p!=0 else 'ZERO DIVISOR'})")
    # observed periods
    from collections import Counter
    cyc = ca if p==11 else cb
    print("   observed trace-cycle periods:", Counter(period(c) for c in cyc.values()))

# --- L1 (19-side): cycle with multiset M(s) or M(-s) is dihedral (shift/rev) to s or -s
def dihedral_cycle_orbit(c, p):
    seen=set()
    for r in range(30):
        seen.add(shift(c,r)); seen.add(shift(rev(c),r))
    return seen
bad1=0
for C, s in cb.items():
    ms, mns = multiset(s), multiset(neg(s,pb))
    for C2, x in cb.items():
        if multiset(x) in (ms, mns):
            if x not in dihedral_cycle_orbit(s,pb) and x not in dihedral_cycle_orbit(neg(s,pb),pb):
                bad1+=1
print("L1 (19-side) violations:", bad1, "(over 361x361)")

# --- L3 (19-side single): M(x) u M(y) = M(t) u M(-t) => {M(x),M(y)} = {M(t),M(-t)}
# group cycles by multiset
byms = defaultdict(list)
for C, x in cb.items(): byms[multiset(x)].append(x)
# for each pair of multisets (mx,my), check unions against (mt, -mt)
ms_list = list(byms.keys())
bad3=0; checked=0
for i, mx in enumerate(ms_list):
    for my in ms_list[i:]:
        u = tuple(sorted(mx+my))
        # does there exist mt with sorted(mt + (-mt)) == u and {mx,my} != {mt,-mt}?
        for mt in ms_list:
            if tuple(sorted(mt + tuple(sorted((-v)%pb for v in mt)))) == u:
                if set([mx,my]) != set([mt, tuple(sorted((-v)%pb for v in mt))]):
                    bad3+=1
        checked+=1
print("L3 (19-side) violations:", bad3, f"(over {checked} multiset pairs)")

# --- L2' (11-side fibers): E/O multisets determine cycle up to dihedral + parity flip
# E(x) = {x_0,x_2,x_4}, O(x) = {x_1,x_3,x_5} (period-6 cycles; for smaller periods these still work)
def EO(x):
    return (tuple(sorted((x[0],x[2],x[4]))), tuple(sorted((x[1],x[3],x[5]))))
bad2=0; tot2=0
for C, t in ca.items():
    if period(t) not in (6,): continue
    target = EO(t)
    for C2, x in ca.items():
        if EO(x)==target or EO(x)==(target[1],target[0]):
            tot2+=1
            # x should be dihedral to t, or to neg(t) (parity flip = shift by 3 = negation on 11-side? shift(t,3)=-t since beta^3=-1)
            if x not in dihedral_cycle_orbit(t,pa) and x not in dihedral_cycle_orbit(neg(t,pa),pa):
                bad2+=1
print(f"L2' (11-side fibers, period-6 cycles): {tot2} matches, violations: {bad2}")

# --- kernel lemma at 3: cycles mod 9 determine C up to {(0,3t)}
c9 = cycles(9)
bymap = defaultdict(set)
for C, x in c9.items(): bymap[x].add(C)
maxfib = max(len(v) for v in bymap.values())
kern_ok = all(len(v)==3 and set((c[0], (c[1]-next(iter(v))[1])%9) for c in v)=={(0,0),(0,3),(0,6)} for v in bymap.values() if len(v)==3)
print(f"kernel lemma mod 9: {len(bymap)} distinct cycles from 81 params, max fiber {maxfib}, all fibers are kernel triples: {kern_ok}")
