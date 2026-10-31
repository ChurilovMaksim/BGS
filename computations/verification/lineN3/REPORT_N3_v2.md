# REPORT_N3 v2: Line N3, what actually blocks: isotropic lines at q | h_p, the Λ certificate, and what remains for m = 3p

Status: 2026-10-31, Asia/Yekaterinburg (UTC+5). Working dir: `/workspace/bgs-lineN/N3`. N2 files were not edited, except that the original (21,239) run's
line in `N2/logs/d_level_split.jsonl` was already there; the duplicate run was killed before it could append. A separate
`N2/REPORT_N2_v2.md` applies the N2 referee fixes. Nothing was pushed.

*v2 (2026-10-31, Asia/Yekaterinburg) applies the referee fixes N3-F1 … N3-F11 (`/workspace/audit/lineN3/REPORT.md`). REPORT_N3.md (v1) is kept unchanged. Fixes are marked [N3-Fk] inline and listed in §6. The Λ certificates are upgraded to full [CA] in N4 (`/workspace/bgs-lineN/N4/REPORT_N4.md`).*

**Labels.**
- [P]: proved, modulo the named standing inputs.
- [CA]: computer-assisted with arb ball arithmetic.
- [CA*]: computer-assisted in verified floating point. Exact blocks are built in arb. Float matrix products carry a priori rounding bounds g_n|X||Y|, with g_n = 2(n+4)u/(1−2(n+4)u) and u = 2⁻⁵³, inflated by 1+10⁻⁹. Eigen and singular value enclosures use residual + Ostrowski + Weyl. This is Rump/Higham-style verification, not interval arithmetic; it can be upgraded to [CA] by redoing the O(d³) products in arb.
- [N]: numerical only.
- [H]: heuristic.

## 0. Summary

| Item | Outcome | Label |
|---|---|---|
| (1) Isotropic lines at q ∣ h_p | **No [P] bound found.** I proved exact structure: geometric twist sequences, iso part = ((q−2)/q)(D_𝔮 + D_𝔮̄), and the ±ρ pairing law M6 (C1, C3 proved; C2 a scope extension). **M6 cannot cancel the dominant isotropic terms.** Those come from slow isotropic orbits in sector 4 (s = −1), so they double between ±ρ. Numerics: at (21,239) there is essentially no cancellation inside the iso part (signed/absolute = 0.948). The obstruction is a per-orbit growth problem beyond the Ehrenfest time. | [P] structure / [N] |
| (2) Λ certificate | **Both (±2,8) families are certified [CA*]** (upper bounds over the *free* twist family, which contains all cat-map orbits): **Λ^{8V} ≤ 1.965736 < 2.00859** (extremal quadratic norm, margin 2.1%) and **Λ^{8E} ≤ 1.660338 < 2.01046**. Transfer to the O1 space is by the new intertwining Lemma I [P], which answers N2-F1. | [CA*] + [P] |
| Consequence | Theorem C's unit-point part at c = h_p is now **unconditional for the (±2,8) families**. Rate ≤ (1.965736·1.052901)^{1/3} = **1.27440** (V) and (1.660338·1.051923)^{1/3} = 1.20428 (E), both < 1.28359, for all p ≥ p₀ (p₀ effective, not computed). The (±2,16) families still need Λ < 3.04 (not done). | [P + CA + CA*] |
| (3) What remains for R′ along m = 3p | The isotropic lines at every q ∣ h_p (now the numerically dominant open piece); small and medium divisors of h_p for non-unit β; K_p-prime and mixed rank-3p conductors in (c_N p^{7/3}, L_m); the (±2,16) Λ. | assessment |

---

## 1. Isotropic lines

Setting: q prime, q ∥ h_m, q ∣ h_p, m = 3p, q = 𝔮𝔮̄ split. Write ℓ := λ mod 𝔮̄ ∈ F_q^*. Since λ^p ≡ 1 mod h_p and q > 2, ℓ has order exactly p.

**Lemma 1.1 (geometric twist sequences) [P].**
- For β ∈ 𝔮 ∖ 0 (mod q), y := β/q ∈ 𝔮̄^{−1}/O. The map γ ↦ Tr(γy) mod 1 factors through O/𝔮̄ ≅ F_q, because y𝔮̄ ⊂ O and Tr(O) ⊂ Z.
- Hence τ_i(β) = Tr(λ^i y) ≡ s·ℓ^i/q (mod 1) for a unique s ∈ F_q^*.
- For unit β the same argument gives τ_i = (s₁ℓ^i + s₂ℓ^{−i})/q with s₁s₂ ≠ 0.
- So the isotropic points are exactly the points whose twist sequence is a single geometric progression: the "q-adic unstable (or stable) manifold" of the fixed point 0.
- Ẑ_β is constant on ⟨ℓ⟩-cosets: (q−1)/p orbits per line. [checked: (15,41) gives 4 distinct values per line, which accounts for the orbit-merging symmetries; (21,239) gives 17.]

**Lemma 1.2 (iso part as a line quadrature) [P].**
- The J3 weight on isotropic β ≠ 0 is the real constant (q−2)/q², the same for ±ρ.
- By orthogonality on ℓ(𝔮), Σ_{β∈ℓ(𝔮)∖0} Ẑ_β = q·A(𝔮̄) − Z = q·D_𝔮̄ (L3 S1/S2 notation). [N3-F3] In TRACE-255 notation this line sum is q·D_q with D_q := (1/q)Σ_{ℓ(q)∖0}Ẑ for the line ℓ(q) = ℓ(𝔮); i.e. N3's D_𝔮̄ is TRACE-255's D for the line ℓ(𝔮). Only the sum over both lines is used, so nothing changes.
- So the iso cross part at level q is 2Re(conj Z_ρ·((q−2)/q)(D_𝔮 + D_𝔮̄)).
- The trivial bound |D_𝔮| ≤ 4h/q (L3 S2) gives rate λ^{1/3} > T. Lemma Q integrates exactly only the frequencies of norm < q.

**1.3 The ±ρ pairing law M6: conditions C1–C3.**
- **C3 [P].** From 8ν₀ ≡ 2·sg (mod 2h) we get ν₀(−ρ) ≡ −ν₀(ρ) (mod q). The members are ν = ν₀ + (2h/q)j with labels t = jy′, and y′ does not depend on ρ.
  - The missing label t_b (the one with ν ≡ 0 mod q) therefore satisfies t_b(−ρ) = −t_b(ρ).
  - So W_{q,β}(−ρ) = q⁻²(−1 − e(−N(β)t̄_b/q)) = conj W_{q,β}(ρ), and iso weights are equal.
  - Composite levels follow from TRACE-228, since n_e does not depend on the sign.
- **C1 [P, by the proof of TRACE-222] [N3-F1].** TRACE-222's *registered* statement covers only twists e(nτ_i(β)/7) at d = 7; its proof never uses the value of τ. Registry action: widen TRACE-222 to arbitrary τ ∈ R/Z and arbitrary non-autonomous products.
  - TRACE-222's antiunitary RK is built from K (complex conjugation) and the reflection R. Neither depends on the twist.
  - On the letter weight ĝ(n)e(Cn²/2)e(an/8)e(nτ):
    - K sends (C, a, τ) to (−C, 4−a, −τ), using conj ĝ(n) = (−1)^nĝ(n);
    - R sends (C, a, τ) to (C, −a, −τ), using ĝ(−n) = ĝ(n);
    - so RK sends (C, a, τ) to (−C, a−4, τ). The twist τ is preserved for every τ ∈ R/Z, not only τ ∈ (1/7)Z.
  - So (RK)V^{(+2)}_{τ,a}(RK)^{−1} = V^{(−2)}_{τ,a+4} for each factor. Antiunitary conjugation is multiplicative, so for every non-autonomous product Tr Π_i V^{(−2)}_{τ_i,a+4} = conj Tr Π_i V^{(+2)}_{τ_i,a}, and likewise for E.
- **C2 [P-sketch; scope extension] [N3-F2].** Stays [P-sketch] until the conductor-independence of the G2 sector law is written out; only then widen TRACE-221(i).
  - The sector law and the table c⁻_{a+4} = s_a·conj c⁺_a (TRACE-221(i)) are statements about the 16-state G2 automaton for each case m mod 24 ∈ {3, 9, 15, 21}.
  - That automaton is exactly the "(P mod b)" factor of L3 S4 at any conductor. The conductor enters only through the twist sequence.
  - So the proof of TRACE-221(i) applies verbatim at every level. Registry action: widen the TRACE-221(i) scope from d = 7 to all levels.
- **Consequence [P mod C2].**
  - At every open level, cross₊ + cross₋ = 2Re Σ_{a,b} conj(c_a z_a)·c_b y_b·(1 + s_a s_b).
  - Mixed pairs (primary sector a, twisted sector b with s_a ≠ s_b) cancel exactly. Pairs with s_a = s_b double.

**1.4 Why M6 does not close the isotropic part [algebra: P mod C2; dominance: N] [N3-F11].**
- [N] The dominant isotropic orbits are slow: they run near y = 0 for up to log_λ q + 0.76 steps with ε ≈ 0.05; with TRACE-268's maximal ε = 1/16 the bound is log_λ q + 1.02 (Lemma E) [N3-F4]. (N4 §3 identifies the dominant family exactly: sector-4 depth 16D = 1.)
- Near y = 0, only sector 4 has spectral radius > 1 (μ* = 1.91547; sectors 0, 2, 6 and E are < 1, TRACE-198 / Line F).
- The primary Z_ρ's top is also sector 4. So the slow isotropic contribution is a {4}×{4} pair (s = −1, −1), which doubles.
- Example: L3 (S4) at (7,239), t = 3 has |μ|^{1/7} = 1.321 and |Ẑ^{(21)}| = 172.7 ≈ ½|μ|³.

**1.5 Numerics on true TRACE-206 sums [N]** (`code/d_level_split.py`, `code/f_iso_signed.py`; target 1.28359):

| (m, q) | rank p | unit rate | iso rate (absolute) | iso weighted, signed | signed/absolute per line | max unit point | max iso point |
|---|---|---|---|---|---|---|---|
| (15, 41) | 5 | 1.1209 | 1.0559 | 0.9900 | 0.400 | 1.4414 | 1.0729 |
| (21, 239) | 7 | 1.1342 | **1.1604** | 1.1570 | **0.948** | 1.5616 | **1.2780** |
| (33, 23) | 11 | 1.0396 | 0.8497 | 0.8473 | 1.000 | 1.1270 | 0.8331 |
| (27, 199) | 9 | 1.1139 | 1.0145 | 0.9703 | 0.304 | 1.4327 | 1.0602 |

[N3-F10] Definitions: "iso rate (absolute)" is the per-point rate from `d_level_split` (weights (q−2)/q² on each isotropic point, summed, m-th root); the per-line absolute rate from `f_iso_signed` (sum of |Ẑ| per line) is 1.1600 at (21,239) and 1.0523 at (15,41). The (33,23) signed entry is from `f_iso_signed_m33_q23_s1.json` (signed = absolute = 0.8473).

Reading:
- At (21,239) the isotropic part is the larger one, and it is a near-coherent sum dominated by one slow orbit family.
- (21,239) and (15,41) have q = h_p prime, the largest possible q. Only there can isotropic slow runs reach length log_λ q ≈ p/2. At (27,199) (q = 199 < h_9 = 1393) the isotropic part is small again (1.0145, signed/absolute 0.30).
- Small q relative to h_p (q = 23 at m = 33) is harmless numerically.
- Both parts stay below T at every computed point.
- **No trend claim** (N2-F8): four data points.

**1.6 What a proof would need [assessment, with the [P] facts above].**
1. A worst-case (two-level) bound fails. Growth at the slow point is μ* = 1.9155. Off the slow point, the free family still grows at about 1.5–1.65 per step (constant-twist spectral radii [N], N2 `c3`), which is already > T. So one must *average over isotropic orbits*.
2. Averaging over C_𝔮 = 𝔮̄^{−1}/O (a well-rounded lattice, both minima ≍ q^{−1/2} [P]) controls correlations only up to lag ≈ log_λ q (Lemma Q; lattice-point counting for ε-boxes with ε ≥ q^{−1/2}). The p-step products need lag p ≈ 2log_λ h_p ≥ 2log_λ q. This is the L3 "beyond Ehrenfest" obstruction, now localised to one-parameter geometric progressions s·ℓ^i in F_q.
3. The exact quantity: (1/q)Σ_{s∈F_q^*} |Tr(R·Π_s³)|, with Π_s = Π_{i<p} L_{sℓ^i/q}. For one-dimensional multiplicative orbits of length p ≈ 2log q, no equidistribution theorem is available: BGK and Bourgain need |⟨ℓ⟩| ≥ q^δ, and here |⟨ℓ⟩| = p ≍ log q.
4. A kick-specific input would be needed, for example a spectral gap for the slow-orbit sector restricted to geometric twist sequences. I did not find one.

---

## 2. Λ certificate (N2-F1 answered)

**2.1 Lemma I (intertwining) [P].**
- Let H(ρ, β) be the lattice-of-discs space: Σ_c e^{−2β|c|}·‖Φ_c‖²_{H²(D(c,ρ))}.
  - O1 space (TRACE-249/250): 8V uses (0.75, 0.25) and 8E uses (0.2, 0.3).
  - Line F space: 8V uses (1.2, 2.5) and 8E uses (0.8, 2.5).
- For every twist sequence and every k′ ≥ 5 [N3-F5(i): stated uniformly with two steps at each end for V and E; for V one step in suffices, and an extra step costs only sup_τ‖L_τ‖, which is uniform]:
  ‖L_{τ_{k′−1}}⋯L_{τ_0}‖_{O1→O1} ≤ C_I·‖L_{τ_{k′−3}}⋯L_{τ_2}‖_{F→F}.
- [N3-F5(ii)] The O1 operators of TRACE-249 are the ω-conjugated operators on the unweighted direct sum; they are unitarily the same as L on H(ρ,β).
- [N3-F5(iii)] Line F's weights e^{−β(|c|−Rc)₊} are equivalent to e^{−β|c|} within the factor e^{βRc}, absorbed into κ_F.
  C_I does not depend on k′, p, or τ.
- *Proof.* L_τ is a sum over letters n of a multiplier e(κns) (sup ≤ e^{2πκ|n|ρ_out}) times a composition into a sub-disc. For composition into a sub-disc of relative radius θ < 1, the H² norm is ≤ (1−θ²)^{−1/2}. Use a Schur test over sites; the column multiplicity is ≤ ⌈λ⌉ per step.
  - (i) **O1 → F, one step (V).** θ ≤ (½ + 1.2/λ)/0.75 = 0.9412 < 1. The weight ratio e^{−2.5|c| + 0.25|c′|}, with |c′| ≤ (|c|+|n|)/λ + ½, is ≤ e^{0.125 + 0.043|n|}.
  - (ii) **F → O1, two steps (V).** The rounding offset is ≤ ½ + 1/(2λ), so θ ≤ (0.5858 + 0.75/λ²)/1.2 = 0.507. The weight exponent on |c| is −0.25 + 2.5/λ² = −0.176 < 0.
  - (iii) **E.** Use two steps at each end. Rounding offset ≤ 1/(2(λ−1)) = 0.1036. O1 → F: θ ≤ (0.1036 + 0.8/λ²)/0.2 = 0.635. F → O1: the weight exponent is −0.3 + 2.5/λ² < 0.
  - The letter sums converge against |J_n(1.8)|. The twist is a unimodular factor e(nτ), so every bound is uniform in τ. ∎
- **Consequence [N3-F5(iv)].** Applied once to the whole p-step product: ‖M_p‖_{O1} ≤ C_I·κ_F·Λ_free^{p−4} for every twist sequence (so the per-block form below is not needed). Equivalently sup_y ‖P^{O1}_{k′}(y)‖^{1/k′} ≤ (C_I·κ_F)^{1/k′}·Λ_free^F, where Λ_free^F bounds the free-family growth in a norm equivalent to F with constant κ_F. Theorem C (N2) therefore holds with Λ := Λ_free^F, in the same space as the O1 HS bounds, and with p-independent constants. This is the intertwining option of N2-F1.
- **Free family versus torus.** The free family {L_τ : τ ∈ R/Z}, with arbitrary sequences, contains all cat-map twist sequences. So the certified bound is an *upper* bound on the torus Λ, which removes the "sampled lower estimate" objection (N2-F6).

**2.2 Perturbation from the core.**
- Line F (`cert_lift.py`) splits L = A + X + Δ, with Galerkin error δ = δ₁ + δ₂. All its bounds use |w(n)| = |J_n|, so they are uniform in τ.
  - V: δ = 4.5e-11, ‖Δ‖ = 1.86e-9, ‖X‖ = 6.16.
  - E: δ = 1.2e-10, ‖Δ‖ = 7.5e-14, ‖X‖ = 0.32.
- Take the norm |||(u, t, y)||| = max(‖Ru‖, ‖t‖, b‖y‖), with u in the Galerkin core, t the core tail, y the far field, and b = f/(‖X‖(‖R^{−1}‖+1)).
- Then |||L_τ||| ≤ f + π, where f = sup_τ ‖R A_τ R^{−1}‖ and π = ε·max(‖R‖,1,b)·(‖R^{−1}‖+1+1/b), ε = δ + ‖Δ‖.
- [P]: T = [[PAP, 0], [X, 0]] maps (u, t, y) to (PAPu, 0, X(u+t)).

**2.3 8E [CA*]** (`code/i_verify.py`, `logs/i_cert_E_K04_K40.json`):
- Identity norm R = I; K0 = 4, ρ = 0.8, K = 40 (320 dims); letters |n| ≤ 60; NG = 2000 τ-cells; Lipschitz constant 94.96.
- Grid maximum 1.63660. Cell bound 1.66034. Penalty 2.8e-9.
- **Λ_free^{8E} ≤ 1.66034 < 2.01046.**

**2.4 8V [N → CA*]** (`code/g_ext_norm.py`, `code/g2_ext_norm.py`, `code/i_verify.py`):
- **Search [N].** Minimise f(R) = max_τ σ_max(R A_τ R^{−1}) over invertible R, using Adam on a log-sum-exp surrogate over a τ-grid, started from a Lyapunov form of L_{1/2}.
  - Truncated test spaces (K0 = 3, K = 20) reach f = 1.9172 (Line F space) and 1.9093 (O1 space). In both, ρ(L_{1/2}) ≈ μ*.
  - In the certificate space (K0 = 4, ρ = 1.2, K = 55, 495 dims, letters |n| ≤ 60, β-weights 1 on the core as in cert_lift):
    - phase 1 (NT = 24, a grid that misses τ = ½) reached f = 1.980;
    - phase 2 (warm start, NT = 25, grid includes ½) reached f = 1.92325, with cond R ≈ 189.
  - R is in `logs/g_R_V_final.npy`.
- **Verification [CA*]** (`logs/i_cert_V_K04_K55.json`):
  - NG = 4000 cells; grid maximum 1.923268 at τ = 0.501375.
  - Lipschitz constant (Frobenius) 339.70, so the cell bound is 1.965730.
  - ‖RS − I‖ ≤ 7.2e-12; product-rounding error 2.0e-11.
  - Penalty from (δ, Δ, ‖X‖): 5.6e-6. Equivalence constant κ = 2966.
  - **Λ_free^{8V} ≤ 1.965736.** Every product satisfies ‖Π_{i<n} L_{τ_i}‖_F ≤ 2966·1.965736^n, for all twist sequences and all n.
- **Comparison.** μ* ≤ 1.9154752 (Line F) ≤ Λ_free ≤ 1.965736. The gap is 2.6%, mostly the Lipschitz cell term 0.042, which a finer grid or a second-order cell bound would shrink.
- **Margin.** 2.00859/1.965736 = 1.0218 (the referee asked for better than 1.3%).

---

## 3. Theorem C, (±2,8): status after N3

**Theorem C′ [P + CA] (v2).** Let F ∈ {8V, 8E} (and, by N4, also 16V, 16E) and m = 3p, **with h_p squarefree** [N3-F8]. For p ≥ p₀ (effective, not computed):
  E_{y∈G_p}|Ẑ^F(y)| ≤ e^{o(p)}·(Λ^F·r_2^F)^p, with (Λ^F·r_2^F)^{1/3} ≤ 1.27440 (V) and 1.20428 (E).

The cross part at c = h_p restricted to unit β (β a unit at every prime of h_p) is therefore O(((1−δ)·1.28359)^m) with δ ≥ 0.007, for every large p.

Ingredients:
- Theorem C (N2, after N2-F1);
- Lemma I (N3 §2.1);
- Λ certificates (N3 §2.3–2.4);
- Prop E: r_2(4000) [CA], independently reproduced by the referee;
- unit weights ≤ 2^{ω}/h_p² with 2^{ω} = e^{O(p/log p)} at squarefree h_p (J3 / TRACE-229 prime-level weights). [N3-F8] Weights at a conductor q^a with a ≥ 2 are not registered, so h_p squarefree is a hypothesis. [N] no q < 3·10⁶ with q² | h_p for any prime p ≤ 10⁵ (N4 `code/d_squarefree.py`, 2750 pairs (p,q) with q | h_p tested).
- [N3-F6] **(−2,8) = (+2,8).** RK maps (C, a, τ) ↦ (−C, a−4, τ) letterwise (C1), and RK is an isometry of the Line F space H(ρ,β) (weights symmetric in |c|, discs with real centres, K and the reflection preserve H²). Since the twist is free, Λ_free^{(−2,8)} = Λ_free^{(+2,8)} exactly; the same holds for the (±2,16) pair.
- [N3-F9] **Level 7·h_p (unit points) [P-sketch].** For p > 3, 7 ∤ h_p (7 | h_p iff ord_7 λ = 3 divides p). By CRT a unit β at 7h_p is (β₇, β_h); its twist sequence is τ_i(β_h) + τ_i(β₇) with τ_i(β₇) ∈ (1/7)Z of period 3. The free-family Λ covers every twist sequence, and the r_2 collision majorant is cancellation-free, so for each fixed β₇ the β_h-average obeys the same bound; the 7-part weights are the TRACE-229 prime-level values (≤ 2/49 each; 7 splits in O since 3² ≡ 2 mod 7, so there are 36 unit β₇). Hence the unit points at 7·h_p have the same rate. The bookkeeping of the rank-3p orbit sums at the mixed level is not written out in full, hence [P-sketch]. Its isotropic part belongs to item 1 below ("d | h_p or 7d").

**What this does not cover:**
- the (±2,16) families, which need Λ < 3.04;
- isotropic β (§1);
- conductors d ∣ h_p with h_p/d > κ^{p/2}, where κ = T³/(Λ_V r_2) = 1.02180, i.e. h_p/d > 1.01084^p = λ^{0.0061p}. Light points at those levels lose the Bowen index (h_p/d)².

Labels: the r_2 part is [CA] (arb). The Λ part was [CA*] in v1. [N3-F7] It is now [CA] (N4 §1): 8E by an arb Schur certificate (Λ^{8E} ≤ 0.4916), 8V by an all-cell arb run (Λ^{8V} ≤ 1.9656353, 442 cells) with ‖R‖ bounded in arb (Frobenius), twiddles e(nτ) in ball arithmetic, and cells recomputed from exact rational labels. Lemma I is [P]: its constants are finite but not computed, which is harmless because they do not depend on p.

## 4. What remains for refuting R′ along m = 3p

Combine Theorem W/W⁺ (TRACE-245), Prop K2 (levels > L_m), the J3 inheritance and weights, Theorem A (as an implication) and Theorem C′. Along m = 3p the open range (c_N p^{7/3}, L_m), with L_m = λ^{0.2271m}, still contains:

1. **Isotropic β at every prime q ∣ h_p (and at d·7 for such d, N3-F9), and at composite d ∣ h_p with some isotropic prime component.**
   - Numerically this is now the largest open piece at q = h_p: rate 1.1604 at (21,239).
   - No [P] mechanism is known. M6 does not cancel it (§1.4), and averaging needs beyond-Ehrenfest equidistribution of one-parameter geometric twist sequences (§1.6).
2. **Unit β at small and medium divisors d ∣ h_p with h_p/d > 1.0108^p.**
   - Theorem C′ would need (h_p/d)²·(Λ r_2)^p ≤ T^{3p}.
   - Since h_p = Π q^{a_q}, these are the conductors that omit a prime factor q > 1.0108^p of h_p, i.e. essentially every proper divisor whenever h_p has a large prime factor.
   - At those levels the J3 inheritance multiplies the lower-level class sums by n_e/e². The same pressure question appears at the sub-conductor with index (h_p/d)², and the index loss returns.
   - So (2) is as hard as (1) unless h_p is prime. In that case the only conductors are 1 and h_p: level 1 is the primary, and the h_p unit points are now proved.
3. **K_p-prime and mixed rank-3p conductors in (c_N p^{7/3}, L_m)**, K_p = 4h_p² + 3.
   - Their points are rank-3p orbits at index ≥ λ^m/L_m². The pressure majorant is ≥ 2.617^m (N2 barrier, clamp a = 1), even for unit points.
   - Theorem C′ does not reach them. For unit points at a prime Q ∣ K_p with Q < L_m, the analogue of G_p has size Q² ≤ L_m² ≪ λ^m.
   - **This is not touched by N3** and is the second structural block.
4. **(±2,16) Λ < 3.04**: *closed in N4* — Λ_free^{16V} ≤ 2.94139, Λ_free^{16E} ≤ 0.44744 [CA].
5. **[N3-F9] Mixed level 7·h_p** (rank 3p, size ≈ λ^{m/6} < L_m = λ^{0.227m}): not absorbed by Prop K2. Unit points: §3 [P-sketch]. Isotropic points: item 1.

**Net (v2) [N3-F9].** Even in the best arithmetic case (h_p prime and K_p/7 prime, so that all K_p-levels exceed L_m and are absorbed by Prop K2), what remains at m = 3p is **the isotropic lines at q = h_p and at the mixed level 7·h_p** (item 1), plus the unit points at 7·h_p unless the [P-sketch] in §3 is accepted. The (±2,16) Λ (item 4) is now certified (N4). So R′ is **not** refuted along m = 3p. The isotropic lines at q = h_p are the single remaining obstruction in that best case, and that case requires infinitely many p with h_p and K_p/7 both prime, which is itself open (Bunyakovsky-type).

## 5. Rigour ledger and files

**[P]:**
- Lemma 1.1 (geometric twist sequences);
- Lemma 1.2 (iso part = ((q−2)/q)(D_𝔮 + D_𝔮̄));
- C3, and C1 given TRACE-222's single-step identity;
- Lemma I (intertwining, constants finite and not computed);
- the perturbation lemma of §2.2;
- Theorem C′ as an implication from the certified inputs;
- the C_𝔮 well-roundedness (successive minima ≍ q^{−1/2}).

**[P-sketch]:** C2 (scope extension of TRACE-221(i)), and hence the general-level M6.

**[CA]:** r_2 (N2 Prop E). **[CA*] (v1):** Λ^{8E} ≤ 1.660338 and Λ^{8V} ≤ 1.965736; **v2: superseded by N4 [CA]** (see §6).

**[N]:** the extremal-norm searches; the level splits (15,41), (21,239), (27,199), (33,23); signed vs absolute iso sums.

**[H]:** none used in conclusions.

**Registry suggestions:**
- widen TRACE-221(i)/222 to all levels (C1, C2);
- new: Lemma I (proved); Λ^{(±2,8)} certificates (computer-assisted, verified floating point);
- Theorem C′ (proved mod the certificates; unit points at h_p, (±2,8) only);
- new open item: the isotropic part at q = h_p.

**Files:**
- `NOTES_N3.md`
- `code/`:
  - `f_iso_signed.py`
  - `g_ext_norm.py`, `g2_ext_norm.py`
  - `i_verify.py`, `i_check_blocks.py`
  - `j_E_plain.py`
  - `d_level_split.py` (the N2 script with the output path moved to N3)
- `logs/`:
  - `i_cert_E_K04_K40.json`, `i_cert_V_K04_K55.json`
  - `g_R_V_final.npy` (and the phase-1 and identity R's)
  - `g2_*.out`
  - `certO1_V_K04_r0.75_K55_b0.25.json` (shows the O1-space core perturbation is large: Δ = 0.12, ‖X‖ = 23.9, which is why Lemma I is used)
  - `d_level_split_N3.jsonl`, `f_iso_signed_*.json`, `j_E_plain.json`
- `SHA256_N3.txt` and its `.sha256`.

To reproduce the certificates:
- `python i_verify.py V 4 1.2 55 logs/g_R_V_final.npy 4000 60 /workspace/bgs-lineF/logs/certV_eta2_a4.json out.json` (about 7 min);
- `python i_verify.py E 4 0.8 40 logs/R_identity_320.npy 2000 60 /workspace/bgs-lineF/logs/certE_eta2.json out.json`.

---

## 6. v2 amendments (referee N3-F1 … N3-F11)

| Fix | Where | Change |
|---|---|---|
| F1 | §1.3 C1 | [P, by the proof of TRACE-222]; registry: widen TRACE-222 to arbitrary τ and non-autonomous products. |
| F2 | §1.3 C2 | Stays [P-sketch] until the conductor-independence is written; TRACE-221(i) widening deferred. |
| F3 | §1.2 | D_𝔮/D_𝔮̄ aligned with TRACE-255's D_q. |
| F4 | §1.4 | ε stated: +0.76 at ε ≈ 0.05; +1.02 at ε = 1/16. |
| F5 | §2.1 | Step counts uniform (two at each end); ω-conjugation and Line F weight equivalence stated; applied once per p-product. |
| F6 | §3 | Λ^{(−2,8)} = Λ^{(+2,8)} via the RK isometry. |
| F7 | §3, §5 | Certificates upgraded to [CA] in N4 (‖R‖ in arb via Frobenius, arb twiddles, exact rational cells). The v1 [CA*] numbers remain valid as stated. |
| F8 | §3 | Theorem C′ stated for h_p squarefree; [N] Wieferich-type check (none for q < 3·10⁶, p ≤ 10⁵). |
| F9 | §3, §4 | Level 7·h_p added: unit points [P-sketch] via modulated twists; isotropic part in item 1; "Net" corrected. |
| F10 | §1.5 | (33,23) signed 0.8473; (27,199) 1.0602; the two absolute iso rates defined. |
| F11 | §1.4 | Labels split: algebra [P mod C2], dominance [N]. |

Registry suggestion (v2): Λ^{(±2,8)}, Λ^{(±2,16)}: computer-assisted [CA] (N4); Theorem C′: proved mod standing inputs for h_p squarefree; level 7·h_p unit points: P-sketch; isotropic part at q | h_p and 7·q: open.
