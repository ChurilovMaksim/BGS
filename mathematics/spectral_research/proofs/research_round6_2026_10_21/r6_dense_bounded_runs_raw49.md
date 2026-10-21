> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_dense_bounded_runs_raw49.md`. Embedded SHA256: `631663c9639c286510125df4806b833d4cfb8344a7a9d0fc36d6c647e83bc9e8`.
> [Thematic guide](../../topics/histories.md).

# All-time cancellation for every bounded disagreement run through length 48

21 October 2026. This note proves a signed estimate for an actual,
unmarked class of rooted path pairs of the exact original matrix.
Every number of disagreement runs is allowed; every run may have
length from 1 through 48; all physical labels may repeat.
The estimate holds for every time and has an exponential time weight.
No random phases enter the estimate.

The class includes both equal-occupation and unequal-occupation pairs.
It is a complete raw class, rather than the complete
unequal-occupation remainder. Its equal-occupation subseries is not
estimated separately here. Consequently this theorem does not prove
H_diag or a spectral limit.

## 1. Exact class and quantitative original-family theorem

For a rooted cyclic word $x=(x_0,\ldots,x_{n-1})$, let
$$
 a_N(x)=\prod_{i\bmod n}(U_N)_{x_i x_{i+1}}.
$$
Let $\mathcal C_{n,48}^{\ne}$ consist of all ordered rooted pairs
(x,y) such that:

- there is at least one agreement $x_i=y_i$;
- $x\ne y$;
- every consecutive cyclic run of disagreements has length at most 48.

Every pair is included exactly once. There is no marked agreement,
marked run, orbit quotient, or regularity condition on repeated labels.
The requirement of an agreement excludes pairs differing at every
position, even when n is small.
Define
$$
 T_{n,N}^{[48]}
 =\sum_{(x,y)\in\mathcal C_{n,48}^{\ne}}
             a_N(x)\overline{a_N(y)}.              \tag{1.1}
$$

Let
$$
 \begin{pmatrix}3&4\\2&3\end{pmatrix}^{49}
 =\begin{pmatrix}a_{49}&b_{49}\\c_{49}&a_{49}\end{pmatrix},
 \qquad
 b_{49}=22988051704762092309141120595493810884.
$$
Put the exact finite constant
$$
 K_{49}=1500000000\,(4b_{49}-1).                    \tag{1.2}
$$
For every sufficiently large odd N of the prescribed family,
$$
 \boxed{\quad
 \sum_{n\ge1}\left(\frac{100}{99}\right)^n
                 |T_{n,N}^{[48]}|
       \le K_{49}.
 \quad}                                           \tag{1.3}
$$
In particular,
$$
 |T_{n,N}^{[48]}|\le K_{49}(99/100)^n,              \tag{1.4}
$$
and for every integer $M\ge0$,
$$
 \sum_{n>M}|T_{n,N}^{[48]}|
       \le K_{49}(99/100)^{M+1}.                  \tag{1.5}
$$
The integer constant is large, but independent of N. There is no
upper time-band restriction in this raw-class theorem.

A smaller unweighted constant, obtained in the same proof, is
$$
 \boxed{\quad
 \sum_{n\ge1}|T_{n,N}^{[48]}|
       \le221323199\,(4b_{49}-1).
 \quad}                                           \tag{1.6}
$$
Thus the contribution of this entire class after normalization by
$N^2$ is $O(N^{-2})$, even for arbitrary uniformly bounded
weights on all positive times.

## 2. Exact transfer and the absence of marking multiplicity

We first work with a finite unitary U. On its $N^2$-dimensional
pair space let
$$
 W=U\otimes\overline U.
$$
Let M project onto the diagonal pair states $(a,a)$, and let
$O=I-M$. In this decomposition,
$$
 W=\begin{pmatrix}P&B\\ C&S\end{pmatrix},
 \qquad P_{ab}=|U_{ab}|^2.
$$
The first-return matrices are
$$
 F_1=P,\qquad F_r=BS^{r-2}C\quad(r\ge2),            \tag{2.1}
$$
and unrestricted returns are
$$
 R_0=I,\qquad R_j=MW^jM=|U^j|^{\circ2}.
$$
Splitting at a first return proves exactly
$$
 R_j=\sum_{r=1}^jF_rR_{j-r}.                       \tag{2.2}
$$
Each R_j is doubly stochastic. With $J=ee^*$ and
$e=N^{-1/2}(1,\ldots,1)^T$, (2.2) proves
$$
 F_re=0,\quad e^*F_r=0\quad(r\ge2).                \tag{2.3}
$$

For an integer $R\ge2$, to permit disagreement runs of length at most $R-1$, introduce
one copy of O for each age $1,\ldots,R-1$. The transfer A has
blocks
$$
 A_{00}=P,\quad A_{0,1}=B,\quad A_{j,0}=C
       \ (1\le j\le R-1),\quad
 A_{j,j+1}=S\ (1\le j<R-1),                       \tag{2.4}
$$
with every other block zero. A closed walk necessarily visits M,
since the age increases strictly during a run confined to O.
The age of a physical disagreement at a given rooted position is
forced by its most recent cyclic agreement. Hence every allowed
physical rooted pair has exactly one lift. No marking factor
is present.

It follows that
$$
 \operatorname{Tr}A^n
 =\sum_{\substack{(x,y):\text{at least one agreement}\\
                \text{each disagreement run}\le R-1}}
                 a(x)\overline{a(y)}.
$$
The all-agreement pairs $x=y$ contribute exactly
$\operatorname{Tr}P^n$. Therefore the nonempty raw class is
$$
 T_n^{[R-1]}=\operatorname{Tr}A^n-\operatorname{Tr}P^n.
                                                               \tag{2.5}
$$
Eliminating the nilpotent age block gives the finite determinant
identity
$$
 \det(I-sA)
 =\det\left(I-\sum_{r=1}^R s^rF_r\right).          \tag{2.6}
$$
Indeed the eliminated terms are precisely
$s^{j+2}BS^jC$, $0\le j\le R-2$.
This is also the determinant of the R-block companion with top
row $F_1,\ldots,F_R$ and identity subdiagonal.

These counting and determinant identities were proved in full and
checked with formal coordinate phases in the frozen renewal note.
The elementary derivation above shows directly why they apply
to exactly the raw class in (1.1).

## 3. Quantitative first-return bounds from physical powers

Write $E_j=R_j-J$, and set
$$
 G_1=E_1,\qquad G_r=F_r\quad(2\le r\le R).
$$
All G_r annihilate constants on both sides. Equations (2.2)--(2.3)
give
$$
 G_r=E_r-\sum_{j=1}^{r-1}G_jE_{r-j}
      \quad(r\ge2).                               \tag{3.1}
$$
Assume the following concrete finite list of physical estimates:
$$
 \|E_j\|_{\rm op}\le q,\qquad
 \max_{a,b}|(U^j)_{ab}|^2\le C_j/N,
      \quad1\le j\le R,                           \tag{3.2}
$$
where $C_j\ge1$.

### Operator norms

Induction in (3.1) proves
$$
 \boxed{\ \|G_r\|_{\rm op}
       \le q(1+q)^{r-1}\quad(1\le r\le R).\ }      \tag{3.3}
$$
In fact, if the preceding bounds hold, the right side of
$\|G_r\|\le q+q\sum_{j<r}\|G_j\|$ equals
$$
 q+q\sum_{j=1}^{r-1}q(1+q)^{j-1}
     =q(1+q)^{r-1}.
$$

### Hilbert--Schmidt norms

The entry estimate in (3.2) and unitarity give
$$
 \|E_j\|_{\rm HS}^2
 =\sum_{a,b}|(U^j)_{ab}|^4-1\le C_j-1.             \tag{3.4}
$$
Every F_j is a contraction as a product of compressions of W,
and $\|E_1\|\le1$ because P is a doubly stochastic contraction.
Thus (3.1), used with these contraction bounds, gives
$$
 \|G_r\|_{\rm HS}\le h_r:=
       \sum_{j=1}^r\sqrt{C_j-1},\qquad1\le r\le R.
                                                               \tag{3.5}
$$
The same formula applies to $r=1$ directly.

### Traces of individual returns

Since every diagonal entry of R_r is at most $C_r/N$,
$$
 0\le\operatorname{Tr}R_r\le C_r,\qquad
 |\operatorname{Tr}E_r|\le\max(1,C_r-1).
$$
Using the Hilbert--Schmidt trace inequality in (3.1) proves
$$
 |\operatorname{Tr}G_r|\le t_r:=
 \max(1,C_r-1)+
       \sum_{j=1}^{r-1}h_j\sqrt{C_{r-j}-1},
       \qquad2\le r\le R.                        \tag{3.6}
$$
This bound is essential for words with a single return factor.
An operator-norm estimate alone would introduce an unnecessary
factor N at that step.

## 4. An absolutely summable logarithmic expansion

For $0<\rho\le1$, define
$$
 a_\rho=\sum_{r=1}^R
                 \rho^{-r}q(1+q)^{r-1},\qquad
 H_\rho=\sum_{r=1}^R\rho^{-r}h_r,\qquad
 T_\rho=\sum_{r=2}^R r\rho^{-r}t_r.                \tag{4.1}
$$
If $a_\rho<1$, then
$$
 \boxed{\quad
 \sum_{n\ge1}\rho^{-n}|T_n^{[R-1]}|
       \le T_\rho+\frac{R H_\rho^2}{1-a_\rho}.
 \quad}                                          \tag{4.2}
$$

Here is a complete coefficient proof. The constant vector gives
the common factor $1-s$ in (2.6) and $\det(I-sP)$.
On its orthogonal complement put
$$
 G(s)=\sum_{r=1}^R s^rG_r.
$$
The formal logarithmic determinant identity and (2.5)--(2.6)
give
$$
 \sum_{n\ge1}\frac{s^n}{n}T_n^{[R-1]}
 =\sum_{m\ge1}\frac1m
    \left\{\operatorname{Tr}G(s)^m
          -\operatorname{Tr}(sG_1)^m\right\}.      \tag{4.3}
$$
This is initially an identity of formal power series. It follows
from differentiating a determinant, expanding
$(I-sA)^{-1}$, and matching the zero constant term; equivalently
from $-\log\det(I-H)=\sum_{m\ge1}\operatorname{Tr}H^m/m$
for a matrix series H with zero constant term. Each coefficient
in (4.3) involves only finitely many terms, so no convergence
has yet been assumed.

In the $m=1$ term the contribution of $G_1$ cancels exactly.
After multiplying the nth coefficient by n, its total weighted
absolute sum is at most $T_\rho$.
For $m\ge2$, expand into ordered words
$(r_1,\ldots,r_m)\in\{1,\ldots,R\}^m$.
The all-1 word cancels. If
$n=r_1+\cdots+r_m$, then $n/m\le R$.
For every remaining word, two Hilbert--Schmidt factors give
$$
 |\operatorname{Tr}(G_{r_1}\cdots G_{r_m})|
 \le h_{r_1}h_{r_2}
                  \prod_{j=3}^m\|G_{r_j}\|_{\rm op}.             \tag{4.4}
$$
This follows from
$|\operatorname{Tr}XY|\le\|X\|_{\rm HS}\|Y\|_{\rm HS}$
and $\|AB\|_{\rm HS}\le\|A\|_{\rm HS}\|B\|_{\rm op}$.
The weight $\rho^{-n}$ factors over the word.
Allowing also the all-1 word in a nonnegative upper bound and
summing gives at most
$$
 R H_\rho^2 a_\rho^{m-2}.
$$
Its sum over $m\ge2$ converges to the second term of (4.2).
Tonelli's theorem for this nonnegative majorant proves the
absolute coefficient summability and justifies every subsequent
reordering. This proves (4.2).

The matrices F_r already contain the full complex sum over their
internal disagreement runs. Their cancellations, unitarity, and
physical power estimates are retained before (4.4) is used.
No bound by the moduli of individual original orbit amplitudes
has replaced those sums.

## 5. Verification of every hypothesis for the exact original family

The frozen original fixed-power theorem proves simultaneously,
for every sufficiently large odd N,
$$
 \max_{1\le j\le49}\bigl\||U_N^j|^2-J_N\bigr\|_{\rm op}
     \le1/100,\qquad
 \max_{a,b}|(U_N^j)_{ab}|^2\le4b_j/N.              \tag{5.1}
$$
Here $b_j$ is the upper-right entry of
$\begin{pmatrix}3&4\\2&3\end{pmatrix}^j$.
The proof verifies its sufficient condition
$51200t\Sigma_j^2\le1$ for every $j\le49$ at the original
fixed $t=10^{-80}/(2\pi)$. There is no dimension-dependent
kick or restriction to a convenient subsequence.

Apply (4.2) with
$$
 R=49,\quad q=1/100,\quad C_j=4b_j,\quad
 \rho=99/100.
$$
The exact geometric sum is
$$
 a_\rho
 =\frac12\left[\left(\frac{101}{99}\right)^{49}-1\right]
 <\frac{55}{64}<1.                               \tag{5.2}
$$
For a proof of the displayed rational bound,
$$
 (101/99)^{49}<e^{98/99}<e<87/32.
$$
The last inequality follows by bounding the terms of the
exponential series from index 4 onward:
$$
 e=\sum_{k\ge0}\frac1{k!}
 <\frac83+\frac1{24}\sum_{j\ge0}5^{-j}
 =\frac{87}{32}.
$$
The bound on the tail uses
$(4+j)!\ge24\cdot5^j$; strictness holds for some terms.
Thus (5.2) involves no numerical approximation to a matrix norm.
Likewise,
$$
 \rho^{-49}
 =(100/99)^{49}<e^{49/99}<\sqrt e<5/3.             \tag{5.3}
$$

The sequence b_j is increasing. Put $C=4b_{49}$.
Equations (3.5)--(3.6) yield the convenient explicit bounds
$$
 h_r\le r\sqrt{C-1},\qquad
 t_r\le(C-1)\left(1+\frac{r(r-1)}2\right).
                                                               \tag{5.4}
$$
The trace estimate uses $C_r\ge16$, so
$\max(1,C_r-1)=C_r-1$.
The exact finite sums are
$$
 \sum_{r=1}^{49}r=1225,\qquad
 \sum_{r=2}^{49}r\left(1+\frac{r(r-1)}2\right)=731324.
$$
Therefore
$$
 H_\rho\le\frac53\,1225\sqrt{C-1},\qquad
 T_\rho\le\frac53\,731324(C-1),\qquad
 \frac1{1-a_\rho}<\frac{64}{9}.
$$
The right side of (4.2) is bounded by
$$
 (C-1)\left[
    \frac53\,731324
     +49\frac{64}{9}\frac{25}{9}\,1225^2\right]
 =\frac{117747728740}{81}(C-1)
 <1500000000(C-1).
$$
This proves (1.3) with the exact constant (1.2).
Equations (1.4)--(1.5) follow immediately from the nonnegative
weighted sum.

For (1.6), take $\rho=1$. The geometric sum becomes
$$
 a_1=(101/100)^{49}-1<2/3
$$
by the same bound $(101/100)^{49}<\sqrt e<5/3$.
Thus (4.2) is at most
$$
 (C-1)\left[731324+3\cdot49\cdot1225^2\right]
   =221323199(C-1).
$$
This finishes the stated all-time signed theorem.

## 6. Exact scope and the remaining obstacle

If $d(x)$ denotes the occupation vector, let
$$
 H_{n,N}^{[48]}
 =\sum_{\substack{(x,y)\in\mathcal C_{n,48}^{\ne}\\d(x)=d(y)}}
           a_N(x)\overline{a_N(y)}.
$$
The actual unequal-occupation contribution from this same class is
$$
 \Omega_{n,N}^{[48]}=T_{n,N}^{[48]}-H_{n,N}^{[48]}.
$$
The present theorem controls the first term completely.
It gives no separate bound for the second term. An estimate for
the positive full same-occupation form factor does not in general
bound this signed subset. The concentration theorem for isolated
single disagreements, corresponding to run length 1, likewise
does not extend to run length 48 merely from (1.3).

Furthermore, pairs with a disagreement run longer than 48 and
pairs with no agreement anywhere are outside the class.
The exact return-energy theorem proves that the energy in those
long returns cannot simply be discarded. Their signed spectral
contribution remains a distinct unresolved problem.

Thus this result is a genuine all-order cancellation theorem for
a larger deterministic raw class, with all repeated labels and all
times included. It is not a statement of H_diag, an approximation
of the original matrix by random phases, or an estimate for the
whole unequal-occupation remainder.

## Sources and verification

The complete physical hypotheses (5.1) are proved in:

- research_round6_2026_10_21/r6_original_fixed_powers_49.md,
  equations (1.8)--(1.9) and the exact threshold check in §7;
  SHA256 3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019.
- Its independent complete audit:
  research_round6_2026_10_21/r6_occupation_audit_fixed_powers_49.md;
  SHA256 0953ee6eb3c665fe667fabcb094651eb7284f6250ebfa2c6d535bd98f7da9b61.

The exact first-return identities and unmarked age transfer are
also established in:

- research_round6_2026_10_21/r6_dense_renewal_long_return_obstruction.md;
  SHA256 95ea7e37c46b840854853c934eebecbd51ac1cb305d0200a283e68b9f7c3d0b2.

The latter note's exact-arithmetic checks include all mismatch-count
coefficients of 38,188 rooted pair weights with formal coordinate
phases, and twelve full companion determinant comparisons. They
verify the finite encoding used here. The constants in §5 were
also checked as exact integer or rational inequalities; their full
elementary proofs are given above. No numerical spectral
experiment or unproved statistical independence assumption enters
the theorem.

