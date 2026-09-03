/-
  M1 cross-energy formal track.

  STATUS: UNVERIFIED IN THE CURRENT AUDIT RUNTIME.
  The current environment used for the Python/C++ research cycle does not
  have Lean/Lake installed, so this file is deliberately limited to small,
  transparent arithmetic certificates and formal targets. It must not be
  cited as machine-checked until `lake build` succeeds in a Lean toolchain.

  The load-bearing general statements still to formalise are:

  F1. the regular key parametrisation (u,v) <-> (x,y) away from u=v=1;
  F2. the singular collapse x=y -> (u,v,d)=(1,1,0) with multiplicity N-2;
  F3. quotient-character projector reconstruction of B(t);
  F4. the exact full double-sum energy expansion, including cross twists;
  F5. divisor/perfect-power exclusion for the regular rational function.

  K2Reduction.lean already certifies the N=53 instance of the regular
  HxH count |P|=(K-1)(K-2). This file begins the arithmetic-regime side
  of M1 and records concrete trace-3 order certificates.
-/

namespace Bgs.M1CrossEnergy

/-- Integer trace sequence for alpha + alpha^{-1} = 3:
    L_0=2, L_1=3, L_{n+2}=3L_{n+1}-L_n. -/
def trace3Lucas : Nat -> Nat
  | 0 => 2
  | 1 => 3
  | Nat.succ (Nat.succ n) => 3 * trace3Lucas (Nat.succ n) - trace3Lucas n

/-- If a trace-3 eigenvalue has order 11 mod 199, the necessary
    integer divisibility certificate is visible in L_11-2. -/
theorem orderCertificate199 : (trace3Lucas 11 - 2) % 199 = 0 := by
  native_decide

/-- Same necessary certificate for the new N=461, K=23 anchor. -/
theorem orderCertificate461 : (trace3Lucas 23 - 2) % 461 = 0 := by
  native_decide

/-- Same necessary certificate for the historical large design
    N=3571, K=17. -/
theorem orderCertificate3571 : (trace3Lucas 17 - 2) % 3571 = 0 := by
  native_decide

/-- The historical N=53, a=10 subgroup calibration is not a trace-3
    eigenvalue example. This prevents accidental reuse as such. -/
theorem calibration53NotTrace3 : (((10 * 10 + 1) % 53) == ((3 * 10) % 53)) = false := by
  native_decide

#print axioms orderCertificate199
#print axioms orderCertificate461
#print axioms orderCertificate3571
#print axioms calibration53NotTrace3

end Bgs.M1CrossEnergy
