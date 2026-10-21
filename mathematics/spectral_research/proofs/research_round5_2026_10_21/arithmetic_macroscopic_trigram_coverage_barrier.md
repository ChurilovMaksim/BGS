> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/arithmetic_macroscopic_trigram_coverage_barrier.md`. Embedded SHA256: `828b12a6b933e2f541b2296d240555d8caceac407442f27397f050f2bf0928c7`.
> [Thematic guide](../../topics/histories.md).

# Original-family coherent mass beyond every sublinear set of trigram centers

Date: 2026-10-21.  
Status: full proof of an original-family coverage obstruction.  
This note does not prove or disprove $H_{\rm diag}$. It rules out exhausting the positive equal-oriented-edge class by arbitrary directed rearrangements of increasingly long arcs, even when the number of arcs grows.

## 1. Statement, definitions, and original-family inputs

Let $U=U_N$ be unitary, set
$$
 P_{uv}=|U_{uv}|^2,\qquad J_N=N^{-1}{\bf1}{\bf1}^*,
$$
and assume, for a fixed $C\ge1$,
$$
 \max_{u,v}P_{uv}\le C/N,\qquad
 \|P-J_N\|_{\rm op}\le1/2.                                    \tag{1.1}
$$
The exact original matrices satisfy (1.1), with $C=9$, for every sufficiently large odd $N$. The two analytic inputs, including their modular-half conventions and uniform error proofs, are:

- $\lvert U_N(x,y)\rvert\le3/\sqrt N$:  
  dual_physical_four_branch_kernel.md, §§1 and 6, SHA256  
  0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c.
- $\|P-J_N\|_{\rm op}\le1/2$:  
  root_oscillatory_matrix_cancellation.md, §4.1, SHA256  
  ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d.

Both proofs concern the exact fixed $\tau=10^{-80}$, all sufficiently large odd $N$, and the original $U_N$. The new combinatorial argument below is proved from (1.1); it does not assume independent path coordinates or random matrix entries.

Fix $0<c\le B<\infty$, and let
$$
 cN\le n\le BN,\qquad s=n/N.
$$
A rooted cyclic word is $x=(x_0,\ldots,x_{n-1})$, with indices modulo $n$. Put
$$
 a(x)=\prod_{i=0}^{n-1}U_{x_i,x_{i+1}},\qquad w(x)=|a(x)|^2,
$$
$$
 L_{uv}(x)=\#\{i:(x_i,x_{i+1})=(u,v)\},\qquad
 d_v(x)=\sum_uL_{vu}(x)=\#\{i:x_i=v\},
$$
and define its centered trigram counts
$$
 T_v^x(u,z)=\#\{i:(x_{i-1},x_i,x_{i+1})=(u,v,z)\}.             \tag{1.2}
$$
For two words with equal oriented edge counts, let
$$
 \mathfrak d(x,y)
 =\#\{v:T_v^x\ne T_v^y\}.                                    \tag{1.3}
$$
This compares entire arrays at each vertex label; it does not count changed positions.

Let $q_N$ be any positive integer sequence with $q_N/N\to0$. Define
$$
 \mathcal F^{>q_N}_{n,N}
 =\sum_{\substack{x,y:\\L(x)=L(y),\ \mathfrak d(x,y)>q_N}}
      a(x)\overline{a(y)}.                                  \tag{1.4}
$$
All pairs here are actual ordered pairs of rooted vertex words, with no marked multiplicity. Equality of edge counts gives $a(y)=a(x)$, so every summand is $w(x)\ge0$.

Put the explicit positive constant
$$
 \alpha=\frac{e^{-B}c^3}{6}.
 \tag{1.5}
$$
Then, uniformly in the stated interval of integer times, for every sufficiently large $N$,
$$
 \boxed{\quad
 \mathcal F^{>q_N}_{n,N}
 \ge \frac{\alpha}{16}\,2^{\alpha N/2}.
 \quad}                                                     \tag{1.6}
$$
The threshold may depend on $c,B,C$ and the sequence $q_N$. The constant and exponential rate in (1.6) do not.

A subset yielding this lower bound has $x,y$ outside both forward and reversed rotation classes. Thus an exponential positive contribution beyond all sublinear sets of changed trigram centers remains inside the previously unestimated class $Z_{n,N}$.

### Consequence for all directed long-arc rearrangements

Let $L_N\to\infty$ be arbitrary. Allow an arbitrary number of cuts, provided every resulting directed arc has at least $L_N$ vertices. Reorder the arcs into one cyclic word, retaining each arc's directed vertex sequence. Such a pair satisfies
$$
 \mathfrak d(x,y)\le 2n/L_N\le2BN/L_N=o(N).                  \tag{1.7}
$$
Therefore (1.6) exhibits exponentially large positive equal-edge-count mass outside the union of **all** these long-arc rearrangements. This applies to growing encounter orders, not only to any fixed number of reconnections.

No assertion about the sign or size of the complete signed residual follows from this positive subclass alone. In particular, the result does not supply a counterexample to $H_{\rm diag}$.

## 2. Three weighted estimates on a closed path

We prove the estimates used to select a positive-mass set of words.

Unitarity makes $P$ doubly stochastic. Set $A=P-J_N$. Then
$$
 AJ_N=J_NA=0,\qquad P^k=J_N+A^k,\qquad \|A\|\le1/2.
$$
Each row and column of $A$ has squared Euclidean norm at most $(C-1)/N$. For a row this follows from
$$
 \sum_v(P_{uv}-1/N)^2=\sum_vP_{uv}^2-1/N\le(C-1)/N;
$$
the column proof is identical. Thus
$$
 |A_{vv}|\le C/N,\qquad
 |(A^k)_{vv}|\le\frac{C-1}{N}2^{-(k-2)}\quad(k\ge2).
 \tag{2.1}
$$
Also $\|A\|_{\rm HS}^2\le C-1$, so
$$
 T_n:=\sum_xw(x)=\operatorname{Tr}P^n
 =1+O_C(2^{-(n-2)}).
 \tag{2.2}
$$
The trace bound uses
$\lvert\operatorname{Tr}A^n\rvert
 \le\|A\|_{\rm HS}^2\|A\|^{n-2}$, valid without normality.

### 2.1 Visit generating function

For a vertex $v$, put $E_v=e_ve_v^*$, $D_z=I+(z-1)E_v$. Direct multiplication gives
$$
 G_{v,n}(z):=\operatorname{Tr}(D_zP)^n
 =\sum_xw(x)z^{d_v(x)}.
 \tag{2.3}
$$
For $|\lambda|>1/2$, set
$$
 R_v(\lambda)=\sum_{k\ge1}\lambda^{-k}(A^k)_{vv}.
$$
By (2.1), uniformly in $v$ and $|\lambda|\ge3/4$,
$$
 R_v(\lambda)=O_C(N^{-1}),\qquad
 R_v'(\lambda)=O_C(N^{-1}).                                 \tag{2.4}
$$
These bounds follow by summing convergent geometric series and their derivatives.

For $\eta=z-1$, the rank-one determinant identity and the reducing constant line of $P$ give the exact formula
$$
 \det(\lambda I-D_zP)
 =\det_{{\bf1}^{\perp}}(\lambda I-A)
       \left[(\lambda-1)(1-\eta R_v(\lambda))-\frac{\eta}{N}\right].
 \tag{2.5}
$$
Indeed, off the spectra, the rank-one multiplier is
$1-\eta e_v^*P(\lambda I-P)^{-1}e_v$, where
$$
 e_v^*P(\lambda I-P)^{-1}e_v
 =\frac1{N(\lambda-1)}+R_v(\lambda).
$$
After multiplication the apparent pole at one cancels; continuity proves (2.5) there too.

Uniformly for $|z|\le2$, one has $|\eta|\le3$. For large $N$, (2.4) implies $|\eta R_v|\le1/4$ outside $3/4$. Every eigenvalue of $D_zP$ in that region must solve
$$
 \lambda
 =1+\frac{\eta}{N(1-\eta R_v(\lambda))},\qquad
 |\lambda-1|\le4/N.                                        \tag{2.6}
$$
The right side maps the closed disk $|\lambda-1|\le6/N$ inside itself and has derivative $O_C(N^{-2})$ there. The elementary contraction argument therefore gives exactly one fixed point. It is a simple zero of the bracket in (2.5), because the derivative of $\lambda$ minus the right side is $1+O_C(N^{-2})$. The perpendicular determinant has no zero outside $1/2$. Hence this is the only eigenvalue outside $3/4$, and it is simple.

Equations (2.4)–(2.6) imply
$$
 \lambda_v(z)=1+\eta/N+O_C(N^{-2}).
$$
The logarithm near one gives, for $n\le BN$,
$$
 \lambda_v(z)^n=e^{s(z-1)}+O_{B,C}(N^{-1}).
$$
The other eigenvalues contribute at most $N(3/4)^n$ to the trace. Thus
$$
 G_{v,n}(z)
 =e^{s(z-1)}+O_{B,C}(N^{-1})+O(N(3/4)^n)
 \quad(|z|\le2),
 \tag{2.7}
$$
uniformly in $v$. Taking $z=2$, and summing over $v$, yields, for all sufficiently large $N$ in the stated time interval,
$$
 \sum_xw(x)\sum_v2^{d_v(x)}
 =Ne^s+O_{B,C}(1)+O(N^2(3/4)^n)
 \le2e^B N.
 \tag{2.8}
$$
Extracting the coefficient of $z^3$ on $|z|=2$ instead gives
$$
 \sum_xw(x)\#\{v:d_v(x)=3\}
 =N e^{-s}s^3/6+O_{c,B,C}(1).
 \tag{2.9}
$$
The coefficient extraction is legitimate for the exact polynomial (2.3); Cauchy's integral formula bounds the error by the uniform bound in (2.7).

### 2.2 Good vertices

Call $v$ good if $d_v=3$ and the three predecessor labels and three successor labels at its visits are six pairwise distinct labels. Let $g(x)$ count good vertices.

This property depends only on $L(x)$: it says that $v$ has three distinct incoming neighbors and three distinct outgoing neighbors, with the two sets disjoint and every corresponding edge multiplicity one. A loop would put $v$ in both sets. A cyclic gap two between visits to $v$ would put its intermediate vertex in both sets. Therefore the three cyclic gaps at a good vertex are automatically at least three.

We claim
$$
 \sum_xw(x)g(x)=N e^{-s}s^3/6+O_{c,B,C}(1).
 \tag{2.10}
$$
Here is the full loss estimate from (2.9). Every entry of $P^k$, $k\ge1$, is at most $C/N$, since $P^k=P^{k-1}P$ and $P^{k-1}$ is row stochastic.

The weighted number of vertices with a pair of visits at cyclic separation one or two is at most
$$
 n\sum_{\ell=1}^2\sum_v(P^\ell)_{vv}(P^{n-\ell})_{vv}
 \le2C^2 n/N\le2C^2B.
 \tag{2.11}
$$
This upper bound is allowed to count additional visits or multiple short gaps.

For three marked visits to $v$ whose cyclic gaps $\ell_i$ are at least three, denote the outgoing neighbors by $b_i$ and incoming neighbors by $a_i$. Summing all interior labels leaves a product of three factors
$$
 P_{v b_i}(P^{\ell_i-2})_{b_i a_{i+1}}P_{a_{i+1}v}.
$$
Bound the three middle factors by $C/N$. The other six coordinates now have a product of three row probability distributions and three column probability distributions. Every atom in each distribution is at most $C/N$. Any fixed equality between two coordinates has probability at most $C/N$; a union bound over fifteen pairs costs at most $15C/N$. Thus, for fixed $v$ and fixed visit positions, the bad weight is at most $15C^4/N^4$. There are at most $Nn^3/6$ choices of $v$ and the unordered triple of visit positions. The total loss is at most
$$
 \frac52 C^4B^3.
 \tag{2.12}
$$
Allowing extra visits only enlarged the bound. Equations (2.9), (2.11), and (2.12) prove (2.10).

### 2.3 Repeated oriented edges

Define
$$
 \mathcal J(x)=\sum_{u,v}\binom{L_{uv}(x)}2.
 \tag{2.13}
$$
This counts pairs of positions occupied by the same oriented edge, including loops. We have the uniform bound
$$
 \sum_xw(x)\mathcal J(x)\le C^3 B^2/2.                        \tag{2.14}
$$

To verify it, let $S_r$ be the weight of words whose oriented edges at positions zero and $r$ agree. If $2\le r\le n-2$,
$$
 S_r=\sum_{u,v}P_{uv}^2
       (P^{r-1})_{vu}(P^{n-r-1})_{vu}
 \le\frac{C^2}{N^2}\sum_{u,v}P_{uv}^2
 \le\frac{C^3}{N^2}.
 \tag{2.15}
$$
For $r=1$, equality forces $x_0=x_1=x_2=u$, so
$$
 S_1=\sum_uP_{uu}^2(P^{n-2})_{uu}\le C^3/N^2.
$$
The case $r=n-1$ is identical by cyclic symmetry. For large $N$ we have $n\ge3$. Rotation invariance and the factor one half for unordered position pairs now give
$$
 \sum_xw(x)\mathcal J(x)
 =\frac n2\sum_{r=1}^{n-1}S_r
 \le\frac{C^3n(n-1)}{2N^2}\le C^3B^2/2,
$$
proving (2.14).

## 3. A fixed positive mass of suitable words

Choose the constant
$$
 K=\max\{e^2,32e^B/\alpha\},
$$
where $\alpha$ is (1.5), and define the set of rooted words
$$
 \mathcal A_{n,N}
 =\left\{x:
  g(x)\ge\alpha N/2,\quad
  \sum_v2^{d_v(x)}\le KN,\quad
  \mathcal J(x)\le\log N
 \right\}.
 \tag{3.1}
$$
All logarithms in this note are natural unless a base is written.

The exact estimates of §2 imply, uniformly in $cN\le n\le BN$,
$$
 \boxed{\quad \sum_{x\in\mathcal A_{n,N}}w(x)\ge\alpha/4
   \quad}                                                    \tag{3.2}
$$
for all sufficiently large $N$.

Indeed, $e^{-s}s^3/6\ge\alpha$, so (2.10) and (2.2) give
$$
 \sum_xw(x)g(x)\ge\alpha N-O(1),\qquad
 \sum_xw(x)=1+o(1).
$$
Since $g(x)\le N$,
$$
 \sum_{\{g\ge\alpha N/2\}}w(x)
 \ge\frac1N\sum_xw(x)g(x)
      -\frac{\alpha}{2}\sum_xw(x)
 \ge\alpha/2-o(1)\ge3\alpha/8.                               \tag{3.3}
$$
By (2.8), the mass with $\sum_v2^{d_v}>KN$ is at most
$2e^B/K\le\alpha/16$. By (2.14), the mass with
$\mathcal J>\log N$ is at most $C^3B^2/(2\log N)\le\alpha/16$ for large $N$. Subtracting the two bad masses from (3.3) proves (3.2).

Every condition in (3.1) depends only on the oriented edge counts. In particular, all coherent partners of an $x\in\mathcal A_{n,N}$ satisfy the same conditions.

## 4. Exact local-pairing count with repeated edges

Fix a word $x$, and write $m_{uv}=L_{uv}(x)$, $d_v=d_v(x)$, and $\mathcal J=\mathcal J(x)$. Distinguish every occurrence of every oriented edge by a separate label. At each vertex $v$, an Euler tour pairs its $d_v$ incoming edge occurrences with its $d_v$ outgoing edge occurrences: the paired outgoing edge is the successor of the incoming edge in the tour.

Any such collection of local bijections defines a permutation of the $n$ labelled edge occurrences. A single Euler tour occurs only when this permutation is one cycle. For an upper bound we may retain all bijections, including those producing multiple cycles.

For a specified centered trigram array $t_{uz}$ at $v$, with row sums $m_{uv}$ and column sums $m_{vz}$, the number of local bijections realizing it is exactly
$$
 \frac{\displaystyle\prod_u m_{uv}!\prod_zm_{vz}!}
      {\displaystyle\prod_{u,z}t_{uz}!}.
 \tag{4.1}
$$
To prove the formula, for each incoming-neighbor group $u$, divide its labelled incoming occurrences into outgoing-neighbor groups of sizes $t_{uz}$. This contributes $m_{uv}!/\prod_z t_{uz}!$. For each $z$, biject the $m_{vz}$ assigned incoming occurrences with the labelled outgoing edges to $z$, contributing $m_{vz}!$. Multiplying gives (4.1). This argument includes loops and parallel edges.

Let $S$ be a specified set of vertex labels outside which $T_v^y=T_v^x$ is required. At $v\notin S$, use (4.1) and discard its denominator. At $v\in S$, use the unrestricted bound $d_v!$. A rooted Euler tour also requires a choice of its initial labelled edge, giving at most $n$ choices. Therefore the number of actual rooted vertex words $y$ satisfying these conditions and $L(y)=L(x)$ is at most
$$
 n\left(\prod_{u,v}m_{uv}!^2\right)\prod_{v\in S}d_v!.
 \tag{4.2}
$$
There is no unverified division by edge labels or period multiplicity in this bound. Every actual rooted word can be labelled, for example by assigning the original labels of each oriented edge in its successive visit order from position zero. This gives a local-pairing system and a starting labelled edge. Those data uniquely reconstruct its rooted vertex word. Thus the number of labelled systems is an upper bound for the number of actual words. Some systems may be inadmissible or give the same vertex word, which can only enlarge this upper bound.

For every integer $m\ge0$, one has $m!\le2^{\binom m2}$, since $j\le2^{j-1}$. Hence
$$
 \prod_{u,v}m_{uv}!^2\le4^{\mathcal J}.                      \tag{4.3}
$$

Suppose now that $x\in\mathcal A_{n,N}$ and $|S|=r\ge1$. Let $y_v=2^{d_v}\ge1$. The function
$$
 t\longmapsto[\log(et)]^2
$$
is concave for $t\ge1$, because its second derivative is $-2\log t/t^2$. Since $\log(d!)\le d^2$ for integers $d\ge0$, Jensen's inequality gives
$$
 \begin{split}
 \sum_{v\in S}\log(d_v!)
 &\le\sum_{v\in S}d_v^2\\
 &\le\frac1{(\log2)^2}\sum_{v\in S}[\log(ey_v)]^2\\
 &\le\frac r{(\log2)^2}
       \left[\log\left(\frac{eKN}{r}\right)\right]^2 .
 \end{split}                                                 \tag{4.4}
$$
This is the point where a single bound on the largest visit count would be insufficient. The exponential-moment budget controls every sublinear set of vertices simultaneously.

Let $\mathcal N_x(q)$ count all coherent partners $y$ with
$\mathfrak d(x,y)\le q$, for $1\le q\le N/2$.
There are at most $(q+1)\binom Nq\le(q+1)(eN/q)^q$ possible supporting sets $S$ of cardinality at most $q$.
The right side of (4.4) increases with $r\le N$, since $K\ge e^2$.
Combining (4.2)–(4.4) therefore proves the explicit bound
$$
 \boxed{\quad
 \mathcal N_x(q)
 \le n\,4^{\mathcal J(x)}(q+1)
        \left(\frac{eN}{q}\right)^q
        \exp\left\{
          \frac q{(\log2)^2}
          \left[\log\left(\frac{eKN}{q}\right)\right]^2
        \right\}.
 \quad}                                                       \tag{4.5}
$$
The case $S=\varnothing$ is covered by the same bound.

For $x\in\mathcal A_{n,N}$, $\mathcal J(x)\le\log N$, and $n\le BN$. If $q=q_N=o(N)$, the logarithm of the right side in (4.5) is
$$
 O_B(\log N)+\log(q_N+1)
 +q_N\log(eN/q_N)
 +\frac{q_N}{(\log2)^2}\log^2(eKN/q_N)=o(N).
 \tag{4.6}
$$
The last conclusion follows from $t\log^2(1/t)\to0$ as $t\downarrow0$, with $t=q_N/N$. The bound is uniform in every $x\in\mathcal A_{n,N}$ and all the allowed times.

## 5. Exponentially many distinct coherent partners

We include the Euler-tour construction to specify the exact lower count.

Fix $x\in\mathcal A_{n,N}$ and let $r=x_0$ be its root. Label its edge occurrences as above. At every visited vertex $v\ne r$, select the edge of its last departure during the rooted tour. The selected edges form a directed tree toward $r$: if a selected edge at $v$ ends at $u\ne r$, then the last departure time at $u$ is strictly later. Hence no selected cycle exists, and every selected forward chain ends at $r$.

At every $v\ne r$, keep its selected edge last in a list of its outgoing edge occurrences. Order the earlier entries arbitrarily. Fix the root's outgoing list. Starting at $r$, follow the next unused outgoing edge in the list of the current vertex.

The resulting walk traverses all edges in one closed tour. It cannot get stuck at a nonroot vertex: for a trail ending there, used incoming degree exceeds used outgoing degree by one, and equality of total degrees rules out exhaustion of all outgoing edges. If it stops at $r$, the used trail is closed. If unused edges remained at a nonroot vertex, its selected last edge would still be unused. Along the selected tree, an unused incoming edge forces unused outgoing degree at the next vertex. This would eventually force unused outgoing degree at $r$, contradicting the stopping condition. Unused edges at $r$ itself directly contradict stopping. Thus none remain.

At each good nonroot vertex there are three outgoing edges with distinct successor labels. Keep the selected edge last and choose either order for the other two. Make these binary choices independently; keep all lists at other vertices fixed. Each choice produces an Euler tour with exactly the original oriented edge counts.

Different binary choices produce different actual rooted vertex words. The rooted word records the ordered list of successors encountered at each good nonroot vertex, and those successors are distinct. It therefore records each binary choice. Parallel edge occurrences elsewhere cannot erase this distinction.

Consequently the number of actual coherent partners so constructed is at least
$$
 2^{\,g(x)-{\bf1}_{\{r\ {\rm good}\}}}
 \ge2^{g(x)-1}
 \ge2^{\alpha N/2-1}.                                        \tag{5.1}
$$
This is a count of rooted vertex words, not of artificial edge labels.

By (4.6), for all sufficiently large $N$, uniformly in the selected $x$ and times,
$$
 \mathcal N_x(q_N)\le2^{\alpha N/2-2}.
$$
Removing all partners with at most $q_N$ changed trigram centers from (5.1) therefore leaves at least
$$
 2^{\alpha N/2-2}                                             \tag{5.2}
$$
actual coherent partners for each $x\in\mathcal A_{n,N}$.

Each such pair contributes exactly $w(x)$. Summing (5.2) over $x\in\mathcal A_{n,N}$, using (3.2), proves
$$
 \mathcal F^{>q_N}_{n,N}
 \ge\frac{\alpha}{4}\,2^{\alpha N/2-2}
 =\frac{\alpha}{16}\,2^{\alpha N/2},
$$
which is (1.6). No summand in this lower bound has a phase estimated by its absolute value: its complex phase cancels exactly because the entire oriented edge array agrees.

Rotations of $x$ have the same centered trigram arrays, so cannot satisfy $\mathfrak d>q_N$. Nor can these constructed pairs belong to the reversed rotation class. At any good vertex $v$, choose an outgoing neighbor $b$. The edge $v\to b$ occurs, while $b\to v$ does not, because incoming and outgoing neighbor sets at $v$ are disjoint. Thus $L(x)\ne L(x)^{\mathsf T}$. Every reversed rotation has edge array $L(x)^{\mathsf T}$, while each coherent partner has array $L(x)$. A good vertex exists for all selected $x$ once $N$ is large.

## 6. Why all increasingly long directed arcs still miss this mass

Partition a rooted cyclic word into $r$ directed arcs and obtain a partner by reordering these arcs without changing any internal directed vertex sequence. The only changed edges are the connectors from an arc's last vertex to the next arc's first vertex.

All internal trigrams whose center is neither the first nor the last vertex of an arc are unchanged. At most the $2r$ endpoint vertex labels can therefore have different arrays $T_v$. This proves
$$
 \mathfrak d(x,y)\le2r.
 \tag{6.1}
$$
The statement is invariant under the choice of root and under cyclic naming of the arcs. Repeated endpoint labels only decrease the number of possible centers.

If every arc contains at least $L_N$ vertices, then $r\le n/L_N$. Take
$$
 q_N=\max\{1,\lceil2BN/L_N\rceil\}.
$$
For any $L_N\to\infty$ this satisfies $q_N=o(N)$, so (1.6) applies. Every pair obtained by any such long-arc rearrangement lies in the class $\mathfrak d\le q_N$. Hence none of the positive subclass in (5.2) is covered, even after taking the union over all numbers of arcs, all cut positions, all arc orders, and all roots.

This is a coverage obstruction to a method with diverging minimum directed-arc length. It is not an assertion that the sum over that union is small; the union can contain large positive and negative pieces of its own. It also makes no claim about operations that reverse the direction of long arcs, or operations that change the arcs' interiors.

## 7. Scope of the remaining problem

The proved exponential contribution is inside the exact original-family off-diagonal physical-cycle class $Z_{n,N}$, at all times $cN\le n\le BN$. It remains after removing every equal-edge coherent partner obtainable by the directed long-arc operations of §6.

Unitarity still permits other coherent classes to compensate this positive contribution. The theorem therefore does not bound the full $|\operatorname{Tr}U_N^n|^2$ from below, does not refute the CUE pair prediction, and does not imply failure of $H_{\rm diag}$.

Its substantive conclusion is that a completion of the current long-arc resummation cannot be based on enlarging the number of well-separated directed cuts while retaining a minimum arc length tending to infinity. Exponentially much exact coherent mass requires changes at more than every sublinear number of trigram centers. A successful cancellation argument must also control these configurations, including their signed interaction with unequal oriented edge arrays, at the final polynomial accuracy required by the original spectral statistic.

