# Uniform higher-cluster candidate for N=7*5^e

Status: proposed proof, not yet audited. Scope is simplicity of the actual A_N for every e>=1. No claim about U_N simplicity, seven-divisible N outside this family, or BGS. This extends the reviewed N175 calculation; the only finite algebraic input is the seven degree-five residue blocks and their certified nonzero offset derivatives.

## 1. Analytic translated model and fixed residue species

Use the real-Jacobi gauge and normalized matrix T=(200A_real-180I)/eta from first_ramified_cluster_split.md. Put Q=q^7, pi=Q-1, and v_pi(pi)=1. Then v_pi(5)=4*5^(e-1). Write

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

## 3. Weighted walk estimate after r base-five digits

After fixing r digits of k, retain k=c modulo5^r. The other sites have been eliminated. For a removed site j whose first differing digit is s<r, the denominator valuation is exactly d_s by(2). All other residue-species denominators have valuation zero.

Define

    D_r=sum_(s=0)^(r-1) 4*5^(r-s-1)d_s
       =(4r-1)5^r+1,
    H_r=(52r+57)5^r-1.                              (3)

The empty sum D_0 is zero and H_0=56.

Claim: on y in pi^(d_r) O, the effective off-diagonal entry between retained sites at coarse cyclic distance a is divisible by pi^(H_r a).

For a straight path between consecutive retained sites, the number of original length-five cut edges is R=7*5^r. At least floor(R/5^s)=7*5^(r-s) of their indices are divisible by5^s, for 0<=s<=r. Since

    min(d_(v5(l)),d_r)=4+sum_(s=1)^r 4*5^s 1_(5^s|l),

the total bond valuation from(1) is at least

    2[4R+sum_(s=1)^r 4*5^s*7*5^(r-s)]
      =56(r+1)5^r.                                 (4)

Among the5^r-1 intermediate fixed-species sites, exactly
4*5^(r-s-1) have first differing digit s. Their denominator cost is D_r. Subtracting from(4) gives H_r. For distance a, apply the same count to a consecutive intervals. Intermediate retained sites contribute no denominator; walks through their complementary local modes still obey the same edge bound.

For completeness, Schur expansions are taken stage by stage, not by a global inverse with uncontrolled small denominators. At stage s, every newly eliminated site's denominator has valuation d_s, whereas every current off-diagonal edge has valuation at least H_s times its coarse distance. Because H_s>d_s, the complementary inverse converges. A backtracking detour or repeated-vertex loop has strictly positive excess valuation: each additional coarse edge costs at least H_s, while each newly inserted denominator costs at most d_s. Removing detours cannot lower the bound for the monotone connection. Thus the straight-path estimate is a lower bound for every walk contribution. Summing convergent contributions preserves the bound; no noncancellation assumption is used.

This weighted count is the new uniform ingredient. The weaker recurrence obtained by forgetting high cuts, h_(r+1)=5h_r-4d_r, eventually fails. Equation(4) restores the missing 5-adic cut valuations at every level.

## 4. The scalar diagonal remains separating

At stage r, split retained sites by their next digit. Distinct digit classes have diagonal differences of valuation exactly d_r. To study one class, eliminate the other four. The inverse is valid by H_r>d_r. A new diagonal self-energy uses at least two off-diagonal connections and one denominator, hence has valuation at least

    B_r=2H_r-d_r.

For the next parameter ball y in pi^(d_(r+1)) O, Cauchy coefficient bounds for integral power series in y/pi^(d_(r+1)) show that its Lipschitz gain is at least

    B_r-d_(r+1)
      = (104r+84)5^r >0.                            (5)

The z-derivative gain is at least 2H_r-2d_r>0. Center the spectral variable at the previous diagonal root before applying these bounds; the complementary denominators are pi^(d_r) times analytic units on this domain. The scalar Schur root is obtained by a convergent contraction. Its difference from the previous root is strictly Lipschitz-contracting in y. Therefore(2) is preserved.

Exact translation covariance by35*5^(r+1) gives the same new scalar root function at all surviving sites. Thus their diagonal gaps retain the precise valuation d_(v5(k-l)), rather than merely a pointwise lower bound. This is needed: an arbitrary diagonal perturbation of small fixed norm would not preserve extremely close higher-digit gaps.

Equations(3)–(5) then supply the off-diagonal and diagonal hypotheses for the next level. The finite sums and inequalities hold for all r>=0, independently of e.

## 5. Termination and statement still requiring audit

Starting with35 distinct residue species, successively fix all e-1 base-five digits of each copy index. At each step the five spectral discs are disjoint, the complement is invertible, and the Schur contractions count the roots in that disc. After e-1 levels each disc contains exactly one simple root. There are35*5^(e-1)=7*5^e roots in total. This would prove simplicity of A_(7*5^e) for every e>=1.

The r=e-1 parameter domain is only used to obtain the final scalar root; there is no further nontrivial digit comparison. Exact zero physical boundaries remove walks and do not weaken any estimate.

The argument must still pass independent review, especially the weighted walk/detour estimate, analytic coefficient bounds after spectral centering, and covariance of the iterated diagonal root. No uniform theorem is accepted solely from the displayed exponents. The earlier N175 proof remains independently valid without this extension.
