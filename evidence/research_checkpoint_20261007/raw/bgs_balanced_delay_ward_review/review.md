# Sealed independent review: boundary delay and stationary phase Ward identity

Date: 7 October 2026. Read-only canonical base: d37c92e563d10d25bb1d6ab85bedffc1f160f773. All review writes are confined to this directory. The canonical base already had an unrelated integration overlay; no such overlay is attributed to this reviewer. No new research route or actual-model limiting proof was attempted.

## Normalized claim and primary verdict

**Primary verdict: proved as written, for the two accepted versions and their expressly bounded claims.**

1. **Boundary delay:** for the explicit tensor family V_d=(F_5 P)^{tensor d}, d>=1, N=5^d, entry intensities are exactly 1/N, the classical transition is J_N, the reverse-kernel norm is q_0^d with q_0<1, and the unregularized scalar one-channel angular delay at 1 has infinite phase-averaged second moment. Accepted source: inputs/boundary_delay_obstruction.md, SHA-256 ce752ed7f8ed8780bf32c449a040b0776b0ec755d4c9d9ed8c42cd2871e91232.

2. **Ward/Poisson:** for every fixed N>=1, U in U(N), and s>0, the phase-stationary ensemble DU obeys the exact finite-N signed identity (12), with its stated overlap Gram matrix, Haar reference, heat normalization and universal smooth Poisson test. The balanced Abel CUE limit is equivalent to the one-test signed estimate (13); that estimate is not proved. Accepted source: phase_ward_identity_v2.md, SHA-256 1fccba816add7065c611edf21164bbef36fa4bad9edf6e30bb39ff9b8d737479.

The original Ward equations and derivation survive. Its presentation required two small corrections before clean promotion: the Peter–Weyl expansion of the Abel observable is not finite, and Haar eigenvectors alone do not imply a CUE eigenvalue law. The authorized v2 changes only those sentences. The original source is retained unchanged at SHA-256 d439dccbb6511d0d1bcd0439bd28df2f0d76849bdf17727c9dccd0c96a58c2bf. The exact patch is phase_ward_v1_to_v2.diff and old-to-new mapping is correction_mapping.json. The v2 wording was checked after editing; neither correction changes equations, assumptions of the main identity, or the open target.

## Dependency graph

Boundary claim:

- explicit Fourier-permutation seed [internal algebra]
- exact seed spectrum and irreducible nonmonic trace polynomial [internal algebra, exact controls]
- non-root-of-unity lambda -> unique tensor eigenvalue lambda^d [internal proof]
- dephased compression identities + complex dark vector -> rank-two leakage derivative [internal proof]
- common phase direction -> rank-three chart [internal proof + ordinary inverse function theorem]
- unitary block determinant -> positive Blaschke delay sum [internal proof]
- local nonnegative lower bound -> logarithmically divergent second moment [internal integration]
- common phase invariance -> transfer observation point to 1 [internal proof].

Ward claim:

- phase Brownian stationarity + unitary perturbation -> generator (4) [internal proof]
- Haar-row moments + translation invariance -> reference normalization (8) [internal proof]
- exact all-index CUE trace mean -> c_(N,s) [verified primary source, elementary summation]
- compact heat positive spectrum + smoothness -> Poisson solution (10)–(11) [verified normalization/source and fixed-N spectral calculus]
- apply stationary generator to that solution -> exact defect (12) [internal proof]
- nonzero bounded scalar factor (N+1)/N -> equivalence (13) [internal proof]
- actual U_N joint signed overlap estimate -> CUE Abel limit [**open**, not an imported input].

No cyclic dependency was found. Neither auxiliary family nor numerical comparison is used to supply the final open arrow.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| F_5 P column convention, flatness and dephasing | Passed | Direct cyclotomic seed reconstruction |
| Whole spectrum, not only one eigenvector | Passed | Newton-identity characteristic polynomial and analytic even/odd split |
| lambda not a root of unity; tensor simplicity | Passed | Degree-four nonintegral trace; exponent-count proof |
| Reverse norm is strictly less than one | Passed | Equality in every row triangle/Cauchy inequality would force Q=J |
| Compression eigenvalue remains simple | Passed | Normal compression and unit-modulus eigenvector correspondence |
| Leakage rank two, common-phase rank three | Passed | Exact derivative and nonzero real minor; independent phase direction |
| Transfer sign, adjoint and extra z factor | Passed | Exact block multiplication below; rational N=2,3,4 controls |
| Divergent second moment for every d | Passed | Positive local lower bound; no finite sampling extrapolation |
| Standard Brownian quadratic variation and cotangent sign | Passed | Direct eigenvalue differentiation and independent matrix jets |
| Diagonal G_jj and denominator N+1 | Passed | Haar-row moments; projected common-angle term |
| Collision behavior and simple-locus measure | Passed | Symmetric gradient divisibility and generic diagonal perturbation |
| All-frequency Haar mean | Passed | Diaconis–Evans 2.1(b), including m>N |
| Poisson inverse sign, existence, uniqueness | Passed | Fixed-N smooth inverse of negative heat generator |
| Original finite-expansion wording | Failed literally; corrected | Abel test has infinitely many Fourier degrees |
| Haar-basis calibration interpretation | Restricted explicitly in v2 | Vanishing overlap contraction alone is not stationarity |
| Actual-model signed expectation tends to zero | Open / not addressed | No joint overlap–spectrum estimate supplied |
| Off-charge terms and higher factorial orders | Out of scope | Remain separate obligations |

## Decisive boundary-delay reconstruction

The claimed odd block has eigenvalues lambda and -lambda^(-1); the even block has eigenvalues 1,1,-1. Exact computations recover the entire characteristic polynomial rather than assuming completeness from the displayed eigenvector. With x=lambda+lambda^(-1), x²=2-2/sqrt(5). If x belonged to Q(sqrt(5)), writing x=a+b sqrt(5) would force a²=1±2/sqrt(5), impossible for rational a. Thus its displayed primitive degree-four polynomial is minimal and nonmonic, so x is not an algebraic integer and lambda cannot be a root of unity.

Every tensor eigenvalue is a sign times lambda^(a-b), with a+b<=d. Equality with lambda^d forces a-b=d and hence a=d,b=0, leaving no other factors. Thus lambda^d is simple. A unit-modulus eigenvector u of the compression obeys bu=0 by norm conservation, so its zero extension is a full-unitary eigenvector. This gives the needed simplicity transfer without assuming it merely because one vector survives compression.

For dephased W, b d=-a b and d c=-a c. Differentiating (d D)u=lambda u and then applying b gives

    partial_k ell(0) = i lambda_0 b_k u_k/(lambda_0+a).

The eigenvector derivative term is essential. The denominator is nonzero because |lambda_0|=1 and 0<a<1. Two nonzero coordinates with non-real ratio make this a real-rank-two map. Along the common internal phase direction, d lambda/dt=i lambda while d ell/dt=0 at the dark point. Consequently leakage coordinates and eigenvalue angle form a rank-three chart. Normalization of the smoothly chosen eigenvector gives exactly 1-|lambda|²=|ell|² even though the perturbed compression need not be normal.

For T=[[a,B],[c,d_theta]], put

    S(z)=[[a,-z B],[c,I-z d_theta]].

Direct multiplication gives

    T* S(z)=[[1,c*],[0,d_theta*-zI]].

Taking determinants proves (6), including (-1)^(N-1) and the adjoint. Its numerator zeros are conjugates of compression eigenvalues. Unit-circle factors cancel, and all remaining angular derivatives are nonnegative Poisson kernels. The additional outer factor z in f supplies the +1 in (7). The exceptional fixed-boundary determinant is a nonzero phase polynomial because its multivariate constant term is 1, so its zero set has Haar measure zero.

In the rank-three chart, write rho=|ell| and x for eigenvalue-angle displacement. For |x|<=rho² and sufficiently small rho, |1-sqrt(1-rho²)e^(ix)|<=C rho². The selected Poisson term is at least c/rho². Its square integrated over this x interval and polar leakage coordinates is bounded below by a positive multiple of integral d rho/rho. Remaining coordinates can be restricted to a positive-volume box with Jacobian bounded below. This proves divergence, rather than observing a large finite sample variance. Finally h_(theta+t)(z)=h_theta(ze^(it)), so the angular-delay law is invariant under shifting the observation point. The d-dependent resonance angle therefore causes no loss at z=1.

## Decisive Ward/Poisson reconstruction

For exp(itH)V, ordinary simple-eigenvalue differentiation gives theta'_j=H_jj and the stated positive cotangent expression for theta''_j. With H=E_aa, |H_jk|²=w_ja w_ka. Independent real Brownian quadratic variations dt supply the factor 1/2 in Itô drift. Pair symmetrization of the ordered j!=k sum supplies the factor 1/4 in (4).

A Haar row has squared amplitudes with Dirichlet(1,...,1) law. Its second moments yield G^H=(ones+I)/(N+1). In the Hessian term, the all-ones part is the square of the common-angle derivative and vanishes on translation-invariant F. Combining the remaining diagonal Hessian with the off-diagonal drift gives exactly N/(N+1) times A_N. Dropping the diagonal/off-diagonal distinction would give an incorrect diffusion coefficient.

For collisions, permutation symmetry makes partial_j F-partial_k F divisible locally by theta_j-theta_k; the cotangent singularity is removable. The total operator is a smooth matrix derivative and is basis-independent at collisions. The simple-locus full-measure assertion is also valid: on each repeated eigenspace, projected coordinate vectors span that space; a hierarchical positive sum of selected independent rank-one forms has simple spectrum. A generic single diagonal coefficient vector works simultaneously on finitely many eigenspaces. Small phase perturbation then yields a simple spectrum, making the phase-family discriminant nonzero. Its real-analytic zero set has measure zero.

For fixed N,s>0, all derivatives of (9) converge because they grow only polynomially in Fourier index against q^m. The exact CUE mean uses the all-index moment, not stable Gaussian matching. The positive fixed-N heat gap makes the inverse on mean-zero smooth functions well-defined. With g=F-c, applying the generator to -integral P_t g dt gives g, so both the Poisson sign and the minus sign in (12) are correct. Smooth spectral calculus justifies differentiation; no N-uniform inverse or derivative bound is inferred. Heat commutes with scalar rotations and conjugation, so the solution retains the symmetries required for (8). Kernel constants and zero-Haar-mean normalization establish uniqueness.

The corrected Haar-eigenbasis control is necessary as a scope clarification. For example, a Haar-conjugated deterministic simple spectrum has Haar eigenvectors and zero conditional overlap defect, yet its eigenvalue statistics remain deterministic. Such a law need not be stationary under independent coordinate phases, so (12) cannot be applied to it. Version 2 says exactly this limitation.

The coherence identity is exact: |DU psi_j|²=|psi_j|² gives (I-P)w_j=c_j, and doubly stochastic P makes sum_a c_ja=0. Under ||P-J||<1, the inverse R gives w_j-1/N=R c_j, hence (15). “Centered” here means the coordinate sum is zero; no unproved phase expectation is needed. Bounding R does not evaluate the spectrally weighted signed covariance in (13).

## Independent finite controls and execution scope

The new script checks the seed in Q[t]/Phi_20 using field arithmetic, separately recovering all characteristic coefficients by Newton identities. Its controls are not reruns of the author's radical-algebra implementation. It checks the transfer identity on rational Cayley unitaries in dimensions 2,3,4. For the Ward generator it constructs second-order matrix jets of exp(it E_aa)V and compares their directly computed class-function derivatives with the eigenangle contraction. Tests include trace powers 1,2,4, a quartic statistic, and a mixed trace statistic in dimensions 2,3,4. Finite CUE Abel sums are checked for N=1,...,8, with diagonal-ensemble negative controls for N>1.

All 79 exact assertions passed. The first development attempt stopped on an unsupported Python int/ANP division; replacing 2/rt by the same rational field element 2*one/rt fixed the implementation typing issue. That failed attempt is preserved in results/attempt1.stderr. There was no mathematical counterexample or tolerance adjustment.

Reproduction:

    python checks/run_controls.py
    python checks/validate_manifest.py computation_manifest.json --root .

The v2 manifest pins the executed inputs before and after the recorded run, hashes the actual result/logs, and records resource caps. Arithmetic is exact; the run is bounded and deterministic. Neither finite checks nor agent agreement proves the analytic divergence, tensor-uniform conclusion, or actual-model asymptotic. Those first two are established by the proof reconstruction above; the last remains open. No Lean/formal certification, repository-wide regression, or publication is claimed.

## Exact surviving gap and strongest safe statement

The first surviving target is precisely, for the literal actual U_N and each fixed s>0,

    E_D R_(G-G^H) Psi_(N,s) -> 0.

Its full signed Hessian-plus-cotangent-gradient contraction must stay intact. The P gap controls an inverse in (15), and reverse-kernel decay is a different input; neither supplies the joint eigenvector-coherence/eigenphase estimate. Fixed-degree overlap moment information is insufficient for this N-dependent Poisson test.

The strongest safe checkpoint comprises the explicit obstruction to unregularized L² boundary-delay estimates and the exact finite-N Ward reduction with this missing target. It proves neither the actual balanced Abel CUE limit nor deterministic BGS. The next Work wave can start at (13), or at an already accepted positive-absorption reduction, while retaining the boundary-variance obstruction. No further experiment is needed to accept these two finite-N results.
