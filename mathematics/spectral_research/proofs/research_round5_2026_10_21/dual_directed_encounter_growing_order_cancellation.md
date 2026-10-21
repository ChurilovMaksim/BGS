> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/dual_directed_encounter_growing_order_cancellation.md`. Embedded SHA256: `f0ffa2acc3e4b66b75620ee116a20cf8793c4d7efc40d5db67ded4259436c4e4`.
> [Thematic guide](../../topics/histories.md).

# Exact signed cancellation for a growing number of long directed arcs

Round 5, 21 October 2026. This is a further theorem for the exact original
family, with tau fixed at 10^{-80} and with all sufficiently large odd
dimensions included. It controls a genuine set of distinct physical
path pairs admitting long-arc reconnections. It includes reconnection
orders growing proportionally to sqrt(N). The complementary pair set
is not controlled, and H_diag remains unproved and unrefuted.

The argument improves the preceding three-arc theorem in two places:
every endpoint contraction must use the mixing error, giving a product
of errors; and maximal-match uniqueness requires arc length only 2K+1,
independently of the number of arcs.

Notation clarification to the frozen three-arc source
dual_directed_encounter_marked_unitarity_resummation.md, SHA256
f3e6a9e37739a557c0a065ef685b9e341804f630ddff30a3618e24e1e65876c9:
its weighted formula (33) has the bound O_{B,C}(W N^{-13}), where
W=sup|w_{n,N}|, or its displayed bound with the normalization W<=1.
No unweighted statement is changed.

## 1. Finite hypotheses and exact class

Let U be an N by N unitary matrix. Put

$$
P_{xy}=|U_{xy}|^2,\qquad J_{xy}=1/N,
$$

and suppose, for C>=1 independent of N,

$$
\max_{x,y}P_{xy}\le C/N,\qquad \|P-J\|_{\rm op}\le1/2.
\tag{1}
$$

Assume N>=max(C,3). For the original family (1) holds with C=9 for
every sufficiently large odd N, by the frozen physical kernel
0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c
and oscillatory matrix proof
ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d.

Let M>=3 and K>=1 be integers, and set

$$
L=2K+2,\qquad \delta=(C-1)2^{-2K}.
\tag{2}
$$

For a rooted cyclic word x=(x_0,...,x_{n-1}), define
$a(x)=\prod_jU_{x_j,x_{j+1}}$, with cyclic indices. A word is
K-regular if its n cyclic substrings of length K are pairwise distinct.

Mark an unordered set of r positions, 3<=r<=M, in x. Reading from
each marked position to immediately before the next partitions x into
r directed arc words A_1,...,A_r. Write b_i for the first vertex,
a_i for the last vertex, and ell_i for the number of internal edges.
The conditions are

$$
\ell_i\ge L,\qquad
\sum_i\ell_i=n-r.
\tag{3}
$$

The original cyclic successor permutation is
$\gamma_r(i)=i+1\pmod r$. A permitted partner permutation sigma
must itself be an r-cycle and satisfy

$$
\sigma(i)\ne\gamma_r(i)\quad\hbox{for every }i.
\tag{4}
$$

Its arc concatenation is a single cyclic word. In addition to the
index condition (4), impose the literal successor mismatch

$$
b_{\sigma(i)}\ne b_{\gamma_r(i)}\quad\hbox{for every }i.
\tag{4a}
$$

Condition (4a) itself implies (4), and ensures that every marked
connector changes its actual next vertex label. Repeated arc-start
labels are allowed when they obey these local inequalities. Condition
(4) refers to disagreement with the original successor, not to the
ordinary condition sigma(i)!=i.
Let $\mathfrak C_r^\circ$ denote this set of permutations, and
let q_r be its cardinality. Certainly q_r<=(r-1)!.
Relabelling which original arc is first conjugates this entire set by
a power of gamma_r, so its collection of partner cyclic orders is
intrinsic to the unordered marking.

Define $\mathscr T_{M,K,n}$ to be the following set of distinct
ordered rooted pairs (x,y):

- both words are K-regular;
- for some r in [3,M], a marking satisfying (3) and a permitted
  single-cycle ordering (4), with the literal mismatches (4a),
  produce the rotation class of y;
- $y\notin{\rm Rot}(x)\cup{\rm Rot}(Rx)$.

Every member of this set has weight one. Write

$$
\mathcal T_{M,K,n}
  =\sum_{(x,y)\in\mathscr T_{M,K,n}}a(x)\overline{a(y)}.
\tag{5}
$$

Also define $\mathscr T^{\rm dist}_{M,K,n}$ by requiring that
the arc-start labels in its presentation are pairwise distinct, and
write $\mathcal T^{\rm dist}_{M,K,n}$ for its signed sum. On this
subclass (4) implies (4a). The theorem below applies separately to
both classes; an arbitrary subset of a signed sum need not satisfy
the same estimate, so the distinct-start case is proved directly.

Sections 4--5 prove that there is at most one admissible presentation,
including its number of arcs, on the regular set. In particular the
union over r and over partner orders has no concealed multiplicities.
The class is empty whenever n<3(L+1).

## 2. An explicit finite estimate

For every n>=1 define

$$
\begin{split}
E_{\rm phase}
&=n\sum_{r=3}^M\frac{(n\delta)^r}{r},\\
E_{\rm irr}
&=2M C^M n^{M+3}(C/N)^{K/2},\\
E_{\rm rev}
&=CM n^{M+3}(C/N)^K.
\end{split}
\tag{6}
$$

The theorem is the finite bound, for each
$\mathcal T^\diamond\in\{\mathcal T,\mathcal T^{\rm dist}\}$,

$$
\boxed{|\mathcal T^\diamond_{M,K,n}|
       \le E_{\rm phase}+E_{\rm irr}+E_{\rm rev}.}
\tag{7}
$$

The first term may also be replaced by

$$
n2^{-n}\sum_{r=3}^M\frac{[8(C-1)n]^r}{r},
\tag{8}
$$

and if n delta<1 then

$$
E_{\rm phase}
\le \frac{n(n\delta)^3}{3(1-n\delta)}.
\tag{9}
$$

The displayed bounds deliberately also include orders with an empty
length sum. They therefore remain upper bounds when not every
r<=M is feasible.

No constant in (6)--(9) is hidden in a fixed-order O symbol. This
permits M and K to grow with N.

## 3. Exact contraction of all changed endpoints

Let A=P-J. Double stochasticity gives AJ=JA=0, P^ell=J+A^ell,
and the squared Euclidean norm of each row and each column of A
is at most (C-1)/N. Hence, for ell>=2,

$$
|(P^\ell-J)_{ba}|
\le \frac{C-1}{N}2^{-(\ell-2)}.
\tag{10}
$$

This follows by placing A^{ell-2} between that row and column
and using \|A\|<=1/2. Nonnormality is immaterial.

For an ordered length tuple and a permitted sigma, let
$\mathcal B_\sigma$ be either the set of b-tuples satisfying (4a)
or the set of pairwise-distinct b-tuples. In the following proof
the same choice is made throughout. Both domains are unchanged by
cyclic relabelling of the arcs and by exchanging the two cyclic
orders. Summing the interior labels of the common arcs gives the
exact contraction

$$
\mathcal A_{\boldsymbol\ell,\sigma}
=\sum_{\boldsymbol b\in\mathcal B_\sigma}
 \sum_{\boldsymbol a}
\prod_{i=1}^r
(P^{\ell_i})_{b_i,a_i}
 U_{a_i,b_{\gamma_r(i)}}\,
 \overline{U_{a_i,b_{\sigma(i)}}}.
\tag{11}
$$

At fixed b this sum factors over a_i. Column unitarity, together
with the literal mismatch (4a), gives

$$
\frac1N\sum_a
 U_{a,b_{\gamma_r(i)}}\overline{U_{a,b_{\sigma(i)}}}=0
\quad\hbox{for every }i.
\tag{12}
$$

Thus (11) equals, exactly,

$$
\sum_{\boldsymbol b\in\mathcal B_\sigma}
\prod_{i=1}^r\left[
 \sum_a(P^{\ell_i}-J)_{b_i,a}
 U_{a,b_{\gamma_r(i)}}\overline{U_{a,b_{\sigma(i)}}}
\right].
\tag{13}
$$

This identity holds for every fixed allowed b-tuple before summing
over b. Every factor must be an error factor; mixed terms with a J factor
have already vanished. By (10) and Cauchy--Schwarz for the two
unit-norm columns, the absolute value of its i-th inner sum is
at most $\delta_i/N$, where
$\delta_i=(C-1)2^{-(\ell_i-2)}$.
There are at most N^r b-tuples. Therefore

$$
\boxed{
|\mathcal A_{\boldsymbol\ell,\sigma}|
\le\prod_i\delta_i
=(C-1)^r2^{-n+3r}
\le\delta^r.}
\tag{14}
$$

This cancellation uses the phases of the actual U and sums them
before taking an absolute value.

For clarity, the intermediate marked functional is

$$
\mathcal H^\diamond_{M,K,n}
=n\sum_x\sum_{r=3}^M\sum_{I\ {\rm admissible}}
           \sum_{\rm permitted\ partner\ orders}
                     a(x)\overline{a(y_{I,\sigma})}.
\tag{15}
$$

As before, n counts all labelled partner root positions. The
admissible markings and orders use the chosen b-domain from (11),
so that the superscript diamond selects the full literal class or
the distinct-start subclass throughout. The
exact count formula is

$$
\mathcal H^\diamond_{M,K,n}
=\sum_{r=3}^M\frac{n^2}{r}
\sum_{\substack{\ell_1+\cdots+\ell_r=n-r\\\ell_i\ge L}}
\sum_{\sigma\in\mathfrak C_r^\circ}
\mathcal A_{\boldsymbol\ell,\sigma}.
\tag{16}
$$

Indeed each unordered marking has r choices of which original
arc is first. There are n positions for this first arc and n
labelled roots for the partner. Summing all permitted orders
makes the relabelling invariant, as noted after (4).
This proves n^2/r, including for periodic words.

The number of length tuples is

$$
Q_{n,r,L}=
\begin{cases}
\binom{n-rL-1}{r-1},&n\ge r(L+1),\\
0,&n<r(L+1),
\end{cases}
\quad
Q_{n,r,L}\le\frac{n^{r-1}}{(r-1)!}.
\tag{17}
$$

Using q_r<=(r-1)! in (16) cancels the denominator in this last
bound. Equations (14)--(17) give (6)'s phase term and the
alternative (8). Summing a geometric series and using 1/r<=1/3
gives (9).

## 4. Unique presentation, independently of the cut number

Inside any matched arc the y-position minus the x-position is
constant modulo n. Call it the matching translation. Every arc
is right-maximal for this translation: the successors just beyond
its endpoint are b_gamma(i) and b_sigma(i), which are different
by (4a).

Suppose a pair of K-regular words admits two presentations, with
possibly different arc counts r and r'. Consider a new arc as
a proper cyclic interval of positions in x relative to the old
arc partition. If it crosses at least two old boundaries, it
contains an entire intervening old arc, whose length is at least
L+1=2K+3. Otherwise it meets at most two contiguous old pieces;
its own length at least 2K+3 makes one of them contain at least K
consecutive vertices. In both cases the new arc overlaps an old
arc in at least K consecutive positions. This argument has no
factor depending on r or r'.

On this overlap, both presentations match the same length-K
substring into y. Regularity of y forces the two matched
starting positions, and hence the two translations, to agree.
Starting from the overlap and moving forward, whichever arc
ended first would either fail to be right-maximal or force the
other to extend through its known mismatch. Therefore their
right endpoints agree.

Every new endpoint is thus an old endpoint. Applying the argument
with the presentations interchanged gives equality of the endpoint
sets, so r=r' and the marking sets agree. With the cuts fixed,
each long arc has a unique matched occurrence in regular y,
even if the first vertex labels of different arcs coincide;
these occurrences determine the partner cyclic order. Thus the
entire presentation is unique.

K-regular words are aperiodic, since a nontrivial period repeats
all their length-K cyclic substrings. Consequently the n partner
root positions in (15) give n distinct words. On regular pairs,
the marked multiplicity is exactly one, also after union over r.

There is no forward rotation pair in this regular set. Such a
rotation would supply a single global matching translation;
regularity would force all the arc translations to coincide
with it, contradicting their right-maximal mismatches.

Exchanging the two cyclic orderings gives another permitted
presentation after relabelling the arcs in the new original
order. The disagreement of their successors at every port is
preserved. Pairwise distinctness of all arc starts, when imposed,
is also preserved. Thus both marked relations and their regular unmarked
versions are invariant under exchanging x and y. Their sums,
and all edge-count restrictions below, are real.

## 5. Absolute exceptional-set estimates

### 5.1. Repeated oriented substrings

For fixed arc lengths and sigma, bound the product of the 2r
connector amplitudes in absolute value by (C/N)^r. The remaining
weight is the product of P over r disjoint directed paths, with
n formal positions and n-r internal edges.

Impose vertex-label identifications of rank h, so the quotient
has n-h vertex variables. Its internal graph has s<=r connected
components. A spanning forest has n-h-s edges, leaving h+s-r
internal factors outside the forest. Bound these by C/N and
sum the forest weight by deleting leaves, using the appropriate
row or column sums of P. The sum is at most N^s. Including the
r bounded connector pairs, the constrained absolute weight is
at most

$$
N^s(C/N)^{h+s-r}(C/N)^r
=C^s(C/N)^h\le C^r(C/N)^h.
\tag{18}
$$

This proof includes loops, repeated edges and nonnormal P.

An equality of two cyclic K-substrings with different starting
positions imposes K directed constraint edges on the position
set, with at most one incoming and one outgoing edge per position.
There are no loops. Each connected component is a path or a
cycle of length at least two; its identification rank is at
least half its number of edges. Thus the total rank is at least
K/2. In the nonempty range n>=3(L+1), K<n, so these K edges
are indeed based at distinct positions.

There are at most n^2 choices of the repeated substring starts.
For fixed lengths and sigma, (18) bounds the x-irregular weight
by n^2 C^r(C/N)^{K/2}. After multiplying by n^2/r and summing
lengths and permutations as in (17), it is at most
$C^r n^{r+3}(C/N)^{K/2}/r$.
The y-irregular bound is the same by exchanging the arc orders.
Their union, summed over r<=M, is at most E_irr in (6).
This is an absolute bound, so applies unchanged to any restriction
of the marked pair set.

### 5.2. Reversed partners

Put S_{xy}=sqrt(P_{xy}P_{yx}). Then S is symmetric and nonnegative,
has row sums at most one, and has entries at most C/N.
For reversed rotation pairs,

$$
|a(x)\overline{a(y)}|=\prod_jS_{x_j,x_{j+1}}.
\tag{19}
$$

If h disjoint pair identifications are imposed on the cyclic
positions, the quotient cycle is a connected multigraph with
n edges and n-h variables. Remove all edges outside a spanning
tree by the bound C/N, then sum its weight by the row sums of S.
The result is

$$
C(C/N)^h.
\tag{20}
$$

Any common forward arc in a reversed pair gives a reversed
matching substring within x. Since every arc has at least
2K+3 vertices, this forces constraints
$x_{i+u}=x_{j-u}$ for 0<=u<2K+3, for some positions i,j.
The position map p->i+j-p is an involution with at most two
fixed points. These constraints therefore impose at least K
distinct nontrivial disjoint pair identifications.
By (20) and a union over at most n^2 alignments, the total
constrained cyclic S-weight is at most
$n^2C(C/N)^K$.

For each original word, there are at most binom(n,r) markings,
q_r<=(r-1)! partner orders and n labelled partner roots.
Their product is at most n^{r+1}/r. Summing over r<=M proves
the absolute reversed-overlap bound E_rev in (6).
One may instead use the longest arc, of at least ceil(n/r)
vertices, to replace K by
$\max(0,\lfloor(\lceil n/r\rceil-2)/2\rfloor)$
in the individual r summand.

Removing both irregular pairs and reversed pairs from (15)
therefore leaves the actual unit-multiplicity class (5), or its
distinct-start version according to the selected b-domain, with
absolute error at most E_irr+E_rev. Combining with Section 3
proves the finite estimate (7).

## 6. A square-root-order corollary

Take, for all sufficiently large N,

$$
M=M_N=\left\lfloor\frac{\sqrt N}{10}\right\rfloor,\qquad
K=K_N=\left\lceil4M+4\log_2N\right\rceil,\qquad L=2K+2.
\tag{21}
$$

For every fixed 0<B<infinity and A_0>0, each actual pair class satisfies

$$
\boxed{\sup_{1\le n\le BN}|\mathcal T^\diamond_{M_N,K_N,n}|
       =O_{A_0,B,C}(N^{-A_0}).}
\tag{22}
$$

We check all three errors explicitly. Let u=log_2 N and B_+=max(B,1).
Then

$$
4M+4u\le K<4M+4u+1,\qquad
\delta\le(C-1)2^{-8M}N^{-8}.
\tag{23}
$$

Thus n delta<=B(C-1)2^{-8M}N^{-7}<1/2 for large N.
By (9),

$$
E_{\rm phase}
\le \tfrac23 B^4(C-1)^3\,2^{-24M}N^{-20}.
\tag{24}
$$

Since M grows proportionally to sqrt(N), this is smaller than
every fixed negative power of N.

For the irregular term, (21)--(23) give

$$
\begin{split}
E_{\rm irr}
&\le
2M C^{\,3M+2u+1/2}B_+^{\,M+3}
 N^{-M+3-2u}\\
&=
2M C^{1/2}B_+^3
 (C^3B_+/N)^M
 N^{\,3-2u+2\log_2 C}.
\end{split}
\tag{25}
$$

For N>= (C^3B_+)^2, the parenthesized power is at most N^{-M/2}.
The resulting bound is again smaller than N^{-A_0} for every
fixed A_0. This deduction is uniform in 1<=n<=BN.

The reversed error is no larger than the irregular error for
large N: E_rev/E_irr is at most
$\tfrac12 C^{1-M}(C/N)^{K/2}\le\tfrac12$,
because C>=1 and N>=C. Thus (24)--(25) prove (22).

This is not an empty class created by an impossible length
threshold. The shortest total length at r=M is

$$
M(L+1)=M(2K+3)
       =8M^2+O(M\log N)
       =\frac{2}{25}N+o(N).
\tag{26}
$$

In particular all orders up to M occur in these classes at n=N
for large N. Indeed take the word x=(0,1,...,N-1), any admissible
partition into r arcs, and sigma=gamma_r^{-1}. For r>=3 this
changes every successor. The starts are distinct, both words have
all vertex labels distinct and hence are K-regular, and the partner
is not a rotation of x. It is not a reversed rotation either: every
long arc retains an oriented internal edge of x, whereas a reversed
word with distinct labels contains only the reverse-oriented edges.
Thus this is a concrete pair in the distinct-start subclass for
every 3<=r<=M. The largest allowed order is asymptotic to sqrt(N)/10.
Also L is of order sqrt(N), so the
condition retains long common directed arcs and does not
claim to cover a positive fraction of all possible pair words.

For any weights with W=sup_{n,N}|w_{n,N}|<infinity, (22) also yields

$$
\frac1{N^2}\left|\sum_{1\le n\le BN}
 w_{n,N}\mathcal T^\diamond_{M_N,K_N,n}\right|
=O_{A_0,B,C}(W N^{-A_0})
\tag{27}
$$

for every fixed A_0, by applying (22) with a larger exponent.
There is no averaging over the parameter, the matrix or dimensions.

## 7. Exact structure of the positive cancellations

The distinct-start subclass contains large positive equal-edge-count
parts; these are not confined to a single common endpoint. Every
statement (28)--(32) in this section refers to that subclass only.
The broader literal-mismatch class may have repeated start labels,
for which the following endpoint classification is not asserted.
Let E_x record all directed edge multiplicities. For fixed r, lengths
and sigma, the connector difference in the distinct column b_j is

$$
e_{a_{\sigma^{-1}(j)}}-e_{a_{\gamma_r^{-1}(j)}}.
\tag{28}
$$

Internal edges cancel. Hence E_x=E_y if and only if

$$
a_i=a_{\pi(i)}\quad\hbox{for all }i,\qquad
\pi=\sigma^{-1}\gamma_r.
\tag{29}
$$

Thus the endpoint labels are constant on each cycle of pi.
Write c(pi) for its number of cycles. There are exactly N^{c(pi)}
assignments satisfying (29), even when some distinct cycles receive
the same vertex label. For each assignment the two path amplitudes
are equal, so the product of connector amplitudes is precisely the
product of the original P connector weights.

Let $\mathcal A^{=,{\rm dist}}_{\boldsymbol\ell,\sigma}$ restrict
the distinct-start version of (11) to equal edge counts.
Replace each long P entry by 1/N and sum the
b labels. The residual connector product is a product of r row
probability distributions, with atoms at most C/N. The probability
of a repeated b label is at most binom(r,2)C/N. Using (10) gives
the finite estimate

$$
\left|\mathcal A^{=,{\rm dist}}_{\boldsymbol\ell,\sigma}
              -N^{c(\pi)-r}\right|
\le N^{c(\pi)-r}
\left[\binom r2\frac CN+
      r\delta(1+\delta)^{r-1}\right].
\tag{30}
$$

This statement is uniform in lengths and in r, with the displayed
r-dependence. Summing it with the exact factor
$n^2Q_{n,r,L}/r$ gives a fully explicit finite estimate for the
positive marked r-arc sum. The same estimate holds for its
unmarked version after an absolute error at most E_irr+E_rev.

For illustration, keep r fixed and suppose K tends to infinity
with K=o(N), L=2K+2, delta=o(1/N), and the exceptional errors
tend to zero faster than every power. Uniformly on c_0<=t=n/N<=B,
the distinct-start contribution with r arcs and equal edge counts is

$$
\frac{t^{r+1}}{r!}
\sum_{\sigma\in\mathfrak C_r^\circ}
N^{c(\sigma^{-1}\gamma_r)+1}
 +O_{r,B,C}\!\left(
 (L+1)\sum_{\sigma\in\mathfrak C_r^\circ}
 N^{c(\sigma^{-1}\gamma_r)}
\right).
\tag{31}
$$

Indeed $Q_{n,r,L}=n^{r-1}/(r-1)!
+O_r(n^{r-2}(L+1))$, and (30) gives the remaining errors.
Formula (31) applies both to fixed M with K proportional to log N
and to any fixed-r part of the square-root-order class (21).
It is not used as a uniform asymptotic expansion for r growing.

For r=3 there is one permitted partner, and pi has one cycle:
the positive leading term is N^2 t^4/6. For r=4 there is again
one permitted partner, the reversed cyclic order of the four
directed arcs. To check this directly, the six cycle orders starting
at arc 1 are 1234, 1243, 1324, 1342, 1423 and 1432. The first five
retain at least one original successor, while 1432 retains none.
For this partner pi=gamma_4^2 has two cycles, giving instead
the positive leading term

$$
N^3t^5/24.
\tag{32}
$$

This partner reverses the order of the arcs, not the orientation
of their internal edges. It is not a physical reversed path.
Both terms are cancelled by the corresponding signed
different-edge-count parts of the distinct-start subclass to the
precision in (7). With logarithmic K the error in (31) is
O(N^{c(pi)} log N) for fixed r and each displayed cycle-count
contribution; in the square-root choice (21) it is instead
O(N^{c(pi)+1/2}). Classes with different cutoffs are not being
merged or silently identified.

More generally condition (4) makes pi have no fixed points.
Also pi is even, since sigma and gamma_r are both r-cycles.
These elementary constraints organize the possible cycle
counts in (31); they do not turn the unestimated complementary
pair set into a random ensemble.

## 8. The first remaining spectral estimate

The proof has removed markings, controlled both irregular words
and reversal overlap, and summed all permitted reconnections up
to a number of arcs of order sqrt(N). This is a concrete signed
cancellation for an unmarked subset of Z_n and the original
matrix family.

It still requires each common arc to contain order sqrt(N)
vertices in the corollary (21). Pairs without such long common
directed blocks are absent, as are reconnections outside the
specified order range. No estimate above supplies their total
complex phase sum.

The first unresolved quantity is therefore the original signed
weighted sum over
$Z_n\setminus\mathscr T_{M_N,K_N,n}$, at the required
N^{-2} time normalization. Neither the product cancellation
(13) nor the absolute forest estimate (18) bounds that complement
to the precision needed for H_diag. Claims about higher
factorial correlations would require additional arguments as well.
The actual CUE/Sine_2 conclusion remains open in this route.

## 9. Exact finite companion checks

The self-contained standard-library script
dual_growing_order_exact_checks.py, SHA256
63acd0e681cdcaaa4cf07b9540ed38a8cd7434c474da368aa949b2dddce32965,
was run successfully. It performs:

- 15,108 permitted-cycle checks for r=3,...,9, including the cycle
  counts of sigma^{-1} gamma_r and the exact inclusion-exclusion
  count of permitted Hamiltonian orders;
- 12,229 regular partner-class checks in a single dictionary over
  r=3,4,5, including 1,341 admitted presentations with repeated
  arc-start labels; no cross-order or same-order duplicate occurs;
- 156 exact nonzero endpoint factorizations using a nonflat rational
  orthogonal 4 by 4 matrix, with every centered J term removed
  separately; 139 of these have repeated start labels;
- 7,680 exact r=4 marked-pair checks, using a rational 2 by 2 unitary
  matrix and hence repeated start labels, which verify the factor
  n^2/r even for periodic words.

These finite checks do not establish any asymptotic estimate. The
proofs in Sections 1--8 do not depend on their outcomes.

