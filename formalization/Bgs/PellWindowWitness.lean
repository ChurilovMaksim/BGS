import Std

namespace Bgs.PellWindowWitness
set_option maxRecDepth 4096

private def pellPair (k : Nat) : Nat × Nat :=
  Nat.rec (1, 0) (fun _ (x,y) => (x+2*y, x+y)) k

def h (k : Nat) : Nat := (pellPair k).1

theorem arc_197 :
    700*(2000*197*(15*10^80) + 8*197*(h 197)^2) < 15*10^80*h 197 := by decide

theorem arc_203 :
    25*(2000*203*(15*10^80) + 8*203*(h 203)^2) < 7*15*10^80*h 203 := by decide

theorem trace_207 :
    50*(h 207)^2*(207*1650797 + 63600000) < 19*8*10^166 := by decide

theorem normalization_207 :
    16*207 < 12*17^2 ∧
      100*(h 207 - 4*207)^2 > 99*(h 207)^2 := by decide

theorem final_gap_207 :
    1000*(99*31^2*h 207 - 9*10000*h 207 - 500000) >
      4000000*h 207 := by decide

theorem pell_five : h 5 = 41 := by decide

theorem pell_five_squarefree (d : Nat) (hd : 2 ≤ d) : ¬d*d ∣ h 5 := by
  rw [pell_five]
  by_cases hd' : d ≤ 6
  · have : d = 2 ∨ d = 3 ∨ d = 4 ∨ d = 5 ∨ d = 6 := by omega
    rcases this with rfl | rfl | rfl | rfl | rfl <;> decide
  · have hx : 7 ≤ d := by omega
    have hy : 49 ≤ d*d := Nat.mul_le_mul hx hx
    intro H
    have hz := Nat.le_of_dvd (by decide : 0 < 41) H
    omega

#print axioms arc_197
#print axioms arc_203
#print axioms trace_207
#print axioms normalization_207
#print axioms final_gap_207
#print axioms pell_five_squarefree
end Bgs.PellWindowWitness
