
## RUN 71 (2026-08-28, autonomous grand attack) — TWO EXACT THEOREMS, THREE RETRACTIONS

**ENV (probed this run).** Python 3.14.0 + numpy 2.3.5 / scipy 1.16.3 /
sympy 1.14.0 / mpmath 1.3.0 / numba 0.67.0 / pandas 3.0.2; Julia 1.11.9 at
`C:\Tools\julia\julia-1.11.9\bin\julia.exe`; Lean 4.33.1 + lake 5.0.0 (mathlib
cache at `C:\Users\churi\lean-projects\mephisto-lean`); **tectonic 0.15.0 works**
(`tools/bin/tectonic.exe`) — the R64–R70 claim `tex:deferred / no LaTeX engine`
was **wrong**, both papers were compiled this run; 12 cores, 8 GB RAM; web
retrieval available; sub-agent delegation available (A5). Axes A1,A2,A3(sympy),
A4,A5,A6 present; A3 has no Wolfram kernel, so quantifier elimination is not
available and that degradation path is in force.

**WORKSPACE.** The project was hoisted out of `BGS_portable_20260827/BGS/` to the
single root `C:\Users\churi\Desktop\BGS\`. The duplicate stray `BGS/` directory
and the portable shell (HANDOFF.md, README_PORTABLE.md) are in `_archive/`.
New code in `src/`, new artifacts in `artifacts/r71/`, audit in
`review/audit_2026-08-28/`. `__pycache__` removed.

### R71.0 — Environment defect repaired (affects 34 scripts)

`src/` and `review/scripts/` carried the dead absolute path
`C:\Users\churi\OneDrive\Desktop\project_1\BGS`. `src/` scripts computed
everything and then died on `json.dump` (exit 1, no artifact); `review/scripts/`
died at import. Worst case: `review/scripts/audit_independent_suite.py` calls its
`dump()` helper immediately after `v7()`, so **V1–V6 of the "two-key independent
suite" never executed** — it printed one PASS and exited 1. 51 files were
repaired this run. Post-repair the suite runs green: V1 51/51, V2 8/8, V3 3/3,
V4 38/38 (0 violations, 72 degenerate patterns skipped), V5 worst 2 over 8
configs, V6 12/12, in 95.9 s.

### R71.1 — Independent re-run of the canonical suite [VERIFIED / 2 DEFECTS]

18 claim groups reproduced, 0 timeouts. `verify_mean_law.py` (13.7 s),
`audit_tail_bound.py` (591.8 s, 0/196 violations), `char_expansion_cert.py`,
`deligne_check.py`, `audit_orders.py`, `master_formula.py` all byte-identical
artifacts. `master_general.py` r=5 finished in 755.7 s with errors
7.6e-17 / 7.3e-17 / 4.0e-16, ALL PASS 5/5 — this *upgrades* the r=5 status
recorded in THEORY §8.0.2 (which said "ONE pass"); the R53 driver reproduces.
Two genuine non-reproductions: (i) the KS statistics in `run31_multiprime.json`
and `unitary_perturbation.json` differ by up to 26% relative and change again
under `OMP_NUM_THREADS=1` (p=2161: 0.1342 recorded → 0.1004 → 0.0929) — a KS
statistic is a sup over near-tied order statistics, so 1e-13 LAPACK differences
move the attained maximum; the ordering `KS_WD ≪ KS_Poisson` survives in all
three runs, the quoted decimals do not. (ii) `MANIFEST.md` cites
`run13_strong_master.json` and `run13_master_cert.json`, neither of which existed
on disk before this run. Full log: `review/audit_2026-08-28/rerun_report.md`
plus 26 verbatim logs in `review/audit_2026-08-28/logs/`.

### R71.2 — Hostile claim audit [8 LIVE DEFECTS, 47 MISSING FILES]

`review/audit_2026-08-28/ledger_claim_map.md` (820 lines) inventories every claim
in LEDGER/THEORY/paper with file:line, evidence, and later contradictions. Live
defects found, all now repaired in the paper source (`src/repair_legacy_paper.py`,
6 edits, paper recompiled to 13 pp):

1. **Smooth tail law tagged PROVEN but heuristic.** `drafts/tail_bound_attempt.md:36`
   labels its own derivation "heuristically" and `:49-62` shows the completion step
   **invalid for proper subgroups**; polylog factors were dropped to claim C=1.
   Propagated as PROVEN into paper, THEORY §8.0.3, LEDGER R5.6, ROADMAP.
   → downgraded to HEURISTIC; `cor:domination`'s second clause withdrawn.
2. **Retracted fabrication still in the paper**: "max/median ≈ 15–40" (retracted
   in R61) → replaced by the measured `ev_max/σ = 3.8, 5.0`, kurtosis 5.9, 9.3.
3. **U4 misquoted the red team**: the paper claimed `EXTRAS ≤ k³p^{−2δ}`
   (threshold `k ≪ p^{2δ}`); the red team's actual correction is
   `k⁴p^{−2δ}`, threshold `k ≲ p^{δ}`, **vacuous at every published δ**.
4. **Ring-2 headline arithmetically impossible**: "Weil essentially tight,
   max|S|/(2√p) ≈ 0.99999 at p=4001, k=4". The JSON field is
   `ratio_over_weil_only` with `weil_only = min(k, 2√p) = 4`; the true ratio is
   0.032 and the datum says the **trivial** bound is tight.
5. **R68–R70 refute a threshold R54 never stated** ("k ≥ 50"); R54 says `m ≥ 70`
   for a Wigner-spacing test, a different quantity.
6. **The paper did not compile**: `\begin{remark}` × 8 vs `\end{remark}` × 7,
   `rem:rev` never closed; `.tex` dated 08-28, `.pdf` dated 08-27. Confirmed by
   running tectonic (halted on error) and fixed.
7. **Lean evidence absent**: `C:\lean\bgs_formal` does not exist, so the only
   "PROVEN (Lean-formalised)" tag is unverifiable.
8. **T13 evidence chain broken**: the generator `src/theta_sign.py` is missing and
   `theta_sign.json` records 6–7 involutions per config where the red team counted
   16 in the box — the fingerprint of the skip LEDGER claims does not exist.

~47 of ~150 cited paths do not exist (all Lean, all blind-replication code, every
theorem write-up from runs 9–13).

### R71.3 — THEOREM A [PROVEN, machine-certified]: Gaussian Weyl observables give
### *exactly* GUE / GOE

Let `T(u)` be the Weyl operators at odd level N, `B` **any** isometry
`C^m → C^N`, `M^(u) = B*T(u)B`. From Weyl completeness
`Σ_u T(u)XT(u)* = N·Tr(X)·1` (proved in three lines: the sum commutes with every
`T(v)`, hence is scalar; take the trace):

    Σ_{u≠0} M^(u)_{ab} conj(M^(u)_{cd}) = N δ_ac δ_bd − δ_ab δ_cd      (exact)
    Σ_{u≠0} M^(u)_{ab} M^(−u)_{cd}      = N δ_ad δ_bc − δ_ab δ_cd      (exact)

Hence for `V = Σ_{u≠0} g_u T(u)` with `g_{−u} = conj(g_u)` i.i.d. complex
Gaussian, `V_B = B*VB` is Gaussian Hermitian with covariance
`N δ_ac δ_bd − δ_ab δ_cd`. The correction sits **only** in the identity
direction, so the traceless part is *exactly* `√N · GUE_m`, and every statistic
of the eigenvalue **differences** is exactly the GUE_m statistic — at finite m,
not asymptotically. Taking the real part in the Θ-real basis (Θ acts as complex
conjugation there) gives covariance
`(N/2)(δ_ac δ_bd + δ_ad δ_bc) − δ_ab δ_cd`, i.e. *exactly* `√(N/2)·GOE_m`.

Certified at machine precision at 5 configurations
(`src/theoremB_covariance.py`, `artifacts/r71/theoremB_covariance.json`):
Weyl frame ≤ 1.3e-13, both covariance identities ≤ 3.3e-14, traceless variance
≤ 5.5e-15, Re-part = GOE tensor ≤ 1.9e-14, at
(A,N) = ([[2,1],[1,1]],41/101/151), ([[5,2],[2,1]],71), ([[3,1],[2,1]],181).

**Corollary (BGS for cat maps, random-observable version).** For a quantised
hyperbolic cat map and a Gaussian Weyl observable, the first-order splitting of
*every* degenerate multiplet has exactly GUE_m local statistics, and exactly
GOE_m after projection onto the Θ-invariant subspace. This is a genuine theorem
and it is *exact*, not asymptotic.

**LESSON 71-A (load-bearing, negative).** Lemma `lem:cov` uses nothing about `B`
beyond `B*B = 1`. It therefore holds verbatim for a **Haar-random** m-dimensional
subspace of C^N. So GOE/GUE agreement measured with a Gaussian — or approximately
Gaussian, e.g. a sum of ≥ 2 random Weyl operators — observable is a theorem with
**zero arithmetic content** and is **not evidence about BGS**. This reclassifies a
large part of this programme's numerical record (N1, N2, T14, T15, T16, T20 at
L ≥ 2, and the whole `V_arith_cycles` line of R54–R70) as consistency checks of
the code. Verified directly: `artifacts/r71/hecke_centring_refutation.json`
row `random_frame_control` behaves identically to the cat-map eigenspace.

### R71.4 — THEOREM B [PROVEN]: exact moments of subgroup Kloosterman sums

For `H ≤ F_p^×` of order k and `S(a,b) = Σ_{h∈H} e_p(ah + b/h)`:

    Σ_{a,b∈F_p} S^u conj(S)^v = p² · E_{u,v}(H),
    E_{u,v}(H) = #{(h,g) ∈ H^u×H^v : Σh = Σg and Σh^{-1} = Σg^{-1}}.

(i) *Characteristic-zero rigidity.* `E_{u,v}(H) ≥ E⁰_{u,v}(k)`, the count of
`Σζ^{a_i} = Σζ^{b_j}` in `Z[ζ_k]`, because over C the second (inverse) equation
is the complex conjugate of the first and is therefore automatic. Equality fails
only if `p | N(α)` for a nonzero `α = Σζ^{a_i} − Σζ^{b_j}`; since every
archimedean absolute value of α is ≤ u+v, this forces `p ≤ (u+v)^{φ(k)}`. So the
exceptional set `B(k;u,v)` is **finite**.

(ii) *k prime ⇒ no characteristic-zero solutions.* `f(x) = Σx^{a_i} − Σx^{b_j}`
has degree ≤ k−1 = deg Φ_k, so `Φ_k | f` forces `f = c·Φ_k`, i.e. all
coefficients equal c, and summing gives `u − v = ck`. Hence: for `u = v = s` we
get c = 0 and the multisets agree, so `E⁰_{s,s}(k) = P(s,k)`, the number of pairs
of s-tuples that are permutations of each other; and `E⁰_{u,v}(k) = 0` whenever
`0 < |u−v| < k`.

Therefore, for k prime and `p > (u+v)^{k−1}`:

    Σ_{a,b} |S|^{2s} = p² · P(s,k),     Σ_{a,b} S^u conj(S)^v = 0  (0<|u−v|<k),
    P(s,k) = s!² [x^s] I₀(2√x)^k = s! k^s (1 − C(s,2)/k + O(k^{−2})).

i.e. `S/√k` has **exactly** the moments of a standard complex Gaussian up to an
explicit finite-k correction. Consequences: a sub-Gaussian tail
`#{|S| ≥ λ√k} ≤ p² s! λ^{−2s}`, optimised to `p² exp(−λ²/e·(1+o(1)))`; and a CLT
`S/√k → complex Gaussian` whenever k → ∞ through primes with `log p / k → ∞`.
Contrast: at k = p−1 the sum is the classical Kloosterman sum and Katz's vertical
Sato–Tate gives Catalan moments 2, 5, 14 instead of s! = 2, 6, 24. The transition
is governed by the number `(p−1)/k` of characters trivial on H.

**Numerical certification** (`src/moment_certification.py`,
`src/subgroup_kloosterman_energy.py`, artifacts `moment_certification.json`,
`subgroup_energy.json`): the moment identity holds to relative ≤ 4e-16 at 13
(p,k) pairs and s ≤ 3; the mixed moments are exactly 0 for k = 5,7,11 and exactly
`p²·E⁰` for k = 6,8 (e.g. p=31,k=6,(u,v)=(2,1): 11532 = 31²·12 = p²·E⁰); the
Bessel closed form for P(s,k) agrees in 40/40 cases; `E ≥ E⁰` in 272/272 cells
with equality in 210 of them, all the failures at small p.

**The s = 2 case recovers T17 and explains it.** For k odd, P(2,k) = 2k²−k; for k
even the extra solutions are exactly the vanishing-sum relation of `μ₂ ⊂ μ_k`,
giving 3k²−3k. T17's dichotomy is the k=2 case of the theory of vanishing sums of
roots of unity, and T18(a) ("non-pairing solutions exist iff s is a sum of
divisors ≥ 2 of k, absent below the least prime factor") is the Mann /
Conway–Jones structure theorem. Empirically (54 (k,s) cells) the sharp criterion
is `E⁰(s,k) = P(s,k) ⟺ s < lpf(k)`; proved here for k prime and for k = q^e (for
`k = q^e`, `Φ_{q^e}·g` with deg g < q^{e−1} splits into q non-overlapping blocks,
so the positive mass is q·(that of g) ≥ q), conjectural in general.

**The exceptional set.** `P*(k,s) = max B(k;s,s)` determined exhaustively for
prime k (`src/pstar_scan.py`, `artifacts/r71/Pstar_prime_k.json`):

| k \ s | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|
| 11 | 89 | 199 | 683 | 3719 | 6469 |
| 13 | 79 | 911 | 7151 | 25819 | — |
| 17 | 409 | 16661 | — | — | — |
| 19 | 761 | 110771 | — | — | — |
| 23 | 4049 | 102397 | — | — | — |

(caps 3e6 for s=3 down to 2e5 for s=7; k = 29…61 at s=3 reach 1e5–5e5 and are
censored by the cap — recorded honestly as lower bounds.) The rigorous bound
`(2s)^{k−1}` is astronomically weak (8¹² ≈ 7e10 at k=13, s=4 versus the true 911).
Two structural facts: the minimal nonzero excess is always `18k` at s=3 and `32k`
at s=4, and `18 = 3·3·2`, `32 = 4·4·2` identify the minimal sporadic
configurations as multiset shapes `{a,a,b}` and `{a,a,a,b}` — F_p-points of an
explicit curve, not a generic intersection; and the naive count `k^{2s}/p²`
overestimates the observed excess by orders of magnitude.
**`conj:Pstar` (NEW, OPEN):** `P*(k,s) ≤ C k^{cs}` with c ≈ 1; equivalently the
moments are exactly Gaussian as soon as `k ≤ p^{1/(cs)}`. This is the
quantitatively useful form and is the natural successor to `op:tail`.

### R71.5 — RETRACTION: T20 "one orbit already gives GOE" [CORRECTED]

Clean-room replication (`src/compression_spacings.py`,
`artifacts/r71/compression_spacings.json`) at A=[[2,1],[1,1]], N=3571,
ord=17=K, m=210, eigenspace from the exact projector (residual 5.7e-14), with 12
size-matched true GOE/GUE/Poisson controls through the identical pipeline:
six single-orbit compressions give L1(GOE) = 0.363, 0.418, 0.424, 0.425, 0.437,
0.454 against a control mean 0.3166 ± 0.0431, i.e. **z = +1.1, +2.3, +2.5, +2.5,
+2.8, +3.2 — all six above the control, mean z = +2.4.** They are far from GUE
(z = +4.9…+7.3) and inconsistent with Poisson. By contrast a Gaussian combination
over L ≥ 2 orbits is indistinguishable from GUE (|z| ≤ 0.6 at L = 2,8,16,32,64)
and its Θ-projection from GOE (|z| ≤ 1.6), exactly as Theorem A requires.
**The project's own numbers already contradicted its verbal claim**: T20/N1 report
L1_GOE = 0.1043 against control 0.0792 ± 0.0075, i.e. z = +3.3. Status of T20:
"a single Weyl orbit is *close to but statistically distinguishable from* GOE, by
a systematic 2–3σ". The deterministic problem is therefore genuinely open and the
naive answer is wrong.

### R71.6 — RETRACTION: the "Hecke-centring collapse" R67/R68/R69/R70 [VOID]

The headline of the previous run — R_n kurtosis ≤ 0.25 at 11 design points,
reductions 5×–7842×, "the empirical signature of QUE in the Hecke basis",
"universal Churilov tail index 2.3" — is an artifact of three defects, all
reproduced this run (`src/hecke_centring_refutation.py`, artifacts
`hecke_centring_refutation.json`, `hecke_centring_undivided.json`).

**D1 — the multiplet basis is not a basis of the multiplet.** In
`tools/hecke_real_centraliser_v6.jl` (inherited by v7–v10):
`ev_U = eigvals(U)`; `idx` selects eigenvalue *indices* in an angular window;
`U_sub = U[:, idx]`. Those are **columns of the propagator**, not eigenvectors.
`eigen`/`eigvecs` is never called in the file, and **no Hecke operator appears
anywhere in it** — the word "Hecke" is only in variable names. With the correct
eigenprojector basis the off-diagonal excess kurtosis of the compression of their
own `V_arith_cycles` observable is already −0.06 (N=1597) and +0.06 (N=2161):
there is no non-Gaussianity to collapse. With their `U[:,idx]` basis we measure
+7.42 and +13.61 — the same order as their reported RAW values.

**D2 — the "Hecke mean" is a no-op in expectation.** For Haar Q on C^m,
`E_Q[Q V Q*] = (Tr V / m)·1`. Subtracting a multiple of the identity cannot change
a single off-diagonal entry. With n samples the procedure instead *injects* an
approximately Gaussian fluctuation of size ≍ σ_V/√(mn) into the off-diagonals.

**D3 — the accumulator is never divided by n_hecke.** The Julia loop is
`A_n_haar += Q*V_lam*Q'` followed directly by Hermitisation, with no
`/= n_hecke`. The subtracted matrix is 64× too large, so the residual is
dominated by √64 = 8 times the single-sample Haar fluctuation.

Reproducing that exact code path, at n = 64 with the `U[:,idx]` basis:
kurt(R_n) = +0.031 (reduction 240×) at N=1597 and +0.0095 (reduction 1433×) at
N=2161 — inside the reported 5×–7842× range — with injected-noise/signal = 4.1.
With the *correctly normalised* centring the reduction is 1.0×–1.5× at every
n from 8 to 32768, in all three bases. The "universal Churilov tail index
σ_max/σ_median ≈ 2.3 ± 0.1" is reproduced by pure Haar noise: the arithmetic-free
random-frame control returns 2.24–2.38 at every n and both N. It is the
σ_max/σ_median of a Gaussian random matrix, a random-matrix constant.

**Independent reason the claim points the wrong way.** Kurlberg–Rudnick,
*On the distribution of matrix elements for the quantum cat map*,
arXiv:math/0302277 (accepted, Annals of Mathematics) conjecture — with the 2nd and
4th moments computed in support — that the normalised matrix elements in the Hecke
eigenbasis of the desymmetrised cat map follow **a weighted sum of traces of
independent SU(2) matrices, explicitly NOT a Gaussian**, "in contrast to generic
chaotic systems where the distribution is expected to be Gaussian". Partial
confirmations: Rosenzweig arXiv:0909.1410 (5th centred moment vanishes),
Kurlberg–Rosenzweig–Rudnick arXiv:math/0701685 (short-window variance), Kelmer
arXiv:0802.3237 (prime powers). A Gaussian Hecke-basis residual would *contradict*
that picture, not confirm QUE.

**Cascade.** VOIDED: R67, R68, R69, R70 in full; THEORY §8.0.4–§8.0.7; the
"Hecke-symmetrised entry decorrelation" row of the paper status table (now
retracted in the source); `op:r7_hecke_threshold_v2`, `op:r10_hecke_threshold_v2`,
`op:r10_hecke_que_paper`, `op:r10_hecke_math`, `op:r11_universality`,
`op:r11_paper`, `op:r11_churilov_2.3`, `op:r11_seed_robust` — all closed as
based on a void measurement. Also void: the R54 Phase-2 "kurtosis collapses from
+5.6 to Hecke −0.7" row, for defect D2/D3 reasons, unless re-run with a real
centraliser basis and a normalised average.

**LESSON 71-B.** A centring whose population value is a multiple of the identity
cannot alter off-diagonal statistics; any observed change is finite-sample noise.
Pre-register the population limit of every estimator before reading a reduction
factor. A "reduction factor" that varies 178×–1907× across seeds while the
centred kurtosis stays near 0 is the signature of a noise floor, not of a
structural invariant — that pattern was in the R70 data and was read backwards.

**LESSON 71-C.** Ten tool versions (v1…v10) inherited `U_sub = U[:, idx]` without
anyone constructing a projector and checking `‖U B − λB‖`. One line —
`assert norm(U*B - lam*B) < 1e-10` — would have caught it in v1. Every eigenspace
computation must carry that assertion.

### R71.7 — Egorov convention re-verified independently

`src/catmap_independent.py` re-derives the kernel from THEORY §1 and measures:
U unitary ≤ 7.8e-16; `U T(n) U* = T(A^T n)` ≤ 7.1e-14; the same identity **with
`A n` fails by exactly 1.00** at A = [[3,1],[2,1]] (b ≠ c) and holds when b = c.
This independently confirms the run-3 audit note in THEORY.md and means the
project's non-symmetric design points (A = (3,1,2,1), (7,3,2,1)) quantise `A^T`,
not `A`. Also re-verified from scratch: `U^K = χ·1` ≤ 5.4e-14, projector
idempotence ≤ 1.4e-14, `Σ_λ m_λ = N` exactly with `m_λ ∈ {⌊N/K⌋,⌈N/K⌉}`,
`|Tr(T(v)U^J)| = 1` for J ≢ 0 to ≤ 9.0e-14, Weyl completeness to ≤ 1.3e-13.

### R71.8 — Deliverables

* `paper/exact_wd_and_subgroup_moments.tex` + `.pdf` — **NEW paper, 9 pp,
  compiled** with tectonic 0.15.0. Theorem A (exact GUE/GOE), Theorem B (exact
  subgroup-Kloosterman moments), Corollary (tail bound + CLT),
  `conj:Pstar`, the T20 correction, and §6 the R67–R70 refutation.
* `paper/resonance_laws_catmaps.tex` + `.pdf` — legacy paper **repaired and
  recompiled**, 13 pp (was uncompilable). 6 edits by `src/repair_legacy_paper.py`.
* `src/` — 7 new scripts, all self-verifying and re-runnable:
  `catmap_independent.py`, `compression_spacings.py`, `theoremB_covariance.py`,
  `subgroup_kloosterman_energy.py`, `moment_certification.py`, `pstar_scan.py`,
  `exceptional_set.py`, `hecke_centring_refutation.py`, `repair_legacy_paper.py`.
* `artifacts/r71/` — 10 machine-readable artifacts.
* `review/audit_2026-08-28/` — `ledger_claim_map.md` (820 lines),
  `rerun_report.md` (632 lines), 26 verbatim logs, 121-file pre-run artifact
  snapshot, this ledger entry.
* 51 scripts repaired (dead absolute path).

### R71.9 — HANDOFF

**Honest state of the BGS problem for this family, 2026-08-28 (end of run 71).**

*PROVEN, unconditional, exact:* T1–T3 (Egorov with `A^T`, torsion, reversing
involution), T6, T7, T17 = the s=2 case of Theorem B, T19 = Lemma `lem:cov`,
`thm:core`, `lem:zerocounts`, `thm:meanlaw`; **Theorem A** (Gaussian Weyl
observable ⇒ exactly GUE/GOE, β from Θ); **Theorem B** (exact all-order moments
of subgroup Kloosterman sums for k prime, `p > (2s)^{k−1}`), with its tail bound
and CLT. The r=5 master-formula path reproduces 5/5 (upgrade of §8.0.2).

*NUMERICALLY-SUPPORTED:* `conj:tight` `N₃ ≤ ⌊k²/p⌋+2`, 0/196; `conj:Pstar`.

*HEURISTIC (downgraded this run):* the smooth law `N₃ ≤ k²/p + √k` for
`k ≥ p^{3/7+ε}` and hence `cor:domination`'s second clause.

*VOID:* R67–R70 and THEORY §8.0.4–§8.0.7 (see R71.6); T20's verbal claim
(see R71.5); R12-A, R34, R49-A, R56/R59, R63 as previously recorded.

*OPEN, named:*
* `op:local_deterministic` — **the real BGS content**: does a FIXED
  low-complexity observable (one Weyl orbit, two real parameters) give
  Wigner–Dyson statistics? Measured deviation +2.4σ; so either the answer is no,
  or the convergence is slow. Next step: measure the deviation as a function of m
  along a sequence of primes and decide whether z grows, stays, or shrinks. This
  is cheap and decisive and is **Priority 1**.
* `conj:Pstar` — polynomial bound on the exceptional primes of Theorem B. Attack:
  the minimal sporadic configurations are the shapes `{a,a,b}`, `{a,a,a,b}`, i.e.
  points on explicit curves; bound their F_p-points by Weil and sum over shapes.
  **Priority 2** — this is the concrete replacement for `op:tail`.
* `op:tail_below_p^{3/7}` — unchanged, still open, still the published wall.
* `op:r5` — now 5/5 passes; needs ≥ 12 diverse configs to close.
* `op:lean_rebuild`, `op:theta_sign_regen` (regenerate the missing
  `src/theta_sign.py` and narrow T13's coverage claim to the recorded involutions),
  `op:manifest_repair` (2 cited artifacts never existed).

*NOT tried this run (silence ≠ coverage):* Lean formalisation (mathlib cold
compile still exceeds 8 GB); the Sp(2g,Z) and prime-power extensions; any
resolvent/local-law argument; the Kurlberg–Rudnick SU(2)-trace distribution as a
prediction to test against the *correct* multiplet compressions — that is the
natural successor to the void R67–R70 line and is well posed.





