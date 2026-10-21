> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_all_entry_validation.md`. Embedded SHA256: `5ebdc6987ebaf1d35d9902dfd03a569604a5aeb45c1d7b46bdf865fa0ce06acd`.
> [Thematic guide](../../topics/classical_trace.md).

# Independent derivation of uniform adjoint-entry bounds

21 October 2026. This manuscript independently checks the proposed all-entry extension of the exact one-step Weyl calculation. The original kick $E_N=\exp(i\tau N A_N)$, with $\tau=10^{-80}$, is fixed throughout.

## 0. Statement and frozen inputs

Use the centered representatives
$$
I_N=\{-(N-1)/2,\ldots,(N-1)/2\},\qquad
v,w\in I_N^2,
$$
and the ordinary-half Weyl matrices
$$
W_N(k,l)=(-1)^{kl}T_N(l,k).
$$
Write $|v|_N=|v|$ for the Euclidean norm of the centered representative and define
$$
C^E_N(w,v)=\frac1N\operatorname{Tr}\bigl(W_N(w)^*E_NW_N(v)E_N^*\bigr).
\tag{0.1}
$$

**Theorem.** There are fixed constants $C,N_0$ and $0<\rho_*<1$ such that for every odd $N\ge N_0$:

$$
|C^E_N(w,v)|\le C(1+|v|_N)^{-1/17}+C/N,
\qquad
|C^E_N(w,v)|\le C(1+|w|_N)^{-1/17}+C/N,
\tag{0.2}
$$
and, on the nonzero-label sector,
$$
\sup_{v,w\ne0}|C^E_N(w,v)|\le\rho_*.
\tag{0.3}
$$
For every permutation $\pi$ of the nonzero labels, let $K_\pi$ retain only the entries $C^E_N(\pi(v),v)$. With $D=N^2-1$,
$$
\|K_\pi\|\le\rho_*,
\qquad D^{-1/2}\|K_\pi\|_{\rm HS}\le C N^{-1/17}.
\tag{0.4}
$$
The constants are independent of the permutation. No arithmetic divisor restriction appears.

The starting analytic input is the exact Weyl WKB construction in counter_one_step_pinching_hs.md, SHA-256 a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629, independently audited in audit_one_step_pinching_hs.md, SHA-256 7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce. Its ordinary symbol is
$$
\begin{aligned}
a(q,p)={}&\cos(14\pi q)+r(q)/10+r(q)\sin(2\pi q)/100-1/10\\
&+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
\end{aligned}
\tag{0.5}
$$
Its Fourier support has $\ell^1$ radius at most $9$, its coefficient one-norm is less than $2$, and
$$
a_{(1,0)}=1/20-i/200,\qquad
a_{(0,1)}=(-3-4i)/1000.
\tag{0.6}
$$

The wider analytic strip for the same exact phase is proved in counter_center_phase_c17_bound.md, SHA-256 992f35db1916f680083fe304caa3001bc71720e2a864f28ea3513f080b5340c5, independently audited in dual_audit_center_phase_c17.md, SHA-256 f9389738b8ff10a520d3c8a9c2d1ad4467e7990273433de4d7e517ccfdd87ad0. The differential extractors used below are reproduced explicitly from audit_explicit_symbol_finite_type16.md, SHA-256 1da0fbd15dec74a90a742804f69165f478673ce07aaf7eb38760de7f60cb7ffb. Their independent audit is dual_audit_explicit_finite_type16.md, SHA-256 34ecf87576cb73990458a656200d9b6e41016f0082796beacea247106c4ed90e.

The proof below adds the arbitrary output label and arbitrary linear phase, rather than treating only the diagonal echo. It gives an independent derivation of the finite-dimensional identities and the required additional estimates. It does not assert spectral universality.

## 1. The exact phase and its $C^{18}$ margin

Let
$$
h=(2\pi N)^{-1},\qquad t=\tau/(2\pi),\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$
The frozen construction gives real periodic $S=S_t$, real positive periodic $b=b_t$, and
$$
F_N(x)=b(x)e^{2\pi iN S(x)},\qquad
B_N=Q_N(F_N),\qquad
N^{-1/2}\|E_N-B_N\|_{\rm HS}\le C/N.
\tag{1.1}
$$
All derivatives of $S,b$ of any fixed order are bounded independently of $N$, and $\int b^2=1$. The functions are the exact center action and its transport amplitude. In particular, no first-order approximation is substituted into the oscillatory exponential.

Put $\varrho=10^{-3}$. The larger-strip argument from the cited supplement proves, on the common complex strip of width $3\varrho/4$,
$$
\left|S_t/t-a\right|\le20000t.
\tag{1.2}
$$
Cauchy's estimate on polydisks gives, now through order $18$,
$$
\left\|S_t/t-a\right\|_{C^{18},\max}
\le20000t\,18!\left(\frac{4000}{3}\right)^{18}.
\tag{1.3}
$$
Since $2\pi>6$, the right side is strictly smaller than
$$
\frac{20000}{6\cdot10^{80}}\,18!\left(\frac{4000}{3}\right)^{18}
=\frac{127903052333056}{3378810882568359375}
<\frac1{4000}.
\tag{1.4}
$$
The last inequality is exact rational arithmetic. The maximum, rather than the sum, convention for $C^{18}$ is used; no count of multiindices is required.

The same construction gives $\|\nabla^2S\|_{\rm op}<1/10$. For example, on the smaller strip in the frozen source each Hessian entry is at most $8\cdot10^5t$, so its Euclidean operator norm is at most $1.6\cdot10^6t<1/10$.

## 2. Finite type through order 17, using only derivatives of order at least two

Let $D_q=(2\pi i)^{-1}\partial_q$, $D_p=(2\pi i)^{-1}\partial_p$, and
$$
\mathcal K=\{-9,-8,-7,-6,-5,-2,-1,1,2,5,6,7,8,9\}.
$$
Define
$$
P_1(s)=s\prod_{k\in\mathcal K\setminus\{1\}}\frac{s-k}{1-k},
$$
$$
\mathcal L_1=D_q(1-D_p^2)P_1(D_q),\qquad
\mathcal L_2=D_p\,\frac{D_p(D_p+1)}2
\prod_{k\in\{1,6,7,8\}}\left(1-\frac{D_q^2}{k^2}\right).
\tag{2.1}
$$
The first operator has order at most $17$, the second order at most $11$, and every differential monomial has order at least two. On the exact support of $a$, they satisfy
$$
\mathcal L_1a=a_{(1,0)}e^{2\pi iq},\qquad
\mathcal L_2a=a_{(0,1)}e^{2\pi ip}.
\tag{2.2}
$$
Indeed the extra $D_q$ or $D_p$ is one on the isolated coordinate mode. The other factors kill exactly the unwanted support: the first operator kills the mixed rows and all pure modes except $1$; the second kills the rows $l=0,-1$ and all nonzero $q$ frequencies in row $l=1$.

Multiplication by $D_q$ or $D_p$ does not change the formal coefficient one-norm. The product bounds for these norms are
$$
\|\mathcal L_1\|_{\ell^1(D_q,D_p)}\le27,\qquad
\|\mathcal L_2\|_{\ell^1(D_q,D_p)}
\le\frac{60125}{28224}<3.
\tag{2.3}
$$
For completeness, the first bound is twice
$$
3\cdot\frac64\cdot\frac75\cdot\frac86\cdot\frac97\cdot\frac{10}8=\frac{27}{2},
$$
with all negative-frequency factors contributing one. The second is
$$
2\cdot\frac{37}{36}\cdot\frac{50}{49}\cdot\frac{65}{64}<3.
$$
Passing to ordinary derivatives can only decrease these coefficient bounds.

For a nonzero torus translation $z$, take a centered lift and put
$\delta=\operatorname{dist}(z,0)=|z|$. For any $A$, write
$$
F_z^A(x)=\frac{A(x+z)-A(x)}{\delta}.
$$
At least one coordinate of $z$ has magnitude at least $\delta/\sqrt2$. Using $|e^{2\pi iu}-1|\ge4|u|$ for centered $u$, the isolated modes in (2.2) give
$$
\max_{2\le|\alpha|\le17}
|\partial^\alpha F_z^a(x)|
\ge\frac{\sqrt2}{300}
\tag{2.4}
$$
at every $x$. If the first coordinate dominates, the better lower bound is $\sqrt2/270$, obtained from $|a_{(1,0)}|\ge1/20$ and the coefficient budget $27$. If the second dominates, use $|a_{(0,1)}|=1/200$ and the budget $3$.

If $\|A-a\|_{C^{18},\max}<1/4000$, the mean-value integral gives, for every $|\alpha|\le17$,
$$
|\partial^\alpha(F_z^A-F_z^a)(x)|
\le\sqrt2\|A-a\|_{C^{18},\max}<\frac{\sqrt2}{4000}.
\tag{2.5}
$$
Applying this with $A=S/t$ and using (1.4) proves
$$
\boxed{\quad
\max_{2\le|\alpha|\le17}
\left|\partial^\alpha\frac{S(x+z)-S(x)}{\delta}\right|
>\frac{t}{2000}.
\quad}
\tag{2.6}
$$
The derivatives of the normalized differences through any fixed order are uniformly bounded by the mean-value formula and derivatives of $S$. The same lower and upper bounds extend to the directional limits as $z\to0$.

## 3. Oscillation with an arbitrary linear phase

The use of orders at least two in (2.6) is essential here. It proves the uniform estimate
$$
\left|\int_{\mathbb T^2}A_z(x)
e^{2\pi i[\lambda F_z^S(x)+\ell\cdot x]}\,dx\right|
\le C(1+\lambda)^{-1/17}
\tag{3.1}
$$
for $\lambda\ge0$, arbitrary integer $\ell$, and any family $A_z$ with a fixed sufficiently high smoothness bound. The phase is interpreted in local charts; the integrand is periodic when $\ell$ is an integer.

Here are the details needed for uniformity in the linear term. For each order $j$, a finite collection of unit directions controls all homogeneous $j$-th partial derivatives. One can use $j+1$ distinct slopes: evaluation of the homogeneous polynomial $u\mapsto(u\cdot\nabla)^jF$ at those slopes is an invertible Vandermonde system. Thus (2.6) gives, at each point, a direction and an order $2\le j\le17$ with directional derivative bounded below by a fixed positive constant. The uniform derivative upper bounds through order $18$ preserve half that bound on a ball of fixed radius.

Choose a fixed finite smooth spatial partition on smaller balls. For each ball and each $z$, select a direction/order at its center. Its lower bound holds on the larger ball containing the support of the partition function. The derivatives of the partition functions are fixed; smooth dependence of the selected direction on $z$ is not needed. Rotate coordinates on that chart and integrate first in the selected direction.

On every such line segment, the $j$-th derivative of the full phase has magnitude at least $c\lambda$, because $j\ge2$ annihilates $\ell\cdot x$. The one-dimensional estimate
$$
\left|\int A(u)e^{i\phi(u)}\,du\right|
\le C_j\mu^{-1/j}
\bigl(\|A\|_\infty+\|A'\|_1\bigr),
\qquad |\phi^{(j)}|\ge\mu,\ j\ge2,
\tag{3.2}
$$
requires no upper bound on the linear part.

An elementary derivation of (3.2) is as follows. A $j$-th derivative with nonzero constant sign implies that $\phi''$ has at most $j-2$ distinct zeros, by repeated Rolle arguments. The sublevel set $\{|\phi'|\le u_0\}$ has measure at most $C_j(u_0/\mu)^{1/(j-1)}$, by the divided-difference mean-value formula applied to $\phi'$. On each of the at most $j-1$ monotonicity intervals of $\phi'$, the part with $|\phi'|>u_0$ is controlled by integration by parts by $C_j(\|A\|_\infty+\|A'\|_1)/u_0$. Choosing $u_0=\mu^{1/j}$ balances the two bounds and proves (3.2), with the trivial integral estimate used if $\mu<1$. Approximation handles endpoints and closed sublevel sets.

Applying (3.2) on each chart and integrating the transverse coordinate proves (3.1). All constants depend on the fixed symbol, $t$, and the amplitude bounds, but not on $z,\ell,\lambda,N$. This argument also supplies a direct finite-type-to-oscillation proof for the added linear term.

## 4. Exact coefficient representation, with all aliases retained

The exact Weyl product and alias pairing from the frozen source are
$$
W_N(u)W_N(v)=e^{\pi i(u_2v_1-u_1v_2)/N}W_N(u+v),
\tag{4.1}
$$
$$
\frac1N\operatorname{Tr}(Q_N(F)^*Q_N(G))
=\sum_{m=(r,s)\in\mathbb Z^2}(-1)^{rs}
\int_{\mathbb T^2}\overline{F(x+(s/2,r/2))}
G(x)e^{-2\pi iNm\cdot x}\,dx.
\tag{4.2}
$$
The latter follows from
$$
W_N(v+Nm)=(-1)^{v_1s+v_2r+rs}W_N(v).
$$
All these are exact identities for odd $N$, including the modular-half convention.

Rewrite (0.1) as the normalized Hilbert--Schmidt pairing
$$
C^E_N(w,v)=\langle W_N(w)E_N,E_NW_N(v)\rangle_2,
\qquad \langle X,Y\rangle_2=N^{-1}\operatorname{Tr}(X^*Y).
\tag{4.3}
$$
Using (1.1) twice changes it by $O(N^{-1})$, uniformly in $v,w$. Indeed the difference is bounded by
$$
\|E_N-B_N\|_2\bigl(\|E_N\|_2+\|B_N\|_2\bigr)=O(N^{-1}),
$$
since $\|E_N\|_2=1$ and $\|B_N\|_2\le1+O(N^{-1})$. No operator-norm approximation to $B_N$ is required.

Exact multiplication by a single mode gives
$$
W_N(w)Q_N(F_N)=Q_N\!\left(e_w(x)F_N(x+Jw/(2N))\right),
$$
$$
Q_N(F_N)W_N(v)=Q_N\!\left(e_v(x)F_N(x-Jv/(2N))\right).
\tag{4.4}
$$
Apply (4.2). In the term indexed by $m$, set
$$
k_m=v-w-Nm,\qquad
z_m\equiv-\frac{J(v-k_m/2)}N\pmod{\mathbb Z^2}.
\tag{4.5}
$$
One obtains
$$
\boxed{\quad
C^E_N(w,v)
=\sum_{m\in\mathbb Z^2}\gamma_{m,v,w}
\int b(x)b(x+z_m)
e^{2\pi i[N(S(x+z_m)-S(x))+k_m\cdot x]}\,dx
+O(N^{-1}),
\quad}
\tag{4.6}
$$
where every $\gamma_{m,v,w}$ has modulus one.

To check the shift and its sign explicitly, before the final change of variable the paired symbols have the relative shift
$$
\frac{J(v+w)}{2N}+(s/2,r/2)
\equiv\frac{J(v-k_m/2)}N\pmod{\mathbb Z^2}.
$$
Here $(s/2,r/2)\equiv Jm/2$ modulo integers. This relative shift occurs in the conjugated factor $F_N$. Shifting the integration variable to that factor reverses its sign, giving $z_m$ in (4.5), and multiplies the integral only by a unit phase. This verifies the full alias formula rather than discarding nonzero aliases.

For each fixed $N$, the original Fourier series are absolutely convergent. The uniform estimates in the next section justify absolute summation of the alias integrals in (4.6).

## 5. High input labels: the two alias regimes

Put $r=|v|_N$. The centered lift is nearest to zero among its translates by $N\mathbb Z^2$:
$$
|v-Nj|\ge|v|\qquad(j\in\mathbb Z^2).
\tag{5.1}
$$

First suppose $|k_m|\le r$. Equation (4.5) and (5.1) give
$$
\begin{aligned}
N\operatorname{dist}(z_m,0)
&=\operatorname{dist}(v-k_m/2,N\mathbb Z^2)\\
&\ge |v|-|k_m|/2\ge r/2.
\end{aligned}
\tag{5.2}
$$
This inequality remains valid near the boundary of the centered square; it does not assume that the lift $v-k_m/2$ is itself centered.

Apply (3.1) with
$\lambda=N\operatorname{dist}(z_m,0)$, $\ell=k_m$, and amplitude $b(x)b(x+z_m)$. When $z_m=0$, (5.2) forces $r=0$, for which the trivial bound suffices. Every term in this regime is therefore bounded by
$$
C(1+r)^{-1/17}.
\tag{5.3}
$$
There are only a fixed number of such aliases: $|v-w|_\infty<N$ and $|k_m|\le r<N$ imply $|m|_\infty<2$. A bound of $25$ aliases is more than sufficient.

Next suppose $|k_m|>r$. Choose the particular lift
$$
z'_m=-J(v-k_m/2)/N,
$$
without requiring that it be centered. It satisfies
$$
N|z'_m|\le|v|+|k_m|/2<\tfrac32|k_m|.
\tag{5.4}
$$
For the phase
$$
\phi_m(x)=N(S(x+z'_m)-S(x))+k_m\cdot x,
$$
the mean-value formula and $\|\nabla^2S\|_{\rm op}<1/10$ show
$$
\left|N\nabla(S(x+z'_m)-S(x))\right|<\tfrac3{20}|k_m|.
\tag{5.5}
$$
Choose a coordinate $j$ with $|(k_m)_j|\ge|k_m|/\sqrt2$. Then
$$
|\partial_j\phi_m(x)|
\ge(1/\sqrt2-3/20)|k_m|>\tfrac12|k_m|.
\tag{5.6}
$$
Every higher derivative of $N(S(x+z'_m)-S(x))$ is bounded by a fixed constant times $|k_m|$, by (5.4) and the corresponding derivative of $S$. These constants do not depend on the possibly long lift $z'_m$. The amplitude has uniform derivative bounds because it depends only on the torus translation.

Repeated integration by parts in coordinate $j$, with the factor $(2\pi i\partial_j\phi_m)^{-1}\partial_j$, now gives for every fixed integer $K$
$$
\left|\int b(x)b(x+z_m)e^{2\pi i\phi_m(x)}\,dx\right|
\le C_K(1+|k_m|)^{-K}.
\tag{5.7}
$$
The boundary terms cancel: $k_m$ is integral, and the amplitude and derivatives of the periodic part of the phase are periodic. Formula (5.6) and the higher-derivative bounds imply the claimed power at every integration.

For $|m|_\infty\ge3$,
$$
|k_m|_\infty\ge N(|m|_\infty-1)
\ge\tfrac23N|m|_\infty.
$$
Thus the far-alias sum in (5.7) is $O_K(N^{-K})$ for $K>2$. The finitely many remaining aliases in this second regime are $O_K((1+r)^{-K})$. Since $r<N$, their total is also $O_K((1+r)^{-K})$.

Combining the two regimes with (4.6) proves the first estimate in (0.2).

Replacing $a$ by $-a$ repeats the whole construction with exactly the same absolute derivative budgets and gives the corresponding column estimate for $E_N^*$. Its adjoint matrix is $(C^E_N)^*$, so the column estimate for $E_N^*$ is the row estimate in (0.2). This proves both estimates.

## 6. Fixed labels: an exact finite-difference Egorov limit

It remains to rule out an entry approaching one among the bounded labels. Let $\Psi_s$ be the real Hamiltonian flow
$$
\Psi_s'=J\nabla a(\Psi_s),\qquad\Psi_0(x)=x,
\tag{6.1}
$$
and, for fixed integer $v$, put
$$
\beta_s(x)=e^{2\pi i v\cdot\Psi_s(x)}.
$$
This is periodic and satisfies
$$
\partial_s\beta_s=(J\nabla a)\cdot\nabla\beta_s.
\tag{6.2}
$$
The sign in (6.1) follows from the $+i$ in $E_N=\exp(itQ_N(a)/h)$.

The exact finite-shift commutator is
$$
\frac{i}{h}(a\star_h\beta-\beta\star_h a)
=\frac{i}{h}\sum_\kappa a_\kappa e_\kappa(x)
\left[\beta(x+\pi hJ\kappa)-\beta(x-\pi hJ\kappa)\right].
\tag{6.3}
$$
Taylor's formula through the linear term gives
$$
\frac{i}{h}(a\star_h\beta-\beta\star_h a)
=(J\nabla a)\cdot\nabla\beta+O_v(h^2)
\tag{6.4}
$$
in supremum norm, uniformly for $s$ in the fixed short interval. There are finitely many $\kappa$; the remainder is bounded by the third derivatives of $\beta_s$, which are finite for each fixed $v$.

The exact quantization bound
$N^{-1/2}\|Q_N(R)\|_{\rm HS}\le2\|R\|_\infty$
and Duhamel's formula in the Hilbert--Schmidt space give
$$
N^{-1/2}\left\|E_NW_N(v)E_N^*-Q_N(\beta_t)\right\|_{\rm HS}
=O_v(N^{-2}).
\tag{6.5}
$$
Conjugation by $E_N$ is exactly unitary on that Hilbert space, so no operator-norm symbolic estimate is invoked.

For fixed $w$, the exact Weyl trace pairs $W_N(w)$ with only Fourier modes of $\beta_t$ congruent to $w$ modulo $N$. Smooth Fourier decay makes the nonzero aliases tend to zero. Hence
$$
\boxed{\quad
C^E_N(w,v)\longrightarrow
\int_{\mathbb T^2}e^{2\pi i[v\cdot\Psi_t(x)-w\cdot x]}\,dx
\quad}
\tag{6.6}
$$
for every fixed pair $v,w$.

## 7. The classical coefficient is strictly below one

Let $v\ne0$. Write the lift of the flow as
$$
\Psi_t(x)=x+D_t(x),
$$
where $D_t$ is periodic. The direct bounds
$\|\nabla a\|_\infty<200$ and
$\|D(J\nabla a)\|_{\infty\to\infty}<10^4$
from the frozen short-time construction give, component by component,
$$
D_t(x)=tJ\nabla a(x)+R_t(x),\qquad
\|R_t\|_\infty\le10^6t^2.
\tag{7.1}
$$
Indeed integrate
$|J\nabla a(\Psi_s(x))-J\nabla a(x)|_\infty
\le10^4\cdot200s$
from $0$ to $t$.

Choose $j\in\{1,2\}$ so that
$$
|v\cdot Je_j|=\max(|v_1|,|v_2|)=:v_{\max}>0.
$$
At Fourier mode $e_j$, (7.1) and (0.6) imply
$$
\begin{aligned}
|\widehat{v\cdot D_t}(e_j)|
&\ge2\pi t\,v_{\max}|a_{e_j}|
-|v|_1\,10^6t^2\\
&\ge v_{\max}\left(\frac{2\pi t}{200}-2\cdot10^6t^2\right)>0.
\end{aligned}
\tag{7.2}
$$
The final strict inequality holds at the fixed $t=10^{-80}/(2\pi)$, and already throughout the certified small interval. Therefore $v\cdot D_t$ is not constant for any nonzero integer $v$.

If the integral in (6.6) had modulus one, its continuous integrand, everywhere of modulus one, would have to be constant. For example, expand the integral of its squared distance from the unit complex number in the direction of its mean. Thus
$$
e^{2\pi i[(v-w)\cdot x+v\cdot D_t(x)]}
$$
would be constant. The real phase on $\mathbb R^2$ then takes values in one translate of $\mathbb Z$, and continuity forces it to be constant. Taking its increment under $x\mapsto x+e_j$ gives $v_j-w_j=0$. Hence $w=v$, after which constancy contradicts (7.2).

Consequently, for every fixed $v\ne0$ and every fixed integer $w$,
$$
\left|\int_{\mathbb T^2}
e^{2\pi i[v\cdot\Psi_t(x)-w\cdot x]}\,dx\right|<1.
\tag{7.3}
$$
This proves the required strictness directly from the two marked coefficients of the prescribed symbol.

## 8. A uniform gap, and every weighted permutation branch

Choose a fixed radius $R$ so large that the first term in each bound (0.2) is at most $1/4$ whenever its label norm exceeds $R$. For sufficiently large $N$, the $C/N$ terms are also at most $1/4$. Thus all entries with $|v|_N>R$ or $|w|_N>R$ have modulus at most $1/2$.

The remaining pairs of nonzero labels form a fixed finite set. By (7.3), the maximum $\kappa$ of their limiting classical moduli is strictly below one. By (6.6), all those finitely many quantum entries have modulus at most $(1+\kappa)/2$ for sufficiently large $N$. Taking
$$
\rho_*=\max\left(\frac34,\frac{1+\kappa}{2}\right)<1
$$
proves (0.3). This assertion is for all sufficiently large odd $N$; it does not require checking the irrelevant finite set of smaller dimensions.

On the traceless matrix space the nonzero Weyl labels give an orthonormal basis. For a permutation $\pi$, $K_\pi$ has one selected entry in each row and column, so
$$
\|K_\pi\|=\max_{v\ne0}|C^E_N(\pi(v),v)|\le\rho_*.
\tag{8.1}
$$
The first estimate in (0.2) also gives
$$
\begin{aligned}
\|K_\pi\|_{\rm HS}^2
&=\sum_{v\ne0}|C^E_N(\pi(v),v)|^2\\
&\le C\sum_{v\in I_N^2\setminus\{0\}}(1+|v|)^{-2/17}+C\\
&\le C N^{2-2/17}.
\end{aligned}
\tag{8.2}
$$
The last inequality follows by centered square shells: the shell of radius $j$ has at most $8j$ labels. Dividing by $D=N^2-1$ and taking the square root proves (0.4), uniformly over all permutations.

Replacing $W_N$ by the original modular Weyl basis changes basis elements by unit signs and exchanges coordinate naming. All entry moduli, norms, and conclusions remain unchanged. Composing the kick with the exact metaplectic factor permutes input labels; the same supremum and Hilbert--Schmidt conclusions therefore hold for the adjoint action of the original $U_N$.

## 9. What this establishes

The argument proves the all-entry estimates, a fixed entrywise gap, and a decaying normalized Hilbert--Schmidt bound for every weighted permutation branch, for the exact family over all sufficiently large odd dimensions. It uses a single short-time WKB approximation only in normalized Hilbert--Schmidt norm, with all modular aliases retained.

No independence between successive branches is asserted. No bound on the unrestricted coherent sum of all histories, and no comparison with the CUE traces, is proved here. The all-time sparse-history extension may use (0.4) as an input, but $H_{\rm diag}$ remains a further assertion.
