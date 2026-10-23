# Independent audit: exact full balanced-pair Schur reduction

7 October 2026. Fresh-context independent internal audit. Canonical BGS and the author directory were read-only; only this separate review directory was written. This is neither an external referee certificate nor a formal proof certificate.

## Normalized claim and primary verdict

**Primary verdict: proved as written.** This verdict covers the exact finite-dimensional reductions, the equivalence of the two proposed *unproved* limiting criteria, the boundary marginal, and the two negative controls in the frozen candidate. It does **not** assert that either limiting criterion holds for the prescribed map.

The audit target is `pinned/bgs_balanced_phase_closure/candidate_v1.md`, SHA-256
`736cce3e0129c8252edba22d6abeb201528f5cc0d3780ac9efa6d70ecb9330fe`.
The parent supplied this hash before the review. `source_manifest.json` records exact source snapshots, authority files and the observed canonical commit `d37c92e563d10d25bb1d6ab85bedffc1f160f773`, with its concurrent dirty state. The candidate's own source-manifest hashes all matched the source files at the review's comparison time.

There is no required mathematical correction to (1)–(21). The safe promotion is an **exact pair-only reduction with an OPEN microscopic radial input**, plus an actual-family boundary-marginal corollary inherited from accepted FM-021 flatness. The full balanced Abel limit, deterministic off-charge comparison, higher factorial orders, TRACE-005 and BGS remain OPEN.

### Claim card

- For every integer N≥1 and fixed U∈U(N), D has independent normalized uniform coordinate phases. Trace means ordinary, unnormalized matrix trace.
- A deterministic coordinate order, or an independent random order conditioned on first, defines prefix compressions and the filtration. No law of the Schur matrices is assumed.
- The analytic logarithm is zero at z=0 on |z|<1. All analytic identities are first proved at fixed N on compact subdisks.
- B_N(m)=E|Tr((DU)^m)|², m≥1, is exactly the full occupation-balanced pair sum. It is not the original deterministic full pair sum.
- Equations (7) and (8) are exact covariance and positive radial-energy formulas. The scaling is r=e^(−s/N) and the pair normalization is N^(−2).
- The proposed CUE value is L(s)=(1−e^(−2s))/(4s²). Its validity for every s>0 is equivalent to (11)–(12), not established by that equivalence.
- A single scattering elimination is defined for 0<r<1. At r=1, use |a|<1 or the explicitly separated decoupled case. The boundary marginal is an almost-everywhere statement, with a point mass when |U_jj|=1.

## Dependency graph and evidence ownership

1. Compression contractivity and the analytic trace-log series → well-defined logarithms, conditional expectation (2), and holomorphic termwise operations at fixed N.
2. A literal determinant Schur complement and the transfer energy identity → (3)–(6), with the left-phase convention preserved.
3. Coordinate martingale orthogonality plus scalar phase orthogonality → (7); differentiation strictly inside the disk → (8).
4. Positive trace coefficients and global phase homogeneity → monotone G_N'', nonnegative *expected* coordinate three-radius differences, and the squeeze (13).
5. The previous item's squeeze and the explicit positive reference measure min(t,1)dt → equivalence of (9) and (11)–(12). No limiting formula is differentiated without justification.
6. Positive Laplace/Hausdorff moment compactness → Abel-to-compact comparison. The reverse direction additionally uses near-zero compact control and the Fejér bound in the pinned `determinant_boundary.md`.
7. A one-variable geometric series and phase constant terms → (15)–(16), with a nonzero rectangular coherence and an unclosed random ratio after subsequent averaging.
8. Unitary feedback, a nonzero determinant polynomial, and the holomorphic mean-value identity → the boundary Poisson marginal (17)–(19).
9. **Inherited accepted input:** actual FM-021 entrywise flatness → uniform O(N^(−1/2)) convergence of this boundary density. This review checks the implication, not the inherited four-branch parametrix or TT* proof. FM-021's mixing and FM-022's reverse-kernel bound are not used to assert radial closure.
10. Direct exact cycle and orthogonal 3×3 calculations → (20)–(21) and their precisely limited nonimplications.

All new exact-reduction leaves above have internal elementary derivations. No quantum-graph universality theorem, nonlinear gauge change, or new external theorem is a dependency. The pinned prior source audit and domain addendum are scope boundaries; their external-paper claims are not recertified here. The existing determinant/compactness result is credited rather than described as new.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Fixed U, independent coordinate phases and ordinary trace | passed | Definitions and literal phase factors agree with the balanced projector |
| All N, including N=1, and arbitrary order | passed | Empty-block conventions; conditioning on an independent order |
| Log branch and conditional expectation | passed | Uniform trace-log series on compact subdisks |
| Left/right phase placement in h | passed | (I−zDd)^(−1)D=D(I−zdD)^(−1) |
| Compression contraction and full-unitary equality | passed | Exact defect v*(I−T*T)v |
| Cross-martingale and cross-power orthogonality | passed | Conditional mean zero and total phase degree |
| Li₂ covariance and positive energy | passed | Scalar phase Taylor coefficients; no missing m or N |
| Three-radius positivity | passed | Each expected coordinate variance is a positive exponential series |
| Three-radius necessity and sufficiency | passed | Monotonicity on a positive compact interval and squeeze (13) |
| Abel ⇒ compact tests, including the endpoint zero | passed | Tilted finite measures and all Hausdorff moments including mass |
| Compact ⇒ Abel | passed with exactly the stated premise | A majorant through zero and a Fejér interval bound; not claimed from separated bands alone |
| Second and fourth conditional moments | passed | Exact geometric-series moments; r⁴ and conjugates verified |
| Contractivity after radial elimination | passed | Feedback energy inequality; no unitary replacement for r<1 |
| Mean-intensity closure | not asserted; correctly left open | Averaging a ratio/product needs joint information |
| Boundary denominator exception and point mass | passed | Constant determinant coefficient 1; decoupling at |U_jj|=1 |
| Boundary moments ⇒ Poisson law | passed | Bounded holomorphic radial limit and every Fourier coefficient |
| FM-021 ⇒ asymptotic boundary uniformity | passed, inherited input | |U_jj|=O(N^(−1/2)) uniformly in j |
| Independent clock and principal-minor witnesses | passed | Reconstructed algebra and bounded controls below |
| Actual microscopic radial limit (9)/(11) | not addressed by a proof; OPEN | No new uniform radial/coherence estimate supplied |
| Deterministic off-charge and higher orders | out of scope; OPEN | Neither exact representation nor either finite witness controls them |
| Inherited FM-021/FM-022 analytic theorems | out of scope for recertification | Statements and use boundaries checked; proofs not independently repeated |

## Decisive analytic checks

### 1. The balanced target and martingale really have the claimed domain

For a rooted cyclic word x, write A_U(x)=∏U_(x_j,x_(j+1)) and n(x) for its coordinate occupation vector. Direct phase integration gives

    B_N(m)=Σ_(n(x)=n(y)) A_U(x) conjugate(A_U(y)).

This includes every word repetition and every m. The omitted deterministic term is exactly |Tr U^m|²−B_N(m), the nonzero-charge sum. Thus the phase integral is an exact projector decomposition of the existing target, without making a random-ensemble theorem into a deterministic one.

For |z|≤ρ<1, the trace-log series is bounded termwise by Nρ^m/m. Conditional integration may therefore be taken termwise; a word survives precisely when every label is revealed. This gives (2) and also E L_k=0. Several-variable analyticity supplies the locally absolutely convergent coordinate Taylor series. It is unnecessary to assert that the sum of absolute values of individual ungrouped word amplitudes converges all the way to |z|<1.

Put Δ_k=L_k−L_(k−1). For k<l, conditioning on the first l−1 phases gives E[Δ_k(z) conjugate(Δ_l(w))]=0. Integrating the newest phase in log(1−ζ_k f_k) gives exactly Σ_n f_k(z)^n conjugate(f_k(w))^n/n². The mean is zero. This proves (7) for different as well as equal radii.

### 2. Transfer phases, loss and energy normalization

With block order (k,S_(k−1)), the determinant of I−zD_kU_k has scalar complement

    1−zζ_k a−z²ζ_k b(I−zD d)^(−1)D c
      =1−zζ_k[a+z bD(I−zdD)^(−1)c].

So the row-phase convention in (3) is correct. Set T=[a,bD;c,dD], y=(I−zdD)^(−1)c and v=(1,zy). Then Tv=(h,y), and the exact identity behind (5) is

    1−|h|²−(1−|z|²)||y||²=v*(I−T*T)v≥0.

At k=N the defect is zero. At a real r, adding 1−r² appropriately gives (6). No inverse at a boundary pole is used.

Applying z∂_z and conjugate(w)∂_conjugate(w) to the scalar series cancels both factors n in n². At z=w=r this yields r²|f_k'(r)|²/(1−|f_k(r)|²), and f_k'=h_k+rh_k'. The left side differentiates the factors z^m conjugate(w)^m/m² to r^(2m). There is no surviving 1/m, extra factor 2 or N. For N=1, U=(u), |u|=1, the identity becomes Σ_(m≥1)r^(2m)=r²/(1−r²), an immediate unit check.

Every differentiation and phase interchange takes place at fixed N on a smaller disk. Substituting r=e^(−s/N) is then exact at each N. No uniform-in-N differentiability is used.

### 3. The derivative-free equivalence is valid

Define

    q_(k,m)=E|Tr((D_kU_k)^m)−Tr((D_(k−1)U_(k−1))^m)|²≥0.

The degree-m coefficient is homogeneous in the first k phases. Simultaneous phase rotation therefore kills all unequal-degree cross terms and gives

    g_(k,N)(s)=E Li₂(|f_k(e^(−s/N))|²)
             =Σ_(m≥1) q_(k,m)e^(−2sm/N)/m².

Consequently every **expected** k contribution to Δ_hG_N is nonnegative. This does not assert pointwise convexity of Li₂(|f_k(r)|²) for every fixed preceding phase configuration.

The full series gives G_N''(s)=4N^(−2)Σ_mB_N(m)e^(−2sm/N), a nonnegative decreasing function. The reference second derivative is

    F(s)=4∫_0^∞e^(−2st)min(t,1)dt=(1−e^(−2s))/s².

If (9) holds, the triangle-kernel identity for Δ_hG_N and monotonicity bound G_N'' uniformly on [s−h,s+h] by its value at the positive left endpoint, for all sufficiently large N. Dominated convergence yields (11); Tonelli computes its limit as (12). Near t=0 that integrand is 4h²t+O(t²), so its apparent singularity is removable. At infinity, s>h gives exponential decay.

Conversely, for 0<h<s/2, the two triangle kernels supported respectively to the right and left of s give exactly (13). Taking liminf/limsup in N and then h↓0 squeezes G_N''(s) to F(s). This is a valid monotone-density argument; it does not differentiate a merely pointwise limit of G_N. In fact G_N itself need not have a finite limit. Each dilogarithm's π²/6 bound does not bound the growing N-term sum uniformly.

### 4. The near-zero qualification in the compact/Abel bridge is essential to the stated proof

The pinned `determinant_boundary.md`, SHA-256
`14c1eeedf76c5362566525cf2b10e84ce422a0e5914881193bf79d80d205a06c`,
uses μ_N=N^(−2)Σ_(m≥1)|Tr V_N^m|²δ_(m/N). It applies to the present B_N by expectation over V_N=DU_N, preserving positivity at every step.

After tilting by e^(−2s₀t) and mapping x=e^(−t), the n-th moment is the Abel transform at s₀+n/2. Its n=0 value controls total mass. Uniform polynomial approximation gives weak convergence on [0,1]. A continuous compact test φ on [0,∞) corresponds to x^(−2s₀)φ(−log x), extended by zero near x=0; it is also continuous at x=1. Thus there is no loss of tests meeting t=0 in the Abel-to-compact direction.

For the reverse implication let a_m=B_N(m), a_(−m)=a_m, a_0=N². Each realization's eigenangle-difference measure is positive, and so is its expectation. The triangular Fejér sum obeys

    0≤F_N(q)=Σ_(|k|<N)(1−|k|/N)a_(q+k)≤F_N(0).

An interval of N integers is covered by weights at least 1/2 in a suitable translate. A fixed nonnegative smooth compact majorant of [−1,1], **including zero**, gives F_N(0)/N²=O(1); the a_0 term contributes exactly 1 separately. This controls every unit t-interval and makes every Laplace tail summable uniformly. The candidate explicitly does not infer this reverse implication from bands separated from zero alone. That qualification is correct and must remain in any integration.

### 5. Elimination moments, conjugates and nonclosure

For f=rζx/(1−rζa), the Fourier coefficients are r^n a^(n−1)x, n≥1. The constant-term computations give

    E f=E f²=0,
    E|f|²=r²|x|²/(1−r²|a|²),
    E[f|f|²]=r⁴x|x|² conjugate(a)/(1−r²|a|²)²,
    E|f|⁴=r⁴|x|⁴(1+r²|a|²)/(1−r²|a|²)³.

For the cubic moment one sums two positive Fourier indices n,l and the conjugate index n+l; for the quartic moment the degree-k coefficient of f² is (k−1)r^k a^(k−2)x². Expanding |A₀+f|⁴ now gives exactly (16), including its factor 4r⁴ and conjugation of a. The relevant coherence is

    Re(conjugate(S_uv) S_uℓ S_ℓv conjugate(S_ℓℓ)),

not the original reverse two-entry kernel Q.

Contractivity after elimination follows independently from
S(x,rζy)=(S'x,y), y=(1−rζa)^(−1)cx. For r<1 it gives a dissipative term (1−r²)|y|² and does not make S' unitary. Each later coordinate still carries the same original r. Fresh phases remain independent of the current matrix, but its entries are jointly random; hence subsequent averaging really contains E[P_ukP_kv/(1−r²P_kk)].

An extra exact strict-contraction witness verifies that equal intensities alone cannot fix the fourth moment: S₊=(1/5)[[1,1],[1,1]] and S₋=(1/5)[[−1,1],[1,1]] have equal squared entry moduli and norm<1. Eliminating the second coordinate at r=1/2 gives fourth moments differing by **8/6125625**, entirely from the coherence term. This is a finite contraction witness, not an actual-family asymptotic obstruction.

At r=1 and |a|=1, contraction itself forces b=c=0 by the row/column norm bounds. The update is then the trivial reduction; one must not evaluate a formal 0/0 in (15). The candidate already separates this case.

### 6. The boundary marginal proof survives degenerate cases

For diagonal feedback W with max|W_ii|<1, put y=(I−U_SS W)^(−1)U_Sj. Unitarity gives

    1−|H_j(W)|²=||y||²−||Wy||²≥0.

Thus H_j is holomorphic and bounded by one on the polydisk, without importing a boundary regularity theorem. The polynomial det(I−U_SS D) has constant coefficient 1, so it is not identically zero. Induction on the number of variables and one-variable polynomial zeros show that its torus zero set has Haar measure zero. Outside that set radial convergence is ordinary continuity of a rational expression. Setting W=D in the energy identity gives |H_j|=1 there.

For 0≤ρ<1, the mean-value property applied to H_j(ρD)^p gives U_jj^p. Uniform boundedness by one permits dominated convergence as ρ↑1. Positive powers plus their conjugates determine every Fourier coefficient of the circle measure. They agree with the Poisson kernel of parameter U_jj; if |U_jj|=1 the measure is the point mass there. In the latter case unitarity already decouples coordinate j. Arbitrary choices on the null exceptional set have no effect. N=1 is included with an empty eliminated block.

For a=|U_jj|<1 the density ranges between (1−a)/(1+a) and (1+a)/(1−a); hence its maximal deviation from 1 is exactly at most 2a/(1−a), as in (19). Inherited actual flatness supplies a=O(N^(−1/2)) uniformly in j, eventually strictly below one. It supplies no control on h_j+r h_j', which is the missing radial observable.

### 7. Both negative controls are exact and correctly scoped

For C_N with N≥2, every proper natural prefix has zero trace in every positive power; the final transfer is f_N(z)=z^N∏_(j<N)ζ_j. Its angular delay is N for **f_N**; the delay of h_N alone is N−1. The boundary value is uniformly distributed, but the sole energy contribution is N²r^(2N)/(1−r^(2N)). Thus (20) is exact and its normalized value is 1/(e^(2s)−1), for every N. This only refutes inference from boundary law and mean total delay. It does not satisfy entrywise flatness/mixing.

For the 3×3 minor witness, let P=11ᵀ/3 and
J=(1/√3)[[0,1,−1],[−1,0,1],[1,−1,0]]. Then P²=P, PJ=JP=0, Jᵀ=−J and J²=−(I−P). Independently reconstructing U₊=P+J and U₋=I−2P proves orthogonality, determinants +1 and −1, singleton minors 1/3 and two-element minors respectively +1/3 and −1/3. These are exactly the displayed candidate matrices.

The complete multivariate phase-averaged characteristic covariance is
Σ_I|det U_II|²∏_(i∈I)z_i conjugate(w_i), so all principal-minor moduli really determine this covariance. On the other hand

    Tr((DU)²)=Σ_iU_ii²ζ_i²+2Σ_(i<j)U_ijU_jiζ_iζ_j.

The mixed coefficients are −4/9 and +8/9. Orthogonality of distinct phase monomials gives (3+3·16)/81=17/27 and (3+3·64)/81=65/27. The witness uses independent coordinate phases, whereas the prior deleted clock uses one common rotation. It changes no actual-model claim and establishes no asymptotic counterexample.

## Independent bounded verification and provenance

`check_independent.py` was newly implemented. It does not import or replay the author's checker. Principal determinants and Newton recursion reconstruct the trace polynomials, whereas a matrix-vector recurrence constructs the transfer series. This differs from the author's explicit closed-word enumeration. A separate exact fourth-root phase grid evaluates literal matrix powers through degree three, where the quadrature is exactly Haar for the relevant exponent differences.

The four Q(i) unitary fixtures have dimensions 1,2,3,4, with maximum powers respectively 5,5,4,4; all two N=2 orders, all six N=3 orders, and forward/reverse N=4 orders are checked. Literal determinant/loss tests use the complex radius (2+i)/5, testing conjugation beyond real radii. Fourth-moment checks are Laurent constant-term series through r^12, including a=0, rather than a replay of the author's contour residues.

Executed counts:

- 129 Newton/transfer log coefficient identities and 129 positive-energy coefficient identities
- 129 phase-degree checks and 47 full-energy/order comparisons
- 240 literal phase-grid matrix-power evaluations and 6 exact Haar-norm comparisons
- 18 complex-radius determinant identities and 18 contraction-loss identities
- 6 nonsingular boundary inner samples and 1 degenerate point-mass control
- 78 second/fourth radial-series coefficient checks across 3 scalar inputs
- 2 strict-contraction coherence fixtures, 2 algebraic orthogonality checks, all 8 principal-minor comparisons and both B₂ values
- 56 cyclic powers at N=1,2,3,4,7, plus 18 transfer checks across all six N=3 reveal orders
- 1 exact exponential generator check for the three-radius expression

The completed command was `python3 run_bounded.py`; the measured runtime was approximately 4.1 seconds. Enforced limits were 160 CPU seconds, 180 wall seconds, 2 GiB address space and one CPU affinity. Single-thread library settings are cooperative. Python and SymPy versions, actual command, before/after input hashes, output hashes and exit status are in `execution_manifest.json`; output is `checks.json` with empty `checks.stderr`.

Two initial harness failures are preserved in `failed_attempts/`: an unavailable SymPy domain attribute, then an exponential/cosh normalization not reduced by the chosen simplifier. The second run reached the final assertion after the substantive checks. Neither was a mathematical counterexample. The final code uses an ordinary rational zero and rewrites cosh in exponentials explicitly. These repairs changed no tested identity or input family.

The candidate's checker, declared scope, existing output and manifests were inspected. The fresh validator obtained from the computation-audit skill validated both the candidate record and this run with artifact/hash checking. Its only difference from the author's pinned validator is a trailing newline. The author checker was not re-executed; the independent run is the fresh computational evidence.

Commands for reproduction and validation:

    cd /workspace/shared/bgs_schur_reduction_review
    python3 run_bounded.py
    python3 validate_manifest.py execution_manifest.json --root .
    python3 validate_manifest.py /workspace/shared/bgs_balanced_phase_closure/execution_manifest.json --root /workspace/shared/bgs_balanced_phase_closure

No actual fixed-tau matrix was approximated, no large-N evidence was inferred from these checks, no inherited analytic theorem was recertified and no canonical build/publication was attempted.

## Exact remaining gap and strongest safe statement

The sole missing estimate for this **full balanced pair** route remains

    N^(−2)Σ_k E[r²|h_k(r)+rh_k'(r)|²/(1−r²|h_k(r)|²)]
       →(1−e^(−2s))/(4s²),  r=e^(−s/N), every s>0,

or, equivalently, convergence of the stated expected three-radius Li₂ sums. The exact loss identity, marginal Poisson law, flat initial entries, initial P mixing and reverse Q decay do not supply this estimate in the candidate. No propagation theorem for Schur-entry flatness, denominators or their joint coherences has been proved here.

A next proposed closure should be tested first against the cyclic control and the strict-contraction coherence witness, then checked for uniform control at 1−r≈N^(−1) and for preservation through **all** elimination steps. Accumulating more low-power numerical matches is not a substitute. If the balanced criterion is eventually proved, it establishes the balanced pair compact tests through the explicit positive-measure bridge; the deterministic off-charge defect and higher factorial hierarchy still need independent estimates.
