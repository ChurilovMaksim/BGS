# Deterministic maximal microscopic transport along an observable flow

**Stable claim:** BGS-TRACE-072. **State:** PROVED.
**Boundary:** Finite-N maximal path bound under one common observation origin. Actual-map growing interval o(sqrt(log N)) uses FM-018 mixing/Egorov and a fixed smooth exactly centered symbol. The time-average endpoint mechanism is prior corpus work; the initial law and BGS remain open.
**Integration and review:** [11 October disposition](../../archive/record/chat_integration_20261011.md).
**Original input:** [dated source](../../archive/evidence/executions/20261011/chat-research/original/deterministic_path_transport.md).


11 October 2026. Project proof and independent internal reconstruction.
This strengthens the maintained ergodic spectral-transfer comparison to
a maximal path estimate and a growing parameter interval. The underlying
time-averaging mechanism and quantum-ergodic transfer are prior corpus
results, with established antecedents in logarithmic quantum ergodicity.
No claim of external priority or a proof of BGS is made.

## Exact finite-dimensional theorem

Let U_N be any unitary matrix, B_N=B_N* with Tr B_N=0 and ||B_N||op≤C,
and U_N(x)=U_N exp(ixB_N/N). For an integer T≥1 put

    A_N,T = (1/T) Σ_{k=0}^{T−1} U_N^(−k) B_N U_N^k,
    v_N,T = ||A_N,T||_F / √N.

Use one uniform circle origin φ shared by the whole eigenangle path.
Let Ξ_N(x;φ) be its periodic unfolded point process, of intensity one,
and use the Laplace metric d_L of the phase path theorem. For every R≥0,

    E_φ sup_|x|≤R d_L(Ξ_N(x;φ),Ξ_N(0;φ))
       ≤ R v_N,T/π + C² R²(T−1)/(2πN).                 (Q1)

For an individual nonnegative smooth compact test f the same bound is
multiplied by ||f′||_1. No randomness in U_N or its coordinate phases,
no simple-spectrum assumption, and no lower bound on spectral gaps is
used. The only random variable in (Q1) is the observation origin.

## Proof

Right differentiation gives U_N(x)* U_N′(x)=iB_N/N. At almost every x,
the eigenangle velocities are eigenvalues of the compression of B_N/N
to the eigenspaces. Consequently

    Σ_j |θ_j′(x)| ≤ ||E_{U_N(x)} B_N||_F / √N.

Full eigenspace pinching leaves every conjugated time average unchanged:
E_{U_N(x)} A_T(U_N(x))=E_{U_N(x)} B_N. Its Frobenius contractivity gives
an upper bound ||A_T(U_N(x))||_F/√N for the displayed velocity sum.

Telescoping unitary powers yields

    ||U_N(x)^k−U_N^k||op ≤ k|x|C/N,
    ||U_N(x)^(−k)B_N U_N(x)^k−U_N^(−k)B_N U_N^k||op
       ≤ 2k|x|C²/N.

Averaging k=0,…,T−1 therefore proves

    Σ_j |θ_j′(x)| ≤ v_N,T+C²|x|(T−1)/N.              (Q2)

Common-origin integration of each periodized derivative of a test gives
||f′||_1/N. As in the phase theorem, the expected absolute derivative of
its Laplace observable is bounded by ||f′||_1/(2π) times (Q2). The total
variation on [−R,R] dominates the supremum relative to x=0. Since
∫_{−R}^R|x|dx=R², this gives (Q1), including its factor 1/2 in the
quadratic correction. Sum the metric weights to obtain the metric claim.
Eigenangle multiplicities and measurability are treated as in the phase
theorem; the proof never divides by a level spacing.

## Classical ergodicity and the actual maintained map

If lim_{T→∞} limsup_{N→∞} v_N,T=0, (Q1) implies maximal comparison on
every bounded parameter interval. This condition follows for an ergodic
quantization with fixed-time Egorov and normalized trace convergence,
when B_N is the exactly trace-centered quantization of a fixed real
smooth mean-zero observable. For each fixed T, v_N,T² tends to the
classical L² norm squared of its T-step average; the mean ergodic theorem
then sends it to zero. Initial-eigenbasis quantum variance alone is
insufficient: a uniform flow bound comes from the time average and (Q2).

For a logarithmic rate assume T_N=⌊c log N⌋ and summable classical
correlations c_b(k), together with

    ε_N=sup_{0≤k<T_N}
      |N^(−1)Tr(B_N U_N^(−k)B_N U_N^k)−c_b(k)|=o(1/T_N).

The exact triangular correlation expansion gives v_N,T_N²≤C_b/T_N+ε_N.
Hence v_N,T_N=O((log N)^(−1/2)) if ε_N=O(1/log N). Under the stronger
displayed o(1/T_N) premise this conclusion certainly holds. Inserting in
(Q1), every R_N=o(√log N) gives a vanishing maximal difference.

The actual frozen-map applicability uses the maintained proof
polar_wkb_quantization_stability.md, Section 2, and FM-018 (O8)–(O14).
For a fixed smooth real symbol b, exactly centered by its quantum trace,
that proof supplies the correlation error

    |quantum correlation−classical correlation|
       ≤ C_b[N^(−2)exp(Γ|k|)+N^(−1)].

Together with the inherited exponential classical mixing input of
FM-018, a sufficiently small fixed c gives the required logarithmic
rate. Thus (Q1) applies to the unchanged maintained U_N as the base,
and its explicitly defined comparison family U_N exp(ixB_N/N), on
R_N=o(√log N). Constants and the cutoff depend on the fixed symbol and
the existing mixing/Egorov bounds; no uniform assertion over all symbols
or over all chaotic systems is made.

This is a full weak local point-process path comparison. A subsequential
limit of the initial common-origin process is transported to the constant
path. Uniform intensity one gives local tightness without extra count
moments. Unbounded factorial correlation expectations need their own
uniform-integrability/occupancy inputs, as in the prior transfer theorem.

## Dependency and novelty audit

The finite-N argument is self-contained. Its time-average comparison is
already in supplement/fixed_map/ergodic-transfer/ergodic_spectral_transfer.md,
Sections 1–4. That source already proves endpoint local-process transfer,
including multiplicities. The added statement here is the maximal path
bound (Q1) and its growing observation interval. The actual-map logarithmic
input is inherited from FM-018 and the smooth-symbol trace pairing in
polar_wkb_quantization_stability.md; it is not re-proved by a finite control.

The result does not determine the initial law. It can preserve a Sine law
if such a law is proved for the base, but also preserves other possible
subsequential laws. It does not remove a Brownian randomization of the
size used for local relaxation, or establish the signed Heisenberg-scale
TRACE-005 cancellation. BGS-BGS-001 stays open.

## Exact clock control despite perfect fixed-time decorrelation

The hypotheses of the finite-dimensional maximal theorem do not identify a
Sine law, even if every fixed nonzero time correlation vanishes exactly.
For N=2^d, d>=1, take U_N=diag(exp(2*pi*i*j/N)) and let B_N be the d-fold
tensor power of [[1,1],[1,-1]]/sqrt(2). Then B_N is Hermitian, B_N^2=I,
Tr B_N=0 and every squared entry is 1/N. Consequently

$$c_N(k)=N^{-1}\operatorname{Tr}(B_NU_N^{-k}B_NU_N^k)
       =N^{-2}|\operatorname{Tr}U_N^k|^2
       =\mathbf 1_{N\mid k}.$$

For 1<=T<=N the triangular correlation formula gives v_N,T^2=1/T exactly.
The maximal path bound therefore tends to zero on R_N=o(sqrt(log N)) at
T_N=floor(log N), while the initial common-origin process is exactly a
random translate of the integer lattice for every N. This example is an
abstract matrix control, with even dimensions and no assertion of a smooth
observable quantization for the maintained Anosov map. It is not a literal
BGS counterexample. It proves that the maximal bound and the observable's
fixed-time correlation decay, even at their strongest displayed finite
accuracy, cannot by themselves determine microscopic spectral statistics.

## The maximal estimate also survives the prior spectral rounding

This connects the new estimate with the prior
[microscopic rounding construction](../microscopic_rounding_control.md), without
claiming that construction as new. For any unitaries U,V and the same
Hermitian B with ||B||op<=C, put epsilon=||V-U||op. Telescoping powers gives

$$\|V^{-k}BV^k-U^{-k}BU^k\|_{\mathrm{op}}\le2Ck\epsilon,$$

and therefore

$$|v_T(V,B)-v_T(U,B)|
 \le N^{-1/2}\|A_T(V,B)-A_T(U,B)\|_F
 \le C(T-1)\epsilon.$$

The first inequality is the reverse triangle inequality and the second uses
the average of 2k, k=0,...,T-1, and ||X||F<=sqrt(N)||X||op. This is a
finite-dimensional statement, with no Egorov assumption. If epsilon_N=O(1/N)
and T_N=floor(c log N), the added error is O(log N/N). Every fixed smooth
observable's logarithmic maximal-path conclusion consequently survives
that rounding, on the same R_N=o(sqrt(log N)) interval.

The credited prior construction can simultaneously preserve its prescribed
low-trace window, entry flatness, intensity gap, reversal control and coarse
Egorov data, while having a fixed signed stable-band CUE pair defect with
liminf greater than 1/2. Adding the maximal-path conclusions does not make
those combined abstract controls sufficient for that necessary pair target.
This is a logical obstruction to a proposed implication: the rounded family
changes the exact propagator and is not a counterexample for the maintained
quantization. The prior proof, rather than a finite experiment, supplies the
pair-defect construction.
