/-
  M1 repair — finite certificates for the degenerate Möbius fiber d = 0.

  STATUS: SOURCE WRITTEN, BUILD NOT VERIFIED IN THE 2026-09-03 RUNTIME.
  The runtime used for the Python/C++ audit did not contain Lean/Lake.

  Historical Möbius map:

      v_d(u) = (u(d-1)+1)/(d-u+1)  mod N.

  At d=0, numerator and denominator are both 1-u, hence v_0(u)=1
  for every u != 1 in F_N.  This is the exact exceptional fiber behind
  the observed failure of the claimed uniform |A_tau(d)| <= 4*sqrt(N)
  bound for pairs (psi1 = 1, psi2 != 1).

  The finite claims below mirror the native_decide style used elsewhere
  in this repository.  A later Mathlib-backed file should prove the
  general prime-field statement symbolically.
-/

namespace Bgs.M1DegenerateFiber


def powmod (b e m : Nat) : Nat :=
  (Nat.pow b e) % m


def invModPrime (x p : Nat) : Nat :=
  powmod x (p - 2) p

/-- Historical d=0 Möbius map, written after simplifying numerator and denominator. -/
def mobiusV0 (p u : Nat) : Nat :=
  let z := (1 + p - (u % p)) % p
  (z * invModPrime z p) % p

/-- All nonzero u != 1 at N=53 map to v=1 on the d=0 fiber. -/
def d0Values53 : List Nat :=
  ((List.range 51).map fun i => i + 2).map fun u => mobiusV0 53 u

/-- All nonzero u != 1 at N=199 map to v=1 on the d=0 fiber. -/
def d0Values199 : List Nat :=
  ((List.range 197).map fun i => i + 2).map fun u => mobiusV0 199 u

/-- Finite certificate for the design N=53: v_0(u)=1 for every u=2,...,52. -/
theorem d0_constant_53 :
    d0Values53.all (fun v => v == 1) = true := by
  native_decide

/-- Therefore the d=0 fiber has exactly N-2=51 admissible u-values at N=53. -/
theorem d0_card_53 : d0Values53.length = 51 := by
  native_decide

/-- Finite certificate for the design N=199: v_0(u)=1 for every u=2,...,198. -/
theorem d0_constant_199 :
    d0Values199.all (fun v => v == 1) = true := by
  native_decide

/-- Therefore the d=0 fiber has exactly N-2=197 admissible u-values at N=199. -/
theorem d0_card_199 : d0Values199.length = 197 := by
  native_decide

#print axioms d0_constant_53
#print axioms d0_card_53
#print axioms d0_constant_199
#print axioms d0_card_199

end Bgs.M1DegenerateFiber
