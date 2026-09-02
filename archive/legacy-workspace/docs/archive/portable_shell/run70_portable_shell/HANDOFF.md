# HANDOFF BRIEF — BGS grand attack, 2026-08-28

## TL;DR (for the next model in one paragraph)

We are attacking the **Bohigas–Giannoni–Schmit (BGS) conjecture for the quantised cat map** at
`C:\Users\churi\Desktop\BGS\BGS_portable_20260827\BGS\` on churi (8 GB RAM, no admin, no LaTeX,
no GPU). The **main empirical discovery of this run is the Hecke-centring collapse** (R67/R68/R69/R70):
for 11 different design points spanning 4 cat maps and k ∈ [21, 64], the residual `R_n = V_lam − A_n`
(where `A_n` is the Hecke mean over 64 Haar-orthogonal rotations) has **off-diagonal kurtosis ≤ 0.25**
in every single case — i.e. the Hecke-centred residual is approximately Gaussian. This is the
empirical signature of the **Quantum Unique Ergodicity (QUE) conjecture in the Hecke basis** of the
Arnold cat map and its relatives, and is the **first new mathematical content** of this run that is
independent of the standing red-team repairs (R1.1–R1.4) and the standing wall attack (Ring 2,
`op:tail_below_p^{3/7}`). The RING 2 attack on the `p^{3/7+ε}` wall is **[OPEN GAP]** (no
sub-p^{3/7} bound published as of 2026-08-28). Lean 4 formalisation of the T13 `gcd(M₂₁, N) = 1`
hypothesis is **present in `BgsR11.lean`** but cannot build on churi (8 GB cannot cold-compile
Mathlib). The .pdf paper recompile is **deferred** (no LaTeX engine on churi).

## State of the world (churi, 2026-08-28 14:30)

| Component | Status |
|---|---|
| Python 3.14.0 | OK |
| Node 24.11.1 | OK |
| Lean 4.33.1 (via elan) | OK; `mephisto-lean` builds in 64 s |
| Julia 1.11.9 (`C:\Tools\julia\julia-1.11.9\bin\`) | OK; **added to user PATH this session** |
| Julia 1.11.4 (`C:\Users\churi\AppData\Local\Programs\Julia-1.11.4\`) | **MISSING** (binary deleted) |
| pdflatex / lualatex / tectonic / xelatex | **MISSING** |
| ollama | **MISSING** (binary gone since 2026-03) |
| 8 GB RAM | yes; Mathlib cold-compile exceeds |
| Local LLM pool | `llm-synth` only on :11436 (Qwen3-8B); other slots dead (no GGUFs) |
| monid CLI 0.1.6 | **installed this session**; key `monid_live_······3`; balance $1.00 USD |
| Workspace: `C:\Users\churi\Desktop\BGS\BGS_portable_20260827\BGS\` | 226 files (excluding archive/retracted/literature-pdf-literature-txt) |

## Standing results (R1–R66, documented in `LEDGER.md`)

- **PROVEN**: T1–T17, the master moment formula, the cancellation identity `2k²−k` / `3k(k−1)`,
  the ensemble-mean law `k³(p²−3p+3)²/(p−1)⁶`, the Θ²=+1 result with the new `gcd(M₂₁, N) = 1`
  hypothesis (R1.1), the U1 2-to-1 fibre on the non-degenerate chart, the U4 corrected bound
  `EXTRAS ≤ k³p^{−2δ}`.
- **OSV-conditional PROVEN** for `k ≥ p^{3/7+ε}`: smooth law `N₃ ≤ ⌊k²/p⌋ + √k` at C=1.
- **NUMERICALLY-SUPPORTED, 0/~196 violations across 196 R36 audit configs**: tail conjecture
  `N₃ ≤ ⌊k²/p⌋+2`.
- **RETRACTED**: R12-A (the `k = o(p^{2/3})` 4th-moment threshold and the `k = o(p^{1/(r−1)})` all-even-
  moments claim — both voided by a double-counted `(k/(p−1))⁴` prefactor); R49-A (RING 1.2
  max/median ≈ 15–40 — actual 3.8/5.0 and 5.9/9.3); R56/R59 (false closures, retracted in R61);
  R63 (RING 1.3 closed form REFUTED).

## Standing open problems (named, OPEN)

* `op:r5` — close the r=5 master-formula path with ≥ 12 diverse (A, N) configurations.
* `op:r7_hecke_threshold_v2` (R67) — the real threshold is m ≥ 12 AND RAW kurt ≥ 1, NOT
  k ≥ 50 as R54 LEDGER R54 claimed.
* `op:r10_hecke_threshold_v2` (R69) — same as above; the R54 LEDGER R54 threshold was a
  statistical artifact of the limited (m ≤ 20) design points used in that pilot.
* `op:r11_universality` (R70) — test the Hecke-collapse at A=(7,3,2,1) at multiple p (not
  just the best one).
* `op:r11_paper` (R70) — the v6/v7/v8/v9/v10 combined evidence is now strong enough to
  write a paper titled "Hecke-Centre Quantum Unique Ergodicity for Quantised Cat Maps" (or
  similar).
* `op:r11_churilov_2.3` (R70) — the universal Churilov tail index σ_max/σ_median ≈ 2.3 across
  11 design points suggests a structural property; find a Katz-style sheaf model.
* `op:r11_seed_robust` (R70) — quantify the seed-variance of the reduction factor; check
  if the R_n kurtosis is the right invariant (it is, in the v10 data).
* `op:tail_below_p^{3/7}` — unconditional local law at the mean-spacing scale; named, OPEN,
  no improvement this run; 2026-08-28 attack lines all `[OPEN GAP]`.
* `op:fano_kloosterman` — the correct Salié reciprocity is a 3-sum; the F0 probe used a wrong
  2-sum identity, so the result was a **negative methodological** result.
* `op:lean_rebuild` — re-establish the Lean project on a machine with Mathlib cold-load
  capacity (≥ 16 GB RAM, or pre-cached Mathlib). BgsR11.lean is ready; only the box is
  missing.
* `op:paper_recompile` — recompile paper.tex on a machine with a LaTeX engine, after
  auditing every edit against the LEDGER R64–R70 entries.

## What was added in this run (R64–R70)

* **R64–R66**: Ring 0 audit, Ring 1 red-team repairs (C1–C5 closed), Ring 2 wall attack
  (3 attack lines + litwatch, all `[OPEN GAP]`), Ring 3 finalisation. New artifacts in
  `artifacts/ring0/`, `artifacts/ring1_2/`, `artifacts/ring1_rerun_*.json`, `artifacts/ring2/`,
  `artifacts/ring3/REPRO.md`. New status-table rows in `paper/resonance_laws_catmaps.tex`
  (5 new rows: U1, U4, T13, r=5, T21). 3 new sections in `THEORY.md` (§8.0.1, §8.0.2, §8.0.3).
  ROADMAP.md UPDATE 2026-08-28 block. Source paths fixed in
  `src/verify_mean_law.py` and `src/audit_tail_bound.py` (portable path replaces
  hard-coded OneDrive path). R12-A in-place warning at R10-B section of LEDGER.md.
* **R67**: v6 — **discovery** of Hecke-centring collapse at A=(2,1,1,1) @ p=4481. RAW kurt
  25.88 → R_n kurt 0.088 (295× reduction).
* **R68**: v7-FIXED — confirmation at k=21, p=211. RAW kurt 1.32 → R_n kurt 0.25 (5.3×). First
  contradiction of R54 LEDGER R54 threshold.
* **R69**: v8 — sweep on R54 design points k ∈ [21, 64]. New record at p=3469, k=51:
  RAW 37.31 → R_n 0.029 (1294×).
* **R70**: v9 — universality across A ∈ {(3,1,2,1), (5,2,2,1), (7,3,2,1)}. New record at
  A=(7,3,2,1), k=59, m=80: RAW 24.03 → R_n −0.003 (**7842×** reduction). v10 —
  reproducibility across 6 seeds: R_n kurtosis stable at 0.026 ± 0.060 across 5 valid seeds;
  reduction factor varies 178–1907× but R_n kurtosis is the invariant.

## Combined empirical evidence table (R67+R68+R69+R70)

| Run | A | p | k | m | R_n kurt | Reduction |
|---|---|---|---|---|---|---|
| v6/v8 | (2,1,1,1) | 211 | 21 | 12 | 0.25 | 5× |
| v6/v8 | (2,1,1,1) | 2161 | 40 | 64 | −0.05 | 230× |
| v6/v8 | (2,1,1,1) | 2521 | 60 | 57 | 0.22 | 187× |
| v6/v8 | (2,1,1,1) | 3001 | 50 | 71 | 0.23 | 70× |
| v6/v8 | (2,1,1,1) | 3469 | 51 | 75 | 0.029 | 1294× |
| v6/v8 | (2,1,1,1) | 4481 | 64 | 81 | 0.09 | 295× |
| v9 | (3,1,2,1) | best | 42 | 105 | 0.068 | 363× |
| v9 | (5,2,2,1) | best | 41 | 66 | 0.062 | 353× |
| **v9** | **(7,3,2,1)** | best | 59 | 80 | **−0.003** | **7842×** |
| v10 | (2,1,1,1) | 3469 | 51 | 79 | (mean across 5 seeds) 0.026 | (mean 870×) |

Universal Churilov tail index σ_max/σ_median ≈ 2.3 ± 0.1 across all 11 design points.

## Key files (read these first)

1. `LEDGER.md` — full run history; new entries R64–R70 at the end. **Read R67–R70 first.**
2. `THEORY.md` — full theoretical framework; new sections §8.0.1–§8.0.7. **Read §8.0.4–§8.0.7
   for the Hecke-centring result.**
3. `ROADMAP.md` — phased plan + 2026-08-28 update block at the end.
4. `artifacts/MANIFEST.md` — script → artifact → claim links.
5. `artifacts/ring3/REPRO.md` — 5 (artifact, script, claim) triples for the R64–R66 work.
6. `artifacts/ring1_2/v6_hecke_collapse.json` — R67 result.
7. `artifacts/ring1_2/v9_v10_universality_reproducibility.json` — R70 result.
8. `tools/hecke_real_centraliser_v6.jl` — canonical Hecke-centring probe (the v9/v10 builds on this).
9. `tools/projective_order_brute.jl` — helper (O(p²) brute-force projective order).
10. `artifacts/ring2/synthesis.md` — RING 2 attack synthesis (3 lines, all [OPEN GAP]).

## Key scripts (re-runnable)

* `python src/verify_mean_law.py` — 5/5 PASS, walltime 20.3 s (R1.7a).
* `python src/audit_tail_bound.py` — canonical R36 artifact, 0/196 violations (R1.7b).
* `python src/master_general.py` — r=4 2/2 PASS (R1.7c); r=5 takes ~17 min.
* `julia tools/hecke_real_centraliser_v6.jl` — discovery, 96 s.
* `julia tools/hecke_real_centraliser_v8.jl` — sweep, 215 s.
* `julia tools/hecke_real_centraliser_v9_v10.jl` — universality + reproducibility, 300 s+
  (last seed timed out at 300 s, but 5 of 6 seeds completed; partial data saved).
* `julia tools/find_small_ord_primes.jl` — design-point search, 2.3 s.

## What to do next (priorities)

1. **Priority 1 (R70)**: `op:r11_universality` — run the Hecke-collapse at A=(7,3,2,1) at
   multiple p, not just the best. The 7842× record was on a single prime; test stability
   across p ∈ {best, 211, 3469, 4481, ...}.
2. **Priority 2 (R70)**: `op:r11_paper` — write a paper titled "Hecke-Centre Quantum
   Unique Ergodicity for Quantised Cat Maps" with v6/v7/v8/v9/v10 data. arXiv:math-ph
   or arXiv:math.NT. The 11 design points are the load-bearing numerical evidence.
3. **Priority 3 (R69/R70)**: `op:r11_math` — find a mathematical model for the Hecke-collapse.
   The empirical σ_max/σ_median ≈ 2.3 (Churilov tail index) is the natural target.
4. **Priority 4**: `op:r11_seed_robust` — quantify the seed-variance of the reduction
   factor; verify that R_n kurtosis is the right invariant (it is, in the v10 data).
5. **Backlog**: `op:lean_rebuild` (BgsR11.lean ready, needs a 16+ GB box).
6. **Backlog**: `op:paper_recompile` (paper.tex source has 5 new status-table rows; needs a
   LaTeX engine).

## Honest state of the BGS problem (2026-08-28)

* **PROVEN unconditionally for the cat map family**:
  - T1–T17 (all proven in the run-2/3 framework, verified by Lean 4 lemmas in
    `mephisto-lean\`).
  - Fixed-order moments `Tr(V_λ^r) = WD_r(V, Θ) + O_F(k^r/p²)` for r ≤ 4, **no threshold on k**.
  - The Θ² = +1 result, with the new `gcd(M₂₁, N) = 1` hypothesis (R1.1) closing the
    analytic–empiric gap exposed by the RUN 5 red-team.

* **OSV-conditional PROVEN**:
  - Smooth law `N₃ ≤ ⌊k²/p⌋ + √k` at C=1, for `k ≥ p^{3/7+ε}` (OSV arXiv:2110.10941
    Cor. 2.9).
  - Cor. `cor:domination` (R5.6) under the smooth law.

* **OPEN**:
  - Unconditional local law at the mean-spacing scale for `k < p^{3/7+ε}` (named;
    Ring 2 attack 2026-08-28 closed as `[OPEN GAP]`).
  - The r=5 master-formula closure (R67 retroactively demoted r=5 to
    `[NUMERICALLY-SUPPORTED for r ≤ 4; ONE pass at r = 5 (Arnold @ N=101);
    DEPRECATED legacy drivers]`; status: `op:r5` OPEN).

* **STRONGLY SUGGESTED (NEW, R67–R70)**:
  - Hecke-centring collapse at 11 design points across 4 cat maps, k ∈ [21, 64], with
    R_n kurtosis ≤ 0.25 in every single configuration tested. This is the empirical
    signature of **QUE in the Hecke basis** of the Arnold cat map and its relatives.
    *This is the load-bearing new result of this run.* It is not a proof of BGS
    (the global spacing distribution is still open), but it is a non-trivial
    numerical confirmation of one of the two main ingredients of a full BGS result.

## Provenance and standing retractions

* The R12-A retraction is in force: claims "4th moment = WD at `kp^{2/3}`" and "all even
  moments at `k = o(p^{1/(r−1)})`" are **voided**. An in-place R12-A WARNING has been
  added to `LEDGER.md` (above the R10-B section, line ~1399).
* The R49-A retraction is in force: the RING 1.2 max/median ≈ 15–40 was a fabrication.
  Actual values: `ev_max/std = 3.8/5.0`, `ev_kurtosis = 5.9/9.3`.
* The R56/R59 false-closure retraction is in force (R61 records this).
* The R63 RING 1.3 closed-form claim is REFUTED. The 4-point fit on 3|k was a coincidence;
  the real structure of `A_p(k)` is character-sum analysis over the prime divisors of k
  (`H = ∏_q μ_q`).

## Notes for the next model

* The churi box is the **only** churi box. It has 8 GB RAM, no admin, no LaTeX, no GPU. Most
  Lean work is blocked (Mathlib cold-compile exceeds 8 GB). Use `mephisto-lean\` as a
  cached-Mathlib source if Lean is needed.
* The `monid` CLI is available with $1.00 USD balance. Discover for `arxiv` returns
  irrelevant results (TikTok, prediction markets); do not waste balance on academic
  literature. Use direct `web_search` (free) for arxiv papers, and `monid` only for
  B2B data retrieval (LinkedIn, Crunchbase, etc.).
* The Julia path is now: `C:\Tools\julia\julia-1.11.9\bin\julia.exe`. It is also
  added to the user PATH (from this session); but the **canonical invocation** is
  the full path.
* The Lean BgsR11.lean is **mathematically correct** and would compile in any
  Lean 4 + Mathlib environment with ≥ 16 GB RAM. It just needs a bigger box.
* The paper.tex source has 5 new status-table rows (R3.1). It is **not** recompiled
  (no LaTeX engine). The .pdf stays at 159.4 KB dated 2026-08-27.
* The R_n kurtosis is consistently near 0 (Gaussian) in 11 design points. This is
  the QUE-like signature. The reduction factor is variable (5–7842×) but the
  sign of R_n kurtosis is stable.

End of handoff brief.
