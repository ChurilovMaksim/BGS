import Std

/- The arithmetic positivity kernel used in TRACE-082's observability budget.
   This source does not formalize complex matrices, codimension, the
   Hilbert--Schmidt norm plateau, TRACE-081's discriminant or any BGS limit.
   Compilation status belongs to the actual execution receipt, not this file. -/
namespace Bgs.CoherenceBudget

def budget (n r : Nat) : Nat := (n - 1) * (n - r)

theorem budget_positive (n r : Nat) (hn : 2 ≤ n) (hr : r < n) :
    0 < budget n r := by
  unfold budget
  exact Nat.mul_pos (by omega) (by omega)

#print axioms budget_positive
end Bgs.CoherenceBudget
