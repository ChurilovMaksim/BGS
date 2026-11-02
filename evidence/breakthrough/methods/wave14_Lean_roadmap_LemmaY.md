# Wave 14, task 4 — Lean formalisation roadmap: Lemma Y chain (mod-D level)

Scope: the mod-D Lemma Y sketch only (odd component, P3′, P2 uniform,
per-class pattern lemma, Lemma S, π₂=π₃ compatibility). Exact Pcarry,
G1 at f ≥ 3, and G3 (Lemma PC, general) are OUT of scope — they are
separate open inputs, not roadmap items. No Lean was built here; no
statement below is a Lean theorem yet. Drafts cited are text with
`sorry` placeholders. Mathlib is v4.33.1; builds are sequential only.

Target statement (T7.1): for q ‖ D_m, if y, y′ ∈ Fix_m mod q have the
same multiset mod q, then Y(y′) ∈ D_t · Y(y) mod q, t = gcd(m, 4).

## Stage 0 — Pell / valuation inputs

| # | Theorem (one line) | Source | Mathlib API |
|---|---|---|---|
| T0.1 | Pell recurrences: x_{n+1} = 6x_n − x_{n−1}, (x_m−1)(x_m+1) = 8y_m² | main Derand; `lean-drafts/LineBPellC1Draft.lean` | needs check — known blocker: `gp` cast lemma |
| T0.2 | v₂(D_m) = 2 (m odd), 2v₂(m) + 3 (m even) | `methods/wave11_task3_LTE_v2Dm.md` (proved) | needs check — ℤ[√2] valuations, likely new argument |
| T0.3 | v₃(D_m) = 2 + 2v₃(m/4) for 4 ∣ m | `methods/wave9_lemmaY_P3prime.md` §3 | needs check |
| T0.4 | rad(D_m) = rad(gp) (as primeFactors equality) | wave 3 sketch; `lean-drafts/LineBRadicalDraft.lean` | VERIFIED (wave 6 grep; `Nat.radical` does not exist, restate via primeFactors) |
| T0.5 | SNF of M^m − I is diag(d₁, d₂), d₁d₂ = D_m | `methods/wave8_lemmaY_proof_attempt.md` | needs check — Smith form over ℤ |

T0.4 is optional for this chain (convenience, not critical path).

## Stage 1 — Setup

| # | Theorem | Source | Mathlib API |
|---|---|---|---|
| T1.1 | Fix_m mod q = ker(M^m − I); sequences fixed by (y₀, y₁) | wave 8/9 setup | needs check — elementary linear algebra over ZMod |
| T1.2 | Class sums Y_r; pair identity pairNum(z, w_y) = z·y = z̄·Y(y) | `methods/pair_sorted_identity_note.md` (wave 7) | needs check |

## Stage 2 — Odd component (wave 8)

| # | Theorem | Source | Mathlib API |
|---|---|---|---|
| T2.1 | p ∤ 24 ⇒ Y_r ≡ 0 mod q (component Lemma Y trivial there) | wave 8 §2 | needs check |
| T2.2 | Mod-3 classification of 4-vectors into 3 D₄-types | wave 8 §3; wave 9 Lemma 6 | needs check — finite case split, decidable |

## Stage 3 — P3′ (wave 9)

| # | Theorem | Source | Mathlib API |
|---|---|---|---|
| T3.1 | Scaling: Fix mod 3^{2f₀} = 3^{f₀} · (all sequences mod 3^{f₀}) | wave 9 Lemma 4 | NEW argument — ℤ[√2] mod 3^e valuation (Lemma 1–3 of the note) |
| T3.2 | Top digit: Y′_r divisible by 3^{f₀−1}, Z′ = n₀·v | wave 9 Lemma 5 | NEW argument — same ℤ[√2] machinery |
| T3.3 | Component Lemma Y mod 3^e | wave 9 §7 | assembly of T3.1 + T3.2 + T2.2 |

## Stage 4 — P2 uniform (waves 9–10)

| # | Theorem | Source | Mathlib API |
|---|---|---|---|
| T4.1 | α-power lemma: α^{2^j} ≡ 1 + 3·2^{j+1}√2 mod 2^{j+4}, j ≥ 2 | `methods/wave10_p2_topbit.md` §1 | needs check |
| T4.2 | Doubling: S^{(k)}_r = 2·S^{(k−1)}_r in ℤ/2^{k+3}, k ≥ 4 | wave 10 topbit §3 | needs check |
| T4.3 | Component Lemma Y mod 2^a, by induction from base k ≤ 6 | wave 9 finite base + wave 10 step | needs check — base is a finite check |

## Stage 5 — Per-class pattern lemma (wave 11)

| # | Theorem | Source | Mathlib API |
|---|---|---|---|
| T5.1 | L1: block mod 2^t (t ≥ 5) has period 2^{t−3} | `methods/wave11_perclass_pattern_proof.md` | needs check — follows T4.1 |
| T5.2 | L2: second half = first half + 2^t·δ_s, δ_s constant per class parity | same note | needs check |
| T5.3 | L3: base tuple mod 32; Klein-4 transitivity, 16-case split | same note | needs check — finite case split |
| T5.4 | L4: induction t → t+1 (cases A/B/C); pattern lemma | same note | needs check — hardest step of this stage |

## Stage 6 — Lemma S and compatibility (waves 11–12)

| # | Theorem | Source | Mathlib API |
|---|---|---|---|
| T6.1 | Pair lemma PL: equal pair-unions ⇒ equal pair-profiles | `methods/wave12_lemmaS_proof.md` §1 | NEW argument — induction via T5.2, cases A/B/C |
| T6.2 | Lemma S: ∃δ ∈ Stab(M) with δγ(F) = F for all v-blocks | wave 12 lemmaS §3 | NEW argument — finite D₄ case analysis on 3 block shapes |
| T6.3 | Bijective τ′ : ℤ/P → ℤ/P from global σ (joint-value multisets) | `methods/wave11_task3_pi2pi3_compatibility.md` §1 | needs check |
| T6.4 | π₂ = π₃ compatibility mod D | wave 11 task 3 + T5.4 + T6.2 | assembly — needs check |

## Stage 7 — Assembly

| # | Theorem | Source | Mathlib API |
|---|---|---|---|
| T7.1 | Mod-D Lemma Y (CRT assembly of T2.1, T3.3, T4.3, T6.4) | all above | needs check — CRT over class sums |
| T7.2 | supp φ̂ is a union of fibers (via T1.2 + T7.1) | wave 7 pair identity | needs check |

## Dependency order and hard points

Order: T0 → T1 → (T2, T3, T4, T5 in any order) → T6 → T7.
Hardest: T3.1/T3.2 (ℤ[√2] valuations at 3), T5.4 (pattern induction),
T6.1/T6.2 (Fix-specific pair/stabiliser arguments). Easiest: T2.2,
T5.3, T4.3-base (finite checks). Suggested first Lean milestone:
T0.1 + T0.2 + T1 + T2 (odd component, no pattern machinery).

## Adjacent, not on this chain

- G3 core (`lean-drafts/LineBG3CoreDraft.lean`, 324 lines): API VERIFIED
  wave 10 — all 8 statements need no restatement; only comment fixes
  (normSq names, geom-sum route, gp = 1 edge case). Feeds the
  hEquidistUnits assembly, not Lemma Y.
- G4b (waves 11–12, closed analytically): Lean needs finite-group
  character orthogonality over ℤ²/Aℤ², the SNF dual-grid
  parametrisation, and the strip estimate for ĝ_η — all NEW arguments.
- Units reduction draft (`LineBUnitsReductionDraft.lean`): surjectivity
  of the units lift is the hard step; not needed for Lemma Y mod-D.
