import Bgs.LineCEncounterDefs
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false


namespace Bgs.LineCEncounter

theorem coeff_identity :
    (List.range 296).all (fun j => c1formula ((j : Int) + 5) == -2 * ((j : Int) + 5) ^ 2) = true := by
  decide

theorem hyp_counts : (hypOK 5 && hypOK 7 && hypOK 11 && hypOK 13) = true := by decide

#print axioms coeff_identity
#print axioms hyp_counts

end Bgs.LineCEncounter
