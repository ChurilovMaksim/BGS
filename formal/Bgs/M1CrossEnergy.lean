/-
  M1 cross-energy formal track.

  STATUS: UNVERIFIED IN THE CURRENT AUDIT RUNTIME.
  The current environment used for the Python/C++ research cycle does not
  have Lean/Lake installed. This file must not be cited as machine-checked
  until `lake build` succeeds in a real Lean toolchain.

  Load-bearing general formalisation targets:

  F1. regular key parametrisation (u,v) <-> (x,y) away from the singular key;
  F2. singular collapse x=y -> (u,v,d)=(1,1,0) with multiplicity N-2;
  F3. quotient-character projector reconstruction of B(t);
  F4. exact full double-sum energy expansion, including cross twists;
  F5. polynomial domain-mask + non-m-th-power classification from M1 cycle 002.

  K2Reduction.lean already certifies the N=53 instance of the regular
  HxH count |P|=(K-1)(K-2). M1_WEIL_002.md contains the human proof of F5;
  the finite Bool checks below are only formal regression targets, not a
  replacement for the general statement.
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

/-! ## Cycle 002 finite residue classifiers

For a primitive quotient character of order m, the polynomial domain mask
Q_d^m changes root multiplicities only by multiples of m. The residue vectors
for the three divisor geometries are:

  generic:  (r, -r, s, -s)
  d = 1:    (r, s-r, -s)
  d = -1:   (-r, r-s, s)

A nontrivial pair must leave at least one nonzero residue. The human general
proof is elementary; these definitions encode representative finite checks.
-/

/-- additive inverse modulo m, written with Nat arithmetic -/
def negMod (x m : Nat) : Nat := (m - (x % m)) % m

/-- generic four-root residue obstruction -/
def genericResiduePass (m r s : Nat) : Bool :=
  !((r % m == 0) && (negMod r m == 0) && (s % m == 0) && (negMod s m == 0))

/-- d=1 collision residue obstruction: (r, s-r, -s) -/
def d1ResiduePass (m r s : Nat) : Bool :=
  let sr := (s + negMod r m) % m
  !((r % m == 0) && (sr == 0) && (negMod s m == 0))

/-- d=-1 collision residue obstruction: (-r, r-s, s) -/
def dm1ResiduePass (m r s : Nat) : Bool :=
  let rs := (r + negMod s m) % m
  !((negMod r m == 0) && (rs == 0) && (s % m == 0))

/-- Exhaust a finite quotient-character square, skipping the trivial pair. -/
def allPairsPass (m : Nat) (pred : Nat -> Nat -> Nat -> Bool) : Bool :=
  (List.range m).all fun r =>
    (List.range m).all fun s =>
      if (r == 0) && (s == 0) then true else pred m r s

/-- Representative m=4 check (historical N=53 subgroup calibration). -/
theorem residueClassifier4 :
    (allPairsPass 4 genericResiduePass &&
     allPairsPass 4 d1ResiduePass &&
     allPairsPass 4 dm1ResiduePass) = true := by
  native_decide

/-- Representative m=18 check (N=199,K=11). -/
theorem residueClassifier18 :
    (allPairsPass 18 genericResiduePass &&
     allPairsPass 18 d1ResiduePass &&
     allPairsPass 18 dm1ResiduePass) = true := by
  native_decide

/-- Representative m=20 check (N=461,K=23). -/
theorem residueClassifier20 :
    (allPairsPass 20 genericResiduePass &&
     allPairsPass 20 d1ResiduePass &&
     allPairsPass 20 dm1ResiduePass) = true := by
  native_decide

#print axioms orderCertificate199
#print axioms orderCertificate461
#print axioms orderCertificate3571
#print axioms calibration53NotTrace3
#print axioms residueClassifier4
#print axioms residueClassifier18
#print axioms residueClassifier20

end Bgs.M1CrossEnergy
