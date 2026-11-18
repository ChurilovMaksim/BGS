import Std

namespace Bgs.OldspaceOutliers

/-- Coefficients of a power of a primitive 28th root in the power basis.
    Uses X^14=-1 and X^12=X^10-X^8+X^6-X^4+X^2-1. -/
private def powerCoord (exponent : Int) (degree : Nat) : Int :=
  let e := (exponent % 28).toNat
  let r := e % 14
  let sign : Int := if e < 14 then 1 else -1
  if r < 12 then
    if r == degree then sign else 0
  else
    let d := r - 12
    if d ≤ degree && (degree-d) % 2 == 0 && degree < 12 then
      if (degree-d) % 4 == 0 then -sign else sign
    else 0

private def gradient (j : Int) (degree : Nat) : Int :=
  -10 * (powerCoord (7+4*j) degree - powerCoord (7-4*j) degree)
  + powerCoord (8*j) degree + powerCoord (-8*j) degree
  - powerCoord (4*j) degree - powerCoord (-4*j) degree

theorem gradient_rational_kernel (a b c d e f : Int)
    (h : ∀ j : Nat, 0 < j → j < 12 →
      a*gradient 1 j + b*gradient 2 j + c*gradient 3 j +
      d*gradient 4 j + e*gradient 5 j + f*gradient 6 j = 0) :
    a = b ∧ b = c ∧ c = d ∧ d = e ∧ e = f := by
  have h₁ := h 1 (by decide) (by decide)
  have h₃ := h 3 (by decide) (by decide)
  have h₄ := h 4 (by decide) (by decide)
  have h₅ := h 5 (by decide) (by decide)
  have h₆ := h 6 (by decide) (by decide)
  change a*0 + b*20 + c*0 + d*0 + e*(-20) + f*0 = 0 at h₁
  change a*10 + b*(-10) + c*0 + d*0 + e*10 + f*(-10) = 0 at h₃
  change a*(-1) + b*(-1) + c*2 + d*2 + e*(-1) + f*(-1) = 0 at h₄
  change a*0 + b*10 + c*10 + d*(-10) + e*(-10) + f*0 = 0 at h₅
  change a*(-1) + b*2 + c*(-1) + d*(-1) + e*2 + f*(-1) = 0 at h₆
  omega

/-- Terms are (frequency of z, power of i, coefficient). -/
private abbrev Laurent := List (Int × Int × Int)

private def mulTerms (f g : Laurent) : Laurent :=
  f.flatMap (fun (k, j, c) => g.map fun (l, i, d) => (k+l, j+i, c*d))

private def hopping : Laurent :=
  mulTerms [(0,0,2), (7,0,-1), (-7,0,-1)] [(0,0,2), (1,0,1), (-1,0,1)]

private def potential : Laurent :=
  [(7,0,400), (-7,0,400), (0,0,-80)] ++
    mulTerms hopping [(0,0,20), (1,1,-1), (-1,1,1)]

private def diff (f : Laurent) : Laurent :=
  f.map fun (k, j, c) => (k, j+1, k*c)

private def atRoot (f : Laurent) (power : Int) (degree : Nat) : Int :=
  (f.map fun (k,j,c) => c * powerCoord (k*power+7*j) degree).sum

theorem gradient_evaluation :
    ∀ j : Fin 7, ∀ d : Fin 12,
      atRoot (diff potential) (14+4*(j.val : Int)) d.val =
        8*gradient j.val d.val := by decide

theorem curvature :
    ∀ d : Fin 12,
      ((List.range 7).map (fun j : Nat =>
        atRoot (diff (diff potential)) (14+4*(j : Int)) d.val)).sum -
        7*atRoot (diff (diff potential)) 14 d.val =
      (if d.val == 0 then -28560 else 0) := by decide

theorem hopping_jet :
    ∀ j : Fin 7, ∀ d : Fin 12,
      atRoot hopping (4*(j.val : Int)) d.val = 0 ∧
      atRoot (diff hopping) (4*(j.val : Int)) d.val = 0 ∧
      atRoot (diff (diff hopping)) (4*(j.val : Int)) d.val =
        196*powerCoord 0 d.val +
          98*(powerCoord (4*(j.val : Int)) d.val + powerCoord (-4*(j.val : Int)) d.val) :=
  by decide

theorem first_uniform_excess (k a b c d e f g h i j l m : Nat)
    (left : a+b+c+d+e+f ≤ k) (right : g+h+i+j+l+m ≤ k)
    (δ : Int) (nonzero : δ ≠ 0)
    (h₁ : (a : Int)-g = δ) (h₂ : (b : Int)-h = δ)
    (h₃ : (c : Int)-i = δ) (h₄ : (d : Int)-j = δ)
    (h₅ : (e : Int)-l = δ) (h₆ : (f : Int)-m = δ) :
    6 ≤ k ∧ (k = 6 → δ = 1 ∨ δ = -1) := by omega

theorem haar_net_factor : 1352 * 40^48 < (47 : Nat)^48 := by decide

#print axioms haar_net_factor
#print axioms gradient_rational_kernel
#print axioms gradient_evaluation
#print axioms curvature
#print axioms hopping_jet
#print axioms first_uniform_excess
end Bgs.OldspaceOutliers
