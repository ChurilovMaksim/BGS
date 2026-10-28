module
public import Bgs.Mathlib.ClockFloor
@[expose] public section

/-!
# Exact positive Abel decomposition and rigidity of the clock floor
(BGS-TRACE-092 §1, equality case of BGS-TRACE-007 / BGS-TRACE-091)

Building on the certificate `P = G + H` of `ClockFloor.lean`, we prove:

* `abelL_excess_decomposition` — the exact finite-`N` identity
  `2 (L_N(s) - 1/(e^{2s}-1)) = N⁻² [ ∑_{0<|m|<N} ĝ_m |T_m|² + ∑_{j≠k} H(2π(x_j-x_k)) ]`
  with `ĝ_m ≥ 0` and `H ≥ 0` (the repository's formula (2) of TRACE-092 in
  circle form);
* `Hfun_eq_zero_iff` — `H(θ) = 0` iff `Nθ ∈ 2πℤ` and `θ ∉ 2πℤ`;
* `abelL_eq_clock_iff` — **equality classification**: `L_N(s) = 1/(e^{2s}-1)` at one
  `s > 0` iff the spectrum is a rotated `N`-clock (up to relabelling and integer shifts);
* `abelL_gt_clock` — strict inequality for every other spectrum.
-/

open Real BigOperators Filter

namespace Bgs.Mathlib

/-- A spectrum `x : Fin N → ℝ` (phases mod 1) is a *rotated clock* if, after a common
rotation `c`, a relabelling `σ` and integer shifts, it is the clock `j/N`. -/
def IsRotatedClock {N : ℕ} (x : Fin N → ℝ) : Prop :=
  ∃ c : ℝ, ∃ σ : Equiv.Perm (Fin N), ∀ j, ∃ n : ℤ, x j = c + (σ j : ℝ) / N + n

variable {N : ℕ} {s : ℝ}

/-! ## Strict scalar inequalities -/

lemma sinh_lt_mul_cosh {t : ℝ} (ht : 0 < t) : Real.sinh t < t * Real.cosh t := by
  let g : ℝ → ℝ := fun t => t * Real.cosh t - Real.sinh t
  have hg : ∀ t, HasDerivAt g (t * Real.sinh t) t := by
    intro t
    have := ((hasDerivAt_id' t).mul (Real.hasDerivAt_cosh t)).sub (Real.hasDerivAt_sinh t)
    convert! this using 1
    ring
  have hmono : StrictMonoOn g (Set.Ici 0) := by
    apply strictMonoOn_of_deriv_pos (convex_Ici 0)
    · exact fun t _ => (hg t).continuousAt.continuousWithinAt
    · intro t ht
      rw [interior_Ici] at ht
      rw [(hg t).deriv]
      exact mul_pos ht (Real.sinh_pos_iff.2 ht)
  have := hmono (Set.mem_Ici.2 le_rfl) (Set.mem_Ici.2 ht.le) ht
  simp [g] at this
  linarith

lemma two_sinh_lt {a : ℝ} (ha : 0 < a) : 2 * Real.sinh a < a * (Real.cosh a + 1) := by
  have h := sinh_lt_mul_cosh (half_pos ha)
  have hc : 0 < Real.cosh (a / 2) := Real.cosh_pos _
  have e1 : Real.sinh a = 2 * Real.sinh (a / 2) * Real.cosh (a / 2) := by
    rw [← Real.sinh_two_mul]; ring_nf
  have e2 : Real.cosh a = 2 * Real.cosh (a / 2) ^ 2 - 1 := by
    have h := Real.cosh_two_mul (a / 2)
    rw [show 2 * (a / 2) = a by ring] at h
    rw [h, Real.cosh_sq]; ring
  rw [e1, e2]
  nlinarith [mul_lt_mul_of_pos_left h hc]

/-- Strict version of the key inequality used for `H ≥ 0`. -/
lemma key_strict {a c : ℝ} (ha : 0 < a) (hc1 : -1 ≤ c) (hc2 : c ≤ 1) :
    Real.sinh a * (1 - c) < a * (Real.cosh a - c) := by
  have h1 := two_sinh_lt ha
  have h2 : 1 < Real.cosh a := Real.one_lt_cosh.2 ha.ne'
  have f1 : 0 < a * (Real.cosh a - 1) := mul_pos ha (by linarith)
  have f2 : 0 < a * (Real.cosh a + 1) - 2 * Real.sinh a := by linarith
  nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ 1 + c) f1.le,
    mul_nonneg (by linarith : (0:ℝ) ≤ 1 - c) f2.le]

/-! ## Zero set of `H` -/

theorem Hfun_eq_zero_iff (hN : 1 ≤ N) (hs : 0 < s) (θ : ℝ) :
    Hfun N s θ = 0 ↔ (Real.cos (N * θ) = 1 ∧ Real.cos θ ≠ 1) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hC : 0 < cC N s := by
    unfold cC
    have : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
    positivity
  by_cases hcos : Real.cos θ = 1
  · obtain ⟨n, hn⟩ := (Real.cos_eq_one_iff θ).1 hcos
    have e : (fun m : ℤ => hc N s m * Real.cos (m * θ)) =
        fun m : ℤ => hc N s m * Real.cos (m * 0) := by
      funext m
      rw [← hn, show (m : ℝ) * (n * (2 * π)) = ((m * n : ℤ) : ℝ) * (2 * π) by push_cast; ring,
        Real.cos_int_mul_two_pi]
      simp
    have h1 := hc_hasSum hN hs θ
    rw [e] at h1
    rw [h1.unique (hc_hasSum hN hs 0), Hfun_zero hN hs]
    have : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
    constructor
    · intro h; exfalso
      have : 0 < (N : ℝ) * s / Real.sinh s ^ 2 := by positivity
      linarith
    · rintro ⟨_, h⟩; exact absurd hcos h
  · have hc1 : 0 < 1 - Real.cos θ := by
      have := Real.cos_le_one θ
      exact sub_pos.2 (lt_of_le_of_ne this hcos)
    set a := 2 * s / N with ha
    have hapos : 0 < a := div_pos (by linarith) hNpos
    have hq : qN N s = Real.exp (-a) := by rw [qN, ha]; congr 1; ring
    have hF : fejSum N θ = (1 - Real.cos (N * θ)) / (N * (1 - Real.cos θ)) := by
      rw [eq_div_iff (by positivity), ← mul_assoc, mul_comm (fejSum N θ) N, mul_assoc,
        fejSum_mul θ]
      field_simp
    have hsin : Real.sin (N * θ / 2) ^ 2 = (1 - Real.cos (N * θ)) / 2 := by
      rw [Real.sin_sq_eq_half_sub, show 2 * ((N : ℝ) * θ / 2) = N * θ by ring]; ring
    have hcosh : Real.cos θ < Real.cosh a := by
      have := Real.cos_le_one θ; have := Real.one_lt_cosh.2 hapos.ne'; linarith
    have hP : poissonKernel (qN N s) θ = Real.sinh a / (Real.cosh a - Real.cos θ) := by
      rw [hq, poissonKernel_exp a θ hapos]
    have hkey := key_strict hapos (Real.neg_one_le_cos θ) (Real.cos_le_one θ)
    have hbr : poissonKernel (qN N s) θ / (2 * (N * s)) < 1 / (N * N * (1 - Real.cos θ)) := by
      rw [hP, div_div, div_lt_div_iff₀ (mul_pos (by linarith) (by positivity)) (by positivity)]
      have hs' : 2 * s = N * a := by rw [ha]; field_simp
      have e : (Real.cosh a - Real.cos θ) * (2 * (N * s)) =
          N * N * (a * (Real.cosh a - Real.cos θ)) := by
        rw [show (2 * (N * s) : ℝ) = N * (2 * s) by ring, hs']; ring
      rw [one_mul, e]
      have := mul_lt_mul_of_pos_left hkey (by positivity : (0 : ℝ) < N * N)
      linarith
    have hform : Hfun N s θ = cC N s * ((1 - Real.cos (N * θ)) *
        (1 / (N * N * (1 - Real.cos θ)) - poissonKernel (qN N s) θ / (2 * (N * s)))) := by
      unfold Hfun
      rw [hF, hsin]
      congr 1
      field_simp
    rw [hform]
    have hpos : 0 < 1 / (N * N * (1 - Real.cos θ)) - poissonKernel (qN N s) θ / (2 * (N * s)) := by
      linarith
    constructor
    · intro h
      refine ⟨?_, hcos⟩
      rcases mul_eq_zero.1 h with h | h
      · exact absurd h hC.ne'
      rcases mul_eq_zero.1 h with h | h
      · linarith
      · exact absurd h hpos.ne'
    · rintro ⟨h, _⟩
      rw [h]; ring

/-! ## Exact decomposition -/

lemma clock_floor_eq_coth (hs : 0 < s) :
    1 / (Real.exp (2 * s) - 1) = (Real.cosh s / Real.sinh s - 1) / 2 := by
  have hE1 : Real.exp s * Real.exp (-s) = 1 := by rw [← Real.exp_add]; simp
  have h2 : Real.exp (2 * s) = Real.exp s * Real.exp s := by rw [← Real.exp_add]; ring_nf
  rw [Real.cosh_eq, Real.sinh_eq, h2]
  have hpos : Real.exp s - Real.exp (-s) ≠ 0 := by
    have : Real.exp (-s) < Real.exp s := Real.exp_lt_exp.2 (by linarith)
    linarith
  have hpos2 : Real.exp s * Real.exp s - 1 ≠ 0 := by
    have : 1 < Real.exp s := by
      rw [← Real.exp_zero]; exact Real.exp_lt_exp.2 hs
    nlinarith
  have hEpos : 0 < Real.exp s := Real.exp_pos s
  have he : Real.exp (-s) = 1 / Real.exp s := by
    rw [eq_div_iff hEpos.ne']; linarith
  have hpos3 : Real.exp s ^ 2 - 1 ≠ 0 := by rw [sq]; exact hpos2
  rw [he] at hpos ⊢
  field_simp
  ring

lemma pair_cos_sum_eq_norm {D : ℕ} (x : Fin D → ℝ) (m : ℤ) :
    ∑ j, ∑ k, Real.cos (m * (2 * π * (x j - x k))) = ‖traceT x m.natAbs‖ ^ 2 := by
  rw [norm_traceT_sq]
  have e : ∀ α : ℝ, Real.cos ((m : ℝ) * α) = Real.cos ((m.natAbs : ℝ) * α) := by
    intro α
    simp only [Nat.cast_natAbs, Int.cast_abs]
    rcases abs_choice ((m : ℤ) : ℝ) with h | h <;> rw [h]
    rw [neg_mul, Real.cos_neg]
  simp_rw [e]

/-- **Exact positive Abel decomposition** (TRACE-092 (2), circle form). -/
theorem abelL_excess_decomposition (hN : 1 ≤ N) (x : Fin N → ℝ) (hs : 0 < s) :
    2 * (abelL x s - 1 / (Real.exp (2 * s) - 1)) =
      (1 / (N : ℝ) ^ 2) *
        (∑ m ∈ (Finset.Ioo (-(N : ℤ)) N).erase 0,
            gc N s m * ‖traceT x m.natAbs‖ ^ 2 +
          ∑ j, ∑ k ∈ Finset.univ.erase j, Hfun N s (2 * π * (x j - x k))) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hsh : 0 < Real.sinh s := Real.sinh_pos_iff.2 hs
  have hid := abelL_poisson_identity hN x hs
  rw [show Real.exp (-2 * s / N) = qN N s from rfl] at hid
  set G : ℝ → ℝ := fun θ => ∑ m ∈ Finset.Ioo (-(N : ℤ)) N, gc N s m * Real.cos (m * θ) with hG
  have hdec : ∀ θ, poissonKernel (qN N s) θ = G θ + Hfun N s θ := by
    intro θ
    have h := (gc_hasSum hN hs θ).add (hc_hasSum hN hs θ)
    have e : (fun m : ℤ => gc N s m * Real.cos (m * θ) + hc N s m * Real.cos (m * θ)) =
        fun m : ℤ => pc N s m * Real.cos (m * θ) := by
      funext m; simp only [gc]; ring
    rw [e] at h
    exact (pc_hasSum hN hs θ).unique h
  simp_rw [hdec, Finset.sum_add_distrib] at hid
  have hGsum : ∑ j, ∑ k, G (2 * π * (x j - x k)) = ∑ m ∈ Finset.Ioo (-(N : ℤ)) N,
      gc N s m * ‖traceT x m.natAbs‖ ^ 2 := by
    calc ∑ j, ∑ k, G (2 * π * (x j - x k))
        = ∑ j, ∑ m ∈ Finset.Ioo (-(N : ℤ)) N, ∑ k,
            gc N s m * Real.cos (m * (2 * π * (x j - x k))) := by
          apply Finset.sum_congr rfl; intro j _
          simp only [hG]
          exact Finset.sum_comm
      _ = ∑ m ∈ Finset.Ioo (-(N : ℤ)) N, ∑ j, ∑ k,
            gc N s m * Real.cos (m * (2 * π * (x j - x k))) := Finset.sum_comm
      _ = _ := by
          apply Finset.sum_congr rfl; intro m _
          rw [← pair_cos_sum_eq_norm, Finset.mul_sum]
          simp only [Finset.mul_sum]
  have h0 : (0 : ℤ) ∈ Finset.Ioo (-(N : ℤ)) N := by
    rw [Finset.mem_Ioo]; omega
  rw [← Finset.add_sum_erase _ _ h0] at hGsum
  have htr0 : ‖traceT x (0 : ℤ).natAbs‖ ^ 2 = (N : ℝ) ^ 2 := by
    rw [← pair_cos_sum_eq_norm]; simp; ring
  rw [htr0] at hGsum
  have hHsum : ∑ j, ∑ k, Hfun N s (2 * π * (x j - x k)) =
      N * (N * s / Real.sinh s ^ 2) +
        ∑ j, ∑ k ∈ Finset.univ.erase j, Hfun N s (2 * π * (x j - x k)) := by
    have : ∀ j : Fin N, ∑ k, Hfun N s (2 * π * (x j - x k)) =
        N * s / Real.sinh s ^ 2 + ∑ k ∈ Finset.univ.erase j, Hfun N s (2 * π * (x j - x k)) := by
      intro j
      rw [← Finset.add_sum_erase _ _ (Finset.mem_univ j)]
      simp only [sub_self, mul_zero, Hfun_zero hN hs]
    simp_rw [this, Finset.sum_add_distrib]
    simp
  rw [hGsum, hHsum] at hid
  have hval : gc N s 0 * (N : ℝ) ^ 2 + N * (N * s / Real.sinh s ^ 2) =
      (N : ℝ) ^ 2 * (Real.cosh s / Real.sinh s) := by
    rw [gc_zero hN hs, Real.sinh_two_mul]
    field_simp
    ring
  rw [clock_floor_eq_coth hs]
  have : (1 / (N : ℝ) ^ 2) * ((N : ℝ) ^ 2 * (Real.cosh s / Real.sinh s)) =
      Real.cosh s / Real.sinh s := by field_simp
  have e2 : 2 * abelL x s + 1 = (1 / (N : ℝ) ^ 2) * ((N : ℝ) ^ 2 * (Real.cosh s / Real.sinh s)) +
      (1 / (N : ℝ) ^ 2) * (∑ m ∈ (Finset.Ioo (-(N : ℤ)) N).erase 0,
            gc N s m * ‖traceT x m.natAbs‖ ^ 2 +
          ∑ j, ∑ k ∈ Finset.univ.erase j, Hfun N s (2 * π * (x j - x k))) := by
    rw [hid, ← hval]; ring
  linarith

/-! ## Rigidity -/

lemma isRotatedClock_of_pairs (hN : 1 ≤ N) (x : Fin N → ℝ)
    (h : ∀ j k, j ≠ k → (∃ n : ℤ, (N : ℝ) * (x j - x k) = n) ∧ ¬ ∃ n : ℤ, x j - x k = n) :
    IsRotatedClock x := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hNz : (0 : ℤ) < N := by exact_mod_cast hN
  set j0 : Fin N := ⟨0, hN⟩
  have hex : ∀ j, ∃ n : ℤ, (N : ℝ) * (x j - x j0) = n := by
    intro j
    by_cases hj : j = j0
    · exact ⟨0, by simp [hj]⟩
    · exact (h j j0 hj).1
  choose t ht using hex
  have hmod : ∀ j, 0 ≤ t j % (N : ℤ) ∧ t j % (N : ℤ) < N := fun j =>
    ⟨Int.emod_nonneg _ hNz.ne', Int.emod_lt_of_pos _ hNz⟩
  let r : Fin N → Fin N := fun j => ⟨(t j % (N : ℤ)).toNat, by
    have := hmod j; omega⟩
  have hrinj : Function.Injective r := by
    intro j k hjk
    by_contra hne
    have hr : t j % (N : ℤ) = t k % (N : ℤ) := by
      have := congrArg Fin.val hjk
      simp only [r] at this
      have h1 := hmod j; have h2 := hmod k
      omega
    have hdvd : (N : ℤ) ∣ t j - t k := Int.ModEq.dvd hr.symm
    obtain ⟨q, hq⟩ := hdvd
    apply (h j k hne).2
    refine ⟨q, ?_⟩
    have e1 := ht j; have e2 := ht k
    have : (N : ℝ) * (x j - x k) = N * q := by
      have : ((t j - t k : ℤ) : ℝ) = ((N * q : ℤ) : ℝ) := by rw [hq]
      push_cast at this
      linarith
    exact mul_left_cancel₀ hNpos.ne' this
  have hrbij : Function.Bijective r := Finite.injective_iff_bijective.1 hrinj
  refine ⟨x j0, Equiv.ofBijective r hrbij, fun j => ⟨t j / (N : ℤ), ?_⟩⟩
  simp only [Equiv.ofBijective_apply, r]
  have hdecomp : ((t j % (N : ℤ)).toNat : ℝ) + N * ((t j / (N : ℤ) : ℤ) : ℝ) = t j := by
    have h1 := Int.emod_add_mul_ediv (t j) N
    have h2 : ((t j % (N : ℤ)).toNat : ℤ) = t j % N := Int.toNat_of_nonneg (hmod j).1
    have : (((t j % (N : ℤ)).toNat : ℤ) : ℝ) + ((N * (t j / (N : ℤ)) : ℤ) : ℝ) =
        ((t j : ℤ) : ℝ) := by rw [h2]; exact_mod_cast h1
    push_cast at this
    exact this
  have e := ht j
  field_simp
  linarith

lemma abelL_of_isRotatedClock {x : Fin N → ℝ} (hx : IsRotatedClock x) (s : ℝ) :
    abelL x s = abelL (clockPhases N) s := by
  obtain ⟨c, σ, hx⟩ := hx
  choose n hn using hx
  have htr : ∀ m : ℕ, traceT x m =
      Complex.exp (2 * π * Complex.I * m * c) * traceT (clockPhases N) m := by
    intro m
    rw [traceT, traceT, Finset.mul_sum]
    conv_rhs => rw [← Equiv.sum_comp σ]
    apply Finset.sum_congr rfl; intro j _
    rw [hn j, ← Complex.exp_add]
    have : 2 * ↑π * Complex.I * ↑m * ((c + (σ j : ℝ) / N + n j : ℝ) : ℂ) =
        (2 * ↑π * Complex.I * ↑m * c + 2 * ↑π * Complex.I * ↑m * ((clockPhases N (σ j) : ℝ) : ℂ))
          + ((m * n j : ℤ) : ℂ) * (2 * π * Complex.I) := by
      simp only [clockPhases]; push_cast; ring
    rw [this, Complex.exp_add, Complex.exp_int_mul_two_pi_mul_I, mul_one]
  unfold abelL
  congr 1
  congr 1
  funext m
  rw [htr, norm_mul, Complex.norm_exp]
  have : (2 * ↑π * Complex.I * ↑(m + 1) * (c : ℂ)).re = 0 := by
    simp
  rw [this, Real.exp_zero, one_mul]

/-- **Rigidity of the clock floor.**  For `N ≥ 1` and `s > 0`, the universal floor
`L_N(s) ≥ 1/(e^{2s} - 1)` is attained iff the spectrum is a rotated `N`-clock. -/
theorem abelL_eq_clock_iff (hN : 1 ≤ N) (x : Fin N → ℝ) (hs : 0 < s) :
    abelL x s = 1 / (Real.exp (2 * s) - 1) ↔ IsRotatedClock x := by
  constructor
  · intro heq
    have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
    have hdec := abelL_excess_decomposition hN x hs
    rw [heq, sub_self, mul_zero] at hdec
    have hA : 0 ≤ ∑ m ∈ (Finset.Ioo (-(N : ℤ)) N).erase 0, gc N s m * ‖traceT x m.natAbs‖ ^ 2 :=
      Finset.sum_nonneg fun m _ => mul_nonneg (gc_nonneg hN hs m) (by positivity)
    have hHnn : ∀ j, ∀ k ∈ Finset.univ.erase j, 0 ≤ Hfun N s (2 * π * (x j - x k)) :=
      fun j k _ => Hfun_nonneg hN hs _
    have hB : 0 ≤ ∑ j, ∑ k ∈ Finset.univ.erase j, Hfun N s (2 * π * (x j - x k)) :=
      Finset.sum_nonneg fun j _ => Finset.sum_nonneg (hHnn j)
    have hB0 : ∑ j, ∑ k ∈ Finset.univ.erase j, Hfun N s (2 * π * (x j - x k)) = 0 := by
      have : (1 / (N : ℝ) ^ 2) * (∑ m ∈ (Finset.Ioo (-(N : ℤ)) N).erase 0,
          gc N s m * ‖traceT x m.natAbs‖ ^ 2 +
          ∑ j, ∑ k ∈ Finset.univ.erase j, Hfun N s (2 * π * (x j - x k))) = 0 := hdec.symm
      rcases mul_eq_zero.1 this with h | h
      · exfalso; have : (0 : ℝ) < 1 / (N : ℝ) ^ 2 := by positivity
        linarith
      · linarith
    apply isRotatedClock_of_pairs hN x
    intro j k hjk
    have hz : Hfun N s (2 * π * (x j - x k)) = 0 := by
      have h1 := (Finset.sum_eq_zero_iff_of_nonneg fun j _ => Finset.sum_nonneg (hHnn j)).1 hB0 j
        (Finset.mem_univ j)
      exact (Finset.sum_eq_zero_iff_of_nonneg (hHnn j)).1 h1 k
        (Finset.mem_erase.2 ⟨hjk.symm, Finset.mem_univ k⟩)
    obtain ⟨h1, h2⟩ := (Hfun_eq_zero_iff hN hs _).1 hz
    constructor
    · obtain ⟨n, hn⟩ := (Real.cos_eq_one_iff _).1 h1
      refine ⟨n, ?_⟩
      have hpi : (0 : ℝ) < 2 * π := by positivity
      have : ((N : ℝ) * (x j - x k)) * (2 * π) = n * (2 * π) := by rw [hn]; ring
      exact mul_right_cancel₀ hpi.ne' this
    · rintro ⟨n, hn⟩
      apply h2
      rw [hn, show 2 * π * (n : ℝ) = n * (2 * π) by ring]
      exact Real.cos_int_mul_two_pi n
  · intro hx
    rw [abelL_of_isRotatedClock hx, abelL_clock hN hs]

/-- Strict floor for every spectrum that is not a rotated clock. -/
theorem abelL_gt_clock (hN : 1 ≤ N) (x : Fin N → ℝ) (hx : ¬ IsRotatedClock x) (hs : 0 < s) :
    1 / (Real.exp (2 * s) - 1) < abelL x s :=
  lt_of_le_of_ne (abelL_ge_clock hN x hs) fun h => hx ((abelL_eq_clock_iff hN x hs).1 h.symm)

end Bgs.Mathlib
