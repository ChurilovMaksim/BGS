# Line G: a general resonance law for the fixed-kick cat map, dilution families, and a corrected conjecture R′

**Claims:** BGS-TRACE-203 to BGS-TRACE-206. **Cross-referenced (states unchanged):** BGS-TRACE-179 (open at that date; refuted as stated by Line H), BGS-TRACE-183, 184, 193, 194, 196.

**Later work (Line H, 30 October 2026).** For the Line B kick f_B at η = 2, BGS-TRACE-209 (computer-assisted, refereed) gives W̃rest_m(2)/m ≥ 1.4·10⁴ for every odd m ≥ 47 with 3 ∤ m, on the lifted space of BGS-TRACE-197 ([lineH_49state_certificate.md](lineH_49state_certificate.md)). Conjecture R (BGS-TRACE-179) as stated is therefore refuted (registered state `refuted`; R_NSW undecided). BGS-TRACE-196 stays conditional as stated; its conclusion for s = −1 holds on the lifted space. Statements below that R is not disproved describe the state before Line H.

**Inputs** (cited, not re-claimed): BGS-TRACE-183 (E1; in particular the exact form P(n) = Σ_{i,j} ψ(|i−j|) n_i n_j of the quadratic form, Line E proof step 2), BGS-TRACE-184 (E2), BGS-TRACE-193 (E11, Galois scaling for the pure 7-mode kick), BGS-TRACE-194 (E12, the a²-resonance law), BGS-TRACE-195 (Prop. G, class-sum representation), BGS-TRACE-165 and 170 (the split F = B^sym + 2mχ + W̃rest).

**Review state.** Written by the Line G author (`computations/verification/lineG/AUTHOR_REPORT.md`) and audited by an independent referee (`computations/verification/lineFG/referee/REPORT.md`, Part G). The referee verified G2 with own code (`referee/code/g_law.py`) and found one substantive overclaim about Conjecture R and an inconsistent definition of R′; both are fixed below. Fixes are marked **[RG1]**–**[RG5]**, nits **[RGn]**.

**Labels.** **[P]** proved here; **[P-sketch]** proof sketch only; **[Lean]** algebraic core kernel-checked in `formalization/Bgs/LineG.lean`; **[N]** floating-point numerics or exact class sums in IEEE double; **[H]** heuristic; **[C]** conjecture. Nothing in Line G is an interval-arithmetic certificate.

## 0. Setting and summary

S = [[3,4],[2,3]], λ = 3 + 2√2, odd m, h = h_m (the NSW numbers 1, 7, 41, 239, 1393, 8119, 47321, 275807, 1607521). Z_m(ν) = Σ_n Φ̂(n) e(−νP(n)/(2h)), P(n) = Σ_{i,j} ψ(|i−j|) n_i n_j (exact, TRACE-183), F_m = (1/φ(2h)) Σ_{ν∈(Z/2h)^×} |Z_m(ν)|². Two kicks at η = 2: **k1** (ĝ(n) = iⁿJ_n(0.9η)) and the Line B kick **f_B** ("full").

1. **Classification of outliers [RG2].** Every outlier ν (|Z(ν)|² ≫ 2m) found at m = 7…15, for both kicks, is explained *numerically* by one of three mechanisms, within the stated main-term tolerances (0.1–15 % for dominant families, up to 37 % at d = 287):
   * the partial-trace law G2 (proved, finite alphabet): primaries are short vectors (a, b) of the lattice {bν ≡ a mod 2h}; the dominant ones are N ≡ ±4 (Line E's E1) and N ≡ ±8;
   * the dilution identity G3 (an identity checked to 2.8e-14, but with a proof sketch only, and without a rigorous bound on the β ≠ 0 terms): secondary families along the divisors d | h;
   * Galois scaling G4 (= TRACE-193): for f_B, the families N ≡ ±196, ±392, ±98 sit at the 49× images of ±4, ±8, ±2.
2. **Sparsity (G6)** and the **moment heuristic (G7, [H])**: a family with |Z| ≍ r^m matters for the k-th moment of |Z|² roughly iff r > λ^{1/(4k)} (for the mean: λ^{1/4} = 1.5538). Numerically only N ≡ ±4 (r = 1.9154732) and N ≡ ±8 (r ≈ 1.615) exceed λ^{1/4} among the families tested.
3. **Conjecture R′ [C] [RG3]** (k1, η = 2), with a single frozen definition (§3): F_m = 4m + Res_m + o(m), where Res_m is an explicit sum over the primaries N ≡ ±4, ±8 and their dilution levels. Evidence is four points m = 9…15 with an upward drift; o(m) is **not** established by the data.
4. **What this says about Conjecture R (TRACE-179) [RG1].** Nothing new. R is the statement max_η |W̃rest_m(η)| = o(m), not F/2m → 2. For **k1**, asymptotic failure of the k1-kick analogue of R is established only by Line F (BGS-TRACE-199, computer-assisted); Line E had it conditionally (TRACE-188) or on a finite range (TRACE-187). For the **Line B kick f_B** it is only conditional on H∞,7 (TRACE-196), with |W̃rest_m| > m certified at m = 11 and 13 only (TRACE-195). **R is not disproved.** R′ is a proposed corrected statement for k1; it is not a statement about R.

## 1. Theorems

### G1 (phase split) [P] [Lean `Bgs.LineG.phase_split`]
Let bν = a + 2hk with a, b, k ∈ Z, b ≠ 0. Then for every integer P with P = 4hq: −νP/(2h) ≡ −(2a/b)q − kP/b (mod 1).
*Proof.* −νP/(2h) = −(a + 2hk)P/(2hb) = −aP/(2hb) − kP/b and aP/(2hb) = 2aq/b. ∎

### G1′ (automaton for P mod b) [P] [Lean `u_succ`, `w_succ`, `quad_form`]
With ψ₀ = ψ(0) = y′ and ψ₁ = ψ(1) = 3y′ − 2h, P is accumulated along the word by the linear automaton (u, w) ↦ (6u − w + nψ₁, u + nψ₀) with step contribution ψ₀n² + 2nu (mod b). This is exact because P(n) = Σ_{i,j} ψ(|i−j|) n_i n_j with ψ(d) = y′x_d − 2h·y_d for d < m (TRACE-183, Line E proof step 2; re-checked by the referee for m = 5, 7) **[RG4]**. Lean proves the one-step recursions and the quadratic-form identity Σ_{i,j<m} ψ(|i−j|) n_i n_j = ψ(0) Σ n_j² + 2 Σ_j n_j u_j for any ψ with ψ(d+2) = 6ψ(d+1) − ψ(d).

### G2 (partial-trace transfer law, finite alphabet; BGS-TRACE-203) [P]
Fix (a, b), coef := −4ac/b with c = 1/(4√2), supp ĝ ⊂ [−L, L], ρ > L/(λ − 1). On H²(D_ρ) let R_n φ(s) = e(coef(n²/2 + ns)) φ((s + n)/λ), and on C^{b²} let A_n be the automaton step with phase e(−k(ψ₀n² + 2nu)/b). With 𝓛 = Σ_n ĝ(n) R_n ⊗ A_n:

  Z_m(ν) = (1 − λ^{−m}) Tr_H[(I ⊗ ⟨𝟙|) 𝓛^m (I ⊗ |δ₀⟩)].

*Proof.* Expand 𝓛^m over words. The C^{b²} factor gives ⟨𝟙|A_w|δ₀⟩ = e(−kP(n)/b) by G1′. R_w is a single weighted composition operator with symbol of derivative λ^{−m} and unique fixed point s*(w) (the periodic orbit), so Tr R_w = e(−(2a/b)q(n))/(1 − λ^{−m}) by the Ruelle / Bandtlow–Jenkinson formula, using q = 2c[Σ n_j s_j + ½Σ n_j²]. The composition order reverses the word; P and q are reversal-invariant. Summing with Π ĝ(n_j) and using G1 gives the claim. ∎

*m-dependence* **[RG4]**. 𝓛 depends on m only through (k, y′, h) mod b, which are periodic in m. On each residue class of m mod that period, Z_m(ν_{a,b}) = (1 − λ^{−m}) Σ_μ c_μ μ^m is an exponential **sum** over the (in general infinitely many) eigenvalues μ of a fixed trace-class operator; its leading |μ| is the growth rate r of the family. For k1 the alphabet is infinite: a rigorous infinite-alphabet version needs a Line-F-type lift (BGS-TRACE-197) of the C^{b²}-extended operator, which is **not done**; Galerkin truncations below are numerical.

*Checks [N].* Author: 34/34 well-conditioned cases agree with brute-force word sums to 1e-14 … 1e-9 (`computations/verification/lineG/logs/check_law.log`); large-coupling representatives overflow in the Galerkin step (numerical conditioning, not a failure of the identity). Referee, own code (`computations/verification/lineFG/referee/code/g_law.py`, `logs/g_law.log`): random complex weights, |n| ≤ 2, m = 5 and 7, brute force over all units: agreement ≤ 1.3e-14 for every tested (a, b) with |a|/b ≤ 1.

### G3 (dilution identity; BGS-TRACE-204) [P-sketch] [N]
Let d | h be odd, t = j·y′ (mod d) with gcd(t, d) = 1, and G_d(t) the quadratic Gauss sum, |G_d(t)| = d **[RGn]** (odd d is needed because the discriminant of x² − 2y² is 8). Writing n ↦ α_n ∈ O = Z[√2] (P(n) ≡ y′·Nm(α_n) mod h on the relevant lattice) and splitting α_n mod d,
  Z(ν₀ + 2hj/d) = (G_d(t)/d²) Σ_{β∈O/d} e(t̄·Nm(β)/d) Z^{(β)}_{ν₀},
where Z^{(β)} is the same sum with the kick at site i translated by Tr(βλ^i)/d.
*Proof sketch.* Finite Fourier analysis on O/d: insert the indicator of α_n ≡ β (mod d) as an average of additive characters and complete the square in e(jP/d) = e(t·Nm(α_n)/d); the β = 0 term gives the main term (G_d/d²) Z_{ν₀}. A full written proof is **not** given.
*Checks [N].* `code/check_dilution.py` is a genuine brute-force-versus-formula test: 49 cases, maximal relative error 2.8e-14 (`logs/check_dilution.log`), but only for **prime** d (7 at m = 9, 41 at m = 5) and alphabets |n| ≤ 1, 2. Composite d (e.g. 217 at m = 15, used in §2) is untested. The main term |Z|² ≈ |Z_ρ|²/d² is good to 0.1–2 % for d = 7, 31 at m = 15, 1–4 % for d = 23, 79, 15 % for d = 41 and 37 % for d = 287 (`logs/dil_stats.log`); the size of the β ≠ 0 terms is not bounded rigorously.
**State: open** until a full proof is written (ideally with a composite-d check).

### G4 (Galois scaling) — no new claim
If ĝ(n) = 0 unless a | n, then Z_g(ν) = Z_{g_a}(a²ν). This is BGS-TRACE-193. For f_B (dominated by its frequency-7 harmonic, but not exactly 7-periodic) the families N ≡ ±196, ±392, ±98 are located at the predicted 49× images of ±4, ±8, ±2 at m = 11, 13 (`logs/tier2full.log`); their sizes are not exact images. When 7 | h (3 | m) the image is not a unit residue and the mass appears as a level-7 dilution family, which is why the f_B value of F/2m is small at m = 9, 15 (1.82, 3.91) and large at m = 11, 13.

### G5 (divisibility) [P] [Lean `nsw_dvd`, `nsw_17`] — lemma inside BGS-TRACE-205
For odd m and d | m, h_d | h_m (Re-divisibility in Z[√2], `re_dvd_pow`). This is the classical divisibility-sequence property (low novelty). Lean also proves nsw 3 = 7, nsw 5 = 41, nsw 7 = 239, **nsw 17 = 1607521** **[RGn]**, 1607521 = 103·15607 and 1607521² + 1 = 2·1136689².

### G6 (sparsity) [P] — lemma inside BGS-TRACE-205
Each pair (ρ, d) contributes at most d residues (one coset of 2h/d, two signs), so |𝓡| ≤ 2|𝓟|·Σ_{d|h, d≤D} d ≤ 2|𝓟| τ(h) D. For a fixed finite primary list 𝓟 this is a counting statement (the referee calls it tautological); with D = √h and τ(h) = h^{o(1)}, |𝓡|/φ(2h) ≤ h^{−1/2+o(1)}.

### G7 (moment hierarchy) [H] — inside BGS-TRACE-205 **[RG4]**
*Heuristic.* If a single family has |Z_ρ| ≍ r^m and O(h^{o(1)}) members at level d = 1, its contribution to the k-th moment of |Z|², (1/φ) Σ_ν |Z|^{2k} **[RGn]**, is ≍ r^{2km}/h, with h ≍ λ^{m/2}; so it is asymptotically relevant iff r > λ^{1/(4k)} (k = 1: λ^{1/4} = 1.5538); dilution levels add a factor Σ_d d·d^{−2k} = O(1). The "iff" is not a theorem: "irrelevant" would also need control of all other families, and the growth rates, member counts and the bulk baseline are inputs, not proved.

## 2. Step 1: numerical map of the residue distribution (BGS-TRACE-205) [N]

Class sums by an orbit-canonical C code (`code/classes_orb.c`), validated against the independent Line E audit implementation to ≤ 3e-11 at m = 11, 13, 15, both kicks; |Z(ν)|² for all ν by one FFT. (The C sources are in the packet; the binaries and the large `.bin` class-sum tables are not committed; their sha256 are in `logs/bin_sha256.txt`.)

| m | k1 bulk F/2m | f_B bulk F/2m | k1 total F/2m | f_B total F/2m |
|---|---|---|---|---|
| 9 | 1.45 | 1.43 | 4.839 | 1.816 |
| 11 | 1.78 | 1.80 | 6.894 | 5.562 |
| 13 | 1.94 | 1.96 | 11.197 | 8.590 |
| 15 | 2.07 | 2.04 | 27.885 | 3.911 |

(The k1 totals agree with the Line E referee's class sums.) Largest k1 residues at m = 15: N ≡ ±4 (|Z|² = 7.349e7 each), ±8 (4.43e5), ±2 (8.8e4), and dilutions of ±4 at d ∈ {7, 31, 41, 217, 287}. Bulk second moment E[x²] (x = |Z|²/bulk mean; exponential statistics would give 2): 2.1, 2.7, 3.2, 3.2 for m = 9…15, with second-tier outliers up to x ≈ 135 at m = 15.

Growth rates of |Z| (G2 law, Galerkin; cross-checked against class sums where the Galerkin step is well conditioned, `logs/law_vs_class.log`, `logs/tune.log`, `logs/growth_law.log`):

| family (a, b) | N ≡ | r | above λ^{1/4}? |
|---|---|---|---|
| (±2, 8) | ±4 | 1.9154732 (law, m ≤ 29; matches the Line F float value) | yes |
| (±2, 16) | ±8 | ≈ 1.615 | yes |
| (±2, 4) | ±2 | ≈ 1.50 | no (barely) |
| (±6, 16) | ±8/3 | ≈ 1.37 | no |
| (±22, 96), (±2, 12), (4, 18) | – | 1.33–1.41 | no |

Only r(±4) is independently checked (the referee's full-alphabet float value 1.9154732041; Line F's certified enclosure [1.9154712, 1.9154753] for the full alphabet). The other rates are float/Galerkin only. `law_vs_class.log` also shows parameter choices for which the Galerkin step overflows (e.g. m = 9, (±2, 8)); these are numerical failures of the truncation, not of the identity.

**Moments [RG4].** Under G7 with k = 2 the threshold is λ^{1/8} = 1.247 < 1.33–1.41, so a CLT-type statement for the bulk in moment form is **expected to fail [N]**; any proof of R′ should be a first-moment statement.

**η-scan [N]** (k1; bulk = outside the dilution families of the primaries and height ≤ 32; `code/eta_scan.py`, `logs/eta_scan.log`):

| bulk F/2m | η = 0.5 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| m = 9 | 0.63 | 1.35 | 1.49 | 1.64 | 1.75 |
| m = 11 | 0.76 | 1.61 | 1.74 | 1.87 | 1.90 |
| m = 13 | 0.86 | 1.83 | 1.92 | 1.93 | 1.97 |

(m = 9 removes 47 % of residues at height ≤ 32, so its row is only indicative; m = 11: 10 %, m = 13: 2.7 %.) The bulk rises with m towards ≈ 2 at every η, faster for stronger kicks: a coupling-dependent finite-m crossover, not a kick-universal term.

## 3. Conjecture R′ (BGS-TRACE-206) [C] — frozen definition [RG3]

The author's report gave two different formulas (§0 without, §3 with a per-member subtraction). The definition below is the single frozen one. It is the one implemented in `computations/verification/lineG/code/formula_table.py` (the code that produced the evidence table), and it is frozen in this commit, before any m = 17 class sum exists.

**Definitions** (k1 kick, η = 2; odd m; h = h_m; U = (Z/2h)^×; φ = φ(2h) = |U|):
- 𝓟* = {(2, 8), (−2, 8), (2, 16), (−2, 16)} (N ≡ ±4, ±8).
- For ρ = (a, b) ∈ 𝓟*, ν_ρ is the unit with bν_ρ ≡ a (mod 2h), and Z_ρ := Z_m(ν_ρ).
- For d | h with 1 < d ≤ √h: M_d(ρ) = {ν ∈ U : bν ≡ a (mod 2h/d), and bν ≢ a (mod 2h/d′) for every divisor d′ of d with d′ < d}; n_d(ρ) = |M_d(ρ)|.
- Cut-off: level d of ρ is *included* iff |Z_ρ|²/d² ≥ 4m.
- RMT_m := 4m − m²/h (the leading term 2m − m²/h of B^sym_m from TRACE-165, plus 2m for χ_m = 1).
- Res_m := (1/φ) Σ_{ρ∈𝓟*} [ (|Z_ρ|² − RMT_m) + Σ_{d included} n_d(ρ) (|Z_ρ|²/d² − RMT_m) ] (members of different families are counted with multiplicity, as implemented).
- W′_m := F_m − RMT_m − Res_m.

**Conjecture R′.** For the k1 kick at η = 2, W′_m = o(m) as m → ∞ through odd m; equivalently (F_m − Res_m)/2m → 2.

Res_m is explicit: each |Z_ρ|² is given by G2 (an m-independent operator on each residue class of m), and grows like (r_ρ²/λ^{1/2})^m/m relative to 2m for r_{±4} = 1.9154732 > λ^{1/4}.

**Evidence [N]** (`logs/formula_table_k1.log`; "pred" = the definition above; "act" replaces the dilution main term by the true members):

| m | F/2m | RMT/2m | Res/2m (pred) | Res/2m (act) | W′/m (pred) | W′/m (act) | #resonant residues |
|---|---|---|---|---|---|---|---|
| 9 | 4.839 | 1.997 | 3.212 | 3.252 | −0.74 | −0.82 | 14 |
| 11 | 6.894 | 1.999 | 5.050 | 5.052 | −0.31 | −0.31 | 46 |
| 13 | 11.197 | 2.000 | 9.214 | 9.217 | −0.04 | −0.04 | 158 |
| 15 | 27.885 | 2.000 | 25.651 | 25.770 | +0.47 | +0.23 | 990 |

**Honest caveats (referee G.1).** Four points; W′/m drifts upward (≈ +0.50 per Δm = 2 at the last step under the frozen definition, ≈ +0.27 for "act"); o(m) is not established by the data. The f_B analogue (W′_act/m = −1.11, −0.33, −0.03, +0.14) is recorded only as data, because for 3 | m its primaries are not unit residues and the implementation substitutes the measured excess of level-7 families; R′ is stated for k1 only.

**Pre-registered m = 17 test.** `computations/verification/lineG/PREDICTIONS_m17.json` with sha256 `fa8505f503790ae2c6265f917debdd4b023b2c50b79412daac7d14f72b8aa344` (`PREDICTIONS_m17.sha256`; the referee verified the hash and that the file predates any m = 17 output; the timestamp is self-attested, and this commit is its first external record). It registers, for k1 at m = 17 (h = 1607521 = 103·15607, φ(2h) = 1591812): the primaries ±4, ±8 to 1e-5 and ±2, ±8/3 to 1e-3 (G2 law); the d = 103 dilution mean 9.33e4 ∈ [7.5e4, 1.17e5]; second-tier values; the bulk F/2m (height-8 definition) 2.04 ∈ [1.95, 2.15]; and the total F/2m 39.1 ∈ [38.7, 39.5]; plus f_B items. The evaluator is `code/eval17.py`. The bulk statistic of the pre-registration is a proxy, not identical to W′_m above; W′_17 under the frozen definition will be computed by `code/formula_table.py k1 17` (code committed here). **Outcome: not part of this PR.** The k1 evaluation at m = 17 finished during integration, after the referee audit; it has not been reviewed and is neither included nor used here (the full-kick m = 17 class sums were still running at commit time). Nothing is claimed at m = 17.

## 4. Why R′ is not proved (BGS-TRACE-206 boundary)

- *Large sieve / Kloosterman over ν.* Σ_ν |Z|² unfolds to a count of pairs (n, n′) with P(n) ≡ P(n′) mod h; the large sieve gives Σ_ν |Z|² ≤ (h + N_eff) Σ|Φ̂|², useless because N_eff ~ e^{cm} ≫ h. The arithmetic reduces to equidistribution of the cyclic orbit {λ^i} (order m) in O/h, a group far too small (m ≍ log h) for Weil/Kloosterman bounds or current sum-product expansion.
- *Spectral route.* G2 gives each fixed (a, b) exactly, but the bulk is a sum over ≍ h different (a, b) with b up to √h; uniformity of the spectral gap in b is missing.

## 5. Relation to Line E and Line F

- G1/G2 generalise TRACE-183/184 (b = 8) to arbitrary lattice vectors (a, b); TRACE-194 (E12) is the case b = 8a² with a odd. The m = 15 values for N ≡ ±4 agree with TRACE-189 (7.34867e7 and 7.34915e7).
- G4 is TRACE-193. G5 generalises TRACE-193's Lean lemma (7 | h_m ⇔ 3 | m).
- The class-sum representation is TRACE-195's Prop. G.
- Line F (BGS-TRACE-197–199) supplies the full-alphabet lift for b = 8; the general (a, b) lift is not done.

## 6. Rigor statement

- Class sums are IEEE double (a-priori rounding ≈ 1e-8 relative on |Z|), not interval arithmetic. Growth rates come from Galerkin truncations without a rigorous error bound for the infinite k1 alphabet.
- Lean covers the algebraic core only (phase split, automaton, quadratic form, NSW divisibility, m = 17 facts); G2 is a paper proof, G3 a sketch, G6 a count, G7 a heuristic.
- Negative results: Galois-twisted reconstructions (`code/probe.py`) do not simplify outliers; shortest-vector classification misses dilution families; broad primary lists over-classify (up to 40 % of residues at small m).

## 7. Literature and novelty

Kurlberg–Rudnick (2000); Keating (1991), Keating–Mezzadri (2000); Degli Esposti–Winn, J. Phys. A 38 (2005) 5895 (citation verified by the referee); Faure–Nonnenmacher–De Bièvre (2003); Gutkin–Osipov (2016), Haake, Bogomolny–Keating. Novelty, to the author's knowledge after a non-exhaustive search: the partial-trace law G2 with the "dual Planck number" reading N ≡ b/a (mod h); the dilution identity G3 (sketch); the moment heuristic G7; the explicit corrected statement R′. Each is elementary once set up; the novelty claim is modest.

## 8. Reproduce

Paths relative to `computations/verification/lineG/`. The C class-sum codes must be compiled first (`gcc -O2 -o classes_orb classes_orb.c -lm`); the class-sum tables (`logs/Torb_*.bin`) are regenerated by `code/batch_orb.sh` (hours at m = 15). Then `python3 formula_table.py k1`, `python3 check_law.py`, `python3 check_dilution.py`, `python3 eta_scan.py`; the m = 17 evaluation is `python3 eval17.py k1` and `python3 formula_table.py k1 17` once `logs/Torb_k1_m17.bin` exists. Lean: `cd formalization && lake exe cache get && lake build Bgs.LineG`.
