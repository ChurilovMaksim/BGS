module
public import Mathlib
@[expose] public section

/-!
# Exact coherence memory and its singular-norm plateau (BGS-TRACE-082)

Let `U` be an `N × N` unitary, `𝒯 X = U X U*`, `𝒟` the diagonal projection and
`𝒬 = 1 - 𝒟` on `M_N(ℂ)` with the Hilbert–Schmidt inner product.

* **M1 (return memory).** For a diagonal start `X₀`, with `aₙ = 𝒟 𝒯ⁿ X₀`,
  `aₙ₊₁ = P aₙ + ∑_{s<n} 𝓛 𝓔^{n-1-s} 𝓒 a_s`, where `P = 𝒟𝒯𝒟`, `𝓛 = 𝒟𝒯𝒬`,
  `𝓒 = 𝒬𝒯𝒟`, `𝓔 = 𝒬𝒯𝒬`.  We prove this for arbitrary complementary
  idempotents on an arbitrary module (`return_memory_recurrence`), and
  identify `𝒟𝒯𝒟` with the unistochastic matrix `P(U)_{ik} = |U_{ik}|²`
  (`diag_conj_diagonal`, `unistochastic_row_sum`, `unistochastic_col_sum`).
* **M2 (plateau).** For `N ≥ 2` and `0 ≤ r < N`, `‖𝓔^r‖_{HS→HS} = 1`
  (`coherence_plateau_hs`, `coherence_plateau_opNorm`).
-/

open Matrix BigOperators

namespace Bgs.Mathlib

/-! ## M1: abstract block recurrence -/

section Recurrence

variable {R V : Type*} [CommRing R] [AddCommGroup V] [Module R V]

/-- The block recurrence behind the return-memory identity M1.  `T` is any
endomorphism, `D` any idempotent and `Q = 1 - D`.  For any start `x₀`, the coherent
part `Q Tⁿ x₀` of a diagonal start is exactly the memory sum. -/
theorem coherent_part_formula (T D : Module.End R V) (hD : D * D = D)
    (x₀ : V) (hx₀ : D x₀ = x₀) (n : ℕ) :
    (1 - D) ((T ^ n) x₀) =
      ∑ s ∈ Finset.range n,
        (((1 - D) * T * (1 - D)) ^ (n - 1 - s)) (((1 - D) * T * D) (D ((T ^ s) x₀))) := by
  set Q : Module.End R V := 1 - D with hQdef
  set E : Module.End R V := Q * T * Q
  set C : Module.End R V := Q * T * D
  have hQQ : Q * Q = Q := by
    simp only [hQdef]; rw [sub_mul, one_mul, mul_sub, mul_one, hD, sub_self, sub_zero]
  have hCD : C * D = C := by simp only [C, mul_assoc, hD]
  have hEQ : E * Q = E := by simp only [E, mul_assoc, hQQ]
  have hsplitQ : Q * T = C + E := by simp only [C, E, hQdef]; noncomm_ring
  induction n with
  | zero =>
    have : Q x₀ = 0 := by
      rw [hQdef, LinearMap.sub_apply, Module.End.one_apply, hx₀, sub_self]
    simpa using this
  | succ n ih =>
    have step : Q ((T ^ (n + 1)) x₀) = C (D ((T ^ n) x₀)) + E (Q ((T ^ n) x₀)) := by
      rw [pow_succ', Module.End.mul_apply T, ← Module.End.mul_apply C D, hCD,
        ← Module.End.mul_apply E Q, hEQ, ← LinearMap.add_apply, ← hsplitQ, Module.End.mul_apply]
    rw [step, ih, map_sum, Finset.sum_range_succ, add_comm]
    simp only [Nat.add_sub_cancel, Nat.sub_self, pow_zero, Module.End.one_apply]
    congr 1
    apply Finset.sum_congr rfl
    intro s hs
    have hs' : n - s = (n - 1 - s) + 1 := by
      have := Finset.mem_range.1 hs; omega
    rw [hs', pow_succ', Module.End.mul_apply E (E ^ (n - 1 - s))]

/-- **M1, return-memory recurrence.**  With `aₙ = D Tⁿ x₀` (`D x₀ = x₀`),
`aₙ₊₁ = (D T D) aₙ + ∑_{s<n} (D T Q) (Q T Q)^{n-1-s} (Q T D) a_s`. -/
theorem return_memory_recurrence (T D : Module.End R V) (hD : D * D = D)
    (x₀ : V) (hx₀ : D x₀ = x₀) (n : ℕ) :
    D ((T ^ (n + 1)) x₀) =
      (D * T * D) (D ((T ^ n) x₀)) +
      ∑ s ∈ Finset.range n,
        (D * T * (1 - D)) ((((1 - D) * T * (1 - D)) ^ (n - 1 - s))
          (((1 - D) * T * D) (D ((T ^ s) x₀)))) := by
  have hQQ : (1 - D) * (1 - D) = 1 - D := by
    rw [sub_mul, one_mul, mul_sub, mul_one, hD, sub_self, sub_zero]
  have hPD : D * T * D * D = D * T * D := by simp only [mul_assoc, hD]
  have hLQ : D * T * (1 - D) * (1 - D) = D * T * (1 - D) := by simp only [mul_assoc, hQQ]
  have hsplit : D * T = D * T * D + D * T * (1 - D) := by noncomm_ring
  have key : ∀ v, (D * T) v = (D * T * D) (D v) + (D * T * (1 - D)) ((1 - D) v) := by
    intro v
    rw [← Module.End.mul_apply, ← Module.End.mul_apply, hPD, hLQ, ← LinearMap.add_apply,
      ← hsplit]
  rw [← map_sum, ← coherent_part_formula T D hD x₀ hx₀ n, pow_succ', Module.End.mul_apply,
    ← Module.End.mul_apply D T, key]

end Recurrence

/-! ## Concrete matrix setting -/

variable {N : ℕ}

/-- Orthogonal projection onto diagonal matrices. -/
def diagPart (X : Matrix (Fin N) (Fin N) ℂ) : Matrix (Fin N) (Fin N) ℂ :=
  Matrix.diagonal fun i => X i i

/-- Orthogonal projection onto off-diagonal matrices, `𝒬 = 1 - 𝒟`. -/
def offPart (X : Matrix (Fin N) (Fin N) ℂ) : Matrix (Fin N) (Fin N) ℂ :=
  X - diagPart X

/-- The adjoint action `𝒯 X = U X U*`. -/
def conjU (U X : Matrix (Fin N) (Fin N) ℂ) : Matrix (Fin N) (Fin N) ℂ :=
  U * X * Uᴴ

/-- The coherence block `𝓔 = 𝒬 𝒯 𝒬`. -/
def cohE (U X : Matrix (Fin N) (Fin N) ℂ) : Matrix (Fin N) (Fin N) ℂ :=
  offPart (conjU U (offPart X))

/-- Squared Hilbert–Schmidt (Frobenius) norm. -/
noncomputable def hs2 (X : Matrix (Fin N) (Fin N) ℂ) : ℝ :=
  ∑ i, ∑ j, ‖X i j‖ ^ 2

theorem offPart_apply (X : Matrix (Fin N) (Fin N) ℂ) (i j : Fin N) :
    offPart X i j = if i = j then 0 else X i j := by
  by_cases h : i = j
  · subst h; simp [offPart, diagPart]
  · simp [offPart, diagPart, h]

/-- **`𝒟𝒯𝒟 = P(U)`.**  The diagonal of `U diag(x) U*` is `P(U) x` with
`P(U)_{ik} = |U_{ik}|²`. -/
theorem diag_conj_diagonal (U : Matrix (Fin N) (Fin N) ℂ) (x : Fin N → ℂ) (i : Fin N) :
    conjU U (Matrix.diagonal x) i i = ∑ k, ((‖U i k‖ ^ 2 : ℝ) : ℂ) * x k := by
  simp only [conjU, Matrix.mul_apply, Matrix.diagonal_apply, Matrix.conjTranspose_apply,
    mul_ite, mul_zero, Finset.sum_ite_eq', Finset.mem_univ, ite_true]
  apply Finset.sum_congr rfl
  intro k _
  rw [Complex.sq_norm, ← Complex.mul_conj]
  simp only [RCLike.star_def]
  ring

theorem hs2_eq_re_trace (X : Matrix (Fin N) (Fin N) ℂ) :
    hs2 X = (Matrix.trace (Xᴴ * X)).re := by
  simp only [hs2, Matrix.trace, Matrix.diag, Matrix.mul_apply, Matrix.conjTranspose_apply,
    Complex.re_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl; intro i _
  apply Finset.sum_congr rfl; intro j _
  rw [RCLike.star_def, mul_comm, Complex.mul_conj, Complex.normSq_eq_norm_sq]
  rw [Complex.ofReal_re]

theorem hs2_nonneg (X : Matrix (Fin N) (Fin N) ℂ) : 0 ≤ hs2 X := by
  unfold hs2; positivity

theorem hs2_eq_zero_iff (X : Matrix (Fin N) (Fin N) ℂ) : hs2 X = 0 ↔ X = 0 := by
  unfold hs2
  rw [Finset.sum_eq_zero_iff_of_nonneg (fun _ _ => by positivity)]
  constructor
  · intro h; ext i j
    have := (Finset.sum_eq_zero_iff_of_nonneg (fun _ _ => by positivity)).1
      (h i (Finset.mem_univ _)) j (Finset.mem_univ _)
    simpa using this
  · rintro rfl; simp

/-- Unitary invariance of the Hilbert–Schmidt norm under `𝒯`. -/
theorem hs2_conjU {U : Matrix (Fin N) (Fin N) ℂ} (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ)
    (X : Matrix (Fin N) (Fin N) ℂ) : hs2 (conjU U X) = hs2 X := by
  have h1 : Uᴴ * U = 1 := Matrix.mem_unitaryGroup_iff'.1 hU
  rw [hs2_eq_re_trace, hs2_eq_re_trace]
  congr 1
  simp only [conjU, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  calc Matrix.trace (U * (Xᴴ * Uᴴ) * (U * X * Uᴴ))
      = Matrix.trace (U * (Xᴴ * (Uᴴ * U) * X) * Uᴴ) := by simp only [Matrix.mul_assoc]
    _ = Matrix.trace (Uᴴ * (U * (Xᴴ * (Uᴴ * U) * X))) := Matrix.trace_mul_comm _ _
    _ = Matrix.trace (Xᴴ * X) := by
        rw [← Matrix.mul_assoc Uᴴ, h1, Matrix.one_mul, Matrix.mul_one]

/-- `𝒬` is a Hilbert–Schmidt contraction. -/
theorem hs2_offPart_le (X : Matrix (Fin N) (Fin N) ℂ) : hs2 (offPart X) ≤ hs2 X := by
  unfold hs2
  apply Finset.sum_le_sum; intro i _
  apply Finset.sum_le_sum; intro j _
  rw [offPart_apply]
  split_ifs <;> simp

/-- `𝓔` is a Hilbert–Schmidt contraction. -/
theorem hs2_cohE_le {U : Matrix (Fin N) (Fin N) ℂ} (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ)
    (X : Matrix (Fin N) (Fin N) ℂ) : hs2 (cohE U X) ≤ hs2 X := by
  unfold cohE
  calc hs2 (offPart (conjU U (offPart X))) ≤ hs2 (conjU U (offPart X)) := hs2_offPart_le _
    _ = hs2 (offPart X) := hs2_conjU hU _
    _ ≤ hs2 X := hs2_offPart_le _

theorem hs2_cohE_iterate_le {U : Matrix (Fin N) (Fin N) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ) (r : ℕ) (X : Matrix (Fin N) (Fin N) ℂ) :
    hs2 ((cohE U)^[r] X) ≤ hs2 X := by
  induction r generalizing X with
  | zero => simp
  | succ r ih =>
    rw [Function.iterate_succ_apply']
    exact (hs2_cohE_le hU _).trans (ih X)

/-- Unistochasticity: rows of `P(U)` sum to one. -/
theorem unistochastic_row_sum {U : Matrix (Fin N) (Fin N) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ) (i : Fin N) :
    ∑ k, ‖U i k‖ ^ 2 = 1 := by
  have h : U * Uᴴ = 1 := Matrix.mem_unitaryGroup_iff.1 hU
  have := congrFun (congrFun h i) i
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.one_apply_eq] at this
  have h2 : ((∑ k, ‖U i k‖ ^ 2 : ℝ) : ℂ) = 1 := by
    rw [← this]; push_cast
    apply Finset.sum_congr rfl; intro k _
    rw [RCLike.star_def, Complex.mul_conj']
  exact_mod_cast h2

/-- Unistochasticity: columns of `P(U)` sum to one. -/
theorem unistochastic_col_sum {U : Matrix (Fin N) (Fin N) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ) (k : Fin N) :
    ∑ i, ‖U i k‖ ^ 2 = 1 := by
  have h : Uᴴ * U = 1 := Matrix.mem_unitaryGroup_iff'.1 hU
  have := congrFun (congrFun h k) k
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.one_apply_eq] at this
  have h2 : ((∑ i, ‖U i k‖ ^ 2 : ℝ) : ℂ) = 1 := by
    rw [← this]; push_cast
    apply Finset.sum_congr rfl; intro i _
    rw [RCLike.star_def, mul_comm, Complex.mul_conj']
  exact_mod_cast h2

/-! ## M2: the plateau -/

/-- `𝒯` as a `ℂ`-linear map. -/
def conjL (U : Matrix (Fin N) (Fin N) ℂ) :
    Matrix (Fin N) (Fin N) ℂ →ₗ[ℂ] Matrix (Fin N) (Fin N) ℂ where
  toFun X := conjU U X
  map_add' X Y := by simp [conjU, Matrix.mul_add, Matrix.add_mul]
  map_smul' c X := by simp [conjU]

theorem conjL_pow_apply (U : Matrix (Fin N) (Fin N) ℂ) (j : ℕ) (X : Matrix (Fin N) (Fin N) ℂ) :
    (conjL U ^ j) X = (conjU U)^[j] X := by
  rw [Module.End.pow_apply]; rfl

theorem trace_conjU {U : Matrix (Fin N) (Fin N) ℂ} (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ)
    (X : Matrix (Fin N) (Fin N) ℂ) : (conjU U X).trace = X.trace := by
  have h1 : Uᴴ * U = 1 := Matrix.mem_unitaryGroup_iff'.1 hU
  rw [conjU, Matrix.trace_mul_cycle, h1, Matrix.one_mul]

theorem trace_conjU_iterate {U : Matrix (Fin N) (Fin N) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ) (j : ℕ) (X : Matrix (Fin N) (Fin N) ℂ) :
    ((conjU U)^[j] X).trace = X.trace := by
  induction j with
  | zero => rfl
  | succ j ih => rw [Function.iterate_succ_apply', trace_conjU hU, ih]

theorem hs2_conjU_iterate {U : Matrix (Fin N) (Fin N) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ) (j : ℕ) (X : Matrix (Fin N) (Fin N) ℂ) :
    hs2 ((conjU U)^[j] X) = hs2 X := by
  induction j with
  | zero => rfl
  | succ j ih => rw [Function.iterate_succ_apply', hs2_conjU hU, ih]

/-- The dimension count of M2: there is a nonzero traceless `X` such that
`𝒯ʲ X` is off-diagonal for every `j ≤ r`, provided `r < N`, `N ≥ 2`. -/
theorem exists_offdiag_orbit {n : ℕ} (hn : 1 ≤ n) {U : Matrix (Fin (n + 1)) (Fin (n + 1)) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin (n + 1)) ℂ) {r : ℕ} (hr : r < n + 1) :
    ∃ X : Matrix (Fin (n + 1)) (Fin (n + 1)) ℂ, X ≠ 0 ∧
      ∀ j ≤ r, offPart ((conjU U)^[j] X) = (conjU U)^[j] X := by
  let G : Matrix (Fin (n + 1)) (Fin (n + 1)) ℂ →ₗ[ℂ] ℂ × (Fin (r + 1) → Fin n → ℂ) :=
    { toFun := fun X => (X.trace, fun j i => ((conjL U ^ (j : ℕ)) X) i.castSucc i.castSucc)
      map_add' := fun X Y => by
        ext <;> simp [Matrix.trace_add]
      map_smul' := fun c X => by
        ext <;> simp [Matrix.trace_smul] }
  have hdim : Module.finrank ℂ (ℂ × (Fin (r + 1) → Fin n → ℂ)) <
      Module.finrank ℂ (Matrix (Fin (n + 1)) (Fin (n + 1)) ℂ) := by
    simp only [Module.finrank_prod, Module.finrank_self, Module.finrank_pi_fintype,
      Fintype.card_fin, Module.finrank_matrix, Finset.sum_const, Finset.card_univ, smul_eq_mul]
    have : (r + 1) * n ≤ (n + 1) * n := Nat.mul_le_mul_right _ hr
    nlinarith
  obtain ⟨X, hXker, hX0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot (G.ker_ne_bot_of_finrank_lt hdim)
  refine ⟨X, hX0, fun j hj => ?_⟩
  rw [LinearMap.mem_ker] at hXker
  have htr : X.trace = 0 := congrArg Prod.fst hXker
  have hdiag : ∀ i : Fin n, ((conjU U)^[j] X) i.castSucc i.castSucc = 0 := by
    intro i
    have := congrFun (congrFun (congrArg Prod.snd hXker) ⟨j, by omega⟩) i
    simpa [G, conjL_pow_apply] using this
  have hlast : ((conjU U)^[j] X) (Fin.last n) (Fin.last n) = 0 := by
    have h := trace_conjU_iterate hU j X
    rw [htr, Matrix.trace, Fin.sum_univ_castSucc] at h
    simp only [Matrix.diag] at h
    rw [Finset.sum_eq_zero (fun i _ => hdiag i), zero_add] at h
    exact h
  ext a b
  rw [offPart_apply]
  split_ifs with hab
  · subst hab
    refine (Fin.lastCases ?_ (fun i => ?_) a)
    · exact hlast.symm
    · exact (hdiag i).symm
  · rfl

/-- **M2 (Hilbert–Schmidt form).**  For every unitary `U` of size `N ≥ 2` and
every `0 ≤ r < N`, `𝓔^r` is a Hilbert–Schmidt contraction that attains norm one:
there is a nonzero off-diagonal `X` with `‖𝓔^r X‖_HS = ‖X‖_HS`. -/
theorem coherence_plateau_hs {N : ℕ} (hN : 2 ≤ N) {U : Matrix (Fin N) (Fin N) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ) {r : ℕ} (hr : r < N) :
    (∀ Y, hs2 ((cohE U)^[r] Y) ≤ hs2 Y) ∧
      ∃ X : Matrix (Fin N) (Fin N) ℂ, X ≠ 0 ∧ offPart X = X ∧
        hs2 ((cohE U)^[r] X) = hs2 X := by
  refine ⟨hs2_cohE_iterate_le hU r, ?_⟩
  obtain ⟨n, rfl⟩ : ∃ n, N = n + 1 := ⟨N - 1, by omega⟩
  obtain ⟨X, hX0, hoff⟩ := exists_offdiag_orbit (by omega) hU hr
  refine ⟨X, hX0, by simpa using hoff 0 (Nat.zero_le _), ?_⟩
  have key : ∀ j ≤ r, (cohE U)^[j] X = (conjU U)^[j] X := by
    intro j hj
    induction j with
    | zero => rfl
    | succ j ih =>
      rw [Function.iterate_succ_apply', Function.iterate_succ_apply', ih (by omega), cohE,
        hoff j (by omega), ← Function.iterate_succ_apply' (conjU U), hoff (j + 1) hj]
  rw [key r le_rfl, hs2_conjU_iterate hU]

/-! ## M2 as an operator-norm statement -/

theorem offPart_add (X Y : Matrix (Fin N) (Fin N) ℂ) :
    offPart (X + Y) = offPart X + offPart Y := by
  ext i j; simp only [offPart_apply, Matrix.add_apply]; split_ifs <;> simp

theorem offPart_smul (c : ℂ) (X : Matrix (Fin N) (Fin N) ℂ) :
    offPart (c • X) = c • offPart X := by
  ext i j; simp only [offPart_apply, Matrix.smul_apply]; split_ifs <;> simp

/-- The coherence block `𝓔 = 𝒬𝒯𝒬` as a `ℂ`-linear map on `M_N(ℂ)`. -/
def cohEL (U : Matrix (Fin N) (Fin N) ℂ) :
    Matrix (Fin N) (Fin N) ℂ →ₗ[ℂ] Matrix (Fin N) (Fin N) ℂ where
  toFun := cohE U
  map_add' X Y := by
    simp [cohE, offPart_add, conjU, Matrix.mul_add, Matrix.add_mul]
  map_smul' c X := by
    simp [cohE, offPart_smul, conjU]

theorem cohEL_pow_apply (U : Matrix (Fin N) (Fin N) ℂ) (r : ℕ) (X : Matrix (Fin N) (Fin N) ℂ) :
    (cohEL U ^ r) X = (cohE U)^[r] X := by
  rw [Module.End.pow_apply]; rfl

section OpNorm

/-- `M_N(ℂ)` equipped with the Hilbert–Schmidt (Frobenius) norm. -/
def HSMat (N : ℕ) := Matrix (Fin N) (Fin N) ℂ

noncomputable instance (N : ℕ) : NormedAddCommGroup (HSMat N) :=
  Matrix.frobeniusNormedAddCommGroup
noncomputable instance (N : ℕ) : NormedSpace ℂ (HSMat N) := Matrix.frobeniusNormedSpace
instance (N : ℕ) : FiniteDimensional ℂ (HSMat N) :=
  inferInstanceAs (FiniteDimensional ℂ (Matrix (Fin N) (Fin N) ℂ))

/-- A linear map on matrices viewed as a bounded operator on Hilbert–Schmidt space. -/
noncomputable def toHS (f : Matrix (Fin N) (Fin N) ℂ →ₗ[ℂ] Matrix (Fin N) (Fin N) ℂ) :
    HSMat N →L[ℂ] HSMat N :=
  LinearMap.toContinuousLinearMap f

/-- The identity identification of matrices with Hilbert–Schmidt space. -/
def HSMat.of : Matrix (Fin N) (Fin N) ℂ ≃ HSMat N := Equiv.refl _

theorem toHS_of (f : Matrix (Fin N) (Fin N) ℂ →ₗ[ℂ] Matrix (Fin N) (Fin N) ℂ)
    (X : Matrix (Fin N) (Fin N) ℂ) : toHS f (HSMat.of X) = HSMat.of (f X) := by
  unfold toHS; rfl

theorem norm_HSMat_of (X : Matrix (Fin N) (Fin N) ℂ) :
    ‖HSMat.of X‖ = Real.sqrt (hs2 X) := by
  have h : ‖HSMat.of X‖ = (∑ i, ∑ j, ‖X i j‖ ^ (2 : ℝ)) ^ (1 / 2 : ℝ) :=
    Matrix.frobenius_norm_def X
  rw [h, Real.sqrt_eq_rpow]
  unfold hs2
  simp only [Real.rpow_two]

/-- **M2 (operator-norm form).**  On Hilbert–Schmidt space,
`‖𝓔^r‖_{HS→HS} = 1` for every unitary `U`, `N ≥ 2`, `0 ≤ r < N`. -/
theorem coherence_plateau_opNorm {N : ℕ} (hN : 2 ≤ N) {U : Matrix (Fin N) (Fin N) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (Fin N) ℂ) {r : ℕ} (hr : r < N) :
    ‖toHS (cohEL U ^ r)‖ = 1 := by
  obtain ⟨hle, X, hX0, -, hXeq⟩ := coherence_plateau_hs hN hU hr
  apply ContinuousLinearMap.opNorm_eq_of_bounds zero_le_one
  · intro Y
    obtain ⟨Y, rfl⟩ := HSMat.of.surjective Y
    rw [toHS_of, cohEL_pow_apply, one_mul, norm_HSMat_of, norm_HSMat_of]
    exact Real.sqrt_le_sqrt (hle Y)
  · intro M _ hM
    have h := hM (HSMat.of X)
    rw [toHS_of, cohEL_pow_apply, norm_HSMat_of, norm_HSMat_of, hXeq] at h
    have hpos : 0 < Real.sqrt (hs2 X) := by
      apply Real.sqrt_pos.2
      rcases (hs2_nonneg X).lt_or_eq with h' | h'
      · exact h'
      · exact absurd ((hs2_eq_zero_iff X).1 h'.symm) hX0
    nlinarith

end OpNorm

#print axioms coherent_part_formula
#print axioms return_memory_recurrence
#print axioms offPart_apply
#print axioms diag_conj_diagonal
#print axioms hs2_eq_re_trace
#print axioms hs2_nonneg
#print axioms hs2_eq_zero_iff
#print axioms hs2_conjU
#print axioms hs2_offPart_le
#print axioms hs2_cohE_le
#print axioms hs2_cohE_iterate_le
#print axioms unistochastic_row_sum
#print axioms unistochastic_col_sum
#print axioms conjL_pow_apply
#print axioms trace_conjU
#print axioms trace_conjU_iterate
#print axioms hs2_conjU_iterate
#print axioms exists_offdiag_orbit
#print axioms coherence_plateau_hs
#print axioms offPart_add
#print axioms offPart_smul
#print axioms cohEL_pow_apply
#print axioms toHS_of
#print axioms norm_HSMat_of
#print axioms coherence_plateau_opNorm
end Bgs.Mathlib
