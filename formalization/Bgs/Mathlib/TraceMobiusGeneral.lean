module
public import Bgs.Mathlib.TraceMobius
@[expose] public section

/-!
# The factorial trace identity for every `k` (BGS-TRACE-001, Theorem 1)

Source: `mathematics/trace-bridge/trace_to_local_statistics_bridge.md`, Theorem 1.

For eigenphases `x : Fin N → ℝ`, `T(m) = ∑_j e^{2πi m x_j}` and the distinct-index sum
`D(m_1,…,m_k) = ∑_{j injective} ∏_a e^{2πi m_a x_{j_a}}` (`distinctSum`), we prove for every
`k` the exact identity in its **cycle form**

  `D(m) = ∑_{σ ∈ S_k} sgn(σ) ∏_{c ∈ cycles(σ)} T(∑_{a ∈ c} m_a)`        (`distinctSum_cycle_formula`)

where the product runs over the orbits (cycles, including fixed points) of `σ`.
Grouping the permutations by their orbit partition `π` gives the note's partition form (7):
the permutations whose cycles are exactly the blocks of `π` contribute
`∑ sgn σ = ∏_{B ∈ π} (-1)^{|B|-1} (|B|-1)! = μ(π)`.

The proof is the classical sign-reversing involution: for an index map `j`,
`∑_{σ : j ∘ σ = j} sgn σ` is `1` if `j` is injective and `0` otherwise
(`sum_sign_stabilizer`), and a sum over maps constant on the cycles of `σ` factorizes over
the cycles (`sum_const_on_cycles`).
-/

open Real Complex BigOperators Finset Equiv

namespace Bgs.Mathlib

open Classical

/-- The set of cycles (orbits) of a permutation, as a quotient type. -/
abbrev CycleClass {k : ℕ} (σ : Perm (Fin k)) : Type := Quotient (Perm.SameCycle.setoid σ)

/-- **Sign-reversing involution.**  `∑_{σ : j ∘ σ = j} sgn σ = [j injective]`. -/
lemma sum_sign_stabilizer {k N : ℕ} (j : Fin k → Fin N) :
    ∑ σ : Perm (Fin k), (if j ∘ σ = j then ((Perm.sign σ : ℤ) : ℂ) else 0) =
      if Function.Injective j then 1 else 0 := by
  split_ifs with hinj
  · rw [Finset.sum_eq_single 1]
    · simp
    · intro σ _ hσ
      rw [if_neg]
      intro hj
      apply hσ
      ext a
      have := congrFun hj a
      simp only [Function.comp_apply] at this
      simp [hinj this]
    · simp
  · obtain ⟨a, b, hab, hne⟩ : ∃ a b, j a = j b ∧ a ≠ b := by
      by_contra h
      push Not at h
      exact hinj fun a b hab => h a b hab
    set τ := swap a b
    set F : Perm (Fin k) → ℂ := fun σ => if j ∘ σ = j then ((Perm.sign σ : ℤ) : ℂ) else 0
      with hF
    have hjτ : ∀ y, j (τ y) = j y := by
      intro y
      by_cases hya : y = a
      · subst hya; simp [τ, hab]
      by_cases hyb : y = b
      · subst hyb; simp [τ, hab]
      · simp [τ, swap_apply_of_ne_of_ne hya hyb]
    have hflip : ∀ σ, F (τ * σ) = -F σ := by
      intro σ
      have hc : (j ∘ ⇑(τ * σ) = j) ↔ (j ∘ σ = j) := by
        have : j ∘ ⇑(τ * σ) = j ∘ σ := by
          funext y; simp [hjτ]
        rw [this]
      simp only [hF, hc]
      split_ifs
      · rw [Perm.sign_mul, Perm.sign_swap hne]; push_cast; ring
      · simp
    have hsum : ∑ σ, F σ = -∑ σ, F σ := by
      calc ∑ σ, F σ = ∑ σ, F (τ * σ) := (Fintype.sum_equiv (Equiv.mulLeft τ) (fun σ => F (τ * σ)) F
          (fun σ => rfl)).symm
        _ = -∑ σ, F σ := by simp_rw [hflip]; rw [Finset.sum_neg_distrib]
    have : ∑ σ, F σ = 0 := by linear_combination hsum / 2
    exact this

/-- Maps constant along a permutation are constant on its cycles. -/
lemma const_on_sameCycle {k N : ℕ} {σ : Perm (Fin k)} {j : Fin k → Fin N} (hj : j ∘ σ = j)
    {a b : Fin k} (h : σ.SameCycle a b) : j a = j b := by
  obtain ⟨i, rfl⟩ := h
  have h1 : ∀ y, j (σ y) = j y := fun y => congrFun hj y
  have hn : ∀ n : ℕ, ∀ y, j ((σ ^ n) y) = j y := by
    intro n
    induction n with
    | zero => intro y; simp
    | succ n ih => intro y; rw [pow_succ', Perm.mul_apply, h1, ih]
  rcases Int.eq_nat_or_neg i with ⟨n, rfl | rfl⟩
  · rw [zpow_natCast, hn]
  · rw [zpow_neg, zpow_natCast]
    have := hn n ((σ ^ n)⁻¹ a)
    rw [show (σ ^ n) ((σ ^ n)⁻¹ a) = a from (eq_symm_apply _).mp rfl] at this
    exact this

/-- **Factorization over cycles.** -/
lemma sum_const_on_cycles {k N : ℕ} (σ : Perm (Fin k)) (f : Fin k → Fin N → ℂ) :
    ∑ j : Fin k → Fin N, (if j ∘ σ = j then ∏ a, f a (j a) else 0) =
      ∏ q : CycleClass σ, ∑ t : Fin N,
        ∏ a ∈ univ.filter (fun a => (Quotient.mk _ a : CycleClass σ) = q), f a t := by
  set mk : Fin k → CycleClass σ := fun a => Quotient.mk _ a with hmk
  set φ : (CycleClass σ → Fin N) → (Fin k → Fin N) := fun g => g ∘ mk with hφ
  have hφinj : Function.Injective φ := by
    intro g g' h
    funext q
    induction q using Quotient.ind with
    | _ a => exact congrFun h a
  have hmkσ : ∀ a, mk (σ a) = mk a := fun a =>
    Quotient.sound (Perm.sameCycle_apply_left.2 (Perm.SameCycle.refl _ _))
  have himg : univ.filter (fun j : Fin k → Fin N => j ∘ σ = j) = univ.image φ := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_image]
    constructor
    · intro hj
      refine ⟨Quotient.lift j (fun a b h => const_on_sameCycle hj h), ?_⟩
      funext a; rfl
    · rintro ⟨g, rfl⟩
      funext a
      simp only [hφ, Function.comp_apply]
      rw [hmkσ]
  rw [Fintype.prod_sum, ← Finset.sum_filter, himg, Finset.sum_image (fun g _ g' _ h => hφinj h)]
  refine Finset.sum_congr rfl fun g _ => ?_
  change ∏ a, f a (g (mk a)) = _
  rw [← Finset.prod_fiberwise (univ : Finset (Fin k)) mk (fun a => f a (g (mk a)))]
  refine Finset.prod_congr rfl fun q _ => ?_
  refine Finset.prod_congr rfl fun a ha => ?_
  have : mk a = q := (Finset.mem_filter.1 ha).2
  rw [this]

lemma prod_ephase {N : ℕ} (x : Fin N → ℝ) {ι : Type*} (s : Finset ι) (m : ι → ℤ) (t : Fin N) :
    ∏ a ∈ s, ephase x (m a) t = ephase x (∑ a ∈ s, m a) t := by
  induction s using Finset.induction_on with
  | empty => simp [ephase]
  | insert a s ha ih => rw [prod_insert ha, sum_insert ha, ih, ephase_add]

/-- **TRACE-001, Theorem 1 (cycle form), for every `k`.** -/
theorem distinctSum_cycle_formula {N k : ℕ} (x : Fin N → ℝ) (m : Fin k → ℤ) :
    distinctSum x m =
      ∑ σ : Perm (Fin k), ((Perm.sign σ : ℤ) : ℂ) *
        ∏ q : CycleClass σ,
          traceZ x (∑ a ∈ univ.filter (fun a => (Quotient.mk _ a : CycleClass σ) = q), m a) := by
  have h1 : distinctSum x m = ∑ j : Fin k → Fin N, ∑ σ : Perm (Fin k),
      ((Perm.sign σ : ℤ) : ℂ) * (if j ∘ σ = j then ∏ a, ephase x (m a) (j a) else 0) := by
    rw [distinctSum]
    refine Finset.sum_congr rfl fun j _ => ?_
    have := sum_sign_stabilizer (k := k) (N := N) j
    have e : ∑ σ : Perm (Fin k), ((Perm.sign σ : ℤ) : ℂ) *
        (if j ∘ σ = j then ∏ a, ephase x (m a) (j a) else 0) =
        (∑ σ : Perm (Fin k), (if j ∘ σ = j then ((Perm.sign σ : ℤ) : ℂ) else 0)) *
          ∏ a, ephase x (m a) (j a) := by
      rw [Finset.sum_mul]
      refine Finset.sum_congr rfl fun σ _ => ?_
      split_ifs <;> simp
    rw [e, this]
    split_ifs <;> simp
  rw [h1, Finset.sum_comm]
  refine Finset.sum_congr rfl fun σ _ => ?_
  rw [← Finset.mul_sum, sum_const_on_cycles]
  congr 1
  refine Finset.prod_congr rfl fun q _ => ?_
  rw [traceZ_eq_sum_ephase]
  refine Finset.sum_congr rfl fun t _ => ?_
  exact prod_ephase x _ m t

#print axioms sum_sign_stabilizer
#print axioms const_on_sameCycle
#print axioms sum_const_on_cycles
#print axioms prod_ephase
#print axioms distinctSum_cycle_formula
end Bgs.Mathlib
