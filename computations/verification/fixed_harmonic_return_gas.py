#!/usr/bin/env python3
"""Finite independent controls for the fixed-harmonic return gas.

Graph partitions and Weyl phases are exact at the stated finite parameters.
Matrix and Bessel evaluations use floating arithmetic, not interval certificates.
No finite calculation certifies an asymptotic limit or research priority.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
import math
from pathlib import Path
import platform
import time

import mpmath as mp
import numpy as np

from even_period_spin_resonance import recurrence


def penrose_partition_controls():
    """All simple labeled graphs on at most six vertices, with root zero."""
    rows = []
    for n in range(2, 7):
        edges = list(combinations(range(n), 2))
        edge_index = {e: i for i, e in enumerate(edges)}
        trees = Counter()
        extra_counts = {}
        connected = 0
        for graph in range(1 << len(edges)):
            adjacency = [[] for _ in range(n)]
            for e, (i, j) in enumerate(edges):
                if (graph >> e) & 1:
                    adjacency[i].append(j)
                    adjacency[j].append(i)
            levels = [-1]*n
            levels[0] = 0
            queue = [0]
            for i in queue:
                for j in adjacency[i]:
                    if levels[j] < 0:
                        levels[j] = levels[i]+1
                        queue.append(j)
            if len(queue) != n:
                continue
            connected += 1
            parents = [-1]+[
                min(j for j in adjacency[i] if levels[j] == levels[i]-1)
                for i in range(1, n)]
            tree = sum(1 << edge_index[tuple(sorted((i, parents[i])))]
                       for i in range(1, n))
            closure = tree
            for e, (i, j) in enumerate(edges):
                if levels[i] == levels[j]:
                    closure |= 1 << e
                elif abs(levels[i]-levels[j]) == 1:
                    lower, upper = (i, j) if levels[i] < levels[j] else (j, i)
                    if lower >= parents[upper]:
                        closure |= 1 << e
            assert tree & graph == tree and graph & closure == graph
            trees[tree] += 1
            extra_counts[tree] = (closure ^ tree).bit_count()
        assert len(trees) == n**(n-2)
        assert all(count == 2**extra_counts[tree] for tree, count in trees.items())
        rows.append({"vertices": n, "all_graphs": 2**len(edges),
                     "connected_graphs": connected, "tree_intervals": len(trees)})
    return rows


def word_phase_controls():
    rng = np.random.default_rng(197346)
    rows = []
    for k in (6, 10, 14, 18):
        b = recurrence(k)
        n = b[k//2]
        orbit, v = [], (1, 0)
        for _ in range(k):
            orbit.append(v)
            v = ((3*v[0]+4*v[1]) % n, (2*v[0]+3*v[1]) % n)
        half = pow(2, -1, n)
        for a in (1, 2, 3):
            if math.gcd(a, n) != 1:
                continue
            checks = central_checks = 0
            for r in range(1, 7):
                h = np.array([[1 if nu <= mu else -1 for mu in range(r)]
                              for nu in range(r)], dtype=np.int64)
                for sample in range(60):
                    indices = rng.integers(-2, 3, size=(r, k))
                    if sample % 2 == 0:
                        preimage = rng.integers(-1, 2, size=k)
                        c = np.roll(preimage, 1)+np.roll(preimage, -1)-6*preimage
                        c += np.where(np.arange(k) % 2 == 0,
                                      int(rng.integers(0, 16)), int(rng.integers(0, 2)))
                        indices[-1] = c-indices[:-1].sum(axis=0)
                    total, phase = [0, 0], 0
                    for row in indices:
                        for value, vector in zip(row, orbit):
                            w = [int(value)*a*q for q in vector]
                            phase += half*(total[0]*w[1]-total[1]*w[0])
                            total = [(p+q) % n for p, q in zip(total, w)]
                    actual_c = indices.sum(axis=0)
                    expected_total = [sum(int(actual_c[j])*a*orbit[j][d]
                                          for j in range(k)) % n for d in (0, 1)]
                    bilinear = indices.T @ h @ indices
                    direct = compact = 0
                    for i in range(k):
                        for j in range(i+1, k):
                            distance = j-i
                            short_b = (b[distance] if distance < k//2 else
                                       -b[k-distance] if distance > k//2 else 0)
                            direct += a*a*b[distance]*int(bilinear[i, j])
                            compact += a*a*short_b*int(bilinear[i, j])
                    assert total == expected_total
                    assert (phase-direct) % n == (phase-compact) % n == 0
                    if sample % 2 == 0:
                        assert total == [0, 0]
                        central_checks += 1
                    checks += 1
            rows.append({"K": k, "N": n, "harmonic": a,
                         "seeded_ordered_word_checks": checks,
                         "constructed_central_words": central_checks})
    return {"seed": 197346, "rows": rows}


def replica_charge_controls():
    """Exhaust all two-charge species pairs through 12 replicas."""
    rows = []
    for r in range(1, 13):
        h = np.array([[1 if i <= j else -1 for j in range(r)] for i in range(r)])
        unit = np.eye(r, dtype=np.int64)
        vectors = np.array([unit[i]-unit[j] for i in range(r)
                            for j in range(r) if i != j], dtype=np.int64).reshape(-1, r)
        pairings = vectors @ h @ vectors.T
        values, counts = np.unique(pairings, return_counts=True)
        histogram = dict(zip(values.tolist(), counts.tolist()))
        expected = r*r*(r*r-1)//3
        assert set(histogram).issubset({-2, 0, 2})
        assert histogram.get(-2, 0)+histogram.get(2, 0) == expected
        assert histogram.get(-2, 0) == histogram.get(2, 0)
        rows.append({"replicas": r, "species": len(vectors),
                     "complete_pairings": pairings.size,
                     "nonzero_pairings": expected, "histogram": histogram})
    return rows


def bessel_controls():
    """High-precision checks of explicit constants; not interval validation."""
    rows = []
    lam = 3+2*mp.sqrt(2)
    for a in (1, 2, 7):
        c = 1+4*mp.pi*a*a/(lam-1)
        radius = 1/(32*mp.sqrt(c))
        for r in (1, 2, 3, 7, 31, 100):
            delta = radius/r
            s = r*delta
            denominator = (1-delta**2*mp.exp(delta**2))**r
            majorant = 2*mp.e**2*s*s*mp.exp(mp.e**2*s*s)/denominator
            assert majorant < 16*s*s
            assert c*majorant < 1
            tau = 2*(c-1)*s*s
            z = s*mp.exp(tau+s*s*(1+mp.exp(2*tau)))
            assert z < 2*s
            loss = 160*c*s*s+1280*s**6
            assert loss < mp.mpf("0.5")
            rows.append({"harmonic": a, "replicas": r,
                         "allowed_r_epsilon": float(radius),
                         "tree_criterion_value": float(c*majorant),
                         "relative_exponent_loss_bound": float(loss)})
    return rows


def quartic_coefficient_experiment():
    """Independent full physical matrices test the computed fourth coefficient.

    At K=10 every nonzero aggregate has l1 norm at least five, so it cannot
    change the full-space coefficient of epsilon^4. Symmetrization cancels
    odd powers. At finite N the odd trace alone has a noncentral projection
    correction; dividing that correction by epsilon^4 would corrupt this test.
    Both physical parity blocks are therefore combined for the coefficient
    test, and the odd trace is also reported. No asymptotic extrapolation
    silently discards its finite-N correction.
    """
    k = 10
    n = recurrence(k)[k//2]
    dim = (n-1)//2
    x = np.arange(1, dim+1)
    inv4 = pow(4, -1, n)
    plus = ((3*x[:, None]**2-2*x[:, None]*x[None, :]+3*x[None, :]**2)*inv4) % n
    minus = ((3*x[:, None]**2+2*x[:, None]*x[None, :]+3*x[None, :]**2)*inv4) % n
    u0 = (np.exp(2j*np.pi*plus/n)-np.exp(2j*np.pi*minus/n))/math.sqrt(n)
    even_u0 = np.empty((dim+1, dim+1), dtype=complex)
    even_u0[1:, 1:] = (np.exp(2j*np.pi*plus/n)+np.exp(2j*np.pi*minus/n))/math.sqrt(n)
    axis = math.sqrt(2/n)*np.exp(2j*np.pi*((3*x*x*inv4) % n)/n)
    even_u0[0, 1:] = even_u0[1:, 0] = axis
    even_u0[0, 0] = 1/math.sqrt(n)
    scalar = np.trace(np.linalg.matrix_power(u0, k))/dim
    gauge = np.exp(-1j*np.angle(scalar)/k)
    u0 *= gauge
    even_u0 *= gauge
    assert np.max(abs(np.linalg.matrix_power(u0, k)-np.eye(dim))) < 2e-12
    assert np.max(abs(np.linalg.matrix_power(even_u0, k)-np.eye(dim+1))) < 2e-12
    rows = []
    b = recurrence(k//2)
    for a in (1, 2):
        sa = sum(1-mp.cos(4*mp.pi*a*a*mp.mpf(b[k//2-ell])/n)
                 for ell in range(1, k//2))
        for delta in (0.08, 0.04, 0.02):
            traces, odd_traces = [], []
            for sign in (-1, 1):
                kick = np.exp(2j*sign*delta*np.cos(2*np.pi*a*x/n))
                echo = np.linalg.matrix_power(kick[:, None]*u0, k)
                even_kick = np.r_[np.exp(2j*sign*delta), kick]
                even_echo = np.linalg.matrix_power(even_kick[:, None]*even_u0, k)
                power = np.eye(dim, dtype=complex)
                even_power = np.eye(dim+1, dtype=complex)
                moments, odd_moments = [], []
                for r in range(1, 6):
                    power = power @ echo
                    even_power = even_power @ even_echo
                    odd_moments.append(np.trace(power)/dim)
                    moments.append((np.trace(power)+np.trace(even_power))/n)
                traces.append(moments)
                odd_traces.append(odd_moments)
            for r in range(1, 6):
                trace = complex((traces[0][r-1]+traces[1][r-1])/2)
                odd_trace = complex((odd_traces[0][r-1]+odd_traces[1][r-1])/2)
                predicted = -mp.mpf(r)**4/4-r*r*(r*r-1)*sa/3
                estimated = (np.log(trace)/k+r*r*delta**2)/delta**4
                rows.append({"K": k, "N": n, "harmonic": a, "replicas": r,
                             "epsilon": delta,
                             "symmetrized_full_trace": [trace.real, trace.imag],
                             "symmetrized_odd_trace": [odd_trace.real, odd_trace.imag],
                             "predicted_fourth_coefficient": float(predicted),
                             "estimated_fourth_coefficient": [float(estimated.real), float(estimated.imag)],
                             "absolute_coefficient_error": float(abs(estimated-complex(predicted)))})
    for a in (1, 2):
        for r in range(1, 6):
            case = [v for v in rows if v["harmonic"] == a and v["replicas"] == r]
            assert case[2]["absolute_coefficient_error"] < 0.4*case[1]["absolute_coefficient_error"], case
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    mp.mp.dps = 70
    start = time.monotonic()
    lam = 3+2*mp.sqrt(2)
    sa = sum(1-mp.cos(4*mp.pi*lam**(-ell)) for ell in range(1, 51))
    result = {
        "scope": "Bounded exact checks and finite floating controls; not a BGS or priority certificate.",
        "python": platform.python_version(), "numpy": np.__version__, "mpmath": mp.__version__,
        "Penrose_partition": penrose_partition_controls(),
        "word_phases": word_phase_controls(),
        "replica_charges": replica_charge_controls(),
        "Bessel_constant_checks": bessel_controls(),
        "physical_quartic_controls": quartic_coefficient_experiment(),
        "S_harmonic_1": mp.nstr(sa, 45),
        "S_series_tail_bound": mp.nstr(8*mp.pi**2*lam**(-102)/(1-lam**(-2)), 12),
    }
    result["elapsed_seconds"] = time.monotonic()-start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "elapsed_seconds": result["elapsed_seconds"],
                      "ordered_word_checks": sum(r["seeded_ordered_word_checks"] for r in result["word_phases"]["rows"]),
                      "all_graphs": sum(r["all_graphs"] for r in result["Penrose_partition"])}))


if __name__ == "__main__":
    main()
