> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_weyl_three_time_resonance_and_exact_recursion.md`. Embedded SHA256: `8f6a660d4bb776c769aa7e96e7a4607609c7a44c06addb494764189e3ef1fbf2`.
> [Thematic guide](../../topics/dephasing.md).

# Exact signed three-time resonance and the nontruncated Weyl recursion

21 October 2026. Round 8, original-family Weyl branch.

## 1. What is proved, and what remains open

For the exact original generator, put

$$
A_j=M_N^jA_NM_N^{-j},\qquad j\in\mathbb Z.
$$

The following signed identity is proved below:

$$
\boxed{\frac1N\operatorname{Tr}(A_jA_{j+1}A_{j+2})
       =-\frac{97}{800000}e_N(12)}
\qquad(N\ge275\text{ odd},\ j\in\mathbb Z).
\tag{1.1}
$$

Consequently,

$$
\boxed{\frac1N\operatorname{Tr}
       \bigl(A_j\,iN[A_{j+1},A_{j+2}]\bigr)
 =\frac{97N}{400000}\sin\frac{24\pi}{N}
 \longrightarrow\frac{291\pi}{50000}>0.}
\tag{1.2}
$$

The equality is independent of $j$, so the limit is uniform even
for starting indices $j=j_N$ that grow arbitrarily with $N$.
Only the time **difference** in this statement is fixed.

This is a concrete signed correlation of the transported original
generator. It identifies an exact coherent cluster that survives the
hyperbolic frequency transport. It does not give a nonzero defect in
$H_{\mathrm{diag}}$, and it does not evaluate the trace functional
of the full exponentiated kick at $m\asymp N$.

Sections 5--7 continue the calculation without truncating the kick.
They establish a local phase formula for the Cayley--Hamilton move
and an exact finite recursion. The recursion has $N^2$ complex
states and retains the unresolved interference. No estimate for that
interference is claimed.

## 2. Exact transport and the required Fourier support

Use the original modular-half Weyl operators

$$
W_N(k,l)=T_N(l,k),\qquad
\omega((k,l),(k',l'))=lk'-kl'.
$$

All labels in identities involving $e_N$ are reduced modulo $N$.
Direct multiplication gives

$$
W_N(u)W_N(v)=e_N(\overline2\,\omega(u,v))W_N(u+v),
\tag{2.1}
$$

where $\overline2$ is the inverse of two, not a real half. Thus

$$
W_N(u)W_N(v)W_N(w)
=e_N\!\left(\overline2[
  \omega(u,v)+\omega(u,w)+\omega(v,w)]\right)W_N(u+v+w).
\tag{2.2}
$$

The exact covariance for the given quadratic kernel is

$$
M_NW_N(k,l)M_N^{-1}=W_N(S(k,l)),
\qquad S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
\tag{2.3}
$$

Here is a direct check of the convention. Let
$Q(x,y)=-\overline8(3x^2-2xy+3y^2)$ be the exponent of
$(M_N)_{xy}$. The entry of $M_NT_N(l,k)$ has exponent
$Q(x,y-l)+k(y-\overline2l)$. The entry of
$T_N(l',k')M_N$ has exponent
$Q(x+l',y)+k'(x+\overline2l')$. Their coefficients of $y$
and $x$ agree for
$l'=4k+3l$, $k'=3k+2l$; their constant terms both equal
$-\overline2kl-3\overline8l^2$ after subtracting $Q(x,y)$.
This proves (2.3) for every odd modulus, including composite ones.

Write $A_N=\sum_{\kappa\in F}c_\kappa W_N(\kappa)$ with the
unaliased finite coefficients specified in the question. Its support
has the following exact form:

$$
\begin{aligned}
F={}&\{(k,0):k\in K_0\}
\ \cup\ \{(k,1),(k,-1):k\in K_1\},\\
K_0={}&\{\pm1,\pm2,\pm5,\pm6,\pm7,\pm8,\pm9\},\\
K_1={}&\{0,\pm1,\pm6,\pm7,\pm8\}.
\end{aligned}
\tag{2.4}
$$

For verification, the Fourier coefficients of $r$ are

$$
r_0=1,\quad r_{\pm1}=\tfrac12,\quad
r_{\pm7}=-\tfrac12,\quad r_{\pm6}=r_{\pm8}=-\tfrac14,
\tag{2.5}
$$

and all others vanish. The pure-position coefficient is

$$
c_{k,0}=\tfrac12\mathbf1_{k=\pm7}
 +\frac{r_k}{10}-\frac{\mathbf1_{k=0}}{10}
 +\frac{r_{k-1}-r_{k+1}}{200i}.
\tag{2.6}
$$

The mixed coefficients are

$$
c_{k,1}=\gamma r_k,
\quad c_{k,-1}=\overline\gamma r_k,
\quad \gamma=\frac{-3-4i}{1000}.
\tag{2.7}
$$

These formulas give (2.4) and the coefficients used below:

$$
c_{1,0}=\frac{10-i}{200},\quad
c_{-6,0}=-\frac12c_{1,0},\quad
c_{-2,0}=\frac{i}{400},\quad
|\gamma|^2=\frac1{40000}.
\tag{2.8}
$$

The coefficients at opposite labels are conjugates. The constant
coefficient is zero. This calculation uses the original modular
basis; no ordinary-half sign has been removed implicitly.

## 3. All four closed triples, with a proof of completeness

By (2.3), the trace in (1.1) for $j=0$ is a sum over
$\kappa_0,\kappa_1,\kappa_2\in F$. A summand has nonzero trace
only if

$$
\kappa_0+S\kappa_1+S^2\kappa_2=0\pmod N.
\tag{3.1}
$$

Since $|k_i|\le9$, $|l_i|\le1$, and
$S^2=\left(\begin{smallmatrix}17&12\\24&17\end{smallmatrix}\right)$,
the two absolute coordinate bounds on the left are respectively
$203$ and $273$. For $N\ge275$, a coordinate divisible
by $N$ in these ranges must be zero. Thus (3.1) is an ordinary
integer equation; no modular solutions have been lost.

Writing $\kappa_i=(k_i,l_i)$, elimination in that equation gives

$$
4(k_0-k_2)=3l_0+l_1+3l_2,
\qquad
4k_1=-24k_2-l_0-3l_1-17l_2.
$$

The second equation modulo four gives
$l_0-l_1+l_2=0$: this expression lies between $-3$ and
$3$, so its only multiple of four is zero. It follows that

$$
l_1=l_0+l_2,\qquad
k_0=k_2+l_1,\qquad
k_1=-6k_2-l_0-5l_2.
\tag{3.2}
$$

There are seven possible pairs $(l_0,l_2)$, since their sum
must still lie in $\{-1,0,1\}$. The resulting support checks
are short enough to give in full.

- For $(l_0,l_2)=(0,0)$, put $t=k_2$. Then
  $k_0=t$, $k_1=-6t$, and both must belong to $K_0$.
  The only possibilities are $t=1,-1$.
- For $(l_0,l_2)=(1,-1)$, one has
  $k_0=k_2=t\in K_1$, $k_1=4-6t\in K_0$.
  The bound $|k_1|\le9$ restricts $t$ to $0,1,2$;
  intersection with $K_1$ leaves $0,1$. Of these only
  $t=1$ works, giving $k_1=-2$.
- The case $(-1,1)$ is the negative of the preceding one and
  gives $t=-1$, $k_1=2$.
- For $(l_0,l_2)=(1,0)$, the conditions are
  $t=k_2\in K_0$, $t+1\in K_1$,
  $-6t-1\in K_1$. The last bound forces $t\in\{-1,0,1\}$.
  The pure support removes zero. For $t=-1$ the middle
  coefficient at $k_1=5$ is absent; for $t=1$ the first
  coefficient at $k_0=2$ is absent. There is no solution.
- For $(l_0,l_2)=(0,1)$, the conditions are
  $t\in K_1$, $t+1\in K_0$, $-6t-5\in K_1$.
  The last bound gives $t\in\{-2,-1,0\}$, and $K_1$
  leaves $-1,0$. For $t=-1$ the first pure coefficient
  would be at zero; for $t=0$ the middle mixed coefficient
  would be at $-5$. Neither exists.
- The two remaining cases are the negatives of these last two and
  also have no solution.

Thus all solutions are exactly

$$
\begin{array}{c|c|c}
\kappa_0&\kappa_1&\kappa_2\\\hline
(1,0)&(-6,0)&(1,0)\\
(-1,0)&(6,0)&(-1,0)\\
(1,1)&(-2,0)&(1,-1)\\
(-1,-1)&(2,0)&(-1,1).
\end{array}
\tag{3.3}
$$

In particular, the pure-position resonance is the concrete relation
$(I-6S+S^2)(1,0)^T=0$, not a probabilistic collision.

## 4. Areas, coefficients, and the exact signed answer

For a closed triple $u+v+w=0$, its area in (2.2) is
$\omega(u,v)$. For the first row of (3.3), the transported
vectors are

$$
u=(1,0),\quad v=(-18,-24),\quad w=(17,24),
$$

and this area is $24$. Negating all three vectors preserves
the area. Because it is even, the exact modular-half phase is
$e_N(\overline2\cdot24)=e_N(12)$ for every odd $N$.
There is no leftover parity sign. The coefficient sum of these
two rows is

$$
2\operatorname{Re}(c_{1,0}^2c_{-6,0})
=-\operatorname{Re}\!\left(\frac{(10-i)^3}{200^3}\right)
=-\frac{97}{800000}.
\tag{4.1}
$$

For the third row, the transported vectors are

$$
u=(1,1),\quad v=(-6,-8),\quad w=(5,7),
$$

whose area is $2$. Its modular phase is $e_N(1)$. Its
coefficient is

$$
\frac\gamma2\cdot\frac{i}{400}\cdot
\frac{\overline\gamma}{2}
=\frac{i}{64000000}.
\tag{4.2}
$$

The fourth row has the same area and the opposite coefficient,
$-i/64000000$. The two mixed contributions therefore cancel
**exactly**, before any absolute value and for every odd modulus.
Equations (4.1)--(4.2) prove (1.1) for $j=0$.

For every integer $j$,
$A_jA_{j+1}A_{j+2}=M_N^j(A_0A_1A_2)M_N^{-j}$, so trace
invariance proves the same equality for that $j$. Since the
three matrices are Hermitian, cyclicity also gives

$$
\frac1N\operatorname{Tr}(A_jA_{j+2}A_{j+1})
=\overline{\frac1N\operatorname{Tr}(A_jA_{j+1}A_{j+2})}.
$$

Multiplying the difference by $iN$ proves (1.2). Its sign is
strictly positive for $N\ge275$, and the limit uses only
$N\sin(24\pi/N)\to24\pi$.

The equality exhibits both phenomena needed in a genuine phase
calculation: a pair of terms that cancels and another pair that
survives with an explicit sign. Declaring all different transported
words decorrelated would lose the second pair.

## 5. The exact kick can be retained without a Taylor truncation

For this section all labels are elements of
$\Lambda_N=(\mathbb Z/N\mathbb Z)^2$. Expand the full kick in
the original Weyl basis:

$$
E_N=e^{i\tau NA_N}=\sum_{\eta\in\Lambda_N}d_N(\eta)W_N(\eta),
\quad
d_N(\eta)=\frac1N\operatorname{Tr}(W_N(\eta)^*E_N).
\tag{5.1}
$$

The Weyl operators form an orthonormal basis for normalized
Hilbert--Schmidt inner product, directly by character orthogonality.
Thus (5.1) is finite and exact, and unitarity gives
$\sum_\eta|d_N(\eta)|^2=1$.

The exact interaction representation is

$$
U_N^m=E_0E_1\cdots E_{m-1}M_N^m,
\qquad
E_j=M_N^jE_NM_N^{-j}
   =\sum_\eta d_N(\eta)W_N(S^j\eta).
\tag{5.2}
$$

Consequently, for every positive integer $m$, with no relation
required between $m$ and $N$,

$$
\begin{split}
\operatorname{Tr}U_N^m
={}&\sum_{\eta_0,\ldots,\eta_{m-1}\in\Lambda_N}
 \left(\prod_{j=0}^{m-1}d_N(\eta_j)\right)
 e_N(\overline2\,\mathcal A(\eta))\\
&\hspace{8mm}\cdot
\operatorname{Tr}\left(W_N(\lambda(\eta))M_N^m\right),\\
\lambda(\eta)&=\sum_{j=0}^{m-1}S^j\eta_j,\\
\mathcal A(\eta)&=\sum_{0\le i<j<m}
                     \omega(S^i\eta_i,S^j\eta_j).
\end{split}
\tag{5.3}
$$

This formula is included to locate the explicit cluster inside a
**nontruncated** representation. It is not itself an estimate of
the spectral functional.

## 6. A local Cayley--Hamilton move, with its full phase change

Because $S^2-6S+I=0$, the change at any three consecutive
positions $j,j+1,j+2$, with arbitrary $h\in\Lambda_N$,

$$
(\eta_j,\eta_{j+1},\eta_{j+2})
\longmapsto
(\eta_j+h,\eta_{j+1}-6h,\eta_{j+2}+h)
\tag{6.1}
$$

preserves $\lambda(\eta)$ in (5.3). Its effect on the full
symplectic area is also local:

$$
\boxed{
\Delta\mathcal A=
\omega\!\left(h,\eta_j+(S-S^{-1})\eta_{j+1}-\eta_{j+2}\right)
-6\omega(h,Sh).}
\tag{6.2}
$$

Here $S-S^{-1}=\left(\begin{smallmatrix}0&4\\8&0\end{smallmatrix}\right)$.
Formula (6.2) is valid modulo every odd $N$, at every position
where the indicated three blocks occur, including when $m\asymp N$.

To prove it write the original three transported vectors as $x,y,z$
and their changes as $a,b,c$, where
$a=S^jh$, $b=-6S^{j+1}h$, $c=S^{j+2}h$. They satisfy
$a+b+c=0$. Thus all area cross terms with vectors before or
after these three consecutive blocks cancel. Expanding only the
three remaining pairs gives

$$
\Delta\mathcal A
=\omega(a,x+y)-\omega(c,y+z)+\omega(a,b).
$$

Symplectic invariance under $S$ turns this exactly into (6.2).
For $h=(1,0)$ and the zero background, the result is $24$,
recovering the pure-position triangle in (3.3).

However the weight also changes from
$d_N(\eta_j)d_N(\eta_{j+1})d_N(\eta_{j+2})$ to

$$
d_N(\eta_j+h)d_N(\eta_{j+1}-6h)d_N(\eta_{j+2}+h),
\tag{6.3}
$$

in addition to the multiplier $e_N(\overline2\Delta\mathcal A)$.
Neither the Cayley--Hamilton identity nor symplectic invariance
identifies these two weights. Thus (6.1) is an exact local change
of summation variables, but it has not become a cancellation or
an exact solvable local relation for the full kick coefficients.
Replacing (6.3) by an equal or independent weight would be an
unproved step.

## 7. The finite recursion and its unresolved quantitative content

Let $v_m(\lambda)$ be the Weyl coefficients of
$L_m=E_0\cdots E_{m-1}$. Then

$$
v_0(\lambda)=\mathbf1_{\lambda=0},
$$

and exact multiplication gives

$$
\boxed{
v_{m+1}(\lambda)=\sum_{\eta\in\Lambda_N}
 v_m(\lambda-\eta)d_N(S^{-m}\eta)
 e_N(\overline2\,\omega(\lambda-\eta,\eta)).}
\tag{7.1}
$$

This is a finite, nontruncated recursion for every $N$. It
has $N^2$ complex coordinates and preserves
$\sum_\lambda|v_m(\lambda)|^2=1$, since right multiplication
by $E_m$ is unitary on matrix Hilbert space. Its trace output is

$$
\operatorname{Tr}U_N^m
=\sum_\lambda v_m(\lambda)
                  \operatorname{Tr}(W_N(\lambda)M_N^m).
\tag{7.2}
$$

The recurrence therefore keeps, rather than removes, the coherent
phases. The norm statement alone gives only the elementary trace
bound $|\operatorname{Tr}U_N^m|\le N$. The local transformation
(6.1) does not currently compress (7.1) to a uniformly bounded
state space or supply a cancellation bound for its output.

The exact three-time identity is useful in auditing a proposed
resummation: it must reproduce the cancellation of the two mixed
triangles and the surviving pure triangle. But summing repetitions
of this cluster while dropping other clusters is not justified.
The best degree-$o(N)$ polynomial approximation obstruction in
the companion file also forbids controlling the full kick by
retaining only a sublinear number of its generator powers in
operator norm.

The first required original-family signed estimate still not
proved here is

$$
\frac1{N^2}\sum_{m\ge1}|\widehat b(m/N)|^2
\left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)
\longrightarrow0
\tag{7.3}
$$

for fixed admissible $b$. In this sum the time is of order
$N$; the compact Fourier support makes the sum finite. A proof
would need a quantitative argument for the fully accumulated
coefficients in (7.1)--(7.2), or another argument for the same
original observable, followed by the higher-order hierarchy.
The explicit local resonance and finite recursion above do not
supply that missing estimate.
