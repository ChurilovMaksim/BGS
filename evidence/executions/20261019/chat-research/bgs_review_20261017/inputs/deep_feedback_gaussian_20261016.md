# Gaussian entries in deep random Schur feedback

16 October 2026. Working proof outside the repository; author self-review,
not an independent audit, a formalization, a priority claim or a BGS proof.

## Exact claim

Let deterministic S_N be unitary, P_N=|S_N|^2, J_N=11*/N, and suppose

    max_ij (P_N)ij <= C0/N,   ||P_N-J_N||op <= 1/100,

with fixed C0>=1. At each size v choose a uniformly random retained label e,
independently choose w uniform on the unit circle, and set, for i,j!=e,

    S_(v-1),ij = S_v,ij + q S_v,ie S_v,ej,
    q=w/(1-S_v,ee w).

All labels keep their original meaning. Fix kappa>0 and integers u=u_N with

    ceil(log(2N)^(4+kappa)) <= u,    u/N -> 0.

For fixed r, sample 2r DISTINCT ordered labels uniformly from the retained
set at depth u, and pair them as (I_a,J_a), a=1,...,r. Then

    (sqrt(u) S_u,I_a J_a)_(a=1,...,r) => (G_a)_(a=1,...,r),       (1)

where G_a are independent circular complex Gaussians with E|G_a|^2=1.
Every fixed mixed polynomial moment also converges. Consequently the
empirical measures of sqrt(u)S_u,ij converge weakly in probability to this
Gaussian law, and the empirical intensity moments satisfy

    u^(-2) sum_ij (u |S_u,ij|^2)^k -> k! in L^2                (2)

for every fixed nonnegative integer k. The intensity measure converges
weakly in probability to the mean-one exponential law.

This is an annealed auxiliary-feedback result, with a deterministic start.
It does not cover fixed u, a specified diagonal or reversed pair, or the
spectral statistics of the fixed initial operator. Its analytic input is
the named internal trajectory theorem TRACE-080 and its Green compression
identity TRACE-077. The complete proofs of those inputs are not replaced
by the finite checks below.

## 1. Strengthening the trajectory probability

Write ell=log(2N), m=ceil(ell^(4+kappa)), g=1/10 and use TRACE-080 constants

    L=C0+7, C=1+g(L-1), T=C0+4C+3.

For any prescribed A>0 take K=64T(A+5), D=K ell. The same joint stopping
rule and first-crossing argument as TRACE-080 apply with this larger D.
Up to that stop all embedded Green martingale increments obey

    E(L_v | past, chosen port)=0, ||L_v||op<=18D/v,
    ||B_m||op<=432D^2/m,

and the full pathwise identity is

    M_v=Q_v M_N Q_v + Q_v Z_v Q_v + Q_v B_v Q_v,
    Z_v=sum_(t>v) L_t,
    ||Q_v M_N Q_v||op<=min(1/99,Bv/N),
    B=C0+(C0-1)/(1-rho_N), rho_N=||P_N-J_N||op.

Here Q_v is the zero-sum projection on the retained labels, embedded in
the original N-dimensional space. Projections onto FUTURE retained sets
are not put inside the martingale increments. The predictable variance
of the Hermitian dilation of Z is at most 324D^2/m, and each dilated jump
has norm at most 18D/m. Rectangular matrix Freedman therefore gives

    Pr(max_(v>=m)||Z_v||op>=eta)
    <= 2N exp[-eta^2/{2(324D^2/m+6D eta/m)}].                 (3)

External input: Tropp, Freedman's inequality for matrix martingales,
Electronic Communications in Probability 16 (2011), Theorem 1.2 and
Corollary 1.3, printed p.264. Exact primary PDF checked:
https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf
The matrices here need not be Hermitian or normal; dilation has dimension
2N and its variance consists of the two products L_v L_v* and L_v* L_v.
Norm bounds suffice for both products. A maximal, stopped inequality is
being used, not independence of increments.

Replace ONLY the coarse Schatten-Markov exceptional term F12 of TRACE-080
by (3) with eta=1/40. Its other exceptions F13--F15 remain unchanged.
F13 and F14 are exp[-c ell^(1+kappa/2)] times polynomial prefactors.
For F15 the exponent equals

    (15K/(64T)+o(1)) ell = (15(A+5)+o(1)) ell,

and its prefactor is 4N^3. Thus with probability 1-O_A(N^(-A)), at EVERY
size N>=v>=m,

    delta_v=max P_v<=D/v, ||P_v-J_v||op<=g,
    max row/column sum P_v,ij^2<=L/v, max(P_v^2)ij<=T/v.    (4)

The constant D depends on A only through its fixed multiplier K; the
cutoff m is unchanged. All deterministic margins in TRACE-080 continue
to hold eventually, since D^2/m->0 and D/m->0.

In addition take eta_N=ell^(-1/2-kappa/4) in (3). Its exponent has order
ell^(1+kappa/2). For any v0=o(N), on an event with arbitrarily small
polynomial failure probability,

    max_(m<=v<=v0) ||P_v-J_v||op <= epsilon_N -> 0,
    epsilon_N=2[Bv0/N+eta_N+432D^2/m],                     (5)

for sufficiently large N. This follows from R=M(I+M)^(-1), R=P-J;
the bracket tends to zero. No conditioning on future success is used in
the martingale or in the argument excluding the first crossing.

## 2. Protecting finitely many labels

For L0 fixed, initially sample L0 distinct ordered marks uniformly among
the N labels. At every step delete a uniform UNMARKED port, then reveal
a fresh uniform phase. Stop at the predetermined terminal size u>=L0.

This marked construction has exactly the law of the original process
conditioned on all marks surviving. Its UNMARKED trajectory has exactly
the original law. Indeed a specified deletion prefix from N down to v
has (v)_(L0) compatible ordered mark tuples, each with weight

    1/[(N)_(L0) (N-L0)_(N-v)].

Their sum is 1/(N)_(N-v), the original deletion-prefix probability.
The independent phase-density factors are identical. Conditional on the
unmarked history at size v, the marks are uniform distinct labels from
the retained set. At size u this agrees with sampling the terminal marks
after the original trajectory. These identities hold for every prefix,
not just for the last survivor set.

In the larger filtration the marks are known, next port is uniform among
v-L0 ports, and the next phase remains fresh. Hence every surviving
marked entry is a complex martingale. The unmarked joint stop of section
1 and its probability estimates remain valid under this marked law.

## 3. The covariance projector

At size v define a_e in C^(v^2) by

    a_e(i,j)=S_ie S_ej.

Unitarity, separately in the row and column indices, gives

    <a_f,a_e>=(sum_i conjugate(S_if)S_ie)
               (sum_j conjugate(S_fj)S_ej)=delta_fe.

Thus the matrix

    C_(ij),(kl)=sum_e S_ie S_ej conjugate(S_ke S_el)         (6)

is an orthogonal projector of rank v. In particular

    ||C||F^2=v,    C_(ij),(ij)=(P^2)ij.                    (7)

These statements hold for arbitrary unitary S without a gap hypothesis.

For marked entry increments dX_a=q S_Ia,e S_e,Ja,

    E(dX_a dX_b | marked past)=0,
    E(dX_a conjugate(dX_b) | marked past)
      =1/(v-L0) sum_(e unmarked)
          S_Ia,e S_e,Ja conjugate(S_Ib,e S_e,Jb)/(1-P_ee). (8)

The zero pseudo-covariance uses E_w q^2=0, not a reality assumption.
On an active old state satisfying (4), replacing (8) by C_(IaJa),(IbJb)/v
has error at most c_(L0,T) D^2/v^3. To check this explicitly:
the normalization change costs L0 T/[v^2(v-L0)]; replacing the denominator
costs delta T/[(1-delta)v(v-L0)]; reinstating the L0 excluded ports costs
L0 delta^2/(v-L0). Use Cauchy and (P^2)ij<=T/v also for cross terms.

Only AVERAGED covariance estimates are needed. Write R=P-J. From (4),

    ||P^2-J||F=||R^2||F<=||R||op ||R||F
                              <=rho sqrt(L-1).

For a uniform distinct pair i,j,

    E_marks |(P^2)ij-1/v|
       <=rho sqrt(L-1)/sqrt(v(v-1)).                       (9)

For four distinct marked labels i,j,k,l, (7) gives

    E_marks |C_(ij),(kl)|<=sqrt(v/(v)_4)=O(v^(-3/2)).       (10)

Uniform pointwise estimates o(1/v) for P^2-J are NOT assumed. The disjoint
endpoints in (1) are essential for the use of (10). Neither a reversed
pair nor two diagonal entries can be inserted into that estimate.

## 4. Martingale Gaussian comparison

Take v0=floor(sqrt(uN)). Then v0/N->0, u/v0->0, and v0>=u eventually.
Use 2r protected labels. Freeze every entry martingale after the FIRST
joint stop of section 1, including its full crossing increment. For the
last v0-u steps use normalized increments sqrt(u)dX_a. The actual
process and this stopped process agree off an O_A(N^(-A)) event.

For the actual process, uniformity of the marks given the unmarked
history and unitarity give

    E |sqrt(u) S_v0,IaJa|^2 <= u/(v0-1) -> 0.             (11)

We need no worst-entry bound for the initial term of this last window.
If the stop precedes v0, the last-window stopped increment sum is zero;
all comparisons of covariance below include that exceptional event.

At step v use deterministic target complex covariance (u/v^2)I_r and
zero pseudo-covariance. Summing expected absolute covariance errors,
(5), (8)--(10), and the common stopping event imply

    sum_(v=u+1)^v0 E ||cov_v-(u/v^2)I_r||
      <= c_r [epsilon_N+u^(-1/2)+D^2/u+O_A(N^(-A))] -> 0. (12)

For completeness the bad-event term is legitimate without conditioning:
each active covariance is bounded by c_r T u/v^2, and the missing
post-stop target covariances by c_r u/v^2. Their TOTAL over all steps is
bounded by a constant. On the successful shrinking-gap event (9) sums
to O(epsilon_N), and on its complement to a constant times its
probability. Uniform marks at each prefix are used before integration.

The maximal normalized vector increment is at most
2sqrt(r)D/sqrt(u)->0; its summed conditional second moment is bounded by
c_r T. Consequently its summed third absolute moments are O_r(D/sqrt(u)).

Here is a direct CLT argument rather than an unqualified citation.
Identify C^r with R^(2r). A complex covariance (u/v^2)I_r with zero
pseudo-covariance is the real covariance (u/(2v^2))I_(2r). For a test
function with three bounded derivatives, compare the martingale sum
to independent centered Gaussian increments of those deterministic real
covariances, replacing increments backwards. Convolve the test with
the not-yet-used Gaussian suffix. The Taylor terms of degree zero and
one cancel; the quadratic error is bounded by (12) times the second
derivative bound. The cubic errors are bounded by the summed third
moments above plus the Gaussian sum O_r(u^(-1/2)). Convolution does not
increase the derivative bounds. Hence the test expectations converge.
The target total complex covariance is

    u sum_(v=u+1)^v0 v^(-2) I_r -> I_r.

Tightness follows from the second moment bound. Smooth bounded test
functions identify the weak limit. Adding the negligible actual initial
term (11), and removing the vanishing stop exception, proves (1).

## 5. Uniform integrability and empirical law

For ANY fixed pattern of marked endpoints (including coincident endpoints),
stop by the same unmarked joint rule and run the entry martingale from N
to u. Its initial term is at most sqrt(C0 u/N). Its total complex
conditional variance is at most 2T eventually, and each normalized jump
is at most 2D/sqrt(u)->0. Applying scalar Freedman to the real and
imaginary parts, in both signs, bounds its tail by

    4 exp[-x^2/{4(2T+c_N x/(3sqrt(2)))}], c_N=2D/sqrt(u).

For large N, c_N<=1; this tail bounds all fixed moments uniformly.
The actual entry is bounded by sqrt(u)<=sqrt(N). For a prescribed
moment degree p choose A>p. Then the contribution on the trajectory
exception is at most N^(p/2)O_A(N^(-A))->0. The stopped contribution on
that exception tends to zero by Cauchy and its uniform higher moments.
Thus the actual entries have uniform moments of every prescribed order;
joint fixed polynomial moment convergence follows from (1) and these
higher-moment bounds.

For an empirical bounded continuous test function, the first moment
follows from the one-entry result. In its second moment, two uniform
ordered entries have four distinct endpoints except with probability
O(1/u); on that dominant event (1) makes them asymptotically independent.
This proves convergence in probability of the empirical complex measure.
For (2), higher moment bounds handle all endpoint coincidences by Cauchy
and their O(1/u) frequency, and permit the same second-moment argument.
The k-th Gaussian intensity moment is k!, giving (2).

## 6. Scope, obligations and next obstruction

Dependency graph:
TRACE-077/080 exact stopped identities and coefficient bounds
-> matrix Freedman probability improvement -> shrinking deep gap
-> protected-label law + covariance projector -> martingale CLT
-> all fixed entry moments -> empirical intensity law.

Self-review obligations: correct marks filtration; full crossing retained;
matrix dilation variance and constants; distinct-endpoint restrictions;
averaged rather than pointwise diagonal estimate; polynomially rare
failure before transferring moments. Exact finite controls are in
feedback_covariance_check.py and its separately hashed execution packet.
They check identities and combinatorics, not the asymptotic input theorem.

The first unresolved implication toward a microscopic spectral law is a
fixed-dimensional entrance law for the entire scattering matrix together
with its radial derivative/clock, or an equivalent signed determinant
comparison at Heisenberg scale. A Gaussian law for finitely many sampled
entries at u->infinity does not supply either implication. Passing from
the fresh-phase ensemble to the frozen physical U_N is a further gap.

No repository files were modified for this research pass.

## 7. Extension: an entire fixed principal block

Additional hypothesis ONLY for this extension:

    B_N,ij=S_N,ij conjugate(S_N,ji), ||B_N||op<=rho_*<1,   (13)

where rho_* is fixed independently of N. First prove the case
rho_*<=1/100 with the same constants as section 1; the general fixed-gap
case is included at the end of section 7.1.

Let I_1,...,I_d be uniformly sampled DISTINCT surviving labels, d fixed.
Then the ENTIRE matrix

    (sqrt(u) S_u,I_a I_b)_(1<=a,b<=d)                       (14)

converges jointly, in law and every fixed mixed polynomial moment, to d^2
independent standard circular complex Gaussians. In particular diagonals
and both directions of each pair are included. This still does not identify
the spectrum of S_u at dimension u, the u=O(1) entrance law or the frozen
physical spectrum.

### 7.1 Shrinking reversal channel in Green coordinates

B=B(S) is Hermitian and a contraction. TRACE-073 section 7 gives exactly

    E_w B(S')=B^c=B_AA+B_Ae B_eA/(1-B_ee),
    Xi_B=B(S')-B^c, E_w Xi_B=0, ||Xi_B||op<=8delta.

Set G_B=(I-B)^(-1), M_B=G_B-I. Block inversion gives the simpler,
UNCENTERED compression identity

    M_(B^c)=(M_B)_AA.                                     (15)

The stochastic Perron projection used for P must not be inserted here.
When rho_*<=1/100, ||M_B,N||<=1/99. Also |B_N,ij|<=C0/N and

    sum_j |B_N,ij|^2=sum_j P_N,ij P_N,ji<=C0/N,

with the same column estimate. Expanding M_B,N=sum_(h>=1)B_N^h gives

    max_ij |M_B,N,ij|<=B0/N,
    B0=C0[1+1/(1-||B_N||op)].                             (16)

Until the entry bound or ||M_B||<=1/11 first fails, apply the ordered
inverse expansion to G_B after (15). Its mean-zero linear increment has
norm<=18delta and its remainder norm<=432delta^2, with the same sharper
12/11 old inverse bound as in section 1. Embedded principal projections
are nested, so the exact telescoping identity uses ordinary coordinate
projections in place of Q. Matrix Freedman (3), the same complete first
crossing, and the already unconditional entry event give

    max_(m<=v<=v0)||B(S_v)||op
       <=2[B0 v0/N+eta_N+432D^2/m] -> 0                   (17)

with arbitrarily small polynomial failure probability, whenever v0=o(N).
This is a consequence of the exact reversal-feedback identities, not a
new independence assumption. The proof uses fresh phases and does not
assert that reversal suppression holds for arbitrary deterministic powers.

For general fixed rho_*<1 set R0=rho_*/(1-rho_*) and H=R0+2. Stop at
the first entry crossing or ||M_B||>R0+1. Then ||G_B^c||<=H. Eventually
8H D/m<=1/2, so the full first-crossing inverse exists with norm<=2H.
The linear increment is bounded by 8H^2 delta and the remainder by
128H^3 delta^2. Matrix Freedman uses variance 64H^4 D^2/m and jump
8H^2 D/m. A fixed deviation 1/4 and the vanishing total remainder
exclude that Green crossing with arbitrarily small polynomial failure;
the initial centered term is now simply its principal compression.
Using (16), then eta_N in the same inequality, gives the general version
of (17):

    max_(m<=v<=v0)||B(S_v)||op
       =O_(C0,rho_*,A)(v0/N+eta_N+D^2/m)->0.

No uniformity as rho_* approaches one is asserted. The rest of the proof
requires only this shrinking estimate, so it proves (14) for (13) as
stated with ANY fixed rho_*<1.

### 7.2 Off-diagonal block first; no diagonal CLT is used here

Consider the covariance (6) of any two DIFFERENT OFF-DIAGONAL entries in
a uniformly sampled finite principal block. Four distinct endpoint labels
are covered by (10). For the four possible three-label patterns, direct
unitary multiplication gives the following squared-Frobenius sums:

    sum_(i,j,l) |C_(ij),(il)|^2 = sum_(i,e) P_ie^2 <= L,
    sum_(i,k,j) |C_(ij),(kj)|^2 = sum_(e,j) P_ej^2 <= L,
    sum_(i,j,l) |C_(ij),(jl)|^2 = ||B||F^2 <= L,
    sum_(i,j,k) |C_(ij),(ki)|^2 = ||B||F^2 <= L.            (18)

For example at fixed i the first matrix is
S^T diag(P_i,.) conjugate(S), a unitary left/right transform of the
displayed diagonal matrix. At fixed j the third is
S diag(B_.,j) conjugate(S). The fourth is obtained by the analogous
left/right transform at fixed i. Summation restrictions to three distinct
labels only decrease these nonnegative sums. Thus each three-label
average absolute covariance is O(v^(-3/2)).

The remaining two-label pattern is a reversed pair, for which EXACTLY

    C_(ij),(ji)=(B^2)ij,
    ||B^2||F<=||B||op ||B||F<=sqrt(L)||B||op.             (19)

Equations (17) and (19) make its averaged absolute covariance o(1/v).
Diagonal variances of these OFF-DIAGONAL entries still use (9); all
pseudo-covariances vanish. The proof in section 4 therefore proves joint
independent Gaussian limits for EVERY finite set of distinct off-diagonal
entries in a random principal block. Section 5 already gives uniform
moments for all label patterns, including diagonal entries without a CLT,
so this off-diagonal convergence includes all fixed mixed moments.

### 7.3 Recovering diagonal covariance, without circularity

At a size v write X_ij=sqrt(v)S_ij. For a uniform label I,

    d_I=v(P^2)_II=(1/v) sum_e |X_Ie|^2 |X_eI|^2.

In its first moment the v-1 noncoincident terms tend to 1 by the
off-diagonal Gaussian result. In its second moment the (v-1)(v-2)
terms with I,e,f distinct tend to 1 by the joint result for the four
directed edges Ie,eI,If,fI. Every other term has frequency O(1/v) and
uniform bounded moments from section 5. Hence

    E(d_I-1)^2 -> 0.                                      (20)

This closes the diagonal VARIANCE. It did not assume Gaussian diagonal
entries. It uses only the already closed off-diagonal result and the
separately proved, nonasymptotic moment bounds.

For two distinct diagonal labels i,k put

    v C_(ii),(kk)=(1/v) sum_e
                   X_ie X_ei conjugate(X_ke X_ek).

Expand its second absolute moment as a double average over e,f. When
i,k,e,f are distinct, all eight directed entries are off diagonal, and
their limiting independent-Gaussian monomial has expectation zero.
The exceptional coincidences occupy O(1/v) of this double average and
are bounded by the uniform eighth or higher moments. Consequently

    E |v C_(II),(KK)|^2 -> 0 for uniform distinct I,K.      (21)

If a diagonal ii and an off-diagonal kl have THREE distinct endpoints,
the projector identity gives

    sum_(i,k,l) |C_(ii),(kl)|^2
       =sum_i C_(ii),(ii)=Tr(P^2)<=L,

so their averaged absolute covariance is O(v^(-3/2)). If they share an
endpoint, the normalized sums instead have the forms

    v C_(ii),(ik)=(1/v)sum_e |X_ie|^2 X_ei conjugate(X_ek),
    v C_(ii),(ki)=(1/v)sum_e |X_ei|^2 X_ie conjugate(X_ke).

Expand their second absolute moments. The generic four-label terms
again have zero independent off-diagonal Gaussian expectation; the
O(1/v) coincidences have bounded moments. Thus these covariances also
are o(1/v) in averaged L^1, without using a diagonal CLT.

All convergences just used are uniform over a late window
u<=v<=floor(sqrt(uN)): if uniformity failed, a sequence of offending
depths would still satisfy v>=m and v/N->0, contradicting the
off-diagonal theorem on that sequence. Uniform moment bounds are
available on the same entire retained range.

### 7.4 Closing the full block

Use d protected labels and the vector of d^2 entries. Section 7.2 treats
all covariances between its off-diagonal components; (20) treats the
diagonal variances; (21) and the subsequent identities treat every
remaining distinct pair. After the O(D^2/v^3) protected-port correction,
the summed expected covariance error of section 4 tends to zero for
this vector as well. Its normalized jumps and total variance obey the
same bounds with constants depending on d. The initial diagonal entries
at v0 require a separate check: section 5 gives
E[v0 |S_v0,II|^2]<=c, so their initial contribution is O(u/v0) in L^2
and tends to zero. A worst-entry bound uD/v0 would NOT suffice for all
u=o(N); this is why the nonasymptotic moment estimate is needed here.
The SAME Taylor martingale
comparison proves (14), and the same uniform moments transfer all fixed
polynomial moments. There is no invocation of a diagonally extended
version of (10), no assumption of pointwise P^2 flatness, and no use of
the desired full-block CLT in its own covariance proof.

## 8. A spectral corollary at fixed, not Heisenberg, powers

Assume (13) and independently put D_u=diag(zeta_1,...,zeta_u), with
independent uniform circle phases on the surviving labels. Let V_u=D_u S_u.
For every fixed M, the vector

    (Tr V_u, Tr V_u^2, ..., Tr V_u^M)

converges jointly to independent circular complex Gaussians with variances
1,2,...,M, including every fixed joint mixed moment. Explicitly, for
finitely supported nonnegative integer sequences p_m,q_m,

    E product_m (Tr V_u^m)^(p_m) conjugate(Tr V_u^m)^(q_m)
      -> 1_(p=q) product_m p_m! m^(p_m).                  (22)

Proof: If sum m p_m != sum m q_m, global phase integration gives exact
zero. Otherwise let this common total be K and expand the traces into
words. Integrating EACH coordinate phase requires the retarded and
advanced words to visit every vertex equally often. The union therefore
has at most K distinct vertices. Every equality pattern using d<K
vertices has O_K(u^d) labelings; its 2K-entry expectation is O_K(u^(-K))
by the uniform moment bounds. The total contribution of such patterns
vanishes.

When d=K, each retarded word vertex occurs exactly once across all its
trace factors. Its directed edges form disjoint oriented cycles, with
length multiplicities p_m, including loops for m=1. The phase constraint
forces the advanced words to use the same vertices exactly once. The
full block theorem and its moment convergence make the leading normalized
entry expectation zero unless the advanced DIRECTED EDGE SET is exactly
the retarded edge set, in which case it tends to one. Those edges have a
unique cycle decomposition. Hence the advanced length multiplicities
must equal p_m, and the possible matchings are exactly
product_m p_m! m^(p_m): match equal-length ordered trace factors, and
choose a cyclic starting point for each. There are (u)_K leading
retarded label assignments; (u)_K/u^K->1. This proves (22).

The bounded higher moments give tightness and uniform integrability.
Moment determinacy here needs no additional theorem: for any real linear
combination of the real/imaginary trace components, a subsequential limit
has the centered-Gaussian moments with some variance sigma^2. The
characteristic-function Taylor remainder of even order 2k is at most
|t|^(2k)(2k-1)!! sigma^(2k)/(2k)!=(t^2 sigma^2/2)^k/k!->0.
Thus every such linear combination is Gaussian with the specified
covariance, identifying the joint weak limit. In particular
E|Tr V_u^m|^2->m for each FIXED m.

The extra D_u is part of the asserted probability space. It cannot be
deleted from this proof: its exact coordinate balance reduces the number
of free labels from potentially 2K to at most K. Nor does this argument
allow K=K(u) without new quantitative bounds uniform in K. At m~u the
number of patterns and the moment-comparison errors are uncontrolled.

## 9. An exact check on the forbidden spectral shortcut

For any deterministic starting unitary, the UNPHASED feedback satisfies

    E Tr S_u=(u/N) Tr S_N.                                (23)

Indeed a protected diagonal entry is a bounded complex martingale: its
fresh-phase increment has mean zero for every chosen deleted port. In a
degenerate |S_ee|=1 case the coupling to that port is zero by unitarity,
so the entry is unchanged. Average the protected initial label uniformly
and then sum over the u final labels. The protected-label identity of
section 2 gives exactly (23), without any trajectory concentration input.

Use the ALREADY EXISTING project construction from
mathematics/symplectic_half_radius_obstruction.md (7 October 2026), not a
new counterexample construction. For odd n, N=n^2, x,y in (Z/nZ)^2 put

    H_xy=n^(-1) exp[2pi i (x_1 y_2-x_2 y_1)/n].

Its previously proved identities are H*=H, H^2=I, P=J,
||B(H)||op=N^(-1/2), and Tr H=sqrt(N). Thus it meets ALL the initial
hypotheses of the full-block theorem for large n, with C0=1. Nevertheless
its unphased feedback obeys

    E Tr S_u=u/sqrt(N),
    E|Tr S_u|^2 >= u^2/N.

For u=N^(3/4)+O(1), those moments diverge, while every fixed normalized
sampled principal block in (14) still converges to independent Gaussians.
Therefore the full-block theorem does NOT imply fixed-power CUE trace
moments of the unphased feedback. This example does not by itself refute
a local spectral limit for that randomized feedback, and it is not the
physical frozen operator. It is a precise moment obstruction to deleting
the extra D_u in section 8 or making a global spectral inference from
entrywise Gaussianity. The initial frozen involution's degenerate spectrum
already supplied a separate, earlier coarse-data obstruction in the cited
project source.

## 10. Why small-channel feedback needs a new law

For EVERY 2-by-2 unitary S there are p in [0,1] and z with |z|=1-p such
that

    B(S)=[[p,z],[conjugate(z),p]].

This follows from the two row and column normalization identities:
|S11|^2=|S22|^2=p and |S12|^2=|S21|^2=1-p. Its eigenvalues are 1 and
2p-1. Hence ||B(S)||op=1 and I-B(S) is singular, even when S is Haar.
The uncentered reversal Green coordinate used in section 7 must therefore
cease to be admissible before the terminal two-channel state. Extending
its small-norm estimate uniformly down to u=2 is false, rather than just
unproved. This is compatible with the Gaussian theorem, whose u diverges.

A concrete next unresolved test is the two-channel transmission law:
under the same deterministic-start hypotheses, is

    |(S_2)12|^2 => Uniform[0,1],
    E |(S_2)12|^(2k) -> 1/(k+1) for all fixed k?          (24)

Equation (24) is NOT proved here. Bi-torus invariance can be imposed by
independent retained row/column phases for spectral probes, but it does
not determine this transmission law. The whole fixed-u scattering law
and its joint radial clock law are still stronger inputs needed for the
positive Schur-energy boundary reduction. Fixed m trace universality in
section 8 and growing-u Gaussian blocks do not supply (24).
