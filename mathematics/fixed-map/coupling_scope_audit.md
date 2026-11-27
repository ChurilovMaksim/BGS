# Coupling scope: how to read the fixed-map results

This is a scope guide for the maintained quantization, not a registry
amendment or a new local universality theorem. Stable IDs and current
states are controlled by [the registry](../../record/claim_registry.md).
The original problem remains the fixed value \(\tau_*=10^{-80}\).

## Three parameters which must not be conflated

For odd \(N\ge3\), retain the literal Weyl matrix \(A_N\) and propagator
\(M_N\) of the [exact problem](../../record/remaining_breakthrough_task_20261021.md).
Write \(U_N(\tau)=\exp(i\tau N A_N)M_N\). Here \(\tau\) is the physical
coupling, \(\kappa=\tau/(2\pi)\) is the classical flow time (with Egorov
map \(\Phi_g^{-\kappa}\circ S^{-1}\)), and \(t=N\tau\) is the
matrix-exponential time without the factor \(N\) in its exponent.
In particular, small fixed \(\tau\ne0\) does not imply small \(t\) as
\(N\to\infty\). The physical symbol includes the ordinary-Weyl midpoint
correction in the \(p\)-dependent term.

## Selected source-checked scopes

| Result | What the source already covers | Boundary for an extension |
| --- | --- | --- |
| [BGS-FM-001](fixed_model_symmetry_theorem.md) | Classical Anosov structure and \(C^1\) symmetry statement for real \(0<|\kappa|\le10^{-12}\), with either sign | Does not exclude \(N\)-dependent quantum symmetries or determine microscopic eigenphases. |
| [BGS-TRACE-106](physical_kick_trace_decay.md) | Normalized trace of the single physical kick: exponent \(1/9\) when \(0<|\tau|\le10^{-20}\) and \(N|\tau|\ge1\); a positive exponent on every bounded physical-time interval | No trace theorem for powers of the full product; do not reuse the paper's variable \(t\) as matrix-exponential time here. |
| [Exact algebraic simplicity](frozen_algebraic_spectral_simplicity.md) | For odd \(N\) with \(7\nmid N\), every nonzero real algebraic matrix-exponential time, hence every nonzero real algebraic \(\tau\) | Does not give simplicity at all transcendental couplings, at \(7\mid N\), or quantitative bounds on gaps. |
| [BGS-TRACE-113](fixed_kick_uniform_trace_bound.md) | For the original \(\tau_*\), one \(N_0\) for every \(m\ge1\), with \(|\operatorname{Tr}U_N^m|\le Ca^m\), \(a<1+\sqrt2\) | Extending the Gaussian normal form and all its error budgets to a larger parameter range requires proof. A logarithmic-time consequence is not control at \(m\asymp N\). |
| [BGS-FM-013](fixed_time_wavepacket_trace_bound.md) | Bounded unnormalized traces at each fixed power for the original \(\tau_*\); distinct numerical bounds for powers one and two | The proof's isolated, nondegenerate periodic points and finite-time packet budgets are the inputs to an extension. The explicit starting constants have their own proof and should not be carried over without rechecking. No uniformity in the power. |
| [BGS-FM-021](position_chain_mixing.md) | Position-chain contraction and cyclic ramp for the original \(\tau_*\); the proof references an explicitly bounded small-time parametrix | Check transport amplitude bounds and non-aliasing separately from the nonzero mixed Fourier coefficient, then re-audit iterate-uniform consequences. Positive-kernel mixing cannot estimate the total signed complement. |
| [Phase-model transfer](phase_model_transfer.md) | Fixed original \(\tau_*\); admissible fixed Laplace and fixed-order factorial tests transferred under the stated parametrix and approximation hypotheses | The approximation errors and constants must be checked before transferring to another fixed coupling or a varying order. The transfer does not prove the limiting statistics of the phase model. |
| [BGS-FM-002](fixed_model_pell_crossover.md) | Gaussian crossover in a shrinking-kick regime on odd Pell dimensions, with \(N\tau_N\sqrt{k}\) bounded in the theorem | Does not cover fixed nonzero \(\tau\), for which \(N|\tau|\sqrt{k}\to\infty\). |
| [Sevenfold oldspace singular spectrum](seven_oldspace_singular_spectrum.md) | Source states the original \(\tau_*\) and \(N=49m\), \(m\) odd; one-step compression | The argument below extends the singular-spectrum theorem to every fixed real \(\tau\ne0\), without extending the separate mean-retention or eigenphase statements. |
| [Finite Pell witnesses](pell_microscopic_window.md) and [continuation](archive_continuation/pell/README.md) | Explicit finite dimensions and the exact original \(\tau_*\); individual states and boundaries remain those of the registry | Do not extrapolate a finite witness to an infinite fixed-parameter subsequence. A finite continuity interval, if proved, is dimension- and test-dependent. |
| [BGS-BGS-001 and BGS-TRACE-005](../open_questions.md) | Open for the original fixed map | Showing parameter dependence of preliminary estimates does not settle any microscopic limit. |

## Research targets, not theorem statements

1. Audit TRACE-113 for a nonzero interval of both signs. The pressure
   argument has an exact sign-specific witness under its classical
   hypotheses. Set \(\Psi=(S\circ\Phi_g^\kappa)^{-1}\), as in the
   [Egorov convention](fixed_kick_uniform_trace_bound.md). At a critical
   fixed point with \(\operatorname{Hess}g=\operatorname{diag}(b,0)\),
   the kick derivative is \(\left(\begin{smallmatrix}1&0\\\kappa b&1\end{smallmatrix}\right)\);
   multiplying by \(S^{-1}\) gives trace \(6-4\kappa b\).
   By the [Hessian calculation](fixed_model_symmetry_theorem.md), this is
   \(6+(39212\pi/125)\tau\) at the origin and
   \(6-(49788\pi/125)\tau\) at \((1/2,1/2)\). Select the first for
   positive coupling and the second for negative coupling. Neither
   witness supplies the quantum normal form or its error bounds uniform
   in the iterate.
2. Keep the pointwise quantifier: fix \(\tau\ne0\) first and then take
   \(N\to\infty\) through all odd integers. Uniformity on compact
   intervals away from zero, almost-everywhere assertions, and the
   shrinking-kick regime are distinct. No published scope change is
   authorized by a notation change.
3. Keep the original band-two test as a checkpoint. Its signed residual
   after the cyclic ramp must give the negative correction, not vanish.
   Boundedness of the close-pair energy alone does not give convergence
   of second moments from a weak limit. A proof for the full hierarchy
   or a direct weak-limit argument needs separate justification.

## Backlog and closure rules

| Priority | Open work item | Acceptance evidence |
| --- | --- | --- |
| P0 | Re-audit pointwise fixed-coupling hypotheses in the all-time trace bound and signed Heisenberg-scale comparison. | A proof for each claimed range with exact quantifiers and dependencies, or a precisely stated missing estimate. |
| P0 | Separate the pair criterion from the complete fixed-order hierarchy and from possible bounded weak-limit obstructions. | A dependency map with named first unproved steps; no changes to existing open states unless their closure conditions are met. |
| P1 | Map additional active claims to fixed, shrinking, arithmetic-only, random or auxiliary parameter regimes. | Source locators and a reviewed boundary for each promoted claim; no regex-based promotion. |
| P1 | Align proof locators, reviews, scripts, generated views and bilingual summaries without erasing older evidence. | Canonical-source diff, check of generated views and a reproducible verification receipt pinned to the reviewed base. |
| P2 | Record reproducibility and documentation gaps in old and new components. | For each issue name the command, inputs, expected result and actual environment; preserve archived snapshots and use errata for corrections. |

## Sevenfold singular spectrum for every fixed nonzero real coupling

For every fixed real \(\tau\ne0\), take the same oldspace \(P\) and
\(N=49m\) with \(m\) odd as in the
[one-step compression proof](seven_oldspace_singular_spectrum.md).
For each \(t\in[0,1]\) and \(\epsilon>0\), at least
\(c(\tau,t,\epsilon)\sqrt N\) singular values of
\(P U_N(\tau)|_{\operatorname{ran}P}\) lie in
\((t-\epsilon,t+\epsilon)\) for all sufficiently large admissible
\(N\). In particular its norm tends to one and its singular spectra
converge to \([0,1]\) in Hausdorff distance. This extends the theorem
on singular values only, not the separate finite-escape or
mean-retention claims. It is not an eigenphase result.

**Quadratic phase rank.** Use the source's \(q_j=1/2+j/7\),
\(\theta_j=2\pi j/7\), and \(F_j=\tau V'(q_j)\) with \(F_0=0\).
With \(x=2\pi u\), the diagonal \(V(q_j+u)\) is
\(-\cos(7x)-1/10+(1+\cos(7x)) f(\theta_j+x)\), where
\(f(y)=(1-\cos y)(1/10-\sin y/100)\).
Its second derivative in \(x\) at zero is \(49-49 f(\theta_j)+2f''(\theta_j)\).
Consequently the relative quadratic coefficient
\(D_j=\tau(V''(q_j)-V''(q_0))/2\) is \(2\pi^2\tau d_j\), where
\[
 200d_j=1020(\cos\theta_j-1)+102\sin\theta_j-57\sin(2\theta_j)
 \qquad (1\le j\le6).
\]
The [exact cyclotomic check](../../computations/verification/coupling_scope_audit/check_oldspace_phase_rank.py)
represents the six \(400d_j\) in the basis
\(\{\zeta_7^r,i\zeta_7^r:0\le r\le5\}\) and obtains rational
rank six by elimination. One can see the rank without computation:
the automorphism fixing \(\zeta_7\) and reversing \(i\) separates the
sine and cosine equations. On the three antisymmetric pairs, angle
doubling is a signed permutation, so \(102I-57T\) is invertible;
the three sine values are independent by the degree-six cyclotomic
polynomial argument of source section 1. Thus paired coefficients
in any rational relation must agree. The three \(\cos\theta_j-1\),
\(1\le j\le3\), are independent: a symmetric degree-six polynomial
for their relation would have to be a multiple of \(\Phi_7\);
if every nonconstant coefficient equals \(a\), its constant
coefficient is \(-6a\), forcing \(a=0\). Thus \(h\cdot D\ne0\) for every nonzero
integer six-vector \(h\). The rank-five linear coefficients alone
do not exclude discrete resonances; they are not used for density
in the full phase torus here.

**Packets across discrete resonances.** In section 4 of the source
replace the formally indexed box by a box of distinct points in
\(\Gamma=\langle F_1,\ldots,F_6,2\pi/7\rangle\) in the momentum
circle. Choose a decomposition of this finitely generated abelian
group as \(\mathbb Z^r\oplus T_f\) with finite torsion group \(T_f\).
Use the image of \([-B,B]^r\cap\mathbb Z^r\) times all of \(T_f\),
including the case \(r=0\). This set \(E\) is exactly invariant under
\(2\pi/7\). Translation by each fixed \(F_j\) moves only an
\(O_\tau(1/B)\) fraction of the points out of it, since only a boundary layer
of the integer box is lost. Therefore the same Fourier packets have
support in \(7\mathbb Z\) and are almost invariant under modulation
by each \(F_j\), using the finite Gram-matrix limit as the packet
radius grows. No independence of the discrete frequencies is needed.

**Simultaneous recurrence and the count of centers.** For this finite
\(E\), omit the countable set of momenta \(p\) solving any equation
\[
 h\cdot D+\sum_{0\le j\le6,\,\gamma\in E}\ell_{j\gamma}H_j(p+\gamma)=0,
 \qquad h\in\mathbb Z^6\setminus\{0\},\quad \ell_{j\gamma}\in\mathbb Z,
\]
where \(j\) ranges over all seven packets and each \(H_j\) is the
first harmonic of section 3. Each equation has only finitely many
solutions, because its constant term is nonzero and the remaining
terms form a first harmonic. The continuous positive orbit in the
torus with velocity \((D,(H_j(p+\gamma))_{j,\gamma})\) has closure
containing \(\mathbb T^6\times\{0\}\): every annihilating character
has zero first six coordinates, by the chosen momentum. Here angles
are taken modulo \(2\pi\). This is the same character criterion as
in section 4, now for the full relative phase vector. For any fixed
tolerance, compactness gives a finite collection of bounded positive
\(z\)-intervals of positive length such that, for each relative
phase target, one whole interval attains the tolerance with strict
margin in all phase and hopping coordinates.

At the admissible center \(s=7/2+7l\) write \(z_s=s^2/N\). The six
relative phases have the expansion
\[
  A_N^{\rm rel}+(7/2)F+7lF+z_sD+O_\tau(N^{-1/2}),
  \qquad A_{N,j}^{\rm rel}=\tau N(V(q_j)-V(q_0)).
\]
This remainder is uniform on the finite union of fixed intervals.
Select a target \(x\) for which \(|1+\sum_{j=1}^6 e^{ix_j}|/7=t\),
and choose one \(z\)-interval to offset
\(A_N^{\rm rel}+(7/2)F\), leaving \(7lF\) temporarily unused.
There are \(\gg\sqrt N\) centers in an interior subinterval.
The closure of the integer rotation by \(7F\), whatever its
dimension, has a fixed finite net of actual multiples \(7aF\).
For each such center choose an adjustment \(a\) from that net
approximating \(-7lF\). Since the adjustments are bounded,
they change \(z_s\) by \(O(N^{-1/2})\); the interior margin and
hopping tolerances survive. Taking the initial centers sufficiently
spaced preserves disjoint supports at all seven translates.

Now apply precisely the packet residual and singular-projector
estimates in source sections 3 and 5 with the fixed \(\tau\).
Choose the momentum set, intervals and adjustment net before the
packet radius and finally the dimension threshold. The propagation
errors can be made arbitrarily small, uniformly over these centers,
and the \(\gg\sqrt N\) normalized combs remain orthogonal. The
compressions of both the kick and its adjoint approximate the scalar
and its conjugate on each comb, so Bessel's inequality for the
spectral projector of \(C^*C\) gives the asserted multiplicity.
At \(\tau=0\), in contrast, the intertwiner reduces the compression
to \(M_m\) itself and all singular values equal one.

## A separate exceptional set for eigenvalue simplicity

**Finite-dimensional eigenvalue simplicity.** For each odd \(N\)
with \(7\nmid N\), the [simplicity proof](frozen_algebraic_spectral_simplicity.md)
shows that the entire discriminant of the characteristic polynomial
is not identically zero in matrix time. Setting matrix time to
\(N\tau\) preserves that property. Its real zero set is locally finite
for each such \(N\); their union, over all these dimensions, is
countable. Outside this union the spectrum is simple simultaneously
at every such dimension, and the algebraic-time theorem excludes
nonzero algebraic couplings from the union. No uniform gap size or
spacing law follows. This exceptional set concerns eigenvalues,
not the singular spectrum of the compression, and does not cover \(7\mid N\).

## The endpoint at zero: a sharp obstruction to uniform trace bounds

Let \(c=1+\sqrt2\) and take odd \(k\ge3\). At the odd Pell dimension
\(N=h_k=(c^k-c^{-k})/2\), the
[exact return](fixed_model_pell_crossover.md) gives
\(M_N^k=\zeta_k I\), \(|\zeta_k|=1\). Thus any estimate
\(|\operatorname{Tr}M_N^m|\le Ca^m\) for all odd \(N\ge N_0\)
and \(m\ge1\) has \(a\ge c\) (or else take \(m=k\) and let \(k\)
grow). In particular the strict improvement in TRACE-113 does not hold
at \(\tau=0\).

The same return gives a finite bound even at nonzero coupling. The
self-adjoint generator has \(\|A_N\|<8/5\) by the
[Pell covering proof](pell_microscopic_window.md). Use
\(\|e^{i\tau N A_N}-I\|\le |\tau|N\|A_N\|\) and telescope
the \(k\) unitary factors. Then
\[
 |\operatorname{Tr}U_N(\tau)^k|
 \ge N\left(1-\tfrac85kN|\tau|\right).
\]
In particular, whenever \(kN|\tau|\le5/16\), the left side is at least
\(N/2\). Suppose a punctured interval admitted common constants
\(C,N_0,a\) with \(1<a<c\). For arbitrarily large odd \(k\) choose
a nonzero \(\tau\) in the interval with \(|\tau|\le 5/(16kh_k)\).
The proposed bound would force \(C\ge h_k/(2a^k)\to\infty\).
This rules out simultaneous uniformity of \(C,N_0\) and a strict gap
\(c-a\) all the way down to zero; it does not identify which constants
must deteriorate in a particular proof. It does not refute the estimate
for any fixed nonzero \(\tau\).

There is also a weak-limit distinction along shrinking couplings.
The same [covering bound](pell_microscopic_window.md), with \(|\tau|\)
in place of \(\tau\), gives for any fixed unfolded interval of
length \(R\) a hit probability at most \(k(R/N+8N|\tau|/15)\).
Therefore along the odd Pell dimensions with \(kN|\tau|\to0\)
(including zero identically), the shifted local process tends weakly
to the empty process: with probability tending to one, every specified
compact test window is empty. This is a statement about the point
process itself, not just its pair statistic; the unit intensity at
each finite \(N\) does not pass to that limit. The larger bounded
Gaussian-crossover window of FM-002 gives a pair-transform obstruction,
not this empty-process conclusion.

## Sharpened finite Pell witnesses (not a registry promotion)

The covering argument in sections 1–2 of
[the original Pell note](pell_microscopic_window.md), after scalar
centering, extends its bounds on the occupancy at \(h_{203}\) and the
band-two defects at \(h_{197},h_{203}\) to **every real**
\(|\tau|\le(206/125)10^{-80}\), including the negative sign and zero.
The \(h_{207}\) normal-form certificate and later dimensions are
not part of this extension.

Set \(B_N=A_N+I/10\). This rotates every perturbed phase by the same
amount, preserving the trace moduli and the uniformly shifted occupancy.
The [literal position coefficients](seven_oldspace_singular_spectrum.md#1-the-seven-translates-and-their-relative-phases)
give diagonal \(c+(1-c)f\), with \(c=\cos(14\pi q)\) and
\(f=(1+\cos(2\pi q))(1/10+\sin(2\pi q)/100)\in[0,11/50]\).
Thus the diagonal is in \([-1,1]\) and the two midpoint hoppings have
absolute value at most \(4/200\) each. By the Hermitian row-sum
bound \(\|B_N\|\le26/25\). With \(\pi>157/50\), the phase-continuation
argument of section 1 now gives an arc of length at most
\((52/157)|\tau|N\) per original phase, on a circle of length one.
The section-2 enlarged cover consequently has measure at most
\[
 d=k\left(2000/N+(52/157)|\tau|N\right),
\]
which also bounds the length-one occupancy, since its enlargement
uses \(1/N\) instead of \(2000/N\).

At the endpoint of the extended interval, exact rational arithmetic
places \(d\) below \(1/700\) at \(k=197\) and \(7/25\) at \(k=203\).
The original section-2 comparison with \(H\ge1/4\) therefore gives
\(68303/3200>21\) and \(1289/89600>1/100\) for the respective band-two
defects, and the hit probability at \(h_{203}\) is below \(7/25\).
At the prescribed \(\tau=10^{-80}\), the stronger cover caps are
\(1/1200\) and \(17/100\), giving defects at least
\(29327/800>36\) and \(4633/54400>0.08\).

**Same experiment against Sine₂.** At the original coupling and
\(N=h_{203}\) the hit probability is below \(17\%\). In the unit-density
Sine₂ process it is above \(80\%\). For the latter bound, use
the standard sine-kernel gap formula \(\Pr(X=0)=\det(I-K)\) on \([0,1]\),
where \(K\) is a positive contraction of trace one, as the compression
of the band-limited Fourier projection. Testing on the unit constant
and integrating the alternating sinc expansion through degree six gives
\[
 \lambda_1\ge
 2\int_0^1(1-x)\frac{\sin(\pi x)}{\pi x}\,dx
 \ge 1-\frac{\pi^2}{36}+\frac{\pi^4}{1800}
             -\frac{\pi^6}{141120}>\frac34.
\]
It follows that \(\det(I-K)\le(1-\lambda_1)e^{-(1-\lambda_1)}
<\frac14 e^{-1/4}<1/5\): the product over the other eigenvalues is
bounded by the exponential of minus their sum, \(u e^{-u}\) is
increasing for \(0\le u\le1\), and \(e^{1/4}>5/4\).
The [exact arithmetic check](../../computations/verification/coupling_scope_audit/check_finite_pell_range.py)
replays the four cover caps and the numerical part of the Sine₂ bound.
It leaves all archival certificates untouched. These comparisons are
finite at fixed coupling and do not settle the asymptotic question.
