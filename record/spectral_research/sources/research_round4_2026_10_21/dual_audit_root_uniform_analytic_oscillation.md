> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/dual_audit_root_uniform_analytic_oscillation.md`. Embedded SHA256: `beafab75dc06644b22aa2395f6fd05dcc3628ab20d895ccb8e560b093819a9ff`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: uniform oscillation of translated analytic phase differences

21 October 2026. Auditor: the Weyl dual-dynamics branch.

Audited source:
`root_uniform_analytic_oscillation.md`, SHA-256
`5eaae7946e30df2507a870535ec46c2dbc2bce07cc96c8b85366772cab590d31`.
The source was read in full and its hash checked. It was not modified.

## Verdict and scope

**The estimates (1.2) and (1.3) in the audited source are proved as stated.**
The argument gives one finite exponent for the fixed analytic phase, uniformly
in the translation, the oscillation parameter, the amplitude family with a
uniform C1 bound, and the grid denominator. No simple or useful numerical value
of the exponent is asserted or required. No critical gap was found in
Sections 1--5.

Section 6 remains a conditional application, as its own wording states. Its
conclusion follows once the application establishes both the asserted uniform
oscillatory-symbol formula and the exact finite-group twirl/pinching identity.
The analytic lemma supplies neither of those separate inputs.

The rest of this audit reconstructs the nontrivial proof steps independently.

## 1. Uniform nonconstancy after compactifying zero translation

For a centered torus translation $z=r\omega$, set
$$
F_{r,\omega}(x)=\int_0^1\omega\cdot\nabla S(x+sr\omega)\,ds.
$$
The displayed parameter set in the source is closed and bounded in
$[0,1/\sqrt2]\times S^1$, hence compact. Differentiating under this finite
integral shows continuity into every finite Cj space, including at r=0.
Since a real analytic periodic function has analytic extensions in a common
neighborhood of its compact real torus, integrating real translates preserves
analyticity in x. Equivalently, local analytic power series can be differentiated
and integrated uniformly in the indicated compact parameter ranges.

For r positive the Fourier coefficient at the coordinate vector $e_j$ is
$$
\widehat F_{r,\omega}(e_j)
=\widehat S(e_j)\frac{e^{2\pi i r\omega_j}-1}{r}.
$$
On $[-1/2,1/2]$, concavity of sine gives
$|e^{2\pi iu}-1|=2|\sin\pi u|\ge4|u|$.
At least one $|\omega_j|$ is at least $1/\sqrt2$. Thus, putting
$c_0=\min_j|\widehat S(e_j)|>0$,
$$
\max_j|\widehat F_{r,\omega}(e_j)|\ge2\sqrt2c_0.
$$
At r=0 the exact coefficient is $2\pi i\omega_j\widehat S(e_j)$, so
the same lower bound persists directly. Every member of the family is therefore
nonconstant. The same member also has mean zero, although nonconstancy alone
suffices for the derivative argument.

If all its positive-order derivatives vanished at one point, its analytic
Taylor series there would be constant. This forces constancy on the connected
torus. One can see the continuation step without importing a separate theorem:
the set where the function has that fixed constant value on a neighborhood is
open; at a limit point all positive-order derivatives vanish by continuity, and
the analytic expansion makes that set open there as well. It is therefore
closed and nonempty, hence is the whole connected torus.

For each positive-order multi-index alpha and positive integer n, the set
where $|\partial^\alpha F|>1/n$ is open in the compact parameter-position
product. These sets cover it by the preceding paragraph. A finite subcover
has a maximum derivative order M and a positive minimum threshold c. This
proves the uniform finite-order inequality (2.3) of the source. It does not
silently infer a uniform order merely from pointwise analyticity.

## 2. Directional reduction and C1 localization

At a fixed derivative order m, define
$$
p(t)=D_{(1,t)}^m F
=\sum_{a=0}^m\binom ma t^a
 \partial_1^{m-a}\partial_2^aF.
$$
Evaluation at the distinct points $0,1,\ldots,m$ gives an invertible
Vandermonde matrix. Passing to the normalized directions
$v_j=(1,j)/\sqrt{1+j^2}$ only multiplies its rows by nonzero constants
$(1+j^2)^{-m/2}$. Its finite inverse gives the stated bound for the partial
derivatives in terms of these finitely many directional derivatives.

The compact finite-order inequality thus yields, near every parameter-position
pair, a fixed direction and order whose derivative stays bounded away from
zero. Finite refinement gives product neighborhoods with their smaller closures
inside the original ones. On the compact metric parameter set, continuous
cutoffs supported in such relative open neighborhoods exist, for example from
distance to their complements after taking one more smaller neighborhood. In
the coordinate balls, the usual smooth bump functions exist. Products of the
two cutoffs have a sum uniformly bounded below on the compact product; dividing
by this sum produces a finite partition of unity.

Its derivatives in x of every fixed order are uniformly bounded because its
denominator has a positive minimum and its numerator derivatives are continuous
and bounded on the compact product. No parameter derivative is taken. Therefore
even an amplitude family with no continuity in z still has uniformly bounded
localized C1 norms.

Choose each ball inside a flat coordinate chart. Slicing the ball along its
selected direction gives intervals of uniformly bounded length and a uniformly
bounded transverse range. The selected phase derivative stays nonzero along
each full interval, since it stays nonzero on the entire ball. The localized
amplitude is supported strictly within the ball. Its supremum norm and the
one-dimensional integral of its first derivative are uniformly bounded by a
constant times the original C1 bound. These facts justify both Fubini slicing
and the uniform application of the one-dimensional estimate.

## 3. Independent reconstruction of the sublevel and oscillatory bounds

Assume $|\phi^{(m)}|\ge c'>0$ on an interval and m is at least two. Put
$g=\phi'$ and $r=m-1$. All needed derivatives exist here because the
application phases are analytic.

Let $E=\{|g|\le\eta\}$ have positive length L. Its Lebesgue measure has
no atoms. Choose r+1 points in E at approximate successive measure quantiles
$(j+1)L/(r+2)$, for $j=0,\ldots,r$. The approximation can be made small
enough that adjacent points have distance at least
$\delta=L/[2(r+2)]$: the measure lying between adjacent quantiles is a
lower bound for their Euclidean separation. Endpoint approximations suffice
if a quantile is attained at a gap endpoint.

For these ordered points $x_0<\cdots<x_r$, the interpolation formula gives
$$
|[x_0,\ldots,x_r]g|
\le\eta\sum_{j=0}^r
 \frac1{\prod_{i\ne j}|x_j-x_i|}
\le\frac{2^r\eta}{r!\delta^r}.
$$
Subtracting the degree-r interpolation polynomial and applying Rolle r times
gives $[x_0,\ldots,x_r]g=g^{(r)}(\xi)/r!$ at an intermediate point.
Its modulus is at least $c'/r!$. Hence
$$
L\le4(r+2)(\eta/c')^{1/r}.
$$
This supplies, in particular, an explicit permissible constant in the source's
sublevel estimate (4.1).

Since $g^{(r)}$ never vanishes, $g'$ has at most r-1 distinct zeros:
r distinct zeros would force a zero of $g^{(r)}$ by Rolle. Thus g is
monotone on at most r intervals, and their intersections with $|g|>\eta$
give at most 2r intervals of one sign and away from zero.

On each such interval, integration by parts using
$e^{i\nu\phi}=(i\nu g)^{-1}(e^{i\nu\phi})'$ gives boundary and amplitude
derivative terms bounded by a constant times
$(\nu\eta)^{-1}(\|A_0\|_\infty+\|A_0'\|_1)$. Its remaining phase term
obeys the same estimate because
$\int |g'|/|g|^2\le1/\eta$ on a monotone interval of one sign. Summing
over the bounded number of intervals proves (4.2).

On E the integral is bounded by $\|A_0\|_\infty |E|$. Choosing
$$
\eta=(c')^{1/m}\nu^{-(m-1)/m}
$$
makes both estimates proportional to $(c'\nu)^{-1/m}$. This proves (4.3)
with constants depending only on the selected finite phase data.

For m=1, one integration by parts on the whole interval yields the bounds
$(\nu c')^{-1}$ for its boundary and amplitude derivative terms. The phase
term is at most
$\nu^{-1}(c')^{-2}\|A_0\|_\infty |I|\sup_I|\phi''|$.
The final two factors are uniformly bounded by the compact analytic family
and the bounded coordinate intervals. Thus the source correctly avoids any
unproved monotonicity assertion for the first-derivative case.

After substituting $\nu=\lambda\eta(z)$, the finite localization has orders
$m_j\le M$. If $\nu\ge1$, then $\nu^{-1/m_j}\le\nu^{-1/M}$.
For $\nu<1$, the trivial absolute integral bound gives the required estimate
after increasing the fixed constant. The same reasoning includes z=0, where
the right side is a constant times the amplitude bound. This verifies (1.2).

## 4. The grid average is genuinely independent of its denominator

Represent a nonzero grid translation by a centered integer vector j divided
by d. A shell $\max(|j_1|,|j_2|)=m$ contains at most 8m points, and its
distance to the origin is at least $m/d$. For $\epsilon=1/M\le1$,
$$
\frac1{d^2}\sum_{z\ne0}\eta(z)^{-\epsilon}
\le8d^{\epsilon-2}\sum_{m\le d/2+1}m^{1-\epsilon}
\le C_\epsilon.
$$
The last bound follows by comparison with the integral of $t^{1-\epsilon}$,
whose upper endpoint is a constant times d. For d=1 the sum is empty.
Combining this with
$(1+\lambda\eta)^{-\epsilon}\le\lambda^{-\epsilon}\eta^{-\epsilon}$
for nonzero eta proves (1.3), with no d-dependent constant. This checks the
improvement over replacing all distances by the minimum nonzero distance.

## 5. The exact additional identity needed in the application

Suppose a finite unitary conjugation group of order $d^2$ has twirl
$$
\mathcal D(X)=d^{-2}\sum_z T_zXT_z^*.
$$
It is an orthogonal projection for the Hilbert--Schmidt inner product: group
averaging gives idempotence, and averaging inverses gives self-adjointness.
If in the application it equals the proposed block pinching
$\sum_\chi P_\chi X P_\chi$, then, for the unitary kick E,
$$
\frac1N\|\mathcal D(E)\|_{\rm HS}^2
=\frac1{d^2}\sum_z\frac1N
 \operatorname{Tr}(E^*T_zET_z^*).
$$
The z=0 term is exactly $d^{-2}$. If each other normalized trace has the
stated uniform oscillatory representation and a uniform $O(N^{-1})$ error,
the proved grid lemma gives
$d^{-2}+C N^{-\epsilon}+O(N^{-1})$, which has the claimed form because
$\epsilon\le1$. Taking absolute values before bounding nonzero terms is
valid for this upper bound on the nonnegative left side.

The original problem must verify the relevant conjugation group, the asserted
pinching identification, the fixed phase with the two nonzero Fourier
coefficients, and the uniform amplitude/remainder properties. Those are
separate from the audited analytic lemma. The source labels its last section
conditional, so this is a boundary of the result rather than a flaw in its
proof.
