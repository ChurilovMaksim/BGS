#!/usr/bin/env python3
"""Exact finite regression for weighted-Wiener stability of resonance variance.

The theorem is analytic; this script checks its algebraic inequality on exact
integer Fourier data and verifies the resulting orbit-sum lower bound using the
independent temporal-resonance implementation.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import extremal_resonance as er

Vec = tuple[int, int]
Fourier = er.Fourier


def l1(v: Vec) -> int:
    return abs(v[0]) + abs(v[1])


def coeff_abs_real(z: er.GI) -> int:
    assert z[1] == 0
    return abs(z[0])


def moment0(f: Fourier) -> int:
    return sum(l1(v) * coeff_abs_real(z) for v, z in f.items())


def momentA(a: er.Mat, f: Fourier) -> int:
    return sum(l1(er.mv(a, v)) * coeff_abs_real(z) for v, z in f.items())


def box(r: int) -> list[Vec]:
    return [(x, y) for x in range(-r, r + 1) for y in range(-r, r + 1)
            if (x, y) != (0, 0)]


def canonical(v: Vec) -> Vec:
    return min(v, er.neg(v))


def core_fourier(support: list[Vec], scale: int) -> Fourier:
    out: Fourier = {}
    for v in support:
        c = canonical(v)
        amp = scale * (1 + ((7 * abs(c[0]) + 11 * abs(c[1]) + 3 * (c[0] * c[1])) % 5))
        out[v] = (amp, 0)
    return out


def tail_fourier(r: int) -> Fourier:
    seeds = [(r + 1, 1), (r + 2, -1), (1, r + 2)]
    out: Fourier = {}
    for j, v in enumerate(seeds, start=1):
        amp = 1 if j != 2 else -1
        out[v] = (amp, 0)
        out[er.neg(v)] = (amp, 0)
    return out


def add_fourier(f: Fourier, g: Fourier) -> Fourier:
    return er.combine([(1, f), (1, g)])


def coeff_l1_real(f: Fourier) -> int:
    return sum(coeff_abs_real(z) for z in f.values())


def scale_fourier(f: Fourier, c: int) -> Fourier:
    return {k: (c*z[0], c*z[1]) for k, z in f.items()}


def one_case(a: er.Mat, rbox: int, initial_scale: int = 10) -> dict:
    support = box(rbox)
    u, v = er.witness(a, support, 1)
    av = er.mv(a, v)
    d = abs(er.det(u, av))
    tail = tail_fourier(rbox)
    scale = initial_scale
    while True:
        p = core_fourier(support, scale)
        P0, PA = moment0(p), momentA(a, p)
        R0, RA = moment0(tail), momentA(a, tail)
        D = d * coeff_abs_real(p[u]) * coeff_abs_real(p[v])
        E = P0*RA + R0*PA + R0*RA
        if E < D:
            break
        scale *= 2
        if scale > 1_000_000:
            raise RuntimeError('Could not enter certified stability radius')

    g = add_fourier(p, tail)
    hp = er.bracket(p, er.transport(a, p, 1))
    hg = er.bracket(g, er.transport(a, g, 1))
    diff = er.combine([(1, hg), (-1, hp)])
    assert coeff_l1_real(diff) <= E

    k = er.add(u, av)
    key = er.orbit_key(a, k)
    op = er.orbit_sums(a, hp)
    og = er.orbit_sums(a, hg)
    hp_orbit = coeff_abs_real(op.get(key, (0, 0)))
    hg_orbit = coeff_abs_real(og.get(key, (0, 0)))
    assert hp_orbit == D
    assert hg_orbit >= D - E > 0

    gamma_over_pi2 = sum(z[0]*z[0] + z[1]*z[1] for z in og.values())
    assert gamma_over_pi2 >= 2*(D-E)*(D-E)

    admitted = 0
    for m in range(0, 8):
        rm = scale_fourier(tail, m)
        r0, ra = moment0(rm), momentA(a, rm)
        Em = P0*ra + r0*PA + r0*ra
        if Em >= D:
            continue
        gm = add_fourier(p, rm)
        hm = er.bracket(gm, er.transport(a, gm, 1))
        om = er.orbit_sums(a, hm)
        val = coeff_abs_real(om.get(key, (0, 0)))
        assert val >= D - Em > 0
        admitted += 1

    return {
        'A': a, 'box_radius': rbox, 'scale': scale,
        'witness_u': u, 'witness_v': v, 'determinant': d,
        'P0': P0, 'PA': PA, 'R0': R0, 'RA': RA,
        'witness_budget_D': D, 'global_error_bound_E': E,
        'orbit_sum_abs_over_pi': hg_orbit,
        'gamma_lower_bound_over_pi2': 2*(D-E)*(D-E),
        'gamma_actual_over_pi2': gamma_over_pi2,
        'admitted_integer_tail_multipliers_checked': admitted,
    }


def main() -> None:
    rows = [one_case(a, 1 + (i % 3)) for i, a in enumerate(er.matrices()[:8])]
    assert len(rows) == 8
    assert all(r['global_error_bound_E'] < r['witness_budget_D'] for r in rows)
    print('PASS weighted-Wiener stability exact regressions:', len(rows))
    print('minimum certified margin:', min(r['witness_budget_D']-r['global_error_bound_E'] for r in rows))
    print('total admitted tail multipliers checked:', sum(r['admitted_integer_tail_multipliers_checked'] for r in rows))


if __name__ == '__main__':
    main()
