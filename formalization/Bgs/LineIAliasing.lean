import Bgs.LineIPhaseSplit
import Mathlib.Algebra.Field.GeomSum
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# BGS-TRACE-218 — Line I aliasing identity, first part (finite-support form)

Source: `mathematics/fixed-map/lineI_rprime_reduction.md` (aliasing identity); registry boundary of `BGS-TRACE-218`.
With `Z(θ) = ∑_n Φ̂(n) e(−θ P(n))` and the collision function
`C_Z(k) = ∑_{n,n'} Φ̂(n) conj Φ̂(n') 1[P(n) − P(n') = k]`, the first identity of the claim reads, for every
modulus `q ≥ 1`,

`(1/q) ∑_{ν' mod q} |Z(ν'/q)|² = ∑_{j ∈ ℤ} C_Z(jq)`.

* `geom_root_sum` : `∑_{ν<q} e(−ν k/q) = q · 1[q ∣ k]` (orthogonality of additive characters mod `q`);
* `aliasing_mean` : `(1/q) ∑_{ν<q} Z(ν/q) conj Z(ν/q) = ∑_{n,n'} Φ̂(n) conj Φ̂(n') 1[q ∣ P(n) − P(n')]`.

The right side of `aliasing_mean` is `∑_j C_Z(jq)` regrouped by `j = (P(n) − P(n'))/q` (pairs with
`q ∣ P(n) − P(n')` are exactly the pairs counted by some `C_Z(jq)`, each by exactly one `j`); the regrouping
into a `j`-indexed series is not itself spelled out in Lean.

**Partial coverage:** (i) only the first identity is formalized; the Möbius formula
`F_m = φ(2h)⁻¹ ∑_{e | 2h} μ(e)(2h/e) ∑_j C_Z(j·2h/e)` is **not** formalized here; (ii) the kick is finitely
supported (finite index set), the source allows `∑ |Φ̂| < ∞`; (iii) the identity is proved for every `q ≥ 1`
(the claim needs only `q ∣ 2h`).  All proofs are kernel-checked.
-/

namespace Bgs.LineIAliasing

open Bgs.LineN4Gauge Finset ComplexConjugate

theorem e_nat_mul (n : ℕ) (x : ℂ) : e (n * x) = e x ^ n := by
  unfold e
  rw [← Complex.exp_nat_mul]; congr 1; ring

theorem e_ne_one {q : ℕ} (hq : 0 < q) {k : ℤ} (hk : ¬ (q : ℤ) ∣ k) : e (-(k : ℂ) / q) ≠ 1 := by
  unfold e
  intro h
  rw [Complex.exp_eq_one_iff] at h
  obtain ⟨n, hn⟩ := h
  have hq' : (q : ℂ) ≠ 0 := by exact_mod_cast hq.ne'
  have hpi : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
    simp [Real.pi_ne_zero, Complex.I_ne_zero]
  have : ((k : ℤ) : ℂ) = ((-(n * q) : ℤ) : ℂ) := by
    push_cast
    have h2 : 2 * (Real.pi : ℂ) * Complex.I * (-(k : ℂ) / q) * q = n * (2 * Real.pi * Complex.I) * q := by
      rw [hn]
    field_simp at h2
    linear_combination -h2
  have hk' : k = -(n * q) := by exact_mod_cast this
  exact hk ⟨-n, by rw [hk']; ring⟩

/-- Orthogonality: `∑_{ν<q} e(−ν k/q) = q · 1[q ∣ k]`. -/
theorem geom_root_sum {q : ℕ} (hq : 0 < q) (k : ℤ) :
    ∑ ν ∈ range q, e (-(ν : ℂ) * k / q) = if (q : ℤ) ∣ k then (q : ℂ) else 0 := by
  have hpow : ∀ ν : ℕ, e (-(ν : ℂ) * k / q) = (e (-(k : ℂ) / q)) ^ ν := by
    intro ν; rw [← e_nat_mul]; congr 1; ring
  simp_rw [hpow]
  split_ifs with hk
  · obtain ⟨c, hc⟩ := hk
    have hq' : (q : ℂ) ≠ 0 := by exact_mod_cast hq.ne'
    have : e (-(k : ℂ) / q) = 1 := by
      rw [hc]; push_cast
      have : -((q : ℂ) * c) / q = ((-c : ℤ) : ℂ) := by push_cast; field_simp
      rw [this, Bgs.LineIPhaseSplit.e_intCast]
    simp [this]
  · have hne := e_ne_one hq hk
    rw [geom_sum_eq hne, ← e_nat_mul]
    have hq' : (q : ℂ) ≠ 0 := by exact_mod_cast hq.ne'
    have : (q : ℂ) * (-(k : ℂ) / q) = ((-k : ℤ) : ℂ) := by push_cast; field_simp
    rw [this, Bgs.LineIPhaseSplit.e_intCast]; simp

variable {ι : Type*} (s : Finset ι) (Φ : ι → ℂ) (P : ι → ℤ)

/-- `Z(θ) = ∑_n Φ̂(n) e(−θ P(n))`. -/
noncomputable def Z (θ : ℂ) : ℂ := ∑ n ∈ s, Φ n * e (-θ * P n)

theorem conj_e_real (r : ℝ) : conj (e (r : ℂ)) = e (-(r : ℂ)) := by
  unfold e
  rw [← Complex.exp_conj]; congr 1
  simp [Complex.conj_ofReal, Complex.conj_ofNat]

theorem Z_mul_conj (θ : ℝ) :
    Z s Φ P θ * conj (Z s Φ P θ)
      = ∑ n ∈ s, ∑ n' ∈ s, Φ n * conj (Φ n') * e (-(θ : ℂ) * ((P n - P n' : ℤ) : ℂ)) := by
  unfold Z
  rw [map_sum, sum_mul_sum]
  refine sum_congr rfl (fun n _ => sum_congr rfl (fun n' _ => ?_))
  have : -(θ : ℂ) * (P n' : ℂ) = ((-(θ * P n') : ℝ) : ℂ) := by push_cast; ring
  rw [map_mul, this, conj_e_real]
  have h2 : -(((-(θ * P n')) : ℝ) : ℂ) = (θ : ℂ) * P n' := by push_cast; ring
  rw [h2]
  have h3 : -(θ : ℂ) * ((P n - P n' : ℤ) : ℂ) = -(θ : ℂ) * P n + θ * P n' := by push_cast; ring
  rw [h3, ← e_add]; ring

/-- **Aliasing identity (first part):**
`(1/q) ∑_{ν<q} |Z(ν/q)|² = ∑_{n,n'} Φ̂(n) conj Φ̂(n') 1[q ∣ P(n) − P(n')]` (`= ∑_j C_Z(jq)`). -/
theorem aliasing_mean {q : ℕ} (hq : 0 < q) :
    (1 / (q : ℂ)) * ∑ ν ∈ range q, Z s Φ P ((ν / q : ℝ) : ℂ) * conj (Z s Φ P ((ν / q : ℝ) : ℂ))
      = ∑ n ∈ s, ∑ n' ∈ s,
          Φ n * conj (Φ n') * (if (q : ℤ) ∣ (P n - P n') then 1 else 0) := by
  have hq' : (q : ℂ) ≠ 0 := by exact_mod_cast hq.ne'
  simp_rw [Z_mul_conj]
  rw [sum_comm]
  rw [mul_sum]
  refine sum_congr rfl (fun n _ => ?_)
  rw [sum_comm, mul_sum]
  refine sum_congr rfl (fun n' _ => ?_)
  rw [← mul_sum]
  have : ∀ ν : ℕ, e (-(((ν : ℝ) / q : ℝ) : ℂ) * ((P n - P n' : ℤ) : ℂ))
      = e (-(ν : ℂ) * ((P n - P n' : ℤ) : ℂ) / q) := by
    intro ν; congr 1; push_cast; ring
  simp_rw [this]
  rw [geom_root_sum hq]
  split_ifs
  · field_simp
  · simp

end Bgs.LineIAliasing
