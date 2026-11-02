/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: draft, not built in this form; statement draft only.
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

/-!
# DRAFT ONLY — NOT A PROOF, NOT FOR MAIN

File: `bgs-breakthrough/lean-drafts/LineBG3CoreDraft.lean`
Task: wave 9, task 4 — draft Lean lemma for the G3 portable core lemma
(wave 6, task 3, note §7b).

Status: text draft only. `lake build` was NOT run (forbidden for this task),
no file in the repository was touched, nothing was pushed to `main`.
Every `sorry` below is an explicit placeholder, not a claim:
this file must not be cited as proved, and must not enter `main`
until every `sorry` is replaced and the axiom audit is clean
(standard axioms only, `sorryAx = 0`).

## What this draft is

The analytic content of G3, stripped of all `dlib` machinery, is one
self-contained finite statement (wave 6, task 3, §7b):

> Let `K` be a finite set, `gp ≥ 1`, `cls : K → ZMod gp` a map,
> `N_r = #{k : cls k = r}`, and `μ : K → ℂ` with `∑_k ‖μ_k‖² = 1`.
> Define `A_r = ∑_{k : cls k = r} μ_k` and `Z_ν = ∑_r A_r · e(−νr/gp)`.
> Then `∑_{ν ∈ (ZMod gp)ˣ} ‖Z_ν‖² ≤ gp · max_r N_r`.

Proof (mathematical, from the G3 note §3, Steps 1–2): Parseval for `Z`
(`∑_{ν} ‖Z_ν‖² = gp · ∑_r ‖A_r‖²`), restriction to units (non-negative
terms dropped), and Cauchy–Schwarz per class
(`‖A_r‖² ≤ N_r · ∑_{k : cls k = r} ‖μ_k‖²`, summed over `r` with
`∑_r ∑_{k : cls k = r} ‖μ_k‖² = ‖μ‖₂² = 1`).

This draft formalises exactly that statement and nothing else.
It contains NO Pell numbers, NO SNF, NO kick coefficients, and NO
`dlib` objects. In particular it does NOT prove the class-count bound
`max_r N_r ≤ 2 · d₁ · R(gp)` (G3 note §4), does NOT prove `‖μ‖₂ = 1`
for the `dlib` weights (G3 note §3, Steps 0–1: Parseval for the finite
FFT plus `|Φ| = 1` from reality of `f`), and does NOT identify the
`dlib` profile with the bridge's `Btup`. Those are separate jobs:
the class bound, the `‖μ‖₂ = 1` step, and the identification G4.
See §8 for the full list of what remains.

## Verified source (current main, via GitHub connector only)

- Repository: `ChurilovMaksim/BGS`, branch `main`,
  HEAD `d87dce0d9277579568edfee6cffecbc96ea61024` (PR #76).
- `formalization/Bgs/LineBNAverageUnits.lean`, blob SHA
  `ae0e303d7a587dee86d0c8729ba121186d40789f`, re-fetched by THIS
  task with `get_file_contents` at the pinned HEAD. Definition used:
  - `nuAvgUnits {g' : ℕ} [NeZero g'] (B : ZMod g' → ℝ) : ℝ :=
      (∑ u : (ZMod g')ˣ, B (u : ZMod g')) / (Nat.totient g' : ℝ)`.
  Hence, for the bridge profile `B`, the units sum in the core lemma
  is `∑_{ν ∈ (ZMod g')ˣ} B ν = (Nat.totient g') * nuAvgUnits B`
  (by definition, after clearing the denominator; `φ(g') ≠ 0` for
  `g' ≥ 1`). The core lemma below proves a bound for the units sum
  of `‖Z_ν‖²`; turning it into a bound for `nuAvgUnits (Btup m ĝ)`
  additionally needs G4, the identification `Btup m ĝ ν = ‖Z_ν‖²`,
  which is NOT in main (see §8). Do not quote the core lemma as a
  bound for `nuAvgUnits` without stating G4 alongside it.
- `formalization/Bgs/LineBDerand.lean`, blob SHA
  `01fa6e63551542de55cce52cb9fb54c660f89b54`, as re-verified at the
  same HEAD in wave 8, task 4 (byte-identical between `6dbcc7a` and
  `d87dce0`): `gp m = (pellX m − 1).toNat / Nat.gcd …`. The `gp` in
  this draft is an arbitrary `ℕ` with `[NeZero gp]`; instantiating it
  to `gp m` is a one-line application, not part of the core lemma.
- `computations/verification/lineB/common/model.py` (SHA `ee6296ab…`)
  and `computations/verification/lineB/phase1/dlib.py` (SHA `af79ab79…`)
  are cited from the G3 note §1 (verified there at `d87dce0`); they
  were NOT re-fetched by this task, and nothing from them is imported
  here — the `dlib` objects enter only through the hypotheses of the
  core lemma, exactly as §7b intends.

## Design decisions (why the draft looks the way it does)

1. Residues are `ZMod gp`, not `Fin gp`. The G3 statement sums over
   `(ZMod gp)ˣ`, and main's `nuAvgUnits` sums over `(ZMod gp)ˣ`, so
   using `ZMod gp` throughout avoids a `Fin ≃ ZMod` transport lemma
   that the core lemma does not need. The price is paid once, in the
   orthogonality lemma (§2): the character is defined through
   `ZMod.val`, and the proof must reduce `val`-products modulo `gp`
   (see the comment on `charExp_orthogonality`).
2. Squared norms are `‖z‖ ^ 2` (real), via the norm on `ℂ`. The
   bridge to `Complex.normSq` (`‖z‖ ^ 2 = Complex.normSq z`, through
   `Complex.norm_eq_abs` and `Complex.normSq_eq_abs`) is an
   elaboration detail; the candidate lemma names in the comments are
   UNCHECKED guesses unless marked verified, and must be confirmed
   against Mathlib v4.33.1 at elaboration time.
3. The bound is stated for an arbitrary majorant `M` of the class
   sizes (`hM : ∀ r, classSize cls r ≤ M`), not for `max_r N_r`
   itself. This avoids `Finset.sup'` / `Finset.max'` API in the main
   theorem; the corollary with `M = max_r N_r` is a one-liner once
   `Finset.max'` (or `Finset.sup'`) is available, since `Fin gp` /
   `ZMod gp` is nonempty for `gp ≥ 1`. The G3 application then takes
   `M = 2 * d₁ * R(gp)` from §4 of the G3 note — again, not proved
   here.
4. `K` needs `[Fintype K]` (finite sums) and `[DecidableEq K]`
   (filtering by class). No other structure on `K` is assumed.
5. `import Mathlib` is deliberately broad for a draft. At elaboration
   it should be narrowed to the modules actually used (complex
   exponentials, `ZMod`, finite sums, roots of unity); narrowing is a
   mechanical step, not a mathematical gap.

## What is genuinely hard in Lean (not just tedious)

- (H1) Orthogonality (§2). The only step where `ZMod.val` arithmetic
  meets analysis: `ν.val * (r - s).val` must be reduced modulo `gp`
  before the geometric-sum argument applies, and the `r = s` vs
  `r ≠ s` case split needs `exp (2πi · k / gp) ≠ 1` for `gp ∤ k`
  (a primitive-root-of-unity fact). Expect several attempts.
- (H2) Parseval (§3). Expanding `‖∑_r A_r χ_r‖²` into a double sum
  needs `‖z‖² = z * star z` as a real number and a sum swap; the
  algebra is routine but the `ℂ`/`ℝ` coercion bookkeeping is fiddly.
  If Mathlib already has finite-DFT Parseval in usable form, use it
  instead — this draft does not assume any such lemma exists.
- (H3) Per-class Cauchy–Schwarz (§4). The step
  `‖∑ μ_k‖² ≤ N_r · ∑ ‖μ_k‖²` for complex `μ_k` goes through
  `‖∑ μ_k‖ ≤ ∑ ‖μ_k‖` (triangle) and real Cauchy–Schwarz
  `(∑ ‖μ_k‖)² ≤ N_r · ∑ ‖μ_k‖²`. Candidate real lemma names are
  flagged UNCHECKED in the comment; verifying them is the first
  elaboration step for §4.
- Tedious only: the fiber partition (§5, finite-sum bookkeeping),
  the units restriction (§6, `Units.val` injectivity + non-negativity),
  and the final assembly (§7, chaining inequalities).

-/

import Mathlib

open Finset

namespace G3Core

/-! ### §1. Definitions. -/

/-- Squared norm on `ℂ`, as a real number. All bounds in this file are
    stated in `sqNorm` to keep the `ℂ`/`ℝ` boundary in one place. -/
noncomputable def sqNorm (z : ℂ) : ℝ := ‖z‖ ^ 2

/-- The DFT character `e(−νr/gp)`, defined through `ZMod.val`.
    Since `ν.val, r.val ∈ [0, gp)`, this is a well-defined function of
    the `ZMod gp` elements (no quotient issue); the orthogonality proof
    must still reduce products modulo `gp` (see §2). -/
noncomputable def charExp {gp : ℕ} (ν r : ZMod gp) : ℂ :=
  Complex.exp (-(2 : ℂ) * (Real.pi : ℂ) * Complex.I
    * ((ν.val * r.val : ℕ) : ℂ) / (gp : ℂ))

/-- Class sum: sum of the weights over the fiber of `cls` above `r`. -/
noncomputable def classSum {K : Type*} [Fintype K] [DecidableEq K]
    {gp : ℕ} (μ : K → ℂ) (cls : K → ZMod gp) (r : ZMod gp) : ℂ :=
  ∑ k ∈ Finset.univ.filter (fun k => cls k = r), μ k

/-- Class size: number of modes in the fiber above `r`. -/
noncomputable def classSize {K : Type*} [Fintype K] [DecidableEq K]
    {gp : ℕ} (cls : K → ZMod gp) (r : ZMod gp) : ℕ :=
  (Finset.univ.filter (fun k => cls k = r)).card

/-- The DFT of the class sums: `Z_ν = ∑_r A_r · e(−νr/gp)`.
    Needs `[NeZero gp]` so that `ZMod gp` is a `Fintype` (for `gp = 0`,
    `ZMod 0 = ℤ` is infinite and the sum would not make sense). -/
noncomputable def dft {gp : ℕ} [NeZero gp] (A : ZMod gp → ℂ) (ν : ZMod gp) : ℂ :=
  ∑ r, A r * charExp ν r

/-! ### §2. Orthogonality of the characters. -/

/-- Orthogonality: summing `χ_ν(r) · conj(χ_ν(s))` over all `ν` picks
    out `r = s`, with value `gp`, and vanishes otherwise.
    PROOF IDEA (to be written out at elaboration): `χ_ν(r) * star (χ_ν(s))`
    equals `exp (-2πi · ν.val * ((r.val : ℤ) - (s.val : ℤ)) / gp)` after
    reducing the exponent modulo `gp` (using `exp (2πi · k) = 1` for
    integer `k` and periodicity of `exp` in the exponent); then the sum
    over `ν : ZMod gp` is a geometric sum over a primitive `gp`-th root
    of unity, equal to `gp` when the ratio is `1` (i.e. `r = s`) and to
    `(ζ^(gp) - 1)/(ζ - 1) = 0` otherwise (needs `ζ ≠ 1`, i.e. `gp ∤ k`).
    This is hard point (H1): expect the `ZMod.val` reduction modulo
    `gp` to take several attempts. -/
theorem charExp_orthogonality {gp : ℕ} [NeZero gp] (r s : ZMod gp) :
    ∑ ν : ZMod gp, charExp ν r * star (charExp ν s)
      = if r = s then (gp : ℂ) else 0 := by
  sorry

/-! ### §3. Parseval for the DFT. -/

/-- Parseval: the total squared norm of the DFT is `gp` times the total
    squared norm of the class sums.
    PROOF IDEA: expand `sqNorm (dft A ν) = ‖∑_r A_r χ_ν(r)‖²` as a double
    sum `∑_{r,s} A_r * star (A_s) * (χ_ν(r) * star (χ_ν(s)))` (needs
    `‖z‖² = z * star z` as reals — bridge via `Complex.normSq`, names
    UNCHECKED, see the header), swap the `ν`-sum inside, and apply §2.
    This is hard point (H2): routine algebra, fiddly `ℂ`/`ℝ` coercions. -/
theorem dft_parseval {gp : ℕ} [NeZero gp] (A : ZMod gp → ℂ) :
    ∑ ν : ZMod gp, sqNorm (dft A ν)
      = (gp : ℝ) * ∑ r, sqNorm (A r) := by
  sorry

/-! ### §4. Cauchy–Schwarz per class. -/

/-- Per-class Cauchy–Schwarz: the squared norm of a class sum is at most
    the class size times the sum of squared norms over the class.
    PROOF IDEA: `‖∑ μ_k‖ ≤ ∑ ‖μ_k‖` (triangle inequality for finite
    sums), then real Cauchy–Schwarz `(∑ ‖μ_k‖)² ≤ N_r · ∑ ‖μ_k‖²`
    (apply a real sum-Cauchy–Schwarz lemma with one factor constantly
    `1`; candidate names UNCHECKED — verifying them against
    Mathlib v4.33.1 is the first elaboration step for this lemma).
    This is hard point (H3). -/
theorem classSum_sqNorm_le {K : Type*} [Fintype K] [DecidableEq K]
    {gp : ℕ} (μ : K → ℂ) (cls : K → ZMod gp) (r : ZMod gp) :
    sqNorm (classSum μ cls r)
      ≤ (classSize cls r : ℝ)
        * ∑ k ∈ Finset.univ.filter (fun k => cls k = r), sqNorm (μ k) := by
  sorry

/-! ### §5. The fibers partition the modes. -/

/-- Summing the per-fiber squared norms over all residues recovers the
    total squared norm of `μ`. PROOF IDEA: finite-sum fiberwise
    regrouping (candidate: `Finset.sum_fiberwise_of_maps_to`, name
    UNCHECKED); the fibers are disjoint and cover `Finset.univ`. -/
theorem sum_fiber_sqNorm {K : Type*} [Fintype K] [DecidableEq K]
    {gp : ℕ} (μ : K → ℂ) (cls : K → ZMod gp) :
    ∑ r, ∑ k ∈ Finset.univ.filter (fun k => cls k = r), sqNorm (μ k)
      = ∑ k, sqNorm (μ k) := by
  sorry

/-! ### §6. Total bound for the class sums. -/

/-- If `‖μ‖₂² = 1` and every class has size at most `M`, then the total
    squared norm of the class sums is at most `M`.
    PROOF IDEA: chain §4 (per class) → sum over `r` → §5 (fibers
    partition) → `hμ` → `N_r ≤ M` pulled out of the sum
    (`Finset.sum_le_sum` + `Finset.sum_const` / `nsmul`). -/
theorem sum_classSum_sqNorm_le {K : Type*} [Fintype K] [DecidableEq K]
    {gp : ℕ} (μ : K → ℂ) (cls : K → ZMod gp) (M : ℕ)
    (hμ : ∑ k, sqNorm (μ k) = 1) (hM : ∀ r, classSize cls r ≤ M) :
    ∑ r, sqNorm (classSum μ cls r) ≤ (M : ℝ) := by
  sorry

/-! ### §7. Restriction from all residues to units. -/

/-- A sum of non-negative terms over the units is at most the sum over
    all residues. PROOF IDEA: the units embed into `ZMod gp` via
    `Units.val` (injective: `Units.val_injective`, name to confirm),
    so the units sum equals the sum over the image finset
    (`Finset.sum_image`), which is a sub-sum of the full sum by
    non-negativity (`Finset.sum_le_sum_of_subset_of_nonneg`, name to
    confirm). -/
theorem sum_units_le_total {gp : ℕ} [NeZero gp] (Z : ZMod gp → ℂ) :
    ∑ u : (ZMod gp)ˣ, sqNorm (Z (u : ZMod gp))
      ≤ ∑ ν : ZMod gp, sqNorm (Z ν) := by
  sorry

/-! ### §8 (of the proof). The portable core lemma. -/

/-- **Portable core lemma (G3 note §7b).** For weights `μ` with total
    squared norm `1` and a class map whose fibers all have size at most
    `M`, the units sum of the DFT squared norms is at most `gp * M`.
    PROOF IDEA: §7 (units ≤ total) → §3 (Parseval, total = `gp` times
    the class-sum total) → §6 (class-sum total ≤ `M`). -/
theorem core_bound {K : Type*} [Fintype K] [DecidableEq K]
    {gp : ℕ} [NeZero gp] (μ : K → ℂ) (cls : K → ZMod gp) (M : ℕ)
    (hμ : ∑ k, sqNorm (μ k) = 1) (hM : ∀ r, classSize cls r ≤ M) :
    ∑ u : (ZMod gp)ˣ, sqNorm (dft (classSum μ cls) (u : ZMod gp))
      ≤ (gp : ℝ) * (M : ℝ) := by
  sorry

/-- Total version (no units restriction), for direct use when the full
    DFT sum is what is needed. PROOF IDEA: §3 + §6. -/
theorem dft_total_bound {K : Type*} [Fintype K] [DecidableEq K]
    {gp : ℕ} [NeZero gp] (μ : K → ℂ) (cls : K → ZMod gp) (M : ℕ)
    (hμ : ∑ k, sqNorm (μ k) = 1) (hM : ∀ r, classSize cls r ≤ M) :
    ∑ ν : ZMod gp, sqNorm (dft (classSum μ cls) ν)
      ≤ (gp : ℝ) * (M : ℝ) := by
  sorry

end G3Core

/-! ### §9. Application to main (comments only — NOT formalised here)

The core lemma is deliberately standalone: it does not import any main
module, so that it can be elaborated and audited independently of the
project. Its application to the assembly runs as follows, with each
step labelled by the gap that owns it:

1. **Units sum = `φ(gp) · nuAvgUnits`.** In main (verified above),
   `nuAvgUnits B = (∑ u : (ZMod g')ˣ, B u) / φ(g')`. Hence the core
   lemma's left-hand side, for `B ν = sqNorm (Z ν)`, is exactly
   `(Nat.totient gp : ℝ) * nuAvgUnits B` (clearing the denominator;
   `φ(gp) > 0` for `gp ≥ 1`). This step is definitional in main.
2. **G4 (identification) — the real blocker.** The core lemma bounds
   `‖Z_ν‖²` where `Z` is the DFT of the `dlib` class sums. Main's
   `nuAvgUnits` is applied to `Btup m ĝ`, the bridge profile. The
   equality `Btup m ĝ ν = sqNorm (Z ν)` (and `kickMatInf` = the actual
   kick, which in main enters only as hypothesis `hTrU`) is NOT in
   main and is NOT proved here. Until G4 is discharged, the core lemma
   must not be quoted as a bound for `nuAvgUnits (Btup m ĝ)`.
3. **Class-count bound — §4 of the G3 note, not in this draft.**
   With `M = 2 * d₁ * R(gp)`, the proved G3 values are (G3 note §8):
   `S ≤ 784, 9216, 26896, 627200` at `m = 3, 4, 5, 6`, against
   thresholds `Deff · φ(D) / 2 = 2058, 13824, 2756840, 32928000`
   (margins `2.6×, 1.5×, 102×, 52×`; the binding case is `m = 4`).
   Formalising the class count needs the SNF certificates
   (`P · diag(d₁, d₂) · V⁻¹ = L^m − I`, `det P = −1`,
   `Q(second column) = 1`, `d₁ ∣ g'`, `d₂ = 2g'`) and the CRT root
   bounds (`R(gp) = 4, 8, 4, 16` at `m = 3..6`) — finite certificate
   checking plus a prime-power root-count lemma, separate from §§1–7.
4. **`‖μ‖₂ = 1` for the `dlib` weights — G3 note §3, Steps 0–1, not in
   this draft.** Needs reality of `f` (conjugation symmetry
   `c(0, −k) = conj (c(0, k))` from the `fCoeff` formula in main's
   `model.py` / `TraceStatement`), hence `|Φ| = 1` for every real `η`,
   hence Parseval for the finite 2-D FFT giving `∑ |μ_k|² = 1`.
   This is the only place the actual kick coefficients enter G3, and
   only through conjugation symmetry, not coefficient sizes.
5. **What remains for full G3 formalisation, in order:**
   (a) elaborate §§2–7 of this draft (hard points H1–H3 above);
   (b) formalise the SNF class-count bound (step 3);
   (c) formalise `‖μ‖₂ = 1` for `dlib` weights (step 4);
   (d) discharge G4 (step 2) — the step the G3 note identifies as the
   real blocker, harder than the `S`-bound itself;
   (e) assemble with G1 (radical draft, wave 8 revision: 495 lines,
   `primeFactors` restatement) and G2 (units draft, 398 lines) into
   the `hEquidistUnits` assembly (wave 5, task 4), whose remaining
   gaps after G3 are exactly G1, G2, G4, G5 (exact constant, separate),
   G6 (general `m`), G7 (real `X` with floors), G8 (docking with
   `nAverageTup_units` and re-verification at the then-current HEAD).
   None of (a)–(e) is claimed done by this draft.

-/
