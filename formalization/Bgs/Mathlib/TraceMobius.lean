module
public import Bgs.Mathlib.TwoClock
@[expose] public section

/-!
# Partition–Möbius formula for distinct-index spectral sums (BGS-TRACE-001)

Source: `mathematics/trace-bridge/trace_to_local_statistics_bridge.md`, Theorem 1.

For eigenphases `x : Fin N → ℝ` put `T(m) = ∑_j e^{2πi m x_j}` (`traceZ`) and
`D(m_1, …, m_k) = ∑_{j_1, …, j_k distinct} e^{2πi ∑_a m_a x_{j_a}}`.
Theorem 1 states `D(m) = ∑_{π ∈ Π_k} μ(π) ∏_{B ∈ π} T(∑_{a ∈ B} m_a)` with
`μ(π) = ∏_B (-1)^{|B|-1} (|B|-1)!`.  We formalize:

* `distinct_sum_two` — `k = 2`: `D(m₁, m₂) = T(m₁) T(m₂) - T(m₁ + m₂)`;
* `distinct_sum_three` — `k = 3`:
  `D = T₁T₂T₃ - T₁₂T₃ - T₁₃T₂ - T₂₃T₁ + 2 T₁₂₃`;
* `distinct_sum_cons` — the general recursion that generates Theorem 1 for every `k`:
  `D(m₀, m) = T(m₀) D(m) - ∑_{a} D(m + m₀ e_a)`, where `D` is the sum over injective
  index maps `Fin k → Fin N` (`distinctSum`).

The identities are deterministic and hold for every finite spectrum; the zero-sum
condition of the note is not needed.
-/

open Real Complex BigOperators Finset

namespace Bgs.Mathlib

/-- `e(m x_j) = e^{2πi m x_j}`. -/
noncomputable def ephase {N : ℕ} (x : Fin N → ℝ) (m : ℤ) (j : Fin N) : ℂ :=
  Complex.exp (2 * π * Complex.I * m * x j)

lemma ephase_add {N : ℕ} (x : Fin N → ℝ) (m m' : ℤ) (j : Fin N) :
    ephase x m j * ephase x m' j = ephase x (m + m') j := by
  rw [ephase, ephase, ephase, ← Complex.exp_add]; congr 1; push_cast; ring

lemma traceZ_eq_sum_ephase {N : ℕ} (x : Fin N → ℝ) (m : ℤ) :
    traceZ x m = ∑ j, ephase x m j := rfl

/-- `D(m₁, m₂)`: the sum over ordered pairs of distinct indices. -/
noncomputable def distinctSum2 {N : ℕ} (x : Fin N → ℝ) (m₁ m₂ : ℤ) : ℂ :=
  ∑ j₁, ∑ j₂, if j₁ ≠ j₂ then ephase x m₁ j₁ * ephase x m₂ j₂ else 0

/-- `D(m₁, m₂, m₃)`: the sum over ordered triples of distinct indices. -/
noncomputable def distinctSum3 {N : ℕ} (x : Fin N → ℝ) (m₁ m₂ m₃ : ℤ) : ℂ :=
  ∑ j₁, ∑ j₂, ∑ j₃, if j₁ ≠ j₂ ∧ j₁ ≠ j₃ ∧ j₂ ≠ j₃ then
    ephase x m₁ j₁ * ephase x m₂ j₂ * ephase x m₃ j₃ else 0

/-- **TRACE-001, `k = 2`.** -/
theorem distinct_sum_two {N : ℕ} (x : Fin N → ℝ) (m₁ m₂ : ℤ) :
    distinctSum2 x m₁ m₂ = traceZ x m₁ * traceZ x m₂ - traceZ x (m₁ + m₂) := by
  have hpt : ∀ j₁ j₂ : Fin N, (if j₁ ≠ j₂ then ephase x m₁ j₁ * ephase x m₂ j₂ else 0) =
      ephase x m₁ j₁ * ephase x m₂ j₂ - if j₁ = j₂ then ephase x m₁ j₁ * ephase x m₂ j₂ else 0 := by
    intro j₁ j₂; by_cases h : j₁ = j₂ <;> simp [h]
  simp only [distinctSum2, hpt, Finset.sum_sub_distrib, Finset.sum_ite_eq, Finset.mem_univ,
    ite_true, traceZ_eq_sum_ephase, Finset.sum_mul_sum, ephase_add]

/-- **TRACE-001, `k = 3`.** -/
theorem distinct_sum_three {N : ℕ} (x : Fin N → ℝ) (m₁ m₂ m₃ : ℤ) :
    distinctSum3 x m₁ m₂ m₃ =
      traceZ x m₁ * traceZ x m₂ * traceZ x m₃
        - traceZ x (m₁ + m₂) * traceZ x m₃
        - traceZ x (m₁ + m₃) * traceZ x m₂
        - traceZ x (m₂ + m₃) * traceZ x m₁
        + 2 * traceZ x (m₁ + m₂ + m₃) := by
  unfold distinctSum3
  simp only [traceZ_eq_sum_ephase, ← ephase_add]
  set f₁ := ephase x m₁
  set f₂ := ephase x m₂
  set f₃ := ephase x m₃
  have hpt : ∀ j₁ j₂ j₃ : Fin N,
      (if j₁ ≠ j₂ ∧ j₁ ≠ j₃ ∧ j₂ ≠ j₃ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0) =
        f₁ j₁ * f₂ j₂ * f₃ j₃
          - (if j₁ = j₂ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0)
          - (if j₁ = j₃ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0)
          - (if j₂ = j₃ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0)
          + 2 * (if j₁ = j₂ ∧ j₂ = j₃ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0) := by
    intro j₁ j₂ j₃
    by_cases h12 : j₁ = j₂ <;> by_cases h13 : j₁ = j₃ <;> by_cases h23 : j₂ = j₃ <;>
      (simp_all; try ring)
  have h0 : ∑ j₁, ∑ j₂, ∑ j₃, f₁ j₁ * f₂ j₂ * f₃ j₃ =
      (∑ j, f₁ j) * (∑ j, f₂ j) * ∑ j, f₃ j := by
    rw [Finset.sum_mul_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [Finset.mul_sum]
  have h12 : ∑ j₁ : Fin N, ∑ j₂, ∑ j₃, (if j₁ = j₂ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0) =
      (∑ j, f₁ j * f₂ j) * ∑ j, f₃ j := by
    simp only [← Finset.mul_sum, Finset.sum_ite_irrel, Finset.sum_const_zero,
      Finset.sum_ite_eq, Finset.mem_univ, ite_true, Finset.sum_mul]
  have h13 : ∑ j₁ : Fin N, ∑ j₂, ∑ j₃, (if j₁ = j₃ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0) =
      (∑ j, f₁ j * f₃ j) * ∑ j, f₂ j := by
    simp only [Finset.sum_ite_eq, Finset.mem_univ, ite_true]
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by ring
  have h23 : ∑ j₁ : Fin N, ∑ j₂, ∑ j₃, (if j₂ = j₃ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0) =
      (∑ j, f₂ j * f₃ j) * ∑ j, f₁ j := by
    simp only [Finset.sum_ite_eq, Finset.mem_univ, ite_true]
    rw [mul_comm, Finset.sum_mul]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by ring
  have h123 : ∑ j₁ : Fin N, ∑ j₂, ∑ j₃,
      (2 * if j₁ = j₂ ∧ j₂ = j₃ then f₁ j₁ * f₂ j₂ * f₃ j₃ else 0) =
        2 * ∑ j, f₁ j * f₂ j * f₃ j := by
    simp only [← Finset.mul_sum]
    congr 1
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.sum_eq_single i]
    · rw [Finset.sum_eq_single i]
      · simp
      · intro b _ hb; simp [Ne.symm hb]
      · simp
    · intro b _ hb; refine Finset.sum_eq_zero fun c _ => ?_; simp [Ne.symm hb]
    · simp
  simp only [hpt, Finset.sum_add_distrib, Finset.sum_sub_distrib]
  rw [h0, h12, h13, h23, h123]

/-- `D(m)` for a general `k`-tuple: the sum over injective index maps `j : Fin k → Fin N`. -/
noncomputable def distinctSum {N k : ℕ} (x : Fin N → ℝ) (m : Fin k → ℤ) : ℂ :=
  ∑ j : Fin k → Fin N, if Function.Injective j then ∏ a, ephase x (m a) (j a) else 0

/-- Sum of `f` off the range of an injective `j`. -/
lemma sum_not_mem_range {N k : ℕ} (f : Fin N → ℂ) (j : Fin k → Fin N)
    (hj : Function.Injective j) :
    ∑ i, (if i ∉ Set.range j then f i else 0) = ∑ i, f i - ∑ a, f (j a) := by
  classical
  have h1 : ∑ a, f (j a) = ∑ i ∈ Finset.univ.image j, f i := by
    rw [Finset.sum_image (fun a _ b _ h => hj h)]
  rw [h1, eq_sub_iff_add_eq, ← Finset.sum_filter]
  rw [← Finset.sum_filter_add_sum_filter_not Finset.univ (fun i => i ∉ Set.range j)]
  congr 1
  congr 1; ext i; simp [Set.mem_range]

/-- **TRACE-001, general recursion.**  Splitting off the first index,
`D(m₀, m) = T(m₀) D(m) - ∑_a D(m + m₀ e_a)`.  Iterating it yields the partition–Möbius
formula (7) for every `k`. -/
theorem distinct_sum_cons {N k : ℕ} (x : Fin N → ℝ) (m₀ : ℤ) (m : Fin k → ℤ) :
    distinctSum x (Fin.cons m₀ m : Fin (k + 1) → ℤ) =
      traceZ x m₀ * distinctSum x m -
        ∑ a : Fin k, distinctSum x (Function.update m a (m a + m₀)) := by
  classical
  -- split the index map as `(j₀, j)`
  have hsplit : distinctSum x (Fin.cons m₀ m : Fin (k + 1) → ℤ) =
      ∑ j : Fin k → Fin N, ∑ j₀ : Fin N,
        if j₀ ∉ Set.range j ∧ Function.Injective j then
          ephase x m₀ j₀ * ∏ a, ephase x (m a) (j a) else 0 := by
    rw [distinctSum, ← (Fin.consEquiv (fun _ => Fin N)).sum_comp, Fintype.sum_prod_type,
      Finset.sum_comm]
    refine Finset.sum_congr rfl fun j _ => Finset.sum_congr rfl fun j₀ _ => ?_
    simp only [Fin.consEquiv_apply, Fin.prod_univ_succ, Fin.cons_zero,
      Fin.cons_succ]
    have hiff : Function.Injective ((Fin.consEquiv fun _ => Fin N) (j₀, j)) ↔
        j₀ ∉ Set.range j ∧ Function.Injective j := Fin.cons_injective_iff
    simp only [hiff]
  -- the product with an updated exponent
  have hupd : ∀ (j : Fin k → Fin N) (a : Fin k),
      ∏ b, ephase x (Function.update m a (m a + m₀) b) (j b) =
        ephase x m₀ (j a) * ∏ b, ephase x (m b) (j b) := by
    intro j a
    have e : (fun b => ephase x (Function.update m a (m a + m₀) b) (j b)) =
        Function.update (fun b => ephase x (m b) (j b)) a (ephase x (m a + m₀) (j a)) := by
      ext b
      by_cases hb : b = a
      · subst hb; simp
      · simp [Function.update_of_ne hb]
    rw [e, Finset.prod_update_of_mem (Finset.mem_univ a),
      ← Finset.mul_prod_erase Finset.univ (fun b => ephase x (m b) (j b)) (Finset.mem_univ a),
      ← ephase_add, Finset.sdiff_singleton_eq_erase]
    ring
  rw [hsplit, distinctSum, Finset.mul_sum]
  simp only [distinctSum]
  rw [Finset.sum_comm (s := Finset.univ (α := Fin k)), ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun j _ => ?_
  by_cases hj : Function.Injective j
  · simp only [hj, and_true, ite_true, hupd]
    have := sum_not_mem_range (ephase x m₀) j hj
    rw [show (∑ j₀, if j₀ ∉ Set.range j then ephase x m₀ j₀ * ∏ a, ephase x (m a) (j a) else 0) =
        (∑ j₀, if j₀ ∉ Set.range j then ephase x m₀ j₀ else 0) * ∏ a, ephase x (m a) (j a) by
      rw [Finset.sum_mul]; refine Finset.sum_congr rfl fun j₀ _ => ?_; split_ifs <;> simp]
    rw [this, traceZ_eq_sum_ephase, ← Finset.sum_mul]
    ring
  · simp [hj]

#print axioms ephase_add
#print axioms traceZ_eq_sum_ephase
#print axioms distinct_sum_two
#print axioms distinct_sum_three
#print axioms sum_not_mem_range
#print axioms distinct_sum_cons
end Bgs.Mathlib
