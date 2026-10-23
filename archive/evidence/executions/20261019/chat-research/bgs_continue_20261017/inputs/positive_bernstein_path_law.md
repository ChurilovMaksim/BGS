# A positive finite path law approximating the entire transmission distribution

17 October 2026. New continuation of the attachment's matched-occupation
expansion, positive clock and low-degree Hardy bound. Working analytic proof;
finite controls are recorded separately. This does not evaluate the limiting
path law and does not prove BGS or two-channel universality.

## 1. Setting and exact probability measure

Let S be any N by N unitary, retain two specified ports A, and close E=A^c
by independent uniform phases. Write r=N-2 and

    F(Z)=S_AA+S_AE(I-Z S_EE)^(-1)Z S_EA,
    T=|F_12(Z)|^2=|F_21(Z)|^2 on the phase torus.

The holomorphic matrix F is contractive in the polydisk and unitary almost
everywhere on its distinguished boundary. No Gaussian input is used.
For source b in {1,2}, put a=3-b and

    f_b(Z)=F_ab(Z),   g_b(Z)=F_bb(Z).

For integers K>=1, 0<=k<=K define the Taylor coefficients by

    f_b(Z)^k g_b(Z)^(K-k)=sum_alpha c_(b,k,alpha) Z^alpha.

Define a nonnegative measure on {0,...,K} times the nonnegative integers:

    Q_(K,k,L)=(1/2) binom(K,k)
        sum_(b=1,2) sum_(|alpha|=L) |c_(b,k,alpha)|^2.       (1)

It is a PROBABILITY measure. Moreover its k-marginal is exactly

    sum_L Q_(K,k,L)=binom(K,k) E[T^k(1-T)^(K-k)].          (2)

Indeed, Parseval gives (2), and summing the right side in k gives 1.
Thus, if (B,L) has law Q, then B alone has the mixture distribution

    T sampled from its actual phase law, then B|T ~ Binomial(K,T). (3)

The auxiliary path-length L is not claimed independent of B or T.
Equation (3) describes the marginal and supplies a coupling for that marginal.
The coefficients in (1) are coherently summed within each occupation class
BEFORE squaring. Replacing them by sums of individual path probabilities
would define a different measure and would lose quantum interference.

## 2. An exact linear clock for tensor columns

For a fixed set of relative phases eta write z=w eta. The column

    x_b(w)=F(w eta)e_b

has boundary norm one. Its K-fold tensor power has norm one and, in the
standard ordered tensor basis, its entries are all products f_b^k g_b^(K-k),
with multiplicity binom(K,k). This realizes (1) as squared coefficients of
an analytic vector, without introducing signs.

On the circle, product differentiation gives the exact identity

    (x_b^tensor K)^* w (x_b^tensor K)'
      =K x_b^* w x_b'.                                  (4)

The other K-1 tensor factors contribute x_b^*x_b=1. This is why the clock
is linear in K, rather than quadratic. Fourier orthogonality identifies
the integrated left side with the total degree-weighted coefficient mass.
Summing (4) over both columns and dividing by 2 gives

    sum_(k,L) L Q_(K,k,L)
       =(K/2) E_eta deg(det F(w eta)) <=K r/2.            (5)

The matrix inner function is rational. Its nonnegative Wigner--Smith
clock has total integral equal to the degree of its determinant, at most r.
Equivalently (5) follows from the exact finite controllability/Kac identity.
Dark unitary modes may reduce the degree and are correctly included in <=.
If |S|^2 is irreducible, the attachment's generic escape argument yields
degree r for almost every eta, so equality holds in (5).

The average over the two sources is essential for the universal factor 1/2.
No assertion that each individual column has clock r/2 is made.

## 3. Low-degree mass does not grow with the tensor degree K

Let Pi_<=l denote Hardy projection onto total internal degree at most l.
Multiplication by the analytic vector x_b(Z)^tensor(K-1) has operator norm
at most 1, since ||x_b(Z)||<=1 in the polydisk and on its boundary.
Analyticity prevents terms of degree >l from contributing below l. Hence

    ||Pi_<=l x_b^tensor K||_H2^2
       <=||Pi_<=l x_b||_H2^2.                            (6)

This proof uses the ordered tensor space; passing to symmetric coordinates
only groups equal entries with their binomial multiplicities.

Suppose now max_ij |S_ij|^2<=C0/N. For a single matrix entry, matched
occupation grouping and Cauchy--Schwarz give, at total degree j,

    q_j(entry)<=j! q_j(classical)<=j! C0/N, j>=0.        (7)

For j>=1, the classical coefficient is
P_aE P_EE^(j-1) P_Eb. It is at most C0/N: the final vector P_Eb is bounded
by C0/N and the total row mass of P_aE P_EE^(j-1) is at most 1.
At j=0 this is just P_ab<=C0/N.

There are two entries in each column. From (6)--(7), for EVERY K>=1,

    sum_(k,L<=l) Q_(K,k,L)
       <=(2 C0/N) sum_(j=0)^l j!.                        (8)

Neither the classical gap nor the cooperon gap is used in this bound.

## 4. A finite positive approximation with an explicit Wasserstein error

Choose integers 0<=L_-<L_+ and put

    epsilon=(2 C0/N) sum_(j=0)^L_- j!
              + K(N-2)/[2(L_++1)].                      (9)

By (5), (8), the probability that L is outside (L_-,L_+] is at most
epsilon. If epsilon<1, the mass in that interval is nonzero. Define the
probability measure

    nu_(N,K,window)=
      sum_(k=0)^K [sum_(L_-<L<=L_+) Q_(K,k,L)] delta_(k/K)
      / sum_(k=0)^K sum_(L_-<L<=L_+) Q_(K,k,L).          (10)

Then, for W1 on [0,1] with distance |s-t|,

    W1(law(T),nu_(N,K,window))
       <=1/(2 sqrt K)+epsilon.                          (11)

Proof: the coupling (3) gives
E|B/K-T|<=E sqrt(T(1-T)/K)<=1/(2 sqrt K).
Conditioning the joint law of (B,L) on the window changes its B/K marginal
in total variation by at most the discarded mass, hence changes W1 by at
most that mass because the diameter is one. This proves (11). No division
by an uncontrolled small retained mass is hidden in the estimate.

For fixed 0<delta<1 choose, at sufficiently large N,

    L_-=floor((1-delta) log N/log log N),
    L_+=floor(N log N),
    K=floor((log N)^(2/3)).                              (12)

The first term in (9) is at most N^(-delta+o(1)), by Stirling's formula.
The second is O((log N)^(-1/3)), as is 1/sqrt K. Consequently

    W1(law(T),nu_(N,K,window))
       =O_(C0,delta)((log N)^(-1/3)).                    (13)

The construction and bound are uniform over all flat unitary inputs and
over the retained pair. Computing (10) directly is generally expensive:
the statement is a finite, positive reduction, not an efficiency claim.

## 5. What has and has not been reduced

Under the original three hypotheses, T_N tends to Uniform[0,1] if and only
if the explicitly defined positive measures (10), with (12), tend to that
same law. This is an equivalent criterion with a controlled approximation
error for the ENTIRE distribution, not just any fixed set of moments.

There is a particularly concrete target for this criterion. If T is uniform,
then the integral of binom(K,k) T^k(1-T)^(K-k) is exactly 1/(K+1).
Let G_K=(K+1)^(-1) sum_(k=0)^K delta_(k/K). Direct quantile integration gives

    W1(G_K,Uniform[0,1])=(2K+1)/[6K(K+1)]<=1/(2K).

Thus a finite sufficient estimate is

    W1(law(T),Uniform[0,1])
       <=1/(2 sqrt K)+epsilon+W1(nu_(N,K,window),G_K)+1/(2K). (14)

The reverse triangle inequality makes convergence of the last W1 term
to zero an equivalent remaining condition along (12). Without the extra
regularity assumption used in section 6, TV closeness of the discrete weights
to 1/(K+1) is sufficient; necessity of that stronger statement is not asserted.

In particular, a concrete unresolved task is to prove that the cumulative
weights in (10) approach those of this uniform grid, with all occupation
amplitudes and their cancellations retained. Even the first weighted sum
sum_k (k/K) nu({k/K}) has not been evaluated asymptotically here.

Unlike the attachment's holomorphic mixed Bernstein--determinant wedge
(AP13), (1)--(11) carry no determinant Fourier weight. Unlike an expansion
in powers T^k followed by a signed polynomial approximation, the measure
in (10) is nonnegative and normalized. These improvements do not remove
the main dynamical task: evaluating its masses on internal lengths from
roughly log N/log log N through N log N. Even proving its first moment
tends to 1/2 in full generality remains open in this program.

The exact interference examples with means 23/45 and 1-1/sqrt(5) remain
valid controls. Neither positivity nor clock normalization forces the
Bernstein marginal to be the uniform-law binomial mixture. Replacing
the unknown marginal by that target would assume the desired conclusion.

## Dependency record

Finite unitary Schur contractivity and boundary unitarity; Parseval;
the elementary tensor-product identity (4); the finite matrix Kac/degree
bound; the matched-occupation factorial estimate and Hardy contraction;
the binomial variance bound. All appear here with their role stated.
G, project local trace inputs, external spectral universality and any
conditional isotropy of cavity columns are not used.

## 6. Combining the new compactness result with beta smoothing

The discrete measure (10) does NOT approximate a continuous transmission
law in TV: discrete and absolutely continuous probability measures are
mutually singular. For example, G_K and Uniform[0,1] have TV distance one
at every K, despite the explicit W1 convergence above. The following
additional result avoids that obstruction by a specified Markov smoothing.

Put b_(K,k)(t)=binom(K,k)t^k(1-t)^(K-k), and let
p_k^window be the normalized weights in (10). Define the probability density

    h_(N,K,window)(t)=(K+1) sum_(k=0)^K p_k^window b_(K,k)(t). (15)

It is nonnegative, integrates to one, and is bounded by K+1. Operationally,
given k from the path measure, sample a Beta(k+1,K-k+1) variable. Uniform
grid weights p_k=1/(K+1) give the density one EXACTLY at every K.

For a probability measure mu on [0,1], define

    (M_K mu)(dy)=(K+1) sum_k b_(K,k)(y)
                        [integral b_(K,k)(t) mu(dt)] dy.   (16)

The kernel is symmetric, positive and preserves Lebesgue probability;
it is a contraction in TV and in L1 on densities. For every fixed f in L1,

    ||M_K(f dt)-f dt||TV ->0.                              (17)

Here is a direct proof. Given t, take B~Binomial(K,t), then
Y|B~Beta(B+1,K-B+1). Its conditional mean is (Kt+1)/(K+2), and its
conditional variance is at most
K/[4(K+2)^2]+1/[4(K+3)]. Thus sup_t E|Y-t|^2<=2/K.
For continuous f the function M_K f converges uniformly to f, by uniform
continuity and this bound. Symmetry identifies this function operator
with the density operator. Approximate an arbitrary L1 function by a
continuous one and use L1 contraction to obtain (17).

This convergence is uniform on every compact subset of L1, by a finite
net. More generally, suppose a sequence mu_N is TV relatively compact
and all its N->infinity cluster measures are absolutely continuous. A
finite net of AC cluster measures approximates its tail in TV. Applying
the kernel contraction and (17) to this finite net proves, for ANY K_N->infinity,

    ||M_(K_N) mu_N-mu_N||TV ->0.                          (18)

Apply (18) to mu_N=law(T_N), under the assumptions of the new fixed-channel
TV compactness theorem. The full B marginal in (2), followed by the beta
kernel, is precisely M_K mu_N. Removing the path-length complement changes
its law by at most the discarded mass. Therefore with (12),

    ||h_(N,K_N,window)(t) dt-law(T_N)||TV ->0.             (19)

The NEW hypothesis in (19) is the full growing-channel input G (or the
weaker rank-compactness assumption in the companion proof), together with
exact Schur consistency and permutation symmetry. It was NOT used in
(1)--(14). No quantitative TV rate is claimed: (18) has only the modulus
supplied by the unknown compact L1 family. The rate (13) is a W1 rate only.

Under those explicit extra inputs, the two-channel conjecture is equivalent
to the concrete positive polynomial-density statement

    integral_0^1 |h_(N,K_N,window)(t)-1| dt ->0.          (20)

Weak and TV convergence of the actual transmission laws to uniform are
equivalent here by the companion compactness theorem. This closes a
regularity/approximation passage, not the estimate in (20).

The degree and bound of (15) are not a small-entropy approximation on a
GROWING unitary group. They concern one fixed two-channel observable.
Consequently they cannot be inserted into the attachment's growing-level
L2 contraction criterion to infer Haar without an additional argument.

There is also a direct, finite, discrete-TV criterion under this regularity.
Let d_N=TV(law(T_N),Uniform),
e_N=(1/2) sum_k |p_k^window-1/(K+1)|, and
rho_N=TV(M_K law(T_N),law(T_N)). Binomial sampling contracts TV, beta
smoothing contracts TV, and M_K preserves the uniform law. Thus

    e_N<=d_N+epsilon_(N,K),
    d_N<=e_N+epsilon_(N,K)+rho_N.                        (21)

For (12), rho_N->0 by (18) and epsilon_(N,K)->0 explicitly. Hence
|d_N-e_N|->0. In particular the original weak uniform-limit question,
its TV version, (20), and flatness of this finite positive histogram in
discrete TV are all equivalent under the explicit full-G/rank hypotheses.
Equation (21) identifies the remaining defect; it does not estimate e_N.
