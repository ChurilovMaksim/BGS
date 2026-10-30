/-
  BGS derandomization, phase 3: finite / algebraic cores.  Kernel `decide` (no native_decide) and Mathlib `ring`.
  P1  The norm-class form q(x0,x1)=x0^2-6x0x1+x1^2 is invariant under the q-sequence step (x0,x1) -> (x1,6x1-x0).
  P2  Odd part of the kick symbol: 800^2 * ||f_odd||_2^2 = 60  (so the parity variance per step is 4*eta^2*60/800^2).
  P3  Parity lattice: H*1 = 4*1, and sum_j (Hk + a*1)_j = 4*sum k + a*m  (cyclic H = 6 - shift - shift^{-1}).
  P4  -1 is not a power of lambda mod h_m (m = 7: h = 239), so x -> -x is not in Gamma (odd m).
  P5  eta = 0 transfer map (p,q) -> (q,6q-p): no nonzero integer periodic point of period <= 12 with |p|,|q| <= 6.
-/
import Mathlib.Tactic.Ring
namespace Bgs.LineB.Phase3
theorem P1_form_invariant (x0 x1 : Int) :
    x1^2 - 6*x1*(6*x1 - x0) + (6*x1 - x0)^2 = x0^2 - 6*x0*x1 + x1^2 := by ring

/-- c_k * 800 as (re, im) for k = 1..9 and k = -1..-9 (only nonzero ones), from phase2 L2. -/
def cpos : List (Int × Int × Int) := [(1,40,-4),(2,0,-2),(5,0,-1),(6,-20,-2),(7,360,0),(8,-20,2),(9,0,1)]
def cneg : List (Int × Int × Int) := [(1,40,4),(2,0,2),(5,0,1),(6,-20,2),(7,360,0),(8,-20,-2),(9,0,-1)]
/-- 2*(odd coefficient) = c_k - c_{-k}; ||f_odd||^2 = sum_{k != 0} |(c_k - c_{-k})/2|^2 = (1/2) sum_{k>0} |c_k - c_{-k}|^2. -/
def oddSq : Int := ((cpos.zip cneg).map (fun (p, q) => (p.2.1 - q.2.1)^2 + (p.2.2 - q.2.2)^2)).foldl (· + ·) 0
theorem P2_odd_norm : oddSq = 120 := by decide   -- so 800^2 ||f_odd||^2 = oddSq/2 = 60

def Hmul (m : Nat) (k : List Int) : List Int :=
  (List.range m).map (fun (j : Nat) => (6 : Int) * k.getD j 0 - k.getD ((j + m - 1) % m) 0 - k.getD ((j + 1) % m) 0)
theorem P3_H_ones : (List.range 6).all (fun i => Hmul (i+3) (List.replicate (i+3) 1) == List.replicate (i+3) 4) = true := by decide
theorem P3_sum : (List.range 5).all (fun i =>
    let m := i + 3
    let k : List Int := (List.range m).map (fun (j : Nat) => ((j : Int) * 7) % 5 - 2)
    ((Hmul m k).map (· + 3)).foldl (· + ·) 0 == 4 * k.foldl (· + ·) 0 + 3 * (m : Int)) = true := by decide

def zmul (h : Nat) (x y : Nat × Nat) : Nat × Nat :=   -- (a + b*sqrt2) mod h (h odd, Z[lambda]/h = Z[sqrt2]/h)
  ((x.1*y.1 + 2*x.2*y.2) % h, (x.1*y.2 + x.2*y.1) % h)
def lamPow (h e : Nat) : Nat × Nat := (List.range e).foldl (fun p _ => zmul h p (3,2)) (1,0)
theorem P4_m7 : (List.range 7).all (fun k => lamPow 239 k != (238, 0)) = true ∧ lamPow 239 7 = (1,0) := by decide

def step (p : Int × Int) : Int × Int := (p.2, 6*p.2 - p.1)
def iter : Nat → Int × Int → Int × Int
  | 0, p => p
  | n+1, p => iter n (step p)
theorem P5_no_periodic : ((List.range 13).filter (· ≥ 1)).all (fun n =>
    (List.range 13).all (fun i => (List.range 13).all (fun j =>
      let p : Int × Int := ((i : Int) - 6, (j : Int) - 6)
      p == (0,0) || iter n p != p))) = true := by decide

#print axioms P1_form_invariant
#print axioms P2_odd_norm
#print axioms P3_H_ones
#print axioms P3_sum
#print axioms P4_m7
#print axioms P5_no_periodic
end Bgs.LineB.Phase3