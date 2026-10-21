> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_pressure_audit.md`. Embedded SHA256: `3b05733fee9eaee5a4f4a4b508ccc52b8bd6d714be2cb2fca4c9b191cd51feb2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit: strict pressure gap and actual quantum traces

Date: 20 October 2026. The parameter is exactly `tau=10^-80`. This audit
concerns the original matrices, not an averaged or conjugate comparison
family.

## 1. Frozen inputs and verdict

| Input | SHA-256 |
|---|---|
| `fermionic_pressure_transfer.md` | `90ebc84c3c9fb7c049a1a9d11e0d5dcb72c4fc89b362da3f848521a7bca79756` |
| `fermionic_resolvent_frame.md` | `1e88189aa0192786ad4947091079efa93079aad8fe9a7194a00692c0fccb184f` |
| `../research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` |
| `../research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |

**Verdict: PASS.** The strict classical gap, its all-time quantum
consequence, the stated Pell exponents, and the complete exponential
trace-sum bound are justified. No bound for the required microscopic
pair statistic is supplied by this argument. This boundary is correctly
stated in the input.

The audited pressure file includes its author's correction of the
entropy paragraph: the identity on the suspension coordinate is treated
by approximation of arbitrary finite partitions by product partitions,
not by claiming a finite generating partition for the identity.

Write `lambda=3+2sqrt2`, `L=((3,-4),(-2,3))`, and let `Psi` in this
file mean the physical forward map `phi_a^(-tau/(2pi)) composed with L`.
It is the inverse of the Egorov map used in the arithmetic-sector notes.
Keeping this convention distinction explicit removes a possible sign
ambiguity, but changes none of the periodic unstable multipliers or
pressure assertions under audit.

## 2. The two Green operators give an actual conjugacy

In the eigen-coordinates of `L`, its two eigenvalues are `lambda` and
`rho=lambda^-1`. For a periodic continuous forcing `g`, the stated
operator has components

$$
(\mathcal G_F g)^u=-\sum_{j\ge0}\lambda^{-j-1}g^u\circ F^j,
\qquad
(\mathcal G_F g)^s=\sum_{j\ge1}\rho^{j-1}g^s\circ F^{-j}.
$$

Uniform convergence proves continuity; index shifts prove
`(G_F g) composed with F-L(G_F g)=g`. The unstable geometric sum is
`1/(lambda-1)`, and the stable one is `1/(1-rho)`. Thus the asserted
maximum-coordinate norm bound `K=(1-rho)^-1<1.21` is correct. The same
calculation works for bounded two-sided sequences. Its solution is unique
because a nonzero solution of the homogeneous equation grows in at least
one time direction.

The lift `Psi=Lx+v(x)` has `||Dv||<10^-69` in these coordinates. Therefore
`w -> G_L[v composed with (Id+w)]` is a contraction of the entire complete
space of continuous periodic functions. Its fixed point yields
`H L=Psi H`, with `H=Id+w`. No derivative of `w` is required.

The separate explicit construction `G=Id+G_Psi(-v)` gives
`G Psi=L G`. These formulas alone would be semiconjugacies, so their
inverse verification matters. First `GH` commutes exactly on lifts with
`L`; its bounded periodic displacement `e` satisfies
`e(L^n x)=L^n e(x)` for every integer `n`, hence vanishes. Thus `GH=Id`.
For `z=HG(y)`, the identity `G Psi^n(z)=G Psi^n(y)` makes
`delta_n=Psi^n(z)-Psi^n(y)` uniformly bounded by `2||G-Id||`. Its recurrence
is

$$
\delta_{n+1}-L\delta_n
=v(\Psi^n z)-v(\Psi^n y).
$$

The bounded-sequence Green bound gives
`||delta||<=K||Dv||||delta||`, so `delta=0` and `HG=Id`. All lift
identities are exact; no integer displacement is discarded. Equivariance
then gives inverse torus homeomorphisms.

The elementary transported dynamical properties also check out. For the
linear map, sufficiently small torus orbit differences have no integer
jumps because `(1+||L||)epsilon` is smaller than the shortest lattice
vector. Two-sided boundedness then proves expansivity. Rational points
are periodic. Fourier mixing follows because the images of every nonzero
integer frequency under `L^T` eventually leave each finite set; the stable
eigendirection contains no such frequency. Approximation by trigonometric
polynomials gives mixing of Haar measure, and hence topological mixing.
A dense orbit follows, for example, by applying the Baire theorem to the
open dense sets `union_(n>=0) L^-n O` for a countable base of open sets.

For a small one-sided Bowen ball of length `m`, the same absence of
integer jumps gives side lengths proportional to `lambda^(-m)` and one
in eigen-coordinates. The area comparison using disjoint half-radius
balls and a maximal separated covering proves entropy `log lambda`.
Uniform continuity of the conjugacy and its inverse transports entropy,
expansivity, and topological mixing without requiring a differentiable
conjugacy.

## 3. Published inputs were read directly

The primary source checked is R. Bowen and D. Ruelle,
*The Ergodic Theory of Axiom A Flows*, Invent. Math. 29 (1975), 181–202,
DOI <https://doi.org/10.1007/BF01389848>, complete author-hosted article:
<https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B42%5D.pdf>.

The locations and uses are as follows. The variational principles for
maps and flows occur on pages 185–186. Theorem 3.3 on page 187 gives
uniqueness and a lower Gibbs estimate for a Hölder potential on a basic
hyperbolic set. Lemma 4.1 on page 189 provides the needed Hölder property
of the infinitesimal geometric potential; Lemma 4.2 there is the volume
estimate using the unstable Jacobian. Proposition 4.4(b) on page 190
sets its pressure to zero on an attractor. Theorem 5.1 and Remark 5.2
on pages 191–192 identify a smooth invariant probability volume with
the geometric equilibrium state in the Anosov case. These statements
do not impose mixing of the suspension flow. The proof below needs no
unstated upper Gibbs estimate and no strict-convexity theorem for pressure.

## 4. Suspension, volume, and metric conventions

The mapping torus of the smooth diffeomorphism `Psi` is a smooth compact
manifold, with smooth nonvanishing vertical vector field. The stable and
unstable bundles supplied by the explicit cone construction suspend to
its stable and unstable bundles. During bounded fractional times all
derivative norms and inverse norms are bounded by compactness. Thus the
integer-time uniform contraction and expansion give flow hyperbolicity.

Dense periodic points and a dense base orbit give dense closed flow
orbits and a dense flow orbit. The entire manifold is locally maximal
and is an attractor by taking its neighborhood to be the entire manifold.
There are no stationary points. Consequently all basic-set and attractor
hypotheses of the cited source hold. No topological mixing of the
constant-roof flow is asserted.

The form `dq wedge dp wedge ds` glues because `det DPsi=1`; it defines
a smooth invariant probability volume. A smooth scalar conformal change
of any smooth metric can realize this prescribed volume form. Metric
changes do not affect the relevant periodic unstable products. More
explicitly, if unstable vector norms differ by the positive factor
`exp u(x)`, the one-step logarithm changes by
`u composed with Psi-u`. Its invariant-measure integrals and periodic
sums are unchanged.

With the chosen cross-section metric, the chain rule and gluing give

$$
\int_0^1\chi(F^t[x,0])\,dt=-\varphi(x),
\qquad
S_m\varphi(x)=\log\Lambda_m(x)
\quad(x\in\operatorname{Fix}\Psi^m).
$$

This matches the `Lambda_m` in the exact quantum modulus estimate. The
positivity of its eigenvalue, rather than only its absolute value, follows
from the verified invariant cone and positive coordinate expansion.

Every flow-invariant probability is `mu times ds` on the measurable
fundamental domain. To verify this, invariance under small vertical shifts
makes the mass of `E times I` proportional to the length of `I`. These
proportionality constants define `mu`; crossing the gluing implies its
`Psi` invariance. The section has zero mass since its distinct time
translates are disjoint. The converse follows directly from the gluing.

The time-one map is measurably `Psi times Id`. For finite product
partitions the entropy of the iterated join is the base entropy plus one
fixed vertical-partition entropy. For an arbitrary finite partition `P`,
finite rectangle approximations supply a finite product-grid partition
`Q` with `H(P|Q)<epsilon`. The chain rule gives

$$
H\!\left(\bigvee_{j<n}(F^1)^{-j}P\right)
\le H\!\left(\bigvee_{j<n}(F^1)^{-j}Q\right)+n\epsilon.
$$

Invariance ensures the same conditional entropy at every lag. Dividing
by `n`, then taking the supremum and `epsilon` to zero, proves the upper
entropy bound; unsplit vertical base partitions give the lower bound.
Thus `h_(mu times ds)(F^1)=h_mu(Psi)` without any generator assumption.

These measure, entropy, and potential identities justify precisely

$$
P_F(t\chi)=P_\Psi(-t\varphi),
\qquad P_\Psi(0)=\log\lambda,
\qquad P_\Psi(-\varphi)=0.
$$

## 5. Why the midpoint inequality is strictly improved

The fixed point `(0,0)` has Hessian
`diag(-19606 pi^2/125,0)`. Its Hamiltonian derivative is nilpotent,
so its exact flow derivative is the identity plus its linear-time term;
there is no neglected quadratic-time remainder. Multiplication by `L`
gives

$$
\operatorname{Tr}D\Psi(0,0)
=6+39212\pi\tau/125>6.
$$

Area preservation and the positive unstable eigenvalue then give
`Lambda_0>lambda`, since `u+u^-1` is strictly increasing for `u>1`.

Let `P_*=P_Psi(-varphi/2)`. The variational principle gives
`P_*<=log(lambda)/2`. If equality held, an equilibrium state at the
midpoint would have zero deficit in both endpoint variational bounds,
because the two nonnegative deficits average to zero. Uniqueness would
make it both the zero-potential equilibrium state and the geometric
equilibrium state. The latter is the smooth invariant volume.

At the period-one orbit of `(0,0)`, the lower Gibbs estimate for zero
potential and the upper volume estimate would consequently give, for
one fixed sufficiently small radius and every positive integer `m`,

$$
c_e\lambda^{-m}
\le m_F(B_m([0,0],e))
\le C_e\Lambda_0^{-m}.
$$

This contradicts `Lambda_0>lambda`. It proves the strict upper inequality
without invoking a cohomology classification of potentials. For the
lower inequality, coordinate expansion greater than five differs from
the metric expansion only by a bounded coboundary. Every invariant
measure therefore has `integral varphi>=log 5`. At the geometric
equilibrium state, entropy equals this integral since its pressure is
zero. Evaluating the midpoint functional gives `P_*>=log(5)/2>0`.

Thus

$$
\Delta=\tfrac12\log\lambda-P_*>0
$$

is a genuine fixed number for the specified `tau`. The proof gives
strict positivity, not an explicit numerical lower bound.

## 6. Periodic sums and the all-time quantum threshold

Distinct points fixed by `Psi^m` are separated in the length-`m` orbit
metric at any sufficiently small expansivity scale. Otherwise their
closeness during one period would repeat in both time directions,
contradicting expansivity. Their positive weighted sum is therefore one
of the sums bounded by the separated-set partition supremum. The
definition of pressure gives

$$
\limsup_{m\to\infty}\frac1m\log
\sum_{x\in\operatorname{Fix}\Psi^m}\Lambda_m(x)^{-1/2}
\le P_*.
$$

The direction of this inequality is correct: the fixed-scale partition
limsup is at most the pressure after letting the separation scale tend
to zero. For each fixed `eta>0` the finite initial range is absorbed
into one constant. No periodic-orbit asymptotic or uniform transfer
spectral gap is needed here.

The all-time exact amplitude bound implies pointwise

$$
\lambda^{-m/2}|\Gamma_h(x,m)|
\le e^{C_{\rm mod}mh^2/2}\Lambda_m(x)^{-1/2}.
$$

Combining this with the pressure upper bound using `eta/2`, choose one
odd-dimension threshold so that `C_mod h^2/2<=eta/2` and the earlier
exact all-time formula is valid. This threshold is independent of `m`.
The factor `exp(C_mod m h^2/2)` is absorbed in an exponential rate;
it is never approximated by `1+o(1)` uniformly in time. In particular
the proof does **not** require `mh^2` to be small.

The resulting estimate is exactly

$$
|\operatorname{Tr}U_N^m|
\le C_\eta e^{(P_*+\eta)m}+2(0.421)^m
\quad\text{for every }m\ge1
$$

at one threshold for each fixed `eta`. Taking `eta=Delta/2` and absorbing
the decaying residual gives a growth base
`a_eff=sqrt(lambda) exp(-Delta/2)<sqrt(lambda)`.

## 7. Pell exponents and their precise scope

The sequence

$$
N_r=(\lambda^r-\lambda^{-r})/(4\sqrt2)
$$

obeys the integral recurrence `N_(r+1)=6N_r-N_(r-1)` with `N_0=0,N_1=1`.
Its parity is the parity of `r`. The identity
`S^r=t_r I+2N_r J`, `J^2=2I`, `t_r^2-8N_r^2=1`, proves
`S^(2r)=I mod N_r`; exact Weyl Egorov and elementary Weyl irreducibility
then prove the stated bare-cat scalar return. This last fact is only the
reference return time, not an assertion about the perturbed matrix.

At that time the actual bound is

$$
|p_{2r,N_r}|\le C\lambda^r e^{-\Delta r}.
$$

Since
`lambda^r=4sqrt2 N_r+lambda^-r` and
`log N_r=r log lambda-log(4sqrt2)+o(1)`, division by `N_r` gives precisely
the stated exponent `delta=Delta/log lambda`. Using any smaller fixed
`eta` in the preceding theorem permits every
`delta<2Delta/log lambda`. The constants and the dimension threshold may
depend on that chosen exponent; the input states this correctly.

The Hilbert–Schmidt identity follows by direct expansion:

$$
\min_{|\omega|=1}N^{-1}\|V-\omega I\|_{\rm HS}^2
=2-2|\operatorname{Tr}V|/N.
$$

This controls the first reference return `2r`. It does not assert a
comparable small normalized trace at all positive multiples of `2r`.
For larger multiples the exponential bound can already exceed the
unitarity bound.

## 8. Positive frame identity and the complete infinite tail

The separately audited frame argument works for every finite unitary
matrix. On `L^2(mu_N)`, with
`mu_N=N^-1 sum_j delta_(zeta_j)`, the vectors `v_j(zeta)=zeta^j` have
Gram matrix `G_L=(c_(k-j))`, `c_m=p_m/N`. The norm of the analysis
operator gives

$$
\sum_{j<L}|\langle v_j,f\rangle|^2
\le\lambda_{\max}(G_L)\|f\|^2.
$$

Apply this to `f(zeta)=(1-r exp(it) zeta)^-1` and integrate in `t`.
Absolute geometric convergence justifies angular Parseval, giving
`sum_(m>=0) r^(2m)|c_(m-j)|^2` for the `j`th term and
`1/(1-r^2)` for the norm. Splitting at `m=j` and summing the two finite
geometric progressions proves exactly

$$
(1-r^{2L})(1+S_N(r))
+\sum_{n=1}^{L-1}(1-r^{2(L-n)})|c_n|^2
\le\lambda_{\max}(G_L),
\quad S_N(r)=\sum_{m\ge1}r^{2m}|c_m|^2.
$$

The normalization and the extra nonnegative finite sum are correct,
including repeated eigenvalues. The Hermitian row bound gives
`lambda_max(G_L)<=1+(2/N)sum_(m<L)|p_m|`. With any all-time growth base
`a>1`, take

$$
L=\left\lfloor
\frac{\log N-2\log\log N}{\log a}\right\rfloor.
$$

The row error is `O((log N)^-2)`, while for `r=exp(-s/N)` the leading
denominator is `1-r^(2L)~2sL/N`. Therefore

$$
\limsup_{N\to\infty\atop N\ \mathrm{odd}}
\frac{\log N}{N}
\left[\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}|p_m|^2\right]
\le\frac{\log a}{2s}.
$$

For the pressure bound use `a=exp(P_*+eta)` and let the fixed `eta`
decrease to zero only after the `N` limsup. This proves the constant
`P_*/(2s)<log(lambda)/(4s)` claimed in the pressure file. All positive
times, including the infinite tail, were included before any limit.

## 9. What remains unproved

The new gap quantitatively distinguishes the actual family from a smooth
conjugate of the bare cat at its first Pell return. The positive frame
argument converts it into a strict constant improvement in a proved
`N/log N` bound for the normalized full exponential trace sum.

That bound still permits divergence. It does not prove even

$$
\sup_{N\ \mathrm{odd}}\frac1{N^2}
\sum_{m\ge1}e^{-2sm/N}|\operatorname{Tr}U_N^m|^2<\infty
$$

for one fixed `s>0`. The full `H_diag` requires more than this pair bound:
the signed weighted sums of products of traces at every fixed order and
arbitrary fixed Fourier support remain unevaluated. No phase-cancellation
estimate is introduced as a premise in the pressure proof.
