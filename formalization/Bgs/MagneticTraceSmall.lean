import Std
/- Exact finite affine-word histograms at p=7, K=3, through fourth order.
   These are finite certificates, not the analytic global semicircle theorem. -/
namespace Bgs.MagneticTraceSmall
set_option maxRecDepth 100000
set_option maxHeartbeats 0
structure State where
  u : Int
  v : Int
  l : Int
  d : Int
  deriving Repr

def letters : List (Int × Int) :=
  [(-1,1),(-1,4),(-1,2),(1,1),(1,4),(1,2)]

def step (s : State) (z : Int × Int) : State :=
  let e := z.1
  let h := z.2
  {u := (h*s.u)%7, v := (h*(s.v-e))%7,
   l := (s.l+e*s.u)%7, d := (s.d+e*s.v-4)%7}

def states : Nat → List State
  | 0 => [{u:=1,v:=0,l:=0,d:=0}]
  | m+1 => (states m).flatMap (fun s => letters.map (step s))

def coefficient (s : State) (t : Int) : Int :=
  (List.range 7).foldl (fun acc k =>
    let x : Int := Int.ofNat k
    let pos : Int := if (s.u*x+s.v)%7=x ∧ (s.l*x+s.d)%7=t then 1 else 0
    let neg : Int := if (-s.u*x+s.v)%7=x ∧ (-s.l*x+s.d)%7=t then 1 else 0
    acc+pos-neg) 0

def histogram (m : Nat) : List Int :=
  (List.range 7).map (fun t => (states m).foldl (fun a s => a+coefficient s (Int.ofNat t)) 0)

def canonical (m : Nat) : List Int :=
  let c := histogram m
  c.map (fun a => a-c.getD 6 0)

/- On the one-dimensional odd block at p=7,K=3,
A_q=(z^2+z^5-z-z^6-1)/3, z=e_7(q).
Hence the trace histogram is 2 times the m-th cyclic power of S.
This calculation is independent of affine-word enumeration. -/
def baseCoefficients : List Int := [-1,-1,1,0,0,1,-1]

def cyclicConvolution (a b : List Int) : List Int :=
  (List.range 7).map (fun t =>
    (List.range 7).foldl (fun acc j =>
      acc + a.getD j 0 * b.getD ((t+7-j)%7) 0) 0)

def coefficientPower : Nat -> List Int
  | 0 => [1,0,0,0,0,0,0]
  | m+1 => cyclicConvolution (coefficientPower m) baseCoefficients

def closedCanonical (m : Nat) : List Int :=
  let c := (coefficientPower m).map (fun x => 2*x)
  c.map (fun x => x-c.getD 6 0)

theorem first_closed_anchor : closedCanonical 1 = [0,0,4,2,2,4,0] := by native_decide
theorem trace1 : canonical 1 = closedCanonical 1 := by native_decide
theorem trace2 : canonical 2 = closedCanonical 2 := by native_decide
theorem trace3 : canonical 3 = closedCanonical 3 := by native_decide
theorem trace4 : canonical 4 = closedCanonical 4 := by native_decide
#print axioms first_closed_anchor
#print axioms trace1
#print axioms trace2
#print axioms trace3
#print axioms trace4
end Bgs.MagneticTraceSmall
