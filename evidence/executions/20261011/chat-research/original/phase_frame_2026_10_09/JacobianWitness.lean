import Std

/- A bounded arithmetic witness only. The generic density theorem, analytic
   null-set lemma, and submersion theorem are NOT formalized by this file.
   No Lean executable was available in the research environment; this file
   must be compiled before calling even its finite statement machine checked. -/

def det3 (a b c d e f g h i : Int) : Int :=
  a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def det4 (a : Fin 4 → Fin 4 → Int) : Int :=
  a 0 0 * det3 (a 1 1) (a 1 2) (a 1 3) (a 2 1) (a 2 2) (a 2 3) (a 3 1) (a 3 2) (a 3 3)
  - a 0 1 * det3 (a 1 0) (a 1 2) (a 1 3) (a 2 0) (a 2 2) (a 2 3) (a 3 0) (a 3 2) (a 3 3)
  + a 0 2 * det3 (a 1 0) (a 1 1) (a 1 3) (a 2 0) (a 2 1) (a 2 3) (a 3 0) (a 3 1) (a 3 3)
  - a 0 3 * det3 (a 1 0) (a 1 1) (a 1 2) (a 2 0) (a 2 1) (a 2 2) (a 3 0) (a 3 1) (a 3 2)

def phaseWitness (r c : Fin 4) : Int :=
  match r.val, c.val with
  | 0, 0 => 1
  | 0, 2 => 1
  | 0, 3 => 1
  | 1, 1 => 1
  | 1, 2 => 1
  | 1, 3 => 1
  | 2, 2 => 1
  | 3, 3 => 1
  | _, _ => 0

theorem phaseWitness_determinant : det4 phaseWitness = 1 := by
  decide

#eval det4 phaseWitness
