# WoW: quantum cat maps and the BGS frontier

A research repository for exact arithmetic reductions, quantized chaotic
maps, spectral correlations and reproducible verification. Mathematical
proofs, numerical tests, finite formal certificates and unresolved targets
are distinguished explicitly. No complete BGS or world-priority claim is made.

## Fixed-strength locality and long-time conjugacy

The [locality proof](mathematics/fixed_strength_locality.md) studies the
natural **single-exponential** kick

```text
V_(kappa,N) = exp(i kappa N Op_N(g-g composed with M)) U_N,
M = transpose([[3,2],[4,3]]),
support(g) disjoint from support(g composed with M).
```

Here the nonzero classical strength kappa is fixed. The quantum comparison
with `A U_N A*`, where `A=exp(i kappa N Op_N(g))`, has operator-norm error
smaller than every power of `1/N`. It survives all fixed polynomial times,
including Heisenberg time. An explicit Gevrey-2 bump also gives the conservative
bound `C kappa^2 N^2 exp(-c N^(1/3))` and a stretched-exponential time range.

Along odd-prime Pell periods, each arithmetic root retains an equal-rank,
superpolynomially narrow cluster. Globally unfolded spacings collapse to
zero, normalized close-pair counts diverge, and the local point process at a
uniformly random origin tends to the empty process despite finite mean
intensity one. Polynomially distorted unfolding cannot remove this effect.

## Stability above the mean-spacing scale

The [robustness addendum](mathematics/locality_robustness.md) strengthens this:
all three conclusions persist under **arbitrary unitary norm errors
`eta_N=o(1/K)`**, including errors much larger than the mean spacing `1/D`.
The proof uses explicit covering inequalities, not eigenvector stability:

```text
fraction of gaps > x <= K/D + ell/x,
normalized ordered close pairs <= x >= 1/(K/D + ell/x) - 1,
probability a random-origin length-L window meets a level <= KL/D + ell.
```

In these formulas the spectrum is covered by K arcs of total length ell.
A nonempty limit after unfolding requires a nonvanishing image-cover length.
For the explicit Gevrey example, this forces a stretched-exponential lower
bound on the unfolding's Lipschitz constant.

**Essential boundary:** these nonlinear Anosov maps are exactly smoothly
symplectically conjugate to an arithmetic cat map. Their inherited structure
is not removed by changing coordinates. The results establish negative local
statistics for this specified family, not positive generic BGS universality.
The norm assumption on an alternative quantization must be checked; equality
of classical principal maps alone does not imply it.

## What has actually been verified

The [execution record](record/locality_packet_executed_20260905.md) and
[compact manifest](evidence/certificates/locality_execution_summary.json)
report a completed **20/20 targeted local suite**, with **124 scientific
source/configuration files unchanged during the recorded run**. The scope is
eight Python checks and twelve C++ executables in the reconstructed worktree,
not every historical symbolic Python verifier. Complete logs and the original
full manifest are retained in the delivered research packet. Two subsequent
editorial wording corrections to the proof are identified separately.

Independent checks include exact integer support/cluster calculations,
54 rational covering/unfolding cases, 27 classical ODE comparisons, physical
Weyl covariance including composite N, and actual one-exponential quantum
matrices. A Poisson-commuting negative control has a nonzero cubic quantum
commutator, preventing an incorrect inference from Poisson commutation alone.
Finite nonmonotonic errors and Fourier-refinement limitations are retained.

The new Lean module has **not** been compiled in the available local runtime.
It covers algebraic kernels only, not the analytic theorems. Remote workflow
33979761923 failed before steps; its cause is not established. Two complete
historical Python attempts were interrupted and are not counted as passes.
Successful local tests or a publication script do not imply a successful
remote CI run or an uploaded binary PDF.

## Repository map

| Location | Contents |
|---|---|
| [mathematics/results.md](mathematics/results.md) | Theorem index and earlier arithmetic results |
| [record/claim_ledger.md](record/claim_ledger.md) | Maintained claim ledger; latest locality scope is supplemented by the execution record above |
| [record/research_operating_protocol.md](record/research_operating_protocol.md) | Review, verification and publication discipline |
| [mathematics/fixed_strength_locality.md](mathematics/fixed_strength_locality.md) | Complete fixed-strength argument and its prior-work boundary |
| [mathematics/locality_robustness.md](mathematics/locality_robustness.md) | Finite covering theorem, norm-stability range and necessary unfolding distortion |
| [computations/verification/fixed_strength_locality.py](computations/verification/fixed_strength_locality.py) | Physical Weyl and finite-matrix falsifiers |
| [computations/verification/fixed_strength_classical.py](computations/verification/fixed_strength_classical.py) | Independent classical flow/sign checks |
| [computations/verification/locality_robustness.py](computations/verification/locality_robustness.py) | Exact rational covering and unfolding checks |
| [computations/cpp/fixed_strength_locality_exact.cpp](computations/cpp/fixed_strength_locality_exact.cpp) | Independent exact integer representation |
| [formalization/Bgs/LocalityKernels.lean](formalization/Bgs/LocalityKernels.lean) | Narrow formalization source; compilation required before machine-checked status |
| [manuscript/fixed_strength_section.tex](manuscript/fixed_strength_section.tex) | Updated main-paper section |

The publication script regenerates the locality companion, diagnostics,
README/ledger additions and main-paper inclusion. Updated binary PDFs and full
logs are delivered separately when remote artifact publishing is unavailable.
Previously committed PDFs must not be assumed to contain the latest section.

## Other maintained research branches

The [Pell Floquet normal form](mathematics/pell_floquet_normal_form.md) proves a
wrapped-normal recurrence law for a shrinking cosine kick, with finite error
`12 epsilon^2/sqrt(K)` in normalized odd Hilbert--Schmidt norm. The
[weighted echo extension](mathematics/pell_weighted_gaussian_echo.md) treats
bounded coefficient arrays and a periodic-memory Gaussian tracial limit.
Neither is an independent-eigenvalue or path-space universality claim.

The [magnetic-quotient analysis](mathematics/magnetic_quotient_semicircle.md)
separates a restricted global semicircle law from fixed-map and microscopic
questions. The earlier arithmetic programme includes exact pair-key and
Cayley-energy reductions, fixed-product rows, real-trace/cyclotomic support,
reflection factorization and Frobenius amplification. Their detailed statements,
hypotheses and external inputs remain in the theorem index and proof notes.
The sharp pointwise split-energy and general microscopic spectral closures
are not declared solved by the locality construction.

The previously reported fourth-moment decimal `5.612...` was corrected in the
Floquet branch to `5.614220692151198071627965...`; the
[integer interval checker](computations/verification/pell_gamma_interval.py)
and [continuation audit](record/floquet_continuation_20260905.md) record that
separate transcription/provenance correction. No such decimal is used as an
input to the fixed-strength locality theorem.

## Reproduction

Python dependencies are pinned in `requirements.txt`. C++ requires C++20,
CMake and Boost. Article generation additionally requires Pandoc, latexmk and
a TeX installation. Run from the repository root:

```sh
python -m pip install -r requirements.txt
python computations/maintenance/publish_fixed_strength.py --integrate-only
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j2
python computations/maintenance/verify_locality_packet.py \
  --build build --logs /tmp/wow-locality-checks \
  --output evidence/certificates/locality_packet_validation.json
```

The targeted runner checkpoints each command atomically. To resume an
interrupted run, repeat that last command with `--resume`; changed source or
log hashes are rejected. A pending or interrupted command is not a success.
For the analytic article and figures:

```sh
python computations/maintenance/publish_fixed_strength.py
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_strength_locality.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error arithmetic_cat_map_moments.tex
```

`cd formalization && lake build` is a separate formalization check. The full
historical suite remains available through `verify_workspace.py`; its scope
and execution result must be reported separately from the targeted suite.

## Remaining central objective

Establish microscopic random-matrix universality for a natural fixed chaotic
family after the correct symmetry reduction, not merely for its global density
or a shrinking perturbation. The present work controls long times for an
arithmetic-conjugate exceptional family. It does not supply the corresponding
joint-trace estimates for a fixed nonconjugate perturbation. That distinction
is retained in the mathematical statements, manuscript and execution record.
