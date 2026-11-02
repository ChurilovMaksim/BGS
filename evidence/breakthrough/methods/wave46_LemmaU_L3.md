# Wave 46, task 2 — Lemma U: L3 proved (generic case), degenerate locus classified

## Verdict

**L3 is PROVED in the generic case** (§2) and **no counterexample exists** at
any of four censused components (§4), including negation-symmetric,
singular, and f = 2 cases. The **scaling-block lemma** (§3) is proved and
verified exactly at m = 30 (30,800 generic tests, 0 disagreements). The
degenerate locus is now sharp: scaling collides iff σ preserves mod-g
classes, except one clean slack family (§3, 56 cases). No Lean built,
repository untouched.

## 1. Setup

M(C) = multiset of Tr(Cβ^k), k ∈ Z/u (length u). L3: M(x) ∪ M(x′) =
M(t) ∪ M(−t) ⟹ {M(x), M(x′)} = {M(t), M(−t)}, where x, x′ are the
first-coordinate cycles of the two colliding blocks. R = Z[√2] mod p^f,
α = (3,2), β = α², Tr(a+b√2) = 2a, N(C) = a²−2b².

## 2. L3 proof (generic case)

Hypotheses: p odd, p ≠ 3, f = 1, p ∤ T, T ≥ 3; t of period T with values
distinct mod p and negation-free mod p; x, x′ with values distinct mod p.

Lemma A (root uniqueness). If ∏(X−a_i) = ∏(X−b_i) in (Z/p^f)[X] with all
roots pairwise distinct mod p, the multisets {a_i}, {b_i} coincide.
Proof: evaluate at a_1; some a_1−b_j ≡ 0 mod p (else the product is a
unit); Q′(a_1) is then a unit mod p, forcing a_1 = b_j exactly; cancel
the monic factor (X−a_1) and induct.

Lemma B (Dickson). If β has order T and p ∤ T, then
∏_{j mod T}(X − Tr(Dβ^j)) = D_T(X, N) − Tr(D^T), where D_T is Dickson
first kind (D_0 = 2, D_1 = X, D_{n+1} = X D_n − N D_{n−1}).
Proof: write D = √N·w (N(w) = 1); the resultant
∏_{Z^T=w^T}(Z²−YZ+1) = 1 + w^{2T} − w^T D_T(Y, 1); separability (p ∤ T)
makes {wβ^j} the full root set; scale back by √N. N = 0 follows by
polynomial continuation. β^T = 1 for unit D by Lemma C
(Tr(E) = Tr(Eβ) = 0 ⟹ E = 0 applied to E = D(β^T−1)).

Step 1 (periods). The union has 2T distinct values mod p, each with
multiplicity u/T. An x-value has multiplicity u/T_x, or u/T_x + u/T_{x′}
if shared. Shared ⟹ 1/T_x + 1/T_{x′} = 1/T ⟹
(T_x−T)(T_{x′}−T) = T²; all periods odd ⟹ LHS even, RHS odd — impossible.
Hence unshared, T_x = T_{x′} = T, and values(x) ⊔ values(x′) =
values(t) ⊔ values(−t).

Step 2 (norms). Multiset equality + Step 1 give P_x·P_{x′} = P_t·P_{−t}.
Dickson forms: P_x = D_T(X,N_x) − θ_x, etc. Coefficient X^{2T−2}:
−T(N_x+N_{x′}) = −2TN_t ⟹ N_x+N_{x′} = 2N_t (T a unit). Coefficient
X^{2T−4}: [T(T−3)/2](N_x²+N_{x′}²) + T²N_xN_{x′} = T(T−3)N_t² + T²N_t²
⟹ 3TN_xN_{x′} = 3TN_t² ⟹ N_xN_{x′} = N_t² (3T a unit; T = 3 by direct
expansion, X² coefficient 9N_xN_{x′} = 9N_t²). So (N_x−N_t)² = 0;
f = 1 gives N_x = N_{x′} = N_t. (f ≥ 2: nilpotent gap δ² = 0, §5.)

Step 3 (signs). Now (D−θ_x)(D−θ_{x′}) = D²−θ_t² with D = D_T(X,N_t),
so (θ_x+θ_{x′})D = θ_xθ_{x′}+θ_t²; D nonconstant ⟹ θ_{x′} = −θ_x and
θ_x² = θ_t² ⟹ θ_x = ±θ_t. Hence P_x = P_t or P_{−t}, so by Lemma A
M(x) = M(t) or M(−t), and M(x′) is the other. ∎

## 3. Degenerate locus: scaling-block lemma + slack

Lemma (scaling-block). t, s distinct-valued; λ·values(t) = values(t) with
σ: λt_j = t_{σ(j)}; g = gcd(T_a, T_b). Then {(λt_k, s_k)} = block0 ⟺
σ(a) ≡ a (mod g) for all a. Proof: the pair (t_{σ(a)}, s_b) lies in
block0 ⟺ σ(a) ≡ b ≡ a (mod g) (distinctness); and (a,b) ↦ (σ(a),b)
permutes compatible pairs iff the condition holds. Corollary (s
negation-free): a one-sided scaling collides ⟺ σ preserves mod-g
classes — block0′ = block1 is impossible since it would need
s_k = −s_{k′}.
Consequences. g = 1: condition vacuous (Cartesian-product blocks) — every
one-sided move preserves blocks. Singular cycles (split case): values are
geometric d·⟨β₁⟩, so σ(j) = j+k and the criterion is k ≡ 0 (mod g).
Multipliers: for nonsingular cycles at p ∤ T only ±1 occur (census);
at p | T the observed group is {λ ≡ ±1 mod p} (mod 25:
[1,4,6,9,11,14,16,19,21,24]);
at split primes singular cycles have the full root-of-unity group
(order 17 at (137,1): [1,16,34,38,50,56,59,60,72,73,74,88,115,119,122,
123,133]).
Example (wave 45's λ = 21, m = 30). √2-cycle mod 25: T_a = 15, values
(0,23,7,15,3,12,5,8,17,20,13,22,10,18,2),
σ_21 = [0,7,11,3,10,14,6,13,2,9,1,5,12,4,8]. For B = (1,2), (0,1),
(2,3) mod 29: T_b = 5, g = 5, σ violates mod-5 at
a ∈ {1,2,4,5,7,8,10,11,13,14} — blocks differ, as wave 45 found.
Slack (lemma sharpness). The criterion is sufficient everywhere
(0 over-predictions in 46,255 tests) but not necessary when s has
repeated values: exactly 56 unpredicted collisions, all (√2-family,
λ = −1, pure-rational B), where s_k = s_{−k} (reversal symmetry of
rational-part cycles) supplies index slack. Negation pairs in s add
collisions by ±-matching but never break sufficiency.

## 4. Census (scripts wave46_LemmaU_L3.py, wave46_LemmaU_L3b.py)

| component | params | multisets | negsym | L3 viol | Dickson |
|-----------|-------:|----------:|-------:|--------:|--------:|
| (53,1) u=27 | 2,809 | 79 | 27 | 0 | 2809/2809 |
| (197,1) u=27 | 38,809 | 2,255 | 99 | 0 | 38809/38809 |
| (137,1) u=17 split | 18,769 | 621 | 69 | 0 | 18769/18769 (incl. 273 singular) |
| (5,2) u=15 | 625 | 29 | 5 | 0 | 25/625 (only C ∈ 5R pass) |
Scaling scan m = 30 (A mod 25 × B mod 29): generic 30,800 tested, 30,800
agree — g = 1: 20,720/20,720 collisions; g = 5 genuine (σ ≠ id): 10,080
tested, 0 collisions. Degenerate B: 15,455 tested, 56 disagreements, all
(False → True) of the slack family above.
Dickson failure at p | T (√2 mod 25, θ = Tr(C^15) = 0): P ≠ D mod 25,
differing coefficients k = 1,3,5,7,9: P (0,0,1,5,10) vs D (20,10,21,0,0);
P ≠ X^15 mod 5 either — the identity fails already mod p when p | T,
as inseparability predicts (Z^T − w^T = (Z^{T/p} − w^{T/p})^p mod p).

## 5. Remaining gaps (exact)

1. L3 at f ≥ 2: nilpotent-norm lemma (δ² = 0 ⟹ δ = 0) unproved;
   censused at (5,2), 0 violations.
2. L3 at p | T: needs a Frobenius/period-collapse argument (mod-p period
   T₀ = T/p^e plus lift); censused at (5,2), 0 violations.
3. L3 at p = 3: 3T ≡ 0 kills Step 2; kernel case; α-formulation
   (det 32 a unit mod 3) is the route.
4. L3 for T = 1 and for x, x′ with repeated values mod p (Lemma A
   fails) — censused (all multisets incl. repeats), 0 violations.
5. L1 still open: multiset ⟹ cycle up to dihedral + scaling. L3 alone
   does not close Lemma U; alignment (wave 45) still needs L1.
6. Two-component scaling scan at a split component (singular × generic
   blocks) not yet run; single-component split census is done (§4).
