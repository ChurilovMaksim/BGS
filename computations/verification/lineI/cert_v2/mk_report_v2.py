L=open('/workspace/bgs-lineI/REPORT.md').read().split('\n')
def ln(i): return L[i-1]
rep={}  # line number -> list of replacement lines
rep[2]=['Status v2: 2026-10-31 (UTC+5), Sessions 1–4 with referee fixes B1–B9, R1–R7 applied (referee report /workspace/audit/lineI/REPORT.md).',
        'REPORT.md (v1) is kept unchanged for provenance. Numbers are double-precision floats (NOT interval-certified) unless marked;']
rep[9]=['* Obtained: (i) an exact, proved dilation-coset L² law (Prop I2; algebraic core Lean-checked) that converts the frozen-R′']
rep[11]=['  reduction R′ ⇐ (E″)+(T″)+(D) (Thm I4, quantifiers fixed) with a Fourier lemma (I5′; the old "diagonal invisibility" is withdrawn); (iii) a full empirical']
rep[12]=['  decomposition of W′ at m=17: on the "rest" set (85% of residues) the mean of |Z|²/RMT is 0.999 [N], and W′ lives on explicit']
rep[28]=['Tr(βλ^i)/d (period ord_d λ | m).','Congruence [P] (R3): P(n) ≡ y′Nm(α_n) (mod 2h), since Nm(α_n) = Σ_{i,j} n_i n_j x_{|i−j|} (because λ^{−d} = λ̄^d) and',
         'ψ(d) = y′x_d − 2h y_d ≡ y′x_d (mod 2h). (Also 0 numerical failures, m=9,15,17.)  R5: for odd m every prime d | h_m splits,',
         'since h² + 1 = 2y′² gives (2/d) = 1; so ε = +1 always and the inert branch of (b) is vacuous here.']
rep[30]=[' - Lean: lean/LineI.lean (cross_term, sum_N_sq, coset_decomp, norm_count_7, norm_count_23_zero [zero count only]), 0 errors,']
rep[35]=['   G2 traces agree with class sums to 2.6e-8 relative; |Z_0|²=30042.05, main/member 613.10; over ALL six t ≠ 0 (this includes the one',
         '   NON-UNIT dilation j = 2, which is not a member of M_7(ρ)) cross 877.61, square 319.51; over the 5 MEMBERS Dev = 900.47, i.e. relative']
rep[36]=['   excess +0.2937 (matches dil.log) (B3).  m=15,21,27: done in Session 3 (zpred).']
rep[37]=[' - Heuristic corollary [C]: frozen dilation term is o(1) relative iff r_tw<√λ/μ≈1.26038 (cross) and r_tw<λ^{1/4}']
rep[40]=['**Thm I4 (reduction) [P, elementary] (B5: quantifiers fixed).** All sums are over UNITS ν mod 2h, normalised by 1/φ(2h).',
         'Fix ONE function Y(m) → ∞ and put K_m = {Λ: y(Λ) ≤ Y(m)}.  If (E″) (1/φ(2h))Σ_{ν unit: Λ_ν∈K_m}(|Z_ν|²−RMT_m) = o(m) for THIS']
rep[41]=['sequence K_m (uniformity in the growing compacta, not merely for each fixed compact K); (T″) cusp control: the same sum over Λ_ν in',
         'y ≥ Y(m), minus the explicit resonance sum, is o(m) (same Y(m)); (D) the dilation remainder (Prop I2 cross+square terms, summed over levels) is o(m),']
rep[42]=['then R′ holds.  Equivalent alternative: (T″) for EVERY Y(m) → ∞ and (E″) for each fixed K, with a diagonal choice of Y(m) growing']
rep[43]=['slowly enough.  (Trivial partition of residues by shape; stated to isolate what must be proved.)']
rep[45]=['**Lemma I5′ (Fourier expansion of weighted horocycle sums) [P] — corrected, see theory_E2_v2.md (B6).** For ALL ν mod 2h:',
         'Σ_ν|Z_ν|² f(z_ν) = 2h Σ_k c_k(1/2h) C(k), C(k) = Σ Φ̂(n)Φ̂(n′)‾ 1[P(n)−P(n′) ≡ k] (sign fixed: c_{[P(n)−P(n′)]}). For UNITS ν the']
rep[46]=['pair (n,n′) carries the Ramanujan sum c_{2h}(k−P(n)+P(n′)).  The diagonal class P ≡ P′ contributes C(0)× the UNWEIGHTED horocycle sum of f']
rep[47]=['(it meets every c_{2hj}, not only c_0), so it is not invisible: it needs an equidistribution input (cite with rate) and C(0) = O(m).']
rep[89]=['1. **Frozen R′ (TRACE-206) [heuristic, B9]: it is expected (heuristically) not to survive asymptotically; we propose an amendment.** For d = 7, the relative error of']
rep[91]=['   (0.6579^m). Hence the frozen d = 7 remainder is expected to contribute Dev/(mφ) ~ C·1.0187^m/m to W′/m (B9b: /m, not /m²) along m ≡ 3 (mod 6), with oscillating sign:']
rep[92]=['   numerically |·| up to 0.021 for m = 21..45 (larger ρ; (−2,8) gives 0.0007 at m=33, 0.003 at m=45), Dev/(m²h) envelope ≈ 1–4·10⁻⁴ flat on m = 33..123.']
rep[93]=['   The data m ≤ 123 do NOT show the growth (predicted change over 21..123 only ×1.1); the extrapolation (≈ 0.2–0.3 at m ≈ 300, ≈ 1 at 400,',
         '   ≈ 6–8 at 500; referee envelope fit e^{0.0190}) rests entirely on r_tw = 1.2837 > 1.26038 (1.9% margin). Session 4: the counting',
         '   statement r_tw > R is being certified (dom/, see S4.2); the coefficient is NOT certified. If it holds, frozen R′ would be expected to FAIL']
rep[94]=['   (W′/m not → 0) at m of a few hundred. Not a proof, and NOT a disproof under TRACE-206\'s closure condition: missing are (i) c(β) ≠ 0,',
         '   (ii) the (±2,16) d = 7 members and all other levels (only (±2,8) at d = 7 modelled), (iii) partial cancellation of the two ρ',
         '   (seen e.g. at m = 33, 51, 105), (iv) no compensation by the bulk / W′_A.  TRACE-206 stays OPEN; R′_A is a proposal for the maintainers.']
rep[95]=[]
rep[104]=['   spectra of the lifted V lattice in |z| < 1.45 and E lattice in |z| < 1.0 (Session 4: all m ≡ 3 (mod 6), ρ = (±2,8), by exact symmetry). Consequence: the dilation SQUARE term is']
rep[105]=['   exponentially small relative to φ(2h) (rate (1.45²/√λ)^m ≤ 0.87089^m). The CROSS-term condition r_tw < 1.26038 is FALSE']
rep[106]=['   numerically (1.2837), so it cannot be certified. Lower-bound (counting) certification: Session 4, S4.2.']
rep[107]=['3. **(E″): no rigorous result.** Three routes analysed; each shows a specific inequality chain fails [assessment]. Halo: O(1) in F units [N].']
rep[118]=['* Symmetries [P] (B4): λ^m = x_m + 2y_m√2 with x_m = 2h²+1, 2y_m = 2hy′, so λ^m ≡ 1 (mod 2h); hence x_{m−d} ≡ x_d (mod 2h) and P is a',
          '  cyclic quadratic form mod 2h (Φ̂ is cyclic too). With λ^m ≡ 1 (mod 7) (3 | m) the cyclic shift multiplies α_n by λ: Ẑ(λβ) = Ẑ(β).',
          '  Ẑ(−β) = Ẑ(β): ĝ(−n) = ĝ(n) (iⁿJ_n even), P(−n) = P(n), α_{−n} = −α_n.  ⇒ 8 classes (referee: 8 orbits of size 6, union 48).']
rep[123]=['* Barrier note [assessment] (B9): uniform-in-d control of (D) via operator bounds needs square-root cancellation in Ẑ_d for d up to ≈ |Z_ρ|/√(4m); the diagonal']
rep[135]=['* Case reduction [P] (R4): h + y′√2 = (1+√2)^m and k ≡ 3h⁻¹ (mod 8); the finite factor depends on m only through (k, ψ₀, ψ₁) mod 8 (ψ₁ = 3y′ − 2h),',
          '  which are functions of (h, y′) mod 8; so the operator depends only on (1+√2)^m mod 8 (period 8 in m since (1+√2)^8 ≡ 1 mod 8). E.g. m ≡ 9 (24) ⇒ m ≡ 1 (8) ⇒ (h,y′) ≡ (1,1)',
          '  (mod 8) ⇒ k ≡ 3, ψ₀ = 1, ψ₁ ≡ 1.  7 | h ⟺ m ≡ 3 (mod 6): (1+√2)³ ≡ 5√2 (mod 7), so (1+√2)⁶ ≡ 1 and the rational part h_m ≡ 0 (mod 7)']
rep[136]=['  exactly for m ≡ 3 (mod 6) (check of the 6 residues).  Verified for m < 700 (referee code/cases.py).']
rep[148]=['the lifted cyclic V operator has spectrum in |z| < 1.45 (rig_spec quantity F (at radius R) ≤ 0.357 < 1, decided in arb; also at R = 1.5, 1.55),']
rep[149]=['and the E operator has spectrum in |z| < 1.0 (F = 0.0138 at R = 1.0).  (R7: "F·R" in v1 meant F evaluated at radius R, Line H notation F_R.)']
rep[150]=['**Theorem I6 (v2).** For all m ≡ 3 (mod 6), ρ ∈ {(2,8), (−2,8)} (Session 4: exact intertwiners, sym/) and all β ≢ 0 (mod 7):']
rep[151]=['  |Ẑ(β)| ≤ 6.769·10⁶ · 1.45^m + 6.859·10⁴     (outward rounded; exact CV = 6 768 179.601…, CE = 68 586.18…; B1),']
rep[153]=['  7 Σ_u |δ_u|² / φ(2h_m) ≤ (13/7)·48·(6.769·10⁶·1.45^m + 6.859·10⁴)² · (e^γ lnln h + 2.50637/lnln h)/h ,']
rep[154]=['which is ≤ 0.01 for every such m ≥ 321 (0.004574 at 321; 0.01046 at 315) and decays like (1.45²/√λ)^m ≤ 0.87089^m (exact 0.8708840…).',
          '(Table m ≡ 3 (mod 6), m ≤ 1425: cert_v2/logs/bounds_sq_v2.json; v1 table cert/logs/bounds_sq.json.) R1 tail, m ≥ 1425: (CV·1.45^m+CE)²']
rep[155]=['≤ (CV+CE)²·1.45^{2m}, h_m ≥ (1+√2)^m/3, lnln h ≤ ln m, 1/lnln h ≤ 1/lnln h_1425, and q^m(e^γ ln m + c) is decreasing since ln q + 1/(m ln m) < 0;',
          'the resulting bound at m = 1425 is ≤ 4.7·10⁻⁶⁹ (arb, bounds_sq_v2.py).']
rep[159]=['3. The lifted partial-trace identity Ẑ = c_m(Tr BV^m − Tr BE^m), c_m = 1 − λ^{−m} (|c_m| ≤ 1), by TRACE-197 (Line F F1) [P, cited]: its',
          '   hypotheses hold (ρ = 0.85 > 0.6036 (V), > 0.1036 (E); β > 0; ĝ superexponential; |C| = c₀ exactly so the α-condition is identical);']
rep[160]=['   the state factor is a finite monomial matrix and B is rank one in state space, so the identity holds termwise per word (as in TRACE-207).',
          '   Checks (B8): referee brute force over all 5⁹ words at Nmax = 2: agreement 1e−12…5e−14; full alphabet at m = 9: rel 1.1e−8.',
          '4b. Relevance to Dev: Σ_{t∈M}|Δ_t|² ≤ Σ_{t≠0}|Δ_t|² = dΣ|δ_u|² (Parseval, Δ₀ = 0).']
rep[165]=['Arithmetic is done in arb (`cert/bounds_sq.py` v1; `cert_v2/bounds_sq_v2.py` v2 with outward-rounded printing, sha in cert_v2/logs/SHA256_v2.txt), with JSON inputs padded by (1+2⁻⁴⁰).']
rep[167]=['* Only the SQUARE part of the d = 7 remainder is covered, for ρ = (±2,8) and m ≡ 3 (mod 6), and it is < 0.01 only for m ≥ 321.']
rep[168]=['* The other 7 operator cases are covered by EXACT symmetry (Session 4, S4.1); a direct certificate of the transferred case m = 15, a = −2,']
rep[169]=['  class 1:3 reproduces F = 0.356981 (V) and 0.013833 (E) (cert2/).']
rep[170]=['* The CROSS term 2εRe(Z̄_ρδ₀) is NOT controlled. Its required radius 1.26038 is below the true value 1.2837 [N; counting cert S4.2].']
rep[172]=['* The .npy Galerkin matrices were deleted after each run. R6: the referee\'s byte-identical regenerated V_1_3/E_1_3 matrices in',
          '  /workspace/audit/lineI/data/ are the designated stored copy (sha == provenance: cert_v2/logs/R6_stored_matrices.txt). Others regenerate deterministically: run']
rep[178]=['For d = 7 its cross part grows relative to φ like (μ·r_tw/√λ)^m = (1.915473·1.28371/2.414214)^m = 1.0187^m [float rates]. Numerically (zpred, m = 9..123):']
rep[179]=['* |Dev_7|/(mφ) is up to 0.021 for m = 21..45 (larger ρ; (−2,8): 0.0007 at m = 33, 0.003 at m = 45), with oscillating sign.']
rep[180]=['* The Dev_7/(m²h) envelope is 1–4·10⁻⁴ on m = 33..123 (flat: the data do NOT show the growth; predicted ×1.1 over 21..123).']
rep[181]=['* Extrapolated (contribution to W′/m ~ 1.0187^m/m): ≈ 0.2–0.3 at m ≈ 300, ≈ 1 at 400, ≈ 6–8 at m ≈ 500.']
rep[183]=['So frozen R′ is expected (heuristically) to fail (W′/m not → 0) along m ≡ 3 (mod 6) from about m ≈ 300–400 on. **Status: heuristic.**']
rep[184]=['It relies on: no compensation by the bulk, by W′_A or by other levels/the (±2,16) members (not modelled); no systematic cancellation between']
rep[185]=['the two ρ (partial cancellation seen at m = 33, 51, 105); a nonvanishing leading twisted coefficient (plausible: max|Ẑ|^{1/m} → 1.2837 observed;',
          'not certified).  This is NOT a disproof under TRACE-206\'s closure condition; TRACE-206 stays OPEN, R′_A is a proposal for the maintainers.']
rep[186]=['**Amendment (precise, proposal).** Keep the frozen P*, Z_ρ, levels d | h with 1 < d ≤ √h, the members M_d(ρ), n_d, the inclusion rule']
rep[190]=['**Conjecture R′_A (conjectured):** W′^A_m = o(m).']
rep[198]=['* [P] Prop I2′ per-member Gauss-sum formula; Ẑ symmetries (±λ) with the cyclic-invariance proof; case reduction; P ≡ y′Nm mod 2h; Prop I8 (one-sided, hypotheses explicit);']
rep[199]=['  Lemma I5′ (corrected). [assessment] Routes A/B/C, barrier note.']
rep[200]=['* [CA] Theorem I6 v2 (square term for d = 7, ρ = (±2,8), m ≡ 3 (mod 6); < 0.01 for m ≥ 321).']
rep[201]=['* [N] r_tw = 1.28371 > 1.26038 (counting part being certified, S4.2); zpred table m ≤ 123; lifted identity (referee 1e−14 / 1.1e−8); halo O(1) in F units.']
rep[202]=['* [C]/heuristic: frozen R′ expected to fail for m ≳ 300–400 (extrapolation; TRACE-206 open). Conjectured: R′_A; W′^A = O(1) (weak evidence).']
out=[]
for i,l in enumerate(L,1):
    out.extend(rep[i] if i in rep else [l])
s='\n'.join(out)
s=s.replace('# Line I — averaging','# Line I (REPORT v2) — averaging',1)
open('/workspace/bgs-lineI/REPORT_v2.md','w').write(s)
