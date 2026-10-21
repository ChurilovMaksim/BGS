> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/root_sharp_microscopic_perturbation_threshold.md`. Embedded SHA256: `ea39b0166a5308caa8c68d83ca4d744d2f404b0a9d5fe0eb2b98df5d5dc47ab0`.
> [Thematic guide](../../topics/closure.md).

# Sharp norm scale for arbitrary spectral replacements

21 October 2026. Round 8. Root proof note.

## 1. Status and purpose

This note proves an exact limitation of arguments that retain only a
coarse operator approximation to the original matrices. It does not
modify the problem's definition of $U_N$, and the replacement matrices
constructed below are not a counterexample for that exact definition.

There are two complementary statements.

1. For arbitrary pairs of unitary matrices, operator norm error $o(1/N)$
   preserves every local Laplace functional with a uniformly random
   spectral origin.
2. For every prescribed constant $C>0$, and for every original sequence
   of unitary matrices, replacements within $C/N$ in operator norm can
   be constructed which fail the Sine-2 limit. The failure is witnessed
   by a bounded continuous functional. Moreover one of five fixed
   admissible tests has a nonvanishing second diagonal-moment defect on
   an infinite subsequence.

The second assertion applies in particular to the exact $U_N$ in the
question along all odd dimensions. The replacement keeps the original
eigenvectors. Hence the uniform compressed shrinking-window theorem
proved in this round also holds for these replacements, despite their
failure of the spectral target. All estimates below are independent of
any unproved property of the original spectrum.

The rounding construction is elementary. No claim of historical
priority or of a new universality theorem is made.

## 2. A finite-dimensional eigenangle matching lemma

Let $U,V$ be $N$-dimensional unitaries and suppose
$\epsilon=\|V-U\|_{\mathrm{op}}<2$. Put
$$
 \eta=2\arcsin(\epsilon/2).
$$
Then their eigenvalues can be labelled, with multiplicities, as
$e^{2\pi i\theta_j}$ and $e^{2\pi i\varphi_j}$, using real lifts, so
that
$$
 |\varphi_j-\theta_j|\le \frac{\eta}{2\pi}
 \quad(1\le j\le N).
 \tag{2.1}
$$

Here is a proof, including the issue of eigenvalue collisions. The
unitary $VU^*$ has no eigenvalue $-1$. Its spectral decomposition
defines a Hermitian principal logarithm $H$ such that
$$
 VU^*=e^{iH},\qquad \|H\|_{\mathrm{op}}\le\eta .
 \tag{2.2}
$$
Indeed $|e^{ih}-1|=2|\sin(h/2)|$ for its principal eigenangles
$h\in(-\pi,\pi)$. Consider $U(t)=e^{itH}U$.

Locally in $t$, choose a fixed rotation $Z(t)=e^{-i\beta}U(t)$ whose
spectrum avoids $-1$. This is possible at each $t$, since a finite
spectrum leaves a point on the circle free. The Cayley transform
$$
 A(t)=i(I-Z(t))(I+Z(t))^{-1}
$$
is a differentiable Hermitian matrix. A direct differentiation gives
$$
 A'(t)=2(I+Z(t))^{-1}H(I+Z(t)^*)^{-1}.
 \tag{2.3}
$$
Consequently the Hermitian order bounds $-\eta I\le H\le\eta I$ give
$$
 -\frac{\eta}{2}(I+A(t)^2)
 \le A'(t)\le
 \frac{\eta}{2}(I+A(t)^2).
 \tag{2.4}
$$
We used
$(I+Z)^{-1}(I+Z^*)^{-1}=(I+A^2)/4$, which follows either from
the Cayley identity or on each spectral eigenspace.

The ordered eigenvalues $\mu_j(t)$ of a differentiable Hermitian
matrix are locally Lipschitz. To verify the only fact used here, the
min--max characterization gives
$$
 |\mu_j(t+h)-\mu_j(t)|\le\|A(t+h)-A(t)\|.
$$
At every point where $\mu_j$ is differentiable, its derivative lies
between the smallest and largest Rayleigh quotients of $A'(t)$ on
the eigenspace for $\mu_j(t)$. This includes a repeated eigenvalue.
One way to see the latter claim is to write
$A(t+h)=A(t)+hA'(t)+o(h)$, decompose into that eigenspace and its
orthogonal complement, and solve the complementary block using its
fixed nonzero spectral gap. The complementary component of a unit
eigenvector is $O(h)$. Its contribution to the eigenvalue is
$O(h^2)$; the remaining first-order eigenvalues are those of the
compression of $A'(t)$ to the eigenspace. The min--max bounds on this
compression give the claimed interval. If the whole space is the
eigenspace, the same statement follows directly from min--max.

Thus (2.4) implies, almost everywhere,
$$
 |\mu_j'(t)|\le\frac{\eta}{2}(1+\mu_j(t)^2).
$$
The corresponding eigenangle $\gamma_j(t)=\beta+2\arctan\mu_j(t)$
therefore satisfies $|\gamma_j'(t)|\le\eta$. It is locally Lipschitz
and hence absolutely continuous. On overlapping intervals the
eigenangles can be matched continuously, relabelling at coincidences;
local cuts are only changed by adding integer multiples of $2\pi$.
A finite cover of the compact parameter interval gives continuous real
lifts with
$$
 |\gamma_j(1)-\gamma_j(0)|\le\int_0^1\eta\,dt=\eta.
$$
This proves (2.1), without assuming a simple spectrum.

## 3. Uniform local Laplace stability below $1/N$

For the point process in the question, denote the Laplace functional
for a deterministic unitary $U$ by
$$
 L_N^U(f)=\int_0^1
 \exp\!\left[-\sum_{j,\ell}f(N(\theta_j-\alpha+\ell))\right]d\alpha .
$$
Let $f\ge0$ be continuously differentiable with compact support.
Using (2.1), the inequality $|e^{-x}-e^{-y}|\le|x-y|$ for
$x,y\ge0$, and unfolding the integral over $\alpha$, we obtain
$$
 \begin{aligned}
 |L_N^U(f)-L_N^V(f)|
 &\le \frac1N\sum_j
   \|f(\,\cdot+N(\varphi_j-\theta_j))-f\|_{L^1(\mathbb R)}\\
 &\le \|f'\|_1\sum_j|\varphi_j-\theta_j|\\
 &\le \frac{N\eta}{2\pi}\|f'\|_1 .
 \end{aligned}
 \tag{3.1}
$$
The $L^1$ translation inequality in the second line follows by
integrating
$f(x+h)-f(x)=\int_0^h f'(x+t)\,dt$ and applying Fubini. The first
line includes every periodic copy of every eigenvalue. In particular,
neither a support-overlap assumption nor simplicity is needed.

It follows that
$$
 \|V_N-U_N\|_{\mathrm{op}}=o(1/N)
 \quad\Longrightarrow\quad
 L_N^{V_N}(f)-L_N^{U_N}(f)\longrightarrow0
 \tag{3.2}
$$
for every such $f$, uniformly over the underlying unitary matrices.
This proves stability of the local point-process law whenever one of
the two sequences has a limit characterized by these functionals.
No assertion about convergence of unbounded factorial moments is
inferred from (3.2).

## 4. Replacement at any fixed positive multiple of $1/N$

Fix $C>0$, put $a=C/\pi>0$, and set
$$
 M_N=\left\lceil\frac N a\right\rceil,\qquad a_N=\frac N{M_N}.
 \tag{4.1}
$$
For any given unitary $U_N$, choose an orthonormal eigenbasis,
retaining multiplicities. Round each eigenangle to its nearest point
of $M_N^{-1}\mathbb Z/\mathbb Z$, choosing either endpoint by a
fixed rule in the case of a tie. Define $V_N$ to have these rounded
eigenvalues in that same eigenbasis. Then
$$
 \|V_N-U_N\|_{\mathrm{op}}
 \le 2\sin\frac{\pi}{2M_N}
 \le\frac{\pi}{M_N}\le\frac C N .
 \tag{4.2}
$$
The construction is deterministic after the tie rule and the basis
choice. Its conclusions do not depend on those choices.

The local process of $V_N$, for any origin $\alpha$, is supported
on a translate of the lattice $a_N\mathbb Z$. Some lattice sites can
be unoccupied and others can have multiplicity. From (4.1),
$$
 a_N\longrightarrow a,\qquad
 0\le a-a_N\le\frac{a^2}{N},\qquad
 a_N\ge a/2\quad\hbox{for all sufficiently large }N.
 \tag{4.3}
$$
These bounds hold without using the distribution of the original
eigenangles.

## 5. A bounded continuous witness against Sine-2

Choose nonzero nonnegative smooth functions $f_1,f_2$ supported in
the disjoint intervals
$$
 I_1=(a/8,a/4),\qquad I_2=(a/2,5a/8).
$$
On locally finite point measures define
$$
 \mathcal O(\xi)
  =(1-e^{-\langle f_1,\xi\rangle})
   (1-e^{-\langle f_2,\xi\rangle}).
 \tag{5.1}
$$
This is a bounded continuous functional for the vague topology,
with values between zero and one. Any point in $I_1$ and a point in
$I_2$ have a positive distance less than $a/2$. For sufficiently
large $N$, that distance is smaller than $a_N$. Thus a translate
of $a_N\mathbb Z$ cannot meet both supports. Multiple points at a
single site do not change this conclusion. Therefore
$$
 \mathcal O(\Xi_{N,\alpha}^{V_N})=0
 \quad\hbox{for every }\alpha
 \quad\hbox{and all sufficiently large }N.
 \tag{5.2}
$$

For Sine-2 the expectation of (5.1) is strictly positive. To justify
positivity without invoking convergence of moments, take subintervals
$J_i\Subset I_i$ on which $f_i\ge c_i>0$. Write $n_i$ for
the counts in $J_i$, $\ell_i=|J_i|$, and
$$
 A=\mathbb E_{\rm sine}(n_1n_2)
  =\int_{J_1\times J_2}
    \left(1-\left(\frac{\sin\pi(x-y)}{\pi(x-y)}\right)^2\right)
       dx\,dy>0.
 \tag{5.3}
$$
The strict inequality holds since $x-y\ne0$ on the disjoint
intervals and $|\sin t|<|t|$ for nonzero real $t$.
The determinantal densities satisfy $0\le\rho_k\le1$, by the
Gram representation of the sine kernel and the determinant bound for
a positive Gram matrix with diagonal one. Expanding $n_1^2n_2^2$
into factorial counts gives
$$
 \mathbb E(n_1^2n_2^2)
 \le \ell_1\ell_2(1+\ell_1)(1+\ell_2).
 \tag{5.4}
$$
Cauchy--Schwarz applied to
$n_1n_2\mathbf1_{\{n_1n_2>0\}}$ now yields
$$
 \mathbb E_{\rm sine}\mathcal O
 \ge
 (1-e^{-c_1})(1-e^{-c_2})
 \frac{A^2}{\ell_1\ell_2(1+\ell_1)(1+\ell_2)}>0.
 \tag{5.5}
$$
Equations (5.2) and (5.5) rigorously exclude weak convergence of the
rounded family to Sine-2. The witness is bounded, so no uniform
integrability assumption is hidden in this conclusion.

## 6. Five fixed admissible tests detecting the same replacement

The preceding bounded witness can also be turned into a fixed-test
failure of the diagonal pair criterion for the rounded family.
This requires a separate argument; failure of weak convergence alone
is not being used to claim convergence or divergence of a moment.

Use the explicit smooth bump
$$
 \phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{\{|\xi|<1\}},\quad
 I_\phi=\int_{\mathbb R}\phi,\quad
 u=\mathcal F^{-1}\phi,\quad
 d(x)=\frac{|u(x)|^2}{8I_\phi^2}.
 \tag{6.1}
$$
Then $d$ is nonnegative Schwartz, $\sup d\le1/8$, and its
Fourier transform is smooth with support in $[-2,2]$.
For
$\Theta=\{0,\pi/2,\pi,3\pi/2\}$, put
$$
 b_\vartheta(x)=d(x)(1+\cos(2\pi x/a+\vartheta)).
 \tag{6.2}
$$
These four functions are also nonnegative Schwartz, have
$\sup b_\vartheta\le1/4<1$, and have smooth Fourier transforms
supported in the fixed compact set
$$
 [-2,2]\ \cup\ ([ -2,2]+1/a)\
                 \cup\ ([ -2,2]-1/a).
 \tag{6.3}
$$
Thus all five tests belong to the precise class specified in the
question. A small $C$ can require a large Fourier band, which is
permitted: the band is fixed before $N$ tends to infinity.

For a real Schwartz function $b$, define its autocorrelation
$$
 c_b(y)=\int_{\mathbb R}b(x)b(x+y)\,dx.
 \tag{6.4}
$$
It is even, Schwartz, and has Fourier transform
$|\widehat b|^2$. Averaging the elementary products of the four
trigonometric factors in (6.2) gives the exact identity
$$
 \frac14\sum_{\vartheta\in\Theta}c_{b_\vartheta}(y)
  =c_d(y)\left(1+\frac12\cos(2\pi y/a)\right).
 \tag{6.5}
$$
Indeed the averages of each individual cosine vanish, whereas the
average of their product is $\frac12\cos(2\pi y/a)$.
It follows that
$$
 F(y):=(1-\cos(2\pi y/a))c_d(y)
       =3c_d(y)-\frac12\sum_{\vartheta\in\Theta}c_{b_\vartheta}(y).
 \tag{6.6}
$$
The function $F$ is nonnegative, even, Schwartz, has compactly
supported smooth Fourier transform, and vanishes on $a\mathbb Z$.
It is nonzero: $c_d(0)=\int d^2>0$, so $c_d$ is positive near
zero and the cosine factor is positive at some nearby nonzero points.

## 7. Pair measures and a bound uniform in all lattice occupancies

For eigenangles $\theta_j$ of any $N$-dimensional unitary, define
the periodic locally finite pair-difference measure
$$
 \mathcal R_N
   =\frac1N\sum_{j\ne k}\sum_{\ell\in\mathbb Z}
           \delta_{N(\theta_j-\theta_k+\ell)} .
 \tag{7.1}
$$
This definition includes distinct eigenvalue indices even when their
angles coincide. Unfolding the random origin in the definition of
$M_{2,N}$, with nonnegative summands, gives exactly
$$
 M_{2,N}(b)=\frac12\langle c_b,\mathcal R_N\rangle .
 \tag{7.2}
$$
For a signed linear combination of the Schwartz correlations in
(6.6), the same identity follows by linearity; every integral and
periodization is absolutely convergent for each finite $N$.

For the rounded matrices, every atom of (7.1) is at $a_N k$, with
$k\in\mathbb Z$. The error between $a_N$ and $a$ must be
controlled despite arbitrarily large occupancies. From (4.3) and
$1-\cos t\le t^2/2$,
$$
 1-\cos(2\pi a_Nk/a)\le\frac{2\pi^2a^2 k^2}{N^2}.
 \tag{7.3}
$$
Choose any exponent $L>3$. Since $c_d$ is nonnegative and
Schwartz, there is a constant $D_L$ such that, for large $N$,
$$
 0\le F(a_N k)
 \le\frac{D_L}{N^2}\,k^2(1+(a/2)|k|)^{-L}.
 \tag{7.4}
$$
For each fixed ordered eigenvalue pair, its periodized differences
correspond to a subset $k_0+M_N\mathbb Z$ of the integer lattice.
Hence their total contribution is at most
$$
 \frac{D_L}{N^2}
 \sum_{k\in\mathbb Z}k^2(1+(a/2)|k|)^{-L}
 =\frac{D_a}{N^2}.
 \tag{7.5}
$$
The series is finite. Summing over at most $N(N-1)$ pairs and
including the $1/N$ in (7.1) yields the uniform estimate
$$
 0\le\langle F,\mathcal R_N^{V_N}\rangle\le D_a/N\longrightarrow0.
 \tag{7.6}
$$
No level-repulsion, multiplicity, global Weyl law, or moment bound
for $U_N$ has been assumed. In particular, coincidences cause no
problem: $F(0)=0$ exactly.

## 8. The CUE value and the fixed-test countersequence

The exact finite matrix formula supplied in the problem gives
$$
 M_{2,N}^{\rm CUE}(b)
   =\frac12\left[\left(\int b\right)^2
                         -\operatorname{Tr}(T_{N,b}^2)\right].
 \tag{8.1}
$$
Here
$$
 \operatorname{Tr}(T_{N,b}^2)
  =\frac1N\sum_{|m|<N}(1-|m|/N)|\widehat b(m/N)|^2.
 \tag{8.2}
$$
The Riemann sum converges to
$\int_{-1}^1(1-|t|)|\widehat b(t)|^2dt$. The triangular
function $(1-|t|)_+$ is the Fourier transform of
$(\sin\pi y/(\pi y))^2$: this follows by convolving two
indicators of $[-1/2,1/2]$ and multiplying their inverse Fourier
transforms. Fourier inversion, using the Schwartz functions in
(6.4), consequently gives
$$
 M_{2,N}^{\rm CUE}(b)\longrightarrow
 \frac12\int_{\mathbb R}c_b(y)
 \left(1-\left(\frac{\sin\pi y}{\pi y}\right)^2\right)dy .
 \tag{8.3}
$$

Define the explicit strictly positive finite constant
$$
 I_a=\int_{\mathbb R}F(y)
   \left(1-\left(\frac{\sin\pi y}{\pi y}\right)^2\right)dy>0 .
 \tag{8.4}
$$
Positivity follows from the properties following (6.6) and the strict
inequality in (5.3); finiteness follows from the Schwartz decay.
Let $\Delta_{2,N}^{V}(b)=M_{2,N}^{V_N}(b)-M_{2,N}^{\rm CUE}(b)$.
Combining (6.6), (7.2), (7.6), and (8.3) gives
$$
 3\Delta_{2,N}^{V}(d)
 -\frac12\sum_{\vartheta\in\Theta}\Delta_{2,N}^{V}(b_\vartheta)
       \longrightarrow-\frac{I_a}{2}.
 \tag{8.5}
$$
The sum of the absolute values of the five coefficients is $5$.
Therefore, for every sufficiently large odd $N$, at least one of
these five fixed tests satisfies
$$
 |\Delta_{2,N}^{V}(b)|\ge I_a/20 .
 \tag{8.6}
$$
The infinite pigeonhole principle selects a single test from this
finite list and an infinite odd subsequence on which (8.6) holds.
This is a rigorous fixed-$k=2$, fixed-test defect for the rounded
sequence. The additional bounded witness in §5 independently rules
out its weak Sine-2 limit.

The selected test can depend on the input sequence. The finite list
of candidate tests, the positive constant $I_a/20$, and the norm
bound $C/N$ do not. This distinction avoids claiming a particular
one of the five signs or individual asymptotics without proof.

## 9. Consequences for the actual research route

Apply the construction to the exact original $U_N$. It produces
another sequence $V_N$, with the same eigenvectors, within $C/N$
of it in operator norm. The original-family fixed-time compact
limits remain valid for this sequence because
$$
 \big\||V_N^n|^{\circ2}-|U_N^n|^{\circ2}\big\|_{\mathrm{op}}
 \le2n\|V_N-U_N\|_{\mathrm{op}}\longrightarrow0
 \quad\hbox{for each fixed }n.
 \tag{9.1}
$$
This inequality follows by telescoping powers and compressing the
identity
$\operatorname{Ad}V-\operatorname{Ad}U$ on Hilbert--Schmidt
space. Thus the shrinking-window and compressed-resolvent theorem
of this round applies equally to the rounded $V_N$. Equations
(5.2)--(5.5) and (8.5)--(8.6) show why that qualitative theorem
cannot close the unweighted microscopic statistic.

For sharpness of uniform Laplace stability itself, the
[explicit two-clock addendum](r8_return_sharp_stability_clock_addendum.md)
supplies the needed direct comparison. For every $C>0$, it constructs
two explicit diagonal unitary sequences within $C/N$ and one fixed
smooth nonnegative test whose Laplace values have a strictly positive
limiting difference. This additional comparison does not presume the
existence of a deterministic Sine-convergent base sequence.

This also identifies the sharp norm scale for a *general* replacement
argument: $o(1/N)$ is sufficient for local Laplace stability, while
no fixed bound $C/N$, however small its positive constant, is
sufficient uniformly over all perturbations. Smooth structured
perturbations can have stronger stability properties; nothing in
this note contradicts a separately proved theorem that imposes
additional hypotheses on their generators.

No rounding is allowed in a proof of the requested $H_{\rm diag}$
without a justified transfer back to the exact $U_N$. There is no
such transfer here. For that exact sequence, even the fixed test
$b_*(x)=|u(x)|^2/(2I_\phi^2)$ still requires the estimate
$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
       (|\operatorname{Tr}U_N^m|^2-\min(m,N))
       \stackrel{?}{\longrightarrow}0 .
 \tag{9.2}
$$
This is explicitly left unproved, as are the required higher orders.
