# Line B: derandomizing the BGS short-time form factor for the fixed-kick perturbed cat map (phases 1–4)

**IDs.** BGS-TRACE-163 to BGS-TRACE-182 were provisional in the packet: `main` at d6fa6e2a ended at BGS-TRACE-148, Line D takes BGS-TRACE-149..162, and earlier drafts used 149..168 (shifted by +14). On `main` at 502af245 the highest registered TRACE id is BGS-TRACE-162, so BGS-TRACE-163 is the next free id. The block was not renumbered.

**Status vocabulary.** proved / verification-pending / conditional / open, as in `record/claims.json`. The referee's extra category *numerical-only* has no state of its own in the record, so it is recorded as state `open` with `ledger_status` beginning `NUMERICAL-ONLY (NO THEOREM CLAIMED)`. Status assignments follow the independent referee audit, §8.10 (copy in `computations/verification/lineB/independent_replay/REFEREE_AUDIT_REPORT.md`). Where an independent second reader closed a referee blocker (B1, B2), the status change and its basis are recorded in `computations/verification/lineB/second_reader/SECOND_READER_REPORT.md`.

**Detailed proofs.** The four phase reports are under `derandomized_fixed_kick/`:
- `phase1_trace_formula.md`
- `phase2_kernel_ramp_nd.md`
- `phase3_parity_decomposition.md`
- `phase4_parity_certificate.md`

Each section below names the statement and its status and points to the proof. Working labels inside the reports ([P], [P-sketch], [N], [C], [Cert], [L], [H]) are superseded by the statuses given here.

## Required non-claims (verbatim, referee audit §8.10)
1. Nothing is proved at τ = m/N = O(1). All results are fixed-m (diagonal / below Ehrenfest). This is not progress on BGS-BGS-001 or BGS-TRACE-148.
2. "B_m → 2m" is not claimed. Theorem N covers a finite list of certified NSW primes, and the infinitude of NSW primes is open.
3. The parity crossover is the derandomized analogue of the known BGOS/Pandey–Mehta symmetry-breaking crossover. It is not a Keating–Mezzadri pseudo-symmetry, and the phenomenon is not new.
4. The certified decay bound is vacuous below m⁺(η) (10²–10⁵). It says nothing at the numerically accessible m.
5. Conjecture R is not reduced to any known conjecture or large-sieve inequality. The "quadratic large sieve" phrasing is withdrawn. KR/Bourgain/BGK do not apply (minimal period ord_h λ = m).
6. The fixed-η CLT is numerical only (m ≤ 11); the KS yardstick is heuristic.
7. The (m, η) = (11, 2) outlier is unexplained; the torsion attribution is withdrawn.
8. The Theorem D_cert arithmetic is IEEE float with an a-priori error bound (plus arb coefficients), not full interval arithmetic, until the full directed-rounding rerun.
   - *Second-reader note (2026-10-29):* the full directed-rounding rerun has now been done (93/93, claim-173). Non-claim 8 still applies to the authors' float grid and its constants; TRACE-173 is proved with the directed-rounding constants only.

## Setting and conventions
- U_N = exp(iτN A_N) M_N with S = [[3,4],[2,3]] and τ = 10⁻⁸⁰ (the repository kernel, `computations/verification/lineB/common/model.py`).
- Line B studies the **diagonal (position) part** of the kick: K_η = diag e^{iηf(q/N)}, with f the fixed real 32-mode trigonometric polynomial and η = τN the effective coupling. Throughout, U = K_η M_N.
- ξ ranges over the q-sequence group G ≅ Fix(T^m), T = [[0,1],[−1,6]]. Γ is the dihedral group of shifts and reversals.
- For odd m: h = h_m (NSW numbers, h_m² = (Tr S^m − 2)/4), λ = 3 + 2√2. The support is 𝒮 = ½𝟙 + V^_odd with V^_odd ≅ (Z/h)².
- F_m(η) = E_ν|Z_m(ν; η)|² is the fixed-η second moment and B_m is its η-Bohr mean. σ² = ‖u‖₂² = 3.75·10⁻⁴, where u = 2f_odd.

## Dependencies and comparison
- **BGS-TRACE-131 (dependency).** Time reversal: M_N is symmetric for S = [[3,4],[2,3]] (α ≡ δ = 3), so Uᵀ = K⁻¹UK for every real position kick. This is the α ≡ δ case of TRACE-131. It is used for the COE (not CUE) symmetry class of the 2m law (TRACE-163, 164) and is not re-claimed.
- **BGS-TRACE-127, 128, 132 (comparison).** These are the random-phase (Haar diagonal) short-time limits: the fixed-m limit 2m, and the time-3 kernel 49 when 7 | N. Line B is the derandomized analogue, with a fixed kick and an N/ν-average; its 2m is the same diagonal value. There is no logical dependence. The 7 | N phenomenon parallels Line B's h₃ = 7 torsion and the failure of Lemma V at m = 3 (n = 7e₀).
- **BGS-TRACE-143, 144 (comparison).** These are the Haar ↔ DFT star-graph equivalence and the Gauss-sum/partition formula. Prop K and Prop C (TRACE-165, 169) are the fixed-kick counterparts (Gauss sums → Ramanujan sums), proved independently.
- **BGS-TRACE-145 to 148.** These cover the random-phase off-diagonal problem. W̃^rest and Conjecture R (TRACE-179) are its derandomized analogue. **No progress on BGS-TRACE-148 is claimed.**

## Claims

### <a id="claim-163"></a>BGS-TRACE-163: trace formula, orbit form, kernel structure; 2m law at m ≤ 8 (proved; finite m)
- **Theorem 1.** For odd N with gcd(N, D_m) = 1:
  Tr(K_ηM)^m = Tr M^m · Σ_{n∈Z^m} Φ̂(n) e(Q(n)/N) e(−ν_N y′_m Nm(α_n)/g′_m),
  where ν_N = N⁻¹ mod g′_m and α_n = Σ n_jλ^j. Hence Tr U^m/Tr M^m = Z_m(ν_N; η) + O(1/N).
- **Theorem 2.** The N-average equals the ν-average F_m(η).
- **Theorem 3 / Prop R.** Orbit form over G, with |k_ν|² ∈ {0, |V[4]|/D}.
- B_m = 2m holds for m ≤ 8. At m = 6 the two torsion coincidences are treated exactly. The distinctness of the S-classes is certified by an exact cyclotomic class computation.
- Pointwise self-averaging in a single N is **false**.
- Proof: `phase1_trace_formula.md` §2–§7 (symmetry class §7). Lean: H_mX_m = D_mI and tables only (`Bgs.LineB.Derand`).

### <a id="claim-164"></a>BGS-TRACE-164: 2m law for general m (conditional on ND_m)
- **Theorem 4.** Under ND_m, 0 ≤ 2m − B_m ≤ 224m²D_m^{−1/2}.
- **Theorem 5.** At η = τN, the N-average over an explicit window performs the η-average. With τ = 10⁻⁸⁰ and crude constants, the window is non-empty only for m ≤ 6.
- ND_m is checked exactly for m ≤ 8 and by float clustering at m = 9.
- Proof: `phase1_trace_formula.md` §6, §8.

### <a id="claim-165"></a>BGS-TRACE-165: Prop K, Lemma S + Addendum, Lemma F, Theorem D (proved)
- **Prop K.** K(ξ,ξ′) = μ(q)/(φ(q)D_eff) (Ramanujan kernel).
- **Lemma S + Addendum.** D_m = 4h_m² and 𝒮 = ½𝟙 + V^_odd for every odd m.
- **Theorem D.** 2m − B^sym_m = h_m⁻² Σ_{d|m}[2(m−d)a(d) + d²b(d)] = m²/h_m·(1 + O(λ^{−m/6})).
- Proof: `phase2_kernel_ramp_nd.md` §A–§B. Lean: m ≤ 9 instances (`Bgs.LineB.Phase2`).

### <a id="claim-166"></a>BGS-TRACE-166: C2 p-splitting and C3 symbol facts (proved)
- `phase2_kernel_ramp_nd.md` §C2–§C3. The c̃_{±7} sign was fixed by the referee.

### <a id="claim-167"></a>BGS-TRACE-167: automatic admissibility for NSW-prime m (proved)
- For odd m with h_m prime and h_m > 18, hypotheses (a) and (b) of Theorem N hold automatically.
- Proof (conjugation argument): `phase2_kernel_ramp_nd.md` §C4, Lemma [ref23-fix] and its proof [second-reader fix].
  - O/hO ≅ F_h × F_h always splits, because 2 is a square mod h.
  - σ(λ) = λ⁻¹, and ord_h λ = m.
  - (a) λ^d ∈ F_h forces λ^d = ±1, hence λ^d = 1.
  - (b) λ^a + λ^b = 6 forces λ^aλ^b = 1. Of the four roots of t² − 6t + 1 in F_h × F_h, only λ and λ⁻¹ have norm 1.
- Second reader (blocker B2 closed, 2026-10-29). The written argument ("u, v are the two roots") needed one extra step, the norm-1 step, because O/hO is not a field. That step is now in the text.
- (a) and (b) are checked exhaustively for the twelve listed NSW-prime m with h > 18. TRACE-168 does not rely on this lemma; its eleven instances are checked directly.

### <a id="claim-168"></a>BGS-TRACE-168: Theorem N for the eleven certified NSW-prime m (proved; a bound)
- For m ∈ {7, 19, 29, 47, 59, 163, 257, 421, 937, 947, 1493}:
  |B_m − B^sym_m| ≤ 8m²N_m/h_m.
- The bound is nontrivial only from m = 29 on.
- Primality evidence:
  - ECPP certificates for m ≥ 59: `computations/verification/lineB/ecpp/`, verified by PARI `primecertisvalid` and by the referee's independent pure-Python checker.
  - APRCL for m ≤ 47.
- Proof: `phase2_kernel_ramp_nd.md` §C4; `phase3_parity_decomposition.md` §6.

### <a id="claim-169"></a>BGS-TRACE-169: Prop C, norm-class formula for all odd m (proved)
- F_m(η) = h⁻² Σ_{r,r′} A_rĀ_{r′} μ(q_{rr′})/φ(q_{rr′}).
- Proof: `phase3_parity_decomposition.md` §1, including the case p² | h.
- Second reader (blocker B2 closed, 2026-10-29): re-derived line by line; no fix needed.
  - The λ-invariant binary forms mod any odd h are exactly c·(x₀² − 6x₀x₁ + x₁²): TᵗGT = G forces G = c[[1, −3], [−3, 1]].
  - Fresh direct check: ν-average over all units for m = 3, 5, 7; kernel identity at m = 9.
  - Gauss sums on the p-primary parts for p² | h: m = 15 (31²) and m = 21 (7²).
  - The self-duality orthogonality holds for s, s′ units and h prime, as stated.

### <a id="claim-170"></a>BGS-TRACE-170: Theorem W and Theorem T (proved; identities)
- **Theorem W.** F = B^sym + 2mχ_m + W̃^rest, with |W̃^rest − W^rest| ≤ 4m²/h.
- **Theorem T.** χ_m = Σ_{a=0}^{3}(−1)^a Tr M_a(η)^m.
- Proof: `phase3_parity_decomposition.md` §2–§3.

### <a id="claim-171"></a>BGS-TRACE-171: Lemma V and Prop L (proved)
- χ_m(η) ≥ 1 − ½mσ²η² for odd m ≥ 5 and all η. It fails at m = 3.
- Proof: `phase4_parity_certificate.md` §1.1. Lean: `m5_U`, `m7_U`, `m9_norm`, `h9_sq`, `m3_relation` (7e₀ = H₃(1,0,0) + 𝟙).

### <a id="claim-172"></a>BGS-TRACE-172: majorant / cycle inequality / Collatz–Wielandt framework (proved)
- Proof: `phase4_parity_certificate.md` §1.2. Lean: `G0_SAFE_ok`, `CC_SAFE_ok`.

### <a id="claim-173"></a>BGS-TRACE-173: Theorem D_cert on η ∈ [1, 81.574] (proved; computer-assisted, directed rounding) [upgraded by the second reader, 2026-10-29]
- For every η in the 93 contiguous intervals I covering [1, 81.57406988332305] and every odd m ≥ 5: |χ_m(η)| ≤ C'_I ρ'_I^{m−1}, together with the lower bound of TRACE-171. Here C'_I, ρ'_I are the **directed-rounding constants** of the independent rerun (per-interval table: `computations/verification/lineB/second_reader/logs/b1/b1_summary.json`): max_I ρ'_I = 0.999820 < 1, max_I C'_I = 1.43e+07 (C'_I = Σ_a C_{I,a}). The proved statement uses these constants, **not** the authors' float constants (C_I ≤ 3.64·10⁶, ρ_I from the IEEE-float grid), which are not themselves directed-rounding certified. For a ≠ 0, t9_cert.py reports ρ'_{I,a} = max(0.9, ·), so ρ'_I ≥ 0.9 on every interval (weaker than, and consistent with, the float values).
- Method: `phase4_parity_certificate.md` §1.3–§1.5.
- Envelope fixes:
  - G1: the tilted Bessel truncation tail is now proved: ≤ 2y^{J+1}/(J+1)!·e^y per factor, at most 10⁻²⁰⁴ at η = 1 and 2.1·10⁻⁸⁶ at η = 81.6.
  - G2: the [9:−9] edge mass is padded and added exactly; it is 0 in all runs.
- The **full 93-interval rerun with the fixed envelopes** (2026-10-29) re-certified all 93/93 intervals: coverage [1, 81.57407] contiguous, max_a ρ_I ∈ [0.852733, 0.999860] (identical to the original grid to 7·10⁻¹⁶), max Σ_a C_I = 3.64·10⁶, tilted truncation tail ≤ 2.0·10⁻⁸⁶, edge spill 0. Logs: `computations/verification/lineB/phase4/logs/grid_v2_*`; summary in `computations/verification/lineB/phase4/logs/grid_v2_summary.json` (byte-identical copy in `evidence/executions/20261029/lineB-derandomized/grid_v2_summary.json`). This rerun uses the same IEEE-float method (not interval arithmetic), so it does not change the status.
- Hypotheses:
  - IEEE-754 binary64 semantics;
  - libm exp/log accurate to ≤ 4 ulp;
  - python-flint/arb enclosures for the coefficients.
- Independent directed-rounding re-certification (second reader, 2026-10-29; referee `t9_cert.py` unmodified, driver `second_reader/code/b1_runner.py`): **93/93 intervals valid**, coverage [1, 81.57406988332305] contiguous with exactly shared float endpoints. 3 intervals (idx 0, 33, 48) are the referee's own runs with exact endpoints; the other 90 were run by the second reader (idx 6, 17, 92 rerun because the referee's runs used rounded endpoints). Blocker B1 is closed.
- Hypotheses of the directed-rounding certificate: IEEE-754 binary64 round-to-nearest (outward rounding by nextafter after each operation); correctness of arb/python-flint ball arithmetic; libm exp used only inside the Edrop term (≤ 10⁻²⁹), assumed accurate to 10⁻⁶ relative (absorbed by explicit margins). The libm ≤ 4 ulp hypothesis of the float grid is not used.
- Second-reader checks: union of the 24 arb sub-balls covers each interval (`sr173_ballcover.log`); coefficient envelopes dominate (`sr173_coefcheck.log`).
- Non-claim: the bound is < 1 only for m ≥ m⁺(η) (float grid: ≈ 1.4·10⁵ at η = 1, 6·10³ at η = 5, 10²–10³ for η ≳ 15; directed-rounding constants: m⁺(η=1) = 116570 for bound ≤ 0.01).

### <a id="claim-174"></a>BGS-TRACE-174: decay at every fixed η ≠ 0 (conditional on (I1)–(I3))
Full statement and hypothesis matching: `phase4_parity_certificate.md` §1.6. The inputs, cited and not re-verified:
- **(I1)** Faure–Roy, Nonlinearity 19 (2006) 1233–1252, Thm 1 and Prop 5 and their torus analogues: trace class and the periodic-orbit trace formula after an anisotropic analytic conjugation. The analytic-weight extension follows Rugh, Nonlinearity 5 (1992) 1237–1263.
- **(I2)** Peripheral resonances are L^∞ eigenvalues: unitarity plus von Neumann's mean ergodic theorem (Walters, Thm 1.14; Reed–Simon I, Thm II.11).
- **(I3)** Measurable ⇒ continuous Livšic for S¹-valued cocycles over a transitive linear Anosov map with Lebesgue measure: Livšic, Izv. Akad. Nauk SSSR Ser. Mat. 36 (1972) 1296–1320; Pollicott–Walkden, Trans. AMS 353 (2001) 2879–2895, §1, Property (R) for G = S¹.

Last step (referee): a peripheral resonance makes the cocycle a continuous coboundary. A continuous coboundary sums to zero on every periodic orbit, so X ≡ 0 on 𝒮, which contradicts Prop L.

C_η is not explicit, and uniformity in η is not claimed.

### <a id="claim-175"></a>BGS-TRACE-175: Theorem U (proved)
- ⟨|Tr U_N^m|²⟩_N = F_m(η) + O(m s2 s0^{2m−1}/X + D_m min(s0^{2m}, D_eff)/X), for m ≤ (1−ε)c(η) log X.
- Proof: `phase2_kernel_ramp_nd.md` §E.

### <a id="claim-176"></a>BGS-TRACE-176: Theorem G (conditional on ND^(≤k))
- Moment CLT for the joint (ν, Bohr-η) average.
- Proof: `phase2_kernel_ramp_nd.md` §D1.

### <a id="claim-177"></a>BGS-TRACE-177: numerical observations (numerical-only → state open)
- Covers ND^(2) at small m, the μ(η) spectrum, the m_* crossover, the W̃^rest tables, the fixed-η CLT numerics and the torsion-split numbers.
- Sources: `phase2_kernel_ramp_nd.md` §C5; `phase3_parity_decomposition.md` §3–§5; `phase4_parity_certificate.md` §2.3.

### <a id="claim-178"></a>BGS-TRACE-178: torsion-split identity F = F_gen + F_tor (proved, trivial; interpretation numerical)
- `phase4_parity_certificate.md` §2.3.

### <a id="claim-179"></a>BGS-TRACE-179: Conjecture R / R_NSW (refuted as stated, at η = 2; R_NSW undecided)
- For 0 < η₀ ≤ η₁: max_{η∈[η₀,η₁]} |W̃^rest_m(η)| = o(m).
- Evidence: for η ∈ [10, 400], |W̃^rest|/2m ≤ 0.11 (m = 7), 0.05 (m = 9), 0.018 (m = 11; −0.0175 at η = 400), 0.008 (m = 13; three η).
- Literature check: `phase4_parity_certificate.md` §2.1–§2.2.
- *Line E annotation (2026-10-30; state unchanged, open):* see `resonant_residue_lineE.md`. The k1-kick analogue of R is violated on a finite range (BGS-TRACE-187, computer-assisted) and, conditionally on H∞, for all large m (BGS-TRACE-188). For the kick of this conjecture, |W̃rest_m(2)| > m is certified at m = 11 and 13 only (BGS-TRACE-195, computer-assisted; an m = 17 certificate is pending and nothing is claimed for it), and asymptotic failure along 3 ∤ m holds only conditionally on H∞,7 (BGS-TRACE-196). R itself is not disproved.
- *Line H annotation (2026-10-30; state changed open → refuted):* see [`lineH_49state_certificate.md`](lineH_49state_certificate.md). For this conjecture's kick (the Line B diagonal kick f_B) at η = 2, BGS-TRACE-209 (computer-assisted, on BGS-TRACE-207 and 208; independent referee audit, ACCEPT AFTER FIXES) gives W̃rest_m(2)/m ≥ 1.4·10⁴ for every odd m ≥ 47 with 3 ∤ m. So for every compact η-range containing 2 the maximum is not o(m), and R as stated is false. R_NSW is not decided: it is violated at every m ≥ 47 with h_m prime, and whether there are infinitely many such m is unknown. Not covered: odd m with 3 ∤ m in {17, 19, 23, 25, 29, 31, 35, 37, 41, 43} (m = 11, 13 are BGS-TRACE-195), every m with 3 | m, η ≠ 2, and s = +1; R restricted to compact ranges avoiding 2 is open and not registered separately. This is not a statement about BGS (BGS-BGS-001) and not progress on BGS-TRACE-148. The "R itself is not disproved" of the Line E annotation describes the state before Line H.

### <a id="claim-180"></a>BGS-TRACE-180: fixed-η CLT (open)
- *Line E annotation (2026-10-30; state unchanged, open):* at η ≈ 2 the ν-law has atoms of mass 1/φ(2h) carrying |Z|² ≈ Λ^{2m} (BGS-TRACE-190, 192), so the moment form (M4 → 2, normalisation by √F) fails numerically there; convergence in law of Z/√(bulk variance) is not contradicted.
### <a id="claim-181"></a>BGS-TRACE-181: ND for composite h_m and even m (open)
### <a id="claim-182"></a>BGS-TRACE-182: the (11, 2) outlier (open; torsion attribution withdrawn)
- *Line E annotation (2026-10-30; state unchanged, open):* numerically identified with the N ≡ ±196 (mod h_m) resonance (BGS-TRACE-192: 3.522 of F/2m = 5.562). Rigorously, F_11(2)/2m ≥ 3.5221 from the residues ±196 alone (≥ 3.5227 including ±4; BGS-TRACE-195, computer-assisted), and the ±196 contribution obeys the exact 49-state law (BGS-TRACE-194), so the outlier is not a numerical artefact. The claim stays open because the residual F/2m ≈ 2.04 at (11, 2), the part not carried by ±196, is not rigorously controlled.

## Literature and novelty (short)
- Boasman–Keating 1995: Fourier/Gauss expansion for cat-map form factors.
- NSW numbers and primes: OEIS A002315 and A088165.
- Lam–Leung and Conway–Jones: vanishing sums of roots of unity.
- Gnutzmann–Seif 2004 and Tanner: random-phase star graphs, the repository's TRACE-143/144 context.
- BGOS (Bohigas–Giannoni–Ozorio de Almeida–Schmit) and Pandey–Mehta: symmetry-breaking crossover.
- Kurlberg–Rudnick; Bourgain; Bourgain–Glibichuk–Konyagin; Faure–Nonnenmacher–De Bièvre: why the minimal-period regime blocks the standard tools.

The new content: the exact Pell-norm trace formula for the fixed kick, the Ramanujan-kernel structure and the exact odd-m ramp, Theorem N with certified primes, the exact parity decomposition and transfer-operator formula, the lower bound Prop L, and a computer-assisted decay certificate on a compact η-range. The parity crossover phenomenon itself is not new (non-claim 3).
