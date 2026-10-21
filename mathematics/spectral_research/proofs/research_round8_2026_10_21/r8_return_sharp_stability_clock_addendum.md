> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_return_sharp_stability_clock_addendum.md`. Embedded SHA256: `f77baf9f94d8ed92c3b83abe88e042e16db31864b80a070ac69db5082da67e08`.
> [Thematic guide](../../topics/dephasing.md).

# An explicit Laplace counterexample at every positive multiple of 1/N

21 October 2026. Round 8. Addendum to the norm-threshold argument.

This construction supplies a pair of explicit deterministic unitary
sequences whose operator distance is at most $C/N$, for any
prescribed $C>0$, and whose local Laplace functionals stay apart.
It needs no assumption that some deterministic sequence already has
a Sine-2 limit. Both sequences below are auxiliary; neither is the
specified kick-cat family.

Together with the proved $o(1/N)$ stability inequality in Section 3
of `root_sharp_microscopic_perturbation_threshold.md`, the construction
establishes sharpness for **uniform Laplace stability itself**. The
separate rounded-family argument in that note establishes a bounded
witness and a five-test failure of Sine-2 for replacements of any base.

## 1. The two explicit spectra

Fix $C>0$ and put
$$
 d=\min\{1/8,C/(4\pi)\}>0,\qquad b=1-2d,\qquad \sigma=d/4.
 \tag{1.1}
$$
For each odd $N\ge3$, use the diagonal matrices
$$
 C_N=\operatorname{diag}_{0\le j<N}e^{2\pi ij/N},\qquad
 D_N=\operatorname{diag}_{0\le j<N}
           e^{2\pi i(j+d(-1)^j)/N}.
 \tag{1.2}
$$
Since their eigenvectors agree,
$$
 \|D_N-C_N\|_{\rm op}
   =2\sin(\pi d/N)
   \le\frac{2\pi d}{N}\le\frac C N.
 \tag{1.3}
$$
The local process for $C_N$ is exactly a translate of
$\mathbb Z$. In unfolded coordinates, one period of the
$D_N$ spectrum is
$$
 x_j=j+d(-1)^j,\qquad 0\le j<N,
$$
and the full process before the random translation consists of
$x_j+N\ell$, $\ell\in\mathbb Z$.

These positions are strictly ordered. The consecutive gaps are
$1-2d=b$, $1+2d$, and, across the end of the odd period,
$1$. The gap $b$ occurs exactly $(N-1)/2$ times per period,
between $x_{2k}=2k+d$ and $x_{2k+1}=2k+1-d$,
$0\le k<(N-1)/2$. The minimum gap is $b\ge3/4$.

## 2. One fixed smooth Laplace test

Choose $f_1\in C_c^\infty((-\sigma,\sigma))$ such that
$0\le f_1\le1$ and $f_1=1$ on
$[-\sigma/2,\sigma/2]$. Put
$$
 f_2(x)=f_1(x-b),\qquad f=f_1+f_2,
 \qquad h(x)=1-e^{-f_1(x)}.
 \tag{2.1}
$$
All functions are fixed before $N$ tends to infinity. Their
supports are disjoint. A point in the first support and one in the
second have positive difference in
$$
 (b-2\sigma,b+2\sigma)\subset(0,1),
 \tag{2.2}
$$
because $b+2\sigma=1-3d/2<1$ and
$b-2\sigma=1-5d/2>0$.

Each individual support has length $2\sigma<b$. Thus, for both
processes and every random origin, each support contains at most one
point. The exact intensity-one identity gives the same single-bump
Laplace values for the two sequences:
$$
 L_N^{C_N}(f_i)=L_N^{D_N}(f_i)
       =1-\int_{\mathbb R}(1-e^{-f_i(x)})\,dx,
       \qquad i=1,2.
 \tag{2.3}
$$
To justify (2.3) directly, at most one summand is nonzero in
$\langle f_i,\Xi\rangle$; consequently
$e^{-\langle f_i,\Xi\rangle}
 =1-\langle1-e^{-f_i},\Xi\rangle$. Integrating the spectral
origin unfolds each eigenvalue period and gives intensity one.

Define the bounded continuous functional
$$
 \mathcal O(\xi)=
   (1-e^{-\langle f_1,\xi\rangle})
   (1-e^{-\langle f_2,\xi\rangle}).
 \tag{2.4}
$$
For the clock process it is identically zero: no two distinct
integers have a positive difference in (2.2), and a single point
cannot belong to both disjoint supports.

For the $D_N$ process, a pair hitting these two supports must have
separation less than one. It must be consecutive, because two or
more consecutive gaps have total length at least $2b>1$. Its gap
must therefore equal $b$: the other possible consecutive gaps
are at least one. Conversely a close pair with its first point at
$t$ contributes $h(t)^2$, because the second point is at
$t+b$ and $f_2(t+b)=f_1(t)$. At most one point lies in each
support, so this counts $\mathcal O$ exactly, without an
overcounting inequality.

Each of the $(N-1)/2$ close pairs per period contributes
$N^{-1}\int h^2$ after integrating the random origin. Indeed,
for its first location $x_{2k}$,
$$
 \int_0^1\sum_{\ell\in\mathbb Z}
    h(x_{2k}-N\alpha+N\ell)^2\,d\alpha
      =\frac1N\int_{\mathbb R}h(t)^2\,dt.
$$
It follows that
$$
 \mathbb E\mathcal O(\Xi^{D_N}_{N,\alpha})
       =\frac{N-1}{2N}\int_{\mathbb R}h(t)^2\,dt,
 \qquad
 \mathbb E\mathcal O(\Xi^{C_N}_{N,\alpha})=0.
 \tag{2.5}
$$

Expanding (2.4) expresses its expectation as
$1-L(f_1)-L(f_2)+L(f_1+f_2)$. The single-bump values cancel by
(2.3). Thus a **single specified Laplace test** satisfies the exact
identity
$$
 \boxed{
 L_N^{D_N}(f)-L_N^{C_N}(f)
   =\frac{N-1}{2N}\int_{\mathbb R}(1-e^{-f_1(t)})^2\,dt
   \longrightarrow
     \frac12\int_{\mathbb R}(1-e^{-f_1(t)})^2\,dt>0.}
 \tag{2.6}
$$
For example, the limiting value is at least
$\sigma(1-e^{-1})^2/2>0$ because of the plateau of $f_1$.

## 3. What sharpness now means

For every $C>0$, (1.3) and (2.6) disprove a universal assertion
that an operator perturbation bounded by $C/N$ must preserve
all local Laplace functionals. The assertion is disproved along all
odd dimensions, by diagonal unitary matrices with explicit spectra.
No eigenvalue matching theorem, factorial-moment convergence, Sine-2
base sequence, or limiting point-process existence argument is needed
for this counterexample.

The upper stability theorem at $o(1/N)$, together with this
counterexample at every fixed positive $C/N$, establishes the
claimed sharp universal order. It does not exclude better stability
under additional structural restrictions on a perturbation.
