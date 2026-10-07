# Independent audit: global scalar bosonic coercivity

Date: 7 October 2026. Canonical BGS base observed at `d37c92e563d10d25bb1d6ab85bedffc1f160f773`, with a pre-existing integration overlay. No canonical files edited and no publication performed.

## Primary verdict

**Proved as written.** For every positive integer N, every unitary U with P_ij=|U_ij|², max P_ij≤C/N and ||P−J||₂≤ρ<1, and every diagonal strict contraction Z with Σz_j=0,

S_U(Z) ≥ H(Z)/(2K²),

where S_U(Z)=log|det(I−UZU*Z*)|−logdet(I−ZZ*), H(Z)=Σ−log(1−|z_j|²), and K=1+√(C−1)/(1−ρ).

The reviewed frozen statement/proof is `../bgs_global_phase_coercivity/report.md`, SHA-256 `b6cf72d2d724e9b39b5726254a542dc417641ab96dd2f539f41b7fc5bbdb0b2e`. This verdict imports the exactly checked generalized exponential metric increasing theorem, not any universality statement. The assumptions imply C≥1 and ρ≥0 whenever the class is nonempty. All determinants and logarithms are well-defined in the strict disk.

Separately, the frozen report's common scalar Möbius invariance, unique global conformal centering, and displayed ordinary real bosonic Jacobian are correct. Their scope is described below. The proposed later block-matrix extension is outside this audit.

## Dependency graph and obligation matrix

1. Strict contractions and scalar bosonic source identification: passed. Weidenmüller's (7), (8)–(10), printed pp.3–4, gives the claimed real bare-body action and sign. Spectral regulators and differentiated sources remain separate.
2. U(N,N) representative, block determinants and orientation: passed by direct finite-dimensional algebra.
3. Polar/Cartan singular-value dictionary: passed by direct polar decomposition; no additional Lie-group theorem is imported.
4. Generalized EMI for all Ky Fan norms: passed against Bhatia's primary preprint, Theorem 4/(15)–(16), printed p.5.
5. Weak majorization → convex log-cosh sum → diagonal pinching: passed. This retains the exact modular bound without an additive N log 2 error.
6. ℓ1 and ℓ∞ inverse estimates with constant K: passed, including nonnormal P and C=1.
7. Modular Jensen and quadratic scaling: passed.
8. Conformal centering Σz=0 → minimizer of the translated log-cosh potential: passed. No substitution Σx=0 is made.
9. N=1, all-zero Z, zero coordinates, unequal radii, strict near-boundary points: passed analytically; finite diagnostics separately recorded.
10. Full supermeasure, source poles, Grassmann-integrated bounds, entropy/normalization and large-N spectral conclusions: not addressed by the theorem and explicitly out of scope.

No circular dependence or unverified source leaf was found in this scalar proof.

## Decisive proof reconstruction

### Determinant orientation and factors

Write x_j=atanh(|z_j|)z_j/|z_j|, with x_j=0 at z_j=0, W=diag x, X=[[0,W],[W*,0]], and K_U=diag(U,U). Let C₀=(I−ZZ*)^(−1/2). The source's g=exp X has blocks [[C₀,ZC₀],[Z*C₀,C₀]]. Direct multiplication gives the frozen report's upper blocks of T=g^(−1)K_Ug:

F=C₀(U−ZUZ*)C₀,
G=C₀(UZ−ZU)C₀.

J₀-unitarity gives FF*−GG*=I. Moreover det(U−ZUZ*)=det U det(I−U*ZUZ*), while the latter determinant is the conjugate of det(I−UZU*Z*) by adjoint and cyclic determinant identities. Therefore |det F|=exp S and exp(2S)=det(I+GG*). This verifies the exact orientation, not just a commuting or real special case.

For T=V exp L, J₀(T*T)J₀=(T*T)^(−1) implies L anticommutes with J₀. Thus L=[[0,B],[B*,0]], and V is block-diagonal unitary. If t_j are B's singular values, T's singular values are e^(±t_j), F's singular values are cosh t_j, and S=Σlogcosh t_j.

Taking Y=K_U X K_U*, the positive matrix exp(−X)exp(2Y)exp(−X) is TT*. Bhatia's EMI applied to A=2Y, B=2X and the Ky Fan 2k norm has left side 4Σ_(j≤k)s_j(W−UWU*) and right side 4Σ_(j≤k)t_j. The factors cancel exactly. Hence s(W−UWU*) is weakly majorized by t. Diagonal pinching then yields

S≥Σφ(|v_j|), φ(t)=logcosh t, v=(I−P)x.

The convex-sum implication can be proved from positive-part integral representations; pinching is an average of unitary conjugations and Ky Fan convexity. Neither needs a stronger source theorem.

### Inverse and nonlinear centering

Let A=P−J and R=(I−P+J)^(−1)=I+Σ_(k≥1)A^k. Each row and column of A has squared Euclidean norm at most (C−1)/N. Multiply one such row/column by A^(k−1), use ||A||₂≤ρ and then ℓ1≤√Nℓ2. Both absolute row and column sums of A^k are bounded by √(C−1)ρ^(k−1). Thus ||R||₁,||R||∞≤K. This argument does not assume reversibility or normality.

For x⁰=x−(mean x)1, Rv=x⁰ exactly. The matrix |R|/K is doubly substochastic. Row Jensen, with unused weight placed at zero, followed by the column sums gives Σφ(|Rv|/K)≤Σφ(|v|). Since φ(t)/t² is decreasing on t>0, φ(t/K)≥K^(−2)φ(t). The direction of this inequality is essential and correct.

Finally F(b)=Σφ(|x_j−b|) is a differentiable convex function on the real plane. Its gradient at zero is −Σtanh(|x_j|)x_j/|x_j|=−Σz_j=0. Thus F(mean x)≥F(0)=H/2, proving the claim. The condition is nonlinear in x. It is neither the assertion Σx=0 nor a change of integration slice.

### Endpoints and necessity

For N=1, the hypothesis Σz=0 forces z=0 and S=H=0. For C=1, row sums force P=J exactly, so A=0, R=I and K=1; no 0/0 series formula is needed. Coordinates z_j=0 use the continuous radial logarithm. All |z_j|<1 may approach one independently; no uniform interior cutoff entered the proof. Centering is necessary: Z=aI gives S=0 but H>0 for a≠0.

## Separate audit of scalar gauge claims

The frozen report's cocycle holds with its displayed order even for noncommuting matrices: clearing the left factor I−conjugate(a)A and right factor I−aB* leaves (1−|a|²)(I−AB*). Applying it to A=UZU*, B=Z and using spectral invariance of the determinant factors proves S_U(m_a(Z))=S_U(Z).

For the centering potential

F_z(a)=Σlog|1−conjugate(a)z_j|²−Nlog(1−|a|²),

strict interior z makes it proper as |a|→1. Its critical equation is precisely Σm_a(z_j)=0. Under a common disk automorphism it changes by a constant independent of a. At a point moved to zero, restriction to a(t)=e^(iθ)tanh t has second derivative 2Σ[1−Re(e^(−2iθ)w_j²)]>0. Transporting along every geodesic establishes strict geodesic convexity, hence a unique global minimizer and a unique center. This is conformal centering, not Euclidean centering of hyperbolic logarithms.

For w_N=−Σ_(j<N)w_j and z_j=(a+w_j)/(1+conjugate(a)w_j), dividing each differential by q_j=(1−|a|²)/(1+conjugate(a)w_j)² gives a unit coefficient on dw_j. Replacing the last output row by the sum of all rows has determinant one in complex coordinates. Since Σdw=Σw=0, the remaining 2×2 real block is [N da−(Σw_j²)d conjugate(a)]/(1−|a|²). Its determinant gives exactly

(N²−|Σw_j²|²)(1−|a|²)^(2N−2) / ∏|1+conjugate(a)w_j|⁴.

The factor is strictly positive because |Σw_j²|≤Σ|w_j|²<N. Thus there is no omitted factor N in the constrained-coordinate volume convention. N=1 gives one. This is an ordinary 2N-dimensional real Jacobian only. It neither proves nor substitutes for a super-Berezinian or the validity of a full supersymmetric gauge fixing.

The common-radius lower bound in §7 is also correct: the logarithmic eigenphase factor is concave as a function of cos θ, so it lies above its endpoint chord; Re Tr(UVU*V*)≤ρN on Σv=0. The F₄ alternating-sign example has involutive Q with trace zero, hence two eigenvalues of each sign and S/H→1/2. The flat-matrix constant 1/2 therefore cannot be uniformly improved for all dimensions. This example is not the actual odd-dimensional BGS map.

## Exact source check

Bhatia, *On the exponential metric increasing property*, ISI preprint isid/ms/2002/14, dated May 10, 2002. Primary institutional URL: https://www.isid.ac.in/~statmath/2002/isid200214.pdf . The PDF has 8 physical pages; printed p.5 is physical PDF page 6. Theorem 4, (15)–(16), explicitly covers complex Hermitian matrices and every symmetric gauge/unitarily invariant norm. The source proves this result, rather than conjecturing it. Application is at size 2N and Ky Fan norms; no positivity of X or Y is required. PDF SHA-256: `dbd04403787b5ff2854d48b4ad83d14b0f46f76e96e7b790006e8843976d5f13`.

I independently located the institutional abstract/PDF in web search, inspected the full cached primary text and visually inspected the rendered theorem page. Live web opening timed out; the already acquired institutional PDF was reused, with its hash matched to the author's frozen source. Published metadata is Linear Algebra Appl. 375 (2003), 211–220, DOI 10.1016/S0024-3795(03)00647-5; published theorem numbering was not imported.

Weidenmüller, arXiv:1812.00655v1, primary URL https://arxiv.org/pdf/1812.00655v1, was checked in the previously authenticated project-local source. Its (7) gives the bosonic domain; (8)–(10) and the paragraph after (9) establish bare-action sign and separate source factors. No graph universality conclusion was imported. Prior balanced-phase report/domain addendum and canonical source authorities were read. This audit makes no global novelty claim.

## Independently coded controls and execution boundary

`checks.py` was written without reading/importing the author's diagnostic implementation. It tests the determinant action directly and uses a different matrix-ball displacement representative. The route was supplied as a hypothesis, so this is an independent reconstruction/implementation, not a claim of blind discovery or independence from all shared-model error.

Command:

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 checks.py > checks.json

All 726 bounded controls passed for N=1,2,3,4,5,8,12,20. Families include Fourier, two Haar draws, two near-identity exponential unitaries, centered random configurations, balanced polygons, and unequal-radius one-against-many configurations. Largest radius is 1−10^(−10). Tests cover determinant/Cartan identities, EMI partial sums, pinching, both inverse norms, centering and modular inequalities. Complex128 maximum relative Cartan/log-cosh discrepancy was 3.92×10^(−8) in near-boundary cases, within the declared 10^(−7) tolerance. Small negative zero-level margins were at roundoff scale. Five separate 100-digit 2×2 controls reach radius 1−10^(−60); 24 high-precision scalar scaling controls and the uncentered negative control also pass.

`gauge_checks.py` independently differentiates the complete real coordinate map symbolically and verifies the ordinary Jacobian exactly at rational interior points for N=1,2,3,4. It also verifies the F₄ sharpness polynomial identity exactly, performs 100 bounded Möbius/action/centering tests with three root starts each for N=1,2,3,4,8, and 20 noncommuting 3×3 cocycle controls. All pass. The first gauge run had an implementation-only N=1 Python-integer/symbolic-zero conversion error before checks completed; using SymPy zero repaired it and the complete run was repeated. It was not a mathematical counterexample.

These samples are not exhaustive, do not certify universal matrix inequalities, and are not asymptotic evidence. The universal verdict rests on the analytic proof and checked EMI theorem. No analytic formalization, full repository build, actual extremely-small-coupling numerical test, fermionic computation, or super-Jacobian test was performed.

## Exact remaining gap and strongest safe conclusion

There is no remaining gap in the stated scalar inequality or in the separately scoped ordinary scalar gauge claims. The resulting bound e^(−S)≤∏(1−|z_j|²)^(1/(2K²)) supplies a global pointwise scalar-body suppression estimate.

It does not imply that a dimension-growing supersymmetric correlation integral has a small omitted tail: inverse-factor derivatives after Grassmann integration, source/regulator poles, the admissible super-coordinate transformation/Berezinian, entropy and normalization, and signed/all-order cancellation still require estimates. Even a completed annealed law would not estimate the original deterministic off-charge defect. TRACE-005 and BGS remain open.
