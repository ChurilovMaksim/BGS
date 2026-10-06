# Independent audit: full factorial target through a finite-order WKB table

Date: 6 October 2026. Primary verdict: **proved as written**, as a fixed-order reduction and equivalence of signed trace-table targets. This is not a proof of TRACE-005 or a spectral point-process theorem for the nonunitary approximant. No missing analytic hypothesis or exponent correction was found.

## Frozen target and sources

Reviewed `/workspace/shared/bgs_exact_quantization_route/factorial_wkb_reduction.md`, SHA-256 `6487183ba4359319fa3def390025e75f33655be4876eca7cea2eced3b56eabcd`. Canonical repository HEAD was `12d2e66dc76cc11cebe988fdc8f6d9caefc4c735`; the working tree contained pending unrelated LOOP integration. No canonical file was changed.

The three source hashes in the target match the actual canonical bytes:

- `mathematics/four_branch_parametrix.md`: `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`.
- `mathematics/trace_to_local_statistics_bridge.md`: `8de10ab48a068363110753165a09a7a569111a04d743e575eed9f669bc8a64fd`.
- `mathematics/signed_heisenberg_comparison.md`: `450e9c98720f4a6793b361611f2dee9d34531442efc521dacdcd902e1cc14313`.

Also inspected model definitions in `fixed_model_symmetry_theorem.md` §1 and `fixed_map_path_model.md`, the repository authorities, and current TRACE-005/TRACE-010/FM-022 scope records. The canonical registry still calls actual signed comparison open. No ledger exists at `.mathbox/` in the inspected root.

## Normalized claim and dependency closure

For each fixed integer k≥2 and fixed W∈C_c^∞(R^(k−1)), the complete partition polynomial evaluated on either the Laurent table or the signed-adjoint table of an N-dimensional V differs from the actual unitary target by O(N^k δ exp(A Nδ/(1−δ))), where δ bounds ||U−V||<1 and A depends only on support. If δ≤C_J N^(−J−1/2), fixed J≥k gives o(1), specifically O(N^(k−J−1/2)). Fix k and J before N; constants may depend on J and support. This is exactly the claimed quantifier structure.

Dependencies:

1. Exact odd-N raw-to-midpoint Weyl identity, the actual g, and Hermiticity/unitarity: canonical model definitions.
2. Exact four-branch Gauss initialization and smooth global characteristic graph for |t|≤10^(−20): direct canonical parametrix proof §§1–2,4 and Dependency boundary.
3. Finite-J transport induction, finite Taylor remainder, entrywise-to-operator bound, unitary Duhamel: reconstructed below; no long-time dynamics.
4. Noncommutative power telescoping and partition product telescoping: elementary algebra, reconstructed below.
5. Exact N^(−k) Fourier/factorial normalization: bridge equations (5), (7), (9), (10).
6. Reference comparison remains an open independent target. Positivity/every-bandwidth arguments apply only afterward to actual U spectra.

There is no dependence on FM-022's mixed-phase nondegeneracy, reverse-path cancellation, an ensemble moment theorem, or long-time Egorov. They are not needed for this reduction.

## Actual one-step analytic reconstruction

The raw symbol f is not inserted into a midpoint differential equation. With W_N(l,k)=(-1)^(kl)T_N(l,k), the actual same matrix A_N is the ordinary quantization of g, whose p-dependent coefficient is r(q+1/2), not r(q). For odd N,

(-1)^(kl) e_N(k(j+inv2·l)) = e(k(j/N+hl/2)).

Thus the exact difference action is Σ c_kl e(k(x+hl/2))u(x+hl), with l∈{−1,0,1}. Factor e(S/h) from this exact action; the remaining amplitude operator is B_h=Σ_(n≥0)h^n P_n in the finite-Taylor sense. Here P_0=g(x,S_x), and directly differentiating the h expression gives

iP_1 a = (g_p/(2π))a_x +(g_xp+g_pp S_xx)a/(4π).

The generator is iA_N/h, so the phase term cancels precisely when S_t=g/(2π). The amplitude residual for a^(J)=Σ_(j=0)^J h^j a_j is

∂_t a^(J) − Σ_(n≥1) h^(n−1)D_n a^(J), D_n=iP_n.

Its coefficient of h^j is (∂_t−D_1)a_j −Σ_(n=2)^(j+1)D_n a_(j+1−n). Therefore the proposed recursion cancels every coefficient j=0,…,J. To obtain its uniform O(h^(J+1)) remainder, expand B_h through order J+1 and retain the O(h^(J+2)) Taylor remainder before dividing by h. Since only finitely many smooth amplitudes are involved, that is legitimate and gives exactly the claimed exponent, not an extra or missing h.

Why the derivative bounds really exist: the source's specified-time graph has X_a≥1−2·10^(−8)>0 and X(a,y)−a bounded. It is onto and has a global inverse. The trigonometric Hamiltonian has all derivatives; its bounded real vector field has a smooth/analytic flow on the fixed interval. Smooth implicit inversion gives every fixed finite phase derivative on enlarged compact charts. This conclusion requires no quantitative all-order estimate and no radius uniform in J. In the scalar transport recursion, the transport coefficient and zero-order coefficient are smooth; induction on j using integration along characteristics constructs a_j with every needed finite derivative on those compact charts. The forcing only uses previous amplitudes. Thus fixed-J uniformity is proved by the source plus finite smooth ODE induction, rather than assumed from an unproved long-time analytic continuation.

The higher D_n inherit the same branch gluing: adding the source's affine phase differences changes S_x only by integers, all higher x derivatives remain unchanged, and every e(l S_x) and symbol derivative is periodic. Initial a_0=1 and a_j=0 preserve gluing by transport uniqueness. Hence the four-branch sum solves the correct cyclic finite-shift equation even at wraparound.

The four finite branches have the sqrt(h)/2 prefactor. Consequently the residual matrix R=(∂_t−iA_N/h)V has entries O_J(h^(J+3/2)), operator norm ≤N max|R_jk|=O_J(h^(J+1/2)), and exact V(0)=M_N by the actual Gauss identity. Unitary Duhamel on the fixed interval gives ||U(t)−V(t)||≤∫||R(s)||ds=O_J(h^(J+1/2)). Real phases are important here: the oscillatory factors have modulus one. The fixed physical τ=10^(−80) lies inside the proven interval. No numerical startup estimate or uniform growing-J claim follows.

## All signed modes and all partitions

Let q=(1−δ)^(−1). Neumann inversion gives ||V^(−1)||≤q, while ||V||≤1+δ≤q. Positive powers telescope without commutation. For p>0 the exact negative identity is

V^(−p)−U^(−p)=Σ_(j=0)^(p−1)V^(−j−1)(U−V)U^(−p+j).

The latter has norm ≤δΣ_(j=1)^p q^j≤pδq^p. Adjoint powers instead apply positive telescoping to V* and U*. Both yield |T_V(n)−T_U(n)|≤N|n|δq^|n| and |T_V(n)|≤Nq^|n|, with exact zero discrepancy at n=0. This explicitly absorbs possible finite-time growth of a nonnormal approximant.

For any partition π with ℓ blocks and block sums n_B, telescope the scalar product. The one changed factor contributes N|n_B|δq^|n_B|; all other factors contribute N and their possible q growth. Summation gives δN^ℓ s_πq^s_π, s_π=Σ_B|n_B|≤Σ_a|m_a|. A zero-sum block is an exact N factor, never an omitted term. The one-block partition has zero discrepancy; all-zero tuples do too.

If d=k−1 and W is supported in [−σ,σ]^d, there are at most (2⌊σN⌋+1)^d lattice modes and Σ_a|m_a|≤2dσN. Define M_N=N^(−d)Σ_m|W(m/N)|=O_W(1) and A as the exact support bound in the note. Multiplying the partition estimate by N^(−k), summing modes, and using d=k−1 gives

Aδ M_N q^(AN) Σ_π |μ(π)| N^|π|.

The last sum is N(N+1)…(N+k−1), by counting permutations with each partition as their cycle supports. Hence the error is O(N^kδq^(AN)), not O(Nδ). The complete Fourier normalization and every Möbius counterterm are retained. This is an absolute bound on the approximation error, not absolute comparison of the actual deterministic spectrum with CUE.

With δ=C_JN^(−J−1/2), Nδ→0 for fixed J≥1; q^(AN)≤exp(ANδ/(1−δ))→1. Thus J=k suffices, and J≥ceil(k+A_target−1/2) gives O(N^(−A_target)). No one fixed finite J is asserted to cover all k. The canonical displayed two-amplitude J=1 bound alone does not provide pair convergence by this estimate.

## Convention and spectral boundary

Laurent T(n)=Tr(V^n) has the exact distinct-index eigenvalue identity, including defective nonnormal matrices, because traces of all integer powers equal sums of eigenvalue powers with algebraic multiplicity. It is a Laurent algebra statement, with no positive circle measure unless additional unitarity is present.

Adjoint T(n<0)=Tr((V*)^(−n)) must be inserted after forming each block sum. It is a path-friendly surrogate and not factorial eigenvalue algebra. For N=1, V=[6/5], its m=1 pair polynomial is 11/25 although there are no distinct pairs; the Laurent polynomial is zero. This is a decisive boundary already stated correctly in the target. The two tables themselves are different, but their transforms are each o(1) away from the exact U target at the chosen order, so their difference is o(1).

Subtracting the same correctly chosen ensemble reference from both transforms proves the asserted iff. It does not estimate either ensemble discrepancy. Long powers are ordinary products of the explicit one-step WKB matrix, potentially with enormously many paths; no evolved long-time WKB phase is asserted. The every-bandwidth extension must be applied to U's positive factorial measures. A future symmetry-block application must use its actual dimension and a norm approximation on that block; the present model construction is for the displayed full odd-N operator.

## Independent finite controls

These scripts were written from the definitions during this review; the author's fixture was neither imported nor used as the definition.

- `python3 /workspace/shared/bgs_factorial_wkb_review/check_independent.py`: passed exact rational checks. A genuinely nonnormal rank-one perturbation of a 3-cycle, with known exact operator error 1/40, passes 50 signed trace bounds, 12 matrix inverse telescope identities, and 9,336 partition-product bounds for k=2,…,5 and leading modes in {−1,0,1}; 5,604 tests include zero blocks. A separate nonnormal triangular matrix passes 120 Laurent/distinct-index identities including k>N. A defective 2×2 Jordan matrix passes 17 positive/negative trace-power identities. Scalar adjoint counterexample passes.
- `python3 /workspace/shared/bgs_factorial_wkb_review/check_raw_gauss.py`: passed 912 exact rational raw/midpoint phase checks (odd N≤31), 32 exact cyclotomic Gauss identities covering all odd N residues modulo eight and all t modulo eight, and 5,456 modular phase-closure checks for all matrix indices at odd N≤31.

Outputs are `checks.json` and `raw_gauss_checks.json`. These are finite algebra controls only. The analytic reasoning above, not these tests, proves the asymptotic reduction.

## Ownership, missing step, and safe promotion

Prior project ownership: FM-001 owns the raw/ordinary dictionary and prescribed frozen operator; `four_branch_parametrix.md` already owns the exact branches, global specified-time characteristic graph, gluing and displayed J=1 residual proof (within the FM-022 proof chain); TRACE-001/002 own the partition and Fourier identities; bridge §8 owns the distinct unitary-to-unitary stability result with reference correlation bounds; TRACE-010 owns the obstruction to all-order absolute deterministic CUE comparison and the signed-target boundary. The fixed-k unconditional trace-table perturbation estimate and its explicit arbitrary-fixed-J extension are the combination supplied by this candidate. Repository search did not identify an existing maintained statement of this exact combination; no global literature priority is claimed.

No mathematical correction or missing lemma is required for the reduction as stated. For standalone promotion, it would improve readability to name the finite-J transport/Duhamel argument as a lemma and explicitly state the Taylor expansion through J+1 with remainder J+2 before dividing by h. That is an exposition improvement, not a gap in the given finite-order argument.

The remaining substantive missing theorem is exactly the signed compact-Fourier ensemble comparison for the constructed WKB trace table, for every fixed k and compact support, with every path and partition counterterm retained. This is equivalent to TRACE-005 at the selected J; replacing its input by an explicit table does not solve it or weaken it to a finite path family. Safe promotion: an independent-internal-reviewed constructive reduction, retaining TRACE-005/BGS as OPEN; no spectral law for V, no long-time Egorov, no effective startup, no external-referee or analytic formalization certificate.
