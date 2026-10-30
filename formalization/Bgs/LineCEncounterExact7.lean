import Bgs.LineCEncounterDefs
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false

namespace Bgs.LineCEncounter

/-! Part lemmas for p = 7 (c = 2). Values obtained by evaluating `countVec`
(outside the repository, test run) and kernel-checked here by `decide`. -/

theorem cv7_0 : countVec 7 2 3 [0, 1, 2] = [2058, 0, 0, 0, 0, 0, 0] := by decide
theorem cv7_1 : countVec 7 2 2 [0, 0, 1] = [294, 0, 0, 0, 0, 0, 0] := by decide
theorem cv7_2 : countVec 7 2 2 [0, 1, 0] = [294, 0, 0, 0, 0, 0, 0] := by decide
theorem cv7_3 : countVec 7 2 2 [0, 1, 1] = [294, 0, 0, 0, 0, 0, 0] := by decide
theorem cv7_4 : countVec 7 2 1 [0, 0, 0] = [42, 0, 0, 0, 0, 0, 0] := by decide

theorem agg7 : aggregate 7 2 parts3 = [9870, 0, 0, 0, 0, 0, 0] := by
  simp [aggregate, parts3, cv7_0, cv7_1, cv7_2, cv7_3, cv7_4]
  decide

theorem exact_7_3 :
    constOff (aggregate 7 2 parts3) = true ∧ certVal (aggregate 7 2 parts3) = 235 * 6 * 7 := by
  rw [agg7]
  decide

#print axioms cv7_0
#print axioms cv7_1
#print axioms cv7_2
#print axioms cv7_3
#print axioms cv7_4
#print axioms agg7
#print axioms exact_7_3

end Bgs.LineCEncounter
