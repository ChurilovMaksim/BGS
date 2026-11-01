import Bgs.LineN3SignConj

/-!
# BGS-TRACE-293 at composite levels — via the inheritance theorem (BGS-TRACE-228) as hypothesis

Source: registry statements of `BGS-TRACE-293` and `BGS-TRACE-228`.  For coprime odd `c, e` with `ce ∣ h_m`, BGS-TRACE-228
gives `W_{ce, eβ′}(±ρ) = (n_e/e²) W_{c,β′}(±ρ)` with the **same** real `n_e ≥ 0` for both signs of `ρ`.

* `inherit_conj` : if `W_c(−ρ) = conj W_c(ρ)` and both signs inherit with the same real factor, then
  `W_{ce}(−ρ) = conj W_{ce}(ρ)`;
* `prime_inherit_conj` : with `c = q` prime (`q ∥ d`) this combines with `Bgs.LineN3SignConj.W_sign_conj`:
  `W_{qe, eβ′}(−ρ) = conj W_{qe, eβ′}(ρ)`.

**Partial coverage:** the inheritance theorem BGS-TRACE-228 (CRT and Gauss sums) is a **hypothesis**, not formalized;
levels with no prime `q ∥ d` (e.g. prime powers `q^k`, `k ≥ 2`) are covered only through a base level `c` at which the
symmetry is assumed.  All proofs are kernel-checked.
-/

namespace Bgs.LineN3SignConjComposite

open ComplexConjugate Bgs.LineJ3PrimeLevel Bgs.LineN3SignConj

theorem inherit_conj (Wc_pos Wc_neg Wd_pos Wd_neg : ℂ) (r : ℝ) (hc : Wc_neg = conj Wc_pos)
    (hpos : Wd_pos = (r : ℂ) * Wc_pos) (hneg : Wd_neg = (r : ℂ) * Wc_neg) : Wd_neg = conj Wd_pos := by
  rw [hneg, hpos, hc, map_mul, Complex.conj_ofReal]

theorem prime_inherit_conj {q : ℕ} [Fact q.Prime] (c cbar y ν0 ν0' N : ZMod q) (hneg : ν0' = -ν0)
    (Wd_pos Wd_neg : ℂ) (ne e : ℕ)
    (hpos : Wd_pos = ((ne / (e : ℝ) ^ 2 : ℝ) : ℂ) * W N (label c cbar y ν0))
    (hneg' : Wd_neg = ((ne / (e : ℝ) ^ 2 : ℝ) : ℂ) * W N (label c cbar y ν0')) :
    Wd_neg = conj Wd_pos :=
  inherit_conj _ _ _ _ _ (W_sign_conj c cbar y ν0 ν0' N hneg) hpos hneg'

end Bgs.LineN3SignConjComposite
