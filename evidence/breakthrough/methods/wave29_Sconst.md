# Wave 29, task 4 — S⁽ᵈ⁾-constancy on the 152 failing classes

**Verdict.** The failing-class statement is proved as a finite exact statement:
ΔS⁽ᵈ⁾ = ΔW_d = ΔA_d = 0 for every d and every one of the 152 failing
(fiber, w)-classes at m = 12, by the τ–δ reduction below plus exact integer
verification on the wave-18 census. No counterexample exists. The mod-10368
target holds a fortiori (ΔW_d = 0, and |W_d| ≤ 300 by wᵢ ∈ [−1, 5]).
What is NOT proved: the conceptual derivation of the τ-structure and the
cancellation laws from the gluing maps γ_q, and the same analysis at
general m. (Census: `methods/wave18_Pw_m12_census.json`; notation as wave 27
task 5: H = 6I − C − Cᵀ, w = Hy/D, classes r = {r, r+4, r+8} mod 4,
S⁽ᵈ⁾ = Σᵢ yᵢwᵢ₊d, W_d = Σᵢ wᵢwᵢ₊d, A_d = Σᵢ yᵢyᵢ₊d, D = D₁₂ = 1536796800.)

## 1. Re-verification: no counterexample

Independently re-checked from the census: for all 152 failing pairs
(y, y′) (same fiber, same sorted(w), distinct Γ-orbits), ΔS⁽ᵈ⁾ = 0,
ΔW_d = 0, ΔA_d = 0 for all d = 0..11, exact integers, 0 violations.
The "find a counterexample" branch is closed for the statement as stated.
Recall from wave 27 §2: ΔW = 0 ⟺ ΔS = 0 ⟺ ΔA = 0, via the invertible
circulant X_circ (S = X_circ·W, A = X_circ²·W), so one constancy gives all
three; also S⁽ᵈ⁾ = (6A_d − A_{d−1} − A_{d+1})/D directly from w = Hy/D.

## 2. τ–δ structure (exact, all 152 pairs)

Every failing pair satisfies y′ = τ(y) for a permutation τ, and
w′ = τ(w) + δ with δ := w′ − τ(w):

- **Type I (137 pairs):** τ is a class-preserving involution (cpi): a
  product of 4 disjoint transpositions, exactly one per class mod 4.
  126 pairs have τ unique; 11 have several y-perms but exactly one cpi.
- **Type II (15 pairs):** the per-class multisets are permuted by the D₄
  class map r ↦ −r+1 (classes swap 0↔1, 2↔3); sample τ e.g.
  (5,0,7,2,9,4,11,6,1,8,3,10): class reflection composed with
  within-class index maps (3-cycle shifts on two class pairs, identity
  on the other two). τ is not an involution here.
- Per-class data sharing (152 pairs): per-class sorted(y) 137/152,
  per-class sorted(w) 136/152, class sums of Y and of W 138/152 each.

## 3. Proved: d ≡ 0 (mod 4) for Type I — pure combinatorics, no check needed

For Type I τ, the d ≡ 0 (mod 4) autocorrelation is preserved
**class-by-class**. Within a 3-element class r = {a, b, c} (cyclic order
under +4), the +4-pairing gives products {y_a y_b, y_b y_c, y_c y_a} and
the +8-pairing (inverse cycle) gives the same multiset, since products
commute. Conjugating by the class transposition τ_r inverts the cycle
but leaves the multiset unchanged. Hence C_r^{(4)} and C_r^{(8)} are
τ-invariant per class (verified 504/504), so ΔA_4 = ΔA_8 = 0; ΔA_0 = 0
since A_0 = Σ y² is fiber-constant. (Note A_8 = A_4 identically, as
−4 ≡ 8 mod 12 and A_{−d} = A_d.) This covers 3 of the 12 values of d
for 137 of the 152 pairs by proof alone.

## 4. General-d reduction (proved as algebra)

With ψ_d(j) := τ(τ(j) + d), one has A_d(y′) = Σ_j y_j y_{ψ_d(j)}, so
ΔA_d = Σ over class pairs (r, s = r + d) of explicit terms. In cyclic
labeling (class r positions r₀, r₁, r₂; class s positions s_k = r_k + d),
ψ_d|_r is the permutation σπ of {0,1,2} (π = τ_r's permutation,
σ = τ_s's permutation); the class contribution is 0 if σπ = id, a
transposition product (y_{r_a} − y_{r_b})(y_{s_b} − y_{s_a})-type term if
σπ is a transposition, or a 3-cycle difference (C⁺ or C⁻, with
C⁺ − C⁻ = det[[1,1,1],[x₀,x₁,x₂],[z₀,z₁,z₂]]) if σπ is a 3-cycle.
Coset sums vanish automatically: Σ_{d≡c (mod 4)} ΔA_d = 0 for each c
(since Σ_{d∈{0,4,8}} A_d = Σ_r Y_r², Σ_{d∈{1,5,9}} A_d = Σ_r Y_r Y_{r+1},
etc., with class sums preserved). The remaining content is the
value-level cancellation of these terms, governed by the laws in §5.

## 5. Cancellation laws (exact on all 152 pairs)

- **Parity law.** Defect classes (where w′ ≠ τ(w)) are always parity
  classes {1,3} or {0,2}, or all, or none. Per-class w′-pattern
  (τ / id / other vs τ(w) / w): (tau,tau,tau,tau) 69;
  (tau,other,tau,other) 23; (other,tau,other,tau) 23; (tau,id,tau,id) 6;
  (id,tau,id,tau) 4; (other,other,other,other) 1.
- **δ-moment law.** Σᵢ i·δᵢ ≡ 0 (mod 12) for all 126 τ-pairs. In
  125/126 cases δ is a rectangle −e_a − e_b + e_c + e_d with
  a + b ≡ c + d (mod 12) (6 patterns up to sign at (tau,other,tau,other)).
  The one 8-point exception, δ = [0,−1,1,0,1,1,0,1,−1,0,−1,−1], has
  τ exchanging its sign sets and equal y-sums over them
  (3073593600 = 3073593600), so its contribution still vanishes.
- **Antipodal-neighbor law (46/46 defect pairs).** The τ-images of the
  δ-support always form {p−1, p+1, p+5, p+7}, and N(p) = N(p+6) holds
  for that p, where N(p) = y_{p−1} + y_{p+1}. With
  T_r := Σ_{j∈r} y_j (w′_{τ(j)} − w_j), one has ΔS⁽⁰⁾ = Σ_r T_r = 0,
  via T_1 + T_3 = 0 for (tau,other,tau,other) and T_0 + T_2 = 0 for
  (other,tau,other,tau). T-values are multiples of D/35; swap
  differences Δy/D have denominators dividing 35 only.
- **Neighbor identity.** D·δᵢ = (y_{τ(i)−1} + y_{τ(i)+1}) −
  (y_{τ(i−1)} + y_{τ(i+1)}) everywhere, i.e. (Hτ − τH)y = Dδ.

## 6. Finite verification completing the proof

For d ≢ 0 (mod 4) and for the 15 Type II pairs, the class-pair terms
of §4 are verified to cancel exactly on all 152 pairs for all d
(exact integer arithmetic on census reps; direct ΔS⁽ᵈ⁾ = 0 was already
in §1). Together with §3, this proves S⁽ᵈ⁾-constancy on the failing
classes. The mod-10368 target follows: ΔW_d = 0, hence
ΔW_d ≡ 0 (mod 10368); conversely the bound |W_d| ≤ 300 means any
M > 600 would have sufficed to force exact constancy from a congruence.

## 7. Worked examples

- **SIGMA pair (τ(w) exact):** y = [1024531200, 475675200, 292723200,
  1280664000, 1244073600, 36590400, 512265600, 1500206400, 804988800,
  256132800, 731808000, 1061121600], y′ = [y₄, y₉, y₂, y₇, y₀, y₅, y₁₀,
  y₃, y₈, y₁, y₆, y₁₁], τ = (0 4)(1 9)(6 10)(3 7),
  w = [3,1,0,4,4,−1,1,5,2,0,2,3], w′ = τ(w) = [4,0,0,5,3,−1,2,4,2,1,1,3];
  class sums Y = (3073593600, 768398400, 1536796800, 3841992000),
  W = (9,0,3,12) shared; fixed positions f = (2,1,0,2).
- **NOSIGMA pair (defect on classes 1, 3):** y = [585446400, 1178210880,
  336631680, 841579200, 102453120, 1309936320, 73180800, 665945280,
  848897280, 1353844800, 1126984320, 797670720],
  τ_y = (0 8)(2 6)(3 11)(5 9) (unique), w = [1,4,0,3,−1,5,−1,2,2,4,3,2],
  w′ = [2,4,−1,3,−1,5,0,2,1,4,3,2] = τ(w) with the class-1 and
  class-3 swaps undone; joint (y,w) pairs differ only at
  (797670720: 2→3), (841579200: 3→2), (1309936320: 5→4),
  (1353844800: 4→5); T_1 = −D/35, T_3 = +D/35.

## 8. What remains open (do not overclaim)

- Conceptual derivation: why τ-structure, the parity law, the
  δ-moment law, and N(p) = N(p+6) hold for genuine Fix vectors — i.e.
  deriving §5 from the gluing maps γ_q, rather than verifying it on
  the 152 classes. This is now the precise remaining gap for a
  non-computational proof of the W-mod lemma.
- Type II pairs need their own full class-pair analysis (only the
  τ-structure is recorded here); general m is untouched (census is
  m = 12 only); the S⁽ᵈ⁾-constancy at general m and the Σ yᵢwᵢ
  constancy mechanism in general m remain open (wave 23 task 4).
- Dead ends, do not retry: pair-sum constancy (false: 1529/1529 reps
  violate for most s); N(p) = N(p+6) for all p (false in general,
  true only for the p determined by each pair's δ-support);
  w-side dihedrality, mod-(D/q) strengthening, broad D-divisibility
  (wave 27 §3); the AP-class mechanism (only 15/152 pairs have ≥6
  AP classes; 137 have none).
