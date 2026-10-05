#!/usr/bin/env python3
"""Finite FLOW-016/017 controls; no asymptotic or chain simulation.

Rational periodic window integration and packing witnesses are independent
of the maximal-operator proof. Character expressions are differentiated
by the maintained direct radial Laurent generator. Floating unitary
matching is a diagnostic with an explicit tolerance, not a certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from math import prod
from pathlib import Path
import platform

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment

from microscopic_noise_removal import add, multiply, power_trace, radial_generator


def signed_distance(a, b, n):
    return (a-b+Q(n, 2)) % n-Q(n, 2)


def window_indices(points, u, radius, n):
    return [j for j, a in enumerate(points)
            if abs(signed_distance(a, u, n)) < radius]


def exact_window_average(points, radius, n, value):
    """Integrate every constant window-count segment, not sampled origins."""
    events = sorted({Q(0), Q(n)} |
                    {(a+s*radius) % n for a in points for s in (-1, 1)})
    total = Q(0)
    for left, right in zip(events, events[1:]):
        total += (right-left)*value(window_indices(points, (left+right)/2,
                                                  radius, n))/n
    return total


def rational_packing_controls():
    cases = active = 0
    for n in (67, 131):
        for warped in (False, True):
            reference = [Q(j)+Q(j % 2, 8) if warped else Q(j)
                         for j in range(n)]
            gaps = [(reference[(j+1) % n]-reference[j]) % n
                    for j in range(n)]
            gap = min(gaps)
            # Any interval has at most length/gap+1 reference points.
            upper_density = 1/gap+Q(1, 2)
            for k in (0, 1, 3, 17, 40, 65, 100):
                if k >= n:
                    continue
                target = [Q(0) if j < k else reference[j] for j in range(n)]
                distances = [abs(signed_distance(a, b, n))
                             for a, b in zip(target, reference)]
                for radius in (1, 2, 3):
                    for p in (2, 4, 6):
                        averaged = exact_window_average(
                            target, radius, n,
                            lambda jj: sum((distances[j]**p for j in jj), Q(0)))
                        assert averaged == Q(2*radius, n)*sum(d**p for d in distances)
                        events = sorted({Q(0), Q(n)} |
                                        {(a+s*radius) % n for a in target
                                         for s in (-1, 1)})
                        for left, right in zip(events, events[1:]):
                            u = (left+right)/2
                            selected = window_indices(target, u, radius, n)
                            count = len(selected)
                            if count > 16*(radius+1)*upper_density:
                                r = Q(count)/(8*upper_density)
                                assert radius*2 < r <= Q(n, 8)
                                inside = sum(abs(signed_distance(reference[j], u, n))
                                             <= r for j in range(n))
                                assert inside <= Q(count, 4)
                                cost = sum(distances[j]**p for j in selected)
                                assert cost >= Q(3, 4*16**p)*count**(p+1)/upper_density**p
                                active += 1
                        cases += 1
    assert active > 0
    return {"exact_integral_cases": cases, "active_packing_segments": active}


def collapse_controls():
    records = []
    for p, order in ((2, 4), (2, 5), (4, 6), (4, 7)):
        for k in (9, 17, 33):
            n = k**order
            cost = Q(sum(j**p for j in range(k)), n)
            factorial = Q(prod(range(k-order+1, k+1)), n)
            assert cost <= Q(1, k**(order-p-1))
            assert factorial == prod((Q(k-j, k) for j in range(order)), start=Q(1))
            assert 0 < factorial < 1
            records.append({"p": p, "order": order, "K": k, "N": n,
                            "cost": str(cost), "factorial_mean": str(factorial)})
    # Boundary check: cost does not vanish at k=p+1 in this construction.
    for p in (2, 4):
        k = 33
        assert Q(sum(j**p for j in range(k)), k**(p+1)) > Q(1, 4*(p+1))
    return records


def conjugate_polynomial(pol):
    return {tuple(-j for j in key): c for key, c in pol.items()}


def character_controls():
    cases = 0
    for n in (4, 5, 6):
        p1 = power_trace(n, 1)
        x = multiply(p1, conjugate_polynomial(p1))
        unit = {(0,)*n: Q(1)}
        square = multiply(p1, p1)
        s2 = {key: Q(1, 2)*c for key, c in add(square, power_trace(n, 2)).items()}
        e2 = {key: Q(1, 2)*c for key, c in add(square, power_trace(n, 2), Q(-1)).items()}
        characters = [
            (add(x, unit, Q(-1)), Q(1)),
            (add(multiply(s2, conjugate_polynomial(s2)), x, Q(-1)), Q(2)+Q(2, n)),
            (add(add(multiply(s2, conjugate_polynomial(e2)), x, Q(-1)), unit), Q(2)),
            (add(add(multiply(e2, conjugate_polynomial(s2)), x, Q(-1)), unit), Q(2)),
            (add(multiply(e2, conjugate_polynomial(e2)), x, Q(-1)), Q(2)-Q(2, n))]
        for character, rate in characters:
            expected = {key: -rate*c for key, c in character.items()}
            assert radial_generator(n, character) == expected
            assert sum(character.values()) > 0  # dimension at the identity
            cases += 1
    return {"dimensions": [4, 5, 6], "exact_radial_character_cases": cases}


def radial_drift_controls():
    for r in range(1, 9):
        a, b, c = Q(16*r, 25), Q(100*r), Q(128*r*r)
        threshold = 800*r
        assert b <= a*threshold/4 and c <= a*threshold**2/4
        bound = b*threshold**(2*r-1)+c*threshold**(2*r-2)
        for x in (Q(0), Q(1, 10), Q(1), Q(5), Q(25), Q(threshold), Q(10*threshold)):
            drift = -a*x**(2*r)+b*x**(2*r-1)+c*x**(2*r-2)
            assert drift <= bound
    return {"orders": list(range(1, 9)), "arithmetic": "Fraction"}


def unitary_matching_controls():
    rng = np.random.default_rng(20261005)
    records = []
    for n in (3, 5, 9):
        for repeated in (False, True):
            angles = np.zeros(n) if repeated else np.linspace(-np.pi, np.pi, n, endpoint=False)
            w = np.diag(np.exp(1j*angles))
            raw = rng.normal(size=(n, n))+1j*rng.normal(size=(n, n))
            hermitian = (raw+raw.conj().T)/(2*np.sqrt(n))
            for scale in (0.001, 0.3, 2.0):
                v = expm(1j*scale*hermitian)@w
                a, b = np.angle(np.linalg.eigvals(v)), np.angle(np.linalg.eigvals(w))
                distances = np.abs((a[:, None]-b[None, :]+np.pi) % (2*np.pi)-np.pi)
                singular = np.linalg.svd(v-w, compute_uv=False)
                for p in (2, 4, 6):
                    rows, cols = linear_sum_assignment(distances**p)
                    left = float(np.sum(distances[rows, cols]**p))
                    right = float((np.pi/2)**p*np.sum(singular**p))
                    assert left <= right+2e-10*max(1, right)
                    records.append({"N": n, "repeated": repeated, "scale": scale,
                                    "p": p, "ratio": left/right if right else None})
        # Principal-log endpoint benchmark: equality for I versus -I.
        for p in (2, 4, 6):
            assert abs(n*np.pi**p-(np.pi/2)**p*n*2**p) < 1e-9
    return {"sampled_matching_cases": len(records), "endpoint_cases": 9,
            "tolerance": 2e-10, "records": records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = {"claim_ids": ["BGS-FLOW-016", "BGS-FLOW-017"],
              "software": {"Python": platform.python_version(), "NumPy": np.__version__},
              "seed": 20261005, "packing": rational_packing_controls(),
              "sharpness": collapse_controls(), "characters": character_controls(),
              "radial_drift": radial_drift_controls(), "unitary": unitary_matching_controls(),
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "non_claims": ["No universal transport, diffusion or chain theorem is certified by finite checks",
                             "No original enormous-step chain simulation",
                             "No deterministic noise removal or full BGS",
                             "No global novelty, external referee or analytic Lean certification"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({"packing": output["packing"], "character_cases": 15,
                      "collapse_cases": len(output["sharpness"]),
                      "matching_cases": output["unitary"]["sampled_matching_cases"]}))


if __name__ == "__main__":
    main()
