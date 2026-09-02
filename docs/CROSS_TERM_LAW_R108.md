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

## 5. The exact pair-type decomposition (R108g/R108h — new theorem-level result)

**Theorem (exact, machine-verified to 0.00e+00 at every design).**
Splitting the H-coupled key pairs by type — (diagonal,diagonal),
(diagonal,off)+(off,diag), (off,off) — gives the identity

    B(t) = (N−2)² δ_{t=0} + 2(N−2)·p_H(t) + B_off(t),

with p_H(t) = #{off-keys at difference t with u,v ∈ H} (a K²-sized
explicit table) and B_off the coupled amplitude of the diagonal-free
system.  Consequently

    E_c = (N−2)⁴ + 2(N−2)²·B_off(0) + 4(N−2)²·Σp_H²
          + 4(N−2)·Σ_t p_H·B_off + E_c^off.

**Conceptual mechanism (new).**  The diagonal key's contribution to
every twisted fiber sum is (N−2)·ψ(1,1) = N−2 — twist-INVARIANT.  It
therefore survives the annihilator averaging at full weight in E_c,
while the flat background is suppressed by m⁴ in the baseline
E_unc/m⁴.  The measured δ is dominated by this
unsuppressed-vs-suppressed mismatch (plus the spike×background
coherence), not by a mysterious irreducible cross-term sum.  The clean
object for the fluctuation problem is the diagonal-free system:

    δ_off := m⁴·E_c^off / E_unc^off − 1.

**Measured law (10-design sweep, exact computation):**

| N | K | δ_full | δ_off | ratio |
|---:|---:|---:|---:|---:|
| 199 | 11 | +6.45% | +1.42% | 4.5 |
| 3571 | 17 | +17.65% | +4.22% | 4.2 |
| 2161 | 40 | +0.45% | +0.09% | 5.0 |
| 6709 | 43 | +0.88% | +0.19% | 4.6 |
| 3001 | 50 | +0.26% | +0.05% | 5.2 |
| 2521 | 60 | +0.13% | +0.02% | 6.5 |
| 4969 | 92 | +0.05% | +0.01% | 5.0 |
| 5081 | 127 | +0.02% | +0.00% | — |
| 1511 | 151 | +0.01% | +0.00% | — |
| 1229 | 307 | +0.00% | +0.00% | — |

δ_off ≈ δ_full/4–5 uniformly, and inherits the ~K^{−3} decay in K.
Correction shares (m⁴E_c − E_unc): pure diagonal-spike term
(m⁴−1)(N−2)⁴ ≈ 0.14–0.24; off-system part ≈ 0.14–0.35; the remainder
is the spike×off interference structure.

**Cross structure of the off system (r108h, direct, verified).**  The
pairwise-Parseval bookkeeping passes its exact checks (E_triv =
E_unc_off and Σ_{ψ,ψ'}Cmat = m⁴E_off to ~1e−15).  At N=2161 the
within-bucket cross terms are 1.4e18 / 1.7e19 / 7.9e19
(low/mid/high-order buckets) and between-bucket ≈ 0.9e19 / 0.7e19 /
7.3e19 — the cross energy is distributed over the mid/high-order twist
pairs, NOT concentrated on low-order characters; the low-order bucket
(which contains the trivial pair) shows a near-total internal
cancellation.  This kills the "m = 210 has many low-order characters"
explanation of the K=17 anomaly: the anomaly is a distributed
correlation effect, not a low-order resonance.

**Structural fact (new observation).**  With a = (3+√5)/2 and
V₀=2, V₁=3, V_n = 3V_{n−1} − V_{n−2}:  V₁₁ − 2 = 39601 = **199²** and
V₁₇ − 2 = 12752041 = **3571²**.  Since a split prime p with ord_p(a) | q
satisfies p² | Norm(a^q − 1) = 2 − V_q, the designs N = 199 (K=11) and
N = 3571 (K=17) are the UNIQUE split primes for those orders —
small-K statistics are inherently single-design, and no "design scatter
at fixed K" test is possible for them.

## 6. The collective-field collapse and the exact dichotomy (R108i–m — new theorems)

### 6.1 Theorem (collective collapse; exact, machine-verified)

Let Y_p(ω) := Â_p(ω)², p = (j1,j2) ∈ Z_m², with Â_p the Fourier--DFT
amplitude of the off-diagonal system.  Since the fiber functions A_p
are real, Â_p(−ω) = conj(Â_p(ω)), hence

    Cmat[p,p'] = (1/N) Σ_ω Y_p(ω) · conj(Y_p'(ω)),

i.e. **Cmat is exactly the Gram matrix of the m² fields {Y_p}**
(Hermitian, PSD — measured |antisym|/|sym| = 0.000), and

    Σ_{p≠p'} Cmat[p,p'] = ‖Y_sum‖²/N − Σ_p E_p,
    Y_sum(ω) := Σ_p Â_p(ω)² = m² · DFT[B_off](ω).

The m⁴ cross terms are NOT independent objects: their sum is the
energy of ONE collective field — the transform of the coupled
amplitude B_off itself — minus the incoherent per-pair energies.
Verified: rel err 5.07e−14 (N=199), 2.87e−12 (N=2161).

### 6.2 Theorem (dichotomy of complete twisted sums; PROVED)

The off-key set is canonically
    S = (G∖{1})² ∖ {u = v},  G = F_N^*,
via the bijection (x,y) ↦ (u,v) = (x/y, (x−1)/(y−1)) with inverse
y = (1−v)/(u−v), x = u(1−v)/(u−v) (admissibility u,v ≠ 1 ⟺ x,y ≠ 1;
u ≠ v ⟺ x ≠ y); |S| = (N−2)(N−3).  Hence for every twist pair p:

    Â_p(0) = Σ_{(u,v)∈S} χ^{j1}(u) χ^{j2}(v)
           = A_{j1}·A_{j2} − D_{j1+j2},
    A_j := Σ_{G∖{1}} χ^j = −1 (j ≢ 0 mod m)  resp.  N−2 (j ≡ 0),
    D_ℓ := A_ℓ with ℓ ≡ j1+j2 mod m,

the "box minus diagonal" character-orthogonality computation.  The
five cases give, EXACTLY:

    Â_{(0,0)}(0)   = (N−2)(N−3)            [flat background]
    Â_p(0)         = −(N−3)  for the 3m−2 pairs with
                       j1 ≡ 0 ∨ j2 ≡ 0 ∨ j1+j2 ≡ 0 (mod m)
                       [one-sided twists; inverse composites]
    Â_p(0)         = +2      for all remaining m²−3m+2 pairs.

So the complete twisted sums obey an exact dichotomy: **giant (size
N−3, sign definite) exactly on the three "trivial-on-stratum"
families; otherwise exactly +2** — far stronger than the Weil scale
√N, with no arithmetic fluctuation at all.  Machine-verified twice
over: (a) FFT pipeline, 8/8 designs, all three checks PASS (giant
count exactly 3m−2; all giants exactly N−3; non-criterion max exactly
2); (b) independent one-stage 2D-DFT code path, worst rel err 1.1e−10.

### 6.3 Corollary (the DC sector is closed)

    Y_sum(0) = (N−2)²(N−3)² + (3m−3)(N−3)² + 4(m²−3m+2)   (exact),

a closed polynomial in (N, m); verified rel 0.00e+00 at all 8 designs
(direct and against the FFT pipeline).  Consequently the entire
unknown part of the k=4 off-system correction lives at **ω ≠ 0**:
the diagonal-frequency sector of the collective field is exactly
solved by §6.2.

### 6.4 Measured structure law of the ω ≠ 0 sector (r108k)

(The exploratory r108i/r108j runs that first measured these quantities
were lost to sandbox restarts; r108k re-measures and certifies all of
them — the numbers below are from the surviving r108k artifact.)

At N=199 → N=2161 (m=18 → 54): the Gram field becomes MORE coherent
with size — rank-1 energy share 0.956 → 0.995; mean pairwise cosine
0.859 → 0.926; fraction of cosines > 0.9: 0.57 → 0.87; constructive
alignment |ΣC|/ℓ₂ = 282 → 223 with pos-fraction 1.000 (all entries
non-negative); Perron profile α_p correlates with the pair energy E_p
at 0.963 → 0.988 and anti-correlates with |Â_p(0)| (−0.79).
Interpretation: the pair fields Y_p are nearly collinear with the
collective mode; the off-system correction is governed by the shape of
ONE field, not by m⁴ independent fluctuations.  The naive random-phase
model of the cross terms is refuted by measurement (constructive, not
cancelling).

### 6.5 What this does to the open problem

The k=4 δ-estimate now decomposes EXACTLY into: (i) the diagonal-spike
mismatch (§5, explicit); (ii) the DC sector of the collective field
(§6.3, closed polynomial); (iii) the ω ≠ 0 sector of ‖Y_sum‖² — the
sole remaining unknown, a single explicit Diophantine field (DFT of
the coupled amplitude B_off at nonzero frequencies), measured to be
quasi-rank-1 and constructive.  The analytic target is now: bound
Σ_{ω≠0}|Y_sum(ω)|² — one object, not m⁴.

## 7. The corrected theorem target (updated)

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
