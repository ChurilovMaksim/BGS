> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_continuation_2026_10_20/audit_simplicity.md`. Embedded SHA256: `c09cc06df2b1c6d74a008e166d00bcb0c644c2ce3256faa9b4c59c78d4ce506d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/algebra.md).

# Independent audit: spectral simplicity on powers of 3 and 5

Date: 20 October 2026.

Reviewed author file: exact_spectral_simplicity.md, final SHA-256
4aef0bf28965da0c359c01dff6e3bd330dd0cafdeb79118a5e84bd359d1ac2eb.
This version includes the $m\ge1$ clarification and the composite bound (3.12).

## Verdict

**The claimed theorem is correct:** for every $k\ge1$, and
$$
 N=3^k\quad\text{or}\quad N=5^k,
$$
the original $M_N$ has simple spectrum. Consequently the original family
$$
 U_N(z)=e^{izNA_N}M_N
$$
has simple spectrum for every algebraic $z$, including $z=0$ and the specified
$$
 \tau=10^{-80}.
$$
For nonreal algebraic $z$, this is a statement about distinct eigenvalues of the generally nonunitary matrix; the original target uses real $\tau$.

The stronger bare-cat classification is also correct. For any odd $N\ge3$, $M_N$ is simple if and only if
$$
 N=p^a,\qquad r_p:=\operatorname{ord}_p(S)=p+1,\qquad
 a=1\ \text{or}\ s_p=1,
$$
where $S^{r_p}=t_{r_p}I+u_{r_p}J$, $J^2=2I$, and $s_p=v_p(u_{r_p})$. Section 7 proves the necessity, sufficiency, and the obstruction at dimensions with two distinct prime factors. The discriminant argument consequently proves simplicity of the actual $U_N(z)$ at every algebraic parameter in every dimension satisfying this criterion.

This review starts from the exact matrix definitions. The prime-power lift, every fixed-point count in a complete period, the Fourier-multiplicity normalization, the CRT twists, and the discriminant specialization were checked independently. The theorem does not follow merely from simple spectrum of $A_N$; that implication is not used.

The classification is complete for $M_N$, and is a sufficient criterion for $U_N(z)$. Degeneracy of the bare matrix does not prove degeneracy of its kicked version. Universal simplicity of $U_N(\tau)$, microscopic pair statistics, and Hdiag are not obtained.

## 1. Exact Egorov and the trace-square identity

For odd $N$, use
$$
 (T_N(a,b)u)(x)
 =e_N[b(x+\overline2a)]u(x+a),
$$
$$
 (M_N)_{xy}
 =N^{-1/2}e_N[-\overline8(3x^2-2xy+3y^2)].
$$
The plus shift is essential. All fractions here are modular fractions.

The matrix $M_N$ is unitary: the inner product of rows reduces to a complete additive-character sum, with the coefficient of the summation index proportional to $x-x'$, and $4$ invertible modulo $N$.

The exact Egorov identity is
$$
 M_NT_N(a,b)M_N^{-1}
 =T_N(3a+4b,2a+3b),
 \qquad
 S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
 \tag{1.1}
$$
There is no residual phase in (1.1). One direct check compares both products to $M_{xw}$. In $M T_N(a,b)$, the relative exponent is
$$
 -\frac a4x+\left(\frac{3a}{4}+b\right)w
 -\frac{3a^2}{8}-\frac{ab}{2}.
$$
For $T_N(A,B)M$, it is
$$
 \left(B-\frac{3A}{4}\right)x+\frac A4w
 -\frac{3A^2}{8}+\frac{BA}{2}.
$$
The expressions agree at $A=3a+4b,\ B=2a+3b$, because $4B-3A=-a$.

The $N^2$ Weyl matrices form a basis of the matrix algebra. Their trace orthogonality follows from the shift and the complete character sum, and remains valid at composite odd $N$.

On that basis, the superoperator $\operatorname{Ad}(M_N^m)$ is the permutation induced by $S^m$. Its trace is therefore the number of fixed Weyl labels. On the other hand, its trace is $\operatorname{Tr}(M_N^m)\operatorname{Tr}(M_N^{-m})$. Hence
$$
 |\operatorname{Tr}M_N^m|^2
 =\#\ker(S^m-I:\,(\mathbb Z/N\mathbb Z)^2
                     \longrightarrow(\mathbb Z/N\mathbb Z)^2).
 \tag{1.2}
$$
This exact identity is the sole input about quantum traces used in the prime-power count.

## 2. The two nonsplit prime calculations

The characteristic polynomial of $S$ is
$$
 X^2-6X+1,
$$
with discriminant $32$. It is irreducible modulo $3$ and modulo $5$: its discriminant is a nonsquare in each field.

Useful exact powers are
$$
 S^2=\begin{pmatrix}17&24\\12&17\end{pmatrix},\qquad
 S^3=\begin{pmatrix}99&140\\70&99\end{pmatrix}.
$$
Modulo $3$, $S^2=-I$, and $S\ne\pm I$. Thus $S$ has order $4$.
Modulo $5$, $S^3=-I$ and $S^2\ne I$. Thus its order is $6$.

Writing $r_0=p+1$, the exact lift checks are
$$
 S^4=\begin{pmatrix}577&816\\408&577\end{pmatrix},
 \quad
 \frac{S^4-I}{3}\equiv
 \begin{pmatrix}0&2\\1&0\end{pmatrix}\pmod3,
$$
$$
 S^6=\begin{pmatrix}19601&27720\\13860&19601\end{pmatrix},
 \quad
 \frac{S^6-I}{5}\equiv
 \begin{pmatrix}0&4\\2&0\end{pmatrix}\pmod5.
 \tag{2.1}
$$
The two displayed residual determinants are respectively $1$ modulo $3$ and $2$ modulo $5$. Thus in each case
$$
 S^{r_0}=I+pB,\qquad B\bmod p\text{ invertible}.
 \tag{2.2}
$$

These are exact integer calculations, independently recomputed. They are not numerical eigenvalue tests.

Over $\mathbb F_{p^2}$, $S\bmod p$ has distinct eigenvalues $\xi,\xi^{-1}$, with $\xi$ of order $r_0$. Consequently,
$$
 r_0\nmid m
 \quad\Longrightarrow\quad
 S^m-I\text{ is invertible modulo }p.
 \tag{2.3}
$$
It is not enough merely to know $S^m\ne I$; the nonsplit argument supplies the stronger invertibility required for the kernel count.

## 3. Lift to every prime power

For odd $p$, (2.2) implies
$$
 S^{r_0p^ju}-I=p^{j+1}C_{j,u},
 \qquad C_{j,u}\equiv uB\pmod p
 \tag{3.1}
$$
whenever $j\ge0$ and $p\nmid u$.

To prove it, first induct on $j$. If
$$
 (I+pB)^{p^j}=I+p^{j+1}B_j,
 \qquad B_j\equiv B\pmod p,
$$
then raising to the $p$-th power gives
$$
 (I+p^{j+1}B_j)^p
 =I+p^{j+2}B_j\pmod{p^{j+3}}.
$$
For $2\le a\le p-1$, the $a$-th binomial term has valuation at least $1+a(j+1)\ge j+3$. The last term has valuation $p(j+1)\ge j+3$, including the boundary case $p=3,j=0$. Finally, raising to $u$ gives residual leading coefficient $uB_j$, proving (3.1).

Since $uB$ is invertible modulo $p$, the leading valuation is exact. Combining (3.1) with (2.3), the order of $S$ modulo $p^k$ is
$$
 r=(p+1)p^{k-1}.
 \tag{3.2}
$$

For $0\le m<r$, all kernel counts in (1.2) are now determined:

| Type of $m$ | Number of such $m$ | Size of the kernel |
|---|---:|---:|
| $m=0$ | $1$ | $p^{2k}$ |
| $p+1\nmid m$ | $p^k$ | $1$ |
| $m=(p+1)p^j u,\ p\nmid u,\ 0\le j\le k-2$ | $(p-1)p^{k-j-2}$ | $p^{2j+2}$ |

For the last row, $C_{j,u}$ is invertible modulo $p^k$. Multiplication by $p^{j+1}$ on one copy of $\mathbb Z/p^k\mathbb Z$ has a kernel of size $p^{j+1}$, and there are two coordinates.

For $k=1$, the last row is empty. This case is included in the formulas below.

## 4. The complete period average is exactly $N$

Using the table,
$$
 \begin{aligned}
 \sum_{m=0}^{r-1}|\operatorname{Tr}M_{p^k}^m|^2
 &=p^{2k}+p^k
 +(p-1)\sum_{j=0}^{k-2}p^{k-j-2}p^{2j+2}\\
 &=p^{2k}+p^k
   +(p-1)p^k\sum_{j=0}^{k-2}p^j\\
 &=p^{2k}+p^k+p^k(p^{k-1}-1)\\
 &=p^{2k-1}(p+1).
 \end{aligned}
 \tag{4.1}
$$
The empty sum at $k=1$ is zero, matching the same final expression. Since $r=(p+1)p^{k-1}$,
$$
 \frac1r\sum_{m=0}^{r-1}|\operatorname{Tr}M_{p^k}^m|^2=p^k=N.
 \tag{4.2}
$$

The term $m=0$, equal to $N^2$, is included. Omitting it would destroy the equality needed for simplicity.

## 5. Remove the projective scalar before Fourier inversion

By exact Egorov and $S^r=I$, the matrix $M_N^r$ commutes with the full Weyl basis. Hence
$$
 M_N^r=\eta I,\qquad |\eta|=1.
$$
Choose $c$ with $|c|=1$ and $c^r\eta=1$, and put
$$
 \widehat M=cM_N.
$$
Then $\widehat M^r=I$. This rephasing changes neither multiplicities nor absolute values of power traces.

Let $n_a$ be the multiplicity of $e^{2\pi ia/r}$ in $\widehat M$, for $0\le a<r$. Finite Fourier orthogonality gives
$$
 \frac1r\sum_{m=0}^{r-1}
 \left|\sum_{a=0}^{r-1}n_a e^{2\pi iam/r}\right|^2
 =\sum_{a=0}^{r-1}n_a^2.
$$
Together with (4.2),
$$
 \sum_a n_a^2=N=\sum_a n_a.
$$
Every $n_a$ is a nonnegative integer, so
$$
 \sum_a n_a(n_a-1)=0
 \quad\Longrightarrow\quad n_a\in\{0,1\}.
$$
Thus $M_N$ has simple spectrum for every $N=3^k$ or $5^k$.

The argument does not assume $M_N^r=I$ before the rephasing. It only needs the scalar consequence of Egorov, so finite metaplectic normalization does not create a gap.

## 6. Transfer to the original kicked family by its discriminant

Every entry of $A_N$ and $M_N$ is algebraic. Since $A_N$ is Hermitian, its distinct-eigenvalue spectral projectors are algebraic and
$$
 e^{izNA_N}=\sum_j e^{izN\rho_j}P_j
$$
is a finite matrix-valued exponential polynomial.

Let
$$
 \chi_z(X)=\det(XI-e^{izNA_N}M_N),
 \qquad \Delta(z)=\operatorname{disc}_X\chi_z.
$$
The coefficients of $\chi_z$, and therefore $\Delta(z)$, are finite exponential polynomials with algebraic coefficients and algebraic frequencies. The discriminant is a polynomial with integer coefficients in the coefficients of the monic characteristic polynomial.

The result already proved gives
$$
 \Delta(0)=\operatorname{disc}\chi_{M_N}\ne0.
$$
After combining equal frequencies,
$$
 \Delta(z)=\sum_{\nu=1}^{t}a_\nu e^{b_\nu z},
$$
where $b_\nu$ are distinct algebraic numbers and the nonzero coefficients $a_\nu$ are algebraic.

For nonzero algebraic $z_0$, the numbers $b_\nu z_0$ remain distinct algebraic numbers. Lindemann–Weierstrass therefore gives
$$
 \Delta(z_0)\ne0.
$$
The exact classical result used is the algebraic-linear-independence form, for example Theorem 3.2 in Sever Angel Popescu, *A simple and self-contained proof for the Lindemann–Weierstrass theorem*, arXiv:2306.14352v2:
https://arxiv.org/pdf/2306.14352v2 .

Thus the kicked matrix has simple spectrum at every algebraic parameter. No perturbative estimate, genericity assertion, smallness assumption on $z_0$, or simplicity assumption on $A_N$ is used.

## 7. Complete classification of the bare cat in odd dimensions

### 7.1. General prime-power period and its leading matrix

Write
$$
 J=\begin{pmatrix}0&2\\1&0\end{pmatrix},\qquad
 S=3I+2J,\qquad J^2=2I.
$$
Every positive power has the form
$$
 S^r=t_rI+u_rJ,\qquad t_r^2-2u_r^2=1,
$$
with integer $t_r,u_r$ and $u_r>0$.

Let $p$ be any odd prime and $r_p=\operatorname{ord}_p S$. The characteristic discriminant $32$ is nonzero modulo $p$, so the reduction is semisimple. In the split case $r_p\mid p-1$; in the nonsplit case $r_p\mid p+1$. In particular $r_p\le p+1$ and $p\nmid r_p$.

Since $S^{r_p}=I\bmod p$, one has $t_{r_p}=1\bmod p$ and $u_{r_p}=0\bmod p$. Put $s_p=v_p(u_{r_p})\ge1$. The identity
$$
 (t_{r_p}-1)(t_{r_p}+1)=2u_{r_p}^2
$$
has $t_{r_p}+1$ a $p$-adic unit. Therefore
$$
 v_p(t_{r_p}-1)=2s_p,\qquad
 p^{-s_p}(S^{r_p}-I)
 \equiv (u_{r_p}/p^{s_p})J\pmod p.
 \tag{7.1}
$$
The residual matrix is invertible because $\det J=-2$ is a unit modulo odd $p$. Thus the matrix lift has no singular leading coefficient.

The binomial proof in Section 3, with initial valuation $s_p$, now gives
$$
 \operatorname{ord}_{p^a}S
 =r_p\,p^{\max(0,a-s_p)}=:R_{p,a}.
 \tag{7.2}
$$
Reduction modulo $p$ forces any period to be divisible by $r_p$, and the invertible residual in (7.1) proves the exact additional power of $p$.

### 7.2. Necessity and sufficiency at a prime power

Exact Egorov implies $M_{p^a}^{R_{p,a}}$ is scalar. Hence $M_{p^a}$ has at most $R_{p,a}$ distinct eigenvalues.

If $r_p\ne p+1$, then $r_p\le p-1$, and
$$
 R_{p,a}\le(p-1)p^{a-1}<p^a.
$$
Thus the spectrum is not simple.

If $r_p=p+1$, but $a\ge2$ and $s_p\ge2$, then
$$
 R_{p,a}=(p+1)p^{\max(0,a-s_p)}<p^a.
$$
For $a\le s_p$ this follows from $p+1<p^2$; for $a>s_p$ it follows from $(p+1)p^{a-2}<p^a$. Again the spectrum is not simple.

The remaining cases are exactly $r_p=p+1$ with $a=1$ or $s_p=1$. The prime case follows from the count $p^2+p$ over a period $p+1$. For $s_p=1$, Sections 3–5 prove simplicity at every $p^a$. This proves the claimed classification at prime powers.

Equivalently, when $a\ge2$ and $r_p=p+1$, the lift condition can be checked as
$$
 S^{p+1}\not\equiv I\pmod{p^2}.
$$
For this specific Pell matrix, (7.1) makes that condition equivalent to an invertible leading lift. No distribution assertion about the primes satisfying it is used.

### 7.3. CRT twists preserve the local classification

Factor $N=\prod_{i=1}^{h}q_i$, where $q_i=p_i^{a_i}$ are pairwise coprime prime powers. The canonical CRT coordinate permutation gives the exact tensor factorization
$$
 M_N=\bigotimes_{i=1}^{h}M_{q_i}^{(c_i)},
 \qquad c_i=(N/q_i)^{-1}\pmod{q_i},
$$
where
$$
 (M_q^{(c)})_{xy}
 =q^{-1/2}e_q[-c\,\overline8(3x^2-2xy+3y^2)].
 \tag{7.3}
$$
All $c_i$ are units. This follows from the CRT additive-character identity; the normalization factors multiply to $N^{-1/2}$. It does not identify a twisted factor with the untwisted $M_q$ without proof.

Direct comparison of the two kernels gives exact Egorov for a twisted factor:
$$
 M_q^{(c)}T_q(a,b)(M_q^{(c)})^{-1}
 =T_q(3a+4c^{-1}b,\ 2ca+3b).
$$
Its label matrix is
$$
 S_c=\begin{pmatrix}3&4c^{-1}\\2c&3\end{pmatrix}
 =\operatorname{diag}(1,c)\,S\,\operatorname{diag}(1,c)^{-1}.
 \tag{7.4}
$$
Thus all orders and fixed-kernel counts agree with those of $S$. The prime-power classification just proved applies to every twisted factor as well.

### 7.4. Every dimension with two distinct prime factors is degenerate

If some factor in (7.3) has a repeated eigenvalue, its tensor product with the other unitary factors also has a repeated eigenvalue.

Otherwise all factors are simple. A simple local factor of dimension $q_i=p_i^{a_i}$ has the even projective period
$$
 R_i=(p_i+1)p_i^{a_i-1},
$$
and
$$
 q_i>\frac{R_i}{2}.
$$
After a scalar rephasing, its $q_i$ distinct eigenvalues are a subset of the $R_i$-th roots of unity. Those roots split into $R_i/2$ antipodal pairs. A subset with more than $R_i/2$ elements contains a full pair; hence the original factor has eigenvalues $\lambda,-\lambda$.

Take antipodal pairs $\lambda,-\lambda$ and $\mu,-\mu$ from two factors. Their tensor product has the same eigenvalue
$$
 \lambda\mu=(-\lambda)(-\mu)
$$
on two distinct tensor eigenvectors. Additional factors can be kept at any fixed eigenvector. Thus $M_N$ is not simple whenever $h\ge2$.

Combined with Section 7.2, this finishes the full odd-dimensional bare-cat classification.

### 7.5. Final independent check of the shorter composite bound

The author's additional estimate $q(M_N)\le\operatorname{ord}_N(S)\le8N/9$ is correct. Indeed, write $N=\prod_{j=1}^{h}n_j$, $h\ge2$, and $R_j=\operatorname{ord}_{n_j}S$. Formula (7.2) gives $R_j/n_j\le(p_j+1)/p_j\le4/3$. If $R_j$ is odd, then $r_{p_j}$ is an odd divisor of the even number $p_j-1$ or $p_j+1$, so $R_j/n_j\le(p_j+1)/(2p_j)\le2/3$. Let $e$ count the even $R_j$. Classical CRT gives $R=\operatorname{lcm}_j R_j$. If $e\ge1$, the product contains at least $e-1$ factors of $2$ beyond those needed in the least common multiple, and therefore $R/N\le(4/3)^e(2/3)^{h-e}/2^{e-1}=2(2/3)^h\le8/9$. If $e=0$, $R/N\le(2/3)^h\le4/9$. Exact Egorov makes $M_N^R$ scalar, so there are at most $R$ distinct eigenvalues. This proves the stronger count without a quantum tensor-factorization assumption. Its scope is the bare $M_N$; it gives no multiplicity bound for the perturbed $U_N(\tau)$.

## 8. Audit limits

The classification is for the exact original $M_N$, including its CRT twists and arbitrary odd composite dimensions. It gives simplicity of $U_N(z)$ at every algebraic parameter whenever the bare-cat criterion is satisfied. The explicit primes $3,5$ satisfy it at every power, as verified in Section 2.

When the bare cat is degenerate, the present argument supplies no proof that $\Delta(z)$ vanishes identically. A kick can split a bare degeneracy. Thus this complete classification of $M_N$ must not be reported as a classification of simplicity of $U_N(\tau)$.

The review covers the exact Egorov, prime-power and CRT arguments, and the Lindemann–Weierstrass discriminant transfer. Separate finite-field compression certificates, complex-time principal-minor criteria, and the numerical range of such certificates are not certified by this review.

These are theorems about the original deterministic family. They provide no quantitative level repulsion, $O(N)$ close-pair count, or CUE/Hdiag limit.

