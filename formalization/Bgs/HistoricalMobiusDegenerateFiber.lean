/-
  Finite diagnostic for the degenerate d=0 fiber in the retracted historical
  Möbius parametrization.

  Historical map:
    v_d(u)=(u(d-1)+1)/(d-u+1) mod p.

  At d=0 numerator and denominator both equal 1-u, so v_0(u)=1 for every
  u != 1. This is the explicit exceptional fiber that invalidates the old
  claimed uniform square-root bound for the corresponding character pair.

  CI builds this module. The statements below are finite certificates at
  p=53 and p=199; the file is a falsifier/regression guard, not support for
  the retracted proof route.
-/

namespace Bgs.HistoricalMobiusDegenerateFiber

def powmod (b e m : Nat) : Nat := (Nat.pow b e) % m

def invModPrime (x p : Nat) : Nat := powmod x (p - 2) p

def mobiusV0 (p u : Nat) : Nat :=
  let z := (1 + p - (u % p)) % p
  (z * invModPrime z p) % p

def d0Values53 : List Nat :=
  ((List.range 51).map fun i => i + 2).map fun u => mobiusV0 53 u

def d0Values199 : List Nat :=
  ((List.range 197).map fun i => i + 2).map fun u => mobiusV0 199 u

theorem d0_constant_53 :
    d0Values53.all (fun v => v == 1) = true := by
  native_decide

theorem d0_cardinality_53 : d0Values53.length = 51 := by
  native_decide

theorem d0_constant_199 :
    d0Values199.all (fun v => v == 1) = true := by
  native_decide

theorem d0_cardinality_199 : d0Values199.length = 197 := by
  native_decide

#print axioms d0_constant_53
#print axioms d0_cardinality_53
#print axioms d0_constant_199
#print axioms d0_cardinality_199

end Bgs.HistoricalMobiusDegenerateFiber
