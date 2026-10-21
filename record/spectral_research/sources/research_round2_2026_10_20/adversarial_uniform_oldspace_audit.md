> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_uniform_oldspace_audit.md`. Embedded SHA256: `5c3beafa999499f7dbcfacd39b6ab13b5a4a82fc6a8da6441d32277c921f8d28`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit: a logarithmic bound for all canonical oldspaces

Input: `arithmetic_iterated_uniform_all_old_logarithmic.md`, SHA-256
`690910507ef2849d81aeb59350d145c84997cd692cbca784711509d6274480fd`.
Its fixed-divisor and uniform-contact geometric inputs are independently
checked in `adversarial_logarithmic_horizon_audit.md` and
`adversarial_uniform_contact_audit.md`.

**Verdict: the full stated theorem passes audit.** In particular the
full-commutant variance of the projector onto the sum of all canonical
oldspaces is O(1/log N) along every odd dimension. The estimate allows
arbitrary multiplicity blocks and arbitrary orthonormal eigenbases.
It concerns matrix elements, not microscopic unweighted eigenphase
statistics.

## 1. Uniform geometry and the re-centering check

For nonzero h, the uniform contact family has a finite-jet lower bound
c(|h|_T+|z|). Its normalized derivatives through every fixed finite
order are bounded on smaller disks. A nonempty ORIGINAL defect set
gives |g|_T<=6^r|h|_T+C_0 epsilon. The C1 holomorphic graph dependence
and the centered inverse graph contraction then give, at every center
of the finite target curve,

||error||_(C^j) <= C_j(6/8)^r|h|_T+C_j C_0 8^-r epsilon.

For epsilon<=c_0|h|_T, one fixed r_0 makes all derivatives through J
small enough to retain the contact lower bound. The derivative of
order J+1, divided by |h|_T, is bounded as well. The threshold r_0
does not depend on h,g or an arithmetic denominator. Larger epsilon
is the trivial range of the later relative sublevel estimate.

An arbitrary nearby true target graph is initially written
Delta_u+gamma_y(t-Delta_s), with y=x+h+Delta. Set
z=Delta_u+gamma_y(-Delta_s). The point y+(-Delta_s)e_s
+gamma_y(-Delta_s)e_u equals x+h+z e_u and lies on the same true
stable leaf. Uniqueness of its centered graph therefore gives the
exact identity

Delta_u+gamma_y(t-Delta_s)=z+gamma_(x+h+z e_u)(t).

If the actual inverse curve is gamma_y+E, its additional error after
this re-centering is exactly E(t-Delta_s). This error need not vanish
at t=0; the relative finite-jet estimate includes order zero and
permits such an error. Shrinking the fixed patches once keeps both
the shifted arguments within the controlled inner disk and z within
the fixed contact range. Division by |h|_T+|z| only improves the
available relative error bound.

The finite target D=Psi^-r(Psi^r(C)-g) has length at most C6^r and
requires at most C6^r patches. A genuine return defect puts the source
translate inside its tube of radius C6^r epsilon. Applying the
relative contact estimate on each finite patch gives area at most

C36^r (epsilon/|h|_T)^beta,  beta=1/J.

The proof retains the finite curve for counting. Extensions of the
complete leaf supply local analytic graphs and endpoint evaluations
only. If the tube is larger than the chart, total area one gives
the same bound after increasing the constant. No unproved early-lag
uniform estimate is needed: the application starts at the fixed r_0.

## 2. Quantum exponents with a growing divisor

A nonzero group translation has |h|_T>=c/d. Substituting the relative
sublevel estimate into the exact coordinate-character cutoff bound
gives

|Tr(G_g U^-r G_h U^r)|/N
 <= C6^r d^(beta/2) delta^(beta/4)
 + C(r+1)256^(10r)N^-1 delta^-6.

Both half-powers are correct: the area estimate first receives the
threshold sqrt(2 delta), and then the trace estimate takes its square
root. No varying symbol is transported through Egorov.

For delta=N^-1/48, d<=N^(1/4096), and
r<=beta log N/4096, the first exponent is bounded by

-beta/192+beta/8192+beta/2048
=-113 beta/24576 <=-beta/256.

The second exponent, after absorbing the logarithmic factor, is at
most -7/8+15/1024+1/32=-849/1024<-3/4. Thus one error
epsilon_N=C N^(-beta/256) works for every permitted divisor and group
word at every lag in [r_0,t_N]. Identity group elements are handled
exactly by trace zero and cyclicity.

The character-projector expansion has total absolute coefficient
sum one, so it does not introduce a growing factor d. The finite
average of length L=t_N+1 has at most 2r_0-1 early lag values, each
of weight at most 1/L. Centered Cauchy--Schwarz bounds each by c-c^2.
Consequently the early contribution is s_0(c-c^2)/L with
s_0=2r_0-1. The remaining contribution is epsilon_N. Projection to
the full commutant can only decrease this norm.

## 3. Exact oldspace arithmetic

If d^2 and e^2 divide N, then de divides N. The two Weyl groups
defining the corresponding invariant subspaces commute because their
symplectic products are multiples of N^2/(de), hence of N. Their
common invariant vectors have support in multiples of lcm(d,e) and
shift invariance by gcd(N/d,N/e)=N/lcm(d,e). Therefore

P_d P_e=P_lcm(d,e).

Every composite-index oldspace is contained in a prime-index one.
The projector onto their total span is exactly
I-product_(p^2|N)(I-P_p), and its rank fraction is
c_N=1-product_(p^2|N)(1-p^-2). The elementary estimate
sum_(n>=1)(2n+1)^-2<sum_(n>=1)[4n(n+1)]^-1=1/4 gives c_N<1/4.

The bound product_(p<=n)p<=4^n is valid by induction. For n=2m,
primes in (m,2m] divide binomial(2m,m)<=4^m. For n=2m+1, primes
in (m+1,2m+1] divide binomial(2m+1,m)<=4^m; the last inequality
uses the two equal maxima of the odd binomial row. Multiplication
by the already bounded lower-prime product proves both induction
steps. Thus no prime-number asymptotic is imported.

## 4. Collective projection and the tail

Take R=floor(beta log N/8192), and form Q from primes p<=R with
p^2|N. Their product d_0 satisfies d_0^2|N and
d_0<=4^R<=N^(1/4096), so the uniform trace bound applies to its group.
Inclusion--exclusion expresses Q as a signed sum of at most 2^s-1
subgroup averages, each of coefficient l1 norm one. The identity
coefficient equals q=rank(Q)/N because every nonidentity group
element has trace zero. Centering Q removes that coefficient.
The centered coefficient l1 norm is at most 2^s<=2^R.

At the controlled lags, the centered Q correlation is therefore
bounded by 4^R epsilon_N. At the early lags it is bounded directly
by q-q^2<=1/4. Applying the coefficient l1 bound at early lags would
lose this theorem; the input correctly does not do so. The commutant
variance is at most s_0/(4L)+4^R epsilon_N.

The difference D=P_old-Q is an orthogonal projector because Q is
contained in P_old. Its rank fraction delta is at most
sum_(p>R)p^-2<=1/R. The centered difference has squared normalized
Hilbert--Schmidt norm delta-delta^2<=1/R. Projection to the commutant
decreases it. The squared triangle inequality gives

Var(P_old) <= s_0/(2L)+2/R+2*4^R epsilon_N.

Finally 4^R epsilon_N<=C N^(beta/4096-beta/256)
=C N^(-15 beta/4096), exactly as claimed. This argument includes the
case of no small prime divisor, where Q is zero, and square-free N,
where P_old itself is zero.

## 5. Eigenbases, individual oldspaces, and moving windows

In any U-eigenbasis, the diagonal entries of E_U(P_old) equal those
of P_old. The sum of squared diagonal deviations is bounded by the
full Hilbert--Schmidt norm, even inside repeated-eigenvalue blocks.
This proves the stated basis-independent mass variance.

For an individual prime p the mean mass is p^-2<=1/9. Chebyshev and
the uniform sector variance, summed over p<=R, give the terms
s_0/[4L(eta-1/9)^2] and R epsilon_N/(eta-1/9)^2. For p>R, Markov's
inequality with the exact trace mean gives 1/(eta R). Containment
of every oldspace in a prime-index one then proves the asserted
union bound for all d.

For the moving-window estimate use the finite time average with
unit complex phases depending on the window center. Its squared
norm for Q-qI has the same correlation bound, because the phases
have modulus one. Its action on D-delta I is a contraction by the
triangle inequality. The same squared triangle bound thus applies
uniformly in the center. The normalized Fejer kernel is at least
4/pi^2 in the window of radius 1/(2L), giving exactly the displayed
factor pi^2/4. No separate correlation estimate for the tail is needed.

## 6. Scope

The waiting time, exponent and constants depend only on the original
fixed analytic map, with tau=10^-80, and not on d or N. The proof
uses finite averages as operator inequalities, without averaging the
family over N or the kick. The full-oldspace O(1/log N) statement
therefore holds along every odd dimension.

It remains a weighted matrix-element result. No positive lower
bound on those weights for every near eigenphase pair has been proved,
and no order-N signed power-trace sum is estimated by this argument.
Accordingly it neither proves nor refutes H_diag.
