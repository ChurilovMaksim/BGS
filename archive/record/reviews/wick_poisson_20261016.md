# TRACE-094: high-derivative and Poisson proof audit

Base: `f78ec82ffe8c6535c961abc969a719704bf3e942`. Date: 16 October 2026.
Primary verdict: **proved as written**, within the precise flat positive Wick
measure and fixed-order/compact m/N hypotheses of the
[canonical proof](../../mathematics/wick_collision_poisson_20261016.md).
This is an internal project verdict, not external refereeing or priority review.

## Claim card and dependencies

Y has independent standard circular complex Gaussian entries. The homogeneous
polynomial is p_m=Tr Y^m, and W assigns an edge table nu probability
c(nu)^2 prod nu!/h_m. For every fixed 0<a<b and fixed derivative/moment order,
aN<=m<=bN and N tends to infinity. The conclusion is a Poisson(2alpha^2)
collision law, B/G->exp(-alpha^2), and the explicitly stated corollaries.
Orders do not grow with N; loops, reversed edges and repeated endpoints remain
admissible. No deterministic spectral process is asserted to be Poisson.

The analytic dependency chain is:

1. TRACE-093's exact Gaussian Fock convention, Schur norms, hook expansion and
   Hessian upper-swap identity.
2. The finite hook-character coefficient bound for a bounded number of trace
   factors, rederived in the proof using the Hall product.
3. Normal ordering and a directed-cycle graph for every partial contraction.
4. Classical finite Haar integration (Collins--Sniady, Corollary 2.4) and its
   fixed-degree Gram inverse, with the project-specific index dictionary.
5. Uniform coordinate derivatives, leading disjoint-label constants, factorial
   moments and finite Bonferroni bounds.

No finite computation is a logical substitute for one of these steps. The
proof does not use the proposed Poisson law to prove an input to itself.

## Independent reconstruction, Sections 1--5

One fresh reviewer received the raw proof and underlying definitions, without
the coordinator's verdict or finite output. It did not edit files, spawn
agents, or conduct an external source review. It independently reconstructed:

| Obligation | Disposition and decisive check |
|---|---|
| Hook overlap | Passed. The coefficient of prod(1-t^v)/(1-t) is a sum of at most 2^ell signs. Finite-N specialization discards only overlong hooks. |
| All partial contractions | Passed. Move all k derivatives of one factor to creation variables. Each identified endpoint joins an incoming and outgoing strand; components are cycles. A zero cycle contains a separate zero marked segment, so no uncharged N loop remains. |
| Composition counting | Passed. Exactly q zero gaps give binom(k,q) binom(m-k-1,k-q-1) choices. For m>k this makes the norm O_k(m(N+m)^(k-1)h_m). |
| Haar input/output dictionary | Passed. For the chosen covariance action the output lists are (I,J) and (J,I); the input lists are (A,D) and (B,C). Every input pairing is an inner product of two allowed partial contractions. |
| Higher upper swaps | Passed. Mixed Fock homogeneity gives K_k=(m-2)_(k-2)K_2. A permutation of transposition length L loses at most 2L^2 jbar/(m-1) of normalized overlap. |
| Coefficient 4^r | Passed. Each of r twice-marked edges gives a factor 2! in each of the two label lists. The number of fully distinct endpoint tuples is (N)_(2r). |
| Shared/reversed/loop patterns | Passed. They have only O_r(N^(2r-1)) label choices and are controlled by the uniform, rather than disjoint-only, derivative estimate. |
| Probability conclusion | Passed. The indicator replacement uses order 2r+1. Bonferroni truncation is held fixed before N tends to infinity, then removed. Bounded transforms require no unproved exponential UI. |

The reviewer requested two exposition corrections: explicitly say that all k
derivatives are moved, and write out the Haar dictionary and K_k identity.
Both are included in the canonical version. No mathematical gap or concrete
counterexample was found in the reviewed chain.

## Separate author adversarial pass and corollaries

The coordinator checked k=1 separately, m>k in the zero-composition count,
N>=2k for the ordinary Gram inverse, the signs in the auxiliary Hall product,
and the distinction between probability of triple edges and moment convergence.
The latter distinction is why indicators D are used before transferring the
bounded transform to C. No exponential moment bound on C is assumed.

Sections 6--7 are author-derived corollaries, outside the independent review:

- Arbitrary deterministic disjoint edge classes require only their cardinality
  densities. Endpoint coincidences are bounded uniformly even for irregular
  classes, and multivariate thinning identifies the joint Poisson law.
- Vertex counts use ordered row derivatives. Distinct lower labels outside the
  fixed upper labels number (N-l)_K; upper multiplicity is prod k_i!. This gives
  independent geometric limits. In/out counts at a single vertex remain equal.
  Moment identification uses the target's exponential moment, plus higher-order
  bounds for subsequential UI, not UI deduced from weak convergence.
- The iid radial-entry comparison assumes ALL even radial moments <=j!.
  This bounds the exact density product by one, allowing triple-edge removal.
  It does not imply the corresponding theorem for kappa>2.

All three deductions were reconstructed by the author directly from the proved
coordinate estimate and probability law. They have not had external refereeing.

## Finite controls and residual boundary

[Actual execution](../../evidence/executions/20261016/wick-poisson/exact/manifest.json)
compares integer monomial Fock norms with contraction graphs/hook overlaps,
and exact rational Haar Gram integration. It covers 928 contraction norms,
17 higher swaps, 86 trace overlaps, 38,435 graph/order pairs through k=5,
7 Haar dictionaries, 12 indicator comparisons, 20 row identities and 12 bounded
radial-weight comparisons. These are bounded checks, not asymptotic proofs.

No full-workspace regression, manuscript PDF, analytic Lean compilation,
non-flat comparison, physical signed cancellation or full BGS claim is certified.
The Gaussian finite benchmark is prior work. Priority of the new complete
comparison and corollaries remains unestablished.
