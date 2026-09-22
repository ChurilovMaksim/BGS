# Research integration and verification — 22 September 2026

The historical research overlay was prepared against
`39d4e01ae6a6b3eb472ab30266b708ca71a70a16`. Before integration,
`main` had advanced by 14 commits to
`ac94d783f31208ae3916250b4b6381c4a77e65c0`, tree
`d243065725589484bafda5fcc5ff117e85ecd803`. A current 694-blob tree
was reconstructed and checked byte-for-byte against the Git blob hashes and
its root tree. The overlay's seven older-file edits were reconciled with the
new manuscript name and scientific registry; the pinned installer was not
misapplied to a different Git revision. This record is an integration audit,
not a claim that the original wide BGS conjecture was solved.

## Maintained additions

- `mathematics/finite_orbit_resonance_rigidity.md`: the smooth theorem for
  finitely many signed Fourier orbits, both trace signs, arbitrary phases and
  all finite lag combinations. `BGS-RES-004` is linked from the current
  claim ledger, result index, generated TeX chapter, topic map and a scoped
  publication candidate. The proof depends on the earlier finite-Fourier
  lag theorem and all-pass invariance, whose existing status is preserved.
- `mathematics/clustered_abel_window_boundary.md`: an exact Poisson-kernel
  lower bound for clustered abstract spectra and a simple-spectrum
  counterexample separating Abel divergence from positive-time window
  form factors. `BGS-TRACE-006` is scoped in the ledger, result index,
  topic map and fixed-map frontier publication candidate. The application
  to the explicitly compensated Pell family is conditional on its already
  maintained pinning theorem; its classical strength vanishes.
- `record/research_cycle_20260922.md` records executed proof,
  counterexample and deduplication branches. Existing polynomial, generic,
  and fixed-point Hessian results are credited instead of relabelled.
- An earlier stale paragraph in
  `mathematics/quantitative_resonance_transversality.md` has been corrected:
  the finite-polynomial several-orbit question was already closed. The
  analytic cohomology summary in `mathematics/open_questions.md` now matches
  the adapted-norm regularity theorem; its Lean status distinguishes the
  historical 16-module pass from later source-level additions.
- Current manuscript `manuscript/BGS_unified.tex` includes the new generated
  finite-orbit chapter beside its pre-existing temporal resonance input.
  The fixed-map chapter had a pre-existing source-hash synchronization
  mismatch at the current base; it has been regenerated. A page-break guard
  keeps Theorem 1 and its displayed conclusion on the same page.

## Proof and execution boundaries

The detailed initial proof audit is
`record/finite_orbit_proof_audit_20260922.md`; a separate internal derivation
of the channel signs, separation, factorization and finite-Fourier
dependency is `record/finite_orbit_secondary_review_20260922.md`. Neither
is an external referee report. The abstract spectral proof is self-contained
in its maintained note; finite diagnostics are in
`record/abel_window_research_20260922.md`.

At this integration, the following commands completed successfully:

| Check | Actual result and limit |
|---|---|
| `python3 computations/verification/finite_orbit_resonance.py --output build/verification/finite_orbit_exact.json` | Eight matrices, 2,976 exact channel comparisons and 28,520 cross-patterns. These finite cases do not prove the theorem. |
| `g++ -std=c++20 -O2 -Wall -Wextra -pedantic -I build/dependencies/boost/usr/include computations/verification/finite_orbit_degeneracy.cpp -o build/verification/finite_orbit_degeneracy`, then execute | Boost arbitrary-precision integers; 147,456 candidates, 912 identities, 7,680 recurrences and 40 delayed collisions. |
| `python3 computations/verification/scientific_registry_audit.py` and `python3 computations/verification/repository_audit.py` | Registry, generated-source and repository structure checks passed. |
| `python3 computations/maintenance/sync_return_sections.py --check`; the corresponding fixed-map and finite-orbit `--check` commands | Both pre-existing chapter families and the new generated chapter match their maintained sources. |
| `python3 computations/maintenance/verify_fixed_map_supplement.py --output-dir build/fixed-map-replay` | 28 isolated finite replays passed; no mixed-resolvent asymptotic theorem follows. |
| `python3 computations/maintenance/verify_workspace.py --build build/cmake --logs build/verification-logs --output build/workspace-verification.json --workers 4 --allow-dirty` | Complete maintained Python/C++ surface: 124/124 checks passed, including both sequential certificate replays. The tracked source-tree hash was identical before and after. The manifest explicitly records the 50-file dirty integration checkout; this is not a clean-commit CI run. |
| `python3 computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper` | Three pdfLaTeX passes; 233 pages and no gated layout/reference warnings. A rendered check of pages 164–165 confirmed that Theorem 1 is kept together after its layout correction. The PDF remains an ignored build artifact. |
| Numerical check printed in `record/abel_window_research_20260922.md` | Direct trace factorizations, Poisson energy and the explicit positive-time bound agreed in the stated finite instances. Floating diagnostics, not proof. |

Boost's headers and CMake were obtained in the ignored `build/` area after
the base runtime lacked them. No package manager output, compiled binary,
PDF, or build tree is promoted to the scientific source tree. The added
`formalization/FiniteOrbitAlgebra20260922.lean` and Wolfram inputs are
**source-only in this pass**; no Lean or Wolfram execution is claimed.
The workspace launcher now supplies the required output path to the new
finite-orbit verifier. Two damaged ignored CMake outputs were rebuilt from
their unchanged sources before the final full run; no such binary is tracked.

The fixed-strength Heisenberg-scale estimate `BGS-TRACE-005`, the general
all-analytic resonance claim `BGS-RES-003`, and terminal microscopic
universality `BGS-BGS-001` remain **OPEN**. No external priority or
independent journal-referee validation is asserted.
