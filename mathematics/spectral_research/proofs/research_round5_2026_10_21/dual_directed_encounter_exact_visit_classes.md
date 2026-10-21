> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/dual_directed_encounter_exact_visit_classes.md`. Embedded SHA256: `1ed54e4498189b1f373840bdbff223f7ee2ace54c83c6333bc396a3ce9c6a854`.
> [Thematic guide](../../topics/histories.md).

# Exact visit generating functions and positive directed encounter classes

Round 5, 21 October 2026. This note concerns the exact original matrices U_N.
It proves an asymptotic formula for specific, explicitly disjoint coherent
path classes at every time n comparable to N. It does not estimate their
signed complement and does not prove or disprove H_diag.

The only analytic input about the original family is the already proved
physical transition estimate

$$
P_{xy}=|(U_N)_{xy}|^2,\qquad J_{xy}=N^{-1},\qquad
\max_{x,y}P_{xy}\le C/N,\qquad \|P-J\|_{\rm op}\le\tfrac12.
\tag{1}
$$

Here C is independent of N, and (1) holds for every sufficiently large odd N.
One may take C=9. The input is proved in the frozen files

- dual_physical_four_branch_kernel.md, SHA256
  0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c;
- root_oscillatory_matrix_cancellation.md, SHA256
  ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d.

Their combination was independently reconstructed in
dual_audit_physical_cycle_classes.md, SHA256
953578dbba89c8aa86994c63a9289ffe26803795f2dac7055e3f306bad9d79ae.
The proof below applies to every doubly stochastic P satisfying (1), and
uses its entries only as exact nonnegative weights of physical paths.
It makes no stochastic approximation to the coherent quantum evolution.

## 1. Statements

Let x=(x_0,...,x_{n-1}) be a rooted cyclic word on the N vertices, with
indices read modulo n. Put

$$
a(x)=\prod_{j=0}^{n-1}U_{x_j,x_{j+1}},\qquad
w(x)=|a(x)|^2=\prod_{j=0}^{n-1}P_{x_j,x_{j+1}}.
\tag{2}
$$

For a vertex v, let K_v(x) be its number of occurrences in x. For every
fixed B>0, uniformly in v, |z|<=2 and 1<=n<=BN, we prove

$$
\left|\sum_xw(x)z^{K_v(x)}
             -\exp\!\left(\frac nN(z-1)\right)\right|
\le \frac{K_{B,C}}{N}+N(3/4)^n
\tag{3}
$$

for all sufficiently large N. Thus, for every fixed nonnegative integer m,

$$
\sum_xw(x)\mathbf1_{\{K_v(x)=m\}}
=e^{-t}\frac{t^m}{m!}
 +O_{B,C}(N^{-1})+O\!\left(N(3/4)^n\right),
\qquad t=n/N.
\tag{4}
$$

The constants in (3)--(4) can be chosen independently of m. Only fixed m
will be used in the combinatorial statements.

Fix m>=3. Call v a good m-hub for x if:

1. K_v(x)=m;
2. all m positive cyclic gaps between its consecutive visits are at least 3;
3. the m immediate predecessor vertices and the m immediate successor
   vertices at these visits are 2m pairwise distinct vertices.

Let g_m(x) count its good m-hubs. At a good m-hub the cyclic path consists
of m directed excursions from v back to v, with no internal visit to v.
Keeping each excursion unchanged, put these excursions into any other
cyclic order. Let $\mathscr E^{(m)}_n$ be the set of ordered pairs (x,y)
where y is any distinct cyclic rotation of any such nonoriginal ordering,
for any good m-hub v of x. In particular this is a set of pairs, not a
multiset. Sections 5--6 prove that its definition introduces no hidden
multiplicity, and that all its pairs lie outside both the original rotation
class and the reversed rotation class.

Its exact coherent sum is nonnegative and equals

$$
\mathcal E^{(m)}_{n,N}
 :=\sum_{(x,y)\in\mathscr E^{(m)}_n}a(x)\overline{a(y)}
 =n\big((m-1)!-1\big)\sum_xw(x)g_m(x).
\tag{5}
$$

For every fixed m>=3 and 0<c<B<infinity, uniformly over the integers
cN<=n<=BN and all sufficiently large odd N,

$$
\boxed{\mathcal E^{(m)}_{n,N}
 =N^2\,\frac{(m-1)!-1}{m!}\,e^{-t}t^{m+1}
  +O_{m,B,C}(N).}
\tag{6}
$$

The threshold implicit in (6) may depend on c; the displayed error
constant may be taken independent of c once the exponentially small
term in (3) has fallen below 1/N.

Moreover, all the sets $\mathscr E^{(m)}_n$, m>=3, are pairwise disjoint.
At n=2N this yields a quantitative forced cancellation. Define the signed
complement

$$
\mathcal W_{n,N}
 =\sum_{(x,y)\notin
       \mathscr E^{(3)}_n\cup\mathscr E^{(4)}_n}
          a(x)\overline{a(y)}.
\tag{7}
$$

Then this is a real number and

$$
\boxed{\mathcal W_{2N,N}
 \le-\left(\frac{28}{3}e^{-2}-1\right)N^2+O_C(N).}
\tag{8}
$$

The coefficient in parentheses is strictly positive. Thus already two
explicit fixed encounter orders require a macroscopic negative coherent
contribution from their complement for the actual original family.
This is a cancellation constraint, not a computation of that complement
and not a spectral universality theorem.

## 2. Exact rank-one generating function

For any doubly stochastic P satisfying (1), let A=P-J. The constant vector
is invariant under P and its adjoint, so PJ=JP=J and AJ=JA=0. The restriction
of P to the orthogonal complement of constants is the restriction of A,
and \|A\|<=1/2. It follows by induction that

$$
P^k=J+A^k,\qquad k\ge1.
\tag{9}
$$

Every entry of every P^k, k>=1, is at most C/N: multiply on the left by
the row stochastic matrix P^{k-1} and use the entry bound for P.
We also need a stronger diagonal estimate. Row and column stochasticity
give, respectively,

$$
\sum_j|A_{vj}|^2=\sum_jP_{vj}^2-\frac1N\le\frac{C-1}{N},
\qquad
\sum_j|A_{jv}|^2\le\frac{C-1}{N}.
\tag{10}
$$

Therefore

$$
|A_{vv}|\le C/N,\qquad
|(A^k)_{vv}|
 \le\frac{C-1}{N}\,2^{-(k-2)},\quad k\ge2.
\tag{11}
$$

Indeed the second expression is the scalar product of the v-th row of A,
the operator A^{k-2}, and the v-th column of A; apply Cauchy--Schwarz and
(10). These bounds are valid even when A is not normal.

Put E_v=e_ve_v^*, eta=z-1, and D_z=I+eta E_v. Direct matrix multiplication
and taking the trace show

$$
G_{v,n}(z):=\operatorname{Tr}(D_zP)^n
 =\sum_x w(x)z^{K_v(x)}.
\tag{12}
$$

For |lambda|>1/2 set

$$
R_v(\lambda)
 =e_v^*A(\lambda-A)^{-1}e_v
 =\sum_{k\ge1}\lambda^{-k}(A^k)_{vv}.
\tag{13}
$$

By (11), if r=|lambda|>=3/4 then

$$
|R_v(\lambda)|
 \le\frac{C}{Nr}+
       \frac{C-1}{Nr(r-1/2)}
 \le\frac{20C}{3N}.
\tag{14}
$$

No logarithmic cutoff or assertion of independent visits is used.

Let det_perp mean the determinant on the orthogonal complement of
constants. For |lambda|>1/2 the exact identity is

$$
\det(\lambda-D_zP)
=\det_{\perp}(\lambda-A)
  \left[(\lambda-1)\big(1-\eta R_v(\lambda)\big)-\frac{\eta}{N}\right].
\tag{15}
$$

To verify it, first suppose lambda!=1. The rank-one determinant formula
for X+uv^* is det(X)(1+v^*X^{-1}u) when X is invertible. It follows
directly by multilinearity of the determinant: terms selecting the
rank-one summand from two columns vanish, and the terms selecting it
once sum to v^*adj(X)u. Apply it to
lambda-P-eta e_ve_v^*P. The constant line and its orthogonal complement
are reducing for P, whence

$$
\det(\lambda-P)
 =(\lambda-1)\det_\perp(\lambda-A),
\quad
e_v^*P(\lambda-P)^{-1}e_v
 =\frac1{N(\lambda-1)}+R_v(\lambda).
\tag{16}
$$

This gives (15) for lambda!=1; analytic continuation gives (15) also at
lambda=1. No scalar eigenvalue has been discarded in this computation.

## 3. Uniform extraction of the dominant root

Take |z|<=2, so |eta|<=3, and take
N>=max(288,40C). Equation (14) ensures |eta R_v|<=1/2 outside the disk
|lambda|<3/4. If lambda is an eigenvalue of D_zP in that region,
det_perp(lambda-A) is nonzero, and (15) forces

$$
\lambda=F_{v,z}(\lambda)
 :=1+\frac{\eta}{N(1-\eta R_v(\lambda))},
\qquad |\lambda-1|\le6/N.
\tag{17}
$$

The map F sends the closed disk $\mathcal D_N=\{|\lambda-1|\le6/N\}$
into itself. On this disk |lambda|>=7/8 and the resolvent derivative
satisfies

$$
|R_v'(\lambda)|
 =|e_v^*A(\lambda-A)^{-2}e_v|
 \le\frac{1/2}{(|\lambda|-1/2)^2}<4.
\tag{18}
$$

Consequently |F'|<=144/N<=1/2 there. Integrating the derivative along a
line segment in this convex disk gives the same Lipschitz bound for F.
Iteration from any point of the disk is Cauchy by the geometric bound
on successive differences, stays in the disk, and converges to a unique
fixed point $\lambda_v(z)$.

This fixed point is a simple zero of the scalar bracket in (15).
Indeed that bracket is
$(1-\eta R_v(\lambda))(\lambda-F_{v,z}(\lambda))$, whose derivative
at the fixed point is nonzero by |eta R_v|<=1/2 and |F'|<=1/2.
Thus $\lambda_v(z)$ is a simple eigenvalue, and every other eigenvalue
of D_zP has modulus strictly smaller than 3/4. This includes the
cases eta=0 and z=0.

Using (14) again in (17) gives the quantitative expansion

$$
\left|\lambda_v(z)-1-\frac{\eta}{N}\right|
 \le\frac{18}{N}|R_v(\lambda_v(z))|
 \le\frac{120C}{N^2}.
\tag{19}
$$

On $\mathcal D_N$ use the logarithm defined by its power series around 1.
For |u|<=1/2,
|\log(1+u)-u|<=|u|^2. Hence for 1<=n<=BN,

$$
\left|n\log\lambda_v(z)-\frac nN\eta\right|
 \le\frac{B(120C+36)}{N}.
\tag{20}
$$

For all sufficiently large N the right side is at most 1. The elementary
integral identity $e^a-e^b=(a-b)\int_0^1e^{b+s(a-b)}\,ds$ then yields

$$
\left|\lambda_v(z)^n-e^{(n/N)\eta}\right|
 \le e^{3B+1}\frac{B(120C+36)}{N}.
\tag{21}
$$

Trace of a matrix power is the sum of the corresponding eigenvalue
powers, counting algebraic multiplicities, even for a nonnormal matrix.
For completeness, choose an eigenvector over the complex numbers and
extend it to a basis. This makes the matrix block upper triangular;
iterate on the lower diagonal block. Powers preserve this triangular
form, so their traces are the sums of the powers of the diagonal entries.
The other N-1 eigenvalues just located contribute at most N(3/4)^n.
Combining with (21) proves (3), with for example
$K_{B,C}=e^{3B+1}B(120C+36)$.

Finally extract the coefficient of z^m by integrating z=e^{iu},
0<=u<=2pi, against e^{-imu}. The integral of z^j is zero unless j=m.
The error in (3) bounds the error of this coefficient, while
$e^{t(z-1)}=e^{-t}\sum_{m\ge0}t^mz^m/m!$. This proves (4).

## 4. Removing short gaps and endpoint coincidences

Write

$$
V_{m,n}=\sum_xw(x)\sum_v\mathbf1_{\{K_v(x)=m\}},
\qquad
M_{m,n}=\sum_xw(x)g_m(x).
\tag{22}
$$

Summing (4) over v gives

$$
V_{m,n}=N e^{-t}\frac{t^m}{m!}
 +O_{B,C}(1)+O\!\left(N^2(3/4)^n\right).
\tag{23}
$$

We show, for each fixed m>=3 and n<=BN, that

$$
0\le V_{m,n}-M_{m,n}
\le
\frac{2C^mB^{m-1}}{(m-2)!}
 +\frac{\binom{2m}{2}C^{m+1}B^m}{m!}.
\tag{24}
$$

All estimates below sum nonnegative path weights. Thus it is legitimate
to remove the requirement of exactly m visits whenever an upper bound
is needed.

First mark m distinct cyclic positions all occupied by one vertex v.
If their positive ordered cyclic gaps are ell_1,...,ell_m, with sum n,
the weight at prescribed cuts is

$$
\prod_{i=1}^m(P^{\ell_i})_{vv}.
\tag{25}
$$

In a sum over all unordered marked m-subsets, the conversion to ordered
positive gap tuples has factor n/m: choose the first cut in n ways;
each unordered subset is obtained m times, once from each of its cuts.
Rotation invariance of w makes each choice of the first cut have the
same total weight for a fixed gap tuple. This explains the factor
without any assumption that the underlying word is aperiodic.

For an exact-m hub with a gap 1 or 2, its set of visits is such a marked
subset. Apply the union bound to the m choices of the short gap. The
factor m cancels the denominator in n/m. There are two possible short
gap lengths, and for each of them at most
$n^{m-2}/(m-2)!$ positive tuples for the other m-1 gaps. By the entry
bound for every P^ell, summing (25) over v is at most C^m/N^{m-1}.
The resulting loss is at most

$$
\frac{2C^m}{(m-2)!}\left(\frac nN\right)^{m-1}.
\tag{26}
$$

It remains to consider all gaps at least 3. Number the outgoing
neighbors b_i and incoming neighbors a_i along the i-th excursion.
The exact weight at prescribed gaps and prescribed neighbors is

$$
\prod_{i=1}^m
 P_{v,b_i}(P^{\ell_i-2})_{b_i,a_i}P_{a_i,v}.
\tag{27}
$$

Since ell_i-2>=1, each middle entry is at most C/N, without a mixing
time requirement. After removing these middle entries by an upper
bound, the remaining factors are the product of 2m probability
distributions: m copies of row v of P and m copies of column v of P.
Each atom has mass at most C/N. Any specified pair of these independent
dummy coordinates coincides with probability at most C/N, by summing
the product of their probabilities and bounding one factor by its
maximum. Thus their union of coincidences has total probability at
most $\binom{2m}{2}C/N$.

For fixed v and a fixed gap tuple the coincident-neighbor weight in
(27) is therefore at most
$\binom{2m}{2}C^{m+1}/N^{m+1}$. Sum v and use the factor n/m.
There are at most $n^{m-1}/(m-1)!$ positive gap tuples; restricting to
gaps at least 3 only reduces their number. This gives the upper bound

$$
\frac{\binom{2m}{2}C^{m+1}}{m!}
   \left(\frac nN\right)^m.
\tag{28}
$$

Equations (26)--(28) prove (24). The argument remains valid if a word
has additional unmarked visits to v, since those were deliberately
allowed only in the bounding sums. Combining (23) and (24) gives

$$
M_{m,n}
 =N e^{-t}\frac{t^m}{m!}
  +O_{m,B,C}(1)+O\!\left(N^2(3/4)^n\right).
\tag{29}
$$

In particular the good-hub cutoff uses the fixed gap 3, not a
logarithmically growing separation.

## 5. Exact excursion rearrangements and multiplicity

Fix a word x and a good m-hub v. Its visits split the directed cycle
into m excursions $A_1,\ldots,A_m$, listed in the original cyclic
order. Each starts at v with successor b_i and ends at v with
predecessor a_i. The no-internal-v property follows from exactly m
visits; the a_i and b_i are all distinct by definition.

There are (m-1)! cyclic orders of m distinct excursions. Their
concatenation gives a cyclic word. This construction is independent
of the choice of which original visit is named first: changing that
choice merely relabels the excursions and leaves the set of new
cyclic orders unchanged. Exclude the original cyclic order.

Every new word traverses the same directed edges as x, with the same
multiplicities. Multiplication of scalar matrix entries commutes, so

$$
a(y)=a(x)
\tag{30}
$$

for it and for every cyclic rotation of it. This is an equality of
complex amplitudes, not an estimate of their absolute values.

To verify all possible identifications, use the local trigram counts

$$
T^x_w(u,z)=
\#\{j:(x_{j-1},x_j,x_{j+1})=(u,w,z)\}.
\tag{31}
$$

They are invariant under cyclic rotation. Reordering excursions at v
leaves $T_w$ unchanged for every w!=v, since it leaves the interior
and endpoint-neighbor portions of each excursion unchanged. At v,
the trigrams are

$$
(a_i,v,b_{\sigma(i)}),\qquad i=1,\ldots,m,
\tag{32}
$$

where sigma is the successor permutation of the chosen cyclic order.
It is an m-cycle. Since all a_i are distinct and all b_i are distinct,
these trigrams determine sigma uniquely. Therefore different cyclic
orders yield different rotation classes, and every nonoriginal cyclic
order changes $T_v$ nontrivially.

This proves simultaneously:

- no nonoriginal ordering belongs to Rot(x);
- different nonoriginal cyclic orders at the same hub give disjoint
  rotation classes;
- different hubs v!=w cannot give the same partner rotation class:
  one would change exactly the centered trigram data at v, and the
  other exactly at w.

In the last statement, “exactly” refers to the support of the nonzero
difference of the arrays $T^y-T^x$, not to a claim about the number
of individual changed trigrams.

Every such word, including x itself, is aperiodic. Indeed, if a word
were a repetition of a shorter cyclic block r>=2 times, then at every
visited vertex its list of outgoing successor vertices would repeat
at least r times. This contradicts the m distinct successors at v.
This also holds for every reordered word, whose outgoing neighbor
set at v is unchanged. Hence every partner rotation class has exactly
n distinct rooted words.

It follows that, for fixed x, precisely
$$
n\big((m-1)!-1\big)g_m(x)
\tag{33}
$$
distinct rooted partners arise. No pair has been counted more than
once. If one allows different values m and m', the same conclusion
persists: coinciding partners would have to have the same changed
trigram center, hence the same hub v, but K_v(x) cannot equal two
different integers. Thus all the classes $\mathscr E^{(m)}_n$ are
pairwise disjoint.

## 6. Excluding reversed partners and proving the asymptotic

Let the directed edge count be
$$
E_x(u,z)=\#\{j:(x_j,x_{j+1})=(u,z)\}.
\tag{34}
$$
Reversal transposes this array, and rotation leaves it unchanged.
At a good hub, the directed edge v->b_1 occurs in x. The edge b_1->v
does not occur: every predecessor of v is one of the a_i, and none
equals b_1. Consequently $E_x\ne E_x^{\mathsf T}$.
Every reordered word y has E_y=E_x by construction, whereas every
rotation of the reversed word has edge count $E_x^{\mathsf T}$.
Thus no such y belongs to the reversed rotation class of x.

The good-hub relation is symmetric in x and y. At the changed hub,
the excursion lengths are permuted and its incoming and outgoing
neighbor sets are unchanged; it is still a good m-hub for y. Reorder
its excursions back to obtain the rotation class of x, which is
different from that of y. Therefore exchanging the two members of
any pair preserves $\mathscr E^{(m)}_n$. This also verifies directly
that its complement is closed under exchange.

Using the amplitude equality (30), the exact count (33), and the
nonnegative weights w proves (5). Equation (29) then gives, uniformly
for n<=BN,

$$
\begin{split}
\mathcal E^{(m)}_{n,N}
={}&N^2\frac{(m-1)!-1}{m!}e^{-t}t^{m+1}\\
&+O_{m,B,C}(N)
 +O_m\!\left(nN^2(3/4)^n\right).
\end{split}
\tag{35}
$$

For cN<=n<=BN the last term is o(N), proving (6). No averaging over n,
N, phases or the kick parameter is present.

For a continuous weight supported on [c,B], a usual Riemann sum also
gives the precisely normalized consequence

$$
\frac1{N^3}\sum_n w_0(n/N)\mathcal E^{(m)}_{n,N}
\longrightarrow
\int_c^B w_0(t)\frac{(m-1)!-1}{m!}e^{-t}t^{m+1}\,dt.
\tag{36}
$$

The error sum in (35), divided by N^3, is O(1/N).
In particular the N^{-2} normalization used for the full pair trace
sum gives a contribution of order N from this positive class whenever
the displayed integral is positive.

## 7. A forced negative complement at the Heisenberg scale

By the pairwise disjointness just proved,

$$
|\operatorname{Tr}U_N^n|^2
=\mathcal E^{(3)}_{n,N}+\mathcal E^{(4)}_{n,N}
 +\mathcal W_{n,N}
\tag{37}
$$

exactly, where $\mathcal W$ is defined by (7).
All three terms are real: the two encounter sums are nonnegative;
the complement is invariant under swapping x and y.

Unitarity gives $|\operatorname{Tr}U_N^n|\le N$ for every n. Put

$$
F(t)=e^{-t}\left(\frac{t^4}{6}+\frac{5t^5}{24}\right).
\tag{38}
$$

Equations (6) and (37) therefore imply, uniformly on every fixed
compact interval 0<c<=t=n/N<=B,

$$
\mathcal W_{n,N}\le N^2(1-F(t))+O_{B,C}(N).
\tag{39}
$$

At t=2 one has $F(2)=28e^{-2}/3>1$. For an elementary check of
strictness, $e=\sum_{j\ge0}1/j!<3$, because for j>=2 the terms
are bounded by $2^{-(j-1)}$, with a strict inequality already at j=3.
Hence $F(2)>28/27>1$. This proves (8). Continuity of F also gives
a fixed open interval containing t=2 on which
$\mathcal W_{n,N}\le-\epsilon N^2$ for some fixed epsilon>0
and all sufficiently large odd N.

In the notation of root_physical_cycle_classes.md, let D_n be the
forward rotation class, R_n the reversed class with forward overlap
removed, and Z_n their complement. Section 6 proves
$\mathscr E^{(3)}_n\cup\mathscr E^{(4)}_n\subset Z_n$.
Thus $\mathcal W=D_n+R_n+
(Z_n-\mathcal E^{(3)}-\mathcal E^{(4)})$.
Since D_n>=0 and the already proved all-time reversed-class bound
gives $|R_n|=o(1)$ uniformly in n for this family, (39) implies the
same negative upper bound, up to o(1), for the remaining part of Z_n.
The target weighted CUE cancellation is still much more precise
than either (8) or (39).

## 8. Exact scope and the first open estimate

This argument has produced original-family phase-coherent classes with
explicit Heisenberg-time asymptotics, and it has forced a signed negative
contribution of order N^2 from their complement. It has not replaced that
complement by a random model. It does not provide an upper bound on its
absolute value or its higher moments, and does not determine its signed
sum.

For example, after subtracting all the previously controlled forward
and reversed classes, the required pair test still asks for the signed
quantity

$$
\frac1{N^2}\sum_{n\ge1}w_0(n/N)
 \left[
  Z_n-\mathcal E^{(3)}_{n,N}-\mathcal E^{(4)}_{n,N}
 \right]
\tag{40}
$$

with enough precision to cancel the explicit contributions in (36)
and then leave the order-one CUE correction. None of the inequalities
above estimates (40) to that accuracy. Its terms must not be replaced
by their absolute values, nor may the explicit positive classes be
mistaken for the full off-diagonal answer. This is the first unresolved
coherent sum in this route.

