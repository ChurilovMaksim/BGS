# The full conditional local point-process law

**Stable claim:** BGS-TRACE-068. **State:** PROVED.
**Boundary:** Haar circular background frozen once, randomness then only in compatible phases; spectral L2 functions, paired CSE phases and half trace. Full conditional weak Sine-beta limit in probability over the background. No prescribed deterministic-background theorem or Sine-limit rate.
**Integration and review:** [11 October disposition](../record/chat_integration_20261011.md).
**Original input:** [dated source](../evidence/executions/20261011/chat-research/original/jack_phase_2026_10_11/quenched_local_law.md).


## Unfolding and conditional laws

Fix \(\beta\in\{1,2,4\}\). Sample \(Q_N\) from the corresponding circular
matrix ensemble once, then freeze it. Only the independent diagonal phases
are averaged. Count \(N\) eigenangles \(\theta_j\), once per Kramers pair
for CSE, and fix a deterministic angular center \(\theta_0\).

Use the periodically continued, intensity-one unfolded process

\[
\Xi_N(Q)=\sum_{j=1}^N\sum_{k\in\mathbb Z}
\delta_{\frac{N}{2\pi}(\theta_j-\theta_0+2\pi k)}.
\tag{1}
\]

Let \(\nu_{N,Q}\) be the law of \(\Xi_N(DQ)\) conditional on \(Q\), and
let \(\rho_{\beta,N}\) be the law of (1) for a circular-\(\beta\) matrix.

For each fixed \(D\), the eigenvalue law of \(DQ\) is the same circular
law when \(Q\) is random. In CUE this follows from Haar invariance;
in COE/CSE use \(DQ\sim D^{1/2}QD^{1/2}\) and the Haar lift.
Consequently the unconditional law of \(\Xi_N(DQ)\) is \(\rho_{\beta,N}\).

## A metric estimate

Choose a countable dense family of nonnegative compactly supported
continuous functions \(h_j\), and include all finite nonnegative rational
combinations so that the associated Laplace tests are closed under products:

\[
L_j(\xi)=\exp\left(-\int h_j\,d\xi\right),\qquad 0\le L_j\le1.
\]

They form a convergence-determining family on any uniformly tight
set of point-process probability laws. Define

\[
d_L(\nu,\rho)=\sum_{j\ge1}2^{-j}|\nu(L_j)-\rho(L_j)|.
\tag{2}
\]

Applying the phase-contraction theorem to
\(f_{N,j}(Q)=L_j(\Xi_N(Q))\) gives

\[
\mathbb E_Q|\nu_{N,Q}(L_j)-\rho_{\beta,N}(L_j)|^2
\le\frac{\operatorname{Var}_{\rho_{\beta,N}}L_j}{N+2/\beta}
\le\frac{1}{4(N+2/\beta)}.
\]

Minkowski's inequality, first for finite sums and then by monotone
convergence, therefore proves the slightly stronger bound

\[
\boxed{\mathbb E_Q d_L(\nu_{N,Q},\rho_{\beta,N})^2
\le\frac1{4(N+2/\beta)}.}
\tag{3}
\]

Using the elementary variance bound \(1\) instead would give the
previously recorded constant \(1/(N+2/\beta)\).

## Uniform tightness is deterministic

For each fixed \(Q\), write the phases as a uniform global scalar phase
and independent relative phases. Conditional on the relative phases,
the global phase rotates all \(N\) points uniformly around a period of
length \(N\). By integrating translations in (1),

\[
\mathbb E_D\Xi_N(DQ)(I)=|I|
\tag{4}
\]

for every bounded interval \(I\), for every \(Q\), and for every \(N\).
This is an exact conditional first-moment identity.

Choose a sequence of compact intervals exhausting the real line.
For any \(\varepsilon>0\), Markov's inequality and (4) provide upper
bounds on their point counts whose joint violation probability is at
most \(\varepsilon\), uniformly in \(N,Q\). The resulting family of
locally finite counting measures is relatively compact in the vague
topology. Hence all the conditional probability laws are uniformly tight.

On this uniformly tight family, convergence of all tests in (2) implies
weak convergence: every subsequential limit has the same Laplace
functional, hence the same probability law. This avoids treating an
arbitrary weighted list of tests as a metric without a tightness argument.

## The limit

The circular-\(\beta\) bulk limit is the Sine-\(\beta\) point process.
Valkó–Virág, arXiv:1710.06988, Theorem 6, state it for the scaling \(N\theta\),
which has intensity \(1/(2\pi)\); Theorem 8 explicitly describes periodic
continuation. We divide their coordinate by \(2\pi\), so Sine-\(\beta\)
in the statement below has intensity one.

Equation (3), uniform tightness, and that circular limit imply

\[
\boxed{\nu_{N,Q_N}\ \Longrightarrow\
\operatorname{Law}(\mathrm{Sine}_\beta)
\quad\hbox{in probability over }Q_N.}
\tag{5}
\]

This is convergence of the full conditional point-process probability law,
not just convergence of one two-point statistic.

For any sequence \(N_j\) satisfying \(\sum_j N_j^{-1}<\infty\), (3) also
implies comparison with \(\rho_{\beta,N_j}\) almost surely, under any
coupling of the \(Q_{N_j}\). Indeed
\(\sum_j\mathbb E d_L^2<\infty\), so \(\sum_j d_L^2<\infty\) almost surely.
Combining with the deterministic annealed limit gives (5) almost surely
along that sequence. Independence across sizes is not needed.

The standard deviation bound in (3) is a comparison with the finite
circular law. It is not, by itself, a convergence rate to the limiting
Sine-\(\beta\) law, nor does it give almost-sure convergence along every N.

## Further consequences and limits

A bounded continuous local spectral statistic can be tested directly in
the contraction theorem. Weak convergence also controls bounded events
whose boundaries have zero Sine-\(\beta\) probability. Unbounded factorial
moments, correlation densities and trace form factors at \(n\asymp N\)
need their own uniform moment or integrability bounds.

This model retains a random choice of the scattering background, despite
freezing it before phase averaging. A specified Fourier matrix, or an
arbitrary quantization of a chaotic flow, is not sampled from this
background distribution. No conclusion for those deterministic systems
is obtained by substituting them into (5).
