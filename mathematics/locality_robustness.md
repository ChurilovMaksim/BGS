---
title: "Microscopic clustering stable above the mean-spacing scale"
author: "BGS research programme"
date: "5 September 2026"
---

# Status and scope

This addendum strengthens the consequences of
[fixed-strength locality](fixed_strength_locality.md). The finite covering
bounds below are elementary. Their role is to make the perturbation and
unfolding thresholds explicit; no priority claim is made. In particular,
operator-norm accuracy better than the mean spacing is **not** necessary
for the negative local-statistics conclusion. The unperturbed reference
still has arithmetic clusters. Nothing here proves positive BGS for a
nonarithmetic chaotic system.

# 1. A finite covering theorem

Let $x_1,\ldots,x_D$ be a multiset on $\mathbb R/\mathbb Z$, including
multiplicities, covered by at most $K$ arcs whose total length is at most
$\ell$. Assume $0\leq\ell<1$. No uniform placement or equal occupancy of
the arcs is assumed. Write $S_j$ for the cyclic gaps multiplied by $D$,
and set
$$
 R_D(x)=\frac1D\#\{(i,j):i\ne j,\ D\operatorname{dist}(x_i,x_j)\leq x\}.
$$
For every $x>0$ and $0<L<D$,
$$
 \frac1D\#\{j:S_j>x\}\leq\frac KD+\frac{\ell}{x},          \tag{R1}
$$
$$
 R_D(x)\geq\frac1{K/D+\ell/x}-1,                           \tag{R2}
$$
and, for a uniformly distributed origin $z$,
$$
 \mathbb P\{[z,z+L/D)\text{ contains a point}\}
                   \leq KL/D+\ell.                        \tag{R3}
$$
The last upper bound can of course be replaced by its minimum with one.
The denominator in (R2) is positive for a nonempty multiset; $K\geq1$.

**Proof.** Merge overlapping arcs first. There are at most $K$ components,
with total length at most $\ell$, and a point outside their union can be
chosen as the seam of the circle. There are at most $K$ gaps connecting
different components. The lengths of the remaining gaps sum to at most
$\ell$. Each gap counted in (R1) has length greater than $x/D$, proving
(R1), without any lower bound on individual gaps.

Divide each covering arc into consecutive cells of length at most $x/D$,
using at most $1+D\ell_i/x$ cells for a component of length $\ell_i$.
A zero-length component needs one cell. Assign shared endpoints to one cell
only, and let $m_c$ be the cell occupancies. All ordered distinct pairs
inside a cell are counted by $R_D(x)$. Cauchy--Schwarz gives
$$
 \frac1D\sum_c m_c(m_c-1)
 \geq \frac D{\#\text{cells}}-1
 \geq\frac1{K/D+\ell/x}-1.
$$
This proves (R2). For (R3), the possible origins are covered by the original
arcs enlarged backwards by $L/D$; their total length is at most
$\ell+KL/D$. End of proof.

Consequently, along any sequence with $K/D\to0$ and $\ell\to0$, the gap
measures converge weakly to $\delta_0$, every fixed-threshold $R_D(x)$
diverges, and the local point measure at a uniform origin converges vaguely
in probability to the empty measure. The last conclusion follows from
(R3) for a compact window containing the support of any test function.
It does not rely on an inference from second moments, nor on uniform
integrability. The expected number in a window is still exactly $L$ at
every finite dimension.

# 2. Perturbations much larger than the mean spacing

Use the notation of the locality theorem, with odd Pell dimension
$D=(N-1)/2=Kn$, the natural single-kick unitary $V_N$, its conjugated
arithmetic reference $W_N$, and
$$
 \delta_N=\|V_N-W_N\|=O(N^{-\infty}).
$$
Let $\widetilde V_N$ be any other unitary satisfying
$$
 \|\widetilde V_N-V_N\|\leq\eta_N,\qquad K\eta_N\to0.       \tag{R4}
$$
The same estimate applies to the parity-restricted matrices; $\widetilde V_N$
need only be defined on that fixed $D$-dimensional space. Then all three
negative local-statistics conclusions above hold for $\widetilde V_N$.

**Proof.** Set $b_N=\delta_N+\eta_N$. The triangle inequality gives
$\|\widetilde V_N-W_N\|\leq b_N$. For large $N$,
$b_N<\sin(\pi/K)$. Normal spectral stability and the unitary homotopy
argument in the locality theorem put exactly $n$ eigenvalues in each root
cluster of circle-coordinate halfwidth
$$
 a_N'\leq\pi^{-1}\arcsin(b_N/2).
$$
Thus the spectrum has a cover with total length
$$
 \ell_N\leq\frac{2K}{\pi}\arcsin(b_N/2)=O(Kb_N)\to0.       \tag{R5}
$$
Apply (R1)--(R3). End of proof.

This statement is uniform over *all* unitary perturbations with the norm
bound (R4); their eigenvectors, internal cluster splitting, and probability
law are unrestricted. In particular, for any fixed $b>0$, the sufficient
condition $\eta_N=O(N^{-b})$ holds since $K=O(\log N)$. When $0<b<1$,
this allowed error is parametrically larger than $1/D$.

For example, a unitary perturbation with norm $O(N^{-1/2})$ still obeys
$$
 \frac1D\#\{j:S_j>x\}=O_x(K/D+K/\sqrt N),\qquad
 R_D(x)=\Omega_x(\sqrt N/K),                                \tag{R6}
$$
where the lower bound is meant for all sufficiently large $N$.
The exact identity $R_D(x)=n-1$ from the unperturbed locality theorem is
not retained under this larger error: individual clusters may have widths
larger than a single mean spacing. The covering proof is what replaces
that identity.

This gives a precise quantization-stability statement **only** for a second
quantization meeting (R4). The same classical principal canonical map by
itself does not imply such an operator-norm bound; leading Fourier-integral
amplitudes or subprincipal conventions must not be silently identified.

# 3. Necessary distortion of any unfolding that restores a nonempty limit

Let $F_N$ be an increasing degree-one map of the circle, with Lipschitz
constant $A_N$. The image of a cover of total length $\ell_N$ is covered by
at most $K$ arcs with total length at most $A_N\ell_N$. Their positions and
occupancies may be arbitrary. Therefore all three collapse conclusions
persist whenever
$$
 A_N\ell_N\to0.                                            \tag{R7}
$$
This is sharper than requiring that every cluster have diameter smaller
than $1/D$ after unfolding.

For a converse necessary bound, suppose the probability that an image
window of a fixed unfolded length $L$ contains a level tends to some
$p_L>0$. By (R3) and $K/D\to0$,
$$
 \liminf A_N\ell_N\geq p_L.                                \tag{R8}
$$
This is a necessary condition, not a sufficient recipe for a desired point
process. If one uses the original equal-width cover, then
$\ell_N\leq2Ka_N$, giving
$$
 \liminf 2KA_Na_N\geq p_L.                                 \tag{R9}
$$
For the explicit Gevrey-2 fixed-strength example and fixed $\kappa\ne0$,
there is a constant $C_\kappa$ such that
$a_N\leq C_\kappa N^2e^{-cN^{1/3}}$. Thus any such unfolding must satisfy
$$
 A_N\geq c_{L,\kappa}\frac{e^{cN^{1/3}}}{KN^2}
 \quad\text{for all sufficiently large }N.                 \tag{R10}
$$
To see the quantifiers, first make the left probability at least $p_L/2$
and $KL/D\leq p_L/4$; then (R3) gives
$2KA_Na_N\geq p_L/4$. Substitute the displayed upper bound on $a_N$.
If a cluster has zero width, no finite Lipschitz unfolding can split its
coincident levels; (R8) remains the appropriate general necessary statement.
The constant in (R10) is not claimed numerically sharp.

# 4. Verification and boundaries

The independent exact finite tests in
`computations/verification/locality_robustness.py` use rational interval
arithmetic. They test long-gap counting, cell pair counts and exact union
lengths for the possible window origins. They include nonuniform cluster
positions, unequal multiplicities, duplicate levels and cyclic seams, and
use a separate piecewise-linear monotone unfolding. Wide-cluster examples
are retained specifically so that individual widths exceed the mean spacing.
No generated finite example proves the limit theorem.

The theorem is a robust negative conclusion for quantizations close to a
specified arithmetic-conjugate family. It does not classify general Anosov
maps, prove that a fixed nonconjugate perturbation has the small norm (R4),
or establish random-matrix universality. Its mathematical input is the
locality theorem plus the explicit covering estimates, not an unproved
extension of the earlier Gaussian central limit theorem.
