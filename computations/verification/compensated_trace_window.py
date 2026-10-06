#!/usr/bin/env python3
"""Finite unitary controls for the compensated Heisenberg-window corollary.

These test telescoping and both trace normalizations, not the smooth-symbol
normal form or the limiting BGS conjecture. Floating-point errors have a
separate comparison tolerance; there is no interval-certification claim.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np


def cluster_window_checks(rng: np.random.Generator) -> list[dict]:
    """Check the pair decomposition and its two independently bounded parts."""
    rows = []
    for period, multiplicity in ((3, 40), (5, 31), (11, 17)):
        dimension = period * multiplicity
        roots = np.arange(period)[:, None] / period
        for mode in ('exact', 'random', 'alternating', 'boundary'):
            eta = (0.0 if mode == 'exact' else
                   1 / (4 * period) if mode == 'boundary' else 0.03 / dimension)
            if mode in ('alternating', 'boundary'):
                offsets = eta * np.broadcast_to(
                    np.where(np.arange(multiplicity) % 2, 1.0, -1.0),
                    (period, multiplicity))
            else:
                offsets = rng.uniform(-eta, eta, (period, multiplicity))
            phases = roots + offsets
            assert eta <= 1 / (4 * period)
            for start, end in ((dimension // 4, dimension),
                               (-dimension, -dimension // 3), (0, 0)):
                times = np.arange(start, end + 1)
                block_traces = np.exp(
                    2j * np.pi * times[:, None, None] * phases[None, :, :]
                ).sum(axis=2)
                total = np.mean(abs(block_traces.sum(axis=1)) ** 2) / dimension
                within = np.mean((abs(block_traces) ** 2).sum(axis=1)) / dimension
                between = total - within
                same_bound = 8 * np.pi**2 * multiplicity * max(abs(times))**2 * eta**2
                harmonic = sum(1 / h for h in range(1, (period - 1) // 2 + 1))
                cross_bound = 2 * dimension * harmonic / len(times)
                tolerance = 1e-9
                assert within <= multiplicity + tolerance
                assert multiplicity - within <= same_bound + tolerance
                assert abs(between) <= cross_bound + tolerance
                assert abs(total - multiplicity) <= same_bound + cross_bound + tolerance
                rows.append({'period': period, 'multiplicity': multiplicity,
                             'mode': mode, 'phase_radius': eta,
                             'first_time': int(start), 'last_time': int(end),
                             'mean_form_factor': float(total),
                             'same_cluster_defect': float(multiplicity - within),
                             'same_cluster_bound': float(same_bound),
                             'cross_cluster_contribution': float(between),
                             'cross_cluster_bound': float(cross_bound)})
    return rows


def report() -> dict:
    rng = np.random.default_rng(20260905)
    rows = []
    for period, multiplicity in ((3, 2), (5, 3)):
        d = period*multiplicity
        angles = np.repeat(np.arange(period), multiplicity)
        u0 = np.diag(np.exp(2j*np.pi*angles/period))
        raw = rng.standard_normal((d,d))+1j*rng.standard_normal((d,d))
        h = (raw+raw.conj().T)/2
        vals, basis = np.linalg.eigh(h)
        vals /= max(abs(vals))
        for amplitude in (0.0001, 0.02):
            u = ((basis*np.exp(1j*amplitude*vals))@basis.conj().T)@u0
            defect = float(np.linalg.norm(u-u0, 2))
            assert defect <= amplitude+1e-12
            maximum_trace_ratio = 0.0
            maximum_form_ratio = 0.0
            for ell in range(-2*d, 2*d+1):
                power = np.linalg.matrix_power(u, ell)
                old_power = np.linalg.matrix_power(u0, ell)
                finite_bound = min(2.0, abs(ell)*defect)
                op_error = float(np.linalg.norm(power-old_power, 2))
                assert op_error <= finite_bound+1e-10
                trace = np.trace(power)/d
                comb = 1.0 if ell % period == 0 else 0.0
                assert abs(np.trace(old_power)/d-comb) < 1e-11
                assert abs(trace-comb) <= finite_bound+1e-10
                if finite_bound:
                    maximum_trace_ratio = max(maximum_trace_ratio, float(abs(trace-comb)/finite_bound))
                form = float(abs(np.trace(power))**2/d)
                assert abs(form/d-abs(trace)**2) < 1e-12
                if ell % period:
                    bound = d*ell*ell*defect*defect
                    assert form <= bound+1e-10
                    maximum_form_ratio = max(maximum_form_ratio, form/bound)
            rows.append({'period':period,'multiplicity':multiplicity,'dimension':d,
                         'amplitude':amplitude,'one_step_operator_defect':defect,
                         'integer_times_checked':4*d+1,
                         'maximum_trace_to_bound_ratio':maximum_trace_ratio,
                         'maximum_off_resonance_form_to_bound_ratio':maximum_form_ratio})
    return {'producer':'computations/verification/compensated_trace_window.py',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status':'PASS','seed':20260905,
            'scope':'Finite generic unitary telescoping, trace/form-factor normalizations, and separated-cluster averaged form-factor bounds; not a verification of the analytic parent theorem or a proof by numerical extrapolation.',
            'checks':rows, 'cluster_window_checks': cluster_window_checks(rng)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    text=json.dumps(report(),indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    else:
        print(text,end='')


if __name__=='__main__':
    main()
