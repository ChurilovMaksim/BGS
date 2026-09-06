#!/usr/bin/env python3
"""Reproduce Floquet figures from the complete, scope-labelled certificate."""
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    data = json.loads((ROOT/'evidence/certificates/pell_floquet_audit.json').read_text())
    out = ROOT/'assets/figures'
    out.mkdir(parents=True, exist_ok=True)
    rows = data['dense_checks'] + data['sampled_checks']
    fig, ax = plt.subplots(figsize=(8,4.8))
    for m, marker in ((1,'o'), (2,'s')):
        selected = sorted((r for r in rows if r['tau']==1.0 and r['m']==m), key=lambda r:r['K'])
        xs = [r['K'] for r in selected]
        ys = [r['trace_real'] for r in selected]
        err = [r.get('complex_RMS_error_upper_bound',0) for r in selected]
        ax.errorbar(xs, ys, yerr=err, marker=marker, capsize=3,
                    label=f'm={m}: actual propagator trace')
        ax.axhline(math.exp(-m*m/2), linestyle='--', label=f'm={m}: wrapped Gaussian limit')
    ax.set_xlabel('Odd prime period K')
    ax.set_ylabel('Real part of normalized trace')
    ax.set_title('Critical quantum kick: epsilon = 1 / sqrt(2K)')
    ax.set_xticks([3,5,7,11,13])
    ax.legend(fontsize=8, loc='center right')
    fig.text(.5,.01,'K <= 7: complete dense calculation. K = 11, 13: 32 seeded probes; bars are RMS bounds, not confidence intervals.',
             ha='center',fontsize=7)
    fig.tight_layout(rect=(0,.04,1,1))
    for suffix in ('svg','png'):
        fig.savefig(out/f'pell_floquet_echo.{suffix}',dpi=170)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(8,4.8))
    selected = data['arithmetic_checks']
    xs = [r['K'] for r in selected]
    ax.plot(xs, [r['K_weighted_phase_l1'] for r in selected], 'o-', label=r'$K\sum_j |c_j|a_j$')
    ax.plot(xs, [r['K_times_commutator_HS_squared'] for r in selected], 's-', label=r'$K\|[G,\overline{B}]\|_{2,N}^2$')
    ax.axhline(2*math.pi/(1-(3+2*math.sqrt(2))**-3),linestyle='--',label='Uniform weighted-phase bound')
    ax.axhline(9,linestyle=':',label='Proved squared-commutator bound')
    ax.set_xscale('log')
    ax.set_xlabel('Odd prime period K')
    ax.set_ylabel('Dimensionless finite quantity')
    ax.set_title('Weighted arithmetic cancellation and commutator control')
    ax.legend(fontsize=8)
    fig.tight_layout()
    for suffix in ('svg','png'):
        fig.savefig(out/f'pell_floquet_commutators.{suffix}',dpi=170)
    plt.close(fig)

if __name__=='__main__':
    main()
