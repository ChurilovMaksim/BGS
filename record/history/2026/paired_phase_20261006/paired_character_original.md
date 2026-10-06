# Actual paired-box coordinates and the exact autocorrelation character

Author checkpoint, 6 October 2026. Base 300d99270d11c87d0aa84e9d8f624491788629ba,
with current curated source hashes in source_manifest.json. No canonical edits.
The target remains the actual signed TRACE-005 hierarchy at tau=10^-80.
This note proves an exact coordinate/phase reduction, not the needed cancellation
estimate. No new prior-art claim is made for finite quadratic Gauss identities.

## 1. Target and first uncertain leaf

For every fixed smooth w supported in (0,1/2), prove

J_N,w=N^-2 sum_m w(m/N)(|Tr U_N^m|²-m)->0.

The accepted fixed-order WKB and rotated-box results permit using exact
nonlinear local amplitudes through this entire Heisenberg band. The proposed
signed mechanism is finite-group character cancellation in the paired box sum.
The first needed estimate is an ACTUAL autocorrelation Fourier coefficient
at a frequency coupled to the displacement, defined in section 6. It is not
a P/Q gap, an individual box's absolute error, or a short-time trace estimate.

Before estimating it, the redundant branch coordinates must be treated correctly.
A single winding group Z^m/B_m Z^m is not automatically the physical label group.
This is a NEW-coordinate warning, not a correction of the accepted formulas:
they already include all 4^m copies with the correct 4^-m average.

## 2. Exact integer-translation identity at the unchanged coupling

Let S_r(t,x,y) be the actual HJ phase extended to every integer r. For integers
z,w, uniqueness of the HJ solution and direct quadratic evaluation at t=0 give

S_r(t,x+z,y+w)
 =S_(r+w-3z)(t,x,y)-2zy-2rz-2wz+3z².                 (P1)

Its x-gradient agrees on both sides, and g(x+z,p)=g(x,p). Likewise

S_(s+4l)(t,x,y)=S_s(t,x,y)+l x-3l y-3ls-6l².         (P2)

Here the momentum shift is integral, so the actual periodic g again gives
uniqueness. Every finite transport amplitude obeys the same gluing WITHOUT
an additional factor: the phase-gradient shifts are integral, while higher
phase derivatives and all symbol coefficients entering its recursion agree.
Thus (P1-P2) hold at literal t=tau, for the actual all-order local construction.

For a branch vector r and winding nu, define
Psi_(r,nu)(x)=sum_j S_(r_j)(tau,x_j,x_(j+1))+nu.x.
Translate by an integer vector z and put

r'_j=r_j+z_(j+1)-3z_j=s_j+4l_j, 0<=s_j<4,
nu'_j=nu_j-2z_(j-1)+l_j-3l_(j-1).

Then

Psi_(r,nu)(x+z)=Psi_(s,nu')(x)+an integer.             (P3)

Amplitudes match exactly. Consequently their global center-based Abel integrals
are identical, as are their exact rotated boxes: the cat and actual stationary
centers both translate by z, so the regulators/boxes translate with them.
The phase constant contributes e(N integer)=1. This is not a comparison of
neighbouring operators or a first-order approximation in tau.

If z is replaced by z+4w, r returns to the same residue and nu changes by
-B_m w, B_m=6I-P_m-P_m^T. Therefore (P3) defines an action of (Z/4)^m on

L_m={0,1,2,3}^m x (Z^m/B_m Z^m).

This action is free. Indeed its cat stationary center is
x_(r,nu)^0=B_m^-1(t_r+4nu), t_(r,j)=r_j-3r_(j-1).
A fixed class under translation z would make its center differ from itself
both by z and by 4w for an integer w. Hence z=0 in (Z/4)^m.

Thus the 4^m det B_m listed terms form exactly det B_m orbits, each with
4^m IDENTICAL contributions. There is no signed cancellation in removing
these duplicate copies, and no pre-existing normalization error.

## 3. The correct finite abelian label group

Let S=[[3,4],[2,3]], A=S^m, and

G_m={z in R²/Z²:(A-I)z=0 in R²/Z²}.

It has D_m=|det(A-I)|=det B_m elements. At zero coupling map a branch/winding
class to its initial point

q=x_0^0 mod1,
p=(x_1^0+r_0-3x_0^0)/4 mod1.                         (P4)

The stationary equations make the successive pairs follow S modulo one.
Indeed q_(j+1)+r_j=3q_j+4p_j and the incoming momentum is 2q_j+3p_j;
the winding condition identifies it with p_(j+1) modulo one.

Integer translations in (P3) preserve (P4). Conversely, equal initial points
modulo one force all subsequent cat coordinates to differ by integers and
hence are related by (P3). The free quotient is therefore G_m.
Its group law is the CAT LABEL group law. Actual continued stationary points
at tau are not asserted to be translates of each other under this law.

Small-dimensional check: at m=1, the single winding group is Z/4 whereas
G_1=(Z/2)^2. At m=2 their Smith forms are (2,16) and (4,8), respectively.
Dropping branches before applying Fourier orthogonality would use the wrong
quadratic group. Keeping the original sum or taking the exact quotient both
preserve the accepted result.

## 4. A quadratic refinement and its perfect pairing

Write z=(q,p), choose any real lift with n=(A-I)z=(n_q,n_p) integer, and define

Q_m(z)=1/2[omega(z,n)-n_q n_p] mod1,
omega((q,p),(q',p'))=q p'-p q'.                       (P5)

This is the exact zero-coupling stationary action. To verify it, use the
unwrapped cat trajectory (q_j,p_j)=S^j z. The one-step quadratic generating
function satisfies

S_0(q_j,q_(j+1))=-1/2[q_(j+1)p_(j+1)-q_jp_j].

Choose only the final branch r_(m-1)=n_q and initial winding nu_0=n_p.
The sum telescopes to (P5). Reducing these integers to the conventional
branch/winding representatives changes it only by the integer in (P3).

Since A is symplectic,

B_m(z,d):=Q_m(z+d)-Q_m(z)-Q_m(d)
 =omega(z,(A-I)d) mod1.                              (P6)

The right side is symmetric modulo one. In deriving it, the residual term
is the integer -n_(z,p)n_(d,q). As A is the identity modulo two, Q_m(k) is
integral for k in Z². Also omega(z,(A-I)k) is integral for z in G_m, by
symplecticity and Az-z integer. Thus Q_m and B_m are well-defined on G_m,
and Q_m(a z)=a² Q_m(z) for integers a.

The pairing B_m is perfect. Every integer n represents d=(A-I)^-1 n in G_m;
if omega(z,n) is integral for every n, z is an integer point and hence zero.
Therefore all characters of G_m are e(B_m(z,d)), indexed uniquely by d.
No coprimality condition on N and D_m is used.

## 5. Exact trace coefficient after removing duplicates

Let I_z(tau;N,J) be any one of the IDENTICAL global Fresnel integrals in the
quotient class z. Its phase includes the winding linear term and its finite-J
amplitude is unchanged. Define

alpha_(N,m,J)(z)=e^(i pi m/4) sqrt(D_m) N^(m/2) 2^-m
                e(-N Q_m(z)) I_z(tau;N,J).

Then exact Gaussian reciprocity and (P3) give

Tr V_(N,J)^m
 =zeta_(N,m) D_m^-1/2 sum_(z in G_m) e(N Q_m(z)) alpha_(N,m,J)(z),
zeta_(N,m)=e(3mN/8)e^(-i pi m/4).                     (P7)

The old integral prefactor 8^-m becomes 2^-m because exactly 4^m duplicate
terms have been removed. At zero coupling every alpha is exactly one for
the GLOBAL Fresnel integrals. This last statement is not exact for truncated
boxes, whose Gaussian tails remain present.

For the actual fixed tau, alpha retains all nonlinear actions, local quantum
corrections and global integral phases. No closeness to one or smoothness
uniform in m of its label dependence is assumed. Through m<=2N it may instead
be defined using the exact rotated boxes, at the accepted summed contour error.
The WKB-to-actual trace error remains the separate fixed-J estimate.

## 6. The exact paired character identity

For ANY function alpha on G_m and any integer N, define

C_d(z)=alpha(z+d) conjugate(alpha(z)),
C_hat_d(xi)=D_m^-1 sum_z C_d(z)e(-B_m(z,xi)).

Expanding the squared modulus in (P7), setting the first label to z+d, and
using (P6) proves

|Tr V_(N,J)^m|²
 =sum_(d in G_m) e(N Q_m(d)) C_hat_d(-N d).            (P8)

This is an exact identity, not an absolute estimate. It retains signs in both
the character transform and the displacement sum. In the stable band, the
required comparison becomes precisely the weighted signed sum of the right
side minus m; the fixed-J comparison controls its replacement of U_N.
The unknown estimate is for the ACTUAL alpha in (P7), not arbitrary alpha.

The d=0 term is D_m^-1 sum_z |alpha(z)|². Neither its value nor the other
selected Fourier coefficients is estimated here. In particular, separate
pointwise smallness of every off-zero C_hat_d is not substituted for the
complete signed m,d sum.

## 7. Exact arithmetic calibration and the first test

At zero coupling alpha=1. Orthogonality in (P8) leaves exactly d in ker[N:G_m->G_m].
For odd N, e(N Q_m(d))=1 on this kernel: both N²Q_m(d) and 2NQ_m(d) are
integers, so NQ_m(d) is integral since gcd(N,2)=1. Therefore

|Tr M_N^m|²=|ker[N:G_m->G_m]|.                        (P9)

This calibrates every resonant and nonresonant dimension without erasing
arithmetic torsion. It is a familiar cat-map Gauss identity, now recovered
from the exact coordinate quotient used by the nonlinear representation.

For a phase-only first response alpha_t(z)=exp(iNt C_m(z)), with
C_m(z)=sum_(j=0)^(m-1)g(S^j z), the selected derivative is

D_m^-1 sum_z e(N B_m(z,d))[C_m(z+d)-C_m(z)]
 =[e(-N B_m(d,d))-1] C_hat_m(-Nd).                    (P10)

This is an exact translation identity. It vanishes automatically at all
resonant d in ker N for every symbol, so initial linear response cannot
remove those arithmetic terms. The second phase-only response involves
D_m^-1 sum_z |C_m(z+d)-C_m(z)|². Exact actual-symbol checks of this response
are recorded separately. They are not a fixed-tau closure theorem: the true
alpha in (P7) also contains nonlinear action and transport corrections.

## 8. Executed scope and remaining obligation

check_branch_quotient.py performed exact integer/cyclotomic checks:
- m=1,2,3,4: 307,984 listed classes collapse with exactly 4^m copies each;
- 1,366,560 polarization identities and perfect-pairing checks;
- 16 exact Gauss-norm calibrations, N=3,5,7,9 at those m, including
  (m,N)=(3,7),(4,3),(4,9).
No floating-point spectrum, changing tau or Heisenberg extrapolation is used.

The mathematical conclusion so far is (P1-P8), not cancellation of the
actual coefficients. The finite group law labels continued cat classes;
it is not a translation symmetry of the perturbed classical dynamics.
Consequently one cannot apply a translated-symbol finite-type bound directly
to C_d without first identifying the exact nonlinear action dependence.
The full signed autocorrelation sum for the actual alpha remains open.
