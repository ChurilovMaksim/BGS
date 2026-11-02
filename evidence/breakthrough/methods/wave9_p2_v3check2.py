def d8_orbit(tup):
    n=len(tup)
    orb=set()
    for b in range(n):
        orb.add(tuple(tup[(i+b)%n] for i in range(n)))
        orb.add(tuple(tup[(-i+b)%n] for i in range(n)))
    return orb
c=[1,3,17,35,1,35,17,3]
e=[0,1,6,35,12,37,18,7]
groups={}
for T in range(64):
    for D in range(0,64,8):
        block=tuple((T*c[s]+D*e[s])%64 for s in range(8))
        ms=tuple(sorted(block))
        groups.setdefault(ms, set()).add(block)
print(f"multisets {len(groups)}")
bad=0
for ms, blocks in groups.items():
    b0=next(iter(blocks))
    orb=d8_orbit(b0)
    if not blocks.issubset(orb):
        bad+=1
        print(f"BAD {ms}: {len(blocks)} blocks, orbit size {len(orb)}")
        print(" blocks:", sorted(blocks)[:4])
print(f"bad (not D8): {bad}")
