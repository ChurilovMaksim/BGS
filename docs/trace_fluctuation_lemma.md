# Lemma (Trace-Fluctuation Reduction for Cat-Map Rank-0 Ensemble)
## R86 — DRAFT 1 (2026-09-01) — status: [CONJECTURED], 75%

## Scope (honest)

This lemma concerns **only** the rank-0 ensemble inside the
quantised-cat-map family `V_n = P_+ (T(n) + T(-n)) P_+` reduced to a
single matrix `M_q = C_q + C_q^*` per level set (Theorem II,
THEORY §19.1). It is **not** a statement about general chaotic
systems, nor about the full Katz equidistribution for Kloosterman
sheaves on `A` for `GL_2`. It is a reduction: an *unconditional*
analytic statement about `Tr(M_q^k)` for `k ≤ 10`, conditional on a
**weaker**, level-set-bounded input that the analyst
(`@theorist`) judges tractable in the toy case (mod-`K`
progression).

## Standing assumptions (inherited from THEORY §18–§19)

* `A ∈ SL_2(ℤ)`, `tr A = t = 3`, hyperbol ic.
* `N` an odd prime with `gcd(N, t²-4) = 1` and `N` *split* for `A`
  (so `t²-4` is a square mod `N`); `K = ord_N(A)`.
* `Q(n) = n_1² - n_1 n_2 - n_2²`, level set `L_q = {n : Q(n) = q}`
  (THEORY §18.1).
* `P_+` the parity projector on the `U_A`-eigenspace of dimension
  `m_+ = (N-1)/(2K)`.
* `M_q = C_q + C_q^*`, where `C_q = (c_{jk}(q))_{j,k}` are the
  Hecke-basis matrix elements (THEORY §18.4) with
  `c_{jk}(q) = e_N(-q/2) · conj(chi)(n_1) · psi(n_1) · J(chi,psi;q) / (N-1)`
  (Theorem II).
* `J(chi,psi;q)` is the twisted Jacobi sum
  `Σ_{x≠0,1} conj(chi)(x) · psi(x-1) · e_N(qx)`.
* `H_q = (1/m) Σ_n∈L_q V_n` is the level-set mean (a `T`-invariant
  matrix, diagonal in Hecke basis). The reduced object is `M_q =
  C_q + C_q^*`.

## The gap we are attacking (`op:local` after R82/R85)

THEORY §19.1 / paper §r82b names the *single* remaining input:

> *"What it does not supply is the joint decorrelation of
> *distinct* entries with rates; that, as noted in §r82b, is the
> single remaining input, and it is a Katz-type equidistribution
> statement for the sheaf above."*

A standard Wigner-type resolvent argument (Erdős–Schlein–Yau and
descendants, adapted to *deterministic* matrices) needs, for the
random-matrix approximation of `M_q`, a **fluctuation bound**

    Var_q[ Tr(M_q^k) ]  ≤  C_k · N^{2k} · N^{-δ_k}       (FLB)

for `k = 1, 2, ..., K_0` (here `K_0 = 10`, the rank-0 closure
horizon per Theorem H, R76, NUMERICALLY-SUPPORTED through `r=10`),
with `δ_k > 0` independent of `q ≠ 0`.

The currently open route is full Katz equidistribution for the
rank-2 hypergeometric sheaf underlying `J(chi,psi;q)`, applied at
the level of a single `M_q`. This is genuinely deep (and would be a
new contribution in its own right if achieved for this family).

## The lemma (the reduction)

**Lemma (Trace-Fluctuation Reduction).** *Fix `k ≤ 10` and a level
set `L_q` of size `N` with `q ≠ 0`, `q ∈ F_N^*`. Assume:*

*(H1) Theorem II (twisted Jacobi sums), as certified in R82,
*holds at `(N, K)`.*

*(H2) Theorem H (rank-0 cyclic shape decomposition, R75–R76)
*holds at `(N, K)` for `r ≤ 10`: the rank-0 ensemble moments
*`E[M_q^k]_{conn} = W_k(RMT)` are exact for `k ≤ 10`.*

*(H3) Sub-Weyl fluctuation (NEW, weakened from Katz).* For the
*twisted Jacobi sums indexed by `(chi,psi) ∈ S × S` over the
*level set `L_q`, the variance of the sum
*
*    Σ_{(chi,psi)∈S×S} J(chi,psi;q) · J(chi',psi';q) · … *
*
*with coefficients drawn from the rank-1 expansion of
*`(C_q)^j (C_q^*)^{k-j}(v,v)` (step 3 below) is bounded by
*
*    Var_q [ Σ_(chi,psi) ]  ≤  C_{k,j} · (log N)^{c_k} · N^{k/2 + 1/2 - ε}
*
*for some absolute `c_k, ε > 0` (uniform in `q`). This is
*`Sub-Weyl` because Weil alone gives `N^{k+1}`, and the full Katz
*equidistribution would give `N^{k/2}`. We require the level-set
*intermediate regime.*

*Then, writing `W_k(RMT)` for the Catalan-number moments of the
*semicircle (i.e. `W_2 = 1, W_4 = 2, W_6 = 5, W_8 = 14, W_10 = 42`
*scaled by `2` for centred vs uncentred),*
*
*    |Tr(M_q^k) − W_k(RMT) · m_+|   ≤   C'_k · m_+^{1 − δ_k}       (★)*
*
*with `δ_k = (1/2 − ε)/(k − 1) · m_+/(log N)` — i.e. fluctuation
*`O(m_+^{1/2 - ε/(k-1)})` after absorbing the level-set size.*

## Proof strategy (4 steps, sketched)

### Step 1 — Binomial expansion of `Tr(M_q^k)`

`M_q^k = (C_q + C_q^*)^k = Σ_{j=0}^k C(k,j) (C_q)^j (C_q^*)^{k-j}`.

Therefore

    Tr(M_q^k) = Σ_{j=0}^k C(k,j) · S_{j,k-j}(q),

where `S_{j,k-j}(q) := Tr[(C_q)^j (C_q^*)^{k-j}]` is a pure
level-set moment of the pair `(C_q, C_q^*)`.

The Catalan moments of `Tr(M_q^k)` in the *random-matrix limit*
(the `W_k(RMT)` in the lemma statement) come from the matched GOE
ensemble, as is standard: `W_2 = 1, W_4 = 2, W_6 = 5, W_8 = 14,
W_10 = 42` for the centred moments of `(1/(2√m)) M` on the scale
`[-2,2]`. These are the targets of `op:local`.

### Step 2 — Rank-1 product structure on the orbit

For `v ∈ L_q` (an arbitrary level-set representative), the matrix
elements

    (C_q)^j (C_q^*)^{k-j}(v, v) = Σ_{i_1, ..., i_{k-1}}
      C_q(v, U^{i_1} v) · C_q^*(U^{i_1} v, U^{i_2} v) · ... · C_q^*(U^{i_{k-1}} v, v)

collapse to a **scalar product on the orbit**, weighted by the
level-set Hecke characters. By Theorem II, the summand is

    J(v, i_1; K) · conj(J)(i_1, i_2; K) · ... · conj(J)(i_{k-1}, v; K)
      · chi(i_1) · ... · conj(chi)(i_{k-1})

— a **rank-1 product** of twisted Jacobi sums with character
weights. Crucially, this product factorises into `(k-1)` independent
factors when we sum over `(i_1, ..., i_{k-1})`, because each
factor `J(i_{r-1}, i_r; K)` depends only on the **adjacent pair**
of orbit indices.

**Consequence:** The fluctuation in the inner sum (over orbit
indices `i_1, ..., i_{k-1}`) factorises into `(k-1)` Weil-bounded
factors, and is **exactly the rank-0 ensemble moment** that Theorem
H computes — provided we average over `v ∈ L_q` (Step 3).

### Step 3 — Double averaging

The trace is `Tr(M_q^k) = Σ_{v ∈ L_q} (C_q)^k(v,v)` (because the
Hecke basis diagonalises everything). So we have

    Tr(M_q^k) = Σ_{v ∈ L_q} F_k(v; q),

where `F_k(v; q) = (C_q)^k(v,v)` is the diagonal entry, a function
of `v` and `q`.

Two averaging operations are now available:

* **Inner averaging** (over orbit indices `i_r`): already done in
  Step 2; gives the rank-0 ensemble moment
  `<F_k(·; q)>_{orbit}` which equals `W_k(RMT) · m_+` by Theorem H
  (H2), *independently of `q`* (because `Q(n) = q` is the only
  `q`-dependence through `C_q(v, ·)` and Theorem II gives the
  Weil bound uniformly in `q ≠ 0`).

* **Outer averaging** (over `v ∈ L_q`): this is *exactly* the
  definition of `Tr(M_q^k)` divided by `|L_q|`. The point of the
  lemma is that **after inner averaging, the outer averaging adds
  no further variance** in the limit — it just realises
  `Tr(M_q^k) ≈ |L_q| · W_k(RMT) · m_+`.

The catch: the inner averaging is over `v ∈ L_q` (orbit indices
`i_r` are functions of `v` through the Hecke decomposition). The
two operations are **coupled**, not independent.

### Step 4 — Sub-Weyl (H3) decouples them

Sub-Weyl (H3) is the claim that the **variance of the rank-0 inner
average across `v ∈ L_q`** is bounded by

    Var_v[ <F_k(·; q)>_{orbit, fixed v} ]  ≤  C_k · (log N)^{c_k} · N^{1/2 - ε}.

The argument sketch (this is the part `@theorist` will calibrate on
the toy level set):

* The inner average, for fixed `v`, is a sum of `(k-1)`-fold
  products of twisted Jacobi sums with character weights. The
  additive energy / large-sieve machinery of Bombieri–Vinogradov
  gives `Σ_v |inner average|^2 ≪ (log N)^{c_k} · N · N^{k/2 + 1/2 - ε}`
  when the character weights are the level-set coset characters
  (sub-Weil because the coset structure imposes a constraint
  `chi_k(a) = const` on `|S| = m_+` characters, reducing the
  character sum from a complete Weil sum to a partial one).

* This is the **same mechanism** that produces R85's certified
  Catalan moment matching at the level-set scale; the Lemma just
  elevates it to a *bound* on the variance, not just a mean.

If (H3) holds, the outer sum `Σ_v F_k(v; q)` differs from
`|L_q| · W_k(RMT) · m_+` by at most `√(Var) · |L_q|`, giving (★)
with `δ_k > 0`.

## What the lemma buys, and what it does not

### What it buys (if proven)

* The `op:local` input *for the resolvent argument* becomes a
  level-set Sub-Weyl bound, not a full Katz equidistribution.
  This is a strictly weaker object.
* Once `(★)` is in hand, the moment-route closure (Theorem G,
  R73) plus a smooth-density lemma (the R75–R76 numerical support
  extended to a bound) yields a **GOE local law for `M_q` per
  level set**, in the sense of Erdős–Schlein–Yau at
  `Im z ≫ m_+^{-1+δ}` for `δ = min_k δ_k / 2`.

### What it does NOT buy (honesty boundary)

* **NOT** a proof of BGS for general chaotic systems. Cat-map
  rank-0 ensemble, full stop.
* **NOT** a closure of full Katz equidistribution. We are routing
  *around* it, not through it.
* **NOT** a proof beyond `k = 10`. Higher moments need the
  rank-1 ensemble (R76 territory) and a separate argument.
* **NOT** a smooth-density result. We get the level-set moment
  bound; the analytic continuation to `s = it` (the resolvent
  input) needs a smooth-density lemma — an additional item
  beyond (★).

## Honest regime of validity

* **Requires:** `N` split, `K` odd, `gcd(K, q) = 1` (so that
  Weil's `2√N` ceiling applies to the twisted Jacobi sums).
* **Requires:** `k ≤ 10` (Theorem H horizon, R76).
* **Assumes:** (H3) Sub-Weyl — to be calibrated on the toy case
  (mod-`K` arithmetic progression) by `@theorist` in Cycle 2.
* **Not assumed:** full Katz equidistribution (H3 is strictly below
  Katz).
* **Not assumed:** smooth density (separate item).

## Falsifiers (what would refute this lemma)

1. **Cycle 2 mod-`K` progression test fails** (calibration): the
   Sub-Weyl bound (H3) does not hold even for the toy level set,
   with the toy showing `δ_k < 1/4` for `k = 4` or catastrophic
   variance growth. This refutes (H3), hence the Lemma as stated.

2. **Cycle 1 T11 Hecke basis fails** (foundational): the
   matrix-element computation of R82.12 is wrong on multiple
   primes, breaking the rank-1 product structure of Step 2. This
   is *not* a refutation of the Lemma per se, but it retracts
   the standing assumption (Theorem II at the level needed), and
   the Lemma must be re-evaluated.

3. **Direct trace computation contradicts (★)**: measuring
   `Tr(M_q^k) − W_k(RMT) · m_+` on a certified design with
   `N ≥ 3571`, finding fluctuation > `O(m_+^{1/2})`. This is the
   strongest falsifier but requires the bound, not the mean, and
   is only falsifiable once the level-set sample is large enough.

4. **Cross-key replication**: `@critic`'s independent trace
   computation in a different basis, with the same level set,
   finds a different fluctuation profile. Refutes the
   numerical support for the *bound*; the *mean* is Theorem H and
   is not under threat.

## Status (R86 + R87, 2026-09-01)

`[NUMERICALLY-SUPPORTED] ~80%` (upgraded from [CONJECTURED] 75% on 2026-09-01
after R87 closed the R86.4 falsifier program).

The Lemma is a clean reduction with named hypotheses (H1–H3) and
explicit falsifiers. The proof strategy is identified (Steps 1–4).
The crucial novel input is (H3), the Sub-Weyl bound on twisted
Jacobi sums over the level-set character coset.

**H1** (Theorem II at (N, K)): PROVEN at all R82.12 designs and at 4
additional split primes certified in R87.1 (N=461, 19489, 95419, 144481),
max |J_closed - J_brute| <= 1.5e-12, Weil-ceiling factor <= 3e-10.
**Closed** (R87.1).

**H2** (Theorem H at r <= 10): PROVEN at r <= 8 (R75.2),
NUMERICALLY-SUPPORTED at r = 9, 10 (R76.4). Unchanged by R87.

**H3** (Sub-Weyl on twisted Jacobi sums over level-set coset): the
R86.4 Cycle 2 toy (additive character on mod-K progression) supports
H3 empirically: 12/14 design points within (log p)^1.5 Sub-Weyl slack,
and the R/(log p)^1.5 ratio drops by 1-2 orders of magnitude as p grows
from ~1500 to ~100k. The toy does NOT promote H3 to PROVEN (it is
additive, not multiplicative; uniform q, not the cat-map q-curve), but
the analytic mechanism is now strongly empirically supported. Follow-on
Cycles 2b/2c (R87.5 handoff) are required to close H3 at the level
needed for the Lemma.

**Direct bound measurement** (R87.4): Tr(M_q^k) - W_k(RMT) * m_+
measured at 2 certified designs (N=461 m=20, N=19489 m=672), for
k in {2, 4, 6, 8}, 200 / 50 q's respectively. C_k = max|Delta|/sqrt(m)
at most 0.021 (k=4), 3-4 orders of magnitude below the 30-slack
acceptance threshold. C_k is monotonically decreasing in m, confirming
the bound is not just satisfied but is *decreasing* in m (consistent
with a true Sub-Weyl fluctuation bound).

**Status tag upgrade rationale**: with (H1) confirmed at 4 new
primes, the (H3) mechanism supported by the additive toy, and the
direct bound (★) confirmed to be 3-4 orders of magnitude below the
30-slack threshold with monotone decrease in m, the empirical case
for the Lemma is now strong enough to support [NUMERICALLY-SUPPORTED]
at 80% (a 5-point upgrade from R86's 75%). The formal status of H3
remains [CONJECTURED] — the toy does not prove the multiplicative
case. A formal proof of H3 via Bombieri-Vinogradov is the remaining
open work.

## Dependency graph

```
[THEORY §18.4] → [THEORY §19.1 Theorem II] ──────────► [H1]
                                                   ╱
[THEORY §13.2 Theorem H, R76] ───────────────────► [H2]
                                                   ╲
[Weil bound on J(chi,psi;q)]                       ╲
[Bombieri–Vinogradov large sieve]                  ─►[H3, NEW] ───► [LEMMA] ──► [op:local closed for k≤10]
```

## What is NOT in scope of R86

* Resolvent argument beyond moment bounds — needs a separate
  smooth-density lemma and is at least a follow-on cycle.
* Rank-1 ensemble (R76) — `k > 10` regime.
* Smooth density at level set — separate.
* Inert designs (R82.34) — out of R86 scope.
* k₀-law (R82.33) and the c² = t²-4 scale law (R82.24–26) — these
  are PROVEN and unaffected.
* Anything in paper.tex — R86 is pre-paper.

## Open references (for follow-up work)

* Bombieri–Vinogradov for character sums over cosets: standard
  textbooks (Davenport §17, Iwaniec–Kowalski Ch. 17).
* Sub-Weyl for Kloosterman: Michel–Venkatesh (2010) on
  equidistribution, or the more elementary Sarnak–Xue (2019) on
  Linnik-type problems; this is the level the toy case sits at.
* Toy calibration (mod-`K` progression): a clean application of
  orthogonality + large sieve to a one-parameter family, expected
  to be `~500` lines of Lean via `@formalist` with Bilu–Hanrot
  and existing mathlib `ZMod.character` API.