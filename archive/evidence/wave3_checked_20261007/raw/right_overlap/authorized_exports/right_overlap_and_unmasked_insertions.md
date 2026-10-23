# Right displacement overlap and complete unmasked pinch compositions

7 October 2026. **Author proof candidate; independent review pending.** The previously frozen left-overlap proof, SHA256 `11c90c3dac599f63d6508685647db66ba78ebfb280955a61b29917daab7786cb`, was independently accepted according to the parent's present handoff. Its source and analytic machinery are reused, but its left-multiplication estimate is not substituted for the right estimate below. Scoped sources and the parent-reported published commit are recorded in `source_bindings.json`.

The literal odd-N U=exp(i 10^-80 N A_N)M_N, physical midpoint half-shift, centering and raw modular aliases are unchanged. No source checkout, publication or target model was modified.

## 1. Definitions and results

Use ordinary Hilbert-Schmidt space H=End(C^N). Define displacement slices and synthesis

    (A_c)_(y+c,y)=U_(y+c,y),  C e_c=A_c*,
    R_U X=XU,  L_B X=BX,  K^R_r=C* R_U^r C.

The slice label is row minus column, explicitly the negative of the source's charge label in a complete sum. Source charge masks retain their original convention. Write T=Ad(U), D=sum_c P_c T P_c. For occupation phases put W_theta=Z_theta U, T_theta=Ad(W_theta), D_theta=V_theta D. All these superoperators fix e0=I/sqrt(N) and preserve H0=e0^perp.

**Candidate results.**

1. For every fixed r>=1, `||K^R_r||=O_r(sqrt(log(2N)/N))`.
2. Uniformly over arbitrary N-dependent unitary B, the positive expression

       F_n(B)=(1/N)sum_b |Tr(U^n K_b B)|^2,
       K_b=Z_b U Z_b*,

   has vanishing mean after division by N on every interval of n whose length tends to infinity. The uniform finite-block bound is (8) below.
3. Every complete, unmasked fixed-order separated-pinch composition sum vanishes on compact positive Heisenberg bands in its natural normalization, both untwisted and annealed, hence also after their exact occupation subtraction. Precise normalizations are (11)--(14).
4. The untwisted composition-average estimate is already uniform for insertion orders j=o(N). Moreover collective compactness and flatness give a stronger pointwise estimate for EVERY word with j>=3 insertions, uniform over separations and occupation phases. Consequently the complete binomially weighted insertion correction is negligible, uniformly in the switch parameter z in [0,1]; see (23).

None of these is a Hamming-filtered or high-switch-masked theorem. No T16, full deterministic offcharge comparison, balanced microscopic law or higher-factorial closure follows.

## 2. Derive the right overlap independently

Direct multiplication, rather than a transpose inference, gives

    K^R_r(c,d)=sum_y U_(y+c,y) conjugate(U_(y+d,y))
                                      (U^r)_(y+d,y+c).       (1)

For fixed r, replace U by the exact four-branch one-step parametrix V from the accepted source. As in the prior proof, `||C_U-C_V||=O(N^-1)` and fixed-power telescoping gives an O_r(N^-1) error in (1). The entry formula for the parametrix has r internal variables. Put x=(x_0,...,x_(r-1)), z_0=x_0+d, z_r=x_0+c, z_j=x_j for 1<=j<r. Its branch phase is

    Phi_R(x;c,d)=S_alpha(x_0+c,x_0)-S_beta(x_0+d,x_0)
                         +sum_(j=0)^(r-1) S_(gamma_j)(z_j,z_(j+1)). (2)

The variables here are scaled real lifts. The full sampled kernels have their source's exact odd-N gluing; no individual branch is reduced modulo one.

For the cat quadratic part, every branch shift is affine. The internal Hessian is again

    H^0=-(3/2)I+(P_r+P_r*)/4,  spectrum in [-2,-1],
    ||(H^0)^-1||_infinity<=1.                               (3)

The external vectors, however, are different from the left-overlap vectors. Directly:

    r=1:  Phi^0_cd=1/4,  Phi^0_xc=-e0,  Phi^0_xd=0;
    r>=2: Phi^0_cd=0,
           Phi^0_xc=-(5/4)e0+(1/4)e_(r-1),
           Phi^0_xd=-(1/4)e0+(1/4)e_1.                     (4)

This includes the double edge at r=2. The l1 norm of the first vector is at most 3/2, and the infinity norm of the second is at most 1/4.

Here is an independent evaluation of the general reduced cat Hessian. Eliminating x_1,...,x_(r-1) in the chain gives the quadratic generating phase

    S_r(u,v)=-(A_r u^2-2uv+A_r v^2)/(2B_r),
    S^r=[[A_r,B_r],[B_r/2,A_r]],  S=[[3,4],[2,3]].

This identity follows by eliminating one intermediate variable at a time: composing S_r(u,x)+S_1(x,v) yields the displayed phase with A_(r+1)=3A_r+2B_r and B_(r+1)=4A_r+3B_r. The base is A_1=3,B_1=4. Affine branch/alias terms do not change a reduced quadratic Hessian.

The remaining right phase is

    S_1(x+c,x)-S_1(x+d,x)+S_r(x+d,x+c).

Its scalar Schur mixed derivative is

    (4A_r^2-B_r^2-4)/(8B_r(A_r-1))
      =(A_r+1)/(4B_r),                                   (5)

using A_r^2-B_r^2/2=1. If lambda=log(3+2sqrt(2)), then A_r=cosh(r lambda), B_r=sqrt(2)sinh(r lambda). Thus (5) lies in [1/(4sqrt(2)),1/4]. The direct exceptional values are 1/4 for r=1 and 3/16 for r=2. This computation does not infer the right bound from the left bound.

The source supplies globally `|partial^2(S_alpha-S_alpha^0)|<eta=10^-60` at the literal tau. In (2), each variable meets at most four factors, each composed with two linear forms of total coefficient l1 norm at most four and combined coefficient at a single variable at most two. Thus the full Hessian row-sum perturbation is less than 64 eta<delta=10^-50, including r=1,2. It follows exactly as in the preceding proof that H=Phi_R,xx is uniformly negative,

    ||H^-1||_infinity<=2,
    ||H^-1-(H^0)^-1||_infinity<=2delta.

For every alias ell, strict concavity gives a unique global stationary point of Phi_R-ell.x. Its reduced phase Psi^R_ell has mixed derivative `Phi_R,cd-Phi_R,cx H^-1 Phi_R,xd`. Using (4), the perturbation from (5) is at most 8delta. Consequently

    1/10 <= Psi^R_(ell,cd) <=1/3                            (6)

for every branch and alias, uniformly on the external parameter square.

The remaining analytic steps use the already reviewed machinery with these newly verified right-phase hypotheses. Insert smooth internal cutoffs by periodicizing the FULL sampled product before branch expansion. Poisson summation retains all aliases; only finitely many have stationary points near the common compact support for fixed r, and the nonstationary tail is summable by repeated integration by parts. Uniform stationary phase turns r sums and r+2 kernels into finitely many matrices `N^-1 b_N(c,d)e(N Psi^R_ell(c,d))`, plus entrywise O_r(N^-2). The bounds (6) place row-difference phase increments between |c-c'|/10 and |c-c'|/3, away from every integer alias. The same summation-by-parts TT* estimate, including endpoint terms, gives norm O_r(sqrt(log(2N)/N)). The accumulated remainder has norm O_r(N^-1). This proves Result 1. Constants are finite for each fixed r; no uniform stationary-phase constant in r is asserted.

## 3. A long coherent run uniformly over all remaining Kraus factors

Character orthogonality gives

    F_n(B)=sum_c |Tr(U^n A_c B)|^2
          =N ||C_B* v_n||^2,
    C_B=L_(B*) C,  v_n=U^n/sqrt(N).                        (7)

This is a LEFT rotation of the frame. Right multiplication commutes with it, so

    C_B* R_U^r C_B=C* R_U^r C,
    ||C_B||^2=||C||^2<=C_flat.

The corresponding statement with left multiplication is generally false for arbitrary B. Applying the block-Gram proof to R_U, define

    gamma_(L,N)=C_flat/L+(1-1/L) max_(1<=r<L)||K^R_r||.

For every B, every integer starting point A and every integer length M>=0,

    sum_(n=A)^(A+M-1) F_n(B)
       <=N [M gamma_(L,N)+C_flat L].                       (8)

The same bound holds after any probability average over B. It is uniform in the matrix B, but B must be fixed while the indicated n is summed. We do not replace B by an uncontrolled n-dependent choice. For fixed L, gamma_(L,N)->C_flat/L.

## 4. Complete composition sums and their exact normalization

For j>=1 and n_i>=0, let

    G_(j,N)(n;theta)=Tr_H[D_theta T_theta^(n_1) ...
                                  D_theta T_theta^(n_j)].

The finite diagonal twirl gives D_theta=(1/N)sum_b Ad(K_(b,theta)), where K_(b,theta)=Z_b W_theta Z_b*. Hence G is the average of squared ordinary matrix traces of unitary Kraus words. In particular G>=0, including when some n_i=0. Repeated modulations, repeated coordinates and consecutive insertions remain in the sum.

At theta=0, fix all gaps except n_j and all Kraus labels except the pinch adjacent to n_j. Cyclicity writes the matrix trace as `Tr(U^(n_j) K_b B)` with B unitary and independent of n_j. Formula (8) therefore applies to that gap after averaging all the remaining labels. In particular `G_(j,N)(n;0)<=C_flat N` for every n and j.

For total length m>=j define

    A_(j,N,m)(theta)=1/binom(m-1,j-1)
             sum_(n_1+...+n_j=m-j) G_(j,N)(n;theta).         (9)

This is the average over all weak compositions, including every boundary n_i=0. It is also exactly the average over all choices of j insertion slots in a rooted product of length m. If S_(j,N,m) denotes the UNnormalized sum over those slot choices, then

    S_(j,N,m)=(m/j) sum_(sum n_i=m-j) G_(j,N)(n),
    S_(j,N,m)=binom(m,j) A_(j,N,m).                         (10)

To check the multiplicity, mark one of the j D slots. Counting marked slot sets gives j choices per term; placing the distinguished D at a specified root and reading its j cyclic gaps gives m root choices per composition. Cyclicity of trace then proves (10), even for periodic slot patterns; no division by a presumed orbit size occurs.

For fixed j, (8) summed over the other j-1 gaps gives, for bounded compact w supported in [a,b], a>0,

    N^-2 sum_(m>=j) |w(m/N)| A_(j,N,m)(0) ->0.             (11)

Equivalently at fixed j,

    N^(-(j+1)) sum_m |w(m/N)| sum_(sum n_i=m-j)G_(j,N)(n;0) ->0,
    N^(-(j+2)) sum_m |w(m/N)| S_(j,N,m)(0) ->0.            (12)

These equivalences use m/N in a fixed positive compact interval. A raw unnormalized coefficient is not asserted to vanish at the original N^-2 normalization.

There is also a useful uniform version that does not need growing-r stationary phase. Put m0=ceil(aN), m1=floor(bN), and assume 1<=j<=m0. Prefix summation by parts in the distinguished gap, whose weight 1/binom(m-1,j-1) decreases as that gap increases, gives

    N^-2 sum_(m=m0)^m1 A_(j,N,m)(0)
      <= ((m1-m0+1)/N) gamma_(L,N)
         +(C_flat L/N)[1+(j-1)sum_(m=m0+1)^m1 1/(m-1)].  (13)

Here is the boundary count. For fixed total s of the other j-1 gaps, there are binom(s+j-2,j-2) fibers. The first allowed total length is max(m0,s+j). Summing their initial decreasing weights gives 1 for s<=m0-j, by the hockey-stick identity; for s>m0-j the ratio is `(j-1)/(s+j-1)`. This is exactly the bracket in (13). At j=1 the single fiber gives the same bound with bracket 1. Thus short fibers and zero gaps have an explicit remainder, not an omitted boundary sector.

Taking N->infinity at fixed L and then L->infinity proves (11) uniformly for j=j_N=o(N), in particular j_N=O(log N). This statement concerns the complete composition average for one chosen j at each N. It is not a bound on every prescribed gap vector or on arbitrary path subsets.

## 5. Annealed separated compositions: a bounded-factor extension

The native theorem supplied by the parent treated one consecutive D block. The following extension is stated and proved here for the additional bounded factor needed by separated compositions; it is not attributed to that earlier scope.

Let phi be smooth, nonnegative and compactly supported on R, with phi>=1 on [0,b]. Set

    S_N(T_theta)=sum_(n in Z) phi(n/N) T_theta^n.

Two discrete differences of phi, together with the trivial O(N) bound, give on the unit circle

    |sum_n phi(n/N)e^(int)| <= C_phi N/(1+N^2 dist(t,2pi Z)^2)
                             <= C'_phi P_(exp(-1/N))(t).

Normal spectral calculus therefore bounds the trace norm of S_N(T_theta) by C_phi Tr_H P_(exp(-1/N))(T_theta). By the accepted universal phase Abel estimate,

    E_theta Tr_H P_r(T_theta)
      =N^2+2 sum_(m>=1) r^m E|Tr W_theta^m|^2=O(N^2),
    r=exp(-1/N).                                           (14)

The actual D has a uniform rank-R approximation F_N with ||D-F_N||<=epsilon and bounded ||F_N||, by the accepted collective compactness theorem. For ANY measurable family of superoperators B_theta with ||B_theta||<=1, cyclicity and trace norm duality give

    |E Tr_H[D_theta S_N(T_theta) B_theta]|/N^2
          <= C_phi R/N + C_phi epsilon.                   (15)

Indeed the finite-rank part has rank at most R, norm O(N), and costs O(RN); the tail costs epsilon times the expected trace norm in (14). V_theta is unitary, so it preserves the rank and approximation error. No independence between B_theta and T_theta is required. Let N->infinity and then epsilon->0. The resulting o(1) in (15) is uniform over all such B_theta.

For a separated pinch word, hold all other gaps fixed and put their remaining superoperator product into B_theta; it is a contraction. All integer powers T_theta^n, including negative powers in the auxiliary smooth majorant, are unitary conjugations. Thus the full traces `Tr[D_theta T_theta^n B_theta]` are nonnegative for this physical B_theta, allowing the actual interval 0<=n<=bN to be bounded by phi. Formula (15) proves

    sup_(other gaps) sum_(n_j=0)^(floor(bN)) E G_(j,N)(n;theta)=o(N^2). (16)

The uniformity is in the other gaps, not a statement about individual unaveraged theta. Summing the O_j(N^(j-1)) other gap vectors and using the lower bound binom(m-1,j-1)>=c_(a,j)N^(j-1) on the band gives, for every fixed j,

    N^-2 sum_m |w(m/N)| E A_(j,N,m)(theta) ->0.             (17)

At j=1 this agrees with the supplied native theorem; at j=2 it handles genuine separated insertions. Equations (11),(17) imply the signed, complete occupation-subtracted fixed-j comparison by the triangle inequality. The phase expectation remains the exact full occupation projector. No repeated-occupation or finite-color term was deleted.

## 6. Three pinches control the whole unmasked insertion tail

This elementary consequence of actual compactness supplies uniformity beyond the fixed-j argument. Let D0=D|H0. In the coordinate matrix-unit basis,

    ||D||_(S2)^2=sum_(c,x,y) |U_xy|^2 |U_(x+c,y+c)|^2
                  <=C_flat N.                             (18)

For example bound the second entry by C_flat/N, sum its N charges, then sum |U_xy|^2=N. This is the ordinary Schatten norm on the N^2-dimensional superoperator space; rescaling the underlying HS inner product changes none of its singular values.

Collective compactness gives, for each epsilon>0, a fixed R with s_(R+1)(D0)<=epsilon eventually. Also ||D0||<=1. Splitting the singular values yields

    ||D0||_(S3)^3 <= R +epsilon ||D0||_(S2)^2,
    eta_N:=N^-1 ||D0||_(S3)^3 ->0.                        (19)

There is no quantitative rate for eta_N asserted here. Since V_theta preserves H0 and is unitary, D_theta|H0 has exactly the same singular values as D0. For every j>=3 and every list of gaps, Schatten Holder with three S3 factors and bounded remaining factors gives

    |G_(j,N)(n;theta)-1| <= ||D0||_(S3)^3 =N eta_N.         (20)

The scalar 1 is the common identity direction, and is retained exactly. The bound is uniform in theta, all gaps, total length, and insertion count j>=3. One may insert the eventual centered gap factor rho^(j-3), but it is not needed. In particular

    0<=A_(j,N,m)(theta)<=1+N eta_N,  j>=3.                 (21)

The proof uses compactness only for this THREE-insertion tail. It cannot bound the first or second insertion by the same argument. Thus it does not contradict the period-six first-loop obstruction or claim a generic compactness-only solution.

Combining (11),(17) for j=1,2 with (21), any nonnegative coefficient array p_(j,m,N) with sum_(j>=1)p_(j,m,N)<=1 satisfies

    N^-2 sum_m |w(m/N)| sum_(j=1)^m p_(j,m,N)
       [A_(j,N,m)(0)+E A_(j,N,m)(theta)] ->0.              (22)

This permits j up to m and avoids multiplying a nonquantitative o(1) by the number of insertion orders. The unmasked tail therefore presents no new obstruction specifically at j=O(log N).

## 7. Full unmasked switch expansion and the surviving boundary

For z in [0,1], noncommutative expansion and (10) are exact:

    Tr[z T_theta+(1-z)D_theta]^m
      =z^m |Tr W_theta^m|^2
        +sum_(j=1)^m binom(m,j)z^(m-j)(1-z)^j A_(j,N,m)(theta).

The insertion coefficients are binomial probabilities whose total is 1-z^m<=1. Thus (22) implies, uniformly for every sequence z_N in [0,1],

    N^-2 sum_m w(m/N){Tr[z_N T+(1-z_N)D]^m-z_N^m|Tr U^m|^2}->0, (23)

and the analogous annealed expression tends to zero. Consequently their exact occupation difference equals, at this compact signed normalization, the scalar-damped ORIGINAL occupation difference, plus o(1). This identifies the unmasked insertion correction; it does not identify the zero-insertion spectral term.

At z_N=1-A log N/N the typical insertion count is O(log N), and (23) is valid there. The remaining obstacles are precise:

- The original high-Hamming extraction introduces Q_q, which is not an NxN unitary conjugation for arbitrary q. The Kraus positivity and uniform-B frame argument cannot be applied to that filtered sum. General signed subsets are not bounded by their complete sums.
- Although (20) survives extra unitary q factors as a trace norm estimate, Fourier cutoff extraction has a growing norm, and no rate for eta_N was proved. This is insufficient for the actual high-Hamming/high-switch boundary masks.
- The unnormalized order-j coefficients grow combinatorially; (11),(22) use their stated averaging or binomial normalization. They do not estimate raw coefficients with arbitrary weights.
- Recovering the undamped zero-insertion term from z_N^m times that term costs polynomial powers of N on the band. Neither (23) nor the known damped interior estimate controls this deconvolution. Differentiating an unspecified o(1) or multiplying it by the marked-switch factor is unjustified.

Thus the precise obstruction at the T16 boundary is no longer an unmasked logarithmic-insertion tail. It is the retained masks, source weights/rates and the undamped zero-insertion comparison. No T16 conclusion is asserted.

## 8. Review boundary

The right-phase geometry, arbitrary-B frame rotation, composition normalization, bounded-factor annealed extension and Schatten tail are new author derivations requiring independent review. Inputs are the exact actual parametrix, flatness, collective compactness and universal phase Abel bound, at their recorded accepted scopes. Exact bounded controls accompany this proof; they do not certify stationary phase or an asymptotic theorem. No uniform growing-r stationary-phase constants, effective actual-tau startup, global novelty, formal analytic certificate or BGS result is claimed.
