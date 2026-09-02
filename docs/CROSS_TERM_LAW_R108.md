# CROSS-TERM LAW R108 — The corrected k=4 layer: measured laws, mechanism, and the decomposition

**Run:** R108 (2026-09-02).  **Artifacts:** `data/referee/r108d_ksweep.json`
(16 designs), `data/referee/r108e_blocks.json` (block decomposition),
`data/referee/r108f_extraction.json` (extraction test).  **Scripts:**
`code/referee/r108d_ksweep.py`, `r108e_blocks.py`, `r108f_extraction.py`.
Companion referee report: `docs/REVIEW_R108.md`.

This note records the NEW measured laws that replace the retracted M1
story (`δ = o(1)`, `|δ| ≤ 16/K²`), and the decomposition that turns the
"unbounded cross terms" into an explicit term plus a small remainder.

## 1. The design sweep (16 designs, K ∈ [11, 307], m ∈ [4, 210])

Exact computation (twist pipeline, validated digit-for-digit against
brute force at N=53; agreement with the independent direct enumeration
at N=3571: 4.3e−12).

| N | K | m | δ_full | δ_half | rel₄ | rel₄·m | max\|A\|/√N |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 199 | 11 | 18 | +6.45% | +0.58% | 0.1132 | 2.04 | 2.06 |
| 3571 | 17 | 210 | +17.65% | +1.22% | 0.0101 | 2.12 | 2.02 |
| 2161 | 40 | 54 | +0.45% | — | 0.0432 | 2.33 | 2.02 |
| 6709 | 43 | 156 | +0.88% | +0.07% | 0.0138 | 2.15 | 2.01 |
| 3001 | 50 | 60 | +0.26% | — | 0.0396 | 2.38 | 2.02 |
| 2521 | 60 | 42 | +0.13% | — | 0.0568 | 2.39 | 2.02 |
| 4481 | 64 | 70 | +0.15% | — | 0.0314 | 2.20 | 2.01 |
| 4021 | 67 | 60 | +0.12% | +0.01% | 0.0359 | 2.15 | 2.01 |
| 4969 | 92 | 54 | +0.05% | — | 0.0405 | 2.19 | 2.01 |
| 7879 | 101 | 78 | +0.05% | +0.01% | 0.0286 | 2.23 | 2.01 |
| 5081 | 127 | 40 | +0.02% | +0.00% | 0.0565 | 2.26 | 2.01 |
| 1511 | 151 | 10 | +0.01% | +0.00% | 0.2103 | 2.10 | 2.02 |
| 9521 | 170 | 56 | +0.01% | — | 0.0388 | 2.17 | 2.01 |
| 5881 | 196 | 30 | +0.01% | — | 0.0766 | 2.30 | 2.01 |
| 6871 | 229 | 30 | +0.00% | +0.00% | 0.0738 | 2.21 | 2.01 |
| 5281 | 264 | 20 | +0.00% | — | 0.1080 | 2.16 | 2.01 |
| 1229 | 307 | 4 | +0.00% | +0.00% | 0.4987 | 2.00 | 2.03 |

**Law 1 (the BGS-relevant fluctuation).** rel₄ · m ∈ [2.00, 2.39]
across every design — the relative cross-q fluctuation of the coset
fourth moment decays like ≈ 2.2/m.  This is the exact quantity the
trace-fluctuation lemma needs, and it is now measured exactly rather
than inferred from a wrong E_c chain.

**Law 2 (the correction).** δ_full falls steeply in K: ≈ K^{−3} for
K ≥ 40 (0.45% at K=40 → 0.00% at K ≥ 229), with small-K scatter
(+6.45% at K=11, +17.65% at K=17).  In the honest BGS regime
(K → ∞, K = o(N)) the measured correction vanishes rapidly.
(The fixed-K scaling of the retracted claim is impossible anyway:
finitely many split primes per order.)  Note: the corrected
δ(N=3571) = +17.65% refutes **both** envelopes ever stated in the
workspace — the papers' 16/K² = 5.5% and the artifacts'
16/m = 7.6% (m1_killer_test.json, g0_hypothesis.json) — which were
also mutually inconsistent laws.

**Law 3 (desymmetrisation).** The H₊ = H·⟨−1⟩-coupled half-coset δ is
5–15× smaller than the full-coset δ at the same design.  The
parity-restricted sector — the BGS-relevant one — is far closer to its
uncoupled baseline.

**Law 4 (per-fiber Weil margin).** max |A_ψ(d)|/√N ≈ 2.0 at every
design (nontrivial pairs, d ≠ 0) — consistent with the provable
(D−1)√N = 3√N with room; the c_w = 4 statement holds with ≥ 2× margin.

## 2. The mechanism (block decomposition, r108e)

Strata (coset classes of the key (u,v)) are grouped by the
inversion-stable flags u∈H, v∈H, u/v-in-same-coset.  Findings at
N=3571 (δ = +17.65%):

- The (H,H)-block — 0.03% of the key mass — carries E2-involvement
  (self + cross with the generic block) ≈ 5.1e14, i.e. **~76% of the
  total deviation** E_c − E_flat = 6.7e14.
- At N=199 the same block explains ≈ **100%** of the deviation
  (7.2e9 vs 7.0e9).
- The next most non-flat strata after (0,0) are the (c,−c) family
  (uv ∈ H) — an order of magnitude below.

## 3. The decomposition (extraction test, r108f)

Replacing the (0,0)-stratum profile by its flattened version (same
mass, uniform over d̄) — equivalently, flattening just the diagonal-key
spike of mass N−2 at d=0 (V2 ≈ V1 to 0.01%):

| N | K | δ true | δ after (H,H)/diagonal extraction | remainder |
|---:|---:|---:|---:|---:|
| 199 | 11 | +6.45% | +2.56% | 2.56% |
| 3571 | 17 | +17.65% | +4.89% | 4.89% |
| 2161 | 40 | +0.45% | +0.20% | 0.20% |
| 6709 | 43 | +0.88% | +0.30% | 0.30% |
| 5081 | 127 | +0.02% | +0.01% | 0.01% |
| 1229 | 307 | +0.00% | +0.00% | 0.00% |

Further flattening the (c,−c) family (V3) changes nothing beyond
~0.1–0.2%.

**Decomposition (measured).**
δ = δ_explicit + δ_remainder where
- δ_explicit is the diagonal-key artifact: the coupling concentrates
  the diagonal mass (N−2 at d=0) on the (H,H)-stratum — its
  self-interaction (N−2)²δ_{t=0} and its interaction with the flat
  background — while the uncoupled baseline E_unc/m⁴ spreads the same
  mass the way the pooled count c(d) does.  This term is explicitly
  computable in closed form from (N, K, H) (the H×H profile is a
  K²-sized table: p_H(d̄) = #{(u,v) ∈ (H\{1})², u≠v : d(u,v) = d̄}).
- δ_remainder is the distributed stratum-correlation term: measured
  2.56% (K=11), 4.89% (K=17), ≤ 0.3% for K ≥ 40, ~0 for K ≥ 127.

## 4. The corrected theorem target

**Candidate decomposition theorem.** Along split primes with
K = ord_N(a) → ∞:

  E_c = E_unc/m⁴ + E_expl(N,K) + Rem,   |Rem| ≤ E_unc/m⁴ · O(1/K^{3/2}),

with E_expl the closed-form diagonal/(H,H) term (computable; dominant
at small K), and Rem the distributed remainder (measured ≤ 0.3% for
K ≥ 40, decaying ~K^{−3}-ish; analytically open — the natural approach
is the coset-stratum profile frame with Weil/Deligne bounds per
stratum-pair interaction).

**What this buys.** The trace-fluctuation input for the GOE local law
does NOT need δ = o(1) at fixed K: the directly relevant rel₄ ≈ 2.2/m
is already measured exactly across the whole design range, and the
decomposition reduces the analytic gap to the Remainder estimate (plus
the closed-form E_expl write-up).  The honest M3 (ESY assembly) can be
written conditionally on |Rem| = O(E_unc/m⁴·K^{−3/2}), with the
condition measured to hold from K ≈ 40 upward.

**Next experiments (priority order).**
1. Derive E_expl in closed form and check it against the measured
   δ − δ_remainder at all 16 designs (should match to numerical
   precision — it is exact algebra once written).
2. Multi-design-per-K sampling in K ∈ {11, 17, 40} (all split primes
   with those orders — finitely many, all small) to separate the K-law
   from design scatter at small K.
3. Attack Rem in the stratum frame: per-stratum-pair interaction
   bounds (the profiles P_e are themselves character sums over coset
   strata — 2D hybrid sums; the Weil-per-stratum route gives the
   natural prior).
