# Dimension-uniform random-feedback control and Gaussian blocks

17 October 2026. Working theorem and author self-review outside BGS.
Conditional on the precisely cited project one-step identities below;
not independently audited, formally certified, or a BGS solution.

## 1. Result and significance

Let S_N be deterministic unitary, P_N=|S_N|^2, and assume, with C0>=1
fixed independently of N,

    max P_N<=C0/N, ||P_N-J_N||op<=1/100.                 (1)

Delete a uniform retained port at each step, with a fresh independent
uniform circle phase and the exact unitary Schur rule. Original labels
are retained. The main improvement is uniformity in the STARTING size N.

**Theorem A.** For every A>0 there are constants K,C_A,m_A depending
only on C0,A such that for ALL integers N>=m>=m_A, with probability at
least 1-C_A m^(-A), simultaneously for every N>=v>=m,

    delta_v=max P_v<=K log(2v)/v,
    ||P_v-J_v||op<=1/10,
    max row/column sum_j P_v,ij^2<=L/v,
    max_(i,j)(P_v^2)ij<=T/v.                            (2)

Here L=C0+7, C=1+(L-1)/10, and T=C0+12C+5 are fixed constants.
There is NO restriction m>=log(N)^c. Constants and sufficient m_A are
not optimized. No quantitative startup N for the original frozen model
is supplied by its merely eventual initial assumptions.

**Theorem B.** Under (1), for ANY sequence

    u_N->infinity, u_N/N->0,                            (3)

the vector of sqrt(u_N) times any fixed number of uniformly sampled
entries with disjoint distinct endpoints converges to independent
standard circular complex Gaussians, with every fixed mixed moment.
The empirical intensity measure converges weakly in probability to
Exp(1), and its every fixed moment converges in L2 to k!.

If in addition B_N,ij=S_N,ij conjugate(S_N,ji) satisfies
||B_N||op<=rho_*<1 with fixed rho_*, the ENTIRE fixed uniformly sampled
principal block has that independent Gaussian limit, including diagonals
and reversed entries. With independent uniform retained row phases,
all fixed trace powers have the Gaussian/CUE fixed-power joint moments.

The previous 16 October proof imposed u>=log(2N)^(4+kappa).
Theorems A--B remove that cutoff. The two-channel entrance law and the
Heisenberg-power hierarchy are still not consequences of these results.

## 2. Exact inputs and their scope

Use ONLY these already stated one-step facts, valid before an old-state
joint stop with delta<=1/16 and ||P-J||<=1/10:

* Green compression and ordered inverse expansion, TRACE-077 G1--G5:
  M=(I-P+J)^(-1)-I. Embedded mean-zero linear increments L_v have
  ||L_v||op<=18 delta_v, are supported in the current retained coordinates,
  and the nonlinear remainder has norm <=432 delta_v^2.
  Their chronological sums Z and R telescope with nested projections.
  The initial compression obeys
  ||Q_v M_N Q_v||<=min(1/99,B v/N),
  B=C0+(C0-1)/(1-rho_N).
* Row energy R_i=sum_j P_ij^2 and H_i=sum_j P_ij(P^2)ij satisfy
  H_i<=1/v+(R_i-1/v)/10. With a uniformly chosen port, freeze the scalar
  increment at deletion of i. TRACE-080 F6,F9,F10 give

      E DeltaR_i<=-R_i/(3v)+5/v^2+delta^2/v,
      E(DeltaR_i)^2<=3500 delta^2(R_i+H_i)/v,
      |DeltaR_i|<=8delta sqrt(R_i)+34delta^2.             (4)

  Transpose gives the column version.
* For K_ij=(P^2)ij, freeze its scalar increment on deletion of either
  endpoint. TRACE-079 S1,S2 and the sharpened bound in TRACE-080 section 7
  give, INCLUDING i=j,

      E DeltaK_ij<=[-K_ij/2+5(P^3)ij+2delta P_ij]/v,
      E(DeltaK_ij)^2<=2600 delta^2[K_ij+(P^3)ij]/v,
      |DeltaK_ij|<=12delta sqrt(K_ij)+18delta^2.          (5)

* At an active old state, the gap and row/column energies imply
  max(P^3)ij<=C/v by the singular-value bound of TRACE-080 F2/section 7.

These are local coefficient identities/inequalities, not probability
claims about future success. The analysis below replaces their earlier
fixed-N union bounds; it does not assume the earlier global cutoff theorem.

## 3. A rank-sensitive matrix martingale estimate

Here is a self-contained high-moment lemma; no dimension factor is needed.
If Hermitian martingale differences Y_t have deterministic bounds
||Y_t||_p<=b_t, with even p>=4, then

    E||sum_t Y_t||_p^p <=p^p (sum_t b_t^2)^(p/2).         (6)

Proof. Expand Tr(X+Y)^p into noncommuting words. The terms with one Y
sum to p Tr(X^(p-1)Y), whose conditional mean is zero. Trace Holder
bounds the terms with j>=2 Y factors by
binom(p,j)||X||_p^(p-j)||Y||_p^j. Taking expectations and Holder yields
a recursion for a_t=(E||sum_(s<=t)Y_s||_p^p)^(1/p).
Inductively set a_(t-1)<=p sqrt(V), V=sum_(s<t)b_s^2, and r=b_t/sqrt(V).
For 2<=j<=p, r^j<=r^2+r^p. Also

    sum_(j=2)^p binom(p,j)p^(-j)<e-2<1,
    (1+r^2)^(p/2)-1>=r^2+r^p.

Thus the recursion is bounded by p^p(V+b_t^2)^(p/2). The V=0 case
is immediate, and induction proves (6).

For arbitrary matrix increments use Hermitian dilation. If an increment
is supported in at most v coordinates and has operator norm <=a_v,
its dilation has Schatten p norm <=(2v)^(1/p)a_v. The nonnegative
submartingale ||dilation(Z_t)||_p^p and the elementary maximal inequality
then give

    P(max_t ||Z_t||op>eta)
      <=p^p eta^(-p) [sum_v (2v)^(2/p)a_v^2]^(p/2).     (7)

One may justify the maximal inequality directly by stopping at the first
crossing and applying conditional Jensen through the remaining steps.
All sums here are finite; all stopped jumps are bounded.

Set ell_v=log(2v), D_v=K ell_v. For s>1 write

    b_s(m)=m^(1-s)[ell_m^2/(s-1)+2ell_m/(s-1)^2
                             +2/(s-1)^3].              (8)

For m>=4, sum_(v>m) ell_v^2/v^s<=b_s(m) for the s used below
(3/2<=s<=2), by monotonicity and an exact elementary integral.
For the stopped Green martingale, a_v=18K ell_v/v, so (7) gives

    P(max ||Z||op>eta)
      <=2(18pK/eta)^p b_(2-2/p)(m)^(p/2).               (9)

For fixed eta this is O_(p,K,eta)(ell_m^p m^(-p/2+1)).
Choosing p large proves any prescribed inverse power of m, UNIFORMLY
in N>=m. The total nonlinear remainder is bounded by

    beta_m=432K^2 b_2(m)->0.                            (10)

The support of EACH increment, rather than the ambient starting dimension,
is the essential improvement in (9).

## 4. Protecting marks removes the fixed-N union bound

Choose d distinct ordered marks uniformly among the initial N labels;
at each step delete a uniform UNMARKED port. For every specified deletion
prefix ending at size v>=d, the sum over compatible mark tuples is

    (v)_d /[(N)_d (N-d)_(N-v)] =1/(N)_(N-v).            (11)

Thus after forgetting the marks the ENTIRE prefix law is exactly the
original unmarked law. Conditional on that prefix the marks are uniform
distinct surviving labels. Fresh phase densities are identical. This
does not require any symmetry or exchangeability of the initial matrix.

In the marked filtration the next port is uniform among v-d labels.
For a row use d=1, its endpoint protected. For a pair use d=2 if the
endpoints differ and d=1 otherwise. The frozen endpoint increments in
(4)--(5) are zero. Hence each conditional first and second moment is
multiplied EXACTLY by v/(v-d) relative to its full-port frozen average.
No estimate is conditioned on eventual survival or a future good event.

At any fixed depth u the probability of an unmarked first crossing with
some bad row is at most u times the marked-row crossing probability;
some bad pair costs at most u^2 times the marked-pair probability.
It costs neither N nor N^2. A sum over u>=m then replaces the old fixed-N
union over original labels and all N depths. Retain the full crossing
state; scalar bookkeeping after it is allowed but is not an actual entry.

## 5. One joint stop and concentration at each depth

Stop at the first full new state violating any of

    delta_v<=D_v/v, ||M_v||op<=1/11,
    all row/column energies<=L/v, all K_ij<=T/v.         (12)

Include simultaneous crossings and the complete crossing transition.
Initially these bounds hold. For all v>=m with m sufficiently large,
delta_v<=1/16 at every active old state. The ordered Green expansion
exists even at a first crossing, as in TRACE-080 section 5; its new inverse
has norm <=12/5<3. Take eta_G=1/40. Equations (9)--(10), the initial
bound 1/99, and eventually

    1/99+eta_G+beta_m<1/11

exclude the Green exit except on (9)'s event.

Put h_m=K^2 ell_m^2/m. This bounds sup_(v>=m)D_v^2/v for m>=4.
For a protected row, Y_v=vR_i has, by (4) and the EXACT v/(v-1) factor,

    E DeltaY<=-4Y_v/(3v)+5/v+delta_v^2
              <=-Y_v/v+(5+h_m)/v.                     (13)

Its conditional variance is bounded by

    V_R ell_v^2/v^2,
    V_R=3500K^2[(1+1/10)L+1],

and its centered increment by

    c_R(v)=16K ell_v sqrt(L)/sqrt(v)+68K^2 ell_v^2/v.   (14)

These follow after multiplication of (4)'s second moment by (v-1)^2;
the normalization v/(v-1) cancels rather than adding a large error.
Continue the scalar after the joint stop by its deterministic recurrence
with coefficient 1-1/v and forcing (5+h_m)/v. The deterministic products
give at terminal u a mean majorant <=max(C0,5+h_m), weights <=1, total
variance <=V_R b_2(u), and centered jump bound c_R(u). Here ell_v/sqrt(v)
and ell_v^2/v decrease for v>=4. For h_m<=1 this majorant plus 1 is <L.
The scalar Bernstein bound therefore gives row/column exception

    E_R(m)=sum_(u>=m) 2u
       exp{-1/[2(V_R b_2(u)+c_R(u)/3)]}.                (15)

For a protected pair d<=2, set alpha_v=(v-1)/(v-d), 1<=alpha_v<=2.
Equations (5) give, with Y_v=vK_ij,

    E DeltaY<=-K_ij+alpha_v[-K_ij/2+5C/v+2delta_v^2]
       <=-(4/3)Y_v/v+(10C+4h_m)/v.                    (16)

The variance and centered jumps are bounded by

    V_K ell_v^2/v^2, V_K=5200K^2(T+C),
    c_K(v)=24K ell_v sqrt(T)/sqrt(v)+36K^2 ell_v^2/v.   (17)

For the variance use (v-1)^2/[v(v-d)]<=2. Deterministic products with
coefficient 1-4/(3v) give mean majorant
max(C0,3(10C+4h_m)/4), which plus 1 is <T for h_m<=1.
Thus the pair exception is

    E_K(m)=sum_(u>=m) u^2
       exp{-1/[2(V_K b_2(u)+c_K(u)/3)]}.                (18)

The tails (15),(18) are smaller than EVERY fixed inverse power of m:
their summands are at most a polynomial times exp[-c sqrt(u)/log(2u)].
This statement is for fixed C0,K, with constants allowed to depend on
the requested power. Diagonal pairs have already been included.

For a protected entry S_ij, its increment is q S_ie S_ej, a complex
martingale increment. In the sum normalized by sqrt(u), the total
conditional complex variance before the joint stop is at most 4T for
u>=4, since

    u sum_(v>u) T/[v(v-d)(1-delta_v)]<=4T, d<=2.        (19)

Every normalized jump has modulus <=c_A(u)=2K ell_u/sqrt(u), and the
initial term has modulus <=sqrt(C0). Freeze increments after the first
joint stop, retaining its full jump. The four signed real/imaginary
Bernstein bounds imply, with t_u=sqrt(K ell_u)-sqrt(C0)>0,

    P(|sqrt(u)S_ij|>sqrt(K ell_u), through crossing)
      <=4 exp{-t_u^2/[4(4T+c_A(u)t_u/(3sqrt(2)))]}.     (20)

After the marked-prefix argument the entry exception E_A(m) is the sum
of (20) times u^2 over u>=m. For any desired A, choose
K>=128T(A+10), also K>=4C0. For all sufficiently large m,
t_u^2>=K ell_u/4 and c_A(u)t_u/(3sqrt(2))<=4T. Therefore

    E_A(m)<=sum_(u>=m)4u^2(2u)^(-K/(128T))
             =O_(C0,A)(m^(-A-7)).                     (21)

Apply the first-crossing union bound to (9),(15),(18),(21). Choose an
even p>2A+4 in (9) and enlarge m_A to absorb all logarithms and deterministic
margins. No exit of (12) is possible outside these events. This proves
Theorem A. The proof remains unconditional in the marked or unmarked
filtration: only the predictable OLD stop mask occurs in increments.

## 6. A shrinking deep gap with no log N restriction

Use eta_m=m^(-1/8) in (9). Its bound is
O_(p,K)(ell_m^p m^(-3p/8+1)); p may again be taken large for any
requested power. Combine with Theorem A. At all m<=v<=v0 with v0=o(N),

    ||M_v||op<=B v0/N+m^(-1/8)+beta_m,
    ||P_v-J_v||op<=2[B v0/N+m^(-1/8)+beta_m]->0.        (22)

The probability exception is O_A(m^(-A)), uniformly in N, provided
m->infinity. The factor 2 follows from R=M(I+M)^(-1) once the bracket
is <1/2. This replaces the 16 October shrinking-gap estimate.

## 7. Gaussian blocks: closing all changed estimates

Set m=u and v0=floor(sqrt(uN)) under (3). For fixed protected marks,
the covariance projector identities and averaged estimates in the
16 October proof are unchanged:

    C_(ij),(kl)=sum_e S_ie S_ej conjugate(S_ke S_el),
    C^2=C, rank C=v, C_(ij),(ij)=(P^2)ij,
    E_marks |(P^2)ij-1/v|<=rho sqrt(L-1)/sqrt(v(v-1)),
    E_marks |C_(ij),(kl)|<=sqrt(v/(v)_4)                  (23)

for distinct pairs/four distinct endpoints respectively. The protected
increment covariance differs from C/v by O_r(D_v^2/v^3).
Now the cumulative correction is

    u sum_(v>u) D_v^2/v^3=O_K(log(2u)^2/u)->0,          (24)

and the largest normalized jump is O_r(log(2u)/sqrt(u))->0.
The total active conditional variance stays bounded. On (22)'s exception,
the sum of missing target or active covariance bounds is O_r(1), so its
expected contribution is O_A(u^(-A)); no future-good conditioning appears.
With epsilon_N=O(v0/N+u^(-1/8)+log(2u)^2/u), the covariance error is

    O_r(epsilon_N+u^(-1/2)+log(2u)^2/u+u^(-A))->0.

The initial term has second moment <=u/(v0-1)->0 for distinct entries.
The Taylor martingale comparison from the 16 October proof consequently
establishes weak convergence for all sequences (3).

For the disjoint-entry vector this also gives a useful quantitative form.
For every fixed r and bounded C3 test f on C^r, the expectation difference
from the standard Gaussian vector is at most

    C_(C0,r) ||f||_(C3) [(u/N)^(1/4)+u^(-1/8)]          (25)

for sufficiently large u and u/N sufficiently small; the C3 norm includes
the function bound. Choose fixed A>=2 in the trajectory estimate and the
shrinking-gap bound. The terms before simplification are the initial
L2 error O(sqrt(u/v0)), the covariance error displayed above, the cubic
Taylor error O(log(2u)/sqrt(u)), and the Gaussian total-variance error
O(u/v0+1/u). With v0=floor(sqrt(uN)) each is bounded by the right side
of (25), with constants depending only on the stated parameters.

For each prescribed moment degree s choose Theorem A's A>s/2+2.
The actual entry at TERMINAL dimension u is bounded by sqrt(u), so its
bad-event contribution is at most u^(s/2)C_Au^(-A)->0, regardless of N.
The stopped entry has bounded moments of every fixed degree by (19)--(20)
and c_A(u)<=1 eventually. This supplies uniform integrability and every
fixed mixed moment. The empirical-law argument using two sampled entries
and O(1/u) endpoint coincidences is unchanged. This proves Theorem B's
disjoint-entry and empirical statements.

For the principal-block extension, use the same uncentered reversal Green
compression and expansion as the 16 October proof. For any fixed rho_*<1
put R0=rho_*/(1-rho_*), H=R0+2. The linear increment norm is
<=8H^2delta_v and the remainder <=128H^3delta_v^2, each supported in
v retained coordinates. Apply (7)--(9) with 18 replaced by 8H^2 and
(10) with 432 replaced by 128H^3. Initial entry compression is O(v/N).
Its Green exit is excluded and its deep norm shrinks as in (22), with
O_A(u^(-A)) failure. All constants may depend on rho_*.

The covariance separation into four-label, three-label, reversed and
diagonal cases in the 16 October proof now applies verbatim, using the
just-proved uniform fixed moments. Diagonal covariance is obtained AFTER
off-diagonal Gaussian moments, avoiding circularity. The initial diagonal
term at v0 has second moment O(u/v0) by those uniform moments. This proves
the entire fixed principal block assertion. The independent-row-phase
trace corollary then follows by exact vertex balance and matching cycles
at each FIXED total degree; no estimate at degree proportional to u is used.

## 8. Self-review obligations and remaining frontier

The essential new checks are the noncommutative trace-word estimate (6),
current-rank accounting in (7), the prefix identity (11), exact v/(v-d)
normalization for frozen endpoint moments, the summable depth-dependent
tails, and the terminal u rather than starting N in the moment transfer.
All first-crossing states must remain complete. Dropping the crossing or
conditioning on future flatness would invalidate this proof.

Theorem A allows N->infinity first while a sufficiently large m is fixed,
with error C_A m^(-A). It does NOT allow m=2: for Haar as well, the
reversal inverse becomes singular at two channels and no large-m
concentration bound identifies a fixed-dimensional law. The source-
weighted spectral averaging and bounded Abel transform in the companion
note formulate that remaining entrance-law problem without delay-moment
divergences. Neither those eigenvector statistics, the microscopic
all-order trace hierarchy, nor frozen-phase removal is proved here.

Theorems A--B are a substantive widening of the auxiliary theorem's regime,
not a full solution or evidence of priority. A fresh independent review
would still be needed before promoting these notes to repository claims.
