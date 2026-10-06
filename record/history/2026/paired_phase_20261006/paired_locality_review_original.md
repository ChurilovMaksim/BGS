# Independent audit: branch quotient and fixed-coupling winding locality

Date: 6 October 2026. Independent reading and derivation in a fresh worker, without editing either author proof or canonical sources.

## Normalized claim and primary verdict

**Primary verdict: proved as written, for the exact target P1–P8 and L1–L7.**

The target is the following pair of statements.

1. For the prescribed four-branch Hamilton–Jacobi construction, at the unchanged coupling and with the physical trace restricted to odd positive N, the integer-translation quotient has exactly 4^m identical copies of each physical cat label. Its quadratic refinement has a perfect pairing. Removing those copies preserves the accepted 4^-m finite-reciprocity average and 8^-m global-integral prefactor, and yields P7 and the selected-character identity P8.
2. For every m >= 1, the actual stationary-action correction has the stated unit-winding locality bounds. Its chosen defect has a well-defined bounded-correction infinite-chain limit on T², satisfying L1 and L2. For every positive integer N, the phase-only selected coefficient is the Fourier coefficient of the one fixed pushforward probability measure, with uniform error O(N 2^(-m/2)).

There is no load-bearing missing implication in those statements. There is one **non-load-bearing wording correction** in the separate first-response discussion: P10 is the normalized derivative, with the actual derivative equal to iN times its displayed expression. That issue does not change P1–P8, L1–L7, or the claimed resonant vanishing.

This verdict is an internal mathematical audit, not external refereeing or formal verification. It inherits the accepted physical finite-order WKB/contour representation within its stated scope. It does not independently re-audit the full contour theorem, all transport recursions, or TRACE-017's complete operator comparison.

## Pinned artifacts and provenance

Author bytes reviewed:

- paired_character_identity.md: SHA-256 ff4c7af878c1964a8fb135bc7b50385204f65c2ba8c129cca6b43015f27b9a7e
- winding_defect_locality.md: SHA-256 bdbe3917626ae75e77c0d55299200ea381b2e6f09a421649fc04741a59045a1f

The manifest's mathematical sources match the live /workspace/shared/BGS copies inspected, including four_branch_parametrix.md, fixed_map_path_model.md, exact_gaussian_reciprocity.md, global_rotated_box_trace.md, rotated_local_first_loop.md, and the credited prior grid source frozen_periodic_point_annihilator.md.

Five status/index files in the live BGS directory no longer match the manifest: RESEARCH.md, record/claim_ledger.md, record/claims.json, mathematics/results.md, and mathematics/open_questions.md. Expected and observed hashes are retained in check_results.json. This is recorded as provenance drift, not silently reconciled or represented as a mathematical discrepancy. The observed status still keeps TRACE-005 and BGS open. All author bytes and all manifest-pinned load-bearing mathematical sources were unchanged at final verification.

## Dependency graph

- Actual raw symbol and global real HJ graph from fixed_map_path_model.md and four_branch_parametrix.md Sections 1, 2, 4 and the dependency boundary.
  - Integer phase and transport gluing -> P1–P3 -> free 4^m quotient -> physical label group G_m.
  - Source real C² bounds -> per-edge eta bound -> small nearest-neighbour Hessian -> L4 -> finite envelope identities and L6–L7.
- Cat generating function and symplectic integer matrix S.
  - Telescoping action -> P5 -> polarization P6 -> perfect pairing.
  - Accepted exact Gaussian reciprocity, G6–G7 -> normalized P7 -> purely algebraic P8.
  - Infinite Green kernel + integer HJ gluing + contraction -> L8 and periodic D_infty.
  - Weighted resolvent + Green periodization -> L1.
  - Periodic local coefficient bound + hyperbolic growth -> Hölder L2.
- Prior exact Pell/grid theorem, explicitly credited and checked in its canonical source.
  - Uniform grid cell comparison + L1/L2 -> L3 -> muhat_tau(-N).

No Fourier-decay theorem or full-amplitude cancellation estimate appears as a leaf. Those remain open rather than being implicitly assumed.

## Obligation matrix

| Obligation | Result | Decisive check |
|---|---|---|
| Actual phase conventions and integer gluing | Passed | Direct quadratic P1/P2 calculation; HJ uniqueness with integral momentum shifts |
| Quotient action, multiplicity, physical group | Passed | Center translation; z+4w changes nu by -B_m w; orbit count and cat initial point |
| m=1,2 repeated neighbours and Smith groups | Passed | Exact matrices and exhaustive rational controls below |
| Quadratic refinement, lift independence, polarization sign | Passed | Symplectic identity gives the residual integer -n_z,p n_d,q |
| Perfect pairing and arbitrary N algebra | Passed | Every integer n is (S^m-I)d for a real lift; no coprimality assumption |
| 4^-m/8^-m normalization and Maslov/root phase | Passed | Direct G6/G7 substitution; alpha=1 for global cat Fresnel integrals |
| Actual real-parameter interpolation | Passed | S_r(t,x,y)=S_0(t,x,y+r) with globally uniform source bound |
| Weighted resolvent and branch derivative bounds | Passed | Neumann estimate and resolvent identity; m=1,2 retained |
| Infinite correction existence, periodicity, cycle gluing | Passed | Bounded contraction; local correction gluing; exact periodization |
| L1 constants | Passed | Summable background difference with 216 eta 2^-m bound |
| Hölder pullback and L2 constant | Passed | Periodic local gradient and weighted sum; 10^4 eta is ample |
| Grid aliases, quadrature and Fourier sign | Passed | Exact rectangle, cell bound, positive phase gives muhat(-N) |
| Literal derivative wording immediately before P10 | Failed, non-load-bearing wording | Derivative has the factor iN |
| Full determinant, transport and quantum-box weight | Out of scope | Not supplied or inferred from phase-only proof |
| Fourier decay, all displacements, torsion sectors, signed hierarchy | Out of scope | Remain explicit open obligations |

## Detailed decisive checks

### 1. Gluing, quotient, and normalization

The two quadratic differences in P1 and P2 are correct. P1 has matching x-gradients and P2 shifts that gradient by the integer l. HJ uniqueness therefore preserves the differences for the actual periodic symbol at fixed tau. The unchanged higher phase derivatives and periodic symbol coefficients justify transport gluing. No new complex multiplier is introduced.

P3 gives x^0_(s,nu') = x^0_(r,nu) - z. Replacing z by z+4w changes nu' by -B_m w. The difference between two representatives of the same winding class moves the center by 4w. Consequently a fixed point of the finite translation action forces z=0 modulo 4. This establishes exact multiplicity; it does not invoke cancellation.

The initial cat point is precisely (x_0, (x_1+r_0-3x_0)/4) modulo integers. Integer translations preserve it. Conversely, the unwrapped trajectory of any cat fixed point provides an integer final branch and initial winding, which can be reduced using the same gluing. Thus the quotient is the physical G_m, not the winding quotient alone.

The accepted global-integral prefactor is e(3mN/8) N^(m/2) 8^-m. Summing identical copies changes it to e(3mN/8) N^(m/2) 2^-m. Substitution of the definition of alpha produces exactly zeta_(N,m)=e(3mN/8)e^(-i pi m/4) and D_m^-1/2 in P7.

At tau=0,

I_z = e(NQ_m(z)) e^(-i pi m/4) N^(-m/2) 2^m / sqrt(D_m),

so alpha=1 exactly for the global Abel/Fresnel integrals. The paper correctly does not assert this exact equality for truncated boxes.

### 2. Quadratic action and signs

For the unwrapped cat trajectory the one-step generating function is -1/2 times the increment of qp. Choosing the final branch n_q and the initial winding n_p therefore gives

F_0 = 1/2 (q n_p - p n_q - n_q n_p),

which is P5. In the polarization calculation, symplecticity gives

omega(z,Ld) - omega(d,Lz) = -omega(Lz,Ld),  L=S^m-I.

Hence the polarization equals omega(z,Ld) minus the integer n_z,p n_d,q. This verifies the sign in P6. Since L is even integral and A is unimodular symplectic, integer-lift changes preserve both Q modulo 1 and the pairing. The refinement is homogeneous quadratic.

Perfection follows directly by allowing every n in Z² as Ld. If omega(z,n) is integral for all such n, z is integral. No determinant inverse modulo N is used.

The expansion with first point z+d gives the character e(+N B(z,d)); with the stated negative-sign Fourier transform this selects -Nd. Thus P8 has the correct sign and its D^-1 average is the squared D^-1/2 trace normalization.

For arbitrary alpha and arbitrary integer N this is an identity for the corresponding normalized quadratic sum. When its left side is written as the physical WKB trace, alpha must be the actual P7 weight and N remains odd, as in the source construction. No claim about an even-dimensional physical quantization is warranted or needed.

### 3. Small dimensions

At m=1:

- B_1=[4], K_0=[1], D_1=4.
- The winding group is Z/4 and the physical group is (Z/2)^2.
- The 16 listed branch/winding terms give four physical labels, four copies each.
- The periodic Green column is [1].
- The unit-winding lift is (1,-1/2), hence d_1=(0,1/2) modulo Z².
- The repeated-edge Hessian is R_xx+2R_xy+R_yy, bounded by 4 eta.

At m=2:

- B_2=[[6,-2],[-2,6]], K_0=[[3/2,-1/2],[-1/2,3/2]], D_2=32.
- The winding Smith factors are (2,16); the physical factors are (4,8).
- The 512 listed terms give 32 physical labels, 16 copies each.
- The periodic Green column is [3/4,1/4].
- The unit-winding lift is (3/4,-1/2).
- The two edge mixed Hessians combine into the one neighbour entry. Its weighted contribution is 4 eta; with the diagonal the bound is 6 eta.

These checks exclude substituting the winding group for the physical quadratic group and exclude accidentally omitting a repeated neighbour.

### 4. Actual interpolation and finite locality

Real r is a valid interpolation: the source HJ initial data and equation give S_r(t,x,y)=S_0(t,x,y+r), and the uniform real graph/source estimates apply for all real parameters. It is not necessary to extend an integer gluing identity to noninteger shifts.

The source's first-time-derivative bound and C² time remainder imply the advertised per-edge bound eta=10^10 tau+10^50 tau². The linear composition p_0=(y+r-3x)/4 has bounded coefficients, so 10^10 safely bounds its required first-response C² derivatives after the factor 1/(2pi).

The unweighted row sum of K_0^-1 is one. The weighted norm is at most two, including m=1,2. Accumulating edge Hessians gives ||E||_w <= 6 eta. Consequently

||G||_w <= 2/(1-12 eta) <= 3,
||G-G_0||_w <= ||G||_w ||E||_w ||G_0||_w <= 36 eta.

These bounds also hold for averages of Hessians. Strict concavity and the contraction equation provide the unique real stationary point for each real interpolation parameter. The envelope theorem gives partial_nu F=x and partial_nu x=G. Thus the winding defect is exactly the integral in L6, not a Taylor approximation.

For branch differentiation the base forcing f has weighted norm <=7/4. The nonlinear mixed forcing has norm <=3 eta, since real branch differentiation is y differentiation of its edge correction. Hence

||(partial_r x_tau)-(partial_r x_0)||_w <= 36 eta (7/4)+3(3 eta)=72 eta.

For the canonical code ranges, the frozen-tail change is at most

(6*72+4*36) eta * 2 sum_(k>R) 2^-k = 1152 eta 2^-R.

### 5. Infinite-chain construction and finite-cycle identification

The infinite Green kernel g_j=(1/sqrt(2)) lambda^(-|j|) solves K_0 g=delta_0 and has total mass one. For each background b, the local nonlinear gradient has sup norm <=2 eta and Lipschitz constant <=4 eta. Its convolution map is a contraction on bounded corrections, even though the unwrapped cat background itself is unbounded. Only the correction is required to lie in ell-infinity.

Integer changes in the initial lift give integer cat position and momentum changes at every positive and negative time. The exact correction identity R_0(x+a,y+3a+4b)=R_0(x,y) therefore preserves the local equation. This establishes periodicity of D_infty. Continuity in s follows from the same contraction; continuity in z is provided by the separate Hölder estimate rather than an invalid sup-norm continuity claim for the whole unwrapped trajectory.

For a period-m label, the background at j+m differs from that at j by exactly such an integer cat increment. Periodizing g therefore makes the equation periodic, and uniqueness identifies its solution with the finite-cycle winding interpolation. In the unwrapped finite representative the final branch is n_q and the initial winding is n_p. Adding s to that winding changes the cat stationary positions by s times the periodized Green column, with the same final-branch gluing. This supplies the exact connection to L6.

For changes of the bounded background,

D_b u = (K_0-E)^-1 E,

so its kernel is bounded by 18 eta 2^(-|j|). This derivative also defines a bounded operator on ell-infinity, allowing the infinitely supported, bounded periodization difference. The convolution estimate in the manuscript yields

sum_j 2^(-|j|)lambda^(-|j+L|) <= [(1+2/lambda)/(1-2/lambda)]2^(-|L|) < 3*2^(-|L|).

The sum over nonzero period shifts is at most 4*2^-m. Discarding the helpful factor 1/sqrt(2) gives 18*3*4 eta 2^-m=216 eta 2^-m. Thus L1 holds for all m>=1, including the small cycles.

### 6. Hölder and quadrature constants

With v_j=s g_j+u_j fixed during comparison, the local gradient at site j is a periodic function of the cat variables at that site. Its outgoing arguments are (q_j+v_j,3q_j+4p_j+v_(j+1)); its incoming arguments are (3q_j-4p_j+v_(j-1),q_j+v_j). The C² edge bound controls its coordinate derivatives by a fixed multiple of eta; 32 eta is more than sufficient for a torus-distance Lipschitz bound and bounded-difference estimate. The weighted averaged resolvent of norm at most three then gives the manuscript's 96 eta sum.

For alpha=log(2)/log(lambda) and 0<t<=1, splitting at R=floor(log(1/t)/log(lambda)) bounds the displayed geometric sum by

[2 lambda/(lambda-2)+4] t^alpha < 10 t^alpha.

The factor 4 inside the minimum costs 4^alpha. Thus 96*10*4^alpha < 10^4, leaving ample room in L2. For larger t the boundedness of u provides the estimate. This proves actual Hölder continuity without asserting C¹ regularity.

The Pell formulas and exact rectangular grids agree with the credited canonical source. U_m >= lambda^(m/2)/2 holds also at m=1,2. For integer N the function e(N[q+D_infty]) is well-defined and Hölder on the torus even though q alone is a coordinate lift. One can take

[f_N]_alpha <= 2pi N (1+10^4 eta)

for the usual flat torus distance of diameter less than one. Comparing each grid sample with its rectangular cell gives a bound of this quantity times (sqrt(2)/U_m)^alpha, hence O(N 2^(-m/2)). L1 contributes at most 432pi N eta 2^-m. Both constants are independent of m and N; all finite-grid aliases are included.

Finally B(z,d_m)=q, and the coefficient has the positive phase e(N[q+D_infty]). With muhat(k)=integral e(-kt)dmu, its integral is exactly muhat(-N). The factor e(NQ(d_m)) belongs to the complete displacement summand in P8, not to the selected coefficient K itself; the paper's phase-only conclusion is consistent with this distinction.

## Bounded independent execution

Run from the shared workspace:

python /workspace/shared/bgs_paired_box_cancellation/independent_review/check_review.py

Results are in check_results.json. The script is independently written for this review and was not copied from the author's checker.

- Symbolic polynomial verification of P1/P2.
- Exhaustive rational branch/winding and cat-action checks at m=1,2: 528 listed terms, and 1,040 polarization pairs, with perfect-pairing annihilators checked.
- Sixteen 80-decimal physical metaplectic trace comparisons for m=1,2,3,4 and N=1,3,5,7, including the complete zeta phase. These are floating diagnostics only, all with absolute error below 10^-70.
- Exact rational weighted-resolvent controls at m=1,...,12 and eta=10^-4, for both signs of the per-edge maximal-entry test Hessian. These support the repeated-neighbour implementation and constants but do not replace the uniform norm proof for arbitrary Hessians.
- SHA-256 provenance comparison with the author manifest. An initial fail-closed run stopped at the first status-file hash mismatch; the final checker records every mismatch explicitly while retaining all mathematical assertions.

Neither bounded execution nor agreement with another reviewer is used as proof of the infinite-chain or asymptotic statements.

## Exact correction and remaining boundary

The literal derivative of the selected phase-only coefficient at t=0 is

iN * D_m^-1 sum_z e(N B_m(z,d)) [C_m(z+d)-C_m(z)].

Therefore the wording before P10 should say “the normalized selected first derivative, divided by iN” or display that factor. The translation identity itself is exact and still vanishes on the stated resonant sectors. This is a local wording/normalization repair, not a restriction of the target theorem.

No target repair is required. The strongest safe conclusion is the exact quotient and character reduction, plus the fixed-tau phase-only Fourier-measure reduction with a uniform exponentially small finite-cycle/quadrature error. The limiting measure's Fourier decay is not established. Transport, determinant and quantum-box weights are not bounded by this proof. Other displacements, odd-N torsion sectors, the signed displacement/time sum and TRACE-005 remain unresolved.

The cheapest next mathematical check is an exact regularity or Fourier-decay criterion for this explicitly defined H_tau or mu_tau, proved from the actual nonlinear equation. Closeness to the coordinate q or positive variance of initial jets cannot substitute for it. Any full-weight extension must independently control the omitted amplitude factors.
