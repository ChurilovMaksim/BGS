# Referee report: Line M (REPORT_M.md sha e3b751f8…, manifest SHA256_M.txt c9a08ee9…)
31 Oct 2026, 15:45 (Asia/Yekaterinburg, UTC+5). Referee work dir: /workspace/audit/lineM (code/, logs/, lean/).
Nothing was written into /workspace/bgs-lineM or any repo clone, and nothing was pushed. `sha256sum -c SHA256_M.txt` passes (6 files).
Author scripts were rerun unchanged with sympy 1.14. Both logs reproduce byte for byte, **including the crash in m_checks.py** (see M-F4).

## Verdict: READY-after-fixes (M-F1 … M-F12)
The headline negative is sound: no unconditional refutation route among (i)–(v) or the author's own ideas. Every route reduces to the signed open-level functional D_iso − E_b/q.
- M1, M2 (first half), M5 and the arithmetic part of M7 are correct as [P].
- M3 and M4 are correct in substance. Their thresholds and constants are overstated as [P]:
  - The m ≥ 11 threshold is float only. The certified threshold is m ≥ 15.
  - The (±2,16) half of M4 is [N].
  - M3's "(1 − o(1))" needs a short argument.
- M6 is mis-summarised in the table. It must stay [H] or conditional.
- M7's literature sentence is too strong as written: Bourgain's input does reach q ≤ p^C.
- None of the fixes changes the conclusion.

| # | Claim | Verdict |
|---|---|---|
| M1 | gcd(h_m,h_n)=h_gcd(m,n), odd m,n; open conductors of distinct m=3p disjoint except 7 | ACCEPT [P] (credit TRACE-230; M-F12). Lean finite check done |
| M2 | positive-weight averaged H♮ ⇒ H♮ (δ/2); signed weights lose positivity | ACCEPT first half [P]. Second half and the "conspiracy consistent" remark are [assessment] (M-F8) |
| M3 | inherited level h_p included and open for every m=3p; capacity ≍ 1.13288^m ≫ 1.0184^m | ACCEPT AFTER M-F1, M-F5 (it is Prop K2's per-level bound evaluated at d=h_p; prime factors of h_p are NOT all open) |
| M4 | (±2,8) rule = all d∣h, 1<d≤√h from m≥11; four families disjoint (3∤h_m) | Disjointness ACCEPT [P] (proof slip M-F3). Degeneration: [P] from m≥15 via Line F F3, [N] at m=11,13 (M-F1). (±2,16): [N], from m≈85 only (M-F2) |
| M5 | squares offset a cross deficit X at level q only if q ≳ \|Z\|²/X; reproduces Prop K2 base | ACCEPT [P] (elementary; it is the Cauchy–Schwarz refinement of K2) |
| M6 | ±ρ antiunitary cancellation at every conductor | NOT [P]. Table statement inconsistent with §7(a) algebra (M-F6). Keep [H]/conditional with closure conditions C1–C4 |
| M7 | ord(λ) ≤ 3p on open conductors; h_p minimal-period (FND); density-one theorems don't apply | Arithmetic ACCEPT [P] (Lean-checked core). Literature: ACCEPT AFTER M-F7 (KR threshold misquoted; Bourgain reaches q ≤ p^C; BGK expansion) |

## 1. Reruns and independent checks
I wrote my own script, code/ref_m.py → logs/ref_m.log. It uses exact integers in ℤ[√2] computed by fast powering, not the author's recurrence.
- [1] Pell h²+1 = 2y² holds for every odd m ≤ 1299.
- [2] M1: 0 failures of gcd(h_m,h_n) = h_gcd(m,n) for odd m, n ≤ 601. The author checked up to 301.
- [3] LTE valuations v_q(h_m) = v_q(h_r) + v_q(m/r): 0 failures in 901 cases (q < 400).
- [4] r(q) lemma (q | h_m ⇔ λ^m ≡ 1 mod q): 0 mismatches for q < 300, odd m < 400.
- [5] 3 ∤ h_m for every odd m < 1300. λ mod 3 has order 4 (λ ≡ −√2), as claimed.
- [6] h_{3n} = h_n(4h_n²+3) holds for every odd n ≤ 431. It is an identity for all odd n (Lean, below).
- [7] gcd(h_{3p}, h_{3p′}) = 7 for all primes 5 ≤ p < p′ < 200.
- [8] For p ≤ 61:
  - Every prime factor q of h_p satisfies q ≡ 1 mod 2p.
  - λ^p ≡ 1 mod 2h_p and λ^p ≢ 1 mod 4h_p.
  - φ(h_p)/h_p ∈ [0.954, 1] and n_{h_p}/h_p ∈ [0.908, 1] for p ≥ 11.
  - The smallest prime factors can be tiny: 23 | h_11, 47 | h_23, 79 | h_13 (M-F5c).
- [9] **Direct membership enumeration (M4).** I tested every unit ν mod 2h, for all four families of P*.
  - The level is d_ρ(ν) = 2h/gcd(bν − a, 2h). It is the unique exact level, and it always divides h.
  - For odd m = 5…19, **no ν lies in two families** with levels ≤ √h (primaries d = 1 included).
  - Each family has exactly one primary.
  - This is the real check. The author's §4 loop only re-tests the gcd arithmetic (M-F3).
- [10] M5 decomposition Dev_d = 2Re(conj Z_ρ·S)/d + Σ|X_ν|² (random data, max relative error 4e-14).
  - This decomposition is **pure algebra at every level d, prime or composite**. G3/K1 is needed only to *name* S as D_iso − E_b/q.
  - The minimum over S is −n|Z_ρ|²/d², which is exactly Prop K2's per-level bound (TRACE-238).
- [11] M6 sign algebra, under c⁻_{a+4} = s_a·conj c⁺_a and conjugate spectra (max error 3e-15):
  - cross₊ + cross₋ = 2Re Σ conj(c_a z_a)c_b y_b·(1 + s_a s_b).
  - So pairs with s_a ≠ s_b cancel, and **pairs with s_a = s_b double, including {2,6}×{2,6}** (M-F6).
- [12] Constants:
  - μ*²/λ^{2/3} = 1.132879, and 1.132879/1.0184224 = 1.112387.
  - μ*²/ξ_lo = 1.492271, λ^{1/6} = 1.34150, λ^{1/4} = 1.55377.
- [13] L_m < √h needs η_m < 0.1009. With η_m ≤ 2.010/log(2p+1) that means p ≳ 2.2e8, consistent with K2's crossover m ≈ 1.68e9 (M-F5d).
- [14, 15] (1+√2)^m mod 8 has period 8, and m ≢ 3m (mod 8) for every odd m. That fact is correct (see M-F9 on its interpretation).
- **Inclusion with actual |Z_ρ|.** Source: Line G float, growth_law.json.
  - (±2,8): |Z|² ≥ 4mh fails at m = 9 and holds at m = 11 (ratio 1.13), m = 13 (2.22) and beyond.
  - (±2,16): |Z|² < 4mh at every m ≤ 29 (the gap is ×24 at m = 29). With the float rate 1.615, extrapolation gives full inclusion only from m ≈ 85.
- **Certified version.** Line F F3 gives |Z_m(ν*)| ≥ ½(1−λ^{−m})(μ_lo^m − 3012.4).
  - From this, |Z|² ≥ 4mh_m holds for every odd m in [15, 20000].
  - Beyond that it is monotone, since the ratio grows like (μ/λ^{1/4})^m/√m = 1.2328^m/√m.

## 2. Claim-by-claim

**M1 [P] — ACCEPT.**
- The argument is: q | h_m ⇔ λ^m ≡ 1 (from ε^{2m} − 1 = 2h_m ε^m for odd m), then LTE for odd q in O/q^k.
- 2 ∤ h_m, so the valuations match and the gcd identity follows.
- The corollary (r(q) ∈ {p, 3p} for q ≠ 7, so distinct m = 3p share only the conductor 7) is correct.
- The r(q) half is TRACE-230 and should be credited (M-F12). Note 49 | h_21 (p = 7).

**M2 — first half ACCEPT [P].**
- The contradiction argument is correct. It needs D7_m > 0 on S⁺ and the same normalisation (with or without φ⁻¹) in the hypothesis and in the divergence condition (M-F8).
- "Signed weights need upper bounds … strictly harder" is an [assessment], not [P].
- "The conspiracy model satisfies every linear relation R′ implies" is a tautology: any sequence that satisfies R′ pointwise satisfies all its averages. It does **not** show compatibility with the *other* proven facts, which are nonlinear: Theorem U Parseval, the sector law, M5.

**M3 — ACCEPT AFTER FIXES.**
- The "positivity floor" n_d|Z_ρ|²/(d²φ) is exactly the magnitude of the frozen main term. Dev_d ≥ −n_d|Z_ρ|²/d² is Prop K2's per-level bound, because Σ|Z(ν)|² ≥ 0.
- So M3 is a correct **no-go statement for the method**: no positivity or Cauchy–Schwarz bound at d = h_p can force the cross part above the D7 demand. It does not show that the conspiracy is realisable.
- The rate 1.13288 is right.
- Gaps:
  - (a) It depends on the m ≥ 15 inclusion (M-F1).
  - (b) "(1−o(1))" needs n_{h_p}/h_p → 1. Here is a short proof:
    - n_q = q − 2 for q ∥ h (TRACE-228), and every q | h_p has q ≡ 1 mod 2p.
    - ω(h_p) ≤ log h_p/log(2p+1).
    - Hence n/h_p ≥ 1 − 2ω/(2p+1) → 1.
  - (c) "The same holds for every prime factor of h_p" is true for capacity but false for openness. Factors as small as 2p+1 occur (23 | h_11) and lie in the Weil range.
  - (d) "h_p < L_m < √h": the second inequality holds only for p ≳ 2e8. It is not needed; inclusion (d ≤ √h) and openness (the TRACE-246 definition) suffice.
- The author's capacity "numerics" evaluate a closed-form expression in the assumed |Z| = μ^m/2. "Stable to 5 digits" is automatic and is not evidence (M-F4).

**M4 — disjointness ACCEPT [P]; degeneration partly [N].**
- The congruence bookkeeping is right: 4ν ≡ ±1 and 8ν ≡ ±1 mod h/d, so gcd(h/d, h/d′) | 3.
- 3 ∤ h_m also follows in one line from Pell: 3 | h ⇒ 2y² ≡ 1 mod 3, which is impossible (Lean-checked).
- The final step is misstated. "dd′ ≥ h with d, d′ ≤ √h ⇒ d = d′ = 1" is wrong. The correct step: it forces d = d′ = √h, so h/d is coprime to itself, so h = 1 (M-F3).
- My enumeration [9] confirms that no ν lies in two families.
- Degeneration: see M-F1 and M-F2.
- "No level is borderline, no discontinuity to exploit" holds for (±2,8) from m ≥ 15 [P]. It does not hold for (±2,16) at small or moderate m, where the cutoff d* = |Z_16|/(2√m) < √h is genuine [N].

**M5 — ACCEPT [P].**
- The algebra holds at every level (check [10]). The threshold q ≳ 4|Z|²/X (with n_q ≈ q) matches the L_m base 1.4923.
- "Sharp" means sharp *within the quadratic relaxation* (equality when all X_ν are equal). Say so.

**M6 — NOT READY as [P]; keep [H] (or register as conditional).**
- Verified: the sign algebra [11], and TRACE-221/222 at d = 7.
- Problems:
  - (i) The table states "sectors 2 and 6 cancel exactly; 0 and 4 double". §7(a) states "mixed pairs cancel". These agree only for pairs that involve the primary's top in sector 4. For the full cross term, {2,6}×{2,6} doubles. Primary sectors 0, 2, 6 have spectrum inside |z| < 1 (TRACE-198), so they are subdominant, but the cancellation is not exact.
  - (ii) Unverified inputs, which are the closure conditions:
    - **C1.** TRACE-222's RK conjugation, extended to the non-autonomous products L_{τ_{m−1}}⋯L_{τ_0} at conductor c, factor by factor. This looks routine.
    - **C2.** The sector law and the relation c⁻_{a+4} = s_a conj c⁺_a are level-independent. TRACE-221(i) is scoped to d = 7.
    - **C3.** W_{c,β}(−ρ) = conj W_{c,β}(ρ) at every included level. At prime q ∥ h this follows from the explicit TRACE-229 formula if the missing label satisfies t_b(−ρ) = −t_b(ρ). Composite levels then follow from TRACE-228.
    - **C4.** Scope is (±2,8) only, since the (±2,16) read-out differs (TRACE-226).
- With C1–C3 written out, M6 can be upgraded to [P] for (±2,8) at squarefree levels with q ∥ h. That is cheap, but it is not done here.

**M7 — arithmetic ACCEPT [P]; literature ACCEPT AFTER M-F7.**
- ord_c(λ) | 3p for every c | h_{3p}.
- λ^p = 1 + 2h_p ε^p, so λ^p ≡ 1 mod 2h_p (Lean-checked as a ring identity).
- p = 2 log_λ h_p + 2 log_λ 2 + o(1).
- Matching the minimal-period regime of FND is a correct analogy for the *unkicked* map.

**Other sections.**
- §3 "m and 3m in different operator cases — that is the L3 failure" is an overstatement. The cases are unitarily intertwined (TRACE-216) and differ only in the constants c_a. The real obstruction is the non-folding factor 4h²+3 (L3 S3) (M-F9).
- §7(d) "Elementary part [P]" and §7(e) "[P, elementary]" give no derivation. In §7(e) the reversal x ↦ x̄ is not multiplication by a fixed γ, so "⟨λ⟩ and the reversal give exactly 2mΣ|B|²" double-counts or is unproved (M-F10).
- §8.4 quotes L2 isotropic values 0.94–1.12. For the full K1 functional, the relevant L2 worst case is 1.178 at (21,239) (REPORT_L2 l.37), still below 1.28. These are m ≤ 51 data (M-F11).

## Required fixes
- **M-F1 (M3/M4 threshold).** Replace "|Z_ρ| ≥ (½ − o(1))μ*^m … from m ≥ 11 [P]" with:
  - "[P] for odd m ≥ 15 from Line F F3 (TRACE-198/199): ½(1−λ^{−m})(μ_lo^m − 3012.4)";
  - "[N] at m = 11, 13 (float growth_law.json, ratios 1.13, 2.22)".
  - m_incl.py should use the certified bound.
- **M-F2 (M4, (±2,16)).** State that the (±2,16) rule is not degenerate for m ≲ 85: float |Z_16|² < 4mh for every m ≤ 29, and the crossover is extrapolated at m ≈ 85. Above that the claim is [N] only (no certified lower bound on |Z_16|; TRACE-238 has only an upper bound). Restrict "no borderline level" to (±2,8).
- **M-F3 (M4 proof).** Fix the last step: dd′ ≥ h ⇒ d = d′ = √h ⇒ h/d is self-coprime ⇒ h = 1. Include d′ = 1 (primaries). Replace the §4 "exhaustive check" with a membership enumeration such as ref_m.py [9].
- **M-F4 (m_checks.py).** Fix the KeyError at p = 199 (H only to 400): the log ends in a traceback and the "asymptotic base" lines never print. Relabel the capacity column as constant arithmetic, not [N]. Drop "stable to 5 digits".
- **M-F5 (M3 wording).**
  - (a) Identify the floor as Prop K2's per-level bound and call M3 a no-go for positivity methods.
  - (b) Add the n_{h_p}/h_p → 1 argument.
  - (c) Restrict the "every prime factor" sentence to capacity. Small factors (e.g. 23 | h_11) are Weil-range, not open.
  - (d) Drop "L_m < √h", which holds only for p ≳ 2e8.
  - (e) State the scope: m = 3p ≥ 495, ρ = (±2,8).
- **M-F6 (M6).** Correct the table: s_a ≠ s_b pairs cancel and s_a = s_b pairs double. The d = 7 "sectors 2,6 cancel" refers to pairs with the primary top (sector 4). Relabel [H] (or conditional on C1–C4), not [P-sketch]. Do not register as proved.
- **M-F7 (M7 citations).**
  - (a) Kurlberg–Rudnick (CMP 221 (2001)): the condition is ord(A,N)/(N^{1/2}(log N)^7) → ∞ plus genericity, and density one comes via ord ≫ N^{1/2}exp((log N)^δ). It is not "q^{1/2+ε}".
  - (b) Bourgain (LNM 1910, 2007) needs only ord(A,p) > p^ε for prime p. So for prime conductors c_W p² < q ≤ p^C the arithmetic input **is** available (as Lines K/L state, ineffectively). Restrict "never reach" to q > p^C for every fixed C and to the composite modulus h_p.
  - (c) Spell out BGK = Bourgain–Glibichuk–Konyagin (J. London Math. Soc. 2006), not "Gamburd". Cite Bourgain, JAMS 18 (2005) for Mordell sums.
  - (d) Add the caveat that all these theorems concern eigenfunctions of the unkicked quantized cat map, not the kicked R′ functional. Only the arithmetic input is relevant.
  - (e) Give the FND reference in full (Faure–Nonnenmacher–De Bièvre, CMP 239 (2003)).
  - (f) Split M7 into an arithmetic part [P] and a literature part [P-cite + assessment].
- **M-F8 (M2).** Make the normalisation of the hypothesis and of the divergence condition consistent, and state D7_m > 0. Label "strictly harder" and the conspiracy-consistency remark [assessment]. The latter is a tautology about linear consequences of R′, not consistency with all proven constraints. Qualify "no Tauberian argument can produce a contradiction" with "from R′ and D7 linear data alone".
- **M-F9 (§3).** Note the TRACE-216 intertwiners. "Different operator case" alone is not an obstruction.
- **M-F10 (§7(d), 7(e)).** Relabel as [P-sketch]/framing or supply proofs. Handle the reversal-pair double counting and the non-unit part in the Gram form.
- **M-F11 (§8.4).** Quote 1.178 (full K1 functional, L2) alongside 0.94–1.12 (isotropic). Mark "very likely false" as [assessment] on m ≤ 51 data.
- **M-F12 (M1 credit).** Cite TRACE-230 for the r(q) lemma and the 49 ∤ h_{3p} (p ≠ 7) exception. State the LTE hypotheses (q odd, unramified). Mention 49 | h_21.

## (a) Registry recommendations
| Proposed claim | State | Closure / notes |
|---|---|---|
| M1 strong divisibility (odd indices) + disjointness of conductors across m = 3p | **proved** | Paper (TRACE-230 + LTE). Lean: finite range and 3 ∤ h (below) |
| M2 averaging lemma (positive weights ⇒ H♮ with δ/2) | **proved** | Elementary. The signed-weight remark is not registered |
| M3 inherited-level no-go: for m = 3p ≥ 495, d = h_p is included and open, and the K2 per-level floor at d = h_p has magnitude ≥ c·1.1328^m ≫ D7 demand | **proved** (structural no-go; not a refutation) | After M-F1/M-F5. Inputs: Line F F3, TRACE-228/230/238/246 |
| M4a family disjointness for P* (all odd m) | **proved** | Lean core (`three_not_dvd_nsw`, `coprime_core`) |
| M4b (±2,8) rule = all d ≤ √h for odd m ≥ 15 | **proved** (on Line F [CA]) | m = 11, 13 [N] |
| M4c (±2,16) rule degenerates for m ≳ 85 | **open** (float evidence) | Closure: a certified lower bound \|Z_16\| ≥ c·r^m with r² > √λ |
| M5 Cauchy–Schwarz sharpness of positivity (q ≳ \|Z\|²/X) | **proved** | Register as a refinement/annotation of TRACE-238 |
| M6 ±ρ pairing law at all levels | **open** (or conditional) | Closure: C1–C3 for (±2,8) at squarefree levels (C4 scope) |
| M7 arithmetic (ord ≤ 3p; λ^p ≡ 1 mod 2h_p; p = 2log_λ h_p + O(1)) | **proved** | Lean `lam_pow_eq`. The literature sentence is an annotation, not a claim |
| "Every refutation needs a signed equidistribution theorem at h_p" | not a claim | [assessment] in prose only |

TRACE-206 stays **open**. Line M changes no existing state.

## (b) Lean formalisability (done in scratch: lean/LineMArith.lean)
- Compiled against Bgs.LineIArith in a built tree whose LineIArith.lean, LineG.lean, toolchain v4.33.1 and lake-manifest are byte-identical to the repo snapshot.
- Runtime is about 6 s. There is no sorry and no native_decide (`decide +kernel` only). Axioms are listed in logs/lean.log.

| Theorem | What it proves | Axioms |
|---|---|---|
| `three_not_dvd_nsw` | ¬ 3 ∣ h_m for every odd m (general, from `pell`) | std |
| `nsw_three_mul` | h_{3n} = h_n(4h_n²+3) for every odd n (general) | std |
| `lam_pow_eq` | (1+√2)^{2p} = 1 + 2h_p(1+√2)^p for odd p (λ^p ≡ 1 mod 2h_p; M7 core) | std |
| `coprime_core` | A, B ∣ h, gcd(A,B) ∣ 3, 3 ∤ h ⇒ AB ∣ h (M4 disjointness core) | std |
| `pp_eq` | ℕ-recurrence agrees with `nsw`/`lucasU` | propext |
| `strong_div_small` | M1 for all odd m, n < 60 | none |
| `three_small` | 3 ∤ h_m, odd m < 200 | none |
| `triple_small` | h_{3n} identity, odd n < 100 | propext |

- Not cheap: general M1 (needs LTE in ℤ[√2]/q^k), M3/M5 analytic statements, and M6.
- Moderately cheap next steps:
  - n_{h_p}/h_p bounds via `count_excl_one` (TRACE-228's Lean lemma).
  - "q | h_p ⇒ q ≡ 1 mod 2p" (needs the splitting of q, via `two_isSq_mod`, plus Lagrange in (ZMod q)^×).

## Files
- code/ref_m.py → logs/ref_m.log (independent checks [1]–[15]).
- lean/LineMArith.lean → logs/lean.log.
- Author reruns: m_checks.py reproduces logs/m_checks.log exactly (traceback included), and m_incl.py reproduces logs/m_incl.log.
