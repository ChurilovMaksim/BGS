# THEOREM_DRAFT v2 — conditional refutation of frozen R′ (TRACE-206) along m = 3p: the Theorem R♯ path (modulus form)

*v2: Line N17b, 2026-11-01 (Asia/Yekaterinburg, UTC+5). v1 (THEOREM_DRAFT.md, Line N16b) is kept unchanged. v2 adds: the H7 analysis (N17b §1–4), the re-derived → ∞ step (N17b §2), the referee lineN14 findings (§7 below), and a corrected subsequence version.*
- Changes from v1 are listed in §8.
- This file is an assembly. The assembly step itself (§2, "⇒") is [P-sketch, bookkeeping]; it has not been refereed.
- Nothing pushed.

**Labels.**
- [P] proof written out and refereed (or elementary).
- [P-sketch] argument complete in outline.
- [CA] rigorous arb/interval computation.
- [CA-fp] IEEE binary64 with explicit a-priori rounding bounds (not interval arithmetic).
- [N] numerics without error control.
- [H] hypothesis/heuristic.

## 0. One-line status
**Frozen R′ is not refuted.** It is refuted *conditionally* on the open inputs H1–H8 below. No single one of them is close to a routine verification except H6 (explicit p₀) and, possibly, H4 (composite core→true).
- **H7 is a serious, non-trivial input** (N17b). W′ is a plain signed sum; the inclusion threshold excludes no (±2,8) level for m ≥ 15; and K_p levels survive even when h_p is prime.

## 1. Objects (pointers only)
- **Map.** The kicked quantized cat map with λ = 3+2√2 = ε², ε = 1+√2. Levels h_p are the NSW numbers, with λ^p ≡ 1 (mod h_p).
- **Deviation.** W′_m is TRACE-206's deviation; along m = 3p it splits into level contributions Dev_d (N6 §1).
- **Level-h_p sum.** Dev_{h_p} ≥ (n|Z|²/h_p²)(|1+X+Y|² − 1) (N6 §0 item 8, N11b §1):
  - X is the isotropic sum;
  - Y = Y_U (unit points) + Y_mix (mixed: iso mod d, unit mod h_p/d) + partially isotropic points.
- **Gas form.** X = X_coded + X_tail, with X_coded = 2[(1+Λ)^p e^{pΔ} − 1] − (dense part) (N11 §4).

## 2. Conditional main theorem (draft)
**Theorem R♯-mod v2 (draft) [P-sketch assembly of the cited pieces].** Let p be prime and m = 3p, with p ≥ max(p₁, p₀). Here p₁ is the first p where the bracket below is positive: p₁ = 1386 with tails = 0 and n = h_p [arith]; ≈1500 with the v1 tail budgets. Assume H0–H8 hold at p. Put S_ρ = φ⁻¹|Z_ρ|²/h_p and

  B_p := (n/h_p)·[(2(1+Re Λ_lo′ − δ_int)^p − 1 − |X_tail| − |Y| − e^{−0.28p})² − 1] − I_p − ε_16 − ε_fl − ε_other,

  with I_p := σ(K_p)/K_p − 1 ≤ e^γ log log K_p + 0.6483/log log K_p − 1 (Robin), K_p = h_{3p}/h_p = 4h_p² + 3.

Then (N17b §2):

  W′_{3p}/m ≥ −4 + m⁻¹Σ_{ρ=(±2,8)} S_ρ·B_p,  with S_ρ ≥ c·1.1329^m.

So if B_p ≥ κ > 0 for infinitely many p, then W′_{3p}/m → +∞ along them. Frozen R′ asserts W′_m = o(m), so **R′ is false**. Only a positive constant lower bound for the bracket is needed; the gas growth (1+Re Λ)^p is used only to beat I_p ≍ e^γ log p.

**What the gas growth does and does not beat (N17b §2b).**
- *Inherited levels:* G(p) > Robin bound on I_p for all p ≥ 1386 [P-arith]. Hypotheses: gas bound with tails/Y = 0, n = h_p, ε's = 0.
- *Other levels:* the per-level negative deviation is bounded a priori only by the floor (h_p/d)·S_ρ [P]. That is an absolute constant only for d ≳ h_p. The unconditional divisor bound τ(h_m) ≤ e^{Θ(p/log p)} is **not** beaten by G = e^{O(10⁻³p)}.
- Hence H7* is genuinely needed below L_fl.

**Erratum to v1.** The "−0.2·(n|Z|²/h_p²)" term (N10-F3 inherited levels) is not uniform in p. It is replaced by −I_p·S_ρ, which grows like e^γ ln p. The v1 threshold 1289 is replaced by p₁.

(Formula: N11 Theorem N11, as verified in N10b §1 / audit lineN11b; N17b §2. Constants: Re Λ_lo′ = 6.234·10⁻⁴ after the N14 charges, δ_int ≤ 5.14416·10⁻⁷ as printed by the referee (v1 had 5.14415e-7).)

(Formula: N11 Theorem N11, as verified in N10b §1 / audit lineN11b. Constants: Re Λ_lo′ = 6.234·10⁻⁴ after the N14 charges, δ_int ≤ 5.14415·10⁻⁷.)

**Hypotheses (each currently OPEN unless marked otherwise):**

| # | Hypothesis | Status / best partial result | Where |
|---|---|---|---|
| H0 | Standing package of N6 Theorem R♯: Line F/J/J3/L16 trace representation; TRACE-197/199/207/212/213/228; Prop X architecture; n_cert | taken as given. Prop X is [P-sketch] (other-sector part made explicit, N8 §1 item 6); n_cert [CA] | N6 §5, N7 §0, N8 |
| H1 **(T)** collective tail: \|X_tail\| below budget. Precisely, the lattice→collision reduction for shell sums with constant C ≤ 0.082 at J₀ = 12 (ρ̄ = 0.28) | OPEN at [P]. Finite part j ≤ 12 [CA-fp]; rate ρ̄ ≤ 0.28 [CA-fp]; tail j > 12 [H, extrapolation]; ≈150× margin [N] | N14 §2, §6; N13 §4 |
| H2 **(I)** interaction δ_int < Re Λ_lo′ | **met at core level:** δ_int ≤ 5.14416e-7 [CA-fp, core functional; IEEE binary64 standard model + libm ≤ 1 ulp assumptions, referee F14.1] + Lemma D tail ≤ 1.56e-8 [P+N: single-chain norms/Γ are N]. Needs H4 for composite windows | N14 §4–5, N13 §(D), audit lineN13 F1–F3 |
| H3 **(KP)** polymer/KP weight e^{a\|γ\|} and the log→modulus step | [P-sketch] (standard cluster bound) | N11 §4, N14 §1.4 |
| H4 **(CT)** composite core→true conversion (cert_core → true operator) for composite windows | OPEN (single-core: ≤ 2.094e-8 relative [CA]+[P-sketch]) | N13 (B), N14 §5 |
| H5 **(Y_mix)** mixed classes at composite h_p: **(R-mix)** E_{mixed, d} F_p ≤ e^{o(p)} d^c r₂^p with c < 0.387, uniformly in d \| h_p; **or** p ∈ 𝒫 := {p : h_p prime} (then Y_mix = 0) | OPEN. Proved: c_B = 0.7375 [P-sketch], which covers iso parts d ≤ 1.588^p. Evidence c ≤ 0 [N] (N15b, N16b §2). No known theorem applies (N15b §2–3). Infinitude of 𝒫 is an open conjecture | N13b §2, N14b, N15b, N16b |
| H6 **(C′ inputs)** Theorem C′ for unit points Y_U: explicit p₀ (e^{o(p)} made effective); h_p squarefree or conductor-q^a weights; level 7h_p unit points (audit N3-F8/F9) | C′ is [P+CA mod these]; p₀ not computed; squarefreeness of h_p unknown in general | N2, N3, audit lineN3 |
| H7 **(Levels ≠ h_p)**, precise form **H7*** (N17b §2–3): for every included level d ∉ {h_p} ∪ {e·h_p} with d < L_fl ≈ 4τ(h_m)h_p/(G − I_p) = h_p^{1+o(1)}, \|Lin_d\| ≤ ε_d\|Z_ρ\|²/h_p with Σε_d ≤ κ₀. Equivalently, cross-correlations grow at a rate below T′ = μ/ε^{1/3} = 1.4279. **Covered:** d = 7 (Line J rate 1.2837 [CA]); Weil-range prime levels (TRACE-244/245, conditional on OP); inherited e·h_p (floor, I_p) [P]; d ≥ L_fl (floor) [P]; inclusion threshold: all (±2,8) levels included for m ≥ 15 [P given TRACE-199], and excluded (±2,16) levels are harmless [P] | **OPEN** for three classes: **hp-div** (d \| h_p, composite h_p; subgroup type like R-mix); **K_p levels** (d \| K_p, ord 3p, need equidistribution ≈3× past separation); **mixed**. The G* route is closed (N12b). Trivial sup bound is short by a factor 1.026 per step. Numerics [N] (N17b §4): non-h_p Dev has mixed signs but is small, \|rel\| ≤ 6.4e-3 (m = 21), ≤ 1.6e-5 (m = 33); at m = 21 Σ_{d≠h_p} is ≤ 5.4% of Dev_{h_p} | N6 §5, N8b §8, N10b, N12b, **N17b** |
| H8 **(Wrap)** deep wrap-around points of gap (a) (span ≥ ℓ₀) | prime h_p: Parseval exact, needs only the H1-type constant [P-sketch]. Composite h_p: see N16b §1. Free (c = 0) if per-point weights are not d-amplified; otherwise trivial c = 1, which covers d ≤ e^{0.967ℓ₀} = λ^{0.549ℓ₀} (ρ̄ = 0.30) / e^{1.175ℓ₀} = λ^{0.667ℓ₀} (ρ̄ = 0.28), with ℓ₀ in λ-steps. **Units (v2):** the condition is c < 0.967ℓ₀/ln d = 0.549ℓ₀/log_λ d. N14 §3 printed "0.97·ℓ₀/log_λ d", off by ln λ = 1.763; N14 is not edited (N16b §1(b)) | N14 §3, N16b §1 |

**Subsequence version (corrected in v2).** On 𝒫 (h_p prime), H5 holds automatically, H6's squarefree clause is trivial, and H8 reduces to H1. In H7, the hp-div and mixed classes vanish, but **the K_p levels remain**: K_p = 4h_p² + 3 is composite with many divisors in general, and 7 | K_p. **R′ fails along m = 3p, p ∈ 𝒫, if H0–H4, H6 (p₀ only), H7*(K_p levels) hold and 𝒫 is infinite.** v1 wrongly suggested that prime h_p leaves H7 essentially to d = 7.
- 𝒫 ∩ [5, 300] = {5, 7, 19, 29, 47, 59, 163, 257} (referee lineN14 confirmed; p = 3 is excluded by range). p = 31 is confirmed as listed in N14b.
- Note that h_{3p} itself need not be squarefree (h_15 = 7·31²·41).

## 3. Ingredients that are proved (with label and file)
| Ingredient | Label | File |
|---|---|---|
| Positivity lemma; sign identity; trivial floor; squarefree reduction of the driver | [P] | N6 §1, §5–6 |
| (±2,16) closed at all levels for p ≥ 339 | [CA]+[P] | N7 §1 |
| Lemma P (family pattern), Lemma P′ (all isotropic points at q = h_p) | [P] | N7 |
| Lemma P′_c (exact orbit lemma at residual levels); classification; weight amplification A_c | [P] | N8b §1–3 |
| Prop X′ explicit error, p ≥ 1289 | [P mod Prop X architecture] | N8 §2, audit lineN12 (provenance) |
| 15 small-depth classes certified (near-0 family positive) | [CA] | N8 §0 |
| Coding lemma for dilute configurations | [P] | N11 §3 |
| \|1+X_gas\| ≥ 2(1+Re Λ)^p − 1 | [P given the model form] | N11 §0 |
| Re Λ_lo ≥ 6.238e-4 | [CA] | N11 §0; N14 uses Re Λ_lo′ = 6.234e-4 |
| Adapted norm V1–V3, Lip_H, quadratic step bound N_H(t) ≤ 1 + 1.0e-12 + 4.26e3 t² | [CA] | N13 (B), audit lineN12/N13 |
| δ_int ≤ 5.14416e-7 (core functional) | [CA-fp] under IEEE standard model + libm ≤ 1 ulp; c2_mid not rigorous as written (F14.1), so it needs those stated assumptions or the N13 arb replay | N14 §4, audit lineN14 |
| Second-moment rate ρ̄ ≤ 0.28 (core→true ≤ 0.28028) | [CA-fp]; ρ̄ needs a-priori constants or arb (referee); core→true is [P-sketch]; tensor joint-pair claim is [H] | N14 §6, audit lineN14 |
| A_bad finite part j ≤ 12 | [CA-fp] | N14 §6 |
| Theorem C′ (unit points, rates 1.27440 / 1.20428) | [P+CA mod H6] | N2, N3 |
| Lemma 1 (sublattice separation, admissible ideals), with the referee fixes: separation per component (union of 2^{ω(d)} sublattices), factor 8 from the inverse-different lift, sub-box partition in the Bowen count | [P] after the fixes stated in N17b §6 | N14b §2, N17b §6 |
| Lemma 2 (subgroup C′ with c_B = 0.7375) | [P-sketch] | N14b §2 |
| W′ structure: TRACE-213 identity; NR part ≥ −4m; Dev_d has floor only; inclusion threshold excludes no (±2,8) level for m ≥ 15; → ∞ step needs only B_p ≥ κ > 0 | [P] / [P given TRACE-199] / [P-sketch] | N17b §1–2 |
| Negative results: D1 + G*_gas route dead for θ ∈ [1/16, 1/4]; 4-fold automaton ≥ 5.41 > 2.611; letterwise CP bound diverges | [N]+[P] / [CA]+[P] / [N] | N12b, audit lineN13; N10b §0 item 3; N14 §2.3 |

## 4. What is unconditionally proved
- **No refutation of R′, conditional on nothing, is proved.** Neither is any single-p inequality W′_{3p} > (TRACE-206 bound) in the large-p regime: Prop X′'s certified errors need p ≥ 1289, and there the open inputs H1–H8 are needed.
- **Unconditional statements are the lemmas of §3,** each as labelled. In particular:
  - the structural identities: positivity lemma, Lemma P/P′/P′_c, coding lemma;
  - the certified constants: Re Λ_lo, the adapted norm, δ_int and ρ̄ at core level;
  - Theorem C′ for squarefree h_p modulo an ineffective p₀;
  - the negative results.
- **Small p are [N] only.** Exact enumerations at small p (p ≤ 13 full; e.g. W′/m = +2.95 at m = 57) are not certified, and are in any case not evidence for the asymptotic statement.
- **Prime h_p at small p.** For each p ∈ 𝒫 the mixed-class input is vacuous, but H1–H4, H6–H7 are still needed, so no fixed p is unconditionally settled.

## 5. Novelty (careful)
- I have **not** done a systematic literature search for prior occurrences of: Lemma P′ (closed-form twist windows of isotropic points); the polymer-gas structure of the level sums; the collision-automaton (Collatz–Wielandt) certificate behind Theorem C′; the subgroup separation lemma.
- They should be described as "obtained in this project" and not claimed as new until checked.
- The literature checked in N15b (BGK; Bourgain; Montgomery–Vaughan–Wooley; Kurlberg–Rudnick; Bourgain LNM 1910; Bonechi–De Bièvre; Faure–Nonnenmacher–De Bièvre) does **not** contain H5. It also shows that H5 is beyond known exponential-sum technology: the subgroup size is ≍ log q, and it sits in the minimal-period regime where the quantum analogue of equidistribution fails (FNDB scars).
- The tested statement (R-mix) is classical and weighted, and FNDB does not refute it.

## 6. Superseded / withdrawn claims (do not cite)
- p-uniform Lemma A∞ (N7/N8): very likely false (N9; [H, model]). Superseded by the modulus/gas route.
- G as stated in N8b: false (N9b), replaced by G*. The G* route via D1 + gas is dead (N12b).
- N12's tail "best cut" (erratum N13); "≈1.5% at G = 13" (N13 §7, withdrawn in N14).
- N14b's (D) value c_D = 0.899 as a "ceiling": it applies to subgroup averages including β = 0, not to mixed sets (N15b).
- N14 §3's formula "c < 0.97·ℓ₀/log_λ d" has a units slip; corrected form in N16b §1.
- v1's "−0.2" inherited-level constant (N10-F3), as a uniform constant: replaced by I_p (N17b §2).
- v1's subsequence version as stated: it omitted the K_p levels of H7.

## 7. Referee lineN14 (/workspace/audit/lineN14/REPORT.md): items reflected
- **N13b and N14b are READY after minor fixes.** The fixes are stated in N17b §5–6:
  - point count 2^{ω(d)}h²/d;
  - S at composite h defined by CRT. At h = 8119, n = 7371; the N6 unit part 7743 differs by n_23 + n_353 = 372, the hp-div members;
  - μ*³/λ = 1.2058;
  - "e^{−0.8p}" softened;
  - Lemma 1 (i)–(iii);
  - μ typo 1.9154732 → 1.9154712.
- **N14 F14.1:**
  - c2_mid is [CA-fp] only under explicit IEEE/libm assumptions, or needs the arb replay;
  - δ_int is printed as 5.14416e-7;
  - ρ̄ needs a-priori constants or arb;
  - the tensor joint-pair claim is [H];
  - core→true is [P-sketch].
- **Referee's "what remains"** (merged with N17b):
  1. Composite mixed: subgroup-C′ with c < 0.387 (H5 = R-mix).
  2. (T): constant ≤ 0.08 at J₀ = 12, the KP weight, wrap-around points (H1, H3, H8).
  3. Composite core→true conversion and the j > 12 tail (H4, H1).
  4. Rigorous c2_mid constants, or the N13 arb replay.
  5. Explicit C′/p₀, a k = O(1) stays lemma, the R₄ automaton (H6).
  6. Lemma 2 from [P-sketch] to [P].
  7. *(added by N17b)* **H7\***: signed control at hp-div, K_p and mixed levels below L_fl (rate T′ = 1.4279). Also the explicit p₁ with all tail budgets included.

## 8. Changes v1 → v2
- §0: added a status note that H7 is serious.
- §2: added the gas-vs-Robin/τ statement (N17b §2b).
- §2: theorem restated with an explicit bracket B_p and the → ∞ step. I_p (Robin) replaces 0.2. p₁ ≈ 1386–1500 replaces 1289. δ_int printed as 5.14416e-7.
- H7 row rewritten (H7*, classes, numerics).
- H8 units made explicit.
- Subsequence version corrected (K_p levels). NSW list extended to ≤ 300.
- §3 labels updated per referee F14.1. Lemma 1 marked [P] after the fixes.
- §6–7 added.
