
## RUN 82 (2026-08-30) — THEOREM I: THE OBSERVABLE FAMILY IS A ONE-PARAMETER
### ARITHMETIC CURVE.  op:dpbug RESOLVED (AND R81.6 PARTLY RETRACTED),
### THE R81.4 "COHERENT MODE" IDENTIFIED AND PUT IN CLOSED FORM

Triage: FRONTIER continuation.  Two fronts per the R81 handoff: op:dpbug /
op:Cdense (the counting layer) and op:local (the fluctuation layer).  The
second front produced the run's main result.

ENV: chat RU / work EN.  Python 3.13.6 (numpy, scipy, sympy), Julia 1.11.4 at
`C:\Users\churi\AppData\Local\Programs\Julia-1.11.4\bin\julia.exe` (the
`C:\Tools\julia` path recorded in older entries does NOT exist), Lean/lake
4.33.1 via elan, tectonic at `tools/bin/tectonic.exe`, 6 cores, 15.94 GB RAM
(6.6 GB free at start), 38 GB free disk.  A1-A4, A6 present; A5 (subagents)
not used this run; A4 available (arXiv API through Python; the harness
WebSearch tool is not available for this model — WebFetch and the arXiv API
are).  Degradation in effect: none beyond A5.

### R82.0 — WORKSPACE REPAIR [DONE]

* The workspace had been copied into itself twice: the research root sat at
  `Desktop/BGS/BGS/BGS/BGS/`.  Flattened to a single root `Desktop/BGS/`
  (14 top-level entries); `AGENTS.md` lifted with it.
* 52 Python files still carried the dead absolute roots
  `C:\Users\churi\Desktop\BGS[\BGS_portable_20260827\BGS]` (a pre-OneDrive
  layout and a deleted snapshot) — the R71 path repair had missed them
  because they were in `review/scripts/`, `src/archive/` and a handful of
  `src/` drivers.  Repaired to a `__file__`-relative `_BGS_ROOT` prelude
  (`src/maintenance/repair_paths_r82.py` + `fix_prelude_r82.py`, both
  idempotent, both with a post-repair `compile()` gate).  Two defects of the
  first pass were caught by that gate and fixed: a wrong nesting depth and a
  UTF-8 BOM pushed off byte 0.  `review/scripts/smoke_test_src.py`: 5/5 PASS.
* MISSING ARTIFACT [recorded, not repaired]: the Lean sources of R80.7
  (`bgs-lean/BgsTailBound.lean`) lived OUTSIDE the workspace at
  `C:/Users/churi/lean-projects/` — that directory no longer exists.  The
  R80.7 statement "the algebraic core of the automaton bound is
  machine-checked" therefore has NO retrievable artifact and is downgraded to
  [UNVERIFIED: artifact lost].  LESSON 82-E below.

### R82.1 — op:dpbug RESOLVED: the DENSE COUNT DP WAS CORRECT; the R81.6
### retraction of the dense series is itself RETRACTED [certified]

A rewritten DP (`src/r82_dp_lib.jl` = canonical library, drivers
`src/r82_dp_exact.jl`, `src/r82b_dp_push.jl`) removes both defects of the
r80/r81 implementation:

* DEAD STATE DIMENSION.  The old key was `(a, b, u, w)` where `w` = position
  of the last nonzero letter.  `w` is never read — the accepting record uses
  `w2 = p + 1`, the current position — so carrying it multiplied the cell
  count by O(R).  That, not a logical error, is what exhausted memory at
  large budgets.  Key here: `(a, b, u)`.
* FLOAT FILTER.  `|a + b*lambda| <= rem` was a Float64 comparison with an
  ad-hoc 1e-9 slack.  Replaced by exact integer arithmetic: with
  `lambda = (3 + sqrt 5)/2`, `a + b*lambda = ((2a + 3b) + b*sqrt 5)/2`, so the
  test is `|A + B sqrt 5| <= 2 rem` with `A = 2a + 3b`, `B = b`, decided by
  integer comparisons of `5B^2` against squares (`le_sqrt`).  No slack, no
  boundary ambiguity.
* SELF-CHECKS (LESSON 81-C, now built in): supermultiplicativity
  `N(R1+R2) >= N(R1)N(R2)` over ALL admissible pairs, both factors read from
  the SAME run; plus budget-independence of every row.

Results (`artifacts/r82/dp_exact.json`, log `dp_exact.log`):

    S_dense(R), R = 5..12:  1, 1, 1, 3, 8, 23, 44, 81
    S_dense(30)  = 301 160 711          (= R80.4, EXACT)
    S_dense(50)  = 7 639 873 992 151 089 (= R80.4's 7.64e15, EXACT)
    S(80)^(1/80) = 2.17936               (= R80.4's 2.1794)
    GLUE CHECK: PASS for all pairs R1 + R2 <= 56 (exact BigInt) and
                all pairs R1 + R2 <= 130 (Float64)
    BUDGET INDEPENDENCE: rmax = 40 and rmax = 56 agree on all 36 rows
    Float vs exact: max relative deviation 2.7e-16 on R <= 56

Cross-validation against the OTHER published census: the width-capped rows
`w <= 17` at L1 = 8..12 come out 3 / 8 / 37 / 68 / 111 — the R80.2
position-DP numbers to the last digit (that cross-check was run by two
methods in R80, so this is a third).

WHY R81.6 SAW A VIOLATION.  The R81.6 glue check was run on the FULL count
`S[R] = sum_w cnt[(w, R)]` of `src/r81e_dp_debug.jl`, where the width was
capped at `wmax = rmax + 1`.  Gluing two relations of widths up to 63 needs
width up to 126, which the `rmax = 124` run (cap 125) cannot represent, so
the "deficit" is the cap, not the count.  The dense series (`w <= R`) is
immune — gluing two dense relations gives `w1 + w2 <= R1 + R2` — and it
passes at every pair up to R = 130.  Consequently:

* RETRACTION OF A RETRACTION: R81.6's withdrawal of the dense S(R) rows is
  itself withdrawn.  The dense rows stand, now with a self-check the earlier
  runs lacked.  What survives of R81.6: the Int128 overflow at R >= 110 is
  real (S(110) ~ 2.0e38 > 2^127/2), so the R81.2 Int128 tail rows and their
  2.32 extrapolation stay VOID.  `op:dpbug` is CLOSED.
* NEW SANDWICH.  Fekete (R81.1) gives `C_dense = sup_R N(R)^{1/R}`, so every
  computed row is a rigorous lower bound:

      2.24970 <= C_dense <= 3        (from S(130), Float64 relative error
                                      < 1e-12; the upper bound is the signed-
                                      compositions bound, R80/THEORY 17.3)

  improving R81.6's surviving `2.1794 < C_dense <= 3`.  The model-based
  estimate remains withdrawn; `op:Cdense` (the VALUE) stays open, and the
  remaining honest statement is the sandwich plus the observed slow rise.

### R82.2 — THEOREM I (TORUS RIGIDITY OF THE OBSERVABLE FAMILY)
### [PROVEN; ingredient standard, consequence new to this programme;
### certified 15/15 at three designs]

Setting: `N` an odd prime, `gcd(N, t^2 - 4) = 1`, `A in SL_2(Z)` with
`tr A = t`, `K = ord_N(A)`, `P` the projector onto a `U_A`-eigenspace,
`P_+-` the parity blocks (Theorems C/D), and the family

    V_n = P_+ (T(n) + T(-n)) P_+,        n in (Z/N)^2 \ {0}.

Let `T` be the centraliser torus of `A` in `SL_2(Z/N)` — the group whose Weil
operators `U_g` are exactly the HECKE OPERATORS of Kurlberg-Rudnick
[KR2000] — and let

    Q(n) = n_1^2 - n_1 n_2 - n_2^2      (discriminant 5 = t^2 - 4 at t = 3)

be the `T`-invariant quadratic form.

THEOREM I.  (a) If `Q(n) = Q(n')` then `V_n` and `V_{n'}` are unitarily
equivalent; in fact `V_{n'} = U_g V_n U_g^*` for an explicit `g = aI + bA`
in `T`.  (b) Hence the family has at most `N` distinct spectra — one per
value of `Q` — instead of `(N^2-1)/K`.  (c) Each nonzero level set is a
single `T`-orbit carrying exactly `|T|/K = m` distinct `<A>`-orbits, and
`(N -+ 1) . m + |cone|/K = (N^2 - 1)/K`.

PROOF.  Identify `(Z/N)^2` with `R = (Z/N)[x]/(x^2 - tx + 1)` as a free
rank-one `R`-module; `Q` is (a scalar multiple of) the norm form of `R` and
`T` is its group of norm-one units, so `T` acts simply transitively on each
level set `{Q = q}`, `q != 0` (order `N - 1` in the split case, `N + 1`
inert; the certificates below verify the sizes exhaustively).  For `g in T`
the Weil operator satisfies the exact Egorov covariance
`U_g T(n) U_g^* = T(gn)` (the intertwining property of the Weil
representation of `SL_2(Z/N)` for odd `N`; in this programme certified for
`A` itself at 3e-14, T1/A1).  Since `g` commutes with `A`, `U_g` commutes
with `U_A` up to a scalar and therefore preserves every `U_A`-eigenspace;
`-I` is central, so `U_g` also preserves each parity block.  Applying
`U_g . U_g^*` to `P_+(T(n) + T(-n))P_+` gives `P_+(T(gn) + T(-gn))P_+`.  By
transitivity any `n'` with `Q(n') = Q(n)` is `gn` for some `g in T`.  []

CERTIFICATION (`src/r82f_torus_rigidity.py`,
`artifacts/r82/torus_rigidity.json`), at (N, K) = (199, 11), (3571, 17),
(9349, 19) — all three split, five certificates each, 15/15 PASS:

  C1  every nonzero level set has exactly `N - 1` points and the cone
      `{Q = 0}` has `2N - 2` (exhaustive enumeration of all `N^2` vectors);
  C2  the number of `<A>`-orbits inside one level set equals `|T|/K = m`
      (18 / 210 / 492) and the global identity of (c) holds exactly
      (3600 = 3600, 750120 = 750120, 4600200 = 4600200);
  C3  6 level sets x 8 DISTINCT orbits each: max deviation between full
      sorted spectra `2.4e-14 / 2.0e-13 / 3.3e-13`;
  C4  spectra for different `q` differ by 11-13 decades more than that;
  C5  the explicit torus element `g = aI + bA` with `det g = 1` and
      `g n_0 = n'`: 21/21 found at each design.

Two independent internal validations of the pipeline that carries this
(`src/r82d_orbit_invariant.py`): orbit invariance
`spec(V_n) = spec(V_{A^T n})` to 7.6e-14 / 1.2e-13, and a TWO-KEY value
check — `mu_4` recomputed through the EXACT `N x N` projector
`((1/K) sum_j lam^-j U^j)((1 + R)/2)` with no randomised eigenbasis and no
SVD: `1.85357709` vs `1.85357709`, `|diff| = 1.3e-14`, captured dimension
105 = `m_+`.

POSITIONING.  The ingredient is standard: the Hecke group and its action are
Kurlberg-Rudnick's [KR2000, chao-dyn/9901031]; that the Hecke group is the
norm-one torus and preserves `Q` is immediate there.  What is new here is the
consequence for THIS programme's observable ensemble — see R82.3 — which
R81.4/R81.5 had left open ("the arithmetic driver is open").

### R82.3 — COROLLARY: THE R81.4 "COHERENT ARITHMETIC MODE" IS THE
### ONE-PARAMETER CURVE, AND THE ENSEMBLE ROUTE HAS AN EXACT CEILING
### [PROVEN, given Theorem I]

R81.4 measured, over `A^T`-orbit representatives `n`, a bulk level-count
variance 1.8x (m+ = 105) to 4.2x (m+ = 246) the matched GOE variance, carried
by ONE coherent mode with positively correlated neighbour windows, while each
sample is internally GOE-rigid (R81.5 D1).  It read this as a new
phenomenon, "modulated universality", with the driver unknown.  Theorem I
settles it:

* the ensemble `{V_n}` is a deterministic ONE-PARAMETER curve `q -> V_q`
  sampled at `q = Q(n)`, each value repeated `m` times;
* therefore a single dominant fluctuation direction and positively
  correlated window counts are automatic, not phenomenological;
* the excess over GOE grows with `m` because the spread of the curve is
  O(1) in `m` while the GOE fluctuation decays (measured: `std(mu_4)` =
  0.38, 0.23, 0.21 at m+ = 9, 105, 246 versus GOE 0.26, 0.027, 0.011);
* an i.i.d.-GOE statement for `{V_n}` is FALSE for an exact and elementary
  reason, and the effective ensemble size is `N - 1`, not `(N^2-1)/K`.

CEILING ON THE FREQUENCY-ENSEMBLE ROUTE [the sharpened obstruction].  The
R74-R80 route averages moments over `n in (Z/N)^2`.  By Theorem I that
average is an average over `q in F_N^*` with each member repeated `m` times:
the `n`-average of any spectral functional is exactly its `q`-average.
Averaging over `n` therefore buys concentration in ONE arithmetic scalar
only; it cannot separate per-system behaviour, so it cannot substitute for a
per-system local law.  Together with Theorem G (the moment route is provably
closed) this closes the "average over the ensemble" escape route explicitly
rather than heuristically.

### R82.4 — THE MODULATION IN CLOSED FORM: A FIBONACCI FREQUENCY COMB
### [NUMERICALLY-SUPPORTED, exhaustive over all level sets]

With `q` the right parameter the whole curve is computable exhaustively
(`src/r82g_q_curve.py`, `artifacts/r82/q_curve_N{199,3571}.npz`): all 198
and all 3570 level sets, no sampling.

    N = 3571, K = 17, m+ = 105:
      Tr(V_q^2)/m+  in [0.11098, 0.12393], mean 0.117600, rel spread 1.22%
                    and  N/(K^2 m+) = 0.117658  -- the mean is the arithmetic
                    value to 4 digits [an exact identity worth proving]
      mu_4(q)       in [1.2246, 2.8573], mean 1.9694, std 0.2350
      mu_6(q)       mean 5.084 (semicircle 5), std 0.55

Additive-Fourier analysis in `q` of the RAW central traces (linear in the
word sum, unlike the normalised moments) shows a SPARSE spectrum, and the
dominant frequencies are exactly the power coefficients of `A`:  writing
`A^j = u_j I + v_j A` (so `u_j = -v_{j-1}` and `v_j = 1, 3, 8, 21, 55, 144,
377, 987, 2584, ...` — the even-index Fibonacci numbers for `t = 3`),

    16 frequencies carry 90% of the variance of Tr(V_q^4) and Tr(V_q^6),
    namely  a = +- v_j,  j = 1..8   (0.4% of the 3570 available modes),
    with nearly equal masses 0.052-0.068 each,

and a least-squares fit on exactly those `(K-1)/2 = 8` frequency pairs
(17 parameters, 3570 data points) gives

    Tr(V_q^4):  R^2 = 0.9426        mu_4(q):  R^2 = 0.98655
    Tr(V_q^6):  R^2 = 0.9276

(`artifacts/r82/raw_trace_dft.json`, `qfit_R2.json`).  Enlarging the
frequency set (adding `u_j`, doubles, pairwise sums and differences: 71
frequencies, 143 parameters) moves `R^2` only to 0.9472 / 0.9872 — the comb
is saturated, and the residue is a different, smaller component.  So:

    mu_4(q) = c_0 + sum_{j=1}^{(K-1)/2} 2 Re( alpha_j e_N(v_j q) ) + eps,
    with  var(eps)/var(mu_4) = 1.3%.

This is the arithmetic driver the R81 handoff asked for, in closed form up to
the coefficients `alpha_j`.  Mechanism consistent with the programme's own
Lemma F: each word of the trace expansion contributes a Weil phase
`w^{Q_J(v)}` with `v = sum eps_i A^{J_i} n`; the `T`-invariant part of a
quadratic form in `n` is a multiple of `Q(n) = q`, and the multipliers
available from products of powers of `A` are exactly the `v_j`.

RELATION TO THE LITERATURE [read, not skimmed].  Kurlberg-Rudnick
[math/0302277] conjecture that the normalised matrix elements of the
DESYMMETRISED quantum cat map are distributed as a weighted sum of traces of
independent `SU(2)` matrices — explicitly NOT Gaussian — and verify the 2nd
and 4th moments; Kurlberg-Rosenzweig-Rudnick [math/0701685] and Rosenzweig
[0909.1410] compute variances and higher moments of the same objects in short
windows.  A weighted sum of `SU(2)` traces is a weighted sum of terms
`2 cos theta_j`; the comb above is a finite-`N` realisation of exactly that
shape with `(K-1)/2` terms and phases `v_j q / N`.  This programme's R73.2
"Hecke dichotomy" (diagonal Sato-Tate, off-diagonal complex Gaussian) is the
same circle of facts.  Nothing here contradicts those papers; R82.4 adds the
explicit finite-`N` frequency set for the compressed-observable family.

### R82.5 — THE MEASUREMENT THAT STARTED IT: THE EXCESS IS EVEN-MODE ONLY
### [NUMERICALLY-SUPPORTED, matched GOE reference at 4x sample count]

`src/r82_shape_modes.py` (`artifacts/r82/shape_modes.json`) decomposes the
R81.4 excess in the basis that diagonalises linear eigenvalue statistics of a
beta-ensemble, `L_k(n) = sum_i T_k(lambda_i/sqrt 2)`:

    Var_arith / Var_GOE      k =  3     4     5     6     7     8     9    10
      m+ = 105 (N = 3571)         1.03  80.7  1.59  71.4  2.81  78.1  5.8  99.9
      m+ = 246 (N = 9349)         0.53  375   2.89  306   5.21  302  10.8  352
      Haar control (same ops)     0.42  0.45  0.38  0.44  0.31  0.38  0.26 0.32

identically for the even/odd spectral moments (`mu_4, mu_6, mu_8` ratios
80.7 / 77.6 / 77.3 at m+ = 105 and 375 / 348 / 327 at m+ = 246; `mu_3, mu_5,
mu_7` ratios 1.0 / 1.2 / 1.7).  Projecting the bulk count vectors on the low
modes and removing that component drops the count-variance ratio from 1.89 to
1.32 (k <= 4) and 1.12 (k <= 8) at m+ = 105, and from 3.82 to 2.09 and 1.46
at m+ = 246: the excess is carried by finitely many low even modes, as
Theorem I demands (a one-parameter family of symmetric densities).

### R82.6 — HYPOTHESES KILLED THIS RUN [recorded so later runs do not
### re-spend on them]

* "the coherent mode is a global width (second-moment) fluctuation" —
  DEAD ON ARRIVAL: the R81 pipeline already normalises every sample to unit
  second moment (r81_local_law_pilot.py lines 120-122), and `Tr(V_q^2)` is
  n-independent to 1.2% anyway.
* H1 "the macroscopic law is arcsine, not semicircle" — REFUTED: `mu_4`
  means 1.92 / 1.95 / 1.97 at the three designs versus semicircle 2 and
  arcsine 1.5; `mu_6` 4.65 / 4.81 / 5.08 versus 5 and 2.5.  The leading
  word-count estimate that suggested 3/2 double-counts the parity block and
  is wrong; the density IS semicircular in the mean.
* H4 "extra mod-N resonances drive the fluctuation" — REFUTED at the real
  design: the exact count of `(eps, J)` with `M n = 0 mod N`, `M != 0`, has
  ZERO extra solutions over 256 orbits at (3571, 17) while `std(mu_4)` is
  0.23.  Resonances DO matter at the toy designs (mean extra 2.6 at N = 199,
  0.75 at N = 9349, `corr(C_4, mu_4) = 0.63` at both) and they are what makes
  those two designs heavy-tailed (kurtosis 8.0 and 20.9 versus 2.73 at
  N = 3571).  The pairing prediction `C_4 = 6(2K - 1)` is EXACT at all three
  designs (126, 198, 222).
* P6/P7 "the modulation is a sparse MULTIPLICATIVE character sum" —
  REFUTED (top-10 multiplicative modes carry 2.5% of the variance); the
  structure is purely additive (R82.4).
* P8 "a hidden scaling symmetry `q -> cq`" — REFUTED (best deviation ~1.0 on
  a quantity of spread 0.23).
* H5 "`mu_4` is a function of `Q` alone" — CONFIRMED, and then upgraded to
  Theorem I: the ANOVA gave within-level variance 0.00000 against total
  0.0535 (3571) and 0.0633 (9349).
* H6 "the modulation depends on the quadratic character `chi(Q)`" — no
  effect (z = 0.29 / 0.40).

### LESSONS (run 82)

* LESSON 82-A: a retraction needs the same standard of evidence as a claim.
  R81.6 retracted a correct series because the CHECK compared counts computed
  under two different width caps.  A self-check must read both sides of an
  inequality from the same run with the same truncations.
* LESSON 82-B: before modelling a state space, ask which fields of the DP key
  are ever READ.  The `w` field cost a factor O(R) in memory and produced the
  "memory exhaustion" that was then misdiagnosed as a state-space explosion.
* LESSON 82-C: when an ensemble shows one dominant coherent fluctuation mode,
  test first whether the ensemble is a curve.  The exact symmetry group of
  the family (here the Hecke torus) bounds the number of distinct members;
  that bound is cheaper to check than any mechanism hunt, and it dissolved a
  ~75%-confidence "new phenomenon".
* LESSON 82-D: analyse the LINEAR quantity.  `Tr(V^r)` is a word sum and has
  a sparse Fourier transform in the right parameter; the normalised moment
  `mu_r`, being a ratio, does not (and `mu_4`'s sparsity is an accident of
  `Tr(V^2)` being nearly constant).  Sparsity tests belong on the raw
  functional.
* LESSON 82-E: load-bearing artifacts must live INSIDE the workspace.  The
  R80.7 Lean sources were kept at `C:/Users/churi/lean-projects/` and are
  gone; the claim they supported is now unverifiable.  The Lean project for
  this programme is re-created at `formal/` inside the workspace.

### RUN 82 HANDOFF

* CLOSED this run: `op:dpbug` (with a counter-retraction of R81.6's dense
  rows); the identification of the R81.4 driver (Theorem I + the Fibonacci
  comb); the R81.5 "arithmetic driver open" item.
* OPEN, by expected value:
  1. `op:local` in its now-correct form: for a FIXED `q`, prove GOE local
     statistics for `V_q`.  Theorem I removes the ensemble as a tool, so this
     is a genuine single-matrix local law.  Concrete entry point: in the
     Hecke basis `{f_j}` (the `T`-character basis) equivariance forces
     `<f_j|T(n)|f_k> = c_{jk} . (chi_j chi_k^{-1})(g_n)`, so `V_q = D_s C_q
     D_s^*` with `D_s` diagonal — the arithmetic content is ONE matrix
     `C_q = (c_{jk})` of explicit exponential sums per level set.  A local
     law for a matrix with such entries needs a decorrelation input; the
     natural source is Katz's equidistribution for Kloosterman sheaves, which
     Kurlberg-Rudnick [math-ph/0101008] already use for the value
     distribution of Hecke eigenfunctions.  NOT YET TRIED: verifying the
     entrywise moment conditions of a local-law framework against those
     bounds.
  2. the coefficients `alpha_j` of the comb (R82.4) in closed form — the
     Lemma-F quadratic forms `Q_J` should give them exactly; that would
     upgrade R82.4 from [NUMERICALLY-SUPPORTED] to [PROVEN].
  3. `Tr(V_q^2) = N/K^2 . (1 + O(1/K))` with the exact correction — the
     measured mean matches `N/K^2` to 4 digits at (3571, 17); a short
     computation should make it exact and explain the 1.2% spread.
  4. `op:Cdense` (the VALUE) — the sandwich is now `2.2497 <= C_dense <= 3`;
     the rigorous routes are a Lyapunov/discharge certificate for an upper
     bound (a positive `V` on the co-reachable states with
     `sum_c z^{|c|} V(T_c sigma) <= V(sigma)`; note a scalar `V = z^{k|sigma|}`
     provably fails because nonzero `sigma` can be arbitrarily small, so the
     certificate must be genuinely two-dimensional in `(sigma, sigma-bar)`),
     or a first-return decomposition `F(z) = P(z)/(1 - P(z))` with
     `C_dense = 1/z*`, `P(z*) = 1`.
  5. the `eps = -1` and composite-`K` analogues of Theorem I (the proof used
     only that `T` is the norm-one torus; the inert case should give
     `N + 1` per level set — untested).
* NOT TRIED this run: subagents (A5 unused); the `r >= 14` census; a Mathlib
  formalisation (see R82.7); the `m = 1674` design.
* FRAGILE: the comb fit is at ONE design (3571, K = 17); at N = 199 the same
  8-frequency model gives only `R^2 = 0.21-0.49`, plausibly because
  `m_+ = 9` makes individual eigenvalues and the (present) resonances
  dominate — this must be re-tested at a third split design before the comb
  is claimed uniformly.  The `alpha_j` are fitted, not derived.
