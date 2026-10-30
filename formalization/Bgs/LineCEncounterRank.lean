import Bgs.LineCEncounterDefs
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false


namespace Bgs.LineCEncounter

theorem rank2_class6 : classOK 6 = true := by decide

theorem countRank2_6_0 : countRank2 6 0 = 1 := by decide
theorem countRank2_6_2 : countRank2 6 2 = 9 := by decide
theorem countRank2_6_4 : countRank2 6 4 = 3 := by decide

theorem rank2_counts6 :
    countRank2 6 0 = 1 ∧ countRank2 6 2 = 9 ∧ countRank2 6 4 = 3 :=
  ⟨countRank2_6_0, countRank2_6_2, countRank2_6_4⟩

#print axioms rank2_class6
#print axioms countRank2_6_0
#print axioms countRank2_6_2
#print axioms countRank2_6_4
#print axioms rank2_counts6

end Bgs.LineCEncounter
