import Bgs.LineCEncounterDefs
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false

namespace Bgs.LineCEncounter

/-! Part lemmas for p = 11 (c = 3). -/

theorem cv11_0 : countVec 11 3 3 [0, 1, 2] = [7986, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide
theorem cv11_1 : countVec 11 3 2 [0, 0, 1] = [726, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide
theorem cv11_2 : countVec 11 3 2 [0, 1, 0] = [726, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide
theorem cv11_3 : countVec 11 3 2 [0, 1, 1] = [726, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide
theorem cv11_4 : countVec 11 3 1 [0, 0, 0] = [66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide

theorem agg11 : aggregate 11 3 parts3 = [41646, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by
  simp [aggregate, parts3, cv11_0, cv11_1, cv11_2, cv11_3, cv11_4]
  decide

theorem exact_11_3 :
    constOff (aggregate 11 3 parts3) = true ∧ certVal (aggregate 11 3 parts3) = 631 * 6 * 11 := by
  rw [agg11]
  decide

#print axioms cv11_0
#print axioms cv11_1
#print axioms cv11_2
#print axioms cv11_3
#print axioms cv11_4
#print axioms agg11
#print axioms exact_11_3

end Bgs.LineCEncounter
