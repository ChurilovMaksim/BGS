# Wave 15, task 1 — S* = 0 for G1 case (1,2): PROVED

**Verdict.** The scalar lemma S* = 0 of wave 14, task 1, §2 (case (1,2):
f = 3, k = 1, s = 2) is proved for unit A; divisible A goes by induction
(wave 12, §0). Hence G1 at f = 3, case (1,2), is fully closed — not via
the dichotomy's second branch (uniform groups), but because that branch
is impossible when singletons exist. Repository untouched, no Lean built.

## 0. Setup and one correction to wave 14, §2

p odd, P = p³, R = Z[√2], α = 3+2√2, γ = α^{L₀} = 1+pu,
u ≡ μ√2 mod p (Lemma A), t = gcd(m,4), g = gcd(L₀,t),
H₀ = ⟨α^{tp²}⟩ (|H₀| = L₀/g), C_{r,z} = Aα^r z (r mod g, z ∈ H₀),
F(C) = {Tr(Cγ^j) : j ∈ Z/p²}. v = v_p(Tr(Cu)) ∈ {0,1,2}:
v = 2 singletons F(C) = {Tr(C)}; v = 1 cosets {Tr(C)+p²d};
v = 0 full classes Tr(C) mod p.

**Correction.** Wave 14, §2, step 1 states Tr(η) ≡ 0 mod p
unconditionally for A″ = A(1+pη). This holds only when Coll ≠ ∅
(Coll = {(r,z) : Tr(Cu) ≡ 0 mod p}): wave 13's digit argument derives
Tr(η) = 0 from pooled collapsed equality, which is vacuous if
Coll = ∅ (e.g. (36,3), A = (1,1): Coll = ∅, and some normalisations
have Tr(η₀) = 2 ≠ 0). But v = 2 ⟹ Coll, so when v = 2 singletons exist,
Tr(η₀) = 0 holds, and γ-shifts (which change η₀ by multiples of u₀,
purely imaginary) normalise η₀ = 0 at the cost of a D_t-rotation of
classes; then A″ = A(1+p²η₁), S* = Tr(η₁) is well defined (γ^p-shifts
change η₁ by u₀, Tr = 0; reflection preserves Tr). When Coll = ∅
there are no singletons and S* is unneeded. The "no-transform" pairs
in the numerics below (216 at (36,3), 6000 at (150,5)) are exactly
this phenomenon: A″ ≡ A mod p² is blocked by N(A′/A) ≢ 1 mod p²,
and all sampled such pairs are singleton-free.

With η₀ = 0: v = 0 and v = 1 cosets match per class exactly (top digit
uniformly distributed, shift by a constant permutes it), so global
equality forces the pooled v = 2 multisets to match. Within one
low-group (low = Tr(C) mod p²), c = C mod p ∈ F_p^× is fixed
(low mod p = 2c) and top digits shift uniformly by c·S*.
**Dichotomy:** either S* = 0, or every nonempty low-group's
top-digit multiset is shift-invariant, hence uniform, hence its
size is divisible by p.

## 1. Lemma (0-or-2): collapsed pairs number 0 or 2

For unit A, #{(r,z) : Tr(C_{r,z}u) ≡ 0 mod p} ∈ {0, 2}.

*Proof.* By Lemma A, Tr(Cu) ≡ 0 mod p ⟺ C mod p ∈ F_p. So count
{(r,z) : (Aα^r z) mod p ∈ F_p}. Claim: φ(r,z) = α^r z mod p is a
bijection {0,…,g−1} × H₀ → ⟨α⟩ mod p (both of size L₀).
Frobenius in R/p: x^p = a + b·(2|p)√2 for x = a+b√2, so
α^{p²} ≡ α mod p; hence H₀ mod p = ⟨α^{tp²}⟩ = ⟨α^t⟩ mod p, of order
L₀/g. If α^{r₁}z₁ ≡ α^{r₂}z₂ mod p, then α^{r₁−r₂} ∈ ⟨α^t⟩ mod p,
and in cyclic ⟨α⟩ mod p (order L₀) this means g | (r₁−r₂), so
r₁ = r₂ (range < g); then z₁ ≡ z₂ mod p, and reduction is injective
on H₀ (order coprime to p; its kernel is a p-group, as
(1+px)^{p²} ≡ 1 mod p³), so z₁ = z₂. Thus φ is bijective.
Collapsed pairs = φ⁻¹{w ∈ ⟨α⟩ : A·w ∈ F_p}; A·w ∈ F_p ⟺
w ∈ A⁻¹F_p, a line; elements of norm 1 on it are c·A⁻¹ with
c² = N(A): 2 solutions if N(A) is a QR mod p, 0 otherwise. ∎

## 2. Theorem: S* = 0

Let A be a unit mod p and suppose v = 2 singletons exist. Then S* = 0.

*Proof.* v = 2 pairs ⊆ collapsed pairs, so at most 2 of them (§1).
Each low-group's size in the pooled multiset is ρ′·n_L, where n_L ≤ 2
is its pair count and ρ′ is a repetition factor prime to p
(ρ′ = (t/g)·ρ with t/g | 4 and ρ·(t/g) = m/L coprime to p, so any
prime divisor of ρ′ divides m/L, hence p ∤ ρ′). If S* ≠ 0, the
dichotomy forces p | ρ′·n_L for every group, hence p | n_L; but
1 ≤ n_L ≤ 2 < p (p odd), impossible. So S* = 0. ∎
Divisible case (p | A): A = pA₁, divide by p and apply G1′ at f = 2
(wave 13); per-class D-relatedness lifts by multiplication by p.

## 3. Numerical confirmation (exact arithmetic)

- (36,3): 17 groups, 0 D-bad pairs; S* ≠ 0 occurs in 72 pairs, all in
  singleton-free fibres (0 pairs with S* ≠ 0 among fibres with
  singletons); 0-or-2 verified on all 648 unit A.
- (150,5): 69 groups, 0 D-bad pairs; 2682 pairs in singleton fibres,
  all S* = 0; 0-or-2 verified on 52 unit group bases + 300 random
  unit A (0 violations). No fibre at either case has all low-groups
  of size divisible by p.

## 4. What remains for G1

Case (1,2) at f = 3 is closed. Remaining: f = 2, s = 0 real-case gap
(needs k = 2 and 4 | L₀; no instance ≤ 10000); case (3,0) in general
(no instance ≤ 10000); G1 at f ≥ 4; G3 (Lemma PC in general);
Lean formalisation. Combined with wave-13 G2, the exact per-class
lemma's remaining gaps are exactly G1 (f = 2 s = 0 real case,
(3,0), f ≥ 4) and G3.

## Files

- This note: wave15_G1_Sstar.md
- Scripts: wave15_G1_Sstar_check.py ((36,3), (150,5) full),
  wave15_G1_Sstar_check2.py ((150,5) singleton fibres + 0-or-2),
  wave15_G1_Sstar_debug.py ((36,3) no-transform analysis)
