import Mathlib
/-! Line N2 arithmetic (`mathematics/fixed-map/lineN2N4_inherited_level.md`, `computations/verification/lineN2/REPORT_N2_v3.md`).
Referee file `computations/verification/lineN2/referee/lean/LineN2Arith.lean` (sha256 31a72985…), integrated unchanged inside the namespace
`Bgs.LineN2`, with `#print axioms` for every theorem. No sorry, no native_decide.
Note: `cond_rate` / `cond_lt_T` / `free24` concern the superseded sampled value 1.98242 (N2-F6) and are kept as the referee wrote them;
no registered claim uses them. -/
namespace Bgs.LineN2
def A : Matrix (Fin 2) (Fin 2) ℤ := !![3,4;2,3]
-- A^p - 1 = h_p • B with det B = -4 (p = 3, 5, 7; h = 7, 41, 239)
theorem idx3 : ∃ B : Matrix (Fin 2) (Fin 2) ℤ, A^3 - 1 = (7:ℤ) • B ∧ B.det = -4 :=
  ⟨!![14,20;10,14], by decide +kernel, by decide +kernel⟩
theorem idx5 : ∃ B : Matrix (Fin 2) (Fin 2) ℤ, A^5 - 1 = (41:ℤ) • B ∧ B.det = -4 :=
  ⟨!![82,116;58,82], by decide +kernel, by decide +kernel⟩
-- Green kernel: sum_n lam^{-|n|}/(lam - 1/lam) = (lam+1)/((lam-1)(lam-1/lam)) = 1/4
theorem green_quarter (s : ℝ) (hs : s^2 = 2) (hpos : 0 < s) :
    ((3+2*s) + 1) / (((3+2*s) - 1) * ((3+2*s) - (3-2*s))) = 1/4 := by
  have h1 : ((3+2*s) - 1) * ((3+2*s) - (3-2*s)) = 4*((3+2*s)+1) := by nlinarith
  rw [h1]; have : (3+2*s)+1 ≠ 0 := by nlinarith
  field_simp
-- thresholds: T^3 / r2(4000) > 2.00859 (8V); conditional rate (1.98242 * r2) < T^3
theorem thr8V : (200859:ℚ)/100000 * (10529012/10000000) < (128359/100000)^3 := by norm_num
theorem cond_rate : (198242:ℚ)/100000 * (10529012/10000000) < (127800/100000)^3 := by norm_num
theorem cond_lt_T : (127800:ℚ)/100000 < 128359/100000 := by norm_num
-- free-family k=24 maximum exceeds the 8V threshold (so free certificates need k' > 24)
theorem free24 : (128359/100000:ℚ)^3 / (10529012/10000000) < 201382/100000 := by norm_num
-- slow-orbit nontriviality: mu*^3 < 1.0644^3 * lam, with lam > 5.828
theorem slow : ((19154752:ℚ)/10000000)^3 < (10644/10000)^3 * 5828/1000 := by norm_num

#print axioms idx3
#print axioms idx5
#print axioms green_quarter
#print axioms thr8V
#print axioms cond_rate
#print axioms cond_lt_T
#print axioms free24
#print axioms slow

end Bgs.LineN2
