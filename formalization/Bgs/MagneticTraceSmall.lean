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
    let x : Int := k
    let pos : Int := if (s.u*x+s.v)%7=x ∧ (s.l*x+s.d)%7=t then 1 else 0
    let neg : Int := if (-s.u*x+s.v)%7=x ∧ (-s.l*x+s.d)%7=t then 1 else 0
    acc+pos-neg) 0

def histogram (m : Nat) : List Int :=
  (List.range 7).map (fun t => (states m).foldl (fun a s => a+coefficient s t) 0)

def canonical (m : Nat) : List Int :=
  let c := histogram m
  c.map (fun a => a-c.getD 6 0)

theorem trace1 : canonical 1 = [0,-2,-2,-2,-2,-2,0] := by native_decide
theorem trace2 : canonical 2 = [52,-10,-4,-4,-4,-10,0] := by native_decide
theorem trace3 : canonical 3 = [-60,-60,-156,-48,-156,-60,0] := by native_decide
theorem trace4 : canonical 4 = [2416,-676,-76,-220,-76,-676,0] := by native_decide
end Bgs.MagneticTraceSmall
