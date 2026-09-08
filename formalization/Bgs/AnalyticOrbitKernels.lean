import Std

/-! Algebraic kernels for analytic_coboundary_regularization.md.
This does not formalize Fourier analysis, analytic convergence, or BGS.
All proofs here use ordinary elaboration/kernel reduction, not native_decide.
-/
namespace Bgs.AnalyticOrbitKernels

theorem growthBySteps (f : Nat → Int) (d : Int)
    (step : ∀ n, f n + d ≤ f (n + 1)) (n : Nat) :
    f 0 + (n : Int) * d ≤ f n := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hn := step n
    simp only [Int.natCast_succ, Int.add_mul, Int.one_mul]
    omega

def positiveAction (v : Int × Int) : Int × Int :=
  (2 * v.1 + v.2, v.1 + v.2)

def negativeAction (v : Int × Int) : Int × Int :=
  (-2 * v.1 - v.2, -v.1 - v.2)

/-- Twice the coefficient divided by i of sin(k.x)-sin((Bk).x). -/
def coefficient (v : Int × Int) : Int :=
  if v = (1, 0) then -1 else
  if v = (-1, 0) then 1 else
  if v = (2, 1) then 1 else
  if v = (-2, -1) then -1 else 0

theorem positiveCancellation :
    coefficient (1, 0) + coefficient (positiveAction (1, 0)) = 0 := by
  decide

theorem negativeNoncancellation :
    coefficient (1, 0) + coefficient (negativeAction (1, 0)) = -2 := by
  decide

theorem signedActionsDiffer : positiveAction (1, 0) ≠ negativeAction (1, 0) := by
  decide

#print axioms growthBySteps
#print axioms positiveCancellation
#print axioms negativeNoncancellation
#print axioms signedActionsDiffer

end Bgs.AnalyticOrbitKernels
