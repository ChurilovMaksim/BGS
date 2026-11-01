import Bgs.LineIAliasing
import Mathlib.NumberTheory.ArithmeticFunction.Moebius
import Mathlib.Data.Nat.Totient

/-!
# BGS-TRACE-218 — Line I aliasing identity, Möbius part (finite-support form)

Source: `mathematics/fixed-map/lineI_rprime_reduction.md` (aliasing identity, display after Prop I1); registry boundary of
`BGS-TRACE-218`.  With `M = 2h`, `F_m = φ(M)⁻¹ ∑_{ν unit mod M} |Z_m(ν/M)|²` and the notation of `Bgs.LineIAliasing`:

* `sum_moebius_divisors` : `∑_{d ∣ n} μ(d) = 1[n = 1]`;
* `sum_units_moebius` : `∑_{ν<M, (ν,M)=1} f(ν) = ∑_{e ∣ M} μ(e) ∑_{ν′ < M/e} f(eν′)` (Möbius sieve over the units mod `M`);
* `Fm_moebius` : `F_m = φ(M)⁻¹ ∑_{e ∣ M} μ(e)(M/e) ∑_{n,n′} Φ̂(n) conj Φ̂(n′) 1[(M/e) ∣ P(n) − P(n′)]`,
  i.e. `F_m = φ(2h)⁻¹ ∑_{e ∣ 2h} μ(e)(2h/e) ∑_j C_Z(j·2h/e)` (the inner sum is `∑_j C_Z(j·2h/e)` regrouped by `j`, as in
  `Bgs.LineIAliasing.aliasing_mean`).

**Partial coverage:** finitely supported kick (the absolutely summable case of the first identity is in
`Bgs.LineISummable`; the Möbius formula itself is proved here for finite support only); the regrouping into a
`j`-indexed series is stated, not formalized.  The claim's non-claimed heuristics (e > 2 terms, resonant residues) are not
part of the claim.  All proofs are kernel-checked.
-/

namespace Bgs.LineIMoebius

open Finset ComplexConjugate Bgs.LineIAliasing
open scoped ArithmeticFunction.Moebius

theorem sum_moebius_divisors (n : ℕ) :
    ∑ d ∈ n.divisors, ((μ d : ℤ) : ℂ) = if n = 1 then 1 else 0 := by
  have h := congrArg (fun f : ArithmeticFunction ℂ => f n)
    (ArithmeticFunction.coe_moebius_mul_coe_zeta (R := ℂ))
  simp only [ArithmeticFunction.coe_mul_zeta_apply, ArithmeticFunction.intCoe_apply,
    ArithmeticFunction.one_apply] at h
  exact h

theorem sum_units_moebius (M : ℕ) (hM : 0 < M) (f : ℕ → ℂ) :
    ∑ ν ∈ (range M).filter (fun ν => Nat.Coprime ν M), f ν
      = ∑ e ∈ M.divisors, ((μ e : ℤ) : ℂ) * ∑ ν' ∈ range (M / e), f (e * ν') := by
  -- indicator of coprimality via Möbius
  have hind : ∀ ν, (if Nat.Coprime ν M then (1 : ℂ) else 0)
      = ∑ e ∈ M.divisors.filter (fun e => e ∣ ν), ((μ e : ℤ) : ℂ) := by
    intro ν
    have hdiv : M.divisors.filter (fun e => e ∣ ν) = (Nat.gcd ν M).divisors := by
      ext e
      simp only [mem_filter, Nat.mem_divisors]
      constructor
      · rintro ⟨⟨h1, h2⟩, h3⟩
        exact ⟨Nat.dvd_gcd h3 h1, (Nat.gcd_pos_of_pos_right ν hM).ne'⟩
      · rintro ⟨h1, -⟩
        exact ⟨⟨h1.trans (Nat.gcd_dvd_right ν M), hM.ne'⟩, h1.trans (Nat.gcd_dvd_left ν M)⟩
    rw [hdiv, sum_moebius_divisors]
  rw [sum_filter]
  have : ∀ ν ∈ range M, (if Nat.Coprime ν M then f ν else 0)
      = ∑ e ∈ M.divisors, ((μ e : ℤ) : ℂ) * (if e ∣ ν then f ν else 0) := by
    intro ν _
    have h := hind ν
    rw [sum_filter] at h
    calc (if Nat.Coprime ν M then f ν else 0) = (if Nat.Coprime ν M then (1 : ℂ) else 0) * f ν := by
            split_ifs <;> simp
      _ = _ := by rw [h, sum_mul]; refine sum_congr rfl (fun e _ => ?_); split_ifs <;> simp
  rw [sum_congr rfl this, sum_comm]
  refine sum_congr rfl (fun e he => ?_)
  rw [← mul_sum]
  congr 1
  rw [← sum_filter]
  have heM : e ∣ M := Nat.dvd_of_mem_divisors he
  have he0 : 0 < e := Nat.pos_of_mem_divisors he
  symm
  refine sum_nbij' (fun ν' => e * ν') (fun ν => ν / e) (fun ν' hν' => ?_) (fun ν hν => ?_)
    (fun ν' _ => ?_) (fun ν hν => ?_) (fun ν' _ => rfl)
  · rw [mem_range] at hν'
    rw [mem_filter, mem_range]
    refine ⟨?_, dvd_mul_right e ν'⟩
    obtain ⟨k, hk⟩ := heM
    rw [hk, Nat.mul_div_cancel_left _ he0] at hν'
    rw [hk]; exact Nat.mul_lt_mul_of_pos_left hν' he0
  · rw [mem_filter, mem_range] at hν
    rw [mem_range]
    exact Nat.div_lt_div_of_lt_of_dvd heM hν.1
  · simp [Nat.mul_div_cancel_left _ he0]
  · rw [mem_filter] at hν
    simp [Nat.mul_div_cancel' hν.2]

variable {ι : Type*} (s : Finset ι) (Φ : ι → ℂ) (P : ι → ℤ)

/-- `F_m = φ(M)⁻¹ ∑_{ν unit mod M} |Z(ν/M)|²`. -/
noncomputable def Fm (M : ℕ) : ℂ :=
  ((Nat.totient M : ℂ))⁻¹ * ∑ ν ∈ (range M).filter (fun ν => Nat.Coprime ν M),
    Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ) * conj (Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ))

/-- **Möbius form:** `F_m = φ(M)⁻¹ ∑_{e∣M} μ(e)(M/e) ∑_{n,n′} Φ̂(n) conj Φ̂(n′) 1[(M/e) ∣ P(n) − P(n′)]`. -/
theorem Fm_moebius (M : ℕ) (hM : 0 < M) :
    Fm s Φ P M = ((Nat.totient M : ℂ))⁻¹ * ∑ e ∈ M.divisors, ((μ e : ℤ) : ℂ) * (((M / e : ℕ) : ℂ) *
      ∑ n ∈ s, ∑ n' ∈ s, Φ n * conj (Φ n') * (if ((M / e : ℕ) : ℤ) ∣ (P n - P n') then 1 else 0)) := by
  unfold Fm
  congr 1
  rw [sum_units_moebius M hM]
  refine sum_congr rfl (fun e he => ?_)
  congr 1
  have heM : e ∣ M := Nat.dvd_of_mem_divisors he
  have he0 : 0 < e := Nat.pos_of_mem_divisors he
  have hq : 0 < M / e := Nat.div_pos (Nat.le_of_dvd hM heM) he0
  have hal := aliasing_mean s Φ P hq
  have hq' : ((M / e : ℕ) : ℂ) ≠ 0 := by exact_mod_cast hq.ne'
  have hpt : ∀ ν' : ℕ, (((e * ν' : ℕ) : ℝ) / M : ℝ) = ((ν' : ℝ) / ((M / e : ℕ) : ℝ) : ℝ) := by
    intro ν'
    rw [Nat.cast_div heM (by exact_mod_cast he0.ne')]
    have : (e : ℝ) ≠ 0 := by exact_mod_cast he0.ne'
    have : (M : ℝ) ≠ 0 := by exact_mod_cast hM.ne'
    push_cast; field_simp
  simp_rw [hpt]
  rw [← hal]
  field_simp

end Bgs.LineIMoebius
