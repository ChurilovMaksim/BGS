/-! BREAKTHROUGH DRAFT — research record, not a theorem.
    Source: BGS breakthrough program (Nov 2026), wave notes in evidence/breakthrough/methods/.
    Status: draft; built counterpart LemmaYSharedBaseProbe.lean (1150 s, 0 errors, 34 sorry).
    Not imported by formalization/Bgs.lean. Registry status unchanged. -/

import Bgs.LineBDerand
/-! DRAFT ONLY — NOT A PROOF, NOT FOR MAIN. Wave 28, task 4: shared-base
refactor for the Lemma Y Lean assembly.

Problem it solves (wave 26, task 5 assembly draft, 216 lines):
milestones 1–3 each define their own copies of `seqFrom`, `IsFix`,
`classSum`, `seqMultiset`, `perClassMultiset`, `IsDihedral` under
`LemmaYM1` / `LemmaYM2` / `LemmaYM3`, so the assembly theorems could
only take the milestone results as hypotheses restated over yet
another copy. This file defines the vocabulary ONCE, in namespace
`Bgs.Breakthrough.LemmaY`, restates every milestone theorem over it,
and states the three assembly theorems so they reference the
restated theorems directly (no hypothesis plumbing).

Status: every proof is `sorry`; this file states the refactor, it
does not prove any milestone theorem and does not prove the
transport from the milestone files to the restated theorems.
Do not cite as proved, do not enter `main` until every `sorry` is
replaced and `sorryAx = 0`.

## What is shared, and what is not

Shared (bodies text-identical across all three milestone drafts,
verified by direct comparison): `seqFrom`, `IsFix`, `classSum`,
`seqMultiset`, `perClassMultiset`, `IsDihedral`. Milestone-only
definitions, hoisted here too so the restatements are self-contained:
`block` (milestone 2, stage 5) and `StabM` (milestone 3, stage 6).
No object from main is redefined: `pellX`, `pellY`, `Dm`, `gp`,
`pellQ`, `pellP` are imported from `Bgs.LineB.Derand` (flat import
on line 1, dotted namespace opened below — wave 20/21 resolution).
In the test copy, which has no Derand module, replace the import
with Mathlib plus stubs, as the M1/M3 fixed-copy probes did.

## Elaboration fixes applied (from the fixed copies)

The restated statements use the FIXED forms, not the draft forms:
(1) import on line 1 (the import-after-doc-comment defect killed
all three drafts as written); (2) the `π r` mismatch fixed by
binding `r : Fin t` with `.val` on the class sums / per-class
multisets in `componentY_mod3`, `componentY_mod3pow`,
`componentY_mod2pow`, `pattern_mod32`, `pattern_lemma`, `pi2_pi3`,
`lemmaY_modD` (the draft bound `r : ℕ` from `classSum` /
`perClassMultiset` and then applied `π : Fin t → Fin t` to it,
which is ill-typed; mathematical meaning unchanged);
(3) `bijective_tau` fixed with the ascribed constructor
`(⟨σ i % m, Nat.mod_lt _ hm⟩ : Fin m)` plus a new `hm : 0 < m`
hypothesis (the draft's `by omega` cannot prove `σ i % m < m`
for variable `m`, and the anonymous constructor had no
determinable expected type).

## Transport (NOT proved here)

Each restated theorem below is the corresponding milestone theorem
with its vocabulary replaced by the shared vocabulary. Because the
milestone definition bodies are text-identical to the shared ones,
the transport is expected to be definitional (`rfl`-style) after
the milestones are refactored onto this base — but that is NOT
proved here, and each restated theorem therefore carries its own
`sorry`. Discharging the restatements from the milestone files is
the remaining refactor step; until then, the assembly theorems in
§5 are conditional on the restated theorems, not on the milestone
files themselves. Build status of the fixed copies (waves 19/23):
M1 and M3 build as fixed copies (0 errors, sorry only); the M2
fixed copy exists in the test copy (wave 25).

## What is NOT in this file

No proof of any statement; no stages beyond the milestones' own
scope; no exact Pcarry (exact-integer class sums are future work —
see `exact_perclass_from_modD`); no G1 at `f ≥ 3`, no general
Lemma PC, no G4b, no 152, no `BGS-BGS-001`, no `TRACE-005`, no
`hEquidistUnits`, no RMT statistics; `m = 0` excluded throughout.
-/
namespace Bgs.Breakthrough.LemmaY

open Bgs.LineB.Derand

/-! ## §1 — Shared vocabulary (one copy for all milestones) -/

/-- Recurrence sequence with initial values `a, b` over `ZMod q`.
Definitional: `seqFrom a b (n + 2) = 6 * seqFrom a b (n + 1) - seqFrom a b n`. -/
def seqFrom {q : Nat} (a b : ZMod q) : ℕ → ZMod q
  | 0 => a
  | 1 => b
  | n + 2 => 6 * seqFrom a b (n + 1) - seqFrom a b n

/-- `Fix_m mod q`: a recurrence sequence that is `m`-periodic. -/
def IsFix {q : Nat} (m : Nat) (y : ℕ → ZMod q) : Prop :=
  ∃ a b : ZMod q, y = seqFrom a b ∧ ∀ i, y (i + m) = y i

/-- Class sums `Y_r(y)` over `range m`, class `i ≡ r (mod t)`. -/
def classSum {q : Nat} (m t : Nat) (y : ℕ → ZMod q) (r : ℕ) : ZMod q :=
  ∑ i ∈ (Finset.range m).filter (fun i => i % t = r), y i

/-- Global multiset of a sequence over one period. -/
def seqMultiset {q : Nat} (m : Nat) (y : ℕ → ZMod q) : Multiset (ZMod q) :=
  Multiset.ofList ((List.range m).map y)

/-- Per-class multiset `M_r` over one period, class `i ≡ r (mod 4)`. -/
def perClassMultiset {q : Nat} (m : Nat) (y : ℕ → ZMod q) (r : ℕ) :
    Multiset (ZMod q) :=
  Multiset.ofList (((List.range m).filter (fun i => i % 4 = r)).map y)

/-- Dihedral permutation of `t` classes: a shift, or a reflection
followed by a shift. -/
def IsDihedral {t : Nat} (π : Fin t → Fin t) : Prop :=
  ∃ b : Fin t, (∀ r, π r = r + b) ∨ (∀ r, π r = -r + b)

/-- Block `B_s(T,D) = T·c_s + D·e_s`, `(c₀,c₁) = (1,3)`,
`(e₀,e₁) = (0,1)` (milestone 2, stage 5). -/
def block {Q : Nat} (T D : ZMod Q) (s : ℕ) : ZMod Q :=
  T * seqFrom 1 3 s + D * seqFrom 0 1 s

/-- `δ` stabilises the per-class multisets of `p`
(milestone 3, stage 6). -/
def StabM {q : Nat} (m : Nat) (p : ℕ → ZMod q) (δ : Fin 4 → Fin 4) : Prop :=
  ∀ r, perClassMultiset m p (δ r).val = perClassMultiset m p r

/-! ## §2 — Milestone 1 restated (stages 0–2: Pell, setup, odd component)

Source: `LineBLemmaYMilestone1Draft.lean` (wave 15). Proofs are the
milestone's, transported onto §1; every proof here is `sorry`
pending that transport. -/

/-- T0.1a (Pell identity, general form of main's finite `pell_id`). -/
theorem pell_id_all (m : Nat) :
    pellX m * pellX m - 8 * pellY m * pellY m = 1 := by
  sorry

/-- T0.1b (factored form). -/
theorem pell_factor (m : Nat) :
    (pellX m - 1) * (pellX m + 1) = 8 * pellY m * pellY m := by
  sorry

/-- T0.1c (positivity, needed before any `toNat` step). -/
theorem pell_pos {m : Nat} (hm : 1 ≤ m) : 1 ≤ pellX m ∧ 1 ≤ pellY m := by
  sorry

/-- T0.1d (Pell formula C1, in main's own `pellQ` / `pellP` form):
odd `m` gives `gp m = pellQ m`, even `m` gives `gp m = 4 * pellP m`. -/
theorem pellC1 {m : Nat} (hm : 1 ≤ m) :
    (m % 2 = 1 → gp m = (pellQ m).toNat) ∧
    (m % 2 = 0 → gp m = 4 * (pellP m).toNat) := by
  sorry

/-- T0.2 (LTE: `v₂(D_m)` depends only on `v₂(m)`). -/
theorem lte_v2 {m : Nat} (hm : 1 ≤ m) :
    Nat.factorization (Dm m).toNat 2 =
      if m % 2 = 1 then 2 else 2 * Nat.factorization m 2 + 3 := by
  sorry

/-- T0.4 (radical lemma, primeFactors restatement: `Nat.radical`
does not exist in Mathlib, so `rad(D_m) = rad(gp)` is stated as
equality of prime-factor lists). -/
theorem radical_eq {m : Nat} (hm : 1 ≤ m) :
    (Dm m).toNat.primeFactors = (gp m).primeFactors := by
  sorry

/-- T1.1b (determination by initial values). Any sequence satisfying
the recurrence and `m`-periodicity is `seqFrom (y 0) (y 1)`. -/
theorem fix_eq_seqFrom {q m : Nat} (y : ℕ → ZMod q)
    (hrec : ∀ n, y (n + 2) = 6 * y (n + 1) - y n)
    (hper : ∀ i, y (i + m) = y i) :
    y = seqFrom (y 0) (y 1) := by
  sorry

/-- T1.2 (class-sum dot identity). If `z` is constant on each
`+t`-class (with class values `zbar`), then the full dot product
splits as a dot product of `zbar` with the class-sum vector `Y`. -/
theorem classSum_dot {q m t : Nat} (ht : t ∣ m) (ht0 : 0 < t)
    (y z : ℕ → ZMod q) (zbar : ℕ → ZMod q)
    (hconst : ∀ i, z i = zbar (i % t)) :
    ∑ i ∈ Finset.range m, z i * y i =
      ∑ r ∈ Finset.range t, zbar r * classSum m t y r := by
  sorry

/-- T2.1 (vanishing for `p ∤ 24`: component Lemma Y is trivial there,
all class sums are 0, so any `π` works). -/
theorem vanishing {m p e : Nat} (hm : 1 ≤ m) (hp : p.Prime)
    (hp2 : p ≠ 2) (hp3 : p ≠ 3)
    (y : ℕ → ZMod (p ^ e)) (hfix : IsFix m y) :
    ∀ r, classSum m (Nat.gcd m 4) y r = 0 := by
  sorry

/-- T2.2a (mod-3 period-4 form). For `4 ∣ m`, every `Fix_m mod 3`
sequence satisfies `y (i + 2) = -y i`. -/
theorem mod3_period4 {m : Nat} (hm : 4 ∣ m)
    (y : ℕ → ZMod 3) (hfix : IsFix m y) :
    ∀ i, y (i + 2) = -y i := by
  sorry

/-- T2.2b (mod-3 classification into 3 types). A 4-vector of the
form `(a, b, -a, -b)` over `𝔽₃` has multiset `{0⁴}`, `{0², 1, 2}`,
or `{1², 2²}`. -/
theorem mod3_types (v : Fin 4 → ZMod 3) (h2 : v 2 = -v 0) (h3 : v 3 = -v 1) :
    Multiset.ofList [v 0, v 1, v 2, v 3] = {0, 0, 0, 0} ∨
    Multiset.ofList [v 0, v 1, v 2, v 3] = {0, 0, 1, 2} ∨
    Multiset.ofList [v 0, v 1, v 2, v 3] = {1, 1, 2, 2} := by
  sorry

/-- T2.2c (equal mod-3 multisets ⇒ `D₄`-related). -/
theorem mod3_D4 (v w : Fin 4 → ZMod 3)
    (hv2 : v 2 = -v 0) (hv3 : v 3 = -v 1)
    (hw2 : w 2 = -w 0) (hw3 : w 3 = -w 1)
    (h : Multiset.ofList [v 0, v 1, v 2, v 3] =
      Multiset.ofList [w 0, w 1, w 2, w 3]) :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧ ∀ r, w r = v (π r) := by
  sorry

/-- T2.3 (mod-3 component Lemma Y: stage-2 assembly). FIXED FORM:
`r : Fin 4` with `.val` on both class sums (draft form was
ill-typed). The degenerate subcase `3 ∣ m/4` (i.e. `12 ∣ m`) makes
class sums vanish mod 3 and the claim trivial — this is exactly
why stage 3 (P3′) needs the top digit, not the mod-3 class sum. -/
theorem componentY_mod3 {m : Nat} (hm : 4 ∣ m)
    (y y' : ℕ → ZMod 3) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧
      ∀ r : Fin 4, classSum m 4 y' r.val = classSum m 4 y (π r).val := by
  sorry

/-! ## §3 — Milestone 2 restated (stages 3–5: P3′, P2 uniform, pattern lemma)

Source: `LineBLemmaYMilestone2Draft.lean` (wave 16). Proofs are the
milestone's, transported onto §1; every proof here is `sorry`
pending that transport. Cross-modulus `ZMod` casts in T3.1/T3.2/T4.2
were flagged UNCHECKED in the draft and resolved by the wave-20
elaboration probe. -/

/-- T0.3 (`v₃(D_m) = 2f₀`). -/
theorem v3_Dm {m : Nat} (hm : 4 ∣ m) :
    Nat.factorization (Dm m).toNat 3 =
      2 * (1 + Nat.factorization (m / 4) 3) := by sorry

/-- T3.1a (scaling, divisibility). Every `Fix_m mod 3^{2f₀}` vector
has all entries divisible by `3^{f₀}`. -/
theorem scaling_div {m f₀ : Nat} (hm : 4 ∣ m)
    (hf : f₀ = 1 + Nat.factorization (m / 4) 3)
    (y : ℕ → ZMod (3 ^ (2 * f₀))) (hfix : IsFix m y) :
    ∀ i, (3 ^ f₀ : ZMod (3 ^ (2 * f₀))) ∣ y i := by sorry

/-- T3.1b (scaling, divided sequence). Division by `3^{f₀}` gives a
bijection `Fix_m mod 3^{2f₀} ≃ Fix_m mod 3^{f₀}` preserving
multisets. -/
theorem scaling_bij {m f₀ : Nat} (hm : 4 ∣ m)
    (hf : f₀ = 1 + Nat.factorization (m / 4) 3)
    (y : ℕ → ZMod (3 ^ (2 * f₀))) (hfix : IsFix m y) :
    ∃ y₁ : ℕ → ZMod (3 ^ f₀), IsFix m y₁ ∧
      ∀ i, y i = ((3 ^ f₀ : ℕ) : ZMod (3 ^ (2 * f₀))) *
        ((y₁ i).val : ZMod (3 ^ (2 * f₀))) := by sorry

/-- T3.2 (top digit). For `y₁ ∈ Fix_m mod 3^{f₀}`, `Y′_r` is
divisible by `3^{f₀-1}` and its top digit is `Z′_r = n₀·v_r`. -/
theorem top_digit {m f₀ : Nat} (hm : 4 ∣ m)
    (hf : f₀ = 1 + Nat.factorization (m / 4) 3) (hf0 : 1 ≤ f₀)
    (y₁ : ℕ → ZMod (3 ^ f₀)) (hfix : IsFix m y₁) :
    ∃ v : Fin 4 → ZMod 3, v 2 = -v 0 ∧ v 3 = -v 1 ∧ ∀ r,
      ((classSum m 4 y₁ r).val / 3 ^ (f₀ - 1)) % 3 =
        (((m / 4) / 3 ^ (f₀ - 1)) % 3 : ℕ) * (v ⟨r % 4, by omega⟩).val
        % 3 := by sorry

/-- T3.3 (component Lemma Y mod 3^e). Assembly of T3.1 + T3.2 +
T2.2. FIXED FORM: `r : Fin 4` with `.val` (draft form ill-typed). -/
theorem componentY_mod3pow {m f₀ : Nat} (hm : 4 ∣ m)
    (hf : f₀ = 1 + Nat.factorization (m / 4) 3)
    (y y' : ℕ → ZMod (3 ^ (2 * f₀))) (hfix : IsFix m y)
    (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧
      ∀ r : Fin 4, classSum m 4 y' r.val = classSum m 4 y (π r).val := by
  sorry

/-- T4.1 (α-power lemma). `α^{2^j} ≡ 1 + 3·2^{j+1}√2 mod 2^{j+4}`,
`j ≥ 2`, in `(c, 2e)`-coordinates. -/
theorem alpha_pow {j : Nat} (hj : 2 ≤ j) :
    (seqFrom 1 3 (2 ^ j) : ZMod (2 ^ (j + 4))) = 1 ∧
    (2 * seqFrom 0 1 (2 ^ j) : ZMod (2 ^ (j + 4))) =
      (3 * 2 ^ (j + 1) : ℕ) := by sorry

/-- T4.2 (doubling identity). `S^{(k)}_r = 2·S^{(k-1)}_r` in
`ℤ/Q_k`, `k ≥ 4`; lifted-value form. -/
theorem doubling {k : Nat} (hk : 4 ≤ k) (T D : ℤ)
    (hD : (8 : ℤ) ∣ D) (r : ℕ) :
    (classSum (2 ^ k) 4
      (fun s => block ((T : ZMod (2 ^ (k + 3)))) ((D : ZMod (2 ^ (k + 3)))) s) r).val
      = 2 * (classSum (2 ^ (k - 1)) 4
      (fun s => block ((T : ZMod (2 ^ (k + 2)))) ((D : ZMod (2 ^ (k + 2)))) s) r).val := by
  sorry

/-- T4.3 (component Lemma Y mod 2^a). `a = 2` if `m` odd,
`2L+3` if `L = v₂(m) ≥ 1` (T0.2). FIXED FORM: `r : Fin (gcd m 4)`
with `.val` (draft form ill-typed). -/
theorem componentY_mod2pow {m : Nat} (hm : 1 ≤ m)
    (y y' : ℕ → ZMod (2 ^ (if m % 2 = 1 then 2
      else 2 * Nat.factorization m 2 + 3)))
    (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧
      ∀ r : Fin (Nat.gcd m 4), classSum m (Nat.gcd m 4) y' r.val =
        classSum m (Nat.gcd m 4) y (π r).val := by sorry

/-- T5.1 (L1, period). A block mod `2^t` (`t ≥ 5`) has period
`2^{t-3}`. -/
theorem block_period {t : Nat} (ht : 5 ≤ t) (T D : ZMod (2 ^ t))
    (hD : (8 : ZMod (2 ^ t)) ∣ D) (s : ℕ) :
    block T D (s + 2 ^ (t - 3)) = block T D s := by sorry

/-- T5.2 (L2, shift). `r_{s+M} = r_s + 2^t·δ_s` with `δ_s`
constant per class parity. -/
theorem block_shift {t : Nat} (ht : 5 ≤ t) (T D : ZMod (2 ^ (t + 1)))
    (hD : (8 : ZMod (2 ^ (t + 1))) ∣ D) :
    ∃ e₀ e₁ : ZMod 2, ∀ s, s < 2 ^ (t - 3) →
      block T D (s + 2 ^ (t - 3)) = block T D s +
        ((2 ^ t : ℕ) : ZMod (2 ^ (t + 1))) *
        ((if s % 2 = 0 then e₀ else e₁).val : ZMod (2 ^ (t + 1))) := by sorry

/-- T5.3 (L3, base mod 32). FIXED FORM: `r : Fin 4` with `.val`
(draft form ill-typed). The naive "flip" sub-claim is FALSE and
is not used. -/
theorem pattern_mod32 (T D T' D' : ZMod 32)
    (hD : (8 : ZMod 32) ∣ D) (hD' : (8 : ZMod 32) ∣ D')
    (hsame : seqMultiset 4 (block T D) = seqMultiset 4 (block T' D')) :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧ ∀ r : Fin 4,
      perClassMultiset 4 (block T' D') r.val =
        perClassMultiset 4 (block T D) (π r).val := by sorry

/-- T5.4 (L4 induction; pattern lemma). FIXED FORM: `r : Fin 4`
with `.val` (draft form ill-typed). -/
theorem pattern_lemma {L : Nat} (hL : 2 ≤ L)
    (p p' : ℕ → ZMod (2 ^ (2 * L + 3)))
    (hfix : IsFix (2 ^ L) p) (hfix' : IsFix (2 ^ L) p')
    (hsame : seqMultiset (2 ^ L) p = seqMultiset (2 ^ L) p') :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧ ∀ r : Fin 4,
      perClassMultiset (2 ^ L) p' r.val =
        perClassMultiset (2 ^ L) p (π r).val := by sorry

/-! ## §4 — Milestone 3 restated (stages 6–7: Lemma S, compatibility, assembly)

Source: `LineBLemmaYMilestone3Draft.lean` (wave 17). Proofs are the
milestone's, transported onto §1; every proof here is `sorry`
pending that transport. -/

/-- T6.1 (pair lemma PL). For a pattern `p ∈ Fix_P mod 2^a`, equal
pair-unions imply equal pair-profiles. PL is FALSE for arbitrary
multisets; the segment structure (cases A/B/C) is the Fix input. -/
theorem pair_lemma {L : Nat} (hL : 2 ≤ L)
    (p : ℕ → ZMod (2 ^ (2 * L + 3))) (hfix : IsFix (2 ^ L) p)
    {r s r' s' : ℕ} (hrs : r ≠ s) (hr's' : r' ≠ s')
    (hunion : perClassMultiset (2 ^ L) p r + perClassMultiset (2 ^ L) p s =
      perClassMultiset (2 ^ L) p r' + perClassMultiset (2 ^ L) p s') :
    (perClassMultiset (2 ^ L) p r = perClassMultiset (2 ^ L) p r' ∧
      perClassMultiset (2 ^ L) p s = perClassMultiset (2 ^ L) p s') ∨
    (perClassMultiset (2 ^ L) p r = perClassMultiset (2 ^ L) p s' ∧
      perClassMultiset (2 ^ L) p s = perClassMultiset (2 ^ L) p r') := by
  sorry

/-- T6.2 (Lemma S, stabiliser adjustment). If `γ ∈ D₄` satisfies
the union equalities `(*)` over every `v`-fiber block, then some
`δ ∈ Stab(M)` maps every `γ(F_a)` back to `F_a`. -/
theorem lemmaS {L : Nat} (hL : 2 ≤ L)
    (p : ℕ → ZMod (2 ^ (2 * L + 3))) (hfix : IsFix (2 ^ L) p)
    (v : Fin 4 → ZMod 3) (hv2 : v 2 = -v 0) (hv3 : v 3 = -v 1)
    (γ : Fin 4 → Fin 4) (hγ : IsDihedral γ)
    (hstar : ∀ a : ZMod 3,
      (∑ r ∈ Finset.univ.filter (fun r : Fin 4 => v r = a),
        perClassMultiset (2 ^ L) p r.val) =
      (∑ r ∈ Finset.univ.filter (fun r : Fin 4 => v r = a),
        perClassMultiset (2 ^ L) p (γ r).val)) :
    ∃ δ : Fin 4 → Fin 4, IsDihedral δ ∧ StabM (2 ^ L) p δ ∧
      ∀ a : ZMod 3, ∀ r : Fin 4, v r = a → v (δ (γ r)) = a := by
  sorry

/-- T6.3 (bijective `τ′` from global `σ`). Bijectivity is
load-bearing: a per-`k` non-injective matching does NOT imply
compatibility. FIXED FORM: ascribed constructor with
`Nat.mod_lt _ hm` plus a new `hm : 0 < m` hypothesis (draft form
ill-typed: anonymous constructor without determinable expected
type, and `by omega` cannot prove `σ i % m < m` for variable `m`). -/
theorem bijective_tau {m P : Nat} (hPm : P ∣ m) (hP4 : 4 ∣ P) (hm : 0 < m)
    (y y' : ℕ → ZMod (2 ^ 6)) (v v' : ℕ → ZMod 3)
    (σ : ℕ → ℕ) (hσbij : Function.Bijective (fun i : Fin m => (⟨σ i % m, Nat.mod_lt _ hm⟩ : Fin m)))
    (hσ : ∀ i, y' i = y (σ i)) (hσv : ∀ i, v' (i % 4) = v (σ i % 4)) :
    ∃ τ' : Fin P → Fin P, Function.Bijective τ' ∧ ∀ k : Fin P,
      y' k.val = y (τ' k).val ∧ v' (k.val % 4) = v ((τ' k).val % 4) := by
  sorry

/-- T6.4 (π₂ = π₃ compatibility). Given the pattern lemma (input A:
`π₂` with `M′_r = M_{π₂(r)}`) and Lemma S (input B: T6.2), there is
`π ∈ Π₂ ∩ Π₃`. FIXED FORM: `r : Fin 4` with `.val` in `hπ₂` and
in the conclusion (draft form ill-typed). -/
theorem pi2_pi3 {L : Nat} (hL : 2 ≤ L)
    (p p' : ℕ → ZMod (2 ^ (2 * L + 3)))
    (hfix : IsFix (2 ^ L) p) (hfix' : IsFix (2 ^ L) p')
    (v v' : Fin 4 → ZMod 3) (hv2 : v 2 = -v 0) (hv3 : v 3 = -v 1)
    (hv2' : v' 2 = -v' 0) (hv3' : v' 3 = -v' 1)
    (hπ₂ : ∃ π₂ : Fin 4 → Fin 4, IsDihedral π₂ ∧ ∀ r : Fin 4, perClassMultiset (2 ^ L) p' r.val = perClassMultiset (2 ^ L) p (π₂ r).val)
    (hπ₃ : ∃ π₃ : Fin 4 → Fin 4, IsDihedral π₃ ∧ ∀ r, v' r = v (π₃ r))
    (hS : ∀ γ : Fin 4 → Fin 4, IsDihedral γ → (∀ a : ZMod 3, (∑ r ∈ Finset.univ.filter (fun r : Fin 4 => v r = a), perClassMultiset (2 ^ L) p r.val) = (∑ r ∈ Finset.univ.filter (fun r : Fin 4 => v r = a), perClassMultiset (2 ^ L) p (γ r).val)) → ∃ δ : Fin 4 → Fin 4, IsDihedral δ ∧ StabM (2 ^ L) p δ ∧ ∀ a : ZMod 3, ∀ r : Fin 4, v r = a → v (δ (γ r)) = a) :
    ∃ π : Fin 4 → Fin 4, IsDihedral π ∧ (∀ r : Fin 4, perClassMultiset (2 ^ L) p' r.val = perClassMultiset (2 ^ L) p (π r).val) ∧ (∀ r, v' r = v (π r)) := by
  sorry

/-- T7.1 (mod-`D` Lemma Y — the chain's target, milestone-3 form).
For `q ‖ D_m`, two `Fix_m mod q` points with the same global
multiset have `D_t`-related class-sum vectors, `t = gcd(m, 4)`.
FIXED FORM: `r : Fin (gcd m 4)` with `.val` (draft form
ill-typed). Exact-integer class sums (Pcarry) are NOT claimed —
mod-`q` only. -/
theorem lemmaY_modD {m q : Nat} (hm : 1 ≤ m)
    (hq : ∃ p e : Nat, p.Prime ∧ q = p ^ e ∧ q ∣ (Dm m).toNat)
    (y y' : ℕ → ZMod q) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧
      ∀ r : Fin (Nat.gcd m 4), classSum m (Nat.gcd m 4) y' r.val =
        classSum m (Nat.gcd m 4) y (π r).val := by
  sorry

/-- T7.2 (support is a union of fibers, conditional form). If a
support predicate on `Fix` points depends only on the pair-value
multiset (the `pair_sorted` data), then T7.1 implies it is
constant on fibers. The `φ̂` criterion itself is NOT restated here. -/
theorem support_union_fibers {m q : Nat} (hm : 1 ≤ m)
    (supp : (ℕ → ZMod q) → Prop)
    (hpair : ∀ y y' : ℕ → ZMod q, IsFix m y → IsFix m y' →
      seqMultiset m y = seqMultiset m y' → (supp y ↔ supp y'))
    (y y' : ℕ → ZMod q) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    supp y ↔ supp y' := by
  sorry

/-! ## §5 — Assembly theorems (reference §§2–4 directly)

Unlike the wave-26 assembly draft, these theorems take NO
milestone result as a hypothesis: the results they need are the
restated theorems of §§2–4, in scope in this file. The proofs are
still `sorry` — the composition argument (branch case analysis +
CRT over class sums) is not formalised here — but the dependency
wiring is now direct reference instead of hypothesis plumbing.
Supply chain, for the future proof of `lemmaY_modD_assembly`:
  prime-power inventory: `pellC1` + `lte_v2` + `radical_eq`
    (every `q ‖ (Dm m).toNat` is `2^a`, `3^e`, or `p^e`, `p ∤ 24`);
  odd branch: `vanishing` (class sums are 0, any `π` works);
  `3^e` branch: `componentY_mod3pow` (via `scaling_div`,
    `scaling_bij`, `top_digit`, `componentY_mod3`);
  `2^a` branch: `componentY_mod2pow` (via `alpha_pow`,
    `doubling`, exponent `a` from `lte_v2`);
  2/3-compatibility: `pi2_pi3` (inputs `pattern_lemma` and
    `lemmaS`, the latter via `pair_lemma`; `bijective_tau` is the
    counting behind it — a per-`k` non-injective matching does NOT
    imply compatibility);
  CRT over class sums combines the branches into one `π ∈ D_t`.
Note: `lemmaY_modD_assembly` below and §4's `lemmaY_modD` state
the same target; §4's is milestone 3's own assembly, this one's
proof route is the explicit branch composition above. Proving
either (plus transport) discharges the other. -/

/-- T7.1-assembly (mod-`D` Lemma Y from the milestone interface
theorems, referenced directly). For `t = gcd(m, 4) < 4` the
4-class statements restrict to `t` classes, and `t = 1` is
trivial since `Fin 1` has one element. -/
theorem lemmaY_modD_assembly {m q : Nat} (hm : 1 ≤ m)
    (hq : ∃ p e : Nat, p.Prime ∧ q = p ^ e ∧ q ∣ (Dm m).toNat)
    (y y' : ℕ → ZMod q) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧
      ∀ r : Fin (Nat.gcd m 4), classSum m (Nat.gcd m 4) y' r.val =
        classSum m (Nat.gcd m 4) y (π r).val := by
  sorry

/-- T7.2-assembly (support is a union of fibers). From
`lemmaY_modD_assembly` plus `classSum_dot` (the dot step), both
in scope above: if a support predicate depends only on the
pair-value multiset (the `pair_sorted` data — main's `φ̂`
support criterion in `LineDOrbitPairFull`), then it is constant
on fibers. The `φ̂` criterion itself is NOT restated here. -/
theorem support_union_from_assembly {m q : Nat} (hm : 1 ≤ m)
    (supp : (ℕ → ZMod q) → Prop)
    (hpair : ∀ y y' : ℕ → ZMod q, IsFix m y → IsFix m y' →
      seqMultiset m y = seqMultiset m y' → (supp y ↔ supp y'))
    (y y' : ℕ → ZMod q) (hfix : IsFix m y) (hfix' : IsFix m y')
    (hsame : seqMultiset m y = seqMultiset m y') :
    supp y ↔ supp y' := by
  sorry

/-! ## Beyond mod-`D`: what the exact lemma still needs -/

/-- Exact per-class lemma from the mod-`D` assembly, with the three
open gaps as EXPLICIT hypotheses (all unproved, all `sorry` here):
  `hG1`     : odd lift G1 at `f ≥ 3` (the `f = 2` case is closed);
  `hPC`     : general Lemma PC, one common `π` across all components;
  `hPcarry` : exact-integer class sums (Pcarry), lifting the
    mod-`q` statement to exact multisets.
This is the form 152's separation step needs; it is NOT claimed
as proved, and none of `hG1`, `hPC`, `hPcarry` is supplied by
milestones 1–3. The conclusion is a placeholder (`True`): exact
integer per-class vocabulary (exact lifts of `classSum` /
`perClassMultiset` over `ℤ`) is future work, as in the wave-26
assembly draft. -/
theorem exact_perclass_from_modD {m : Nat} (hm : 1 ≤ m)
    (hG1 : True) (hPC : True) (hPcarry : True)
    (y y' : ℕ → ℤ) (hsame : True) :
    ∃ π : Fin (Nat.gcd m 4) → Fin (Nat.gcd m 4), IsDihedral π ∧ True := by
  sorry

/-! NOT in this file: no complete proof (every proof is `sorry`);
no transport theorems from the milestone files (see header);
no redefinition of main's objects, no change to `LineBDerand`,
no full-`Bgs` import; `m = 0` excluded. -/
end Bgs.Breakthrough.LemmaY
