## 9. RUN 71 (2026-08-28) — TWO EXACT THEOREMS, AND WHERE THE ARITHMETIC ACTUALLY SITS

This section supersedes §8.0.4–§8.0.7 (void) and sharpens §7 (the ingredient
table). Full write-up with proofs: `paper/exact_wd_and_subgroup_moments.pdf`.
Machine certification: `artifacts/r71/`. Ledger: R71.

### 9.1 Standing assumptions used below

N odd prime p; A ∈ SL(2,Z) with gcd(c,N)=1; U_A and T(n) as in §1. Note the
run-3 correction, re-verified independently this run at machine precision:
the kernel satisfies `U_A T(n) U_A* = T(Aᵗ n)`, and the same identity with `A n`
fails by exactly 1.00 whenever b ≠ c. All statements below are for the `Aᵗ`
convention.

### 9.2 THEOREM A [PROVEN, exact, machine-certified]

**Lemma A1 (Weyl tight frame).** `Σ_{u ∈ (Z/N)²} T(u) X T(u)* = N·Tr(X)·1`.
*Proof.* The sum commutes with every `T(v)` (the Weyl cocycle phase cancels
between `T(v)T(u)` and its adjoint), the `T(v)` span M_N(C), so the sum is
scalar; its trace is `N² Tr X`. ∎

**Lemma A2 (compressed covariance).** For **any** isometry `B: C^m → C^N` and
`M^{(u)} = B* T(u) B`,

    Σ_{u ≠ 0} M^{(u)}_{ab} conj(M^{(u)}_{cd}) = N δ_ac δ_bd − δ_ab δ_cd,
    Σ_{u ≠ 0} M^{(u)}_{ab}      M^{(−u)}_{cd} = N δ_ad δ_bc − δ_ab δ_cd,

both **exactly**. (This is the correct, un-regrouped form of T19; the `N/K` and
`1/K` of T19 appear only after regrouping by Aᵗ-orbits.)

**Theorem A.** Let `V = Σ_{u≠0} g_u T(u)` with `g_{−u} = conj(g_u)` and the `g_u`
otherwise i.i.d. standard complex Gaussian (so `V = V*`). Then `V_B = B* V B` is
Gaussian Hermitian with covariance `N δ_ac δ_bd − δ_ab δ_cd`. The correction term
is supported on the one-dimensional identity direction, which is orthogonal to
the traceless Hermitian matrices and independent of them; hence

* the traceless part of `V_B` is **exactly** the traceless part of `√N · GUE_m`;
* adding a multiple of `1_m` shifts all eigenvalues equally, so **every statistic
  of the eigenvalue differences of `V_B` is exactly the GUE_m statistic** — all
  spacing distributions, number variances, form factors, n-level correlations, at
  finite m, not asymptotically;
* if `ran B` is Θ-invariant with Θ² = +1 and B is chosen so that Θ acts as
  complex conjugation (possible by T4), then the compression of the
  time-reversal projection `(V + ΘVΘ⁻¹)/2` is `Re V_B`, with covariance
  `(N/2)(δ_ac δ_bd + δ_ad δ_bc) − δ_ab δ_cd`: **exactly** `√(N/2) · GOE_m`.

**Corollary A3 (BGS for cat maps, random-observable form).** For a quantised
hyperbolic cat map, the first-order splitting of every degenerate multiplet under
a Gaussian Weyl observable has exactly GUE_m local statistics, and exactly GOE_m
after time-reversal projection, with β dictated by Θ.

**Certification.** `src/theoremB_covariance.py` →
`artifacts/r71/theoremB_covariance.json`: Lemma A1 ≤ 1.3e-13, both identities of
Lemma A2 ≤ 3.3e-14, traceless variance = N‖Y‖²_HS to ≤ 5.5e-15, Re-part = GOE
tensor to ≤ 1.9e-14, at (A,N) = ([[2,1],[1,1]], 41/101/151), ([[5,2],[2,1]], 71),
([[3,1],[2,1]], 181). Spacing-level confirmation in
`artifacts/r71/compression_spacings.json`.

### 9.3 The consequence that matters: what is NOT evidence

Lemma A2 uses nothing about B beyond `B*B = 1`. **Theorem A therefore holds
verbatim for a Haar-random m-dimensional subspace of C^N**, and the cat map
enters only through (i) the existence of eigenspaces of dimension ≈ N/K and
(ii) the antiunitary Θ needed for the GOE half. Consequently:

> Agreement with GOE/GUE measured using a Gaussian — or approximately Gaussian,
> e.g. a sum of two or more random Weyl operators — observable is a **theorem with
> no arithmetic content**, and is **not evidence about BGS**.

This is verified directly: in `artifacts/r71/hecke_centring_refutation.json` the
row `random_frame_control` (an arithmetic-free Haar frame) behaves identically to
the true cat-map eigenspace on every statistic measured. §7's rows for
"symmetry class", "second-order structure", "covariance of the observable family"
should be read as consequences of Lemma A2, not as arithmetic facts.

### 9.4 THEOREM B [PROVEN]: exact moments of subgroup Kloosterman sums

Let `H ≤ F_p^×`, `|H| = k`, `S(a,b) = Σ_{h∈H} e_p(ah + b/h)` — the model for the
Hecke-basis entries of §T11. Put
`E_{u,v}(H) = #{(h,g) ∈ H^u × H^v : Σh = Σg, Σh⁻¹ = Σg⁻¹}`, so that
`Σ_{a,b ∈ F_p} S^u conj(S)^v = p² E_{u,v}(H)`, and let `E⁰_{u,v}(k)` be the
number of solutions of `Σ ζ^{a_i} = Σ ζ^{b_j}` in `Z[ζ_k]`.

**(B1) Characteristic-zero rigidity.** `E_{u,v}(H) ≥ E⁰_{u,v}(k)`, since over C
the inverse equation is the complex conjugate of the first and hence automatic;
reduction mod a prime of `Z[ζ_k]` above p is injective on solutions. Equality
fails only if `p | N(α)` for some nonzero `α = Σζ^{a_i} − Σζ^{b_j}`; every
archimedean absolute value of α is at most u+v, so `p ≤ (u+v)^{φ(k)}`. **The
exceptional set is finite.**

**(B2) k prime ⇒ no characteristic-zero solutions.** With
`f(x) = Σ x^{a_i} − Σ x^{b_j}`, deg f ≤ k−1 = deg Φ_k, so `Φ_k | f` forces
`f = c·Φ_k`: all coefficients equal c, and summing gives `u − v = ck`. Hence
`E⁰_{s,s}(k) = P(s,k)` (pairs of s-tuples that are permutations of one another)
and `E⁰_{u,v}(k) = 0` for `0 < |u−v| < k`.

**Theorem B.** For k prime and `p ≡ 1 (mod k)` with `p > (u+v)^{k−1}`:

    Σ_{a,b} |S|^{2s} = p² · P(s,k),     Σ_{a,b} S^u conj(S)^v = 0  (0<|u−v|<k),
    P(s,k) = s!² [x^s] I₀(2√x)^k = s! k^s (1 − C(s,2)/k + O_s(k^{−2})).

So `S/√k` has **exactly** standard complex Gaussian moments up to an explicit
finite-k correction. Corollaries: the sub-Gaussian tail
`#{(a,b) : |S| ≥ λ√k} ≤ p² s! λ^{−2s}`, optimised to
`p² exp(−λ²/e·(1+o(1)))`; and a CLT `S/√k → complex Gaussian` whenever `k → ∞`
through primes with `log p / k → ∞`. **Contrast:** at k = p−1 the sum is the
classical Kloosterman sum and Katz's vertical Sato–Tate gives Catalan moments
2, 5, 14 rather than `s! = 2, 6, 24`. The transition is governed by the number
`(p−1)/k` of characters trivial on H, via
`S = (k/(p−1)) Σ_{χ|_H = 1} Kl_χ`.

**Relation to T17/T18.** s = 2 recovers T17 exactly: `P(2,k) = 2k²−k` for k odd,
and for k even the extra solutions are the vanishing-sum relation of `μ₂ ⊂ μ_k`,
giving `3k²−3k`. T18(a) is the Mann / Conway–Jones structure theorem for
vanishing sums of roots of unity, and T18(b) ("sporadic mod-p coincidences") is
exactly the condition `p | N(α)` of (B1). Empirically, over 54 (k,s) cells, the
sharp criterion is `E⁰(s,k) = P(s,k) ⟺ s < lpf(k)`; proved here for k prime and
for `k = q^e`, conjectural in general.

**The exceptional set (new open problem `conj:Pstar`).**
`P*(k,s) = max{p : E_s(H) > P(s,k)}`, determined exhaustively for prime k
(`src/pstar_scan.py`): 89, 199, 683, 3719, 6469 for k=11, s=3..7; 79, 911, 7151,
25819 for k=13, s=3..6; 409, 16661 for k=17; 761, 110771 for k=19; 4049, 102397
for k=23. The rigorous bound `(2s)^{k−1}` is astronomically weak (8¹² ≈ 7·10¹⁰ at
k=13, s=4, versus the true 911). The minimal nonzero excess is always `18k` at
s=3 and `32k` at s=4, and `18 = 3·3·2`, `32 = 4·4·2` identify the minimal
sporadic configurations as the multiset shapes `{a,a,b}` and `{a,a,a,b}` — i.e.
F_p-points of explicit curves. **Conjecture:** `P*(k,s) ≤ C k^{cs}` with c ≈ 1,
equivalently exact Gaussian moments as soon as `k ≤ p^{1/(cs)}`. This is the
quantitatively useful form and the concrete successor to `op:tail`.

**Barrier (unchanged, T18).** With `k = p^θ` the "random" term `k^{2s}/p²`
overtakes the main term `s! k^s` once `s > 2/θ`, so no version of Theorem B can
reach `s ≍ log m`. The mean-spacing scale needs a resolvent argument, not
moments.

### 9.5 The deterministic problem is open, and the naive answer is wrong

T20 claimed that a single Weyl orbit (two real parameters) already gives GOE.
Clean-room replication (`src/compression_spacings.py`, `src/single_orbit_trend.py`)
with size-matched true GOE controls through an identical unfolding pipeline gives,
for the Hermitian part of `P_λ T(u) P_λ`, a **systematically positive** deviation
from GOE that does **not** shrink with the multiplet size:

| p | K | m | control L1(GOE) | single-orbit L1 | z (mean over 8 orbits) |
|---|---|---|---|---|---|
| 8969 | 59 | 153 | 0.3503 ± 0.0554 | 0.4847 | **+2.43 ± 0.46** |
| 3571 | 17 | 210 | 0.3029 ± 0.0512 | 0.4449 | **+2.77 ± 0.47** |
| 14503 | 56 | 259 | 0.2876 ± 0.0529 | 0.2903 | +0.05 ± 0.36 |
| 9349 | 19 | 492 | 0.1900 ± 0.0352 | 0.3756 | **+5.28 ± 0.45** |

By contrast a Gaussian combination over L ≥ 2 orbits is indistinguishable from
GUE (|z| ≤ 0.6 at L = 2, 8, 16, 32, 64) and its Θ-projection from GOE
(|z| ≤ 1.6) — exactly as Theorem A requires. The project's own T20/N1 numbers
already gave z = +3.3. **Status:** a single Weyl-orbit compression is close to but
statistically distinguishable from GOE, by a systematic 2–5σ, with no visible
decay in m. `op:local_deterministic` is the real BGS content of this family and
it is open; the natural target to test against is the Kurlberg–Rudnick
SU(2)-trace distribution, not a Gaussian.
