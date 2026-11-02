import json
def load(m):
    with open(f"wave36_2part_m{m}.json") as f: return json.load(f)
d32, d64, d128 = load(32), load(64), load(128)
# map: orbit canon -> fiber index at level m
def orbit_to_fiber(d):
    mp = {}
    for fi, f in enumerate(d["fibers"]):
        for c in f["own_orbit_canons"]:
            mp[tuple(c)] = fi
    return mp
o32, o64 = orbit_to_fiber(d32), orbit_to_fiber(d64)
print("== m=64 fibers: their reduced (m=32) orbit -> which m=32 split fiber?")
for fi, f in enumerate(d64["fibers"]):
    rc = [tuple(c) for c in f["reduced_orbit_canons"]]
    print(f"  m64 fiber {fi} size={f['size']} orbits={f['n_orbits']} kind={f['kind']} "
          f"reduced_in_m32_split={[o32.get(c) for c in rc]}")
print("== m=128 fibers: reduced (m=64) orbits -> which m=64 split fiber?")
for fi, f in enumerate(d128["fibers"]):
    rc = [tuple(c) for c in f["reduced_orbit_canons"]]
    print(f"  m128 fiber {fi} size={f['size']} orbits={f['n_orbits']} kind={f['kind']} "
          f"reduced_in_m64_split={[o64.get(c) for c in rc]}")
print("== m=128 OLD fibers: do their reduced canon pairs equal an m=64 fiber's own canon set?")
for fi, f in enumerate(d128["fibers"]):
    if f["kind"] != "OLD": continue
    rc = {tuple(c) for c in f["reduced_orbit_canons"]}
    match = [gj for gj, g in enumerate(d64["fibers"]) if {tuple(c) for c in g["own_orbit_canons"]} == rc]
    print(f"  m128 OLD fiber {fi} size={f['size']} -> m64 fiber {match}")
