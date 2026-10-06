# Transport of local moments without a maximum-displacement estimate

**Claim ID:** BGS-FLOW-016. **Status:** project proof with independent internal
review of the new implications; inherited inputs retain their recorded scope.
The point-field theorem below is proved directly. Its matrix application uses
the explicitly stated estimates in FLOW-004 and FLOW-009, and the reference
kernel limit in FLOW-014. No deterministic noise removal is asserted.
Hardy--Littlewood maximal estimates, spectral perturbation along unitary
paths, and moment interpolation are standard mechanisms; priority is not claimed.

## 1. Contract

Let $A_N,B_N$ be possibly random counting measures on the line, periodic
with period $N$, with exactly $N$ points per period, including multiplicities.
Match the labels bijectively on the circle and choose periodic lifts with
shortest signed displacements $d_j$, $|d_j|\le N/2$. Write

$$
c_{p,N}=\frac1N\sum_{j=1}^N|d_j|^p,\qquad p\ge1.
\tag{T1}
$$

The origin $u$ is independent and uniform on $[0,N)$. Expectations below
include the fields and this origin. Suppose that for every fixed $q>1$

$$
\sup_N\mathbb E B_N([u-1/2,u+1/2])^q<\infty.
\tag{T2}
$$

For a fixed $p$ with $\sup_N\mathbb E c_{p,N}<\infty$, every fixed bounded
window has uniformly bounded target count moments of order $1<s<p+1$.
If, in addition, $\mathbb E c_{p,N}\to0$ and the reference fields viewed
from $u$ converge weakly to a locally finite point process, the target
fields have the same weak limit. Their factorial test expectations converge
for every integer order $k<p+1$, provided the reference limit is simple
or factorial measures are defined by distinct labels with multiplicity.

In particular, if the vanishing transport hypothesis holds for arbitrarily
large fixed $p$, all fixed factorial orders transfer. The quantifier is
**fixed order, then $N\to\infty$**. There is no assertion uniform in growing
order, and no estimate of the largest displacement.

## 2. Maximal density and the packing inequality

Fix $R\ge1$ and $N>4R$. Put

$$
M(u)=\sup_{r\ge1}\frac{B_N([u-r,u+r])}{2r},\qquad
m(x)=B_N([x-1/2,x+1/2]).
\tag{T3}
$$

The period integral of $m$ is $N$, and $M\ge1$ by letting $r\to\infty$.
Let $H$ be the centered maximal operator on periodic functions, allowing
all positive radii. Each point in $[u-r,u+r]$ contributes a full unit of
mass to $\int_{u-r-1/2}^{u+r+1/2}m(x)dx$. Hence $M\le3Hm/2$.
For $q>1$, the dimension-free periodic estimate is

$$
\frac1N\int_0^N(Hm)^qdu\le C_q\frac1N\int_0^Nm^qdu.
\tag{T4}
$$

Here is a proof retaining the independence of $N$. For $\lambda$ at most
three times the period mean, the weak $(1,1)$ bound follows from the total
length $N$. Above this threshold a witnessing interval has radius less
than $N$: larger intervals average at most $3/2$ times the period mean.
For centers in $[0,N]$ such intervals lie in $[-N,2N]$. Extend the
function by zero outside those three periods. The one-dimensional greedy
interval selection, with the union covered by triple dilates of disjoint
selected intervals, gives
$|\{Hm>\lambda\}\cap[0,N]|\le9\lambda^{-1}\int_0^Nm$.
Finite selections followed by monotone exhaustion suffice. Apply this
bound to $m1_{m>\lambda/2}$, since $H(m1_{m\le\lambda/2})\le\lambda/2$,
and integrate the distribution function. The resulting constant is at
most $18q2^{q-1}/(q-1)$. This proves (T4), and (T2) bounds every fixed
$\mathbb EM^q$.

Let $n=A_N([u-R,u+R])$ and
$T_p(u)=\sum_{a_j+\ell N\in[u-R,u+R]}|d_j|^p$. This window contains
at most one copy of each label. If $n>16(R+1)M$, choose $r=n/(8M)$.
Then $r\le N/8$ and $r>2R$. At most $n/4$ of the matched reference
points are in $[u-r,u+r]$. Thus at least $3n/4$ displacements have size
at least $r-R\ge n/(16M)$. Consequently

$$
T_p(u)\ge\frac{3n^{p+1}}{4\,16^pM^p}.
\tag{T5}
$$

The complementary case bounds $n$ by $16(R+1)M$. For every $s>0$,

$$
n^s\le C_{p,s,R}\left(M^s+M^{ps/(p+1)}T_p^{s/(p+1)}\right).
\tag{T6}
$$

Origin averaging counts each displacement for a length $2R$, so
$\mathbb E T_p=2R\mathbb E c_{p,N}$. For $1<s<p+1$, Hölder gives

$$
\mathbb En^s\le C_{p,s,R}\left[
\mathbb EM^s+
\left(\mathbb EM^{ps/(p+1-s)}\right)^{(p+1-s)/(p+1)}
(2R\mathbb Ec_{p,N})^{s/(p+1)}\right].
\tag{T7}
$$

There is no independence assumption between $M$ and the displacement cost.
This is the additional uniform integrability missing from a weak-law coupling.

## 3. Weak law and factorial observables

For $f\ge0$ compactly supported and $C^1$, integrate the difference of
the translated periodizations along each shortest displacement. Since
$|e^{-a}-e^{-b}|\le|a-b|$ for nonnegative $a,b$,

$$
\mathbb E|\Phi_{N,f}(A_N)-\Phi_{N,f}(B_N)|
\le\|f'\|_1\mathbb Ec_{1,N}
\le\|f'\|_1(\mathbb Ec_{p,N})^{1/p}.
\tag{T8}
$$

Here $\Phi$ already includes origin averaging; it is not a fixed-origin
observable. The uniform first count bound from (T7) gives local tightness.
Positive smooth Laplace tests determine the locally finite point-field
law (approximation on each compact set then tightness), proving weak transfer.

For $\psi\in C_c(\mathbb R^k)$ define
$Z_\psi(\xi)=\sum_{i_1,\ldots,i_k\ {\mathrm{distinct}}}
\psi(x_{i_1},\ldots,x_{i_k})$, using atom labels even at coincident positions.
The partition inclusion-exclusion formula writes it as a finite polynomial
in product measures and diagonal restrictions. It is continuous under vague
convergence of counting measures. If the support lies in $[-R,R]^k$, then
$|Z_\psi|\le\|\psi\|_\infty\xi([-R,R])^k$.
Choose $k<s<p+1$ in (T7). Truncation and uniform integrability then prove
convergence of its expectation. For $k=1$ the same argument uses any $s>1$.

With all count moments, the conclusion extends to Schwartz tests. Tile
the line into unit intervals. For any $k$ tiles, Hölder bounds the expected
product of their counts by the common stationary $k$th count moment.
The sum of the suprema of a Schwartz test over these boxes is finite,
and its tails tend uniformly to zero. Compact truncation proves the claim.
The same argument, with moments of order $2k$ and higher, works in $L^2$.
Terms using two different period copies of one circle label are absent on
any fixed compact window once $N>2R$; for Schwartz tests their separations
are at least $N$, and the same tail estimate removes them.

The range $k<p+1$ cannot be enlarged to $k>p+1$ under these hypotheses.
Take reference points $0,1,\ldots,N-1$ and move the first $K$ to zero.
For the interval $[u,u+1)$ its target $k$th factorial mean, $k\ge2$, is
$(K)_k/N$, whereas the reference mean is zero. The transport cost is
$N^{-1}\sum_{j=0}^{K-1}j^p$. Set $N$ asymptotic to $K^k$, choosing
odd dimensions if desired. Then the factorial defect tends to one but
the cost tends to zero for $k>p+1$. Multiplicities are allowed; jitter
inside a vanishing interval gives a simple version. No critical-endpoint
claim at $k=p+1$ is made.

## 4. From Schatten moments to unfolded displacements

For unitary $V,W$ put $H=-i\log(VW^*)$, with principal Hermitian
logarithm, and follow $V(s)=e^{isH}W$. Continuous eigenangle branches are
absolutely continuous. Where a branch is simple its derivative is
$\langle v_j,Hv_j\rangle$; at collisions diagonalize the compression
of $H$ to the eigenspace. Equivalently perturb and pass to the limit.
Convexity gives $\sum_j|\theta'_j|^p\le\operatorname{Tr}|H|^p$.
Minkowski over $s\in[0,1]$ bounds the $p$th sum of the total branch
displacements by the same quantity. Their shortest circular displacements
are smaller. Since $|h|\le(\pi/2)|e^{ih}-1|$ for $|h|\le\pi$,

$$
c_{p,N}(V,W)\le\frac{N^{p-1}}{4^p}\operatorname{Tr}|V-W|^p.
\tag{T9}
$$

Unfolding is $x=N\theta/(2\pi)$ as throughout the project. This is an
existence of a matching for each pair, not a specified cyclic ordering.
The estimates are unchanged by a measurable minimum-cost choice.

## 5. Projected diffusion: a larger time window for all local moments

Let $Y$ be FLOW-011's globally localized projected diffusion from
$Y_0=\Pi A_N$, with $|p_1(A_N)|+|p_2(A_N)|\le K$ and hence
$|p_2(Y_0)|\le C_K$ by FLOW-012 (G3). Let $V$ be normalized traceless
unitary Brownian motion from $Y_0$, coupled by FLOW-009's common noises.
For $|m_2(Y)|\le1/2$, that proof gives, with $R_a=L_a-B_a$,

$$
\Big\|\sum_aR_a^2\Big\|_{\rm op}\le
\frac{4|p_2(Y)|^2+44}{N^2},\quad
\|A_\Pi\|_{\rm op}\le80/N^2,
\quad \overline Lp_2=-\tfrac12(1-|m_2|^2)p_2+e,
\quad |e|\le150/N,\quad \overline\Gamma(p_2,\bar p_2)\le64.
\tag{T10}
$$

For each fixed integer $r\ge1$, choose a threshold $K_{N,r}\ge4C_K+300$
with
$K_{N,r}^2=C_{K,r}(1+t\log N)$, increasing the constant as needed.
Assume $t\to0$ and $t^2\log N\to0$. This threshold is $o(N)$ and lies
inside the region where the localization equals one. Stop at
$\sigma_r=\inf\{s:|p_2(Y_s)|\ge K_{N,r}\}$. On this interval the
drift has size at most $K_{N,r}/2+150/N$. For $t\le1/4$ the initial
value and integrated drift use less than half the threshold. Apply the
scalar exponential martingale inequality to the real and imaginary
parts, each with bracket at most $64t$, and take their union:

$$
\mathbb P(\sigma_r\le t)\le4e^{-cK_{N,r}^2/t}
\le C_{K,r}N^{-4r-4}.
\tag{T11}
$$

All processes in this statement are the full global processes. Only the
comparison estimate is stopped; on an exit we use a bounded circle cost.
For $Z=V^*Y$, the stopped martingale part of $Z-I$ has both matrix
brackets bounded by $vI\,ds$, $v=(4K_{N,r}^2+44)/N^2$, since conjugation
and the unitary factors preserve the bracket bounds. The additional
drift has operator norm at most $v/2+80/N^2$; the commutator term is
zero by FLOW-009 (14). FLOW-004's Hermitian-dilation Itô estimate is

$$
\mathbb E\operatorname{Tr}|M_t|^{2r}
\le N(2r-1)!!(vt)^r.
\tag{T12}
$$

Its dimension factor is $N$, not $N\log N$. Schatten triangle and the
drift bound, followed by (T9), show for the stopped pair

$$
\mathbb Ec_{2r,N}\le C_r[(K_{N,r}^2+1)t]^r
+C_r\left(\frac{(K_{N,r}^2+1)t}{N}\right)^{2r}.
\tag{T13}
$$

The full pair costs at most $(N/2)^{2r}$ on the exit event. Therefore

$$
\mathbb Ec_{2r,N}(Y_t,V_t)
\le C_{K,r}(t+t^2\log N)^r+C_{K,r}N^{-2r-4}\longrightarrow0.
\tag{T14}
$$

The threshold used in proving this estimate can depend on $r$. The
underlying common-noise coupling and global processes do not.
No maximum displacement, or convergence in operator norm on the
microscopic scale, is inferred.

Suppose FLOW-014's reference hypotheses hold at these times. For distinct
initial levels its locally uniform kernel bound (U23)--(U24) bounds every
fixed reference factorial count moment on a fixed compact set. Repeated
initial levels require a separate finite-$N$ argument, not an assumed
pointwise confluent kernel. Approximate their unitary by distinct spectra.
The strip/potential error budgets can be kept arbitrarily close by choosing
the perturbation sufficiently small at each fixed $N$; the kernel bounds
have no minimum-gap constant. Take a nonnegative compact smooth bump at
least one on the desired window and its tensor powers. Its origin-averaged
distinct-label statistic is continuous in the matrix and bounded by
$C_kN^k$ at this fixed $N$. Brownian motion driven by the same noises is
continuous in its initial matrix. Dominated convergence therefore transfers
the uniform factorial-majorant bounds from the approximants to the repeated
start. The approximation limit is taken at each fixed $N$ first. Ordinary
count moments then follow by the Stirling identity, with constants uniform
in large $N$ for each fixed moment order.
Full and traceless Brownian motions differ by an independent scalar phase.
Uniform-origin averaging makes every rotation-invariant factorial statistic
identical under the two laws, just as for the earlier Laplace observable.
Thus (T2) holds for the reference $V_t$ and its local limit is Sine$_2$.
Equations (T7)--(T14) prove all fixed factorial orders for $Y_t$.

For the actual frozen map, FLOW-014 uses
$J=\lfloor c\log N\rfloor$, $g=4\log J/J$, $t=8g$.
Then $t^2\log N=O((\log\log N)^2/\log N)\to0$.
The present argument applies at that same time, although the previous
maximum-displacement estimate required $t\log N\to0$ and could not.

## 6. Boundary

This proof supplies uniform integrability for a noisy diffusion. It does
not estimate FLOW-015's signed defect for $A_N$ itself. The matrix moment
argument uses specific projected covariance and trace drift estimates;
classical chaos alone supplies none of them. No conclusion about every
chaotic quantum system or deterministic microscopic BGS follows.
