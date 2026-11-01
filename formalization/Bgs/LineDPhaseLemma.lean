/-
# BGS-TRACE-150: phase replacement for the false lattice collapse

Verified in a test copy 2026-11-01 (rebuild EXIT:0, standard axioms);
imported by `Bgs.lean` in main.

Background: `LineDExpansion.psi_tStar_depends_on_residue` is conditional
on `hcollapse` — from `N₁ ≡ ±N₂ [MOD g']` conclude
`t*(N₁) ∓ t*(N₂) ∈ ℤ`. That hypothesis is FALSE for the true `t*`
(counterexample at `m = 3`: `t*(1) − t*(15) = −1/14 ∉ ℤ`
although `15 ≡ 1 [MOD 14]`). So the residue-dependence of `Psi_m(t*)`
cannot go through a collapse of `t*` itself.

What is proved here instead, and what is NOT:

* The true `t*` (boundary 150: `t* = t_N − 1/(N·D_m)`, with `t_N` from
  the 149 bridge) has the form `t* = k/D_m` with an integer numerator
  `k = (D·r − 1)/N`, `r = D⁻¹ mod N` (`tStar_eq`). This is the exact
  form, not a mod-1 statement.
* Key congruence: for every divisor `e ∣ D_m`, `N·k ≡ −1 (mod e)`
  (`Nk_eq_neg_one_zmod`), hence `k mod e` is determined by `N mod e`:
  `N₁ ≡ N₂ [MOD e]` gives `e ∣ (k₁ − k₂)` (`k_sub_dvd_of_modEq`),
  and `N₁ + N₂ ≡ 0 [MOD e]` gives `e ∣ (k₁ + k₂)`
  (`k_add_dvd_of_negModEq`). No analysis: this is `D·r ≡ 1 (mod N)`
  read modulo a divisor of `D`.
* Phase lemma at the `PsiMode` level (`psimode_eq_of_phase_int`): if
  `(t₁ − t₂)·2(Qn − Qn') ∈ ℤ` for all mode pairs, then the mode sums
  coincide — termwise, from `exp(2πi·integer) = 1`. No collapse of
  the parameters is needed: only the phases need to be integral.
* Assembly (`psimode_eq_of_edvd_diff` / `psimode_eq_of_edvd_sum`):
  with `D = d·e` and `d ∣ 2Q` for all modes, the phase integrality
  follows from `e ∣ (k₁ ∓ k₂)`: the product
  `(t₁ ∓ t₂)·2ΔQ = ((k₁ ∓ k₂)/e)·(2ΔQ/d)` is an integer. The minus
  case additionally uses `psiMode_even` (symmetric covariances).
* Quadratic-form divisibility (`two_mul_Qform_dvd`): for the
  adjugate form `Q(n) = nᵀ X_m n` (Derand's `Xm`), `d ∣ 2Q(n)` follows
  from entry divisibility `d ∣ 2X_ij` by linearity over the double
  sum — no pairing argument is needed, because the entries
  themselves (not only `4X_ij`) turn out to be divisible by `d`.
* Computational instances for `m = 3..9` (`xm_entry_dvd`,
  `dOf_dvd_derand_D`, `e_eq_gp`, all by `decide`): with
  `d = 14, 24, 82, 140, 478, 816, 2786` the entries satisfy
  `d ∣ 2X_ij`, and `D/d = gp m` — exactly the boundary's
  `g'_m = D_m/gcd(D_m, 2X_ii, 4X_ij)`. So the final theorems
  (`psimode_tStar_eq_of_modEq`, `psimode_tStar_eq_of_negModEq`) state
  the residue-dependence with the boundary's own modulus `gp m`.
* The `t*` here is the true boundary `t*`: at `m = 3` it takes the
  values `t*(1) = −1/196`, `t*(15) = 13/196`, whose difference
  `−1/14 ∉ ℤ` is exactly why no collapse of `t*` itself can hold —
  only the phases need to be integral.

What is deliberately NOT claimed:

* The identification `Psi_m = PsiMode c (Qform ∘ v)` — i.e. that the
  boundary's `Psi_m` is the mode sum with the adjugate form and the
  averaged covariances — is 149-full analytic content (`hTrace`,
  `hAvg`, `hPair` of `LineDBridge`). The theorems here are at the
  `PsiMode` level; they close the "residue ⇒ phase ⇒ mode sum"
  step, not the identification step.
* The `H·X = D·I` certificate (`lemmaQ` in Derand) is context for why
  `Xm` is the right matrix, not a hypothesis of the lemmas: the
  phase argument only uses the entries of `Xm` and `D_m`.
* The minus case needs symmetric covariances (`psiMode_even`'s
  hypothesis), kept explicit.

No `sorry`, no `admit`, no `axiom`, no `native_decide` in this file.
`#print axioms` for the main theorems is at the end.
-/

import Bgs.LineDBridge
import Bgs.LineDDmBridge
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

namespace Bgs
namespace LineD
namespace PhaseLemma

open Finset

/-! ### §1. The true `t*` and its integer numerator -/

/-- `t* = t_N − 1/(N·D_m)` (boundary 150), with `t_N` from the 149 bridge. -/
noncomputable def tStar (m N : ℕ) [NeZero m] [NeZero N]
    (h : Nat.Coprime (LineD.Defs.Dm m).toNat N) : ℝ :=
  LineD.Bridge.tN m N h - 1 / ((N : ℝ) * ((LineD.Defs.Dm m).toNat : ℝ))

/-- The numerator `k` with `t* = k/D`: `k = (D·r − 1)/N`, `r = D⁻¹ mod N`
(exact division; no coprimality hypothesis is needed for the definition). -/
noncomputable def kStar (m N : ℕ) [NeZero m] : ℤ :=
  ((LineD.Defs.Dm m) * ((((LineD.Defs.Dm m).toNat : ZMod N)⁻¹).val : ℤ) - 1) / (N : ℤ)

/-- `N ∣ (D·r − 1)`: from `D·r = 1` in `ZMod N` (the `tN` specification). -/
theorem dvd_Dr_sub_one (m N : ℕ) [NeZero m] [NeZero N]
    (h : Nat.Coprime (LineD.Defs.Dm m).toNat N) (hDpos : 0 < LineD.Defs.Dm m) :
    (N : ℤ) ∣ (LineD.Defs.Dm m) * ((((LineD.Defs.Dm m).toNat : ZMod N)⁻¹).val : ℤ) - 1 := by
  have hspec := LineD.Bridge.tN_spec m N h
  have hr : ((((LineD.Defs.Dm m).toNat : ZMod N)⁻¹).val : ZMod N)
      = ((LineD.Defs.Dm m).toNat : ZMod N)⁻¹ := ZMod.natCast_zmod_val _
  have hDcast : ((LineD.Defs.Dm m : ℤ) : ZMod N) = ((LineD.Defs.Dm m).toNat : ZMod N) := by
    conv_lhs => rw [← Int.toNat_of_nonneg hDpos.le]
    exact Int.cast_natCast _
  rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
  push_cast
  rw [hDcast, hr, hspec]
  simp

/-- `k·N = D·r − 1` (exact division). -/
theorem kStar_mul (m N : ℕ) [NeZero m] [NeZero N]
    (h : Nat.Coprime (LineD.Defs.Dm m).toNat N) (hDpos : 0 < LineD.Defs.Dm m) :
    kStar m N * (N : ℤ)
      = (LineD.Defs.Dm m) * ((((LineD.Defs.Dm m).toNat : ZMod N)⁻¹).val : ℤ) - 1 := by
  unfold kStar
  exact Int.ediv_mul_cancel (dvd_Dr_sub_one m N h hDpos)

/-- `t* = k/D` exactly. -/
theorem tStar_eq (m N : ℕ) [NeZero m] [NeZero N]
    (h : Nat.Coprime (LineD.Defs.Dm m).toNat N) (hDpos : 0 < LineD.Defs.Dm m) :
    tStar m N h = (kStar m N : ℝ) / ((LineD.Defs.Dm m).toNat : ℝ) := by
  have hN : ((N : ℝ)) ≠ 0 := by exact_mod_cast (NeZero.ne N)
  have hD : (((LineD.Defs.Dm m).toNat : ℝ)) ≠ 0 := by
    have hpos : 0 < (LineD.Defs.Dm m).toNat := by omega
    exact_mod_cast hpos.ne'
  have hk := kStar_mul m N h hDpos
  have hkR : (kStar m N : ℝ) * (N : ℝ)
      = (LineD.Defs.Dm m : ℝ) * ((((LineD.Defs.Dm m).toNat : ZMod N)⁻¹).val : ℝ) - 1 := by
    exact_mod_cast hk
  have hDcastR : (LineD.Defs.Dm m : ℝ) = ((LineD.Defs.Dm m).toNat : ℝ) := by
    exact_mod_cast (Int.toNat_of_nonneg hDpos.le).symm
  unfold tStar LineD.Bridge.tN
  rw [hDcastR] at hkR
  field_simp
  linear_combination -hkR

/-! ### §2. The key congruence: `k mod e` is determined by `N mod e` -/

/-- `N·k ≡ −1 (mod e)` for every divisor `e ∣ D`: from `N·k = D·r − 1`
and `D ≡ 0 (mod e)`. -/
theorem Nk_eq_neg_one_zmod (m N e : ℕ) [NeZero m] [NeZero N]
    (h : Nat.Coprime (LineD.Defs.Dm m).toNat N) (hDpos : 0 < LineD.Defs.Dm m)
    (heD : e ∣ (LineD.Defs.Dm m).toNat) :
    ((N : ZMod e) * (kStar m N : ZMod e)) = -1 := by
  have hk := kStar_mul m N h hDpos
  obtain ⟨q, hq⟩ := heD
  have hD0 : (((LineD.Defs.Dm m) : ℤ) : ZMod e) = 0 := by
    have h1 : (LineD.Defs.Dm m : ℤ) = (((LineD.Defs.Dm m).toNat : ℕ) : ℤ) :=
      (Int.toNat_of_nonneg hDpos.le).symm
    rw [h1, hq]
    push_cast
    rw [ZMod.natCast_self, zero_mul]
  have h2 := congrArg (fun x : ℤ => (x : ZMod e)) hk
  push_cast at h2
  rw [hD0, zero_mul, zero_sub, mul_comm] at h2
  exact h2

/-- Cancellation through a unit in `ZMod e`: from `u·k₁ = u·k₂ = −1`,
the `k`'s coincide. -/
theorem zmod_k_eq_of_mul_eq {e : ℕ} (u : (ZMod e)ˣ) (k₁ k₂ : ℤ)
    (h1 : (u : ZMod e) * (k₁ : ZMod e) = -1)
    (h2 : (u : ZMod e) * (k₂ : ZMod e) = -1) :
    (k₁ : ZMod e) = (k₂ : ZMod e) := by
  have e1 : (k₁ : ZMod e) = ((u⁻¹ : (ZMod e)ˣ) : ZMod e) * (-1) := by
    have h : (k₁ : ZMod e) = ((u⁻¹ : (ZMod e)ˣ) : ZMod e) * ((u : ZMod e) * (k₁ : ZMod e)) := by
      rw [← mul_assoc, Units.inv_mul, one_mul]
    rw [h, h1]
  have e2 : (k₂ : ZMod e) = ((u⁻¹ : (ZMod e)ˣ) : ZMod e) * (-1) := by
    have h : (k₂ : ZMod e) = ((u⁻¹ : (ZMod e)ˣ) : ZMod e) * ((u : ZMod e) * (k₂ : ZMod e)) := by
      rw [← mul_assoc, Units.inv_mul, one_mul]
    rw [h, h2]
  rw [e1, e2]

/-- Plus case: `N₁ ≡ N₂ [MOD e]` gives `e ∣ (k₁ − k₂)`. -/
theorem k_sub_dvd_of_modEq (m N₁ N₂ e : ℕ) [NeZero m] [NeZero N₁] [NeZero N₂]
    (h₁ : Nat.Coprime (LineD.Defs.Dm m).toNat N₁)
    (h₂ : Nat.Coprime (LineD.Defs.Dm m).toNat N₂)
    (hDpos : 0 < LineD.Defs.Dm m) (heD : e ∣ (LineD.Defs.Dm m).toNat)
    (hc₁ : Nat.Coprime N₁ e) (hres : N₁ ≡ N₂ [MOD e]) :
    (e : ℤ) ∣ (kStar m N₁ - kStar m N₂) := by
  have hN1 := Nk_eq_neg_one_zmod m N₁ e h₁ hDpos heD
  have hN2 := Nk_eq_neg_one_zmod m N₂ e h₂ hDpos heD
  have hNeq : (N₁ : ZMod e) = (N₂ : ZMod e) :=
    (ZMod.natCast_eq_natCast_iff N₁ N₂ e).mpr hres
  rw [← hNeq] at hN2
  have hu : (ZMod.unitOfCoprime N₁ hc₁ : ZMod e) = (N₁ : ZMod e) :=
    ZMod.coe_unitOfCoprime N₁ hc₁
  have hkeq : (kStar m N₁ : ZMod e) = (kStar m N₂ : ZMod e) := by
    have h1 : ((ZMod.unitOfCoprime N₁ hc₁ : (ZMod e)ˣ) : ZMod e) * (kStar m N₁ : ZMod e) = -1 := by
      rw [hu]; exact hN1
    have h2 : ((ZMod.unitOfCoprime N₁ hc₁ : (ZMod e)ˣ) : ZMod e) * (kStar m N₂ : ZMod e) = -1 := by
      rw [hu]; exact hN2
    exact zmod_k_eq_of_mul_eq (ZMod.unitOfCoprime N₁ hc₁) _ _ h1 h2
  rw [ZMod.intCast_eq_intCast_iff] at hkeq
  rw [Int.modEq_iff_dvd] at hkeq
  obtain ⟨c, hc⟩ := hkeq
  exact ⟨-c, by
    have h2 : kStar m N₁ - kStar m N₂ = -(kStar m N₂ - kStar m N₁) := by ring
    rw [h2, hc]; ring⟩

/-- Minus case: `N₁ + N₂ ≡ 0 [MOD e]` gives `e ∣ (k₁ + k₂)`. -/
theorem k_add_dvd_of_negModEq (m N₁ N₂ e : ℕ) [NeZero m] [NeZero N₁] [NeZero N₂]
    (h₁ : Nat.Coprime (LineD.Defs.Dm m).toNat N₁)
    (h₂ : Nat.Coprime (LineD.Defs.Dm m).toNat N₂)
    (hDpos : 0 < LineD.Defs.Dm m) (heD : e ∣ (LineD.Defs.Dm m).toNat)
    (hc₁ : Nat.Coprime N₁ e) (hres : (N₁ + N₂) ≡ 0 [MOD e]) :
    (e : ℤ) ∣ (kStar m N₁ + kStar m N₂) := by
  have hN1 := Nk_eq_neg_one_zmod m N₁ e h₁ hDpos heD
  have hN2 := Nk_eq_neg_one_zmod m N₂ e h₂ hDpos heD
  have hu : (ZMod.unitOfCoprime N₁ hc₁ : ZMod e) = (N₁ : ZMod e) :=
    ZMod.coe_unitOfCoprime N₁ hc₁
  have hN2eq : (N₂ : ZMod e) = -(N₁ : ZMod e) := by
    have h0 : ((N₁ + N₂ : ℕ) : ZMod e) = 0 := by
      simpa using (ZMod.natCast_eq_natCast_iff _ _ _).mpr hres
    push_cast at h0
    linear_combination h0
  have hsum0 : (N₁ : ZMod e) * ((kStar m N₁ : ZMod e) + (kStar m N₂ : ZMod e)) = 0 := by
    have hmul : (N₁ : ZMod e) * (kStar m N₂ : ZMod e) = 1 := by
      have hN1eq : (N₁ : ZMod e) = -(N₂ : ZMod e) := by
        rw [hN2eq]; simp
      rw [hN1eq, neg_mul, hN2, neg_neg]
    rw [mul_add, hN1, hmul]
    simp
  have hkeq0 : (kStar m N₁ : ZMod e) + (kStar m N₂ : ZMod e) = 0 := by
    have h : (kStar m N₁ : ZMod e) + (kStar m N₂ : ZMod e)
        = ((ZMod.unitOfCoprime N₁ hc₁)⁻¹ : (ZMod e)ˣ) * ((N₁ : ZMod e)
          * ((kStar m N₁ : ZMod e) + (kStar m N₂ : ZMod e))) := by
      rw [← hu, ← mul_assoc, Units.inv_mul, one_mul]
    rw [h, hsum0, mul_zero]
  have hmod : (kStar m N₁ + kStar m N₂) ≡ 0 [ZMOD (e : ℤ)] := by
    rw [← ZMod.intCast_eq_intCast_iff]
    push_cast
    exact hkeq0
  rw [Int.modEq_iff_dvd] at hmod
  obtain ⟨c, hc⟩ := hmod
  exact ⟨-c, by
    have h2 : kStar m N₁ + kStar m N₂ = -(0 - (kStar m N₁ + kStar m N₂)) := by ring
    rw [h2, hc]; ring⟩

/-! ### §3. The phase lemma at the `PsiMode` level -/

/-- If every phase difference `(t₁ − t₂)·2(Qn − Qn')` is an integer,
then the mode sums coincide — termwise, since `exp(2πi·integer) = 1`. -/
theorem psimode_eq_of_phase_int {ι : Type*} [Fintype ι] (c : ι → ι → ℂ) (Q : ι → ℤ)
    {t₁ t₂ : ℝ} (h : ∀ n n', ∃ k : ℤ, (t₁ - t₂) * (2 * ((Q n : ℝ) - Q n')) = (k : ℝ)) :
    LineD.Bridge.PsiMode c Q t₁ = LineD.Bridge.PsiMode c Q t₂ := by
  unfold LineD.Bridge.PsiMode
  apply Finset.sum_congr rfl; intro n _
  apply Finset.sum_congr rfl; intro n' _
  obtain ⟨k, hk⟩ := h n n'
  congr 1
  rw [show 2 * Real.pi * Complex.I * (t₁ : ℂ) * (2 * ((Q n : ℝ) - Q n'))
      = 2 * Real.pi * Complex.I * (t₂ : ℂ) * (2 * ((Q n : ℝ) - Q n'))
        + (k : ℤ) * (2 * Real.pi * Complex.I) by
    have hkC : ((t₁ : ℂ) - (t₂ : ℂ)) * (2 * (((Q n : ℤ) : ℂ) - ((Q n' : ℤ) : ℂ)))
        = (k : ℂ) := by
      exact_mod_cast hk
    push_cast
    linear_combination (2 * Real.pi * Complex.I) * hkC]
  rw [Complex.exp_add, Complex.exp_int_mul_two_pi_mul_I, mul_one]

/-- The real-arithmetic core, shared by the plus and minus cases:
with `tᵢ = kᵢ/D`, `D = d·e`, `k₁ − k₂ = e·s` and `x = d·j`,
`(t₁ − t₂)·x = s·j`. -/
theorem phase_real {D d e : ℕ} (hDpos : 0 < D) (hdD : d ∣ D) (he : D = d * e)
    (t₁ t₂ : ℝ) (k₁ k₂ : ℤ) (hk₁ : t₁ = (k₁ : ℝ) / (D : ℝ))
    (hk₂ : t₂ = (k₂ : ℝ) / (D : ℝ))
    (s j : ℤ) (hdiff : k₁ - k₂ = e * s)
    (x : ℝ) (hx : x = ((d * j : ℤ) : ℝ)) :
    (t₁ - t₂) * x = ((s * j : ℤ) : ℝ) := by
  have hDne : ((D : ℝ)) ≠ 0 := by exact_mod_cast hDpos.ne'
  have hdpos : 0 < d := Nat.pos_of_dvd_of_pos hdD hDpos
  have hdne : ((d : ℝ)) ≠ 0 := by exact_mod_cast hdpos.ne'
  have hepos : 0 < e := by
    rcases Nat.eq_zero_or_pos e with h | h
    · rw [h, mul_zero] at he; omega
    · exact h
  have hene : ((e : ℝ)) ≠ 0 := by exact_mod_cast hepos.ne'
  have hcast : ((k₁ : ℝ) / (D : ℝ) - (k₂ : ℝ) / (D : ℝ))
      = (((k₁ - k₂ : ℤ) : ℝ) / (D : ℝ)) := by
    push_cast; rw [sub_div]
  rw [hk₁, hk₂, hcast, hdiff, hx]
  have heR : ((D : ℝ)) = (d : ℝ) * (e : ℝ) := by exact_mod_cast he
  rw [heR]
  push_cast
  field_simp

/-- Phase integrality from `e ∣ (k₁ − k₂)` and `d ∣ 2Q`: with `D = d·e`,
`(t₁ − t₂)·2ΔQ = ((k₁ − k₂)/e)·(2ΔQ/d)` is an integer. -/
theorem phase_int_of_edvd {ι : Type*} [Fintype ι] (Q : ι → ℤ)
    {D d e : ℕ} (hDpos : 0 < D) (hdD : d ∣ D) (he : D = d * e)
    (hQd : ∀ i, (d : ℤ) ∣ 2 * Q i)
    (t₁ t₂ : ℝ) (k₁ k₂ : ℤ) (hk₁ : t₁ = (k₁ : ℝ) / (D : ℝ))
    (hk₂ : t₂ = (k₂ : ℝ) / (D : ℝ))
    (hdiff : (e : ℤ) ∣ (k₁ - k₂)) (n n' : ι) :
    ∃ k : ℤ, (t₁ - t₂) * (2 * ((Q n : ℝ) - Q n')) = (k : ℝ) := by
  have hdvd : (d : ℤ) ∣ 2 * (Q n - Q n') := by
    have h1 := hQd n; have h2 := hQd n'
    have hsub : (d : ℤ) ∣ (2 * Q n - 2 * Q n') := Int.dvd_sub h1 h2
    rwa [← mul_sub] at hsub
  obtain ⟨j, hj⟩ := hdvd
  obtain ⟨s, hs⟩ := hdiff
  refine ⟨s * j, ?_⟩
  have h2Δ : (2 : ℝ) * (((Q n : ℤ) : ℝ) - ((Q n' : ℤ) : ℝ)) = ((d * j : ℤ) : ℝ) := by
    have hjR : ((2 * (Q n - Q n') : ℤ) : ℝ) = ((d * j : ℤ) : ℝ) := by exact_mod_cast hj
    push_cast at hjR ⊢
    exact hjR
  exact phase_real hDpos hdD he t₁ t₂ k₁ k₂ hk₁ hk₂ s j hs
    (2 * ((Q n : ℝ) - Q n')) h2Δ

/-- Assembly, plus case: `e ∣ (k₁ − k₂)` gives equal mode sums. -/
theorem psimode_eq_of_edvd_diff {ι : Type*} [Fintype ι] (c : ι → ι → ℂ) (Q : ι → ℤ)
    {D d e : ℕ} (hDpos : 0 < D) (hdD : d ∣ D) (he : D = d * e)
    (hQd : ∀ i, (d : ℤ) ∣ 2 * Q i)
    (t₁ t₂ : ℝ) (k₁ k₂ : ℤ) (hk₁ : t₁ = (k₁ : ℝ) / (D : ℝ))
    (hk₂ : t₂ = (k₂ : ℝ) / (D : ℝ))
    (hdiff : (e : ℤ) ∣ (k₁ - k₂)) :
    LineD.Bridge.PsiMode c Q t₁ = LineD.Bridge.PsiMode c Q t₂ := by
  apply psimode_eq_of_phase_int c Q
  intro n n'
  exact phase_int_of_edvd Q hDpos hdD he hQd t₁ t₂ k₁ k₂ hk₁ hk₂ hdiff n n'

/-- Phase integrality from `e ∣ (k₁ + k₂)` and `d ∣ 2Q`: the difference
against the negated parameter is `(t₁ − (−t₂))·2ΔQ = ((k₁+k₂)/e)·(2ΔQ/d)`. -/
theorem phase_int_of_edvd_sum {ι : Type*} [Fintype ι] (Q : ι → ℤ)
    {D d e : ℕ} (hDpos : 0 < D) (hdD : d ∣ D) (he : D = d * e)
    (hQd : ∀ i, (d : ℤ) ∣ 2 * Q i)
    (t₁ t₂ : ℝ) (k₁ k₂ : ℤ) (hk₁ : t₁ = (k₁ : ℝ) / (D : ℝ))
    (hk₂ : t₂ = (k₂ : ℝ) / (D : ℝ))
    (hdiff : (e : ℤ) ∣ (k₁ + k₂)) (n n' : ι) :
    ∃ k : ℤ, (t₁ - (-t₂)) * (2 * ((Q n : ℝ) - Q n')) = (k : ℝ) := by
  have hdvd : (d : ℤ) ∣ 2 * (Q n - Q n') := by
    have h1 := hQd n; have h2 := hQd n'
    have hsub : (d : ℤ) ∣ (2 * Q n - 2 * Q n') := Int.dvd_sub h1 h2
    rwa [← mul_sub] at hsub
  obtain ⟨j, hj⟩ := hdvd
  obtain ⟨s, hs⟩ := hdiff
  refine ⟨s * j, ?_⟩
  have h2Δ : (2 : ℝ) * (((Q n : ℤ) : ℝ) - ((Q n' : ℤ) : ℝ)) = ((d * j : ℤ) : ℝ) := by
    have hjR : ((2 * (Q n - Q n') : ℤ) : ℝ) = ((d * j : ℤ) : ℝ) := by exact_mod_cast hj
    push_cast at hjR ⊢
    exact hjR
  have hdiff' : k₁ - (-k₂) = e * s := by
    rw [sub_neg_eq_add]; exact hs
  exact phase_real hDpos hdD he t₁ (-t₂) k₁ (-k₂) hk₁
    (by rw [hk₂, Int.cast_neg, neg_div]) s j hdiff' (2 * ((Q n : ℝ) - Q n')) h2Δ

/-- Assembly, minus case: `e ∣ (k₁ + k₂)` gives equal mode sums, via
evenness (symmetric covariances). -/
theorem psimode_eq_of_edvd_sum {ι : Type*} [Fintype ι] (c : ι → ι → ℂ) (Q : ι → ℤ)
    {D d e : ℕ} (hDpos : 0 < D) (hdD : d ∣ D) (he : D = d * e)
    (hQd : ∀ i, (d : ℤ) ∣ 2 * Q i)
    (t₁ t₂ : ℝ) (k₁ k₂ : ℤ) (hk₁ : t₁ = (k₁ : ℝ) / (D : ℝ))
    (hk₂ : t₂ = (k₂ : ℝ) / (D : ℝ))
    (hdiff : (e : ℤ) ∣ (k₁ + k₂))
    (hc : ∀ n n', c n n' = c n' n) :
    LineD.Bridge.PsiMode c Q t₁ = LineD.Bridge.PsiMode c Q t₂ := by
  have h1 : LineD.Bridge.PsiMode c Q t₁
      = LineD.Bridge.PsiMode c Q (-t₂) := by
    apply psimode_eq_of_phase_int c Q
    intro n n'
    exact phase_int_of_edvd_sum Q hDpos hdD he hQd t₁ t₂ k₁ k₂ hk₁ hk₂ hdiff n n'
  rw [h1, LineD.Bridge.psiMode_even c Q _ hc]

/-! ### §4. The adjugate form and its divisibility -/

/-- The quadratic form `Q(n) = nᵀ X_m n` with Derand's adjugate `Xm`
(`Xm` takes natural indices, hence `i.val`, `j.val`). -/
noncomputable def Qform (m : ℕ) (n : Fin m → ℤ) : ℤ :=
  ∑ i, ∑ j, LineB.Derand.Xm m i.val j.val * n i * n j

/-- `d ∣ 2Q(n)` from entry divisibility `d ∣ 2X_ij`, by linearity. -/
theorem two_mul_Qform_dvd {m d : ℕ}
    (h : ∀ i j : Fin m, (d : ℤ) ∣ 2 * LineB.Derand.Xm m i.val j.val) (n : Fin m → ℤ) :
    (d : ℤ) ∣ 2 * Qform m n := by
  have hsum : 2 * Qform m n
      = ∑ i, ∑ j, (2 * LineB.Derand.Xm m i.val j.val) * n i * n j := by
    unfold Qform
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl; intro i _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl; intro j _
    ring
  rw [hsum]
  apply Finset.dvd_sum; intro i _
  apply Finset.dvd_sum; intro j _
  exact ((h i j).mul_right (n i)).mul_right (n j)

/-- The table of `d_m = gcd(D_m, 2X_ii, 4X_ij)` values for `m = 3..9`
(the boundary's denominator; `D_m/d_m = gp m` below). -/
def dOf : ℕ → ℕ
  | 3 => 14
  | 4 => 24
  | 5 => 82
  | 6 => 140
  | 7 => 478
  | 8 => 816
  | 9 => 2786
  | _ => 1

/-- Entry divisibility `d_m ∣ 2X_ij` for `m = 3..9`, by finite check
(`decide` over the finite index type `Fin m`). -/
theorem xm_entry_fin {m : ℕ} (h3 : 3 ≤ m) (h9 : m ≤ 9) (i j : Fin m) :
    (dOf m : ℤ) ∣ 2 * LineB.Derand.Xm m i.val j.val := by
  revert i j
  interval_cases m <;> decide

/-- Positivity of `D_m` for `m = 3..9`, by finite check. -/
theorem derand_D_pos {m : ℕ} (h3 : 3 ≤ m) (h9 : m ≤ 9) :
    0 < (LineB.Derand.Dm m).toNat := by
  interval_cases m <;> decide

/-- Positivity of `d_m` for `m = 3..9`, by finite check. -/
theorem dOf_pos {m : ℕ} (h3 : 3 ≤ m) (h9 : m ≤ 9) : 0 < dOf m := by
  interval_cases m <;> decide

/-- `d_m ∣ D_m` for `m = 3..9`, by finite check. -/
theorem dOf_dvd_derand_D {m : ℕ} (h3 : 3 ≤ m) (h9 : m ≤ 9) :
    dOf m ∣ (LineB.Derand.Dm m).toNat := by
  interval_cases m <;> decide

/-- `D_m/d_m = gp m` for `m = 3..9`: the phase modulus is the
boundary's `g'_m` (and Derand's `gp`). -/
theorem e_eq_gp {m : ℕ} (h3 : 3 ≤ m) (h9 : m ≤ 9) :
    (LineB.Derand.Dm m).toNat / dOf m = LineB.Derand.gp m := by
  interval_cases m <;> decide

/-! ### §5. Final instantiation: residue-dependence at the `PsiMode` level -/

/-- Plus case: `PsiMode` at `t*(N₁)` equals `PsiMode` at `t*(N₂)` when
`N₁ ≡ N₂ [MOD gp m]` (for `m = 3..9`, admissible `N`). -/
theorem psimode_tStar_eq_of_modEq {m : ℕ} [NeZero m] (h3 : 3 ≤ m) (h9 : m ≤ 9)
    {ι : Type*} [Fintype ι] (c : ι → ι → ℂ) (v : ι → Fin m → ℤ)
    {N₁ N₂ : ℕ} [NeZero N₁] [NeZero N₂]
    (hcop₁ : Nat.Coprime (LineD.Defs.Dm m).toNat N₁)
    (hcop₂ : Nat.Coprime (LineD.Defs.Dm m).toNat N₂)
    (hres : N₁ ≡ N₂ [MOD LineB.Derand.gp m]) :
    LineD.Bridge.PsiMode c (fun i => Qform m (v i)) (tStar m N₁ hcop₁)
      = LineD.Bridge.PsiMode c (fun i => Qform m (v i)) (tStar m N₂ hcop₂) := by
  -- Identify the two `D`'s and transfer all numerics to the Derand side.
  have hDid : (LineD.Defs.Dm m).toNat = (LineB.Derand.Dm m).toNat := by
    rw [dm_eq_derand_dm]
  have hDpos : 0 < LineD.Defs.Dm m := by
    rw [dm_eq_derand_dm]
    have h := derand_D_pos h3 h9
    omega
  have hDposN : 0 < (LineD.Defs.Dm m).toNat := by
    rw [hDid]; exact derand_D_pos h3 h9
  have hdD : dOf m ∣ (LineD.Defs.Dm m).toNat := by
    rw [hDid]; exact dOf_dvd_derand_D h3 h9
  have he : (LineD.Defs.Dm m).toNat = dOf m * LineB.Derand.gp m := by
    rw [hDid]
    have h := e_eq_gp h3 h9
    have h2 := Nat.div_mul_cancel (dOf_dvd_derand_D h3 h9)
    rw [h] at h2
    rw [← h2]
    exact mul_comm _ _
  have hQd : ∀ i, (dOf m : ℤ) ∣ 2 * Qform m (v i) := by
    intro i
    exact two_mul_Qform_dvd (fun i' j' => xm_entry_fin h3 h9 i' j') (v i)
  -- The `k`-congruence at the boundary's modulus `gp m`.
  have heD : LineB.Derand.gp m ∣ (LineD.Defs.Dm m).toNat := ⟨dOf m, by rw [he, mul_comm]⟩
  have hc₁ : Nat.Coprime N₁ (LineB.Derand.gp m) :=
    (Nat.Coprime.coprime_dvd_left heD hcop₁).symm
  have hdiff : (LineB.Derand.gp m : ℤ) ∣ (kStar m N₁ - kStar m N₂) :=
    k_sub_dvd_of_modEq m N₁ N₂ _ hcop₁ hcop₂ hDpos heD hc₁ hres
  exact psimode_eq_of_edvd_diff c (fun i => Qform m (v i)) hDposN hdD he hQd
    (tStar m N₁ hcop₁) (tStar m N₂ hcop₂) (kStar m N₁) (kStar m N₂)
    (tStar_eq m N₁ hcop₁ hDpos) (tStar_eq m N₂ hcop₂ hDpos) hdiff

/-- Minus case: `PsiMode` at `t*(N₁)` equals `PsiMode` at `t*(N₂)` when
`N₁ + N₂ ≡ 0 [MOD gp m]` (for `m = 3..9`, admissible `N`), under
symmetric covariances. -/
theorem psimode_tStar_eq_of_negModEq {m : ℕ} [NeZero m] (h3 : 3 ≤ m) (h9 : m ≤ 9)
    {ι : Type*} [Fintype ι] (c : ι → ι → ℂ) (v : ι → Fin m → ℤ)
    {N₁ N₂ : ℕ} [NeZero N₁] [NeZero N₂]
    (hcop₁ : Nat.Coprime (LineD.Defs.Dm m).toNat N₁)
    (hcop₂ : Nat.Coprime (LineD.Defs.Dm m).toNat N₂)
    (hres : (N₁ + N₂) ≡ 0 [MOD LineB.Derand.gp m])
    (hc : ∀ n n', c n n' = c n' n) :
    LineD.Bridge.PsiMode c (fun i => Qform m (v i)) (tStar m N₁ hcop₁)
      = LineD.Bridge.PsiMode c (fun i => Qform m (v i)) (tStar m N₂ hcop₂) := by
  have hDid : (LineD.Defs.Dm m).toNat = (LineB.Derand.Dm m).toNat := by
    rw [dm_eq_derand_dm]
  have hDpos : 0 < LineD.Defs.Dm m := by
    rw [dm_eq_derand_dm]
    have h := derand_D_pos h3 h9
    omega
  have hDposN : 0 < (LineD.Defs.Dm m).toNat := by
    rw [hDid]; exact derand_D_pos h3 h9
  have hdD : dOf m ∣ (LineD.Defs.Dm m).toNat := by
    rw [hDid]; exact dOf_dvd_derand_D h3 h9
  have he : (LineD.Defs.Dm m).toNat = dOf m * LineB.Derand.gp m := by
    rw [hDid]
    have h := e_eq_gp h3 h9
    have h2 := Nat.div_mul_cancel (dOf_dvd_derand_D h3 h9)
    rw [h] at h2
    rw [← h2]
    exact mul_comm _ _
  have hQd : ∀ i, (dOf m : ℤ) ∣ 2 * Qform m (v i) := by
    intro i
    exact two_mul_Qform_dvd (fun i' j' => xm_entry_fin h3 h9 i' j') (v i)
  have heD : LineB.Derand.gp m ∣ (LineD.Defs.Dm m).toNat := ⟨dOf m, by rw [he, mul_comm]⟩
  have hc₁ : Nat.Coprime N₁ (LineB.Derand.gp m) :=
    (Nat.Coprime.coprime_dvd_left heD hcop₁).symm
  have hdiff : (LineB.Derand.gp m : ℤ) ∣ (kStar m N₁ + kStar m N₂) :=
    k_add_dvd_of_negModEq m N₁ N₂ _ hcop₁ hcop₂ hDpos heD hc₁ hres
  exact psimode_eq_of_edvd_sum c (fun i => Qform m (v i)) hDposN hdD he hQd
    (tStar m N₁ hcop₁) (tStar m N₂ hcop₂) (kStar m N₁) (kStar m N₂)
    (tStar_eq m N₁ hcop₁ hDpos) (tStar_eq m N₂ hcop₂ hDpos) hdiff hc

/- Axiom audit for all main theorems of this module. -/
#print axioms PhaseLemma.dvd_Dr_sub_one
#print axioms PhaseLemma.kStar_mul
#print axioms PhaseLemma.tStar_eq
#print axioms PhaseLemma.Nk_eq_neg_one_zmod
#print axioms PhaseLemma.zmod_k_eq_of_mul_eq
#print axioms PhaseLemma.k_sub_dvd_of_modEq
#print axioms PhaseLemma.k_add_dvd_of_negModEq
#print axioms PhaseLemma.psimode_eq_of_phase_int
#print axioms PhaseLemma.phase_real
#print axioms PhaseLemma.phase_int_of_edvd
#print axioms PhaseLemma.phase_int_of_edvd_sum
#print axioms PhaseLemma.psimode_eq_of_edvd_diff
#print axioms PhaseLemma.psimode_eq_of_edvd_sum
#print axioms PhaseLemma.two_mul_Qform_dvd
#print axioms PhaseLemma.xm_entry_fin
#print axioms PhaseLemma.derand_D_pos
#print axioms PhaseLemma.dOf_pos
#print axioms PhaseLemma.dOf_dvd_derand_D
#print axioms PhaseLemma.e_eq_gp
#print axioms PhaseLemma.psimode_tStar_eq_of_modEq
#print axioms PhaseLemma.psimode_tStar_eq_of_negModEq

end PhaseLemma
end LineD
end Bgs
