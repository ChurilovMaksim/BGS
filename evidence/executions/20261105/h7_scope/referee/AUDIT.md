# Hostile referee audit: H7*/H8 notes, grok47 directory (PR #85)

Repo `ChurilovMaksim/BGS`, branch `research-grok46-1104`, shallow clone at commit `b8e91215` (committed 2026-11-05 00:29 Europe/Berlin).
Directory `evidence/research/20261104_grok47/`. I audited `proofs/h7_h8.md`, `h7_rates.md`, `h7_multidisc.md` and `h7_scope.md`, together with `code/h7_multidisc_cert.py`, `code/h7_rates.py::newton_enclose` and the logs.
I ran no Lean, pushed nothing and edited nothing in the repo. All 66 entries in `HASHES.txt` match the checkout.

Auditor artefacts: `ints.py` and `ints2.py` (exact integers, sympy/BPSW, deterministic below 2^64), and `mine/krawczyk.py` with its logs `mine/krawczyk_*.json`.

## Summary of verdicts

| # | Item | Verdict |
|---|------|---------|
| 1a | 7 \| K_p and 7 ∤ h_p for every prime p ≥ 5 (h7_h8 Lemma 4) | CONFIRMED |
| 1b | Every prime factor of K_p is ≡ 1 mod 3 (Lemma 3) | CONFIRMED (minor: q = 2 is not excluded explicitly) |
| 1c | gcd(h_p, K_p) = 1 (Lemma 3) | CONFIRMED |
| 2a | 3437426497 \| K_19 and 24061985479 \| K_19 | CONFIRMED |
| 2b | 2735635252619983 \| K_29 | CONFIRMED |
| 2c | d² ≤ h_m, floor(h_m/d²) = 278, 5, 133; not h_p, not e·h_p | CONFIRMED |
| 2d | List of included K_p-divisors used by h7_rates.md | NEEDS FIX: d = 4663 at p = 7 is missing |
| 3a | Re-enclosure of the d = 3437426497 crossing on the multi-disc section | CONFIRMED (independent Krawczyk test, arb) |
| 3b | Level-7 calibration against TRACE-223 | CONFIRMED (plus a new class 0:1 check) |
| 3c | Rigour of `newton_enclose` | CONFIRMED in substance; minor NEEDS FIX (float sums are not directed-rounded) |
| 4a | Per-orbit sufficient reading fails on the finite section | NEEDS FIX (wording: the statement is about the vertex part only) |
| 4b | The aggregate is open | CONFIRMED |
| 4c | v5 is unaffected because p < 1409 | CONFIRMED in conclusion; NEEDS FIX in attribution: the hypothesis list is the draft's 𝒫-subsequence statement, not the TRACE-325 row |
| 4d | No overclaim remains | NEEDS FIX: three small items, listed under 4 |

Nothing is WRONG. No numerical claim I checked failed.

## 1. Arithmetic lemmas (h7_h8.md §1)

**Lemma 4 (7 | K_p, 7 ∤ h_p, p ≥ 5): CONFIRMED.** I checked the proof by hand. Modulo 7 one has u_{n+1} ≡ −u_n − u_{n−1}. From (1, 0) the terms from index 1 run 0, −1, 1 and repeat, so u_n ≡ 0 exactly when n ≡ 1 (mod 3). For the index (p−1)/2 this means p ≡ 3 (mod 6), and the only such prime is 3. Otherwise h_p ≡ ±1, so K_p ≡ 4 + 3 ≡ 0 (mod 7). Also K_3 = 199 ≡ 3 (mod 7), and h_5·K_5 = 41·6727 = 275807.

I checked exactly for every prime 5 ≤ p < 2000:
- 7 | K_p and 7 ∤ h_p;
- 3 ∤ h_p and gcd(h_p, K_p) = 1;
- u_{(3p−1)/2} = h_p·K_p.

All pass. This extends the note's own range, which stops at p ≤ 200.

**Lemma 3 (gcd = 1; q | K_p ⇒ q ≡ 1 mod 3): CONFIRMED.**
- Modulo 3 the sequence is 1, 1, 2, 2, … and never 0, so 3 ∤ h_p.
- The reciprocity computation (−3/q) = (q/3) is correct.
- Minor gap: the text says "for an odd prime q ≠ 3" but never says why q = 2 cannot occur. K_p = 4h² + 3 is odd. Add one clause.

**Factorisations (Prop. 5): CONFIRMED.** I refactored K_p for p ∈ {5, 7, 11, 13, 17, 19, 23, 29, 31}. All factors are below 2^64, so BPSW is deterministic. The results match the table exactly, including 57887325592525441 at p = 23.
- Every factor is ≡ 1 (mod 3).
- Every factor other than 7 is ≡ 1 (mod 6p), which is the N8b congruence.
- The primality of h_p matches the table.

The included divisor lists, recomputed (d | K_p, 1 < d, d² ≤ h_p·K_p, excluding 7):
- p = 19: 457, 3199, 14593, 102151, 6669001, 7521721, 46683007, 52652047, 3437426497, 24061985479. That is ten.
- p = 29: 13921, 97447, 5806729, 40647103, 28073057689, 80835474409, 196511403823, 565848320863, 390805036088569, 2735635252619983. That is ten.

The Prop. 6 integer comparisons were recomputed: 2·169·33·6728 < 3·140·32·6725, and 2·3072² > 2209². Both hold. I found √h_15 = 525.17…, so √h_15 < 526 < 961.

## 2. Inclusion facts (exact integers)

| d | factorisation | p | K_p mod d | gcd(d, h_p) | d² ≤ h_m | floor(h_m/d²) | gcd(β, d) |
|---|---|---|---|---|---|---|---|
| 3437426497 | 457·7521721 | 19 | 0 | 1 | yes | 278 | 1 |
| 24061985479 | 7·457·7521721 | 19 | 0 | 1 | yes | 5 | 1 |
| 2735635252619983 | 7·13921·28073057689 | 29 | 0 | 1 | yes | 133 | 1 |

Here h_19 = 9369319 (prime), K_19 = 351136554095047, h_29 = 63018038201 (prime) and K_29 = 15885092554810781265607. All match the notes.

Because gcd(d, h_p) = 1, no d is h_p or e·h_p. Inclusion then follows from TRACE-273, which covers every odd m in [15, 20001], so the separate arb recheck in the note is redundant but harmless. **CONFIRMED.**

The order of λ mod d was recomputed for all 23 conductors of h7_rates Lemma 3. Small d were done by stepping. For the large d I used λ^{3p} = 1, λ^p ≠ 1 and λ^3 ≠ 1. Every order equals 3p, so Lemma 3 is **CONFIRMED**.

**NEEDS FIX (h7_rates.md §0, §8 and `h7_rates.py` line 60):** d = 4663 is missing.
- 4663 | K_7 = 228487, and 4663² = 21743569 ≤ h_21 = 54608393.
- The order of λ mod 4663 is 21.
- h7_h8.md lists it as an included K_7-divisor, but h7_rates.md says "d = 49 at p = 7" and never mentions 4663.

So the count of conductors that were not exhausted is **eighteen, not seventeen**, and 4663 was not searched at all. This affects only the "open" list and changes no verdict.

## 3. Independent re-enclosure and calibration

**Code check of `h7_multidisc_cert.py`, by hand:**
- λ-orbit map (x, y) ↦ (3x + 4y, 2x + 3y) is multiplication by 3 + 2√2.
- Trace: Tr((b_x + b_y√2)(x + y√2)) = 2(b_x·x + 2b_y·y).
- Phase: exp(πi·2n·tw/d)·exp(πi·na/4) = e(n(a/8 + τ)).
- Product order: the first factor is on the right.
- Composition: coefficients C(k, j)·λ^{−j}·B^{k−j}.
- Multiplier and weight: e(Cnc)·exp(2πiCnρu), weight i^n·J_n(1.8)·e(Cn²/2), with C = −1/(4√2). The convention for negative-order J matches `certG_build_sector.py`.
- Core invariance: |c + n| ≤ 19, 19/λ < 3.26, and the rounding margin is certified at > 1e-8.
- Power-of-two scaling is exact.

**Independent method.** `mine/krawczyk.py` reuses only `build_blocks` and `assemble`. Everything else is new:
- my own orbit and trace;
- the product without rescaling, at precision 320;
- a float eigencentre, with the inverse R of the midpoint Jacobian;
- a Brouwer/Krawczyk box test on the exact quadratic expansion F(y0 + X) = F(y0) + J0·X − δμ·δv, where every bound is an arb upper bound;
- R is shown nonsingular by ‖I − R·J0‖∞ < 1.

This shares nothing with their Newton–Kantorovich, Neumann inflation or balancing.

| orbit | P | my box r | my per-step rate enclosure | theirs (log) |
|---|---|---|---|---|
| d = 3437426497, β = (−208, 0), a = 0 | 57 | 9.5e-6 (product scale 2.2e9), ‖I − RJ‖ = 2.7e-7 | [1.45877246639015403, 1.45877246639015426] | [1.458772466390154, 1.4587724663901542] |
| level 7, (2,1), a = 4 | 3 | 3.7e-9 | [1.2835951321515, 1.2835951336547] | [1.2835951329030868, …0901] |
| level 7, (1,3), a = 6 | 3 | 5.5e-10 | [1.2837142951988, 1.2837142954232] | [1.2837142953109737, …9815] |
| level 7, (0,1), a = 0 (new) | 3 | 4.0e-10 | [1.2624306303209, 1.2624306304893] | not run |

How these compare with TRACE-223:
- **2:1:** the interval lies inside the certified disc [1.2835950326, 1.2835952326].
- **1:3:** the upper end is ≤ 1.2837144.
- **0:1:** the upper end is ≤ 1.2624308.

The crossing at d = 3437426497 exceeds T' = 1.42785 by 0.03092. The crossing is **CONFIRMED** and the calibration is **CONFIRMED**.

I also recomputed (r/T')^P = 3.391, 26.135 and 11.626, which matches §6 of h7_multidisc.md.

Side observation (float only): on this orbit |μ₂|/|μ₁| ≈ 2e-16, so the section monodromy is numerically rank one. On the section, Tr ≈ the leading eigenvalue. That is not certified, since the other 279 eigenvalues are not bounded.

**`newton_enclose` (h7_rates.py), minor NEEDS FIX.** The method is sound:
- the midpoint Jacobian inverse comes from an exact solve;
- the Neumann inflation by the ∞-norm of the ball radius is correct;
- the Lipschitz constant 2 is correct;
- the residual is computed on the ball.

The issue: β0, δ, the row sums, η and h are accumulated in float64 with round-to-nearest, which is not directed rounding. The margins (h ~ 1e-14 against 1/2, a radius of 5e-15 against gaps of 3e-2) make this harmless, and my independent all-arb test agrees. Still, a [CA] tag should either do these sums in arb or apply an explicit (1 + 1e-12) safety factor.

Reproducibility nit: `h7_rates.py` hard-codes `sys.path` `/workspace/computations/verification/lineI/code`. In a clone the import of `law` fails unless the repo root is `/workspace`.

## 4. Scoping (h7_scope.md, and h7_multidisc.md §6) against record/claims.json

**4a, NEEDS FIX (wording).** "The sufficient per-orbit reading fails on the finite section" is true of the **vertex** section's spectral radius, and that is all that is certified.
- Ẑ = c_m·Σ_a c_a·(Tr V^m − Tr E^m)/3 (TRACE-221).
- The edge section was only floated (rates ≈ 0.35, [N]).
- Trace and spectral radius are not certified to agree (see the side observation in §3).

h7_multidisc.md §5 says this, but the registry-ready note h7_scope.md does not. Add: "certified per-step spectral radius of the vertex section monodromy; the edge comparison and trace-versus-radius are [N] only."

**4b, CONFIRMED.** The closure condition of TRACE-305 is the aggregate bound |Lin_d| ≤ ε_d·|Z|²/h_p with Σ ε_d ≤ κ0. The registry `closure_condition` field says exactly that. The "i.e. growth < T'" in the TRACE-305 title is a sufficient majorant, and no enclosure of Σ_β κ·Ẑ exists at these conductors.

**4c, conclusion CONFIRMED, attribution NEEDS FIX.**
- **The problem.** h7_scope.md (and h7_multidisc.md §6) attribute to "Theorem R♯-mod v5 (BGS-TRACE-325)" the hypothesis list "H0, H1, H6 and H7*, p ≥ p_thr, and 𝒫 infinite." That list is the draft's 𝒫-subsequence statement (THEOREM_DRAFT_v5.md, line 128). The TRACE-325 row itself reads: "H0, H1, H5–H8 hold at p … and B_p ≥ κ > 0 for infinitely many primes p ≥ p_thr."
- **The thresholds are quoted correctly.** The registry and draft give 3307 at C ≤ 0.082 (fragile) and 1409 at C ≤ 8.8e-4 (robust). p_thr is the max of the listed thresholds, with p₀ and the additive budgets not computed, so p_thr ≥ p₁ ≥ 1409 > 29.
- **A stronger reason should be added.** Both forms of the theorem need the hypotheses at infinitely many primes, so a failure at the finitely many primes 19 and 29 cannot fire or block the implication whatever p_thr is.

**4d, remaining overclaim or inaccuracy:**
- (i) The vertex-only wording, as in 4a.
- (ii) The TRACE-325 attribution, as in 4c.
- (iii) h7_rates.md §0 and §8: the 4663 omission, so it should read "eighteen," not "seventeen."

Nothing else in the four notes claims that H7* is refuted, that frozen R′ is touched, or that the untruncated monodromy crosses. The one-step tail (< 9.65e-5) is correctly marked as not a monodromy bound.

Two further minor points:
- h7_h8 Lemma 3 should exclude q = 2 explicitly.
- `newton_enclose` uses float sums (§3).

## Safe registry wording (proposed; registry not edited)

> **H7\* finite-section note (grok47, PR #85; not a claim row).** [P] For every prime p ≥ 5: 7 | K_p, 7 ∤ h_p, gcd(h_p, K_p) = 1, and every prime factor of K_p is ≡ 1 (mod 3). [P, finite] Complete factorisations of K_p for 5 ≤ p ≤ 31. The included K_p-divisors other than 7 at p ∈ {5, 7, 19, 29} are 31, 217; 49, 4663; ten at p = 19; ten at p = 29. [CA, finite section only] On the compression of the TRACE-223 multi-disc **vertex** operator to centres |c| ≤ 3, modes < 40, letters |n| ≤ 16 (calibrated: level-7 classes 2:1, 1:3, 0:1 inside or under the TRACE-223 bounds), the sector-0 per-step spectral radius of one λ-orbit exceeds T' = 1.42785 at d = 3437426497 (p = 19, β = (−208, 0), ≥ 1.4587724663), d = 24061985479 (p = 19, β = (227, 227), ≥ 1.5119805975) and d = 2735635252619983 (p = 29, β = (−89, 0), ≥ 1.4686852948). Each d divides K_p, is coprime to h_p, and has d² ≤ h_{3p} (included by TRACE-273). Consequently a per-orbit cap at T' (the sufficient reading "cross-correlation growth < T'" of TRACE-305) cannot be certified from this section. **Not shown:** any bound on the untruncated monodromy, on the edge operator, on Tr versus spectral radius, or on the aggregate Σ_β κ_d(Nβ)·Ẑ(β). H7\* (TRACE-305) stays open; it is neither proved nor refuted at these levels. Theorem R♯-mod v5 (TRACE-325) is unaffected: its hypotheses are required for infinitely many primes p ≥ p_thr, and p_thr ≥ 1409 > 29. Frozen R′ (TRACE-206) stays open. Conductors not exhausted: 4663 and the seventeen others at p = 19, 29 (eighteen in total).
