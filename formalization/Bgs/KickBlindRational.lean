set_option maxRecDepth 100000

namespace Bgs.KickBlindRational

/-!
# Rational witness for BGS-TRACE-117

This file certifies fully expanded rational inequalities.  It does not
formalize Weyl operators, the matrix exponential, or the trace comparison.
Those steps are in `mathematics/fixed-map/kick_blind_arithmetic_spike.md`
and are rechecked by `computations/verification/kick_blind_spike.py` and
`computations/cpp/kick_blind_spike.cpp`.

`B = 184981/160000` is the rational majorant of `Σ |c_kl|` produced by those
two verifiers.  `u_201` is computed here from the recurrence
`(1+√2)^n = u_n + v_n √2`.
-/

def iter : Nat → Int × Int
  | 0 => (1, 0)
  | n + 1 =>
    let (u, v) := iter n
    (u + 2 * v, u + v)

def u201 : Int := (iter 201).1

def v201 : Int := (iter 201).2

theorem kickBlind_norm : u201 * u201 - 2 * v201 * v201 = -1 := by
  decide

theorem kickBlind_positive : u201 > 0 ∧ v201 > 0 := by
  decide

theorem kickBlind_odd : u201 % 2 = 1 := by
  decide

theorem kickBlind_bases : (iter 5).1 = 41 ∧ (iter 7).1 = 239 := by
  decide

def xNum : Int := u201 * 184981

def xDen : Int := (10 : Int) ^ 80 * 160000

/-- `ρ_201 < 1`, i.e. `xDen > (n+1) xNum` at `n = 201`. -/
theorem kickBlind_rho : xDen > (201 + 1) * xNum := by
  decide

/-- Uniform comparison `(1-ρ_201)^2 * (225/239) > 3/4`, cleared as
`300 (xDen - 202 xNum)^2 > 239 (xDen - xNum)^2`.
Together with the monotonicity argument in the proof note, this is the
kicked gap for every odd `n` from 7 through 201. -/
theorem kickBlind_uniform : 300 * (xDen - (201 + 1) * xNum) ^ 2 >
    239 * (xDen - xNum) ^ 2 := by
  decide

def xNum5 : Int := 41 * 184981

def xDen5 : Int := (10 : Int) ^ 80 * 160000

theorem kickBlind_n5_rho : xDen5 > 6 * xNum5 := by
  decide

/-- Endpoint `n = 5`: `(1-ρ_5)^2 * (31/41) > 3/4`. -/
theorem kickBlind_n5 : 124 * (xDen5 - 6 * xNum5) ^ 2 >
    123 * (xDen5 - xNum5) ^ 2 := by
  decide
#print axioms kickBlind_norm
#print axioms kickBlind_positive
#print axioms kickBlind_odd
#print axioms kickBlind_bases
#print axioms kickBlind_rho
#print axioms kickBlind_uniform
#print axioms kickBlind_n5_rho
#print axioms kickBlind_n5
end Bgs.KickBlindRational
