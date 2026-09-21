# Exact antiunitary no-go for one-position-shear fallbacks

Date: 21 September 2026.

Status: exact finite-dimensional theorem recovered from the 15 September
direct-attack audit. It explains why the old one-shear Bessel laboratory
cannot be turned into a CUE example merely by changing the classical cat.
It is a negative design theorem, not a BGS theorem.

Let \(N\) be odd and

\[
S=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL(2,\mathbb Z)
\]

with \(b\) invertible modulo \(N\). In the standard position chart a
metaplectic quantization has quadratic kernel

\[
(U_{S,N})_{x,y}=\gamma_NN^{-1/2}
 e_N(\alpha x^2+\beta xy+\gamma y^2),
\]

where \(\beta\) is invertible. Thus

\[
U_{S,N}=D_LF_\beta D_R,\qquad
(F_\beta)_{x,y}=N^{-1/2}e_N(\beta xy),
\]

with diagonal unitaries \(D_L,D_R\) and a symmetric Fourier matrix
\(F_\beta^T=F_\beta\).

Let \(D\) be an arbitrary diagonal unitary -- in particular any nonlinear
\(q\)-only kick -- and put \(U=DU_{S,N}=D_1F_\beta D_2\). Choose a diagonal
unitary \(A\) satisfying entrywise \(A^2=D_2D_1^{-1}\). Then

\[
AUA^{-1}=LF_\beta L,\qquad L=AD_1=D_2A^{-1},
\]

which is symmetric and unitary. Complex conjugation \(C\) therefore reverses
it. Conjugating back gives

\[
\Theta=A^{-1}CA,\qquad
\boxed{\Theta U\Theta^{-1}=U^{-1}.} \tag{1}
\]

For the project cat

\[
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},
\]

\(b=4\) is invertible for every odd \(N\). Hence **every \(q\)-only kick**
in this flat metaplectic chart has the exact antiunitary (1) at every odd
dimension. Classical irreversibility does not remove it.

This is why the final frozen model must keep genuinely two-directional
Fourier content. The theorem does not say that every two-directional kick
is CUE; it only closes the one-shear fallback as a route to the unitary
Dyson class.
