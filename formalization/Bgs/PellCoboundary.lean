import Std
/- Universal integer structural identity and finite K=11 certificates.
   This does not formalize Duhamel estimates or the limiting spectral law. -/
namespace Bgs.PellCoboundary

def step (v : Prod Int Int) : Prod Int Int :=
  (3*v.1+2*v.2, 4*v.1+3*v.2)

def rootTwo (v : Prod Int Int) : Prod Int Int := (v.2,2*v.1)

def sub (v w : Prod Int Int) : Prod Int Int := (v.1-w.1,v.2-w.2)
def add (v w : Prod Int Int) : Prod Int Int := (v.1+w.1,v.2+w.2)

theorem structuralIdentity (a b : Int) :
    step (sub (rootTwo (a,b)) (a,b)) = add (rootTwo (a,b)) (a,b) := by
  apply Prod.ext <;> simp [step,sub,add,rootTwo] <;> omega

def advance (v : Prod Int Int) : Prod Int Int :=
  let w := step v
  (w.1 % 8119,w.2 % 8119)

def vector (species j : Nat) : Prod Int Int :=
  (List.range j).foldl (fun v _ => advance v)
    (if species == 0 then (2,4) else (4,4))

def pairKeys : List (Prod Int Int) :=
  (List.range 11).flatMap fun t =>
    ((List.range 11).filter (fun s => t < s)).flatMap fun s =>
      (List.range 2).flatMap fun a =>
        (List.range 2).flatMap fun b =>
          ([-1,1] : List Int).flatMap fun e =>
            ([-1,1] : List Int).map fun f =>
              ((e*(vector a t).1+f*(vector b s).1)%8119,
               (e*(vector a t).2+f*(vector b s).2)%8119)

def multiplicity (v : Prod Int Int) : Nat :=
  (pairKeys.filter (fun w => w == v)).length

set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem firstSpeciesPeriod : vector 0 11 = (2,4) := by native_decide
theorem secondSpeciesPeriod : vector 1 11 = (4,4) := by native_decide
theorem pairCount : pairKeys.length = 880 := by native_decide
theorem distinctCount : pairKeys.eraseDups.length = 836 := by native_decide
theorem noZero : pairKeys.contains (0,0) = false := by native_decide
theorem multiplicityAtMostTwo :
    pairKeys.all (fun v => decide (multiplicity v <= 2)) = true := by native_decide
theorem doubleKeyCount :
    (pairKeys.eraseDups.filter (fun v => multiplicity v == 2)).length = 44 := by
  native_decide

end Bgs.PellCoboundary
