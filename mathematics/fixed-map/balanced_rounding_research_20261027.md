# Balanced spectral rounding and short-trace information

**Claim: BGS-TRACE-114. Status: analytic proof with author self-review, 27 October 2026.** No independent referee review or formal certification is asserted. This is a general auxiliary construction, not the original kicked family and not a proof or disproof of TRACE-005. It strengthens the short-trace side of the barrier in [TRACE-025](rounding_simple_spectrum_endpoint_barriers.md) at the cost of a larger operator perturbation; it does not inherit that result's quantitative charge or high-switch estimates.

## Construction

Let $U_N$ be any sequence of $N$-dimensional unitaries. Choose $0<\gamma<1/2$ and $\gamma+1/2<\alpha<1$, set $M=\lfloor N^\gamma\rfloor$, $K=\lceil N^\alpha\rceil$, and $h=2\pi/K$. There exist unitaries $V_N$ sharing an eigenbasis with $U_N$ such that

$$\|V_N-U_N\|\le h+N^{-4},\qquad
\max_{1\le m\le M}|\operatorname{Tr}V_N^m-\operatorname{Tr}U_N^m|
\le \tfrac12 NM^2h^2+M^2h+MN^{-4}=o(1).$$

Moreover the uniformly shifted microscopic point process of $V_N$ converges weakly to the empty process. For instance $\gamma=1/3,\alpha=11/12$ gives an $O(N^{-1/6})$ trace error and $O(N^{-11/12})$ operator error. Hence even absolute $o(1)$ control of all traces up to a positive power of $N$, together with eigenvector preservation and $o(N^{-1/2})$ operator closeness, does not determine the microscopic law.

**Proof.** Write the eigenvalues of $U_N$ as $e^{i\theta_j}$. For each $j$ choose adjacent grid endpoints $u_j$ and $u_j+h$ in a lifted interval containing $\theta_j$, and $p_j=(\theta_j-u_j)/h$. The linearly interpolated exponential at moment $m$ differs from $e^{im\theta_j}$ by at most $m^2h^2/2$; this follows from the second-derivative bound for $e^{imx}$. Define real vectors in $\mathbb R^{2M}$ whose coordinates are the real and imaginary parts of $e^{im(u_j+h)}-e^{imu_j}$ for $1\le m\le M$. Starting from $p_j$, whenever more than $2M$ coordinates are fractional, their vectors are linearly dependent. Move along a nonzero real kernel vector, within the box $[0,1]^N$, to an endpoint of the feasible segment. At least one coordinate becomes integral, no coordinate leaves the box, and every interpolated moment stays unchanged. Repeat until at most $2M$ coordinates are fractional. Round those to the nearest endpoint. Each coefficient changes by at most $1/2$ and each complex vector entry by at most $mh$, so the final moment error is at most $Mmh$ in addition to the interpolation error. This establishes the bound for a grid unitary $V_N^0$.

Give its $j$th eigenvalue an additional phase $N^{-4}2^{-j}$ and call the result $V_N$. The total change in each trace is at most $mN^{-4}\sum_j2^{-j}\le mN^{-4}$. The perturbation has norm at most $N^{-4}$. The phases lie in $K$ arcs of width at most $N^{-4}$. After a uniform common shift, the probability of any eigenphase entering a fixed interval of unfolded length $\ell$ is at most $K(\ell/N+N^{-4}/(2\pi))$, which tends to zero. This proves convergence to the empty process. Degenerate eigenvalues do not obstruct the construction: choose any orthonormal eigenbasis.

The same argument applies to the original fixed-$\tau$ matrices as input, but the constructed $V_N$ does not satisfy their defining kick identity. It does not preserve their exact $O(N^{-2})$ Egorov expansion or other unasserted subprincipal conditions. It is a logical barrier to routes using only the stated information, not a counterexample to the original model.

## Conditional consequence of TRACE-113

If the original family satisfies [TRACE-113](fixed_kick_uniform_trace_bound.md), so $|\operatorname{Tr}U_N^m|\le Ca^m$ for all $m\ge1$ and all sufficiently large odd $N$, then the auxiliary $V_N$ also satisfies $|\operatorname{Tr}V_N^m|\le(C+1)a^m$ eventually. For $m\le M$ this follows from the absolute $o(1)$ estimate; for $m>M$ it follows from $|\operatorname{Tr}V_N^m|\le N$ and $a^M/N\to\infty$. This conclusion uses TRACE-113 as a named input, whose full external dependencies have not been independently re-audited in this note.

## Prior work and limits

The repository's [FM-001](fixed_model_symmetry_theorem.md) already contains the classical $C^1$ symmetry classification, with a stronger parameter range than the independently reconstructed chat argument. [RES-006](fixed_map_resolvent_frontier.md) already contains the adjoint resolvent formulation. Clock rigidity and its positive decomposition are in [TRACE-007 and TRACE-092](../trace-bridge/abel_clock_rigidity.md). These are prior results, not claimed here as new. The proof above was reconstructed separately from its finite fixture; finite checks cannot establish its asymptotic statements. The original fixed coupling, the pair limit and the full Sine₂ problem remain unchanged and open.
