/-
  RUN 82.26 -- Lean certificate for the SCALE LAW c^2 = t^2 - 4 of op:cscale,
  at the design prime p = 199 (a = 139, K = 11, branch scale c = 123 = L_5).

  What is checked here, entirely by the KERNEL (no native_decide, no axioms):

    S1  a = 139 has order exactly 11 in (Z/199)^*, and a * ainv = 1 where
        ainv = 63 = 3 - a  (the Vieta partner a^{-1} = t - a, t = 3);
    S2  the half-index Lucas trace s = a^5 + a^6 (= a^5 + a^{-5}, since
        a^{-5} = a^{11-5} = a^6 by the order-11 group law) equals 123, and
        s^2 = 5 mod 199 -- the one-line identity s^2 = a^{K-1} + 2 + a^{1-K}
        instantiated: a^{10} = a^{-1}, so s^2 = a^{-1} + 2 + a = t + 2 = 5;
    S3  the two branch scales c = 123 and c' = 76 = -s satisfy
        c^2 = 5, c'^2 = 5, c * c' = -5 = -(t^2-4) mod p.

  The general identity (any prime, any K) is not formalised -- only its
  instantiation at the design prime, matching the numeric certificates of
  R82.24.  All statements are closed by `decide` on small numerals.
-/

namespace Bgs.ScaleLaw

def p : Nat := 199
def a : Nat := 139
def ainv : Nat := 63        -- 3 - a  (t = 3)
def s : Nat := 123          -- a^5 + a^6 mod p  (verified S2 below)
def c : Nat := 123
def c' : Nat := 76

-- S1: the order of a mod p is exactly 11, and ainv = a^{-1}
theorem S1_order : a^11 % p = 1 ∧ a * ainv % p = 1 ∧
    (a^1 % p != 1) ∧ (a^2 % p != 1) ∧ (a^3 % p != 1) ∧ (a^4 % p != 1) ∧
    (a^5 % p != 1) ∧ (a^6 % p != 1) ∧ (a^7 % p != 1) ∧ (a^8 % p != 1) ∧
    (a^9 % p != 1) ∧ (a^10 % p != 1) := by decide

-- S2a: a^{-1} = a^{10} = 63 (the Vieta partner), so a^{-5} = a^{6}
theorem S2a_power : a^10 % p = ainv ∧ a^6 % p = 61 := by decide

-- S2b: the half-index Lucas trace s = a^5 + a^{-5} = a^5 + a^6 = 123,
--      and s^2 = 5 mod p
theorem S2_trace : (a^5 % p + a^6 % p) % p = s ∧ (s * s) % p = 5 := by decide

-- S3: both branch scales square to the discriminant 5 = t^2-4, and their
--     product is -5 mod p
theorem S3_branches : (c * c) % p = 5 ∧ (c' * c') % p = 5 ∧
    (c * c') % p = p - 5 := by decide

#print axioms S1_order
#print axioms S2a_power
#print axioms S2_trace
#print axioms S3_branches

end Bgs.ScaleLaw
