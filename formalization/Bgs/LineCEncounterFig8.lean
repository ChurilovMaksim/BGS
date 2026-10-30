import Bgs.LineCEncounterDefs
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false


namespace Bgs.LineCEncounter

theorem msPerms_count : (msPerms 6 (mergedWord 6 2)).length = 360 := by decide

theorem fig8_6 :
    fig8Words 6 1 = 6 * d 1 * d 5 ∧ fig8Words 6 2 = 6 * d 2 * d 4 ∧
    fig8Words 6 3 = 6 * d 3 * d 3 := by decide

#print axioms msPerms_count
#print axioms fig8_6

end Bgs.LineCEncounter
