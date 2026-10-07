# Actual fixed-lag displacement overlap and the positive one-pinch band

7 October 2026. **Author proof candidate, separately self-audited; independent review pending.** This file does not promote a repository claim. It concerns the literal odd-dimensional operator at fixed tau=10^-80. No source repository was changed. Exact input hashes are in `source_bindings.json`.

## 1. Statement and scope

Use the exact raw Weyl quantization and physical midpoint symbol in the frozen `mathematics/fixed_map_path_model.md`. Set U=U_N, with its original scalar centering. Let A_c be the displacement slice of U,

    (A_c)_(y+c,y)=U_(y+c,y),  other entries zero,
    C_N e_c=A_c*,             H_N X=U X,
    K_(r,N)=C_N* H_N^r C_N.

All subscripts on finite matrices are modulo N. The slice index c here is row minus column; the source's P_c uses column minus row. This is the explicit reindexing c->-c in the complete sum, not a change to the source charge convention or its masks. The Hilbert space End(C^N) has ordinary Hilbert-Schmidt norm. C_N has N columns; it is not the charge-pinched superoperator D_N. The exact entry formula is

    K_(r,N)(c,d)=sum_x U_(x+c,x) conjugate(U_(x+c,x+c-d))
                              (U^r)_(x,x+c-d).                 (1)

**Candidate theorem.** For every fixed integer r>=1, through all odd N,

    ||K_(r,N)|| <= C_r sqrt(log(2N)/N).                         (2)

The constants may depend on r and the fixed literal map. No growing-r estimate is asserted. Consequently, for every bounded weight w supported in a fixed [a,b] contained in (0,infinity),

    N^-2 sum_m |w(m/N)| E_(N,m)(0) -> 0,                      (3)
    E_(N,m)(0)=(1/N)sum_b |Tr(U^(m-1) Z_b U Z_b*)|^2.

Combining (3) with the independently reviewed annealed one-pinch theorem supplied by the parent gives the occupation-subtracted compact one-pinch limit. That external-to-this-packet input is recorded by its supplied manifest; its proof was not re-audited here. This does not estimate T16, Hamming-filtered echoes, or general separated pinch insertions.

The source-specific discriminator is the exact four-branch quantization with a uniformly small perturbation of its cat Hessian. Neither compactness of D nor fixed-word trace convergence is substituted for this statement.

## 2. Exact frame identity and the fixed-block implication

Z_b U Z_b*=sum_c e_N(bc) A_c, so finite character orthogonality gives

    E_(N,m)(0)=sum_c |Tr(U^(m-1) A_c)|^2
             =N ||C_N* v_(m-1)||^2,   v_n=U^n/sqrt(N).       (4)

Every v_n is a unit vector, and v_(n+j)=H_N^j v_n. The columns of C_N are orthogonal and eventual actual flatness gives

    ||C_N||^2=max_c sum_y |U_(y+c,y)|^2 <= C_flat.            (5)

For fixed L, let epsilon_(L,N)=max_(1<=r<L)||K_(r,N)|| (zero if L=1). The synthesis map with columns H_N^(-j) C_N, j=0,...,L-1, has a block Gram matrix whose diagonal block norms are at most C_flat and off-diagonal block norms are at most epsilon_(L,N). Here K_-r=K_r*. The block row/column norm estimate proves

    ||(1/L)sum_(j=0)^(L-1) H_N^(-j) C_N C_N* H_N^j||
        <= C_flat/L + (1-1/L)epsilon_(L,N).                  (6)

By (4), this bounds the average of E_(N,n+j+1)(0)/N for EVERY starting integer n. Partition a time interval of length M into blocks of L and a remainder of size less than L. The remainder costs at most C_flat L/M. Thus (2), first N->infinity at fixed L and then L->infinity, proves

    (NM_N)^-1 sum_(m in I_N) E_(N,m)(0) ->0                 (7)

for any intervals I_N of positive integer times with lengths M_N->infinity. Bounded compact weights in (3) follow by positivity and an enclosing interval of O(N) terms. This uses fixed-lag estimates only, not a propagation estimate at times of order N.

## 3. The inherited one-step parametrix, with explicit smallness

Use Sections 1, 2 and 4 of the hash-pinned `four_branch_parametrix.md`. With x=j/N, y=k/N,

    V_N(j,k)=e(3N/8)/(2 sqrt(N)) sum_(alpha=0)^3
                 e(N S_alpha(x,y)) b_(alpha,N)(x,y),
    b_(alpha,N)=a_(alpha,0)+N^-1 a_(alpha,1),
    ||U_N-V_N||=O(N^-3/2),                                 (8)

where the phases are real smooth on R^2, the amplitudes have uniform-in-N bounds for each fixed number of derivatives on compact sets, and

    S_alpha^0(x,y)=-(3x^2-2x(y+alpha)+3(y+alpha)^2)/8.

The full V_N kernel, including both amplitudes, is exactly periodic in each sampled index. This follows from the phase and amplitude gluing in the source; individual branches are not declared periodic. We retain all four branches, the odd-N scalar, and the actual midpoint symbol.

The same source supplies uniform real-space derivative bounds for g through order four below 10^9, and the C^2 time-Taylor remainder at tau bounded by (10^50/2)tau^2. In g(x,(y+alpha-3x)/4), a second derivative has coefficient sum less than 4 against the derivatives of g. A conservative bound therefore gives, for each coordinate Hessian entry,

    |partial^2(S_alpha-S_alpha^0)|
       <=10^10 tau +(10^50/2)tau^2 < 10^-60 =: eta.         (9)

This bound holds globally on R^2 and for all four branches. Only second derivatives need a numerical smallness constant; higher fixed derivative bounds may have arbitrary finite constants. The fixed physical tau and its forced half-shift are not replaced by a tunable perturbation.

Let C_V denote the displacement-slice construction with V_N. Disjoint column supports and the entrywise consequence of (8) imply

    ||C_U-C_V|| <= sqrt(N) max_jk |U_jk-V_jk|=O(N^-1).

Since ||V_N||<=1+O(N^-3/2), telescoping fixed powers gives

    ||K_(r,N)-C_V* L_(V_N)^r C_V||=O_r(N^-1),              (10)

where L_(V_N) denotes left multiplication by V_N. This avoids multiplying entrywise remainders by the number of internal summation variables.

## 4. One cyclic phase for all fixed lags

Expand the r+2 factors in (1) with V_N. Put t=c-d, use scaled variables c,d in [0,1], and introduce x=(x_0,...,x_(r-1)), x_r=x_0+t. A branch term has phase

    Phi(x;c,d)=S_alpha(x_0+c,x_0)
              -S_beta(x_0+c,x_0+c-d)
              +sum_(j=0)^(r-1) S_(gamma_j)(x_j,x_(j+1)).   (11)

The scaled representatives x_0+c and x_0+c-d are used literally on the real line. Their sampled full kernels equal the required modular entries by (8)'s gluing. Thus no piecewise reduction modulo one or omitted alias is hidden in (11).

Write Phi^0 for the same phase with all S replaced by S^0. Branch indices change its affine part only. If P_r is cyclic coordinate shift (including P_1=I), its internal Hessian is

    H^0=Phi^0_xx=-(3/2)I+(1/4)(P_r+P_r*).                 (12)

For r=1 this is -1; for r=2 the off-diagonal entries are 1/2. Its eigenvalues lie in [-2,-1], and ||(H^0)^-1||_infinity<=1. The last bound follows directly from the maximum-coordinate argument for the strictly diagonally dominant matrix -H^0.

The full Hessian in (x,c,d) satisfies the uniform row-sum estimate

    ||Hess Phi-Hess Phi^0||_infinity <=64 eta < delta,
    delta:=10^-50.                                         (13)

To check the count in (13), each phase correction is composed with two linear forms, whose combined coefficient l1 norm is at most five, and whose combined coefficient at any single variable is at most two. Its Hessian row sum is therefore at most 10 eta. Each variable participates in at most four factors, counting the two exceptional factors and the two incident cyclic links; the bound 64 eta includes repeated-variable r=1,2 cases with spare margin. Symmetry gives the same column-sum bound. It follows that every internal H=Phi_xx is negative definite, -H>= (1-delta)I, and

    ||H^-1||_infinity<=2,
    ||H^-1-(H^0)^-1||_infinity<=2delta.                    (14)

These statements hold on all of R^r and for all real c,d. In particular x->grad_x Phi is one-to-one, proper and onto R^r: strict concavity proves injectivity and properness, and for any ell, the strictly concave coercive function Phi(x)-ell.x attains its unique maximum. This supplies the unique stationary point x_ell(c,d) for every integer alias ell, smoothly in c,d.

## 5. Transversality survives every alias

For any ell in Z^r, define the stationary value

    Psi_ell(c,d)=Phi(x_ell(c,d);c,d)-ell.x_ell(c,d).

Implicit differentiation gives its exact mixed derivative

    Psi_(ell,cd)=Phi_cd - Phi_cx H^-1 Phi_xd,               (15)

evaluated at x_ell. The linear alias term has zero Hessian and contributes no extra term to this formula.

For Phi^0, direct differentiation of the two exceptional factors and the last cyclic link gives

    Phi^0_cd=1/4,
    v:=Phi^0_xc=(e_(r-1)-e_0)/4,
    Phi^0_xd=-v.                                           (16)

For r=1 the displayed v is zero. For r>=2, ||v||_2^2=1/8, ||v||_1=1/2 and ||v||_infinity=1/4. Since -(H^0)^-1 is positive with norm at most one,

    1/8 <= 1/4+v* (H^0)^-1 v <=1/4.                       (17)

These bounds hold independently of branch indices and ell. For reference, eliminating the cat chain gives the sharper value (A_r+1)/(4B_r) when S^r has first row (A_r,B_r); that identity is not needed for the lower bound.

From (13), the perturbation of Phi_cd is at most delta, that of the row Phi_cx has l1 norm at most delta, and that of Phi_xd has infinity norm at most delta. Apply (14) in (15), using ||v||_1<=1/2 and ||Phi_xd||_infinity<=1. The total change from the expression in (17) is at most 5delta. Consequently every reduced phase satisfies

    1/10 <= Psi_(ell,cd) <=1/3.                            (18)

This is global on the external parameter square and includes every discrete alias. No nonstationary branch or arithmetic residue class has been discarded.

## 6. Discrete stationary phase, with the sampled boundaries retained

Choose chi in C_c^infinity(R) with sum_(k in Z) chi(s+k)=1, for example a smooth partition of unity on the circle lifted to a compact interval. The full sampled product of kernels in (1) is N-periodic in each internal index. Therefore its finite cyclic sum equals the sum over all integer internal indices multiplied by product_j chi(x_j). Make this replacement BEFORE expanding into individual branches. This is how the individual nonperiodic phases in (11) acquire smooth compact internal cutoffs without dropping boundary terms.

For a fixed branch list the resulting matrix entry, apart from a bounded scalar, is

    N^(-(r+2)/2) sum_(k in Z^r)
          a_N(k/N;c,d) e(N Phi(k/N;c,d)),                  (19)

where a_N is smooth with common compact internal support and bounded derivatives of every fixed order, uniformly in N and in c,d on a neighborhood of [0,1]^2. Poisson summation is exact and changes (19) into

    N^((r-2)/2) sum_(ell in Z^r)
       integral a_N(x;c,d) e(N[Phi(x;c,d)-ell.x]) dx.       (20)

Only finitely many ell can have a stationary point in the common support as c,d vary in the external compact square: grad_x Phi is bounded there. The cardinality may depend on fixed r and the branch list, never on N. For the remaining sufficiently large aliases, repeated integration by parts with the nonzero gradient gives O_M(N^-M(1+|ell|)^-M) uniformly, and similarly after any fixed number of parameter derivatives. Choose M as large as needed relative to r. A finite number of aliases whose stationary point is outside the support may harmlessly be included in the stationary calculation below.

For each retained ell, the unique nondegenerate stationary point and (14) give

    integral a_N e(N[Phi-ell.x])
       =N^(-r/2) e(N Psi_ell) b_(ell,N)(c,d)
          +O_r(N^(-r/2-1)),                               (21)

uniformly in the external parameters. The b_(ell,N) are smooth with uniformly bounded derivatives. They vanish to the necessary orders if the stationary point is outside the support.

For clarity, the elementary stationary-phase input used in (21) can be proved uniformly as follows. Cut off a fixed small neighborhood of the smooth stationary point; outside it integrate by parts. The parameter-dependent Morse change of variables makes the phase exactly Psi_ell-|y|^2/2. Its Jacobian at zero is |det(-H)|^-1/2 and all required derivatives are uniformly bounded on the compact parameter set. For the compact smooth transformed amplitude b(y), Gaussian Fourier inversion gives

    integral e^(-pi i N |y|^2) b(y)dy
     =e^(-pi i r/4) N^(-r/2)
          integral e^(pi i |xi|^2/N) bhat(xi) dxi.

Subtract b(0); the error is bounded by (pi/N) integral |xi|^2 |bhat(xi)| dxi. Smooth compact amplitudes and their parameter derivatives bound this integral uniformly. Gaussian damping justifies the oscillatory inversion. This proves the leading term and the stated uniform remainder, including parameters for which the amplitude vanishes at the critical point. No external long-time trace theorem is used.

Combining (20)--(21), each fixed branch list contributes a finite sum of matrices

    N^-1 b_(ell,N)(c,d) e(N Psi_ell(c,d))                   (22)

plus entrywise O_r(N^-2). There are finitely many branch lists for fixed r. The total remainder therefore has operator norm O_r(N^-1). The number of links is fixed at this step; it is not being set to a Heisenberg time.

## 7. Alias-safe TT* for the resulting charge matrix

Here the mixed derivative bounds (18) directly give the discrete norm estimate, without a small-amplitude or random-phase argument. Let B_N have the form (22), and let c=i/N, c'=i'/N. For i!=i', put d0=|c-c'| and psi(y)=Psi_ell(c,y)-Psi_ell(c',y). Its derivative has constant sign and lies in absolute value between d0/10 and d0/3. The discrete phase increments N[psi((j+1)/N)-psi(j/N)] satisfy the same bounds; they are less than 1/3 and stay at distance at least d0/10 from every integer.

Their total variation is O(d0), because psi_yy=O(d0). The product amplitude has uniformly bounded sup norm and variation. Summation by parts with denominator e(Delta_j)-1 therefore bounds the unnormalized column sum by O(1/d0), including its two endpoint terms. Hence

    |(B_N B_N*)_(ii)|=O(N^-1),
    |(B_N B_N*)_(ii')| <= C/[N |i-i'|],  i!=i'.           (23)

Schur's row/column bound yields ||B_N||^2=O(log(2N)/N). This is the proof of the source's discrete norm lemma with the sufficient upper bound 1/3<1/2 in place of its more conservative 1/4. The proof explicitly excludes all nonzero integer sampling aliases. The smooth amplitudes in (22) need not vanish at j=0,N-1 because the summation-by-parts endpoint terms are retained.

The finite branch/alias sum, its O_r(N^-1) error and (10) now prove (2). Sections 1--2 then give (3).

## 8. What remains for T16

This result has q=1 and a single pinch. The supplied native annealed theorem allows its complete occupation subtraction; it does not add a Hamming or high-switch mask to (3).

To reach T16, one still needs control of occupation-subtracted traces with D insertions separated by arbitrary coherent links, in the full switch expansion and with high-Hamming coefficient extraction and the low-switch subtraction retained. At z=1-A log(N)/N, the binomial expansion in D has typical insertion count of order log N for m~N. Fixed-r constants in (2) are not bounds for that insertion hierarchy, and an unmasked norm bound cannot be applied to an arbitrary path subset. Deconvolving the factor z^m also incurs polynomial powers of N. None of these steps is supplied by (2), (3), or the native consecutive-block theorem.

The balanced microscopic law, deterministic full offcharge comparison, higher factorial TRACE-005 and BGS remain open. The candidate one-pinch proof requires independent review of the exact source assumptions and Sections 3--7 before promotion. Finite controls test identities and arithmetic only, not this analytic limit.
