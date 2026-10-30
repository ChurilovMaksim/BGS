import Bgs.LineEResonance
open Bgs.LineE
#print axioms nsw_mod7_cycle
#print axioms nsw_mod7
#print axioms three_dvd_iff
#print axioms cert49_5p
#print axioms cert49_11p
#print axioms cert49_11m
#print axioms cert49_13p
#print axioms cert49_13m
#print axioms cert49_17p
#print axioms cert49_19m
#print axioms cert49_11_control
#print axioms pell
#print axioms xy_mod
#print axioms cert21
-- statement shape
#check @nsw_mod7
-- independent controls (should evaluate false)
#eval cert49 5 1 12717 32 6 1 11      -- true
#eval cert49 5 1 12717 32 6 3 11      -- wrong kappa
#eval cert49 5 1 12717 32 6 1 12      -- wrong gamma
#eval cert49 5 1 12719 32 6 1 11      -- wrong nu
#eval cert49 5 (-1) 12717 32 6 1 11   -- wrong sign s
#eval cert49 4 1 12717 32 6 1 11      -- m=9 (3 | m)
#eval (List.range 12).map (fun j => nsw j % 7)
