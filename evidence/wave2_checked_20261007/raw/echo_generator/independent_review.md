# Independent audit of the one-pinch averaged lemma

7 October 2026. Fresh, independent reconstruction from the stated definitions and pinned accepted inputs. Only this report was written; no proof source was edited.

**Primary verdict: proved as written.** This covers L1, the signed reduction L2 and its nonnegative-weight consequence, the single consecutive-block extension (including deterministic `j_N <= aN`), the changed-family one-pinch counterexample, and the exact positive-overlap reduction. No mathematical correction or additional hypothesis is needed within their expressly stated scopes.

The literal untwisted estimate L6 remains open. The proof does not establish a separated-insertion theorem, a Hamming/switch-masked conclusion, T16, or BGS. No such enlargement is accepted here.

## 1. Normalized claim and accepted dependency boundary

Let `H_N=End(C^N)`, `T=Ad(U_N)`, and let `D=sum_c P_c T P_c` be the pinching by the literal cyclic coordinate charges. With `V_theta=Ad(Z_theta)`, put `A_theta=V_theta T` and `B_theta=V_theta D`. The trace `Tr` is the ordinary trace of an operator on the `N^2`-dimensional space `H_N`, while `tr` is the ordinary matrix trace on `C^N`. The coefficient field is complex. Torus measure is normalized Haar measure on all `N` independent phases.

For every fixed complex `w in C_c^infinity((a,b))`, with `0<a<b<infinity`, the audited assertion is

    N^-2 sum_(m>=1) w(m/N) integral Tr[B_theta A_theta^(m-1)] dtheta -> 0.

The generic argument applies to any sequence of unitary matrices whose charge pinching admits uniform finite-rank approximation in operator norm. The actual odd-dimensional literal family has this property by accepted FM-028, Section C2, equation C4. Its compactness is at `theta=0`; no occupation-uniform compact embedding is imported. L1--L2 need only this whole-`D` compactness, not FM-028's quasimode, radial/resolvent, Egorov, or classical-mixing conclusions. The positive-overlap note separately uses C1/C6 and hence their Egorov/mixing dependencies; it does not need the radial/resolvent conclusions. The only other analytic input is the exact all-unitary Abel estimate (A) of accepted TRACE-023:

    sum_(k>=1) q^k integral |tr((Z_theta U_N)^k)|^2 dtheta
      <= N(1+q)/(2(1-q)).

I read both proof statements and their current acceptance scopes in `mathematics/phase_trace_checkpoint.md`; the preparation headings in the frozen proof files do not supersede that scope. `record/claims.json` also marks FM-028 and TRACE-023 proved with their inherited analytic boundaries. Only the Abel component of TRACE-023 is used here, not its compact-color source identities or any external color-flavor theorem.

Dependency graph:

1. Exact cyclic character twirl and adjoint trace identity give the echo formula, positivity, and occupation interpretation.
2. FM-028 C4 gives bounded-rank approximants to `D_N` with arbitrarily small operator-norm error.
3. Smooth discrete summation by parts gives a Poisson majorant for the fully time-summed spectral kernel.
4. TRACE-023 (A) controls the expected trace norm of that kernel by `O_w(N^2)`.
5. Finite rank costs `O_w(N)` before normalization, while the small-norm remainder costs `O_w(epsilon N^2)`.
6. Sending `N` to infinity and then `epsilon` to zero proves L1 and hence L2.
7. The counterexample adds the previously independently reviewed period-six cyclic-carry family, plus the exact flat-return identity.
8. The positive-overlap note additionally uses actual flatness and FM-028 C1/C6, both only in their stated scopes.

## 2. Independent reconstruction of the exact echo

Set `Z_b=diag(exp(2pi i b j/N))` and `R_b=Ad(Z_b)`. On the matrix unit `|j><j+c|`, `R_b` is multiplication by `exp(-2pi i bc/N)`. Therefore cyclic character orthogonality gives

    D=(1/N) sum_b R_b T R_b*.

Since `Z_theta` commutes with every `Z_b`, with `W_theta=Z_theta U_N` this implies

    B_theta=(1/N) sum_b Ad(Z_b W_theta Z_b*),
    A_theta=Ad(W_theta).

Now `Tr_H Ad(K)=|tr K|^2` for every finite matrix `K`, and adjoint maps multiply their arguments in the same order. Cyclicity of the ordinary trace yields

    E_N,m(theta)=(1/N) sum_b
      |tr(W_theta^(m-1) Z_b W_theta Z_b*)|^2 >= 0.

No factor of `N` is missing. Changing the scalar normalization of the Hilbert--Schmidt inner product does not change the operator trace, singular values, or operator norms of a superoperator.

Grouping `tr(H Z_b W Z_b*)`, where `H=W^(m-1)`, by `c=k-j` gives Fourier coefficient

    sum_j H_(j+c,j) W_(j,j+c).

Consequently Parseval gives exactly

    E_N,m(theta)=sum_c |sum_j H_(j+c,j) W_(j,j+c)|^2.

Expansion in the independent row phases counts the complete integer occupation vector. Thus the torus integral is the full occupation-balanced contribution, including all repeated occupations. A finite modulation average alone would be a checksum constraint, but that substitution is not made here.

## 3. Independent time-kernel and finite-rank argument

Extend the sampled coefficients `a_m=w(m/N)` by zero to every integer. Because the support is compact and lies strictly inside a fixed positive band,

    sum_m |a_m| <= C_w N,
    sum_m |a_m-2a_(m-1)+a_(m-2)| <= C_w/N.

For `f_N(z)=sum_m a_m z^(m-1)`, multiplication by `(1-z)^2` expresses its coefficients as those second differences, apart from a harmless index shift. For `d=dist(x,2pi Z)`, `|1-exp(ix)|` is comparable to `d` on a fundamental interval. Combining the trivial and twice-differenced bounds gives

    |f_N(exp(ix))| <= C_w min(N,1/(N d^2))
      <= C'_w N/(1+N^2 d^2).

This holds for arbitrary complex `w`; coefficient positivity is unused. For `q_N=exp(-1/N)`, the exact denominator

    |1-q_N exp(ix)|^2=(1-q_N)^2+2q_N(1-cos x)

shows that the last majorant is bounded by a constant times `P_(q_N)(x)`. The constants depend on the fixed weight and band, not on `N`, phases, or eigenvalue multiplicities.

If the eigenvalues of `W_theta` are `exp(i lambda_alpha)`, then `A_theta` is unitary and its eigenvalues, with all multiplicities, are `exp(i(lambda_alpha-lambda_beta))`. Thus functional calculus gives

    ||f_N(A_theta)||_1
      =sum_(alpha,beta)|f_N(exp(i(lambda_alpha-lambda_beta)))|
      <=C_w sum_(alpha,beta)P_(q_N)(lambda_alpha-lambda_beta).

The absolutely convergent Poisson Fourier expansion gives the exact identity

    sum_(alpha,beta)P_q(lambda_alpha-lambda_beta)
      =N^2+2 sum_(k>=1)q^k |tr(W_theta^k)|^2.

Integrating and applying accepted (A) gives

    integral ||f_N(A_theta)||_1 dtheta
      <=C_w [N^2+N(1+q_N)/(1-q_N)] <=C''_w N^2.

This is a trace-norm bound only after the complete time sum. No termwise-in-time absolute estimate, pointwise pair-density estimate, or microscopic eigenphase law is substituted.

For completeness, C4 really does imply the finite-rank premise used here: approximate its compact limit `K` by a fixed finite-rank operator `F`, and compress `F` back to `H_N` through the isometric embeddings. The resulting `K_N` has uniformly bounded rank and approximates `D_N` in operator norm. Since `||D_N||<=1`, its norm can be taken at most two for sufficiently small error.

Write `D_N=K_N+R_N`, where `rank K_N<=r_epsilon`, `||K_N||<=2`, and `||R_N||<=epsilon`, eventually. Unitarity of `V_theta`, trace duality, and the trivial kernel norm bound imply

    |Tr[V_theta K_N f_N(A_theta)]| <=2r_epsilon C_w N,
    integral |Tr[V_theta R_N f_N(A_theta)]|dtheta
      <=epsilon C''_w N^2.

After multiplication by `N^-2`, the limsup is at most `C''_w epsilon`. Letting `epsilon` tend to zero proves L1. In fact this argument also bounds the phase integral of the absolute value of the time-summed trace. It never claims convergence of the family `V_theta D_N` in one fixed compact embedding.

The identity direction is reducing for both `T` and `D`, and fixed by `V_theta`. Its exact contribution is `N^-2 f_N(1)=O_w(N^-1)`. There is no omitted stationary-mode exception.

## 4. Signed consequence and consecutive pinches

By definition, `S_N(w)` equals the untwisted aggregate minus the averaged aggregate. The latter is `o(1)`, proving L2 for complex weights. For real nonnegative weights the untwisted aggregate is nonnegative, so `liminf S_N(w)>=0`. Also `S_N(w)->0` if and only if that untwisted aggregate tends to zero. This is an equivalence of unresolved limits, not a proof of either vanishing limit.

For consecutive pinches, fix `N`, `theta`, and an integer `j`, independent of the summation variable `m`. Decompose

    B_theta^j
      =V_theta K_N B_theta^(j-1)+V_theta R_N B_theta^(j-1).

Because `||B_theta||<=1`, the first term has rank at most `r_epsilon` and norm at most two, and the second has norm at most `epsilon`, uniformly in `j`. If every sampled `m` is at least `j`, the shifted kernel satisfies exactly

    sum_m w(m/N) z^(m-j)=z^(1-j) f_N(z).

Multiplication by this unit-modulus scalar leaves both the spectral norm and trace norm of the kernel unchanged. The proof therefore works for fixed `j` and for deterministic `j_N<=aN`. All nonzero samples satisfy `m/N>a`, so the support requirement is respected. The same rank/tail argument handles fixed-in-`m` contraction factors on either side of `D_N` when the entire remaining time dependence is a single adjacent unitary power, as stated.

For separated pinches with insertion locations changing with `m`, the needed factorization need not exist. Likewise a Hamming or high-switch coefficient mask is not automatically represented by this unmasked trace. These extensions are expressly excluded and have not been smuggled into the signed consequence.

## 5. Audit of the period-six counterexample

The imported v2 source and its independent review have the hashes listed below, matching `ACCEPTANCE_AND_PROVENANCE.md`. I independently checked the parts B1--B4 needed here:

- Cube bijectivity for `p=2 mod 3` makes the displayed kernel a permutation conjugate of the two-dimensional finite Fourier kernel with invertible bilinear matrix `A`.
- Its square is the row permutation `C=-A^-1 A^T`, with `C^3=I`, hence the sixth power is the identity. The inverse ket-label convention does not change this conclusion.
- `A-A^T` is invertible, giving the reverse norm exactly `1/p`.
- Literal addition modulo `p^2` retains the low-digit carry. A row-Gram entry has scale `p^-4`. At most `p` exceptional row partners have both underlying polynomial factors constant, while nonexceptional entries have size at most `2sqrt(2)(2+log p)p^-9/4`. The Hermitian row-sum bound is exactly the displayed estimate for the squared charge-block norm. The case `p|c` and singleton carry intervals are included.
- The zero-charge block is `J` exactly by flatness; therefore `||D_N-J_H||` is bounded by the maximum nonzero-charge block norm and tends to zero. This supplies uniform rank-one approximation, including a common compact identity embedding if desired.

For any flat unitary with `U^m=I`, substituting `U^(m-1)=U*` into the charge-energy identity makes each inner sum equal to one. Therefore `E_N,m(0)=N` exactly. Other times contribute nonnegative terms. The arithmetic-progression Riemann sum gives

    N^-1 sum_(6|m) w(m/N) -> (1/6) integral w(t)dt.

Applying the already proved generic lemma to `D_N=J_H+R_N` bounds the averaged aggregate by `O_w(N^-1+||R_N||)=o(1)`. Thus the counterexample's strict positive liminf is proved on every fixed positive band for nonzero nonnegative `w`. The restriction `b<1/6` in the old full-residual theorem is not required for this different one-pinch corollary. No old Hamming/switch-masked lower bound is imported to justify the new first-loop statement.

The family is changed, not literal BGS. Actual fixed-word information already excludes a six-step recurrence for the actual product `Q_N M_N`; it does not provide the missing actual Heisenberg estimate.

## 6. Audit of the positive-overlap formulation

Write `a_(alpha,b)=<v_alpha,Z_b U Z_b* v_alpha>`. Then

    C_(alpha,beta)=(1/N)sum_b a_(alpha,b) conjugate(a_(beta,b))

is a positive semidefinite Gram matrix. Direct evaluation of `Ad(Z_b U Z_b*)` on `X_(alpha,beta)=|v_alpha><v_beta|` gives

    <X_(alpha,beta),D X_(alpha,beta)>_HS=C_(alpha,beta).

This is the diagonal matrix entry of the superoperator on an eigenoperator; it is not `<P_alpha,D P_beta>`. The echo is

    E_N,m(0)=sum_(alpha,beta)lambda_alpha^(m-1)
      conjugate(lambda_beta)^(m-1) C_(alpha,beta)=u_m* C u_m,

where `u_m(alpha)=conjugate(lambda_alpha)^(m-1)`. This orientation is correct.

For `F(X)_c=sum_j X_(j+c,j)U_(j,j+c)`, disjoint coordinate supports and Cauchy--Schwarz give `||F||^2<=C_flat`. The map sending a coordinate vector `a` to `sum_alpha a_alpha P_alpha` is an ordinary-HS isometry. Fourier Parseval identifies `C` with the transpose/conjugate of its ordinary Gram matrix. Those operations preserve positivity and operator norm, so `||C||<=C_flat`. No simple-spectrum hypothesis occurs.

For `alpha!=beta`, `X_(alpha,beta)` is centered and an exact adjoint eigenvector. Accepted FM-028 C1/C6 uniformly bounds its image under `D` by `o(1)`. For the diagonal case, write `P_alpha=I/N+Y_alpha`; then `Y_alpha` is centered, is an exact eigenvector at phase one, and has ordinary-HS norm at most one. The reducing identity direction gives

    C_(alpha,alpha)=1/N+<Y_alpha,D Y_alpha>_HS=1/N+o(1)

uniformly. Switching the scalar HS normalization does not alter this operator-norm application. Consequently `Tr C=o(N)`. Degenerate eigenspaces cause no gap; the construction is valid for every chosen orthonormal eigenbasis, with the noted possible basis dependence of `Tr C`.

For `w>=0`, `H_N(w)=sum_m w(m/N)u_m u_m*` is positive and the unresolved untwisted aggregate is exactly `N^-2 Tr[C H_N(w)]`. The two separate bounds `||C||=O(1)` and `Tr C=o(N)` do not control alignment with large eigenvalues of `H_N(w)`. The period-six counterexample demonstrates this failure even when all centered pinching norms vanish.

The sufficient unaveraged Poisson pair bound in the main note does close L6 by the same finite-rank/tail argument. It is stated as an additional input, not derived from actual flatness, fixed-word freeness, or the radial theorem. The exact remaining gap is an actual-model estimate forcing this positive overlap to be `o(N^2)`.

## 7. Obligation results and bounded controls

Passed: complex weight quantifier; fixed positive Heisenberg band; full time summation; `m-1` shift; superoperator/matrix trace normalization; finite-rank consequence of C4; arbitrary occupation twists; identity direction; all multiplicities; consecutive block and `j_N<=aN`; signed reduction; cyclic-carry witness; Gram orientation; flatness norm; centered quasimode use.

Out of scope: separated moving insertions, Hamming/switch masks, signed T16, microscopic CUE identification, full BGS.

I additionally ran independent exact SymPy Laurent-polynomial controls for the two-dimensional Hadamard unitary with two independent formal row phases. These are generic finite algebra controls, not instances of the odd-dimensional literal model. For `m=1,...,6`, direct pinched-superoperator traces agreed exactly with the two-term twirl. The untwisted values were `(0,2,0,2,0,2)` and their exact full phase averages were `(1,3/2,3/2,11/8,11/8,23/16)`. This confirms in particular that positivity of each echo is not finite-N positivity of its signed subtraction. All 21 consecutive-shift identities with `1<=j<=m<=6` passed exactly. An initial attempt failed before any checks because SymPy returned an immutable matrix; converting it to `MutableDenseMatrix` fixed the harness, and the corrected run exited zero. No source files or additional artifacts were written by these controls.

No finite control is used as evidence for an asymptotic claim. The universal proof is the time-kernel and finite-rank argument above.

### Additional requested audit: literal-time sign certificates

The short analytic certificate in `computation_audit.md` also passes. Independently expanding the stated trigonometric symbol over exact rational real/imaginary coefficients gives `sum_v(|Re c_v|+|Im c_v|)=593/500`. Since each literal Weyl operator is unitary, aliases do not affect this upper bound for `||A_N||`. Selfadjointness gives `||exp(i t N A_N)-I||<=|t|N(593/500)`. The adjoint-channel difference is at most twice the unitary difference; pinching is operator-norm contractive. Telescoping the one-pinch product therefore gives `2mN(593/500)|t|` in superoperator norm, hence `2mN^3(593/500)|t|` in trace. Subtracting the phase expectation costs at most another factor two, uniformly over phases.

I independently evaluated the zero-time `N=3` occupation sums using integer coefficient pairs in `Z[zeta_3]`, enumerating all 27 and 81 rooted paths at `m=3,4`. The cat chirp here is the positive Fourier kernel `3^-1/2 zeta_3^(jk)`. The results were `E_3,3=1`, averaged echo `13/9`, and signed value `-4/9`; at `m=4`, the values were `3`, `37/27`, and `44/27`. The exact error coefficients `4m*3^3*(593/500)` are `48033/125` and `64044/125`. At `t=10^-80` they preserve the asserted negative and positive signs. These conclusions use a global Lipschitz bound, not unbounded Taylor extrapolation. The rest of the author's finite-control implementation and its normal/optimized execution record are outside this independent audit; I do not certify those executions merely from their reported success.

## 8. Exact reviewed revisions

Paths below are relative to this report's directory for the three targets, and relative to `/workspace/shared/bgs_checked_checkpoint_validation/source_snapshot` for accepted inputs.

- `one_pinch_averaged_lemma.md`: `8f4fa7f6988a78ed7a1d576e184761efd6674e8275806ce51918ab41ff92b6f8` (final dependency-only clarification inspected; the earlier reviewed version was `47759948e8de566b8decab7d19450b27a31989c4bfbee5e2c9807796c13fe170`)
- `generic_counterexample.md`: `bccafdfa6300d04e45e89bd9fb0cdfdbdcfc2b491f84390d030d3c66be89c9a5`
- `positive_overlap_obligation.md`: `4e0538c8f0532087b2c9af356aa4aa69f7a7d2414f4be8cd470c7066477cad8a`
- `computation_audit.md`: `ba6a30c43d7c55e1a5160643e98a9a96320f48a3fa762aaa588d2c58c0696f65` (only the literal-time sign certificate independently audited)
- `mathematics/actual_charge_radial_shell.md`: `eccca8f36860e537f736828c435fce94f10006fbbaa48722fbd9481671ed4c0b`
- `mathematics/uniform_phase_pair_abel_bound.md`: `ecd82a74edfabb89f6cbf46054d76c52dd41e5eb2d5a9790771b16a7c033da3f`
- `mathematics/phase_trace_checkpoint.md`: `f52a4c7beb9042d403dd125f9425d4a29f6d1cd43a624b91a3b4b89f9abe9208`
- `evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/bilinear_carry_counterexample_v2.md`: `88408d0241a9346fd16b33117ff3779b8abccb740a3992aa29a631c59f8c49ab`
- `evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/carry_review/review_v2.md`: `5d0cbaf1b444073c8b19f24e3024a9cc4670d450eb995e45e6f304f084b39c4a`

**Exact remaining gap for the audited bounded theorem: none.** The strongest safe conclusion is an annealed one-block disappearance theorem and reduction of the literal signed first loop to a nonnegative untwisted overlap. The next model-specific obligation is a quantitative estimate on that overlap, not another manipulation of the already controlled annealed term.
