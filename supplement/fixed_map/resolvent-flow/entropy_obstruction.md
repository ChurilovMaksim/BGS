# A limitation of global-entropy smoothing of a deterministic spectrum

Status: elementary proved implication, internally audited. No novelty or
BGS claim. The result concerns a proposed proof mechanism, not a failure
of universality. It applies even to a fixed sequence with sine statistics.

Let T_N=R/(N Z), let x_N be any deterministic labeled N-point configuration
on T_N (multiplicities allowed), and let Q_N be labeled unfolded CUE.
For another configuration y, define the rotation-invariant matching distance

\[
d_N(y,x_N)=\inf_{\alpha\in T_N,\,\sigma\in S_N}
 \left[\frac1N\sum_{j=1}^N
  \operatorname{dist}_{T_N}(y_j,x_{\sigma(j)}+\alpha)^2\right]^{1/2}.
\tag{1}
\]

The scale is unfolded: d_N=o(1) means that the RMS matched displacement,
after a common rotation, is negligible compared with one mean spacing.

**Proposition.** For every sequence of probability laws P_N on T_N^N,

\[
d_N(Y_N,x_N)\longrightarrow0\quad\text{in }P_N\text{-probability}
\quad\Longrightarrow\quad
\frac1N D(P_N\Vert Q_N)\longrightarrow+\infty.
\tag{2}
\]

Relative entropy is allowed to be infinite. Label exchangeability of P_N
is not required. The conclusion remains true after ignoring common
rotations in (1); those rotations have already been included in the bound.

## Proof with a finite-dimensional bound

In unfolded coordinates the labeled CUE density is

\[
q_N(y)=\frac1{N^N N!}
 \left|\det[e^{2\pi i(k-1)y_j/N}]_{k,j=1}^N\right|^2
 \le\frac1{N!}.
\tag{3}
\]

Each column of the determinant has Euclidean norm sqrt(N), so (3) follows
from Hadamard's determinant inequality. Its normalization is the ordinary
CUE Vandermonde density with the change of variables theta=2pi y/N.

Fix 0<delta<=N. A mesh of M=ceil(N/delta) equally spaced rotations has
covering radius at most delta/2. If d_N(y,x_N)<=delta, some permutation
and rotation give product-torus distance at most sqrt(N)delta. Replacing
that rotation by the mesh point adds at most sqrt(N)delta/2. Thus the
event is contained in a union of M N! torus balls of radius 2sqrt(N)delta.
The infimum in (1) is attained by compactness and finiteness.

A torus ball is a quotient projection of the Euclidean ball of the same
radius. Projection cannot increase Lebesgue volume, even beyond the
injectivity radius. If v_N denotes Euclidean unit-ball volume, (3) gives

\[
Q_N(d_N\le\delta)\le
 \min\{1,\lceil N/\delta\rceil v_N(2\sqrt N\delta)^N\}
 \le\min\{1,\lceil N/\delta\rceil(C\delta)^N\},
\qquad C=\sqrt{8\pi e}.
\tag{4}
\]

For completeness, the volume estimate v_N<=(2pi e/N)^(N/2) follows by
integrating exp(-lambda |z|^2) over the unit ball, bounding it below by
exp(-lambda)v_N, and then choosing lambda=N/2 in the Gaussian integral
over all of R^N. No asymptotic Stirling approximation is needed.

Let E={d_N<=delta}, p=P_N(E), q=Q_N(E). Binary data processing and the
bound on binary entropy give

\[
D(P_N\Vert Q_N)\ge
 p\log(1/q)-\log2.
\tag{5}
\]

For 0<delta<=1 and N>=2, ceil(N/delta)<=2N/delta. Combining (4)--(5),

\[
\frac{D(P_N\Vert Q_N)}N\ge
p\left[\left(1-\frac1N\right)\log\frac1\delta
        -\log C-\frac{\log(2N)}N\right]-\frac{\log2}N.
\tag{6}
\]

If the bound inside (4) exceeds one, the logarithmic lower bound in (6)
can be negative but remains valid. If q=0, the extended entropy inequality
has its usual interpretation. Under convergence in probability, one can
choose a deterministic delta_N tending to zero with P_N(E_N) tending to
one. Formula (6) proves (2), regardless of how fast delta_N shrinks.
Alternatively fix delta, let N tend to infinity, and then send delta to
zero. This completes the proof.

## Exact consequence and limits

A smoothing law cannot simultaneously (i) preserve one deterministic
spectrum at vanishing unfolded RMS distance and (ii) satisfy global
D(P_N||CUE_N)=o(N). In particular, that conjunction cannot be used to
transfer a CUE comparison back to the original fixed map.

This proposition does **not** rule out local correlation convergence,
entropy comparisons in a fixed or mesoscopic window, entropy relative
to a conditioned law, time reversal arguments, or Dyson Brownian methods
with a different displacement scale. No assertion is made that every
such method assumes the incompatible global conditions above. The result
does not supply an estimate of the frozen map's loop residual.

The proof was checked by a separate internal agent, including the rotation
mesh, torus-volume projection, labeling factor, and arbitrary rates
delta_N->0. This is not external peer review or a formal Lean proof.
