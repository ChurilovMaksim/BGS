> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/dual_audit_physical_cycle_classes.md`. Embedded SHA256: `953578dbba89c8aa86994c63a9289ffe26803795f2dac7055e3f306bad9d79ae`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit of the all-time physical cycle classes

Round 5, 21 October 2026. Auditor: Weyl-dual branch.

## 1. Frozen objects and verdict

The principal target is root_physical_cycle_classes.md, SHA256
de9d6a510aa9c6e36f30a1d42d7c5e3760e71e594cbf0335a4c1a1653ac7708d.

Its original-family application uses:

- dual_physical_four_branch_kernel.md, SHA256
  0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c;
- root_oscillatory_matrix_cancellation.md, SHA256
  ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d.

**Verdict: the finite-dimensional theorems and their stated all-time
consequences are proved as written.** The two corrections to the reversed
class are distinct and both are necessary; both have been independently
verified. The original-family application is closed by the supplied kernel
and oscillatory inputs. The remaining pair limit in Section 6 of the target
is explicitly an unproved target, not a conclusion of these estimates.

The auditor reconstructed the cycle identities and estimates from their
definitions. This audit did not modify any of the frozen sources.

## 2. Correct phase convention and disjoint classes

For a rooted word $x=(x_0,\ldots,x_{n-1})$, the amplitude
$$
 a(x)=\prod_{j=0}^{n-1}U_{x_j,x_{j+1}},\qquad x_n=x_0,
$$
is the convention in the ordinary expansion of $\operatorname{Tr}U^n$.
It is invariant under cyclic rotations since its factors are complex
numbers. The set of distinct rotations has cardinality $d(x)$, the
least period of the word, and $d(x)\mid n$.

For $Rx=(x_0,x_{n-1},\ldots,x_1)$, multiplication of the entries
$$
 Q_{uv}=U_{uv}\overline{U_{vu}}
$$
along the word gives exactly $a(x)\overline{a(Rx)}$. This verifies the
orientation used in the reversed path sum. Reversal preserves the period
and hence the number of distinct rotations.

The three definitions in target equation (4) are disjoint sets of ordered
pairs $(x,y)$, not a multiset of specified rotation operations. They
partition all ordered pairs. Their total is exactly
$|\operatorname{Tr}U^n|^2$. Swapping $x,y$ preserves each set and
conjugates its summand, so each aggregate is real. Positivity is asserted
only for the forward class and for the overlap removed from the reversed
class, where it is correct.

## 3. The forward class and the all-time $O(1)$ error

Let $P_{uv}=|U_{uv}|^2$ and $J_{uv}=1/N$. Under the target hypotheses
$\max P_{uv}\le C/N$, $P$ is doubly stochastic and every entry of every
power $P^d$, $d\ge1$, is at most $C/N$. Indeed multiplication on the
left by a stochastic matrix makes a convex combination of the entries of
each column. Therefore $\operatorname{Tr}P^d\le C$.

The exact formula is
$$
 D_n=\sum_xd(x)|a(x)|^2,\qquad
 n\operatorname{Tr}P^n-D_n=\sum_x(n-d(x))|a(x)|^2\ge0.
$$
For each proper divisor $d\mid n$, words with period dividing $d$
are in bijection with words of length $d$, repeated $n/d$ times.
Their total probability weight is at most
$$
 (C/N)^{n-d}\operatorname{Tr}P^d\le C(C/N)^{n-d}.
$$
Every proper divisor is at most $n/2$, and using at most $n$ divisors
with coefficient $n$ gives
$$
 0\le n\operatorname{Tr}P^n-D_n\le Cn^2(C/N)^{n/2}\quad(n\ge2).
$$
This deliberately overcounts words having several divisors of their
period; the terms are nonnegative, so it is a valid upper bound. There
is no correction at $n=1$.

For $z=\sqrt{C/N}\le1/4$,
$$
 \sum_{n\ge2}n^2z^n
 =\frac{z(1+z)}{(1-z)^3}-z\le8z^2.
$$
The quotient by $z^2$ has nonnegative power-series coefficients and
equals $212/27<8$ at $z=1/4$. Thus the entire periodic correction is
at most $8C^2/N$.

Next $PJ=JP=J$, so with $A=P-J$, $P^n=J+A^n$. Orthogonality of the
constant block in Hilbert--Schmidt inner product gives
$$
 \|A\|_{\rm HS}^2=\|P\|_{\rm HS}^2-1
 \le(C/N)\sum_{u,v}P_{uv}-1=C-1.
$$
This is the gain that avoids an unnecessary factor $N$. For $n\ge2$,
$$
 |\operatorname{Tr}A^n|
 \le\|A\|_{\rm HS}\|A^{n-1}\|_{\rm HS}
 \le C\,2^{-(n-2)}.
$$
The first step is ordinary Hilbert--Schmidt Cauchy--Schwarz applied to
$A^*$ and $A^{n-1}$; no normality of $A$ is required. The second
uses the operator-norm ideal inequality and $\|A\|_{\rm op}\le1/2$.
At time one, $|\operatorname{Tr}P-1|\le C+1$.
Since $\sum_{n\ge2}n2^{-(n-2)}=6$, this proves
$$
 \sum_{n\ge1}|D_n-n|
 \le7C+1+\frac{8C^2}{N}.
$$
The absolute convergence concerns $D_n-n$, as the target correctly
states. Neither $D_n$ nor $n$ is summable by itself.

## 4. First reversed correction: duplicate rotations

Let $T_n$ initially include all distinct rotations of $Rx$, including
any forward overlap. Then
$$
 T_n=\sum_xd(x)a(x)\overline{a(Rx)},\qquad
 n\operatorname{Tr}Q^n=\sum_xn\,a(x)\overline{a(Rx)}.
$$
The difference again consists solely of words having a proper period,
but their absolute weights are now controlled by
$$
 S_{uv}=\sqrt{P_{uv}P_{vu}},
$$
not by $P$. This distinction in the target is correct and necessary.
The matrix $S$ is nonnegative symmetric, $\max S_{uv}\le C/N$, and
Cauchy--Schwarz using one row and one column of $P$ gives
$\sum_vS_{uv}\le1$. All its powers are substochastic and have entries
at most $C/N$. Thus $\operatorname{Tr}S^d\le C$.

Repeating the preceding proper-period argument with $S$ proves
$$
 |T_n-n\operatorname{Tr}Q^n|\le Cn^2(C/N)^{n/2},\quad n\ge2,
$$
with zero error at one. Its all-time sum is at most $8C^2/N$. This
step bounds the exceptional terms by their absolute weights only after
the exact class difference has been identified. It makes no
dephasing replacement in the remaining coherent sum.

## 5. Second reversed correction: overlap with forward rotations

Two cyclic rotation classes are either equal or disjoint. Therefore
$$
 I_n:=T_n-R_n
 =\sum_xd(x)\mathbf1_{\{\operatorname{Rot}(Rx)=\operatorname{Rot}(x)\}}
       |a(x)|^2\ge0.
$$
On this set $a(Rx)=a(x)$ exactly, explaining the positive summand.
At $n=1,2$, every reversed word is a rotation, so $R_1=R_2=0$;
this removes the two short-time terms which would not vanish merely
from the large-time estimate for $Q$.

Here is the complete reflection count for $n\ge3$. Equality of the
rotation classes is equivalent to the existence of an integer $j$
modulo $n$ such that
$$
 x_i=x_{j-i}\quad\text{for every }i\pmod n.
$$
The permutation $i\mapsto j-i$ is an involution. For odd $n$ it has
one fixed point, because $2i=j\pmod n$ has one solution. For even
$n$ it has two fixed points when $j$ is even, and none when $j$
is odd. The number of cycles is therefore at most
$\lfloor n/2\rfloor+1$. A fixed word chooses one of the $N$ symbols
independently on each such cycle, so there are at most
$N^{\lfloor n/2\rfloor+1}$ fixed words for a specified reflection.
This assertion concerns the positions in a word and is unrelated to
whether the matrix dimension $N$ is prime.

There are $n$ possible reflections. Using $d(x)\le n$ and
$|a(x)|^2\le(C/N)^n$, the union bound gives
$$
 I_n\le n^2C^nN^{1-\lceil n/2\rceil}.
$$
Repeated counting of a highly symmetric word is harmless here.
Put $v=C^2/N\le1/4$. The odd and even cases sum separately:
$$
 \sum_{\substack{n\ge3\\n\ {\rm odd}}}I_n
 \le C\sum_{k\ge1}(2k+1)^2v^k
 \le27Cv=\frac{27C^3}{N},
$$
because $(2k+1)^2\le9k^2$ for $k\ge1$, and
$\sum k^2v^k=v(1+v)/(1-v)^3<3v$ for $v\le1/4$.
For even $n=2k\ge4$,
$$
 \sum I_n\le4N\sum_{k\ge2}k^2v^k
 \le32Nv^2=\frac{32C^4}{N}.
$$
The standing hypothesis $N\ge16C^2$ is more than sufficient for all
the radii used in these estimates.

## 6. The signed reversed main term and the original-family application

The matrix $Q$ is Hermitian, and
$$
 \|Q\|_{\rm HS}^2=\sum_{u,v}P_{uv}P_{vu}\le C.
$$
If $\rho=\|Q\|_{\rm op}$, then for $n\ge2$,
$|\operatorname{Tr}Q^n|\le C\rho^{n-2}$. Consequently
$$
 \sum_{n\ge3}n|\operatorname{Tr}Q^n|
 \le C\frac{\rho(3-2\rho)}{(1-\rho)^2}\le12C\rho
 \quad(0\le\rho\le1/2).
$$
Together with the two independently checked corrections and the exact
zero values of $R_1,R_2$, this yields precisely
$$
 \sum_{n\ge1}|R_n|
 \le12C\rho+\frac{8C^2+27C^3+32C^4}{N}.
$$

For completeness, the auditor also read and reconstructed the analytic
input ff98c2a2... in full. Its fourth-Schatten expansion has normalization
$4^{-4}$ after Poisson summation on four residue progressions.
The assumed $1/8$ derivative bound excludes every nonzero reciprocal
lattice mode. Six integrations by parts give a summable majorant over
the four-dimensional alias lattice. The zero mode tends to zero by
cutting out the zero-measure critical set of a nonconstant analytic
phase and integrating by parts on its complement. The use of
$\partial_q\partial_r\phi\not\equiv0$ ensures the rectangular phase
is nonconstant.

The off-axis coefficient at $(29/4,1/4)$ is
$-e^{im\pi/2-i\alpha_0}/800$ in the first time derivative of the
phase. It cannot be canceled by a swapped branch. For same-orientation
distinct branches its difference has magnitude at least
$\sqrt2/800$. The two remainders are bounded by $70000t^2$;
the kernel's gradient bounds give rectangular gradients at most
$1400t$ or $800t$. These verify the oscillatory lemma's hypotheses
for every required branch pair.

The supplied kernel 0b8e8a... provides all of that note's previously
listed kernel inputs, including exact residue phases and boundary
gluing. Hence for the original matrices one has, eventually for every
odd $N$,
$$
 \max|U_{xy}|^2\le9/N,\quad
 \|P-J\|\le1/2,\quad \rho_N=\|Q_N\|\longrightarrow0.
$$
Thus the finite theorem may be applied with the fixed $C=9$, after
increasing the dimension threshold. There is no circular dependence:
the kernel uses only the original finite-shift equation, whereas the
oscillatory lemma uses that already constructed kernel.

## 7. Exact scope of the weighted correction and remaining gap

The decomposition gives
$$
 |\operatorname{Tr}U_N^n|^2-n-Z_{n,N}
 =(D_{n,N}-n)+R_{n,N}.
$$
The sum of absolute values of this correction over all positive times
is $O(1)$. Therefore multiplying by arbitrary uniformly bounded
weights and dividing by $N^2$ gives an $O(N^{-2})$ correction.
For an infinite series the assertion concerns the grouped correction.
The source explicitly avoids asserting that its three separate
unweighted terms are summable. With an exponential time weight the
separate series converge: $ |\operatorname{Tr}U_N^n|^2\le N^2$,
$D_n\le Cn$, and the already proved bound for $R_n$ controls $Z_n$.

The test function used in Section 6 of the source is fixed by the prior
checkpoint:
$$
 \varphi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
 I=\int\varphi,\quad u=\mathcal F^{-1}\varphi,\quad
 b_*=|u|^2/(2I^2).
$$
It is an admissible nonnegative Schwartz function. Since $\varphi$
is even, $\widehat b_*=(\varphi*\varphi)/(2I^2)$; this is smooth,
supported in $[-2,2]$, and strictly positive in $(-2,2)$.
The bound $|u|\le I$ and equality at zero give $\sup b_*=1/2$.

At order two, the exact factorial Fourier identity has
$D(m,-m)=|p_m|^2-N$. The CUE value of the nonzero trace moment is
$\min(|m|,N)$: its two-point kernel subtracts the number
$(N-|m|)_+$ of pairs of Fourier indices in $\{0,\ldots,N-1\}$
with the required nonzero difference from the diagonal contribution
$N$. The $m=0$ terms agree exactly. Therefore, with
$w=|\widehat b_*|^2$,
$$
 \Delta_{2,N}(b_*)=N^{-2}\sum_{1\le n<2N}w(n/N)
 [|\operatorname{Tr}U_N^n|^2-\min(n,N)].
$$
Substituting the proved correction yields target equation (26).
The deterministic Riemann sum of
$N^{-2}w(n/N)(n-N)_+$ converges to
$\int_1^2(u-1)w(u)\,du>0$. Thus the required limiting value of the
remaining $Z$-sum is indeed the negative of this strictly positive
integral. The source does not prove that value. Declaring all the
remaining normalized off-diagonal contributions negligible would
contradict the necessary value above the Heisenberg threshold.

## 8. Supplementary finite checks

An exact Python enumeration checked all 2046 binary words of lengths
one through ten. It verified the equivalence between equality of the
forward and reversed rotation classes and invariance under at least
one reflection, the disjoint-or-identical property of the classes,
the period divisibility, and the special lengths one and two.
The reflection-cycle bound was checked for each position reflection
in the same range. Rational arithmetic also checked $212/27<8$
and the geometric-series constant below three.

These finite checks support the audit of the definitions and small-time
cases. They do not substitute for the arbitrary-$n,N$ arguments
given above. No numerical spectral experiment or parameter
randomization is used in this audit.

