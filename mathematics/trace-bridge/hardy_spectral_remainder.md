# Sharp clock extremum and an exact positive remainder for radial secular statistics

**Stable claim:** `BGS-TRACE-091`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** p is the characteristic polynomial of a unitary, with all roots on the unit circle. Self-inversiveness alone is insufficient. Required CUE excesses are positive and unproved for the physical family.

Canonical status is [the claim ledger](../../record/claim_ledger.md); source `S15` is preserved verbatim in [the imported record](../../archive/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s15). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../../archive/evidence/executions/20261016/chat-integration/receipt.json).


Date: 15 October 2026.

## Status

This note proves finite-dimensional identities for the FULL radial characteristic-polynomial ratio of any unitary matrix. In particular, the normalized origin-averaged ratio is minimized by the regular N-clock, with an explicit nonnegative Hardy-space remainder and an equality classification. A related sum-of-squares identity recovers the project's previously established Abel floor.

These statements do not prove a CUE or Sine_2 limit for the prescribed propagator U_N=exp(i*10^-80*N*A_N)M_N. The value of the positive remainder for that family is still unestimated at the required scale. No independent external refereeing, Lean verification, or literature-priority claim is made. This canonical copy includes the 16 October integration review.

The Hardy-space projection used here is elementary rational-function orthogonality. It is not presented as a newly invented general method. The previous packet already defined the bounded radial ratio and its CUE benchmark; those facts are credited rather than counted again as new results.

## 1. Unchanged observable

For a unitary U of dimension N, set

    p(z)=det(I-z U)=sum_{k=0}^N c_k z^k.

Then c_0=1, |c_N|=1, and

    c_{N-k}=c_N conjugate(c_k).                              (1)

This follows by taking elementary symmetric functions of eigenvalues on the unit circle, including multiplicities. The converse from coefficient self-inversiveness is not assumed: for example 1+3z+z^2 is self-inversive but its roots are off the unit circle. For such polynomials q need not be zero-free in the disk, so the Hardy/Blaschke proof below would fail. Fix 0<s<t and put

    a=exp(-s/N), b=exp(-t/N), x=a^N=exp(-s), y=b^N=exp(-t).

The full bounded statistic is

    Z_U(s,t)=exp(-(t-s)) * (1/(2pi)) integral_0^{2pi}
                       |p(a exp(i theta))/p(b exp(i theta))|^2 dtheta. (2)

It is exactly the same uniformly shifted spectral statistic as in the previous packet (the sign of the uniform angular variable is immaterial). No phase, parameter, matrix, or noise ensemble is introduced in (2). The denominator is zero-free on and inside the unit circle. The pointwise normalized ratio is in (0,1].

Define the clock value

    Z_cl(s,t)=exp(-(t-s))*[1+(exp(-s)-exp(-t))^2/(1-exp(-2t))]. (3)

It is independent of N.

## 2. Main finite identity and sharp minimum

Let

    A=(1-xy)/(1-y^2),    D=(x-y)/(1-y^2),
    q(z)=p(bz),
    q^*(z)=z^N conjugate(q(1/conjugate(z))),
    B(z)=q^*(z)/q(z).

The polynomial q^* has all its zeros in |z|=b; consequently B is a finite Blaschke product (up to a unimodular factor), even when roots coincide. On |z|=1, |B(z)|=1, and

    B(0)=conjugate(c_N)y.

Define the rational remainder

    E_{U;a,b}(z)=p(az)/p(bz)-A-c_N D B(z).                    (4)

Use the normalized Hardy norm

    ||f||_{H2}^2=(1/(2pi)) integral_0^{2pi}|f(exp(i theta))|^2dtheta.

**Theorem.** For every finite unitary spectrum,

    Z_U(s,t)=Z_cl(s,t)+exp(-(t-s))*||E_{U;a,b}||_{H2}^2.      (5)

In particular Z_U(s,t)>=Z_cl(s,t). For N>=2, equality at any one fixed pair 0<s<t holds if and only if the spectrum is a rotated regular N-gon. At N=1 every spectrum is such a clock.

### 2.1. Rational orthogonality, proved directly

Let

    K_B={ R(z)/q(z): R is a polynomial of degree at most N-1 }.

Every element g of this N-dimensional space is orthogonal in H2 to B(z)z^j for j>=0. Indeed, on the unit circle,

    g(z) conjugate(B(z)z^j)=R(z)z^{-j}/q^*(z).

The rational function R/q^* is analytic outside its poles in |z|=b and vanishes at infinity. Its Laurent series for |z|>b contains only strictly negative powers; multiplying by z^{-j} introduces no constant coefficient. Its circle average is zero. This proves the needed orthogonality, without assuming simple roots or a minimum spacing.

Since the leading coefficient of q^* is 1, the function

    g(z)=p(az)/q(z)-c_N x B(z)

belongs to K_B. Its value at zero is g(0)=1-xy.

The reproducing vector for evaluation at zero on K_B is

    k_0(z)=1-conjugate(B(0))*B(z)=1-c_N y B(z).

It belongs to K_B because its degree-N numerator cancels, has norm squared 1-y^2, and <g,k_0>=g(0) by the orthogonality just proved. Here <f,g>=integral f conjugate(g).

Thus

    p(az)/q(z)=c_N x B(z)+A k_0(z)+E(z),

and all three summands are mutually orthogonal: E is in K_B and E(0)=0. Therefore

    ||p(az)/p(bz)||_{H2}^2
       =x^2+(1-xy)^2/(1-y^2)+||E||_{H2}^2
       =1+(x-y)^2/(1-y^2)+||E||_{H2}^2.

Since x-Ay=D, E is exactly (4). This proves (5).

### 2.2. Equality classification

Using (1), equation (4) is exactly

    E(z)= [sum_{k=1}^{N-1} c_k d_k(a,b) z^k]/p(bz),         (6)
    d_k(a,b)=a^k-A b^k-D b^{N-k}.

The endpoint weights d_0,d_N vanish, and every interior weight is strictly positive. To prove this, apply the difference operator

    (L v)_k=v_{k+1}-(b+b^{-1})v_k+v_{k-1}.

The b^k and b^{N-k} terms are annihilated, while

    (L d)_k=(a+a^{-1}-b-b^{-1})a^k<0.

The last inequality uses 0<b<a<1. A nonpositive interior minimum of d, with zero endpoints, would instead give Ld>=0 there, a contradiction. Hence d_k>0 for 1<=k<N.

It follows that E=0 if and only if all c_1,...,c_{N-1} vanish. Thus p(z)=1+c_N z^N, whose zeros, and hence the eigenvalues of U, form a rotated regular N-gon. This proves the equality statement, including repeated-spectrum exclusion.

## 3. Positive kernel extension, not just a scalar inequality

Keep real 0<b<1 fixed but allow complex numerator parameters a,c. Set x=a^N, v=c^N, y=b^N and define E_a by (4), with A and D allowed to be complex. The same orthogonal decomposition gives

    integral p(a z) conjugate(p(c z))/|p(b z)|^2 dtheta/(2pi)
       =1+(a^N-b^N)(conjugate(c)^N-b^N)/(1-b^(2N))
          +<E_a,E_c>.                                      (7)

Therefore the difference between the full kernel and the displayed clock kernel is positive semidefinite for every finite collection of numerator parameters. Its rank is at most N-1, since E_a belongs to K_B and has value zero at the origin.

This is a Gram-matrix assertion, not an entrywise lower bound for complex cross-correlations. It does not replace the mixed shifted determinant criterion of the previous packet by a single scalar mean.

## 4. Exact Abel sum-of-squares identity

For 0<r<1 put q_r(z)=p(rz), y=r^N, B_r=q_r^*/q_r, and

    F_r(z)=(z/N) q_r'(z)/q_r(z).

Its Taylor expansion is

    F_r(z)=-(1/N) sum_{m>=1} r^m Tr(U^m) z^m,

so

    ||F_r||_{H2}^2=(1/N^2) sum_{m>=1}r^(2m)|Tr U^m|^2.      (8)

Subtract c_N y B_r from F_r to obtain an element of K_{B_r}; its value at zero is -y^2. The same projection gives

    R_{U,r}(z)=F_r(z)+y^2/(1-y^2)-c_N y B_r(z)/(1-y^2),

and the exact identity

    (1/N^2) sum_{m>=1} r^(2m)|Tr U^m|^2
       = y^2/(1-y^2)+||R_{U,r}||_{H2}^2.                    (9)

With r=exp(-s/N), this is

    L_U(s)=1/(exp(2s)-1)+||R_{U,r}||_{H2}^2.                (10)

The scalar lower bound in (10) is ALREADY proved in the project (TRACE-007), using the Cohn-Kumar universal-optimality theorem. The contribution here is a direct rational orthogonality proof together with the explicit positive remainder, not a claim to have discovered that lower bound.

Equality in (9) also characterizes the regular clock. One way to see this is to use the self-inversive coefficient identity: a nonzero intermediate coefficient c_k would require simultaneously

    k/N + y^2/(1-y^2) = y^2 r^(-2k)/(1-y^2)

and its reflected equation at N-k. Adding the two equations is impossible because r^(-2k)+r^(-2(N-k))<1+r^(-2N) for 0<k<N. Equivalently differentiate the positive remainder in (5) at a=b with the correct fixed-N order of operations.

## 5. Exact CUE reference and the unresolved physical energy

For the Haar U(N) reference, the established one-ratio identity gives

    E_CUE ||p(az)/p(bz)||_{H2}^2
       =1+(a-b)^2/(1-b^2) * (1-a^(2N))/(1-a^2).              (11)

This is an ensemble identity and is not imposed on the deterministic U_N.
Combining (11) with (5), the exact mean of the positive remainder is

    E_CUE ||E_{U;a,b}||_{H2}^2
       =(a-b)^2(1-a^(2N))/[(1-b^2)(1-a^2)]
           -(a^N-b^N)^2/(1-b^(2N)).                         (12)

At the microscopic radii a=exp(-s/N), b=exp(-t/N), its limit is

    E_CUE_limit(s,t)
       =(t-s)^2(1-exp(-2s))/(4*s*t)
          -(exp(-s)-exp(-t))^2/(1-exp(-2t)).                 (13)

This is strictly positive when 0<s<t. For example, after rewriting with hyperbolic sines, positivity follows from strict convexity and monotonicity of log(sinh(x)/x) for x>0: its second derivative is 1/x^2-csch(x)^2>0.

At s=1,t=2:

    Z_clock = 0.3881443433921127...
    Z_CUE_limit = 0.4076409877718897...
    E_CUE_limit = 0.052997374133475834...

For the ORIGINAL BGS operator, the scalar target is therefore exactly

    ||E_{U_N;exp(-1/N),exp(-2/N)}||_{H2}^2
           -> 0.052997374133475834... .                      (14)

It is NOT a vanishing-remainder target. Forcing this energy to zero would instead force the clock value of the bounded test. This corrects a potential misuse of positivity but does not prove (14).

The pair target equivalently asks in (10) for

    ||R_{U_N,exp(-s/N)}||_{H2}^2
       -> (1-exp(-2s))/(4*s^2)-1/(exp(2s)-1).                (15)

A positive norm representation does not determine the norm. Neither (14) nor (15) is evaluated here for the prescribed exp(i*10^-80*N*A_N)M_N.

## 6. The attempted use of available short traces

The residual numerator (6) makes the first attempted closure test explicit. At fixed s,t write u=k/N. Its weight is

    d_{s,t}(u)=exp(-s*u)-A exp(-t*u)-D exp(-t*(1-u)),

where A,D no longer depend on N. In particular d_{s,t}(0)=0 and d_k=O_{s,t,L}(1/N) for k<=L fixed.

Suppose Tr(U_N^j)=O_j(1) for every fixed j. Newton's identities then bound each fixed secular coefficient c_j. The first L Taylor coefficients of 1/p(bz) are polynomials in the same finite list of traces and are bounded too. Equation (6) therefore proves

    sum_{j=0}^L |[z^j]E_{U_N;a,b}(z)|^2=O_{s,t,L}(N^-2).    (16)

The project's FM-013 supplies the stated fixed-trace input for its unchanged odd-dimensional family, with its recorded project-proof status and ineffective thresholds. This pass does not re-prove FM-013.

Thus low Taylor coefficients of the newly isolated positive remainder actually disappear. They do not supply its required nonzero limiting norm in (14). The unestimated part lies in the growing Taylor degrees. Treating (16) as control of the whole Hardy norm would be an invalid interchange of a finite truncation and N->infinity.

This is the concrete point where the direct attempt remains incomplete. The positive remainder includes the FULL physical coefficients, not an edge-type or phase-balanced subset. It retains all cancellations enforced by unitarity, but has not eliminated the need for a model-specific long-scale estimate.

## 7. A trace-norm stability corollary

For completeness, the new energy inherits a dimension-independent stability estimate. For unitaries U,V of equal size,

    |Z_U(s,t)-Z_V(s,t)| <= log(t/s) ||U-V||_1,                (17)

where ||.||_1 is the unnormalized trace norm. One may also use a sharper bound with the trace norm of the principal Hermitian logarithm.

Proof: the microscopic test h_{s,t}(x)=log[(t^2+4pi^2 x^2)/(s^2+4pi^2 x^2)] has total variation ||h'||_1=4log(t/s). Write U=exp(iH)V, with ||H||_1<=pi||U-V||_1/2; this follows by scalar functional calculus from |theta|<=pi|exp(i theta)-1|/2. Along exp(iuH)V, summed absolute eigenangle velocities are at most ||H||_1, including multiplicities via eigenspace compression. Uniform-origin integration of the exponential linear statistic costs ||h'||_1/(2pi) times that sum. Integration in u proves (17). All derivatives of h are integrable, so periodization and differentiation are justified at fixed N.

Consequently the excess energies in (5) differ by at most exp(t-s)log(t/s)||U-V||_1. This is a transfer bound, not an evaluation of either endpoint. The underlying phase-matching argument is prior project methodology; no novelty is asserted for it.

## 8. Verification performed

The autonomous verifier contains two mathematically different checks.

1. Exact rational/complex-rational checks. Characteristic polynomials are assembled from rational unit-modulus eigenvalues, including repeated roots, rotated spectra, and clocks. A finite Stein equation is solved exactly for the companion recurrence; it evaluates the INFINITE Hardy norm, rather than replacing it with a truncated Taylor sum. There are 24 choices of spectrum and radii. Both (5) and (9), strict interior weights, and equality classification are checked exactly. An additional 24 complex cross-identities verify (7).

2. Floating-point checks. There are 23 spectra: clocks, clusters, random test spectra, and five matrices using the exact BGS formula at EXPLICIT PROXY couplings 0.03 or 0.30. They compare the ratio integral, its positive product form, the rational remainder norm, the Abel norm, and the orthogonal cross terms. No computation at these parameters is advertised as an asymptotic result for 10^-80.

Executed command:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -O verify_hardy.py

All checks use explicit exceptions, not ordinary assert statements. The run completed. The largest radial identity error was 4.45e-16, and the largest Abel identity error was 7.11e-15. Exact values and full floating records are in verification.json.

### Quadrature caution

The old contractive-ratio quadrature uses O(N log(1/epsilon)) angles for fixed radii parameters. That bound must NOT be blindly applied to the Blaschke remainder: a clustered spectrum can make its inner factor wind on an O(N^-2) angular scale.

The new checker separately controls these norms. If h is analytic in |z|<=R>1 and |h|<=H there, the trapezoidal error for |h|^2 on M points is bounded by

    2H^2/[(1-R^-2)(R^M-1)].                                 (18)

Cauchy's coefficient estimate proves (18) by summing the aliased Fourier coefficients of |h|^2. Choose R=exp(s/(2N)). The elementary Blaschke bound is

    |B_b(z)| <= [(R-b)/(1-bR)]^N,   |z|=R.

The checker uses this bound and corresponding explicit bounds for the rational terms, selects M conservatively in logarithmic arithmetic, and records the resulting analytic expression for the quadrature error. At worst M is of order N^2 here. Roundoff and spectral computation errors remain separate; no interval certification of the numerical eigenphases is claimed.

## 9. Provenance and exact remaining task

Sources read:

- Supplied bgs_bounded_secular_2026-10-15/THEOREM.md, especially its bounded ratio, CUE calibration, and unchanged physical target.
- ChurilovMaksim/BGS, mathematics/fixed_map_resolvent_frontier.md, its already proved TRACE-007 Abel floor and Cohn-Kumar proof.
- ChurilovMaksim/BGS, mathematics/fixed_time_wavepacket_trace_bound.md, the precise fixed-j scope of FM-013.
- ChurilovMaksim/BGS, mathematics/polar_wkb_quantization_stability.md, for the boundary of prior spectral-transfer methods (no WKB endpoint limit is imported).
- Conrey, Farmer, Zirnbauer, arXiv:math-ph/0511024, for established Haar ratio identities.

The literature search and repository search did not certify priority for (5)-(7). The proof is stated on its own merit, not as a Fields-level result or a claim that classical Hardy-space tools are new.

What has been obtained is a sharp universal minimum and an exact nonnegative remainder for the whole bounded statistic, plus an analogous Abel identity. What has NOT been obtained is the required physical value of that remainder. Unitarity yields the minimum but does not force the CUE excess. The main model-specific Heisenberg-scale comparison and all fixed higher correlations are still open in this continuation.
