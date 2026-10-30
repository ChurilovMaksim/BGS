module
public import Bgs.Mathlib.FlatChirp
@[expose] public section

/-!
# The tensor construction `A_k = H^{⊗k} ⊗ V_p` (BGS-TRACE-081, §4 and §7)

Source: `mathematics/spectral-obstructions/flat_spectrum_obstruction.md`, §4, §7.

The `k`-fold tensor power of a square matrix `M` over an index type `ι` is realised
concretely on words `Fin k → ι`: `(M^{⊗k})_{ij} = ∏_l M_{i_l j_l}` (`tensorPow`).
The obstruction matrix is `A_k = H^{⊗k} ⊗ V_p` (`flatA`), of dimension `N = 4^k p`.

Formalized here (identities (O10), (O11) and the exact-period part of §7):

* `tensorPow_mul`, `tensorPow_one`, `tensorPow_pow`, `tensorPow_conjTranspose`,
  `tensorPow_trace` (`Tr M^{⊗k} = (Tr M)^k`), `reversalB_tensorPow`, `normSq_tensorPow`;
* `flatA_entry_normSq` (`|A_{ij}|² = 1/N`), `flatA_unitary`, `flatA_pow_period` (`A^{6p} = 1`);
* `reversalB_flatA` (`B(A) = B(H)^{⊗k} ⊗ J_p`) and
  `reversalB_flatA_mul_conjTranspose` (`B(A) B(A)ᴴ = 4^{-k} (1 ⊗ J_p)`);
* (O11) `flatA_trace_pow_le`: `|Tr A^q| ≤ 4^k √p`, i.e. `|Tr A^q|/N ≤ p^{-1/2}` for `p ∤ q`;
* §7: `four_pow_mod_six` (`6 ∣ 4^k - 4`), `flatA_pow_resonance` (`A^{t} = 1` for
  `t = N - 4p`) and `flatA_trace_resonance` (`Tr A^t = N`).
-/

open Finset Matrix

namespace Bgs.Mathlib

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- The `k`-fold tensor power `M^{⊗k}` indexed by words `Fin k → ι`. -/
noncomputable def tensorPow (k : ℕ) (M : Matrix ι ι ℂ) : Matrix (Fin k → ι) (Fin k → ι) ℂ :=
  fun i j => ∏ l, M (i l) (j l)

omit [DecidableEq ι] in
theorem tensorPow_mul (k : ℕ) (M M' : Matrix ι ι ℂ) :
    tensorPow k (M * M') = tensorPow k M * tensorPow k M' := by
  ext i j
  simp only [tensorPow, mul_apply]
  rw [Finset.prod_univ_sum, Fintype.piFinset_univ]
  exact Finset.sum_congr rfl fun m _ => Finset.prod_mul_distrib

omit [Fintype ι] in
theorem tensorPow_one (k : ℕ) : tensorPow k (1 : Matrix ι ι ℂ) = 1 := by
  ext i j
  simp only [tensorPow, one_apply]
  by_cases hij : i = j
  · subst hij; simp
  · obtain ⟨l, hl⟩ := Function.ne_iff.mp hij
    rw [ite_eq_right_iff.mpr (fun h => absurd h hij)]
    exact Finset.prod_eq_zero (Finset.mem_univ l) (by simp [hl])

theorem tensorPow_pow (k n : ℕ) (M : Matrix ι ι ℂ) :
    tensorPow k (M ^ n) = (tensorPow k M) ^ n := by
  induction n with
  | zero => simp [tensorPow_one]
  | succ n ih => rw [pow_succ, tensorPow_mul, ih, pow_succ]

omit [Fintype ι] [DecidableEq ι] in
theorem tensorPow_conjTranspose (k : ℕ) (M : Matrix ι ι ℂ) :
    (tensorPow k M)ᴴ = tensorPow k Mᴴ := by
  ext i j
  simp [tensorPow, conjTranspose_apply]

omit [DecidableEq ι] in
theorem tensorPow_trace (k : ℕ) (M : Matrix ι ι ℂ) :
    (tensorPow k M).trace = M.trace ^ k := by
  simp only [Matrix.trace, Matrix.diag, tensorPow]
  rw [← Fin.prod_const, Finset.prod_univ_sum, Fintype.piFinset_univ]

theorem tensorPow_unitary (k : ℕ) {M : Matrix ι ι ℂ} (hM : Mᴴ * M = 1) :
    (tensorPow k M)ᴴ * tensorPow k M = 1 := by
  rw [tensorPow_conjTranspose, ← tensorPow_mul, hM, tensorPow_one]

omit [Fintype ι] [DecidableEq ι] in
theorem reversalB_tensorPow (k : ℕ) (M : Matrix ι ι ℂ) :
    reversalB (tensorPow k M) = tensorPow k (reversalB M) := by
  ext i j
  simp [reversalB, tensorPow, map_prod, Finset.prod_mul_distrib]

omit [Fintype ι] [DecidableEq ι] in
theorem normSq_tensorPow (k : ℕ) (M : Matrix ι ι ℂ) (i j : Fin k → ι) :
    Complex.normSq (tensorPow k M i j) = ∏ l, Complex.normSq (M (i l) (j l)) := by
  simp [tensorPow, map_prod]

/-! ## Kronecker products -/

section Kron

variable {κ : Type*} [Fintype κ] [DecidableEq κ]

/-- Shorthand for the Kronecker product of complex matrices. -/
noncomputable abbrev kron (A : Matrix ι ι ℂ) (B : Matrix κ κ ℂ) : Matrix (ι × κ) (ι × κ) ℂ :=
  Matrix.kroneckerMap (· * ·) A B

lemma kron_pow (A : Matrix ι ι ℂ) (B : Matrix κ κ ℂ) (n : ℕ) :
    (kron A B) ^ n = kron (A ^ n) (B ^ n) := by
  induction n with
  | zero => simp [kron]
  | succ n ih => rw [pow_succ, ih, pow_succ, pow_succ, kron, kron, kron, ← mul_kronecker_mul]

omit [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] in
lemma kron_conjTranspose (A : Matrix ι ι ℂ) (B : Matrix κ κ ℂ) :
    (kron A B)ᴴ = kron Aᴴ Bᴴ := by
  ext i j; simp [kron, conjTranspose_apply]

lemma kron_unitary {A : Matrix ι ι ℂ} {B : Matrix κ κ ℂ} (hA : Aᴴ * A = 1) (hB : Bᴴ * B = 1) :
    (kron A B)ᴴ * kron A B = 1 := by
  rw [kron_conjTranspose, kron, kron, ← mul_kronecker_mul, hA, hB, Matrix.one_kronecker_one]

omit [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] in
lemma reversalB_kron (A : Matrix ι ι ℂ) (B : Matrix κ κ ℂ) :
    reversalB (kron A B) = kron (reversalB A) (reversalB B) := by
  ext i j; simp [reversalB, kron]; ring

omit [DecidableEq ι] [DecidableEq κ] in
lemma kron_trace (A : Matrix ι ι ℂ) (B : Matrix κ κ ℂ) :
    (kron A B).trace = A.trace * B.trace := Matrix.trace_kronecker A B

end Kron

/-! ## Unitary matrices have bounded traces -/

/-- Every entry of a unitary matrix has squared modulus at most `1`. -/
lemma unitary_entry_normSq_le {U : Matrix ι ι ℂ} (hU : Uᴴ * U = 1) (i j : ι) :
    Complex.normSq (U i j) ≤ 1 := by
  have h := congrFun (congrFun hU j) j
  simp only [mul_apply, conjTranspose_apply, one_apply_eq, RCLike.star_def] at h
  have h' : ∑ x, Complex.normSq (U x j) = 1 := by
    have : ((∑ x, Complex.normSq (U x j) : ℝ) : ℂ) = 1 := by
      rw [← h]; push_cast
      exact Finset.sum_congr rfl fun x _ => by rw [Complex.normSq_eq_conj_mul_self]
    exact_mod_cast this
  rw [← h']
  exact Finset.single_le_sum (f := fun x => Complex.normSq (U x j))
    (fun x _ => Complex.normSq_nonneg _) (Finset.mem_univ i)

lemma unitary_entry_norm_le {U : Matrix ι ι ℂ} (hU : Uᴴ * U = 1) (i j : ι) :
    ‖U i j‖ ≤ 1 := by
  have h := unitary_entry_normSq_le hU i j
  rw [Complex.normSq_eq_norm_sq] at h
  nlinarith [norm_nonneg (U i j)]

/-- `|Tr U| ≤ n` for a unitary `n × n` matrix. -/
lemma unitary_trace_norm_le {U : Matrix ι ι ℂ} (hU : Uᴴ * U = 1) :
    ‖U.trace‖ ≤ Fintype.card ι := by
  calc ‖U.trace‖ ≤ ∑ i, ‖U i i‖ := norm_sum_le _ _
    _ ≤ ∑ _i : ι, (1 : ℝ) := Finset.sum_le_sum fun i _ => unitary_entry_norm_le hU i i
    _ = Fintype.card ι := by simp

lemma unitary_pow {U : Matrix ι ι ℂ} (hU : Uᴴ * U = 1) (n : ℕ) : (U ^ n)ᴴ * U ^ n = 1 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc _ (U ^ n), ih,
      Matrix.one_mul, hU]

/-! ## The obstruction matrix `A_k = H^{⊗k} ⊗ V_p` -/

/-- `A_k = H^{⊗k} ⊗ V_p`, a unitary matrix of size `N = 4^k p`. -/
noncomputable def flatA (k p : ℕ) [NeZero p] :
    Matrix ((Fin k → Fin 4) × ZMod p) ((Fin k → Fin 4) × ZMod p) ℂ :=
  kron (tensorPow k coreH) (chirpV p)

lemma flatA_card (k p : ℕ) [NeZero p] :
    Fintype.card ((Fin k → Fin 4) × ZMod p) = 4 ^ k * p := by
  simp [Fintype.card_prod, ZMod.card]

/-- **(O10), flatness.** `|A_{ij}|² = 1/N` with `N = 4^k p`. -/
theorem flatA_entry_normSq (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (i j) :
    Complex.normSq (flatA k p i j) = 1 / (4 ^ k * p) := by
  simp only [flatA, kron, kroneckerMap_apply, Complex.normSq_mul, normSq_tensorPow,
    coreH_entry_normSq, chirpV_entry_normSq p hp2, Finset.prod_const, Finset.card_univ,
    Fintype.card_fin]
  rw [div_pow, one_pow]; field_simp

/-- `A_k` is unitary. -/
theorem flatA_unitary (k p : ℕ) [NeZero p] : (flatA k p)ᴴ * flatA k p = 1 :=
  kron_unitary (tensorPow_unitary k coreH_unitary) (chirpV_unitary p)

lemma flatA_pow (k p : ℕ) [NeZero p] (n : ℕ) :
    flatA k p ^ n = kron (tensorPow k (coreH ^ n)) (chirpV p ^ n) := by
  rw [flatA, kron_pow, tensorPow_pow]

/-- **(O10), period.** `A_k^{6p} = 1`: the spectrum lies in the `6p`-th roots of unity. -/
theorem flatA_pow_period (k p : ℕ) [NeZero p] : flatA k p ^ (6 * p) = 1 := by
  rw [flatA_pow, pow_mul, coreH_pow_six, one_pow, tensorPow_one, mul_comm, pow_mul,
    chirpV_pow_p, one_pow, kron, Matrix.one_kronecker_one]

/-- The reversal matrix of the chirp is the flat matrix `J_p = p⁻¹ 𝟙𝟙ᵀ`. -/
theorem reversalB_chirpV (p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (i j : ZMod p) :
    reversalB (chirpV p) i j = (p : ℂ)⁻¹ := by
  have hT : chirpV p j i = chirpV p i j := by
    rw [← transpose_apply (chirpV p) i j, chirpV_transpose]
  rw [reversalB, hT, Complex.mul_conj, chirpV_entry_normSq p hp2]
  push_cast; ring

/-- The flat projection `J_p = p⁻¹ 𝟙𝟙ᵀ`. -/
noncomputable def flatJ (p : ℕ) : Matrix (ZMod p) (ZMod p) ℂ := fun _ _ => (p : ℂ)⁻¹

theorem flatJ_mul_self (p : ℕ) [NeZero p] : flatJ p * flatJ p = flatJ p := by
  ext i j
  simp [flatJ, mul_apply, ZMod.card]
  have : (p : ℂ) ≠ 0 := by exact_mod_cast NeZero.ne p
  field_simp

theorem flatJ_conjTranspose (p : ℕ) : (flatJ p)ᴴ = flatJ p := by
  ext i j; simp [flatJ, conjTranspose_apply]

/-- **(O10), reversal.** `B(A_k) = B(H)^{⊗k} ⊗ J_p`. -/
theorem reversalB_flatA (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) :
    reversalB (flatA k p) = kron (tensorPow k (reversalB coreH)) (flatJ p) := by
  rw [flatA, reversalB_kron, reversalB_tensorPow]
  congr 1
  ext i j; exact reversalB_chirpV p hp2 i j

omit [Fintype ι] in
lemma tensorPow_smul_one (k : ℕ) (c : ℂ) :
    tensorPow k (c • (1 : Matrix ι ι ℂ)) = c ^ k • (1 : Matrix (Fin k → ι) (Fin k → ι) ℂ) := by
  ext i j
  simp only [tensorPow, Matrix.smul_apply, one_apply, smul_eq_mul]
  by_cases hij : i = j
  · subst hij; simp
  · obtain ⟨l, hl⟩ := Function.ne_iff.mp hij
    simp only [hij, ite_false, mul_zero]
    exact Finset.prod_eq_zero (Finset.mem_univ l) (by simp [hl])

/-- `B(A_k) B(A_k)ᴴ = 4^{-k} (1 ⊗ J_p)`; since `1 ⊗ J_p` is a nonzero orthogonal projection,
this says `‖B(A_k)‖ = 2^{-k}`. -/
theorem reversalB_flatA_mul_conjTranspose (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) :
    reversalB (flatA k p) * (reversalB (flatA k p))ᴴ =
      ((1 / 4 : ℂ) ^ k) • kron (1 : Matrix (Fin k → Fin 4) (Fin k → Fin 4) ℂ) (flatJ p) := by
  rw [reversalB_flatA k p hp2, kron_conjTranspose, kron, kron, ← mul_kronecker_mul,
    tensorPow_conjTranspose, ← tensorPow_mul, reversal_coreH_mul_conjTranspose,
    flatJ_conjTranspose, flatJ_mul_self, tensorPow_smul_one, kron]
  rw [Matrix.smul_kronecker]

/-- **(O11).** `|Tr A_k^q| ≤ 4^k √p` whenever `p ∤ q`; equivalently
`|Tr A_k^q| / N ≤ p^{-1/2}` with `N = 4^k p`. -/
theorem flatA_trace_pow_le (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (q : ℕ) (hq : ¬ p ∣ q) :
    ‖(flatA k p ^ q).trace‖ ≤ 4 ^ k * Real.sqrt p := by
  rw [flatA_pow, kron_trace, tensorPow_trace, norm_mul, norm_pow,
    chirpV_trace_pow_norm p hp2 q hq]
  gcongr
  have := unitary_trace_norm_le (unitary_pow coreH_unitary q)
  simpa using this

/-- **(O11), normalized form.** `|Tr A_k^q| / N ≤ p^{-1/2}` for `p ∤ q`. -/
theorem flatA_trace_pow_div_le (k p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (q : ℕ)
    (hq : ¬ p ∣ q) :
    ‖(flatA k p ^ q).trace‖ / (4 ^ k * p) ≤ 1 / Real.sqrt p := by
  have hp : (0 : ℝ) < p := by exact_mod_cast (Fact.out : p.Prime).pos
  have hs : 0 < Real.sqrt p := Real.sqrt_pos.mpr hp
  rw [div_le_div_iff₀ (by positivity) hs]
  calc ‖(flatA k p ^ q).trace‖ * Real.sqrt p ≤ 4 ^ k * Real.sqrt p * Real.sqrt p := by
        gcongr; exact flatA_trace_pow_le k p hp2 q hq
    _ = 1 * (4 ^ k * p) := by rw [mul_assoc, Real.mul_self_sqrt hp.le]; ring

/-! ## §7: Heisenberg-scale resonances -/

/-- `4^k ≡ 4 (mod 6)` for `k ≥ 1`. -/
theorem four_pow_mod_six (k : ℕ) (hk : 1 ≤ k) : 6 ∣ 4 ^ k - 4 := by
  induction k, hk using Nat.le_induction with
  | base => norm_num
  | succ k hk ih =>
    have h4 : 4 ≤ 4 ^ k := by
      calc 4 = 4 ^ 1 := by norm_num
        _ ≤ 4 ^ k := Nat.pow_le_pow_right (by norm_num) hk
    obtain ⟨c, hc⟩ := ih
    refine ⟨4 * c + 2, ?_⟩
    rw [pow_succ]; omega

/-- The resonance time `t_k = N_k - 4 p = (4^k - 4) p` is a multiple of `6p`, so
`A_k^{t_k} = 1`. -/
theorem flatA_pow_resonance (k p : ℕ) [NeZero p] (hk : 1 ≤ k) :
    flatA k p ^ ((4 ^ k - 4) * p) = 1 := by
  obtain ⟨c, hc⟩ := four_pow_mod_six k hk
  rw [hc, show 6 * c * p = 6 * p * c by ring, pow_mul, flatA_pow_period, one_pow]

/-- **§7.** `Tr A_k^{t_k} = N_k` at the resonance time `t_k = (4^k - 4) p`. -/
theorem flatA_trace_resonance (k p : ℕ) [NeZero p] (hk : 1 ≤ k) :
    (flatA k p ^ ((4 ^ k - 4) * p)).trace = (4 ^ k * p : ℕ) := by
  rw [flatA_pow_resonance k p hk, trace_one, flatA_card]

#print axioms tensorPow_mul
#print axioms tensorPow_one
#print axioms tensorPow_pow
#print axioms tensorPow_conjTranspose
#print axioms tensorPow_trace
#print axioms tensorPow_unitary
#print axioms reversalB_tensorPow
#print axioms normSq_tensorPow
#print axioms kron_pow
#print axioms kron_conjTranspose
#print axioms kron_unitary
#print axioms reversalB_kron
#print axioms kron_trace
#print axioms unitary_entry_normSq_le
#print axioms unitary_entry_norm_le
#print axioms unitary_trace_norm_le
#print axioms unitary_pow
#print axioms flatA_card
#print axioms flatA_entry_normSq
#print axioms flatA_unitary
#print axioms flatA_pow
#print axioms flatA_pow_period
#print axioms reversalB_chirpV
#print axioms flatJ_mul_self
#print axioms flatJ_conjTranspose
#print axioms reversalB_flatA
#print axioms tensorPow_smul_one
#print axioms reversalB_flatA_mul_conjTranspose
#print axioms flatA_trace_pow_le
#print axioms flatA_trace_pow_div_le
#print axioms four_pow_mod_six
#print axioms flatA_pow_resonance
#print axioms flatA_trace_resonance
end Bgs.Mathlib
