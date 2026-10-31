/-
  Bgs/LineDOrbitPair.lean — orbit-pair infrastructure for TRACE-151 + TRACE-149.

  What this module is
  -------------------
  The finite, algebraic core of the two Line D claims:

  * TRACE-151: Psi_m(s/D) as a sum over pairs (ξ, ξ') in Fix_m, with weights
    phihat_s and the Kluyver/Gaussian factor ω.
  * TRACE-149: the mode sum whose theta-average is Psi_m(t_N); the bridge
    theorem itself lives in LineDBridge (it needs the ensemble functional).

  What this module proves (no sorry / axiom / native_decide)
  -----------------------------------------------------------
  * `Fix m` — the faithful finite model of Fix_m = {ξ : H_m ξ ∈ ℤ^m} mod 1,
    as the kernel of H_m modulo D_m, with `fix_lift_mem` / `fix_lift_unique`
    (the lift correspondence, over ℤ, no rationals needed).
  * `V4 m` — the kernel of H_m mod 4 (the object of LineDCerts `rad_count`),
    and `Deff m = D_m / |V4 m|` with the table for m = 3..6; the
    m = 7 row (57121) is PENDING — kernel `decide` for m = 7 is
    OOM-killed (exit 137) on this VM in every configuration tried;
    the values are confirmed externally, see the report.
  * `PsiPair` — the pair sum of 151, its diagonal/off-diagonal split
    (`psiPair_diag_split`), and the support-sum lemma (`diag_sum_eq`):
    if |φ|² takes only the values 0 and c, the diagonal sum is c · |support|.
  * `pair_sum_eq_zero_of_involution_neg` — the exact finite vanishing lemma
    that turns the 157 `hdiag` hypothesis package into a theorem about
    Fix_m pairs, once an involution σ with g(σa, σb) = -g a b is supplied.
  * `bridge_154` / `bridge_154_not_dvd` — the 154 bound applied to the
    φ-support subtype of Fix_m, closing the "concrete carrier" gap of
    LineDParity (the Γ-action on the support is the hypothesis `hInv`;
    Γ itself, its generators and the phihat values are NOT invented here).

  What is deliberately NOT claimed
  ---------------------------------
  * `Fintype.card (Fix m) = D_m` (needs Smith normal form / elementary
    divisors; not checked in Mathlib 4.33.1, not assumed).
  * The values of phihat_s, the independence of the support from s
    (Line B Prop R), the Γ-generators and their action on Fix_m, the
    formula Tr U^m, the theta-averaging, |Tr M_N^m| = 1 — all analytic
    inputs, kept as explicit hypotheses in LineDBridge / downstream modules.
  * `det H_m = Tr S^m - 2` in general m (eigenvalue product; separate
    project). Tables for small m are proved by computation only.
-/

import Bgs.LineDDefs
import Bgs.LineDParity
import Mathlib.Data.Complex.Basic
import Mathlib.GroupTheory.GroupAction.Defs

namespace Bgs
namespace LineD
namespace OrbitPair

open Matrix Finset
open Bgs.LineD.Defs

/-- Fix_m as a finite type: the kernel of H_m modulo D_m.

    Correspondence with the boundary's Fix_m = {ξ : H_m ξ ∈ ℤ^m} mod 1:
    if ξ has H_m ξ ∈ ℤ^m, then D_m ξ ∈ ℤ^m (adjugate: X_m H_m = D_m I), so
    ξ mod 1 is determined by D_m ξ mod D_m, and D_m ξ mod D_m lies in this
    kernel; conversely `fix_lift_mem` shows every lift with D_m ∣ H_m y
    gives a point here, and `fix_lift_unique` shows the lift is unique
    modulo D_m. The equality `card (Fix m) = D_m` itself is NOT proved
    here (it needs Smith normal form); see the module header. -/
def Fix (m : ℕ) [NeZero m] : Type :=
  { y : ZMod m → ZMod (Dm m).toNat //
    (Hmat m ℤ).map (Int.castRingHom (ZMod (Dm m).toNat)) *ᵥ y = 0 }

/-- The subtype Fintype instance. Typeclass search does not unfold the
    `Fix` definition, so the instance is given explicitly. -/
instance Fix.fintype (m : ℕ) [NeZero m] : Fintype (Fix m) := by
  have hD : NeZero (Dm m).toNat :=
    ⟨fun hc => by
      rw [Int.toNat_eq_zero] at hc
      have h := Dm_pos m
      omega⟩
  unfold Fix
  infer_instance

/-- Same definitional-unfolding point as `Fix.fintype`: `erase` and
    other Finset operations need `DecidableEq (Fix m)`. -/
instance Fix.decidableEq (m : ℕ) [NeZero m] : DecidableEq (Fix m) := by
  unfold Fix
  infer_instance

/-- V[4]: the kernel of H_m mod 4 (the object of LineDCerts `rad_count`).
    |V[4]| is the denominator in D_eff = D_m / |V[4]|. -/
def V4 (m : ℕ) [NeZero m] : Type :=
  { y : ZMod m → ZMod 4 //
    (Hmat m ℤ).map (Int.castRingHom (ZMod 4)) *ᵥ y = 0 }

/-- Same definitional-unfolding point as `Fix.fintype`. -/
instance V4.fintype (m : ℕ) [NeZero m] : Fintype (V4 m) := by
  unfold V4
  infer_instance

/-- A lift y : ZMod m → ℤ with D_m ∣ (H_m y)_i for every i determines a
    point of Fix_m (its reduction mod D_m). The reduced vector is written
    as a composition so that `RingHom.map_mulVec` applies syntactically. -/
theorem fix_lift_mem (m : ℕ) [NeZero m] (y : ZMod m → ℤ)
    (hy : ∀ i, (Dm m) ∣ (Hmat m ℤ *ᵥ y) i) :
    (Hmat m ℤ).map (Int.castRingHom (ZMod (Dm m).toNat)) *ᵥ
      (Int.castRingHom (ZMod (Dm m).toNat) ∘ y) = 0 := by
  funext i
  simp only [Pi.zero_apply]
  rw [← RingHom.map_mulVec]
  show (((Hmat m ℤ *ᵥ y) i : ℤ) : ZMod (Dm m).toNat) = 0
  rw [ZMod.intCast_zmod_eq_zero_iff_dvd]
  have hD : ((Dm m).toNat : ℤ) = Dm m := Int.toNat_of_nonneg (le_of_lt (Dm_pos m))
  rw [hD]
  exact hy i

/-- Two lifts give the same point of Fix_m iff they agree modulo D_m. -/
theorem fix_lift_unique (m : ℕ) [NeZero m] (y y' : ZMod m → ℤ)
    (h : (fun i => ((y i : ℤ) : ZMod (Dm m).toNat))
      = fun i => ((y' i : ℤ) : ZMod (Dm m).toNat)) :
    ∀ i, (Dm m) ∣ (y' i - y i) := by
  intro i
  have hi := congrFun h i
  rw [ZMod.intCast_eq_intCast_iff_dvd_sub] at hi
  have hD : ((Dm m).toNat : ℤ) = Dm m := Int.toNat_of_nonneg (le_of_lt (Dm_pos m))
  rwa [hD] at hi

/-- D_eff = D_m / |V[4]| (151: the effective support size; |phihat_s|²
    takes values in {0, |V[4]| / D_m}, so the diagonal sum is D_eff · c
    after the support-sum lemma, with c = |V[4]| / D_m). -/
def Deff (m : ℕ) [NeZero m] : ℤ := Dm m / (Fintype.card (V4 m) : ℤ)

-- Tables: D_m and |V4| for m = 3..6, by kernel computation (decide).
-- The m = 7 row is NOT here: kernel `decide` for det H_7 (and the
-- combined m = 7 file) is OOM-killed (LEAN_EXIT 137) on this VM
-- (7.7 GiB RAM); the values det = 228484, |V4| = 4, Deff = 57121 are
-- confirmed by an external integer computation, see the report.

set_option maxRecDepth 100000 in
set_option maxHeartbeats 3200000 in
theorem Dm_table3 : Dm 3 = 196 := by decide

set_option maxRecDepth 100000 in
set_option maxHeartbeats 3200000 in
theorem Dm_table4 : Dm 4 = 1152 := by decide

set_option maxRecDepth 100000 in
set_option maxHeartbeats 3200000 in
theorem Dm_table5 : Dm 5 = 6724 := by decide

set_option maxRecDepth 100000 in
set_option maxHeartbeats 3200000 in
theorem Dm_table6 : Dm 6 = 39200 := by decide

set_option maxRecDepth 100000 in
set_option maxHeartbeats 3200000 in
theorem V4_card3 : Fintype.card (V4 3) = 4 := by decide

set_option maxRecDepth 100000 in
set_option maxHeartbeats 3200000 in
theorem V4_card4 : Fintype.card (V4 4) = 16 := by decide

set_option maxRecDepth 100000 in
set_option maxHeartbeats 3200000 in
theorem V4_card5 : Fintype.card (V4 5) = 4 := by decide

set_option maxRecDepth 100000 in
set_option maxHeartbeats 3200000 in
theorem V4_card6 : Fintype.card (V4 6) = 8 := by decide

/-- D_eff table for m = 3..6: 49, 72, 1681, 4900 (boundary 151);
    the m = 7 value 57121 is pending on the m = 7 decides (OOM, see above). -/
theorem Deff_table :
    Deff 3 = 49 ∧ Deff 4 = 72 ∧ Deff 5 = 1681 ∧ Deff 6 = 4900 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [Deff, Dm_table3, Dm_table4, Dm_table5, Dm_table6,
      V4_card3, V4_card4, V4_card5, V4_card6] <;> norm_num

/-- Psi_m(s/D) as a pair sum over Fix_m (151, orbit-pair formula).

    * `φ : ℤ → Fix m → ℂ` — the weights phihat_s (s is the numerator).
    * `S : Fix m → K → ℝ` — the values S_k(ξ) (k ranges over the mode set).
    * `ω : K → ℝ → ℂ` — the Kluyver/Gaussian factor (J0 or Gaussian).
    * `η : ℝ` — the kick parameter.
    The sum is the boundary's
    `∑_{ξ, ξ'} phihat_s(ξ) conj phihat_s(ξ') ∏_k ω_k(η(S_k(ξ) - S_k(ξ')))`.
    The values of φ and the identification of S with the kick orbit sum
    are analytic inputs, kept as parameters, not invented. -/
noncomputable def PsiPair (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (φ : ℤ → Fix m → ℂ) (S : Fix m → K → ℝ) (ω : K → ℝ → ℂ) (η : ℝ)
    (s : ℤ) : ℂ :=
  ∑ ξ : Fix m, ∑ ξ' : Fix m,
    φ s ξ * star (φ s ξ') * ∏ k, ω k (η * (S ξ k - S ξ' k))

/-- Diagonal/off-diagonal split of the pair sum. The diagonal term is
    `φ ξ * star (φ ξ) * ∏ k, ω k 0`; with the hypothesis `ω k 0 = 1`
    (true for both J0 and the Gaussian) it is exactly |φ ξ|². -/
theorem psiPair_diag_split (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (φ : ℤ → Fix m → ℂ) (S : Fix m → K → ℝ) (ω : K → ℝ → ℂ) (η : ℝ)
    (s : ℤ) :
    PsiPair m φ S ω η s
      = (∑ ξ : Fix m, φ s ξ * star (φ s ξ) * ∏ k, ω k 0)
        + ∑ ξ : Fix m, ∑ ξ' ∈ Finset.univ.erase ξ,
            φ s ξ * star (φ s ξ') * ∏ k, ω k (η * (S ξ k - S ξ' k)) := by
  unfold PsiPair
  have hξ : ∀ ξ : Fix m,
      (∑ ξ' : Fix m, φ s ξ * star (φ s ξ') * ∏ k, ω k (η * (S ξ k - S ξ' k)))
        = φ s ξ * star (φ s ξ) * ∏ k, ω k 0
          + ∑ ξ' ∈ Finset.univ.erase ξ,
              φ s ξ * star (φ s ξ') * ∏ k, ω k (η * (S ξ k - S ξ' k)) := by
    intro ξ
    have hdiag : φ s ξ * star (φ s ξ) * ∏ k, ω k (η * (S ξ k - S ξ k))
        = φ s ξ * star (φ s ξ) * ∏ k, ω k 0 := by
      simp [sub_self]
    rw [← Finset.add_sum_erase _ _ (Finset.mem_univ ξ), hdiag]
  rw [Finset.sum_congr rfl (fun ξ _ => hξ ξ), Finset.sum_add_distrib]

/-- Support of φ in Fix_m: the ξ with φ ξ ≠ 0. The boundary's claim
    (151, Line B Prop R) is that this support is independent of s;
    that independence is an analytic input, NOT proved here — the
    support is defined for one φ at a time. -/
noncomputable def support (m : ℕ) [NeZero m] (φ : Fix m → ℂ) :
    Finset (Fix m) :=
  @Finset.filter _ (fun ξ => φ ξ ≠ 0) (Classical.decPred _) Finset.univ

/-- Support-sum lemma: if |φ|² takes only the values 0 and c, the
    diagonal sum over Fix_m is c · |support|. Combined with
    `psiPair_diag_split` and the boundary values |phihat_s|² ∈
    {0, |V[4]| / D_m}, the diagonal part of Psi_m(s/D) is
    (D_m / |V[4]|) · (|V[4]| / D_m) · |support| in the obvious normalisation;
    the support size itself is the 151 content (Prop R), not proved here. -/
theorem diag_sum_eq (m : ℕ) [NeZero m] (φ : Fix m → ℂ) (c : ℂ)
    (h : ∀ ξ, φ ξ * star (φ ξ) = 0 ∨ φ ξ * star (φ ξ) = c) :
    ∑ ξ : Fix m, φ ξ * star (φ ξ) = c * ((support m φ).card : ℂ) := by
  -- ℂ has no DecidableEq, so the support filter carries Classical.decPred
  -- explicitly; all filter lemmas below are applied with that same
  -- instance, so the rewrite matching is syntactic.
  have hsup : support m φ
      = @Finset.filter _ (fun ξ => φ ξ ≠ 0) (Classical.decPred _) Finset.univ := rfl
  rw [hsup]
  have hnot : ∑ ξ ∈ @Finset.filter _ (fun ξ => ¬ φ ξ ≠ 0)
        (fun ξ => Classical.propDecidable (¬ φ ξ ≠ 0)) Finset.univ,
      φ ξ * star (φ ξ) = 0 := by
    apply Finset.sum_eq_zero
    intro ξ hξ
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hξ
    have hφ : φ ξ = 0 := by simpa using hξ
    rw [hφ]
    simp
  have hfil : ∑ ξ ∈ @Finset.filter _ (fun ξ => φ ξ ≠ 0)
        (Classical.decPred _) Finset.univ,
      φ ξ * star (φ ξ)
      = ((@Finset.filter _ (fun ξ => φ ξ ≠ 0) (Classical.decPred _)
          Finset.univ).card : ℂ) * c := by
    have hterm : ∀ ξ ∈ @Finset.filter _ (fun ξ => φ ξ ≠ 0)
          (Classical.decPred _) Finset.univ,
        φ ξ * star (φ ξ) = c := by
      intro ξ hξ
      simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hξ
      rcases h ξ with h0 | hc
      · exfalso
        apply hξ
        rcases mul_eq_zero.mp h0 with hφ | hφs
        · exact hφ
        · exact star_eq_zero.mp hφs
      · exact hc
    rw [Finset.sum_congr rfl hterm, Finset.sum_const, nsmul_eq_mul]
  calc ∑ ξ : Fix m, φ ξ * star (φ ξ)
      = (∑ ξ ∈ @Finset.filter _ (fun ξ => φ ξ ≠ 0) (Classical.decPred _)
          Finset.univ, φ ξ * star (φ ξ))
        + ∑ ξ ∈ @Finset.filter _ (fun ξ => ¬ φ ξ ≠ 0)
          (fun ξ => Classical.propDecidable (¬ φ ξ ≠ 0))
          Finset.univ, φ ξ * star (φ ξ) :=
        (@Finset.sum_filter_add_sum_filter_not (Fix m) ℂ _ Finset.univ
          (fun ξ => φ ξ ≠ 0) (Classical.decPred _)
          (fun ξ => Classical.propDecidable (¬ φ ξ ≠ 0))
          (fun ξ => φ ξ * star (φ ξ))).symm
    _ = ((@Finset.filter _ (fun ξ => φ ξ ≠ 0) (Classical.decPred _)
          Finset.univ).card : ℂ) * c + 0 := by
        rw [hfil, hnot]
    _ = c * ((@Finset.filter _ (fun ξ => φ ξ ≠ 0) (Classical.decPred _)
          Finset.univ).card : ℂ) := by
        rw [add_zero, mul_comm]

/-- Vanishing of a finite sum under an involution that negates the
    summand. This is the exact finite step behind the 157 diagonal
    vanishing: with σ the Gamma-pairing involution and
    g(ξ, ξ') the summand, `hneg` is the pairing input, and the
    conclusion is the vanishing of the total sum — no analysis. -/
theorem sum_eq_zero_of_involution_neg {α : Type*} [Fintype α] (f : α → ℂ)
    (σ : α → α) (hσ : Function.Involutive σ) (hneg : ∀ a, f (σ a) = -f a) :
    ∑ a, f a = 0 := by
  have h1 : ∑ a, f (σ a) = ∑ a, f a :=
    Equiv.sum_comp (Equiv.ofBijective σ hσ.bijective) f
  have h2 : ∑ a, f (σ a) = -∑ a, f a := by
    calc ∑ a, f (σ a) = ∑ a, -f a :=
          Finset.sum_congr rfl (fun a _ => hneg a)
      _ = -∑ a, f a := Finset.sum_neg_distrib _
  have hS : (∑ a, f a) = -(∑ a, f a) := h1.symm.trans h2
  have hSS : (∑ a, f a) + (∑ a, f a) = 0 := by
    nth_rewrite 1 [hS]
    exact neg_add_cancel _
  have h2S : (2 : ℂ) * (∑ a, f a) = 0 := by rw [two_mul]; exact hSS
  exact (mul_eq_zero.mp h2S).resolve_left (by norm_num)

/-- Pair version of the involution-vanishing lemma, for pair sums over
    Fix_m (the form the 157 `hdiag` package needs). -/
theorem pair_sum_eq_zero_of_involution_neg {α : Type*} [Fintype α]
    (g : α → α → ℂ) (σ : α → α) (hσ : Function.Involutive σ)
    (hneg : ∀ a b, g (σ a) (σ b) = -g a b) :
    ∑ a, ∑ b, g a b = 0 := by
  have hprod : (∑ a, ∑ b, g a b) = ∑ p : α × α, g p.1 p.2 :=
    (Fintype.sum_prod_type (fun p : α × α => g p.1 p.2)).symm
  rw [hprod]
  apply sum_eq_zero_of_involution_neg (fun p : α × α => g p.1 p.2)
    (fun p => (σ p.1, σ p.2))
  · intro p
    obtain ⟨a, b⟩ := p
    exact Prod.ext (hσ a) (hσ b)
  · intro p
    exact hneg p.1 p.2

/-- The Γ-action on the φ-support, from invariance of the support.
    This is a definition, not an instance: the caller supplies it as the
    instance when applying `bridge_154` (see `supportMulAction`). -/
@[instance_reducible]
noncomputable def supportSMul (m : ℕ) [NeZero m]
    {G : Type*} [Group G] [MulAction G (Fix m)]
    (φ : Fix m → ℂ)
    (hInv : ∀ (g : G) (ξ : Fix m), ξ ∈ support m φ → g • ξ ∈ support m φ) :
    SMul G ↥(support m φ) :=
  ⟨fun g x => ⟨g • x.1, hInv g x.1 x.2⟩⟩

/-- The SemigroupAction structure on the φ-support, from invariance
    (in this Mathlib version `MulAction` extends `SemigroupAction`,
    which carries the `SMul`). -/
@[instance_reducible]
noncomputable def supportSemigroupAction (m : ℕ) [NeZero m]
    {G : Type*} [Group G] [MulAction G (Fix m)]
    (φ : Fix m → ℂ)
    (hInv : ∀ (g : G) (ξ : Fix m), ξ ∈ support m φ → g • ξ ∈ support m φ) :
    SemigroupAction G ↥(support m φ) :=
  { toSMul := supportSMul m φ hInv
    mul_smul := fun g h x => Subtype.ext (mul_smul g h x.1) }

/-- The MulAction structure on the φ-support, from invariance. -/
@[instance_reducible]
noncomputable def supportMulAction (m : ℕ) [NeZero m]
    {G : Type*} [Group G] [MulAction G (Fix m)]
    (φ : Fix m → ℂ)
    (hInv : ∀ (g : G) (ξ : Fix m), ξ ∈ support m φ → g • ξ ∈ support m φ) :
    MulAction G ↥(support m φ) :=
  { toSemigroupAction := supportSemigroupAction m φ hInv
    one_smul := fun x => Subtype.ext (one_smul G x.1) }

/-- Bridge to 154: the 154 bound applied to the φ-support subtype of
    Fix_m. This closes the "concrete carrier" gap of LineDParity: the
    carrier is now Fix_m, the subset is the φ-support, and the only
    remaining inputs are the action on the support (supplied, e.g., by
    `supportMulAction` from invariance `hInv`), its compatibility with
    the ambient action (`hAct`, true by `rfl` for the natural action),
    the support size (`hD`, odd square — the 151 content) and the group
    data. Γ itself, its generators and the phihat values are still
    parameters of the caller, not inventions of this module. -/
theorem bridge_154 (m : ℕ) [NeZero m] (hm : 0 < m) (a : ℕ) (ha : Odd a)
    {G : Type*} [Group G] [MulAction G (Fix m)] [Fintype G]
    (φ : Fix m → ℂ)
    [MulAction G ↥(support m φ)]
    (hAct : ∀ (g : G) (x : ↥(support m φ)), (g • x).1 = g • x.1)
    (hD : (support m φ).card = a * a) (hG : Fintype.card G = 2 * m)
    (ρ : G) (hρ : ρ * ρ = 1) (hρ1 : ρ ≠ 1) :
    (2 * m : ℚ) - Bgs.LineD.Parity.Bsym G ↥(support m φ)
        ≥ (m : ℚ) / (Fintype.card ↥(support m φ) : ℚ)
      ∧ Bgs.LineD.Parity.Bsym G ↥(support m φ) < (2 * m : ℚ) := by
  classical
  have hD' : Fintype.card ↥(support m φ) = a * a := by
    rw [Fintype.card_coe]
    exact hD
  exact Bgs.LineD.Parity.sym_bound m hm a ha hD' hG ρ hρ hρ1

/-- Bridge to 154, non-divisibility variant: same conclusion without
    exhibiting ρ, when 2m does not divide the support size. -/
theorem bridge_154_not_dvd (m : ℕ) [NeZero m] (hm : 0 < m)
    {G : Type*} [Group G] [MulAction G (Fix m)] [Fintype G]
    (φ : Fix m → ℂ)
    [MulAction G ↥(support m φ)]
    (hAct : ∀ (g : G) (x : ↥(support m φ)), (g • x).1 = g • x.1)
    (hnot : ¬ (2 * m ∣ Fintype.card ↥(support m φ)))
    (hG : Fintype.card G = 2 * m) :
    (2 * m : ℚ) - Bgs.LineD.Parity.Bsym G ↥(support m φ)
        ≥ (m : ℚ) / (Fintype.card ↥(support m φ) : ℚ)
      ∧ Bgs.LineD.Parity.Bsym G ↥(support m φ) < (2 * m : ℚ) := by
  classical
  exact Bgs.LineD.Parity.sym_bound_of_not_dvd m hm hG hnot

#print axioms Fix.fintype
#print axioms Fix.decidableEq
#print axioms V4.fintype
#print axioms supportSMul
#print axioms supportSemigroupAction
#print axioms supportMulAction
#print axioms fix_lift_mem
#print axioms fix_lift_unique
#print axioms Deff_table
#print axioms psiPair_diag_split
#print axioms diag_sum_eq
#print axioms sum_eq_zero_of_involution_neg
#print axioms pair_sum_eq_zero_of_involution_neg
#print axioms bridge_154
#print axioms bridge_154_not_dvd

end OrbitPair
end LineD
end Bgs
