# Line E: resonant residues of the fixed-kick cat map. An exact transfer-operator law for giant traces, and what it says about Conjecture R

**Claims:** BGS-TRACE-183 to BGS-TRACE-196. **Annotated:** BGS-TRACE-179, BGS-TRACE-180, BGS-TRACE-182 (states unchanged).

**Inputs** (cited, not re-claimed):
- BGS-TRACE-163: Theorem 1, Lemma Q, Theorem 3 and Proposition R.
- BGS-TRACE-165: Lemma S, and B^sym_m ≤ 2m.
- BGS-TRACE-170: the decomposition W̃rest_m = F_m − B^sym_m − 2mχ_m, and |χ_m| ≤ 1.
- Fixed-map conventions: `derandomized_fixed_kick.md` and `derandomized_fixed_kick/phase1_trace_formula.md`.

**Review state.**
- Claims 183–192 (E1–E10) were audited by an independent referee. The report is `computations/verification/lineE/referee/REPORT.md`. Every required fix F1–F13 and every nit is applied below. Each section marks where a fix is applied with **[F#]**.
- Claims 193–196 (E11–E14) are new in this revision (the "step 2" extension). **They have not been refereed.** They are registered as *verification-pending* (E11–E13) or *conditional* (E14).

**Labels.**
- **[P]**: proved here, using the cited inputs.
- **[CA]**: computer-assisted rigorous (arb ball arithmetic, or IEEE arithmetic with an a-priori rounding bound), with a log.
- **[N]**: numerical (double precision or exact class sums), with a log.
- **[C]**: conditional.
- **[Lean]**: finite pieces kernel-checked in `formalization/Bgs/LineE.lean` and `formalization/Bgs/LineEResonance.lean`.

## 0. Scope [F1]

There are three kicks. Every rigorous growth statement below names its kick.

| name | kick f(q) (K_η = diag e^{iηf(q/N)}) | role |
|---|---|---|
| **k1** | 0.9 cos 2πq | the model in which E3–E6 are certified |
| **f7** | 0.9 cos 2π·7q | the pure 7-mode kick (E11) |
| **f_B**, the *Line B / TRACE-179 kick* | Σ_k c_k e(kq), with c_k = `fCoeff(k,0)` in `computations/verification/lineB/common/model.py` | the diagonal (ℓ = 0) part of the repository kick A_N |

About f_B:
- It has 14 non-zero modes, |k| ≤ 9: c_{±7} = 9/20, c_{±1} = 1/20 ∓ i/200, and further terms of size ≤ 1/40.
- This is the kick of BGS-TRACE-163…182. Conjecture R (BGS-TRACE-179) is a statement about **this** kick.

What is and is not shown.
- **Everything rigorous about exponential growth for all large m is about k1.** It is a statement about the *k1-kick analogue* of Conjecture R, not about R itself:
  - finite range: E5 [CA];
  - all m, but conditional: E6 [C].
- For the TRACE-179 kick f_B the results are:
  - (i) numerical identifications (E8, E10);
  - (ii) an exact law (E12, not yet refereed);
  - (iii) rigorous finite-m lower bounds at m = 11 and 13 (E13, not yet refereed; an m = 17 certificate is running, with a pre-registered prediction, and nothing is claimed for it);
  - (iv) a conditional asymptotic statement along 3 ∤ m (E14).
- **Conjecture R (TRACE-179) is not disproved.** It is an o(m) statement as m → ∞. Finitely many m cannot contradict it, and the asymptotic statements are conditional. TRACE-179 stays **open**.
- Nothing here is a counterexample to BGS (TRACE-005), and nothing concerns eigenvalue statistics beyond the second moment of Tr U^m. No progress on TRACE-148 is claimed.

## 1. Setting

The notation is that of BGS-TRACE-163:
- S = [[3,4],[2,3]], λ = 3+2√2, m odd ≥ 5.
- h = h_m = ((1+√2)^m + (1−√2)^m)/2 (the NSW numbers), D_m = 4h², g′ = 2h, y_m = h·y′. Here h² + 1 = 2y′², so y′ is odd and gcd(y′, 2h) = 1.
- H = H_m = 6I − C − Cᵀ, q(n) = nᵀH⁻¹n, Φ̂(n) = Π_j ĝ(n_j) with g = e^{iηf}.
- Z_m(ν) = Σ_{n∈Z^m} Φ̂(n) e(−ν y′ Nm(α_n)/g′), and F_m(η) = avg_{ν∈(Z/g′)^×}|Z_m(ν)|².
- By Lemma Q, −ν y′ Nm(α_n)/g′ ≡ −2ν q(n) (mod 1).
- c := 1/(λ−λ⁻¹) = 1/(4√2).
- W̃rest_m = F_m − B^sym_m − 2mχ_m. B^sym_m ≤ 2m (TRACE-165), and B^sym is kick-independent. |χ_m| ≤ 1 (TRACE-170), and χ_m ≡ 1 for an even kick. Hence **W̃rest_m ≥ F_m − 4m** for every kick.

## 2. Summary of claims

**Refereed claims (E1–E10).**

| ID | # | statement (scope) | label | state |
|---|---|---|---|---|
| BGS-TRACE-183 | E1 | Resonant residue ν* (N ≡ −4 mod h_m): exact collapse of the phase to ½q(n) + κ_m(Σn)²/8; finite N with c ↦ c(1+4/N) | [P] [Lean m=5..21] | proved |
| BGS-TRACE-184 | E2 | Exact IFS law Z_L = (1−λ^{−m}) Σ_{a even} c_a Tr 𝓛_a^m, operators independent of m; **finite alphabet** | [P] | proved |
| BGS-TRACE-185 | E3 | Certified spectrum of the L-truncated k1 operators (η-grid of 9 points) | [CA] | proved (computer-assisted) |
| BGS-TRACE-186 | E4 | \|Z_L(m)\| ≥ (1−λ^{−m})·½(μ_lo^m − 4T₁r₂^{m−1}) > 0 for all odd m ≥ m0 (truncated k1 kick) | [CA] | proved (computer-assisted) |
| BGS-TRACE-187 | E5 | Physical k1 kick: η = 2, odd m ∈ [17,39], W̃rest_m/m ≥ 7.98…2848; η = 1.75 for m ∈ [19,27]; η = 1.5 for m ∈ [23,33] | [CA] | proved (computer-assisted; k1, finite range) |
| BGS-TRACE-188 | E6 | k1-kick analogue of R fails at η = 2, *if* H∞ holds | [C] | conditional |
| BGS-TRACE-189 | E7 | m = 15 prediction vs outcome (k1) | [N] | open (numerical record) |
| BGS-TRACE-190 | E8 | f_B: giant traces at N ≡ ∓196 (mod h_m) when 3 ∤ m; diluted when 3 \| m | [N] | open |
| BGS-TRACE-191 | E9 | η-interval certification | — | open |
| BGS-TRACE-192 | E10 | The TRACE-182 outlier is the ±196 resonance | [N] (+E13) | open (numerical identification) |

**New in this revision, not yet refereed (E11–E14).**

| ID | # | statement (scope) | label | state |
|---|---|---|---|---|
| BGS-TRACE-193 | E11 | Pure 7-mode kick: Z_{f7}(ν) = Z_{k1}(49ν). Hence the E5 bounds hold verbatim for f7 at 3 ∤ m | [P] [CA] [Lean nsw mod 7] | verification-pending |
| BGS-TRACE-194 | E12 | a²-resonance law, N ≡ ∓4a² (mod h): 49-state IFS law for f_B at N ≡ ∓196 when 3 ∤ m; finite alphabet | [P] [Lean m ≤ 19] | verification-pending |
| BGS-TRACE-195 | E13 | Gauss-completed orbit formula (Prop. G), and rigorous lower bounds for the **TRACE-179 kick** at m = 11 and 13 (m = 17 certificate pending) | [P] [CA] | verification-pending |
| BGS-TRACE-196 | E14 | If the full-alphabet 49-state operator has a dominant simple eigenvalue \|μ\| > λ^{1/4} (H∞,7), then R fails for f_B at η = 2 along 3 ∤ m | [C] | conditional |

**Non-claims.**
- Not a BGS counterexample. Nothing about level statistics. Nothing about TRACE-148.
- E1's starting formula is TRACE-163 Theorem 1 (the Boasman–Keating mechanism). Only the choice of residue and the collapse at that residue are new.
- E5 and E13 hold for finitely many m and finitely many η. **Conjecture R is not disproved**, for any kick. E5 refutes the quantitative form "|W̃rest_m| ≤ m for all m ≥ 17" at η = 2 **for the k1 kick** [F1]. E13 shows |W̃rest_m(2)| > m for the TRACE-179 kick at m = 11 and 13 only (m = 17 certificate pending).
- TRACE-180 is **not** contradicted as a convergence-in-law statement (see §9) [F3].

## 3. Literature placement [F4]

- **Boasman–Keating (1995).** The Fourier/Gauss-sum expansion is theirs, via TRACE-163.
- **Faure–Nonnenmacher–De Bièvre (2003); Bonechi–De Bièvre.**
  - Their special N have a short period of S mod N.
  - Here m is fixed and N → ∞ in a residue class. The trace is large because the Pell phase collapses (E1), not because S^m ≡ ±I (mod N).
  - So the arithmetic flavour is the same, but the mechanism and the regime differ.
- **Kurlberg–Rudnick.** Their results concern the unkicked map and generic N. Line B already notes that the KR, Bourgain and BGK bounds do not apply (ord_h λ = m).
- **Keating–Mezzadri (2000), "Pseudo-symmetries of Anosov maps and spectral statistics".**
  - In their work, arithmetic quantum pseudo-symmetries (operators commuting with U_N for special N) change the eigenvalue statistics.
  - The resonance here is **analogous** (an arithmetic effect at special N with no classical counterpart), but no pseudo-symmetry operator is exhibited.
  - The class N ≡ −4 (mod h_m) depends on m. The mechanism is reciprocity: N acts through an effective "dual dimension" −4.
  - We do **not** claim that E1–E2 are an instance of the Keating–Mezzadri mechanism.
- **Ruelle (1976); Bandtlow–Jenkinson (2008).** Trace formula for holomorphic composition operators (used in E2 and E12). **Lidskii's theorem.**
- **In the record.** See Appendix A. TRACE-117..119, 133..137 and FM-036 concern different regimes. TRACE-163..182 are inputs.

## 4. E1, the resonant residue — BGS-TRACE-183 [P] [Lean]

**Theorem E1.** Let m ≥ 5 be odd. Let ν* be the odd lift (mod 2h) of −4̄ (mod h), so that N ≡ −4 (mod h_m) and ν = N̄. Then for every kick with Σ n²|ĝ(n)| < ∞:

  Z_m(ν*) = Σ_n Φ̂(n) e(½q(n) + κ_m(Σ_j n_j)²/8),

with κ_m odd.

For odd N ≡ −4 (mod h), Tr(K M_N)^m = Tr M_N^m · Σ_n Φ̂(n) e((1+4/N)·½q(n) + κ_m(Σn)²/8), and |Tr M_N^m| = 1.

The hypothesis gcd(N, D_m) = 1 of Theorem 1 is automatic here, since N is odd and N ≡ −4 (mod h) [F13].

**Proof.**
1. Write 4ν* + 1 = −k·h; k is odd. Then −2ν*q − ½q = −(4ν*+1)q/2 = k·h·q/2 = k·r/(8h), with r = nᵀXn = D·q ∈ Z.
2. Here X_ij = φ(|i−j|) and φ(d) = h(y′x_d − 2h·y_d), so r/h ∈ Z. It remains to compute r/h mod 8.
3. Diagonal terms: the coefficient is y′, with weight 1.
4. Pairs (d ≥ 1): the coefficient is y′x_d − 2h·y_d, and it is counted twice, so only its value mod 4 matters. Since x_d ≡ (−1)^d (mod 4) and y_d ≡ d (mod 2) (Lean `xy_mod`, all d), and h is odd, it is ≡ (−1)^d·y′ − 2d ≡ y′ (mod 4), because y′ is odd.
5. Hence k·r/h ≡ k·y′(Σn)² (mod 8), and κ = k·y′ mod 8 is odd. The odd lift is unique mod 2h, so κ is well defined.
6. Finite N: Theorem 1 contributes e(Q/N) with Q = 2q, which equals e((4/N)·½q). ∎

**Remarks [F13].**
- The κ table (κ = 7, 5, 3, 1 for m ≡ 5, 7, 1, 3 mod 8) is **[N]**: verified for m ≤ 41, not proved. It is also inessential, because every odd κ gives |c_a| = ½ for a even (E2).
- Observed k ∈ {−5, −3} for m ≤ 41; k < 0, not just "k odd".
- At −ν* (N ≡ +4) the phase is exactly −½q − κ(Σn)²/8.

**Checks.**
- `computations/verification/lineE/code/resid.py`: exact rational check, all odd m = 5..41.
- Referee: `referee/code/e1_exact.py`, exact for m = 5..25, with control ν* + 2 failing.
- Lean `Bgs.LineE`:
  - `pell` and `xy_mod`, for all d;
  - `cert5`…`cert21` by `decide`, with ν* = 51, 179, 1741, 6089, 59151, 206855, 2009401, 7026989, 68260491;
  - control `cert11_control`, which evaluates to false.

## 5. E2, the IFS law — BGS-TRACE-184 [P] [F10]

**Theorem E2.** Let ĝ be supported in {|n| ≤ L} (finite alphabet), and let ρ > L/(λ−1). Then

  Z_m(ν*) = (1−λ^{−m}) Σ_{a∈{0,2,4,6}} c_a Tr 𝓛_a^m,

where:
- c_a = (1/8)Σ_{b∈Z/8} e((κb² − ab)/8);
- (𝓛_aφ)(s) = Σ_{|n|≤L} ĝ(n) e(cn²/2 + an/8) e(cns) φ((s+n)/λ), acting on the Hardy space H²(D_ρ).

The operators do not depend on m. m enters only through the factor (1−λ^{−m}), through c_a (via κ, i.e. m mod 8), and at finite N through c ↦ c(1+4/N).

**Proof.**
1. *Quadratic form.*
   - H⁻¹ is circulant with entries G(d) = c(λ^{−d} + λ^{−(m−d)})/(1−λ^{−m}).
   - With the periodic s_j := Σ_{k≥1} n_{j−k}λ^{−k} = (1−λ^{−m})⁻¹ Σ_{d=1}^{m} n_{j−d}λ^{−d}, one has ½q(n) = c[Σ_j n_j s_j + ½Σ_j n_j²] and s_{j+1} = (s_j + n_j)/λ.
   - The off-diagonal coefficients ½G(d) and the diagonal ½G(0) = c[λ^{−m}/(1−λ^{−m}) + ½] match.
2. *Sectors.*
   - b = Σn mod 8 is well defined in e(κb²/8), and e(κb²/8) = Σ_a c_a e(ab/8) by the inverse DFT on Z/8.
   - The Gauss sum mod 8 gives |c_a|² = ¼ for a even, for every odd κ. Also c_a = 0 for a odd, by b ↦ b+4.
   - This is checked exactly (sympy, cyclotomic) in `code/bounds.py`.
3. *Word expansion.*
   - 𝓛_a^m = Σ_{w∈{−L..L}^m} M_{p_w} C_{ψ_w}. This is a **finite** sum of weighted composition operators.
   - Each ψ_w is affine of slope λ^{−m}. p_w is the product of the weights along the word, a holomorphic function.
4. *Trace class.*
   - Put θ_n = (ρ+|n|)/(λρ) < 1, which follows from ρ > L/(λ−1).
   - Then ψ_n maps D̄_ρ into D_ρ, and ‖e_k∘ψ_n‖ ≤ θ_n^k in the orthonormal basis e_k = (s/ρ)^k.
   - The rank-one expansion M_{e(cn·)}C_{ψ_n} = Σ_k ⟨·, e_k⟩ M_{e(cn·)}(e_k∘ψ_n) gives ‖M_{e(cn·)}C_{ψ_n}‖₁ ≤ e^{2πc|n|ρ}/(1−θ_n).
   - The sum of these bounds over |n| ≤ L is T₁ in the certificates.
5. *Trace formula* (Ruelle 1976; Bandtlow–Jenkinson 2008, trace formula for composition operators with a holomorphic weight on H² of a disc).
   - If ψ is holomorphic on a neighbourhood of D̄_ρ with ψ(D̄_ρ) ⊂ D_ρ, then M_pC_ψ is trace class and Tr(M_pC_ψ) = p(s*)/(1−ψ′(s*)), where s* is the unique fixed point of ψ.
   - For a period-m word, the fixed point is the periodic orbit s_j, and 1 − ψ_w′ = 1 − λ^{−m}.
   - Summing over words reproduces Σ_n Φ̂(n) e(½q) restricted to each sector.
6. *Lidskii.* H²(D_ρ) is a Hilbert space, so Tr 𝓛^m = Σ_k μ_k^m for a trace-class operator.
7. *Finite N.* Replace c by c(1+4/N) everywhere. ∎

**Checks.**
- `code/trace_check.py`: brute-force n-sums equal Galerkin eigenvalue sums to 1e-13, at (m,L) = (5,4), (5,6), (7,3), (7,4).
- **Finite-N table [F8].** It was regenerated with the hypothesis ρ > L/(λ−1) enforced (`review/predict_finiteN.py`: L = 10, ρ = 2.6 > 2.07, assertion in code). The direct physical traces come from `review/indep_trace.py` (matrix-free chirp–DFT–chirp, no shared code). Log: `review/predict_finiteN_L10_rho2.6.log`.
  - The earlier table used L = 12 with ρ = 2.0 < 2.485. That is outside the theorem, and it is withdrawn.

| m | N = h_m − 4 | \|Tr U_N^m\|² direct | E2 prediction (L=10, ρ=2.6) | rel. diff |
|---|---|---|---|---|
| 5 | 37 | 121.83215496 | 121.83215367 | 1.1e-8 |
| 7 | 235 | 2120.2047659 | 2120.2047360 | 1.4e-8 |
| 9 | 1389 | 29946.148430 | 29946.148219 | 7.0e-9 |
| 11 | 8115 | 405032.63049 | 405032.62813 | 5.8e-9 |
| 13 | 47317 | 5456806.8166 | 5456806.7826 | 6.2e-9 |

- The residual ~1e-8 is the truncation L = 10. The referee obtained the same agreement with independent code (`referee/logs/direct_trace.log`).
- Against exact full-alphabet class sums, m ≤ 15: relative 1e-8 (`referee/logs/cmp_tm.log`).

## 6. E3–E4, certified spectrum — BGS-TRACE-185, 186 [CA]

Method: `code/cert.py`, python-flint/arb at 700–1200 bits.
- **Galerkin matrices.** Exact Galerkin matrices of 𝓛_a in the basis (s/ρ)^k. The matrices are block-triangular products, so the section is exact.
- **Truncation error.** δ ≥ ‖𝓛_a − P_K𝓛_aP_K‖ is bounded by column tails plus a Cauchy estimate at radius 2ρ.
- **Sector 4.** Householder deflation at the top eigenvector, then resolvent bounds on the circles |z − b11| = r1 and |z| = r2 from ‖Y^j‖_F, j ≤ p. These bounds are monotone in |z|, so no sampling is needed. Riesz-projection rank equality follows from δ·sup‖R‖ < 1.
- **Sectors 0, 2, 6.** The spectrum lies in |z| ≤ r2.
- **E4.** Weyl's inequality Σ|μ_k| ≤ ‖𝓛‖₁ ≤ T₁ gives the 4T₁r₂^{m−1} term. The coefficient of μ*^m is c_4(1−λ^{−m}), with |c_4| = ½ exactly and algebraic multiplicity 1.

**Certificate hygiene [F9].**
- *Cache key.* `powers_bound` used to cache by `id(Y)` without holding a reference. A recycled id could have handed sector 6 the norms of sector 2. The cache is now keyed by an explicit sector label.
  - The referee's no-cache rerun shows that no logged run was affected (`referee/certrun/`).
  - An exact symmetry explains why sectors 2 and 6 agree: with R: φ(s) ↦ φ(−s), w_a(−n) = w_{−a}(n), so 𝓛_{8−a} = R𝓛_aR.
- *Bessel tail.* The tail in `bounds.py` is now explicit: Σ_{n>N0}|J_n(x)| ≤ (x/2)^{N0+1}/(N0+1)! · (1 − (x/2)/(N0+2))⁻¹, with N0 = 60. It replaces the earlier 59 extra terms × (1+2⁻²⁰) padding.
- *Determinism.* numpy is used only to precondition (the approximate eigenvector). b11 can vary between runs: at the 1e-88 level in the referee rerun, and by up to 1.3e-61 (sector-4 midpoint) in the regeneration below. The certified enclosures do not depend on this: the regenerated |μ*| bounds and all sector certifications are identical to the refereed run.
- *Regeneration.* All nine certificates were regenerated with the fixed code (`code/run_certs.sh`). The logs are in `computations/verification/lineE/logs/`.

| cert | η | L | K | \|μ*\| ∈ | r₁ | r₂ | m0 (E4) |
|---|---|---|---|---|---|---|---|
| cert_L6 | 2.0 | 6 | 100 | [1.9154751, 1.9154771] | 1e-6 | 1.0 | 17 |
| cert_L8b_eta2 | 2.0 | 8 | 170 | b11 ± 0.05 = [1.86547, 1.96547] | 0.05 | 1.0 | 19 |
| cert_L6_eta1.25 | 1.25 | 6 | 100 | [1.65975, 1.75975] | 0.05 | 1.0 | 17 |
| cert_L6_eta1.5 | 1.5 | 6 | 100 | [1.76190, 1.86190] | 0.05 | 1.0 | 17 |
| cert_L6_eta1.75 | 1.75 | 6 | 100 | [1.83180, 1.93180] | 0.05 | 1.0 | 17 |
| cert_L6r145_eta2.25 | 2.25 | 6 | 100 | [1.86083, 1.96083] | 0.05 | 1.45 | 41 |
| cert_L6r145_eta2.5 | 2.5 | 6 | 100 | [1.81757, 1.91757] | 0.05 | 1.45 | 49 |
| cert_L6r145_eta2.75 | 2.75 | 6 | 100 | [1.73712, 1.83712] | 0.05 | 1.45 | 63 |
| cert_L6r145_eta3.0 | 3.0 | 6 | 100 | [1.62250, 1.72250] | 0.05 | 1.45 | 103 |

Notes:
- For r₁ = 0.05 the enclosure is just b11 ± 0.05 (nit). It certifies at r₁ = 1e-6 for L = 6, η = 2.
- At η ≥ 2.25, sectors 2 and 6 need r₂ = 1.45 (their spectral radius exceeds 1).
- **Scope.** These certificates are for the L-truncated k1 operators only. The full-alphabet μ is not certified.
  - Float values: 1.9154733 at L = 10 vs 1.9154761 at L = 6.

## 7. E5, physical k1 kick, finite range — BGS-TRACE-187 [CA] [F1, F2, F6]

**Bound chain.**
- |Z(ν*) − Z_L| ≤ s₀^m − (s₀−t_L)^m, with s₀ = Σ_n|J_n(0.9η)| and t_L = Σ_{|n|>L}|J_n|.
- F_m ≥ |Z(ν*)|²/φ(2h), with φ(2h) = φ(h) ≤ h − 1.
- W̃rest_m ≥ F_m − 4m.

η = 2, k1 kick (best of L = 6 and L = 8):

| m | 17 | 19 | 21 | 23 | 25 | 27 | 29 | 31 | 33 | 35 | 37 | 39 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F_m/2m ≥ | 5.99 | 20.3 | 36.0 | 44.1 | 88.0 | 167 | 310 | 554 | 927 | 1355 | 1426 | 404 |
| W̃rest_m/m ≥ | 7.98 | 36.6 | 68.0 | 84.3 | 172 | 331 | 616 | 1104 | 1851 | 2706 | 2848 | 804 |

**Violation range vs positivity range [F2].** |W̃rest_m| > m needs F/2m > 2.5, and W̃rest > 0 needs F/2m > 2.

| η | where the bound is positive | where it proves \|W̃rest_m\| > m |
|---|---|---|
| 2.0 | m ∈ [17,39] | **m ∈ [17,39]** |
| 1.75 | m ∈ [17,27] | **m ∈ [19,27]** |
| 1.5 | m ∈ [17,33] | **m ∈ [23,33]** |
| 1.25 | m ∈ [17,41] | **none** (F/2m ≥ 0.45 at most) |
| ≥ 2.25 | empty physical range at L = 6 | none |

Further notes:
- **R_NSW sub-sequence.** h_19 and h_29 = 63018038201 are prime, and both lie in the η = 2 range (nit).
- **Sanity [F6].** At m = 17, the single-residue term |Z(ν*)|²/φ(h)/2m ≈ 18.3 (TO, L = 10). This is *not* F/2m. The true F/2m includes the ±ν* pair and the background, roughly 2·18.3 + 2.
- The bounds are loose by factors of 1.5–15 (referee try-to-break).
- **Why the range is finite.** The tail term behaves like s₀^{m−1}, and s₀ ≈ 2.37 > 1.92 ≈ |μ*|. Larger L extends the range, but no finite L covers all m. Hence E6.

## 8. E6, conditional asymptotic for k1 — BGS-TRACE-188 [C] [F1]

**Hypothesis H∞.** On some Banach space of functions analytic on a domain U ⊃ D_ρ, the full-alphabet operator 𝓛_4^{(∞)} (all n ∈ Z) satisfies:
- it is quasi-compact, with an isolated simple eigenvalue μ∞, |μ∞| > λ^{1/4};
- the rest of the spectra of 𝓛_a^{(∞)} lies in a smaller disc;
- the trace formula holds.

**Statement.** Under H∞, F_m(η) ≥ C(|μ∞|²λ^{−1/2})^m for all large odd m (using h_m < λ^{m/2}/2). Hence **the k1-kick analogue of Conjecture R fails at η = 2.** This is *not* TRACE-179 itself.

The referee's suggested route, recorded and not attempted: H²/H^∞ on thin stadium domains {dist(s, [−R,R]) < τ}. On such domains the multiplier bound e^{2πc|n|τ} does not depend on R.

## 9. E7, E8, E9, E10 [F5, F12, F3]

**E7 (BGS-TRACE-189) [N] [F5].** Prediction F_15/2m ≥ 20 (k1, η = 2); observed 27.885 (exact class sums).
- |Z(ν*)|² = 7.34867e7 (exact class sum), which equals the TO value 7.34867e7 to about 1e-8 (L = 10).
- The value 7.34915e7 is |Z(−ν*)|². It matches its own law (c ↦ −c, κ ↦ −κ).
- The earlier "6e-5 discrepancy" compared the two residues. It is withdrawn.

**E8 (BGS-TRACE-190) [N] [F12].** For the TRACE-179 kick f_B at η = 2:
- 3 ∤ m: the top two residues sit at N ≡ ∓196 = ∓4·49 (mod h_m) (exact class sums, m = 7, 11, 13). These are the Galois images 49̄·(∓ν*) of the k1 resonance, through the dominant mode c_{±7} = 9/20.
- 3 | m: the image **does not exist**, because 7 | h_m ⟺ 3 | m (proved in Lean, `nsw_mod7`).
  - m = 9: F/2m = 1.82. The top |Z|² is about 897.
  - m = 15: F/2m = 3.91, against 8.59 at m = 13. The resonance is diluted over the 12 unit classes N ≡ ±196 (mod h/7), each with |Z|² ≈ 1.09e6. Together they carry 1.745 of the 3.910 (`referee/logs/e8_m9_m15.log`).
- So the f_B evidence is **not monotone in m**: strong for 3 ∤ m, weak for 3 | m. The two subsequences must be treated separately.

**E9 (BGS-TRACE-191).** η-interval certification (rather than a grid of η) is open.

**E10 (BGS-TRACE-192) [N].** For f_B at η = 2, the two residues N ≡ ±196 carry most of F/2m, and the remainder is close to the diagonal baseline of about 2 (`referee/logs/e10.log`):

| m | F/2m | carried by the ±196 residues | remainder |
|---|---|---|---|
| 7 | 2.729 | 1.111 | 1.618 |
| 11 | 5.562 | 3.522 | 2.040 |
| 13 | 8.590 | 6.458 | 2.132 |

- This is a numerical identification of the TRACE-182 outlier.
- E13 below gives **rigorous** lower bounds for the ±196 contributions at m = 11, 13: 3.5227 and 6.4579, which match the table. So the outlier is not a numerical artefact.
- A proved *mechanism* for all m is still missing: E14 is conditional. TRACE-182 therefore stays **open**.

**TRACE-180 [F3].**
- The ν-law at η ≈ 2 has two atoms, each of mass 1/φ(2h) → 0, carrying |Z|² ≈ Λ^{2m}.
- At the numerical level this kills the **moment** form of a fixed-η CLT: M4 → 2 fails (M4 = 1556 at (11,2) for f_B; 1848 at m = 11 for k1), and normalisation by √F fails.
- It is compatible with convergence in law of Z(ν)/√(bulk variance). TRACE-180 as a weak-convergence statement is **not** contradicted.

---------------------------------------------------------------------------------------------------

## 10. Step 2 (new, not yet refereed): from k1 to the actual Line B kick

Everything in §10 is new in this revision. It has been self-checked with code independent of the E1–E10 code. It has **not** been seen by the referee. The verifiers are in `computations/verification/lineE/step2/`.

### 10.1 E11, the pure 7-mode kick — BGS-TRACE-193 [P] [CA] [Lean]

**Proposition.** Let f7(q) = 0.9 cos(2π·7q). Then:
1. Z_{f7}(ν) = Z_{k1}(49ν) for every ν.
2. If 3 ∤ m: F_m(f7; η) = F_m(k1; η) and W̃rest_m(f7; η) = W̃rest_m(k1; η).
3. Hence the E5 bounds hold verbatim for f7:
   - η = 2: m ∈ {17, 19, 23, 25, 29, 31, 35, 37};
   - η = 1.75: m ∈ {19, 23, 25};
   - η = 1.5: m ∈ {23, 25, 29, 31}.

**Proof.**
1. ĝ_{f7}(n) = ĝ_{k1}(n/7) if 7 | n, and 0 otherwise. Also α_{7n′} = 7α_{n′}, so Nm(α_{7n′}) = 49·Nm(α_{n′}). This gives (1).
2. If 3 ∤ m then 7 ∤ h_m (Lean `nsw_mod7`: nsw j ≡ 0 (mod 7) ⟺ j ≡ 1 (mod 3), with m = 2j+1). So 49 is a unit mod g′ = 2h, and ν ↦ 49ν permutes the units. Hence F(f7) = F(k1).
3. B^sym is kick-independent (TRACE-165). Both kicks are even, so χ_m ≡ 1 for both. Hence W̃rest agrees. ∎

**Check** (`step2/check_f7.py`, Prop. G over all units, no truncation): Z_{f7}(ν) = Z_{k1}(49ν) to ≤ 2e-8 absolute at m = 5, 7, 11, and F(f7) = F(k1) to 1e-14 relative there. At m = 9 (3 | m) F(f7) = 32.88 ≠ F(k1) = 87.11, so the hypothesis 3 ∤ m is genuinely needed. The k1 values F_m/2m = 1.843, 2.805, 4.839, 6.894 reproduce the referee's exact class sums.

**Scope.** f7 is **not** the TRACE-179 kick. f_B has 13 further modes, of size up to 1/20.

### 10.2 E12, the a²-resonance law — BGS-TRACE-194 [P] [Lean finite]

Let a be odd with gcd(a, 2h) = 1, and s ∈ {±1}. Let ν = ν_{a,s} be the odd lift of −s(4a²)⁻¹ (mod h), so that N ≡ −s·4a² (mod h). Write 4a²ν + s = k·h.

**Theorem E12.** Assume:
- (i) 2 is a square mod p for every prime p | a. Fix r with r² ≡ 2 (mod a²) (Hensel). Let ι: Z[√2, ½] → Z/a² be the ring map with √2 ↦ r, and ℓ = ι(λ) = 3+2r.
- (ii) ℓ^m ≢ 1 (mod p) for every p | a.

Then for every n ∈ Z^m:

  −ν y′Nm(α_n)/g′ ≡ (s c/a²)[Σ_j n_j s_j + ½Σ n_j²] + κ(Σn)²/8 + (γ/a²)[Σ_j n_j σ_j + 2̄Σ n_j²]  (mod 1),

where:
- s_j is the real periodic orbit of E2;
- σ_j ∈ Z/a² is the unique periodic orbit of σ ↦ ℓ⁻¹(σ + n_j);
- 2̄ = 2⁻¹ mod a²;
- 1/(8a²) = u/8 + v/a², with u = (a²)⁻¹ mod 8 and v = (1 − ua²)/8;
- κ = −k·u·y′ mod 8 (odd);
- γ = −k·v·2B(1 − ℓ^{−m}) mod a², with B = ι((2y′ + h√2)/4).

Consequently, for ĝ supported in {|n| ≤ L} (finite alphabet) and ρ > L/(a(λ−1)):

  Z_m(ν_{a,s}) = (1−λ^{−m}) Σ_{b even} c_b Tr 𝓛_b^m,

where c_b is as in E2 (with this κ) and 𝓛_b acts on H²(D_ρ) ⊗ ℓ²(Z/a²):

  (𝓛_bΦ)(u, σ) = Σ_{|n|≤L} ĝ(n) e(s c(x_n u + x_n²/2) + bn/8 + γ(nσ + 2̄n²)/a²) Φ((u + x_n)/λ, ℓ⁻¹(σ + n)),  x_n = n/a.

At finite N (TRACE-163 Thm 1), s·c is replaced by s·c(1 + s·4a²/N).

**Specialisation to the Line B kick.**
- For a = 7: 2 ≡ 3² (mod 7), so r ≡ ±3 (mod 7) and ℓ = 3+2r ≡ 2 or 4 (mod 7). Both have order 3, so (ii) ⟺ 3 ∤ m. Also gcd(7, h) = 1 ⟺ 3 ∤ m.
- So E12 applies exactly at N ≡ ∓196 (mod h_m) for every odd m with 3 ∤ m. These are the residues of E8.

**Proof.**
1. *Splitting.* By Lemma Q, the phase is −2νq with q = P/(4h), where P = Σ_{ij} ψ(|i−j|) n_i n_j ∈ Z and ψ(d) = y′x_d − 2h·y_d. Since ν = (kh − s)/(4a²):

   −2νq = −(kh − s)P/(8a²h) = s·q/(2a²) − k·P/(8a²).

2. *Real part.* s·q/(2a²) = (s c/a²)[Σ n_j s_j + ½Σn_j²] by E2 step 1. Rescaling by x = n/a gives the real IFS with letters x_n and the same contraction 1/λ.
3. *Mod 8 part.* −kP/(8a²) ≡ −kuP/8 − kvP/a² (mod 1), because P ∈ Z. By E1 steps 3–4, P ≡ y′(Σn)² (mod 8). So −kuP/8 ≡ κ(Σn)²/8.
4. *Mod a² part.*
   - With x_d = (λ^d + λ^{−d})/2 and y_d = (λ^d − λ^{−d})/(4√2): ψ(d) = βλ^d + β̄λ^{−d}, where β = (2y′ − √2h)/4 and β̄ = (2y′ + √2h)/4.
   - ψ is symmetric: ψ(m−d) = ψ(d) (Lemma Q, step 1). Hence β̄ = βλ^m, and ψ(d) = β̄(λ^{−d} + λ^{−(m−d)}), an identity in Z[√2, ½].
   - Apply ι, and let σ_j be the periodic orbit of σ ↦ ℓ⁻¹(σ + n_j). It exists and is unique by (ii), since the composed affine map σ ↦ ℓ^{−m}σ + const has exactly one fixed point.
   - By the same periodic bookkeeping as E2 step 1:

     (1 − ℓ^{−m}) Σ_j n_jσ_j = ℓ^{−m}Σ n_j² + Σ_{i<j} n_in_j(ℓ^{−d} + ℓ^{−(m−d)}),  where d = j − i.

   - Also ι(ψ(0)) = B(1+ℓ^{−m}) = B[2ℓ^{−m} + (1−ℓ^{−m})]. Therefore

     P ≡ 2B(1 − ℓ^{−m})[Σ n_jσ_j + 2̄Σ n_j²]  (mod a²),

     and −kvP/a² gives the γ-term.
5. *Trace law.* As in E2, with H²(D_ρ) replaced by H²(D_ρ) ⊗ ℓ²(Z/a²).
   - For a word w, the operator is (M_{p_w}C_{ψ_w}) ⊗ Π_w, where Π_w is a weighted permutation matrix (σ ↦ ℓ^{−m}σ + b_w is a bijection).
   - Tr(A ⊗ Π) = Tr A · Tr Π. Tr Π_w is the weight at the unique fixed point, which is the γ-phase of the periodic σ-orbit.
   - The real factor is handled as in E2, with ψ_n(u) = (u + x_n)/λ and θ_n = (ρ + |x_n|)/(λρ) < 1.
   - Sectors as in E2. Lidskii applies on the Hilbert space H²(D_ρ) ⊗ C^{a²}. ∎

**Remarks.**
- For a = 1 the theorem reduces to E1/E2 (κ only, no γ-term).
- For a = 7, γ ∈ {11, 38} (one value per root r), independent of m for m ≤ 41. It equals −s·ι(c), with ι(c) = ι(1/(4√2)). This identity is observed [N] (`step2/cert49_py.log`); it is not needed.
- For a = 3, 5, 11 there is no √2 mod a², and E12 does not apply.

**Checks.**
- `step2/check_phase.py`: phase identity against the exact Line B integer phase, 138/138 cases, for a ∈ {1, 7, 17, 23}, odd m ≤ 25, s = ±1, and both roots r.
- `step2/check_trace.py`: brute-force n-sum = 49-state Galerkin trace law to ≤ 1e-13, at m = 5, 7, a ∈ {1, 7}, s = ±1, random weights.
- `step2/cert49_py.py`: the coefficient identities, cleared of denominators by 392h², checked exactly for all odd m ≤ 41 with 3 ∤ m. 52/52.
- **Lean** (module `Bgs.LineEResonance`):
  - `cert49_*` proves the same integer identities by `decide` at m = 5, 7, 11, 13, 17, 19, for s = ±1. The literals are in `step2/lean_literals.txt`.
  - `cert49_11_control` (wrong γ) evaluates to false.
  - `nsw_mod7` proves 7 | h_m ⟺ 3 | m for all m.
- **Independent physical check** (`step2/check_finiteN.py`, finite-N form). The direct trace |Tr U_N^m|² for the **Line B kick** at m = 11, N = 7923 = h − 196 is 262377.67. It comes from the matrix-free code `review/indep_trace_full.py`, which shares no code with step 2. The 49-state law (L = 48, K = 30/40) gives 262391.35, a relative difference of 5.2e-5. This residual is consistent with the truncation L = 48 of ĝ, as in the infinite-N comparison below.
  - At N = 43 (m = 7) the effective coupling c(1+196/N) ≈ 5.6c puts the Galerkin computation outside its regime. It diverges, and this case is recorded as not tested.
- `step2/cmp_full.py` (infinite N, Line B kick, η = 2): the law (L = 40, K = 30) vs the referee's exact class sums agrees to 1e-4…4e-3 at m = 5, 7, 11, 13.

### 10.3 E13, Gauss completion and rigorous bounds for the TRACE-179 kick — BGS-TRACE-195 [P] [CA]

**Proposition G (exact orbit formula on the support).** Let m be odd, ν a unit mod 2h, and t = (16ν)⁻¹ mod h. Let z_j = a_jz₀ + b_jz₁ (mod h) denote the q-sequences mod h: z_{j+1} = 6z_j − z_{j−1}, periodic since T^m ≡ I (mod h). Then

  |Z_m(ν)| = h⁻¹ |Σ_{(z₀,z₁)∈(Z/h)²} e(t·R(z)/h) Π_{j<m} g(½ + z_j/h)|,  where R(z) := 2zᵀHz/h mod h.

R is a binary quadratic form mod h in (z₀, z₁). Its coefficients (A, B, C) are computed exactly.

**Proof.**
1. *Theorem 3 and Lemma S.* By TRACE-163 Theorem 3, Z = Σ_{ξ∈G} k_ν(ξ)Φ(ξ). By Proposition R and TRACE-165 Lemma S, k_ν vanishes off 𝒮 = ½𝟙 + G[h], and |k_ν(ξ)| = D_eff^{−1/2} = 1/h on 𝒮 (|Rad| = 4, D = 4h²).
2. *Shift identity.* For γ ∈ Z^m, the substitution β ↦ β + γ in the definition of k_ν gives

   k_ν(½𝟙 − 4νH⁻¹γ) = k_ν(½𝟙)·e(2νq(γ) − ⟨γ, ½𝟙⟩),

   using 𝒬(β+γ) = 𝒬(β) + 𝒬(γ) + 4βᵀH⁻¹γ and 𝒬 ≡ 2q (mod 1).
3. *Choice of γ.* For w = z/h ∈ G[h], put t′ = (4ν)⁻¹ mod h and γ = −t′Hw ∈ Z^m. Then −4νH⁻¹γ = 4νt′w ≡ w (mod Z^m).
4. *The character term is trivial.* 𝟙ᵀHw = 4Σw_j ∈ Z, and h is odd, so h | Σz_j. Hence ⟨γ, ½𝟙⟩ = −2t′Σz_j/h ∈ Z.
5. *Phase.* 2νq(γ) = 2νt′² zᵀHz/h² = νt′²·R(z)/h, and νt′² ≡ (16ν)⁻¹ (mod h). R(z) ∈ Z because Hz ≡ 0 (mod h). R mod h depends only on z mod h.
6. Taking absolute values gives the formula. ∎

**Remarks.**
- Observed [N]: R = −ȳ′·(z₀² − 6z₀z₁ + z₁²) (mod h). This agrees with the referee's independent class-sum formula, which has v = −16̄ν̄ȳ′ (referee §3.1). It is not used: the certificate computes A, B, C directly and checks R at 200 random points.
- Prop. G uses no truncation of ĝ. The values g(½ + z/h) = e^{iηf(½+z/h)} are evaluated directly.
- Check `step2/check_propG.py`: Prop. G vs brute-force n-sum (k1), m = 5, L = 9: relative ≤ 7e-7 at the resonant and at non-resonant ν. At m = 7, L = 4 the n-sum is truncation-limited (1e-2).

**Certificate** (`step2/cert_class.py` + `step2/zres.c`). It certifies lower bounds on |Z_m(ν)|² at N ≡ ∓196 for the **exact Line B kick f_B**.

Inputs:
- The kick coefficients are exact rationals, asserted equal to `model.py fCoeff(k,0)`.
- Tables of g(½+k/h) and e(k/h) are computed in arb (96 bits) and rounded to double. The measured error is eps.

Kernel:
- IEEE double, without FMA contraction or fast-math.
- Rows are summed in double. Row totals are accumulated in x87 long double (u_L = 2⁻⁶⁴).

A-priori error bound (`errbound`), with u = 2⁻⁵³ and n = h:
- *Products.* Each term is a product of m+1 tabulated unimodular numbers, computed by m complex multiplications (naive formula, error ≤ √5u|x||y|, Brent–Percival–Zimmermann). The error e_k obeys e_{k+1} ≤ e_k(1+eps)(1+√5u) + eps + √5u(1+eps).
- *Row sums.* Recursive summation gives ≤ √2·γ_n(u)·n·(1+e_m) per row.
- *Row totals.* ≤ √2·γ_{n+T+2}(u_L)·n²(1+e_m)(1+γ_n), where T is the number of threads.

The resulting bound on |S − S_exact| is subtracted from |S|, which is padded by (1 − 2⁻⁵⁰) for the output and abs() roundings. The final bounds are:
- F_m ≥ (|Z(ν₊)|² + |Z(ν₋)|²)/φ(2h);
- W̃rest_m ≥ F_m − 4m.

Results (η = 2, Line B diagonal kick f_B; `step2/cert_class.jsonl`):

| m | h | \|Z\|² ≥ at N ≡ −196 | \|Z\|² ≥ at N ≡ +196 | F_m/2m ≥ | W̃rest_m/m ≥ | abs. error bound on S |
|---|---|---|---|---|---|---|
| 11 | 8119 | 290544.5725 | 309515.7860 | 3.5227 | 3.0454 | 8.4e-5 |
| 13 | 47321 | 3628100.5005 | 4203360.8595 | 6.4579 | 8.9159 | 1.7e-2 |
| 17 | 1607521 | *pending* | *pending* | *pending* | *pending* | — |

- m = 5 and 7 reproduce the referee's exact class sums. At m = 11 and 13, the certified F/2m bounds from the two residues alone are within 1e-4 of the referee's "carried by ±196" column (3.522, 6.458).
- Predictions from the 49-state law (L = 48, K = 40, ρ = 2.2) are in `step2/predictions.jsonl`, written 2026-10-30 07:40–07:41 CET.
  - m = 11: 290557 and 309515. m = 13: 3628327 and 4203526. These were computed *after* the m = 11, 13 certificates, so they are consistency checks only.
  - m = 17: 5.66587e8 (N ≡ −196) and 7.04767e8 (N ≡ +196). These were written while the m = 17 certificate was running (started 07:39:56 CET), before its result existed. This is a genuine pre-registered prediction; the outcome is still pending.
  - Certified m = 17 values: **pending.** The certificate was still running when this revision was committed, so no m = 17 bound is claimed anywhere in this revision. When it finishes, its two values are to be compared with the predictions above; the comparison is a test of the 49-state law (E12/E14), not an input to any claim.

**What E13 proves.** For the TRACE-179 kick at η = 2, |W̃rest_m(2)| > m at m = 11 and 13 (m = 17 certificate pending). In particular F_11(2)/2m ≥ 3.52, so the TRACE-182 outlier is genuine and is carried by the ±196 residues. **What it does not prove:** anything about m → ∞. R is untouched.

### 10.4 E14, conditional asymptotic failure of R for the TRACE-179 kick along 3 ∤ m — BGS-TRACE-196 [C]

**Hypothesis H∞,7.** Let 𝓛_b^{(∞)} be the full-alphabet (all n ∈ Z) 49-state operators of E12 for f_B at η = 2 and a = 7. On some Banach space of functions on U × Z/49, with U ⊃ D_ρ, the following hold:
- these operators are quasi-compact;
- the trace formula of E12 holds;
- one sector b₀ has an isolated simple eigenvalue μ∞ with |μ∞| > λ^{1/4};
- all other spectrum (all sectors, both s = ±1) lies in a strictly smaller disc;
- the eigenvalue has a non-vanishing coefficient. This is automatic: |c_b| = ½, and the multiplicity is 1.

**Statement.** Under H∞,7, for odd m → ∞ with 3 ∤ m:
- |Z_m(ν_{7,±})| ≍ |μ∞|^m;
- F_m(2) ≥ C·(|μ∞|²/λ^{1/2})^m;
- W̃rest_m(2)/m → ∞.

So Conjecture R (TRACE-179) fails at η = 2 for the Line B kick along the subsequence 3 ∤ m, *conditionally on H∞,7*. Nothing is claimed along 3 | m (E8).

**Evidence for H∞,7** [N]. These are float Galerkin computations, not certified (`step2/spec_full_m13_K30.log`; L = 40, K = 30, ρ = 2):
- leading eigenvalues |μ| = 1.884 (s = +1, b = 4) and 1.897 (s = −1, b = 0);
- the next eigenvalues are ≤ 1.30 in every sector;
- λ^{1/4} = 1.554;
- the law (L = 48, K = 40) reproduces the certified m = 11, 13 values to ≤ 1e-4 (computed after those certificates, so a consistency check only). The pre-registered m = 17 prediction (§10.3) is not yet tested: its certificate is pending.

**Why it is only conditional.**
- The 49-state Galerkin matrices have dimension 49K ≈ 1.5–4·10³. Ball-arithmetic certification of them was not feasible in this session.
- The ℓ¹ alphabet-tail argument of E5 fails for the same reason as for k1 (s₀ ≈ 2.37 > 1.9).

**Closure route.** Certify the truncated 49-state spectrum, as E3 does for k1, and prove a uniform alphabet-tail estimate, e.g. on stadium domains. That would turn E14 into a theorem.

## 11. Effect on existing claims

- **BGS-TRACE-179 (Conjecture R): stays open.**
  - Evidence against R for the Line B kick is now: rigorous at m = 11 and 13 (m = 17 certificate pending) (E13); exact structure along 3 ∤ m (E12); a conditional asymptotic disproof (E14). The weak point is 3 | m (E8).
  - The k1-kick analogue of R is refuted on a finite range (E5) and conditionally for all large m (E6).
- **BGS-TRACE-180 (fixed-η CLT): stays open.** The moment form fails at η ≈ 2. Convergence in law is not contradicted [F3].
- **BGS-TRACE-182 ((11,2) outlier): stays open.**
  - Numerical identification (E10), plus a rigorous lower bound F_11(2)/2m ≥ 3.52 from the ±196 residues (E13). So the outlier is not a numerical artefact.
  - The closure condition (a *proved mechanism*) is met only conditionally (E14).

## 12. Lean

`formalization/Bgs/LineE.lean` (namespace `Bgs.LineE`, unchanged from the refereed copy):
- `pell` and `xy_mod`, for all d;
- `cert5`…`cert21`, and the control `cert11_control`.

`formalization/Bgs/LineEResonance.lean` (new, not refereed):
- `nsw_mod7_cycle`, `nsw_mod7` (7 | h_m ⟺ 3 | m), `three_dvd_iff`;
- `cert49`, `cert49_{5,7,11,13,17,19}{p,m}`, and the control `cert49_11_control`.

Both files:
- are imported by `Bgs.lean`;
- have no `sorry` and no `native_decide`;
- use only the axioms propext, Classical.choice and Quot.sound (`#print axioms` log in the evidence receipt).

Not formalised: the analytic trace formulas (E2, E12), the ball-arithmetic certificates (E3–E5, E13), and the passage from coefficient identities to Z (a one-line argument).

## 13. Reproduce

- Python: python-flint 0.9.0, numpy 2.5.4, scipy 1.18.1, sympy 1.14.0 (pinned in `computations/verification/lineE/README.md`).
- E1–E5:
  - `code/resid.py`;
  - `code/trace_check.py`;
  - `PY=… bash code/run_certs.sh` (all nine certificates and their bounds);
  - `review/predict_finiteN.py m`;
  - `review/indep_trace.py m 2.0 512`;
  - `review/indep_trace_full.py 11 2.0 512 196`.
- Step 2:
  - `gcc -O3 -march=native -ffp-contract=off -fno-fast-math -fopenmp -o step2/zres step2/zres.c`;
  - `step2/check_phase.py`, `check_trace.py`, `check_propG.py`, `cert49_py.py`, `check_finiteN.py`;
  - `step2/cert_class.py full m 2.0 196,-196 [threads]`.
- Lean: `cd formalization && lake exe cache get && lake build Bgs`.

## Appendix A. Overlap with the record [F11]

| item | already in the record? | verdict |
|---|---|---|
| n-side formula, Lemma Q, Theorem 3, Prop. R | TRACE-163 (and Boasman–Keating (5.4)) | input |
| B^sym ≤ 2m, \|χ\| ≤ 1, W̃ decomposition | TRACE-165, 170 | input |
| transfer operators for a trace-type quantity | TRACE-170/172/173 (χ_m, which *decays*) | the method is in-house; here a different (IFS) operator acts on a growing quantity |
| residue N ≡ −4 (mod h_m), collapse of the phase, IFS law | no | new (E1, E2) |
| residues N ≡ −4a² (mod h_m), 49-state law | no | new (E12) |
| explanation of TRACE-182 | no ("no explanation is claimed") | numerical identification + rigorous m = 11 bound |

**TRACE-133..137 (revival claims).**
- Their regime is the scalar return S^t ≡ I (mod N), with random phases and t ~ 2 log_λ N. That is N ≈ h_m with m tied to N.
- Line E is the opposite regime: fixed m, N → ∞ in a residue class, a fixed kick, and *growth*.
- Not overlapping.

**The labels 35, 1189 are not a coincidence (correction).**
- In the old class-sum variable t, the label of the resonant residue at m = 7, 11 is t* = 35, 1189. These numbers appear in the TRACE-134 minimal-period family.
- This is a Pell identity: h_{m−2}·y_{(m−1)/2} ≡ 1 (mod h_m) for every odd m, verified for m = 5..79 (`referee/logs/tstar_identity.log`). Hence t* = h_{m−2}⁻¹ = y_{(m−1)/2}, and 35 = y_3, 1189 = y_5, 40391 = y_7.
- There is still no dynamical link.

**TRACE-117/118/119 and FM-036.**
- TRACE-117..119 are kick-blind arithmetic spikes in the Abel statistic at Pell dimensions N = u_n. FM-036 concerns Pell moduli and microscopic stability.
- They share the Pell arithmetic, but their regime is N itself a Pell number, with minimal period and N → ∞ along that sequence.
- Line E fixes m and lets N → ∞ in a residue class mod h_m. Not overlapping.

**TRACE-180 [F3].** The moment form of the fixed-η CLT fails at η ≈ 2. Convergence in law is not contradicted.
