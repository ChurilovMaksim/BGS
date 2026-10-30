module
public import Bgs.Mathlib.FlatTensor
@[expose] public section

/-!
# Return intensities `R_m = P(A^m)` of the flat obstruction family (BGS-TRACE-083, R1)

Source: `mathematics/spectral-obstructions/coherent_first_return_pulse.md`, proof of R1.

For `A = H^{⊗k} ⊗ V_p` (TRACE-081) the diagonal return matrices `R_m = P(A^m)` are

  `R_m = (S^{m/2} if m even, J_n if m odd) ⊗ (I_p if p ∣ m, J_p if p ∤ m)`,

with `S = K^{⊗k}`, `K = H²` a permutation.  Formalized here:

* `chirpV_pow_apply`: `(V_p^m)_{ij} = p⁻¹ ∑_b ψ(m b² + (j-i) b)`;
* `chirpV_pow_entry_normSq`: `|(V_p^m)_{ij}|² = 1/p` if `p ∤ m`, and `V_p^m = 1` if `p ∣ m`
  (`chirpV_pow_of_dvd`);
* `coreH_pow_even` (`H^{2r} = K^r`), `coreK_pow_three` (`K³ = 1`),
  `coreH_pow_odd_entry_normSq` (`H^{2r+1}` is flat: all entries `1/4`);
* `intensity_flatA_pow`: the factorization `|(A^m)_{ij}|² = |(H^{⊗k,m})_{i₁j₁}|² · c_p(m)`,
  with `c_p(m) = δ_{i₂j₂}` if `p ∣ m` and `1/p` otherwise;
* `intensity_flatA_pow_odd`: for odd `m` and `p ∤ m`, `P(A^m) = J_N` (all entries `1/N`).
-/

open Finset Matrix

namespace Bgs.Mathlib

/-- Entry formula for powers of the chirp: `(V_p^m)_{ij} = p⁻¹ ∑_b ψ(m b² + (j-i) b)`. -/
theorem chirpV_pow_apply (p : ℕ) [NeZero p] (m : ℕ) (i j : ZMod p) :
    (chirpV p ^ m) i j = (p : ℂ)⁻¹ * ∑ b : ZMod p, ψp p (m * b ^ 2 + (j - i) * b) := by
  rw [chirpV_pow, chirpD_pow, mul_apply, Finset.mul_sum]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [mul_diagonal, conjTranspose_apply, RCLike.star_def, mul_right_comm,
    fourier_conj_mul, mul_assoc]
  congr 1
  rw [← AddChar.map_add_eq_mul]; congr 1; ring

/-- If `p ∣ m` then `V_p^m = 1`. -/
theorem chirpV_pow_of_dvd (p : ℕ) [NeZero p] {m : ℕ} (h : p ∣ m) : chirpV p ^ m = 1 := by
  obtain ⟨c, rfl⟩ := h
  rw [pow_mul, chirpV_pow_p, one_pow]

/-- If `p ∤ m` then `V_p^m` is flat: `|(V_p^m)_{ij}|² = 1/p`. -/
theorem chirpV_pow_entry_normSq (p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) {m : ℕ} (hm : ¬ p ∣ m)
    (i j : ZMod p) : Complex.normSq ((chirpV p ^ m) i j) = 1 / p := by
  rw [chirpV_pow_apply, Complex.normSq_mul]
  have hm' : (m : ZMod p) ≠ 0 := by rwa [Ne, ZMod.natCast_eq_zero_iff]
  rw [chirp_sum_normSq p hp2 (m : ZMod p) (j - i) hm', Complex.normSq_inv,
    Complex.normSq_natCast]
  have hp : (p : ℝ) ≠ 0 := by exact_mod_cast (Fact.out : p.Prime).ne_zero
  field_simp

/-! ## Powers of the core -/

/-- The permutation `K = H²`. -/
def coreK : Matrix (Fin 4) (Fin 4) ℂ := !![1, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1; 0, 1, 0, 0]

theorem coreH_sq_eq_K : coreH ^ 2 = coreK := coreH_sq

theorem coreK_pow_three : coreK ^ 3 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [coreK, pow_succ, mul_apply, Fin.sum_univ_four]

/-- `H^{2r} = K^r`. -/
theorem coreH_pow_even (r : ℕ) : coreH ^ (2 * r) = coreK ^ r := by
  rw [pow_mul, coreH_sq_eq_K]

/-- The three powers of `K` are `0/1` permutation matrices. -/
lemma coreK_pow_cases (r : ℕ) : coreK ^ r = coreK ^ (r % 3) := by
  conv_lhs => rw [← Nat.div_add_mod r 3, pow_add, pow_mul, coreK_pow_three, one_pow, one_mul]

/-- `H^{2r+1}` is flat: every entry has squared modulus `1/4`. -/
theorem coreH_pow_odd_entry_normSq (r : ℕ) (i j : Fin 4) :
    Complex.normSq ((coreH ^ (2 * r + 1)) i j) = 1 / 4 := by
  rw [pow_succ, coreH_pow_even, coreK_pow_cases]
  have h3 : r % 3 < 3 := Nat.mod_lt _ (by norm_num)
  interval_cases (r % 3) <;>
  · fin_cases i <;> fin_cases j <;>
      simp [coreK, coreH, coreW, pow_succ, mul_apply, Fin.sum_univ_four, Complex.normSq_apply] <;>
      norm_num

/-! ## The return matrices `R_m` -/

/-- **R1, factorization of `R_m = P(A^m)`.**
`|(A^m)_{ij}|² = |(H^{⊗k})^m_{i₁ j₁}|² · c`, where `c = [i₂ = j₂]` if `p ∣ m` and
`c = 1/p` if `p ∤ m`. -/
theorem intensity_flatA_pow (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (m : ℕ) (i j) :
    Complex.normSq ((flatA k p ^ m) i j) =
      Complex.normSq ((tensorPow k (coreH ^ m)) i.1 j.1) *
        (if p ∣ m then (if i.2 = j.2 then (1 : ℝ) else 0) else 1 / (p : ℝ)) := by
  rw [flatA_pow, kron, kroneckerMap_apply, Complex.normSq_mul]
  congr 1
  split_ifs with h hij
  · rw [chirpV_pow_of_dvd p h, hij, one_apply_eq, Complex.normSq_one]
  · rw [chirpV_pow_of_dvd p h, one_apply_ne hij, Complex.normSq_zero]
  · exact chirpV_pow_entry_normSq p hp2 h _ _

/-- **R1, odd times.**  For odd `m` with `p ∤ m`, `R_m = J_n ⊗ J_p = J_N`:
every entry of `A^m` has squared modulus `1/(4^k p)`. -/
theorem intensity_flatA_pow_odd (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (r : ℕ)
    (hm : ¬ p ∣ 2 * r + 1) (i j) :
    Complex.normSq ((flatA k p ^ (2 * r + 1)) i j) = 1 / (4 ^ k * p) := by
  rw [intensity_flatA_pow k p hp2, normSq_tensorPow]
  simp only [hm, ite_false]
  simp only [coreH_pow_odd_entry_normSq, prod_const, card_univ, Fintype.card_fin]
  rw [div_pow, one_pow]; field_simp

/-- **R1, odd multiples of `p`.**  For odd `m` with `p ∣ m`, `R_m = J_n ⊗ I_p`. -/
theorem intensity_flatA_pow_odd_dvd (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (r : ℕ)
    (hm : p ∣ 2 * r + 1) (i j) :
    Complex.normSq ((flatA k p ^ (2 * r + 1)) i j) =
      (1 / 4 : ℝ) ^ k * (if i.2 = j.2 then (1 : ℝ) else 0) := by
  rw [intensity_flatA_pow k p hp2, normSq_tensorPow]
  simp only [hm, ite_true]
  simp only [coreH_pow_odd_entry_normSq, prod_const, card_univ, Fintype.card_fin]

/-- **R1, even times.**  For `m = 2r`, `R_m = S^r ⊗ (I_p or J_p)` with `S = K^{⊗k}`. -/
theorem intensity_flatA_pow_even (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (r : ℕ) (i j) :
    Complex.normSq ((flatA k p ^ (2 * r)) i j) =
      Complex.normSq ((tensorPow k (coreK ^ r)) i.1 j.1) *
        (if p ∣ 2 * r then (if i.2 = j.2 then (1 : ℝ) else 0) else 1 / (p : ℝ)) := by
  rw [intensity_flatA_pow k p hp2, coreH_pow_even]

#print axioms chirpV_pow_apply
#print axioms chirpV_pow_of_dvd
#print axioms chirpV_pow_entry_normSq
#print axioms coreH_sq_eq_K
#print axioms coreK_pow_three
#print axioms coreH_pow_even
#print axioms coreK_pow_cases
#print axioms coreH_pow_odd_entry_normSq
#print axioms intensity_flatA_pow
#print axioms intensity_flatA_pow_odd
#print axioms intensity_flatA_pow_odd_dvd
#print axioms intensity_flatA_pow_even
end Bgs.Mathlib
