# All-order continuation, 5 October 2026

Opening base: `be2e7a9c236df20a0e026a714c8c97327bde973a`, clean local and
remote main. Full deterministic BGS remains the objective; this checkpoint
does not replace it by an auxiliary stochastic model.

## Executed portfolio and outcome contract

| Route | Discriminator | Outcome and remaining implication |
|---|---|---|
| Actual signed defect by spectral heat decomposition | Separate fixed character degrees from growing degrees in the local Fourier observable. | Fixed-degree heat factors approach one; the local observable requires growing Fourier indices. No bound of their actual signed tail has been obtained. Actual FLOW-015 defect stays open. |
| Imported graph universality | Inspect the original graph paper's definition of spectral correlations and phase averaging. | Gnutzmann--Altland uses an energy average and rationally independent bond lengths to obtain a phase average. No mapping to one fixed quantum-map spectrum is supplied; its classical gap alone is not an applicable theorem here. |
| Local-moment transport | Replace a maximum displacement estimate by fixed high Schatten moments and a packing bound controlled by reference maximal density. | FLOW-016 gives all-order uniform integrability when every fixed transport moment vanishes. The projected covariance permits the broader window $t^2\log N\to0$, including the actual logarithmic time. |

Within the third route, FLOW-017 strengthens exit estimates and
uses one superpolynomially small step size to transfer all fixed factorial
orders to the original uncentered chain. Both proof files received one
independent internal review with initial and correction passes by the same
reviewer. These passes are not external refereeing or two reviewers.

Success criterion: fully prove the stated auxiliary all-order law, preserve
its exact initial operator and chain, check finite identities independently,
and integrate only audited conclusions. Deterministic noise removal is a
separate unresolved edge, not a consequence of successful auxiliary checks.

Dependencies and mathematical limits are stated in
[FLOW-016](../mathematics/local_moment_transport.md) and
[FLOW-017](../mathematics/coboundary_all_order_limit.md). The cheapest
falsifier is a clock with a collapsed block: it verifies that a single
finite transport order cannot control arbitrarily high factorial moments.

## Direct heat-spectrum discriminator

For a fixed positive compact smooth $f$, set $h=1-e^{-f}$ and, for
$N$ larger than its support diameter, periodize
$g_N(\theta)=e^{-f_N(N\theta/(2\pi))}$.
Its circle Fourier coefficients are
$g_m=\delta_{m0}-N^{-1}\widehat h(m/N)$.
The Weyl integration formula and determinant expansion give the Haar
coefficient of a charge-zero irreducible character of highest weight
$\lambda$ in the local origin-averaged observable:

$$
c_{\lambda,N}=\det[g_{\lambda_i-i+j}]_{i,j=1}^N.
$$

Thus at each fixed $N$ the exact signed heat defect also has the character
expansion

$$
\mathfrak D_{N,f}(A,t)=\sum_{\sum\lambda_i=0}
c_{\lambda,N}(e^{-t\gamma_{\lambda,N}}-1)\chi_\lambda(A),
\quad
\gamma_{\lambda,N}=\frac{\sum_i\lambda_i^2+
\sum_i(N+1-2i)\lambda_i}{2N}.
$$

Smoothness gives convergence at a fixed dimension; it supplies no
dimension-uniform tail bound. This reformulation is a route computation,
not an additional solved claim. Character heat calculus is prior FLOW-015.

The first two neutral positive degrees give a concrete actual-map check.
Write $s_2=(p_1^2+p_2)/2$, $e_2=(p_1^2-p_2)/2$. In dimensions $N\ge4$
the nonconstant characters of these degrees are

$$
|p_1|^2-1,\quad |s_2|^2-|p_1|^2,\quad
s_2\bar e_2-|p_1|^2+1,\quad
e_2\bar s_2-|p_1|^2+1,\quad |e_2|^2-|p_1|^2.
$$

Their rates are $1$, $2+2/N$, $2$, $2$, $2-2/N$, respectively.
FM-013 bounds their values for the actual starting operator by $C_K$.
Haar character orthonormality and $0\le\Phi\le1$ give
$|c_{\lambda,N}|\le1$. The entire contribution of these five modes to
the signed defect is therefore $O_K(t)$. Their formulas and rates were
checked against direct radial Laurent differentiation, separately from
the transport proof. The growing-degree remainder, which still
contains the Heisenberg-scale indices, remains unestimated. No claim about
all fixed trace orders is inferred merely from the first two trace bounds.

## Exact promoted scope and open continuation

The [review](all_order_review_20261005.md) accepted the auxiliary claims
following fixed-N confluence, pre-exit generator region and Schwartz
period-copy clarifications. C15--C17 give one-chain origin averages and
the complete signed Fourier/CUE target in $L^2$, followed by the exact
discrete noise-removal equivalence. All orders are fixed before N tends to
infinity. The actual unperturbed signed defect remains unestimated. The
model, coupling and terminal objective are unchanged.

This closes the noisy all-order uniform-integrability leaf left open at
previous checkpoints. It uses $\varepsilon_N=N^{-\log\log N}$ and
$\lfloor2t_NN^{4\log\log N}\rfloor$ steps. The earlier polynomial
bounded-Laplace theorem is not enlarged. A single polynomial all-order
schedule and growing-order estimates remain open. World priority is
unverified; the full objective is not replaced by this subsidiary result.

## Computational record

The [contract](../evidence/20261005/all_order_contract.json) and
[version-2 manifest](../evidence/executions/20261005/all-order/manifest.json)
pin all executed sources and declared results. The bounded run completed
with exit zero in 15.06 seconds, under 55 seconds wall time, 50 seconds CPU,
2 GiB address space, one affinity core, one cooperative numerical thread
and a 1 MiB log cap. Input hashes were unchanged; the manifest validator
accepted the record. The initial uncapped smoke check is not promoted.
Two runner contract-validation failures executed no child.

Finite scope: 234 exact rational origin integrals, 96 active packing
segments, 12 collapsed-clock cases, 15 radial character identities, fixed
radial drift controls of orders 1--8, and 54 binary64 unitary matching
diagnostics plus nine principal-log endpoint identities. Seed 20261005 is
confined to matching diagnostics. No enormous-chain simulation, asymptotic
certification or analytic Lean proof is claimed. The review's narrow
algebra reconstruction is recorded separately.

Exact source scope is in
[the literature check](../literature/all_order_sources_20261005.md).
Cross-layer integration and the complete manuscript build are recorded
separately after execution, rather than strengthening the theorem from
successful software output.

The [integration record](../evidence/executions/20261005-all-order-integration.json)
records 8/8 focused checks, the 67-claim/26-source audit and the complete
250-page three-pass manuscript build, with pages 238--239 visually inspected.
Exact-commit CI is checked after publication and retained outside tracked
scientific evidence to avoid self-referential commit records.
