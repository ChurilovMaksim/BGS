import Std

/-
Finite certificates only. These do not formalize the character-theoretic
spectral theorem, operator norm estimates, smooth functions, or local limits.
Compilation must be reported from an actual successful build, not from the
presence of this source. The Boolean theorem uses kernel decision reduction.
-/
namespace Bgs.GeneralHyperbolicParity

def add2 (a b : Bool) : Bool := if a then !b else b

def refinement (x y : Bool) : Bool := add2 (x && y) (add2 x y)

def determinant2 (a b c d : Bool) : Bool := add2 (a && d) (b && c)

theorem refinement_nonzero :
    forall x y : Bool, refinement x y = (x || y) := by
  decide

theorem invariant_refinement :
    forall a b c d x y : Bool,
      determinant2 a b c d = true ->
      refinement (add2 (a && x) (b && y)) (add2 (c && x) (d && y)) =
        refinement x y := by
  decide

/-- Polarization of the invariant refinement is the symplectic form over F₂.
This certifies the parity identity used in Weyl multiplication, not the
operator representation or any limiting theorem. -/
theorem refinement_polarization :
    forall x y u v : Bool,
      add2 (refinement (add2 x u) (add2 y v))
        (add2 (refinement x y) (refinement u v)) =
          add2 (x && v) (y && u) := by
  decide

theorem nontrivial_central_parity : refinement true false = true := by
  decide

abbrev Mat := (Int × Int) × (Int × Int)

def identity : Mat := ((1,0),(0,1))

def mulMod (n : Int) (a b : Mat) : Mat :=
  (((a.1.1*b.1.1+a.1.2*b.2.1)%n,
    (a.1.1*b.1.2+a.1.2*b.2.2)%n),
   ((a.2.1*b.1.1+a.2.2*b.2.1)%n,
    (a.2.1*b.1.2+a.2.2*b.2.2)%n))

def powMod (n : Int) (a : Mat) : Nat -> Mat
  | 0 => identity
  | k+1 => mulMod n (powMod n a k) a

def minusPell : Mat := ((-3,-2),(-4,-3))
def traceFour : Mat := ((3,2),(1,1))

theorem prime_square_modulus : (169 : Int) = 13*13 := by decide
theorem negative_trace_period : powMod 169 minusPell 7 = identity := by decide
theorem mixed_modulus : (989 : Int) = 23*43 := by decide
theorem mixed_period : powMod 989 traceFour 11 = identity := by decide

theorem odd_sector_dimension : ((169 : Int)-1)/2 = 84 := by decide
theorem odd_root_multiplicity : (84 : Int)/7 = 12 := by decide
theorem even_sector_dimension : ((989 : Int)+1)/2 = 495 := by decide
theorem even_root_multiplicity : (495 : Int)/11 = 45 := by decide

theorem split_factor : (9*9 : Int)%23 = 12 := by decide
theorem nonsplit_square_control :
    ([1,3,4,9,10,12] : List Int).contains 6 = false := by decide

#print axioms invariant_refinement
#print axioms refinement_polarization
#print axioms nontrivial_central_parity
#print axioms negative_trace_period
#print axioms mixed_period

end Bgs.GeneralHyperbolicParity
