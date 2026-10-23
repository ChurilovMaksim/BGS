# Square-root clock rigidity for every finite unitary spectrum

Independent continuation of the Abel audit, 16 October 2026.

**Verdict:** the exponent 1/3 in the initial finite-spectrum bound improves
to 1/2. Exponent 1/2 is optimal for the stated local bounded-Lipschitz
Wasserstein distance, uniformly over unitary spectra. All arguments below
include multiplicities and N=1. They estimate the distance to the clock in
terms of the Abel excess, not the Abel excess of a physical family.

Use the functions q_s, the exact positive identity, and the semimetric d_R
from the canonical `mathematics/abel_clock_rigidity_20261016.md`. In particular the stationary unfolded process
Xi_N has intensity one and ordered q-energy density

    e_N = (1/N) sum_(j != k) sum_(l in Z) q_s(x_j-x_k+lN)
        <= 2 delta_N(s).                                      (1)

## 1. Cyclic gaps provide the improved coercivity

Sort an unfolded period x_1 <= ... <= x_N < x_1+N, retaining labels at
coincident positions. Extend by x_(j+N)=x_j+N. Define

    g_j = x_(j+1)-x_j >= 0,
    (1/N) sum_(j=1)^N g_j = 1,
    A_N = (1/N) sum_(j=1)^N (1-g_j)_+.

Thus zero gaps are allowed and contribute one to the unnormalized deficit.
For N=1 the one gap is exactly 1 and A_N=0. The mean-gap identity gives

    (1/N) sum_j (g_j-1)_+ = A_N,
    (1/N) sum_j |g_j-1| = 2 A_N.                             (2)

Set

    c_s = 4s^3/[pi^2 sinh(s)^2 (s^2+pi^2)] > 0.

For 0<=g<=1, the sine chord bound gives

    sin(pi g)/(pi g) >= (2/pi)(1-g),
    q_s(g) >= c_s(1-g)^2,                                   (3)

using continuous values at zero. For g<=1/2 apply sin(pi g)>=2g;
for g>=1/2 apply sin(pi g)>=2(1-g), and use g<=1.
Every forward nearest-neighbor pair is one of the nonnegative terms in
the full ordered q-energy sum. When N=1 its contribution is q_s(1)=0,
which is also harmless. Therefore

    (1/N) sum_j q_s(g_j) <= e_N,
    A_N <= [(1/N) sum_j (1-g_j)_+^2]^(1/2)
         <= (e_N/c_s)^(1/2).                                 (4)

The first step of (4) uses ordinary finite Cauchy--Schwarz, with the
normalization 1/N and (1-g_j)_+=0 for g_j>1.

The exact unit-interval void probability for a uniform spatial origin is

    P[Xi_N([0,1))=0]
      = (1/N) sum_j (g_j-1)_+ = A_N.                         (5)

Indeed, within a gap of length g_j the set of spatial origins from which
the following half-open unit interval is empty has length (g_j-1)_+.
These disjoint pieces exhaust the possible empty unit intervals, modulo
one period. Endpoint ambiguities are null because the origin is uniform.
This reasoning also includes zero gaps, repeated points, and periods N=1.

## 2. Coupling and boundary proof

Fix R>=0. Put

    K=ceil(R)+3, J=2K+1,
    I=[-K,K+1), M_R=2ceil(R)+6.

View Xi_N with its periodic particle labels. Each particle x has an incoming
gap g^-(x) and outgoing gap g^+(x). They may be zero. Define the local mark

    D_I = sum_(x in Xi_N cap I)
                 [|g^-(x)-1|+|g^+(x)-1|].

Period averaging and (2) give the exact expectation

    E D_I = 4J A_N.                                         (6)

The identity remains valid when I is longer than the period: each labelled
image is counted as its own particle. Select the leftmost particle Y in
[0,1), with any measurable tie rule. On the void event choose Y=0 for
the construction only. Define the good event

    G={Xi_N([0,1))>=1 and D_I<=1/4}.

Equations (5), (6), and Markov give

    P(G^c) <= A_N + 16J A_N.                                 (7)

On G there are no coincidences in I: a zero incoming or outgoing gap at
such a particle would contribute one to D_I. Index the bi-infinite actual
particles consecutively with p_0=Y and compare p_n with a_n=Y+n.
For each p_n in I, telescoping consecutive gaps from Y to p_n gives

    |p_n-a_n| <= D_I.                                        (8)

For n>0 use outgoing gap marks, and for n<0 use incoming marks. No gap is
used more than once in a given telescope; its initial or terminal particle
lies in I. The same bound holds for the first particle to the right of I
and the first particle to its left, because the final boundary-crossing
gap is marked at its endpoint inside I. Both incoming and outgoing marks
were included precisely for this boundary reason.

This proves that every clock site a_n in [-R-1,R+2] has its indexed actual
partner p_n inside I. To see this explicitly on the right, if p_n were
outside I, let p_b be the first exterior right particle. Then b<=n and

    a_b >= K+1-D_I >= K+3/4 > R+2,

contradicting a_b<=a_n<=R+2. On the left, if p_b is the first exterior
left particle, then

    a_b <= -K+D_I <= -K+1/4 < -R-1,

which contradicts a_b>=a_n>=-R-1. Points exactly on the deterministic
boundary of I occur with probability zero under the uniform origin;
the displayed weak inequalities also leave the required strict margins.
Conversely any actual particle in [-R,R+1] has a partner clock site in
[-R-1,R+2] by (8). Thus no relevant missing site or exterior point is
omitted.

On G choose the matched clock Y+Z; off G choose Z. Let T be an independent
uniform variable on [0,1), and translate BOTH the actual process and the
chosen clock by -T. The actual process retains its original law by
stationarity. Conditional on the entire initial process the clock phase
is either Y-T or -T modulo one, which is exactly uniform. This is a
coupling with the desired uniformly shifted clock law.

For a test phi in d_R, the original coordinates of its translated support
lie in [-R+T,R+T] subset [-R,R+1]. Bounds (8) and the boundary argument
therefore cover every contributing actual particle and every contributing
clock site. There are at most M_R relevant sites: if phi(p_n-T) or
phi(a_n-T) is nonzero, then a_n belongs to the interval

    [-R+T-D_I,R+T+D_I],

whose length is at most 2R+1/2. The chosen M_R is a convenient upper bound
on its number of integer-spaced sites. Global Lipschitz continuity of phi
gives

    d_R(Xi_N-T, chosen_clock-T) <= M_R D_I on G.

The distance is at most one off G. Combining (6) and (7),

    W_(d_R)(Law(Xi_N),Law(Z+U))
      <= C_R A_N,
    C_R = 1+16J+4J M_R.                                      (9)

This constant is explicit, dimension-independent and not optimized.
Consequently, for every s>0, N>=1, and R>=0,

    W_(d_R)(Law(Xi_N),Law(Z+U))
      <= min(1, C_R sqrt(2/c_s) sqrt(delta_N(s))).            (10)

No separate count-UI premise is used. Formula (10) strengthens the finite
spectral implication; the earlier elementary general stationary-process
1/3 theorem can remain as a separate statement.

## 3. Exact alternating family and optimality

Let N be any even integer, 0<epsilon<1/4, and set

    x_j=j+epsilon(-1)^j, 0<=j<N,
    theta_j=x_j/N modulo 1.

The full periodically extended unfolded configuration has period 2. Its
gaps alternate between 1-2epsilon and 1+2epsilon. In particular A_N=epsilon.
Writing z=exp(-s), direct geometric summation gives T_m=0 unless m=qN/2,
and, at those frequencies,

    |T_(qN/2)|^2/N^2 = [1+(-1)^q cos(2pi q epsilon)]/2.

Therefore the exact excess is

    delta_N(s)
      = z(1-z)[1-cos(2pi epsilon)]
        /[2(1+z)(1+2z cos(2pi epsilon)+z^2)].                 (11)

This does not depend on the even dimension N. For fixed s>0,

    delta_N(s) = [pi^2 z(1-z)/(1+z)^3] epsilon^2
                   + O_s(epsilon^4).                       (12)

The coefficient is strictly positive.

There is also the uniform lower bound

    d_2(mu, Z+t) >= epsilon                                 (13)

for EVERY translate mu of this period-2 configuration and EVERY real
clock phase t. To verify this without a generic-origin caveat, the
half-open interval [-1,1) contains exactly two actual particles for any
translate: every half-open interval of length two contains one full
period, including translates with particles on its boundary. These two
particles are consecutive, with separation 1+2epsilon or 1-2epsilon.
Their fractional phases have circular distance 2epsilon. By the circle
triangle inequality, at least one has distance at least epsilon from the
fractional phase t. Both particles lie in [-1,1], at distance at least one
from the boundary of [-2,2].

The function

    phi_t(x)=min(dist(x,Z+t), (2-|x|)_+, 1)

is nonnegative, globally 1-Lipschitz, bounded by one, and supported on
[-2,2]. It vanishes on the target clock. At the selected actual particle
its value is at least epsilon, so its integral against mu is at least
epsilon. This proves (13), including all root shifts and clock phases.

Every coupling with a random-phase clock is supported on pairs satisfying
(13). Thus W_(d_2)>=epsilon for the alternating family. Combining this
with (12), no bound with delta_N(s)^alpha and a dimension-independent
constant can hold for all spectra when alpha>1/2. In fact the contradiction
already holds at N=2 as epsilon tends to zero; taking any even N->infinity
gives the same obstruction if a large-dimension qualification is imposed.

## 4. CUE factor review

The canonical note's formula

    G_s-I_s = (1/2) integral_R q_s(x)[1-sinc(x)^2] dx

has the CORRECT factor 1/2. At finite dimension, translation invariance of
the unfolded CUE factorial density rho_(2,N)(x-y) gives

    E[(1/(2N)) sum_(j!=k) q_s^[N](x_j-x_k)]
       = (1/2) integral_0^N q_s^[N](x) rho_(2,N)(x) dx
       = (1/2) integral_R q_s(x) rho_(2,N)(x) dx.

Here rho_(2,N)(x)=1-[sin(pi x)/(N sin(pi x/N))]^2, continuously at
its apparent singularities. It is periodic, lies in [0,1], and converges
pointwise to 1-sinc(x)^2. Since q_s is integrable, dominated convergence
proves the displayed limit with factor 1/2. The canonical low-mode integral

    I_s=[sinh(2s)-2s-(4/3)s^3]/[8s^2 sinh(s)^2]

also follows by direct integration and is consistent with this normalization.

The finite checks in `verify_square_root.py` are numerical supplements;
the analytic arguments above establish the theorem and rate optimality.

## 5. General stationary square-root extension

16 October 2026. This upgrades the general-process cube-root bound and uses
the same coupling as `square_root_rigidity.md`. It requires stationarity,
local finiteness, intensity one, and finite ordered q_s-energy density e.
Multiplicity is allowed. No ergodicity, independent count-UI, or prior Palm
inversion theorem is required.

Let

    c_s=4s^3/[pi^2 sinh(s)^2(s^2+pi^2)],
    K=ceil(R)+3, J=2K+1, M_R=2ceil(R)+6,
    C_R=1+16J+4J M_R.

Then the stronger general theorem is

    W_(d_R)(Law(Xi),Law(Z+U))
        <= min(1, C_R sqrt(e/c_s)).                         (G1)

The alternating period-two family from `square_root_rigidity.md` proves
that exponent 1/2 cannot be increased uniformly over this class.

### 1. Gap marks exist without an ergodicity assumption

Almost surely every nonempty stationary locally finite configuration is
unbounded in both directions. Indeed, on the translation-invariant event
that a nonempty configuration is bounded below, it has a finite leftmost
coordinate L. The finite subprobability distribution of L on that event
would be invariant under every translation. The equal masses of the
intervals [k,k+1), k in Z, must then all be zero, so the event has probability
zero. The rightmost-coordinate argument is identical. Local finiteness
ensures that a leftmost coordinate exists whenever a nonempty support is
bounded below.

At each location with m copies, assign internal ranks 1,...,m and order
particles lexicographically by location and rank. This convention is
translation covariant. On a nonempty configuration, each particle has an
immediate successor and predecessor. Its outgoing gap g^+ and incoming
gap g^- are finite and nonnegative; all but one outgoing gap at an m-fold
site are zero. Artificial ranks do not change the counting process or its
energy.

Define the probability measure of the outgoing gap mark by

    nu(B)=E sum_(x in Xi cap [0,1)) 1{g^+(x) in B}.

Its total mass is one because Xi has intensity one. Stationarity implies
the elementary marked intensity identity

    E sum_(x in Xi) F(x,g^+(x))
        = integral_R integral_[0,infinity) F(x,g) nu(dg) dx    (G2)

for every nonnegative Borel function F. To prove (G2), first take rectangle
indicators: the expected mark counting measure in its location variable is
translation invariant, and hence is Lebesgue measure times its unit-interval
value. Simple-function approximation and monotone convergence finish the
proof. Thus no conditional Palm construction is being assumed.

### 2. Mean gap and void identities

Let p0 be the probability of a globally empty configuration. On a nonempty
configuration, the half-open positive gap intervals [x,x+g^+(x)) partition
the real line, ignoring the zero-length intervals at repeated points.
At zero their coverage number is therefore 1; on an empty configuration
it is 0. Apply (G2) and Tonelli to the coverage indicator to obtain

    integral g nu(dg)=1-p0.                                 (G3)

In particular the mean gap is finite without an extra hypothesis.

On a nonempty configuration, the unit interval [0,1) is empty precisely
when zero lies in the interior portion of one gap remaining after its
last unit length is removed. This portion has length (g-1)_+. Potential
endpoint equalities have zero probability: the mean measure of points at
any prescribed coordinate is zero by intensity one. Formula (G2) gives

    P[Xi([0,1))=0]=p0+integral(g-1)_+ nu(dg).                (G4)

Set A=integral(1-g)_+ nu(dg). By (G3),

    integral(g-1)_+ nu(dg)=A-p0,
    P[Xi([0,1))=0]=A,
    B:=integral|g-1| nu(dg)=2A-p0<=2A.                     (G5)

These identities permit nonempty components of different intensities and
an empty component; no hidden ergodicity assumption is used.

### 3. Incoming marks and energy coercivity

The incoming and outgoing gap mark distributions agree. For any bounded
function h, sums of h(g^+) and h(g^-) over particles in [0,L) cancel edge
by edge except for at most one edge crossing each endpoint. Their difference
has absolute value at most 2||h||_infinity, pathwise, including multiplicities.
Taking expectations and applying stationarity yields

    L |integral h dnu^+ - integral h dnu^-| <= 2||h||_infinity.

Let L tend to infinity. Equality of bounded mark integrals follows, and
truncation extends it to nonnegative unbounded h. In particular, both
incoming and outgoing |g-1| marks have mean B.

Every outgoing successor is a different particle, including when its gap
is zero. Its q_s(g) contribution is contained in the full ordered q-energy.
Thus integral q_s(g) nu(dg)<=e. The chord bound (3) of the finite proof and
Cauchy--Schwarz against the probability measure nu give

    A <= [integral(1-g)_+^2 nu(dg)]^(1/2)
      <= sqrt(e/c_s).                                       (G6)

### 4. Apply the explicit coupling

On I=[-K,K+1) set

    D_I=sum_(x in Xi cap I)[|g^-(x)-1|+|g^+(x)-1|].

Equations (G2), (G5), and incoming-mark equality give

    E D_I=2J B<=4J A.

Select the leftmost point in [0,1) as anchor. The event of no anchor has
probability A by (G5). On the event with an anchor and D_I<=1/4, consecutive
particles in I, together with their first exterior neighbors, match the
anchor's consecutive lattice labels with displacement at most D_I.
The complete boundary and test-support argument is exactly the one in
Section 2 above; it uses no periodicity, fixed number
of particles, or finite total spectrum. Nonemptiness and two-sided
unboundedness supply the bi-infinite ordering it needs.

The bad-event probability is at most A+16J A; the good-event local d_R
cost is at most M_R D_I. Translate both configurations by an independent
uniform T in [0,1) to make the clock phase exactly uniform while preserving
the stationary process law. The resulting coupling has expected distance
at most (1+16J+4JM_R)A. Combining with (G6) proves (G1).

The extra local count bound already established from q_s near zero remains
valid. It is separate from this proof and supplies first-count-moment UI
for a bounded-energy sequence; neither it nor a higher-moment hypothesis
is assumed to derive the square-root estimate.
