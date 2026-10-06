import Std
/- Finite executable GF(5) certificate, coefficient arrays in ascending order.
   No abstract polynomial/Rabin-correctness theorem or commutant theorem is claimed. -/
namespace SevenPrimary
abbrev Poly := Array Nat

def trim (a : Poly) : Poly := Id.run do
  let mut n := a.size
  for _ in [:a.size] do
    if n > 0 && a[n-1]! == 0 then n := n-1
  return a.extract 0 n

def inv5 (a : Nat) : Nat := (a*a*a)%5

def rem5 (a b : Poly) : Poly := Id.run do
  if b.isEmpty then return a
  let mut r := a
  let d := b.size-1
  let inv := inv5 b[d]!
  for k in [:a.size] do
    let n := a.size-1-k
    if n >= d then
      let c := (r[n]! * inv)%5
      if c != 0 then
        for j in [:b.size] do
          let i := n-d+j
          r := r.set! i ((r[i]! + 5 - (c*b[j]!)%5)%5)
  return trim r

def mul5 (a b : Poly) : Poly := Id.run do
  if a.isEmpty || b.isEmpty then return #[]
  let mut r := Array.replicate (a.size+b.size-1) 0
  for i in [:a.size] do
    for j in [:b.size] do
      r := r.set! (i+j) ((r[i+j]!+a[i]!*b[j]!)%5)
  return trim r

def gcd5 (a b : Poly) : Poly := Id.run do
  let mut u := a
  let mut v := b
  for _ in [:a.size+b.size+1] do
    if !v.isEmpty then
      let r := rem5 u v
      u := v
      v := r
  if !v.isEmpty then return #[] -- exhaustion is a failed certificate
  let c := inv5 u[u.size-1]!
  return u.map (fun x => (c*x)%5)

def frob5 (a f : Poly) : Poly := Id.run do
  if a.isEmpty then return #[]
  let mut wide := Array.replicate (5*(a.size-1)+1) 0
  for i in [:a.size] do wide := wide.set! (5*i) a[i]!
  return rem5 wide f

def subX (a : Poly) : Poly := Id.run do
  let mut r := a
  for _ in [:2-a.size] do r := r.push 0
  r := r.set! 1 ((r[1]!+4)%5)
  return trim r

def primeTrial (p : Nat) : Bool :=
  p >= 2 && (List.range p).all (fun d => d < 2 || p%d != 0)

def rabinChecks (f : Poly) : Bool := Id.run do
  if f.size < 2 || f[f.size-1]! != 1 || !(f.all (fun c => c < 5)) then return false
  let d := f.size-1
  let x := rem5 #[0,1] f
  let mut h := x
  for k in [1:d+1] do
    h := frob5 h f
    if d%k == 0 && primeTrial (d/k) then
      if gcd5 f (subX h) != #[1] then return false
  return h == x

structure Factor where
  coeffs : Poly
  multiplicity : Nat
  deriving Inhabited
structure Entry where
  polynomial : Poly
  unit : Nat
  factors : Array Factor
  deriving Inhabited

def productCheck (e : Entry) : Bool := Id.run do
  let mut r := #[e.unit]
  for f in e.factors do
    for _ in [:f.multiplicity] do r := mul5 r f.coeffs
  return r == e.polynomial

def factorCheck (e : Entry) : Bool :=
  e.factors.all (fun f => f.multiplicity > 0 && rabinChecks f.coeffs)
def degreeCheck (e : Entry) : Bool :=
  e.factors.all (fun f => (f.coeffs.size-1)%42 != 0)

example : rabinChecks #[0,1] = true := by native_decide
example : rabinChecks #[1,1] = true := by native_decide
example : rabinChecks #[2,1] = true := by native_decide
example : rabinChecks #[3,1] = true := by native_decide
example : rabinChecks #[4,1] = true := by native_decide
example : rabinChecks #[0,0,1] = false := by native_decide
example : rabinChecks #[0,1,1] = false := by native_decide
example : rabinChecks #[0,2,1] = false := by native_decide
example : rabinChecks #[0,3,1] = false := by native_decide
example : rabinChecks #[0,4,1] = false := by native_decide
example : rabinChecks #[1,0,1] = false := by native_decide
example : rabinChecks #[1,1,1] = true := by native_decide
example : rabinChecks #[1,2,1] = false := by native_decide
example : rabinChecks #[1,3,1] = false := by native_decide
example : rabinChecks #[1,4,1] = true := by native_decide
example : rabinChecks #[2,0,1] = true := by native_decide
example : rabinChecks #[2,1,1] = true := by native_decide
example : rabinChecks #[2,2,1] = false := by native_decide
example : rabinChecks #[2,3,1] = false := by native_decide
example : rabinChecks #[2,4,1] = true := by native_decide
example : rabinChecks #[3,0,1] = true := by native_decide
example : rabinChecks #[3,1,1] = false := by native_decide
example : rabinChecks #[3,2,1] = true := by native_decide
example : rabinChecks #[3,3,1] = true := by native_decide
example : rabinChecks #[3,4,1] = false := by native_decide
example : rabinChecks #[4,0,1] = false := by native_decide
example : rabinChecks #[4,1,1] = false := by native_decide
example : rabinChecks #[4,2,1] = true := by native_decide
example : rabinChecks #[4,3,1] = true := by native_decide
example : rabinChecks #[4,4,1] = false := by native_decide
example : rabinChecks #[0,0,0,1] = false := by native_decide
example : rabinChecks #[0,0,1,1] = false := by native_decide
example : rabinChecks #[0,0,2,1] = false := by native_decide
example : rabinChecks #[0,0,3,1] = false := by native_decide
example : rabinChecks #[0,0,4,1] = false := by native_decide
example : rabinChecks #[0,1,0,1] = false := by native_decide
example : rabinChecks #[0,1,1,1] = false := by native_decide
example : rabinChecks #[0,1,2,1] = false := by native_decide
example : rabinChecks #[0,1,3,1] = false := by native_decide
example : rabinChecks #[0,1,4,1] = false := by native_decide
example : rabinChecks #[0,2,0,1] = false := by native_decide
example : rabinChecks #[0,2,1,1] = false := by native_decide
example : rabinChecks #[0,2,2,1] = false := by native_decide
example : rabinChecks #[0,2,3,1] = false := by native_decide
example : rabinChecks #[0,2,4,1] = false := by native_decide
example : rabinChecks #[0,3,0,1] = false := by native_decide
example : rabinChecks #[0,3,1,1] = false := by native_decide
example : rabinChecks #[0,3,2,1] = false := by native_decide
example : rabinChecks #[0,3,3,1] = false := by native_decide
example : rabinChecks #[0,3,4,1] = false := by native_decide
example : rabinChecks #[0,4,0,1] = false := by native_decide
example : rabinChecks #[0,4,1,1] = false := by native_decide
example : rabinChecks #[0,4,2,1] = false := by native_decide
example : rabinChecks #[0,4,3,1] = false := by native_decide
example : rabinChecks #[0,4,4,1] = false := by native_decide
example : rabinChecks #[1,0,0,1] = false := by native_decide
example : rabinChecks #[1,0,1,1] = true := by native_decide
example : rabinChecks #[1,0,2,1] = true := by native_decide
example : rabinChecks #[1,0,3,1] = false := by native_decide
example : rabinChecks #[1,0,4,1] = false := by native_decide
example : rabinChecks #[1,1,0,1] = true := by native_decide
example : rabinChecks #[1,1,1,1] = false := by native_decide
example : rabinChecks #[1,1,2,1] = false := by native_decide
example : rabinChecks #[1,1,3,1] = true := by native_decide
example : rabinChecks #[1,1,4,1] = true := by native_decide
example : rabinChecks #[1,2,0,1] = true := by native_decide
example : rabinChecks #[1,2,1,1] = false := by native_decide
example : rabinChecks #[1,2,2,1] = false := by native_decide
example : rabinChecks #[1,2,3,1] = false := by native_decide
example : rabinChecks #[1,2,4,1] = false := by native_decide
example : rabinChecks #[1,3,0,1] = false := by native_decide
example : rabinChecks #[1,3,1,1] = true := by native_decide
example : rabinChecks #[1,3,2,1] = false := by native_decide
example : rabinChecks #[1,3,3,1] = false := by native_decide
example : rabinChecks #[1,3,4,1] = true := by native_decide
example : rabinChecks #[1,4,0,1] = false := by native_decide
example : rabinChecks #[1,4,1,1] = true := by native_decide
example : rabinChecks #[1,4,2,1] = false := by native_decide
example : rabinChecks #[1,4,3,1] = true := by native_decide
example : rabinChecks #[1,4,4,1] = false := by native_decide
example : rabinChecks #[2,0,0,1] = false := by native_decide
example : rabinChecks #[2,0,1,1] = true := by native_decide
example : rabinChecks #[2,0,2,1] = false := by native_decide
example : rabinChecks #[2,0,3,1] = true := by native_decide
example : rabinChecks #[2,0,4,1] = false := by native_decide
example : rabinChecks #[2,1,0,1] = false := by native_decide
example : rabinChecks #[2,1,1,1] = false := by native_decide
example : rabinChecks #[2,1,2,1] = false := by native_decide
example : rabinChecks #[2,1,3,1] = true := by native_decide
example : rabinChecks #[2,1,4,1] = true := by native_decide
example : rabinChecks #[2,2,0,1] = false := by native_decide
example : rabinChecks #[2,2,1,1] = false := by native_decide
example : rabinChecks #[2,2,2,1] = true := by native_decide
example : rabinChecks #[2,2,3,1] = true := by native_decide
example : rabinChecks #[2,2,4,1] = false := by native_decide
example : rabinChecks #[2,3,0,1] = true := by native_decide
example : rabinChecks #[2,3,1,1] = false := by native_decide
example : rabinChecks #[2,3,2,1] = false := by native_decide
example : rabinChecks #[2,3,3,1] = false := by native_decide
example : rabinChecks #[2,3,4,1] = false := by native_decide
example : rabinChecks #[2,4,0,1] = true := by native_decide
example : rabinChecks #[2,4,1,1] = false := by native_decide
example : rabinChecks #[2,4,2,1] = true := by native_decide
example : rabinChecks #[2,4,3,1] = false := by native_decide
example : rabinChecks #[2,4,4,1] = true := by native_decide
example : rabinChecks #[3,0,0,1] = false := by native_decide
example : rabinChecks #[3,0,1,1] = false := by native_decide
example : rabinChecks #[3,0,2,1] = true := by native_decide
example : rabinChecks #[3,0,3,1] = false := by native_decide
example : rabinChecks #[3,0,4,1] = true := by native_decide
example : rabinChecks #[3,1,0,1] = false := by native_decide
example : rabinChecks #[3,1,1,1] = true := by native_decide
example : rabinChecks #[3,1,2,1] = true := by native_decide
example : rabinChecks #[3,1,3,1] = false := by native_decide
example : rabinChecks #[3,1,4,1] = false := by native_decide
example : rabinChecks #[3,2,0,1] = false := by native_decide
example : rabinChecks #[3,2,1,1] = false := by native_decide
example : rabinChecks #[3,2,2,1] = true := by native_decide
example : rabinChecks #[3,2,3,1] = true := by native_decide
example : rabinChecks #[3,2,4,1] = false := by native_decide
example : rabinChecks #[3,3,0,1] = true := by native_decide
example : rabinChecks #[3,3,1,1] = false := by native_decide
example : rabinChecks #[3,3,2,1] = false := by native_decide
example : rabinChecks #[3,3,3,1] = false := by native_decide
example : rabinChecks #[3,3,4,1] = false := by native_decide
example : rabinChecks #[3,4,0,1] = true := by native_decide
example : rabinChecks #[3,4,1,1] = true := by native_decide
example : rabinChecks #[3,4,2,1] = false := by native_decide
example : rabinChecks #[3,4,3,1] = true := by native_decide
example : rabinChecks #[3,4,4,1] = false := by native_decide
example : rabinChecks #[4,0,0,1] = false := by native_decide
example : rabinChecks #[4,0,1,1] = false := by native_decide
example : rabinChecks #[4,0,2,1] = false := by native_decide
example : rabinChecks #[4,0,3,1] = true := by native_decide
example : rabinChecks #[4,0,4,1] = true := by native_decide
example : rabinChecks #[4,1,0,1] = true := by native_decide
example : rabinChecks #[4,1,1,1] = true := by native_decide
example : rabinChecks #[4,1,2,1] = true := by native_decide
example : rabinChecks #[4,1,3,1] = false := by native_decide
example : rabinChecks #[4,1,4,1] = false := by native_decide
example : rabinChecks #[4,2,0,1] = true := by native_decide
example : rabinChecks #[4,2,1,1] = false := by native_decide
example : rabinChecks #[4,2,2,1] = false := by native_decide
example : rabinChecks #[4,2,3,1] = false := by native_decide
example : rabinChecks #[4,2,4,1] = false := by native_decide
example : rabinChecks #[4,3,0,1] = false := by native_decide
example : rabinChecks #[4,3,1,1] = true := by native_decide
example : rabinChecks #[4,3,2,1] = false := by native_decide
example : rabinChecks #[4,3,3,1] = false := by native_decide
example : rabinChecks #[4,3,4,1] = true := by native_decide
example : rabinChecks #[4,4,0,1] = false := by native_decide
example : rabinChecks #[4,4,1,1] = false := by native_decide
example : rabinChecks #[4,4,2,1] = true := by native_decide
example : rabinChecks #[4,4,3,1] = false := by native_decide
example : rabinChecks #[4,4,4,1] = true := by native_decide
example : rabinChecks #[0,0,0,0,1] = false := by native_decide
example : rabinChecks #[0,0,0,1,1] = false := by native_decide
example : rabinChecks #[0,0,0,2,1] = false := by native_decide
example : rabinChecks #[0,0,0,3,1] = false := by native_decide
example : rabinChecks #[0,0,0,4,1] = false := by native_decide
example : rabinChecks #[0,0,1,0,1] = false := by native_decide
example : rabinChecks #[0,0,1,1,1] = false := by native_decide
example : rabinChecks #[0,0,1,2,1] = false := by native_decide
example : rabinChecks #[0,0,1,3,1] = false := by native_decide
example : rabinChecks #[0,0,1,4,1] = false := by native_decide
example : rabinChecks #[0,0,2,0,1] = false := by native_decide
example : rabinChecks #[0,0,2,1,1] = false := by native_decide
example : rabinChecks #[0,0,2,2,1] = false := by native_decide
example : rabinChecks #[0,0,2,3,1] = false := by native_decide
example : rabinChecks #[0,0,2,4,1] = false := by native_decide
example : rabinChecks #[0,0,3,0,1] = false := by native_decide
example : rabinChecks #[0,0,3,1,1] = false := by native_decide
example : rabinChecks #[0,0,3,2,1] = false := by native_decide
example : rabinChecks #[0,0,3,3,1] = false := by native_decide
example : rabinChecks #[0,0,3,4,1] = false := by native_decide
example : rabinChecks #[0,0,4,0,1] = false := by native_decide
example : rabinChecks #[0,0,4,1,1] = false := by native_decide
example : rabinChecks #[0,0,4,2,1] = false := by native_decide
example : rabinChecks #[0,0,4,3,1] = false := by native_decide
example : rabinChecks #[0,0,4,4,1] = false := by native_decide
example : rabinChecks #[0,1,0,0,1] = false := by native_decide
example : rabinChecks #[0,1,0,1,1] = false := by native_decide
example : rabinChecks #[0,1,0,2,1] = false := by native_decide
example : rabinChecks #[0,1,0,3,1] = false := by native_decide
example : rabinChecks #[0,1,0,4,1] = false := by native_decide
example : rabinChecks #[0,1,1,0,1] = false := by native_decide
example : rabinChecks #[0,1,1,1,1] = false := by native_decide
example : rabinChecks #[0,1,1,2,1] = false := by native_decide
example : rabinChecks #[0,1,1,3,1] = false := by native_decide
example : rabinChecks #[0,1,1,4,1] = false := by native_decide
example : rabinChecks #[0,1,2,0,1] = false := by native_decide
example : rabinChecks #[0,1,2,1,1] = false := by native_decide
example : rabinChecks #[0,1,2,2,1] = false := by native_decide
example : rabinChecks #[0,1,2,3,1] = false := by native_decide
example : rabinChecks #[0,1,2,4,1] = false := by native_decide
example : rabinChecks #[0,1,3,0,1] = false := by native_decide
example : rabinChecks #[0,1,3,1,1] = false := by native_decide
example : rabinChecks #[0,1,3,2,1] = false := by native_decide
example : rabinChecks #[0,1,3,3,1] = false := by native_decide
example : rabinChecks #[0,1,3,4,1] = false := by native_decide
example : rabinChecks #[0,1,4,0,1] = false := by native_decide
example : rabinChecks #[0,1,4,1,1] = false := by native_decide
example : rabinChecks #[0,1,4,2,1] = false := by native_decide
example : rabinChecks #[0,1,4,3,1] = false := by native_decide
example : rabinChecks #[0,1,4,4,1] = false := by native_decide
example : rabinChecks #[0,2,0,0,1] = false := by native_decide
example : rabinChecks #[0,2,0,1,1] = false := by native_decide
example : rabinChecks #[0,2,0,2,1] = false := by native_decide
example : rabinChecks #[0,2,0,3,1] = false := by native_decide
example : rabinChecks #[0,2,0,4,1] = false := by native_decide
example : rabinChecks #[0,2,1,0,1] = false := by native_decide
example : rabinChecks #[0,2,1,1,1] = false := by native_decide
example : rabinChecks #[0,2,1,2,1] = false := by native_decide
example : rabinChecks #[0,2,1,3,1] = false := by native_decide
example : rabinChecks #[0,2,1,4,1] = false := by native_decide
example : rabinChecks #[0,2,2,0,1] = false := by native_decide
example : rabinChecks #[0,2,2,1,1] = false := by native_decide
example : rabinChecks #[0,2,2,2,1] = false := by native_decide
example : rabinChecks #[0,2,2,3,1] = false := by native_decide
example : rabinChecks #[0,2,2,4,1] = false := by native_decide
example : rabinChecks #[0,2,3,0,1] = false := by native_decide
example : rabinChecks #[0,2,3,1,1] = false := by native_decide
example : rabinChecks #[0,2,3,2,1] = false := by native_decide
example : rabinChecks #[0,2,3,3,1] = false := by native_decide
example : rabinChecks #[0,2,3,4,1] = false := by native_decide
example : rabinChecks #[0,2,4,0,1] = false := by native_decide
example : rabinChecks #[0,2,4,1,1] = false := by native_decide
example : rabinChecks #[0,2,4,2,1] = false := by native_decide
example : rabinChecks #[0,2,4,3,1] = false := by native_decide
example : rabinChecks #[0,2,4,4,1] = false := by native_decide
example : rabinChecks #[0,3,0,0,1] = false := by native_decide
example : rabinChecks #[0,3,0,1,1] = false := by native_decide
example : rabinChecks #[0,3,0,2,1] = false := by native_decide
example : rabinChecks #[0,3,0,3,1] = false := by native_decide
example : rabinChecks #[0,3,0,4,1] = false := by native_decide
example : rabinChecks #[0,3,1,0,1] = false := by native_decide
example : rabinChecks #[0,3,1,1,1] = false := by native_decide
example : rabinChecks #[0,3,1,2,1] = false := by native_decide
example : rabinChecks #[0,3,1,3,1] = false := by native_decide
example : rabinChecks #[0,3,1,4,1] = false := by native_decide
example : rabinChecks #[0,3,2,0,1] = false := by native_decide
example : rabinChecks #[0,3,2,1,1] = false := by native_decide
example : rabinChecks #[0,3,2,2,1] = false := by native_decide
example : rabinChecks #[0,3,2,3,1] = false := by native_decide
example : rabinChecks #[0,3,2,4,1] = false := by native_decide
example : rabinChecks #[0,3,3,0,1] = false := by native_decide
example : rabinChecks #[0,3,3,1,1] = false := by native_decide
example : rabinChecks #[0,3,3,2,1] = false := by native_decide
example : rabinChecks #[0,3,3,3,1] = false := by native_decide
example : rabinChecks #[0,3,3,4,1] = false := by native_decide
example : rabinChecks #[0,3,4,0,1] = false := by native_decide
example : rabinChecks #[0,3,4,1,1] = false := by native_decide
example : rabinChecks #[0,3,4,2,1] = false := by native_decide
example : rabinChecks #[0,3,4,3,1] = false := by native_decide
example : rabinChecks #[0,3,4,4,1] = false := by native_decide
example : rabinChecks #[0,4,0,0,1] = false := by native_decide
example : rabinChecks #[0,4,0,1,1] = false := by native_decide
example : rabinChecks #[0,4,0,2,1] = false := by native_decide
example : rabinChecks #[0,4,0,3,1] = false := by native_decide
example : rabinChecks #[0,4,0,4,1] = false := by native_decide
example : rabinChecks #[0,4,1,0,1] = false := by native_decide
example : rabinChecks #[0,4,1,1,1] = false := by native_decide
example : rabinChecks #[0,4,1,2,1] = false := by native_decide
example : rabinChecks #[0,4,1,3,1] = false := by native_decide
example : rabinChecks #[0,4,1,4,1] = false := by native_decide
example : rabinChecks #[0,4,2,0,1] = false := by native_decide
example : rabinChecks #[0,4,2,1,1] = false := by native_decide
example : rabinChecks #[0,4,2,2,1] = false := by native_decide
example : rabinChecks #[0,4,2,3,1] = false := by native_decide
example : rabinChecks #[0,4,2,4,1] = false := by native_decide
example : rabinChecks #[0,4,3,0,1] = false := by native_decide
example : rabinChecks #[0,4,3,1,1] = false := by native_decide
example : rabinChecks #[0,4,3,2,1] = false := by native_decide
example : rabinChecks #[0,4,3,3,1] = false := by native_decide
example : rabinChecks #[0,4,3,4,1] = false := by native_decide
example : rabinChecks #[0,4,4,0,1] = false := by native_decide
example : rabinChecks #[0,4,4,1,1] = false := by native_decide
example : rabinChecks #[0,4,4,2,1] = false := by native_decide
example : rabinChecks #[0,4,4,3,1] = false := by native_decide
example : rabinChecks #[0,4,4,4,1] = false := by native_decide
example : rabinChecks #[1,0,0,0,1] = false := by native_decide
example : rabinChecks #[1,0,0,1,1] = false := by native_decide
example : rabinChecks #[1,0,0,2,1] = false := by native_decide
example : rabinChecks #[1,0,0,3,1] = false := by native_decide
example : rabinChecks #[1,0,0,4,1] = false := by native_decide
example : rabinChecks #[1,0,1,0,1] = false := by native_decide
example : rabinChecks #[1,0,1,1,1] = true := by native_decide
example : rabinChecks #[1,0,1,2,1] = false := by native_decide
example : rabinChecks #[1,0,1,3,1] = false := by native_decide
example : rabinChecks #[1,0,1,4,1] = true := by native_decide
example : rabinChecks #[1,0,2,0,1] = false := by native_decide
example : rabinChecks #[1,0,2,1,1] = false := by native_decide
example : rabinChecks #[1,0,2,2,1] = true := by native_decide
example : rabinChecks #[1,0,2,3,1] = true := by native_decide
example : rabinChecks #[1,0,2,4,1] = false := by native_decide
example : rabinChecks #[1,0,3,0,1] = false := by native_decide
example : rabinChecks #[1,0,3,1,1] = true := by native_decide
example : rabinChecks #[1,0,3,2,1] = false := by native_decide
example : rabinChecks #[1,0,3,3,1] = false := by native_decide
example : rabinChecks #[1,0,3,4,1] = true := by native_decide
example : rabinChecks #[1,0,4,0,1] = false := by native_decide
example : rabinChecks #[1,0,4,1,1] = false := by native_decide
example : rabinChecks #[1,0,4,2,1] = true := by native_decide
example : rabinChecks #[1,0,4,3,1] = true := by native_decide
example : rabinChecks #[1,0,4,4,1] = false := by native_decide
example : rabinChecks #[1,1,0,0,1] = false := by native_decide
example : rabinChecks #[1,1,0,1,1] = false := by native_decide
example : rabinChecks #[1,1,0,2,1] = false := by native_decide
example : rabinChecks #[1,1,0,3,1] = false := by native_decide
example : rabinChecks #[1,1,0,4,1] = true := by native_decide
example : rabinChecks #[1,1,1,0,1] = true := by native_decide
example : rabinChecks #[1,1,1,1,1] = false := by native_decide
example : rabinChecks #[1,1,1,2,1] = false := by native_decide
example : rabinChecks #[1,1,1,3,1] = false := by native_decide
example : rabinChecks #[1,1,1,4,1] = false := by native_decide
example : rabinChecks #[1,1,2,0,1] = false := by native_decide
example : rabinChecks #[1,1,2,1,1] = false := by native_decide
example : rabinChecks #[1,1,2,2,1] = true := by native_decide
example : rabinChecks #[1,1,2,3,1] = false := by native_decide
example : rabinChecks #[1,1,2,4,1] = false := by native_decide
example : rabinChecks #[1,1,3,0,1] = true := by native_decide
example : rabinChecks #[1,1,3,1,1] = false := by native_decide
example : rabinChecks #[1,1,3,2,1] = true := by native_decide
example : rabinChecks #[1,1,3,3,1] = false := by native_decide
example : rabinChecks #[1,1,3,4,1] = false := by native_decide
example : rabinChecks #[1,1,4,0,1] = false := by native_decide
example : rabinChecks #[1,1,4,1,1] = true := by native_decide
example : rabinChecks #[1,1,4,2,1] = false := by native_decide
example : rabinChecks #[1,1,4,3,1] = false := by native_decide
example : rabinChecks #[1,1,4,4,1] = true := by native_decide
example : rabinChecks #[1,2,0,0,1] = false := by native_decide
example : rabinChecks #[1,2,0,1,1] = false := by native_decide
example : rabinChecks #[1,2,0,2,1] = true := by native_decide
example : rabinChecks #[1,2,0,3,1] = false := by native_decide
example : rabinChecks #[1,2,0,4,1] = false := by native_decide
example : rabinChecks #[1,2,1,0,1] = false := by native_decide
example : rabinChecks #[1,2,1,1,1] = false := by native_decide
example : rabinChecks #[1,2,1,2,1] = true := by native_decide
example : rabinChecks #[1,2,1,3,1] = true := by native_decide
example : rabinChecks #[1,2,1,4,1] = false := by native_decide
example : rabinChecks #[1,2,2,0,1] = true := by native_decide
example : rabinChecks #[1,2,2,1,1] = true := by native_decide
example : rabinChecks #[1,2,2,2,1] = false := by native_decide
example : rabinChecks #[1,2,2,3,1] = false := by native_decide
example : rabinChecks #[1,2,2,4,1] = false := by native_decide
example : rabinChecks #[1,2,3,0,1] = false := by native_decide
example : rabinChecks #[1,2,3,1,1] = true := by native_decide
example : rabinChecks #[1,2,3,2,1] = false := by native_decide
example : rabinChecks #[1,2,3,3,1] = false := by native_decide
example : rabinChecks #[1,2,3,4,1] = false := by native_decide
example : rabinChecks #[1,2,4,0,1] = true := by native_decide
example : rabinChecks #[1,2,4,1,1] = false := by native_decide
example : rabinChecks #[1,2,4,2,1] = false := by native_decide
example : rabinChecks #[1,2,4,3,1] = false := by native_decide
example : rabinChecks #[1,2,4,4,1] = false := by native_decide
example : rabinChecks #[1,3,0,0,1] = false := by native_decide
example : rabinChecks #[1,3,0,1,1] = false := by native_decide
example : rabinChecks #[1,3,0,2,1] = false := by native_decide
example : rabinChecks #[1,3,0,3,1] = true := by native_decide
example : rabinChecks #[1,3,0,4,1] = false := by native_decide
example : rabinChecks #[1,3,1,0,1] = false := by native_decide
example : rabinChecks #[1,3,1,1,1] = false := by native_decide
example : rabinChecks #[1,3,1,2,1] = true := by native_decide
example : rabinChecks #[1,3,1,3,1] = true := by native_decide
example : rabinChecks #[1,3,1,4,1] = false := by native_decide
example : rabinChecks #[1,3,2,0,1] = true := by native_decide
example : rabinChecks #[1,3,2,1,1] = false := by native_decide
example : rabinChecks #[1,3,2,2,1] = false := by native_decide
example : rabinChecks #[1,3,2,3,1] = false := by native_decide
example : rabinChecks #[1,3,2,4,1] = true := by native_decide
example : rabinChecks #[1,3,3,0,1] = false := by native_decide
example : rabinChecks #[1,3,3,1,1] = false := by native_decide
example : rabinChecks #[1,3,3,2,1] = false := by native_decide
example : rabinChecks #[1,3,3,3,1] = false := by native_decide
example : rabinChecks #[1,3,3,4,1] = true := by native_decide
example : rabinChecks #[1,3,4,0,1] = true := by native_decide
example : rabinChecks #[1,3,4,1,1] = false := by native_decide
example : rabinChecks #[1,3,4,2,1] = false := by native_decide
example : rabinChecks #[1,3,4,3,1] = false := by native_decide
example : rabinChecks #[1,3,4,4,1] = false := by native_decide
example : rabinChecks #[1,4,0,0,1] = false := by native_decide
example : rabinChecks #[1,4,0,1,1] = true := by native_decide
example : rabinChecks #[1,4,0,2,1] = false := by native_decide
example : rabinChecks #[1,4,0,3,1] = false := by native_decide
example : rabinChecks #[1,4,0,4,1] = false := by native_decide
example : rabinChecks #[1,4,1,0,1] = true := by native_decide
example : rabinChecks #[1,4,1,1,1] = false := by native_decide
example : rabinChecks #[1,4,1,2,1] = false := by native_decide
example : rabinChecks #[1,4,1,3,1] = false := by native_decide
example : rabinChecks #[1,4,1,4,1] = false := by native_decide
example : rabinChecks #[1,4,2,0,1] = false := by native_decide
example : rabinChecks #[1,4,2,1,1] = false := by native_decide
example : rabinChecks #[1,4,2,2,1] = false := by native_decide
example : rabinChecks #[1,4,2,3,1] = true := by native_decide
example : rabinChecks #[1,4,2,4,1] = false := by native_decide
example : rabinChecks #[1,4,3,0,1] = true := by native_decide
example : rabinChecks #[1,4,3,1,1] = false := by native_decide
example : rabinChecks #[1,4,3,2,1] = false := by native_decide
example : rabinChecks #[1,4,3,3,1] = true := by native_decide
example : rabinChecks #[1,4,3,4,1] = false := by native_decide
example : rabinChecks #[1,4,4,0,1] = false := by native_decide
example : rabinChecks #[1,4,4,1,1] = true := by native_decide
example : rabinChecks #[1,4,4,2,1] = false := by native_decide
example : rabinChecks #[1,4,4,3,1] = false := by native_decide
example : rabinChecks #[1,4,4,4,1] = true := by native_decide
example : rabinChecks #[2,0,0,0,1] = true := by native_decide
example : rabinChecks #[2,0,0,1,1] = false := by native_decide
example : rabinChecks #[2,0,0,2,1] = false := by native_decide
example : rabinChecks #[2,0,0,3,1] = false := by native_decide
example : rabinChecks #[2,0,0,4,1] = false := by native_decide
example : rabinChecks #[2,0,1,0,1] = true := by native_decide
example : rabinChecks #[2,0,1,1,1] = false := by native_decide
example : rabinChecks #[2,0,1,2,1] = true := by native_decide
example : rabinChecks #[2,0,1,3,1] = true := by native_decide
example : rabinChecks #[2,0,1,4,1] = false := by native_decide
example : rabinChecks #[2,0,2,0,1] = false := by native_decide
example : rabinChecks #[2,0,2,1,1] = true := by native_decide
example : rabinChecks #[2,0,2,2,1] = false := by native_decide
example : rabinChecks #[2,0,2,3,1] = false := by native_decide
example : rabinChecks #[2,0,2,4,1] = true := by native_decide
example : rabinChecks #[2,0,3,0,1] = false := by native_decide
example : rabinChecks #[2,0,3,1,1] = false := by native_decide
example : rabinChecks #[2,0,3,2,1] = true := by native_decide
example : rabinChecks #[2,0,3,3,1] = true := by native_decide
example : rabinChecks #[2,0,3,4,1] = false := by native_decide
example : rabinChecks #[2,0,4,0,1] = true := by native_decide
example : rabinChecks #[2,0,4,1,1] = true := by native_decide
example : rabinChecks #[2,0,4,2,1] = false := by native_decide
example : rabinChecks #[2,0,4,3,1] = false := by native_decide
example : rabinChecks #[2,0,4,4,1] = true := by native_decide
example : rabinChecks #[2,1,0,0,1] = false := by native_decide
example : rabinChecks #[2,1,0,1,1] = false := by native_decide
example : rabinChecks #[2,1,0,2,1] = false := by native_decide
example : rabinChecks #[2,1,0,3,1] = true := by native_decide
example : rabinChecks #[2,1,0,4,1] = true := by native_decide
example : rabinChecks #[2,1,1,0,1] = false := by native_decide
example : rabinChecks #[2,1,1,1,1] = false := by native_decide
example : rabinChecks #[2,1,1,2,1] = false := by native_decide
example : rabinChecks #[2,1,1,3,1] = false := by native_decide
example : rabinChecks #[2,1,1,4,1] = true := by native_decide
example : rabinChecks #[2,1,2,0,1] = false := by native_decide
example : rabinChecks #[2,1,2,1,1] = true := by native_decide
example : rabinChecks #[2,1,2,2,1] = false := by native_decide
example : rabinChecks #[2,1,2,3,1] = false := by native_decide
example : rabinChecks #[2,1,2,4,1] = false := by native_decide
example : rabinChecks #[2,1,3,0,1] = false := by native_decide
example : rabinChecks #[2,1,3,1,1] = false := by native_decide
example : rabinChecks #[2,1,3,2,1] = true := by native_decide
example : rabinChecks #[2,1,3,3,1] = false := by native_decide
example : rabinChecks #[2,1,3,4,1] = true := by native_decide
example : rabinChecks #[2,1,4,0,1] = true := by native_decide
example : rabinChecks #[2,1,4,1,1] = false := by native_decide
example : rabinChecks #[2,1,4,2,1] = false := by native_decide
example : rabinChecks #[2,1,4,3,1] = false := by native_decide
example : rabinChecks #[2,1,4,4,1] = false := by native_decide
example : rabinChecks #[2,2,0,0,1] = false := by native_decide
example : rabinChecks #[2,2,0,1,1] = false := by native_decide
example : rabinChecks #[2,2,0,2,1] = true := by native_decide
example : rabinChecks #[2,2,0,3,1] = false := by native_decide
example : rabinChecks #[2,2,0,4,1] = true := by native_decide
example : rabinChecks #[2,2,1,0,1] = true := by native_decide
example : rabinChecks #[2,2,1,1,1] = false := by native_decide
example : rabinChecks #[2,2,1,2,1] = false := by native_decide
example : rabinChecks #[2,2,1,3,1] = false := by native_decide
example : rabinChecks #[2,2,1,4,1] = false := by native_decide
example : rabinChecks #[2,2,2,0,1] = false := by native_decide
example : rabinChecks #[2,2,2,1,1] = true := by native_decide
example : rabinChecks #[2,2,2,2,1] = true := by native_decide
example : rabinChecks #[2,2,2,3,1] = false := by native_decide
example : rabinChecks #[2,2,2,4,1] = false := by native_decide
example : rabinChecks #[2,2,3,0,1] = false := by native_decide
example : rabinChecks #[2,2,3,1,1] = false := by native_decide
example : rabinChecks #[2,2,3,2,1] = false := by native_decide
example : rabinChecks #[2,2,3,3,1] = true := by native_decide
example : rabinChecks #[2,2,3,4,1] = false := by native_decide
example : rabinChecks #[2,2,4,0,1] = false := by native_decide
example : rabinChecks #[2,2,4,1,1] = false := by native_decide
example : rabinChecks #[2,2,4,2,1] = true := by native_decide
example : rabinChecks #[2,2,4,3,1] = false := by native_decide
example : rabinChecks #[2,2,4,4,1] = false := by native_decide
example : rabinChecks #[2,3,0,0,1] = false := by native_decide
example : rabinChecks #[2,3,0,1,1] = true := by native_decide
example : rabinChecks #[2,3,0,2,1] = false := by native_decide
example : rabinChecks #[2,3,0,3,1] = true := by native_decide
example : rabinChecks #[2,3,0,4,1] = false := by native_decide
example : rabinChecks #[2,3,1,0,1] = true := by native_decide
example : rabinChecks #[2,3,1,1,1] = false := by native_decide
example : rabinChecks #[2,3,1,2,1] = false := by native_decide
example : rabinChecks #[2,3,1,3,1] = false := by native_decide
example : rabinChecks #[2,3,1,4,1] = false := by native_decide
example : rabinChecks #[2,3,2,0,1] = false := by native_decide
example : rabinChecks #[2,3,2,1,1] = false := by native_decide
example : rabinChecks #[2,3,2,2,1] = false := by native_decide
example : rabinChecks #[2,3,2,3,1] = true := by native_decide
example : rabinChecks #[2,3,2,4,1] = true := by native_decide
example : rabinChecks #[2,3,3,0,1] = false := by native_decide
example : rabinChecks #[2,3,3,1,1] = false := by native_decide
example : rabinChecks #[2,3,3,2,1] = true := by native_decide
example : rabinChecks #[2,3,3,3,1] = false := by native_decide
example : rabinChecks #[2,3,3,4,1] = false := by native_decide
example : rabinChecks #[2,3,4,0,1] = false := by native_decide
example : rabinChecks #[2,3,4,1,1] = false := by native_decide
example : rabinChecks #[2,3,4,2,1] = false := by native_decide
example : rabinChecks #[2,3,4,3,1] = true := by native_decide
example : rabinChecks #[2,3,4,4,1] = false := by native_decide
example : rabinChecks #[2,4,0,0,1] = false := by native_decide
example : rabinChecks #[2,4,0,1,1] = true := by native_decide
example : rabinChecks #[2,4,0,2,1] = true := by native_decide
example : rabinChecks #[2,4,0,3,1] = false := by native_decide
example : rabinChecks #[2,4,0,4,1] = false := by native_decide
example : rabinChecks #[2,4,1,0,1] = false := by native_decide
example : rabinChecks #[2,4,1,1,1] = true := by native_decide
example : rabinChecks #[2,4,1,2,1] = false := by native_decide
example : rabinChecks #[2,4,1,3,1] = false := by native_decide
example : rabinChecks #[2,4,1,4,1] = false := by native_decide
example : rabinChecks #[2,4,2,0,1] = false := by native_decide
example : rabinChecks #[2,4,2,1,1] = false := by native_decide
example : rabinChecks #[2,4,2,2,1] = false := by native_decide
example : rabinChecks #[2,4,2,3,1] = false := by native_decide
example : rabinChecks #[2,4,2,4,1] = true := by native_decide
example : rabinChecks #[2,4,3,0,1] = false := by native_decide
example : rabinChecks #[2,4,3,1,1] = true := by native_decide
example : rabinChecks #[2,4,3,2,1] = false := by native_decide
example : rabinChecks #[2,4,3,3,1] = true := by native_decide
example : rabinChecks #[2,4,3,4,1] = false := by native_decide
example : rabinChecks #[2,4,4,0,1] = true := by native_decide
example : rabinChecks #[2,4,4,1,1] = false := by native_decide
example : rabinChecks #[2,4,4,2,1] = false := by native_decide
example : rabinChecks #[2,4,4,3,1] = false := by native_decide
example : rabinChecks #[2,4,4,4,1] = false := by native_decide
example : rabinChecks #[3,0,0,0,1] = true := by native_decide
example : rabinChecks #[3,0,0,1,1] = false := by native_decide
example : rabinChecks #[3,0,0,2,1] = false := by native_decide
example : rabinChecks #[3,0,0,3,1] = false := by native_decide
example : rabinChecks #[3,0,0,4,1] = false := by native_decide
example : rabinChecks #[3,0,1,0,1] = false := by native_decide
example : rabinChecks #[3,0,1,1,1] = false := by native_decide
example : rabinChecks #[3,0,1,2,1] = false := by native_decide
example : rabinChecks #[3,0,1,3,1] = false := by native_decide
example : rabinChecks #[3,0,1,4,1] = false := by native_decide
example : rabinChecks #[3,0,2,0,1] = true := by native_decide
example : rabinChecks #[3,0,2,1,1] = false := by native_decide
example : rabinChecks #[3,0,2,2,1] = true := by native_decide
example : rabinChecks #[3,0,2,3,1] = true := by native_decide
example : rabinChecks #[3,0,2,4,1] = false := by native_decide
example : rabinChecks #[3,0,3,0,1] = true := by native_decide
example : rabinChecks #[3,0,3,1,1] = true := by native_decide
example : rabinChecks #[3,0,3,2,1] = false := by native_decide
example : rabinChecks #[3,0,3,3,1] = false := by native_decide
example : rabinChecks #[3,0,3,4,1] = true := by native_decide
example : rabinChecks #[3,0,4,0,1] = false := by native_decide
example : rabinChecks #[3,0,4,1,1] = false := by native_decide
example : rabinChecks #[3,0,4,2,1] = false := by native_decide
example : rabinChecks #[3,0,4,3,1] = false := by native_decide
example : rabinChecks #[3,0,4,4,1] = false := by native_decide
example : rabinChecks #[3,1,0,0,1] = false := by native_decide
example : rabinChecks #[3,1,0,1,1] = true := by native_decide
example : rabinChecks #[3,1,0,2,1] = true := by native_decide
example : rabinChecks #[3,1,0,3,1] = false := by native_decide
example : rabinChecks #[3,1,0,4,1] = false := by native_decide
example : rabinChecks #[3,1,1,0,1] = false := by native_decide
example : rabinChecks #[3,1,1,1,1] = true := by native_decide
example : rabinChecks #[3,1,1,2,1] = false := by native_decide
example : rabinChecks #[3,1,1,3,1] = false := by native_decide
example : rabinChecks #[3,1,1,4,1] = false := by native_decide
example : rabinChecks #[3,1,2,0,1] = false := by native_decide
example : rabinChecks #[3,1,2,1,1] = true := by native_decide
example : rabinChecks #[3,1,2,2,1] = false := by native_decide
example : rabinChecks #[3,1,2,3,1] = false := by native_decide
example : rabinChecks #[3,1,2,4,1] = false := by native_decide
example : rabinChecks #[3,1,3,0,1] = true := by native_decide
example : rabinChecks #[3,1,3,1,1] = false := by native_decide
example : rabinChecks #[3,1,3,2,1] = false := by native_decide
example : rabinChecks #[3,1,3,3,1] = false := by native_decide
example : rabinChecks #[3,1,3,4,1] = false := by native_decide
example : rabinChecks #[3,1,4,0,1] = true := by native_decide
example : rabinChecks #[3,1,4,1,1] = false := by native_decide
example : rabinChecks #[3,1,4,2,1] = false := by native_decide
example : rabinChecks #[3,1,4,3,1] = true := by native_decide
example : rabinChecks #[3,1,4,4,1] = true := by native_decide
example : rabinChecks #[3,2,0,0,1] = false := by native_decide
example : rabinChecks #[3,2,0,1,1] = true := by native_decide
example : rabinChecks #[3,2,0,2,1] = false := by native_decide
example : rabinChecks #[3,2,0,3,1] = true := by native_decide
example : rabinChecks #[3,2,0,4,1] = false := by native_decide
example : rabinChecks #[3,2,1,0,1] = true := by native_decide
example : rabinChecks #[3,2,1,1,1] = false := by native_decide
example : rabinChecks #[3,2,1,2,1] = true := by native_decide
example : rabinChecks #[3,2,1,3,1] = false := by native_decide
example : rabinChecks #[3,2,1,4,1] = true := by native_decide
example : rabinChecks #[3,2,2,0,1] = true := by native_decide
example : rabinChecks #[3,2,2,1,1] = false := by native_decide
example : rabinChecks #[3,2,2,2,1] = false := by native_decide
example : rabinChecks #[3,2,2,3,1] = false := by native_decide
example : rabinChecks #[3,2,2,4,1] = false := by native_decide
example : rabinChecks #[3,2,3,0,1] = false := by native_decide
example : rabinChecks #[3,2,3,1,1] = false := by native_decide
example : rabinChecks #[3,2,3,2,1] = false := by native_decide
example : rabinChecks #[3,2,3,3,1] = true := by native_decide
example : rabinChecks #[3,2,3,4,1] = false := by native_decide
example : rabinChecks #[3,2,4,0,1] = false := by native_decide
example : rabinChecks #[3,2,4,1,1] = false := by native_decide
example : rabinChecks #[3,2,4,2,1] = false := by native_decide
example : rabinChecks #[3,2,4,3,1] = true := by native_decide
example : rabinChecks #[3,2,4,4,1] = false := by native_decide
example : rabinChecks #[3,3,0,0,1] = false := by native_decide
example : rabinChecks #[3,3,0,1,1] = false := by native_decide
example : rabinChecks #[3,3,0,2,1] = true := by native_decide
example : rabinChecks #[3,3,0,3,1] = false := by native_decide
example : rabinChecks #[3,3,0,4,1] = true := by native_decide
example : rabinChecks #[3,3,1,0,1] = true := by native_decide
example : rabinChecks #[3,3,1,1,1] = true := by native_decide
example : rabinChecks #[3,3,1,2,1] = false := by native_decide
example : rabinChecks #[3,3,1,3,1] = true := by native_decide
example : rabinChecks #[3,3,1,4,1] = false := by native_decide
example : rabinChecks #[3,3,2,0,1] = true := by native_decide
example : rabinChecks #[3,3,2,1,1] = false := by native_decide
example : rabinChecks #[3,3,2,2,1] = false := by native_decide
example : rabinChecks #[3,3,2,3,1] = false := by native_decide
example : rabinChecks #[3,3,2,4,1] = false := by native_decide
example : rabinChecks #[3,3,3,0,1] = false := by native_decide
example : rabinChecks #[3,3,3,1,1] = false := by native_decide
example : rabinChecks #[3,3,3,2,1] = true := by native_decide
example : rabinChecks #[3,3,3,3,1] = false := by native_decide
example : rabinChecks #[3,3,3,4,1] = false := by native_decide
example : rabinChecks #[3,3,4,0,1] = false := by native_decide
example : rabinChecks #[3,3,4,1,1] = false := by native_decide
example : rabinChecks #[3,3,4,2,1] = true := by native_decide
example : rabinChecks #[3,3,4,3,1] = false := by native_decide
example : rabinChecks #[3,3,4,4,1] = false := by native_decide
example : rabinChecks #[3,4,0,0,1] = false := by native_decide
example : rabinChecks #[3,4,0,1,1] = false := by native_decide
example : rabinChecks #[3,4,0,2,1] = false := by native_decide
example : rabinChecks #[3,4,0,3,1] = true := by native_decide
example : rabinChecks #[3,4,0,4,1] = true := by native_decide
example : rabinChecks #[3,4,1,0,1] = false := by native_decide
example : rabinChecks #[3,4,1,1,1] = false := by native_decide
example : rabinChecks #[3,4,1,2,1] = false := by native_decide
example : rabinChecks #[3,4,1,3,1] = false := by native_decide
example : rabinChecks #[3,4,1,4,1] = true := by native_decide
example : rabinChecks #[3,4,2,0,1] = false := by native_decide
example : rabinChecks #[3,4,2,1,1] = false := by native_decide
example : rabinChecks #[3,4,2,2,1] = false := by native_decide
example : rabinChecks #[3,4,2,3,1] = false := by native_decide
example : rabinChecks #[3,4,2,4,1] = true := by native_decide
example : rabinChecks #[3,4,3,0,1] = true := by native_decide
example : rabinChecks #[3,4,3,1,1] = false := by native_decide
example : rabinChecks #[3,4,3,2,1] = false := by native_decide
example : rabinChecks #[3,4,3,3,1] = false := by native_decide
example : rabinChecks #[3,4,3,4,1] = false := by native_decide
example : rabinChecks #[3,4,4,0,1] = true := by native_decide
example : rabinChecks #[3,4,4,1,1] = true := by native_decide
example : rabinChecks #[3,4,4,2,1] = true := by native_decide
example : rabinChecks #[3,4,4,3,1] = false := by native_decide
example : rabinChecks #[3,4,4,4,1] = false := by native_decide
example : rabinChecks #[4,0,0,0,1] = false := by native_decide
example : rabinChecks #[4,0,0,1,1] = true := by native_decide
example : rabinChecks #[4,0,0,2,1] = true := by native_decide
example : rabinChecks #[4,0,0,3,1] = true := by native_decide
example : rabinChecks #[4,0,0,4,1] = true := by native_decide
example : rabinChecks #[4,0,1,0,1] = false := by native_decide
example : rabinChecks #[4,0,1,1,1] = false := by native_decide
example : rabinChecks #[4,0,1,2,1] = false := by native_decide
example : rabinChecks #[4,0,1,3,1] = false := by native_decide
example : rabinChecks #[4,0,1,4,1] = false := by native_decide
example : rabinChecks #[4,0,2,0,1] = false := by native_decide
example : rabinChecks #[4,0,2,1,1] = false := by native_decide
example : rabinChecks #[4,0,2,2,1] = false := by native_decide
example : rabinChecks #[4,0,2,3,1] = false := by native_decide
example : rabinChecks #[4,0,2,4,1] = false := by native_decide
example : rabinChecks #[4,0,3,0,1] = false := by native_decide
example : rabinChecks #[4,0,3,1,1] = false := by native_decide
example : rabinChecks #[4,0,3,2,1] = false := by native_decide
example : rabinChecks #[4,0,3,3,1] = false := by native_decide
example : rabinChecks #[4,0,3,4,1] = false := by native_decide
example : rabinChecks #[4,0,4,0,1] = false := by native_decide
example : rabinChecks #[4,0,4,1,1] = false := by native_decide
example : rabinChecks #[4,0,4,2,1] = false := by native_decide
example : rabinChecks #[4,0,4,3,1] = false := by native_decide
example : rabinChecks #[4,0,4,4,1] = false := by native_decide
example : rabinChecks #[4,1,0,0,1] = true := by native_decide
example : rabinChecks #[4,1,0,1,1] = false := by native_decide
example : rabinChecks #[4,1,0,2,1] = true := by native_decide
example : rabinChecks #[4,1,0,3,1] = false := by native_decide
example : rabinChecks #[4,1,0,4,1] = false := by native_decide
example : rabinChecks #[4,1,1,0,1] = false := by native_decide
example : rabinChecks #[4,1,1,1,1] = true := by native_decide
example : rabinChecks #[4,1,1,2,1] = false := by native_decide
example : rabinChecks #[4,1,1,3,1] = false := by native_decide
example : rabinChecks #[4,1,1,4,1] = false := by native_decide
example : rabinChecks #[4,1,2,0,1] = false := by native_decide
example : rabinChecks #[4,1,2,1,1] = false := by native_decide
example : rabinChecks #[4,1,2,2,1] = false := by native_decide
example : rabinChecks #[4,1,2,3,1] = false := by native_decide
example : rabinChecks #[4,1,2,4,1] = true := by native_decide
example : rabinChecks #[4,1,3,0,1] = false := by native_decide
example : rabinChecks #[4,1,3,1,1] = false := by native_decide
example : rabinChecks #[4,1,3,2,1] = false := by native_decide
example : rabinChecks #[4,1,3,3,1] = true := by native_decide
example : rabinChecks #[4,1,3,4,1] = true := by native_decide
example : rabinChecks #[4,1,4,0,1] = false := by native_decide
example : rabinChecks #[4,1,4,1,1] = true := by native_decide
example : rabinChecks #[4,1,4,2,1] = true := by native_decide
example : rabinChecks #[4,1,4,3,1] = false := by native_decide
example : rabinChecks #[4,1,4,4,1] = false := by native_decide
example : rabinChecks #[4,2,0,0,1] = true := by native_decide
example : rabinChecks #[4,2,0,1,1] = true := by native_decide
example : rabinChecks #[4,2,0,2,1] = false := by native_decide
example : rabinChecks #[4,2,0,3,1] = false := by native_decide
example : rabinChecks #[4,2,0,4,1] = false := by native_decide
example : rabinChecks #[4,2,1,0,1] = false := by native_decide
example : rabinChecks #[4,2,1,1,1] = true := by native_decide
example : rabinChecks #[4,2,1,2,1] = false := by native_decide
example : rabinChecks #[4,2,1,3,1] = true := by native_decide
example : rabinChecks #[4,2,1,4,1] = false := by native_decide
example : rabinChecks #[4,2,2,0,1] = false := by native_decide
example : rabinChecks #[4,2,2,1,1] = false := by native_decide
example : rabinChecks #[4,2,2,2,1] = true := by native_decide
example : rabinChecks #[4,2,2,3,1] = false := by native_decide
example : rabinChecks #[4,2,2,4,1] = true := by native_decide
example : rabinChecks #[4,2,3,0,1] = false := by native_decide
example : rabinChecks #[4,2,3,1,1] = false := by native_decide
example : rabinChecks #[4,2,3,2,1] = true := by native_decide
example : rabinChecks #[4,2,3,3,1] = false := by native_decide
example : rabinChecks #[4,2,3,4,1] = false := by native_decide
example : rabinChecks #[4,2,4,0,1] = false := by native_decide
example : rabinChecks #[4,2,4,1,1] = false := by native_decide
example : rabinChecks #[4,2,4,2,1] = false := by native_decide
example : rabinChecks #[4,2,4,3,1] = true := by native_decide
example : rabinChecks #[4,2,4,4,1] = false := by native_decide
example : rabinChecks #[4,3,0,0,1] = true := by native_decide
example : rabinChecks #[4,3,0,1,1] = false := by native_decide
example : rabinChecks #[4,3,0,2,1] = false := by native_decide
example : rabinChecks #[4,3,0,3,1] = false := by native_decide
example : rabinChecks #[4,3,0,4,1] = true := by native_decide
example : rabinChecks #[4,3,1,0,1] = false := by native_decide
example : rabinChecks #[4,3,1,1,1] = false := by native_decide
example : rabinChecks #[4,3,1,2,1] = true := by native_decide
example : rabinChecks #[4,3,1,3,1] = false := by native_decide
example : rabinChecks #[4,3,1,4,1] = true := by native_decide
example : rabinChecks #[4,3,2,0,1] = false := by native_decide
example : rabinChecks #[4,3,2,1,1] = true := by native_decide
example : rabinChecks #[4,3,2,2,1] = false := by native_decide
example : rabinChecks #[4,3,2,3,1] = true := by native_decide
example : rabinChecks #[4,3,2,4,1] = false := by native_decide
example : rabinChecks #[4,3,3,0,1] = false := by native_decide
example : rabinChecks #[4,3,3,1,1] = false := by native_decide
example : rabinChecks #[4,3,3,2,1] = false := by native_decide
example : rabinChecks #[4,3,3,3,1] = true := by native_decide
example : rabinChecks #[4,3,3,4,1] = false := by native_decide
example : rabinChecks #[4,3,4,0,1] = false := by native_decide
example : rabinChecks #[4,3,4,1,1] = false := by native_decide
example : rabinChecks #[4,3,4,2,1] = true := by native_decide
example : rabinChecks #[4,3,4,3,1] = false := by native_decide
example : rabinChecks #[4,3,4,4,1] = false := by native_decide
example : rabinChecks #[4,4,0,0,1] = true := by native_decide
example : rabinChecks #[4,4,0,1,1] = false := by native_decide
example : rabinChecks #[4,4,0,2,1] = false := by native_decide
example : rabinChecks #[4,4,0,3,1] = true := by native_decide
example : rabinChecks #[4,4,0,4,1] = false := by native_decide
example : rabinChecks #[4,4,1,0,1] = false := by native_decide
example : rabinChecks #[4,4,1,1,1] = false := by native_decide
example : rabinChecks #[4,4,1,2,1] = false := by native_decide
example : rabinChecks #[4,4,1,3,1] = false := by native_decide
example : rabinChecks #[4,4,1,4,1] = true := by native_decide
example : rabinChecks #[4,4,2,0,1] = false := by native_decide
example : rabinChecks #[4,4,2,1,1] = true := by native_decide
example : rabinChecks #[4,4,2,2,1] = false := by native_decide
example : rabinChecks #[4,4,2,3,1] = false := by native_decide
example : rabinChecks #[4,4,2,4,1] = false := by native_decide
example : rabinChecks #[4,4,3,0,1] = false := by native_decide
example : rabinChecks #[4,4,3,1,1] = true := by native_decide
example : rabinChecks #[4,4,3,2,1] = true := by native_decide
example : rabinChecks #[4,4,3,3,1] = false := by native_decide
example : rabinChecks #[4,4,3,4,1] = false := by native_decide
example : rabinChecks #[4,4,4,0,1] = false := by native_decide
example : rabinChecks #[4,4,4,1,1] = false := by native_decide
example : rabinChecks #[4,4,4,2,1] = false := by native_decide
example : rabinChecks #[4,4,4,3,1] = true := by native_decide
example : rabinChecks #[4,4,4,4,1] = true := by native_decide
example : mul5 #[3,2,0,3,4,2,1] #[0,3,4,4,0,3] = #[0,4,3,0,2,3,0,2,1,1,1,3] := by native_decide
example : rem5 #[3,2,0,3,4,2,1] #[0,3,4,4,0,3] = #[3,0,3,4,1] := by native_decide
example : gcd5 #[3,2,0,3,4,2,1] #[0,3,4,4,0,3] = #[1] := by native_decide
example : frob5 #[3,2,0,3,4,2,1] #[0,3,4,4,0,3] = #[3,1,0,2,2] := by native_decide
example : subX #[3,2,0,3,4,2,1] = #[3,1,0,3,4,2,1] := by native_decide
example : mul5 #[3,2,3,2,1,4,1,2,1] #[1,2] = #[3,3,2,3,0,1,4,4,0,2] := by native_decide
example : rem5 #[3,2,3,2,1,4,1,2,1] #[1,2] = #[] := by native_decide
example : gcd5 #[3,2,3,2,1,4,1,2,1] #[1,2] = #[3,1] := by native_decide
example : frob5 #[3,2,3,2,1,4,1,2,1] #[1,2] = #[] := by native_decide
example : subX #[3,2,3,2,1,4,1,2,1] = #[3,1,3,2,1,4,1,2,1] := by native_decide
example : mul5 #[1,1,1,4,2,2,4] #[2,4] = #[2,1,1,2,0,2,1,1] := by native_decide
example : rem5 #[1,1,1,4,2,2,4] #[2,4] = #[1] := by native_decide
example : gcd5 #[1,1,1,4,2,2,4] #[2,4] = #[1] := by native_decide
example : frob5 #[1,1,1,4,2,2,4] #[2,4] = #[1] := by native_decide
example : subX #[1,1,1,4,2,2,4] = #[1,0,1,4,2,2,4] := by native_decide
example : mul5 #[1,0,4,0,1,4,0,4,2] #[2,4,4,2,4,4,1,2,3] = #[2,4,2,3,2,4,2,4,4,2,0,1,0,4,0,1,1] := by native_decide
example : rem5 #[1,0,4,0,1,4,0,4,2] #[2,4,4,2,4,4,1,2,3] = #[3,4,3,2,0,3,1,1] := by native_decide
example : gcd5 #[1,0,4,0,1,4,0,4,2] #[2,4,4,2,4,4,1,2,3] = #[1] := by native_decide
example : frob5 #[1,0,4,0,1,4,0,4,2] #[2,4,4,2,4,4,1,2,3] = #[3,2,4,4,2,2,3,2] := by native_decide
example : subX #[1,0,4,0,1,4,0,4,2] = #[1,4,4,0,1,4,0,4,2] := by native_decide
example : mul5 #[2,4,0,1,1] #[4,0,0,4,4,4] = #[3,1,0,2,3,4,0,3,3,4] := by native_decide
example : rem5 #[2,4,0,1,1] #[4,0,0,4,4,4] = #[2,4,0,1,1] := by native_decide
example : gcd5 #[2,4,0,1,1] #[4,0,0,4,4,4] = #[1] := by native_decide
example : frob5 #[2,4,0,1,1] #[4,0,0,4,4,4] = #[3,3,4,3,2] := by native_decide
example : subX #[2,4,0,1,1] = #[2,3,0,1,1] := by native_decide
example : mul5 #[4,4,1,0,2] #[2] = #[3,3,2,0,4] := by native_decide
example : rem5 #[4,4,1,0,2] #[2] = #[] := by native_decide
example : gcd5 #[4,4,1,0,2] #[2] = #[1] := by native_decide
example : frob5 #[4,4,1,0,2] #[2] = #[] := by native_decide
example : subX #[4,4,1,0,2] = #[4,3,1,0,2] := by native_decide
example : mul5 #[3,2,4,2,0,1,4,4,4] #[3,1] = #[4,4,4,0,2,3,3,1,1,4] := by native_decide
example : rem5 #[3,2,4,2,0,1,4,4,4] #[3,1] = #[3] := by native_decide
example : gcd5 #[3,2,4,2,0,1,4,4,4] #[3,1] = #[1] := by native_decide
example : frob5 #[3,2,4,2,0,1,4,4,4] #[3,1] = #[3] := by native_decide
example : subX #[3,2,4,2,0,1,4,4,4] = #[3,1,4,2,0,1,4,4,4] := by native_decide
example : mul5 #[4,0,3] #[1,2,4] = #[4,3,4,1,2] := by native_decide
example : rem5 #[4,0,3] #[1,2,4] = #[2,1] := by native_decide
example : gcd5 #[4,0,3] #[1,2,4] = #[1] := by native_decide
example : frob5 #[4,0,3] #[1,2,4] = #[4,4] := by native_decide
example : subX #[4,0,3] = #[4,4,3] := by native_decide
example : mul5 #[1,4,0,4,2] #[2,4,4,0,3,3,3] = #[2,2,0,4,3,4,3,4,3,3,1] := by native_decide
example : rem5 #[1,4,0,4,2] #[2,4,4,0,3,3,3] = #[1,4,0,4,2] := by native_decide
example : gcd5 #[1,4,0,4,2] #[2,4,4,0,3,3,3] = #[1,1] := by native_decide
example : frob5 #[1,4,0,4,2] #[2,4,4,0,3,3,3] = #[3,4,4,1,4,1] := by native_decide
example : subX #[1,4,0,4,2] = #[1,3,0,4,2] := by native_decide
example : mul5 #[0,1,1,2,2,2,1] #[3,4,4,3,4,0,3,2,2] = #[0,3,2,4,1,4,4,4,3,1,1,4,1,1,2] := by native_decide
example : rem5 #[0,1,1,2,2,2,1] #[3,4,4,3,4,0,3,2,2] = #[0,1,1,2,2,2,1] := by native_decide
example : gcd5 #[0,1,1,2,2,2,1] #[3,4,4,3,4,0,3,2,2] = #[1] := by native_decide
example : frob5 #[0,1,1,2,2,2,1] #[3,4,4,3,4,0,3,2,2] = #[2,1,4,2,4,3,2,1] := by native_decide
example : subX #[0,1,1,2,2,2,1] = #[0,0,1,2,2,2,1] := by native_decide
example : mul5 #[1,3,0,4,2,0,3] #[3,2,2] = #[3,1,3,3,4,2,3,1,1] := by native_decide
example : rem5 #[1,3,0,4,2,0,3] #[3,2,2] = #[1,1] := by native_decide
example : gcd5 #[1,3,0,4,2,0,3] #[3,2,2] = #[1] := by native_decide
example : frob5 #[1,3,0,4,2,0,3] #[3,2,2] = #[3] := by native_decide
example : subX #[1,3,0,4,2,0,3] = #[1,2,0,4,2,0,3] := by native_decide
example : mul5 #[0,2,2,1,3,3] #[0,1] = #[0,0,2,2,1,3,3] := by native_decide
example : rem5 #[0,2,2,1,3,3] #[0,1] = #[] := by native_decide
example : gcd5 #[0,2,2,1,3,3] #[0,1] = #[0,1] := by native_decide
example : frob5 #[0,2,2,1,3,3] #[0,1] = #[] := by native_decide
example : subX #[0,2,2,1,3,3] = #[0,1,2,1,3,3] := by native_decide
example : mul5 #[4,2,1,1,2,4,1] #[2,2] = #[3,2,1,4,1,2,0,2] := by native_decide
example : rem5 #[4,2,1,1,2,4,1] #[2,2] = #[1] := by native_decide
example : gcd5 #[4,2,1,1,2,4,1] #[2,2] = #[1] := by native_decide
example : frob5 #[4,2,1,1,2,4,1] #[2,2] = #[1] := by native_decide
example : subX #[4,2,1,1,2,4,1] = #[4,1,1,1,2,4,1] := by native_decide
example : mul5 #[1,0,1,1,2,0,1] #[3,4,3,4,3,2,4] = #[3,4,1,1,1,2,0,2,0,2,1,2,4] := by native_decide
example : rem5 #[1,0,1,1,2,0,1] #[3,4,3,4,3,2,4] = #[4,4,4,0,0,2] := by native_decide
example : gcd5 #[1,0,1,1,2,0,1] #[3,4,3,4,3,2,4] = #[1] := by native_decide
example : frob5 #[1,0,1,1,2,0,1] #[3,4,3,4,3,2,4] = #[1,1,4,1,3,1] := by native_decide
example : subX #[1,0,1,1,2,0,1] = #[1,4,1,1,2,0,1] := by native_decide
example : mul5 #[2,3] #[1] = #[2,3] := by native_decide
example : rem5 #[2,3] #[1] = #[] := by native_decide
example : gcd5 #[2,3] #[1] = #[1] := by native_decide
example : frob5 #[2,3] #[1] = #[] := by native_decide
example : subX #[2,3] = #[2,2] := by native_decide
example : mul5 #[4,4] #[4,2,2] = #[1,4,1,3] := by native_decide
example : rem5 #[4,4] #[4,2,2] = #[4,4] := by native_decide
example : gcd5 #[4,4] #[4,2,2] = #[1] := by native_decide
example : frob5 #[4,4] #[4,2,2] = #[0,1] := by native_decide
example : subX #[4,4] = #[4,3] := by native_decide
example : mul5 #[1,1,0,0,4,0,2,3,0,1] #[1,0,4,1,0,3] = #[1,1,4,0,0,3,1,2,3,2,3,0,0,0,3] := by native_decide
example : rem5 #[1,1,0,0,4,0,2,3,0,1] #[1,0,4,1,0,3] = #[0,3,4,2,1] := by native_decide
example : gcd5 #[1,1,0,0,4,0,2,3,0,1] #[1,0,4,1,0,3] = #[1] := by native_decide
example : frob5 #[1,1,0,0,4,0,2,3,0,1] #[1,0,4,1,0,3] = #[1,0,3,1] := by native_decide
example : subX #[1,1,0,0,4,0,2,3,0,1] = #[1,0,0,0,4,0,2,3,0,1] := by native_decide
example : mul5 #[3,3,0,3,3,4,1,2,4,1,1,4] #[2,0,3,0,0,4] = #[1,1,4,0,1,4,3,1,3,0,0,0,1,3,4,4,1] := by native_decide
example : rem5 #[3,3,0,3,3,4,1,2,4,1,1,4] #[2,0,3,0,0,4] = #[1,2,2,1] := by native_decide
example : gcd5 #[3,3,0,3,3,4,1,2,4,1,1,4] #[2,0,3,0,0,4] = #[1] := by native_decide
example : frob5 #[3,3,0,3,3,4,1,2,4,1,1,4] #[2,0,3,0,0,4] = #[1,4,1,1,2] := by native_decide
example : subX #[3,3,0,3,3,4,1,2,4,1,1,4] = #[3,2,0,3,3,4,1,2,4,1,1,4] := by native_decide
example : mul5 #[4,1,4,1,4,2] #[1,1,0,2,1] = #[4,0,0,3,1,0,3,4,3,2] := by native_decide
example : rem5 #[4,1,4,1,4,2] #[1,1,0,2,1] = #[4,4,2,1] := by native_decide
example : gcd5 #[4,1,4,1,4,2] #[1,1,0,2,1] = #[1] := by native_decide
example : frob5 #[4,1,4,1,4,2] #[1,1,0,2,1] = #[1,4,1] := by native_decide
example : subX #[4,1,4,1,4,2] = #[4,0,4,1,4,2] := by native_decide
example : mul5 #[1,1,0,4,3,4,1,2,1,1] #[1,2,0,0,4,4,2,1,3] = #[1,3,2,4,0,3,0,3,2,2,2,0,2,0,1,4,4,3] := by native_decide
example : rem5 #[1,1,0,4,3,4,1,2,1,1] #[1,2,0,0,4,4,2,1,3] = #[3,3,1,4,1,4,2] := by native_decide
example : gcd5 #[1,1,0,4,3,4,1,2,1,1] #[1,2,0,0,4,4,2,1,3] = #[1] := by native_decide
example : frob5 #[1,1,0,4,3,4,1,2,1,1] #[1,2,0,0,4,4,2,1,3] = #[4,1,3,0,3,0,4,3] := by native_decide
example : subX #[1,1,0,4,3,4,1,2,1,1] = #[1,0,0,4,3,4,1,2,1,1] := by native_decide
example : mul5 #[0,3,0,1,2,2,1,0,0,4,2,4,3] #[0,3,2] = #[0,0,4,1,3,3,0,2,2,0,2,4,1,2,1] := by native_decide
example : rem5 #[0,3,0,1,2,2,1,0,0,4,2,4,3] #[0,3,2] = #[0,2] := by native_decide
example : gcd5 #[0,3,0,1,2,2,1,0,0,4,2,4,3] #[0,3,2] = #[0,1] := by native_decide
example : frob5 #[0,3,0,1,2,2,1,0,0,4,2,4,3] #[0,3,2] = #[0,2] := by native_decide
example : subX #[0,3,0,1,2,2,1,0,0,4,2,4,3] = #[0,2,0,1,2,2,1,0,0,4,2,4,3] := by native_decide
example : mul5 #[3,1,2,0,2,3,4] #[4] = #[2,4,3,0,3,2,1] := by native_decide
example : rem5 #[3,1,2,0,2,3,4] #[4] = #[] := by native_decide
example : gcd5 #[3,1,2,0,2,3,4] #[4] = #[1] := by native_decide
example : frob5 #[3,1,2,0,2,3,4] #[4] = #[] := by native_decide
example : subX #[3,1,2,0,2,3,4] = #[3,0,2,0,2,3,4] := by native_decide
example : mul5 #[1,3,2,2,4,4,1] #[1] = #[1,3,2,2,4,4,1] := by native_decide
example : rem5 #[1,3,2,2,4,4,1] #[1] = #[] := by native_decide
example : gcd5 #[1,3,2,2,4,4,1] #[1] = #[1] := by native_decide
example : frob5 #[1,3,2,2,4,4,1] #[1] = #[] := by native_decide
example : subX #[1,3,2,2,4,4,1] = #[1,2,2,2,4,4,1] := by native_decide
example : mul5 #[3,2,3,1,1] #[4,4,2,3,3,3,2] = #[2,0,1,4,4,0,1,4,2,0,2] := by native_decide
example : rem5 #[3,2,3,1,1] #[4,4,2,3,3,3,2] = #[3,2,3,1,1] := by native_decide
example : gcd5 #[3,2,3,1,1] #[4,4,2,3,3,3,2] = #[1] := by native_decide
example : frob5 #[3,2,3,1,1] #[4,4,2,3,3,3,2] = #[2,0,3,4,2] := by native_decide
example : subX #[3,2,3,1,1] = #[3,1,3,1,1] := by native_decide
example : mul5 #[2,4,1,0,1,4,1,1] #[1,2,3] = #[2,3,0,4,4,1,2,0,0,3] := by native_decide
example : rem5 #[2,4,1,0,1,4,1,1] #[1,2,3] = #[3] := by native_decide
example : gcd5 #[2,4,1,0,1,4,1,1] #[1,2,3] = #[1] := by native_decide
example : frob5 #[2,4,1,0,1,4,1,1] #[1,2,3] = #[3] := by native_decide
example : subX #[2,4,1,0,1,4,1,1] = #[2,3,1,0,1,4,1,1] := by native_decide
example : mul5 #[3,3,2,3,0,2,1,4,2] #[0,1] = #[0,3,3,2,3,0,2,1,4,2] := by native_decide
example : rem5 #[3,3,2,3,0,2,1,4,2] #[0,1] = #[3] := by native_decide
example : gcd5 #[3,3,2,3,0,2,1,4,2] #[0,1] = #[1] := by native_decide
example : frob5 #[3,3,2,3,0,2,1,4,2] #[0,1] = #[3] := by native_decide
example : subX #[3,3,2,3,0,2,1,4,2] = #[3,2,2,3,0,2,1,4,2] := by native_decide
example : mul5 #[1,4,3,1,1,3,0,3,3] #[3,1,1,1,1,0,4] = #[3,3,4,1,2,3,2,0,3,3,0,3,3,2,2] := by native_decide
example : rem5 #[1,4,3,1,1,3,0,3,3] #[3,1,1,1,1,0,4] = #[0,1,3,0,0,4] := by native_decide
example : gcd5 #[1,4,3,1,1,3,0,3,3] #[3,1,1,1,1,0,4] = #[1] := by native_decide
example : frob5 #[1,4,3,1,1,3,0,3,3] #[3,1,1,1,1,0,4] = #[0,1,0,2] := by native_decide
example : subX #[1,4,3,1,1,3,0,3,3] = #[1,3,3,1,1,3,0,3,3] := by native_decide
example : mul5 #[0,3,4,1] #[2,3] = #[0,1,2,4,3] := by native_decide
example : rem5 #[0,3,4,1] #[2,3] = #[3] := by native_decide
example : gcd5 #[0,3,4,1] #[2,3] = #[1] := by native_decide
example : frob5 #[0,3,4,1] #[2,3] = #[3] := by native_decide
example : subX #[0,3,4,1] = #[0,2,4,1] := by native_decide
example : mul5 #[] #[4,4,3,1,1,0,4,2,2] = #[] := by native_decide
example : rem5 #[] #[4,4,3,1,1,0,4,2,2] = #[] := by native_decide
example : gcd5 #[] #[4,4,3,1,1,0,4,2,2] = #[2,2,4,3,3,0,2,1,1] := by native_decide
example : frob5 #[] #[4,4,3,1,1,0,4,2,2] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[0,4,4,3,4,4,3,0,0,3,2,3,4] #[2] = #[0,3,3,1,3,3,1,0,0,1,4,1,3] := by native_decide
example : rem5 #[0,4,4,3,4,4,3,0,0,3,2,3,4] #[2] = #[] := by native_decide
example : gcd5 #[0,4,4,3,4,4,3,0,0,3,2,3,4] #[2] = #[1] := by native_decide
example : frob5 #[0,4,4,3,4,4,3,0,0,3,2,3,4] #[2] = #[] := by native_decide
example : subX #[0,4,4,3,4,4,3,0,0,3,2,3,4] = #[0,3,4,3,4,4,3,0,0,3,2,3,4] := by native_decide
example : mul5 #[2,2,3,2,2,1,4,4,3,1] #[2,0,4,3] = #[4,4,4,3,2,4,2,3,0,0,4,3,3] := by native_decide
example : rem5 #[2,2,3,2,2,1,4,4,3,1] #[2,0,4,3] = #[2,2] := by native_decide
example : gcd5 #[2,2,3,2,2,1,4,4,3,1] #[2,0,4,3] = #[1] := by native_decide
example : frob5 #[2,2,3,2,2,1,4,4,3,1] #[2,0,4,3] = #[0,4,3] := by native_decide
example : subX #[2,2,3,2,2,1,4,4,3,1] = #[2,1,3,2,2,1,4,4,3,1] := by native_decide
example : mul5 #[3] #[2,2,1,1,3,1,1] = #[1,1,3,3,4,3,3] := by native_decide
example : rem5 #[3] #[2,2,1,1,3,1,1] = #[3] := by native_decide
example : gcd5 #[3] #[2,2,1,1,3,1,1] = #[1] := by native_decide
example : frob5 #[3] #[2,2,1,1,3,1,1] = #[3] := by native_decide
example : subX #[3] = #[3,4] := by native_decide
example : mul5 #[0,3,4,0,1,2,2,0,2,4] #[4,4] = #[0,2,3,1,4,2,1,3,3,4,1] := by native_decide
example : rem5 #[0,3,4,0,1,2,2,0,2,4] #[4,4] = #[] := by native_decide
example : gcd5 #[0,3,4,0,1,2,2,0,2,4] #[4,4] = #[1,1] := by native_decide
example : frob5 #[0,3,4,0,1,2,2,0,2,4] #[4,4] = #[] := by native_decide
example : subX #[0,3,4,0,1,2,2,0,2,4] = #[0,2,4,0,1,2,2,0,2,4] := by native_decide
example : mul5 #[1,3,0,3,3,1,1,1,2] #[4,4,1,2,3,4,2,1] = #[4,1,3,2,3,2,1,1,4,2,0,1,3,1,0,2] := by native_decide
example : rem5 #[1,3,0,3,3,1,1,1,2] #[4,4,1,2,3,4,2,1] = #[3,2,0,2,3,2,4] := by native_decide
example : gcd5 #[1,3,0,3,3,1,1,1,2] #[4,4,1,2,3,4,2,1] = #[1] := by native_decide
example : frob5 #[1,3,0,3,3,1,1,1,2] #[4,4,1,2,3,4,2,1] = #[3,3,1,0,2,2,4] := by native_decide
example : subX #[1,3,0,3,3,1,1,1,2] = #[1,2,0,3,3,1,1,1,2] := by native_decide
example : mul5 #[2,1,0,4,0,3,3,4,2,4] #[3,0,4,2,2,3,3,1] = #[1,3,3,0,1,3,1,2,2,2,0,1,1,4,2,4,4] := by native_decide
example : rem5 #[2,1,0,4,0,3,3,4,2,4] #[3,0,4,2,2,3,3,1] = #[1,1,0,0,0,4,4] := by native_decide
example : gcd5 #[2,1,0,4,0,3,3,4,2,4] #[3,0,4,2,2,3,3,1] = #[1] := by native_decide
example : frob5 #[2,1,0,4,0,3,3,4,2,4] #[3,0,4,2,2,3,3,1] = #[3,1,0,3,2,0,2] := by native_decide
example : subX #[2,1,0,4,0,3,3,4,2,4] = #[2,0,0,4,0,3,3,4,2,4] := by native_decide
example : mul5 #[4,0,2,0,3,0,4,4,4,0,2] #[2,3,3,1] = #[3,2,1,0,2,1,2,3,2,3,0,0,1,2] := by native_decide
example : rem5 #[4,0,2,0,3,0,4,4,4,0,2] #[2,3,3,1] = #[2,3] := by native_decide
example : gcd5 #[4,0,2,0,3,0,4,4,4,0,2] #[2,3,3,1] = #[1] := by native_decide
example : frob5 #[4,0,2,0,3,0,4,4,4,0,2] #[2,3,3,1] = #[1,4,2] := by native_decide
example : subX #[4,0,2,0,3,0,4,4,4,0,2] = #[4,4,2,0,3,0,4,4,4,0,2] := by native_decide
example : mul5 #[1,3,2,0,0,1] #[2,4,3,3] = #[2,0,4,0,0,3,4,3,3] := by native_decide
example : rem5 #[1,3,2,0,0,1] #[2,4,3,3] = #[4,3,3] := by native_decide
example : gcd5 #[1,3,2,0,0,1] #[2,4,3,3] = #[1] := by native_decide
example : frob5 #[1,3,2,0,0,1] #[2,4,3,3] = #[2,2] := by native_decide
example : subX #[1,3,2,0,0,1] = #[1,2,2,0,0,1] := by native_decide
example : mul5 #[3,2,4,2,1,2,1] #[1,4,4,3] = #[3,4,4,0,1,1,4,0,0,3] := by native_decide
example : rem5 #[3,2,4,2,1,2,1] #[1,4,4,3] = #[3,0,3] := by native_decide
example : gcd5 #[3,2,4,2,1,2,1] #[1,4,4,3] = #[2,1] := by native_decide
example : frob5 #[3,2,4,2,1,2,1] #[1,4,4,3] = #[4,4,1] := by native_decide
example : subX #[3,2,4,2,1,2,1] = #[3,1,4,2,1,2,1] := by native_decide
example : mul5 #[2,2,2,0,2,1,2] #[3] = #[1,1,1,0,1,3,1] := by native_decide
example : rem5 #[2,2,2,0,2,1,2] #[3] = #[] := by native_decide
example : gcd5 #[2,2,2,0,2,1,2] #[3] = #[1] := by native_decide
example : frob5 #[2,2,2,0,2,1,2] #[3] = #[] := by native_decide
example : subX #[2,2,2,0,2,1,2] = #[2,1,2,0,2,1,2] := by native_decide
example : mul5 #[2,4,3,1,2,3,2,3,2,0,4,4,4] #[0,1,1,0,2,4,0,1] = #[0,2,1,2,3,4,2,1,2,2,4,0,2,3,0,1,4,0,4,4] := by native_decide
example : rem5 #[2,4,3,1,2,3,2,3,2,0,4,4,4] #[0,1,1,0,2,4,0,1] = #[2,0,2,3,0,1,4] := by native_decide
example : gcd5 #[2,4,3,1,2,3,2,3,2,0,4,4,4] #[0,1,1,0,2,4,0,1] = #[1] := by native_decide
example : frob5 #[2,4,3,1,2,3,2,3,2,0,4,4,4] #[0,1,1,0,2,4,0,1] = #[2,4,0,1,1,1,4] := by native_decide
example : subX #[2,4,3,1,2,3,2,3,2,0,4,4,4] = #[2,3,3,1,2,3,2,3,2,0,4,4,4] := by native_decide
example : mul5 #[2,1,2,1,0,0,2,0,1,2,3,4] #[3,2,4,4,3,1,4,3] = #[1,2,1,4,0,2,0,4,3,1,1,2,4,1,1,1,2,0,2] := by native_decide
example : rem5 #[2,1,2,1,0,0,2,0,1,2,3,4] #[3,2,4,4,3,1,4,3] = #[3,3,1,3,4,3] := by native_decide
example : gcd5 #[2,1,2,1,0,0,2,0,1,2,3,4] #[3,2,4,4,3,1,4,3] = #[1] := by native_decide
example : frob5 #[2,1,2,1,0,0,2,0,1,2,3,4] #[3,2,4,4,3,1,4,3] = #[0,2,2,1,2,4,3] := by native_decide
example : subX #[2,1,2,1,0,0,2,0,1,2,3,4] = #[2,0,2,1,0,0,2,0,1,2,3,4] := by native_decide
example : mul5 #[] #[2,3] = #[] := by native_decide
example : rem5 #[] #[2,3] = #[] := by native_decide
example : gcd5 #[] #[2,3] = #[4,1] := by native_decide
example : frob5 #[] #[2,3] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[0,2,1,4,3] #[3,1,4] = #[0,1,0,1,2,4,2] := by native_decide
example : rem5 #[0,2,1,4,3] #[3,1,4] = #[1] := by native_decide
example : gcd5 #[0,2,1,4,3] #[3,1,4] = #[1] := by native_decide
example : frob5 #[0,2,1,4,3] #[3,1,4] = #[1] := by native_decide
example : subX #[0,2,1,4,3] = #[0,1,1,4,3] := by native_decide
example : mul5 #[4,0,2,2,2,0,4] #[1,2,1,2,4] = #[4,3,1,4,4,0,3,0,2,3,1] := by native_decide
example : rem5 #[4,0,2,2,2,0,4] #[1,2,1,2,4] = #[1,2,4,2] := by native_decide
example : gcd5 #[4,0,2,2,2,0,4] #[1,2,1,2,4] = #[1] := by native_decide
example : frob5 #[4,0,2,2,2,0,4] #[1,2,1,2,4] = #[3,3,4,4] := by native_decide
example : subX #[4,0,2,2,2,0,4] = #[4,4,2,2,2,0,4] := by native_decide
example : mul5 #[3,4,2,1,1,3,2,2,0,0,1,1,2] #[1,2,3,1,1,4,1,0,2] = #[3,0,4,0,1,1,3,4,1,4,2,3,4,1,2,1,2,4,4,2,4] := by native_decide
example : rem5 #[3,4,2,1,1,3,2,2,0,0,1,1,2] #[1,2,3,1,1,4,1,0,2] = #[2,3,1,0,4,4,4,4] := by native_decide
example : gcd5 #[3,4,2,1,1,3,2,2,0,0,1,1,2] #[1,2,3,1,1,4,1,0,2] = #[4,4,1] := by native_decide
example : frob5 #[3,4,2,1,1,3,2,2,0,0,1,1,2] #[1,2,3,1,1,4,1,0,2] = #[2,3,3,2,1,2,4] := by native_decide
example : subX #[3,4,2,1,1,3,2,2,0,0,1,1,2] = #[3,3,2,1,1,3,2,2,0,0,1,1,2] := by native_decide
example : mul5 #[3] #[2,2,3,0,3,3,4] = #[1,1,4,0,4,4,2] := by native_decide
example : rem5 #[3] #[2,2,3,0,3,3,4] = #[3] := by native_decide
example : gcd5 #[3] #[2,2,3,0,3,3,4] = #[1] := by native_decide
example : frob5 #[3] #[2,2,3,0,3,3,4] = #[3] := by native_decide
example : subX #[3] = #[3,4] := by native_decide
example : mul5 #[4,0,4] #[0,4,2,0,4,0,2,4] = #[0,1,3,1,4,0,4,1,3,1] := by native_decide
example : rem5 #[4,0,4] #[0,4,2,0,4,0,2,4] = #[4,0,4] := by native_decide
example : gcd5 #[4,0,4] #[0,4,2,0,4,0,2,4] = #[1,0,1] := by native_decide
example : frob5 #[4,0,4] #[0,4,2,0,4,0,2,4] = #[4,2,0,4,4,2,3] := by native_decide
example : subX #[4,0,4] = #[4,4,4] := by native_decide
example : mul5 #[] #[0,4,0,0,3,0,2] = #[] := by native_decide
example : rem5 #[] #[0,4,0,0,3,0,2] = #[] := by native_decide
example : gcd5 #[] #[0,4,0,0,3,0,2] = #[0,2,0,0,4,0,1] := by native_decide
example : frob5 #[] #[0,4,0,0,3,0,2] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[3,2] #[2,1,3,2,1,0,0,4,3] = #[1,2,1,2,2,2,0,2,2,1] := by native_decide
example : rem5 #[3,2] #[2,1,3,2,1,0,0,4,3] = #[3,2] := by native_decide
example : gcd5 #[3,2] #[2,1,3,2,1,0,0,4,3] = #[1] := by native_decide
example : frob5 #[3,2] #[2,1,3,2,1,0,0,4,3] = #[3,0,0,0,0,2] := by native_decide
example : subX #[3,2] = #[3,1] := by native_decide
example : mul5 #[2,1,4] #[1,0,3,0,3,4] = #[2,1,0,3,3,1,1,1] := by native_decide
example : rem5 #[2,1,4] #[1,0,3,0,3,4] = #[2,1,4] := by native_decide
example : gcd5 #[2,1,4] #[1,0,3,0,3,4] = #[1] := by native_decide
example : frob5 #[2,1,4] #[1,0,3,0,3,4] = #[3,1,3,4] := by native_decide
example : subX #[2,1,4] = #[2,0,4] := by native_decide
example : mul5 #[] #[3,0,1,2,0,3,1] = #[] := by native_decide
example : rem5 #[] #[3,0,1,2,0,3,1] = #[] := by native_decide
example : gcd5 #[] #[3,0,1,2,0,3,1] = #[3,0,1,2,0,3,1] := by native_decide
example : frob5 #[] #[3,0,1,2,0,3,1] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[2,1,3,4,1,1,4,1,2,4] #[1,4,3,2,2] = #[2,4,3,3,2,0,0,0,2,0,2,3,2,3] := by native_decide
example : rem5 #[2,1,3,4,1,1,4,1,2,4] #[1,4,3,2,2] = #[1,3,3] := by native_decide
example : gcd5 #[2,1,3,4,1,1,4,1,2,4] #[1,4,3,2,2] = #[1] := by native_decide
example : frob5 #[2,1,3,4,1,1,4,1,2,4] #[1,4,3,2,2] = #[2,3,0,3] := by native_decide
example : subX #[2,1,3,4,1,1,4,1,2,4] = #[2,0,3,4,1,1,4,1,2,4] := by native_decide
example : mul5 #[4,1,3,0,3,1,1] #[3,1] = #[2,2,0,3,4,1,4,1] := by native_decide
example : rem5 #[4,1,3,0,3,1,1] #[3,1] = #[2] := by native_decide
example : gcd5 #[4,1,3,0,3,1,1] #[3,1] = #[1] := by native_decide
example : frob5 #[4,1,3,0,3,1,1] #[3,1] = #[2] := by native_decide
example : subX #[4,1,3,0,3,1,1] = #[4,0,3,0,3,1,1] := by native_decide
example : mul5 #[2,0,0,1,0,2,1,2,1] #[3,2,1] = #[1,4,2,3,2,2,2,0,3,4,1] := by native_decide
example : rem5 #[2,0,0,1,0,2,1,2,1] #[3,2,1] = #[3,4] := by native_decide
example : gcd5 #[2,0,0,1,0,2,1,2,1] #[3,2,1] = #[1] := by native_decide
example : frob5 #[2,0,0,1,0,2,1,2,1] #[3,2,1] = #[0,1] := by native_decide
example : subX #[2,0,0,1,0,2,1,2,1] = #[2,4,0,1,0,2,1,2,1] := by native_decide
example : mul5 #[3,1,1,3,4,2,2,3,4,3,0,4] #[4,0,3,1,1] = #[2,4,3,3,3,4,4,0,3,0,2,2,2,0,4,4] := by native_decide
example : rem5 #[3,1,1,3,4,2,2,3,4,3,0,4] #[4,0,3,1,1] = #[1,1,1,1] := by native_decide
example : gcd5 #[3,1,1,3,4,2,2,3,4,3,0,4] #[4,0,3,1,1] = #[3,1] := by native_decide
example : frob5 #[3,1,1,3,4,2,2,3,4,3,0,4] #[4,0,3,1,1] = #[4,2,0,4] := by native_decide
example : subX #[3,1,1,3,4,2,2,3,4,3,0,4] = #[3,0,1,3,4,2,2,3,4,3,0,4] := by native_decide
example : mul5 #[1,4,2,3,1,3,3,3] #[1,1,0,2] = #[1,0,1,2,2,3,2,3,4,1,1] := by native_decide
example : rem5 #[1,4,2,3,1,3,3,3] #[1,1,0,2] = #[0,4,1] := by native_decide
example : gcd5 #[1,4,2,3,1,3,3,3] #[1,1,0,2] = #[1] := by native_decide
example : frob5 #[1,4,2,3,1,3,3,3] #[1,1,0,2] = #[4,3,3] := by native_decide
example : subX #[1,4,2,3,1,3,3,3] = #[1,3,2,3,1,3,3,3] := by native_decide
example : mul5 #[2,0,0,3,4,3] #[4,4,2,4,3,2,4,0,2] = #[3,3,4,0,4,3,0,1,4,4,2,3,3,1] := by native_decide
example : rem5 #[2,0,0,3,4,3] #[4,4,2,4,3,2,4,0,2] = #[2,0,0,3,4,3] := by native_decide
example : gcd5 #[2,0,0,3,4,3] #[4,4,2,4,3,2,4,0,2] = #[1,1] := by native_decide
example : frob5 #[2,0,0,3,4,3] #[4,4,2,4,3,2,4,0,2] = #[1,1,2,0,4,1,4,4] := by native_decide
example : subX #[2,0,0,3,4,3] = #[2,4,0,3,4,3] := by native_decide
example : mul5 #[2,0,3,1,0,4,1,4,3] #[4,1,4,4,4,4,3] = #[3,2,0,0,1,0,0,4,4,2,3,4,1,4,4] := by native_decide
example : rem5 #[2,0,3,1,0,4,1,4,3] #[4,1,4,4,4,4,3] = #[1,1,3,4,0,4] := by native_decide
example : gcd5 #[2,0,3,1,0,4,1,4,3] #[4,1,4,4,4,4,3] = #[1] := by native_decide
example : frob5 #[2,0,3,1,0,4,1,4,3] #[4,1,4,4,4,4,3] = #[0,0,3,1,4,2] := by native_decide
example : subX #[2,0,3,1,0,4,1,4,3] = #[2,4,3,1,0,4,1,4,3] := by native_decide
example : mul5 #[1] #[4,0,3,1,1] = #[4,0,3,1,1] := by native_decide
example : rem5 #[1] #[4,0,3,1,1] = #[1] := by native_decide
example : gcd5 #[1] #[4,0,3,1,1] = #[1] := by native_decide
example : frob5 #[1] #[4,0,3,1,1] = #[1] := by native_decide
example : subX #[1] = #[1,4] := by native_decide
example : mul5 #[0,2] #[4,0,3] = #[0,3,0,1] := by native_decide
example : rem5 #[0,2] #[4,0,3] = #[0,2] := by native_decide
example : gcd5 #[0,2] #[4,0,3] = #[1] := by native_decide
example : frob5 #[0,2] #[4,0,3] = #[0,3] := by native_decide
example : subX #[0,2] = #[0,1] := by native_decide
example : mul5 #[2] #[4,0,1,0,1,1,1] = #[3,0,2,0,2,2,2] := by native_decide
example : rem5 #[2] #[4,0,1,0,1,1,1] = #[2] := by native_decide
example : gcd5 #[2] #[4,0,1,0,1,1,1] = #[1] := by native_decide
example : frob5 #[2] #[4,0,1,0,1,1,1] = #[2] := by native_decide
example : subX #[2] = #[2,4] := by native_decide
example : mul5 #[] #[2,3,2,2,2,1,2,2,3] = #[] := by native_decide
example : rem5 #[] #[2,3,2,2,2,1,2,2,3] = #[] := by native_decide
example : gcd5 #[] #[2,3,2,2,2,1,2,2,3] = #[4,1,4,4,4,2,4,4,1] := by native_decide
example : frob5 #[] #[2,3,2,2,2,1,2,2,3] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[3,3,3,4,3,2,1,4,2,3,2] #[1,4,1,4,2,1] = #[3,0,3,1,0,4,2,3,2,1,1,3,2,1,2,2] := by native_decide
example : rem5 #[3,3,3,4,3,2,1,4,2,3,2] #[1,4,1,4,2,1] = #[0,4,3,3,2] := by native_decide
example : gcd5 #[3,3,3,4,3,2,1,4,2,3,2] #[1,4,1,4,2,1] = #[1] := by native_decide
example : frob5 #[3,3,3,4,3,2,1,4,2,3,2] #[1,4,1,4,2,1] = #[4,0,0,3,2] := by native_decide
example : subX #[3,3,3,4,3,2,1,4,2,3,2] = #[3,2,3,4,3,2,1,4,2,3,2] := by native_decide
example : mul5 #[3,3] #[0,1,3,0,3] = #[0,3,2,4,4,4] := by native_decide
example : rem5 #[3,3] #[0,1,3,0,3] = #[3,3] := by native_decide
example : gcd5 #[3,3] #[0,1,3,0,3] = #[1,1] := by native_decide
example : frob5 #[3,3] #[0,1,3,0,3] = #[3,0,4,2] := by native_decide
example : subX #[3,3] = #[3,2] := by native_decide
example : mul5 #[2,4,0,3,0,2,3,1,1,3,3] #[3,4,0,3,4,3,2,4,1] = #[1,0,1,0,2,3,2,3,0,0,4,0,0,0,0,0,4,0,3] := by native_decide
example : rem5 #[2,4,0,3,0,2,3,1,1,3,3] #[3,4,0,3,4,3,2,4,1] = #[4,2,2,3,3,1,1,1] := by native_decide
example : gcd5 #[2,4,0,3,0,2,3,1,1,3,3] #[3,4,0,3,4,3,2,4,1] = #[1] := by native_decide
example : frob5 #[2,4,0,3,0,2,3,1,1,3,3] #[3,4,0,3,4,3,2,4,1] = #[2,0,1,1,4,3,1,2] := by native_decide
example : subX #[2,4,0,3,0,2,3,1,1,3,3] = #[2,3,0,3,0,2,3,1,1,3,3] := by native_decide
example : mul5 #[2,3,3] #[0,0,0,2] = #[0,0,0,4,1,1] := by native_decide
example : rem5 #[2,3,3] #[0,0,0,2] = #[2,3,3] := by native_decide
example : gcd5 #[2,3,3] #[0,0,0,2] = #[1] := by native_decide
example : frob5 #[2,3,3] #[0,0,0,2] = #[2] := by native_decide
example : subX #[2,3,3] = #[2,2,3] := by native_decide
example : mul5 #[1,2,1,0,1,4,0,4] #[0,3,0,4,2,3,3,2,3] = #[0,3,1,2,0,4,3,0,0,4,4,2,3,4,3,2] := by native_decide
example : rem5 #[1,2,1,0,1,4,0,4] #[0,3,0,4,2,3,3,2,3] = #[1,2,1,0,1,4,0,4] := by native_decide
example : gcd5 #[1,2,1,0,1,4,0,4] #[0,3,0,4,2,3,3,2,3] = #[1] := by native_decide
example : frob5 #[1,2,1,0,1,4,0,4] #[0,3,0,4,2,3,3,2,3] = #[1,1,2,0,0,1,2,1] := by native_decide
example : subX #[1,2,1,0,1,4,0,4] = #[1,1,1,0,1,4,0,4] := by native_decide
example : mul5 #[2,1,1,1,0,2] #[0,1,1,3,4] = #[0,2,3,3,3,3,4,1,1,3] := by native_decide
example : rem5 #[2,1,1,1,0,2] #[0,1,1,3,4] = #[2,2,4,1] := by native_decide
example : gcd5 #[2,1,1,1,0,2] #[0,1,1,3,4] = #[1] := by native_decide
example : frob5 #[2,1,1,1,0,2] #[0,1,1,3,4] = #[2,0,4] := by native_decide
example : subX #[2,1,1,1,0,2] = #[2,0,1,1,0,2] := by native_decide
example : mul5 #[0,3,0,2,2,2,3,3,3,0,1] #[2,3,0,1,4,1,4,0,4] = #[0,1,4,4,3,2,2,2,2,2,2,2,0,4,3,3,1,0,4] := by native_decide
example : rem5 #[0,3,0,2,2,2,3,3,3,0,1] #[2,3,0,1,4,1,4,0,4] = #[4,4,2,2,0,0,0,4] := by native_decide
example : gcd5 #[0,3,0,2,2,2,3,3,3,0,1] #[2,3,0,1,4,1,4,0,4] = #[1] := by native_decide
example : frob5 #[0,3,0,2,2,2,3,3,3,0,1] #[2,3,0,1,4,1,4,0,4] = #[4,4,1,0,1,1,2,2] := by native_decide
example : subX #[0,3,0,2,2,2,3,3,3,0,1] = #[0,2,0,2,2,2,3,3,3,0,1] := by native_decide
example : mul5 #[4,2,3,4,0,2,4,4] #[0,4,1] = #[0,1,2,4,4,4,3,3,0,4] := by native_decide
example : rem5 #[4,2,3,4,0,2,4,4] #[0,4,1] = #[4,4] := by native_decide
example : gcd5 #[4,2,3,4,0,2,4,4] #[0,4,1] = #[1] := by native_decide
example : frob5 #[4,2,3,4,0,2,4,4] #[0,4,1] = #[4,4] := by native_decide
example : subX #[4,2,3,4,0,2,4,4] = #[4,1,3,4,0,2,4,4] := by native_decide
example : mul5 #[2] #[2,3,4] = #[4,1,3] := by native_decide
example : rem5 #[2] #[2,3,4] = #[2] := by native_decide
example : gcd5 #[2] #[2,3,4] = #[1] := by native_decide
example : frob5 #[2] #[2,3,4] = #[2] := by native_decide
example : subX #[2] = #[2,4] := by native_decide
example : mul5 #[4,0,1,2,1,2,3] #[4,2,2,3,3] = #[1,3,2,2,2,2,2,4,0,0,4] := by native_decide
example : rem5 #[4,0,1,2,1,2,3] #[4,2,2,3,3] = #[4,3,1,4] := by native_decide
example : gcd5 #[4,0,1,2,1,2,3] #[4,2,2,3,3] = #[1] := by native_decide
example : frob5 #[4,0,1,2,1,2,3] #[4,2,2,3,3] = #[0,1,1] := by native_decide
example : subX #[4,0,1,2,1,2,3] = #[4,4,1,2,1,2,3] := by native_decide
example : mul5 #[1,2,0,1,1,1] #[3,0,1] = #[3,1,1,0,3,4,1,1] := by native_decide
example : rem5 #[1,2,0,1,1,1] #[3,0,1] = #[0,3] := by native_decide
example : gcd5 #[1,2,0,1,1,1] #[3,0,1] = #[1] := by native_decide
example : frob5 #[1,2,0,1,1,1] #[3,0,1] = #[0,2] := by native_decide
example : subX #[1,2,0,1,1,1] = #[1,1,0,1,1,1] := by native_decide
example : mul5 #[1,2] #[4] = #[4,3] := by native_decide
example : rem5 #[1,2] #[4] = #[] := by native_decide
example : gcd5 #[1,2] #[4] = #[1] := by native_decide
example : frob5 #[1,2] #[4] = #[] := by native_decide
example : subX #[1,2] = #[1,1] := by native_decide
example : mul5 #[4] #[1,2,2,3,4,1,1,1,2] = #[4,3,3,2,1,4,4,4,3] := by native_decide
example : rem5 #[4] #[1,2,2,3,4,1,1,1,2] = #[4] := by native_decide
example : gcd5 #[4] #[1,2,2,3,4,1,1,1,2] = #[1] := by native_decide
example : frob5 #[4] #[1,2,2,3,4,1,1,1,2] = #[4] := by native_decide
example : subX #[4] = #[4,4] := by native_decide
example : mul5 #[3,0,3,0,3,0,1,4] #[4] = #[2,0,2,0,2,0,4,1] := by native_decide
example : rem5 #[3,0,3,0,3,0,1,4] #[4] = #[] := by native_decide
example : gcd5 #[3,0,3,0,3,0,1,4] #[4] = #[1] := by native_decide
example : frob5 #[3,0,3,0,3,0,1,4] #[4] = #[] := by native_decide
example : subX #[3,0,3,0,3,0,1,4] = #[3,4,3,0,3,0,1,4] := by native_decide
example : mul5 #[1,2,4,0,2,3,0,0,1,3,2,2] #[3,3,1,1,2,3,4,4,2] = #[3,4,4,0,4,1,4,4,1,4,1,1,4,4,4,1,3,2,2,4] := by native_decide
example : rem5 #[1,2,4,0,2,3,0,0,1,3,2,2] #[3,3,1,1,2,3,4,4,2] = #[2,1,2,3,0,1,2,3] := by native_decide
example : gcd5 #[1,2,4,0,2,3,0,0,1,3,2,2] #[3,3,1,1,2,3,4,4,2] = #[1] := by native_decide
example : frob5 #[1,2,4,0,2,3,0,0,1,3,2,2] #[3,3,1,1,2,3,4,4,2] = #[3,3,3,2,3,0,2,1] := by native_decide
example : subX #[1,2,4,0,2,3,0,0,1,3,2,2] = #[1,1,4,0,2,3,0,0,1,3,2,2] := by native_decide
example : mul5 #[4,4,1,4,1,1,2,1,1,2,2,3,3] #[1,4,0,3,2,2,2] = #[4,0,2,0,2,4,1,0,0,4,1,2,4,1,4,3,1,2,1] := by native_decide
example : rem5 #[4,4,1,4,1,1,2,1,1,2,2,3,3] #[1,4,0,3,2,2,2] = #[1,1,4,0,3,1] := by native_decide
example : gcd5 #[4,4,1,4,1,1,2,1,1,2,2,3,3] #[1,4,0,3,2,2,2] = #[1] := by native_decide
example : frob5 #[4,4,1,4,1,1,2,1,1,2,2,3,3] #[1,4,0,3,2,2,2] = #[2,4,4,4,1,4] := by native_decide
example : subX #[4,4,1,4,1,1,2,1,1,2,2,3,3] = #[4,3,1,4,1,1,2,1,1,2,2,3,3] := by native_decide
example : mul5 #[1,3] #[4,3,4,4] = #[4,0,3,1,2] := by native_decide
example : rem5 #[1,3] #[4,3,4,4] = #[1,3] := by native_decide
example : gcd5 #[1,3] #[4,3,4,4] = #[1] := by native_decide
example : frob5 #[1,3] #[4,3,4,4] = #[4,4,1] := by native_decide
example : subX #[1,3] = #[1,2] := by native_decide
example : mul5 #[4,3,0,0,1,0,0,0,2,2] #[1,1,4,2] = #[4,2,4,0,2,1,4,2,2,4,0,2,4] := by native_decide
example : rem5 #[4,3,0,0,1,0,0,0,2,2] #[1,1,4,2] = #[3,1,3] := by native_decide
example : gcd5 #[4,3,0,0,1,0,0,0,2,2] #[1,1,4,2] = #[1] := by native_decide
example : frob5 #[4,3,0,0,1,0,0,0,2,2] #[1,1,4,2] = #[1,4,2] := by native_decide
example : subX #[4,3,0,0,1,0,0,0,2,2] = #[4,2,0,0,1,0,0,0,2,2] := by native_decide
example : mul5 #[1,3,0,0,1] #[4,2,4] = #[4,4,0,2,4,2,4] := by native_decide
example : rem5 #[1,3,0,0,1] #[4,2,4] = #[3,2] := by native_decide
example : gcd5 #[1,3,0,0,1] #[4,2,4] = #[4,1] := by native_decide
example : frob5 #[1,3,0,0,1] #[4,2,4] = #[] := by native_decide
example : subX #[1,3,0,0,1] = #[1,2,0,0,1] := by native_decide
example : mul5 #[4,0,1,1,0,4] #[3,4,2,3,0,1,2,1,1] = #[2,1,1,4,1,1,2,3,4,3,1,4,4,4] := by native_decide
example : rem5 #[4,0,1,1,0,4] #[3,4,2,3,0,1,2,1,1] = #[4,0,1,1,0,4] := by native_decide
example : gcd5 #[4,0,1,1,0,4] #[3,4,2,3,0,1,2,1,1] = #[1] := by native_decide
example : frob5 #[4,0,1,1,0,4] #[3,4,2,3,0,1,2,1,1] = #[0,0,0,4,0,1,0,1] := by native_decide
example : subX #[4,0,1,1,0,4] = #[4,4,1,1,0,4] := by native_decide
example : mul5 #[1,0,3,2,0,0,4,1,4] #[4,2,2,2] = #[4,2,4,1,0,0,0,2,1,3,0,3] := by native_decide
example : rem5 #[1,0,3,2,0,0,4,1,4] #[4,2,2,2] = #[] := by native_decide
example : gcd5 #[1,0,3,2,0,0,4,1,4] #[4,2,2,2] = #[2,1,1,1] := by native_decide
example : frob5 #[1,0,3,2,0,0,4,1,4] #[4,2,2,2] = #[] := by native_decide
example : subX #[1,0,3,2,0,0,4,1,4] = #[1,4,3,2,0,0,4,1,4] := by native_decide
example : mul5 #[2,4,0,2,0,3,2,2,4,4,0,3,1] #[2,1,4,0,4] = #[4,0,2,0,0,0,2,1,3,2,3,0,1,4,4,2,4] := by native_decide
example : rem5 #[2,4,0,2,0,3,2,2,4,4,0,3,1] #[2,1,4,0,4] = #[3,1,3,2] := by native_decide
example : gcd5 #[2,4,0,2,0,3,2,2,4,4,0,3,1] #[2,1,4,0,4] = #[1] := by native_decide
example : frob5 #[2,4,0,2,0,3,2,2,4,4,0,3,1] #[2,1,4,0,4] = #[2,1,3] := by native_decide
example : subX #[2,4,0,2,0,3,2,2,4,4,0,3,1] = #[2,3,0,2,0,3,2,2,4,4,0,3,1] := by native_decide
example : mul5 #[0,2,1,4,3,2] #[1,3,3,2,2] = #[0,2,2,3,2,4,0,0,0,4] := by native_decide
example : rem5 #[0,2,1,4,3,2] #[1,3,3,2,2] = #[2,2,4] := by native_decide
example : gcd5 #[0,2,1,4,3,2] #[1,3,3,2,2] = #[1] := by native_decide
example : frob5 #[0,2,1,4,3,2] #[1,3,3,2,2] = #[0,2,3,4] := by native_decide
example : subX #[0,2,1,4,3,2] = #[0,1,1,4,3,2] := by native_decide
example : mul5 #[2] #[1,4] = #[2,3] := by native_decide
example : rem5 #[2] #[1,4] = #[2] := by native_decide
example : gcd5 #[2] #[1,4] = #[1] := by native_decide
example : frob5 #[2] #[1,4] = #[2] := by native_decide
example : subX #[2] = #[2,4] := by native_decide
example : mul5 #[4,4,4,1,1,3,3,1,3,0,0,1,1] #[0,1,2,2] = #[0,4,2,0,2,1,2,1,3,1,3,1,1,3,4,2] := by native_decide
example : rem5 #[4,4,4,1,1,3,3,1,3,0,0,1,1] #[0,1,2,2] = #[4,3,4] := by native_decide
example : gcd5 #[4,4,4,1,1,3,3,1,3,0,0,1,1] #[0,1,2,2] = #[1] := by native_decide
example : frob5 #[4,4,4,1,1,3,3,1,3,0,0,1,1] #[0,1,2,2] = #[4,3,4] := by native_decide
example : subX #[4,4,4,1,1,3,3,1,3,0,0,1,1] = #[4,3,4,1,1,3,3,1,3,0,0,1,1] := by native_decide
example : mul5 #[2,1,4,4,4,1,2] #[2,0,1,4,3] = #[4,2,0,2,2,0,1,4,3,1,1] := by native_decide
example : rem5 #[2,1,4,4,4,1,2] #[2,0,1,4,3] = #[2,1,1,4] := by native_decide
example : gcd5 #[2,1,4,4,4,1,2] #[2,0,1,4,3] = #[1] := by native_decide
example : frob5 #[2,1,4,4,4,1,2] #[2,0,1,4,3] = #[1,1,3,3] := by native_decide
example : subX #[2,1,4,4,4,1,2] = #[2,0,4,4,4,1,2] := by native_decide
example : mul5 #[2,2,0,1,4,4,3] #[3,3,3] = #[1,2,2,4,0,2,3,1,4] := by native_decide
example : rem5 #[2,2,0,1,4,4,3] #[3,3,3] = #[2,2] := by native_decide
example : gcd5 #[2,2,0,1,4,4,3] #[3,3,3] = #[1] := by native_decide
example : frob5 #[2,2,0,1,4,4,3] #[3,3,3] = #[0,3] := by native_decide
example : subX #[2,2,0,1,4,4,3] = #[2,1,0,1,4,4,3] := by native_decide
example : mul5 #[0,2,4,0,3,3,3,2,0,2] #[2,1,0,1,3,1] = #[0,4,0,4,3,4,3,4,4,4,1,4,4,1,2] := by native_decide
example : rem5 #[0,2,4,0,3,3,3,2,0,2] #[2,1,0,1,3,1] = #[4,4,3,1,1] := by native_decide
example : gcd5 #[0,2,4,0,3,3,3,2,0,2] #[2,1,0,1,3,1] = #[1] := by native_decide
example : frob5 #[0,2,4,0,3,3,3,2,0,2] #[2,1,0,1,3,1] = #[2,3,3,1] := by native_decide
example : subX #[0,2,4,0,3,3,3,2,0,2] = #[0,1,4,0,3,3,3,2,0,2] := by native_decide
example : mul5 #[2,0,4,4,3,1,2,4,4] #[3,3] = #[1,1,2,4,1,2,4,3,4,2] := by native_decide
example : rem5 #[2,0,4,4,3,1,2,4,4] #[3,3] = #[1] := by native_decide
example : gcd5 #[2,0,4,4,3,1,2,4,4] #[3,3] = #[1] := by native_decide
example : frob5 #[2,0,4,4,3,1,2,4,4] #[3,3] = #[1] := by native_decide
example : subX #[2,0,4,4,3,1,2,4,4] = #[2,4,4,4,3,1,2,4,4] := by native_decide
example : mul5 #[4,3,2,4,2,4] #[1,4,1,0,2,0,0,3] = #[4,4,3,0,3,2,2,4,3,4,2,1,2] := by native_decide
example : rem5 #[4,3,2,4,2,4] #[1,4,1,0,2,0,0,3] = #[4,3,2,4,2,4] := by native_decide
example : gcd5 #[4,3,2,4,2,4] #[1,4,1,0,2,0,0,3] = #[1] := by native_decide
example : frob5 #[4,3,2,4,2,4] #[1,4,1,0,2,0,0,3] = #[4,2,2,4,2,3,4] := by native_decide
example : subX #[4,3,2,4,2,4] = #[4,2,2,4,2,4] := by native_decide
example : mul5 #[4,1,2,3,1,0,4,3,3] #[3,4,4] = #[2,4,1,1,3,1,1,0,2,4,2] := by native_decide
example : rem5 #[4,1,2,3,1,0,4,3,3] #[3,4,4] = #[4,4] := by native_decide
example : gcd5 #[4,1,2,3,1,0,4,3,3] #[3,4,4] = #[1] := by native_decide
example : frob5 #[4,1,2,3,1,0,4,3,3] #[3,4,4] = #[0,1] := by native_decide
example : subX #[4,1,2,3,1,0,4,3,3] = #[4,0,2,3,1,0,4,3,3] := by native_decide
example : mul5 #[2,3,0,3] #[0,2,0,2] = #[0,4,1,4,2,0,1] := by native_decide
example : rem5 #[2,3,0,3] #[0,2,0,2] = #[2] := by native_decide
example : gcd5 #[2,3,0,3] #[0,2,0,2] = #[1] := by native_decide
example : frob5 #[2,3,0,3] #[0,2,0,2] = #[2] := by native_decide
example : subX #[2,3,0,3] = #[2,2,0,3] := by native_decide
example : mul5 #[0,2,1,4,2] #[1] = #[0,2,1,4,2] := by native_decide
example : rem5 #[0,2,1,4,2] #[1] = #[] := by native_decide
example : gcd5 #[0,2,1,4,2] #[1] = #[1] := by native_decide
example : frob5 #[0,2,1,4,2] #[1] = #[] := by native_decide
example : subX #[0,2,1,4,2] = #[0,1,1,4,2] := by native_decide
example : mul5 #[0,0,1,2,2,1,3,2] #[3,4,0,2,0,2,1] = #[0,0,3,0,4,3,2,4,0,2,3,2,2,2] := by native_decide
example : rem5 #[0,0,1,2,2,1,3,2] #[3,4,0,2,0,2,1] = #[3,3,3,4,3,3] := by native_decide
example : gcd5 #[0,0,1,2,2,1,3,2] #[3,4,0,2,0,2,1] = #[1] := by native_decide
example : frob5 #[0,0,1,2,2,1,3,2] #[3,4,0,2,0,2,1] = #[4,4,1,1,0,4] := by native_decide
example : subX #[0,0,1,2,2,1,3,2] = #[0,4,1,2,2,1,3,2] := by native_decide
example : mul5 #[3,4,0,0,0,4] #[4,1] = #[2,4,4,0,0,1,4] := by native_decide
example : rem5 #[3,4,0,0,0,4] #[4,1] = #[1] := by native_decide
example : gcd5 #[3,4,0,0,0,4] #[4,1] = #[1] := by native_decide
example : frob5 #[3,4,0,0,0,4] #[4,1] = #[1] := by native_decide
example : subX #[3,4,0,0,0,4] = #[3,3,0,0,0,4] := by native_decide
example : mul5 #[] #[4,3,3,1,1,3,4,2,1] = #[] := by native_decide
example : rem5 #[] #[4,3,3,1,1,3,4,2,1] = #[] := by native_decide
example : gcd5 #[] #[4,3,3,1,1,3,4,2,1] = #[4,3,3,1,1,3,4,2,1] := by native_decide
example : frob5 #[] #[4,3,3,1,1,3,4,2,1] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[] #[1,3,0,2] = #[] := by native_decide
example : rem5 #[] #[1,3,0,2] = #[] := by native_decide
example : gcd5 #[] #[1,3,0,2] = #[3,4,0,1] := by native_decide
example : frob5 #[] #[1,3,0,2] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[2] #[3,3] = #[1,1] := by native_decide
example : rem5 #[2] #[3,3] = #[2] := by native_decide
example : gcd5 #[2] #[3,3] = #[1] := by native_decide
example : frob5 #[2] #[3,3] = #[2] := by native_decide
example : subX #[2] = #[2,4] := by native_decide
example : mul5 #[0,1,3,0,2,0,1] #[4,3,2,4,4,1] = #[0,4,0,1,3,2,1,4,0,1,4,1] := by native_decide
example : rem5 #[0,1,3,0,2,0,1] #[4,3,2,4,4,1] = #[1,4,3,4,4] := by native_decide
example : gcd5 #[0,1,3,0,2,0,1] #[4,3,2,4,4,1] = #[1] := by native_decide
example : frob5 #[0,1,3,0,2,0,1] #[4,3,2,4,4,1] = #[3,2,3,2,3] := by native_decide
example : subX #[0,1,3,0,2,0,1] = #[0,0,3,0,2,0,1] := by native_decide
example : mul5 #[3,2,3,3,4,1,3,2,2,3,4] #[0,3,2,2,2,4] = #[0,4,2,4,0,0,1,2,4,4,2,3,1,2,0,1] := by native_decide
example : rem5 #[3,2,3,3,4,1,3,2,2,3,4] #[0,3,2,2,2,4] = #[3,0,4,4] := by native_decide
example : gcd5 #[3,2,3,3,4,1,3,2,2,3,4] #[0,3,2,2,2,4] = #[1] := by native_decide
example : frob5 #[3,2,3,3,4,1,3,2,2,3,4] #[0,3,2,2,2,4] = #[3,4,3,3,4] := by native_decide
example : subX #[3,2,3,3,4,1,3,2,2,3,4] = #[3,1,3,3,4,1,3,2,2,3,4] := by native_decide
example : mul5 #[3,1,0,4,1,3,2] #[4,2,3,1,4] = #[2,0,1,2,0,0,1,0,3,4,3] := by native_decide
example : rem5 #[3,1,0,4,1,3,2] #[4,2,3,1,4] = #[1,0,4] := by native_decide
example : gcd5 #[3,1,0,4,1,3,2] #[4,2,3,1,4] = #[1] := by native_decide
example : frob5 #[3,1,0,4,1,3,2] #[4,2,3,1,4] = #[2,4,2,1] := by native_decide
example : subX #[3,1,0,4,1,3,2] = #[3,0,0,4,1,3,2] := by native_decide
example : mul5 #[3,1] #[4,2,1,3,4,2] = #[2,0,0,0,0,0,2] := by native_decide
example : rem5 #[3,1] #[4,2,1,3,4,2] = #[3,1] := by native_decide
example : gcd5 #[3,1] #[4,2,1,3,4,2] = #[1] := by native_decide
example : frob5 #[3,1] #[4,2,1,3,4,2] = #[1,4,2,1,3] := by native_decide
example : subX #[3,1] = #[3] := by native_decide
example : mul5 #[1,3,1,3] #[0,3] = #[0,3,4,3,4] := by native_decide
example : rem5 #[1,3,1,3] #[0,3] = #[1] := by native_decide
example : gcd5 #[1,3,1,3] #[0,3] = #[1] := by native_decide
example : frob5 #[1,3,1,3] #[0,3] = #[1] := by native_decide
example : subX #[1,3,1,3] = #[1,2,1,3] := by native_decide
example : mul5 #[] #[4,4,3,2,1,1,0,4,4] = #[] := by native_decide
example : rem5 #[] #[4,4,3,2,1,1,0,4,4] = #[] := by native_decide
example : gcd5 #[] #[4,4,3,2,1,1,0,4,4] = #[1,1,2,3,4,4,0,1,1] := by native_decide
example : frob5 #[] #[4,4,3,2,1,1,0,4,4] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[4,0,4,0,3,0,2,3,3,1,1,3] #[0,3,0,2] = #[0,2,0,0,0,2,0,2,4,3,4,4,1,2,1] := by native_decide
example : rem5 #[4,0,4,0,3,0,2,3,3,1,1,3] #[0,3,0,2] = #[4,2,3] := by native_decide
example : gcd5 #[4,0,4,0,3,0,2,3,3,1,1,3] #[0,3,0,2] = #[1,1] := by native_decide
example : frob5 #[4,0,4,0,3,0,2,3,3,1,1,3] #[0,3,0,2] = #[4,2,3] := by native_decide
example : subX #[4,0,4,0,3,0,2,3,3,1,1,3] = #[4,4,4,0,3,0,2,3,3,1,1,3] := by native_decide
example : mul5 #[0,0,2,0,3,3,2,1] #[3,4,3,0,1] = #[0,0,1,3,0,1,4,0,3,1,2,1] := by native_decide
example : rem5 #[0,0,2,0,3,3,2,1] #[3,4,3,0,1] = #[1,3,2,4] := by native_decide
example : gcd5 #[0,0,2,0,3,3,2,1] #[3,4,3,0,1] = #[1] := by native_decide
example : frob5 #[0,0,2,0,3,3,2,1] #[3,4,3,0,1] = #[2,0,2,1] := by native_decide
example : subX #[0,0,2,0,3,3,2,1] = #[0,4,2,0,3,3,2,1] := by native_decide
example : mul5 #[3,4,2,1,4,3,0,3,4,1] #[4,2,4,2,0,4,3] = #[2,2,3,0,4,0,4,2,3,3,3,1,4,0,1,3] := by native_decide
example : rem5 #[3,4,2,1,4,3,0,3,4,1] #[4,2,4,2,0,4,3] = #[0,0,1,0,2,3] := by native_decide
example : gcd5 #[3,4,2,1,4,3,0,3,4,1] #[4,2,4,2,0,4,3] = #[1] := by native_decide
example : frob5 #[3,4,2,1,4,3,0,3,4,1] #[4,2,4,2,0,4,3] = #[0,4,2,1,4,2] := by native_decide
example : subX #[3,4,2,1,4,3,0,3,4,1] = #[3,3,2,1,4,3,0,3,4,1] := by native_decide
example : mul5 #[1,1,1] #[4,1,4,4,2] = #[4,0,4,4,0,1,2] := by native_decide
example : rem5 #[1,1,1] #[4,1,4,4,2] = #[1,1,1] := by native_decide
example : gcd5 #[1,1,1] #[4,1,4,4,2] = #[1] := by native_decide
example : frob5 #[1,1,1] #[4,1,4,4,2] = #[2,3,0,3] := by native_decide
example : subX #[1,1,1] = #[1,0,1] := by native_decide
example : mul5 #[4,4,4,4,3,3,0,4,2,2] #[3,2,1,1] = #[2,0,4,3,0,3,3,3,2,4,0,4,2] := by native_decide
example : rem5 #[4,4,4,4,3,3,0,4,2,2] #[3,2,1,1] = #[0,0,2] := by native_decide
example : gcd5 #[4,4,4,4,3,3,0,4,2,2] #[3,2,1,1] = #[1] := by native_decide
example : frob5 #[4,4,4,4,3,3,0,4,2,2] #[3,2,1,1] = #[3] := by native_decide
example : subX #[4,4,4,4,3,3,0,4,2,2] = #[4,3,4,4,3,3,0,4,2,2] := by native_decide
example : mul5 #[] #[3,0,4,3,3,2,2,2] = #[] := by native_decide
example : rem5 #[] #[3,0,4,3,3,2,2,2] = #[] := by native_decide
example : gcd5 #[] #[3,0,4,3,3,2,2,2] = #[4,0,2,4,4,1,1,1] := by native_decide
example : frob5 #[] #[3,0,4,3,3,2,2,2] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[2,3] #[4,0,4,1] = #[3,2,3,4,3] := by native_decide
example : rem5 #[2,3] #[4,0,4,1] = #[2,3] := by native_decide
example : gcd5 #[2,3] #[4,0,4,1] = #[1] := by native_decide
example : frob5 #[2,3] #[4,0,4,1] = #[0,3,1] := by native_decide
example : subX #[2,3] = #[2,2] := by native_decide
example : mul5 #[3,4,3,0,1,0,1,2,1] #[2,1,4,3,1,1,0,4] = #[1,1,2,3,4,2,3,3,0,0,1,0,3,0,3,4] := by native_decide
example : rem5 #[3,4,3,0,1,0,1,2,1] #[2,1,4,3,1,1,0,4] = #[2,3,2,0,1,3,2] := by native_decide
example : gcd5 #[3,4,3,0,1,0,1,2,1] #[2,1,4,3,1,1,0,4] = #[1] := by native_decide
example : frob5 #[3,4,3,0,1,0,1,2,1] #[2,1,4,3,1,1,0,4] = #[3,0,4,3,2,2,1] := by native_decide
example : subX #[3,4,3,0,1,0,1,2,1] = #[3,3,3,0,1,0,1,2,1] := by native_decide
example : mul5 #[2,2,2,1,1,2] #[0,1,4,1,0,2] = #[0,2,0,2,1,1,1,3,4,2,4] := by native_decide
example : rem5 #[2,2,2,1,1,2] #[0,1,4,1,0,2] = #[2,1,3,0,1] := by native_decide
example : gcd5 #[2,2,2,1,1,2] #[0,1,4,1,0,2] = #[1,1] := by native_decide
example : frob5 #[2,2,2,1,1,2] #[0,1,4,1,0,2] = #[2,0,0,3,1] := by native_decide
example : subX #[2,2,2,1,1,2] = #[2,1,2,1,1,2] := by native_decide
example : mul5 #[1,2,2,0,2,2,2,4,0,4,4] #[3,1,1] = #[3,2,4,4,3,3,0,1,1,1,1,3,4] := by native_decide
example : rem5 #[1,2,2,0,2,2,2,4,0,4,4] #[3,1,1] = #[1,2] := by native_decide
example : gcd5 #[1,2,2,0,2,2,2,4,0,4,4] #[3,1,1] = #[1] := by native_decide
example : frob5 #[1,2,2,0,2,2,2,4,0,4,4] #[3,1,1] = #[1,2] := by native_decide
example : subX #[1,2,2,0,2,2,2,4,0,4,4] = #[1,1,2,0,2,2,2,4,0,4,4] := by native_decide
example : mul5 #[4,0,0,1,1,4,3,3,2,4,0,4] #[4,2,3] = #[1,3,2,4,1,1,3,0,3,4,4,3,3,2] := by native_decide
example : rem5 #[4,0,0,1,1,4,3,3,2,4,0,4] #[4,2,3] = #[4] := by native_decide
example : gcd5 #[4,0,0,1,1,4,3,3,2,4,0,4] #[4,2,3] = #[1] := by native_decide
example : frob5 #[4,0,0,1,1,4,3,3,2,4,0,4] #[4,2,3] = #[4] := by native_decide
example : subX #[4,0,0,1,1,4,3,3,2,4,0,4] = #[4,4,0,1,1,4,3,3,2,4,0,4] := by native_decide
example : mul5 #[] #[3,4] = #[] := by native_decide
example : rem5 #[] #[3,4] = #[] := by native_decide
example : gcd5 #[] #[3,4] = #[2,1] := by native_decide
example : frob5 #[] #[3,4] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[1,1,2,2,4,4,0,0,3] #[0,4,4,0,3] = #[0,4,3,2,4,2,3,2,2,4,2,0,4] := by native_decide
example : rem5 #[1,1,2,2,4,4,0,0,3] #[0,4,4,0,3] = #[1,3,4,4] := by native_decide
example : gcd5 #[1,1,2,2,4,4,0,0,3] #[0,4,4,0,3] = #[1] := by native_decide
example : frob5 #[1,1,2,2,4,4,0,0,3] #[0,4,4,0,3] = #[1,3,2,2] := by native_decide
example : subX #[1,1,2,2,4,4,0,0,3] = #[1,0,2,2,4,4,0,0,3] := by native_decide
example : mul5 #[1,4,4,0,2,2,4,3,1,1,0,0,1] #[1] = #[1,4,4,0,2,2,4,3,1,1,0,0,1] := by native_decide
example : rem5 #[1,4,4,0,2,2,4,3,1,1,0,0,1] #[1] = #[] := by native_decide
example : gcd5 #[1,4,4,0,2,2,4,3,1,1,0,0,1] #[1] = #[1] := by native_decide
example : frob5 #[1,4,4,0,2,2,4,3,1,1,0,0,1] #[1] = #[] := by native_decide
example : subX #[1,4,4,0,2,2,4,3,1,1,0,0,1] = #[1,3,4,0,2,2,4,3,1,1,0,0,1] := by native_decide
example : mul5 #[1,3] #[0,3,1,0,3,1,3,0,3] = #[0,3,0,3,3,0,1,4,3,4] := by native_decide
example : rem5 #[1,3] #[0,3,1,0,3,1,3,0,3] = #[1,3] := by native_decide
example : gcd5 #[1,3] #[0,3,1,0,3,1,3,0,3] = #[1] := by native_decide
example : frob5 #[1,3] #[0,3,1,0,3,1,3,0,3] = #[1,0,0,0,0,3] := by native_decide
example : subX #[1,3] = #[1,2] := by native_decide
example : mul5 #[4,0,0,1,2,1,2,1,4,2,3,2] #[3,0,4,3,3,1] = #[2,0,1,0,3,1,2,1,0,1,0,1,1,2,2,4,2] := by native_decide
example : rem5 #[4,0,0,1,2,1,2,1,4,2,3,2] #[3,0,4,3,3,1] = #[4,4,1,3,4] := by native_decide
example : gcd5 #[4,0,0,1,2,1,2,1,4,2,3,2] #[3,0,4,3,3,1] = #[1] := by native_decide
example : frob5 #[4,0,0,1,2,1,2,1,4,2,3,2] #[3,0,4,3,3,1] = #[3,3,3,0,4] := by native_decide
example : subX #[4,0,0,1,2,1,2,1,4,2,3,2] = #[4,4,0,1,2,1,2,1,4,2,3,2] := by native_decide
example : mul5 #[2,1] #[2] = #[4,2] := by native_decide
example : rem5 #[2,1] #[2] = #[] := by native_decide
example : gcd5 #[2,1] #[2] = #[1] := by native_decide
example : frob5 #[2,1] #[2] = #[] := by native_decide
example : subX #[2,1] = #[2] := by native_decide
example : mul5 #[2,3,1,3,4,2,1,2,2,2,3,3] #[0,1,3,4,4,0,4,3] = #[0,2,4,3,1,4,3,3,2,0,0,0,3,0,3,1,3,1,4] := by native_decide
example : rem5 #[2,3,1,3,4,2,1,2,2,2,3,3] #[0,1,3,4,4,0,4,3] = #[2,4,3,4,1,3] := by native_decide
example : gcd5 #[2,3,1,3,4,2,1,2,2,2,3,3] #[0,1,3,4,4,0,4,3] = #[1] := by native_decide
example : frob5 #[2,3,1,3,4,2,1,2,2,2,3,3] #[0,1,3,4,4,0,4,3] = #[2,1,2,2,2,0,4] := by native_decide
example : subX #[2,3,1,3,4,2,1,2,2,2,3,3] = #[2,2,1,3,4,2,1,2,2,2,3,3] := by native_decide
example : mul5 #[2,0,0,2,2,4,1,2,2,2,2] #[1,3,0,4,1,4] = #[2,1,0,0,0,3,1,0,4,4,3,0,3,3,0,3] := by native_decide
example : rem5 #[2,0,0,2,2,4,1,2,2,2,2] #[1,3,0,4,1,4] = #[3,3,2,1,4] := by native_decide
example : gcd5 #[2,0,0,2,2,4,1,2,2,2,2] #[1,3,0,4,1,4] = #[1] := by native_decide
example : frob5 #[2,0,0,2,2,4,1,2,2,2,2] #[1,3,0,4,1,4] = #[3,1,1,2,2] := by native_decide
example : subX #[2,0,0,2,2,4,1,2,2,2,2] = #[2,4,0,2,2,4,1,2,2,2,2] := by native_decide
example : mul5 #[0,1,1,2,2,0,4,1] #[4,4,2,2,3] = #[0,4,3,4,0,2,2,0,3,0,4,3] := by native_decide
example : rem5 #[0,1,1,2,2,0,4,1] #[4,4,2,2,3] = #[0,3,3] := by native_decide
example : gcd5 #[0,1,1,2,2,0,4,1] #[4,4,2,2,3] = #[1] := by native_decide
example : frob5 #[0,1,1,2,2,0,4,1] #[4,4,2,2,3] = #[3,1,3,4] := by native_decide
example : subX #[0,1,1,2,2,0,4,1] = #[0,0,1,2,2,0,4,1] := by native_decide
example : mul5 #[1,0,4,3,4,3] #[3,1] = #[3,1,2,3,0,3,3] := by native_decide
example : rem5 #[1,0,4,3,4,3] #[3,1] = #[1] := by native_decide
example : gcd5 #[1,0,4,3,4,3] #[3,1] = #[1] := by native_decide
example : frob5 #[1,0,4,3,4,3] #[3,1] = #[1] := by native_decide
example : subX #[1,0,4,3,4,3] = #[1,4,4,3,4,3] := by native_decide
example : mul5 #[2,0,1,4,1,1,2,0,4,1,1,2] #[0,2] = #[0,4,0,2,3,2,2,4,0,3,2,2,4] := by native_decide
example : rem5 #[2,0,1,4,1,1,2,0,4,1,1,2] #[0,2] = #[2] := by native_decide
example : gcd5 #[2,0,1,4,1,1,2,0,4,1,1,2] #[0,2] = #[1] := by native_decide
example : frob5 #[2,0,1,4,1,1,2,0,4,1,1,2] #[0,2] = #[2] := by native_decide
example : subX #[2,0,1,4,1,1,2,0,4,1,1,2] = #[2,4,1,4,1,1,2,0,4,1,1,2] := by native_decide
example : mul5 #[3,0,4,3,4,4] #[4,0,3,4,4,2] = #[2,0,0,4,0,2,0,3,3,4,3] := by native_decide
example : rem5 #[3,0,4,3,4,4] #[4,0,3,4,4,2] = #[0,0,3,0,1] := by native_decide
example : gcd5 #[3,0,4,3,4,4] #[4,0,3,4,4,2] = #[1] := by native_decide
example : frob5 #[3,0,4,3,4,4] #[4,0,3,4,4,2] = #[3,2,2,4] := by native_decide
example : subX #[3,0,4,3,4,4] = #[3,4,4,3,4,4] := by native_decide
example : mul5 #[2,4,0,0,4] #[2,3,0,4,2,1] = #[4,4,2,3,3,2,4,1,3,4] := by native_decide
example : rem5 #[2,4,0,0,4] #[2,3,0,4,2,1] = #[2,4,0,0,4] := by native_decide
example : gcd5 #[2,4,0,0,4] #[2,3,0,4,2,1] = #[1] := by native_decide
example : frob5 #[2,4,0,0,4] #[2,3,0,4,2,1] = #[4,0,4,3,4] := by native_decide
example : subX #[2,4,0,0,4] = #[2,3,0,0,4] := by native_decide
example : mul5 #[3,1,1,1,4,1] #[4,3,0,0,4] = #[2,3,2,2,1,0,2,4,1,4] := by native_decide
example : rem5 #[3,1,1,1,4,1] #[4,3,0,0,4] = #[4,2,4,1] := by native_decide
example : gcd5 #[3,1,1,1,4,1] #[4,3,0,0,4] = #[1,1] := by native_decide
example : frob5 #[3,1,1,1,4,1] #[4,3,0,0,4] = #[4,0,2,1] := by native_decide
example : subX #[3,1,1,1,4,1] = #[3,0,1,1,4,1] := by native_decide
example : mul5 #[4,2,2,4,4,1,1,0,4,1] #[3,3] = #[2,3,2,3,4,0,1,3,2,0,3] := by native_decide
example : rem5 #[4,2,2,4,4,1,1,0,4,1] #[3,3] = #[2] := by native_decide
example : gcd5 #[4,2,2,4,4,1,1,0,4,1] #[3,3] = #[1] := by native_decide
example : frob5 #[4,2,2,4,4,1,1,0,4,1] #[3,3] = #[2] := by native_decide
example : subX #[4,2,2,4,4,1,1,0,4,1] = #[4,1,2,4,4,1,1,0,4,1] := by native_decide
example : mul5 #[2,2,2,4,1,3,1] #[0,4,4,0,3,2,0,4] = #[0,3,1,1,0,0,1,0,3,4,0,1,2,4] := by native_decide
example : rem5 #[2,2,2,4,1,3,1] #[0,4,4,0,3,2,0,4] = #[2,2,2,4,1,3,1] := by native_decide
example : gcd5 #[2,2,2,4,1,3,1] #[0,4,4,0,3,2,0,4] = #[1] := by native_decide
example : frob5 #[2,2,2,4,1,3,1] #[0,4,4,0,3,2,0,4] = #[2,1,3,1,2,1,1] := by native_decide
example : subX #[2,2,2,4,1,3,1] = #[2,1,2,4,1,3,1] := by native_decide
example : mul5 #[2,0,1,3,2,2,1,4,0,1,1] #[2,3,4,1,4,4,4] = #[4,1,0,1,0,1,1,2,2,2,4,0,0,1,3,3,4] := by native_decide
example : rem5 #[2,0,1,3,2,2,1,4,0,1,1] #[2,3,4,1,4,4,4] = #[2,2,2,4,1,3] := by native_decide
example : gcd5 #[2,0,1,3,2,2,1,4,0,1,1] #[2,3,4,1,4,4,4] = #[1] := by native_decide
example : frob5 #[2,0,1,3,2,2,1,4,0,1,1] #[2,3,4,1,4,4,4] = #[0,1,1,1,0,2] := by native_decide
example : subX #[2,0,1,3,2,2,1,4,0,1,1] = #[2,4,1,3,2,2,1,4,0,1,1] := by native_decide
example : mul5 #[4] #[4,4,4,0,0,4] = #[1,1,1,0,0,1] := by native_decide
example : rem5 #[4] #[4,4,4,0,0,4] = #[4] := by native_decide
example : gcd5 #[4] #[4,4,4,0,0,4] = #[1] := by native_decide
example : frob5 #[4] #[4,4,4,0,0,4] = #[4] := by native_decide
example : subX #[4] = #[4,4] := by native_decide
example : mul5 #[] #[0,4,0,4] = #[] := by native_decide
example : rem5 #[] #[0,4,0,4] = #[] := by native_decide
example : gcd5 #[] #[0,4,0,4] = #[0,1,0,1] := by native_decide
example : frob5 #[] #[0,4,0,4] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[3,0,2,3,3,0,2,0,3,2,1] #[2,4,0,2,4,3,3,3,3] = #[1,2,4,0,0,0,2,1,2,4,2,4,1,0,0,3,3,4,3] := by native_decide
example : rem5 #[3,0,2,3,3,0,2,0,3,2,1] #[2,4,0,2,4,3,3,3,3] = #[4,3,0,1,1,2,2,2] := by native_decide
example : gcd5 #[3,0,2,3,3,0,2,0,3,2,1] #[2,4,0,2,4,3,3,3,3] = #[1] := by native_decide
example : frob5 #[3,0,2,3,3,0,2,0,3,2,1] #[2,4,0,2,4,3,3,3,3] = #[4,1,4,2,2,1,2,4] := by native_decide
example : subX #[3,0,2,3,3,0,2,0,3,2,1] = #[3,4,2,3,3,0,2,0,3,2,1] := by native_decide
example : mul5 #[2,4,3] #[0,3,0,1,3,4,2,3,3] = #[0,1,2,1,0,3,4,1,4,1,4] := by native_decide
example : rem5 #[2,4,3] #[0,3,0,1,3,4,2,3,3] = #[2,4,3] := by native_decide
example : gcd5 #[2,4,3] #[0,3,0,1,3,4,2,3,3] = #[1] := by native_decide
example : frob5 #[2,4,3] #[0,3,0,1,3,4,2,3,3] = #[2,4,3,0,0,3,2,2] := by native_decide
example : subX #[2,4,3] = #[2,3,3] := by native_decide
example : mul5 #[4,1] #[0,1,1] = #[0,4,0,1] := by native_decide
example : rem5 #[4,1] #[0,1,1] = #[4,1] := by native_decide
example : gcd5 #[4,1] #[0,1,1] = #[1] := by native_decide
example : frob5 #[4,1] #[0,1,1] = #[4,1] := by native_decide
example : subX #[4,1] = #[4] := by native_decide
example : mul5 #[3,4,1,1,1,3,3,2,1,1,3,0,4] #[2,4,4,0,2,1,4,1,3] = #[1,0,0,2,1,0,0,0,2,3,1,4,2,4,3,4,4,0,0,4,2] := by native_decide
example : rem5 #[3,4,1,1,1,3,3,2,1,1,3,0,4] #[2,4,4,0,2,1,4,1,3] = #[2,0,2,3,2,0,0,3] := by native_decide
example : gcd5 #[3,4,1,1,1,3,3,2,1,1,3,0,4] #[2,4,4,0,2,1,4,1,3] = #[1] := by native_decide
example : frob5 #[3,4,1,1,1,3,3,2,1,1,3,0,4] #[2,4,4,0,2,1,4,1,3] = #[1,2,0,2,1,4,1,2] := by native_decide
example : subX #[3,4,1,1,1,3,3,2,1,1,3,0,4] = #[3,3,1,1,1,3,3,2,1,1,3,0,4] := by native_decide
example : mul5 #[1,4,4,4,4,3,1,2,1,3,3] #[0,4,4,1,4,3,4] = #[0,4,0,3,0,0,4,4,4,3,2,3,4,1,0,1,2] := by native_decide
example : rem5 #[1,4,4,4,4,3,1,2,1,3,3] #[0,4,4,1,4,3,4] = #[1,3,3,1,2] := by native_decide
example : gcd5 #[1,4,4,4,4,3,1,2,1,3,3] #[0,4,4,1,4,3,4] = #[1,3,1] := by native_decide
example : frob5 #[1,4,4,4,4,3,1,2,1,3,3] #[0,4,4,1,4,3,4] = #[1,3,2,3,1] := by native_decide
example : subX #[1,4,4,4,4,3,1,2,1,3,3] = #[1,3,4,4,4,3,1,2,1,3,3] := by native_decide
example : mul5 #[2,1] #[0,0,2,0,2,3,1] = #[0,0,4,2,4,3,0,1] := by native_decide
example : rem5 #[2,1] #[0,0,2,0,2,3,1] = #[2,1] := by native_decide
example : gcd5 #[2,1] #[0,0,2,0,2,3,1] = #[1] := by native_decide
example : frob5 #[2,1] #[0,0,2,0,2,3,1] = #[2,0,0,0,0,1] := by native_decide
example : subX #[2,1] = #[2] := by native_decide
example : mul5 #[] #[0,4,0,3,1] = #[] := by native_decide
example : rem5 #[] #[0,4,0,3,1] = #[] := by native_decide
example : gcd5 #[] #[0,4,0,3,1] = #[0,4,0,3,1] := by native_decide
example : frob5 #[] #[0,4,0,3,1] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[4,1,0,0,4,2,4,1,2] #[1,3,4,3,2,2,4,2,2] = #[4,3,4,1,0,4,4,0,0,1,4,2,4,0,3,1,4] := by native_decide
example : rem5 #[4,1,0,0,4,2,4,1,2] #[1,3,4,3,2,2,4,2,2] = #[3,3,1,2,2,0,0,4] := by native_decide
example : gcd5 #[4,1,0,0,4,2,4,1,2] #[1,3,4,3,2,2,4,2,2] = #[1] := by native_decide
example : frob5 #[4,1,0,0,4,2,4,1,2] #[1,3,4,3,2,2,4,2,2] = #[1,1,4,3,1,3,4,3] := by native_decide
example : subX #[4,1,0,0,4,2,4,1,2] = #[4,0,0,0,4,2,4,1,2] := by native_decide
example : mul5 #[2,2,2,4,0,2,2,4,2,1,3,2] #[0,2,0,3,0,2] = #[0,4,4,0,4,0,0,3,2,0,3,1,0,3,3,1,4] := by native_decide
example : rem5 #[2,2,2,4,0,2,2,4,2,1,3,2] #[0,2,0,3,0,2] = #[2,3,3,3,4] := by native_decide
example : gcd5 #[2,2,2,4,0,2,2,4,2,1,3,2] #[0,2,0,3,0,2] = #[1] := by native_decide
example : frob5 #[2,2,2,4,0,2,2,4,2,1,3,2] #[0,2,0,3,0,2] = #[2,2,1,1,2] := by native_decide
example : subX #[2,2,2,4,0,2,2,4,2,1,3,2] = #[2,1,2,4,0,2,2,4,2,1,3,2] := by native_decide
example : mul5 #[2,4,2,0,4,1,4,0,4] #[2,4,4,1,3] = #[4,1,3,1,1,2,4,4,2,3,3,4,2] := by native_decide
example : rem5 #[2,4,2,0,4,1,4,0,4] #[2,4,4,1,3] = #[1,4,2,4] := by native_decide
example : gcd5 #[2,4,2,0,4,1,4,0,4] #[2,4,4,1,3] = #[1] := by native_decide
example : frob5 #[2,4,2,0,4,1,4,0,4] #[2,4,4,1,3] = #[4,1,1,4] := by native_decide
example : subX #[2,4,2,0,4,1,4,0,4] = #[2,3,2,0,4,1,4,0,4] := by native_decide
example : mul5 #[] #[4,4,3] = #[] := by native_decide
example : rem5 #[] #[4,4,3] = #[] := by native_decide
example : gcd5 #[] #[4,4,3] = #[3,3,1] := by native_decide
example : frob5 #[] #[4,4,3] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[1,0,0,3,0,0,2] #[4,4,1,1] = #[4,4,1,3,2,3,1,3,2,2] := by native_decide
example : rem5 #[1,0,0,3,0,0,2] #[4,4,1,1] = #[0,3,3] := by native_decide
example : gcd5 #[1,0,0,3,0,0,2] #[4,4,1,1] = #[1,1] := by native_decide
example : frob5 #[1,0,0,3,0,0,2] #[4,4,1,1] = #[4,3,4] := by native_decide
example : subX #[1,0,0,3,0,0,2] = #[1,4,0,3,0,0,2] := by native_decide
example : mul5 #[1,4,1,3,1,2,4,2] #[0,4,2,1,1,4] = #[0,4,3,3,4,4,0,3,1,4,4,3,3] := by native_decide
example : rem5 #[1,4,1,3,1,2,4,2] #[0,4,2,1,1,4] = #[1,4,0,3,1] := by native_decide
example : gcd5 #[1,4,1,3,1,2,4,2] #[0,4,2,1,1,4] = #[2,1] := by native_decide
example : frob5 #[1,4,1,3,1,2,4,2] #[0,4,2,1,1,4] = #[1,4,1,0,3] := by native_decide
example : subX #[1,4,1,3,1,2,4,2] = #[1,3,1,3,1,2,4,2] := by native_decide
example : mul5 #[] #[3] = #[] := by native_decide
example : rem5 #[] #[3] = #[] := by native_decide
example : gcd5 #[] #[3] = #[1] := by native_decide
example : frob5 #[] #[3] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[0,3,0,1,2] #[2,4,3,4,1,4,4,1,4] = #[0,1,2,1,0,4,2,1,4,4,4,1,3] := by native_decide
example : rem5 #[0,3,0,1,2] #[2,4,3,4,1,4,4,1,4] = #[0,3,0,1,2] := by native_decide
example : gcd5 #[0,3,0,1,2] #[2,4,3,4,1,4,4,1,4] = #[1] := by native_decide
example : frob5 #[0,3,0,1,2] #[2,4,3,4,1,4,4,1,4] = #[4,2,1,2,4,1,2,4] := by native_decide
example : subX #[0,3,0,1,2] = #[0,2,0,1,2] := by native_decide
example : mul5 #[1,1,1,0,4,1,3,2,4,4,4] #[1,1,0,1,0,4,0,4,4] = #[1,2,2,2,0,0,3,2,0,0,3,1,2,1,1,0,2,2,1] := by native_decide
example : rem5 #[1,1,1,0,4,1,3,2,4,4,4] #[1,1,0,1,0,4,0,4,4] = #[0,0,0,3,4,1,3,4] := by native_decide
example : gcd5 #[1,1,1,0,4,1,3,2,4,4,4] #[1,1,0,1,0,4,0,4,4] = #[4,1] := by native_decide
example : frob5 #[1,1,1,0,4,1,3,2,4,4,4] #[1,1,0,1,0,4,0,4,4] = #[0,3,3,0,4,3,0,2] := by native_decide
example : subX #[1,1,1,0,4,1,3,2,4,4,4] = #[1,0,1,0,4,1,3,2,4,4,4] := by native_decide
example : mul5 #[2,1,0,4,0,4,3,4,2,1] #[0,4,1,3,0,4,2,4] = #[0,3,1,2,4,2,1,1,1,4,0,2,1,3,4,0,4] := by native_decide
example : rem5 #[2,1,0,4,0,4,3,4,2,1] #[0,4,1,3,0,4,2,4] = #[2,0,2,0,3,1,1] := by native_decide
example : gcd5 #[2,1,0,4,0,4,3,4,2,1] #[0,4,1,3,0,4,2,4] = #[2,1] := by native_decide
example : frob5 #[2,1,0,4,0,4,3,4,2,1] #[0,4,1,3,0,4,2,4] = #[2,3,4,1,4,4] := by native_decide
example : subX #[2,1,0,4,0,4,3,4,2,1] = #[2,0,0,4,0,4,3,4,2,1] := by native_decide
example : mul5 #[0,1,0,4,1,2] #[3,4,4,1,1,0,3] = #[0,3,4,1,0,2,1,1,3,4,3,1] := by native_decide
example : rem5 #[0,1,0,4,1,2] #[3,4,4,1,1,0,3] = #[0,1,0,4,1,2] := by native_decide
example : gcd5 #[0,1,0,4,1,2] #[3,4,4,1,1,0,3] = #[1] := by native_decide
example : frob5 #[0,1,0,4,1,2] #[3,4,4,1,1,0,3] = #[2,1,2,2,0,1] := by native_decide
example : subX #[0,1,0,4,1,2] = #[0,0,0,4,1,2] := by native_decide
example : mul5 #[0,3,4,2,4,3] #[1,2,4,2,4] = #[0,3,0,2,0,4,2,3,2,2] := by native_decide
example : rem5 #[0,3,4,2,4,3] #[1,2,4,2,4] = #[0,1,0,4] := by native_decide
example : gcd5 #[0,3,4,2,4,3] #[1,2,4,2,4] = #[1,1] := by native_decide
example : frob5 #[0,3,4,2,4,3] #[1,2,4,2,4] = #[2,0,4,1] := by native_decide
example : subX #[0,3,4,2,4,3] = #[0,2,4,2,4,3] := by native_decide
example : mul5 #[3,4,3] #[0,4,2,2] = #[0,2,2,1,4,1] := by native_decide
example : rem5 #[3,4,3] #[0,4,2,2] = #[3,4,3] := by native_decide
example : gcd5 #[3,4,3] #[0,4,2,2] = #[1] := by native_decide
example : frob5 #[3,4,3] #[0,4,2,2] = #[3,0,1] := by native_decide
example : subX #[3,4,3] = #[3,3,3] := by native_decide
example : mul5 #[0,0,4,0,2,0,0,4] #[1,4,2,1,4,1] = #[0,0,4,1,0,2,0,0,4,0,4,1,4] := by native_decide
example : rem5 #[0,0,4,0,2,0,0,4] #[1,4,2,1,4,1] = #[0,1,4,1] := by native_decide
example : gcd5 #[0,0,4,0,2,0,0,4] #[1,4,2,1,4,1] = #[1] := by native_decide
example : frob5 #[0,0,4,0,2,0,0,4] #[1,4,2,1,4,1] = #[4,2,2,2,4] := by native_decide
example : subX #[0,0,4,0,2,0,0,4] = #[0,4,4,0,2,0,0,4] := by native_decide
example : mul5 #[1,2,4] #[2,3,1] = #[2,2,0,4,4] := by native_decide
example : rem5 #[1,2,4] #[2,3,1] = #[3] := by native_decide
example : gcd5 #[1,2,4] #[2,3,1] = #[1] := by native_decide
example : frob5 #[1,2,4] #[2,3,1] = #[3] := by native_decide
example : subX #[1,2,4] = #[1,1,4] := by native_decide
example : mul5 #[1,3,1,2,1,2,1,2,2,3,3,4,2] #[0,1,4,1,4] = #[0,1,2,4,3,2,2,3,2,4,2,0,2,3,4,3,3] := by native_decide
example : rem5 #[1,3,1,2,1,2,1,2,2,3,3,4,2] #[0,1,4,1,4] = #[1,3,0,3] := by native_decide
example : gcd5 #[1,3,1,2,1,2,1,2,2,3,3,4,2] #[0,1,4,1,4] = #[1] := by native_decide
example : frob5 #[1,3,1,2,1,2,1,2,2,3,3,4,2] #[0,1,4,1,4] = #[1,3,0,3] := by native_decide
example : subX #[1,3,1,2,1,2,1,2,2,3,3,4,2] = #[1,2,1,2,1,2,1,2,2,3,3,4,2] := by native_decide
example : mul5 #[4,0,3,3,3,0,4,2,0,4,3,1] #[1,1,0,0,3,0,0,4] = #[4,4,3,1,3,3,3,1,1,1,1,2,1,3,2,3,1,2,4] := by native_decide
example : rem5 #[4,0,3,3,3,0,4,2,0,4,3,1] #[1,1,0,0,3,0,0,4] = #[0,4,0,0,0,0,1] := by native_decide
example : gcd5 #[4,0,3,3,3,0,4,2,0,4,3,1] #[1,1,0,0,3,0,0,4] = #[1] := by native_decide
example : frob5 #[4,0,3,3,3,0,4,2,0,4,3,1] #[1,1,0,0,3,0,0,4] = #[1,0,2,0,1,1,2] := by native_decide
example : subX #[4,0,3,3,3,0,4,2,0,4,3,1] = #[4,4,3,3,3,0,4,2,0,4,3,1] := by native_decide
example : mul5 #[3,1,4,3,1,2,1] #[4,2,1,3,3,0,3] = #[2,0,1,0,1,3,4,4,2,3,1,1,3] := by native_decide
example : rem5 #[3,1,4,3,1,2,1] #[4,2,1,3,3,0,3] = #[0,2,2,2,0,2] := by native_decide
example : gcd5 #[3,1,4,3,1,2,1] #[4,2,1,3,3,0,3] = #[1] := by native_decide
example : frob5 #[3,1,4,3,1,2,1] #[4,2,1,3,3,0,3] = #[3,3,2,3,0,1] := by native_decide
example : subX #[3,1,4,3,1,2,1] = #[3,0,4,3,1,2,1] := by native_decide
example : mul5 #[4,3,4,2,2] #[0,1] = #[0,4,3,4,2,2] := by native_decide
example : rem5 #[4,3,4,2,2] #[0,1] = #[4] := by native_decide
example : gcd5 #[4,3,4,2,2] #[0,1] = #[1] := by native_decide
example : frob5 #[4,3,4,2,2] #[0,1] = #[4] := by native_decide
example : subX #[4,3,4,2,2] = #[4,2,4,2,2] := by native_decide
example : mul5 #[4,1] #[4,3,2] = #[1,1,1,2] := by native_decide
example : rem5 #[4,1] #[4,3,2] = #[4,1] := by native_decide
example : gcd5 #[4,1] #[4,3,2] = #[1] := by native_decide
example : frob5 #[4,1] #[4,3,2] = #[0,4] := by native_decide
example : subX #[4,1] = #[4] := by native_decide
example : mul5 #[3,4,2,1,4,0,4] #[3,0,2] = #[4,2,2,1,1,2,0,0,3] := by native_decide
example : rem5 #[3,4,2,1,4,0,4] #[3,0,2] = #[3] := by native_decide
example : gcd5 #[3,4,2,1,4,0,4] #[3,0,2] = #[1] := by native_decide
example : frob5 #[3,4,2,1,4,0,4] #[3,0,2] = #[3] := by native_decide
example : subX #[3,4,2,1,4,0,4] = #[3,3,2,1,4,0,4] := by native_decide
example : mul5 #[0,1,4,0,0,2,4] #[0,1,2,2,2] = #[0,0,1,1,0,0,0,3,2,2,3] := by native_decide
example : rem5 #[0,1,4,0,0,2,4] #[0,1,2,2,2] = #[0,2,2,2] := by native_decide
example : gcd5 #[0,1,4,0,0,2,4] #[0,1,2,2,2] = #[0,1] := by native_decide
example : frob5 #[0,1,4,0,0,2,4] #[0,1,2,2,2] = #[0,2,2,2] := by native_decide
example : subX #[0,1,4,0,0,2,4] = #[0,0,4,0,0,2,4] := by native_decide
example : mul5 #[] #[2,1,3,3] = #[] := by native_decide
example : rem5 #[] #[2,1,3,3] = #[] := by native_decide
example : gcd5 #[] #[2,1,3,3] = #[4,2,1,1] := by native_decide
example : frob5 #[] #[2,1,3,3] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[4] #[4,1,0,3,3] = #[1,4,0,2,2] := by native_decide
example : rem5 #[4] #[4,1,0,3,3] = #[4] := by native_decide
example : gcd5 #[4] #[4,1,0,3,3] = #[1] := by native_decide
example : frob5 #[4] #[4,1,0,3,3] = #[4] := by native_decide
example : subX #[4] = #[4,4] := by native_decide
example : mul5 #[] #[1,3,0,4] = #[] := by native_decide
example : rem5 #[] #[1,3,0,4] = #[] := by native_decide
example : gcd5 #[] #[1,3,0,4] = #[4,2,0,1] := by native_decide
example : frob5 #[] #[1,3,0,4] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[4,3,2,2,1,3,0,3,0,4] #[2,2,1] = #[3,4,4,1,3,0,2,4,1,1,3,4] := by native_decide
example : rem5 #[4,3,2,2,1,3,0,3,0,4] #[2,2,1] = #[1,1] := by native_decide
example : gcd5 #[4,3,2,2,1,3,0,3,0,4] #[2,2,1] = #[1] := by native_decide
example : frob5 #[4,3,2,2,1,3,0,3,0,4] #[2,2,1] = #[1,1] := by native_decide
example : subX #[4,3,2,2,1,3,0,3,0,4] = #[4,2,2,2,1,3,0,3,0,4] := by native_decide
example : mul5 #[3,3,2,4,4,4,2,1,2,1,3] #[1,1,0,1,4,1] = #[3,1,0,4,3,0,1,0,2,0,2,1,0,4,3,3] := by native_decide
example : rem5 #[3,3,2,4,4,4,2,1,2,1,3] #[1,1,0,1,4,1] = #[0,4,1,3,4] := by native_decide
example : gcd5 #[3,3,2,4,4,4,2,1,2,1,3] #[1,1,0,1,4,1] = #[1] := by native_decide
example : frob5 #[3,3,2,4,4,4,2,1,2,1,3] #[1,1,0,1,4,1] = #[0,4,0,1,2] := by native_decide
example : subX #[3,3,2,4,4,4,2,1,2,1,3] = #[3,2,2,4,4,4,2,1,2,1,3] := by native_decide
example : mul5 #[1,0,2,3,1,0,4,3,2] #[1,4,2,1,3] = #[1,4,4,2,0,2,0,4,0,3,4,1,1] := by native_decide
example : rem5 #[1,0,2,3,1,0,4,3,2] #[1,4,2,1,3] = #[3,4,4] := by native_decide
example : gcd5 #[1,0,2,3,1,0,4,3,2] #[1,4,2,1,3] = #[2,1,1] := by native_decide
example : frob5 #[1,0,2,3,1,0,4,3,2] #[1,4,2,1,3] = #[3,4,4] := by native_decide
example : subX #[1,0,2,3,1,0,4,3,2] = #[1,4,2,3,1,0,4,3,2] := by native_decide
example : mul5 #[0,3,0,1] #[2,0,1,3] = #[0,1,0,0,4,1,3] := by native_decide
example : rem5 #[0,3,0,1] #[2,0,1,3] = #[1,3,3] := by native_decide
example : gcd5 #[0,3,0,1] #[2,0,1,3] = #[1] := by native_decide
example : frob5 #[0,3,0,1] #[2,0,1,3] = #[1,3,3] := by native_decide
example : subX #[0,3,0,1] = #[0,2,0,1] := by native_decide
example : mul5 #[4,2,3,2,1,3,3,3,3,0,1,3] #[4] = #[1,3,2,3,4,2,2,2,2,0,4,2] := by native_decide
example : rem5 #[4,2,3,2,1,3,3,3,3,0,1,3] #[4] = #[] := by native_decide
example : gcd5 #[4,2,3,2,1,3,3,3,3,0,1,3] #[4] = #[1] := by native_decide
example : frob5 #[4,2,3,2,1,3,3,3,3,0,1,3] #[4] = #[] := by native_decide
example : subX #[4,2,3,2,1,3,3,3,3,0,1,3] = #[4,1,3,2,1,3,3,3,3,0,1,3] := by native_decide
example : mul5 #[0,1,3,2,4,0,0,1,0,3,2,1,3] #[1,0,0,2,3,4] = #[0,1,3,2,1,4,2,2,0,4,4,4,3,3,0,2,3,2] := by native_decide
example : rem5 #[0,1,3,2,4,0,0,1,0,3,2,1,3] #[1,0,0,2,3,4] = #[4,2,2,2] := by native_decide
example : gcd5 #[0,1,3,2,4,0,0,1,0,3,2,1,3] #[1,0,0,2,3,4] = #[4,1] := by native_decide
example : frob5 #[0,1,3,2,4,0,0,1,0,3,2,1,3] #[1,0,0,2,3,4] = #[3,3,2,0,2] := by native_decide
example : subX #[0,1,3,2,4,0,0,1,0,3,2,1,3] = #[0,0,3,2,4,0,0,1,0,3,2,1,3] := by native_decide
example : mul5 #[4,4,1,4,0,2,4,0,2,0,1,2,4] #[3,0,0,4,3,1,1,4] = #[2,2,3,3,3,1,4,3,0,0,3,0,0,2,3,1,0,0,2,1] := by native_decide
example : rem5 #[4,4,1,4,0,2,4,0,2,0,1,2,4] #[3,0,0,4,3,1,1,4] = #[0,2,3,0,3,0,3] := by native_decide
example : gcd5 #[4,4,1,4,0,2,4,0,2,0,1,2,4] #[3,0,0,4,3,1,1,4] = #[1] := by native_decide
example : frob5 #[4,4,1,4,0,2,4,0,2,0,1,2,4] #[3,0,0,4,3,1,1,4] = #[4,3,2,2,2,3,3] := by native_decide
example : subX #[4,4,1,4,0,2,4,0,2,0,1,2,4] = #[4,3,1,4,0,2,4,0,2,0,1,2,4] := by native_decide
example : mul5 #[2,3,1,1,0,2] #[1,2,3,3,1,1,2,3] = #[2,2,3,3,1,3,0,0,3,2,0,4,1] := by native_decide
example : rem5 #[2,3,1,1,0,2] #[1,2,3,3,1,1,2,3] = #[2,3,1,1,0,2] := by native_decide
example : gcd5 #[2,3,1,1,0,2] #[1,2,3,3,1,1,2,3] = #[1] := by native_decide
example : frob5 #[2,3,1,1,0,2] #[1,2,3,3,1,1,2,3] = #[3,0,3,0,1,4] := by native_decide
example : subX #[2,3,1,1,0,2] = #[2,2,1,1,0,2] := by native_decide
example : mul5 #[4,0,1,0,3,2,0,3] #[4,4,1,0,4] = #[1,1,3,4,4,0,0,4,4,1,0,2] := by native_decide
example : rem5 #[4,0,1,0,3,2,0,3] #[4,4,1,0,4] = #[4,0,1,2] := by native_decide
example : gcd5 #[4,0,1,0,3,2,0,3] #[4,4,1,0,4] = #[1] := by native_decide
example : frob5 #[4,0,1,0,3,2,0,3] #[4,4,1,0,4] = #[4,1,4,4] := by native_decide
example : subX #[4,0,1,0,3,2,0,3] = #[4,4,1,0,3,2,0,3] := by native_decide
example : mul5 #[3,3,1,2,3,3,1,4,1,3,0,3,1] #[4] = #[2,2,4,3,2,2,4,1,4,2,0,2,4] := by native_decide
example : rem5 #[3,3,1,2,3,3,1,4,1,3,0,3,1] #[4] = #[] := by native_decide
example : gcd5 #[3,3,1,2,3,3,1,4,1,3,0,3,1] #[4] = #[1] := by native_decide
example : frob5 #[3,3,1,2,3,3,1,4,1,3,0,3,1] #[4] = #[] := by native_decide
example : subX #[3,3,1,2,3,3,1,4,1,3,0,3,1] = #[3,2,1,2,3,3,1,4,1,3,0,3,1] := by native_decide
example : mul5 #[4,2,4,0,4,1] #[0,1,1,0,2] = #[0,4,1,1,2,3,3,1,3,2] := by native_decide
example : rem5 #[4,2,4,0,4,1] #[0,1,1,0,2] = #[4,0,4,2] := by native_decide
example : gcd5 #[4,2,4,0,4,1] #[0,1,1,0,2] = #[1] := by native_decide
example : frob5 #[4,2,4,0,4,1] #[0,1,1,0,2] = #[4,2,3,1] := by native_decide
example : subX #[4,2,4,0,4,1] = #[4,1,4,0,4,1] := by native_decide
example : mul5 #[3,1,1,2,2,4,4,3,0,3,4,1,3] #[3,3,4] = #[4,2,3,3,1,1,2,2,0,1,1,2,3,3,2] := by native_decide
example : rem5 #[3,1,1,2,2,4,4,3,0,3,4,1,3] #[3,3,4] = #[4,2] := by native_decide
example : gcd5 #[3,1,1,2,2,4,4,3,0,3,4,1,3] #[3,3,4] = #[1] := by native_decide
example : frob5 #[3,1,1,2,2,4,4,3,0,3,4,1,3] #[3,3,4] = #[4,2] := by native_decide
example : subX #[3,1,1,2,2,4,4,3,0,3,4,1,3] = #[3,0,1,2,2,4,4,3,0,3,4,1,3] := by native_decide
example : mul5 #[2,3,1] #[4,4,0,2] = #[3,0,1,3,1,2] := by native_decide
example : rem5 #[2,3,1] #[4,4,0,2] = #[2,3,1] := by native_decide
example : gcd5 #[2,3,1] #[4,4,0,2] = #[2,1] := by native_decide
example : frob5 #[2,3,1] #[4,4,0,2] = #[2,3,1] := by native_decide
example : subX #[2,3,1] = #[2,2,1] := by native_decide
example : mul5 #[1,3,0,1,0,1,0,0,3,3] #[3,2,4,3,0,1,1,4] = #[3,1,0,3,1,3,4,1,0,1,3,2,3,3,1,0,2] := by native_decide
example : rem5 #[1,3,0,1,0,1,0,0,3,3] #[3,2,4,3,0,1,1,4] = #[3,4,2,3,0,4] := by native_decide
example : gcd5 #[1,3,0,1,0,1,0,0,3,3] #[3,2,4,3,0,1,1,4] = #[1] := by native_decide
example : frob5 #[1,3,0,1,0,1,0,0,3,3] #[3,2,4,3,0,1,1,4] = #[2,1,3,3,3,4] := by native_decide
example : subX #[1,3,0,1,0,1,0,0,3,3] = #[1,2,0,1,0,1,0,0,3,3] := by native_decide
example : mul5 #[2,1,1,3] #[3,2,1,2,3,2,1] = #[1,2,2,1,0,2,3,2,2,3] := by native_decide
example : rem5 #[2,1,1,3] #[3,2,1,2,3,2,1] = #[2,1,1,3] := by native_decide
example : gcd5 #[2,1,1,3] #[3,2,1,2,3,2,1] = #[2,1] := by native_decide
example : frob5 #[2,1,1,3] #[3,2,1,2,3,2,1] = #[3,3,4,0,2] := by native_decide
example : subX #[2,1,1,3] = #[2,0,1,3] := by native_decide
example : mul5 #[1,1,4,3,2,0,3,1,3,2,4] #[3,4,4,0,1,1,4] = #[3,2,0,4,0,2,1,1,1,1,3,3,2,4,3,2,1] := by native_decide
example : rem5 #[1,1,4,3,2,0,3,1,3,2,4] #[3,4,4,0,1,1,4] = #[2,4,1,3,2,2] := by native_decide
example : gcd5 #[1,1,4,3,2,0,3,1,3,2,4] #[3,4,4,0,1,1,4] = #[1] := by native_decide
example : frob5 #[1,1,4,3,2,0,3,1,3,2,4] #[3,4,4,0,1,1,4] = #[2,2,2,3,4] := by native_decide
example : subX #[1,1,4,3,2,0,3,1,3,2,4] = #[1,0,4,3,2,0,3,1,3,2,4] := by native_decide
example : mul5 #[4,2,4,4,0,4,0,3,1,4,3,2] #[2,0,1,4,4,0,2] = #[3,4,2,1,3,1,0,0,1,0,4,2,3,1,2,1,1,4] := by native_decide
example : rem5 #[4,2,4,4,0,4,0,3,1,4,3,2] #[2,0,1,4,4,0,2] = #[0,1,1,3,4,3] := by native_decide
example : gcd5 #[4,2,4,4,0,4,0,3,1,4,3,2] #[2,0,1,4,4,0,2] = #[3,1] := by native_decide
example : frob5 #[4,2,4,4,0,4,0,3,1,4,3,2] #[2,0,1,4,4,0,2] = #[0,0,4,2,0,4] := by native_decide
example : subX #[4,2,4,4,0,4,0,3,1,4,3,2] = #[4,1,4,4,0,4,0,3,1,4,3,2] := by native_decide
example : mul5 #[4,3,0,2,4,0,1,2] #[1,0,2] = #[4,3,3,3,4,4,4,2,2,4] := by native_decide
example : rem5 #[4,3,0,2,4,0,1,2] #[1,0,2] = #[3,3] := by native_decide
example : gcd5 #[4,3,0,2,4,0,1,2] #[1,0,2] = #[1] := by native_decide
example : frob5 #[4,3,0,2,4,0,1,2] #[1,0,2] = #[3,2] := by native_decide
example : subX #[4,3,0,2,4,0,1,2] = #[4,2,0,2,4,0,1,2] := by native_decide
example : mul5 #[2,4,1,3,0,1] #[0,4] = #[0,3,1,4,2,0,4] := by native_decide
example : rem5 #[2,4,1,3,0,1] #[0,4] = #[2] := by native_decide
example : gcd5 #[2,4,1,3,0,1] #[0,4] = #[1] := by native_decide
example : frob5 #[2,4,1,3,0,1] #[0,4] = #[2] := by native_decide
example : subX #[2,4,1,3,0,1] = #[2,3,1,3,0,1] := by native_decide
example : mul5 #[1,2,4] #[3,3,1,1,2,3,2,2] = #[3,4,4,0,3,1,1,3,2,3] := by native_decide
example : rem5 #[1,2,4] #[3,3,1,1,2,3,2,2] = #[1,2,4] := by native_decide
example : gcd5 #[1,2,4] #[3,3,1,1,2,3,2,2] = #[1] := by native_decide
example : frob5 #[1,2,4] #[3,3,1,1,2,3,2,2] = #[0,2,2,4,3,3,1] := by native_decide
example : subX #[1,2,4] = #[1,1,4] := by native_decide
example : mul5 #[4,2] #[0,4,4] = #[0,1,4,3] := by native_decide
example : rem5 #[4,2] #[0,4,4] = #[4,2] := by native_decide
example : gcd5 #[4,2] #[0,4,4] = #[1] := by native_decide
example : frob5 #[4,2] #[0,4,4] = #[4,2] := by native_decide
example : subX #[4,2] = #[4,1] := by native_decide
example : mul5 #[3,3,4,3,1,3,2] #[0,0,2,2] = #[0,0,1,2,4,4,3,3,0,4] := by native_decide
example : rem5 #[3,3,4,3,1,3,2] #[0,0,2,2] = #[3,3,1] := by native_decide
example : gcd5 #[3,3,4,3,1,3,2] #[0,0,2,2] = #[1] := by native_decide
example : frob5 #[3,3,4,3,1,3,2] #[0,0,2,2] = #[3,0,3] := by native_decide
example : subX #[3,3,4,3,1,3,2] = #[3,2,4,3,1,3,2] := by native_decide
example : mul5 #[1,2,4,2,4,2,3,1] #[1,1,0,4] = #[1,3,1,0,4,2,3,0,4,2,4] := by native_decide
example : rem5 #[1,2,4,2,4,2,3,1] #[1,1,0,4] = #[4,3] := by native_decide
example : gcd5 #[1,2,4,2,4,2,3,1] #[1,1,0,4] = #[3,1] := by native_decide
example : frob5 #[1,2,4,2,4,2,3,1] #[1,1,0,4] = #[2,3,3] := by native_decide
example : subX #[1,2,4,2,4,2,3,1] = #[1,1,4,2,4,2,3,1] := by native_decide
example : mul5 #[0,3,1,4,2,4] #[2,1,3,4] = #[0,1,0,3,3,1,1,0,1] := by native_decide
example : rem5 #[0,3,1,4,2,4] #[2,1,3,4] = #[0,1,3] := by native_decide
example : gcd5 #[0,3,1,4,2,4] #[2,1,3,4] = #[2,1] := by native_decide
example : frob5 #[0,3,1,4,2,4] #[2,1,3,4] = #[0,1,3] := by native_decide
example : subX #[0,3,1,4,2,4] = #[0,2,1,4,2,4] := by native_decide
example : mul5 #[4,3,0,3,3,3] #[4] = #[1,2,0,2,2,2] := by native_decide
example : rem5 #[4,3,0,3,3,3] #[4] = #[] := by native_decide
example : gcd5 #[4,3,0,3,3,3] #[4] = #[1] := by native_decide
example : frob5 #[4,3,0,3,3,3] #[4] = #[] := by native_decide
example : subX #[4,3,0,3,3,3] = #[4,2,0,3,3,3] := by native_decide
example : mul5 #[0,0,3,0,2,2] #[3,4,1,3,3,3] = #[0,0,4,2,4,3,4,2,2,2,1] := by native_decide
example : rem5 #[0,0,3,0,2,2] #[3,4,1,3,3,3] = #[3,4,4,3] := by native_decide
example : gcd5 #[0,0,3,0,2,2] #[3,4,1,3,3,3] = #[1] := by native_decide
example : frob5 #[0,0,3,0,2,2] #[3,4,1,3,3,3] = #[4,0,2,2] := by native_decide
example : subX #[0,0,3,0,2,2] = #[0,4,3,0,2,2] := by native_decide
example : mul5 #[2,1,3,2,3,4,4,1] #[1,3,1] = #[2,2,3,2,2,0,4,2,2,1] := by native_decide
example : rem5 #[2,1,3,2,3,4,4,1] #[1,3,1] = #[4,1] := by native_decide
example : gcd5 #[2,1,3,2,3,4,4,1] #[1,3,1] = #[4,1] := by native_decide
example : frob5 #[2,1,3,2,3,4,4,1] #[1,3,1] = #[] := by native_decide
example : subX #[2,1,3,2,3,4,4,1] = #[2,0,3,2,3,4,4,1] := by native_decide
example : mul5 #[3,4] #[2,0,4,0,4,3,1,1,3] = #[1,3,2,1,2,0,0,2,3,2] := by native_decide
example : rem5 #[3,4] #[2,0,4,0,4,3,1,1,3] = #[3,4] := by native_decide
example : gcd5 #[3,4] #[2,0,4,0,4,3,1,1,3] = #[2,1] := by native_decide
example : frob5 #[3,4] #[2,0,4,0,4,3,1,1,3] = #[3,0,0,0,0,4] := by native_decide
example : subX #[3,4] = #[3,3] := by native_decide
example : mul5 #[0,3,3,0,1,2,3,1,2] #[4] = #[0,2,2,0,4,3,2,4,3] := by native_decide
example : rem5 #[0,3,3,0,1,2,3,1,2] #[4] = #[] := by native_decide
example : gcd5 #[0,3,3,0,1,2,3,1,2] #[4] = #[1] := by native_decide
example : frob5 #[0,3,3,0,1,2,3,1,2] #[4] = #[] := by native_decide
example : subX #[0,3,3,0,1,2,3,1,2] = #[0,2,3,0,1,2,3,1,2] := by native_decide
example : mul5 #[4,0,2,0,2,3,4,1] #[2,0,3,3,4] = #[3,0,1,2,1,2,2,2,4,2,4,4] := by native_decide
example : rem5 #[4,0,2,0,2,3,4,1] #[2,0,3,3,4] = #[2,4,3] := by native_decide
example : gcd5 #[4,0,2,0,2,3,4,1] #[2,0,3,3,4] = #[1] := by native_decide
example : frob5 #[4,0,2,0,2,3,4,1] #[2,0,3,3,4] = #[4,3,1] := by native_decide
example : subX #[4,0,2,0,2,3,4,1] = #[4,4,2,0,2,3,4,1] := by native_decide
example : mul5 #[0,4,3,3,4,3,3,2,4,3,0,1,2] #[1,0,0,2,1,3] = #[0,4,3,3,2,3,4,2,3,4,1,0,3,0,1,0,0,1] := by native_decide
example : rem5 #[0,4,3,3,4,3,3,2,4,3,0,1,2] #[1,0,0,2,1,3] = #[3,4,0,1,4] := by native_decide
example : gcd5 #[0,4,3,3,4,3,3,2,4,3,0,1,2] #[1,0,0,2,1,3] = #[1] := by native_decide
example : frob5 #[0,4,3,3,4,3,3,2,4,3,0,1,2] #[1,0,0,2,1,3] = #[3,1,1,2,2] := by native_decide
example : subX #[0,4,3,3,4,3,3,2,4,3,0,1,2] = #[0,3,3,3,4,3,3,2,4,3,0,1,2] := by native_decide
example : mul5 #[0,4,4,0,0,3,2] #[2,2] = #[0,3,1,3,0,1,0,4] := by native_decide
example : rem5 #[0,4,4,0,0,3,2] #[2,2] = #[4] := by native_decide
example : gcd5 #[0,4,4,0,0,3,2] #[2,2] = #[1] := by native_decide
example : frob5 #[0,4,4,0,0,3,2] #[2,2] = #[4] := by native_decide
example : subX #[0,4,4,0,0,3,2] = #[0,3,4,0,0,3,2] := by native_decide
example : mul5 #[0,3,1,4,4,2,2] #[1,3,1,3] = #[0,3,0,0,1,1,4,0,3,1] := by native_decide
example : rem5 #[0,3,1,4,4,2,2] #[1,3,1,3] = #[0,1,4] := by native_decide
example : gcd5 #[0,3,1,4,4,2,2] #[1,3,1,3] = #[1] := by native_decide
example : frob5 #[0,3,1,4,4,2,2] #[1,3,1,3] = #[0,1,4] := by native_decide
example : subX #[0,3,1,4,4,2,2] = #[0,2,1,4,4,2,2] := by native_decide
example : mul5 #[1,0,2,0,1,2,2,3,0,1,4,2] #[4,2,2,0,4] = #[4,2,0,4,2,0,2,0,4,3,1,0,2,3,1,3] := by native_decide
example : rem5 #[1,0,2,0,1,2,2,3,0,1,4,2] #[4,2,2,0,4] = #[0,3,0,3] := by native_decide
example : gcd5 #[1,0,2,0,1,2,2,3,0,1,4,2] #[4,2,2,0,4] = #[3,1] := by native_decide
example : frob5 #[1,0,2,0,1,2,2,3,0,1,4,2] #[4,2,2,0,4] = #[3,1,1,2] := by native_decide
example : subX #[1,0,2,0,1,2,2,3,0,1,4,2] = #[1,4,2,0,1,2,2,3,0,1,4,2] := by native_decide
example : mul5 #[2] #[3,0,4,0,3,2,3,4,1] = #[1,0,3,0,1,4,1,3,2] := by native_decide
example : rem5 #[2] #[3,0,4,0,3,2,3,4,1] = #[2] := by native_decide
example : gcd5 #[2] #[3,0,4,0,3,2,3,4,1] = #[1] := by native_decide
example : frob5 #[2] #[3,0,4,0,3,2,3,4,1] = #[2] := by native_decide
example : subX #[2] = #[2,4] := by native_decide
example : mul5 #[1] #[2,0,3,4,2,3,1] = #[2,0,3,4,2,3,1] := by native_decide
example : rem5 #[1] #[2,0,3,4,2,3,1] = #[1] := by native_decide
example : gcd5 #[1] #[2,0,3,4,2,3,1] = #[1] := by native_decide
example : frob5 #[1] #[2,0,3,4,2,3,1] = #[1] := by native_decide
example : subX #[1] = #[1,4] := by native_decide
example : mul5 #[1,1,4,4,0,3,0,1,1,3,2] #[2,1,2,3,1] = #[2,3,1,2,1,2,4,2,2,2,2,2,4,4,2] := by native_decide
example : rem5 #[1,1,4,4,0,3,0,1,1,3,2] #[2,1,2,3,1] = #[4,3,4,4] := by native_decide
example : gcd5 #[1,1,4,4,0,3,0,1,1,3,2] #[2,1,2,3,1] = #[1] := by native_decide
example : frob5 #[1,1,4,4,0,3,0,1,1,3,2] #[2,1,2,3,1] = #[2,3,4] := by native_decide
example : subX #[1,1,4,4,0,3,0,1,1,3,2] = #[1,0,4,4,0,3,0,1,1,3,2] := by native_decide
example : mul5 #[0,0,2,1,0,3,2] #[3,2] = #[0,0,1,2,2,4,2,4] := by native_decide
example : rem5 #[0,0,2,1,0,3,2] #[3,2] = #[3] := by native_decide
example : gcd5 #[0,0,2,1,0,3,2] #[3,2] = #[1] := by native_decide
example : frob5 #[0,0,2,1,0,3,2] #[3,2] = #[3] := by native_decide
example : subX #[0,0,2,1,0,3,2] = #[0,4,2,1,0,3,2] := by native_decide
example : mul5 #[1,1,3,2,4,4,4,2,3,3] #[4,1,2,1,4,0,3,3,1] = #[4,0,0,4,4,1,0,3,0,0,3,3,3,4,4,0,2,3] := by native_decide
example : rem5 #[1,1,3,2,4,4,4,2,3,3] #[4,1,2,1,4,0,3,3,1] = #[0,0,2,2,0,2,2,1] := by native_decide
example : gcd5 #[1,1,3,2,4,4,4,2,3,3] #[4,1,2,1,4,0,3,3,1] = #[1] := by native_decide
example : frob5 #[1,1,3,2,4,4,4,2,3,3] #[4,1,2,1,4,0,3,3,1] = #[4,4,1,2,4,4,2] := by native_decide
example : subX #[1,1,3,2,4,4,4,2,3,3] = #[1,0,3,2,4,4,4,2,3,3] := by native_decide
example : mul5 #[] #[1,1,0,3] = #[] := by native_decide
example : rem5 #[] #[1,1,0,3] = #[] := by native_decide
example : gcd5 #[] #[1,1,0,3] = #[2,2,0,1] := by native_decide
example : frob5 #[] #[1,1,0,3] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[2,2,0,4,1,0,3,4] #[0,0,4,0,1,3,1,4] = #[0,0,3,3,2,4,2,4,3,3,0,2,0,1,1] := by native_decide
example : rem5 #[2,2,0,4,1,0,3,4] #[0,0,4,0,1,3,1,4] = #[2,2,1,4,0,2,2] := by native_decide
example : gcd5 #[2,2,0,4,1,0,3,4] #[0,0,4,0,1,3,1,4] = #[1] := by native_decide
example : frob5 #[2,2,0,4,1,0,3,4] #[0,0,4,0,1,3,1,4] = #[2,0,2,1,1,4,1] := by native_decide
example : subX #[2,2,0,4,1,0,3,4] = #[2,1,0,4,1,0,3,4] := by native_decide
example : mul5 #[4,2,4,0,3,1] #[4,1,2,1,4,1,3] = #[1,2,1,2,3,3,2,0,0,2,0,3] := by native_decide
example : rem5 #[4,2,4,0,3,1] #[4,1,2,1,4,1,3] = #[4,2,4,0,3,1] := by native_decide
example : gcd5 #[4,2,4,0,3,1] #[4,1,2,1,4,1,3] = #[1] := by native_decide
example : frob5 #[4,2,4,0,3,1] #[4,1,2,1,4,1,3] = #[3,3,3,1,4,3] := by native_decide
example : subX #[4,2,4,0,3,1] = #[4,1,4,0,3,1] := by native_decide
example : mul5 #[2,2,2,0,2,2,0,3,4] #[1,1] = #[2,4,4,2,2,4,2,3,2,4] := by native_decide
example : rem5 #[2,2,2,0,2,2,0,3,4] #[1,1] = #[3] := by native_decide
example : gcd5 #[2,2,2,0,2,2,0,3,4] #[1,1] = #[1] := by native_decide
example : frob5 #[2,2,2,0,2,2,0,3,4] #[1,1] = #[3] := by native_decide
example : subX #[2,2,2,0,2,2,0,3,4] = #[2,1,2,0,2,2,0,3,4] := by native_decide
example : mul5 #[1,2,3,2,4,4,2,3,1,0,2,4,2] #[3,2,1,4,1,3,2] = #[3,3,4,3,3,4,2,3,3,3,1,2,0,0,2,3,3,4,4] := by native_decide
example : rem5 #[1,2,3,2,4,4,2,3,1,0,2,4,2] #[3,2,1,4,1,3,2] = #[3,1,3,3,2,3] := by native_decide
example : gcd5 #[1,2,3,2,4,4,2,3,1,0,2,4,2] #[3,2,1,4,1,3,2] = #[1] := by native_decide
example : frob5 #[1,2,3,2,4,4,2,3,1,0,2,4,2] #[3,2,1,4,1,3,2] = #[3,3,0,4,3,3] := by native_decide
example : subX #[1,2,3,2,4,4,2,3,1,0,2,4,2] = #[1,1,3,2,4,4,2,3,1,0,2,4,2] := by native_decide
example : mul5 #[2,4,0,4,0,4,1,2,2] #[4,1,3,3] = #[3,3,0,4,1,3,0,1,0,1,2,1] := by native_decide
example : rem5 #[2,4,0,4,0,4,1,2,2] #[4,1,3,3] = #[4,2,1] := by native_decide
example : gcd5 #[2,4,0,4,0,4,1,2,2] #[4,1,3,3] = #[1] := by native_decide
example : frob5 #[2,4,0,4,0,4,1,2,2] #[4,1,3,3] = #[4] := by native_decide
example : subX #[2,4,0,4,0,4,1,2,2] = #[2,3,0,4,0,4,1,2,2] := by native_decide
example : mul5 #[0,0,1,3,2,1,0,1,3] #[0,2] = #[0,0,0,2,1,4,2,0,2,1] := by native_decide
example : rem5 #[0,0,1,3,2,1,0,1,3] #[0,2] = #[] := by native_decide
example : gcd5 #[0,0,1,3,2,1,0,1,3] #[0,2] = #[0,1] := by native_decide
example : frob5 #[0,0,1,3,2,1,0,1,3] #[0,2] = #[] := by native_decide
example : subX #[0,0,1,3,2,1,0,1,3] = #[0,4,1,3,2,1,0,1,3] := by native_decide
example : mul5 #[4,1] #[2,4,3] = #[3,3,1,3] := by native_decide
example : rem5 #[4,1] #[2,4,3] = #[4,1] := by native_decide
example : gcd5 #[4,1] #[2,4,3] = #[1] := by native_decide
example : frob5 #[4,1] #[2,4,3] = #[1,4] := by native_decide
example : subX #[4,1] = #[4] := by native_decide
example : mul5 #[4] #[4,1,2,1] = #[1,4,3,4] := by native_decide
example : rem5 #[4] #[4,1,2,1] = #[4] := by native_decide
example : gcd5 #[4] #[4,1,2,1] = #[1] := by native_decide
example : frob5 #[4] #[4,1,2,1] = #[4] := by native_decide
example : subX #[4] = #[4,4] := by native_decide
example : mul5 #[] #[1,0,1,3,4,0,4,3,1] = #[] := by native_decide
example : rem5 #[] #[1,0,1,3,4,0,4,3,1] = #[] := by native_decide
example : gcd5 #[] #[1,0,1,3,4,0,4,3,1] = #[1,0,1,3,4,0,4,3,1] := by native_decide
example : frob5 #[] #[1,0,1,3,4,0,4,3,1] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[] #[3,3,0,0,2,2,4,1,4] = #[] := by native_decide
example : rem5 #[] #[3,3,0,0,2,2,4,1,4] = #[] := by native_decide
example : gcd5 #[] #[3,3,0,0,2,2,4,1,4] = #[2,2,0,0,3,3,1,4,1] := by native_decide
example : frob5 #[] #[3,3,0,0,2,2,4,1,4] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : mul5 #[0,0,3,2,4,0,3,3,2] #[2,3,4,3,2,2,0,4,2] = #[0,0,1,3,1,4,4,2,2,2,2,3,3,1,3,4,4] := by native_decide
example : rem5 #[0,0,3,2,4,0,3,3,2] #[2,3,4,3,2,2,0,4,2] = #[3,2,4,4,2,3,3,4] := by native_decide
example : gcd5 #[0,0,3,2,4,0,3,3,2] #[2,3,4,3,2,2,0,4,2] = #[1] := by native_decide
example : frob5 #[0,0,3,2,4,0,3,3,2] #[2,3,4,3,2,2,0,4,2] = #[1,3,3,0,2,1,2,2] := by native_decide
example : subX #[0,0,3,2,4,0,3,3,2] = #[0,4,3,2,4,0,3,3,2] := by native_decide
example : mul5 #[] #[0,4,4,4,1,0,4,0,2] = #[] := by native_decide
example : rem5 #[] #[0,4,4,4,1,0,4,0,2] = #[] := by native_decide
example : gcd5 #[] #[0,4,4,4,1,0,4,0,2] = #[0,2,2,2,3,0,2,0,1] := by native_decide
example : frob5 #[] #[0,4,4,4,1,0,4,0,2] = #[] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : rabinChecks #[] = false := by native_decide
example : rabinChecks #[0] = false := by native_decide
example : rabinChecks #[1] = false := by native_decide
example : rabinChecks #[2] = false := by native_decide
example : rabinChecks #[1,0] = false := by native_decide
example : rabinChecks #[1,2] = false := by native_decide
example : rabinChecks #[5,1] = false := by native_decide
example : rabinChecks #[1,1,0] = false := by native_decide
example : rabinChecks #[0,0,1] = false := by native_decide
example : rabinChecks #[1,2,1] = false := by native_decide
example : rabinChecks #[4,0,1] = false := by native_decide
example : factorCheck ⟨#[1], 1, #[⟨#[0,1],0⟩]⟩ = false := by native_decide
example : trim #[0,0,0] = #[] := by native_decide
example : trim #[1,0,0] = #[1] := by native_decide
example : subX #[] = #[0,4] := by native_decide
example : subX #[2] = #[2,4] := by native_decide
end SevenPrimary
