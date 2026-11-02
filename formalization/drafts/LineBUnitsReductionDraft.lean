/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: draft, not built in this form; statement draft only.
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

/-!
# DRAFT ONLY — NOT A PROOF, NOT FOR MAIN

File: `bgs-breakthrough/lean-drafts/LineBUnitsReductionDraft.lean`
Task: wave 3, task 4 — draft Lean lemmas for the units reduction,
first step of the Lean lemma sequence toward `hEquidistUnits`.
Status: text draft only. `lake build` was NOT run (forbidden for this task),
no file in the repository was touched, nothing was pushed to `main`.
Every `sorry` below is an explicit placeholder, not a claim:
this file must not be cited as proved, and must not enter `main`
until every `sorry` is replaced and the axiom audit is clean
(standard axioms only, `sorryAx = 0`).

## Verified source (current main, via GitHub connector)

- Repository: `ChurilovMaksim/BGS`, branch `main`,
  HEAD `6dbcc7a0ed38d780ff7643bdb55917a9bc5efed1` (PR #75).
- `formalization/Bgs/LineBDerand.lean`, blob SHA
  `01fa6e63551542de55cce52cb9fb54c660f89b54` (unchanged from the
  previous HEAD `a562e0cf`), read with `get_file_contents` at that ref:
  - `pellX : Nat → Int`, `pellY : Nat → Int`, mutually recursive:
    `pellX 0 = 1`, `pellX (n+1) = 3 * pellX n + 8 * pellY n`,
    `pellY 0 = 0`, `pellY (n+1) = pellX n + 3 * pellY n`.
  - `Dm m = 2 * (pellX m - 1)` (an `Int`).
  - `gp m = (pellX m - 1).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat`.
  - `gprime_values`: `gp 1..10 = [2, 8, 14, 48, 82, 280, 478, 1632, 2786, 9512]`.
  - `D_values`: `Dm 1..8 = [4, 32, 196, 1152, 6724, 39200, 228484, 1331712]`.
- `formalization/Bgs/LineBNAverageBridge.lean`, blob SHA
  `3373aa6b3e73363913cf2d110bb2d8edab74bfa2`, §0, already proved in main:
  - `gp_pos : 1 ≤ m → 0 < gp m`.
  - `gp_dvd_Dm : 1 ≤ m → gp m ∣ (Dm m).toNat`.
  - `nu_mul`: an inverse of `N` mod `Dm` reduces to an inverse mod `gp`.
- `formalization/Bgs/LineBNAverageUnits.lean`, blob SHA
  `ae0e303d7a587dee86d0c8729ba121186d40789f`:
  - `nuAvgUnits B = (∑ u : (ZMod g')ˣ, B u) / (Nat.totient g' : ℝ)`.
  - `nAverageTup_units`: the general bridge with target `nuAvgUnits`
    and hypothesis `hEquidistUnits` (NOT proved there — it is the
    residue of TRACE-175).
- `formalization/Bgs/LineBNAverage.lean`, blob SHA
  `8b2ce39c146e071b1d52bd6d1acbe7996dbe948e`:
  - `window X D = (Finset.Ioc ⌊X⌋₊ ⌊2 * X⌋₊).filter (fun N => Nat.Coprime N D)`.
  - `winAvg W f = (∑ N ∈ W, f N) / W.card`.
  - `mem_window`: `N ∈ window X D → X < N ∧ N ≤ 2 * X ∧ Nat.Coprime N D`.

## Numerical checks (independent Python, integers — not proofs)

- Equal fibers of the units reduction, brute force:
  `m = 3`: `D = 196`, `g' = 14`, `φ(D) = 84`, `φ(g') = 6`,
  every fiber has exactly `14 = 84 / 6` elements;
  `m = 4`: `D = 1152`, `g' = 48`, `φ(D) = 384`, `φ(g') = 16`,
  every fiber has exactly `24 = 384 / 16` elements;
  `m = 5`: `D = 6724`, `g' = 82`, `φ(D) = 3280`, `φ(g') = 40`,
  every fiber has exactly `82 = 3280 / 40` elements.
- Radical equality `rad(D_m) = rad(g'_m)` (prime divisors coincide)
  for `m = 1..12`, e.g. `m = 6`: `{2, 5, 7}` on both sides.
- Window spread: for `m = 3..6`, every `X = 1..500`, with
  `N ∈ (X, 2X]`, `gcd(N, D_m) = 1`, `ν_N = N⁻¹ mod g'`,
  the counts of the units `ν` differ by at most `1`
  (maximum spread `1`, attained already at small `X`).
  A numerical check is not a proof; it only fixes the statement.

## Dependencies (proposed, to be confirmed at build time — not built here)

- `Bgs.LineBNAverage` — for `window`, `winAvg` only.
- `Bgs.LineBNAverageUnits` — for `nuAvgUnits` only.
- `Bgs.LineBNAverageBridge` — for `gp_pos`, `gp_dvd_Dm` only
  (do NOT re-prove them here).
- `Bgs.LineB.Derand` — for `Dm`, `gp` only.
  Do NOT re-define `pellX`/`pellY`/`Dm`/`gp` in this file:
  redefinition would silently change the object.
- `ZMod` units API (`ZMod.card_units`, `Units.map`); see the
  elaboration-risk notes on `redUnits` and on the totient card.

## Scope and the one open hypothesis

- `m ≥ 1` only, so `gp m > 0` (from main's `gp_pos`) and
  `gp m ∣ (Dm m).toNat` (from main's `gp_dvd_Dm`).
- The draft takes ONE hypothesis, `hCoprime`:
  `Nat.Coprime N (Dm m).toNat ↔ Nat.Coprime N (gp m)` for all `N`.
  This is equivalent to `rad(D_m) = rad(g'_m)`. It is NOT proved
  here: the odd-prime case follows in one line from
  `(x - 1)(x + 1) = 8y²` (M03), but the `p = 2` case is still open.
  It is passed as an EXPLICIT argument to every window lemma that
  needs it (§2–§3) — deliberately not a section variable, so that
  the conditionality is visible in each statement and cannot be
  silently dropped by a `sorry` proof. The units-reduction lemmas
  (§1) do NOT need it.
- `X : ℝ` is the window parameter of main's `window`; the counting
  lemmas are stated for `window X (Dm m).toNat`, i.e. with the
  `⌊X⌋₊` / `⌊2X⌋₊` floors of main's definition, not for the
  informal interval `(X, 2X]`. For integer `X` the two agree.
-/

import Bgs.LineBNAverage
import Bgs.LineBNAverageUnits
import Bgs.LineBNAverageBridge
import Bgs.LineB.Derand

namespace Bgs.Breakthrough.UnitsReduction

open Bgs.LineB.Derand Bgs.LineB.NAverageBridge Bgs.LineB.NAverage
open Bgs.LineB.NAverageUnits

section Setup

variable {m : ℕ} (hm : 1 ≤ m)

/-- `gp m` is positive (main's `gp_pos`), as a `NeZero` instance
    for `ZMod (gp m)`. -/
instance neZero_gp : NeZero (gp m) := ⟨(gp_pos hm).ne'⟩

/-! ## 1. The units reduction map and its fibers

The map is the reduction of a unit mod `D_m` to a unit mod `g'_m`.
It is a group homomorphism because reduction mod a divisor is a
ring homomorphism; its fibers are cosets of its kernel, hence all
of the same cardinality. The mathematics here is standard group
theory. The genuinely hard step is surjectivity (L2 below).
-/

/-- Reduction of units mod `g'`. Implemented as `Units.map` of the
    canonical ring hom `ZMod D →+* ZMod g'`.

    ELABORATION RISK (not a mathematical gap): the exact Mathlib
    constructor and argument order for the reduction ring hom
    (`ZMod.castHom`) must be confirmed at elaboration. If it differs,
    replace this definition by the Mathlib reduction hom; the lemmas
    below are stated through `redUnits_val` (L1), so they survive
    such a replacement. -/
noncomputable def redUnits (D g' : ℕ) (hdvd : g' ∣ D) :
    (ZMod D)ˣ →* (ZMod g')ˣ :=
  Units.map (ZMod.castHom hdvd)

/-- The reduction map acts on representatives by `· % g'`.
    Proof route: `ZMod.castHom` applied to a `Nat.cast`, then
    `ZMod.val_natCast` / `Nat.mod_eq_of_lt` on the representative.
    This is the only property of `redUnits` the later lemmas use. -/
theorem redUnits_val (D g' : ℕ) (hdvd : g' ∣ D) (u : (ZMod D)ˣ) :
    (redUnits D g' hdvd u : ZMod g') = ((u.val : ZMod g')) := by
  sorry

/-- L1 — the reduction map for our parameters.
    Specialisation of `redUnits` to `D = (Dm m).toNat`, `g' = gp m`,
    using main's `gp_dvd_Dm`. -/
noncomputable def redUnits_m : (ZMod (Dm m).toNat)ˣ →* (ZMod (gp m))ˣ :=
  redUnits (Dm m).toNat (gp m) (gp_dvd_Dm hm)

/-- L2 — SURJECTIVITY: every unit mod `g'` lifts to a unit mod `D`.
    This is the genuinely hard step of §1, and the step most likely
    to be missing from Mathlib in usable form.

    Mathematical proof idea (prime avoidance): given `a` coprime to
    `g'`, choose `b ≡ a (mod g')` avoiding every prime divisor `p`
    of `D`: if `p ∣ g'` then `p ∤ a` already forces `p ∤ b`; if
    `p ∤ g'` then, as `t` ranges mod `p`, `a + t·g'` avoids one
    residue class mod `p`, and CRT over the finitely many such `p`
    picks such a `t` simultaneously. In Lean this is a CRT /
    prime-avoidance argument over the prime divisors of `D`; there
    is no shortcut through group theory alone, because surjectivity
    is not formal: the map on all residues is surjective, but the
    lift must stay a unit.

    BEFORE proving this by hand: search Mathlib for an existing
    surjectivity lemma for `(ZMod n)ˣ → (ZMod m)ˣ` under `m ∣ n`
    (candidate names around `ZMod.units` / `ZMod.castHom`); if one
    exists, L2 is a one-line application and the hard step vanishes.
    Do not silently assume it exists — the draft does not. -/
theorem redUnits_m_surjective :
    Function.Surjective (redUnits_m (m := m) hm) := by
  sorry

/-- L3 — equal fibers. Once L2 holds, `redUnits_m` is a surjective
    group homomorphism between finite groups, so every fiber is a
    coset of the kernel and all fibers have cardinality `|ker|`.

    Proof route (standard, tedious not hard): a fiber over `v` is
    the coset `u • ker` for any preimage `u` of `v`
    (`MonoidHom` fiber / preimage-of-singleton API), and a coset
    has the cardinality of the subgroup. No number theory. -/
theorem redUnits_m_fiber_card (u v : (ZMod (gp m))ˣ) :
    ((redUnits_m (m := m) hm) ⁻¹' {u}).card
      = ((redUnits_m (m := m) hm) ⁻¹' {v}).card := by
  sorry

/-- L4 — fiber cardinality in totients. `|ker| = φ(D) / φ(g')`:
    `|(ZMod n)ˣ| = φ(n)` (Mathlib `ZMod.card_units` — name to be
    confirmed at elaboration), surjectivity (L2) gives
    `φ(D) = |ker| · φ(g')`, and division is exact.

    Numerical instances (checked, §0 header): `m = 3`: `14`;
    `m = 4`: `24`; `m = 5`: `82`. -/
theorem redUnits_m_fiber_card_totient (u : (ZMod (gp m))ˣ) :
    ((redUnits_m (m := m) hm) ⁻¹' {u}).card
      = Nat.totient (Dm m).toNat / Nat.totient (gp m) := by
  sorry

/-- L5 — complete-block corollary, in counting form. Over one full
    block of `D` consecutive residues, each unit residue mod `g'`
    occurs exactly `φ(D) / φ(g')` times among the units mod `D`.

    Proof route: `N ∈ Finset.range D` with `Nat.Coprime N D`
    corresponds bijectively to `(ZMod D)ˣ` via `ZMod.val`
    (`ZMod.unitsEquivCoprime`-style API, name to be confirmed),
    and `N % g' = r` corresponds to lying in the fiber over the
    unit with representative `r` by L1; then apply L4. -/
theorem block_count (r : ℕ) (hr : Nat.Coprime r (gp m)) :
    ((Finset.range (Dm m).toNat).filter
      (fun N => Nat.Coprime N (Dm m).toNat ∧ N % gp m = r)).card
      = Nat.totient (Dm m).toNat / Nat.totient (gp m) := by
  sorry

/-! ## 2. Window counts

The window is main's `window X (Dm m).toNat`: the consecutive
integers `(⌊X⌋₊, ⌊2X⌋₊]` filtered by `Nat.Coprime N (Dm m).toNat`.
Under `hCoprime` this filter is the same as `Nat.Coprime N (gp m)`,
so the window sees exactly the units mod `g'`, and the inverse map
`N ↦ ν_N = N⁻¹ mod g'` is a bijection on those units. The counting
is then counting consecutive integers by residue class mod `g'`,
which is where the spread `≤ 1` comes from — not from any deep
equidistribution theorem.
-/

/-- Count of window elements in residue class `r` mod `g'`. -/
noncomputable def cntRes (X : ℝ) (r : ℕ) : ℕ :=
  ((window X (Dm m).toNat).filter (fun N => N % gp m = r)).card

/-- Count of window elements with inverse `ν`: since
    `ν_N = ν` iff `N ≡ ν⁻¹ (mod g')`, this is `cntRes` at the
    representative of `ν⁻¹`. -/
noncomputable def cntUnit (X : ℝ) (ν : (ZMod (gp m))ˣ) : ℕ :=
  cntRes (m := m) X (ν⁻¹ : ZMod (gp m)).val

/-- The canonical inverse of `N` mod `g'`, as an element of
    `ZMod (gp m)`. On the window (where `N` is coprime to `g'`
    by `hCoprime`) this is a genuine inverse; off the window it
    is the `ZMod` inverse, which is `0` for non-units — the lemma
    `nuOf_mul` is therefore stated only on the window. -/
noncomputable def nuOf (N : ℕ) : ZMod (gp m) := (N : ZMod (gp m))⁻¹

/-- On the window, `ν_N` inverts `N`. Proof route: `N` coprime to
    `g'` (by `mem_window` + `hCoprime`) gives `(N : ZMod g')` a unit
    (`ZMod.unitOfCoprime`), and a unit times its inverse is `1`. -/
theorem nuOf_mul (X : ℝ)
    (hCoprime : ∀ N : ℕ,
      Nat.Coprime N (Dm m).toNat ↔ Nat.Coprime N (gp m))
    {N : ℕ} (hN : N ∈ window X (Dm m).toNat) :
    nuOf (m := m) N * (N : ZMod (gp m)) = 1 := by
  sorry

/-- Identification of the inverse-count with the residue-count:
    `ν_N = ν` (as a unit) iff `N % g' = ν⁻¹.val`. Proof route:
    `nuOf_mul` + uniqueness of inverses in `ZMod g'` on the unit
    subgroup, plus `ZMod.val` of a product. -/
theorem cntUnit_eq_filter_nuOf (X : ℝ)
    (hCoprime : ∀ N : ℕ,
      Nat.Coprime N (Dm m).toNat ↔ Nat.Coprime N (gp m))
    (ν : (ZMod (gp m))ˣ) :
    cntUnit (m := m) X ν
      = ((window X (Dm m).toNat).filter
          (fun N => nuOf (m := m) N = (ν : ZMod (gp m)))).card := by
  sorry

/-- L6 — residue spread over a consecutive interval. For any
    `a < b` and any residues `r s` mod `g'`, the numbers of
    `n ∈ (a, b]` with `n % g' = r` resp. `= s` differ by at most `1`.

    Proof idea: write `(a, b]` as complete blocks of length `g'`
    plus a remainder interval of length `< g'`; each residue gets
    the same number of hits from the complete blocks, and at most
    one hit from the remainder. This is the second elaboration-heavy
    step: no ready-made Mathlib counting lemma for
    `Finset.Ioc`-by-residue was identified in this draft, so prove
    it by induction on `b - a` or by the block decomposition, and
    expect the induction / `Finset` bookkeeping to take several
    attempts. It contains no new mathematics. -/
theorem interval_residue_spread {g' a b : ℕ} (hg' : 0 < g')
    (r s : ℕ) :
    (((Finset.Ioc a b).filter (fun n => n % g' = r)).card : ℤ)
      - (((Finset.Ioc a b).filter (fun n => n % g' = s)).card : ℤ)
      |>.natAbs ≤ 1 := by
  sorry

/-- L7 — WINDOW SPREAD (the main window lemma). Counts of the
    units `ν` over the window differ by at most `1`.

    Proof assembly: under `hCoprime`, `mem_window` shows every
    window element is coprime to `g'`, so the window is partitioned
    by the unit residues (via `cntUnit_eq_filter_nuOf`); the window
    is a consecutive interval (`Ioc ⌊X⌋₊ ⌊2X⌋₊` filtered by a
    coprimality condition that, under `hCoprime`, only removes
    non-unit residues); apply L6 to the two residues `ν⁻¹.val`,
    `μ⁻¹.val`. The filter step needs care: L6 counts all residues
    in the interval, L7 counts only unit residues, but non-unit
    residues contribute `0` to the window count because the window
    filter removes them — this is exactly where `hCoprime` is used.

    Numerical instances (checked, §0 header): spread `≤ 1` for
    `m = 3..6`, `X = 1..500`. -/
theorem window_units_spread (X : ℝ)
    (hCoprime : ∀ N : ℕ,
      Nat.Coprime N (Dm m).toNat ↔ Nat.Coprime N (gp m))
    (ν μ : (ZMod (gp m))ˣ) :
    ((cntUnit (m := m) X ν : ℤ) - (cntUnit (m := m) X μ : ℤ)).natAbs ≤ 1 := by
  sorry

/-- L8 — window size lower bound (needed to turn the spread into a
    rate). With `R = rad(D_m)` (product of distinct prime divisors)
    and `ρ = φ(D_m) / D_m`, the window has
    `|W| ≥ φ(R) · (X / R - 1)`, hence `|W| ≥ ρ·X / 2` for `X ≥ 2R`.
    Proof route: the window is an interval of length `≈ X` filtered
    by coprimality to `D_m`; count via complete blocks of length `R`
    (each block contributes exactly `φ(R)` coprime residues) plus a
    remainder bounded by `φ(R)`. This is standard block counting;
    its formalisation goes through L5-style arguments with `R` in
    place of `D`. Stated here as the lemma the S-route corollary
    needs; its proof is not attempted in this draft.
    (`Nat.radical` name / definition to be confirmed at elaboration.) -/
theorem window_card_lower (X : ℝ) (hX : 2 * (Nat.radical (Dm m).toNat : ℝ) ≤ X) :
    ((window X (Dm m).toNat).card : ℝ)
      ≥ (Nat.totient (Dm m).toNat : ℝ) / (Dm m).toNat * X / 2 := by
  sorry

/-! ## 3. S-route corollary: what the window lemma gives, and what it does not

From L7 alone, with `B ≥ 0`, the window average differs from the
units average by at most `(∑_ν B ν) / |W|`: indeed, writing both
averages over the unit partition of the window, the difference is
`∑_ν (cnt_ν / |W| - 1 / φ) · B ν`, and L7 plus `∑_ν cnt_ν = |W|`
forces `|cnt_ν / |W| - 1 / φ| ≤ 1 / |W|` for every `ν`.
This is the S-route. It is the whole content the window lemma
delivers for `hEquidistUnits`; the rest is about the size `S`
of the profile sum, which the window lemma says nothing about.
-/

/-- S-route corollary (conditional on `hCoprime`, `L7`, `L8`).
    `B` is the squared profile on units; `B ≥ 0` is used. -/
theorem winAvg_sub_nuAvgUnits_le (X : ℝ)
    (hCoprime : ∀ N : ℕ,
      Nat.Coprime N (Dm m).toNat ↔ Nat.Coprime N (gp m))
    (B : ZMod (gp m) → ℝ) (hBnn : ∀ ν, 0 ≤ B ν)
    (hW : (window X (Dm m).toNat).Nonempty) :
    |winAvg (window X (Dm m).toNat) (fun N => B (nuOf (m := m) N))
      - nuAvgUnits (B ∘ (fun u : (ZMod (gp m))ˣ => (u : ZMod (gp m))))|
      ≤ (∑ u : (ZMod (gp m))ˣ, B (u : ZMod (gp m)))
        / (window X (Dm m).toNat).card := by
  sorry

end Setup

/-! ## 4. What is still missing for the full `hEquidistUnits`

The window lemma (L7) does NOT close `hEquidistUnits` in the form
stated in main's `nAverageTup_units`,
`|winAvg - nuAvgUnits| ≤ D · min(s0^{2m}, Deff) / X`.
What remains, in order:

1. `hCoprime` itself — the `p = 2` case of `rad(D_m) = rad(g'_m)`.
   Until it is proved, L7–L8 and the corollary are conditional.
2. L2 surjectivity, if Mathlib has no ready-made units-lifting lemma
   (see the note on L2). L3–L5 depend on it.
3. L6 interval-residue counting formalised (block decomposition or
   induction on interval length; elaboration-heavy, no new maths).
4. The Deff branch: the S-route gives `|diff| ≤ S / |W|` with
   `S = ∑_ν B ν`. The `s0^{2m}` branch closes from `S ≤ φ(g')·s0^{2m}`
   (trivial, from `|Z| ≤ s0^m`) plus L8 — with a constant of order
   `g'`, not the bridge's `D_m` (M03 C-sharp: `4g'/X · s0^{2m}` for
   `X ≥ 4g'`). The `Deff` branch does NOT close this way: it needs
   `S ≤ Deff · φ(D_m)`, which is FALSE in general — wave 2, task 3
   killed it on model profiles (e.g. `m = 4`, uniform `ĝ` on 9 points:
   asymptotic failure factor `≈ 1.92`; `m = 6`, uniform on 10 points:
   factor up to `3.50`). So the Deff branch needs either an input
   about the ACTUAL kick `ĝ` (compute `S` for the real 32-mode kick
   from current main and compare with the threshold), or a
   correlation argument using that `δ_ν` and `B(ν)` are not
   adversarially aligned. The window lemma alone cannot supply it.
5. The exact constant: the bridge's claimed `D_m · min(...) / X`
   versus the first error term of the bridge carries the known
   `≈ 2π` discrepancy (bridge header, `nAverageTup_units` header);
   L7 does not resolve it — it is a separate analytic-constant
   problem, not a counting problem.
6. Outside `hEquidistUnits` proper (not closed by this draft at all):
   the `kickMatInf` identification with the real quantum kick, and
   the analytic layer of TRACE-175 beyond the window average.

## What is NOT in this draft

- No proof of any statement above is complete: every proof is `sorry`.
- No redefinition of main's objects, no change to any main module,
  no import of the full `Bgs` aggregator.
- No statement about `BGS-BGS-001`, `TRACE-005`, or RMT statistics.
  A counting lemma about units is not a spectral theorem.
- The `m = 0` case is excluded (`gp 0 = 0`, `Dm 0 = 0` in main's
  definitions; the units group `ZMod 0` is `ℤ` and the whole
  reduction picture degenerates).
-/

end Bgs.Breakthrough.UnitsReduction
