import Std

/- Algebraic kernel only: this file is not a formalization of the geometric
   support theorem. Compiler execution must be recorded separately. -/
namespace TemporalCancellation

def deltaSum (a : Nat -> Int) : Nat -> Int
  | 0 => 0
  | n + 1 => deltaSum a n + (a (n + 1) - a n)

theorem deltaSum_eq (a : Nat -> Int) (n : Nat) :
    deltaSum a n = a n - a 0 := by
  induction n with
  | zero => simp [deltaSum]
  | succ n ih =>
    rw [deltaSum, ih]
    omega

def coeff : List Int -> Nat -> Int
  | [], _ => 0
  | a :: _, 0 => a
  | _ :: xs, n + 1 => coeff xs n

def correlation (p : List Int) (r : Nat) : Int :=
  ((List.range p.length).map (fun i => coeff p i * coeff p (i + r))).sum

def residue (p q : List Int) (r : Nat) : Int :=
  ((List.range (max p.length q.length)).map
    (fun i => coeff p i * coeff q (i + r) - coeff q i * coeff p (i + r))).sum

example : (List.range 4).map (correlation [1, 5, 6]) = [62, 35, 6, 0] := by decide
example : (List.range 4).map (correlation [2, 7, 3]) = [62, 35, 6, 0] := by decide
example : [residue [0, 1] [1, 0, 1] 1,
           residue [0, 1] [1, 0, 1] 2] = [0, 0] := by decide
example : [residue [1, 5, 6] [0, 1, 5, 6] 1,
           residue [1, 5, 6] [0, 1, 5, 6] 2,
           residue [1, 5, 6] [0, 1, 5, 6] 3] = [56, 35, 6] := by decide

end TemporalCancellation
