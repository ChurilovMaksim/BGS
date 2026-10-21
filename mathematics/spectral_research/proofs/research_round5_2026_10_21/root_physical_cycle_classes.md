> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/root_physical_cycle_classes.md`. Embedded SHA256: `de9d6a510aa9c6e36f30a1d42d7c5e3760e71e594cbf0335a4c1a1653ac7708d`.
> [Thematic guide](../../topics/histories.md).

# Exact forward and reversed physical cycle classes at all times

Round 5, 21 October 2026. This note proves finite matrix identities and bounds
for specific coherent path classes. Application to the original U_N uses the
four-branch kernel and oscillatory matrix theorem of the companion notes.
The full H_diag assertion remains open: paths in different, nonreversed
rotation classes are not estimated by this argument.

## 1. Definitions without multiplicity ambiguity

Let U be an N by N unitary matrix, and put

$$
P_{xy}=|U_{xy}|^2,\quad Q_{xy}=U_{xy}\overline{U_{yx}},
\quad J_{xy}=1/N.
\tag{1}
$$

For n>=1 a rooted path is a word x=(x_0,...,x_{n-1}) in {0,...,N-1}^n;
indices in the word are cyclic. Set

$$
a(x)=\prod_{j=0}^{n-1}U_{x_j,x_{j+1}}.
\tag{2}
$$

Let Rot(x) denote the set of DISTINCT cyclic rotations of the word. Its
cardinality d(x) is the least positive period of x, and divides n. Define
Rx=(x_0,x_{n-1},...,x_1), so that a(Rx) uses every edge in the opposite
orientation. The choice of initial point in Rx is immaterial to its rotation
class. Direct expansion gives

$$
|\operatorname{Tr}U^n|^2=\sum_{x,y}a(x)\overline{a(y)}.
\tag{3}
$$

Define the following three DISJOINT classes in this exact sum:

$$
\begin{split}
D_n&=\sum_x\sum_{y\in\mathrm{Rot}(x)}a(x)\overline{a(y)},\\
R_n&=\sum_x\sum_{y\in\mathrm{Rot}(Rx)\setminus\mathrm{Rot}(x)}
                                      a(x)\overline{a(y)},\\
Z_n&=\sum_x\sum_{y\notin\mathrm{Rot}(x)\cup\mathrm{Rot}(Rx)}
                                      a(x)\overline{a(y)}.
\end{split}
\tag{4}
$$

Thus |Tr U^n|^2=D_n+R_n+Z_n exactly. In particular D_n is nonnegative. The
other two sums are real because exchanging x and y preserves each class and
conjugates the summand. There is no absolute value inside any of these phase
sums.

## 2. Uniform hypotheses for the all-time estimates

Suppose that for a fixed C>=1,

$$
\max_{x,y}P_{xy}\le C/N,\qquad \|P-J\|_{\mathrm{op}}\le1/2,
\qquad \rho:=\|Q\|_{\mathrm{op}}\le1/2.
\tag{5}
$$

Assume N>=16 C^2. These hypotheses are proved for the actual U_N for all
sufficiently large odd N in the companion kernel/oscillation chain. There
rho_N in fact tends to zero. Constants here do not depend on n or N.

The theorem is

$$
\boxed{\sum_{n\ge1}|D_n-n|\le7C+1+\frac{8C^2}{N},}
\tag{6}
$$

$$
\boxed{\sum_{n\ge1}|R_n|
 \le12C\rho+\frac{8C^2+27C^3+32C^4}{N}.}
\tag{7}
$$

Both series are ordinary absolutely convergent numerical series. The claim
in (6) is about the difference D_n-n, not summability of D_n or n separately.

## 3. The forward class and all periodic corrections

Cyclic rotation preserves a(x), so

$$
D_n=\sum_x d(x)|a(x)|^2,
\qquad n\operatorname{Tr}P^n=\sum_x n|a(x)|^2.
\tag{8}
$$

The difference is supported on periodic words d(x)<n. Fix a proper divisor
d of n. Every word whose period divides d is a repetition, n/d times, of a
word z of length d, with probability product

$$
|a(x)|^2=\left(\prod_{j=0}^{d-1}P_{z_j,z_{j+1}}\right)^{n/d}.
$$

Since each P entry is at most C/N, its sum over all such words is at most

$$
(C/N)^{n-d}\operatorname{Tr}P^d\le C(C/N)^{n-d}.
\tag{9}
$$

The last inequality follows without a spectral estimate: every P^d entry is
at most C/N, because P is stochastic and P^d=P^{d-1}P. Therefore its trace is
at most C. Every proper divisor d is at most n/2, and there are at most n of
them. Overcounting their union by a nonnegative sum is valid. Thus, for n>=2,

$$
0\le n\operatorname{Tr}P^n-D_n\le Cn^2(C/N)^{n/2}.
\tag{10}
$$

At n=1 the difference is zero. Put z=sqrt(C/N)<=1/4. A direct differentiation
of the geometric series gives

$$
\sum_{n\ge2}n^2z^n
=\frac{z(1+z)}{(1-z)^3}-z\le8z^2.
\tag{11}
$$

For example the quotient by z^2 has nonnegative power-series coefficients,
so its maximum for 0<=z<=1/4 is its value 212/27<8 at 1/4. Combining (10)
and (11) bounds the sum of all periodic corrections by 8C^2/N.

Next P is doubly stochastic, hence PJ=JP=J. Let A=P-J. Then
P^n=J+A^n. The normalized constant vector and its orthogonal complement reduce
P, and

$$
\|A\|_{\mathrm{HS}}^2=\|P\|_{\mathrm{HS}}^2-1\le C-1\le C.
\tag{12}
$$

Here sum_xy P_xy^2<=(C/N) sum_xy P_xy=C. For n>=2, finite-dimensional HS
Cauchy--Schwarz and the ideal inequality imply

$$
|\operatorname{Tr}A^n|
\le\|A\|_{\mathrm{HS}}\|A^{n-1}\|_{\mathrm{HS}}
\le C\,2^{-(n-2)}.
\tag{13}
$$

No normality of P is assumed. At n=1, |Tr P-1|<=C+1. Since
sum_{n>=2} n 2^{-(n-2)}=6,

$$
\sum_{n\ge1} n|\operatorname{Tr}P^n-1|\le7C+1.
\tag{14}
$$

Equations (10)--(14) prove (6).

## 4. The reversed class, with two distinct corrections

First include the overlap with the forward class and call that sum

$$
T_n=\sum_x\sum_{y\in\mathrm{Rot}(Rx)}a(x)\overline{a(y)}
   =\sum_x d(x)a(x)\overline{a(Rx)}.
\tag{15}
$$

Without removing duplicate rotations,

$$
n\operatorname{Tr}Q^n
 =\sum_x n a(x)\overline{a(Rx)}.
\tag{16}
$$

This is an exact phase identity because the product of Q entries along x is
precisely a(x) overline{a(Rx)}.

### 4.1 Duplicate rotations

Let S_xy=sqrt(P_xy P_yx), a real nonnegative symmetric matrix. Cauchy--Schwarz
and the unit row and column sums of P give

$$
\sum_y S_{xy}\le
\sqrt{\sum_y P_{xy}}\sqrt{\sum_y P_{yx}}=1,
\qquad \max_{x,y}S_{xy}\le C/N.
\tag{17}
$$

By iteration S^d is substochastic and every entry of S^d is at most C/N.
Thus Tr S^d<=C for all d>=1. The argument of (9), now applied to S, gives

$$
|T_n-n\operatorname{Tr}Q^n|
\le Cn^2(C/N)^{n/2}\quad(n\ge2),
\tag{18}
$$

and zero at n=1. Its all-time sum is at most 8C^2/N. This estimate takes the
absolute value only after the entire class difference has been formed; the
subsequent bound uses absolute values to control the exceptional periodic
words, which are already negligible.

### 4.2 Intersection with the forward class

Two rotation classes either are identical or are disjoint. Therefore the
intersection contributes exactly

$$
I_n:=T_n-R_n=\sum_x d(x)
  1_{\mathrm{Rot}(Rx)=\mathrm{Rot}(x)}|a(x)|^2\ge0.
\tag{19}
$$

For n=1 or 2 every reversal is a rotation, hence R_1=R_2=0 exactly. For n>=3,
if the indicator in (19) is one, x is fixed by at least one of the n dihedral
reflections acting on its positions. A reflection of n cyclic positions has
at most floor(n/2)+1 cycles: it has one fixed point for odd n, and zero or two
fixed points for even n. Thus the number of its fixed words is at most
N^{floor(n/2)+1}. Each |a(x)|^2 is at most (C/N)^n. Since d(x)<=n, the union
bound over the n possible reflections yields

$$
I_n\le n^2 C^n N^{1-\lceil n/2\rceil},\quad n\ge3.
\tag{20}
$$

Set v=C^2/N<=1/4. For odd n=2k+1>=3, the sum of (20) is bounded by
C sum_{k>=1}(2k+1)^2 v^k<=27C v=27C^3/N. Here (2k+1)^2<=9k^2 and
sum_{k>=1}k^2v^k=v(1+v)/(1-v)^3<3v for v<=1/4.
For even n=2k>=4, (11) gives
N sum_{k>=2}4k^2 v^k<=32N v^2=32C^4/N. Consequently

$$
\sum_{n\ge3}I_n\le\frac{27C^3+32C^4}{N}.
\tag{21}
$$

### 4.3 The signed main term

Q is Hermitian and

$$
\|Q\|_{\mathrm{HS}}^2
=\sum_{x,y}P_{xy}P_{yx}\le C.
\tag{22}
$$

Hence for n>=2, |Tr Q^n|<=C rho^{n-2}. In particular

$$
\sum_{n\ge3}n|\operatorname{Tr}Q^n|
\le C\,\frac{\rho(3-2\rho)}{(1-\rho)^2}\le12C\rho,
\quad0\le\rho\le1/2.
\tag{23}
$$

Combine (18), (19), (21), and (23), remembering the exact R_1=R_2=0, to get
(7). This proves the theorem.

## 5. What is established for the original U_N

The kernel and oscillatory matrix chain supplies the same C, (5), and
rho_N=||Q_N||->0 for every sufficiently large odd N. Therefore

$$
\boxed{\sum_{n\ge1}|D_{n,N}-n|=O(1),\qquad
       \sum_{n\ge1}|R_{n,N}|=o(1).}
\tag{24}
$$

For every bounded set of weights w_{n,N}, even depending on N, with
sup_{n,N}|w_{n,N}|<=W, the correction identity is

$$
\left|\frac1{N^2}\sum_n w_{n,N}
 [|\operatorname{Tr}U_N^n|^2-n-Z_{n,N}]\right|=O(WN^{-2}).
\tag{25}
$$

For finite sums (25) is literal. For infinite sums it asserts absolute
convergence of the CORRECTION series, with the same bound. It does not assert
that the separate series with |Tr U_N^n|^2, n, or Z_n converge for every bounded
weight. They do converge separately for the exponential weights in the user
problem.

This establishes the complete linear ramp of the forward rotation class and
removes the entire distinct reversed rotation class at all times. It is a
statement about the original phase products, with no parameter average and
no random replacement. It is not a bound on the nonreversed class Z_{n,N}.

## 6. The remaining pair gap in the new exact decomposition

For the explicit test b_* from the original checkpoint, put
w(u)=|bhat_*(u)|^2. It is supported in [-2,2]. The exact pair identity and (25)
give

$$
\Delta_{2,N}(b_*)
=\frac1{N^2}\sum_{1\le n<2N}w(n/N)
 [Z_{n,N}+n-\min(n,N)]+O(N^{-2}).
\tag{26}
$$

Consequently the presently unproved pair statement becomes

$$
\boxed{\frac1{N^2}\sum_{1\le n<2N}w(n/N)Z_{n,N}
       \longrightarrow-\int_1^2 (u-1)w(u)\,du.}
\tag{27}
$$

The integral is strictly negative after the displayed minus sign: bhat_* is
a positive convolution on (-2,2), so w>0 there. In particular it would be
wrong to aim to show that EVERY remaining off-diagonal contribution is o(1)
in the normalized functional. Above the Heisenberg threshold the required
aggregate has a nonzero negative limit. The exact finite dimension must be
visible in its cancellations.

For a band supported in (-1,1), the analogous target is zero; it too is
unproved for this family. All fixed orders k>=3 remain unproved as well.
No lower bound contradicting H_diag on an infinite subsequence has been
established in this note.
