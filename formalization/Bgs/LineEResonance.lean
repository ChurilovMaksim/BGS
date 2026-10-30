import Mathlib
import Bgs.LineE

/-!
# Line E, step 2 (Galois-image resonance N ≡ ∓196 mod h_m): finite and algebraic facts

* `nsw_mod7`      : 7 ∣ h_m ↔ 3 ∣ m  (m = 2j+1), via h_{j} mod 7 having period 3 (1, 0, 6).
                    So 49 is a unit mod g'_m = 2h_m exactly when 3 ∤ m: this is the hypothesis of the
                    pure 7-mode corollary Z^{f7}_m(ν) = Z^{k1}_m(49ν) and of the 49-state law.
* `cert49 j s nu li inv kap gam` : for m = 2j+1, h = h_m, the exact coefficientwise identity (cleared denominators)
      −ν y'/g'          ≡ s·X_0/(98D) + κ/8 + γ(M_m + 2⁻¹)/49          (mod 1)
      −2ν y' x_d/g'     ≡ s·2X_d/(98D) + κ/4 + γ(M_d + M_{m−d})/49     (mod 1),   1 ≤ d < m,
  with M_k = li^k·inv mod 49, li = λ⁻¹ mod 49 (√2 ↦ 10), inv = (1 − li^m)⁻¹ mod 49, 196ν + s ≡ 0 (mod h), ν odd.
  These are the coefficient identities of the a = 7 resonance law (phase = s·q(n)/98 + κ(Σn)²/8 + (γ/49)[Σ n_iσ_i + ½Σn_i²]),
  checked by `decide` for m ∈ {5, 7, 11, 13, 17, 19} and s = ±1.  Negative control: a wrong γ fails.
All finite checks by `decide` (kernel evaluation); no `native_decide`, no `sorry`.
-/

namespace Bgs.LineE

theorem nsw_mod7_cycle (j : ℕ) :
    (nsw (3 * j) % 7 = 1 ∧ nsw (3 * j + 1) % 7 = 0 ∧ nsw (3 * j + 2) % 7 = 6) := by
  induction j with
  | zero => decide
  | succ j ih =>
    obtain ⟨h0, h1, h2⟩ := ih
    have e3 : nsw (3 * (j + 1)) = 6 * nsw (3 * j + 2) - nsw (3 * j + 1) := by
      rw [show 3 * (j + 1) = (3 * j + 1) + 2 by ring]; rfl
    have e4 : nsw (3 * (j + 1) + 1) = 6 * nsw (3 * (j + 1)) - nsw (3 * j + 2) := by
      rw [show 3 * (j + 1) + 1 = (3 * j + 2) + 2 by ring, show 3 * (j + 1) = (3 * j + 2) + 1 by ring]; rfl
    have e5 : nsw (3 * (j + 1) + 2) = 6 * nsw (3 * (j + 1) + 1) - nsw (3 * (j + 1)) := by
      rw [show 3 * (j + 1) + 2 = (3 * (j + 1)) + 2 by ring]; rfl
    have a3 : nsw (3 * (j + 1)) % 7 = 1 := by rw [e3]; omega
    have a4 : nsw (3 * (j + 1) + 1) % 7 = 0 := by rw [e4]; omega
    have a5 : nsw (3 * (j + 1) + 2) % 7 = 6 := by rw [e5]; omega
    exact ⟨a3, a4, a5⟩

/-- 7 ∣ h_{2j+1} iff j ≡ 1 (mod 3), i.e. iff 3 ∣ m for m = 2j+1. -/
theorem nsw_mod7 (j : ℕ) : nsw j % 7 = 0 ↔ j % 3 = 1 := by
  obtain ⟨h0, h1, h2⟩ := nsw_mod7_cycle (j / 3)
  have hj : j = 3 * (j / 3) + j % 3 := (Nat.div_add_mod j 3).symm
  have hr : j % 3 < 3 := Nat.mod_lt _ (by norm_num)
  interval_cases hm : j % 3
  · rw [hj]; simp only [Nat.add_zero]; rw [h0]; decide
  · rw [hj]; rw [h1]; decide
  · rw [hj]; rw [h2]; decide

theorem three_dvd_iff (j : ℕ) : j % 3 = 1 ↔ 3 ∣ (2 * j + 1) := by omega

/-- coefficient identities of the a = 7 resonance law (cleared by 392 h²) -/
def cert49 (j : ℕ) (s nu li inv kap gam : ℤ) : Bool :=
  let m := 2 * j + 1
  let h := nsw j
  let xm := (xy m).1
  let ym := (xy m).2
  let D := 2 * (xm - 1)
  let yp := ym / h
  let X : ℕ → ℤ := fun d => if d = 0 then ym else ym * (xy d).1 - (xm - 1) * (xy d).2
  let M : ℕ → ℤ := fun k => (li ^ k * inv) % 49
  let Q := 392 * h ^ 2
  decide (D = 4 * h ^ 2) && decide (ym % h = 0) && decide (nu % 2 = 1) &&
  decide ((196 * nu + s) % h = 0) && decide ((23 * li) % 49 = 1) && decide ((10 * 10) % 49 = 2) &&
  decide (((1 - li ^ m) * inv) % 49 = 1) && decide (s = 1 ∨ s = -1) &&
  decide ((-nu * yp * 196 * h - s * X 0 - kap * 49 * h ^ 2 - gam * (M m + 25) * 8 * h ^ 2) % Q = 0) &&
  (List.range m).all (fun d => d = 0 ||
     decide ((-2 * nu * yp * (xy d).1 * 196 * h - s * 2 * X d - kap * 98 * h ^ 2
              - gam * (M d + M (m - d)) * 8 * h ^ 2) % Q = 0))

theorem cert49_5p  : cert49 2 1 73 32 13 7 11 = true := by decide
theorem cert49_5m  : cert49 2 (-1) 9 32 13 1 38 = true := by decide
theorem cert49_7p  : cert49 3 1 189 32 23 5 11 = true := by decide
theorem cert49_7m  : cert49 3 (-1) 289 32 23 3 38 = true := by decide
theorem cert49_11p : cert49 5 1 12717 32 6 1 11 = true := by decide
theorem cert49_11m : cert49 5 (-1) 3521 32 6 7 38 = true := by decide
theorem cert49_13p : cert49 6 1 74603 32 16 7 11 = true := by decide
theorem cert49_13m : cert49 6 (-1) 20039 32 16 1 38 = true := by decide
theorem cert49_17p : cert49 8 1 565913 32 48 3 11 = true := by decide
theorem cert49_17m : cert49 8 (-1) 2649129 32 48 5 38 = true := by decide
theorem cert49_19p : cert49 9 1 12763307 32 9 1 11 = true := by decide
theorem cert49_19m : cert49 9 (-1) 5975331 32 9 7 38 = true := by decide

/-- negative control: the wrong 7-adic coupling (γ = 38 instead of 11 at s = +1) fails -/
theorem cert49_11_control : cert49 5 1 12717 32 6 1 38 = false := by decide

#print axioms nsw_mod7_cycle
#print axioms nsw_mod7
#print axioms three_dvd_iff
#print axioms cert49_5p
#print axioms cert49_5m
#print axioms cert49_7p
#print axioms cert49_7m
#print axioms cert49_11p
#print axioms cert49_11m
#print axioms cert49_13p
#print axioms cert49_13m
#print axioms cert49_17p
#print axioms cert49_17m
#print axioms cert49_19p
#print axioms cert49_19m
#print axioms cert49_11_control

end Bgs.LineE
