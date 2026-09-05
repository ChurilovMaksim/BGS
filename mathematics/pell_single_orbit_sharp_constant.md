# Sharp finite-span coercivity for a single Fourier orbit

Status: an analytic project result with a self-contained proof below. No
world-priority or positive BGS claim is made. The accompanying rational
checker has a narrower finite verification scope; its existence alone does
not certify execution. This note strengthens the earlier single-orbit lower
bound by solving the autocorrelation realizability problem explicitly.

## 1. Statement and normalization

Let T=((3,2),(4,3)), lambda=3+2sqrt(2), and b_v(x)=2 cos(2 pi v.x).
Set C b_v=b_(Tv), and use the Poisson bracket
{f,g}=f_(x1)g_(x2)-f_(x2)g_(x1). For an even real mean-zero Fourier
polynomial h, write its cosine coefficients as a_w, one coefficient for
w modulo sign. Define

    sigma^2(h) = 2 sum_O (sum_(w in O modulo sign) a_w)^2,
    Gamma(g) = sigma^2({g,Cg}/(4 pi)),

where O ranges over the signed T-orbits of nonzero integer frequencies.
Fix v=(a,b) not equal to zero and a nonnegative integer L. Consider

    g = sum_(j=0)^L c_j b_(T^j v),    c_j real,
    C_r = sum_j c_j c_(j+r),         c_j=0 outside [0,L],
    d_r = det(v,T^r v),             M=floor(L/2),
    S_M = sum_(k=0)^M 1/d_(2k+1)^2.

The determinant d_1=4a^2-2b^2 is nonzero. Each subsequent d_r is nonzero,
and d_r/d_1=(lambda^r-lambda^(-r))/(lambda-lambda^(-1)).

THEOREM. The exact minimum over nonzero coefficient vectors is

    min Gamma(g)/||g||_L2^4 = pi^2/S_M.                    (1)

Equivalently, with C_0=sum_j c_j^2,

    Gamma(g) >= 4 pi^2 C_0^2/S_M,                        (2)

and equality is attained by a real coefficient vector supported at the even
times 0,2,...,2M. A translation of all time labels leaves the statement
unchanged. In particular increasing the permitted span from 2M to 2M+1
does not change the minimum.

The optimum over all finite spans is the infimum

    inf Gamma(g)/||g||_L2^4
        = pi^2 / sum_(k>=0) d_(2k+1)^(-2).                (3)

It is not attained by any nonzero finite coefficient vector. Formula (3)
is a sharp infimum, whereas (1) is an attained finite-dimensional minimum.

## 2. Exact reduction to autocorrelations

Direct differentiation gives

    {b_u,b_w}/(4 pi) = pi det(u,w) (b_(u-w)-b_(u+w)).

Combining the j,l and l,j terms in {g,Cg}, for r=l-j>=1 the coefficient
at the translated minus frequency T^j(v-T^r v) is

    pi d_r (c_j c_(j+r-1)-c_(j+r)c_(j-1)),

and the coefficient at the corresponding plus frequency has the opposite
sign. Summing over j gives pi d_r(C_(r-1)-C_(r+1)).

These generated frequency classes must not be assumed disjoint without
proof. Identify (a,b) with b+sqrt(2)a, whose multiplication under T is by
lambda and whose quadratic norm is Q(v)=b^2-2a^2, which is nonzero. Then

    Q(v+T^r v)=Q(v)(2+lambda^r+lambda^(-r)),
    Q(v-T^r v)=Q(v)(2-lambda^r-lambda^(-r)).

For r>=1 the signs are opposite and the absolute values within each sign
increase strictly with r. Since Q is invariant under plus or minus T,
all the generated plus/minus orbit classes are different. Also a nonzero
vector cannot be periodic under plus or minus T in characteristic zero.
Consequently the exact identity is

    Gamma(g) = 4 pi^2 sum_(r>=1)
                         d_r^2(C_(r-1)-C_(r+1))^2.       (4)

Cosine orthogonality gives ||g||_L2^2=2C_0.

## 3. Lower bound and equality conditions

Because C_r=0 for r>L,

    C_0 = sum_(k=0)^M (C_(2k)-C_(2k+2)).

Weighted Cauchy--Schwarz yields

    C_0^2 <= S_M sum_(k=0)^M
                  d_(2k+1)^2(C_(2k)-C_(2k+2))^2.

The last sum is a sub-sum of (4), proving (2). To attain equality it is
necessary and sufficient to have

    C_(2k) = C_0 [sum_(j=k)^M d_(2j+1)^(-2)]/S_M, 0<=k<=M,
    C_(2k+1)=0,                                  k>=0.    (5)

Necessity includes the vanishing of all the nonnegative even-r summands
in (4), which forces the odd autocorrelations to vanish since they have
finite support. It remains to show that (5) is an actual autocorrelation
of a real finite sequence. Positive values and a formal Cauchy--Schwarz
equality are not by themselves sufficient for this step.

## 4. Realizability by a positive trigonometric polynomial

Normalize C_0=1. Put w_j=d_(2j+1)^(-2) for 0<=j<=M, and w_(M+1)=0.
The finite sequence w is strictly decreasing and positive up to M. Set

    a_j = (j+1)(w_j-w_(j+1))/S_M,   0<=j<=M.

Every a_j is positive, and telescoping gives sum a_j=1. Let

    F_j(theta)=|sum_(l=0)^j exp(i l theta)|^2/(j+1)

be the Fejer kernel with constant Fourier coefficient one, and define

    P_M(theta)=sum_(j=0)^M a_j F_j(theta).

Since F_j is nonnegative and F_0=1, P_M is strictly positive everywhere.
Its Fourier coefficient at k>=0 is

    sum_(j=k)^M a_j(1-k/(j+1))
        = [sum_(j=k)^M w_j]/S_M,

precisely the even autocorrelation desired in (5), now indexed by k.
The elementary real Fejer--Riesz factorization therefore gives a real
polynomial p(z)=sum_(j=0)^M u_j z^j such that

    P_M(theta)=|p(exp(i theta))|^2.

Here is a root proof of the required real factorization. Multiply the real
reciprocal Laurent polynomial P_M(z) by z^M. Its roots come in reciprocal
and complex-conjugate pairs, and none lies on the unit circle because P_M
is strictly positive there. Choose the M roots outside the unit disc,
including complex conjugate pairs together. The resulting factor has real
coefficients. Its product with its reciprocal has the same roots and
multiplicities as z^M P_M. On the unit circle the ratio of P_M to the squared
modulus of this real factor is a positive constant. A positive real scaling
of the factor yields the stated identity. The constant case M=0 is immediate.

Now set c_(2j)=u_j and c_(2j+1)=0. Its autocorrelation has (5), and its norm
satisfies C_0=1. Thus it attains (2). Scaling produces every positive C_0.
This proves (1), including actual real-coefficient realizability, not just
a relaxation of the coefficient optimization problem.

## 5. Infinite-span sharpness and elementary examples

The sum S_infinity is finite because

    |d_r|/|d_1| >= lambda^(r-1), r>=1.

For every finite M, S_M<S_infinity. The attained minima pi^2/S_M decrease
to pi^2/S_infinity, proving (3). Every finite nonzero sequence obeys its
strictly larger finite-span bound, so no such sequence attains the infinite
infimum.

Let D_r=d_r/d_1. These integers satisfy D_1=1, D_2=6,
D_(r+1)=6D_r-D_(r-1). In particular D_3=35, D_5=1189, D_7=40391. The
universal dimensionless factor in (3) is therefore exactly

    beta = 1/(1 + 1/35^2 + 1/1189^2 + 1/40391^2 + ...).

This is not a decimal fit. It obeys 1-lambda^(-4)<=beta<1.
For spans L=0 or 1, the optimal ratio is pi^2 d_1^2. For spans L=2 or 3,

    min Gamma(g)/||g||_L2^4 = pi^2 d_1^2 (1225/1226).       (6)

At C_0=1 one may take

    c_0=(sqrt(614/613)+sqrt(612/613))/2,
    c_2=(sqrt(614/613)-sqrt(612/613))/2,
    c_1=0.

Indeed c_0^2+c_2^2=1 and c_0 c_2=1/1226. Equation (4) reduces to
4 pi^2 d_1^2[(1-C_2)^2+1225 C_2^2], whose minimum occurs at C_2=1/1226.
This explicitly disproves the stronger but false assertion that a single
cosine minimizes Gamma at fixed L2 norm.

For a rational finite-N-independent error bound on beta, one may use
lambda>5 and D_(2k+1)>=lambda^(2k)>5^(2k). The tail after k=M is smaller
than

    5^(-4(M+1))/(1-5^(-4)).

Computing the rational partial sum and this rational tail encloses beta by
reciprocation, without evaluating an irrational number or a trigonometric
function in floating point.

## 6. Scientific boundary

This theorem concerns a single Fourier orbit of the fixed cat map. For
several initial frequency orbits, generated plus/minus classes can collide,
and equation (4) need not remain valid. It does not replace their actual
orbit grouping by a sum of positive independent contributions.

The argument uses standard Fourier differentiation, quadratic norm separation,
Cauchy--Schwarz and real spectral factorization. It does not claim to invent
Fejer kernels or the Fejer--Riesz theorem. Its project-level advance is the
exact finite-span minimum and its attainable autocorrelation classification.
It neither proves positive microscopic BGS nor establishes world priority.
