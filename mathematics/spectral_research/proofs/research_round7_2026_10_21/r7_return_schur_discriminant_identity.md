> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/r7_return_schur_discriminant_identity.md`. Embedded SHA256: `fc36418d779397802e481ad4383ee40460e19d27916f5b21b5da0f9ced9b9a33`.
> [Thematic guide](../../topics/dephasing.md).

# The complementary determinant equals a squared tomography determinant

21 October 2026. The identities in Sections 1--3 hold for every finite
unitary matrix. Their application in Section 4 concerns the exact original
family and retains the arithmetic scope of the established intensity
invertibility theorem.

## 1. An unconditional finite-dimensional identity

Let $U\in U(N)$. On the Hilbert space of $N\times N$ matrices with
the Hilbert--Schmidt inner product, put
$$
 WX=UXU^*,\qquad
 \Pi X=\operatorname{diag}(X_{00},\ldots,X_{N-1,N-1}),\qquad O=I-\Pi,
 \quad S=OWO\big|_{\operatorname{ran}O}.
 \tag{1.1}
$$
Define the $N\times N$ matrix of diagonal observations
$$
 D(U)_{n,x}=(U^n)_{xx},\qquad0\le n,x<N.
 \tag{1.2}
$$
Then
$$
 \boxed{\det(I_{\operatorname{ran}O}-S)=|\det D(U)|^2.}
 \tag{1.3}
$$
In particular the determinant on the left is a nonnegative real
number, even though $S$ need not be self-adjoint or normal.

Choose an orthonormal eigenbasis of $U$, with eigenvalues
$\lambda_1,\ldots,\lambda_N$, repeated with multiplicities, and
write the intensity matrix as
$$
 \mathcal B_{xj}=|\psi_j(x)|^2.
$$
An equivalent identity is
$$
 \det(I-S)=|\det\mathcal B|^2
             \prod_{1\le j<k\le N}|\lambda_j-\lambda_k|^2.
 \tag{1.4}
$$
When eigenvalues repeat, both sides of (1.4) are zero. No particular
choice of basis inside a degenerate eigenspace is required.

## 2. Proof, including all degenerate cases

First suppose that $U$ has simple spectrum and $\mathcal B$ is
invertible. In the orthogonal splitting into coordinate diagonal and
off-diagonal matrices, write
$$
 W=\begin{pmatrix}P&B\\ C&S\end{pmatrix},\qquad
 \mathfrak F(z)=zP+z^2B(I-zS)^{-1}C.
 \tag{2.1}
$$
There is no eigenvector of $S$ with eigenvalue one. Such a vector,
if present, would extend by zero on the diagonal to a stationary
vector of $W$, by equality in the norm contraction of the
compression. Simple spectrum makes every stationary matrix a
linear combination of the eigenprojectors, whose diagonal map
is $\mathcal B$. Its invertibility excludes that vector.

Set $R=(I-S)^{-1}$. Unique stationary extension from the diagonal
space is the map
$$
 X=\begin{pmatrix}I\\RC\end{pmatrix}.
$$
Consequently $WX=X=W^*X$, so
$$
 P+BRC=I,\qquad B=C^*R^*(I-S).
 \tag{2.2}
$$
If $\mathcal J$ is the isometry whose columns are the eigenprojectors,
then $X=\mathcal J\mathcal B^{-1}$. Differentiating (2.1), using
$R+RSR=R^2$, gives
$$
 \mathfrak F(1)=I,\qquad
 \mathfrak F'(1)=I+BR^2C=X^*X=(\mathcal B\mathcal B^*)^{-1}.
 \tag{2.3}
$$
These steps are also proved in full in Section 7 of
[the stationary-dephasing note](r7_return_uniform_stationary_dephasing.md),
SHA256
c2bf50a33a642b984afa7bfa83fdc0d28b8019c79d4f47121ab52adee5e53075.

Block Gaussian elimination of $I-zW$ gives the exact rational identity
$$
 \det(I-zW)=\det(I-zS)\det(I-\mathfrak F(z)).
 \tag{2.4}
$$
It holds wherever $I-zS$ is invertible, including a neighborhood of
one in the present case. The spectrum of $W$ consists of the
ratios $\lambda_j/\lambda_k$. Thus
$$
 \lim_{z\to1}\frac{\det(I-zW)}{(1-z)^N}
 =\prod_{j\ne k}(1-\lambda_j/\lambda_k)
 =\prod_{j<k}|\lambda_j-\lambda_k|^2.
 \tag{2.5}
$$
On the other hand, (2.3) implies
$$
 I-\mathfrak F(z)=(1-z)\mathfrak F'(1)+O((1-z)^2),
 \quad
 \lim_{z\to1}\frac{\det(I-\mathfrak F(z))}{(1-z)^N}
 =|\det\mathcal B|^{-2}.
 \tag{2.6}
$$
Equations (2.4)--(2.6) prove (1.4) in this case.

If the spectrum is simple but $\mathcal B$ is singular, a nonzero
coefficient vector in its kernel gives a nonzero stationary matrix
with zero coordinate diagonal. Therefore $1\in\operatorname{spec}S$,
and both sides of (1.4) vanish.

If the eigenvalue multiplicities are $m_1,\ldots,m_t$, with at least
one multiplicity larger than one, then
$$
 \dim\ker(W-I)=\sum_{\ell=1}^t m_\ell^2>N.
$$
Its diagonal map has target dimension $N$, so again it has a
nonzero kernel and $1\in\operatorname{spec}S$. The product on the
right of (1.4) vanishes because of the repeated eigenvalue. This
settles all remaining cases without a continuity or genericity
argument.

Finally let $V_{n,j}=\lambda_j^n$, for $0\le n<N$. Direct spectral
expansion gives
$$
 D(U)=V\mathcal B^T.
$$
The Vandermonde formula, or alternation followed by comparison of
the top monomial, gives
$$
 |\det D(U)|^2
 =|\det\mathcal B|^2\prod_{j<k}|\lambda_j-\lambda_k|^2.
$$
Together with (1.4) this proves (1.3) for every unitary $U$.

## 3. Exact signed trace cycles at every time

For all unitary $U$, (2.4) holds as a formal power series identity
at zero. Put
$$
 F_1=P,\qquad F_r=BS^{r-2}C\quad(r\ge2),
 \qquad\mathfrak F(z)=\sum_{r\ge1}F_rz^r.
$$
The formal logarithm of (2.4), with constant term zero, yields
$$
 \boxed{
 |\operatorname{Tr}U^n|^2
 =\operatorname{Tr}S^n
   +n\sum_{\ell=1}^n\frac1\ell
      \sum_{\substack{r_1,\ldots,r_\ell\ge1\\
                      r_1+\cdots+r_\ell=n}}
           \operatorname{Tr}(F_{r_1}\cdots F_{r_\ell}) .
 }
 \tag{3.1}
$$
Indeed
$$
 -\log\det(I-zW)=\sum_{n\ge1}\frac{z^n}{n}\operatorname{Tr}W^n,
 \qquad
 -\log\det(I-\mathfrak F(z))
 =\sum_{\ell\ge1}\frac1\ell\operatorname{Tr}(\mathfrak F(z)^\ell).
$$
For each coefficient there are only finitely many terms, so no
convergence at the unit circle is being assumed. The identities
follow either by diagonalization for the first logarithm and
formal differentiation for the second, or from
$d\log\det A=\operatorname{Tr}(A^{-1}dA)$ and matching constant
terms. Finally $\operatorname{Tr}W^n=|\operatorname{Tr}U^n|^2$
because $W$ has the ratio eigenvalues.

Formula (3.1) retains every sign and every complex phase in the
matrix products. Replacing them by products of norms is a different
quantity. The endpoint identities for $\mathfrak F(1)$ and
$\mathfrak F'(1)$ do not bound its coefficients of order $N$,
nor the cycle sum (3.1) on that scale.

## 4. Consequences and limits for the original family

For every original odd $N$, identity (1.3) applies at the exact
prescribed phase. For $7\nmid N$, the established simple-spectrum
and invertible-intensity theorem makes its two sides strictly
positive. For $7\mid N$, the identity remains valid, but strict
positivity has not been proved by this argument.

The new stationary-dephasing theorem gives, for every choice of
eigenbasis along all odd $N$,
$$
 0\le\mathcal B_N\mathcal B_N^*-J_N\le q_N I,\qquad q_N\to0.
$$
Since the constant singular value of $\mathcal B_N$ is one,
$$
 |\det\mathcal B_N|^2\le q_N^{N-1}.
 \tag{4.1}
$$
Hadamard's inequality applied to $V_{n,j}=\lambda_j^n$, whose rows
have Euclidean norm $\sqrt N$, gives
$\prod_{j<k}|\lambda_j-\lambda_k|^2\le N^N$.
Consequently
$$
 0\le\frac{\det(I-S_N)}{N^N}
     =\frac{|\det D(U_N)|^2}{N^N}
 \le q_N^{N-1}.
 \tag{4.2}
$$
For each fixed $A>0$, (4.2) is at most $e^{-AN}$ for all
sufficiently large odd $N$: choose $q_N\le e^{-2A}$ and use
$2(N-1)\ge N$. No rate for that threshold is obtained.

This upper estimate gives no lower bound on the Vandermonde product
or on individual eigenvalue gaps. The exact identity
$$
 \prod_{j<k}|\lambda_j-\lambda_k|^2
       =\frac{\det(I-S_N)}{|\det\mathcal B_N|^2}
 \quad(7\nmid N)
$$
contains two potentially very small quantities. Their ratio is
uncontrolled. Likewise, no estimate of the weighted sum of (3.1)
at $n\asymp N$ follows. The original $H_{\rm diag}$ remains
unproved and undisproved.
