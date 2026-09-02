# BGS — Bohigas–Giannoni–Schmit Conjecture for the Quantised Cat Map

> **Complete research workspace** on the BGS conjecture for quantised
> linear automorphisms of the two-torus, with the rank-2 generalisation
> to Sp(2g).
>
> **Main papers:** [`paper/final/cat_map_bgs_main.pdf`](paper/final/cat_map_bgs_main.pdf) (25 pp, compiled)
> and [`paper/final/bgs_complete_paper.pdf`](paper/final/bgs_complete_paper.pdf) (the full chain).
> **Definitive proof:** [`paper/final/mobius_fiber_theorem.pdf`](paper/final/mobius_fiber_theorem.pdf) (the δ = o(1) theorem).
> **Compiled:** 2026-09-02. **Last verified:** all artifacts reproduce.

## Quick orientation for a new AI agent

Read this file, then `docs/programme_status.md` (the honest state),
then `HANDBOOK.md` (the detailed reference), then `THEORY.md` (the
mathematical framework, §19.18–19.36 for the latest results).

The programme is **not finished**.  What IS finished: the rank-1
(cat map) chain through the k=4 fluctuation layer (M1 = theorem), and
the rank-2 (Sp₄ diagonal) coupled-energy flatness (G0 mechanism).
What is NOT finished: the ESY deterministic assembly (M3), the
non-diagonal Sp₄ Hecke operator (M4d), and k ≥ 6 layers.  All are
scoped in `docs/research_goals.md` and `docs/sp4_project_scope.md`.

## Folder structure

```
paper/final/          — compiled PDFs (the main results)
  cat_map_bgs_main.pdf          — the 25-page main paper
  bgs_complete_paper.pdf        — the complete research paper
  h_coupling_research_note.pdf  — the H-coupling research note
  mobius_fiber_theorem.pdf      — the δ = o(1) standalone proof
paper/sections/       — LaTeX section files (new results)
paper/patches/        — paper patch scripts (idempotent)

code/core/            — cat-map quantisation (certified ≤ 7e-14)
code/theorems/        — theorem implementations (A–H, II)
code/verification/    — reproducible verification scripts
code/sp4/             — Sp₄ Weil representation + G0 probe
code/kloosterman/     — subgroup Kloosterman sum tools
code/shape_automaton/ — shape-language automaton
code/maintenance/     — workspace hygiene scripts
code/llm/             — LLM audit utilities

data/proof/           — proof artifacts (Lean inputs, twist identities)
data/moments/         — moment tables (Catalan layer, surface terms)
data/spectral/        — GOE spacing, rigidity, Stieltjes, radius
data/rank2_sp4/       — rank-2 Sp₄ coupled-energy measurements
data/legacy/          — older computations (chronological record)
data/diagnostics/     — diagnostic scripts and outputs
data/tools/           — tectonic.exe (LaTeX compiler)

formal/               — Lean 4 project (no Mathlib)
  Bgs/K2Reduction.lean    — k=2 counting certificate (native_decide)
  Bgs/K4Variety.lean      — k=4 variety count certificate
  Bgs/OpLocal.lean        — op:local type signature (sorry-obligations)
  Bgs/ScaleLaw.lean       — scale law c² = t²−4 certificate
  Bgs/TorusLevelSets.lean — level-set counting certificate

docs/                 — supporting documents
  programme_status.md       — honest state of the programme
  research_goals.md         — the prize-track hierarchy
  sp4_project_scope.md      — the Sp(2g) project plan
  roadmap.md                — the historical roadmap
  trace_fluctuation_lemma.md — the trace-fluctuation lemma statement
  REVIEW_ERRORS.md          — the referee-pass error list
  REVIEW_FINDINGS.md        — the referee-pass findings
  literature/               — arXiv/OpenAlex/Crossref harvest scripts
  archive/                  — retired/failed lines (do not cite)

HISTORY.md            — the complete session log (R1–R107, chronological)
HANDBOOK.md           — the detailed mathematical reference
THEORY.md             — the full theoretical framework (§0–§19.36)
tools/                — build tools
```

## The main results (summary)

### Rank 1: the quantised cat map

| Result | Status |
|---|---|
| **Thm A**: Gaussian observable ⇒ exact `√N·GUE_m`; time-reversal ⇒ `√(N/2)·GOE_m` | PROVEN |
| **Thm B**: subgroup Kloosterman moments exactly `p²P(s,k)` balanced, 0 unbalanced | PROVEN |
| **Thm C**: `Θ² = +1` unconditional (no GSE) | PROVEN |
| **Thm D**: parity dichotomy — block-diagonal off the degenerate locus | PROVEN |
| **Thm E**: Hecke torus antiunitary ⇒ β = 1 off the degenerate locus | PROVEN |
| **Thm G**: moment route closed — `l1/l2 ≍ √K` | PROVEN |
| **Thm H**: cyclic shape decomposition exact, `M_r = 0` for `r ≤ 10` | PROVEN |
| **Thm I**: observable = one-parameter curve `q → V_q` | PROVEN |
| **Thm II**: twisted Jacobi sums certified to machine precision | PROVEN |
| **Arcsine law**: full-group moments closed-form | PROVEN |
| **GOE P(s)**: 3 designs, KS PASS | NUM-SUPPORTED |
| **GOE rigidity Σ²(L)**: matched control 6/6 | NUM-SUPPORTED |
| **H3 k=2 exact**: combinatorial, no Katz/Weil | PROVEN + Lean |
| **H3 k=4 + M1 δ = o(1)**: Möbius-fiber theorem | PROVEN |
| **Layer-uniform law**: rel_k ~ c(k)K/N | NUM (3 designs) |
| **Resolvent convergence**: m^−1.2 | NUM (4 points) |

### Rank 2: the Sp₄ generalisation

| Result | Status |
|---|---|
| **Sp₄ diagonal = phase-free dilation, exact covariance** | PROVEN |
| **Rank-2 coupled energy flat off-diagonal (~1.7%)** | NUM-SUPPORTED |
| **Rank-2 coset flatness = |coset|/G exact** | PROVEN |
| **Rank-2 coset-sector theorem (position-only)** | PROVEN |
| **Rank-2 Weil constant 0.88·√N** | NUM-SUPPORTED |

### The G0 hypothesis

For any kernel whose difference fibers are rational-function orbits of
bounded degree over an abelian group, the coupled energy factors as
`E_c = E_flat/m⁴·(1 + δ)` with `δ = O(c_w²/K²) = o(1)`.  The flat part
is elementary; the Weil part is bounded by RH over finite fields
applied to the fiber curves.  The cat map is the D = 4 rank-1 case;
the Sp₄ diagonal is the first rank-2 confirmation.

## What remains (the honest list)

1. **M3 (ESY assembly)**: the Newtonian iteration from the calibrated
   inputs to the local law.  All four inputs are measured or proven;
   the write-up is 10–15 pp of literature-standard technique.
2. **M4d (non-diagonal Sp₄ Hecke operator)**: the Bruhat assembly of
   ω(D) from the verified generators; the genuine rank-2 coupled-
   energy test with the entangled theta kernel.  See
   `docs/sp4_project_scope.md` for the sub-milestones.
3. **k ≥ 6 layers**: the template (Theorem 92.3) generalises; each
   layer needs its own δ_k analysis.
4. **General BGS**: NOT claimed — the H-coupling method applies to
   arithmetic quantum-chaos families but requires family-specific
   verification.

## Build instructions

```bash
# LaTeX papers
cd paper && ../data/tools/bin/tectonic.exe -X compile <file>.tex

# Lean certificates
cd formal && lake build

# Verification scripts (Python 3.14, numpy 2.3.5)
cd .. && python code/verification/baseline_r82.py
```

## Historical log

The complete chronological session log (R1–R107, 82+ numbered runs)
is in `HISTORY.md`.  Each run records: date, environment, what was
tried, results with status tags, artifact paths, retraction cascades,
and the named next experiment.  The ledger is append-only — no claims
are deleted, only retracted with explicit cascades.
