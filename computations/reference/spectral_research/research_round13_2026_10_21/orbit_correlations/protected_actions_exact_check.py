"""Finite exact check of the sixteen-point action table.

This does not evaluate U_N or prove an N-asymptotic statement. All values
are rational; every protected point is enumerated, including every
possible starting point on its primitive orbit.
"""

from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json


def linear(z):
    q, p = z
    return 3*q-4*p, -2*q+3*p


def torus(z):
    return tuple(v % 1 for v in z)


def bare_phase(q_next, q):
    return -(3*q_next*q_next - 2*q_next*q + 3*q*q)/8


def kick_value(q):
    assert q % 1 in (Q(0), Q(1, 2))
    return Q(9, 10) if q % 1 == 0 else Q(-11, 10)


def point_text(z):
    return [str(c) for c in z]


points = tuple(product((Q(0), Q(1, 2)), (Q(j, 8) for j in range(8))))
assert len(set(points)) == 16
assert all(torus(linear(z)) in points for z in points)
assert all(torus(linear(linear(z))) == z for z in points)

rows = []
for z in points:
    d = 1 if torus(linear(z)) == z else 2
    cur = z
    action = Q(0)
    kick = Q(0)
    lifted = [point_text(z)]
    for _ in range(d):
        nxt = linear(cur)
        action += bare_phase(nxt[0], cur[0])
        kick += kick_value(nxt[0])
        cur = nxt
        lifted.append(point_text(cur))
    winding = tuple(cur[j]-z[j] for j in range(2))
    assert all(x.denominator == 1 for x in winding)
    half_action = action-winding[1]*(z[0]+winding[0]/2)
    reduced = action-winding[1]*z[0]
    parity = int(winding[0]*winding[1]) % 2
    # For odd N=2s+1, combine (-1)^(n_q n_p) with the half action.
    # The resulting phase differs from N*reduced by an integer:
    # N*(half_action-reduced)+parity/2.
    for odd in (1, 3, 5, 7):
        phase_difference = odd*(half_action-reduced)+Q(parity, 2)
        assert phase_difference.denominator == 1
    rows.append({
        "point": point_text(z), "primitive_period": d,
        "lifted_path": lifted, "winding": point_text(winding),
        "half_action": str(half_action), "odd_character_parity": parity,
        "reduced_action": str(reduced), "B_mod_1": str(reduced % 1),
        "C": str(kick),
    })

by_point = {tuple(row["point"]): row for row in rows}
for z in points:
    own = by_point[tuple(point_text(z))]
    nxt = by_point[tuple(point_text(torus(linear(z))))]
    assert (own["B_mod_1"], own["C"]) == (nxt["B_mod_1"], nxt["C"])

visited = set()
cycles = []
for z in points:
    if z in visited:
        continue
    orbit = [z]
    nxt = torus(linear(z))
    if nxt != z:
        orbit.append(nxt)
    visited.update(orbit)
    row = by_point[tuple(point_text(z))]
    cycles.append({
        "orbit": [point_text(p) for p in orbit],
        "d": len(orbit), "B_mod_1": row["B_mod_1"], "C": row["C"],
    })

assert len(cycles) == 10
assert sum(c["d"] == 1 for c in cycles) == 4
assert sum(c["d"] == 2 for c in cycles) == 6
assert sum(c["d"] for c in cycles) == 16

expected = {
    ("0", "0"): ("0", "9/10"),
    ("0", "1/2"): ("1/2", "9/10"),
    ("1/2", "0"): ("3/4", "-11/10"),
    ("1/2", "1/2"): ("3/4", "-11/10"),
    ("0", "1/8"): ("13/16", "-1/5"),
    ("0", "7/8"): ("13/16", "-1/5"),
    ("0", "3/8"): ("5/16", "-1/5"),
    ("0", "5/8"): ("5/16", "-1/5"),
    ("0", "1/4"): ("1/4", "9/5"),
    ("1/2", "1/4"): ("3/4", "-11/5"),
}
for key, val in expected.items():
    row = by_point[key]
    assert (row["B_mod_1"], row["C"]) == val

assert (Q(48612+49788, 16)-Q(24, 16))/125 == Q(12297, 250)

result = {
    "scope": "Exhaustive exact rational enumeration of 16 protected points; no quantum asymptotic experiment",
    "point_count": 16, "fixed_points": 4, "primitive_two_cycles": 6,
    "all_starting_points_checked": True,
    "cycles": cycles, "all_point_rows": rows,
    "one_step_liminf_coefficient_times_pi_tau": "12297/250",
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")
print(json.dumps({"output": str(out), "sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
                  "point_count": 16, "cycles": 10, "arithmetic": "rational exact"}))
