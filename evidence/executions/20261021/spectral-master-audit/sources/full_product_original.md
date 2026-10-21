# Round 12: physical exponential tails, Pell aliases, and the unestimated signed sum

Date: 21 October 2026. Branch: `r12_full_product`.

## 0. Result and exact scope

This investigation does **not** prove or refute $H_{\rm diag}$. It obtains
no new estimate for the original Heisenberg-time trace sum. In particular,
it does not improve the old physical short-Pell trace estimate quoted in
Section 9 of `fermionic_quantitative_pressure.md`.

The attempted extension of the Round 11 two-copy limit was executed as
follows. The exponential at its actual argument $s=N\tau$,

\[
E_N=\exp(iN\tau A_N),\qquad \tau=10^{-80},
\]

has an operator-norm polynomial approximation with arbitrarily small
power-law error, with degree proportional to $N\tau$. This follows either
from the real-axis Taylor remainder or from an explicitly proved
Chebyshev--Bessel expansion. The latter has coefficient \(\ell^1\) mass
\(O(\sqrt{1+N\tau})\), in place of the exponential coefficient bound obtained
by taking moduli in the ordinary power series.

However, the first nontrivial exact two-copy alias occurs at word length
\(\asymp\sqrt N\), and the Chebyshev coefficients in that controlled degree
range carry vanishing \(\ell^2\) mass at $s=N\tau$. The attempted
resummation supplies no cancellation estimate for the remaining coefficients.
Section 6 states the resulting full finite signed sum, including all
aliases, and the still unproved original pair estimate.

Thus the **scalar exponential tail is rigorously controlled** below. The
**remainder after retaining only a fixed number of Magnus coefficients is
not controlled at the physical argument**. These are different assertions.
There is no claimed new universality theorem, no replacement of the fixed
\(\tau\), and no average over parameters or dimensions.

## 1. Inputs actually inspected

The frozen master was used only as the parent's declared base, not read in
its entirety in this branch. Its declared SHA-256 is
`b8b2741c3b15304e82cef77e0db517a6b9db23ffb22f7e49658b22ee5f900185`.

| Input | Actual read scope | SHA-256 |
|---|---|---|
| `research_round12_2026_10_21/round12_target_checkpoint.md` | complete | `b39996f6cc4c86aebbf03b5a0775bf08b1ad250821b1b0bedd6c0c68767a0ec9` |
| `research_round11_2026_10_21/r11_arithmetic_pell_magnus.md` | complete | `83fef65536de1e5528ad8e4d5eebf39a2b42d7da4217274a32c1e4e6dc7707d5` |
| `research_round8_2026_10_21/r8_weyl_quantitative_band_escape.md` | complete | `9982f37ec0faa8e6628dcb8d80b18fdb1005f2c2af119727526634a5c941f54a` |
| `research_round8_2026_10_21/r8_weyl_explicit_linear_degree_corollary.md` | complete | `227bf6ab1905006f57f54b30372419acb7f5db08c1a4b22f022f56f1d6097e52` |
| `research_round3_2026_10_21/arithmetic_flat_packet_obstruction_test.md` | complete | `58bcfa0d7db85583d23f16c8ab1e5327926e11221b102cb7c6d0128037abb1cc` |
| `research_round2_2026_10_20/fermionic_quantitative_pressure.md` | Sections 8--9 only, lines 725--806 | `d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2` |

Search hits and introductory excerpts from other old files were inspected
to avoid duplication. Their uninspected proofs are not mathematical inputs
to the propositions below. In particular, the old pressure theorem is
mentioned to delimit novelty; it is not used to prove the estimates below.
No external Bessel or stationary-phase theorem is used without proof.

## 2. Conventions and the exact product

Write

\[
W_N(k,l)=T_N(l,k),\qquad
\sigma((k,l),(k',l'))=lk'-kl',\qquad
C=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
\]

Direct multiplication of the given Weyl operators gives

\[
W_vW_w=e_N(\overline2\sigma(v,w))W_{v+w},\qquad
\operatorname{tr}_N W_v=\mathbf1_{v=0\pmod N},
\tag{2.1}
\]

where \(\operatorname{tr}_N=N^{-1}\operatorname{Tr}\) and
\(\overline2\) is the modular inverse, exactly as in the question.
Substitution in the prescribed quadratic kernel gives

\[
M_NW_vM_N^*=W_{Cv}.
\tag{2.2}
\]

For example, in the original $(a,b)$ ordering, comparison of the
coefficients of $x,y$ in $M_NT_N(a,b)$ and $T_N(a',b')M_N$ gives

\[
a'=3a+4b,\qquad b'=2a+3b.
\]

The constant terms agree because

\[
\frac12a'b'-\frac38(a')^2=-\frac38a^2-\frac12ab,
\]

as a rational identity, hence also modulo odd $N$. This verifies (2.2)
with the correct order of the labels.

The Fourier norm of the original $f-1/10$ is at most

\[
a:=\frac{59}{50},\qquad \|A_N\|\le a.
\tag{2.3}
\]

Indeed its $l=0$ part is

\[
\frac9{10}\cos(14\pi q)+\frac1{10}\cos(2\pi q)
-\frac1{10}\cos(14\pi q)\cos(2\pi q)
+\frac1{100}r(q)\sin(2\pi q).
\]

The Fourier \(\ell^1\) norm of $r$ is at most (4), giving at most
\(9/10+1/10+1/10+4/100=57/50\) for this part. The remaining $p$ part
has norm at most $4/100$. Unitarity of each $W_v$ proves (2.3).

Set

\[
X_{j,N}=M_N^jA_NM_N^{-j},\qquad s=N\tau.
\]

For every positive integer $m$, without approximation,

\[
U_N^m=\left(\prod_{j=0}^{m-1}e^{isX_{j,N}}\right)M_N^m.
\tag{2.4}
\]

The product is ordered from smaller to larger $j$, left to right.

For odd $r\ge3$, write

\[
(1+\sqrt2)^r=x+y\sqrt2,\quad N=xy,\quad c=x^2+2y^2.
\tag{2.5}
\]

Then $x,y$ are coprime odd positive integers, $x^2-2y^2=-1$, and

\[
C^r=\begin{pmatrix}c&2N\\4N&c\end{pmatrix},\qquad
c\equiv1\pmod x,\quad c\equiv-1\pmod y,\quad c^2\equiv1\pmod N.
\tag{2.6}
\]

For the matrix representation
$D(a+b\sqrt2)=\left(\begin{smallmatrix}a&b\\2b&a\end{smallmatrix}\right)$,
one has $C=D((1+\sqrt2)^2)$ and
$(x+y\sqrt2)^2=c+2N\sqrt2$, proving the displayed formula for $C^r$.
The expanding eigenvalue of $C$ is
\(\lambda=(1+\sqrt2)^2\). Since $C^{2r}\equiv I\pmod N$, (2.2)
implies that $M_N^{2r}$ commutes with all Weyl operators. A matrix
commuting with the diagonal modulation is diagonal, and commuting also
with the one-site shift forces that diagonal to be constant. Thus

\[
M_N^{2r}=\gamma_N I,\quad |\gamma_N|=1,\qquad
U_N^{2r}=\gamma_N\prod_{j=0}^{2r-1}e^{isX_{j,N}}.
\tag{2.7}
\]

Also $N=(\lambda^r-\lambda^{-r})/(4\sqrt2)$, so
$r=(\log N)/\log\lambda+O(1)$.

## 3. The actual exponential has a controlled linear-degree tail

### 3.1. Real-axis Taylor estimate

Let $H=H^*$, \(\|H\|\le a\), $s\ge0$. The integral Taylor formula
applied on the real interval $[0,s]$ gives, for $n\ge1$,

\[
e^{isH}-\sum_{j=0}^{n-1}\frac{(isH)^j}{j!}
=\frac{i^n}{(n-1)!}\int_0^s(s-t)^{n-1}H^ne^{itH}\,dt.
\]

Because $e^{itH}$ is unitary on this interval,

\[
\left\|e^{isH}-\sum_{j=0}^{n-1}\frac{(isH)^j}{j!}\right\|
\le\frac{(as)^n}{n!}.
\tag{3.1}
\]

There is no factor $e^{as}$ in this bound. The elementary inequality
\(n!\ge(n/e)^n\) follows by comparing
\(\sum_{j=1}^n\log j\) with \(\int_1^n\log t\,dt\).
For $n\ge eas+K\log N$, put $t=(n-eas)/n\in[0,1)$. Then

\[
\frac{(as)^n}{n!}\le(eas/n)^n=(1-t)^n
\le e^{-nt}\le N^{-K}.
\tag{3.2}
\]

The case $s=0$ is exact. A rationally specified sufficient choice is

\[
n=\left\lceil3a\tau N\right\rceil
  +K\left\lceil\log_2N\right\rceil,
\tag{3.3}
\]

for positive integer $K$, since $e<3$ and \(\log_2N\ge\log N\).
This is a standard approximation result. Its significance here is only
that the physical argument causes no uncontrolled scalar Taylor tail
once one retains linearly many terms.

### 3.2. Chebyshev--Bessel expansion and its coefficient budget

Define, for integers $n$,

\[
J_n(z)=\frac1{2\pi}\int_{-\pi}^{\pi}
 e^{i(z\sin\theta-n\theta)}\,d\theta,\qquad z\ge0.
\tag{3.4}
\]

These are the Fourier coefficients of $e^{iz\sin\theta}$.
Conjugating the integral and replacing $\theta$ by $-\theta$ proves
\(J_n(z)\in\mathbb R\). Shifting $\theta$ by $\pi$ in $J_{-n}(z)$
then gives $J_{-n}(z)=(-1)^nJ_n(z)$. Fourier orthogonality gives

\[
\sum_{n\in\mathbb Z}|J_n(z)|^2=1.
\tag{3.5}
\]

Specifically, (3.6) below ensures absolute convergence of the Fourier
series. Multiplying that series by its conjugate and integrating term
by term proves (3.5), since $|e^{iz\sin\theta}|=1$.

For $n\ge0$, shift the integration contour in (3.4) down by

\(i\log2\). The vertical sides cancel by periodicity and the integrand is
entire. Since \(\sinh(\log2)=3/4\),

\[
|J_n(z)|\le 2^{-n}e^{3z/4}.
\tag{3.6}
\]

In particular, for $n\ge2z$,

\[
|J_n(z)|\le e^{-n/4},
\tag{3.7}
\]

because \(\log2>5/8\). The latter inequality follows, for instance, from
\(\log2=2\sum_{j\ge0}((2j+1)3^{2j+1})^{-1}>2/3>5/8\), obtained by
integrating the geometric series for $1/(1-t^2)$ on $[0,1/3]$.

The absolute convergence supplied by (3.6) justifies termwise Fourier
summation. Replacing \(\theta\) by \(\theta+\pi/2\), pairing the positive
and negative modes, and writing $u=\cos\theta$, gives

\[
e^{izu}=J_0(z)+2\sum_{n\ge1}i^nJ_n(z)T_n(u),\quad -1\le u\le1.
\tag{3.8}
\]

Here $T_n(\cos\theta)=\cos(n\theta)$. The spectral theorem now gives
the operator-norm convergent identity

\[
e^{isH}=\sum_{n\ge0}\beta_n(as)T_n(H/a),\qquad
\beta_0(z)=J_0(z),\quad \beta_n(z)=2i^nJ_n(z)\ (n\ge1),
\tag{3.9}
\]

and \(\|T_n(H/a)\|\le1\).

Put \(D=\lceil2z\rceil\). By Cauchy--Schwarz and (3.5),

\[
\sum_{|n|\le D}|J_n(z)|\le\sqrt{2D+1}\le\sqrt{4z+3}.
\]

For the two remaining tails use (3.7). Consequently

\[
\sum_{n\ge0}|\beta_n(z)|
=\sum_{n\in\mathbb Z}|J_n(z)|
\le\sqrt{4z+3}+C_0,
\quad C_0:=\frac2{1-e^{-1/4}}.
\tag{3.10}
\]

For every integer $L\ge2z$, (3.7) also proves the operator estimate

\[
\left\|e^{isH}-\sum_{n=0}^L\beta_n(z)T_n(H/a)\right\|
\le C_0e^{-(L+1)/4}.
\tag{3.11}
\]

In particular, with $z=a\tau N$ and

\[
L_N=\left\lceil2a\tau N+4K\log N+4\log C_0\right\rceil,
\tag{3.12}
\]

the right side of (3.11) is at most $N^{-K}$. This uses the exact
prescribed $\tau$, and $L_N=\Theta(N)$ for fixed $\tau>0$.

### 3.3. Error of the full product

Let $Q_N$ denote either polynomial approximation above, with
\(\|E_N-Q_N\|\le\varepsilon_N\). Its conjugates approximate every
factor in (2.4) with the same error, and \(\|Q_N\|\le1+\varepsilon_N\).
A telescoping expansion gives

\[
\|U_N^m-(Q_NM_N)^m\|
\le m\varepsilon_N(1+\varepsilon_N)^{m-1}.
\tag{3.13}
\]

At a Pell return $m=2r$, this is
\(O((\log N)N^{-K})\) for the choices above. For any fixed $B$ and
all $m\le BN$, $K>1$ gives

\[
\sup_{1\le m\le BN}
\left|\operatorname{tr}_NU_N^m-
             \operatorname{tr}_N(Q_NM_N)^m\right|
=O_B(N^{1-K}).
\tag{3.14}
\]

These are complete norm-error estimates for a growing-degree
approximation. They make no claim that the remaining polynomial trace
has been estimated, or that the matrix $Q_NM_N$ is unitary.

## 4. Exact first aliases in the two-copy limit

Let $R_N=M_N^r$ on the Pell dimensions (2.5). By (2.2),

\[
R_NW_vR_N^*=W_{cv}.
\tag{4.1}
\]

For scalar integer labels $V,W$, the alias condition is

\[
V+cW\equiv0\pmod N
\iff
V+W=xp,\quad V-W=yq,
\quad p,q\in\mathbb Z,\quad p\equiv q\pmod2.
\tag{4.2}
\]

Indeed, (2.6) gives the two congruences modulo $x$ and $y$. Their
simultaneous solutions are

\[
V=\frac{xp+yq}{2},\qquad W=\frac{xp-yq}{2},
\]

and these are integers exactly for the indicated parity. The converse
follows from the Chinese remainder theorem because $\gcd(x,y)=1$.

The lattice in (4.2) has basis

\[
b_1=\left(\frac{x+y}{2},\frac{x-y}{2}\right),\qquad
b_2=\left(\frac{x-y}{2},\frac{x+y}{2}\right),
\tag{4.3}
\]

with determinant $xy=N$. Its shortest nonzero \(\ell^1\) length is
exactly $x$. To prove this, note the identity

\[
|V|+|W|=\max(x|p|,y|q|).
\tag{4.4}
\]

If $p,q$ are odd, the right side is at least $x$, attained for

\((p,q)=(1,1)\). If both are even and not both zero, it is at least
\(\min(2x,2y)=2y>x\). The last inequality follows from
\(y<x<\sqrt2y\) for the odd indices $r\ge3$.

This yields an explicit failure of uniform fixed-word convergence at a
growing word length. Take

\[
V=(x+y)/2,\qquad W=(x-y)/2.
\]

For the base label $v=(1,0)$, all symplectic product phases vanish,
and

\[
W_v^V(R_NW_vR_N^*)^W
=W_{(V+cW,0)}=I,
\quad V+cW=N(2y-x).
\tag{4.5}
\]

The normalized trace is exactly one. In the fixed two-copy tracial
limit used in Round 11, this word has trace zero, since its two separate
totals $Vv,Wv$ are nonzero. Its length is $V+W=x\asymp\sqrt N$.
Thus that fixed-word limit cannot be asserted uniformly up to these
lengths. This is a statement about the proposed approximation method;
it is not an original spectral countersequence.

For completeness, the count of scalar aliases in the square
\([-L,L]^2\) obeys

\[
\frac{4(L-x/2)_+^2}{N}
\le\#\{(V,W): |V|,|W|\le L,\ V+cW\equiv0\pmod N\}
\le\frac{4(L+x/2)^2}{N}.
\tag{4.6}
\]

The centered fundamental parallelogram of (4.3) is contained in the
\(\ell^\infty\) ball of radius $x/2$. Its translates tile the plane,
with area $N$ each. The union of cells whose centers lie in the square
contains the square of radius $(L-x/2)_+$, and is contained in the
square of radius $L+x/2$. Comparing areas proves (4.6). Thus for

\(L=\lfloor\tau N\rfloor\) the count is asymptotic to $4\tau^2N$.
No claim follows that these aliases carry large exponential
coefficients; (4.6) is only a count.

## 5. The controlled degree range carries vanishing Bessel mass

Here is a direct bound sufficient to test the proposed resummation:

\[
|J_n(z)|\le4z^{-1/2},\qquad z>0,\quad 0\le n\le z/2.
\tag{5.1}
\]

For $z\le16$, the integral definition gives $|J_n(z)|\le1$, which
implies (5.1). Suppose $z\ge16$. Set

\(\nu=n/z\in[0,1/2]\), \(\delta=z^{-1/2}\le1/4\), and split the
interval of integration according as \(|\cos\theta-\nu|\le\delta\)
or not. On that set, \(\cos\theta\in[-1/4,3/4]\), so
\(|\sin\theta|\ge\sqrt7/4\). On each of the intervals

\([-\pi,0]\) and \([0,\pi]\), cosine is monotone. The total length of
the exceptional set is therefore at most $16\delta/\sqrt7$.

The complement consists of at most four intervals. On each, the
derivative of the phase \(\sin\theta-\nu\theta\) is monotone, has one
sign, and has modulus at least \(\delta\). Integration by parts gives
a bound $3/(z\delta)$ for each integral: its endpoint terms are at
most $2/(z\delta)$, and the integral of

\(|\sin\theta|/|\cos\theta-\nu|^2\) is the total variation of the
reciprocal derivative, at most $1/\delta$. Hence

\[
|J_n(z)|\le\frac1{2\pi}
 \left(\frac{16\delta}{\sqrt7}+\frac{12}{z\delta}\right)
<4z^{-1/2},
\]

proving (5.1) without a stationary-phase theorem.

For any integer $L\le z/2$, (5.1) gives

\[
\sum_{n=0}^{L}|\beta_n(z)|^2\le\frac{64(L+1)}{z}.
\tag{5.2}
\]

In particular, at $z=a\tau N$, every fixed constant $C$ gives

\[
\sum_{n\le C\sqrt N}|\beta_n(a\tau N)|^2
=O_C((\tau\sqrt N)^{-1})\longrightarrow0.
\tag{5.3}
\]

The hypotheses $L\le z/2$ hold eventually, however large the fixed
threshold caused by the small prescribed $\tau$. Meanwhile (3.5) gives

\[
\sum_{n\ge0}|\beta_n(z)|^2=2-|J_0(z)|^2\longrightarrow2.
\tag{5.4}
\]

Thus the high degrees cannot be discarded on the basis of small
coefficient \(\ell^2\) mass. Statements (5.3)--(5.4) are coefficient
statements; they do not identify operator norms, because the matrices
\(T_n(A_N/a)\) are not an orthogonal family. The already existing
Round 8 band-escape results are consistent with the necessity of
linear degree and are not claimed as new here.

Taking absolute values in a $d=2r$ factor expansion yields at best the
coefficient bound

\[
\left(\sqrt{4a\tau N+3}+C_0\right)^{2r}.
\tag{5.5}
\]

Its logarithm is $O((\log N)^2)$; it does not give a useful trace
bound. Replacing an exponential coefficient budget by (5.5) has not
provided the required signs or correlations.

## 6. Exact remaining signed sum after the tail has been removed

This section records the actual missing estimate and does not introduce
it as a hypothesis. Let $G_N=(\mathbb Z/N\mathbb Z)^2$. Write

\[
A_N=\sum_{w\in G_N}a_N(w)W_w,\qquad
T_n(A_N/a)=\sum_{v\in G_N}t_{n,N}(v)W_v.
\]

Here $a_N(w)$ is the sum of the original Fourier coefficients with
label congruent to $w$, so all small-dimensional aliases are included.
Equation (2.1) and the Chebyshev recurrence give exactly

\[
\begin{split}
t_{0,N}(v)&=\mathbf1_{v=0},\qquad t_{1,N}(v)=a_N(v)/a,\\
t_{n+1,N}(v)&=\frac2a\sum_{w\in G_N}a_N(w)t_{n,N}(v-w)
 e_N(\overline2\sigma(w,v-w))-t_{n-1,N}(v).
\end{split}
\tag{6.1}
\]

For the truncation (3.12), define

\[
q_N(v)=\sum_{n=0}^{L_N}\beta_n(a\tau N)t_{n,N}(v),\qquad
Q_N=\sum_{v\in G_N}q_N(v)W_v,
\tag{6.2}
\]

and the known finite metaplectic character

\[
\chi_{m,N}(v)=\operatorname{tr}_N(W_vM_N^m).
\tag{6.3}
\]

The normalized trace of the full truncated product is the finite sum

\[
\begin{split}
\mathcal S_{m,N}
:={}&\operatorname{tr}_N(Q_NM_N)^m\\
={}&\sum_{v_0,\ldots,v_{m-1}\in G_N}
 \left[\prod_{j=0}^{m-1}q_N(C^{-j}v_j)\right]
 e_N\left(\overline2\sum_{0\le i<j<m}\sigma(v_i,v_j)\right)
 \chi_{m,N}\left(\sum_{j=0}^{m-1}v_j\right).
\end{split}
\tag{6.4}
\]

This follows from (2.2), followed by multiplication using (2.1).
No absolute values, phase deletions, or selection of low frequencies is
used. On the Pell dimensions, if $m$ is a multiple of $2r$, then

\[
\chi_{m,N}(v)=\gamma_N^{m/(2r)}\mathbf1_{v=0},
\tag{6.5}
\]

so (6.4) is a full signed alias sum. For other $m$, (6.3) is retained.
Although the factors $X_{j,N}$ repeat with period $2r$, the number of
factors in (6.4) is still $m$, which reaches order $N$ in the target.

Take the parent's fixed admissible test $b_*$, whose Fourier support
is in $[-2,2]$, and set $w(t)=|\widehat b_*(t)|^2$. Equations
(3.13)--(3.14), the bound $|\operatorname{tr}_NU_N^m|\le1$, and

\(|\mathcal S_{m,N}|\le(1+N^{-K})^m\) give, for $K>2$,

\[
\begin{split}
&\frac1{N^2}\sum_{1\le m<2N}w(m/N)
 \left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)\\
&\qquad=\sum_{1\le m<2N}w(m/N)
 \left(|\mathcal S_{m,N}|^2-\frac{\min(m,N)}{N^2}\right)
 +O_{b_*,K}(N^{2-K}).
\end{split}
\tag{6.6}
\]

For clarity, the error follows term by term from

\[
\big||\operatorname{tr}_NU_N^m|^2-|\mathcal S_{m,N}|^2\big|
\le \big(1+(1+N^{-K})^m\big)
       mN^{-K}(1+N^{-K})^{m-1};
\]

summing $m\le2N$ gives $O(N^{2-K})$.

The following statement is **not proved** here, even on the Pell
subsequence:

\[
\boxed{
\sum_{1\le m<2N}w(m/N)
 \left(|\mathcal S_{m,N}|^2-\frac{\min(m,N)}{N^2}\right)
\longrightarrow0.}
\tag{6.7}
\]

Consequently the exact original pair estimate on the left of (6.6)
remains unproved. The short-Pell trace bound from the old pressure
work does not supply (6.7). The bounded coefficients
\(\|T_n(A_N/a)\|\le1\), the \(\ell^1\) improvement (3.10), and the
CRT classification (4.2) do not imply it. The issue is the full signed
high-degree sum; the discarded scalar tail is not the issue after
(3.12).

This also does not estimate the operator-norm difference between
\(\prod_j e^{isX_{j,N}}\) and a finite-order Magnus approximation.
A finite-order commutator coefficient, including the Round 11 lower
bound for the second coefficient, cannot be substituted for (6.7).

## 7. Flat endpoint check: old mechanism, no full-product implication

During the attempted two-copy estimate, the exact coordinate vector
\(\delta_0\) was tested. Directly from the original $l=0,\pm1$
Fourier modes,

\[
\|(A_N-9I/10)\delta_0\|
=\frac{\sqrt2}{200}r\left(\frac12+\frac1{2N}\right)
\le\frac{\sqrt2\pi^2}{200N^2}.
\tag{7.1}
\]

The diagonal entry is $9/10$. The two off-diagonal entries have
equal modulus $r(1/2+1/(2N))/200$, at coordinates $1,-1$, and

\[
r\left(\frac12+\frac1{2N}\right)
=4\cos^2\left(\frac{7\pi}{2N}\right)
  \sin^2\left(\frac{\pi}{2N}\right)\le\pi^2/N^2.
\]

The spectral theorem, using \(|e^{isu}-e^{isv}|\le s|u-v|\), gives

\[
\|E_N\delta_0-e^{i(9/10)N\tau}\delta_0\|
\le\frac{\sqrt2\pi^2\tau}{200N}.
\tag{7.2}
\]

On the Pell dimensions, define \((\Pi_c\psi)(x)=\psi(cx)\). Since
\(c^2\equiv1\pmod N\), direct conjugation gives
\(\Pi_cW_v\Pi_c^*=W_{cv}\). Equation (4.1) and Weyl irreducibility
therefore imply $R_N=\zeta_N\Pi_c$. In particular, $R_N\delta_0$
is a scalar multiple of \(\delta_0\). Both $E_N$ and
\(R_NE_NR_N^*\) satisfy (7.2), and their two-factor product has error
at most twice the right side from the phase $e^{i(9/5)N\tau}$.

This is not presented as a new spectral theorem: it is a rank-one
specialization of the weak Jacobi-coupling/flat-packet mechanism already
analyzed in the fully inspected Round 3 source. That source also gives
the contrary full-propagator effect: small coordinate packets are sent
almost orthogonally to themselves by $E_NM_N$. The two isolated factors
at indices $0,r$ do not control the other $2r-2$ factors in (2.7).
No spectral cluster, quasimode of the full $U_N$, or countersequence is
inferred from (7.2).

## 8. Verification and final ledger

The companion `r12_full_product_exact_checks.py` performs integer
checks of the Pell identities, the lattice determinant, the explicit
alias word, and the shortest alias on several finite indices. These
are regression checks of the displayed proofs, not an asymptotic
experiment or a measurement of the original spectral statistics.

**Established in this branch:** the complete physical scalar tail
estimates (3.1)--(3.14), the exact alias lattice and growing-word test
(4.2)--(4.6), the elementary Bessel coefficient bound (5.1)--(5.4), and
the exact full-sum/error identity (6.4)--(6.6).

**Not established:** a new signed-sum bound for original traces at
times of order $N$, (6.7), any $H_{\rm diag}$ conclusion, a fixed
admissible countertest, or the physical remainder after retaining
finitely many Magnus coefficients. None of the standard approximation
facts above is counted as the requested fundamental closure.
