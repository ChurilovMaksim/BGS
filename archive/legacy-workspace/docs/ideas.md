# BGS Grand Attack — IDEAS incubator

**Purpose.** Live notebook for sparks, sub-conjectures, cross-field analogies, and candidate new mathematics. Anything that doesn't yet have a place in `LEDGER` or `THEORY.md` goes here with timestamp + 1-line. Re-harvested at each stuck-protocol moment (≥3 unproductive cycles) and at every Ring boundary.

**Status tags (mirror main contract):** [SPARK] [SUB-CONJECTURED] [PARALLEL] [DEFERRED] [VOIDED].

**Promotion rule.** A SUB-CONJECTURE becomes a [CONJECTURED] in LEDGER only after at least one discriminating computation. VOIDED entries kept with mechanism-level reason (per `known_failure_modes` rule 1).

---

## Cycle 0 — RING 0 audit (2026-08-27)

### [RETIRED 2026-08-27, user request] Churilov 2026 drafts (3 files)
All three Churilov 2026 drafts in `user_drafts/` were REMOVED at
the user's instruction. The directory was deleted. Historical
triage (kept for traceability only):

- `Wigner_matrices.txt`: Churilov adaptive near-root truncation
  `W_n = σ_n H_n + S_n + A_n`. The CONCEPT (Churilov decomposition)
  informed RING 1.2 v3 design (R61, R62) but the load-bearing
  numerical claim was retracted in R61 as a fabrication.
  Status: framework reference only, no numerical transfer.
- `Lattice-Quotient_Spectra.txt`: heat-trace, mesh–time crossover.
  Never used in any deliverable.
- `Spectral_Selectors.txt`: quantum graphity, no BGS link.

### [SPARK] 2026-08-27 — 3 attack lines in RING 3 are not symmetric
Line A (trace formula) and Line B (RMT) are classical. Line C (new math) is where genuine originality lives. **Recommendation:** invest disproportionately in Line C, but only after Line A and B have produced at least a partial PROVEN result, so the gap Line C is filling is well-characterized. **Time budget:** RING 3 = 10-20 days; recommend 4d Line A, 4d Line B, 8-12d Line C.

### [SPARK] 2026-08-27 — cat map as "spine" of RING 3
Every RING 3 attack line should cross-validate against RING 1 cat map (per plan §3.4). This means each RING 3 result is "graded" by whether it gives the same numerical answer on cat map as our PROVEN machinery. This is a strong constraint and should prevent wild goose chases. **Concretely:** any candidate Line C tool must, on `p=3571, k=17, m=210`, return a spacing distribution within KS < 0.05 of GUE; if it doesn't, it's not yet a BGS tool, it's a competing framework.

### [SPARK] 2026-08-27 — Bourgain's implicit δ IS the lever
Plan §1.1 already documented: OSV Cor 2.9 explicit for `k ≥ p^{3/7+ε}`, Bourgain 2005 JAMS implicit down to `k ≥ p^ε` with non-explicit `δ`. **The single highest-value research move in RING 1** is to extract the Bourgain δ explicitly (or to prove it's fundamentally non-explicit). Even a `δ(ε) = c·ε^2` bound would close the entire cat-map local law for k above any `p^ε`. **Effort:** 1-2 days of literature deep dive. **Try first** before attempting Stepanov for H^3 (which is the alternative plan §1.1 lists).

### [SPARK] 2026-08-27 — R54 self-correction lesson (memory)
The durable lesson `drop-dont-tighten-loop` is critical. **Every** RING 1 result that undergoes 3+ tightening cycles in one session must be dropped, not tightened. **Add to daily discipline:** count edit cycles on each sub-claim; if ≥3, drop.

### [SUB-CONJECTURED] H-1 (RING 1.2): Real centraliser torus Hecke symmetrization achieves Wigner spacing at m ≥ 70
**Evidence:** R49-A showed entries Gaussian, correlations are the obstruction; R54 Haar pilot collapsed kurtosis +5.6 → -0.7; centraliser torus {xI+yA: x²+xyt+y²≡1} has order N∓1, structure that Haar cannot reproduce. **Probability:** ~40% (calibrated, dated). **Discriminator:** `src/hecke_resolvent_m210.py` on p=3571 (m=210), real centraliser, expect KS_GOE < 0.05. **Status:** pending RING 1.2 run.

### [SUB-CONJECTURED] H-2 (RING 1.1): Bourgain's δ is fundamentally non-explicit
**Evidence:** OSV Rem 2.11 verbatim "not explicit and not obvious how to get such an explicit result"; 20 years of follow-up (Bourgain–Garaev 2012, BCGLSS 2015) has not produced an explicit δ. **Probability:** ~70% the δ cannot be made explicit in current framework. **Discriminator:** if a paper published in 2024-2026 with explicit δ exists, find it via OpenAlex. Otherwise, the right move is to switch to a different attack (Stepanov for H^3, Katz-Monsky). **Status:** literature check pending in RING 1.1.

### [SUB-CONJECTURED] H-3 (RING 2.2): Anosov geodesic flow on constant-negative-curvature surface is the cleanest RING 2 test
**Evidence:** standard semi-classical analysis (Colin de Verdière, Zelditch, Jakobson) gives quantum ergodicity for Hecke eigenfunctions; Marklof's pair correlation for arithmetic groups is the closest pre-existing result; BGS for such flows is conjectured (Kurlberg–Marklof, Jakobson–Naud). **Probability:** ~30% the RING 2 cat-map machinery transfers cleanly. **Discriminator:** test whether `T_corr(L) = T_GOE(L)` (number variance at L=8,16) for the Laplacian on Γ\H. **Status:** defer to RING 2.

### [RETIRED 2026-08-27] H-4: Frame-holonomy heat trace as Wigner-Dyson skeleton

### [VOIDED] H-5: Schwartz–Zippel N_3 ≤ 2k
**Reason:** R54 self-correction (LEDGER:2951-2971) caught the degree-3 error and the H-membership false claim. The unconditional ceiling is N_3 ≤ 4k (bidegree-(2,2) → total degree 4). The 2k claim is **withdrawn** per memory lesson `drop-dont-tighten-loop`.

---

## How to use this file

- Every Ring gets a new section, named "Cycle N — RING X".
- New ideas go to the bottom of the active cycle.
- A cycle ends when: (a) the relevant sub-problem has a [CONJECTURED] entry in LEDGER, or (b) the cycle is closed as [VOIDED] with reason.
- A SUB-CONJECTURE's probability is re-calibrated at every cycle boundary.
- Cross-references to LEDGER entries: `LEDGER.md#<tag>`.
- Cross-references to drafts: `drafts/<filename>`.

## Cycle 1 — RING 1.1 discriminator (R58, R61)

### [VOIDED] H-2' (was ~85%): Bourgain δ is fundamentally non-explicit
**Reason:** R58 discriminator result (12 configs, |sum| ~ 2-7·k
growing with k) confirms that the Linn 2024 transfer does NOT
resolve op:tail below p^{3/7}. The OSV Rem 2.11 wall is real
for the H^3 subgroup case. H-2 promoted from 70% to 85% but is
now VOIDED as a "could be made explicit soon" hope; the honest
reading is that no published theorem gives a useful pointwise δ
for k < p^{3/7}, and the Linn transfer does not change that.
**Replacement:** the right path is Stepanov-for-H^3 (open) or
Deligne over µ_k sheaf (requires a non-trivial paper).

### [DEFERRED] H-6: Churilov-type decomposition applies to R_n (Hecke-centered residual)
**Evidence:** R61 corrected design. R49-A showed raw V_arth has
heavy outliers (kurt 5.9-9.3, max/std 3.8-5.0); the Hecke mean
A_n should remove the entry-correlation structure (R49-A
conclusion: "wall is entry-correlation, not marginal laws"),
leaving R_n as a Wigner-candidate. Churilov 2026 proves
W_n = σH + S + A for finite-variance Wigner with rank(S) = o_P(n).
**Probability:** ~50% the decomposition transfers. **Discriminator:**
v3 test on p=1009 m=36 first, then p=4481 m=70. **Status:** v3
written, run blocked on Julia compile time.

### [DEFERRED] H-7: Hecke mean A_n on R_n gives Wigner spacing at m=70
**Evidence:** R54 pilot at m≤17 with Haar surrogate showed
kurtosis collapse (raw +5.6 → Hecke -0.7) but inconclusive on
Wigner spacing (KS_GOE 0.13-0.35). The kurtosis-collapse is
the mechanism; the question is whether it survives to m=70 with
the REAL centraliser torus. **Probability:** ~30%. **Discriminator:**
v3 with struct-Hecke (block-diagonal). **Status:** deferred.


---

## Cycle R75 (2026-08-28) — after Theorem H

### [SPARK] phi-weights factor per shape (R75 handoff priority 1)
The cyclic shape sum is phi=1. The Weyl phases of R74.1 are products over the
word; within a fixed collected vector they should collapse to a single phase
per (shape, shift). If true, the phi-weighted excess = per-shape phase times
wc — and the phase average over shifts is itself a (short) Gauss sum.
Discriminator: compute the phase for the m-shape at r=5 and check the
ensemble 5th moment against direct simulation at a small design point.

### [SUB-CONJECTURED] S(R) = poly(R) C^R via beta-expansion automata
The multiples of x^2 - t x + 1 with bounded l1 norm are the relation language
of the beta-shift for the Pisot unit lambda. For quadratic Pisot the
relation/carry automaton on Z^2 should give S(R) <= poly(R) C^R with C
computable from the continued fraction of lambda' = 1/lambda. Census:
1,1,1,3,8,31,64,105 (R = 5..12). Promote to [CONJECTURED] after extracting C
from the automaton and fitting out-of-sample R = 13..16.

### [SPARK] the first genuinely modular relation M_r > 0
M_r = 0 for r <= 8. Counting heuristic: modular non-shapes with ||c||_1 = r
appear when (2r)^r K^r / (r!^2 N^2) ~ 1 — around r ~ 10-14 at K=17, N=3571.
Finding the first one calibrates the N^{-2} accident law of the ensemble
route. Cheap after vectorising the census (numpy support-sweep).

### [SPARK] ensemble odd moments as a QUE-adjacent observable
The 5th moment ~ 40 K^{-4} is nonzero and arithmetic (pure m-shape). The
ensemble odd moments thus form a clean arithmetic deviation profile from GUE
— possibly the same information content as a sub-QUE statement (matrix-element
distribution), but at moment level. Worth one paragraph in the next paper.

---

## Cycle 1 — run 80 (2026-08-29)

### [SPARK] op:Cdense — the growth constant of the m_t-multiple language
Dense shapes (width <= L1) of x^2-3x+1: S(R)^(1/R) = 2.078 (R=50), 2.179
(R=80), still rising; compositions bound C <= 3. The constant is the
Littlewood-multiple analogue of the Pisot minimal-weight growth constants
(Frougny-Steiner). Route: the co-reachable core of the R79 automaton is
empirically stabilising; its Perron value is the candidate C. Discriminator:
S(R)^(1/R) should flatten to the core Perron value once R >> core size.

### [SPARK] The coincidence-orbit moduli of Theorem H
The wrap coincidences (R80.2) parametrise shapes modulo
sig ~ +-x^a sig' mod (x^K - 1) with m_t | h (the wrapped suffix). The
quotient objects are shapes on the CYCLE Z/K — a finite ring analogue of
the quotient of the multiple-space by (x^K-1). Candidate structure: the
collision classes are exactly the m_t-multiples in Z[x]/(x^K - 1), i.e. the
cyclic module Z[lambda]/(lambda^K - 1) — count them with the SAME automaton
on a K-cycle. Would give a closed form for the collision excess and the
ceiling r*(K).

### [SPARK] J-weights as a transfer operator
Psi(y) = sum_walks prod J_|c| is the trace of a transfer operator on the
automaton; its dominant singularity in y is the analytic shadow of C_dense.
A joint Perron analysis in (state-space, y) might yield BOTH the growth
constant and the asymptotics of X_r(K) from one object.

### [SUB-CONJECTURED] The E-residue is O(m^{-1/2})-suppressed at large N
part1 (N=199): R5 ~ -223 comparable to I5; part2 (N=3571, m=210): the
certificate shows max|E| = 0.8 across ALL w — the eigenspace trace of a Weyl
operator is tiny at the real design. If Tr(T(w)P_lam) = O(m^{1/2} N^{-1/2+eps})
uniformly (a Kloosterman-type bound on the eigenspace trace), then R5 is
Gauss-suppressed and the ensemble moments are exactly rank-0 + kernel-slice
dominated. Discriminator: the R5 MC at N=3571 vs the N=199 value.
