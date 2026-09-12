# The complete Pell resonance lattice and growing return times

**Status: project proof, with the limitations in Section 8.**
The lattice and first-return results below hold at every odd Pell index,
without a primality restriction or harmonic averaging. The growing-return
theorem uses prime indices and a specified harmonic average. These results
do not establish microscopic BGS universality. Priority is unverified.

## 1. Exact integer structure at every order

Let $K\ge3$ be odd, and write
$$
 N+F\sqrt2=(1+\sqrt2)^K,\quad \lambda=3+2\sqrt2,\quad
 s=F^{-1}\pmod N,\quad h=3+2s\pmod N .
$$
Then $N$ is odd, $N^2-2F^2=-1$, $s^2=2$, and $h^K=1$.
Both $h-1=2(1+s)$ and $h-h^{-1}=4s$ are units modulo $N$.
None of these facts requires $K$ to be prime.

On $\mathbb Z^K$ let $(Sx)_j=x_{j-1}$, with indices modulo $K$, and put
$$
 M=S^2-6S+I,\qquad {\bf1}=(1,\ldots,1),\qquad
 \mathcal L=\left\{c:\sum_jc_jh^j=\sum_jc_jh^{-j}=0\pmod N\right\}.
                                                               \tag{L1}
$$

**Theorem 1 (complete resonance lattice).** One has
$$
 M\mathbb Z^K
 =\left\{c\in\mathcal L:\sum_jc_j=0\pmod4\right\},\qquad
 \mathcal L=\coprod_{r=0}^3(M\mathbb Z^K+r{\bf1}).              \tag{L2}
$$
In particular
$$
 \mathbb Z^K/M\mathbb Z^K
 \simeq(\mathbb Z/N)^2\times\mathbb Z/4
 \simeq\mathbb Z/N\times\mathbb Z/(4N).                        \tag{L3}
$$
The nontrivial Smith factors of $M$ are $N,4N$.

**Proof.** The eigenvalues of $S$ are the $K$th roots of unity. Factoring
$z^2-6z+1=(z-\lambda)(z-\lambda^{-1})$ gives
$$
 |\det M|=\lambda^K+\lambda^{-K}-2=4N^2.                       \tag{L4}
$$
Consider the homomorphism
$$
 \Phi(c)=\left(\sum_jc_jh^j,\ \sum_jc_jh^{-j},\
                         \sum_jc_j\pmod4\right)
 \in(\mathbb Z/N)^2\times\mathbb Z/4 .
$$
The first two coordinates are onto using only $e_0,e_1$, since their
determinant $h^{-1}-h$ is a unit. Adding an integer multiple of $Ne_0$
then adjusts the last coordinate arbitrarily without changing the first
two: $N$ is odd. Thus $\Phi$ is onto. The relations satisfied by $h$
and $M{\bf1}=-4{\bf1}$ imply $M\mathbb Z^K\subset\ker\Phi$.
Both subgroups have index $4N^2$, so they are equal.

The geometric sum $\sum_jh^j$ vanishes because $h-1$ is a unit, and
the inverse sum vanishes too. Therefore $\mathbf1\in\mathcal L$.
Its coefficient sum $K$ generates $\mathbb Z/4$, proving the disjoint
coset decomposition. The final isomorphism in (L3) uses $\gcd(4,N)=1$.

The real-vector inequality
$$
 \|Mx\|_1\ge6\|Sx\|_1-\|S^2x+x\|_1\ge4\|x\|_1              \tag{L5}
$$
gives a useful additional consequence: a vector in the odd cosets of
(L2) has norm at least $K$, and one in the coset $2{\bf1}$ has norm
at least $2K$. Indeed $c=M(q-r{\bf1}/4)$ and every coordinate of
$q-r{\bf1}/4$ is at distance at least $1/4$ or $1/2$ from zero.
Thus every central relation of norm less than $K$ lies in the integer
image of $M$, without the earlier largest-gap cutoff.

## 2. A summable majorant for the entire lattice

For $0\le z<1$, define
$$
 A_0(z)=\frac{1+z^4}{1-z^4},\qquad
 A_1(z)=\frac{z+z^3}{1-z^4},\qquad
 A_2(z)=\frac{2z^2}{1-z^4}.
$$
Using the four affine lattices in (L2) and (L5), one obtains
$$
 \sum_{c\in\mathcal L}z^{\|c\|_1}
 \le A_0(z)^K+2A_1(z)^K+A_2(z)^K,                            \tag{L6}
$$
and the nonzero sum is bounded by the right side minus one.
For example, the coset $r$ contributes at most
$(\sum_{q\in\mathbb Z}z^{4|q-r/4|})^K$. Summing its two geometric
tails gives $A_0,A_1,A_2,A_1$, respectively. At $z=0$ the inequalities
are understood by continuity. No restriction on relation order is present.

Use the physical kicked cat propagator and odd normalized trace from
[the return-law proof](pell_harmonic_returns.md):
$$
 U_{\epsilon,a}=e^{i\epsilon B_a}U_0,\quad
 B_a(x)=2\cos(2\pi ax/N),\quad D=(N-1)/2,\quad U_0^K=I.
$$
Its construction by Fourier transforms, chirps and dilations remains valid
at every odd $K$. For every unit $a$ it is equivalent to the kick with
Weyl vector $(q,1)$, $q=-a^2F$, and unperturbed operator $S_h^{-1}$.

In the exact Bessel expansion of $U_{\epsilon,a}^{mK}$, let
$c_j=\sum_{r=0}^{m-1}n_{r,j}$. Centrality is exactly $c\in\mathcal L$.
Put $\delta=|\epsilon|$ and $b=m\delta<1$. Modified-Bessel convolution gives
$$
 \sum_{\sum_rn_{r,j}=c_j}\prod_{r,j}|J_{n_{r,j}}(2\epsilon)|
 \le\prod_j I_{c_j}(2b)\le e^{Kb^2}b^{\|c\|_1}.
$$
Consequently the absolute weight of **all** central terms with $c\ne0$
is at most
$$
 e^{Kb^2}\{A_0(b)^K-1+2A_1(b)^K+A_2(b)^K\}.                  \tag{L7}
$$
The error from replacing normalized odd word traces by central indicators
is at most
$$
 \frac{e^{2mK\delta}}{N-1}.                                  \tag{L8}
$$
This follows from the exact centered-Weyl trace
$(N\mathbf1_{v=0}-1)/(N-1)$ and $\sum_n I_n(2\delta)=e^{2\delta}$.
Individual Weyl operators need not preserve parity; the formula is the
linear full-space trace with the odd projector.

## 3. Uniform first-return suppression

**Theorem 2.** For every odd $K\ge3$, every unit $a\bmod N$, and
$|\epsilon|=\delta\le1/10$,
$$
 \left|\operatorname{tr}_-U_{\epsilon,a}^K\right|
 \le e^{-K\delta^2/2}+3(21/100)^K+\frac{e^{2K\delta}}{N-1}.     \tag{L9}
$$
If $t_K=2K\epsilon_K^2\to t<\infty$, then, uniformly over all unit harmonics,
$$
 \operatorname{tr}_-U_{\epsilon_K,a}^K\longrightarrow e^{-t/2}.
                                                               \tag{L10}
$$
If instead $K\epsilon_K^2\to\infty$ and $|\epsilon_K|\le1/10$,
the first normalized return trace tends to zero uniformly over all units.
This includes every fixed nonzero quantum kick of magnitude at most $1/10$.

**Proof.** For $m=1$ there is exactly one assignment with $c=0$:
all Bessel indices vanish. Its coefficient is $J_0(2\delta)^K$.
Alternating scalar Bessel series, for $0\le\delta\le1/10$, give
$$
 1-\delta^2\le J_0(2\delta)
 \le1-\delta^2+\delta^4/4=(1-\delta^2/2)^2\le e^{-\delta^2},
$$
$$
 0\le J_n(2\delta)\le\delta^n/n!\quad(n\ge1),\qquad
 |J_n(2\epsilon)|\le J_0(2\delta)(2\delta)^{|n|}.              \tag{L11}
$$
The last inequality follows from $J_0\ge99/100$ and
$1/n!\le(99/100)2^n$ for $n\ge1$. The identities for negative indices
and negative $\epsilon$ give the absolute-value assertion.

Applying (L6) with $z=2\delta$ bounds the whole central absolute sum by
$J_0(2\delta)^K(A_0(z)^K+2A_1(z)^K+A_2(z)^K)$.
For $x=16\delta^4\le1/625$,
$$
 \log A_0(2\delta)\le\frac{2x}{1-x}\le\delta^2/2,\quad
 A_1(2\delta)\le5/24<21/100,\quad
 A_2(2\delta)\le25/312<21/100.
$$
Together with (L8) this proves (L9). More precisely,
$$
 \left|\operatorname{tr}_-U_{\epsilon,a}^K-J_0(2\delta)^K\right|
 \le J_0(2\delta)^K
       \{A_0(2\delta)^K-1+2A_1(2\delta)^K+A_2(2\delta)^K\}
       +\frac{e^{2K\delta}}{N-1}.                            \tag{L12}
$$
When $t_K$ is bounded, $K\delta^4=O(K^{-1})$, so (L12) tends to zero,
and $J_0(2\delta)^K\to e^{-t/2}$. Finally
$\log N=(K/2)\log\lambda+O(1)$ and $2\delta\le1/5<\log\lambda/2$;
the last term of (L9) decays exponentially. This proves both limits.

## 4. A deterministic microscopic exclusion for every unit harmonic

Let the eigenphases of $U_{\epsilon,a}$ be $x_j\in\mathbb R/\mathbb Z$,
including multiplicities. For a fixed $L>0$, use
$\phi_L(u)=L^{-1}(1-|u|/L)_+$ and the globally unfolded factorial statistic
$$
 C_D(U;\phi_L)=D^{-1}\sum_{i\ne j}\sum_{n\in\mathbb Z}
                       \phi_L(D(x_i-x_j+n)).
$$
The Fourier-positivity identity in Section 7 of
[the Floquet proof](pell_floquet_normal_form.md) implies
$$
 C_D(U;\phi_L)\ge1-\frac1L+
           2\operatorname{sinc}^2(LK/D)|\operatorname{tr}_-U^K|^2.
                                                               \tag{L13}
$$
This finite inequality assumes $D>L$, as in that proof.
Hence for any sequence of unit harmonics, any odd $K\to\infty$, and
$t_K=2K\epsilon_K^2\to t<\infty$,
$$
 \liminf C_D(U_{\epsilon_K,a_K};\phi_L)
                      \ge1-\frac1L+2e^{-t}.                  \tag{L14}
$$
The corresponding count variance in a randomly translated interval of
length $L/D$ has lower limit at least $2L^2e^{-t}$.

In particular these pair measures cannot converge vaguely to a bounded
density $\rho(u)$ with $\rho(u)\to1$ as $|u|\to\infty$.
Indeed convergence would give
$C_D(\phi_L)\to\int_{-1}^1(1-|v|)\rho(Lv)\,dv$, whose limit as
$L\to\infty$ is one, contradicting (L14). This also holds when the
definition initially uses smooth compact tests, by positivity and
approximation of the continuous triangular test.

More generally such a pair-density limit requires
$|\epsilon_K|\sqrt K\to\infty$: otherwise choose a subsequence on which
$t_K$ converges to a finite value. This necessary condition now holds
for **every unit harmonic sequence**, with no frequency-window restriction,
harmonic averaging or prime-index hypothesis.

## 5. Ordered-label geometry without factorial loss

For the rest of the note $K$ runs through odd primes, $a$ is uniform on
$$
 \mathcal A_K=\{1\le a\le\lfloor\sqrt N\rfloor:\gcd(a,N)=1\}.
$$
This is the endpoint harmonic window of the previous return theorem.

**Lemma 3.** Let $j_1<\cdots<j_\ell$ be uniform among distinct ordered
labels in $\{0,\ldots,K-1\}$, $\ell\le K/2$. A nonconstant affine form
in $j_i/K$ with integer coefficients, at least one of absolute value
at least one, lies in any interval of length $2\eta$ with probability
at most $C\ell(\eta+K^{-1})$. The same assertion holds for two independent
ordered label sets if the form is nonconstant in either set.

**Proof.** Condition on every coordinate except one with nonzero
coefficient. Its allowed integer positions form an interval of size $A$.
There are at most $2\eta K+2$ positions mapping into the prescribed
interval. Moreover
$$
 \mathbb E(A^{-1})\le
 \frac{\binom K{\ell-1}}{\binom K\ell}
 =\frac{\ell}{K-\ell+1}.                                   \tag{L15}
$$
To see this, sum over admissible choices of the other $\ell-1$ coordinates:
each has marginal weight $A/\binom K\ell$; terms with $A=0$ do not occur.
Their number is at most $\binom K{\ell-1}$. This proves the claim,
including the end coordinates. Condition on the second label set too
for the two-copy version.

Consider now any cycle-pair crossing diagram with $\ell$ labels, as
defined in the preceding return proof, and either orientation at every
chord. If there is a crossing, its ordered-grid phase average satisfies,
uniformly for $1\le\ell\le J_K=\lceil10\log K\rceil$,
$$
 \left\|\ell!K^{-\ell}\sum_{j_1<\cdots<j_\ell}
              \operatorname{phase}(a;j)\right\|_{L^2(\mathcal A_K)}
       \le C\frac{(\log K)^4}{\sqrt K}.                       \tag{L16}
$$
For a diagram without crossings the same expression is exactly
$(K)_\ell/K^\ell$, and its difference from one is at most $\ell^2/(2K)$.

Here are the uniform details of (L16). Set $\eta=(\log K)^2/K$.
Exclude configurations where an edge's circle distance is within $\eta$
of zero or $1/2$, or where two distinct edge distances are within $\eta$
of each other. In the second-moment calculation make these exclusions
jointly for both copies. Each bad event lies in a bounded number of
nontrivial affine strips with integer coefficients on at most four
endpoint variables. Distinct unordered edges have different coefficient
vectors; edges in different copies use independent coordinates.
There are $O(\ell^4)$ strips. Lemma 3 bounds their joint probability by
$C\ell^5(\eta+K^{-1})$, without an $\ell!$ penalty.

On the good set, the unique largest edge is separated by at least $\eta$.
The exact Pell phase has modulus comparable to
$\lambda^{Kd_*-K/2}$; all other at most $2J_K^2$ terms have relative
sum at most $C J_K^2\lambda^{-K\eta}=o(1)$.
For the real quadratic phase coefficient $u$ this gives
$$
 |u|\le C\lambda^{-K\eta},\qquad
 \lfloor\sqrt N\rfloor\sqrt{|u|}\ge c\lambda^{K\eta/2},
 \qquad \log(2/|u|)\le CK .
$$
The elementary quadratic differencing estimate (H13) in
`pell_harmonic_transition.md` makes the absolute harmonic average
at most $C\sqrt K\,e^{-c(\log K)^2}$.
This applies to the difference of two diagram phases in the second
moment, because the largest edge among both copies is unique.
The square root of the bad probability, plus this negligible term,
is at most the right side of (L16).

Finally the proportion of units in this prime-index window is $1-o(1)$
by (H8) of the same note. Conditioning an $L^2$ estimate divides its
squared bound by that proportion; it does not add an $O(1/\log K)$
error. The normalization $(K)_\ell/K^\ell\le1$ only improves the bound.

## 6. Uniform approximation at growing return multiplicities

**Theorem 4.** Fix $\gamma\in(0,1)$. Allow an arbitrary sequence of positive
integers $m=m_K$ and real kicks $\epsilon=\epsilon_K$. Put
$$
 t=2K\epsilon^2,\qquad s=m^2t.
$$
If $s\le(1-\gamma)\log K$ for all sufficiently large $K$, then
$$
 \left\|\operatorname{tr}_-U_{\epsilon,a}^{mK}
 -\frac{e^{-mt/2}}mL_{m-1}^{(1)}(mt)\right\|_{L^2(\mathcal A_K)}
       \longrightarrow0.                                  \tag{L17}
$$
Here $m$ need not be fixed. The comparison is absolute, not relative.

**Proof.** All constants below are independent of $m$.
Write $b=m|\epsilon|=\sqrt{s/(2K)}$.
The lattice error (L7) is bounded by
$$
 C e^{s/2+Cs^2/K}\frac{s^2}{K}
       +e^{s/2}C(2b)^K=o(1).                               \tag{L18}
$$
The correction (L8) is $e^{\sqrt{2Ks}}/(N-1)=o(1)$.
Thus only the coefficientwise-balanced arrays remain; there is no
total-order truncation.

At one site their total modified-Bessel majorant is $I_0(2b)$.
The inactive majorant is $I_0(2|\epsilon|)^m$.
The active majorant is at most $I_0(2b)-1\le b^2e^{b^2}$.
Consequently the mass with $\ell$ active sites is at most
$e^{s/2}(s/2)^\ell/\ell!$. With $J=J_K=\lceil10\log K\rceil$,
$$
 e^{s/2}\sum_{\ell>J}\frac{(s/2)^\ell}{\ell!}=o(1),           \tag{L19}
$$
uniformly in the stated range. For example, the geometric-ratio bound
and $\ell!\ge(\ell/e)^\ell$ make this $O(K^{-10})$.

The majorant of a balanced site whose total integer order is at least
four is at most
$$
 e^{m\epsilon^2}\sum_{R\ge4}\frac{(2b)^R}{R!}\le Cb^4 .
$$
Indeed the bound
$I_n(2|\epsilon|)\le e^{\epsilon^2}|\epsilon|^{|n|}/|n|!$
and the multinomial theorem dominate the order-$R$ sum by
$(2m|\epsilon|)^R/R!$; ignoring balance only enlarges it.
Marking one such site and summing all the others costs at most
$CKb^4e^{Kb^2}=Cs^2e^{s/2}/K=o(1)$.

Every surviving active site has one $+1$ and one $-1$ in different
cycles. Its signed coefficient is $-J_1(2\epsilon)^2$.
We may replace the common coefficient at $\ell\le J$ by
$(-\epsilon^2)^\ell e^{-mK\epsilon^2}$.
Uniform relative errors are $O(mK\epsilon^4+\ell\epsilon^2)$:
use $\log J_0(2\epsilon)=-\epsilon^2+O(\epsilon^4)$ and
$J_1(2\epsilon)/\epsilon=1+O(\epsilon^2)$, with the value at zero by
continuity. Since $mK\epsilon^4\le s^2/(4K)$, summing these errors with
the Poisson majorant costs at most $C(s+s^2)e^{s/2}/K=o(1)$.

There are $\binom m2^\ell$ type lists and $2^\ell$ orientations.
With the relative normalization in (L16), the total weight is bounded by
$$
 \sum_{\ell=0}^J\frac{(\binom m2 t)^\ell}{\ell!}\le e^{s/2}.
$$
Thus all crossing diagrams together contribute in $L^2$ at most
$$
 C e^{s/2}\frac{(\log K)^4}{\sqrt K}
 \le C(\log K)^4 K^{-\gamma/2}=o(1).                         \tag{L20}
$$
Replacing $(K)_\ell/K^\ell$ by one in the noncrossing diagrams costs
at most $J^2e^{s/2}/(2K)=o(1)$. Their series tail beyond $J$ has the
same bound as (L19). The exact noncrossing enumeration (R18)--(R19)
in the preceding proof sums the remaining series to
$e^{-mt/2}L_{m-1}^{(1)}(mt)/m$, for every positive integer $m$.
This proves (L17), including sequences of growing $m$.

**Corollary 5 (supercritical Haar return law).** If
$$
 t_K=2K\epsilon_K^2\longrightarrow\infty,\qquad
 t_K=o(\log K),
$$
the empirical eigenvalue measures of $U_{\epsilon_K,a}^K$ converge weakly
in probability to Haar measure on the unit circle.
For each fixed positive $m$, Theorem 4 applies and its Laguerre moment
tends to zero, since a fixed-degree polynomial times $e^{-mt_K/2}$
vanishes. Fourier approximation and compactness finish the proof.
This is a global eigenvalue law, not microscopic circular-ensemble statistics.

## 7. Why a one-step stochastic gap cannot close this proof

In the physical position basis, the metaplectic kernel for
$T=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$ is, up to
a scalar phase,
$$
 (U_0)_{xy}=N^{-1/2}e_N((3x^2-2xy+3y^2)/8).
$$
The identity follows either from the Fourier/chirp construction or by
direct Weyl covariance. All divisions are inverses modulo the odd $N$.
Multiplication by the physical kick changes only its row phases.

The orthonormal odd basis is $(e_x-e_{-x})/\sqrt2$, $1\le x\le D$.
In that basis the entry-modulus matrix $P_{xy}=|(U_{\epsilon,a}^-)_{xy}|^2$
is, for every real kick strength and every harmonic,
$$
 P=\frac2N(J-C),\qquad
 C_{xy}=\cos(2\pi\,2^{-1}xy/N),\qquad
 P^2=\frac1N I+\frac2N J.                                  \tag{L21}
$$
Here $J$ is the $D$-by-$D$ all-ones matrix.
To verify the last identity, finite character orthogonality gives
$C{\bf1}=-{\bf1}/2$ and $C^2=(N/4)I-J/2$.
Therefore the stationary vector has eigenvalue one and all other
eigenvalues of $P$ have absolute value $N^{-1/2}$. Equivalently, with
$E=J/D$,
$$
 P^{2r}=N^{-r}I+(1-N^{-r})E .
$$
This exceptionally fast stochastic mixing coexists with the deterministic
microscopic obstruction (L14). The entry-modulus chain loses the correlated
quantum phases. It is not a substitute for the fixed classical map, nor
does its gap alone imply local spectral universality.

For comparison, Gnutzmann--Altland's quantum-graph argument explicitly uses
an average over rationally independent bond phases, not only a gap of the
entry-modulus transition matrix: see equation (2) and its preceding
assumption in [arXiv:nlin/0402029v2](https://arxiv.org/pdf/nlin/0402029v2).
That phase-independence input has not been proved for the present map.

## 8. Boundary of the advance

The exact four-coset theorem removes the short-relation lifting restriction
from the Bessel analysis. The first-return suppression reaches fixed small
quantum kicks and every odd Pell index; the growing-return theorem controls
$m^2(2K\epsilon^2)$ up to a specified logarithmic scale.
These are distinct statements with distinct averaging assumptions.

For fixed critical $t>0$, (L17) permits $m$ of order $\sqrt{\log K}$,
so physical times are at most of order $K\sqrt{\log K}$.
Allowing larger $m$ by simultaneously decreasing $\epsilon$ does not
establish a Heisenberg-time theorem at a fixed perturbation strength.
At fixed nonzero classical kick strength the quantum kick is of order $N$,
far outside (L9) and (L17).

The first-return bound alone does not prove a Haar return law at fixed
nonzero quantum $\epsilon$. Corollary 5 has the additional
$t_K=o(\log K)$ restriction. Neither Haar density, rapid mixing of $P$,
nor agreement with fixed or slowly growing free Brownian moments
establishes sine-kernel/GOE correlations, level repulsion or BGS.
External novelty assessment and full formal verification remain open.
