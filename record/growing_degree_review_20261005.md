# Independent internal review: growing degree and the fixed local pair test

Base: `9555cd19dbf7cac335320dc231f2a7b7bb71954f`.
One fresh read-only reviewer reconstructed the candidate mathematics.
Three successive analytic passes by that same reviewer cover G1--G13,
the added G14, and the added G15--G16. These are not three independent
reviewers or external refereeing. No author verdict was supplied in the
tasks. The author separately checked the source normalization and finite
implementation.

**Verdict: G1--G16 proved as written under the pinned inherited inputs.**
The reviewer reconstructed growing packet uniformity rather than merely
assuming it from fixed-time FM-013. All additions were reviewed before
claim promotion.

## Exact scope

| Obligation | Independently checked implication | Boundary |
|---|---|---|
| G1--G2, G6 | Wick normalization, triangular completeness and exact evaluation norms | Both Gram degrees at most $2Q\le N$; no growing-degree CLT |
| G3--G4 | Tensor Casimir bound, Haar contractivity and projected heat defect | Initial $2Q^2$ bound; subsequently sharpened by G15 |
| G5, G7 | Gaussian transition/Parseval Mehler derivation and Euler-product majorant | Positive real parameter; larger source complex domain not imported |
| G8--G10 | Exponential seminorm growth, weighted sampling residual, lattice overlap and return-volume trace integration | Exact odd-N frame and FM-007 return-volume are inherited; no Heisenberg cancellation |
| G11 | $N^{1/4}$ evaluation cost times $N^{-1/2}$ compact Haar deviation | Actual $Q_N=\lfloor\gamma\log N\rfloor$ projection, every heat time |
| G12--G13 | Optimized stronger bounded-trace range and universal Laguerre lower bound | Stronger all-index trace hypothesis not proved for actual map |
| G14 | Exact Gram blindness, variance, clock limit and pair Fourier normalization | One fixed Schwartz pair test; actual value remains unknown |
| G15 | Permutation isometry, class-size balance, cut-and-join quotient and attained Casimir endpoints | Stable range and Haar reducing spaces essential |
| G16 | Band heat gap and particular-local-test inverse bound | Haar $L^2$, not point evaluation or supremum norm |
| Full actual signed tail / BGS | No estimate supplied | OPEN |

## Critical reconstructions

Remove accumulated quadratic evolution, including cat jumps, before
expanding the packet. For an order-$\ell\le5$ word, the insertion
orders satisfy $\sum r_i=\ell$, their number is at most $\ell$, and
the polynomial degree is at most $\sum(r_i+2)\le3\ell$.
Their ordered time volume is at most $(j\kappa)^n/n!$. Coefficients
and every fixed Schwartz seminorm therefore grow by $Ce^{Cj}$,
not an increasing polynomial degree at each iteration. Returning the
quadratic metaplectic evolution costs only a fixed power of its
exponentially bounded variational matrix and inverse.

The physical Fourier remainder has fixed rescaled directions. Fixed
seminorm control gives physical residual $Ce^{Cj}h^4$ at order five;
the weighted sampling bound retains this order. Finite unitary Duhamel
divides by $h$ and absorbs the total time into the exponential,
giving $Ce^{Cj}h^3$. In a small logarithmic window the lattice
Gaussian scale is bounded, so half the nearest-distance exponent can
be factored out and the remaining lattice sum is uniformly bounded.
Weakening Gaussian decay to power four costs another exponential.
The exact frame and uniform return-volume estimate then give G8.
Outside that window, $|p_j|\le N\le e^{j/c_0}$ suffices.

For G14, a participating $m$ satisfies $aN<m<bN$ and a lower
word has $q\le Q<aN$. Thus $m+q<(a+b)N<N$; its exact Gaussian
Gram counterpart cannot contain $Z_m$. For covariance,
$m+n<2bN<N$. The real even test is
$\widehat\varphi(\xi)=w(|\xi|)/2$, as checked against pair bridge
(13); omitting the half would double the statistic.

For G15, class partition $\lambda$ has size $q!/z_\lambda$,
and $\mathcal T_qf=\sum_\lambda(f_\lambda/z_\lambda)p_\lambda$.
Its Gaussian norm is $\sum_\lambda|f_\lambda|^2/z_\lambda$.
The reviewer independently retained the balance
$(q!/z_\lambda)c_{\lambda\mu}=(q!/z_\mu)c_{\mu\lambda}$ when
transferring right transpositions. This gives the exact ordered-split
coefficient $m/2$ and distinct-cycle join coefficient $mn$.
Mixed merging lowers both degrees by $\min(m,n)$, including $p_0=N$.
Haar reducing-space invariance lifts the leading quotient action to
$-qI-(\mathcal C_q\otimes I+I\otimes\overline{\mathcal C_q})/N$.
Constant/sign class functions attain both interval endpoints.

Each G14 band term is in $\mathcal V_{m,N}$, whose gap is at least
$a(1-b)N$. Orthogonality gives G16 for the entire local test.
For $L(P_tJ)=J$, its norm is at least
$\|J\|_2/\|P_tJ\|_2$. At the inherited logarithmic noisy time,
$Nt_N/\log N\to\infty$, so the lower bound is superpolynomial.
No unknown actual-map value is used in this argument.

## Corrections and acceptance

The initial literal inequality $N\sqrt h\ge1$ was false at $N=3,5$.
It was replaced by the exact positive uniform lower bound
$N\sqrt h\ge\sqrt{3/(2\pi)}$ before acceptance. The third pass
corrected the inverse's `image` to its `domain` and recorded the
exact recovery equation and two-point Lipschitz condition. A byte scan
also repaired one form-feed escape in the displayed `-\frac1N`;
the final source has no unexpected control bytes. These are resolved
corrections, not unresolved mathematical assumptions.

| Accepted scope | SHA256 |
|---|---|
| G1--G13 after small-N correction | `a15f59752d838d1aace0cad84b088bb29f769622d17eb862fd0a9ac0b42fb687` |
| Added G14 | `1707a23e5e3a2a5ccda5e75d17d0bb499f2fea2c4af83fda21e820b76a5d70d0` |
| Final G1--G16 mathematical body | `a58cf219aa7fc7d214ecf0f631c85445017058f72193c285b49a446a43044d3d` |
| Source scope checked in third pass | `d6a85c47c0006ffe075c591c5a31f72ae5af274691dc6a50632b18cba20d5951` |
| Promoted proof, only status header changed | `8d1f24b798e44eb0cd8c2841dc624c56b584b0e39c27d83fc5bc331071c88a24` |

The initial pre-correction body was
`bf74552d457805ab8f46f7dcf82467453ea1772ad1d6b87fd7d90febfe80b478`.
The intermediate G15--G16 body before the inverse wording and byte
corrections was
`e784336726819aa9813f53122ca6f1f958fd41136270695570a72b82aab92e84`.
The reviewed inherited proof files retain the pins
`670bdf1e6815ae8add447706726c556874bc7d0f0f562721cb0a3e2b6655f84e`
(FLOW-019), `dea4b671554a5726756e4d1871b427469b4a3ff960fed52ac4a425a0f481a4b4`
(FM-013), and `af615f74c88d475267207b2404d6b0674e6aa7f5b9cc32346bf412d2de3feb39`
(FM-007).

## Execution and source limits

The reviewer did not run the new finite checker. All bounded-run results
are author execution and are not retroactively attributed to that
reviewer. The implementation uses exact Fractions and rational
real/imaginary pairs, with independently enumerated permutation cycles
versus trace-generator images and exact semidefinite gap matrices.
Imported helpers load NumPy, but no floating diagnostics are executed
by this verifier. Integer packet compositions check only bookkeeping.

Primary Ghanmi pages and normalization were checked by the author; the
reviewer reconstructed the required identity directly and did not
certify bibliographic metadata or priority. The existing
Diaconis--Evans stable moment input and other inherited analytic claims
keep their earlier grades. No external referee, full inherited-proof
audit, new analytic Lean, world priority, actual complementary point
evaluation or full BGS proof is claimed.
