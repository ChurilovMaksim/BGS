# Flat equal-edge sector: Gaussian comparison through all sublinear times

**Claim ID:** `BGS-TRACE-093`. 16 October 2026.

**Subsequent continuation:** [TRACE-094](wick_collision_poisson_20261016.md) proves
the full flat collision law and exact Heisenberg ratio left open at this
checkpoint. The earlier open-law wording below describes this proof alone.

**Status:** complete project derivation; coordinator reconstruction and fresh
internal audit scope are recorded in the dated review. This supersedes
the safe exponent 3/4 as a sufficient range. No external priority, unchanged
physical-profile extension, signed-unitary comparison or BGS solution is claimed.

## Definitions and the classical exact Gaussian benchmark

For each rooted cyclic word x of length m on N labels retain its directed
edge table nu_ab=#{i:(x_i,x_(i+1))=(a,b)}, with x_(m+1)=x_1.
Let c(nu) be the number of rooted words with that table and put

    d(nu)=prod_ab nu_ab!,
    B_(N,m)=N^(-m) sum_nu c(nu)^2,
    G_(N,m)=N^(-m) sum_nu c(nu)^2 d(nu).

If every entry of a unitary U has squared modulus 1/N, words with identical
edge tables have identical complex amplitudes, so B_(N,m) is exactly their
positive contribution to |Tr U^m|^2. Other table pairs retain their phases.
No independent entry or row phases are introduced in this definition.

Let X be iid complex Ginibre with E|X_ab|^2=1/N and put Y=sqrt(N)X.
Gaussian entry moments give exactly G=E|Tr X^m|^2. The classical formula is

    G = (m!/N^m)[binom(N+m,m+1)-binom(N,m+1)]
      = [prod_(j=0)^m(N+j)-prod_(j=0)^m(N-j)]/[(m+1)N^m].   (0)

The second binomial and falling product are zero if m>=N. All dimensions
and positive m are covered. In particular G=1 for m=1, and G=2 for m=2.
The exact formula and its sinh double-scaling limit are PRIOR results:
Kristjansen--Plefka--Semenoff--Staudacher (2002), equations (2.4), (2.8).
The later Akemann--Vernizzi equation (6.2) has a missing normalization factor;
see the [source audit](../literature/abel_gaussian_sources_20261016.md).

For a self-contained specialization of the classical kernel calculation,
the unscaled Ginibre eigenvalue kernel is

    K_N(z,w)=pi^(-1)exp[-(|z|^2+|w|^2)/2]
                         sum_(j=0)^(N-1)(z conjugate(w))^j/j!.

The determinantal covariance identity and angular monomial orthogonality give

    N^m G = integral |z|^(2m)K_N(z,z)d²z
             - double_integral z^m conjugate(w)^m |K_N(z,w)|²d²z d²w
          = sum_(j=max(0,N-m))^(N-1)(j+m)!/j!.

Hockey-stick summation yields (0), including m>=N. The kernel and its
normalization are checked in Byun--Forrester, Propositions 2.1--2.2.
The Wick measure below is the EXACT finite probability measure

    W(nu)=c(nu)^2 d(nu)/(N^m G),
    B/G=E_W[1/d(nu)],
    C_edge(nu)=sum_ab binom(nu_ab,2).

The proof concerns this positive measure, not the eigenvalue process of
any fixed unitary.


## Theorem

With B and G as defined above, for N>=3 and 3<=m<=N,

    0 <= 1-B/G <= m(m-1)/[N(N+1)] + 15m/N^2.               (1)

For m=1 the deficit is zero; for m=2 it is exactly 1/(2N).
Consequently B/G -> 1 along every m=m_N=o(N).
In particular, when m~c N^(3/4), B/G still tends to one: there is no
nonzero relative critical correction at that proposed scale.
The bound does not establish convergence for m~alpha N, nor evaluate a
signed physical unitary trace statistic.

There is, however, a further Heisenberg-scale conclusion: for every fixed
alpha>0 and every m/N->alpha,

    liminf B/G >= 2^(-2alpha^2),
    lim (log B)/N = (1+alpha)log(1+alpha)-alpha.             (1a)

The first statement is a bound, not the limiting ratio. The second is an
exact exponential rate for the flat positive sector; the Gaussian rate
being transferred is classical. It makes no signed-unitary assertion.

## 1. Gaussian Fock norms and the collision identity

Use unscaled independent standard complex Gaussians Y_ab, and let
p_m(Y)=Tr Y^m, h_m=E|p_m|^2=N^m G. For a holomorphic polynomial
f=sum_nu f_nu Y^nu,

    ||f||^2 = sum_nu |f_nu|^2 prod_ab nu_ab!,
    (partial_ab)^*=multiplication by Y_ab.

Let H_ab,cd=partial_ab partial_cd p_m. The total Hessian energy is

    E sum_abcd |H_ab,cd|^2 = m(m-1) h_m.                  (2)

Indeed every monomial of total degree m contributes the falling factorial
m(m-1). The weighted repeated-directed-edge expectation is exactly

    E_W C_edge = [E sum_ab |H_ab,ab|^2]/(2h_m),            (3)

where W assigns edge table nu weight c(nu)^2 prod nu! / (N^m G).
The coefficient calculation is nu_e^2(nu_e-1)^2(nu_e-2)!
=nu_e! nu_e(nu_e-1). Since 1-1/prod nu!<=C_edge/2,

    0<=1-B/G <= [E sum_ab |H_ab,ab|^2]/(4h_m).            (4)

No Gaussian approximation is being made here.

## 2. Elementary invariant-polynomial facts

For partitions lambda of degree k, the classical Ginibre eigenvalue PDF
and the alternant formula for Schur functions give

    E[s_lambda(Y) conjugate(s_mu(Y))]
      = delta_(lambda,mu) prod_(i=1)^N (N-i+lambda_i)!/(N-i)!.

This is obtained by multiplying the two Schur alternants by the squared
Vandermonde in the eigenvalue PDF and integrating monomials:
integral z^a conjugate(z)^b exp(-|z|^2)d^2z=pi a! delta_ab.
Thus it needs no asymptotic random-matrix theorem.

For the hook lambda_j=(k-j,1^j), 0<=j<min(k,N), write

    w_(k,j)=(N+k-j-1)!/(N-j-1)!.

The two finite identities needed below are

    p_k = sum_(j=0)^(k-1) (-1)^j s_(k-j,1^j),
    C_k := sum_(a=1)^(k-1) p_a p_(k-a)
         = sum_(j=0)^(k-1) (-1)^j(k-1-2j) s_(k-j,1^j).    (5)

Here hooks with length>N vanish. In particular,

    h_k=sum_j w_(k,j),
    ||C_k|| <= (k-1) sqrt(h_k),
    <p_k,C_k> <= (k-1)h_k.                               (6)

Set C_1=0. To verify (5) without importing a cut-and-join theorem, let
H(t)=sum h_j t^j and E(t)=sum e_j t^j be the complete and elementary
symmetric-function series. The hook Jacobi-Trudi identity gives

    F(t,u)=sum_(k>=1) sum_(j=0)^(k-1) s_(k-j,1^j)t^k u^j
          =[H(t)E(ut)-1]/(1+u).

Because H(t)E(-t)=1, the u=-1 value is P(t)=sum_(k>=1)p_k t^k.
Differentiating the displayed quotient at u=-1 gives

    [(t partial_t-1)-2u partial_u]F(t,u)|_(u=-1)=P(t)^2.

These are precisely both identities (5), coefficient by coefficient.

For k>=2, comparing corresponding positive hook weights gives

    h_k >= (N+1)h_(k-1),                                 (7)

because w_(k,j)/w_(k-1,j)=N+k-j-1>=N+1 for every hook
appearing at degree k-1. Thus for m>=3,
h_(m-1)/h_m<=1/(N+1) and h_(m-2)/h_m<=1/(N+1)^2.
The second estimate uses m-2>=1, which explains why m=2 is handled
separately. One must not put h_0=1: p_0=N.

## 3. Exact contraction bounds for the Hessian

Let k=m-2. The derivative formula is

    H_ab,cd = m sum_(r+s=k) (Y^r)_bc (Y^s)_da.            (8)

There are four natural contractions (all finite polynomials):

    T_cd=sum_a H_aa,cd = m(m-1)(Y^k)_dc,
    S_bc=sum_a H_ab,ca = m sum_(r+s=k)(Y^r)_bc p_s,
    A=sum_ac H_aa,cc = m(m-1)p_k,
    B=sum_ab H_ab,ba = m[2N p_k+C_k].                     (9)

The letter B in this paragraph is a Hessian scalar contraction, not the
original equal-edge sector; in the bounds below it is written B_H.
Equation (9) is used only for m>=3, k>=1.

The gradient degree identity gives E||Y^k||_F^2=h_(k+1)/(k+1),
so, using (6)-(7),

    E||T||_F^2/h_m <= m^2(m-1)/(N+1),
    E|A|^2/h_m <= m^2(m-1)^2/(N+1)^2,
    E|B_H|^2/h_m <= m^2(2N+m)^2/(N+1)^2.                 (10)

The crucial bound for S avoids summing separate matrix-power estimates.
Let D_ij=partial/partial Y_ji. Fock adjointness gives exactly

    E||S||_F^2 = <p_m,Tr(Y^2 D^2)p_m>.

Acting with the differential operator on p_m using (8) gives

    Tr(Y^2D^2)p_m
      = m sum_(r+s=m-2) p_(r+2) p_s
      = m[Np_m+C_m-p_1p_(m-1)].                          (11)

The last inner product with p_1p_(m-1) is nonnegative: all trace
polynomials have nonnegative real monomial coefficients and Gaussian
monomial inner products are diagonal and positive. Therefore (6) proves

    E||S||_F^2 <= m(N+m-1)h_m.                            (12)

This exact contraction estimate is the gain over the earlier factorial
domination proof. It retains the one-circuit trace structure.

## 4. Off-diagonal repeated edges: two sphere moments

The law of Y and p_m are invariant under unitary conjugation. For a!=b,
H_ab,ab can therefore be replaced in expectation by H(uv*,uv*) for a
uniform orthonormal pair u,v. Conditional on u, v is uniform on the
(N-1)-dimensional complex unit sphere in u-perp.

For any symmetric quadratic tensor Q on a d-dimensional complex space,

    E_v |sum_ij Q_ij v_i v_j|^2 = 2||Q||_F^2/[d(d+1)].

Orthogonal projection can only decrease its norm. Apply this first to v
in u-perp, then to u in C^N. Without requiring H to be symmetric in its
two upper indices, projection onto that symmetric subspace also decreases
the norm. Consequently, for every fixed Hessian tensor H,

    E_(u,v) |H(uv*,uv*)|^2
       <= 4||H||_F^2/[N^2(N^2-1)].                       (13)

Sum over the N(N-1) off-diagonal matrix units and use (2):

    E sum_(a!=b)|H_ab,ab|^2/h_m
       <= 4m(m-1)/[N(N+1)].                             (14)

The sphere formula follows directly from a normalized complex Gaussian
vector, whose fourth moments and independent squared radius are explicit.
There is no representation-theoretic irreducibility premise in (13).

## 5. Diagonal repeated loops: the 24 contractions

For a diagonal matrix unit use H(uu*,uu*) with u uniform in C^N. The
eighth moment of u, or equivalently the fourth moment in u and conjugate(u),
is the sum over S_4 of the corresponding index pairings divided by
(N)_4=N(N+1)(N+2)(N+3). The same normalized-Gaussian argument proves it.

Pairings use the positive index list (a,c,f,h) and negative list (b,d,e,g)
in H_ab,cd conjugate(H_ef,gh). Classify them by the number of links
between H and its conjugate:

* Four cross links: four terms, each bounded by ||H||_F^2.
* Two cross links: sixteen terms. The internal contractions are two
  copies each of T and S on each side; their sum is bounded by
  4(||T||_F+||S||_F)^2 <=8(||T||_F^2+||S||_F^2).
* No cross links: four terms, bounded in sum by
  (|A|+|B_H|)^2 <=2(|A|^2+|B_H|^2).

This classification uses only H_ab,cd=H_cd,ab. It can be checked by listing
all 24 permutations; complex transposes do not affect the norm bounds.
After summing over N diagonal units, conjugation invariance gives

    E sum_a |H_aa,aa|^2
      <= [4E||H||_F^2+8E(||T||_F^2+||S||_F^2)
                      +2E(|A|^2+|B_H|^2)]
           /[(N+1)(N+2)(N+3)].                           (15)

For 3<=m<=N, divide by h_m and use (2), (10), (12). The four
contributions in the numerator are bounded respectively by

    4m^2, 8m^3/(N+1), 8m(N+m),
    2m^2[(m-1)^2+(2N+m)^2]/(N+1)^2.

Their sum is at most 48mN, hence certainly at most 60mN. Since the
denominator in (15) is at least N^3,

    E sum_a |H_aa,aa|^2/h_m <= 60m/N^2.                  (16)

Combining (4), (14), (16) proves (1). The deliberately rounded constant
15 is not claimed optimal.

## 6. A bounded comparison and exact exponential rate at m~alpha N

The restriction m<=N was needed only to simplify constants in (16).
For all N>=2,m>=3, the preceding proof gives the explicit bound

    E_W C_edge <= L_(N,m),
    L_(N,m)= 2m(m-1)/[N(N+1)]
       + {4m(m-1)+8m^2(m-1)/(N+1)+8m(N+m-1)
             +2m^2[(m-1)^2+(2N+m)^2]/(N+1)^2}
          /[2(N+1)(N+2)(N+3)].                           (17)

Every factorial satisfies log(n!)<=binom(n,2)log 2. Since the exact
Gaussian table measure gives B/G=E_W[1/d(nu)], Jensen yields

    1 >= B/G >= exp[-E_W log d] >= 2^(-L_(N,m)).           (18)

For m/N->alpha finite and positive, L_(N,m)=2alpha^2+o(1). Thus
log(B/G)=O_alpha(1), uniformly when m/N stays in a fixed compact
subset of (0,infinity). The exact Gaussian product formula implies

    lim_(N->infinity) (log G)/N
       = (1+alpha)log(1+alpha)-alpha.                     (19)

When alpha<1 the falling-product/rising-product ratio tends to zero
exponentially; when m>=N it is exactly zero. At alpha=1, if m<N,
the bound Q_m<=exp[-m(m+1)/N] still makes it exponentially small.
Stirling's formula or a Riemann sum of log(1+j/N) proves (19).
Equations (18)-(19) prove (1a), including alpha>=1.

For alpha=1 the resulting flat equal-edge rate is 2log 2-1, about
0.386294. The earlier flat Jensen lower bound (3/e-1)log 2 is much
smaller. This improvement concerns the exactly flat class, whose
Gaussian conjugation structure is essential to the proof; it does
not strengthen the physical non-flat theorem automatically.

## 7. Exact Heisenberg collision mean and negligible triple edges

For every fixed alpha>0 and m/N->alpha, under the exact Gaussian edge-table
measure W proportional to c(nu)^2 prod nu!,

    E_W C_edge -> 2alpha^2,                                (M1)
    Pr_W(max_ab nu_ab>=3) ->0.                             (M2)

Thus a Poisson model of mean alpha^2 with convergence of its first
moment is incompatible with (M1). Without separate uniform integrability,
first-moment convergence alone does not rule out a weak limit with a
smaller mean: rare large collision counts could carry a moment defect.
These results do not establish a Poisson law of mean 2alpha^2 or the corresponding conjectural ratio
B/G->exp(-alpha^2). Control of higher collision moments is still needed.

### 1. The exact partial-swap contraction

Let R exchange the two upper tensor indices of the Gaussian Hessian:
(RH)_ab,cd=H_cb,ad. This is an isometric involution. Fock adjointness
and the displayed derivative formula give

    K:=E sum_abcd H_ab,cd conjugate(H_cb,ad)
      = <p_m, sum_abcd Y_cb Y_ad partial_ab partial_cd p_m>
      = m <p_m,C_m>.                                      (M3)

The cut-join identity proved in the prior note gives the exact hook-weight
representation

    K = m sum_j (m-1-2j)w_(m,j)
      = m[m-1-2jbar]h_m,
    jbar = [sum_j j w_(m,j)]/h_m.                         (M4)

Consequently H_+=(H+RH)/2 satisfies

    E||H_+||_F^2 = m(m-1-jbar)h_m.                        (M5)

The successive weight ratio is

    w_(m,j+1)/w_(m,j)=(N-j-1)/(N+m-j-1)
                    <=q:=(N-1)/(N+m-1)<1.

For each ell, summing w_(j+ell)<=q^ell w_j gives
Pr_hook(j>=ell)<=q^ell. Hence

    0<=jbar<=q/(1-q)=(N-1)/m.                            (M6)

This remains valid at m=N and for m>N, including all positive weights
and their truncation at j=min(m,N)-1. When m/N->alpha>0, jbar is bounded.

### 2. Exact orthonormal-pair projection identity

For u uniform on the complex unit sphere, put

    W_bd(u)=sum_ac H_ab,cd u_a u_c,
    V=E_(Y,u)||W(u) conjugate(u)||^2,
    D=E sum_a |H_aa,aa|^2.

Pair symmetry H_ab,cd=H_cd,ab makes W(u) symmetric. Conditional on u,
v is uniform on the sphere in u-perp. Its exact quadratic moment gives

    E_v|H(uv*,uv*)|^2
      = 2/[N(N-1)] {||W||^2
                -2||W conjugate(u)||^2+|u*W conjugate(u)|^2}.

Taking u expectation and summing the N(N-1) off-diagonal coordinate
directions gives the exact equality

    E sum_(a!=b)|H_ab,ab|^2
       = 4E||H_+||_F^2/[N(N+1)] -4V +2D/N.              (M7)

The first term uses the sphere fourth moment, while the last uses
conjugation invariance: E|H(uu*,uu*)|^2=D/N.

The sphere sixth moment defining V has six pairings. In the product
H_ab,cd conjugate(H_eb,gh), its positive u indices are (a,c,h) and
negative indices (d,e,g). Two pairings have no internal contraction
and are bounded by 2||H||^2 in sum. The other four contract to T or S;
their sum is bounded by (||T||+||S||)^2<=2(||T||^2+||S||^2).
Thus

    0<=V <= [2E||H||^2+2E(||T||^2+||S||^2)]
                  /[N(N+1)(N+2)].                        (M8)

For m/N->alpha, the bounds established earlier give

    V/h_m=O_alpha(1/N),   D/h_m=O_alpha(1/N).

Insert (M5)-(M6) into (M7), and add the diagonal contribution D. The exact
Hessian collision identity then gives

    E_W C_edge
      = 2m(m-1-jbar)/[N(N+1)] -2V/h_m
                     +(1/2+1/N)D/h_m
      ->2alpha^2.                                        (M9)

This proves (M1), including the coefficient 2.

### 3. Triple edges are negligible

Let J be the third derivative tensor of p_m. Gaussian degree counting
gives E||J||^2=(m)_3 h_m. Replacing the fourth sphere moment in the
off-diagonal bound by the sixth sphere moment gives

    E sum_(a!=b)|partial_ab^3 p_m|^2
      <=36 E||J||^2/[N(N+1)^2(N+2)].

Indeed the two unit-vector moment factors are 3!/(N-1)_3 and
3!/(N)_3, and there are N(N-1) off-diagonal directions. The coefficient
norm identity for the third derivative therefore yields

    E_W sum_(a!=b) binom(nu_ab,3)
      <= 6(m)_3/[N(N+1)^2(N+2)] = O_alpha(1/N).            (M10)

For diagonal loops, Pr(any nu_aa>=3) is at most one third of the
diagonal contribution to E C_edge, namely D/(6h_m)=O_alpha(1/N).
Markov's inequality and (M10) prove (M2).

### 4. Exact remaining question

On the event in which all edge counts are at most two,

    prod nu_ab!=2^(C_edge),

and hence B/G differs from E_W[2^(-C_edge)] by o(M1), by (M2).
To identify the conjectural limiting ratio it remains to prove the full
collision distribution. First-moment convergence and absence of triple
edges do not establish its Poisson law or higher uniform integrability.
Endpoint-sharing collections of distinct repeated edges, including
oppositely directed pairs, must be controlled in any factorial-moment
argument; they cannot be discarded from their iid-word probability alone.

The exact C++ sampler in [the C++ sampler](../computations/verification/research_20261016/sample_conditioned_ewens.cpp) suggests the
Poisson mean 2alpha^2 and ratio exp(-alpha^2), but its outputs are only
finite exploratory observations and provide no proof of that claim.

## 8. A closed finite formula and an exponentially accurate mean

There is a useful further simplification of the first-moment argument. For
r>=1 use the same hook weights and set

    h_r=sum_j w_(r,j),  c_r=sum_j(r-1-2j)w_(r,j),
    u_m=w_(m,0)-w_(m,m-1) if m<=N, and w_(m,0) otherwise.

The sums stop at j=min(r,N)-1. For N>=2,m>=3 define

    E=m(m-1)h_m,  K=m c_m,
    J=m^2(m-1)h_(m-1)+m(Nh_m+c_m-u_m)
                         +2m^2(Nh_(m-1)+c_(m-1)),
    Z=4m^2 sum_j (N+m-2-j)^2 w_(m-2,j).

Then the EXACT finite collision mean is

\[
 \mathbb E_W C_{\rm edge}
 =\frac{2(N^2+4N+2)(E+K)-4J+(N+2)Z}
        {2h_mN(N+1)(N+2)(N+3)}.                          \tag{F1}
\]

Here J=E||T+S^transpose||^2 and Z=E|A+B_H|^2. To verify these
identifications, Fock adjointness gives

    <T,S^transpose>=m^2[N h_(m-1)+c_(m-1)].

Indeed T=m times the coordinate gradient of p_(m-1); moving that derivative
onto S multiplies by Y, and summing produces m[Np_(m-1)+C_(m-1)].
Also <p_m,p_1 p_(m-1)>=u_m: multiplying the hook expansion of p_(m-1)
by p_1 adds one box. The two hook predecessors cancel at each interior
hook, leaving the row with coefficient 1 and the column with coefficient
(-1)^(m-2). Non-hook terms are orthogonal to p_m. The one-box identity
follows directly by multiplying a Schur alternant by the sum of variables.
The displayed Z follows by applying the C_(m-2) hook identity to A+B_H.

For clarity, the exact generic sphere pairing sums, before norm bounds, are

    fourth-tensor sum = 2||H||^2+2<H,RH>
                         +4||T+S^transpose||^2+|A+B_H|^2,
    third-tensor sum  = ||H||^2+<H,RH>+||T+S^transpose||^2.

They are identities for every pair-symmetric complex H; taking expectations
and dividing by the appropriate rising sphere denominators gives

    D=(2E+2K+4J+Z)/[(N+1)(N+2)(N+3)],
    V=(E+K+J)/[N(N+1)(N+2)].

Insert these in (M9) to obtain (F1). This also provides a direct audit of
the finite constants without asymptotic tensor estimates.

There is an especially simple rational answer when m>=N+2:

\[
 \boxed{\displaystyle
 \mathbb E_W C_{\rm edge}=F(N,m):=
 \frac{2m\{(N+5)m(m+1)-(N+2)(N+3)\}}
      {(N+1)(N+2)(N+3)(m+2)}.}                            \tag{F2}
\]

To see this, for any r the untruncated weights j=0,...,N-1 have sum
R_r=prod_(i=0)^r(N+i)/(r+1). Their normalized law is beta-binomial
with n=N-1, parameters 1,r+1; equivalently its masses are proportional
to binom(N+r-j-1,r). Elementary stars-and-bars sums give

    E_full j=(N-1)/(r+2),
    E_full[j(j-1)]=2(N-1)(N-2)/[(r+2)(r+3)].

When m>=N+2 all three hook sums at r=m,m-1,m-2 are untruncated and
u_m=w_(m,0). Substitute these two moments, R_(m-1)/R_m=
(m+1)/[m(N+m)] and R_(m-2)/R_m=(m+1)/[(m-1)(N+m)(N+m-1)]
in (F1). Ordinary rational simplification yields (F2); the executed
symbolic simplification is preserved with the finite controls.

More generally, fix 0<a<b<infinity. Uniformly for aN<=m<=bN,

\[
 \mathbb E_W C_{\rm edge}=F(N,m)+O_{a,b}(e^{-c_aN})          \tag{F3}
\]

for some c_a>0 and all sufficiently large N. This assertion does not use
(F2) outside its exact range. Rather, it compares the truncated hook sums
in (F1) with their full stars-and-bars sums. The successive weight ratio
is at most N/(N+r). For r=m,m-1,m-2 and large N it is at most
(1+a/2)^(-1), and the omitted tail j>=r has relative mass at most
exp[-(a/2)N log(1+a/2)]. Its first two moments cost only polynomial
factors of N. The omitted column in u_m is bounded by the same geometric
tail. The finitely many rational coefficients and norm ratios in (F1)
have at most polynomial growth in this compact m/N range. Absorbing those
factors into a smaller exponent proves (F3).

Writing alpha_N=m/N in a fixed positive compact interval, expansion of
the explicit rational F gives the rigorous quantitative consequence

\[
 \mathbb E_W C_{\rm edge}
   =2\alpha_N^2-\frac{2(\alpha_N^2+\alpha_N+1)}N
          +O_{a,b}(N^{-2}).                               \tag{F4}
\]

None of (F1)--(F4) establishes a collision distribution. They give exact
or controlled first moments only.

## 9. What must cancel in an exactly flat unitary

For any flat unitary, write the exact ordered path-pair decomposition

\[
 |\operatorname{Tr}U^m|^2=B_{N,m}+R_{N,m},\qquad
 0\le1+R_{N,m}/B_{N,m}\le N^2/B_{N,m}.                    \tag{C1}
\]

Thus at m/N->alpha>0, the ratio R/B tends to -1 with exponential error
exp[-N((1+alpha)log(1+alpha)-alpha)+o(N)]. This evaluates the necessary
compensation relative to the positive sector, while the final signed
answer is controlled only to O(N^2), not its required CUE scale O(N).

The sublinear comparison also moves this necessary cancellation to much
earlier times. For any fixed c>0 and m=floor(sqrt(c N log N)), the exact
Gaussian product and sum log(1+j/N)=m(m-1)/(2N)+O(m^3/N^2) give

\[
 B_{N,m}\sim G_{N,m}\sim
        \frac{N^{(c+1)/2}}{\sqrt{c\log N}}.                \tag{C2}
\]

The falling/rising ratio is at most exp[-m(m+1)/N]=N^{-c+o(1)}.
The logarithmic remainder tends to zero, and m=o(N), so no unjustified
truncation of the large Gaussian product is used. In particular, for c>3,

\[
 0\le1+R_{N,m}/B_{N,m}
       \le(1+o(1))\sqrt{c\log N}\,N^{(3-c)/2}\to0.         \tag{C3}
\]

This is an exact-class unitary consequence without phase randomization.
The actual frozen intensity profile is non-flat; extending these sharp
flat comparisons to it still requires a separate proof.

## Consequences and boundaries

The N^(3/4) threshold in the factorial-domination proof is not a genuine
critical scale for this relative comparison: the sharper result proves
that its relative deficit vanishes there as well. The Gaussian finite
product is therefore an asymptotic evaluation of B throughout m=o(N),
including scales approaching Heisenberg times by an arbitrary vanishing
factor. The exact product must be retained when truncating its logarithm
would leave a nonvanishing error.

No statement here bounds the signed difference between |Tr U^m|^2 and its
positive equal-edge part for a specified unitary U. The physical intensity
profile is not exactly flat, so this theorem is not automatically a
theorem for that profile. Neither determinant cancellation nor Gaussian
comparison identifies the CUE value of the required physical signed sum.

At m of order N, (18) bounds the ratio away from zero and transfers the
exponential rate, but does not identify the asymptotic ratio. Determining
that ratio, or proving that m=o(N) is sharp, remains open in this
continuation. World-priority checking has not
been completed; Gaussian Fock identities, Schur orthogonality, hook
identities and sphere moments are established mathematics.

## Review and reproduction

The [coordinator proof audit and independent tensor-check scope](../archive/record/reviews/gaussian_hessian_20261016.md)
separate the written proof from finite fixtures. The initial factorial route,
including the exact Ewens/one-circuit sampling identity, is preserved as a
[superseded range checkpoint](../archive/record/reviews/equal_edge_factorial_20261016.md).
[Executed checks](../evidence/executions/20261016/abel-gaussian/README.md) pin the
word, polynomial, generic tensor and sampling programs. The [source audit](../literature/abel_gaussian_sources_20261016.md)
credits the prior Gaussian benchmark and records the normalization trap.
