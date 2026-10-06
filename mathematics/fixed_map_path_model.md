# Fixed model and normalization

Pinned base: `0ffb20cc152d0ddd2620887e46d21d1120b95fd8`.
All limits below are through odd positive integers N at the fixed coupling
\(\tau=10^{-80}\). Put \(e(z)=e^{2\pi iz}\), \(e_N(j)=e(j/N)\),
\(h=N^{-1}\), and let inverse integers in subscripts denote inverses modulo N.

\[
(T_N(a,b)u)_j=e_N(b(j+2^{-1}a))u_{j+a},\quad
W_N(a,b)=(-1)^{ab}T_N(a,b),\quad
(M_N)_{jk}=N^{-1/2}e_N(-8^{-1}(3j^2-2jk+3k^2)).
\]

Define
\[
r(q)=(1-\cos14\pi q)(1+\cos2\pi q),\qquad
\cos\alpha=-3/5,\quad\sin\alpha=4/5,
\]
\[
g(q,p)=\cos14\pi q+r(q)/10+r(q)\sin2\pi q/100
+r(q+1/2)\cos(2\pi p-\alpha)/100-1/10.
\]
For the Fourier expansion \(g=\sum c_{kl}e(kq+lp)\), put
\(A_N=\sum c_{kl}W_N(l,k)\), \(E_N(t)=e^{itNA_N}\),
\(U_N=E_N(\tau)M_N\). This is exactly the raw-symbol quantization in
FM-001, with the forced ordinary half-shift; it is not a new quantization.
It is Hermitian/unitary as appropriate, including composite odd N.
The matrix action on lattice-periodic samples is exactly
\[
(A_Nu)(x)=\sum c_{kl} e(k(x+hl/2))u(x+hl),\qquad l\in\{-1,0,1\}.
\]
Indeed \((-1)^{kl}e_N(k(j+2^{-1}l))=e(k(j/N+hl/2))\).

Classical convention: \(X_g=(g_p,-g_q)\),
\(\Phi=\Phi_g^{\tau/(2\pi)}\),
\(S=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)\),
\(G=S\circ\Phi\). Conjugation \(U_N(\cdot)U_N^*\) pulls smooth
symbols back by G; the opposite conjugation uses the inverse map.
Use ordinary matrix traces, normalized Hilbert–Schmidt norm
\((N^{-1}\operatorname{Tr}(X^*X))^{1/2}\), and normalized coordinate l2.

The Fourier bound \(\sum(|\Re c|+|\Im c|)| (k,l)|^2=51451/1000<52\)
and support \(|(k,l)|<10\) imply
\(\|X_g\|\le400\), \(\|DX_g\|\le3000\),
\(\|D^2X_g\|\le200000\). These are Euclidean induced norms.
For coarse maximum-norm WKB estimates, every coordinate derivative of g
through order four is below \(10^9\), and every multilinear derivative
through order three of \((-g_p,g_q)/(2\pi)\) is below \(10^{12}\).

These results give two specified families within the exact coordinate trace
expansion. Neither family exhausts the ordered pairs of paths. General
noncyclic interference, signed factorial comparison, and deterministic BGS
remain open. No shrinking-coupling limit, probabilistic model, or averaging
in N or tau is substituted.
