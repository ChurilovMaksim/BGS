# Lines N2–N4: the inherited level c = h_p as a periodic-orbit / pressure problem, certified Λ, and the isotropic obstruction

**Status.** Each result below is labelled:
* paper proofs [P];
* computer-assisted inputs [CA] (arb ball arithmetic; script named);
* kernel-checked finite arithmetic in Lean (`formalization/Bgs/LineN2Arith.lean`, `LineN3Arith.lean`, `LineN4Arith.lean`;
  `norm_num`/`decide`/`nlinarith`, no `native_decide`, no `sorry`, `#print axioms` for every theorem);
* floating-point numerics [N], heuristics [H], [P-sketch] and [assessment]. **[N], [H], [P-sketch] and [assessment] items are notes
  only (§5); they are not registered as claims.**

**Sources and referee audits.**
* Line N2: `computations/verification/lineN2/REPORT_N2_v3.md` (author; v1 and v2 kept), referee `lineN2/referee/REPORT.md`
  **READY after fixes N2-F1–N2-F9** (applied by the author in v2/v3; the v3 residuals were checked in the N3 referee report §A).
* Line N3: `computations/verification/lineN3/REPORT_N3_v2.md` (author; v1 kept), referee `lineN3/referee/REPORT.md`
  **READY after fixes N3-F1–N3-F11** (applied by the author in v2).
* Line N4: `computations/verification/lineN4/REPORT_N4.md` (author, unchanged, sha256 6b8684a3…), referee `lineN4/referee/REPORT.md`
  **READY after fixes N4-F1–N4-F9**. The fixes were applied at integration as **`REPORT_N4_v2.md`** (errata §7, with integration notes
  I-1–I-3).
* **Line N5** (`/workspace/bgs-lineN/N5/REPORT_N5.md`, Lemma H half-period identity) supersedes the single-slow-window analysis of N4
  §3.3–§3.4. N5 is **not yet refereed and not integrated**: nothing from N5 is registered, and the N4 §3 numbers that depend on the
  wrong premise (the requirement G ≤ 1.547, the leading rate 1.4468, the remainder rates 1.2426 / 1.0672 / 0.9165 on the 16D = 1
  family) are **not registered** (REPORT_N4_v2 I-2).

The integration record is `evidence/executions/20261031/lineN2N4/INTEGRATION.md`.

**Standing inputs.** As in the Line L and Lines M/N notes: BGS-TRACE-197, 225, 226, 227, 238, 241, all proved; of Theorem J3
(BGS-TRACE-231, conditional) only the notation and its proved parts are used; Theorem K (BGS-TRACE-240) is conditional and is not a
dependency (its proved implication is re-derived as in BGS-TRACE-257). No proved claim of this note depends on a non-proved claim, except
on BGS-TRACE-206 through its frozen definition (gate: `computations/verification/lineN4/integration_checks/proved_deps_gate_N2N4.py`,
strict for 244..298). **No explicit p₀ is claimed: m₁, p₀ and the Lemma I constants are effective, not computed.**

## Registered claims (`record/claims.json`)

| § | claim | content | label | state |
|---|---|---|---|---|
| §1 | BGS-TRACE-286 | N2 Theorem A: the Ω-hypothesis (287) ⇒ H♮_mid ⇒ frozen R′ false (m ≥ m₁); slow orbit ≤ 1.0644^m | [P] implication + Lean | proved |
| §1 | BGS-TRACE-287 | N2 Ω-hypothesis: β-weighted pressure sums Ω^F_m(k,a) ≤ e^{o(m)}((1−δ)T_F)^m for infinitely many m | hypothesis | **open** |
| §2 | BGS-TRACE-288 | N2 Theorem B: class sums at h_p = periodic-orbit sums over the index-4 subgroup G_p ⊂ Fix(A^p); Fourier form; Bowen-ball lemma | [P] + Lean | proved |
| §2 | BGS-TRACE-289 | N2 Theorem C: limsup (1/p) log E_{G_p}\|Ẑ^F\| ≤ log Λ^F_{k′} + log r₂^F(k) + η (Λ in the O1 space, or via Lemma I) | [P] | proved |
| §2 | BGS-TRACE-290 | N2 Prop E: finite tail-free carry automaton; r₂(4000) ≤ 1.0529012 / 1.0519234 / 1.0534557 / 1.0529202 | [P] + [CA] + Lean | proved |
| §3 | BGS-TRACE-291 | N3 Lemma 1.1: isotropic twists are geometric, τ_i = sℓ^i/q, ord ℓ = p | [P] | proved |
| §3 | BGS-TRACE-292 | N3 Lemma 1.2: isotropic cross part = 2Re(conj Z_ρ ((q−2)/q)(D_𝔮 + D_𝔮̄)) | [P] | proved |
| §3 | BGS-TRACE-293 | N3 M6 condition C3: W_{q,β}(−ρ) = conj W_{q,β}(ρ) | [P] | proved |
| §4 | BGS-TRACE-294 | N3 Lemma I / N4 Lemma I₁₆: intertwining O1 ↔ Line F space, p-independent constants, all four families | [P] + Lean | proved |
| §4 | BGS-TRACE-295 | N4: Λ_free^{8V} ≤ 1.9656353, Λ^{8E} ≤ 0.4915932, Λ^{16V} ≤ 2.9413897, Λ^{16E} ≤ 0.4474396 (all twist sequences) | [CA] + Lean | proved |
| §4 | BGS-TRACE-296 | Theorem C′: for p with h_p squarefree, p ≥ p₀, unit-β part at h_p has rates 1.27438 / 0.80266 / 1.45789 / 0.77812 < T_F | [P + CA] + Lean | proved |
| §3 | BGS-TRACE-297 | N4 gauge lemma (up to a unimodular scalar) | [P] | proved |
| §3 | BGS-TRACE-298 | isotropic part at q \| h_p (and 7q, composite d with an isotropic component) | — | **open** |

Amended (state unchanged):
* **BGS-TRACE-222** (proved): scope widened to every twist τ ∈ R/Z and every non-autonomous product (the proof never uses the value
  of τ: RK sends (C, a, τ) ↦ (−C, a−4, τ)). This is condition C1 of M6 (N3-F1). Also used for Λ^{(−2,·)} = Λ^{(+2,·)} in 295.
* **BGS-TRACE-266** (proved): scope widened to any odd conductor c with ord_c λ = p, prime or composite (e.g. c = h_p; the proof uses
  only the period of the twists and cyclicity of the trace), with a dependency on BGS-TRACE-277 (N2-F2).
* **BGS-TRACE-276** (open): C1 and C3 now proved (222 widened, 293); only C2 remains; closure condition reduced to C2.
* **BGS-TRACE-206, 239** stay open; **BGS-TRACE-240** stays conditional. Frozen R′ is **not** refuted.

## 1. Theorem A and the Ω-hypothesis (BGS-TRACE-286, 287)
ψ^F_{k,a}(y) = (1/k) log max(a, ‖P_k(y)‖_op), Ω^F_m(k,a) = Σ_{c open} Σ_β |W_{c,β}| (σ(h_m)/h_m) exp(Σ_{i<m} ψ^F_{k,a}(βλ^i/c)). If
for infinitely many m ∈ S⁺, m ≥ m₁ (BGS-TRACE-245), every family has Ω^F_m ≤ e^{o(m)}((1−δ)T_F)^m, then the open-range cross part is
o(ξ_lo^m), H♮_mid holds and frozen R′ is false. Families (N2-F4): the upper bound |Z_ρ| ≤ Cμ_F^m with μ_F T_F ≤ ξ_lo (μ*·T = 2.458680
< ξ_lo; μ_F ≤ 1.6677 for (±2,16), BGS-TRACE-253). Levels (N2-F3): the Weil range and composite levels below c_W p² by BGS-TRACE-245
and the "open" definition of BGS-TRACE-246. Slow orbit: the β = 1 slow orbit of Theorem N3 (BGS-TRACE-283) contributes ≤ 1.0644^m (Lean `Bgs.LineN2.slow`), so it does not by itself falsify the hypothesis; see the Line N5 caveat in §3.

## 2. Theorem B, Theorem C, Proposition E (BGS-TRACE-288–290)
A^p − 1 = h_p B, det B = −4; G_p = (1/h_p)Z²/Z² has index 4 in Fix(A^p) (Lean `idx3`, `idx5`; [N] p ≤ 47). L3 S4 at the composite
level h_p (BGS-TRACE-266 widened) turns the class sum into Σ_{y∈G_p} W(y) Σ_F a_F Tr(J_F M_F(y)³). Theorem C bounds the G_p-average by
Λ_{k′}·r₂(k) (geometric-mean split, Bowen-ball lemma, Hölder, Lemma O1); Λ must be the norm in the O1 space or transferred by Lemma I
(N2-F1). Prop E: the Green kernel sums to 1/4 exactly (Lean `green_quarter`), so the carry automaton is finite; arb Collatz–Wielandt
bounds give r₂(4000) (table in 290; referee rerun).

## 3. Isotropic structure (BGS-TRACE-291–293, 297, 298)
For prime q ∣ h_p split as 𝔮𝔮̄, isotropic β ∈ 𝔮 have τ_i = sℓ^i/q with ℓ = λ mod 𝔮̄ of order exactly p; the isotropic part is a line
quadrature ((q−2)/q)(D_𝔮 + D_𝔮̄) with the same weight for ±ρ (C3 gives W(−ρ) = conj W(ρ)). The gauge lemma
L_τT_σ = T_{λσ}L_{τ−κλσ}, L_τG_ν = G_{ν/λ}L_{τ+ν/λ} makes a product along a two-sided geometric twist a gauge conjugate of L_{t₀}^n,
**up to a unimodular scalar** (N4-F1). No bound on the isotropic part is known (298): M6 does not cancel the dominant {4}×{4} terms, and
one-parameter orbits of length p ≈ 2log q are beyond BGK/Bourgain and beyond the Lemma Q lag.

Line N5 caveat (not registered; owner audit of PR #66, R1): Line N5 (`REPORT_N5_v2.md`, after the sign correction of N5 v1; under refereeing) reports [P-sketch + N] that the 16D = 1 isotropic family at q = h_p has rate → μ*λ^{−1/6} = 1.42785 > T and a positive cross contribution ≈ 2.735^m > ξ_lo^m. If confirmed, the target of BGS-TRACE-298 and the Ω-hypothesis (287) fail along m = 3p, and Theorem A (286) gives nothing there. The small-m numerics (m ≤ 21) say nothing about large m.

## 4. Certified Λ and Theorem C′ (BGS-TRACE-294–296)
Lemma I / I₁₆ transfers free-family bounds from the Line F spaces to the O1 spaces with p-independent constants. N4 certifies all four
free-family radii in arb (8V: τ-cell scheme with the N3 extremal norm R, committed as `lineN3/logs/g_R_V_final.npy`; 8E, 16V, 16E:
Schur tests). **I-1:** the 16V value is registered as 2.9413897, because f + π = 2.94138961 exceeds the author's 2.9413896. Theorem C′
is an implication **for p with h_p squarefree** (prime-power conductor weights are not registered); squarefreeness is [N] evidence only
(no q < 3·10⁶ with q² ∣ h_p for p ≤ 10⁵) and is not proved for any p.

## 5. Not registered (notes only)
* N4 §3.3–§3.4 (superseded by Line N5): G ≤ 1.547, leading rate 1.4468, remainder rates 1.2426 / 1.0672 / 0.9165; the referee's Lean
  `remainder_rates` and `leading_fails` are left out of `LineN4Arith.lean`.
* The 16D = 1 dominant-family identification and its shares 88.9% / 62.0% [N] (N5 relies on it; to be registered with N5 after review).
* The 7·h_p unit points (N3-F9, [P-sketch]; N5 has an unrefereed [P] upgrade).
* Line N5 / N6 (under refereeing): the 16D = 1 isotropic family at h_p (rate 1.42785, positive cross part ≈ 2.735^m), see the §3 caveat.
* M6 condition C2 ([P-sketch], N3-F2): remains a condition of the open BGS-TRACE-276.
* The pressure interpretation (Cao–Feng–Huang 2008) [cite], the barriers for the method's majorant (2.617^m at clamp a = 1, N2-F7),
  the level-split numerics (N2-F8) and the sampled Λ values 1.98242 etc. (N2-F6, superseded lower estimates).
