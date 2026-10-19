# From fixed-channel TV compactness to the full normalized path clock

17 October 2026. New conditional analytic result, outside BGS.
Theorem below has a complete written proof; author self-review and exact
finite controls of its kernel identities are recorded separately. The Haar
target and BGS remain open. No external or formal certification is claimed.

## 1. Statement

For each N let S_N be a unitary input with uniformly randomized retained
labels. Retain two ports, close E_N by independent uniform phases, and write
r_N=N-2, F_N for the Schur output, T_N=|F_(N,12)|^2. Average over the two
sources b. Define the full positive occupation law by

    Q_(N,K)(k,alpha)=(1/2)binom(K,k)
       sum_b |[Z^alpha] F_(N,3-b,b)^k F_(N,b,b)^(K-k)|^2.    (1)

Its random variables are B=k, Alpha=alpha, and L=sum_e alpha_e. Their
definition includes both the input ensemble, if any, and coefficient weights.
For an independent uniform source b and Haar boundary phases define

    A_(N,b,e)=(F_N e_b)^*[-i partial_phi_e](F_N e_b)
             =tau_e |v_e^*F_N e_b|^2>=0,
    J_N=(1/r_N)sum_e A_(N,b,e).                            (2)

Use the exact Schur consistency and permutation symmetry of the prior
framework. The additional input needed here is ONLY:

    for every fixed v>=2, the laws mu_(N,v) of the v-port
    phase reductions are relatively compact in total variation.       [TC]

The preceding fixed-channel compactness proof supplies [TC] under its rank
condition R, hence under the explicitly stated full growing-channel input G.
That G proof remains conditional on its named project one-step inputs. No
new unconditional BGS conclusion is inferred from it here.

**Theorem.** Assume [TC]. For EVERY sequence of integers K_N->infinity,

    W1( law_(Q_(N,K_N))(B/K_N,L/(K_N r_N)),
        law(T_N,J_N) ) ->0.                               (3)

Here W1 on [0,1] times [0,infinity) uses |t-t'|+|j-j'|. There is no
condition K_N/N->0 and no unproved uniform resolvent-derivative bound.
The laws of J_N and L/(K_N r_N) in (3) are uniformly integrable.
They need not concentrate at their common mean. Under complete escape that
mean is 1/2, but its normalization does not identify the joint law in (3).

More basically, for every fixed number q of sampled distinct internal marks,

    W1( law_(Q_(N,K_N))(B/K_N,Alpha_1/K_N,...,Alpha_q/K_N),
        law(T_N,A_(N,b,1),...,A_(N,b,q)) ) ->0.             (4)

The SAME source b is used for all current coordinates in the second law.

## 2. Finite-dimensional kernels and a useful TV-to-W1 estimate

Fix q. For V in U(2+q) close its q internal coordinates. Let M_K(V,.) be
the coefficient probability kernel (1) on the normalized endpoint count and
q occupations, and M_infinity(V,.) the boundary-current kernel (2) before
averaging the current coordinates. The fixed-colligation theorem proves

    W1(M_K(V,.),M_infinity(V,.))->0 for EVERY V.            (5)

Crucially, these kernels have a UNIFORM conditional first-moment bound:

    integral (t+sum_e a_e) M_K(V,d(t,a))<=1+q/2,
    integral (t+sum_e a_e) M_infinity(V,d(t,a))<=1+q/2.      (6)

This is the source-averaged tensor Kac identity, valid even at decoupled V.
It is stronger than an unconditional ensemble moment bound. For any input
probability laws mu,nu on U(2+q), with TV=one half of total variation,

    W1(mu M_K,nu M_K)<=(2+q) TV(mu,nu),                   (7)

and the same holds for M_infinity. To prove (7), split mu and nu into their
common submeasure and residual submeasures of equal mass delta=TV(mu,nu).
Couple the common output identically. On the residuals use any independent
coupling. Distance is bounded by the sum of the two nonnegative norm costs;
(6) bounds its expected contribution by 2 delta(1+q/2). This proves (7).
No boundedness of the realized clocks is asserted or needed.

For a fixed input law mu, mixture coupling and (5)--(6) give
W1(mu M_K,mu M_infinity)->0 by dominated convergence. By (7) this convergence
is uniform when mu ranges over a TV compact set: choose a finite TV net,
use the convergence at its finitely many points, and then let its mesh tend
to zero. It is also uniform over asymptotically TV relatively compact tails.

## 3. Exact identification of marked marginals

Choose q internal labels and first close all the other internal coordinates.
This gives V with law mu_(N,2+q), independently of the remaining phases.
Schur associativity identifies the remaining holomorphic transfer function
with the q-variable transfer function of V.

The same statement holds for the COEFFICIENT marginals in (1). Indeed, sum
|c_(alpha,beta)|^2 over the unmarked multi-index beta. Iterated Parseval
identifies it with the integral over the unmarked boundary phases of the
squared q-variable coefficient. Tonelli applies to the nonnegative sums.
The transfer column tensor has H2 norm one, so no unjustified evaluation
of a divergent boundary series is required.

Consequently the two laws in (4) are exactly

    mu_(N,2+q) M_(K_N),     mu_(N,2+q) M_infinity.         (8)

Apply the compact-set convergence of section 2 and [TC]. This proves (4).

There is another consequence needed for the full clock. By (7), the images
under M_infinity of a TV compact input family are W1 compact. Thus the current
one-mark laws are W1 relatively compact. By (4) the one-mark occupation laws
along K_N->infinity are asymptotically W1 relatively compact as well. In
particular, for X_N=Alpha_1/K_N and Y_N=A_(N,b,1),

    lim_(M->infinity) limsup_(N->infinity)
       [ E X_N 1_(X_N>M)+E Y_N 1_(Y_N>M) ]=0.              (9)

This is the needed uniform integrability; a bare bound E X_N<=1/2 would
not suffice. No inference from a bounded mean alone is used.

## 4. A sampling lemma for exchangeable nonnegative arrays

Let (U_N,X_(N,1),...,X_(N,r_N)) and
(V_N,Y_(N,1),...,Y_(N,r_N)) have internal permutation symmetry, U_N,V_N
in [0,1], r_N->infinity, and nonnegative coordinates satisfying (9).
Suppose every fixed q marked joint law converges to its counterpart in W1.
Then

    W1(law(U_N,r_N^-1 sum_e X_(N,e)),
       law(V_N,r_N^-1 sum_e Y_(N,e)))->0.                 (10)

Proof. Sample q distinct coordinates uniformly, independently given the full
array. Truncate coordinates at M. The conditional finite-population variance
of their sampled mean is at most M^2/(4q). The original and sampled means'
untruncated tails each have expected size at most E X_(N,1)1_(X_(N,1)>M).
Therefore natural coupling of U_N with itself gives

    W1(law(U_N,mean_all X),law(U_N,mean_q X))
       <=M/(2 sqrt q)+2 E X_(N,1)1_(X_(N,1)>M),           (11)

with an identical bound for Y. The map from q marked coordinates to their
mean is 1-Lipschitz for the sum metric, so the distance between the two sampled
laws tends to zero at fixed q. First let N->infinity, then choose M large
using (9), and finally choose q large. Equations (11) prove (10).

Apply this lemma with U_N=B/K_N, X_(N,e)=Alpha_e/K_N, V_N=T_N,
Y_(N,e)=A_(N,b,e). Equations (4), (9) give (3). Jensen's inequality for a
superlinear UI test, or the same truncation bound, gives uniform integrability
of both full averages from the one-coordinate UI in (9).

This lemma concerns averages of nonnegative marked observables with UI.
It makes NO claim about a central limit theorem for a sum of products
C_i S_ij with the same endogenous index; the previous matching-array
counterexample to that different inference remains valid.

## 5. A finite positive window now retains the full normalized clock

Add max_ij |S_(N,ij)|^2<=C0/N, and choose fixed 0<delta<1,

    L_-=floor((1-delta)log N/log log N),
    L_+=floor(N log N),
    K_N->infinity with K_N=o(log N).                      (12)

Normalize (1) after restriction L_-<L<=L_+. The prior positive path bound
gives discarded probability

    epsilon_N<=(2C0/N)sum_(j=0)^L_- j!
                         +K_N(N-2)/(2(L_++1))->0.        (13)

The upper cutoff in normalized clock coordinates tends to infinity:
L_+/(K_N r_N)~log N/K_N->infinity. By (9)--(11), the discarded upper-tail
FIRST CLOCK MOMENT also tends to zero. The discarded lower-tail first moment
is bounded by L_-/(K_N r_N)->0. Thus conditioning on the window changes the
joint endpoint/normalized-clock law by o(1) in W1, not just in weak topology.

For clarity, for a law lambda on a nonnegative normed space and an event A
of mass 1-epsilon, independent residual coupling gives

    W1(lambda,lambda(.|A))
       <= integral_(A^c) ||x||dlambda
                 +epsilon/(1-epsilon) integral_A ||x||dlambda. (14)

Use ||(t,j)||=t+j, (13), the preceding tail estimates and the bounded mean
to justify this step. In particular the previously chosen
K_N=floor((log N)^(2/3)) is allowed. The resulting FINITE positive law of
(k/K_N,L/(K_N r_N)) approximates law(T_N,J_N) in W1.

No quantitative rate for the clock coordinate is asserted: [TC] supplies
qualitative compactness and UI. The earlier explicit O((log N)^(-1/3))
bound for the endpoint marginal alone remains valid independently of [TC].

## 6. Haar benchmark and an important nonconcentration check

The exact Haar cavity law, already derived in attachment MC16--MC24, is

    Q~H_2 independent of (V,xi_e),
    C_e=V^(1/2)xi_e,
    V=(GG^*)^(-1), G a 2 by 4 iid standard complex Gaussian matrix,
    xi_e iid CN(0,I_2).                                   (15)

It is a benchmark input for THIS section only, not for (3). Since
A_(b,e)=|C_e^*Qe_b|^2, conditional laws of large numbers give

    J_N -> e_b^*Q^*VQe_b in distribution and L1.            (16)

The matrix V is unitarily invariant, so Q^*VQ has the same law as V and is
independent of Q. Its diagonal entry is 1/Gamma(3,1). To derive this last
fact, write the two rows of G as g_1,g_2 in C^4. Block inverse gives
V_11^-1=||projection_(g_2^perp) g_1||^2, the sum of three independent
standard complex squared magnitudes. Thus the limiting density is

    j -> exp(-1/j)/(2j^4), j>0; mean 1/2, variance 1/4.   (17)

It is independent of T~Uniform[0,1]. Combining (3) with this benchmark
identifies the Haar averaged path law for ANY K_N->infinity as the product
of that uniform law and (17). This is a consequence for a reference model;
the inverse-Wishart delay mechanism itself is prior, not a novelty claim.
It also excludes replacing J_N by the deterministic 1/2, even for Haar.

## 7. Precise remaining mathematical task

The two-port target still requires identification of the endpoint marginal
of law(T_N,J_N), or equivalently of the finite positive histogram weights
defined previously. Neither [TC] nor (3) proves independence of T_N from J_N,
the inverse-gamma law (17) for a deterministic start, or conditional isotropy
of the marked cavity projectors. Even E T_N->1/2 remains unproved in the
full stated class. What is now closed is the uniform tensor/large-N transfer
and extension from finitely many positive occupations to the WHOLE clock.

Dependencies for (3): exact Schur associativity, Parseval, the fixed-unitary
tensor-current theorem, source-averaged Kac bound, and [TC]. [TC] is supplied
by the pinned prior proof under R/G. Source (15) is used solely in section 6;
its exact attachment excerpt and hash are recorded in proof_inputs.json.

## 8. Extension to any fixed number of retained channels

The transfer argument is not restricted to two outputs. Fix m>=1. For a
uniform source b, expand the ordered tensor column (F_N e_b)^tensor K and
group equal output coordinates into the multinomial count n=(n_1,...,n_m),
sum_a n_a=K, together with the internal occupation alpha. This defines the
same nonnegative coefficient probability law with multinomial multiplicity.
Its joint endpoint/current limit is

    (n/K,L/[K(N-m)]) compared in W1 with
    ((|F_(N,ab)|^2)_(a=1)^m,
          (N-m)^-1 sum_e (F_N e_b)^*D_e(F_N e_b)).         (18)

Under [TC] at levels m+q for every fixed q, their W1 distance tends to zero
for ANY K_N->infinity. The proof is identical with the diagonal unitary
diag(exp(i s_a/K)) in (5) of the fixed-colligation proof. The crucial
conditional mean bound becomes 1+q/m, since sum_b A_(b,e)=tau_e. Thus (7)
has constant 2+2q/m. Sampling closes the full normalized clock as before.

In the Haar reference model, (18) tends to the product of the uniform
Dirichlet(1,...,1) law on the output simplex and 1/Gamma(m+1,1). Indeed
the benchmark has V=(GG^*)^-1 with G of size m by 2m; the inverse diagonal
entry is the squared norm of a Gaussian projected onto an (m+1)-dimensional
orthogonal complement. Its reciprocal has that gamma law. Unitary invariance
again gives independence from F_N. Its mean is 1/m; when m>1 its variance
is 1/[m^2(m-1)]. These reference limits are not asserted for the original
deterministic input family.

## 9. An exact interior radial transform at the boundary scale

The joint limit has a useful expression involving only interior resolvents.
For real t, lambda>=0 and rho=exp[-lambda/(2K r_N)], Parseval gives EXACTLY

    E_(Q_(N,K)) exp[it B/K-lambda L/(K r_N)]
      =(1/2)sum_b E_Z
         [ exp(it/K)|f_b(rho Z)|^2+|g_b(rho Z)|^2 ]^K.     (19)

For lambda>0 these are strictly interior transfer functions, so no boundary
inverse is being estimated. Under [TC], for ANY K_N->infinity, (3) implies
that (19) differs by o(1) from

    E exp[it T_N-lambda J_N].                             (20)

Indeed the exponential test is bounded and Lipschitz, with constant at most
|t|+lambda in the chosen sum metric. The radial loss scale is precisely
1-rho of order 1/[K_N(N-2)]; replacing it by a mesoscopic regulator would
change the observable. This connects the positive occupation construction
to a bounded high-power radial resolvent observable without assuming a
uniform derivative expansion near the torus.

For the Haar benchmark, (20) tends to

    [(exp(it)-1)/(it)] integral_0^infinity
               exp(-lambda j-1/j)/(2j^4) dj,              (21)

with the first factor interpreted as 1 at t=0. For the deterministic model
this evaluation is OPEN. The existing all-fixed-order normal-source/path
comparisons do not evaluate (19): their initial law remains unidentified,
and they do not supply a growing physical-source-product identification.
No transfer to the signed balanced trace target is claimed from (19).
