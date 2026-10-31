# REPORT N12b — D1 cone-field certificate for Γ_out(1/8) < T′ (closed box, N12 adapted norm): INFEASIBLE, and why; G*_gas at θ = 1/8 inconsistent
Labels: [P] · [P-sketch] · [CA] arb · [CA*] float+rounding margin · [N] · [H]. Nothing pushed.
Asia/Yekaterinburg (UTC+5), 2026-11-01 00:08 → 00:35 (`date`). All jobs ran at nice 19, OMP=1, sequentially. One coarse run (G=64) was killed to free the shared core.
Earlier lines are untouched except NOTES_N10b.md (timestamp erratum, as requested) and the new N10b/SHA256_N10b_v2.txt.
Per N12-F3, the N12 stepnorm table, Lip_H and the quadratic constants are treated as **[N]**.

## 0. Verdict
- **No certificate.** No certified bound Γ_out(1/8) < 1.4279 was obtained.
  - The best rigorous bound in hand is the t-uniform **57.22** [CA*]. It is useless.
  - The best [N] graph bound with N12's step norms is 5.49.
- **The cone certificate at k ≤ 3 is infeasible** in this setting, by about 4 orders of magnitude in cell count (§2).
- **More decisive** (§3) [N lower bounds + bookkeeping]: G\*_gas at θ = 1/8 cannot hold as stated.
  - With minimum stay length L ≥ 3, D1 itself fails: Γ_out(1/8, L) ≥ 1.4336 > T′.
  - With L ≤ 2, the stay fugacity is O(1)·K, where K is the per-stay constant. Rank-p pieces would then need K ≲ 2–8e-4.
  - So the D1-plus-gas factorisation must be replaced by a combined pressure/transfer bound in which short box visits carry their actual weights (§4, [H]).

## 1. Pre-flight data (a_blocks.py; 150 random outside points + top periodic orbits; ṽ = Tv coordinates) [N]
| k | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| max μ*σ₁(P_k)^{1/k} | 5.51 | 3.22 | 2.02 | 1.81 |
| max μ*σ₂(P_k)^{1/k} | 2.51 | **1.57** | **1.253** | 1.184 |

- Any fixed-norm k-block bound stays above T′ for k ≤ 8 (N11b: 1.43 at k = 8; ≥ 1.30 at k = 12 along the 1.2624 orbit). A rank-one cone is therefore required.
- Rank-one cones need **k ≥ 3**, since the σ₂ rate is 1.57 > T′ at k = 2. At k = 3 the margin is (1.253/1.428)³ = 0.67.
- Derivatives: ‖∂P₃/∂y₀‖ ≤ 24.1 and ‖∂P₃/∂y₁‖ ≤ 117.6 (medians 7.0 and 39.4). Keeping the cell error at 10% of the target (T′/μ\*)³ = 0.414 requires cell width ≈ 3e-4 along the unstable direction.

## 2. Coarse cone pre-flight and the precise obstruction [N, centre values, NOT rigorous]
- **Design** (b_cone.py, b_cone2.py):
  - k = 3 blocks on a G×G graph of twist-pair cells, using successors under F³ (mean out-degree 142–213).
  - Each cell carries a split v = a·u_c + q, with u_c the dominant direction iterated backward over J = 10 steps.
  - Edges carry nonnegative 2×2 bounds [[|α|, β], [γ, D]], with D ≤ σ₁ sin∠(u_{c′}, u_L) + σ₂.
  - The bound comes from a vector max-iteration.
- **Results:** Γ_pf = **2.067 (G=16), 2.125 (G=32)**. The "α-only" (cone-only) rate is 1.20 / 1.30, but it is meaningless alone. The off-cone D-rate has median ≈ 1.45–1.49 and max 1.99–2.24.
- **Why it fails** (e_align.py, 40 points). Compare the block output u_L(P₃(y)) with the cone direction u(F³y + δe):
  - Along the stable direction e_s, the misalignment sin∠ has median 0.99 / 0.77 / 0.53 / 0.23 / 0.178 at δ = 1e-1 / 1e-2 / 1e-3 / 1e-4 / 1e-5. The δ = 0 floor is 0.179 (max 0.90).
  - Along the unstable direction there is no sensitivity.
  - The direction field depends on the past, which is amplified by λ per backward step along the stable direction. It therefore has to be resolved to **≈ 1e-5 along the stable direction**, while P₃ has to be resolved to **≈ 3e-4 along the unstable direction**.
  - That is ~3e8 cells, each needing a 495-dim 3-block (~0.2 s) plus ~200 edges: about 2 CPU-years on 1 core.
  - The Lipschitz constant used for rigor is Lip_H = 167 ([N] per N12-F3; an interval version would be needed). With it, the rigorous cell width shrinks further, to ~1e-5–1e-6 in both directions.
- **Cheaper geometries tried:** fixed Φ-split 2×2 (rejected analytically: D(t) ≥ N_H(t) ≈ 2–5) and k = 1 graph (§0: 5.49). Neither comes near T′.

## 3. Minimum stay length vs D1: G*_gas at θ = 1/8 is inconsistent [N lower bounds + bookkeeping]
f_perL.py is N9b's a_per with an added box-run statistic (n ≤ 7, all 41,000 primitive orbits, closed 1/8 box). Γ_per(1/8, L) is the max rate over orbits whose box runs are all < L. These are **lower bounds** on Γ_out(1/8, L).

| L | 1 | 2 | 3 | 4 | 5 | ≥6 |
|---|---|---|---|---|---|---|
| Γ_per(1/8, L) | 1.2624 | 1.3426 | **1.4336** | 1.5117 | 1.5683 | 1.6141 |

Stays of length ≥ L carry fugacity z(L) = K·q^L[(1+L)/(1−q) + q/(1−q)²], with q = μ\*/(λΓ) and K = C·C_θ (REPORT_N9b_v2 F2):
- **L ≥ 3:** D1 is false (Γ_out ≥ 1.4336 > T′). The earlier "L ≥ 9–14" (N11b, with N12 constants) is incompatible with D1 at θ = 1/8.
- **L = 1:** z = 0.83K. Rank-3p/unit/mixed pieces need Γ·e^{z} < T′, so K < 0.149. Rank-p pieces need z < 2e-4, so K < 2.4e-4.
- **L = 2:** z = 0.26K, giving K < 0.234 (rank-3p) and K < 7.6e-4 (rank-p).
- The per-stay constant K is ≳ 1 in every norm measured: N_H(1/8) = 2.84 at the box edge, and N12 estimates K_stay ~ 10².
- **So no L satisfies both conditions at θ = 1/8.** This is a defect of the sup-rate × gas factorisation, not evidence against the refutation: the offending orbits spend most of their time near the slow fixed point, where the count is reduced, and the factorisation over-penalises them.

## 4. What should replace D1 + gas [H, proposal]
- Bound the class sum directly by a **restricted pressure**.
  - Level-h_p points are Fix(F^p)-type lattice points, and m = 3p steps cover full periods, so Σ_x|r(x)| ≈ Σ_{y} ‖P_p(y)³‖/μ\*^{3p}.
  - The condition is then on the **s = 3 pressure restricted to orbits outside long stays** (stays ≥ L handled by the gas, short visits weighted by their true transfer factors): λ·R₃^{out}(θ, L) < μ\*³·(budget). Here μ\*³/λ = 1.206.
  - This is an automaton/transfer-operator certificate on the twist-pair graph with vector weights. It is the N10b "R_s via G\*" route, and it avoids pointwise sup bounds over brief near-fixed-point passages.
- Compared with §2, it does **not** need cone directions resolved along the stable direction: it averages over the stable coordinate, using a transfer operator on functions of y instead of a cone field. It is still a large computation, and should be designed (and pre-flighted on periodic-orbit sums Σρ³ restricted by box runs) before any fine run.

## 5. Gas form (REPORT_N9b_v2 F2) — corrected status
- G\*_gas(Γ, θ = 1/8, L) with z(L) < 2e-4 is **not attainable**: L ≥ 3 violates D1 (§3), and L ≤ 2 needs K ≪ 1.
- REPORT_N9b_v2's "L ≥ 9–14 with the adapted norm" is hereby withdrawn as a usable target. Those constants are also [N] per N12-F3.

## 6. NOTES_N10b timestamp fix (same procedure as N9b)
- Headings are relabelled "clock label … INVALID — invented", with stat evidence. Real times (2026-10-31, +05):

  | event | time |
  |---|---|
  | first code | 23:03:25 |
  | last log | 23:13:31 |
  | N11/NOTE_FROM_N10b.md | 23:10:42 |
  | REPORT/NOTES/SHA256 | 23:16:30 |

- An ERRATUM with a real `date` (2026-11-01 00:11:05 +05) was appended.
- The original is kept at N12b/logs/NOTES_N10b.orig.md.
- New manifest N10b/SHA256_N10b_v2.txt, self-hash 92a8bd0e7736b417d21bcaa11b4841e6118508c8a0d82162b991c4c19425b164. The old manifest is kept and now mismatches by design.

## Files
- code: common.py, a_blocks.py, b_cone.py, b_cone2.py, c_graph1.py, d_trivial.py, e_align.py, f_perL.py
- logs: a_blocks_th0.125.json, b_cone_G16_th0.125.json, b_cone_G32_th0.125.json, b_cone2_G*.out, c_graph1_G{64,256}_th0.125.json, d_trivial.json, e_align.json, f_perL_a4.jsonl, NOTES_N10b.orig.md
- REPORT_N12b.md, REPORT_N11b_v2.md, NOTES_N12b.md, SHA256_N12b.txt (+ .sha256)
