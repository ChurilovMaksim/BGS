# Referee report: Line L (REPORT_L.md sha cd3097e9…8496)
31 Oct 2026. Referee work dir: /workspace/audit/lineL (rerun/, ref/). Nothing written into /workspace/bgs-lineL.
Scripts with absolute output paths (l3_op_cert.py, l4_const.py) were copied and repointed; l2_rabs.py was not run.

## Verdict summary
| # | Claim | Verdict |
|---|---|---|
| 1 | Lemma O1, Theorem OP_abs [P], certificate [CA] | ACCEPT (minor text fixes F3, F4) |
| 2 | c_W = 10^{−25.62}, q0 = 10^{13.2}, non-vacuous from p ≈ 8.2e25 | ACCEPT c_W and q0. "p₀ explicit" is an OVERCLAIM; fix F2 |
| 3 | Theorem W / K2′ unconditional on OP | ACCEPT AFTER FIX F1 (W2′ must be the bounded-J version, W-F7) and F2; still conditional on standing inputs |
| 4 | Theorem U [P] | ACCEPT [P]; [N] extended |
| 5 | (b) (±2,16) narrowing to 1.1311^{m(1+η)} | ACCEPT [P+CA] (η must be specified) |
| 5 | (d) deficit identity | NOT VERIFIED; do not register until proof or P-check |
| 5 | (a), (c), §6 negatives / "real wall" | [assessment] only |

## 1. OP_abs and certificate
- **Reproduction.** I reran rerun/l3_op_cert.py and l4_const.py. final_op_cert.jsonl and final_constants.jsonl are identical to the author's apart from the timing fields.
  - 8V: rate 1.26278, A_k 1.742e14, δ 0.008108, log10 c −25.615.
  - 8E: rate 1.13642, log10 c −20.93.
  - 16V: rate 1.39243, log10 c −22.53.
  - 16E: rate 1.30276, log10 c −20.84.
  - All rates are below their targets (1.28359 for (±2,8); 1.4742 for (±2,16)).
- **Rigour.**
  - Every decision is made in arb: rate.upper() < target.lower(); η uses the lower bound; A_k uses the upper bound.
  - Bessel tails are bounded by (x/2)^{|a|}/|a|! with a geometric remainder.
  - The Chernoff tail uses the exact Green identity for the carries, e_j = −C0g Σ v_i λ^{−|j+1−i|}. Referee check: max error 1.8e−15.
  - The automaton box DV = 50 ≥ 48, so there is no box loss.
  - Floats appear only in harmless places:
    - the s-grid (any s > 0 is valid);
    - the log10 q grid (rounding q down is conservative because T_k decreases in q);
    - the printed mids (c_W = 10^{−25.62} < 10^{−25.615} is conservative).
  - Verdict: genuinely rigorous.
- **Collision structure.** α_v = 0 ⇔ (X²−6X+1) | v.
  - Brute force agrees with the automaton at k = 6 (relative error 5e−16).
  - The only collision with |v_j| ≤ 3 at k = 6 is v = 0.
  - Everything that depends on v (the collision set, |N(α_v)|, A_k, T_k) is invariant under j → k−1−j, because X²−6X+1 is palindromic. So index ordering does not affect the certificate.
- **Lemma O1 (author-flagged).**
  - The HS bound for an affine composition on H² is ≤ (1−θ²)^{−1/2}, with θ = (ρλ^{−k} + dev)/ρ.
  - dev_V = Σ ½λ^{−i} = λ/(2(λ−1)) = 0.6036.
  - dev_E = 1/(2(λ−1)) = 0.1036, because edge discs are centred at e+½ and the per-step offset is ≤ 1/(2λ).
  - The multiplier satisfies |Im s_j| ≤ ρλ^{−j}.
  - **ω-ratio.** Site-index rounding is ½ per step for both V and E, so the site drift is ≤ 0.6036. This gives the factor coth(β(1−λ^{−k}))·e^{2β(dev+1)}.
    - For V the "+1" is pure slack.
    - For E the "+1" is NEEDED: dev_E + 1 = 1.1036 ≥ 0.6036. The text must say this (F3).
  - NS = 64 for L16 is conservative (‖I⊗J_B block‖²_HS ≤ 2). NS = 1 for (±2,8) is correct because the phases are unimodular.
  - **Numerical test against the actual Galerkin lift operators** (/workspace/bgs-lineF/code/lift.py):
    - ref_checks.py: k ≤ 3, |n| ≤ 4, ρ_V 0.75/0.9, ρ_E 0.2, κ = C0 and C0/2. Max HS/bound = 0.484.
    - ref_O1_stress.py: k ≤ 5, |n| ≤ 10, ρ_V 0.75/0.65, ρ_E 0.2/0.12. Max HS/bound = 0.287 with the stated τ assignment.
    - With the τ assignment reversed the ratio is 93.8, so the bound FAILS. The stated assignment (τ_j = 2πκρλ^{−j} + βλ^{−(k−j)}, with j = 0 the outermost letter) is essential and correct.
    - By the palindromic invariance above, this has no effect on the collision sums.
- **Trace formula at ρ_V = 0.75–0.9, ρ_E = 0.2 (author-flagged).**
  - The TRACE-197 hypotheses hold: ½/ρ_V + 1/λ = 0.838 (at 0.75) < 1, and ½/(λρ_E) + 1/λ = 0.6005 < 1.
  - β > 0 gives trace class through the site weights together with the superexponential ĝ.
  - The β-conjugation is diagonal on sites, commutes with J = I and with I⊗J_B, and leaves the traces unchanged.
  - The scalar side of the trace identity does not depend on the admissible (ρ, β).
  - Verdict: valid, given TRACE-197 as a standing input.

## 2. Constants
- η = 162.8 and c = (η/(6A_k))² = 2.43e−26 recompute correctly. c_W p² ≥ 2p+1 holds from p ≈ 8.2e25. q0 = 10^{13.2} (Weil-range validity) is correct.
- **F2 (overclaim).** "p₀ = 10^{13.2}/2" only makes T_k valid (q ≥ q0). The theorem's conclusion "cross part = o(ξ_lo^m)", and K2′'s "for every m ∈ S⁺ with p ≥ p₀", also need an m-threshold where the error terms fall below the margin. That threshold depends on:
  - sup‖L‖ and sup‖L‖₁;
  - C′_F = e^{O(k)};
  - the conductor count;
  - the margins (e.g. δ/2 ≈ 0.004 for 8V).
  
  It is not computed. Required rewording: "q0 and c_W are explicit; the threshold m₁ is effective but not computed". Alternatively, compute m₁.
- Suggestion: count Weil-range conductors polynomially (≤ 2w, with σ(h)/h) rather than through τ(h). This keeps m₁ effective and small.

## 3. Theorem W / K2′
- **F1 (required).** REPORT_L cites W2′ from REPORT_K2_v2. That version still contains the finite-rank error: I⊗J_B is NOT finite rank. Referee fix W-F7 has still not been applied; K2 has no v3 and I found no "bounded J" text.
  - The fix: bound |Tr(JX)| ≤ ‖J‖‖X‖₁ (with ‖J_B‖ ≤ ½), so C_J = ‖J‖·sup‖L‖₁/sup‖L‖, and use the factor max(1, sup‖L‖)^{2k}. Apply this to the β-conjugated family.
  - With that fix, W2′ applies family by family, with k depending on F, and the conclusions follow.
- With (OP_k, δ) certified (δ_max for 8V = 1 − 1.26278/1.28359 = 0.0162), Theorem K2′ no longer needs OP as a hypothesis.
- It remains conditional on the standing inputs:
  - the Line F/J lattice trace representation (TRACE-197);
  - Theorem J/J3 with L16;
  - the K2 S_Z extraction;
  - W1 [P-cite Weil].
- Per F2, "for every large m" is correct; "for every p ≥ p₀" is not.

## 4. Theorem U
- **Proof re-checked:**
  - The Neumann/Graf addition gives Σ_a J_a(x)J_{a−d}(x) = δ_{d0}, and the i^d factor cancels.
  - θ_j ∈ Z for α_v ∈ hO, because Tr γ is even.
  - Parseval over O/h is valid because the trace pairing is non-degenerate for odd h.
- **Extended [N]** (rerun/logs/l1_unit_m7_3.log, l1_unit_m9_2.log):
  - At m = 7 (h = 239) and m = 9 (h = 1393 = 7·199), the level-h sum equals Σ|w|² to within 2e−8.
  - At proper divisors (q = 7, 199) the sum is ≠ 1, consistent with the aliasing remark.
- **Caveat:** the congruence form of the TRACE-206 phase P(n) (the ψ_d coefficients) is taken as given. The referee did not re-derive it from TRACE-206; it is supported numerically only.

## 5. Open range
- **(b)** Accepted as [P+CA] given the (±2,16) Z-bound, with d ≤ |Z|/(2√m), positivity absorption, and 1.6677² = 2.781, giving 2.781/2.4587 = 1.1311. The text must specify the η (its dependence and size).
- **(d)** The deficit identity is not verified. A sketch via Z_j = Z/q + δ_j with Σδ_j = 0 gives a similar shape, but it needs a written proof or a P-check. It is not used in any theorem.
- **(a), (c), §6:** the identities are fine, but the claims "insufficient", "fails" and "real wall" are [assessment]/[H]. Do not register them as theorems.

## Required fixes
- F1: use the bounded-J W2′ (W-F7) in Theorem W/K2′, and get K2 updated to v3.
- F2: qualify "p₀ explicit" as above.
- F3: state the role of the "+1" slack for E (dev_E 0.1036 versus site drift 0.6036). Also state that the τ assignment is essential.
- F4: state that the β-conjugation commutes with J = I⊗J_B.
- F5: (b) specify η. (d) prove or downgrade to [H].

## Safe to register now
| Item | Label | State |
|---|---|---|
| Collision structure α_v = 0 ⇔ (X²−6X+1) \| v | P | accepted |
| Lemma O1 (with the stated τ assignment, the +1 slack, TRACE-197 hypotheses) | P | accepted (F3 text) |
| Theorem OP_abs: I_k ≤ C_pair·S_k | P | accepted |
| OP certificate, 4 families: rates 1.26278 / 1.13642 / 1.39243 / 1.30276 at (k, ρ, β) as in final_op_cert.jsonl | CA | accepted |
| (OP_k, δ) holds for all four k1 families (δ ≤ 0.0162 for 8V) | P+CA | accepted |
| T_k bound and constants: c_W = 10^{−25.62}, q0 = 10^{13.2}, non-vacuous for p ≳ 8.2e25 | P+CA | accepted (Weil-range validity only) |
| r_abs = 1.0511 | N | accepted as N |
| Theorem U | P | accepted |
| Theorem W unconditional on OP; K2′ for all sufficiently large m ∈ S⁺ | P+CA | conditional on F1. Standing inputs: Line F/J, J3, L16, S_Z |
| (±2,16) open range narrows to q < 1.1311^{m(1+η)} | P+CA | after F5 (η specified) |
| Deficit identity | — | NOT registrable yet |
| Negatives (a), (c), §6 | assessment | as assessment only |

---
## DELTA (31 Oct 2026, 15:01 UTC+5): REPORT_L_v2.md (sha 05adc7ed…) + K2/REPORT_K2_v3.md (sha 3776b07c…)
Checked by diffing against v1 and K2_v2.
- Manifests verify: SHA256_L.txt (170 entries, includes v2; its .sha256 matches) and SHA256_K2_v3.txt pass `sha256sum -c`.
- v1 and K2_v2 are kept unchanged.
- No new code or numerics, so the certificate rerun from round 1 still stands.

| Fix | Status |
|---|---|
| F1 bounded-J W2′ | **Applied correctly**, both in K2_v3 [v3 errata] and in L_v2 §3. |
| F2 p₀ overclaim | **Applied.** |
| F3 "+1" slack and τ ordering | **Applied**, correctly. |
| F4 conjugation commutes with J | **Applied.** |
| F5 η in (b); deficit identity | **Applied.** |

**F1 detail.**
- The bound |Tr(JX)| ≤ ‖J‖‖X‖₁, with one leftover factor in trace norm, gives sup‖L‖₁·sup‖L‖^{ℓ−1} ≤ (sup‖L‖₁/sup‖L‖)·max(1, sup‖L‖)^{2k} for ℓ ≤ 2k. This is correct.
- C′ = e^{O(k)} independent of m, so Theorem W and K2′ are unaffected.
- Nit, unverified: L_v2 says the errata are "merged in the repo with Line K (PR #63)". I did not check that PR. The local K2_v3 is correct.

**F2 detail.** L_v2 now says "q₀ = 10^{13.2} and c_W explicit; m₁ effective, not computed". Theorem W and K2′ are stated for m ≥ m₁, and the Summary items 3 and 4 are fixed.

**F3 detail.**
- The "+1" is needed for E (1.1036 ≥ 0.6036) and is pure slack for V.
- j = 0 is the outermost letter, and this τ assignment is essential (0.287 vs 93.8).
- The collision sums do not depend on the ordering.

**F4 detail.** J_B acts only on the internal index, so it commutes with the site-diagonal conjugation. The TRACE-197 radius conditions are stated.

**F5 detail.**
- (b): η_m^{(16)} ≤ (0.4043/Λ₁₆ + 1)/ℓ + O(log ℓ/m), with Λ₁₆ = log 1.1311 = 0.12319. This gives 4.282/log(2p+1).
  - The formula is consistent with REPORT_v2 Prop K2: plugging in Λ = log 1.4923 there reproduces 2.010.
  - Arithmetic checked: 0.4043/0.12319 = 3.282, and 4.282/log(20001) = 0.432.
  - C ≤ 3.8e−25 comes from REPORT_v2 line 102 (J3 §1 + L16), already accepted. A smaller C only lowers κ₀.
- (d): the deficit identity is downgraded to [H] and is used nowhere.
- (a), (c), §6: labelled [assessment].

**Verdict: READY.**

### Final registrable claims (Line L v2)
| Item | Label | State |
|---|---|---|
| Collision structure α_v = 0 ⇔ (X²−6X+1) \| v | P | proved |
| Lemma O1 (τ assignment as stated; TRACE-197 radius conditions) | P | proved |
| Theorem OP_abs: I_k ≤ C_pair·S_k | P | proved |
| Certificate, 4 families: rates 1.26278 / 1.13642 / 1.39243 / 1.30276 < targets | CA | proved |
| Theorem U (level-h scalar L² unitarity) | P | proved (+N at m = 5, 7, 9) |
| r_abs = 1.0511 | N | numerical |
| W2′ bounded-J form (K2_v3 errata) | P | proved |
| T_k bound; c_W = 10^{−25.62}, q₀ = 10^{13.2}, non-vacuous for p ≳ 8.2e25 | P+CA | proved |
| (±2,16) open range narrows to q < 1.1311^{m(1+η)}, η ≤ (4.282+o(1))/log(2p+1) | P+CA | proved, given the standing inputs |
| Deficit identity (d) | H | heuristic |
| (a), (c), §6 negatives | assessment | — |

### Repo TRACE items
- **TRACE-244 (OP), open → PROVED [P+CA].** Suggested wording: "(OP_k, δ) holds for the four TRACE-206 k1 lattice-lifted families (±2,8) V/E and (±2,16) V/E (Line F operators, β-weighted), at the certified (k, ρ, β) in final_op_cert.jsonl, with δ > 0 (δ ≈ 0.0162 for (±2,8)V). Proof: Lemma O1 + Theorem OP_abs (cancellation-free) + arb certificate [Line L v2]."
  - This concerns the operators defined in Line F, so it inherits only TRACE-197's well-definedness and radius hypotheses.
- **TRACE-245 (Theorem W), conditional on OP → PROVED [P+CA].** It is no longer conditional on OP, but it is still conditional on the standing inputs. Suggested wording: "Assuming the Line F/J lattice trace representation (TRACE-197), Theorem J/J3 with L16, and Weil (W1): for every m = 3p ∈ S⁺ with m ≥ m₁ (effective, not computed), the total cross part of conductors {q, 7q}, q | h_m prime, q ≤ c_W p², with c_W = 10^{−25.62}, is o(ξ_lo^m). The T_k bound is valid for q ≥ q₀ = 10^{13.2}." Uses W2′ in bounded-J form.
  - Do NOT write "explicit p₀" or "unconditional" without the standing-input clause.
- **TRACE-246 (K2′), conditional on OP → PROVED [P+CA]** under the same standing inputs, adding S_Z / Prop K2. Suggested wording: "For all sufficiently large m ∈ S⁺ (m ≥ m₁, effective, not computed), frozen R′ implies a slow λ-orbit at an open-range level c_W p² < q < L_m (for (±2,16): q < 1.1311^{m(1+η)})."
- **TRACE-247 (C1): do NOT promote; it stays open.**
  - Theorem U is the global, all-units L² identity behind C1. Because of aliasing it does not give the per-level statement (the author agrees, §1 and §5(a); sub-level sums ≠ 1 numerically at q = 7 and 199).
  - Register Theorem U as a separate [P] item linked to TRACE-247 ("level-h Parseval / L² version; does not imply C1").

---
## Line L2 referee (REPORT_L2.md sha 6be0793b…, manifest SHA256_L2.txt: 23 files, `sha256sum -c` passes)
Work dir: /workspace/audit/lineL/L2rerun. Code is copied there and its sys.path repointed. The scripts print to stdout only.

**Verdict: READY after text fixes L2-F1 to L2-F4. All [P] statements check, and no claim changes direction.**

### Checks
- **§1 decomposition [P]: correct.**
  - |ℓ(𝔞)| = [O:𝔞] and A(𝔞) = [O:𝔞]^{−1}Σ_{ℓ(𝔞)}Ẑ_β.
  - D_iso follows by inclusion–exclusion, since 𝔮∩𝔮̄ = qO.
- **H_mean sufficiency [P]: correct**, given Theorem K1, Prop K2, Theorem W and the standing inputs. This is the same chain as REPORT_v2 Theorem K.
- **Prop S [P]: the proof is correct.**
  - f_k(0) = ‖L_0^k‖²_HS ≥ ρ₀^{2k}, using HS ≥ op ≥ spectral radius. This is invariant under the β-conjugation.
  - f_k is continuous on the torus.
  - For β = 1, τ_i = Tr(λ^i)/q ∈ (0, 2λ^{|i|}/q]. Indices are cyclic mod r, and λ̄ = λ^{−1} has the same order mod 𝔮̄.
  - This gives 2I−k+2 good blocks (the count should read min(r, 2I−k+2); trivial), so C_k = log_λ(2/ε_k) + k/2 + 1.
  - The hypothesis ρ₀ ≥ μ* follows from the Line F spectral data, since Z = c_m(c^f μ*^m + ε) with |c^f| = ½ and μ* ≥ 1.9154712.
  - (1.28359/1.9154712)^{30} = 6.09e−6 ≤ 6.1e−6 ✓.
- **Lemma A1 [P]: correct.** This covers Parseval on O/𝔮, Cauchy–Schwarz over the q−1 nonzero β, the collision form, exact collisions giving 0 (Theorem U), and Σ|w|² = 1.
- **Prop A2 [P]: correct.** Σ_u M(u)² ≥ G^{2m}/q.
  - Constants [CA] re-derived: G = 2.3693986; (G/T)² = 3.4074 and 2.5832; ¼(μ*/T)^{2m} = ¼·2.2269^m.
- **Lemma B1 [P]: correct.** In both embeddings |σ(λ^{−c}F(λ))| ≤ ‖F‖λ^c·λ/(λ−1); (λ/(λ−1))² = 1.4571; N(λ) = 1; N𝔮 ≥ q.
- **Lemma B2 [P]: correct.** The lattice has index q (or q² if q is inert), and Minkowski's cube gives ‖F‖ ≤ q^{1/r} < 3.3233^{1+η}.
- **Lemma B3 [P]: correct.**
  - Distinct prime ideals containing α_v are coprime, so their product divides (α_v).
  - Σ_v Πρ(v_j) = G^{2m}.
  - E log max(1, ‖v‖_∞)² = o(m), because of the superexponential tails.
- **Disjointness arithmetic: correct.** log 1.4923 = 0.40032, log λ^{1/3} = 0.58758, so η < 0.4678 for (±2,8) and η^{(16)} < 3.770 for (±2,16).
- **(c) numerics [N], spot-checked:**
  - **Independent brute force at m = 7, h = 239** (|n_j| ≤ 3, 823k words) against twlaw.Z for β ∈ {0, 1, (3,7), (17,100)}: all agree to 1e−7 (`L2rerun/chk7.log`). The author validated at m = 5 only.
  - **Row (2,8), m = 15, q = 41 rerun:** |D_𝔮| = 0.4522, r = 5, max|Ẑ|^{1/15} = 1.0729, |Z| = 8572.7. Identical to the table.
  - Not rechecked: the J3 claim of slow β "radius 1.83 at q ≈ 4.9e17 | h_47".

### Required text fixes
- **L2-F1 (factual).** "√h ≈ 2.4142^m" is wrong. In fact h_m ≈ ½λ^{m/2} = ½·2.4142^m (h_21 = 54608393, h_9 = 1393), so √h ≈ 1.5538^m.
  - The conclusion gets *stronger*: the barrier thresholds 3.4074^m and 2.5832^m exceed h_m itself, so no divisor q | h_m qualifies.
  - Fix §0.3, §2 (table column and text), and the "top of included range" wording.
- **L2-F2.** "Sporadic collisions of height ≤ 4 exist at every open level" needs two things stated:
  - (i) 3.3233^{1+η} < 5, i.e. η < 0.340, which holds only for large p;
  - (ii) why the Minkowski vector is *sporadic*: any nonzero F with ‖F‖_∞ ≤ 4 has F(λ) ≠ 0 by Cauchy's root bound (λ = 5.83 > 1 + 4).
  
  Otherwise B2 could return an exact collision. Also state that B1/B2 are written for split q, and that inert q gives index q².
- **L2-F3.** For (±2,16), "for every p" should be "for all sufficiently large p", because of the o(1) and O(log ℓ/m) terms in η^{(16)}. The same applies in §0.4.
- **L2-F4.** Summary item 2, "K2′ is too weak to refute anything [P]", is too strong. What is [P]:
  - for every m ∈ S⁺ such that h_m has a prime q ∥ h_m in (max(c_W p², λ^{C_k + 6.1e−6·m}), L_m), the conclusion of K2′ holds unconditionally.
  
  That this covers all large m (so K2′ cannot refute R′ at all) is [H]: C_k is not computed, and the evidence is only the factor data. Suggested headline: "K2′ gives no contradiction at any m with an open-range prime above λ^{C_k+6.1e−6 m} [P]; [H] this is most/all m."

### Safe to register (Line L2)
| Item | Label | State |
|---|---|---|
| Decomposition D_𝔮, D_iso via Ẑ_β (§1) | P | proved |
| H_mean ⇒ frozen R′ refuted | P | proved, given K1, Prop K2, Theorem W and the standing inputs |
| Prop S (β = 1 slow at q ∥ h_m once log_λ q ≥ C_k + 6.1e−6·m; C_k effective, not computed) | P | proved, given the Line F spectral data (standing) |
| Consequence: K2′ gives no contradiction at such m | P | with L2-F4 wording; the "all m" form is H |
| Lemma A1: \|D_𝔮\|² ≤ (1−1/q)C_𝔮, and C_𝔮 = Σ_{α_v∈𝔮∖0}R(v) + 1 − \|Z\|²/q | P | proved |
| Prop A2: phase-blind barrier ≥ G^{2m}/q, thresholds 3.4074^m / 2.5832^m > h_m | P + CA | after L2-F1 |
| Lemmas B1, B2, B3 | P | proved (B2 with L2-F2) |
| Height zone ∩ open range = ∅ for large p, both families | P | after L2-F2, L2-F3 |
| Isotropic/full-level survey: K1 rate ≤ 1.178 < 1.28359 for (±2,8), m ≤ 183 / 51 | N | (±2,16) not tested |
| Slow-orbit model, "inherited levels harmless" | H | — |
| Signed sporadic-collision reformulation (§0.6, §5), "what does not work" | assessment | — |

---
## Line L3 referee (REPORT_L3.md sha f9b76e03…, manifest SHA256_L3.txt d25dde0f…: 8 files, `sha256sum -c` passes)
Work dir: /workspace/audit/lineL/L3 (s2s3.py, s2s3.log). Nothing written into author dirs.

**Verdict: READY after fixes L3-F1 to L3-F4.**
- All [P] identities and lemmas check.
- There are two factual slips in side statements (Gauss-sum shape; the S3 exceptional prime is 7, not 3) and a few labels to fix.
- The conclusions ("structural route blocked") are unaffected.
- The FNDB analogy is labelled [assessment], which is correct, but one sentence overreaches (L3-F4).

### Checks
- **S1 [P]: correct.**
  - Σx_{|i−j|}n_in_j = α_nᾱ_n, using Tr λ^d = 2x_d.
  - The −2hΣy-term gives e(integer) = 1.
  - χ(x) = e(−ν₀y′Nm x/2h) is 2hO-periodic.
  - B̂_m factorises, and g(t) = Σ i^nJ_n(1.8)e(nt) = e^{i·1.8cos2πt} by Jacobi–Anger, so |B̂_m| ≡ 1.
- **S2 [P]: correct in substance.**
  - 1/2h = a/q + b/M′ since gcd(q, M′) = 1 for q ∥ h odd, and Nm x ≡ 0 (q) on 𝔮.
  - **Slip (L3-F1):** "|F̂_{M′}| ≡ 1/M′ on M′² points" is false, because M′ = 2h/q is even (≡ 2 mod 4). Computed with the actual coefficient (ν₀y′b) at (m,q) = (9,199) and (9,7):
    - |F̂_{M′}| = 2/M′ on exactly ¼ of the points, so Σ|F̂_{M′}| = M′/2.
    - The bound improves to |A(𝔮)| ≤ h/q and |D_𝔮| ≤ h/q + |Z|/q ≤ 2h/q, with threshold ≈ 1.8808^m instead of 2·1.8808^m. The direction of the conclusion is unchanged.
    - |Z| ≤ h needs the Z-bound (m ≥ 495) or a check at small m; say so.
  - Characters should be indexed by O^∨ (or plain (Z/M′)²), since the trace pairing degenerates at 2.
  - 2.41421/1.28359 = 1.8808 ✓.
- **S3 [P].**
  - h_{3p} = h_p(4h_p²+3) is correct: with V_n = η^n − η^{−n} for odd n, η = 1+√2, V_{3n} = V_n³ + 3V_n.
  - Checked exactly for p ≤ 23; gcd = 1 in every case.
  - **Slip (L3-F2):** "primes of K_p have rank 3p except 3" is wrong. The proof's own argument gives the exceptions as divisors of 2h_1 = 2 and 2h_3 = 14, i.e. **7, of rank 3**.
    - 7 | K_p for every p = 5…23 (7² | K_7, so 49 | h_21).
    - 3 never occurs (gcd = 1).
    - Other primes do have rank 3p: 31 (rank 15, 31² | K_5), 4663 (21), 313, 4088137 (39), 409 (51), 457, 14593 (57), and so on.
  - The non-folding conclusion is unaffected.
  - (The 49 | h_21 is harmless for REPORT_v2's "49 ∤ h" in Prop K2, since that is for m ≥ 495; and v_7(h_{3p}) = 1 + v_7(p) [P], so 7 | p is needed.)
- **S4: correct given the Line G/I transfer law.** Period-p twists give Π_β³ by cyclicity. Label it "[P given Line G/I transfer law] + [N]" rather than "[P by construction]".
  - Logs checked: spectral error ≤ 1.73e−13 (at (7,239), t = 3; others ~1e−15).
  - |μ| = 7.0159 ⇒ ½|μ|³ = 172.67 vs |Ẑ| = 172.74; per step 7.0159^{1/7} = 1.321.
  - |Ẑ^{(p)}|³ = 55.49 vs 172.7 ✓.
- **Lemma Q [P]: correct.** The double annihilator of ℓ(𝔮) is 𝔮 mod q (q odd), and γ ∈ 𝔮∖0 ⇒ |Nm γ| ≥ q.
  - The "use" (mean block energy ∈ I_k ± T_k(q), q ≥ q₀(k), no Weil) is correct.
  - **Label (L3-F3):** the "Remark [P, …]" (Hölder ⇒ μ*^m/q, reproducing L_m) contains an [H] step (the size of ∫f_k^s near 0) and must be labelled [H] as a whole.
- **Lemma E [P]: correct, with conservative constants.**
  - Step 1: |Δ²u| ≤ 8ε < 1.
  - Step 2: γ = n₀/2 + (n₁ − 3n₀)/8·√2 ∈ ⅛O.
  - Step 3: an exact solve gives |σ₁σ₂(δ)| ≤ ε²λ^{−K}/(1−λ^{−K})², which is ≤ the stated 4ε²λ^{−K}(1−λ^{−2K})^{−2} ≤ 4.12ε²λ^{−K}.
  - Step 4: 8qδ ∈ O∖qO, and it lies in the conjugate ideal when β is isotropic; 64·4.12 = 264.
  - At ε = 0.05: log_λ(0.66) = −0.236, so run ≤ log_λ q + 0.764 (×2 for non-isotropic) ✓.
  - The bound for β a unit in fact holds for every β ≠ 0.
- **Cost bound:**
  - The arithmetic is correct: (G/T)^{3p} = 1.8459^m, and h_p ≈ ½λ^{m/6} = ½·1.3415^m.
  - The statement "costs ≥ G^{3p}/q [P, as in L2 Prop A2]" has no precise formulation of which class of bounds it covers.
  - Either state it as a phase-blind lower bound in the L2 A2 form (then [P]), or label it [H]. Part of L3-F3.

### Required fixes
- **L3-F1.** S2: correct the Gauss shape: |F̂_{M′}| = 2/M′ on M′²/4 points, Σ = M′/2. Optionally sharpen to |D_𝔮| ≤ 2h/q and threshold ≈ 1.8808^m. State when |Z| ≤ h holds.
- **L3-F2.** S3: change "except 3" to "except 7 (rank 3; 7 | K_p)".
- **L3-F3 (labels).**
  - S4: [P given Line G/I] + [N].
  - Lemma Q Remark: [H].
  - Cost bound: precise statement or [H].
  - Reason 2 "no m = p quantity bounds it" and Reason 3 "the only m = p controls available": [N]/[assessment], not [P].
  - "Iterating CRT is not a descent": [assessment].
- **L3-F4 (FNDB).** It is correctly [assessment], and the citation is right: Faure–Nonnenmacher–De Bièvre, CMP 239 (2003), half-scarred eigenstates at short (≈ 2 log_λ N) periods.
  - But "so no general equidistribution principle can give H_mean" overreaches. FNDB is about eigenstates of the quantized cat map, not these kicked orbit sums.
  - Suggested wording: "[assessment] by analogy with FNDB, principles valid for all cat-map quantizations at minimal period cannot suffice; kick-specific input seems necessary."
  - "Beyond the Ehrenfest time" (m ≫ log_λ q) is an accurate description.

### Safe to register (Line L3)
| Item | Label | State |
|---|---|---|
| S1: A = χ·B_m, B̂_m(y) = Π g(Tr λ^jy), \|B̂_m\| ≡ 1 | P | proved |
| S2: CRT split, A(𝔮) = Gauss sum at level 2h/q; \|D_𝔮\| ≤ 4h/q (indeed ≤ 2h/q), useful only for q ≳ 1.8808^m > L_m | P | after L3-F1 |
| S3: h_{3p} = h_p(4h_p²+3); primes of K_p other than 7 have rank 3p; no Gauss-side folding to m = p | P | after L3-F2 |
| S4: Ẑ^{(3p)}_β = c·Tr[R·Π_β³] at rank-p levels | P (given Line G/I) + N (err ≤ 1.7e−13) | proved |
| Lemma Q (exact line quadrature) and its use for block energies | P | proved |
| Lemma E (cusp excursions): λ^{k−1} ≤ 264ε²q (isotropic), ≤ 264ε²q² (β ≠ 0) | P | proved |
| Cost bound G^{3p}/q vs q ≤ h_p ≈ ½·1.342^m | H (or P once stated precisely) | — |
| Rank-p vs full-rank numerics, \|Ẑ^{(p)}\|³ not tracking \|Ẑ^{(3p)}\| | N | — |
| Hölder ⇒ positivity threshold (Lemma Q Remark) | H | — |
| "Structural route blocked"; H_mean = equidistribution beyond Ehrenfest time; FNDB analogy | assessment | after L3-F4 wording |
