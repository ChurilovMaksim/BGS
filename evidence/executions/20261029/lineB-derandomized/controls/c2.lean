import Bgs.LineBPhase4
open Bgs.LineB.Phase4 in
theorem bad : ∀ k : Fin 5, Umod 41 k.val ≠ 0 := by decide
