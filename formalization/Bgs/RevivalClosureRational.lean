set_option maxRecDepth 1000000
set_option maxHeartbeats 0

namespace Bgs.RevivalClosureRational

/-!
# Rational witness for BGS-TRACE-133, BGS-TRACE-134 and BGS-TRACE-135

Finite integer facts behind `mathematics/fixed-map/revival_closure_law.md`.
Every theorem is closed by kernel `decide`; there is no `sorry` and no
`native_decide`.

Scope (what is and is not certified):
* `thmA_phase_7` checks the Heisenberg-group phase arithmetic of the
  twisted closure formula (half the symplectic cocycle summed along the
  orbit equals `beta = -2 sum a_i a_j y_(j-i)` modulo 7) for every
  `a` in `(Z/7)^3`. It does not check the operator identity, the trace,
  or the Fourier expansion.
* The orders `ord_N(S)` are certified only for the dimensions listed
  below (minimality included). For 8119, 47321 and 40391 only the integer
  identity `Tr S^t - 2 = kappa N^2` is certified, which gives `S^t = I`
  modulo `N` but not minimality.
* `window_41` and `window_239` are exhaustive instances of the norm lemma.
  At `N = 41`, `L = 3`, `|c| <= 5` there is no non-zero closure at all,
  because every non-zero integer relation has height at least `6` there;
  the check therefore certifies only the absence of non-zero closures.
  At `N = 239`, `L = 4`, `|c| <= 6` non-zero closures exist and every one
  is an exact relation.
* The analytic bound of BGS-TRACE-134 and the conjectural revival laws are
  not formalized.
-/

/-- `[[a, b], [c, d]]`. -/
structure M2 where
  a : Int
  b : Int
  c : Int
  d : Int
deriving DecidableEq

def M2.mul (X Y : M2) : M2 :=
  ⟨X.a * Y.a + X.b * Y.c, X.a * Y.b + X.b * Y.d,
   X.c * Y.a + X.d * Y.c, X.c * Y.b + X.d * Y.d⟩

def M2.modN (X : M2) (N : Int) : M2 := ⟨X.a % N, X.b % N, X.c % N, X.d % N⟩

def catS : M2 := ⟨3, 4, 2, 3⟩
def one : M2 := ⟨1, 0, 0, 1⟩

/-- `S^m` reduced modulo `N` at every step. -/
def powMod (N : Int) : Nat → M2
  | 0 => one.modN N
  | m + 1 => ((powMod N m).mul catS).modN N

/-- Exact `S^m` over the integers. -/
def powZ : Nat → M2
  | 0 => one
  | m + 1 => (powZ m).mul catS

def isOne (N : Int) (X : M2) : Bool := X == one.modN N
def isMinusOne (N : Int) (X : M2) : Bool := X == (⟨-1, 0, 0, -1⟩ : M2).modN N

/-- `ord_N(S) = t`: `S^t = I` and `S^d ≠ I` for `1 <= d < t`. -/
def ordIs (N : Int) (t : Nat) : Bool :=
  isOne N (powMod N t) && (List.range t).all (fun d => d == 0 || !isOne N (powMod N d))

/-- `Tr S^t - 2 = kappa N^2` over the integers. -/
def kappaIs (N : Int) (t : Nat) (k : Int) : Bool :=
  let P := powZ t
  P.a + P.d - 2 == k * N * N

/-! ## Orders and the near-minimal-period families -/

theorem ord_7 : ordIs 7 3 = true := by decide
theorem ord_41 : ordIs 41 5 = true := by decide
theorem ord_239 : ordIs 239 7 = true := by decide
theorem ord_1393 : ordIs 1393 9 = true := by decide
theorem ord_35 : ordIs 35 6 = true := by decide
theorem ord_1189 : ordIs 1189 10 = true := by decide

theorem kappa_7 : kappaIs 7 3 4 = true := by decide
theorem kappa_41 : kappaIs 41 5 4 = true := by decide
theorem kappa_239 : kappaIs 239 7 4 = true := by decide
theorem kappa_1393 : kappaIs 1393 9 4 = true := by decide
theorem kappa_8119 : kappaIs 8119 11 4 = true := by decide
theorem kappa_47321 : kappaIs 47321 13 4 = true := by decide
theorem kappa_35 : kappaIs 35 6 32 = true := by decide
theorem kappa_1189 : kappaIs 1189 10 32 = true := by decide
theorem kappa_40391 : kappaIs 40391 14 32 = true := by decide

/-! ## Cayley–Hamilton, Pell shape, cocycle -/

theorem cayley_hamilton : catS.mul catS = ⟨6 * 3 - 1, 6 * 4, 6 * 2, 6 * 3 - 1⟩ := by decide

def pellShape (X : M2) : Bool :=
  X.a == X.d && X.b == 2 * X.c && X.c % 2 == 0 && X.a * X.a - 8 * (X.c / 2) * (X.c / 2) == 1

theorem pell_shape : (List.range 26).all (fun d => pellShape (powZ d)) = true := by decide

def omega (u v : Int × Int) : Int := u.1 * v.2 - u.2 * v.1

/-- `omega(e2, S^d e2) = -4 y_d`, where `S^d = [[x, 4y], [2y, x]]`. -/
theorem cocycle_y : (List.range 26).all (fun d =>
    let P := powZ d
    omega (0, 1) (P.b, P.d) == -2 * P.c) = true := by decide

/-! ## Phase arithmetic of the twisted closure formula at `N = 7`, `m = 3` -/

def heis (N inv2 : Int) (x y : (Int × Int) × Int) : (Int × Int) × Int :=
  (((x.1.1 + y.1.1) % N, (x.1.2 + y.1.2) % N), (x.2 + y.2 + inv2 * omega x.1 y.1) % N)

def orbitVec (N : Int) (j : Nat) : Int × Int :=
  let P := powZ j
  (P.b % N, P.d % N)

def yv (j : Nat) : Int := (powZ j).c / 2

def phaseOk (N inv2 a0 a1 a2 : Int) : Bool :=
  let g := fun (a : Int) (j : Nat) =>
    (((a * (orbitVec N j).1) % N, (a * (orbitVec N j).2) % N), (0 : Int))
  let prod := heis N inv2 (heis N inv2 (g a0 0) (g a1 1)) (g a2 2)
  let beta := -2 * (a0 * a1 * yv 1 + a0 * a2 * yv 2 + a1 * a2 * yv 1)
  prod.2 % N == beta % N

def Z7 : List Int := (List.range 7).map Int.ofNat

/-- `4` is the inverse of `2` modulo `7`. -/
theorem thmA_phase_7 :
    Z7.all (fun a0 => Z7.all (fun a1 => Z7.all (fun a2 => phaseOk 7 4 a0 a1 a2))) = true := by
  decide

def closes (N a0 a1 a2 : Int) : Bool :=
  (a0 * (orbitVec N 0).1 + a1 * (orbitVec N 1).1 + a2 * (orbitVec N 2).1) % N == 0 &&
  (a0 * (orbitVec N 0).2 + a1 * (orbitVec N 1).2 + a2 * (orbitVec N 2).2) % N == 0

/-- `|Lambda_3| = 7^(3-2)` at `N = 7`. -/
theorem lambda_count_7 :
    (Z7.foldl (fun acc a0 => Z7.foldl (fun acc a1 =>
      Z7.foldl (fun (acc : Nat) a2 => if closes 7 a0 a1 a2 then acc + 1 else acc) acc) acc) 0) = 7 := by
  decide

/-! ## Norm lemma, exhaustive instances

Reduce `sum c_j x^j` modulo `x^2 - 6x + 1`, so `p(S) = alpha I + beta S`.
`p(S) = 0 mod N` iff `N | alpha` and `N | beta` (odd `N`), and `p(lambda) = 0`
iff `alpha = beta = 0`. -/

def coeffRange (A : Nat) : List Int :=
  (List.range (2 * A + 1)).map (fun i => Int.ofNat i - Int.ofNat A)

def red3 (c0 c1 c2 : Int) : Int × Int := (c0 - c2, c1 + 6 * c2)
def red4 (c0 c1 c2 c3 : Int) : Int × Int := (c0 - c2 - 6 * c3, c1 + 6 * c2 + 35 * c3)

def implies (N : Int) (r : Int × Int) : Bool :=
  !(r.1 % N == 0 && r.2 % N == 0) || (r.1 == 0 && r.2 == 0)

/-- `N = 41`, window `L = 3`, `|c_j| <= 5`; `A^2 lambda^L / 4 < N^2`.
Certifies that no non-zero closure exists in this box. -/
theorem window_41 : (coeffRange 5).all (fun c0 => (coeffRange 5).all (fun c1 =>
    (coeffRange 5).all (fun c2 => implies 41 (red3 c0 c1 c2)))) = true := by decide

/-- `N = 239`, window `L = 4`, `|c_j| <= 6`; `A^2 lambda^L / 4 < N^2`.
Every closure in this box is an exact relation (for example `1 - 6x + x^2`). -/
theorem window_239 : (coeffRange 6).all (fun c0 => (coeffRange 6).all (fun c1 =>
    (coeffRange 6).all (fun c2 => (coeffRange 6).all (fun c3 =>
      implies 239 (red4 c0 c1 c2 c3))))) = true := by decide

/-- The box of `window_239` does contain a non-zero relation. -/
theorem window_239_nonvacuous : red4 1 (-6) 1 0 = (0, 0) := by decide

/-! ## Half-period parity at even-order primes -/

theorem half_61 : isMinusOne 61 (powMod 61 31) = true := by decide
theorem half_101 : isMinusOne 101 (powMod 101 51) = true := by decide
theorem ord_61 : ordIs 61 62 = true := by decide
theorem ord_101 : ordIs 101 102 = true := by decide

#print axioms ord_7
#print axioms ord_41
#print axioms ord_239
#print axioms ord_1393
#print axioms ord_35
#print axioms ord_1189
#print axioms kappa_7
#print axioms kappa_41
#print axioms kappa_239
#print axioms kappa_1393
#print axioms kappa_8119
#print axioms kappa_47321
#print axioms kappa_35
#print axioms kappa_1189
#print axioms kappa_40391
#print axioms cayley_hamilton
#print axioms pell_shape
#print axioms cocycle_y
#print axioms thmA_phase_7
#print axioms lambda_count_7
#print axioms window_41
#print axioms window_239
#print axioms window_239_nonvacuous
#print axioms half_61
#print axioms half_101
#print axioms ord_61
#print axioms ord_101
end Bgs.RevivalClosureRational
