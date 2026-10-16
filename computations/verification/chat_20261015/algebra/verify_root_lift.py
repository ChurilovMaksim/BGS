"""Finite tests of spectral root lifting, not tests of BGS for the physical map.

Dependencies: NumPy, SciPy.  All floating checks use explicit tolerances;
these checks corroborate exact identities but do not prove asymptotic limits.
Run with: OPENBLAS_NUM_THREADS=1 python verify_root_lift.py
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.linalg import qr, eigvals

def cue_phases(q: int, rng: np.random.Generator) -> np.ndarray:
    if q < 1:
        raise ValueError('q must be positive')
    z = (rng.normal(size=(q, q)) + 1j * rng.normal(size=(q, q))) / np.sqrt(2)
    unitary, r = qr(z, mode='economic', check_finite=False)
    diagonal = np.diag(r)
    unitary = unitary * (diagonal / np.abs(diagonal))[None, :]
    return np.sort(np.mod(np.angle(eigvals(unitary, check_finite=False)) / (2 * np.pi), 1))

def lift_phases(phases: np.ndarray, d: int) -> np.ndarray:
    if d < 1:
        raise ValueError('d must be positive')
    return np.sort(((phases[None, :] + np.arange(d)[:, None]) / d).ravel())

def traces(phases: np.ndarray, powers: np.ndarray) -> np.ndarray:
    return np.exp(2j * np.pi * powers[:, None] * phases[None, :]).sum(axis=1)

def local_points(phases: np.ndarray, origin: float, radius: float) -> np.ndarray:
    q = len(phases)
    turns = int(np.ceil(radius / q)) + 2
    x = q * (phases[:, None] - origin + np.arange(-turns, turns + 1)[None, :])
    return np.sort(x[np.abs(x) < radius])

def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> None:
    rng = np.random.default_rng(20261015)
    phi = cue_phases(11, rng)
    d = 7
    theta = lift_phases(phi, d)
    q, n = (len(phi), len(theta))
    powers = np.arange(1, 2 * n + 1)
    actual = traces(theta, powers)
    expected = np.zeros(len(powers), dtype=complex)
    mask = powers % d == 0
    expected[mask] = d * traces(phi, powers[mask] // d)
    trace_error = float(np.max(np.abs(actual - expected)))
    need(trace_error < 1e-09, 'root lift trace identity failed')
    local_error = 0.0
    for origin in rng.random(100):
        x = local_points(theta, float(origin), 4.0)
        y = local_points(phi, float(d * origin % 1), 4.0)
        need(len(x) == len(y), 'local point counts differ')
        if len(x):
            local_error = max(local_error, float(np.max(np.abs(x - y))))
    need(local_error < 1e-10, 'unfolded point-process identity failed')
    gap_base = q * np.diff(np.r_[phi, phi[0] + 1])
    gap_lift = n * np.diff(np.r_[theta, theta[0] + 1])
    gap_error = float(np.max(np.abs(np.sort(gap_lift) - np.sort(np.tile(gap_base, d)))))
    need(gap_error < 1e-10, 'gap replication identity failed')
    a, b = (0.25, 0.49)
    target = (b * b - a * a) / 2
    rows = []
    repetitions = 24
    for q, d in [(31, 5), (63, 11), (127, 23), (255, 47)]:
        n = q * d
        r = np.arange(int(np.ceil(a * q)), int(np.floor(b * q)) + 1)
        mu = float(np.sum(r) / q ** 2)
        var = float(np.sum(r * r) / q ** 4)
        vals = []
        for _ in range(repetitions):
            base = cue_phases(q, rng)
            val = float(np.sum(np.abs(traces(base, r)) ** 2) / q ** 2)
            vals.append(val)
        full_powers = np.arange(int(np.ceil(a * n)), int(np.floor(b * n)) + 1)
        original_cue_mean = float(np.sum(full_powers) / n ** 2)
        rows.append({'q': q, 'd': d, 'N': n, 'trials': repetitions, 'mean_resonant_energy': float(np.mean(vals)), 'exact_CUE_mean_base': mu, 'exact_variance_single_base': var, 'standard_error_mean': float(np.sqrt(var / repetitions)), 'CUE_mean_dimension_N': original_cue_mean, 'mean_total_signed_discrepancy': float(np.mean(vals) - original_cue_mean), 'asymptotic_resonant_energy': target})
    report = {'status': 'finite numerical verification; no physical BGS claim', 'seed': 20261015, 'trace_error': trace_error, 'point_process_error': local_error, 'spacing_error': gap_error, 'window': [a, b], 'trials': rows}
    output = Path(__file__).with_name('verification.json')
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
if __name__ == '__main__':
    main()
