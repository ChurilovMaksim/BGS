import Bgs.LineCEncounterDefs
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false


namespace Bgs.LineCEncounter

theorem aut5 : autCount 5 = 10 := by decide
theorem aut6 : autCount 6 = 12 := by decide
theorem ham6 : (hamCycles 6).length = 60 := by decide

#print axioms aut5
#print axioms aut6
#print axioms ham6

end Bgs.LineCEncounter
