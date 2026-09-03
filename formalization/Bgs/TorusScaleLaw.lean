/-
  Finite branch-scale certificate at p=199, a=139, K=11.

  The module checks the recorded design identities only. It is not a symbolic
  proof of a scale law for arbitrary primes or subgroup orders. All statements
  are closed by kernel decide on concrete numerals.
-/

namespace Bgs.TorusScaleLaw

def p : Nat := 199
def a : Nat := 139
def ainv : Nat := 63
def halfTrace : Nat := 123
def c : Nat := 123
def c' : Nat := 76

theorem generator_exact_order_and_inverse :
    a^11 % p = 1 ∧ a * ainv % p = 1 ∧
    (a^1 % p != 1) ∧ (a^2 % p != 1) ∧ (a^3 % p != 1) ∧
    (a^4 % p != 1) ∧ (a^5 % p != 1) ∧ (a^6 % p != 1) ∧
    (a^7 % p != 1) ∧ (a^8 % p != 1) ∧ (a^9 % p != 1) ∧
    (a^10 % p != 1) := by
  decide

theorem inverse_and_half_power : a^10 % p = ainv ∧ a^6 % p = 61 := by
  decide

theorem half_trace_and_discriminant :
    (a^5 % p + a^6 % p) % p = halfTrace ∧
    (halfTrace * halfTrace) % p = 5 := by
  decide

theorem branch_scales :
    (c * c) % p = 5 ∧ (c' * c') % p = 5 ∧ (c * c') % p = p - 5 := by
  decide

#print axioms generator_exact_order_and_inverse
#print axioms inverse_and_half_power
#print axioms half_trace_and_discriminant
#print axioms branch_scales

end Bgs.TorusScaleLaw
