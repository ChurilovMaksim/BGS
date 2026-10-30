namespace Bgs.LineB.Derand
/-
  BGS derandomization: finite exact certificates (core Lean 4, kernel `decide`, no native_decide).
  Key Lemma Q (every fixed m): with H_m = 6I - C - C^T (cyclic; H_1=[4], H_2=[[6,-2],[-2,6]]),
  X_m := y_m * G_Nm + (D_m/2) * G_beta, G_Nm[i][j] = x_{|i-j|}, G_beta[i][j] = -y_{|i-j|} (i≠j), 0 (i=j),
  we have  H_m * X_m = D_m * I,  D_m = 2(x_m - 1) = Tr S^m - 2.
  Hence 2 n^T H^{-1} n = (2 y_m/D_m) Nm(alpha_n) + beta(n) exactly (Theorem 1 phase identity).
-/
def pellX : Nat → Int
  | 0 => 1
  | n+1 => 3 * pellX n + 8 * pellY n
where pellY : Nat → Int
  | 0 => 0
  | n+1 => pellX n + 3 * pellY n

def pellY (n : Nat) : Int := pellX.pellY n

def Dm (m : Nat) : Int := 2 * (pellX m - 1)

def dist (_m i j : Nat) : Nat :=
  let d := if i ≤ j then j - i else i - j
  d   -- linear distance |i-j| (Toeplitz form; not cyclic)

def Hm (m : Nat) (i j : Nat) : Int :=
  if m = 1 then 4
  else if m = 2 then (if i = j then 6 else -2)
  else (if i = j then 6 else 0) - (if (j + m - i) % m = 1 then 1 else 0) - (if (i + m - j) % m = 1 then 1 else 0)

def Xm (m : Nat) (i j : Nat) : Int :=
  let d := dist m i j
  pellY m * pellX d + (Dm m / 2) * (if i = j then 0 else - pellY d)

def matmulEntry (m : Nat) (A B : Nat → Nat → Int) (i j : Nat) : Int :=
  (List.range m).foldl (fun s k => s + A i k * B k j) 0

def checkQ (m : Nat) : Bool :=
  (List.range m).all fun i => (List.range m).all fun j =>
    matmulEntry m (Hm m) (Xm m) i j == (if i = j then Dm m else 0)

theorem lemmaQ_1  : checkQ 1  = true := by decide
theorem lemmaQ_2  : checkQ 2  = true := by decide
theorem lemmaQ_3  : checkQ 3  = true := by decide
theorem lemmaQ_4  : checkQ 4  = true := by decide
theorem lemmaQ_5  : checkQ 5  = true := by decide
theorem lemmaQ_6  : checkQ 6  = true := by decide
theorem lemmaQ_7  : checkQ 7  = true := by decide
theorem lemmaQ_8  : checkQ 8  = true := by decide
theorem lemmaQ_9  : checkQ 9  = true := by decide
theorem lemmaQ_10 : checkQ 10 = true := by decide
theorem lemmaQ_12 : checkQ 12 = true := by decide

/-- control: a deliberately wrong variant (sign of beta-part flipped) must fail -/
def XmBad (m : Nat) (i j : Nat) : Int :=
  let d := dist m i j
  pellY m * pellX d + (Dm m / 2) * (if i = j then 0 else pellY d)
def checkQBad (m : Nat) : Bool :=
  (List.range m).all fun i => (List.range m).all fun j =>
    matmulEntry m (Hm m) (XmBad m) i j == (if i = j then Dm m else 0)
theorem lemmaQ_bad_fails : checkQBad 5 = false := by decide

/-- D_m values and Pell identity x^2 - 8 y^2 = 1 -/
theorem D_values : (List.range 9).map Dm = [0, 4, 32, 196, 1152, 6724, 39200, 228484, 1331712] := by decide
theorem pell_id : (List.range 30).all (fun m => pellX m * pellX m - 8 * pellY m * pellY m == 1) = true := by decide

/-- reduced fraction y_m/(x_m-1) = y'/g' : the period of the limit in N (g') and the numerator y' -/
def gp (m : Nat) : Nat := (pellX m - 1).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat
def yp (m : Nat) : Nat := (pellY m).toNat / Nat.gcd (pellX m - 1).toNat (pellY m).toNat
theorem gprime_values : (List.range' 1 10).map gp = [2, 8, 14, 48, 82, 280, 478, 1632, 2786, 9512] := by decide
theorem yprime_values : (List.range' 1 10).map yp = [1, 3, 5, 17, 29, 99, 169, 577, 985, 3363] := by decide

/-- L = mult. by lambda on Z[lambda] in basis (1,lambda): L = [[0,-1],[1,6]]; d1 = gcd of entries of L^m - I.
    Check h_m | d1 (odd m, h_m = g'_m/2 = NSW numbers) and P_m | d1 (even m), used for the support/fixed-point bounds. -/
def Lpow : Nat → Int × Int × Int × Int     -- (a,b,c,d) = [[a,b],[c,d]]
  | 0 => (1, 0, 0, 1)
  | n+1 => let (a,b,c,d) := Lpow n; (b, -a + 6*b, d, -c + 6*d)   -- right-multiply by L
def d1 (m : Nat) : Nat := let (a,b,c,d) := Lpow m; Nat.gcd (Nat.gcd (a-1).natAbs b.natAbs) (Nat.gcd c.natAbs (d-1).natAbs)
theorem d1_values : (List.range' 1 10).map d1 = [1, 2, 7, 12, 41, 70, 239, 408, 1393, 2378] := by decide
theorem det_check : (List.range' 1 12).all (fun m => let (a,b,c,d) := Lpow m; (a-1)*(d-1) - b*c == - Dm m) = true := by decide

/-! ### Added: structure of V = O/(lambda^m - 1) used in the |Rad| = |V[4]| <= 16 bound and the fixed-point bounds -/
def pellP : Nat → Int          -- Pell numbers P_0=0, P_1=1, P_{n+1} = 2P_n + P_{n-1}
  | 0 => 0
  | 1 => 1
  | n+2 => 2 * pellP (n+1) + pellP n
def pellQ : Nat → Int          -- companion Pell numbers Q_0=2, Q_1=2
  | 0 => 2
  | 1 => 2
  | n+2 => 2 * pellQ (n+1) + pellQ n

/-- D_m = Q_m^2 (m odd), D_m = 8 P_m^2 (m even), for 1 <= m <= 20 -/
theorem D_closed : (List.range' 1 20).all (fun m =>
    if m % 2 = 1 then Dm m == pellQ m * pellQ m else Dm m == 8 * pellP m * pellP m) = true := by decide

/-- (Q_m/2) | d1 (m odd), P_m | d1 (m even), m <= 14; hence d2 = D/d1 <= 2 sqrt D (odd), sqrt(8D) (even) -/
theorem d1_divisible : (List.range' 1 14).all (fun m =>
    if m % 2 = 1 then (d1 m : Int) % (pellQ m / 2) == 0 else (d1 m : Int) % pellP m == 0) = true := by decide

/-- |Rad| = |V[4]| = gcd(4,d1) * gcd(4,d2); D_eff = D/|Rad| equals the values found numerically (logs/analyze_B_actual.log) -/
def d2 (m : Nat) : Nat := (Dm m).toNat / d1 m
def radSize (m : Nat) : Nat := Nat.gcd 4 (d1 m) * Nat.gcd 4 (d2 m)
theorem d1d2 : (List.range' 1 12).all (fun m => (d1 m * d2 m : Int) == Dm m) = true := by decide
theorem Deff_values : (List.range' 1 8).map (fun m => (Dm m).toNat / radSize m)
    = [1, 4, 49, 72, 1681, 4900, 57121, 83232] := by decide

#print axioms lemmaQ_1
#print axioms lemmaQ_2
#print axioms lemmaQ_3
#print axioms lemmaQ_4
#print axioms lemmaQ_5
#print axioms lemmaQ_6
#print axioms lemmaQ_7
#print axioms lemmaQ_8
#print axioms lemmaQ_9
#print axioms lemmaQ_10
#print axioms lemmaQ_12
#print axioms lemmaQ_bad_fails
#print axioms D_values
#print axioms pell_id
#print axioms gprime_values
#print axioms yprime_values
#print axioms d1_values
#print axioms det_check
#print axioms D_closed
#print axioms d1_divisible
#print axioms d1d2
#print axioms Deff_values
end Bgs.LineB.Derand