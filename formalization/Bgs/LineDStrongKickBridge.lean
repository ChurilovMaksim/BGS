import Bgs.LineDOrbitPairFull
import Bgs.LineDStrongKick
import Bgs.LineDParity

/-!
# Bridge: the strong-kick limit at the concrete weights `phihatFix`

Instantiates `StrongKick.strong_kick_limit` with the concrete data of
`LineDOrbitPairFull`: `G = DihedralGroup m` acting by
`OrbitPairFull.gammaMulAction`, weights `phihatFix m`, the common
square value `c = |V[4]| / D_m`, and `D = card (support)`.

What is proved here (all with standard axioms, no `sorry`):
* Γ-invariance of `phihatFix` (via the permutation action on the
  quotient `Vquot`, the adjugate commutation, and the pairing
  invariance);
* the common square value on the support (from
  `phihatFix_modulus_values`);
* the normalisation `∑_{ξ : Fix m} |phihatFix ξ|² = 1` (character
  dichotomy over `Vquot`), hence support nonemptiness and
  `c * card support = 1`.

What stays as explicit hypotheses of the final theorem: the
Kluyver/Gaussian factor data (`hω0`, `hωbound`, `hωlim`) and the
mode-separation data (`hSInv`, `hSep`). These are outside 151:
they concern the concrete mode sums `S_k`, not the weights.
-/

namespace Bgs
namespace LineD
namespace StrongKickBridge

open Bgs.LineD
open Finset Filter Topology
open scoped Matrix

/-! ### §1. The dihedral permutation: bijectivity and commutation -/

/-- The dihedral index permutation is bijective (by cases: a shift
    has inverse `· - k`, a reflection is its own inverse). -/
theorem gammaPerm_bijective (m : ℕ) (g : DihedralGroup m) :
    Function.Bijective (OrbitPairFull.gammaPerm m g) := by
  cases g with
  | r k =>
    show Function.Bijective (fun j : ZMod m => j + k)
    exact (Equiv.addRight k).bijective
  | sr k =>
    apply Function.bijective_iff_has_inverse.mpr
    refine ⟨fun j => k - j, fun j => ?_, fun j => ?_⟩ <;>
      show k - (k - j) = j
    · exact sub_sub_self k j
    · exact sub_sub_self k j

/-- The permutation of a product of dihedral elements composes in
    reverse order (this is the content of `gammaMulAction`'s
    `mul_smul` proof, restated for plain vectors). -/
theorem gammaPerm_mul (m : ℕ) (g h : DihedralGroup m) (j : ZMod m) :
    OrbitPairFull.gammaPerm m (g * h) j
      = OrbitPairFull.gammaPerm m h (OrbitPairFull.gammaPerm m g j) := by
  cases g <;> cases h <;>
    simp only [OrbitPairFull.gammaPerm, DihedralGroup.r_mul_r,
      DihedralGroup.r_mul_sr, DihedralGroup.sr_mul_r,
      DihedralGroup.sr_mul_sr] <;>
    ring

/-- The inverse permutation, applied after the permutation, is the
    identity. -/
theorem gammaPerm_inv_apply (m : ℕ) (g : DihedralGroup m) (j : ZMod m) :
    OrbitPairFull.gammaPerm m g⁻¹ (OrbitPairFull.gammaPerm m g j) = j := by
  rw [← gammaPerm_mul, mul_inv_cancel, DihedralGroup.one_def]
  simp [OrbitPairFull.gammaPerm]

/-- The permutation, applied after the inverse permutation, is the
    identity. -/
theorem gammaPerm_apply_inv (m : ℕ) (g : DihedralGroup m) (j : ZMod m) :
    OrbitPairFull.gammaPerm m g (OrbitPairFull.gammaPerm m g⁻¹ j) = j := by
  rw [← gammaPerm_mul, inv_mul_cancel, DihedralGroup.one_def]
  simp [OrbitPairFull.gammaPerm]

/-- The adjugate commutes with coordinate permutations: `X` is a
    polynomial in `H` (adjugate), and `H` commutes with `Γ` by
    `Hmat_mulVec_comp_gammaPerm`; the clean proof goes through the
    triviality of the integral kernel of `H`. -/
theorem Xmat_mulVec_comp_gammaPerm (m : ℕ) [NeZero m]
    (x : ZMod m → ℤ) (g : DihedralGroup m) :
    Defs.Xmat m *ᵥ (x ∘ OrbitPairFull.gammaPerm m g)
      = (Defs.Xmat m *ᵥ x) ∘ OrbitPairFull.gammaPerm m g := by
  have hH : Defs.Hmat m ℤ *ᵥ
      (Defs.Xmat m *ᵥ (x ∘ OrbitPairFull.gammaPerm m g)
        - (Defs.Xmat m *ᵥ x) ∘ OrbitPairFull.gammaPerm m g) = 0 := by
    rw [Matrix.mulVec_sub]
    have h1 : Defs.Hmat m ℤ *ᵥ
        (Defs.Xmat m *ᵥ (x ∘ OrbitPairFull.gammaPerm m g))
        = Defs.Dm m • (x ∘ OrbitPairFull.gammaPerm m g) := by
      rw [Matrix.mulVec_mulVec, Defs.Hmat_mul_Xmat, Matrix.smul_mulVec,
        Matrix.one_mulVec]
    have h2 : Defs.Hmat m ℤ *ᵥ
        ((Defs.Xmat m *ᵥ x) ∘ OrbitPairFull.gammaPerm m g)
        = Defs.Dm m • (x ∘ OrbitPairFull.gammaPerm m g) := by
      rw [OrbitPairFull.Hmat_mulVec_comp_gammaPerm, Matrix.mulVec_mulVec,
        Defs.Hmat_mul_Xmat, Matrix.smul_mulVec, Matrix.one_mulVec]
      funext j
      rfl
    rw [h1, h2, sub_self]
  have h0 := OrbitPairFull.Hmat_mulVec_eq_zero m _ hH
  exact sub_eq_zero.mp h0

/-- The pairing is invariant under simultaneous permutation of both
    arguments (the adjugate commutes with `Γ`, then reindex the dot
    product by the bijective permutation). -/
theorem pairNum_comp_gammaPerm (m : ℕ) [NeZero m]
    (y w : ZMod m → ℤ) (g : DihedralGroup m) :
    OrbitPairFull.pairNum m (y ∘ OrbitPairFull.gammaPerm m g)
        (w ∘ OrbitPairFull.gammaPerm m g)
      = OrbitPairFull.pairNum m y w := by
  show (Defs.Xmat m *ᵥ (y ∘ OrbitPairFull.gammaPerm m g)) ⬝ᵥ
      (w ∘ OrbitPairFull.gammaPerm m g) = (Defs.Xmat m *ᵥ y) ⬝ᵥ w
  rw [Xmat_mulVec_comp_gammaPerm]
  show (∑ i, ((Defs.Xmat m *ᵥ y) ∘ OrbitPairFull.gammaPerm m g) i
      * (w ∘ OrbitPairFull.gammaPerm m g) i)
    = ∑ i, (Defs.Xmat m *ᵥ y) i * w i
  exact Equiv.sum_comp (Equiv.ofBijective (OrbitPairFull.gammaPerm m g)
    (gammaPerm_bijective m g))
    (fun i => (Defs.Xmat m *ᵥ y) i * w i)

/-- The quadratic-form numerator is invariant under permutation. -/
theorem Qnum_comp_gammaPerm (m : ℕ) [NeZero m]
    (y : ZMod m → ℤ) (g : DihedralGroup m) :
    OrbitPairFull.Qnum m (y ∘ OrbitPairFull.gammaPerm m g)
      = OrbitPairFull.Qnum m y :=
  pairNum_comp_gammaPerm m y y g

#print axioms gammaPerm_bijective
#print axioms gammaPerm_mul
#print axioms gammaPerm_inv_apply
#print axioms gammaPerm_apply_inv
#print axioms Xmat_mulVec_comp_gammaPerm
#print axioms pairNum_comp_gammaPerm
#print axioms Qnum_comp_gammaPerm

/-! ### §2. The permutation action on `Vquot` and invariance of `phihat` -/

/-- The permutation action on the quotient `Vquot`, defined on
    representatives: `π • [y] = [y ∘ π]`. Well-defined since the
    `H`-range is `π`-stable (`Hmat_mulVec_comp_gammaPerm`). -/
noncomputable def vquotPerm (m : ℕ) [NeZero m] (g : DihedralGroup m) :
    OrbitPairFull.Vquot m → OrbitPairFull.Vquot m :=
  Quotient.lift
    (fun y => Submodule.Quotient.mk (y ∘ OrbitPairFull.gammaPerm m g)) (by
      intro y y' hy
      have h2 : (LinearMap.range (Matrix.mulVecLin (Defs.Hmat m ℤ))).quotientRel
          y y' := hy
      rw [Submodule.quotientRel_def] at h2
      obtain ⟨t, ht⟩ := h2
      rw [Matrix.mulVecLin_apply] at ht
      have ha : y = y' + Defs.Hmat m ℤ *ᵥ t := by
        rw [add_comm]
        exact sub_eq_iff_eq_add.mp ht.symm
      apply (Submodule.Quotient.eq _).mpr
      refine ⟨t ∘ OrbitPairFull.gammaPerm m g, ?_⟩
      rw [Matrix.mulVecLin_apply]
      have hyy : y - y' = Defs.Hmat m ℤ *ᵥ t := by
        rw [ha, add_sub_cancel_left]
      calc Defs.Hmat m ℤ *ᵥ (t ∘ OrbitPairFull.gammaPerm m g)
          = (Defs.Hmat m ℤ *ᵥ t) ∘ OrbitPairFull.gammaPerm m g :=
            OrbitPairFull.Hmat_mulVec_comp_gammaPerm m ℤ t g
        _ = (y - y') ∘ OrbitPairFull.gammaPerm m g := by rw [hyy]
        _ = y ∘ OrbitPairFull.gammaPerm m g
            - y' ∘ OrbitPairFull.gammaPerm m g := by
          funext i
          simp [Pi.sub_apply])

/-- The quotient permutation on a representative class. -/
theorem vquotPerm_mk (m : ℕ) [NeZero m] (g : DihedralGroup m)
    (y : ZMod m → ℤ) :
    vquotPerm m g (Submodule.Quotient.mk y)
      = Submodule.Quotient.mk (y ∘ OrbitPairFull.gammaPerm m g) := rfl

/-- The quotient permutation is bijective (inverse: the inverse
    permutation). -/
theorem vquotPerm_bijective (m : ℕ) [NeZero m] (g : DihedralGroup m) :
    Function.Bijective (vquotPerm m g) := by
  apply Function.bijective_iff_has_inverse.mpr
  refine ⟨vquotPerm m g⁻¹, ?_, ?_⟩
  · intro q
    induction q using Quotient.inductionOn with
    | _ y =>
      show vquotPerm m g⁻¹ (vquotPerm m g (Submodule.Quotient.mk y))
        = Submodule.Quotient.mk y
      rw [vquotPerm_mk, vquotPerm_mk]
      congr 1
      funext i
      show y (OrbitPairFull.gammaPerm m g
        (OrbitPairFull.gammaPerm m g⁻¹ i)) = y i
      rw [gammaPerm_apply_inv]
  · intro q
    induction q using Quotient.inductionOn with
    | _ y =>
      show vquotPerm m g (vquotPerm m g⁻¹ (Submodule.Quotient.mk y))
        = Submodule.Quotient.mk y
      rw [vquotPerm_mk, vquotPerm_mk]
      congr 1
      funext i
      show y (OrbitPairFull.gammaPerm m g⁻¹
        (OrbitPairFull.gammaPerm m g i)) = y i
      rw [gammaPerm_inv_apply]

/-- The summand is invariant under simultaneous permutation of the
    point and the summation variable (pairing and quadratic form are
    `Γ`-invariant). -/
theorem phiSummand_perm (m : ℕ) [NeZero m] (s : ℤ)
    (w : ZMod m → ℤ) (g : DihedralGroup m)
    (η : OrbitPairFull.Vquot m) :
    OrbitPairFull.phiSummand m s (w ∘ OrbitPairFull.gammaPerm m g)
        (vquotPerm m g η)
      = OrbitPairFull.phiSummand m s w η := by
  induction η using Quotient.inductionOn with
  | _ y =>
    show OrbitPairFull.phiSummand m s (w ∘ OrbitPairFull.gammaPerm m g)
        (Submodule.Quotient.mk (y ∘ OrbitPairFull.gammaPerm m g))
      = OrbitPairFull.phiSummand m s w (Submodule.Quotient.mk y)
    rw [OrbitPairFull.phiSummand_mk, OrbitPairFull.phiSummand_mk,
      Qnum_comp_gammaPerm, pairNum_comp_gammaPerm]

/-- `phihat` is invariant under the quotient permutation (reindex
    the defining sum by the bijective permutation). -/
theorem phihat_perm (m : ℕ) [NeZero m] (s : ℤ)
    (g : DihedralGroup m) (q : OrbitPairFull.Vquot m) :
    OrbitPairFull.phihat m s (vquotPerm m g q)
      = OrbitPairFull.phihat m s q := by
  induction q using Quotient.inductionOn with
  | _ w =>
    show OrbitPairFull.phihat m s
        (Submodule.Quotient.mk (w ∘ OrbitPairFull.gammaPerm m g))
      = OrbitPairFull.phihat m s (Submodule.Quotient.mk w)
    rw [OrbitPairFull.phihat_mk, OrbitPairFull.phihat_mk]
    have hsum : (∑ η, OrbitPairFull.phiSummand m s
          (w ∘ OrbitPairFull.gammaPerm m g) η)
        = ∑ η, OrbitPairFull.phiSummand m s w η := by
      have h := Equiv.sum_comp (Equiv.ofBijective (vquotPerm m g)
        (vquotPerm_bijective m g))
        (fun η => OrbitPairFull.phiSummand m s
          (w ∘ OrbitPairFull.gammaPerm m g) η)
      rw [← h]
      exact Finset.sum_congr rfl (fun η _ => phiSummand_perm m s w g η)
    rw [hsum]

/-- The backward map intertwines the quotient permutation with the
    `Γ`-action on `Fix`: `quotToFix (π • q) = g • quotToFix q`. -/
theorem quotToFix_perm (m : ℕ) [NeZero m] (g : DihedralGroup m)
    (q : OrbitPairFull.Vquot m) :
    OrbitPairFull.quotToFix m (vquotPerm m g q)
      = g • OrbitPairFull.quotToFix m q := by
  induction q using Quotient.inductionOn with
  | _ w =>
    show OrbitPairFull.quotToFix m
        (Submodule.Quotient.mk (w ∘ OrbitPairFull.gammaPerm m g))
      = g • OrbitPairFull.quotToFix m (Submodule.Quotient.mk w)
    show OrbitPairFull.quotToFixRep m (w ∘ OrbitPairFull.gammaPerm m g)
      = g • OrbitPairFull.quotToFixRep m w
    apply Subtype.ext
    funext i
    show ((Defs.Xmat m *ᵥ (w ∘ OrbitPairFull.gammaPerm m g)) i
        : ZMod (Defs.Dm m).toNat)
      = ((Defs.Xmat m *ᵥ w) (OrbitPairFull.gammaPerm m g i)
        : ZMod (Defs.Dm m).toNat)
    simp only [Xmat_mulVec_comp_gammaPerm, Function.comp_apply]

/-- The forward equivalence intertwines the `Γ`-action with the
    quotient permutation. -/
theorem fixEquivQuot_smul (m : ℕ) [NeZero m] (g : DihedralGroup m)
    (ξ : OrbitPair.Fix m) :
    OrbitPairFull.fixEquivQuot m (g • ξ)
      = vquotPerm m g (OrbitPairFull.fixEquivQuot m ξ) := by
  have key : OrbitPairFull.quotToFix m
        (OrbitPairFull.fixEquivQuot m (g • ξ))
      = OrbitPairFull.quotToFix m
        (vquotPerm m g (OrbitPairFull.fixEquivQuot m ξ)) := by
    have h1 : OrbitPairFull.quotToFix m
        (OrbitPairFull.fixEquivQuot m (g • ξ)) = g • ξ :=
      (OrbitPairFull.fixEquivQuot m).left_inv (g • ξ)
    have h2 : OrbitPairFull.quotToFix m
        (OrbitPairFull.fixEquivQuot m ξ) = ξ :=
      (OrbitPairFull.fixEquivQuot m).left_inv ξ
    rw [quotToFix_perm, h2]
    exact h1
  exact (OrbitPairFull.fixEquivQuot m).symm.injective key

/-- `phihatFix` is `Γ`-invariant: the main invariance input for the
    strong-kick instance (item 2 of the task). -/
theorem phihatFix_smul (m : ℕ) [NeZero m] (s : ℤ)
    (g : DihedralGroup m) (ξ : OrbitPair.Fix m) :
    OrbitPairFull.phihatFix m s (g • ξ)
      = OrbitPairFull.phihatFix m s ξ := by
  show OrbitPairFull.phihat m s (OrbitPairFull.fixEquivQuot m (g • ξ))
    = OrbitPairFull.phihat m s (OrbitPairFull.fixEquivQuot m ξ)
  rw [fixEquivQuot_smul, phihat_perm]

#print axioms vquotPerm_mk
#print axioms vquotPerm_bijective
#print axioms phiSummand_perm
#print axioms phihat_perm
#print axioms quotToFix_perm
#print axioms fixEquivQuot_smul
#print axioms phihatFix_smul

/-! ### §3. The support lemmas: `hSq` and `hInv` -/

/-- Item 1: on the support, `φ * star φ = c` (from the modulus
    values; the `= 0` alternative contradicts support membership). -/
theorem phihatFix_sq (m : ℕ) [NeZero m] (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m))
    (ξ : OrbitPair.Fix m)
    (hξ : ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s)) :
    OrbitPairFull.phihatFix m s ξ * star (OrbitPairFull.phihatFix m s ξ)
      = (Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ) := by
  have hne : OrbitPairFull.phihatFix m s ξ ≠ 0 := by
    simp only [OrbitPair.support, Finset.mem_filter, Finset.mem_univ,
      true_and] at hξ
    exact hξ
  rcases OrbitPairFull.phihatFix_modulus_values m s hs ξ with h | h
  · exact h
  · exfalso
    apply hne
    rcases mul_eq_zero.mp h with h1 | h1
    · exact h1
    · exact star_eq_zero.mp h1

/-- Item 3: the support is `Γ`-invariant (from `Γ`-invariance of
    `phihatFix`). -/
theorem phihatFix_support_inv (m : ℕ) [NeZero m] (s : ℤ)
    (g : DihedralGroup m) (ξ : OrbitPair.Fix m)
    (hξ : ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s)) :
    g • ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s) := by
  have hne : OrbitPairFull.phihatFix m s ξ ≠ 0 := by
    simp only [OrbitPair.support, Finset.mem_filter, Finset.mem_univ,
      true_and] at hξ
    exact hξ
  simp only [OrbitPair.support, Finset.mem_filter, Finset.mem_univ,
    true_and]
  rw [phihatFix_smul]
  exact hne

/-! ### §5. Normalization: the character argument -/

/-- Helper: `eChar (a / D) = 1` iff `D ∣ a` (via
    `Complex.exp_eq_one_iff`). -/
theorem eChar_eq_one_iff_dvd (m : ℕ) [NeZero m] (a : ℤ) :
    OrbitPairFull.eChar (((a : ℚ)) / Defs.Dm m) = 1 ↔ (Defs.Dm m) ∣ a := by
  have hDpos : 0 < Defs.Dm m := Defs.Dm_pos m
  have hDQ : ((Defs.Dm m : ℚ)) ≠ 0 := by exact_mod_cast ne_of_gt hDpos
  have h2pi : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
    apply mul_ne_zero
    · apply mul_ne_zero
      · norm_num
      · exact_mod_cast Real.pi_ne_zero
    · exact Complex.I_ne_zero
  constructor
  · intro h
    have h2 : Complex.exp
        (2 * Real.pi * Complex.I * ((((a : ℚ)) / Defs.Dm m : ℚ) : ℂ)) = 1 := h
    rw [Complex.exp_eq_one_iff] at h2
    obtain ⟨n, hn⟩ := h2
    have hcast : ((((a : ℚ)) / Defs.Dm m : ℚ) : ℂ)
        = (a : ℂ) / (Defs.Dm m : ℂ) := by
      push_cast
      ring
    rw [hcast] at hn
    have hn2 : (a : ℂ) / (Defs.Dm m : ℂ) = (n : ℂ) := by
      rw [mul_comm (n : ℂ)] at hn
      exact mul_left_cancel₀ h2pi hn
    have hnQ : (a : ℚ) / (Defs.Dm m : ℚ) = (n : ℚ) := by
      exact_mod_cast hn2
    have h3 : (a : ℚ) = (Defs.Dm m : ℚ) * n := by
      rw [div_eq_iff hDQ] at hnQ
      rw [mul_comm] at hnQ
      exact hnQ
    exact ⟨n, by exact_mod_cast h3⟩
  · intro h
    obtain ⟨n, hn⟩ := h
    have hnQ : (a : ℚ) / (Defs.Dm m : ℚ) = (n : ℚ) := by
      rw [div_eq_iff hDQ, hn]
      push_cast
      ring
    rw [hnQ]
    exact OrbitPairFull.eChar_int n

/-- The character `q ↦ eChar (−pairNum y w / D)` on `Vquot`,
    defined on representatives. Well-defined since shifting `w` by
    `H t` changes the pairing by a multiple of `D`. -/
noncomputable def vquotChar (m : ℕ) [NeZero m] (y : ZMod m → ℤ) :
    OrbitPairFull.Vquot m → ℂ :=
  Quotient.lift
    (fun w => OrbitPairFull.eChar (((-OrbitPairFull.pairNum m y w : ℤ) : ℚ)
      / Defs.Dm m)) (by
      intro w w' hw
      have h2 : (LinearMap.range (Matrix.mulVecLin (Defs.Hmat m ℤ))).quotientRel
          w w' := hw
      rw [Submodule.quotientRel_def] at h2
      obtain ⟨t, ht⟩ := h2
      rw [Matrix.mulVecLin_apply] at ht
      have ha : w = w' + Defs.Hmat m ℤ *ᵥ t := by
        rw [add_comm]
        exact sub_eq_iff_eq_add.mp ht.symm
      have hP := OrbitPairFull.pairNum_add_right_mod m y w' t
      rw [← ha] at hP
      rw [Int.modEq_iff_dvd] at hP
      obtain ⟨b, hb⟩ := hP
      apply OrbitPairFull.eChar_eq_of_int_sub (k := b)
      have hDQ : ((Defs.Dm m : ℚ)) ≠ 0 := by
        exact_mod_cast ne_of_gt (Defs.Dm_pos m)
      have hbQ : ((OrbitPairFull.pairNum m y w' : ℚ))
          - (OrbitPairFull.pairNum m y w : ℚ)
          = (Defs.Dm m : ℚ) * b := by exact_mod_cast hb
      rw [div_sub_div_same, div_eq_iff hDQ]
      push_cast
      linear_combination hbQ)

/-- The character on a representative class. -/
theorem vquotChar_mk (m : ℕ) [NeZero m] (y w : ZMod m → ℤ) :
    vquotChar m y (Submodule.Quotient.mk w)
      = OrbitPairFull.eChar (((-OrbitPairFull.pairNum m y w : ℤ) : ℚ)
        / Defs.Dm m) := rfl

/-- Character property of `vquotChar`. -/
theorem vquotChar_add (m : ℕ) [NeZero m] (y : ZMod m → ℤ)
    (q₁ q₂ : OrbitPairFull.Vquot m) :
    vquotChar m y (q₁ + q₂) = vquotChar m y q₁ * vquotChar m y q₂ := by
  induction q₁ using Quotient.inductionOn with
  | _ w₁ =>
    induction q₂ using Quotient.inductionOn with
    | _ w₂ =>
      change vquotChar m y (Submodule.Quotient.mk w₁ + Submodule.Quotient.mk w₂)
        = vquotChar m y (Submodule.Quotient.mk w₁)
          * vquotChar m y (Submodule.Quotient.mk w₂)
      rw [← Submodule.Quotient.mk_add, vquotChar_mk, vquotChar_mk, vquotChar_mk,
        ← OrbitPairFull.eChar_add]
      congr 1
      have h : OrbitPairFull.pairNum m y (w₁ + w₂)
          = OrbitPairFull.pairNum m y w₁ + OrbitPairFull.pairNum m y w₂ := by
        show (Defs.Xmat m *ᵥ y) ⬝ᵥ (w₁ + w₂)
          = (Defs.Xmat m *ᵥ y) ⬝ᵥ w₁ + (Defs.Xmat m *ᵥ y) ⬝ᵥ w₂
        exact dotProduct_add _ _ _
      rw [h]
      push_cast
      ring

/-- Character-sum dichotomy, nontrivial case: if the character takes
    a value `≠ 1`, its sum vanishes (reindex by `+ q₀`). -/
theorem vquotChar_sum_eq_zero (m : ℕ) [NeZero m] (y : ZMod m → ℤ)
    (hne : ∃ q₀, vquotChar m y q₀ ≠ 1) :
    (∑ q, vquotChar m y q) = 0 := by
  obtain ⟨q₀, hq₀⟩ := hne
  have hS : (∑ q, vquotChar m y q)
      = (∑ q, vquotChar m y q) * vquotChar m y q₀ := by
    calc ∑ q, vquotChar m y q
        = ∑ q, vquotChar m y (q + q₀) :=
          (Equiv.sum_comp (Equiv.addRight q₀) (vquotChar m y)).symm
      _ = ∑ q, vquotChar m y q * vquotChar m y q₀ :=
          Finset.sum_congr rfl (fun q _ => vquotChar_add m y q q₀)
      _ = (∑ q, vquotChar m y q) * vquotChar m y q₀ :=
          (Finset.sum_mul _ _ _).symm
  have h0 : (∑ q, vquotChar m y q) * (1 - vquotChar m y q₀) = 0 := by
    rw [mul_sub, mul_one, ← hS, sub_self]
  rcases mul_eq_zero.mp h0 with h1 | h1
  · exact h1
  · exfalso
    exact hq₀ (sub_eq_zero.mp h1).symm

/-- Triviality of the character forces the class to vanish: if
    `χ ≡ 1`, then `D ∣ pairNum y w` for all `w`, hence `X y ≡ 0`
    mod `D`, hence `y ∈ H ℤ^m` (via `H X = D • 1` and no torsion in
    `ℤ^m`). -/
theorem vquotChar_triv (m : ℕ) [NeZero m] (y : ZMod m → ℤ)
    (h : ∀ q, vquotChar m y q = 1) :
    (Submodule.Quotient.mk y : OrbitPairFull.Vquot m) = 0 := by
  have h1 : ∀ w, OrbitPairFull.eChar (((-OrbitPairFull.pairNum m y w : ℤ) : ℚ)
      / Defs.Dm m) = 1 := by
    intro w
    have hw := h (Submodule.Quotient.mk w)
    rwa [vquotChar_mk] at hw
  have h2 : ∀ w, (Defs.Dm m) ∣ OrbitPairFull.pairNum m y w := by
    intro w
    have hw := h1 w
    rw [eChar_eq_one_iff_dvd] at hw
    exact dvd_neg.mp hw
  have hsingle : ∀ j, OrbitPairFull.pairNum m y (Pi.single j 1)
      = (Defs.Xmat m *ᵥ y) j := by
    intro j
    show (Defs.Xmat m *ᵥ y) ⬝ᵥ (Pi.single j 1) = (Defs.Xmat m *ᵥ y) j
    show (∑ i, (Defs.Xmat m *ᵥ y) i * ((Pi.single j (1 : ℤ) : ZMod m → ℤ) i))
      = (Defs.Xmat m *ᵥ y) j
    rw [Fintype.sum_eq_single j]
    · simp
    · intro i hi
      rw [Pi.single_eq_of_ne hi, mul_zero]
  have h3 : ∀ j, (Defs.Dm m) ∣ (Defs.Xmat m *ᵥ y) j := by
    intro j
    have hj := h2 (Pi.single j 1)
    rwa [hsingle] at hj
  have hz : ∀ j, ∃ zj, (Defs.Xmat m *ᵥ y) j = Defs.Dm m * zj := fun j => h3 j
  choose z hz using hz
  have hX : Defs.Xmat m *ᵥ y = Defs.Dm m • z := by
    funext j
    rw [Pi.smul_apply, smul_eq_mul]
    exact hz j
  have hHX : Defs.Hmat m ℤ *ᵥ (Defs.Xmat m *ᵥ y) = Defs.Dm m • y := by
    rw [Matrix.mulVec_mulVec, Defs.Hmat_mul_Xmat, Matrix.smul_mulVec,
      Matrix.one_mulVec]
  have hkey : Defs.Dm m • y = Defs.Dm m • (Defs.Hmat m ℤ *ᵥ z) := by
    rw [← hHX, hX, Matrix.mulVec_smul]
  have hy : y = Defs.Hmat m ℤ *ᵥ z := by
    have hDm0 : (Defs.Dm m : ℤ) ≠ 0 := ne_of_gt (Defs.Dm_pos m)
    funext j
    have hj := congrFun hkey j
    simp only [Pi.smul_apply, smul_eq_mul] at hj
    exact mul_left_cancel₀ hDm0 hj
  rw [← Submodule.Quotient.mk_zero]
  apply (Submodule.Quotient.eq _).mpr
  refine ⟨z, ?_⟩
  rw [Matrix.mulVecLin_apply, sub_zero]
  exact hy.symm

/-- The torsion summand as a function of the quotient class: `q ↦
    phiSummand s w γ.1` for any representative `w` of `q`
    (well-defined by `pairNum_add_right_mod`). -/
noncomputable def phiSummandQ (m : ℕ) [NeZero m] (s : ℤ)
    (q : OrbitPairFull.Vquot m) (γ : ↥(OrbitPairFull.torsionSubgroup m)) : ℂ :=
  Quotient.lift (fun w => OrbitPairFull.phiSummand m s w γ.1) (by
    intro w w' hw
    have h2 : (LinearMap.range (Matrix.mulVecLin (Defs.Hmat m ℤ))).quotientRel
        w w' := hw
    rw [Submodule.quotientRel_def] at h2
    obtain ⟨t, ht⟩ := h2
    rw [Matrix.mulVecLin_apply] at ht
    have ha : w = w' + Defs.Hmat m ℤ *ᵥ t := by
      rw [add_comm]
      exact sub_eq_iff_eq_add.mp ht.symm
    show OrbitPairFull.phiSummand m s w γ.1
      = OrbitPairFull.phiSummand m s w' γ.1
    obtain ⟨y, hy⟩ := Quotient.exists_rep γ.1
    rw [← hy]
    show OrbitPairFull.phiSummand m s w (Submodule.Quotient.mk y)
      = OrbitPairFull.phiSummand m s w' (Submodule.Quotient.mk y)
    rw [OrbitPairFull.phiSummand_mk, OrbitPairFull.phiSummand_mk, ha]
    have hP := OrbitPairFull.pairNum_add_right_mod m y w' t
    rw [Int.modEq_iff_dvd] at hP
    obtain ⟨b, hb⟩ := hP
    apply OrbitPairFull.eChar_eq_of_int_sub (k := b)
    have hDQ : ((Defs.Dm m : ℚ)) ≠ 0 := by
      exact_mod_cast ne_of_gt (Defs.Dm_pos m)
    have hbQ : ((OrbitPairFull.pairNum m y w' : ℚ))
        - (OrbitPairFull.pairNum m y (w' + Defs.Hmat m ℤ *ᵥ t) : ℚ)
        = (Defs.Dm m : ℚ) * b := by exact_mod_cast hb
    rw [div_sub_div_same, div_eq_iff hDQ]
    push_cast
    linear_combination hbQ) q

/-- The quotient torsion summand on a representative class. -/
theorem phiSummandQ_mk (m : ℕ) [NeZero m] (s : ℤ)
    (w : ZMod m → ℤ) (γ : ↥(OrbitPairFull.torsionSubgroup m)) :
    phiSummandQ m s (Submodule.Quotient.mk w) γ
      = OrbitPairFull.phiSummand m s w γ.1 := rfl

/-- The modulus identity as a function of the quotient class
    (from `phihat_modulus` by quotient induction). -/
theorem phihat_modulus_Q (m : ℕ) [NeZero m] (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m)) (q : OrbitPairFull.Vquot m) :
    OrbitPairFull.phihat m s q * star (OrbitPairFull.phihat m s q)
      = (Defs.Dm m : ℂ)⁻¹ * ∑ γ : ↥(OrbitPairFull.torsionSubgroup m),
          phiSummandQ m s q γ := by
  induction q using Quotient.inductionOn with
  | _ w =>
    show OrbitPairFull.phihat m s (Submodule.Quotient.mk w)
        * star (OrbitPairFull.phihat m s (Submodule.Quotient.mk w))
      = (Defs.Dm m : ℂ)⁻¹ * ∑ γ : ↥(OrbitPairFull.torsionSubgroup m),
          phiSummandQ m s (Submodule.Quotient.mk w) γ
    rw [OrbitPairFull.phihat_modulus m s hs w,
      Finset.sum_congr rfl (fun γ _ => (phiSummandQ_mk m s w γ).symm)]

/-- The inner sum over the quotient: it is `D` for `γ = 0` (the
    summand is identically `1`) and `0` otherwise (the character
    `vquotChar` is nontrivial, by `vquotChar_triv`). -/
theorem phiSummandQ_inner (m : ℕ) [NeZero m] (s : ℤ)
    (γ : ↥(OrbitPairFull.torsionSubgroup m)) :
    (∑ q, phiSummandQ m s q γ)
      = if γ = 0 then ((Defs.Dm m).toNat : ℂ) else 0 := by
  by_cases hγ : γ = 0
  · rw [if_pos hγ, hγ]
    have h1 : ∀ q, phiSummandQ m s q 0 = 1 := by
      intro q
      induction q using Quotient.inductionOn with
      | _ w =>
        show phiSummandQ m s (Submodule.Quotient.mk w) 0 = 1
        show OrbitPairFull.phiSummand m s w
            (0 : ↥(OrbitPairFull.torsionSubgroup m)).1 = 1
        have h0 : (0 : ↥(OrbitPairFull.torsionSubgroup m)).1
            = Submodule.Quotient.mk 0 := by
          show (0 : OrbitPairFull.Vquot m) = Submodule.Quotient.mk 0
          exact rfl
        rw [h0, OrbitPairFull.phiSummand_mk]
        have hQ : OrbitPairFull.Qnum m 0 = 0 := by
          show OrbitPairFull.pairNum m 0 0 = 0
          show (Defs.Xmat m *ᵥ 0) ⬝ᵥ 0 = 0
          rw [Matrix.mulVec_zero]
          exact zero_dotProduct _
        have hP : OrbitPairFull.pairNum m 0 w = 0 := by
          show (Defs.Xmat m *ᵥ 0) ⬝ᵥ w = 0
          rw [Matrix.mulVec_zero]
          exact zero_dotProduct _
        rw [hQ, hP]
        simp [OrbitPairFull.eChar]
    rw [Finset.sum_congr rfl (fun q _ => h1 q)]
    rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
    have hcard : Fintype.card (OrbitPairFull.Vquot m) = (Defs.Dm m).toNat := by
      rw [← OrbitPairFull.card_Fix m]
      exact (Fintype.card_congr (OrbitPairFull.fixEquivQuot m)).symm
    rw [hcard]
  · rw [if_neg hγ]
    have h10 : γ.1 ≠ 0 := fun h => hγ (Subtype.ext h)
    obtain ⟨y, hy⟩ := Quotient.exists_rep γ.1
    have hpt : ∀ q, phiSummandQ m s q γ
        = OrbitPairFull.eChar (((2 * s * OrbitPairFull.Qnum m y : ℤ) : ℚ)
            / Defs.Dm m)
          * vquotChar m y q := by
      intro q
      induction q using Quotient.inductionOn with
      | _ w =>
        show phiSummandQ m s (Submodule.Quotient.mk w) γ
          = OrbitPairFull.eChar (((2 * s * OrbitPairFull.Qnum m y : ℤ) : ℚ)
              / Defs.Dm m)
            * vquotChar m y (Submodule.Quotient.mk w)
        show OrbitPairFull.phiSummand m s w γ.1
          = OrbitPairFull.eChar (((2 * s * OrbitPairFull.Qnum m y : ℤ) : ℚ)
              / Defs.Dm m)
            * vquotChar m y (Submodule.Quotient.mk w)
        rw [← hy]
        show OrbitPairFull.phiSummand m s w (Submodule.Quotient.mk y)
          = OrbitPairFull.eChar (((2 * s * OrbitPairFull.Qnum m y : ℤ) : ℚ)
              / Defs.Dm m)
            * vquotChar m y (Submodule.Quotient.mk w)
        rw [OrbitPairFull.phiSummand_mk, vquotChar_mk, ← OrbitPairFull.eChar_add]
        congr 1
        push_cast
        ring
    rw [Finset.sum_congr rfl (fun q _ => hpt q), ← Finset.mul_sum]
    have hne : ∃ q₀, vquotChar m y q₀ ≠ 1 := by
      by_contra hcon
      push Not at hcon
      have hmk := vquotChar_triv m y hcon
      apply h10
      rw [← hy]
      show (Submodule.Quotient.mk y : OrbitPairFull.Vquot m) = 0
      exact hmk
    rw [vquotChar_sum_eq_zero m y hne, mul_zero]

/-- Item 5: the normalization `∑ ξ, φ ξ * star (φ ξ) = 1`
    (transfer to `Vquot`, modulus identity, swap the sums, and only
    `γ = 0` survives). -/
theorem phihatFix_norm (m : ℕ) [NeZero m] (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m)) :
    (∑ ξ : OrbitPair.Fix m, OrbitPairFull.phihatFix m s ξ
        * star (OrbitPairFull.phihatFix m s ξ)) = 1 := by
  have step1 : (∑ ξ : OrbitPair.Fix m, OrbitPairFull.phihatFix m s ξ
        * star (OrbitPairFull.phihatFix m s ξ))
      = ∑ q : OrbitPairFull.Vquot m, OrbitPairFull.phihat m s q
        * star (OrbitPairFull.phihat m s q) :=
    Equiv.sum_comp (OrbitPairFull.fixEquivQuot m)
      (fun q => OrbitPairFull.phihat m s q * star (OrbitPairFull.phihat m s q))
  rw [step1]
  have step2 : (∑ q : OrbitPairFull.Vquot m, OrbitPairFull.phihat m s q
        * star (OrbitPairFull.phihat m s q))
      = (Defs.Dm m : ℂ)⁻¹ * ∑ γ : ↥(OrbitPairFull.torsionSubgroup m),
          ∑ q : OrbitPairFull.Vquot m, phiSummandQ m s q γ := by
    rw [Finset.sum_congr rfl (fun q _ => phihat_modulus_Q m s hs q)]
    have hcomm : (∑ q : OrbitPairFull.Vquot m,
          ∑ γ : ↥(OrbitPairFull.torsionSubgroup m), phiSummandQ m s q γ)
        = ∑ γ : ↥(OrbitPairFull.torsionSubgroup m),
          ∑ q : OrbitPairFull.Vquot m, phiSummandQ m s q γ :=
      Finset.sum_comm
    rw [← Finset.mul_sum, hcomm]
  rw [step2]
  have hsum : (∑ γ : ↥(OrbitPairFull.torsionSubgroup m),
        ∑ q : OrbitPairFull.Vquot m, phiSummandQ m s q γ)
      = ((Defs.Dm m).toNat : ℂ) := by
    rw [Finset.sum_eq_single (0 : ↥(OrbitPairFull.torsionSubgroup m))]
    · rw [phiSummandQ_inner m s 0, if_pos rfl]
    · intro γ _ hγ
      rw [phiSummandQ_inner m s γ, if_neg hγ]
    · intro h
      exact absurd (Finset.mem_univ _) h
  rw [hsum]
  have hDm0 : (Defs.Dm m : ℂ) ≠ 0 := by exact_mod_cast ne_of_gt (Defs.Dm_pos m)
  have hcast : (((Defs.Dm m).toNat : ℂ)) = (Defs.Dm m : ℂ) := by
    exact_mod_cast OrbitPairFull.Dm_toNat_cast m
  rw [hcast, inv_mul_cancel₀ hDm0]

/-! ### §6. From the normalization: `hcardPos` and `hNorm` -/

/-- Item 6a: the support is nonempty (otherwise the norm sum would
    be `0`, not `1`). -/
theorem phihatFix_cardPos (m : ℕ) [NeZero m] (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m)) :
    0 < (OrbitPair.support m (OrbitPairFull.phihatFix m s)).card := by
  by_contra hcon
  push Not at hcon
  have hcard0 : (OrbitPair.support m (OrbitPairFull.phihatFix m s)).card = 0 :=
    Nat.le_zero.mp hcon
  have hempty : OrbitPair.support m (OrbitPairFull.phihatFix m s) = ∅ :=
    Finset.card_eq_zero.mp hcard0
  have hall : ∀ ξ, OrbitPairFull.phihatFix m s ξ = 0 := by
    intro ξ
    by_contra hne
    have hmem : ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s) := by
      simp only [OrbitPair.support, Finset.mem_filter, Finset.mem_univ,
        true_and]
      exact hne
    rw [hempty] at hmem
    exact Finset.notMem_empty ξ hmem
  have hnorm := phihatFix_norm m s hs
  have hzero : (∑ ξ : OrbitPair.Fix m, OrbitPairFull.phihatFix m s ξ
        * star (OrbitPairFull.phihatFix m s ξ))
      = ∑ _ξ : OrbitPair.Fix m, (0 : ℂ) := by
    apply Finset.sum_congr rfl
    intro ξ _
    simp [hall ξ]
  rw [hzero] at hnorm
  simp at hnorm

/-- Item 6b: `c * D = 1` (the norm sum is `card • c`). -/
theorem phihatFix_hNorm (m : ℕ) [NeZero m] (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m)) :
    ((Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ))
      * ((OrbitPair.support m (OrbitPairFull.phihatFix m s)).card : ℂ) = 1 := by
  have hnorm := phihatFix_norm m s hs
  have hsplit : (∑ ξ : OrbitPair.Fix m, OrbitPairFull.phihatFix m s ξ
        * star (OrbitPairFull.phihatFix m s ξ))
      = ∑ ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s),
          OrbitPairFull.phihatFix m s ξ
            * star (OrbitPairFull.phihatFix m s ξ) := by
    symm
    apply Finset.sum_subset
    · exact Finset.subset_univ _
    · intro ξ _ hξ
      have h0 : OrbitPairFull.phihatFix m s ξ = 0 := by
        by_contra hne
        exact hξ (by
          simp only [OrbitPair.support, Finset.mem_filter, Finset.mem_univ,
            true_and]
          exact hne)
      rw [h0, star_zero, mul_zero]
  have hsup : (∑ ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s),
        OrbitPairFull.phihatFix m s ξ
          * star (OrbitPairFull.phihatFix m s ξ)) = 1 := by
    rw [← hsplit]
    exact hnorm
  have hconst : (∑ ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s),
        OrbitPairFull.phihatFix m s ξ
          * star (OrbitPairFull.phihatFix m s ξ))
      = (OrbitPair.support m (OrbitPairFull.phihatFix m s)).card
        • ((Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ)) := by
    rw [Finset.sum_congr rfl (fun ξ hξ => phihatFix_sq m s hs ξ hξ)]
    exact Finset.sum_const _
  rw [hsup, nsmul_eq_mul] at hconst
  exact (mul_comm _ _).trans hconst.symm

/-! ### §7. Assembly: the strong-kick limit with `phihatFix` weights -/

/-- Item 7: the strong-kick limit with the concrete weights
    `phihatFix`, obtained by instantiating
    `StrongKick.strong_kick_limit` with `G := DihedralGroup m`
    (action `gammaMulAction`), `φ := phihatFix m`,
    `c := |V4| / D`, `D := card (support)`. The `ω`- and
    `S`-hypotheses remain explicit hypotheses: they are outside the
    151 content. `Odd s` is kept as stated in the task, although the
    proof only uses `IsCoprime` (the modulus and norm identities
    need no parity). The subtype action is introduced with `letI`
    (needed for instance synthesis in the `exact` step; the linter
    suggestion to use plain `let` does not apply here). -/
theorem strong_kick_limit_phihatFix (m : ℕ) [NeZero m] {K : Type*}
    [Fintype K] (S : OrbitPair.Fix m → K → ℝ) (ω : K → ℝ → ℂ) (s : ℤ)
    (_hodd : Odd s) (hs : IsCoprime s (Defs.Dm m))
    (hω0 : ∀ k, ω k 0 = 1)
    (hωbound : ∀ k (z : ℝ), ‖ω k z‖ ≤ 1)
    (hωlim : ∀ (k : K) (Δ : ℝ), Δ ≠ 0 →
      Tendsto (fun η : ℝ => ω k (η * Δ)) atTop (𝓝 0))
    (hSInv : ∀ (g : DihedralGroup m) (ξ : OrbitPair.Fix m) (k : K),
      S (g • ξ) k = S ξ k)
    (hSep : ∀ (ξ ξ' : OrbitPair.Fix m),
      (∀ k, S ξ k = S ξ' k) → ξ' ∈ Parity.orbitFinset (DihedralGroup m) ξ) :
    Tendsto (fun η : ℝ => OrbitPair.PsiPair m (OrbitPairFull.phihatFix m) S ω η s)
      atTop
      (𝓝 (((@Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
        inferInstance
        (OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s)
          (fun g ξ hξ => phihatFix_support_inv m s g ξ hξ))
        inferInstance : ℚ)) : ℂ)) := by
  have hInv : ∀ (g : DihedralGroup m) (ξ : OrbitPair.Fix m),
      ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s) →
        g • ξ ∈ OrbitPair.support m (OrbitPairFull.phihatFix m s) :=
    fun g ξ hξ => phihatFix_support_inv m s g ξ hξ
  letI : MulAction (DihedralGroup m)
      ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s)) :=
    OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s)
      (fun g ξ hξ => phihatFix_support_inv m s g ξ hξ)
  exact StrongKick.strong_kick_limit m (DihedralGroup m)
    (OrbitPairFull.phihatFix m) S ω s
    ((Fintype.card (OrbitPair.V4 m) : ℂ) / (Defs.Dm m : ℂ))
    (OrbitPair.support m (OrbitPairFull.phihatFix m s)).card
    hω0 hωbound hωlim hSInv hSep
    (fun g ξ _ => phihatFix_smul m s g ξ)
    (fun ξ hξ => phihatFix_sq m s hs ξ hξ)
    hInv
    (fun _ _ => rfl)
    (phihatFix_cardPos m s hs)
    rfl
    (phihatFix_hNorm m s hs)

#print axioms phihatFix_sq
#print axioms phihatFix_support_inv
#print axioms eChar_eq_one_iff_dvd
#print axioms vquotChar_mk
#print axioms vquotChar_add
#print axioms vquotChar_sum_eq_zero
#print axioms vquotChar_triv
#print axioms phiSummandQ_mk
#print axioms phihat_modulus_Q
#print axioms phiSummandQ_inner
#print axioms phihatFix_norm
#print axioms phihatFix_cardPos
#print axioms phihatFix_hNorm
#print axioms strong_kick_limit_phihatFix

end StrongKickBridge
end LineD
end Bgs
