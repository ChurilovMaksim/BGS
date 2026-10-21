> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_dense_higher_block_involution.md`. Embedded SHA256: `4a59d67a8196ae73555f6bea28b70c5566c76f0c4d24a160eb87e809a28b79ab`.
> [Thematic guide](../../topics/histories.md).

# Dense cancellation by higher-block lifting, and its exact connected-cycle defect

21 October 2026, round 6. This note concerns the prescribed matrices at
the fixed parameter $\tau=10^{-80}$. The algebraic identities hold
for every finite matrix; the quantitative mass statement applies to
the original family along all sufficiently large odd dimensions.

This is not a proof or disproof of $H_{\rm diag}$. The contribution
of this investigation is an explicit, unmarked, phase-preserving
involution for dense physical pseudoorbits and an exact formula for
what fails when one projects it to a single cycle. A quantitative
original-family statement shows that the affected single-cycle sector
has essentially all of the positive path mass on Heisenberg times.
No historical priority is claimed for higher-block presentations,
Sylvester's determinant identity, or determinant pseudoorbit expansions.

The round-2 pseudoorbit cutoff already used determinant truncation.
The present note does not count that truncation as a new spectral
estimate. Its additional content is the concrete physical-word
involution, its cycle-fugacity defect, and the mass estimate in §6.

## 1. Higher-block transfer without approximating the matrix

Let $U$ be an $N\times N$ matrix, and let
$\mathcal V_K=\{0,\ldots,N-1\}^K$. For $K\ge2$ define

$$
(B_K)_{u,v}
=\mathbf1_{\{(u_2,\ldots,u_K)=(v_1,\ldots,v_{K-1})\}}
U_{u_K,v_K},
\qquad B_1=U.                                             \tag{1.1}
$$

Indices in this section run from 1 within a block. These matrices are
not claimed to be unitary. They are finite lifts of the exact physical
matrix, with all phases unchanged.

Closed length-$n$ walks in $B_K$ are in bijection with rooted
cyclic words $x=(x_0,\ldots,x_{n-1})$: the lifted state at time $j$
is

$$
(x_j,x_{j+1},\ldots,x_{j+K-1}),
$$

with cyclic physical indices. The product of lifted weights is
$\prod_j U_{x_j,x_{j+1}}$, since shifting the index of this cyclic
product by $K-1$ changes nothing. The converse follows by overlapping
successive blocks. This remains valid when $n<K$. Consequently

$$
\operatorname{Tr}(B_K^n)=\operatorname{Tr}(U^n)
\qquad(n\ge1).                                           \tag{1.2}
$$

There is also a direct finite determinant reduction. Define rectangular
matrices indexed by $u\in\mathcal V_K$, $a\in\mathcal V_{K-1}$:

$$
R_{u,a}=\mathbf1_{\{\operatorname{suffix}_{K-1}(u)=a\}},
\qquad
S_{a,v}=\mathbf1_{\{\operatorname{prefix}_{K-1}(v)=a\}}
U_{a_{K-1},v_K}.
$$

Then $RS=B_K$ and $SR=B_{K-1}$, entry by entry. Eliminating either
off-diagonal block in

$$
\begin{pmatrix}I&zR\\S&I\end{pmatrix}
$$

gives $\det(I-zRS)=\det(I-zSR)$. Thus

$$
\boxed{\det(I-zB_K)=\det(I-zU).}                           \tag{1.3}
$$

No convergence of an infinite expansion or limit in $K$ is used.

## 2. Genuine unmarked pseudoorbits and a cycle variable

A pseudoorbit at level $K$ is a subset $S\subset\mathcal V_K$
together with a permutation $\pi:S\to S$ for which every used
matrix entry $(B_K)_{u,\pi(u)}$ is nonzero. Its components are the
cycles of $\pi$. Empty pseudoorbits are allowed. Write

$$
c(\pi)=\text{number of cycles},\qquad
a(S,\pi)=\prod_{u\in S}(B_K)_{u,\pi(u)}.
$$

Every such pair $(S,\pi)$ occurs exactly once. There is no choice of
root, first component, component order, or artificial edge label.
In physical words these are collections of cycles whose cyclic
length-$K$ blocks are globally distinct, across all components.

Introduce the finite polynomial

$$
\mathscr Z_K(z,t)=
\sum_{S,\pi}(-t)^{c(\pi)}z^{|S|}a(S,\pi).                 \tag{2.1}
$$

Terms with a zero edge could equivalently be included with weight
zero. Since
$\operatorname{sgn}\pi=(-1)^{|S|-c(\pi)}$,
the principal-minor expansion gives

$$
\mathscr Z_K(z,1)=\det(I-zB_K)=\det(I-zU).                \tag{2.2}
$$

The coefficient $-[t]\mathscr Z_K(z,t)$ is the generating
polynomial of unrooted single cycles with distinct cyclic
$K$-blocks. It is not the complete logarithm of the determinant.
The latter also includes repeated visits to lifted states.

## 3. The explicit phase-preserving involution

Fix any ordering of $\mathcal V_K$, for example lexicographic order.
Call a pseudoorbit bad if $S$ contains two distinct states with
the same $(K-1)$-suffix. Choose the first such pair $u,u'$
as a function of $S$ alone. Replace $\pi$ by

$$
\pi'(u)=\pi(u'),\qquad
\pi'(u')=\pi(u),\qquad
\pi'(w)=\pi(w)\ \ (w\notin\{u,u'\}).                     \tag{3.1}
$$

The rows of $B_K$ indexed by $u,u'$ coincide. In particular,
both new edges are valid and

$$
a(S,\pi')=a(S,\pi).                                      \tag{3.2}
$$

The same pair is selected after the replacement, because $S$ has
not changed. Therefore (3.1) is a fixed-point-free involution.
Composing a permutation with a transposition changes its cycle
count by exactly one: it splits one cycle when the two selected
states were on that cycle, and merges two cycles otherwise.
This can be checked by following the two outgoing strings from
the selected states. Hence

$$
c(\pi')=c(\pi)\pm1.                                      \tag{3.3}
$$

At $t=1$, paired terms in (2.1) cancel exactly, including their
complete complex phase. This argument allows arbitrarily short
pieces and arbitrarily many repeated physical vertices.

### The surviving pseudoorbits are exactly the lower-block ones

For a nonbad pseudoorbit, suffixes of the selected states are
distinct. Validity of the transitions and bijectivity of $\pi$
imply that the selected prefixes and suffixes have the same
multiset. Therefore prefixes are distinct as well.

Let
$$
T=\{\operatorname{suffix}_{K-1}(u):u\in S\}.
$$
Project every state $u$ to its suffix and every successor to
the suffix of $\pi(u)$. This yields a permutation $\rho$ of
$T$, with valid $B_{K-1}$ transitions, the same cycle count,
and the same amplitude.

Conversely, given a lower-block pseudoorbit $(T,\rho)$, the
upper state with suffix $a\in T$ is obtained by appending $a$
to the first letter of $\rho^{-1}(a)$:
$$
u(a)=(\rho^{-1}(a)_1,a_1,\ldots,a_{K-1}).
$$
The overlap condition for the lower transition
$\rho^{-1}(a)\to a$ makes the prefix of $u(a)$ equal to
$\rho^{-1}(a)$. Set $\pi(u(a))=u(\rho(a))$.
This is the inverse construction. For $K=2$, the lower blocks
are individual letters and the same formula applies.

Thus cancellation plus this bijection proves (1.3) combinatorially.
Iteration reduces the full pseudoorbit sum to collections of
vertex-disjoint physical cycles, and its coefficients of degree
greater than $N$ vanish exactly.

## 4. The exact connected-cycle defect

The involution also computes what happens away from the fermionic
value $t=1$. For each involution orbit select its member with the
smaller cycle count $c$, and retain its amplitude $a$. The paired
contribution is

$$
z^{|S|}a\bigl[(-t)^c+(-t)^{c+1}\bigr]
=z^{|S|}a(-t)^c(1-t).
$$

Define the explicit finite polynomial

$$
\mathscr R_K(z,t)=
\sum_{\text{bad involution orbits}}
(-1)^c t^{c-1}z^{|S|}a.                                 \tag{4.1}
$$

The survivor bijection holds with the entire cycle variable.
Consequently

$$
\boxed{
\mathscr Z_K(z,t)-\mathscr Z_{K-1}(z,t)
=t(1-t)\mathscr R_K(z,t).
}                                                       \tag{4.2}
$$

At $t=0$, the constant term of $\mathscr R_K$ consists exactly
of involution orbits pairing a single cycle with two cycles:

$$
\mathscr R_K(z,0)
=-\sum_{\substack{\text{bad single cycles}\\\text{at level }K}}
z^{|S|}a(S,\pi).                                         \tag{4.3}
$$

Indeed $c=1$ is the only possible contribution. A single cycle
containing the selected pair always splits into two cycles, so
every bad single cycle occurs in exactly one such orbit.

Writing
$$
\mathscr C_K(z)=-[t]\mathscr Z_K(z,t),
$$
we obtain the exact connected-sector identity

$$
\boxed{
\mathscr C_K(z)-\mathscr C_{K-1}(z)
=-\mathscr R_K(z,0)
=\sum_{\text{bad single cycles at level }K}z^{|S|}a.
}                                                       \tag{4.4}
$$

The cancellation at $t=1$ therefore does not cancel the single-cycle
coefficient. It cancels that contribution against a two-cycle
contribution to a different coefficient of $t$. Equations
(4.2)--(4.4) are exact; no statement about the size of the displayed
complex sum has been deduced from determinant truncation.

The same issue persists after taking a product with a conjugate
pseudoorbit polynomial. A successor swap changes the cycle count
on one side. Projecting to one cycle on each side does not retain
its partner. One cannot use this involution to delete a term of
$|\operatorname{Tr}U^n|^2$ unless a separate argument restores
the required cycle projections.

## 5. First failure at a lower block level gives a canonical pairing

Consider an unrooted physical cycle whose length-$K$ blocks are
distinct but whose vertices are not all distinct. There is a unique
smallest $q\in\{2,\ldots,K\}$ for which its length-$q$ blocks
are distinct. Its lift at level $q$ is a bad single cycle: the
$(q-1)$-suffixes repeat.

Apply (3.1) at that level. The result is a genuine two-component
pseudoorbit at level $q$, with exactly the same directed physical
edge array and amplitude. Record the level $q$ with it.
The map from the original unrooted cycle to this tagged two-cycle
pseudoorbit is injective: the selected state pair depends only on
the state set; applying the involution again recovers the single
cycle, whose physical word determines its lift at every level.

This gives an explicit unmarked pairing of all such physical
single cycles with two-cycle objects. The tag is the uniquely
determined first failure level, not a sum over presentations.
It does not assert that the two-cycle object can be lifted back
to every larger level without introducing block collisions.

## 6. The affected sector carries essentially all positive path mass

Assume now that $U$ is unitary and

$$
P_{uv}=|U_{uv}|^2,\qquad
\max P_{uv}\le C/N,\qquad
\|P-J\|_{\mathrm{op}}\le1/2,\qquad
N\ge\max(C,3),\quad C\ge1.                              \tag{6.1}
$$

These are the already proved original-family hypotheses, with
$C=9$, from the frozen four-branch kernel and oscillatory matrix
proofs in research_round5_2026_10_21/dual_physical_four_branch_kernel.md
and research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md.
Their source hashes are respectively
0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c
and ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d.

For a set of rooted words $\mathcal A$, let

$$
\mathsf W_n(\mathcal A)=\sum_{x\in\mathcal A}\prod_jP_{x_j,x_{j+1}}.
$$

The full mass is $\operatorname{Tr}P^n$, not a probability obtained
by changing the ensemble. It is $1+O(C2^{-n})$ on the present
time range, as proved below.

### 6.1. A fixed sampling interval bounds vertex-simple cycles

Here is the row/column sandwich directly. Put $A=P-J$.
Every row and column of $A$ has squared Euclidean norm at most
$(C-1)/N$, because
$$
\sum_v(P_{uv}-1/N)^2=\sum_vP_{uv}^2-1/N
\le(C-1)/N,
$$
and the same calculation applies to columns. Since $AJ=JA=0$,
$P^\ell-J=A^\ell$. Placing one factor of $A$ at each end
and using $\|A\|\le1/2$ proves

$$
|(P^\ell-J)_{uv}|
\le\frac{C-1}{N}2^{-(\ell-2)},\qquad \ell\ge2.
                                                               \tag{6.2}
$$

Choose an integer $d\ge2$ satisfying

$$
(C-1)2^{-(d-2)}\le\frac12.
$$

For example
$$
d=2+\max\{0,\lceil\log_2(2\max\{C-1,1\})\rceil\}
$$
works. For $C=9$, $d=6$ works. Then
$$
(P^d)_{uv}\ge\frac1{2N}.
$$
Also $\max(P^m)_{uv}\le C/N$ for every $m\ge1$, by
stochasticity and the entrywise bound on $P$.

Take $n\ge d$ and $m=\lfloor n/d\rfloor$. If $m>N$,
vertex-simple length-$n$ words do not exist. When $1\le m\le N$,
sample the positions $0,d,\ldots,(m-1)d$. Vertex simplicity
implies that all sampled labels are distinct. Sum all nonsampled
positions without constraints. The first $m-1$ transitions
are $P^d$, and the last transition has length
$n-(m-1)d\ge d$. Bounding that last transition by $C/N$ gives

$$
\mathsf W_n(\mathrm{vertex\ simple})
\le\frac CN
\sum_{\substack{v_0,\ldots,v_{m-1}\\\mathrm{distinct}}}
\prod_{i=0}^{m-2}(P^d)_{v_i,v_{i+1}}.
$$

At step $j$, $j$ old labels are forbidden, each with transition
probability at least $1/(2N)$. Sum them successively, starting
with the $N$ choices of $v_0$, to obtain

$$
\boxed{
\mathsf W_n(\mathrm{vertex\ simple})
\le C\prod_{j=1}^{m-1}\left(1-\frac j{2N}\right)
\le C\exp\left[-\frac{m(m-1)}{4N}\right].
}                                                       \tag{6.3}
$$

For $n>N$ the left side is zero; this can of course be used
instead of (6.3). Uniformly for $cN\le n\le BN$, $c>0$,
the vertex-simple mass is exponentially small in $N$.
Explicitly, if $N\ge4d/c$, then either it vanishes or
$$
\mathsf W_n(\mathrm{vertex\ simple})
\le C\exp[-c^2N/(16d^2)].
$$

### 6.2. Long-block regularity has almost full mass

For $1\le K<n/2$, equality of cyclic length-$K$ blocks at
two distinct positions has identification rank exactly $K$.
Here is a self-contained verification. After translating one start
to zero, the $K$ equality edges are $u\leftrightarrow u+a\pmod n$,
$0\le u<K$, with $a\ne0$. Every vertex has at most one incoming
and one outgoing directed equality edge. A cycle would have to
contain a complete orbit of addition by $a$. Such an orbit has
ordinary span $n-\gcd(n,a)\ge n/2$, so all its tails cannot
lie in the interval of length $K<n/2$. This also excludes the
possible two-edge cycle at $a=n/2$. The equality graph is a forest
with $K$ edges.

After these identifications, the connected physical cycle graph
has $n-K$ vertices and $n$ edge factors. Choose an undirected
spanning tree. Bound its $K+1$ remaining edge factors by $C/N$.
Sum tree leaves in either orientation using the row and column sums
of $P$, both equal to one; the last free label gives $N$.
Thus the mass of one equality event is at most

$$
N(C/N)^{K+1}=C(C/N)^K.
$$

The union bound is applied here only to the nonnegative path
weights $\prod P$, not to the signed amplitude sum. Therefore

$$
\boxed{
\mathsf W_n(\mathrm{not}\ K\mathrm{\!-\!regular})
\le C\binom n2(C/N)^K.
}                                                       \tag{6.4}
$$

For completeness, write $A=P-J$. Then
$\|A\|_{HS}^2\le C$, $\|A\|\le1/2$, and for $n\ge2$
$$
|\operatorname{Tr}P^n-1|
=|\operatorname{Tr}A^n|
\le C2^{-(n-2)}.
$$
One proof of the last inequality is
$\|A^2\|_1\le\|A\|_{HS}^2$ followed by multiplication by
$\|A^{n-2}\|$. Normality is not needed.

Combining this with (6.3)--(6.4), for $m\le N$,

$$
\begin{split}
\mathsf W_n(K\mathrm{\!-\!regular,\ not\ vertex\ simple})
\ge {}&
1-C2^{-(n-2)}
-C\binom n2(C/N)^K\\
&-C\exp[-m(m-1)/(4N)].
\end{split}                                             \tag{6.5}
$$

The corresponding upper bound is $1+C2^{-(n-2)}$.
For $n>N$, remove the last error term since vertex simplicity
is impossible.

Taking $K=\lceil4\log_2N\rceil$, for every fixed $A_0>0$
and $0<c\le B<\infty$,

$$
\boxed{
\mathsf W_n(K\mathrm{\!-\!regular,\ not\ vertex\ simple})
=1+O_{A_0,c,B,C}(N^{-A_0}),
\qquad cN\le n\le BN.
}                                                       \tag{6.6}
$$

All these words are primitive because their cyclic $K$-blocks
are distinct. Dividing by the exact $n$ roots per unrooted
cycle shows

$$
\sum_{\substack{\text{unrooted }K\text{-regular single cycles}\\
\text{not vertex simple}}}|a(\gamma)|^2
=\frac1n\left[1+O_{A_0,c,B,C}(N^{-A_0})\right].            \tag{6.7}
$$

Consequently the canonical one-cycle/two-cycle pairing of §5
affects essentially all of the positive rooted path mass at
Heisenberg times. It cannot be ignored as an exponentially rare
exception when trying to preserve the connected-cycle projection.
This is a positive mass statement; it does not lower-bound the
absolute value of the sum of their complex amplitudes.

## 7. What this route has and has not accomplished

The exact dense involution resolves presentation multiplicities for
the pseudoorbit determinant: each term is a state subset and one
permutation, and its cancelling partner is explicit. It permits all
short pieces, repeated physical vertices, and all reconnection
orders. It therefore exposes how a complete phase-preserving dense
cancellation can occur without estimating each large class separately.

Its exact defect (4.2) prevents substituting this result into the
connected trace-pair statistic. The defect is already present at the
finite algebraic level and its single-cycle domain has the full
positive mass (6.6). No quantitative cancellation for
$\mathscr R_K(z,0)$, for its conjugate products, or for the required
unequal-occupation terms $\Omega_n(U_N)$ is proved here.

Thus the first spectral obligation remains the full signed
Heisenberg-time sum from §9 of the current master. The present note
does not turn determinant truncation, a zero at the cycle-fugacity
value $t=1$, or the positive mass calculation into a bound on its
single-cycle coefficient.

## 8. Exact finite verification and a nonzero unitary defect

The companion script r6_dense_higher_block_exact_checks.py uses only
integer and rational arithmetic. It enumerates all valid subsets
and permutations for the following weighted higher-block matrices:

| Physical matrix | Level $K$ | Unmarked objects | Bad objects | Survivors |
| --- | ---: | ---: | ---: | ---: |
| $\begin{pmatrix}2&3\\5&7\end{pmatrix}$ | 1 | 5 | 0 | 5 |
| same | 2 | 13 | 8 | 5 |
| same | 3 | 65 | 52 | 13 |
| $\begin{pmatrix}2&3&5\\7&11&13\\17&19&23\end{pmatrix}$ | 1 | 16 | 0 | 16 |
| same | 2 | 844 | 828 | 16 |

For each term, the checks verify involutivity, validity of new
edges, equality of the complete directed edge array and amplitude,
the change of cycle count by one, the exact survivor bijection and
its inverse. They then verify (4.2), (4.3), and (4.4)
coefficient by coefficient. Matrix traces are checked through
length 9, including lengths smaller than the block level.

The two-dimensional example gives
$$
\mathscr Z_2-\mathscr Z_1
=-135\,t(1-t)z^3-210\,t(1-t)^2z^4.
$$
Thus cancellation at $t=1$ visibly leaves a nonzero
single-cycle coefficient.

The same distinction holds inside the unitary class, with no
rounding or genericity argument. Take the rational orthogonal
matrix
$$
U_*=\frac19
\begin{pmatrix}
7&-4&-4\\
-4&1&-8\\
-4&-8&1
\end{pmatrix}.
$$
Its numerator times its transpose is $81I$, as checked entry
by entry. All 16 level-1 and all 844 level-2 pseudoorbits satisfy
the same identities. In this case
$$
[z^3]\mathscr R_2(z,0)=-\frac{128}{243}\ne0.
$$
This value can also be checked without enumeration: the bad
single cycles of length 3 have physical words $iij$, $i\ne j$,
up to rotation, so their amplitude sum is
$$
\sum_i(U_*)_{ii}\sum_{j\ne i}(U_*)_{ij}^2
=\sum_i(U_*)_{ii}\bigl(1-(U_*)_{ii}^2\bigr)
=1-\frac{345}{729}=\frac{128}{243}.
$$
This auxiliary matrix is used only to check the algebraic defect.
It is not substituted for the prescribed family.

The companion also verifies:

- the canonical first-failure injection for 83 binary cycles
  through length 11 at block level 4, and 332 ternary cycles
  through length 7 at block level 3;
- all 68,228 cyclic-block rank cases through length 75;
- positive collision and sampling bounds on 87,360 rooted words
  for the explicit nonuniform unistochastic matrix
  $\begin{pmatrix}9&16\\16&9\end{pmatrix}/25\otimes J_2$,
  including 62 individual collision events;
- 4,851 exact uniform-matrix vertex-simple mass comparisons.

Every assertion passed. These checks verify the stated finite
constructions and constants; the proofs in §§1--6 establish the
claims for arbitrary dimension. The finite checks imply no
asymptotic spectral universality statement.
