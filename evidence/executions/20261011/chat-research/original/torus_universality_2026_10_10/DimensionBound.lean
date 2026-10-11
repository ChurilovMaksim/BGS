import Std

/-
Arithmetic tail of the zero-weight argument.  The representation-theoretic
injection and root multiplicities are proved in torus_contraction.md, not here.
Lean/lake are absent from the current runtime: this source is UNCOMPILED.
It must not be called a machine-checked proof or a formalization of BGS.
-/

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
