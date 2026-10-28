module
public import Mathlib
@[expose] public section

/-!
# A two-step obstruction inside the unistochastic class (BGS-TRACE-074, §§1–2)

Source: `mathematics/trace-bridge/unitary_two_step_obstruction.md`.

**§2, rank-one unitary correction (5)–(6).**  For unit vectors `c ≠ d` put `v = c - d`,
`γ = 1 - d^* c` and `H(c,d) = I - γ⁻¹ v v^*`.  Then `γ ≠ 0` (`gamma_ne_zero`),
`H c = d` (`householder_apply`) and `H^* H = I` (`householder_unitary`).

**§2, compatible prescriptions (7)–(9).**  For any unitary `Z`, labels `i ≠ j`, and unit
vectors `a, β` with `a_j = 0`, `β_i = 0`, the deterministic construction
`L = H(Z e_j, β)`, `W = L Z`, `r = W^* e_i`, `R = H(a, r)`, `S = W R` gives a unitary `S` with
`S e_j = β`, `S a = e_i`, `e_i^* S = a^*` (`twoStep_prescriptions`), hence
`(P²)_{ij} = ∑_k |a_k|² |β_k|²` (`twoStep_P2_entry`) — with `a = β = b^{-1/2} 1_B` this is
exactly `1/b` (equation (9)).

**§1, positive companion (4).**  For a doubly stochastic real `P` and `h ≥ 2`,
`|(P^h)_{ij} - 1/n| ≤ ‖P - J‖^{h-2} √((∑_k P_ik² - 1/n)(∑_k P_kj² - 1/n))`
(`doublyStochastic_power_entry`), and with nonnegative entries bounded by `δ`, the right side
is at most `‖P - J‖^{h-2} (δ - 1/n)` (`doublyStochastic_power_entry_delta`).

The Haar-measure statements of §§3–5 are not formalized.
-/

open Finset Matrix

namespace Bgs.Mathlib

section Householder

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- `γ = 1 - d^* c`. -/
noncomputable def hhGamma (c d : n → ℂ) : ℂ := 1 - star d ⬝ᵥ c

/-- The rank-one correction `H(c,d) = I - γ⁻¹ (c - d)(c - d)^*` (`H(c,c) = I`). -/
noncomputable def householder (c d : n → ℂ) : Matrix n n ℂ :=
  if c = d then 1 else 1 - (hhGamma c d)⁻¹ • vecMulVec (c - d) (star (c - d))

omit [DecidableEq n] in
lemma star_dot_sub_self {c d : n → ℂ} (hc : star c ⬝ᵥ c = 1) :
    star (c - d) ⬝ᵥ c = hhGamma c d := by
  simp [hhGamma, star_sub, sub_dotProduct, hc]

omit [DecidableEq n] in
lemma star_dot_comm (c d : n → ℂ) : star c ⬝ᵥ d = star (star d ⬝ᵥ c) := by
  simp [dotProduct, mul_comm]

omit [DecidableEq n] in
lemma norm_sq_sub {c d : n → ℂ} (hc : star c ⬝ᵥ c = 1) (hd : star d ⬝ᵥ d = 1) :
    star (c - d) ⬝ᵥ (c - d) = hhGamma c d + star (hhGamma c d) := by
  simp only [hhGamma, star_sub, sub_dotProduct, dotProduct_sub, hc, hd, star_one]
  rw [star_dot_comm c d]
  ring

omit [DecidableEq n] in
lemma dot_star_self_ne_zero {v : n → ℂ} (hv : v ≠ 0) : star v ⬝ᵥ v ≠ 0 := by
  intro h
  apply hv
  have h' : ∑ i, Complex.normSq (v i) = 0 := by
    have : ((∑ i, Complex.normSq (v i) : ℝ) : ℂ) = star v ⬝ᵥ v := by
      push_cast
      simp [dotProduct, Complex.normSq_eq_conj_mul_self]
    exact_mod_cast this.trans h
  funext i
  have := (Finset.sum_eq_zero_iff_of_nonneg (fun i _ => Complex.normSq_nonneg (v i))).mp h' i
    (mem_univ i)
  simpa using this

omit [DecidableEq n] in
/-- `γ ≠ 0` for distinct unit vectors (equality case of Cauchy–Schwarz). -/
theorem gamma_ne_zero {c d : n → ℂ} (hc : star c ⬝ᵥ c = 1) (hd : star d ⬝ᵥ d = 1)
    (hcd : c ≠ d) : hhGamma c d ≠ 0 := by
  intro h
  have := norm_sq_sub hc hd
  rw [h, star_zero, add_zero] at this
  exact dot_star_self_ne_zero (sub_ne_zero.mpr hcd) this

/-- **(6)** `H(c,d) c = d`. -/
theorem householder_apply {c d : n → ℂ} (hc : star c ⬝ᵥ c = 1) (hd : star d ⬝ᵥ d = 1) :
    householder c d *ᵥ c = d := by
  unfold householder
  split_ifs with hcd
  · simp [hcd]
  · rw [sub_mulVec, one_mulVec, smul_mulVec, vecMulVec_mulVec, star_dot_sub_self hc]
    have hγ := gamma_ne_zero hc hd hcd
    ext i
    simp [Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
    field_simp
    ring

/-- **(6)** `H(c,d)` is unitary. -/
theorem householder_unitary {c d : n → ℂ} (hc : star c ⬝ᵥ c = 1) (hd : star d ⬝ᵥ d = 1) :
    (householder c d)ᴴ * householder c d = 1 := by
  unfold householder
  split_ifs with hcd
  · simp
  · set v := c - d
    set γ := hhGamma c d
    have hγ : γ ≠ 0 := gamma_ne_zero hc hd hcd
    have hγ' : star γ ≠ 0 := star_ne_zero.mpr hγ
    have hvv : star v ⬝ᵥ v = γ + star γ := norm_sq_sub hc hd
    rw [conjTranspose_sub, conjTranspose_one, conjTranspose_smul, conjTranspose_vecMulVec,
      star_star, sub_mul, mul_sub, mul_sub, Matrix.one_mul, Matrix.mul_one, Matrix.one_mul,
      smul_mul_smul_comm, vecMulVec_mul_vecMulVec, hvv]
    rw [show vecMulVec v ((γ + star γ) • star v) = (γ + star γ) • vecMulVec v (star v) by
      ext i j; simp [vecMulVec_apply]; ring]
    rw [smul_smul]
    have hcoef : star γ⁻¹ * γ⁻¹ * (γ + star γ) = star γ⁻¹ + γ⁻¹ := by
      rw [star_inv₀]; field_simp
    rw [hcoef, add_smul]
    abel

end Householder

/-! ## The compatible prescriptions (7)–(9) -/

section Prescriptions

variable {n : Type*} [Fintype n] [DecidableEq n]

lemma mulVec_single_eq_col (M : Matrix n n ℂ) (j : n) : M *ᵥ Pi.single j 1 = fun k => M k j := by
  ext k; simp [mulVec, dotProduct, Pi.single_apply]

lemma unitary_mul_conj {U : Matrix n n ℂ} (hU : Uᴴ * U = 1) : U * Uᴴ = 1 :=
  (mul_eq_one_comm_of_card_eq _ _ ℂ rfl).mp hU

lemma unitary_norm_vec {U : Matrix n n ℂ} (hU : Uᴴ * U = 1) (x : n → ℂ) :
    star (U *ᵥ x) ⬝ᵥ (U *ᵥ x) = star x ⬝ᵥ x := by
  rw [star_mulVec, dotProduct_mulVec, vecMul_vecMul, hU, vecMul_one]

/-- **(7)–(8).**  The deterministic two-step construction realises the compatible row and
column prescriptions `S e_j = β`, `S a = e_i`, `S^* e_i = a` with `S` unitary.
(The labels need not even be distinct for this algebraic step.) -/
theorem twoStep_prescriptions {Z : Matrix n n ℂ} (hZ : Zᴴ * Z = 1) {i j : n}
    {a β : n → ℂ} (ha : star a ⬝ᵥ a = 1) (hβ : star β ⬝ᵥ β = 1) (haj : a j = 0)
    (hβi : β i = 0) :
    let L := householder (Z *ᵥ Pi.single j 1) β
    let W := L * Z
    let r := Wᴴ *ᵥ Pi.single i 1
    let R := householder a r
    let S := W * R
    Sᴴ * S = 1 ∧ S *ᵥ Pi.single j 1 = β ∧ S *ᵥ a = Pi.single i 1 ∧ Sᴴ *ᵥ Pi.single i 1 = a := by
  intro L W r R S
  have hej : star (Pi.single j (1 : ℂ)) ⬝ᵥ Pi.single j 1 = 1 := by simp
  have hei : star (Pi.single i (1 : ℂ)) ⬝ᵥ Pi.single i 1 = 1 := by simp
  have hZe : star (Z *ᵥ Pi.single j 1) ⬝ᵥ (Z *ᵥ Pi.single j 1) = 1 := by
    rw [unitary_norm_vec hZ, hej]
  have hL : Lᴴ * L = 1 := householder_unitary hZe hβ
  have hW : Wᴴ * W = 1 := by
    simp only [W, conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc Lᴴ, hL,
      Matrix.one_mul, hZ]
  have hWej : W *ᵥ Pi.single j 1 = β := by
    simp only [W, ← mulVec_mulVec]; exact householder_apply hZe hβ
  have hWc : W * Wᴴ = 1 := unitary_mul_conj hW
  have hr : star r ⬝ᵥ r = 1 := by
    have hWh : (Wᴴ)ᴴ * Wᴴ = 1 := by rw [conjTranspose_conjTranspose]; exact hWc
    simp only [r]; rw [unitary_norm_vec hWh, hei]
  have hrj : r j = 0 := by
    have : r j = star (W i j) := by simp [r]
    have hWij : W i j = β i := by
      rw [← hWej]; simp [mulVec, dotProduct, Pi.single_apply]
    rw [this, hWij, hβi, star_zero]
  have hR : Rᴴ * R = 1 := householder_unitary ha hr
  have hRa : R *ᵥ a = r := householder_apply ha hr
  have hRej : R *ᵥ Pi.single j 1 = Pi.single j 1 := by
    simp only [R, householder]
    split_ifs with h
    · exact one_mulVec _
    · rw [sub_mulVec, one_mulVec, smul_mulVec, vecMulVec_mulVec]
      have : star (a - r) ⬝ᵥ Pi.single j 1 = 0 := by
        simp [dotProduct, Pi.single_apply, haj, hrj]
      rw [this]; simp
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp only [S, conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc Wᴴ, hW,
      Matrix.one_mul, hR]
  · simp only [S, ← mulVec_mulVec, hRej, hWej]
  · show (W * R) *ᵥ a = Pi.single i 1
    rw [← mulVec_mulVec, hRa]
    simp only [r, mulVec_mulVec, hWc, one_mulVec]
  · have hRc : R * Rᴴ = 1 := unitary_mul_conj hR
    have : Rᴴ *ᵥ r = a := by rw [← hRa, mulVec_mulVec, hR, one_mulVec]
    simp only [S, conjTranspose_mul, ← mulVec_mulVec]
    exact this

/-- **(9).**  If `S` is unitary with `S e_j = β` and `S^* e_i = a`, then
`(P²)_{ij} = ∑_k |S_{ik}|² |S_{kj}|² = ∑_k |a_k|² |β_k|²`. -/
theorem twoStep_P2_entry {S : Matrix n n ℂ} {i j : n} {a β : n → ℂ}
    (hSj : S *ᵥ Pi.single j 1 = β) (hSi : Sᴴ *ᵥ Pi.single i 1 = a) :
    ∑ k, Complex.normSq (S i k) * Complex.normSq (S k j) =
      ∑ k, Complex.normSq (a k) * Complex.normSq (β k) := by
  have hcol : ∀ k, S k j = β k := fun k => by
    rw [← hSj]; simp [mulVec, dotProduct, Pi.single_apply]
  have hrow : ∀ k, star (S i k) = a k := fun k => by
    rw [← hSi]; simp [mulVec, dotProduct, Pi.single_apply]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [hcol, ← hrow]
  simp

/-- **(9), the explicit value.**  With `a = β = b^{-1/2} 1_B` for a set `B` of size `b`,
`∑_k |a_k|² |β_k|² = 1/b`. -/
theorem twoStep_value (B : Finset n) (hB : B.Nonempty) :
    let a : n → ℂ := fun k => if k ∈ B then ((Real.sqrt B.card : ℝ) : ℂ)⁻¹ else 0
    ∑ k, Complex.normSq (a k) * Complex.normSq (a k) = 1 / B.card := by
  intro a
  have hb : (0 : ℝ) < B.card := by exact_mod_cast hB.card_pos
  have hval : ∀ k, Complex.normSq (a k) = if k ∈ B then 1 / (B.card : ℝ) else 0 := by
    intro k
    simp only [a]
    split_ifs
    · rw [Complex.normSq_inv, Complex.normSq_ofReal, Real.mul_self_sqrt hb.le, one_div]
    · simp
  simp only [hval, ite_mul, zero_mul, mul_ite, mul_zero]
  rw [Finset.sum_ite_mem, Finset.univ_inter,
    Finset.sum_congr rfl fun k hk => if_pos hk, Finset.sum_const, nsmul_eq_mul]
  field_simp

end Prescriptions

/-! ## §1: the positive companion (4) -/

section Companion

open scoped Matrix.Norms.L2Operator

variable {n : ℕ}

/-- The flat doubly stochastic matrix `J = n⁻¹ 𝟙𝟙ᵀ` (real version). -/
noncomputable def flatJR (n : ℕ) : Matrix (Fin n) (Fin n) ℝ := fun _ _ => (n : ℝ)⁻¹

lemma mul_flatJR {P : Matrix (Fin n) (Fin n) ℝ} (hrow : ∀ i, ∑ k, P i k = 1) :
    P * flatJR n = flatJR n := by
  ext i j; simp [mul_apply, flatJR, ← Finset.sum_mul, hrow]

lemma flatJR_mul {P : Matrix (Fin n) (Fin n) ℝ} (hcol : ∀ j, ∑ k, P k j = 1) :
    flatJR n * P = flatJR n := by
  ext i j; simp [mul_apply, flatJR, ← Finset.mul_sum, hcol]

lemma pow_mul_flatJR {P : Matrix (Fin n) (Fin n) ℝ} (hrow : ∀ i, ∑ k, P i k = 1) (h : ℕ) :
    P ^ h * flatJR n = flatJR n := by
  induction h with
  | zero => simp
  | succ h ih => rw [pow_succ, Matrix.mul_assoc, mul_flatJR hrow, ih]

/-- `(P - J)^h = P^h - J` for doubly stochastic `P` and `h ≥ 1`. -/
theorem sub_flatJR_pow {P : Matrix (Fin n) (Fin n) ℝ} (hrow : ∀ i, ∑ k, P i k = 1)
    (hcol : ∀ j, ∑ k, P k j = 1) (h : ℕ) (hh : 1 ≤ h) :
    (P - flatJR n) ^ h = P ^ h - flatJR n := by
  induction h, hh using Nat.le_induction with
  | base => simp
  | succ h hh ih =>
    have hJJ : flatJR n * flatJR n = flatJR n := by
      ext i j
      rcases Nat.eq_zero_or_pos n with h0 | h0
      · subst h0; exact Fin.elim0 i
      · simp [mul_apply, flatJR]; field_simp
    rw [pow_succ, ih, pow_succ, sub_mul, mul_sub, mul_sub, pow_mul_flatJR hrow,
      flatJR_mul hcol, hJJ]
    abel

lemma l2_one_le_one : ‖(1 : Matrix (Fin n) (Fin n) ℝ)‖ ≤ 1 := by
  rcases Nat.eq_zero_or_pos n with h0 | h0
  · subst h0; rw [Subsingleton.elim (1 : Matrix (Fin 0) (Fin 0) ℝ) 0, norm_zero]
    exact zero_le_one
  · rw [← diagonal_one, l2_opNorm_diagonal]
    exact (pi_norm_le_iff_of_nonneg zero_le_one).mpr fun i => by simp

/-- `|(A M B)_{ij}| ≤ ‖A_{i·}‖₂ ‖M‖ ‖B_{·j}‖₂`. -/
theorem entry_mul_mul_le (A M B : Matrix (Fin n) (Fin n) ℝ) (i j : Fin n) :
    |(A * M * B) i j| ≤
      Real.sqrt (∑ k, A i k ^ 2) * ‖M‖ * Real.sqrt (∑ k, B k j ^ 2) := by
  set b : Fin n → ℝ := fun k => B k j
  set w : Fin n → ℝ := M *ᵥ b
  have hentry : (A * M * B) i j = ∑ k, A i k * w k := by
    rw [Matrix.mul_assoc, mul_apply]
    simp only [w, b, mulVec, dotProduct, mul_apply]
  have hw : Real.sqrt (∑ k, w k ^ 2) ≤ ‖M‖ * Real.sqrt (∑ k, b k ^ 2) := by
    have h := l2_opNorm_mulVec M ((EuclideanSpace.equiv (Fin n) ℝ).symm b)
    simp only [EuclideanSpace.norm_eq, Real.norm_eq_abs, sq_abs] at h
    exact h
  have hcs : |∑ k, A i k * w k| ≤ Real.sqrt (∑ k, A i k ^ 2) * Real.sqrt (∑ k, w k ^ 2) := by
    rw [← Real.sqrt_mul (Finset.sum_nonneg fun k _ => sq_nonneg _)]
    apply Real.abs_le_sqrt
    exact Finset.sum_mul_sq_le_sq_mul_sq _ _ _
  rw [hentry]
  calc |∑ k, A i k * w k| ≤ Real.sqrt (∑ k, A i k ^ 2) * Real.sqrt (∑ k, w k ^ 2) := hcs
    _ ≤ Real.sqrt (∑ k, A i k ^ 2) * (‖M‖ * Real.sqrt (∑ k, b k ^ 2)) :=
        mul_le_mul_of_nonneg_left hw (Real.sqrt_nonneg _)
    _ = _ := by ring

lemma row_sq_sub_flat {P : Matrix (Fin n) (Fin n) ℝ} (hrow : ∀ i, ∑ k, P i k = 1) (i : Fin n) :
    ∑ k, (P - flatJR n) i k ^ 2 = ∑ k, P i k ^ 2 - 1 / n := by
  rcases Nat.eq_zero_or_pos n with h0 | h0
  · subst h0; exact Fin.elim0 i
  have hn : (n : ℝ) ≠ 0 := by exact_mod_cast h0.ne'
  simp only [Matrix.sub_apply, flatJR, sub_sq, Finset.sum_add_distrib, Finset.sum_sub_distrib,
    ← Finset.sum_mul, ← Finset.mul_sum, hrow, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul]
  field_simp; ring

lemma col_sq_sub_flat {P : Matrix (Fin n) (Fin n) ℝ} (hcol : ∀ j, ∑ k, P k j = 1) (j : Fin n) :
    ∑ k, (P - flatJR n) k j ^ 2 = ∑ k, P k j ^ 2 - 1 / n := by
  rcases Nat.eq_zero_or_pos n with h0 | h0
  · subst h0; exact Fin.elim0 j
  have hn : (n : ℝ) ≠ 0 := by exact_mod_cast h0.ne'
  simp only [Matrix.sub_apply, flatJR, sub_sq, Finset.sum_add_distrib, Finset.sum_sub_distrib,
    ← Finset.sum_mul, ← Finset.mul_sum, hcol, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul]
  field_simp; ring

/-- **(4), first inequality.**  For a doubly stochastic `P` and `h ≥ 2`,
`|(P^h)_{ij} - 1/n| ≤ ρ^{h-2} √((∑_k P_ik² - 1/n)(∑_k P_kj² - 1/n))`, `ρ = ‖P - J‖`. -/
theorem doublyStochastic_power_entry {P : Matrix (Fin n) (Fin n) ℝ}
    (hrow : ∀ i, ∑ k, P i k = 1) (hcol : ∀ j, ∑ k, P k j = 1) (h : ℕ) (hh : 2 ≤ h)
    (i j : Fin n) :
    |(P ^ h) i j - 1 / n| ≤ ‖P - flatJR n‖ ^ (h - 2) *
      Real.sqrt ((∑ k, P i k ^ 2 - 1 / n) * (∑ k, P k j ^ 2 - 1 / n)) := by
  have hpow : (P - flatJR n) ^ h =
      (P - flatJR n) * (P - flatJR n) ^ (h - 2) * (P - flatJR n) := by
    rw [← pow_succ', ← pow_succ]; congr 1; omega
  have hentry : (P ^ h) i j - 1 / n = ((P - flatJR n) ^ h) i j := by
    rw [sub_flatJR_pow hrow hcol h (by omega)]; simp [flatJR]
  have hnorm : ‖(P - flatJR n) ^ (h - 2)‖ ≤ ‖P - flatJR n‖ ^ (h - 2) := by
    rcases Nat.eq_zero_or_pos (h - 2) with h0 | h0
    · rw [h0, pow_zero, pow_zero]; exact l2_one_le_one
    · exact norm_pow_le' _ h0
  rw [hentry, hpow]
  refine (entry_mul_mul_le _ _ _ i j).trans ?_
  rw [row_sq_sub_flat hrow, col_sq_sub_flat hcol]
  have hs1 : 0 ≤ ∑ k, P i k ^ 2 - 1 / n := by
    rw [← row_sq_sub_flat hrow]; exact Finset.sum_nonneg fun k _ => sq_nonneg _
  rw [Real.sqrt_mul hs1]
  calc Real.sqrt (∑ k, P i k ^ 2 - 1 / n) * ‖(P - flatJR n) ^ (h - 2)‖ *
        Real.sqrt (∑ k, P k j ^ 2 - 1 / n)
      ≤ Real.sqrt (∑ k, P i k ^ 2 - 1 / n) * ‖P - flatJR n‖ ^ (h - 2) *
        Real.sqrt (∑ k, P k j ^ 2 - 1 / n) := by gcongr
    _ = _ := by ring

/-- **(4), second inequality.**  If moreover `0 ≤ P_kl ≤ δ`, then
`|(P^h)_{ij} - 1/n| ≤ ρ^{h-2} (δ - 1/n)`. -/
theorem doublyStochastic_power_entry_delta {P : Matrix (Fin n) (Fin n) ℝ}
    (hrow : ∀ i, ∑ k, P i k = 1) (hcol : ∀ j, ∑ k, P k j = 1) (hnn : ∀ k l, 0 ≤ P k l)
    {δ : ℝ} (hδ : ∀ k l, P k l ≤ δ) (h : ℕ) (hh : 2 ≤ h) (i j : Fin n) :
    |(P ^ h) i j - 1 / n| ≤ ‖P - flatJR n‖ ^ (h - 2) * (δ - 1 / n) := by
  refine (doublyStochastic_power_entry hrow hcol h hh i j).trans ?_
  gcongr
  have hr : ∑ k, P i k ^ 2 ≤ δ := by
    calc ∑ k, P i k ^ 2 ≤ ∑ k, δ * P i k :=
          Finset.sum_le_sum fun k _ => by rw [sq]; exact mul_le_mul_of_nonneg_right (hδ i k) (hnn i k)
      _ = δ := by rw [← Finset.mul_sum, hrow, mul_one]
  have hc : ∑ k, P k j ^ 2 ≤ δ := by
    calc ∑ k, P k j ^ 2 ≤ ∑ k, δ * P k j :=
          Finset.sum_le_sum fun k _ => by rw [sq]; exact mul_le_mul_of_nonneg_right (hδ k j) (hnn k j)
      _ = δ := by rw [← Finset.mul_sum, hcol, mul_one]
  have hr0 : 0 ≤ ∑ k, P i k ^ 2 - 1 / n := by
    rw [← row_sq_sub_flat hrow]; exact Finset.sum_nonneg fun k _ => sq_nonneg _
  have hc0 : 0 ≤ ∑ k, P k j ^ 2 - 1 / n := by
    rw [← col_sq_sub_flat hcol]; exact Finset.sum_nonneg fun k _ => sq_nonneg _
  rw [Real.sqrt_le_left (by linarith)]
  nlinarith

end Companion

end Bgs.Mathlib
