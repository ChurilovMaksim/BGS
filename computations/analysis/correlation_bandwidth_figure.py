#!/usr/bin/env python3
"""Draw exact clock/dimer correlation atoms from the extension counterexample.

The infinite measures are proved in bandlimited_correlation_extension.md.
Only displayed windows are truncated; every displayed weight is exact.
"""
from fractions import Fraction as F
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]


def main():
    clock = {F(r): F(1) for r in range(-3, 4) if r}
    dimer = {F(2*r): F(1) for r in range(-2, 3) if r}
    for r in range(-2, 3):
        for sign in (-1, 1):
            dimer[F(2*r)+F(sign, 2)] = F(1, 2)
    dimer = {x: w for x, w in dimer.items() if abs(x) <= 3}
    plt.rcParams.update({'font.size': 10, 'svg.hashsalt': 'wow-bandwidth-v1'})
    fig, axes = plt.subplots(3, 1, figsize=(7.3, 6.0), constrained_layout=True)
    for ax, atoms, title, color in zip(axes[:2], [clock, dimer],
            ['Unit clock: limiting pair measure',
             'Period-two basis {0, 1/2}: limiting pair measure'],
            ['#24527a', '#a74732']):
        xs = sorted(atoms)
        ax.vlines(list(map(float, xs)), 0, [float(atoms[x]) for x in xs],
                  color=color, linewidth=2)
        ax.scatter(list(map(float, xs)), [float(atoms[x]) for x in xs],
                   color=color, s=24, zorder=3)
        ax.set(xlim=(-3.2, 3.2), ylim=(0, 1.2), ylabel='Atom weight', title=title)
        ax.set_xticks(range(-3, 4))
    # Fourier transform of dimer minus clock; common -Lebesgue term cancels.
    # At q=m/2 the exact weight is (1+cos(pi*m/2))/2 - 1_{m even}.
    cosine = [F(1), F(0), F(-1), F(0)]
    ms = [m for m in range(-4, 5) if m]
    weights = [(1+cosine[m % 4])/2-int(m % 2 == 0) for m in ms]
    ax = axes[2]
    ax.axvspan(-.5, .5, color='#dce7e8', label='No difference inside |frequency| < 1/2')
    ax.axhline(0, color='#555555', linewidth=.7)
    ax.vlines([m/2 for m in ms], 0, list(map(float, weights)), color='#455a45', linewidth=2)
    ax.scatter([m/2 for m in ms], list(map(float, weights)), color='#455a45', s=24)
    ax.set(xlim=(-2.2, 2.2), ylim=(-1.15, .8), xlabel='Fourier frequency',
           ylabel='Signed weight', title='Fourier transform of the difference')
    ax.legend(loc='lower center', fontsize=8, frameon=False)
    for ax in axes:
        ax.spines[['top', 'right']].set_visible(False)
    dest = ROOT/'assets/figures/correlation_bandwidth.svg'
    fig.savefig(dest, metadata={'Date': None})
    dest.write_text('\n'.join(line.rstrip() for line in dest.read_text().splitlines())+'\n')
    plt.close(fig)
    print(dest.relative_to(ROOT))


if __name__ == '__main__':
    main()
