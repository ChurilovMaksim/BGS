# Sharp coercivity for the resonance functional on a Fourier line

Date: 21 September 2026.

Status: self-contained project proof with exact finite regressions and separate Wolfram checks in the recovered handoff. No independent referee, Lean certificate, global priority claim, or BGS conclusion is asserted.

## 1. Statement

Let \(A\in SL(2,\mathbb Z)\), \(|\operatorname{tr}A|>2\). On \(\mathbb T^2\), let

\[
e_k(x)=e^{2\pi i k\cdot x},\qquad C_Ag(x)=g(A^Tx),
\]

and use the standard Poisson bracket. Put

\[
\sigma=\operatorname{sign}(\operatorname{tr}A),\qquad
B=\sigma A,\qquad
T=\operatorname{tr}B\ge3,
\]

\[
\lambda=\frac{T+\sqrt{T^2-4}}2,
\qquad
a_0=1,\quad a_1=T+1,\quad
a_{j+2}=Ta_{j+1}-a_j.
\]

Fix any nonzero \(v\in\mathbb Z^2\), not necessarily primitive, and set

\[
D=\det(v,Bv)\ne0,\qquad w=v+Bv.
\]

For nonconstant real \(G\in H^{1+\beta}(\mathbb T)\), \(\beta>0\), write

\[
G(t)=c_0+\sum_{n\ge1}
(c_ne^{2\pi int}+\overline{c_n}e^{-2\pi int}),
\qquad d_n=nc_n,
\]

\[
g(x)=G(v\cdot x),\qquad
E_\beta=\sum_{n\ge1}n^{2\beta}|d_n|^2,
\qquad
h=\frac{\{g,C_Ag\}}{4\pi}.
\]

For \(m\ge1\) let

\[
J_m=\sum_{j\in\mathbb Z}\widehat h(A^j(mw)),
\]

and define

\[
\rho_\beta=2\sum_{j\ge0}(a_ja_{j+1})^{-\beta},
\qquad
\kappa_\beta=1-\rho_\beta.
\]

If \(\kappa_\beta>0\), then

\[
\boxed{
\pi|D|\kappa_\beta E_\beta
\le
\sum_{m\ge1}m^{2\beta}|J_m|
\le
\pi|D|(1+\rho_\beta)E_\beta.}
\tag{1}
\]

The lower constant \(\kappa_\beta\) is optimal over nonconstant real trigonometric polynomials \(G\). Consequently the dynamical variance

\[
\Gamma_A(g)=
\sum_{\text{oriented }A\text{-orbits }O}
\left|\sum_{k\in O}\widehat h(k)\right|^2
\tag{2}
\]

is strictly positive, every Green--Kubo/orbit rearrangement used here is absolutely convergent, and \(h\) is not an \(L^2\) dynamical coboundary.

## 2. Exact Fourier reduction

The map

\[
x\mapsto(v\cdot x,Bv\cdot x)
\]

is a finite covering of degree \(|D|\), so the weak derivative product defining \(h\) belongs to \(L^2\). Fourier labels \(kv+\ell Bv\) are unique and

\[
\frac{\widehat h(kv+\ell Bv)}{\pi}
=
-D\,k\ell\,c_kc_{\sigma\ell}.
\tag{3}
\]

In the basis \((v,Bv)\),

\[
B^jw=(-a_{j-1},a_j),\qquad
B^{-j}w=(a_j,-a_{j-1}),\qquad j\ge1.
\]

Writing \(q_m=-J_m/(\pi D)\), one obtains

\[
q_m=d_m^2
-2\sum_{j\ge0}
\overline{d_{a_jm}}\,d_{a_{j+1}m},
\qquad \sigma=+1,
\tag{4a}
\]

\[
q_m=|d_m|^2
-2\sum_{j\ge0}
\Re(d_{a_jm}d_{a_{j+1}m}),
\qquad \sigma=-1.
\tag{4b}
\]

The negative-trace conjugation is essential for arbitrary Fourier phases.

For positive integers \(a,b\),

\[
\sum_{m\ge1}m^{2\beta}|d_{am}d_{bm}|
\le(ab)^{-\beta}E_\beta.
\tag{5}
\]

Applying (5) to (4) gives both sides of (1).

## 3. Absolute convergence and exclusion of coboundaries

For every zero-mean \(h\in H^\beta(\mathbb T^2)\), \(\beta>0\), choose expanding/contracting covectors for \(B\). The invariant integral quadratic form \(\det(k,Ak)\) is nonzero on every nonzero integer \(k\), hence there is \(c_A>0\) with

\[
N(k)N(A^nk)\ge c_A\lambda^{|n|}.
\]

Weighted Cauchy--Schwarz yields

\[
\sum_{k\ne0}|\widehat h(k)\widehat h(A^nk)|
\le
c_A^{-\beta}\lambda^{-\beta|n|}
\sum_{k\ne0}N(k)^{2\beta}|\widehat h(k)|^2.
\tag{6}
\]

Thus the Green--Kubo series and orbit-square expansion converge absolutely. If \(h=u-C_Au\) with \(u\in L^2\), the absolutely convergent coefficient sum telescopes to zero on every orbit. A nonzero \(J_m\) therefore rules out such a transfer.

## 4. Exact \(H^2\) constant

The recurrence satisfies

\[
a_{j+1}^2-a_ja_{j+2}=T+2
\]

and the telescoping identity

\[
\sum_{j=0}^{J}\frac1{a_ja_{j+1}}
=
\frac{(T+1)-a_{J+2}/a_{J+1}}{T+2}.
\]

Letting \(J\to\infty\) gives

\[
\sum_{j\ge0}\frac1{a_ja_{j+1}}=\frac1{\lambda+1},
\]

hence

\[
\boxed{
\kappa_1=\frac{\lambda-1}{\lambda+1}
=\sqrt{\frac{T-2}{T+2}}.}
\tag{7}
\]

For the project matrix \(A=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)\), \(v=(1,0)\), one has \(D=4\) and

\[
\boxed{\kappa_1=\frac1{\sqrt2}.}
\tag{8}
\]

For \(A=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)\) the same \(v\) gives \(D=2\); these conventions must not be interchanged.

## 5. \(H^{3/2}\) positivity for large trace

At \(\beta=1/2\),

\[
a_ja_{j+1}\ge(T+1)\lambda^{2j},
\]

so

\[
\rho_{1/2}
\le
\frac{2}{\sqrt{T+1}(1-\lambda^{-1})}.
\tag{9}
\]

For \(T\ge6\),

\[
\boxed{
\kappa_{1/2}
\ge1-\frac{1+\sqrt2}{\sqrt7}>0.}
\tag{10}
\]

Thus every nonconstant real Fourier-line observable in \(H^{3/2}\) has strictly positive resonance variance whenever \(|\operatorname{tr}A|\ge6\).

## 6. Sharpness

For fixed \(\beta\) with \(\kappa_\beta>0\), set \(x_n=n^\beta d_n\) and normalize \(\sum x_n^2=1\). Finite multiplicative boxes built from the primes dividing \(a_0,\ldots,a_{J+1}\) are asymptotically invariant under each fixed dilation \(n\mapsto a_jn\). In (4), the first \(J\) cross terms therefore approach their maximal negative contribution, while the tail is bounded by \(4\sum_{j>J}(a_ja_{j+1})^{-\beta}\). Letting the box size and then \(J\) tend to infinity produces trigonometric polynomials for which the ratio in the lower side of (1) tends to \(\kappa_\beta\).

## 7. Boundary

This closes the all-members resonance-nondegeneracy problem on a complete infinite-dimensional Fourier-line class, for arbitrary phases and both trace signs. It does not settle the full two-dimensional analytic cohomological equation: a symbol with several independent Fourier directions has additional decompositions not controlled by the scalar dilation argument. The frozen BGS symbol has several directions. Even full analytic nondegeneracy would still not replace the separate Heisenberg-time joint-trace estimate required for microscopic BGS.
