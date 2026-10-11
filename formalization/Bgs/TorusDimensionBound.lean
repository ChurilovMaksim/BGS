import Std

/- Compiled with Lean 4.33.1 on 11 October 2026. Finite arithmetic kernel only; no analytic, representation-theoretic, rank-classification or BGS formalization. -/

theorem zero_weight_dimension_bound
    (h r mzero mroot dim : Nat)
    (hinj : mzero ≤ r * mroot)
    (hweights : mzero + h * (r * mroot) ≤ dim) :
    (h + 1) * mzero ≤ dim := by
  calc
    (h + 1) * mzero = mzero + h * mzero := by
      rw [Nat.add_mul, Nat.one_mul, Nat.add_comm]
    _ ≤ mzero + h * (r * mroot) :=
      Nat.add_le_add_left (Nat.mul_le_mul_left h hinj) mzero
    _ ≤ dim := hweights

#print axioms zero_weight_dimension_bound
