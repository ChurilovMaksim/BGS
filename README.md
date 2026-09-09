# WoW — arithmetic quantum maps and quantum-chaos verification

This branch is the canonical current research state. Historical branch source trees are not vendored into `main`; Git history and `archive/branch-snapshots/README.md` retain their provenance.

## Current scientific status

The repository contains exact arithmetic reductions, finite-field/Cayley energy results, Pell/Floquet and cohomological resonance laws, unrestricted finite-Fourier temporal nondegeneracy, fixed-strength locality/conjugacy results, finite and independent verification kernels, noncommuting return-word constructions, holomorphic/Husimi identifiability results, and continuous-variable information-limit theorems.

Repository-wide claim status is controlled by:

1. `record/claim_ledger.md` for the base corpus through 2026-09-06;
2. `record/claim_ledger_addendum_20260907.md` for the dated scopes added or corrected on 2026-09-07.

The dated addendum wins for claims in its scope. Historical prose, exploratory notes and finite experiments do not override these ledgers.

A positive generic microscopic BGS/GOE/COE universality theorem is **not** claimed and remains open. In particular, the missing positive bridge is still Heisenberg-scale desymmetrized joint-trace comparison on every compact Fourier support. Under positive normalized averaging, the deterministic extension to all Schwartz correlation tests is now proved; it needs no separate trace-tail assumption.

## Current theorem index

Read `mathematics/results.md` together with `mathematics/results_20260907_addendum.md`. The current genuinely open obligations are in `mathematics/open_questions.md`.

The latest result connects Gaussian and semicircular **global observable
laws in the same fixed Pell cat map**. Sample unit harmonics up to
$L=N^{\beta+o(1)}$, $0\le\beta\le1/2$. Every fixed spectral moment converges
in probability, uniformly over the odd eigenspaces, to a circle-graphon
moment law. Its fourth moment is $3-2\beta$; the sixth moment distinguishes
it from an independent-crossing model. The limiting support is unbounded
for every $\beta<1/2$ and becomes $[-2,2]$ at $\beta=1/2$.
Ordered quantum moments and an explicit commutator limit are also proved.
The graphon law construction is prior work; priority for this arithmetic
realization is unverified. See
[`mathematics/pell_harmonic_transition.md`](mathematics/pell_harmonic_transition.md)
and [the scoped review](record/pell_harmonic_transition_review_20260909.md).
These changing-frequency observables do not establish microscopic BGS.

The September 7 addendum includes the audited unrestricted finite-Fourier theorem, the global Corvaja--Zannier Cayley subgroup-curve specialization, and the rare-phase / fixed-noisy-Gaussian / pure-loss information-limit results.

The September 9 result is a Gaussian limit for the normalized **full
Cayley--Jacobi trace**, jointly at finitely many distinct positive integer
multiples of its additive parameter. It holds along every split-prime sequence
with prime subgroup order `K -> infinity`, `K=o(log p)`, and in probability over
dyadic split designs with `K=X^(o(1)) -> infinity`. The proof uses weighted
cyclotomic resultant budgets at every fixed order. See
[`mathematics/cayley_trace_gaussian_limit.md`](mathematics/cayley_trace_gaussian_limit.md).
Parameter multiples are not powers of one quantum propagator; microscopic
BGS remains open.

The scalar refinement also gives a Kolmogorov-distance bound
`C((K-1)^(-1/2)+sqrt((K-1)/log p))` for every split-prime design.
In dyadic windows with sufficiently large `Q<=X^(1/4)`, all but a fraction
`O((log X)X^(-1/4))` have distance
`O(Q^(-1/2)+sqrt(log Q/log X))` from the standard normal law.
These are quantitative bounds with absolute, unoptimized constants.

## Canonical publication

There is one maintained publication entry point:

`manuscript/WoW_unified.tex`

Build it with:

```sh
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

The split `.tex` files under `manuscript/` are source segments of that one
article. The September 8 revision built to 153 pages. Its analytic transfer
estimate preserves the full adapted exponential rate, and its deterministic
correlation theorem removes the band-limit under explicit positivity and
all-bandwidth hypotheses. The scoped proof review, limitations and actual
execution record are in `record/referee_audit_20260908.md`.
The September 9 revision adds the trace-limit proof and scalar error bounds,
and initially built to 159 pages. Its specific review
and verification scope is recorded in `record/cayley_trace_review_20260909.md`.
The subsequent harmonic-transition revision builds to 165 pages, with the
new proof in Section 24, pages 40--46.

The harmonic transition is illustrated in
`assets/figures/pell_harmonic_transition.svg`. Its points are numerical
harmonic samples, with the sixth pairing sum explicitly labeled as a proxy;
the proof does not rely on fitting those samples.

An exact illustration of why a fixed Fourier cap is insufficient is in
`assets/figures/correlation_bandwidth.svg`; its producer is
`computations/analysis/correlation_bandwidth_figure.py`.

The complete finite trace laws for three arithmetic designs are illustrated in
`assets/figures/cayley_trace_gaussian.svg`. This floating-point illustration is
separate from the exact all-order verifier:

```sh
python computations/verification/cayley_higher_moments.py
python computations/analysis/cayley_trace_limit_figure.py
```

## Verification

```sh
python -m pip install -r requirements.txt
python computations/verification/repository_audit.py
cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release
cmake --build build/cmake --parallel
python computations/maintenance/verify_workspace.py --build build/cmake --logs build/verification-logs --output build/workspace-verification.json
(cd formalization && lake build)
```

`verify_workspace.py` runs the maintained Python verification surface and every CMake-backed C++ verifier; the extremal-resonance C++ target has a no-argument self-test and a second packet replay after the Python exact witness producer completes.

The active computational stack is Python/C++/Lean/TeX. Julia is retired from the repository and the structural audit rejects tracked `.jl`, `Project.toml`, or `Manifest.toml` files.

The September 8 local pass completed 106 Python/C++ checks and the full pinned
Lean build (16 active modules). Native Lean certificates retain their native
evaluation trust boundary; see `formalization/README.md`. A workflow ending
with `steps=[]` is an infrastructure non-run and supplies no scientific evidence.

## Provenance

The recovered 204-file consolidation delivery is identified by SHA-256 `8addfd45f0c8d3d43d06472477aa8c5aac8eb3f2b94082fe6b715b20a3447099`; byte-level details are in `archive/delivery-20260906/README.md`. Promoted evidence and maintained producers are mapped in `evidence/provenance.md`.

The repeated September 7 synchronization/integrity audits are recorded under `record/`; they distinguish proof corrections, finite regressions, external-theorem inputs, publication freshness and unavailable CI/Lean execution rather than collapsing them into one verdict.
