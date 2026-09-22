#!/usr/bin/env python3
"""Illustrate complete finite Cayley-trace laws; not a theorem certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
from math import erf, sqrt
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'computations' / 'verification'))
from cayley_higher_moments import cayley_design


def split_prime(K, lower):
    t = (lower - 1 + K - 1) // K
    while not sp.isprime(t*K+1):
        t += 1
    return t*K+1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'assets/figures/cayley_trace_gaussian.svg')
    parser.add_argument('--report', type=Path,
                        default=ROOT/'evidence/certificates/cayley_trace_illustration_20260909.json')
    args = parser.parse_args()
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'svg.hashsalt': 'bgs-cayley-trace-20260909',
                         'axes.spines.top': False, 'axes.spines.right': False})
    fig, axes = plt.subplots(1, 3, figsize=(12.3, 4.0), sharey=True)
    records = []
    for ax, (K, p) in zip(axes, [(11, 199), (31, split_prime(31, 100000)),
                                (101, split_prime(101, 1000000))]):
        _, values = cayley_design(K, p)
        indicator = np.zeros(p)
        indicator[list(values.values())] = 1
        transform = np.fft.ifft(indicator)*p/sqrt(K-1)
        imaginary_error = float(np.max(np.abs(transform.imag)))
        assert imaginary_error < 1e-10
        sample = np.sort(transform.real[1:])
        normal_cdf = np.fromiter((0.5*(1+erf(float(t)/sqrt(2))) for t in sample),
                                 dtype=float, count=p-1)
        positions = np.arange(1, p)/(p-1)
        ks = float(max(np.max(positions-normal_cdf),
                       np.max(normal_cdf-(positions-1/(p-1)))))
        ax.hist(sample, bins=35 if K == 11 else 65, density=True,
                color='#346e95', alpha=0.75, label='All nonzero frequencies')
        grid = np.linspace(-4.5, 4.5, 500)
        ax.plot(grid, np.exp(-grid**2/2)/sqrt(2*np.pi), color='#bd592e',
                linewidth=2, label='Standard normal')
        ax.set(xlim=(-4.5, 4.5), xlabel='Normalized real trace',
               title=f'K = {K}, p = {p:,}\nCDF distance = {ks:.4f}')
        records.append({'K': K, 'p': p, 'nonzero_frequencies': p-1,
                        'cdf_distance_to_normal': ks, 'max_imaginary_residual': imaginary_error,
                        'moments': {str(r): float(np.mean(sample**r)) for r in [1, 2, 3, 4, 6]}})
    axes[0].set_ylabel('Empirical density')
    axes[1].legend(loc='upper left', fontsize=8)
    fig.suptitle('Finite Cayley-trace laws', fontsize=15)
    fig.text(0.5, 0.025,
             'Numerical illustration. Theorems require a stated limiting regime; '
             'these finite plots do not prove universality.', ha='center', fontsize=9)
    fig.tight_layout(rect=(0, 0.06, 1, 0.94))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={'Date': None})
    plt.close(fig)
    if args.output.suffix == '.svg':
        args.output.write_text('\n'.join(line.rstrip() for line in
                                        args.output.read_text().splitlines())+'\n')
    report = {'status': 'NUMERICAL', 'numpy': np.__version__,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'figure_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest(),
              'sampling': 'Every q=1,...,p-1; FFT in double precision; no random samples.',
              'designs': records}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(records, indent=2))


if __name__ == '__main__':
    main()
