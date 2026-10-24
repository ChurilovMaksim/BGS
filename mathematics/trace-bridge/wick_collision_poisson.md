# Heisenberg-scale Wick collisions and the flat equal-edge ratio

**Claim ID:** `BGS-TRACE-094`. 16 October 2026.

**Status:** project proof, adversarial author review and one independent internal
reconstruction of Sections 1--5. Base: `f78ec82ffe8c6535c961abc969a719704bf3e942`.
This continuation uses the exact definitions and Gaussian Fock convention of
[TRACE-093](gaussian_equal_edge.md). It concerns the positive flat
equal-edge sector, not the signed trace of the physical propagator.

Write `p_m(Y)=Tr Y^m`, `h_m=E|p_m|^2`, and let `W(nu)=c(nu)^2 prod nu!/h_m`.
Put `C=sum_e binom(nu_e,2)` and `D=#{e:nu_e>=2}`. All sums use directed edges,
including loops. Fix `0<a<b<infinity` and restrict `aN<=m<=bN`.

## Theorem

For every fixed positive integer r, uniformly on the stated compact m/N range,

    E_W (D)_r = [2(m/N)^2]^r + O_(a,b,r)(N^-1),
    Pr_W(max_e nu_e>=3)=O_(a,b)(N^-1).

Consequently, for `m/N->alpha>0`,

    C => Poisson(2alpha^2),       B_(N,m)/G_(N,m) -> exp(-alpha^2).

In particular `m=o(N)` is the precise vanishing-deficit side of the critical
scale among sequences for which m/N has a finite limit. This is a collision
law of a positive auxiliary measure; it is not a Poisson law of quantum energy
levels. No global priority or external referee certification is claimed.

## 1. Bounded trace-product overlaps

For a partition rho of m into ell positive parts, the hook character formula is

    sum_(j=0)^(m-1) (-t)^j chi_(m-j,1^j)(rho)
      = prod_(v in rho)(1-t^v)/(1-t).

It follows that every character on the left has absolute value at most 2^ell:
expand the numerator and then `1/(1-t)`. Schur orthogonality in TRACE-093,
and the hook expansion of p_m, therefore give

    0 <= <p_m, prod_(v in rho) p_v> <= 2^ell h_m.            (1)

The lower bound also follows directly from nonnegative monomial coefficients.
Here is an elementary symmetric-function derivation fixing the coefficient
convention. Use the Hall product with `p_rho` orthogonal of squared norm
`z_rho=prod_l l^(m_l) m_l!`; the Cauchy identity makes Schur functions
orthonormal in this product. This auxiliary product is distinct from the
Gaussian Fock product used elsewhere. The hook generating identity already
proved in TRACE-093 is

    F(z,u)=sum_(m>=1) sum_(j=0)^(m-1) s_(m-j,1^j) z^m u^j
          =[H(z)E(uz)-1]/(1+u).

Also `H(z)E(uz)=exp(sum_(v>=1) p_v z^v[1-(-u)^v]/v)`.
Taking its Hall product with p_rho shows that the coefficient of `s_(m-j,1^j)`
in p_rho is the coefficient of u^j in
`prod_(v in rho)[1-(-u)^v]/(1+u)`. Put u=-t to obtain the displayed hook
formula. Finite-N specialization simply discards hooks of length greater than
N; it does not change the coefficients of the remaining hooks. Their Gaussian
squared norms are `w_(m,j)=(N+m-j-1)!/(N-j-1)!`, and `h_m=sum_j w_(m,j)`.
Thus the bound uses established finite symmetric-function algebra, not an
asymptotic character estimate.

## 2. Every partial contraction of a fixed derivative order is bounded

Let `H^(k)_(a_1 b_1,...,a_k b_k)=partial_(a_1 b_1)...partial_(a_k b_k) p_m`.
For any partial bijection P from a subset of `{1,...,k}` to another subset,
identify and sum `a_i=b_(P(i))` for its matched slots. Denote the resulting
tensor by `C_P H^(k)`; its squared norm includes Gaussian expectation and
the sums over all remaining indices. The key bound is

    ||C_P H^(k)||^2 <= C_k m(N+m)^(k-1) h_m,
    ||C_P H^(k)||^2 <= C_(a,b,k) (m)_k h_m.                (2)

Only sufficiently large N (hence m>k) is needed. Here the empty P gives
`||H^(k)||^2=(m)_k h_m` exactly.

To prove (2), use the marked trace identity

    H^(k) = m sum_(cyclic orders sigma with sigma(1)=1)
               sum_(r_1+...+r_k=m-k, r_i>=0)
               prod_i (Y^(r_i))_(b_(sigma(i)),a_(sigma(i+1))).

There are `(k-1)!` cyclic orders. Move the contracted derivatives in the first
factor of the squared norm onto multiplication by their coordinate variables;
all k derivatives are moved, including those with remaining free indices.
The resulting polynomial is a sum of products of traces, all with coefficient
m and with total degree m. This assertion has an explicit graph construction:
use one copy of each creation edge `a_i' -> b_i'` of length 1 and each marked
trace segment `b_(sigma(i)) -> a_(sigma(i+1))` of length r_i. Internal matches
P join their endpoints within each copy; each unmatched endpoint is joined to
its counterpart in the other copy. Every component is a directed cycle.
Its length L gives p_L; a zero-length cycle gives p_0=N.

A zero-length cycle must contain at least one marked segment and no creation
edge. Different such cycles use disjoint segments. Thus their number z is at
most the number q of zero r_i. There are at most 2k positive-length cycles.
For `m-k>0`, q<=k-1 and the number of compositions with q zeros is

    binom(k,q) binom(m-k-1,k-q-1).

By (1), each product contributes at most `2^(2k) N^q h_m` to its inner product
with p_m. Summing compositions gives a bound by

    2^(2k) m(k-1)! sum_(q=0)^(k-1)
          binom(k,q) N^q m^(k-q-1) h_m
      <= C_k m(N+m)^(k-1)h_m.

This proves the first estimate. On the compact m/N range its ratio to
`(m)_k h_m` is bounded, proving the second. In particular the graph argument
does not use an independent-word approximation or omit reversed edges.

## 3. Fixed coordinate derivatives and their disjoint-label leading term

Let `E_k=(m)_k h_m`. Unitary conjugation preserves p_m and the Gaussian law.
The balanced Haar moment of order 2k is the classical inverse Gram formula on S_(2k),
whose Gram matrix entries are `N^(#cycles(sigma^-1 tau))`. For fixed k,

    Wg_N(sigma,tau)=N^(-2k)[1_(sigma=tau)+O_k(N^-1)].       (3)

This follows by dividing the Gram matrix by N^(2k) and inverting `I+O_k(1/N)`.
For large N the permutation tensors are independent; no growing-order Haar
limit is used. Precisely, the row sum of the off-diagonal normalized Gram
entries is at most `((2k)!-1)/N`, so a Neumann inverse supplies a uniform
entrywise remainder once N is sufficiently large depending on k.
The exact Haar identity is Collins--Sniady, arXiv:math-ph/0402073v1,
Corollary 2.4, equation (11), with their degree n=2k and dimension d=N.
The [source check](../../literature/wick_poisson_sources_20261016.md) records its
normalization and bounded applicability.

For completeness the input/output dictionary is explicit. Write two input
copies as H_(A,B) and its conjugate H_(C,D), and prescribe output labels I,J.
Conjugation by `conjugate(U)` gives factors
`prod_l U_(i_l A_l) conjugate(U_(j_l B_l))`. The squared expression therefore
has the following lists in its Haar integral:

| List | U factors | conjugate(U) factors |
|---|---|---|
| output indices | (I,J) | (J,I) |
| input indices | (A,D) | (B,C) |

An input permutation tau imposes `(A,D)_l=(B,C)_(tau(l))` for each l.
Links inside the first copy identify an upper A with a lower B; links inside
the second identify an upper C with a lower D. The remaining links identify
free upper indices across the copies and free lower indices across the copies.
Thus the summed input expression is the inner product of two partial
contractions C_P H, C_Q H, with a permutation of their free indices. No
uncontrolled sums of N factors are introduced in this interpretation.

Every input contraction in this Haar formula is an inner product of two
partial contractions from (2), possibly followed by permutations of free
indices. Cauchy--Schwarz bounds its magnitude by `C_(a,b,k) E_k`. Consequently,
uniformly over all choices of coordinate edges e_1,...,e_k, with repetitions,

    ||partial_(e_1)...partial_(e_k) p_m||^2/h_m
        <= C_(a,b,k) N^(-k).                              (4)

For a sharper asymptotic suppose the sets of prescribed upper and lower labels
are disjoint. The output Kronecker constraints in the Haar formula then permit
only fully cross pairings. If label a occurs A_a times among the upper indices,
and label b occurs B_b times among the lower indices, their number is
`prod_a A_a! prod_b B_b!`. The leading input contractions permute upper indices
relative to lower indices. They equal `E_k[1+O_(a,b,k)(N^-1)]`:

For one upper transposition, TRACE-093 and Fock homogeneity give exactly

    K_k=(m-2)_(k-2) K_2,
    <H^(k), R H^(k)> / E_k = 1-2 jbar/(m-1),
    jbar <= (N-1)/m.

Any fixed permutation is a bounded product of transpositions. The triangle
inequality for the tensor norm, followed by squaring, bounds its relative
overlap defect by `O_k(jbar/(m-1))=O_(a,b,k)(N^-1)`. All overlaps are real
because the tensor polynomials have real coefficients. Inserting into (3) gives

    ||partial_(e_1)...partial_(e_k) p_m||^2/h_m
      = [(m)_k/N^(2k)] [prod_a A_a! prod_b B_b!+O_(a,b,k)(N^-1)]. (5)

For the identity for K_k, apply k-2 identical, summed coordinate derivatives
to the two Hessian polynomials. Their degree is m-2, so mixed Fock homogeneity
multiplies their inner product by `(m-2)_(k-2)`. Pair-slot symmetry treats every
upper transposition alike. If a permutation uses L transpositions, the explicit
overlap defect is at most `2L^2 jbar/(m-1)`. At k=1 there is no nontrivial
upper permutation and this step is unnecessary.

## 4. Factorial moments, including endpoint coincidences

Gaussian coefficient norms give the exact identity, for distinct e_i,

    E_W prod_i (nu_(e_i))_(k_i)
      = ||prod_i partial_(e_i)^(k_i) p_m||^2/h_m.          (6)

For ordered r-tuples of directed edges with all 2r endpoints different, apply
(5) with k=2r, two copies of each edge. The multiplicity factor is `4^r`.
There are `(N)_(2r)` such edge tuples. Dividing (6) by `2^r` gives

    E_W sum_(e_1,...,e_r distinct) prod_i binom(nu_(e_i),2)
      = [2(m/N)^2]^r + O_(a,b,r)(N^-1).                  (7)

Indeed the remaining tuples are only `O_r(N^(2r-1))` in number, and each is
bounded by `C N^(-2r)` using (4). This includes loops, reversed edges and
shared incoming/outgoing vertices.

To replace binomial counts by indicators, put b_i=binom(nu_(e_i),2). For all
nonnegative integer counts,

    0 <= prod_i b_i - prod_i 1_(nu_(e_i)>=2)
       <= sum_i [((nu_(e_i))_3)/2] prod_(j!=i) b_j.

After summation, every term on the right has derivative order 2r+1 and at most
N^(2r) choices of edge labels. Bound (4) makes its expectation O_(a,b,r)(1/N).
Thus (7) proves the displayed factorial moments of D. Also (4) at k=3 gives

    Pr(max_e nu_e>=3) <= sum_e E(nu_e)_3/6 = O_(a,b)(1/N). (8)

## 5. Distribution and the equal-edge ratio

For each q in [0,1], the finite Bonferroni bounds for `(1-q)^D` and the
factorial moments just proved imply

    E_W(1-q)^D -> exp(-2alpha^2 q).

For clarity take the limit N first with the truncation order fixed, and only
then send that order to infinity in the convergent exponential series.
Equivalently thin each of the D objects with probability q and apply the
ordinary inclusion--exclusion bounds to the probability of no retained object.
These probability generating functions determine the Poisson limit. By (8),
C=D with probability tending to one, so C has the same limit.

On that same event `prod nu_e!=2^C`; both reciprocals are in [0,1]. Therefore

    |B/G-E_W 2^(-C)| <= Pr(max_e nu_e>=3)=O(1/N),
    B/G -> exp(-alpha^2).

This closes the flat Heisenberg ratio left open by TRACE-093. It supplies
no signed physical trace estimate, no non-flat extension and no BGS theorem.

## 6. Collision locations and geometric vertex occupations

The same proof gives a spatial form of the law. Let `A_(N,1),...,A_(N,l)` be
disjoint deterministic subsets of directed edges with
`|A_(N,j)|/N^2 -> beta_j`. Then

    ( #{e in A_(N,j):nu_e>=2} )_(j=1)^l
       => independent Poisson(2alpha^2 beta_j) variables.    (9)

Indeed mixed factorial sums have the same leading multiplicity `4^r`, with
`prod_j |A_(N,j)|^(r_j)+O_r(N^(2r-1))` good tuples. Bounds (4) and the
indicator replacement apply unchanged. Mixed Bonferroni bounds follow by
thinning each class with its own probability. Equivalently the random measure
`sum_e 1_(nu_e>=2) delta_(a/N,b/N)` converges to a Poisson random measure of
intensity `2alpha^2 dx dy` on the unit square, by rectangle partitions and
tightness of the total mass. This does not describe eigenvalue locations.

There is a different, useful local occupation law. Put `n_a=sum_b nu_ab`.
The cyclic word ensures `sum_b nu_ab=sum_b nu_ba` exactly. For any fixed distinct
vertices a_1,...,a_l and fixed nonnegative k_i, with K=sum_i k_i,

    E_W prod_i (n_(a_i))_(k_i)
      = prod_i k_i! (m/N)^K + O_(a,b,K,l)(N^-1).           (10)

To prove it, expand each row falling factorial as an ordered sum of coordinate
derivatives. Except for `O_(K,l)(N^(K-1))` choices, the K lower labels are all
different and outside the l fixed upper labels. Their number is `(N-l)_K`.
Formula (5) has upper multiplicity `prod_i k_i!` and lower multiplicity one.
Formula (4) disposes of every remaining choice. This proves (10), including
the K=0 identity separately.

Consequently the finitely many n_(a_i) converge jointly to independent geometric
variables on `{0,1,...}` with mean alpha and probabilities

    Pr(n=j) = alpha^j/(1+alpha)^(j+1).                    (11)

Their factorial moments are `k! alpha^k`. These moments determine the joint
law: the sum of the limiting geometric variables has an exponential moment
near zero. Tightness and the next higher moment give subsequential moment
convergence and uniform integrability at each fixed order; the resulting
analytic moment generating function identifies every subsequential law.
In/out occupations at the SAME vertex are equal, not independent.

Permutation symmetry of W and the two-vertex version imply the empirical
occupation law: for every bounded function f on the nonnegative integers,

    N^-1 sum_a f(n_a) -> E f(Geom(alpha)) in probability.   (12)

Its expectation converges by the one-vertex law and its variance vanishes by
the two-vertex law and exchangeability. Thus a Poisson vertex-occupation
approximation is incorrect for this Wick-biased one-circuit measure.

## 7. A non-Gaussian high-power trace corollary

Let xi have a rotation-invariant complex law, `E|xi|^2=1`, and
`E|xi|^(2j)<=j!` for every j>=1. Let Z have independent entries xi/sqrt(N),
and put kappa=E|xi|^4, so `1<=kappa<=2`. Then at m/N->alpha>0,

    E|Tr Z^m|^2 / E|Tr X^m|^2
         -> exp[(kappa-2)alpha^2],                        (13)

where X is the variance-1/N complex Ginibre matrix. Independence and rotation
invariance give the exact ratio `E_W prod_e q_(nu_e)` with
`q_j=E|xi|^(2j)/j!`. All factors lie in [0,1], and q_0=q_1=1.
On the event of no triple edge the product is `(kappa/2)^C`. Its boundedness
and (8) permit replacement by that expression with error O(1/N).
The Poisson limit proves (13). In particular a uniform unit-modulus xi recovers
the flat B/G limit. No claim for fourth moments greater than two follows from
this bounded argument; exponential uniform integrability would be needed.

## Relation to BGS and review boundary

The complete positive Heisenberg comparison is now explicit. The unitary
signed complement must still cancel an exponentially large quantity to leave
the required polynomial spectral statistic. Neither the Haar integral used
as a proof device for the auxiliary Gaussian derivatives nor the iid entry
corollary replaces the maintained deterministic propagator by a random model.
The physical intensity profile is non-flat. TRACE-005 and BGS-BGS-001 remain
OPEN, with their original quantifiers and symmetry qualifications.

Sections 1--5 have an independent internal reconstruction. Sections 6--7 are
author-derived corollaries, separately checked here; no external referee review
or analytic Lean certification is asserted. The exact finite checks compare
different representations and audit indices; they are not the proof of any
asymptotic statement.

[Internal review](../../archive/record/reviews/wick_poisson_20261016.md),
[execution provenance](../../evidence/executions/20261016/wick-poisson/README.md),
and [classical-source/priority boundary](../../literature/wick_poisson_sources_20261016.md).

