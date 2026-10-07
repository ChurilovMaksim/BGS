
## 8. Separate claim card: complete unmasked separated compositions

The author export right_overlap_and_unmasked_insertions.md defines, on the same ordinary HS space,

    T_theta=Ad(Z_theta U),       D_theta=V_theta D,
    G_j(n;theta)=Tr_H[D_theta T_theta^n_1 ... D_theta T_theta^n_j],
    A_(j,N,m)(theta)
       =binom(m-1,j-1)^-1
           sum_(n_1+...+n_j=m-j, n_i>=0) G_j(n;theta).

Every G is a probability average of squared ordinary traces of unitary words, hence nonnegative. The distinguished scalar identity contribution to every G is exactly 1.

**Separate verdict: proved as written**, for the full unmasked fixed-j composition averages, their signed occupation subtraction, and the stated untwisted j_N=o(N) extension. This verdict uses the actual right-frame estimate proved above and the accepted Abel/compactness inputs specified below. It says nothing about a prescribed gap vector at j=1,2 or a signed path subset.

The natural positive-band statements, for fixed j>=1 and bounded compact weights w, are

    N^-2 sum_m |w(m/N)| A_(j,N,m)(0) ->0,
    N^-2 sum_m |w(m/N)| E_theta A_(j,N,m)(theta) ->0.

The signed difference therefore tends to zero. The equivalent raw-composition normalization is N^(-(j+1)); the raw rooted-slot normalization is N^(-(j+2)). The original N^-2 normalization is attached to the A average, not to these raw coefficients.

### 8.1 Fixed-B placement and exact rooted multiplicity

The author's F_n(B) is

    (1/N) sum_b |tr(U^n K_b B)|^2
       =sum_c |tr(A_c B U^n)|^2,

by cyclicity and character orthogonality, so it is exactly the F used above. For unitary B, C_B=L_(B*) C is the correct frame. Because right multiplication commutes with this left rotation,

    C_B* R_U^r C_B=C*R_U^r C.

The corresponding arbitrary-B covariance for LEFT multiplication is false and is not used. Fixing all other gaps and Kraus labels makes B fixed during the distinguished n sum. Averaging the remaining labels does not change the bound.

For rooted products of length m with j marked D slots, mark one of those j slots. Every slot choice then has j markings. Conversely choose one of m root positions and a weak composition of m-j into j cyclic gaps. Cyclic trace invariance gives

    S_(j,N,m)=(m/j) sum_(sum n_i=m-j)G_j(n)
              =binom(m,j) A_(j,N,m).

This counts periodic patterns with the same multiplicity, because it counts markings before dividing by j. No rotation-orbit freeness is assumed. It includes j=1, j=m and every zero gap.

### 8.2 The decreasing-weight fiber count and j=o(N)

For fixed other gaps of total s, let n be the distinguished gap. Its inverse-binomial weight h(n)=1/binom(n+s+j-1,j-1) is nonincreasing. Applying the interval frame bound to partial sums, then discrete summation by parts, gives

    sum_(allowed n) h(n) F_n(B)
      <=N gamma_(L,N) sum_(allowed n) h(n)
          +N C_flat L h(first allowed n).

All terms remain nonnegative. The first allowed total length is max(m0,s+j). For j>=2 there are binom(s+j-2,j-2) other-gap vectors at total s.

The initial-weight sum for s<=m0-j equals

    sum_(s=0)^(m0-j) binom(s+j-2,j-2)/binom(m0-1,j-1)=1

by the hockey-stick identity. For each s>m0-j the ratio is exactly (j-1)/(s+j-1). This reconstructs the author bound

    N^-2 sum_(m=m0)^m1 A_(j,N,m)(0)
      <=((m1-m0+1)/N) gamma_(L,N)
         +(C_flat L/N)
             [1+(j-1) sum_(m=m0+1)^m1 1/(m-1)].

At j=1 there is one fiber and bracket 1. The condition j<=m0 ensures the lower endpoint is present; fixed j and j_N=o(N) satisfy it eventually on a positive band.

The harmonic sum is bounded on m in [aN,bN]. Thus the remainder is O_(a,b)(L(1+j)/N), and the double limit at fixed L proves uniform vanishing along every j_N=o(N), including O(log N). This is not a growing-lag stationary-phase claim. The all-gap average and its natural normalization are essential.

## 9. Separate annealed bounded-factor audit

The newly used analytic inputs are exactly:

- accepted FM-028, actual_charge_radial_shell.md, C2/C4: uniform finite-rank approximation of the entire D_N in operator norm under the ordinary-Weyl embeddings;
- accepted TRACE-023, uniform_phase_pair_abel_bound.md, theorem (A):

      sum_(k>=1) r^k E_theta |tr(Z_theta U)^k|^2
        <=N(1+r)/(2(1-r)),       0<r<1,

  for every unitary U.

Their accepted scope is confirmed in the pinned phase_trace_checkpoint.md. This audit uses neither FM-028's Egorov/mixing/quasimode conclusions nor TRACE-023's other source/color claims. The compactness source hash is eccca8f36860e537f736828c435fce94f10006fbbaa48722fbd9481671ed4c0b; the Abel source hash is ecd82a74edfabb89f6cbf46054d76c52dd41e5eb2d5a9790771b16a7c033da3f.

**Separate verdict: proved as written** for the author's bounded-factor lemma (15), its positive auxiliary interval consequence (16), and fixed-j annealed composition conclusion (17).

Choose a nonnegative smooth compact phi on the real line with phi>=1 on [0,b] and put S_N(T_theta)=sum_(n in Z)phi(n/N)T_theta^n. Two discrete differences give a Fourier bound C N/(1+N² dist(t,2pi Z)²). Comparison with the Poisson kernel at r=e^-1/N, normal spectral calculus, and the exact adjoint spectrum give

    E_theta ||S_N(T_theta)||S1
      <=C E_theta Tr_H P_r(T_theta)
      =C[N²+2 sum_(k>=1)r^k E_theta |tr(Z_theta U)^k|²]
      =O(N²).

This is the trace norm AFTER the complete smooth time sum. It is not an unaveraged pair-density estimate.

Given any contraction family B_theta, fixed during this sum, write D=F+R with rank F<=R_epsilon independent of N, ||F||<=2 and ||R||<=epsilon. Multiplication by V_theta preserves rank and approximation error. Cyclicity and trace duality yield

    |E_theta Tr_H[D_theta S_N(T_theta) B_theta]|/N²
      <=C R_epsilon/N+C epsilon.

There is no independence requirement on B_theta and theta. The inequality is uniform in every such bounded family.

For the physical separated product, B_theta is a probability mixture of adjoints of unitary words. T_theta^n has the same property for every integer n, INCLUDING negative n. Therefore Tr_H[D_theta T_theta^n B_theta]>=0 for every integer n. The nonnegative auxiliary smooth sum really majorizes the required interval 0<=n<=bN. This validates the short-gap and negative-power step rather than merely bounding the modulus of a different signed sum.

The resulting o(N²) is uniform in the other gap vectors. There are O_j(N^(j-1)) such vectors on a fixed band. Dividing by the lower bound binom(m-1,j-1)>=c_(a,j)N^(j-1) proves the stated annealed A aggregate for every fixed j. No occupation-uniform compact EMBEDDING is claimed: only the rank and tail error are preserved by V_theta, which is sufficient.

The preceding native consecutive-block theorem already states a fixed-in-time bounded-factor extension. The present use is nevertheless separately checked, including the all-integer smooth majorant and physical CP positivity. It is not an unproved inference that fixed total time leaves all the other lengths fixed.

## 10. Separate Schatten-tail audit: genuinely derived, with no new tail assumption

**Separate verdict: proved as written**, for equations (18)–(22), conditional only in the ordinary dependency sense on the accepted compactness and actual flatness inputs. There is no additional unproved Schatten-tail hypothesis.

The singular-value argument is a NEW internally proved consequence of those inputs. The older FM-028 scope warning that its radial theorem supplies no Schatten theorem correctly describes that older theorem alone; this candidate additionally uses actual entrywise flatness and performs a separate finite-dimensional interpolation.

In the orthonormal matrix-unit basis, the charge block has entries U_xy conjugate(U_(x+c,y+c)). Thus

    ||D||S2²=sum_(c,x,y)|U_xy|² |U_(x+c,y+c)|².

Actual entrywise flatness supplies |U_xy|²<=C/N. There are N charges and sum_(x,y)|U_xy|²=N. Therefore ||D||S2²<=C N. This is ordinary superoperator Schatten norm on dimension N². Scalar normalization of the underlying HS inner product does not change the singular values; a normalized superoperator trace must not be inserted.

The reducing identity direction gives D=J_identity plus D0. Consequently ||D0||S2²<=C N and ||D0||op<=1. Uniform rank-R approximation implies s_(R+1)(D0)<=epsilon eventually, with R depending on epsilon but not N. Splitting the singular values gives

    ||D0||S3³
       <=R +epsilon sum_(k>R)s_k(D0)²
       <=R +C epsilon N.

First N->infinity at fixed epsilon, then epsilon->0 proves

    eta_N=||D0||S3³/N ->0.

No rate follows. No ordinary-model spectral pairing input is hidden here.

Since V_theta fixes the identity direction and is unitary on its complement, D_theta|H0 has exactly the singular values of D0. T_theta is unitary there. For any j>=3, select three of the D factors as Schatten-3 factors; group all remaining factors as operator-norm contractions. Finite-dimensional noncommutative Hölder yields

    |Tr_H0[D_theta^0 T_theta^n_1 ... D_theta^0 T_theta^n_j]|
        <=||D0||S3³=N eta_N.

There is NO factor j, rank N², or number of compositions in this estimate. Reordering the factors is unnecessary; Hölder controls their original order. Adding back the reducing scalar identity contribution gives

    |G_j(n;theta)-1|<=N eta_N

uniformly in all theta, separations, lengths and j>=3. The author retains this 1 in both its pointwise bound and subsequent normalization. CP positivity independently gives G_j>=0 and A_j>=0.

This does not handle j=1 or j=2. Those low orders use the separate right-frame and annealed time-sum arguments. Thus this tail estimate does not conflict with the inherited period-six first-pinch obstruction under coarse compactness-only inputs.

For any nonnegative coefficient array p_(j,m,N) with total at most one, its low-j contribution is bounded by the two separately vanishing positive time aggregates. Its j>=3 contribution on O(N) band times is bounded by

    N^-2 O(N)(1+N eta_N)=O(1/N)+O(eta_N)->0.

No unspecified o(1) is multiplied by the number of insertion orders. This validates (22), including orders up to m.

## 11. Full unmasked convex-switch correction and precise non-closure

Noncommutative expansion and the rooted multiplicity identity give exactly

    Tr_H[zT_theta+(1-z)D_theta]^m
      =z^m |tr(Z_theta U)^m|²
        +sum_(j=1)^m binom(m,j)z^(m-j)(1-z)^j A_(j,N,m)(theta).

The coefficients are nonnegative and sum to 1-z^m<=1. Equation (22) therefore proves (23), uniformly in any z_N in [0,1], for both theta=0 and the phase average. This uniform all-z statement is valid at the ORIGINAL unmasked compact-band N^-2 normalization. It is stronger than a q_N->0-only first-pinch resummation, but its extra strength uses the independently reviewed three-insertion Schatten tail.

The exact occupation-subtracted insertion correction also vanishes by subtracting these two complete sums. This is a genuine complete-unmasked statement. It leaves the zero-insertion term multiplied by z_N^m.

The following implications remain unproved and MUST NOT be integrated as consequences:

1. A prescribed j=1 or j=2 gap vector estimate.
2. An arbitrary signed subset or Hamming/high-switch coefficient mask.
3. Quantitative decay for eta_N or the positive time aggregates.
4. Multiplication by a polynomial deconvolution cost at z_N=1-A log N/N.
5. Differentiation of a bare o(1), or a marked-switch-source bound.
6. The undamped zero-insertion occupation comparison, T16, higher factorial TRACE-005, or BGS.

Extra unitary charge-marker factors preserve the centered Hölder bound itself, but growing Fourier extraction norm cannot be absorbed without a quantitative eta_N rate. Kraus positivity and the arbitrary-NxN-unitary-B frame dictionary do not automatically survive an arbitrary q marker.

The shared identity term is retained as 1 in the unsigned words and cancels in the signed occupation difference. An obstruction obtained by deconvolving that unsigned identity term alone is therefore not a refutation of signed T16. Nothing in this accepted bounded extension authorizes unsigned deconvolution or identifies the signed zero-insertion endpoint.

## 12. Independent finite checks, provenance and remaining access limits

All four authorized Markdown exports were read in full through Library. Read content omitted the final LF; restoring exactly that LF reproduced every supplied size and SHA256. Local copies are in authorized_exports/. This is separately authorized readable export access; the denied ZIP transfer was not retried or bypassed.

- right_overlap_and_unmasked_insertions.md: Library libfile_37494326fb148191b2418b864c75a600, 18,848 bytes, SHA256 4c149ab775835c42f4bdb537c558252bf8e129c4b359ef30f6fe1a8578ed8f3e.
- transpose_reduction.md: Library libfile_1f1e4ffc980c8191af8e8fe2ad817450, 5,187 bytes, SHA256 83425306c15e3b7b69626ccd53c46c8c077bfa13078d6314961fe6f95b61ee30.
- RIGHT_FRAME_HANDOFF.md: Library libfile_eb4195e34998819183e129f460dc5472, 4,697 bytes, SHA256 416d7e114ad7319b35effddad0a42d27ab5e0abbe16b8a58d3f350035c09358f.
- self_audit.md: Library libfile_259f830abf8881918d6fe6b05a3a7362, 5,469 bytes, SHA256 e15de2140749e3d33639b425dcae18332746c29f29feb9c8c15478a5a12cd0b0.

The independently written check_separated_independent.py passed 227 exact controls in ordinary Python and python -O:

- exhaustive rooted cyclic coefficient multiplicities for all m=1,...,12, every j=1,...,m, and every binary insertion-slot pattern, compared independently with the weak-composition representation;
- every endpoint-fiber count at allowed j in bands [1,5], [4,11], [10,21];
- direct right-phase Hessian, exceptional boundary vectors, and Schur value for r=1,...,16;
- exact ordinary Schatten-2 entry identity, flatness envelope, and reducing identity direction in Gaussian-rational unitary fixtures N=3,5.

The first supplementary run exposed a test-implementation issue: direct structural equality of an unexpanded SymPy product was used to check unitarity. Expanding the exact Gaussian-rational polynomial before comparison fixed that issue; the fixture was mathematically unitary. All final runs use explicit exceptions, remain active under -O, and complete without failure. This is not a counterexample to a mathematical claim.

The author packet's 222 core controls and its own 18 transpose controls were NOT reproduced, because those code sources were not part of the authorized Markdown exports. Instead, 129 accepted-left controls, 72 independent right-frame controls (including exactly 18 direct transpose controls), and 227 independent separated controls each passed in normal and optimized Python. The total number is corroboration only, not a theorem certificate.

Software: Python 3.12.14, SymPy 1.14.0, Linux 6.18.44 x86_64. No randomness, floating tolerance, actual-tau extrapolation, proof-assistant compilation, full baseline build or asymptotic computation was used. The finite bounds are the actual implemented ranges, with no truncation or skipped cases. Computation manifests and hashed outputs are supplied in the review directory; their legacy-v1 provenance limitations are explicit.

## 13. Final obligation matrix and strongest safe integrated statement

Passed separately:

- Right-frame transpose reduction and actual fixed-r overlap.
- Arbitrary unitary B fixed during its n sum and all-start uniform prefix bound.
- Direct right-Hessian derivation, including r=1,2 and alias-independent perturbation.
- Rooted cyclic multiplicity and zero-gap composition normalization.
- Decreasing-weight boundary fibers and untwisted j=o(N) average.
- Annealed bounded-factor spectral-kernel lemma and negative auxiliary powers.
- Actual S2 bound, compactness-to-S3 consequence and identity-sector subtraction.
- Uniform all-orders j>=3 word bound and binomial-probability summation.
- Complete unmasked all-z insertion correction, untwisted and annealed.
- Exact full occupation subtraction of those complete sums.

Not supplied:

- Author's complete finite suite or ZIP manifest-byte verification.
- Any quantitative growing-r or compactness rate.
- Masks, marked sources, polynomial deconvolution, the zero-insertion endpoint, T16, TRACE-005 or BGS.

**Strongest safe result:** the actual right-frame and fixed-B theorem; complete unmasked fixed-j separated composition averages, with untwisted j=o(N) scope as stated; the uniform centered three-insertion Schatten bound; and the full unmasked binomial insertion correction uniformly over z in [0,1], at the stated original compact-band normalization. These are internally proved extensions using accepted inputs, not conditional on an additional Schatten-tail estimate.

The cheapest useful next mathematical check is a quantitative eta_N/low-order source bound compatible with a specified mask extraction or deconvolution, or a new direct signed zero-insertion argument. Merely increasing the insertion-control sample size or applying the unmasked positivity bound to a path subset would not address that remaining implication.

