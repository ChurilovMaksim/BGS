import Bgs.LineIAliasing
import Bgs.LineISummable

/-!
# BGS-TRACE-214 — Lemma I5′: Fourier expansion of weighted horocycle sums of `|Z_ν|²`

Source: registry statement of `BGS-TRACE-214`.  Notation of `Bgs.LineIAliasing` (finitely supported kick `Φ̂` on `s`,
integer phases `P(n)`, `Z(θ) = ∑_n Φ̂(n) e(−θP(n))`, `Z_ν = Z(ν/M)`, `M = 2h`).  The weight is
`f(z_ν) = ∑_k c_k e(kν/M)` with `c_k = c_k(1/2h)` and `∑_k |c_k| < ∞` (the Fourier expansion of a 1-periodic `f` at height
`1/2h`, `z_ν = (ν + i)/2h`; only these values of `f` enter).  `C(k) = ∑_{n,n′} Φ̂(n) conj Φ̂(n′) 1[P(n) − P(n′) ≡ k mod M]`,
and `c_M(x) = ∑_{ν mod M, (ν,M)=1} e(νx/M)` is the Ramanujan sum.

* `char_sum` : `∑_{ν<M} |Z_ν|² e(kν/M) = M·C(k)`;
* `horocycle_all` (a) : `∑_{ν mod M} |Z_ν|² f(z_ν) = M ∑_k c_k C(k)`;
* `horocycle_units` (b) : `∑_{ν unit} |Z_ν|² f(z_ν) = ∑_k c_k ∑_{n,n′} Φ̂(n) conj Φ̂(n′) c_M(k − P(n) + P(n′))`.

**Partial coverage:** finitely supported kicks (any finite support; the `c_k` only absolutely summable); the remarks on the
diagonal class and on the use for R′ are not part of the claim's identities and are not formalized.
All proofs are kernel-checked.
-/

namespace Bgs.LineIHorocycle

open Finset ComplexConjugate Bgs.LineN4Gauge Bgs.LineIAliasing

variable {ι : Type*} (s : Finset ι) (Φ : ι → ℂ) (P : ι → ℤ)

/-- `C(k) = ∑_{n,n′} Φ̂(n) conj Φ̂(n′) 1[P(n) − P(n′) ≡ k mod M]`. -/
noncomputable def C (M : ℕ) (k : ℤ) : ℂ :=
  ∑ n ∈ s, ∑ n' ∈ s, Φ n * conj (Φ n') * (if (M : ℤ) ∣ (P n - P n' - k) then 1 else 0)

/-- The Ramanujan sum `c_M(x) = ∑_{ν mod M, (ν, M) = 1} e(νx/M)`. -/
noncomputable def ram (M : ℕ) (x : ℤ) : ℂ :=
  ∑ ν ∈ (range M).filter (fun ν => Nat.Coprime ν M), e ((ν : ℂ) * x / M)

/-- The weight `f(z_ν) = ∑_k c_k e(kν/M)`. -/
noncomputable def f (c : ℤ → ℂ) (M : ℕ) (ν : ℕ) : ℂ := ∑' k : ℤ, c k * e ((k : ℂ) * ν / M)

theorem e_real_arg (k : ℤ) (ν M : ℕ) : (k : ℂ) * ν / M = (((k : ℝ) * ν / M : ℝ) : ℂ) := by push_cast; ring

theorem pair_char (N : Finset ℕ) (M : ℕ) (k : ℤ) :
    ∑ ν ∈ N, Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ) * conj (Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ)) * e ((k : ℂ) * ν / M)
      = ∑ n ∈ s, ∑ n' ∈ s, Φ n * conj (Φ n') * ∑ ν ∈ N, e ((ν : ℂ) * ((k - P n + P n' : ℤ) : ℂ) / M) := by
  simp_rw [Z_mul_conj, sum_mul]
  rw [sum_comm]
  refine sum_congr rfl (fun n _ => ?_)
  rw [sum_comm]
  refine sum_congr rfl (fun n' _ => ?_)
  rw [Finset.mul_sum]
  refine sum_congr rfl (fun ν _ => ?_)
  rw [mul_assoc, e_add]
  congr 2
  push_cast; ring

theorem char_sum {M : ℕ} (hM : 0 < M) (k : ℤ) :
    ∑ ν ∈ range M, Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ) * conj (Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ)) * e ((k : ℂ) * ν / M)
      = (M : ℂ) * C s Φ P M k := by
  rw [pair_char, C, Finset.mul_sum]
  refine sum_congr rfl (fun n _ => ?_)
  rw [Finset.mul_sum]
  refine sum_congr rfl (fun n' _ => ?_)
  have : ∀ ν : ℕ, e ((ν : ℂ) * ((k - P n + P n' : ℤ) : ℂ) / M) = e (-(ν : ℂ) * ((P n - P n' - k : ℤ) : ℂ) / M) := by
    intro ν; congr 1; push_cast; ring
  simp_rw [this]
  rw [geom_root_sum hM]
  split_ifs <;> ring

theorem summable_weight (c : ℤ → ℂ) (hc : Summable (fun k => ‖c k‖)) (M ν : ℕ) (a : ℂ) :
    Summable (fun k : ℤ => a * (c k * e ((k : ℂ) * ν / M))) := by
  refine Summable.mul_left a (Summable.of_norm_bounded hc (fun k => ?_))
  rw [norm_mul, e_real_arg, Bgs.LineISummable.norm_e_real, mul_one]

theorem interchange (N : Finset ℕ) (M : ℕ) (c : ℤ → ℂ) (hc : Summable (fun k => ‖c k‖)) :
    ∑ ν ∈ N, Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ) * conj (Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ)) * f c M ν
      = ∑' k : ℤ, c k * ∑ ν ∈ N, Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ) * conj (Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ))
          * e ((k : ℂ) * ν / M) := by
  unfold f
  simp_rw [← tsum_mul_left]
  rw [← Summable.tsum_finsetSum (fun ν _ => summable_weight c hc M ν _)]
  congr 1; funext k
  rw [Finset.mul_sum]
  refine sum_congr rfl (fun ν _ => ?_)
  ring

/-- **(a)** `∑_{ν mod M} |Z_ν|² f(z_ν) = M ∑_k c_k C(k)`. -/
theorem horocycle_all {M : ℕ} (hM : 0 < M) (c : ℤ → ℂ) (hc : Summable (fun k => ‖c k‖)) :
    ∑ ν ∈ range M, Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ) * conj (Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ)) * f c M ν
      = (M : ℂ) * ∑' k : ℤ, c k * C s Φ P M k := by
  rw [interchange s Φ P _ M c hc, ← tsum_mul_left]
  congr 1; funext k
  rw [char_sum s Φ P hM]; ring

/-- **(b)** `∑_{ν unit} |Z_ν|² f(z_ν) = ∑_k c_k ∑_{n,n′} Φ̂(n) conj Φ̂(n′) c_M(k − P(n) + P(n′))`. -/
theorem horocycle_units (M : ℕ) (c : ℤ → ℂ) (hc : Summable (fun k => ‖c k‖)) :
    ∑ ν ∈ (range M).filter (fun ν => Nat.Coprime ν M),
        Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ) * conj (Z s Φ P (((ν : ℝ) / M : ℝ) : ℂ)) * f c M ν
      = ∑' k : ℤ, c k * ∑ n ∈ s, ∑ n' ∈ s, Φ n * conj (Φ n') * ram M (k - P n + P n') := by
  rw [interchange s Φ P _ M c hc]
  congr 1; funext k
  rw [pair_char]
  rfl

end Bgs.LineIHorocycle
