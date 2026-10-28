# Uniform two-state discrimination through pure loss

**Status.** Internal analytic proof, independently stress-tested by Python and C++ scalar verifiers. This is a theorem about one explicit binary discrimination problem. It is not a minimax theorem for full tomography and not a BGS statement.

Let
\[
 |\psi_n^\pm\rangle=\sqrt{1-u}|0\rangle\pm\sqrt u|n\rangle,
 \qquad n\ge1,\qquad 0<u\le1/16,
\]
and let a one-mode pure-loss channel of transmissivity \(0<\eta\le1\) produce outputs \(\sigma_\pm\). For \(B\ge1\) copies set \(t=Bu\eta^n\).

## Theorem

\[
\left|D(\sigma_+^{\otimes B},\sigma_-^{\otimes B})-
\sqrt{1-e^{-4t}}\right|
\le 5ut+\sqrt{u(43t+8\sqrt t)}.
\]

### Proof

All loss events except the zero- and \(n\)-photon components are diagonal and identical under the two hypotheses. On \(\operatorname{span}\{|0\rangle,|n\rangle\}\), the two subnormalized blocks are
\[
 M_\pm=\begin{pmatrix}a&\pm c\\ \pm c&b\end{pmatrix},
\]
where
\[
 a=1-u+u(1-\eta)^n,\qquad b=u\eta^n,\qquad
 c^2=u(1-u)\eta^n.
\]
Put \(q=u\eta^n\), \(s=a+b\),
\[
 r=\sqrt{(a-b)^2+4c^2},\qquad d=ab-c^2.
\]
Then
\[
 d=u^2[\eta(1-\eta)]^n,
 \qquad 1-u\le s\le1,
 \qquad r^2\ge(1-2u)^2.
\]
The last inequality follows because \(a-b=1-u+u(1-\eta)^n-q\ge1-2u\).

Let \(\ell=(s-r)/2\) be the smaller eigenvalue of either block and replace each block by \(s\) times its top normalized eigenvector, leaving the common orthogonal remainder unchanged. The trace distance between one original state and its replacement is exactly \(\ell\). Therefore tensor-product telescoping and the triangle inequality change the binary trace distance by at most \(2B\ell\). Since
\[
 \ell=\frac{2d}{s+r}\le\frac{2d}{s},
\]
we get
\[
 2B\ell\le \frac{4Bu^2\eta^n}{1-u}<5ut.
\]

The squared overlap of the two top eigenvectors is
\[
 \gamma=\frac{(a-b)^2}{r^2}.
\]
In the replacement model, the number \(M\) of tensor factors landing in the two-dimensional block is binomial, \(M\sim\operatorname{Bin}(B,s)\), and orthogonality of the block labels gives the exact identity
\[
 D_{\rm repl}=\mathbb E\sqrt{1-\gamma^M}.
\]
Set \(\delta=1-\gamma\) and \(L=-\log\gamma\). Write
\[
 z=(1-\eta)^n,\qquad e=\eta^n,
 \qquad h=1-z-e\in[0,1].
\]
Then
\[
 r^2=1-2uh+u^2(1-z+e)^2-4u^2e.
\]
Using \(u\le1/16\), \(0\le h\le1\), and \(0\le1-z+e\le2\), one obtains
\[
 \delta=\frac{4q(1-u)}{r^2},\qquad
 \delta\le5q,
 \qquad |\delta-4q|\le16uq.
\]
Since \(\delta\le5/16\),
\[
 0\le -\log(1-\delta)-\delta
 \le\frac{\delta^2}{2(1-\delta)},
\]
whence
\[
 |L-4q|\le35uq,
 \qquad L\le8q.
\]
Also \(1-s=uh\le u\). Thus
\[
 |BsL-4t|\le39ut\le43ut.
\]
For the binomial fluctuation,
\[
 \mathbb E|ML-BsL|
 \le L\sqrt{Bs(1-s)}\le8u\sqrt t.
\]
Finally, for \(x,y\ge0\),
\[
 |\sqrt{1-e^{-x}}-\sqrt{1-e^{-y}}|\le\sqrt{|x-y|}.
\]
Apply this with \(x=ML\), \(y=4t\), then Jensen's inequality. Combining the replacement error proves the displayed bound.

## Corollaries

If \(u_j\to0\) while \(B_j u_j\eta_j^{n_j}\to c\in[0,\infty)\), then the Helstrom success probability satisfies
\[
 P_{\rm succ}^{\rm opt}\to\frac{1+\sqrt{1-e^{-4c}}}{2}.
\]
For any fixed target success probability \(p\in(1/2,1)\), the least copy count obeys
\[
 B_p\sim\frac{-\log(4p(1-p))}{4u\eta^n}.
\]
Consequently \(B_p(\eta)/B_p(1)\sim\eta^{-n}\). In particular, if \(\eta_n\to1\):

- \(n(1-\eta_n)\to0\) leaves the leading copy complexity unchanged;
- \(n(1-\eta_n)\to\gamma\in(0,\infty)\) multiplies it by \(e^\gamma\);
- \(n(1-\eta_n)\to\infty\) gives a diverging loss penalty.

For the moment-constrained pair \(u=E/n^\beta\),
\[
 B_p\sim\frac{-\log(4p(1-p))}{4E}\,n^\beta\eta_n^{-n}.
\]

## Non-claims

The theorem gives an exact joint small-signal/loss transition for this known pair. It does not by itself determine the minimax risk of full continuous-variable tomography, because the latter also contains a growing set of unknown matrix entries. It makes no claim about microscopic spectral universality, BGS, GOE, or COE.
