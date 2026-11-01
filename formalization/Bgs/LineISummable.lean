import Bgs.LineIAliasing
import Mathlib.Analysis.Normed.Ring.InfiniteSum

/-!
# BGS-TRACE-211 and BGS-TRACE-218 (first identity) — absolutely summable kicks

Sources as in `Bgs.LineIPhaseSplit` and `Bgs.LineIAliasing`; this module removes the finite-support restriction of
those files: the kick `Φ̂` is indexed by an arbitrary type `ι` (e.g. `ℤ^m`) with `∑ |Φ̂(n)| < ∞`
(hypothesis `Summable (‖Φ̂ ·‖)`), as in the registry boundaries ("any kick with ∑|Φ̂| < ∞").  Phases are real
(`ν₀ ∈ ℝ`, integer `δ`, `θ = ν/q`), as in the source (`ν₀` a unit residue).

* `phase_split` : `Z(ν₀ + δ) = Z(ν₀) σ̂(δ)` for every integer `δ`, `Z(ν) = ∑'_n Φ̂(n) e(−νP(n)/M)`,
  `σ(p) = Z(ν₀)⁻¹ ∑'_{P(n) ≡ p} Φ̂(n) e(−ν₀P(n)/M)`, and `sigma_mass` : `∑_p σ(p) = 1` (BGS-TRACE-211);
* `aliasing_mean` : `(1/q) ∑_{ν<q} |Z(ν/q)|² = ∑'_{(n,n′)} Φ̂(n) conj Φ̂(n′) 1[q ∣ P(n) − P(n′)]` (`= ∑_j C_Z(jq)`),
  `Z(θ) = ∑'_n Φ̂(n) e(−θP(n))` (BGS-TRACE-218, first identity).

**Partial coverage:** the regrouping of the pair series into `∑_j C_Z(jq)` is stated, not formalized; the Möbius formula
(`Bgs.LineIMoebius`) is formalized for finite support only.  All proofs are kernel-checked.
-/

namespace Bgs.LineISummable

open Bgs.LineN4Gauge Finset ComplexConjugate

theorem norm_e_real (r : ℝ) : ‖e (r : ℂ)‖ = 1 := by
  unfold e
  have : 2 * (Real.pi : ℂ) * Complex.I * r = ((2 * Real.pi * r : ℝ) : ℂ) * Complex.I := by push_cast; ring
  rw [this, Complex.norm_exp_ofReal_mul_I]

variable {ι : Type*} (Φ : ι → ℂ) (hΦ : Summable (fun n => ‖Φ n‖)) (P : ι → ℤ)

section PhaseSplit
variable (M : ℕ) [NeZero M]

noncomputable def Z (ν : ℝ) : ℂ := ∑' n, Φ n * e (-(ν : ℂ) * P n / M)

noncomputable def sigma (ν0 : ℝ) (p : ZMod M) : ℂ :=
  (Z Φ P M ν0)⁻¹ * ∑' n, (if ((P n : ZMod M) = p) then Φ n * e (-(ν0 : ℂ) * P n / M) else 0)

noncomputable def sigmaHat (ν0 : ℝ) (δ : ℤ) : ℂ :=
  ∑ p : ZMod M, sigma Φ P M ν0 p * e (-(δ : ℂ) * (p.val : ℂ) / M)

omit [NeZero M] in
include hΦ in
theorem summable_term (ν : ℝ) (p : ZMod M) (c : ℂ) (hc : ‖c‖ ≤ 1) :
    Summable (fun n => (if ((P n : ZMod M) = p) then Φ n * e (-(ν : ℂ) * P n / M) else 0) * c) := by
  refine Summable.of_norm_bounded hΦ (fun n => ?_)
  split_ifs
  · rw [norm_mul, norm_mul]
    have : -(ν : ℂ) * P n / M = ((-ν * P n / M : ℝ) : ℂ) := by push_cast; ring
    rw [this, norm_e_real, mul_one]
    calc ‖Φ n‖ * ‖c‖ ≤ ‖Φ n‖ * 1 := mul_le_mul_of_nonneg_left hc (norm_nonneg _)
      _ = ‖Φ n‖ := mul_one _
  · simp

include hΦ in
theorem sigma_mass (ν0 : ℝ) (hZ : Z Φ P M ν0 ≠ 0) : ∑ p : ZMod M, sigma Φ P M ν0 p = 1 := by
  unfold sigma
  rw [← mul_sum]
  have hs := fun p (_ : p ∈ (univ : Finset (ZMod M))) =>
    (summable_term Φ hΦ P M ν0 p 1 (by simp)).congr (fun n => mul_one _)
  rw [← Summable.tsum_finsetSum hs]
  simp only [sum_ite_eq, mem_univ, if_true]
  exact inv_mul_cancel₀ hZ

include hΦ in
/-- **Prop I1 (summable kick):** `Z(ν₀ + δ) = Z(ν₀) σ̂(δ)` for every integer `δ`. -/
theorem phase_split (ν0 : ℝ) (hZ : Z Φ P M ν0 ≠ 0) (δ : ℤ) :
    Z Φ P M (ν0 + δ) = Z Φ P M ν0 * sigmaHat Φ P M ν0 δ := by
  unfold sigmaHat sigma
  simp_rw [mul_assoc, ← tsum_mul_right]
  rw [← mul_sum, ← mul_assoc, mul_inv_cancel₀ hZ, one_mul]
  have hs := fun p (_ : p ∈ (univ : Finset (ZMod M))) =>
    summable_term Φ hΦ P M ν0 p (e (-(δ : ℂ) * (p.val : ℂ) / M)) (by
      have : -(δ : ℂ) * (p.val : ℂ) / M = ((-(δ : ℝ) * p.val / M : ℝ) : ℂ) := by push_cast; ring
      rw [this, norm_e_real])
  rw [← Summable.tsum_finsetSum hs]
  unfold Z
  congr 1; funext n
  simp only [ite_mul, zero_mul, sum_ite_eq, mem_univ, if_true]
  rw [Bgs.LineIPhaseSplit.e_shift P M δ n, mul_assoc, e_add]
  congr 2; push_cast; ring

end PhaseSplit

section Aliasing

/-- `Z(θ) = ∑'_n Φ̂(n) e(−θ P(n))`. -/
noncomputable def Zq (θ : ℝ) : ℂ := ∑' n, Φ n * e (-(θ : ℂ) * P n)

include hΦ in
theorem Zq_mul_conj (θ : ℝ) :
    Zq Φ P θ * conj (Zq Φ P θ)
      = ∑' z : ι × ι, Φ z.1 * conj (Φ z.2) * e (-(θ : ℂ) * ((P z.1 - P z.2 : ℤ) : ℂ)) := by
  unfold Zq
  have hn : ∀ θ' : ℝ, Summable (fun n => ‖Φ n * e (-(θ' : ℂ) * P n)‖) := by
    intro θ'
    refine hΦ.congr (fun n => ?_)
    have : -(θ' : ℂ) * P n = ((-θ' * P n : ℝ) : ℂ) := by push_cast; ring
    rw [norm_mul, this, norm_e_real, mul_one]
  rw [Complex.conj_tsum]
  rw [tsum_mul_tsum_of_summable_norm (hn θ) (by simpa using hn θ)]
  congr 1; funext z
  rw [map_mul]
  have h1 : -(θ : ℂ) * (P z.2 : ℂ) = ((-(θ * P z.2)) : ℝ) := by push_cast; ring
  rw [h1, Bgs.LineIAliasing.conj_e_real]
  have h3 : -(θ : ℂ) * ((P z.1 - P z.2 : ℤ) : ℂ) = -(θ : ℂ) * P z.1 + -(((-(θ * P z.2)) : ℝ) : ℂ) := by
    push_cast; ring
  rw [h3, ← e_add]; ring

include hΦ in
/-- **Aliasing identity (summable kick):** `(1/q) ∑_{ν<q} |Z(ν/q)|² = ∑'_{n,n′} Φ̂(n) conj Φ̂(n′) 1[q ∣ P(n) − P(n′)]`. -/
theorem aliasing_mean {q : ℕ} (hq : 0 < q) :
    (1 / (q : ℂ)) * ∑ ν ∈ range q, Zq Φ P ((ν : ℝ) / q) * conj (Zq Φ P ((ν : ℝ) / q))
      = ∑' z : ι × ι, Φ z.1 * conj (Φ z.2) * (if (q : ℤ) ∣ (P z.1 - P z.2) then 1 else 0) := by
  have hq' : (q : ℂ) ≠ 0 := by exact_mod_cast hq.ne'
  simp_rw [Zq_mul_conj Φ hΦ P]
  have hpair : Summable (fun z : ι × ι => ‖Φ z.1 * conj (Φ z.2)‖) := by
    have := summable_mul_of_summable_norm (R := ℝ) (f := fun n => ‖Φ n‖) (g := fun n => ‖Φ n‖)
      (by simpa using hΦ) (by simpa using hΦ)
    refine this.congr (fun z => ?_)
    simp
  have hs : ∀ ν ∈ range q, Summable (fun z : ι × ι =>
      Φ z.1 * conj (Φ z.2) * e (-(((ν : ℝ) / q : ℝ) : ℂ) * ((P z.1 - P z.2 : ℤ) : ℂ))) := by
    intro ν _
    refine Summable.of_norm_bounded hpair (fun z => ?_)
    rw [norm_mul]
    have : -(((ν : ℝ) / q : ℝ) : ℂ) * ((P z.1 - P z.2 : ℤ) : ℂ) = ((-((ν : ℝ) / q) * (P z.1 - P z.2 : ℤ) : ℝ) : ℂ) := by
      push_cast; ring
    rw [this, norm_e_real, mul_one]
  rw [← Summable.tsum_finsetSum hs, ← tsum_mul_left]
  congr 1; funext z
  rw [← mul_sum]
  have : ∀ ν : ℕ, e (-(((ν : ℝ) / q : ℝ) : ℂ) * ((P z.1 - P z.2 : ℤ) : ℂ))
      = e (-(ν : ℂ) * ((P z.1 - P z.2 : ℤ) : ℂ) / q) := by
    intro ν; congr 1; push_cast; ring
  simp_rw [this]
  rw [Bgs.LineIAliasing.geom_root_sum hq]
  split_ifs
  · field_simp
  · simp

end Aliasing

end Bgs.LineISummable
