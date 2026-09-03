# Research programme and roadmap

This roadmap is subordinate to root `STATUS.md`. It is the active execution programme, not a probability forecast and not a theorem-status document.

## Mission

Target a rigorous BGS-type spectral result for the audited quantised cat-map setting, with a proof chain strong enough to survive independent expert review. The ambition is a fundamental mathematical result; no award or significance claim is made in advance.

The programme follows one rule: **preserve broadly, trust narrowly**. Negative results, failed lemmas, expensive finite-N data, and alternative mechanisms are retained, but only results that pass the relevant proof/reproduction gates become load-bearing.

## Engineering policy

Active executable mathematics uses two complementary paths whenever the calculation is load-bearing:

- Python for transparent formulas, exact/integer checks where practical, falsifiers, and reproducible analysis;
- C++17 for independent reimplementation, large-N streaming/sparse computation, and protection against NumPy/BLAS-specific mistakes.

Lean is the formal track. Formal files may be written before the toolchain is available, but they must be labelled `UNVERIFIED` until an actual `lake build` succeeds. Julia is not an active dependency; historical Julia remains provenance and is ported only when a calculation becomes load-bearing again.

Compiled binaries, caches, generated Lean state, temporary sweeps, and per-run scratch outputs stay out of Git. A promoted computation gets one producer path and one compact result artifact.

## Programme gates

### G0 — provenance and reproducibility

Status: **GREEN / continuous**.

Requirements:

- every promoted result has a current producer and result path;
- historical/prototype outputs keep explicit status;
- `code/maintenance/repo_health.py` passes before promotion;
- no generated build state or redundant executable binaries are committed;
- independent implementation is required for numerically load-bearing identities when feasible.

### G1 — rank-1 exact algebra

Status: **PARTIALLY CLOSED**.

Already surviving:

- twisted-Jacobi computational representation;
- R82 reproduction;
- exact finite `k=2` layer;
- independent matrix-element regression;
- M1 cycle 001 weighted key table, quotient-character projector, singular/regular decomposition, and explicit cross-twist energy reconstruction.

Still required:

- paper-quality general proof of the weighted key parametrisation and singular split;
- exact Fourier/projector normalization in theorem form;
- formalisation of those algebraic identities.

### G2 — M1 regular single-twist analytic estimate

Status: **CLOSED AS A LEMMA / NOT THE FULL M1 THEOREM**.

Cycle 002 converts the regular `d!=0` fiber sum to a complete polynomial character sum by the exact domain mask

`Q_d(Y)^m`, `Q_d(Y)=Y(Y-1)(Y+d)(Y+d-1)`.

The root-multiplicity residues modulo the quotient-character order `m` are classified for generic `d` and the `d=±1` collisions. Every nontrivial twist is non-`m`-th-power. Applying the standard multiplicative-character Weil theorem gives

`|A_{r,s}(d)| <= 3 sqrt(N)` for every nontrivial twist and `d!=0`,

with `<=2 sqrt(N)` at `d=±1`.

The proof is `research/M1_WEIL_002.md`; Python/C++ classifiers are regression checks only. Improving this individual constant is no longer the primary task.

### G3 — centering / singular-term decision

Status: **ACTIVE AND LOAD-BEARING**.

Cycle 001 gives the exact raw lower bound

`E >= (N-2)^4`.

Therefore the programme must settle one of two routes:

- derive an exact spectral centering identity that removes the deterministic singular contribution before the M1 asymptotic estimate; or
- retain raw energy and prove a growth regime for `K` strong enough to absorb the singular scale.

This gate must be resolved before any raw `O(N^3 K^4)` theorem is promoted.

### G4 — assembled regular cross-twist covariance

Status: **PRIMARY ANALYTIC BOTTLENECK**.

The exact energy is

`E=m^{-4} ||sum_tau F_tau||_2^2`, `F_tau=A_tau*A_tau`.

Cycle 001 directly shows that the off-diagonal twist Gram terms are nonzero and can be material. Cycle 002 bounds each `A_tau(d)` separately, but that alone does not control the sum of cross covariances.

Required outputs:

1. derive a fixed-normalization Fourier formula for `<F_tau,F_sigma>`;
2. identify exact selection rules, if any, before taking absolute values;
3. otherwise reduce a two-twist covariance to a finite-field character sum whose conductor/degree stays controlled;
4. sum over the true twist geometry without an `m^4` worst-case loss;
5. obtain a normalized assembled remainder that tends to zero.

### G5 — arithmetic scaling regime

Status: **STRUCTURE IDENTIFIED / theorem integration open**.

For the fixed trace-3 cat map, if a split eigenvalue has order `K`, then `N | (L_K-2)` for the trace recurrence `L_{n+1}=3L_n-L_{n-1}`. Hence fixed `K` cannot accompany `N->infinity`; along an infinite split-prime sequence `K(N)->infinity`, with at least the elementary logarithmic lower constraint from the expanding eigenvalue.

Every asymptotic theorem must state the actual `(N,K(N),m(N))` regime and show that every error term vanishes in that regime.

### G6 — spectral consequence

Status: **OPEN**.

After G3–G5, rebuild the trace/moment/local-statistics implication from a valid noncommutative starting point. The superseded R86/R87 scalar-binomial step cannot be reused.

Required outputs:

- exact connection from the controlled finite-field observable to the relevant spectral statistic;
- a local or mesoscopic law at a stated scale;
- desymmetrisation handled explicitly;
- comparison with GOE performed with the statistic matched to its correct reference distribution.

Existing spacing and number-variance results are calibration/falsifiers, not this gate.

### G7 — robustness and universality stress tests

Status: **ONGOING NUMERICAL / NOT THEOREM**.

Use independent split-prime designs and large-N streaming implementations to try to falsify every proposed bound. The next mandatory large stress case for M1 is `N=3571,K=17,m=210`, using a memory-aware implementation rather than the dense small-N tensor.

After a rank-1 theorem exists, test variation in arithmetic regime, sector dimension, observable choice, and prime families before making a broader universality statement.

### G8 — higher rank / Sp4 programme

Status: **FINITE-N EXACT + EXPERIMENTAL**.

Keep the existing exact rank-2 identities as calibration. A higher-rank promotion requires its own uniform finite-field mechanism; it may not inherit rank-1 bounds by analogy. Negative product-kernel and other failed mechanisms remain part of the evidence base.

This workstream is parallel and must not distract from the active rank-1 bottleneck unless it produces a demonstrably cleaner replacement route.

### G9 — formalisation, manuscript, and adversarial review

Status: **CONTINUOUS, proof-complete promotion pending**.

For each load-bearing theorem:

1. write the human proof with all normalisations and exceptional cases;
2. encode finite/exact algebraic layers in Lean where practical;
3. disclose every `sorry`, opaque axiom, or unbuilt file;
4. run an independent computational implementation on theorem-level identities;
5. perform a red-team pass that actively searches for counterexamples, regime mistakes, normalisation drift, hidden commutativity, and statistic/reference mismatches;
6. only then promote manuscript language from conjectural/conditional to theorem status.

A proof-complete paper is the final output of the programme, not an input assumption.

## Immediate execution queue

1. **M1-003: centering audit — ACTIVE.** Trace the exact singular term back through the spectral moment reduction and determine whether it cancels under the correct centered observable. If it does, write the centering identity before any asymptotic estimate; if it does not, retain the raw lower-bound obstruction explicitly.
2. **M1-004: assembled covariance — ACTIVE NEXT.** Derive the Fourier-side formula for cross-twist Gram terms and search for exact selection rules or a two-twist character-sum bound.
3. **M1-005: large stress implementation.** Build sparse/streaming C++ plus Python orchestration for `N=3571,K=17,m=210`; reproduce the historical correction with every cross term retained.
4. **Formal track.** Extend `formal/Bgs/M1CrossEnergy.lean` with the general key/projector and cycle-002 statements when a Lean toolchain is available; until then keep formal obligations explicit and unverified.
5. **Manuscript discipline.** Do not resurrect a proof-complete M1 paper until G3–G5 are actually closed.

## Promotion discipline

A result is promoted only when the evidence type matches the claim:

- exact finite computation -> finite identity/certificate only;
- numerical sweep -> empirical/falsifier evidence only;
- human analytic proof -> theorem candidate, pending dependency audit;
- Lean source without a successful build -> formal specification only;
- successful formal build -> machine-checked only for the statements actually encoded;
- spectral numerics -> evidence for the target law, never a substitute for the asymptotic theorem.

The programme optimises for correctness and depth, not for the number of files, experiments, or claimed milestones.
