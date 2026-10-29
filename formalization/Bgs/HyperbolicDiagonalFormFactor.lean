set_option maxRecDepth 1000000
set_option maxHeartbeats 0

namespace Bgs.HyperbolicDiagonalFormFactor

/-!
# Finite certificate for BGS-TRACE-131

Decides Cassini at ten pairs, `u 6 3 = 198`, the identities
`S^n = v_n S - v_{n-1} I` and `det(S^n - I) = 2 - u_n` for the matrices
and exponents below, and the kernels of those reduced matrices.
The products `42025` and `375` are integer arithmetic of the revival
numerators. They do not formalize `D_2` or the phase average.
-/

def v (t : Int) : Nat → Int
  | 0 => 0
  | 1 => 1
  | n + 2 => t * v t (n + 1) - v t n

def u (t : Int) : Nat → Int
  | 0 => 2
  | n + 1 => t * v t (n + 1) - 2 * v t n

def cassini (t : Int) (n : Nat) : Bool :=
  let vn := v t n
  let vp := v t (n - 1)
  vn * vn - t * vn * vp + vp * vp == 1

theorem cassini_range :
    cassini 3 1 && cassini 3 5 && cassini 3 12 &&
    cassini 6 1 && cassini 6 5 && cassini 6 8 &&
    cassini (-16) 1 && cassini (-16) 4 && cassini 4 3 &&
    cassini 5 6 := by
  decide

theorem sign_trace : u (-6) 5 = -u 6 5 := by decide

theorem gap_model : u 6 3 = 198 ∧ 2 - u 6 3 = -196 := by decide

abbrev Mat := (Int × Int) × (Int × Int)

def norm (n a : Int) : Int := (a % n + n) % n

def mulMod (n : Int) (a b : Mat) : Mat :=
  ((norm n (a.1.1 * b.1.1 + a.1.2 * b.2.1),
    norm n (a.1.1 * b.1.2 + a.1.2 * b.2.2)),
   (norm n (a.2.1 * b.1.1 + a.2.2 * b.2.1),
    norm n (a.2.1 * b.1.2 + a.2.2 * b.2.2)))

def eye : Mat := ((1, 0), (0, 1))

def powMod (n : Int) (a : Mat) : Nat → Mat
  | 0 => eye
  | k + 1 => mulMod n (powMod n a k) a

def model : Mat := ((3, 4), (2, 3))
def five : Mat := ((5, 2), (2, 1))
def fib : Mat := ((2, 1), (1, 1))
def tr5 : Mat := ((4, 1), (3, 1))
def sPlus : Mat := ((-20, -9), (9, 4))
def sMinus : Mat := ((-17, -18), (1, 1))

def mul (a b : Mat) : Mat :=
  ((a.1.1 * b.1.1 + a.1.2 * b.2.1, a.1.1 * b.1.2 + a.1.2 * b.2.2),
   (a.2.1 * b.1.1 + a.2.2 * b.2.1, a.2.1 * b.1.2 + a.2.2 * b.2.2))

def ipow : Mat → Nat → Mat
  | _, 0 => eye
  | a, k + 1 => mul (ipow a k) a

def subI (a : Mat) : Mat :=
  ((a.1.1 - 1, a.1.2), (a.2.1, a.2.2 - 1))

def detM (a : Mat) : Int := a.1.1 * a.2.2 - a.1.2 * a.2.1

def smul (c : Int) (a : Mat) : Mat :=
  ((c * a.1.1, c * a.1.2), (c * a.2.1, c * a.2.2))

def madd (a b : Mat) : Mat :=
  ((a.1.1 + b.1.1, a.1.2 + b.1.2), (a.2.1 + b.2.1, a.2.2 + b.2.2))

/-- `v_n S - v_{n-1} I`, for `n ≥ 1`. -/
def companion (t : Int) (n : Nat) (s : Mat) : Mat :=
  madd (smul (v t n) s) (smul (-(v t (n - 1))) eye)

theorem model_companion_3 : ipow model 3 = companion 6 3 model := by decide
theorem model_det_3 : detM (subI (ipow model 3)) = 2 - u 6 3 := by decide
theorem five_companion_2 : ipow five 2 = companion 6 2 five := by decide
theorem five_det_2 : detM (subI (ipow five 2)) = 2 - u 6 2 := by decide
theorem fib_companion_2 : ipow fib 2 = companion 3 2 fib := by decide
theorem fib_det_2 : detM (subI (ipow fib 2)) = 2 - u 3 2 := by decide
theorem tr5_det : detM (subI tr5) = 2 - u 5 1 := by decide

theorem order41 : powMod 41 model 5 = eye := by decide

theorem order41_not_1 : powMod 41 model 1 ≠ eye := by decide
theorem order41_not_2 : powMod 41 model 2 ≠ eye := by decide
theorem order41_not_4 : powMod 41 model 4 ≠ eye := by decide

theorem same_trace_order_11 :
    powMod 11 model 12 = eye ∧ powMod 11 five 12 = eye := by decide

theorem same_trace_order_11_proper :
    powMod 11 model 6 ≠ eye ∧ powMod 11 five 6 ≠ eye := by decide

def kernelOf (n : Nat) (e00 e01 e10 e11 : Nat) : Nat :=
  (List.range n).foldl (fun acc x =>
    (List.range n).foldl (fun acc2 y =>
      let a := (e00 * x + e01 * y) % n
      let b := (e10 * x + e11 * y) % n
      acc2 + if a = 0 && b = 0 then 1 else 0) acc) 0

def kernelMat (n : Nat) (a : Mat) : Nat :=
  kernelOf n
    (norm (n : Int) (a.1.1 - 1)).toNat
    (norm (n : Int) a.1.2).toNat
    (norm (n : Int) a.2.1).toNat
    (norm (n : Int) (a.2.2 - 1)).toNat

theorem kernel_model_49 : kernelMat 49 (powMod 49 model 3) = 49 := by decide
theorem kernel_five_49 : kernelMat 49 (powMod 49 five 3) = 49 := by decide
theorem kernel_model_7 : kernelMat 7 (powMod 7 model 3) = 49 := by decide
theorem kernel_fib_5 : kernelMat 5 (powMod 5 fib 2) = 5 := by decide

/-- Trace `-16`. The matrices are reduced from their integer entries. -/
theorem kernel_plus_3 : kernelMat 3 sPlus = 9 := by decide
theorem kernel_minus_3 : kernelMat 3 sMinus = 3 := by decide

theorem revival_41 : (5 : Int) * 5 * (41 * 41) = 42025 := by decide
theorem revival_5 : (3 : Int) * 5 * (5 * 5) = 375 := by decide

/-- Cross-multiplication of `1/2 + 1/8 = 5/8`. -/
theorem sigma_five_eighths : ((1 : Int) * 4 + 1) * 1 = 5 := by decide

theorem gcd_time_one :
    Nat.gcd 4 5 = 1 ∧ Nat.gcd 4 7 = 1 ∧ Nat.gcd 4 9 = 1 ∧
    Nat.gcd 4 11 = 1 ∧ Nat.gcd 3 9 = 3 ∧ Nat.gcd 3 5 = 1 := by decide

theorem square_41 : (41 : Int) * 41 = 1681 := by decide

end Bgs.HyperbolicDiagonalFormFactor
