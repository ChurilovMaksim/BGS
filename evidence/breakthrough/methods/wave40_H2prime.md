# Wave 40, task 2 — H2' lift-sweeping lemma: PROVED under order-growth

## Verdict

**Theorem.** Let p be odd, R = Z[√2], β ∈ R with N(β) = 1,
β^u ≡ 1 mod p^fR, d = ord_p(β) (order of β mod pR), and
β^k = A_k + B_k√2. Assume 4 ∤ d, and (f = 1 or β^d ≢ 1 mod p²R).
Then H2' holds: {B_k mod p^f : k ∈ Z/u} is a union of full mod-p
fibers, each internally uniform (S, μ below). In the Lemma U setup
u is odd, so d | u is odd and 4 ∤ d is automatic: there, H2' holds
iff the order grows on lifting, and the wave-39 dividing line
(42,13,2) is exactly the failure of growth.

## Lemma 1 (order growth, binomial induction)

Let x = β^d = 1 + pγ with γ ≢ 0 mod pR (i.e. β^d ≢ 1 mod p²R).
Then x^{p^j} = 1 + p^{j+1}γ_j with γ_j ≡ γ mod pR for all j ≥ 0.
*Proof.* Induction on j: (1 + p^{j+1}γ_j)^p = 1 + p^{j+2}γ_j +
terms divisible by p^{k(j+1)+1} (k ≥ 2, via p | C(p,k)) and by
p^{p(j+1)}; all are divisible by p^{j+3}, so the bracket is
γ_j mod pR. ∎
**Corollary.** ord_{p^j}(β) = d·p^{j−1}: β^{d·p^{j−1}} = x^{p^{j−1}}
≡ 1 mod p^jR, while β^{d·p^{j−2}} = 1 + p^{j−1}γ_{j−2} ≢ 1 mod p^jR
(γ_{j−2} ≡ γ ≢ 0 mod pR, R a domain); ord is a multiple of d and
divides d·p^{j−1}, so it equals d·p^{j−1}. ∎

## Lemma 2 (collision factorisation)

B_a ≡ B_b mod p^f ⟺ (β^{a−b} − 1)(β^{a+b} + 1) ≡ 0 mod p^fR.
*Proof.* N(β) = 1 gives β^{−k} = β̄^k = A_k − B_k√2, so
β^k − β^{−k} = 2B_k√2, and B_a ≡ B_b mod p^f ⟺
β^a − β^{−a} ≡ β^b − β^{−b} mod p^fR (p odd). With x = β^b,
y = β^{a−b}: xy − x^{−1}y^{−1} = x − x^{−1} ⟺
x(y−1) = −x^{−1}y^{−1}(y−1) ⟺ (y−1)(x + x^{−1}y^{−1}) = 0 ⟺
(y−1)(x²y + 1) = 0 (xy a unit), and x²y = β^{a+b}. All steps
reverse. ∎

## Lemma 3 (second factor is a unit when 4 ∤ d)

If a ≡ b ≡ k₀ mod d, then β^{a+b} + 1 ≢ 0 mod 𝔭 for every prime
𝔭 | p, hence it is a unit in R/p^fR (CRT: p unramified in Q(√2),
disc 8, so p^fR = ∏ 𝔭^f with distinct 𝔭, and R/p^fR ≅ ∏ R/𝔭^f).
*Proof.* a + b ≡ 2k₀ mod d and β^d ≡ 1 mod 𝔭 give
β^{a+b} ≡ β^{2k₀} mod 𝔭. If β^{2k₀} ≡ −1 mod 𝔭, then
ord_𝔭(β) ∤ 2k₀ but ord_𝔭(β) | 4k₀; writing ord_𝔭 = 2^s·m with
m odd forces s ≥ 2 (s = 0: m | 4k₀ ⟹ m | k₀; s = 1: 2m | 4k₀ ⟹
m | k₀ ⟹ 2m | 2k₀). But ord_𝔭(β) | d and 4 ∤ d give s ≤ 1,
contradiction. ∎

## Proof of the Theorem

Let T = ord_{p^f}(β) = d·p^{f−1} (Lemma 1; T = d if f = 1). T | u,
so the multiset over Z/u is (u/T) copies of the period multiset
{B_k : k ∈ Z/T}. Fix k₀ ∈ Z/d. The subsequence B_{k₀+jd},
j ∈ Z/p^{f−1}, all satisfy B ≡ B_{k₀} mod p (β^d ≡ 1 mod pR).
Injectivity: if B_{k₀+jd} ≡ B_{k₀+j′d} mod p^f, Lemma 2 gives
(β^{td} − 1)(β^{a+b} + 1) ≡ 0 with t = j − j′; Lemma 3 makes the
second factor a unit, so β^{td} ≡ 1 mod p^fR, so T | td, so
p^{f−1} | t, i.e. j ≡ j′ mod p^{f−1}. Hence the subsequence has
p^{f−1} distinct values, all in the fiber over B_{k₀} mod p,
which has exactly p^{f−1} elements: it exhausts the fiber, once.
Assembling over k₀ ∈ Z/d: value x occurs
#{k₀ : B_{k₀} ≡ x mod p} times per period. So with
S = {B_{k₀} mod p} and μ(r) = (u/T)·#{k₀ : B_{k₀} ≡ r mod p},
every x ∈ Z/p^f with x mod p ∈ S occurs exactly μ(x mod p)
times, and no other value occurs. μ(−r) = μ(r) since
B_{−k} = −B_k and k₀ ↦ −k₀ permutes Z/d. ∎

## Partial converse (level counting)

If β^d = 1 + p^sγ with γ ≢ 0 mod pR and s ≥ 2, the same binomial
induction gives period ≤ d·p^{f−s}, so at most d·p^{f−s} distinct
values, while H2' needs ≥ p^{f−1} (one full fiber). Hence H2'
fails whenever d < p^{s−1}. Instance: (42,13,2) has d = 7, s = 2
(β⁷ ≡ 1 mod 169, β⁷ ≡ (1,1014) mod 2197), 7 < 13, and indeed only
7 distinct B values occur (u = 21). The intermediate regime
(s ≥ 2, d ≥ p^{s−1}) is not ruled out by counting.

## Verification (exact integer arithmetic)

- Sweep A (wave-39 scope, m ∈ {12,18,24,30,36,42,48,60}, p ≤ 200
  odd, p^f ≤ 10⁵): 24 components, **0 theorem violations**;
  growth holds 23, H2' holds 23, both fail 1 (42,13,2).
- Sweep B (all even m ≤ 120, same p, f ranges): 91 components,
  **0 violations; growth ⟺ H2' exactly** (87/87, both fail 4:
  (m,13,2) for m ∈ {14,42,70,98}, all d = 7, β⁷ ≡ 1 mod 169).
- Growth-lemma orders: 15 components with f ≥ 2 and growth,
  0 mismatches (β^{d·p^{f−1}} ≡ 1, β^{d·p^{f−2}} ≢ 1 mod p^f).
- Factorisation equivalence (Lemma 2): 1200 random pairs over
  (30,5,2), (36,3,3), (12,3,2), (60,11,1), 0 mismatches.
- Check script: wave40_H2prime_check.py. No Lean, repository untouched.

## What remains

- 4 | d at f ≥ 2: the theorem does not cover it (Lemma 3 fails:
  some (𝔭, k₀) has β^{2k₀} ≡ −1 mod 𝔭). No such component exists
  in scope — all 4 | d components found have f = 1, where H2' is
  trivial — so whether H2' holds or fails there is open.
- The "collisions arise only from (i)–(iii)" classification is
  still open (unchanged); mechanism (iii) itself is now proved
  under H2', and H2' under order-growth.
