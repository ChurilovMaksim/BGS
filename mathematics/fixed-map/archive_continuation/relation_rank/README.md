# Multiplicative rank of a selected spectrum at powers of seven

**Registry:** BGS-TRACE-359.

Let $N=7^k$, $k\ge4$, and let $U_N(t)=\exp(itA_N)M_N$ be the
[unchanged model](../../fixed_model_symmetry_theorem.md).
For every nonzero real algebraic $t$, including $t=10^{-80}N$, there
are $R=180\cdot7^{k-4}$ simple eigenvalues $\lambda_1,\ldots,\lambda_R$
whose nontrivial integer monomials are all transcendental:
$$
\prod_{j=1}^R\lambda_j^{a_j}\notin\overline{\mathbb Q}
\quad\text{for }0\ne a\in\mathbb Z^R.
$$
Thus $R/N=180/2401$. This is an exact algebraic statement, not a
separation estimate. The [archived full proof](BGS_Phase_Rank.tex)
and its two prerequisite TeX sources are preserved as received.
See the [claim registry](../../../../record/claims.json) for maintained
statuses and the
[archive verification suite](../../../../computations/verification/bgs_f_november/)
for finite checks.

## Inputs and specialization

The [archived spectrum source](../earlier_routes/BGS_Spectrum.tex), §3, supplies the cat
dilation normal form, its square/nonsquare orbits at primitive conductors,
and the first-order compression. Only that normal form and those local
compressions are needed here, not its claims for other levels or other
dimensions. The [archived splitting-law source](../weak_kick/BGS_Split_Law.tex),
§§1–2, supplies the four stationary contributions in the chosen
character class, including their exact Gauss factors. No shrinking-kick
limit or transfer of that limit to fixed coupling is a premise.
The external inputs are Rellich's analytic eigenbranch theorem for an
analytic Hermitian matrix ([Theorem 2.1](https://www.mat.univie.ac.at/~armin/publ/handbook_paper.pdf),
applied to a local Hermitian logarithm with cut outside the spectrum)
and [Lindemann–Weierstrass, Theorem 3.2](https://arxiv.org/pdf/2306.14352v2).

Fix $t_*\ne0$ real algebraic. Entries and characteristic coefficients of
$U_N(t)$ are finite sums $a_\nu e^{itb_\nu}$ with $a_\nu,b_\nu$
algebraic, by spectral decomposition of the algebraic Hermitian $A_N$.
After collecting frequencies, any nonzero such sum is nonzero at
$t_*$. A simultaneous labeling is essential: there is one permutation of
the local analytic branches near $0$ on which **every** polynomial
relation over $\overline{\mathbb Q}$ of the ordered eigenvalues at $t_*$
holds identically. Otherwise, for each permutation choose one relation
whose analytic restriction is not identically zero. In the rational
span of these finitely many relations choose one polynomial outside the
finite union of their permutation-wise vanishing subspaces. The
product of this polynomial over all permuted variables is symmetric
and nonzero after analytic substitution near $0$. As a polynomial in
the characteristic coefficients it is a nonzero exponential polynomial,
yet vanishes at $t_*$. This contradicts coefficient separation.

For selected branches $z_j(t)$ put $d_j=z_j'(0)/(iz_j(0))$.
If $\prod_j\lambda_j^{a_j}$ were algebraic, clearing negative powers
would give a polynomial relation of the labeled eigenvalues at $t_*$.
Logarithmic differentiation along the simultaneous branches gives
$\sum_j a_j d_j=0$. Rational independence of the $d_j$ therefore
suffices. When a selected branch is simple for small nonzero $t$ it
must remain simple at $t_*$, since equality to another branch would
be another polynomial relation.

## Rational independence of the stationary derivatives

Take $\rho^2=2$, $\rho\equiv3\bmod7$, and use Weyl coordinates
$(a,b)=(v_1+\rho v_2,(v_1-\rho v_2)/(-2\rho))$.
There are two unit orbits under dilation by $(3+2\rho)^{-1}$,
each of length $m=3\cdot7^{k-1}$.
At the primitive cat nodes $\ell\equiv3\bmod7$, indexed also by
$h\bmod3$, the two eigenbranches have derivatives from the diagonal
compression of $A_N$. In the square orbit the only stationary
Weyl labels are the opposite pairs of
$(0,1),(0,8),(0,-6),(0,7)$. Write the associated coefficients as
$c=(200-20i,-100+10i,-100+10i,1800)/4000$.
The first three pairs are primitive; for the fourth both transformed
coordinates are divisible by $7$. With
$\mathcal L(x)=\log(x^6)/6$, each stationary contribution is given by
$$
\Phi_i(\ell)=b_i(x_i+a_i/2)+
          \ell\mathcal L((x_i+a_i)/x_i),
\qquad
b_i x_i(x_i+a_i)=\ell a_i .
$$
Use the simple square-orbit root after dividing by $7$ for the
fourth label. The four contributions to $m d_{\pm,\ell,h}$ are
$c_i^\pm G_i\zeta_3^{h\mathbf 1_{i<4}}\zeta_N^{\Phi_i(\ell)}$
and their conjugates, where $c_i^+=c_i$, $c_i^-=\overline c_i$, and
the nonzero $G_i\in\mathbb Q(\zeta_7)$ depend on $i,k$ but not on
$\ell,h$ in this class. Simplicity in this cluster follows from the
nonzero difference in the $(0,1)$ coordinate described below.

Put $B=7^{k-2}$, $D=7^{k-1}$. Over
$\mathbb Q(i,\zeta_3,\zeta_7)$ the powers $1,\zeta_N,\ldots,\zeta_N^{D-1}$
form a basis. The positive phase residues modulo $49$ are $10,3,17,14$,
distinct from one another and from the four negative residues. Select
representatives $0\le r<B$ in the six classes $3,10,17,24,38,45\bmod49$,
and keep the six lifts $\ell=r+uB$, $0\le u\le5$.
Taylor expansion using stationarity gives
$$
\Phi_i(r+uB)=\Phi_i(r)+uB\Phi_i'(r)\pmod{7^k},
\qquad
\Phi_i'(r)=\mathcal L((x_i+a_i)/x_i).
$$
If $\Phi_i'/7$ is a unit, the six lifts at each representative are
independent over $\mathbb Q(i,\zeta_3)$ as distinct powers of $\zeta_7$.
On each selected residue class modulo $49$ where that unit condition
holds, two distinct representatives give different coordinates modulo
$D$: the valuation of their phase difference is that of $r-r'$ plus
one. The fourth label has that property across all selected classes,
and the first three separate classes by residues modulo $343$.

Omit one derivative, the $(-,2)$ branch, for each selected $\ell$.
In an alleged rational dependence put its deleted coefficient equal
to zero. Extracting the fourth label gives
$\sum_{h,\pm}n_{\ell,h,\pm}=0$ for each $\ell$.
The phase table from §4 of the [proof](BGS_Phase_Rank.tex) then
allows elimination of the classes in order by using one primitive
coordinate for each:
$(17,2),(45,3),(10,3),(3,1),(38,2),(24,1)$, with pairs
$(r\bmod49,\text{label index})$.
The selected coordinate at each step has unique residue among the
remaining classes and $\Phi_i'/7$ a unit. Each resulting equation is
$$
\sum_{h=0}^2\zeta_3^h
     (c_i n_{\ell,h,+}+\overline c_i n_{\ell,h,-})=0.
$$
The only dependence of the three powers of $\zeta_3$ over $\mathbb Q(i)$
is their sum. Since $c_i,\overline c_i$ are independent over $\mathbb Q$,
both rational coefficient lists are constant in $h$. The deleted branch
sets one constant to zero and the fourth-label equation sets the other
to zero. This proves independence of $6\cdot7^{k-4}\cdot6\cdot5$ derivatives.
In particular the positive branch at $h=2$ is also distinct from its
deleted partner: their difference has a nonzero contribution in the
coordinate $10\bmod49$. All selected branches are simple for small
nonzero $t$, so specialization applies.

## Consequences and novelty boundary

The selected eigenvalues produce at least $R(R-1)+1$ distinct ratios
in the full spectrum, including the identity. At fixed $N$, their
powers are equidistributed on the $R$-torus as the time-window length
$T$ tends to infinity, uniformly in the initial time at fixed $N$.
Any fixed nonzero integer stepping is allowed. The geometrical-series
argument has no useful uniform rate here: it depends on denominators
$|1-\prod_j\lambda_j^{a_j}|$. Taking first $T\to\infty$ and only then
$k\to\infty$, the normalized trace of the selected spectral projector
has a standard complex Gaussian limit. At fixed $N$ the corresponding
upper time density of $|\operatorname{Tr}U_N^m|\ge N-R/2$ is at most
$4e^{-R/16}$, by a two-coordinate exponential tail estimate for the
selected Haar phases and the triangle inequality for the others.

Prior [transcendence of ratios](../../../spectral_research/proofs/research_round2_2026_10_20/arithmetic_transcendental_eigenvalue_ratios.md)
already rules out algebraic ratios for $7\nmid N$; prior
[exact nonrecurrence](../../../spectral_research/proofs/research_round2_2026_10_20/root_all_time_algebraic_nonrecurrence.md)
rules out algebraic matrix-line returns for every odd $N\ne7$.
The [algebraic-time rank-transfer theorem](../../algebraic_time_rank_transfer.md)
already transfers simple-eigenvalue counts, with different local inputs.
The contribution here is the rational-rank construction of a
positive-density **selected** set in the tower $7^k$ and its simultaneous
specialization for arbitrary monomials, not a new generic
nonrecurrence principle. Finite arithmetic checks cover the stationary
table and exact direct ranks modulo $101$ at $k=4,5,6$
($180,1260,8820$); the rational-rank argument is needed for the whole
tower. None of this bounds near-resonances on time scale $m\asymp N$,
proves the signed pair limit, or decides weak convergence to Sine₂.
