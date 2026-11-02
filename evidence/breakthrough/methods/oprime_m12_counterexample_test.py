"""O' at m=12 for the wave-4 O* counterexample only (no Fix_12 enumeration).

Criterion (same as oprime_m8_test.py, adapted m=8 -> m=12):
  H = 6I - C - C^T (circulant), D = det H_12 = 1536796800.
  For y in Fix_12 (H y == 0 mod D), w = (H*lift(y))/D (integer vector).
  V4 = ker(H mod 4); for v in V4, z = (H*v_lift)/4 (integer vector).
  pairNum(z,w) = z^T X w, Qnum(z) = z^T X z, X = adj(H).
  s = 1: y is in supp phihat  <=>  for every gamma in torsion,
  (2*Qnum(z_gamma) - pairNum(z_gamma,w)) == 0 (mod D).

Computational shortcuts (exact, no floats):
  * V4 is enumerated by the recurrence v_{i+1} = 2 v_i - v_{i-1} (mod 4)
    implied by Hv == 0 (mod 4), plus the two wrap-around equations;
    every candidate found is then checked directly against Hv % 4 == 0.
    (Brute force over 4^12 was not needed and not used.)
  * X*z is NOT computed via a 12x12 adjugate.  Instead t_z solves
    H t_z = D z over Q; since adj(H) H = D I, t_z = adj(H) z, and it
    must come out integral -- checked.  Then Qnum(z) = z . t_z.
  * Likewise pairNum(z,w) = z . t_w where H t_w = D w; the solve must
    return t_w == y (checked), so pairNum(z,w) = z . y, independently
    confirmed by the solve rather than assumed.

The two vectors y, y' are regenerated here from the mod-81 aff-bad
fiber (gluing_components.fix_mod / aff_perms / canon), and asserted
equal to the wave-4 reported tuples, so the test does not merely
copy the parent report.
"""
import sys, json
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from collections import defaultdict
import sympy as sp
from gluing_components import fix_mod, aff_perms, canon

m = 12
D = 1536796800
q = 81
M = D // q
inv = pow(M % q, -1, q)

def phi(t):
    return (t * M * inv) % D

def Hvec(v, mod=None):
    out = [6*v[i] - v[(i-1) % m] - v[(i+1) % m] for i in range(m)]
    if mod is not None:
        out = [x % mod for x in out]
    return out

# --- regenerate y, y' from mod 81 ---
vecs = fix_mod(m, q)
perms = aff_perms(m)
by = defaultdict(list)
for v in vecs:
    by[tuple(sorted(v))].append(v)
target = None
for s, vs in by.items():
    cs = {canon(v, perms, m) for v in vs}
    if len(cs) > 1:
        target = (s, vs); break
assert target is not None, "no aff-bad fiber mod 81"
s, vs = target
v1 = vs[0]
v2 = next(v for v in vs if canon(v, perms, m) != canon(v1, perms, m))
y = tuple(phi(t) for t in v1)
yp = tuple(phi(t) for t in v2)
print("sorted mod81:", s)
print("v1:", v1, "canon:", canon(v1, perms, m))
print("v2:", v2, "canon:", canon(v2, perms, m))
print("y :", y)
print("y':", yp)

# wave-4 reported tuples (for cross-check only; the test below uses y, y')
y_rep = (1366041600, 1366041600, 683020800, 1195286400, 341510400, 853776000,
         170755200, 170755200, 853776000, 341510400, 1195286400, 683020800)
yp_rep = (1366041600, 1195286400, 1195286400, 1366041600, 853776000, 683020800,
          170755200, 341510400, 341510400, 170755200, 683020800, 853776000)
print("matches wave-4 reported y :", y == y_rep)
print("matches wave-4 reported y':", yp == yp_rep)
assert y == y_rep and yp == yp_rep

for name, vec in (("y", y), ("y'", yp)):
    print(name, "H == 0 mod D:", all(x % D == 0 for x in Hvec(vec)),
          "| y mod 81 ok:", tuple(x % q for x in vec) in (v1, v2))
print("sorted(y) == sorted(y'):", tuple(sorted(y)) == tuple(sorted(yp)))
print("global canons distinct:", canon(y, perms, m) != canon(yp, perms, m))

# --- V4 by recurrence ---
V4 = []
for a in range(4):
    for b in range(4):
        seq = [a, b]
        for _ in range(10):
            seq.append((2*seq[-1] - seq[-2]) % 4)
        # seq now has v0..v11; wrap equations: i=11 and i=0
        if (2*seq[11] - seq[10]) % 4 != seq[0]:
            continue
        if (2*seq[0] - seq[11]) % 4 != seq[1]:
            continue
        # direct check
        assert all(x % 4 == 0 for x in Hvec(seq)), seq
        V4.append(tuple(seq))
print("V4 size:", len(V4))
print("V4:", V4)
tors = []
for v in V4:
    hv = Hvec(v)
    assert all(x % 4 == 0 for x in hv), (v, hv)
    tors.append(tuple(x // 4 for x in hv))
print("torsion z vectors:", tors)

# --- solve H t = D z (sympy, exact rationals) ---
Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6; Hsp[i, (i-1) % m] -= 1; Hsp[i, (i+1) % m] -= 1
print("det H (sympy) =", int(Hsp.det()), "== D:", int(Hsp.det()) == D)

def solve_H(rhs):
    t = Hsp.LUsolve(sp.Matrix(rhs))
    assert all(x.q == 1 for x in t), t  # integral
    t = tuple(int(x) for x in t)
    assert Hvec(t) == list(rhs) or all(
        (6*t[i] - t[(i-1) % m] - t[(i+1) % m]) == rhs[i] for i in range(m))
    return t

tors_t = [solve_H([D*z_i for z_i in z]) for z in tors]
tors_Q = [sum(z[i]*t[i] for i in range(m)) for z, t in zip(tors, tors_t)]
print("Qnum values:", tors_Q)
print("2*Qnum mod D:", [ (2*qv) % D for qv in tors_Q ])

def support_report(name, vec):
    Hy = Hvec(vec)
    assert all(x % D == 0 for x in Hy), name
    w = tuple(x // D for x in Hy)
    print(f"\n--- {name} ---")
    print("w =", w)
    tw = solve_H([D*wi for wi in w])
    print("solve H t = D w returns y:", tw == vec)
    assert tw == vec
    fails = []
    rows = []
    for vi, (v, z, qv) in enumerate(zip(V4, tors, tors_Q)):
        pair = sum(z[i]*vec[i] for i in range(m))  # = z . t_w
        val = (2*qv - pair) % D
        rows.append({"v": list(v), "z": list(z), "Qnum": qv,
                     "pairNum": pair, "val_mod_D": val, "pass": val == 0})
        if val != 0:
            fails.append(vi)
    for r in rows:
        print(f"  v={r['v']} z={r['z']} Q={r['Qnum']} pair={r['pairNum']} "
              f"(2Q-pair) mod D = {r['val_mod_D']} {'PASS' if r['pass'] else 'FAIL'}")
    print(f"{name}: {len(rows)-len(fails)}/{len(rows)} torsion conditions pass; "
          f"IN SUPPORT: {len(fails) == 0}")
    return {"name": name, "y": list(vec), "w": list(w),
            "n_torsion": len(rows), "n_pass": len(rows)-len(fails),
            "in_support": len(fails) == 0, "rows": rows}

out = {"m": m, "D": D, "V4_size": len(V4), "V4": [list(v) for v in V4],
       "tors_z": [list(z) for z in tors], "tors_Q": tors_Q,
       "y": support_report("y", y), "yp": support_report("y'", yp)}
json.dump(out, open("/home/hatch/workspace/bgs-breakthrough/methods/oprime_m12_counterexample_result.json", "w"), indent=1)
print("\nwritten oprime_m12_counterexample_result.json")
print("SUMMARY: y in support:", out["y"]["in_support"],
      "| y' in support:", out["yp"]["in_support"])
