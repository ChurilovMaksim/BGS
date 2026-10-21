> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_quantitative_gauge_reversal_obstruction.md`. Embedded SHA256: `7cb30d1ef2cba42132c5aff08d06fd931be1175c87fd2bdc26a8b4de3a8c2c29`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Fixed-phase obstruction to approximate gauge reversal of the original unitary

21 October 2026. Author: /root/audit_uniform_word_r4.

Base checkpoint: the round-4 unified manuscript, SHA-256
e74f697134ea0d7d0ad5776c118ac267cf4999ae029e5b1f0252de364596fa4a.
The original matrices, all odd dimensions, and $\tau=10^{-80}$ are
unchanged.

This is a new raw proof submitted for independent checking. It does not
prove or refute $H_{\rm diag}$.

## 1. Question and result

The potential obstruction examined here was the following: because the
Hamiltonian has one off-diagonal hopping phase and the cat kernel is
symmetric, could a diagonal gauge, perhaps chosen on a subsequence with
$N\alpha_0$ close to a multiple of $2\pi$, give a time-reversal symmetry
of the full unitary to error $o(N^{-1})$?

The answer for this gauge class is negative, quantitatively and uniformly.
Let ${\cal K}$ denote coordinate conjugation, and let $D_N$ be any
diagonal unitary, without an algebraicity, regularity, or parameter
independence assumption. Then for every odd $N\ge10^7$ and every
$\eta\in\mathbb C$, $|\eta|=1$,

$$
 \boxed{
 \frac1{\sqrt N}
 \|D_N\overline{U_N}D_N^*-\eta U_N^*\|_{\rm HS}
 >10^{-328}.}
 \tag{1.1}
$$

The same lower bound holds for the operator norm. Thus these errors
cannot tend to zero, in particular cannot be $o(N^{-1})$, on any
subsequence. The constant is deliberately very conservative.

The proof is an exact finite-dimensional commutator calculation. It
does not infer a fixed-time quantum identity from a classical limit,
and it does not use a quantitative transcendence theorem.

## 2. The apparent magnetic flux is cut in the exact finite matrix

Write $h_N=(N+1)/2$ for the modular inverse of two, and
$\gamma=e^{-i\alpha_0}/200=(-3-4i)/1000$. The original modular
quantization gives, for all odd $N\ge3$,

$$
 (A_N)_{x,x+1}
 =\gamma\,r((x+h_N)/N).
 \tag{2.1}
$$

The diagonal entries are real; the opposite hopping is the conjugate.
This follows by summing the $l=1$ Fourier terms before reducing their
integer $k$-frequencies. Formula (2.1) is consequently valid even if
those frequencies alias.

The nonnegative $r(q)$ vanishes exactly when $7q$ is an integer or
$q=1/2$ modulo one. The second case never occurs on an odd grid.
The number of cut hopping edges is therefore
$d=\gcd(7,N)$, either one or seven. The cuts are equally spaced and
leave $d$ paths, each with $n=N/d$ vertices. In particular there is
always a cut at $x=-h_N$; there is no unbroken magnetic cycle.

On each oriented path choose diagonal entries of a gauge $G$ by
$G_{x+1}=e^{i\alpha_0}G_x$ along its nonzero edges. Then $G^*A_NG$
is real symmetric with nonnegative hoppings. The antiunitary
$G{\cal K}G^*=D{\cal K}$, $D=G^2$, preserves $A_N$ exactly.

However, it fails to reverse the cat matrix by an amount of order one.
Symmetry and unitarity give $\overline M_N=M_N^*$, and the flat
nonzero entries give the exact formula

$$
 \frac1N\|D\overline M_ND^*-M_N^*\|_{\rm HS}^2
 =\frac1{N^2}\sum_{x,y}|D_x\overline{D_y}-1|^2
 =2-2\left|\frac{\operatorname{Tr}D}{N}\right|^2.
 \tag{2.2}
$$

For arbitrary starting phases on the paths,

$$
 |\operatorname{Tr}D|
 \le d\left|\sum_{j=0}^{n-1}e^{2ij\alpha_0}\right|
 \le\frac{2d}{|1-e^{2i\alpha_0}|}
 =\frac{5d}{4}\le\frac{35}{4}.
 \tag{2.3}
$$

Here $|1-e^{2i\alpha_0}|=2|\sin\alpha_0|=8/5$.
Thus the defect in (2.2) tends to $\sqrt2$ in normalized HS norm,
regardless of rational approximations to $N\alpha_0$. If $N\alpha_0$
is nearly integral in units of $\pi$, the numerator of the geometric
sum is small, which does not make this cat defect small.

This argument alone concerns a common reversal of the two factors.
The following calculation treats approximate reversal of their full
product directly.

## 3. Exact ordinary-half representation and a trace discriminator

For integer labels define

$$
 W_N(k,l)\psi(x)
 =e^{2\pi i k(x+l/2)/N}\psi(x+l),\qquad
 W_N(k,l)=(-1)^{kl}T_N(l,k).
$$

The latter identity retains the original modular-half convention. Put

$$
 R(q)=r(q+1/2)
 =(1+\cos14\pi q)(1-\cos2\pi q).
$$

Then $A_N=Q_N(a)$, where $Q_N(e^{2\pi i(kq+lp)})=W_N(k,l)$ and

$$
 a(q,p)=V(q)+\gamma R(q)e^{2\pi ip}
                  +\overline\gamma R(q)e^{-2\pi ip},
$$

$$
 V(q)=\cos14\pi q+r(q)/10+r(q)\sin2\pi q/100-1/10.
 \tag{3.1}
$$

The support satisfies $|k|\le9,\ |l|\le1$, and the sum of absolute
Fourier coefficients is at most $59/50<2$. For example the first
three non-sine terms in $V$ reduce to
$.9\cos14\pi q+.1\cos2\pi q-.1\cos14\pi q\cos2\pi q$,
of coefficient mass $1.1$. The remaining sine term has mass at most
$.04$, as do the two mixed rows together.

The exact multiplication and cat transport are

$$
 W_uW_v=e^{\pi i\omega(u,v)/N}W_{u+v},
 \quad\omega(u,v)=u_2v_1-u_1v_2,\qquad
 M_NW_vM_N^*=W_{Sv},
 \quad S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
 \tag{3.2}
$$

These formulas follow by multiplication of the given kernels and
character orthogonality. The passage from modular to ordinary halves
has no extra cat sign because
$(3k+2l)(4k+3l)-kl$ is even.

Let $h=(2\pi N)^{-1}$, $t=\tau/(2\pi)$,
$E_N(s)=e^{isA_N/h}$, and $W=W_N(1,0)$, a diagonal unitary.
The trace discriminator for the full product is

$$
 F_N(t)=\frac1N\operatorname{Tr}(W^*U_NWU_N^*)
 =\frac1N\operatorname{Tr}
       (W^*E_N(t)W_N(3,4)E_N(t)^*).
 \tag{3.3}
$$

We prove a positive uniform lower bound for its imaginary part.

## 4. Uniform finite Taylor remainder

Define ${\cal L}_N X=(i/h)[A_N,X]$. Formula (3.2) gives

$$
 {\cal L}_NW_v
 =-4\pi N\sum_u a_u
       \sin\!\left(\frac{\pi\omega(u,v)}N\right)W_{u+v}.
 \tag{4.1}
$$

Since $|N\sin(\pi b/N)|\le\pi|b|$, every coefficient is bounded by
$4\pi^2|a_u||\omega(u,v)|$, independently of $N$.

After $j$ brackets starting at $(3,4)$, the unreduced integer label
satisfies $|v_1|\le3+9j,\ |v_2|\le4+j$. For the next bracket,

$$
 |\omega(u,v)|\le39+18j\le111,\qquad 0\le j\le4.
$$

Using coefficient mass less than two and $\pi<4$, each of these
five steps multiplies the coefficient mass by less than
$128\cdot111=14208$. All $W_v$ are unitary even before reducing
their labels, so aliasing can only decrease the triangle bound:

$$
 \|{\cal L}_N^5W_N(3,4)\|
 \le14208^5<10^{21}.
 \tag{4.2}
$$

Taylor's formula with the integral remainder is exact:

$$
 e^{t{\cal L}_N}X
 =\sum_{j=0}^4\frac{t^j}{j!}{\cal L}_N^jX
 +\frac1{4!}\int_0^t(t-s)^4
        e^{s{\cal L}_N}{\cal L}_N^5X\,ds.
$$

For real $s$, $e^{s{\cal L}_N}$ is unitary conjugation and is an
operator-norm isometry. Thus no exponential of $\|A_N/h\|$ enters
the estimate. The remainder in (3.3) has absolute value at most

$$
 10^{21}t^5.
 \tag{4.3}
$$

## 5. The first nonzero coefficient

For $N\ge35$, the coefficients of $t^j$, $0\le j<4$, in (3.3)
vanish exactly. Indeed the initial shift label is four, and each bracket
changes it by at most one, so it cannot be zero modulo $N$ at those
orders. At order four, returning to shift zero requires all four
insertions to have $l=-1$.

Such insertions have $|k|\le8$. Their final modulation label lies
between $-29$ and $35$. Its difference from the target label one
lies between $-30$ and $34$, so there is also no nonzero modulation
alias for $N\ge35$.

For each four-step history let $K_0=3$, $L_j=4-j$,
$K_{j+1}=K_j+k_j$, and put

$$
 s_N(b)=\frac N\pi\sin(\pi b/N).
$$

The order-four coefficient before multiplication by $t^4/4!$ is

$$
 (4\pi^2)^4\overline\gamma^{\,4}\,C_N,\qquad
 C_N=\sum_{k_0+\cdots+k_3=-2}
           \prod_{j=0}^3R_{k_j}s_N(K_j+k_jL_j).
 \tag{5.1}
$$

All $C_N$ are real. Each $|K_j+k_jL_j|\le35$, and
$\sum_k|R_k|=4$.

We evaluate the limit coefficient by hand. Write
${\cal D}=(2\pi i)^{-1}\partial_q$ and
$B_L=R{\cal D}+L({\cal D}R)$. The ordered four insertions, with the
common factors $4\pi^2\overline\gamma$ suppressed, are
$B_1B_2B_3B_4e^{6\pi iq}$.
The differential identity

$$
 B_1B_2\cdots B_j={\cal D}^{\,j}R^j
 \tag{5.2}
$$

holds without dividing by $R$. To prove it, use
$B_1={\cal D}R$, and, at the induction step, the product rule

$$
 R^j\bigl(R{\cal D}+(j+1){\cal D}R\bigr)
 ={\cal D}R^{j+1}.
$$

Thus the target Fourier coefficient is

$$
 C_\infty=(R^4)_{-2}
 =\left\langle(1+\cos14\pi q)^4\right\rangle
       \bigl((1-\cos2\pi q)^4\bigr)_{-2}
 =\frac{35}{8}\frac74=\frac{245}{32}.
 \tag{5.3}
$$

The factorization of this coefficient is exact because the second
factor has frequencies of absolute value at most four; no nonzero
multiple of seven can contribute to frequency $-2$.

For a quantitative finite-$N$ estimate,

$$
 |s_N(b)-b|\le\frac{\pi^2|b|^3}{6N^2},\qquad |s_N(b)|\le|b|.
$$

Telescoping the product of four real factors in (5.1) therefore gives

$$
 |C_N-245/32|
 \le\frac{2\pi^2\,35^2}{3N^2}\,140^4
 <\frac{10^{13}}{N^2}.
 \tag{5.4}
$$

For every $N\ge10^7$, this is less than or equal to $1/10$,
and hence $C_N>7$.

## 6. Positive imaginary part and the gauge distance

The fixed phase gives

$$
 \overline\gamma^{\,4}=\frac{-527+336i}{10^{12}}.
$$

Consequently (4.3) and (5.1) imply

$$
 \operatorname{Im}F_N(t)
 =\frac{(4\pi^2)^4}{24}\frac{336}{10^{12}}C_Nt^4
       +\epsilon_N(t),\qquad
 |\epsilon_N(t)|\le10^{21}t^5.
 \tag{6.1}
$$

The leading classical coefficient is exactly
$343\pi^8/12500000000$. More conservatively, $\pi>3$ and $C_N>7$
give a coefficient greater than $10^{-4}$, since

$$
 \frac{7\cdot36^4\cdot336}{24\cdot10^{12}}
 =\frac{321489}{1953125000}>10^{-4}.
$$

Our $0<t<10^{-80}$ therefore satisfies

$$
 \operatorname{Im}F_N(t)>
 \frac{t^4}{20000}>
 \frac{\tau^4}{20000\cdot8^4}>
 10^{-328},
 \qquad N\ge10^7.
 \tag{6.2}
$$

For any unitary matrix $U$, any diagonal unitary $D$, and any unit
scalar $\zeta$, put $V=\zeta D U^TD^*$. Because $D$ commutes with
the diagonal $W$, entrywise expansion gives

$$
 F(V)=\overline{F(U)},\qquad
 F(U)=N^{-1}\sum_{x,y}
            \overline{W_x}W_y|U_{xy}|^2.
$$

Telescoping the two occurrences of $U$ in $F$, with normalized HS
Cauchy--Schwarz, gives

$$
 |F(U)-F(V)|\le
 2N^{-1/2}\|U-V\|_{\rm HS}.
$$

It follows that

$$
 N^{-1/2}\|U-\zeta DU^TD^*\|_{\rm HS}
 \ge|\operatorname{Im}F(U)|.
 \tag{6.3}
$$

Conjugating the difference in (1.1) and multiplying by diagonal unitaries
identifies its norm with the left side of (6.3), with
$\zeta=\overline\eta$. Equations (6.2)--(6.3) prove (1.1).
Since normalized HS norm is at most operator norm, the operator-norm
claim follows too.

## 7. Meaning of the fixed phase and boundaries of the result

The surviving coefficient depends on the fixed value
$\operatorname{Im}e^{4i\alpha_0}$, not on $e^{iN\alpha_0}$.
The number four comes from the exact cat transport
$(1,0)\mapsto(3,4)$ and the four unit-shift brackets required to return
to the diagonal subspace. This explains why approximating $N\alpha_0$
cannot remove the obstruction.

The excluded antiunitaries are exactly the coordinate-diagonal gauge
class $D_N{\cal K}$, with arbitrary phases, including the gauges
realizing the Jacobi paths. The result does not exclude arbitrary
antiunitaries constructed from the eigenvectors of $U_N$; those exist
for every finite unitary and have no automatic physical meaning.
It also does not by itself exclude all approximate monomial,
Fourier-integral, or nonlocal reversers.

The nearest prior results were read to avoid duplicating an already
settled exact-symmetry question:

| Prior source | SHA-256 |
|---|---|
| arithmetic_banded_time_reversal.md | 39d017750473ee6779fc52656613b06dee5cd5591e4dbd288c64c10904cae6dd |
| arithmetic_monomial_reversal_closure.md | 38462ab5c59f850c507b578b9b63092c452e427b48cdf3812a863434bb3a72f9 |
| arithmetic_seven_chain_cut_stability.md | d6ddc0695d91441729852ea5fc89d6318a1297b22eb4837cd5d3e0c930c3d349 |

The first gives a common-factor obstruction, and the second an exact
full-product monomial exclusion by algebraic exponential-polynomial
rigidity. The present new step is a quantitative approximate obstruction
for the full product, with a uniform finite-$N$ commutator remainder.

The route toward a wrong symmetry class through this diagonal flux
mechanism is ruled out. The original signed pair-trace statistic on
times of order $N$, and all higher orders of $H_{\rm diag}$, remain
unevaluated.
