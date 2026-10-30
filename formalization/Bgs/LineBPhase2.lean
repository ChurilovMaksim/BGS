/-
  BGS derandomization, phase 2: finite certificates (core Lean 4, kernel `decide`, no native_decide).
  L1  Theorem D (exact diagonal ramp, odd m): closed form = direct orbit counts (phase2/logs/deficit_odd.log).
  L2  Affine symmetries of the aliased kick symbol on n-torsion: only n = 7 is non-trivial (n <= 60).
  L3  Coefficient facts used in Theorem N (weights of the shifted symbol c~_k = (-1)^k c_k, scaled by 800).
  L4  Theorem N hypotheses for m = 7 and m = 19: h_m prime, lambda has exact order m mod h_m, admissibility (a),(b).
-/
namespace Bgs.LineB.Phase2
/-! ## L1 -/
def pellQ : Nat → Nat
  | 0 => 2
  | 1 => 2
  | n+2 => 2 * pellQ (n+1) + pellQ n
def hm (m : Nat) : Int := (pellQ m / 2 : Nat)
def divs (n : Nat) : List Nat := (List.range (n+1)).filter (fun d => d > 0 && n % d == 0)
def mu : Nat → Int      -- Moebius function by trial factorisation (small n)
  | n => if n == 1 then 1 else
      let ps := (List.range (n+1)).filter (fun p => p ≥ 2 && n % p == 0 && (List.range p).all (fun q => q < 2 || p % q != 0))
      if ps.any (fun p => n % (p*p) == 0) then 0 else (if ps.length % 2 == 0 then 1 else -1)
def aD (d : Nat) : Int := (divs d).foldl (fun s e => s + mu (d / e) * hm e * hm e) 0
def bD (d : Nat) : Int := (divs d).foldl (fun s e => s + mu (d / e) * hm e) 0
def deficitNum (m : Nat) : Int := (divs m).foldl (fun s d => s + 2 * ((m:Int) - d) * aD d + (d:Int) * d * bD d) 0
/-- closed form equals the direct counts sum_{xi in support}(2m - |Gamma xi|) for m = 1,3,5,7,9 -/
theorem thmD_matches_direct :
    [1,3,5,7,9].map deficitNum = [1, 59, 1009, 11675, 112913] := by decide
/-- D_eff = h_m^2 for odd m (support size found numerically: 1, 49, 1681, 57121, 1940449) -/
theorem Deff_odd : [1,3,5,7,9].map (fun m => hm m * hm m) = [1, 49, 1681, 57121, 1940449] := by decide

/-! ## L2  coefficients c_k * 800 as Gaussian integers (re, im) -/
def ck : List (Int × Int × Int) :=   -- (k, re, im)
  [(-9,0,-1),(-8,-20,-2),(-7,360,0),(-6,-20,2),(-5,0,1),(-2,0,2),(-1,40,4),
   (1,40,-4),(2,0,-2),(5,0,-1),(6,-20,-2),(7,360,0),(8,-20,2),(9,0,1)]
def imod (a : Int) (n : Nat) : Nat := (a % (n:Int)).toNat
/-- aliased coefficient vector on Z/n : C_r = sum_{k = r mod n} c_k -/
def alias (n : Nat) : List (Int × Int) :=
  (List.range n).map fun r => ck.foldl (fun (acc : Int × Int) (t : Int × Int × Int) =>
    if imod t.1 n == r then (acc.1 + t.2.1, acc.2 + t.2.2) else acc) (0,0)
def gmul (z w : Int × Int) : Int × Int := (z.1*w.1 - z.2*w.2, z.1*w.2 + z.2*w.1)
def ipow (t : Nat) : Int × Int := match t % 4 with | 0 => (1,0) | 1 => (0,1) | 2 => (-1,0) | _ => (0,-1)
/-- (a, t): theta -> a*theta + t/4 is a symmetry of f on (1/n)Z  iff  C_{r a} = C_r * i^{r t} for all r (a a unit) -/
def isSym (n a t : Nat) : Bool :=
  let C := alias n
  (List.range n).all fun r => (C.getD ((r*a) % n) (0,0)) == gmul (C.getD r (0,0)) (ipow (r*t))
def nontrivSyms (n : Nat) : List (Nat × Nat) :=
  ((List.range n).filter (fun a => Nat.gcd a n == 1)).flatMap fun a =>
    ((List.range 4).filter (fun t => (n*t) % 4 == 0 && !(a % n == 1 % n && t == 0) && isSym n a t)).map (fun t => (a,t))
theorem only_n7_has_symmetries :
    (List.range' 1 60).filter (fun n => !(nontrivSyms n).isEmpty) = [7] := by decide
theorem n7_all_units : nontrivSyms 7 = [(2,0),(3,0),(4,0),(5,0),(6,0)] := by decide

/-! ## L3  shifted weights c~_k = (-1)^k c_k (odd m: support = 1/2 + odd part) -/
def ckt : List (Int × Int × Int) := ck.map fun t => if t.1 % 2 == 0 then t else (t.1, -t.2.1, -t.2.2)
/-- real parts: c~_{+-7} = -360, all other real parts in {-40,-20,0} (so <= 0) -/
theorem shifted_real_parts :
    (ckt.all fun t => if t.1 == 7 || t.1 == -7 then t.2.1 == -360 else (t.2.1 == -40 || t.2.1 == -20 || t.2.1 == 0)) = true := by decide
/-- separation: two hits per k (<= 2 solutions j) of all non-(+-7) terms have total |Re| < |Re c~_7| -/
theorem big_weight_separation :
    2 * ((ckt.filter (fun t => t.1 != 7 && t.1 != -7)).foldl (fun s t => s + t.2.1.natAbs) 0) < 360 := by decide
/-- equal shifted coefficients only within the classes {7,-7},{6,-8},{8,-6},{5,-9},{-5,9}; in particular k=1 is alone -/
def eqClass (k : Int) : List Int := (ckt.filter (fun t => (t.2.1, t.2.2) == ((ckt.find? (fun s => s.1 == k)).map (fun s => (s.2.1,s.2.2))).getD (0,0))).map (·.1)
theorem coefficient_classes :
    [eqClass 1, eqClass (-1), eqClass 7, eqClass 6, eqClass 8, eqClass 5, eqClass 2] =
    [[1], [-1], [-7,7], [-8,6], [-6,8], [-9,5], [2]] := by decide

/-! ## L4  Theorem N hypotheses (m = 7, 19) -/
def primeTD (n b : Nat) : Bool :=   -- trial division by all d < b, with b*b > n
  n ≥ 2 && b * b > n && (List.range b).all (fun d => d < 2 || n % d != 0)
def powModAux : Nat → Nat → Nat → Nat → Nat
  | 0, _, _, _ => 1
  | fuel+1, b, e, h => if e == 0 then 1 % h else
      let r := powModAux fuel (b*b % h) (e/2) h
      if e % 2 == 1 then (b*r) % h else r
def powMod (b e h : Nat) : Nat := powModAux 64 (b % h) e h
def zmul (h : Nat) (x y : Nat × Nat) : Nat × Nat := ((x.1*y.1 + 2*x.2*y.2) % h, (x.1*y.2 + x.2*y.1) % h)
def lamPow (h e : Nat) : Nat × Nat := (List.range e).foldl (fun p _ => zmul h p (3,2)) (1,0)
def lamPows (h m : Nat) : List (Nat × Nat) := (List.range m).map (lamPow h)
def orderExact (h m : Nat) : Bool :=
  lamPow h m == (1,0) && ((lamPows h m).drop 1).all (· != (1,0))
def Kset : List Int := [-9,-8,-7,-6,-5,-2,-1,1,2,5,6,7,8,9]
def condA (h m : Nat) : Bool :=     -- lambda^d is never a ratio k'/k (k != k') mod h
  let P := lamPows h m
  Kset.all fun k => Kset.all fun k' => k == k' ||
    let r := (imod k' h * powMod (imod k h) (h-2) h) % h     -- Fermat inverse (h prime)
    !(P.contains (r, 0))
def condB (h m : Nat) : Bool :=     -- lambda^a + lambda^b = 6 only for {a,b} = {1, m-1}
  let P := lamPows h m
  (List.range m).all fun a => (List.range m).all fun b =>
    let s := ((P.getD a (0,0)).1 + (P.getD b (0,0)).1, (P.getD a (0,0)).2 + (P.getD b (0,0)).2)
    !(s.1 % h == 6 % h && s.2 % h == 0) || (a == 1 && b == m-1) || (a == m-1 && b == 1)
theorem thmN_m7 : (hm 7 == 239 && primeTD 239 16 && orderExact 239 7 && condA 239 7 && condB 239 7 && 239 > 28*7) = true := by decide
set_option maxRecDepth 200000 in
theorem thmN_m19_prime : primeTD 9369319 3062 = true := by decide
theorem thmN_m19_h : hm 19 = 9369319 := by decide
set_option maxRecDepth 20000 in
theorem thmN_m19_order : orderExact 9369319 19 = true := by decide
set_option maxRecDepth 20000 in
theorem thmN_m19_condA : condA 9369319 19 = true := by decide
set_option maxRecDepth 20000 in
theorem thmN_m19_condB : condB 9369319 19 = true := by decide

end Bgs.LineB.Phase2