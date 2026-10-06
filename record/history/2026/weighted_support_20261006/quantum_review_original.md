# Independent audit: paired quantum factors approach 1; individual Z need not

Date: 6 October 2026. Read-only with respect to the canonical repository and candidate.

## Claim and primary verdict

**Primary verdict: conditional on a named input.** The new local statements Q1–Q10 are valid, using the already accepted actual local first-loop theorem and its verified radius-one extension. The final uniform weighted error O(N^(-1/2)) follows with **only** the additional positive leading-mass hypothesis Q11, sup_m sum_z rho_m(z)<infinity. This review does not accept Q11, weighted periodic equidistribution EQ, or the physical-leaf regularity argument on the strength of the candidate. Those are separate reviews.

More precisely, for fixed finite J>=0, h=(2*pi*N)^(-1), mh<=b, the literal unit-winding displacement d_m satisfies

- ell_1(z) is purely imaginary;
- |ell_1(z+d_m)-ell_1(z)|<=C_J independently of m and z;
- P_(z+d_m)P_z Z_(z+d_m) conjugate(Z_z)=1+O_(J,b)(sqrt(h));
- the selected normalized exact-box autocorrelation differs from its leading counterpart by at most C_(J,b) sqrt(h) sum_z rho_m(z).

These conclusions concern the prescribed real phases at tau=10^(-80), the original odd-N Weyl quantization, the actual fixed-J amplitudes, and the actual conditioned rotated boxes. They do not replace Z_z itself by 1. In fact h ell_1(z) can remain O(1).

There is **no additional unchecked quantum step** in this audit. Keep three levels distinct:

1. Local paired-factor convergence and the bound C sqrt(h) Z_m^cl are proved from the inherited accepted quantum inputs.
2. The O(N^(-1/2)) exact-box-versus-leading **comparison** requires Q11 only. W3 is needed if one supplies Q11 through the physical determinant definition of rho. Full EQ is unnecessary for this comparison.
3. O(N^(-1/2)) **decay of the coefficient itself** additionally requires decay of the leading coefficient, using the separately reviewed physical phase/weight dictionary and an adequate weighted transfer result such as EQ. Q11 alone does not provide this decay.




### Operator identity and bandwidth scope

The coefficient audited here is a summand of the prescribed **fixed-J WKB representation V_(N,J)**. It is representation-dependent and is not an exact intrinsic summand or observable of the unitary U_N. The unitary operator is unchanged; passage from V_(N,J) to U_N uses only the separately accepted aggregate operator/trace comparison.

- The local paired-factor theorem and weighted comparison hold for every **fixed finite J>=0** and fixed finite b with mh<=b. Equivalently, they hold on every fixed m/N band m<=B N, with b=B/(2*pi). Constants and the sufficiently-large-N threshold may depend on J and B; J does not grow with N.
- Comparison of one exact-box coefficient with the corresponding **global Fresnel coefficient of V_(N,J)** is certified here in the conservative contour band **1<=m<=2N** (and odd positive N), using the explicitly inherited summed absolute tail. No larger band is inferred by this audit.
- The actual U trace has the accepted aggregate estimate Tr U_N^m=Tr V_(N,J)^m+O_J(N^(3/2-J)) in that band for fixed J>=1. This gives no canonical orbit-by-orbit decomposition for U. For a complete fixed-k factorial comparison, the separate accepted reduction takes fixed J>=k. In particular the local J=0 assertion is not a J=0 transfer to U.

Frozen reviewed candidate: `quantum_homoclinic_first_loop.md`, SHA-256 `cad314323df7e5668133cba7f29e3a7b6afb2014bb3b42cd11a86283fd200454`.
The sibling physical dictionary, SHA-256 `5bee8e6b45ae785d8fa14c4caf40e959cd49c79cbbd97e319a9ff4eb1b9037ff`, is reviewed separately. W3/W9 normalization was reconstructed here, but no independent verdict on its bundle/holonomy regularity is made.

## 1. Dependency graph

1. Actual finite-shift raw Weyl formula + real Hamilton–Jacobi phase + real initial amplitudes -> parity of P_n and a_1.
2. Real leading logarithmic amplitude + rotation c=exp(-i*pi/4) + N^(-1)=2*pi*h -> imaginary first connected coefficient.
3. Global strict concavity + literal real winding interpolation + massive inverse -> summable stationary-point variation.
4. Local phase/amplitude derivatives + stationary variation -> entrywise summable K' and covariance G'.
5. Finite Wick contractions + odd degree at each of the two W vertices -> an obligatory cross contraction -> uniformly bounded ell_1'.
6. Accepted conditioned-box expansion + imaginary ell_1 + bounded unit increment + Gaussian probability -> exact paired factor 1+O(sqrt(h)).
7. Paired-character normalization + positive leading weights + translation permutation + Cauchy–Schwarz -> error C sqrt(h) Z_m^cl.
8. **Additional named hypothesis Q11** -> O(N^(-1/2)) weighted comparison. No EQ is used in steps 1–8.
9. **Separate physical dictionary + norm-uniform EQ** would identify/cancel the leading selected coefficient. This is not proved by the quantum argument.

## 2. Fresh parity calculation with the raw finite-shift operator

Temporarily write H=1/N, as in the one-step construction. A term in P_n contains:

- an amplitude Taylor derivative of order a;
- v copies of the midpoint term pi*i*k*l*H;
- n_r copies, for r>=2, of the phase Taylor term 2*pi*i*H^(r-1)*l^r*S^(r)/r!.

Its H grade is n=a+v+sum_(r>=2)(r-1)n_r. Its total symbol moment order is a+2v+sum r n_r. Replacing symbol moments by derivatives of the real symbol g contributes i raised to the negative of this latter number. The explicit exponent factors contribute i^(v+sum n_r). Their quotient is precisely i^(-n). All remaining factors are real when the test amplitude is real. Thus P_n=i^(-n) times a real differential operator; D_n=iP_n=i^(1-n) times a real operator.

D_1 is real. The real scalar leading transport with initial value 1 gives a_0>0. D_2a_0 is imaginary, so uniqueness of the real transport equation gives a_1 imaginary. This proves the needed claim directly from the literal finite-shift expression, rather than relying on Hermiticity alone or changing the quantizer. The stronger induction a_j=i^(-j) times a real function is also available but unnecessary.

Set L_j=log a_(j,0), and evaluate derivatives at the actual real stationary edge. With each edge's two entries of y understood (including their aliases at m=1), the rotated local exponent has

W = sum_j [D L_j[y] + D^3 S_j[y,y,y]/6],

Q = sum_j [-i D^2 L_j[y,y]/2 - i D^4 S_j[y,y,y,y]/24 + 2*pi*a_(j,1)/a_(j,0)].

For J=0 the last term is absent. This uses i*c^3=c, c^2=-i and i*c^4=-i. Therefore W is real and odd, Q is imaginary, and with the full real Gaussian of covariance G,

ell_1=E_G Q - (i/2)E_G W^2

is purely imaginary. The 2*pi conversion is retained exactly. Gaussian box conditioning is not silently substituted in this formal coefficient; its effect on the actual local theorem is exponentially small and is already controlled by that theorem.

## 3. Literal winding variation, gluing and all finite dimensions

Keep the integer branch vector fixed and set nu(s)=nu+s e_i. For the stationary equation grad Phi(x(s))+nu(s)=0, differentiation gives

K(s)x'(s)=e_i,   K=-Phi'',   x'=G e_i.

This sign is positive. The actual Hessian bounds apply at every real x and do not require nu(s) to be integral. Hence the interpolation stays in the domain where the analytic amplitudes, phase and massive inverse are defined. Symmetry gives identical row and column bounds for G; the weighted estimate gives exponential localization.

Each edge contributes a bounded fixed-size tensor to K. Differentiating its coefficients costs at most C(|x'_j|+|x'_(j+1)|). Summing over edges gives

sum_(a,b)|K'_(a,b)|<=C,

with repeated endpoint entries combined. From G'=-G K'G and the absolute row/column bound B,

sum_(a,b)|G'_(a,b)| <= B^2 sum_(a,b)|K'_(a,b)| <= C.

The same argument gives a summable derivative for every coefficient in the displayed W and Q; the highest new derivatives required are fifth phase derivatives, third derivatives of log a_0, and first derivatives of a_1/a_0. Accepted fixed-J local analyticity supplies them uniformly over real charts.

At the interpolation endpoints, exact integer phase gluing changes the action only by affine/integer terms and identifies the complete amplitudes without an extra factor. Thus all phase derivatives of order at least two, local logarithmic derivatives, K, and the formal coefficient ell_1 match under re-representation. The central unit winding is the actual label translation d_m; arbitrary site i is its cyclic shift. No derivative of the structural conjugacy is used.

For clarity, in the unperturbed lifted coordinates the endpoint variation is

(delta q,delta p)=(G_(0,0),(G_(1,0)-3G_(0,0))/4)=(S^m-I)^(-1)(0,1).

At m=1, G_(1,0) means G_(0,0), yielding (1,-1/2). At m=2 it yields (3/4,-1/2). The checked formula holds for m=1,...,12 with no discarded repeated edges. The group identification itself is the established exact branch quotient and is not inferred solely from these finite checks.

## 4. Wick-contraction derivative and why it has no volume factor

Q has local degrees 0,2,4. Differentiating its Gaussian expectation differentiates either a local coefficient or one covariance in a finite pairing. Summability of coefficient derivatives or the entrywise l1 norm of G' bounds the complete site sum.

For E(W_j W_k), each labeled vertex has odd degree (1 or 3), so any perfect pairing has at least one covariance joining the two vertices. This remains true when j=k or their physical endpoint coordinates coincide; it is a pairing statement on labeled legs, not on distinct coordinate values.

- Differentiate a coefficient at j: the coefficient derivatives sum over j, and a retained cross covariance sums over k by a row/column bound.
- Differentiate a cross covariance: sum that G' entry over j,k using its entrywise l1 norm.
- Differentiate a self covariance: at least one cross covariance remains. It sums the other vertex, and the differentiated local G' entry sums the remaining site.

All other covariance factors have a fixed uniform bound. A degree-six term has 15 pairings, and the number of local coordinate choices is fixed. Aliased endpoints at m=1,2 give only bounded multiplicities. Thus |ell_1'(s)|<=C, and integration over 0<=s<=1 proves Q8. This is a finite exact contraction calculation; neither convergence of the full formal expansion nor long-time stationary phase is needed.

## 5. Exact finite-h factors and weighted normalization

The accepted local theorem on the radius-one global contour gives

Z_z=exp(h ell_1(z))(1+epsilon_z), |epsilon_z|<=C sqrt(h),

uniformly for mh<=b. Since ell_1 is imaginary,

Z_(z+d) conjugate(Z_z)=exp(h[ell_1(z+d)-ell_1(z)])(1+O(sqrt(h)))=1+O(sqrt(h)).

The independent real Gaussian probability satisfies P_z=1+O(m exp(-c/h)), so adding both probabilities preserves the bound. It is not exactly 1 at finite h. Also |Z_z|>=1-C sqrt(h), uniformly; no division or unverified zero-free logarithm is needed for the paired estimate. For r literal successive pulses, endpoint comparison gives O(sqrt(h)+rh), without r separate O(sqrt(h)) errors; this says nothing about how many pulses a general displacement needs.

Let T_box,d denote the single paired-character summand with its outer unit phase included, and T_0,d the corresponding leading-weight expression. P7/P8 use the factor D_m^(-1). Therefore

D_m^(-1) w_0(z+d)w_0(z)=sqrt(rho_m(z+d)rho_m(z)),

where rho_m=w_0^2/D_m. No D_m average remains outside this sum, and no 4^m or 2*pi multiplicity is missing. The physical W3 interpretation of rho is separately reviewed; this normalization algebra already holds with the definition rho=w_0^2/D_m.

Consequently

|T_box,d-T_0,d| <= C sqrt(h) sum_z sqrt(rho(z+d)rho(z))
                  <= C sqrt(h) [sum_z rho(z+d)]^(1/2)[sum_z rho(z)]^(1/2)
                  = C sqrt(h) Z_m^cl.

Translation is a permutation of the finite abelian label group. This uses neither weak nor effective equidistribution, no pointwise bound on individual rho, and no derivative of rho. Positivity and bounded total leading mass are sufficient. It yields comparison with the leading coefficient; it does not show that the leading coefficient is small.

## 6. Global Fresnel comparison in the inherited finite band

The candidate's additional tail comparison is correctly normalized, provided one imports the **summed absolute** contour-tail theorem, not just the signed trace-tail estimate. Write delta alpha=alpha_global-alpha_box. The quotient removes exactly 4^m identical copies. Hence the existing summed absolute trace-tail bound is

||delta alpha||_l1/sqrt(D_m)<=epsilon_N,

epsilon_N=C_J sqrt(N) exp(-4N/5) for m<=2N. It follows that the normalized l2 norm is at most epsilon_N. Meanwhile the exact box main norm satisfies

D_m^(-1) sum_z |alpha_box(z)|^2 <= C Z_m^cl.

Cauchy–Schwarz for a fixed translated, character-weighted autocorrelation then bounds the global-minus-box coefficient by

2 C^(1/2) (Z_m^cl)^(1/2) epsilon_N + epsilon_N^2.

Thus Q11 also makes this one-coefficient error exponentially small in the conservative band. The global representation of the actual U trace uses its separate J>=1 one-step comparison; Q's J=0 local algebra does not grant a J=0 actual-trace reduction.

## 7. Obligation matrix

| Obligation | Status | Reason |
|---|---|---|
| Literal raw Weyl parity, a_1 imaginary | passed | explicit monomial count and real transport |
| h=(2*pi*N)^(-1), 2*pi a_1 contribution | passed | direct scaled expansion |
| Q1 includes P and conditioned Z | passed | full Gaussian normalization retained |
| Radius-one use of the accepted local theorem | passed, inherited project input | global theorem Section 6 explicitly verifies the required tilt family |
| Unit winding stays in admissible real domain | passed | global strict concavity and real interpolation |
| Branch gluing and cyclic m=1,2 aliases | passed | exact affine gluing; repeated endpoints combined |
| Uniform ell_1 unit-increment bound | passed | explicit finite Wick contraction summation |
| Exact paired box factor 1+O(sqrt(h)) | passed | imaginary exponent plus bounded difference |
| Q10 error with no exponentially many-class loss | passed | exact normalization and Cauchy–Schwarz |
| Uniform bounded positive leading mass Q11 | conditional | separate classical input; not proved here |
| Physical W3 and W9 interpretation | separately reviewed | normalization reconstructed; full dynamical dictionary outside this audit |
| Physical regularity, J_d ratio and oscillatory integral | out of scope | assigned to independent physical reviewer |
| Norm-uniform classical EQ | conditional | separately pending; not implied by Q1–Q11 |
| Summed absolute global-tail to one autocorrelation | passed, inherited finite-band input | normalized l1 -> l2 and Cauchy–Schwarz |
| Full displacement/time signed hierarchy | not addressed | an unnormalized outer sum remains |

## 8. Source and computation checks

Relevant authorities read: canonical AGENTS, SOURCE_OF_TRUTH, repository conventions, RESEARCH, claim ledger/registry and results/open-question scope. Canonical HEAD during review was `6f3874e5fb1d5b31b5825e2ff273e8c643e0046a`. Candidate hashes and all relevant manifest dependency hashes were verified unchanged.

The accepted local analytic theorem's external Poincare leaf already has an exact primary-source check in `literature/convex_box_poincare_check.md`, including its convex-box limiting argument. This audit inherits that accepted analytic input; it does not claim a new external referee audit of it.

Exact inherited acceptance chain (canonical root `/workspace/shared/BGS`):

- Accepted original local theorem `rotated_local_first_loop_v2.md`: SHA-256 `fe41ac7dc34660f2adedb82f741903be482e2b8eaef35d84feba6341bfcc32f1`.
- Original local review: SHA-256 `4abbf247e2e578b83d98b42e4d01e69702afe8b2e77d122c28f057a00cfd89e5`; its v2 hash confirmation: `a0f8e402683ebd4ed78c9f4535eb799460e481ba5335549308d1407048414e95`.
- Original acceptance/review manifest: `record/heisenberg_wkb_review_provenance.json`; editorial map: `record/heisenberg_wkb_editorial_mapping.json`; later finite-band scope edits: `record/global_rotated_box_integration_delta.json`.
- Current local source actually read: `mathematics/rotated_local_first_loop.md`, SHA-256 `2923a5f4b5946005e28ef77925f26e380ab945fc1682db24dcec3f9ed2f8bc98`.
- Original global contour source `global_bent_contour.md`: SHA-256 `d4abd7785da50537bc4cfd218bb753dd10426d07175a7d954ebddb67b8f38aec`; original conditional tail source `conditional_bent_tail.md`: `762aeac6e6840cf8798ab810ff77f2be3b2a327f42e47c5d53625b1d8a2d2ce1`.
- Global review and raw-to-canonical mapping: `record/global_rotated_box_review_scope.md` and `record/global_rotated_box_source_mapping.json`.
- Current global source actually read, including its independently justified radius-one extension in Section 6: `mathematics/global_rotated_box_trace.md`, SHA-256 `0468be632207b88ce5b24e190187662ad1be91dd709621a20f4adf5adfa48a94`.

The companion `sources_and_artifacts.json` pins these current source and review-manifest files together with this review and the independent checker/output. Original acceptance hashes are provenance, not a claim that the current editorial bytes are identical to the originals.


Independent exact-arithmetic control:

`python3 /workspace/shared/bgs_physical_quantum_homoclinic_review/check_quantum_first_loop.py`

Result: 386 Weyl parity grade checks; 2,912 independent pairing-derivative versus Gaussian Price-identity checks, m=1,...,12; exact unit-winding endpoint labels in the same range. Repeated endpoint aliases were retained. Output is `quantum_first_loop_results.json`. These are finite rational algebra controls, not verification of the actual analytic amplitudes, asymptotic estimates, classical mass or EQ.

## Exact remaining gap and strongest safe statement

No additional quantum gap was found in Q1–Q10. The strongest conclusion established without a new classical input is the explicit error bound C sqrt(h) Z_m^cl. A uniform bound on Z_m^cl immediately upgrades it to O(N^(-1/2)); it does not require norm-uniform EQ. Actual selected-coefficient decay additionally requires the independently checked leading-weight/physical-phase transfer. No finite selected-coefficient result can be summed over exponentially many displacements without a new aggregate argument.
