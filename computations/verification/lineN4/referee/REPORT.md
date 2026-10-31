# Referee report: Line N4 (+ N2 v3, N3 v2 check)
Referee: Grok Bot. Date 2026-10-31, times Asia/Yekaterinburg (UTC+5). Read-only on /workspace/bgs-lineN; everything written here is under /workspace/audit/lineN4. Nothing was pushed.

## Verdict
**READY-after-fixes (N4-F1..F9).** All the fixes are about wording, labels, or hygiene. I found no numerical or logical error in the certificates.
- **8V, 8E, 16V, 16E Λ bounds are [CA].** I reproduced them independently (§B):
  - 8V: Λ ≤ 1.9656353;
  - 8E: Λ ≤ 0.4915932;
  - 16V: Λ ≤ 2.9413896;
  - 16E: Λ ≤ 0.4474396.
- **Lemma S, tensor doubling, the permutation patterns, Lemma I₁₆, the gauge lemma and the 16D=1 identification are [P].** I checked them.
- **Remainder rates 1.2426, 1.0672, 0.9165 are [P+CA].**
- **What is still open is stated clearly.** The leading term (G ≤ 1.547 over the fast half) and the generic isotropic points are explicitly left open. So is R′, which is not refuted.

## A. N2 v3 and N3 v2
- **N2/REPORT_N2_v3.md fixes all three N2 leftovers:**
  - Theorem A states m ≥ m₁ inline.
  - §0 row (c) and the plain-terms paragraph are marked superseded.
  - The conductor-q^a weights are replaced by an explicit squarefree hypothesis, consistent with TRACE-229.
- **N3/REPORT_N3_v2.md applies N3-F1..F11 inline and has a §6 table.**
  - Theorem C′ is [P+CA] for h_p squarefree.
  - The 7·h_p unit points are [P-sketch]: 7∤h_p for p>3, 7 splits, and there are 36 unit β₇.
  - "Net" is corrected.
  - Lemma I is restated with k′ ≥ 5, two steps at each end, and ‖M_p‖ ≤ C_I κ Λ^{p−4}.
- **Manifests.**
  - The old N2/N3 manifests (SHA256_N2, _N2_v2, _N3) all verify OK.
  - The v3 and v2 reports are not in their own directory's manifest. They are hashed in N4/SHA256_N4.txt, lines 55–56, and those hashes match the files: d6a80358… and a70a743c…. That is acceptable for the PR (see N4-F7).

## B. Independent rechecks (code/, logs/)
| check | referee result | author |
|---|---|---|
| f₁/f₂ basis, 128 blocks (`ref_blocks16.py`) | 64 blocks have disjoint supports of size 32/32. The other 64 have identical 64-element supports and are orthogonal by cancellation: max \|⟨f₁,f₂⟩\| = 1e-14 (float), equal norms in all 128 blocks. Exactly two patterns swap^{n+PAR}, 64 blocks each; 16 distinct actions | "orthogonal, equal norms, exact" (J3); patterns ✓ |
| Schur, own arb blocks + own Perron vectors (`ref_schur.py`, prec 100) | 8E f ≤ 0.4915809; 16E 0.4474392; 16V 2.9413889; 8V phase-blind 3.9308 | 0.4915878; 0.4474392; 2.9413896; 3.932 ✓ |
| 16 → scalar reduction | Write M = M_e⊗I + M_o⊗swap. With x = x_s⊗(1,1), Mx = (M_s x_s)⊗(1,1), and the same holds for Mᵀ. So the bound is independent of PAR (derived) | f identical for P0 and P1 ✓ |
| cert_lift16 rerun (E and V) | δ₁, δ₂, Δ, ‖X‖ bit-identical to cert16_{E,V}.json | ✓ |
| cert_lift16 diff against Line F | only cc = c₀/2 plus a header comment | ✓ |
| penalties | 16V: ε = 2(δ₁+δ₂+Δ) = 1.156e-12, b = 0.772, π = 3.92e-8. 8V: π = 1.9e-9·35.874·(26.217+1+85.3) = 7.67e-6 | ✓ |
| 8V coverage (`ref_cover.py`, own Fraction parser) | 442 cells tile [0,1] exactly, with no gaps or overlaps; max depth 4; 365 F and 77 S cells; max bound 1.96562754 (cell 213L) | ✓ |
| 8V cells, rigorous ‖X(t₀)‖ (`ref_lambda_arb.py`, own blocks) | 213L 1.91473757352; 220 1.90103730187; 186L 1.91396525640; 0 1.62125463092. All agree with the author's n0 to about 1e-13 | ✓ |
| cell formula | 213L: 1.914738 + 6.25e-4·77.961 + (6.25e-4)²/2·11080.9 + 1.6e-9 = 1.965628 | ✓ |
| rates and thresholds | (Λr₂)^{1/3} = 1.27437, 0.80266, 1.45788, 0.77811. Remainder 1.24257 / 1.06716 / 0.91651; leading term 1.44681; G = T²λ^{1/3}/μ* = 1.5472 | ✓ |
| Lean (`lean/LineN4Arith.lean`, compiles) | λ bracket; assembly sums; Λ < thresholds; unit rates < T; remainder sixth powers < T⁶λ; leading term > T | — |

**Soundness of the b_arb_cert scheme**, checked line by line:
- R A_τ R⁻¹ = (R A S)(I+F)⁻¹, with ‖(I+F)⁻¹‖ ≤ 1/(1−‖F‖_F).
- ‖M‖ ≤ max|M_ii| + ‖offdiag‖_F.
- s_min(U)² ≥ 1 − ‖U*U−I‖_F.
- The Taylor remainder satisfies sup‖X″‖ ≤ Σ(2πn)²‖C_n‖_F.
- The tail is bounded by ‖R‖_F‖S‖_F Σ‖w₀B_n‖_F.
- certfloor is rigorous.
- The twiddles are acb balls.
- Periodicity in τ is 1.

N3-F7 (certificate hygiene) is therefore met.

## C. Mathematical points
- **Lemma S [P].** The test vector p = √(xy) gives ‖D⁻¹MD‖ ≤ √(αβ), and |A| ≤ M entrywise. It is uniform in τ, the phases and the sign of C.
- **Tensor doubling [P].** The even-letter part is ½(L^ψ + L^{ψ(−1)^n}) per internal coordinate, with any unimodular extension ψ to odd n. The odd part is the same times I⊗swap. Line F's δ, Δ and ‖X‖ depend only on |w(n)|, so each tensor term is ≤ 2× the scalar bound.
- **Lemma I₁₆ [P].** The constants check out: (½+1.2/λ)/0.9 = 0.784; (0.5858+0.9/λ²)/1.2 = 0.510; −0.3+2.5/λ² = −0.226. The internal factor is unitary.
- **Gauge lemma [P].** Both identities check by substitution. However, T_σG_ν = e(νσ)G_νT_σ, so the telescoped product equals the conjugated power only **up to a unimodular scalar** (N4-F1). This is harmless for every norm or modulus statement.
- **16D [P].** 16D = |N(γ)|/q is an integer for γ = 4qδ ∈ 𝔮, and 16D = 1 holds exactly when γ generates 𝔮 or 𝔮̄.
- **Remainder [P+CA].** It uses μ* ≤ 1.916473 and complement radius 0.76905 (Line F certV), Λ = 1.9656353 [CA], and the p-independent constants κ and C. The point count is polynomial (2p per line).
- **Leading term and generic isotropic points: open**, and stated as open (§3.3, §3.4, §4).

## D. Fixes
- **N4-F1.** §3.1 Corollary: change "exactly; all intermediate gauges cancel" to "exactly up to a unimodular scalar (T_σG_ν = e(νσ)G_νT_σ)".
- **N4-F2.** §5 N3-F9: "the isotropic analysis applies verbatim at 7·h_p with t₀ = ½ + period-3 shift" is unproved. Label it [H], or [P-sketch] with the twist identity written out.
- **N4-F3.** §0 row (2): "all 128 block factors (16 distinct actions × sign of a)" is inconsistent, since 16×2 ≠ 128. Write "128 blocks (16 cases × 8), 16 distinct actions, 2 permutation patterns".
- **N4-F4.** §5 N3-F8 / §4: d_squarefree is [N] evidence (q < 3·10⁶). It does not prove that any h_p is squarefree. Theorem C′ remains conditional on that hypothesis; say so in §4 and in the registry. Optionally prove it for small p by fully factoring h_p.
- **N4-F5.** §2.1: half the blocks have overlapping f₁/f₂ supports, and orthogonality there comes from cancellation. Add an exact Z[ζ₁₆] inner-product and norm check to b16_schur.py, or a log of it, instead of only citing J3.
- **N4-F6.** §3.3: state explicitly that the remainder constants (κ, the complement constant C, and the 2p-per-line count) are p-independent. Also state that the small-gauge window is the one from §3.2.
- **N4-F7.** Put N2_v3 and N3_v2 hashes into their own directories' manifests (or reference SHA256_N4 lines 55–56 from them).
- **N4-F8.** §2.2 and b16_final: say that D is defined exactly as √(x/y) from the stored float vectors x, y. ‖R‖ ≤ (1/min d)(1+1e-12) covers the float d. Store x and y, not only d.
- **N4-F9.** §2.4 scope remark ("absorbed by Line L §5(b)"): cite the TRACE id, or mark it [cited, unchecked here].

## E. Registry states for the integration PR (N2 v3 + N3 v2 + N4)
| claim | state |
|---|---|
| N2 Thm A (m ≥ m₁), Thm B | proved, as in N2 v3 |
| N2 Thm C: unit-point rate (Λ r₂)^{1/3}, r₂(4000) certified | proved [P+CA] |
| N3 Thm C′, 4 families, **hypothesis h_p squarefree** | proved [P+CA], conditional on squarefree (open in general; [N] for q < 3e6) |
| Λ_free 8V ≤ 1.9656353, 8E ≤ 0.4915932, 16V ≤ 2.9413896, 16E ≤ 0.4474396 | [CA] (upgrade from N3's [CA*]) |
| Lemma I / I₁₆ (intertwining O1↔F) | proved |
| 7·h_p unit points | P-sketch |
| TRACE-222 / TRACE-266 widening (twist-independent proof; non-prime q) | amend scope as in N3 v2 |
| N3 C2 | open |
| Gauge lemma (up to scalar), 16D=1 dominant family | proved |
| 16D=1 share (88.9% / 62.0%) | numerical |
| Remainder rates 1.2426 / 1.0672 / 0.9165 on the 16D=1 family | proved [P+CA] |
| Leading term (G ≤ 1.547 over fast half), generic isotropic points | open |
| N3 §4 item 4 ((±2,16) Λ) | closed; items 1–3 open; R′ not refuted |
| TRACE-240 conditional, TRACE-239 open | unchanged |

## Files
- code: ref_blocks16.py, ref_schur.py, ref_cover.py, ref_lambda_arb.py (from lineN3)
- logs: ref_blocks16.log, ref_schur.jsonl, ref_cover.log, ref_cells_8V.log, rerun_cert16_{E,V}.json
- lean: LineN4Arith.lean (compiles with `lake env lean` in the pr63 formalization)
- SHA256.txt
