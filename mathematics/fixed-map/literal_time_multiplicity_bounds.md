# Literal-time multiplicity bounds for N=7*5^e

Claim ID: BGS-FM-026. Independently reviewed project proof with the registered
Lindemann–Weierstrass theorem as an inherited external input.

For the unchanged actual A_N,M_N, let N=7*5^e, e>=1, and
U_N(t)=exp(itA_N)M_N. At every nonzero real algebraic t, including
literal t=10^-80 N:

- every eigenvalue has multiplicity at most 7;
- at least 612N/625+7 eigenvalues are simple for even e>=4;
- at least 612N/625+175 eigenvalues are simple for even e>=6;
- at N=4375, at least 4333 eigenvalues are simple;
- at N=109375, at least 107443 eigenvalues are simple;
- at least 24N/25 eigenvalues are simple for odd e>=3;
- at least 24N/25+35 eigenvalues are simple for odd e>=5;
- at least 24N/25+875 eigenvalues are simple for odd e>=7.

The even bounds sharpen the earlier 24N/25+7 count. They are additive counts
on disjoint complete unperturbed cat eigenspaces, followed by the already
accepted rank-transfer theorem. They do not identify the resulting fixed-time
U eigenvectors with oldform subspaces.

## Inherited theorem inputs

[Rank transfer](algebraic_time_rank_transfer.md),
[cat multiplicity](uniform_cat_multiplicity.md), the complete
[oldform tower](oldform_tower_compression.md), independently accepted
[even](even_oldform_second_jet.md) and [odd](odd_oldform_second_jet.md)
deepest-core splitting, and [newest-even-sector splitting](even_new_sector_first_jet.md)
retain their accepted scopes and source-bound reviews. The newest-sector
premise, conditional in the original rank-transfer source, was separately
accepted in the preceding packet. No cat-packet theorem is duplicated here.

## First-old quotient and the uniform count

The [first-old classifier](first_old_layer_classification.md) applies to
N=7*5^(2l+2), l>=1. Its quotient W1 orthogonal to W2 has dimension
24N/625 and consists of complete size-seven cat eigenspaces. The norm classes
c=2,4 modulo 5 account for exactly half of that quotient and give simple
first-order slopes uniformly in depth and wild character. Each such block
contributes all seven locally simple eigenvalue branches: rank six of its
slope matrix includes one simple zero slope and is not a count of six branches.
Thus these blocks contribute 12N/625 branches. The newest sector contributes
24N/25=600N/625, and the disjoint deepest even core contributes seven at order
two, giving 612N/625+7 for every even e>=4.

For c=1 modulo 5 the first-order compression is exactly zero. For c=3 it is
an exact cyclotomic scalar times a conjugate of the seven-point sine matrix;
the integer coefficient-balancing classifier decides zero versus simple
rank six at every depth and label. Nonempty intersection is insufficient:
at residual 625, c=13 has five intersections but six zero and 24 simple
blocks. The complete quotient there has 276 zero and 324 simple blocks.
This classification does not equate first-order zeros with U collisions.

## Residual 25 and the sharper even count

For every j>=2, the [residual-25 theorem](residual25_affine_dictionary.md)
proves simple second-order splitting of all 24 size-seven intermediate
blocks in W_j orthogonal to W_(j+1), at e=2j+2. Together with the prior
3,2,2 deepest blocks, all 175 dimensions of W_j split by order two.
For even e>=6, j=(e-2)/2>=2, so W_j is disjoint from W1 orthogonal to W2
and from the newest sector. The resulting count is 612N/625+175.

The [return-operator theorem](intermediate_return_operator.md) supplies the
matrix inverse with its character, initial factors, resonant projector and
k=0 subtraction. The failed deepest scalar normalization has negative
entry valuations on the inherited coherent lattice; its correction is an
affine orbit sum. The residual-25 theorem projects that sum using integral
circlewise six-cycle eigenbases, retaining all 17 actual upper-pair
coefficients and seven-factor cocycles. The nonprimitive j=2 residual cat
is retained; its normalized valuation is at least 49/25. The theorem does
not replace a ramified global projector by a unit denominator without proof.

At N=4375 (l=1), exactly 18 first-old blocks split at first order. Hence
4200 + 18*7 + 7 = 4333. At N=109375 (l=2), exactly 324 first-old blocks split,
and residual-25 splitting supplies the disjoint 175-dimensional old group.
Hence 105000 + 324*7 + 175 = 107443. These are lower bounds, not full simplicity.

## Odd newest sector and residual 125

The [odd newest-sector theorem](odd_newest_sector_first_jet.md) gives simple
first-order compression on every complete seven-dimensional cat group in
W1-perpendicular, accounting for 24N/25 branches for odd e>=3. Its five-fiber
holonomy, full 5L dual denominator, Gauss signs and all wild labels are retained.
The inherited deepest odd core contributes 35 disjoint branches for odd e>=5.

The [residual-125 theorem](residual125_uniform_splitting.md) splits all 120
new seven-dimensional groups in W_j minus W_(j+1), e=2j+3, j>=2, at second
order. Together with the deepest core, W_j contains 840+35=875 branches.
The [separately checked combination](odd_sector_count_combination.md) proves
W_j is contained in W1, so these complete groups are disjoint from the newest
sector. It gives 24N/25+875 for odd e>=7, counting the 35 only once. Existing
algebraic-time rank transfer applies to the resulting local branch count.

## Exact rank-transfer attribution and boundary

Within a complete cat block, distinct first nonconstant phase coefficients
give locally distinct branches. Different complete cat eigenvalues remain
separated near t=0. The disjoint groups above therefore witness the stated
rank lower bound for chi'_U(t)(U(t)) at sufficiently small nonzero real t.
The [existing algebraic-time rank theorem](algebraic_time_rank_transfer.md)
transfers that lower bound to every nonzero real algebraic t. Its sole
external coefficient-separation input remains the registered
Lindemann–Weierstrass dependency; no new external theorem is introduced.

The rank of chi'(U) counts simple eigenvalues. Higher derivative-stack ranks
count total dimensions of eigenspaces of multiplicity at most k; they are not
N minus a gcd degree. Only full-column-rank iff gcd 1 is used. The
[rank-transfer audit](../../record/cat_jet_rank_review.md) retains these distinctions
and the exact external coefficient-separation mapping.

The [finite first-order companion](finite_cat_first_jet.md) proves simple U
at N=35,175. N=35 remains an independent mechanism for the previously certified
FM-008 case; no duplicate claim is created. N=175 remains bounded. The two
finite general-return controls are not promoted into additional full-U cases.

No full uniform U simplicity, quantitative gap, full complex scalar U
commutant, higher trace estimate, plateau or BGS follows. Larger even
intermediate residuals (especially 625 and above) still require character
compression with 5-primary cycle denominators and possible phase cancellation.
Larger odd intermediate residuals beyond the accepted 125 case still require
their own compatible basis. The separate odd first-old follow-on is excluded. The shorter
all-depth digit rule for singular sums is optional and unproved; the separate
Cayley/Morse continuation is unchecked and not a dependency.

Finite [portable replays](../../computations/verification/intermediate_old_layers_certificates.py)
support the separately reviewed reductions. Their success is not empirical
extrapolation to arbitrary dimension or time.
