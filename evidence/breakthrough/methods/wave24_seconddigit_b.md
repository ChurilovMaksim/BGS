# Wave 24, task 5 — second-digit lemma, part (b): PROVED in general

**Verdict.** Part (b) is proved for every odd p with α^{L₀} ≡ 1 (mod p²)
(k ≥ 2; exactness k = 2 is NOT used, as in part (a)). Together with part
(a) (wave 21), the second-digit mechanism is now a proof, not an
empirical observation. Repository untouched, no Lean built.

## Setup

R = ℤ[√2], p odd, α = 3+2√2, L₀ = ord_p(α) ≥ 3 (wave 16 §1).
G = ⟨α⟩ mod p² has order L₀. A unit mod p², twist A′ = A(1+pc√2),
c ∈ 𝔽_p^× (ζ ∈ G in the general twist permutes the orbit, so ζ = 1
wlog). B = A^{L₀}. Gap case: B real mod p (B ≡ B̄ mod p).
Orbit values v_z = Tr(Az) mod p², z ∈ G; v_z = v0_z + p·v1_z;
t_z = Tr(A√2·z) mod p; twisted v1′_z = v1_z + c·t_z.

## Lemma 1 (Teichmüller decomposition mod p²)

Let m = |(R/p)^×|, coprime to p, and T = {u : u^m = 1} ⊂ (R/p²)^×.
Reduction π|_T : T → (R/p)^× is an isomorphism: injective since
(1+pu₀)^m = 1+pmu₀ mod p² forces u₀ = 0; surjective since any lift w
of ā has w^m = 1+pu₀, and w(1−pu₀/m) ∈ T lifts ā. Every unit writes
uniquely w = τ(w)(1+pλ(w)), τ(w) ∈ T, λ(w) ∈ R/p. α ∈ T (α^{L₀} = 1
mod p², L₀ | m), and π|_T injective gives ord(α) = L₀ in T.
Write A = τ_A(1+pλ_A), λ_A = a + b√2, T_j = τ_Aα^j ∈ T,
τ̄_j = π(T_j) = ξ̄_j + η̄_j√2.

## Lemma 2 (orbit second digits)

Tr(Aα^j) = Tr(T_j) + p·Tr(τ̄_jλ_A), so with d1_j = second digit of
Tr(T_j): v1_j = d1_j + Tr(τ̄_jλ_A) = d1_j + 2aξ̄_j + 4bη̄_j, and
t_j = Tr(τ̄_j√2) = 4η̄_j. Twist changes only λ: v1′_j = v1_j + c·t_j.

## Lemma 3 (P₂ obstruction)

Sums over j ∈ ℤ/L₀, all in 𝔽_p, carry-free: Στ̄_j = 0 and Στ̄_j² = 0
(geometric sums; α−1, α²−1 units since N(α−1) = −4, N(α²−1) = −32,
p odd; L₀ ≥ 3 so ᾱ² ≠ 1) give Σξ̄_jη̄_j = 0, Ση̄_j² = L₀N(τ_A)/4,
hence Σt_j = 0, Σt_j² = 4L₀N(τ_A) ≠ 0, and
Σv1_jt_j = 4Σd1_jη̄_j + 4bL₀N(τ_A). If the v1-marginal is preserved,
Σv1_j² = Σ(v1_j+ct_j)², so 2Σv1_jt_j + cΣt_j² = 0, i.e.
2Σd1_jη̄_j + L₀N(τ_A)(2b+c) = 0. Define K = −2Σd1_jη̄_j/(L₀N(τ_A)):
preservation with c ≠ 0 forces c = K − 2b.

## Lemma 4 (gap symmetry: K = 0 in the gap case) — the heart

Gap ⟺ (a/ā)^{L₀} = 1, a = π(τ_A) ⟺ ā/a ∈ ⟨ᾱ⟩ (norm-1 group cyclic,
⟨ᾱ⟩ its unique order-L₀ subgroup). Write ā/a = ᾱ^r. Then
ρ := (τ̄_A/τ_A)·α^{−r} ∈ T (T conjugation-stable) and π(ρ) = 1, so
ρ = 1 by injectivity of π|_T. Hence τ̄_A = τ_Aα^r in R/p², exactly.
Therefore T̄_j = τ̄_Aα^{−j} = τ_Aα^{r−j} = T_{r−j} exactly in R/p².
So d1_{r−j} = d1_j (Tr(T̄_j) = Tr(T_j) exactly) while η̄_{r−j} = −η̄_j
(conjugation negates the √2-coefficient mod p). Reindexing,
Σd1_jη̄_j = Σd1_{r−j}η̄_{r−j} = −Σd1_jη̄_j, so Σd1_jη̄_j = 0
(p odd), i.e. K = 0.

## Theorem (b2: second digits detect real-B twists)

In the gap case, preservation with c ≠ 0 forces c = −2b (Lemma 3+4).
But c = −2b with gap ⟺ A′ ∈ Ā·G (trivial): Ā⁻¹A′ =
(τ_A/τ̄_A)(1+p(2b+c)√2) ∈ G ⟺ gap and 2b+c = 0; and A′ ∉ A·G for
c ≠ 0 (1+pc√2 has order p, |G| = L₀ coprime to p). Hence every
genuine twist in the gap case changes the v1-marginal. ∎

## Theorem (b1: power sums detect non-real-B twists, wave 16 §5)

If the full multiset {Tr(Az)} mod p² is preserved, then for all r,
ΣTr(A′z)^r = ΣTr(Az)^r mod p²; expanding Tr(A′z) = Tr(Az)+p·Tr(Afz)
(f = c√2) gives r·S_r ≡ 0 mod p, S_r = ΣTr(Az)^{r−1}Tr(Afz).
Binomial expansion + Σ_{z∈G} z^k = L₀[L₀|k] gives S_r = 0 for
r < L₀ (the two surviving terms cancel via f̄ = −f) and
S_{L₀} = L₀f(B−B̄). With gcd(L₀,p) = 1, preservation forces
B real or f = 0. Contrapositive: B non-real, c ≠ 0 ⟹ the full
multiset changes. ∎

## Numerical confirmation (not part of the proof)

- p=13: K = 0 for all 168 τ ∈ T (gap automatic there); P₂ alone
  proves (b2) at p=13.
- p=31: K = 0 ⟺ gap-type, exactly 450/450 each way; ρ = 1 verified
  for all 450 gap τ's (scripts wave24_K_probe.py, wave24_K_gap.py).
- p=1546463 (third k=2 prime, L₀ = 773231, C++ __int128):
  20 gap-genuine + 22 non-gap-genuine twists, 0 marginal preservations;
  5/5 trivial controls preserved; K = 0 for all 25 gap A's checked
  (wave24_b_p1546463.cpp).

## Honest scope / dead end recorded

- A first attempt via trace-linear δ (d1_j = Tr(τ_jδ)) FAILED:
  d1 does not satisfy the homogeneous recurrence (carry term from the
  mod-p sequence); explicit failure at p=13, A=(1,2), j=2. Do not retry
  the δ-route; the proof above avoids δ entirely.
- NOT proved here: uniform v1-marginal change in the non-gap case
  (only full-multiset change via S_{L₀}); the converse "non-gap ⟹
  K ≠ 0" (empirical at p=31 only); whether (a)+(b) complete the
  wave-14 f=2 s=0 stabiliser argument (separate check); f ≥ 4,
  general PC, Lean formalisation.

## Files

- This note: wave24_seconddigit_b.md
- Probes: wave24_b_probe.py (failed δ-route), wave24_K_probe.py,
  wave24_K_gap.py, wave24_b_p1546463.cpp
- Prior: wave21_seconddigit_injectivity.md (part (a)),
  wave19_G1_seconddigit.md, wave16_G1_f2s0.md §5
