module
public import Bgs.Mathlib.FlatTensor
@[expose] public section

/-!
# Small column phases: (O1), (O2), (O5) survive the perturbation (BGS-TRACE-081, §5, §7)

Source: `mathematics/spectral-obstructions/flat_spectrum_obstruction.md`, §§5–7.

Throughout, matrices carry the Euclidean operator norm (`Matrix.Norms.L2Operator`).
For phases `α : n → ℝ` put `E = diag(e^{iα_j})` and `U = A E`.

Formalized here:

* `pow_sub_pow_norm_le`: for `‖U‖, ‖A‖ ≤ 1`, `‖U^q - A^q‖ ≤ q ‖U - A‖` (telescoping, (O13));
* `entry_norm_le_l2`, `trace_norm_le_l2`: `|X_{ii}| ≤ ‖X‖`, `|Tr X| ≤ N ‖X‖`;
* `phaseE_sub_one_norm_le`: `‖E - 1‖ ≤ ε` if all `|α_j| ≤ ε`, hence `‖U - A‖ ≤ ε` (O12);
* `intensityP_mul_phase` (`P(U) = P(A)`), `reversalB_mul_phase` (`B(U) = E^* B(A) E`);
* (O1) for `U_k = A_k E` (`flatU`): `flatU_unitary`, `flatU_entry_normSq` (`P(U_k) = J_N`),
  `norm_reversalB_flatA` (`‖B(A_k)‖ = 2^{-k}`) and `norm_reversalB_flatU` (same for `U_k`);
* (O13) `flatU_trace_sub_le`: `|Tr U_k^q - Tr A_k^q| ≤ N q ε`;
* (O2) `flatU_trace_pow_le`: `|Tr U_k^q|/N ≤ p^{-1/2} + q ε` for `p ∤ q`;
* (O5) `flatU_trace_resonance`: `|Tr U_k^{t} - N| ≤ N t ε` and
  `flatU_form_factor_ge`: `|Tr U_k^{t}|²/N ≥ N (1 - t ε)²` when `t ε ≤ 1`.

The simple-spectrum selection lemma of §5 (generic phases split all degeneracies) and the
spacing/point-process statements (O3), (O4) are **not** formalized here; the results above
hold for *every* choice of small phases, in particular for the one selected in §5.
-/

open Finset Matrix
open scoped Matrix.Norms.L2Operator

namespace Bgs.Mathlib

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- **(O13), telescoping.** In a normed ring, if `‖U‖ ≤ 1` and `‖A‖ ≤ 1` then
`‖U^q - A^q‖ ≤ q ‖U - A‖`. -/
theorem pow_sub_pow_norm_le {R : Type*} [NormedRing R] {U A : R} (hU : ‖U‖ ≤ 1)
    (hA : ‖A‖ ≤ 1) (q : ℕ) : ‖U ^ q - A ^ q‖ ≤ q * ‖U - A‖ := by
  have key : ∀ q : ℕ, ‖U ^ (q + 1) - A ^ (q + 1)‖ ≤ (q + 1 : ℕ) * ‖U - A‖ := by
    intro q
    induction q with
    | zero => simp
    | succ q ih =>
      have hid : U ^ (q + 1 + 1) - A ^ (q + 1 + 1) =
          U ^ (q + 1) * (U - A) + (U ^ (q + 1) - A ^ (q + 1)) * A := by
        rw [pow_succ U (q + 1), pow_succ A (q + 1)]; noncomm_ring
      have hUq : ‖U ^ (q + 1)‖ ≤ 1 :=
        (norm_pow_le' U (Nat.succ_pos q)).trans (pow_le_one₀ (norm_nonneg _) hU)
      rw [hid]
      calc ‖U ^ (q + 1) * (U - A) + (U ^ (q + 1) - A ^ (q + 1)) * A‖
          ≤ ‖U ^ (q + 1)‖ * ‖U - A‖ + ‖U ^ (q + 1) - A ^ (q + 1)‖ * ‖A‖ :=
            (norm_add_le _ _).trans (add_le_add (norm_mul_le _ _) (norm_mul_le _ _))
        _ ≤ 1 * ‖U - A‖ + ((q + 1 : ℕ) * ‖U - A‖) * 1 := by
            gcongr
        _ = (q + 1 + 1 : ℕ) * ‖U - A‖ := by push_cast; ring
  cases q with
  | zero => simp
  | succ q => exact key q

/-- A unitary matrix has operator norm at most `1`. -/
lemma l2_norm_le_one_of_unitary {U : Matrix n n ℂ} (hU : Uᴴ * U = 1) : ‖U‖ ≤ 1 := by
  have h := l2_opNorm_conjTranspose_mul_self U
  rw [hU] at h
  have h1 : ‖(1 : Matrix n n ℂ)‖ ≤ 1 := by
    rcases isEmpty_or_nonempty n with hn | hn
    · rw [Subsingleton.elim (1 : Matrix n n ℂ) 0, norm_zero]; exact zero_le_one
    · rw [← diagonal_one, l2_opNorm_diagonal]
      exact (pi_norm_le_iff_of_nonneg zero_le_one).mpr fun i => by simp
  nlinarith [norm_nonneg U]

/-- Diagonal entries are bounded by the operator norm: `|X_{ii}| ≤ ‖X‖`. -/
lemma entry_norm_le_l2 (X : Matrix n n ℂ) (i j : n) : ‖X i j‖ ≤ ‖X‖ := by
  have h := l2_opNorm_mulVec X (EuclideanSpace.single j (1 : ℂ))
  have hx : ‖EuclideanSpace.single j (1 : ℂ)‖ = 1 := by simp
  rw [hx, mul_one] at h
  refine le_trans ?_ h
  have := PiLp.norm_apply_le ((EuclideanSpace.equiv n ℂ).symm (X *ᵥ (EuclideanSpace.single j 1))) i
  refine le_trans (le_of_eq ?_) this
  simp [EuclideanSpace.single]

/-- `|Tr X| ≤ N ‖X‖`. -/
lemma trace_norm_le_l2 (X : Matrix n n ℂ) : ‖X.trace‖ ≤ Fintype.card n * ‖X‖ := by
  calc ‖X.trace‖ ≤ ∑ i, ‖X i i‖ := norm_sum_le _ _
    _ ≤ ∑ _i : n, ‖X‖ := Finset.sum_le_sum fun i _ => entry_norm_le_l2 X i i
    _ = Fintype.card n * ‖X‖ := by simp

/-- The diagonal phase matrix `E = diag(e^{iα_j})`. -/
noncomputable def phaseE (α : n → ℝ) : Matrix n n ℂ :=
  Matrix.diagonal fun j => Complex.exp (Complex.I * α j)

lemma phaseE_unitary (α : n → ℝ) : (phaseE α)ᴴ * phaseE α = 1 := by
  rw [phaseE, diagonal_conjTranspose, diagonal_mul_diagonal, ← diagonal_one]
  congr 1; funext j
  simp only [Pi.star_apply, RCLike.star_def]
  rw [← Complex.exp_conj, ← Complex.exp_add]
  simp [Complex.conj_ofReal]

/-- `‖E - 1‖ ≤ ε` whenever all `|α_j| ≤ ε`. -/
lemma phaseE_sub_one_norm_le (α : n → ℝ) {ε : ℝ} (hε : 0 ≤ ε) (hα : ∀ j, |α j| ≤ ε) :
    ‖phaseE α - 1‖ ≤ ε := by
  have hd : phaseE α - 1 = diagonal fun j => Complex.exp (Complex.I * α j) - 1 := by
    ext i j
    by_cases h : i = j
    · subst h; simp [phaseE]
    · simp [phaseE, diagonal_apply_ne _ h, one_apply_ne h]
  rw [hd, l2_opNorm_diagonal]
  refine (pi_norm_le_iff_of_nonneg hε).mpr fun j => ?_
  exact (Real.norm_exp_I_mul_ofReal_sub_one_le).trans (by
    rw [Real.norm_eq_abs]; exact hα j)

/-- **(O12).** `‖A E - A‖ ≤ ε` for unitary `A` and phases `|α_j| ≤ ε`. -/
theorem mul_phase_sub_norm_le {A : Matrix n n ℂ} (hA : Aᴴ * A = 1) (α : n → ℝ) {ε : ℝ}
    (hε : 0 ≤ ε) (hα : ∀ j, |α j| ≤ ε) : ‖A * phaseE α - A‖ ≤ ε := by
  have : A * phaseE α - A = A * (phaseE α - 1) := by rw [Matrix.mul_sub, Matrix.mul_one]
  rw [this]
  calc ‖A * (phaseE α - 1)‖ ≤ ‖A‖ * ‖phaseE α - 1‖ := l2_opNorm_mul _ _
    _ ≤ 1 * ε := by
        gcongr
        · exact l2_norm_le_one_of_unitary hA
        · exact phaseE_sub_one_norm_le α hε hα
    _ = ε := one_mul ε

/-- Column phases preserve the intensity matrix: `P(A E) = P(A)`. -/
theorem intensityP_mul_phase (A : Matrix n n ℂ) (α : n → ℝ) :
    intensityP (A * phaseE α) = intensityP A := by
  ext i j
  simp only [intensityP, phaseE, mul_diagonal, Complex.normSq_mul]
  rw [Complex.normSq_eq_norm_sq (Complex.exp _), mul_comm Complex.I,
    Complex.norm_exp_ofReal_mul_I]
  simp

/-- Column phases conjugate the reversal matrix: `B(A E) = E^* B(A) E`. -/
theorem reversalB_mul_phase (A : Matrix n n ℂ) (α : n → ℝ) :
    reversalB (A * phaseE α) = (phaseE α)ᴴ * reversalB A * phaseE α := by
  ext i j
  simp only [reversalB, phaseE, mul_diagonal, diagonal_conjTranspose, diagonal_mul,
    Pi.star_apply, RCLike.star_def, map_mul]
  ring

/-- `‖X‖² = ‖X Xᴴ‖` (C⋆-identity). -/
lemma l2_norm_mul_self_eq (X : Matrix n n ℂ) : ‖X‖ * ‖X‖ = ‖X * Xᴴ‖ := by
  have h := l2_opNorm_conjTranspose_mul_self Xᴴ
  rw [conjTranspose_conjTranspose, l2_opNorm_conjTranspose] at h
  exact h.symm

/-- A nonzero orthogonal projection has operator norm `1`. -/
lemma l2_norm_proj {P : Matrix n n ℂ} (hP : Pᴴ = P) (hPP : P * P = P) (h0 : P ≠ 0) :
    ‖P‖ = 1 := by
  have h := l2_opNorm_conjTranspose_mul_self P
  rw [hP, hPP] at h
  have hne : ‖P‖ ≠ 0 := norm_ne_zero_iff.mpr h0
  have : ‖P‖ * (‖P‖ - 1) = 0 := by linarith
  rcases mul_eq_zero.mp this with h1 | h1
  · exact absurd h1 hne
  · linarith

/-- Unitary conjugation preserves the operator norm. -/
lemma l2_norm_unitary_conj {E : Matrix n n ℂ} (hE : Eᴴ * E = 1) (X : Matrix n n ℂ) :
    ‖Eᴴ * X * E‖ = ‖X‖ := by
  have hE' : E * Eᴴ = 1 := (mul_eq_one_comm_of_card_eq _ _ ℂ rfl).mp hE
  have hn1 : ‖E‖ ≤ 1 := l2_norm_le_one_of_unitary hE
  have hn2 : ‖Eᴴ‖ ≤ 1 := by rw [l2_opNorm_conjTranspose]; exact hn1
  apply le_antisymm
  · calc ‖Eᴴ * X * E‖ ≤ ‖Eᴴ * X‖ * ‖E‖ := l2_opNorm_mul _ _
      _ ≤ (‖Eᴴ‖ * ‖X‖) * ‖E‖ := by gcongr; exact l2_opNorm_mul _ _
      _ ≤ (1 * ‖X‖) * 1 := by gcongr
      _ = ‖X‖ := by ring
  · have hX : X = E * (Eᴴ * X * E) * Eᴴ := by
      simp only [← Matrix.mul_assoc, hE', Matrix.one_mul]
      rw [Matrix.mul_assoc, hE', Matrix.mul_one]
    calc ‖X‖ = ‖E * (Eᴴ * X * E) * Eᴴ‖ := by rw [← hX]
      _ ≤ ‖E * (Eᴴ * X * E)‖ * ‖Eᴴ‖ := l2_opNorm_mul _ _
      _ ≤ (‖E‖ * ‖Eᴴ * X * E‖) * ‖Eᴴ‖ := by gcongr; exact l2_opNorm_mul _ _
      _ ≤ (1 * ‖Eᴴ * X * E‖) * 1 := by gcongr
      _ = ‖Eᴴ * X * E‖ := by ring

/-- The perturbed obstruction matrix `U_k = A_k E`. -/
noncomputable def flatU (k p : ℕ) [NeZero p] (α : (Fin k → Fin 4) × ZMod p → ℝ) :
    Matrix ((Fin k → Fin 4) × ZMod p) ((Fin k → Fin 4) × ZMod p) ℂ :=
  flatA k p * phaseE α

theorem flatU_unitary (k p : ℕ) [NeZero p] (α) : (flatU k p α)ᴴ * flatU k p α = 1 := by
  rw [flatU, conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc (flatA k p)ᴴ,
    flatA_unitary, Matrix.one_mul, phaseE_unitary]

/-- **(O1), flatness of `U_k`.** `P(U_k) = J_N`: every entry has squared modulus `1/N`. -/
theorem flatU_entry_normSq (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (α) (i j) :
    Complex.normSq (flatU k p α i j) = 1 / (4 ^ k * p) := by
  have := congrFun (congrFun (intensityP_mul_phase (flatA k p) α) i) j
  simp only [intensityP] at this
  rw [flatU, this, flatA_entry_normSq k p hp2]

lemma kron_one_flatJ_ne_zero (k p : ℕ) [NeZero p] :
    kron (1 : Matrix (Fin k → Fin 4) (Fin k → Fin 4) ℂ) (flatJ p) ≠ 0 := by
  intro h
  have := congrFun (congrFun h (fun _ => 0, 0)) (fun _ => 0, 0)
  simp [kron, flatJ, NeZero.ne] at this

/-- **(O1), reversal norm of `A_k`.** `‖B(A_k)‖ = 2^{-k}`. -/
theorem norm_reversalB_flatA (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) :
    ‖reversalB (flatA k p)‖ = (1 / 2) ^ k := by
  have hP : ‖kron (1 : Matrix (Fin k → Fin 4) (Fin k → Fin 4) ℂ) (flatJ p)‖ = 1 := by
    apply l2_norm_proj
    · rw [kron_conjTranspose, conjTranspose_one, flatJ_conjTranspose]
    · rw [kron, ← mul_kronecker_mul, Matrix.mul_one, flatJ_mul_self]
    · exact kron_one_flatJ_ne_zero k p
  have h := l2_norm_mul_self_eq (reversalB (flatA k p))
  rw [reversalB_flatA_mul_conjTranspose k p hp2, norm_smul, hP, mul_one, norm_pow] at h
  have h4 : ‖(1 / 4 : ℂ)‖ = (1 / 2) ^ 2 := by norm_num
  rw [h4, ← pow_mul, mul_comm 2 k, pow_mul] at h
  have hnn := norm_nonneg (reversalB (flatA k p))
  have hpos : (0 : ℝ) ≤ (1 / 2) ^ k := by positivity
  nlinarith [sq_nonneg (‖reversalB (flatA k p)‖ - (1 / 2) ^ k),
    sq_nonneg (‖reversalB (flatA k p)‖ + (1 / 2) ^ k)]

/-- **(O1), reversal norm of `U_k`.** `‖B(U_k)‖ = 2^{-k}` for every choice of phases. -/
theorem norm_reversalB_flatU (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (α) :
    ‖reversalB (flatU k p α)‖ = (1 / 2) ^ k := by
  rw [flatU, reversalB_mul_phase, l2_norm_unitary_conj (phaseE_unitary α),
    norm_reversalB_flatA k p hp2]

/-- `‖U_k^q - A_k^q‖ ≤ q ε` and hence `|Tr(U_k^q - A_k^q)| ≤ N q ε` (O13). -/
theorem flatU_trace_sub_le (k p : ℕ) [NeZero p] (α) {ε : ℝ} (hε : 0 ≤ ε)
    (hα : ∀ j, |α j| ≤ ε) (q : ℕ) :
    ‖(flatU k p α ^ q).trace - (flatA k p ^ q).trace‖ ≤ (4 ^ k * p) * (q * ε) := by
  rw [← trace_sub]
  have h1 := trace_norm_le_l2 (flatU k p α ^ q - flatA k p ^ q)
  rw [flatA_card] at h1
  have h2 := pow_sub_pow_norm_le (l2_norm_le_one_of_unitary (flatU_unitary k p α))
    (l2_norm_le_one_of_unitary (flatA_unitary k p)) q
  have h3 := mul_phase_sub_norm_le (flatA_unitary k p) α hε hα
  rw [← flatU] at h3
  push_cast at h1
  calc _ ≤ (4 ^ k * p : ℝ) * ‖flatU k p α ^ q - flatA k p ^ q‖ := h1
    _ ≤ (4 ^ k * p) * (q * ε) := by
        gcongr
        exact h2.trans (by gcongr)

/-- **(O2).** For every `q` with `p ∤ q`: `|Tr U_k^q| / N ≤ p^{-1/2} + q ε`. -/
theorem flatU_trace_pow_le (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (α) {ε : ℝ} (hε : 0 ≤ ε)
    (hα : ∀ j, |α j| ≤ ε) (q : ℕ) (hq : ¬ p ∣ q) :
    ‖(flatU k p α ^ q).trace‖ / (4 ^ k * p) ≤ 1 / Real.sqrt p + q * ε := by
  have hp : (0 : ℝ) < p := by exact_mod_cast (Fact.out : p.Prime).pos
  have hN : (0 : ℝ) < 4 ^ k * p := by positivity
  have h1 := flatA_trace_pow_div_le k p hp2 q hq
  have h2 := flatU_trace_sub_le k p α hε hα q
  have h3 : ‖(flatU k p α ^ q).trace‖ ≤
      ‖(flatA k p ^ q).trace‖ + (4 ^ k * p) * (q * ε) := by
    have := norm_le_norm_add_norm_sub' ((flatU k p α ^ q).trace) ((flatA k p ^ q).trace)
    linarith
  rw [div_le_iff₀ hN] at h1 ⊢
  nlinarith

/-- **(O5).** At the resonance time `t = (4^k - 4) p`, `|Tr U_k^t - N| ≤ N t ε`. -/
theorem flatU_trace_resonance (k p : ℕ) [NeZero p] (hk : 1 ≤ k) (α) {ε : ℝ} (hε : 0 ≤ ε)
    (hα : ∀ j, |α j| ≤ ε) :
    ‖(flatU k p α ^ ((4 ^ k - 4) * p)).trace - ((4 ^ k * p : ℕ) : ℂ)‖ ≤
      (4 ^ k * p) * (((4 ^ k - 4) * p : ℕ) * ε) := by
  rw [← flatA_trace_resonance k p hk]
  exact flatU_trace_sub_le k p α hε hα _

/-- **(O5), form factor.** With `N = 4^k p` and `t = (4^k - 4) p`, if `t ε ≤ 1` then
`|Tr U_k^t|² / N ≥ N (1 - t ε)²`. -/
theorem flatU_form_factor_ge (k p : ℕ) [NeZero p] (hk : 1 ≤ k) (α) {ε : ℝ} (hε : 0 ≤ ε)
    (hα : ∀ j, |α j| ≤ ε) (hsmall : (((4 ^ k - 4) * p : ℕ) : ℝ) * ε ≤ 1) :
    (4 ^ k * p : ℝ) * (1 - (((4 ^ k - 4) * p : ℕ) : ℝ) * ε) ^ 2 ≤
      ‖(flatU k p α ^ ((4 ^ k - 4) * p)).trace‖ ^ 2 / (4 ^ k * p) := by
  have hN : (0 : ℝ) < 4 ^ k * p := by
    have : (0 : ℝ) < p := by exact_mod_cast Nat.pos_of_ne_zero (NeZero.ne p)
    positivity
  set t : ℝ := (((4 ^ k - 4) * p : ℕ) : ℝ)
  have h := flatU_trace_resonance k p hk α hε hα
  have hNc : ‖((4 ^ k * p : ℕ) : ℂ)‖ = 4 ^ k * p := by
    rw [Complex.norm_natCast]; push_cast; ring
  have h2 : (4 ^ k * p : ℝ) * (1 - t * ε) ≤ ‖(flatU k p α ^ ((4 ^ k - 4) * p)).trace‖ := by
    have := norm_sub_norm_le ((4 ^ k * p : ℕ) : ℂ) ((flatU k p α ^ ((4 ^ k - 4) * p)).trace)
    rw [norm_sub_rev] at this
    rw [hNc] at this
    nlinarith
  have h0 : 0 ≤ (4 ^ k * p : ℝ) * (1 - t * ε) := by nlinarith
  rw [le_div_iff₀ hN]
  nlinarith [mul_le_mul h2 h2 h0 (norm_nonneg _)]

#print axioms pow_sub_pow_norm_le
#print axioms l2_norm_le_one_of_unitary
#print axioms entry_norm_le_l2
#print axioms trace_norm_le_l2
#print axioms phaseE_unitary
#print axioms phaseE_sub_one_norm_le
#print axioms mul_phase_sub_norm_le
#print axioms intensityP_mul_phase
#print axioms reversalB_mul_phase
#print axioms l2_norm_mul_self_eq
#print axioms l2_norm_proj
#print axioms l2_norm_unitary_conj
#print axioms flatU_unitary
#print axioms flatU_entry_normSq
#print axioms kron_one_flatJ_ne_zero
#print axioms norm_reversalB_flatA
#print axioms norm_reversalB_flatU
#print axioms flatU_trace_sub_le
#print axioms flatU_trace_pow_le
#print axioms flatU_trace_resonance
#print axioms flatU_form_factor_ge
end Bgs.Mathlib
