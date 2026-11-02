"""Component-level Gamma-bad fibers for m=9 and m=12, plus P_w lifts at m=12.

Gamma = dihedral perms p[j] = (j+k) % m or (k-j) % m, acting by (p.y)_j = y_{p[j]}.
A fiber = sorted(y) class. A fiber is Gamma-bad if it contains >1 Gamma-orbit
(lex-min canon over Gamma). For m=12, each component Gamma-bad fiber is lifted
to a global pair (other components 0, CRT phi) and P_w is tested globally:
sorted(w) equal + different global Gamma canons => P_w KILLED.
"""
import json, sys
from collections import defaultdict
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from gluing_components import fix_mod

def gamma_perms(m):
    perms = []
    for k in range(m):
        perms.append([(j + k) % m for j in range(m)])
        perms.append([(k - j) % m for j in range(m)])
    # dedup preserving order
    seen, out = set(), []
    for p in perms:
        t = tuple(p)
        if t not in seen:
            seen.add(t); out.append(p)
    return out

def gamma_canon(y, perms):
    best = None
    for p in perms:
        t = tuple(y[p[j]] for j in range(len(y)))
        if best is None or t < best:
            best = t
    return best

def analyze_component(m, q):
    vecs = fix_mod(m, q)
    perms = gamma_perms(m)
    by = defaultdict(list)
    for v in vecs:
        by[tuple(sorted(v))].append(v)
    bad = []
    for s, vs in by.items():
        canons = {}
        for v in vs:
            canons.setdefault(gamma_canon(v, perms), []).append(v)
        if len(canons) > 1:
            bad.append({"sorted": list(s), "n_vecs": len(vs),
                        "n_gamma_orbits": len(canons),
                        "orbit_sizes": sorted(len(vs2) for vs2 in canons.values()),
                        "examples": [list(canons[c][0]) for c in sorted(canons)][:4]})
    return {"m": m, "q": q, "n_fix": len(vecs), "n_fibers": len(by),
            "n_gamma_bad": len(bad), "bad": bad}

def check_H(vec, D, m):
    return all((6*vec[i] - vec[(i-1) % m] - vec[(i+1) % m]) % D == 0 for i in range(m))

def w_of(vec, D, m):
    w = []
    for i in range(m):
        num = 6*vec[i] - vec[(i-1) % m] - vec[(i+1) % m]
        assert num % D == 0, (vec, i, num)
        w.append(num // D)
    return tuple(w)

def main():
    results = {}
    for m, qs in [(9, [4, 49, 39601]), (12, [128, 81, 25, 49, 121])]:
        for q in qs:
            r = analyze_component(m, q)
            results[f"m{m}_q{q}"] = r
            print(f"m={m} q={q} n_fix={r['n_fix']} fibers={r['n_fibers']} "
                  f"gamma_bad={r['n_gamma_bad']}", flush=True)
            for b in r["bad"]:
                print(f"   bad sorted={b['sorted']} vecs={b['n_vecs']} "
                      f"orbits={b['n_gamma_orbits']} sizes={b['orbit_sizes']}", flush=True)
    # --- m=12 lifts: for every component gamma-bad fiber, lift one pair
    # from each pair of distinct gamma-orbits and test P_w globally. ---
    m, D = 12, 1536796800
    perms = gamma_perms(m)
    lift_tests = []
    kills = []
    for q in [128, 81, 25, 49, 121]:
        r = results[f"m12_q{q}"]
        vecs = fix_mod(m, q)
        by = defaultdict(list)
        for v in vecs:
            by[tuple(sorted(v))].append(v)
        M = D // q
        inv = pow(M % q, -1, q)
        def phi(t):
            return (t * M * inv) % D
        for b in r["bad"]:
            s = tuple(b["sorted"])
            vs = by[s]
            canons = {}
            for v in vs:
                canons.setdefault(gamma_canon(v, perms), []).append(v)
            canon_list = sorted(canons)
            # test every pair of distinct gamma-orbits (first example each)
            for i in range(len(canon_list)):
                for j in range(i+1, len(canon_list)):
                    v1, v2 = canons[canon_list[i]][0], canons[canon_list[j]][0]
                    y1 = tuple(phi(t) for t in v1)
                    y2 = tuple(phi(t) for t in v2)
                    assert check_H(y1, D, m) and check_H(y2, D, m)
                    assert tuple(sorted(y1)) == tuple(sorted(y2))
                    gc1, gc2 = gamma_canon(y1, perms), gamma_canon(y2, perms)
                    assert gc1 != gc2, "lifted pair should stay gamma-distinct"
                    ws1, ws2 = tuple(sorted(w_of(y1, D, m))), tuple(sorted(w_of(y2, D, m)))
                    t = {"q": q, "sorted_mod_q": list(s),
                         "v1": list(v1), "v2": list(v2),
                         "y1": list(y1), "y2": list(y2),
                         "w_sorted_y1": list(ws1), "w_sorted_y2": list(ws2),
                         "w_sorted_equal": ws1 == ws2,
                         "gamma_canons_distinct": gc1 != gc2}
                    lift_tests.append(t)
                    if ws1 == ws2:
                        kills.append(t)
                    print(f"  lift q={q} sorted={list(s)[:6]}... w_eq={ws1 == ws2} "
                          f"ws1={list(ws1)} ws2={list(ws2)}", flush=True)
    out = {"components": results, "lift_tests": lift_tests, "kills": kills,
           "n_lift_tests": len(lift_tests), "n_kills": len(kills)}
    json.dump(out, open('/home/hatch/workspace/bgs-breakthrough/methods/pw_m12_components_result.json', 'w'), indent=1)
    print(f"LIFT TESTS: {len(lift_tests)} pairs, P_w KILLS: {len(kills)}")

if __name__ == "__main__":
    main()
