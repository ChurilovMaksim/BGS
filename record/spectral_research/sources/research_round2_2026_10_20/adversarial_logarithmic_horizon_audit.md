> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_logarithmic_horizon_audit.md`. Embedded SHA256: `342899a923a09e459865611299dbf9a2162473e439f39646d167a914fcb28341`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the fixed-divisor logarithmic horizon

Research continuation, 20 October 2026. This audit checks the actual
arguments and constants. It does not use the author's or another
reviewer's verdict as an input.

## 1. Frozen inputs and conclusion

The principal input is `arithmetic_iterated_logarithmic_horizon.md`,
SHA-256
`37cae903cc22d77e04ba9848f00fdfd4f19920e9c3a22381de92e965588ce8c6`.
Its imported cutoff calculation was checked against Sections 3 and 5 of
`arithmetic_iterated_effective_horizon.md`, SHA-256
`9739e62cc9a4282d39b379c50835f05fd3d46d664663cf6032b3337857751768`.
The all-iterate Fourier input has SHA-256
`c8e02b81819350ab52e7bc3dd791ffbeb1ae1a2192a9a99f1168c4c56d7123e2`.

**Conclusion: the stated fixed-divisor theorem passes this audit.**
For every fixed odd d there is an integer M_d such that the exact sector
correlations differ from d^-4 by O_d(N^(-1/(384 M_d))), uniformly for
1 <= |r| <= floor(log N/(1024 M_d)). This supplies the full-commutant
variance O_d(1/log N) and the stated uniform weighted spectral windows.
It does not give an unweighted pair count or H_diag.

The following points record independent checks of the places where an
unjustified geometric or uniformity claim could change that conclusion.

## 2. Analytic curves, global graphs, and area charts

In eigen-coordinates the map is F = diag(lambda,mu) + G, with
lambda = 3+2 sqrt(2), mu = lambda^-1, and the first two derivatives of
G and of the analogous inverse-map perturbation bounded by 10^-60 on
one fixed complex tube. The finite Fourier estimate for the second
derivative of the vector field is valid: the stated majorant is
2 (59/50) 9 (2 pi 10)^2 < 10^5. The factor two bounds the exponential
growth of all Fourier terms on the chosen tube. The flow and coordinate
changes leave an enormous margin before the bound 10^-60.

For the forward stable Lyapunov--Perron equation the stable Green bound
at weight eta=1/4 is 1/(eta-mu), which is less than 20. It is not the
unweighted bound 5/4. The input uses the correct value. The unstable
Green bound is 1/(lambda-eta)<1. These estimates give a contraction on
the specified complex sequence ball. Holomorphic dependence on the
stable parameter follows by uniform convergence of the iterates.

The real construction extends to every real stable coordinate. This
does not require a large complex tube: real G is globally Lipschitz,
so the same real sequence equation is a contraction on a ball whose
radius is proportional to the real initial stable coordinate. Its
solution decays. Conversely, a bounded real difference orbit satisfies
the same Green equation, and its difference from another such orbit
with the same initial stable coordinate is bounded by
(1-mu)^-1 ||DG|| times itself. It is therefore unique. Re-centering the
real graph at any of its points agrees with the uniformly analytic
local graph. The complete leaf is consequently one real analytic graph
over the entire real stable axis. This is the property needed for
analytic continuation in Section 4.

Continuity in the center is proved component by component. Each finite
iteration and fixed component is continuous in the center; infinite
Green sums have uniform geometric tails. Contraction then gives uniform
convergence of the zeroth component. No continuity of the full chaotic
orbit sequence in a weighted sup norm is assumed. Cauchy's formula
gives continuous graph jets on smaller disks.

For the stable projective transform, the derivative with respect to
the slope is exactly 1/(lambda+alpha-c sigma)^2 because det DF=1.
It is at most 1/25 in the stated cone. Differentiation in the base
therefore has contraction factor at most 6/25, while coefficient
derivatives are O(10^-60). The successive derivative differences form
a summable sequence, proving that the line field is C1. Integrating
the field (sigma,1) gives the transverse Jacobian
exp(integral partial_u sigma), between 1/2 and 2 on the fixed plaques.
This proves the area disintegration used later. No differentiability
of the conjugating homeomorphism is needed here.

## 3. Conjugacy and exclusion of translated germs

The two-sided Green construction produces inverse, equivariant
homeomorphisms. To check the inverse claim, their composition commuting
with the diagonal linear map has bounded displacement v with
v(D^n z)=D^n v(z) for every integer n. The unstable coordinate is killed
by positive n and the stable coordinate by negative n. For the other
composition, the difference of its two-sided orbits is a bounded
solution whose forcing is at most ||DG|| times the difference. The
Green norm again gives uniqueness.

The expanding coordinate of the inverse conjugacy is the exact
discounted limit H_u = ell_u x + v_infinity. Its fibers are the complete
stable graphs: equality of expanding coordinates gives convergence
under the inverse conjugacy, while convergence forces equality of those
coordinates. Equivariance implies uniform continuity on lifts, since
each conjugacy differs from the identity by a continuous periodic map.
The projected complete graphs are dense, being images of irrational
straight stable lines.

Suppose translation by h takes one stable germ into another. Both
complete lifted curves are real analytic graphs over the full real
stable axis. The one-dimensional identity theorem extends their
equality from the germ to the whole line. Equality of the stable slope
under h then holds on a dense projected leaf and hence everywhere.
The C1 vector field has unique integral curves, so this translation
preserves the entire stable foliation.

On the lifted leaf coordinate it induces a continuous function A with
A(t+ell_u n)=A(t)+ell_u n. Since ell_u Z^2 is dense, A(t)=t+c.
Integration of the periodic part gives c=ell_u h. Thus
v_infinity(x+h)=v_infinity(x). The two independently proved nonzero
Fourier coefficients at e_1 and e_2 imply h is integral. This excludes
every nonzero torus translation, without a genericity assumption.

## 4. Finite contact and its stability

The shifted comparison family is

L(t)=gamma_z(t)-Delta_u-gamma_(z+h+Delta)(t-Delta_s).

The stable argument t-Delta_s is essential: its omission would compare
the wrong target leaf. In the specified parameter range its modulus
is below 3a_0, safely inside the disk of analyticity. The family is
compact with all jets on smaller disks and contains no identically
zero function. Compactness with the real evaluation point gives one
finite derivative order J_h and a strictly positive minimum b_h of
the maximum of derivatives of orders zero through J_h.

The claimed sublevel estimate follows elementarily. Uniform upper
bounds through order J_h+1 give a fixed interval cover where a selected
derivative stays above b_h/4. A measurable sublevel set of length l on
such an interval supplies j+1 ordered points with adjacent separation
at least a fixed multiple of l/(j+1). This follows by quantiles of its
Lebesgue measure; coordinate separation is at least measure separation.
The divided difference is O_j(epsilon/l^j). The real mean-value theorem
identifies it with the j-th derivative divided by j!, forcing
l <= C_j epsilon^(1/j). Order zero gives an empty sublevel set at small
thresholds. The number of covering intervals is bounded independently
of the member of the family.

An error small in C^(J_h), with bounded next derivative, preserves
this proof. It does not create an additive floor for the sublevel
threshold. This distinction is decisive when the threshold is a
negative power of N.

## 5. The inverse graph transform on one disk

The transform in Section 6 is valid for every centered graph A with
sup_(|s|<4a_0)|A(s)| <= a_0/100. Schwarz gives |A(s)|<=|s|/400 on
the inner disk |s|<=a_0 and Cauchy gives |A'(s)|<=1/300 there.
The stable-coordinate inverse equation sends that disk strictly into
itself because 4mu<4/5 and the nonlinear correction is tiny. Its
implicit contraction is at most 2mu epsilon_0.

For two inputs with outer-disk difference D, Schwarz bounds their
difference on the inner disk by D/4. The two implicit arguments differ
by at most epsilon_0 D. The leading output difference is at most
mu D/4 < D/20; parameter changes and nonlinear terms add less than
the stated margin up to D/8. Thus one fixed disk works at every
iteration. Cauchy gives a C^j error bounded by C_j 8^-r.

The transform is centered along the same backward orbit when comparing
an arbitrary translated leaf with the actual stable leaf through its
center. No mismatch of centers enters the contraction. At every point
of the resulting inverse curve the analytic graph is available.

In the later comparison, the target argument has modulus at most
|t|+|Delta_s| <= 5a_0/4 < 2a_0. It is inside the disk on which the
Cauchy error is asserted. Hence the uniform finite-jet lower bound is
retained for all r beyond the fixed threshold r_h.

## 6. Why the finite-curve count is valid

After the area-preserving change of variables, the original small
defect set has points satisfying

dist(Psi^r(y+h), Psi^r(y)-g) <= C epsilon.

For a finite source stable plaque C, these points satisfy
dist(y+h, D)<=10*6^r epsilon with the one finite torus curve
D=Psi^-r(Psi^r(C)-g). The inverse Lipschitz estimate is used only for
this implication. Integer choices of a lift alter D by an integral
deck vector because S^-r is integral. They do not produce additional
torus target curves.

The forward stable plaque has length O(eta^r), as follows by Cauchy
from the LP estimate. The weaker length bound length(D)<=C6^r is
therefore valid. The finite curve stays in a fixed vertical cone, and
covering it in intrinsic order takes O(6^r) patches of fixed small
stable-coordinate radius. Only those finite patches are counted.

Each counted patch has a holomorphic extension to the fixed larger
disk. The extension is used for jets and for evaluation just beyond
an endpoint. It is never substituted for D in a tube-volume estimate.
The complete leaf would be dense and such a substitution would be
invalid.

When the tube radius is less than a_0/100, a relevant patch has a
unique nearby lift relative to the fixed source plaque. Indeed the
shortest nonzero lattice vector in Q Z^2 has maximum norm at least
1/2, while all diameters under consideration are below 10a_0.
Its center has displacement Delta of size below a_0. Bounded graph
slopes turn proximity to the patch into a graph-value sublevel bound
at the same stable coordinate. The uniform finite-contact estimate
then gives C_h(6^r epsilon)^(1/J_h) for each patch. Summing O(6^r)
patches and integrating through the C1 area charts proves

area{defect<=epsilon} <= C_h 6^((1+1/J_h)r) epsilon^(1/J_h).

For larger tube radius the same inequality follows from total area
one after increasing the constant. The finitely many earlier iterates
are nonidentity by the exact e_1,e_2 Fourier test. Their real analytic
defect functions have positive sublevel powers by finite directional
jets and the same divided-difference argument. A finite fixed group
therefore admits beta_d=1/M_d>0 with
area{defect<=epsilon} <= C_d 36^r epsilon^beta_d for all r>=1.

## 7. Imported quantum estimate and exponents

The raw cutoff proof uses Egorov only for the two fixed coordinate
characters. A varying cutoff is multiplied into a trace identity
obtained by cyclicity; it is never propagated. The Weyl product,
commutator, and alias Hilbert--Schmidt estimates yield, before any
sublevel substitution,

|Tr F_(g,h,r,N)|/N <= area{v<=2 delta}^(1/2)
 + C(r+1) rho_r^-10 N^-1 delta^-6,

where rho_r=(1000*256^r)^-1 and v is the sum of squared symbol defects.
The two moduli agree with the torus defects just estimated. Thus the
first term is at most C_d6^r delta^(beta_d/4).

For delta=N^-1/48 and r<=beta_d log N/1024, its power is bounded by

-beta_d/192 + beta_d/512 = -5 beta_d/1536
 <= -beta_d/384.

The remaining term has exponent at most -7/8+15/256 before the
logarithmic prefactor. Absorbing log N+1 by C N^1/32 leaves -201/256,
which is smaller than -3/4. The asserted weaker final exponent is
therefore valid.

The exact projector expansion has total absolute coefficient sum one;
the identity pair has coefficient d^-4. Cases with exactly one
identity group element have zero trace by cyclicity. Negative lags
follow by exchanging the projectors. The stated commutant bound and
moving-window bound then follow by the finite Fejer average. No simple
spectrum is assumed.

## 8. Precise scope

The compactness constants are fixed once d is fixed. A terminating
certificate can in principle be searched for using finite jets,
computable uniform graph approximations and their parameter moduli;
the note does not claim their numerical evaluation.

This audit finds no missing hypothesis in the fixed-d result. It does
not infer uniformity for growing d from that result alone. It does
not remove matrix-element weights from the spectral window estimate,
and it does not evaluate the signed power-trace sums at times of
order N needed for H_diag.
