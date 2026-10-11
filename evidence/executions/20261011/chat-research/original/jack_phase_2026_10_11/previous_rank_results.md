# Recovery of the preceding occupation/rank work

The preceding session ended while the runtime was disconnected. Its latest
birthday-law and central-limit statements were not saved. This note gives a
fresh self-contained coupling proof of the same asymptotic laws. It uses
looser first-moment constants but improves the simple total-variation
constant and removes reliance on a global signed-graph rank lemma.

The existing earlier research directories are left unchanged. Their pinned
computation inputs and evidence records have not been overwritten.

## Setup

Let \(x_1,\ldots,x_n\) be independent uniform labels in a set of size \(N\),
and conditionally choose \(h\) uniformly from the permutations preserving
all labels. Thus on each occupation block it is an independent uniform
permutation. Let \(C\) be the adjacency matrix of the cycle on \(n\ge3\)
positions, and

\[
R=\operatorname{rank}(C-P_hCP_h^T).
\]

The rank may be over any field. None of the argument below uses a
characteristic-specific cancellation.

Define

\[
L=\sum_{i<j}\mathbf1_{x_i=x_j},\qquad
\mu=\frac{n(n-1)}{2N},\qquad
K_3=\sum_v\binom{m_v}{3}.
\]

Distinct collision-pair indicators are pairwise independent, including
pairs sharing one index. Consequently

\[
\mathbb EL=\mu,\qquad
\operatorname{Var}L=\mu(1-1/N),\qquad
\mathbb EK_3=\binom n3/N^2.
\tag{1}
\]

Let \(m_2\) be the number of blocks of size two, and \(V_3\) the number
of positions in blocks of size at least three. Elementary binomial
inequalities give

\[
L-m_2\le3K_3,\qquad V_3\le3K_3.
\tag{2}
\]

## Coupling with thinned collisions

Give every unordered collision pair an independent fair coin.
Let \(B\) be the number of heads. Thus \(B\mid x\sim\operatorname{Bin}(L,1/2)\).
Use its coin to decide whether each block of size two is transposed.
Choose permutations on larger blocks independently. This constructs
exactly the required conditional law of \(h\).

Let \(T_2\) be the number of performed size-two transpositions. Then

\[
0\le B-T_2\le L-m_2,\quad
\mathbb E(2B)=\mu,\quad
\operatorname{Var}(2B)=2\mu-\mu/N.
\tag{3}
\]

Write \(M_i=\mathbf1_{h(i)\ne i}\), with indices cyclically interpreted, and

\[
W=\sum_i(M_iM_{i+1}+M_iM_{i+2}).
\]

For distinct positions \(i,j\), reciprocal images need only one label
equality and have probability at most \(1/N\). Every other pair of
nontrivial images implies two independent label equalities. Summing
at most \(n^2\) image choices gives

\[
\mathbb P(M_i=M_j=1)\le N^{-1}+n^2N^{-2},
\qquad
\mathbb EW\le2n/N+2n^3/N^2.
\tag{4}
\]

## A local rank calculation and a perturbation estimate

Keep only those size-two transpositions both of whose moved positions
are at cyclic distance at least three from every other moved position.
Fix all other positions. Call the resulting permutation \(h_g\), and
let \(T_g\) be its number of transpositions.

Every discarded size-two transposition touches a conflict in \(W\).
There are at most \(2W\) incident moved positions, hence at most \(2W\)
discarded transpositions and at most \(4W\) discarded size-two positions.
At most \(V_3\) additional positions come from larger blocks.

For an isolated transposition \(a,b\), put
\(e=e_a-e_b\) and \(v=C e\). Their supports are disjoint because both
moved centers are separated by at least three from all moved centers.
The affected adjacency difference is

\[
C-P_{(a\,b)}CP_{(a\,b)}^T=e v^T+v e^T.
\]

The vectors \(e,v\) are nonzero and linearly independent over every
field, so this matrix has rank two. Neighborhoods of different
retained transpositions are disjoint. Hence

\[
R_g=2T_g.
\]

If two permutation matrices differ on at most \(m\) positions, their
difference has rank at most \(m\). Expanding the difference of their
conjugated adjacency matrices therefore gives

\[
|R-R_g|\le2(V_3+4W).
\]

Furthermore \(B-T_g\le3K_3+2W\), by (2).
These facts prove the entirely deterministic coupling inequality

\[
\boxed{|R-2B|\le12K_3+12W.}
\tag{5}
\]

In particular \(R=2B\) on the event \(K_3=W=0\).
Taking expectations gives

\[
\mathbb E|R-2B|
\le24n/N+26n^3/N^2,\qquad
\mathbb E|R-\mu|
\le\sqrt{2\mu}+24n/N+26n^3/N^2.
\tag{6}
\]

## Poisson approximation and a birthday limit

Use total variation \(d_{\rm TV}=\sup_A|\mathbb P(X\in A)-\mathbb P(Y\in A)|\).
For collision indicators, a dependency neighborhood consists of the pairs
sharing an index, including the pair itself. The Chen–Stein quantities are

\[
b_1=\binom n2(2n-3)/N^2,\qquad
b_2=\binom n2(2n-4)/N^2,\qquad b_3=0.
\]

Arratia–Goldstein–Gordon, *Annals of Probability* 17 (1989), Theorem 1,
bounds the total-variation norm they use by twice ours.
Its \(b_3=0\) consequence gives

\[
d_{\rm TV}(L,\operatorname{Pois}(\mu))
\le(b_1+b_2)/\mu=(4n-7)/N\le4n/N.
\tag{7}
\]

No extra factor \(1-e^{-\mu}\) is needed or asserted for this
total-variation comparison.

Binomial thinning contracts total variation. By (1) and (4),

\[
\mathbb P(K_3+W>0)
\le2n/N+\frac{13n^3}{6N^2}.
\]

Together with (5) and (7), this proves

\[
\boxed{
d_{\rm TV}\!\left(R,\,2\operatorname{Pois}(\mu/2)\right)
\le\min\left(1,\frac{6n}{N}+\frac{13n^3}{6N^2}\right).
}
\tag{8}
\]

Thus when \(n/\sqrt N\to s\),

\[
R\ \Longrightarrow\ 2\operatorname{Pois}(s^2/4).
\tag{9}
\]

Equation (8) is informative throughout \(n=o(N^{2/3})\).

## A law of large numbers and a wider central limit theorem

Equation (6) directly gives

\[
\frac{NR}{n^2}\longrightarrow\frac12
\quad\hbox{in }L^1,\qquad \sqrt N\ll n\ll N.
\tag{10}
\]

For \(\sqrt N\ll n\ll N^{3/4}\), the mean coupling error in (6),
divided by \(\sqrt{2\mu}\), tends to zero:
it is \(O(N^{-1/2}+n^2N^{-3/2})\).
The thinning comparison in (7) tends to zero, and the usual Poisson
central limit theorem applies because \(\mu\to\infty\).
Therefore

\[
\boxed{\frac{R-\mu}{\sqrt{2\mu}}
\ \Longrightarrow\ \mathcal N(0,1),
\qquad \sqrt N\ll n\ll N^{3/4}.}
\tag{11}
\]

This distributional convergence does not by itself establish
\(\operatorname{Var}R\sim2\mu\).

The previously recovered one-sided mean bound also has a short direct
proof: \(R\le2(n-C(h))\), and conditionally
\(\mathbb E C(h)=\sum_v H_{m_v}\).
Since \(m-H_m\le m(m-1)/4\), one obtains \(\mathbb ER\le\mu\).
The stronger lower-error constants from the preceding unsaved argument
are not needed for (9)–(11).

## Transfer to the positive physical diagonal in the Fourier model

For the symmetric Fourier scattering model, let \(\mathcal D_n x\)
be the dihedral orbit of a word. The positive word-diagonal rank measure is

\[
D(E)=\mathbb E_x\!\left[|\mathcal D_nx|\,
       \mathbb P_h(R\in E\mid x)\right].
\]

The earlier word-symmetry count proves

\[
0\le1-\frac{D(\text{all})}{2n}
\le(2n-1)N^{1-n/2}=:\varepsilon_{n,N}.
\]

Its proof is in the preserved orbit_reorganization.md.
Since \(0\le|\mathcal D_nx|/(2n)\le1\), the supremum over sets of the
difference between this weighted measure and the unweighted law is at
most \(\varepsilon_{n,N}\). Hence the birthday rank law transfers to
the positive physical diagonal:

\[
\frac{D(\{2j\})}{2n}\longrightarrow
e^{-s^2/4}\frac{(s^2/4)^j}{j!}.
\]

Exactly, \(D(\{0\})=2n\mathbb E[1/\prod_v m_v!]\):
the dihedral orbit size cancels its stabilizer size.
These positive contributions do not control the signed off-diagonal
interference or the full Fourier form factor at \(n\asymp N\).

## Another unsaved checkpoint: the proposed N^(1/7) correction window

The preceding session recorded an improvement from the saved
\(n=o(N^{1/9})\) result to

\[
M_n=2n-2n^2/N+O(n^7/N^2+n^{44}/N^7),
\qquad n=o(N^{1/7}).
\]

Its new load-bearing ingredients were: the number of deleted old-edge
paths is at most the original rank; support size at most \(3R+1\) per
connected component; fixed-rank cycle counting \(C'_R n^{R+1}\);
a rank tail split at R=14, with ratio
\(32\sqrt e\,n^{7/2}/\sqrt N\).
A counterexample to the tempting support bound \(2R\) was the twelve-cycle
permutation [0,7,2,9,4,11,6,1,8,3,10,5], of rank four.

The detailed new signed-graph proof and its run receipt did not survive the
offline runtime. This paragraph preserves the exact research checkpoint
and its dependencies; it is not included among this turn's fully restored
proofs or verified computation results. Reconstructing that graph proof
is a separate task. The new Jack/Pfaffian results do not depend on it.

## Primary probabilistic source

R. Arratia, L. Goldstein, L. Gordon, *Two Moments Suffice for Poisson
Approximations: The Chen–Stein Method*, Ann. Probab. 17(1), 9–25 (1989),
Theorem 1, including its factor-two convention.
https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/AGG-1.pdf

