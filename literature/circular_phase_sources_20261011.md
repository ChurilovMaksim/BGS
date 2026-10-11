# Sources, convention checks and proof audit

## Primary sources checked on 11 October 2026

1. Andrei Okounkov and Grigori Olshanski,
   *Asymptotics of Jack polynomials as the number of variables goes to infinity*,
   arXiv:q-alg/9709011, v1, 5 September 1997.
   https://arxiv.org/pdf/q-alg/9709011

   Section 1.1, equations (1.2)–(1.3), defines integer Laurent signatures
   and identifies normalized Jack polynomials with compact spherical
   functions. Their parameter theta equals 1/alpha in these notes.
   Theta = 1/2 corresponds to U(N)/O(N), and theta = 2 to U(2N)/Sp(N).
   Section 2.3 gives positive branching coefficients; Section 4 explicitly
   uses nonnegative Laurent coefficients. Our direct triangular proof
   avoids depending on that positivity as an unexplained lemma.

2. Sho Matsumoto,
   *Moments of characteristic polynomials for compact symmetric spaces
   and Jack polynomials*, arXiv:math/0608751, v3, 26 July 2007.
   https://arxiv.org/pdf/math/0608751

   Sections 6.2 and 6.3 identify the COE and CSE circular densities.
   CSE eigenvalues are doubled, with N distinct eigenvalues and beta = 4.
   The source uses a contiguous rather than interleaved symplectic matrix;
   a basis permutation gives the convention here.
   Characteristic-polynomial duality can interchange alpha and 1/alpha:
   it must not be confused with the spherical parameter alpha used here.

3. Benedek Valkó and Bálint Virág,
   *Operator limit of the circular beta ensemble*,
   arXiv:1710.06988, v1, 19 October 2017.
   https://arxiv.org/pdf/1710.06988

   Theorem 6 gives the circular-beta point-process limit for every beta>0.
   Theorem 8 gives the periodically lifted finite process. Their scaling
   uses N times the eigenangles; our intensity-one scaling adds 1/(2pi).
   Theorem 1 and Corollary 2 prove a much more quantitative annealed coupling.
   Those estimates are not silently combined into a rate for our arbitrary
   Laplace metric.

4. Tiefeng Jiang and Sho Matsumoto,
   *Moments of traces of circular beta-ensembles*,
   arXiv:1102.4123v2, 22 December 2015; Annals of Probability 43(6),
   3279–3336 (2015).
   https://arxiv.org/pdf/1102.4123

   Lemma 4.2 gives the finite circular Jack norm product. The one-sided
   norm comparison for alpha≥1 works in every polynomial degree; it
   does not require the degree restriction of a two-sided comparison.
   Fixed-order trace limits must not be substituted for growing n~N.

5. Fritz Haake, Hans-Jürgen Sommers and Joachim Weber,
   *Fluctuations and Ergodicity of the Form Factor of Quantum Propagators
   and Random Unitary Matrices*, arXiv:chao-dyn/9906024v1,
   14 June 1999.
   https://arxiv.org/pdf/chao-dyn/9906024

   Equations (14), (21) and (22) already give the exact CUE variance and
   CSE second/fourth cumulants rederived here. Equations (25), (27) and
   (29) describe the CSE limiting curve and critical fourth-cumulant
   correction. The PDF contains a later typesetting date; that does not
   make these results new in 2018 or 2026. Section II computes the first
   four moments and discusses near-Gaussian traces. It does not by itself
   supply our written all-order boundary-layer proof or conditional
   diagonal-phase theorem. Its main ergodicity theorem averages time;
   our averaging variable is independent diagonal phases with Q frozen.
   It calls n=N half the Heisenberg time for CSE, with N distinct pairs.

6. Fritz Haake, Marek Kuś, Hans-Jürgen Sommers, Henning Schomerus and
   Karol Życzkowski, *Secular determinants of random unitary matrices*,
   arXiv:chao-dyn/9603006v1, 12 March 1996.
   https://arxiv.org/pdf/chao-dyn/9603006

   The discussion around Section 4 concerns the fixed-order joint Gaussian
   law for CUE and numerical observations for COE/CSE. It is relevant
   historical context, not a proof that replaces the growing-order,
   critical-normalization calculation here.

## Independent audit

The child jack_phase_audit independently checked the candidate theorem.
It was assigned one proof-audit task, not a search for confirming opinions.

The audit verified:

- the positive pair expansion for Laurent exponents;
- the strict eigenvalue separation under dominance;
- the factor 2N(N-1)/alpha in the constant-coefficient equation;
- the strengthened denominator N+alpha K and the unique sharp mode;
- COE weights 2lambda and K=O(N);
- CSE duplicated weights, paired phases and half trace;
- orthogonality of projected modes, even though their images need not
  remain spectral functions;
- conditional tightness and the finite-ensemble meaning of the rate.

The audit also explicitly rejected extensions to arbitrary non-spectral
functions, to 2N independent CSE phases, to all-size almost-sure convergence
from the variance estimate alone, and to a specified deterministic Fourier
background.

This is an independent mathematical review, not a kernel-checked formal
certificate. The arithmetic Lean draft is separately labelled uncompiled.
The reviewer was a separate reasoning agent, not an external human referee
or a journal peer-review process.

Two further audit passes verified the exact finite cumulant grouping,
partial fractions, their uniform bounds, and the all-order extension.
The latter checked cyclic multiplicity at every fixed r, the complete
Gaussian moment argument, the arbitrary |n−N|=o(N) boundary layer,
conditional tightness and moments, and the quantitative critical block
Taylor estimate. It also checked the CUE shift calculation and the L²
curve argument, pointing out that a true n=0 cell would invalidate L²
convergence. The final written curve uses ceil(Nτ) on τ>0.

## Priority status

A second independent audit checked the full form-factor argument: the
confluent determinant, its Pfaffian integral expansion, inverse-matrix
orientation, repeated-denominator bound for closed walks, coefficient mass
13/4, exact half-integer harmonic mean and the high-frequency plateau.
It also checked the all-degree one-sided Jack norm inequality for COE/CUE.
This audit explicitly distinguishes a supremum of individual mean-square
errors from the mean square of a temporal supremum.

The same primary source Jiang–Matsumoto, arXiv:1102.4123v2
(22 December 2015), Lemma 4.2, verifies the finite circular norm product.
The CSE calculation here derives its needed moment bounds directly, so its
proof does not assume an asymptotic trace CLT or an unverified Pfaffian kernel.

The recent preprint Yun Li, arXiv:2610.01803v1 (1 October 2026), was also
checked: Theorem 1 concerns fixed trace orders. It is not used to infer
Heisenberg-scale convergence. Recentness alone does not close that gap.

A bounded search for Jack constant-coefficient and diagonal-phase contraction
bounds did not locate an identical statement. That is insufficient to claim
a new theorem in the literature. The correct status is: a complete proof
derived and audited in this session, with scientific priority unestablished.

The exact ensemble means and fourth cumulants have positive known priority
in the 1999 source. They are explicitly excluded from any novelty claim.
The additional search for critical CSE traces included high powers,
logarithmic variance and higher cumulants. It located historical Gaussian
discussions and recent fixed-order limits, but did not settle priority
of the exact all-order and frozen-phase formulations. Search absence is
not evidence that these are first results.

## Remaining BGS gap

The theorem concerns a circular-distributed scattering matrix subsequently
frozen. There is still no argument deriving the same conditional local law
for a specified deterministic chaotic propagator from classical mixing
and symmetry alone. In particular the Fourier family's interference sectors
at n proportional to N remain a separate unsolved problem.


## Additional load-bearing references and prior corpus

Tropp, *Freedman’s inequality for matrix martingales*, ECP 16 (2011),
262--270, Theorem 1.1, is used only for the conditional joint-delay stopping
argument. The entry-flat event is not proved by that theorem.
Arratia--Goldstein--Gordon, *Two Moments Suffice for Poisson Approximations*,
Ann. Probab. 17(1) (1989), Theorem 1, supports the birthday collision limit.
The TV convention and the different zero-event factor were checked explicitly.

The deterministic maximal path theorem inherits the actual-map fixed-symbol
mixing/Egorov closure of FM-018 and polar_wkb_quantization_stability.md,
Section 2. The time-average endpoint mechanism and logarithmic RMS transfer
are already in supplement/fixed_map/ergodic-transfer/ergodic_spectral_transfer.md,
Sections 1--4. Its initial-eigenbasis-only counterexample, Section 5, prevents
replacing time-average control by one initial diagonal variance.
Schubert, arXiv:math-ph/0503045, Section 4, Theorem 4 and equations (65)--(70),
is a prior logarithmic quantum-ergodicity antecedent, not an imported microscopic
law. Tanner, arXiv:nlin/0104014, supplies historical phase-ensemble context,
not the growing-ramp proof used here. Haake et al., arXiv:chao-dyn/9603006v1,
and Yun Li, arXiv:2610.01803v1, concern their own fixed-trace regimes.

The 6 October metadata cache is immutable. The 11 October cache retains those
observations, adds seven reviewed primary references and updates exact direct
and transitive impact sets. An offline PASS establishes agreement with that
reviewed cache, not applicability of an uninspected external theorem.
