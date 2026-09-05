import Std

/-!
Integer kernels used by the finite Fourier coboundary construction.
This file does not formalize the operator estimates or the smooth limit.
-/
namespace Bgs.PellFourierKernel

def differences (prev : Int) : List Int -> List Int
  | [] => []
  | x :: xs => (x - prev) :: differences x xs

def endpoint (prev : Int) : List Int -> Int
  | [] => prev
  | x :: xs => endpoint x xs

def partialSums (prev : Int) : List Int -> List Int
  | [] => []
  | x :: xs => (prev + x) :: partialSums (prev + x) xs

theorem telescope (prev : Int) (xs : List Int) :
    (differences prev xs).sum = endpoint prev xs - prev := by
  induction xs generalizing prev with
  | nil => simp [differences, endpoint]
  | cons x xs ih =>
      simp only [differences, List.sum_cons, endpoint, ih]
      omega

theorem zeroEndpoint (prev : Int) (xs : List Int)
    (h : endpoint prev xs = prev) : (differences prev xs).sum = 0 := by
  rw [telescope, h]
  omega

theorem reconstruct (prev : Int) (xs : List Int) :
    differences prev (partialSums prev xs) = xs := by
  induction xs generalizing prev with
  | nil => rfl
  | cons x xs ih =>
      simp only [partialSums, differences, ih]
      congr 1
      omega

theorem periodTwoCoordinates (a b : Int) :
    (3*a+2*b) % 2 = a % 2 /\ (4*a+3*b) % 2 = b % 2 := by
  omega

#print axioms telescope
#print axioms zeroEndpoint
#print axioms reconstruct
#print axioms periodTwoCoordinates

end Bgs.PellFourierKernel
