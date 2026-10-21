> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_original_uniform_weyl_self_overlap.md`. Embedded SHA256: `7ad8afb5fa2f9098111166b70398aad2fc95bf10de508f47ae661ec25080755d`.
> [Thematic guide](../../topics/dephasing.md).

# Round 8: the exact asymptotic largest Weyl self-overlap

Date: 21 October 2026. Original-family branch.

## Status and scope

This is a new quantitative theorem for the exact matrices in the question,
with the prescribed constant $\tau=10^{-80}$, along **all odd dimensions**.
It identifies the limiting largest normalized Hilbert--Schmidt overlap of a
nonidentity Weyl operator with its one-step quantum evolution. In particular,
it excludes approximate pure-Weyl symmetries by an almost-orthogonality bound,
substantially stronger than the earlier nonexplicit bound $\rho<1$.

This is **not** a proof or refutation of $H_{\rm diag}$. No estimate for a
Heisenberg-time spectral trace sum is claimed. The quantum input reused below
is the already proved all-entry tail estimate from Round 4; the new steps are
the uniform maximum limit, the exact displacement-map interpretation, the
explicit density expansion, and the identification of its maximizing mode.

## 1. Statement

Use the original modular Weyl operators

$$
 W_v=T_N(l,k),\qquad v=(k,l)\in(\mathbb Z/N\mathbb Z)^2,
$$

and define

$$
 d_N=\max_{v\ne0}
 \left|\frac1N\operatorname{Tr}
       (W_v^*U_NW_vU_N^*)\right|.
$$

Put

$$
 t=\frac{\tau}{2\pi},\qquad
 S_f=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad
 S_c=S_f^T=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

Let $\Phi_t$ denote the time-$t$ flow of $Z=J\nabla a$, where the
ordinary-half Weyl symbol of the *actual* $A_N$ is

$$
\begin{split}
 a(q,p)={}&\cos(14\pi q)+\frac{r(q)}{10}
   +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}\\
 &+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
\end{split}                                                    \tag{1.1}
$$

The half-period shift in the last term is essential. Define the map on the
two-dimensional torus

$$
 F_t(x)=S_c\Phi_t(x)-x\pmod{\mathbb Z^2},
$$

and let $g_t$ be the density of $(F_t)_*dx$ relative to normalized
Lebesgue measure. The map is a four-sheeted smooth covering, so this density
is smooth. With the convention
$\widehat g(v)=\int_{\mathbb T^2}g(y)e^{-2\pi i v\cdot y}\,dy$, the theorem is

$$
 \boxed{\lim_{\substack{N\to\infty\\N\ \mathrm{odd}}}d_N
       =\Gamma_t
       :=\max_{v\in\mathbb Z^2\setminus\{0\}}|\widehat g_t(v)|
       =|\widehat g_t(4,-8)|.}                                  \tag{1.2}
$$

The maximizing integer modes are exactly $(4,-8)$ and $(-4,8)$. Moreover,

$$
 \boxed{\left|\Gamma_t-\frac{8\pi\sqrt{101}}{25}\tau\right|
        \le10^8\tau^2.}                                       \tag{1.3}
$$

In particular,

$$
 9\tau<\Gamma_t<11\tau.                                        \tag{1.4}
$$

In fact there is a fixed threshold $N_0$ such that, for every odd
$N\ge N_0$, the maximum defining $d_N$ is attained exactly at the two
residue classes $\pm(4,-8)$. Consequently,

$$
 d_N=\Gamma_t+O_\tau(N^{-2}).                                  \tag{1.4a}
$$

No effective bound for $N_0$ is asserted. It may be enormous because
$\tau$ is fixed and tiny.

For arbitrary phases $\zeta\in\mathbb C$, $|\zeta|=1$, this gives

$$
\begin{split}
 &\lim_{\substack{N\to\infty\\N\ \mathrm{odd}}}
 \min_{v\ne0}\min_{|\zeta|=1}
 \frac{\|U_NW_vU_N^*-\zeta W_v\|_{\rm HS}}{\sqrt N}\\
 &\hspace{35mm}=\sqrt{2-2\Gamma_t}
                >\sqrt{2-22\tau}.
\end{split}                                                    \tag{1.5}
$$

This minimizes over all $N^2-1$ nonidentity labels, including labels that
depend arbitrarily on $N$, and hence includes all powers-of-seven
subsequences and all nontrivial finite rational translations.

## 2. Previously proved quantum estimates used here

The source is
`research_round4_2026_10_21/root_all_entry_and_arbitrary_weyl_routes.md`,
Sections 2--6. Its statements are used with their proofs, not as an
assumption of universality.

The source SHA-256 is
`c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`.
The center-phase construction and its audit have SHA-256, respectively,
`a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`
and `7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce`.

For $E_N=e^{i\tau NA_N}$, set

$$
 C^E_{w,u}=N^{-1}\operatorname{Tr}(W_w^*E_NW_uE_N^*).
$$

The source proves, for the original modular quantization, uniformly over all
odd sufficiently large $N$ and all nonzero labels,

$$
 |C^E_{w,u}|
 \le C_*(1+|w|_N)^{-1/17}+C_*/N.                               \tag{2.1}
$$

Here $|w|_N$ is the Euclidean norm of the centered integer representative.
The constant is allowed to depend on the fixed $\tau$. No uniformity as
$\tau\to0$ is used.

For clarity, the proof mechanism behind the reused estimate is: an exact
finite-shift Schrödinger equation gives a center generating phase and
amplitude for $E_N$ with normalized HS error $O(N^{-1})$; the exact
Weyl trace pairing retains all half-period aliases; coefficient-extracting
differential operators applied to the known finite symbol give a finite-type
lower bound of order at most 17, even after adding an arbitrary linear
phase; oscillatory integration and an alias split give the column bound.
Applying the same construction to $-a$ gives the output-label estimate
(2.1). The underlying center-phase construction is in
`counter_one_step_pinching_hs.md` and independently checked in
`audit_one_step_pinching_hs.md`, in the same Round 4 directory. Thus (2.1)
has neither a squarefree-modulus restriction nor a restriction $7\nmid N$.

The same source, Section 6, proves the following fixed-label limit directly
from the finite Weyl commutator and Duhamel's formula. In the ordinary-half
basis $\widetilde W_v=(-1)^{kl}W_v$, for fixed integer $u,w$,

$$
 \frac1N\operatorname{Tr}
 (\widetilde W_w^*E_N\widetilde W_uE_N^*)
 \longrightarrow
 \int_{\mathbb T^2}e^{2\pi i(u\cdot\Phi_t(x)-w\cdot x)}\,dx.
                                                                  \tag{2.2}
$$

More explicitly, with $h=(2\pi N)^{-1}$ and
$f_s(x)=e^{2\pi i u\cdot\Phi_s(x)}$, the difference of the exact
commutator multiplier and the Poisson multiplier is bounded using
$|\sin z-z|\le |z|^3/6$. Summing the finite Fourier support in $a$
and the convergent weighted Fourier series in $f_s$ gives operator-norm
error $O_u(h^2)$. Duhamel then compares
$E_N\widetilde W_uE_N^*$ to $Q_N(f_t)$; all nonzero aliases in its
pairing with a fixed Weyl operator tend to zero by smooth Fourier decay.
Only fixed labels are used in this step.

## 3. Uniform maximum limit and the displacement map

Exact finite Egorov gives

$$
 M_NW_vM_N^*=W_{S_fv}.
$$

Consequently the diagonal coefficient of $\operatorname{Ad}U_N$ is
$C^E_{v,S_fv}$. Equation (2.1), using its **output** label, gives

$$
 \left|N^{-1}\operatorname{Tr}(W_v^*U_NW_vU_N^*)\right|
 \le C_*(1+|v|_N)^{-1/17}+C_*/N.                               \tag{3.1}
$$

For a fixed integer $v$, (2.2) gives the limit

$$
 \int e^{2\pi i((S_fv)\cdot\Phi_t(x)-v\cdot x)}\,dx
  =\int e^{2\pi i v\cdot F_t(x)}\,dx
  =\widehat g_t(-v).                                          \tag{3.2}
$$

There is no residual parity sign: $S_f\equiv I\pmod2$, so
$(-1)^{v_1v_2}=(-1)^{(S_fv)_1(S_fv)_2}$. Alternatively, absolute values
alone already suffice for (1.2).

Equations (3.1)--(3.2) justify the maximum limit without an Egorov estimate
for growing labels. Given $\varepsilon>0$, choose a fixed radius $R$
so that $C_*(1+R)^{-1/17}<\varepsilon$. Outside that radius (3.1) bounds
every coefficient by $\varepsilon+o(1)$. Inside the radius there are
finitely many integer labels, so (3.2) is uniform there. Hence

$$
 \limsup d_N\le
 \max\left\{\sup_{v\ne0}|\widehat g_t(v)|,\varepsilon\right\}.
$$

Conversely, each fixed label gives
$\liminf d_N\ge|\widehat g_t(v)|$. Taking the supremum, then letting
$\varepsilon\downarrow0$, proves the first equality in (1.2). The
explicit analysis below shows that the supremum is attained and positive.

The fixed-label argument (2.2) also gives an error $O_{u,w,\tau}(N^{-2})$:
its operator comparison has that error, and smooth Fourier decay bounds
the trace aliases by $O(N^{-K})$ for every fixed $K$. This rate is
only used at the eventual fixed maximizing labels.

## 4. A quantitative density expansion with an explicit remainder

All estimates in this section hold for $0<t\le10^{-12}$, and in
particular for the required value. Norms of vectors and operator norms in
this section use $\ell^\infty$.

### 4.1. Elementary symbol bounds

The definition of $r$ gives

$$
 \|r\|_\infty\le4,\quad
 \|r'\|_\infty\le32\pi,\quad
 \|r''\|_\infty\le456\pi^2.
$$

Differentiating (1.1) term by term gives

$$
\begin{array}{ll}
 \|a_q\|_\infty\le17.92\pi<60,&
 \|a_p\|_\infty\le0.08\pi<60,\\
 \|a_{qq}\|_\infty\le252.16\pi^2,&
 \|a_{qp}\|_\infty\le0.64\pi^2,\quad
 \|a_{pp}\|_\infty\le0.16\pi^2.
\end{array}
$$

In particular,

$$
 \|Z\|_\infty\le60,\qquad \|DZ\|_{\infty\to\infty}\le2600.       \tag{4.1}
$$

Also the Fourier coefficient one-norm of $a$ is at most
$1+0.4+0.04+0.1+0.04<2$, and every frequency has $|k|+|l|\le9$.
Termwise differentiation therefore gives the safe bound

$$
 \|D^2Z\|_{\infty,\infty\to\infty}\le3\cdot10^6.               \tag{4.2}
$$

For example the sharper Fourier estimate
$2(18\pi)^3<2\cdot72^3$ already lies below (4.2).

### 4.2. Flow and Jacobian bounds

Write $d_s(x)=\Phi_s(x)-x$. The integral equation for the flow and the
variational equation imply

$$
 \|d_s\|_\infty\le60s,\qquad
 \|D\Phi_s\|\le e^{2600s}\le2,\qquad
 \|D\Phi_s-I\|\le2601s.                                       \tag{4.3}
$$

For the last bound, $e^x-1\le x/(1-x)$ for $0\le x<1$, and
$s\le10^{-12}<1/(2600\cdot2601)$.

Subtracting the first-order flow and variational equations gives

$$
 \|d_t-tZ\|_\infty\le78000t^2,
 \qquad
 \|D\Phi_t-I-tDZ\|\le2\cdot10^8t^2.                          \tag{4.4}
$$

For the second inequality, the integrand after subtraction is bounded by

$$
 \|DZ(\Phi_s)-DZ(x)\|\,\|D\Phi_s\|
       +\|DZ(x)\|\,\|D\Phi_s-I\|
 \le(360000000+6762600)s.
$$

Its integral is less than $2\cdot10^8t^2$, as asserted.

Now put

$$
 B=S_c-I=\begin{pmatrix}2&4\\2&2\end{pmatrix},\quad
 R=B^{-1}S_c=\begin{pmatrix}1/2&1\\1/2&1/2\end{pmatrix},\quad
 G_t(x)=x+Y_t(x),\quad Y_t=Rd_t,\quad Y=RZ.
$$

Then $F_t=B\circ G_t$ modulo the integer lattice and $\|R\|=3/2$.
Equations (4.3)--(4.4) give

$$
 \|Y_t\|_\infty\le90t,\quad
 \|DY_t\|\le3902t,\quad
 \|DY_t-tDY\|\le3\cdot10^8t^2.                                \tag{4.5}
$$

Since $\|DY_t\|<1$, the lift $G_t=I+Y_t$ is a global
diffeomorphism: for each lifted $y$, the equation
$x=y-Y_t(x)$ has a unique solution by contraction. Periodicity of
$Y_t$ makes it a diffeomorphism of the torus. Thus $F_t$ is the
composition of this diffeomorphism with the degree-minus-four linear cover
$B$, proving the covering assertion in Section 1.

Let $D=\operatorname{div}Y$, $E_t=DY_t$, and
$J_t=\det(I+E_t)$. Here $J_t>0$. Since
$\|DY\|\le3900$, we have $|D|\le7800$. The two-dimensional identity
$\det(I+E)=1+\operatorname{tr}E+\det E$, together with (4.5), yields

$$
 |J_t-1-tD|\le6.2\cdot10^8t^2,
 \qquad |J_t-1|\le7801t<\tfrac12.                              \tag{4.6}
$$

Indeed the first error is bounded by
$(6\cdot10^8+3902^2)t^2<6.2\cdot10^8t^2$.

The density $h_t$ of $(G_t)_*dx$ is
$h_t(y)=J_t(G_t^{-1}y)^{-1}$. Writing $s=J_t-1$, the identity

$$
 \frac1{1+s}=1-s+\frac{s^2}{1+s}
$$

and (4.6) give

$$
 \left|J_t(x)^{-1}-1+tD(x)\right|
   \le7.5\cdot10^8t^2.                                      \tag{4.7}
$$

The bilinear derivative bound for $Y$ is at most $4.5\cdot10^6$,
so the Lipschitz constant of $D$, measured against $\ell^\infty$
distance, is at most $9\cdot10^6$. If $x=G_t^{-1}y$, then
$|x-y|_\infty\le90t$. Replacing $D(x)$ by $D(y)$ in (4.7)
therefore costs at most $8.1\cdot10^8t^2$. Consequently

$$
 \boxed{\|h_t-1+t\operatorname{div}(RZ)\|_\infty
                     \le3\cdot10^9t^2.}                      \tag{4.8}
$$

### 4.3. Transfer through the four-sheeted linear cover

For a torus function $h$, define

$$
 (P_Bh)(y)=\frac14\sum_{Bx=y}h(x).
$$

Change of variables on the four inverse branches shows that this is the
density transfer operator for $B$. It preserves constants, is a
contraction in the supremum norm, and satisfies

$$
 \widehat{P_Bh}(v)=\widehat h(B^Tv).                            \tag{4.9}
$$

Since $F_t=B\circ G_t$, we have $g_t=P_Bh_t$. Direct multiplication gives

$$
 RJ=\begin{pmatrix}-1&1/2\\-1/2&1/2\end{pmatrix},
 \qquad
 \operatorname{div}(RZ)=-a_{qq}+\frac12a_{pp}.
$$

Thus (4.8) proves the explicit expansion

$$
 \boxed{g_t=1+t\ell+\mathcal R_t,\qquad
 \ell=P_B(a_{qq}-a_{pp}/2),\qquad
 \|\mathcal R_t\|_\infty\le3\cdot10^9t^2.}                    \tag{4.10}
$$

No oscillatory asymptotic or numerical experiment enters this remainder.

## 5. The six surviving Fourier modes and the unique maximizing pair

The $p$-independent part of $a$ has the exact expansion

$$
\begin{split}
 V(q)={}&\frac9{10}\cos(14\pi q)+\frac1{10}\cos(2\pi q)
  -\frac1{20}\big(\cos(12\pi q)+\cos(16\pi q)\big)\\
 &+\frac1{100}\big(\sin(2\pi q)+\tfrac12\sin(4\pi q)
   +\tfrac14\sin(10\pi q)+\tfrac12\sin(12\pi q)\\
 &\hspace{36mm}-\tfrac12\sin(16\pi q)-\tfrac14\sin(18\pi q)\big).
\end{split}                                                    \tag{5.1}
$$

In particular,

$$
 a_{2,0}=-\frac{i}{400},\qquad
 a_{6,0}=-\frac1{40}-\frac{i}{400},\qquad
 a_{8,0}=-\frac1{40}+\frac{i}{400}.                             \tag{5.2}
$$

For $v=(v_1,v_2)$,

$$
 B^Tv=(2v_1+2v_2,\,4v_1+2v_2).
$$

Both coordinates are even. Since $a$ has only $p$-frequencies
$-1,0,1$, a nonzero coefficient of $\ell$ requires
$4v_1+2v_2=0$. Write $v=m(1,-2)$; its preimage frequency is
$(-2m,0)$. By (5.1), the only possibilities are

$$
 m=\pm1,\ \pm3,\ \pm4.
$$

Their coefficients are

$$
 \widehat\ell\big(m(1,-2)\big)
      =-16\pi^2m^2 a_{-2m,0}.                                 \tag{5.3}
$$

The three absolute values for positive $m$ are therefore

$$
 L_1=\frac{\pi^2}{25},\qquad
 L_3=\frac{9\pi^2\sqrt{101}}{25},\qquad
 L_4=\frac{16\pi^2\sqrt{101}}{25}.                             \tag{5.4}
$$

The gap $L_4-L_3=7\pi^2\sqrt{101}/25$ is greater than 25. By (4.10),
every Fourier coefficient of $\mathcal R_t$ has modulus at most
$3\cdot10^9t^2$. Hence the modulus at either $\pm(4,-8)$ exceeds
the modulus at every other nonzero integer mode by at least

$$
 25t-6\cdot10^9t^2>0
$$

for the stated range $0<t\le10^{-12}$. The two maximizing moduli are
equal because $g_t$ is real. This proves the second equality in (1.2),
and

$$
 |\Gamma_t-L_4t|\le3\cdot10^9t^2.                             \tag{5.5}
$$

Substitute $t=\tau/(2\pi)$. Since $\pi>3$,

$$
 L_4t=\frac{8\pi\sqrt{101}}{25}\tau,
 \qquad 3\cdot10^9t^2<10^8\tau^2,
$$

proving (1.3). The elementary inequalities
$3<\pi<22/7$ and $10<\sqrt{101}<201/20$, together with the
fixed value $\tau=10^{-80}$, imply (1.4).

To prove the eventual finite-dimensional maximizing assertion, let
$\delta>0$ be the gap between $\Gamma_t$ and the supremum over all
other nonzero classical Fourier modes; the displayed estimate gives a
strictly positive lower bound for it. Choose a fixed radius containing
$\pm(4,-8)$ such that the tail in (3.1) is less than $\Gamma_t/3$.
For all sufficiently large odd $N$, this excludes every label outside
that radius. Uniform convergence over the remaining finite set, with an
error smaller than $\delta/3$, excludes every label other than the
specified pair. Their finite-dimensional moduli agree because
$W_{-v}=W_v^*$, which implies
$C^U_{-v,-v}=\overline{C^U_{v,v}}$. The fixed-label error noted in
Section 3 now proves (1.4a).

## 6. Operator consequence and exact limitation

For unitary matrices $X,Y$ with normalized HS norms equal to one,

$$
 \min_{|\zeta|=1}\frac{\|X-\zeta Y\|_{\rm HS}^2}{N}
       =2-2\left|N^{-1}\operatorname{Tr}(Y^*X)\right|.
$$

Apply this with $X=U_NW_vU_N^*$, $Y=W_v$, then minimize in $v$.
Equations (1.2)--(1.4) prove (1.5). Thus neither a fixed Weyl translation
nor a translation whose label changes with dimension can become an
approximate projective commuting symmetry of this family in normalized HS
norm.

This conclusion concerns a single Weyl operator at one time. It does not
control a coherent combination of many Weyl operators, an arbitrary
eigenbasis-dependent symmetry, or a long product of the adjoint matrix.
In particular, the first unresolved actual-family test remains

$$
 \frac1{N^2}\sum_{1\le m<2N}
 w(m/N)\big(|\operatorname{Tr}U_N^m|^2-\min(m,N)\big)
       \longrightarrow0,                                    \tag{6.1}
$$

for the fixed admissible test $w=|\widehat b_*|^2$ specified in the
Round 7 continuation ledger. The theorem above supplies no replacement
for the cancellations in (6.1), and no infinite sequence violating
$H_{\rm diag}$ has been constructed here.

## 7. Independent algebra checks of the leading coefficient

The finite commutator gives a separate normalization check. Temporarily
write $U_N(\sigma)=e^{i\sigma NA_N}M_N$, only for this derivative
calculation, and take $v=(4,-8)$. For odd $N>18$, the relevant Fourier
frequency is unaliased:
$v-S_fv=(8,0)$. The exact Weyl product gives

$$
 \left.\frac{d}{d\sigma}
 \frac1N\operatorname{Tr}(W_v^*U_N(\sigma)W_vU_N(\sigma)^*)
 \right|_{\sigma=0}
       =-2N a_{8,0}\sin(64\pi/N).
$$

Its limit is $-128\pi a_{8,0}=(8\pi/25)(10-i)$, whose modulus is
$8\pi\sqrt{101}/25$, exactly the coefficient in (1.3). This check is
not a substitution of $\tau_N$ for the fixed parameter in the theorem.

The Laurent coefficients (5.2), the list of even nonzero frequencies, and
the rational inequalities in the density remainder were additionally
checked with exact rational arithmetic in Python. The decimal value
$8\pi\sqrt{101}/25\approx10.103236934657454$ is for interpretation
only; the proofs above use the exact expression and rational bounds.
