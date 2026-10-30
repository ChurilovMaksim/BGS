import Bgs.LineCEncounterDefs
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false

namespace Bgs.LineCEncounter

/-! Part lemmas for p = 13 (c = 10). -/

/-! Step 3.1: cv13_0 split by k.

The whole-list `decide` for cv13_0 peaked at ~5.9 GB and killed the module
build (Lean exit 137) on a 7.7 GB VM. Each component lemma below is a single
`getD` component of the same `countVec` value, proven by the same kernel
`decide`; the values are exactly the components computed by `#eval` of
`countVec 13 10 3 [0, 1, 2]` (13182 at k = 0, 0 elsewhere). `cv13_0` is then
reassembled from the 13 component lemmas by list extensionality
(`List.ext_getElem` + `omega` case split on the index); no definition
(`countVec`, `parts3`, `aggregate`) is changed, and every component is still
proven by kernel `decide`. -/

theorem cv13_0_k0 : (countVec 13 10 3 [0, 1, 2]).getD 0 0 = 13182 := by decide
theorem cv13_0_k1 : (countVec 13 10 3 [0, 1, 2]).getD 1 0 = 0 := by decide
theorem cv13_0_k2 : (countVec 13 10 3 [0, 1, 2]).getD 2 0 = 0 := by decide
theorem cv13_0_k3 : (countVec 13 10 3 [0, 1, 2]).getD 3 0 = 0 := by decide
theorem cv13_0_k4 : (countVec 13 10 3 [0, 1, 2]).getD 4 0 = 0 := by decide
theorem cv13_0_k5 : (countVec 13 10 3 [0, 1, 2]).getD 5 0 = 0 := by decide
theorem cv13_0_k6 : (countVec 13 10 3 [0, 1, 2]).getD 6 0 = 0 := by decide
theorem cv13_0_k7 : (countVec 13 10 3 [0, 1, 2]).getD 7 0 = 0 := by decide
theorem cv13_0_k8 : (countVec 13 10 3 [0, 1, 2]).getD 8 0 = 0 := by decide
theorem cv13_0_k9 : (countVec 13 10 3 [0, 1, 2]).getD 9 0 = 0 := by decide
theorem cv13_0_k10 : (countVec 13 10 3 [0, 1, 2]).getD 10 0 = 0 := by decide
theorem cv13_0_k11 : (countVec 13 10 3 [0, 1, 2]).getD 11 0 = 0 := by decide
theorem cv13_0_k12 : (countVec 13 10 3 [0, 1, 2]).getD 12 0 = 0 := by decide

theorem cv13_0 : countVec 13 10 3 [0, 1, 2] = [13182, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by
  have hlen : (countVec 13 10 3 [0, 1, 2]).length = 13 := by decide
  apply List.ext_getElem
  · rw [hlen]; rfl
  · intro i hi1 hi2
    rw [hlen] at hi1
    have hc : i = 0 ∨ i = 1 ∨ i = 2 ∨ i = 3 ∨ i = 4 ∨ i = 5 ∨ i = 6 ∨ i = 7 ∨ i = 8 ∨ i = 9 ∨ i = 10 ∨ i = 11 ∨ i = 12 := by omega
    rcases hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k0
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k1
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k2
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k3
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k4
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k5
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k6
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k7
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k8
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k9
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k10
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k11
    · rw [List.getElem_eq_getD (fallback := 0), List.getElem_eq_getD (fallback := 0)]
      exact cv13_0_k12

theorem cv13_1 : countVec 13 10 2 [0, 0, 1] = [1014, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide
theorem cv13_2 : countVec 13 10 2 [0, 1, 0] = [1014, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide
theorem cv13_3 : countVec 13 10 2 [0, 1, 1] = [1014, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide
theorem cv13_4 : countVec 13 10 1 [0, 0, 0] = [78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by decide

theorem agg13 : aggregate 13 10 parts3 = [70278, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] := by
  simp [aggregate, parts3, cv13_0, cv13_1, cv13_2, cv13_3, cv13_4]
  decide

theorem exact_13_3 :
    constOff (aggregate 13 10 parts3) = true ∧ certVal (aggregate 13 10 parts3) = 901 * 6 * 13 := by
  rw [agg13]
  decide

#print axioms cv13_0_k0
#print axioms cv13_0_k1
#print axioms cv13_0_k2
#print axioms cv13_0_k3
#print axioms cv13_0_k4
#print axioms cv13_0_k5
#print axioms cv13_0_k6
#print axioms cv13_0_k7
#print axioms cv13_0_k8
#print axioms cv13_0_k9
#print axioms cv13_0_k10
#print axioms cv13_0_k11
#print axioms cv13_0_k12
#print axioms cv13_0
#print axioms cv13_1
#print axioms cv13_2
#print axioms cv13_3
#print axioms cv13_4
#print axioms agg13
#print axioms exact_13_3

end Bgs.LineCEncounter
