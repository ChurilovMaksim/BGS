# Heisenberg-window control for the explicitly compensated family

This is a direct quantitative corollary of Theorem 3 in
[smooth_recurrence_and_compensation.md](smooth_recurrence_and_compensation.md),
not a positive BGS theorem or a newly claimed general perturbation method.
The family, its vanishing classical strength and its norms are essential.
The finite verifier checks normalization and the cluster estimate; it does not
certify the analytic parent theorem. External priority is unassessed.

## Exact finite statement

Use the odd-prime Pell sequence and the physical Weyl convention of the
parent note. For a fixed real C7 symbol g put d=Cg, r={g,d}/(4 pi),
A=A_N(g), D=A_N(d), R=A_N(r), and

    V = exp(i[epsilon(A-D) - epsilon^2 R/N]) U0,
    S = exp(-i epsilon A) V exp(i epsilon A),
    delta_N = C_g |epsilon|^3/N^2 + D_g epsilon^2/N^3.

The parent theorem proves ||S-U0||_op <= delta_N for every real epsilon.
For every integer ell, independently of its size,

    ||S^ell-U0^ell||_op <= min(2, |ell| delta_N).              (H1)

For ell>=1 use the telescoping identity

    S^ell-U0^ell = sum_(j=0)^(ell-1) S^(ell-1-j)(S-U0)U0^j.

Each factor outside S-U0 is unitary. Negative ell follows by taking
adjoints; ell=0 is exact. Unitary similarity preserves traces, hence on
the full space

    |Tr(V^ell)/N - Tr(U0^ell)/N| <= min(2, |ell| delta_N).     (H2)

For inversion-even g, all the relevant operators preserve odd parity and
the same estimate holds for tau_-(M)=Tr_-(M)/d_N, d_N=(N-1)/2.
No Hilbert--Schmidt-to-operator-norm upgrade is being assumed: the parent
compensated estimate already holds in operator norm.

The phase-normalized unperturbed odd spectrum has every K-th root of unity
with the same multiplicity (N-1)/(2K). Consequently, exactly,

    tau_-(U0^ell) = 1_{K divides ell}.                       (H3)

On the full space the corresponding value is 1 when K divides ell and
1/N otherwise. These assertions follow from the free signed dilation
orbits in the Pell construction; they do not require N to be prime.

## A window proportional to the Hilbert-space dimension

Fix c>0. If epsilon_N=o(N^(1/3)), then

    N delta_N = C_g |epsilon_N|^3/N + D_g epsilon_N^2/N^2 -> 0.

It follows from (H2)--(H3) that

    sup_(|ell|<=cN)
      |tau_-(V^ell) - 1_{K divides ell}| -> 0.                (H4)

This covers times proportional to d_N, not only fixed multiples of K.
For example epsilon_N=N^(1/3)/log N is allowed. Its quantum exponent grows,
but the classical action amplitude epsilon_N/N still vanishes. For every
fixed rho>0, choosing integers ell_N divisible by K with ell_N/d_N->rho
is possible because K/d_N->0; (H4) then gives tau_-(V^ell_N)->1.
The conclusion is persistence of coherent arithmetic returns, not local
random-matrix universality.

## The usual form-factor normalization needs a stronger hypothesis

Define F_N(ell)=|Tr_-(V^ell)|^2/d_N. At nonresonant times K does not divide
ell, (H2) gives the explicit inequality

    F_N(ell) <= d_N ell^2 delta_N^2.                         (H5)

Thus epsilon_N=o(N^(1/6)) is sufficient for

    sup_(0<|ell|<=cN, K does not divide ell) F_N(ell) -> 0.    (H6)

Indeed d_N ell^2 delta_N^2 is bounded by a constant, depending on c and g,
times |epsilon_N|^6/N + epsilon_N^4/N^3, using (x+y)^2<=2x^2+2y^2.
At resonant times in the same window,

    F_N(ell)/d_N = |tau_-(V^ell)|^2 -> 1                     (H7)

uniformly whenever epsilon_N=o(N^(1/3)). In particular (H6)--(H7) hold
together under the stronger o(N^(1/6)) assumption.

The distinction is necessary: convergence of normalized traces to zero
in (H4) alone does NOT imply F_N(ell)->0, because the latter multiplies the
squared normalized trace by d_N. This note does not exchange these two
normalizations or silently claim (H6) at the weaker scale.

## An averaged form-factor theorem at the weaker strength

The pointwise qualification above does not prevent an averaged statement at
the weaker scale epsilon=o(N^(1/3)). Spectral separation supplies the missing
upper bound; normalized trace convergence alone would not supply it.

**Finite cluster estimate.** Let K>=3 be odd and D=Kn. Suppose a unitary
spectrum has exactly n phases in each circular arc of radius eta about j/K,
0<=j<K, where 0<=eta<=1/(4K). Choose real lifts

    theta_(j,r)=j/K+e_(j,r),  |e_(j,r)|<=eta.

For M>=1 consecutive integer times I, put L=max_(ell in I)|ell| and
H_h=sum_(r=1)^h 1/r. With F(ell)=|Tr U^ell|^2/D, one has

    |(1/M)sum_(ell in I) F(ell)-n|
       <= 8 pi^2 n L^2 eta^2 + (2D/M) H_((K-1)/2).          (H8)

**Proof.** Expand the squared trace into ordered eigenphase pairs. The
same-cluster contribution would be n if all e_(j,r) were zero. Ordered
pair symmetry cancels its imaginary part. The inequality
1-cos(t)<=t^2/2 and |e_(j,r)-e_(j,s)|<=2eta show that this contribution is
between n-8 pi^2 n L^2 eta^2 and n.

For a distinct-cluster pair, write h=min(|j-k|,K-|j-k|). Its phase
difference has circular distance at least h/K-2eta>=h/(2K). A finite
geometric sum and |sin(pi x)|>=2 dist(x,Z) therefore give

    |(1/M)sum_(ell in I) exp(2 pi i ell(theta_(j,r)-theta_(k,s)))|
       <= 1/(M |sin(pi(theta_(j,r)-theta_(k,s)))|)
       <= K/(Mh).

There are n^2 ordered eigenphase pairs for each ordered pair of clusters,
and sum_(j!=k)1/h=2K H_((K-1)/2). After dividing by D, the total
distinct-cluster contribution in absolute value is at most
2D H_((K-1)/2)/M. Combining the two bounds proves (H8). No randomness,
independence or cancellation between different cluster pairs is assumed.

**Application to the compensated family.** Assume g is inversion-even and
epsilon_N=o(N^(1/3)). Then, for fixed 0<a<b,

    (1/#I_N)sum_(ell in I_N) F_N(ell) = (d_N/K)(1+o(1)),
    I_N={ell in Z : a d_N<=ell<=b d_N}.                      (H9)

To justify multiplicities rather than merely spectral proximity, set
S=exp(-i epsilon A)V exp(i epsilon A). Once delta_N<sin(pi/K), the
straight homotopy U0+t(S-U0) has its spectrum in disjoint disks about the
K roots. The normal resolvent bound for U0 excludes spectrum outside the
delta_N neighborhoods throughout the homotopy. Contour projection ranks
are constant, hence each final cluster contains exactly n=d_N/K levels.
Every final eigenvalue is unitary and within chord distance delta_N of its
root. Circular phase distance is at most one quarter of chord distance,
so eta=delta_N/4 is valid. For large N, eta<=1/(4K), since
N delta_N->0 and K=O(log N) on this Pell sequence.

Apply (H8) with D=d_N, M=#I_N asymp D and L=O(D). Dividing its right
side by n gives

    O_(a,b)((D delta_N)^2 + K log K/D)=o(1).

This proves (H9). Its mean diverges because d_N/K tends to infinity.
It is a form-factor obstruction in a Heisenberg window for the explicitly
compensated family, with the same symmetry and vanishing-classical-strength
qualifications as (H4). It does not strengthen the pointwise assertion (H6).

## Relation to the larger microscopic pinning range

The parent note obtains nearest-neighbour spacing collapse and divergent
close-pair counts in the larger range epsilon=o(N^(2/3)K^(-1/3)). There it
suffices that K delta_N tends to zero. Uniform trace comparison to times
proportional to N needs N delta_N tending to zero instead. These are
compatible conclusions for different ranges, not an improvement of the
Heisenberg-time estimate at unchanged strength.

The counterterm -epsilon^2 R/N is explicitly part of V. It must not be
removed when quoting (H1)--(H9), nor described as an unchanged fixed-strength
classical perturbation. These statements do not establish the microscopic
BGS conjecture, do not resolve all arithmetic symmetries, and do not claim
novelty for the elementary telescoping argument.
