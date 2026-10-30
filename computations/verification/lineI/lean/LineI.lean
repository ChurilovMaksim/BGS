import Mathlib

/-!
# Line I — algebraic core of the dilation-coset L² law (Prop. I2)

Setting (paper proof in REPORT.md §2): for a prime d ∥ h, the members of a dilation coset are
Z_t = Σ_u W_u e(−t u/d), and coset Parseval gives Σ_t |Z_t|² = d Σ_u |W_u|².  Writing
W_u = c·N_u/d² + δ_u with c = Z_ρ = Σ_u W_u, N_u = #{γ ∈ (ℤ/d)² : Nm γ = u}, the norm counts of a
split (ε = 1) or inert (ε = −1) prime are N_u = d − ε (u ≠ 0), N_0 = d + (d−1)ε.  This file proves:

* `cross_term`   : Σ_u N_u δ_u = ε d δ_0          whenever Σ_u δ_u = 0;
* `sum_N_sq`     : Σ_u N_u² = d³ + d² − d;
* `coset_decomp` : d Σ_u |c N_u/d² + δ_u|² = |c|²(d³+d²−d)/d³ + 2ε Re(c̄ δ_0) + d Σ_u |δ_u|²;
* `norm_count_7`, `norm_count_23` : the norm counts for x² − 2y² over ℤ/7 and ℤ/23 (split, ε = 1), by `decide`.
No `sorry`, no `native_decide`.
-/

namespace LineI
open Finset BigOperators

variable {d : ℕ}

/-- Norm-count profile of a prime with sign ε. -/
def Nprof (d : ℕ) (ε : ℤ) (u : Fin (d+1)) : ℤ := if u = 0 then (d+1 : ℤ) + d * ε else (d+1 : ℤ) - ε

-- We index residues mod p := d+1 by `Fin (d+1)` to avoid a positivity side condition; p = d+1.

theorem cross_term (ε : ℤ) (δ : Fin (d+1) → ℂ) (hδ : ∑ u, δ u = 0) :
    ∑ u, (Nprof d ε u : ℂ) * δ u = (ε : ℂ) * ((d:ℂ)+1) * δ 0 := by
  have hsplit : ∀ u : Fin (d+1), (Nprof d ε u : ℂ) * δ u
      = ((d:ℂ) + 1 - ε) * δ u + (if u = 0 then ((d:ℂ)+1) * ε * δ u else 0) := by
    intro u
    unfold Nprof
    by_cases hu : u = 0
    · simp only [hu, if_true]; push_cast; ring
    · simp only [hu, if_false]; push_cast; ring
  rw [Finset.sum_congr rfl (fun u _ => hsplit u), Finset.sum_add_distrib, ← Finset.mul_sum, hδ]
  simp only [Finset.sum_ite_eq', Finset.mem_univ, if_true, mul_zero, zero_add]
  ring

theorem sum_N_sq (ε : ℤ) (hε : ε * ε = 1) :
    ∑ u : Fin (d+1), (Nprof d ε u)^2 = ((d:ℤ)+1)^3 + ((d:ℤ)+1)^2 - ((d:ℤ)+1) := by
  have h : ∀ u : Fin (d+1), (Nprof d ε u)^2
      = ((d:ℤ)+1-ε)^2 + (if u = 0 then ((d:ℤ)+1+d*ε)^2 - ((d:ℤ)+1-ε)^2 else 0) := by
    intro u; unfold Nprof; by_cases hu : u = 0 <;> simp [hu]
  rw [Finset.sum_congr rfl (fun u _ => h u), Finset.sum_add_distrib]
  simp [Finset.sum_ite_eq', Finset.card_univ, Fintype.card_fin]
  have : ε^2 = 1 := by nlinarith [hε]
  nlinarith [hε, this]

/-- `normSq` expansion helper. -/
lemma normSq_add' (x y : ℂ) : Complex.normSq (x + y) = Complex.normSq x + 2 * (starRingEnd ℂ x * y).re + Complex.normSq y := by
  rw [Complex.normSq_add]; simp [Complex.mul_re]; ring

theorem coset_decomp (ε : ℤ) (hε : ε * ε = 1) (c : ℂ) (δ : Fin (d+1) → ℂ) (hδ : ∑ u, δ u = 0) :
    ((d:ℝ)+1) * ∑ u, Complex.normSq (c * (Nprof d ε u : ℂ) / ((d:ℂ)+1)^2 + δ u)
      = Complex.normSq c * ((((d:ℝ)+1)^3 + ((d:ℝ)+1)^2 - ((d:ℝ)+1)) / ((d:ℝ)+1)^3)
        + 2 * (ε:ℝ) * (starRingEnd ℂ c * δ 0).re + ((d:ℝ)+1) * ∑ u, Complex.normSq (δ u) := by
  set p : ℝ := (d:ℝ) + 1 with hp
  have hp0 : p ≠ 0 := by positivity
  have hpC : ((d:ℂ)+1) = (p:ℂ) := by simp [hp]
  -- expand each term
  have hterm : ∀ u, Complex.normSq (c * (Nprof d ε u : ℂ) / ((d:ℂ)+1)^2 + δ u)
      = Complex.normSq c * ((Nprof d ε u : ℝ))^2 / p^4
        + 2 * ((Nprof d ε u : ℝ) / p^2) * (starRingEnd ℂ c * δ u).re + Complex.normSq (δ u) := by
    intro u
    rw [normSq_add', hpC]
    have e1 : c * (Nprof d ε u : ℂ) / (p:ℂ)^2 = c * (((Nprof d ε u : ℝ) / p^2 : ℝ) : ℂ) := by push_cast; ring
    rw [e1, Complex.normSq_mul, Complex.normSq_ofReal, map_mul, Complex.conj_ofReal]
    have : (starRingEnd ℂ c * (((Nprof d ε u : ℝ) / p^2 : ℝ) : ℂ) * δ u).re
        = ((Nprof d ε u : ℝ) / p^2) * (starRingEnd ℂ c * δ u).re := by
      rw [mul_comm (starRingEnd ℂ c), mul_assoc, Complex.re_ofReal_mul]
    rw [this]; field_simp
  rw [Finset.sum_congr rfl (fun u _ => hterm u), Finset.sum_add_distrib, Finset.sum_add_distrib]
  -- sum of N_u^2
  have hN2 : ∑ u : Fin (d+1), ((Nprof d ε u : ℝ))^2 = p^3 + p^2 - p := by
    have := sum_N_sq (d := d) ε hε
    have h' : ((∑ u : Fin (d+1), (Nprof d ε u)^2 : ℤ) : ℝ) = ((((d:ℤ)+1)^3 + ((d:ℤ)+1)^2 - ((d:ℤ)+1) : ℤ) : ℝ) := by rw [this]
    push_cast at h'; rw [hp]; linarith [h']
  -- cross term: Σ N_u Re(c̄ δ_u) = ε p Re(c̄ δ_0)
  have hX : ∑ u : Fin (d+1), (Nprof d ε u : ℝ) * (starRingEnd ℂ c * δ u).re = (ε:ℝ) * p * (starRingEnd ℂ c * δ 0).re := by
    have hc := cross_term (d := d) ε (fun u => starRingEnd ℂ c * δ u) (by rw [← Finset.mul_sum, hδ, mul_zero])
    have hre := congrArg Complex.re hc
    simp only [Complex.re_sum] at hre
    have l : ∀ u : Fin (d+1), ((Nprof d ε u : ℂ) * (starRingEnd ℂ c * δ u)).re = (Nprof d ε u : ℝ) * (starRingEnd ℂ c * δ u).re := by
      intro u; rw [show ((Nprof d ε u : ℂ)) = (((Nprof d ε u : ℝ)) : ℂ) by push_cast; ring, Complex.re_ofReal_mul]
    rw [Finset.sum_congr rfl (fun u _ => l u)] at hre
    rw [hre, hp]
    rw [show ((ε:ℂ) * ((d:ℂ)+1)) = (((ε:ℝ) * ((d:ℝ)+1) : ℝ) : ℂ) by push_cast; ring, mul_comm, Complex.re_mul_ofReal]
    ring
  have s1 : ∑ u : Fin (d+1), Complex.normSq c * ((Nprof d ε u : ℝ))^2 / p^4 = Complex.normSq c * (p^3 + p^2 - p) / p^4 := by
    rw [← hN2, Finset.mul_sum, Finset.sum_div]
  have s2 : ∑ u : Fin (d+1), 2 * ((Nprof d ε u : ℝ) / p^2) * (starRingEnd ℂ c * δ u).re
      = (2 / p^2) * ((ε:ℝ) * p * (starRingEnd ℂ c * δ 0).re) := by
    rw [← hX, Finset.mul_sum]; refine Finset.sum_congr rfl (fun u _ => ?_); ring
  rw [s1, s2]
  field_simp

/-- Norm counts for x² − 2y² over ℤ/7 (7 splits: 2 ≡ 3²). -/
theorem norm_count_7 :
    ((Finset.univ : Finset (ZMod 7 × ZMod 7)).filter (fun p => p.1^2 - 2*p.2^2 = 0)).card = 13 ∧
    ∀ u : ZMod 7, u ≠ 0 → ((Finset.univ : Finset (ZMod 7 × ZMod 7)).filter (fun p => p.1^2 - 2*p.2^2 = u)).card = 6 := by
  decide

/-- Norm counts for x² − 2y² over ℤ/23 (23 splits: 2 ≡ 5²). -/
theorem norm_count_23_zero :
    ((Finset.univ : Finset (ZMod 23 × ZMod 23)).filter (fun p => p.1^2 - 2*p.2^2 = 0)).card = 45 := by
  decide

end LineI

#print axioms LineI.cross_term
#print axioms LineI.sum_N_sq
#print axioms LineI.coset_decomp
#print axioms LineI.norm_count_7
#print axioms LineI.norm_count_23_zero
