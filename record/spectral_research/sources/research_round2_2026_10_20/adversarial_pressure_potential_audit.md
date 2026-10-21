> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_pressure_potential_audit.md`. Embedded SHA256: `b0f2bed058af3a88a56122a3d73d64263296666b58f293ca846a023a58282e19`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit of the analytic parameter potential

Input: `arithmetic_pressure_analytic_potential.md`, SHA-256
`44da5eefab7cce7d7eb222fa54f027eec8a1a545b8ca0c4fd3fcf1fc7520637f`.
The actual ordinary-Weyl symbol and the fixed-map geometric inputs were
checked in the preceding audits.

**Verdict: the complete potential construction passes.** It gives a
holomorphic parameter family in one fixed C^alpha space for
0<alpha<=1/2, with radius 10^-16 and norm bound 10^11 |s|, the exact
coordinate-potential first variation, and the displayed third-order
potential remainder. Analyticity or quantitative remainders for the
pressure functional are separate assertions and are not inferred here.

## 1. Holder Green bound

In the fixed eigen-coordinate quotient metric, the torus diameter is
less than one and the Lipschitz norm of D^n is at most lambda^|n|.
Thus composition costs at most lambda^(alpha |n|) in C^alpha. The
unstable and stable Green sums have Holder-seminorm factors

1/(lambda-lambda^alpha),
lambda^alpha/(1-lambda^(alpha-1)).

For alpha<=1/2 the second is at most
lambda/(sqrt(lambda)-1)=lambda/sqrt(2)<5, and the first is smaller.
The supremum bound is (1-lambda^-1)^-1<5/4. Combining these bounds
with the norm sup+[.] gives operator norm at most five. There is no
assumption of analytic spatial dependence of a forcing function.

## 2. Complex flow and composition in the fixed space

The finite Fourier bounds ||X||<=22, ||DX||<=2000 and ||D^2X||<=10^5
on the original strip justify complex-time Picard iteration for
|s|<=10^-8 and the smaller eigen-coordinate tube. The total displacement
is at most 22|s|, whereas the initial imaginary part in the original
coordinates is below 2*10^-4. Both remain well within 1/100. The first
and second variational equations give the bounds 4000|s| and
2*10^5|s|. The fixed linear coordinate changes therefore give

||V_s||, ||DV_s||, ||D^2 V_s|| <= 10^9 |s|.

The second-derivative raw factor is already below 1.2*10^7. The
constant 10^9 has ample margin. Divergence of the original Hamiltonian
vector field vanishes identically, including at complex points, so
det DF_s=1 there as used later.

For a Holder section w of norm at most 10^-5, the point z+w(z) stays
in the same reserved tube. Choose shortest lift differences when
comparing two base points. The straight segment between the two
complex arguments stays in the tube, and the mean-value bound gives

[V_s(Id+w)]_alpha <= 10^9 |s| (1+[w]_alpha).

Here dist^(1-alpha)<=1 uses the fixed quotient diameter. Adding the
supremum bound gives the stated norm at most 3*10^9|s|. The same
argument for DV_s uses the bound on D^2V_s. The integral difference
formula and the Holder Banach-algebra inequality then give contraction
factor 15*10^9|s| after the Green operator. It is at most 1.5*10^-6
on |s|<10^-16, and the image stays inside the prescribed ball.

The Nemytskii map is genuinely holomorphic on this complex Holder
ball. Taylor expansion of V_s(z+w+h) has coefficients given by its
spatial derivatives at z+w. Cauchy bounds on the reserved margin
control their supremum and Holder seminorms, the latter using one
additional spatial derivative and the fixed Holder norm of w. The
Taylor coefficients after division by their factorials grow at most
geometrically after slightly decreasing that margin. The Holder
algebra bound makes the series converge in the fixed norm. The same
reasoning applies jointly in s. Uniformly convergent holomorphic
contraction iterates therefore give a holomorphic solution w_s.

For real s, the equivariant semiconjugacy Id+w_s is a homeomorphism
by the bounded two-sided Green inverse argument. Its smallness condition
is below 2*10^-7. No spatial derivative of this Holder map is used.

## 3. Pulled-back unstable cocycle

The derivative cocycle A_s=DF_s(Id+w_s)=D+B_s is holomorphic in s in
the same space, with ||B_s||<=3*10^9|s|<=10^10|s|=:a_s<=10^-6.
For a slope eta of norm at most 10^-4, the denominator
lambda+B_11+B_12 eta has inverse Banach-algebra norm less than 1/5.
The scalar projective fraction has eta derivative

det A_s / (lambda+B_11+B_12 eta)^2.

Determinant one therefore gives norm at most 1/25. Composition with
the fixed base D^-1 costs less than three, yielding the contraction
3/25. There is no parameter-dependent composition of an arbitrary
Holder section. The invariant slope has norm at most
(3/5)/(1-3/25) times a_s, which is below a_s.

Its multiplier b_s=lambda+B_11+B_12 eta_s differs from lambda by at
most 2a_s in the Banach algebra. The logarithm series consequently
converges and has norm less than a_s. This proves the claimed weaker
bound 10^11|s| even after changing the fixed coordinate metric.

For real s, b_s>5 and the invariant vector is expanded by its product
up to bounded endpoint vector norms. It is the geometric unstable
direction. With u_s(z)=log||Q^-1(1,eta_s(z))||, the exact cocycle
identity gives

log J_s^u(H_s z)=log b_s(z)+u_s(Dz)-u_s(z).

The function u_s is Holder. This is an exact coboundary relation,
not a pressure approximation.

## 4. Exact first variation and potential remainder

At s=0, the unperturbed derivative is constant. Differentiating
DF_s(H_s z) therefore introduces no term from the derivative of H_s.
The first cocycle derivative is D Q(DX)Q^-1. Since the zero-parameter
off-diagonal entry and slope are zero, the first logarithmic multiplier
derivative is

ell_u (DX) Q^-1 e_u,
Q^-1 e_u=(sqrt(3)/2,sqrt(3)/(2 sqrt(2))).

For DX=(1/(2pi))[[a_pq,a_pp],[-a_qq,-a_qp]], the two mixed derivatives
cancel, giving exactly

xi=(a_pp-2a_qq)/(4pi sqrt(2)).

This is the variation of the chosen coordinate multiplier potential.
The variation of a different metric representative may differ by the
derivative of a coboundary.

The quotient (psi_s-psi_0)/s is holomorphic and bounded by 10^11 on
the radius-R disk. Cauchy coefficient bounds and the geometric sum
for |s|<=R/2 give

||psi_s-psi_0-s xi-(s^2/2)psi''_0||
 <=2*10^11 R^-2 |s|^3=2*10^43 |s|^3.

It is important that this uses the bounded quotient; replacing it by
an O(1) bound for psi would lose one power of R. Bounds on open disks
are sufficient, by applying Cauchy's formula on inner circles and
taking their radii up to R.

## 5. Independent exact check of the proposed variance input

Using the corrected ordinary-Weyl symbol, write a_v for its Fourier
coefficients and z_(k,l)=(2k^2-l^2)a_(k,l). Then xi_v=(pi/sqrt(2))z_v.
Independent rational complex arithmetic gives

sum_v |z_v|^2 = 313386243/80000,
sum_v z_v conjugate(z_(S^T v)) = -7/2000000.

The only nonzero one-step frequency matches are
(1,-1) -> (1,1) and (-1,1) -> (-1,-1). Their individual products are
-7/4000000 minus and plus (3/500000)i, respectively.
No match at two or more positive steps is possible: for |k|>=2 and
|l|<=1, S^T(k,l) has coordinates of the same sign and second
coordinate of magnitude at least five. Such coordinates subsequently
grow. The remaining k=0,1,-1 cases give only the two chains just
listed, whose next step has second-coordinate magnitude seven.
Negative lags give the conjugate correlation.

Thus the proposed variance is exactly

sigma^2=(pi^2/2)(313386243/80000-14/2000000)
       =7834656061*pi^2/4000000.

This independently verifies the finite Fourier arithmetic. Turning
sigma^2/8 into a certified pressure-gap coefficient still requires
the pressure differentiation formula and a controlled remainder.

## 6. Convention and scope for the next step

This potential belongs to the forward Egorov map S Phi_s. The earlier
quantum pressure estimate used its physical inverse. In dimension two
with preserved area their unstable-potential pressures do agree, but
that equality should be stated through the exact stable/unstable-angle
coboundary: determinant one makes log J^u+log J^s a coboundary, and
log J^u of the inverse is minus log J^s at the inverse base point.
Their integrals agree for every common invariant measure, and the
entropies of a map and its inverse agree. This proves the pressure
identification by the variational principle. Equality of topological
entropies alone would not prove it.

The audited construction does not yet quantify the pressure functional
on this Holder space. A verified coding and transfer/resolvent estimate,
or another complete quantified argument, is still required for an
explicit lower bound on the actual pressure gap at tau=10^-80.
