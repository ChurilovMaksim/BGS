#!/usr/bin/env python3
"""Render analytic density-one pair references, without sampled spectra.

For Sine2, the two-point determinant gives rho_2(x)=1-sinc(x)^2.
This is a pair-correlation function, not a nearest-neighbour spacing density.
The SVG is a README illustration, not computational evidence for BGS.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=root / "assets/figures/microscopic_pair_reference.svg",
    )
    args = parser.parse_args()
    x = np.linspace(0.0, 4.0, 1601)
    rho = 1.0 - np.sinc(x) ** 2
    with plt.rc_context({
        "font.family": "DejaVu Sans", "font.size": 11,
        "svg.hashsalt": "bgs-pair-reference-v1",
        "axes.spines.top": False, "axes.spines.right": False,
    }):
        fig, ax = plt.subplots(figsize=(8.4, 3.5), layout="constrained")
        fig.patch.set_facecolor("white")
        ax.plot(x, rho, color="#245983", lw=2.3,
                label=r"Sine$_2$: $1-(\sin(\pi x)/(\pi x))^2$")
        ax.axhline(1.0, color="#737373", ls="--", lw=1.5,
                   label="Poisson: 1")
        ax.set(xlim=(0.0, 4.0), ylim=(0.0, 1.08),
               xlabel="Separation x / mean spacing",
               ylabel=r"Pair correlation $\rho_2(x)$")
        ax.set_xticks(np.arange(0.0, 4.1, 0.5))
        ax.grid(axis="y", color="#e6e6e6", lw=0.7)
        ax.legend(loc="lower right", frameon=False, fontsize=10)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        metadata = {"Date": None, "Creator": "BGS analytic reference"} \
            if args.output.suffix.lower() == ".svg" else None
        fig.savefig(args.output, dpi=150, metadata=metadata)
        plt.close(fig)
    print(args.output)


if __name__ == "__main__":
    main()
