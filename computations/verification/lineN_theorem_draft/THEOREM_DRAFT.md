# THEOREM_DRAFT — conditional refutation of frozen R′ (TRACE-206) along m = 3p: the Theorem R♯ path (modulus form)

*Draft assembled in Line N16b, 2026-11-01 (Asia/Yekaterinburg, UTC+5), from Lines N2–N16b and the referee reports /workspace/audit/lineN*/REPORT.md up to lineN13.*
- /workspace/audit/lineN14 existed at drafting time but contained no REPORT.md, so the N14 referee findings are **not** incorporated.
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

## 1. Objects (pointers only)
- **Map.** The kicked quantized cat map with λ = 3+2√2 = ε², ε = 1+√2. Levels h_p are the NSW numbers, with λ^p ≡ 1 (mod h_p).
- **Deviation.** W′_m is TRACE-206's deviation; along m = 3p it splits into level contributions Dev_d (N6 §1).
- **Level-h_p sum.** Dev_{h_p} ≥ (n|Z|²/h_p²)(|1+X+Y|² − 1) (N6 §0 item 8, N11b §1):
  - X is the isotropic sum;
  - Y = Y_U (unit points) + Y_mix (mixed: iso mod d, unit mod h_p/d) + partially isotropic points.
- **Gas form.** X = X_coded + X_tail, with X_coded = 2[(1+Λ)^p e^{pΔ} − 1] − (dense part) (N11 §4).

## 2. Conditional main theorem (draft)
**Theorem R♯-mod (draft) [P-sketch assembly of the cited pieces].** Let p be prime, p ≥ max(1289, p₀), and assume H0–H8 hold at p. Then

  Dev_{h_p} ≥ (n|Z|²/h_p²)·[(2(1+Re Λ_lo′ − δ_int)^p − 1 − |X_tail| − |Y| − e^{−0.28p})² − 1] − 0.2·(n|Z|²/h_p²).

Together with the N6 positivity lemma and level bookkeeping (H7), this is meant to give W′_{3p} − (TRACE-206 bound) → +∞ along such p. The precise growth statement should be re-derived from N6 §5 and N11 §4 when the assembly is refereed; I do not restate it here. **If H0–H8 hold for infinitely many p, frozen R′ is false.**

(Formula: N11 Theorem N11, as verified in N10b §1 / audit lineN11b. Constants: Re Λ_lo′ = 6.234·10⁻⁴ after the N14 charges, δ_int ≤ 5.14415·10⁻⁷.)

**Hypotheses (each currently OPEN unless marked otherwise):**

| # | Hypothesis | Status / best partial result | Where |
|---|---|---|---|
| H0 | Standing package of N6 Theorem R♯: Line F/J/J3/L16 trace representation; TRACE-197/199/207/212/213/228; Prop X architecture; n_cert | taken as given. Prop X is [P-sketch] (other-sector part made explicit, N8 §1 item 6); n_cert [CA] | N6 §5, N7 §0, N8 |
| H1 **(T)** collective tail: \|X_tail\| below budget. Precisely, the lattice→collision reduction for shell sums with constant C ≤ 0.082 at J₀ = 12 (ρ̄ = 0.28) | OPEN at [P]. Finite part j ≤ 12 [CA-fp]; rate ρ̄ ≤ 0.28 [CA-fp]; tail j > 12 [H, extrapolation]; ≈150× margin [N] | N14 §2, §6; N13 §4 |
| H2 **(I)** interaction δ_int < Re Λ_lo′ | **met at core level:** δ_int ≤ 5.14415e-7 [CA-fp, core functional] + Lemma D tail ≤ 1.56e-8 [P+N: single-chain norms/Γ are N]. Needs H4 for composite windows | N14 §4–5, N13 §(D), audit lineN13 F1–F3 |
| H3 **(KP)** polymer/KP weight e^{a\|γ\|} and the log→modulus step | [P-sketch] (standard cluster bound) | N11 §4, N14 §1.4 |
| H4 **(CT)** composite core→true conversion (cert_core → true operator) for composite windows | OPEN (single-core: ≤ 2.094e-8 relative [CA]+[P-sketch]) | N13 (B), N14 §5 |
| H5 **(Y_mix)** mixed classes at composite h_p: **(R-mix)** E_{mixed, d} F_p ≤ e^{o(p)} d^c r₂^p with c < 0.387, uniformly in d \| h_p; **or** p ∈ 𝒫 := {p : h_p prime} (then Y_mix = 0) | OPEN. Proved: c_B = 0.7375 [P-sketch], which covers iso parts d ≤ 1.588^p. Evidence c ≤ 0 [N] (N15b, N16b §2). No known theorem applies (N15b §2–3). Infinitude of 𝒫 is an open conjecture | N13b §2, N14b, N15b, N16b |
| H6 **(C′ inputs)** Theorem C′ for unit points Y_U: explicit p₀ (e^{o(p)} made effective); h_p squarefree or conductor-q^a weights; level 7h_p unit points (audit N3-F8/F9) | C′ is [P+CA mod these]; p₀ not computed; squarefreeness of h_p unknown in general | N2, N3, audit lineN3 |
| H7 **(Levels ≠ h_p)** level bookkeeping: d = 7 [CA]; Weil-range prime levels (Theorem W/W⁺ as registered, TRACE-244/245, conditional on OP); d > L* trivial floor [P]; inherited levels e·h_p floor ≤ 0.2 [P]; residual isotropic classes at proper divisors are deep gap-(a) classes [P] (N8b Lemma P′_c) | the remaining residual patterns (rank-3p/K_p levels; inconsistent/partially isotropic lines) were reduced to G*(Γ < T′) (N8b, N10b §1). **The G* route is closed negatively** (N12b; audit lineN13). OPEN; numerics Γ_eff ≤ 1.069 [N] | N6 §5, N8b §8, N9b, N10b, N12b |
| H8 **(Wrap)** deep wrap-around points of gap (a) (span ≥ ℓ₀) | prime h_p: Parseval exact, needs only the H1-type constant [P-sketch]. Composite h_p: see N16b §1. Free (c = 0) if per-point weights are not d-amplified; otherwise trivial c = 1, which covers d ≤ e^{0.967ℓ₀} (ρ̄ = 0.30) / e^{1.175ℓ₀} (ρ̄ = 0.28), with ℓ₀ in λ-steps | N14 §3, N16b §1 |

**Subsequence version.** On 𝒫 (h_p prime), H5 holds automatically, H6's squarefree clause is trivial, and H8 reduces to H1. **R′ fails along m = 3p, p ∈ 𝒫, if H0–H4, H6 (p₀ only), H7 hold and 𝒫 is infinite.** For p ≤ 89, 𝒫 ∩ [5, 89] = {5, 7, 19, 29, 47, 59} [N, sympy primality].

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
| δ_int ≤ 5.14415e-7 (core functional) | [CA-fp] | N14 §4 |
| Second-moment rate ρ̄ ≤ 0.28 (core→true ≤ 0.28028) | [CA-fp] | N14 §6 |
| A_bad finite part j ≤ 12 | [CA-fp] | N14 §6 |
| Theorem C′ (unit points, rates 1.27440 / 1.20428) | [P+CA mod H6] | N2, N3 |
| Lemma 1 (sublattice separation, admissible ideals) | [P] | N14b §2 |
| Lemma 2 (subgroup C′ with c_B = 0.7375) | [P-sketch] | N14b §2 |
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
