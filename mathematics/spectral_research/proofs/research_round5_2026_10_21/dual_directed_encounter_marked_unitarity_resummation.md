> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/dual_directed_encounter_marked_unitarity_resummation.md`. Embedded SHA256: `f3e6a9e37739a557c0a065ef685b9e341804f630ddff30a3618e24e1e65876c9`.
> [Thematic guide](../../topics/histories.md).

# Exact unmarked signed resummation of three long directed arcs

Round 5, 21 October 2026. This note proves a genuine phase cancellation
for a precisely defined, unmarked class of physical path pairs of the
original matrices. It also computes its positive and negative parts
associated with coalesced and noncoalesced cut endpoints. An intermediate
marked functional is evaluated first; a uniqueness argument and an
absolute exceptional-set bound then remove all its multiplicities.
The full pair trace outside this class, and H_diag, remain unestimated.

## 1. Inputs and statement

Let U be unitary of dimension N. As in the frozen physical kernel and
oscillation proofs, put

$$
P_{xy}=|U_{xy}|^2,\qquad J_{xy}=1/N.
$$

Assume a fixed C>=1 satisfies

$$
\max_{x,y}P_{xy}\le C/N,\qquad \|P-J\|_{\rm op}\le1/2.
\tag{1}
$$

For the original U_N these inequalities hold with C=9 for every
sufficiently large odd N. The fixed tau remains 10^{-80}. The analytic
sources are dual_physical_four_branch_kernel.md, SHA256
0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c,
and root_oscillatory_matrix_cancellation.md, SHA256
ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d.

Write $a(x)=\prod_{j\in\mathbb Z/n\mathbb Z}U_{x_j,x_{j+1}}$
for a rooted cyclic word x of length n. Let

$$
K=K_N=\lceil4\log_2N\rceil,\qquad L=L_N=4K+2.
\tag{2}
$$

An admissible marking I is an unordered set of three positions in x.
Starting at each marked position and stopping immediately before the
next one splits the word into three ordered directed arcs A_1,A_2,A_3.
The first vertex of A_i is denoted b_i and its last vertex a_i. Write
ell_i for its number of internal edges, so its number of vertices is
ell_i+1. Require

$$
\ell_i\ge L,\qquad b_1,b_2,b_3\ \text{pairwise distinct}.
\tag{3}
$$

In particular $\ell_1+\ell_2+\ell_3=n-3$.
The original connectors are the three edges $a_i\to b_{i+1}$;
indices i are cyclic modulo 3. The partner consists of the same directed
arcs in the other cyclic order, A_1,A_3,A_2, so its connectors are
$a_i\to b_{i-1}$.

There is only one other cyclic order of three distinct marked arcs.
Changing which marked position is named first changes neither the
partner rotation class nor its amplitude. Let y_I denote any rooted
representative of this partner class. Define the exact marked sum

$$
\mathcal H_{n,N}
 :=n\sum_x\ \sum_{I\ {\rm admissible}}
                  a(x)\overline{a(y_I)}.
\tag{4}
$$

The factor n counts all n choices of a root position on the partner,
including multiplicity when its rooted word is periodic. Equation (4)
is an intermediate marked observable. Section 6 first records its
exact multiplicity, and then proves that it becomes one outside an
exceptional set whose absolute contribution is smaller than any
fixed negative power of N.

Call a cyclic word K-regular if its n cyclic substrings of length K
are pairwise distinct. Define $\mathscr T_{n,N}$ to be the set of
ordered pairs (x,y) of K-regular words for which an admissible marking
I of x produces the rotation class of y, and for which
$y\notin{\rm Rot}(x)\cup{\rm Rot}(Rx)$. This is a set of distinct
rooted pairs, with unit weight for each pair. Write

$$
\mathcal T_{n,N}
 =\sum_{(x,y)\in\mathscr T_{n,N}}a(x)\overline{a(y)}.
\tag{4a}
$$

The class is empty if n<3L+3, since there cannot be an admissible
marking. Let $\mathcal T^=$ be its restriction to pairs with equal
directed edge counts, and $\mathcal T^\ne=\mathcal T-\mathcal T^=$.

Let $\mathcal H^=_{n,N}$ be the restriction of (4) to
a_1=a_2=a_3, and let
$\mathcal H^\ne_{n,N}=\mathcal H_{n,N}-\mathcal H^=_{n,N}$.
For every fixed B<infinity, uniformly for all integers 1<=n<=BN,

$$
\boxed{\mathcal H_{n,N}=O_{B,C}(N^{-12}),\qquad
       \mathcal T_{n,N}=O_{B,C}(N^{-12}).}
\tag{5}
$$

For every fixed 0<c<=B<infinity, uniformly for cN<=n<=BN,

$$
\boxed{\mathcal H^=_{n,N}
       =\frac{t^4}{6}N^2+O_{B,C}(N\log N),\qquad
       \mathcal H^\ne_{n,N}
       =-\frac{t^4}{6}N^2+O_{B,C}(N\log N),\quad t=n/N.}
\tag{6}
$$

The same two formulas hold with $\mathcal H^=,\mathcal H^\ne$
replaced by the unmarked sums $\mathcal T^=,\mathcal T^\ne$.
The first part in (6) is a nonnegative sum with identical amplitudes in
each pair. The negative part is calculated by exact column unitarity in
(5), not merely forced by the general inequality |Tr U^n|<=N.

Thus this gives an actual signed class cancellation inside Z_n, with
uniform control throughout every fixed Fourier time band. The
remaining coverage problem is that Z_n contains many pairs outside
this three-arc class.

## 2. Exact endpoint contraction and its count factor

For a positive length tuple ell satisfying (3), define

$$
\begin{split}
\mathcal A_{\boldsymbol\ell}
:={}&\sum_{\substack{b_1,b_2,b_3\\\text{pairwise distinct}}}
       \sum_{a_1,a_2,a_3}
\prod_{i=1}^3 (P^{\ell_i})_{b_i,a_i}\\
&\hspace{8mm}\cdot
\prod_{i=1}^3
 U_{a_i,b_{i+1}}\,\overline{U_{a_i,b_{i-1}}}.
\end{split}
\tag{7}
$$

The internal edge amplitudes of each arc occur once in each word with
opposite conjugations, giving their exact squared modulus. Summing all
internal vertex labels of an arc therefore gives
$(P^{\ell_i})_{b_i,a_i}$. Only its connector amplitudes retain phases.

The exact count is

$$
\boxed{\mathcal H_{n,N}
=\frac{n^2}{3}
\sum_{\substack{\ell_1+\ell_2+\ell_3=n-3\\\ell_i\ge L}}
\mathcal A_{\boldsymbol\ell}.}
\tag{8}
$$

Here is a full justification of both factors. Choose a first marked
position and read the three arcs cyclically from it. Every unordered
marking has exactly three such choices, even if the word itself is
periodic. Conversely, an ordered length tuple, all its arc vertex labels,
and a position at which the first arc starts determine a rooted original
word and a distinguished first marked position. There are n positions
for that first arc. Its total amplitude is independent of the choice
by rotation invariance. Therefore the sum in (4) before its factor n
is n/3 times the endpoint sum (7), summed over lengths. The remaining
factor n is exactly the already specified partner root marking.

Equivalently, concatenate arbitrary arc vertex words
$(A_1,A_2,A_3)$. Sum the pair consisting of any of the n labelled
rotations of $A_1A_2A_3$ and any of the n labelled rotations of
$A_1A_3A_2$, then divide by 3. This is another exact parametrization
of (4). Interchanging A_2 and A_3 and interchanging the two root
positions exchanges the pair. Hence the marked sum is real.
The same symmetry applies to its coalesced and noncoalesced restrictions.

## 3. Quantitative phase cancellation

Put A=P-J. Double stochasticity implies AJ=JA=0 and P^k=J+A^k.
Every row and every column of A has squared Euclidean norm at most
(C-1)/N, because

$$
\sum_j(P_{ij}-1/N)^2=\sum_jP_{ij}^2-1/N\le(C-1)/N.
\tag{9}
$$

Sandwiching A^{ell-2} between the corresponding row and column gives
the uniform entry estimate

$$
|(P^\ell-J)_{ba}|
 \le\frac{C-1}{N}\,2^{-(\ell-2)},\qquad \ell\ge2.
\tag{10}
$$

Define

$$
\delta_N=(C-1)2^{-(L-2)}\le(C-1)N^{-16}.
\tag{11}
$$

For each length in (7) its P entry is $N^{-1}(1+\epsilon_i)$,
with |\epsilon_i|<=delta_N. Replacing all three entries by 1/N
in (7) gives exactly zero. Indeed column unitarity says

$$
\sum_{a_i}U_{a_i,b_{i+1}}\overline{U_{a_i,b_{i-1}}}
=\mathbf1_{\{b_{i+1}=b_{i-1}\}}.
\tag{12}
$$

All three b labels are distinct, so the product of these Kronecker
symbols vanishes for every permitted triple. The cancellation in
(12) retains the original complex phases of U.

To bound the error, use

$$
\left|\prod_{i=1}^3(P^{\ell_i})_{b_i,a_i}-N^{-3}\right|
\le\frac{3\delta_N(1+\delta_N)^2}{N^3}.
\tag{13}
$$

For fixed b, the sum of the absolute connector product over a factors,
and each factor obeys

$$
\sum_a|U_{a,b_{i+1}}U_{a,b_{i-1}}|
\le
\left(\sum_a|U_{a,b_{i+1}}|^2
      \sum_a|U_{a,b_{i-1}}|^2\right)^{1/2}=1.
\tag{14}
$$

There are at most N^3 permitted b triples. Equations (12)--(14) prove

$$
|\mathcal A_{\boldsymbol\ell}|
\le3\delta_N(1+\delta_N)^2.
\tag{15}
$$

The number of length tuples in (8) is

$$
q_{n,L}=
\begin{cases}
\binom{n-3L-1}{2},&n\ge3L+3,\\
0,&n<3L+3.
\end{cases}
\tag{16}
$$

This follows by subtracting L from each of the three lengths and
counting nonnegative triples with prescribed sum. In particular
q_{n,L}<=n^2/2. Therefore (8) gives the explicit bound

$$
|\mathcal H_{n,N}|
\le\frac{n^4}{2}\delta_N(1+\delta_N)^2.
\tag{17}
$$

For n<=BN this is O_{B,C}(N^{-12}), proving the first part of (5).
Notice that
unitarity was applied before taking any absolute value. The absolute
estimate in (14) is used only for the error in replacing the long
P-arcs by their exactly known rank-one part.

## 4. The explicitly evaluated positive part

When a_1=a_2=a_3=v, all directed edges, including the connectors, have
the same multiplicities in both words. Thus a(y_I)=a(x) and the
summand is nonnegative. Its endpoint contraction is exactly

$$
\mathcal A^=_{\boldsymbol\ell}
=\sum_v\sum_{\substack{b_1,b_2,b_3\\\text{distinct}}}
      \prod_{i=1}^3(P^{\ell_i})_{b_i,v}
      \prod_{i=1}^3P_{v,b_i}.
\tag{18}
$$

For a row probability distribution P_{v,*}, let D_v be the probability
that three independent dummy draws have distinct values. This is just
a notation for the finite product sum in (18), after replacing its
three long arcs by 1/N. Since each row atom is at most C/N, a union
bound over the three pairs gives

$$
1-3C/N\le D_v\le1.
\tag{19}
$$

Consequently (10)--(13) imply

$$
\left|\mathcal A^=_{\boldsymbol\ell}-N^{-2}\right|
\le \frac{3C}{N^3}
    +\frac{3\delta_N(1+\delta_N)^2}{N^2}.
\tag{20}
$$

By (8), with the same count factor on this restricted set,

$$
\mathcal H^=_{n,N}
=\frac{n^2q_{n,L}}{3N^2}
 +O\!\left(\frac{Cn^4}{N^3}
           +\frac{\delta_N(1+\delta_N)^2n^4}{N^2}\right).
\tag{21}
$$

For cN<=n<=BN and large N, (16) gives
$q_{n,L}=n^2/2+O(n(L+1)+(L+1)^2)$. With L=O(log N),
(21) becomes

$$
\mathcal H^=_{n,N}
=\frac{n^4}{6N^2}+O_{B,C}(N\log N).
\tag{22}
$$

Together with (17) this proves both assertions in (6).
There is no factor e^{-t} in (22): the marked common endpoint v is
allowed to have additional unmarked visits inside the arcs. The exact
three-visit subclass considered in
dual_directed_encounter_exact_visit_classes.md has the different
coefficient e^{-t}t^4/6 precisely because it forbids those extra visits.

## 5. Forward overlap is impossible in the negative part

Let E_x(u,z) count the directed edges u->z in x. Internal arc edges are
identical in both paths and cancel in E_y-E_x. The connector ending
at the distinct vertex b_j has source a_{j-1} in x and source
a_{j+1} in y. Thus, in column b_j, the entire edge-count difference
is the vector

$$
e_{a_{j+1}}-e_{a_{j-1}}.
\tag{23}
$$

As the three columns b_j are distinct, E_x=E_y holds if and only if
a_{j+1}=a_{j-1} for all j. For three indices this is equivalent to
a_1=a_2=a_3. It follows that $\mathcal H^\ne$ consists entirely of
pairs with different directed edge counts. In particular none is
a cyclic rotation of the other word. This conclusion requires no
aperiodicity and no assumption about repeated interior labels.

Thus (22) and its negative counterpart give a phase-sensitive
resummation between equal-edge-count and different-edge-count parts
of the marked pair expansion. They do not just subtract two estimates
obtained from the size of the full trace.

## 6. Removing the marking multiplicity

### 6.1. Its exact value before the regularity restriction

Let d(y) be the number of distinct rotations of a word y. For fixed x,
let k(x,y) count the admissible unordered markings I for which the
partner rotation class is Rot(y). Each such marking contributes all
n labelled root positions, and each distinct y in this rotation class
occurs n/d(y) times. Therefore the exact relation to unmarked pairs is

$$
\mathcal H_{n,N}
=\sum_{x,y}r_n(x,y)a(x)\overline{a(y)},\qquad
r_n(x,y)=\frac{n}{d(y)}\,k(x,y).
\tag{24}
$$

The weights r_n are nonnegative integers. They are zero for pairs not
represented by this three-arc construction, and satisfy the elementary
bound

$$
0\le r_n(x,y)\le n\binom n3.
\tag{25}
$$

Equation (8) and the arc-word
parametrization also show the symmetry r_n(x,y)=r_n(y,x): exchanging
the two arc orderings and the two labelled roots is a bijection of
the parametrizing markings, preserving their threefold quotient.

On pairs with different edge counts, the restriction of (24) equals
$\mathcal H^\ne$, by Section 5.

### 6.2. Unique short substrings imply a unique marking

Suppose x and y are K-regular and admit two admissible three-arc
presentations. Each presentation pairs each arc of x with the
identical forward vertex word of its corresponding arc in y.
Within an arc the matched y-position minus the x-position is a
constant modulo n. Call it the matching translation of that arc.

Every arc is maximal under extending this match one step to the
right. Indeed the successor at its endpoint is b_{i+1} in the
original order and b_{i-1} in the partner order. These labels are
different by admissibility. This property applies to both proposed
presentations of the pair.

Take one arc from the second presentation. As a proper cyclic
interval of positions in x it is cut by the three boundaries of
the first presentation into at most four contiguous pieces. Its
number of vertices is at least L+1=4K+3. Hence one such piece
contains at least K consecutive vertices. On that piece both
presentations match the same K-letter word of x into y.
K-regularity of y implies that those matched starting positions
in y are equal. Therefore the matching translations of the
two intersecting arcs are equal.

Their right endpoints must now agree. Starting at a point in
the common interval, if the first endpoint came earlier, the
second matching arc would extend through the first arc's known
mismatch, which is impossible. If the second endpoint came
earlier, it would not be right-maximal because the first arc
still gives a matching successor with the same translation.
Thus every endpoint of the second partition is an endpoint
of the first partition. Both have three distinct endpoints,
so their endpoint sets and marking sets are identical.

This proves k(x,y)<=1 on K-regular pairs. A K-regular word is
aperiodic: a nontrivial cyclic period would give the same
length-K substring at two different positions. Hence d(y)=n.
By (24), every represented regular pair has r_n(x,y)=1.

There are also no forward rotation pairs in this regular set.
If y were a rotation of x, that rotation would supply one global
matching translation. K-regularity would force the translation
of every long common arc to equal it, contradicting the
right-maximal mismatch at every arc endpoint.

### 6.3. Absolute weight of irregular words

We prove that deleting the irregular pairs changes the marked
sum, and either of its edge-count restrictions, by less than
every fixed power of N^{-1}, uniformly for 1<=n<=BN.
Only n>=3L+3 need be considered; in this range K<n.

For fixed arc lengths in (8), take absolute values of the six
connector amplitudes and bound their product by (C/N)^3.
The remaining exact weight is the product of P over the n-3
internal edges of the three directed arcs.

More generally impose any vertex-label identifications of rank h
on these n positions, meaning that their quotient has n-h distinct
vertex variables. The internal graph is the quotient of three
paths, so it has some number s<=3 of connected components.
Choose a spanning forest of its underlying undirected graph.
It has n-h-s edges. Among the n-3 internal P factors there are
therefore h+s-3 factors outside this forest. Bound them by C/N.
The sum of the forest weight is at most N^s: remove one leaf
at a time, using a row or a column sum of P equal to one
according to the orientation of the incident edge.
Including the three bounded connector pairs, the constrained
absolute sum is consequently at most

$$
N^s(C/N)^{h+s-3}(C/N)^3
=C^s(C/N)^h\le C^3(C/N)^h.
\tag{25a}
$$

The count h+s-3 is nonnegative because a graph contains its
spanning forest. Loops and parallel factors are harmless:
they are among the factors outside the forest.

If two length-K cyclic substrings of x at different starting
positions p and q agree, their K constraints are
$x_{p+u}=x_{q+u}$, 0<=u<K. View these as directed edges
from p+u to q+u on the position set. Each position has at most
one outgoing and one incoming constraint edge. The components
are directed paths or cycles. There are no loops, since p!=q;
every cycle has length at least two. A path of j edges imposes
j independent identifications, and a cycle of j>=2 edges
imposes j-1>=j/2. Thus the rank of all these identifications
is at least K/2, including the possibility of opposite edges
forming a two-cycle.

There are at most n^2 choices of p,q. Dropping every other
constraint, including distinct b labels, can only enlarge
the absolute bound. For fixed length tuple, (25a) therefore
bounds its x-irregular part by
$n^2C^3(C/N)^{K/2}$, for N>=C.
Multiplying by n^2/3 and q_{n,L}<=n^2/2 in (8) gives at most
$C^3n^6(C/N)^{K/2}/6$.
The y-irregular part has the same bound by exchanging the
two arc orderings and their roots. The total loss is at most

$$
\frac{C^3n^6}{3}(C/N)^{K/2}.
\tag{25b}
$$

With K=ceil(4 log_2 N), this is O_{A_0,B,C}(N^{-A_0})
for every fixed A_0>0, uniformly for n<=BN.
Indeed the negative term $-(K/2)\log(N/C)$ has size
proportional to $-(\log N)^2$, which dominates any fixed
multiple of log N.

Thus the marked functional becomes a genuine unit-multiplicity
pair set after removing an absolutely negligible exceptional set.

As a compatible special case, the positive exact-three-visit
good-hub pairs from the companion note,
when their three visit gaps are at least L+1, occur in
$\mathcal H^=$ with the correct unit multiplicity. Their unique hub,
distinct incoming and outgoing neighbors, and exactly three visits
identify the three cut positions, and their words are aperiodic.
For arbitrary irregular pairs the exact multiplicity remains (24);
their total contribution has just been bounded in absolute value.

## 7. Removing reversed rotation pairs

This exclusion can be made without changing the leading negative term.
Define

$$
S_{uv}=\sqrt{P_{uv}P_{vu}}.
\tag{26}
$$

The matrix S is symmetric and nonnegative, each entry is at most C/N,
and each row sums to at most one, by Cauchy--Schwarz and the row and
column sums of P. If y belongs to Rot(Rx), then

$$
|a(x)\overline{a(y)}|=\prod_jS_{x_j,x_{j+1}}.
\tag{27}
$$

We need an elementary constrained-cycle bound. Impose on the n cyclic
positions h disjoint pair identifications of their vertex labels.
The quotient of the cycle is a connected multigraph with n edges
and d=n-h vertex variables. Choose any spanning tree of its underlying
connected graph. It uses d-1 of the factors S; bound the other n-d+1
factors by C/N. Summing the remaining tree weight by removing leaves
uses the row sums of S, at most one, and leaves only N choices for
the root. Thus the total constrained weight is at most

$$
N(C/N)^{n-d+1}=C(C/N)^h.
\tag{28}
$$

Loops and parallel edges cause no change: loops cannot be tree edges,
and surplus parallel edges are among the bounded factors. For d=1
the empty tree gives the same formula.

If a three-arc partner is a reversed rotation of x, at least one
arc has at least $r=\lceil n/3\rceil$ vertices. This arc occurs as
a forward substring in both words, hence as a reversed matching
substring in x. There are positions i,j such that

$$
x_{i+u}=x_{j-u},\qquad 0\le u<r,
\tag{29}
$$

with indices modulo n. The map on cyclic positions
p->i+j-p is an involution with at most two fixed points. The
constraints (29) therefore impose at least

$$
h_n=\max\left(0,\left\lfloor\frac{\lceil n/3\rceil-2}{2}\right\rfloor\right)
\ge n/6-2
\tag{30}
$$

distinct, disjoint nontrivial pair identifications. Indeed each such
pair covers at most two of the r constrained starting positions, and
only fixed points cover a position without an identification.

For each of the at most n^2 pairs i,j, apply (28). For a fixed original
word, there are at most $\binom n3$ markings and n labelled partner
roots. A union bound using (27) consequently gives the explicit
absolute bound for the entire marked reversed overlap:

$$
\left|\mathcal H_{\rm rev}\right|_{\rm absolute\ sum}
\le C n^3\binom n3(C/N)^{h_n}
\le\frac{C n^6}{6}(C/N)^{h_n}.
\tag{31}
$$

Here the middle notation means the sum of absolute values of its
marked terms, so the same estimate applies to either restriction
$\mathcal H^=$ or $\mathcal H^\ne$. For cN<=n<=BN this is
O(N^{-A_0}) for every fixed A_0>0, uniformly on that interval.
Indeed h_n grows at least linearly in N, whereas n^6 is polynomial
and C/N tends to zero.

For the uniform estimate throughout 1<=n<=BN, note that a nonempty
marking requires n>=3L+3=12K+9. Then (30) gives h_n>=2K-1.
The same expression in (31) is therefore smaller than every
fixed power of N^{-1} throughout the entire nonempty range.

Combining this bound with Section 6 yields

$$
|\mathcal T_{n,N}-\mathcal H_{n,N}|
 +|\mathcal T^=_{n,N}-\mathcal H^=_{n,N}|
 +|\mathcal T^\ne_{n,N}-\mathcal H^\ne_{n,N}|
=O_{A_0,B,C}(N^{-A_0})
\tag{32}
$$

for every fixed A_0>0, uniformly for 1<=n<=BN.
The unmarked assertions in (5)--(6) follow. All these classes
are invariant under exchanging x and y, by the arc-order
involution, so their signed sums are real.

In particular, for any uniformly bounded weights w_{n,N} and
fixed B, the entire unmarked class has the band-sum estimate

$$
\frac1{N^2}\left|
\sum_{1\le n\le BN}w_{n,N}\mathcal T_{n,N}\right|
=O_{B,C}(N^{-13}).
\tag{33}
$$

This is a signed quantitative result for a genuine class of
original-family pairs, with no marking multiplicity left.
It does not rely on the very small norm of the physical Q matrix.

## 8. The remaining coverage problem

The exact phase sum over all three endpoint labels first vanishes by
unitarity when the long common arcs carry the rank-one weight J.
The proved mixing estimate for P makes the replacement error small
enough after summing all Heisenberg-scale length compositions.
The regular-substring argument then removes the markings, and its
exceptional set is controlled in absolute value by a spanning-forest
estimate. This gives a genuine unmarked class with the cancellation
(33), while its same-edge-count and different-edge-count parts
have the respective positive and negative terms in (6).

Pairs admitting no such long three-arc presentation are absent
from $\mathscr T_{n,N}$. They include other reconnection
patterns and pairs sharing no such long directed arcs.
The current proof does not estimate their coherent sum.
If additional classes are summed later, overlaps with
$\mathscr T_{n,N}$ must also be accounted for as intersections
of actual pair sets.

For a check on this logical boundary, the normalized discrete Fourier
matrix F_N has |(F_N)_{xy}|^2=1/N. It obeys the assumptions used in
Sections 1--6 with P=J, and (12) makes the marked total identically
zero at every permitted length, without any error. The same
exceptional-set argument consequently makes its regular unmarked
class smaller than every fixed negative power in every fixed
time band. Nevertheless,
direct character orthogonality gives F_N^2 as coordinate reflection
and F_N^4=I, so $|\operatorname{Tr}F_N^n|^2=N^2$ whenever 4 divides n.
Thus this three-arc cancellation alone cannot control the full pair
trace. This is an auxiliary check of an inference, not a replacement
of the original matrix family; no spectral conclusion for U_N is
drawn from the Fourier example.

The first unproved estimate in this route is the signed weighted
sum over $Z_n\setminus\mathscr T_{n,N}$, with the precision required
for the CUE target after the N^{-2} time normalization. Bounds on
absolute term sums do not provide it: the explicitly evaluated
positive and negative parts inside the removed class are already
individually of order N^2 at each Heisenberg-scale time.
H_diag, and even its full pair-order instance for the original
family, remains open here.

