"""Insert the run-71 VOID banner before THEORY.md section 8.0.4 and append
section 9 (the two exact theorems of run 71).  Idempotent."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "THEORY.md")

BANNER = """> ## SECTIONS 8.0.4 - 8.0.7 ARE VOID (retracted 2026-08-28, run 71)
>
> Everything in section 8.0.4-8.0.7 below - the "Hecke-centring collapse", the
> reduction factors 5x-7842x, the "universal Churilov tail index ~ 2.3", and the
> reading of any of it as a signature of Quantum Unique Ergodicity - rests on a
> measurement with three independent defects, all reproduced in run 71
> (`src/diagnostics/hecke_centring_refutation.py`, `artifacts/r71/*.json`, LEDGER R71.6):
>
> 1. the "multiplet basis" is `U_sub = U[:, idx]`, i.e. **columns of the
>    propagator selected by eigenvalue index** - not eigenvectors. `eigen` /
>    `eigvecs` is never called in `archive/hecke_centring_failed_line/v6.jl` nor in any
>    of v7-v10, and **no Hecke operator occurs anywhere in that code**;
> 2. the "Hecke mean" is a Haar average, and `E_Q[Q V Q*] = (Tr V / m) . 1`, so
>    its population value is a multiple of the identity and **cannot change any
>    off-diagonal entry**; with finitely many samples it merely injects
>    approximately Gaussian noise;
> 3. the accumulator is **never divided by `n_hecke`**, so the subtracted matrix
>    is 64x too large and the residual is about 8x the single-sample Haar
>    fluctuation - the "collapse" is that noise.
>
> With the correct eigenprojector basis the RAW off-diagonal excess kurtosis of
> the same observable is already -0.06 (p=1597) and +0.06 (p=2161): there is
> nothing to collapse. Reproducing the exact defective code path recovers the
> reported reductions (240x and 1433x at n_hecke=64). The "Churilov index 2.3" is
> reproduced by an arithmetic-free Haar random frame (2.24-2.38 at every sample
> count and both primes).
>
> Independently, the conclusion points the wrong way: Kurlberg-Rudnick,
> "On the distribution of matrix elements for the quantum cat map",
> arXiv:math/0302277 (accepted, Annals of Mathematics), conjecture - with the
> second and fourth moments computed in support - that Hecke-basis matrix
> elements of the desymmetrised cat map follow a weighted sum of traces of
> independent SU(2) matrices and are **not** Gaussian, "in contrast to generic
> chaotic systems where the distribution is expected to be Gaussian".
>
> Read section 9 instead. The sections below are retained unaltered for
> provenance.

"""

text = open(P, encoding="utf-8", errors="surrogateescape").read()
changed = []

if "SECTIONS 8.0.4 - 8.0.7 ARE VOID" not in text:
    anchor = "### 8.0.4 R67 "
    i = text.index(anchor)
    text = text[:i] + BANNER + text[i:]
    changed.append("inserted VOID banner before 8.0.4")

if "## 9. RUN 71" not in text:
    text = text.rstrip() + "\n\n" + open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "theory_section9.md"), encoding="utf-8").read()
    changed.append("appended section 9")

open(P, "w", encoding="utf-8", errors="surrogateescape").write(text)
print("; ".join(changed) if changed else "no change needed")
