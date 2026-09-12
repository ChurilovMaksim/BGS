# Two return transitions for an even-period kicked cat map

**Research status.** Project proof with explicit remainder estimates.
Independent review and priority verification are outstanding. The harmonic
below depends on the dimension and is close to half the lattice frequency.
This is not a result for a fixed smooth classical perturbation or a resolution
of generic BGS. The note is a research checkpoint, not a manuscript release.

The final statement is Theorem 4, equations (S29)--(S31): both return
asymptotics for every vanishing kick, including the transition governed by
$K\epsilon^4$. Sections 1--9 establish the lattice bounds, spin law,
and critical limit used in that proof.

## 1. The deterministic family and the result

Fix
$$
 A=\begin{pmatrix}3&4\\2&3\end{pmatrix},\quad
 \lambda=3+2\sqrt2,\quad v_j=A^j(1,0).
$$
Let $b_0=0,b_1=1,b_{j+1}=6b_j-b_{j-1}$. For odd $m\ge3$ set
$$
 K=2m,\qquad N=b_m,\qquad D=(N-1)/2,\qquad a=(N+1)/2.         \tag{S1}
$$
Thus $K=6,10,14,\ldots$ and $N=35,1189,40391,\ldots$.
Both $N$ and $a$ are units relative to $2$ and $N$, respectively.
Let $U_0W(w)U_0^{-1}=W(Aw)$, with the centered convention of
[the pressure note](hyperbolic_return_pressure.md), and choose its scalar
phase so that $U_0^K=I$. Define
$$
 U_{\epsilon}=e^{2i\epsilon\cos(2\pi ax/N)}U_0.                \tag{S2}
$$
Normalized traces are on the full odd parity subspace.

**Theorem.** For any real sequence satisfying
$$
 K\epsilon_K^2\longrightarrow\infty,\qquad
 K\epsilon_K^4\longrightarrow0,                              \tag{S3}
$$
one has, deterministically,
$$
 \operatorname{tr}_-U_{\epsilon_K}^K\longrightarrow0,\qquad
 \operatorname{tr}_-U_{\epsilon_K}^{2K}\longrightarrow-\frac12.
                                                               \tag{S4}
$$
For example $\epsilon_K=K^{-1/3}$ satisfies (S3).
The second conclusion rules out a bounded, unit-tail microscopic pair
density under global mean unfolding, as proved in Section 6.

This strengthens the project's earlier necessary first-return criterion:
the condition $|\epsilon|\sqrt K\to\infty$ alone is not sufficient to
remove microscopic obstructions when arbitrary dimension-dependent
harmonics are allowed.

There is a quantitative finite-parameter version. For $0\le z\le3/10$
define
$$
 G_K(z)=e^{5Kz^8}-1+2(13/50)^K+31(3/5)^K.
$$
For real $\delta=|\epsilon|\le1/10$,
$$
 \left|\operatorname{tr}_-U_\epsilon^K-J_0(2\epsilon)^K\right|
 \le G_K(2\delta)+\frac{e^{2K\delta}}{N-1},                  \tag{S5}
$$
$$
 \left|\operatorname{tr}_-U_\epsilon^{2K}
       +\frac12-J_0(4\epsilon)^{K/2}
                    -\frac12J_0(4\epsilon)^K\right|
 \le2\sqrt2\pi K\delta^4+G_K(3\delta)
                         +\frac{e^{4K\delta}}{N-1}.         \tag{S6}
$$
In particular, if $t_K=2K\epsilon_K^2\to t<\infty$, the second
trace tends to $e^{-t}+\tfrac12e^{-2t}-\tfrac12$.
Formula (S6) also covers $t_K\to\infty$ with $t_K=o(\sqrt K)$.

## 2. The even-period lattice has only 32 quotient classes

Cayley--Hamilton gives $A^j=b_jA-b_{j-1}I$. Since
$b_m=0$ modulo $N$, $A^m=-b_{m-1}I$ there. The determinant
identity $b_{m-1}^2-b_mb_{m-2}=1$ implies $A^K=I$ modulo $N$.
Thus the quantum normalization in (S2) exists. The oddness of $N$
follows from $b_j\equiv j\pmod2$ and odd $m$.

For the cyclic matrix $L=S+S^{-1}-6I$ on $\mathbb Z^K$ let
$$
 \mathcal C=\{c:\sum_jc_jv_j=0\bmod N\}.
$$
The two vectors $v_0,v_1$ have determinant $2$, a unit modulo $N$.
Hence $\mathcal C$ has index $N^2$. Also $L\mathbb Z^K\subset\mathcal C$
and
$$
 |\det L|=\lambda^K+\lambda^{-K}-2=32N^2.
$$
Consequently
$$
 |\mathcal C/L\mathbb Z^K|=32.                               \tag{S7}
$$
In fact every class has a representative constant on each parity.
Since $\det(A^2-I)=-32$ is a unit modulo odd $N$, each of
$\sum_{j\ {\rm even}}A^jv_0$ and
$\sum_{j\ {\rm odd}}A^jv_0$ vanishes modulo $N$.
On parity-constant vectors the recurrence is
$B=\left(\begin{smallmatrix}-6&2\\2&-6\end{smallmatrix}\right)$.
The group $\mathbb Z^2/B\mathbb Z^2$ has order 32 and maps injectively
to $\mathcal C/L\mathbb Z^K$: if a parity-constant forcing has an
integer preimage, uniqueness of $L^{-1}$ makes that preimage parity-constant
as well. The map is therefore onto by (S7).

Representatives of the forcing are $(r,s)$ with $0\le r<16$,
$0\le s<2$, since a column Hermite basis of $B$ is
$\left(\begin{smallmatrix}16&10\\0&2\end{smallmatrix}\right)$.
The corresponding fractional preimage is
$$
 p_{\rm even}=-(3r+s)/16,\qquad p_{\rm odd}=-(r+3s)/16
                                                    \pmod1 .
$$
The distinct nonzero pairs of absolute fractional numerators, disregarding
order, are
$$
 (0,8),(1,3),(1,5),(2,2),(2,6),(3,7),(4,4),(5,7),(6,6),(8,8).
$$
In particular every noninteger class has $\|Lp\|_1\ge K/2$.

To sum the classes, put $x=z^{1/4}$ and
$H_j(x)=(x^j+x^{16-j})/(1-x^{16})$.
The inequality $\|Lp\|_1\ge4\|p\|_1$ bounds the class with numerator
pair $(i,j)$ by $[H_i(x)H_j(x)]^{K/2}$.
For $z\le3/10$, $x<3/4$. Each shifted sum increases with $x$.
Checking the ten displayed pairs at the rational point $x=3/4$ gives
$$
 \max H_i(3/4)H_j(3/4)
 =H_1(3/4)H_3(3/4)
 =\frac{10040323357589760}{28926125721773329}<\frac9{25}.
$$
Thus all 31 noninteger classes have total weight at most
$31(3/5)^K$. This finite quotient calculation supplies an explicit
uniform bound; it is not an asymptotic inference from small matrices.

For the integer class use the interval decomposition from the pressure
note, now with positive weights $z^{\|Lp\|_1}$. Put
$v=2z^4/(1-z^4)$. The sum of activities of intervals starting at a
specified site is at most
$$
 B(z)=z^4\frac{2v+4v^2}{1-4v}
     =\frac{4z^8(1+3z^4)}{(1-z^4)(1-9z^4)}
     \le5z^8.                                               \tag{S8}
$$
The partition sum of disjoint intervals is bounded by the partition
sum allowing every subset, hence by $\exp(KB(z))$.
Configurations with no adjacent zeros have weight at most
$2(2\sqrt v)^K$. Subtract the all-zero configuration.

For $z\le3/10$, $2\sqrt v<13/50$. Combining these estimates proves
$$
 \sum_{c\in\mathcal C,\ c\ne0}z^{\|c\|_1}\le G_K(z).          \tag{S9}
$$
All orders and all quotient classes have been included.

## 3. The zero-aggregate part is an exact probability expectation

Expand two periods by
$e^{i\epsilon(W+W^{-1})}=\sum_n i^nJ_n(2\epsilon)W^n$.
Write the two indices at site $j$ as $x_j$ and $y_j$.
The aggregate $c=x+y$ must lie in $\mathcal C$ for the central part.
For real $\epsilon$ put
$$
 A_c=\sum_{n\in\mathbb Z}|J_n(2\epsilon)J_{c-n}(2\epsilon)|.
$$
Parseval gives $A_0=\sum_nJ_n(2\epsilon)^2=1$.
For $c\ne0$, the modified-Bessel convolution and its series give
$$
 A_c\le I_{|c|}(4\delta)
 \le e^{4\delta^2}\frac{(2\delta)^{|c|}}{|c|!}
 \le(3\delta)^{|c|},\qquad \delta\le1/10.                    \tag{S10}
$$
Thus (S9) bounds every nonzero aggregate by $G_K(3\delta)$.
This uses the exact value $A_0=1$; replacing it by an exponential
majorant would destroy the useful growing-time range.

The remaining aggregate is $y=-x$. Let $X_j$ be independent integer
variables with
$$
 \Pr(X_j=n)=J_n(2\epsilon)^2.
$$
The cross phase between the two entire blocks vanishes because their
total Weyl vectors are opposite. Each within-block phase is the same.
Since $\omega(v_i,v_j)=2b_{j-i}$, the zero-aggregate contribution is
exactly
$$
 Q_K=\mathbb E\left[
 (-1)^{\sum_jX_j}
 e_N\left(2a^2\sum_{i<j}X_iX_j b_{j-i}\right)\right].        \tag{S11}
$$
The odd-projection error is at most $e^{4K\delta}/(N-1)$,
by the absolute mass of the full Fourier--Bessel series.

Our harmonic is chosen so that $2a^2=2^{-1}$ modulo $N$.
For $1\le d<K$, let $d_*=\min(d,K-d)$. The relations
$b_{K-d}=-b_d$ modulo $N$ and $b_d\equiv d\pmod2$ show that
$$
 e_N(2^{-1}b_d)=(-1)^d e^{i\eta_d},\qquad
 |\eta_d|=\pi b_{d_*}/N.                                   \tag{S12}
$$
At $d=K/2$ either sign of the angle $\pi$ is permissible.
Crucially, $K$ is even, so wrapping a distance preserves its parity.

The identity
$b_j=(\lambda^j-\lambda^{-j})/(4\sqrt2)$ gives
$b_d/N\le\lambda^{d-m}$ for $d<m$. Therefore
$$
 \sum_{d=1}^{K-1}(K-d)|\eta_d|
 \le\pi K\left(\frac12+\frac1{\lambda-1}\right)
 =\frac{\pi K}{\sqrt2}.                                    \tag{S13}
$$
Parseval applied to the derivative of $e^{2i\epsilon\cos x}$ gives
$\mathbb E X_j^2=2\epsilon^2$. Since $|X_j|\le X_j^2$,
the telescoping product inequality and independence imply
$$
 \left|Q_K-
  \mathbb E(-1)^{\sum_jX_j+\sum_{i<j}(j-i)X_iX_j}\right|
 \le\frac{\pi K}{\sqrt2}(\mathbb E|X_0|)^2
 \le2\sqrt2\pi K\epsilon^4.                                 \tag{S14}
$$
This is a direct expectation estimate. It has no diagram-order cutoff
and no factorial or exceptional-spacing loss.

## 4. A two-parity calculation closes the second return

Let $P=\sum_{j\ {\rm even}}X_j$ and
$Q=\sum_{j\ {\rm odd}}X_j$, reduced modulo two.
The exponent in the expectation in (S14) equals $P+Q+PQ$ modulo two.
Its sign is $+1$ only when both parities are even, and $-1$ otherwise.
The Bessel addition identity gives
$$
 \mathbb E(-1)^{X_0}=J_0(4\epsilon).
$$
There are exactly $K/2$ independent variables in each class, so
$$
 \mathbb E(-1)^{P+Q+PQ}
 =2\left(\frac{1+J_0(4\epsilon)^{K/2}}2\right)^2-1
 =-\frac12+J_0(4\epsilon)^{K/2}
                      +\frac12J_0(4\epsilon)^K.             \tag{S15}
$$
Combining (S9)--(S15) proves (S6).

For one period the zero Fourier index has coefficient $J_0(2\epsilon)^K$.
The bound $|J_n(2\epsilon)|/J_0(2\epsilon)\le(2\delta)^{|n|}$
and (S9) give (S5). Under (S3), $K\delta^8\to0$, all geometric
remainders vanish, and $e^{4K\delta}/(N-1)\to0$ because
$\log N=(K/2)\log\lambda+O(1)$ and $\delta\to0$.
Finally $\log J_0(2\epsilon)=-\epsilon^2+O(\epsilon^4)$ and
$\log J_0(4\epsilon)=-4\epsilon^2+O(\epsilon^4)$.
These facts prove both limits in (S4).

The value $-1/2$ also belongs to an all-moment return law, proved next.
Its growing-time range is narrower than the direct second-moment range
in (S3). No joint stochastic-process convergence is asserted.

## 5. The complete return law in a slower growing-time range

For a nonnegative integer or half-integer $j$, set
$$
 H_j(t)=\sum_{\ell=-j}^{j}e^{-t(j(j+1)-\ell^2)},\qquad
 H_{-1/2}(t)=0,\qquad
 F_r(t)=\frac{H_{r/2}(t)-H_{r/2-1}(t)}2\quad(r\ge1).         \tag{S17}
$$
The sums advance in steps of one. Thus
$F_1(t)=e^{-t/2}$ and
$F_2(t)=e^{-t}+\tfrac12e^{-2t}-\tfrac12$.

**Theorem 2.** If $t_K=2K\epsilon_K^2=o(\log K)$, then for every
fixed positive integer $r$,
$$
 \operatorname{tr}_-U_{\epsilon_K}^{rK}-F_r(t_K)\longrightarrow0.
                                                               \tag{S18}
$$
If also $t_K\to\infty$, the empirical eigenphase measure of
$U_{\epsilon_K}^K$ converges weakly to
$$
 d\mu_\infty(\theta)=\frac{1-\cos(2\theta)}{2\pi}\,d\theta.
                                                               \tag{S19}
$$
This is the averaged fundamental eigenphase measure of Haar $SU(2)$,
and it is not the uniform circle measure. For $t_K\to t<\infty$,
the corresponding limiting measure has Fourier moments $F_r(t)$.

**Proof: reduction to two by two matrices.**
Let $\alpha_j$ be independent uniform angles and put
$$
 \widetilde W_j=e^{i\alpha_j}\sigma_{\nu(j)},\qquad
 \nu(j)=x\ {\rm for\ even}\ j,\quad z\ {\rm for\ odd}\ j.
$$
The Pauli matrices give
$\widetilde W_i\widetilde W_j
 =(-1)^{j-i}\widetilde W_j\widetilde W_i$.
Integration over each angle kills every nonzero aggregate Fourier index
at that site. Consequently the ideal zero-aggregate series is exactly
$$
 \mathbb E\,\frac12\operatorname{Tr}V_K^r,\qquad
 V_K=\prod_{j=0}^{K-1}e^{i\epsilon \xi_j\sigma_{\nu(j)}},
 \quad \xi_j=2\cos\alpha_j.                                 \tag{S20}
$$

Here are bounds justifying replacement of the quantum series.
For $r$ periods, convolution gives
$$
 \sum_{\sum_{\nu=1}^r n_\nu=c}
                  \prod_\nu |J_{n_\nu}(2\epsilon)|
 \le I_c(2r\delta)
 \le e^{r^2\delta^2}(r\delta)^{|c|}/|c|!.
$$
Thus the nonzero aggregate error is at most
$e^{r^2K\delta^2}G_K(r\delta)$, eventually $r\delta\le3/10$.

To compare phases in the zero-aggregate terms, reorder the word by site.
The difference between the actual commutator and the Pauli commutator
is the angle $\eta_{j-i}$ of (S12). If
$S_j=\sum_\nu|n_{\nu,j}|$, the total phase discrepancy is bounded by
$\sum_{i<j}|\eta_{j-i}|S_iS_j$.
The unweighted one-site absolute mass is at most $I_0(2r\delta)$.
The mass with an extra factor $S_j$ is at most
$$
 \delta\frac{d}{d\delta}I_0(2r\delta)
   =2r\delta I_1(2r\delta)
   \le2r^2\delta^2e^{r^2\delta^2}.
$$
The first inequality follows term by term from the positive Bessel
series: its power of $\delta$ is at least $\sum_\nu|n_\nu|$.
By (S13) the entire phase error is therefore at most
$$
 2\sqrt2\pi r^4K\delta^4 e^{r^2K\delta^2}.                   \tag{S21}
$$
The remaining odd-projection error is $e^{2rK\delta}/(N-1)$.
When $t_K=o(\log K)$, all these errors tend to zero: for example
$e^{r^2t_K/2}K\delta^4=K^{-1+o(1)}O(t_K^2)$ and
$e^{r^2t_K/2}K\delta^8=K^{-3+o(1)}O(t_K^4)$.

**Proof: exact representation averages.**
In the spin-$j$ representation write $J_x,J_y,J_z$ for the usual
Hermitian angular momentum matrices:
$J_x^2+J_y^2+J_z^2=j(j+1)I$ and the eigenvalues of $J_y$ are
$-j,-j+1,\ldots,j$. Concretely, in the basis indexed by $\ell$,
$J_z$ is diagonal with entries $\ell$ and
$J_+e_\ell=\sqrt{(j-\ell)(j+\ell+1)}e_{\ell+1}$;
$J_x=(J_++J_+^*)/2$ and $J_y=(J_+-J_+^*)/(2i)$.
These formulas also directly verify the Casimir identity.
Since $\xi=2\cos\alpha$,
$$
 \mathbb E D_j(e^{i\epsilon\xi\sigma_\nu})=J_0(4\epsilon J_\nu).
$$
Independence of successive increments yields
$$
 \mathbb E D_j(V_K)
   =[J_0(4\epsilon J_x)J_0(4\epsilon J_z)]^{K/2}.             \tag{S22}
$$
For fixed $j$ one pair is
$I-4\epsilon^2(J_x^2+J_z^2)+O_j(\epsilon^4)$.
Each averaged rotation is a contraction. The exponential
$e^{-4\epsilon^2(J_x^2+J_z^2)}$ is a contraction too.
A telescoping product estimate therefore compares (S22) with
$e^{-t_K(J_x^2+J_z^2)}$ with error $O_j(K\epsilon^4)$,
uniformly in $t_K$. Taking traces gives $H_j(t_K)$.

For any $g\in SU(2)$ with eigenvalues $e^{\pm i\theta}$, the elementary
character identity is
$$
 \tfrac12\operatorname{Tr}(g^r)
  =\cos(r\theta)=\tfrac12(\chi_{r/2}(g)-\chi_{r/2-1}(g)).
$$
This follows by subtracting the two finite geometric character sums.
Combining it with (S20)--(S22) proves (S18).

For $j>0$, $j(j+1)-\ell^2\ge j>0$. Thus as $t\to\infty$ all
$H_j(t)$ with $j>0$ vanish, while $H_0=1$. The limiting moments
are $F_2=-1/2$ and $F_r=0$ for $r\ne2$. These are precisely the
Fourier coefficients of (S19). Trigonometric polynomial approximation
on the compact circle proves weak convergence. The same argument
establishes the fixed-$t$ assertion; existence of its probability measure
also follows from the positive probability measures in (S20).

## 6. A microscopic obstruction and its precise scope

Let $x_1,\ldots,x_D$ be the eigenphases of $U_\epsilon$ on a circle
of circumference $D$. For fixed $L>0$ take
$\phi_L(s)=L^{-1}(1-|s|/L)_+$. Define the globally unfolded pair statistic
$$
 C_D(\phi_L)=\frac1D\sum_{i\ne j}\sum_{r\in\mathbb Z}
                         \phi_L(x_i-x_j+rD).
$$
Write $\operatorname{sinc}(u)=\sin(\pi u)/(\pi u)$, continuously
extended by one at zero. For $D>L$, its Fourier identity is
$$
 C_D(\phi_L)=1-\frac1L+
 2\sum_{n\ge1}\operatorname{sinc}^2(Ln/D)
                       |\operatorname{tr}_-U_\epsilon^n|^2.
$$
All summands are nonnegative. Keeping $n=2K$, using $K/D\to0$
and (S4), gives
$$
 \liminf C_D(\phi_L)\ge\frac32-\frac1L.                       \tag{S16}
$$
If a bounded pair density $\rho(s)$ with $\rho(s)\to1$ at infinity
were a limit for all these fixed tests, then
$\int\phi_L(s)\rho(s)\,ds\to1$ as $L\to\infty$.
This contradicts (S16). No random harmonic average is involved.

This obstruction also coexists with rapid mixing of the stochastic matrix
of quantum transition probabilities. In the odd position basis,
$$
 P_{xy}=|U_{\epsilon,xy}|^2
       =\frac2N\left(1-\cos(2\pi xy/N)\right),\qquad
 P^2=\frac1N I+\frac2N\mathbf1\mathbf1^{\mathsf T}.
$$
The first identity follows by subtracting the two parity-related quadratic
kernels with denominator four; the second follows by finite cosine
orthogonality. Thus every nonconstant eigenvalue of $P$ has absolute value
$N^{-1/2}$, independently of the kick. This auxiliary stochastic mixing
statement is not a proof of uniform classical hyperbolicity for the
dimension-dependent perturbed map.

The limitation matters. The physical kick in (S2) is
$$
 2\cos(2\pi ax/N)=2(-1)^x\cos(\pi x/N)
$$
on integer position sites. It explicitly carries lattice-parity
oscillations. Although $\|U_{\epsilon_K}-U_0\|\to0$ and hence a
leading Egorov statement with error $o(1)$ survives, this is not
quantization by one fixed smooth semiclassical symbol.
The classical map obtained by assigning a dimension-dependent oscillatory
kick has not been proved uniformly Anosov.

Accordingly (S16) is a counterexample to universality under weak
quantization/first-return criteria, not a counterexample to a properly
specified generic BGS statement for a fixed smooth system.
Whether an analogous persistent higher return occurs for a fixed smooth
harmonic in the supercritical regime remains unresolved.

## 7. Checks and experiment, with their limits

The companion script
[even_period_spin_resonance.py](../computations/verification/even_period_spin_resonance.py)
checks the 32 quotient classes and their bound with rational arithmetic,
729 complete two-block Weyl words, and 1,000 seeded multiblock Weyl/Pauli
identities. Direct physical matrices cover $N=35,1189$ at two kick
strengths. Twelve finite spin-representation calculations independently
compare the matrix product in (S22) with its character formula.
These bounded checks support the algebra; they do not prove its
asymptotic extension or establish priority.

The sparse experiment samples (S11), using (S15) as a control variate.
It replaces the omitted Bessel tail by zero with an explicit tail bound.
The deterministic bound (S9) accounts for **all** nonzero aggregates;
it is not estimated by Monte Carlo.
At $K=10002$, $t=8$, $N=b_{5001}$ has $\log_{10}N\approx3827.77$.
With 30,000 samples the zero-aggregate estimate was
$-0.49652-0.00025i$. The complex Bernstein radius was $0.01027$,
and the nonzero-aggregate error bound was less than $8.4\cdot10^{-6}$.
The stated failure bound $10^{-6}$ is simultaneous over eight experiment
cases and concerns sampling error; floating rounding is not interval-certified.
The enormous physical matrix was **not** built or diagonalized.

Reproduction, with the repository requirements installed:

    OPENBLAS_NUM_THREADS=1 python computations/verification/even_period_spin_resonance.py \
      --output build/even-period-spin-resonance-precheck.json --samples 30000

The nearby primary reference inspected during this work was Keppeler,
Marklof and Mezzadri, *Quantum cat maps with spin 1/2*,
[arXiv:nlin/0012012](https://arxiv.org/pdf/nlin/0012012).
It treats explicit spin coupling and a semiclassical diagonal form-factor
approximation. That is related context, not a verification of the present
even-period theorem or a basis for claiming its priority.

## 8. The scale that destroys the persistent second return

The $K\epsilon^4$ error in (S14) reflects a further transition.
Define the positive convergent constant
$$
 \kappa=4\left[1+\sum_{\ell\ge1}
                     (1-\cos(\pi\lambda^{-\ell}))\right]
       =4.58474690328119272607521570503\ldots .                \tag{S23}
$$
The tail after $\ell=M$ is at most
$2\pi^2\lambda^{-2(M+1)}/(1-\lambda^{-2})$.

**Theorem 3 (critical second-return decay).** In the same deterministic
family, if
$$
 K\epsilon_K^2\to\infty,\qquad
 K\epsilon_K^4\to u\in[0,\infty),
$$
then
$$
 \operatorname{tr}_-U_{\epsilon_K}^{2K}
                 \longrightarrow-\frac12e^{-\kappa u}.     \tag{S24}
$$
This is an absolute limit at fixed $u$. It does not, by itself,
justify a limit with $u\to\infty$ or an all-moment law at this scale.

**Proof.** All nonzero aggregates in Section 3 remain negligible:
$K\delta^8=(K\delta^4)^2/K\to0$. It suffices to analyze (S11).
Factor its phase exactly as in (S12), so that
$$
 Q_K=\mathbb E\left[
 (-1)^{P+Q+PQ}
 \exp\left(i\sum_{i<j}\eta_{j-i}X_iX_j\right)\right].         \tag{S25}
$$
Here $P,Q$ are the parities of Section 4, including all integer values
of the $X_j$.

First, terms with at least one $|X_j|\ge2$ can be removed from the
quadratic phase with an error tending to zero, without changing $P,Q$.
Indeed the Bessel series gives, for $\delta\le1/10$,
$$
 \mathbb E[|X_0|\mathbf1_{\{|X_0|\ge2\}}]
 \le\frac{e^{2\delta^2}\delta^4}{1-\delta^2/6}
 \le2\delta^4.
$$
Combining this with $\mathbb E|X_0|\le2\delta^2$ and (S13)
bounds the error by $4\sqrt2\pi K\delta^6=o(1)$.

Next retain only pairs whose separation differs from $K/2$ by
at most a fixed $M$. The error from the removed phase angles is at most
$$
 \frac{4\pi K\delta^4}{\lambda-1}\lambda^{-M}.                \tag{S26}
$$
This bound is uniform in $K$ and tends to zero as $M\to\infty$
after taking the limit in $K$.

For fixed $M$, the retained pairs form a graph of degree $2M+1$.
An edge is active when both endpoint variables have absolute value one.
Its vertex occupation probability is
$p_K=2J_1(2\epsilon_K)^2\sim2\delta^2$, so $Kp_K^2\to4u$.
There are $K/2$ edges of type zero (exactly opposite sites) and
$K$ edges of each type $\ell=1,\ldots,M$. Attach to each active edge
the sign of $X_iX_j$, combined with the sign of $\eta_{j-i}$.

The marked edge counts converge jointly to independent Poisson variables.
For type zero the two sign means are $u,u$; for each positive type
they are $2u,2u$. Here is an elementary verification of the assertion.
In a fixed joint factorial moment, tuples of edges with disjoint
endpoints have independent occupation and sign probabilities and give
exactly the stated limiting product of means. For a tuple with overlapping
edges, a connected component with $v\ge3$ vertices has $O_M(K)$ possible
placements and probability $p_K^v$. Its contribution vanishes because
$Kp_K^v\to0$. Collections of such components are treated multiplicatively.
All constants in this argument may depend on the fixed moment and $M$.

For completeness these moment limits determine the laws.
Greedily color the retained edges using at most $4M+1$ colors, each a
matching. Occupation indicators within a matching are independent.
Holder's inequality applied to these color classes bounds, for every
fixed real $s>0$, the exponential moment of the total active edge count
by
$$
 \exp\left[
 \frac{|E|p_K^2}{4M+1}
          (e^{(4M+1)s}-1)\right],
$$
with unused color classes allowed. This is uniformly bounded for fixed
$M,s$. Consequently the joint moment convergence just obtained gives
convergence of the joint generating functions in a neighborhood of one
and determines the marked Poisson limit.

The two total parities become uniform and independent of those counts.
To verify this stronger point, insert any nontrivial parity character
$(-1)^{\alpha P+\beta Q}$ in a fixed factorial moment.
An edge tuple with $q$ edges fixes at most $2q$ site variables.
The unused sites contribute a factor of absolute value at most
$$
 J_0(4\epsilon_K)^{K/2-2q}\longrightarrow0.
$$
The remaining factorial-moment sum is bounded by the unmarked one.
The same exponential-moment bound then proves independence and uniformity
of the limiting parities. In particular their sign in (S25) has mean
$-1/2$, even after conditioning on the limiting marked counts.

Finally, the edge angles tend to $\pi$ at type zero and to
$\pm\pi\lambda^{-\ell}$ at type $\ell>0$. The marked Poisson
characteristic function therefore gives, for the retained graph,
$$
 -\frac12
 \exp\left[-4u+4u\sum_{\ell=1}^{M}
                    (\cos(\pi\lambda^{-\ell})-1)\right].
$$
Letting $M\to\infty$ in (S26) proves (S24).

**A stronger necessary condition.**
For any sequence $\epsilon_K\to0$ in this tuned family, convergence
to a bounded microscopic pair density with tail one requires
$$
                         K\epsilon_K^4\longrightarrow\infty. \tag{S27}
$$
If this failed, take a subsequence with $K\epsilon_K^4\to u<\infty$.
If $K\epsilon_K^2$ has a bounded subsequence, (S5) leaves a nonzero
first return. Otherwise pass to a subsequence tending to infinity and
use the nonzero second return in (S24). The positive Fourier identity
of Section 6 rules out the proposed pair density in either case.
This establishes necessity, not sufficiency, of (S27).

## 9. A sharper finite bound for the critical experiment

The constant in $G_K(3\delta)$ is deliberately coarse. Keeping the
factorials of the smallest aggregate resonance produces a substantially
smaller rigorous bound. Put $z=3\delta$, $v=2z^4/(1-z^4)$ and
$$
 B_\sharp(\delta)=
 2I_1(4\delta)^2 I_6(4\delta)
 +\frac{2z^{16}}{1-z^8}
 +\frac{12z^4v^2}{1-4v}.
$$
Then the entire nonzero-aggregate error in the second return is at most
$$
 e^{K B_\sharp(\delta)}-1+2(13/50)^K+31(3/5)^K.              \tag{S28}
$$
For a one-site integer preimage $p=\pm e_j$, the exact aggregate indices
are $(1,-6,1)$ or its negative, and their absolute activity is at most
$2I_1^2I_6$. The other one-site preimages have norm $8|p_j|$
and contribute at most $2z^{16}/(1-z^8)$.
The interval majorants with hull length at least two sum to
$$
 B(z)-2z^4v=\frac{12z^4v^2}{1-4v}.
$$
The positive partition bound of Section 2 proves (S28); the winding
configurations and the 31 noninteger classes keep their earlier bounds.
The argument is uniform for $\delta\le1/10$.

This refinement is for finite experimental control. The proof of
Theorem 3 uses the simpler $G_K$ estimate and is independent of
any Monte Carlo output.

## 10. Summing all aggregates beyond the second transition

The growing-$u$ endpoint can be proved without a Poisson approximation.
More importantly, the contraction survives summation over every aggregate.
This removes a restriction such as $K\delta^8\to0$ from the conclusion
about the second return.

**Theorem 4 (complete two-return asymptotics for a vanishing kick).**
For every real sequence $\epsilon_K\to0$ in (S1)--(S2),
$$
 \operatorname{tr}_-U_{\epsilon_K}^{K}
       =e^{-K\epsilon_K^2}+o(1),                            \tag{S29}
$$
$$
 \operatorname{tr}_-U_{\epsilon_K}^{2K}
       =-\frac12e^{-\kappa K\epsilon_K^4}
          +e^{-2K\epsilon_K^2}
          +\frac12e^{-4K\epsilon_K^2}+o(1).                 \tag{S30}
$$
These are absolute, sequential asymptotics; no relative-error estimate
is asserted when the displayed expression tends to zero. In particular,
$$
 \operatorname{tr}_-U_{\epsilon_K}^{K}\to0
 \quad\hbox{and}\quad
 \operatorname{tr}_-U_{\epsilon_K}^{2K}\to0
 \quad\Longleftrightarrow\quad K\epsilon_K^4\to\infty.       \tag{S31}
$$
This equivalence concerns these two returns. It does not make their
decay sufficient for microscopic universality or determine other returns
at the second transition.

### 10.1 A contraction uniform in arbitrary external fields

Write $\mu(n)=J_n(2\epsilon)^2$, $\delta=|\epsilon|$, and
$$
 d=\mu(1)^2=J_1(2\epsilon)^4.
$$
For $0<\delta\le1/20$, the alternating Bessel series implies
$$
 \mu(0)\ge\mu(1),\qquad
 \tfrac12\delta^4\le d\le\delta^4.
$$
For arbitrary real $h,g$, four entries of
$$
 \sum_{x,y\in\mathbb Z}\mu(x)\mu(y)
                  e^{i\pi xy+ihx+igy}
$$
are $(x,y)=(0,0),(1,0),(0,1),(1,1)$.
Each has weight at least $d$. Removing weight $d$ from each entry
leaves a positive measure of mass $1-4d$. The four removed terms satisfy
$$
 |1+e^{ih}+e^{ig}-e^{i(h+g)}|^2
                   =4+4\sin h\sin g\le8.
$$
Since $2\sqrt2<3$, the whole pair average has modulus at most $1-d$.
The estimate is uniform in the two fields, which is essential below.

The same argument on the restricted set $|x|,|y|\le2$ gives the bound
$g_0=s^2-d$, where $s=\sum_{|n|\le2}\mu(n)$.
The complementary pair mass is $h_0=1-s^2$, and $g_0\ge1/2$
in the stated range. For example,
$\mu(0)\ge(1-\delta^2)^2$ already implies this last inequality.
Thus large charges can be retained exactly as part of the complementary
mass; they will not be discarded with an extensive truncation error.

### 10.2 The zero aggregate at every growing second-scale parameter

Put $u=K\delta^4$. In (S25) retain only the angles with
$|j-i-m|\le M$, where $m=K/2$ and $M<m/2$.
The error is still bounded by (S26), using the full variables $X_j$.
Group sites into antipodal pairs $\{r,r+m\}$, $0\le r<m$.
The retained interaction graph on pair labels has degree at most $2M$,
so a greedy independent set contains at least $m/(2M+1)$ pairs.
Condition on all other variables.

Expand the parity factor by the exact identity
$$
 (-1)^{P+Q+PQ}
 =\tfrac12\big[-1+(-1)^P+(-1)^Q+(-1)^{P+Q}\big].           \tag{S32}
$$
In each summand the selected pairs interact only internally.
The conditioned variables and the parity character merely supply real
external fields. Section 10.1 applies to every selected pair, giving
$$
 |Q_K|\le
 2\exp\!\left[-\frac{dm}{2M+1}\right]
       +\frac{4\pi u}{\lambda-1}\lambda^{-M}.                \tag{S33}
$$
Take $M=\lceil2\log(2+u)/\log\lambda\rceil$ when $u\to\infty$.
Eventually $M<m/2$, because $u\le K/20^4$.
The two terms tend to zero: their controlling scales are
$u/\log(2+u)$ and $u/(2+u)^2$, respectively.
Consequently $Q_K\to0$ for every such sequence, with no restriction
on $K\delta^6$ or $K\delta^8$.

This alone would not control nonzero aggregates. The next two steps do.

### 10.3 Separated pairs with the full, untruncated interaction

Choose an integer spacing
$$
 R=\left\lceil
       \frac{\log(1+128\pi/d)}{\log\lambda}\right\rceil,
 \qquad \rho=1-d/2.                                       \tag{S34}
$$
Select pair labels $0,R,\ldots,(q-1)R$, where
$q=\lfloor m/R\rfloor$. Their successive circular gaps are at least $R$.
Any subset of these labels has the same separation property.

For two pair labels at oriented separation $r$, $0<r<m$,
the sum of the absolute values of their four interaction angles is at most
$$
 2\pi\big(\lambda^{-r}+\lambda^{-(m-r)}\big).
$$
This follows directly from $b_j/b_m\le\lambda^{j-m}$.
If both pairs satisfy $|X|\le2$, the absolute change in their joint
phase factor on removing this interaction is therefore at most
$$
 t_{ab}=8\pi\big(\lambda^{-r}+\lambda^{-(m-r)}\big).
$$
For each selected pair the sum over other selected pairs is bounded by
$$
 w=\frac{16\pi\lambda^{-R}}{1-\lambda^{-R}}
                         \le d/8.                         \tag{S35}
$$

Here is a finite expansion that controls these interactions in relative
form. First specify the subset of selected pairs that have a charge
of absolute value at least three, and condition on their values and on
all outside variables. Call the remaining pairs good.
All interactions involving a conditioned pair are external fields
for the good pairs, regardless of the size of its charges.

On the good pairs expand each inter-pair phase factor as $1+f_{ab}$,
where $|f_{ab}|\le t_{ab}$. In a term indexed by an edge set $E$,
untouched pairs contribute at most $g_0$ by Section 10.1.
Touched pairs contribute at most their positive mass $s^2$.
If there are $n$ good pairs, the term is bounded by
$$
 g_0^n\prod_{\{a,b\}\in E}t_{ab}
                       (s^2/g_0)^{|V(E)|}.
$$
Since $s^2/g_0\le2$ and $|V(E)|\le2|E|$, the sum of these bounds is at most
$$
 g_0^n\prod_{\{a,b\}}(1+4t_{ab})
       \le g_0^n e^{2nw}.
$$
The expansion is over a finite graph and the remaining good spins have
finite support, so it entails no unproved infinite cluster expansion.
Now sum over all complementary pairs with their exact positive masses
$h_0$. The result is at most
$$
 (h_0+g_0e^{2w})^q
 \le(1-d+4w)^q\le\rho^q.                                 \tag{S36}
$$
Here $e^{2w}-1\le4w$ in the indicated range.
This bound is uniform in all outside fields, retains every integer charge,
and uses every interaction angle.

### 10.4 Nonzero aggregates supply fields and remove only a few pairs

Fix any $c\in\mathcal C$ in the exact two-block expansion.
Write the block indices as $x$ and $c-x$.
The cross phase between the two block totals vanishes modulo $N$,
since the aggregate Weyl vector is zero modulo $N$.
The remaining ordered phase is
$$
 e_N\!\left(
  a^2\sum_{i<j}b_{j-i}
     [\,2x_ix_j-c_ix_j-x_ic_j+c_ic_j\,]\right).              \tag{S37}
$$
Thus its quadratic part in $x$ is precisely the one in (S11).
The other terms are a constant and real linear fields after exponentiation.

Define the one-site signed weights
$$
 \nu_c(x)=i^c(-1)^xJ_x(2\epsilon)J_{c-x}(2\epsilon).
$$
They have total absolute mass $A_c$ from (S10), and $\nu_0=\mu$.
Extracting the factor $(-1)^{\sum x_j}$ and then using (S12)
produces exactly the parity factor (S32).
Consequently the preceding contraction applies to every selected pair
whose two aggregate indices vanish, for each of the four parity characters.

At most $\|c\|_1$ of the $q$ selected pairs fail this condition.
Condition on all their variables and bound their signed weights by
absolute values. Equations (S10) and (S36) bound the contribution of $c$ by
$$
 2\rho^q\rho^{-\|c\|_1}\prod_j A_{c_j}
       \le2\rho^q(3\delta/\rho)^{\|c\|_1}.                 \tag{S38}
$$
This inequality also holds when $\|c\|_1>q$.
All Fourier series are absolutely convergent at finite $K$, so the
conditioning and rearrangements are justified before taking limits.
Since $3\delta/\rho\le4\delta\le3/10$, (S9) now gives a finite bound
for the entire physical trace:
$$
 |\operatorname{tr}_-U_\epsilon^{2K}|
 \le2\rho^q[1+G_K(3\delta/\rho)]
                       +\frac{e^{4K\delta}}{N-1}.          \tag{S39}
$$
In particular,
$$
 |\operatorname{tr}_-U_\epsilon^{2K}|
 \le68\exp\!\left(q\log\rho+5K(4\delta)^8\right)
                       +\frac{e^{4K\delta}}{N-1}.          \tag{S40}
$$
The constants are deliberately conservative. Unlike an additive estimate
by $G_K$, this expression preserves phase cancellation in the nonzero
aggregate terms.

### 10.5 Passing to limits and completing the two-return formula

As $\delta\to0$, $R=O(1+\log(1/\delta))$, $R\to\infty$, and
$\delta^4R^2\to0$.
Suppose $u=K\delta^4\to\infty$. If $u\le R^2$, then
$K\delta^8=u\delta^4\to0$ and the original aggregate bound (S9),
together with (S33), proves that the second trace tends to zero.

On the remaining indices $u>R^2$, eventually $K\ge4R$ and
$q\ge K/(4R)$. Since $\log\rho\le-d/2\le-\delta^4/4$,
$$
 q\log\rho+5K(4\delta)^8
 \le-\frac{u}{16R}+327680\,u\delta^4
 \le-\frac{u}{32R}\longrightarrow-\infty.
$$
The last inequality holds eventually because $\delta^4R\to0$.
The odd-projection error tends to zero since
$\log N=K\log\lambda/2+O(1)$ and $\delta\to0$.
Equation (S40) proves the same conclusion on these remaining indices.
This establishes
$$
 K\delta^4\to\infty,\quad\delta\to0
       \quad\Longrightarrow\quad
             \operatorname{tr}_-U_\epsilon^{2K}\to0.       \tag{S41}
$$

For the first return one can retain the common factor $J_0(2\epsilon)^K$
when summing the aggregates. For $\delta\le1/10$,
$$
 \frac{|J_n(2\epsilon)|}{J_0(2\epsilon)}
      \le(2\delta)^{|n|}\quad(n\ne0),\qquad
 J_0(2\epsilon)\le e^{-\delta^2}.
$$
The Bessel series gives both estimates, with
$J_0(2\epsilon)\ge1-\delta^2>0$.
Using (S9) therefore yields
$$
 |\operatorname{tr}_-U_\epsilon^K|
 \le e^{-K\delta^2/2}+33(3/5)^K
                              +\frac{e^{2K\delta}}{N-1}.  \tag{S42}
$$
Indeed $5(2\delta)^8\le\delta^2/2$ in this range.
For bounded $K\delta^2$, (S5) and the Bessel series give (S29);
for $K\delta^2\to\infty$, (S42) gives it.
A subsequence argument covers arbitrary sequences.

For (S30), first pass to a subsequence on which $K\delta^2$
has a limit in $[0,\infty]$. If the limit is finite, (S6) proves the
formula, since $K\delta^4\to0$.
If it is infinite, pass further to a subsequence on which $K\delta^4$
has a limit in $[0,\infty]$. A finite limit is Theorem 3;
an infinite limit is (S41). Each subsequence has the asserted
vanishing difference, which proves (S30) for the original sequence.
Finally (S29), Theorem 3, and (S41) imply (S31).

### 10.6 Verification status and remaining problem

The new nonzero-aggregate reduction (S37) is checked by 23,328 exhaustive
ordered Weyl words: all $x\in\{-1,0,1\}^6$ for each of the 32
parity-constant aggregate representatives at $N=35$.
The conditional sign-averaging algorithm is compared with complete sign
enumeration on fourteen finite graphs, including graphs with cycles.
These are finite algebra and implementation controls. The bounds and
limits above are mathematical arguments requiring independent review.

The companion experiment now also treats $K\delta^4=0.02,0.1,0.3$
at $K=10002$. It keeps all interactions within twelve offsets of an
antipodal pair, bounds the omitted angles and Bessel tail explicitly,
and uses (S28) for all nonzero aggregates.
Conditional averaging includes cycles rather than silently replacing the
interaction graph by a forest. The empirical standard error and the
conservative Bernstein bound are reported separately.
Numerical rounding is not interval-certified.

    OPENBLAS_NUM_THREADS=1 python computations/verification/even_period_spin_resonance.py \
      --output build/even-period-spin-resonance-precheck.json \
      --samples 30000 --critical-samples 8000

What has been closed here is the two-return problem for this particular
dimension-dependent harmonic. The passage to a fixed smooth symbol,
all higher returns at the second scale, and microscopic BGS statistics
remain unproved. In particular, (S31) removes two obstructions; it does
not establish the desired universal limit.
