def d4_orbit(tup):
    orb=set()
    for b in range(4):
        orb.add(tuple(tup[(i+b)%4] for i in range(4)))
        orb.add(tuple(tup[(-i+b)%4] for i in range(4)))
    return orb
# c_s, e_s mod64 for s=0..7
c=[1,3,17,35,1,35,17,3]
e=[0,1,6,35,12,37,18,7]
groups={}
params={}
for T in range(64):
    for D in range(0,64,8):
        block=tuple((T*c[s]+D*e[s])%64 for s in range(8))
        S=tuple((block[r]+block[r+4])%64 for r in range(4))
        ms=tuple(sorted(block))
        groups.setdefault(ms, set()).add(S)
        params.setdefault(block, []).append((T,D))
print(f"params 512, distinct blocks {len(params)}, distinct multisets {len(groups)}")
bad=[]
for ms, Ss in groups.items():
    s0=next(iter(Ss))
    orb=d4_orbit(s0)
    if not Ss.issubset(orb):
        bad.append((ms,Ss))
        print(f"BAD {ms}: S tuples {sorted(Ss)} not in D4 orbit of {s0}: {sorted(orb)}")
print(f"bad multisets: {len(bad)}")
from collections import Counter
print("S-group size dist:", Counter(len(v) for v in groups.values()))
