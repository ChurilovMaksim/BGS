#!/usr/bin/env python3
"""Analytic pair and empty-component bounds, not simulated cat-map spectra."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'verification'))
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'svg.fonttype': 'none', 'svg.hashsalt': 'wow-return-obstruction'})
import matplotlib.pyplot as plt
from return_trace_obstruction import cue_gaussian


def main():
    x = np.linspace(0.5, 12, 400)
    fig, (ax, gap_ax) = plt.subplots(1, 2, figsize=(12, 4.6), layout='constrained')
    ax.plot(x, [cue_gaussian(v)/v for v in x], color='#222222', label='Sine-kernel pair target')
    ax.axhline(1, color='#777777', ls='--', label='Poisson pair target')
    for a, color in ((0.5, '#126e82'), (1, '#be6a15'), (2, '#833f8c')):
        theta = 1+2*sum(math.exp(-a*r*r) for r in range(1, 40))
        ax.plot(x, theta-1/x, color=color, label=rf'Return lower bound, $v\sigma^2={a:g}$')
    ax.set(xlabel=r'Fixed unfolded probe width $L$', ylabel=r'Gaussian pair statistic divided by $L$',
           xlim=(0.5, 12), ylim=(0, 2.55), title='A nonuniform return law forces excess local pairs')
    ax.legend(frameon=False, fontsize=9)
    ax.grid(alpha=0.15)
    t = np.linspace(0, 4, 401)
    gap = 1-(np.sqrt(t*(4-t))/2+np.arccos(1-t/2))/np.pi
    gap_ax.fill_between(t, 0, gap, color='#126e82', alpha=0.17)
    gap_ax.plot(t, gap, color='#126e82', label=r'$1-b(t)/\pi$')
    gap_ax.set(xlabel=r'Fixed Brownian return parameter $t=\tau^2$',
               ylabel='Lower bound on the empty-component probability',
               xlim=(0, 4), ylim=(0, 1),
               title='A return support gap forces an empty component')
    gap_ax.text(0.97, 0.93, r'Harmonic endpoint $\beta=1/2$'+'\n'+r'Proof range: $0<t<4$',
                transform=gap_ax.transAxes, ha='right', va='top', fontsize=9)
    gap_ax.legend(frameon=False)
    gap_ax.grid(alpha=0.15)
    fig.text(0.5, -0.04, 'Analytic limits and rigorous lower bounds; no finite-spectrum fit.', ha='center', fontsize=9)
    root = Path(__file__).resolve().parents[2]
    (root/'assets/figures').mkdir(parents=True, exist_ok=True)
    (root/'build').mkdir(exist_ok=True)
    svg = root/'assets/figures/return_obstruction.svg'
    fig.savefig(svg, bbox_inches='tight', metadata={'Date': None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    fig.savefig(root/'build/return-obstruction-figure.png', dpi=150, bbox_inches='tight')
    plt.close(fig)

if __name__ == '__main__':
    main()
