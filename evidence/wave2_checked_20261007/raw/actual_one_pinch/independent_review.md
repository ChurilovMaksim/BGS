# Independent audit: actual fixed-lag overlap and unmasked one-pinch band

7 October 2026. Fresh reconstruction in an isolated reviewer task. No source repository files were edited, no further agents were started, and no finite computation is used as an asymptotic proof.

**Primary verdict: proved as written.** The candidate fixed-lag estimate and its positive compact-band consequence are supported by the actual argument. Combined with the separately accepted annealed deletion theorem, they close the unmasked, occupation-subtracted one-pinch compact-band limit. I found no substantive missing implication in the candidate's Sections 3–7. This verdict does not include separated insertions, Hamming/switch masks, T16, TRACE-005, or BGS.

The inherited parametrix is an accepted project input at the pinned canonical revision. This review checks the exact properties newly used here, rather than restarting its entire historical baseline audit. The signed consequence uses the annealed result within its smooth-weight scope.

## 1. Exact claim card and provenance

Let the literal odd-dimensional family be

    U_N = exp(i tau N A_N) M_N,  tau = 10^-80,

with the unchanged ordinary physical midpoint symbol, its scalar centering, and its raw Weyl aliases. On End(C^N) use ordinary Hilbert–Schmidt inner product. Define A_c by

    (A_c)_(y+c,y) = (U_N)_(y+c,y),
    C_N e_c = A_c*,  H_N X = U_N X,
    K_(r,N) = C_N* H_N^r C_N.

The exact conclusion, for each fixed integer r >= 1, is

    ||K_(r,N)|| <= C_r sqrt(log(2N)/N).

The constants depend on the fixed map and r, not N. No uniformity for growing r is needed or asserted. It follows that the untwisted echo

    E_(N,m)(0) = (1/N) sum_b |tr(U_N^(m-1) Z_b U_N Z_b*)|^2

satisfies

    (N M_N)^-1 sum_(m in I_N) E_(N,m)(0) -> 0

for arbitrary positive-time integer intervals I_N of lengths M_N -> infinity. In particular, for any fixed bounded weight supported in a positive compact band,

    N^-2 sum_m |w(m/N)| E_(N,m)(0) -> 0.

For the signed consequence take w in C_c^infinity((a,b)), 0 < a < b < infinity, which is the scope of the separately accepted annealed theorem.

Audited candidate: `packet/actual_fixed_lag_overlap.md`, equations (1)–(23), all 200 lines. Frozen Library item: `libfile_6f84eea055f08191869065d582c6e52c`, backing `file_000000003ee881f5817080e205dc7aa0`, 44,596 bytes, archive SHA256 `e946093acf988c637f57459884e1ede0099badedf7b682f58396441a9396bda4`. Materialization used the current Library resolved-reference flow and persisted the supplied identity/version attributes.

Canonical BGS checkout is clean at `129c676b8e6457e7e5f1bd6f786b3939cbd84653`. Each of the six packet source copies matches its `source_bindings.json` hash and the corresponding canonical file. The review does not promote repository status or assert priority.

## 2. Dependency graph

1. Literal finite-N definitions and character orthogonality give the slice-frame identity and exact overlap matrix.
2. Accepted `four_branch_parametrix.md`, Sections 1–2 and 4, gives four sampled branches with both transport amplitudes, exact sampled gluing, operator remainder O(N^-3/2), global C^2 phase smallness at literal tau, and all fixed smooth derivative bounds on bounded charts.
3. Fixed-power operator comparison reduces K_(r,N) to that parametrix, with error O_r(N^-1).
4. Direct cyclic cat-phase algebra gives a uniformly negative internal Hessian and a positive reduced charge mixed derivative. The specified-time perturbation preserves both globally.
5. Cutoff-before-expansion, exact Poisson summation, all-alias stationary phase, and summable tails reduce each branch to finitely many N^-1 oscillatory charge matrices plus O_r(N^-2) entry error.
6. Alias-safe discrete summation by parts and TT* give O_r(sqrt(log N/N)) operator norms.
7. A finite-block Gram estimate, followed by N -> infinity at fixed block length and then block length -> infinity, gives the all-starting-time positive echo limit.
8. Separately accepted `../bgs_wave2_echo_generator/one_pinch_averaged_lemma.md`, L1–L2, removes the full occupation-phase average for smooth compact weights. Its independent review is a dependency receipt, not a new proof furnished by this packet.

All new analytic leaves in steps 4–7 are proved internally. No external long-time trace theorem, pointwise microscopic pair-density bound, Egorov estimate, or classical mixing theorem is inserted into those steps.

## 3. Orientation, frame, and approximation

With the inner product linear in its second argument,

    (C_N* X)_c = tr(A_c X).

Consequently

    (K_(r,N))_(c,d) = tr(A_c U_N^r A_d*)
      = sum_x U_(x+c,x) conjugate(U_(x+c,x+c-d))
               (U_N^r)_(x,x+c-d).

This is candidate (1), with left multiplication by U, not adjoint evolution. The row-minus-column slice label is the negative of the source charge label; the complete character sum is unchanged. It does not change any masked source convention.

Since Z_b U Z_b* = sum_c e_N(bc) A_c, Parseval gives

    E_(N,m)(0) = sum_c |tr(U^(m-1) A_c)|^2
               = N ||C_N* (U^(m-1)/sqrt(N))||^2.

The vectors U^n/sqrt(N) have ordinary HS norm one. Slice supports are disjoint, so C_N has orthogonal columns and ||C_N||^2 is the maximal slice squared norm. The parametrix supplies |U_jk| <= C/sqrt(N), eventually, hence this norm is bounded independently of N.

For the operator remainder U-V = O(N^-3/2), the slice-synthesis error is at most sqrt(N) max_jk |(U-V)_jk| = O(N^-1). Since ||V|| <= 1+O(N^-3/2), fixed-power telescoping gives the claimed K comparison O_r(N^-1). This is operator comparison before branch expansion; no uncontrolled accumulation of entrywise errors over r internal sums occurs.

## 4. Independent all-r Hessian calculation

Write t=c-d, use x_r=x_0+t, and temporarily ignore branch affine terms. For the unshifted cat phase

    S^0(x,y) = -3x^2/8 + xy/4 - 3y^2/8,

the difference of the two exceptional terms is

    S^0(x_0+c,x_0)-S^0(x_0+c,x_0+t)
      = x_0 t/2 - ct/4 + 3t^2/8.

Replacing the last cyclic second argument x_0 by x_0+t changes that link by

    (x_(r-1)/4-3x_0/4)t - 3t^2/8.

Thus, with x_(j+1) cyclic in the following sum,

    Phi^0 = -3/4 sum_j x_j^2 + 1/4 sum_j x_j x_(j+1)
            + (c-d)(x_(r-1)-x_0)/4 - c(c-d)/4
            + affine branch terms.

This identity applies also to r=1 and r=2. Branch offsets add affine terms because S_alpha^0-S_0^0 = alpha x/4 - 3alpha y/4 - 3alpha^2/8. Hence they do not change any Hessian. The displayed identity proves, for every r,

    H^0 = -(3/2) I + (P_r+P_r*)/4,
    Phi^0_cd = 1/4,
    Phi^0_xc = v = (e_(r-1)-e_0)/4,
    Phi^0_xd = -v.

At r=1, H^0=-1 and v=0. At r=2,

    H^0 = [[-3/2, 1/2], [1/2, -3/2]],  v=(-1,1)/4.

The reduced mixed derivatives are respectively 1/4 and 3/16. These minimum cases are not treated by a false generic-neighbor count.

The cyclic shift spectrum gives spec(H^0) contained in [-2,-1]. Strict diagonal dominance gives ||(H^0)^-1||_infinity <= 1, and symmetry gives its ordinary spectral bound as well. Since ||v||_2^2 <= 1/8,

    1/8 <= 1/4 + v* (H^0)^-1 v <= 1/4.

The actual phase corrections satisfy the source's global Hessian bound at fixed tau. Composition with the exceptional linear forms costs at most 10 eta per participating factor. Each variable participates in at most four factors, including repeated-variable cases; 64 eta is safe. With eta=10^-60 and delta=10^-50, the full Hessian perturbation is strictly below delta in row/column-sum norm. Its internal block remains negative definite and its inverse remains bounded by two in infinity norm.

For an arbitrary alias ell, strict concavity and coercivity give a unique global critical point of Phi-ell.x. Implicit differentiation yields

    Psi_(ell,cd) = Phi_cd - Phi_cx (Phi_xx)^-1 Phi_xd.

No Hessian comes from the linear alias term. Using the perturbed inverse and the row/infinity bounds gives a change at most 5 delta from the cat expression. Therefore 1/10 <= Psi_(ell,cd) <= 1/3 for every branch and every alias. No stationary degeneracy or exceptional arithmetic residue class remains.

## 5. Sampled gluing and all-alias stationary phase

The source's real phase identities are

    S_(alpha+4)-S_alpha = x-3y-3alpha-6,
    S_alpha(x+1,y)-S_(alpha-3)(x,y) = -2alpha-2y+3,
    S_alpha(x,y+1) = S_(alpha+1)(x,y).

At sampled x=j/N,y=k/N their first two differences multiplied by N are integers. The transport equations preserve the matching gluing of a_0 and a_1: integer changes in S_x preserve all periodic symbol derivatives and the higher x derivatives, and the initial amplitudes have the matching identities. Thus the FULL four-branch V_N is exactly periodic in each sampled index, including lattice wraparound. This is a property of V_N itself, not merely U_N or the leading amplitude.

Let chi be a compact smooth lifted partition with sum_(k in Z) chi(s+k)=1. Before branch splitting, the complete sampled product entering K is periodic in every internal index. Therefore multiplying its integer-lattice extension by product_j chi(x_j) reproduces its finite cyclic sum exactly. After this equality is established, individual branch phases may be nonperiodic without causing a boundary error. The candidate takes these operations in the correct order.

For a fixed r and branch list, the resulting amplitude is smooth, uniformly bounded in every fixed derivative, and supported in one common compact internal set. Poisson summation produces

    N^((r-2)/2) sum_(ell in Z^r)
      integral a_N(x;c,d) e(N[Phi(x;c,d)-ell.x]) dx.

Only finitely many aliases can have a critical point meeting this common support as c,d vary over their compact square. Their number can depend on fixed r, which is permitted. For the remaining large aliases, the gradient has size comparable to |ell| on the support. Repeated integration by parts gives a summable O(N^-M (1+|ell|)^-M) tail; choose M greater than r and sufficiently large for the prefactor. If parameter derivatives are wanted, additional integrations absorb the corresponding powers of N.

For each retained alias, uniform negative definiteness and compactness of the parameter set give a uniform local Morse chart at its smoothly varying critical point. Outside a fixed critical neighborhood, strong concavity bounds the gradient away from zero. Gaussian Fourier inversion in the Morse chart gives the leading N^-r/2 term and error O(N^-r/2-1), uniformly even when the critical point crosses the cutoff boundary. A compact smooth cutoff vanishes to all orders at that boundary; no discontinuous stationary-point selection or boundary stationary phase is being used.

The prefactor therefore gives finitely many entries

    N^-1 b_(ell,N)(c,d) e(N Psi_ell(c,d))

with uniform smooth amplitude bounds, plus O_r(N^-2) entry error. Its matrix operator norm is O_r(N^-1). The Gaussian normalization and powers of N are consistent.

## 6. Discrete TT* and the order of limits

For two rows c=i/N,c'=i'/N, set d0=|c-c'| and psi(y)=Psi_ell(c,y)-Psi_ell(c',y). The established mixed derivative interval implies that psi' has constant sign and magnitude between d0/10 and d0/3. The sampled increments

    Delta_j = N[psi((j+1)/N)-psi(j/N)]

have the same interval. Their distance from every integer is at least d0/10: the upper bound is below 1/3, so nonzero sampling aliases are explicitly excluded. Their total variation is O(d0), using the bounded third phase derivatives; the product amplitude has O(1) sup norm and total variation.

Discrete summation by parts with denominator e(Delta_j)-1 has endpoint cost O(1/d0), amplitude-variation cost O(1/d0), and reciprocal-denominator variation O(d0)/d0^2 = O(1/d0). This does not require the external amplitude to vanish at sampled endpoints. Consequently TT* has diagonal entries O(1/N) and off-diagonal entries bounded by C/[N |i-i'|]. The row and column harmonic sums give ||B_N||^2=O(log(2N)/N). The finite branch/alias sum and its O_r(N^-1) errors prove the fixed-lag estimate.

For the time consequence, the synthesis map with blocks H_N^-j C_N has diagonal Gram norm bounded by C_flat and off-diagonal norms bounded by max_(1<=r<L)||K_(r,N)||. Its block row/column estimate gives

    ||(1/L) sum_(j=0)^(L-1) H_N^-j C_N C_N* H_N^j||
      <= C_flat/L + (1-1/L) max_(1<=r<L)||K_(r,N)||.

The associated echo average is bounded for every starting time because its orbit vector is a unit vector. The remainder from partitioning an interval into blocks of fixed L costs at most C_flat L/M_N. First N tends to infinity at this fixed L; then L tends to infinity. This uses no growing-r estimate and no Heisenberg-time approximation. Positivity then handles arbitrary bounded positive-compact-band weights at the original N^-2 normalization.

## 7. Obligation matrix and finite evidence

- Exact model, scalar centering, raw half-shift and odd/composite aliases: passed against the frozen model and exact generator reconstruction.
- Slice orientation, left/right multiplication, HS normalization and echo factor N: passed by direct derivation.
- Parametrix error transfer and both-amplitude sampled gluing: passed at the inherited accepted input's stated scope.
- Internal Hessian and closing-link mixed vectors for all r, including r=1,2: passed by the displayed all-r polynomial identity.
- Literal fixed-tau perturbation and alias-independent reduced Hessian bounds: passed.
- All lattice aliases, compact cutoffs and cutoff-crossing stationary points: passed.
- N powers, stationary remainder and matrix error norm: passed.
- TT* nonzero integer-alias exclusion and endpoint terms: passed.
- Fixed-r versus long-time limit order: passed.
- Signed occupation-subtracted corollary: passed using the separately accepted annealed theorem, for its smooth compact weights.
- Separated insertions, growing insertion hierarchy, Hamming/high-switch masks, T16 and BGS: out of scope and remain open.

The packet's `check_overlap.py` and serialized normal/optimized reports were inspected. The 129 controls cover Gaussian-rational fixtures at N=3,5, cyclic Hessian cases r=1,...,16, and rational constant slack. They implement the stated bounded checks and expressly do not certify WKB, stationary phase, or a limit. I did not rerun this duplicate finite suite; the decisive Hessian conclusion above is an all-r analytic derivation, not extrapolation from those 16 cases.

Executed read-only checks included `git rev-parse HEAD`, `git status --short`, `sha256sum` on the materialized archive, and a Python hash comparison of every bound source copy against both the manifest and canonical source. Applicable canonical governance/status sources were read. No baseline full build, formal certificate, broad source search, or source mutation was performed.

## 8. Remaining gap, safe statement, and next action

There is no identified gap in the audited one-pinch argument. The safe result is the fixed-lag overlap theorem, all-starting-time interval average, and unmasked occupation-subtracted smooth compact-band one-pinch limit for the unchanged literal model.

There is no compact-band rate from this double-limit argument, since no growth law for C_r is supplied. No rate or practical startup should be added during integration. The positive consequence is valid for bounded compact-band weights; the signed consequence should keep the smooth-weight hypothesis of the imported annealed theorem.

The cheapest next action is parent-side integration of this bounded theorem with its source hashes and this independent audit, while retaining the explicit exclusion of arbitrary separated D insertions, growing insertion counts, coefficient masks, and boundary deconvolution. Those are the earliest still-open implications toward T16; they are not defects in the present theorem.
