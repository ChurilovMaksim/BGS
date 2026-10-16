# Coordinator audit of the flat equal-edge Hessian argument

Base: `b425a36141cd81c7ef4e832984e7f7ff5074ddc7`.
Date: 16 October 2026. Canonical claim: `BGS-TRACE-093`.

## Scope and disposition

The coordinator reconstructed the finite benchmark, Fock contraction,
Schur/hook argument, sphere estimates, all-m Jensen comparison, collision
mean, triple-edge estimate and the subsequent finite rational formula.
They are accepted as project proofs under their displayed hypotheses.
There is no external referee or analytic Lean certification.

The derivation worker supplied the first Fock/Haar proof. A separate review
worker independently checked the orientation of S and the Fock operator and
supplied an exact generic-tensor verifier. Its 12 integer-complex fixtures
test all 24 eighth-moment and six sixth-moment pairings beyond trace Hessians.
Its final full mathematical review was not received at this checkpoint;
the complete acceptance above is the coordinator's reconstruction. The later
closed rational formula is a coordinator continuation with exact finite and
symbolic checks, not a separately refereed theorem.

## Reconstructed checks and sensitive points

| Step | Audit and exact boundary |
|---|---|
| Gaussian normalization | Entry variance 1/N is split from the unscaled Fock variable Y. The classical formula contains 1/(m+1); at m=1 the unscaled moment is N. The falling product is zero for m>=N. |
| Deficit reduction | For d=prod nu!, 1-1/d<=C_edge/2: check separately C=0, C=1 and C>=2. No bounded-count approximation is used. |
| Fock degree identity | Summing ordered derivatives of a degree-m monomial gives (m)_2. The self-coordinate sum gives exactly 2h_m E_W C_edge. |
| Contracted matrix S | With D_ij=partial/partial Y_ji, S_bc=(D^2)_bc p_m. Its Fock adjoint produces Tr(Y^2D^2), not Tr(YDYD) or an operator with derivatives acting on the leading Y factors. Normal ordering matters. |
| Hook expansion | Both p_m and C_m are expanded using H(t)E(ut). Hooks longer than N vanish. The removed inner product with p_1 p_(m-1) is nonnegative because both trace polynomials have nonnegative monomial coefficients. |
| Consecutive h ratio | Each surviving hook from degree k-1 has ratio N+k-j-1>=N+1. The nonexistent convention h_0=1 is never used; p_0=N. The theorem treats m=2 separately. |
| Off-diagonal sphere estimate | Condition first on u, then v in u-perp. Dropping orthogonal projections increases Frobenius norm. The two fourth moments give 4/[N^2(N^2-1)], followed by N(N-1) coordinate directions. |
| Diagonal sphere estimate | The 24 pairings have 4,16,4 terms by cross-link class. Their exact sums are 2||H||^2+2<H,RH>, 4||T+S^transpose||^2, and |A+B_H|^2. Cauchy--Schwarz yields the stated bound for every pair-symmetric complex tensor. |
| Finite constant | For 3<=m<=N the numerator in the diagonal bound is at most (4+8+16+20)mN=48mN. The theorem rounds this to 60mN, giving 15m/N^2 in the deficit. |
| All-m transfer | The unsimplified collision bound is valid for all N>=2,m>=3. At m/N in a fixed positive compact range its diagonal contribution is O(1/N); Jensen and log(n!)<=binom(n,2)log2 yield the bounded ratio and exact exponential rate. |
| Partial swap | Moving the derivatives of H_cb,ad gives the exact cut-and-join overlap m<p_m,C_m>. The bounded hook mean follows from a geometric tail, not from unproved sampling independence. |
| Sixth moment and triples | Conditional projection is exact; its six pairings control V. Off-diagonal third derivatives use both sphere sixth moments, with the explicit factor 36. Diagonal triples are bounded by the already small loop collision mean. |
| Finite mean | The cross contraction <T,S^transpose> follows from one Fock adjoint. The one-box hook cancellation gives u_m. Keeping the exact 24+6 sums gives (F1). Full hook weights have elementary beta-binomial moments, yielding (F2) only when m>=N+2. |
| Exponentially accurate mean | At m/N in a positive compact interval, the omitted hook tails and column weight are exponentially small. This justifies the rational reference outside its exact finite range and its 1/N expansion; no formula is extrapolated at fixed small m. |

The proof does not establish the collision distribution, its higher-moment
UI, or a limiting value of B/G at m/N->alpha. The first moment and absence
of triples are insufficient for the proposed Poisson law. No diagonal-entry
or independent-phase universality theorem is imported for the actual physical
matrix. Exact flatness is essential to identifying B as the flat word sector.

## Executed finite checks

[Python receipt](../../evidence/executions/20261016/abel-gaussian/receipt.json)
pins commands and hashes. The factorial control enumerates 117,268 rooted
words and 9,250 tables. The polynomial control separately checks Fock norms,
hook signs, the partial swap and the closed mean; the generic-tensor control
does not restrict H to derivatives of a trace. The symbolic control checks
the rational simplification and its first expansion coefficients exactly.
The [C++ observations](../../evidence/executions/20261016/abel-gaussian/conditioned_ewens_exploratory.json)
are finite Monte Carlo only. All such checks supplement the written proofs.
