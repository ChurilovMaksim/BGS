/-
  BGS Line D: the parity bridge for `B_m^sym < 2m` (BGS-TRACE-154),
  instantiating the abstract `LineDParity.sym_bound` at the concrete
  Gamma-invariant phihat-support, with `Γ = DihedralGroup m`.
  TEST COPY ONLY — not pushed to the repository, registry untouched,
  `Bgs.lean` aggregator unchanged (this module is built by a direct
  `lake env lean` call, not imported by the aggregator).

  Sources: BGS-TRACE-154 boundary (claims.json): "For odd m,
  D_eff = a_m^2 with a_m odd, so the Gamma-invariant support has odd
  size; the reversal involution has a fixed point xi_0 with
  |Gamma xi_0| <= m, hence 2m - B_m^sym >= m/D_eff > 0. Same argument
  whenever 2m does not divide D_eff (e.g. m = 6)."
  The abstract argument is `Bgs.LineD.Parity.sym_bound` /
  `sym_bound_of_not_dvd`; the concrete input (support, weights,
  Gamma action, normalisation) is 151-full (`LineDOrbitPairFull`,
  `LineDStrongKickBridge`).

  What is built here, and what is NOT (honest scope):
  - Built: `card (V4 m) = 4` for odd `m` (kernel of `H_m` mod 4 is
    exactly the constants, via the arithmetic-progression recurrence);
    `D_eff m = A_m^2` with `A_m` odd for odd `m` (via `λ = (1+√2)^2`
    and `det_formula`); `card (support) = D_eff.toNat` (from the
    152-bridge normalisation); the assembly `bsym_bound_odd`
    (154's conclusion for odd `m`), `bsym_bound_of_not_dvd` (the
    conditional variant), and the `m = 6` corollary.
  - NOT built: the concrete kick factor `ω` and the `P_K`
    separation (these belong to 152, not to 154); nothing about
    eigenvalue statistics beyond the second moment (154's own
    boundary excludes it).

  No `sorry`, no `admit`, no `axiom`, no `native_decide` in this file.
  `#print axioms` for the main theorems is at the end.
-/

import Bgs.LineDStrongKickBridge
import Bgs.LineDParity

open scoped Matrix

namespace Bgs
namespace LineD
namespace ParityBridge

open Bgs.LineD

/-! ### §1 — The kernel of `H_m` mod 4 for odd `m` -/

/-- Pointwise form of the `V4` condition: the `i`-th component of
    `H_m y` over `ZMod 4` vanishes. -/
lemma v4_eq_zero_of_mem (m : ℕ) [NeZero m] (y : OrbitPair.V4 m) (i : ZMod m) :
    6 * y.1 i - y.1 (i + 1) - y.1 (i - 1) = 0 := by
  have h : (Defs.Hmat m (ZMod 4)) *ᵥ y.1 = 0 := by
    rw [← OrbitPairFull.Hmat_map_zmod]
    exact y.2
  have hi := congrFun h i
  rw [OrbitPairFull.Hmat_mulVec_apply] at hi
  simpa using hi

/-- The recurrence: `y_{i+1} = 2 y_i - y_{i-1}` over `ZMod 4`
    (since `6 = 2` mod 4). -/
lemma v4_recurrence (m : ℕ) [NeZero m] (y : OrbitPair.V4 m) (i : ZMod m) :
    y.1 (i + 1) = 2 * y.1 i - y.1 (i - 1) := by
  have h6 : (6 : ZMod 4) = 2 := by decide
  have h := v4_eq_zero_of_mem m y i
  rw [h6] at h
  linear_combination -h

/-- Arithmetic progression: `y_k = y_0 + k * (y_1 - y_0)` along the
    cyclic index, proved by two-step induction. -/
lemma v4_ap (m : ℕ) [NeZero m] (y : OrbitPair.V4 m) :
    ∀ k : ℕ, y.1 (k : ZMod m)
      = y.1 0 + (k : ZMod 4) * (y.1 1 - y.1 0) := by
  have key : ∀ k : ℕ,
      y.1 (k : ZMod m) = y.1 0 + (k : ZMod 4) * (y.1 1 - y.1 0)
        ∧ y.1 ((k + 1 : ℕ) : ZMod m)
          = y.1 0 + ((k + 1 : ℕ) : ZMod 4) * (y.1 1 - y.1 0) := by
    intro k
    induction k with
    | zero =>
      constructor
      · simp
      · simp
    | succ k ih =>
      obtain ⟨hk, hk1⟩ := ih
      refine ⟨hk1, ?_⟩
      have hrec := v4_recurrence m y ((k + 1 : ℕ) : ZMod m)
      rw [show ((k + 1 : ℕ) : ZMod m) + 1 = ((k + 2 : ℕ) : ZMod m) by
            push_cast; ring,
          show ((k + 1 : ℕ) : ZMod m) - 1 = (k : ZMod m) by
            push_cast; ring] at hrec
      rw [hrec, hk1, hk]
      push_cast
      ring
  exact fun k => (key k).1

/-- For odd `m`, the difference `y_1 - y_0` vanishes: going once
    around the cycle gives `m * δ = 0` in `ZMod 4`, and `m` is a unit
    mod 4. -/
lemma v4_delta_eq_zero (m : ℕ) [NeZero m] (hodd : Odd m) (y : OrbitPair.V4 m) :
    y.1 1 - y.1 0 = 0 := by
  have hap := v4_ap m y m
  rw [ZMod.natCast_self] at hap
  have hm0 : (m : ZMod 4) * (y.1 1 - y.1 0) = 0 := by
    have h2 : y.1 0 + (m : ZMod 4) * (y.1 1 - y.1 0) = y.1 0 + 0 := by
      rw [add_zero]
      exact hap.symm
    exact add_left_cancel h2
  have h2 : ¬ (2 ∣ m) := by
    rcases hodd with ⟨k, hk⟩
    rintro ⟨j, hj⟩
    omega
  have hcop2 : Nat.Coprime m 2 :=
    Nat.coprime_comm.mpr ((Nat.prime_two.coprime_iff_not_dvd).mpr h2)
  have hcop : Nat.Coprime m 4 := by
    have h4 : (4 : ℕ) = 2 ^ 2 := by norm_num
    rw [h4, Nat.coprime_pow_right_iff (by norm_num : 0 < 2)]
    exact hcop2
  have hu : IsUnit (m : ZMod 4) := (ZMod.isUnit_iff_coprime m 4).mpr hcop
  obtain ⟨u, hu⟩ := hu
  calc y.1 1 - y.1 0
      = ((u⁻¹ : (ZMod 4)ˣ) : ZMod 4)
          * ((u : ZMod 4) * (y.1 1 - y.1 0)) := by
        rw [← mul_assoc, Units.inv_mul, one_mul]
    _ = 0 := by
        rw [← hu] at hm0
        rw [hm0, mul_zero]

/-- For odd `m`, every `V4` vector is constant. -/
lemma v4_const (m : ℕ) [NeZero m] (hodd : Odd m) (y : OrbitPair.V4 m)
    (i : ZMod m) : y.1 i = y.1 0 := by
  have hap := v4_ap m y i.val
  rw [ZMod.natCast_zmod_val] at hap
  rw [hap, v4_delta_eq_zero m hodd y]
  simp

/-- For odd `m`, `|V4 m| = 4`: the kernel is exactly the constants. -/
theorem v4_card_eq_four (m : ℕ) [NeZero m] (hodd : Odd m) :
    Fintype.card (OrbitPair.V4 m) = 4 := by
  have hequiv : OrbitPair.V4 m ≃ ZMod 4 := {
    toFun := fun y => y.1 0
    invFun := fun c => ⟨fun _ => c, by
      rw [OrbitPairFull.Hmat_map_zmod]
      funext i
      rw [OrbitPairFull.Hmat_mulVec_apply]
      show (6 : ZMod 4) * c - c - c = 0
      have h4 : (4 : ZMod 4) = 0 := by decide
      have h6c : (6 : ZMod 4) * c - c - c = 4 * c := by ring
      rw [h6c, h4, zero_mul]⟩
    left_inv := by
      intro y
      apply Subtype.ext
      funext i
      exact (v4_const m hodd y i).symm
    right_inv := fun _ => rfl }
  rw [Fintype.card_congr hequiv]
  simp

/-! ### §2 — The square root sequence `A_m` and `D_eff = A_m^2` -/

/-- The pair recursion for `A_m`: `(A_n, A_{n+1})`. -/
def AmPair : ℕ → ℕ × ℕ
  | 0 => (1, 1)
  | n + 1 => ((AmPair n).2, 2 * (AmPair n).2 + (AmPair n).1)

/-- `A_m`: `1, 1, 3, 7, 17, 41, ...` — half-sums `(α^m + β^m)/2`
    for `α = 1+√2`, `β = 1-√2`. -/
def Am (n : ℕ) : ℕ := (AmPair n).1

lemma Am_add_two (n : ℕ) : Am (n + 2) = 2 * Am (n + 1) + Am n := rfl

lemma Am_odd (n : ℕ) : Odd (Am n) := by
  have key : ∀ n, Odd (Am n) ∧ Odd (Am (n + 1)) := by
    intro n
    induction n with
    | zero => exact ⟨odd_one, odd_one⟩
    | succ n ih =>
      obtain ⟨h0, h1⟩ := ih
      obtain ⟨a, ha⟩ := h0
      refine ⟨h1, ?_⟩
      rw [Am_add_two, ha]
      exact ⟨Am (n + 1) + a, by ring⟩
  exact (key n).1

/-- `S_n = α^n + β^n` for `α = 1+√2`, `β = 1-√2`. -/
noncomputable def SSeq (n : ℕ) : ℝ := (1 + Real.sqrt 2) ^ n + (1 - Real.sqrt 2) ^ n

lemma sqrt2_sq : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)

lemma alpha_sq : (1 + Real.sqrt 2) ^ 2 = 2 * (1 + Real.sqrt 2) + 1 := by
  calc (1 + Real.sqrt 2) ^ 2 = 1 + 2 * Real.sqrt 2 + (Real.sqrt 2) ^ 2 := by ring
    _ = 2 * (1 + Real.sqrt 2) + 1 := by rw [sqrt2_sq]; ring

lemma beta_sq : (1 - Real.sqrt 2) ^ 2 = 2 * (1 - Real.sqrt 2) + 1 := by
  calc (1 - Real.sqrt 2) ^ 2 = 1 - 2 * Real.sqrt 2 + (Real.sqrt 2) ^ 2 := by ring
    _ = 2 * (1 - Real.sqrt 2) + 1 := by rw [sqrt2_sq]; ring

lemma SSeq_add_two (n : ℕ) :
    SSeq (n + 2) = 2 * SSeq (n + 1) + SSeq n := by
  show (1 + Real.sqrt 2) ^ (n + 2) + (1 - Real.sqrt 2) ^ (n + 2)
      = 2 * ((1 + Real.sqrt 2) ^ (n + 1) + (1 - Real.sqrt 2) ^ (n + 1))
        + ((1 + Real.sqrt 2) ^ n + (1 - Real.sqrt 2) ^ n)
  rw [pow_add (1 + Real.sqrt 2) n 2, pow_add (1 - Real.sqrt 2) n 2,
      pow_succ (1 + Real.sqrt 2) n, pow_succ (1 - Real.sqrt 2) n,
      alpha_sq, beta_sq]
  ring

lemma SSeq_eq_two_Am (n : ℕ) : SSeq n = 2 * (Am n : ℝ) := by
  have key : ∀ n, SSeq n = 2 * (Am n : ℝ) ∧ SSeq (n + 1) = 2 * (Am (n + 1) : ℝ) := by
    intro n
    induction n with
    | zero =>
      constructor
      · simp only [SSeq, Am, AmPair, pow_zero, Nat.cast_one]; ring
      · simp only [SSeq, Am, AmPair, Nat.cast_one]; ring
    | succ n ih =>
      obtain ⟨h0, h1⟩ := ih
      refine ⟨h1, ?_⟩
      show SSeq (n + 2) = 2 * (Am (n + 2) : ℝ)
      rw [SSeq_add_two, h1, h0, Am_add_two]
      push_cast
      ring
  exact (key n).1

lemma SSeq_double (n : ℕ) :
    SSeq (2 * n) = (SSeq n) ^ 2 - 2 * (-1 : ℝ) ^ n := by
  have hab : (1 + Real.sqrt 2) * (1 - Real.sqrt 2) = -1 := by
    calc (1 + Real.sqrt 2) * (1 - Real.sqrt 2) = 1 - (Real.sqrt 2) ^ 2 := by ring
      _ = -1 := by rw [sqrt2_sq]; norm_num
  have e1 : (1 + Real.sqrt 2) ^ (2 * n) = ((1 + Real.sqrt 2) ^ n) ^ 2 := by
    rw [show (2 * n : ℕ) = n * 2 from by ring, pow_mul]
  have e2 : (1 - Real.sqrt 2) ^ (2 * n) = ((1 - Real.sqrt 2) ^ n) ^ 2 := by
    rw [show (2 * n : ℕ) = n * 2 from by ring, pow_mul]
  have e3 : (1 + Real.sqrt 2) ^ n * (1 - Real.sqrt 2) ^ n = (-1 : ℝ) ^ n := by
    rw [← mul_pow, hab]
  show (1 + Real.sqrt 2) ^ (2 * n) + (1 - Real.sqrt 2) ^ (2 * n)
      = ((1 + Real.sqrt 2) ^ n + (1 - Real.sqrt 2) ^ n) ^ 2 - 2 * (-1 : ℝ) ^ n
  rw [e1, e2, ← e3]
  ring

/-- `D_m` over `ℝ`, from `det_formula` (`λ = 3+2√2`, `μ = 3-2√2`). -/
lemma Dm_eq_real (m : ℕ) [NeZero m] :
    (Defs.Dm m : ℝ)
      = (3 + 2 * Real.sqrt 2) ^ m + (3 - 2 * Real.sqrt 2) ^ m - 2 := by
  have hC := OrbitPairFull.det_formula m
  have hlam : OrbitPairFull.lamC = ((3 + 2 * Real.sqrt 2 : ℝ) : ℂ) := by
    simp only [OrbitPairFull.lamC]
    push_cast
    ring
  have hmu : OrbitPairFull.muC = ((3 - 2 * Real.sqrt 2 : ℝ) : ℂ) := by
    simp only [OrbitPairFull.muC]
    push_cast
    ring
  rw [hlam, hmu] at hC
  apply Complex.ofReal_injective
  push_cast
  push_cast at hC
  exact hC

/-- For odd `m`, `D_m = 4 * A_m^2` (using `λ = (1+√2)^2`). -/
lemma Dm_eq_four_Am_sq (m : ℕ) [NeZero m] (hodd : Odd m) :
    (Defs.Dm m : ℝ) = 4 * (Am m : ℝ) ^ 2 := by
  have hR := Dm_eq_real m
  have hneg1 : (-1 : ℝ) ^ m = -1 := by
    rcases hodd with ⟨k, hk⟩
    rw [hk, pow_succ, pow_mul]
    simp
  have hlam_eq : (3 + 2 * Real.sqrt 2) = (1 + Real.sqrt 2) ^ 2 := by
    rw [alpha_sq]; ring
  have hmu_eq : (3 - 2 * Real.sqrt 2) = (1 - Real.sqrt 2) ^ 2 := by
    rw [beta_sq]; ring
  have hS : SSeq (2 * m) = 4 * (Am m : ℝ) ^ 2 + 2 := by
    rw [SSeq_double, SSeq_eq_two_Am, hneg1]
    ring
  rw [hR, hlam_eq, hmu_eq, ← pow_mul, ← pow_mul]
  have hSdef : (1 + Real.sqrt 2) ^ (2 * m) + (1 - Real.sqrt 2) ^ (2 * m)
      = SSeq (2 * m) := rfl
  rw [hSdef, hS]
  ring

/-- For odd `m`, `D_eff m = A_m^2` as integers. -/
lemma Deff_eq_Am_sq (m : ℕ) [NeZero m] (hodd : Odd m) :
    OrbitPair.Deff m = (Am m : ℤ) ^ 2 := by
  have hR := Dm_eq_four_Am_sq m hodd
  have hZ : Defs.Dm m = 4 * (Am m : ℤ) ^ 2 := by
    exact_mod_cast hR
  show Defs.Dm m / (Fintype.card (OrbitPair.V4 m) : ℤ) = (Am m : ℤ) ^ 2
  rw [v4_card_eq_four m hodd, hZ]
  omega

/-! ### §3 — The support size is `D_eff` -/

/-- From the 152-bridge normalisation: `card (support) = D_eff.toNat`. -/
lemma support_card_eq_Deff_toNat (m : ℕ) [NeZero m] (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m)) :
    (OrbitPair.support m (OrbitPairFull.phihatFix m s)).card
      = (OrbitPair.Deff m).toNat := by
  have hNorm := StrongKickBridge.phihatFix_hNorm m s hs
  have hDmC : (Defs.Dm m : ℂ) ≠ 0 := by
    exact_mod_cast (ne_of_gt (Defs.Dm_pos m))
  have h2 : (Fintype.card (OrbitPair.V4 m) : ℂ)
      * ((OrbitPair.support m (OrbitPairFull.phihatFix m s)).card : ℂ)
      = (Defs.Dm m : ℂ) := by
    rw [div_mul_eq_mul_div, div_eq_one_iff_eq hDmC] at hNorm
    exact hNorm
  have hcast : (((Defs.Dm m).toNat : ℕ) : ℂ) = (Defs.Dm m : ℂ) := by
    rw [← Int.cast_natCast, Int.toNat_of_nonneg (le_of_lt (Defs.Dm_pos m))]
  have hNat : Fintype.card (OrbitPair.V4 m)
      * (OrbitPair.support m (OrbitPairFull.phihatFix m s)).card
      = (Defs.Dm m).toNat := by
    apply Nat.cast_injective (R := ℂ)
    push_cast
    rw [hcast]
    exact h2
  have hV4ne : Fintype.card (OrbitPair.V4 m) ≠ 0 := by
    rintro h0
    rw [h0, Nat.zero_mul] at hNat
    have hDm0 : Defs.Dm m = 0 := by
      have h1 := Int.toNat_of_nonneg (le_of_lt (Defs.Dm_pos m))
      rw [← hNat] at h1
      exact (by simpa using h1.symm)
    exact (ne_of_gt (Defs.Dm_pos m)) hDm0
  have hDeff : OrbitPair.Deff m
      = ((OrbitPair.support m (OrbitPairFull.phihatFix m s)).card : ℤ) := by
    show Defs.Dm m / (Fintype.card (OrbitPair.V4 m) : ℤ) = _
    have hDmZ : Defs.Dm m = (Fintype.card (OrbitPair.V4 m) : ℤ)
        * ((OrbitPair.support m (OrbitPairFull.phihatFix m s)).card : ℤ) := by
      have h1 := Int.toNat_of_nonneg (le_of_lt (Defs.Dm_pos m))
      rw [← hNat] at h1
      push_cast at h1
      exact h1.symm
    rw [hDmZ]
    have hV4neZ : (Fintype.card (OrbitPair.V4 m) : ℤ) ≠ 0 := by
      exact_mod_cast hV4ne
    exact Int.mul_ediv_cancel_left _ hV4neZ
  rw [hDeff]
  exact Int.toNat_natCast _

/-! ### §4 — Assembly: 154's conclusion -/

/-- The Gamma action on the phihat-support subtype, for `154`. -/
noncomputable abbrev suppAct (m : ℕ) [NeZero m] (s : ℤ) :
    MulAction (DihedralGroup m)
      ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s)) :=
  OrbitPair.supportMulAction m (OrbitPairFull.phihatFix m s)
    (fun g ξ hξ => StrongKickBridge.phihatFix_support_inv m s g ξ hξ)

/-- 154, main case: for odd `m`, `2m - B_m^sym ≥ m / D_eff` and
    `B_m^sym < 2m` on the concrete phihat-support. -/
theorem bsym_bound_odd (m : ℕ) [NeZero m] (hodd : Odd m) (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m)) :
    (2 * m : ℚ) - @Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
        inferInstance (suppAct m s) inferInstance
      ≥ (m : ℚ) / ((OrbitPair.Deff m).toNat : ℚ)
    ∧ @Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
        inferInstance (suppAct m s) inferInstance
      < (2 * m : ℚ) := by
  classical
  letI := suppAct m s
  have hm : 0 < m := by
    rcases hodd with ⟨k, hk⟩
    omega
  have hD : Fintype.card ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
      = Am m * Am m := by
    rw [Fintype.card_coe, support_card_eq_Deff_toNat m s hs, Deff_eq_Am_sq m hodd]
    rw [← Nat.cast_pow, Int.toNat_natCast, pow_two]
  have hD' : Fintype.card ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
      = (OrbitPair.Deff m).toNat := by
    rw [Fintype.card_coe]
    exact support_card_eq_Deff_toNat m s hs
  have hG : Fintype.card (DihedralGroup m) = 2 * m := DihedralGroup.card
  have hρ1 : DihedralGroup.sr (0 : ZMod m) ≠ 1 := by
    rw [DihedralGroup.one_def]
    intro h
    injection h
  have hmain := Parity.sym_bound m hm (Am m) (Am_odd m) hD hG
    (DihedralGroup.sr 0) (DihedralGroup.sr_mul_self 0) hρ1
  rw [hD'] at hmain
  exact hmain

/-- 154, conditional variant: the same conclusion whenever
    `2m` does not divide the support size. -/
theorem bsym_bound_of_not_dvd (m : ℕ) [NeZero m] (hm : 0 < m) (s : ℤ)
    (hs : IsCoprime s (Defs.Dm m))
    (hnot : ¬ (2 * m
      ∣ (OrbitPair.support m (OrbitPairFull.phihatFix m s)).card)) :
    (2 * m : ℚ) - @Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
        inferInstance (suppAct m s) inferInstance
      ≥ (m : ℚ) / ((OrbitPair.Deff m).toNat : ℚ)
    ∧ @Parity.Bsym (DihedralGroup m)
        ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
        inferInstance (suppAct m s) inferInstance
      < (2 * m : ℚ) := by
  classical
  letI := suppAct m s
  have hG : Fintype.card (DihedralGroup m) = 2 * m := DihedralGroup.card
  have hnot' : ¬ (2 * m
      ∣ Fintype.card ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))) := by
    rw [Fintype.card_coe]
    exact hnot
  have hD' : Fintype.card ↥(OrbitPair.support m (OrbitPairFull.phihatFix m s))
      = (OrbitPair.Deff m).toNat := by
    rw [Fintype.card_coe]
    exact support_card_eq_Deff_toNat m s hs
  have hmain := Parity.sym_bound_of_not_dvd m hm hG hnot'
  rw [hD'] at hmain
  exact hmain

/-- 154, the `m = 6` example from the boundary (`D_eff 6 = 4900`,
    `12 ∤ 4900`). -/
theorem bsym_bound_six (s : ℤ) (hs : IsCoprime s (Defs.Dm 6)) :
    (2 * 6 : ℚ) - @Parity.Bsym (DihedralGroup 6)
        ↥(OrbitPair.support 6 (OrbitPairFull.phihatFix 6 s))
        inferInstance (suppAct 6 s) inferInstance
      ≥ (6 : ℚ) / ((OrbitPair.Deff 6).toNat : ℚ)
    ∧ @Parity.Bsym (DihedralGroup 6)
        ↥(OrbitPair.support 6 (OrbitPairFull.phihatFix 6 s))
        inferInstance (suppAct 6 s) inferInstance
      < (2 * 6 : ℚ) := by
  have hnot : ¬ (2 * 6
      ∣ (OrbitPair.support 6 (OrbitPairFull.phihatFix 6 s)).card) := by
    have hcard : (OrbitPair.support 6 (OrbitPairFull.phihatFix 6 s)).card
        = 4900 := by
      rw [support_card_eq_Deff_toNat 6 s hs]
      have h6 : OrbitPair.Deff 6 = 4900 := OrbitPairFull.Deff_table_full.2.2.2.1
      rw [h6]
      rfl
    rw [hcard]
    decide
  exact bsym_bound_of_not_dvd 6 (by norm_num) s hs hnot

/- Axiom audit for the main theorems of this module. -/
#print axioms v4_card_eq_four
#print axioms Deff_eq_Am_sq
#print axioms support_card_eq_Deff_toNat
#print axioms bsym_bound_odd
#print axioms bsym_bound_of_not_dvd
#print axioms bsym_bound_six
