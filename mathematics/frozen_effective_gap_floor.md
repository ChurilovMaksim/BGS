# An effective but submicroscopic gap floor for the frozen propagator

**Claim ID:** `BGS-FM-011`. **Status:** project proof conditional on
the cited primary external theorem, whose exact constants and hypotheses
were checked; author-level audit of the application, no independent referee
or computer-formalized proof. Adapted from §7 of the submitted
`NEW_RESULTS_RU(1).md` (source hash and audit in
[`record/two_continuations_review_20260924.md`](../record/two_continuations_review_20260924.md)).
This strengthens `BGS-FM-008` only in the formal sense that the
otherwise qualitative nonzero gap has an explicit, astronomically
small \(N\)-dependent lower bound.

## Statement

Let \(N\ge3\) be odd with \(7\nmid N\), \(\tau=10^{-80}\), and let
\(e^{2\pi i\theta_j}\) be the eigenvalues of the **unchanged**
\(U_N=e^{i\tau NA_N}M_N\). Define positive integers
\[
\begin{gathered}
J=N(N-1),\quad d_*=4NN!,\quad
Q_*=N!(2000^2d_*)^N,\quad
K_*=N\,2^{14d_*J},\\
C_*=(2N^2)^N2^J,\quad D_*=2Nd_*JQ_*,\quad
H_*=(K_*^JC_*)^{d_*},\\
q_*=800Q_*10^{80},\qquad
S_*=6d_*N(N!)D_*,\\
\mathcal B_N=
3d_*S_*^N\log H_*+(2Nq_*S_*)^{18S_*^N}
Jd_*\log(2K_*).
\end{gathered}                                                \tag{1}
\]
Then for \(i\ne j\),
\[
\boxed{\operatorname{dist}(\theta_i-\theta_j,\mathbb Z)
 \ge \frac{2^{-J/2}}{\pi}\exp(-\mathcal B_N/2).}              \tag{2}
\]
This bound is far **smaller** than the microscopic spacing \(N^{-1}\);
it gives no pair correlation, uniform local occupancy, Abel bound,
or CUE law. Nothing is asserted at \(7\mid N\), and \(N=7\) has
exact degeneracies.

## Exact external input

[D. Roy, *Une version effective du théorème de
Lindemann–Weierstrass*, arXiv:1607.00579v1,
Theorem 1.1](https://arxiv.org/pdf/1607.00579v1.pdf) proves:
for \(r\) algebraic numbers \(\alpha_1,\ldots,\alpha_r\)
linearly independent over \(\mathbb Q\), all conjugates bounded
by \(c\), and \(q\alpha_\ell\) algebraic integers for an integer
\(q>0\), set \(d=[\mathbb Q(\alpha_1,\ldots,\alpha_r):\mathbb Q]\).
If a nonzero integer polynomial \(P\) has total degree at most \(D\)
and coefficient bound \(H\), for integers \(D,H\ge1\), then
\[
|P(e^{\alpha_1},\ldots,e^{\alpha_r})|
\ge H^{-3dS^r}\exp[-(cqS)^{18S^r}],
\qquad S=6dr(r!)D.                                         \tag{3}
\]
The printed theorem allows complex algebraic exponents. This
source supplies neither a model-specific trace cancellation nor
an effective constant independent of the algebraic degree.

## Integral frequency basis and height controls

Set \(E_0=\mathbb Q(\zeta_N,i,\sqrt N)\), and let \(E\) be its
extension containing all eigenvalues \(a_j\) of \(A_N\).
The field \(E_0/\mathbb Q\) is abelian and
\([E_0:\mathbb Q]\le4N\); the splitting field degree is
\([E:\mathbb Q]\le d_*\). Every embedding of \(E_0\)
commutes with complex conjugation on \(E_0\). Applying an
embedding to the raw Hermitian matrix \(A_N\) gives another
Hermitian matrix, with kick terms and eigenvalues bounded by
\(79/50\); its eigenvalues are the conjugates of \(a_j\).
Thus \(\beta_j=800a_j\) are totally real algebraic integers:
in the path gauge, \(800A_N=8H\), with \(H=100A_{\rm path}\);
\(8H\) has integral algebraic entries by direct inspection of
the Fourier coefficients with denominators at most \(8\).
All conjugates of \(\beta_j\) have modulus \(<2000\).

Choose a \(\mathbb Q\)-basis
\(\beta_1,\ldots,\beta_r\) from the \(\beta_j\),
where \(1\le r\le N\). Its trace Gram matrix
\(G_{\ell k}=\operatorname{Tr}_{E/\mathbb Q}
(\beta_\ell\beta_k)\) is an integral positive-definite
matrix: each summand of the trace of a real square is
nonnegative, and the \(\beta_\ell\) are linearly independent.
With \(g=\det G\ge1\), Cramer's rule and
\(|G_{\ell k}|,|\operatorname{Tr}(\beta_\ell\beta_j)|
\le2000^2d_*\) give integers \(n_{\ell j}\) such that
\[
\beta_j=g^{-1}\sum_\ell n_{\ell j}\beta_\ell,\qquad
1\le g\le Q_*,\quad |n_{\ell j}|\le Q_* .                 \tag{4}
\]
Set \(\alpha_\ell=i\tau N\beta_\ell/(800g)\).
They are linearly independent over \(\mathbb Q\), and
\[
e^{i\tau Na_j}=\prod_\ell(e^{\alpha_\ell})^{n_{\ell j}},
\quad |\sigma(\alpha_\ell)|\le2N,\quad
q\alpha_\ell=iN\beta_\ell\ \text{integral},\quad
q=800g\,10^{80}\le q_* .                                \tag{5}
\]
Here \(i\in E_0\) and \(g\ge1\); the deliberately huge \(c=2N\)
is valid for every embedding of the exponent field.

Let \(P_j\) be the algebraic spectral projectors of \(A_N\), and
\[
\mathscr P(X)=\operatorname{Disc}_w
  \det\!\left(wI-\sum_{j=1}^N X_jP_jM_N\right).
                                                               \tag{6}
\]
Its total degree is \(J\). When \(|X_j|=1\), the matrix
inside is unitary, also after every embedding of the
coefficient field: the embedded \(P_j\) remain orthogonal
spectral projectors and the embedded \(M_N\) is a unitary
finite Fourier matrix (a sign of \(\sqrt N\) changes only a
global factor). Thus \(|\sigma\mathscr P(X)|\le2^J\).
Fourier coefficient extraction on the \(N\)-torus bounds
each coefficient by \(2^J\). There are fewer than
\((2N^2)^N\) monomials, giving coefficient \(\ell^1\)-norm
at most \(C_*\).

Put \(b_j=4000a_j\) and
\(\Delta=\prod_{i<j}(b_i-b_j)^2\ne0\).
The \(b_j\), and \(\Delta P_j\), are algebraic integers
entry by entry, using the explicit spectral-projector
product and cancelling its denominators against \(\Delta\).
Also \(NM_N=\sqrt N\) times roots of unity is integral.
Therefore \(K=N|\operatorname{Norm}_{E/\mathbb Q}\Delta|\)
is a positive integer and \(KP_jM_N\) is integral.
All conjugate differences \(|\sigma(b_i-b_j)|<2^{14}\),
so \(K\le K_*\). It follows that all coefficients of
\(K^J\mathscr P\) are algebraic integers.

Substitute \(X_j=\prod_{\ell=1}^rZ_\ell^{n_{\ell j}}\).
The resulting Laurent polynomial is nonzero: substitution
along \(Z_\ell=e^{\alpha_\ell t/t_*}\) recovers the
discriminant of \(e^{itA_N}M_N\), which is not identically
zero by the imaginary-time witness in `BGS-FM-008`.
Take its product over all field embeddings. This is a
nonzero **integer Laurent polynomial**. Multiplication by
\(\prod_\ell Z_\ell^{d_*JQ_*}\) clears all negative powers.
The resulting integer polynomial \(R\) satisfies
\[
\deg R\le D_*,\qquad
\max|\operatorname{coeff}R|\le H_* .                    \tag{7}
\]
Indeed each initial Laurent exponent has magnitude at most
\(JQ_*\), each norm has at most \(d_*\) factors, and
the coefficient \(\ell^1\)-norm is submultiplicative.

## Application and conversion to phases

Apply (3) to \(R\) and (5). With all its parameters enlarged
monotonically to the displayed integers in (1),
\[
|R(e^\alpha)|\ge
\exp\left[-3d_*S_*^N\log H_*
-(2Nq_*S_*)^{18S_*^N}\right].
\]
The clearing monomial has modulus one, and each conjugate
factor other than the original is at most
\((2K_*)^J\). Hence
\[
|\operatorname{Disc}U_N|\ge e^{-\mathcal B_N}.           \tag{8}
\]
If \(\delta_N\) is the smallest chord distance between
distinct eigenvalues of \(U_N\), there are \(J/2\)
unordered pairs and each other chord is at most \(2\).
Therefore
\[
|\operatorname{Disc}U_N|
 \le\delta_N^2\,2^{J-2},\qquad
\delta_N\ge2^{1-J/2}e^{-\mathcal B_N/2}.
\]
Since \(2\sin(\pi\,\operatorname{dist}(\theta_i-\theta_j,
\mathbb Z))\le2\pi\operatorname{dist}(\theta_i-\theta_j,
\mathbb Z)\), (2) follows.

No factorization certificate from the separately submitted
§6 is used here. The proof depends on Roy's published
inequality in exactly the form (3) and on the **qualitative**
simple-spectrum witness already maintained as `BGS-FM-008`.
