> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round14_2026_10_21/structural/r14_quartic_return_addendum.md`. Embedded SHA256: `4128be1d1670f64159f2b94d9303777408580c32d550f40c7862dd6d01be0ea1`.
> [Thematic guide](../../../topics/classical_trace.md).

# Exact first nonzero coefficient of the one-step coordinate return

21 October 2026. Addendum to
`r14_original_coordinate_phase_bridge_test.md`, frozen SHA-256
`4bc02ec2a3565f34c33a830db584cf761e62e5b69c23c7a727ab124046ca583a`.

Editorial provenance: the main note was first reviewed under SHA-256 `7b6657c8e1ca2ee91391509c2c97b9054715681a0afa2cedff94f8dd4c4ecc3f`; one accidental carriage-return byte in a TeX command was then replaced by the literal backslash-r, with no mathematical change. The exact byte patch and both hashes are retained in `main_cr_editorial_patch.json`. The hash above is the corrected source.

This strengthens its Theorem A. It is a fixed-time original-family result, not a proof or disproof of `H_diag`.

## 1. Statement with an explicit analytic remainder

For the exact original matrices through all odd dimensions,

$$
\boxed{
\lim_{N\to\infty,\ N\ {\rm odd}}
\sum_x|U_N(x,x)|^2
=1-\frac{25823\pi^4}{4800000000000}\tau^4+E,
\qquad |E|\le10^{56}\tau^5.}
\tag{1.1}
$$

In particular the limit is strictly less than $1-10^{-7}\tau^4$. The parameter is the fixed prescribed $\tau=10^{-80}$; the remainder estimate is evaluated at that parameter. No sequence $\tau_N$ is introduced.

The main note already proves that the limit equals $\int_0^1k_{t_*}(q,q)dq$, including the finite-grid Gauss phases, discrete aliases and exact-matrix comparison. It also proves vanishing of the first three Taylor coefficients. What remains here is a completely explicit calculation of the fourth coefficient and a fifth-order Cauchy remainder.

## 2. Highest momentum mode and a differential identity

Set $\kappa=2\pi$, $\lambda=i\kappa$, and

$$
u(Q)=\frac{-3-4i}{1000}R(Q),\qquad R(Q)=r(Q+1/2).
$$

The coefficient of $e^{\lambda p}$ in the corrected symbol $a$ is exactly $u$: the cosine contributes $e^{-i\alpha_0}/200=(-3-4i)/1000$. In the coordinates of the main note,

$$
\partial_t\mathcal G=a(Q,p+D\mathcal G),\qquad
D=\partial_Q-\tfrac34\partial_p,\qquad
\mathcal G=\sum_{n\ge1}t^n\mathcal G_n.
$$

Write $g_n(Q)$ for the coefficient of $e^{n\lambda p}$ in $\mathcal G_n$, and put

$$
D_n=\partial_Q-\tfrac34n\lambda.
$$

At time order $n$, the momentum Fourier degree is at most $n$. To attain its highest positive degree, every participating coefficient must attain its own highest positive degree. Thus neither the momentum-independent term $V$ nor the negative momentum mode contributes to $g_n$. The recursion is obtained from

$$
u e^{\lambda p}\exp\!\left(\lambda\sum_{j\ge1}
t^j(D_jg_j)e^{j\lambda p}\right)
$$

by selecting time degree $n-1$ and momentum degree $n$. This gives, explicitly,

$$
\begin{aligned}
g_1&=u,\\
2g_2&=u\lambda D_1u,\\
3g_3&=u\left(\lambda D_2g_2+
\tfrac12\lambda^2(D_1u)^2\right),\\
4g_4&=u\left(\lambda D_3g_3+
\lambda^2(D_1u)(D_2g_2)+
\tfrac16\lambda^3(D_1u)^3\right).
\end{aligned}
\tag{2.1}
$$

The operators obey the graded product identity
$D_{r+s}(fg)=(D_rf)g+f(D_sg)$ when $f,g$ have momentum degrees $r,s$. With $d=D_1u$, $e=D_1^2u$, $f=D_1^3u$, the recursion yields

$$
g_2=\frac\lambda2ud,\qquad
g_3=\frac{\lambda^2}{6}(u^2e+2ud^2),
$$
$$
g_4=\frac{\lambda^3}{24}(u^3f+9u^2de+6ud^3).
$$

Differentiating $u^4$ three times with $D_4$ gives

$$
D_4^3(u^4)=4u^3f+36u^2de+24ud^3.
$$

Therefore the required compact identity is

$$
\boxed{g_4=\frac{\lambda^3}{96}D_4^3(u^4).}
\tag{2.2}
$$

This identity is a direct algebraic consequence of (2.1); no symbolic-computation output is needed as a premise.

## 3. The finite Fourier coefficient by hand

Use $z=e^{\lambda Q}$. The real Laurent polynomial is

$$
R=1-\frac{z+z^{-1}}2+\frac{z^7+z^{-7}}2
-\frac{z^8+z^6+z^{-6}+z^{-8}}4.
\tag{3.1}
$$

On the Fourier mode $z^k$, $D_4$ acts as multiplication by $\lambda(k-3)$. For $k=2$, equation (2.2), together with $\lambda^6=-\kappa^6$, thus gives

$$
\frac{[z^2]g_4}{\kappa^6}=\frac{[z^2]u^4}{96}.
\tag{3.2}
$$

Here is a finite hand-check of $[z^2]R^4$. Let $a_j=[z^j]R^2$, with $a_{-j}=a_j$. Squaring (3.1) gives the following complete nonzero table for $j\ge0$; all omitted entries vanish.

| $j$ | 0 | 1 | 2 | 5 | 6 | 7 | 8 | 9 | 12 | 13 | 14 | 15 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $a_j$ | $9/4$ | $-3/2$ | $3/8$ | $1/4$ | $-1$ | $3/2$ | $-1$ | $1/4$ | $1/16$ | $-1/4$ | $3/8$ | $-1/4$ | $1/16$ |

The table can also be obtained immediately by multiplying
$(1-\cos\kappa Q)^2$ and $(1+\cos7\kappa Q)^2$, using $\cos^2 x=(1+\cos2x)/2$. The coefficient needed in the square of $R^2$ is

$$
\begin{aligned}
[z^2]R^4
&=a_1^2+2\sum_{j\ge0}a_ja_{j+2}\\
&=\frac94+2\left(\frac{27}{32}+\frac38+1+\frac38
+\frac3{128}+\frac1{16}+\frac3{128}\right)\\
&=\frac94+2\cdot\frac{173}{64}=\frac{245}{32}.
\end{aligned}
\tag{3.3}
$$

Since $(-3-4i)^4=-527-336i$, (3.2)–(3.3) imply

$$
\frac{[z^2]g_4}{\kappa^6}
=\frac{245(-527-336i)}{3072\cdot10^{12}}
=-\frac{25823}{614400000000000}
-\frac{343i}{12800000000000}.
\tag{3.4}
$$

The independent `Fraction` calculation in `check_quartic_coefficient.py` verifies (3.3)–(3.4), but (3.1)–(3.3) are the complete finite proof.

## 4. Diagonal differentiation and the real return coefficient

At time order four the four-sheet sum retains only momentum degrees $0,4,-4$. The degree zero term is killed by $\partial_s$. The positive degree-four term in the sum of phase corrections is

$$
4g_4(Q)e^{\lambda(s-3Q)}.
$$

Applying $\partial_Q\partial_s$ at fixed endpoints and then setting $Q=s=q$ gives

$$
4\lambda\bigl(g'_4(q)-3\lambda g_4(q)\bigr)e^{-2\lambda q}.
$$

Integration over $q\in[0,1]$ selects Fourier index two. Its value is
$4\lambda(2\lambda-3\lambda)[z^2]g_4=4\kappa^2[z^2]g_4$.
The negative momentum term is its complex conjugate, because the Hamilton–Jacobi phase is real for real inputs. Thus the full time-four coefficient of the diagonal integral is

$$
8\kappa^2\Re([z^2]g_4)
=-\frac{25823\kappa^8}{76800000000000}.
\tag{4.1}
$$

Finally $t_*^4=\tau^4/\kappa^4$, and $\kappa^4=16\pi^4$. This converts (4.1) exactly to the fourth-order term in (1.1).

## 5. Fifth-order remainder and strict sign

Use the same genuine holomorphic phase and strip constants as in Sections 1 and 4 of the main note: $T=10^{-12}$,
$\|G_n\|_{S_{.003}}\le10T^{1-n}$.
For $|t|\le T/2$,

$$
\left\|G(t)-\sum_{n=1}^4t^nG_n\right\|_{S_{.003}}
\le\frac{20|t|^5}{T^4}=2\cdot10^{49}|t|^5.
$$

The mixed endpoint derivative across strip gap .001 costs $10^6$, and the four sheet translates cost four. The uniform kernel remainder is at most $8\cdot10^{55}|t|^5$; integrating along a unit interval does not enlarge it. At $t=t_*<\tau$, it is bounded by $10^{56}\tau^5$, as in (1.1).

The positive coefficient
$a_4=25823\pi^4/4800000000000$ exceeds $4\cdot10^{-7}$, already using $\pi>3$. The remainder divided by $\tau^4$ is at most $10^{56}\tau=10^{-24}$. Hence

$$
\lim_N\sum_x|U_N(x,x)|^2
\le1-(a_4-10^{-24})\tau^4
<1-10^{-7}\tau^4.
$$

This is a strict statement at the fixed original parameter. It does not require resolving an exponentially small numerical difference on a computer.

## 6. What this adds to the original target

It shows that the limiting diagonal coordinate return is not exactly one, and identifies its first departure from the unperturbed metaplectic return with a certified sign and remainder. Combined with the already proved original one-step trace formula, it strengthens the explicit discrepancy between the allowed common phase and independent coordinate phases.

It leaves unchanged the missing long-time signed trace estimate displayed as (8.2) in the main note. A fixed-time discrepancy contributes only $O(N^{-2})$ to that pair criterion. No assertion of full sine-process convergence, a fixed-test countersequence, or literature priority follows from this addendum.
