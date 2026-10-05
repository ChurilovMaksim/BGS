# Growing neutral degree: exact evaluation cost and the actual logarithmic window

**Claim ID: BGS-FLOW-020. Status: project proof with independent internal review of the new implications.**
5 October 2026. Base: `9555cd19dbf7cac335320dc231f2a7b7bb71954f`.
The original odd-dimensional operator and fixed coupling are unchanged.
This continuation makes the projection estimate quantitative in degree;
it does not prove the complete actual local statistic or BGS.
Complex Hermite/Mehler identities and Ehrenfest packet methods are prior
or standard mechanisms, not world-priority claims.

## 1. Exact finite-degree theorem

Use the full normalized unitary heat semigroup of FLOW-015 and the
neutral span $\mathcal H_{Q,N}$ and Haar projection $\mathsf P_{Q,N}$ of
[FLOW-019](fixed_degree_heat_projection.md). Let $Q\ge0$ and $N\ge\max(3,2Q)$.
For variance $v>0$ define the complex Wick polynomial

$$
H^{[v]}_{a,b}(z)=\sum_{r=0}^{\min(a,b)}
(-v)^r r!\binom ar\binom br z^{a-r}\bar z^{b-r}.
\tag{G1}
$$

For finite nonnegative multiplicity vectors $\boldsymbol a,\boldsymbol b$,
put $q(\boldsymbol a)=\sum_{m\ge1}ma_m$, and index
$q(\boldsymbol a)=q(\boldsymbol b)\le Q$. Define

$$
E_{\boldsymbol a,\boldsymbol b}(U)=
\prod_{m=1}^Q\frac{H^{[m]}_{a_m,b_m}(p_m(U))}
{\sqrt{m^{a_m+b_m}a_m!b_m!}},\qquad
\mathcal K_Q(A)=\sum_{q(\boldsymbol a)=q(\boldsymbol b)\le Q}
|E_{\boldsymbol a,\boldsymbol b}(A)|^2.
\tag{G2}
$$

Empty products equal one. These $E$ form an **exact** orthonormal basis
of $\mathcal H_{Q,N}$. Thus point evaluation on the entire span has
norm $\sqrt{\mathcal K_Q(A)}$, and on its mean-zero part has norm
$\sqrt{\mathcal K_Q(A)-1}$.

For $F\in L^2({\rm Haar})$, $b=\mathbb E_{\rm Haar}F$, and every $t\ge0$,

$$
|P_t\mathsf P_QF(A)-b|
\le\sqrt{\mathcal K_Q(A)-1}\,\|F-b\|_2,
\tag{G3}
$$

$$
|(P_t-I)\mathsf P_QF(A)|
\le\min(2Q^2t,1)\sqrt{\mathcal K_Q(A)-1}\,\|F-b\|_2.
\tag{G4}
$$

At $Q=0$ both left sides vanish. For every $s>0$ one has the computable bound

$$
\log\mathcal K_Q(A)\le 2sQ+\frac{\pi^2}{12s}
+2\sum_{m=1}^Q\frac{e^{-sm}}{1+e^{-sm}}\frac{|p_m(A)|^2}{m}.
\tag{G5}
$$

All statements permit $Q=Q_N$ throughout the stable range. They involve
the actual initial traces, not independently Gaussian trace samples.

## 2. Orthogonality, completeness and the Mehler dictionary

The generating function of G1 is
$\exp(uz+v\bar z-muv)$ when the variance is $m$.
For a centered complex Gaussian $Z$ with $\mathbb E|Z|^2=m$,
integrating two such generating functions gives
$\exp(m u\bar u'+m v\bar v')$. Comparing coefficients yields

$$
\mathbb E H^{[m]}_{a,b}(Z)\overline{H^{[m]}_{c,d}(Z)}
=\mathbf1_{a=c,b=d}\,m^{a+b}a!b!.
\tag{G6}
$$

For products in G2, both weighted degrees of the Gram integrand are at
most $2Q$. Diaconis--Evans Theorem 2.1(a) therefore makes G6 exact for
Haar traces whenever $2Q\le N$. Wick subtraction lowers both weighted
degrees by the same amount, so the transformation from sorted trace
words is triangular with nonzero diagonal. It preserves the neutral
span and proves the asserted orthonormal basis. No growing-degree CLT
is used. Cauchy--Schwarz, with equality for the finite reproducing
vector, proves the two evaluation norms.

For clarity the particular Mehler identity used here is

$$
\sum_{a,b\ge0}\frac{r^{a+b}|H^{[m]}_{a,b}(z)|^2}
{m^{a+b}a!b!}
=\frac1{1-r^2}\exp\left(\frac{2r|z|^2}{m(1+r)}\right),
\quad 0<r<1.
\tag{G7}
$$

It also has a direct Gaussian derivation. The Ornstein--Uhlenbeck
transition $z\mapsto rz+\sqrt{1-r^2}Z$ has kernel, relative to the
stationary complex Gaussian measure,

$$
J_r(z,w)=\frac1{1-r^2}
\exp\left(\frac{2r\Re(z\bar w)-r^2(|z|^2+|w|^2)}
{m(1-r^2)}\right).
$$

The generating function shows that its eigenvalue on $H_{a,b}$ is
$r^{a+b}$. Gaussian polynomials are complete: orthogonality to all of
them makes the entire Laplace transform of the integrable Gaussian-weighted
function zero, hence its Fourier transform zero. Cauchy--Schwarz with
the Gaussian weight justifies that entire transform and its derivatives.
For each $z$, $J_{\sqrt r}(z,\cdot)\in L^2$; Parseval and its Gaussian
convolution square give G7 as $J_r(z,z)$. This argument supplies all
convergence needed in the stated positive-real range.

The known source is Ghanmi, arXiv:1707.06969v1, (2.4), Theorem 4.1
and (4.5), printed pp.2,4. His normalization has
$H^{[m]}_{a,b}=m^{a+b}H^{1/m}_{a,b}$; set his $u=v=rm$ in (4.5).
The admissibility condition becomes $r^2<1$. The
[source check](../literature/growing_degree_sources_20261005.md)
also retains the prior stable Haar locator.

Each neutral term of degree $q\le Q$ has weight $e^{-2sq}$.
Discarding the neutrality restriction in a nonnegative sum and applying
G7 at $r_m=e^{-sm}$ gives

$$
\mathcal K_Q(A)\le e^{2sQ}
\prod_{m=1}^Q(1-e^{-2sm})^{-1}
\exp\left(2\sum_{m=1}^Q
\frac{e^{-sm}}{1+e^{-sm}}\frac{|p_m(A)|^2}{m}\right).
$$

Finally
$\sum_{m\ge1}-\log(1-e^{-2sm})
=\sum_{k\ge1}[k(e^{2sk}-1)]^{-1}
\le\pi^2/(12s)$, proving G5. All summands are nonnegative,
so the exchanges require only monotone convergence.

## 3. A degree-uniform heat bound without a large Gram-matrix norm

Choose a Hermitian Hilbert--Schmidt orthonormal basis $X_a$ of $N$ by
$N$ matrices. The diagonal units and real/imaginary off-diagonal units
give $\sum_a X_a^2=NI$. The normalized group generator is
$(2N)^{-1}\sum_a\partial_{iX_a}^2$; it has $Gp_1=-p_1/2$, as in D5.

A trace word with positive and negative degrees $q$ is a matrix
coefficient of $U^{\otimes q}\otimes\bar U^{\otimes q}$.
Writing $d=2q$, its Hermitian infinitesimal generators are
$D_a=\sum_{\ell=1}^d D_a^{(\ell)}$, with a fundamental $X_a$ or
antifundamental $-\bar X_a$ on each slot. For any vector,

$$
\sum_a\|D_av\|^2\le d\sum_{a,\ell}\|D_a^{(\ell)}v\|^2
=d^2N\|v\|^2.
$$

The tensor heat Casimir therefore has spectrum in $[0,2q^2]$.
Diagonalizing that finite Hermitian matrix shows the same range for its
matrix-coefficient functions. Taking $q\le Q$ covers the trace span.
Its heat invariance and Haar self-adjointness were proved in FLOW-019,
so the restriction has nonnegative decay rates at most $2Q^2$ and
commutes with the projection. Haar mean is preserved. Contractivity
proves G3, and $1-e^{-\lambda t}\le\min(\lambda t,1)$ proves G4.
This coarse bound needs no representation-theoretic highest-weight input.

## 4. Quantitative packet input for the prescribed operator

There exist constants $C_0,\alpha>0$, independent of odd $N\ge3$ and
nonzero integer $j$, such that the **unchanged** map satisfies

$$
|p_j(U_N)|\le C_0 e^{\alpha|j|}.
\tag{G8}
$$

The bound is useful only through a logarithmic time window. It is not
a Heisenberg trace cancellation estimate. The new uniformity is proved
below, rather than inferred from the fixed-$j$ thresholds of FM-013.

Use the exact coherent frame, sampling intertwining and odd-N metaplectic
descent of [FM-013](fixed_time_wavepacket_trace_bound.md), (2)--(6).
Its symbol is a fixed finite Fourier polynomial; the kick time remains
$\kappa=10^{-80}/(2\pi)$. Along the piecewise classical path through $j$
kicks and $j$ linear cat steps, the variational matrix $J(s)$ and its
inverse obey $\|J(s)\|+\|J(s)^{-1}\|\le C e^{c j}$.
This follows from bounded one-kick derivatives, the fixed linear cat
matrix and multiplication of at most $j$ such matrices. Derivatives of
the kick Hamiltonian of each fixed order are uniformly bounded along
the path, because the symbol is periodic.

Fix the packet expansion order $L=5$ and a Schwartz seminorm order $D$.
After removing the trajectory, action and quadratic metaplectic evolution,
the order-$r$ perturbing Taylor operator has degree $r+2$ and coefficients
bounded by $C_r e^{c(r+2)j}$. Iterated Duhamel terms contributing to
order $\ell\le L$ have $r_1+\cdots+r_n=\ell$, $n\le\ell$.
Acting on the initial Gaussian, their polynomial degree is at most
$\sum_i(r_i+2)\le3\ell$. Their coefficient integrals have volume at
most $(j\kappa)^n/n!$; the number of compositions depends only on $L$.
Every needed envelope seminorm therefore has a bound

$$
\sum_{a+b\le D}\|y^a\partial_y^b a_\ell\|_2
\le C_{D,L}e^{c_{D,L}j},\quad 0\le\ell\le L.
\tag{G9}
$$

Reapplying the quadratic evolution costs at most another exponential:
conjugating position and momentum uses the linear $J(s)$, so each fixed
seminorm is bounded by a fixed power of $\|J(s)\|+\|J(s)^{-1}\|$.
This also treats the cat jumps, which are exactly quadratic. No degree
or number of nonlinear perturbation insertions grows with $j$ at fixed $L$.

Taylor's integral remainder for each Fourier exponential on these
Schwartz envelopes gives the physical $ih\partial_t$ residual
$C e^{cj}h^{(L+3)/2}$ in finitely many such seminorms. The bounded
Fourier frequencies make the rescaled translations uniformly bounded
on these fixed seminorms for $h\le1$. Sampling preserves the bound:
for any envelope $b$,

$$
\left\|\mathcal P_N\left[h^{-1/4}b((x-q)/\sqrt h)
e^{ip(x-q)/h}\right]\right\|\le
C\sup_y(1+|y|)^2|b(y)|\le C_D\|b\|_{\mathscr S_D}.
$$

Indeed Cauchy--Schwarz on integer translates, followed by the mesh of
spacing $(N\sqrt h)^{-1}$, bounds the squared norm by a constant times
that squared supremum; $N\sqrt h=\sqrt{N/(2\pi)}$ is bounded below
by $\sqrt{3/(2\pi)}$ here. A fixed $D$ larger than
three supplies the last Sobolev bound. This applies to the Taylor
remainder itself; it is not sampling an arbitrary small plane-$L^2$ error.
Finite-dimensional unitary Duhamel over the $j$ kick intervals, and exact
unitary cat jumps, therefore give a packet approximation error
$C e^{cj}h^{(L+1)/2}=C e^{cj}h^3$.

The finitely many polynomial-Gaussian terms have degree at most $3L$
and coefficients/seminorms bounded exponentially. The eigenvalues of
their Gaussian covariance matrices lie between $C^{-1}e^{-cj}$ and
$Ce^{cj}$. Gaussian overlap and Poisson summation, as in FM-013 (7),
then give for some $c_0>0$ and $1\le j\le c_0\log N$,

$$
|\langle\psi_{z,N},U_N^j\psi_{z,N}\rangle|
\le C e^{cj}(1+\operatorname{dist}(F^jz,z)/\sqrt h)^{-4}
+C e^{cj}h^3.
\tag{G10}
$$

To make the periodization uniform, choose $c_0$ small enough that the
largest physical covariance $h e^{cj}$ is at most $C N^{-1/2}$.
The lattice Gaussian sum is then bounded by a constant times its
nearest-image Gaussian with a weakened exponent. Polynomial factors
and the weakening from $e^{-cj}\operatorname{dist}/\sqrt h$ to
$\operatorname{dist}/\sqrt h$ cost only another $e^{cj}$.
All constants use finitely many seminorm orders fixed before varying $j$.

The return-volume estimate [FM-007](frozen_seven_cut_reduction.md), (11),
is uniform in $j$. Its covering degree is
$\lambda^j+\lambda^{-j}-2$, and its displacement Jacobian is bounded
below by $c\lambda_-^j$. It gives

$$
|\{z:\operatorname{dist}(G^jz,z)\le r\}|
\le C e^{c j}r^2.
$$

The same distributional estimate holds for $F^j=G^{-j}$ by the
area-preserving change of variable $w=F^jz$. Integration of G10
against the exact trace frame thus gives
$|p_j(U_N)|\le C e^{cj}(Nh+Nh^3)\le C e^{cj}$ in that logarithmic
window. Dyadic integration of the power four uses precisely the
two-dimensional return-volume bound. Constants absorb finitely many
small dimensions if the window was initially stated for large $N$.

For $j>c_0\log N$, the elementary bound $|p_j|\le N$ is at most
$e^{j/c_0}$. Increase $\alpha$ to dominate $c$ and $1/c_0$;
negative $j$ follow by unitarity. This proves G8 for all stated $N,j$.
No useful exponential bound beyond the logarithmic window is inferred.

## 5. An unconditional growing-degree projection at the actual map

Set $s=2\alpha+1$, $\gamma=1/(4s)$ and $Q_N=\lfloor\gamma\log N\rfloor$.
The stable range holds for all sufficiently large $N$. By G8 and G5,

$$
\mathcal K_{Q_N}(U_N)\le D_s e^{2sQ_N},\qquad
D_s=e^{\pi^2/(12s)}(1-e^{-(s-2\alpha)})^{-2C_0^2}.
$$

For every fixed compact local factorial or positive Laplace test of
FLOW-019 P5, its origin average $F_N$ has CUE variance $C_F/N$.
Consequently, uniformly at every $t\ge0$,

$$
|P_t\mathsf P_{Q_N,N}F_N(U_N)-\mathbb E_{\rm CUE}F_N|
\le C_F' N^{-1/4}.
\tag{G11}
$$

Its projected heat defect has the same bound times
$\min(2Q_N^2t,1)$. This removes a genuinely growing logarithmic
filtration; it does not assert an effective numerical value for
$\gamma$ or a uniform estimate at $Q\asymp N$.
Schwartz tests inherit the exact G3/G5 criterion, but the qualitative
variance bound alone supplies no automatic growing-degree rate.

If instead $|p_m(A_N)|\le K$ uniformly for all $m\le Q_N$, choose
$s=\pi/\sqrt{24Q_N}$ in G5. For $Q_N\ge1$ this gives

$$
\sqrt{\mathcal K_{Q_N}(A_N)}\le
e^{\pi\sqrt{Q_N/6}}(1+\sqrt{24Q_N}/\pi)^{K^2}.
\tag{G12}
$$

Thus G3 gives convergence of projected compact tests throughout
$Q_N\le c(\log N)^2$, for any fixed $c<3/(2\pi^2)$ under that stronger
uniform trace hypothesis. The actual map has not been proved to satisfy
that stronger hypothesis.

## 6. A universal evaluation obstruction and the remaining signed vector

The cost cannot be made polynomial at Heisenberg degree by choosing a
better starting spectrum. Let
$L=\lfloor(\sqrt{1+4Q}-1)/2\rfloor$. Restrict G2 to
$a_m=b_m\in\{0,1,2\}$ for $1\le m\le L$ and zero elsewhere.
Their largest positive degree is $L(L+1)\le Q$. With $x=|p_m(A)|^2/m$,
the corresponding squared normalized polynomials are
$1$, $(1-x)^2$ and $(1-2x+x^2/2)^2$. For all $x\ge0$,

$$
(1-x)^2+(1-2x+x^2/2)^2\ge1/32.
$$

If $|x-1|\ge1/4$ the first square is at least $1/16$; otherwise
$3/4<x<5/4$ and the second polynomial is at most $-7/32$.
It follows for **every** unitary $A$ in the stable range that

$$
\mathcal K_Q(A)\ge(33/32)^L.
\tag{G13}
$$

In particular the centered evaluation norm grows faster than every
power of $N$ if $Q/(\log N)^2\to\infty$. At $Q\asymp N$ it is at
least $e^{c\sqrt N}$, uniformly over starting spectra. This obstructs
the whole-filtration evaluation-norm route from CUE Haar concentration
to a Heisenberg-degree pointwise bound. It does not obstruct a special
observable's signed coefficient cancellation.

For the clock and $Q<N$, G1 at zero is nonzero only when $a_m=b_m$;
the squared normalized value is then one. Hence exactly
$\mathcal K_Q(C_N)=\sum_{q=0}^Q p(q)$. G12 controls its projected
compact tests through the stated logarithm-squared range, even though
the full local clock defect of FLOW-019 P8 remains nonzero. G8's
exponential trace bound is also satisfied by clocks; it cannot alone
imply BGS.

## 7. Exact blindness of every sublinear projection to a fixed local pair test

This identifies a specific missed observable, not only a large norm.
Fix nonzero $0\le w\in C_c^\infty((a,b))$, $0<a<b<1/2$, and put

$$
J_{N,w}(A)=N^{-2}\sum_{m\ge1}w(m/N)(|p_m(A)|^2-m).
$$

The Fourier weight defines a Schwartz local pair comparison in the
repository's unfolding; the sum is finite. More explicitly, in the
[pair bridge](trace_to_local_statistics_bridge.md), (13), use the real even
test $\widehat\varphi(\xi)=w(|\xi|)/2$. Its exact difference from finite
CUE is $J_{N,w}$; the factor one half prevents double counting the two
frequency signs. If $Q<aN$, then

$$
\mathsf P_{Q,N}J_{N,w}=0,\qquad
\|J_{N,w}\|_{L^2({\rm Haar})}^2
=N^{-4}\sum_{m\ge1}m^2|w(m/N)|^2=O_w(N^{-1}).
\tag{G14}
$$

Here $2Q<N$ and each participating $m$ has $m+Q<N$.
Diaconis--Evans thus evaluates its Gram product with a neutral word
of degree at most $Q$ exactly. That word cannot involve trace index
$m>Q$. Its Gaussian counterpart is independent of
$|Z_m|^2-m$, whose mean is zero. Every such inner product vanishes.
For the second identity, any participating $m,n$ obey $m+n<N$;
the covariance of the two centered Gaussian squared moduli is
$\mathbf1_{m=n}m^2$. These are finite exact moment statements.

For the clock all participating traces vanish, and
$J_{N,w}(C_N)\to-\int_a^b\xi w(\xi)d\xi<0$ by a Riemann sum.
Every $Q_N=o(N)$ is eventually blind to this same **fixed** local
test. Heat commutation also gives $\mathsf P_{Q_N}P_tJ_{N,w}=0$;
it does not give $P_tJ_{N,w}=0$. Thus the logarithmic and
logarithm-squared projection estimates leave a concrete microscopic
comparison entirely in the complement. At $Q\asymp N$ the whole-span
norm obstruction G13 applies, while the special pair coefficients
may still enjoy cancellation.

For the actual map the remaining signed vector is precisely
$N^{-2}\sum_m w(m/N)(|p_m(U_N)|^2-m)$ for this example.
The estimates above do not prove its vanishing. Higher-order factorial
counterterms require their full signed vectors as well. The unprojected
complementary estimate, TRACE-005 and the full deterministic BGS goal
remain **OPEN**.

## 8. A sharp degree-uniform Casimir interval by permutation cut-and-join

The quadratic bound G4 can be improved without a highest-weight theorem.
Put $\mathcal V_{q,N}=\mathcal H_{q,N}\ominus\mathcal H_{q-1,N}$,
$q\ge1$, with $\mathcal H_{0,N}$ the constants. In the stable range
$2q\le N$, every heat decay rate on $\mathcal V_{q,N}$ lies in

$$
q-\frac{q(q-1)}N\ \le\lambda\le\ q+\frac{q(q-1)}N.
\tag{G15}
$$

This is the standard finite permutation cut-and-join mechanism; the
application and its full normalization are proved here. On class
functions on $S_q$, with normalized counting measure, define

$$
\mathcal T_q f=\frac1{q!}\sum_{\sigma\in S_q}
f(\sigma)p_{\operatorname{cycle}(\sigma)},\qquad
\mathcal C_q f(\sigma)=\sum_{\tau\text{ transposition}}f(\sigma\tau).
$$

For cycle partition $\lambda$ with multiplicities $a_m$ put
$z_\lambda=\prod_m m^{a_m}a_m!$. Its class has size $q!/z_\lambda$.
Independent complex Gaussians of variances $m$ give
$\mathbb E p_\lambda(Z)\overline{p_\mu(Z)}
=\mathbf1_{\lambda=\mu}z_\lambda$. Hence $\mathcal T_q$ is an
isometry onto the holomorphic weighted-degree-$q$ trace polynomial
space. Right multiplication by each transposition is a self-adjoint
unitary on the full permutation space. The sum is central, preserves
class functions and has operator norm at most $q(q-1)/2$.

Transporting $\mathcal C_q$ through $\mathcal T_q$ gives exactly the
positive cut-and-join operator: on a product of trace factors it splits
a cycle of length $m$ with coefficient $m/2$ for each ordered split
$m=b+(m-b)$, and joins two distinct factor positions of lengths $m,n$
with coefficient $mn$. These coefficients follow by counting the
transpositions within a cycle and between two cycles. The ordered split
sum counts an unordered split twice, including the half-length case
with its displayed $m/2$ coefficient.

The Wick map sends a holomorphic degree-$q$ polynomial times an
antiholomorphic one to $\mathcal V_{q,N}$. G6 makes this map an
isometry from the tensor product of the two holomorphic Gaussian
spaces: the normalized basis is exactly the part of G2 with degree
$q$. Its leading raw trace polynomial is unchanged. In D5 the diagonal
term at that degree is $-q$. Positive splitting and same-sign merging
give $-\mathcal C_q/N$ on each of the two factors. Opposite-sign
merging strictly lowers both weighted degrees, including $p_0=N$.
Wick lower terms also have degree less than $q$.

Haar self-adjointness and invariance of the two nested filtrations make
$\mathcal V_{q,N}$ reducing. Therefore its action is determined by
this leading quotient, and under the isometry above is precisely

$$
G_N\big|_{\mathcal V_{q,N}}=-qI-\frac1N
(\mathcal C_q\otimes I+I\otimes\overline{\mathcal C_q}).
$$

The permutation operator is real. Its two norms give G15; no algebraic
independence beyond the stable range is assumed. Both endpoints are
attained: the constant and sign class functions have respective
$\mathcal C_q$ eigenvalues $q(q-1)/2$ and $-q(q-1)/2$, and their
two-factor Wick images are nonzero by the isometry. Taking the union of
$q\le Q$ improves G4's factor to
$\min\{[Q+Q(Q-1)/N]t,1\}$. In particular the maximal decay rate
is at most $3Q/2$ for $2Q\le N$. This stronger bound still does not
estimate a complementary actual-map value.

## 9. Heat inversion is unstable even for the particular fixed pair test

Each $|p_m|^2-m$ in G14 is exactly one Wick polynomial, in
$\mathcal V_{m,N}$, and $2m<N$ on the stated band. Different $m$
are orthogonal. By G15 every participating decay rate is at least
$m[1-(m-1)/N]\ge a(1-b)N$. Thus, for every $t\ge0$,

$$
\|P_tJ_{N,w}\|_2\le e^{-a(1-b)Nt}\|J_{N,w}\|_2.
\tag{G16}
$$

For sufficiently large $N$ the test is nonzero by the exact variance
in G14. Any linear operator $L$ whose domain contains $P_tJ_{N,w}$ and
satisfies $L(P_tJ_{N,w})=J_{N,w}$ has Haar-$L^2$ operator norm
at least $e^{a(1-b)Nt}$. The same lower bound applies to the Lipschitz
constant of a map defined on $\{0,P_tJ_{N,w}\}$ with images
$0,J_{N,w}$. At the actual proved
logarithmic noisy time this lower bound exceeds every fixed power of
$N$. This establishes instability for a specific fixed **local pair
test**, in the Haar-$L^2$ norm; it is not a point-evaluation or
supremum-norm lower bound. The prior FLOW-015 character obstruction
concerned a different function space.

The original operator's value $J_{N,w}(U_N)$ remains unknown. A
model-specific signed estimate might bypass every whole-space or
inverse-norm obstruction above. Neither small noisy/Haar norms nor
the exact sublinear projection identity supply that estimate. The
full deterministic BGS target remains **OPEN**.
