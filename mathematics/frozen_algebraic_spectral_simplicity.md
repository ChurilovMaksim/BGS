# Algebraic spectral simplicity of the frozen propagator away from 7

**Claim ID:** `BGS-FM-008`. **Status:** project proof with an independently
checked external Lindemann–Weierstrass input and author-level p-adic audit;
no peer review. Adapted from Sections 2.5 and 3.1–3.5 of the submitted
24 September 2026 article (PDF SHA-256
`aeb0f82d35b3d40eb2e9a3fded9417c55df95e393f3de148f01457ecad844454`).
The simpler cyclic Jacobi decomposition and rank statement were already
available in [`frozen_kick_rank_boundary.md`](frozen_kick_rank_boundary.md).

## Theorem and precise limits

Let $N\ge3$ be odd with $7\nmid N$, and let $A_N,M_N$ be the **unchanged**
matrices of [`fixed_model_symmetry_theorem.md`](fixed_model_symmetry_theorem.md).
The eigenvalues of $A_N$ are simple. In **every** eigenbasis of $A_N$,
every square minor of $M_N$, of any order and with arbitrary row and column
sets, is nonzero. This is an algebraic nonvanishing result: no uniform lower
bound on the minors is asserted.

Moreover, for each nonzero real algebraic $t$, put
$U_N(t)=e^{itA_N}M_N$. Then:

1. $U_N(t)$ and each nonzero integer power $U_N(t)^m$ have simple spectra;
2. the ratio of any two **different** eigenvalues of $U_N(t)$ is
   transcendental;
3. every coefficient of $\det(I-zU_N(t))$ is nonzero;
4. for each nonzero integer $m$,
   $|\operatorname{Tr}U_N(t)^m|^2$ is transcendental.

These conclusions apply at the original fixed coupling
$t=\tau N=10^{-80}N$. They cover **only** $7\nmid N$. They exclude exact
collisions but supply no quantitative eigenphase gap or estimates of joint
traces at $m\asymp N$; neither the pair limit nor CUE follows.

## 1. A 5-adic degeneration of the Jacobi generator

Work in an algebraic closure of $\mathbb Q(i,e^{2\pi i/N})$ with a valuation
$v$ over $\varpi=1+2i$, normalized by $v(5)=1$. Only a finite extension
is needed for each $N$. Along the unique Jacobi path from
[`frozen_kick_rank_boundary.md`](frozen_kick_rank_boundary.md), take
$B=1000A_N$. Its upper and lower off-diagonal entries are

$$
b_j=(-3-4i)r_j,\qquad c_j=(-3+4i)r_j,\qquad
r_j=r((x_j+h)/N)\ne0.
$$

Here $v(-3-4i)=0$ and $v(-3+4i)=2$, because
$-3+4i=(1+2i)^2$. Writing $z=e^{2\pi iq}$,
$r(q)=-(z^7-1)^2(z+1)^2/(4z^8)$. As $7\nmid N$, for every nonzero
path coupling

$$
0\le v(r_j)\le\tfrac12.                          \tag{1}
$$

Indeed, if the root of unity has a prime-to-five order factor,
$1-z^7$ is a valuation unit; otherwise it has order $5^a$,
$v(1-z^7)=1/(4\cdot5^{a-1})\le1/4$. The factor $z+1$ is a unit
because $N$ is odd. The diagonal entries of $B$ have valuation at least
$1$ by multiplying the exact trigonometric terms by $1000$.

Choose $\sigma$ with $v(\sigma)=-3/4$ and diagonal $D$ with
$D_0=1$, $D_{j+1}=D_j/(\sigma b_j)$. Write $d_j=v(D_j)$; then

$$
\tfrac14\le d_{j+1}-d_j=\tfrac34-v(r_j)\le\tfrac34.\tag{2}
$$

The conjugate $B'=\sigma D^{-1}BD$ has upper off-diagonal entries $1$,
diagonal entries of strictly positive valuation, and lower entries with
valuation $1/2+2v(r_j)>0$. Its reduction is therefore the single
nilpotent Jordan block $J$ with ones above the diagonal. Its algebraic
eigenvalues $\beta_i=\sigma(1000a_i)$ all reduce to zero.

## 2. Fourier minors with the smallest possible valuation

Write $N=5^aM$ with $\gcd(5,M)=1$ and $\zeta$ a primitive $N$th root of
unity. For distinct row positions $i_1,\ldots,i_r\pmod N$ and arbitrary
distinct column positions $j_1,\ldots,j_r\pmod N$, the generalized
Vandermonde determinant $\det(\zeta^{i_\alpha j_\beta})$ is divisible
in $\mathbb Z[X_1,\ldots,X_r]$ by
$\prod_{\alpha<\gamma}(X_\gamma-X_\alpha)$, with an integral
quotient. Thus its valuation is at least
$\sum_{\alpha<\gamma}v(1-\zeta^{i_\gamma-i_\alpha})$.

For $a>0$ and a nonzero difference $d\pmod N$, this last valuation is
the **positive linear combination**

$$
v(1-\zeta^d)=\mathbf1_{M\mid d}
 \left(\frac1{4\cdot5^{a-1}}+
 \sum_{h=1}^{a-1}5^{h-a}\mathbf1_{5^h\mid d}\right). \tag{3}
$$

For $a=0$ it is zero. For each modulus $M5^h$, the number of pairs
equal modulo that modulus is minimized by evenly distributed residue
counts. A consecutive block of $r$ positions attains this minimum
**simultaneously** for all $h$. It follows that every order-$r$ minor
of the Fourier matrix $F=(\zeta^{ij})_{0\le i,j<N}$ has valuation at
least

$$
c_{N,r}=\sum_{d=1}^{r-1}(r-d)v(1-\zeta^d).       \tag{4}
$$

Consecutive columns make the quotient in the Vandermonde determinant a
unit monomial; consecutive rows attain (4). This proves the bound and
identifies an extremal minor even when $5\mid N$. The finite exact
regression [`frozen_total_minors.py`](../computations/verification/frozen_total_minors.py)
checks representative subset cases; it cannot prove the all-$N$ balance
argument.

## 3. Exterior powers and total nonvanishing

Order the path as in Section 1. The metaplectic kernel factors as

$$
(M_N)_{jk}=N^{-1/2}u_jw_k\,\zeta^{jk},
$$

where $u_j,w_k$ are roots of unity and $\zeta=e_N(4^{-1})$ is primitive.
Conjugating by $D$ does not change the Fourier-minor inequality apart
from its row/column valuation shifts. Let $I_+=\{N-r,\ldots,N-1\}$,
$I_-=\{0,\ldots,r-1\}$. By (2) and (4), among the entries of
$\wedge^r(D^{-1}M_ND)$, the entry $(I_+,I_-)$ has uniquely smallest
valuation, and it is nonzero. Rescaling by its inverse, the exterior
operator reduces to the elementary matrix $E_{I_+,I_-}$.

For $B'$ with reduction $J$, a right eigenvector for any $\beta_i$
has components $\varphi_j(\beta_i)$, where each $\varphi_j\in\mathcal O[X]$
is monic of degree $j$ and $\varphi_j\equiv X^j$ modulo the maximal
ideal. Divide each exterior product of $r$ distinct right eigenvectors
by the Vandermonde of its eigenvalues. Polynomial alternants show that
the resulting integral vector reduces to $e_0\wedge\cdots\wedge e_{r-1}$.
The corresponding normalized left exterior vector reduces, up to sign,
to $(e_{N-r}\wedge\cdots\wedge e_{N-1})^T$. Contracting the two with
the rescaled middle operator gives reduction $\pm1$. This contraction
is, up to nonzero Vandermonde and eigenvector-normalization factors,
**any chosen** order-$r$ minor of $M_N$ in an eigenbasis of $A_N$.
Consequently every such minor is nonzero.

## 4. Fixed algebraic times and spectral consequences

Order the real, distinct eigenvalues of $A_N$ as
$a_1>\cdots>a_N$. In that eigenbasis all leading principal minors
$b_r=\det(M_N)_{\{1,\ldots,r\},\{1,\ldots,r\}}$ are nonzero;
put $b_0=1$. For real $s\to+\infty$, the characteristic coefficients of
$e^{sA_N}M_N$ obey

$$
e_r(s)=b_r e^{s(a_1+\cdots+a_r)}(1+o(1)).     \tag{5}
$$

This follows by comparing the finitely many distinct exponent sums.
Rescale the characteristic polynomial near $z=e^{sa_j}w$. Its two
leading terms are the adjacent coefficients $r=j-1,j$; Rouché's
theorem gives one simple eigenvalue
$\Lambda_j(s)=(b_j/b_{j-1})e^{sa_j}(1+o(1))$.
Their modulus scales are pairwise distinct. Thus the discriminant of
$e^{itA_N}M_N$ is *not identically zero* as a function of complex $t$.

Each coefficient of $\det(zI-e^{itA_N}M_N)$ and each polynomial
expression in those coefficients is a **finite exponential polynomial**
in $t$ with algebraic coefficients and real algebraic frequencies, by
the algebraicity of the spectral projectors of $A_N$ and of $M_N$.
For fixed nonzero algebraic $t$, the [Lindemann–Weierstrass theorem,
Popescu's Theorem 3.2 (arXiv:2306.14352v2)](https://arxiv.org/pdf/2306.14352)
says that exponentials of *distinct algebraic* exponents are linearly
independent over the field of algebraic numbers. Therefore any such
exponential polynomial vanishes at this $t$ **if and only if** it is
identically zero. Applying this to the discriminant and (5) proves
simplicity and nonvanishing of all characteristic coefficients.

For any fixed algebraic $\eta\ne0,1$, the resultant of
$\chi_t(z)$ and $\eta^N\chi_t(z/\eta)$ is another such exponential
polynomial. It is not identically zero because at $t=-is$ the
eigenvalue moduli have different exponential scales, and a nonzero
eigenvalue cannot be $\eta$ times itself when $\eta\ne1$. Hence no
ratio of different eigenvalues at a nonzero algebraic $t$ is
algebraic. Equal powers would give a root-of-unity ratio, proving
the power statement.

Finally, for $m\ne0$, $|\operatorname{Tr}U_N(t)^m|^2$
is an exponential polynomial in $t$ with algebraic coefficients
(for real $t$, use $U_N(t)^{-m}=M_N^{-1}e^{-itA_N}$ as appropriate in
the trace product). The same large imaginary-time witness shows it is
nonconstant: the leading exponent of the product of the largest and
smallest eigenvalue contributions is positive. Lindemann–Weierstrass
applied after subtracting any prescribed algebraic constant shows the
squared trace is transcendental.

The total-minor argument and fixed-time transcendence are qualitative.
In particular they do not bound how close a ratio can be to a root of
unity as $N\to\infty$, or the cancellation of the alternating partition
sum defining a microscopic factorial statistic.
