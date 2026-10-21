> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_quantitative_pressure.md`. Embedded SHA256: `d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2`.
> [Thematic guide](../../topics/classical_trace.md).

# A quantitative pressure gap at the exact parameter

## Status and inputs

This note proves a numerical lower bound for the pressure gap of the
**original** classical map at `tau=10^-80`. It does not prove `H_diag`.
The new estimate concerns an actual invariant of the original map, rather
than a comparison family or a conditional universality statement.

The main input is the independently audited, frozen file
`arithmetic_pressure_analytic_potential.md`, SHA-256
`44da5eefab7cce7d7eb222fa54f027eec8a1a545b8ca0c4fd3fcf1fc7520637f`.
In its notation,

$$
 X=(a_p,-a_q)/(2\pi),\quad \Xi_s=S\Phi_s,\quad
 S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\quad
 \lambda=3+2\sqrt2,\quad h_0=\log\lambda.
$$

Here `Phi_s` is the flow of `X`, and the original map is
`Psi=Xi_tau^(-1)`. The frozen input supplies a holomorphic family

$$
 \psi_s\in C^{1/2}(\mathbb T^2;\mathbb C),\qquad |s|<10^{-16},
$$

with

$$
 \psi_0=h_0,\qquad
 \|\psi_s-h_0\|_{C^{1/2}}\le10^{11}|s|,\qquad
 \psi'_0=\xi=\frac{a_{pp}-2a_{qq}}{4\pi\sqrt2}.        \tag{0.1}
$$

For real `s`, `Xi_s H_s=H_s S`, and `psi_s` is cohomologous to
`log J^u_(Xi_s) o H_s`. The Holder metric is the eigen-coordinate
metric specified in that input. All bounds below allow the stated fixed
change to the standard torus metric.

The geometric-pressure identity used below is proved, with its
suspension hypotheses checked, in `fermionic_pressure_transfer.md`,
SHA-256
`90ebc84c3c9fb7c049a1a9d11e0d5dcb72c4fc89b362da3f848521a7bca79756`.
Its published input is Bowen--Ruelle, *The Ergodic Theory of Axiom A
Flows*, Invent. Math. **29** (1975), 181--202, Proposition 4.4(b),
pp. 189--190, together with the unit-roof suspension argument in that
file. The primary paper is available at
<https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B42%5D.pdf>.

The only published coding input is made explicit in Section 1. All
operator constants, the analytic pressure radius, and the pressure
remainder are proved in this note.

## 1. A concrete twelve-edge coding of the fixed cat map

### 1.1. Geometry and the exact incidence matrix

Use stable-horizontal and unstable-vertical coordinates

$$
 B(q,p)=(q-\sqrt2p,q+\sqrt2p).
$$

The lattice `B Z^2` has basis

$$
 e=(1,1),\qquad f=(-\sqrt2,\sqrt2),
$$

and `B S B^(-1)=diag(lambda^(-1),lambda)`. The construction of
Siemaszko--Wojtkowski, *Counting Berg partitions*, Nonlinearity
**24** (2011), 2383--2403, arXiv:1007.3984, Section 2 and Theorems
4.1--4.2, applies to this basis. Its primary full text is
<https://arxiv.org/pdf/1007.3984> (construction on pp. 2--3, theorems
and their positive-eigenvalue application on pp. 8--11 of the preprint).

For clarity, the hypotheses and conclusions needed here are these.
For a lattice basis `(v,p),(-u,q)` in the first and second quadrants,
the construction gives two rectangular tiles of side lengths `(u,p)`
and `(v,q)`. When both eigenvalues of the diagonal toral map are
positive, placing an intersection of the horizontal and vertical
spines at a fixed point makes this a Berg partition. Its connectivity
matrix is the transpose of the matrix representing the map in that
lattice basis. In the present case all four side lengths are positive,
the eigendirections are irrational, and the origin is a fixed point.
Consequently the two tiles have side lengths

$$
 (w_1,h_1)=(\sqrt2,1),\qquad
 (w_2,h_2)=(1,\sqrt2),
$$

and the exact connectivity matrix is

$$
 C=S^T=\begin{pmatrix}3&2\\4&3\end{pmatrix}.           \tag{1.1}
$$

We use **edges**, not just the two vertices: for each `i,j`, there
are `C_ij` separate edges from vertex `i` to vertex `j`. The alphabet
therefore has twelve edges. Each edge records one connected strip
of `S R_i` crossing one lattice translate of `R_j`.

Here is why the geometric crossing information gives the coding
properties used later. The Berg conditions are
`S J^s subset J^s` and `S J^u superset J^u`. Thus the preimage of
an old vertical boundary is an old vertical boundary, and an image
strip has no vertical boundary cutting its interior. Every crossing
is a full-height strip in its destination rectangle. Its preimage
is a full-width horizontal strip in its source rectangle. In
particular every admissible concatenation of edges is realizable,
by successively intersecting full crossing strips.

### 1.2. Coding diameter and finite fibers

Let `Sigma` be the two-sided edge shift and `sigma` its left shift.
For an edge sequence, intersect its finite past and future strip
conditions. A future word of `n` edges cuts the unstable-coordinate
length to at most `sqrt(2) lambda^(-n)`. A past word of `n` edges
cuts the stable-coordinate length by the same bound. These are
closed, nonempty, nested rectangles; their diameters tend to zero.
They define a continuous map

$$
 \pi:\Sigma\longrightarrow\mathbb T^2,
 \qquad \pi\sigma=S\pi.                              \tag{1.2}
$$

Generic points off all iterates of the spines have their unique edge
itinerary. They are dense. Approximating an arbitrary point by such
points and taking a compactness subsequence of their codes proves
surjectivity, including points on boundaries.

The input eigen coordinates are the two rows of `B`, in reverse
order, divided by `sqrt(3)`. Thus, if two codes agree at edges
`-n,...,n`, the preceding rectangle bound implies, with ample room,

$$
 d(\pi x,\pi y)\le10\lambda^{-n},\qquad n\ge0.        \tag{1.3}
$$

The harmless constant ten also covers the endpoints and indexing
conventions for the first edge. For example, the direct centered
rectangle computation gives the smaller coordinate bound
`sqrt(2/3) lambda^(-n)` when both past and future conditions have
length `n`.

One can also verify that every fiber of `pi` has at most four elements.
For sufficiently long centered words their small cylinder rectangles
embed in the torus, have positive side lengths, and distinct such
cylinders have disjoint interiors. For a code of a point `x`, each
of its nested rectangles contains at least one open coordinate
quadrant germ with vertex `x`. The sets of admissible quadrant germs
are nested nonempty subsets of a set of four elements, so one germ
belongs to all of them. Two different codes cannot admit the same
germ: once a word includes an edge at which they differ, that germ
would lie inside two disjoint cylinder interiors. This proves the
fiber bound. No entropy formula for finite extensions is needed in
the subsequent proof of pressure equality.

### 1.3. The Parry measure pushes forward to area

The right and left Perron vectors of `C` can be chosen as

$$
 r=(1,\sqrt2),\qquad l=(\sqrt2,1).
$$

The stationary vertex probabilities are both `1/2`. The probability
of an individual edge `i -> j`, conditional on its source vertex,
is `r_j/(lambda r_i)`. The area of a geometric future cylinder with
initial vertex `i` and final vertex `j` after `n` edges is exactly

$$
 \frac{w_i h_j}{2\sqrt2\,\lambda^n}.
$$

This equals its Markov probability, since `r_i=h_i` and
`w_i h_i/(2sqrt(2))=1/2`. Tile boundaries have zero area. The same
equality for arbitrary finite two-sided words follows by translating
the word with the invariant map. Approximating continuous functions
by their values on shrinking cylinders now proves

$$
 \pi_*\mu=dx,                                        \tag{1.4}
$$

where `mu` is this stationary two-sided edge Markov measure and `dx`
is normalized torus area. This is a direct area computation, not an
appeal to a qualitative maximal-entropy theorem.

## 2. A bounded, parameter-independent one-sided cohomology

Set

$$
 a_0=\lambda^{-1/2}=\sqrt2-1<0.415,\qquad \theta=2/3.
$$

For a two-sided function `F`, write

$$
 V(F)=\sup_{n\ge0}a_0^{-n}\operatorname{var}_{[-n,n]}F,
 \qquad A(F)=\|F\|_\infty+V(F).
$$

By (1.3), composition with `pi` maps a torus `C^(1/2)` function
into this space, with

$$
 A(f\circ\pi)\le5\|f\|_{C^{1/2}}.                   \tag{2.1}
$$

For each initial vertex choose once and for all one of its loop edges.
Given `x`, let `bar x` have the same nonnegative edges as `x` and
the constant chosen loop as its negative past. Define the bounded
linear operator

$$
 u_F(x)=\sum_{n\ge0}
       \bigl(F(\sigma^n x)-F(\sigma^n\bar x)\bigr).
$$

The two arguments in the summand agree in the centered block of
radius `n`, so the series converges uniformly and
`||u_F||_infty <= V(F)/(1-a_0)`. Moreover

$$
 F^+=F-u_F+u_F\circ\sigma                            \tag{2.2}
$$

depends only on nonnegative edges. To check this last point without
formal rearrangement of divergent series, first truncate the definition
of `u_F`, telescope, and let the truncation tend to infinity. The
uniformly convergent resulting formula is

$$
 F^+(x)=F(\bar x)+\sum_{n\ge0}
 \bigl(F(\sigma^{n+1}\bar x)
       -F(\sigma^n\overline{\sigma x})\bigr).          \tag{2.3}
$$

The remaining finite-telescoping endpoint tends to zero by the same
centered-variation bound. Formula (2.3) proves future dependence and
`||F^+||_infty <= ||F||_infty+V(F)/(1-a_0)`.

Here are explicit seminorm bounds. Let `var_k^+` denote variation
when the first `k>=1` edges agree. For `k>=2` put
`J=floor((k-2)/2)`. In (2.3), the first term varies by at most
`V a_0^(k-1)`. For the term indexed by `n<=k-2`, either compare its
two components separately, using the common future, or use the
individual bound on that term. Its variation is at most
`2V min(a_0^n,a_0^(k-n-2))`. The remaining terms have variation at
most `2V a_0^n`. Consequently

$$
 \operatorname{var}_k^+F^+
 \le V a_0^{k-1}
   +\frac{2V}{1-a_0}
      \left(a_0^{k-2-J}+a_0^{J+1}\right)
 \le16 V\theta^k.                                   \tag{2.4}
$$

The last inequality follows separately for even and odd `k`, using
`sqrt(a_0)<theta`; the resulting numerical coefficients are below
15. For `k=1`, twice the supremum bound gives a smaller bound than
`8 A(F) theta`. Thus the norm

$$
 \|g\|_\theta=\|g\|_\infty+
    \sup_{k\ge1}\theta^{-k}\operatorname{var}_k^+g
$$

satisfies the convenient uniform estimate

$$
 \boxed{\|F^+\|_\theta\le32 A(F).}                   \tag{2.5}
$$

This map is bounded and linear and preserves constants. It therefore
preserves Banach-valued holomorphy in the scalar parameter. In
particular, with `d_s=psi_s-h_0` and `F_s=d_s o pi`, for every fixed
`0<=t<=1` the one-sided potential

$$
 v_t(s)=-t F_s^+
$$

is holomorphic on the original input disk and obeys

$$
 \boxed{\|v_t(s)\|_\theta\le10^{14}|s|.}             \tag{2.6}
$$

The inequalities (0.1), (2.1), and (2.5) actually give a smaller
constant than the displayed one.

## 3. An elementary quantitative spectral gap at zero potential

Use the future edge space, with the marginal of `mu`, again denoted
by `mu`. For `x` with initial vertex `i`, define

$$
 (\mathcal L_0g)(x)=
 \sum_{e:j\to i}\frac{l_j}{\lambda l_i}\,g(ex).        \tag{3.1}
$$

The sum is over individual incoming edges. These weights sum to one.
This is the conditional backward Markov operator. In particular

$$
 \mathcal L_0 1=1,\quad \mu\mathcal L_0=\mu,\quad
 \Pi g=(\mu g)1,\quad
 \|\mathcal L_0\|_\theta\le1.                        \tag{3.2}
$$

For the last inequality, if the first `k>=1` edges of two arguments
agree, their incoming edges can be paired with exactly equal weights.
The prepended arguments then agree for `k+1` edges. Thus the
seminorm is multiplied by at most `theta`, and the supremum norm
does not increase.

The backward **vertex** transition matrix is exactly

$$
 P=\begin{pmatrix}
 3/\lambda&2\sqrt2/\lambda\\
 2\sqrt2/\lambda&3/\lambda
 \end{pmatrix}.                                      \tag{3.3}
$$

Its stationary probabilities are `(1/2,1/2)` and its other eigenvalue
is

$$
 q_0=\lambda^{-2}<0.03.
$$

Its distance in total variation from stationarity, starting at either
vertex after `j` steps, is exactly `q_0^j/2`.

For completeness, approximate a Holder function `g` by a function
`g_k` depending only on its first `k` edges, choosing one admissible
completion in each cylinder. Then

$$
 \|g-g_k\|_\infty\le |g|_\theta\theta^k,
 \qquad \|g_k\|_\infty\le\|g\|_\infty.
$$

For `n>=k`, the distribution of the initial `k` edges after `n`
backward steps is obtained from the vertex distribution after
`n-k` steps by a Markov kernel. Total variation cannot increase
under that kernel. Hence

$$
 \|\mathcal L_0^n g-\mu g\|_\infty
 \le2|g|_\theta\theta^k
       +q_0^{n-k}\|g\|_\infty.                       \tag{3.4}
$$

Also `|L_0^n g|_theta <= theta^n |g|_theta`. Choose
`k=floor(n/2)` for `n>=2` and handle `n=0,1` directly from (3.2).
Since `sqrt(theta)<5/6` and `sqrt(q_0)<5/6`, this proves

$$
 \boxed{\|\mathcal L_0^n-\Pi\|_\theta
           \le6(5/6)^n,\qquad n\ge0.}               \tag{3.5}
$$

This proof includes variation in the initial vertex, which is not
controlled by the tail seminorm alone.

## 4. A numerical holomorphic pressure disk

Let

$$
 R_p=10^{-24},\qquad
 \mathcal L_vg=\mathcal L_0(e^v g).
$$

The norm `||.||_theta` is a Banach algebra norm, as follows directly
from the product variation inequality. Consequently

$$
 \|\mathcal L_v-\mathcal L_0\|
 \le e^{\|v\|_\theta}-1\le2\|v\|_\theta
$$

when `||v||_theta<=1`. For `v=v_t(s)` and `|s|<2 R_p`, this gives

$$
 \|E\|:=\|\mathcal L_v-\mathcal L_0\|<4\cdot10^{-10}.
                                                               \tag{4.1}
$$

Equation (3.5) gives a resolvent formula, proved by multiplying its
convergent series by `z-L_0`:

$$
 (z-\mathcal L_0)^{-1}
 =\frac{\Pi}{z-1}
  +\sum_{n\ge0}z^{-n-1}(\mathcal L_0^n-\Pi),
 \qquad |z|>5/6,\quad z\ne1.
$$

In particular

$$
 \|(z-\mathcal L_0)^{-1}\|
 \le\frac1{|z-1|}+\frac6{|z|-5/6}.                   \tag{4.2}
$$

On the circle `Gamma_1: |z-1|=1/24` the bound is `72`. On
`Gamma_0: |z|=9/10` it is `100`. Moreover it is at most `114`
throughout the region `|z|>=9/10, |z-1|>=1/24`. The Neumann
resolvent formula with (4.1) therefore proves that the perturbed
spectrum lies in the union of the two disks bounded by these
circles, and that both circles stay in the resolvent set.

Let `Pi_v` be the resolvent integral over `Gamma_1`. The resolvent
identity, integrated over two nested circles, gives
`Pi_v^2=Pi_v` and commutation with `L_v`. The difference from the
unperturbed rank-one projection satisfies

$$
 \|\Pi_v-\Pi\|
 \le\frac1{24}\frac{72^2\|E\|}{1-72\|E\|}
 <10^{-6}.                                          \tag{4.3}
$$

Two projections at distance less than one have equal finite rank:
restriction of either to the range of the other is injective.
Thus `Pi_v` has rank one. With `h_v=Pi_v 1`, the number

$$
 z_t(s)=\frac{\mu(\mathcal L_v h_v)}{\mu h_v}
$$

is holomorphic, is the unique eigenvalue in the second disk, and
satisfies `|z_t(s)-1|<1/24`. The denominator is nonzero by (4.3).
The holomorphy follows directly from the Neumann resolvent formula,
its contour integral, and this displayed quotient. No qualitative
perturbation theorem with unspecified constants is being used.

Choose the logarithm branch equal to zero at `s=0` and put

$$
 q_t(s)=\log z_t(s).
$$

It is holomorphic on `|s|<2R_p`, uniformly for the indicated fixed
values of `t`, and

$$
 \boxed{|q_t(s)|<1/12\quad (|s|\le R_p).}             \tag{4.4}
$$

For real `s`, the operator and its projection are real. Equation
(4.3) gives `h_v>0` and `mu h_v>0`, while the eigenvalue is real
and positive. The contour integral over `Gamma_0` bounds the
remaining powers by a constant times `(9/10)^n`. Therefore

$$
 \lim_{n\to\infty}\frac1n
 \log\mu(\mathcal L_v^n1)=\log z_t(s)                \tag{4.5}
$$

for real `s`. Positivity and the nonzero coefficient of the rank-one
term are both verified here; a possible cancellation of the leading
eigenvector does not enter this limit.

## 5. Identifying this eigenvalue with torus pressure

This identification can be proved directly with linear Bowen balls.
It avoids any need for a quantitative theorem on entropy of an
extension or for a smooth structural conjugacy.

Use the input eigen coordinates, so the map is
`D=diag(lambda,lambda^(-1))`, on a fixed lattice. Choose a fixed
sufficiently small `epsilon>0`, for example `10^-3`. A nonzero
lattice vector has maximum norm at least `1/2`: its preimage is a
nonzero integer vector and the inverse coordinate matrix has norm
less than two. Short differences `z_j` of two orbits in an
`n`-step Bowen ball have size below `epsilon`. The possible lattice
jump in `z_(j+1)-D z_j` has norm below `(1+lambda)epsilon<1/2`;
hence it vanishes. Thus the Bowen ball is exactly the projected
rectangle

$$
 |u|<\epsilon\lambda^{-(n-1)},\qquad |v|<\epsilon.
$$

Its normalized area is `c_epsilon lambda^(-n)`, with
`c_epsilon>0` independent of its center and `n`.

For a real `C^(1/2)` potential `f`, the oscillation of its Birkhoff
sum on that ball is bounded independently of `n`. Indeed at time
`j` the orbit difference is at most
`epsilon(lambda^(-j)+lambda^(-(n-1-j)))`, and hence the sum of
the `1/2` powers is at most

$$
 \frac{2\epsilon^{1/2}}{1-\lambda^{-1/2}}.
$$

An `epsilon`-separated set has disjoint Bowen balls of radius
`epsilon/2`; a maximal such set has Bowen balls of radius `epsilon`
covering the torus. Combining their exact volumes and the preceding
bounded distortion proves, for positive constants independent of `n`,

$$
 c_f\lambda^n\int e^{\sum_{j<n}f(S^j x)}dx
 \le Z_n(f,\epsilon)
 \le C_f\lambda^n\int e^{\sum_{j<n}f(S^j x)}dx.        \tag{5.1}
$$

Here `Z_n` is the supremum of the weighted sums over separated sets.
For the lower inequality any maximal separated set suffices; for
the upper inequality use disjoint balls for each separated set.
Taking logarithms, dividing by `n`, and then using the definition
of pressure as the small-radius limit proves

$$
 P_S(f)=h_0+limsup_{n\to\infty}\frac1n
                 \log\int e^{\sum_{j<n}f(S^j x)}dx.  \tag{5.2}
$$

By (1.4), the integral equals the corresponding integral on the
two-sided shift. Replacing `f o pi` by the cohomologous one-sided
potential changes a Birkhoff sum by the bounded endpoint term
`u_F-u_F o sigma^n`; for real potentials this does not change the
logarithmic growth rate. Finally the Markov identity

$$
 \mu(\mathcal L_v^n1)=
 \int\exp\left(\sum_{j<n}v\circ\sigma^j\right)d\mu
$$

follows from (3.1) and stationarity, or by successively conditioning
on the prepended edges. Equations (4.5) and (5.2) therefore give
the exact equality

$$
 \boxed{P_S(-t\psi_s)=(1-t)h_0+q_t(s)}                \tag{5.3}
$$

for real `s` in the displayed parameter disk. The construction in
Section 4 is its explicitly bounded holomorphic extension.

## 6. Pressure derivatives and the quadratic coefficient

We record the derivative computation, including the variance term.
For a general analytic curve of one-sided potentials `v(s)` with
`v(0)=0`, put `w=v'(0)` and normalize the corresponding eigenfunction
by `mu h(s)=1`. Differentiate
`L_(v(s)) h(s)=z(s) h(s)` at zero. Applying `mu` gives
`z'(0)=mu w`; on the mean-zero subspace, (3.5) gives the convergent
solution

$$
 h'(0)=\sum_{n\ge1}\mathcal L_0^n(w-\mu w).
$$

Differentiating a second time, applying `mu`, and subtracting
`z'(0)^2` for the logarithm yields

$$
 (\log z)''(0)=\mu v''(0)
  +\mu(w-\mu w)^2
  +2\sum_{n\ge1}\mu\bigl((w-\mu w)
                  \mathcal L_0^n(w-\mu w)\bigr).     \tag{6.1}
$$

The series converges absolutely by (3.5). Conditional expectation
gives
`mu(g L_0^n f)=mu(f (g o sigma^n))`, so the final two terms are
the asymptotic variance of `w`. This also follows by expanding the
square of its length-`n` Birkhoff sum and dividing by `n`.

Asymptotic variance is unchanged by the bounded coboundary (2.2).
Indeed the two Birkhoff sums differ by a uniformly bounded endpoint
term. One of their second moments is `O(n)` by (3.5); the
Cauchy--Schwarz inequality then shows that their second moments,
divided by `n`, differ by `O(n^(-1/2))`. The same reasoning also
shows equality of their means. Using (1.4) and (0.1), let

$$
 \sigma^2(\xi)=\lim_{n\to\infty}\frac1n
        \int\left(\sum_{j<n}\xi(S^j x)\right)^2dx.   \tag{6.2}
$$

The mean of `xi` is zero, since it is a linear combination of second
derivatives of a periodic function. For `v_t(s)=-t F_s^+`, equation
(6.1) gives

$$
 q_t'(0)=0,\qquad
 q_t''(0)=-t\int\psi''_0\,dx+t^2\sigma^2(\xi).       \tag{6.3}
$$

For real `|s|<2R_p`, the map `Xi_s` is a smooth area-preserving
Anosov map, topologically conjugate to `S` by the input construction.
For example the input derivative cocycle is within `10^-6` of the
diagonal hyperbolic matrix, and its invariant unstable multiplier
exceeds five; the inverse cone gives the stable direction. The
Hamiltonian flow preserves area exactly. Its unit-roof suspension
has the entire compact mapping torus as a transitive basic
hyperbolic attractor, with dense periodic orbits and no flow fixed
points. Thus the geometric-pressure-zero identity from the precise
Bowen--Ruelle input specified above applies. Conjugacy and the exact
metric coboundary in (0.1) give

$$
 P_S(-\psi_s)=0.
$$

Conjugacy preserves pressure by uniform continuity of it and its
inverse in the separated-set definition; a continuous coboundary
changes Birkhoff sums by a bounded endpoint term. These facts need
no differentiability of `H_s`.

Equation (5.3) now gives `q_1(s)=0` on a real interval and hence
identically on its complex disk. Therefore (6.3), with `t=1`, gives
`integral psi''_0 dx=sigma^2(xi)`. At `t=1/2` we obtain

$$
 q_{1/2}''(0)=-\frac14\sigma^2(\xi).                 \tag{6.4}
$$

Define

$$
 \Delta(s)=\frac{h_0}{2}
       -P_{\Xi_s}\left(-\frac12\log J^u_{\Xi_s}\right)
       =-q_{1/2}(s).
$$

Equations (4.4), (6.3), and (6.4), followed by the Cauchy coefficient
bound on the circle of radius `R_p`, prove

$$
 \boxed{\left|\Delta(s)-\frac{\sigma^2(\xi)}8s^2\right|
       \le10^{72}|s|^3,\qquad |s|\le R_p/2.}         \tag{6.5}
$$

More explicitly, the coefficient bounds from (4.4) sum to
`(1/12) R_p^(-3)|s|^3/(1-|s|/R_p)`, which is at most
`(1/6)10^72|s|^3`. The weaker displayed constant is convenient.

## 7. A short exact Fourier lower bound for the coefficient

No numerical Fourier experiment is required for a positive numerical
coefficient. The ordinary symbol in the input has support
`|k|<=9, |l|<=1`, and

$$
 \widehat\xi(k,l)=\frac\pi{\sqrt2}(2k^2-l^2)\widehat a(k,l).
                                                               \tag{7.1}
$$

For any real, mean-zero finite Fourier polynomial, summing its
correlations under `S` and grouping by orbits of `S^T` gives

$$
 \sigma^2(\xi)
 =\sum_{n\in\mathbb Z}\int\xi(x)\xi(S^n x)dx
 =\sum_{\mathcal O}
      \left|\sum_{v\in\mathcal O}\widehat\xi(v)\right|^2.
                                                               \tag{7.2}
$$

All sums here are finite after the support restrictions are imposed.
Indeed a nonzero vector cannot be periodic under `S^T`; each pair
of support vectors can be related by at most one iterate. Fourier
orthogonality first gives the correlation formula; for each orbit,
the double sum of coefficient products is the square displayed in
(7.2). Expanding the Birkhoff square in (6.2) proves that the sum of
these correlations is exactly the variance in (6.2).

The quadratic form `2k^2-l^2` is invariant under
`S^T(k,l)=(3k+2l,4k+3l)`. The orbits of `(7,0)` and `(-7,0)` each
meet the permitted support at just that one point: the equation
`2k^2-l^2=98` with `|l|<=1` admits only `(+/-7,0)`, and these two
vectors cannot be on the same orbit, since all eigenvalues of every
integer power of `S^T` are positive.

To compute the coefficient directly, use

$$
 r(q)=1+\cos(2\pi q)-\cos(14\pi q)
             -\tfrac12\cos(12\pi q)-\tfrac12\cos(16\pi q).
$$

Its Fourier coefficients at 6 and 8 coincide, so that of
`r(q) sin(2pi q)` at 7 is zero. The corrected `p`-dependent term
has only `l=+/-1`, and hence does not enter. It follows that

$$
 \widehat a(7,0)=\frac12-\frac1{20}=\frac9{20},\qquad
 \widehat\xi(7,0)=\frac{441\pi}{10\sqrt2}.
$$

Keeping only these two nonnegative orbit squares in (7.2) proves

$$
 \boxed{\sigma^2(\xi)\ge\frac{194481\pi^2}{100}.}     \tag{7.3}
$$

Thus `sigma^2(xi)/8>2187`, using just `pi>3`.
At the exact fixed parameter `tau=10^-80`, the error in (6.5) is
at most `10^-8 tau^2`. In particular we have the fully numerical
bound

$$
 \boxed{\Delta(\tau)\ge2000\tau^2=2\cdot10^{-157}.}   \tag{7.4}
$$

The full Fourier computation can refine the quadratic coefficient;
it is not required for (7.4). The proof of this numerical lower bound
is complete with only the two explicitly evaluated coefficients.

## 8. Equality with the original inverse-map pressure gap

The original classical map is `Psi=Xi_tau^(-1)`. For an
area-preserving two-dimensional Anosov map `F`, let `alpha(x)` be
the angle between its unit unstable and stable vectors. The
determinant identity is

$$
 J_F^u(x)J_F^s(x)\sin\alpha(Fx)=\sin\alpha(x).
$$

Since the unstable direction of `F^(-1)` is the stable direction
of `F`, this gives

$$
 \log J_{F^{-1}}^u(Fx)
 =\log J_F^u(x)+\log\sin\alpha(Fx)-\log\sin\alpha(x).
$$

The angle is bounded away from zero. For every invariant measure,
the two unstable logarithms therefore have equal integrals. Entropy
of an invertible map equals that of its inverse: the finite forward
and backward joined partitions differ by an invariant translate.
The variational principle then proves equality of the two geometric
pressures at any real coefficient. Consequently, with the original
notation `P_*` from `fermionic_pressure_transfer.md`,

$$
 \boxed{\frac12\log\lambda-P_*
           =\Delta(\tau)\ge2000\tau^2.}              \tag{8.1}
$$

The parameter was not changed with `N`, and no averaging was used.

## 9. What this does and does not resolve

The frozen actual quantum pressure transfer, including its Weyl-twisted
version in `fermionic_twisted_pressure.md`, SHA-256
`9bfc9b4a27e8cd7d23bc1693d439f7cb0be31321fbe1947875d9bb8271649bd5`,
now permits the explicit exponent choice `eta=1000 tau^2`.
Thus it gives constants `C,N_0`, independent of `m,a,b`, for which

$$
 \sup_{a,b}|\operatorname{Tr}(T_N(a,b)U_N^m)|
 \le C\exp\bigl((\tfrac12\log\lambda-1000\tau^2)m\bigr)
          +2q_*^m                                  \tag{9.1}
$$

for every `m>=1` and every odd `N>=N_0`. This section uses that
previously proved quantum theorem as an identified input; (6.5)
and (8.1) do not depend on it.

The multiplicative constant and the common quantum threshold are
still not evaluated numerically. The new numerical quantity is the
strict exponent gap, which previously had no explicit lower bound.
As in the prior pressure transfer, applying (9.1) at Pell return
times yields a positive, now explicitly selectable polynomial
suppression exponent.

This estimate continues to grow exponentially in time. At times of
order `N`, it does not control the required signed pair sum or the
higher factorial sums. In particular no conclusion about `H_diag`
is inferred from (9.1). The first missing estimate remains a
Heisenberg-time cancellation in the complete weighted off-diagonal
orbit sum; the bounded-frequency test `b_*` already requires such a
new estimate. A numerical pressure gap supplies an actual stronger
input to that problem but does not replace it.
