set_option maxRecDepth 1000000
set_option maxHeartbeats 0

namespace Bgs.HyperbolicDiagonalFormFactor

/-!
# Finite certificate for BGS-TRACE-131

Companion values, kernel counts, the order of the model matrix modulo 41,
the revival cross-multiplications, and the trace-equivalent kernel split.
The operator expansion is not formalized.
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

theorem gap_tr5 : (4 * 0 - 1 * 3 : Int) = -3 ∧ 2 - 5 = -3 := by decide

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

/-- `S^3 - I` for `S = [[3,4],[2,3]]` is `[[98,140],[70,98]]`. -/
theorem kernel_model_49 : kernelOf 49 98 140 70 98 = 49 := by decide

/-- `S^3 - I` for `S = [[5,2],[2,1]]` is `[[168,70],[70,28]]`. -/
theorem kernel_five_49 : kernelOf 49 168 70 70 28 = 49 := by decide

theorem kernel_model_7 : kernelOf 7 98 140 70 98 = 49 := by decide

/-- Unipotent defect: `S = [[2,1],[1,1]]`, `S^2 - I` modulo 5. -/
theorem kernel_fib_5 : kernelOf 5 4 3 3 1 = 5 := by decide

/-- Trace `-16`, outside `gcd(β, p) = 1`. Residues modulo 3. -/
theorem kernel_plus_3 : kernelOf 3 0 0 0 0 = 9 := by decide
theorem kernel_minus_3 : kernelOf 3 0 0 1 0 = 3 := by decide

theorem revival_41 : (5 : Int) * 5 * (41 * 41) = 42025 := by decide
theorem revival_5 : (3 : Int) * 5 * (5 * 5) = 375 := by decide

/-- Cross-multiplication of `1/2 + 1/8 = 5/8`. -/
theorem sigma_five_eighths : ((1 : Int) * 4 + 1) * 1 = 5 := by decide

theorem gcd_time_one :
    Nat.gcd 4 5 = 1 ∧ Nat.gcd 4 7 = 1 ∧ Nat.gcd 4 9 = 1 ∧
    Nat.gcd 4 11 = 1 ∧ Nat.gcd 3 9 = 3 ∧ Nat.gcd 3 5 = 1 := by decide

theorem square_41 : (41 : Int) * 41 = 1681 := by decide

end Bgs.HyperbolicDiagonalFormFactor
