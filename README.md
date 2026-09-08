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

The September 7 addendum includes the audited unrestricted finite-Fourier theorem, the global Corvaja--Zannier Cayley subgroup-curve specialization, and the rare-phase / fixed-noisy-Gaussian / pure-loss information-limit results.

## Canonical publication

There is one maintained publication entry point:

`manuscript/WoW_unified.tex`

Build it with:

```sh
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

The split `.tex` files under `manuscript/` are source segments of that one
article. The September 8 revision builds to 153 pages. Its analytic transfer
estimate preserves the full adapted exponential rate, and its deterministic
correlation theorem removes the band-limit under explicit positivity and
all-bandwidth hypotheses. The scoped proof review, limitations and actual
execution record are in `record/referee_audit_20260908.md`.

An exact illustration of why a fixed Fourier cap is insufficient is in
`assets/figures/correlation_bandwidth.svg`; its producer is
`computations/analysis/correlation_bandwidth_figure.py`.

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