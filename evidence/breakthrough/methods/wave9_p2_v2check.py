import itertools, collections
# starting tuple mod32: (T, 3T+D, 17T+6D, 3T+3D) mod32, T in Z32, D in {0,8,16,24}
def start(T,D):
    return tuple((x%32) for x in (T, 3*T+D, 17*T+6*D, 3*T+3*D))
def d4_orbit(tup):
    orb=set()
    for b in range(4):
        orb.add(tuple(tup[(i+b)%4] for i in range(4)))
        orb.add(tuple(tup[(-i+b)%4] for i in range(4)))
    return orb

groups={}
params={}
for T in range(32):
    for D in (0,8,16,24):
        tup=start(T,D)
        ms=tuple(sorted(tup))
        groups.setdefault(ms, set()).add(tup)
        params.setdefault(tup, []).append((T,D))
print(f"total params 128, distinct starting tuples: {len(params)}, distinct multisets: {len(groups)}")
bad=[]
for ms, tups in groups.items():
    # check all tuples in one D4 orbit
    t0=next(iter(tups))
    orb=d4_orbit(t0)
    if not tups.issubset(orb):
        bad.append((ms,tups,orb))
        print(f"BAD multiset {ms}: tuples {sorted(tups)} not subset of D4 orbit {sorted(orb)}")
print(f"bad multisets: {len(bad)}")
# Also check: for each multiset, how many tuples, orbit sizes
from collections import Counter
print("group size dist:", Counter(len(v) for v in groups.values()))
# Print a few groups
for ms,tups in list(groups.items())[:5]:
    print(ms, sorted(tups))
