set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false

namespace Bgs.LineDCerts

/-!
# Line D: finite arithmetic certificates (kernel `decide`, Lean core only, no Mathlib import)

Certificates for the Line D note (`mathematics/fixed-map/band_limited_kick_bridge.md`):

* `hx_ok`: `H_m X_m = D_m I` for `3 ≤ m ≤ 8`, where `H_m = 6I - C - Cᵀ` and
  `X_m[i][j] = y_m x_d - (D_m/2) y_d [i ≠ j]`, `d = |i-j|`, `S^d = [[x_d,4y_d],[2y_d,x_d]]`
  (Line B Lemma Q).  This is the integer inverse used in `A(n) = 2 nᵀ X_m n` (Theorem D1).
* `fix_count`: the number of period-`m` sequences `x_{j+1} = 6x_j - x_{j-1}` in `Z/d₂`
  (i.e. pairs `(x₀,x₁)` with `x_m = x₀`, `x_{m+1} = x₁`) equals `D_m`
  (`m = 3, d₂ = 28`; `m = 4, d₂ = 96`).  Together with the classical count |Fix(T^m)| = D_m
  (T = [[0,1],[-1,6]]) this shows that all of `Fix_m` lies in `d₂`-torsion for these `m`.
* `rad_count`: `#{w ∈ (Z/4)^m : H_m w ≡ 0 (mod 4)}` equals `4, 16, 4, 8` for `m = 3, 4, 5, 6`;
  by Prop. D3 (Line B Prop R) this is `D_m / D_eff`, the inverse density of the support of the Gauss weights.
* `coll4_ok`, `coll6_ok`: every listed sequence (2 for `m = 4`, 26 for `m = 6`) is a genuine period-`m`
  solution of `x_{j+1} = 6x_j − x_{j-1}` in `Z/d₂` whose point multiset is invariant under `x ↦ x + d₂/2`,
  hence has `S_k = 0` for every odd `k` (Lemma D5(b)), and the `m = 6` list has length 26.
  These theorems certify **only the listed sequences**.  They do **not** certify that the sequences lie on the
  support of the Gauss weights, that they are pairwise Γ-inequivalent, or that they form the complete K = 1
  collision set; those three facts are checked in Python (`code/collisions.py`, `logs/collisions.log`; referee
  replay `referee_replay/lean_semantics.py`, `lean_semantics.log`).

Not formalised: the Gauss-sum completion (Theorem D1), the Fourier inversion (Prop. D3), the
strong-kick limit (Theorem D4), analytic bounds, the regime-III estimate, and all numerics.
`hx_ok` checks H X = D I with D := 2(x_m − 1); it does not prove det H_m = D_m (classical product formula).
`rad_count` computes #ker(H_m mod 4); its identification with D_m/D_eff is Line B Prop R / Prop. D3.
-/

/-! ## Pell data and the matrices H_m, X_m -/

def pellXY : Nat → Int × Int
  | 0 => (1, 0)
  | n + 1 => let (x, y) := pellXY n; (3 * x + 8 * y, x + 3 * y)

def Dm (m : Nat) : Int := 2 * ((pellXY m).1 - 1)

def dist (i j : Nat) : Nat := if i ≤ j then j - i else i - j

def Hent (m i j : Nat) : Int :=
  (if i = j then 6 else 0) - (if (i + 1) % m = j then 1 else 0) - (if (j + 1) % m = i then 1 else 0)

def Xent (m i j : Nat) : Int :=
  let d := dist i j
  (pellXY m).2 * (pellXY d).1 - (if i = j then 0 else (Dm m / 2) * (pellXY d).2)

def hxOK (m : Nat) : Bool :=
  (List.range m).all fun i => (List.range m).all fun j =>
    ((List.range m).foldl (fun acc k => acc + Hent m i k * Xent m k j) 0) == (if i = j then Dm m else 0)

theorem hx_ok : (hxOK 3 && hxOK 4 && hxOK 5 && hxOK 6 && hxOK 7 && hxOK 8) = true := by decide

theorem D_values : (Dm 3, Dm 4, Dm 5, Dm 6) = (196, 1152, 6724, 39200) := by decide

/-! ## Orbit count |Fix_m| = D_m in Z/d₂ -/

/-- iterate (a, b) ↦ (b, 6b - a) mod M, n times -/
def stepN (M : Nat) : Nat → Nat × Nat → Nat × Nat
  | 0, v => v
  | n + 1, (a, b) => stepN M n (b, (6 * b + 5 * M * M - a) % M)

def isPeriodic (M m a b : Nat) : Bool := stepN M m (a, b) == (a, b)

def fixCount (M m : Nat) : Nat :=
  (List.range M).foldl (fun acc a => acc + ((List.range M).filter (fun b => isPeriodic M m a b)).length) 0

theorem fix_count : (fixCount 28 3, fixCount 96 4) = (196, 1152) := by decide

/-! ## Radical size #ker(H_m mod 4) -/

def digits4 : Nat → Nat → List Nat
  | 0, _ => []
  | k + 1, n => (n % 4) :: digits4 k (n / 4)

def inKer4 (m : Nat) (w : List Nat) : Bool :=
  (List.range m).all fun i =>
    let s : Int := (List.range m).foldl (fun acc j => acc + Hent m i j * (w.getD j 0 : Int)) 0
    s % 4 == 0

def radCount (m : Nat) : Nat :=
  ((List.range (4 ^ m)).filter (fun n => inKer4 m (digits4 m n))).length

theorem rad_count : (radCount 3, radCount 4, radCount 5, radCount 6) = (4, 16, 4, 8) := by decide

/-! ## K = 1 collision groups: half-turn invariant orbits -/

/-- the full orbit x₀, …, x_{m-1} from (x₀, x₁) -/
def orbitSeq (M : Nat) : Nat → Nat → Nat → List Nat
  | 0, _, _ => []
  | n + 1, a, b => a :: orbitSeq M n b ((6 * b + 5 * M * M - a) % M)

def isOrbit (M : Nat) (xs : List Nat) : Bool :=
  match xs with
  | a :: b :: _ => orbitSeq M xs.length a b == xs && isPeriodic M xs.length a b
  | _ => false

def countIn (x : Nat) (xs : List Nat) : Nat := (xs.filter (· == x)).length

/-- multiset invariance under q ↦ q + 1/2, i.e. x ↦ x + M/2 (mod M) -/
def halfTurnInv (M : Nat) (xs : List Nat) : Bool :=
  xs.all fun x => countIn x xs == countIn ((x + M / 2) % M) xs

def collOK (M : Nat) (L : List (List Nat)) : Bool := L.all fun xs => isOrbit M xs && halfTurnInv M xs

def coll4 : List (List Nat) := [[0, 48, 0, 48], [80, 32, 16, 64]]

def coll6 : List (List Nat) :=
  [[284, 4, 300, 116, 396, 20], [340, 348, 68, 60, 292, 12], [300, 340, 60, 20, 60, 340],
   [300, 420, 540, 20, 140, 260], [228, 300, 452, 172, 20, 508], [500, 460, 20, 220, 180, 300],
   [380, 20, 300, 100, 300, 20], [420, 28, 308, 140, 532, 252], [36, 460, 484, 204, 180, 316],
   [324, 220, 436, 156, 500, 44], [52, 332, 260, 108, 388, 540], [340, 540, 100, 60, 260, 380],
   [340, 460, 180, 60, 180, 460], [516, 236, 340, 124, 404, 60], [420, 220, 340, 140, 500, 60],
   [244, 524, 100, 76, 356, 380], [476, 196, 140, 84, 364, 420], [92, 180, 428, 148, 460, 372],
   [380, 180, 140, 100, 460, 420], [188, 468, 380, 132, 412, 100], [500, 380, 100, 220, 100, 380],
   [420, 140, 420, 140, 420, 140], [556, 260, 444, 164, 540, 276], [460, 260, 540, 180, 540, 260],
   [500, 268, 548, 220, 212, 492], [540, 500, 220, 260, 220, 500]]

theorem coll4_ok : collOK 96 coll4 = true := by decide
theorem coll6_ok : (collOK 560 coll6 && coll6.length == 26) = true := by decide

/-! ## Controls: the checkers reject wrong data -/

/-- wrong determinant (D_3 + 1) is rejected by the H X = D I checker -/
def hxBad (m : Nat) : Bool :=
  (List.range m).all fun i => (List.range m).all fun j =>
    ((List.range m).foldl (fun acc k => acc + Hent m i k * Xent m k j) 0) == (if i = j then Dm m + 1 else 0)

theorem hx_control : hxBad 3 = false := by decide
theorem fix_control : fixCount 28 3 ≠ 197 := by decide
theorem rad_control : radCount 4 ≠ 4 := by decide
/-- a non-orbit and a non-half-turn-invariant orbit are rejected -/
theorem coll_control : (collOK 96 [[0, 48, 0, 47]], collOK 96 [[0, 0, 0, 0]]) = (false, false) := by decide

end Bgs.LineDCerts

#print axioms Bgs.LineDCerts.hx_ok
#print axioms Bgs.LineDCerts.fix_count
#print axioms Bgs.LineDCerts.rad_count
#print axioms Bgs.LineDCerts.coll4_ok
#print axioms Bgs.LineDCerts.coll6_ok
#print axioms Bgs.LineDCerts.coll_control
#print axioms Bgs.LineDCerts.D_values
#print axioms Bgs.LineDCerts.hx_control
#print axioms Bgs.LineDCerts.fix_control
#print axioms Bgs.LineDCerts.rad_control
