# All fixed clock powers under an explicit entry-flatness premise

**Stable claim:** BGS-TRACE-060, conditional equality-law extension.
**State:** CONDITIONAL. The probability of the premise is unresolved.
**Review:** independent internal reconstruction, 11 October 2026, from main
`b126cfb18f445b82358fc156632873082ac22503`. The original candidate was
incomplete as written. Sections 3.2 and 3.4 repair two leading-order word
errors without weakening its quantified conclusion. The
[review packet](../../archive/evidence/executions/20261011/clock-universality/README.md)
preserves that input and the review scope. This is neither external peer
review nor a Lean formalization, a priority claim or a solution of BGS.

## 1. Process, quantified claim and dependencies

Use the fresh original independent uniform phases and independent uniform
coordinate order of [the first-delay proof](delay_bootstrap.md).
Start with deterministic unitary U_N and F_N(z)=zU_N. At retained size u,
S_u=F_u(1), T_u=F_u(1)*F_u'(1), Q_u=S_uT_uS_u*, and T_N=Q_N=I.
Equivalently the derivative is the angular delay with the factor −i.
The exact feedback congruences imply T_u,Q_u≥I. Set

ell=log(2N), m=ceil(ell^(1+kappa)), kappa>0, m<N,
A_m={max_ij |(S_u)_ij|²≤K ell/u for every u≥m},
H_u=uT_u/N, V_u=uQ_u/N, Gamma_(r,u)=S_u H_u^r.

K and kappa are fixed. For every fixed integer L≥1 there is a deterministic
epsilon_N→0, depending on L,K,kappa, such that

P(A_m intersect {at some u≥m, one of the following exceeds epsilon_N})→0:

max_j |(H_u^r)_jj−f_r(u/N)|,
max_j |(V_u^r)_jj−f_r(u/N)|,
max_(j≠k) [|(H_u^r)_jk|+|(V_u^r)_jk|],
max_(j,k) |(Gamma_(r,u))_jk|,       1≤r≤L.             (1)

All maxima are over the labels alive at the stated size. This is an
intersection estimate, not a probability conditional on the future A_m.
If P(A_m^c)→0 is proved separately, (1) becomes convergence in probability
for the actual process. L is fixed before N tends to infinity.

Write tau=−log x and M(z,tau)=sum_(r≥1) f_r(exp(−tau))z^r. The references
are the unique triangular polynomial solution of

partial_tau f_r=−(r−1)f_r+r[z^r]{−log(1−M²)},
f_r(1)=1.                                              (2)

The right-hand coefficient uses only orders below r. In particular

f1=1, f2=2−x, f3=6−6x+x²,
f4=22−32x+12x²−x³,
f5=90−170x+100x²−20x³+x⁴.

The proof uses the [all-fixed killed moment hierarchy](all_moment_delay_bootstrap.md)
as its upstream input. It does not use an endpoint intensity-gap premise.
The separate [fourth-order proof](fourth_delay_law.md) supplies
explicit low-degree identities and checks, but is not needed as a circular
dependency for the general induction. No actual scattering matrices are
assumed free or Haar distributed.

## 2. Predictable stops, high moments and the base order

Choose a fixed sufficiently large p after L and keep p fixed as N grows.
With zeta=1/4 and b>0 fixed, use the moving cap

M_p(u)=u^(p−1)Tr(T_u^p)/N^p≤B_u=B(u/m)^zeta,
B=ell^b, R_p(u)=1+(uB_u)^(1/p).                         (3)

The killed hierarchy bounds each fixed killed M_p in expectation under
the joint first-diagonal stop. Its moving-cap exit bound is O(C_p/B),
without a log N loss. Additional entry/power stops only reduce the killed
quantities. Frozen entry martingales retain the complete first crossing
state; they are not killed. Input and outgoing norms obey ||H||=||V||≤R_p.

The local first-diagonal bound from the upstream proof is

C[sqrt(ell B^(1/p)m^(−zeta/p) log(2u)/u^((p−1−zeta)/p))
  +sqrt(ell/u)log(2u)+ell/u].                            (4)

For surviving j≠k, the first-power formula is

T'_jk=T_jk+q T_je S_ek+conj(q)conj(S_ej)T_ek
             +T_ee|q|²conj(S_ej)S_ek.                  (5)

Put a=S_ee, d=1−|a|² and q=w/(1−wa). Exact uniform-phase averaging gives
E q^n=0 for every n≥1 and E|q|²=1/d. Coordinate averaging in (5), after
normalization and freezing a deleted label, gives drift −H_jk/u+O(H_jk/u²)
and forcing O((epsilon1(u)+delta_u)/u), where delta_u=K ell/u.
Use column orthogonality and sum_e |S_ej S_ek|≤1; the omitted retained
endpoints cost O(delta_u/u). The output argument uses row orthogonality.
The first-diagonal variance bounds also control these off-diagonal entries.
A stable scalar comparison and a union over the live pairs give the local
off-diagonal version of (4). Entry convergence does not assert convergence
of H to I in Hilbert–Schmidt norm.

For Gamma=ST, the exact identity

Gamma'_jk=Gamma_jk+q(S_je Gamma_ek+S_ek Gamma_je)
                    +q²S_je S_ek Gamma_ee              (6)

is a compressed complex martingale before normalization. Its normalized
frozen drift is −(u−r)g_jk/u², r=|{j,k}|, with no forcing. The q² term
uses (1/u)sum_e |S_je S_ek|²≤delta_u/u, rather than an incorrect
delta_u² bound. The local variance and live-pair block argument are as in
the [explicit cross-clock proof](fourth_delay_law.md#1-the-holomorphic-cross-clock-is-a-compressed-martingale).
This closes r=1. The joint stop includes the first violation of each
envelope used in these estimates, not a future good-event condition.

## 3. Repaired finite-word induction

Fix k≥2 and suppose (1) through k−1 holds with local envelope E_(k−1)(u).
Stop before the k-th input/output diagonal exceeds
C_k=max_(x∈[0,1]) f_k(x)+2. Positivity gives

|(H^k)_ij|²≤(H^k)_ii(H^k)_jj,
|(S H^k)_ij|²≤(V^k)_ii(H^k)_jj.                        (7)

Thus no concentration of unknown k-th off-diagonal entries is presumed.
Since h^r≤1+h^k for h≥0 and 1≤r≤k, all scalar moments of degree at most k
at an eliminated endpoint are bounded by a k-dependent constant at this stop.

### 3.1 Exact open words and top-order transport

Let v=S*e and let K,J be the feedback embeddings of the upstream proof.
The exact normalized formulas are

H'^k=alpha_k K*H(R_w H)^(k−1)K,
Gamma'_k=alpha_k J*S H(R_w H)^(k−1)K,
alpha_k=(1−1/u)^k,
R_w=KK*=I+qev*+conj(q)ve*.                              (8)

Expand the r interior insertions with positive gaps n0,...,nr, sum n_i=k.
The two orientations A=ev* and B=ve* have contractions
e*H^n e=(H^n)_ee, v*H^n v=(V^n)_ee,
v*H^n e=(Gamma_n)_ee. Consecutive identical orientations introduce a
lower-degree mixed scalar. Alternating words involve only the lower
input/output diagonal references. At a=0 phase averaging retains balanced
q and conj(q) counts. For |a|≤sqrt(delta_u)≤1/2, every fixed balanced
phase moment differs from its a=0 value by O(delta_u), every non-pure
unbalanced moment is O(sqrt(delta_u)), and pure q or conj(q) powers have
exactly zero mean. These bounds follow from their convergent geometric series.

The sole unknown k-th diagonal transport in the input formula is the
zero-interior, two-boundary term. Its averaged coefficient is

alpha_k/u *conj(S_ei)S_ej/(1−|S_ee|²) * (H^k)_ee.       (9)

The outgoing formula has the analogous row coefficient. The absolute row
sum over source diagonals is at most (1+O(delta_u))/u, by unitarity and
Cauchy–Schwarz. The mixed two-boundary term has net phase q², so its mean
is exactly zero even for nonzero a. All other averaged terms reduce to
strictly lower powers and lower mixed powers.

After reference subtraction and label freezing, the input/output own
coefficient is 1−k/u+O(1/u²). Its transport gives a full absolute live-row
norm at most 1−(k−1)/(2u) eventually. For the mixed family it is
1−k/u+O(1/u²), with no own-diagonal transport. Complex transport is handled
by absolute row sums; it is not called a nonnegative matrix.

### 3.2 Leading endpoint omission and its compensation

In (10)–(12), the common coordinate-average and normalization factor
alpha_k/u has been taken outside: the expressions are the coefficients
of the main drift polynomial. One cannot regard every omitted retained
endpoint as a small error. For the sum of the two orientations of a
diagonal even alternating word with r=2q interior insertions and no boundary
insertion, the ideal coordinate-averaged coefficient is

(product_(i=1)^(2q−1) f_(n_i))
 [2 f_(n0+n_(2q))−f_(n0)f_(n_(2q))].                  (10)

The negative product is leading: e=j is omitted from the summation.
The alternating two-boundary word A...B with the same gaps contributes
product_(i=0)^(2q) f_(n_i), cancelling that product. This compensation
holds for the main drift polynomial after replacing lower diagonal entries
by f; it is not an exact equality of the individual random words.
The replacement errors are bounded by the lower envelope and flatness.

For X_n=H^n, V^n or Gamma_n, the remaining lower-matrix polynomial is

L_k(X)=
 2 sum_(q≥1,n0+...+n_(2q)=k; n_i≥1)
       (product_(i=1)^(2q−1) f_(n_i)) X_(n0+n_(2q))
 +sum_(q≥1,n0+...+n_(2q−1)=k; n_i≥1)
       [(product_(i=0)^(2q−2) f_(n_i)) X_(n_(2q−1))
        +(product_(i=1)^(2q−1) f_(n_i)) X_(n0)].        (11)

Every matrix index in (11) is at most k−1. In mixed reductions use
Gamma_a H_b=Gamma_(a+b) and V_a Gamma_b=Gamma_(a+b).

Let C_(2q)(k) be the sum of products over positive 2q-part compositions
of k. Merging the first and last gap of (10) leaves a multiplicity s−1.
By symmetry, the total even merged-gap contribution is
2(k−2q)/(2q) C_(2q)(k). The two one-boundary orientations contribute
2 C_(2q)(k). Their sum is k/q C_(2q)(k), including k=2q, where the
even merged-gap sum is empty. Consequently, when X_n=f_n I, (11) is

P_k I, P_k=sum_(q=1)^floor(k/2) (k/q) C_(2q)(k)
             =k[z^k]{−log(1−M²)}.                     (12)

This derives the ideal drift (2) directly for entries. It avoids inferring
an entry polynomial from a trace identity alone, and does not assume a
finite matrix realizing all ideal entries exactly.

### 3.3 Lower drift errors

Lower-moment substitutions, omitted-endpoint remainders and nonzero-a
phase corrections, including frozen-reference increments, have bound

C_k[E_(k−1)(u)+sqrt(delta_u)] R_p(u)^(2k)/u+C_k/u².      (13)

For an endpoint sum use Cauchy–Schwarz over the eliminated coordinate.
A diagonal moment of degree between k and 2k is at most R_p^k times
the stopped k-th diagonal bound; lower moments use (7). This justifies
the coarse R_p^(2k) allowance without assuming higher-order diagonal
concentration. No division by an uncontrolled future quantity is used.

For a live label, reference freezing has exact conditional increment

(1−1/u)[f_k((u−1)/N)−f_k(u/N)]
                     =−x f_k'(x)/u+O(1/u²), x=u/N.    (14)

Pairs have the analogous freeze with r=1 or 2. The f_k are fixed smooth
polynomials. The discrepancy from the ideal continuous equation is therefore
O(1/u²), including deletion; an eliminated label keeps its previous reference.

### 3.4 Variance: the separate two-boundary interior branch

It is false that every word with an interior insertion contains a small
lower-power retained-to-eliminated endpoint. Interior words with both
boundary insertions instead have endpoint products of scattering entries,
of the forms conj(S_ei)S_ej, S_ie conj(S_je), or S_ie S_ej. Unitarity
and flatness imply

(1/u)sum_e |S_ei S_ej|²≤delta_u/u,
(1/u)sum_e |S_ie S_ej|²≤delta_u/u.                     (15)

All their internal scalar contractions are bounded by (7). Their FULL
raw second moments are ≤C_k delta_u/u≤C_(K,k)ell/u² and their jumps are
O_k(delta_u). This argument applies directly at nonzero a using |q|≤2;
it requires no fictitious small lower endpoint and no phase independence.

The zero-interior two-boundary term (9), and its outgoing/mixed analogues,
belong to this same scattering-endpoint branch. By (7), |q|≤2 and (15),
their full raw second moments are at most 16 C_k² delta_u/u and their
jumps at most 4 C_k delta_u. This covers the remaining zero-interior case.

All other interior words have at most one boundary insertion. They do
contain a lower clock off-diagonal or mixed endpoint of size E_(k−1).
Square that factor and average the other endpoint using the higher-diagonal
bound above. Zero-interior, one-boundary terms contain a scattering entry
and use the high-moment cap. Scaling, coordinate selection and the frozen
reference supply the final O(1/u²) term. Finite-word Cauchy–Schwarz handles
cross terms, without assuming independence of phase monomials. Each real
or imaginary centered entry increment therefore satisfies

Var≤C_(k,p)[ell R_p^(2k)/u²+E_(k−1)² R_p^(2k)/u+1/u²],
jump≤C_(k,p)(sqrt(delta_u)+E_(k−1))R_p^k+C_(k,p)/u.     (16)

These are deterministic conditional-on-the-past bounds before the enlarged
stop. The crossing increment is included, also for simultaneous exits.

## 4. One local envelope closes every fixed order

Set D1=8 and Dk=D_(k−1)+4k+4=2k(k+3). Choose fixed p so large that

D_L(1+zeta)/p<1/8,
2D_L(1+kappa+b)/p<kappa/4.                              (17)

Enlarge p for the upstream fixed-moment bookkeeping if needed. Use

E_k(u)=C_(k,p)[sqrt(ell/u) R_p(u)^Dk(log(2u))^(k+3)
                         +ell/u R_p(u)^Dk].            (18)

This dominates (4), decreases geometrically with increasing u up to the
displayed logarithms, and vanishes at m for every k≤L. More specifically,
the lower drift relative to E_k/u has spare factor R_p^(−2k−4);
the lower-envelope noise relative to E_k has spare R_p^(−3k−4).
Since inf_(u≥m)R_p(u)≥(mB)^(1/p)→infinity, these factors uniformly
absorb fixed constants and logarithms. The standalone sqrt(delta_u)
drift and the zero-interior noise are smaller for the same reason.

On a dyadic block [v/2,v], scalar Freedman on (16), for at most O(v²)
pairs alive at the block start and both real components, bounds raw noise by

C_(k,p) R_p(v)^k log(2v)[sqrt(ell/v)+E_(k−1)(v)].       (19)

For any fixed r0 its exception probability is O(v^(−r0−3)), after
enlarging constants. Labels deleted in the block are frozen; there is no
union over all original N² labels at each small block. Propagate these
raw partial noises pathwise using the absolute-row stability of Section 3.1.
No martingale transform with a future-dependent propagator is asserted.
Only blocks above the current u are summed, so geometric decay gives (18)
without an N/m or log N accumulation.

Use the joint stop consisting of flatness, the p-cap, all previous/current
entry envelopes and the top-diagonal caps. A first envelope or diagonal-cap
exit outside the cap and martingale exceptions contradicts the stable
comparison with (13), (14) and (19). Deleted-label rows are identities and retain the previous-size reference.
At a global first exit the surviving labels first receive the new-size
reference f_k((u−1)/N), then their complete crossing value and reference
are frozen together. Thus a phase-dependent exit does not alter (14).
Complete crossing states allow simultaneous exits. In particular

E_L(m)=O(ell^(−kappa/2+D_L(1+kappa+b)/p)
                  (log ell)^(L+3))+o(1)→0.             (20)

The moment-cap exception is O(C_p ell^(−b)); the block exceptions sum to
O(m^(−r0)). On A_m no flatness exit occurs, so the probability of any
remaining first exit tends to zero. This proves (1). Phase averages were
never conditioned on A_m or on future survival.

## 5. Reference transform and weak clock law

Equation (2), as a formal series, is equivalent to

partial_tau M=M+z M_z[−1+2M/(1−M²)], M(z,0)=z/(1−z).

Characteristics yield

z=M(1−M)/[(1+M)(1−xM)],
(1−xz)M²−[1−(1−x)z]M+z=0.                             (21)

The formal root M(0)=0 is unique. The
[full-depth reference proposition](full_depth_clock_measure.md)
derives its probability measure mu_x, including the atom for x>1/2,
the merging endpoint x=1/2 and mu_1=delta_1. Its compact support is
uniformly bounded. At x=0 the density is

sqrt((b−h)(h−a))/(2 pi h²),
a=3−2sqrt(2), b=3+2sqrt(2), h∈[a,b].                   (22)

All fixed moments of the empirical H_u law follow from (1), uniformly in
u≥m. The method of moments then gives weak convergence to mu_(u/N), in
the same intersection-probability sense. To see the uniform assertion,
otherwise select a violating sequence of sizes and a converging subsequence
of u/N. Moment bounds give tightness and uniform integrability of each
fixed power by the next higher even power. Every subsequential limit has
the reference moments at that subsequential x. Compact moment determinacy
forces that limit to mu_x; continuity of the compact reference family
then contradicts the weak-law violation. For a fixed weak tolerance,
only finitely many moment bounds and their exceptional events are needed.

If P(A_m^c)→0 is separately established, this is an actual convergence-in-
probability theorem; at m/N→0 its limit is (22). Uniform integrability of
killed moments follows from the upstream hierarchy. No unrestricted
expectation on rare flatness failures is claimed.

The endpoint moments 1,2,6,22,90,... and the inverse-Jacobi reference
family have prior random-matrix antecedents; see the
[exact source comparison](../../literature/cavity_sources_20261011.md).
This proof identifies a conditional random-Schur clock law. It supplies
neither P(A_m^c)→0, growing-order or edge statistics, a microscopic
eigenphase law, signed TRACE-005, nor global deterministic BGS.
