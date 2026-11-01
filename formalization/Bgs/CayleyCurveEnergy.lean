import Bgs.CayleyEnergy

/-
  Finite kernel-checked certificate for the ratio-curve decomposition used in
  mathematics/cayley-arithmetic/cayley_energy_curve_bound.md.

  Scope: the explicit exceptional design (p,K,a)=(53,13,10).  The general
  K^(8/3) theorem still depends on the external Makarychev--Vyugin subgroup-
  curve estimate and is NOT formalized here.
-/

namespace Bgs.CayleyCurveEnergy

open Bgs.CayleyEnergy


def N : Nat := 53
def K : Nat := 13
def a : Nat := 10

def H : List Nat := subgroup N K a

def parameters : List Nat := H.filter fun r => r != 1

def hpairs : List (Nat × Nat) :=
  H.flatMap fun x => H.map fun y => (x, y)

def parameterPairs : List (Nat × Nat) :=
  parameters.flatMap fun r => parameters.map fun s => (r, s)


def addMod (x y : Nat) : Nat := (x + y) % N

def subMod (x y : Nat) : Nat := (x + N - (y % N)) % N

def mulMod (x y : Nat) : Nat := (x * y) % N

def inv (x : Nat) : Nat := invModPrime N x

/--
  d_rho(x)=(rho*x+x^{-1}-(rho+1))/(1-rho).
-/
def ratioValue (rho x : Nat) : Nat :=
  mulMod
    (subMod (addMod (mulMod rho x) (inv x)) (addMod rho 1))
    (inv (subMod 1 rho))

/--
  G_{rho,sigma}(U,V) after the toric change (x,y)=(U/V,UV).
-/
def curveValue (rho sigma U V : Nat) : Nat :=
  let U2 := mulMod U U
  let V2 := mulMod V V
  let UV := mulMod U V
  let t1 := mulMod (mulMod sigma (subMod rho 1)) (mulMod U2 V2)
  let t2 := mulMod (mulMod rho (subMod 1 sigma)) U2
  let t3 := mulMod (mulMod 2 (subMod sigma rho)) UV
  let t4 := mulMod (subMod 1 sigma) V2
  let t5 := subMod rho 1
  addMod (addMod (addMod (addMod t1 t2) t3) t4) t5


def ratioCount (rho sigma : Nat) : Nat :=
  (hpairs.filter fun xy =>
    ratioValue rho xy.1 == ratioValue sigma xy.2).length


def curveCount (rho sigma : Nat) : Nat :=
  (hpairs.filter fun uv => curveValue rho sigma uv.1 uv.2 == 0).length


def allCurveCountsMatch : Bool :=
  parameterPairs.all fun rs =>
    ratioCount rs.1 rs.2 == curveCount rs.1 rs.2


def allDiagonalCounts : Bool :=
  parameters.all fun rho => ratioCount rho rho == 2 * K - 1


def enlargedTotal : Nat :=
  parameterPairs.foldl
    (fun total rs => total + ratioCount rs.1 rs.2)
    0


def offDiagonalCounts : List Nat :=
  parameterPairs.filterMap fun rs =>
    if rs.1 != rs.2 then some (ratioCount rs.1 rs.2) else none


def maxOffDiagonal : Nat := offDiagonalCounts.foldl Nat.max 0


theorem generator_exact_order :
    generatorExactOrder N K a = true := by
  decide +kernel

/-- The rational ratio-fibre and transformed polynomial curve counts agree. -/
theorem toric_curve_counts_match : allCurveCountsMatch = true := by
  decide +kernel

/-- Every parameter-diagonal enlarged fibre has exactly 2K-1 points. -/
theorem diagonal_curve_counts : allDiagonalCounts = true := by
  decide +kernel

/-- Exact enlarged energy surrogate at the exceptional K=13 design. -/
theorem enlarged_curve_total : enlargedTotal = 1036 := by
  decide +kernel

/-- Largest off-diagonal parameter-fibre count in the design. -/
theorem max_offdiagonal_curve_count : maxOffDiagonal = 12 := by
  decide +kernel

#print axioms toric_curve_counts_match
#print axioms diagonal_curve_counts
#print axioms enlarged_curve_total
#print axioms max_offdiagonal_curve_count

#print axioms generator_exact_order
end Bgs.CayleyCurveEnergy
