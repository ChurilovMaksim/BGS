# Breakthrough program — research record (Nov 2026)

Autonomous method-search program for the Bohigas–Giannoni–Schmit (BGS)
conjecture for the frozen toric map. This directory is a research record,
promoted under the evidence rules: promotion means an object is useful to
the research record; it does not make it a theorem. The claim registry
(`record/claims.json`) controls registered status and is unchanged by this
package. Nothing here is recorded as solved without the cycle: mathematical
argument → numerical check (Python/C++) → Lean 4 formalization. Proof
sketches, censuses, and drafts with `sorry` are labeled as such, never as
proofs. BGS in full generality remains open.

## Layout

| Path | Contents |
|---|---|
| `methods/` | Wave notes (`waveNN_*.md`, `M01`–`M10`) and their check scripts (`.py`, `.cpp`), exactly as run. Scripts were run from this directory and may reference each other by bare filename. |
| `working/` | Auxiliary working material (`audit/`, `cleanup-plan/`, `frozen-map/`, `g4/`, `g4check/`, `literature/`, `numerics/`), text files only. |
| `../formalization/drafts/` | Lean drafts. Each file carries a header with its exact build result and `sorry` count. None is imported by `formalization/Bgs.lean`. |
| `PROGRAM.md`, `DAY1_REPORT.md` | Program plan and day-1 report. |
| `../executions/20261102/breakthrough-integration.md` | Receipt for this integration: base commit, file counts, re-verification results, exclusions. |

## What is NOT here (as of the 2026-11-02 integration)

- 8 large data files (1.3 GB total: `.json`/`.npz`/`.npy`/`.bin` census outputs)
  cannot be pushed through the GitHub connector (16 MiB UTF-8 snapshot limit)
  and stay local. Small result files are summarized inside the wave notes.
- Run logs (`.log`), binary pickles (`.pkl`), and the superseded draft
  `LineBRadicalDraft_v1_preAPIfix.lean` (replaced by `LineBRadicalDraft.lean`).
- The exact Δ(48) value: a background enumeration is still running.
- The Lean draft of DIV/PAR valuation lemma V3 (`DivParV3.lean`): its
  sequential build was still running when this package was assembled.
- Binary pickles and logs inside the working directories, and `.json`
  result files there (summarized in the notes where they matter).

## Wave index (one line each; the note file is the record)

- Day 1 (`M01`–`M10`): method swarm. M01/M05 killed; target ensemble for the
  fixed map is CUE not COE; frozen even kick commutes with parity (pooled
  spectrum looks Poisson-like, desymmetrized sectors RMT-like).
- Waves 2–13: G3 in the wave-6 sense (the S-bound) argued analytically
  modulo G4 at m = 3–6 (sketch, S ≤ g′·max N_r; not in Lean); wave 12 uses
  the label G3 for a different statement (one common π across components),
  which is NOT proved; 2-adic and 3-adic LTE proved; G4b closed as an
  analytic argument (not in Lean); Lemma Y as proof sketch; O\* killed at
  m=12; universal Deff branch of hEquidistUnits killed.
- Waves 14–26: exact per-fiber deficit Δ_F (R = Bsym_fiber − Δ); Bsym values
  at m=8/12; JBL restated per-class; 175 as a diagonal-model theorem only
  (NOT full propagator, TRACE-005, spectrum, CUE, or exact constant); Lemma Y
  Lean milestone drafts build with `sorry` (statement well-formedness only).
- Waves 27–31: M4/R40/R30 proved (G1 at f=4 closed); PC at (12,3,5),
  (12,3,11), (12,5,11); Hypothesis H dead; H12-poly proved exponentially;
  COH fails at m=60 (R\*\*+COH route to JBL dead, JBL survives); RB1′/RB2
  refuted; diagonal 175 fixed copy builds (0 errors, 5 sorry).
- Waves 32–36: Δ→0 recount v2; Lemma F exponent identity proved (H0
  unconditional); F2-poly proved; Split-Count Lemma (n_q ≤ 10) false but
  SC(c=5) survives; SIZE proved; SCJ locked/free decomposition; Lift-Tower
  false as stated, repaired; PAIR reduced to Lemma U; 2-part pattern
  T_k = 5(k−4) modulo three lemmas; σ-structure: JBL holds (existence
  reading), strong exactly-affine reading fails at m=30 (18,000 pairs).
- Wave 37: Full Blindness proved for odd p; B(60) = 5,929 exactly; m=60 joint
  total polynomial with c_J = 8; Lemma U: no counterexample; 18,000
  non-affine pairs at m=30 characterized (residue-scaling mechanism).
- Wave 38: N(b) ≤ 2p^{2e}/d unconditional; polynomiality exactly equivalent
  to bounding e(p) (open Wieferich-type problem); Blindness Law for both
  move types, but B(m) route to SCJ dead (B(180) ≥ 7.6×10²⁰); partial-
  conjugation mechanism of Lemma U proved; 2-part gaps reduced to three
  statements; period-≤4 birth stability proved.
- Wave 39: polynomial SCJ dead (section ≥ 2.96×10²⁶ at m=180); Δ→0 survives
  via SCJ′ modulo F1–F4; scaling mechanism under saturation hypothesis H2′;
  Split Bit Lemma modulo Gap G; reversal exclusion at p=8 for split
  points; outside-regime vanishing slice for odd p.
- Wave 40: Δ→0 recount v3; H2′ under order-growth; W₂ verified to 10⁹
  (e=2 exactly at 13, 31, 1546463; no e≥3); JBL ⟺ PC when v₂(m) ≤ 2; Pairing
  Lemma exhaustive at m=8/16; Gap G proved at m=32.
- Wave 41: Gap G at m=64; reversal exclusion for general p; SC-sup modulo
  S-tuple lemma; F2-poly reconciled (drops out of Δ→0); Lemma U
  classification with H4 exactly empty (one-step branching is the wrong
  tool); census 44,932,435 points, 0 conflicts.
- Wave 42: Gap G at m=128 (T_k rests only on the U-lemma); full-cycle
  rigidity at m=30; S-tuple dihedral lemma PROVED (SC-sup unconditional);
  SCL for the 3-part to v₃(m) ≤ 10; F1–F4 verified at m=252.
- Wave 43: full-cycle rigidity at m=60 for small components (new mechanisms:
  partial negations, p=3 kernel translations); Gap G at m=256/512 with
  induction step reduced to tower pinning, (B3) proved; SCL-poly for odd p
  (SCL drops out of Δ→0, replaced by W₂); F4 proved except gcd(d_a,36)=1
  regime; Pairing Lemma REFUTED at m=32, pair (8192,17) — JBL itself
  untouched.
- Wave 44: JBL-grade pairing holds at m=32 (0 bad pairs), naive
  class-by-class pairing refuted (20,480 pairs); doubling-tower pinning
  (B1),(B2) proved for j ≥ 7 modulo DIV and PAR; slice PC at m=24
  (376,185,238 pairs, 0 failures); F4 gcd=1 regime looks vacuous; Lemma U
  at m=60 completed including 601²/2281² (87,649,154 representatives,
  0 conflicts).
- Wave 45: common π for JBL proved for both GPL families + trivial
  stabilizer; JBL-grade pairing at (8192,577): 57,939,907 collisions,
  0 bad (sampling, not proof); Lemma U alignment modulo L1/L3, census at
  m=110 (0 conflicts); DIV at j=7 modulo PAR; mod-16 digit rule at j=9,10;
  F3 uniform phase gap exactly 2π/3 modulo H-quad/H-diff; W₂ extended to
  10¹⁰ (no new e≥2); Lean draft of H2′ (0 errors, 3 sorry).
- Wave 46: Δ→0 v4 — exactly three hypotheses (W₂, SCJ′, 2-part bound);
  T_k rests on the 2-part U-lemma over Gap G; H-quad/H-diff derived from
  definitions (F3 on 3-adic LTE alone, 36∤m vacuous); DIV and PAR proved
  in general (pinning unconditional for j ≥ 7); L1 proved at f=1 and for
  units, false for non-units (mod-49 counterexample); L3 via Dickson
  identity; Gap G at j=11 via step-32 witnesses (8,388,608 points); F4
  gcd=1 vacuous at 6 values; PC pairwise compatibility clean (16,211,212
  pairs); JBL Theorem B for class-homogeneous fibers (strong form
  refuted by counterexample).
- Wave 47: single-q weak form proved for negation family and rotation
  families R1–R3 at q=577, (577,3) consistency for R1/R2 — proved
  coverage 15.0% of 19,660,800 rotation pairs; ladder prediction confirmed
  at j=12 (33,554,432 points); L1\* collision form confirmed at 4 new
  prime powers (318,056 collisions, 0 unexplained) but sharp Stab
  equality false (holds in 64 of 1,171 groups; only inclusion survives);
  PC triple intersections PENDING (runs); F1 proved in general, F2a
  modulo locked-period existence; 2-part U-lemma reduced to CSL-max;
  ψ-analysis proved in general; F4 bullets closed (vacuous at 360/1260,
  lcm<M dichotomy, non-injective a); T_k periods closed modulo standing
  hypotheses; Lean DIV/PAR V3 draft PENDING (build running).
- Wave 47x (extension): L3 at p|T proved for unit cycles with distinct
  mod-p values (p odd ≠ 3) via Frobenius/period-collapse; mirror
  conjugate-prime twins DO feed genuine ℘-collisions (real instance at
  (137²,137), u=2329, g=17) and must be listed in any Lemma U closure;
  CSL-max proved modulo Gap G + Tower-Base Lemma (T_k rests on Gap G
  alone); ladder prediction confirmed at j=13 (134,217,728 points);
  JBL rotation census: proved families 15.0%, rest open.

## Standing open fronts (after this package)

Δ→0 needs W₂ in general (verified to 10¹⁰), SCJ′ (upper bound itself,
locked existence in general), and the 2-part bound. T_k needs Gap G in
general (ladder census-confirmed through j=13) plus the Tower-Base Lemma.
JBL needs the weak form for the remaining rotation classes, joint
(577,665857) consistency, and general m. Lemma U needs: L1\* proof for
units at general p^f, L3 for non-uniform towers / repeated-value /
singular cycles / p=3, and mirror twins in the mechanism list. PC needs
triple intersections of Π cosets and pairs with 1153² beyond the slice.
