# Independent audit of ordinary compact-stratum centering

7 October 2026. Bounded proof audit; no source, canonical, staging, or publication edits. The mathematical audit below was independently reconstructed from the target statement and exact source definitions. The executable controls were reproduced unchanged and inspected, not presented as a newly written independent checker.

## Claim and primary verdict

**Proved as written on the stated almost-everywhere, fixed-N domain.** The normalized claim is: for odd N≥3, every labelled mixed circle/open-disk stratum has the ordinary centering identity (9), with the distinct coarea factor (5) and gauge factor (7); the completed compact source and every fixed holomorphic source derivative satisfy (13) and the explicit, deliberately large majorant (17). No decisive mathematical defect was found in Sections 3–7 or the supporting low-N normalization controls.

Acceptance is restricted exactly as follows:

- The all-stratum centering/source theorem is for odd N≥3. N=1 and N=2 do not permit discarding their non-centerable positive-measure sectors. Their stated special cases are correct.
- Centering is on the stable domain, whose complement is null for the product measures at N≥3. Singular/nonunique configurations are not assigned a unique center.
- The original source identity is imported from the accepted four-family compact theorem on |a|,|b|<1. The compact expression and its estimates continue on |ab|<1; this does not assert that the raw phase integral is defined throughout that continuation domain.
- Source sets are compact, the derivative order is fixed, and the Cauchy neighborhood used in (17) remains inside the source domain. The epsilon estimate assumes 0<ε≤1/(N+3).
- All estimates are fixed-N absolute errors. There is no positive full signed-source probability law, no N-uniform coefficient norm, no normalized microscopic tail theorem, and no BGS conclusion.

## Exact revision and dependency graph

Target: `../bgs_wave2_centering/compact_stratum_centering.md`, SHA256 `e7ce0e1cfb780732481eb92d773339046c9ac481a29729f7904709e6cd62f205`.

Packet manifest SHA256: `22e8254203473334b8dec4ff7eb5c6a227435ecaaf51e7c734a30c6ce321dffc`. All eleven artifact hashes in that manifest were independently recomputed and agree.

The only mathematical source definition imported here is the checked snapshot's `mathematics/compact_phase_pair_identity.md`, SHA256 `4b821bd3c4d67e0f07b32982be8ec06a5e7592d8574aa34c99f67b382b2060f3`, Sections 2, 4, and 5: local odd order γ,β,α,δ; the two positive circle operations and two negative disk operations; the site/flavor block placement in (T); and the BB-pivot source denominator. This audit does not re-audit the already accepted compact-projector theorem or its external literature leaf.

Dependency chain:

1. Stable tuple → proper, strictly hyperbolically convex potential → unique smooth interior center.
2. Centered closed-disk tuple, odd N → second-moment bound → positive gauge determinant and regular slice.
3. Euclidean sum-map coarea plus the ordinary delta insertion → the exact mixed-stratum identity.
4. Accepted compact source → finitely many bounded extracted coefficient functions → apply the ordinary identity sector by sector.
5. Center near boundary → at least (N+1)/2 coordinates in one boundary cap → anchored subset probability → signed-source total-variation error.
6. Finite exterior/commuting quotient algebra and BB pivot → explicit coefficient majorant; Cauchy estimates → derivative version.

No new external theorem is needed for steps 1–3 or 5–6.

## Obligation checks and decisive derivations

**Center existence, exceptional set, and N=1/N=2: passed.** At an occupied boundary point of multiplicity h the numerator can lose at most 2h logarithmic powers, whereas the denominator contributes N. Thus stable tuples have a proper potential, including tangential approaches. The geodesic Hessian at the origin is a sum of nonnegative terms, with equality only for a single antipodal boundary pair. Möbius covariance transfers this criterion along any geodesic. A stable tuple cannot lie entirely in one antipodal pair. The center equation follows by Wirtinger differentiation. If h>N/2 it is impossible by real projection; if h=N/2 equality forces exactly two distinct equally weighted boundary points. These have a geodesic family of centers, not a unique one. This also verifies each low-N case: one disk center, no one-circle center; all two-disk tuples uniquely centerable; mixed circle/disk pairs not centerable; distinct circle pairs nonunique.

**Odd-N nondegeneracy: passed.** Rotate the square-sum to be nonnegative real. Its magnitude is Σx_i²−Σt_i²≤Σx_i² with x_i∈[-1,1], Σx_i=0. At a real box-slice vertex all but at most one coordinates are endpoints. For odd N all N endpoints cannot sum to zero; the N−1 endpoint sum is even, so the remaining coordinate must be zero. The maximum is N−1, yielding Δ≥N²−(N−1)²=2N−1. The witness with paired ±1 and one zero proves sharpness only for the closed polydisk, as stated.

**Mixed coarea versus gauge determinant: passed.** A disk gives two real tangent columns and hence I₂ in DS DSᵀ; a circle gives the unit tangent i y_i. Thus the eigenvalues are (2N−k±|Σ_B y_i²|)/2 and the coarea Jacobian is their square-root product, (5). The lower bound for k<N is N(N−k) after squaring. For the all-circle slice it is Δ/4. Separately, differentiating T_z with z held fixed and then using Σy_i=0 gives [-N dp+(Σy_i²)d p̄]/(1−|p|²); its real determinant is Δ/(1−|p|²)². These factors are different. Combining the latter with the N sitewise circle/disk Jacobians gives precisely exponent 2N−k−2 and denominator powers 2/4 in (10). The original Haar and area constants remain. Eliminating one disk coordinate leaves π^(-N), consistent with the N=1 calibration.

**Ordinary exact formula and a.e. domain: passed.** The sum map is regular on every odd-N centered stratum. The unique-zero two-dimensional delta formula applies on the stable domain; nonnegative integrands permit exhaustion and Tonelli, and absolute integrability handles complex g. No extra rotation quotient or super-Jacobian is introduced. Null unstable original configurations do not affect the integral.

**Completed source, signs, and derivative domain: passed conditional only on the already accepted compact source identity.** The exact local functional agrees with the target's four operations and ησ=(-1)^(N−|Bσ|). Odd extraction and commuting-flavor differentiation precede evaluation and ordinary centering. The BB body resolvent is bounded by (1−|ab|)^(-1) on the closed BB polydisk. Finite odd extraction and polynomial numerator dependence give every coefficient and every fixed source derivative a finite compact-source bound. No body-only surrogate is substituted for the full signed functional.

**Cap lemma and anchored union bound: passed.** For N=2m−1, outside radius (N+3)(1−r), the exact Möbius identity implies Re y_i<−1+2/(N+2). If at most m−1 coordinates are in the cap, the centered real sum is at most −1+(N+1)/(N+2)<0. Hence some m labels lie in a cap of radius τ=(N+3)ε. With a selected circle anchor, each further selected circle has probability 2 arcsin(τ)/π≤τ and each selected disk has probability at most 4τ². This gives 4^(m−j)τ^(N−j). With no selected circle, the selected disk anchor must lie in a shell of probability at most 2τ, yielding 2·4^(m−1)τ^N. A fixed anchor for each labelled subset avoids any angular-covering factor. The sum over subsets is a union bound; overlapping subsets do not require division. The binomial limits in Q correctly cover all feasible j.

**Signed-source total variation and universal coarse estimate: passed.** Each omitted sector integral is bounded by its coefficient supremum times the product-measure tail; taking absolute values and summing gives (13), without asserting positivity or cancellation. For τ≤1 each exponent N−j≥m−1 and each cap coefficient is at most 2·4^(m−1). Vandermonde gives at most binom(N,m) subsets, establishing (17)'s cap factor. The worst exponent is (N−1)/2.

**Explicit algebra majorant and Cauchy extension: passed.** The displayed A,B,C,D blocks follow by multiplying the exact source supermatrix, including the minus sign in the lower-right block of Ztilde. The coefficient-sum operator norm is submultiplicative under exterior multiplication and the commuting square-zero quotient. That quotient preserves precisely the selected coefficients because no selected commuting variable is differentiated twice. The A perturbation has degree two in only 2N odd generators; its resolvent series stops after power N, giving H. The independent block bounds give ||C||≤q₀N+u₀N², ||B||≤v₀N+r₀N² and ||D||≤1+(v₀+r₀)N², hence L. A and its Schur complement have even, commuting entries. Their Leibniz determinant bounds are N!H^N and N!L^N, so every selected coefficient is bounded by (N!)²(HL)^N. There are 4^N sectors. The stated complex-polydisc Cauchy estimate supplies ν!δ^(-|ν|)M_N(Kδ). The constants are large but specified and valid.

## Exact twenty controls: reproduction and actual scope

Command: `python3 checks/reproduce_exact20.py > checks/run.log`, executed from an unchanged copy of the pinned checker inside this review directory. Exit code 0. The reproduced result JSON equals the frozen result JSON exactly; all twenty controls pass. Script SHA256: `44b0afc0181d2090dda2cc6b9b007b0bcb16b869948ebe47b32979057a7c8f1d`.

Coverage inspected independently:

- Eight raw real Jacobian comparisons: every N=3 circle count k=0,1,2,3 at p=0 and p=1/5+i/7. The configurations satisfy the actual circle/open-disk and centering constraints. The all-circle shape factor is 2/√3, not one.
- Six fixed-z gauge-derivative controls at N=1,2,3,5,7,9.
- One N=1 disk normalization calibration.
- One N=2 all-disk global mass control. The angular Fourier coefficients produce 8(n+1)/[(2n+1)²(2n+3)²], equal to the displayed telescoping difference, with sum one.
- One N=3 all-circle global mass control. Two labelled orientations, Δ=9, J=3/2, and dH=√3 dφ yield 3√3/[π²(1+|p|²+|p|⁴)], whose disk integral is one.
- One N=3 zero-source cutoff control. Only the all-circle body sector remains at zero sources; the exact radial density gives (15), with leading loss 2√3 ε/π. This confirms the sharp first-order worst exponent at N=3 and the failure of an exact cutoff normalization.
- One grouped real box-slice vertex check through N=31. This tests possible vertices, not all complex tuples.
- One factorized completed-source check at U=I₃ and nonzero sources, with local value 19/18 and cube 6859/5832. It tests source signs and normalization, not a nontrivial coupled source or a cutoff integral.

These controls do not test the all-N cutoff bound or all-N algebra majorant by enumeration. Those are accepted on the separate proofs above. Repeating an unchanged checker is reproducibility evidence; it is not claimed as independent implementation evidence.

## Remaining gap and strongest safe outcome

There is no remaining gap within this finite-N centering/cutoff theorem beyond its imported accepted source identity. The unresolved next implication is an N-uniform estimate or controlled signed cancellation of the actual source-differentiated coefficient combination, including circle boundary strata, at ab=exp(-2s/N), sufficient after N^(-2) normalization. H, M_N, 4^N, and the cap factor give no such result, and no normalization lower bound has been introduced. No assertion that a prescribed ε_N yields a vanishing normalized microscopic error follows.

The strongest safe outcome is the exact odd-N ordinary centered representation plus an effective fixed-N completed-source cutoff approximation, including derivatives. Full BGS remains open.
