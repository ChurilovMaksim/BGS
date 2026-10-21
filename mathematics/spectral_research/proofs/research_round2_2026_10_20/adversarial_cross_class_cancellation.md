> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/adversarial_cross_class_cancellation.md`. Embedded SHA256: `0ba7b2f260b2fbc80236b0e82d4960f726850bad0f33563b5582705d48c549a4`.
> [Thematic guide](../../topics/histories.md).

# Actual cross-class correlations forced beyond the dimension threshold

Research continuation, 20 October 2026. The quantum family is exactly
the one in the question, at the unchanged $\tau=10^{-80}$, and all
limits below run through all sufficiently large odd $N$.

## 1. The statement to be tested

The actual three-cell calculation and its six-connection extension
evaluate complete reconnection classes through long zero buffers.
They do not justify dropping products belonging to different
collections of interiors. This note proves a stronger, quantitative
fact: for a fixed sufficiently large logarithmic-buffer offset,
the total cross-class contribution is bounded above by a strictly
negative constant at every degree in a full Heisenberg band.

Thus the tempting statement
$$
 \text{the signed contribution between different complete
 long-buffer reconnection classes is }o(1)
 \tag{1.1}
$$
is false for the actual family and the actual principal Euler
coefficient. The proof allows every number of cuts, arbitrary
admissible nonzero interiors, and buffers longer than the chosen
threshold. It is not a toy-model counterexample.

The result concerns the principal Euler coefficients, not the
complete power-trace statistic. It neither proves nor refutes
$H_{\rm diag}$.

## 2. Exact objects and proved inputs

The following frozen inputs are used.

| Input | SHA-256 |
|---|---|
| fermionic_pseudoorbit_cutoff.md | 03173e53d1a10e2c1afad517c48943a5330d43fc4059b80fc0e37d5b1598a9eb |
| fermionic_signed_three_cell_profile.md | edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5 |
| fermionic_six_connection_cancellation.md | 4661fed89558f03c58e085ec70df919b14056ff4ec5e3e765e6564ce35fbb865 |

Let $p_0$ be the interior fixed orbit coded by the constant
zero loop, and let $\Lambda>5$ be its actual unstable multiplier.
Use $a_{p,N}$ for the exact primitive principal weight and
$d_p$ for the primitive period. In particular write
$a_{0,N}=a_{p_0,N}$. Put
$$
 h=(2\pi N)^{-1},\qquad
 \mathcal Z_N(z)=\prod_{p\ {\rm primitive}}
                         (1-a_{p,N}z^{d_p}).
$$
Every coefficient has its exact finite Euler expansion. We remove
$p_0$ from every orbit set in this note and use
$$
 \mathcal Z_N^-(z)=
 \prod_{p\ne p_0}(1-a_{p,N}z^{d_p})
 =\frac{\mathcal Z_N(z)}{1-a_{0,N}z}.
 \tag{2.1}
$$
The superscript minus means deletion of this one primitive factor.

For $m\ge0$, let $\mathcal E_m^-$ be the finite set of all
finite subsets $\mathfrak p$ of distinct primitive orbits,
excluding $p_0$, whose periods sum to $m$. Define
$$
 A_N(\mathfrak p)=(-1)^{|\mathfrak p|}
                     \prod_{p\in\mathfrak p}a_{p,N},
 \qquad
 Q_{m,N}^-=\sum_{\mathfrak p\in\mathcal E_m^-}
                                  |A_N(\mathfrak p)|^2.
 \tag{2.2}
$$
Thus $\sum_{\mathfrak p\in\mathcal E_m^-}A_N(\mathfrak p)$
is the coefficient of $\mathcal Z_N^-$, not that of
$\mathcal Z_N$.

The actual amplitude modulus estimate is
$$
 |a_{p,N}|^2=\Lambda_p^{-1}e^{\xi_{p,N}},
 \qquad |\xi_{p,N}|\le C d_p h^2.
 \tag{2.3}
$$
The classical positive Euler product has the proved form
$$
 F_0(z)=\prod_p(1+\Lambda_p^{-1}z^{d_p})
       =\frac{e^{H_F(z)}}{1-z},
 \tag{2.4}
$$
where $H_F$ is holomorphic in a fixed disk of radius
$R_{\rm cl}>1$, and
$$
 C_F=e^{H_F(1)}>0.
 \tag{2.5}
$$

For the actual positive transfer operator the signed-profile
input proves
$$
 \sup_{\ell\ge0}\|T^\ell\|<\infty,\qquad
 \|J^R\|\le C_J\Lambda^{-R},\qquad
 (J^Rf)(o)=\Lambda^{-R}f(o).
 \tag{2.6}
$$
Its periodic product is the exact $\Lambda_p^{-1}$ geometric
weight. An open word beginning and ending with $R$ zero edges
has its periodic and open weights in ratio $1+O(\theta^R)$,
uniformly in the middle word and its length. This follows from
the explicitly proved one-sided Hölder sum, with $\theta=2/3$.

Finally
$$
 \mathcal Z_N(z)=D_N(z)e^{G_N(z)},\quad
 D_N(z)=\det(I-zU_N),\quad
 |e^{G_N(z)}|\le(1-.421|z|)^{-2}
 \tag{2.7}
$$
on $|z|<.421^{-1}$, and
$$
 |\operatorname{Tr}U_N^d|\le3\min(N,a^d),
 \qquad a=\sqrt{3+2\sqrt2}\,1.0002.
 \tag{2.8}
$$
These inputs are actual all-time identities and estimates.

## 3. The positive coefficient after deletion of the fixed orbit

The classical product omitting $p_0$ is
$$
 F_0^-(z)=\frac{F_0(z)}{1+\Lambda^{-1}z}
 =\frac{e^{H_F(z)}}{(1-z)(1+\Lambda^{-1}z)}.
 \tag{3.1}
$$
The additional denominator has its zero at $-\Lambda$, outside
the unit circle. For any fixed
$1<r<\min(R_{\rm cl},\Lambda)$, the function
$$
 H_-(z)=\frac{e^{H_F(z)}}{1+\Lambda^{-1}z}
$$
is holomorphic on $|z|<r$. Summing its Taylor coefficients
therefore gives
$$
 [z^m]F_0^-(z)=C_-+O(r^{-m}),\qquad
 C_-:=\frac{C_F}{1+\Lambda^{-1}}>0.
 \tag{3.2}
$$
In particular these nonnegative coefficients are uniformly
bounded for all $m\ge0$.

For each orbit set of total degree $m$, (2.3) bounds the ratio
of its squared quantum weight to its classical geometric weight
between $e^{-Cmh^2}$ and $e^{Cmh^2}$. Positivity gives the
same bounds after summation:
$$
 e^{-Cmh^2}[z^m]F_0^-\le Q_{m,N}^-
                  \le e^{Cmh^2}[z^m]F_0^-.
 \tag{3.3}
$$
Consequently, for every fixed $B<\infty$,
$$
 \sup_{0\le m\le BN}Q_{m,N}^-\le M_B,
 \tag{3.4}
$$
with a fixed finite $M_B$, and uniformly for
$bN\le m\le BN$, $b>0$,
$$
 Q_{m,N}^-=C_-+o(1).
 \tag{3.5}
$$
This checks the factor $1+\Lambda^{-1}$ in the positive
normalization. The signed denominator in (2.1) is different.

## 4. A marked primitive orbit has total weight $O(\Lambda^{-2R})$

Fix an integer $R_0\ge0$ and set
$$
 R=\left\lceil\frac{\log N}{2\log\Lambda}\right\rceil+R_0,
 \qquad k=2R,\qquad \varepsilon=\Lambda^{-k}.
 \tag{4.1}
$$
Then $N\varepsilon\le\Lambda^{-2R_0}$. For a nonconstant
primitive cyclic code of period $d$, let $r_k(p)$ be the
number of cyclic positions at which $k$ successive zero
edges occur. Overlapping occurrences are counted.

If $d\le k$, a primitive code with such an occurrence must be
the constant zero code. Indeed a nonzero edge in a $d$-periodic
word is met within every $d$ successive positions. Since
$p_0$ was deleted, the only relevant periods satisfy $d\ge k+1$.
The sole periodic boundary point creates no ambiguity here:
its finite coding fiber has at most four elements, so every
one of its itineraries has period at most four. For $k>4$
none can contain $0^k$, since the constant zero itinerary
codes the different interior point $p_0$. Assign $r_k=0$
to that boundary orbit.

For a primitive orbit of period $d\ge k+1$, every marked
occurrence determines a unique midpoint cut. Its chronological
word then has the form
$$
 0^R\,u\,0^R,\qquad |u|=d-k.
 \tag{4.2}
$$
The same orbit contributes once for each such marked pointed
position. Hence its contribution to the sum over all such
period-$d$ words is precisely
$r_k(p)\Lambda_p^{-1}$. Allowing imprimitive periodic words
only increases that positive sum.

The open sum of all words (4.2), evaluated at the constant
zero tail, is
$$
 [J^R T^{d-k}J^R1](o).
 \tag{4.3}
$$
The left $J^R$ evaluates exactly as in (2.6); the other
factors have the uniformly bounded norms in (2.6). Thus
(4.3) is at most $C\Lambda^{-2R}=C\varepsilon$.
The open-periodic comparison multiplies this by a fixed
constant at most. We obtain
$$
 \boxed{\displaystyle
 \sum_{\substack{p\ne p_0\\d_p=d}}
       r_k(p)\Lambda_p^{-1}\le C_{\rm mark}\varepsilon,
 \qquad d\ge k+1.}
 \tag{4.4}
$$
There is no missing factor $d$: the left side already counts
exactly the marked pointed positions, not all $d$ positions
of every orbit.

For $d\le BN$, (2.3) has multiplicative error at most
$e^{CBNh^2}=1+o(1)$. Increasing a fixed constant gives
$$
 \sum_{\substack{p\ne p_0\\d_p=d}}
       r_k(p)|a_{p,N}|^2\le C_B\varepsilon,
 \qquad k+1\le d\le BN.
 \tag{4.5}
$$
All estimates are uniform in those degrees and all large odd $N$.

## 5. Marker-free Euler sets retain positive mass

Call an orbit set in $\mathcal E_m^-$ marker-free if
$r_k(p)=0$ for every one of its components. Let
$Q_{m,N}^{\rm free}$ be the sum of its squared weights.

Use $1_{\{\exists p:r_k(p)>0\}}\le\sum_{p\in\mathfrak p}r_k(p)$
and remove one distinguished primitive factor. The remaining
orbit sets exclude both $p_0$ and that distinguished orbit;
their positive coefficient is at most $Q_{m-d,N}^-$.
Therefore
$$
 \begin{aligned}
 Q_{m,N}^- -Q_{m,N}^{\rm free}
 &\le
 \sum_{d=k+1}^m Q_{m-d,N}^-
       \sum_{\substack{p\ne p_0\\d_p=d}}
            r_k(p)|a_{p,N}|^2\\
 &\le C_B\,m\varepsilon.
 \end{aligned}
 \tag{5.1}
$$
This is a positive Euler union bound. It does not replace a
signed orbit sum by its absolute values.

Combining (3.5), (4.1), and (5.1), uniformly for
$bN\le m\le BN$,
$$
 \boxed{\displaystyle
 Q_{m,N}^{\rm free}
 \ge C_- - C_B'\Lambda^{-2R_0}+o(1).}
 \tag{5.2}
$$
Choose $R_0$ once and for all so that
$C_B'\Lambda^{-2R_0}<C_-/4$. This is an auxiliary fixed buffer
offset, not a change of $\tau$ or of the quantum family.
Then for all large odd $N$,
$$
 Q_{m,N}^{\rm free}\ge C_-/2
 \qquad(bN\le m\le BN).
 \tag{5.3}
$$

## 6. The signed series with the fixed orbit removed still cuts off

The cutoff must be checked for $\mathcal Z_N^-$, since it is
the series summed here. Equation (2.3) at $p_0$ gives
$$
 |a_{0,N}|^2=\Lambda^{-1}e^{O(h^2)}.
 \tag{6.1}
$$
As $\Lambda>5$, for all large $N$ one has
$|a_{0,N}|\le.48$, so $1-a_{0,N}z$ has no zero on
$|z|\le2$ and its reciprocal is at most $25$ there.
Also $2<.421^{-1}$, so (2.7) applies on that circle.

For clarity, (2.8) gives
$$
 S_N(2):=\sum_{d\ge1}
              \frac{|\operatorname{Tr}U_N^d|}{d\,2^d}
 \le C\,\frac{N^\beta}{\log N}=o(N),
 \quad \beta=1-\frac{\log2}{\log a}\in(0,1).
 \tag{6.2}
$$
Split at $\lfloor\log_aN\rfloor$: the first part is a
geometric sum of $(a/2)^d/d$, and the second is bounded by
$N\sum 2^{-d}/d$. Both have the order stated in (6.2).

Unitarity gives the exterior determinant bound
$$
 |D_N(2e^{it})|\le2^N e^{S_N(2)}.
 \tag{6.3}
$$
Use (2.1), (2.7), (6.1), and Cauchy's coefficient formula:
$$
 |[z^m]\mathcal Z_N^-|
 \le C\,2^{N-m}\exp(S_N(2)).
 \tag{6.4}
$$
In particular there is a fixed $c_0>0$ such that
$$
 \boxed{\displaystyle
 |[z^m]\mathcal Z_N^-|\le e^{-c_0N},
 \qquad 6N/5\le m\le3N/2,}
 \tag{6.5}
$$
for every sufficiently large odd $N$. The proof uses the
complete geometric trace tail in (6.2); no truncation is left
uncontrolled.

## 7. Complete reconnection classes and the forced cross term

Here is one precise class relation containing all the reconnections
already evaluated in the signed-profile and six-connection notes.
For a term in $\mathcal E_m^-$, choose finitely many disjoint cuts,
each with at least $R$ zero edges on both sides. Follow its orbits
between cuts to obtain cells, each containing at least one nonzero
edge. Reconnect these cells by any successor permutation, retaining
uncut components. Allow the move whenever its output is again a
set of distinct primitive orbits, excluding $p_0$, with the same
total degree. Use the equivalence relation generated by all such
moves, in both directions.

Every resulting cut still has $R$ zero edges on both sides.
Thus neither endpoint of a nontrivial move can be marker-free.
In particular every marker-free orbit set is an isolated, singleton
class. This remains true if one allows arbitrarily longer buffers,
all admissible incoming and outgoing nonzero edges, and every finite
number of cuts. The six reconnections of each good three-cell
cluster are in a single such class.

In fact the following conclusion holds for **any** partition
$\mathscr C_{m,N}$ of $\mathcal E_m^-$ which leaves those
marker-free sets singleton. Let its exact class sums be
$$
 B_N(C)=\sum_{\mathfrak p\in C}A_N(\mathfrak p).
 \tag{7.1}
$$
Positivity gives
$$
 \sum_{C\in\mathscr C_{m,N}}|B_N(C)|^2
       \ge Q_{m,N}^{\rm free}.
 \tag{7.2}
$$
No estimate of a nonsingleton class is used.

The full ordered cross-class sum is
$$
 \mathcal X_{m,N}
 :=\sum_{\substack{C,C'\in\mathscr C_{m,N}\\C\ne C'}}
                            B_N(C)\overline{B_N(C')}.
 \tag{7.3}
$$
It is real, and the exact square identity yields
$$
 \mathcal X_{m,N}
 =|[z^m]\mathcal Z_N^-|^2
       -\sum_C|B_N(C)|^2.
 \tag{7.4}
$$
Consequently, uniformly for $6N/5\le m\le3N/2$,
$$
 \boxed{\displaystyle
 \mathcal X_{m,N}
 \le -C_-+C'\Lambda^{-2R_0}+o(1).}
 \tag{7.5}
$$
For the fixed sufficiently large offset in Section 5, this gives
$$
 \boxed{\displaystyle
 \mathcal X_{m,N}\le-C_-/4<0}
 \tag{7.6}
$$
for every sufficiently large odd $N$ and every degree in the
band. No upper bound on $|\mathcal X_{m,N}|$ is asserted; its
negative magnitude could be larger than this fixed lower bound.

The constants in (7.5) are independent of the choice of partition,
provided its marker-free classes are singleton. Thus evaluating
additional within-buffer permutations cannot remove the conclusion.

## 8. Consequence for the attempted completion

The actual one-family sine kernel and the actual six-term
fermionic cancellation can be enlarged to every reconnection
allowed in Section 7, and each enlarged class can hypothetically
be evaluated exactly. One still cannot discard the products
between those classes: the actual coefficient cutoff forces a
strictly nonvanishing negative total between them.

These terms compare different retained interior collections.
Their exact actions include differences of the cell base values
$W_e(q_*,q_*)$, which cancel inside one reconnection family but
not between arbitrary families. The independent endpoint
probability laws do not compute those differences.

Equation (7.6) is therefore a concrete disproof, on the original
family, of the proposed cross-class $o(1)$ step (1.1). It does
not disprove a method that also computes these cross-class phases.
It does not imply a counterexample to $H_{\rm diag}$, whose
power-trace and factorial observables remain different. The new
result identifies an actual correlation that a successful
completion must retain rather than assume away.
