/-!
# Line L, L2, L3 — numeric constant inequalities (BGS-TRACE-251, 258, 260, 261, 264, 265)

Scaled natural-number forms of the scalar inequalities quoted in the Line L / L2 claims
(`mathematics/fixed-map/lineL_op_open_range.md` §9). Core Lean only, no Mathlib import.
`decide` only; no `native_decide`, no `sorry`.

* `propS_const`: (1.28359 / 1.9154712)^30 ≤ 6.1·10⁻⁶ (Prop S, BGS-TRACE-258).
* `rate_*_lt_target`, `delta8V`: the arb upper ends of the four certified rates are below the targets, and
  1 − 1.2627766/1.28359 ≥ 0.0162 (BGS-TRACE-251; the arb certificate itself is not formalised).
* `barrier8`, `barrier16`: (G/T)² ≥ 3.4074 for T = 1.28359 and ≥ 2.5832 for T = 1.4742, from the arb lower bound
  G ≥ 2.3693985 (BGS-TRACE-260; the bound on G = Σ|J_n(1.8)| is [CA], not formalised).
* `sqrt2_lower`, `sqrt2_upper`: 1.4142135 < √2 < 1.4142136 (as squares).
* `hpair`, `h9`, `h21`, `h_norm`, `barrier_above_h`, `barrier_above_h21`: h_m (rational part of (1+√2)^m) has h_9 = 1393,
  h_21 = 54608393, h² − 2y² = ±1, 2.5832 > 1 + √2 and h_21 < 2.5832^21 (L2-F1).
* `lambda_gt_five`, `B1_const`, `B2_const`: λ = 3 + 2√2 > 5 (Cauchy bound in L2-F2), (L/(L−1))² ≤ 1.4572 at
  L = 5.8284270 ≤ λ (B1; monotonicity of x/(x−1) is a paper step), 1.4923³ ≤ 3.3234 (B2).
* `L3_S3_identity`, `L3_F2_seven`, `L3_F2_49`, `L3_F1_rate` (Line L3, BGS-TRACE-264, 265): h_{3p} = h_p(4h_p² + 3),
  gcd(h_p, K_p) = 1 and 7 ∣ K_p for p = 5…23, 49 ∣ K_7, and (1 + √2)/1.28359 ≥ 1.8808 (finite instances only).
-/

namespace Bgs.LineL

/-- (1.28359/1.9154712)^30 ≤ 61/10^7. -/
theorem propS_const : 12835900 ^ 30 * 10 ^ 7 ≤ 61 * 19154712 ^ 30 := by decide

theorem rate_8V_lt_target : 12627766 < 12835900 := by decide
theorem rate_8E_lt_target : 11364195 < 12835900 := by decide
theorem rate_16V_lt_target : 13924301 < 14742000 := by decide
theorem rate_16E_lt_target : 13027593 < 14742000 := by decide

/-- 1.2627766 ≤ (1 − 0.0162)·1.28359, i.e. δ_OP(8V) ≥ 0.0162. -/
theorem delta8V : 12627766 * 10000 ≤ (10000 - 162) * 12835900 := by decide

/-- (2.3693985/1.28359)² ≥ 3.4074. -/
theorem barrier8 : 34074 * 12835900 ^ 2 ≤ 23693985 ^ 2 * 10 ^ 4 := by decide
/-- (2.3693985/1.4742)² ≥ 2.5832. -/
theorem barrier16 : 25832 * 14742000 ^ 2 ≤ 23693985 ^ 2 * 10 ^ 4 := by decide
theorem barrier8_gt_barrier16 : 25832 < 34074 := by decide

theorem sqrt2_lower : 14142135 ^ 2 < 2 * 10 ^ 14 := by decide
theorem sqrt2_upper : 2 * 10 ^ 14 < 14142136 ^ 2 := by decide

/-- (1+√2)^m = h + y√2: returns (h, y). -/
def hpair : Nat → Nat × Nat
  | 0 => (1, 0)
  | n + 1 => let p := hpair n; (p.1 + 2 * p.2, p.1 + p.2)

theorem h9 : (hpair 9).1 = 1393 := by decide
theorem h21 : (hpair 21).1 = 54608393 := by decide
/-- h² − 2y² = −1 for odd m (here m = 21). -/
theorem h_norm : (hpair 21).1 ^ 2 + 1 = 2 * (hpair 21).2 ^ 2 := by decide
/-- 2.5832 > 1 + 1.4142136 > 1 + √2. -/
theorem barrier_above_h : 10 ^ 7 + 14142136 < 25832000 := by decide
theorem barrier_above_h21 : (hpair 21).1 * 10000 ^ 21 < 25832 ^ 21 := by decide

/-- λ ≥ 3 + 2·1.4142135 = 5.828427 > 5. -/
theorem lambda_gt_five : 5 * 10 ^ 7 < 3 * 10 ^ 7 + 2 * 14142135 := by decide
/-- (L/(L−1))² ≤ 1.4572 at L = 5.8284270. -/
theorem B1_const : 58284270 ^ 2 * 10 ^ 4 ≤ 14572 * 48284270 ^ 2 := by decide
theorem B2_const : 14923 ^ 3 ≤ 33234 * 10 ^ 8 := by decide

/-- L3 (S3): h_{3p} = h_p (4 h_p² + 3) for p = 5, 7, …, 23. -/
theorem L3_S3_identity :
    [5, 7, 11, 13, 17, 19, 23].all
      (fun p => (hpair (3 * p)).1 == (hpair p).1 * (4 * (hpair p).1 ^ 2 + 3)) = true := by decide
/-- L3-F2: gcd(h_p, K_p) = 1 and 7 ∣ K_p (K_p = 4 h_p² + 3) for p = 5, …, 23. -/
theorem L3_F2_seven :
    [5, 7, 11, 13, 17, 19, 23].all
      (fun p => Nat.gcd (hpair p).1 (4 * (hpair p).1 ^ 2 + 3) == 1 &&
        (4 * (hpair p).1 ^ 2 + 3) % 7 == 0) = true := by decide
/-- L3-F2: 49 ∣ K_7. -/
theorem L3_F2_49 : (4 * (hpair 7).1 ^ 2 + 3) % 49 = 0 := by decide
/-- L3-F1: (1 + 1.4142135)/1.28359 ≥ 1.8808. -/
theorem L3_F1_rate : 18808 * 12835900 ≤ 24142135 * 10000 := by decide

end Bgs.LineL

#print axioms Bgs.LineL.propS_const
#print axioms Bgs.LineL.rate_8V_lt_target
#print axioms Bgs.LineL.rate_8E_lt_target
#print axioms Bgs.LineL.rate_16V_lt_target
#print axioms Bgs.LineL.rate_16E_lt_target
#print axioms Bgs.LineL.delta8V
#print axioms Bgs.LineL.barrier8
#print axioms Bgs.LineL.barrier16
#print axioms Bgs.LineL.barrier8_gt_barrier16
#print axioms Bgs.LineL.sqrt2_lower
#print axioms Bgs.LineL.sqrt2_upper
#print axioms Bgs.LineL.h9
#print axioms Bgs.LineL.h21
#print axioms Bgs.LineL.h_norm
#print axioms Bgs.LineL.barrier_above_h
#print axioms Bgs.LineL.barrier_above_h21
#print axioms Bgs.LineL.lambda_gt_five
#print axioms Bgs.LineL.B1_const
#print axioms Bgs.LineL.B2_const
#print axioms Bgs.LineL.L3_S3_identity
#print axioms Bgs.LineL.L3_F2_seven
#print axioms Bgs.LineL.L3_F2_49
#print axioms Bgs.LineL.L3_F1_rate
