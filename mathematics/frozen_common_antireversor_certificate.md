# Exact obstruction to a common antiunitary reversor

**Claim ID:** `BGS-FM-009`. **Status:** exact finite polynomial certificate
with an author-level audit of the deduction, adapted from Section 4 and
Appendix B of the submitted 24 September 2026 PDF (SHA-256
`aeb0f82d35b3d40eb2e9a3fded9417c55df95e393f3de148f01457ecad844454`).
The coefficient enumeration and every cyclotomic test are performed in
integer arithmetic by the maintained verifier. This is a certificate-backed
project proof, not a formal-kernel verification or an external referee.

## Exact statement

For the original, unmodified matrices $A_N,M_N$ of
[`fixed_model_symmetry_theorem.md`](fixed_model_symmetry_theorem.md),

$$
\operatorname{Tr}[A_N,M_N]^3\ne0
\quad\text{for all odd }N\ge3\text{ except }N=7.       \tag{1}
$$

Consequently no antiunitary $R$ (with *arbitrary*, potentially
transcendental matrix entries) satisfies **both**
$RA_NR^{-1}=A_N$ and $RM_NR^{-1}=M_N^{-1}$ at those $N$.
At $N=7$, $A_7=\tfrac9{10}I$ and coordinatewise conjugation $K$
is such a common reversor. For odd $N\ne7$, there is also no
antiunitary $J=QK$ with **algebraic** entries $Q$ satisfying
$JU_NJ^{-1}=U_N^{-1}$ at the fixed $\tau=10^{-80}$.

The algebraic-entry restriction on the *last* assertion is essential:
every finite-dimensional unitary operator has an antiunitary reversor
constructed in its own eigenbasis. No false absence claim is made for
arbitrary antiunitaries reversing $U_N$ alone. The nonzero number (1)
has no lower bound uniform in $N$ here, and does not control spectral
spacing.

## Necessary trace obstruction

$M_N$ is a symmetric unitary and $A_N$ is Hermitian. Write any
antiunitary as $R=QK$, where $K$ is conjugation in the standard basis.
If $RMR^{-1}=M^{-1}$, then $Q\overline M Q^{-1}=M^{-1}$;
$\overline M=M^{-1}$ by symmetry, so $QM=MQ$. If also
$RAR^{-1}=A$, then $QA^{\mathsf T}Q^{-1}=A$.
Since $[A^{\mathsf T},M]=-[A,M]^{\mathsf T}$,
$[A,M]$ is similar to $-[A,M]^{\mathsf T}$. Taking its third
trace forces $\operatorname{Tr}[A,M]^3=0$.

## Explicit finite Laurent polynomials

For $v=(a,b)$ let $T_N(v)$ denote the raw modular Weyl operator.
Write the **actual** raw kick as
$A_N=\sum_{v\in\mathcal S}c_vT_N(v)$ with its 32 nonzero
Fourier coefficients, and $d_v=4000c_v\in\mathbb Z[i]$.
These coefficients are generated independently of any floating-point
matrix by [`frozen_antireversor.py`](../computations/verification/frozen_antireversor.py).
Use $\omega(v,w)=v_1w_2-v_2w_1$, $S=\left(\begin{smallmatrix}3&4\\
2&3\end{smallmatrix}\right)$, $t=v+w=(a,b)$,
$u=(c,d)$, and $Q_0(a,b)=5(2b^2-a^2)$. Put

$$
E_\pm(v,w,u)=Q_0(t)+Q_0(u)+14\omega(v,w)
-2ac+4bd\ \pm\ 2\omega(t,u).                        \tag{2}
$$

The Weyl product and $M_NT_N(v)M_N^{-1}=T_N(Sv)$ also give
$E_+=14\omega(v,w)+14\omega(t,Su)+Q_0(t+Su)$,
$E_-=14\omega(v,w)+14\omega(t,S^2u)+Q_0(t+S^2u)$.
Therefore, whenever the indicator below is nonzero, its displayed
exponent is an integer:

$$
\begin{aligned}
P(z)&=\sum_{v,w,u\in\mathcal S}d_vd_wd_u
       \bigl(z^{E_-}-z^{E_+}\bigr),\\
P_7(z)&=\sum_{v,w,u\in\mathcal S}d_vd_wd_u
\bigl(\mathbf1_{t+S^2u\in7\mathbb Z^2}z^{E_-/7}
 -\mathbf1_{t+Su\in7\mathbb Z^2}z^{E_+/7}\bigr). \tag{3}
\end{aligned}
$$

These are **real integer Laurent polynomials** by pairing
$(v,w,u)$ with $(-v,-w,-u)$. Expanding the eight terms in the cube,
cyclically identifying traces, using $M_N^3$ and the Weyl product
gives the finite identity

$$
\operatorname{Tr}[A_N,M_N]^3=
\frac{3\operatorname{Tr}M_N^3}{4000^3}
\begin{cases}
P(e_N(28^{-1})),&7\nmid N,\\
P_7(e_N(4^{-1})),&7\mid N.
\end{cases}                                         \tag{4}
$$

Here $|\operatorname{Tr}M_N^3|=\gcd(N,7)>0$, since exact
metaplectic conjugation gives
$|\operatorname{Tr}M_N^3|^2=|\ker(S^3-I\bmod N)|$
and $S^3-I=14\left(\begin{smallmatrix}7&10\\5&7\end{smallmatrix}\right)$
with determinant of the latter integer matrix $-1$.

The phase in (4) follows from the character of the metaplectic
representation: for $7\nmid N$, $I-S^3$ is invertible modulo $N$
and
$\operatorname{Tr}(T_N(a,b)M_N^3)
=\operatorname{Tr}(M_N^3)e_N(5(2b^2-a^2)28^{-1})$.
When $7\mid N$ this trace vanishes unless both $a,b$ are divisible
by $7$; in the latter case it equals
$\operatorname{Tr}(M_N^3)e_N(35(2(b/7)^2-(a/7)^2)4^{-1})$.
These two formulas can alternatively be verified by conjugating
$M_N^3$ by $T_N(w)$ and solving $(I-S^3)w=v$. There is no division
by 7 in the $7\mid N$ case.

## Complete root-of-unity exclusion

The exact enumeration gives $P$ with 2225 nonzero terms and exponents
$-238,\ldots,4211$; $P_7$ has 120 terms and exponents
$-18,\ldots,527$. Their integer contents both equal 160. Hence

$$
Q=z^{238}P/160\in\mathbb Z[z],\quad \deg Q=4449;
\qquad Q_7=z^{18}P_7/160\in\mathbb Z[z],\quad \deg Q_7=545.
$$

If a primitive odd-order root of unity of order $n$ were a zero,
$\Phi_n$ would divide the corresponding $Q$ over $\mathbb Z$, and
so also after reduction modulo 2. Since for odd $n$ one has
$\varphi(n)^2\ge n$, the bound $\varphi(n)\le\deg Q$ gives
finite $n$. Bounding $n/\varphi(n)$ by the product over its at most
seven (respectively six) smallest possible odd prime factors sharpens
these ranges to $n\le13006$ and $n\le1509$.

The verifier constructs $\Phi_n\bmod2$ recursively and divides in
$\mathbb F_2[z]$ for **all** 2415 odd eligible orders with $7\nmid n$
and **all** 57 eligible orders with $7\mid n$. Only $n=1,3$
survive the first necessary test, and only $n=7$ the second.
Order $1$ is outside $N\ge3$. For order $3$ the exact integer
remainder is

$$
Q(z)\bmod(z^2+z+1)=-51462z\ne0.              \tag{5}
$$

Thus (4) proves (1) for all specified $N$; $n=7$ is the explicit
exception. The certificate and complete polynomial coefficient tables
are in [`evidence/20260924/antireversor`](../evidence/20260924/antireversor).
Finite screening alone would not cover all odd $N$ without the proved
totient bounds and the equivalence of a cyclotomic factor with
root-of-unity vanishing.

For the algebraic-entry corollary, a putative $J=QK$ with
$JU_NJ^{-1}=U_N^{-1}$ gives an equality of finite exponential
polynomials in the nonzero algebraic time $t=\tau N$. The distinct
algebraic exponents are linearly independent over algebraic numbers by
[Lindemann–Weierstrass, Popescu Theorem 3.2](https://arxiv.org/pdf/2306.14352).
The equality therefore holds as an analytic identity in $t$.
Evaluation and differentiation at $t=0$ yield
$JM_NJ^{-1}=M_N^{-1}$ and $JA_NJ^{-1}=M_N^{-1}A_NM_N$.
Then $R=M_NJ$ would be the forbidden common reversor.

The polynomial identities, excluded orders, and conclusion's exact
scope are independently recorded in
[`record/frozen_antireversor_review_20260924.md`](../archive/record/frozen_antireversor_review_20260924.md).
