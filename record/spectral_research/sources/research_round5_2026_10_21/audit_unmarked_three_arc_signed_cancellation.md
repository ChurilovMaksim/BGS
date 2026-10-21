> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_unmarked_three_arc_signed_cancellation.md`. Embedded SHA256: `43d297e1cdb1f2f12f120e0a274b6343472a7ebda9e83dd56aefbfc2b5e1984a`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: unmarked signed cancellation of three long arcs

Date: 21 October 2026. Auditor: /root/audit_uniform_word_r4.

Frozen target:
dual_directed_encounter_marked_unitarity_resummation.md.

Target SHA256:
f3e6a9e37739a557c0a065ef685b9e341804f630ddff30a3618e24e1e65876c9.

Frozen companion:
dual_three_arc_exact_checks.py.

Companion SHA256:
43827b41475583737106ab1ae6a3d6555c43b4b33f33e59e38a5a7365165b2c8.

Both hashes were independently recomputed. The complete proof in
Sections 1--8 was read and reconstructed. The companion was executed
independently and passed its 40,176 exact marked-pair checks, 24 exact
flat-phase cancellations, 1,337 regular partner-class checks (including
53 coalesced examples), and 8,554 substring-rank checks. Those checks
supplement, and do not replace, the proofs below. No frozen file was
changed.

## Verdict and quantitative notation correction

The unweighted theorem is proved as stated. In particular, for every
fixed $B,C$, its actual unmarked class satisfies
$$
\mathcal T_{n,N}=O_{B,C}(N^{-12})
\quad\text{uniformly for }1\le n\le BN,
$$
and its equal-edge-count and different-edge-count restrictions satisfy
$$
\mathcal T^=_{n,N}
=\frac{n^4}{6N^2}+O_{B,C}(N\log N),\qquad
\mathcal T^\ne_{n,N}
=-\frac{n^4}{6N^2}+O_{B,C}(N\log N)
$$
on every fixed bulk interval $cN\le n\le BN$. The negative formula
describes the sum of a conjugation-invariant class; its individual
terms need not be negative or real.

There is one quantitative notation correction to target (33).
With
$$
W=\sup_{n,N}|w_{n,N}|<\infty,
$$
the correct statement is
$$
\frac1{N^2}
\left|\sum_{1\le n\le BN}w_{n,N}\mathcal T_{n,N}\right|
\le C_{B,C}\,W\,N^{-13}
$$
for all sufficiently large $N$. Equivalently the big-O constant may
depend on $W$, or the weights may be normalized by $W\le1$.
The target's displayed $O_{B,C}(N^{-13})$, if interpreted as uniform
over arbitrary bounded norms without this factor, omits that
dependence. This does not affect the main theorem or its exponent.
The source author and root have acknowledged this correction; the
frozen source remains unchanged.

No substantive gap was found in the counting, unmarking, exceptional
set bounds, or reversed-pair exclusion. The proof gives a genuine
signed cancellation for the stated class of original-family pairs.
It does not establish the required sum over the remaining pair class.

## 1. Inputs and their scope

The combinatorial theorem assumes only
$$
P_{xy}=|U_{xy}|^2,\qquad
\max_{x,y}P_{xy}\le C/N,\qquad
\|P-J\|_{\rm op}\le\tfrac12,\qquad J_{xy}=1/N,
$$
for a unitary $U$. Both row and column sums of $P$ are one.
The proof uses no stochastic replacement of the phases of $U$.

For the exact original family, the two analytic input files are:

- dual_physical_four_branch_kernel.md, SHA256
  0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c;
- root_oscillatory_matrix_cancellation.md, SHA256
  ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d.

These supply $C=9$ for every sufficiently large odd $N$, with the
specified fixed $\tau=10^{-80}$. Their proofs were independently
reconstructed in this auditor's frozen files
audit_four_branch_physical_kernel.md and
audit_sampled_oscillatory_matrix.md. The present audit checks the new
finite-dimensional implication from the displayed two hypotheses;
it does not replace those analytic hypotheses by an assertion about
classical mixing or a different family.

## 2. Exact arc parametrization and all multiplicities

Set
$$
K=\lceil4\log_2N\rceil,\qquad L=4K+2.
$$
An unordered set of three marked positions cuts a rooted cyclic word
into three forward vertex words $A_1,A_2,A_3$. Their first and last
labels are $b_i,a_i$, respectively. Their internal edge counts obey
$\ell_i\ge L$ and
$\ell_1+\ell_2+\ell_3=n-3$. The three starting labels are distinct.

The original ordering is $123$; the only other cyclic ordering is
$132$. The original connectors are $a_i\to b_{i+1}$, while the
partner connectors are $a_i\to b_{i-1}$. Cyclically renaming the
three arcs does not change either rotation class or amplitude.

For a fixed tuple of lengths, all internal edges occur once in the
original amplitude and once in the conjugate partner amplitude.
Their product is therefore a product of $P$ entries, with no phase
error. Summing all internal labels gives exactly
$$
\mathcal A_{\boldsymbol\ell}
=\sum_{\substack{b_1,b_2,b_3\\\mathrm{distinct}}}
  \sum_{a_1,a_2,a_3}
  \prod_{i=1}^3(P^{\ell_i})_{b_i,a_i}
  \prod_{i=1}^3
  U_{a_i,b_{i+1}}\overline{U_{a_i,b_{i-1}}}.
$$
The matrix indices have the orientation shown: the remaining
orthogonality below is column orthogonality, not row orthogonality.

To count markings, distinguish one of the three marked positions.
Every unordered marking has exactly three such distinctions,
regardless of any period of the vertex word. Conversely, an ordered
length tuple, the three arc vertex words, and a position for the
first marked vertex determine one rooted word and its distinguished
marking. There are $n$ choices for that position. The marked
functional separately specifies $n$ labelled root positions for
the partner, including multiplicity if its vertex word is periodic.
Hence the exact identity is
$$
\mathcal H_{n,N}
=\frac{n^2}{3}
  \sum_{\substack{\ell_1+\ell_2+\ell_3=n-3\\\ell_i\ge L}}
  \mathcal A_{\boldsymbol\ell}.
$$
There is no unproved aperiodicity assumption in this formula.

If $d(y)$ is the number of distinct rooted rotations of $y$, and
$k(x,y)$ is the number of admissible unordered markings producing
its rotation class, the multiplicity of the distinct rooted pair is
exactly
$$
r_n(x,y)=\frac{n}{d(y)}\,k(x,y).
$$
Indeed each one of the $d(y)$ distinct words occurs precisely
$n/d(y)$ times among the labelled partner roots. This also gives
$$
0\le r_n(x,y)\le n\binom n3.
$$
The arc-word parametrization with two labelled roots is invariant
under interchanging the two arc orderings and the two roots.
Consequently $r_n(x,y)=r_n(y,x)$, including periodic words.

Subtracting $L$ from the three internal edge counts gives
$$
q_{n,L}
=\binom{n-3L-1}{2}
\quad\text{when }n\ge3L+3,
$$
and zero otherwise. In every case $q_{n,L}\le n^2/2$.
The difference between internal edges and vertex counts is therefore
accounted for at every count factor.

## 3. The signed endpoint cancellation and its error

Let $A=P-J$. Double stochasticity implies $AJ=JA=0$ and
$P^\ell=J+A^\ell$. Every row and column of $A$ has squared
Euclidean norm at most $(C-1)/N$, because
$$
\sum_j(P_{ij}-1/N)^2
=\sum_jP_{ij}^2-1/N
\le(C-1)/N.
$$
For $\ell\ge2$, sandwiching $A^{\ell-2}$ between the relevant
row and column therefore gives
$$
|(P^\ell-J)_{ba}|
\le\frac{C-1}{N}2^{-(\ell-2)}.
$$
No normality of $P$ or $A$ is needed.

For the allowed lengths write
$$
(P^{\ell_i})_{b_i,a_i}
=N^{-1}(1+\epsilon_i),\qquad
|\epsilon_i|\le\delta_N,
$$
where
$$
\delta_N=(C-1)2^{-(L-2)}
=(C-1)2^{-4K}\le(C-1)N^{-16}.
$$
Replacing the three long arc entries by $1/N$ produces zero
exactly. For each fixed admissible triple $b$, the sum over
the three endpoint labels factors, and
$$
\sum_a U_{a,b_{i+1}}\overline{U_{a,b_{i-1}}}
=\delta_{b_{i+1},b_{i-1}}=0.
$$
This step retains the original complex phases and is performed
before taking absolute values.

For the error,
$$
\left|\prod_i(P^{\ell_i})_{b_i,a_i}-N^{-3}\right|
\le N^{-3}3\delta_N(1+\delta_N)^2.
$$
For fixed $b$, the sum of the absolute connector product over
the three $a_i$'s is at most one, by three applications of
$$
\sum_a|U_{a,b}U_{a,b'}|
\le\left(\sum_a|U_{a,b}|^2\right)^{1/2}
   \left(\sum_a|U_{a,b'}|^2\right)^{1/2}=1.
$$
There are at most $N^3$ triples $b$. Thus
$$
|\mathcal A_{\boldsymbol\ell}|
\le3\delta_N(1+\delta_N)^2,
$$
and the exact count in Section 2 gives
$$
|\mathcal H_{n,N}|
\le\frac{n^4}{2}\delta_N(1+\delta_N)^2.
$$
This is $O_{B,C}(N^{-12})$ uniformly for $n\le BN$.
For $n<3L+3$ the sum is empty, so there is no small-time
exception to the uniform statement.

## 4. The coalesced term and the exact edge-count criterion

If $a_1=a_2=a_3=v$, reordering the arcs preserves every directed
edge count, including those of the connectors. The complex
amplitudes agree exactly, and the summand is nonnegative.
The contraction becomes
$$
\mathcal A^=_{\boldsymbol\ell}
=\sum_v\sum_{\substack{b_1,b_2,b_3\\\mathrm{distinct}}}
 \prod_i(P^{\ell_i})_{b_i,v}\prod_i P_{v,b_i}.
$$
For the row probability distribution $P_{v,*}$, the sum of
$\prod_iP_{v,b_i}$ over distinct triples is between
$1-3C/N$ and $1$. The lower bound is a union bound over the
three equality events for the three independently summed row
indices; it uses $\sum_bP_{vb}^2\le C/N$.
The long arc approximation consequently yields
$$
\left|\mathcal A^=_{\boldsymbol\ell}-N^{-2}\right|
\le\frac{3C}{N^3}
 +\frac{3\delta_N(1+\delta_N)^2}{N^2}.
$$
The same exact count factor gives
$$
\mathcal H^=_{n,N}
=\frac{n^2q_{n,L}}{3N^2}
 +O\!\left(\frac{Cn^4}{N^3}
 +\frac{\delta_N(1+\delta_N)^2n^4}{N^2}\right).
$$
On $cN\le n\le BN$, the finite tuple count satisfies
$$
q_{n,L}
=\frac{n^2}{2}+O(n(L+1)+(L+1)^2).
$$
Since $L=O(\log N)$, this proves
$$
\mathcal H^=_{n,N}
=\frac{n^4}{6N^2}+O_{B,C}(N\log N).
$$
The error bound can use constants independent of $c$; the
threshold for entering the nonempty range may depend on $c$.
Extra unmarked visits to $v$ inside the arcs are allowed, which
is why this coefficient has no factor $e^{-n/N}$.

Conversely, equal edge counts force coalescence. After cancelling
the common internal edges, the edge-count difference in the
column indexed by $b_j$ is
$$
e_{a_{j+1}}-e_{a_{j-1}}.
$$
These three columns are distinct. Hence all edge-count differences
vanish if and only if $a_{j+1}=a_{j-1}$ for every $j$, which
for three indices is equivalent to $a_1=a_2=a_3$.
Repeated interior labels do not affect this calculation.
The noncoalesced marked sum therefore consists exactly of the
represented pairs with different directed edge counts. Its total
is $\mathcal H-\mathcal H^=$, giving the asserted negative
leading coefficient.

## 5. Unique marking on regular pairs

A cyclic word is $K$-regular when its $n$ substrings of length
$K$, indexed by cyclic starting positions, are pairwise
different. Such a word is aperiodic: a nontrivial cyclic period
would repeat one of those substrings.

Suppose a pair $x,y$ of regular words has two admissible
three-arc presentations. Each arc is a matched forward interval
of positions in $x$ and $y$, with a fixed positional
translation modulo $n$. Each such interval is right maximal.
At its last vertex the next label in $x$ is $b_{i+1}$,
whereas the next label at the matched position of $y$ is
$b_{i-1}$; these differ by the distinct-start condition.

Take an arc of the second presentation. Relative to the three
boundaries of the first presentation, this proper cyclic
interval splits into at most four contiguous pieces. It contains
at least $L+1=4K+3$ vertices. Therefore one piece contains at
least $K$ consecutive vertices and lies in a single arc of
the first presentation.

On this piece the two presentations match the same length-$K$
word into $y$. Regularity of $y$ forces the two matched
starting positions in $y$ to be identical. Thus the two
positional translations are equal.

Starting within this common piece, compare the two right
endpoints along the forward cyclic order. Both intervals are
proper, so the comparison is made before either completes a
full turn. If one interval ended strictly earlier, the other
would extend the match through the former's prescribed unequal
successors. This contradicts its right maximality. Their right
endpoints must therefore coincide.

This associates each of the three distinct right endpoints
of the second partition with a right endpoint of the first.
The endpoint sets, and hence the marking sets, are equal.
Thus $k(x,y)\le1$. Since $y$ is aperiodic, $d(y)=n$,
and the exact multiplicity in Section 2 is one on every
represented regular pair.

Forward rotation pairs are absent from this regular class.
If $y$ were a rotation of $x$, that rotation would supply
a global matching translation. On each long arc regularity
would force its translation to be this same global one.
The unequal successors at the arc endpoint would then
contradict the global match. This also handles the coalesced
case; the simpler edge-count argument alone would not do so.

Ordinary oriented substring regularity does not by itself
exclude reversed words: a long palindromic match is possible.
The independent reversed-pair estimate in Section 7 below is
therefore necessary, and is present in the target.

## 6. Absolute removal of irregular pairs

Fix three arc lengths. Before imposing label constraints, the
three open paths have $n$ formal vertex positions and $n-3$
internal edge factors $P$. Bound the absolute product of the
six connector amplitudes by $(C/N)^3$.

Now impose any collection of label equalities of rank $h$,
so the quotient has $n-h$ vertex variables. Let $s\le3$
be the number of connected components of the quotient of the
three internal paths. A spanning forest has $n-h-s$ edges.
Among the original $n-3$ internal factors, exactly
$h+s-3$ remain outside the chosen forest. Bound these by
$C/N$. This number is nonnegative, since the forest is
a subgraph of the quotient.

Summing the forest factors over all vertex labels gives
$N^s$: remove a leaf and use either a row sum or a column
sum of $P$, according to the orientation of its incident
edge, until only one free label in each component remains.
Loops and parallel edges are outside the forest as needed.
Together with the bounded connectors this proves
$$
\sum_{\text{specified equalities}}|a(x)\overline{a(y)}|
\le N^s(C/N)^{h+s-3}(C/N)^3
=C^s(C/N)^h
\le C^3(C/N)^h.
$$
Additional unprescribed coincidences are included in this
sum; the estimate does not require that all remaining
variables take distinct values.

If two length-$K$ cyclic substrings at different starting
positions agree, the $K$ formal constraints can be drawn
as arrows $p+u\to q+u$, $0\le u<K$. In the nonempty
marking range $K<n$, all tails are distinct and all heads
are distinct. Thus each vertex has at most one incoming
and one outgoing arrow. Components are paths or cycles;
there are no loops, since $p\ne q$. A path of $j$ edges
has rank $j$, while a cycle of $j\ge2$ arrows has rank
$j-1\ge j/2$, including a two-cycle of opposite arrows.
The total rank is consequently at least $K/2$.

There are at most $n^2$ starting-position pairs. For $N\ge C$,
the forest bound gives, for fixed lengths, an irregular
$x$-contribution at most
$$
n^2 C^3(C/N)^{K/2}.
$$
The same estimate holds for irregular $y$. This can either
be seen by exchanging the arc orderings or by observing that
the formal vertex positions of $y$ are a permutation of
those of $x$, which leaves equality ranks unchanged.
Dropping the distinct-start restriction is legitimate after
taking absolute values.

Multiplication by the exact factor $n^2/3$, summation over
at most $n^2/2$ length tuples, and a union bound for the two
words give the explicit total loss
$$
E_{\rm irr}
\le\frac{C^3n^6}{3}(C/N)^{K/2}.
$$
This controls marked multiplicities already, rather than
merely counting bad unmarked pairs.

For fixed $B,C,A_0$ and $n\le BN$,
$$
n^6(C/N)^{K/2}
\le B^6N^6
\exp\!\left[-\frac{2}{\log2}(\log N)\log(N/C)\right],
$$
up to the favorable ceiling in $K$. The negative quadratic
term in $\log N$ dominates every fixed power, so the loss
is $O_{A_0,B,C}(N^{-A_0})$. This proves the absolute
negligibility needed for both edge-count restrictions as
well as the complete signed sum.

## 7. Absolute removal of reversed rotation pairs

Define the symmetric nonnegative matrix
$$
S_{uv}=\sqrt{P_{uv}P_{vu}}.
$$
It has entries at most $C/N$ and row sums at most one:
$$
\sum_vS_{uv}
\le\sqrt{\sum_vP_{uv}}\sqrt{\sum_vP_{vu}}=1.
$$
If $y$ is a rooted rotation of the reversal of $x$, then
$$
|a(x)\overline{a(y)}|
=\prod_{j=0}^{n-1}S_{x_j,x_{j+1}}.
$$
This equality includes loops and repeated labels.

Impose $h$ disjoint nontrivial pair equalities among the
cyclic positions. The quotient of the cycle has $d=n-h$
vertices, is connected, and retains $n$ edge factors.
Keep a spanning tree of $d-1$ factors and bound its
remaining $h+1$ factors by $C/N$. Leaf summation of the
tree uses the substochastic row sums of the symmetric
matrix $S$ and leaves at most $N$ choices for its root.
Therefore the constrained sum is at most
$$
N(C/N)^{h+1}=C(C/N)^h.
$$
The empty tree when $d=1$, surplus parallel edges, and
loops satisfy exactly the same estimate.

At least one of the three arcs contains
$r=\lceil n/3\rceil$ vertices. If its partner is reversed,
this arc is both a forward substring of $x$ and the reverse
of another substring of $x$. Thus for some $i,j$,
$$
x_{i+u}=x_{j-u},\qquad0\le u<r.
$$
The index map $p\mapsto i+j-p$ is an involution with at
most two fixed points, even when $n$ is even. Every
nontrivial pair can account for at most two of the $r$
starting positions. Hence these constraints include at
least
$$
h_n=\max\!\left(0,
\left\lfloor\frac{\lceil n/3\rceil-2}{2}\right\rfloor\right)
\ge n/6-2
$$
distinct disjoint pair identifications.

There are at most $n^2$ choices of $i,j$, at most
$\binom n3$ unordered markings for a given $x$, and $n$
labelled partner roots. Applying the preceding constrained
cycle bound, followed by this union bound, yields
$$
E_{\rm rev}
\le Cn^3\binom n3(C/N)^{h_n}
\le\frac{Cn^6}{6}(C/N)^{h_n}.
$$
The sum here is explicitly a sum of absolute values of
marked terms. Thus it controls either restriction as well
as the total, and is not weakened by possible phase signs.

Uniformity down to the smallest nonempty time is valid:
$$
n\ge3L+3=12K+9
\quad\Longrightarrow\quad h_n\ge2K-1.
$$
The target uses a conservative integer bound here; direct
substitution even gives $h_n\ge2K$. Consequently
$E_{\rm rev}=O_{A_0,B,C}(N^{-A_0})$ for every fixed
$A_0$, uniformly for all $n\le BN$ having a marking.
Below that threshold the class is empty.

This removes the actual reversed rotation pairs. It does
not assume that ordinary substring regularity rules out
palindromes, and it does not use a bound for the physical
matrix $Q_{xy}=U_{xy}\overline{U_{yx}}$.

## 8. Transfer to the unmarked class and precise conclusion

After removing irregular words, the marked multiplicity
is exactly one by Section 5. Forward rotations are absent
there. Removing reversed rotations costs the absolute
bound in Section 7. Thus
$$
|\mathcal T-\mathcal H|
+|\mathcal T^=-\mathcal H^=|
+|\mathcal T^\ne-\mathcal H^\ne|
=O_{A_0,B,C}(N^{-A_0})
$$
uniformly for $1\le n\le BN$, with an immaterial constant
for the three restrictions. Section 4 shows that the
coalesced restriction is exactly the equal-edge-count
restriction, so this transfer introduces no ambiguity
in the definitions of the two parts.

The arc-order involution exchanges the two words,
preserves their admissibility, regularity and exclusions,
and preserves equality or inequality of edge counts.
Each resulting unmarked class is therefore invariant
under conjugating its summand by exchanging $x,y$.
Its total is real. The equal-edge-count total is
nonnegative because every such pair has identical complex
amplitudes.

The error transfer proves all the unmarked assertions
in the target, including the corrected weighted estimate
stated at the start of this audit. The set consists of
distinct rooted pairs lying outside both forward and
reversed rotation classes, so it is a genuine subset of
the physical remainder $Z_n$.

The result has a clear remaining limit: pairs with no
admissible long three-arc presentation are not estimated.
Other reconnection types, intersections with any future
classes, and pairs sharing no such long arcs require
additional arguments. In particular the first missing
estimate in this route is the required signed weighted
sum over
$$
Z_n\setminus\mathscr T_{n,N}.
$$
The present class cancels to a negligible quantity at the
pair-statistic normalization, while its two computed
parts separately have order $N^2$ at each bulk time.
Neither an absolute-value bound on the complement nor
the existence of this cancellation evaluates that missing
sum.

As an internal check of this scope, the normalized Fourier
matrix has $P=J$, satisfies the assumptions, and gives
exact zero for the marked contraction. The same exception
bounds apply to its unmarked class. Nevertheless character
orthogonality gives $F_N^2$ equal to coordinate reflection
and $F_N^4=I$. Hence its full traces revive with magnitude
$N$ at multiples of four. This example checks the logical
boundary of the implication; it is not a counterexample
for the original $U_N$.
