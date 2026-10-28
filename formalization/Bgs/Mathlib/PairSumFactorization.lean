module
public import Mathlib
@[expose] public section

/-!
# Inverse-row pair-sum factorization (Cayley arithmetic, Theorems 1, 2 and 4)

Source: `mathematics/cayley-arithmetic/cayley_inverse_pair_sum_factorization.md`, §§2–3, 5.

Let `R` be a commutative ring and `F(X) = ∏_i (X - x_i)` a monic split polynomial of
degree `m` (`pairPoly`).  Put

* `D_F(Z) = ∏_i (Z - 2 x_i)` (`doublePoly`), which equals `2^m F(Z/2)` in the coefficient
  sense of (4): `D_F = scaleRoots F 2` (`doublePoly_eq_scaleRoots`, `doublePoly_coeff`);
* `S_F(Z) = ∏_{i<j} (Z - x_i - x_j)` (`pairSumPoly`), monic of degree `binom(m,2)`
  (`pairSumPoly_monic`, `natDegree_pairSumPoly`).

Formalized here:

* **Theorem 1** (`pair_sum_resultant_factorization`): for every `z ∈ R`,
  `Res_X(F(X), F(z - X)) = D_F(z) · S_F(z)²`; the root-level identity behind it is
  `prod_pairs_eq_diag_mul_sq` / `resultant_reflect_eq_prod`.  The polynomial identity (6)
  in `R[Z]` is the instance `R ↦ R[Z]`, `z ↦ Z` (`pair_sum_resultant_factorization_poly`).
* **Theorem 2** (`rootMultiplicity_zero_D_mul_sq`, `pair_sum_order_three_iff`): over a field,
  if `D(0) ≠ 0` and `S ≠ 0`, the order of zero of `D S²` at `0` is `2 ord_0 S`; it is
  therefore even, and `≥ 3 ⇔ ≥ 4 ⇔ s_0 = s_1 = 0`.
* **Theorem 4, ingredients (17)–(18), (21)**: for `F = E(X²) + X O(X²)`,
  `F(-r) = F(r) - 2 r O(r²)` (`parity_eval_neg`); `∏ x_i = (-1)^m E(0)` (`prod_roots_eq`);
  and `s_0² = ∏_i O(x_i²)` (`pair_sum_const_sq`) over a domain where `2 ≠ 0`, `F(0) ≠ 0`.

Boundary: the general (non-split) case uses symmetric-function integrality and is covered by
specialising from a splitting extension; the half-degree resultant identities (20), (23) are
not formalized.
-/

open Polynomial Finset

namespace Bgs.Mathlib

variable {R : Type*} [CommRing R]

/-- `F(X) = ∏_i (X - x_i)`. -/
noncomputable def pairPoly {m : ℕ} (x : Fin m → R) : R[X] := ∏ i, (X - C (x i))

/-- `D_F(Z) = ∏_i (Z - 2 x_i)`. -/
noncomputable def doublePoly {m : ℕ} (x : Fin m → R) : R[X] := ∏ i, (X - C (2 * x i))

/-- `S_F(Z) = ∏_{i<j} (Z - x_i - x_j)`, the pair-sum polynomial. -/
noncomputable def pairSumPoly {m : ℕ} (x : Fin m → R) : R[X] :=
  ∏ i, ∏ j ∈ Ioi i, (X - C (x i + x j))

lemma pairPoly_monic {m : ℕ} (x : Fin m → R) : (pairPoly x).Monic :=
  monic_prod_of_monic _ _ fun _ _ => monic_X_sub_C _

lemma pairSumPoly_monic {m : ℕ} (x : Fin m → R) : (pairSumPoly x).Monic :=
  monic_prod_of_monic _ _ fun _ _ => monic_prod_of_monic _ _ fun _ _ => monic_X_sub_C _

lemma natDegree_pairPoly [Nontrivial R] {m : ℕ} (x : Fin m → R) :
    (pairPoly x).natDegree = m := by
  rw [pairPoly, natDegree_prod_of_monic _ _ fun i _ => monic_X_sub_C _]
  simp

/-- `S_F` is monic of degree `binom(m, 2)`. -/
theorem natDegree_pairSumPoly [Nontrivial R] {m : ℕ} (x : Fin m → R) :
    (pairSumPoly x).natDegree = m.choose 2 := by
  rw [pairSumPoly, natDegree_prod_of_monic _ _ fun _ _ =>
    monic_prod_of_monic _ _ fun _ _ => monic_X_sub_C _]
  have h : ∀ i : Fin m, (∏ j ∈ Ioi i, (X - C (x i + x j))).natDegree = m - 1 - i := by
    intro i
    rw [natDegree_prod_of_monic _ _ fun _ _ => monic_X_sub_C _]
    simp only [natDegree_X_sub_C, sum_const, smul_eq_mul, mul_one, Fin.card_Ioi]
  simp_rw [h]
  rw [Fin.sum_univ_eq_sum_range (fun i => m - 1 - i) m]
  rw [Finset.sum_range_reflect (fun i => i) m, Finset.sum_range_id, Nat.choose_two_right]

lemma eval_pairPoly {m : ℕ} (x : Fin m → R) (r : R) :
    (pairPoly x).eval r = ∏ i, (r - x i) := by
  simp [pairPoly, eval_prod]

/-- Splitting a product over ordered pairs of a symmetric function into the diagonal and
twice the strictly upper triangle. -/
theorem prod_pairs_eq_diag_mul_sq {m : ℕ} (a : Fin m → Fin m → R)
    (hsym : ∀ i j, a i j = a j i) :
    ∏ i, ∏ j, a i j = (∏ i, a i i) * (∏ i, ∏ j ∈ Ioi i, a i j) ^ 2 := by
  have hsplit : ∀ i : Fin m, ∏ j, a i j =
      a i i * (∏ j ∈ Ioi i, a i j) * ∏ j ∈ Iio i, a i j := by
    intro i
    have hu : (univ : Finset (Fin m)) = insert i (Ioi i ∪ Iio i) := by
      ext j; simp only [mem_univ, mem_insert, mem_union, mem_Ioi, mem_Iio, true_iff]
      rcases lt_trichotomy i j with h | h | h
      · exact Or.inr (Or.inl h)
      · exact Or.inl h.symm
      · exact Or.inr (Or.inr h)
    have hdisj : Disjoint (Ioi i) (Iio i) := by
      rw [Finset.disjoint_left]; intro j h1 h2
      simp only [mem_Ioi, mem_Iio] at h1 h2; exact absurd (h1.trans h2) (lt_irrefl _)
    have hni : i ∉ Ioi i ∪ Iio i := by simp
    rw [hu, prod_insert hni, prod_union hdisj, mul_assoc]
  have htri : ∏ i, ∏ j ∈ Iio i, a i j = ∏ i, ∏ j ∈ Ioi i, a i j := by
    rw [Finset.prod_comm' (t' := univ) (s' := fun j => Ioi j) (by intro i j; simp)]
    exact Finset.prod_congr rfl fun j _ => Finset.prod_congr rfl fun i _ => hsym i j
  rw [Finset.prod_congr rfl fun i _ => hsplit i, prod_mul_distrib, prod_mul_distrib, htri]
  ring

/-- `Res_X(F(X), G) = ∏_i G(x_i)` for the split monic `F` and any `G` of degree `≤ n`. -/
theorem resultant_pairPoly_left [Nontrivial R] {m : ℕ} (x : Fin m → R) (G : R[X]) (n : ℕ)
    (hG : G.natDegree ≤ n) :
    (pairPoly x).resultant G m n = ∏ i, G.eval (x i) := by
  have h := resultant_prod_left (univ : Finset (Fin m)) (fun i => X - C (x i)) G n
    (by simp) hG
  rw [← pairPoly, natDegree_pairPoly] at h
  rw [h]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [natDegree_X_sub_C, resultant_X_sub_C_left _ _ _ hG]

lemma natDegree_reflect_le [Nontrivial R] {m : ℕ} (x : Fin m → R) (z : R) :
    ((pairPoly x).comp (C z - X)).natDegree ≤ m := by
  calc ((pairPoly x).comp (C z - X)).natDegree
      ≤ (pairPoly x).natDegree * (C z - X).natDegree := natDegree_comp_le
    _ ≤ m * 1 := by
        rw [natDegree_pairPoly]
        gcongr
        exact (natDegree_sub_le _ _).trans (by simp)
    _ = m := mul_one m

/-- `Res_X(F(X), F(z - X)) = ∏_{i,j} (z - x_i - x_j)`  (equation (7)). -/
theorem resultant_reflect_eq_prod [Nontrivial R] {m : ℕ} (x : Fin m → R) (z : R) :
    (pairPoly x).resultant ((pairPoly x).comp (C z - X)) m m =
      ∏ i, ∏ j, (z - x i - x j) := by
  rw [resultant_pairPoly_left x _ m (natDegree_reflect_le x z)]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [eval_comp, eval_pairPoly]
  simp [sub_sub]

/-- **Theorem 1 (pair-sum factorization).**
`Res_X(F(X), F(z - X)) = D_F(z) · S_F(z)²` for every commutative ring `R` and `z ∈ R`. -/
theorem pair_sum_resultant_factorization [Nontrivial R] {m : ℕ} (x : Fin m → R) (z : R) :
    (pairPoly x).resultant ((pairPoly x).comp (C z - X)) m m =
      (doublePoly x).eval z * ((pairSumPoly x).eval z) ^ 2 := by
  rw [resultant_reflect_eq_prod, prod_pairs_eq_diag_mul_sq _ (fun i j => by ring)]
  simp only [doublePoly, pairSumPoly, eval_prod, eval_sub, eval_X, eval_C]
  congr 1
  · exact Finset.prod_congr rfl fun i _ => by ring
  · congr 1
    exact Finset.prod_congr rfl fun i _ => Finset.prod_congr rfl fun j _ => by ring

/-- **Theorem 1, polynomial form (6).**  In `R[Z]`:
`Res_X(F(X), F(Z - X)) = D_F(Z) · S_F(Z)²`, with `F` regarded over `R[Z]`. -/
theorem pair_sum_resultant_factorization_poly [Nontrivial R] {m : ℕ} (x : Fin m → R) :
    (pairPoly (fun i => C (x i))).resultant
        ((pairPoly (fun i => C (x i))).comp (C X - X)) m m =
      doublePoly x * (pairSumPoly x) ^ 2 := by
  rw [resultant_reflect_eq_prod, prod_pairs_eq_diag_mul_sq _ (fun i j => by ring)]
  simp only [doublePoly, pairSumPoly]
  congr 1
  · exact Finset.prod_congr rfl fun i _ => by
      rw [show (2 : R) * x i = x i + x i by ring, C_add]; ring
  · congr 1
    exact Finset.prod_congr rfl fun i _ => Finset.prod_congr rfl fun j _ => by
      rw [C_add]; ring

/-- `D_F = 2^m F(Z/2)` in the coefficient sense: `D_F` is `F` with roots scaled by `2`. -/
theorem doublePoly_eq_scaleRoots [Nontrivial R] {m : ℕ} (x : Fin m → R) :
    doublePoly x = (pairPoly x).scaleRoots 2 := by
  have key : ∀ s : Finset (Fin m),
      (∏ i ∈ s, (X - C (x i))).scaleRoots 2 = ∏ i ∈ s, (X - C (2 * x i)) := by
    intro s
    induction s using Finset.induction with
    | empty => simp
    | insert a s has ih =>
      rw [prod_insert has, prod_insert has, mul_scaleRoots', ih, X_sub_C_scaleRoots,
        mul_comm (x a)]
      rw [(monic_X_sub_C _).leadingCoeff, (monic_prod_of_monic _ _ fun i _ =>
        monic_X_sub_C _).leadingCoeff]
      simp
  rw [doublePoly, pairPoly, key]

/-- **Equation (4).** `D_F(Z) = ∑_j 2^{m-j} f_j Z^j`: the `j`-th coefficient of `D_F` is
`2^{m-j} f_j`. -/
theorem doublePoly_coeff [Nontrivial R] {m : ℕ} (x : Fin m → R) (j : ℕ) :
    (doublePoly x).coeff j = 2 ^ (m - j) * (pairPoly x).coeff j := by
  rw [doublePoly_eq_scaleRoots, coeff_scaleRoots, natDegree_pairPoly, mul_comm]

/-! ## Theorem 2: the zero-order identity -/

section ZeroOrder

variable {K : Type*} [Field K]

/-- **Theorem 2 (pair-sum zero-order identity).**  If `D(0) ≠ 0` and `S ≠ 0` then
`ord_{Z=0}(D S²) = 2 ord_{Z=0} S`. -/
theorem rootMultiplicity_zero_D_mul_sq (D S : K[X]) (hD : D.eval 0 ≠ 0) (hS : S ≠ 0) :
    (D * S ^ 2).rootMultiplicity 0 = 2 * S.rootMultiplicity 0 := by
  have hD0 : D ≠ 0 := by rintro rfl; simp at hD
  rw [rootMultiplicity_mul (mul_ne_zero hD0 (pow_ne_zero 2 hS)),
    rootMultiplicity_eq_zero (by simpa [IsRoot] using hD), zero_add]
  rw [show S ^ 2 = S * S by ring, rootMultiplicity_mul (mul_ne_zero hS hS)]
  ring

/-- `ord_0 S ≥ 2 ⇔ s_0 = s_1 = 0`. -/
lemma two_le_rootMultiplicity_zero_iff (S : K[X]) (hS : S ≠ 0) :
    2 ≤ S.rootMultiplicity 0 ↔ S.coeff 0 = 0 ∧ S.coeff 1 = 0 := by
  rw [le_rootMultiplicity_iff hS, map_zero, sub_zero, X_pow_dvd_iff]
  constructor
  · intro h; exact ⟨h 0 (by norm_num), h 1 (by norm_num)⟩
  · rintro ⟨h0, h1⟩ d hd
    interval_cases d
    · exact h0
    · exact h1

/-- **Theorem 2, consequence (10).**  With `D(0) ≠ 0` the order `I = ord_0(D S²)` is even,
and `I ≥ 3 ⇔ I ≥ 4 ⇔ s_0 = s_1 = 0`. -/
theorem pair_sum_order_three_iff (D S : K[X]) (hD : D.eval 0 ≠ 0) (hS : S ≠ 0) :
    Even ((D * S ^ 2).rootMultiplicity 0) ∧
    (3 ≤ (D * S ^ 2).rootMultiplicity 0 ↔ 4 ≤ (D * S ^ 2).rootMultiplicity 0) ∧
    (3 ≤ (D * S ^ 2).rootMultiplicity 0 ↔ S.coeff 0 = 0 ∧ S.coeff 1 = 0) := by
  rw [rootMultiplicity_zero_D_mul_sq D S hD hS, ← two_le_rootMultiplicity_zero_iff S hS]
  refine ⟨even_two_mul _, by omega, by omega⟩

end ZeroOrder

/-! ## Theorem 4: the constant pair-sum coefficient -/

/-- **(17), parity step.**  For `F = E(X²) + X O(X²)`: `F(-r) = F(r) - 2 r O(r²)`. -/
theorem parity_eval_neg (E O : R[X]) (r : R) :
    (E.comp (X ^ 2) + X * O.comp (X ^ 2)).eval (-r) =
      (E.comp (X ^ 2) + X * O.comp (X ^ 2)).eval r - 2 * r * O.eval (r ^ 2) := by
  simp only [eval_add, eval_mul, eval_comp, eval_pow, eval_X, neg_sq]
  ring

/-- **(18).**  For the monic split `F`, `∏ x_i = (-1)^m F(0)`. -/
theorem prod_roots_eq {m : ℕ} (x : Fin m → R) :
    ∏ i, x i = (-1) ^ m * (pairPoly x).eval 0 := by
  rw [eval_pairPoly]
  simp only [zero_sub, prod_neg, card_univ, Fintype.card_fin]
  rw [← mul_assoc, ← pow_add, ← two_mul, pow_mul]
  simp

/-- **Theorem 4, root form (14)/(21).**  Let `R` be a domain with `2 ≠ 0`, let
`F = ∏ (X - x_i) = E(X²) + X O(X²)` with `F(0) ≠ 0`.  Then the constant pair-sum coefficient
`s_0 = S_F(0)` satisfies `s_0² = ∏_i O(x_i²)` (which is `Res_X(F, O(X²))`). -/
theorem pair_sum_const_sq [IsDomain R] {m : ℕ} (x : Fin m → R) (E O : R[X])
    (hF : pairPoly x = E.comp (X ^ 2) + X * O.comp (X ^ 2)) (h2 : (2 : R) ≠ 0)
    (h0 : (pairPoly x).eval 0 ≠ 0) :
    ((pairSumPoly x).eval 0) ^ 2 = ∏ i, O.eval (x i ^ 2) := by
  have hxi : ∀ i, x i ≠ 0 := by
    intro i hi
    apply h0
    rw [eval_pairPoly]
    exact Finset.prod_eq_zero (mem_univ i) (by simp [hi])
  -- `∏_{i,j} (0 - x_i - x_j)` computed two ways
  have hA := prod_pairs_eq_diag_mul_sq (fun i j => (0 : R) - x i - x j) (fun i j => by ring)
  have hB : ∏ i, ∏ j, ((0 : R) - x i - x j) = ∏ i, (-(2 * x i) * O.eval (x i ^ 2)) := by
    refine Finset.prod_congr rfl fun i _ => ?_
    have hroot : (pairPoly x).eval (x i) = 0 := by
      rw [eval_pairPoly]; exact Finset.prod_eq_zero (mem_univ i) (sub_self _)
    have h1 : (pairPoly x).eval (-x i) = ∏ j, ((0 : R) - x i - x j) := by
      rw [eval_pairPoly]; exact Finset.prod_congr rfl fun j _ => by ring
    rw [← h1, hF, parity_eval_neg, ← hF, hroot]
    ring
  have hdiag : ∏ i, ((0 : R) - x i - x i) = ∏ i, (-(2 * x i)) :=
    Finset.prod_congr rfl fun i _ => by ring
  have hS : (pairSumPoly x).eval 0 = ∏ i, ∏ j ∈ Ioi i, ((0 : R) - x i - x j) := by
    simp only [pairSumPoly, eval_prod, eval_sub, eval_X, eval_C]
    exact Finset.prod_congr rfl fun i _ => Finset.prod_congr rfl fun j _ => by ring
  rw [hB, hdiag, prod_mul_distrib] at hA
  have hne : ∏ i, (-(2 * x i)) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr fun i _ => neg_ne_zero.mpr (mul_ne_zero h2 (hxi i))
  rw [hS]
  exact (mul_left_cancel₀ hne hA).symm

end Bgs.Mathlib
