#!/usr/bin/env python3
"""Plot the proved second-return formulas; no finite spectra or fitted data."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]


def main():
    plt.rcParams.update({"svg.hashsalt": "pell-harmonic-returns-v1", "font.size": 11})
    t = np.linspace(0, 5, 501)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(t, np.exp(-2*t), label=r"$\beta=0$: wrapped normal", color="#172d46")
    for beta, color in ((1/6, "#127e83"), (1/4, "#b27713"), (1/2, "#b44054")):
        b = (1-2*beta)/2
        label = {1/6: r"$\beta=1/6$", 1/4: r"$\beta=1/4$",
                 1/2: r"$\beta=1/2$: free unitary Brownian"}[beta]
        ax.plot(t, np.exp(-t)*(1-t*np.exp(-b*t)), label=label, color=color)
    ax.axhline(0, color="grey", linewidth=0.7)
    ax.set(xlabel=r"Rescaled kick variance $t=\tau^2$",
           ylabel=r"Limiting normalized trace $F_{2,\beta}(t)$",
           title="Second return of the kicked Pell cat map")
    ax.legend(frameon=False)
    ax.grid(alpha=0.15)
    fig.text(0.12, 0.015, "Analytic limits at time 2K; global return law, not microscopic BGS.",
             fontsize=9, color="#555555")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    out = ROOT/"assets/figures/pell_harmonic_returns.svg"
    fig.savefig(out, metadata={"Date": None})
    fig.savefig(ROOT/"build/harmonic-returns-preview.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
