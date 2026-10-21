> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/arithmetic_monomial_reversal_closure.md`. Embedded SHA256: `38462ab5c59f850c507b578b9b63092c452e427b48cdf3812a863434bb3a72f9`.
> [Thematic guide](../../topics/symmetry.md).

# Arbitrary-phase monomial symmetries of the exact kicked family

Date: 21 October 2026.

## 1. Statement and scope

Throughout, $N\geq11$ is odd. The matrices $A=A_N$ and $M=M_N$
are exactly those in the question, with modular inverses in the Weyl
operators and in the quadratic kernel. For real $c,z$, put
$$
 U_c(z)=e^{icNzA}M e^{i(1-c)NzA}.
 \tag{1.1}
$$
The original matrix is $U_1(\tau)$, where
$\tau=10^{-80}$. The choice $c=1/2$ is the symmetric splitting of
the same kick. A monomial matrix is a diagonal matrix times a coordinate
permutation matrix. Its nonzero entries need not be algebraic.

**Theorem 1.** Let $c$ be any real algebraic number and let $z_0\ne0$
be any real algebraic number.

1. No monomial antiunitary $D$, with arbitrary complex phases in its
   nonzero entries, satisfies
   $$
   D U_c(z_0)D^{-1}=\eta U_c(z_0)^{-1}
   \tag{1.2}
   $$
   for any scalar $\eta$.
2. If a monomial unitary $J$, again with arbitrary phases, satisfies
   $$
   J U_c(z_0)J^{-1}=\eta U_c(z_0),
   \tag{1.3}
   $$
   then $\eta=1$ and $J$ is scalar.

This includes all coordinate permutations, all diagonal Jacobi gauges,
all affine shifts, all diagonal chirps, and every composite-modulus
involution $x\mapsto ax$ with $a^2=1\pmod N$. It does not require a
symmetry of $U_c(z_0)$ to preserve $A$ or to reverse $M$ separately.
It also does not assume that the unknown diagonal phases, or their ratios,
are algebraic.

The restriction that $c$ is algebraic is used in the exponential-polynomial
argument below. No assertion for arbitrary transcendental $c$ is made.
The theorem concerns a specified geometric class of operators. Every finite
unitary matrix has an antiunitary reverser obtained from an eigenbasis;
that unrestricted class is not excluded here. Absence of the symmetries in
Theorem 1 implies neither spectral simplicity nor CUE statistics, and does
not prove or disprove $H_{\rm diag}$.

For comparison, the earlier manuscript
`research_continuation_2026_10_20/affine_reversal_and_crt_obstructions.md`,
SHA-256
`856f7e0d7373e1b3c260b20477969a12e3e78886836b11fd4eac9ddd9cc7642c`,
excluded Weyl-normalizing reversal of the original product and common
monomial reversal of its two factors. The present proof removes the
common-factor condition for arbitrary-phase monomial reversers and includes
every algebraic split parameter $c$. All ingredients needed for this
new conclusion are proved below, apart from the precisely cited
Lindemann--Weierstrass theorem.

## 2. Exact matrix facts and two useful support lines

Use frequency coordinates
$$
 W(k,l)=T_N(l,k),\qquad (k,l)\in(\mathbb Z/N\mathbb Z)^2.
 \tag{2.1}
$$
These are the original modular Weyl matrices. No replacement of their
modular half by a real half is made. They satisfy
$$
 \operatorname{Tr}W(k,l)=N\,\mathbf1_{(k,l)=(0,0)}.
 \tag{2.2}
$$
Indeed, a nonzero shift has zero diagonal, and a zero shift reduces the
trace to an additive character sum. The same identity applied to
$W(v)^*W(w)$ shows that the $N^2$ matrices $W(v)$ are an orthogonal
basis of the full matrix algebra.

The matrix $M$ is symmetric and unitary, so
$$
 \overline M=M^{-1}.
 \tag{2.3}
$$
Direct substitution in its kernel gives
$$
 T(a,b)M=M T(3a-4b,-2a+3b).
 \tag{2.4}
$$
For completeness, relative to the phase of $M_{xy}$, the phase of the
left side at $(x,y)$ is
$$
 (b-3a/4)x+(a/4)y+ba/2-3a^2/8,
$$
where all fractions are modular inverses. The corresponding phase of
$MT(a',b')$ is
$$
 -(a'/4)x+(3a'/4+b')y-3(a')^2/8-b'a'/2.
$$
They coincide for $a'=3a-4b, b'=-2a+3b$. Consequently
$$
 M W(v)M^{-1}=W(Sv),\qquad
 S=\begin{pmatrix}3&2\\4&3\end{pmatrix},\quad
 S^{-1}=\begin{pmatrix}3&-2\\-4&3\end{pmatrix}.
 \tag{2.5}
$$

Write $\mathcal D$ for the space of diagonal matrices and
$\mathcal S=M\mathcal D M^{-1}$. Their respective Weyl supports lie on
$$
 L=\{(k,0):k\in\mathbb Z/N\mathbb Z\},\qquad
 SL=\{(3k,4k):k\in\mathbb Z/N\mathbb Z\}.
$$
Since $4$ is a unit modulo odd $N$, the two lines meet only at zero.
Orthogonality of the Weyl basis therefore gives
$$
 \mathcal D\cap\mathcal S=\mathbb C I.
 \tag{2.6}
$$
If $a$ is a unit, neither $(0,1)$ nor $(0,a)$ lies on $L\cup SL$
for $N\geq11$. For example, $(3k,4k)=(0,a)$ would make $k=a/4$
a unit and hence force $N\mid3$.

Let $c_N(k,l)$ denote the coefficient of $W(k,l)$ in $A$, with
frequencies aliased modulo $N$. From the definition of $r$,
$$
 r_0=1,\quad r_{\pm1}=\frac12,\quad r_{\pm7}=-\frac12,
 \quad r_{\pm6}=r_{\pm8}=-\frac14,
 \tag{2.7}
$$
and all other Fourier coefficients of $r$ vanish. The $p$-support of
$A$ consists only of the rows $l=0,1,-1$, and
$$
 c_N(0,1)=\gamma=\frac{-3-4i}{1000},\qquad
 c_N(0,-1)=\overline\gamma.
 \tag{2.8}
$$
There is no alias into $r_0$ because $N\geq11>8$. No uniqueness
claim about other Fourier coefficients is needed in Theorem 1.

For a residue $a$ with $a^2=1$, define
$$
 (P_a\psi)(x)=\psi(ax),\qquad K\psi=\overline\psi.
$$
Directly from (2.1),
$$
 P_a W(k,l)P_a^{-1}=W(ak,al),\qquad
 P_aK W(k,l)(P_aK)^{-1}=W(-ak,al).
 \tag{2.9}
$$
In the antiunitary identity, scalar coefficients are conjugated.

## 3. The only external theorem and its exact use

We use the following form of the Lindemann--Weierstrass theorem:
if $\alpha_1,\ldots,\alpha_s$ are distinct complex algebraic numbers,
then $e^{\alpha_1},\ldots,e^{\alpha_s}$ are linearly independent over
the field of algebraic numbers. A published source is S. A. Popescu,
*A Simple and Self-contained Proof for the Lindemann--Weierstrass Theorem*,
in *New Frontiers in Number Theory and Applications*, Trends in Mathematics,
Springer, 2024, pp. 349--366,
DOI [10.1007/978-3-031-51959-8_16](https://doi.org/10.1007/978-3-031-51959-8_16).
The author's [arXiv version, Theorem 3.2](https://arxiv.org/pdf/2306.14352),
states exactly this form.

**Lemma 3.1 (evaluation is injective).** Suppose
$$
 F(z)=\sum_{j=1}^s b_j e^{\lambda_j z},\qquad
 b_j,\lambda_j\in\overline{\mathbb Q}.
$$
If $z_0\ne0$ is algebraic and $F(z_0)=0$, then $F\equiv0$.

**Proof.** Combine all equal $\lambda_j$. The remaining exponents
$\lambda_jz_0$ are distinct algebraic numbers. Lindemann--Weierstrass
then makes every combined coefficient zero. $\square$

All entries of $A$ and $M$ are algebraic: their defining coefficients
belong to $\mathbb Q(i)$, their phases are roots of unity, and
$N^{-1/2}$ is algebraic. The distinct eigenvalues $\lambda$ of $A$
are therefore real algebraic numbers. Their spectral projections are
algebraic matrices, as is seen from the explicit formula
$$
 \Pi_\lambda=\prod_{\mu\ne\lambda}
                 \frac{A-\mu I}{\lambda-\mu}.
 \tag{3.1}
$$
Thus every entry of $e^{itNzA}$, for algebraic $t$, is a finite sum
of exponentials $e^{itN\lambda z}$ with algebraic coefficients and
algebraic exponents. Products, inverses of these exponentials, and finite
matrix minors have the same property. In particular this applies to
$U_c(z)$, $U_c(z)^{-1}$, and
$$
 U_c^{\flat}(z)
 =e^{-icNz\overline A}\overline M
       e^{-i(1-c)Nz\overline A}.
 \tag{3.2}
$$
The last expression is holomorphic in $z$, and equals
$\overline{U_c(z)}$ when $z$ is real. It is not ordinary entrywise
conjugation at a nonreal value of $z$.

### 3.1. The projective scalar must be one

Cyclicity gives
$$
 p(z):=\operatorname{Tr}U_c(z)
      =\operatorname{Tr}(e^{iNzA}M),
 \tag{3.3}
$$
independently of $c$. Moreover,
$$
 \operatorname{Tr}M=N^{-1/2}\sum_x e_N(-\overline2x^2),
 \qquad |\operatorname{Tr}M|^2=1.
 \tag{3.4}
$$
To verify the second equality, square the absolute value of the sum and
make the invertible change $u=x-y, v=x+y$. The resulting sum is
$\sum_{u,v}e_N(-\overline2uv)=N$, by additive-character
orthogonality. This holds at every odd composite $N$ as well as at
primes.

It follows that $p(0)\ne0$. Lemma 3.1 then shows
$$
 p(z_0)\ne0\qquad(z_0\ne0\text{ algebraic}).
 \tag{3.5}
$$
Taking traces in (1.2), and using unitarity at real $c,z_0$, gives
$\overline{p(z_0)}=\eta\overline{p(z_0)}$, hence $\eta=1$.
Taking traces in (1.3) gives the same conclusion. No algebraicity of
$\eta$ or of the unknown symmetry is used.

## 4. Eliminating the unknown phases by rank

Fix a coordinate permutation $\pi$, and use the convention
$(P_\pi\psi)(x)=\psi(\pi(x))$. For a coefficient vector
$d=(d_x)_{x\bmod N}$, set
$$
 J_d=\operatorname{diag}(d_x)P_\pi.
$$
Either of the matrix equations
$$
 J_d U_c^{\flat}(z)=U_c(z)^{-1}J_d
 \tag{4.1}
$$
or
$$
 J_d U_c(z)=U_c(z)J_d
 \tag{4.2}
$$
is a homogeneous linear system $B_\pi(z)d=0$ with $N^2$ rows and
$N$ columns. Every entry of $B_\pi(z)$, and every one of its minors,
has the exponential-polynomial form of Lemma 3.1. This assertion does
not involve the unknown $d_x$.

If a nonzero solution exists at $z=z_0$, every $N$-column maximal
minor vanishes there. Lemma 3.1 implies that all these minors vanish
identically. Consequently
$$
 \operatorname{rank}B_\pi(z)\leq N-1\quad\text{for every complex }z.
 \tag{4.3}
$$

### 4.1. Classification of the kernel at zero

At $z=0$, (4.1) reduces to $J_d\overline M=\overline M J_d$,
and (4.2) reduces to $J_dM=MJ_d$. The following argument is identical
for $M$ and $\overline M$; write $F$ for either one. Reindexing
the column by $\pi(y)$, the equation is
$$
 d_x F_{\pi(x),\pi(y)}=d_y F_{x,y}.
 \tag{4.4}
$$
All entries of $F$ are nonzero. If any $d_y\ne0$, (4.4) forces
all $d_x\ne0$. The ratio $d_x/d_y$ is a quotient of two kernel
phases and is therefore an $N$-th root of unity. Symmetry of $F$,
applied to (4.4) with $x,y$ exchanged, also gives
$$
 (d_x/d_y)^2=1.
$$
Since $N$ is odd, $d_x=d_y$ for all $x,y$. Thus
$$
 F_{\pi(x),\pi(y)}=F_{x,y}.
 \tag{4.5}
$$
Putting $y=x$ in the explicit quadratic kernel gives
$\pi(x)^2=x^2\pmod N$, since its diagonal coefficient is
$\mp\overline2$. Subtracting the squared terms from (4.5) then
gives
$$
 \pi(x)\pi(y)=xy\pmod N.
 \tag{4.6}
$$
Set $a=\pi(1)$. Then $a^2=1$, so $a$ is a unit and
$\pi(x)a=x$ implies $\pi(x)=ax$. Conversely every such $P_a$
commutes with $M$ and $\overline M$, since its quadratic kernel
is unchanged by simultaneous multiplication of $x,y$ by $a$.

This proves the full classification:
$$
 \ker B_\pi(0)\ne\{0\}\quad\Longleftrightarrow\quad
 \pi(x)=ax,\quad a^2=1,
 \tag{4.7}
$$
and the nonzero kernel is precisely the one-dimensional space of
constant $d$. This includes all CRT solutions of $a^2=1$, not
merely $a=\pm1$. It simultaneously rules out nonzero affine shifts
and nonconstant diagonal chirps at $z=0$; no unproved classification
of monomial metaplectic operators is being invoked.

### 4.2. A local analytic solution, without unitarity

Suppose (4.3) holds. Classification (4.7) gives a permissible $a$ and
$\operatorname{rank}B_\pi(0)=N-1$. The columns other than column zero
are linearly independent at zero, because the kernel at zero consists
only of constant vectors. Choose $N-1$ rows on which those columns
form an invertible square matrix. Set $d_0(z)=1$ and solve those rows
for the remaining $d_x(z)$ by matrix inversion. Near zero this gives
an analytic vector with
$$
 d_x(0)=1\quad\text{for every }x.
$$
The remaining rows vanish as well: the selected rows have rank $N-1$,
while the full rank is at most $N-1$ by (4.3). Thus
$$
 J(z)=\operatorname{diag}(d_x(z))P_a
 \tag{4.8}
$$
is an invertible analytic solution of the full relevant intertwining
equation near $z=0$, with $J(0)=P_a$.

The branch $J(z)$ is not required to be unitary, even for real $z$.
In particular
$$
 Q=\frac{J'(0)P_a^{-1}}{iN}
 \tag{4.9}
$$
is an arbitrary complex diagonal matrix. The support argument below
uses only its diagonality.

## 5. Proof of the antiunitary exclusion

Suppose that (1.2) holds. Section 3.1 gives $\eta=1$. Write
$D=J_dK$, with the unknown diagonal phases in $J_d$. Its equation
is (4.1) at $z_0$. Sections 4.1--4.2 therefore give an analytic
solution (4.8) near zero. Put
$$
 A_D=P_a\overline A P_a^{-1}.
$$
Differentiate (4.1) at zero, or equivalently differentiate
$J(z)U_c^{\flat}(z)J(z)^{-1}=U_c(z)^{-1}$. Since
$$
 (U_c^{\flat})'(0)
 =-iN\{c\overline A M^{-1}+(1-c)M^{-1}\overline A\},
$$
$$
 (U_c^{-1})'(0)
 =-iN\{(1-c)A M^{-1}+cM^{-1}A\},
$$
the differentiated equation, multiplied on the left by $M$, is
$$
 \boxed{\operatorname{Ad}_M Q-Q
 =c\operatorname{Ad}_M A_D+(1-c)A_D
   -(1-c)\operatorname{Ad}_M A-cA.}
 \tag{5.1}
$$
Here $\operatorname{Ad}_M X=MXM^{-1}$. To check the positions of
the factors explicitly, before multiplication by $M$ the equation is
$$
 QM^{-1}-M^{-1}Q-cA_DM^{-1}-(1-c)M^{-1}A_D
 =-(1-c)AM^{-1}-cM^{-1}A.
$$

The $p$-support of $A_D$ is $l=0,\pm a$, by (2.9).
The coefficient of $\operatorname{Ad}_M A$ at $(0,1)$ is zero:
its preimage under $S$ is $(-2,3)$, outside $l=0,\pm1$.
The coefficient of $\operatorname{Ad}_M A_D$ there is also zero.
Indeed, its preimage in the original support of $A$ is
$(2a,3a)$. If $3a=0\pmod N$, the unit property of $a$ would
give $N\mid3$. If $3a=\pm1\pmod N$, squaring and using $a^2=1$
would give $N\mid8$. These cases are impossible for odd $N\geq11$.
The left side of (5.1) has zero coefficient at $(0,1)$ by Section 2.
Consequently
$$
 (1-c)c_{A_D}(0,1)-c\gamma=0.
 \tag{5.2}
$$

### 5.1. Composite involutions other than $\pm1$

If $a\ne1,-1\pmod N$, the $p$-support of $A_D$ makes
$c_{A_D}(0,1)=0$. Equation (5.2) forces $c=0$. At $c=0$,
(5.1) is
$$
 \operatorname{Ad}_M Q-Q=A_D-\operatorname{Ad}_M A.
 \tag{5.3}
$$
Now inspect its coefficient at $(0,a)$. The left side is zero since
this index is outside $L\cup SL$. The $A_D$ coefficient is
$\overline\gamma\ne0$, from the original index $(0,1)$.
The coefficient of $\operatorname{Ad}_M A$ vanishes: its preimage
$(-2a,3a)$ has forbidden $p$-coordinate by the same unit and
squaring argument. This is a contradiction. In particular no exceptional
CRT involution survives.

### 5.2. The involution $a=1$

Here $c_{A_D}(0,1)=\overline\gamma$, so (5.2) says
$$
 (1-c)\overline\gamma-c\gamma=0.
$$
Writing $\gamma=u+iv$, its left side is $u(1-2c)-iv$.
Since $c$ is real and $v=-4/1000\ne0$, this is impossible.

### 5.3. The involution $a=-1$

Now $c_{A_D}(0,1)=\gamma$, so (5.2) forces $c=1/2$.
In this case the difference $W=A_D-A$ is diagonal. To verify this
exactly, including boundary links, note that the mixed Fourier
coefficients are $\gamma r_k$ on $l=1$ and
$\overline\gamma r_k$ on $l=-1$, with real $r_k$.
The antiunitary map in (2.9) for $a=-1$ sends $(k,l)$ to
$(k,-l)$ and conjugates coefficients. Every mixed term is therefore
unchanged. On $l=0$ it reverses the odd sine term, giving
$$
 W_{xx}=w(x/N),\qquad
 w(q)=-\frac{r(q)\sin(2\pi q)}{50}.
 \tag{5.4}
$$
This Fourier verification uses the original modular Weyl matrices,
so no boundary-flux assumption is implicit in it. Equivalently, the
upper Jacobi link of $A$ is
$$
 A_{x,x+1}=\frac{e^{-i\alpha_0}}{200}
       r\!\left(\frac{x+h_N}{N}\right),\qquad h_N=(N+1)/2,
$$
and reflection followed by conjugation gives the same link because
$r$ is even and $2h_N-1=N$.

The diagonal matrix $W$ has trace zero, since $w(-q)=-w(q)$ and
the grid is invariant under $x\mapsto-x$. It is not zero: at
$q=1/N$, all three factors $1-\cos(14\pi/N)$,
$1+\cos(2\pi/N)$, and $\sin(2\pi/N)$ are positive for
$N\geq11$.

Equation (5.1) at $c=1/2$ becomes
$$
 \operatorname{Ad}_M Q-Q=\frac12(W+\operatorname{Ad}_M W),
$$
or
$$
 \operatorname{Ad}_M(Q-W/2)=Q+W/2.
 \tag{5.5}
$$
The left side lies in $\mathcal S$; the right side lies in
$\mathcal D$. By (2.6), both are scalar. Hence $Q-W/2$ and
$Q+W/2$ are scalar, so $W$ is scalar. Its trace zero would then
give $W=0$, contrary to (5.4). This finishes the proof of part 1.

## 6. Proof of the unitary commutant assertion

Suppose (1.3) holds. Its projective scalar is one by Section 3.1.
Apply the same maximal-minor argument to (4.2). The analytic branch
near zero has $J(0)=P_a$, $a^2=1$. Put
$$
 A_a=P_a A P_a^{-1},\qquad X=A_a-A,
$$
and define the complex diagonal $Q$ by (4.9). Differentiating (4.2)
at zero, then multiplying on the right by $M^{-1}$, gives
$$
 \operatorname{Ad}_M Q-Q=cX+(1-c)\operatorname{Ad}_M X.
 \tag{6.1}
$$

If $a\ne1,-1$, then $c_X(0,1)=-\gamma\ne0$. If $a=-1$,
then $c_X(0,1)=\overline\gamma-\gamma\ne0$. In both cases
the coefficient of $\operatorname{Ad}_M X$ at $(0,1)$ vanishes:
the preimages for $A$ and $A_a$ have $p$-coordinates $3$
and $3a$, respectively. The previous modular argument excludes
both. The left side of (6.1) also vanishes there, so $c=0$.

At $c=0$, inspect (6.1) at $S(0,1)=(2,3)$. This index is
outside $L\cup SL$: it is not on $L$, and invertibility of $S$
would otherwise put $(0,1)$ on $L$. Thus the left side is zero,
whereas the right side has coefficient $c_X(0,1)\ne0$. This
contradiction leaves only $a=1$, and hence the original permutation
$\pi$ is the identity.

It remains to show that the diagonal commuting matrix at $z_0$ is
scalar; the analytic branch at zero alone would not establish this.
For $\pi=\mathrm{id}$, the identity matrix belongs to the kernel
of (4.2) for every $z$. At zero that kernel is one dimensional by
Section 4.1. Therefore some $(N-1)$-row and $(N-1)$-column
minor $F(z)$ of $B_{\mathrm{id}}(z)$ satisfies $F(0)\ne0$.
It is an algebraic exponential polynomial, so Lemma 3.1 gives
$F(z_0)\ne0$. The rank at $z_0$ is consequently at least $N-1$,
and is at most $N-1$ because the identity is in the kernel. Its
kernel is exactly the scalar matrices. This proves part 2.

## 7. Consequences for the exact original family and their limits

Take $z_0=\tau=10^{-80}$. It is a fixed nonzero real algebraic
number, so all preceding arguments apply without a small-$\tau N$
assumption. In particular, there is no arbitrary-phase Jacobi gauge,
with or without a coordinate permutation, that reverses the original
$U_N$ or any algebraic symmetric splitting (1.1). This includes all
independent phase choices on the seven Jacobi paths when $7\mid N$.
The obstruction is a statement about the full product with $M_N$,
not merely the flux of an individual path.

The split matrices are unitarily conjugate to the original product.
Writing $E=e^{iNz_0A}$,
$$
 U_c(z_0)=E^{c-1}U_1(z_0)E^{1-c}.
 \tag{7.1}
$$
Hence Theorem 1 also excludes reversers of $U_1(z_0)$ of the form
$$
 E^{1-c}D E^{c-1},
 \tag{7.2}
$$
where $D$ is any monomial antiunitary and $c$ is real algebraic.
Likewise it excludes nonscalar commuting operators of this form with
$D$ monomial unitary. These dressed operators need not have algebraic
entries; the rank argument is applied before the dressing.

The restriction to sufficiently large odd dimensions is harmless for
the asymptotic question but is stated explicitly. At $N=7$,
$A_7=(9/10)I$, and coordinate conjugation does reverse the scalar
kick times $M_7$. Theorem 1 deliberately makes no assertion at
$N=3,5,7,9$.

No estimate of the signed products of traces at times of order $N$
has been deduced here. In particular the missing step for the original
problem remains the weighted cancellation
$$
 \frac1{k!N^k}\sum_{\substack{m\in\mathbb Z^k\\\sum m_a=0}}
 \left(\prod_{a=1}^k\widehat b(m_a/N)\right)
 \left(D_{U_N}(m)-\mathbb E_{\rm CUE}D_{V_N}(m)\right)=o(1)
$$
for every fixed $k\geq2$ and every test function specified in the
question. Theorem 1 removes an exact geometric symmetry mechanism;
it neither supplies that cancellation nor turns symmetry absence into
a universality theorem.
