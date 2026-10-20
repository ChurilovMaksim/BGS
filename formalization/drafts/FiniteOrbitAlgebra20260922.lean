import Mathlib

/-!
Small algebraic kernels for the finite-orbit argument.

STATUS: source only; Lean/lake were unavailable in the 22 September 2026
execution environment. This file has NOT been typechecked in that pass.
It does not formalize hyperbolicity, holomorphic factorization, Fourier
convergence, the main resonance theorem, or BGS. No `sorry` or new axiom
is used. The hypotheses below remain explicit proof obligations.
-/

namespace BGSFiniteOrbit

/-- A fixed vector cannot have equal images at two times when the
corresponding difference map is injective and vanishes at zero. -/
theorem two_time_cancellation {V : Type*} [AddGroup V]
    (F G : V -> V) (w b : V)
    (hinj : Function.Injective (fun x => F x - G x))
    (hzero : F 0 = G 0) (hF : F w = b) (hG : G w = b) : w = 0 := by
  apply hinj
  rw [hF, hG, hzero]
  simp

/-- Algebraic cancellation behind the common-factor reality step.
Analytic identities and the nonvanishing hypothesis are NOT proved here. -/
theorem common_factor_cancel {K : Type*} [Field K]
    (r a b : K) (hr : r != 0) (ha : r * a = 1) (hb : r * b = 1) : a = b := by
  have h : r * (a - b) = 0 := by
    rw [mul_sub, ha, hb]
    simp
  exact sub_eq_zero.mp ((mul_eq_zero.mp h).resolve_left hr)

end BGSFiniteOrbit
