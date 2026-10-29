set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option Elab.async false

namespace Bgs.LineCEncounter

/-!
# Line C: finite algebraic core of the first off-diagonal (Sieber–Richter-type) term

Kernel-`decide` certificates for
`mathematics/fixed-map/random_phase_encounter_pairs.md`
(BGS-TRACE-144, BGS-TRACE-145 and BGS-TRACE-146: finite instances only):

* `aut5`, `aut6`: exactly `2m` permutations of the positions preserve the
  undirected edge multiset of the cyclic walk `0,1,…,m-1` (the diagonal / dihedral term).
* `rank2_class6`: for `m = 6`, among the 60 undirected Hamiltonian cycles `H` on `{0,…,5}`
  (written as sequences starting with `0`), all `3×3` minors of `A_C - A_H` vanish
  (i.e. `rank ≤ 2`) exactly when `H = C`, `|C \ H| = 2` (a 2-opt / loop reversal), or
  `H` is `C` with two vertices at cyclic distance `3` exchanged (a "swap").  Counts
  `1 + 9 + 3`, matching `m(m-3)/2 = 9`, `m(m-5)/2 = 3`.
* `fig8_6`: for `m = 6`, merging positions `0` and `k` (`k = 1,2,3`; all other pairs follow by
  rotation/reflection), the number of distinct words with the same edge multiset equals
  `m·d(k)·d(m-k)`, `d(l) = if l ≥ 3 then 2 else 1` (Eulerian circuits of a figure eight).
* `coeff_identity`: `2m(m(m-3)/2 + m(m-5)/2) - (m^2/2)(4m-12) = -2m^2` for `5 ≤ m ≤ 300`.
* `hyp_counts`: `#{(u,v) ∈ F_p^2 : uv = k}` is `2p-1` for `k = 0` and `p-1` otherwise
  (`p = 5, 7, 11, 13`), which gives `Σ_{u,v} e_p(c u v) = p`.
* `exact_7_3`, `exact_11_3`, `exact_13_3`: the aggregated Gauss-sum count
  vectors `A_k` of Proposition 2; with `A_k` constant on `k ≠ 0` they certify
  `E|Tr U^3|^2 = 235/49` at `N = 7`, `631/121` at `N = 11`, `901/169` at `N = 13` (given the on-paper reduction of Prop. 2).

Not formalised: the probabilistic reduction (Theorem 1 / Prop. 2), Gauss-sum evaluation,
the general-`m` rank classification (Lemma 4) and the asymptotic bound.
-/

/-! ## lists, permutations, edge multisets -/

def ins (x : Nat) : List Nat → List Nat
  | [] => [x]
  | y :: ys => if x ≤ y then x :: y :: ys else y :: ins x ys

def isort : List Nat → List Nat
  | [] => []
  | x :: xs => ins x (isort xs)

def insertAll (x : Nat) : List Nat → List (List Nat)
  | [] => [[x]]
  | y :: ys => (x :: y :: ys) :: (insertAll x ys).map (fun l => y :: l)

def perms : List Nat → List (List Nat)
  | [] => [[]]
  | x :: xs => (perms xs).flatMap (insertAll x)

def edgeCode (a b : Nat) : Nat := if a ≤ b then a * 64 + b else b * 64 + a

/-- sorted list of undirected edges (encoded) of the cyclic walk `s` -/
def edges (s : List Nat) : List Nat :=
  isort ((List.range s.length).map
    (fun j => edgeCode (s.getD j 0) (s.getD ((j + 1) % s.length) 0)))

def sameEdges (s t : List Nat) : Bool := edges s == edges t

/-- relabel the word `x` by the permutation `σ` of positions: `y_j = x_{σ j}` -/
def applyPerm (x σ : List Nat) : List Nat := σ.map (fun j => x.getD j 0)

def autCount (m : Nat) : Nat :=
  let x := List.range m
  ((perms (List.range m)).filter (fun σ => sameEdges (applyPerm x σ) x)).length

theorem aut5 : autCount 5 = 10 := by decide
theorem aut6 : autCount 6 = 12 := by decide

/-! ## rank-2 classification at m = 6 -/

def cnt (l : List Nat) (c : Nat) : Int := ((l.filter (· == c)).length : Int)

/-- the matrix `B = A_C - A_H` as a list of rows (off-diagonal entries; diagonal `0`) -/
def Bmat (n : Nat) (ec eh : List Nat) : List (List Int) :=
  (List.range n).map fun a => (List.range n).map fun b =>
    if a == b then 0 else cnt ec (edgeCode a b) - cnt eh (edgeCode a b)

def ent (B : List (List Int)) (i j : Nat) : Int := (B.getD i []).getD j 0

def det3 (B : List (List Int)) (i j k r s t : Nat) : Int :=
  ent B i r * (ent B j s * ent B k t - ent B j t * ent B k s)
  - ent B i s * (ent B j r * ent B k t - ent B j t * ent B k r)
  + ent B i t * (ent B j r * ent B k s - ent B j s * ent B k r)

def triples (n : Nat) : List (Nat × Nat × Nat) :=
  (List.range n).flatMap fun i => (List.range n).flatMap fun j =>
    (List.range n).filterMap fun k => if i < j ∧ j < k then some (i, j, k) else none

/-- all 3×3 minors vanish, i.e. rank ≤ 2 (over ℚ) -/
def rankLe2 (n : Nat) (ec eh : List Nat) : Bool :=
  let B := Bmat n ec eh
  let T := triples n
  T.all fun r1 => T.all fun r2 => det3 B r1.1 r1.2.1 r1.2.2 r2.1 r2.2.1 r2.2.2 == 0

/-- undirected Hamiltonian cycles on `{0,…,n-1}` as sequences `0 :: π` with `π.head < π.last` -/
def hamCycles (n : Nat) : List (List Nat) :=
  ((perms ((List.range n).drop 1)).filter
    (fun π => π.headD 0 < π.getLastD 0)).map (fun π => 0 :: π)

/-- `|C \ H|` -/
def diffSize (ec eh : List Nat) : Nat := (ec.filter (fun e => !(eh.contains e))).length

def swapSeq (s : List Nat) (a b : Nat) : List Nat :=
  s.map (fun v => if v == a then b else if v == b then a else v)

def cycDist (m a b : Nat) : Nat :=
  let d := if a ≤ b then b - a else a - b
  min d (m - d)

def isSwap (m : Nat) (eh : List Nat) : Bool :=
  (List.range m).any fun a => (List.range m).any fun b =>
    a < b && cycDist m a b ≥ 3 && edges (swapSeq (List.range m) a b) == eh

/-- classification predicate is equivalent to rank ≤ 2, for every Hamiltonian cycle -/
def classOK (m : Nat) : Bool :=
  let ec := edges (List.range m)
  (hamCycles m).all fun h =>
    let eh := edges h
    rankLe2 m ec eh == (eh == ec || diffSize ec eh == 2 || isSwap m eh)

def countRank2 (m : Nat) (k : Nat) : Nat :=
  let ec := edges (List.range m)
  ((hamCycles m).filter fun h =>
    let eh := edges h; rankLe2 m ec eh && diffSize ec eh == k).length

theorem ham6 : (hamCycles 6).length = 60 := by decide
theorem rank2_class6 : classOK 6 = true := by decide
theorem rank2_counts6 :
    countRank2 6 0 = 1 ∧ countRank2 6 2 = 9 ∧ countRank2 6 4 = 3 := by decide

/-! ## figure-eight (one merged pair) zero-form count at m = 6

By rotation and reflection of the positions it suffices to merge positions `0` and `k`,
`k = 1, 2, 3`.  We count distinct words `y` (rearrangements of the merged word) with the same
edge multiset; the number of permutations `σ` is twice this (stabiliser of the merged pair). -/

def d (l : Nat) : Nat := if l ≥ 3 then 2 else 1

def mergedWord (m k : Nat) : List Nat := (List.range m).map (fun j => if j == k then 0 else j)

/-- distinct elements of a list -/
def nub : List Nat → List Nat
  | [] => []
  | x :: xs => if xs.contains x then nub xs else x :: nub xs

/-- all distinct rearrangements of the multiset `l` (fuel `n = l.length`) -/
def msPerms : Nat → List Nat → List (List Nat)
  | 0, _ => [[]]
  | n + 1, l => (nub l).flatMap fun a => (msPerms n (l.erase a)).map (a :: ·)

def fig8Words (m k : Nat) : Nat :=
  let x := mergedWord m k
  ((msPerms m x).filter (fun y => sameEdges y x)).length

/-- sanity: `msPerms` produces `6!/2 = 360` distinct words for a merged word of length 6 -/
theorem msPerms_count : (msPerms 6 (mergedWord 6 2)).length = 360 := by decide

theorem fig8_6 :
    fig8Words 6 1 = 6 * d 1 * d 5 ∧ fig8Words 6 2 = 6 * d 2 * d 4 ∧
    fig8Words 6 3 = 6 * d 3 * d 3 := by decide

/-! ## coefficient identity -/

def c1formula (m : Int) : Int :=
  2 * m * (m * (m - 3) / 2 + m * (m - 5) / 2) - (m * m * (4 * m - 12)) / 2

theorem coeff_identity :
    (List.range 296).all (fun j => c1formula ((j : Int) + 5) == -2 * ((j : Int) + 5) ^ 2) = true := by
  decide

/-! ## hyperbolic-plane counts -/

def hypCount (p k : Nat) : Nat :=
  ((List.range p).flatMap fun u => (List.range p).filter fun v => (u * v) % p == k).length

def hypOK (p : Nat) : Bool :=
  hypCount p 0 == 2 * p - 1 && (List.range p).all (fun k => k == 0 || hypCount p k == p - 1)

theorem hyp_counts : (hypOK 5 && hypOK 7 && hypOK 11 && hypOK 13) = true := by decide

/-! ## exact small values via Proposition 2

`E = N^{-m} Σ_ρ W(ρ) Σ_σ Σ_z e_N(c Q_{ρ,σ}(z))`, `c = 4^{-1} mod N`.  We list the set partitions
of the positions as label words, with `W` scaled by `den`, and compute the count vector
`A_k = Σ_ρ den·W(ρ) Σ_σ #{z : c Q_{ρ,σ}(z) ≡ k}`. -/

/-- all vectors in `{0..p-1}^n` -/
def vecs (p : Nat) : Nat → List (List Nat)
  | 0 => [[]]
  | n + 1 => (vecs p n).flatMap fun v => (List.range p).map fun a => a :: v

def walkSum (p : Nat) (w : List Nat) (z : List Nat) : Nat :=
  ((List.range w.length).map fun j =>
    z.getD (w.getD j 0) 0 * z.getD (w.getD ((j + 1) % w.length) 0) 0).foldl (· + ·) 0 % p

/-- `#{z : c (P_x(z) - P_y(z)) ≡ k}` summed over σ, for one partition word `x` with `n` labels -/
def countVec (p c n : Nat) (x : List Nat) : List Nat :=
  let ys := (perms (List.range x.length)).map (applyPerm x)
  let zs := vecs p n
  (List.range p).map fun k =>
    (ys.map fun y => (zs.filter fun z =>
      (c * (walkSum p x z + p - walkSum p y z)) % p == k).length).foldl (· + ·) 0

def addVec (a b : List Int) : List Int := (List.range a.length).map fun k => a.getD k 0 + b.getD k 0

def aggregate (p c : Nat) (parts : List (List Nat × Nat × Int)) : List Int :=
  parts.foldl (fun acc t =>
    let cv := countVec p c t.2.1 t.1
    addVec acc ((List.range p).map fun k => t.2.2 * (cv.getD k 0 : Int)))
    ((List.range p).map fun _ => 0)

/-- set partitions of 3 positions: (label word, #labels, 6·W) ; W = 1, -1/2, 2/3 -/
def parts3 : List (List Nat × Nat × Int) :=
  [([0,1,2], 3, 6), ([0,0,1], 2, -3), ([0,1,0], 2, -3), ([0,1,1], 2, -3), ([0,0,0], 1, 4)]

def constOff (A : List Int) : Bool := (A.drop 1).all (· == A.getD 1 0)

/-- `E·den·p^m = A_0 - A_1` -/
def certVal (A : List Int) : Int := A.getD 0 0 - A.getD 1 0

theorem exact_7_3 :
    constOff (aggregate 7 2 parts3) = true ∧ certVal (aggregate 7 2 parts3) = 235 * 6 * 7 := by
  decide

theorem exact_11_3 :
    constOff (aggregate 11 3 parts3) = true ∧ certVal (aggregate 11 3 parts3) = 631 * 6 * 11 := by
  decide

theorem exact_13_3 :
    constOff (aggregate 13 10 parts3) = true ∧ certVal (aggregate 13 10 parts3) = 901 * 6 * 13 := by
  decide

end Bgs.LineCEncounter
