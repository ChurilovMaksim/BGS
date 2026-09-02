# RED-TEAM REVIEW — RUN 5 CLAIMS (C1–C5)

Reviewer: independent adversarial pass ("red team"), fresh context.
Method: full read of LEDGER.md RUN-5 sections, `src/exact_verify_run5.py`,
`src/calibrate_stream.py`, `src/campaign.py`, `src/largescale.py`,
`src/analyze_campaign.py`, `src/fine_r4_struct.py`, `src/master_formula.py`,
`src/m1_new_configs.py`, `src/theta_sign.py`; artifacts `exact_run5.json`,
`campaign_state.json` (incl. controls + per-prime checks), `campaign_pooled.json`,
`m1_run5.json`; `review/blind_replication/report.md`.
Independent verification scripts in `review/redteam_run5_scratch/`
(`rt_c5.py`, `rt_c5b.py`, `rt_c4_c123.py`). All numbers below were produced
by those scripts unless attributed to repo artifacts.

---

## C1 — O6 theorem: reversing involution R ⇒ M=SR has a_M=d_M ⇒ Θ²=+1 identically

**Verdict: DOWNGRADED** (conclusion plausible, theorem as stated has a real hole).

**What checks out.**
* Index/convention attacks fail: with the repo kernel
  `UU(x,y)=ω^{icb(d x²−2xy+a y²)}` (row x, column y), Θ² is the *matrix
  product* `U_M · conj(U_M)` with **entrywise** conjugation and no transpose
  (consistent with calibrate_stream G2 and the blind replication §2). Both
  orders give a summand linear in the summed variable whenever d=a:
  `(U·conj U)(x,w)=Σ_y ω^{icb[d(x²−y²)+(a−d)y²+2y(w−x)]}` — and the diagonal
  constant `icb(d−a)x²` vanishes identically when d=a. The ledger's
  `Q_M(x,y)−Q_M(y,w)` phrasing corresponds to the other order and is equally
  fine.
* "R necessarily traceless" is correct, though nowhere *proved* in the repo:
  R²=I and det R=−1 force char. poly x²−1, hence tr R=0. Run-2 T3 only builds
  tracelessness into the ansatz. Minor gap, easily closed.

**The hole: the gcd(M₂₁,N)=1 hypothesis is real and is silently violated by
legitimate reversing pairs.**
* The kernel formula needs `icb=(2M₂₁)⁻¹ mod N`, i.e. gcd(M₂₁,N)=1. This
  hypothesis appears nowhere in R5.1.
* Concrete counterexample family (machine-verified, `rt_c4_c123.py`):
  for the Arnold map A=[[2,1],[1,1]],
  `R = [[1,−1],[0,−1]]` satisfies R²=I, det R=−1, R·A·R=A⁻¹ **exactly**
  (integer matrices). Then M=S·R=[[1,−1],[0,1]] has M₂₁=0 for every N, so
  `Q_M` is undefined and the "linear-in-y ⇒ Θ²=I" argument does not even get
  off the ground. This R lies inside the scanned box |·|≤25;
  `theta_sign.reversing_involutions([2,1,1,1],25)` enumerates it (16 reversals
  total), but `theta_sign.py:64` (`if Mf[2] % N == 0: return None`) skips it,
  and `theta_sign.py:100` drops it from the tallies.
* Consequently T13's empirical statement "c=+1 for **all** reversing
  involutions in the box" excludes exactly the degenerate-chart cases where
  the new analytic proof also breaks. The two omissions coincide — the
  numerics could never have caught the gap.
* The degenerate chart is very probably still benign (the c=0 Weil operator is
  chirp/monomial, so conj(U_M) cancels it pointwise and Θ²=+1 is trivial),
  but nothing in the repo states or proves this. As written — "For reversing
  involution R … hence … exactly", "No Weil cocycle needed",
  "unconditional, elementary" — the claim overreaches.

**Fix required:** add the hypothesis gcd(M₂₁,N)=1 (or handle the c≡0 chart
separately, where it is easy), and re-word T13's coverage claim.

---

## C2 — U1: every fibre of Φ(x,y)=(a₁x+a₃y, b₁/x+b₃/y) on H² has ≤2 points

**Verdict: BROKEN as stated** (true generically; false without a
non-degeneracy hypothesis that the application does not guarantee).

**Counterexample (machine-verified, p=113, α=9, k=14).**
* a₁=a₃=0, (b₁,b₃)=(1,2) (both frequency vectors nonzero!): first coordinate
  of Φ is constant, fibre of (0,τ) is {(x,y)∈H²: b₁/x+b₃/y=τ} — max fibre
  size **5**, growing ~k. Symmetric case b₁=b₃=0, (a₁,a₃)=(1,2): also 5.
  In the master-moment application these coefficient patterns arise whenever
  two left frequencies are parallel to the same eigen-direction — perfectly
  legitimate members of a frequency box.
* Generic coefficients: max fibre = 2, confirming the intended regime.

**Degenerate-case audit of the elimination (the requested angles).**
* τa₁=0 branches: if (a₁,a₃)≠(0,0) one always gets a polynomial of degree
  ≤2 in x; degree drop (a₁=0 or τ=0) leaves ≤1 root; a double root is one
  point — "≤2" survives all of these. Dividing by a₃ is safe because the
  a₃=0 branch is handled by σ=a₁x forcing x.
* Denominators: H⊂F_p^×, so xy≠0 always; multiplying by xy is invertible.
  Roots of the quadratic outside H only shrink the fibre — irrelevant for an
  upper bound.
* The only genuine failures are the two "parallel frequencies" cases above.
* **Why the machine check missed it:** `fine_r4_struct.py:127` draws every
  coefficient from `rng.integers(1,p)` — zeros are impossible by
  construction. The check verifies the generic case only, giving false
  confidence in a lemma stated without the needed hypothesis.
* Salvage: U1 holds iff (a₁,a₃)≠(0,0) **and** (b₁,b₃)≠(0,0) for the pair.
  Downstream, U3's decomposition itself survives (brute==decomposed
  re-verified), and U2 actually sharpens: C(u,v)≤2 (not just ≤4) for
  (u,v)≠(0,0), since hh′=−u/v determines the pair through a quadratic.

---

## C3 — U4 conditional theorem (character orthogonality + ℓ² table + Cauchy–Schwarz)

**Verdict: orthogonality SURVIVES; ℓ² identity mis-derived (harmless);
final bookkeeping BROKEN — the printed conditional strength is not derivable.**

1. **Orthogonality direction and normalization: correct.**
   `#sol(S_F) = p⁻²(k⁴ + Σ_{(r,s)≠0} Πᵢ Sᵢ(r,s))` — two F_p constraints, each
   costing 1/p. Machine-exact verification including a non-trivial case
   (coef₁=coef₂, 40 pairings + 24 extras): brute = 64 = formula = 64.000000.
   Also fine: bounding extras by p⁻²|Σ_{≠0}ΠSᵢ| is legitimate because
   pairings ≥ 2k²−k > p⁻²k⁴ for k<p makes the leftover bracket negative.

2. **The "exact l² table identity" is wrong as an equality, right as a weak
   inequality, and does not come from U2.**
   For ab≢0, h↦(ah,b/h) is injective on H, hence
   `Σ_{r,s}|S(r,s)|² = Σ_{h,h'}Σ_{r,s}e_p(raΔ+s bΔ') = p²·#{h=h'} = p²k`
   **exactly** (machine-confirmed: 13448 = p²k = 13448 at p=41,k=8).
   The claimed "= p²·#{(h,h') collision-weighted}" is false as an equality
   (the collision weights C(u,v) never enter; only the diagonal does), and the
   ceiling 5p²k² is ~√k·5 slackier than the truth (537,920 vs 13,448).
   Attribution "consequence of U2" is bogus — injectivity suffices, U2 idle.

3. **Final Cauchy–Schwarz bookkeeping: the printed bound is unreachable.**
   With ‖S‖₂²=p²k (exact) and sup|S|≤kp^{−δ}, every Hölder/CS chain gives
   `extras ≤ p⁻²·‖S₁S₂‖₂·‖S₃S₄‖₂ ≤ p⁻²(kp^{−δ})²·(p√k)² = k⁴p^{−2δ}`
   (equivalently sup·‖S‖₂³ routes give the same scaling). The printed
   `extras ≤ 5k⁴p^{δ−2}` is *smaller* than this by the factor
   p^{2−3δ}/5 — at the repo's own demonstration scale (k=14, p=113,
   δ=0.005) the corrected CS ceiling is ≈3.7×10⁴ while the printed bound is
   15.4: **2400× too strong to follow from the stated inputs.** No choice of
   which factor carries the sup rescues it; CS simply cannot see the
   p⁻²-scale (random-image-model-sized) answer.
   Consequence for the headline: extras = o(pairings~2k²) follows from the
   *correct* bound only for k ≲ p^{δ} — vacuous for any published BGK/Bourgain–
   Garaev-type δ — whereas U4 claims k ≤ p^{1−δ/2−ε}. The conditional
   theorem, as proven, collapses to near-vacuity; reaching k~p^{1−δ/2}
   would need genuine cancellation input (correlation of the Sᵢ), not
   sup+ℓ² bookkeeping. **U4 downgraded to "conditional sketch with incorrect
   quantitative conclusion."**

---

## C4 — campaign statistics (β=0.87/1.74, L1 orderings, Σ²(64) anomaly, P3)

**Verdict: class dichotomy SURVIVES quantitatively; the Σ²(64) "4.5σ anomaly"
is DOWNGRADED to estimator/provenance artefact; P3 relaxation is POST-HOC and
unnecessary once artifacts are made consistent.**

*(a) Unfolding bias and matched controls.*
* Controls DO run the identical `unfold()/L1_table()/nvar()` code path
  (`largescale.controls`), so the pipeline-sharing claim is true. But they are
  computed at a **single** m_ref (~497) with reps=6, while the measurement
  pools 20 branches with heterogeneous dims (438…725). I rebuilt the control
  side properly: 10 independent pools of true GOE/GUE at the *exact* recorded
  dims list, through the same functions:
  * GOE: L1_goe = 0.0523 ± 0.0058, β = 0.838 ± 0.040, Σ²(64)[80-win]
    = 0.940 ± 0.039.
  * GUE: L1_gue = 0.0474 ± 0.0095, β = 1.822 ± 0.124.
* Measured values sit **inside 1σ** of these matched controls everywhere that
  matters: sym L1_goe 0.0596 (+1.3σ), gen L1_gue 0.0453 (−0.2σ), sym β 0.873
  (+0.9σ), gen β 1.743 (−0.6σ). The apparent "beats its own control"
  (0.0596 vs 0.0948) is a small-sample/single-m artefact of the shipped
  control, not super-GOE rigidity.
* Polynomial unfolding bias is real but *shared*: forcing mean spacing 1 with
  a degree-12 fit over ~500 levels suppresses long-range variance for data
  and control alike (their own GOE control Σ²(64)=0.806 vs my matched-dim
  0.940±0.039 and the literature asymptote ≈1.0 — the *control* is the
  outlier at −3.4σ, direction exactly as unfolding-suppression predicts).

*(b) The 4.5σ anomaly dissolves on three independent grounds.*
1. **Estimator/artifact mismatch:** 1.161±0.060 comes from
   `analyze_campaign.boot_nvar` (60 windows) compared against
   `goe_ctl_max=0.891` from `campaign_state` (80-window `nvar`, max over L —
   taken at L=16, not L=64!). The state file's *own* pooled value with the
   standard estimator is **1.0271**.
2. Window count is not the explanation of that gap (my synthetic A/B: 60w−80w
   = −0.004 ± 0.037), so the two run-5 artifacts disagree for reasons the
   current code cannot reproduce — a **provenance inconsistency**: no
   reviewer can regenerate 1.161 from today's `analyze_campaign.py` +
   `campaign_state.json`.
3. Against the matched-dim GOE control, the consistent-estimator value
   1.027 gives z ≈ (1.027−0.940)/0.039 ≈ **+2.2σ**, not 4.5σ — unremarkable
   for a long-window estimate, and in the expected direction given mild
   residual unfolding suppression of the control.

*(c) Preregistered P3 and the 10×→6× relaxation.*
* Facts: original P3 = Σ²(64) ≤ min(1.6×ctl_max, Poisson_max/10). Per-prime,
  only p=41611 violates (state `checks`), `prereg_all_pass=false` retained.
  Pooled: with the 60-window number 1.161 > 11.06/10 = 1.106 → FAILS the
  original criterion; passes only after the post-hoc relaxation to /6
  (=1.844), documented in `analyze_campaign.py`'s docstring ("relaxed from
  10x with reason").
* Judgment: **post-hoc.** Two aggravating circumstances: (i) the relaxation
  was only *needed* because the analysis switched estimators between
  artifacts — with the state file's own 80-window value (1.027) the ORIGINAL
  P3 passes pooled (1.027 < 1.106), i.e. the "violation" that motivated the
  relaxation is itself an artefact; (ii) the campaign's own protocol P4
  ("treat violation as bug signal first") was applied to the per-prime case
  but the pooled relaxation was adopted without resolving why two artifacts
  disagree. Mitigation: the state file preserves `prereg_all_pass: false`
  and the docstring discloses the relaxation — honest bookkeeping, misleading
  headline (`all_pass: true` in campaign_pooled.json refers to relaxed-only
  criteria).
* Bottom line: β and L1 class claims (sym→GOE, gen→GUE) **survive**,
  including under blind replication; the rigidity-at-L=64 *anomaly* claim and
  the necessity of the P3 relaxation **do not**.

---

## C5 — m1_new_configs.run_config([7,3,2,1],71) r=5 failure

**Verdict: BROKEN — reproduced verbatim; the hinted cause (PSI argument
placement) is exonerated; the actual primary bug is different, and fixing it
is not sufficient; additionally, NO passing r=5 exists anywhere in the repo.**

1. **Reproduction.** `run_config([7,3,2,1],71)` fails exactly as reported:
   |err| = 0.88 / **17.38** / 7.82 at λ#0,1,2 (artifact `m1_run5.json`
   matches digit-for-digit).
2. **Primary bug (visible in source, `m1_new_configs.py:29,44`).**
   `MF.rho_tables` returns RH[J] as *integer exponent tables* (output of
   `to_exp`, values in [0,2N)); master_formula.py always converts them via
   `exp(1jπρ/N)`. `s_of_j5` feeds them in raw:
   `rhof = rho.ravel()` … `np.dot(Wf*qq, rhof[idx])`. The ρ_J(v) factor thus
   enters as an O(N) integer instead of a unit phase. Fixing only this drops
   the error from 17.4 to ≤ 0.20 — still 10⁵× above the 10⁻⁶ gate.
3. **The hint is wrong about the culprit.** Verified independently:
   * product rule `T(g)T(h) = ζ^{Ψ(g,h)}T(g+h)`, Ψ row-first, holds to
     2.2e-15;
   * the bilinearised cross-phase κ(uP₂·g_{l,1} − uP₁·g_{l,2}) equals the
     explicit Σ_{prefix}Ψ(gᵢ,g_l) PSI lookups to **0.00e+00** for every J;
   * reducing the prefix sum uP mod N before the cross-phase is also
     harmless: κ·N = N(N+1) ≡ 0 (mod 2N) because N+1 is even.
   So sign/index placement of the PSI arguments is NOT the defect.
4. **At least one further defect remains.** After phasing ρ, the published
   vectorised structure still misses lhs by O(10⁻¹) (the size of the whole
   J-sum), while an independent clean-room rebuild of S_J (explicit PSI
   lookups, unreduced prefix sums) yields materially different |S_J|
   (290.6/298.8 vs 217.4/221.9/153.2) — the prefix/tail bookkeeping in
   `s_of_j5` is inconsistent with a convention-faithful computation
   somewhere beyond ρ. Machine-exact agreement was not achieved by any
   variant tested (best |err| ≈ 0.02–0.20 across branches).
5. **Scope inflation in the framing.** `artifacts/m1_run5.json` contains
   ONLY the failed config (note literally "instant-only", `passed: false`);
   the three Arnold r=5 configs never completed. Hence there is no evidence
   that "everything else passes at r=5" — run-4's master assembly covers
   r ≤ 4 only. **All of r=5 is unvalidated**, not one configuration.
6. Cosmetic but telling: `s_of_j5` line 44 ends in
   `… if False else …` dead code — unfinished editing.

---

## Summary table

| Claim | Verdict | One-line reason |
|---|---|---|
| C1 (O6/Θ²=+1) | DOWNGRADED | Proof silently assumes gcd(M₂₁,N)=1; legit reversal R=[[1,−1],[0,−1]] has M₂₁=0 and is silently skipped by theta_sign.py:64 |
| C2 (U1 fibre ≤2) | BROKEN as stated | a₁=a₃=0 (or b₁=b₃=0) gives fibres ~k (measured 5 at k=14); checker excludes zeros by construction |
| C3 (U4 conditional) | orthogonality SURVIVES; final bound BROKEN | ℓ² truth is p²k (exact); CS delivers extras ≤ k⁴p^{−2δ}, not 5k⁴p^{δ−2}; usable threshold collapses to k≲p^{δ} |
| C4 (campaign stats) | class dichotomy SURVIVES; anomaly + P3-relaxation DOWNGRADED/post-hoc | Matched-dim GOE control: L1 0.0523±0.0058, Σ²(64) 0.940±0.039 → measured within ~1–2σ; 1.161 vs 1.027 artifact inconsistency; original P3 would pass pooled under consistent estimator |
| C5 (r=5 failure) | BROKEN; hint misdirects | Primary bug = raw ρ exponents instead of ζ^{ρ/N}; fix insufficient (residual ~0.2); PSI placement exonerated (0.00e+00); no passing r=5 exists at all |

### Recommended minimal repairs (report only; nothing was changed)
* C1: add gcd(M₂₁,N)=1 clause or prove the c≡0 chart separately; amend T13 wording.
* C2: add (a₁,a₃)≠(0,0)∧(b₁,b₃)≠(0,0) hypothesis; re-draw checker coefficients from [0,p).
* C3: replace printed bound by extras ≲ k⁴p^{−2δ} + honest threshold k≲p^{δ}, or add a genuinely cancellative input; delete the U2 attribution.
* C4: reconcile campaign_state (1.027) vs campaign_pooled (1.161); recompute against matched-dim pooled controls; revert or re-justify P3 relaxation; keep `prereg_all_pass=false` visible in headlines.
* C5: convert ρ via exp(1jπρ/N), then debug the remaining prefix-tail discrepancy against the clean-room implementation; complete the three Arnold configs before claiming r=5.
