# REVIEW R108 — Full referee audit of the BGS programme (2026-09-02)

**Referee:** independent re-derivation and re-execution, run as R108.
**Method:** every load-bearing claim of the k=4 chain was re-implemented
from the paper definitions only (`code/referee/r108*_*.py`), validated
against brute-force ground truth at N=53, and cross-checked against the
workspace artifacts.  Exact layers (Theorems C, H, II, 91.5, B) were
re-verified independently; the fluctuation layer (M1) was re-derived and
re-measured.  Three audit subagents covered HISTORY/artifact provenance,
the verification suite, and code-vs-paper fidelity.

## Verdict in one paragraph

The exact/arithmetic layers of the programme are solid and reproduce
independently to machine precision or exactly.  The M1 "Möbius–fiber
theorem" (`δ = o(1)`, `|δ| ≤ 16/K²`) — the claimed closure of the k=4
fluctuation layer — is **not proven and is partially false**: its N=3571
calibration number is wrong (a real code bug, root cause identified),
its "exact twist decomposition" has non-vanishing cross terms that carry
89–99.99% of the very quantity it claims to bound, its Parseval constant
is off by at least 16×, and its regime claim ("δ = o(1) at fixed K") is
a logical error.  The k=4 layer of H3 is therefore **OPEN**, and the
honest open problem it leaves is sharper than the one the workspace had:
control of the coset-stratum cross terms (§C below).

## A. Independently CONFIRMED (solid)

| Claim | Check | Result |
|---|---|---|
| Thm 91.5 arcsine law, Tr(M_q^{2s}) = C(2s,s)(N−1) − β_s | own construction of V = J/(N−1) over the full character group, s = 1..6, q = 1,2,3, N = 53, 199 | EXACT integers, rel ≤ 7e−15; partial-isometry algebra V V* = I−E, V*V = I−F holds to 2e−14 |
| Thm B, balanced 2nd moment of subgroup Kloosterman sums | own S_H(a,b) at p=199, k=11 (−1∉H) | Σ\|S_H\|⁴ = 9,147,831 = p²(2k²−k) EXACTLY (rel 0.0) |
| k=2 layer / key-table model | own brute-force ground truth at N=53 (a=10, K=13): Z₀ = 12,063, E_c = 3.410502e9, mean Σ₄ = 4143.4615, std = 1913.79 | all match the paper to all digits |
| Twist identity B = (1/m²)Σ(A_ψ⋆A_ψ) as an identity for B | pipeline vs ground truth at N=53 | rel diff 1.4e−16 (the identity for B itself is exact algebra and holds) |
| Flatness c(d) = (N−2)+ε, \|ε\| ≤ 2 | measured all fibers, N = 53, 199, 3571 | c ∈ {N−4, N−3, N−2}; elementary proof checks out |
| Thm C (Θ² = +1) | subagent re-run, 504 configurations | worst \|Θ²−1\| = 1.56e−15 PASS |
| Thm H (shape decomposition, M_r = 0, r ≤ 10) | subagent re-run | 8/8 exact matches PASS |
| Thm II certificates (R82.12) | subagent re-run baseline_r82.py | N=199: 5.95e−14, N=3571: 2.38e−13 PASS |
| GOE spacing KS, designs N=3571 (m₊=105), N=19489 (m₊=336) | subagent re-run goe_spacing_test.py | KS 0.0140 < 0.0211, 0.0089 < 0.0113 PASS |
| h3 k=2 exact reduction | subagent re-run | identity verified; \|P\| exact |
| E_unc values | own pipeline | E_unc(199) = 1.13993e16, E_unc(3571)/m⁴ = 3.79058e15 — match paper |

## B. REFUTED / wrong (with root causes)

### F1 — The N=3571 coupled energy is wrong; δ = −6.9% should be +17.65%

The paper's table (Thm `thm:delta` context, R95.2, mobius_fiber_theorem)
states E_c(N=3571) = 3.545e15, E_unc/m⁴ = 3.791e15, δ = −6.9%.
Two fully independent recomputations agree:

- twist pipeline (validated digit-for-digit against brute force at N=53):
  E_c = 4.459482e15;
- direct enumeration of H-coupled key pairs via a difference table
  (`r108b_direct3571.py`): E_c = 4.459482e15 (rel diff 4.3e−12),
  Z₀ = 26,385,585.

Hence **δ(N=3571) = +17.65%**, not −6.9%.  The sign itself was wrong.

**Root cause:** `code/large_m/third_calibration.py` (RUN 93.2, the source
of the 3.545e15 number) has a fancy-indexing bug in its class-1 loop:
`Dp = dg_flat[U2 - 1, V2 - 1]` uses **inner** (paired) indexing, so the
u-coordinate of the partner key is taken from the *column* index (v₁)
instead of the *row* index (u₁).  The docstring states the correct rule
— partner of (u₁,v₁) is (t₁/u₁, t₂/v₁) — which requires **outer**
indexing (`np.ix_(U2-1, V2-1)`).  The N=53/199 numbers were later
re-verified by the (correct) twist pipeline, but the N=3571 number was
carried over from the buggy R93.2 script and never re-checked.  The
artifact `artifacts/r93/sigma4_third_calibration.json` is missing from
the workspace, so the wrong number also lacks provenance.

### F2 — The "exact twist decomposition" has non-vanishing cross terms

Thm `thm:twist` (R95.1) claims E_c "decomposes into the m² twist-pair
energies" — i.e. E_c = (1/m⁴)(E_triv + Σ_ψ E_ψ) with no cross terms —
"verified to all digits at N=53, N=199".  What was verified at those
designs was the **identity for B** (which is exact algebra and does
hold); the **energy decomposition** is a different statement and it is
false.  Measured (own pipeline, exact):

| N | m⁴E_c − E_unc | nontriv pair share | cross-term share |
|---:|---:|---:|---:|
| 53 | 9.54e9 | 1.06e9 (11.1%) | 8.49e9 (88.9%) |
| 199 | 7.35e14 | 6.17e12 (0.8%) | 7.29e14 (99.2%) |
| 3571 | 1.3009e24 | 9.93e19 (0.008%) | 1.3008e24 (99.99%) |

The cross terms are not small, grow with N along the designs, and are
not bounded by *any* argument in the workspace (a trivial bound gives
m⁴·256N⁵ per cross pair, i.e. 256m⁴N⁵ total — divergent relative to
E_unc ~ N⁷).  **The entire content of the k=4 estimate lives in the
cross terms, and the M1 proof does not touch them.**

### F3 — The Parseval constant 16 is unproven (correct constant: 256)

Thm `thm:delta`/`thm:fiberweil` route: "Parseval gives E_twist ≤ c_w²N⁵
per nontrivial pair" with c_w = 4, i.e. 16N⁵.  From the per-fiber Weil
bound alone the correct derivation is:
\|(A⋆A)(t)\| ≤ Σ_d\|A(d)\|² ≤ N·(4√N)² = 16N², hence
E_ψ ≤ N·(16N²)² = **256N⁵**.  The constant 16 does not follow from any
stated step.  (The original note also asserts Σ_ω|Â(ω)|² ≤ 4N⁴ —
the correct value is 16N³.)  Empirically per-pair energies are far
below even this: max E_ψ/N⁵ = 0.29 (53), 0.081 (199), 0.0042 (3571) —
the per-pair part of the claim was never the problem; see F2.

### F4 — "δ = o(1) along the design scaling (K fixed, N → ∞)" is a logical error, and the scaling itself is impossible

Even granting \|δ\| ≤ c_w²/K²: at **fixed K** this is a constant, not
o(1).  Moreover, for the cat map the "K fixed, N → ∞" scaling cannot
exist: ord_N(a) = K with a = (3+√5)/2 forces N to divide the fixed
rational integer Norm(a^K − 1), so only finitely many split primes have
ord = K.  The honest regime for BGS is N → ∞ with m₊ = (N−1)/(2K) → ∞,
i.e. K → ∞ (K = o(N)).  In that regime a bound \|δ\| ≤ C/K² *would*
give δ → 0 — but only once the cross terms (F2) are controlled, which
is exactly the missing mathematics.  Empirically δ moves the wrong way
along the three legacy designs (+1.1% → +6.4% → +17.65% at K = 13, 11, 17).

### F5 — The per-fiber Weil bound needs the d = 0 carve-out

As stated ("for every d"), Thm `thm:fiberweil` is false: the diagonal
key (1,1) carries multiplicity N−2 at difference d = 0, so
\|A_ψ(0)\| = N−2 for every pair, including nontrivial ones (measured:
51 at N=53, 197 at N=199, 3569 at N=3571).  With d = 0 (equivalently the
diagonal key) excluded, the bound holds with room:
max\|A_ψ(d)\| = 120.51 ≤ 4√3571 = 239.03 at N=3571 (0.51 of the
ceiling; the degree count gives 3√N, so c_w = 3.5 suffices).

### F6 — Design bookkeeping errors in the Möbius-fiber note

The note's setup says "a²−3a+1 = 0 in F_N, H = ⟨a⟩" for all three
designs including N=53, K=13.  But 5 = t²−4 is a **non-residue mod 53**
(5²⁶ ≡ −1), so x²−3x+1 has no root in F₅₃; the N=53 design element is
a = 10 (ord 13), which is not a root (10²−30+1 = 18 ≠ 0).  The N=53
point tests the character-sum mechanism, not the cat map proper.
(At N=199, a=139 and at N=3571, a=2469 the root claim is correct;
a = 47 also has order 17 and generates the same H as 2469 — 47¹⁷ ≡ 1.)
Related: the paper tables mix m = 210 (full annihilator coset) and
m₊ = 105 (parity-restricted half) at N=3571 without flagging which is
which; and two different asymptotics are claimed for the same object
mean(Σ₄): ~N^{1.9} (Thm `cor:h3closed`) vs ~N³/K² (conditional corollary),
with three different rates for the same relative fluctuation
(K²/N^{0.9}; O(K² polylog/N^{1.5}); measured N^{−1.03}).

### F7 — Numerical claims contradicted by their own stored data (subagent audit)

- **Resolvent rate m^{−1.2}** (Thm 99.1, "4 points"): stored deviations
  0.3586, 0.0868, 0.0371, 0.0379 at m = 9, 105, 336, 837; the fitted
  slope is ≈ m^{−0.6}, and the last two points show no decay.  The
  m^{−1.2} claim is not derivable from the artifact.
- **Third GOE spacing design (N=95419, m₊=837, "KS PASS")**: the
  available N=95419 artifact records a *rejected* full-coset result;
  no passing artifact for the desymmetrised coset exists.  The honest
  count is **two** passing designs (N=3571, N=19489), not three.
- M1/δ artifacts (`artifacts/r95/twist_decomposition_exact.json`,
  `artifacts/r93/...`) are missing; several `artifacts/rXX/...` paths
  cited in papers are dangling.

### F8 — Code defects found by re-execution

- `code/large_m/third_calibration.py`: the F1 indexing bug (class-1).
- `code/verification/word_trace_algebra.py` (R91.15 draft): crashes
  (`word ('V','V') unresolved`); its reduction rules R·W = R, E·R = R,
  R·E = R are numerically false (errors √2, 1, 1).  Superseded by the
  correct `word_trace_proof.py` engine (R91.17) — and by the independent
  check in `r108c_arcsine_thmB.py`, which verifies Thm 91.5 exactly —
  but the broken file should be quarantined.
- `code/theorems/sp4_g0_probe.py`: bracketing bug at line 123
  (`float(np.abs(diag) ** 2).sum()` — the `.sum()` is applied to a
  float, not the array); crashes after the covariance check.
- Path fragility: scripts compute ROOT and expect `src/` + `artifacts/`
  (the pre-R82 layout); the tree now has `code/` + `data/`.  Requires
  symlinks to run; several scripts write artifacts into `code/artifacts/`.

## C. What the k=4 layer actually reduces to (the corrected statement)

Let S be the annihilator coset (characters trivial on H, \|S\| = m) and
A_{ψ₁ψ₂}(d) the twisted fiber sums (diagonal key included at d = 0).

1. **Exact algebra (true):** B(t) = (1/m²) Σ_{ψ∈S²} (A_ψ ⋆ A_ψ)(t),
   and E_c = Σ_t B(t)² — but the expansion of E_c contains **all**
   cross terms Σ_{ψ≠ψ'} Σ_t (A_ψ⋆A_ψ)(t)(A_{ψ'}⋆A_{ψ'})(t).
2. **Trivial pair (true):** E_triv = E_unc exactly (measured equal at
   all three designs).
3. **Per-fiber Weil (true with carve-out):** \|A_ψ(d)\| ≤ 4√N for
   nontrivial ψ and d ≠ 0 (degree count D ≤ 4, bound 3√N; measured max
   ratio ≤ 0.52 across the sweep).
4. **Per-pair energies (true, vacuous):** E_ψ ≤ 256N⁵ provable;
   measured ≤ 0.3N⁵ — never the obstacle.
5. **The open problem (new, sharp; decomposed in R108f):** bound
   Cross := m⁴E_c − E_unc − Σ_{ψ≠11} E_ψ.  The block decomposition
   (r108e) localises it: the (H,H)-stratum (0.03% of key mass) carries
   ~76–100% of the deviation; flattening the diagonal-key spike removes
   60–72% of δ.  Hence δ = δ_explicit (closed form) + δ_remainder, with
   δ_remainder ≤ 0.3% for K ≥ 40 (measured across 16 designs; see
   docs/CROSS_TERM_LAW_R108.md).  The remaining analytic estimate is the
   distributed remainder in the coset-stratum frame.
6. **Desymmetrisation observation (new, BGS-relevant):** at N=3571 the
   H₊ = H·⟨−1⟩-coupled half-coset energy has δ(half) = +1.22% vs
   δ(full) = +17.65%; at N=199, +0.58% vs +6.45%.  The parity-restricted
   coupling is far closer to its uncoupled baseline.  Which coupling
   (H₊-even or ψ₀-twisted odd coset) models the parity-odd sector is
   measured in the sweep.
7. **Directly BGS-relevant measured law:** the relative cross-q
   fluctuation of the coset fourth moment satisfies
   rel₄ · m ∈ [2.0, 2.4] across all 16 sweep designs
   (m ∈ [4, 210], K ∈ [11, 307]) — the 1/m decay the local-law input
   needs, measured exactly.

## D. Status changes required (retraction cascade)

1. M1 / "H3 k=4 + M1 δ = o(1): PROVEN" → **RETRACTED as a proof**;
   replaced by: exact identity + flatness + per-fiber Weil (carve-out
   version) PROVEN; δ-control OPEN (cross terms).
2. Thm `thm:delta` (`cat_map_bgs_main.tex`), the abstract of
   `bgs_complete_paper.tex`, and `mobius_fiber_theorem.tex`: correct the
   N=3571 numbers, remove the 16-constant and the o(1)-at-fixed-K claim,
   restate the open cross-term problem.  [DONE in R108 for main paper
   and mobius note; bgs_complete pending.]
3. Thm 99.1 (resolvent m^{−1.2}) → downgrade to "rate unstable; stored
   data fit ≈ m^{−0.6}; last two points flat".
4. GOE spacing "three designs" → two designs (N=95419 unsupported).
5. `third_calibration.py` → mark RETRACTED (R93.2), fix the indexing
   bug in place with a pointer to R108.
6. `word_trace_algebra.py` → quarantine (superseded by
   `word_trace_proof.py` + R108c independent check).
7. `sp4_g0_probe.py` → fix the bracketing bug.
8. Folder hygiene: durable `artifacts/` mapping; referee scripts and
   outputs under `code/referee/`, `data/referee/`.

## E. What remains a genuine path to BGS in this family

Unchanged in substance from `docs/research_goals.md`, but with the k=4
layer re-opened and correctly posed: the M3 (ESY assembly) write-up is
still "literature-standard given the inputs", but the inputs now must
include the cross-term bound (or a desymmetrised-sector variant in which
it is small — the sweep decides).  The exact layers (A, B, C, H, II,
91.5, k=2) plus the two-design GOE spacing/rigidity evidence stand.

*All numbers in this report are reproducible:*
`python3 code/referee/r108_k4_independent.py`,
`python3 code/referee/r108b_direct3571.py`,
`python3 code/referee/r108c_arcsine_thmB.py`,
`python3 code/referee/r108d_ksweep.py`
(artifacts in `data/referee/`).
