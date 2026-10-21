> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_original_isolated_cross_occupation.md`. Embedded SHA256: `20585b313f25044ae8cab78bdd70edeb3922356788d912666d3f690e5676e68f`.
> [Thematic guide](../../topics/histories.md).

# Exact cancellation of literal isolated substitutions in the original unequal-occupation sector

21 October 2026. This note concerns actual pairs of rooted trajectories for a fixed unitary matrix. It gives an all-time, signed estimate for two precisely defined subsets of its unequal-occupation sector. The number of changed vertices can grow linearly with the length of the trajectory. No quotient by cyclic rotations, choice of marking, typical-word restriction, or substitution of a random matrix model is used.

For the prescribed family, the required one-step estimates are supplied by the proved and independently audited round-5 physical kernel and sampled oscillatory matrix construction. All further arguments in this note are finite-dimensional and proved below.

## 1. Original input and the two conclusions

Let $U$ be an $N$-dimensional unitary matrix. Write
$$
 P_{ab}=|U_{ab}|^2,\qquad J_{ab}=N^{-1},\qquad E=P-J.
$$
Assume
$$
 \|E\|_{\rm op}\le\frac14,\qquad
 \max_{a,b}P_{ab}\le\frac CN,\qquad C\ge1.
 \tag{1.1}
$$
For a rooted cyclic word $x=(x_0,\ldots,x_{n-1})$, with $x_n=x_0$, set
$$
 a(x)=\prod_{j=0}^{n-1}U_{x_jx_{j+1}},\qquad
 d_v(x)=\#\{j:x_j=v\}.
 \tag{1.2}
$$
The full unequal-occupation sum is
$$
 \Omega_n(U)=\sum_{d(x)\ne d(y)}a(x)\overline{a(y)}.
 \tag{1.3}
$$

### 1.1. Arbitrary labels, at least one common edge between defects

For an actual ordered pair $(x,y)$, define its literal mismatch set
$$
 I(x,y)=\{j\in\mathbb Z/n\mathbb Z:x_j\ne y_j\}.
 \tag{1.4}
$$
Let $\mathcal C^{(3)}_n$ consist of the pairs such that:

1. $I(x,y)\ne\varnothing$;
2. every cyclic gap between successive elements of $I(x,y)$ is at least three;
3. $d(x)\ne d(y)$.

For a singleton mismatch set, its unique cyclic gap is $n$. Define
$$
 \Omega_n^{\rm iso}(U)
 =\sum_{(x,y)\in\mathcal C^{(3)}_n}a(x)\overline{a(y)}.
 \tag{1.5}
$$
Thus the two words can differ at any labels, at up to $\lfloor n/3\rfloor$ positions. Consecutive defects have at least two common vertices and one common edge between their two-edge neighborhoods. The pair itself determines all defects, even when words or labels repeat.

**Theorem A.** Under (1.1),
$$
 \Omega_1^{\rm iso}=\Omega_2^{\rm iso}=0,\qquad
 |\Omega_3^{\rm iso}|\le12C,
 \tag{1.6}
$$
and
$$
 \boxed{
 |\Omega_n^{\rm iso}(U)|
 \le96(C-1)\left(\frac34\right)^n,\qquad n\ge4.
 }
 \tag{1.7}
$$
In particular, for any sequence of weights satisfying $|w_n|\le W$,
$$
 \boxed{
 \frac1{N^2}\left|\sum_{n\ge1}w_n\Omega_n^{\rm iso}(U)\right|
 \le
 \frac{W}{N^2}
 \left(12C+\frac{243}{2}(C-1)\right).
 }
 \tag{1.8}
$$
These infinite sums of the signed class totals converge absolutely. We have not asserted absolute convergence after taking the modulus of every individual trajectory weight.

### 1.2. Arbitrary density of isolated polarized defects

Fix any disjoint coordinate sets $A,B\subset\{0,\ldots,N-1\}$. Let $\mathcal C^{AB}_n$ consist of pairs whose nonempty literal mismatch set has every cyclic gap at least two, and for which, at every mismatch,
$$
 x_j\in A,\qquad y_j\in B.
 \tag{1.9}
$$
The words agree at every other position. Put
$$
 S_n^{AB}(U)=
 \sum_{(x,y)\in\mathcal C^{AB}_n}a(x)\overline{a(y)},\qquad
 \Omega_n^{AB}(U)=S_n^{AB}(U)+S_n^{BA}(U).
 \tag{1.10}
$$
The two classes in (1.10) are disjoint. The second is obtained from the first by interchanging $x,y$, so $\Omega_n^{AB}$ is real. Every such pair has different occupations: the excess number of visits of $x$ to $A$ is the strictly positive number of mismatches. The mismatch density is allowed to reach $1/2$.

**Theorem B.** If $\|P-J\|_{\rm op}\le1/4$, then, for $n\ge2$,
$$
 \boxed{
 |\Omega_n^{AB}(U)|\le4N\left(\frac78\right)^n.
 }
 \tag{1.11}
$$
The sharper all-time bound is
$$
 \boxed{
 \sum_{n\ge1}|\Omega_n^{AB}(U)|\le\frac{28}{3}N,\qquad
 \frac1{N^2}\left|\sum_{n\ge1}w_n\Omega_n^{AB}(U)\right|
 \le\frac{28W}{3N}.
 }
 \tag{1.12}
$$
Here $\Omega_1^{AB}=0$. Neither the flat-entry hypothesis nor the value of $C$ is needed for Theorem B. The sets $A,B$ may depend on $N$. They must be chosen once for the class: taking a union over many choices would require separate multiplicity control and is not asserted here.

### 1.3. Application to the exact prescribed $U_N$

The round-5 source
$$
 \text{root\_oscillatory\_matrix\_cancellation.md},
 \quad\text{equation (25),}
$$
proved, for the original modular-half family and its fixed positive time $t=\tau/(2\pi)$,
$$
 \|P_N-J_N\|_{\rm op}\le40000t+o(1).
 \tag{1.13}
$$
The physical kernel source
$$
 \text{dual\_physical\_four\_branch\_kernel.md}
$$
proves the associated column error and the uniform bound $|U_N(a,b)|\le3/\sqrt N$ for every sufficiently large odd $N$. The independent audits are
$$
 \text{audit\_sampled\_oscillatory\_matrix.md},\qquad
 \text{audit\_four\_branch\_physical\_kernel.md}.
$$
These sources and proofs are included in the cumulative research document. In particular, even the upper construction time $10^{-10}$ satisfies $40000\cdot10^{-10}<1/4$, and the actual fixed time is much smaller. Thus (1.1) holds with $C=9$ for every sufficiently large odd $N$, with no averaging and no restriction to primes or a subsequence.

Consequently, the original family satisfies the particularly simple bound
$$
 \boxed{
 \frac1{N^2}\left|
 \sum_{n\ge1}w_{n,N}\Omega_n^{\rm iso}(U_N)\right|
 \le\frac{1080W}{N^2}
 }
 \tag{1.14}
$$
for every uniformly bounded sequence of weights. The value $1080$ equals $12\cdot9+(243/2)\cdot8$.

These results do not prove that the full $\Omega_n(U_N)$ is small. The precise remaining portion is described in Section 8.

## 2. A defect matrix with exact row and column cancellation

For $z=(z_0,\ldots,z_{N-1})\in\mathbb T^N$, let
$$
 Z=\operatorname{diag}(z_0,\ldots,z_{N-1}),\qquad
 Q(z)_{ab}=|(UZU)_{ab}|^2,
$$
and define
$$
 D(z)=Q(z)-P^2.
 \tag{2.1}
$$
All absolute squares here are entrywise and evaluated on the unit torus. Equivalently, every entry is a finite Laurent polynomial:
$$
 D(z)_{ab}
 =\sum_{u\ne v}
 U_{au}U_{ub}\overline{U_{av}U_{vb}}\;z_u z_v^{-1}.
 \tag{2.2}
$$
Indeed, expanding $Q(z)$, the terms $u=v$ sum to
$$
 \sum_u|U_{au}|^2|U_{ub}|^2=(P^2)_{ab},
$$
and their phase weight is one.

The matrix $UZU$ is unitary. Therefore $Q(z)$ and $P^2$ are both nonnegative doubly stochastic matrices. It follows exactly that
$$
 D(z){\bf1}=0,\qquad {\bf1}^{T}D(z)=0,\qquad
 D(z)J=JD(z)=0.
 \tag{2.3}
$$
A nonnegative doubly stochastic matrix $R$ has operator norm at most one on $\ell^2$: Jensen's inequality gives
$$
 \sum_a\left|\sum_bR_{ab}v_b\right|^2
 \le\sum_{a,b}R_{ab}|v_b|^2
 =\sum_b|v_b|^2.
 \tag{2.4}
$$
It preserves the constant line and its orthogonal complement. In particular, $\|Q(z)-J\|_{\rm op}\le1$.

Since $PJ=JP=J$, one has $P^2=J+E^2$. Hence
$$
 D(z)=(Q(z)-J)-E^2,
 \qquad
 \boxed{\|D(z)\|_{\rm op}\le1+\|E\|_{\rm op}^2\le\frac{17}{16}.}
 \tag{2.5}
$$
This stronger estimate, uniform over all $N$ phases, will be useful. We also have the separate entrywise bound
$$
 \sum_b|D(z)_{ab}|\le2,\qquad
 \sum_a|D(z)_{ab}|\le2.
 \tag{2.6}
$$
It follows directly from $D=Q-P^2$ and the row and column sums of the two nonnegative matrices.

## 3. Exact contraction for a fixed literal mismatch set

Let $I=\{j_1,\ldots,j_r\}$ be nonempty, listed in cyclic order, and suppose its successive cyclic gaps $g_1,\ldots,g_r$ are at least two. The sum of these gaps is $n$. Put
$$
 \ell_i=g_i-2\ge0,\qquad
 \sum_{i=1}^r\ell_i=n-2r.
 \tag{3.1}
$$
At a defect position $j_i$, its predecessor $a$ and successor $b$ are shared by $x,y$. Summing the two changed labels $u=x_{j_i}\ne y_{j_i}=v$ gives exactly the matrix entry (2.2). Each edge in a common arc gives
$$
 U_{ab}\overline{U_{ab}}=P_{ab}.
$$
Summing all shared vertices therefore gives the exact finite identity
$$
 \boxed{
 F_I(z):=
 \sum_{I(x,y)=I}a(x)\overline{a(y)}\,
 z^{d(x)-d(y)}
 =\operatorname{Tr}\bigl(D(z)P^{\ell_1}\cdots
 D(z)P^{\ell_r}\bigr).
 }
 \tag{3.2}
$$
The predecessor of the first displayed defect is used to write the trace. Choosing a different displayed first defect only cyclically rotates the trace. No extra factor $n$ or $r$ appears.

Identity (3.2) also covers $\ell_i=0$. In that case the successor of one defect is the predecessor of the next, and the factor $P^0=I$ identifies that shared coordinate. For $n=2$, a single defect has the same predecessor and successor; its contribution is $\operatorname{Tr}D(z)$, again as in (3.2).

At every common vertex the two occupation contributions cancel. Thus the product of the local phase factors in (2.2) is exactly $z^{d(x)-d(y)}$, including all repetitions of labels.

Because $D(z)J=JD(z)=0$, and $P^\ell=J+E^\ell$ for $\ell\ge1$, every positive-length common arc in (3.2) can be replaced by $E^\ell$:
$$
 F_I(z)=
 \operatorname{Tr}\bigl(D(z)E^{\ell_1}\cdots
 D(z)E^{\ell_r}\bigr).
 \tag{3.3}
$$
For $\ell_i=0$ the factor is simply $I=E^0$; the identity $P^0=J+E^0$ is neither true nor used.

## 4. Exact removal of the equal-occupation terms

Let $\mathcal I_n^{(3)}$ be the collection of nonempty literal subsets of $\mathbb Z/n\mathbb Z$ with cyclic gaps at least three, and set
$$
 F_n(z)=\sum_{I\in\mathcal I_n^{(3)}}F_I(z).
 \tag{4.1}
$$
Each actual ordered pair with the prescribed isolated mismatch condition occurs in exactly one summand, since its mismatch set is the literal set (1.4).

Finite Fourier orthogonality on $\mathbb T^N$ gives
$$
 \int_{\mathbb T^N} z^{d(x)-d(y)}\,dz
 ={\bf1}_{\{d(x)=d(y)\}}.
$$
Consequently,
$$
 \boxed{
 \Omega_n^{\rm iso}(U)
 =F_n({\bf1})-\int_{\mathbb T^N}F_n(z)\,dz.
 }
 \tag{4.2}
$$
This is an exact identity for one explicitly specified subset of the original sum. The integral is only its constant Fourier coefficient. No equality between a whole original spectral statistic and an independently phased model is claimed.

Both the class of isolated mismatches and its equal-occupation subcollection are invariant under interchanging $x,y$. Thus the total in (4.2) is real. Uniform phase bounds imply
$$
 |\Omega_n^{\rm iso}(U)|\le
 2\sup_{z\in\mathbb T^N}|F_n(z)|.
 \tag{4.3}
$$

## 5. Counting literal cyclic mismatch sets

For integers $g\ge2$, let $c^{(g)}_{n,r}$ be the number of subsets of $\mathbb Z/n\mathbb Z$ with $r\ge1$ points and all cyclic gaps at least $g$. If $n<gr$, this number is zero. Otherwise
$$
 \boxed{
 c^{(g)}_{n,r}
 =\frac nr\binom{n-(g-1)r-1}{r-1}.
 }
 \tag{5.1}
$$
To prove this, distinguish one point of the subset. Choose its position in $n$ ways. The ordered gaps $g_i\ge g$ sum to $n$, so the number of ordered gap lists is the displayed binomial coefficient. Every literal subset has exactly $r$ choices of its distinguished point. Dividing by $r$ proves the formula, including periodic subsets.

A useful equivalent count includes the empty set. For $w>0$, form the $g$ by $g$ matrix $T_g(w)$, with states $0,\ldots,g-1$, by
$$
 (T_g(w))_{00}=1,\qquad
 (T_g(w))_{0,g-1}=w,\qquad
 (T_g(w))_{j,j-1}=1\quad(1\le j\le g-1),
 \tag{5.2}
$$
and all other entries zero. The transition from $0$ to $g-1$ selects a defect. Its following $g-1$ steps force unselected positions. Every legal labeled cyclic subset corresponds to exactly one closed state path of length $n$. The empty subset corresponds to the path staying at state $0$. Therefore, for $n\ge1$,
$$
 1+\sum_{r\ge1}c^{(g)}_{n,r}w^r
 =\operatorname{Tr}T_g(w)^n.
 \tag{5.3}
$$
This identity counts subsets, not distinguished defects.

Let $\lambda>1$ solve
$$
 \lambda^g-\lambda^{g-1}=w.
 \tag{5.4}
$$
The left side is strictly increasing on $(1,\infty)$, starts at zero, and tends to infinity, so this root exists uniquely. The vector $h_j=\lambda^{-j}$ has strictly positive entries and satisfies $T_g(w)h=\lambda h$. The matrix
$$
 R=\lambda^{-1}\operatorname{diag}(h)^{-1}
 T_g(w)\operatorname{diag}(h)
$$
is consequently nonnegative and row stochastic. Its powers have diagonal entries at most one. Similarity invariance of the trace gives the elementary bound
$$
 0\le\operatorname{Tr}T_g(w)^n
 =\lambda^n\operatorname{Tr}R^n\le g\lambda^n.
 \tag{5.5}
$$

## 6. Proof of Theorem A

First observe that
$$
 \|E\|_{\rm HS}^2
 =\sum_{a,b}P_{ab}^2-1
 \le\frac CN\sum_{a,b}P_{ab}-1=C-1.
 \tag{6.1}
$$
The equality uses $\sum_{a,b}P_{ab}=N$.

For a gap-at-least-three mismatch pattern, let $r=|I|$ and $m=n-2r$. Then $m\ge r$. If $n\ge4$, every allowed nonempty pattern has $m\ge2$: for $r=1$ this is $n-2\ge2$, and for $r\ge2$ it follows from $m\ge r$.

Regard (3.3) as a cyclic product containing $m$ individual factors $E$ and $r$ individual factors $D(z)$. Apply Hilbert--Schmidt Cauchy--Schwarz to any two of the $E$ factors and bound all other factors in operator norm. Explicitly, after a cyclic permutation the product has trace $\operatorname{Tr}(E B E C)$, where $B,C$ consist of the remaining factors, so
$$
 |\operatorname{Tr}(E B E C)|
 \le\|EB\|_{\rm HS}\|EC\|_{\rm HS}
 \le\|E\|_{\rm HS}^2\|B\|_{\rm op}\|C\|_{\rm op}.
$$
With $q=1/4$ and $d=17/16$, this proves the uniform bound
$$
 |F_I(z)|\le(C-1)d^r q^{m-2}
 =16(C-1)4^{-n}\,17^r.
 \tag{6.2}
$$
The cancellation (3.3) was performed before this modulus was taken.

Now use (5.3)--(5.5) with $g=3,w=17$. The root $\lambda$ solves
$$
 \lambda^3-\lambda^2=17.
$$
At $\lambda=3$, the left side is $18$, so $\lambda<3$. Summing (6.2) over the literal subsets, without further marking, yields
$$
 \sup_z|F_n(z)|
 \le16(C-1)4^{-n}\operatorname{Tr}T_3(17)^n
 \le48(C-1)\left(\frac34\right)^n.
 \tag{6.3}
$$
Equation (4.3) proves (1.7).

For $n=3$, there are exactly three singleton mismatch sets. Each gives $\operatorname{Tr}(D(z)E)$. Since $0\le P_{ab}\le C/N$ and $C\ge1$,
$$
 \max_{a,b}|E_{ab}|\le C/N.
$$
Using (2.6),
$$
 |\operatorname{Tr}(D(z)E)|
 \le\frac CN\sum_{a,b}|D(z)_{ab}|\le2C.
$$
Thus $\sup_z|F_3(z)|\le6C$, and (4.3) gives (1.6).

Finally,
$$
 96\sum_{n=4}^\infty(3/4)^n
 =96\,\frac{(3/4)^4}{1-3/4}=\frac{243}{2}.
$$
Summing the bounds proves (1.8).

## 7. Proof of Theorem B and its density-one-half resummation

Let $\Pi_A,\Pi_B$ be the coordinate projections, and write
$$
 X=U\Pi_AU,\qquad Y=U\Pi_BU,\qquad
 D^{AB}_{ab}=X_{ab}\overline{Y_{ab}}.
 \tag{7.1}
$$
Disjointness gives
$$
 XY^*=U\Pi_A\Pi_BU^*=0,\qquad
 X^*Y=U^*\Pi_A\Pi_BU=0.
$$
Taking the corresponding diagonal entries, with complex conjugation where appropriate, proves
$$
 D^{AB}{\bf1}=0,\qquad {\bf1}^TD^{AB}=0.
 \tag{7.2}
$$
For the row absolute sums, Cauchy--Schwarz gives
$$
 \sum_b|D^{AB}_{ab}|
 \le\sqrt{(XX^*)_{aa}(YY^*)_{aa}}
 =\sqrt{(U\Pi_AU^*)_{aa}(U\Pi_BU^*)_{aa}}
 \le\frac12.
 \tag{7.3}
$$
The last step uses nonnegativity and the fact that the two diagonal numbers sum to at most one. For columns, the same argument with $X^*X=U^*\Pi_AU$ and $Y^*Y=U^*\Pi_BU$ gives
$$
 \sum_a|D^{AB}_{ab}|\le\frac12.
$$
The inequality $\|R\|_{\rm op}\le
\sqrt{\|R\|_{\ell^1\to\ell^1}\|R\|_{\ell^\infty\to\ell^\infty}}$, obtained by weighted Cauchy--Schwarz in each row and summing columns, therefore yields
$$
 \boxed{\|D^{AB}\|_{\rm op}\le\frac12.}
 \tag{7.4}
$$

For a fixed literal mismatch set $I$ with cyclic gaps at least two, the exact contraction is now
$$
 \sum_{\substack{(x,y)\in\mathcal C_n^{AB}\\I(x,y)=I}}
 a(x)\overline{a(y)}
 =\operatorname{Tr}\bigl(D^{AB}P^{\ell_1}\cdots
 D^{AB}P^{\ell_r}\bigr)
 =\operatorname{Tr}\bigl(D^{AB}E^{\ell_1}\cdots
 D^{AB}E^{\ell_r}\bigr).
 \tag{7.5}
$$
The same reasoning as in Section 3 covers zero-length common arcs. Thus
$$
 \left|\text{the sum in (7.5)}\right|
 \le N\,d^r q^{n-2r},\qquad d=\frac12,\quad q=\frac14.
 \tag{7.6}
$$

For clarity, the following resummation works for every $0<q<1/2$, provided $\|E\|\le q$, with the same $d=1/2$. Define the exact scalar sum
$$
 Z_n(q,d)=
 \sum_{r\ge1}c^{(2)}_{n,r}d^r q^{n-2r}.
 \tag{7.7}
$$
The two-state matrix
$$
 T(q,d)=\begin{pmatrix}q&d\\1&0\end{pmatrix}
$$
has trace powers
$$
 Z_n(q,d)=\operatorname{Tr}T(q,d)^n-q^n
 =\lambda_+^n+\lambda_-^n-q^n,\qquad
 \lambda_\pm=\frac{q\pm\sqrt{q^2+4d}}2.
 \tag{7.8}
$$
One may prove the trace identity either by (5.3), rescaling the weights, or directly by assigning weight $d$ to the forced defect-and-neighbor pair and $q$ to every remaining common step. Formula (5.1) ensures there is no additional root factor.

For $d=1/2,q=1/4$,
$$
 \lambda_+=\frac{1+\sqrt{33}}8<\frac78,\qquad
 |\lambda_-|<\lambda_+.
$$
Equations (7.6)--(7.8) imply
$$
 |S_n^{AB}|\le N Z_n(q,d)\le2N(7/8)^n.
$$
Interchanging $x,y$ conjugates the value, so (1.11) follows.

For the sharper all-time sum, $q+d<1$, so both eigenvalues have modulus less than one and the geometric matrix series converges. Direct inversion gives
$$
 \begin{aligned}
 \sum_{n=1}^\infty Z_n(q,d)
 &=\operatorname{Tr}\bigl(T(I-T)^{-1}\bigr)
       -\frac q{1-q}\\
 &=\frac{q+2d}{1-q-d}-\frac q{1-q}\\
 &=\frac{d(2-q)}{(1-q-d)(1-q)}.
 \end{aligned}
 \tag{7.9}
$$
At $q=1/4,d=1/2$, this equals $14/3$. Multiplication by $N$, followed by the two disjoint orientations in (1.10), proves (1.12).

## 8. What has and has not been removed

Every pair controlled here has different vertex occupation vectors. It is therefore neither a forward rotation nor a reversed rotation of the same word. It belongs to the actual unequal-occupation sector, irrespective of any earlier partition into forward, reversed, or other pair classes.

The mismatch set is measured in the given common rooting of the two words. We do not additionally choose a relative cyclic shift to maximize their agreement. Every legal pair is counted once in its stated class, and no typical-word assertion is needed. Permitting a further relative shift, or a union over choices of the coloring $A,B$, would define a different class and could create multiplicities.

Theorems A and B cannot in general be added to estimate their union by subtracting an intersection bound without further work: Theorem A includes some of the polarized pairs, and these signed sums do not permit a monotonicity argument. Each theorem is a separate exact sector statement. An explicit disjoint refinement can be defined if needed; no such refinement is silently imposed.

The original pair discrepancy remains exactly
$$
 \Delta_{2,N}(b)=\frac1{N^2}\sum_{n\ge1}
 |\widehat b(n/N)|^2
 \{\mathcal O_n(U_N)-\min(n,N)+\Omega_n(U_N)\}.
 \tag{8.1}
$$
For example, using Theorem A alone permits the exact replacement
$$
 \Omega_n=\Omega_n^{\rm iso}+\Omega_n^{\rm rest},
 \qquad
 \Omega_n^{\rm rest}:=
 \sum_{\substack{d(x)\ne d(y)\\(x,y)\notin\mathcal C_n^{(3)}}}
 a(x)\overline{a(y)}.
$$
The total weighted contribution of $\Omega_n^{\rm iso}$ in (8.1) is $O(N^{-2})$ with the explicit constant (1.14). The estimate still required is
$$
 \frac1{N^2}\sum_{n\ge1}|\widehat b(n/N)|^2
 \{\mathcal O_n(U_N)-\min(n,N)+\Omega_n^{\rm rest}(U_N)\}
 \longrightarrow0.
 \tag{8.2}
$$
This includes pairs with adjacent mismatches, longer changed segments, or independent ordering changes. Nothing in the present argument controls all of them. The higher-order requirements in $H_{\rm diag}$ also remain. The conclusions are genuine new cancellations in the original expansion, not a proof of universality or its negation.

## 9. Verification scope

The companion exact-arithmetic script tests the literal cyclic subset counts against direct enumeration and transfer-matrix traces. It also enumerates actual pairs for small unitary examples, verifies mismatch uniqueness, computes their occupation Laurent polynomial, and compares it with (3.2), (4.2), and the polarized version (7.5). These checks test normalization, phase placement, and repeated-label cases. The estimates for the prescribed all-odd family follow from the proofs and the round-5 input, not from numerical experiments.

The script completed successfully with 400 exact cyclic-count identities, 599 full Laurent-polynomial identities, and 506476 actual ordered pair enumerations. The models were a nonflat rational two-dimensional rotation with $\|P-J\|=41/841<1/4$, a three-dimensional Householder matrix, and a flat four-dimensional Hadamard matrix. In the last model the entire gap-three phase polynomial vanishes exactly, while the polarized gap-two sum at $n=6$ is nonzero. Thus the checks include nonzero cancellation and repeated-label cases rather than only empty or trivial classes.
