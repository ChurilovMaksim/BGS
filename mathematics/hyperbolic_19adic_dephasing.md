# Exact hyperbolic dephasing on the subsequence N = 19^k

Date: 21 September 2026.

Status: recovered direct-attack theorem from 15 September, with exact
arithmetic replay and a repaired source-to-theorem presentation of the
non-archimedean van der Corput step. The Parseval identities are exact.
The pointwise incomplete-sum estimate is a project proof using Cluckers'
analytic p-adic van der Corput theorem as an external input. None of these
statements evaluates the complete quantum BGS path sum.

## Long order of the fixed cat

Let

\[
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad p=19,\qquad N=p^k.
\]

Identify \((x,y)\) with \(x+y\sqrt2\) in the unramified quadratic extension
of \(\mathbb Z_{19}\). Multiplication by \(\lambda=3+2\sqrt2\) is represented
by \(S\). Exact arithmetic gives

\[
\lambda^{10}\equiv-1\pmod{19},\qquad
\lambda^{20}\equiv1+19(4\sqrt2)\pmod{19^2}. \tag{1}
\]

Thus \(\lambda\bmod19\) has order 20. Writing
\(g=\lambda^{20}=1+19u\) with \(u\) a unit, the binomial lifting identity

\[
g^{19^j}=1+19^{j+1}u_j,\qquad u_j\in\mathcal O^\times
\]

shows inductively that \(g\) has exact order \(19^{k-1}\) modulo \(19^k\).
Therefore

\[
\boxed{\operatorname{ord}_{19^k}(S)
=20\,19^{k-1}={20\over19}N>N.} \tag{2}
\]

## Primitive orbits and exact Parseval

For \(r=(r_1,r_2)\),

\[
\det(r,Sr)=2(r_1^2-2r_2^2). \tag{3}
\]

Since 2 is a quadratic non-residue modulo 19, every vector primitive modulo
19 makes (3) a unit; hence \(r,Sr\) are a basis over
\(\mathbb Z/19^k\mathbb Z\). If \(S^dr=r\), then also \(S^d(Sr)=Sr\), so
the basis property forces \(S^d=I\). Every primitive vector has the full
period (2).

Let \(J\) be distinct times in an interval shorter than this period and let
\(a_j\in\mathbb C\). Character orthogonality gives

\[
\boxed{
\sum_{\xi\in(\mathbb Z/N\mathbb Z)^2}
\left|\sum_{j\in J}a_j e_N(\xi\cdot S^jr)\right|^2
=N^2\sum_{j\in J}|a_j|^2.} \tag{4}
\]

For \(|J|=L\), \(a_j=1\), Chebyshev gives

\[
\#\left\{\xi:
\left|\sum_{j\in J}e_N(\xi\cdot S^jr)\right|>
\Lambda\sqrt L\right\}
\le {N^2\over\Lambda^2}. \tag{5}
\]

This is internal finite Fourier orthogonality, not an ensemble average.

If \(r=19^s r_0\), with \(r_0\) primitive, then the period is
\(T_{k,s}=20\,19^{k-s-1}\), and the same expansion gives

\[
\sum_\xi\left|\sum_{j\in J}a_j e_N(\xi\cdot S^jr)\right|^2
=N^2\sum_{c\bmod T_{k,s}}
\left|\sum_{\substack{j\in J\\j\equiv c\;(T_{k,s})}}a_j\right|^2,
\tag{6}
\]

hence

\[
\boxed{
\sum_\xi|\cdots|^2
\le N^2\left(1+{|J|\over T_{k,s}}\right)
\sum_{j\in J}|a_j|^2.} \tag{7}
\]

## Pointwise p-adic finite type

Let

\[
K=\mathbb Q_{19}(\sqrt2),\qquad
g=\lambda^{20}=\exp(19c),\qquad c=u\sqrt2,\quad
u\in\mathbb Z_{19}^\times. \tag{8}
\]

For primitive \(r\) and primitive dual frequency \(\xi\), trace pairing gives

\[
\xi\cdot S^jr=\operatorname{Tr}_{K/\mathbb Q_{19}}(C\lambda^j)
\]

with \(C\) a unit. Split \(j=a+20n\), put \(C_a=C\lambda^a\), and lower the
conductor by one:

\[
F_a(x)=19^{-1}
\left\{\operatorname{Tr}(C_a\exp(19cx))-\operatorname{Tr}(C_a)\right\}
\in\mathbb Z_{19}\{x\}. \tag{9}
\]

Fourier completion adds only a linear twist
\(\Phi_{a,h}(x)=F_a(x)-hx\). If \(C_a=A+B\sqrt2\bmod19\), then

\[
19^{-1}F_a''\equiv4Au^2,\qquad
19^{-2}F_a'''\equiv8Bu^3\pmod{19}. \tag{10}
\]

Since \(C_a\) is a unit, either \(A\) is a unit or \(B\) is. Hence uniformly
in \(x\) and \(h\):

- quadratic branch: \(|\Phi''|_{19}=19^{-1}\);
- cubic branch: \(|\Phi'''|_{19}=19^{-2}\).

## Incomplete hyperbolic sum theorem

Cluckers' analytic non-archimedean van der Corput lemma,
[arXiv:1001.2013, Proposition 3.3](https://arxiv.org/abs/1001.2013),
gives \(O(|y|^{-1/d})\) decay when the \(d\)-th derivative of an analytic
phase is bounded below by one.

For \(M=19^{k-1}\), the complete twisted sum equals

\[
M\int_{\mathbb Z_{19}}
\psi\!\left(19^{-(k-1)}\Phi_{a,h}(x)\right)dx. \tag{11}
\]

In the quadratic branch divide the phase by 19 and compensate the
oscillatory parameter by 19; in the cubic branch divide by \(19^2\) and
compensate by \(19^2\). These are fixed powers and only alter the constant.
The Gauss norms remain uniformly bounded in \(a,h,r,\xi\). Cluckers'
proposition therefore gives

\[
\left|\sum_{n\bmod M}e_M(\Phi_{a,h}(n))\right|
\le C M^{2/3}, \tag{12}
\]

uniformly in \(h\), with the stronger \(CM^{1/2}\) bound in the quadratic
branch. The unnormalized Fourier transform of an interval has
\(\ell^1\)-norm \(O(M\log M)\), while Fourier inversion contributes \(1/M\).
Thus

\[
\left|\sum_{n\in I}e_M(F_a(n))\right|
\le C M^{2/3}\log M. \tag{13}
\]

Summing the twenty residue classes gives

\[
\boxed{
\left|\sum_{j\in J}e_N(\xi\cdot S^jr)\right|
\le C N^{2/3}\log N} \tag{14}
\]

for primitive \(r,\xi\) and every consecutive interval \(J\) of length at
most \(N\).

If \(\xi=19^s\xi_0\) with \(\xi_0\) primitive, reduction to the effective
conductor \(19^{k-s}\), followed by splitting into \(O(19^s)\) effective
pieces, gives

\[
\boxed{
\left|\sum_{j\in J}e_N(\xi\cdot S^jr)\right|
\le C N^{2/3}19^{s/3}\log N.} \tag{15}
\]

Fresh finite regression is in
[hyperbolic_19adic_audit.py](../computations/verification/hyperbolic_19adic_audit.py).

## Boundary and the v9 correction

Equations (4)--(15) act directly on Heisenberg-length hyperbolic time phases.
They do not prove that every non-CUE configuration in the full tensor/path
expansion contains a free variable to which these sums apply, and they do not
evaluate the surviving signed main sector.

An earlier v9 dossier used a two-frequency expression
\(A\lambda^j+B\lambda^{-j}\) as though a cited Bourgain theorem supplied the
required uniform incomplete single-sum estimate. The 15 September source
audit found that it did not. That theorem and its sliding-variable corollary
are retracted. The maintained \(19^k\) theorem is a replacement, not a
validation of v9.
