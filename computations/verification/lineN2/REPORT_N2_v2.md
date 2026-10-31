# REPORT_N2 v2: Line N2, the inherited level c = h_p as a periodic-orbit / pressure problem

*v2 applies the referee fixes N2-F1 … N2-F9 (`/workspace/audit/lineN2/REPORT.md`). The original is kept as REPORT_N2.md. Each fix is marked [N2-Fk] where it is applied. See §8 for the list and N3/REPORT_N3.md for the follow-up.*

Status date: 2026-10-31 (Asia/Yekaterinburg, UTC+5). Working dir: `/workspace/bgs-lineN/N2`. REPORT_N.md was left alone because it is under referee audit; corrections to it are listed in §1 here. Nothing was pushed.

**Labels.**
- [P]: proved, modulo the *standing inputs* named in each statement (Line F spectral certificate F2, J3 weights and inheritance, K/K2 W1–W3, W2′ and Theorem K, Line L Lemma O1 and its τ-profile and C_pair, L3 S4).
- [CA]: computer-assisted and rigorous (python-flint/arb ball arithmetic, script named).
- [N]: floating-point numerics with no error control.
- [H]: heuristic.

---

## 0. Summary

| Goal | Outcome | Label |
|---|---|---|
| (a) β-weighted K2′ that the slow orbit does not trivially satisfy, and that still kills frozen R′ | Theorem A. It implies H♮_mid, so by Theorem K, R′ fails. The N3 slow orbit contributes about 1.0644^m < 1.28359^m, so it is not the obstruction. | [P] mod standing inputs |
| (b) cross part at c = h_p as a sum over period-p points, weighted by the cocycle | Theorem B: an exact identity over G_p = (1/h_p)Z²/Z² ⊂ Fix(A^p), which has **index 4** (not 32). Also a Fourier / cyclic-path form and a Bowen-ball comparison with Lebesgue. | [P] (+[N] check) |
| (c) pressure bound below 1.28359 | Theorem C reduces the unit-point part to Λ_{k′}·r_2(k) < T³. **r_2 is now certified** (Prop. E): r_2(4000) ≤ 1.0529012 for 8V (others in §4). **Λ (the twisted joint spectral radius) is not certified.** [N] evidence says Λ_{30} ≈ 1.98242 against the threshold 2.00859, with asymptote μ* ≈ 1.91547. | [P] + [CA]; conditional on Λ [N] |
| (d) refuting R′ along m = 3p | **No.** Even with Λ certified, the pressure lever only controls the light (unit) points at h_p. The heavy levels still block: isotropic lines at every prime q ∣ h_p, small divisors of h_p, and the K_p-prime and mixed rank-3p conductors in (c_N p^{7/3}, L_m). An index-loss barrier [P] shows the same pressure method cannot reach them. | [P] barrier |

The conditional result in plain terms: *if* sup_y‖P_{30}(y)‖^{1/30} ≤ 2.0085 in the Line F lifted V representation (numerically 1.98242), then at the inherited level h_p, for every p, the unit-point cross part grows at rate at most (Λ_{30}·r_2)^{1/3} ≤ 1.2780 < 1.28359 [P+CA]. This is a statement for all p, but only about one sub-piece of the open range.

---

## 1. Setup, errata, attribution

**1.1 [P + N].** Fix(A^p) has |det(A^p − I)| = 4h_p² points, and A^p − I = h_p·B with B integral and det B = −4. So G_p := (1/h_p)Z²/Z² ⊂ Fix(A^p) has index 4. Verified for all primes p ≤ 47 (`code/a_index_identity.py` → `logs/a_index_identity.json`).
- **Erratum (REPORT_N §7/N4, repeated in the brief):** "index 32 = N(4√2)" is wrong. The index is 4.
- The map y ↦ (Tr y, Tr λy) mod h_p is a bijection O/h_p → (Z/h_p)² [P; checked].
- **Referee confirmation** (`/workspace/audit/lineN/REPORT.md` §6, fix N-F8): Fix(T^p) = (4√2·h_pε^p)⁻¹O/O^∨ has 4h_p² points. The conductor-h_p points ((1/h_p)O + O^∨)/O^∨ number h_p², so the index is 4. The value 32 came from forgetting [O^∨ : O] = N(2√2) = 8, and 32/8 = 4. N2 uses 4 throughout, and nothing downstream in N2 depends on the index beyond |G_p| = h_p² ≍ λ^p.

**1.2 Attribution.**
- REPORT_N's N3 (slow β at a *prime* scarred conductor q ∥ h_m) duplicates Line L2, Proposition S (`bgs-lineL/L2/REPORT_L2.md` §1, threshold C_k + 6.1·10⁻⁶ m). That should be credited to L2.
- What N3 adds is composite conductors, chiefly c = h_p, and that is the case used here.

**1.3 Sectors.**
- The fixed points of A are the constant twists 0, ¼, ½, ¾. Sector a is the constant twist a/8, and sectors are torus translates: L_{a,τ} = L_{0,τ+a/8}.
- μ* (|μ*| ∈ [1.9154712, 1.9154752], Line F F2 [CA]) sits at twist ½ (sector 4). The rest of that spectrum is in |z| < 1. The other sectors and the E family have untwisted spectral radius < 1.

---

## 2. (a) Theorem A: weighted K2′ [P mod standing inputs]

For a family F, k ≥ 1 and clamp 0 < a ≤ 1, set ψ^F_{k,a}(y) = (1/k)·log max(a, ‖P_k(y)‖_op), where P_k is the k-step kicked cocycle. Define

  Ω^F_m(k,a) = Σ_{c open} Σ_{β mod c} |W_{c,β}| · (σ(h_m)/h_m) · exp(Σ_{i<m} ψ^F_{k,a}(βλ^i/c)).

Here W_{c,β} are the J3 weights:
- for a prime q ∥ h: W = q⁻²(−1 − e(N(β)t̄_b/q)), so |W| ≤ 2/q² off the isotropic lines and (q−2)/q² on the 2(q−1) isotropic β;
- for composite c: the CRT product;
- for inheritance: W_{ce,eβ′} = (n_e/e²)·W_{c,β′}, with total multiplier ≤ σ(h)/h.

**Theorem A.** Suppose that for infinitely many m ∈ S⁺, every F satisfies Ω^F_m(k,a) ≤ e^{o(m)}·((1−δ)T_F)^m for some fixed k, a, δ > 0. Then the open-range cross part is o(ξ_lo^m). Hence H♮_mid holds, and by Theorem K the frozen R′ (TRACE-206) is false. The same holds if ψ is replaced by a fixed geometric mean of finitely many such potentials (different k, a, op or HS).

*Proof sketch.*
1. W2′, before the geometric mean, gives |Tr| ≤ C_J·max(1, sup‖L‖)^{2k}·e²·a^{−2}·exp(Σ_{i<m}ψ). The blocks miss at most 2k positions, and each clamp costs a^{-1}.
2. The cross part at level c is 2Re(conj Z_ρ · Σ_β W·Ẑ_β), with |Z_ρ| ≤ Cμ^m and μT_F ≤ ξ_lo.
3. Summing over open c with the inheritance multiplier gives exactly Ω, so the hypothesis yields o(ξ_lo^m).
4. The rest is Theorem K.

**What is missing for [P] unconditionally.** Nothing beyond the standing inputs. The issue is only whether the hypothesis can be verified.

**Sourcing of the |Z_ρ| inputs (referee fix N-F2).**
- Theorem A needs only the *upper* bound |Z_ρ| ≤ C·μ_F^m with μ_F·T_F ≤ ξ_lo.
- The *lower* bound behind N3 (the slow orbit makes the unweighted K2′ false) must be taken **per family** from the proved spectral-radius bound of TRACE-198 [CA], ρ(L₀^F) ≥ μ* for that same family F. It must not come from the Line F standing input plus a switch of family. With that change, N3 is [P] with no standing input.
- This requires the period/truncation condition r > 2(N + k), coming from the min(r,·) truncation. For c = h_p, r = p, and log_λ h_p = p/2 − O(1).
- θ_F and t_F are fixed per family (t_F ≈ 25 + k ≈ 40, an [H] estimate from the referee). So N3 at c = h_p applies for p ≳ 110 [H]: effective, but not computed.

**Non-triviality.**
- The N3 slow orbit at h_p (twist ½, i.e. the μ*-point) contributes at most (μ*/λ^{1/3})^m·e^{O(1/k)} ≈ 1.0644^m < T^m = 1.28359^m. This uses the F2 gap ‖L_4^n‖ ≤ C_0μ^n, so that orbit does *not* by itself violate the hypothesis.
- The unweighted K2′ of REPORT_N had been trivially *false* because of that orbit; the weights are what fix this.

---

## 3. (b) Theorem B: the cross part at h_p as a periodic-orbit sum [P]

**Theorem B.** At c = h_p (m = 3p),

  Ẑ_β = Σ_F a_F·Tr(J_F·M_F(y)³),  where y = y(β) ∈ G_p,

and M_F(y) is the p-step operator cocycle along the A-orbit of y (L3 S4). So

  Σ_β W_{h_p,β}·Ẑ_β = Σ_{y ∈ G_p} W(y)·Σ_F a_F·Tr(J_F·M_F(y)³).

This is a weighted sum over an index-4 subgroup of the period-p points of the cat map: a twisted dynamical zeta / transfer-operator quantity.

**Fourier form [P; N-checked at p = 5, error 1e-13].**
- E_{G_p}Π_{i<p}g(A^i y) = Σ_{(k_i): Σ_i (A^T)^i k_i ∈ h_pZ²} Π_i ĝ(k_i).
- Equivalently it is a sum over cyclic state paths D_{i+1} = A^{−T}(D_i + k_i) on the lattice B^{−T}Z², which has index 4 over Z².

**Bowen-ball lemma [P].**
- Fix(A^p) is (p,ε)-separated by expansivity. So for continuous φ,
  Σ_{y ∈ G_p} e^{S_pφ(y)} ≤ (λ^{p+k}/(c′ε²))·e^{pω_φ(ε)}·∫e^{S_pφ} dLeb.
- Since |G_p| = h_p² ≍ λ^p, the average over G_p is at most e^{p·ω(ε)}·O_ε(1)·∫e^{S_pφ}.

**Interpretation [P-cite].**
- The growth rate is a subadditive pressure, sup_μ[h_μ − log λ + 3χ(μ)] (Cao–Feng–Huang 2008; Bowen volume lemma).
- Endpoints:
  - [P] δ_0 (the slow point): 3 log μ* − log λ = 0.187 < 3 log T = 0.749.
  - [P+CA] Lebesgue: χ(Leb) ≤ (1/2k)·log I_k ≤ log 1.26278 < log T (Line L certificate plus Jensen).
  - Low-entropy measures are fine. The middle entropy band is what needs Λ.

---

## 4. (c) Pressure reduction (Theorem C) and the certified block rate (Proposition E)

**Theorem C [P mod standing inputs].** For every F, k, k′, a ∈ (0,1] and η > 0:

  limsup_p (1/p)·log E_{y∈G_p}|Ẑ^F(y)| ≤ log Λ^F_{k′} + log r_2^F(k) + η,

where:
- Λ^F_{k′} := sup_{y∈T²}‖P_{k′}(y)‖_op^{1/k′}, computed as an operator norm **in the same Hilbert space as the O1 HS bounds**, i.e. the lattice-lifted space (ρ, β) = (0.75, 0.25) for 8V, (0.2, 0.3) for 8E [N2-F1]. Alternatively, it can be computed in the Line F space (ρ = 1.2 / 0.8, β = 2.5) **together with** an intertwining lemma whose constants do not depend on p. N3 proves such a lemma (Lemma I, N3 §2.1). The [N] values below are in the *truncated* Line F lift (K0 = 3), so as stated here they are not yet numerics for the right object;
- r_2^F(k) := R^{1/k}, where R is any Collatz–Wielandt bound for the block matrix B = a·Z^k + C_pair·M_0⋯M_{k−1}. This block matrix is the carry automaton of exact collisions with Line L O1 weights.

*Proof.*
1. Split by geometric mean: |Ẑ| ≤ C·e^{S_pψ^{op}_{k′}}·e^{2S_pψ^{HS,a}_k}.
2. Bound the first factor by its sup: Λ_{k′}^p.
3. Apply the Bowen-ball lemma to φ = 2ψ^{HS,a}_k.
4. Write ∫Π_{i<p}(a+f_k)^{1/k}(T^iy) and apply Hölder over the k residue classes, using T-invariance of Leb. The leftover positions cost at most (a + sup f_k), a constant.
5. ∫Π_{j<Q}(a+f_k)(T^{jk}y) is a sum of exact collisions of concatenated words. By Lemma O1 it is majorised by Σ_{v: α_v=0} Π_j[a·1[v^{(j)}=0] + C_pair·Π_iρ_i(v_i)] = ∫Π_j[a + C_pair·Π_i ρ̂_i(τ_{jk+i}(y))] dy.
6. Proposition E bounds this by R^Q.

**Proposition E (finite, tail-free majorant) [P] + certificate [CA].**
1. ρ_i(d) = Σ_a u_i(a)u_i(a−d) with u_i ≥ 0, so ρ̂_i = |û_i|² ≥ 0.
2. For any V, ρ̂_i ≤ g_i := Σ_{|d|≤V} ρ_i(d)e(dt) + ε_i pointwise, where ε_i ≥ Σ_{|d|>V} ρ_i(d). The coefficients of g_i are nonnegative and supported on |d| ≤ V.
3. An exact collision v = (X²−6X+1)E(X) has carries e = G∗v, with G(n) = λ^{−|n|}/(λ−λ^{−1}). Since Σ_n G(n) = √2/(4√2) = 1/4 exactly, letters |v_i| ≤ V force |e_j| ≤ ⌊V/4⌋.
4. So the finite carry automaton on [−⌊V/4⌋, ⌊V/4⌋]² computes the majorant **exactly**, with no tail. A finite Collatz–Wielandt bound Bx ≤ Rx with x > 0 then gives ⟨0|B^Q|0⟩ ≤ R^Q.
   - This replaces Line L's whole-word Chernoff tail, which does not scale to long products.
   - It also replaces the u-coordinate discretisation (`code/b2_u_operator.py`), which turned out to be unreliable: its Perron vector lives on the countable set {b − a/λ}.

**Certificate setup** (`code/e_r2_cert.py`, arb at 128 bits):
- V = 40, E0 = 10 (441 states), a = 1, J1 = 14.
- The 2·14 boundary letters use their own τ_j. The middle letters use the single upper value τ_mid, which is valid because ρ is monotone in τ.
- Bessel tails are bounded by (x/2)^a/a!.
- The float Perron vector is checked in arb; the float rounding of the final endpoint is absorbed by a factor (1 + 2⁻⁴⁰).

**[CA] certified upper bounds on r_2(k)** (log: `logs/e_r2_cert.jsonl`; they agree with the float `b_r2_float.py` values to about 1e-15):

| Family | C_pair | ε_max (V=40) | k=1000 | k=2000 | k=4000 | Λ-threshold T³/r_2(4000) |
|---|---|---|---|---|---|---|
| 8V | 25.83 | 3.9e-12 | 1.0582753 | 1.0546895 | **1.0529012** | **2.00859** |
| 8E | 9.09 | 3.0e-18 | 1.0543496 | 1.0527315 | 1.0519234 | 2.01046 |
| 16V | 1044.9 | 1.7e-15 | 1.0605065 | 1.0558008 | 1.0534557 | 3.04126 |
| 16E | 582.0 | 2.5e-19 | 1.0583518 | 1.0547276 | 1.0529202 | 3.04280 |

The per-letter rate tends to r_abs ≈ 1.0511 [N].

**The missing input Λ (not certified).** Numerics for 8V (Line F lift, K0 = 3, r = 1.2, K = 20, β = 2.5, N0 = 10):
- [N] (`c2_jsr_periodic.py`, `logs/c2_jsr_V*.json`): over all periodic points of period ≤ 4, the maximal spectral rate is exactly μ* = 1.9154732, attained at the fixed points.
- [N] Sampling plus local refinement of sup_y‖P_{k′}(y)‖^{1/k′} lands on the constant-twist point: **2.12342 (k′=10), 2.01677 (k′=20), 1.98242 (k′=30)**.
- [N] (`c4_free_ascent.py`): for the *unconstrained* family {L_τ}, i.e. arbitrary twist sequences, coordinate ascent from 1 + 8 starts (k = 12) and 1 + 5 starts (k = 24) always converges to constant τ = ½ with a boundary excursion:

  | k | free maximum | constant τ = ½ |
  |---|---|---|
  | 12 | 2.11721 | 2.08725 |
  | 24 | 2.01382 | 1.99952 |

  This is consistent with free JSR = μ*. The excursions are transients that vanish like C^{1/k}.
- E family (`c2`, r = 0.8): sup ≈ 0.401 at k′ = 30, far below 2.01.
- The 16 families need Λ < 3.04. They were not computed in N2.

**Conditional corollary [P + CA, conditional on Λ].** If Λ^{8V}_{k′} ≤ 2.0085·(1−δ)³ for some k′ (the [N] value at k′ = 30 is 1.98242), and the corresponding bounds hold for 8E, 16V and 16E, then for **all** p the unit-point cross part at c = h_p is O(e^{o(p)}·(1−δ′)^m·T^m):
- the unit weights are |W| ≤ 2^{ω(h_p)}/h_p² = e^{o(p)}/|G_p|;
- with Λ = 1.98242 and r_2 = 1.05290 the rate is (Λ·r_2)^{1/3} = **1.27799 < 1.28359**;
- asymptotically, with Λ → μ*: (μ*·r_2)^{1/3} = **1.26344**, a margin of 1.6%.

The constants are astronomically large (sup f_k with k = 4000, and the Bowen-ball ε), but they do not depend on p.

**What a full [CA] for Λ would need.** Both are feasible in principle; neither was done here.
1. A truncation-error bound for the lifted operator *uniform in the twist τ*. Line F's ε_F control was for fixed twists.
2. An extremal-norm certificate sup_τ |||L_τ||| ≤ Λ_target on a τ-grid with a Lipschitz margin. A naive Lyapunov ellipsoid built from L_{1/2} alone fails (`c5_ellipsoid.py`: 9.15), so this needs an SDP or a polytope extremal norm.

The cheaper alternative is to bound only cat-map-constrained products. But a direct torus grid needs resolution λ^{−k′} in the unstable direction, which is infeasible for k′ ≥ 20. The free family is the practical route.

**Barriers [P].**
- Phase-blind word-level bounds fail at h_p. They need G < T·λ^{1/3} = 2.3101, but G = Σ|J_n(1.8)| = 2.3693986.
- The phase-blind Cauchy–Schwarz moment route gives 2.385 > 2.115.
- So any certificate must use the y-dependence of the operator norms, as Theorem C does.

---

## 5. (d) Does this refute R′ along m = 3p? **No.**

Combine Theorem W/W⁺ (prime and large conductors via Weil), Theorem U, the Line L/L3 decomposition, Prop K2 (levels > L_m), and Theorem C with Λ assumed. The open range (c_N p^{7/3}, L_m), with L_m ≈ λ^{0.227m}, still contains these blocking levels:

1. **Isotropic lines at every prime q ∣ h_p.**
   - All q ∣ h_p split in Q(√2), so these lines always exist.
   - Their weight is (q−2)/q² per point, about q times the unit weight. The isotropic β form a sub-orbit of index ≥ q ≈ λ^{p/2} when q is large.
   - The Bowen / pressure majorant is of e^{S_pψ} type and cannot see an index-q subgroup. Over the sub-orbit, the majorant includes the β = 0 (μ*) term, which gives ≥ (μ*/λ^{1/6})^m = 1.428^m > T^m. **[P] barrier: the method loses the subgroup index.**
2. **Small and medium divisors d ∣ h_p with d < h_p·κ^{−p/2}**, where κ = T³/(Λr_2) ≈ 1.05. The same loss applies: the e^{o(p)} slack is spent.
3. **K_p-prime and mixed rank-3p conductors in (c_N p^{7/3}, L_m)**, where K_p = 4h_p² + 3 and 7 ∣ K_p always.
   - Their points lie in Fix(A^{3p}) at index ≥ λ^{3p}/L_m².
   - The analogous Bowen bound gives a per-m factor λ/L_m^{2/m} = 5.828/1.4923² = 2.617 > T. **[P] barrier: the pressure method does not handle them.**
   - Levels 7·d are handled like h_p (period-3 modulated cocycle) for unit points only.

Even in the best case (h_p prime and K_p/7 prime, so K_p-levels exceed L_m and Prop K2 absorbs them), item 1 still blocks at h_p. Whether infinitely many p have K_p/7 prime is itself open (Bunyakovsky-type).

**[N] sanity check on true TRACE-206 sums** (`code/d_level_split.py`, L2 transfer law; target 1.28359):

| (m, q = h_p) | unit-part rate (1/q²)Σ_unit\|Ẑ\| | isotropic-part rate (1/q)Σ_iso\|Ẑ\| | max single unit-point rate | max single iso-point rate |
|---|---|---|---|---|
| (15, 41) | 1.1209 | 1.0559 | 1.4414 | 1.0729 |
| (21, 239) | 1.1342 | **1.1604** | 1.5616 | **1.2780** | [N2-F8]: the original run had finished (1584.6 s); the duplicate restart was killed before appending |

At these m both parts are below target. Single unit points can exceed T, which is why an averaged (pressure) statement is the right form. **At (21,239) the isotropic part is the larger one** (1.1604 > 1.1342), and its largest single point reaches rate 1.2780. So the isotropic obstruction may not be purely methodological [N; no trend claim from two data points] [N2-F8].

---

## 6. Rigour ledger
- [P] Theorems A, B, C; Proposition E (the structural part); the index-4 fact.
- [P] **(lower bound for the pressure majorant)** for the barriers of §5. These are statements about the method's majorant, not about the true sums. The 2.617 bound uses the clamp a = 1, so the Lebesgue integral is ≥ 1 [N2-F7].
  - All are modulo the standing inputs: F2, J3 weights and inheritance, W1–W3 and W2′, Theorem K, Lemma O1, L3 S4.
  - The O1 constants and τ-profile were taken from Line L as given and were not re-derived.
- [CA] r_2(k) bounds in §4 (arb). Inherited [CA] items: μ* enclosure (Line F), I_k (Line L).
- [N] The JSR Λ values, the free-family ascent, the level split numerics, b2 (abandoned).
- [H] None used in any conclusion.

## 7. Files
- `NOTES_N2.md` (working log)
- `code/`:
  - `a_index_identity.py`
  - `b_r2_float.py`, `b2_u_operator.py` (abandoned)
  - `c_jsr_float.py`, `c2_jsr_periodic.py`, `c3_free_jsr.py` (greedy beam; uninformative), `c4_free_ascent.py`, `c5_ellipsoid.py`
  - `d_level_split.py`
  - `e_r2_cert.py`
- `logs/`: the matching `.json` / `.jsonl` / `.out` / `.npy` files. `e_r2_cert_prelim.jsonl` is the first run, before the rounding guard; it gives identical values to 1e-15.
- `SHA256_N2.txt` and `SHA256_N2.txt.sha256`.


---

## 8. v2 amendments (referee N2-F1 … F9)

- **[N2-F1] Representation.** Theorem C requires Λ as an operator norm in the O1 space (see the §4 text above). The intertwining Lemma I is proved in N3 §2.1: with C_I independent of p and τ, ‖P^{O1}_{k′}‖ ≤ C_I·‖P^{F}_{k′−3}‖ (V; two end steps for E). So Λ may be certified in the Line F space, where the core perturbation is tiny. The phrase "in any valid representation" is withdrawn.
- **[N2-F2] Theorem B at the composite level h_p.** It is [P, by the proof of TRACE-266]. The cyclicity argument (λ^p ≡ 1 mod 2h_p, so the twist sequence has period p) does not use primality. Registry: widen TRACE-266 to every c with ord_c λ = p.
- **[N2-F3] Theorem A** holds for m ≥ m₁ (TRACE-245; effective, not computed). "Open" means as in TRACE-246: the Weil-range levels and the composite levels below c_W·p² are covered by TRACE-245 / TRACE-246, matching TRACE-239's O♮^{<L}. Theorem A is a **proved implication** ("Ω-hypothesis ⇒ H♮_mid ⇒ R′ false", like TRACE-257). Its Ω-hypothesis is a new **open** item, and TRACE-240 (Theorem K) is itself conditional in main.
- **[N2-F4] Families.** The N3 lower bound uses the family F that carries μ* (TRACE-198: the V family, where μ* is untwisted in sector 4). Theorem A needs the *upper* bound μ_F·T_F ≤ ξ_lo for every F. The (±2,16) families have μ_F ≤ 1.6677 (TRACE-253). Check: μ*·T = 2.458680 < ξ_lo = 2.458689.
- **[N2-F5] Non-triviality at all conductors.** A slow N3 segment of length 2·log_λ c costs a factor (μ*/T)⁶/λ² = 0.325 per unit of log_λ c at rank p, and 0.066 at rank 3p. Both are < 1, so N3 slow orbits never violate the Ω-hypothesis at any level.
- **[N2-F6] Λ numerics.** The [N] values (2.12342 / 2.01677 / 1.98242 at k′ = 10/20/30, and the free-family ascent) come from sampling plus local refinement. They are **lower** estimates of a supremum. The k′ = 20 value (2.01677) and the free k = 24 maximum (2.01382) **exceed** the 8V threshold 2.00859, so any certificate needs k′ ≳ 30 or an extremal norm. The corollary's hypothesis must also include the (±2,16) Λ < 3.04, which was not computed. N3 replaces sampling by certified extremal-norm *upper* bounds on the free family (N3 §2).
- **[N2-F7] Barriers.** They are lower bounds for the pressure majorant, not for the sums (applied in §6). 2.617 = λ/L_m^{2/m}, with clamp a = 1.
- **[N2-F8] (21,239)** row filled in. The sentence "isotropic part not numerically worse" is deleted. `logs/d_level_split.jsonl` is in the v2 manifest.
- **[N2-F9] Unit weights.** |W| ≤ 2^{ω(h_p)}/h_p² assumes h_p squarefree, because J3 weights are stated for q ∥ h. For q^a ∥ h_p with a ≥ 2, use the prime-power weights (J3 §3: |W| = 1/q² and (q−1)/q² when q² | h, and CRT products in general). These are ≤ 2/q² per prime power on unit β, so the same bound holds with 2^{ω} = e^{O(p/log p)} = e^{o(p)}. Alternatively, assume squarefreeness explicitly. The rate statement is unchanged.
- **Prop E remark.** The Perron vector is clipped at 1e-200. That is still rigorous, since Collatz–Wielandt accepts any x > 0. The referee's independent left-vector certificate gives r_2(4000) ≤ 1.05290115 (8V), 1.05192335, 1.05345567, 1.05292016.
