> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round9_2026_10_21/root_diagonal_cocycle_normalization.md`. Embedded SHA256: `afeaa52cea23836c5b4fa58d1040daa6df792d0b9adea83f8eb1de8690211921`.
> [Thematic guide](../../topics/classical_trace.md).

# An actual analytic quantization with a uniformly normalized first cocycle phase

21 October 2026. Round 9. Primary derivation by the root agent.

## 0. Result and scope

For the exact family in the question, the continuous first quantum graph
phase can be removed to relative error $o(1)$, uniformly on every orbit
of length at most $BN$, by an explicitly defined type of unitary
modification which preserves the local-law limit and the truth of the
full $H_{\rm diag}$.

The construction uses real trigonometric polynomials of degrees tending
to infinity sufficiently slowly. It changes neither the prescribed
$\tau$ nor the sequence of odd dimensions. It provides an equivalent
quantization, not an independently known CUE model.

More precisely, there are real trigonometric polynomials $v_j$, integer
thresholds $n_j\uparrow\infty$, and
$$
j(N)=\max\{j:n_j\le N\},\qquad
\widetilde U_N=\exp\!\left(\frac{i}{N}Q_N(v_{j(N)})\right)U_N
\tag{0.1}
$$
for all sufficiently large odd $N$, with the following properties.

1. The random-origin local laws of $U_N$ and $\widetilde U_N$
   approach one another. Moreover,
   $$
   H_{\rm diag}(U_N)\quad\Longleftrightarrow\quad
   H_{\rm diag}(\widetilde U_N).
   \tag{0.2}
   $$
   This is an equivalence, not an assertion that either side holds.
2. Every $\widetilde U_N$ is the exact comb restriction of a plane
   operator with the same generating phase $F$ as the original
   operator and an exact amplitude on one fixed complex spatial strip.
   The all-time contour and dominated-graph trace construction continues
   to apply to this amplitude. It does not rely on a formal kernel
   equality.
3. If $\widetilde\gamma_N(x)$ is its normalized graph scalar and
   $\gamma_0(x)>0$ the original leading scalar, then
   $$
   \sup_x\left|
   \frac{\widetilde\gamma_N(x)}{\gamma_0(x)}-1
   \right|=o(N^{-1}).
   \tag{0.3}
   $$
   Consequently, for every fixed $B<\infty$,
   $$
   \sup_{\substack{x\in\mathbb T^2\\1\le m\le BN}}
   \left|\frac{\prod_{r=0}^{m-1}
   \widetilde\gamma_N(\Psi^r x)}
   {\prod_{r=0}^{m-1}\gamma_0(\Psi^r x)}-1\right|
   \longrightarrow0.
   \tag{0.4}
   $$
   Periodicity is not needed for this product estimate.

The construction closes the regularity and actual-unitary-realization
issue explicitly left open in Section 8 of the Round 3 subprincipal
stability proof, at the precision relevant to (0.4). It does not create
one fixed analytic function equal to the continuous graph phase, nor
does it assert exact cancellation at each finite $N$.

There is a separate and still unproved step between (0.4) and
cancellation of the full signed orbit sums. Section 8 identifies it
without hiding it in the construction.

## 1. Normalization and previously proved inputs actually used

Put $h=(2\pi N)^{-1}$ and use ordinary real-midpoint Weyl
quantization
$$
Q_N(v)=\sum_{k,l}\widehat v(k,l)(-1)^{kl}T_N(l,k).
\tag{1.1}
$$
For a plane symbol $v$ the corresponding operator is
$$
(\operatorname{Op}_h(v)\psi)(Q)=
\sum_{k,l}\widehat v(k,l)
e^{2\pi i k(Q+\pi hl)}\psi(Q+2\pi hl).
\tag{1.2}
$$
At the indicated $h$, (1.2) descends exactly to (1.1). The sign is
necessary: the modular midpoint differs from the real midpoint by
$(-1)^{kl}$ for odd $N$. A real $v$ makes both operators
self-adjoint.

The original plane propagator, including its metaplectic factor, has
the exact kernel
$$
\mathcal U_h(Q,q)=C_h e^{iF(Q,q)/h}B_h(Q,q),\qquad
C_h=\frac{e^{i\pi/4}}{\sqrt{8\pi h}},
\tag{1.3}
$$
where
$$
F=F_0+G,\qquad
F_0=-\frac{3Q^2-2Qq+3q^2}{8}.
\tag{1.4}
$$
Here $G$ is bounded holomorphic on a fixed tube around $\mathbb R^2$,
is real on the real plane, and has uniformly small Hessian. The exact
amplitude is bounded holomorphic on a fixed smaller tube and is $C^2$
in real $h$, uniformly there:
$$
B_h=B_0+ihb_1+O(h^2),\qquad
B_0=2\sqrt{F_{Qq}},\qquad B_0,b_1\ {\rm real}.
\tag{1.5}
$$
These assertions were proved from the finite Fourier generator:
Hamilton--Jacobi characteristics at the fixed time
$10^{-80}/(2\pi)$, horizontal Weyl shifts, and a convergent
analytic-scale Dyson series. The complete source
exact_amplitude.md was reread for this derivation; its equations
(7), (20)--(28) give the exact exponent, uniform derivative bounds,
and equality of distribution kernels. In particular this note does
not use a merely formal semiclassical propagator.

The phase generates
$$
p=-F_q(Q,q),\qquad P=F_Q(Q,q),\qquad
\Psi(q,p)=(Q,P).
\tag{1.6}
$$
The deck law, with
$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},\qquad
(a,c)=L(b,d),
$$
is
$$
F(Q+a,q+b)-F(Q,q)=cQ-dq+\frac{ca-db}{2},\qquad
B_h(Q+a,q+b)=B_h(Q,q).
\tag{1.7}
$$
The metaplectic comb restriction differs from $M_N$ by the fixed
scalar already calculated in the original trace proof. This scalar
is retained in both families and never affects (0.2).

The centered contour kernel constructed from (1.3) has a global
contracting graph, with scalar
$$
\gamma_h(x)=\gamma_0(x)
\left(1+ih\sigma(x)+O(h^2)\right),
\quad \gamma_0>0,\quad \sigma\in C(\mathbb T^2;\mathbb R).
\tag{1.8}
$$
Its proof uses a contraction on continuous sections and uniform
finite jets in $s=\sqrt h$; it does not prove smoothness of $\sigma$.
The relevant proof and the stability of its construction are recalled
in Section 4 below.

The original $\Psi$ is area preserving and Anosov, hence ergodic.
Fixed-time Egorov, trace-product convergence, and the smooth-symbol
quantum ergodicity proof are provided in full in the Round 3 source.
The additional, varying-symbol argument needed here is proved in
the companion Round 9 continuous-symbol stability note.

All these inputs concern this exact corrected quantization and every
odd dimension, including composite dimensions. Their exact source
hashes are recorded in Section 9.

## 2. Exact analytic realization for a fixed real trigonometric polynomial

Fix such a polynomial $v$. This section proves the step not supplied
by changing an abstract scalar potential.

Let $H_a$ denote the bounded holomorphic functions on
$$
S_a=\{(Q,q):|\operatorname{Im}Q|<a,\
|\operatorname{Im}q|<a\},
$$
with the supremum norm. Choose one positive $a$ strictly inside the
original phase and amplitude strips. All strips extend over the full
real plane.

For $\kappa=(k,l)$, define a weighted real shift
$$
(\mathcal W_{\kappa,h}B)(Q,q)
=E_{\kappa,h}(Q,q)B(Q+2\pi hl,q),
\tag{2.1}
$$
$$
E_{\kappa,h}=e^{i\vartheta_{\kappa,h}},\qquad
\vartheta_{\kappa,h}
=2\pi k(Q+\pi hl)
+\frac{F(Q+2\pi hl,q)-F(Q,q)}h.
\tag{2.2}
$$
The apparent quotient is extended continuously at $h=0$.
Expansion of the quadratic part, with an exact integral for $G$,
gives
$$
\begin{split}
\vartheta_{\kappa,h}
={}&2\pi\bigl[(k-3l/4)Q+(l/4)q\bigr]\\
&+h\left(2\pi^2kl-\frac32\pi^2l^2\right)
+2\pi l\int_0^1G_Q(Q+2\pi uhl,q)\,du.
\end{split}
\tag{2.3}
$$
For real $h$, every shift in (2.3) is horizontal. Thus
$$
\sup_{S_a}|E_{\kappa,h}|
\le
\exp\!\left(2\pi a(|k-3l/4|+|l|/4)
+2\pi |l|\,\|G_Q\|_{S_a}\right)
 =:c_{\kappa,a},
\tag{2.4}
$$
uniformly over real $h$. The term multiplying $h$ in (2.3) is
real and creates no growth of the modulus. In particular, no
$\exp(C/h)$ bound and no truncation of the unbounded real variables
are needed.

Set
$$
\mathcal L_{v,h}=\sum_{\kappa}\widehat v(\kappa)
\mathcal W_{\kappa,h},\qquad
\ell_{v,a}=\sum_{\kappa}|\widehat v(\kappa)|c_{\kappa,a}<\infty.
\tag{2.5}
$$
It is a bounded operator $H_a\to H_a$, with norm at most
$\ell_{v,a}$ uniformly in real $h$. Therefore
$$
B_h^v:=e^{\,i2\pi h\mathcal L_{v,h}}B_h
\tag{2.6}
$$
is defined by an absolutely convergent bounded-operator exponential
on the same fixed spatial strip.

Termwise application of (1.2) to (1.3) gives (2.1). Induction on the
number of factors then identifies every term of the exponential
series. On the real plane the kernel series is dominated by
$$
|C_h|\,\|B_h\|_{\mathbb R^2}
\exp\!\left(2\pi|h|\sum_\kappa|\widehat v(\kappa)|\right).
$$
It is therefore absolutely integrable against every Schwartz test
function on $\mathbb R^2$. The bounded $L^2$ exponential of the
self-adjoint operator $\operatorname{Op}_h(v)$ gives the same
distribution kernel:
$$
\boxed{\quad
\mathcal K_{\exp(i2\pi h\operatorname{Op}_h(v))\mathcal U_h}
(Q,q)=C_he^{iF(Q,q)/h}B_h^v(Q,q).
\quad}
\tag{2.7}
$$
The matrix obtained on the comb is exactly
$\exp(iQ_N(v)/N)U_N$, including the common metaplectic scalar.
It is unitary. Neither a polar correction nor an $O(h^\infty)$
kernel substitution has been used.

### 2.1 Spatial periodicity and reality

For the translation in (1.7), the exponent (2.2) changes by
$2\pi(ka+lc)$, an integer multiple of $2\pi$. The real shift
commutes with the deck translation. Hence every
$\mathcal W_{\kappa,h}$, and then (2.6), preserves the amplitude's
deck law.

Analytic conjugation, followed by $(k,l)\mapsto(-k,-l)$, gives
$\mathcal L_{v,-h}\mathcal C=\mathcal C\mathcal L_{v,h}$
for real $v$. Together with $B_{-h}=\mathcal C B_h$, (2.6)
implies
$$
B^v_{-h}=\mathcal C B^v_h.
\tag{2.8}
$$
This is an amplitude identity; no negative-$h$ branch of $C_h$
is required.

### 2.2 Actual finite $h$-jets

For fixed $\kappa$, differentiation of (2.3) in real $h$ gives
bounded coefficients on $S_a$. Differentiating the shifted
function in (2.1) costs one spatial derivative per differentiation.
If $a<a'<a''$ are fixed inside the available strips, Cauchy's
estimate therefore gives, for $r=0,1,2$,
$$
\|\partial_h^r\mathcal L_{v,h}\|_{H_{a'}\to H_a}
\le C_{v,r,a,a'}
\tag{2.9}
$$
for real $h$ in a fixed bounded interval. The constants are finite
for each fixed polynomial, with no claim of uniformity in its degree.

The exponential in (2.6) is bounded on each of these strips by
$\exp(2\pi |h|\ell_{v,a'})$. Differentiating its convergent series,
or using the integral formula for the derivative of a bounded
operator exponential, proves two real-$h$ derivatives from the
outer strip to the inner one. In the second derivative only two
derivative losses occur; allocate one fixed positive strip gap to
each. The remaining exponential factors are bounded on their
respective strips. This proves genuine $C^2_h$ regularity, rather
than an assertion about formal coefficients.

In particular,
$$
\mathcal L_{v,0}B_0=v(Q,F_Q(Q,q))B_0.
$$
Taylor's theorem and (1.5)--(2.6) give
$$
\boxed{\quad
B_h^v=B_0+ih
\bigl[b_1+2\pi v(Q,F_Q)B_0\bigr]+O_v(h^2)
\quad}
\tag{2.10}
$$
in a fixed smaller spatial analytic norm. Cauchy's estimate gives
the same uniform remainder for any required fixed finite number of
spatial derivatives.

There is an alternative direct check avoiding any concern about
accumulating one strip loss per undifferentiated factor. The exact
Weyl multiplication law gives
$$
\mathcal W_{\kappa_1,h}\cdots\mathcal W_{\kappa_n,h}
=\exp\!\left(2\pi^2ih
\sum_{r<s}\omega(\kappa_r,\kappa_s)\right)
\mathcal W_{\kappa_1+\cdots+\kappa_n,h},
\quad \omega(\kappa,\eta)=lk'-kl'.
\tag{2.11}
$$
For frequencies bounded by the fixed degree of $v$, the total
frequency is $O_v(n)$ and the area sum is $O_v(n^2)$.
For real $h$ the central factor has modulus one. Formula (2.3)
bounds the remaining weighted shift by $C_v^n$; its first two
$h$-derivatives cost only a fixed polynomial in $n$ and at
most two spatial derivatives of $B_h$. Take these derivatives
using one fixed outer-to-inner strip gap. The sums of absolute
word coefficients are $s_v^n$. In the exponential series the
factor $1/n!$ therefore dominates all these bounds. Derivatives
of $h^n$ introduce another fixed polynomial in $n$; on a
fixed real interval around zero, the terms of degree $n<2$
are treated directly. This proves uniform convergence of both
derivative series with only the stated fixed strip gap.

## 3. Exact all-time sector construction remains valid

Here are the checks needed to apply the previously proved exact
trace construction to (2.7), rather than assume that arbitrary
analytic amplitudes are quantizations.

The exponential $\exp(i2\pi h\operatorname{Op}_h(v))$ is a sum of
finite Weyl words. The absolute coefficient mass of words of length
$r$ is at most
$$
\frac{(2\pi |h|\,s_v)^r}{r!},
\qquad s_v=\sum_\kappa|\widehat v(\kappa)|.
\tag{3.1}
$$
If $d_v=\max_{\widehat v(\kappa)\ne0}|\kappa|_1$, their real
displacement is at most $2\pi |h|d_v r$. Therefore every fixed
exponentially weighted displacement sum converges. The original
kick has the same property, with its original finite generator and
its original coefficient $t_*/h$. Products of finitely many such
series retain the property: at every fixed $m,h$, the factors
$L^r$ transporting displacements are fixed linear maps, and the
word-length factorials dominate each resulting exponential weight.

Thus the expansion of each fixed power of the new plane operator
into translated metaplectic words has the absolute and
displacement-weighted convergence required by the old exact comb
trace proof. Coherent-state insertion, grouping integer deck
translations modulo $(L^m-I)\mathbb Z^2$, and unfolding each class
are consequently justified by absolute convergence. This step uses
the honest odd-lattice representation and its actual phase; it
does not average Bloch sectors.

There is also a direct check for the common Abel regulator in the
path-kernel representation. Every word has the same quadratic
cyclic Hessian
$$
H_m=-\frac14(6I-R-R^{-1}),
\tag{3.2}
$$
including the coincident edges for $m=1,2$. Its eigenvalues lie in
$[-2,-1]$. Word displacements enter only the real linear part.
The Gaussian integral with regulator $e^{-\epsilon|q|^2}$
has a completed-square factor of modulus at most one and a
determinant prefactor bounded by its limit at $\epsilon=0$,
independently of that real linear part. The absolute word mass
allows dominated convergence through the common Abel limit.
Consequently the resulting full $\mathbb R^m$ sector integrals
are the exact finite traces.

Finally, (2.7) has the same phase $F$. Its strong concavity,
unique critical point in each sector, bounded complex contour, and
coercive decay are unchanged. The amplitude (2.6) is bounded
holomorphic on that contour. The contour deformation and
trace-class edge factorization therefore apply with this actual
amplitude. Uniform spatial derivatives and finite $h$-jets
are supplied by (2.9)--(2.10).

These checks establish the entire analytic input for the new
endpoint; they do not assume that editing a formal orbit weight
produces a finite-dimensional unitary matrix.

## 4. Graph response and the scalar transformation law

For completeness, the relevant perturbation property of the
dominated graph is derived here. Center (2.7) along an edge
$x\mapsto\Psi x$, put $s=\sqrt h$, and use the bounded
contour that is $(1-i)sy$ near the critical point. With the
normalization of the existing Gaussian construction, let
$$
K_s(x)=K_0(x)+sK_1(x)+s^2K_2(x)+s^3K_3(x)
+O_{\mathcal S_1}(s^4).
\tag{4.1}
$$
The remainder is uniform in the real base point. To recall why
the analytic amplitude estimates suffice, the straight part of
the contour gives polynomial times Gaussian majorants for all
terms through this order. The bounded nonstraight tails are
exponentially small in $1/h$. Spatial Cauchy estimates and two
real-$h$ derivatives of the amplitude control the remainder in
trace norm. The fixed phase already has the required analytic
derivatives and uniform coercivity.

Formula (2.10), evaluated at the center of an edge, gives
$$
K_0^v=K_0,\qquad K_1^v=K_1,\qquad
K_2^v(x)-K_2(x)
=i\,2\pi v(\Psi x)K_0(x).
\tag{4.2}
$$
Changes in the spatial argument of $v$ start at order $s^3$
and cannot affect the scalar coefficient at $s^2=h$.

Let $P=e_0e_0^*$ be the top eigenspace of the fixed Gaussian
kernel. The normalized graph quotient is
$$
g_x(w)=
\frac{(I-P)K_s(x)(e_0+w)}
{e_0^*K_s(x)(e_0+w)}.
\tag{4.3}
$$
It acts on continuous sections using the invertible base map.
In the fixed neighborhood already verified for the original
phase, its contraction constant is less than $0.172$ and the
denominator is bounded away from zero. The perturbation (4.2)
multiplies numerator and denominator by the same scalar at order
$s^2$. It therefore contributes zero to the order-$s^2$
variation of the normalized graph. This conclusion remains
valid for the full past-orbit fixed section: its coefficient
equation is $w_2=\mathcal T w_2+b_2$, with
$\|\mathcal T\|<0.172$, and the additional term in $b_2$
vanishes.

The scalar is
$\gamma_s(x)=e_0^*K_s(x)(e_0+w_s(x))$. Its additional
coefficient at order $h$ is thus precisely
$i2\pi v(\Psi x)\gamma_0(x)$. The finite coefficient recursion
and contraction estimate also control the $O(s^4)$ remainder:
an approximate graph with defect $C_vs^4$ is within
$C_vs^4/(1-0.172)$ of the exact graph.

Reflection of the transverse variables gives
$K_{-s}=\mathcal R K_s\mathcal R$. Uniqueness of the normalized
graph makes $\gamma_s$ even in $s$, so the odd terms vanish.
Reality (2.8) makes the order-$h$ coefficient purely imaginary.
We obtain, uniformly in $x$,
$$
\boxed{\quad
\frac{\gamma_h^v(x)}{\gamma_0(x)}
=1+ih\,[\sigma(x)+2\pi v(\Psi x)]+O_v(h^2).
\quad}
\tag{4.4}
$$

For each fixed $v$, its contour kernels converge to the same
$K_0$ as $h\to0$. Thus they eventually belong to the same
numerical graph neighborhood. The graph decomposition has the
same consecutive mixed-product cancellations and, after
increasing the dimension threshold if necessary, the same
bounds
$$
\|\mathcal B_h^v\|<0.174,\qquad
\|\mathcal B_h^v\|_1<0.209.
\tag{4.5}
$$
The summed residual trace is therefore at most
$$
\frac{0.209}{0.174}
\left(0.174\sqrt{3+2\sqrt2}\right)^m
<1.202(0.421)^m.
\tag{4.6}
$$
This bound uses the actual sector count
$|\det(L^m-I)|<(3+2\sqrt2)^m$ and the unchanged prefactor.
It is valid for every positive iterate at each dimension above
the applicable threshold.

## 5. Choosing one sequence for all odd dimensions

Set the fixed continuous real function
$$
v=-\frac1{2\pi}\sigma\circ\Psi^{-1}.
\tag{5.1}
$$
Let $v_j$ be its two-dimensional Fejér means. These are real
trigonometric polynomials,
$$
\|v_j-v\|_\infty\to0,\qquad
\|v_j\|_\infty\le\|v\|_\infty,\qquad
\int v_j=\int v=:\mu.
\tag{5.2}
$$
Uniform convergence follows by splitting convolution with the
positive Fejér approximate identity into a small neighborhood,
where uniform continuity applies, and its complement, whose
kernel mass tends to zero.

For each fixed $j$, Sections 2--4 supply a finite $C_j$ and a
positive $h_j$ such that
$$
\left|\frac{\gamma_h^{v_j}(x)}{\gamma_0(x)}
-1-ih[\sigma(x)+2\pi v_j(\Psi x)]\right|
\le C_j h^2,\qquad 0<h\le h_j,
\tag{5.3}
$$
and the common graph bounds (4.5)--(4.6) hold. They also give a
finite $\ell_{v_j,a}$ for (2.5). Choose increasing integer
thresholds $n_j$ so large that for every $N\ge n_j$:

- $h_N\le h_j$ and $C_jh_N\le1/j$;
- $h_N\ell_{v_j,a}\le1/j$, retaining a common uniformly bounded
  exact amplitude on the chosen fixed strip;
- all the norm-approximation thresholds in the companion
  continuous-symbol selection proof hold for this $j$ and
  every earlier index;
- $N$ exceeds the finite Fourier alias threshold for $v_j$.

Each is an eventual condition for fixed $j$, so finitely many
conditions can be imposed simultaneously. Insist also on
$n_{j+1}>n_j$. This defines one $j(N)\to\infty$ on every
sufficiently large odd $N$, rather than selecting a
subsequence of dimensions. Any finite initial segment can be
defined by $\widetilde U_N=U_N$.

For $j=j(N)$, put
$$
\epsilon_N=2\pi\|v_j-v\|_\infty+\frac1j\longrightarrow0.
$$
Equations (5.1) and (5.3) give
$$
\sup_x\left|
\frac{\widetilde\gamma_N(x)}{\gamma_0(x)}-1\right|
\le h_N\epsilon_N.
\tag{5.4}
$$
This proves (0.3).

If $z_r=\widetilde\gamma_N(\Psi^r x)/
\gamma_0(\Psi^r x)-1$, the elementary telescoping bound yields
$$
\left|\prod_{r=0}^{m-1}(1+z_r)-1\right|
\le(1+h_N\epsilon_N)^m-1
\le \exp(mh_N\epsilon_N)-1.
\tag{5.5}
$$
For $m\le BN$, the right side is at most
$\exp(B\epsilon_N/(2\pi))-1\to0$. This proves (0.4), with
one sequence valid for every fixed $B$. No uniformity over
unbounded $B$ is claimed or needed.

The common graph threshold in the selection preserves (4.6)
for this entire sequence, at every positive time. The phase
and classical map remain exactly the original ones.

## 6. Why this varying modification preserves the local laws

This section records the critical estimates, proved fully in
the companion continuous-symbol note; no convergence of
the derivatives of $v_j$ is assumed.

For any fixed real smooth $a$,
$$
\limsup_{N\to\infty}\|Q_N(a)\|\le\|a\|_\infty.
\tag{6.1}
$$
An elementary proof is useful. Given $M>\|a\|_\infty$, the
function $c=\sqrt{M^2-a^2}$ is smooth real. The finite Weyl
product formula and rapid Fourier decay give
$$
Q_N(a)^2+Q_N(c)^2=M^2I+o_{\rm op}(1).
$$
Positivity of $Q_N(c)^2$ proves (6.1), on letting $M$
decrease to $\|a\|_\infty$.

Apply (6.1) to the finitely many $v_j-v_l$, $l\le j$, when
choosing $n_j$. The thresholds can ensure
$$
\|Q_N(v_j-v_l)\|\le\|v_j-v_l\|_\infty+1/j
\quad(N\ge n_j,\ l\le j).
\tag{6.2}
$$
For $B_N=Q_N(v_{j(N)})$, this implies bounded operator norm
and, for every fixed $l$,
$$
\limsup_N\|B_N-Q_N(v_l)\|\le\|v-v_l\|_\infty.
\tag{6.3}
$$

Along $V_N(t)=e^{itB_N/N}U_N$, fixed powers remain
$O(1/N)$-close in operator norm to those of $U_N$.
For fixed $l$, the time-average proof using fixed-time
Egorov and ergodicity consequently gives quantum ergodicity
uniformly in $t$ and in the choice of eigenbasis. Equation
(6.3) allows $l\to\infty$ after $N\to\infty$, proving
$$
\sup_{t,\ {\rm eigenbases}}\frac1N\sum_j
\left|\langle\psi_{j,N,t},B_N\psi_{j,N,t}\rangle-\mu\right|^2
\longrightarrow0.
\tag{6.4}
$$
Only a fixed smooth observable is transported at each stage of
this argument. Growing derivatives of $v_{j(N)}$ are never
inserted into Egorov.

Absolutely continuous real eigenangle branches in turns satisfy,
almost everywhere,
$$
\theta'_j(t)=\frac1{2\pi N}
\langle\psi_{j,N,t},B_N\psi_{j,N,t}\rangle.
\tag{6.5}
$$
At a degeneracy choose a basis diagonalizing the compression of
$B_N$ to that eigenspace; (6.4) covers this basis as well.
Cauchy--Schwarz and integration give, with
$\phi_N=\mu/(2\pi N)$,
$$
\max_j N|\theta_j(1)-\theta_j(0)-\phi_N|\le C,\qquad
\sum_j|\theta_j(1)-\theta_j(0)-\phi_N|\to0.
\tag{6.6}
$$
The scalar rotation is absorbed exactly by the uniform origin.

Couple both spectra with the same origin after this rotation.
For $f\in W^{1,1}(\mathbb R)$, periodization and a change of
variable give
$$
\mathbb E_\alpha\sum_{j,\ell}
|f(N(\theta_j(1)-\phi_N-\alpha+\ell))
-f(N(\theta_j(0)-\alpha+\ell))|
\le \|f'\|_1
\sum_j|\theta_j(1)-\theta_j(0)-\phi_N|.
\tag{6.7}
$$
Nonnegative compact smooth Laplace tests therefore differ by
$o(1)$.

For full $H_{\rm diag}$ transfer one needs moments in addition.
If one endpoint has $H_{\rm diag}$, a positive bandlimited
Schwartz majorant on any fixed compact interval, expanded by
partitions of repeated labels, bounds all local-count moments.
The bounded maximum displacement in (6.6) transfers those
moments to the other endpoint on enlarged intervals.
Translation invariance and Minkowski's inequality then bound
all moments of Schwartz-weighted local counts, including their
tails. Finally, for periodized test weights $w_j^0,w_j^1$,
$$
|e_k(w^1)-e_k(w^0)|
\le\frac{\sum_j|w_j^1-w_j^0|}{(k-1)!}
\left(\sum_j(w_j^0+w_j^1)\right)^{k-1}.
\tag{6.8}
$$
Equation (6.7) makes the first factor tend to zero in $L^1$.
Truncation and the moment of order $k+1$ control the second
factor on its complement. Thus the factorial-moment difference
is $o(1)$. The argument is symmetric in the two endpoints
and proves (0.2), with no assumed moment bounds on an endpoint
that has not been supplied by one of the two $H_{\rm diag}$
hypotheses.

## 7. What is new relative to the earlier source

The earlier smooth stability theorem already supplied the
quantum-ergodicity mechanism and its all-order moment transfer.
Those parts are not new claims of this pass.

The new construction combines:

1. a varying sequence uniformly approximable in operator norm
   by fixed smooth quantizations, avoiding the missing
   smoothness of the graph potential;
2. an exact bounded weighted-shift exponential on a common
   spatial analytic strip, giving real unitary endpoints;
3. a single choice of dimension thresholds satisfying both
   the spectral and analytic estimates;
4. the uniform $o(N^{-1})$ scalar estimate (0.3), which gives
   (0.4) at every fixed Heisenberg-scale multiple.

This is a new result within the accumulated proof record. No
claim of historical priority in the literature is made.

## 8. The global estimate still missing

The exact trace formula for the new family has a sum over
all original classical periodic points, with unchanged action
phases and modified scalar weights, plus (4.6). Schematically,
with the actual deck and metaplectic phases retained,
$$
\operatorname{Tr}\widetilde U_N^m
=\sum_{x\in\operatorname{Fix}\Psi^m}
\mathcal A_0(x,m)e^{iS_{x,m}/h_N}
[1+\varepsilon_{N,m}(x)]+R_{N,m},
\tag{8.1}
$$
where
$$
\sup_{\substack{m\le BN\\x\in\operatorname{Fix}\Psi^m}}
|\varepsilon_{N,m}(x)|\to0,\qquad
|R_{N,m}|\le1.202(0.421)^m.
\tag{8.2}
$$
Here $\mathcal A_0$ denotes the actual positive leading
amplitude; the notation in (8.1) does not replace it by a
constant Lyapunov exponent.

From (8.2) alone one obtains only
$$
\left|\sum_x
\mathcal A_0(x,m)e^{iS_{x,m}/h_N}
\varepsilon_{N,m}(x)\right|
\le\sup_x|\varepsilon_{N,m}(x)|
\sum_x\mathcal A_0(x,m).
\tag{8.3}
$$
The last sum grows exponentially in the orbit length in this
setting. Thus (8.3) is not an $o(1)$ trace estimate at
$m\asymp N$. Neither (0.3) nor unitarity licenses replacing
the left side by an unweighted norm of $\varepsilon$.

No estimate of this full signed error sum, the original fixed
weighted pair sum, or the higher $H_{\rm diag}$ sums is
claimed here. The theorem improves the quantization available
for a future cancellation argument; it does not supply that
argument.

## 9. Exact source provenance

All old sources were retained unchanged.

| Source | SHA-256 |
|---|---|
| research_continuation_2026_10_20/exact_amplitude.md | 69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e |
| research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md | 42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b |
| research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md | c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1 |
| research_round2_2026_10_20/adversarial_all_time_audit.md | dbc1070d04c238213138b5eb433776d3ce0dfb6e9c07fca7eb90ebd9b42c7c25 |
| research_round3_2026_10_21/subprincipal_stability_theorem.md | 63597dea1e627925280e79644ccc54ed68b9327c9ab757f6eea9ad69962e2381 |

The new continuous-symbol selection proof is in the companion
Round 9 note. Its final hash and this note's audit are to be
recorded in the round manifest after review.
