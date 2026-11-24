# Finite Pell witnesses and necessary spectral tests

**Registry:** BGS-TRACE-363.

**Registry:** BGS-TRACE-362.

**Scope.** The finite inequalities below concern the literal fixed coupling
`tau = 10^(-80)`, not a tuned sequence of kicks. The asymptotic implications
in the last section are conditional statements about weak convergence; none
establishes that convergence for the prescribed family. These notes do not
change the core claim registry.

Use the [maintained model](../../fixed_map_resolvent_frontier.md) with raw
modular Weyl operators, and write
$(1+\sqrt2)^k=h_k+v_k\sqrt2$. As in the [standalone task](../../../../record/remaining_breakthrough_task_20261021.md),
let $p_{m,N}=\operatorname{Tr}U_N^m$, $b_*$ be the specified band-two test,
and $w=|\widehat b_*|^2$. The full pair defect includes the entire CUE
subtraction:
$$
\Delta_{2,N}(b_*)=N^{-2}\sum_{1\le m<2N}w(m/N)
   (|p_{m,N}|^2-\min(m,N)).
$$

## Dimension h_209: a finite return, not an evaluation of the band-two test

At $N=h_{209}=5.00136142311784\ldots\cdot10^{79}$, the certificate gives
$$
|p_{209,N}|/N>1.8\cdot10^{-5}.
$$
At the same dimension it gives:

* An excess greater than $3.2\cdot10^{-10}$ over the **limiting** CUE
  Abel benchmark $(1-e^{-2s})/(4s^2)$ at $s=10^6$.
* An excess in expectation greater than $8.74\cdot10^{-6}$ over Sine₂
  for the bounded continuous observable
  $G(\xi)=(1-\xi(f_T)/T)_+$, where $T=10^6$ and
  $f_T(y)=(1-|y|/T)_+$. The support length is fixed in unfolded units.
* Positive signed non-cyclic interference at this one short return:
  $Y_{209,N}/N^2>3.23\cdot10^{-10}$.

No positive lower bound for **the full** $\Delta_{2,h_{209}}(b_*)$ follows
from the return: the one term does not pay for the whole CUE subtraction.

The [original Pell proof](BGS_F.tex), §§1–4, transfers the normalized trace
for a finite Weyl polynomial to the trace of a finite lattice operator.
For odd $k$, $S^k-I=2h_kB_k$ with $B_k$ integral and unimodular.
Closing an ordered word modulo $h_k$ is therefore equivalent to closing
its unique translated trajectory on the half-integer lattice. The change
in its total Weyl phase telescopes to zero modulo $h_k$. The stable and
unstable directions bound all such cycles in a finite region, split into
four parity sectors. For $k=209$ the rational polynomial approximation,
controlled rounding and trace reevaluation give the center
$(42155281424489+2359315878140i)/2^{61}$ and total error below
$2.1\cdot10^{-7}$. From the central checker directory, `python research/verify.py` reads
the supplied diagonal outputs and verifies the rational error budget and
strict inequalities; the separate, slower `python research/reproduce.py`
regenerates those outputs with C++. It is not a
dense computation in dimension $h_{209}$.

The older [main-branch exact Pell witnesses](../../pell_microscopic_window.md)
treated, in particular, $h_{207}$ for the original band-two weight. The
already-maintained [TRACE-113 power-trace bound](../../fixed_kick_uniform_trace_bound.md),
$|p_{m,N}|\le C a^m$ with $a<1+\sqrt2$, also settles the tempting
extension of this new finite obstruction by the **same** return:
$|p_{k,h_k}|/h_k\to0$ as odd $k\to\infty$. This does not say that all
other Pell-time tests converge, and it gives no control at $m\asymp N$.

## Stronger finite band-two witnesses at other dimensions

The [original spacing chapter](BGS_Spacings.tex), §§1–3, separately gives
$\Delta_{2,h_{207}}(b_*)>0.02448$ and the return bound
$\operatorname{Re}(\overline\mu p_{207,h_{207}})/h_{207}>0.65530$
where $M_{h_{207}}^{207}=\mu I$. This strengthens the maintained lower
bound $0.001$ at that same size. It also gives
$\Delta_{2,N}(b_*)>221$ on the 1034 odd multiples of $h_{175}$ in
$[10^{70},2\cdot10^{70}]$. A short linear return covers the spectrum
by relatively few arcs; Cauchy–Schwarz on that covering gives the
weighted lower bound after subtracting the whole CUE reference.
At $h_{207}$ the strengthened calculation instead uses the
Hilbert–Schmidt bound for averaged phase velocities and a certified
upper bound for the finite CUE subtraction. The rational verification (`python spacings/certify.py` from the central
checker directory) reproduced these finite claims. Other diagnostics, continuous tests and
asymptotic discussion in the chapter are preserved with scope as
stated in the source, not independently audited line by line.

## What weak Sine₂ would imply

The [Pell source](BGS_F.tex), §§5–7, proves three implications not
requiring a separate second-moment hypothesis at the outset. See also
[the standalone pair-implication proof](../pair_implications/README.md).

1. For every fixed $C>0$, weak Sine₂ implies
   $\max_{1\le m\le CN}|p_{m,N}|/N\to0$. Against a putative subsequence,
   modulate the local count on a fixed interval by its limiting frequency
   $m/N$. The first moments are uniformly integrable because their means
   equal that of the limit. Sine₂ variance for the limiting linear
   statistic is at most the interval length. Taking its length to infinity
   forces the normalized trace to vanish.
2. With the positive measure of unfolded pair differences including
   diagonals, $\gamma_N$, weak Sine₂ implies
   $\liminf\gamma_N(g)\ge\gamma_{\mathrm{Sine}_2}(g)$ for nonnegative
   continuous $g$. For compactly supported $g$, stationarity represents
   this as the expectation of a nonnegative local continuous functional;
   truncate that functional, then use monotone convergence. Thus a
   negative deficit separated from zero along an infinite subsequence
   would refute the weak law even without proving uniform integrability.
   A positive excess does not give that conclusion by this argument.
3. Weak Sine₂ **plus** the specific test `(P)` implies all fixed
   second-order tests and the Abel limit. The autocorrelation of $b_*$
   is strictly positive everywhere. The single matching weighted
   integral excludes any positive defect in a vague subsequential
   limit of $\gamma_N$. Stationarity and Cauchy–Schwarz then bound the
   measures of all unit intervals, controlling tails for Schwartz and
   Abel tests.

The general Heisenberg-scale signed hierarchy and the full weak fixed-map
law remain open. See the [central checker](../../../../computations/verification/bgs_f_november/)
and the [original problem statement](problem.md).
