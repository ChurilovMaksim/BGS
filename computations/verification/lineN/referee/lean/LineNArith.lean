import Mathlib
/-! Cheap Line N arithmetic checks (referee). -/
def S : Matrix (Fin 2) (Fin 2) ℤ := !![3,4;2,3]
-- |det(S^p - 1)| = 4 h_p^2 for p = 3,5,7 (h_3=7,h_5=41,h_7=239): Fix(T^p) count
theorem fix3 : ((S^3 - 1).det).natAbs = 4*7^2 := by decide +kernel
theorem fix5 : ((S^5 - 1).det).natAbs = 4*41^2 := by decide +kernel
theorem fix7 : ((S^7 - 1).det).natAbs = 4*239^2 := by decide +kernel
-- index of conductor-h_p points = N(4√2)/[O^∨:O] = 32/8 = 4
theorem idx : (32:ℕ) / 8 = 4 := by norm_num
-- 4*3^(4/3) < 17.31 : (17.31/4)^3 > 3^4
theorem c17 : (3:ℚ)^4 < (1731/400)^3 := by norm_num
-- J2 = 2τ²-τ equality at tested levels
theorem j2a : 2*15^2-15 = 435 ∧ 2*183^2-183 = 66795 ∧ 2*141^2-141 = 39621 := by norm_num
