import Mathlib
/-! Phase 4 finite certificates (decide / norm_num only; no native_decide). -/
namespace Bgs.LineB.Phase4
/-- ‖u‖₂² = (1/2)Σβ_k² with 800β = (16,8,4,8,-8,-4):  equals 240/640000 = 3.75e-4. -/
theorem U2_value :
    ((16:ℚ)^2 + 8^2 + 4^2 + 8^2 + (-8)^2 + (-4)^2) / 2 / 800^2 = 240 / 640000 := by norm_num

theorem sigma2_decimal : (240:ℚ) / 640000 = 375 / 1000000 := by norm_num

/-- γ0 = 1 - 1/λ = 2√2 - 2 ≥ 0.8284 reduces to 1.4142² ≤ 2. -/
theorem G0_SAFE_ok : ((14142:ℚ)/10000)^2 ≤ 2 := by norm_num
/-- c = 1/(2√2) ≤ 0.35356 reduces to 2·0.70712² ≥ 1. -/
theorem CC_SAFE_ok : 2 * ((70712:ℚ)/100000)^2 ≥ 1 := by norm_num

/-- U_{-1}=0, U_0=1, U_k = 6U_{k-1} - U_{k-2} (mod h). -/
def Umod (h : ℕ) : ℕ → ℕ
  | 0 => 1
  | 1 => 6 % h
  | (k+2) => (6 * Umod h (k+1) + (h - Umod h k % h)) % h

/-- Lemma V core, m = 5 (h = 41 prime): U_{d-1} ≢ 0 mod 41 for 1 ≤ d ≤ 4. -/
theorem m5_prime : Nat.Prime 41 := by norm_num
theorem m5_U : ∀ k : Fin 4, Umod 41 k.val ≠ 0 := by decide
/-- m = 7 (h = 239 prime): U_{d-1} ≢ 0 mod 239 for 1 ≤ d ≤ 6. -/
theorem m7_prime : Nat.Prime 239 := by norm_num
theorem m7_U : ∀ k : Fin 6, Umod 239 k.val ≠ 0 := by decide

/-- The circulant H_m on Z^m, (H k)_j = 6 k_j − k_{j−1} − k_{j+1} (indices mod m), here m = 3. -/
def H3 (k : Fin 3 → ℤ) : Fin 3 → ℤ := fun j => 6 * k j - k (j - 1) - k (j + 1)

/-- m = 3 obstruction to Lemma V: the explicit dual-lattice relation
 7e₀ = H₃(1,0,0) + 𝟙 = (6,−1,−1) + (1,1,1), so 7e₀ ∈ HZ³ + Z𝟙 with |supp| = 1, ‖·‖∞ = 7 ≤ 18. -/
theorem m3_relation : (fun j => H3 ![1, 0, 0] j + 1) = ![7, 0, 0] := by decide

/-- Norm inequality for m = 9 (the start of the general analytic range):
 324·(2 + T_4) < h_9² with T_4 = λ⁴ + λ⁻⁴ = 1154, h_9 = 1393. -/
theorem m9_norm : 324 * (2 + 1154) < 1393^2 := by norm_num
/-- T_k = λ^k + λ^{-k} recurrence values T_0..T_4 = 2, 6, 34, 198, 1154. -/
def T : ℕ → ℤ
  | 0 => 2
  | 1 => 6
  | (k+2) => 6 * T (k+1) - T k
theorem T4 : T 4 = 1154 := by decide
/-- h_m² = (T_m - 2)/4, checked for m = 9: T_9 = 7761798. -/
theorem h9_sq : (T 9 - 2) = 4 * 1393^2 := by decide

#print axioms U2_value
#print axioms sigma2_decimal
#print axioms G0_SAFE_ok
#print axioms CC_SAFE_ok
#print axioms m5_prime
#print axioms m5_U
#print axioms m7_prime
#print axioms m7_U
#print axioms m3_relation
#print axioms m9_norm
#print axioms T4
#print axioms h9_sq
end Bgs.LineB.Phase4