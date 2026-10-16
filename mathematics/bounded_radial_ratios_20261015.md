# Contractive radial secular ratios and the full microscopic process

**Stable claim:** `BGS-TRACE-090`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** Any unitary spectrum. The mixed-moment convergence premise for the frozen model is open; weak convergence alone supplies no unbounded count UI. Discrete Toeplitz contraction requires grid M>=N.

Canonical status is [the claim ledger](../record/claim_ledger.md); source `S14` is preserved verbatim in [the imported record](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s14). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../evidence/executions/20261016/chat-integration/receipt.json).


Date: 15 October 2026.

## Status and boundary

This note gives self-contained finite spectral identities, a uniformly bounded
radial determinant observable, a weak local-process characterization, and an
exponentially accurate angular quadrature bound. They hold for any unitary
matrix. They do NOT establish a new spectral limit for the frozen BGS family.
In particular, neither its bounded determinant moment limit nor its original
signed Heisenberg trace hierarchy is proved here. No external referee approval, formal certification, or priority claim is made.

The preceding collision-crossover note evaluated an equal-directed-edge
subfamily at m comparable to sqrt(N) and exhibited exact cancellation of
repeated visits in the determinant. Its Section 10 correctly left the
microscopic logarithmic derivative unestimated. The current note does not
extrapolate that subfamily to time N. It tests a different organization of the
FULL determinant, retaining all spectral phases.

## 1. Original matrix and conventions

The physical family is still

    U_N = exp(i*tau*N*A_N) M_N, tau=10^-80, N>=3 odd.

The periodic profile is

    r(q)=(1-cos(14*pi*q))*(1+cos(2*pi*q)).

The diagonal of A_N is

    cos(14*pi*x/N)+r(x/N)/10+r(x/N)*sin(2*pi*x/N)/100-1/10.

Its upper cyclic edge is

    ((-3-4*i)/5)*r(((x+inverse_mod(2,N)) mod N)/N)/200,

and its lower edge is the conjugate. This is the previously checked raw/midpoint
prescription, including the physical half-shift. The cat factor is

    M_xy = N^(-1/2) exp(2*pi*i*(-inverse_mod(8,N))
                       *(3*x*x-2*x*y+3*y*y)/N).

For a general unitary U with eigenvalues exp(2*pi*i*theta_j), put

    p_U(z)=det(I-z U),
    Xi_(N,alpha)=sum_j sum_(l in Z) delta_(N*(theta_j-alpha+l)),

where alpha is uniform on [0,1). This is the only random variable attributed
to the original deterministic spectrum. In particular

    E_alpha <f,Xi_N> = integral_R f(x) dx

for nonnegative integrable f, by Tonelli and a change of variables.

## 2. Exact bounded radial ratio

Fix 0<s<t and set r_s=exp(-s/N), r_t=exp(-t/N). Define

    F_(N;s,t)(alpha)
       = exp(-(t-s)) * |p_U(r_s exp(-2*pi*i*alpha))
                         /p_U(r_t exp(-2*pi*i*alpha))|^2.        (1)

All denominators are nonzero. The following statements are unconditional:

    0 < F_(N;s,t)(alpha) <= 1,                                (2)
    E_alpha[-log F_(N;s,t)] = t-s.                            (3)

To prove them, write V=exp(-2*pi*i*alpha)U and c_s=cosh(s/N),
c_t=cosh(t/N). Then

    F_(N;s,t)=product_j (c_s-cos(2*pi*(theta_j-alpha)))
                            /(c_t-cos(2*pi*(theta_j-alpha))). (4)

Each factor is in (0,1). This follows directly from
|1-r exp(i*x)|^2 = 2r*(cosh(-log r)-cos x); the N factors of r_s/r_t
cancel the exterior exp(-(t-s)). Jensen's circle identity for the zero-free
polynomial p_U inside the unit disk gives (3). Alternatively it follows from
the positive linear-statistic identity below, without complex logarithms.

Let

    f_(s,t)(x)=log((t^2+4*pi^2*x^2)/(s^2+4*pi^2*x^2)).          (5)

This function is nonnegative, integrable, and has integral t-s. Exactly,

    sum_(l in Z) f_(s,t)(x+Nl)
      =log((cosh(t/N)-cos(2*pi*x/N))
                 /(cosh(s/N)-cos(2*pi*x/N))).                 (6)

A proof is to differentiate both sides in t and apply the Fourier series of
the Poisson kernel, then integrate from s to t; all derivative series are
absolutely convergent. This avoids conditional logarithmic products.
Equations (4)-(6) give

    F_(N;s,t)(alpha)=exp(-<f_(s,t),Xi_(N,alpha)>).              (7)

Thus (1) is an exact Laplace observable of the FULL spectrum. Its bound is not
obtained by estimating the numerator and denominator separately.

## 3. Positive matrix form and a uniform finite logarithmic expansion

Let

    H_t = c_t I - (V+V*)/2,
    kappa = c_t-c_s,
    K = kappa H_t^(-1).

Then H_t is positive definite and

    0<=K<=q_N I<I,  q_N=(c_t-c_s)/(c_t-1),
    F_(N;s,t)=det(I-K).                                      (8)

For all N>=1, q_N is at most

    q_* = 1-(sinh(s/2)/sinh(t/2))^2 <1.

Indeed sinh(s*x)/sinh(t*x) decreases in x>0; this follows because u*coth(u)
is increasing. Take x=1/(2N)<=1/2. Moreover

    E_alpha Tr K = N*(c_t-c_s)/sinh(t/N) <= t-s.               (9)

The integral of 1/(c_t-cos theta) is 1/sinh(t/N). The upper bound follows by
integrating sinh u over [s/N,t/N]. Thus for any integer L>=1, if

    F_L=exp(-sum_(k=1)^L Tr(K^k)/k),

then

    0<=E(F_L-F)<= (t-s)*q_*^L/((L+1)*(1-q_*)).                (10)

This follows from the eigenvalue expansion of -log det(I-K),
Tr K^k <= q_*^(k-1) Tr K, and |exp(-a)-exp(-b)|<=|a-b| for a,b>=0.
It is uniform over all spectra and dimensions. It does NOT evaluate the law
of the few remaining resolvent traces, which still contain microscopic
spectral information. Their individual means alone cannot evaluate the
nonlinear exponential in F_L.

## 4. A bounded determinant criterion for weak Sine_2 convergence

The subfamily t=2s suffices. Put F_(N;s)=F_(N;s,2s). For positive s_j, real
shifts a_j, and positive integer powers k_j, consider

    Z_N = integral_0^1 product_(j=1)^r
                       F_(N;s_j)(alpha+a_j/N)^(k_j) d alpha. (11)

Let Z_N^CUE be its Haar U(N) expectation. The statement

    Z_N-Z_N^CUE ->0                                          (BR)

for every fixed finite set of such parameters is equivalent to WEAK convergence
of Xi_(N,alpha) to Sine_2. Positive rational s_j, rational a_j, and integer k_j
already form a sufficient countable family.

Here weak convergence refers to the distribution of locally finite counting
measures, with multiplicities allowed before the limit. It is NOT asserted to
imply convergence of unbounded factorial moments.

### Proof of sufficiency

First, mixed integer moments of the [0,1]-valued variables F_(N;s_j) determine
expectations of every continuous function of any fixed finite vector, by
polynomial approximation on [0,1]^r. In particular one obtains (BR) with
arbitrary positive real powers in place of integer k_j. No tail condition or
moment growth estimate is needed in this step.

Second, the positive functions

    K_s(x)=f_(s,2s)(x)/s

have integral one and form an approximate identity as s decreases to zero.
They have the scaling form s^(-1)K_1(x/s). Given f>=0 in C_c^infinity(R),
f*K_s tends to f in L1. A finite positive Riemann sum then approximates this
convolution in L1 by

    g(x)=sum_j b_j f_(s,2s)(x-a_j),  b_j>=0.

The locations, widths, and coefficients can be approximated by suitable
rational values; L1 continuity of translations and scale changes suffices.
For every deterministic spectrum, unit mean intensity gives the uniform bound

    |E exp(-<f,Xi_N>)-E exp(-<g,Xi_N>)| <= ||f-g||_1.          (12)

The same bound holds for Sine_2. Equation (7) and (BR) identify the limit for g.
First take N to infinity at the fixed finite collection, then send the L1
error to zero. This identifies all compact nonnegative Laplace tests.
Local tightness follows from E Xi_N(I)=|I| and Markov, or from the usual
Laplace-functional criterion. The limit is Sine_2.

### Quantitative approximation of a compact test

For 0<s<=1, H=||f||_1 and D=||f'||_1, the elementary kernel bounds

    K_s(x)<=log(4)/s,
    K_s(x)<=3s/(4*pi^2*x^2),  x!=0

give

    ||f-f*K_s||_1
       <= D*s*[log(4)+(3/(2*pi^2))*log(1/s)]
                         +(3H/pi^2)*s.                     (13)

Split the translation-integral bound at |x|=s and |x|=1. The first two
regions use ||f(. -x)-f||_1<=|x|D, and the tail uses 2H.
For a midpoint Riemann mesh of width epsilon covering supp f, define

    g(x)=sum_j epsilon*f(a_j)*K_s(x-a_j).

Since ||K_s'||_1=2 log(4)/s, the error is at most

    ||f*K_s-g||_1
       <= epsilon*D + epsilon*log(4)/s*(H+epsilon*D).         (14)

These bounds turn (12) into a finite nonasymptotic approximation certificate.
They bound the approximation error, NOT the unknown physical discrepancy in
(BR). No dimension-dependent f or shrinking s is substituted before N tends
to infinity.

### Converse and the unbounded-moment boundary

Each exponent sum in (11) is continuous and integrable, with O(x^-2) tails.
Weak convergence gives convergence of compactly supported truncations.
The tails cost at most their L1 norm uniformly over all N, by unit intensity.
The same is true for Sine_2. This proves necessity of (BR).

Weak convergence alone does not imply factorial moment convergence. For
example, from any good deterministic base spectrum, relocate n_N=o(N) levels
into a much narrower than 1/N packet, with n_N^2/N tending to infinity. The
probability that a fixed microscopic observation window sees a changed point
is O(n_N/N), so the weak law and every bounded test above are preserved.
The packet's factorial second moment is of order n_N^2/N. Thus a separate
uniform-integrability argument remains necessary to infer all unbounded
correlation limits from (BR). This differs from the previous full factorial
hierarchy H_diag, which itself implies that moment control. No claim of
closing the stronger task is made by replacing H_diag with the weaker BR.

## 5. Exact finite CUE calibration

For one ratio (power one), let a=exp(-s/N), b=exp(-t/N). Then

    E_CUE F_(N;s,t)
       = exp(-(t-s))*[1+(a-b)^2/(1-b^2)*(1-a^(2N))/(1-a^2)].  (15)

Consequently

    Z_Sine(s,t)
       = exp(-(t-s))*[1+(t-s)^2/(4st)*(1-exp(-2s))].          (16)

This is a specialization of the established unitary ratio formula, not a new
random-matrix result. Here is an independent finite Toeplitz verification.
The single-eigenvalue factor in (4) has Fourier coefficients

    delta_(j,0) - d*b^|j|,
    d=(c_t-c_s)/sinh(t/N)=(a-b)*(1-ab)/(a*(1-b^2)).

Expanding the two Vandermonde determinants in the CUE density gives

    E_CUE F = det[I-d (b^|i-j|)_(0<=i,j<N)].                  (17)

The inverse of R_ij=b^|i-j| is tridiagonal, with endpoint diagonals
1/(1-b^2), internal diagonals (1+b^2)/(1-b^2), and off-diagonals
-b/(1-b^2). Its determinant is (1-b^2)^(N-1). Applying the tridiagonal
determinant recurrence gives (15); N=1 follows from the single entry.
The verifier checks this rational identity exactly for 27 choices.

For finitely many shifted ratios with integer powers, the CUE mean is the
Toeplitz determinant of the product of the single-eigenvalue factors (4).
The microscopic limit is the Sine-kernel Fredholm determinant weighted by
h=1-exp(-g), where g is the exponent sum in (11). Since 0<=h<1 and h is
integrable, the positive weighted kernel is trace class. One may truncate
g in L1 first, use the finite CUE kernel convergence on the compact set,
and then remove the truncation using (12). No unjustified tail limit is used.

At s=1,t=2 the Sine value is

    exp(-1)*(1+(1-exp(-2))/8) = 0.4076409877718897...

For the regular N-clock, the exact value at every N is instead

    exp(-(t-s))*[1+(exp(-s)-exp(-t))^2/(1-exp(-2t))],

which is 0.3881443433921127... at s=1,t=2.
For Poisson intensity one the Laplace functional is

    exp(-(t^2-s^2)/(2t)),

which is exp(-3/4)=0.4723665527410147... there. These comparisons demonstrate
that the observable is not fixed by unit intensity or unitarity alone.

## 6. A rigorous angular quadrature bound for arbitrary spectra

Write phi=2*pi*alpha and analytically continue the rational factors (4) in
complex phi. Define

    eta_N=arcosh((cosh(s/N)+cosh(t/N))/2).

For |Im phi|<=eta_N, each ratio has modulus at most one. Indeed, for
z=cos(x+i*y),

    |c_s-z|<=|c_t-z| iff Re z <= (c_s+c_t)/2,

and Re cos(x+i*y)<=cosh(y). Also eta_N<t/N, so no denominator pole enters
this strip. Products of shifted ratios with positive INTEGER powers obey
the same bound in the smallest of their strips. Numerator zeros do not
obstruct this rational analytic continuation.

For 0<eta<eta_N, the Fourier coefficients obey |Fhat_k|<=exp(-eta |k|).
Therefore the M-point equally spaced angular rule satisfies

    |(1/M)sum_(j=0)^(M-1) F(j/M) - integral_0^1 F(alpha)dalpha|
               <= 2/(exp(eta M)-1).                         (18)

As eta_N*N tends to sqrt((s^2+t^2)/2), this requires O(N log(1/epsilon))
angular samples for error epsilon, uniformly over every spectrum, including
clusters and multiplicities. It is a numerical integration result, not a
bound on the difference from CUE.

For the Toeplitz reference with Fourier indices |k|<N, the same analytic strip
bounds the FFT aliasing error by

    2 exp(-eta(M-N))/(1-exp(-eta M)).

Both the exact and discrete Toeplitz matrices are positive contractions.
Their determinant difference is at most their trace-norm difference,
bounded by N^2 times this coefficient error. Roundoff in a floating-point
implementation is a separate issue.

### Domain of the discrete Toeplitz contraction

The sampled Toeplitz matrix is a compression of multiplication by its
sampled symbol only with the appropriate discrete Fourier isometry. If
the matrix has size N and the angular grid has M points, require **M>=N**.
Indeed V_(j,k)=M^(-1/2) exp(2 pi i j k/M), with 0<=k<N, has V*V=I
in that domain. For a real sampled symbol in [0,1], V*diag(f_j)V is
therefore a positive contraction. If M<N, columns repeat; the constant
symbol on the one-point grid gives the all-ones N by N matrix, of norm N.
The determinant perturbation bound used above cannot invoke contraction
in that excluded domain. The maintained checker now enforces M>=N.

## 7. The original pair energy is still a boundary derivative

Let Z_N(s,u)=E_alpha F_(N;s,s+u), with u>-s at fixed N. Set

    L_N(s)=N^(-2) sum_(m>=1) exp(-2sm/N) |Tr U^m|^2.

Then exactly

    Z_N(s,0)=1,   partial_u Z_N(s,0)=-1,
    partial_u^2 Z_N(s,0)=1+2L_N(s).                           (19)

Proof: let

    D_N(s,alpha)=(1/N)sum_j
           sinh(s/N)/(cosh(s/N)-cos(2*pi*(theta_j-alpha))).

The first derivative of log F at u=0 is -D_N, and its second is
-partial_s D_N. The mean of D_N is exactly one, so the mean of its
s-derivative is zero. Thus the second derivative in (19) is E D_N^2.
The Poisson series and Parseval give E D_N^2=1+2L_N(s).

Equation (19) pinpoints the remaining difficulty. Boundedness of F for u>=0
is not uniform integrability of D_N^2. One must not differentiate a proposed
pointwise limit at u=0 without a uniform derivative/moment argument. The
cluster modification in Section 4 is an explicit obstruction to doing so.
The original target L_N(s)->(1-exp(-2s))/(4s^2) remains unproved.

## 8. Physical attempt, not a theorem about its limit

For the actual U_N the new direct necessary test at s=1,t=2 is

    integral_0^1 exp(-1) * |p_N(exp(-1/N-2*pi*i*alpha))
                            /p_N(exp(-2/N-2*pi*i*alpha))|^2 d alpha
                  -> 0.4076409877718897...                   (20)

The verifier computes the LEFT side and two higher mixed observables from the
full exact matrix prescription, not an equal-edge sector and not truncated
power traces. Its completed dimensions are 31,61,127,251,509. Couplings 0.03
and 0.30 are explicit proxies; tau=0 is an unperturbed cat control. The literal
10^-80 is not numerically simulated or inferred from those values.

For proxy tau=0.30:

| N | one-ratio mean | finite CUE | shifted two-ratio mean | finite CUE |
|---:|---:|---:|---:|---:|
|31|0.4425180270|0.4076099725|0.1966646546|0.1623968622|
|61|0.4205110520|0.4076329746|0.1853594233|0.1624336159|
|127|0.4100829676|0.4076391389|0.1656294479|0.1624434572|
|251|0.4068344590|0.4076405144|0.1628797547|0.1624456527|
|509|0.4089350486|0.4076408727|0.1625967767|0.1624462245|

The shifted product uses centers -1/2 and +1/2 in unfolded units, both with
s=1,t=2. Its exact finite CUE mean is a Toeplitz determinant, not a fitted
constant. Angular quadrature error bounds are below 3e-15 for exact input
phases; computed phases have their separate floating-point Schur residuals.
No interval-arithmetic certification of those eigenphases is asserted.

These tests are compatible with CUE at the displayed proxy sizes; they prove
neither a limit at a proxy coupling nor a transfer to 10^-80. No estimate of
the actual discrepancy in (20), or of the full collection (BR), was obtained.
The normalized positive determinant avoids a separate catastrophic inverse-
denominator bound, but it does not make the underlying spectral distribution
universal. FM-021's classical intensity gap is not inserted as a substitute.

## 9. Verification receipts and provenance

Run with NumPy and SciPy:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -O verify_bounded_secular.py

The completed checks include:

- 27 exact rational Toeplitz determinant identities;
- 15 spectra (clocks, fully coincident spectra, and seeded configurations);
- 270 checks inside the analytically proved contractive complex strip;
- 135 checks of the periodized kernel identity with an explicit infinite-tail bound;
- 30 derivative comparisons for (19), with Richardson finite differences;
- 45 finite logarithmic-tail inequalities from (10);
- direct characteristic-polynomial and positive-matrix determinant comparisons;
- 15 full BGS-formula/control probes, and exact finite CUE references.

Checks use explicit exceptions and are not disabled by Python optimization.
Exact rational checks and floating-point diagnostics are distinguished in
verification.json. The code uses the stable sin/sinh/log1p formula rather than
subtraction of separately enormous determinants.

Source boundaries:

1. Supplied bgs_collision_crossover_2026-10-15/THEOREM.md, especially Section 10:
   its square-root-time subfamily does not estimate the microscopic denominator.
2. ChurilovMaksim/BGS, supplement/fixed_map/weighted-secular/determinant_boundary.md:
   correct finite CUE ratio formula; deterministic ratio convergence is open.
3. J. B. Conrey, D. W. Farmer, M. R. Zirnbauer, arXiv:math-ph/0511024:
   established Haar-averaged characteristic-polynomial ratio identities.
   Their Haar average is not silently identified with a deterministic origin average.
4. A. Soshnikov, arXiv:math/0002099: determinantal-process and convergence background.
5. R. Band, J. M. Harrison, C. H. Joyner, arXiv:1205.4214:
   finite pseudo-orbit organization is established work, not a new BGS closure.

The contractive ratio, its positive-matrix interpretation, and the elementary
Laplace approximation argument are stated with proofs, not as a verified claim
of originality. No complete literature-priority review was performed.

**Unclosed:** the model-specific asymptotic mean in (20), all mixed bounded
ratios, the uniform integrability needed for the stronger correlation target,
and the full signed Heisenberg hierarchy. This note removes a representation
and numerical-conditioning obstacle. It is NOT a proof of BGS.
