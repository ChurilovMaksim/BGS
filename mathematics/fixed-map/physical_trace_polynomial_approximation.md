# Physical polynomial approximation and its all-order trace error

**Claim:** BGS-TRACE-107. **Status:** analytic author proof with author check,
21 October 2026. Standard approximation and finite algebra; no priority claim.
The fixed model is defined in [physical kick trace decay](physical_kick_trace_decay.md).
This note controls approximation errors and arithmetic aliases. The remaining
signed trace sum is not evaluated.

## 1. Polynomial degree at the actual coupling

The original finite Fourier polynomial has coefficient one-norm at most
$a_*=59/50$. Indeed, its $p$-independent part can be written as

$$
\frac9{10}\cos14\pi q+\frac1{10}\cos2\pi q
-\frac1{10}\cos14\pi q\cos2\pi q+\frac1{100}r(q)\sin2\pi q,
$$

whose one-norm is at most $57/50$ because $|r|_0=4$.
The remaining term contributes at most $4/100$. Consequently
$\|A_N\|\le a_*$ for every odd $N$, including aliased small moduli.

Let $H=H^*$, $\|H\|\le a_*$ and $s\ge0$.
The real-axis integral Taylor remainder gives

$$
\left\|e^{isH}-\sum_{j=0}^{n-1}\frac{(isH)^j}{j!}\right\|
 \le\frac{(a_*s)^n}{n!}.                              \tag{1}
$$

There is no exponential prefactor: the integral contains the unitary
$e^{itH}$ for real $t$. Since $n!\ge(n/e)^n$, choosing
$n\ge ea_*s+K\log N$ makes (1) at most $N^{-K}$.

A lower leading degree follows from the Chebyshev expansion. Define

$$
J_n(z)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{i(z\sin\theta-n\theta)}d\theta.
$$

Fourier orthogonality gives $\sum_{n\in\mathbb Z}|J_n(z)|^2=1$ and
$J_{-n}=(-1)^nJ_n$. Shift the contour downward by $i\log2$ to obtain
$|J_n(z)|\le2^{-n}e^{3z/4}$ for $n\ge0$. Thus
$|J_n(z)|\le e^{-n/4}$ if $n\ge2z$, using $\log2>5/8$.
Absolute Fourier convergence, a shift by $\pi/2$, and pairing opposite
frequencies prove

$$
e^{izu}=J_0(z)+2\sum_{n\ge1}i^nJ_n(z)T_n(u),\qquad |u|\le1.
$$

Here $T_n(\cos\theta)=\cos n\theta$ and
$\|T_n(H/a_*)\|\le1$. Put $C_0=2/(1-e^{-1/4})$ and

$$
L_N=\left\lceil 2a_*\tau N+4K\log N+4\log C_0\right\rceil,
\quad z=a_*\tau N,\quad \tau=10^{-80},
$$

$$
Q_N=J_0(z)I+2\sum_{n=1}^{L_N}i^nJ_n(z)T_n(A_N/a_*).
$$

Then

$$
\|E_N(\tau)-Q_N\|\le C_0e^{-(L_N+1)/4}\le N^{-K}.    \tag{2}
$$

The coefficient budget is at most $\sqrt{4z+3}+C_0$: apply
Cauchy--Schwarz to $|n|\le\lceil2z\rceil$ and the exponential bound
to the remainder. This budget does not estimate a coherent trace sum.

## 2. All fixed factorial orders, not only the pair test

Write $U=E_N(\tau)M_N$ and $V=Q_NM_N$. More generally suppose
$\|U-V\|\le\varepsilon$, $U$ is unitary and $\|V\|\le1+\varepsilon$.
For integer $n$ define

$$
p_n(U)=\operatorname{Tr}U^n,\quad p_0=N,
\qquad \widetilde p_n(V)=
\begin{cases}\operatorname{Tr}V^n,&n>0,\\
N,&n=0,\\
\operatorname{Tr}(V^*)^{-n},&n<0.
\end{cases}
$$

The negative-index expression uses adjoint powers, not inverse powers.
No inverse or unitarity of $V$ is assumed. Telescoping gives

$$
|p_n(U)-\widetilde p_n(V)|
 \le N|n|\varepsilon(1+\varepsilon)^{|n|-1}.           \tag{3}
$$

For fixed $k\ge2$ and fixed Schwartz $b$ with smooth Fourier support
in $[-B,B]$, define the trace-polynomial statistic

$$
\mathcal M_{k,N}(p;b)=\frac1{k!N^k}
\sum_{\substack{m\in\mathbb Z^k\\\sum m_a=0}}
\left(\prod_a\widehat b(m_a/N)\right)
\sum_{\pi\in\mathcal P_k}
\left(\prod_{D\in\pi}(-1)^{|D|-1}(|D|-1)!\right)
\prod_{D\in\pi}p_{\sum_{a\in D}m_a}.                 \tag{4}
$$

For the unitary $U$, this is its phase-averaged factorial statistic.
For $V$, (4) is only a trace polynomial; it is not asserted to be a
point-process moment or to satisfy positivity.

**Theorem.** For $N\varepsilon\le1$,

$$
|\mathcal M_{k,N}(p(U);b)-\mathcal M_{k,N}(\widetilde p(V);b)|
 \le C_{k,b,B}N^k\varepsilon.                        \tag{5}
$$

Proof. There are at most $(2BN+1)^{k-1}$ contributing frequency tuples.
Every block frequency has modulus at most $kBN$. By (3), each nonzero
trace difference is bounded by $C_{k,B}N^2\varepsilon$; each unchanged
factor is bounded by $C_{k,B}N$. A partition with $\ell$ blocks therefore
contributes at most $C_{k,B}N^{\ell+1}\varepsilon$ after telescoping
the product. Multiplying by the number of tuples and $N^{-k}$ gives
$C_{k,b,B}N^\ell\varepsilon\le C_{k,b,B}N^k\varepsilon$.
The number of partitions and their Möbius coefficients depend only on
$k$. Zero block frequencies cause no error. This proves (5).

With (2), every fixed order is approximated with error $O(N^{k-K})$;
choose $K>k$. A single sequence works for all fixed orders by taking
$K=\log N$: its error is $\exp[-(\log N)^2]$ and its degree is
$2a_*\tau N+O((\log N)^2)$. This assertion follows from the same explicit
bound; it does not require a uniform-in-$k$ estimate.

At $k=2$, subtracting the unchanged CUE reference gives the imported
pair-functional error $O(N^{2-K})$. Equations (3)--(5) extend that error
control to the complete fixed-order hierarchy. The limiting value of
the remaining trace polynomial is still unknown.

## 3. Exact two-copy alias threshold on Pell dimensions

Here use the modular Weyl labels $W_N(k,l)=T_N(l,k)$, without the
ordinary-half correction. Direct substitution in $M_N$ gives

$$
M_NW_N(v)M_N^*=W_N(Cv),\qquad
C=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$

For odd $r\ge3$, write $(1+\sqrt2)^r=x+y\sqrt2$ and set $N=xy$,
$c=x^2+2y^2$. Then $x,y$ are coprime odd integers,
$x^2-2y^2=-1$, $y<x<2y$, and

$$
C^r=\begin{pmatrix}c&2N\\4N&c\end{pmatrix},\quad
c\equiv1\pmod x,\quad c\equiv-1\pmod y.
$$

Consequently, for integer scalar labels,

$$
V+cW\equiv0\pmod N
\iff V+W=xp,\quad V-W=yq,
\quad p,q\in\mathbb Z,\quad p\equiv q\pmod2.          \tag{6}
$$

Moreover $|V|+|W|=\max(x|p|,y|q|)$. Odd $p,q$ give minimum $x$;
even nonzero pairs give minimum at least $2y>x$. The shortest nonzero
alias therefore has length exactly $x\asymp\sqrt N$, realized by
$V=(x+y)/2$, $W=(x-y)/2$. In fact $V+cW=N(2y-x)$.
For $v=(1,0)$ and $R=M_N^r$,

$$
W_N(v)^V(RW_N(v)R^*)^W=I.                            \tag{7}
$$

All symplectic phases in this identity vanish. A rule keeping only
separately zero totals in the two copies misses (7). Thus a fixed-word
limit with that rule cannot be extended uniformly to these growing
lengths. This is an obstruction to that approximation, not a spectral
counterexample for $U_N$.

## 4. Why the controlled degrees cannot carry the full exponential

For $z>0$ and $0\le n\le z/2$, the defining integral gives
$|J_n(z)|\le4z^{-1/2}$. For $z\le16$ use $|J_n|\le1$.
Otherwise put $\nu=n/z$, $\delta=z^{-1/2}$ and remove
$|\cos\theta-\nu|\le\delta$. This set has length at most
$16\delta/\sqrt7$. The complement consists of at most four intervals
where the derivative of $\sin\theta-\nu\theta$ is monotone, of one
sign and at least $\delta$ in modulus. Integration by parts bounds
each integral by $3/(z\delta)$. Division by $2\pi$ proves the claim.

Writing $\beta_0=J_0$, $\beta_n=2i^nJ_n$ for $n>0$, it follows that

$$
\sum_{n=0}^L|\beta_n(z)|^2\le64(L+1)/z\quad(L\le z/2),
\qquad \sum_{n\ge0}|\beta_n(z)|^2=2-|J_0(z)|^2.
$$

For fixed $D$, the degrees $n\le D\sqrt N$ therefore carry vanishing
coefficient square mass at $z=a_*\tau N$, whereas the total mass tends
to two. These are coefficient statements. The matrices $T_n(A_N/a_*)$
are not asserted orthogonal, and no operator-norm lower bound is inferred.

## 5. Review boundary

The Taylor/Bessel estimates, pair error and CRT threshold were derived
in the imported Round 12 notes and checked directly here. The extension
(5) is an additional argument from this review. The source history and
actual finite execution scope are in the [audit](../../record/spectral_research/spectral_master_audit.md).
The BGS and signed Heisenberg-scale claims remain open.
