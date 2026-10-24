#!/usr/bin/env python3
"""Reproducible harmonic sampling; integer phases, floating diagnostics.

No dense spectra are substituted for computed matrices. The fourth-moment
central term has the stated finite remainder; the sixth pairing sum is only
an asymptotic proxy, explicitly labeled as such.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import random
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/"computations/verification"))
from pell_harmonic_transition import design, pell_phase


def integer_root(n: int, degree: int) -> int:
    if n < 0 or degree < 1:
        raise ValueError("nonnegative integer and positive degree required")
    low, high = 0, 1 << ((n.bit_length()+degree-1)//degree)
    while low+1 < high:
        mid = (low+high)//2
        if mid**degree <= n:
            low = mid
        else:
            high = mid
    return high if high**degree <= n else low


def summarize(values: list[float]) -> dict:
    a = np.asarray(values)
    return {"mean": float(a.mean()),
            "sample_standard_deviation": float(a.std(ddof=1)) if len(a)>1 else 0.0,
            "standard_error": float(a.std(ddof=1)/math.sqrt(len(a))) if len(a)>1 else 0.0,
            "count": len(a)}


def sample_laws() -> dict:
    rng = random.Random(20260909)
    rows = []
    for k in (31, 61, 127):
        n, _f, _s, _h = design(k)
        phases = [pell_phase(d, k) % n for d in range(k)]
        grid = np.arange(k)
        difference = (grid[None, :]-grid[:, None]) % k
        first, second = np.arange((k+1)//2), np.arange((k+1)//2, k)
        cross_difference = (second[None, :]-first[:, None]) % k
        for j in range(5):
            beta = j/8
            length = integer_root(n**j, 8)
            assert length**8 <= n**j < (length+1)**8
            accepted = [1] if length == 1 else []
            rejected = 0
            while len(accepted) < (1 if length == 1 else 512):
                a = rng.randrange(1, length+1)
                if math.gcd(a, n) == 1:
                    accepted.append(a)
                else:
                    rejected += 1
            fourth, sixth, commutator = [], [], []
            for index, a in enumerate(accepted):
                # Reduction occurs in Python integers before conversion to float.
                residues = [(a*a*t) % n for t in phases]
                z = np.exp(2j*np.pi*np.asarray([t/n for t in residues]))
                scalar = float(z.real.mean())
                fourth.append(n/(n-1)*(2+scalar-1.5/k))
                commutator.append(float(4/k**2*np.sum(abs(z[cross_difference]-1)**2)))
                if index < 128:
                    triangle = 0.0
                    for s2, s3 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                        zj = z if s2 == 1 else z.conj()
                        zk = z if s3 == 1 else z.conj()
                        zd = z[difference] if s2*s3 == 1 else z[difference].conj()
                        triangle += float((zj[:, None]*zk[None, :]*zd).real.mean())/4
                    sixth.append(5+6*scalar+3*scalar*scalar+triangle)
            rho = 1-2*beta
            rows.append({
                "K": k, "N": str(n), "beta": beta, "L": str(length),
                "rejected_nonunits": rejected,
                "fourth_central": summarize(fourth),
                "fourth_uniform_block_remainder_bound": 8*k**3/(n-1),
                "sixth_pairing_proxy": summarize(sixth),
                "full_space_commutator_norm_squared": summarize(commutator),
                "limits": {"fourth": 2+rho,
                           "sixth": 5+6*rho+15*rho*rho/4+max(0, 1.5*rho-1)**2,
                           "commutator": 2*(1-rho*rho)},
            })
    paths = [Path(__file__), ROOT/"computations/verification/pell_harmonic_transition.py",
             ROOT/"mathematics/pell/pell_harmonic_transition.md"]
    return {
        "status": "NUMERICAL",
        "scope": "Monte Carlo harmonic averages; error bars are sampling standard errors, not rigorous analytic or floating-point enclosures",
        "sixth_scope": "Pairing proxy only; repeated-label corrections are not subtracted",
        "commutator_scope": "Normalized full-space Hilbert-Schmidt norm from exact distinct Weyl supports; the theorem also proves the same odd-space limit",
        "randomness": {"generator": "Python random.Random (Mersenne Twister)", "seed": 20260909},
        "software": {"python": platform.python_version(), "numpy": np.__version__},
        "source_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in paths},
        "rows": rows,
    }


def figure(data: dict, output: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"svg.hashsalt": "pell-harmonic-transition-v1", "font.size": 10})
    beta = np.linspace(0, .5, 401)
    rho = 1-2*beta
    limits = [2+rho, 5+6*rho+15*rho*rho/4+np.maximum(0, 1.5*rho-1)**2,
              2*(1-rho*rho)]
    fig, axes = plt.subplots(1, 3, figsize=(12.2, 4.0))
    keys = ["fourth_central", "sixth_pairing_proxy", "full_space_commutator_norm_squared"]
    titles = ["Fourth spectral moment", "Sixth pairing sum (proxy)", "Quantum commutator"]
    colors = {31: "#547fa6", 61: "#d28a36", 127: "#258c78"}
    for ax, key, limit, title in zip(axes, keys, limits, titles):
        ax.plot(beta, limit, color="#202d40", linewidth=1.8, label="Proved limit")
        for k in (31, 61, 127):
            rows = [r for r in data["rows"] if r["K"] == k]
            ax.errorbar([r["beta"] for r in rows], [r[key]["mean"] for r in rows],
                        yerr=[2*r[key]["standard_error"] for r in rows],
                        fmt="o", ms=3.5, capsize=2, color=colors[k], label=f"K={k}")
        ax.set_xlabel(r"Harmonic exponent $\beta$")
        ax.set_title(title)
        ax.set_xlim(-.015, .515)
        ax.grid(alpha=.18)
    axes[0].set_ylabel("Normalized moment")
    axes[2].set_ylabel(r"$N^{-1}\mathrm{Tr}([Y_f,Y_g]^*[Y_f,Y_g])$")
    axes[0].legend(fontsize=8)
    fig.suptitle("One Pell cat map: growing harmonics change the global observable law", y=1.02)
    fig.text(.5, -.02, "Points: sampled integer harmonics. Bars: twice the sampling standard error; no certified rounding bounds.",
             ha="center", fontsize=8.5)
    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    metadata = {"Date": None} if output.suffix == ".svg" else {}
    fig.savefig(output, bbox_inches="tight", dpi=160, metadata=metadata)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT/"build/pell_harmonic_transition_numerical.json")
    parser.add_argument("--figure", type=Path)
    parser.add_argument("--input", type=Path, help="render an existing numerical report")
    args = parser.parse_args()
    data = json.loads(args.input.read_text()) if args.input else sample_laws()
    if not args.input:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+"\n")
    if args.figure:
        figure(data, args.figure)
    print(json.dumps({"status": data["status"], "designs": len(data["rows"])}))


if __name__ == "__main__":
    main()
