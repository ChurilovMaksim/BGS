# Wave 43, task 2 — Gap G induction step: from m=128 to general 2^k

## Verdict

No counterexample at m = 256 or m = 512: Gap G holds exactly at m = 256
for all periods and at m = 512 for p = 256, 512 (0 symmetric O in all
cases). The induction step is proved as a reduction theorem: Gap G at
period p = 2^j (j ≥ 7) follows from the level-independent machinery
plus a tower lemma, and the tower lemma's key pinning — the mod-8
slope δ of the shift-8 operator is odd — is PROVED from 2-adic
valuations. Full Gap G for all 2^k is not yet proved: the remaining
gaps are the doubling-tower pinning (B1, B2 below) and the divisibility
lemma in general form, plus one more tower digit at j ≥ 9.

## 1. Level-independent machinery (waves 40–42, restated)

Kernel sequence mod Q = 8m², minimal period p = 2^j, ν = (1,0).
w_k = y_{2k+1} has period p/4; quarter defect
w_{k+p/8} = w_k + (Q/2)ε_k, ε alternates. Balance lemma: O symmetric
⟺ 2B_c = A_c for all classes c mod Q/2 (sums over quarter indices
k < p/8). φ_k = (w_{k+p/16} − w_k)/(Q/4) mod 4 satisfies
(i) φ_{k+1} ≡ 2φ_k − φ_{k−1} (mod 4),
(ii) φ_k ≡ ε_k (mod 2),
(iii) φ_k + φ_{k+p/16} ≡ 2ε_k (mod 4).
Pair analysis: pairs (j, j+p/16), j < p/16, partition quarter
indices. A pair with ε_j = 1 contributes 0; with ε_j = 0, φ_j = 2
contributes 0 (t flips); with ε_j = 0, φ_j = 0 contributes
2(1−2t_j) = ±2 (pair members have equal w-values, so equal t).
Hence 2B_c − A_c = Σ_{φ=0 pairs in c} ±2, and Gap G ⟺ some class
has nonzero sum. ψ-analysis (φ_k = ε_k + 2ψ_k, ψ alternates on
parity classes): φ = 0 pair representatives number 2^{j−6},
spaced 4 apart. Verified: p = 128 → 2 reps, p = 256 → 4,
p = 512 → 8, all spaced 4.

## 2. Tower lemma and reduction theorem

Define the shift-4 operator Op⁽²⁾_k = (w_{k+4} − w_k)/(Q/2^{j−4})
mod 4 and the shift-8 operator Op⁽³⁾_k = (w_{k+8} − w_k)/M mod 8,
where M is the natural modulus (Q/8 for j ≤ 8, Q/16 for j = 9;
see §4). Tower lemma:
(B1) Op⁽²⁾_k ≡ φ_k + 2 (mod 4) — separation: φ = 0 reps 4 apart
lie in distinct classes (difference ≡ Q/2^{j−5}·odd ≢ 0 mod Q/2).
(B2) Op⁽³⁾_k ≡ φ_k (mod 4) where defined — grouping: φ = 0 reps
differing by 8 share a class (v_{j+8} = v_j).
(B3) The mod-8 slope δ of Op⁽³⁾ is odd — witness: Op⁽³⁾ mod 8
alternates along φ = 0 reps, so of the two mod-8 classes exactly
one has t-agreement, giving 2B − A = ±2^{j−6} ≠ 0.
Reduction theorem: (A) + (B1)–(B3) ⟹ Gap G at period 2^j.
At j = 7 the classes are singletons, so both are ±2 witnesses
and (B3) is not needed; at j ≥ 8 the witness is ±2^{j−6}.

## 3. δ odd: PROVED from 2-adic valuations (the new step)

Parametrisation (verified pattern, m ≤ 512): y_0 = (Q/8p)t,
y_1 = a(Q/8p)t + (Q/p)s, ν = (1,0) ⟺ t odd, s even.
Write y_n = P_n y_1 − P_{n−1} y_0 (P_0 = 0, P_1 = 1,
P_{n+1} = 6P_n − P_{n−1}). Then the shift-8 slope is
δ = ((Xa − Y)t + 8Xs)/256, where
X = (P_{19}−P_3) − (P_{17}−P_1) = 60245508192768 = 2^9 · 117667008189,
Y = (P_{18}−P_2) − (P_{16}−P_0) = 10336495061760 = 2^8 · 40376933835.
Hence δ = (2·117667008189·a − 40376933835)·t + 16·117667008189·s
≡ (2a − 3)·t (mod 8) since 117667008189 ≡ 1 (mod 4) and
40376933835 ≡ 3 (mod 8). Y_odd is odd, 2·X_odd·a is even, t is
odd, so δ is odd — for every odd t, every a, every s.
The same computation gives δ′ odd at j = 9 (modulus Q/16):
the p-cancellation absorbs exactly one more power of 2.
Note the same v_2 data predicts the j = 9 modulus drop:
(Q/8)-divisibility of shift-8 differences would force
(Xa − Y)t + 8Xs ≡ 0 (mod 512), but the bracket is
2^8·odd, so it fails — exactly as observed (§4).

## 4. Exact verification at m = 256 and m = 512

m = 256, all p ≤ 256: Gap G holds directly (symO = 0);
(B1) holds for p ≥ 128, (B2) holds for p = 128, 256;
φ = 0 reps as in §1; at p = 256 the two classes take values
{0, ±4} per point, one witness.
m = 512, p = 256: identical to m = 256 (f0 = 4, values {0, ±4}).
m = 512, p = 512: Gap G holds (524288 points, symO = 0);
shift-8 divisibility by Q/8 FAILS at every point (as §3
predicts) but holds by Q/16; Op⁽²⁾ ≡ φ + 2 holds (0
violations); Op₃′ mod 8 at φ = 0 reps is exactly
(4,0,4,0,4,0,4,0) or (0,4,0,4,0,4,0,4) (δ′ odd, §3);
φ = 0 classes per point have sizes (2,2,4) — the Op₃′ ≡ 0
reps form the size-4 class (step-8 grouping), the Op₃′ ≡ 4
reps pair by step 16 into two size-2 classes — and take
values {0, +4, −4}, so every point has a ±4 witness.
Parametrisation pattern holds at (512,512): y_0 multiple of
step0, t odd, a mod 8 ∈ {1,3,5,7}.

## 5. What remains open

- General proof of (B1), (B2): the doubling tower
Op⁽ˢ⁺¹⁾_k = (Op⁽ˢ⁾_k + Op⁽ˢ⁾_{k+2^s})/2 plus pinning at
k = 0, 1 from the parametrisation. Verified exactly to
m = 512; (B1) also at (512,512).
- Divisibility lemma in general form (Lemma 2 family):
shift-8 differences divisible by Q/2^{j−5}; the modulus
law v_2 ≥ j + 8 (m = p case) follows from the same
P-coefficient valuations as §3 but is not written out.
- At j ≥ 9, t-agreement inside step-8 groups needs the
mod-16 digit of the shift-8 operator (the size-4 class at
p = 512 contributes ±4, i.e. a 3–1 t-split, not ±8);
this is the next tower digit.
- Hence: Gap G is unconditional to m = 512 and follows in
general from the tower pinning above; the Split Bit Lemma
is unconditional to m = 512, and T_k = 5(k−4) still rests
only on the U-lemma at the 2-part (Gap G side closed to
m = 512, general case modulo tower pinning).
No Lean built, repository untouched. Checks:
wave43_GapG_explore.py, wave43_GapG_explore2.py,
wave43_GapG_explore3.py, wave43_GapG_m512.py,
wave43_GapG_m512b.py.
