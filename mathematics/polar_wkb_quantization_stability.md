# Principal WKB polar quantization and smooth spectral transport

**Status:** project analytic proof, with an independent internal audit of
the smooth-symbol and polar comparison. The spectral-transport mechanism is
credited to the earlier project theorem. Supporting proof for `BGS-TRACE-017`;
no new stable claim ID. Fixed coupling and odd dimensions are unchanged.
No BGS conclusion, external priority or analytic formalization is asserted.
The [curated review](../record/polar_wkb_review.md) separates audit scopes;
the [provenance](../evidence/polar_wkb_provenance.json) identifies the source
revision, reviewed artifacts and actual hash comparisons.

## Result and prior ownership

The marked-transport and ergodic spectral-flow mechanisms are already proved
in `supplement/fixed_map/ergodic-transfer/ergodic_spectral_transfer.md`,
sections 1–5 (18 September). They must not be represented as new results.
Below we spell out a bad-label version, verify the logarithmic input for the
actual FM018 operator, and derive a concrete comparison for the principal
four-branch WKB matrix using its explicit finite-shift construction.

Let h=1/N, N odd, and retain exactly U_N=exp(i tau N A_N) M_N,
tau=10^-80, ordinary symbol g and W_N(l,k)=(-1)^(kl)T_N(l,k) from
`mathematics/fixed_map_path_model.md`. Let W0_N be the matrix obtained from
`mathematics/four_branch_parametrix.md`, section 2, retaining just a_{r,0}:

    (W0_N)_{jk}=e(3N/8) sqrt(h)/2
                    sum_{r=0}^3 e(S_r(tau,jh,kh)/h) a_{r,0}(tau,jh,kh).

For all sufficiently large odd N it is invertible. Define its exact unitary
polar factor V_N=W0_N(W0_N* W0_N)^(-1/2). There is a fixed smooth real torus
symbol b, defined explicitly below from the first amplitude transport, such that

    V_N=exp(i h Op_N(b)) U_N + O_op(h²).                      (A)

Consequently, after a harmless common rotation, the spectra of U_N and V_N
admit a periodic labelled matching with bounded unfolded displacements and
mean-square displacement O(1/log N). If either endpoint has all compact
factorial correlation limits, those limits agree at both endpoints. In
particular an all-order compact CUE/Sine law for one is equivalent to the same
law for the other. No such law is proved for either endpoint here.

The construction is for this explicitly defined principal WKB matrix and
these exact branch phases, amplitudes and modular factors. It is not a
statement about an arbitrary quantization of the same classical map.

## 1. Deterministic marked transport, all orders

Let x_j be N labelled points on R/NZ and y_j=x_j+d_j modulo N, with real
lifts d_j satisfying |d_j|<=D and q_N^2=N^-1 sum_j d_j^2 ->0. Multiplicities
are allowed but factorial tuples always have distinct labels. For a compact
continuous phi on R^(k-1), use the periodized anchored factorial statistic
of TRACE001–003 with normalization 1/N. Suppose supp phi lies in [-R,R]^(k-1).
Put L=2(R+2D+1) and

    n_j(L)=#{ell: dist(x_ell,x_j)<=L},
    M_p(L)=N^-1 sum_j n_j(L)^p.

Here n_j includes j. Periodic distances and all periodized test arguments are
used throughout. Once N>2L, each contributing coordinate has a unique small
lift; no periodic image multiplicity enters the following bound.

For epsilon>0 let bad labels B={j:|d_j|>epsilon}, beta=|B|/N. Then
beta<=q_N^2/epsilon^2. For every eta>0, bounded D and 0<epsilon<=1,

    |C_k(y;phi)-C_k(x;phi)|
      <= C_k omega_phi(2epsilon) M_{k-1}(L)
       + C_k ||phi||_infty beta^(eta/(k-1+eta))
                             M_{k-1+eta}(L)^((k-1)/(k-1+eta)).   (B)

The modulus omega uses the sup norm and phi extended by zero, hence is a
global modulus of continuity. To prove (B), divide tuples into those with
all labels good and those having a bad label. If either endpoint term is
nonzero, every original point lies within R+2D of the original anchor.
The all-good relative coordinates move by at most 2epsilon; counting
possible tuples gives at most sum_j n_j(L)^(k-1). For a bad tuple choose any
of its bad labels as the counted label (a union bound over k choices);
all other labels lie within L of that label. Its absolute contribution is
at most 2||phi||_infty. Thus the bad contribution is bounded by a constant
times N^-1 sum_{j in B} n_j(L)^(k-1). Holder gives (B).

Uniform boundedness of M_{k-1+eta} therefore suffices: first N->infinity at
fixed epsilon, then epsilon->0. For C^1 tests the prior supplement gives the
stronger quantitative estimate

    |C_k(y;phi)-C_k(x;phi)| <= C_{k,phi,D} q_N M_{2k-2}(L)^(1/2). (C)

This follows from the mean-value formula, summing each displacement with
that label fixed, and Cauchy–Schwarz. Along straight interpolation a tuple
meeting derivative support still has every original point in the enlarged
box. The same periodic lift works throughout that interpolation.

Reference factorial bounds of all fixed orders imply all these moments.
Indeed n^p <= C_p[1+(n-1)_p] for integers n>=1. The falling factorial counts
ordered distinct non-anchor neighbors; a nonnegative smooth compact test
majorizing [-L,L]^p bounds its average by a reference (p+1)-point statistic.
This also proves local count moment control from all compact correlation
limits rather than assuming it redundantly. Noninteger moments follow by
increasing the exponent to the next integer. If local moments are stated
instead for a uniformly random spatial origin, they also imply these
anchored moments: for every j and z in [x_j-1,x_j+1], its L-neighborhood
lies in the (L+1)-neighborhood of z; summing and integrating gives
M_p(L)<= (2N)^-1 integral_0^N n_z(L+1)^(p+1) dz.

The hypotheses are symmetric between endpoints. Bounded displacement makes
all target neighborhoods subsets of enlarged reference neighborhoods, so
all local moments also transfer. Thus a reference may be either endpoint.
Uniform bounded k-point statistics alone do not suffice: for N=m^2 place
m labels at 0 and the others at mutual distance >1 away from the cluster.
Moving half the cluster to a and half to -a, 0<a<1/4, gives q_N=a/sqrt(m),
yet a pair test supported in (-a,a), equal to 1 at zero, changes from
1-1/m to 1/2-1/m. This is the prior supplement's realizable counterexample.

## 2. Uniform spectral-flow control for the actual operator

Let B_N=Op_N(b)+O_op(h) be Hermitian, with b fixed smooth real, centered by
its mean. Exact quantum trace centering changes it by O(h) (indeed the
smooth alias contribution is superpolynomially small). Write C=sup||B_N||,
U_s=exp(i s B_N/N)U_N, and

    B_T=T^-1 sum_{r=0}^{T-1} U_N^(-r) B_N U_N^r.

The prior finite-dimensional argument gives continuous phase lifts in cycles,
with unfolded endpoint displacements d_j, such that

    max|d_j|<=C/(2pi),
    (N^-1 sum d_j^2)^(1/2)
                  <= (||B_T||_N+C^2(T-1)/N)/(2pi).            (D)

For completeness: analytic Hermitian perturbation theory applied to local
Cayley transforms labels eigenangles along the analytic unitary path. At
almost every s, writing theta_j for radian eigenangles and b_j for the
diagonal entries of B_N in an eigenbasis of U_s, the conventions are
explicitly theta_j'=b_j/N, (theta_j/(2pi))'=b_j/(2pi N), and
x_j'=b_j/(2pi) for unfolded coordinates x_j=N theta_j/(2pi). At degeneracies choose the basis diagonalizing
the compression of B_N. Each diagonal entry equals that of its U_s time
average, so its mean square is bounded by the normalized HS norm squared
of that average. Telescoping U_s^r-U_N^r bounds the difference between the
two averages by C^2(T-1)/N uniformly in s. Integrating velocities and using
Minkowski proves (D). Crossings simply permute the labels. Integer changes
of final lifts are absorbed into the periodization. No spectral simplicity
or uniform eigenvalue gap is used.

Here the requisite time-average bound follows from the actual FM018 inputs,
not an additional QE conjecture. FM018 (O8) gives

    ||Ad(U_N)^r Op_N(a)-Op_N(a composed with G^r)||op
                             <= C N^-2 exp(Gamma r)||a||H5,

and its checked classical input (O11) gives exponential correlation decay
for the fixed mean-zero smooth observable b. The same correlation estimate
for negative r follows by adjunction/invariance, so the inverse convention
in B_T causes no change.

The smooth-symbol trace pairing extends (O9) as follows. Expand both smooth
symbols into integer Weyl modes. The normalized trace equals the classical
Fourier pairing except signed pairs whose indices differ by a nonzero
multiple of N. Every such pair has an index of magnitude >=N/2. Bounding
one Fourier l1 tail and the other l1 norm gives, for every fixed s>0,

    |<Op(a),Op(c)>_N-<a,c>|
                         <= C_s N^-s ||a||H(s+2)||c||H(s+2).

The bound overcounts pairs but is uniform and sufficient. Derivative norms
of b composed with G^r grow at most exponentially at each fixed order.
Consequently, enlarging Gamma if needed,

    |<B_N,Ad(U_N)^r B_N>_N-<b,b composed with G^r>|
                           <= C(N^-2 exp(Gamma |r|)+N^-1).

The O(N^-1) term allows the stated O(h) operator correction to B_N. Expand
the squared HS norm of its time average into the triangular correlation
sum. At T=floor(c log N), with c>0 sufficiently small,

    ||B_T||_N^2 <= C/T+C N^-2 exp(Gamma T)+C/N = O(1/log N).

Thus (D) proves q_N=O((log N)^-1/2), uniformly through the perturbation path.
One never needs to assume QE for every U_s or transfer an eigenbasis at s=0.
A mean symbol produces only the scalar rotation exp(i mean(b)/N), irrelevant
to every anchored correlation. The constants/startup are noneffective,
inheriting actual-map mixing, and may depend on the fixed symbol.

## 3. The actual WKB first correction is a smooth symbol

Let K1_N be the same four-branch matrix as W0_N with a_0 replaced by a_1.
The canonical finite-shift construction proves

    U_N=W0_N+h K1_N+O_op(h^(3/2)).                           (E)

It supplies globally smooth amplitudes with uniform derivatives on the
needed charts, phases solving S_t=g(x,S_x)/(2pi), and scalar transports
(partial_t-D1)a0=0, (partial_t-D1)a1=D2 a0, initial a0=1,a1=0.
The coefficients of D1 are real. Along its real characteristics a0 is an
exponential of a bounded real integral, hence positive and bounded away
from zero on this fixed time interval. Therefore c_r=a1_r/a0_r is smooth.

The required global chart assertion is verified rather than presumed.
For the lifted characteristic flow (X(t,a,y),P(t,a,y)), initially
X=a and P=(y+r-3a)/4, the Hamiltonian divergence is zero. Thus
det d(X,P)/d(a,y)=1/4. Solving X(t,a,y)=x and differentiating at fixed x
gives the exact identity S_r,xy=P_y-P_a X_y/X_a=1/(4X_a)>0. The canonical
no-caustic estimate bounds X_a above and below, uniformly on the whole
fixed time interval. The leading transport also gives a0=X_a^(-1/2).
Alternatively, the specified C^2 phase bound gives S_r,xy>=1/8 directly
at tau. The phase correction and its first derivatives are bounded and
periodic. For fixed x,r, y -> S_r,x(tau,x,y) is thus a smooth strictly
increasing bijection R->R. Define

    c(x,p)=c_r(tau,x,y) where p=S_r,x(tau,x,y).              (F)

This is independent of the choice of r after the exact y/r relabelling.
Indeed S_r(t,x,y+1)=S_{r+1}(t,x,y), and a_{r,j} have the same relabelling.
Moreover the other canonical identities are

    S_{r+4}(t,x,y)-S_r(t,x,y)=x-3y-3r-6,
    S_r(t,x+1,y)-S_{r-3}(t,x,y)=-2r-2y+3.

Their x derivatives shift p by 1 and by 0 respectively. Amplitude transport
uniqueness gives a_{r+4,j}(x,y)=a_{r,j}(x,y) and
a_{r,j}(x+1,y)=a_{r-3,j}(x,y): all transport coefficients agree since g
is periodic in p and the added phases have vanishing second x derivative.
Together these identities imply c(x,p+1)=c(x,p) and c(x+1,p)=c(x,p).
Thus (F) is a fixed smooth complex symbol on the actual ordinary torus.
There is no N-dependent choice of spectral logarithm here.

We next prove the only needed symbol-composition estimate directly. For any
fixed smooth torus symbol c=sum c_{kl} e(kx+lp), its exact Weyl action is

    Op_N(c)u(x)=sum c_{kl} e(k(x+hl/2))u(x+hl).

Apply it to the entire lattice-periodic four-branch sum W0, using its global
phase/amplitude extensions when x+hl leaves the fundamental chart. On a
single branch, after factoring e(S_r(x,y)/h), its leading amplitude is

    sum c_{kl}e(kx+l S_r,x) a0_r = c(x,S_r,x)a0_r=a1_r.

Taylor's integral remainder and |e(i alpha)-1|<=|alpha| give a remainder
bounded by C h (|l|+l^2+|kl|) for each Fourier coefficient, uniformly in
x,y,r. This uses globally bounded a0 and its first derivative, and bounded
S_xx; these follow from the phase/amplitude gluing and compact charts.
All the Fourier moments converge because c is smooth. Including sqrt(h),

    Op_N(c)W0_N=K1_N+O_entry(h^(3/2))
                      =K1_N+O_op(h^(1/2)).                 (G)

The last estimate is simply ||R||op<=N max|R_jk|. Integer Fourier labels,
ordinary midpoint factors and the full branch sum have been retained, so
there is no omitted sampling alias or unjustified continuous FIO replacement.

## 4. Polar reduction and the exact error scale

A crude entrywise bound gives ||K1_N||op=O(h^-1/2). Equation (E) first
implies ||W0_N||op=O(1). Equations (E),(G) then give, with C_N=Op_N(c),

    U_N=(I+h C_N)W0_N+O_op(h^(3/2)),
    W0_N=(I-h C_N)U_N+O_op(h^(3/2)).                        (H)

Here ||C_N||<=sum|c_{kl}|=O(1), so inversion of I+h C_N is valid.
Thus W0_N is invertible for all sufficiently large N. Write
Z_N=W0_N U_N*=I-h C_N+O(h^(3/2)). Right unitary equivariance of polar factors
and elementary functional calculus near I yield

    Z_N* Z_N=I-h(C_N+C_N*)+O(h^(3/2)),
    (Z_N* Z_N)^(-1/2)=I+(h/2)(C_N+C_N*)+O(h^(3/2)),
    polar(Z_N)=I-(h/2)(C_N-C_N*)+O(h^(3/2)).                (I)

The ordinary Weyl adjoint identity is exact: Op_N(c)*=Op_N(conjugate c).
Therefore choose the fixed real symbol b=-Im c. Equation (I) becomes
polar(Z_N)=exp(i h Op_N(b))+O(h^(3/2)), proving the O(h^(3/2)) version of (A); section 5 gives its stated O(h²) remainder.

For the final O(h^(3/2)) unitary discrepancy, the principal Hermitian log
and its analytic path give maximum unfolded matching displacement O(h^1/2)
by TRACE bridge section 8. Compose that matching with (D). It preserves the
bounded displacement and q_N=O((log N)^-1/2). With reference moments through
order 2k-1, (C) gives O((log N)^-1/2) compact C^1 correlation error.
For compact continuous tests use (B). Both endpoints have identical all-order
compact limits whenever either has them, by the moment argument in section 1.

## 5. Vanishing first-order unitarity defect; O(h²) polar correction

For this real Weyl symbol the result can be strengthened without an external
FIO norm theorem. The second Taylor operator in the canonical construction is

    P2 a = -g_pp a_xx/(8pi²)
           -(g_xpp+S_xx g_ppp)a_x/(8pi²)
           -[S_xxx g_ppp/(24pi²)
             +(g_xxpp+2S_xx g_xppp+S_xx² g_pppp)/(32pi²)] a.

All g derivatives are evaluated at (x,S_x). This follows by expanding the
finite shift to order h²: the terms are l² a_xx/2,
pi i(k l²+l³S_xx)a_x, and
[pi i l³S_xxx/3-pi²(k l+l²S_xx)²/2]a, then using Fourier differentiation.
In particular P2 maps real amplitudes to real amplitudes. Since D2=iP2,
D1 is real and a1(0)=0, the transport equation makes a1 purely imaginary.
Thus c=c1=a1/a0 is imaginary and C1=Op_N(c1) is exactly skew-adjoint.
The term of order h in the polar unitarity defect vanishes.

To justify an O(h²), rather than just o(h), remainder, extend the exact
finite-shift transport by one amplitude:

    (partial_t-D1)a2=D2 a1+D3 a0,      a2(0)=0.

The same global characteristics and gluing give smooth bounded a2.
Finite Taylor remainder with three amplitudes now gives a factored O(h³)
residual, entrywise O(h^(7/2)), and operator norm O(h^(5/2)). Unitary Duhamel,
with the unchanged exact initial Gauss identity, therefore proves

    U_N=W0_N+h K1_N+h² K2_N+O_op(h^(5/2)).                 (J)

Here K2 has amplitude a2. The ratio c2=a2/a0 descends to a smooth torus symbol
by exactly (F), and (G) gives K2=Op(c2)W0+O_op(h^(1/2)).

One further Taylor coefficient in the composition with c1 gives

    Op(c1)W0=K1+h L1+O_op(h^(3/2)),                        (K)

where L1 has branch amplitude

    sum_(k,l) (c1)hat_kl e(kx+l p)
       [l (a0)_x + pi i (l² S_xx+k l)a0],   p=S_x.

The sum and every fixed derivative converge. The remainder is entrywise
O(h^(5/2)) by the second-order integral Taylor bound, summed with a fixed
higher Fourier moment. In particular modes with |l|>=N are still included.
The ratio of this amplitude to a0 defines a smooth torus symbol ell: a0_x,
S_xx and all their gluing identities agree under the same r,x,y changes as
before, while e(kx+lp) is periodic. Applying (G) to ell gives

    L1=Op(ell)W0+O_op(h^(1/2)).

Substituting into (J),(K) proves the genuine operator estimate

    U_N=[I+h C1+h²(Op(c2)-Op(ell))]W0_N+O_op(h^(5/2)).     (L)

All operators in parentheses are uniformly bounded fixed smooth symbols.
Consequently W0_N=(I-h C1+O_op(h²))U_N. Since C1*=-C1,

    ||W0_N*W0_N-I||op=O(h²),
    ||polar(W0_N)-W0_N||op=O(h²).                          (M)

Also (A) improves to O_op(h²). Its spectral-flow matching error is therefore
O(h) in unfolded units instead of O(h^(1/2)); the logarithmic RMS bound is
unchanged. This uses real principal amplitude plus explicit symbol control,
not just a vanishing formal coefficient without a controlled remainder.

Statement (M) is a singular-value/polar fact. It does NOT match eigenvalues
of the possibly nonnormal W0_N with eigenvalues of its unitary polar factor.
Such a principal-table spectral reduction requires its own argument; no
pseudospectral or nonnormal eigenvalue continuity inference is made here.

## 6. Dependency and scope audit

- Prior deterministic mechanism: ergodic-transfer supplement, sections 1–5;
  TRACE bridge section 8 supplies final o(h) maximum-displacement transfer.
- Actual logarithmic input: FM018 (O8) and (O11), with its inherited FM001,
  FM006 and checked Parry–Pollicott source leaf. This note does not redo the
  external classical mixing theorem or claim a new external source audit.
- Actual WKB input: canonical four_branch_parametrix, sections 1–2 and 4;
  two-amplitude residual O_op(h^(3/2)), exact odd-N Gauss prefactor/gluing.
- Constructive contribution of this proof: (F)–(I), direct smooth ratio symbol
  and its alias-respecting left composition, followed by polar functional
  calculus. No unspecified all-order FIO calculus is used.
- Rounding obstruction respected: O_op(h) alone is never used as smooth-symbol
  evidence. The essential input is the fixed torus symbol c extracted from
  the transported amplitudes. Spectral rounding need not have this symbol.
- The main deterministic BGS question is still open: the principal WKB polar
  factor has not been proved to have the sine-kernel factorial correlations.
  This is equivalence of two exact unitary quantization choices, not evaluation
  of either spectrum or a Heisenberg-time oscillatory cancellation estimate.
