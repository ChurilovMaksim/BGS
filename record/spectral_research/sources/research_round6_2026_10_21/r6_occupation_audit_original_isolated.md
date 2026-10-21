> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_occupation_audit_original_isolated.md`. Embedded SHA256: `9b0af6c7c2b04ce183ac7f107de50e928d79aa2bc542631db7278e7aa97d9616`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: original isolated unequal-occupation classes

21 October 2026. Audit by the occupation branch, from the definitions and raw proof, without relying on the companion computation.

Audited source: r6_original_isolated_cross_occupation.md.

SHA256 of the audited source:

81e6edcb3a7bc50cd9b5ccb190a03510523428fb0ca12030cd7ad06d46ff1bf4

## Verdict

Theorems A and B, their all-time weighted bounds, and the constant $1080$ for $C=9$ are correct under their stated one-step hypotheses. The proof really concerns specified signed subsets of the original unequal-occupation sum. The torus integral in Theorem A removes exactly the equal-occupation pairs from that class; it is not an ensemble replacement.

No correction to the author's mathematical statement is needed. The $n=3$ bound is deliberately nonsharp, which does not affect any stated constant. The two theorem classes may overlap, so their separate signed estimates cannot simply be added to estimate a union; the source explicitly handles this scope issue.

## 1. Reconstruction of the fixed-pattern contraction

For a nonempty literal mismatch set $I=\{j_1,\ldots,j_r\}$, all successive cyclic gaps satisfy $g_i\ge2$. At mismatch $j_i$, both its predecessor $a$ and successor $b$ are common to the two words. The two-edge amplitude for changed labels $u\ne v$ is exactly
$$
 U_{au}U_{ub}\overline{U_{av}U_{vb}}.
$$
Its phase is $z_u/z_v$. Summing changed labels gives the source's matrix
$$
 D(z)_{ab}=\sum_{u\ne v}
 U_{au}U_{ub}\overline{U_{av}U_{vb}}\,z_u/z_v.
$$
The common segment from the successor of defect $j_i$ to the predecessor of the next defect has $g_i-2$ edges, not $g_i-1$. Summing it gives $P^{g_i-2}$. Thus, with $\ell_i=g_i-2$,
$$
 F_I(z)=\operatorname{Tr}(D(z)P^{\ell_1}\cdots D(z)P^{\ell_r}).
$$

This is a contraction of a fixed rooted graph. The root positions $0,\ldots,n-1$ already belong to the actual words. Writing the trace by starting just before a chosen defect merely orders the same finite contraction; it does not introduce an additional marked defect or a factor $n/r$. Choosing another defect to display first cyclically permutes the matrix factors.

For a gap $g_i=2$, the two neighboring two-edge defect blocks share their intervening common vertex, but they do not share an edge. The factor $P^0=I$ identifies that vertex correctly.

For $n=2$ and $r=1$, predecessor and successor are the same common vertex $a$, so the actual contribution is
$$
 \sum_a\sum_{u\ne v}
 U_{au}U_{ua}\overline{U_{av}U_{va}}\,z_u/z_v
 =\operatorname{Tr}D(z).
$$
This is precisely the $\ell_1=0$ instance, and there are two possible literal singleton mismatch sets, one at each root position.

At a common position, the two word occupations cancel. All remaining phase factors are $z_{x_j}/z_{y_j}$ at the mismatch positions, so their product is exactly $z^{d(x)-d(y)}$. Repeated visits to a coordinate, including a changed label equal to a neighboring common label, cause no exception.

## 2. Stochastic cancellation is exact

The identity
$$
 D(z)=|UZU|^2-P^2
$$
uses entrywise squared moduli. Both terms are nonnegative doubly stochastic, because $UZU$ is unitary. Hence $DJ=JD=0$.

Let $E=P-J$. Since $PJ=JP=J$, for every integer $\ell\ge1$,
$$
 P^\ell=J+E^\ell.
$$
Every such $J$ term adjacent to a $D$ vanishes. Therefore all positive-length common arcs can be replaced by $E^\ell$. When $\ell=0$, the factor remains the identity $I=E^0$; no incorrect equation $P^0=J+E^0$ is used.

A nonnegative doubly stochastic matrix has $\ell^2$ norm at most one by row Jensen followed by its column sums. It leaves both the constant line and its orthogonal complement invariant. Therefore
$$
 \|D(z)\|\le\||UZU|^2-J\|+\|E^2\|
 \le1+(1/4)^2=17/16.
$$
The separate bounds on every absolute row and column sum of $D$, at most two, also follow directly from its difference of two stochastic matrices. These facts are uniform in all phases and require no normality of $P$.

## 3. Occupation projection and counting are normalized correctly

Each actual pair determines a unique literal set $I(x,y)$. Summing fixed-$I$ contractions consequently counts each legal pair once. Torus integration kills exactly the nonconstant occupation differences. Thus
$$
 \Omega_n^{\rm iso}=F_n(\mathbf1)-\int_{\mathbb T^N}F_n(z)\,dz
$$
is correct, including its absence of a normalization factor.

For the number $c^{(g)}_{n,r}$ of literal cyclic subsets, distinguish one selected position. It has $n$ possible labels, and the ordered excess gaps $g_i-g\ge0$ sum to $n-gr$. Their number is
$$
 \binom{n-gr+r-1}{r-1}.
$$
Every subset has exactly $r$ possible distinguished selected positions, even if it is periodic. This gives
$$
 c^{(g)}_{n,r}
 =\frac nr\binom{n-(g-1)r-1}{r-1}.
$$
This factor belongs only to the number of mismatch sets and is not added again to an individual trace contraction.

For the transfer count, a transition $0\to g-1$ marks the current selected position and the following $g-1$ positions are forced unselected. A legal labeled cyclic subset yields exactly one closed state sequence; the empty set gives the constant state-zero path. This proves
$$
 1+\sum_{r\ge1}c^{(g)}_{n,r}w^r=\operatorname{Tr}T_g(w)^n
$$
also at $n=g$, at $n=gr$, and at $n<g$. In particular a periodic maximally packed subset does not receive an extra factor.

The vector $h_j=\lambda^{-j}$, with $\lambda^g-\lambda^{g-1}=w$, is strictly positive and satisfies $T_gh=\lambda h$. After diagonal similarity and division by $\lambda$, the matrix is row stochastic. Its trace powers are at most $g$, proving $\operatorname{Tr}T_g(w)^n\le g\lambda^n$ without a spectral normality assumption.

## 4. Dimension-free Hilbert--Schmidt reduction in Theorem A

Entry flatness and bistochasticity imply
$$
 \|E\|_{\rm HS}^2
 =\sum_{a,b}P_{ab}^2-1
 \le (C/N)\sum_{a,b}P_{ab}-1=C-1.
$$
For gaps at least three, $m=n-2r\ge r$. At $n\ge4$, every allowed pattern has $m\ge2$, including the singleton pattern.

Select two of the $m$ factors $E$ and cyclically write the trace as $\operatorname{Tr}(E B E C)$. The elementary inequality $|\operatorname{Tr}XY|\le\|X\|_{\rm HS}\|Y\|_{\rm HS}$, valid also without adjoints because it is the Hilbert--Schmidt inner product with $Y^*$, gives
$$
 |\operatorname{Tr}(E B E C)|
 \le\|E\|_{\rm HS}^2\|B\|\|C\|.
$$
All remaining factors contribute only their operator norms. With $q=1/4,d=17/16$, the result is exactly
$$
 |F_I(z)|\le(C-1)d^r q^{n-2r-2}
 =16(C-1)4^{-n}17^r.
$$
This is the source of the absence of a factor $N$; no normalized Hilbert--Schmidt norm is being used.

For the gap-three transfer matrix with $w=17$, the positive root satisfies $\lambda^3-\lambda^2=17$. Its value is strictly less than $3$, since the left side at $3$ is $18$. Summing all literal patterns, and then subtracting the constant Fourier coefficient, gives
$$
 |\Omega_n^{\rm iso}|\le96(C-1)(3/4)^n,\qquad n\ge4.
$$

At $n=3$, there are three singleton patterns. Each contributes $\operatorname{Tr}(DE)$, of modulus at most
$$
 \max_{a,b}|E_{ab}|\sum_{a,b}|D_{ab}|
 \le(C/N)(2N)=2C.
$$
The uniform phase bound therefore gives the claimed $12C$. In fact the constant Fourier coefficient vanishes for each singleton defect, so $6C$ also follows, but the larger stated bound is valid.

The geometric sum is
$$
 96\sum_{n=4}^\infty(3/4)^n=243/2.
$$
For $C=9$, the complete constant is $12\cdot9+(243/2)\cdot8=1080$. These are sums of absolute values of the already contracted signed class totals. They are not absolute sums over individual trajectory amplitudes.

## 5. Polarized gap-two class and its all-time sum

For disjoint $A,B$, let $X=U\Pi_AU$, $Y=U\Pi_BU$, and $D^{AB}=X\circ\overline Y$. Then $XY^*=X^*Y=0$. Their diagonal entries give the zero row and column sums of $D^{AB}$, with conjugation in the column identity.

The diagonal entries of $XX^*=U\Pi_AU^*$ and $YY^*=U\Pi_BU^*$ are nonnegative and add to at most one. Row Cauchy--Schwarz gives absolute row sums at most $1/2$. The same calculation with $X^*X$ and $Y^*Y$ bounds columns. The Schur test consequently gives $\|D^{AB}\|\le1/2$.

At every defect, $x_j\in A$, $y_j\in B$, so labels differ automatically. The original occupation excess of $x$ over $y$ in $A$ equals the number of defects and is positive. No equal-occupation projection is needed for this class.

The fixed-pattern contraction, including zero common-edge lengths and the $n=2$ case, is therefore the trace of $r$ matrices $D^{AB}$ and $n-2r$ matrices $E$, with bound
$$
 N(1/2)^r(1/4)^{n-2r}.
$$
The gap-two count resums to
$$
 Z_n(q,d)=\operatorname{Tr}
 \begin{pmatrix}q&d\\1&0\end{pmatrix}^{n}-q^n,
$$
where $q=1/4,d=1/2$. Here $Z_1=0$, $Z_2=2d$; these provide useful direct checks on the root convention and the $n=2$ factor.

The two eigenvalues are $(1\pm\sqrt{33})/8$; the positive one is below $7/8$ and dominates the other in modulus. This proves the pointwise bound after the two disjoint orientations are included.

For the sharper sum, direct inversion gives
$$
 \sum_{n\ge1}Z_n(q,d)
 =\frac{q+2d}{1-q-d}-\frac q{1-q}
 =\frac{d(2-q)}{(1-q-d)(1-q)}
 =14/3.
$$
Multiplication by $N$ and the two orientations gives $28N/3$. The signs of the negative eigenvalue cause no difficulty: $Z_n$ is nonnegative by its original positive subset count.

## 6. Original-family input and remaining scope

I checked that the invoked round-5 equation (25) is exactly
$$
 \|P_N-J_N\|_{\rm op}\le40000t+o(1),
 \qquad t=\tau/(2\pi),
$$
and that the physical kernel source uses $h=(2\pi N)^{-1}$ and $E_N(t)=e^{itA_N/h}=e^{i\tau N A_N}$. Its column error is $Cth$, its four branch amplitudes give $2\sqrt{1+40000t}/\sqrt N$, and their combination yields the stated eventual bound $3/\sqrt N$. Thus the exact norm and flatness hypotheses required by the present finite proof match the original family. The strict margin $40000t<1/4$, together with the proved $o(1)$, yields $\|P_N-J_N\|\le1/4$ eventually along all odd dimensions.

The full construction of those analytic phases and the oscillatory $o(1)$ is upstream in the named round-5 proofs and their independent audits; this audit does not claim to repeat that entire construction. No stronger one-step input is silently used by Theorems A or B.

The remaining weighted pair discrepancy still contains $\mathcal O_n-\min(n,N)$ and the complementary unequal-occupation class. None of the verified estimates here bounds that full remainder. The author's explicit remaining equation (8.2) correctly records that gap.
