> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/root_exponential_coherent_edge_classes.md`. Embedded SHA256: `001fd27ca128f1a00417838e0f4b07d7ad19f291e8c2c5fbb593e614d2ec29e0`.
> [Thematic guide](../../topics/histories.md).

# Exponentially large coherent edge classes and their forced cancellation

21 October 2026. Author: `/root`. Original family and fixed $\tau$
unchanged. This note contains a complete argument for a new structural
result; it does not prove or refute $H_{\rm diag}$.

The one-hub encounter investigation suggested counting simultaneous local
reorderings. The useful combinatorial structure is a directed tree of last
exits. Its elementary Euler-tour proof is included, so no graph-enumeration
theorem is assumed.

## 1. Statement

Let $U_N$ be unitary, and set $P_{xy}=|U_N(x,y)|^2$,
$J_{xy}=1/N$. Suppose a fixed $C\ge1$ satisfies, for all sufficiently
large $N$,

$$
 \max_{x,y}P_{xy}\le C/N,\qquad \|P-J\|_{\rm op}\le1/2.                 \tag{1.1}
$$

The preceding four-branch and oscillatory-kernel proofs establish (1.1)
for the specified matrices in the problem, with $C=9$, along **all odd
dimensions**. No parameter or dimension average is made here.

For a rooted cyclic word $x=(x_0,\ldots,x_{n-1})$, put

$$
 a(x)=\prod_{j=0}^{n-1}U_{x_j,x_{j+1}},\qquad
 L_{uv}(x)=\#\{j:(x_j,x_{j+1})=(u,v)\},                         \tag{1.2}
$$

with cyclic indexing. Thus $L(x)$ records every **oriented** edge
multiplicity. Define disjoint exact sums

$$
 \mathcal F_{n,N}=\sum_{x,y:\,L(x)=L(y)}a(x)\overline{a(y)},\qquad
 \mathcal G_{n,N}=\sum_{x,y:\,L(x)\ne L(y)}a(x)\overline{a(y)}.    \tag{1.3}
$$

Equality of all the edge counts implies equality of the scalar products
$a(x)=a(y)$ exactly. In particular $\mathcal F_{n,N}\ge0$, both
sums are real, and

$$
 |\operatorname{Tr}U_N^n|^2=\mathcal F_{n,N}+\mathcal G_{n,N}.      \tag{1.4}
$$

Fix $0<c\le B<\infty$, let $cN\le n\le BN$ be an integer, and put
$s=n/N$. Then, uniformly in this range,

$$
 \boxed{\quad
 \mathcal F_{n,N}\ge
 \exp\left\{\frac{\log2}{6}e^{-s}s^3N-O_{c,B,C}(1)\right\}.
 \quad}                                                       \tag{1.5}
$$

Consequently

$$
 \boxed{\quad
 \mathcal G_{n,N}\le N^2-
 \exp\left\{\frac{\log2}{6}e^{-s}s^3N-O_{c,B,C}(1)\right\}.
 \quad}                                                       \tag{1.6}
$$

In particular $\mathcal G_{n,N}$ is negative with exponentially large
absolute value for sufficiently large $N$ in every such scaled-time
interval. Its cancellation with $\mathcal F_{n,N}$ leaves a nonnegative
quantity at most $N^2$, by unitarity.

One can remove the forward and reversed rotation classes from
$\mathcal F_{n,N}$ without changing its exponential lower bound.
Let $\mathcal C_{n,N}$ be the restriction of $\mathcal F_{n,N}$
to $y\notin\operatorname{Rot}(x)\cup\operatorname{Rot}(Rx)$.
Then

$$
 \mathcal C_{n,N}\ge\mathcal F_{n,N}
               -2n\operatorname{Tr}P^n.                       \tag{1.7}
$$

Thus the remaining class $Z_{n,N}$ from the exact cycle decomposition
contains an exponentially large positive subclass. These statements do
**not** evaluate the polynomial-scale remainder in (1.4), which is the
issue in the spectral-statistics problem.

## 2. A uniform visit-count generating function

The argument first needs the mean number of vertices visited exactly
three times. We prove the required estimate rather than infer it from
mixing language.

Write $A=P-J$. Since $P$ is doubly stochastic, $PJ=JP=J$,
$P^k=J+A^k$, and the constant vector and its orthogonal complement
reduce $A$. Every row and every column of $A$ has squared
Euclidean norm at most $(C-1)/N$:

$$
 \sum_y(P_{vy}-1/N)^2=\sum_yP_{vy}^2-1/N\le(C-1)/N.             \tag{2.1}
$$

Therefore, for every $v$,

$$
 |A_{vv}|\le C/N,\qquad
 |(A^k)_{vv}|\le\frac{C-1}{N}2^{-(k-2)}\quad(k\ge2).           \tag{2.2}
$$

The second estimate sandwiches $A^{k-2}$ between row $v$ and
column $v$ of $A$. It does not require $A$ to be normal.
Also $\|A\|_{\rm HS}^2\le C-1$, so, for $n\ge2$,

$$
 T_n:=\operatorname{Tr}P^n=1+O_C(2^{-(n-2)}).                  \tag{2.3}
$$

For a vertex $v$, let $E_v=e_ve_v^*$,
$D_z=I+(z-1)E_v$, and

$$
 G_{v,n}(z)=\operatorname{Tr}(D_zP)^n
 =\sum_x |a(x)|^2 z^{\#\{j:x_j=v\}}.                          \tag{2.4}
$$

This is an exact polynomial identity, including for complex $z$.
We show, uniformly in $v$, $|z|\le2$, and $cN\le n\le BN$,

$$
 G_{v,n}(z)=e^{s(z-1)}+O_{c,B,C}(N^{-1}).                      \tag{2.5}
$$

For $|\lambda|>1/2$, put

$$
 R_v(\lambda)=\sum_{k\ge1}\lambda^{-k}(A^k)_{vv}.              \tag{2.6}
$$

Using (2.2), for $|\lambda|\ge3/4$ one obtains directly

$$
 |R_v(\lambda)|\le\frac{20C}{3N},\qquad
 |R_v'(\lambda)|\le\frac{31C}{N}.                            \tag{2.7}
$$

For the first bound the $k=1$ term contributes at most
$4C/(3N)$, and the remaining geometric sum at most
$16(C-1)/(3N)$. For the derivative these contributions are
$16C/(9N)$ and $256(C-1)/(9N)$, respectively.

Let $\eta=z-1$. The rank-one determinant identity gives

$$
 \det(\lambda I-D_zP)
 =\det_{\boldsymbol1^\perp}(\lambda I-A)
 \left[(\lambda-1)(1-\eta R_v(\lambda))-\frac\eta N\right].     \tag{2.8}
$$

To verify it, first take $\lambda\ne1$ outside the spectra.
The determinant multiplier for
$D_zP=P+\eta e_ve_v^*P$ is
$1-\eta e_v^*P(\lambda I-P)^{-1}e_v$. The resolvent decomposition
of $P=J+A$ makes this diagonal expression
$1-\eta/[N(\lambda-1)]-\eta R_v(\lambda)$. Multiplication by
$\det(\lambda I-P)=(\lambda-1)
\det_{\boldsymbol1^\perp}(\lambda I-A)$ gives (2.8).
Continuity removes the apparent exclusion at $\lambda=1$.

Here $|\eta|\le3$. For $N\ge80C$,
$|\eta R_v|\le1/4$ on $|\lambda|\ge3/4$. Every root of (2.8)
in that region must consequently satisfy

$$
 \lambda=1+\frac{\eta}{N(1-\eta R_v(\lambda))},\qquad
 |\lambda-1|\le4/N.                                         \tag{2.9}
$$

The right side maps the closed disk $|\lambda-1|\le6/N$
strictly inside itself. By (2.7), its derivative there is at most
$496C/N^2<1/2$ for all sufficiently large $N$. Iteration is
a contraction of this complete disk and has one fixed point. Every
root outside $3/4$ is this fixed point, and differentiating the
bracket in (2.8) shows it is simple. The factor on
$\boldsymbol1^\perp$ is nonzero there because $\|A\|\le1/2$.
Thus the other $N-1$ eigenvalues of $D_zP$, counted with their
algebraic multiplicities, have modulus at most $3/4$.

Moreover, (2.7)--(2.9) give

$$
 \lambda(z)=1+\eta/N+O_C(N^{-2}),\qquad
 \log\lambda(z)=\eta/N+O_C(N^{-2})                            \tag{2.10}
$$

uniformly for $|z|\le2$, using the logarithm near one. For example
the errors can be bounded by $80C/N^2$ and $96C/N^2$, respectively,
once $N$ is sufficiently large. Taking powers with $n\le BN$
gives $\lambda(z)^n=e^{s\eta}+O_{B,C}(N^{-1})$.
The trace of a matrix power is the sum of eigenvalue powers even for
nonnormal matrices. The contribution of the other eigenvalues is at
most $N(3/4)^n$. This proves (2.5).

Cauchy's coefficient formula on $|z|=2$, applied to the polynomials
in (2.4), now proves, for every fixed $m\ge0$,

$$
 \sum_{x:\,\#\{j:x_j=v\}=m}|a(x)|^2
 =e^{-s}\frac{s^m}{m!}+O_{c,B,C,m}(N^{-1}),                    \tag{2.11}
$$

uniformly in $v$. This is the needed visit-count statement for
closed paths, whose total mass is $T_n$, rather than an assumed
stationary-chain probability law.

## 3. Good vertices have a positive linear mean

Call $v$ good for $x$ when it occurs exactly three times, the
three cyclic gaps between its occurrences are at least three, and
the six immediate predecessor and successor vertex labels at those
occurrences are pairwise distinct. Let $g(x)$ be the number of
good vertices. We prove

$$
 G_n:=\sum_x|a(x)|^2g(x)
 =N e^{-s}s^3/6+O_{c,B,C}(1).                                 \tag{3.1}
$$

Without the last two restrictions, this follows by summing (2.11)
with $m=3$ over $v$. It remains to bound the lost weighted count.

Every $P^k$ entry is at most $C/N$ for $k\ge1$, by
stochasticity and $P^k=P^{k-1}P$. For a fixed cyclic position
$i$ and $\ell=1,2$, the weight of words with
$x_i=x_{i+\ell}=v$ is
$(P^\ell)_{vv}(P^{n-\ell})_{vv}$. Thus the total lost count
from a gap one or two is bounded above by

$$
 n\sum_{\ell=1}^2\sum_v
       (P^\ell)_{vv}(P^{n-\ell})_{vv}
 \le2C^2n/N\le2C^2B.                                        \tag{3.2}
$$

This overcounts some words, which is legitimate in a nonnegative
bound. For large $N$ in the stated interval, $n>2$.

Next fix three distinct cyclic positions for the occurrences of
$v$, with gaps $\ell_1,\ell_2,\ell_3\ge3$. Denote the three
successor labels by $b_j$ and the three predecessor labels by
$a_j$. Summing over all intervening labels gives a product of
three factors of the form

$$
 P_{v b_j}(P^{\ell_j-2})_{b_j a_{j+1}}P_{a_{j+1}v}.            \tag{3.3}
$$

Bound the three middle factors by $C/N$. The remaining six
variables carry three row distributions of $P$ and three column
distributions; all have mass one and largest atom at most $C/N$.
For any chosen pair, its equality has product-distribution mass at
most $C/N$. A union bound over the 15 pairs therefore bounds the
weight for this fixed $v$ and set of positions by
$15C^4/N^4$. Summing over $N$ vertices and at most
$n^3/6$ position sets gives a bound $(5/2)C^4B^3$.
Dropping the condition that there are no further occurrences of
$v$ only enlarges this bound. Equations (3.2)--(3.3) prove (3.1).

## 4. Last exits form a directed tree

Fix a rooted cyclic word $x$ and let its root be $r=x_0$.
Temporarily distinguish different occurrences of the same oriented
edge by their position in $x$. This produces a finite directed
multigraph with equal incoming and outgoing degree at each vertex
and a specified Euler tour $x$.

For every visited vertex $v\ne r$, select the edge occurrence of
its **last departure** during this tour. These selected edges form
a directed tree toward $r$. To prove it, let the last departure
time from $v$ be $j$, and let its selected edge end at $w$.
If $w\ne r$, its next departure is at time $j+1$, or later
in the chosen chronological order, so the last departure time of
$w$ is strictly greater than $j$. A directed cycle of selected
edges is impossible. Every finite forward chain of them therefore
ends at the only visited vertex without a selected edge, namely
$r$.

Retain, at each nonroot vertex, its selected edge as the last item
in its list of outgoing edge occurrences. Order the preceding
items arbitrarily; order the root's list arbitrarily. Starting at
$r$, repeatedly use the next unused edge from the list at the
current vertex. This procedure always traverses all edges and
returns to $r$:

* It cannot get stuck at a vertex $v\ne r$. If all its outgoing
  edges had been used while the current trail ends at $v$, the
  number of used incoming edges would exceed its total incoming
  degree by one.
* If it stops at $r$, the used trail is closed, so used incoming
  and outgoing degrees agree at every vertex. If unused edges
  remain at some $v\ne r$, its selected last edge is unused.
  Its endpoint has unused incoming degree and hence unused outgoing
  degree. Following the selected tree would then force unused
  outgoing degree at $r$, contradicting the stopping condition.

Thus every such choice of lists yields a rooted Euler tour with
exactly the original oriented edge multiplicities. This proves the
enumeration mechanism without invoking an external theorem.

## 5. Simultaneous independent choices at good vertices

At a good vertex $v\ne r$, there are exactly three outgoing edge
occurrences, and their successor labels are distinct. Keep the
selected last edge fixed and independently choose either order for
the other two. At all other vertices keep the original outgoing
lists, including the root's list. Section 4 gives one complete
Euler tour for each binary choice.

These choices give distinct **unlabelled vertex words**, not merely
distinct artificially labelled tours. The vertex word records the
ordered successor list encountered at each good vertex. Its three
successor labels are distinct, so swapping the first two entries
changes this recorded list. Hence two different binary choices
cannot yield the same rooted word. Parallel edge occurrences at
other vertices do not affect this distinction.

There are therefore at least

$$
 2^{g(x)-1_{\{r\text{ good}\}}}\ge2^{g(x)-1}                   \tag{5.1}
$$

distinct rooted words $y$ with $L(y)=L(x)$. The lower bound is
valid even if $g(x)=0$; in that case its right side is $1/2$,
while the original word already gives one choice.

All such words have exactly the same complex amplitude as $x$.
Consequently, writing $w(x)=|a(x)|^2$,

$$
 \mathcal F_{n,N}\ge\frac12\sum_x w(x)2^{g(x)}.                \tag{5.2}
$$

For sufficiently large $N$, $T_n=\sum_xw(x)>0$ by (2.3).
Normalize these weights to a probability distribution and apply
convexity of the real exponential. This yields the exact bound

$$
 \boxed{\qquad
 \mathcal F_{n,N}\ge
 \frac{T_n}{2}\exp\left((\log2)\frac{G_n}{T_n}\right).
 \qquad}                                                     \tag{5.3}
$$

No independence of the visits or of the good-vertex indicators has
been assumed. Only their first weighted moment enters (5.3).
Substituting (2.3) and (3.1) proves (1.5), uniformly on the stated
scaled-time interval. Unitarity in (1.4) proves (1.6).

For a fixed $x$, each of the two rotation classes contains at
most $n$ distinct rooted words. Among those with the same edge
counts, every summand equals $w(x)$. Removing them therefore
loses at most $2n\sum_x w(x)=2nT_n$, proving (1.7).

## 6. Relation to the original remaining class

The exact physical-cycle decomposition from the companion source is
$|\operatorname{Tr}U_N^n|^2=D_{n,N}+R_{n,N}+Z_{n,N}$.
The positive class $\mathcal C_{n,N}$ in (1.7) is contained in
$Z_{n,N}$, with no overlap with $D$ or $R$. Put
$\mathcal W_{n,N}=Z_{n,N}-\mathcal C_{n,N}$.

Even without the stronger estimate on $Q_N$, the reversed class
has $|R_{n,N}|\le nC$. Indeed let
$S_{xy}=\sqrt{P_{xy}P_{yx}}$. Its row sums are at most one by
Cauchy--Schwarz, and $S_{xy}\le C/N$, hence
$\operatorname{Tr}S^n\le C$. Removing repeated rotations only
decreases the corresponding absolute sum, so
$|R_{n,N}|\le n\operatorname{Tr}S^n\le nC$.
Since $D\ge0$,

$$
 \mathcal W_{n,N}\le N^2+nC-\mathcal C_{n,N}.                  \tag{6.1}
$$

Thus the unevaluated $Z$ contains positive and negative contributions
of at least an exponential scale. This follows for the **actual**
matrices from proved kernel estimates; it is not a claim about a
random replacement or a different matrix family.

The stronger companion estimates
$\sum_n|D_{n,N}-n|=O(1)$ and $\sum_n|R_{n,N}|=o(1)$
still leave the first unproved fixed-test assertion

$$
 N^{-2}\sum_{1\le n<2N}|\widehat b_*(n/N)|^2Z_{n,N}
 \longrightarrow-\int_1^2(s-1)|\widehat b_*(s)|^2\,ds.          \tag{6.2}
$$

Equations (1.5)--(6.1) do not supply (6.2). They identify a large
exactly coherent part of its summands and prove that another part
must compensate it. Determining the remaining weighted residue at
the required scale is still open, as are all higher orders in
$H_{\rm diag}$. In particular a lower bound for a positive subclass
is **not** a lower bound for the full signed statistic.
