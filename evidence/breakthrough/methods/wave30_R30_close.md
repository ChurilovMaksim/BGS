# Wave 30, task 1 — R30: normalisation, twist-form reduction, assembly

**Verdict: R30 is NOT fully closed.** Mod-p normalisation is proved
(transfer) and twist-form reduction is proved at level p — but its
naive strengthening to pure-twist form is FALSE, with the sharp
boundary Re(λ₂) = b₁². The generalised-twist assembly then closes
everything except ONE named joint-distribution lemma, verified
exactly in 2187 gap cases. Repository untouched, no Lean built.

## 0. R30 (G1 at f = 3, s = 0)

p odd, |H₀| ≥ 3, β ∈ T₃ of order |H₀|, C, C′ units mod p³ with equal
H₀-orbit multisets {Tr(Cβ^j)} = {Tr(C′β^j)} mod p³. Claim: C′ ≡ Cβ^j
or C̄β^j mod p³. Divisible case: routine induction (p | C, C′ both
or neither by the mod-p norm argument; divide by p, apply f = 2 L6).

## 1. Mod-p normalisation: PROVED (transfer)

Equal mod-p³ multisets reduce mod p; |H₀| coprime to p. The wave-11
mod-p machinery (wave-25 §3 step 1, a mod-p statement) gives
C′ ≡ Cz₀ or C̄z₀ mod p. Absorb z₀ (orbit unchanged); in the
conjugate branch replace C by C̄ (β̄ = β⁻¹ permutes H₀, orbit
unchanged). Hence C′ = C(1 + pλ₁ + p²λ₂), λᵢ ∈ R/p. No new input
needed: this step is identical at every f.

## 2. Twist-form reduction: PROVED at level p, FALSE as pure twist

For C′ = C(1 + pλ₁ + p²λ₂), the r = 2 power sum gives, exactly:
p-coefficient of Σ(v′)² − Σv² is 4|H₀|N·Re(λ₁) (uses Σβ^{2j} = 0);
if Re(λ₁) = 0, the p²-coefficient is 4|H₀|N·(Re(λ₂) − Im(λ₁)²)
(uses ΣvW = 0, ΣW² = −4|H₀|N from wave 29). Verified in 540 cases.
Hence preservation forces **Re(λ₁) = 0**, i.e. λ₁ = b₁√2: the twist
form at level p. But it also forces Re(λ₂) = b₁², NOT λ₂ = 0 — so
the p²-term survives and no r = 2 argument reduces to a pure twist.
The wave-28/29 pure-twist results therefore do NOT apply directly;
the assembly must run on generalised twists C′ = C(1 + pb₁√2 + p²λ₂).

## 3. Assembly

**Gap dichotomy (r = |H₀|).** Σv^{|H₀|−1}W = |H₀|√2(B_H − B̄_H)
(middle terms cancel for even |H₀|), so the p-coefficient of
Σ(v′)^{|H₀|} − Σv^{|H₀|} is |H₀|²b₁√2(B_H − B̄_H) (verified, 540
cases). Preservation ⟹ b₁ = 0 or B_H real mod p (gap).

**Non-gap case: CLOSED.** b₁ = 0, so C′ = C(1 + p²λ₂); r = 2 mod p³
gives Re(λ₂) = 0, λ₂ = d√2; r = |H₀| mod p³ gives
|H₀|²d√2(B_H − B̄_H) ≠ 0 unless d = 0 (non-gap!) ⟹ C′ = C mod p³.
Sweep: 540 non-gap cases, 0 nontrivial preserving twists. ∎

**Gap case.** Wave-27 gap symmetry holds. P₂ (wave 28) applies to
generalised twists unchanged (v1 shift is b₁t_j regardless of the
p²-term): b₁ = 0 or C′ ∈ C̄·H₀ mod p².
- b₁ = 0: C′ = C(1 + p²ν). Ring r = 2 ⟹ Re(ν) = 0, ν = f√2.
  v2-marginal second sum (gap kills Σd2·t) ⟹ f(2d₂ + f) = 0,
  d₂ = Im(λ₂) of the base: f = 0 (⟹ C′ = C ✓) or f = −2d₂, which
  is conjugate-trivial (C′ ∈ C̄·H₀ mod p³, since b₁ = 0). ✓
- b₁ ≠ 0: C′ = C̄h(1 + p²σ). Multiset equality transfers to the
  p²-twist of base C̄ (b₁(C̄) = −b₁ ≠ 0): ring r = 2 ⟹ Re(σ) = 0;
  v2-marginal ⟹ σ = g√2, g ∈ {0, 2d₂}. g = 0 gives C′ = C̄h ✓.
  The spurious g = 2d₂ branch is killed ONLY by the joint
  distribution (see §4) — this is the remaining gap.

## 4. The remaining gap: Joint Lemma (numerically verified, unproved)

**Joint Lemma.** Gap-case base B with Im(λ₁^B) ≠ 0, σ ≠ 0: the
p²-twist B(1 + p²σ) never preserves the H₀-orbit multiset mod p³.
Evidence: 2187 gap cases (p = 5, 7, 13, Teichmüller orbits), 0
non-D-related preserving twists; joint (v0, v1) → v2 distribution
matches 0/1221 for the spurious branch. Why moments cannot prove
it: the v2-marginal multiset still matches in 170/1221 cases; fiber
power sums match IDENTICALLY for f = −2d₂ (third fiber moment
cancels term by term); the orbit product matches in 1202/1202
spurious cases. The proof must use multiset structure, not moments.

## 5. Consequence

R30 holds modulo the Joint Lemma; G1 at f = 4, case (3,1) is
therefore closed modulo R30 modulo exactly this lemma. The two
pieces named in the task: normalisation ✓ proved, twist-form
reduction ✓ proved at level p with the sharp boundary of §2 —
its pure-twist form fails, and the workaround is the
generalised-twist assembly of §3 plus the Joint Lemma of §4.

## Files

- This note: wave30_R30_close.md
- Checks: wave30_R30_close_check.py (Q1 identities, Q2 p²-twist
  sweep); diagnostics in-session (joint distribution, product)
- Prior: wave28_R30_P2.md, wave29_R30_v2.md, wave27_R30_gapcond.md,
  wave25_G1_f2s0_close.md §3 (f = 2 chain this mirrors)
