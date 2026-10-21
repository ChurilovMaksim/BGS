> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_exact_identities_and_closure.md`. Embedded SHA256: `7fc90f4202399ff5fe4a719282ffa0723fd0eb4e16291ac891d13f164ffcd712`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Independent audit of the finite identities and Laplace closure

21 October 2026. Auditor: /root/audit_uniform_word_r4.

## Source identity, verdict, and scope

Target: root_exact_identities_and_closure.md.

SHA-256: 5f5892fd970cf395e0faef1757e9ebb3e64ea3488af6785197a5a25a7ddbe113.

The hash was recomputed. The frozen source was not modified.

**Verdict:** the finite identities and the implication
$H_{\rm diag}\Rightarrow\Xi_N\Rightarrow{\rm Sine}_2$ are correct.
Sections 1--6 below independently check the finite and analytic steps.
Section 7 supplies a detailed completion of the topological probability
paragraph, including a precisely identified published compactness theorem
and verification of its hypotheses. This completion requires no additional
spectral estimate.

There is one typesetting error in target equation (5.3):
the text $+sum_{k=2}^J$ should be $+\sum_{k=2}^J$.
The exponential braces in that formula are balanced; there is no additional
brace erratum.

The target explicitly leaves $H_{\rm diag}$ unproved. Its last section
correctly identifies a particular fixed pair test that remains unevaluated.
The closure is not itself a new universality theorem for the given family.

## 1. Fourier periodization and factorial inclusion--exclusion

For a Schwartz function $b$, the periodization and every differentiated
series converge absolutely and uniformly for fixed $N$. Changing
variables $x=N(t+\ell)$, and using $e^{2\pi im\ell}=1$ for integer
$m,\ell$, gives

$$
 \int_0^1b_N(t)e^{-2\pi imt}\,dt=N^{-1}\widehat b(m/N).
$$

Compact support of $\widehat b$ makes the resulting Fourier expansion a
finite sum at each $N$. In the product of $k$ such expansions,
integration over $\alpha$ is zero unless $\sum_a m_a=0$, with no
further factors. This proves the target normalization $1/(k!N^k)$.
The argument is valid even when Fourier frequencies exceed $N$.

For a fixed eigenvalue index, the substitutions in the intensity identity
partition the real line into shifted intervals of length $N$. Their
Jacobians are $N^{-1}$. Tonelli therefore gives intensity one after
summing the $N$ indices, regardless of multiplicities. In particular the
first factorial term is exactly $\int b$ for every deterministic spectrum.

For the partition formula, fix an index tuple with equality partition
$\sigma$. A product of traces for a partition $\pi$ includes this tuple
exactly when every block of $\pi$ lies within a block of $\sigma$.
Its coefficient after the asserted signed sum is

$$
 \prod_{B\in\sigma}
 \left[
 \sum_{\pi\in{\rm Part}(B)}
       \prod_{A\in\pi}(-1)^{|A|-1}(|A|-1)!
 \right].
$$

Inside a block of size $r$, partitions followed by the cyclic ordering
of each block enumerate permutations of $r$ letters. The displayed
product is their sign. Its sum is one for $r=1$, and zero for $r\ge2$
by the fixed-transposition sign-reversing bijection. Exactly the distinct
index tuples survive. This proves the formula for all integer frequencies,
including vanishing block sums and negative frequencies.

## 2. Haar density and the exact CUE determinant

The target's differential calculation gives the joint eigenangle density
without imposing a universality hypothesis. Here are the relevant
geometric details. On the locus of distinct eigenvalues, diagonalize
$V=WZW^*$. The invariant metric separates diagonal angle directions
from the off-diagonal complex directions of $A=W^*dW$. In each
off-diagonal plane the differential is multiplication by $z_j-z_i$;
its two-real-dimensional volume factor is $|z_j-z_i|^2$. All remaining
metric factors are independent of the angles. The finite redundancy from
ordering the eigenvalues is absorbed into normalization.

The omitted multiplicity strata have zero volume. For a multiplicity
pattern $m_1+\cdots+m_r=N$, the eigenspace parameters have real
dimension $N^2-\sum_i m_i^2$, and the distinct eigenangles contribute
$r$. A repeated pattern therefore has dimension
$N^2-\sum_i(m_i^2-1)<N^2$. Local smooth parameter charts of this lower
dimension have zero ambient volume, as is seen by a bounded-Lipschitz
covering argument on compact subcharts. There are finitely many patterns
and countably many such subcharts.

The metric is invariant under both left and right multiplication; its
normalized volume is Haar measure. To check identification with a given
normalized Haar measure directly, integrate $F(xy)$ against the two
measures: right invariance of the volume evaluates the double integral
as its integral of $F$, while left invariance of Haar evaluates it as
the Haar integral of $F$.

Expansion of the squared Vandermonde leaves exactly $N!$ equal
permutation pairs after integration. Thus the normalization is precisely
$N!^{-1}$, in the angle convention of the problem. Inserting
$\prod_a(1+t b_N(\theta_a))$ and expanding both determinants gives the
finite Gram determinant. Depending on which Vandermonde is conjugated,
the Gram matrix is $I+tT_{N,b}$ or its transpose; the determinants
coincide. The matrix in the target is exactly

$$
 (T_{N,b})_{ij}=N^{-1}\widehat b((i-j)/N).
$$

Its quadratic form is

$$
 z^*T_{N,b}z
 =N^{-1}\int_{\mathbb R}b(x)
       \left|\sum_{j=0}^{N-1}z_j e^{2\pi ijx/N}\right|^2\,dx.
$$

Hence it is positive semidefinite, its trace is $H=\int b$, and its
nonnegative eigenvalues $\lambda_j$ satisfy
$k!e_k(\lambda)\le(\sum_j\lambda_j)^k=H^k$.
Rotation invariance of the Haar density allows the extra $\alpha$
average. Comparing polynomial coefficients proves the exact CUE
factorial moment, including $e_k=0$ for $k>N$.

## 3. The one-remainder Bonferroni estimate

Write $s=\sup b<1$. For $t\in[-1/2,1/2]$, the central periodization
term is at most $s$; all other terms have sum bounded by

$$
 C_LN^{-L}\sum_{\ell\ne0}(|\ell|-1/2)^{-L},\qquad L>1.
$$

Thus $0\le b_N\le1$ for all sufficiently large $N$, uniformly in $t$.
No compact support of $b$ is being assumed here.

For $x_j\in[0,1]$, introduce independent Bernoulli indicators only to
prove the numerical product inequality. If their sum is $r\ge1$, then

$$
 \sum_{k=0}^L(-1)^k\binom rk=(-1)^L\binom{r-1}{L};
$$

for $r=0$ the sum is one. Therefore odd partial sums bound the product
from below and even partial sums from above. This use of auxiliary
indicators changes no model in the theorem.

For odd $J$, let $S_L$ be the factorial partial sums. Then
$S_J\le P\le S_{J-1}$. The first orientation of the difference is

$$
 P^U-P^C
 \le S_{J-1}^U-S_J^C
 \le\sum_{k=2}^{J-1}|\Delta_k|+M_J^C.
$$

The reverse orientation is bounded using $S_{J-1}^C-S_J^U$ and
$M_J^U=M_J^C+\Delta_J$, yielding

$$
 |P^U-P^C|\le\sum_{k=2}^J|\Delta_k|+H^J/J!.
$$

This proves exactly the desired error with only a CUE remainder.
It does not assume a bound on a deterministic moment of order $J+1$
or any uniformity as $J$ grows.

## 4. Approximation of the Laplace test

For $f\in C_c^\infty$, $f\ge0$, the function
$h=1-e^{-f}$ is nonnegative, smooth, compactly supported, and has
supremum strictly below one. If $g=\mathcal F^{-1}\varphi$ for a
nonzero $\varphi\in C_c^\infty$, then
$K=|g|^2/\int|g|^2$ is a nonnegative Schwartz function of integral one.
The convolution formula for its Fourier transform makes that transform
smooth and compactly supported.

Consequently $b_B=h*K_B$ meets every test hypothesis in $H_{\rm diag}$:
in particular its integral is the same $H=\int h$, and its Fourier
support is fixed once $B$ is fixed. Translation continuity in $L^1$
and domination by $2H K$ prove
$\|h-b_B\|_1\to0$. Here translation continuity could also be read
directly from
$\|h(\cdot-u)-h\|_1\le |u|\|h'\|_1$.

For $N$ exceeding the diameter of the support, different copies for
each individual eigenangle do not overlap. This condition concerns
copies of one angle, not separation of different eigenangles. It gives
the exact product representation of the Laplace functional even when
eigenangles have multiplicities.

For fixed $B$ and sufficiently large $N$, both periodized tests lie
in $[0,1]$. Telescoping the finite products and integrating the sum
of absolute differences over $\alpha$ gives

$$
 |P_N(h)-P_N(b_B)|
 \le\int_{\mathbb R}|h-b_B|.
$$

The same inequality survives Haar averaging. Therefore the correct
version of target equation (5.3) is

$$
 \begin{aligned}
 &\left|
 \mathbb E_\alpha e^{-\langle f,\Xi_N\rangle}
 -\mathbb E_{\rm CUE}e^{-\langle f,\Xi_N^{\rm CUE}\rangle}
 \right|\\
 &\hspace{1cm}\le
 2\|h-b_B\|_1+\sum_{k=2}^J|\Delta_{k,N}(b_B)|+H^J/J!.
 \end{aligned}
 \tag{4.1}
$$

One first fixes a sufficiently large finite $B$, then an odd finite
$J$, and only then lets all odd $N$ tend to infinity. All uses of
$H_{\rm diag}$ concern fixed admissible tests and finitely many fixed
orders. The case $H=0$ is immediate.

## 5. CUE local limit and the factorial series

To derive the CUE $k$-point density from the joint density, expand the
Vandermonde along the $k$ nonintegrated columns. Orthogonality of the
other columns retains equal complementary index sets and contributes
$(N-k)!$. The remaining sum of squared $k$-minors is the determinant
of the rank-$N$ projection kernel, by expansion of the determinants.
After scaling, on an interval of diameter less than $N$, this gives

$$
 K_N(x,y)=\frac1N\sum_{j=0}^{N-1}e^{2\pi ij(x-y)/N}.
$$

The interval condition ensures that two different periodic copies of one
eigenangle cannot be selected in that local observation. The claim is
not that the unfolded process has this determinantal description on
arbitrarily large intervals at fixed $N$.

The phase factor in the sine-quotient formula cancels from every
determinant. The remaining quotient converges uniformly on each fixed
compact set, including the continuous diagonal value one. Both the
finite kernels and the limiting sine kernel are Gram kernels with
diagonal one. For the limit, a Gram representation is

$$
 K(x,y)=\int_{-1/2}^{1/2}e^{2\pi i\xi(x-y)}\,d\xi.
$$

Their factorial determinants lie in $[0,1]$. With $h=1-e^{-f}$, each
factorial integral divided by $k!$ is bounded by $H^k/k!$. For a
fixed large $N$, the compactly supported observation involves at most
$N$ points, so the product expansion is finite and the determinants
vanish for $k>N$. For the Sine process, local finiteness makes the
random product finite almost surely, and the sum of expected absolute
factorial terms is at most $e^H$ by Tonelli and the same determinant
bound. Thus this series really is its Laplace functional.

Dominated convergence for each integral and then for the series proves
the asserted CUE local Laplace limit. Combining it with (4.1) proves
Laplace convergence for the deterministic family if $H_{\rm diag}$
holds.

## 6. The explicit pair test and the remaining spectral estimate

The target's function

$$
 \varphi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
 I=\int\varphi,\quad
 u=\mathcal F^{-1}\varphi,\quad
 b_*=\frac{|u|^2}{2I^2}
$$

is admissible. Indeed $\varphi$ is real, even, nonnegative, smooth and
compactly supported; $I>0$; and $|u(x)|\le I=u(0)$. Thus
$\sup b_*=1/2$, and
$\widehat b_*=(\varphi*\varphi)/(2I^2)$ is smooth with support
in $[-2,2]$. It vanishes at the two endpoints.

For $m\ne0$, integrating the CUE pair kernel against
$e^{2\pi im(\theta-\phi)}$ yields $N-(N-|m|)_+=\min(|m|,N)$.
The constant-density piece contributes zero to the off-diagonal integral
for such $m$. At zero frequency the deterministic and CUE terms agree.
The two signs of $m$ cancel the factor $1/2$ in the pair factorial
normalization. Therefore, with $w=|\widehat b_*|^2$,

$$
 \Delta_{2,N}(b_*)=
 \frac1{N^2}\sum_{1\le n<2N}w(n/N)
      \bigl(|\operatorname{Tr}U_N^n|^2-\min(n,N)\bigr).
 \tag{6.1}
$$

Neither convergence of (6.1) to zero along all odd $N$, nor a fixed
positive lower bound along an infinite subsequence, follows from the
audited closure. This remains an explicit first unproved spectral
estimate. Higher factorial orders would still be necessary after it.

## 7. Completion of the topological probability argument

This section makes explicit the short final paragraph of target
Section 6. It proves the needed properties of the state space and the
uniqueness of the limiting law. The only probability compactness theorem
used is identified in Section 7.4.

### 7.1 A countable complete metric for the vague state space

Let $E$ be the set of locally finite positive integer-valued point
measures on $\mathbb R$, allowing multiplicities. Choose a countable
family $f_m\in C_c^\infty(\mathbb R)$, $f_m\ge0$, which is uniformly
dense for nonnegative compactly supported continuous tests, with
approximations supported in a common larger compact interval. Such a
family exists by separability of continuous functions on each compact
interval, followed by nonnegative smooth approximation and a countable
union over the intervals. Include cutoffs $\chi_r$ that are at least
one on $[-r,r]$ and supported in $(-r-1,r+1)$.

Define

$$
 d(\mu,\nu)=\sum_{m\ge1}2^{-m}
       \min\{1,|\langle f_m,\mu\rangle-\langle f_m,\nu\rangle|\}.
 \tag{7.1}
$$

The tests separate point measures: an isolated atom whose mass differs
can be detected by a bump, and uniform approximation in a fixed compact
set preserves detection. Hence (7.1) is a metric.

Vague convergence implies convergence in this metric by convergence of
each coordinate and control of the geometric tail. Conversely, convergence
in the metric bounds the cutoff integrals and hence the local masses.
Approximate an arbitrary nonnegative continuous compactly supported test
uniformly, in one fixed larger compact set, by the $f_m$. The local mass
bound controls the approximation error and gives convergence of its
integrals. Splitting a real test into positive and negative parts then
gives vague convergence. Equivalently, this sequential argument proves
continuity of every test functional on the metric space, while the
geometrically convergent series in (7.1) is vaguely continuous with one
argument fixed. Thus this metric has precisely the vague topology.

Finite point measures with rational atom positions form a countable dense
subset: truncate any locally finite measure on increasingly large
intervals and approximate its finitely many atoms by rational points.
Therefore $E$ is separable.

Here is also a direct proof of completeness. For a $d$-Cauchy sequence,
each cutoff coordinate is a real Cauchy sequence, so its supremum is finite.
Consequently all local masses are uniformly bounded. The compactness
construction in the next paragraph extracts a vaguely convergent
subsequence with limit in $E$. Since the whole sequence is $d$-Cauchy,
it converges to the same limit in $d$. Hence $d$ is complete.

### 7.2 Deterministic compact sets and preservation of integer masses

Consider any sequence of point measures with a uniform mass bound on
each interval $[-r,r]$. On a fixed such interval, measures with at most
an integer $L$ atoms, counted with multiplicity, form a compact space:
they are the continuous image of the finite disjoint union of
$[-r,r]^j$, $0\le j\le L$, under the map sending a tuple to its
sum of unit atoms. Thus a diagonal extraction makes the restrictions
converge weakly on every $[-r,r]$, to a finite integer-valued measure
$\nu_r$.

Boundary atoms cause no inconsistency. For $s>r$, tests supported in
$(-r,r)$ show
$\nu_s|_{(-r,r)}=\nu_r|_{(-r,r)}$. These restrictions therefore patch
to a locally finite integer-valued measure $\nu$ on the whole real
line. Every compactly supported test lies in one of these open interiors,
so the extracted sequence converges vaguely to $\nu$.

For positive finite bounds $L_r$, the set

$$
 {\cal K}=\{\mu\in E:\langle\chi_r,\mu\rangle\le L_r
                       \text{ for every }r\ge1\}
 \tag{7.2}
$$

is closed for the vague metric, and the preceding extraction applies to
every sequence in it. Hence it is compact, since in a metric space
sequential compactness and compactness coincide. This also supplies the
compactness assertion used in the completeness proof.

### 7.3 Uniform tightness from exact intensity

For the random point measures in the problem,

$$
 \mathbb E\langle\chi_r,\Xi_N\rangle=H_r:=\int\chi_r<\infty.
$$

Fix $\varepsilon>0$ and put
$L_r=2^{r+1}H_r/\varepsilon$. Markov's inequality and the union bound
give, uniformly in $N$,

$$
 \mathbb P(\Xi_N\notin{\cal K})
 \le\sum_{r\ge1}\frac{H_r}{L_r}
 =\varepsilon/2<\varepsilon.
 \tag{7.3}
$$

The compact set (7.2) therefore proves tightness of the laws. The random
measures are Borel measurable: at each fixed $N$, all smooth compactly
supported coordinate integrals are measurable functions of the angles
and of $\alpha$, with only finitely many relevant copies on the compact
observation. These coordinates generate the vague Borel sigma-field,
as also verified below.

### 7.4 Exact published compactness theorem and its hypotheses

The probability theorem used here is Patrick Billingsley,
*Weak Convergence of Measures: Applications in Probability*,
Society for Industrial and Applied Mathematics, Philadelphia, 1971,
**Theorem 4.1, printed page 10**. It identifies tightness with relative
sequential weak compactness of probability measures. The standing state
space assumptions, **separability and completeness**, are stated in
Section 2 on printed page 2.

The original publication was directly checked, including images of the
two relevant pages:

https://www.math.ucdavis.edu/~gravner/MAT236A/materials/Billingsley-paper.pdf

The PDF indices of printed pages 2 and 10 are 7 and 15, respectively.
This is the 1971 SIAM text; no theorem number from a different edition of
Billingsley's other book is being substituted.

Sections 7.1--7.3 above verify the complete separable metric state space,
the Borel probability laws, and the tightness hypothesis. The theorem
therefore gives a weakly convergent further subsequence of every sequence
of these laws, with its limit a probability law on $E$.

### 7.5 Uniqueness from the stated smooth Laplace tests

Suppose two probability laws on $E$ have the same Laplace functional
for every nonnegative $C_c^\infty$ test. Fix finitely many such tests
$f_1,\ldots,f_k$, and under either law set

$$
 Y_j=e^{-\langle f_j,\mu\rangle}\in(0,1].
$$

For all nonnegative integers $a_1,\ldots,a_k$,

$$
 \mathbb E\prod_jY_j^{a_j}
 =\mathbb E e^{-\langle\sum_j a_jf_j,\mu\rangle}.
$$

Thus the two distributions on $[0,1]^k$ have all polynomial moments
equal. To see directly that this determines the distribution, for
continuous $F$ use the multivariate Bernstein polynomials

$$
 B_mF(y)=
 \sum_{a_1,\ldots,a_k=0}^m
 F(a_1/m,\ldots,a_k/m)
 \prod_{j=1}^k\binom m{a_j}y_j^{a_j}(1-y_j)^{m-a_j}.
$$

They converge uniformly to $F$. Indeed this expression is the expectation
of $F$ at independent binomial averages; their variances are at most
$1/(4m)$. Uniform continuity of $F$ and the union bound show that,
for any fixed $u>0$, the uniform approximation error is at most its
modulus of continuity at $u$, plus
$2\|F\|_\infty k/(4mu^2)$. Let $m$ and then $u^{-1}$ tend to infinity.

Consequently the two laws integrate every continuous $F$ equally.
Their probabilities of closed subsets agree by the continuous
approximants
$\max(0,1-m\,{\rm dist}(y,A))$ to the indicator of a closed set $A$.
Closed sets generate the Borel sigma-field, so the distributions agree.
Applying the Borel inverse $-\log$ on $(0,1]^k$ proves equality of
the joint distributions of the coordinate integrals.

Use now the countable test family from Section 7.1. Its coordinates
generate the Borel sigma-field of $E$: coordinates are continuous, and
metric balls are measurable functions of their countable list; separability
supplies a countable base of such balls. Equality of all finite coordinate
distributions therefore gives equality of the probability laws on the
pi-system of cylinders and hence on its generated sigma-field. For
completeness, that last measure-theoretic extension follows from the
pi--lambda argument: the class of sets on which two finite probability
measures agree is a lambda-system. The smallest lambda-system containing
a pi-system is closed under intersections. To verify this, first fix a
set from the pi-system and apply the lambda-system property to the class
of sets whose intersection with it lies in the smallest lambda-system;
then fix an arbitrary set in the smallest lambda-system and repeat.
Closure under intersections together with the lambda-system properties
makes it a sigma-field. Therefore equality extends to the whole generated
sigma-field. This also justifies the closed-set uniqueness used above.
The needed Laplace uniqueness consequently requires no moment determinacy
or uniform-integrability assumption.

### 7.6 Concluding weak convergence

For every smooth compactly supported nonnegative $f$, the function
$\mu\mapsto e^{-\langle f,\mu\rangle}$ is bounded and vaguely continuous.
Any weak subsequential limit supplied by Section 7.4 therefore inherits
the Laplace limit already proved in Sections 4--5. By Section 7.5 its law
is exactly that of ${\rm Sine}_2$.

Finally, if the full sequence of laws did not converge to this law, one
bounded continuous function and a subsequence would witness a fixed
failure of convergence of integrals. Tightness would supply a further
weakly convergent subsequence; its identified limit contradicts that
failure. Thus the full sequence converges. This argument applies to
the sequence of all odd dimensions and introduces no averaging over
dimensions, kicks, or phases.
