> **Packet copy (Line B, IDs BGS-TRACE-163 to 182).** On main at 502af245 the highest TRACE id is BGS-TRACE-162, so 163 is the next free id; the block was not renumbered. This is the detailed phase report cited by `../derandomized_fixed_kick.md`, copied unchanged below this box. Its status labels ([P], [P-sketch], [N], [C], [Cert], [L], [H]) are the working labels; the **integration status of every claim is the one in `../derandomized_fixed_kick.md` and `record/claims.json`**, which follow the referee's table (audit §8.10) with the second-reader upgrades of 167, 169 and 173 (`computations/verification/lineB/second_reader/SECOND_READER_REPORT.md`). Path map: `phase3/code/`, `phase3/logs/` → `computations/verification/lineB/phase3/`, `…/phase3/logs/` (ECPP certificates in `computations/verification/lineB/ecpp/`); `phase3/lean/Phase3Checks.lean` → `formalization/Bgs/LineBPhase3.lean` (`Bgs.LineB.Phase3`).

# Phase 3: fixed-η off-diagonal W_m(η), parity symmetry breaking, primality certificates

> [ref23-fix] Referee audit of phases 2+3 (/workspace/audit/derand23/REPORT.md) applied: items 8–16 of its fix list. Phase 4 (phase4/REPORT4.md) supersedes §3's decay claim (certified on a compact η-range, sketched for all η) and §4(b) (torsion attribution withdrawn).

Labels:
- [P] proved here.
- [P-sketch] proof outlined, standard step not written out.
- [N] numerical, exact arithmetic or float with stated error.
- [C] conjecture.
- [L] Lean-checked (`decide`/`ring`, no native_decide).
- [Cert] PARI ECPP certificate verified by `primecertisvalid`.

All new files are in /workspace/bgs-derand/phase3/ (code/, logs/, lean/). Lean was built only in the private copy phase3/build after `lake exe cache get`.

**Model conventions (referee correction applied).**
- ξ runs over the q-sequences of Fix(T^m), with T = [[0,1],[−1,6]]. This is not Fix(S^m) by position sequence.
- For odd m the support is 𝒮 = ½·𝟙 + V^_odd. Here V^_odd ≅ (Z/h_m)² via (x₀, x₁) ↦ the sequence x_{j+1} = 6x_j − x_{j−1} (mod h), with ξ_j = ½ + x_j/h.
- Γ is the dihedral group of shifts and reversals of q-sequences.
- All phase-2 and phase-3 code (`Orbits`, `fast_classes.py`) uses exactly this model.

## 0. Summary of outcome

The target was W_m(η) = o(m) at fixed η. Its status:

1. **W_m splits exactly into a parity part and a remainder [P].**
   - F_m(η) = B^sym_m + 2m·χ_m(η) + W^rest_m(η) + E, with |E| ≤ 4m²/h_m. Write W̃^rest := W^rest + E = F − B^sym − 2mχ_m; **all tabulated "W^rest" values in this report are W̃^rest** [ref23-fix].
   - The parity part comes from the pairs (ξ, −γξ). x ↦ −x is a symmetry of the cat map that is not in Γ, and the kick breaks it only through the small odd part f_odd of its symbol.
2. **The parity part is solved [P identity + N spectrum].**
   - χ_m(η) = Σ_{a=0}^{3} (−1)^a Tr M_a(η)^m exactly, for an explicit transfer operator M_a(η).
   - Its leading eigenvalue μ(η) = exp(−2‖f_odd‖²η²)(1 + O(η⁴)) with ‖f_odd‖² = 60/800² [L].
   - Numerically |μ| < 1 for η ∈ [0.1, 400] (truncation K ≤ 20), so 2m·χ_m(η) decays exponentially beyond m_*(η) [N]; a proof would follow from Ruelle–Pollicott theory for analytic Anosov maps (sketched in phase 4, and certified there on a compact η-range) [ref23-fix]. m_*(η) ≈ 5333/η² holds for η ≲ 25; in general m_* = log 2/(−log μ(η)).
   - Below that scale the fixed-η value is ≈ 4m (exact parity doubling), not 2m. This is the dominant term of W at moderate η (χ_m ∈ [0.82, 0.995] for 2 ≤ η ≤ 10, m ≤ 11 [ref23-fix]). **So "W_m = o(m) uniformly at fixed η" is false in the pre-asymptotic sense, and true only beyond m_*(η).**
3. **W̃^rest is not proved to be o(m) [open; C + strong N].**
   - Numerically, for η ≥ 10, |W̃^rest|/2m ≤ 0.11 (m = 7), ≤ 0.05 (m = 9; −0.05 at η = 400) [ref8-fix], ≤ 0.018 (m = 11; −0.0175 at η = 400) [lineB-final fix], and ≤ 0.008 (m = 13; h² = 2.2·10⁹ points, η = 10, 25, 50).
   - Two further obstructions were proposed: small-η pre-mixing, and torsion at small prime factors of a composite h_m (m = 11: F/2m = 5.56 at η = 2 and M4 = 15.9 at η = 5). [ref23-fix/phase 4] The exact torsion-class split of phase 4 shows that the η = 2 excess is *not* carried by the 23-torsion classes; the torsion attribution is withdrawn and the outlier is unexplained.
   - The generic remainder is equivalent (by Parseval) to an ℓ²-collision bound for a pushforward measure (§4); this is not covered by known large-sieve inequalities, and I could not prove it [ref23-fix].
4. **Primality [Cert].** h_m is certified prime by ECPP for m = 59, 163, 257, 421, 937, 947, 1493 (up to 572 digits). Theorem N (phase 2) is therefore fully unconditional for all eleven listed m (admissibility is automatic for prime h_m; the bound is nontrivial from m = 29) [ref23-fix]. Primality is deterministic for m ≤ 47.
5. **Fixed-η CLT [N only].** At m = 11 (7744 values of ν) and η ≥ 10: M4 = 1.94–2.00, M6 = 5.5–6.2, KS = 0.006–0.013, below the heuristic 5% yardstick 0.0155. At small η the law is far from Gaussian (M4 = 15.9 at (11,5), 1556 at (11,2), 6.1 at (9,2)) [ref23-fix].

## 1. Exact norm-class formula for the fixed-η second moment [P, N-validated]

**Proposition C.** For odd m, write h = h_m, q(x) = x₀² − 6x₀x₁ + x₁² mod h, and A_r(η) = Σ_{x: q(x)=r} e^{iηS(½+x/h)}. Then

  F_m(η) = E_ν|Z_m(ν)|² = h⁻² Σ_{r,r′∈Z/h} A_r Ā_{r′} μ(q_{rr′})/φ(q_{rr′}),  q_{rr′} = h/gcd(r − r′, h).

*Proof.*
- By Prop K, k_ν(ξ)·conj k_ν(ξ′) = e(ν̄t)/D_eff with t = 𝒬*(ξ) − 𝒬*(ξ′), where 𝒬* is the dual quadratic form on 𝒮.
- 𝒬* is Γ-invariant, in particular invariant under (x₀,x₁) ↦ (x₁, 6x₁ − x₀) [L: `P1_form_invariant`].
- [ref23-fix] V = V_2 ⊕ V_odd is 𝒬- and ⟨·,·⟩-orthogonal, so k_ν(½𝟙+x) = k^{(2)}_ν·k^{odd}_ν(x). k^{odd}_ν is a Gauss sum of a quadratic form nondegenerate on V_odd (Rad = V[4]), hence equals (ε_ν/h)·e(ν̄𝒬^∨(x)) with 𝒬^∨ the dual form mod h. 𝒬^∨ is λ-invariant; over Z/p^e the λ-invariant binary forms are a free rank-1 module spanned by the norm form (μ² − 1 is a unit: Nm(λ² − 1) = −32). So 𝒬^∨ = c·q/h with c a unit, for every odd m including p² | h.
- Averaging e(ν̄c(r − r′)/h) over units ν mod 2h gives the Ramanujan sum c_h(r − r′)/φ(h) = μ(q)/φ(q). ∎

*Check:* the values agree to all printed digits with the phase-2 FFT/`Orbits` computation for m = 5, 7, 9 (logs/W_scan.log vs fast_classes.py output). The class formula reduces the cost from D log D to m·h², which makes m = 11 (h² = 6.6·10⁷) and m = 13 (h² = 2.2·10⁹) feasible.

*Self-duality [P].* Expand Φ in characters. Then A_r = Σ_s B_s Kl_T(rs) + (s = 0 terms), with B_s = Σ_{n: Nm α_n ≡ s} Ĝ(n), and Kl_T(u) = Σ_{Nm y = u} e(Tr y/h) is a (norm-torus) Kloosterman sum. The Gauss-sum evaluation Σ_y e((aNm y + Tr y)/h) = ±h·e(−ā/h) gives the orthogonality

  Σ_r Kl_T(rs) conj Kl_T(rs′) = h(h·[s = s′] − 1)   for s, s′ ∈ (Z/h)^×, h prime [ref23-fix].

So the ξ-side class sums and the n-side Pell-norm classes give the same F. Weil's bound |Kl_T| ≤ 2√h alone gives only |W| ≤ 4(s0^m − |ĝ(0)|^m)², which is useless for large m.

## 2. Parity decomposition [P]

**Lemma P.**
- (i) k_ν(−ξ) = k_ν(ξ), because 𝒬 is even (substitute β → −β). Also −𝒮 = 𝒮, because −½ ≡ ½.
- (ii) For odd m, x ↦ −x is not in Γ. If −x = λ^k x for all x, then λ^k ≡ −1 (mod h), so λ^{2k} ≡ 1, so m | k, which forces 1 ≡ −1; impossible for h odd [L: `P4_m7` for m = 7]. The same argument excludes −x = λ^kσ(x) for all x.
- (iii) The points with a nontrivial stabiliser, or with −x ∈ Γx, number at most 2mh + Σ_{d|m,d<m} φ(m/d)h_d² (= 2mh − 2m + 1 for prime m) [ref23-fix]. (Lemma P(ii) uses ord_h(λ) = m, true also for composite h.)

**Theorem W (decomposition).** For odd m and every η,

  F_m(η) = B^sym_m + W^par_m(η) + W^rest_m(η),
  W^par_m = D_eff⁻¹ Σ_{ξ∈𝒮, −ξ∉Γξ} |Γξ| Φ(ξ)Φ̄(−ξ) = 2m·χ_m(η) + E,  |E| ≤ 4m²/h_m,
  χ_m(η) = h⁻² Σ_{x∈V^_odd} exp(iη[S(½+x/h) − S(½−x/h)]).

B^sym = 2m − (Theorem D deficit) ≈ 2m − m²/h_m. **Define W̃^rest := F − B^sym − 2mχ_m = W^rest + E; all tables below report W̃^rest/2m** [ref23-fix]. W^rest collects all other non-Γ pairs, which lie in the same norm class with Ramanujan weight 1, or in different classes with weight μ(q)/φ(q). *Proof:* group the pairs in Prop C by ξ′ ∈ Γξ, ξ′ ∈ Γ(−ξ), or otherwise, and use Lemma P. ∎

## 3. The parity characteristic function: exact transfer operator [P] and spectrum [N]

On the support, S(½+x) − S(½−x) = Σ_j u(ξ_j), where u(θ) = f(θ) − f(−θ) = 2f_odd(θ) (only sine-type coefficients, c_k − c_{−k}).

**Theorem T.** For odd m,

  χ_m(η) = Σ_{a=0}^{3} (−1)^a Tr(M_a(η)^m),  M_a[(p,q),(q,r)] = ŵ_η(6q − p − r + a),

where ŵ_η are the Fourier coefficients of e^{iηu}, and the states (p,q) range over Z². The series converges absolutely, and truncating to |p|,|q| ≤ K is exact up to m·‖ŵ‖₁^{m−1}·Σ_{|n−a|>4K}|ŵ(n)| [ref23-fix].

*Proof.*
- χ_m is the average of the product function ⊗_j e^{iηu} over the coset 𝒮 of the annihilator of V_2 = ⟨𝟙⟩.
- Poisson summation on V^ turns this into the sum of its Fourier coefficients over the dual lattice HZ^m + Z𝟙, twisted by the character e(⟨n, ½𝟙⟩) = (−1)^{Σn_j}.
- Since H𝟙 = 4𝟙 [L: `P3_H_ones`], each dual vector is uniquely n = Hk + a𝟙 with k ∈ Z^m and a ∈ {0,1,2,3}. Then Σ_j n_j = 4Σk + am [L: `P3_sum`], and (−1)^{am} = (−1)^a for odd m.
- (Hk)_j = 6k_j − k_{j−1} − k_{j+1} is nearest-neighbour, so the cyclic sum over k is a trace of the m-th power of M_a.
- If max|k| > K, then max|n − a| ≥ 4K, since H⁻¹ has row sums ¼. ∎

*Validation* (logs/parity_transfer.log, W_decomp.log): transfer trace vs direct sum over the support for m = 3–11 and η ≤ 200 agree to |diff| ≤ 7·10⁻⁵ (at η = 400 the truncation K is insufficient: differences up to 1.1·10⁻²) [ref23-fix], and to ≤ 10⁻¹⁰ for η ≤ 10.

**Spectrum** [N; K = 8 → 12 and 14 → 20 stable to 6 digits]:

| η | max\|μ_a\| | ρ(\|M_a\|) | parity half-life log 2/(−log\|μ\|) |
|---|---|---|---|
| 1 | 0.999813 | 0.9998 | 3698 |
| 2 | 0.999251 | 0.9993 | 925 |
| 5 | 0.995345 | 0.9955 | 149 |
| 10 | 0.98177 | 0.9825 | 37.7 |
| 25 | 0.90034 | 0.909 | 6.6 |
| 50 | 0.73105 | 0.791 | 2.2 |
| 100 | 0.61995 | 0.949 | 1.4 |
| 200 | 0.5586 | 1.25 | 1.2 |
| 400 | 0.545 | 1.7 | 1.1 |

- For η ≤ 100 the positive majorant already has ρ(|M_a|) < 1. So |χ_m(η)| ≤ C_η ρ_+(η)^m, which is a rigorous route to exponential decay modulo a certified bound on the truncated spectral radius. That certification was not done here, so this is [N]. (It is done in phase 4 on a compact η-range, with a tilted majorant.) [ref23-fix]
- For larger η only the complex spectrum is < 1.

**Small-η law [P-sketch].**
- At η = 0, M_0 is the 0/1 matrix of the Pell map (p,q) ↦ (q, 6q − p). Its only periodic integer point is 0 [L: `P5_no_periodic`, for |p|,|q| ≤ 6 and period ≤ 12]. So 1 is a simple isolated eigenvalue, and the rest of the truncated spectrum is nilpotent.
- Analytic perturbation then gives μ(η) = 1 − ½η²σ² + O(η⁴). Here σ² = Σ_j Cov(u(ξ₀), u(ξ_j)) = ‖u‖₂² = 4‖f_odd‖², because the cross-correlations vanish: k·e₁ = k′·(T^T)^j e₁ has no solutions with 0 < |k|,|k′| ≤ 9 and j ≠ 0.
- 800²‖f_odd‖² = 60 [L: `P2_odd_norm`], so μ(η) ≈ exp(−1.875·10⁻⁴ η²). This matches the computed values: 0.9998125 vs 0.999813 at η = 1, and 0.995324 vs 0.995345 at η = 5.

**Corollary (fixed-η ramp, parity-resolved).**
- At fixed η ≠ 0, W^par_m(η)/2m = χ_m(η) → 0 exponentially in m [P for the identity; decay [N] here; numerically |μ| < 1 for η ∈ [0.1, 400]; a proof would follow from Ruelle–Pollicott theory for analytic Anosov maps — see phase 4] [ref23-fix].
- The crossover scale is m_*(η) = 1/(2‖f_odd‖²η²) ≈ 5333/η² for η ≲ 25 (−log μ/η² = 1.875·10⁻⁴ at η ≤ 10, 1% off at 25, wrong for η ≥ 50); in general m_* = log 2/(−log μ(η)), e.g. 2.2 at η = 50 [ref23-fix].
- For m ≪ m_*(η), F_m(η) ≈ 4m − W-corrections. This is the doubled value of a spectrum with an extra unitary symmetry (two independent parity sectors).
- So the "COE diagonal value 2m at fixed η" can hold only for m ≫ m_*(η). The correct comparison with the phase-2 window is m_*(η) > c(η)·log X; for X = 10^{160} this holds for η ≲ 9 [ref23-fix]. Phase 1 (REPORT.md §7, logs/crossover.log) had already observed this 4m → 2m crossover numerically at m = 7. What is new is the exact crossover function χ_m(η) and its rate. This is an exactly solvable instance of weak breaking of a classical (parity) symmetry, analogous to the semiclassical BGOS crossover (Bohigas–Giannoni–Ozorio de Almeida–Schmit 1995; Pandey–Mehta 1983 for RMT); it is not a Keating–Mezzadri pseudo-symmetry [ref23-fix].

## 4. The remainder W̃^rest [N; precise obstruction; C]

From logs/W_decomp.log and logs/W_decomp_m13.log (W̃^rest/2m = (F − B^sym − 2mχ)/2m [ref23-fix]; the m = 13, η = 25 entry is below the resolution |E|/2m ≤ 5.4·10⁻⁴; at m = 13 the transfer-operator χ agrees with the direct sum to 5 digits):

| η | m = 5 | m = 7 | m = 9 | m = 11 | m = 13 |
|---|---|---|---|---|---|
| 5 | −0.39 | +0.16 | −0.07 | +0.15 | — |
| 10 | −0.07 | −0.11 | −0.02 | +0.016 | **+0.008** |
| 25 | +0.02 | −0.09 | −0.04 | +0.005 | **+0.0006** |
| 50 | −0.01 | −0.04 | −0.03 | +0.009 | **+0.0075** |
| 100 | −0.16 | −0.09 | +0.04 | +0.016 | — |
| 400 | −0.36 | +0.02 | −0.05 | −0.018 | — |

The trend in m is toward 0 for η ≥ 10. Two regimes are identified ((a) pre-mixing, (c) the generic part); a third mechanism (b) was proposed and is withdrawn [ref8-fix]:

- **(a) Pre-mixing at small η.** W̃^rest/2m ≈ −1.2 to −1.6 at η = 0.5 for all m. Φ is almost constant on classes, and F → O(1) as η → 0, since F(0) is the class-size variance. The scale is η√m·‖f‖ ≲ 1.
- **(b) Torsion of composite h_m.** At m = 11, h = 23·353, and η = 2:
  - F/2m = 5.56;
  - (1/h²)Σ|A_r|² over Ramanujan level q = 1 contributes 118.7 of F = 122.4;
  - the dominant classes have r ≡ 0 mod 23, i.e. x mod 23 on the isotropic (eigen)lines of λ mod 23, with coherent |A_r| ≈ 3500 against a random value ≈ 590 (logs/diag_q_m11.log).

  Phase 3 proposed this as the second-moment shadow of the phase-2 torsion obstruction; phase 4 withdraws that explanation (below) [ref8-fix]. The descriptive fact stands: the largest |A_r| at (11, η = 2) all have r ≡ 0 mod 23; these classes carry 13.7% of Σ|A_r|² against a point share of 8.5% (referee t12). **[ref23-fix / phase 4] Withdrawn as an explanation of the η = 2 outlier: the exact split F = F_gen + F_tor (phase4/REPORT4.md §2.3) leaves a normalised excess +3.25 in the non-torsion classes; the torsion classes hold only 0.77·2m of F = 5.56·2m.**
- **(c) Generic part: the open core.** By §1, W^rest = Σ_{s} |B_s|² − (Γ- and parity-diagonal), with B_s = Σ_{n∈Z^m: Nm(α_n) ≡ s (h)} Ĝ(n) and Ĝ = ⊗ĝ (complex weights with |Ĝ|² a probability product measure). W̃^rest = o(m) is equivalent (by Parseval) to an ℓ²-collision bound for the pushforward measure; this is not covered by known large-sieve inequalities (Baier–Zhao and successors treat many moduli and one variable) [ref23-fix]:
  - the pushforward of the complex product measure Ĝ under the Pell-norm quadratic form n ↦ 2nᵀH⁻¹n mod 1 has ℓ²-collision mass (2 + o(1))·m (the Γ ⋊ {±1} multiplicity) at fixed η as m → ∞;
  - its effective support (s0(η)^{2m} points) vastly exceeds the modulus h ≈ λ^{m/2}/2;
  - Weil (|Kl| ≤ 2√h) handles only one Fourier mode at a time, and the needed cancellation is among the ~s0^{2m} modes, i.e. exactly the off-diagonal Pell-norm coincidences.

  Minimal-period caution [ref23-fix]: h_m has ord_h λ = m ≈ 2 log h/log λ, the Faure–Nonnenmacher–De Bièvre (scarring) regime, where Kurlberg–Rudnick, Bourgain and Bourgain–Glibichuk–Konyagin sum-product bounds (which need ord > N^{1/2} or |⟨λ⟩| ≥ h^δ) do not apply.

  Mixing / decay of correlations for the toral automorphism (the transfer-operator route that solved §3) does not apply directly: the pair (x, tx) with t ∈ T∖±⟨λ⟩ is not a dynamical pair, and the multiplier t has no small lift.

**Conjecture R [C] [ref23-fix].** For every 0 < η₀ ≤ η₁ < ∞, max_{η∈[η₀,η₁]} |W̃^rest_m(η)| = o(m) as m → ∞ through odd m. (Version R_NSW: along m with h_m prime — a sequence not known to be infinite; admissibility is automatic.) The former torsion-removal clause is dropped: phase 4 shows the torsion classes carry no excess at η ≥ 10 and are not the cause of the small-η outlier.

## 5. Fixed-η distribution of Z_m(ν) [N]

|Z(ν)|² = h⁻²|Σ_r A_r e(ur/h)|², with u = c·ν⁻¹ uniform over units mod h (logs/fixed_eta_dist.log). For m = 9 this matches phase-2 exactly.

| | M4 | M6 | \|E Z²\|/F | KS | 5% yardstick (heuristic) |
|---|---|---|---|---|---|
| m = 11, η ∈ {10, 25, 50, 100, 200, 400} | 1.936–2.004 | 5.51–6.15 | ≤ 0.03 | 0.006–0.013 | 0.0155 |
| m = 11, η = 5 | 15.9 | — | — | — | — |

Gaussian targets are M4 = 2, M6 = 6, |E Z²|/F = 0. At small η the law is far from Gaussian [ref23-fix]: M4 = 6.1 at (m, η) = (9, 2); M4 = 1556, KS = 0.40 at (11, 2); KS = 0.040 above the yardstick at (11, 0.5); M4 = 15.9 at (11, 5) (a few ν with coherent class sums; the torsion attribution is withdrawn, phase 4). The "5% critical value" treats the φ(h) values of ν as i.i.d. samples, but they are a deterministic population, so it is only a heuristic yardstick. A fixed-η CLT is **not proved**. [H] With parity present, the Gaussian should have the doubled variance and stay complex circular (χ_m real; sectors heuristically independent in the limit).

## 6. Primality certificates [Cert]
code/ecpp_certs.py uses cypari2 2.2.4 (PARI 2.17.2): `primecert` (ECPP), then an independent `primecertisvalid` = 1. Certificates are saved in logs/cert_h{m}.txt.

| m | digits | steps | time |
|---|---|---|---|
| 59 | 23 | 1 | |
| 163 | 63 | 6 | |
| 257 | 99 | 10 | |
| 421 | 161 | 21 | |
| 937 | 359 | 48 | |
| 947 | 363 | 45 | |
| 1493 | 572 | 74 | 16 s, verified in 1.3 s |

Phase-2 Theorem N is now unconditional for m ∈ {7, 19, 29, 47, 59, 163, 257, 421, 937, 947, 1493}. The certificates are not re-checked in Lean.

## 7. Lean [L]
phase3/lean/Phase3Checks.lean is built in phase3/build (own `cp -a` copy; `lake exe cache get` reported "No files to download"; Mathlib not built from source). Axioms are at most [propext, Quot.sound] (logs/lean_phase3.log).
- `P1_form_invariant` (ring): q(x₀,x₁) is invariant under the q-sequence step.
- `P2_odd_norm`: 800²‖f_odd‖² = 60.
- `P3_H_ones` and `P3_sum`: the parity-lattice facts.
- `P4_m7`: −1 ∉ ⟨λ⟩ mod 239.
- `P5_no_periodic`: the η = 0 transfer map has no nonzero periodic points in the box.

## 8. Reproduce
P=/workspace/bgs-derand/phase3/venv/bin/python (own venv: numpy, sympy, mpmath, cypari2; the earlier /workspace/bgs-p1b/venv disappeared in a box restore at ~20:18); cd phase3/code, then run:
- `$P W_scan.py 3,4,5,6,7,8,9`
- `$P parity_split.py 3,5,7,9 <etas>`
- `$P parity_transfer_run.py`
- `$P W_decomp.py 3,5,7,9,11 <etas>`
- `$P W_decomp.py 13 5,10,25,50,100` (~0.5–1 h)
- `$P diag_q.py 11 2,5,25`
- `$P fixed_eta_dist.py 9,11 <etas>`
- `$P ecpp_certs.py 59,163,257,421,937,947,1493`

## 9. Literature for this phase
- Keating–Mezzadri 2000 (pseudo-symmetries; kept only for the arithmetic-symmetry discussion — §3 is NOT a KM pseudo-symmetry) [ref23-fix].
- Bohigas–Giannoni–Ozorio de Almeida–Schmit, Nonlinearity 8 (1995) 203; Pandey–Mehta 1983 (symmetry-breaking crossover; §3 is the derandomized analogue) [ref23-fix].
- Faure–Nonnenmacher–De Bièvre, CMP 239 (2003) 449 (scars at minimal period); Kurlberg–Rudnick 2000/2001; Bourgain, LNM 1910 (2007); Bourgain–Glibichuk–Konyagin 2006; Faure–Roy, Nonlinearity 2006; Rugh 1992 [ref23-fix].
- Keating 1991 (cat-map trace formula; parity and arithmetic degeneracies).
- Keppeler–Marklof–Mezzadri 2001 (diagonal approximation for perturbed cat maps).
- Bogomolny–Keating 1996 (off-diagonal action correlations). W^rest is the derandomized analogue.
- Weil / Kloosterman bounds (§1).
- The GOE-with-parity doubling is classical; what is new here is the exact transfer-operator crossover for this kick.
