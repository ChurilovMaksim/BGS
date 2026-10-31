# Line L3 report: the structural/recursive route to the open range. Result: blocked, with the precise reasons

31 Oct 2026. Labels: [P] proved here, [CA] computer-assisted, [N] floating-point numerics, [H] heuristic, [assessment] opinion on
strategy (not an impossibility proof). Standing inputs and notation as in REPORT_L_v2 / L2/REPORT_L2.

**Errata (referee L3-F1–F4; applied at integration, 31 Oct 2026): see §6. Where §6 and the text above differ, §6 governs.**
The author's file before this change is `../pre_polish/L3/REPORT_L3.md`.
Target (L2 §1): H_mean, i.e. |D_iso − E_b/q| ≤ ((1−δ)T)^m at open levels, with T = 1.28359 for (±2,8).

## 0. Summary

- **Exact structure [P].** Three identities hold exactly:
  - A(x) = B_m(x)·χ(x), where B_m is the law of the walk positions α_n. Its Fourier transform is the **unimodular** product
    B̂_m(y) = Π_{j<m} g(Tr λ^j y), with g(t) = e^{i·1.8 cos 2πt} (S1).
  - A CRT split of χ: on 𝔮 the level-q factor of the phase is identically 1, so A(𝔮) is a level-(2h/q) Gauss sum of B_m
    restricted to 𝔮 (S2).
  - At rank-p levels (twist period p): Ẑ^{(3p)}_β = c_{3p}·Tr[R·Π_β³], with Π_β the p-step twisted transfer operator (S4).
- **(1) Inherited levels: blocked.**
  - **Reason 1 [P].** h_{3p} = h_p(4h_p² + 3). The m = 3p phase has a factor at level K_p = 4h_p² + 3, coprime to h_p
    (up to 3), on which λ^p ≢ 1. So the Gauss side does not fold to m = p.
  - **Reason 2 [N].** On the transfer side, Ẑ^{(3p)} is a cubic spectral function of Π_β built with the m = 3p automaton
    constants (m ≡ 3 mod 6). The m = p twisted sums use a different automaton case (p ≢ 3 mod 6). Numerically
    |Ẑ^{(p)}_β|³ does not track |Ẑ^{(3p)}_β| (factor 3–30 off). No m = p quantity bounds it.
  - **Reason 3 [P].** The only m = p controls available are trace-level Parseval and cancellation-free Schatten moments over the
    line. They do not control Tr Π³, and cancellation-free moments lose (G/T)^{3p}/q ≥ 1.846^m/1.342^m.
- **(2) Full-rank levels: blocked.**
  - The CRT/descent produces exactly the representation A(𝔮) = Σ_z F̂(z)·B̂_m(z/2h), with |B̂_m| = 1 and Σ_z|F̂(z)| = 2h/q.
  - So |D_𝔮| ≤ 4h/q [P] is the trivial bound. It reproduces the large-sieve threshold q ≥ 2·1.8808^m, which lies above L_m.
  - Any gain needs cancellation in averages of the unimodular cat-map products B̂_m over the structured point set
    (1/q)ℓ(𝔮) + (1/M′)O^∨. Iterating the CRT over further primes is not a descent [P/assessment, §2].
- **New rigorous facts with no closing power.**
  - Exact line quadrature (Lemma Q) [P].
  - Cusp-excursion lemma (Lemma E) [P]: an isotropic β ≠ 0 has no twist run near 0 longer than log_λ q + 0.76
    (ε = 0.05); a non-isotropic β has none longer than 2log_λ q + 0.76.
- **Precise obstruction [assessment].** H_mean is an equidistribution statement for the cat-map orbit on the finite lattice
  𝔮^∨/O^∨ at time scales m ≫ log_λ q, i.e. **beyond the Ehrenfest time**.
  - Lemma Q integrates exactly only frequencies of norm < q, which controls correlations up to lag ≈ log_λ q.
  - Orbit sums of length m generate frequencies of norm up to λ^m ≫ q (q < L_m ≈ λ^{0.227m}).
  - The period here is minimal (λ^m ≡ 1 mod 2h, m ≈ 2log_λ 2h). This is the regime where Faure–Nonnenmacher–De Bièvre (2003)
    constructed half-scarred eigenstates for quantum cat maps.
  - So no general equidistribution principle can give H_mean; only kick-specific input could [assessment].
- **(3) Numerics [N].** Inherited/rank-p levels behave differently from full-rank ones:
  - |D|^{1/m} is 0.92–1.12 at rank-p levels, versus 0.82–0.87 at full-rank levels (L2 table).
  - The cause is slow β with a dominant period-p eigenvalue: per-step |μ_β|^{1/p} up to 1.32 at (p,q) = (7,239), giving
    |Ẑ^{(21)}| = 172.7 ≈ ½|μ_β|³ = ½·345.3.
  - The spectral identity (S4) holds to ≤ 1.7·10⁻¹³; Lemma E is consistent with all runs.

## 1. Exact structure

**(S1) Walk-measure form [P].**
- TRACE-212 gives the exact identity P(n) = y′·Nm(α_n) − 2h·Σ_{i,j}y_{|i−j|}n_in_j, because Σ x_{|i−j|}n_in_j = α_nᾱ_n.
- Hence w(n) = Φ̂(n)·χ(α_n), with χ(x) = e(−ν₀y′Nm(x)/2h) periodic mod 2hO, and A(x) = χ(x)·B_m(x), where
  B_m(x) := Σ_{α_n=x}Φ̂(n).
- B_m is the law of the walk α_n with i.i.d. complex steps ĝ(n_j) at positions λ^j. Its Fourier transform is
  B̂_m(y) = Σ_x B_m(x)e(Tr xy) = Π_{j<m} g(Tr λ^j y), where g(t) = Σĝ(n)e(nt) = e^{i·1.8cos 2πt}. So |B̂_m| ≡ 1.
- (This is the Fourier side of Theorem U.)

**(S2) CRT split [P].** Let q ∥ h be an odd prime and M′ = 2h/q. Choose a, b with aM′ + bq = 1. Then
χ(x) = e(−c a Nm x/q)·e(−c b Nm x/M′), with c = ν₀y′.
- On 𝔮 ∪ 𝔮̄ we have Nm x ≡ 0 (mod q), so A(𝔮) = Σ_{x∈𝔮}B_m(x)ψ′(x) with ψ′ at level M′ (the "complementary level").
- Fourier on both factors: A(𝔮) = Σ_z F̂(z)B̂_m(z/2h), where F = 1_𝔮 ⊗ ψ′. Here Σ|F̂_q| = 1 (q points of mass 1/q on ℓ(𝔮)),
  and |F̂_{M′}| ≡ 1/M′ (Gauss) on M′² points.
- **Hence |A(𝔮)| ≤ M′ = 2h/q and |D_𝔮| ≤ 2h/q + |Z|/q ≤ 4h/q [P].**
- |D_𝔮| ≤ T^m therefore follows only for q ≥ 4h/T^m ≈ 2(λ^{1/2}/T)^m = 2·1.8808^m. This is the large-sieve threshold of
  REPORT_L §5c, now as an exact trivial bound. It is above L_m.

**(S3) Gauss-side inheritance [P].**
- For q | h_p and m = 3p: λ^p ≡ 1 (mod 2h_p), and B_{3p} = B_p ∗ (λ^p)_∗B_p ∗ (λ^{2p})_∗B_p. So B_{3p} ≡ B_p^{∗3} as measures mod 2h_p.
- But h_{3p} = h_p(4h_p² + 3) (from V_{3n} = V_n³ + 3V_n for odd n, V = 2h), and gcd(h_p, 4h_p²+3) | 3.
- By (S2), ψ′ has a factor at level K_p = 4h_p² + 3. Every prime of K_p has rank 3p (if q′ | K_p with λ^p ≡ 1 mod q′ then
  q′ | h_p, so q′ | 3).
- So the K_p-factor sees B_{3p} mod K_p, where no folding is available. **The Gauss side does not reduce to m = p.**

**(S4) Transfer-side inheritance [P by construction; N-checked].**
- If r(q) = p, the twists τ_i(β) have period p. The Line G/I transfer law then gives
  Ẑ^{(3p)}_β = c_{3p}·Tr_K[(I_K ⊗ ⟨1|)Π_β³(I_K ⊗ |0⟩)], with Π_β = Π_{i<p}T_{τ_i} the p-step operator on H²-Galerkin ⊗ (P mod b) states,
  built with the m = 3p automaton constants.
- Check (`code/inherit_test.py`): error ≤ 1.7·10⁻¹³ at (p,q) = (5,41) and (7,239), 6 isotropic β each.
- Eigenvalues come in equal-modulus pairs [N]. Slow β have a dominant pair:
  - (7,239), t = 3: |μ| = 7.016 (per step 1.321), |Ẑ^{(21)}| = 172.7 ≈ ½·7.016³ (= ½·345.3);
  - (5,41), t = 2: |μ| = 1.809, |Ẑ^{(15)}| = 2.87.
- **Comparison with m = p:** |Ẑ^{(p)}_β|³ = 55.5 vs 172.7 (t = 3), 0.0966 vs 2.87 (p = 5, t = 2), 0.37 vs 1.30, … [N].
  The m = p sum uses a different automaton case: p ≢ 3 (mod 6), and the TRACE-216 intertwiners only relate cases inside
  m ≡ 3 (mod 6). So it is not a function of Π_β.

## 2. Why the routes are blocked (precise)

**(1) Inherited levels.**
- The user's hope was that the contribution is controlled by m = p quantities with μ*^p-type rates. This needs a bound on
  (1/q)Σ_{β∈ℓ∖0}Tr[R·Π_β³] in terms of m = p data.
- The available m = p identities are:
  - Theorem U at level h_p: Σ_{β mod h_p}|Ẑ^{(p)}_β|² = h_p², which concerns the m = p operators, not Π_β;
  - Lemma Q (below) for ‖Π_β‖²_HS (exact line average = Σ_{γ∈𝔮}c_γ).
- They control power-1 or HS-type quantities, not the cubic spectral function.
- Bounding |Tr RΠ³| ≤ ‖R‖·‖Π‖_{S3}³ and using Hölder plus cancellation-free moments costs ≥ G^{3p}/q [P, as in L2 Prop A2].
  That is ≥ T^{3p} for every q ≤ (G/T)^{3p} = 1.846^m, and here q ≤ h_p ≈ 1.342^m.
- (S3) shows that no Gauss-side folding repairs this.
- [assessment] Inherited levels are genuinely m = 3p objects. The m = p data enter only through the Gauss-side factor mod 2h_p.

**(2) Full-rank levels: CRT / descent.**
- (S2) is the CRT factorisation: the level-q part becomes an ideal indicator and the level-(2h/q) part a Gauss twist.
- Iterating over a second prime q₂ | 2h/q replaces the level-q₂ Gauss factor, on 𝔮, by a sum over Nm x mod q₂. That is an
  E_b-type sum at the pair (q, q₂), not a smaller instance.
- After all prime factors the expression is always Σ_z F̂(z)B̂_m(z/2h) at the full level 2h. There the only information is
  |B̂_m| = 1 (Theorem U). That gives the trivial bound 4h/q, i.e. the threshold 1.8808^m > L_m [P].
- So the recursion does not descend in complexity [assessment, with the [P] identities].
- A signed bound needs cancellation in Σ_{z∈S_𝔮}ω(z)B̂_m(z/2h) over the structured set S_𝔮 = (2h/q)ℓ(𝔮) + qO^∨ (mod 2h),
  weighted by Gauss phases ω. That is an exponential sum of a unimodular cat-map orbit product over a lattice coset.

**Lemma Q (exact line quadrature) [P].** For any absolutely convergent F(y) = Σ_γ c_γe(Tr γy) and any prime 𝔮 | q of degree 1,
(1/q)Σ_{β∈ℓ(𝔮)}F(β/q) = Σ_{γ∈𝔮}c_γ. In particular the average is exact (= c₀) whenever F has no frequency γ ≠ 0 with |Nm γ| ≥ q.
- *Proof.* Orthogonality on the additive group ℓ(𝔮), whose annihilator is 𝔮 (mod q). ∎
- *Use.* For F = f_k (k-block HS²), (1/q)Σ_{β∈ℓ}f_k(β/q) ∈ [I_k − T_k(q), I_k + T_k(q)] with **no Weil input and no upper limit
  on q**. So on isotropic lines the mean block energy is ≈ I_k for all q ≥ q₀(k).
- *Limit.* Orbit sums Σ_{i<m}φ(βλ^i/q) and their moments contain frequencies Σ±γ_tλ^{i_t} of norm up to ≈ λ^m ≫ q.
  Lemma Q says nothing about correlations at lag ≳ log_λ q, and the m/k-th power in W2′ needs exactly those
  (L2: Hölder over blocks reproduces μ^m/q, i.e. the L_m threshold, see below).
- **Remark [P, with REPORT_L Theorem OP_abs constants].** Decoupling the blocks by Hölder gives at best (1/q)Σ_β f_k(β/q)^{m/2k}.
  This is ≥ (cusp region) ≈ μ*^m·λ^{−k}, with k ≤ log_λ q forced by Lemma Q's exactness, so ≈ μ*^m/q. The requirement
  μ*^m/q ≤ T^m is q ≥ (μ*/T)^m = (μ*²/ξ)^m, exactly the base of L_m. So this method reproduces positivity (Prop K2) and
  nothing below it. [The lower bound on the method is a heuristic computation of ∫f_k^s near y = 0, labelled [H].]

**Lemma E (cusp excursions) [P].** Let 0 < ε ≤ 1/16, β ∈ O/q, β ≠ 0, and suppose dist(Tr(βλ^j)/q, Z) ≤ ε for k ≥ 3 consecutive j.
Then λ^{k−1} ≤ 264·ε²·q (β isotropic), and λ^{k−1} ≤ 264·ε²·q² (β a unit mod q).
*Proof.*
1. Write Tr(β̃λ^j)/q = n_j + u_j with |u_j| ≤ ε. The recurrence t_{j+1} = 6t_j − t_{j−1} and 8ε < 1 force
   n_{j+1} = 6n_j − n_{j−1} on the window.
2. So n_j = Tr(γλ^j) with γ ∈ (1/8)O (solve Tr γ = n₀, Tr γλ = n₁). Put δ = β̃/q − γ, so u_j = σ₁(δ)λ^j + σ₂(δ)λ^{−j}.
3. The two end equations give |σ₁(δ)σ₂(δ)| ≤ 4ε²λ^{−(k−1)}(1 − λ^{−2(k−1)})^{−2} ≤ 4.12ε²λ^{−(k−1)}.
4. Also 8qδ ∈ O is ≡ 8β̃ ≢ 0 (mod q), so |Nm(8qδ)| ≥ q (isotropic: 8qδ ∈ 𝔮̄) or ≥ 1 (unit). ∎
- With ε = 0.05: isotropic runs are ≤ log_λ q + 0.76, non-isotropic runs ≤ 2log_λ q + 0.76.
- [N] check (`code/excursion_check.py`, `logs/excursion_check.json`): max isotropic run 1, 2, 2, 2, 4, 4 and max non-isotropic
  (sampled) run 3, 5, 5, 6, 8, at q = 41, 239, 353, 599, 4663, 15607. All are within the bounds.
- *Limit [assessment].* Lemma E bounds time spent near the cusp. But twisted block norms are also large near other rational
  points: the d = 7 twisted radii 1.262–1.45 exceed T (TRACE-217). A per-β bound would need a quantitative bound on the
  time spent near every such point. That is again an equidistribution statement beyond Ehrenfest time.

## 3. Numerics summary [N]

| level type | examples (m, q, r) | \|D_𝔮\|^{1/m} | max\|Ẑ\|^{1/m} (iso) | cause of the excess |
|---|---|---|---|---|
| rank p = m/3 (inherited or not) | (21,239,7), (51,15607,17), (33,353,11), (39,599,13), (123,2297,41) | 0.94–1.12 | up to 1.278 | slow β; dominant period-p eigenvalue pair, per-step up to 1.32 |
| full rank r = m | (39,313), (51,409), (57,457), (111,6217), (123,9103), (183,367), (183,7687) | 0.82–0.87 | ≤ 0.89 | none; generic decay ≈ 0.86/step |

(Data from L2 `logs/iso_survey.jsonl`. New L3 checks: `logs/inherit_p5_q41.json`, `logs/inherit_p7_q239.log`, `logs/excursion_check.json`.)
- [H] Rank-p levels are the only place where the numerics come within a factor ~1.15 per step of the target, and only in
  the per-β maximum; the 1/q weight restores a margin ≥ 6 in |D|.

## 4. Verdict [assessment]

- The structural/recursive route is **blocked**. The precise obstruction is the same in all three formulations:
  1. **Gauss side:** cancellation in averages of the unimodular product Π_{j<m}g(Tr λ^jy) over the coset S_𝔮 of the
     level-2h lattice.
  2. **Transfer side:** a mean bound for the cubic spectral function of the period-p products over the isotropic line
     (rank-p levels), or for the m-step products (full rank).
  3. **Dynamics:** equidistribution of cat-map orbits on 𝔮^∨/O^∨ at times ≫ log_λ q.
- Formulation 3 is beyond the Ehrenfest time, in the minimal-period regime where scarring is known to be possible (FND 2003).
  A proof must use the specific kick g = e^{i·1.8cos} (e.g. its Fourier support, or the log|·| structure of the twisted
  operators), not general dynamics.
- Proved here: (S1), (S2) with the trivial bound |D_𝔮| ≤ 4h/q, (S3) non-folding, (S4) the spectral form, Lemma Q, Lemma E.

## 5. Files (/workspace/bgs-lineL/L3)
- `code/inherit_test.py`, `code/excursion_check.py`.
- `logs/inherit_p5_q41.json`, `logs/inherit_p7_q239.log` (+ .json), `logs/excursion_check.json`.
- `NOTES_L3.md`, `REPORT_L3.md`.
- `SHA256_L3.txt` (its own hash in `SHA256_L3.txt.sha256`).

## 6. Errata L3-F1–F4 (referee, /workspace/audit/lineL/REPORT.md, section "Line L3 referee"; applied at integration, 31 Oct 2026)

Applied in the repository copy by the integrator (the author was busy). The conclusions ("structural route blocked") are unchanged.

| Item | Correction |
|---|---|
| **L3-F1** (§0 (2), §1 S2, §2 (2)) | M′ = 2h/q is **even** (≡ 2 mod 4), so "\|F̂_{M′}\| ≡ 1/M′ on M′² points" is false. Correct shape (referee check with the actual coefficient ν₀y′b at (m,q) = (9,199), (9,7)): **\|F̂_{M′}\| = 2/M′ on exactly M′²/4 points and 0 elsewhere, so Σ\|F̂_{M′}\| = M′/2.** Characters are indexed by O^∨ (or plainly (Z/M′)²), since the trace pairing degenerates at 2. Hence **\|A(𝔮)\| ≤ h/q and \|D_𝔮\| ≤ h/q + \|Z\|/q ≤ 2h/q** (in place of 2h/q and 4h/q), the last step **whenever \|Z\| ≤ h**: this holds for m ≥ 495 by the Z-bound \|Z_ρ\| ≤ C_ρμ^m, C ≈ ½, μ = 1.9155 < 1+√2 (Prop K2, BGS-TRACE-238); for smaller m it has to be checked case by case. The threshold becomes q ≥ 2h/T^m ≈ (λ^{1/2}/T)^m = **1.8808^m** (instead of 2·1.8808^m); it is still above L_m = 1.4923^{m(1+η_m)} (for η_m < 0.578, i.e. all large p). The direction of every conclusion is unchanged. |
| **L3-F2** (§1 S3) | "every prime of K_p has rank 3p (… q′ \| 3)" is wrong: the proof's own argument gives the exceptions as divisors of 2h_1 = 2 and 2h_3 = 14, i.e. **7, of rank 3**. 7 \| K_p for every p = 5…23 (7² \| K_7, so 49 \| h_21; v_7(h_{3p}) = 1 + v_7(p)); 3 never occurs (gcd(h_p, K_p) = 1 for p ≤ 23, and in general it divides 3). All other primes of K_p have rank 3p (e.g. 31 (rank 15), 4663 (21), 313, 4088137 (39), 409 (51), 457, 14593 (57)). The non-folding conclusion is unaffected. (49 \| h_21 does not affect "49 ∤ h" in Prop K2, which is for m ≥ 495.) |
| **L3-F3** (labels) | (i) §1 S4: "[P by construction; N-checked]" → **[P given the Line G/I transfer law] + [N]**. (ii) §2 Lemma Q, "Remark [P, …]": the whole Remark is **[H]** (it contains the heuristic size of ∫f_k^s near y = 0). (iii) The cost bound "≥ G^{3p}/q [P, as in L2 Prop A2]" (§0 (1) Reason 3, §2 (1)) is **[H]**: no precise statement of the class of bounds it covers is given. (iv) §0 (1) Reason 2 ("no m = p quantity bounds it") is **[N]/[assessment]**, and Reason 3 ("the only m = p controls available") is **[assessment]**, not [P]. (v) §2 (2) "iterating the CRT is not a descent" is **[assessment]** (the identities used are [P]). Also: in Lemma E the bound λ^{k−1} ≤ 264ε²q² holds for every β ≠ 0, not only for units (referee). |
| **L3-F4** (§0 "Precise obstruction", §4) | "So no general equidistribution principle can give H_mean" overreaches: Faure–Nonnenmacher–De Bièvre (CMP 239, 2003) concerns eigenstates of quantized cat maps, not these kicked orbit sums. Replace by: **[assessment] by analogy with FNDB, principles valid for all cat-map quantizations at minimal period cannot suffice; kick-specific input seems necessary.** "Beyond the Ehrenfest time" (m ≫ log_λ q) remains an accurate description. |

