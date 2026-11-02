# Wave 28, task 1 — R30: the P₂ carry-free computation at f = 3, s = 0

**Verdict: P₂ GOES THROUGH unchanged at the v1 level.** For a pure
level-1 twist, v1-marginal preservation forces c = K₁ − 2b₁, and in
the gap case K₁ = 0, so c = −2b₁ — conjugate-triviality mod p²,
exactly as in f = 2. The f = 3 break is one level up: at mod p³ a
residual (1 + p²Q) survives, and its naive formula is FALSE (exact
counterexample below); the corrected formula is given in §4. Only
this P₂ step is proved here; the v2 step is NOT attempted.
Repository untouched, no Lean built.

## 1. Setup (R30's setting)

p odd, R = ℤ[√2], k = 3 (α^{L₀} ≡ 1 mod p³, so β = α^t ∈ T₃, the
Teichmüller group mod p³), H₀ = ⟨β⟩, |H₀| ≥ 3, A a unit mod p³.
Write A = τ_A(1 + pλ₁ + p²λ₂), τ_A ∈ T₃, λᵢ ∈ R/p (normalised
extraction), T_j = τ_Aβ^j ∈ T₃, τ̄_j = T_j mod p = ξ̄_j + η̄_j√2,
t_j = Tr(τ̄_j√2) = 4η̄_j, d1_j = p¹-digit of Tr(T_j).
Orbit values v_j = Tr(Aβ^j) mod p³, v_j = v0_j + p·v1_j + p²·v2_j.

**Digit lemma (carry-free).** Mod p², Aβ^j ≡ T_j(1 + pλ₁), so
v1_j = d1_j + Tr(τ̄_jλ₁) mod p: the p·λ₁ term needs T_j only mod p,
so no Teichmüller digit δ_j enters. (d1_j itself is carry-affected
— wave 24's δ-route dead end — but P₂ never expands it.)

**Twist.** A′ = A(1 + pc√2), c ∈ 𝔽_p^×. Then v0′ = v0 and
v1′_j = v1_j + c·t_j (mod p²: Tr(Aβ^j√2) ≡ t_j mod p).

## 2. P₂ computation (all sums in 𝔽_p)

β̄ ≠ 1 gives Στ̄_j = 0; β̄² ≠ 1, i.e. |H₀| ≥ 3, gives Στ̄_j² = 0.
Hence Σξ̄ = Ση̄ = Σξ̄η̄ = 0 and, with N = N(τ_A),
Ση̄² = −|H₀|N/4 (SIGN CORRECTED, see §5), so Σt = 0 and
Σt² = −4|H₀|N ≠ 0 (p ∤ |H₀|, N a unit).
With λ₁ = a₁ + b₁√2: ΣTr(τ̄_jλ₁)t_j = 16b₁Ση̄² = −4b₁|H₀|N, so
Σv1_jt_j = Σd1_jt_j − 4b₁|H₀|N.
If the v1-marginal is preserved, Σ(v1′)² = Σv1², i.e.
2Σv1t + cΣt² = 0. With c ≠ 0, defining
K₁ = Σd1_jt_j/(2|H₀|N) = 2Σd1_jη̄_j/(|H₀|N):
**preservation forces c = K₁ − 2b₁.** (Same shape as f = 2.)

## 3. Gap symmetry kills K₁

Gap (B_H real mod p) plus wave 27 gives conj(τ_A) = τ_Aτ_β^r mod p³
exactly, and conj(τ_β) = τ_β^{−1} (T₃ conjugation-stable, reduction
injective), so conj(T_j) = T_{r−j} exactly mod p³. Hence
Tr(T_{r−j}) = Tr(T_j) exactly, so d1_{r−j} = d1_j, while
t_{r−j} = −t_j. Reindexing: Σd1t = −Σd1t, so Σd1t = 0 (p odd),
K₁ = 0, and **c = −2b₁**. Then Ā^{−1}A′ ≡ τ_β^{−r} mod p², i.e.
**A′ ∈ Ā·H₀ mod p²: the twist is trivial at level p².** ∎

## 4. Sharp boundary at p³: the residual Q

Mod p³, Ā^{−1}A′ = τ_β^{−r}(1 + p²Q) for some Q ∈ R/p (the
p-coefficient vanishes by §3; verified in all 1636 gap cases).
The naive coefficient formula Q_naive = −4b₁² + 2(b₂−a₁b₁)√2 is
FALSE: at p = 5, A = (14,95), λ₁ = (2,1), λ₂ = (4,1),
Q_true = (1,4) but Q_naive = (1,3). Cause: conjugation and
inversion do not commute with normalised digit extraction — the
p² digit picks up {0,1} carry spills. **Corrected formula,
verified on all 1636 gap cases at p = 5, 7, 13:**
**Q = Q_naive + (0, δ), δ = [b₁≠0] + [2b₁≥p]**
(real part of Q_naive always correct; imag part off by 0/1/2).
Mechanism: conjugation-normalisation spill ([b₁≠0]) plus the
product carry in the p-coefficient sum b₁ + b₁ = 2b₁ ([2b₁≥p]);
both land in the imaginary part only. Q is therefore the input
to the v2 step, not a corollary of P₂.

## 5. Two corrections to inherited formulas

(a) Wave 24 Lemma 3 states Ση̄² = +L₀N/4; exact check gives
**−L₀N/4** (e.g. p = 5 orbit: Ση² ≡ 1, −L₀N/4 ≡ 1, +L₀N/4 ≡ 4).
K's sign flips with it; K = 0, c = −2b₁, Σt² ≠ 0 are unchanged.
(b) Wave 27's gap-symmetry check reduces conj mod p³; an unreduced
conj breaks tuple equality (caught in the check script, not a
mathematical failure).

## 6. Scope (honest)

- Proved: v1-P₂ for R30, including K₁ = 0 in the gap case.
- NOT proved: the v2 step. Flag for it: with δ_j the first
Teichmüller digit of T_j, ΣIm(δ_j)η̄_j ≠ 0 in 1636/1636 gap
cases, so the v2 effective digit e2 = d2 + s1 has a carry term
gap symmetry does NOT kill — the v2 step needs more than §3.
- Checks run on Teichmüller orbits at p = 5, 7, 13 (no k = 3 prime
is known below 2×10⁹; R30's setting itself has β Teichmüller,
which is exactly what was checked). Remaining R30 steps (mod-p
normalisation, r = 2 power sums forcing the twist form, v2-P₂,
full L6 assembly) are untouched by design.

## Files

- This note: wave28_R30_P2.md
- Check: wave28_R30_P2_check.py (ALL CHECKS PASS: K₁ = 0 in 1636
gap cases, P₂ identity exact, p-coefficient vanishes in 1636,
naive Q fails in 1414, corrected Q exact in 1636)
- Prior: wave27_R30_gapcond.md (gap symmetry), wave25_G1_f2s0_close.md
§2 (f = 2 transfer), wave24_seconddigit_b.md Lemma 3 (P₂ at f = 2)
