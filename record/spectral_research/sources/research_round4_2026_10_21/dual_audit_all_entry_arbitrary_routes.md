> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/dual_audit_all_entry_arbitrary_routes.md`. Embedded SHA256: `e0f6e0785d8a052ab20464a5efaaec7a41f608010c9e4398dbe1c7fd143ecc6e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: all-entry estimates and arbitrary Weyl permutation routes

21 October 2026. Auditor: the dual-Weyl research branch, separate from the
root author and the author of the independent analytic derivation.

## 1. Frozen target and verdict

The complete target is `root_all_entry_and_arbitrary_weyl_routes.md`,
SHA-256
`c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`.
All Sections 1--9 were checked. The target remained unchanged throughout.

**Verdict: the estimates (1.1)--(1.5) and their stated scope are proved as
written, using the explicitly identified and previously proved WKB inputs.**
No critical gap or needed modification was found. In particular the proof
supplies the necessary C18 bound, retains the output-dependent aliases,
checks the negative-kick application, and treats time one separately in the
two-HS improvement. It does not establish H_diag, and the target correctly
does not claim that conclusion.

The companion `counter_all_entry_validation.md`, SHA-256
`5ebdc6987ebaf1d35d9902dfd03a569604a5aeb45c1d7b46bdf865fa0ce06acd`,
was read as an additional independent derivation. Its status was not treated
as proof of the target. The algebraic identities and estimates recorded
below were reconstructed directly.

## 2. Input identity and derivative margin

The hashes of the target's actual input files were recomputed and match:

- `counter_one_step_pinching_hs.md`:
  `a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`.
- `audit_one_step_pinching_hs.md`:
  `7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce`.
- `counter_center_phase_c17_bound.md`:
  `992f35db1916f680083fe304caa3001bc71720e2a864f28ea3513f080b5340c5`.
- `root_uniform_analytic_oscillation.md`:
  `5eaae7946e30df2507a870535ec46c2dbc2bce07cc96c8b85366772cab590d31`.
- `audit_explicit_symbol_finite_type16.md`:
  `1da0fbd15dec74a90a742804f69165f478673ce07aaf7eb38760de7f60cb7ffb`.

The first source proves the normalized-HS approximation to the exact
propagator, positive amplitude, real center action, derivative bounds, and
alias pairing. The C17-named supplement actually proves the analytic
supremum bound on a wider strip; this is sufficient to obtain C18, despite
its filename. Its wider-strip proof and the earlier extractor were also
independently audited by this branch in separate frozen reports.

With t=tau/(2pi)<tau/6, the required maximum-partial-derivative bound is

$$
20000t\,18!\,(4000/3)^{18}
<\frac{127903052333056}{3378810882568359375}<\frac1{4000}.
$$

The exact cross-multiplication margin is

$$
3378810882568359375
-4000\cdot127903052333056
=2867198673236135375>0.
$$

This rational identity was independently checked with integer arithmetic.
The maximum convention is essential here: summing over all multiindices
would lose the displayed margin. The target uses the maximum convention
explicitly. Lower orders are covered by the same factorial-radius bound.
The limiting use of the open polydisk radius is justified by taking smaller
radii and passing to the supremum limit.

The negative-kick use is valid. Replacing a by -a leaves the absolute
Fourier, flow, midpoint, transport, and residual estimates unchanged, and
only changes the signs of the marked coefficients. Applying the same
construction with positive t and symbol -a produces the exact E_N^*.
No unproved time reversal of the positive-time action is required.

## 3. The finite-type step genuinely survives every added linear phase

The pure-q frequencies of the ordinary-half symbol are the stated
plus/minus set {1,2,5,6,7,8,9}; the mixed rows have p-frequency plus/minus
one and q-frequencies 0, plus/minus 1,6,7,8. The half-period shift in the
mixed term does not change this support. The two marked coefficients have
moduli at least 1/20 and exactly 1/200.

The target multiplies the previously checked extractors by one extra D_q
or D_p. Hence their minimum orders become two, while their maximum orders
become 17 and 11. Their selected Fourier multiplier remains one. The
formal coefficient one-norms remain at most 27 and

$$
2\frac{37}{36}\frac{50}{49}\frac{65}{64}
=\frac{60125}{28224}<3.
$$

The passage from formal D variables to ordinary derivatives decreases
each coefficient magnitude because each positive derivative contributes
a factor (2pi)^(-1). The target deliberately retains the looser bounds.

For a centered nonzero translation z of length eta, one coordinate has
magnitude at least eta/sqrt(2). Since |exp(2pi i u)-1|>=4|u| for
|u|<=1/2, the corresponding extracted mode gives a pointwise jet lower
bound sqrt(2)/270 or sqrt(2)/300. After taking their minimum and subtracting
the perturbation error sqrt(2)/4000 supplied by C18, the lower bound is
strictly greater than 1/2000 for the normalized difference of S/t.

The derivative count is correct: differentiating the normalized translated
difference 17 times uses the 18th derivative of its parent function in
the integral mean-value formula. A C17 bound alone would not suffice.
The target supplies exactly the additional derivative needed. The same
formula includes the directional limits at z=0 and gives uniformly bounded
higher derivatives for the compact parameter family.

The finite collection of directional derivatives can be chosen by invertible
Vandermonde evaluation of the homogeneous partial-derivative polynomial at
finitely many distinct slopes. Uniform upper derivatives preserve a fixed
fraction of the lower bound on a neighborhood of uniform radius. A finite
smooth partition on these neighborhoods therefore has uniform C1 bounds.
No smooth choice of the successful direction as a function of z is needed.

On each resulting line segment some derivative of order j between two and
17 is bounded below. Adding any linear function changes none of those
derivatives. The one-dimensional estimate follows from the sublevel bound
for the first derivative, proved by divided differences, followed by
integration by parts on its finitely many monotonicity intervals. Specifically
the jth derivative of constant nonzero sign bounds the number of zeros of
the second derivative by j-2 via Rolle's theorem; thus there are finitely
many such intervals independently of the added slope. This argument uses
no upper bound on the first derivative. Endpoint terms are bounded in the
same integration-by-parts estimate.

The resulting uniform rate (1+lambda eta)^(-1/17) is therefore valid.
For the target's optional real nonintegral modulation, restricting the
coordinate cover to the fixed fundamental rectangle only introduces a
finite number of interval endpoints on each slice. For the actual use all
modulations are integer and periodic. This distinction creates no loss or
missing boundary assumption.

## 4. Exact multiplication and the alias signs

Let omega(u,v)=u_2 v_1-u_1 v_2. For one Fourier mode indexed by a, the
phase in the product W_(-w) W_a W_v is

$$
\omega(-w,a)+\omega(a-w,v)
=\omega(a,v+w)+\omega(v,w).
$$

Since omega(a,v+w)=-a dot J(v+w), this proves directly the target's

$$
W_{-w}Q(F)W_v
=e^{\pi i\omega(v,w)/N}
Q\bigl(e_{v-w}(x)F(x-J(v+w)/(2N))\bigr).
$$

The coefficient is the normalized pairing of E_N with this transformed
E_N. Replacing either factor by Q(F) costs at most
eta_N(2+eta_N), with eta_N=||E_N-Q(F)||_HS/sqrt(N). This uses HS
Cauchy--Schwarz and exact Weyl unitarity, and does not require an
operator-norm approximation to Q(F).

In the exact alias pairing put H_m=(s/2,r/2), k_m=v-w-Nm, and change
the variable so that the conjugated F factor is at x. The other factor is
then at x-J(v+w)/(2N)-H_m, and the modulation contributes the unit phase
exp(-2pi i k_m dot H_m). As H_m-Jm/2=(0,r) is integral,

$$
z_m\equiv-J(v-k_m/2)/N\pmod{\mathbb Z^2}.
$$

The exact scalar is the product of the above initial phase, (-1)^(rs), and
exp(-2pi i k_m dot H_m), with the harmless original/ordinary basis signs
if coefficients are written in the original basis. Thus both the shift
and the unit factors in (4.3) are correct. The difference of actions has
the order S(x+z_m)-S(x), not its negative. No alias is omitted.

## 5. The two alias regimes and the row estimate

If |k_m|<=V=|v|_N, then v is a nearest lift to N Z^2 and the distance
function is 1-Lipschitz. Consequently

$$
N\,\operatorname{dist}(z_m,\mathbb Z^2)
=\operatorname{dist}(v-k_m/2,N\mathbb Z^2)
\ge V-|k_m|/2\ge V/2.
$$

This does not require v-k_m/2 to be centered, so there is no failure at
the edge of the centered square. There are only a uniformly bounded number
of aliases in the disk |k_m|<=V<=N/sqrt(2). The added-linear-phase estimate
then gives the claimed column decay for this part.

If |k_m|>V, choose the actual real lift z=-J(v-k_m/2)/N, which may be
large. Periodicity permits this lift in the phase. The mean-value formula
with ||S''||<1/10 gives

$$
|N\nabla(S(x+z)-S(x))|
\le\tfrac1{10}(V+|k_m|/2)<\tfrac3{20}|k_m|.
$$

A coordinate of k_m has magnitude at least |k_m|/sqrt(2); subtracting
3|k_m|/20 leaves strictly more than |k_m|/2. All normalized higher
derivatives are bounded by the same mean-value argument, now using the
appropriate higher derivative of the fixed action. These statements remain
valid for arbitrarily distant aliases because |z| is bounded by
(V+|k_m|/2)/N.

Repeated integration by parts therefore gives O_K((1+|k_m|)^(-K)).
Its coefficients are periodic, the modulation is integral, and the chosen
coordinate derivative never vanishes; endpoint terms cancel exactly.
There are only a bounded number of aliases up to radius 2N. The remaining
mesh-N shell sum is O(N^(-K)) for K>2. This verifies the absolute summability
and the uniform column estimate, including the O(N^(-1)) matrix error.

For the negative kick, the adjoint coefficient matrix is (C^E)^*.
Applying the checked column estimate to E_N^* and interchanging the labels
therefore proves the row bound. The reversal of input and output is exact.

## 6. Fixed-label limit and exclusion of modulus one

The exact commutator multiplier is

$$
-2h^{-1}\sin(2\pi^2h\omega),
$$

whereas Z=J grad a acting on a Fourier mode has multiplier
-4pi^2 omega. Both signs and the h=(2pi N)^(-1) conversion agree.
The global estimate |sin x-x|<=|x|^3/6 gives an O(h^2) difference after
summing the finite a support and the weighted third Fourier moment of the
transported smooth mode.

The C6 bound in dimension two is enough for that sum: sixth-order Fourier
decay gives (1+|u|)^(-6), multiplication by (1+|u|)^3 leaves a summable
two-dimensional sequence. For f_s=e_v composed with the autonomous flow,
partial_s f_s=Z dot grad f_s follows either from the flow semigroup or by
differentiating its composition law. Thus the exact unitary Duhamel formula
proves the stated operator error O_v(h^2). No restriction of growing
frequencies is used to obtain this fixed-label result.

The fixed-label Fourier trace has leading term fhat_t(w). Its other aliases
are rapidly decaying by smoothness, and the ordinary/original basis change
only multiplies the coefficient by signs. The limiting modulus is therefore
|fhat_t(w)|.

If this modulus were one, the continuous unit-modulus function
e_v(Psi_t(x)) e_(-w)(x) would be constant. For example, choosing its average
as the unit constant makes its squared L2 distance to that constant zero,
and continuity then gives equality everywhere. The lifted phase is a
continuous function into one translate of the integers; connectedness of
R^2 makes it constant. Integer shifts imply w=v, because the displacement
of the lifted flow is periodic.

The displacement remainder is correctly bounded in the infinity norm:
||d_s||_infty<=200s and ||DZ||<=10000 give

$$
\|d_t-tZ\|_\infty
\le\int_0^t10000\cdot200s\,ds=10^6t^2.
$$

For a nonzero vector v select the axis Fourier coefficient paired with its
largest coordinate. The leading coefficient of v dot tZ has magnitude at
least (2pi/200)t||v||_infty, while the remainder contributes at most
2\,10^6t^2||v||_infty. The latter is smaller for t<=10^(-10), since
2\,10^6 t<=2\,10^(-4)<2pi/200. Hence v dot d_t cannot be constant.
This proves strict loss for every fixed nonzero input and every fixed output.

The two high-label estimates reduce the global maximum to a fixed finite
collection of centered integer pairs. Their strict limits have maximum
less than one, and convergence is uniform on this finite collection. This
proves one fixed rho<1 for all sufficiently large odd N. The conclusion
concerns individual entries, and is fully compatible with unitarity of C.

## 7. Arbitrary permutations and the all-time constants

Each selected D_j is a weighted permutation, so its singular values are
exactly the selected coefficient moduli. It has operator norm at most rho.
The uniform column bound summed after reindexing by the invertible modular
map S gives

$$
\|D_j\|_{\rm HS}/\sqrt M\le C N^{-1/17}=:\sigma_N
$$

for every time, every N, and every chosen permutation. The shell count is
the same 8r count as in the cat proof; M>=8N^2/9 justifies the normalization.
No property of a particular permutation was used.

With rho replaced by 1-g as in the target, 0<g<=1/2 and
||R_j||<=2-g. The number z_g=g/[2(2-g)] lies in (0,1), and the stated
delta is positive and below one half. To check the latter, it suffices to
check (2-g)^2>g, which holds throughout 0<g<=1/2. Moreover

$$
z_g^{-\delta}(\rho+z_g(2-g))
=(1-g/2)^{-1/2}(1-g/2)=\sqrt{1-g/2}=\eta.
$$

The binomial majorant with the floor follows from z_g^r>=z_g^(delta n)
for every selected r. Thus the operator sum is bounded by eta^n. One
selected D_j charged in HS gives sigma_N rho^(-1)eta^n for the normalized
trace; two selected factors give sigma_N^2 rho^(-2)eta^n whenever n>=2.
For n>=2 there are indeed at least two selected factors because delta<1/2
and the number is integral. This check also covers n=2 exactly.

The two-HS trace inequality is valid with different matrices and arbitrary
intervening factors: use cyclicity to write Tr(A D_a B D_b), then ordinary
HS Cauchy--Schwarz and the ideal inequality. Complex conjugation in that
inequality causes no additional hypothesis on these matrices.

Finally rho>=1/2 and

$$
1-\eta=\frac{g/2}{1+\sqrt{1-g/2}}\ge g/4.
$$

Consequently the target's constants 8 sigma_N/g for all n>=1 and
16 sigma_N^2/g for n>=2 are valid. The factor M/N^2 is less than one.
Time one is not silently omitted from the first assertion and not included
in the second assertion. A separately selected route list for each n is
also permitted because every bound is uniform at that time. This does not
turn the bound into a bound on the union of all lists.

## 8. Pair statistic, normalization, and limits of the result

Removing the scalar identity mode leaves an M by M unitary with

$$
\operatorname{Tr}C^n=|\operatorname{Tr}U_N^n|^2-1.
$$

Thus these are contributions to the original complete squared-trace
functional. They are not an entrywise-probability approximation. The
absolute trace series of the removed class converges, so every bounded
weighted correction is controlled; the source does not incorrectly assert
convergence of separate unweighted full series.

The test b_* in the cited closure manuscript is nonnegative Schwartz with
supremum 1/2 and Fourier transform supported on [-2,2]. That support follows
from its construction as the squared modulus of the inverse transform of
the nonnegative even bump supported on [-1,1]. Therefore its positive
Fourier sum has the stated range n<2N, with zero endpoint weights. The
subtracted benchmark min(n,N)-1 matches the scalar-mode removal exactly.

For arbitrary routes the selected trace need not be real, but its modulus
estimate is the correct complex bound, and the target says this explicitly.
No positivity of the complementary trace is assumed. The enormous number
of possible lists is not summed. The remaining signed dense-history limit
in Section 9 is still unproved, and neither all fixed orders of H_diag nor
Sine_2 convergence follows from the proved removal estimates alone.
