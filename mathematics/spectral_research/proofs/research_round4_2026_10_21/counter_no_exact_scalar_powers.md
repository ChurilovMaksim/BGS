> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_no_exact_scalar_powers.md`. Embedded SHA256: `b443bef206df2c6a7764ade3bec61c9a27acd29429ee5889048e7e6e483718a3`.
> [Thematic guide](../../topics/closure.md).

# No exact scalar powers for the prescribed family

Research continuation, 21 October 2026.

## 1. Exact statement and scope

All matrices and Fourier coefficients in this note are those in the original
problem, including the modular inverses in the Weyl operators, the prescribed
matrix $M_N$, and the fixed number $\tau=10^{-80}$. Write
$$
U_N(s)=e^{isNA_N}M_N,\qquad s\in\mathbb C.
\tag{1.1}
$$
The problem's matrix is $U_N(\tau)$.

**Theorem 1.** For every odd $N\ge3$ with $N\ne7$, every nonzero algebraic
number $s_0$, and every integer $n\ge1$,
$$
\boxed{U_N(s_0)^n\notin\mathbb C I.}
\tag{1.2}
$$
In particular, the exact unitary $U_N=U_N(\tau)$ has infinite order in the
projective unitary group for every such $N$.

The exceptional dimension is genuine: $A_7=(9/10)I$ and $U_7(s)^3$ is scalar
for every $s\in\mathbb C$.

The proof uses algebraicity of the *fixed* kick parameter, an exact covariance,
and a strict Fourier coefficient imbalance of the specified perturbation.
It supplies no lower bound, uniform in $n,N$, for the distance of $U_N^n$
from scalar matrices. It therefore excludes exact projective revivals, while
leaving possible near-revivals and the spectral-statistics limit unresolved.
No assertion of historical novelty is made.

## 2. Exact modular covariance and the Weyl basis

Put
$$
W_N(k,l)=T_N(l,k),\qquad
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
\tag{2.1}
$$
These are the original modular-half Weyl matrices, without any additional
integer-lift sign convention. All arithmetic in this section is modulo $N$.

First,
$$
\frac1N\operatorname{Tr}(W_N(u)^*W_N(v))=\mathbf 1_{\{u=v\}}.
\tag{2.2}
$$
Indeed a nonzero translation has zero diagonal, while a zero translation with
nonzero modulation has trace $\sum_x e_N(bx)=0$. Applying this observation
to $T_N(a,b)^*T_N(a',b')$, whose translation and modulation are respectively
$a'-a,b'-b$, proves (2.2); when the labels coincide the product is $I$.
Thus these $N^2$ matrices form an orthonormal basis of $M_N(\mathbb C)$.
In particular, equality of two Weyl matrices implies equality of their labels,
and a scalar matrix has zero coefficient at each nonzero label.

The covariance needed below is
$$
M_NT_N(a,b)=T_N(3a+4b,\,2a+3b)M_N,
\qquad
M_NW_N(v)M_N^{-1}=W_N(Sv).
\tag{2.3}
$$
Here is a direct check, including the phase. Remove the common factor
$$
N^{-1/2}e_N\!\left(-8^{-1}(3x^2-2xy+3y^2)\right)
$$
from the $(x,y)$ entry. For $M_NT_N(a,b)$ the remaining exponent is
$$
-4^{-1}ax+(3\cdot4^{-1}a+b)y
 -3\cdot8^{-1}a^2-2^{-1}ab.
\tag{2.4}
$$
For $T_N(a',b')M_N$ it is
$$
(b'-3\cdot4^{-1}a')x+4^{-1}a'y
 +2^{-1}a'b'-3\cdot8^{-1}(a')^2.
\tag{2.5}
$$
Substitute $a'=3a+4b$, $b'=2a+3b$. The coefficients of $x,y$ agree, and
the constant term is
$$
8^{-1}a'(4b'-3a')
=-8^{-1}a(3a+4b),
$$
which is the constant in (2.4). This proves (2.3) for every odd $N$, with
no residual phase.

Consequently,
$$
M_N^n\in\mathbb CI
\quad\Longrightarrow\quad
S^n=I\pmod N.
\tag{2.6}
$$
To see this, conjugation by the scalar $M_N^n$ is the identity, so (2.3)
gives $W_N(S^nv)=W_N(v)$ for every label $v$. Apply (2.2).
Since $\det S=1$, each orbit under $S$ is a finite cycle, and (2.6) implies
that the length of each cycle divides $n$.

We shall also use the converse implication that $S^n=I\pmod N$ makes
$M_N^n$ scalar. In that case (2.3) says $M_N^n$ commutes with every Weyl
matrix, hence with every matrix by (2.2). A matrix commuting with every
matrix is scalar: commuting with the diagonal coordinate projections makes
it diagonal, and commuting with all matrix units makes its diagonal entries
equal.

## 3. A Fourier imbalance which survives all aliases

In this section abbreviate
$$
C_j(q)=\cos(2\pi jq),\qquad S_j(q)=\sin(2\pi jq).
$$
The prescribed function $r$ has the exact expansion
$$
r=1+C_1-C_7-\tfrac12 C_8-\tfrac12 C_6.
\tag{3.1}
$$
It follows that
$$
f-\tfrac1{10}
=\tfrac9{10}C_7
 +\left(\tfrac1{10}C_1-\tfrac1{20}C_8-\tfrac1{20}C_6\right)
 +\tfrac1{100}rS_1
 +\tfrac1{100}r\cos(2\pi p-\alpha_0).
\tag{3.2}
$$
There is no frequency $7$ in the pure-$q$ product $rS_1$, since
$$
rS_1=S_1+\tfrac12S_2-\tfrac12S_8+\tfrac12S_6
      -\tfrac14S_9+\tfrac14S_5.
\tag{3.3}
$$
The last term in (3.2) has only $p$-frequencies $1,-1$. Therefore, for the
original Fourier coefficients before reduction modulo $N$,
$$
c_{(7,0)}=c_{(-7,0)}=\frac9{20}.
\tag{3.4}
$$

For a finite Fourier polynomial $F=\sum_\kappa F_\kappa e^{2\pi i\kappa x}$
let $\|F\|_{\mathcal F,1}=\sum_\kappa|F_\kappa|$.
The triangle inequality and convolution give
$\|FG\|_{\mathcal F,1}\le\|F\|_{\mathcal F,1}\|G\|_{\mathcal F,1}$.
A sine or cosine of nonzero frequency has this norm equal to $1$, including
the phase-shifted cosine in (3.2). Formula (3.1) gives
$\|r\|_{\mathcal F,1}=4$. Thus the three terms after $(9/10)C_7$ in (3.2)
have total Fourier norm at most
$$
\frac1{10}+\frac1{20}+\frac1{20}+\frac4{100}+\frac4{100}
=\frac7{25}.
$$
They have no coefficients at $(7,0),(-7,0)$ by (3.3), so
$$
\boxed{\sum_{\kappa\ne(7,0),(-7,0)}|c_\kappa|\le\frac7{25}.}
\tag{3.5}
$$

For every residue label $v\in(\mathbb Z/N\mathbb Z)^2$, set
$$
\widetilde c_v=\sum_{\kappa\equiv v\pmod N}c_\kappa.
\tag{3.6}
$$
The sum is finite and the exact quantization rule gives
$$
A_N=\sum_v\widetilde c_v W_N(v).
\tag{3.7}
$$
No assumption about absence of Fourier aliases has entered this formula.

Suppose $N$ is odd, $N\ge3$, and $N\ne7$. The label
$v_0=(7\bmod N,0)$ is then nonzero. Let $\mathcal O$ be its orbit under
$S$, and let $L=|\mathcal O|$. By (3.6),
$$
\sum_{v\in\mathcal O}\widetilde c_v
=\sum_{\kappa:\ \kappa\bmod N\in\mathcal O}c_\kappa.
\tag{3.8}
$$
The right side includes $c_{(7,0)}=9/20$. If it also includes $c_{(-7,0)}$,
that coefficient is positive and real. All other terms have total absolute
value at most $7/25$ by (3.5). Consequently
$$
\boxed{\operatorname{Re}\sum_{v\in\mathcal O}\widetilde c_v
\ge\frac9{20}-\frac7{25}=\frac{17}{100}>0.}
\tag{3.9}
$$
This bound is valid also in the small dimensions where several original
frequencies reduce to the same label.

## 4. Exact algebraic evaluation of exponential polynomials

The only external theorem used is the distinct-exponent form of
Lindemann--Weierstrass: a linear combination of exponentials of distinct
complex algebraic numbers, with nonzero algebraic coefficients, cannot vanish.
A precise published source is Cheng-Chao Huang, *Explicit Bounds for Linear
Forms in the Exponentials of Algebraic Numbers*, Proceedings of ISSAC 2022,
Theorem 1.1, DOI
[10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170).
The statement was independently checked on 21 October 2026 in the
[author's version, arXiv:2112.05004v2, 16 May 2022](https://arxiv.org/pdf/2112.05004v2),
page 1. The exact version displays the publication metadata and DOI. The DOI
landing page itself was inaccessible in the browsing tool; the theorem text
and its hypotheses were read in the versioned author PDF.

Here is the needed implication, with its hypotheses verified explicitly.
Let
$$
F(s)=\sum_{\beta\in B}a_\beta e^{\beta s},
\qquad a_\beta,\beta\in\overline{\mathbb Q},
\tag{4.1}
$$
where $B$ is finite. First combine terms with equal slopes $\beta$, then
discard zero coefficients. If any terms remain and $s_0\ne0$ is algebraic,
their exponents $\beta s_0$ are distinct algebraic numbers. The quoted
theorem therefore says $F(s_0)\ne0$. We have proved
$$
s_0\in\overline{\mathbb Q}\setminus\{0\},\quad F(s_0)=0
\quad\Longrightarrow\quad F\equiv0.
\tag{4.2}
$$
No rational independence assumption on the slopes is needed.

Every entry of $A_N$ and $M_N$ is algebraic. Indeed, all $e_N$-values
are roots of unity, $N^{-1/2}$ is algebraic, and the coefficients in the
Fourier expansion are rational combinations of $i$ and
$$
e^{i\alpha_0}=\frac{-3+4i}{5},\qquad
e^{-i\alpha_0}=\frac{-3-4i}{5}.
$$
There is no need for the angle $\alpha_0$ itself to be algebraic.

Let $\Lambda$ be the set of distinct eigenvalues of the Hermitian matrix
$A_N$. Its characteristic polynomial has algebraic coefficients, so every
$\lambda\in\Lambda$ is algebraic. The spectral projectors are the algebraic
matrices
$$
P_\lambda=\prod_{\substack{\mu\in\Lambda\\\mu\ne\lambda}}
\frac{A_N-\mu I}{\lambda-\mu}.
\tag{4.3}
$$
This formula allows arbitrary multiplicities. The finite-dimensional spectral
theorem gives
$$
e^{isNA_N}=\sum_{\lambda\in\Lambda}e^{iNs\lambda}P_\lambda.
\tag{4.4}
$$
Therefore
$$
U_N(s)^n
=\sum_{\lambda_1,\ldots,\lambda_n\in\Lambda}
e^{iNs(\lambda_1+\cdots+\lambda_n)}
P_{\lambda_1}M_NP_{\lambda_2}M_N\cdots P_{\lambda_n}M_N.
\tag{4.5}
$$
Each entry, and every difference of two diagonal entries, is of the form
(4.1): its coefficients are algebraic, and its slopes are the algebraic
numbers $iN(\lambda_1+\cdots+\lambda_n)$. Equal sums are combined before
applying (4.2).

It follows in particular that
$$
U_N(s_0)^n\in\mathbb CI
\quad\Longrightarrow\quad
U_N(s)^n=\zeta(s)I\quad\hbox{for every }s\in\mathbb C,
\tag{4.6}
$$
for an entire scalar function $\zeta$, whenever $s_0\ne0$ is algebraic.
To prove (4.6), apply (4.2) separately to each off-diagonal entry and to
each diagonal entry minus the first diagonal entry. These vanish at $s_0$
and hence identically. This argument does not assume that the unknown
scalar at $s_0$ is algebraic.

## 5. Contradiction from the first derivative

Assume the hypotheses of Theorem 1 and, for contradiction,
$U_N(s_0)^n\in\mathbb CI$. By (4.6), $U_N(s)^n$ is scalar for all $s$.
At $s=0$ this says $M_N^n$ is scalar; it is nonzero because $M_N$ is
unitary. By (2.6), $S^n=I\pmod N$. In particular the orbit length $L$ in
Section 3 divides $n$.

The product rule, using $U_N(0)=M_N$ and
$U_N'(0)=iNA_NM_N$, gives
$$
\left.\frac{d}{ds}U_N(s)^n\right|_{s=0}
=iN B_nM_N^n,\qquad
B_n=\sum_{j=0}^{n-1}M_N^jA_NM_N^{-j}.
\tag{5.1}
$$
The left side is scalar by (4.6). Since $iNM_N^n$ is an invertible scalar,
$B_n$ must be scalar.

On the other hand, (2.3) and (3.7) give
$$
B_n=\sum_v\left(\sum_{j=0}^{n-1}
\widetilde c_{S^{-j}v}\right)W_N(v).
\tag{5.2}
$$
As $j$ runs from $0$ to $n-1$, $S^{-j}v_0$ traverses every point of
$\mathcal O$ exactly $n/L$ times. Thus its coefficient at the nonzero
label $v_0$ has real part
$$
\operatorname{Re}\frac1N\operatorname{Tr}(W_N(v_0)^*B_n)
=\frac nL\operatorname{Re}\sum_{v\in\mathcal O}\widetilde c_v
\ge\frac{17n}{100L}>0.
\tag{5.3}
$$
This contradicts scalarity of $B_n$, by (2.2). Theorem 1 follows.

## 6. The genuine exceptional dimension

At $N=7$, the Fourier factor $1-C_7$ reduces to zero in every fixed
$p$-frequency block: replacing a $q$-frequency $k$ by $k+7$ leaves
the original matrix $T_7(l,k)$ exactly unchanged. Since
$r=(1-C_7)(1+C_1)$, the quantizations of $r$, $rS_1$, and
$r\cos(2\pi p-\alpha_0)$ all vanish. The remaining quantization is
$$
A_7=\operatorname{Op}_7(C_7-\tfrac1{10})=\frac9{10}I.
\tag{6.1}
$$
Also
$$
S^3=\begin{pmatrix}99&70\\140&99\end{pmatrix}=I\pmod7.
\tag{6.2}
$$
The converse following (2.6) gives $M_7^3\in\mathbb CI$, so
$$
U_7(s)^3=e^{\,3is7(9/10)}M_7^3\in\mathbb CI.
\tag{6.3}
$$
This finite exception has no asymptotic consequence by itself.

## 7. What the theorem does and does not settle

Theorem 1 distinguishes the prescribed family from auxiliary flat-adjoint
reflection examples with a scalar power of order two, and from auxiliary
finite Fourier examples with a scalar power of order four. It also excludes
any exact projective periodicity along an infinite sequence of allowed
dimensions in the original family.

The argument is qualitative at the algebraic evaluation step. Formula (5.3)
is a lower bound for a derivative at $s=0$; it is not a lower bound for the
matrix at $s=\tau$, and no such transfer is made. In particular,
$$
\operatorname{dist}(U_N^n,\mathbb CI)>0
$$
for each fixed $N\ne7,n$ does not control how fast this positive number may
decay as $n,N$ grow. Nothing here proves $H_{\mathrm{diag}}$, disproves it,
or supplies the still missing signed trace cancellations at times of order
$N$.
