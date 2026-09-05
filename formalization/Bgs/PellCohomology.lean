import Std
/- General cleared-denominator cohomological identities, followed by a
   finite original-coordinate pair-key certificate. These statements do
   not formalize operator norms or the asymptotic Floquet law. -/
namespace Bgs.PellCohomology

def weight (k j : Int) : Int := k - 1 - 2*j

theorem interior_difference (k j : Int) :
    weight k j - weight k (j-1) = -2 := by
  unfold weight
  omega

theorem boundary_difference (k : Int) :
    weight k 0 - weight k (k-1) = 2*(k-1) := by
  unfold weight
  omega

theorem centered_pair (k j : Int) :
    weight k j + weight k (k-1-j) = 0 := by
  unfold weight
  omega

def pell : Nat -> (Prod Int Int)
  | 0 => (1,0)
  | k+1 => let p := pell k; (p.1+2*p.2,p.1+p.2)

def advance (n : Int) (v : (Prod Int Int)) : (Prod Int Int) :=
  ((3*v.1+2*v.2)%n,(4*v.1+3*v.2)%n)

def vector (j : Nat) : (Prod Int Int) :=
  (List.range j).foldl (fun v _ => advance 8119 v) (1,0)

def pairKeys : List ((Prod Int Int)) :=
  (List.range 11).flatMap fun t =>
    ((List.range 11).filter (fun s => t < s)).flatMap fun s =>
      ([-1,1] : List Int).flatMap fun e =>
        ([-1,1] : List Int).map fun d =>
          ((e*(vector t).1+d*(vector s).1)%8119,
           (e*(vector t).2+d*(vector s).2)%8119)

set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem pell11 : pell 11 = (8119,5741) := by native_decide
theorem period11 : vector 11 = (1,0) := by native_decide
theorem pairKeyCount11 : pairKeys.length = 220 := by native_decide
theorem pairKeysUnique11 : pairKeys.Nodup := by native_decide
theorem pairKeysNonzero11 : pairKeys.contains (0,0) = false := by native_decide
end Bgs.PellCohomology
