# Actual kick simplicity for N=7*5^e

Claim ID: BGS-FM-025.

Status: exact project proof with independent internal v2 audit. Scope is simplicity of the actual A_N for every e>=1. No claim about U_N simplicity, seven-divisible N outside this family, or BGS. This v2 repairs the two-index weighted invariant and coefficientwise analytic domains missing from v1. It extends the reviewed N175 calculation; the only finite algebraic input is the seven degree-five residue blocks and their certified nonzero offset derivatives.

## 1. Analytic translated model and fixed residue species

Use the real-Jacobi gauge and normalized matrix T=(200A_real-180I)/eta from the independently reviewed bounded input retained at ../record/history/2026/spectral_extension_20261006/cluster_source.md. Put Q=q^7, pi=Q-1, and v_pi(pi)=1. Then v_pi(5)=4*5^(e-1). Write

    d_s=5^(s+1)-1  (s>=0).

For an integer u not divisible by5^e,

    v_pi([u]_Q)=5^(v5(u))-1,
    [u]_Q=(Q^u-1)/(Q-1).

For u divisible by5^e, [u]_Q=0. In particular, at the cut between consecutive length-five blocks, u=5l, the bond of T has valuation 2d_(v5(l)), or is zero at an actual boundary.

Introduce an analytic translation parameter y through

    Q^x -> Q^x(1+pi y),
    q^x -> q^x(1+pi y)^(1/7),
    [x]_Q -> [x]_Q+Q^x y.

The seventh root is the branch congruent to1. It has integral power-series coefficients because seven is a unit. All normalized matrix coefficients are integral power series in y. The fixed eta and [h]_Q normalization are not translated. The actual matrix is y=0.

At an integer shift delta divisible by35, let y_delta=[delta]_Q. The analytic translation agrees exactly with shifting every position by delta, since q^delta is congruent to1 and is the specified seventh root of Q^delta. Translation parameters compose by

    y op z=y+z+pi yz.

The cyclic position model therefore gives exact covariance under shifts by35. This remains true when some original bonds are zero; their analytic translates are retained as coefficients.

At y in pi^4 O the same seven length-five residue blocks occur. Their combined35 eigenvalues are distinct by the accepted bounded gcd certificates. Enlarge the unramified coefficient field to split them. Each actual length-five diagonal block has a unit eigenvector matrix and simple analytic eigenvalues: the characteristic derivative is a unit, and the first coordinate recurrence has unit internal bonds. These bases and their inverses are integral analytic functions of y.

Fix one of the35 residue eigenvalues. It occurs at P=5^(e-1) sites, one in every seventh length-five block. Label these sites k modulo P. Their parameters are

    y_k=[35k]_Q,
    v_pi(y_k-y_l)=d_(v5(k-l)) for k!=l modulo P.

The bounded offset certificate says that the corresponding local eigenvalue function has unit derivative in y. Its power series is integral. Consequently its values at different sites differ by (y_k-y_l) times a unit.

## 2. First Schur reduction, with spatial weights retained

For spectral z in the residue disc of the fixed species, eliminate the other34 species. Their diagonal eigenvalues differ from z by units. After the unit block eigenbasis changes, the only couplings between length-five blocks are the original cut bonds. Expanding the complementary inverse gives convergent walks in this one-dimensional cyclic block graph.

On the parameter ball y in pi^(d_r) O, a cut at u=5l has analytic coefficient valuation at least

    2 min(d_(v5(l)),d_r),                             (1)

with the zero-boundary case interpreted by the same bound. Indeed [u]_Q+Q^u y has valuation at least the minimum of the two displayed valuations; every other bond factor is a unit.

After the first Schur reduction, the fixed-species effective matrix has a scalar diagonal equation at each site plus off-diagonal walk sums. The first diagonal self-energy is divisible by pi^16, since a nontrivial return uses at least two cut bonds, each divisible by pi^8. On the y-ball pi^4, its Lipschitz constant in y is divisible by pi^12. Its z-derivative is also topologically small. The scalar diagonal equation therefore has an analytic root rho(y), and rho differs from the local eigenvalue by a strictly contracting Lipschitz function. In particular

    rho(y)-rho(y')=(y-y') times a unit.               (2)

Dividing the diagonal equation by its analytic unit factor puts it in the form rho(y_k)-z. This preserves all off-diagonal valuation bounds. The same operation will be used at every later stage. Covariance gives the same scalar function at translated sites.

At the initial level, an off-diagonal connection between fixed-species sites at cyclic distance a crosses at least7a cut bonds, so its valuation is at least56a on the pi^4 parameter ball. Keeping only this unweighted bound forever would fail; it discards the higher valuations of every fifth, twenty-fifth, and subsequent cut.

## 3. Coefficientwise two-index invariant and weighted Schur elimination

All bounds in this section are Gauss valuations of coefficients, not pointwise divisibility. Let O be the complete discrete valuation ring after the fixed unramified splitting extension. Write O< u,w > for its convergent restricted power-series algebra with its coefficientwise Gauss valuation. The root and matrix functions below lie in this algebra after the indicated substitutions; ordinary formal power series with integral coefficients converge because every unscaled argument is divisible by pi.

After fixing s digits, the surviving sites form S_s={k:k=c modulo5^s}. The diagonal equations have analytic roots rho_(s,k)(y) on the BROAD level-s parameter ball y in pi^(d_s)O, with unit divided differences. Covariance is established on this broad ball first: shifts by35*5^s m have parameters of valuation at least d_s and preserve it. For R>s, use a local chart relative to a chosen reference site c. Its origin is translated to c before imposing the smaller ball; raw edge indices are correspondingly shifted. Root functions at other S_s sites are evaluated by translation inside the broad ball and then restricted to this chart. No claim is made that a translation of valuation d_s preserves the narrower R-ball. The weighted counting is uniform in this shifted raw origin. For EVERY R>=s retain a separate weighted representation on

    y=pi^(d_R)u,
    z=rho_(s,c)(y)+pi^(d_s+1)w.                     (3a)

The bounds are uniform in the choice of center c in S_s. For sites removed at an earlier level j<s, the corresponding spectral denominator is pi^(d_j) times an analytic unit on(3a). Its constant term after division is nonzero, while both the parameter movement and the current spectral disc are strictly smaller than that earlier gap. Row normalizations of the scalar diagonal factors are analytic units and do not affect weights.

The raw cut at u=5l is divisible, COEFFICIENTWISE after y=pi^(d_R)u, by pi to the power

    b_R(l)=2 min(d_(v5(l)),d_R).                    (3b)

This follows directly by factoring pi^min out of [5l]_Q+Q^(5l)y before squaring. Other factors and their inverses are analytic units. The exact-boundary case [5l]_Q=0 obeys the same capped formula. This raw-factor information is retained for every R; it is not inferred later from a bound H_s on one ball.

Define

    D_s=sum_(j=0)^(s-1) 4*5^(s-j-1)d_j
       =(4s-1)5^s+1,
    H_s=(52s+57)5^s-1.                              (3c)

Thus D_0=0, H_0=56, and D_(s+1)=5D_s+4d_s.

For each interval between adjacent surviving sites, let E_s^(R) be the sum of raw edge weights b_R(l) on that interval minus D_s. There are7*5^s original cut edges in the interval. The precise invariant is:

    every effective off-diagonal entry is bounded below by
    the MINIMUM of the two sums of E_s^(R) along cyclic arcs
    joining its endpoint sites.                     (3d)

Intervals need not all have the same weight. Formula(3d), for every R>=s, is the invariant; H_s is only its scalar consequence.

For R=s, count divisibilities in any interval of length7*5^s. For each j<=s there are at least7*5^(s-j) multiples of5^j. Since

    min(d_(v5(l)),d_s)=4+sum_(j=1)^s 4*5^j 1_(5^j|l),

the raw edge sum is at least56(s+1)5^s. Subtracting D_s gives H_s. For R>=s the raw caps are larger, so every E_s^(R)>=H_s>d_s. In particular(3d) implies the valuation bound H_s times coarse cyclic distance.

Here is the matrix induction establishing(3d). At s=0 eliminate only the other34 residue species. Their inverse is a convergent Neumann series with unit diagonal denominators. Each term connects fixed-species sites by raw cut edges. A cycle has strictly positive edge cost, so deleting cycles leaves one of the two simple cyclic arcs. The unit scalar diagonal normalizations preserve the bound.

For the inductive step, work in the same domain(3a) with R>=s+1 and eliminate the four unwanted next-digit classes. Every newly removed diagonal denominator has valuation exactly d_s. The complement inverse converges because its off-diagonal entries have valuation at least H_s>d_s. Bound each term of its Neumann series as a walk of dense current edges. Replace each dense edge by an arc attaining the minimum in(3d). Subtract d_s also at every newly removed current vertex visited inside an expanded arc, even if that visit did not originally supply a denominator; this only lowers the bound. A loop in this expanded cyclic walk has positive cost: each traversed interval costs at least H_s and the vertex penalty is at most d_s per interval. Erasing loops therefore cannot increase the lower bound. The remaining simple arc has exactly the next interval cost

    sum(five consecutive E_s^(R))-4d_s
      =sum(raw b_R on the larger interval)-D_(s+1).

This is(3d) at s+1. The argument applies to the direct retained entry as well as every Schur correction term, and to any number of consecutive coarse intervals. It does not flatten previously resummed diagonal returns into unrestricted raw walks through arbitrarily small denominators. Those would not have the required positivity. All summands and inverses used here have the stated coefficientwise Gauss bounds.

After the next diagonal roots are constructed below, replacing the old spectral coordinate in(3a) by

    z=rho_(s+1,c)(y)+pi^(d_(s+1)+1)w'

is an integral Gauss-algebra substitution: the center change has valuation greater than d_s+1 and the new disc is narrower. Thus the same two-index bounds remain valid in the new centered domains.

## 4. Analytic root separation is preserved

At stage s, different next-digit classes have diagonal gap valuation exactly d_s. Restrict to the parameter ball y in pi^(d_(s+1))O and the spectral coordinate(3a) centered at the chosen class. The four complementary classes have diagonal denominators pi^(d_s) times analytic units. Their off-diagonal perturbation is smaller by H_s-d_s>0, so the complement inverse exists in the coefficientwise Gauss algebra.

The new diagonal Schur self-energy uses two off-diagonal connections and at least one complementary denominator. Its Gauss valuation is at least

    B_s=2H_s-d_s.

Consequently its Lipschitz gain with respect to the UNscaled parameter y is at least

    B_s-d_(s+1)=(104s+84)5^s>0.                     (4a)

This is a coefficient bound: subtracting the values of any restricted series at u,u' factors u-u', and then y-y'=pi^(d_(s+1))(u-u'). It is not an inference from pointwise values. With respect to the spectral variable, the scaled disc in(3a) gives the safe positive gain

    B_s-(d_s+1)=2H_s-2d_s-1>0.                     (4b)

Center z at the previous scalar diagonal root and solve the scalar Schur equation by successive substitution. Equations(4a)–(4b) make this an analytic contraction. The correction belongs to pi^(B_s)O<u>, so it is strictly Lipschitz-contracting in y. Adding it to the previous root preserves unit divided differences, hence exact valuation of every surviving gap.

The factorization of the new scalar diagonal equation as rho_(s+1,k)(y)-z times an analytic unit follows from(4b). Its unit normalization leaves the off-diagonal bounds unchanged. Construct these charts for each next-digit reference class. Exact translation covariance by35*5^(s+1) preserves its broad NEW level-(s+1) ball pi^(d_(s+1))O and identifies the new root functions at its surviving sites. The next digit classes are separate translated charts; they are not identified by translations that leave a smaller chart. Translation acts by y op y_k and has unit derivative 1+pi y_k. Therefore

    v_pi(rho_(s+1,k)(0)-rho_(s+1,l)(0))
      =v_pi(y_k-y_l)=d_(v5(k-l)).                    (4c)

The base of this Lipschitz induction is the integral local eigenvalue function with nonzero residue offset derivative. The first34-species self-energy has valuation16 and y-Lipschitz gain12 on the pi^4 ball, as established in section2. Restriction to later parameter balls preserves every previously proved strict divided-difference bound.

Thus the off-diagonal interval-weight invariant and the diagonal separation property are proved together. In particular the improvement in H_(s+1) comes from the representation with R=s+1, not from restriction of a naked H_s estimate.

## 5. Termination and statement still requiring audit

Starting with35 distinct residue species, successively fix all e-1 base-five digits of each copy index. At each step the five spectral discs are disjoint, the complement is invertible, and the Schur contractions count the roots in that disc. After e-1 levels each disc contains exactly one simple root. There are35*5^(e-1)=7*5^e roots in total. This would prove simplicity of A_(7*5^e) for every e>=1.

The r=e-1 parameter domain is only used to obtain the final scalar root; there is no further nontrivial digit comparison. Exact zero physical boundaries remove walks and do not weaken any estimate.

The argument must still pass independent review, especially the weighted walk/detour estimate, analytic coefficient bounds after spectral centering, and covariance of the iterated diagonal root. No uniform theorem is accepted solely from the displayed exponents. The earlier N175 proof remains independently valid without this extension.

## Review boundary

The v1 proof remained incomplete. Only the v2 two-index coefficientwise
cyclic-arc invariant and corrected broad/local analytic domains have the
accepted uniform verdict. The finite replay certifies the inherited residue
and jet input; it does not replace the all-depth analytic induction.
See [the scoped review](../record/uniform_five_cluster_review.md).
