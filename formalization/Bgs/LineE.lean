import Mathlib

/-!
# Line E: finite and algebraic facts behind the resonant-residue identity (Theorem E1)

* `pell`      : x_d^2 - 8 y_d^2 = 1 for all d   (S^d = [[x_d,4y_d],[2y_d,x_d]])
* `xy_mod`    : x_d ≡ (-1)^d (mod 4) and y_d ≡ d (mod 2) for all d  (the two parity facts used in the proof)
* `cert m`    : for each odd m in 5..21, with h = h_m, D = 4h^2, g' = 2h, y_m = h y', nu* = odd lift of -4⁻¹ mod h,
                k = (-4 nu* - 1)/h, kappa = k y' mod 8:
                (i) the Lemma-S data D = 2(x_m - 1) = 4h^2, h ∣ y_m;
                (ii) the diagonal identity  -nu* y'/g' ≡ G(0)/2 + kappa/8  (mod 1)  (cleared: mod 8h^2);
                (iii) the pair identities   -2 nu* y' x_d/g' ≡ G(d) + kappa/4 (mod 1), 1 ≤ d < m (cleared: mod 4h^2),
                with G(d) = phi(d)/D, phi(d) = y_m x_d - (x_m-1) y_d, phi(0) = y_m (Lemma Q of TRACE-163).
All finite checks are by `decide` (kernel evaluation); no `native_decide`.
-/

namespace Bgs.LineE

def xy : ℕ → ℤ × ℤ
  | 0 => (1, 0)
  | d + 1 => (3 * (xy d).1 + 8 * (xy d).2, (xy d).1 + 3 * (xy d).2)

theorem pell (d : ℕ) : (xy d).1 ^ 2 - 8 * (xy d).2 ^ 2 = 1 := by
  induction d with
  | zero => simp [xy]
  | succ d ih =>
    simp only [xy]
    have h : (3 * (xy d).1 + 8 * (xy d).2) ^ 2 - 8 * ((xy d).1 + 3 * (xy d).2) ^ 2
        = (xy d).1 ^ 2 - 8 * (xy d).2 ^ 2 := by ring
    rw [h, ih]

theorem xy_mod (d : ℕ) :
    ((xy d).1 % 4 = if d % 2 = 0 then 1 else 3) ∧ (xy d).2 % 2 = (d % 2 : ℕ) := by
  induction d with
  | zero => simp [xy]
  | succ d ih =>
    obtain ⟨h1, h2⟩ := ih
    simp only [xy]
    rcases Nat.mod_two_eq_zero_or_one d with hd | hd
    · have hd' : (d + 1) % 2 = 1 := by omega
      rw [hd] at h1 h2; rw [hd']; simp at h1 ⊢
      constructor <;> omega
    · have hd' : (d + 1) % 2 = 0 := by omega
      rw [hd] at h1 h2; rw [hd']; simp at h1 ⊢
      constructor <;> omega

/-- NSW numbers h_m for odd m = 2j+1 : 1, 7, 41, 239, ... -/
def nsw : ℕ → ℤ
  | 0 => 1
  | 1 => 7
  | j + 2 => 6 * nsw (j + 1) - nsw j

/-- the finite certificate for m = 2j+1 with explicit nu* -/
def cert (j : ℕ) (nu : ℤ) : Bool :=
  let m := 2 * j + 1
  let h := nsw j
  let xm := (xy m).1
  let ym := (xy m).2
  let D := 2 * (xm - 1)
  let yp := ym / h
  let k := (-4 * nu - 1) / h
  let kap := (k * yp) % 8
  let phi : ℕ → ℤ := fun d => if d = 0 then ym else ym * (xy d).1 - (xm - 1) * (xy d).2
  decide (D = 4 * h ^ 2) && decide (ym % h = 0) && decide (nu % 2 = 1) &&
  decide ((4 * nu + 1) % h = 0) &&
  decide ((-4 * h * nu * yp - phi 0 - kap * h ^ 2) % (8 * h ^ 2) = 0) &&
  (List.range m).all (fun d => d = 0 ||
     decide ((-2 * nu * yp * (xy d).1 * (2 * h) - phi d - kap * h ^ 2) % (4 * h ^ 2) = 0))

theorem cert5  : cert 2 51 = true := by decide
theorem cert7  : cert 3 179 = true := by decide
theorem cert9  : cert 4 1741 = true := by decide
theorem cert11 : cert 5 6089 = true := by decide
theorem cert13 : cert 6 59151 = true := by decide
theorem cert15 : cert 7 206855 = true := by decide
theorem cert17 : cert 8 2009401 = true := by decide
theorem cert19 : cert 9 7026989 = true := by decide
theorem cert21 : cert 10 68260491 = true := by decide

/-- negative control: a wrong residue (nu* + 2) must fail -/
theorem cert11_control : cert 5 6091 = false := by decide

end Bgs.LineE
