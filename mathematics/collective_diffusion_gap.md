# Uniform two-copy collective diffusion and a refined common-noise regulator

**Claim ID:** `BGS-FM-019`. **Status:** project proof, independently
checked internally in two passes, with exact finite controls and separately
labelled floating diagnostics, 6 October 2026. Base main:
`a3d73edf6fd26485325405d4d24197730c76e9f7`.
The statements below concern a specified auxiliary noise ensemble. The
unregularized fixed map, its signed Heisenberg traces and full BGS remain
the original target. Priority and an analytic formalization are not claimed.

The [review](../archive/record/collective_diffusion_review_20261006.md) and
[programme](../archive/record/collective_diffusion_program_20261006.md) state the
acceptance and execution scope. General noise moment-semigroup and design
methods are prior; see the [source check](../literature/collective_diffusion_sources_20261006.md).

## 1. Exact objects and conclusions

Let N>=3 be odd, u>=0 real, m a positive integer, h=(N+1)/2, and
T_v T_w=exp(2 pi i h omega(v,w)/N) T_(v+w), with residue labels
v,w in (Z/N Z)^2 and omega(v,w)=v_a w_b-v_b w_a. This is the raw
modular Weyl convention of FM-018; ordinary W_v=(-1)^(v_a v_b)T_v
continues to use integer labels with its alias signs. Set Z=T_(0,1),
X=T_(1,0), and H_1=(Z+Z*)/2, H_2=(Z-Z*)/(2i), with H_3,H_4 from X.
On K_N=M((C^N) tensor (C^N)), use inner product
N^-2 Tr(C*D), collective H_l^[2]=H_l tensor I+I tensor H_l, and

$$
A_N=\frac{N^2}{2}\big((\operatorname{ad}H_1^{[2]})^2+
 (\operatorname{ad}H_2^{[2]})^2\big),\quad
B_N=\frac{N^2}{2}\big((\operatorname{ad}H_3^{[2]})^2+
 (\operatorname{ad}H_4^{[2]})^2\big),\quad L_N=A_N+B_N. \tag{D1}
$$

Here A_N is a **two-copy diffusion operator**, not the physical kick
Hamiltonian called A_N in the fixed-model proof. That Hamiltonian is
written A_N^phys whenever it occurs below. Write S_N for physical swap,
P_N for the orthogonal projection on span{I,S_N}, and Q_N=I-P_N.

**Theorem.** There is a universal constant c_0>0, independent of N
and of the unitary U, such that

$$
\ker L_N=\operatorname{span}\{I,S_N\},\qquad
 L_N\ge c_0 Q_N. \tag{D2}
$$

The proof is an analytic lattice estimate, not an inference from computed
eigenvalues. It applies also to composite odd N. Its consequences include:

1. The collective diffusion channel E_(u,N)=exp(-uL_N) obeys
   ||E_(u,N)Q_N||<=exp(-c_0 u). Multiplication on the right by
   Ad(U tensor U) preserves this bound for every U.
2. The original two Gaussian pairs, kept in their stated order, have
   the explicit, weaker bound

   $$
   \inf_{|\zeta|=1}\sigma_{\min}
   [(e^{-uA_N}e^{-uB_N}\operatorname{Ad}(U^{\otimes2})-\zeta I)
   |_{\operatorname{ran}Q_N}]
   \ge\frac{(1-N^{-1/2})(1-e^{-uN^2q_N})}{10},\quad
   q_N=16\sin^2\frac{\pi}{2N}\sin^2\frac{\pi}{N}. \tag{D3}
   $$

   At vanishing u this lower bound is of order u/N^2 and does not
   close the desired microscopic comparison for this two-kick ensemble.
3. An explicitly refined ensemble, defined in Section 7, retains common
   noise in the physical copies and has two-copy channel

   $$
   C_{N,u,m}=(e^{-(u/m)A_N}e^{-(u/m)B_N})^m
                 \operatorname{Ad}(U^{\otimes2}),\qquad
   \|C_{N,u,m}Q_N\|\le e^{-c_0u}+64\pi u^2N^3/m. \tag{D4}
   $$

   For u_N=N^-alpha, 0<alpha<1, m_N=N^3, it consequently has
   a uniform unit-circle singular gap at least c_0 u_N/4, eventually.
   This mass dominates N^-1. The one-copy channel is **exactly** the
   same D_(u,N) Ad(U) as in FM-018, at every m, not merely asymptotically.
   Section 8 gives the precise sense of the unchanged classical limit.

No nonlinear color-flavor integral, original signed noise removal or
higher-copy rate follows from this two-copy statement.

## 2. Exact total-Weyl blocks and their signs

Put s(t)=sin(2 pi h t/N), a periodic function of the integer residue t.
The N^2-dimensional spaces

$$
\mathcal K_{N,\kappa}
 =\operatorname{span}\{T_v\otimes T_{\kappa-v}:v\in(\mathbb Z/N)^2\}
 \quad(\kappa\in(\mathbb Z/N)^2) \tag{D5}
$$

give an orthogonal decomposition of K_N. Both A_N and B_N preserve
every space. To derive their action directly, write S_e=T_e tensor I+
I tensor T_e. The commutator coefficient in [T_e,T_v] is
2i s(omega(e,v)), so ad S_e takes total label kappa to kappa+e.
Applying ad S_e ad S_-e brings it back. Its diagonal coefficient is
4[s(omega(e,v))^2+s(omega(e,kappa-v))^2], and its two off-diagonal
coefficients, at v+e and v-e, are both
4s(omega(e,v))s(omega(e,kappa-v)). Thus on coefficient vectors f(a,b),

$$
\begin{split}
(A_{N,\kappa}f)(a,b)&=2N^2\{[s(a)^2+s(\kappa_a-a)^2]f(a,b)
  +s(a)s(\kappa_a-a)[f(a,b+1)+f(a,b-1)]\},\\
(B_{N,\kappa}f)(a,b)&=2N^2\{[s(b)^2+s(\kappa_b-b)^2]f(a,b)
  +s(b)s(\kappa_b-b)[f(a+1,b)+f(a-1,b)]\}.
\end{split} \tag{D6}
$$

All coefficients are real, and these are self-adjoint positive matrices.
For kappa=0, the sum is the weighted graph operator

$$
2N^2\left[\sin^2(\pi a/N)(2-U_b-U_b^*)+
              \sin^2(\pi b/N)(2-U_a-U_a^*)\right]. \tag{D7}
$$

The point (0,0) is isolated. On the remaining vertices the graph is
connected. Its two zero vectors are delta_(0,0) and the constant vector;
these represent I and N S_N, since
S_N=N^-1 sum_v T_v tensor T_-v. This identity follows by evaluating
coordinate matrix entries, or by orthonormal Weyl completeness.

Choose centered integer representatives |kappa_a|,|kappa_b|<= (N-1)/2.
Translate to y=a-kappa_a/2, z=b-kappa_b/2, and make the unitary sign
gauge (-1)^(kappa_b a+kappa_a b). The coordinate y is integral for
even kappa_a and half-integral otherwise, and similarly for z.
Use N points in the centered interval [-N/2,N/2), with integer points
[-(N-1)/2,(N-1)/2] in the integral case. The shift U_b has boundary
holonomy (-1)^kappa_a, and U_a has holonomy (-1)^kappa_b. Inside the
chosen interval all edges have the ordinary positive shift.

For theta_a=pi kappa_a/(2N), theta_b=pi kappa_b/(2N), the gauged block is

$$
\begin{split}
L_{N,\kappa}={}&2N^2\cos^2\theta_a\sin^2(\pi y/N)\Delta_b^-
 +2N^2\cos^2\theta_b\sin^2(\pi z/N)\Delta_a^-\\
&+2N^2\sin^2\theta_a\cos^2(\pi y/N)\Delta_b^+
 +2N^2\sin^2\theta_b\cos^2(\pi z/N)\Delta_a^+,\qquad
 \Delta_j^\pm=2I\pm(U_j+U_j^*). \tag{D8}
\end{split}
$$

For example s(a)s(kappa_a-a)=(-1)^kappa_a
[sin^2 theta_a-sin^2(pi y/N)]; multiplying the b-edges by the gauge
removes this sign, including its stated boundary holonomy. The diagonal
is 4N^2[sin^2 theta_a cos^2(pi y/N)+cos^2 theta_a sin^2(pi y/N)].
These identities verify every coefficient of D8 without dropping aliases.
Each of its four summands is positive because its weight commutes
with its corresponding shift. Also cos^2 theta_a,cos^2 theta_b>=1/2.

## 3. A uniform punctured-lattice Poincare estimate

Here is the needed elementary lattice lemma. There is C_*<infinity,
independent of odd N, with the following two properties for

$$
\mathfrak E_N(f)=2N^2\sum_{y,z}
 [\sin^2(\pi y/N)|f(y,z+1)-f(y,z)|^2+
  \sin^2(\pi z/N)|f(y+1,z)-f(y,z)|^2]. \tag{D9}
$$

Boundary differences carry the specified holonomy; local differences
inside the centered interval do not.

(a) On the integral grid with both holonomies +1, discard (0,0).
For the counting mean f_bar on the remaining vertices Omega_N,
sum_(Omega_N)|f-f_bar|^2<=C_* E_N(f).

(b) If at least one coordinate grid is half-integral, and its **cross**
holonomy is -1 (y half-integral means the z-cycle is antiperiodic),
then sum|f|^2<=C_* E_N(f). This includes the cases where both are
half-integral and both cycles are antiperiodic.

We provide the scale argument in detail, since pointwise lower bounds
on the smallest nonzero diffusion weights would instead lose N^2.
For |t|<=N/2,
N^2 sin^2(pi t/N)>=4t^2. It suffices to estimate the form with weights
y^2,z^2, ignoring boundary edges until the final outer-cycle estimate.

First consider a square annulus r<=max(|y|,|z|)<2r, with r>=2 and
4r<=N/2. Enlarge it to r/2<=max(|y|,|z|)<4r. Cover the enlargement
by right, left, top and bottom rectangles; the right rectangle is
r/2<=y<4r, |z|<4r. All side lengths are between fixed positive
multiples of r. Half-integral translations change counts by at most one.

On the right rectangle, average f in the z-window r<=z<2r,
separately for each y, and call the averages m_y. The elementary path
bound |sum_(1..ell) d_j|^2<=ell sum|d_j|^2, ell<=8r+2, gives

$$
\sum_{R}|f-m_y|^2\le C r^2\sum_R|D_z f|^2
 \le C\sum_R y^2|D_z f|^2. \tag{D10}
$$

The first sum on the right includes only edges in R. Applying the same
one-dimensional path bound in y to the m_y, and Jensen to their
differences, yields

$$
\sum_R|m_y-\overline m|^2
 \le C r^2\sum_{\substack{(y,z)\in R\\r\le z<2r}}|D_y f|^2
 \le C\sum_R z^2|D_y f|^2. \tag{D11}
$$

The factor counting all z in R is included on the left of D11; the
window average contributes its reciprocal. Thus the resulting factor
is r^2, rather than r^3. Replacing the comparison constant by the
mean on R can only reduce its variance. The other rectangles have
the same estimate, using a positive or negative corner window.
Adjacent rectangles overlap in a corner containing at least c r^2
vertices. The squared difference of their means is at most C/r^2
times the sum of their two variances, by averaging on that overlap.
Connecting the four means along three overlaps proves

$$
\sum_{\text{enlarged annulus}}|f-\mu|^2
 \le C\sum_{\text{enlarged annulus edges}}
 (y^2|D_z f|^2+z^2|D_y f|^2), \tag{D12}
$$

with a universal C. The same proof works for annuli cut off at N/2,
provided their inner radius is between N/16 and N/8: all widths still
have fixed comparable ratios. Edges crossing the outer cut are ignored
in D12. The central patch max(|y|,|z|)<4, with (0,0) discarded in
case (a), is a connected graph of a bounded number of vertices using
edges of positive weight. Its path proof gives the analogous estimate.
For the half-integral grids there is no isolated origin: vertical edges
are everywhere positive if y is half-integral, and horizontal edges
at z!=0 connect the columns. The transposed argument covers the other
case. These observations also prove the central patch estimate directly.

Partition the grid into this central part, dyadic square rings and a
final outer ring. For N>=65, choose the final dyadic radius r_J between
N/8 and N/4; all odd N<65 are treated by the direct path argument
below. The final ring extends to the outer coordinate cut, including
all grid points with max(|y|,|z|)=N/2 when a half-integral grid has
such a boundary point. Its enlarged comparison annulus is
r_J/2<=max(|y|,|z|)<=N/2, intersected with the chosen grid. Each ring
has M_j vertices comparable to r_j^2, with r_j=2^j up to a fixed
choice at the central patch. Adjacent ring means mu_j satisfy

$$
 |\mu_{j+1}-\mu_j|^2\le C r_j^{-2}\mathfrak E_{B_j}(f), \tag{D13}
$$

by D12 on an enlarged annulus containing both rings; B_j denotes this
enlargement. To see this without equating different means, compare
each ring mean with the mean of that enlargement, then use Jensen.
The central-to-first-ring comparison uses the fixed connected patch.
Every vertex and edge occurs in a bounded number of enlargements.

The required summation has no logarithmic loss. For arbitrary complex
d_j, Cauchy--Schwarz with weights 2^-(ell-j) gives

$$
\sum_{j=0}^{J-1}4^j\left|\sum_{\ell=j}^{J-1}d_\ell\right|^2
 \le4\sum_{\ell=0}^{J-1}4^\ell|d_\ell|^2. \tag{D14}
$$

Indeed |sum d_ell|^2<=2 sum 2^(ell-j)|d_ell|^2; interchange the
finite sums and use sum_(j<=ell)2^j<=2^(ell+1). Apply this with
d_j=mu_j-mu_(j+1). D12--D14 and bounded overlap give
sum|f-mu_J|^2<=C E_N(f). In case (a), taking the full counting mean
only reduces this variance. This proves (a).

For (b), suppose y is half-integral. In the outer strip |y|>=N/4,
the coefficient 2N^2 sin^2(pi y/N)>=N^2. The antiperiodic z-cycle
has difference eigenvalues 4sin^2(pi(ell+1/2)/N)>=4/N^2.
Consequently E_N(f)>=4 sum_(outer strip)|f|^2. This strip occupies
a fixed fraction of the final outer annulus. Its norm bound, D12
on that annulus, and averaging imply r_J^2|mu_J|^2<=C E_N(f).
Since N^2 is comparable to r_J^2, combine this with the preceding
chain estimate to obtain sum|f|^2<=C E_N(f). If z is half-integral,
transpose the proof.

For small N where the ring partition has fewer than two annuli, use
the connected finite grid directly. In case (a) every remaining vertex
connects to (1,1) using at most 4N edges of positive weight. In (b)
it connects in at most 4N edges to a full antiperiodic cycle whose
coefficient is positive. Telescoping around that cycle controls the
value at its starting point because its holonomy is -1. Cauchy--Schwarz
then gives the norm estimate with a bound C N^4; the finitely many
N below the fixed ring threshold have one universal bound. The
minimum positive weight is bounded below uniformly: integral nonzero
coordinates have 2N^2 sin^2(pi/N)>=8, and half-integral coordinates
have 2N^2 sin^2(pi/(2N))>=2. Enlarging C_* completes both assertions
for every odd N>=3. In particular c_*:=min(1,C_*^-1)>0 is universal.

## 4. All total labels, including the even nonzero labels

For kappa=0, D7 and lattice case (a) give gap c_* outside
delta_(0,0) and the constant vector.

If at least one centered kappa coordinate is odd, the first line of
D8 dominates one half of D9 with the cross antiperiodicity specified
above. Case (b) gives L_(N,kappa)>=c_*/2, without discarding a vector.

If both are even, translate to the integral grid with periodic shifts.
Call the first line of D8 M and the second R. By case (a),
M>= (c_*/2)(I-P_0), where P_0 projects on the two-dimensional space
span{delta_0,1}. For nonzero kappa put

$$
 K=2N^2(\sin^2\theta_a+\sin^2\theta_b)\ge8,
 \qquad 0\le R\le4K I. \tag{D15}
$$

There is also P_0 R P_0>= (K/2) P_0. To verify this exact compression,
write u=c 1+d delta_0. In each coordinate direction its normalized
coefficient form, before the common factor K, is

$$
 2N^2|c|^2+2|d|^2+8\operatorname{Re}(\overline c d),
 \qquad \|u\|^2=N^2|c|^2+|d|^2+
                    2\operatorname{Re}(\overline c d). \tag{D16}
$$

Here sum_y cos^2(pi y/N)=N/2; the two edges adjacent to the origin
are distinct for N>=3. With t=Nc, the first form is at least
(2-4/N)(|t|^2+|d|^2) and the norm is at most
(1+1/N)(|t|^2+|d|^2), so their ratio is at least 1/2.

For f=u+v, u=P_0 f, v=(I-P_0)f, if ||v||^2>=||u||^2/32,
the M energy is at least c_*/66 times ||f||^2. Otherwise
||R^(1/2)u||>=sqrt(K/2)||u|| and
||R^(1/2)v||<=2sqrt(K)||v||<sqrt(K/8)||u||. The triangle inequality
gives R energy at least (K/8)||u||^2>= (4K/33)||f||^2.
This is stronger than c_*/66. Taking c_0=c_*/66 proves D2 in every
block. The only kernel occurs in kappa=0, with the two vectors already
identified as I and S_N. No Lie-generation depth or prime-field argument
is needed for this quantitative estimate.

## 5. Exact pair-dephasing angle

Let P_q,P_p project on ker A_N,ker B_N, respectively. We compute their
angle on Q_N explicitly. Fourier transform in b in D6 gives the
unscaled q eigenvalues

$$
 4[s(a)^2+s(\kappa_a-a)^2+
        2s(a)s(\kappa_a-a)\cos(2\pi j/N)]. \tag{D17}
$$

Their zeros occur precisely when kappa_a=0 and either a=0 or j=0.
For odd N, two grid sine values agree up to sign only at residue
indices equal up to sign: the alternative reflection would require
a half-integer multiple of N. A zero of D17 further requires opposite
signs and j=0, unless both sine values vanish. Similarly ker B_N is
supported only on blocks with kappa_b=0. Hence P_q P_p vanishes outside
kappa=0. On that block P_q keeps row a=0 pointwise and averages every
other row in b; P_p keeps column b=0 and averages every other column.

Discard the isolated origin. The row partition has N-1 singleton
vertices (0,b), b!=0, and N-1 full rows a!=0 of size N. The column
partition is transposed. In the respective normalized indicator bases
the overlap matrix, with m=N-1, is

$$
 \begin{pmatrix}0&N^{-1/2}I_m\\
                 N^{-1/2}I_m&N^{-1}{\bf1}_m{\bf1}_m^t
 \end{pmatrix}. \tag{D18}
$$

On the zero-sum coordinate vectors its eigenvalues are +/-N^-1/2.
On the two constant coordinate vectors they are 1 and -1/N.
The eigenvalue 1 represents the counting constant on the punctured
grid. Restoring the origin adds only the other common invariant. Thus

$$
 \|P_qP_pQ_N\|=N^{-1/2},\qquad
 (2I-P_q-P_p)|_{\operatorname{ran}Q_N}\ge(1-N^{-1/2})I. \tag{D19}
$$

The last inequality also follows directly from Cauchy--Schwarz for
the two projection ranges with this angle, so no projection-spectrum
theorem is an external dependency.

## 6. Explicit bound for the original ordered two-pair ensemble

The smallest positive eigenvalue of the unscaled q generator is at
least q_N in D3, and the same holds for p. Here is a direct bound from
D17. The distinct nonnegative sine magnitudes are
sin(pi l/N), 0<=l<=(N-1)/2. Their least positive separation is
2sin(pi/(2N))sin(pi/N), by the sine-difference formula and monotonicity.
If the two magnitudes differ, D17 is at least four times this squared
separation. If both are nonzero and their signs agree, odd N gives
cos(2pi j/N)>=-cos(pi/N), so D17>=q_N. If the signs disagree and the
magnitudes agree, the zero at j=0 is omitted and the remaining values
are at least 16sin^4(pi/N)>=q_N. If one magnitude vanishes, its bound
4sin^2(pi/N)>=q_N also suffices. Therefore
A_N>=N^2 q_N(I-P_q)/2 and B_N>=N^2 q_N(I-P_p)/2.

Set F=e^-uA_N, G=e^-uB_N, and r=e^-uN^2q_N/2. On Q_N,
(I-F^2)+(I-G^2)>= (1-r^2)(1-N^-1/2) I=:h_N I.
For any unit x in that subspace put beta=1-||FGx||^2. The two losses
1-||Gx||^2 and ||(I-F^2)^(1/2)Gx||^2 are at most beta. Since
||(I-G)x||^2<=1-||Gx||^2, the triangle inequality gives
||(I-F^2)^(1/2)x||<=2sqrt(beta). Thus h_N<=5beta, and
||FGQ_N||<=sqrt(1-h_N/5)<=1-h_N/10.
Every collective conjugation and its adjoint fix I,S_N, so Ad(U tensor U)
is unitary and reducing on Q_N. The reverse triangle inequality now
proves D3. It is a genuine quantitative statement about the original
ordered ensemble, but q_N is of order N^-4 and its lower bound does
not dominate the microscopic mass when u tends to zero.

## 7. A refined ensemble with Heisenberg-scale two-copy mass

For independent standard real Gaussian four-vectors xi^(j), define
K_(t,xi) exactly as in FM-018 O22 and

$$
 \widetilde V_{N,u,m}
 =K_{u/m,\xi^{(m)}}\cdots K_{u/m,\xi^{(1)}} U,
 \quad
 K_{t,\xi}=e^{iN\sqrt t(\xi_1H_1+\xi_2H_2)}
           e^{iN\sqrt t(\xi_3H_3+\xi_4H_4)}. \tag{D20}
$$

Both physical copies use the **same complete sequence** of 4m Gaussian
variables. Independence is between sub-kicks within this one matrix,
not between copies or between powers of the matrix. Gaussian integration
within each commuting pair gives D4's exact channel. The same calculation
in one copy, where the pair diffusion operators commute, gives exactly
D_(u,N) Ad(U) for every m. The higher-copy channel generally changes
with m; this is an explicit change of regulator, not an identity for
the original m=1 law.

For bounded positive A,B, the contraction Duhamel estimate is

$$
 \|e^{-tA}e^{-tB}-e^{-t(A+B)}\|
 \le t^2\|[A,B]\|/2. \tag{D21}
$$

For example differentiate the product and use
[B,e^-sA]=integral_0^s e^-(s-r)A [A,B]e^-rA dr, with the sign immaterial
to the norm. Variation of constants and contraction of all semigroups
give D21 by integrating s from 0 to t. The coordinate q eigenvalues
are squared differences of two sums of roots of unity, hence at most
16; thus ||A_N||,||B_N||<=8N^2 and ||[A_N,B_N]||<=128 pi N^3. Indeed the four terms in
[ad S_Z ad S_Z*,ad S_X ad S_X*] each have two factors of norm
at most 4 and one commutator of norm at most 8 pi/N. The latter
is ad of a collective Weyl commutator; |exp(2 pi i/N)-1|<=2 pi/N
and its two collective terms give the bound 8 pi/N. Multiplication
by N^4/4 gives the asserted 128 pi N^3 bound.
Telescoping m products proves

$$
 \|(e^{-(u/m)A_N}e^{-(u/m)B_N})^m-e^{-uL_N}\|
 \le64\pi u^2N^3/m. \tag{D22}
$$

D2 and D22 give D4. With u=N^-alpha and m=N^3, the error is
64 pi N^-2alpha=o(u). For all sufficiently large N,
1-e^-c_0u>=c_0u/2 and the error is at most c_0u/4, so the gap is
d_N=c_0u/4. In particular N d_N->infinity. At a microscopic source
z_N=exp(-s/N+i omega/N), fixed s>=0 and real omega,
the same reverse triangle argument gives

$$
 \sigma_{\min}[(I-z_N C_{N,u_N,m_N})|_{\operatorname{ran}Q_N}]
 \ge1-e^{-c_0u_N}-64\pi N^{-2\alpha}\ge c_0u_N/4. \tag{D23}
$$

This does not assume normality. The bound holds for every U, and thus
for the unchanged actual U_N=e^(i tau N A_N^phys) M_N, tau=10^-80.
The original m=1 ensemble still has only D3 here; D22 at m=1 is
insufficient at these vanishing-noise scales.

## 8. Precise classical-limit and spectral boundaries

The statement about the classical limit is an observable comparison in
normalized Hilbert--Schmidt mean square. It does not assert uniform
operator-norm closeness of the noise matrices or a long product Egorov
theorem at m=N^3. For a fixed smooth ordinary symbol a, let
C_N=Op_N(a composed with G). The one-step Egorov bound O8 of FM-018
gives ||Ad(U_N) Op_N(a)-C_N||_HS<=C_a N^-2.
For a smooth b, its integer Fourier expansion and
ell_N(v)=2N^2[sin^2(pi v_a/N)+sin^2(pi v_b/N)] imply

$$
 \|\mathscr L_N^{1/2}\operatorname{Op}_N(b)\|_{HS}
 \le\sqrt2\pi\sum_v|b_v||v|\le C\|b\|_{H^3}, \tag{D24}
$$

even after aliases, by the triangle inequality and sin x<=|x|.
The normalized one-copy HS convention is used here. For the complete
noise product K in D20, its mean adjoint channel is exactly D_(u,N).
Unitarity therefore gives

$$
 \mathbb E\|\operatorname{Ad}(K) C_N-C_N\|_{HS}^2
 =2\langle C_N,(I-D_{u,N})C_N\rangle_{HS}
 \le2u\langle C_N,\mathscr L_N C_N\rangle_{HS}\le C_a u. \tag{D25}
$$

Combining with Egorov, using the squared triangle inequality, yields
E||Ad(tilde V) Op_N(a)-Op_N(a composed with G)||_HS^2
<=C_a(u+N^-4), uniformly in m. At u_N->0 the refined ensemble thus
retains the actual fixed map on every fixed smooth observable in this
precise mean-square sense. No growing symbol range is asserted by D25.

This ensemble samples one matrix and retains it when computing its
quenched spectral moments. Channel powers with independent new matrices
at each physical time are still a different statistic, as in FM-018 O20.
Even the strong two-copy mass does not control the full nonlinear
determinant functional or all higher moments. Nor does the mean-square
classical limit imply microscopic spectral continuity: the ensemble
need not be o(1/N) close to U_N in operator norm.

The unchanged required deterministic quantity
N^-2 sum_m w(m/N)(|Tr U_N^m|^2-m), for every fixed stable band
0<a<m/N<b<1/2, is unestimated here. TRACE-005, the higher factorial
counterterms and BGS-BGS-001 remain OPEN. The quantitative conclusion
D23 is a closed auxiliary two-copy obligation for the refined common
regulator, not a solution of those deterministic obligations.
