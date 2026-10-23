# Independent audit of the quadratic slow source and signed coefficient

Date: 6 October 2026. Scope: the two frozen reports named below. New work is confined to this directory. No candidate, canonical, or existing evidence file was edited.

## Verdict and exact target

**Primary verdict: proved as written for all five requested targets.**

For every odd N≥3 and integer m≥2, let D be the balanced step on the first k=(N−1)/2 vertices after the identically zero Jacobi edge. Let X=Σ(r<s)D^(r)D^(s), P₀ the full U(N) Haar projection, Y=(I−P₀)X, and W=ΠCₘ*Y. With the ordinary unnormalized Hilbert–Schmidt norm, the exact claims are:

1. P₀X=(4N)⁻¹Σ(r<s)(Swap_rs−I/N), and all local pair norms add with exactly binom(m,2)N^(m−2).
2. ||W||²/||Y||²=(N²−3N+3)/(3N(N²−2)); the actual fixed-time source has norm Θ(N⁻¹/²), uniformly in m.
3. For τ=10⁻⁸⁰, ε=N⁻⁵, odd N≥19, and every m≥2, ||ΠKₘ(τ)* (Lₘ+ε)⁻¹/²(I−P₀)||≥N²/4. This includes 7|N and requires no identification P₀=ker Lₘ.
4. The normalized cyclic coefficient of this Y is −1/(N²−2)+δ_N, with 0≤δ_N≤(9π⁴/40000)((N²−1)/(N²−2))τ²N⁻³; it is strictly negative.
5. For this Y only, the Rayleigh quotient of Lₘ+ΠCₘLₘCₘ*Π is 3/(20000N)+O(N⁻³), uniformly in m.

The audit does not assert a bound on the whole signed trace, an all-vector two-frame gap, Haar relaxation of the deterministic map, or closure of the plateau problem. The unregularized corollary in report §4 inherits the separately stated connected-graph kernel theorem; that theorem is not needed for any target above.

Frozen targets:

- `bgs_weighted_plateau_independent/nonlinear_source/report.md`, SHA-256 `4fa3415ce156c563f4d63a180914acdf7c22b8ffb7e3935ad34506258c2b1083`.
- `bgs_weighted_plateau_independent/nonlinear_source/signed_pairing.md`, SHA-256 `093cabf412c6e5eff4a3584b954d130be1cd16900ae41324834caad4185ebc37`.

Both hashes were verified before and after the controls. The actual-model definition was checked directly against `BGS/mathematics/fixed_map_path_model.md`, SHA-256 `d5365063f0967dabcac741a93c6f411d6402c913074944e1f9e383b2b5149b08`.

## Dependency graph and obligations

The fixed Weyl quantization and metaplectic kernel imply the actual Jacobi middle-edge weight and the chirped discrete Fourier formula for M*DM. The two-copy Haar calculation plus exact tensor contractions imply the norms and all-m multiplicities. Interval additive energy then gives the source ratio. The commutator identity gives the first-frame energy. The spectral theorem gives the all-time source error and, with a test vector, the regularized inverse-energy lower bound. Collective conjugation and pair orthogonality give the signed coefficient. A separate matrix-unit contraction and a finite Fourier correlation give the two-frame Rayleigh quotient.

All these leaves are definitions or internal finite-dimensional proofs. No external asymptotic theorem, character formula, probabilistic mixing result, or literature-dependent transfer is required.

| Obligation | Status | Decisive check |
|---|---|---|
| Actual A and M, including composite odd N | Passed | Direct comparison with the defining Fourier/Weyl quantization; independent implementation uses that definition |
| Full Haar projection rather than a selected invariant subset | Passed | Twirling a pair acts only on that pair, even when m>N |
| Overlapping and disjoint pair multiplicities | Passed | Vanishing partial traces kill every distinct-pair contraction |
| Positive exact q_N and actual Θ(N⁻¹/²) source | Passed | Exact interval energy and a global-in-time spectral bound |
| N²/4 bound for 7-divisible N≥19 | Passed | Regularized test vector; no use of the full-kernel identity |
| Literal-τ signed estimate and strict sign | Passed | Exact square formula; squaring the one-copy Duhamel bound |
| Two-frame constant and quantifiers | Passed | Exact nearest-neighbor contraction and bounded Fourier correlation |
| Whole trace, all-mode two-frame gap, Haar relaxation | Out of scope | These do not follow from the audited vector statements |

## Independent analytic reconstruction

### A. Haar projection and the uniform tensor factors

Put t₂=Tr D²=(N²−1)/(4N). A two-copy twirl of D⊗D is αI+βS. This elementary two-copy commutant fact follows by diagonal-unitary invariance, then permutation matrices, and finally a rotation in each coordinate two-plane. The first condition permits only unchanged or swapped index pairs; the remaining conditions make their coefficients independent of the indices and impose the single relation on repeated indices. No hypothesis m≤N occurs here.

The trace and swapped trace are 0 and t₂. Solving N²α+Nβ=0 and Nα+N²β=t₂ gives Q=(t₂/(N²−1))(S−I/N). Haar integration commutes with embedding a pair with identity in the other slots, so P₀X is the sum of the embedded Q, even if the global invariant tensors have linear relations.

Both partial traces of D⊗D−Q vanish. Any contraction of different pair embeddings has an index present in one pair and absent in the other; tracing that index gives zero, whether the pairs share one index or are disjoint. Consequently each pair contributes independently, with spectator factor N^(m−2). Locally,

||D⊗D−Q||²=t₂²−t₂²/(N²−1)=(N²−1)(N²−2)/(16N²).

This proves the exact norm and rules out both hidden occupation exclusions and growing-m loss.

### B. Balanced source and Fourier moment

Write B=M*DM. Flatness gives B_ii=0. The only balanced terms of B⊗B are B_ij B_ji |ij><ji| for i≠j; Hermiticity makes their coefficient |B_ij|². Therefore T=Σ(i≠j)|B_ij|²|ij><ji|, and W is the pair sum of T−Q.

Again each partial trace vanishes. Since Tr T=0, Tr(TS)=t₂, and ||T||²=t₄=Σ(i≠j)|B_ij|⁴, the local squared norm is t₄−t₂²/(N²−1).

From the given M kernel, B_ij is a unit-modulus chirp times N⁻¹Σ_l φ_l e_N(4⁻¹l(j−i)). The difference multiplier 4⁻¹ permutes Z/NZ for every odd N, including multiples of seven. The interval of length k has pair-sum counts 1,2,…,k,…,2,1 after a cyclic translation. Since 2k−2=N−3<N, no pair sums collide modulo N. Its additive energy is E=(2k³+k)/3. Removing the zero Fourier mode yields

t₄=E/N²−k⁴/N³=(N²−1)(N²+3)/(48N³).

Dividing the local source norm by the local Y norm gives exactly q_N. All factors binom(m,2)N^(m−2) cancel. In particular q_N∼1/(3N).

### C. Actual energy and a uniform numerical constant

The invariant correction commutes with the collective A. Locally,

[A⊗I+I⊗A,D⊗D]=[A,D]⊗D+D⊗[A,D].

The cross inner product is zero because Tr(D[A,D])=0. Partial traces again vanish, so different pairs remain orthogonal. The step crosses the identically zero boundary edge and exactly one potentially nonzero middle edge. Thus ||[A,D]||²=2w_mid, and

e_N=||HₘY||²/||Y||²=16Nw_mid/(N²−2),
w_mid=cos⁴(7π/(2N))sin⁴(π/(2N))/2500.

This gives e_N∼π⁴/(2500N⁵). For N≥19, positivity is immediate and

e_N N⁵≤(π⁴/2500)N²/(N²−2)<(100/2500)(361/359)<1/20.

For N=7 the middle edge and every other off-diagonal edge vanish; the exact operator A is (9/10)I. Thus e_7=0 while q_7>0, consistently with the extra kernel.

The self-adjointness of Hₘ gives ||(exp(−itNHₘ)−I)Y||≤|t|N||HₘY|| for every real t. Contracting by Cₘ* and Π proves the claimed source error. The error O(|τ|N⁻³/²) is one power of N smaller than sqrt(q_N), so the actual fixed-time source is Θ(N⁻¹/²). This uses no expansion at unresolved numerical time τ.

### D. Regularized inverse-energy estimate, including 7|N

Every Haar invariant is balanced and commutes with A_tot, hence LₘP₀=P₀Lₘ=0. The vector v=(Lₘ+ε)^(1/2)Y is therefore in the Haar complement, and applying the operator under audit to v gives the actual source T_τY. Its input norm is sqrt(e_N+ε)||Y||, proving the test-vector lower bound in report (13).

The stated constant can be verified without any tiny-number arithmetic. For N≥19, q_N≥1/(6N), e_N≤N⁻⁵/20, and |τ|≤1. Thus

sqrt(q_N)−|τ|N sqrt(e_N) ≥ (2/5−1/(4N))N⁻¹/² ≥ (3/8)N⁻¹/²,
sqrt(e_N+N⁻⁵) ≤ sqrt(21/20)N⁻⁵/² ≤ (3/2)N⁻⁵/².

The ratio is at least N²/4. These inequalities hold in particular at τ=10⁻⁸⁰. They never use connectedness, invertibility of L on the Haar complement, or 7∤N. Regularization is exactly what makes the stated unrestricted claim legitimate.

### E. Signed cyclic coefficient

For every single-copy unitary U, distinct pair embeddings of D⊗D and UDU*⊗UDU* have zero contraction. Hence

<X,C_UX>=binom(m,2)N^(m−2)[Tr(DUDU*)]².

The Haar projection of X is fixed by C_U. Subtracting its squared norm and dividing by ||Y||² gives ((N²−1)a_N(t)²−1)/(N²−2). Because D and UDU* are Hermitian, a_N(t) is real. The slot cycle permutes the unordered pairs in X and in its invariant correction, so RₘY=Y. Unitarity of the cycle then identifies the cyclic and ordinary coefficient with exactly the stated sign.

Flatness gives Tr(DMDM*)=0. Moving E=exp(itNA) across the trace and using Hilbert–Schmidt Cauchy–Schwarz gives

|a_N(t)|≤|t|N||[A,D]||/||D||.

Using w_mid≤π⁴/(40000N⁴),

||[A,D]||²/||D||²=8Nw_mid/(N²−1)≤(9π⁴/40000)N⁻⁵

for N≥3, since 8N²/(N²−1)≤9. Squaring proves S2 with its nonnegative correction. Relative to the magnitude 1/(N²−2), that correction is at most

(9π⁴/40000)τ²(N²−1)/N³ < (9/400)τ²/N ≤9/7600<1

for N≥19 and |τ|≤1. Strict negativity at the literal τ follows uniformly in N and m.

### F. Two initial compressed frames

The chirp drops out of F(d)=|B_(i,i+d)|², which is independent of i and has F(0)=0. On two copies T=diag(F(i−j))S. The swap commutes with A⊗I+I⊗A. The two terms in the commutator with the diagonal factor change different tensor coordinates and have disjoint off-diagonal supports. For each directed nearest-neighbor edge, summing over the untouched coordinate gives E_F=Σ_d(F(d+1)−F(d))². This proves exactly

||[A⊗I+I⊗A,T]||²=2||A_off||²E_F.

The commutator has zero partial traces: tracing over one slot kills the commutator in that slot, and the other term is a commutator with Tr_slot T=0. Hence all pair multiplicities cancel once more.

The Laurent polynomial r² has degree 16 and constant coefficient 9/4. Exact discrete sampling for N≥19 gives ||A_off||²=9N/80000. Consequently the second-frame energy equals 9N³E_F/[2500(N²−1)(N²−2)].

For θ=2π4⁻¹/N the uncentered interval Fourier-power autocorrelation is N⁻³Σ_s(k−|s|)²e^(isθ). Removing F(0) subtracts exactly 2k²sin²(kθ/2)/(N⁴sin²(θ/2)). Summing the triangular-square polynomial by its second difference gives the stated S_k formula. Since sin(θ/2)≥1/2 for odd N≥3,

0≤C_F≤S_k/N³≤(4k+4)/N³≤3/N².

Also 2t₄/N=1/24+O(N⁻²), whence E_F=1/24+O(N⁻²). Substitution yields 3/(20000N)+O(N⁻³); the first-frame e_N is only O(N⁻⁵). This computation proves only the Rayleigh quotient of the specified Y. A single vector cannot establish a lower spectral gap of the full two-frame operator.

## Computation audit and reproducibility

The two supplied scripts were read and reproduced with outputs redirected here. Their implemented tensor ranges and auxiliary times match their reports. They neither resolve 10⁻⁸⁰ numerically nor purport to certify the universal bounds numerically.

The new `independent_checks.py` constructs A directly from the exact Gaussian-rational Fourier coefficients and the defining W_N(l,k), rather than importing the source midpoint-matrix helper. It independently checks the coefficient reality symmetry and the rational constant coefficient 9/4 of r². It builds the full tensor operators, occupation projection, and cyclic pairing at (N,m)=(3,2),(3,5),(5,3),(7,2),(19,2),(21,2). Thus the independent controls include m>N and both the scalar N=7 and nonscalar 7-divisible N=21 cases. Auxiliary times are 0 and 0.137.

Exact Fraction arithmetic verifies the additive energy, local norm division, q_N formula, and q_N≥1/(6N) in their respective ranges for odd N=3,…,201. FFT versus closed-form correlation controls run at N=3,5,7,19,21,35,49,101,1001. All assertions pass. Largest full-tensor invariant contraction residual is below 5.4×10⁻¹⁵; signed identity residual is below 3.4×10⁻¹⁶. At N=21, the analytic test-vector lower expression is approximately 234.637, versus the target N²/4=110.25. This decimal is a diagnostic; section D proves the inequality for every allowed N.

Commands, from any directory:

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python bgs_weighted_plateau_independent/nonlinear_source/check_nonlinear.py > bgs_slow_source_review/reproduced_nonlinear_checks.json
    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python bgs_weighted_plateau_independent/nonlinear_source/check_signed.py > bgs_slow_source_review/reproduced_signed_checks.json
    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python bgs_slow_source_review/independent_checks.py > bgs_slow_source_review/independent_checks.json

The finite controls use complex128 matrices and are not interval certificates. There is no randomness. BLAS and OpenMP thread limits are cooperative. The mathematical conclusions depend on the analytic derivations above, not on passing finite controls. All source hashes and output hashes are recorded in `manifest.json`.

## Remaining implication and safest use

There is no remaining gap in the five scoped vector claims. The absent next implication is a bound on the complete signed cyclic complement, including all modes and their cancellations uniformly at m comparable to N. Neither the large unsigned inverse-energy norm nor this one negative diagonal coefficient supplies that bound. The cheapest useful next step is to state the exact full-trace estimate required by the plateau argument and identify a cancellation mechanism that genuinely acts on that trace. Repeating larger numerical tests of this one vector would not establish it.

Original execution/source bytes are mapped in record/collective_promotion_mapping.json. Floating finite controls remain diagnostics; they do not prove analytic limits.
