# Wave 12, task 4 — G3: one common π across components

## Status in one paragraph

**G3 is NOT proved as a theorem, and it is NOT pure combinatorics.**
Two things are now sharp. (1) *Negative, proved:* component π-sets plus
the global multiset (i.e. a common σ) do **not** imply a common π, in
general — explicit abstract counterexamples for t = 2 and t = 4 (§2).
Any proof of G3 for Fix vectors must therefore use Fix structure, exactly
as Lemma S in wave 11 task 3 needed Fix structure. (2) *Positive,
numerically strong:* the Fix-structure statement that would close the
mod-p part of G3 — the pair-contingency lemma (§3) — holds in every
tested case (3 settings, 670 800 preserved (d₁,d₂) cases, 0 bad), and a
first full-vector check at m = 12 (all five prime powers
simultaneously, 2 000 000 random CRT vectors, 30 838 colliding pairs)
finds 0 π-empty pairs and 0 exact per-class failures among 30 838
repeat samples (§4). The remaining
gap is precisely stated in §5: a proof of the pair-contingency lemma,
plus the already-open prime-power lifts G1/G2 (per-component π_q for
q = p^e, e ≥ 2, and for p = 2) — G3 at prime-power level cannot be closed
before G1/G2 give the component π_q to combine.

## 1. What G3 is (marginal version, distinguished from exact joint)

Fix m, t = gcd(m,4), classes O_r = {i : i ≡ r (mod t)}, D_t acting by
r ↦ r+b and r ↦ −r+b. For a pair y, y′ ∈ Fix_m with the same exact
multiset, and for each prime power q ‖ D_m, let

  Π_q = {π ∈ D_t : per-class multisets of y′ mod q equal those of y
         mod q composed with π}.

Per-component lemmas (if proved) say Π_q ≠ ∅ for each q. **G3 (marginal)**
is: ∩_q Π_q ≠ ∅. This is necessary for the exact per-class lemma (an
exact π lies in every Π_q) but strictly weaker than it: exact per-class
also needs the joint CRT pairing inside each class to match, not only
the marginals. This note proves nothing about the joint pairing beyond
the m = 12 random check in §4 (which does test exact per-class, and
passes). All "π" below are marginal π's unless stated otherwise.

## 2. Negative result: pure combinatorics does NOT give G3

Hypotheses: (i) Π_{q1}, Π_{q2} nonempty for two components,
(ii) y, y′ have the same global multiset (equivalently, some σ ∈ S_m
with y′ = y ∘ σ). Conclusion "∩ Π_q ≠ ∅" is **false** for arbitrary
sequences. Hence any G3 proof must use that y, y′ are Fix sequences
(recurrence + periodicity), not just their component π-sets and σ.

### 2a. t = 2 (m ≡ 2 mod 4 shape; class sizes 3, padded from a 2+2 core)

Values are types (r₁, r₂) ∈ {0,1}², r₁ = residue mod q₁, r₂ = residue
mod q₂. Counts C[r][type] for y, C′ for y′ (script
`wave12_g3_abstract.py`):

  C  = class 0: {(1,1)×2, (0,0)},  class 1: {(0,1), (1,0), (0,0)}
  C′ = class 0: {(0,1), (1,1), (0,0)}, class 1: {(1,0), (1,1), (0,0)}

Global multisets coincide: {(1,1)×2, (0,1), (1,0), (0,0)×2} in both.
Aggregating by r₁ (first coordinate):
  y:  class 0 → [0:1, 1:2], class 1 → [0:2, 1:1]
  y′: class 0 → [0:2, 1:1], class 1 → [0:1, 1:2]
so Π_{q1} = {swap} only. Aggregating by r₂ (second coordinate):
  y:  class 0 → [0:1, 1:2], class 1 → [0:2, 1:1]
  y′: class 0 → [0:1, 1:2], class 1 → [0:2, 1:1]
so Π_{q2} = {id} only. Π_{q1} ∩ Π_{q2} = ∅. As arbitrary sequences this
is a genuine G3 counterexample (realise C, C′ literally as sequences
of length 6, classes = even/odd positions). It is not a Fix
counterexample: the residue patterns (0/1 only) are not Fix patterns
in general, and §3–§4 show Fix sequences avoid this configuration.

### 2b. t = 4 (random search, script `wave12_g3_abstract_t4.py`, trial 273)

Classes 0..3, class size 3, types (r₁,r₂) ∈ {0,1}², counts by type
index (0=(0,0), 1=(0,1), 2=(1,0), 3=(1,1)):

  C  = [[1,1,1,0], [2,0,1,0], [1,2,0,0], [1,2,0,0]]
  C′ = [[0,2,1,0], [1,1,1,0], [3,0,0,0], [1,2,0,0]]

Column sums coincide (check: type 0: 1+2+1+1 = 0+1+3+1 = 5; type 1:
1+0+2+2 = 2+1+0+2 = 5; type 2: 1+1+0+0 = 1+1+0+0 = 2; type 3: 0).
Aggregating by r₁: y rows [2,1],[2,1],[3,0],[3,0]; y′ rows
[2,1],[2,1],[3,0],[3,0]; hence Π_{q1} = {id, (1,0,3,2)} (id and the
reflection r ↦ −r+1). Aggregating by r₂: y rows [2,1],[3,0],[1,2],
[1,2]; y′ rows [1,2],[2,1],[3,0],[1,2]; hence Π_{q2} = {(3,0,1,2)}
(the shift r ↦ r−1) only. Intersection is empty. Again, arbitrary
sequences only — not Fix sequences.

Consequence: the "σ + component π's" input is insufficient, in the
same sense as wave 11 task 3 §5 for Lemma S. A G3 proof must invoke a
Fix property that rules out the §2 configurations. §3 isolates the
property that does the work at mod-p level.

## 3. The Fix property that does the work: pair-contingency (mod p)

### 3a. Setup (wave 11 task 2, mod-p layer)

Let p be odd, p | D_m. Then α^m = 1 in R/p (R = ℤ[√2], α = 3+2√2),
every recurrence sequence mod p is m-periodic, and every such sequence
is y_j = Tr(A α^j) for a unique A ∈ R/p (α−β has norm −32, a unit
mod p). Wave 11 task 2 Step 1–2 shows: the global multiset mod p
determines (N, Tr(A^L)) (L = order of α mod p), and then A′ (for a
second sequence with the same global multiset mod p) satisfies
A′ = A α^k or A′ = Ā α^k for some k. Hence, as sequences,

  y′ ≡ d_p(y) (mod p) for some d_p ∈ D_m, d_p(j) = j+k or −j+k.

So at mod-p level the component data is stronger than a π-set: it is
a dihedral sequence operation d_p, whose induced class map π_{d_p} ∈
Π_p. G3 at mod-p level is therefore: for two odd primes p₁, p₂ | D_m,
with d₁, d₂ the operations above, show Π_{p₁} ∩ Π_{p₂} ≠ ∅, where
Π_{pᵢ} is the π-set for the pair (y, dᵢ(y)) mod pᵢ.

### 3b. Pair-contingency lemma (statement to be proved; §3c is evidence)

Let a (mod p₁), b (mod p₂) be recurrence sequences of length m, and
d₁, d₂ ∈ D_m. Suppose the pair multiset is preserved:

  {(a_{d₁(j)}, b_{d₂(j)}) : j ∈ ℤ/m} = {(a_j, b_j) : j ∈ ℤ/m}   (∗)

(as multisets of pairs). Let Π₁, Π₂ be the π-sets for (a, d₁(a)) and
(b, d₂(b)) respectively (per-class multisets mod p₁, p₂). Then

  Π₁ ∩ Π₂ ≠ ∅.

Why (∗) is the right hypothesis: if y, y′ are global Fix sequences
with the same exact multiset, then reducing mod p₁p₂ gives pair
sequences (a_j, b_j) for y and (a_{d₁(j)}, b_{d₂(j)}) for y′ (by §3a),
and exact multiset equality implies (∗). So the lemma, if proved,
gives G3 across any two odd primes. (For p = 2 the representation
fails — that is G2, not addressed here; for p = 3 at prime-power level
the P3′/Lemma-S machinery of wave 11 task 3 is the analogue, with
Lemma S still open.)

Proof sketch (not completed — the gap is named at the end of this
subsection). Put A ∈ R/(p₁p₂) for the CRT pair (A₁, A₂) (R/(p₁p₂) ≅
R/p₁ × R/p₂ is a product of fields, α^m = 1 there). The pair values
are Tr(A α^j) ∈ ℤ/(p₁p₂) reduced mod p₁, p₂. The mixed sequence in
(∗) has components Tr(A₁ α^{σ₁j}·(shift)) and Tr(A₂ α^{σ₂j}·(shift))
with σᵢ = +1 (shift dᵢ) or −1 (reflection dᵢ). The claim to prove is:
(∗) forces (σ₁, k₁) and (σ₂, k₂) to be compatible — i.e. there is a
common shift/reflection k, σ such that (A₁ α^{k₁}, A₂ α^{k₂}) is
(A₁, A₂)·α^k or its conjugate, up to elements stabilising A₁ resp.
A₂ (ω with Aᵢω = Aᵢ). If σ₁ ≠ σ₂ or the shifts are incompatible, the
mixed orbit {(A₁ α^{σ₁j}, A₂ α^{σ₂j})} has a different trace-pair
distribution from the diagonal orbit, because the Step-1 polynomial
identity over the product of fields R/(p₁p₂) — ∏_{z∈⟨α⟩}(X −
Tr(Az)) = C·(Tr(A^L) − V_L(X, N)) applied componentwise — determines
(A₁, A₂) from the pair distribution up to exactly this common
shift/conjugation freedom. Once a common (σ, k) is obtained, its
induced class map π lies in both Π₁ and Π₂ up to the stabilisers of
the per-class multisets (e.g. if A₁ is α²-periodic, shift by 2 is in
Stab₁, so π_{d₁} and π_{d₂} differing by 2 is harmless). **Gap:** the
step "pair trace distribution determines (A₁, A₂) up to common
shift/conjugation" is stated, not proved, here. It is the precise
remaining lemma for mod-p G3. Its numerical support is §3c, and it is
strictly stronger than the §2 combinatorics because it uses that
a_j, b_j are traces of the same index j under α^j (recurrence), which
the §2 abstract sequences violate.

### 3c. Numerical verification of pair-contingency (exact, all cases)

Script `wave12_g3_pair_contingency.py`: enumerate ALL recurrence
sequences mod p₁, mod p₂ (p² each, periodicity asserted), ALL
(d₁, d₂) ∈ D_m × D_m, test (∗) by sorted pair multisets, and for every
preserved case compute Π₁, Π₂ exactly and check intersection.
"Preserved" counts (d₁, d₂) pairs preserving the pair multiset; they
are numerous because recurrence sequences have many value repetitions
and symmetries — the test is therefore not vacuous.

  m=6,  p₁=5,  p₂=7:  pairs 25×49=1225, preserved 79 632, BAD 0
  m=8,  p₁=3,  p₂=17: pairs 9×289=2601, preserved 272 640, BAD 0
  m=12, p₁=5,  p₂=7:  pairs 25×49=1225, preserved 318 528, BAD 0

Total: 670 800 preserved cases, 0 with Π₁ ∩ Π₂ = ∅. Caveat: these are
mod-p recurrence pairs, not Fix-mod-D pairs — a mod-p sequence need
not lift to a Fix sequence mod p^e (the lift image is a proper subset,
see §5). So §3c supports the mod-p lemma, not exact G3 by itself.

## 4. Full-vector check at m = 12 (all prime powers at once)

Script `wave12_g3_random_m12.py`: D₁₂ = 1536796800 = 2⁷·3⁴·5²·7²·11².
Enumerate Fix₁₂ mod q for q ∈ {128, 81, 25, 49, 121} (sizes = q each,
by the wave 11 component solver), sample random CRT combinations
(uniform component choices), combine by CRT, group by sorted exact
multiset, and for every colliding pair check (i) ∩_q Π_q ≠ ∅ and
(ii) exact per-class canonical form constant. (An exact π would lie in
every Π_q, so (i) is implied by (ii); (i) is reported separately
because G3 is the marginal statement.)

  samples 2 000 000, distinct multisets 1 969 162,
  repeat samples 30 838 (each checked against the first sample with
  that multiset), π-empty pairs 0, exact per-class failures 0.

This is the first check of G3/exact per-class at m = 12 with all five
prime powers present simultaneously (previous joint searches covered
(2,3) and (2,3,5) subclasses with other components zero). It does not
prove anything: random sampling covers ~0.13% of the 1.54·10⁹ Fix
vectors, and colliding pairs are a biased subset (fibres with larger
multiplicity are oversampled). It does rule out any "generic"
counterexample at m = 12: a π-empty pair would have had to be rare
(< ~1/30 838 of colliding pairs, at this sample size) or absent.

## 5. What remains for G3, precisely

1. **Lemma PC (§3b):** prove that pair trace distribution determines
   (A₁, A₂) up to common shift/conjugation (mod p₁, p₂). This closes
   mod-p G3 (common π across all odd primes). Numerical support: §3c.
2. **G1 (odd prime-power lift):** per-component π_q for q = p^e, e ≥ 2.
   Mod-p π's do not automatically lift to mod p^e π's with the same π
   (α^m = 1 + ε, ε² = 0 mod p^e). Until G1 gives Π_q, there is nothing
   to combine at prime-power level for odd p.
3. **G2 (2-primary):** per-component π for q = 2^a at per-class
   multiset level (the wave 11 task 1 pattern lemma gives this for
   patterns mod 2^a — it should be cited as the 2-component input,
   not reproved here).
4. **2-vs-odd compatibility at prime-power level:** the wave 11 task 3
   compatibility (π₂ vs π₃) is for class sums mod D, modulo Lemma S
   (stabiliser adjustment, verified at P = 8, 16, not proved, and not
   pure combinatorics). The per-class-multiset analogue of Lemma S
   for (pattern, odd) pairs is open and is the same kind of gap as PC.
5. **Joint pairing (beyond G3):** even with a common marginal π, exact
   per-class needs the CRT pairing inside each class to match; §4
   checks it at m = 12 by sampling only.

No change to the BGS repository; no Lean built. Nothing in this note
is claimed as a Lean theorem; §3b is a proof sketch with a named gap,
§3c/§4 are exact-arithmetic verifier artefacts.

## Files

- This note: [wave12_g3_common_pi.md](sandbox://workspace/bgs-breakthrough/methods/wave12_g3_common_pi.md)
- Abstract obstructions: [wave12_g3_abstract.py](sandbox://workspace/bgs-breakthrough/methods/wave12_g3_abstract.py) (t=2),
  [wave12_g3_abstract_t4.py](sandbox://workspace/bgs-breakthrough/methods/wave12_g3_abstract_t4.py) (t=4)
- Pair-contingency test: [wave12_g3_pair_contingency.py](sandbox://workspace/bgs-breakthrough/methods/wave12_g3_pair_contingency.py)
- Full m=12 random check: [wave12_g3_random_m12.py](sandbox://workspace/bgs-breakthrough/methods/wave12_g3_random_m12.py)
- Prior notes used: [wave11_perclass_proof.md](sandbox://workspace/bgs-breakthrough/methods/wave11_perclass_proof.md),
  [wave11_perclass_pattern_proof.md](sandbox://workspace/bgs-breakthrough/methods/wave11_perclass_pattern_proof.md),
  [wave11_task3_pi2pi3_compatibility.md](sandbox://workspace/bgs-breakthrough/methods/wave11_task3_pi2pi3_compatibility.md)
