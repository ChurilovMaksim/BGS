import json
def load(m):
    with open(f"wave36_2part_m{m}.json") as f: return json.load(f)
d128, d256 = load(128), load(256)
o128 = {}
for fi, f in enumerate(d128["fibers"]):
    for c in f["own_orbit_canons"]:
        o128[tuple(c)] = fi
print("== m=256 OLD fibers -> m=128 fibers (via reduced orbits):")
for fi, f in enumerate(d256["fibers"]):
    if f["kind"] != "OLD": continue
    rc = [tuple(c) for c in f["reduced_orbit_canons"]]
    src = sorted({o128.get(c) for c in rc})
    print(f"  m256 OLD fiber {fi} size={f['size']} orbits={f['n_orbits']} "
          f"red_orbits={f['n_reduced_orbits']} <- m128 fibers {src} "
          f"(sizes {[d128['fibers'][s]['size'] for s in src if s is not None]}, "
          f"orbits {[d128['fibers'][s]['n_orbits'] for s in src if s is not None]})")
print("== m=256 NEW fibers: reduced orbits in m=128 split fibers?")
for fi, f in enumerate(d256["fibers"]):
    if f["kind"] != "NEW": continue
    rc = [tuple(c) for c in f["reduced_orbit_canons"]]
    print(f"  m256 NEW fiber {fi} size={f['size']} orbits={f['n_orbits']} "
          f"reduced_in_m128_split={[o128.get(c) for c in rc]}")
print("== m=128 fibers and their fate at m=256:")
lifted = set()
for f in d256["fibers"]:
    if f["kind"] == "OLD":
        for c in f["reduced_orbit_canons"]:
            lifted.add(o128.get(tuple(c)))
for fi, f in enumerate(d128["fibers"]):
    print(f"  m128 fiber {fi} size={f['size']} orbits={f['n_orbits']} "
          f"kind_at_128={f['kind']} -> {'LIFTS (on-support)' if fi in lifted else 'FAILS (preimage unsupported or non-split)'}")
