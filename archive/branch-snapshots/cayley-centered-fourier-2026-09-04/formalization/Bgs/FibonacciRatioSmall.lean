/-
  Kernel-checked finite residue for the Fibonacci/Lucas ratio almost-Sidon
  theorem in mathematics/cayley_resultant_structure.md.

  The general theorem uses Carmichael's primitive-divisor theorem to reduce
  any non-forced collision to a bounded index range.  This module checks that
  residual range (indices 1..12) exactly.  It is not a formalization of
  Carmichael's theorem itself.
-/

namespace Bgs.FibonacciRatioSmall

structure Value where
  idx : Nat
  num : Int
  den : Nat
deriving DecidableEq, Repr

-- x_n = L_n/F_n for n=1,...,12.  Fractions need not be reduced because all
-- comparisons below are performed by exact cross multiplication.
def positive : List Value := [
  { idx := 1,  num := 1,   den := 1 },
  { idx := 2,  num := 3,   den := 1 },
  { idx := 3,  num := 4,   den := 2 },
  { idx := 4,  num := 7,   den := 3 },
  { idx := 5,  num := 11,  den := 5 },
  { idx := 6,  num := 18,  den := 8 },
  { idx := 7,  num := 29,  den := 13 },
  { idx := 8,  num := 47,  den := 21 },
  { idx := 9,  num := 76,  den := 34 },
  { idx := 10, num := 123, den := 55 },
  { idx := 11, num := 199, den := 89 },
  { idx := 12, num := 322, den := 144 }
]

def negValue (v : Value) : Value := { v with num := -v.num }

def signed : List Value := positive.flatMap fun v => [v, negValue v]

abbrev Pair := Value × Value

def pairs : List Pair :=
  signed.flatMap fun a =>
    signed.filterMap fun b =>
      if a == b then none else some (a, b)


def diffNum (a b : Value) : Int :=
  a.num * Int.ofNat b.den - b.num * Int.ofNat a.den


def diffDen (a b : Value) : Nat := a.den * b.den


def diffEq (a b c d : Value) : Bool :=
  diffNum a b * Int.ofNat (diffDen c d) ==
    diffNum c d * Int.ofNat (diffDen a b)


def collisionCount (p : Pair) : Nat :=
  (pairs.filter fun q => diffEq p.1 p.2 q.1 q.2).length

-- Sum over every ordered pair of the representation count at its difference;
-- this equals sum_d r(d)^2 without constructing rational hash keys.
def energy : Nat :=
  pairs.foldl (fun total p => total + collisionCount p) 0


def allHighCollisionsUseFirstThree : Bool :=
  pairs.all fun p =>
    if collisionCount p > 2 then
      decide (p.1.idx ≤ 3 ∧ p.2.idx ≤ 3)
    else true


def x1 : Value := { idx := 1, num := 1, den := 1 }
def nx1 : Value := negValue x1

def x2 : Value := { idx := 2, num := 3, den := 1 }
def x3 : Value := { idx := 3, num := 4, den := 2 }

-- N=12 gives |S_N|=24 and the exact formula
-- 2N(4N-3)+32 = 1112.
theorem bounded_energy : energy = 1112 := by
  native_decide

-- Every non-forced collision in the bounded residue necessarily touches only
-- x_1,x_2,x_3.  Combined with the primitive-divisor argument, this isolates
-- the complete exceptional relation set in the general proof.
theorem bounded_high_collisions_are_local :
    allHighCollisionsUseFirstThree = true := by
  native_decide

-- Representative high-multiplicity bins: +1, +2, +4.
theorem difference_one_multiplicity : collisionCount (x3, x1) = 4 := by
  native_decide

theorem difference_two_multiplicity : collisionCount (x2, x1) = 3 := by
  native_decide

theorem difference_four_multiplicity : collisionCount (x2, nx1) = 3 := by
  native_decide

#print axioms bounded_energy
#print axioms bounded_high_collisions_are_local
#print axioms difference_one_multiplicity
#print axioms difference_two_multiplicity
#print axioms difference_four_multiplicity

end Bgs.FibonacciRatioSmall
