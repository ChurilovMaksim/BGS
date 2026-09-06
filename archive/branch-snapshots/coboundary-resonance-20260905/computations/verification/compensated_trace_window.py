#!/usr/bin/env python3
"""Finite unitary controls for the compensated Heisenberg-window corollary.

These test telescoping and both trace normalizations, not the smooth-symbol
normal form or the limiting BGS conjecture. Floating-point errors have a
separate comparison tolerance; there is no interval-certification claim.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np


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
            'scope':'Finite generic unitary telescoping and trace/form-factor normalization checks; not a verification of the analytic parent theorem or a proof by numerical extrapolation.',
            'checks':rows}


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
