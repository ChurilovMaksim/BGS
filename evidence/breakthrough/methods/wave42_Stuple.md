# Wave 42, task 3 — S-tuple dihedral lemma: PROVED

**Verdict.** The lemma holds in all cases (no hypothesis, no counterexample).
It was the single remaining lemma behind SC-sup, so SC-sup is now
unconditional (modulo wave 41 §§2–3, which were already unconditional),
and Δ→0 v3 stands on H0, SCL, SCJ′ only.

## 0. Setup

R = ℤ[√2], α = 3+2√2, β = 3−2√2 (αβ = 1, α+β = 6, α−β = 4√2),
Tr(x) = x + x̄. A kernel point y mod q has an integer lift sequence
Ỹ with Ỹ_i = Tr(Aα^i), A ∈ (1/8)R (from the lifted initial pair).
Class sums: S_r = Σ_{i≡r mod C} y_i (mod q), C = 4 if 4|m, C = 2 if
m ≡ 2 (mod 4), C = 1 if m odd. A component fibre is the set of kernel
points mod q with the same sorted multiset {y_i}.

## 1. The η-operator and its periodicity

For 4|m put N = m/4 and η = Σ_{j<N} α^{4j} = (α^m−1)/(α^4−1).
For m ≡ 2 (mod 4) put N₂ = m/2 and η₂ = Σ_{j<N₂} α^{2j}.
Ring identities (checked exactly): η(α^4−1) = δ := α^m−1,
η = η̄·α^{4(N−1)}, (α^4−1)/(4√2) = 102+72√2 ∈ R,
(α^2−1)/(4√2) = 3+2√2 ∈ R.

**Periodicity lemma.** W_i := η·y_i ∈ R/qR is 4-periodic
(2-periodic for η₂). Proof: u_i = y_{i+4}−y_i = Tr(Aα^i(α^4−1));
η·Tr(z) = Tr(ηz) + (η−η̄)z̄ with z = Aα^i(α^4−1).
Tr(ηz) = Tr(Aα^iδ) = Ỹ_{i+m}−Ỹ_i ∈ qℤ. The error is
(η−η̄)z̄ = (α^4−1)·Σ″·β^i·Āδ̄ ∈ qR, since (α^4−1)/(4√2) ∈ R and
4√2·Āδ̄ ∈ qR (from the system E_0 = Ỹ_m−Ỹ_0, E_1 = Ỹ_{m+1}−Ỹ_1 ∈ qℤ:
αE_0−E_1 = 4√2·Āδ̄). The same argument with 2 in place of 4 gives
2-periodicity for η₂.
Hence {η·y_i} = {W_0,…,W_3}×(m/4) is fibre-invariant (η acts
pointwise on the values), and likewise for η₂.
Numerically: periodicity of η·y_i holds on all 8192 points at (32,8192).

## 2. W_r = S_r + error, with the error determined by S

Write C = Aη, D = Āη, so W_r = Cα^r + Dβ^r, and S_r = Tr(Cα^r).
Then W_r − S_r = (D−C̄)·β^r =: e_0·β^r, where
e_0 = C̄·Λ, Λ = α^{4(N−1)}−1, since D−C̄ = Ā(η−η̄) = C̄Λ.
Moreover C̄ = (αS_0−S_1)/(4√2) (solving Tr(C) = S_0, Tr(Cα) = S_1),
and C̄·ε = −α^4·Āδ̄ ∈ (q/(4√2))R, so e_0 ∈ (q/(4√2))R.

## 3. Odd q: W = S exactly

At odd q, N(4√2) = −32 is a unit, so 4√2 is a unit in R/qR,
hence e_0 ∈ qR and W_r = S_r exactly. The S-multiset is therefore
fibre-invariant. Then:
- **C = 4, p ≠ 3:** N(ε) = −1152 is prime to q, so ε is a unit;
  Cε = Aδ ∈ qR (from 4√2·Aδ ∈ qR) gives C ≡ 0, so S = 0. Trivial.
- **C = 4, q = 3^e:** C = 3^{e−1}c, c ∈ R/3R (ε = 24·unit, so
  Ann(ε) = {3^{e−1}·c}). S-multiset/3^{e−1} = {Tr(cα^r) mod 3}
  takes only 3 values — (0,0,0,0), (0,0,1,2), (1,1,2,2) — each a
  single dihedral orbit of c (finite check in wave42_Stuple_check.py).
  Hence S is determined up to dihedral.
- **C = 2, q odd:** α^2−1 has norm −32, hence is a unit;
  C₂(α^2−1) = Aδ ∈ qR gives C₂ = 0, so S = (0,0). Trivial.
- **C = 1:** S = Σy_i is determined by the multiset. Trivial.

## 4. 2-part, C = 4 (f = 2v₂(m)+3 ≥ 7)

Wave 41 §6: S = 2^{f−5}·s, s_r = (3a+8c, a, 3a−8c, 17a−48c),
(a,c) ∈ ℤ/32 × ℤ/4; rotation (a,c) ↦ (3a−8c, −a+3c), reflection
(a,c) ↦ (17a−48c, −6a+19c) (both map S correctly, checked).
From §2: e_0 = (αS_0−S_1)·6α^2Σ″ = 2^{f−4}·6α^2Σ″T, where
T = (4a+12c)+(3a+8c)√2 and Σ″ = Σ_{j<N−1} α^{4j}.
Scaled (÷2^{f−5}): w_r = s_r + 12α^2Σ″T·β^r ∈ R/32R, with
Σ″ ≡ (N−1) + 24K√2 (mod 32R), K = (N−2)(N−1)/2 — determined by
N mod 32. The w-multiset is fibre-invariant (it is the scaled
η-multiset). Finite check over all N mod 32 and all (a,c):
1248 w-groups, each a single dihedral orbit — 0 bad. Hence the
fibre determines S up to dihedral.

## 5. 2-part, C = 2 (f = 5, q = 32)

Wave 41 §6: S_1 = 2b, S_0 = 2(3b+8ε), (b,ε) ∈ ℤ/16 × ℤ/2;
swap (b,ε) ↦ (3b+8ε, b+ε mod 2) is an involution mapping S correctly.
From §2: e_0 = 2^{f−3}·αΣ₂″T₂, T₂ = (4b+12ε)+(3b+8ε)√2,
Σ₂″ ≡ (N₂−1) + 12K√2 (mod 16R), determined by N₂ mod 16.
Scaled (÷2): w_r = s_r + 2αΣ₂″T₂·β^r ∈ R/16R, fibre-invariant.
Finite check over all N₂ mod 16 and all (b,ε): 288 w-groups,
each a single swap orbit — 0 bad. Hence S up to swap-or-equal.

## 6. What this closes, and what it does not

SC-sup is now unconditional (wave 41 task 4 + this lemma).
Δ→0 v3 is conditional exactly on H0 (proved), SCL, SCJ′.
Not claimed: any Lean formalisation of this lemma (not built here),
and nothing about the remaining hypotheses SCL and SCJ′.

Check script: `wave42_Stuple_check.py` (same directory, ALL CHECKS PASS).
