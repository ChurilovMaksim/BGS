/-
  Bgs/LineDOrbitPairFull.lean — 151-full: closing the gaps of the 151+149 block.

  What this module is
  -------------------
  The block (LineDDefs / LineDOrbitPair / LineDBridge / LineDParity) left
  151 not full for five reasons: (a) phihat values and s-independence of
  the support (Prop R); (b) the Γ-action on Fix_m with generators;
  (c) card (Fix m) = D_m (Smith); (d) the D_eff table at m = 7;
  (e) assembly of PsiPair with the boundary weights. This module closes
  all five: (b) and (c) completely; (a) as theorems from the concrete
  phihat definition, for odd s coprime to D (the source's hypotheses
  for Prop R — see the report for the scope note); (d) structurally,
  with no kernel decide (det H_m = Tr S^m - 2 plus the trace formula,
  and |V4 7| = 4 by the constancy of the mod-4 kernel); (e) by
  exhibiting the pair sum with the concrete weights `phihatFix` on
  `Fix m` and its complex-S variant `PsiPairC`, connected back to the
  block's `PsiPair`. The multiset ⇒ Gamma-class bridge (pending-153)
  is explicitly NOT part of this module. Whatever does not close stays
  an explicit hypothesis, never a postulate.

  No sorry / axiom / native_decide anywhere in this file.
-/

import Bgs.LineDOrbitPair
import Bgs.LineDParity
import Mathlib.GroupTheory.SpecificGroups.Dihedral
import Mathlib.LinearAlgebra.FreeModule.Finite.CardQuotient
import Mathlib.LinearAlgebra.Vandermonde
import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.Algebra.Polynomial.Roots

namespace Bgs
namespace LineD
namespace OrbitPairFull

open Matrix Finset
open Bgs.LineD.Defs
open Bgs.LineD.OrbitPair

/-! ### Pointwise form of H_m and its cast to ZMod D -/

/-- Pointwise form of the H_m action: (H_m x)_i = 6 x_i - x_{i+1} - x_{i-1}. -/
theorem Hmat_mulVec_apply (m : ℕ) [NeZero m] (α : Type*) [Ring α]
    (x : ZMod m → α) (i : ZMod m) :
    (Hmat m α *ᵥ x) i = 6 * x i - x (i + 1) - x (i - 1) := by
  have h1 : Hmat m α *ᵥ x
      = (6 : α) • x - shiftMat m α *ᵥ x - (shiftMat m α)ᵀ *ᵥ x := by
    rw [Hmat, Matrix.sub_mulVec, Matrix.sub_mulVec, Matrix.smul_mulVec,
      Matrix.one_mulVec]
  rw [h1]
  simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul, shift_mulVec,
    shift_transpose_mulVec]

/-- `H_m` maps to `H_m` over any commutative ring under the integer cast. -/
theorem Hmat_map_ringHom (m : ℕ) {β : Type*} [CommRing β] (f : ℤ →+* β) :
    (Hmat m ℤ).map f = Hmat m β := by
  ext i j
  simp only [Hmat, Matrix.map_apply, Matrix.sub_apply, Matrix.smul_apply,
    Matrix.one_apply, Matrix.transpose_apply, shiftMat, Matrix.of_apply]
  split_ifs <;> simp <;> ring

/-- The integer H_m maps to H_m over ZMod D under the cast. -/
theorem Hmat_map_zmod (m : ℕ) (D : ℕ) :
    (Hmat m ℤ).map (Int.castRingHom (ZMod D)) = Hmat m (ZMod D) :=
  Hmat_map_ringHom m (Int.castRingHom (ZMod D))

/-- Pointwise form of casting a matrix-vector product: the cast of
    `(H_m v)_i` is the cast-matrix product of the cast vector. This is the
    usable form of `RingHom.map_mulVec` (which is stated pointwise). -/
theorem map_cast_mulVec_apply (m : ℕ) [NeZero m] (D : ℕ) (v : ZMod m → ℤ) (i : ZMod m) :
    ((Hmat m ℤ *ᵥ v) i : ZMod D)
      = ((Hmat m ℤ).map (Int.castRingHom (ZMod D)) *ᵥ
        (Int.castRingHom (ZMod D) ∘ v)) i := by
  show (Int.castRingHom (ZMod D)) ((Hmat m ℤ *ᵥ v) i) = _
  rw [RingHom.map_mulVec]

/-! ### The dihedral Γ-action on Fix_m (gap (b)) -/

/-- The index map of a dihedral element: rotation by `i`, resp. the
    reflection `j ↦ i - j`. These are chosen so that precomposition is a
    left action against the `DihedralGroup` multiplication table
    (`r i * r j = r (i+j)`, `r i * sr j = sr (j-i)`,
    `sr i * r j = sr (i+j)`, `sr i * sr j = r (j-i)`):
    `σ_{gh} = σ_h ∘ σ_g` in each of the four cases. -/
def gammaPerm (m : ℕ) : DihedralGroup m → (ZMod m → ZMod m)
  | DihedralGroup.r i => fun j => j + i
  | DihedralGroup.sr i => fun j => i - j

/-- H_m commutes with coordinate permutations coming from Γ: the permuted
    vector is again in the kernel. The point is that H is symmetric in the
    two neighbours: for a shift, `σ(i±1) = σi ± 1`; for a reflection,
    `σ(i±1) = σi ∓ 1`, and both give `(H ξ)_{σi}`. -/
theorem Hmat_mulVec_comp_gammaPerm (m : ℕ) [NeZero m] (α : Type*) [Ring α]
    (x : ZMod m → α) (g : DihedralGroup m) :
    Hmat m α *ᵥ (x ∘ gammaPerm m g) = (Hmat m α *ᵥ x) ∘ gammaPerm m g := by
  funext i
  cases g with
  | r k =>
    simp only [Function.comp_apply, gammaPerm, Hmat_mulVec_apply]
    rw [show i + k + 1 = (i + 1) + k by ring, show i + k - 1 = (i - 1) + k by ring]
  | sr k =>
    simp only [Function.comp_apply, gammaPerm, Hmat_mulVec_apply]
    rw [show k - (i + 1) = (k - i) - 1 by ring, show k - (i - 1) = (k - i) + 1 by ring]
    abel

/-- Kernel preservation under Γ, stated for an arbitrary vector with a
    kernel hypothesis. The generalisation is essential: rewriting the
    matrix inside a goal mentioning `ξ.1` fails, because `Fix m` is
    defined via that matrix (dependent-rewrite motive error); for a plain
    variable `y` the same rewrite is harmless. -/
theorem kernel_comp_gammaPerm (m : ℕ) [NeZero m]
    (y : ZMod m → ZMod (Dm m).toNat)
    (hy : (Hmat m ℤ).map (Int.castRingHom (ZMod (Dm m).toNat)) *ᵥ y = 0)
    (g : DihedralGroup m) :
    (Hmat m ℤ).map (Int.castRingHom (ZMod (Dm m).toNat)) *ᵥ (y ∘ gammaPerm m g) = 0 := by
  have h2 : Hmat m (ZMod (Dm m).toNat) *ᵥ y = 0 := by
    rw [← Hmat_map_zmod m (Dm m).toNat]
    exact hy
  rw [Hmat_map_zmod m (Dm m).toNat,
    Hmat_mulVec_comp_gammaPerm m (ZMod (Dm m).toNat) y g, h2]
  funext i
  rfl

/-- The Γ-action on Fix_m: precomposition of coordinates. -/
instance gammaMulAction (m : ℕ) [NeZero m] : MulAction (DihedralGroup m) (Fix m) where
  smul g ξ :=
    ⟨ξ.1 ∘ gammaPerm m g, kernel_comp_gammaPerm m ξ.1 ξ.2 g⟩
  one_smul ξ := by
    apply Subtype.ext
    funext j
    show ξ.1 (gammaPerm m 1 j) = ξ.1 j
    rw [DihedralGroup.one_def]
    simp only [gammaPerm, add_zero]
  mul_smul g h ξ := by
    apply Subtype.ext
    funext j
    show ξ.1 (gammaPerm m (g * h) j)
      = ξ.1 (gammaPerm m h (gammaPerm m g j))
    cases g <;> cases h <;>
      simp only [gammaPerm, DihedralGroup.r_mul_r, DihedralGroup.r_mul_sr,
        DihedralGroup.sr_mul_r, DihedralGroup.sr_mul_sr] <;>
      congr 1 <;> ring

/-- Pointwise form of the Γ-action (definitional). -/
theorem gamma_smul_apply (m : ℕ) [NeZero m] (g : DihedralGroup m) (ξ : Fix m)
    (j : ZMod m) : (g • ξ).1 j = ξ.1 (gammaPerm m g j) := rfl

#print axioms gammaMulAction

/-! ### Cardinality of Fix_m (gap (c)) -/

/-- `NeZero` for the modulus `D_m` as a natural number. -/
instance neZeroDmToNat (m : ℕ) [NeZero m] : NeZero (Dm m).toNat :=
  ⟨fun hc => by
    rw [Int.toNat_eq_zero] at hc
    have h := Dm_pos m
    omega⟩

/-- `(D_m : ℤ)` cast back from its natural-number form. -/
theorem Dm_toNat_cast (m : ℕ) [NeZero m] : ((Dm m).toNat : ℤ) = Dm m :=
  Int.toNat_of_nonneg (le_of_lt (Dm_pos m))

/-- The kernel of `H_m` over `ℤ` is trivial (determinant nonzero). -/
theorem Hmat_mulVec_eq_zero (m : ℕ) [NeZero m] (v : ZMod m → ℤ)
    (h : Hmat m ℤ *ᵥ v = 0) : v = 0 := by
  have hQ : (Hmat m ℚ) *ᵥ (fun i => (v i : ℚ)) = 0 := by
    have h1 : (Hmat m ℤ).map (Int.castRingHom ℚ) *ᵥ
        (Int.castRingHom ℚ ∘ v) = 0 := by
      funext i
      rw [← RingHom.map_mulVec, h]
      simp
    rwa [Hmat_map_ringHom m (Int.castRingHom ℚ)] at h1
  have hdet : (Hmat m ℚ).det ≠ 0 := by
    rw [← Hmat_map_ringHom m (Int.castRingHom ℚ)]
    show ((Int.castRingHom ℚ).mapMatrix (Hmat m ℤ)).det ≠ 0
    rw [← RingHom.map_det]
    show ((Hmat m ℤ).det : ℚ) ≠ 0
    simp only [ne_eq, Int.cast_eq_zero]
    exact ne_of_gt (Dm_pos m)
  have hv : (fun i => (v i : ℚ)) = 0 :=
    Matrix.eq_zero_of_mulVec_eq_zero hdet hQ
  funext i
  have hi := congrFun hv i
  simp only [Pi.zero_apply] at hi
  exact_mod_cast hi

/- NOTE (deferred to the Prop R phase): `Fix m` and `V4 m` carry an
   `AddCommGroup` structure as kernels of linear maps, but building it by
   hand needs the `nsmul`/`zsmul`/`neg_add_cancel` fields, which the
   `where` syntax does not default here. The clean construction is
   transport from `↥(LinearMap.ker (Matrix.mulVecLin _))` via
   `inferInstanceAs`; it is not needed for the cardinality argument
   below, so it is deferred rather than faked. -/

/-- Canonical lift of a `Fix` point to `ℤ^m`: `ZMod.val` representatives. -/
noncomputable def fixLift (m : ℕ) [NeZero m] (ξ : Fix m) : ZMod m → ℤ :=
  fun i => ((ξ.1 i).val : ℤ)

/-- The canonical lift reduces back to `ξ` modulo `D_m`. -/
theorem fixLift_cast (m : ℕ) [NeZero m] (ξ : Fix m) :
    (fun i => ((fixLift m ξ i : ℤ) : ZMod (Dm m).toNat)) = ξ.1 := by
  funext i
  simp only [fixLift, Int.cast_natCast]
  rw [ZMod.natCast_val, ZMod.cast_id]

/-- The lift satisfies `D_m ∣ (H_m y)_i` for every `i`. -/
theorem fixLift_dvd (m : ℕ) [NeZero m] (ξ : Fix m) (i : ZMod m) :
    Dm m ∣ (Hmat m ℤ *ᵥ fixLift m ξ) i := by
  have hcast : ((Hmat m ℤ *ᵥ fixLift m ξ) i : ZMod (Dm m).toNat) = 0 := by
    have hcomp : (Int.castRingHom (ZMod (Dm m).toNat)) ∘ fixLift m ξ = ξ.1 := by
      funext j
      exact congrFun (fixLift_cast m ξ) j
    rw [map_cast_mulVec_apply, hcomp]
    exact congrFun ξ.2 i
  rw [ZMod.intCast_zmod_eq_zero_iff_dvd] at hcast
  rwa [Dm_toNat_cast m] at hcast

/-- The forward map `Fix m → ℤ^m ⧸ H_m ℤ^m`: `ξ ↦ [z]` with `H_m y = D_m z`. -/
noncomputable def fixToQuot (m : ℕ) [NeZero m] (ξ : Fix m) :
    (ZMod m → ℤ) ⧸ LinearMap.range (Matrix.mulVecLin (Hmat m ℤ)) :=
  Submodule.Quotient.mk
    (fun i => (Hmat m ℤ *ᵥ fixLift m ξ) i / Dm m)

/-- The defining equation of the forward map. -/
theorem fixToQuot_spec (m : ℕ) [NeZero m] (ξ : Fix m) :
    Hmat m ℤ *ᵥ fixLift m ξ
      = Dm m • (fun i => (Hmat m ℤ *ᵥ fixLift m ξ) i / Dm m) := by
  funext i
  simp only [Pi.smul_apply, smul_eq_mul, mul_comm (Dm m) _,
    Int.ediv_mul_cancel (fixLift_dvd m ξ i)]

/-- The backward map on representatives: `w ↦ X_m w (mod D_m)`. -/
noncomputable def quotToFixRep (m : ℕ) [NeZero m] (w : ZMod m → ℤ) : Fix m :=
  ⟨(fun i => ((Xmat m *ᵥ w) i : ZMod (Dm m).toNat)), by
    have h1 : (Hmat m ℤ).map (Int.castRingHom (ZMod (Dm m).toNat)) *ᵥ
        (Int.castRingHom (ZMod (Dm m).toNat) ∘ (Xmat m *ᵥ w)) = 0 := by
      funext i
      rw [← RingHom.map_mulVec]
      have h2 : Hmat m ℤ *ᵥ (Xmat m *ᵥ w) = Dm m • w := by
        rw [Matrix.mulVec_mulVec, Hmat_mul_Xmat, Matrix.smul_mulVec,
          Matrix.one_mulVec]
      have h3 := congrFun h2 i
      simp only [Pi.smul_apply, smul_eq_mul] at h3
      rw [h3]
      show ((Dm m * w i : ℤ) : ZMod (Dm m).toNat) = 0
      have hD0 : ((Dm m : ℤ) : ZMod (Dm m).toNat) = 0 := by
        rw [← Dm_toNat_cast m, Int.cast_natCast]
        exact ZMod.natCast_self _
      simp only [Int.cast_mul, hD0, zero_mul]
    exact h1⟩

/-- The backward map descends to the quotient: `w` and `w + H_m t` give the
    same point, since `X_m (H_m t) = D_m t ≡ 0 (mod D_m)`. -/
noncomputable def quotToFix (m : ℕ) [NeZero m] :
    (ZMod m → ℤ) ⧸ LinearMap.range (Matrix.mulVecLin (Hmat m ℤ)) → Fix m :=
  Quotient.lift (quotToFixRep m) (by
    intro w w' h
    have h2 : (LinearMap.range (Matrix.mulVecLin (Hmat m ℤ))).quotientRel w w' := h
    rw [Submodule.quotientRel_def] at h2
    obtain ⟨t, ht⟩ := h2
    have ht' : Hmat m ℤ *ᵥ t = w - w' := ht
    have hw' : w' = w - Hmat m ℤ *ᵥ t := by
      rw [ht']
      exact (sub_sub_self w w').symm
    apply Subtype.ext
    funext i
    have hX : Xmat m *ᵥ w' = Xmat m *ᵥ w - Dm m • t := by
      rw [hw', Matrix.mulVec_sub, Matrix.mulVec_mulVec, Xmat_mul_Hmat,
        Matrix.smul_mulVec, Matrix.one_mulVec]
    have hcast : ((Xmat m *ᵥ w' : ZMod m → ℤ) i : ZMod (Dm m).toNat)
        = ((Xmat m *ᵥ w : ZMod m → ℤ) i : ZMod (Dm m).toNat) := by
      rw [hX]
      simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul, Int.cast_sub,
        Int.cast_mul]
      have hD0 : ((Dm m : ℤ) : ZMod (Dm m).toNat) = 0 := by
        rw [← Dm_toNat_cast m, Int.cast_natCast]
        exact ZMod.natCast_self _
      rw [hD0, zero_mul, sub_zero]
    exact hcast.symm)

/-- The equivalence `Fix m ≃ ℤ^m ⧸ H_m ℤ^m` (proof: adjugate inversion). -/
noncomputable def fixEquivQuot (m : ℕ) [NeZero m] :
    Fix m ≃ (ZMod m → ℤ) ⧸ LinearMap.range (Matrix.mulVecLin (Hmat m ℤ)) where
  toFun := fixToQuot m
  invFun := quotToFix m
  left_inv ξ := by
    show quotToFixRep (m := m)
      (fun i => (Hmat m ℤ *ᵥ fixLift m ξ) i / Dm m) = ξ
    have hHz : Hmat m ℤ *ᵥ (Xmat m *ᵥ
        (fun i => (Hmat m ℤ *ᵥ fixLift m ξ) i / Dm m))
        = Hmat m ℤ *ᵥ fixLift m ξ := by
      rw [Matrix.mulVec_mulVec, Hmat_mul_Xmat, Matrix.smul_mulVec,
        Matrix.one_mulVec]
      exact (fixToQuot_spec m ξ).symm
    have hEq : Xmat m *ᵥ (fun i => (Hmat m ℤ *ᵥ fixLift m ξ) i / Dm m)
        = fixLift m ξ := by
      have h0 : Hmat m ℤ *ᵥ (Xmat m *ᵥ
          (fun i => (Hmat m ℤ *ᵥ fixLift m ξ) i / Dm m) - fixLift m ξ) = 0 := by
        rw [Matrix.mulVec_sub, hHz, sub_self]
      have := Hmat_mulVec_eq_zero m _ h0
      exact sub_eq_zero.mp this
    apply Subtype.ext
    funext i
    show ((Xmat m *ᵥ (fun j => (Hmat m ℤ *ᵥ fixLift m ξ) j / Dm m)) i :
      ZMod (Dm m).toNat) = ξ.1 i
    rw [hEq]
    exact congrFun (fixLift_cast m ξ) i
  right_inv q := by
    induction q using Quotient.inductionOn with
    | h w =>
      show fixToQuot m (quotToFixRep (m := m) w)
        = Submodule.Quotient.mk w
      -- The lift of `quotToFixRep w` differs from `X_m w` by a multiple of `D_m`.
      set v := Xmat m *ᵥ w with hv
      set y := fixLift m (quotToFixRep (m := m) w) with hy
      have hmod : ∀ i, Dm m ∣ (y i - v i) := by
        intro i
        have hcast : ((y i : ℤ) : ZMod (Dm m).toNat) = ((v i : ℤ) : ZMod (Dm m).toNat) := by
          simp only [hy, fixLift, Int.cast_natCast]
          have h1 : (quotToFixRep (m := m) w).1 i
              = ((v i : ℤ) : ZMod (Dm m).toNat) := rfl
          rw [h1]
          simp only [ZMod.natCast_val, ZMod.cast_id]
        rw [ZMod.intCast_eq_intCast_iff_dvd_sub, Dm_toNat_cast m] at hcast
        rwa [← neg_sub, dvd_neg] at hcast
      -- Hence `H_m y = H_m v + D_m • (H_m (d/D))` with `d = y - v`.
      have hH : Hmat m ℤ *ᵥ y = Dm m • w + Dm m • (Hmat m ℤ *ᵥ (fun i => (y i - v i) / Dm m)) := by
        have h1 : Hmat m ℤ *ᵥ y = Hmat m ℤ *ᵥ v + Hmat m ℤ *ᵥ (y - v) := by
          rw [← Matrix.mulVec_add]
          congr 1
          funext i
          exact (add_sub_cancel (v i) (y i)).symm
        have h2 : Hmat m ℤ *ᵥ v = Dm m • w := by
          rw [hv, Matrix.mulVec_mulVec, Hmat_mul_Xmat, Matrix.smul_mulVec,
            Matrix.one_mulVec]
        have h3 : Hmat m ℤ *ᵥ (y - v) = Dm m • (Hmat m ℤ *ᵥ (fun i => (y i - v i) / Dm m)) := by
          funext i
          simp only [Pi.smul_apply, smul_eq_mul, Matrix.mulVec_apply_eq_sum]
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro j _
          simp only [Pi.sub_apply]
          rw [mul_comm (Dm m) _, mul_assoc, Int.ediv_mul_cancel (hmod j)]
        rw [h1, h2, h3, ← smul_add]
      -- So the forward class is `[w + H_m (d/D)] = [w]`.
      have hEq : (fun i => (Hmat m ℤ *ᵥ y) i / Dm m)
          = w + Hmat m ℤ *ᵥ (fun i => (y i - v i) / Dm m) := by
        funext i
        have hi := congrFun hH i
        simp only [Pi.smul_apply, smul_eq_mul, Pi.add_apply] at hi
        rw [hi, Int.add_ediv_of_dvd_left (by exact Dvd.intro _ rfl : Dm m ∣ Dm m * w i)]
        rw [Int.mul_ediv_cancel_left _ (ne_of_gt (Dm_pos m)),
          Int.mul_ediv_cancel_left _ (ne_of_gt (Dm_pos m)), Pi.add_apply]
      show Submodule.Quotient.mk (fun i => (Hmat m ℤ *ᵥ y) i / Dm m)
        = Submodule.Quotient.mk w
      rw [hEq, Submodule.Quotient.eq]
      refine ⟨(fun i => (y i - v i) / Dm m), ?_⟩
      show Hmat m ℤ *ᵥ (fun i => (y i - v i) / Dm m)
        = w + Hmat m ℤ *ᵥ (fun i => (y i - v i) / Dm m) - w
      rw [add_sub_cancel_left]

/-- Cardinality of `Fix m`: the quotient `ℤ^m ⧸ H_m ℤ^m` has `|det H_m| = D_m`
    elements, by the Smith-normal-form index theorem of Mathlib. -/
theorem card_Fix (m : ℕ) [NeZero m] : Fintype.card (Fix m) = (Dm m).toNat := by
  have hcard : Nat.card (Fix m)
      = Nat.card ((ZMod m → ℤ) ⧸ LinearMap.range (Matrix.mulVecLin (Hmat m ℤ))) :=
    Nat.card_congr (fixEquivQuot m)
  rw [Nat.card_eq_fintype_card] at hcard
  rw [hcard]
  have hinj : Function.Injective (Matrix.mulVecLin (Hmat m ℤ)) := by
    intro a b hab
    have hab' : Hmat m ℤ *ᵥ a = Hmat m ℤ *ᵥ b := by
      simpa [Matrix.mulVecLin_apply] using hab
    have h0 : Hmat m ℤ *ᵥ (a - b) = 0 := by
      rw [Matrix.mulVec_sub, hab', sub_self]
    have h := Hmat_mulVec_eq_zero m _ h0
    exact sub_eq_zero.mp h
  have hdet := Submodule.natAbs_det_equiv
    (LinearMap.range (Matrix.mulVecLin (Hmat m ℤ)))
    (LinearEquiv.ofInjective (Matrix.mulVecLin (Hmat m ℤ)) hinj)
  have hsub : (LinearMap.range (Matrix.mulVecLin (Hmat m ℤ))).subtype ∘ₗ
        AddMonoidHom.toIntLinearMap
          ((LinearEquiv.ofInjective (Matrix.mulVecLin (Hmat m ℤ)) hinj) :
            (ZMod m → ℤ) →+ LinearMap.range (Matrix.mulVecLin (Hmat m ℤ)))
      = Matrix.mulVecLin (Hmat m ℤ) := by
    apply LinearMap.ext
    intro x
    show ↑(LinearEquiv.ofInjective (Matrix.mulVecLin (Hmat m ℤ)) hinj x)
      = Hmat m ℤ *ᵥ x
    rw [LinearEquiv.ofInjective_apply, Matrix.mulVecLin_apply]
  rw [hsub] at hdet
  have hdetM : LinearMap.det (Matrix.mulVecLin (Hmat m ℤ)) = Dm m := by
    rw [← Matrix.toLin'_apply', LinearMap.det_toLin']
    rfl
  rw [hdetM] at hdet
  rw [← hdet]
  have h1 : ((Dm m).natAbs : ℤ) = Dm m :=
    Int.natAbs_of_nonneg (le_of_lt (Dm_pos m))
  have h2 : ((Dm m).toNat : ℤ) = Dm m :=
    Int.toNat_of_nonneg (le_of_lt (Dm_pos m))
  exact Nat.cast_injective (by rw [h1, h2])

/-! ### Determinant of H_m via the Vandermonde matrix (gap (d))

Over `ℂ`, the vectors `i ↦ ω ^ (i.val * j.val)` are eigenvectors of `Hmat m ℂ`
with eigenvalue `6 - ω ^ j.val - (ω ^ j.val)⁻¹`, where `ω` is a primitive
`m`-th root of unity. Hence `det (Hmat m ℂ)` is the product of these
eigenvalues; evaluating the product (next section) gives
`det = Tr S ^ m - 2` with `S = !![6, -1; 1, 0]`, and in particular
`Dm 7 = 228484` and `Deff 7 = 57121`.
-/

/-- A primitive `m`-th root of unity over `ℂ`. -/
noncomputable def primRoot (m : ℕ) : ℂ := Complex.exp (2 * Real.pi * Complex.I / m)

theorem primRoot_isPrimitiveRoot (m : ℕ) (hm : m ≠ 0) :
    IsPrimitiveRoot (primRoot m) m :=
  Complex.isPrimitiveRoot_exp m hm

theorem primRoot_pow (m : ℕ) [NeZero m] : (primRoot m) ^ m = 1 :=
  (primRoot_isPrimitiveRoot m (NeZero.ne m)).pow_eq_one

/-- Powers of a root of unity depend only on the exponent mod `m`. -/
theorem pow_eq_of_natModEq {m : ℕ} {ω : ℂ} (hω : ω ^ m = 1) {a b : ℕ}
    (h : a ≡ b [MOD m]) : ω ^ a = ω ^ b := by
  have e1 : a = m * (a / m) + a % m := (Nat.div_add_mod a m).symm
  have e2 : b = m * (b / m) + b % m := (Nat.div_add_mod b m).symm
  rw [e1, e2, pow_add, pow_add, pow_mul, pow_mul, hω]
  simp only [one_pow, one_mul]
  rw [show a % m = b % m from h]

/-- Shifting the index `i ↦ i + 1` multiplies the Vandermonde entry by `ω ^ j.val`. -/
theorem eigen_next (m : ℕ) [NeZero m] (j i : ZMod m) :
    (primRoot m) ^ ((i + 1).val * j.val)
      = (primRoot m) ^ j.val * (primRoot m) ^ (i.val * j.val) := by
  have hmod : (i + 1).val * j.val ≡ i.val * j.val + j.val [MOD m] := by
    have h1 : (i + 1).val = (i.val + 1) % m := by
      have hv := ZMod.val_add i 1
      rw [ZMod.val_one_eq_one_mod] at hv
      rw [hv]
      calc (i.val + 1 % m) % m = (i.val % m + 1 % m) % m := by
            rw [Nat.mod_eq_of_lt (ZMod.val_lt i)]
        _ = (i.val + 1) % m := (Nat.add_mod _ _ _).symm
    rw [h1, ← show (i.val + 1) * j.val = i.val * j.val + j.val by ring]
    exact (Nat.mod_modEq _ _).mul_right _
  rw [pow_eq_of_natModEq (primRoot_pow m) hmod, pow_add]
  exact mul_comm _ _

/-- Shifting the index `i ↦ i - 1` divides the Vandermonde entry by `ω ^ j.val`. -/
theorem eigen_prev (m : ℕ) [NeZero m] (j i : ZMod m) :
    (primRoot m) ^ ((i - 1).val * j.val) * (primRoot m) ^ j.val
      = (primRoot m) ^ (i.val * j.val) := by
  have hmod : ((i - 1).val + 1) * j.val ≡ i.val * j.val [MOD m] := by
    have h1 : ((i - 1) + 1 : ZMod m) = i := sub_add_cancel i 1
    have h2 : ((i - 1).val + 1) % m = i.val := by
      have hv := ZMod.val_add (i - 1) 1
      rw [h1, ZMod.val_one_eq_one_mod] at hv
      calc ((i - 1).val + 1) % m
          = ((i - 1).val % m + 1 % m) % m := by rw [Nat.add_mod]
        _ = ((i - 1).val + 1 % m) % m := by
            rw [Nat.mod_eq_of_lt (ZMod.val_lt (i - 1))]
        _ = i.val := hv.symm
    have h3 : (i - 1).val + 1 ≡ i.val [MOD m] := by
      show ((i - 1).val + 1) % m = i.val % m
      rw [h2, Nat.mod_eq_of_lt (ZMod.val_lt i)]
    exact h3.mul_right _
  have hpow := pow_eq_of_natModEq (primRoot_pow m) hmod
  rw [show ((i - 1).val + 1) * j.val = (i - 1).val * j.val + j.val by ring,
    pow_add] at hpow
  exact hpow

/-- The Vandermonde column `j` is an eigenvector of `Hmat m ℂ`. -/
theorem eigen_vec (m : ℕ) [NeZero m] (j : ZMod m) :
    Hmat m ℂ *ᵥ (fun i => (primRoot m) ^ (i.val * j.val))
      = (6 - (primRoot m) ^ j.val - ((primRoot m) ^ j.val)⁻¹)
        • (fun i => (primRoot m) ^ (i.val * j.val)) := by
  have hω : primRoot m ≠ 0 := by
    intro h0
    have h1 := primRoot_pow (m := m)
    rw [h0, zero_pow (NeZero.ne m)] at h1
    exact zero_ne_one h1
  have hωj : (primRoot m) ^ j.val ≠ 0 := pow_ne_zero _ hω
  funext i
  rw [Hmat_mulVec_apply]
  simp only [Pi.smul_apply, smul_eq_mul]
  rw [eigen_next m j i]
  have hprev := eigen_prev m j i
  have hprev' : (primRoot m) ^ ((i - 1).val * j.val)
      = ((primRoot m) ^ j.val)⁻¹ * (primRoot m) ^ (i.val * j.val) := by
    rw [← hprev, mul_comm ((primRoot m) ^ ((i - 1).val * j.val))
      ((primRoot m) ^ j.val), inv_mul_cancel_left₀ hωj]
  rw [hprev']
  ring

/-- The Vandermonde matrix for the primitive root `ω`. -/
noncomputable def vandMat (m : ℕ) : Matrix (ZMod m) (ZMod m) ℂ :=
  Matrix.of fun i j => (primRoot m) ^ (i.val * j.val)

/-- `Hmat` times the Vandermonde matrix is the Vandermonde matrix times the
diagonal matrix of eigenvalues. -/
theorem Hmat_mul_vandMat (m : ℕ) [NeZero m] :
    Hmat m ℂ * vandMat m
      = vandMat m * Matrix.diagonal
          (fun j => 6 - (primRoot m) ^ j.val - ((primRoot m) ^ j.val)⁻¹) := by
  ext i j
  have hev := eigen_vec m j
  rw [Matrix.mul_apply, Matrix.mul_diagonal]
  have hsum : (∑ k, Hmat m ℂ i k * vandMat m k j)
      = (Hmat m ℂ *ᵥ (fun k => vandMat m k j)) i := by
    rw [Matrix.mulVec_apply_eq_sum]
  rw [hsum]
  simp only [vandMat, Matrix.of_apply]
  rw [hev]
  simp only [Pi.smul_apply, smul_eq_mul]
  exact mul_comm _ _

/-- The index equivalence `Fin m ≃ ZMod m` (values are preserved). -/
def finZModEquiv (m : ℕ) [NeZero m] : Fin m ≃ ZMod m where
  toFun k := (k.val : ZMod m)
  invFun a := ⟨a.val, ZMod.val_lt a⟩
  left_inv k := by
    rw [Fin.ext_iff]
    show ((k.val : ZMod m).val) = k.val
    rw [ZMod.val_natCast, Nat.mod_eq_of_lt k.isLt]
  right_inv a := by
    show ((a.val : ZMod m)) = a
    rw [ZMod.natCast_val, ZMod.cast_id]

/-- The Vandermonde matrix is invertible: its determinant is nonzero. -/
theorem vandMat_det_ne_zero (m : ℕ) [NeZero m] : (vandMat m).det ≠ 0 := by
  have hEq : vandMat m
      = (Matrix.vandermonde (fun k : Fin m => (primRoot m) ^ k.val)).reindex
          (finZModEquiv m) (finZModEquiv m) := by
    ext i j
    show (primRoot m) ^ (i.val * j.val)
      = ((primRoot m) ^ ((finZModEquiv m).symm i).val)
        ^ ((finZModEquiv m).symm j).val
    have hi : (finZModEquiv m).symm i = ⟨i.val, ZMod.val_lt i⟩ := rfl
    have hj : (finZModEquiv m).symm j = ⟨j.val, ZMod.val_lt j⟩ := rfl
    rw [hi, hj]
    show (primRoot m) ^ (i.val * j.val) = ((primRoot m) ^ i.val) ^ j.val
    rw [← pow_mul]
  rw [hEq, Matrix.det_reindex_self, Matrix.det_vandermonde_ne_zero_iff]
  intro a b hab
  have h := (primRoot_isPrimitiveRoot m (NeZero.ne m)).pow_inj a.isLt b.isLt hab
  exact Fin.ext h

/-- The product `∏ j, (λ - ω ^ j.val)` is `λ ^ m - 1`: the factors are
exactly the roots of `X ^ m - 1`. -/
theorem prod_sub_primRoot (m : ℕ) [NeZero m] (lam : ℂ) :
    ∏ j : ZMod m, (lam - (primRoot m) ^ j.val) = lam ^ m - 1 := by
  have hprod := Polynomial.X_pow_sub_one_eq_prod (Nat.pos_of_ne_zero (NeZero.ne m))
    (primRoot_isPrimitiveRoot m (NeZero.ne m))
  have hev := congrArg (Polynomial.eval lam) hprod
  simp only [Polynomial.eval_sub, Polynomial.eval_pow, Polynomial.eval_X,
    Polynomial.eval_one, Polynomial.eval_prod, Polynomial.eval_C] at hev
  rw [hev]
  apply Finset.prod_bij (fun j _ => (primRoot m) ^ j.val)
  · intro j _
    rw [Polynomial.mem_nthRootsFinset (Nat.pos_of_ne_zero (NeZero.ne m)) 1]
    rw [← pow_mul, mul_comm j.val m, pow_mul, primRoot_pow, one_pow]
  · intro a _ b _ hab
    have h := (primRoot_isPrimitiveRoot m (NeZero.ne m)).pow_inj (ZMod.val_lt a)
      (ZMod.val_lt b) hab
    exact ZMod.val_injective m h
  · intro ζ hζ
    rw [Polynomial.mem_nthRootsFinset (Nat.pos_of_ne_zero (NeZero.ne m)) 1] at hζ
    obtain ⟨k, _, hkeq⟩ := (primRoot_isPrimitiveRoot m (NeZero.ne m)).eq_pow_of_pow_eq_one hζ
    refine ⟨(k : ZMod m), Finset.mem_univ _, ?_⟩
    have hmod : k % m ≡ k [MOD m] := Nat.mod_modEq _ _
    have hp := pow_eq_of_natModEq (primRoot_pow m) hmod
    rw [ZMod.val_natCast, hp, hkeq]
  · intro j _
    rfl

/-- The larger root of `x ^ 2 - 6 * x + 1`: `λ = 3 + 2√2`. -/
noncomputable def lamC : ℂ := 3 + 2 * Real.sqrt 2

/-- The smaller root: `μ = 3 - 2√2 = λ⁻¹`. -/
noncomputable def muC : ℂ := 3 - 2 * Real.sqrt 2

theorem sqrt2_sq : ((Real.sqrt 2 : ℂ)) ^ 2 = 2 := by
  exact_mod_cast Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)

theorem lamC_mul_muC : lamC * muC = 1 := by
  have hs := sqrt2_sq
  calc lamC * muC = 9 - 4 * (Real.sqrt 2 : ℂ) ^ 2 := by simp only [lamC, muC]; ring
    _ = 1 := by rw [hs]; norm_num

theorem lamC_sq : lamC ^ 2 = 6 * lamC - 1 := by
  have hs := sqrt2_sq
  simp only [lamC]
  linear_combination 4 * hs

theorem muC_sq : muC ^ 2 = 6 * muC - 1 := by
  have hs := sqrt2_sq
  simp only [muC]
  linear_combination 4 * hs

theorem lamC_ne_zero : lamC ≠ 0 := by
  intro h0
  have h := lamC_mul_muC
  rw [h0, zero_mul] at h
  exact zero_ne_one h

theorem muC_eq_inv : muC = lamC⁻¹ :=
  eq_inv_of_mul_eq_one_left (by rw [mul_comm]; exact lamC_mul_muC)

/-- The eigenvalue factors through `λ`: `6 - z - z⁻¹ = λ⁻¹(λ - z)(λ - z⁻¹)`. -/
theorem factor_eig (z : ℂ) (hz : z ≠ 0) :
    6 - z - z⁻¹ = lamC⁻¹ * (lamC - z) * (lamC - z⁻¹) := by
  have hsq : lamC ^ 2 + 1 = 6 * lamC := by linear_combination lamC_sq
  have hz1 : z * z⁻¹ = 1 := mul_inv_cancel₀ hz
  calc 6 - z - z⁻¹ = lamC⁻¹ * (lamC * (6 - z - z⁻¹)) :=
        (inv_mul_cancel_left₀ lamC_ne_zero _).symm
    _ = lamC⁻¹ * ((lamC - z) * (lamC - z⁻¹)) := by
        congr 1
        linear_combination -hsq - hz1
    _ = lamC⁻¹ * (lamC - z) * (lamC - z⁻¹) := by rw [mul_assoc]

/-- The inverse power is the power at the negated index. -/
theorem inv_pow_eq_neg (m : ℕ) [NeZero m] (j : ZMod m) :
    ((primRoot m) ^ j.val)⁻¹ = (primRoot m) ^ (-j).val := by
  by_cases hj : j = 0
  · subst hj
    simp
  · rw [ZMod.neg_val, if_neg hj]
    have hpow : (primRoot m) ^ (m - j.val) * (primRoot m) ^ j.val = 1 := by
      rw [← pow_add, Nat.sub_add_cancel (le_of_lt (ZMod.val_lt j))]
      exact primRoot_pow m
    exact (eq_inv_of_mul_eq_one_left hpow).symm

/-- The determinant of `Hmat m ℂ` is the product of the eigenvalues. -/
theorem det_Hmat_eq_prod (m : ℕ) [NeZero m] :
    (Hmat m ℂ).det
      = ∏ j : ZMod m, (6 - (primRoot m) ^ j.val - ((primRoot m) ^ j.val)⁻¹) := by
  have hmul := Hmat_mul_vandMat m
  have hW := vandMat_det_ne_zero m
  have h1 : (Hmat m ℂ).det * (vandMat m).det
      = (vandMat m).det
        * ∏ j : ZMod m, (6 - (primRoot m) ^ j.val - ((primRoot m) ^ j.val)⁻¹) := by
    rw [← Matrix.det_mul, hmul, Matrix.det_mul, Matrix.det_diagonal]
  rw [mul_comm (vandMat m).det] at h1
  exact mul_right_cancel₀ hW h1

/-- The product of the eigenvalues is `λ⁻ᵐ(λᵐ - 1)²`. -/
theorem prod_eig (m : ℕ) [NeZero m] :
    (∏ j : ZMod m, (6 - (primRoot m) ^ j.val - ((primRoot m) ^ j.val)⁻¹))
      = lamC⁻¹ ^ m * (lamC ^ m - 1) ^ 2 := by
  have hfac : ∀ j : ZMod m, 6 - (primRoot m) ^ j.val - ((primRoot m) ^ j.val)⁻¹
      = lamC⁻¹ * (lamC - (primRoot m) ^ j.val)
        * (lamC - ((primRoot m) ^ j.val)⁻¹) :=
    fun j => factor_eig _ (pow_ne_zero _ (by
      intro h0
      have h1 := primRoot_pow (m := m)
      rw [h0, zero_pow (NeZero.ne m)] at h1
      exact zero_ne_one h1))
  have hneg : (∏ j : ZMod m, (lamC - ((primRoot m) ^ j.val)⁻¹))
      = ∏ j : ZMod m, (lamC - (primRoot m) ^ j.val) := by
    apply Fintype.prod_equiv (Equiv.neg (ZMod m)) _ _
    intro j
    show lamC - ((primRoot m) ^ j.val)⁻¹ = lamC - (primRoot m) ^ (-j).val
    rw [inv_pow_eq_neg m j]
  simp only [hfac]
  rw [Finset.prod_mul_distrib, Finset.prod_mul_distrib, Finset.prod_const,
    Finset.card_univ, ZMod.card, hneg, prod_sub_primRoot m lamC]
  ring

/-- The determinant formula: `(Dm m : ℂ) = λ ^ m + μ ^ m - 2`. -/
theorem det_formula (m : ℕ) [NeZero m] :
    ((Dm m : ℤ) : ℂ) = lamC ^ m + muC ^ m - 2 := by
  have hdetC : (Hmat m ℂ).det = lamC⁻¹ ^ m * (lamC ^ m - 1) ^ 2 := by
    rw [det_Hmat_eq_prod m, prod_eig m]
  have hDm : (Hmat m ℂ).det = ((Dm m : ℤ) : ℂ) := by
    rw [← Hmat_map_ringHom m (Int.castRingHom ℂ)]
    show ((Int.castRingHom ℂ).mapMatrix (Hmat m ℤ)).det = ((Dm m : ℤ) : ℂ)
    rw [← RingHom.map_det]
    rfl
  rw [← hDm, hdetC, muC_eq_inv]
  have h1 : (lamC⁻¹ : ℂ) ^ m * lamC ^ m = 1 := by
    rw [← mul_pow, inv_mul_cancel₀ lamC_ne_zero, one_pow]
  have h2 : (lamC⁻¹ : ℂ) ^ m * lamC ^ (2 * m) = lamC ^ m := by
    rw [show (2 * m) = m + m by ring, pow_add, ← mul_assoc, h1, one_mul]
  have hexp : (lamC ^ m - 1) ^ 2 = lamC ^ (2 * m) - 2 * lamC ^ m + 1 := by
    have h : (lamC ^ m - 1) ^ 2 = (lamC ^ m) ^ 2 - 2 * lamC ^ m + 1 := by ring
    rw [h, pow_two, ← pow_add, show m + m = 2 * m by ring]
  rw [hexp, mul_add, mul_sub, h2]
  have h3 : (lamC⁻¹ : ℂ) ^ m * (2 * lamC ^ m) = 2 := by
    calc (lamC⁻¹ : ℂ) ^ m * (2 * lamC ^ m)
        = 2 * ((lamC⁻¹) ^ m * lamC ^ m) := by ring
      _ = 2 := by rw [h1, mul_one]
  rw [h3]
  simp only [mul_one]
  ring

/-- The companion matrix `S = !![6, -1; 1, 0]`, whose powers have trace
`λ ^ m + μ ^ m`. -/
def Smat : Matrix (Fin 2) (Fin 2) ℂ := !![6, -1; 1, 0]

theorem Smat_sq : Smat ^ 2 = 6 • Smat - 1 := by
  rw [pow_two]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Smat, Matrix.mul_apply, Fin.sum_univ_two] <;> norm_num

/-- The integer sequence `u 0 = 2, u 1 = 6, u (n+2) = 6 * u (n+1) - u n`
(the Lucas-type sequence for `λ = 3 + 2√2`). -/
def uSeq : ℕ → ℤ
  | 0 => 2
  | 1 => 6
  | n + 2 => 6 * uSeq (n + 1) - uSeq n

theorem sum_pow_eq_u (m : ℕ) : lamC ^ m + muC ^ m = (uSeq m : ℂ) := by
  have hrec : ∀ k, lamC ^ (k + 2) + muC ^ (k + 2)
      = 6 * (lamC ^ (k + 1) + muC ^ (k + 1)) - (lamC ^ k + muC ^ k) := by
    intro k
    have e1 : lamC ^ (k + 2) = 6 * lamC ^ (k + 1) - lamC ^ k := by
      calc lamC ^ (k + 2) = lamC ^ k * lamC ^ 2 := by rw [pow_add]
        _ = lamC ^ k * (6 * lamC - 1) := by rw [lamC_sq]
        _ = 6 * lamC ^ (k + 1) - lamC ^ k := by rw [pow_succ]; ring
    have e2 : muC ^ (k + 2) = 6 * muC ^ (k + 1) - muC ^ k := by
      calc muC ^ (k + 2) = muC ^ k * muC ^ 2 := by rw [pow_add]
        _ = muC ^ k * (6 * muC - 1) := by rw [muC_sq]
        _ = 6 * muC ^ (k + 1) - muC ^ k := by rw [pow_succ]; ring
    rw [e1, e2]; ring
  have hQ : ∀ m, (lamC ^ m + muC ^ m = (uSeq m : ℂ))
      ∧ (lamC ^ (m + 1) + muC ^ (m + 1) = (uSeq (m + 1) : ℂ)) := by
    intro m
    induction m with
    | zero =>
      refine ⟨?_, ?_⟩
      · norm_num [uSeq]
      · have h : lamC + muC = 6 := by simp [lamC, muC]; ring
        norm_num [uSeq, h]
    | succ m ihm =>
      obtain ⟨h0, h1⟩ := ihm
      refine ⟨h1, ?_⟩
      show lamC ^ (m + 2) + muC ^ (m + 2) = (uSeq (m + 2) : ℂ)
      rw [hrec m, h0, h1]
      simp only [uSeq, Int.cast_sub, Int.cast_mul]
      norm_num
  exact (hQ m).1

theorem trace_Smat_pow (m : ℕ) : (Smat ^ m).trace = lamC ^ m + muC ^ m := by
  rw [sum_pow_eq_u m]
  have hQ : ∀ m, (Smat ^ m).trace = (uSeq m : ℂ)
      ∧ (Smat ^ (m + 1)).trace = (uSeq (m + 1) : ℂ) := by
    intro m
    induction m with
    | zero =>
      refine ⟨?_, ?_⟩
      · simp [uSeq, Matrix.trace, Fin.sum_univ_two]
      · show (Smat ^ (0 + 1)).trace = (uSeq (0 + 1) : ℂ)
        rw [pow_one]
        simp [Smat, uSeq, Matrix.trace, Fin.sum_univ_two]
    | succ m ihm =>
      obtain ⟨h0, h1⟩ := ihm
      refine ⟨h1, ?_⟩
      show (Smat ^ (m + 2)).trace = (uSeq (m + 2) : ℂ)
      have hS : (Smat ^ (m + 2)).trace
          = 6 * (Smat ^ (m + 1)).trace - (Smat ^ m).trace := by
        calc (Smat ^ (m + 2)).trace
            = (Smat ^ m * Smat ^ 2).trace := by rw [pow_add]
          _ = (Smat ^ m * (6 • Smat - 1)).trace := by rw [Smat_sq]
          _ = (Smat ^ m * (6 • Smat)).trace - (Smat ^ m * 1).trace := by
              rw [Matrix.mul_sub, Matrix.trace_sub]
          _ = 6 * (Smat ^ m * Smat).trace - (Smat ^ m).trace := by
              rw [Matrix.mul_smul, Matrix.trace_smul, Matrix.mul_one]
              simp
          _ = 6 * (Smat ^ (m + 1)).trace - (Smat ^ m).trace := by
              rw [pow_succ]
      rw [hS, h0, h1]
      simp only [uSeq, Int.cast_sub, Int.cast_mul]
      norm_num
  exact (hQ m).1

/-- The boundary form: `det H_m = Tr S ^ m - 2`. -/
theorem det_eq_trace_sub_two (m : ℕ) [NeZero m] :
    ((Dm m : ℤ) : ℂ) = (Smat ^ m).trace - 2 := by
  rw [det_formula m, trace_Smat_pow m]

theorem uSeq_seven : uSeq 7 = 228486 := by decide

/-- The determinant at `m = 7`, proved structurally (no kernel `decide`). -/
theorem Dm_seven : Dm 7 = 228484 := by
  have h := det_formula 7
  rw [sum_pow_eq_u 7, uSeq_seven] at h
  have h2 : ((Dm 7 : ℤ) : ℂ) = (228484 : ℂ) := by
    rw [h]; norm_num
  exact_mod_cast h2

/-! ### The pairing on `ℤ^m` (Prop R infrastructure)

The source's quadratic form and pairing are `Q(β) = βᵀH⁻¹β` and
`β·ξ = βᵀH⁻¹ξ` with `H⁻¹ = X_m / D_m`. We work with the integral
numerators `pairNum y w = (X_m y) ⬝ᵥ w` and `Qnum y = pairNum y y`;
everything below is exact over `ℤ` or a congruence mod `D_m`.
-/

/-- The adjugate is symmetric, since `H_m` is. -/
theorem Xmat_transpose (m : ℕ) [NeZero m] : (Xmat m)ᵀ = Xmat m := by
  show ((Hmat m ℤ).adjugate)ᵀ = (Hmat m ℤ).adjugate
  rw [Matrix.adjugate_transpose, Hmat_transpose]

/-- The integral pairing numerator `(X_m y) ⬝ᵥ w`. -/
def pairNum (m : ℕ) [NeZero m] (y w : ZMod m → ℤ) : ℤ :=
  (Xmat m *ᵥ y) ⬝ᵥ w

/-- The integral quadratic-form numerator. -/
def Qnum (m : ℕ) [NeZero m] (y : ZMod m → ℤ) : ℤ := pairNum m y y

/-- Symmetry of the pairing (uses symmetry of `X_m`). -/
theorem pairNum_eq (m : ℕ) [NeZero m] (y w : ZMod m → ℤ) :
    pairNum m y w = pairNum m w y := by
  show (Xmat m *ᵥ y) ⬝ᵥ w = (Xmat m *ᵥ w) ⬝ᵥ y
  rw [dotProduct_comm, dotProduct_mulVec, ← Matrix.mulVec_transpose,
    Xmat_transpose]

/-- Shifting the left argument by `H_m t` changes the pairing by a multiple
of `D_m` (exact form). -/
theorem pairNum_add_left (m : ℕ) [NeZero m] (y w t : ZMod m → ℤ) :
    pairNum m (y + Hmat m ℤ *ᵥ t) w
      = pairNum m y w + Dm m * (t ⬝ᵥ w) := by
  have hX : Xmat m *ᵥ (y + Hmat m ℤ *ᵥ t) = Xmat m *ᵥ y + Dm m • t := by
    rw [Matrix.mulVec_add, Matrix.mulVec_mulVec, Xmat_mul_Hmat,
      Matrix.smul_mulVec, Matrix.one_mulVec]
  show (Xmat m *ᵥ (y + Hmat m ℤ *ᵥ t)) ⬝ᵥ w
    = (Xmat m *ᵥ y) ⬝ᵥ w + Dm m * (t ⬝ᵥ w)
  rw [hX, add_dotProduct]
  congr 1
  rw [smul_dotProduct]
  exact smul_eq_mul _ _

/-- Shifting the left argument by `H_m t` does not change the pairing mod `D_m`. -/
theorem pairNum_add_left_mod (m : ℕ) [NeZero m] (y w t : ZMod m → ℤ) :
    pairNum m (y + Hmat m ℤ *ᵥ t) w ≡ pairNum m y w [ZMOD Dm m] := by
  rw [pairNum_add_left, Int.modEq_iff_dvd]
  exact ⟨-(t ⬝ᵥ w), by ring⟩

/-- Shifting the right argument by `H_m t` does not change the pairing mod `D_m`. -/
theorem pairNum_add_right_mod (m : ℕ) [NeZero m] (y w t : ZMod m → ℤ) :
    pairNum m y (w + Hmat m ℤ *ᵥ t) ≡ pairNum m y w [ZMOD Dm m] := by
  rw [pairNum_eq, pairNum_add_left, pairNum_eq, Int.modEq_iff_dvd]
  exact ⟨-(t ⬝ᵥ y), by ring⟩

/-- Polar identity for `Qnum` (exact over `ℤ`). -/
theorem Qnum_add (m : ℕ) [NeZero m] (y w : ZMod m → ℤ) :
    Qnum m (y + w) = Qnum m y + Qnum m w + 2 * pairNum m y w := by
  have h : pairNum m (y + w) (y + w)
      = pairNum m y y + pairNum m w w + 2 * pairNum m y w := by
    show (Xmat m *ᵥ (y + w)) ⬝ᵥ (y + w)
      = (Xmat m *ᵥ y) ⬝ᵥ y + (Xmat m *ᵥ w) ⬝ᵥ w
        + 2 * ((Xmat m *ᵥ y) ⬝ᵥ w)
    rw [Matrix.mulVec_add, add_dotProduct, dotProduct_add, dotProduct_add,
      show (Xmat m *ᵥ w) ⬝ᵥ y = (Xmat m *ᵥ y) ⬝ᵥ w from pairNum_eq m w y]
    ring
  exact h

/-! ### The additive character and `φ̂` (Prop R)

The source's `φ̂_s(ξ) = D⁻¹ Σ_{η∈V} e(2sQ(η) - η·ξ)` with
`e(x) = exp(2πi x)`, `Q(η) = ηᵀH⁻¹η`, `η·ξ = ηᵀH⁻¹ξ`. We define it over
`V = ℤ^m / H_m ℤ^m` via the integral numerators, so every value is a
concrete complex number with no hidden choices.
-/

/-- The additive character `q ↦ exp (2πi q)` on `ℚ`. -/
noncomputable def eChar (q : ℚ) : ℂ := Complex.exp (2 * Real.pi * Complex.I * q)

theorem eChar_add (q₁ q₂ : ℚ) : eChar (q₁ + q₂) = eChar q₁ * eChar q₂ := by
  simp only [eChar, ← Complex.exp_add]
  congr 1
  push_cast
  ring

theorem eChar_int (k : ℤ) : eChar (k : ℚ) = 1 := by
  have h : (2 * Real.pi * Complex.I * ((k : ℚ) : ℂ))
      = (k : ℂ) * (2 * Real.pi * Complex.I) := by
    push_cast
    ring
  simp only [eChar]
  rw [h]
  exact Complex.exp_int_mul_two_pi_mul_I k

/-- `eChar` of a rational depends only on its class mod `ℤ`. -/
theorem eChar_eq_of_int_sub {q₁ q₂ : ℚ} {k : ℤ} (h : q₁ - q₂ = (k : ℚ)) :
    eChar q₁ = eChar q₂ := by
  have h1 : q₁ = q₂ + (k : ℚ) := by linarith
  rw [h1, eChar_add, eChar_int, mul_one]

/-- The finite abelian group `V = ℤ^m / H_m ℤ^m` (the source's `V`). -/
abbrev Vquot (m : ℕ) [NeZero m] :=
  (ZMod m → ℤ) ⧸ LinearMap.range (Matrix.mulVecLin (Hmat m ℤ))

noncomputable instance Vquot_fintype (m : ℕ) [NeZero m] : Fintype (Vquot m) :=
  Fintype.ofEquiv (Fix m) (fixEquivQuot m)

noncomputable instance Vquot_decidableEq (m : ℕ) [NeZero m] : DecidableEq (Vquot m) :=
  fun a b =>
    match decEq ((fixEquivQuot m).symm a) ((fixEquivQuot m).symm b) with
    | isTrue h => isTrue ((fixEquivQuot m).symm.injective h)
    | isFalse h => isFalse (fun hab => h (congrArg _ hab))

/-- `Qnum` shifts by a multiple of `D_m` under `y ↦ y + H_m t` (exact form). -/
theorem Qnum_add_H (m : ℕ) [NeZero m] (y t : ZMod m → ℤ) :
    Qnum m (y + Hmat m ℤ *ᵥ t)
      = Qnum m y + Dm m * (t ⬝ᵥ (Hmat m ℤ *ᵥ t))
        + 2 * (Dm m * (t ⬝ᵥ y)) := by
  have h1 : Qnum m (Hmat m ℤ *ᵥ t) = Dm m * (t ⬝ᵥ (Hmat m ℤ *ᵥ t)) := by
    have h := pairNum_add_left m 0 (Hmat m ℤ *ᵥ t) t
    rw [zero_add] at h
    have h0 : pairNum m 0 (Hmat m ℤ *ᵥ t) = 0 := by
      show (Xmat m *ᵥ (0 : ZMod m → ℤ)) ⬝ᵥ (Hmat m ℤ *ᵥ t) = 0
      rw [Matrix.mulVec_zero]
      simp [dotProduct]
    rw [h0, zero_add] at h
    exact h
  have h2 : pairNum m y (Hmat m ℤ *ᵥ t) = Dm m * (t ⬝ᵥ y) := by
    rw [pairNum_eq]
    have h := pairNum_add_left m 0 y t
    rw [zero_add] at h
    have h0 : pairNum m 0 y = 0 := by
      show (Xmat m *ᵥ (0 : ZMod m → ℤ)) ⬝ᵥ y = 0
      rw [Matrix.mulVec_zero]
      simp [dotProduct]
    rw [h0, zero_add] at h
    exact h
  rw [Qnum_add, h1, h2]

/-- `Qnum` mod `D_m` is unchanged by `y ↦ y + H_m t`. -/
theorem Qnum_add_H_mod (m : ℕ) [NeZero m] (y t : ZMod m → ℤ) :
    Qnum m (y + Hmat m ℤ *ᵥ t) ≡ Qnum m y [ZMOD Dm m] := by
  rw [Qnum_add_H, Int.modEq_iff_dvd]
  exact ⟨-(t ⬝ᵥ (Hmat m ℤ *ᵥ t) + 2 * (t ⬝ᵥ y)), by ring⟩

/-- Shifting the right argument by `H_m t` (exact form). -/
theorem pairNum_add_right (m : ℕ) [NeZero m] (y w t : ZMod m → ℤ) :
    pairNum m y (w + Hmat m ℤ *ᵥ t) = pairNum m y w + Dm m * (t ⬝ᵥ y) := by
  rw [pairNum_eq, pairNum_add_left, pairNum_eq]

/-- The `φ̂` summand as a well-defined function of `η : V` (for fixed `w`). -/
noncomputable def phiSummand (m : ℕ) [NeZero m] (s : ℤ) (w : ZMod m → ℤ) :
    Vquot m → ℂ :=
  Quotient.lift (fun y => eChar (((2 * s * Qnum m y - pairNum m y w : ℤ) : ℚ) / Dm m))
    (by
      intro y y' hy
      have h2 : (LinearMap.range (Matrix.mulVecLin (Hmat m ℤ))).quotientRel y y' := hy
      rw [Submodule.quotientRel_def] at h2
      obtain ⟨t, ht⟩ := h2
      rw [Matrix.mulVecLin_apply] at ht
      have ha : y = y' + Hmat m ℤ *ᵥ t := by
        rw [add_comm]
        exact sub_eq_iff_eq_add.mp ht.symm
      have hQ : Qnum m y ≡ Qnum m y' [ZMOD Dm m] := by
        rw [ha]
        exact Qnum_add_H_mod m y' t
      have hP : pairNum m y w ≡ pairNum m y' w [ZMOD Dm m] := by
        rw [ha]
        exact pairNum_add_left_mod m y' w t
      rw [Int.modEq_iff_dvd] at hQ hP
      obtain ⟨a, ha'⟩ := hQ
      obtain ⟨b, hb'⟩ := hP
      apply eChar_eq_of_int_sub (k := -2 * s * a + b)
      have hD : ((Dm m : ℚ)) ≠ 0 := by
        exact_mod_cast ne_of_gt (Dm_pos m)
      have haQ : ((Qnum m y' : ℚ)) - (Qnum m y : ℚ) = (Dm m : ℚ) * a := by
        exact_mod_cast ha'
      have hbQ : ((pairNum m y' w : ℚ)) - (pairNum m y w : ℚ) = (Dm m : ℚ) * b := by
        exact_mod_cast hb'
      rw [div_sub_div_same, div_eq_iff hD]
      push_cast
      linear_combination (-2 * s : ℚ) * haQ + hbQ)

theorem phiSummand_mk (m : ℕ) [NeZero m] (s : ℤ) (w y : ZMod m → ℤ) :
    phiSummand m s w (Submodule.Quotient.mk y)
      = eChar (((2 * s * Qnum m y - pairNum m y w : ℤ) : ℚ) / Dm m) :=
  rfl

/-- The source's `φ̂_s`, as a well-defined function on `V`. -/
noncomputable def phihat (m : ℕ) [NeZero m] (s : ℤ) : Vquot m → ℂ :=
  Quotient.lift
    (fun w => ((Dm m : ℂ))⁻¹ * ∑ η : Vquot m, phiSummand m s w η)
    (by
      intro w w' hw
      have h2 : (LinearMap.range (Matrix.mulVecLin (Hmat m ℤ))).quotientRel w w' := hw
      rw [Submodule.quotientRel_def] at h2
      obtain ⟨t, ht⟩ := h2
      rw [Matrix.mulVecLin_apply] at ht
      have ha : w = w' + Hmat m ℤ *ᵥ t := by
        rw [add_comm]
        exact sub_eq_iff_eq_add.mp ht.symm
      congr 1
      apply Finset.sum_congr rfl
      intro η _
      induction η using Quotient.inductionOn with
      | _ y =>
        -- `inductionOn` yields raw `Quotient.mk`, but `phiSummand_mk` is stated
        -- for `Submodule.Quotient.mk` (a plain def); `rw` cannot match across
        -- that def, so convert the goal by defeq first.
        change phiSummand m s w (Submodule.Quotient.mk y)
             = phiSummand m s w' (Submodule.Quotient.mk y)
        rw [phiSummand_mk, phiSummand_mk, ha]
        apply eChar_eq_of_int_sub (k := -(t ⬝ᵥ y))
        have hD : ((Dm m : ℚ)) ≠ 0 := by
          exact_mod_cast ne_of_gt (Dm_pos m)
        have hP := pairNum_add_right m y w' t
        have hPQ : ((pairNum m y (w' + Hmat m ℤ *ᵥ t) : ℚ))
            - (pairNum m y w' : ℚ) = (Dm m : ℚ) * (t ⬝ᵥ y) := by
          have hP' : ((pairNum m y (w' + Hmat m ℤ *ᵥ t) : ℚ))
              = (pairNum m y w' : ℚ) + (Dm m : ℚ) * (t ⬝ᵥ y) := by
            exact_mod_cast hP
          rw [hP']
          ring
        rw [div_sub_div_same, div_eq_iff hD]
        push_cast
        linear_combination -hPQ)

theorem phihat_mk (m : ℕ) [NeZero m] (s : ℤ) (w : ZMod m → ℤ) :
    phihat m s (Submodule.Quotient.mk w)
      = ((Dm m : ℂ))⁻¹ * ∑ η : Vquot m, phiSummand m s w η :=
  rfl

/-- The inner character `η ↦ e(4s·pairNum(z,η)/D)` for fixed lift `z`. -/
noncomputable def innerChar (m : ℕ) [NeZero m] (s : ℤ) (z : ZMod m → ℤ) :
    Vquot m → ℂ :=
  Quotient.lift (fun y => eChar (((4 * s * pairNum m z y : ℤ) : ℚ) / Dm m))
    (by
      intro y y' hy
      have h2 : (LinearMap.range (Matrix.mulVecLin (Hmat m ℤ))).quotientRel y y' := hy
      rw [Submodule.quotientRel_def] at h2
      obtain ⟨t, ht⟩ := h2
      rw [Matrix.mulVecLin_apply] at ht
      have ha : y = y' + Hmat m ℤ *ᵥ t := by
        rw [add_comm]
        exact sub_eq_iff_eq_add.mp ht.symm
      have hP : pairNum m z y ≡ pairNum m z y' [ZMOD Dm m] := by
        rw [ha]
        exact pairNum_add_right_mod m z y' t
      rw [Int.modEq_iff_dvd] at hP
      obtain ⟨b, hb'⟩ := hP
      -- hb' : pairNum z y' - pairNum z y = D * b, so
      -- (4s·Pzy)/D - (4s·Pzy')/D = 4s·(Pzy - Pzy')/D = 4s·(-D·b)/D = -(4s·b).
      apply eChar_eq_of_int_sub (k := -(4 * s * b))
      have hD : ((Dm m : ℚ)) ≠ 0 := by
        exact_mod_cast ne_of_gt (Dm_pos m)
      have hbQ : ((pairNum m z y' : ℚ)) - (pairNum m z y : ℚ) = (Dm m : ℚ) * b := by
        exact_mod_cast hb'
      rw [div_sub_div_same, div_eq_iff hD]
      push_cast
      linear_combination (-4 * s : ℚ) * hbQ)

theorem innerChar_mk (m : ℕ) [NeZero m] (s : ℤ) (z y : ZMod m → ℤ) :
    innerChar m s z (Submodule.Quotient.mk y)
      = eChar (((4 * s * pairNum m z y : ℤ) : ℚ) / Dm m) :=
  rfl

/-- Character property of `innerChar` in the second argument. -/
theorem innerChar_add (m : ℕ) [NeZero m] (s : ℤ) (z : ZMod m → ℤ)
    (η₁ η₂ : Vquot m) :
    innerChar m s z (η₁ + η₂) = innerChar m s z η₁ * innerChar m s z η₂ := by
  induction η₁ using Quotient.inductionOn with
  | _ y₁ =>
    induction η₂ using Quotient.inductionOn with
    | _ y₂ =>
      -- `inductionOn` yields raw `Quotient.mk`, but `mk_add`/`innerChar_mk`
      -- are stated for `Submodule.Quotient.mk` (a plain def); convert by defeq.
      change innerChar m s z (Submodule.Quotient.mk y₁ + Submodule.Quotient.mk y₂)
           = innerChar m s z (Submodule.Quotient.mk y₁)
             * innerChar m s z (Submodule.Quotient.mk y₂)
      rw [← Submodule.Quotient.mk_add, innerChar_mk, innerChar_mk, innerChar_mk,
        ← eChar_add]
      congr 1
      have h : pairNum m z (y₁ + y₂) = pairNum m z y₁ + pairNum m z y₂ := by
        show (Xmat m *ᵥ z) ⬝ᵥ (y₁ + y₂) = (Xmat m *ᵥ z) ⬝ᵥ y₁ + (Xmat m *ᵥ z) ⬝ᵥ y₂
        exact dotProduct_add _ _ _
      rw [h]
      push_cast
      ring

/-- Character-sum dichotomy over `V`. -/
theorem innerChar_sum (m : ℕ) [NeZero m] (s : ℤ) (z : ZMod m → ℤ) :
    (∑ η : Vquot m, innerChar m s z η)
      = if (∀ η : Vquot m, innerChar m s z η = 1) then (Dm m : ℂ) else 0 := by
  by_cases htriv : ∀ η : Vquot m, innerChar m s z η = 1
  · rw [if_pos htriv]
    have hcard : Fintype.card (Vquot m) = (Dm m).toNat := by
      rw [← card_Fix m]
      exact (Fintype.card_congr (fixEquivQuot m)).symm
    rw [Finset.sum_congr rfl (fun η _ => htriv η), Finset.sum_const, Finset.card_univ,
      hcard, nsmul_eq_mul, mul_one]
    have h2 : ((Dm m).toNat : ℤ) = Dm m := Int.toNat_of_nonneg (le_of_lt (Dm_pos m))
    exact_mod_cast h2
  · rw [if_neg htriv]
    push_neg at htriv
    obtain ⟨η₀, hη₀⟩ := htriv
    have h2 : (∑ η : Vquot m, innerChar m s z (η₀ + η))
        = innerChar m s z η₀ * (∑ η : Vquot m, innerChar m s z η) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro η _
      exact innerChar_add m s z η₀ η
    have h3 : (∑ η : Vquot m, innerChar m s z η)
        = innerChar m s z η₀ * (∑ η : Vquot m, innerChar m s z η) := by
      rw [← h2]
      exact (Equiv.sum_comp (Equiv.addLeft η₀) (fun η => innerChar m s z η)).symm
    have h4 : (1 - innerChar m s z η₀) * (∑ η : Vquot m, innerChar m s z η) = 0 := by
      linear_combination h3
    rcases mul_eq_zero.mp h4 with h | h
    · exact absurd (sub_eq_zero.mp h).symm hη₀
    · exact h

/-- Triviality criterion: the inner character is trivial iff `4 • γ = 0`
(for `s` coprime to `D`). -/
theorem innerChar_triv_iff (m : ℕ) [NeZero m] (s : ℤ) (hs : IsCoprime s (Dm m))
    (z : ZMod m → ℤ) :
    (∀ η : Vquot m, innerChar m s z η = 1)
      ↔ (4 : ℤ) • (Submodule.Quotient.mk z : Vquot m) = 0 := by
  have hD0 : (Dm m) ≠ 0 := ne_of_gt (Dm_pos m)
  have hDQ : ((Dm m : ℚ)) ≠ 0 := by exact_mod_cast hD0
  constructor
  · intro htriv
    -- Step 1: D ∣ 4s·(Xz)_i for every i.
    have hdiv : ∀ i : ZMod m, Dm m ∣ 4 * s * (Xmat m *ᵥ z) i := by
      intro i
      have h1 := htriv (Submodule.Quotient.mk (Pi.single i 1))
      rw [innerChar_mk] at h1
      have hP : pairNum m z (Pi.single i 1) = (Xmat m *ᵥ z) i := by
        show (Xmat m *ᵥ z) ⬝ᵥ (Pi.single i 1) = (Xmat m *ᵥ z) i
        rw [dotProduct_single]
        simp
      rw [hP] at h1
      simp only [eChar] at h1
      rw [Complex.exp_eq_one_iff] at h1
      obtain ⟨n, hn⟩ := h1
      have h2pi : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
        apply mul_ne_zero
        apply mul_ne_zero
        · norm_num
        · exact_mod_cast Real.pi_ne_zero
        · exact Complex.I_ne_zero
      rw [mul_comm (n : ℂ) (2 * Real.pi * Complex.I : ℂ)] at hn
      have hq : ((((4 * s * (Xmat m *ᵥ z) i : ℤ) : ℚ) / Dm m : ℚ) : ℂ) = (n : ℂ) :=
        mul_left_cancel₀ h2pi hn
      have hqQ : ((4 * s * (Xmat m *ᵥ z) i : ℤ) : ℚ) / Dm m = (n : ℚ) := by
        exact_mod_cast hq
      have hqZ : 4 * s * (Xmat m *ᵥ z) i = n * Dm m := by
        have h := (div_eq_iff hDQ).mp hqQ
        exact_mod_cast h
      exact ⟨n, by rw [mul_comm (Dm m) n]; exact hqZ⟩
    -- Step 2: coprimality removes s.
    obtain ⟨u, v, huv⟩ := hs
    have hdiv4 : ∀ i : ZMod m, Dm m ∣ 4 * (Xmat m *ᵥ z) i := by
      intro i
      obtain ⟨c, hc⟩ := hdiv i
      have h2 : 4 * (Xmat m *ᵥ z) i
          = u * (4 * s * (Xmat m *ᵥ z) i) + v * Dm m * (4 * (Xmat m *ᵥ z) i) := by
        have : u * s + v * Dm m = 1 := huv
        linear_combination (-(4 * (Xmat m *ᵥ z) i)) * this
      rw [h2]
      apply dvd_add
      · exact dvd_mul_of_dvd_right ⟨c, hc⟩ u
      · exact ⟨v * (4 * (Xmat m *ᵥ z) i), by ring⟩
    -- Step 3: build t with H*ᵥt = 4z, hence 4 • mk z = 0.
    classical
    let t : ZMod m → ℤ := fun i => 4 * (Xmat m *ᵥ z) i / Dm m
    have ht : Hmat m ℤ *ᵥ t = (4 : ℤ) • z := by
      have hDsmul : Dm m • (Hmat m ℤ *ᵥ t) = Dm m • ((4 : ℤ) • z) := by
        have e1 : Dm m • (Hmat m ℤ *ᵥ t) = Hmat m ℤ *ᵥ (Dm m • t) := by
          rw [← Matrix.mulVec_smul]
        have e2 : Dm m • t = (4 : ℤ) • (Xmat m *ᵥ z) := by
          funext i
          rw [Pi.smul_apply, Pi.smul_apply]
          show Dm m * (4 * (Xmat m *ᵥ z) i / Dm m) = 4 * (Xmat m *ᵥ z) i
          rw [Int.mul_ediv_cancel' (hdiv4 i)]
        rw [e1, e2]
        have e3 : Hmat m ℤ *ᵥ ((4 : ℤ) • (Xmat m *ᵥ z))
            = (4 : ℤ) • (Hmat m ℤ *ᵥ (Xmat m *ᵥ z)) :=
          Matrix.mulVec_smul _ _ _
        rw [e3, Matrix.mulVec_mulVec, Hmat_mul_Xmat, Matrix.smul_mulVec, Matrix.one_mulVec,
          smul_smul, smul_smul, mul_comm (4 : ℤ) (Dm m)]
      funext i
      have h := congrFun hDsmul i
      rw [Pi.smul_apply, Pi.smul_apply, Pi.smul_apply] at h
      have e1 : Dm m • (Hmat m ℤ *ᵥ t) i = Dm m * (Hmat m ℤ *ᵥ t) i := smul_eq_mul _ _
      have e2 : Dm m • ((4 : ℤ) • z i) = Dm m * (4 * z i) := by
        have e : (4 : ℤ) • z i = 4 * z i := smul_eq_mul _ _
        rw [e, smul_eq_mul]
      rw [e1, e2] at h
      show (Hmat m ℤ *ᵥ t) i = 4 * z i
      exact mul_left_cancel₀ hD0 h
    have hmk : (Submodule.Quotient.mk ((4 : ℤ) • z) : Vquot m) = 0 := by
      rw [Submodule.Quotient.mk_eq_zero]
      exact ⟨t, by rw [Matrix.mulVecLin_apply]; exact ht⟩
    -- mk_smul is proved by rfl, so mk (4•z) ≡ 4•mk z definitionally.
    exact hmk
  · intro h4
    -- 4 • mk z = 0 → 4z ∈ range → ∃t, H*ᵥt = 4z → D ∣ 4·(Xz)_i → D ∣ 4s·P z y → eChar = 1.
    -- mk_smul is rfl, so h4 is definitionally mk (4•z) = 0.
    have hmk : (Submodule.Quotient.mk ((4 : ℤ) • z) : Vquot m) = 0 := h4
    rw [Submodule.Quotient.mk_eq_zero] at hmk
    obtain ⟨t, ht⟩ := hmk
    rw [Matrix.mulVecLin_apply] at ht
    -- ht : H *ᵥ t = 4 • z
    have hX : (4 : ℤ) • (Xmat m *ᵥ z) = Dm m • t := by
      have e1 : Xmat m *ᵥ ((4 : ℤ) • z) = (4 : ℤ) • (Xmat m *ᵥ z) :=
        Matrix.mulVec_smul _ _ _
      have e2 : Xmat m *ᵥ (Hmat m ℤ *ᵥ t) = Dm m • t := by
        rw [Matrix.mulVec_mulVec, Xmat_mul_Hmat, Matrix.smul_mulVec, Matrix.one_mulVec]
      rw [ht] at e2
      rw [e1] at e2
      exact e2
    have hdiv4 : ∀ i : ZMod m, Dm m ∣ 4 * (Xmat m *ᵥ z) i := by
      intro i
      have h := congrFun hX i
      rw [Pi.smul_apply, Pi.smul_apply] at h
      have e1 : (4 : ℤ) • (Xmat m *ᵥ z) i = 4 * (Xmat m *ᵥ z) i := smul_eq_mul _ _
      have e2 : Dm m • t i = Dm m * t i := smul_eq_mul _ _
      rw [e1, e2] at h
      exact ⟨t i, h⟩
    intro η
    induction η using Quotient.inductionOn with
    | _ y =>
      -- Same `Quotient.mk` vs `Submodule.Quotient.mk` conversion as in `phihat`.
      change innerChar m s z (Submodule.Quotient.mk y) = 1
      rw [innerChar_mk]
      have hdiv : Dm m ∣ 4 * s * pairNum m z y := by
        have hsum : 4 * s * pairNum m z y
            = ∑ i, (s * (4 * (Xmat m *ᵥ z) i)) * y i := by
          show 4 * s * ((Xmat m *ᵥ z) ⬝ᵥ y) = _
          simp only [dotProduct, Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro i _
          ring
        rw [hsum]
        apply Finset.dvd_sum
        intro i _
        exact dvd_mul_of_dvd_left (dvd_mul_of_dvd_right (hdiv4 i) s) (y i)
      obtain ⟨k, hk⟩ := hdiv
      have hq : (((4 * s * pairNum m z y : ℤ) : ℚ) / Dm m) = (k : ℚ) := by
        rw [hk]
        push_cast
        rw [mul_div_cancel_left₀ (k : ℚ) hDQ]
      rw [hq, eChar_int]

/-- `star` of a rational phase: `star (e(q)) = e(-q)`. -/
theorem star_eChar (q : ℚ) : star (eChar q) = eChar (-q) := by
  have h1 : eChar q = Complex.exp (2 * Real.pi * ((q : ℝ) : ℂ) * Complex.I) := by
    show Complex.exp (2 * Real.pi * Complex.I * (q : ℂ)) = _
    congr 1
    push_cast
    ring
  have h2 : eChar (-q) = Complex.exp (-(2 * Real.pi * ((q : ℝ) : ℂ)) * Complex.I) := by
    show Complex.exp (2 * Real.pi * Complex.I * ((-q : ℚ) : ℂ)) = _
    congr 1
    push_cast
    ring
  rw [h1, h2, Complex.exp_mul_I, Complex.exp_mul_I, Complex.cos_neg, Complex.sin_neg,
    star_add, star_mul]
  have hc : star (Complex.cos (2 * Real.pi * ((q : ℝ) : ℂ)))
      = Complex.cos (2 * Real.pi * ((q : ℝ) : ℂ)) := by
    rw [show (2 * (Real.pi : ℂ) * ((q : ℝ) : ℂ))
        = (((2 * Real.pi * (q : ℝ)) : ℝ) : ℂ) from by push_cast; ring,
      ← Complex.ofReal_cos]
    exact Complex.conj_ofReal _
  have hs : star (Complex.sin (2 * Real.pi * ((q : ℝ) : ℂ)))
      = Complex.sin (2 * Real.pi * ((q : ℝ) : ℂ)) := by
    rw [show (2 * (Real.pi : ℂ) * ((q : ℝ) : ℂ))
        = (((2 * Real.pi * (q : ℝ)) : ℝ) : ℂ) from by push_cast; ring,
      ← Complex.ofReal_sin]
    exact Complex.conj_ofReal _
  have hI : star (Complex.I : ℂ) = -Complex.I := by simp
  rw [hc, hs, hI]
  ring

/-- Left additivity of `pairNum` in the first argument. -/
theorem pairNum_add_fst (m : ℕ) [NeZero m] (y₁ y₂ w : ZMod m → ℤ) :
    pairNum m (y₁ + y₂) w = pairNum m y₁ w + pairNum m y₂ w := by
  show (Xmat m *ᵥ (y₁ + y₂)) ⬝ᵥ w = (Xmat m *ᵥ y₁) ⬝ᵥ w + (Xmat m *ᵥ y₂) ⬝ᵥ w
  rw [Matrix.mulVec_add, add_dotProduct]

/-- The 4-torsion subgroup of `V` (the source's `V[4]` as a subgroup). -/
noncomputable def torsionSubgroup (m : ℕ) [NeZero m] : AddSubgroup (Vquot m) where
  carrier := {γ | (4 : ℤ) • γ = 0}
  add_mem' := by
    intro a b ha hb
    have ha' : (4 : ℤ) • a = 0 := ha
    have hb' : (4 : ℤ) • b = 0 := hb
    show (4 : ℤ) • (a + b) = 0
    rw [smul_add, ha', hb', add_zero]
  zero_mem' := by
    show (4 : ℤ) • (0 : Vquot m) = 0
    exact smul_zero _
  neg_mem' := by
    intro a ha
    have ha' : (4 : ℤ) • a = 0 := ha
    show (4 : ℤ) • (-a) = 0
    rw [smul_neg, ha', neg_zero]

noncomputable instance torsionDecidablePred (m : ℕ) [NeZero m] :
    DecidablePred (· ∈ torsionSubgroup m) :=
  fun γ =>
    match decEq ((4 : ℤ) • γ) 0 with
    | isTrue h => isTrue (show γ ∈ torsionSubgroup m from h)
    | isFalse h => isFalse (show ¬(γ ∈ torsionSubgroup m) from h)

/-- The inner character as a function on `V × V`. -/
noncomputable def innerCharQ (m : ℕ) [NeZero m] (s : ℤ) : Vquot m → Vquot m → ℂ :=
  Quotient.lift (fun z => fun η' => innerChar m s z η')
    (by
      intro z z' hz
      have h2 : (LinearMap.range (Matrix.mulVecLin (Hmat m ℤ))).quotientRel z z' := hz
      rw [Submodule.quotientRel_def] at h2
      obtain ⟨t, ht⟩ := h2
      rw [Matrix.mulVecLin_apply] at ht
      have ha : z = z' + Hmat m ℤ *ᵥ t := by
        rw [add_comm]
        exact sub_eq_iff_eq_add.mp ht.symm
      funext η'
      induction η' using Quotient.inductionOn with
      | _ y' =>
        change innerChar m s z (Submodule.Quotient.mk y')
             = innerChar m s z' (Submodule.Quotient.mk y')
        rw [innerChar_mk, innerChar_mk, ha]
        apply eChar_eq_of_int_sub (k := 4 * s * (t ⬝ᵥ y'))
        have hD : ((Dm m : ℚ)) ≠ 0 := by
          exact_mod_cast ne_of_gt (Dm_pos m)
        have hP := pairNum_add_left m z' y' t
        have hPQ : ((pairNum m (z' + Hmat m ℤ *ᵥ t) y' : ℚ))
            = (pairNum m z' y' : ℚ) + (Dm m : ℚ) * (t ⬝ᵥ y') := by
          exact_mod_cast hP
        rw [div_sub_div_same, div_eq_iff hD]
        push_cast
        linear_combination (4 * s : ℚ) * hPQ)

theorem innerCharQ_mk (m : ℕ) [NeZero m] (s : ℤ) (z : ZMod m → ℤ) (η' : Vquot m) :
    innerCharQ m s (Submodule.Quotient.mk z) η' = innerChar m s z η' :=
  rfl

/-- Pointwise factorisation of a summand against its conjugate. -/
theorem phiSummand_mul_star (m : ℕ) [NeZero m] (s : ℤ) (w y y' : ZMod m → ℤ) :
    phiSummand m s w (Submodule.Quotient.mk y)
        * star (phiSummand m s w (Submodule.Quotient.mk y'))
      = phiSummand m s w (Submodule.Quotient.mk (y - y'))
        * innerChar m s (y - y') (Submodule.Quotient.mk y') := by
  rw [phiSummand_mk, phiSummand_mk, phiSummand_mk, innerChar_mk, star_eChar,
    ← eChar_add, ← eChar_add]
  congr 1
  have hQ : Qnum m y = Qnum m (y - y') + Qnum m y' + 2 * pairNum m (y - y') y' := by
    have h := Qnum_add m (y - y') y'
    rw [sub_add_cancel] at h
    exact h
  have hP : pairNum m y w = pairNum m (y - y') w + pairNum m y' w := by
    have h := pairNum_add_fst m (y - y') y' w
    rw [sub_add_cancel] at h
    exact h
  have hQ' : ((Qnum m y : ℚ))
      = (Qnum m (y - y') : ℚ) + (Qnum m y' : ℚ)
        + 2 * (pairNum m (y - y') y' : ℚ) := by
    exact_mod_cast hQ
  have hP' : ((pairNum m y w : ℚ))
      = (pairNum m (y - y') w : ℚ) + (pairNum m y' w : ℚ) := by
    exact_mod_cast hP
  rw [← neg_div, ← add_div, ← add_div]
  congr 1
  push_cast
  linear_combination (2 * s : ℚ) * hQ' - hP'

/-- Reindexing the double sum by the difference variable. -/
theorem sum_factor (m : ℕ) [NeZero m] (s : ℤ) (w : ZMod m → ℤ) (η' : Vquot m) :
    (∑ γ : Vquot m, phiSummand m s w (γ + η') * star (phiSummand m s w η'))
      = (∑ γ : Vquot m, phiSummand m s w γ * innerCharQ m s γ η') := by
  apply Finset.sum_congr rfl
  intro γ _
  induction γ using Quotient.inductionOn with
  | _ y0 =>
    induction η' using Quotient.inductionOn with
    | _ y' =>
      change phiSummand m s w (Submodule.Quotient.mk y0 + Submodule.Quotient.mk y')
          * star (phiSummand m s w (Submodule.Quotient.mk y'))
        = phiSummand m s w (Submodule.Quotient.mk y0)
          * innerCharQ m s (Submodule.Quotient.mk y0) (Submodule.Quotient.mk y')
      rw [← Submodule.Quotient.mk_add, innerCharQ_mk]
      have h := phiSummand_mul_star m s w (y0 + y') y'
      rw [add_sub_cancel_right] at h
      exact h

/-- The inner-character sum over the second variable, by torsion membership. -/
theorem innerCharQ_sum (m : ℕ) [NeZero m] (s : ℤ) (hs : IsCoprime s (Dm m))
    (γ : Vquot m) :
    (∑ η' : Vquot m, innerCharQ m s γ η')
      = if γ ∈ torsionSubgroup m then (Dm m : ℂ) else 0 := by
  induction γ using Quotient.inductionOn with
  | _ z =>
    change (∑ η' : Vquot m, innerCharQ m s (Submodule.Quotient.mk z) η')
        = if (Submodule.Quotient.mk z) ∈ torsionSubgroup m then (Dm m : ℂ) else 0
    have h1 : (∑ η' : Vquot m, innerCharQ m s (Submodule.Quotient.mk z) η')
        = (∑ η' : Vquot m, innerChar m s z η') := by
      apply Finset.sum_congr rfl
      intro η' _
      exact innerCharQ_mk m s z η'
    rw [h1, innerChar_sum]
    by_cases htriv : ∀ η' : Vquot m, innerChar m s z η' = 1
    · rw [if_pos htriv,
        if_pos (show (Submodule.Quotient.mk z) ∈ torsionSubgroup m from
          (innerChar_triv_iff m s hs z).mp htriv)]
    · rw [if_neg htriv]
      by_cases hmem : (Submodule.Quotient.mk z) ∈ torsionSubgroup m
      · exfalso
        exact htriv ((innerChar_triv_iff m s hs z).mpr hmem)
      · rw [if_neg hmem]

/-- Collapsing an indicator sum over `V` to the subgroup sum. -/
theorem sum_ite_torsion (m : ℕ) [NeZero m] (f : Vquot m → ℂ) :
    (∑ γ : Vquot m, if γ ∈ torsionSubgroup m then f γ else 0)
      = ∑ γ : ↥(torsionSubgroup m), f γ.1 := by
  have h1 : (∑ γ : Vquot m, if γ ∈ torsionSubgroup m then f γ else 0)
      = ∑ γ ∈ Finset.univ.filter (· ∈ torsionSubgroup m), f γ := by
    rw [Finset.sum_filter]
  rw [h1]
  symm
  apply Finset.sum_bij (fun γ _ => γ.1)
  · intro γ _
    show γ.1 ∈ Finset.univ.filter (· ∈ torsionSubgroup m)
    rw [Finset.mem_filter]
    exact ⟨Finset.mem_univ _, γ.2⟩
  · intro a _ b _ hab
    exact Subtype.ext hab
  · intro x hx
    obtain ⟨_, hx2⟩ := Finset.mem_filter.mp hx
    exact ⟨⟨x, hx2⟩, Finset.mem_univ _, rfl⟩
  · intro γ _
    rfl

/-- The double sum collapses to `D` times the torsion sum. -/
theorem double_sum_eq (m : ℕ) [NeZero m] (s : ℤ) (hs : IsCoprime s (Dm m))
    (w : ZMod m → ℤ) :
    (∑ η : Vquot m, ∑ η' : Vquot m,
        phiSummand m s w η * star (phiSummand m s w η'))
      = (Dm m : ℂ) * ∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1 := by
  rw [Finset.sum_comm]
  have hstep : ∀ η' : Vquot m,
      (∑ η : Vquot m, phiSummand m s w η * star (phiSummand m s w η'))
        = ∑ γ : Vquot m, phiSummand m s w γ * innerCharQ m s γ η' := by
    intro η'
    rw [← Equiv.sum_comp (Equiv.addRight η')
      (fun η => phiSummand m s w η * star (phiSummand m s w η'))]
    exact sum_factor m s w η'
  rw [Finset.sum_congr rfl (fun η' _ => hstep η'), Finset.sum_comm]
  have hstep2 : ∀ γ : Vquot m,
      (∑ η' : Vquot m, phiSummand m s w γ * innerCharQ m s γ η')
        = phiSummand m s w γ
          * (if γ ∈ torsionSubgroup m then (Dm m : ℂ) else 0) := by
    intro γ
    rw [← Finset.mul_sum, innerCharQ_sum m s hs γ]
  rw [Finset.sum_congr rfl (fun γ _ => hstep2 γ)]
  have hstep3 : ∀ γ : Vquot m,
      phiSummand m s w γ * (if γ ∈ torsionSubgroup m then (Dm m : ℂ) else 0)
        = if γ ∈ torsionSubgroup m then (Dm m : ℂ) * phiSummand m s w γ else 0 := by
    intro γ
    by_cases h : γ ∈ torsionSubgroup m
    · rw [if_pos h, if_pos h, mul_comm]
    · rw [if_neg h, if_neg h, mul_zero]
  rw [Finset.sum_congr rfl (fun γ _ => hstep3 γ)]
  have hstep4 : ∀ γ : Vquot m,
      (if γ ∈ torsionSubgroup m then (Dm m : ℂ) * phiSummand m s w γ else 0)
        = (Dm m : ℂ) * (if γ ∈ torsionSubgroup m then phiSummand m s w γ else 0) := by
    intro γ
    by_cases h : γ ∈ torsionSubgroup m
    · rw [if_pos h, if_pos h]
    · rw [if_neg h, if_neg h, mul_zero]
  rw [Finset.sum_congr rfl (fun γ _ => hstep4 γ), ← Finset.mul_sum]
  congr 1
  exact sum_ite_torsion m (fun γ => phiSummand m s w γ)

/-- The modulus identity: `|φ̂_s(ξ)|²` is `D⁻¹` times the torsion sum. -/
theorem phihat_modulus (m : ℕ) [NeZero m] (s : ℤ) (hs : IsCoprime s (Dm m))
    (w : ZMod m → ℤ) :
    phihat m s (Submodule.Quotient.mk w)
        * star (phihat m s (Submodule.Quotient.mk w))
      = (Dm m : ℂ)⁻¹ * ∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1 := by
  have hD : (Dm m : ℂ) ≠ 0 := by exact_mod_cast ne_of_gt (Dm_pos m)
  have hstarD : star ((Dm m : ℂ))⁻¹ = ((Dm m : ℂ))⁻¹ := by
    simp only [star_inv₀, star_intCast]
  rw [phihat_mk, star_mul, star_sum, hstarD]
  have hAB : (∑ η : Vquot m, phiSummand m s w η)
        * (∑ η' : Vquot m, star (phiSummand m s w η'))
      = (Dm m : ℂ) * ∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1 := by
    rw [Finset.sum_mul_sum]
    exact double_sum_eq m s hs w
  rw [show (Dm m : ℂ)⁻¹ * (∑ η : Vquot m, phiSummand m s w η)
        * ((∑ η' : Vquot m, star (phiSummand m s w η')) * (Dm m : ℂ)⁻¹)
      = (Dm m : ℂ)⁻¹ * (Dm m : ℂ)⁻¹
        * ((∑ η : Vquot m, phiSummand m s w η)
          * (∑ η' : Vquot m, star (phiSummand m s w η'))) from by ring, hAB]
  rw [show (Dm m : ℂ)⁻¹ * (Dm m : ℂ)⁻¹
        * ((Dm m : ℂ) * ∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1)
      = ((Dm m : ℂ)⁻¹ * (Dm m : ℂ))
        * ((Dm m : ℂ)⁻¹ * ∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1) from by ring,
    inv_mul_cancel₀ hD, one_mul]

/-- From torsion membership to a lift of `4z` through `H`. -/
theorem torsion_ht (m : ℕ) [NeZero m] (z : ZMod m → ℤ)
    (hz : (4 : ℤ) • (Submodule.Quotient.mk z : Vquot m) = 0) :
    ∃ t : ZMod m → ℤ, Hmat m ℤ *ᵥ t = (4 : ℤ) • z := by
  have hmk : (Submodule.Quotient.mk ((4 : ℤ) • z) : Vquot m) = 0 := hz
  rw [Submodule.Quotient.mk_eq_zero] at hmk
  obtain ⟨t, ht⟩ := hmk
  rw [Matrix.mulVecLin_apply] at ht
  exact ⟨t, ht⟩

/-- The key divisibility: `4·pairNum` is a multiple of `D` on torsion. -/
theorem four_pairNum_eq (m : ℕ) [NeZero m] (z₁ z₂ t : ZMod m → ℤ)
    (ht : Hmat m ℤ *ᵥ t = (4 : ℤ) • z₁) :
    4 * pairNum m z₁ z₂ = Dm m * (t ⬝ᵥ z₂) := by
  have e1 : (4 : ℤ) • (Xmat m *ᵥ z₁) = Dm m • t := by
    have h1 : Xmat m *ᵥ ((4 : ℤ) • z₁) = (4 : ℤ) • (Xmat m *ᵥ z₁) :=
      Matrix.mulVec_smul _ _ _
    rw [← ht] at h1
    have h2 : Xmat m *ᵥ (Hmat m ℤ *ᵥ t) = Dm m • t := by
      rw [Matrix.mulVec_mulVec, Xmat_mul_Hmat, Matrix.smul_mulVec, Matrix.one_mulVec]
    rw [h2] at h1
    exact h1.symm
  have e2 : ((4 : ℤ) • (Xmat m *ᵥ z₁)) ⬝ᵥ z₂
      = (4 : ℤ) • ((Xmat m *ᵥ z₁) ⬝ᵥ z₂) :=
    smul_dotProduct _ _ _
  have e3 : (Dm m • t) ⬝ᵥ z₂ = Dm m * (t ⬝ᵥ z₂) := by
    rw [smul_dotProduct]
    exact smul_eq_mul _ _
  have e0 : (4 : ℤ) • ((Xmat m *ᵥ z₁) ⬝ᵥ z₂) = 4 * ((Xmat m *ᵥ z₁) ⬝ᵥ z₂) :=
    smul_eq_mul _ _
  show 4 * ((Xmat m *ᵥ z₁) ⬝ᵥ z₂) = Dm m * (t ⬝ᵥ z₂)
  rw [← e0, ← e2, e1, e3]

/-- Multiplicativity of the torsion summand in the first factor. -/
theorem phiSummand_torsion_mul (m : ℕ) [NeZero m] (s : ℤ) (w z₁ z₂ : ZMod m → ℤ)
    (hz : (4 : ℤ) • (Submodule.Quotient.mk z₁ : Vquot m) = 0) :
    phiSummand m s w (Submodule.Quotient.mk (z₁ + z₂))
      = phiSummand m s w (Submodule.Quotient.mk z₁)
        * phiSummand m s w (Submodule.Quotient.mk z₂) := by
  obtain ⟨t, ht⟩ := torsion_ht m z₁ hz
  have h4 : 4 * pairNum m z₁ z₂ = Dm m * (t ⬝ᵥ z₂) :=
    four_pairNum_eq m z₁ z₂ t ht
  rw [phiSummand_mk, phiSummand_mk, phiSummand_mk, ← eChar_add]
  apply eChar_eq_of_int_sub (k := s * (t ⬝ᵥ z₂))
  have hD : ((Dm m : ℚ)) ≠ 0 := by exact_mod_cast ne_of_gt (Dm_pos m)
  have hQ : Qnum m (z₁ + z₂) = Qnum m z₁ + Qnum m z₂ + 2 * pairNum m z₁ z₂ :=
    Qnum_add m z₁ z₂
  have hP : pairNum m (z₁ + z₂) w = pairNum m z₁ w + pairNum m z₂ w :=
    pairNum_add_fst m z₁ z₂ w
  have hQ' : ((Qnum m (z₁ + z₂) : ℚ))
      = (Qnum m z₁ : ℚ) + (Qnum m z₂ : ℚ) + 2 * (pairNum m z₁ z₂ : ℚ) := by
    exact_mod_cast hQ
  have hP' : ((pairNum m (z₁ + z₂) w : ℚ))
      = (pairNum m z₁ w : ℚ) + (pairNum m z₂ w : ℚ) := by
    exact_mod_cast hP
  have h4' : ((4 * pairNum m z₁ z₂ : ℚ)) = (Dm m : ℚ) * (t ⬝ᵥ z₂) := by
    exact_mod_cast h4
  rw [← add_div, ← sub_div, div_eq_iff hD]
  push_cast
  linear_combination (2 * s : ℚ) * hQ' - hP' + s * h4'

/-- The torsion summand is a character of the torsion subgroup. -/
theorem torsion_char (m : ℕ) [NeZero m] (s : ℤ) (w : ZMod m → ℤ)
    (γ₁ γ₂ : ↥(torsionSubgroup m)) :
    phiSummand m s w ((γ₁ + γ₂ : ↥(torsionSubgroup m)).1)
      = phiSummand m s w γ₁.1 * phiSummand m s w γ₂.1 := by
  obtain ⟨z₁, hz₁⟩ := Quotient.exists_rep γ₁.1
  obtain ⟨z₂, hz₂⟩ := Quotient.exists_rep γ₂.1
  have h1 : γ₁.1 = Submodule.Quotient.mk z₁ := hz₁.symm
  have h2 : γ₂.1 = Submodule.Quotient.mk z₂ := hz₂.symm
  have ht1 : (4 : ℤ) • (Submodule.Quotient.mk z₁ : Vquot m) = 0 := by
    rw [← h1]
    exact γ₁.2
  have hsum : ((γ₁ + γ₂ : ↥(torsionSubgroup m)).1 : Vquot m)
      = Submodule.Quotient.mk (z₁ + z₂) := by
    rw [AddSubgroup.coe_add, h1, h2, ← Submodule.Quotient.mk_add]
  rw [hsum, phiSummand_torsion_mul m s w z₁ z₂ ht1, h1, h2]

/-- The torsion sum is either the full cardinality or zero. -/
theorem torsion_sum_values (m : ℕ) [NeZero m] (s : ℤ) (w : ZMod m → ℤ) :
    (∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1)
      = (Fintype.card ↥(torsionSubgroup m) : ℂ)
      ∨ (∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1) = 0 := by
  by_cases htriv : ∀ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1 = 1
  · left
    rw [Finset.sum_congr rfl (fun γ _ => htriv γ), Finset.sum_const, Finset.card_univ,
      nsmul_eq_mul, mul_one]
  · right
    push_neg at htriv
    obtain ⟨γ₀, hγ₀⟩ := htriv
    have h2 : (∑ γ : ↥(torsionSubgroup m), phiSummand m s w (γ₀ + γ).1)
        = phiSummand m s w γ₀.1
          * (∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro γ _
      exact torsion_char m s w γ₀ γ
    have h3 : (∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1)
        = phiSummand m s w γ₀.1
          * (∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1) := by
      rw [← h2]
      exact (Equiv.sum_comp (Equiv.addLeft γ₀) (fun γ => phiSummand m s w γ.1)).symm
    have h4 : (1 - phiSummand m s w γ₀.1)
        * (∑ γ : ↥(torsionSubgroup m), phiSummand m s w γ.1) = 0 := by
      linear_combination h3
    rcases mul_eq_zero.mp h4 with h | h
    · exact absurd (sub_eq_zero.mp h).symm hγ₀
    · exact h

/-- Uniqueness of the torsion lift modulo 4. -/
theorem torsion_t_mod4_unique (m : ℕ) [NeZero m] (z₁ z₂ t₁ t₂ : ZMod m → ℤ)
    (ht1 : Hmat m ℤ *ᵥ t₁ = (4 : ℤ) • z₁) (ht2 : Hmat m ℤ *ᵥ t₂ = (4 : ℤ) • z₂)
    (hmk : (Submodule.Quotient.mk z₁ : Vquot m) = Submodule.Quotient.mk z₂) :
    ∀ i : ZMod m, ((t₁ i : ℤ) : ZMod 4) = ((t₂ i : ℤ) : ZMod 4) := by
  have hmem : z₁ - z₂ ∈ LinearMap.range (Matrix.mulVecLin (Hmat m ℤ)) :=
    (Submodule.Quotient.eq _).mp hmk
  obtain ⟨s, hs⟩ := hmem
  rw [Matrix.mulVecLin_apply] at hs
  have h0 : Hmat m ℤ *ᵥ (t₁ - t₂ - (4 : ℤ) • s) = 0 := by
    rw [Matrix.mulVec_sub, Matrix.mulVec_sub, Matrix.mulVec_smul, ht1, ht2, hs, smul_sub]
    abel
  have hdiff : t₁ - t₂ = (4 : ℤ) • s := sub_eq_zero.mp (Hmat_mulVec_eq_zero m _ h0)
  intro i
  have hi : t₁ i - t₂ i = 4 * s i := congrFun hdiff i
  have h21 : t₂ i - t₁ i = 4 * (-s i) := by linear_combination -hi
  exact (ZMod.intCast_eq_intCast_iff_dvd_sub _ _ _).mpr ⟨-s i, h21⟩

/-- A torsion element has a lift through `H`, with the canonical representative. -/
theorem torsion_lift_exists (m : ℕ) [NeZero m] (γ : ↥(torsionSubgroup m)) :
    ∃ t : ZMod m → ℤ, Hmat m ℤ *ᵥ t = (4 : ℤ) • (Quotient.out γ.1) := by
  apply torsion_ht
  have h : (Submodule.Quotient.mk (Quotient.out γ.1) : Vquot m) = γ.1 :=
    Quotient.out_eq γ.1
  rw [h]
  exact γ.2

/-- The chosen torsion lift (via the canonical representative). -/
noncomputable def torsionLift (m : ℕ) [NeZero m] (γ : ↥(torsionSubgroup m)) :
    ZMod m → ℤ :=
  Classical.choose (torsion_lift_exists m γ)

/-- The chosen lift indeed lifts `4·out γ`. -/
theorem torsionLift_spec (m : ℕ) [NeZero m] (γ : ↥(torsionSubgroup m)) :
    Hmat m ℤ *ᵥ (torsionLift m γ) = (4 : ℤ) • (Quotient.out γ.1) :=
  Classical.choose_spec (torsion_lift_exists m γ)

/-- The forward map: torsion element ↦ its lift reduced mod 4. -/
noncomputable def torsionToV4 (m : ℕ) [NeZero m] (γ : ↥(torsionSubgroup m)) : V4 m :=
  ⟨(Int.castRingHom (ZMod 4)) ∘ (torsionLift m γ), by
    funext i
    rw [← map_cast_mulVec_apply m 4 (torsionLift m γ) i, torsionLift_spec]
    show (((4 : ℤ) * (Quotient.out γ.1) i : ℤ) : ZMod 4) = 0
    rw [Int.cast_mul]
    have h4 : ((4 : ℤ) : ZMod 4) = 0 :=
      (ZMod.intCast_zmod_eq_zero_iff_dvd 4 4).mpr ⟨1, by norm_num⟩
    rw [h4, zero_mul]⟩

/-- The val-lift of a `V4` vector is divisible by 4 after applying `H`. -/
theorem v4_dvd (m : ℕ) [NeZero m] (v : V4 m) (i : ZMod m) :
    (4 : ℤ) ∣ (Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i := by
  have hcast : (Int.castRingHom (ZMod 4)) ∘ (fun j => ((v.1 j).val : ℤ)) = v.1 := by
    funext j
    show (((v.1 j).val : ℤ) : ZMod 4) = v.1 j
    rw [Int.cast_natCast, ZMod.natCast_val, ZMod.cast_id]
  have h0 : ((Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i : ZMod 4) = 0 := by
    rw [map_cast_mulVec_apply, hcast]
    exact congrFun v.2 i
  exact (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).mp h0

/-- Dividing the lifted `H`-image by 4 recovers the `H`-image of the val-lift. -/
theorem v4_lift_four (m : ℕ) [NeZero m] (v : V4 m) :
    (4 : ℤ) • (fun i => (Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i / 4)
      = Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ)) := by
  funext i
  show (4 : ℤ) * ((Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i / 4)
    = (Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i
  exact Int.mul_ediv_cancel' (v4_dvd m v i)

/-- The backward map: `V4` vector ↦ torsion element via the val-lift. -/
def v4ToTorsion (m : ℕ) [NeZero m] (v : V4 m) : ↥(torsionSubgroup m) :=
  ⟨Submodule.Quotient.mk (fun i => (Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i / 4),
    by
      have hmk : (Submodule.Quotient.mk ((4 : ℤ) • (fun i =>
          (Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i / 4)) : Vquot m) = 0 := by
        rw [Submodule.Quotient.mk_eq_zero]
        exact ⟨fun j => ((v.1 j).val : ℤ), by
          rw [Matrix.mulVecLin_apply, v4_lift_four]⟩
      exact hmk⟩

/-- Forward after backward is the identity on `V4`. -/
theorem torsionToV4_left_inv (m : ℕ) [NeZero m] (v : V4 m) :
    torsionToV4 m (v4ToTorsion m v) = v := by
  apply Subtype.ext
  funext i
  show ((torsionLift m (v4ToTorsion m v) i : ℤ) : ZMod 4) = v.1 i
  have hcasti : (((v.1 i).val : ℤ) : ZMod 4) = v.1 i := by
    rw [Int.cast_natCast, ZMod.natCast_val, ZMod.cast_id]
  have hmk : Submodule.Quotient.mk (Quotient.out (v4ToTorsion m v).1)
      = Submodule.Quotient.mk (fun i =>
        (Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i / 4) :=
    Quotient.out_eq (v4ToTorsion m v).1
  have huniq := torsion_t_mod4_unique m (Quotient.out (v4ToTorsion m v).1)
    (fun i => (Hmat m ℤ *ᵥ (fun j => ((v.1 j).val : ℤ))) i / 4)
    (torsionLift m (v4ToTorsion m v)) (fun j => ((v.1 j).val : ℤ))
    (torsionLift_spec m (v4ToTorsion m v)) (v4_lift_four m v).symm hmk
  rw [huniq i, hcasti]

/-- Backward after forward is the identity on torsion. -/
theorem torsionToV4_right_inv (m : ℕ) [NeZero m] (γ : ↥(torsionSubgroup m)) :
    v4ToTorsion m (torsionToV4 m γ) = γ := by
  apply Subtype.ext
  show Submodule.Quotient.mk (fun i =>
      (Hmat m ℤ *ᵥ (fun j => (((torsionToV4 m γ).1 j).val : ℤ))) i / 4) = γ.1
  have hF : ∀ j : ZMod m,
      (torsionToV4 m γ).1 j = ((torsionLift m γ j : ℤ) : ZMod 4) := fun j => rfl
  have hcast' : ∀ j : ZMod m,
      ((fun k => (((torsionToV4 m γ).1 k).val : ℤ)) j : ZMod 4)
        = ((torsionLift m γ j : ℤ) : ZMod 4) := by
    intro j
    show ((((torsionToV4 m γ).1 j).val : ℤ) : ZMod 4)
      = ((torsionLift m γ j : ℤ) : ZMod 4)
    rw [Int.cast_natCast, ZMod.natCast_val, ZMod.cast_id, hF]
  have hdvd' : ∀ j : ZMod m,
      (4 : ℤ) ∣ ((torsionToV4 m γ).1 j).val - torsionLift m γ j := by
    intro j
    exact (ZMod.intCast_eq_intCast_iff_dvd_sub _ _ _).mp (hcast' j).symm
  have hts : (fun j => (((torsionToV4 m γ).1 j).val : ℤ)) - torsionLift m γ
      = (4 : ℤ) • (fun j =>
        (((torsionToV4 m γ).1 j).val - torsionLift m γ j) / 4) := by
    funext j
    show ((torsionToV4 m γ).1 j).val - torsionLift m γ j
      = 4 * ((((torsionToV4 m γ).1 j).val - torsionLift m γ j) / 4)
    exact (Int.mul_ediv_cancel' (hdvd' j)).symm
  have hH : Hmat m ℤ *ᵥ ((fun j => (((torsionToV4 m γ).1 j).val : ℤ)) - torsionLift m γ)
      = (4 : ℤ) • (Hmat m ℤ *ᵥ (fun j =>
        (((torsionToV4 m γ).1 j).val - torsionLift m γ j) / 4)) := by
    rw [hts, Matrix.mulVec_smul]
  have hL : Hmat m ℤ *ᵥ (fun j => (((torsionToV4 m γ).1 j).val : ℤ))
      = (4 : ℤ) • (fun i =>
        (Hmat m ℤ *ᵥ (fun j => (((torsionToV4 m γ).1 j).val : ℤ))) i / 4) :=
    (v4_lift_four m (torsionToV4 m γ)).symm
  have hEq : (4 : ℤ) • (fun i =>
        (Hmat m ℤ *ᵥ (fun j => (((torsionToV4 m γ).1 j).val : ℤ))) i / 4)
      - (4 : ℤ) • (Quotient.out γ.1)
      = (4 : ℤ) • (Hmat m ℤ *ᵥ (fun j =>
        (((torsionToV4 m γ).1 j).val - torsionLift m γ j) / 4)) := by
    rw [← hL, ← torsionLift_spec, ← Matrix.mulVec_sub, hH]
  have hys : (fun i =>
        (Hmat m ℤ *ᵥ (fun j => (((torsionToV4 m γ).1 j).val : ℤ))) i / 4)
      - Quotient.out γ.1
      = Hmat m ℤ *ᵥ (fun j =>
        (((torsionToV4 m γ).1 j).val - torsionLift m γ j) / 4) := by
    funext j
    have hj : (4 : ℤ) *
        (fun i => (Hmat m ℤ *ᵥ (fun j => (((torsionToV4 m γ).1 j).val : ℤ))) i / 4) j
        - (4 : ℤ) * (Quotient.out γ.1) j
        = (4 : ℤ) * (Hmat m ℤ *ᵥ (fun j =>
          (((torsionToV4 m γ).1 j).val - torsionLift m γ j) / 4)) j :=
      congrFun hEq j
    have hj2 : (4 : ℤ) * ((fun i =>
        (Hmat m ℤ *ᵥ (fun j => (((torsionToV4 m γ).1 j).val : ℤ))) i / 4) j
        - (Quotient.out γ.1) j)
        = (4 : ℤ) * (Hmat m ℤ *ᵥ (fun j =>
          (((torsionToV4 m γ).1 j).val - torsionLift m γ j) / 4)) j := by
      linear_combination hj
    exact mul_left_cancel₀ (by norm_num : (4 : ℤ) ≠ 0) hj2
  have hout : (Submodule.Quotient.mk (Quotient.out γ.1) : Vquot m) = γ.1 :=
    Quotient.out_eq γ.1
  rw [← hout, Submodule.Quotient.eq]
  exact ⟨fun j => (((torsionToV4 m γ).1 j).val - torsionLift m γ j) / 4, by
    rw [Matrix.mulVecLin_apply]; exact hys.symm⟩

/-- The torsion subgroup has the same cardinality as `V4`. -/
theorem card_torsion_eq_card_V4 (m : ℕ) [NeZero m] :
    Fintype.card ↥(torsionSubgroup m) = Fintype.card (V4 m) :=
  Fintype.card_congr
    { toFun := torsionToV4 m
      invFun := v4ToTorsion m
      left_inv := torsionToV4_right_inv m
      right_inv := torsionToV4_left_inv m }

/-- The torsion summand is unchanged when `s` changes by an even amount
    (the source's "support independent of s" step, for torsion representatives). -/
theorem phiSummand_torsion_odd_eq (m : ℕ) [NeZero m] (s₁ s₂ : ℤ)
    (hodd1 : Odd s₁) (hodd2 : Odd s₂) (w : ZMod m → ℤ) (γ : ↥(torsionSubgroup m)) :
    phiSummand m s₁ w γ.1 = phiSummand m s₂ w γ.1 := by
  obtain ⟨z, hz⟩ := Quotient.exists_rep γ.1
  have h1 : γ.1 = Submodule.Quotient.mk z := hz.symm
  have ht0 : (4 : ℤ) • (Submodule.Quotient.mk z : Vquot m) = 0 := by
    rw [← h1]
    exact γ.2
  obtain ⟨t, ht⟩ := torsion_ht m z ht0
  have h4 : 4 * Qnum m z = Dm m * (t ⬝ᵥ z) := four_pairNum_eq m z z t ht
  obtain ⟨k₁, hk₁⟩ := hodd1
  obtain ⟨k₂, hk₂⟩ := hodd2
  rw [h1, phiSummand_mk, phiSummand_mk]
  apply eChar_eq_of_int_sub (k := (k₁ - k₂) * (t ⬝ᵥ z))
  have hD : ((Dm m : ℚ)) ≠ 0 := by exact_mod_cast ne_of_gt (Dm_pos m)
  have h4' : ((4 * Qnum m z : ℚ)) = (Dm m : ℚ) * (t ⬝ᵥ z) := by exact_mod_cast h4
  rw [div_sub_div_same, div_eq_iff hD]
  push_cast
  rw [hk₁, hk₂]
  push_cast
  linear_combination (k₁ - k₂ : ℚ) * h4'

/-- The modulus dichotomy for `phihat`, with the value identified as `|V4|/D`. -/
theorem phihat_modulus_values (m : ℕ) [NeZero m] (s : ℤ) (hs : IsCoprime s (Dm m))
    (w : ZMod m → ℤ) :
    phihat m s (Submodule.Quotient.mk w) * star (phihat m s (Submodule.Quotient.mk w))
      = ((Fintype.card (V4 m) : ℂ) / (Dm m : ℂ))
      ∨ phihat m s (Submodule.Quotient.mk w)
        * star (phihat m s (Submodule.Quotient.mk w)) = 0 := by
  rw [phihat_modulus m s hs w]
  rcases torsion_sum_values m s w with h | h
  · left
    rw [h, card_torsion_eq_card_V4, div_eq_mul_inv, mul_comm]
  · right
    rw [h, mul_zero]

/-- The support of `phihat` is the same for all odd `s` coprime to `D`
    (the source proves this for odd `s`; the boundary states it without
    the parity restriction — see the report for the scope note). -/
theorem phihat_support_odd_eq (m : ℕ) [NeZero m] (s₁ s₂ : ℤ)
    (hs1 : IsCoprime s₁ (Dm m)) (hs2 : IsCoprime s₂ (Dm m))
    (hodd1 : Odd s₁) (hodd2 : Odd s₂) (w : ZMod m → ℤ) :
    phihat m s₁ (Submodule.Quotient.mk w) = 0 ↔
      phihat m s₂ (Submodule.Quotient.mk w) = 0 := by
  have hmod : phihat m s₁ (Submodule.Quotient.mk w)
        * star (phihat m s₁ (Submodule.Quotient.mk w))
      = phihat m s₂ (Submodule.Quotient.mk w)
        * star (phihat m s₂ (Submodule.Quotient.mk w)) := by
    rw [phihat_modulus m s₁ hs1 w, phihat_modulus m s₂ hs2 w]
    congr 1
    apply Finset.sum_congr rfl
    intro γ _
    exact phiSummand_torsion_odd_eq m s₁ s₂ hodd1 hodd2 w γ
  constructor
  · intro h
    have h0 : phihat m s₂ (Submodule.Quotient.mk w)
        * star (phihat m s₂ (Submodule.Quotient.mk w)) = 0 := by
      rw [← hmod, h, zero_mul]
    rcases mul_eq_zero.mp h0 with h2 | h2
    · exact h2
    · exact star_eq_zero.mp h2
  · intro h
    have h0 : phihat m s₁ (Submodule.Quotient.mk w)
        * star (phihat m s₁ (Submodule.Quotient.mk w)) = 0 := by
      rw [hmod, h, zero_mul]
    rcases mul_eq_zero.mp h0 with h2 | h2
    · exact h2
    · exact star_eq_zero.mp h2

/-- The mod-2 reduction `ZMod 4 →+* ZMod 2`. -/
def phi42 : ZMod 4 →+* ZMod 2 := ZMod.castHom (by norm_num) (ZMod 2)

theorem phi42_one : phi42 1 = 1 := map_one _

theorem phi42_two : phi42 2 = 0 := by
  have h : (2 : ZMod 4) = 1 + 1 := by decide
  rw [h, map_add, map_one]
  decide

theorem phi42_three : phi42 3 = 1 := by
  have h : (3 : ZMod 4) = 2 + 1 := by decide
  rw [h, map_add, phi42_two, map_one]
  simp

/-- Case enumeration on `ZMod 4` (tiny decide, 4 elements). -/
theorem zmod4_cases : ∀ x : ZMod 4, x = 0 ∨ x = 1 ∨ x = 2 ∨ x = 3 := by decide

/-- In `ZMod 4`, `2 * x = 0` forces `x ∈ {0, 2}`. -/
theorem zmod4_two_mul_eq_zero (x : ZMod 4) (hx : 2 * x = 0) : x = 0 ∨ x = 2 := by
  rcases zmod4_cases x with rfl | rfl | rfl | rfl
  · exact Or.inl rfl
  · exact absurd hx (by decide)
  · exact Or.inr rfl
  · exact absurd hx (by decide)

/-- The kernel of `phi42` is contained in the multiples of 2. -/
theorem phi42_eq_zero_two_mul (x : ZMod 4) (hx : phi42 x = 0) : 2 * x = 0 := by
  rcases zmod4_cases x with rfl | rfl | rfl | rfl
  · simp
  · rw [phi42_one] at hx
    exact absurd hx one_ne_zero
  · decide
  · rw [phi42_three] at hx
    exact absurd hx one_ne_zero

/-- Equal mod-2 images give equal doubles in `ZMod 4`. -/
theorem two_mul_eq_of_phi42_eq (a b : ZMod 4) (h : phi42 a = phi42 b) : 2 * a = 2 * b := by
  have h0 : phi42 (a - b) = 0 := by rw [map_sub, h, sub_self]
  have h1 : 2 * (a - b) = 0 := phi42_eq_zero_two_mul _ h0
  have h2 : 2 * a - 2 * b = 0 := by linear_combination h1
  exact sub_eq_zero.mp h2

/-- Kernel elements of `phi42` are doubles. -/
theorem exists_two_mul_of_phi42_eq_zero (x : ZMod 4) (hx : phi42 x = 0) :
    ∃ w : ZMod 4, x = 2 * w := by
  rcases zmod4_cases x with rfl | rfl | rfl | rfl
  · exact ⟨0, by simp⟩
  · rw [phi42_one] at hx
    exact absurd hx one_ne_zero
  · exact ⟨1, by simp⟩
  · rw [phi42_three] at hx
    exact absurd hx one_ne_zero

/-- A `ZMod 2`-valued function on `ZMod 7` with the two-step recurrence
    `u (i+1) = u (i-1)` is constant: `i ↦ i+2` generates `ZMod 7`. -/
theorem eq_of_step_two (u : ZMod 7 → ZMod 2)
    (h : ∀ i : ZMod 7, u (i + 1) = u (i - 1)) : ∀ i : ZMod 7, u i = u 0 := by
  have h2 : ∀ j : ZMod 7, u (j + 2) = u j := by
    intro j
    have hj := h (j + 1)
    rwa [show j + 1 + 1 = j + 2 from by ring, show j + 1 - 1 = j from by ring] at hj
  have hk : ∀ k : ℕ, u ((2 * k : ℕ) : ZMod 7) = u 0 := by
    intro k
    induction k with
    | zero => simp
    | succ k ih =>
      have hcast : ((2 * (k + 1) : ℕ) : ZMod 7) = ((2 * k : ℕ) : ZMod 7) + 2 := by
        push_cast
        ring
      rw [hcast, h2, ih]
  intro i
  have hmod : 2 * ((i.val * 4) % 7) ≡ i.val [MOD 7] := by
    have h1 : (i.val * 4) % 7 ≡ i.val * 4 [MOD 7] := Nat.mod_modEq _ _
    have h2' : 2 * ((i.val * 4) % 7) ≡ 2 * (i.val * 4) [MOD 7] :=
      Nat.ModEq.mul (Nat.ModEq.refl 2) h1
    have h3 : 2 * (i.val * 4) ≡ i.val [MOD 7] := by
      rw [show 2 * (i.val * 4) = i.val + 7 * i.val from by ring]
      exact ((Nat.modEq_iff_dvd' (by omega : i.val ≤ i.val + 7 * i.val)).mpr
        ⟨i.val, by omega⟩).symm
    exact h2'.trans h3
  have hi : ((2 * ((i.val * 4) % 7) : ℕ) : ZMod 7) = i := by
    have h2'' : ((2 * ((i.val * 4) % 7) : ℕ) : ZMod 7) = ((i.val : ℕ) : ZMod 7) :=
      (ZMod.natCast_eq_natCast_iff _ _ _).mpr hmod
    rw [h2'', ZMod.natCast_val, ZMod.cast_id]
  rw [← hi]
  exact hk _

/-- The pointwise recurrence for a plain vector in the `V4 7` kernel
    (stated for a plain vector: rewriting the matrix next to `↑v` would
    hit the dependent-rewrite trap, since `V4 7` is defined via the matrix). -/
theorem v4Seven_rec_aux (y : ZMod 7 → ZMod 4)
    (hy : (Hmat 7 ℤ).map (Int.castRingHom (ZMod 4)) *ᵥ y = 0) (i : ZMod 7) :
    6 * y i - y (i + 1) - y (i - 1) = 0 := by
  have h0 := congrFun hy i
  rw [Hmat_map_zmod, Hmat_mulVec_apply] at h0
  exact h0

/-- The pointwise recurrence for a `V4 7` vector. -/
theorem v4Seven_rec (v : V4 7) (i : ZMod 7) :
    6 * v.1 i - v.1 (i + 1) - v.1 (i - 1) = 0 :=
  v4Seven_rec_aux v.1 v.2 i

/-- Every `V4 7` vector is constant: the two-step parity argument.
    Mod 2, the recurrence gives `u (i+1) = u (i-1)`, so all components
    agree mod 2; lifting the difference by 2 and repeating gives
    agreement of the doubles, hence equality in `ZMod 4`. -/
theorem v4Seven_const (v : V4 7) (i : ZMod 7) : v.1 i = v.1 0 := by
  have h6 : (6 : ZMod 4) = 2 := by decide
  have hneg : ∀ x : ZMod 2, -x = x := by decide
  -- Step 1: `phi42 ∘ v.1` satisfies the two-step recurrence.
  have hstep1 : ∀ j : ZMod 7, phi42 (v.1 (j + 1)) = phi42 (v.1 (j - 1)) := by
    intro j
    have hrec := v4Seven_rec v j
    rw [h6] at hrec
    have hsum : v.1 (j + 1) + v.1 (j - 1) = 2 * v.1 j := by linear_combination -hrec
    have hφ : phi42 (v.1 (j + 1)) + phi42 (v.1 (j - 1)) = 0 := by
      have h1 : phi42 (v.1 (j + 1) + v.1 (j - 1)) = phi42 (2 * v.1 j) := by rw [hsum]
      rw [map_add, map_mul, phi42_two, zero_mul] at h1
      exact h1
    have h2 : phi42 (v.1 (j + 1)) = -phi42 (v.1 (j - 1)) :=
      eq_neg_of_add_eq_zero_left hφ
    rw [h2, hneg]
  have hconst1 : ∀ j : ZMod 7, phi42 (v.1 j) = phi42 (v.1 0) := by
    have h := eq_of_step_two (phi42 ∘ v.1) (by intro j; exact hstep1 j)
    simpa only [Function.comp_apply] using h
  -- Step 2: lift the difference by 2.
  have hlift : ∀ j : ZMod 7, ∃ w : ZMod 4, v.1 j - v.1 0 = 2 * w := by
    intro j
    apply exists_two_mul_of_phi42_eq_zero
    rw [map_sub, hconst1 j, sub_self]
  choose w hw using hlift
  have hv : ∀ j : ZMod 7, v.1 j = v.1 0 + 2 * w j := by
    intro j
    linear_combination hw j
  -- Step 3: `phi42 ∘ w` satisfies the two-step recurrence.
  have hstep3 : ∀ j : ZMod 7, phi42 (w (j + 1)) = phi42 (w (j - 1)) := by
    intro j
    have hrec := v4Seven_rec v j
    rw [hv j, hv (j + 1), hv (j - 1), h6] at hrec
    have hX : 2 * (2 * w j - w (j + 1) - w (j - 1)) = 0 := by
      linear_combination hrec
    have hφX : phi42 (2 * w j - w (j + 1) - w (j - 1)) = 0 := by
      rcases zmod4_two_mul_eq_zero _ hX with h | h
      · rw [h]
        exact map_zero _
      · rw [h]
        exact phi42_two
    rw [map_sub, map_sub, map_mul, phi42_two, zero_mul, zero_sub] at hφX
    have hsum : phi42 (w (j + 1)) + phi42 (w (j - 1)) = 0 := by
      have h := hφX
      rw [sub_eq_add_neg, ← neg_add] at h
      exact neg_eq_zero.mp h
    have h2 : phi42 (w (j + 1)) = -phi42 (w (j - 1)) :=
      eq_neg_of_add_eq_zero_left hsum
    rw [h2, hneg]
  have hconst3 : ∀ j : ZMod 7, phi42 (w j) = phi42 (w 0) := by
    have h := eq_of_step_two (phi42 ∘ w) (by intro j; exact hstep3 j)
    simpa only [Function.comp_apply] using h
  -- Conclusion: the doubles agree, and the double at 0 vanishes.
  have h2w : 2 * w i = 2 * w 0 := two_mul_eq_of_phi42_eq _ _ (hconst3 i)
  have hw0 : 2 * w 0 = 0 := by
    have h := hw 0
    rw [sub_self] at h
    exact h.symm
  rw [hv i, h2w, hw0, add_zero]

/-- `V4 7` is the type of constant vectors, hence equivalent to `ZMod 4`. -/
def v4SevenEquiv : V4 7 ≃ ZMod 4 where
  toFun v := v.1 0
  invFun c := ⟨Function.const _ c, by
    funext i
    rw [Hmat_map_zmod, Hmat_mulVec_apply]
    show (6 : ZMod 4) * c - c - c = 0
    rw [show (6 : ZMod 4) = 2 from by decide]
    ring⟩
  left_inv v := by
    apply Subtype.ext
    funext i
    show v.1 0 = v.1 i
    exact (v4Seven_const v i).symm
  right_inv c := rfl

/-- `|V4|` at `m = 7`, structurally: the kernel is the constants (no kernel decide). -/
theorem V4_card7 : Fintype.card (V4 7) = 4 := by
  haveI : NeZero (4 : ℕ) := ⟨by norm_num⟩
  have h := Fintype.card_congr v4SevenEquiv
  rw [h]
  exact ZMod.card 4

/-- `D_eff` at `m = 7`, structurally: `D_7 = 228484` (trace formula) over `|V4| = 4`. -/
theorem Deff_seven : Deff 7 = 57121 := by
  show Dm 7 / (Fintype.card (V4 7) : ℤ) = 57121
  rw [Dm_seven, V4_card7]
  norm_num

/-- The full `D_eff` table of boundary 151: 49, 72, 1681, 4900, 57121. -/
theorem Deff_table_full :
    Deff 3 = 49 ∧ Deff 4 = 72 ∧ Deff 5 = 1681 ∧ Deff 6 = 4900 ∧ Deff 7 = 57121 := by
  refine ⟨?_, ?_, ?_, ?_, Deff_seven⟩ <;>
    simp only [Deff, Dm_table3, Dm_table4, Dm_table5, Dm_table6,
      V4_card3, V4_card4, V4_card5, V4_card6] <;> norm_num

/-- The modulus dichotomy for `phihat` at an arbitrary quotient point. -/
theorem phihat_modulus_values_all (m : ℕ) [NeZero m] (s : ℤ) (hs : IsCoprime s (Dm m))
    (q : Vquot m) :
    phihat m s q * star (phihat m s q) = ((Fintype.card (V4 m) : ℂ) / (Dm m : ℂ))
      ∨ phihat m s q * star (phihat m s q) = 0 := by
  induction q using Quotient.inductionOn with
  | _ w =>
    change phihat m s (Submodule.Quotient.mk w) * star (phihat m s (Submodule.Quotient.mk w))
        = ((Fintype.card (V4 m) : ℂ) / (Dm m : ℂ))
        ∨ phihat m s (Submodule.Quotient.mk w)
          * star (phihat m s (Submodule.Quotient.mk w)) = 0
    exact phihat_modulus_values m s hs w

/-- The support dichotomy for `phihat` at an arbitrary quotient point. -/
theorem phihat_support_odd_eq_all (m : ℕ) [NeZero m] (s₁ s₂ : ℤ)
    (hs1 : IsCoprime s₁ (Dm m)) (hs2 : IsCoprime s₂ (Dm m))
    (hodd1 : Odd s₁) (hodd2 : Odd s₂) (q : Vquot m) :
    phihat m s₁ q = 0 ↔ phihat m s₂ q = 0 := by
  induction q using Quotient.inductionOn with
  | _ w =>
    change phihat m s₁ (Submodule.Quotient.mk w) = 0 ↔
      phihat m s₂ (Submodule.Quotient.mk w) = 0
    exact phihat_support_odd_eq m s₁ s₂ hs1 hs2 hodd1 hodd2 w

/-- The concrete weights `phihat_s` transported to `Fix m` along `fixEquivQuot`. -/
noncomputable def phihatFix (m : ℕ) [NeZero m] (s : ℤ) (ξ : Fix m) : ℂ :=
  phihat m s (fixEquivQuot m ξ)

/-- The modulus dichotomy for the weights on `Fix m`. -/
theorem phihatFix_modulus_values (m : ℕ) [NeZero m] (s : ℤ) (hs : IsCoprime s (Dm m))
    (ξ : Fix m) :
    phihatFix m s ξ * star (phihatFix m s ξ) = ((Fintype.card (V4 m) : ℂ) / (Dm m : ℂ))
      ∨ phihatFix m s ξ * star (phihatFix m s ξ) = 0 :=
  phihat_modulus_values_all m s hs (fixEquivQuot m ξ)

/-- The support of the weights on `Fix m` is the same for odd `s` coprime to `D`. -/
theorem phihatFix_support_odd_eq (m : ℕ) [NeZero m] (s₁ s₂ : ℤ)
    (hs1 : IsCoprime s₁ (Dm m)) (hs2 : IsCoprime s₂ (Dm m))
    (hodd1 : Odd s₁) (hodd2 : Odd s₂) (ξ : Fix m) :
    phihatFix m s₁ ξ = 0 ↔ phihatFix m s₂ ξ = 0 :=
  phihat_support_odd_eq_all m s₁ s₂ hs1 hs2 hodd1 hodd2 (fixEquivQuot m ξ)

/-- The pair sum with complex mode sums (the boundary's `S_k(ξ)` are complex,
    while the block's `PsiPair` takes real `S`). -/
noncomputable def PsiPairC (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (φ : ℤ → Fix m → ℂ) (S : Fix m → K → ℂ) (ω : K → ℂ → ℂ) (η : ℂ)
    (s : ℤ) : ℂ :=
  ∑ ξ : Fix m, ∑ ξ' : Fix m,
    φ s ξ * star (φ s ξ') * ∏ k, ω k (η * (S ξ k - S ξ' k))

/-- Assembly (5): the boundary pair sum with the concrete weights `phihatFix`
    is `PsiPairC` with those weights, by definition. The identification of
    the boundary's torus `Fix_m` with the block's finite `Fix m` is the
    block's finite model itself (via `fixEquivQuot`); the torus↔finite
    identification as such is not formalized here. -/
theorem psiPairC_phihat (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (S : Fix m → K → ℂ) (ω : K → ℂ → ℂ) (η : ℂ) (s : ℤ) :
    PsiPairC m (phihatFix m) S ω η s
      = ∑ ξ : Fix m, ∑ ξ' : Fix m,
        phihatFix m s ξ * star (phihatFix m s ξ')
          * ∏ k, ω k (η * (S ξ k - S ξ' k)) :=
  rfl

/-- Assembly (5) for the block's own `PsiPair`: plugging the concrete
    weights `phihatFix` into the block's pair sum gives the boundary sum. -/
theorem psiPair_phihat (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (S : Fix m → K → ℝ) (ω : K → ℝ → ℂ) (η : ℝ) (s : ℤ) :
    PsiPair m (phihatFix m) S ω η s
      = ∑ ξ : Fix m, ∑ ξ' : Fix m,
        phihatFix m s ξ * star (phihatFix m s ξ')
          * ∏ k, ω k (η * (S ξ k - S ξ' k)) :=
  rfl

/-- `PsiPairC` with real mode sums cast to `ℂ` is the block's `PsiPair`. -/
theorem psiPairC_real (m : ℕ) [NeZero m] {K : Type*} [Fintype K]
    (φ : ℤ → Fix m → ℂ) (S : Fix m → K → ℝ) (ω : K → ℝ → ℂ) (η : ℝ) (s : ℤ) :
    PsiPairC m φ (fun ξ k => ((S ξ k : ℝ) : ℂ)) (fun k z => ω k z.re) ((η : ℝ) : ℂ) s
      = PsiPair m φ S ω η s := by
  unfold PsiPairC PsiPair
  apply Finset.sum_congr rfl
  intro ξ _
  apply Finset.sum_congr rfl
  intro ξ' _
  congr 1
  apply Finset.prod_congr rfl
  intro k _
  show ω k (((η : ℂ) * (((S ξ k : ℝ) : ℂ) - ((S ξ' k : ℝ) : ℂ))).re)
    = ω k (η * (S ξ k - S ξ' k))
  congr 1
  rw [← Complex.ofReal_sub, ← Complex.ofReal_mul, Complex.ofReal_re]

#print axioms gammaMulAction
#print axioms card_Fix
#print axioms fixEquivQuot
#print axioms det_formula
#print axioms det_eq_trace_sub_two
#print axioms trace_Smat_pow
#print axioms Dm_seven
#print axioms V4_card7
#print axioms Deff_seven
#print axioms Deff_table_full
#print axioms phihat_modulus
#print axioms phihat_modulus_values
#print axioms phihat_support_odd_eq
#print axioms phihatFix_modulus_values
#print axioms phihatFix_support_odd_eq
#print axioms torsion_sum_values
#print axioms card_torsion_eq_card_V4
#print axioms psiPairC_phihat
#print axioms psiPair_phihat
#print axioms psiPairC_real

end OrbitPairFull
end LineD
end Bgs
