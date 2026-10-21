> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_growing_order_signed_cancellation.md`. Embedded SHA256: `bfcf47681e92fea287307294ee36c6ad6a511b6f5612c0a2edfe1083ddb1fc97`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: signed cancellation with a growing number of arcs

Date: 21 October 2026. Auditor: /root/audit_uniform_word_r4.

Frozen target:
dual_directed_encounter_growing_order_cancellation.md.

Target SHA256:
f0ffa2acc3e4b66b75620ee116a20cf8793c4d7efc40d5db67ded4259436c4e4.

Frozen companion:
dual_growing_order_exact_checks.py.

Companion SHA256:
63acd0e681cdcaaa4cf07b9540ed38a8cd7434c474da368aa949b2dddce32965.

Both hashes were independently recomputed. The complete source,
Sections 1--9, was read and reconstructed. The companion was run
independently and passed:

- 15,108 permitted-cycle and relative-cycle-count checks;
- 12,229 regular partner-class checks across orders 3, 4 and 5,
  including 1,341 presentations with repeated arc-start labels;
- 156 exact nonzero endpoint factorizations, including 139 with
  repeated start labels;
- 7,680 exact marked-root count checks at order four, using two
  vertex labels and including periodic words.

The finite checks are corroboration. The proof below is independent
of their outcomes and of other agents' verdicts. No frozen source
was changed.

## Verdict and a notation clarification

The finite theorem, the square-root-order corollary, and the
stated fixed-order positive-part formulas are proved on their
respective stated hypotheses. The extension to repeated start
labels is valid because the literal successor inequality, rather
than pairwise distinctness alone, supplies both endpoint
orthogonality and right maximality.

One notation clarification should be retained when citing the
source. The symbol $\mathfrak C_r^\circ$, introduced after
(4a), means the set of $r$-cycles satisfying the index condition
$$
\sigma(i)\ne\gamma_r(i)\quad\text{for every }i,
$$
independently of the vertex labels $b$. The literal condition
$$
b_{\sigma(i)}\ne b_{\gamma_r(i)}
$$
is then imposed by the separate domain $\mathcal B_\sigma$.
The phrase “this set of permutations” after (4a) can otherwise
be read ambiguously. Equations (11), (16) and the permutation
count require, and consistently use, the reading just specified.
This is a notational qualification, not a missing estimate.

In particular, for
$$
M_N=\lfloor\sqrt N/10\rfloor,\qquad
K_N=\lceil4M_N+4\log_2N\rceil,\qquad
L_N=2K_N+2,
$$
both the literal-mismatch class and its separately evaluated
distinct-start subclass satisfy
$$
\sup_{1\le n\le BN}|\mathcal T^\diamond_{M_N,K_N,n}|
=O_{A_0,B,C}(N^{-A_0})
$$
for every fixed $A_0>0$. These are actual unmarked pair sets.
There is no claimed control of their complement in $Z_n$.

## 1. The exact class and its symmetry

Fix $N\ge\max(C,3)$, integers $M\ge3,K\ge1$, and
$L=2K+2$. The input matrix is unitary, with
$$
P_{xy}=|U_{xy}|^2\le C/N,\qquad
\|P-J\|_{\rm op}\le\tfrac12.
$$
The original-family application uses the same frozen analytic
inputs as the preceding three-arc theorem, with $C=9$ for
every sufficiently large odd $N$.

An $r$-marking divides a rooted word into $r$ forward
vertex words, with internal lengths $\ell_i\ge L$,
$\sum_i\ell_i=n-r$, starts $b_i$ and ends $a_i$.
The original successor is $\gamma_r(i)=i+1\bmod r$.
The partner ordering $\sigma$ is an $r$-cycle, so it
produces a single cyclic word. The index condition forbids
retained original successors. The additional literal
condition requires that the actual next label changes
at each endpoint.

The literal condition implies the index condition but
does not require all the $b_i$'s to be distinct. Its
domain is checked independently for each $\sigma$.
For the distinct-start version, index inequality already
implies literal inequality. The two signed sums are
proved separately; one is not bounded merely by being
a subset of the other.

Cyclically renaming the original arcs conjugates
$\sigma$ by a power of $\gamma_r$ and leaves the
collection of permitted orders invariant. Exchanging
the original and partner cyclic orders and then
renaming their arcs also preserves the two successor
inequalities. Distinctness of all starts, when imposed,
is preserved as well. This verifies conjugation
symmetry of the marked relations and, after regularity
and the exclusions, of the unmarked relations.

## 2. All endpoint factors are mixing errors

Let $A=P-J$. Double stochasticity gives $AJ=JA=0$.
Each row and each column of $A$ has squared norm at
most $(C-1)/N$. Hence for $\ell\ge2$,
$$
|(P^\ell-J)_{ba}|
\le\frac{C-1}{N}2^{-(\ell-2)}.
$$
The proof uses the corresponding row and column around
$A^{\ell-2}$; it applies to nonnormal $P$.

For fixed lengths and $\sigma$, summing the common
arc interiors gives exactly
$$
\mathcal A_{\boldsymbol\ell,\sigma}
=\sum_{\boldsymbol b\in\mathcal B_\sigma}
\sum_{\boldsymbol a}
\prod_{i=1}^r
(P^{\ell_i})_{b_i,a_i}
U_{a_i,b_{\gamma_r(i)}}
\overline{U_{a_i,b_{\sigma(i)}}}.
$$
For each fixed allowed $b$-tuple the sum factors over
the $a_i$'s. Its constant part at every single endpoint
vanishes by column orthogonality:
$$
\sum_aN^{-1}U_{a,b_{\gamma_r(i)}}
\overline{U_{a,b_{\sigma(i)}}}=0.
$$
This uses the literal inequality of the two column
labels. It remains true when some other start labels
coincide.

Consequently the exact contraction is
$$
\mathcal A_{\boldsymbol\ell,\sigma}
=\sum_{\boldsymbol b\in\mathcal B_\sigma}
\prod_{i=1}^r
\left[
\sum_a(P^{\ell_i}-J)_{b_i,a}
U_{a,b_{\gamma_r(i)}}
\overline{U_{a,b_{\sigma(i)}}}
\right].
$$
In particular, no mixed term retaining a $J$ factor
survives. This is a product cancellation, not a first
order telescopic replacement estimate.

Cauchy--Schwarz for the two unit-norm columns shows
that the absolute value of the $i$-th bracket is at
most $\delta_i/N$, where
$\delta_i=(C-1)2^{-(\ell_i-2)}$.
There are at most $N^r$ start tuples, so
$$
|\mathcal A_{\boldsymbol\ell,\sigma}|
\le\prod_i\delta_i
=(C-1)^r2^{-n+3r}
\le\delta^r,\qquad
\delta=(C-1)2^{-2K}.
$$
The exponent is correct because
$\sum_i(\ell_i-2)=n-3r$.
All orthogonality is used before taking absolute
values. The phases are those of the given $U$.

## 3. Root factors and combinatorial budgets

For fixed $r$, distinguishing a first marked arc
introduces exactly $r$ choices for each unordered
marking, even for a periodic vertex word. There are
$n$ positions for that distinguished start and
$n$ labelled partner roots. Summing over the full
relabelling-invariant set of permitted $\sigma$'s
therefore gives the exact identity
$$
\mathcal H^\diamond_{M,K,n}
=\sum_{r=3}^M\frac{n^2}{r}
\sum_{\substack{\sum_i\ell_i=n-r\\\ell_i\ge L}}
\sum_{\sigma\in\mathfrak C_r^\circ}
\mathcal A_{\boldsymbol\ell,\sigma}.
$$
No assumption of aperiodicity is used at this stage.
Periodic words are counted with their specified
labelled partner-root multiplicities.

The number of length compositions is exactly
$$
Q_{n,r,L}=
\binom{n-rL-1}{r-1}
$$
when $n\ge r(L+1)$, and zero otherwise. Subtracting
$L$ from each internal length proves the formula.
The bound
$$
Q_{n,r,L}\le\frac{n^{r-1}}{(r-1)!}
$$
combines with
$|\mathfrak C_r^\circ|\le(r-1)!$. Thus the factorial
cost of the partner permutations is cancelled by the
composition denominator; no fixed-order constant
has been hidden.

The two phase bounds are consequently
$$
|\mathcal H^\diamond|
\le n\sum_{r=3}^M\frac{(n\delta)^r}{r}
$$
and
$$
|\mathcal H^\diamond|
\le n2^{-n}
\sum_{r=3}^M\frac{[8(C-1)n]^r}{r}.
$$
Including infeasible orders only enlarges these
nonnegative bounds. When $n\delta<1$, using
$1/r\le1/3$ and a geometric series gives
$$
|\mathcal H^\diamond|
\le\frac{n(n\delta)^3}{3(1-n\delta)}.
$$
All formulas remain valid when $C=1$, in which
case every contraction is exactly zero.

## 4. Uniqueness across all allowed cut numbers

Each presented arc identifies a forward interval of
$x$ with one of $y$ by a constant translation
of positions modulo $n$. It is right maximal:
the successors just beyond its endpoint are
$b_{\gamma_r(i)}$ and $b_{\sigma(i)}$, which
are literally different.

Consider two admissible presentations of a regular
pair, with possibly different numbers of cuts.
Take an arc of the second presentation as a proper
cyclic interval in $x$. If it crosses at least
two boundaries of the first partition, it contains
an entire intervening old arc, of at least $2K+3$
vertices. Otherwise it splits into at most two old
pieces, and its own length of at least $2K+3$
forces one piece to have at least $K$ consecutive
vertices.

Thus every new arc overlaps some old arc in at
least $K$ consecutive positions, independently
of either number of cuts. On this overlap the
two presentations match the same $K$-substring
into $y$. Regularity forces identical starting
positions there, hence identical translations.

From a point in the overlap, compare the two
right endpoints along the forward cyclic order.
If one ended earlier, the other would extend
through its prescribed unequal successors.
This contradicts right maximality. Their right
endpoints therefore coincide.

Every endpoint of one partition lies in the
other endpoint set. Interchanging the two
presentations gives the reverse inclusion,
so both endpoint sets and both cut numbers
are equal. Once the cuts are fixed, each
long arc has a unique matched occurrence in
regular $y$, determined by its first
$K$-substring. These occurrences determine
the entire partner cyclic order, even with
repeated first vertex labels.

This proves global uniqueness, including across
orders $r$, across choices of $\sigma$, and
across marking sets. Regular words are aperiodic,
so labelled partner roots now give distinct
rooted words. The marked multiplicity is
exactly one on the represented regular set.

There are no forward rotations there. A global
rotation would supply one global matching
translation; regularity would force every
arc translation to equal it, contradicting
the mismatch at each endpoint.

## 5. Exceptional words and reversed pairs

For fixed lengths and $\sigma$, the common
interiors are $r$ open paths with $n$
formal vertex positions and $n-r$ internal
$P$ factors. Bound the $2r$ connector
amplitudes by $(C/N)^r$.

After rank-$h$ label identifications the
quotient has $n-h$ variables and $s\le r$
connected components. A spanning forest has
$n-h-s$ edges. Of the internal factors,
$h+s-r$ lie outside the forest and are
bounded by $C/N$. Summing the forest by
row or column leaf sums gives $N^s$.
Therefore the constrained absolute weight
is at most
$$
N^s(C/N)^{h+s-r}(C/N)^r
=C^s(C/N)^h\le C^r(C/N)^h.
$$
The forest exists in the quotient graph,
so $h+s-r\ge0$. Loops and repeated
parallel factors cause no problem.

An equality of two distinct cyclic
$K$-substrings gives $K$ arrows between
formal positions, with at most one arrow
entering and leaving each position and no
loops. Since $K<n$ in the nonempty range,
all their starting positions are distinct.
Each component is a path or a cycle.
Paths give one identification per edge,
and cycles of length at least two give
at least half as many. The rank is thus
at least $K/2$.

A union over at most $n^2$ starting pairs,
followed by the count in Section 3, gives
for irregular $x$ at fixed $r$
$$
\frac{C^r n^{r+3}}{r}(C/N)^{K/2}.
$$
The same bound holds for $y$, by
exchanging the two arc orders. Equivalently
their formal vertex positions are
permutations of one another, preserving
the equality ranks. For $N\ge C$,
summing and enlarging $r$ to $M$
in the positive factors gives
$$
E_{\rm irr}
=2M C^M n^{M+3}(C/N)^{K/2}.
$$
This is an absolute bound on marked
terms and applies to either start domain
or any edge-count restriction.

For reversed partners use
$$
S_{uv}=\sqrt{P_{uv}P_{vu}}.
$$
It is symmetric, has row sums at most
one and entries at most $C/N$. On
a reversed rotation pair the absolute
weight is exactly the product of $S$
around the original cyclic word.

If $h$ disjoint pair identifications
are imposed on its positions, the quotient
cycle has $n-h$ vertices and $n$
factors. Keep a spanning tree and bound
its $h+1$ surplus factors by $C/N$.
Leaf summation gives the bound
$$
C(C/N)^h.
$$
Any common forward arc in a reversed
pair gives a reversed substring match
inside $x$. Its $2K+3$ vertices
impose a reflection of formal indices.
The reflection has at most two fixed
points, so at least $K$ distinct
disjoint nontrivial pairs are identified.

There are at most $n^2$ alignments.
For each $x$ and $r$, at most
$\binom nr(r-1)!n\le n^{r+1}/r$
marked partner data occur. Therefore
the reversed loss is at most
$$
E_{\rm rev}
=CMn^{M+3}(C/N)^K.
$$
The stated longer-arc improvement of
the identification rank is also valid.

After deleting both exceptional sets,
the marked functional becomes the
actual unmarked class by Section 4.
Forward rotations are already absent.
This proves the exact finite estimate
$$
|\mathcal T^\diamond_{M,K,n}|
\le E_{\rm phase}+E_{\rm irr}+E_{\rm rev}.
$$
All arguments are uniform in $M,K,n$;
when there is no admissible marking
the left side is zero.

## 6. Square-root-order constants

Let $u=\log_2N$, $B_+=\max(B,1)$,
and use the target's $M_N,K_N,L_N$.
Then
$$
4M+4u\le K<4M+4u+1,\qquad
\delta\le(C-1)2^{-8M}N^{-8}.
$$
For large $N$, $n\delta<1/2$
uniformly for $n\le BN$. The geometric
phase bound gives exactly
$$
E_{\rm phase}
\le\tfrac23 B^4(C-1)^3\,2^{-24M}N^{-20}.
$$
Since $M\sim\sqrt N/10$, this is
smaller than every fixed inverse power.

Separately using the upper bound on
$K$ in the power of $C$ and the
lower bound in the power of $N$
gives the target's conservative bound
$$
E_{\rm irr}
\le2M C^{3M+2u+1/2}B_+^{M+3}
N^{-M+3-2u}.
$$
Equivalently,
$$
E_{\rm irr}
\le2M C^{1/2}B_+^3
(C^3B_+/N)^M
N^{3-2u+2\log_2C}.
$$
The extra $C^{1/2}$ only enlarges
the bound. If $N\ge(C^3B_+)^2$,
the parenthesized power is at most
$N^{-M/2}$. All remaining factors
are dominated by a fixed polynomial
for sufficiently large $N$, proving
decay faster than every fixed power.

The exact ratio of the displayed
reversed and irregular bounds is
$$
\frac{E_{\rm rev}}{E_{\rm irr}}
=\tfrac12 C^{1-M}(C/N)^{K/2}\le\tfrac12,
$$
using $C\ge1,N\ge C$.
This completes the claimed uniform
corollary without hidden growth losses.
Multiplication by at most $BN$
bounded weights and division by
$N^2$, with an explicit factor
$W=\sup|w_{n,N}|$, proves the
weighted version with any prescribed
inverse-power exponent.

The admissible class is not
combinatorially empty. Its minimum
total length at order $M$ is
$$
M(2K+3)=8M^2+O(M\log N)
=\tfrac2{25}N+o(N).
$$
At $n=N$, the word listing all
$N$ labels once admits every
order $3\le r\le M$ for large
$N$. Reordering by
$\sigma=\gamma_r^{-1}$ changes
every successor, keeps both words
regular, and gives neither a forward
nor reversed rotation. A retained
internal forward edge excludes the
latter, since the reversed word
with distinct labels contains only
reverse-oriented edges. This checks
set nonemptiness; no lower bound
for the weight of that particular
pair is needed or asserted.

## 7. Positive parts and cutoff-dependent errors

This part applies to the distinct-start
subclass only. In column $b_j$, the
edge-count difference is
$$
e_{a_{\sigma^{-1}(j)}}-
e_{a_{\gamma_r^{-1}(j)}}.
$$
Because the columns are distinct,
equal edge counts are equivalent to
$$
a_i=a_{\pi(i)},\qquad
\pi=\sigma^{-1}\gamma_r.
$$
The endpoint labels are constant
on the cycles of $\pi$.
There are exactly $N^{c(\pi)}$
such assignments, with equality
between labels of different cycles
allowed. Repeated start labels in
the larger literal class would not
justify this columnwise criterion;
the source correctly does not
claim it there.

On every such assignment, the
complex connector product is
exactly the product of the
original $P$-connector weights.
After replacing the long entries
by $1/N$, its distinct-start
sum is a product of row
probability distributions with
coincidences excluded. A union
bound over pairs gives loss at
most $\binom r2 C/N$.
The error in the long entries
is at most
$r\delta(1+\delta)^{r-1}$
in relative value. Hence
$$
\left|\mathcal A^{=,\mathrm{dist}}_{\boldsymbol\ell,\sigma}
-N^{c(\pi)-r}\right|
\le N^{c(\pi)-r}
\left[\binom r2 C/N+
r\delta(1+\delta)^{r-1}\right].
$$
This verifies the finite displayed
$r$-dependence in (30).

For fixed $r$, the target's
assumptions $L=o(N)$,
$\delta=o(1/N)$, and
superpolynomial exceptional loss
give on each fixed bulk interval
$$
\mathcal T^{=,\mathrm{dist}}_r
=\frac{t^{r+1}}{r!}
\sum_{\sigma\in\mathfrak C_r^\circ}
N^{c(\sigma^{-1}\gamma_r)+1}
+O_{r,B,C}\!\left(
(L+1)\sum_{\sigma\in\mathfrak C_r^\circ}
N^{c(\sigma^{-1}\gamma_r)}
\right).
$$
Indeed the length count has error
$O_r(n^{r-2}(L+1))$, and the
two relative errors above supply
the remaining terms. This is a
fixed-$r$ expansion; it is not
being used uniformly at $r=M_N$.
For logarithmic $K$, its
proportionality constant must
of course satisfy the already
stated $\delta=o(1/N)$
condition when $C>1$.

At $r=3$ there is one permitted
order and one relative cycle,
giving $N^2t^4/6$. At $r=4$
only the reversed cyclic order
of arcs retains no successor;
its relative permutation is
$\gamma_4^2$, with two cycles,
giving $N^3t^5/24$. This
reverses arc order, not internal
edge orientation.

The corresponding signed
different-edge-count sums
cancel these positive terms to
the relevant finite-theorem
accuracy. With logarithmic
cutoffs the positive error is
$O(N^{c(\pi)}\log N)$;
with the square-root cutoff
it is $O(N^{c(\pi)+1/2})$.
The source correctly keeps
these two rates separate.
Likewise the new class with
square-root cutoffs is not
silently identified with the
earlier logarithmic-cutoff
three-arc class.

Finally, $\pi$ has no fixed
points by the index condition,
and is even because it is the
product of the inverse of one
$r$-cycle and another
$r$-cycle. This confirms the
stated restrictions on its
cycle counts.

## 8. Exact scope

The result is a signed,
quantitatively controlled
cancellation for actual
unit-multiplicity pairs in
$Z_n$, including a number
of cuts proportional to
$\sqrt N$. It includes
literal mismatches with
repeated starts and proves
the distinct-start version
independently.

It still requires long
common forward arcs. The
square-root corollary does
not estimate
$$
Z_n\setminus
\mathscr T_{M_N,K_N,n}
$$
at the normalization needed
for the pair statistic.
An absolute forest bound
for exceptions inside this
parametrization does not
bound that complement.
The fixed-order positive
formulas also do not
justify any conclusion
about the full signed
trace.

The first missing spectral
step is the signed
weighted sum on this
complement, followed by
the further higher-order
requirements of
$H_{\rm diag}$.
The theorem neither
proves nor refutes the
original CUE/Sine_2
conclusion.
