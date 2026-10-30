import Mathlib
-- negative control: a false certificate must NOT typecheck
def xy : ℕ → ℤ × ℤ
  | 0 => (1, 0)
  | d + 1 => (3 * (xy d).1 + 8 * (xy d).2, (xy d).1 + 3 * (xy d).2)
def nsw : ℕ → ℤ
  | 0 => 1
  | 1 => 7
  | j + 2 => 6 * nsw (j + 1) - nsw j

/-- the finite certificate for m = 2j+1 with explicit nu* -/
def cert (j : ℕ) (nu : ℤ) : Bool :=
  let m := 2 * j + 1
  let h := nsw j
  let xm := (xy m).1
  let ym := (xy m).2
  let D := 2 * (xm - 1)
  let yp := ym / h
  let k := (-4 * nu - 1) / h
  let kap := (k * yp) % 8
  let phi : ℕ → ℤ := fun d => if d = 0 then ym else ym * (xy d).1 - (xm - 1) * (xy d).2
  decide (D = 4 * h ^ 2) && decide (ym % h = 0) && decide (nu % 2 = 1) &&
  decide ((4 * nu + 1) % h = 0) &&
  decide ((-4 * h * nu * yp - phi 0 - kap * h ^ 2) % (8 * h ^ 2) = 0) &&
  (List.range m).all (fun d => d = 0 ||
     decide ((-2 * nu * yp * (xy d).1 * (2 * h) - phi d - kap * h ^ 2) % (4 * h ^ 2) = 0))

theorem bad : cert 3 181 = true := by decide
