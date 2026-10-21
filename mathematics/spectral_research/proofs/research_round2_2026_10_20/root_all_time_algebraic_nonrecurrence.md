> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/root_all_time_algebraic_nonrecurrence.md`. Embedded SHA256: `d4bb6ae891984cff12b9fb437b3c4bda2edb58247a3d0d398b4efb477d70e3a7`.
> [Thematic guide](../../topics/algebra.md).

# No positive power lies on an algebraic matrix line

## Theorem

For every odd $N\ge3$, except $N=7$, every positive integer $m$,
and every nonzero algebraic complex number $z_0$, define
$$
U_N(z)=e^{izNA_N}M_N.
$$
Then
$$
\boxed{U_N(z_0)^m\notin\mathbb C^\times B
\quad\text{for every nonzero }
B\in M_N(\overline{\mathbb Q}).}                       \tag{T}
$$

This applies to the exact parameter $\tau=10^{-80}$, at every
positive time and every odd dimension other than the single exception.
It excludes exact phased returns to any algebraic matrix, including
Weyl and metaplectic matrices. It is an exact assertion: it gives no
lower bound on the distance to such a matrix and no local-statistics
limit.

## 1. The algebraic evaluation principle

Lindemann--Weierstrass states that exponentials of distinct algebraic
numbers are linearly independent over the algebraic numbers.
A precise source containing the full proof is S. A. Popescu,
*A simple and self-contained proof for the Lindemann--Weierstrass
theorem*, Theorem 3.2, <https://arxiv.org/pdf/2306.14352>.
The theorem and proof were checked in the preceding audit.

Consequently, after equal frequencies have been combined,
$$
F(z)=\sum_{j=1}^r c_j e^{\beta_j z},\qquad
c_j,\beta_j\in\overline{\mathbb Q},\quad \beta_j\ne\beta_k\ (j\ne k)
$$
obeys
$$
z_0\in\overline{\mathbb Q}\setminus\{0\},\quad F(z_0)=0
\quad\Longrightarrow\quad F\equiv0.                   \tag{1.1}
$$

The entries of the specified $A_N,M_N$ are algebraic. Their
coefficients use roots of unity, algebraic square roots, rational
numbers, and $e^{i\alpha_0}=(-3+4i)/5$.
The distinct eigenvalues $\lambda_j$ of the Hermitian $A_N$
are algebraic, as are its spectral projectors
$$
P_j=\prod_{k\ne j}\frac{A_N-\lambda_k I}{\lambda_j-\lambda_k}.
$$
Thus
$$
e^{izNA_N}=\sum_j e^{iN\lambda_jz}P_j.                 \tag{1.2}
$$
Every entry of $U_N(z)^m$ is a finite exponential polynomial to
which (1.1) applies. Repeated sums of eigenvalues are combined before
applying the theorem. Simplicity and rational independence of the
eigenvalues are not assumed.

## 2. Exact Egorov and a dominant coefficient

Put
$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
v_0=(0,7)\pmod N.
$$
The exact identity, with no scalar phase, is
$$
M_N T_N(a,b)M_N^{-1}=T_N(3a+4b,\,2a+3b).              \tag{2.1}
$$

For a direct check, in the kernel of $M_NT_N(a,b)$ change the
summation variable to $z=y+a$. Relative to the phase of
$(M_N)_{xz}$, the additional phase is
$$
\left(\frac{3a}{4}+b\right)z-\frac a4x
-\frac{3a^2}{8}-\frac{ab}{2}.
$$
The extra phase for $T_N(a',b')M_N$ is
$$
\frac{a'}4z+\left(b'-\frac{3a'}4\right)x
-\frac{3(a')^2}{8}+\frac{a'b'}2.
$$
Substitute $a'=3a+4b,\ b'=2a+3b$: all coefficients agree.
The fractions in this kernel calculation mean modular inverses;
$2,4,8$ are invertible since $N$ is odd. This proves (2.1).

The Weyl matrices are linearly independent and satisfy
$$
\operatorname{Tr}\bigl(T_N(v)^*T_N(w)\bigr)
=N\mathbf1_{v=w}.                                    \tag{2.2}
$$
A nonzero shift has zero trace. At zero shift, character
orthogonality gives zero unless the modulation is zero.
Together with the multiplication law this proves (2.2).

The original Fourier prescription gives a decomposition
$$
A_N=\frac12T_N(v_0)+\frac12T_N(-v_0)
+\sum_w r_{w,N}T_N(w),\qquad
\sum_w|r_{w,N}|\le\frac{19}{50}.                      \tag{2.3}
$$
To check the bound directly, expand
$$
r(q)=1+\cos(2\pi q)-\cos(14\pi q)
-\tfrac12\cos(12\pi q)-\tfrac12\cos(16\pi q).
$$
The Fourier coefficient norm $\sum|\widehat r|$ is $4$, and
that of $r-1$ is $3$. After keeping the two displayed coefficients
of $\cos(14\pi q)$, the three remaining terms of $f-1/10$
have coefficient norms at most $3/10,\ 4/100,\ 4/100$.
A sine or cosine has coefficient norm one, and this norm is
submultiplicative. Reducing indices modulo $N$ only combines
coefficients and cannot increase their total absolute mass.
Thus (2.3) holds also in small and composite dimensions.

## 3. An incomplete-orbit estimate for every time

Define
$$
Q_{m,N}=\sum_{j=0}^{m-1}M_N^jA_NM_N^{-j}.
$$
For the dimensions in (T), $v_0\ne0$: among the allowed odd
dimensions only $7$ divides $7$. Let $d$ be the length of
the $S$-orbit of $v_0$. If $a_{w,N}$ are the Weyl
coefficients of $A_N$, equation (2.1) gives the coefficient
of $T_N(v_0)$ in $Q_{m,N}$:
$$
q_{v_0}=\sum_{j=0}^{m-1}a_{S^{-j}v_0,N}.              \tag{3.1}
$$

The visits to $v_0$ occur at $j=0,d,2d,\ldots$, so their
number is exactly $\lceil m/d\rceil$. Every other orbit point
is visited at most this many times. The positive displayed
coefficient at $-v_0$ contributes a nonnegative real number.
For the remaining coefficient mass, (2.3) therefore gives
$$
\boxed{\operatorname{Re}q_{v_0}
\ge\left(\frac12-\frac{19}{50}\right)
       \left\lceil\frac md\right\rceil
=\frac3{25}\left\lceil\frac md\right\rceil>0.}         \tag{3.2}
$$

This proves that $Q_{m,N}$ is not scalar for every $m\ge1$.
No condition $d\mid m$ is needed. The incomplete-orbit count is
what extends the earlier scalar-return argument to arbitrary
algebraic matrix lines.

## 4. Projective evaluation proves the theorem

Suppose $U_N(z_0)^m=cB$, with $B$ algebraic and nonzero.
Invertibility gives $c\ne0$ and invertible $B$. Fix a nonzero
entry $B_{rs}$. For every $i,j$, the exponential polynomial
$$
B_{rs}(U_N(z)^m)_{ij}-B_{ij}(U_N(z)^m)_{rs}
$$
has algebraic coefficients and frequencies and vanishes at $z_0$.
By (1.1) it vanishes identically. Therefore, with the entire function
$c(z)=(U_N(z)^m)_{rs}/B_{rs}$,
$$
U_N(z)^m=c(z)B\qquad(z\in\mathbb C).                  \tag{4.1}
$$
In particular $c(0)\ne0$ and $M_N^m=c(0)B$.
Differentiation at zero gives both
$$
\left.\partial_zU_N(z)^m\right|_0=iNQ_{m,N}M_N^m
$$
and
$$
\left.\partial_zU_N(z)^m\right|_0
=\frac{c'(0)}{c(0)}M_N^m.
$$
Canceling the invertible $M_N^m$ makes $Q_{m,N}$ scalar,
contradicting (3.2). This proves (T).

The initially alleged scalar $c$ was not assumed algebraic.
The projective equations eliminate it before applying
Lindemann--Weierstrass. No trace-zero or determinant restriction
is needed; in particular $N=3,5,9$ are included.

## 5. Exception and exact limitations

At $N=7$, $r$ vanishes at every grid point and every modular
midpoint in the matrix prescription. Hence directly
$$
A_7=\frac9{10}I,\qquad
U_7(z)^m=e^{iz\,7m(9/10)}M_7^m.
$$
The exception in (T) is therefore real.

The theorem rules out exact algebraic return mechanisms at all
positive times. Algebraic matrices are dense, so it alone provides
no uniform distance to their scalar multiples. It does not control
the complete signed trace sums at times of order $N$, does not
assert simple spectrum, and does not prove $H_{\rm diag}$.

