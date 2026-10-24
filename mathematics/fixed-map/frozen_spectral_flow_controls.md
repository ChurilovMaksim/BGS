# Spectral flow and exact controls for fixed-map shortcuts

**Status, 25 September 2026.** The statements below are exact finite-dimensional
identities and a separate isospectral control family. They provide no
Heisenberg-scale estimate for the maintained frozen propagator and no BGS
limit. The only external input in the correction to the iterated-kick shortcut
is the Lindemann--Weierstrass application already pinned for `BGS-FM-010`.

## Eigenphase motion

Let $A=A^*$ and $M$ be unitary, and set $U(t)=e^{itA}M$. On any open interval
where the spectrum is simple, choose differentiable eigenvectors and
eigenangles

$$
U(t)\psi_j(t)=e^{i\theta_j(t)}\psi_j(t).
$$

Write $A_{jk}(t)=\langle\psi_j(t),A\psi_k(t)\rangle$ in the instantaneous
eigenbasis. Then

$$
\boxed{\quad \dot\theta_j=A_{jj},\qquad
\ddot\theta_j=\sum_{k\ne j}|A_{jk}|^2
   \cot\!\left(\frac{\theta_j-\theta_k}{2}\right).\quad}       \tag{1}
$$

Indeed, $\dot U=iAU$ gives the first identity. Differentiating the eigenvalue
equation and projecting onto $\psi_k$, $k\ne j$, gives

$$
\langle\psi_k,\dot\psi_j\rangle
=\frac{iA_{kj}}{1-e^{i(\theta_k-\theta_j)}}.
$$

Differentiate $A_{jj}=\langle\psi_j,A\psi_j\rangle$, choose the parallel
gauge $\langle\psi_j,\dot\psi_j\rangle=0$, and take twice the real part of
the sum over $k\ne j$; this is (1). It is a local identity on simple-spectrum
intervals. It gives no uniform bound as gaps close, and it does not provide a
global smooth labeling through degeneracies.

## Powers are ordered products of conjugated kicks

For the maintained model put $t_N=\tau N$ and
$A_{\ell,N}=M_N^\ell A_NM_N^{-\ell}$. Direct insertion of
$M_N^{-\ell}M_N^\ell=I$ gives, for every integer $m\ge1$,

$$
U_N^m=
\left(\prod_{\ell=0}^{m-1}e^{it_NA_{\ell,N}}\right)M_N^m,
$$

where the factors are ordered with increasing $\ell$ from left to right.
This is the exact iteration formula.

The tempting replacement by a single exponential,

$$
U_N^m\stackrel{?}{=}
\exp\!\left(it_N\sum_{\ell=0}^{m-1}A_{\ell,N}\right)M_N^m,
$$

is false already at $m=2$ for every odd $N\ge3$ with $7\nmid N$. To see
this, write $A=A_N$ and $A_1=M_NAM_N^{-1}$. By `BGS-FM-008`, $A$ has simple
spectrum and every entry of $M_N$ in an eigenbasis of $A$ is nonzero. If
$[A,A_1]=0$, then $A_1$ is diagonal in this eigenbasis. Since $A_1$ is
unitarily conjugate to the simple-spectrum matrix $A$, $M_N$ would have to be
monomial in that basis, contradicting the nonzero-entry statement. Hence
$[A,A_1]\ne0$.

This also rules out accidental equality at the physical value $t_N$. The
entries of

$$
F(t)=e^{itA}e^{itA_1}-e^{it(A+A_1)}
$$

are exponential polynomials with algebraic coefficients and algebraic
frequencies. If the two matrices agreed at the nonzero algebraic number
$t_N=10^{-80}N$, Lindemann--Weierstrass would force $F$ to vanish identically.
But

$$
F''(0)=-[A,A_1]\ne0,
$$

which is impossible. This use of exponential independence is qualitative;
the exact ordered product, rather than an unordered exponential, must be
retained in any long-time analysis. The exceptional dimension $N=7$ has
$A_7=(9/10)I$ and is not covered by this noncommutation argument.

## An exact isospectral control family

Let $p\equiv1\pmod4$ be prime, index the standard basis by $j\in\mathbb F_p$,
let $\chi$ be the quadratic character modulo $p$ with $\chi(0)=0$, set
$\omega=e^{2\pi i/p}$, and

$$
S e_j=e_{j+1},\qquad D e_j=\omega^j e_j,\qquad
A_{jk}=\frac{\chi(j-k)}{\sqrt p}.
$$

Then $A=A^*$, its diagonal is zero, and every off-diagonal entry has squared
modulus $1/p$. In addition $A^2=I-\mathbf1\mathbf1^*/p$: the discrete Fourier
eigenvalue at the constant vector is zero, and for each nonzero frequency $h$ it is
$\chi(h)p^{-1/2}G$, where $G=\sum_r\chi(r)\omega^r$ and $|G|^2=p$.
Since $A$ is Hermitian, these nonzero eigenvalues are $\pm1$.

Define

$$
B=\sum_{r=1}^{p-1}\frac{\chi(r)}{\sqrt p(1-\omega^r)}S^r.
$$

Because $\chi(-r)=\chi(r)$, $B=B^*$. Also
$DS^rD^*=\omega^rS^r$, so

$$
B-DBD^*=A.
$$

Both $B$ and $DBD^*$ are polynomials in $S$ and therefore commute. It follows
that for every real $t$,

$$
e^{itA}D=e^{itB}De^{-itB}.
$$

Thus the spectrum remains exactly the regular $p$-gon although the kick
generator has zero diagonal and uniform off-diagonal magnitudes. For every
$s>0$ its pair Abel statistic is

$$
L_p(s)=\frac1{p^2}\sum_{m\ge1}e^{-2sm/p}
       |\operatorname{Tr}(e^{itA}D)^m|^2
=\sum_{r\ge1}e^{-2sr}
=\frac1{e^{2s}-1}.
$$

The difference from the CUE benchmark is the strictly positive quantity
$e^{-s}(\sinh^2s-s^2)/(2s^2\sinh s)$, as in `BGS-TRACE-007`. The
construction is an exact control
example, not the prescribed BGS family. It shows that zero diagonal and
uniform kick-entry magnitudes alone cannot imply CUE statistics.
