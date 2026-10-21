#!/usr/bin/env python3
"""Independent finite rational check of protected primitive cycles.

This reproduces root's recorded JSON exactly as mathematical data.
It proves only the finite action table, not a spectral limit.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def linear(z):
    q, p = z
    return (3*q - 4*p, -2*q + 3*p)


def torus(z):
    return tuple(t % 1 for t in z)


def action_edge(Q, q):
    return -(3*Q*Q - 2*Q*q + 3*q*q)/8


def protected_value(z):
    q, p = torus(z)
    if q == 0:
        return F(9, 10)
    if q == F(1, 2):
        return -F(11, 10)
    raise AssertionError("Point is outside the protected lines.")


def enumerate_records():
    points = {(q, F(j, 8)) for q in (F(0), F(1, 2))
              for j in range(8)}
    assert len(points) == 16
    assert {torus(linear(z)) for z in points} == points
    assert all(torus(linear(linear(z))) == z for z in points)
    remaining = set(points)
    records = []
    while remaining:
        start = min(remaining)
        orbit = [start]
        z = torus(linear(start))
        while z != start:
            assert z in remaining and z not in orbit
            orbit.append(z)
            z = torus(linear(z))
        remaining.difference_update(orbit)

        lifted = start
        action = F(0)
        value = F(0)
        for _ in orbit:
            nxt = linear(lifted)
            action += action_edge(nxt[0], lifted[0])
            value += protected_value(nxt)
            lifted = nxt
        deck = (lifted[0]-start[0], lifted[1]-start[1])
        assert all(t.denominator == 1 for t in deck)
        nq, np = deck
        bare = action - np*(start[0] + nq/2)
        parity = int(nq*np) % 2
        odd_effective = (bare + F(parity, 2)) % 1
        assert odd_effective == (action - np*start[0]) % 1

        records.append({
            "period":len(orbit),
            "orbit":[[str(q),str(p)] for q,p in orbit],
            "deck":[str(t) for t in deck],
            "action_bare_mod1":str(bare % 1),
            "odd_effective_action_mod1":str(odd_effective),
            "sum_a":str(value),
            "cocycle_parity":parity,
        })
    assert len(records) == 10
    assert sum(r["period"] for r in records) == 16
    assert sum(r["period"] == 1 for r in records) == 4
    return records


def main():
    target = Path(__file__).with_suffix(".json")
    raw = target.read_bytes()
    assert json.loads(raw) == enumerate_records()
    print(json.dumps({
        "finite_exact_check": "passed",
        "protected_points":16,
        "fixed_points":4,
        "primitive_two_cycles":6,
        "recorded_json_sha256":hashlib.sha256(raw).hexdigest(),
        "spectral_asymptotic_established_by_check":False,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
