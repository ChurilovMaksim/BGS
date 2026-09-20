"""Finite diagnostic of the actual weighted subset-energy sum.

No phase average replaces the fixed map. Artificial phase controls are
explicit comparisons, never evidence of CUE universality.
"""
import argparse
from itertools import combinations, islice
import importlib.util
import json
from math import comb
from pathlib import Path
import time

import numpy as np

HERE = Path(__file__).resolve().parent


def model(n):
    source = HERE.parent/'secular-route/exact_structure_checks.py'
    spec = importlib.util.spec_from_file_location('secular_structure', source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    a, m = module.frozen_matrices(n)
    energies, vectors = np.linalg.eigh(a)
    b = vectors.conj().T@m@vectors
    return energies, b


def principal_minors(energies, b, k):
    n = len(energies)
    count = comb(n, k)
    frequencies = np.empty(count)
    weights = np.empty(count, dtype=complex)
    iterator = combinations(range(n), k)
    offset = 0
    while batch := list(islice(iterator, 8192)):
        index = np.array(batch, dtype=np.int64)
        stop = offset+len(batch)
        frequencies[offset:stop] = energies[index].sum(axis=1)
        weights[offset:stop] = np.linalg.det(b[index[:, :, None], index[:, None, :]])
        offset = stop
    assert offset == count
    order = np.argsort(frequencies, kind='stable')
    return frequencies[order], weights[order]


def close_pairs(frequencies, weights, widths, control_count=4):
    indices = np.arange(len(weights))
    magnitude = np.abs(weights)
    abs_prefix = np.concatenate(([0], np.cumsum(magnitude, dtype=np.longdouble)))
    square = magnitude.astype(np.longdouble)**2
    square_prefix = np.concatenate(([0], np.cumsum(square, dtype=np.longdouble)))
    # long-double accumulation limits artificial loss in nearby interval sums.
    prefix = np.concatenate(([0j], np.cumsum(weights, dtype=np.clongdouble)))
    diagonal = np.sum(magnitude**2, dtype=np.longdouble)
    rng = np.random.default_rng(20260920+len(weights))
    controls = []
    for _ in range(control_count):
        artificial = magnitude*np.exp(2j*np.pi*rng.random(len(weights)))
        artificial_prefix = np.concatenate(([0j], np.cumsum(artificial, dtype=np.clongdouble)))
        controls.append((artificial, artificial_prefix))
    rows = []
    for width in widths:
        left = np.searchsorted(frequencies, frequencies-width, side='left')
        signed = 2*np.real(np.sum(weights*np.conj(prefix[indices]-prefix[left]), dtype=np.clongdouble))
        absolute = 2*np.sum(magnitude*(abs_prefix[indices]-abs_prefix[left]), dtype=np.longdouble)
        artificial_signed = [float(2*np.real(np.sum(w*np.conj(p[indices]-p[left]), dtype=np.clongdouble)))
                             for w, p in controls]
        # E S=0 and E S^2=2 sum_(i>j, close) |w_i w_j|^2 for
        # independently uniform phases. This is an analytic null-model
        # variance, not a distributional or independence claim for the map.
        null_variance = 2*np.sum(square*(square_prefix[indices]-square_prefix[left]), dtype=np.longdouble)
        rows.append({'width': width, 'unordered_close_pairs': int(np.sum(indices-left)),
                     'signed_offdiagonal_sum': float(signed),
                     'absolute_offdiagonal_sum': float(absolute),
                     'diagonal_mass': float(diagonal),
                     'signed_over_diagonal': float(signed/diagonal),
                     'signed_over_absolute': float(signed/absolute) if absolute else None,
                     'independent_phase_standard_deviation': float(np.sqrt(null_variance)),
                     'artificial_phase_controls': artificial_signed})
    return rows


def run(n):
    started = time.monotonic()
    energies, b = model(n)
    k = n//2
    frequency, weights = principal_minors(energies, b, k)
    # The sum of principal minors must agree with the coefficient of det(I-zB).
    # In these small dimensions direct polynomial evaluation remains stable.
    direct = np.poly(np.linalg.eigvals(b))[k]
    summed = (-1)**k*np.sum(weights, dtype=np.clongdouble)
    check = float(abs(summed-direct))
    assert check <= 5e-9*max(1, abs(direct))
    maximum_frequency = float(np.max(abs(frequency)))
    # Global scalar centering only rotates these weights at nonzero epsilon.
    # Here epsilon=0 isolates correlations of actual minor phases. It is not
    # a resolved calculation of the minute frozen kick or a BGS statistic.
    rows = close_pairs(frequency, weights, [1/n, 1/n**2, 1/n**4])
    result = {'N': n, 'k': k, 'subset_count': len(weights),
              'principal_minor_sum_check': check,
              'minimum_adjacent_frequency_gap_float': float(np.diff(frequency).min()),
              'maximum_absolute_subset_frequency': maximum_frequency,
              'diagonal_mass': float(np.sum(abs(weights)**2)),
              'total_weight_squared': float(abs(summed)**2),
              'windows': rows, 'seconds': time.monotonic()-started,
              'scope': 'floating diagnostic of minor weights at epsilon=0; no asymptotic or CUE claim'}
    (HERE/f'probe_N{n}.json').write_text(json.dumps(result, indent=2)+'\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dimensions', type=int, nargs='+', default=[15, 19, 23])
    args = parser.parse_args()
    for n in args.dimensions:
        r = run(n)
        print(json.dumps({'N': n, 'subsets': r['subset_count'],
                          'minor_sum_error': r['principal_minor_sum_check'],
                          'seconds': r['seconds'], 'windows': r['windows']}), flush=True)
