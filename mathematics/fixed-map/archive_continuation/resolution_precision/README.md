# Microscopic precision and exact pair-test stability

**Registry:** BGS-TRACE-364.

**Scope.** These perturbation estimates and counterexamples concern arbitrary
unitary spectra with one common uniform shift. The auxiliary unitaries
are not literal fixed-kick quantizations. This note extracts the arguments
in [the November 22 source](BGS_Resolution_Precision.tex). Neither
BGS-BGS-001 nor BGS-TRACE-005 is resolved.

Use the [target's conventions](../../../../record/remaining_breakthrough_task_20261021.md):
\(\phi(t)=e^{-1/(1-t^2)}\mathbf1_{(-1,1)}(t)\), \(I=\int\phi\),
\(b_*=|\mathcal F^{-1}\phi|^2/(2I^2)\),
\(g_*(x)=\int b_*(y)b_*(y+x)\,dy\), and
\(w=\widehat g_*=(\phi*\phi)^2/(4I^4)\).
Let \(\gamma_U\) be the ordered reduced second-moment measure **with
diagonal** of the uniformly shifted unfolded spectrum of \(U\).
The [pair identities](../pair_implications/README.md) give
\(2\Delta_{2,N}(U;b_*)=\gamma_U(g_*)-\mathbb E_{\rm CUE}
\gamma^{\rm CUE}(g_*)\).

## 1. Two perturbation scales

For \(U,V\in U(N)\), write \(VU^*=e^{iH}\) using a Hermitian principal
logarithm with spectrum in \([-\pi,\pi]\). Along \(W_t=e^{itH}U\) choose
locally analytic orthonormal eigenvectors and continue the angle lifts
piecewise, permuting at the joins if necessary. This follows from the
standard Hermitian analytic perturbation theorem applied to a local
Cayley transform at a cut avoiding the local spectrum; a finite
subcover handles the path. Differentiation in radians gives
\(\dot\varphi_j=\langle v_j,Hv_j\rangle\), including on an analytic branch
at a crossing. Thus \(\sum_j|\dot\varphi_j|\le\mathrm{Tr}|H|\) and
\(\max_j|\dot\varphi_j|\le\|H\|_{\mathrm{op}}\).
Chord distance and \(|x|\le(\pi/2)|e^{ix}-1|\) give, for the same matching
in turns,
\[
 \sum_j|\theta'_j-\theta_j|\le\tfrac14\|V-U\|_{S_1},
 \qquad
 \max_j|\theta'_j-\theta_j|\le\tfrac14\|V-U\|_{\mathrm{op}} .
\]
Here the trace norm is unnormalized. Periodization absorbs changes of
the integer lifts. For \(f\in C_c^1(\mathbb R)\) integrate the comparison
of the two linear statistics over the common origin. Unfolding each
summand costs \(1/N\); translation by unfolded distance
\(N|\theta'_j-\theta_j|\) costs at most that distance times
\(\|f'\|_{L^1}\). This bounds the expected absolute difference by
\(\|f'\|_{L^1}\|V-U\|_{S_1}/4\). For nonnegative \(f\) the same bound
applies to the Laplace functional difference. Thus \(o(1)\) trace-norm
error preserves every weak local point-process limit. Local tightness
follows from intensity one, and smooth compact nonnegative Laplace tests
determine the law.

For the pair test the specified weight gives a *relative* estimate:
\[
 \left|\gamma_V(g_*)-\gamma_U(g_*)\right|
  \le C_*\,N\|V-U\|_{\mathrm{op}}\,\gamma_U(g_*)
 \qquad \left(N\|V-U\|_{\mathrm{op}}\le 2\right).
\]
The function \(g_*\) is Schwartz and strictly positive everywhere, as
shown in the [pair note](../pair_implications/README.md).
The triangle kernel \(q(x)=(1-|x|)_+\) obeys \(q\le Cg_*\) and
\((q*\gamma_U)(t)\le(q*\gamma_U)(0)\) by stationary Cauchy–Schwarz for
interval counts. As \(q\ge1/2\) on \([-1/2,1/2]\), each unit interval
has mass at most \(C'\gamma_U(g_*)\).
The function \(G(x)=\sup_{|h|\le1}|g_*'(x+h)|\) has summable unit-interval
suprema. Each unfolded matched pair moves at most
\(N\|V-U\|_{\mathrm{op}}/2\). Sum the mean-value estimate over periodized
pairs and bound \(\gamma_U(G)\) by the unit-interval estimate.
Since the CUE expectation stays bounded, convergence of
\(\Delta_{2,N}(\,\cdot\,;b_*)\) to zero on either side implies the needed
energy bound there. Hence \(o(1/N)\) operator error transfers this exact
test in both directions, without a separate moment or Abel hypothesis.
This does not bound the original family's pair energy.

## 2. A simultaneous low-trace counterexample at \(O(1/N)\)

For arbitrary \(U_N\) and prescribed \(K=K_N=o(\sqrt N)\), there are
unitaries \(V_N\) in the same eigenbasis with the same determinant and
\(\|V_N-U_N\|_{\mathrm{op}}=O(1/N)\). Their spectra are simple with
minimum angular gap at least \(3/(4N^3)\) radians, and
\[
 \max_{1\le m\le K}|\mathrm{Tr}(V_N^m-U_N^m)|=o(1).
\]
The squared errors also sum to \(o(1)\) if \(K=o(N^{2/5})\).
Every nontrivial balanced integer monomial in the eigenvalues of \(V_N\)
is transcendental. Nevertheless
\(\liminf_N\Delta_{2,N}(V_N;b_*)\ge101/32\), and a bounded continuous
statistic rules out a Sine₂ limit for \(V_N\).

**Balanced rounding.** In radians set \(q=\lfloor N/32768\rfloor\)
for sufficiently large \(N\), \(h=2\pi/q\), and
\(\varphi_j=a_j+ht_j\) with \(a_j\in h\mathbb Z,\ 0\le t_j<1\).
Choose a vertex \(p\in[0,1]^N\) preserving the \(K\) complex linear
interpolants
\(\sum_j [ (1-p_j)e^{ima_j}+p_j e^{im(a_j+h)}]\)
at their values at \(p=t\), and the real sum \(\sum_j t_j\).
There are at most \(r=2K+1\) fractional coordinates, since any more
gives a nonzero two-sided kernel direction. Round only them independently
to Bernoulli choices of mean \(p_j\). Denote the resulting angles
by \(\psi_j\), their traces by \(Z_m\), and the total lifted angle
change by \(S=\sum_j(\psi_j-\varphi_j)\).
Direct interpolation and independent bounded increments give
\[
 |\mathbb EZ_m-\mathrm{Tr}U_N^m|\le Nm^2h^2/2,\qquad
 \mathbb E|Z_m-\mathbb EZ_m|^2\le rm^2h^2,\qquad
 \mathbb ES^2\le rh^2 .
\]
Subtract the common angle \(S/N\) to restore the determinant exactly;
the corrected \(Z_m\) changes by at most \(m|S|\). The expected squared
sum of errors is \(O(K^4/N^2+K^5/N^2)\). Hoeffding's bound (or
symmetrization and \(\cosh x\le e^{x^2/2}\)) and a union bound over
\(S\) and the real and imaginary trace errors bound the maximal error
by \(O(K^2/N+K^{3/2}\sqrt{\log(2K+2)}/N)\) with probability at least
\(3/4\). A Markov bound with factor \(4\) for the squared sum gives a
common realization. If \(r=0\) there is no fluctuation.

**Deterministic split.** Add
\(\delta_j=j/N^3+\sqrt{p_j'}/(4N^3p_N')\), with \(p_j'\) the \(j\)-th prime,
and subtract the common mean of these increments. They alter traces by
\(O(m/N)\), preserving both estimates, and separate the angles by the
asserted gap: within one node the rational parts have spacing \(1/N^3\)
and the irrational span is at most \(1/(4N^3)\), while distinct nodes
are separated by \(h-O(N^{-2})\). Since \(|S|\le rh\), the operator error
is \(O(1/N)\). For a nonzero balanced integer vector \(\mathbf n\), both
common shifts cancel in the eigenvalue monomial. Grid phases contribute a
root of unity and the jitter contributes \(\exp(i\sum_j n_j\delta_j)\).
Independent sign automorphisms of the prime square roots imply that
\(\sum_j n_j\delta_j\ne0\). Hermite–Lindemann gives transcendence.

**Specified pair weight and bounded distinction.** For \(m=bq\),
\(1\le b\le8192\), all node phases align, so
\(|\mathrm{Tr}V_N^m|/N\ge1-1/(2N)\) by
\(|\delta_j|\le2/N^2\) and \(m/N\le1/4\).
The overlap interval \([-1/4,1/4]\) in the bump convolution gives
\(w(t)\ge1/2048\) for \(0\le t\le1/4\):
each bump factor is greater than \(1/4\) there and
\(4I^4\le4(2/e)^4<2\). Globally \(w\le e^{-2}/(4I^2)<9/16\)
using \(I\ge e^{-4/3}\). The full CUE subtraction is at most \(27/32\),
since \(N^{-2}\sum_{1\le m<2N}\min(m,N)<3/2\).
Keeping the \(8192\) positive terms proves the liminf
\(8192/2048-27/32=101/32\).
For continuous \(0\le f\le1\) supported on \([-1,1]\) and equal to
\(1\) on \([-1/2,1/2]\), the bounded continuous functional
\(\min(1,X(f))\) has expectation at most \(1/16384+o(1)\) for the
rounded spectra: a hit requires the origin within one of the \(q\)
arcs of length \(2/N+O(N^{-2})\) around the rotated grid nodes.
For Sine₂ its expectation is at least \(1/2\), by
\(\mathbf1_{Y\ge1}\ge Y-\binom Y2\) for the inner-window count \(Y\)
of mean \(1\) and two-point intensity at most \(1\).
This bounded test does not require any uniform integrability.

## 3. Equal traces through almost half the dimension

For \(N=2q+1\) and \(0<a\le1/2\), use the simple spectrum
\(\{(j-a/2)/q,(j+a/2)/q:0\le j<q\}\cup\{0\}\) in turns.
Its determinant is \(1\), minimum gap is \(a/(2q)\) turns, and
its trace at \(m\) is \(1+2q\,\mathbf1_{q\mid m}\cos(\pi a m/q)\).
All traces \(1\le m<q\) therefore agree for every \(a\). Comparing
\(a=1/6\) to \(1/2\), in the band \(m<2N\) only \(q,2q,3q,4q\)
can contribute to the defect difference. Their contributions tend
respectively to \(\frac34w(1/2),-\frac34w(1),0,0\), with the last
using \(w(2)=0\).
The overlap of two centered intervals is nonincreasing in their
relative shift, and strictly decreases from \(1/2\) to \(1\) when
both radii are near \(0.7\). Layer-cake integration of the centered
bump thus gives \(w(1/2)>w(1)\).
The two unfolded limits are random shifts of alternating gaps
\(1/3,5/3\) and the unit clock. The residual shift modulo the
unfolded period \(N/q\) is uniform, that period tends to \(2\),
and the extra point hits a fixed window with probability \(O(1/N)\).
Matching equal \(j\) and equal signs also shows these examples are
\(O(1/N)\) apart.

## Position and reproduction

- [TRACE-114](../../balanced_rounding_research_20261027.md) already
  preserves polynomial short-trace windows at a coarser operator scale.
  The [microscopic rounding construction](../../../spectral-obstructions/microscopic_rounding_control.md)
  has \(O(1/N)\) operator error with squared errors through
  \(o(N^{1/3})\) and a different smooth weight. The advance here is exact
  determinant preservation with enlarged windows and the **prescribed
  full CUE subtraction**, plus a bounded weak-law witness.
- The [previous low-trace obstruction](../../fixed_map_resolvent_frontier.md)
  already exhibits examples with matching sublinear trace data. The
  example above matches all positive traces up to a window asymptotic
  to half the dimension, uses determinant one and simple spectra, and
  gives the exact difference for the target weight \(w\).
- [TRACE-115/116](../../../trace-bridge/microscopic_unitary_stability_20261027.md)
  already give operator-norm weak stability, relative Poisson-energy
  transfer, and compact weight transfer with Poisson control. Here the
  trace norm can be smaller than \(N\|U-V\|_{\mathrm{op}}\), and the
  specified \(g_*\)-energy controls its own relative error. General
  \(O(1/N)\) sharpness was also shown in the
  [factorial bridge](../../../trace-bridge/trace_to_local_statistics_bridge.md).
- [Finite verifiers](../../../../computations/verification/bgs_f_november/resolution_precision/)
  include check.py with the --verify flag (rational certificates) and
  check_matrix.py (a finite numerical linear-programming comparison).
  They do not prove the asymptotic claims. No full Lean formalization
  is asserted.
