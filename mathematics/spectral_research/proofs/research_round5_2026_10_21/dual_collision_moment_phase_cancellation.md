> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/dual_collision_moment_phase_cancellation.md`. Embedded SHA256: `8528fb6bf6f633c3bb799261da69638ef0c9e55a30e062eb5e94dcab6440493a`.
> [Thematic guide](../../topics/histories.md).

# Collision observables retain the clean-arc phase cancellations

21 October 2026. Further round-5 calculation for the exact original
matrix family. This note proves a marked-observable estimate beyond
the square-root order, and then identifies exactly why that estimate
does not remove the remaining marking multiplicities. It does not
prove H_diag, and it does not enlarge the already proved unmarked
class without a further argument.

## 1. Setting and the observable

Let U be unitary, P_ab=|U_ab|^2, J_ab=1/N, and assume

$$
\max P_{ab}\le C/N,\qquad \|P-J\|_{\rm op}\le1/2,
\qquad C\ge1,\quad N\ge C.
\tag{1}
$$

For the original family these hypotheses have been proved, with
C=9, eventually along all odd dimensions at fixed tau. The input
sources are the four-branch kernel (SHA256 0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c)
and the oscillatory matrix proof (SHA256 ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d).

Use the arc notation of the frozen growing-order proof
dual_directed_encounter_growing_order_cancellation.md, SHA256
f0ffa2acc3e4b66b75620ee116a20cf8793c4d7efc40d5db67ded4259436c4e4.
Here all necessary new arguments are supplied explicitly.

For integers K>=1, M>=3 set

$$
L=2K+2,\qquad \delta=(C-1)2^{-2K}.
\tag{2}
$$

An unordered marking I of r positions of a rooted cyclic word x
produces r forward arc words, with internal edge lengths ell_i>=L,
starts b_i and ends a_i. The original successor is gamma(i)=i+1
modulo r. A partner is a single r-cycle sigma, with

$$
\sigma(i)\ne\gamma(i),\qquad
b_{\sigma(i)}\ne b_{\gamma(i)}\quad(1\le i\le r).
\tag{3}
$$

Either all literal-mismatch b-tuples, or only pairwise-distinct
b-tuples, may be used throughout. No regularity requirement is
imposed in this note; periodic words and repeated presentations
are deliberately retained.

Let R_K(x) be the number of unordered pairs of different starting
positions whose cyclic length-K substrings in x are equal. Thus
R_K(x)=0 is exactly K-regularity, and R_K is invariant under rotations.
For each integer j>=1 define the marked signed observable

$$
\mathcal H_{j;M,K,n}
=n\sum_x\sum_{r=3}^M\sum_{I}\sum_{\sigma}
 a(x)\overline{a(y_{I,\sigma})}
 [R_K(x)+R_K(y_{I,\sigma})]^j.
\tag{4}
$$

The sums use the selected b-domain and the length restrictions.
As in the earlier marked identity, the prefactor n counts labelled
partner roots even when some rotations coincide. It is not a count
of distinct partner words. If n<3(L+1) the observable is zero.

## 2. One repeated substring has exactly K independent constraints

For 1<=K<n/2, equality of length-K substrings starting at different
cyclic positions imposes identification rank exactly K on the n
formal vertex positions. Translate the first starting position to
zero and let d, 1<=d<n, be the displacement of the second start.
The K directed constraint edges are

$$
u\longrightarrow u+d\pmod n,\qquad 0\le u<K.
\tag{5}
$$

Each formal position has at most one incoming and one outgoing
constraint edge, and none is a loop. If the underlying undirected
multigraph contained a cycle, its edges would form a complete
directed orbit of translation by d. This includes the possible
two-edge cycle when d=n/2. Write g=gcd(n,d). Every complete orbit
is one residue class modulo g and, in the ordinary representative
interval [0,n-1], has span n-g>=n/2. Such an orbit cannot have all
its tails in the interval [0,K-1], whose span is K-1<n/2.
There is therefore no cycle: the constraint graph is a forest with
K edges, and its rank is K.

In the nonempty range of (4), n>=3(2K+3), so K<n/2 is automatic.
The same rank statement holds for a repeated substring in y:
the arc reordering is a permutation of the n formal positions,
which does not change the rank of the identifications.

## 3. An arbitrary constraint event only spoils affected arcs

Fix r, the ordered lengths, sigma, and a conjunction E of equality
constraints between formal vertex positions. Let S be the set of
arc indices touched by these constraints, s=|S|, and let their
total identification rank be h. All constraints lie in these s
arc words by definition.

For an untouched arc i, summing its internal variables and then
its endpoint a_i gives, at each fixed allowed b-tuple,

$$
F_i(b)=\sum_a(P^{\ell_i})_{b_i a}
 U_{a,b_{\gamma(i)}}\overline{U_{a,b_{\sigma(i)}}}.
$$

The event E does not depend on any variable inside this arc,
including its endpoint or start as formal positions. The b-domain
depends only on b, so the a-sum is still free. Column orthogonality
and the literal mismatch in (3) give exactly

$$
F_i(b)=\sum_a(P^{\ell_i}-J)_{b_i a}
 U_{a,b_{\gamma(i)}}\overline{U_{a,b_{\sigma(i)}}},
\qquad |F_i(b)|\le\delta_i/N,
\tag{6}
$$

where delta_i=(C-1)2^{-(ell_i-2)}. The last bound follows from
the row/column sandwich for P-J and the Cauchy--Schwarz inequality
for two unit-norm columns of U.

For the s affected arcs, take the modulus and bound their 2s
connector amplitudes by (C/N)^s. The remaining internal graph
is a union of s paths, with v formal positions and v-s edges.
After imposing rank h, it has v-h variables and t<=s connected
components. A spanning forest has v-h-t edges. Bound the
h+t-s remaining internal P factors by C/N and sum the forest
by deleting leaves, using row or column sums one. Including the
affected connectors, the constrained positive sum is at most

$$
N^t(C/N)^{h+t-s}(C/N)^s
=C^t(C/N)^h\le C^s(C/N)^h.
$$

The untouched starts now occur in no remaining factor: their
possible appearances in affected connectors were removed by the
pointwise connector bound. Enlarge the b-domain to all labels,
then sum these r-s free starts. The resulting N^{r-s} exactly
cancels the N^{-(r-s)} in (6). Thus the exact endpoint contraction
restricted to E obeys

$$
\boxed{
|\mathcal A_{\boldsymbol\ell,\sigma}(E)|
\le C^s(C/N)^h\prod_{i\notin S}\delta_i.}
\tag{7}
$$

The unaffected J cancellations occur before any modulus. The
subsequent forest estimate is absolute. In particular (7) does
not treat a complex weight as a probability.

## 4. Uniform collision-moment theorem

A length-K block meets at most two arcs: crossing two boundaries
would require passing through an entire intervening arc of at
least L+1=2K+3>K vertices. Therefore one event counted by R_K(x)
or R_K(y) touches at most four arcs. An ordered conjunction of j
such events touches at most 4j arcs. Its rank is at least K by
Section 2, since adding equalities cannot decrease the rank of
the first event.

Assume n delta<1. Then delta<1 in the nonempty range. For each
ordered j-tuple of collision events, (7) gives

$$
|\mathcal A(E)|
\le C^{4j}(C/N)^K\,
\delta^{\max(r-4j,0)}.
\tag{8}
$$

There are at most 2 binom(n,2)<=n^2 available collision events
(including both words), so expanding [R_K(x)+R_K(y)]^j has at
most n^{2j} ordered event tuples, with repetitions allowed.

The exact root/mark factor is n^2/r after summing all permitted
orders. There are at most n^{r-1}/(r-1)! length tuples and at most
(r-1)! permitted Hamiltonian orders. Consequently

$$
|\mathcal H_{j;M,K,n}|
\le C^{4j}(C/N)^K
\sum_{r=3}^M\frac{n^{r+2j+1}}r
 \delta^{\max(r-4j,0)}.
\tag{9}
$$

For 3<=r<4j bound n^{r+2j+1} by n^{6j+1} and 1/r by one.
For r>=4j sum the geometric tail in n delta. This proves the
finite estimate

$$
\boxed{
|\mathcal H_{j;M,K,n}|
\le C^{4j}n^{6j+1}(C/N)^K
\left(4j+\frac1{1-n\delta}\right).}
\tag{10}
$$

It is uniform in M: infeasible orders contribute zero, and the
geometric upper bound includes all feasible orders without
assuming that their number is fixed. For C=1, zero powers are
interpreted as empty products when their exponent is zero; the
same estimates follow directly from (6)--(9).

## 5. Logarithmic moment orders and all feasible long-arc counts

Take

$$
u=\log_2N,\quad K=\lceil4u\rceil,\quad L=2K+2,
\qquad 1\le j\le\lfloor u/3\rfloor.
\tag{11}
$$

For fixed B>0 and 1<=n<=BN,
delta<=(C-1)N^{-8}, so n delta<1/2 eventually. Put B_+=max(B,1).
Since 4j<=4u/3, 6j+1<=2u+1 and K<4u+1, (10) yields

$$
|\mathcal H_{j;M,K,n}|
\le C B_+(4u/3+2)
N^{-2u+1+(16/3)\log_2C+2\log_2B_+}.
\tag{12}
$$

Thus for every fixed A_0>0,

$$
\sup_{M\ge3}\sup_{1\le n\le BN}
\sup_{1\le j\le\lfloor(\log_2N)/3\rfloor}
|\mathcal H_{j;M,K,n}|
=O_{A_0,B,C}(N^{-A_0}).
\tag{13}
$$

In particular all feasible reconnection orders can be retained:
their maximum is floor(n/(L+1)), which is of order N/log N at
n of order N. This is a theorem for the marked collision
observables (4), not for the unmarked regular pair class.

The marked moment of order zero is independently bounded by
n(n delta)^3/[3(1-n delta)] by the all-port contraction (14)--(16)
in the frozen growing-order proof. With exactly (11), this gives
O_{B,C}(N^{-20}) uniformly for all n<=BN, not superpolynomial
decay. Increasing the fixed coefficient of log N in K obtains
any prescribed fixed power for that order-zero uniform bound;
no such adjustment is needed for the positive-order estimate (13).
On a Heisenberg-time band cN<=n<=BN the stronger product bound
(C-1)^r 2^{-n+3r} is available, but it is not needed here.

## 6. Exact obstruction to inferring the zero-collision indicator

To remove irregular presentations one would need the marked sum
with the factor

$$
\boldsymbol1_{\{R_K(x)+R_K(y)=0\}},
\tag{14}
$$

and then the uniqueness argument would identify it with an
unmarked class. Equations (10)--(13) do not establish this.
The weights a(x) conjugate(a(y)) are signed or complex, so the
absolute value of a signed union sum is not bounded by a union
bound on the absolute values of signed event sums.

The failure is algebraic and persists even when an increasing
number of moments is known exactly. For an integer H>=1 define
the finite signed measure

$$
\mu_H=\sum_{q=0}^{H}(-1)^q\binom Hq\delta_q.
\tag{15}
$$

For every polynomial p of degree less than H,

$$
\int p(q)\,d\mu_H(q)=0,
\tag{16}
$$

because the H-th forward finite difference of p is zero. In
particular the total signed mass and all moments through order
H-1 vanish. Nevertheless

$$
\mu_H(\{0\})=1,\qquad \|\mu_H\|_{\rm TV}=2^H.
\tag{17}
$$

One may take H=floor((log_2 N)/3)+1 to match the moment range in
(13). This is not asserted to arise from the original U_N. It
is an exact counterexample to the inference from the displayed
moment information alone to (14), and makes clear which positivity
is absent. For the actual coherent path weights, the separately
proved exponential equal-edge-count classes already show that
large total variation is a material issue.

The next missing estimate in this extended route is quantitative
control of the signed zero-collision indicator, or an alternative
exact way to divide out presentation multiplicities, when the
number of arcs is allowed to be of order N/log N. The earlier
square-root-order theorem avoids this issue through a genuine
absolute exceptional-set bound. It remains the proved unmarked
result; (13) must not be substituted for it.

## 7. Finite exact checks

The companion dual_collision_moment_exact_checks.py, SHA256
958e95892d1191c45846ccdae66708fe79d7bb4887ead4dd9fcabc0e6bb780e1,
ran successfully. It checks 34,655 repeated-block configurations
with 3<=n<=60 and K<n/2, always obtaining rank exactly K.
For a nonflat rational orthogonal 2 by 2 matrix and a four-arc
event touching exactly two arcs, it sums 128 endpoint terms and
verifies a nonzero full contraction equals the version with every
untouched P^ell replaced by P^ell-J; the resulting fraction also
satisfies (7). Finally it checks 465 exact zero moments for (15),
with unit mass at zero and total variation 2^H for each H<=30.
These finite tests do not replace the proofs above.
