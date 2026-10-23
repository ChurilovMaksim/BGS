# Microscopic point-process transport from eigenspace pinching

**Stable claim:** BGS-TRACE-071. **State:** PROVED.
**Boundary:** Full centered point-process path comparison on R^2 loglog(1/delta)/log(1/delta)->0; all fixed normal-source Lp products and derivatives. Random clock is conditioned on the phase-independent past. No initial law, no Lp norm of a continuous supremum, no higher physical-source product assertion.
**Integration and review:** [11 October disposition](../archive/record/chat_integration_20261011.md).
**Original input:** [dated source](../archive/evidence/executions/20261011/chat-research/original/laplace_path_transport.md).


11 October 2026. Self-contained project derivation extending TRACE-053/056.
Independent internal reconstruction is recorded separately. External priority
and formal certification are not asserted.

## Exact statement

Let S_m be deterministic unitary, δ_m=max_ij |(S_m)_ij|²→0 and
|| |S_m|²−J_m ||op≤ρ<1, where every entry of J_m is 1/m. Let H_m be
deterministic Hermitian, independent of the remaining iid uniform diagonal
phases D, with Tr H_m=m and Tr H_m²≤C_H m for a fixed C_H≥1.
Correlation of H_m with S_m is allowed. Define

W_x=DS_m exp(ixH_m/m),   W̃_x=exp(−ix/m)W_x.

Ξ_m(x) is the periodic point measure of eigenangles of W̃_x unfolded by
m/(2π), at a deterministic origin, with all integer translates by m included.
Eigenvalues are counted with multiplicity. For f≥0 in C_c^∞(R), write
L_f(ξ)=exp(−ξ(f)).

For an interval [−R,R], let β_m,R bound the operator norm on traceless
matrices of E_D E_{W_x}, uniformly over |x|≤R. E_W denotes full eigenspace
pinching, including repeated eigenvalues. Put a_m,R=√((C_H−1)β_m,R).
Then the finite-dimensional bound is

    E_D sup_|x|≤R |L_f(Ξ_m(x))−L_f(Ξ_m(0))|
       ≤ (R/π) ||f′||_L¹ a_m,R.                       (P1)

Choose a countable family (f_j) of nonnegative smooth compact tests, with
smooth cutoffs ≥1 on [−n,n] and a uniformly dense family on each enlarged
compact interval. The bounded metric

    d_L(ξ,η)=Σ_j 2^(−j)/(1+||f_j′||_1)
                         |L_f_j(ξ)−L_f_j(η)|

metrizes the vague topology on locally finite point measures. Moreover,

    E_D sup_|x|≤R d_L(Ξ_m(x),Ξ_m(0)) ≤ (R/π) a_m,R.    (P2)

Thus for fixed R the full centered point-process path approaches the
constant path of the same initial phase ensemble, in the uniform metric in
probability. Without centering, the comparison path is the deterministic
translation of Ξ_m(0) by x/(2π). This includes joint laws at any fixed
number of real parameter values; it does not identify the initial law.

There is also a growing-interval result. If R_m≥1 and

    R_m² log log(1/δ_m) / log(1/δ_m) → 0,

then the right side of (P2) tends to zero for R=R_m. Logarithms in this
condition are used only eventually, where δ_m is sufficiently small.

## Proof of the maximal bound

Put B=H_m−I. Tr B=0 and ||B||_F²≤(C_H−1)m. Along the analytic real
unitary flow, eigenangle branches are absolutely continuous. At a
multiple eigenvalue their velocities are the eigenvalues of the
compression of H_m/m; no simple-spectrum or minimum-gap assumption is
needed. At almost every x the centered velocities v_j satisfy

    Σ_j |v_j|²=m^(−2)||E_{W_x}B||_F².

Because B is independent of D, the pinching input and Cauchy–Schwarz give

    E_D Σ_j |v_j| ≤ a_m,R.                            (P3)

Periodize f at period m: f_m(t)=Σ_k f(t+km). Differentiation of the
Laplace observable and its bound by one give

    |∂_x L_f(Ξ_m(x))|
       ≤ (m/(2π)) Σ_j |v_j| |f_m′(mθ_j/(2π)−x/(2π))|.

Introduce a fresh independent common rotation φ∈[0,2π). D↦e^(iφ)D
preserves its law, rotates every eigenangle by φ, and leaves the
eigenspace pinching and centered velocity multiset unchanged. Therefore
each derivative weight has common-phase mean

    (1/m)∫_0^m |f_m′(t)|dt ≤ ||f′||_1/m.

One may formulate the velocity weights as spectral-compression traces,
so no choice of labels equivariant under common rotation is required.
Taking expectations and using (P3) yields

    E_D |∂_x L_f(Ξ_m(x))| ≤ ||f′||_1 a_m,R/(2π).

The supremum of the difference from x=0 is bounded by the total
variation on [−R,R]. Integration proves (P1). The path is continuous,
so its supremum is measurable as a supremum over rational x. Summing
(P1) with the displayed metric weights proves (P2).

To verify the metric, convergence of every Laplace coordinate to that
of a locally finite measure implies convergence of every f_j integral
by −log. The cutoff coordinates give uniform bounds for mass on every
compact interval. Uniform approximation then gives convergence against
every compactly supported continuous function. The converse follows
from vague convergence and the summable metric tail. This also shows
that the constant-path comparison is a statement about point processes,
rather than just a collection of isolated transform values.

## Uniform pinching on a growing interval

Since δ_m≥1/m and ||H_m||op≤√(C_H m),

    ||S_m exp(ixH_m/m)−S_m||op ≤ R_m√(C_H/m),
    δ_eff≤2δ_m+2C_H R_m²/m≤(2+2C_H R_m²)δ_m.

The intensity matrix is a restriction of Π Ad(S) Π, hence its operator
norm changes by at most twice the unitary operator-norm change. Under
the stated condition R_m=O(√log(1/δ_m)), this change tends to zero, and
the intensity singular gap stays uniformly below one.

TRACE-053 depends here only on that fixed gap and δ_eff. It supplies

    β_m,R_m≤C_ρ log log(1/δ_eff)/log(1/δ_eff).

The condition implies log(2+2C_H R_m²)=o(log(1/δ_m)), so these
logarithmic ratios are asymptotically equivalent. Consequently
R_m a_m,R_m→0, proving the growing-interval assertion.

## All fixed products of normally absorbed sources

For Z_m(s;W)=m^(−1)Tr[(I−exp(−s/m)W)^(−1)−I], Re s>0,
TRACE-056 gives L¹ comparison of W_x with V_x=exp(ix/m)DS_m.
The uniform phase-source bound from rank-one resampling gives, for
every fixed integer q≥2 and Re s≥σ>0,

    ||Z_m(s;W_x)||_q, ||Z_m(s;V_x)||_q ≤ L(σ)q.

Indeed both are independent-phase ensembles with a deterministic
unitary endpoint. For 1≤p<q, interpolation gives

    ||Y||_p ≤ ||Y||_1^a ||Y||_q^(1−a),
    a=(1/p−1/q)/(1−1/q),  Y=Z_m(s;W_x)−Z_m(s;V_x).

It follows that the comparison holds in every fixed L^p, uniformly for
|x|≤R_m under the same growing-interval condition. Fixed complex
s derivatives follow from Cauchy contours in Re s>0. Telescoping a
product and using Hölder with a sufficiently large fixed exponent
compares expectations of every fixed mixed product, with arbitrary
complex conjugates and those derivatives. This is a consequence for
normally absorbed endpoints, not for H-weighted anisotropic absorption.

## A general robustness corollary and its exact boundary

For arbitrary unitary U,V of size m and the common-origin averaged
Laplace observable Φ_m,f of FLOW-015, take the principal Hermitian
logarithm K of UV*, with spectrum in [−π,π]. The existing displacement
bound of FM-007 and the common-origin bound FLOW-015 (D14) imply

    |Φ_m,f(U)−Φ_m,f(V)|
       ≤ ||f′||_1 Tr|K|/(2π)
       ≤ (||f′||_1/4)||U−V||_1.                      (P4)

Here ||·||_1 is the unnormalized nuclear norm. This is a direct corollary
of existing project results, not a separate new principle. Common
rotations may be optimized out on the right. Nuclear error o(1) is
sufficient for common-origin weak local-law transfer, without occupancy
assumptions. The stronger unbounded factorial-correlation transfer
still needs its separate occupancy/uniform-integrability hypotheses.

The order cannot be relaxed uniformly to a bounded nuclear error.
For even m, let U have clock angles 2πj/m. Move every odd-indexed
angle backwards by 2πa/m, with fixed 0<a<1, obtaining V. Then
||U−V||op=O(m^(−1)) but ||U−V||_1→πa. For h=1−exp(−f) supported
in an interval of length w with 1−a<w<1, chosen positive on an interior
interval longer than 1−a, exact inclusion–exclusion gives

    Φ_m,f(V)−Φ_m,f(U)=½∫ h(t)h(t−(1−a))dt>0.

Only the alternating short-gap pairs overlap; no triple fits in a
window of length less than one. This diagnostic changes the operator
and is not a counterexample to the frozen quantization.

## Scope left open

The theorem homogenizes real spectral velocities of an independent-phase
ensemble and transfers its complete bounded local observables. It gives
no CUE/Sine identification for arbitrary deterministic S_m, no D=I
conclusion, no complex H-weighted physical-source L^p bound for p>2,
and no signed Heisenberg-scale trace cancellation for the literal map.
The phase-independent source assumption is essential in (P3): a source
chosen in the random eigenbasis cannot be inserted into averaged pinching.
