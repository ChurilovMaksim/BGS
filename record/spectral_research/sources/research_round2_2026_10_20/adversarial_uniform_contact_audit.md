> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_uniform_contact_audit.md`. Embedded SHA256: `27c1f823be45f3e4fd6bc862bd20d9575a9a01e6deeff10d36eb601a9222eb75`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of uniform contact at infinitesimal translations

Research continuation, 20 October 2026.

## 1. Input and verdict

Input: `root_uniform_translation_contact.md`, SHA-256
`257afa4511da2fae8bd9260cc33a654bf045115f80aa0861bb8eae6a4f92347e`.
Its actual-map Fourier and Green inputs were checked in the earlier
audits listed in the same research directory. The companion finite-curve
argument is audited separately in
`adversarial_logarithmic_horizon_audit.md`.

**Verdict: the three claimed assertions pass independent audit:**

1. The stable graphs depend C1 on their real centers with values in
   one fixed holomorphic Banach space.
2. Their comparison family has one positive finite-jet lower bound
   proportional to the size of the translation, uniformly even as that
   size tends to zero.
3. For a nonempty original translated-return set, backward graph error
   is bounded relative to that same size after a fixed number of steps.

The proof below records why separate leaf analyticity and real C1
regularity are not silently substituted for the first assertion.

## 2. A direct graph transform in the weighted holomorphic norm

Write the actual lift in eigen-coordinates as
F(u,s)=(lambda u,rho s)+v(u,s), with rho=lambda^-1 and the perturbation
derivatives tiny on a fixed complex tube. Let

||eta||_* = sup_(0<|t|<R) |eta(t)|/|t|,

for holomorphic eta with eta(0)=0, and restrict to the ball of radius
b=10^-40. The centered inverse graph equation is

gamma(t)=rho[eta(rho t+Delta v_s)-Delta v_u],
Delta v = v(x+t e_s+gamma(t)e_u)-v(x).

This is the correct equation for pulling the graph based at Fx back
to the graph based at x. The stable argument of eta has modulus at
most 0.18|t|, because rho<0.172 and the perturbation derivative is
smaller than 10^-50. For eta=t H with ||H||<=b, Cauchy's estimate on
the interior disk gives |eta'|<=2b there. The map in gamma is a
contraction of size at most rho(1+2b)||Dv||, less than 10^-49.
It preserves the indicated ball.

For a direct change of the input eta, the right side changes by at
most rho*0.18 ||Delta eta||_* |t|. Absorbing the tiny implicit change
in gamma gives a contraction q<1/25. This is stronger than the crude
unweighted estimate rho/4, which would not prove q<1/25. The weighted
norm and the actual 0.18 input ratio are both used here.

## 3. Justification of Banach differentiability

Consider the implicit contraction as a map of real x and the Banach
variables eta,gamma. Differentiation with respect to x produces
differences such as Dv(x+w)-Dv(x), where w=t e_s+gamma(t)e_u.
They are O(|t|), uniformly over the ball. Division by |t| therefore
causes no singularity in the norm ||.||_*.

Input functions are evaluated only on the disk of radius 0.18R.
Evaluation, their first derivative, and any fixed finite number of
their derivatives there are bounded operators from the input Banach
space by Cauchy's estimate. A variation in gamma changes the argument
by O(|t|) in exactly the required norm. These facts give continuous
Frechet derivatives of the implicit map in eta and in the real
center, with locally uniform Lipschitz bounds for those derivatives.
Additional derivatives of v are bounded on a slightly smaller reserved
complex tube by Cauchy's estimate; only a finite bound is needed for
the Lipschitz assertion.

Differentiating the uniformly convergent implicit contraction proves
the derivative formulas for the solved graph transform. Equivalently,
the linearized equation has inverse bounded by the geometric series
for its implicit contraction. The nonlinear remainder is quadratic
in a fixed neighborhood in the displayed holomorphic Banach space,
where all arguments remain inside the reserved tube.

This last point avoids the genuine problem of applying a nonlinear
implicit-function theorem to a growing weighted orbit-sequence space:
such a space would permit complex orbit displacements leaving the
analytic tube. No growing orbit sequences occur in this graph proof.

Let Gamma_(n+1)(x)=G_x(Gamma_n(Fx)), Gamma_0=0. Uniform graph contraction
gives ||Gamma_n-Gamma_(n-1)||<=Cq^n. Their center derivatives obey

D Gamma_(n+1)=partial_x G_x(Gamma_n(Fx))
 + D_eta G_x(Gamma_n(Fx)) D Gamma_n(Fx) DF(x).

Since ||DF||<6 and q<1/25, these derivatives are bounded. Subtraction
of consecutive identities gives

||D Gamma_(n+1)-D Gamma_n||
 <= (6/25)||D Gamma_n-D Gamma_(n-1)||+Cq^n.

The successive differences are summable. Thus the limit is C1 into
the fixed Banach space. Small perturbation derivatives also give a
small uniform bound for D_x gamma_x. Derivative evaluation in t on
any smaller disk is a bounded linear operation, so differentiation
in x commutes with it. This is the particular regularity needed later.

## 4. Global leaves and the finite-translation test

The invariant local graphs give a C1 stable slope sigma(x)=gamma_x'(0).
The field (sigma,1) is globally bounded and Lipschitz on real lifts,
so its integral curves extend over the entire real stable coordinate.
Overlapping the local holomorphic graphs makes these complete graphs
real analytic. Under the equivariant conjugacy they lie in straight
stable fibers. In fact they fill each such fiber: the conjugacy differs
from the identity by a bounded periodic map, so the stable coordinate
of its restriction to a complete graph goes to both infinities.
The injective continuous restriction is therefore onto the straight
stable line. The projected stable leaves are dense.

A translation preserving the foliation acts continuously on the
expanding leaf coordinate H_u. Lattice equivariance gives
A(t+ell n)=A(t)+ell n. Density of ell Z^2 forces A(t)=t+c, and
integration of the periodic part gives c=ell h. The two nonzero
fundamental Fourier coefficients of v_infinity then force h=0 on
the torus.

A single coincident translated germ already implies such a foliation
symmetry. Identity of global real analytic graph functions extends
the coincident interval to the whole real stable axis. Equality of
slopes on that dense leaf then extends by continuity to all points.
C1 uniqueness of integral curves gives the whole foliation symmetry.

## 5. The infinitesimal test: analyticity of the needed derivative

For a constant vector w, put z_w(t)=D_x gamma_x(t)w and
L_x(t)=x+t e_s+gamma_x(t)e_u. On the real interval the tangent identity
is sigma(L_x(t))=gamma_x'(t). The just-proved Banach C1 regularity
allows differentiation in x and gives

D sigma(L_x(t))w = z_w'(t)-partial_u sigma(L_x(t))z_w(t).

Taking w=e_u and rearranging yields

partial_u sigma(L_x(t)) = z_(e_u)'(t)/(1+z_(e_u)(t)).

The denominator stays away from zero on a fixed smaller disk because
the center derivative of gamma is small. The right side is holomorphic.
Substitution into the first identity shows that D sigma(.)w is real
analytic along every stable leaf. Separate real C1 regularity and
leaf analyticity alone would not establish this step.

If D_x gamma_x(.)w vanished identically on one plaque, D sigma(.)w
would vanish on that plaque. Its leafwise analyticity extends the
identity over the connected complete stable leaf. Density and
continuity give D sigma(y)w=0 for every y. Integrating the derivative
along y+t w makes sigma invariant under all translations t w.
The finite-translation test then gives t w=0 on the torus for every
real t. This forces w=0. Thus the infinitesimal comparison family
has no identically vanishing nonzero direction.

## 6. Compactification and uniform contact

The comparison functions are

F_(x,h,z)(t)=gamma_x(t)-z-gamma_(x+h+z e_u)(t),
a=|h|_T+|z|>0.

Away from a=0, the normalized functions F/a form a compact family
by continuous dependence on their compact parameters. For a sequence
with a tending to zero, choose the shortest representative of h and
extract directions h/a -> w, z/a -> z_*. Uniform Frechet Taylor
expansion of the C1 graph map gives convergence in the fixed
holomorphic norm to

-z_* - D_x gamma_x(t)(w+z_* e_u),
with |w|+|z_*|=1.

This proves compact closure in a holomorphic norm, not just pointwise
compactness of real functions. The value at zero is -z_*. If a limit
were identically zero, z_*=0; the infinitesimal test then forces
w=0, a contradiction. For actual nonzero parameters the same value
at zero forces z=0, and the finite-translation test excludes the
remaining case h nonzero.

Consider this compact closure together with the real evaluation point
in a fixed compact subinterval. Derivative evaluations are continuous
on a slightly smaller complex disk. Every member has a nonzero
derivative of some finite order at each point. A finite subcover of
these open nonvanishing conditions yields one integer J and one c>0
such that max_(0<=j<=J)|F^(j)(t)|>=c a. Cauchy's formula bounds all
derivatives through J+1 of F/a uniformly.

The elementary divided-difference sublevel proof then gives

length{|F|<=epsilon} <= C min(1,(epsilon/|h|_T)^(1/J)).

Perturbations are controlled as follows. If their C^J norm is at most
(c/2)|h|_T, their derivatives cannot reduce the preceding maximum
below c a/2, since a>=|h|_T. It suffices that their derivatives through
J+1, divided by a, stay bounded. This is the exact normalization
under which the perturbed sublevel argument is uniform. A stronger
bound after division by |h|_T is also sufficient, and is supplied by
the relative backward estimate in its range of use.

## 7. Relative backward error and its quantifiers

Assume that the ORIGINAL small-return set is nonempty, so at least
one actual y satisfies
dist(F^r(y+h),F^r(y)-g)<=epsilon. Triangle inequality and ||DF||<6 give

|g|_T <= 6^r |h|_T + epsilon.

All distances may be taken in the fixed eigen-coordinate torus norm;
changing to another fixed norm only changes harmless constants.
The inequality is derived before any enlargement to a union of tubes.
An arbitrary intersection with such an enlarged tube does not supply
the premise and would not justify the inequality.

At a center z on the finite target stable segment, its translate by
-g has graph gamma_z based at z-g. The genuine stable graph at that
same center is gamma_(z-g). The C1 holomorphic dependence gives
initial difference at most C|g|_T, uniformly in the center. Iterating
the inverse graph transform along the same backward center orbit
and applying Cauchy's estimate gives C^j error <=C_j8^-r|g|_T.
The stronger available q^r is not needed. Thus

error <= C_j(6/8)^r |h|_T + C_j8^-r epsilon.

If epsilon<=c_0|h|_T, division by |h|_T leaves an exponentially
decaying bound with constants independent of h,g. A single r_0
therefore makes the C^J error small enough to preserve the uniform
finite-jet lower bound. The same calculation for J+1 supplies the
normalized upper bound required in Section 6. Larger epsilon is the
trivial range for the eventual relative sublevel estimate.

The subsequent tube radius can be 6^r epsilon without changing this
error calculation. It was epsilon in the original return relation
that bounded g. Finite curve counting must still be performed, as
in the companion logarithmic-horizon proof. Extending a local graph
to the complete dense leaf is legitimate for jets and is illegitimate
as a replacement target in that counting.

## 8. Boundary of the verified result

The contact order and constants depend on the one actual analytic
map at tau=10^-80 and do not depend on an arithmetic denominator.
This audit validates the classical input for such uniformity. It
does not itself supply the additional quantum trace application,
nor a lower bound for every eigenphase pair's arithmetic-sector
matrix-element weights. In particular it does not establish H_diag.
