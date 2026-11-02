# Wave 46, task 10 — Δ → 0 v4: one conditional theorem

## Verdict

**Theorem (v4).** Assume (W₂), (SCJ′), and the 2-part polynomial
bound (T_k pattern). Then Δ(m) → 0. Everything else on v3's
list is now proved, dropped, or verified to 10¹⁰. The weakest
remaining piece is W₂ in general (open Wieferich-type problem,
no theoretical approach); second is SCJ′ uniformity beyond the
9t family; third is the 2-part, now a concrete lemma program.

## 1. Hypothesis ledger (exact, minimal)

| Hypothesis | Status in v4 | Evidence / closing route |
|---|---|---|
| H0 (only-split-contributes) | PROVED | Wave 35, Lemma F exponent identity |
| SC-sup (support constant on component fibers) | PROVED | Wave 42, S-tuple dihedral lemma (unconditional) |
| SIZE s_q ≤ m², RB3′ (Q₂, S₂ ≤ 8m²), H12-poly, Lemma 9-split | PROVED | Waves 34, 32, 31, 29 |
| F2-poly (pure form max\|f_qt\| ≤ m^b) | DROPPED | Wave 41: wave-35 §4 counting already closes mechanism B; f = 2 via wave-34 bound |
| SCL (n_q ≤ 10) | DEAD as stated, REPLACED | Wave 35: n_q = 18 at (816, 17⁴); replaced by SCL-poly below |
| SCL-poly, odd p: n_q ≤ 2m^{2e}·log₂m | PROVED modulo W₂ | Wave 43: tower + LTE + N(b) ≤ 2p^{2e}/d; e = 1 unconditional (≤ 2m²·log₂m) |
| W₂: e(p) ≤ 2 for all odd p | OPEN in general; VERIFIED to 10¹⁰ | Wave 45: 455,052,510 primes scanned; e = 2 exactly at 13, 31, 1546463; no e ≥ 3 anywhere ≤ 10¹⁰ |
| SCJ′: Σ_{|S|≥2} Δ_F ≤ D_m^γ, uniform γ < 1 | OPEN in general | 9t route γ = 1/3: see §3 |
| 2-part polynomial bound (T_k pattern) | OPEN in general | Modulo Gap G (all 2^k) + Lemma U (general); see §4 |

Minimality: no proved item is listed as a hypothesis, and no
open item on the list is implied by the others. Under W₂ the
below-base e ≥ 3 hole (wave 43 §5: levels 2..e unproved) is
vacuous, since no e ≥ 3 prime exists; without W₂ it is a
separate fourth gap, needing an e ≥ 3 prime (none known).

## 2. Proof skeleton (mechanisms A/B/C, wave-40 trichotomy)

Δ(m) ≤ 16·ΣΔ_F/D_m, D_m ≥ ρ^m − 2, ρ = 3+2√2, so any
polynomial total and any D_m^γ total (γ < 1) give Δ → 0.

- (A, odd part). Σ_odd n_q s_q² ≤ 5.08·m^{2E+5}·log₂m under
  W_E (wave 43 §5); N_A ≤ (Σ/4)·Q₂, M_A ≤ 8m⁴, hence
  ΣΔ_F(A_odd) ≤ 650·m^{2E+15}·log₂m (arithmetic rechecked:
  5.08/4·8·64 = 650.24). Under W₂: ≤ 650·m¹⁹·log₂m = o(D_m).
- (A, 2-part). Needs the T_k polynomial bound (open, §4).
- (B, twin identification). Closed: wave-35 §4 counting for
  f ≥ 3, wave-34 bound |f_qt| ≤ 2m·p² for f = 2, H12-poly
  Σ twin qt ≤ D_m·18u³/α^{8u} beats every polynomial
  prefactor. No open hypothesis.
- (C, joint splits). By SCJ′ directly: ΣΔ_F(C) ≤ D_m^γ,
  γ < 1 uniform, so ΣΔ_F(C)/D_m ≤ D_m^{γ−1} → 0. No
  per-tuple counting, no B(m) needed.
Every contributing fiber is in A ∪ B ∪ C by H0, so
ΣΔ_F ≤ poly(m) + o(D_m) + D_m^γ = o(D_m). ∎

## 3. Inside SCJ′: the 9t route to γ = 1/3 (what is proved)

SCJ′ as a bare statement stands or falls on its own; the
9t family is the extremal observed case (largest sections
~D_m^{1/3}; m = 60 sections are tiny against D_m), and its
justification now rests on:

- (F1) 729 splits with a top-digit colliding pair: VERIFIED
  at m = 36, 180, 252 (wave 42); proof in general open.
- (F2) Enough D_{3t} components non-split and all-blind for
  the 729-move (conditions v₃(d_a) ≤ 1, v₃(period o) ≤ 1):
  VERIFIED at m = 180, 252 (wave 42); proof open.
- (F3) Uniform phase gap: PROVED modulo H-quad + H-diff for
  the counted fiber-0 top-digit pair at 729 (wave 45): gap
  exactly 2π/3, Δ_F ≥ 3|O||O′| per fiber, verified at
  m = 36, 72, 144, 180, 252. H-quad/H-diff are verified
  exactly at 180, 252 but NOT derived from the definitions
  of Q, P, W. Scope 36 | m, v₃(m) = 2; the 36 ∤ m case open.
- (F4) Distinctness: PROVED via the swap-free criterion
  (wave 43) except the gcd(d_a, 36) = 1 regime, which looks
  vacuous (wave 44 numbers: d_a = 8, 16, 30, 21 at
  m = 72, 144, 180, 252; none at m = 36) but the vacuity is
  NOT proved; m = 108 undetermined (non-standard, 3 | t);
  large odd components at m = 72, 144 untested.
What SCJ′ still lacks beyond 9t: any bound for non-9t
families uniform in m. No family observed threatens it
(falsifier would need ΣΔ_F(C) ≥ D_m^γ for every γ < 1).

## 4. Inside the 2-part: Gap G + Lemma U status

- Gap G proved at m = 32, 64, 128, 256, 512 (waves 40–43,
  45). Remaining for all 2^k: (PAR) parametrisation in
  general (verified to 512); (DIV) for general j (proved
  at j = 7 modulo PAR, wave 45); mod-16 existence of a
  sharing step-16 class at j ≥ 11 (rule proved at j = 9,
  10, wave 45).
- Lemma U: full-cycle rigidity proved at m = 30 and m = 60
  complete (waves 42, 44); in general the alignment theorem
  holds modulo exactly L1 (value multiset determines a
  β-cycle), L3 (no single-component recombination), plus
  the degenerate locus (wave 45; scalings are degenerate,
  not a mechanism). Given Gap G at each level, T_k rests
  only on Lemma U.
So the 2-part is a finite named-lemma program, not an
open-ended search.

## 5. Finite-range corollary

For m ≤ 10¹⁰, W₂ is a verified fact for every relevant
prime (p ≤ m in the tower regime; wave 45 §5), so the
odd-part bound is unconditional there: ΣΔ_F(A_odd) ≤
650·m¹⁹·log₂m. The only caveat is the doubly-hypothetical
below-base e ≥ 3 case (needs an e ≥ 3 prime p > 10¹⁰ with
d | m, p ∤ m; no such prime is known anywhere). Hence:

**Corollary.** For m ≤ 10¹⁰, Δ(m) → 0 conditional on SCJ′
and the 2-part bound only. In general, conditional on W₂,
SCJ′, and the 2-part bound.

## 6. What closes v4 (shopping list for v5)

1. W₂ in general — the weakest piece: boundedness of e(p)
   is a Wieferich-type open problem; the only available
   move is further verification (10¹¹ ≈ 6–7 core-hours).
2. SCJ′: general proofs of F1, F2; derivation of H-quad/
   H-diff from Q, P, W; proof of F4-vacuity in the
   gcd = 1 regime (incl. m = 108 and large odd components);
   extension of F3 beyond 36 | m; a uniformity argument
   for non-9t families.
3. 2-part: PAR in general; DIV for general j; mod-16
   existence at j ≥ 11; L1, L3, and the degenerate locus
   for Lemma U.

## 7. Not claimed

No Lean built; repository untouched. v4 is an analytic
conditional theorem, not a proof of Δ → 0: three hypotheses
(W₂, SCJ′, 2-part) remain open in general, and the SCJ′
sub-items in §3 are a proof route for the 9t family only.
Nothing here touches BGS-001, TRACE-005, or the spectrum.

## Files

- This note: wave46_Delta_v4.md
- Sources: wave40_Delta_SCJprime.md, wave41_F2poly_status.md,
  wave42_Stuple.md, wave42_SCJprime_F.md, wave43_SCL_oddp.md,
  wave43_SCJprime_F4.md, wave44_F4_gcd1_numbers.md,
  wave45_W2_sweep10.md, wave45_SCJprime_F3.md,
  wave45_GapG_DIV_j7.md, wave45_GapG_mod16.md,
  wave45_LemmaU_general.md. No new check script: the only
  new computation is the §2 coefficient check (650.24),
  done in-line by hand arithmetic above.
