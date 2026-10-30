# Line I (REPORT v2) — averaging across residues for Conjecture R′ (kicked quantized cat map S=[[3,4],[2,3]])
Status v2: 2026-10-31 (UTC+5), Sessions 1–4 with referee fixes B1–B9, R1–R7 applied (referee report /workspace/audit/lineI/REPORT.md).
REPORT.md (v1) is kept unchanged for provenance. Numbers are double-precision floats (NOT interval-certified) unless marked;
quoted values are rounded outward / to the displayed digits. Python: /workspace/bgs-derand/phase3/venv/bin/python.

## 0. Bottom line
* An unconditional proof of R′ (W′ = o(m)) was NOT obtained. I believe it is equivalent in difficulty to a bulk
  off-diagonal / weighted-equidistribution statement that current tools (large sieve, Kloosterman/Weil) do not reach
  (§4 explains why each route fails quantitatively).
* Obtained: (i) an exact, proved dilation-coset L² law (Prop I2; algebraic core Lean-checked) that converts the frozen-R′
  dilation term into explicit twisted transfer-operator traces, closed numerically to 2.6e-8; (ii) a precise
  reduction R′ ⇐ (E″)+(T″)+(D) (Thm I4, quantifiers fixed) with a Fourier lemma (I5′; the old "diagonal invisibility" is withdrawn); (iii) a full empirical
  decomposition of W′ at m=17: on the "rest" set (85% of residues) the mean of |Z|²/RMT is 0.999 [N], and W′ lives on explicit
  near-resonant families ("resonance halo") and low heights, each ≈ O(1) in F units.
* Main risk found for the FROZEN R′ (TRACE-206): its dilation main term grows like ~1.52^m, so the relative error of
  the dilation members must decay faster than 1.52^{-m}; at m=15 the frozen definition is off by +0.24·m in W′
  (d=41 members +15%, d=287 +37%). This is the most likely place where frozen R′ could fail as stated.

## 1. Statements, classified  ([P]=proved on paper, [L]=Lean-checked, [N]=numerically verified, [C]=conjecture)
**Prop I1 (relative phase split) [P, from lineG G1; N].** For a resonant ν0=ν_ρ and δ, Z(ν0+δ)=Z_ρ·σ̂_ρ(δ), σ_ρ the
(complex) resonant measure pushed to P mod 2h. Dilations = σ̂ at δ∈(2h/d)Z; the halo = small rational δ.

**Prop I2 (dilation-coset L² law) [P; algebraic core L; N to 1.5e-12].** d prime, d∥h, ε=(2/d).
W(γ)=Σ_{α_n≡γ mod d} w(n), w=Φ̂·e(−ν0P/2h), W_u=Σ_{Nmγ≡u}W(γ), Z_t=Σ_γ W(γ)e(−t·Nmγ/d) (= Z(ν0+2hj/d), t=jy′).
(a) Σ_t|Z_t|² = dΣ_u|W_u|²; (b) N(u)=d−ε (u≠0), N(0)=d+(d−1)ε; with δ_u=W_u−Z_0N(u)/d² (Σδ_u=0):
(c) Σ_u N(u)δ_u = εdδ_0, Σ_u N(u)² = d³+d²−d;
(d) Σ_{t≠0}|Z_t|² = |Z_0|²(1/d−1/d²) + 2εRe(Z̄_0δ_0) + dΣ_u|δ_u|².
δ's are the twisted sums Ẑ(β)=Σ_n w(n)e(Tr(βα_n)/d), i.e. traces of the G2 operator with the kick translated by
Tr(βλ^i)/d (period ord_d λ | m).
Congruence [P] (R3): P(n) ≡ y′Nm(α_n) (mod 2h), since Nm(α_n) = Σ_{i,j} n_i n_j x_{|i−j|} (because λ^{−d} = λ̄^d) and
ψ(d) = y′x_d − 2h y_d ≡ y′x_d (mod 2h). (Also 0 numerical failures, m=9,15,17.)  R5: for odd m every prime d | h_m splits,
since h² + 1 = 2y′² gives (2/d) = 1; so ε = +1 always and the inert branch of (b) is vacuous here.
 - Paper proof: finite Fourier analysis on (Z/d)², norm counts of a split/inert prime.
 - Lean: lean/LineI.lean (cross_term, sum_N_sq, coset_decomp, norm_count_7, norm_count_23_zero [zero count only]), 0 errors,
   no sorry/native_decide, axioms propext/Classical.choice/Quot.sound only (logs/lean_LineI.out). The Fourier step
   (a) and the identification Z_t=Z(ν0+2hj/d) are paper+numerics, not Lean.
 - Numerics: code/verify_coset.py → logs/verify_coset.log (m=5 d=41, m=9 d=7, m=11 d=23, m=7 d=239; max err 1.5e-12).
 - Twisted-trace closure: code/dilpred.py → logs/dilpred_d7.log. m=9, ρ=(2,8): predicted members from 49 twisted
   G2 traces agree with class sums to 2.6e-8 relative; |Z_0|²=30042.05, main/member 613.10; over ALL six t ≠ 0 (this includes the one
   NON-UNIT dilation j = 2, which is not a member of M_7(ρ)) cross 877.61, square 319.51; over the 5 MEMBERS Dev = 900.47, i.e. relative
   excess +0.2937 (matches dil.log) (B3).  m=15,21,27: done in Session 3 (zpred).
 - Heuristic corollary [C]: frozen dilation term is o(1) relative iff r_tw<√λ/μ≈1.26038 (cross) and r_tw<λ^{1/4}
   ≈1.5538 (square), r_tw = spectral radius of the twisted operators.

**Thm I4 (reduction) [P, elementary] (B5: quantifiers fixed).** All sums are over UNITS ν mod 2h, normalised by 1/φ(2h).
Fix ONE function Y(m) → ∞ and put K_m = {Λ: y(Λ) ≤ Y(m)}.  If (E″) (1/φ(2h))Σ_{ν unit: Λ_ν∈K_m}(|Z_ν|²−RMT_m) = o(m) for THIS
sequence K_m (uniformity in the growing compacta, not merely for each fixed compact K); (T″) cusp control: the same sum over Λ_ν in
y ≥ Y(m), minus the explicit resonance sum, is o(m) (same Y(m)); (D) the dilation remainder (Prop I2 cross+square terms, summed over levels) is o(m),
then R′ holds.  Alternative sufficient hypothesis (DF1: sufficient, not equivalent): (T″) for EVERY Y(m) → ∞ and (E″) for each fixed K, with a diagonal choice of Y(m) growing
slowly enough.  (Trivial partition of residues by shape; stated to isolate what must be proved.)

**Lemma I5′ (Fourier expansion of weighted horocycle sums) [P] — corrected, see theory_E2_v2.md (B6).** For ALL ν mod 2h:
Σ_ν|Z_ν|² f(z_ν) = 2h Σ_k c_k(1/2h) C(k), C(k) = Σ Φ̂(n)Φ̂(n′)‾ 1[P(n)−P(n′) ≡ k] (sign fixed: c_{[P(n)−P(n′)]}). For UNITS ν the
pair (n,n′) carries the Ramanujan sum c_{2h}(k−P(n)+P(n′)).  The diagonal class P ≡ P′ contributes C(0)× the UNWEIGHTED horocycle sum of f
(it meets every c_{2hj}, not only c_0), so it is not invisible: it needs an equidistribution input (cite with rate) and C(0) = O(m).

**Empirical facts [N] (k1 kick, η=2):**
* W′_act/m, m=7..17: −1.226, −0.819, −0.314, −0.041, +0.229, +0.092 (reproduces lineG). Full kick m=11,13: −0.332, −0.033.
* m=17 decomposition of W′/m=+0.092: low-height/broad-dilation +0.040, halo(θ≈±1/2) +0.048, halo(±1/4,±3/4) +0.016,
  θ≈0 −0.008, rest −0.004.  "Rest" (85% of residues) mean |Z|²/RMT: 0.722, 0.865, 0.948, 1.019, 0.999 (m=9..17).
* Halo window |θ|∈0.5±0.1: W′/m +.073,+.068,+.062,+.048 (m=11..17); halo·m ≈ 0.80,0.88,0.93,0.82 (≈O(1) in F units);
  concentrated on 8|b and small e=b−4|a|≡0 mod 8 (excess at fixed e grows with m: e=8: 4.3,6.1,9.3,12.6).
* Shape space: unweighted Hecke points ≈ Haar (rms z 0.96); weighted local means on y<3 have cell sd 0.043/0.013/0.018
  at m=17 ≈ noise; all structure at y≥3 (cusp), φ∈[75°,105°) (directions (1,4),(1,8)) = halo.
* Low-height excess decays: ℓ∈[4,8): .137,.099,.066,.055,.034 (m=9..17).
* Dilation deviation act−main (W/m): m9 .080, m11 .004, m13 .006, m15 .240, m17 .0015.
**[C] (weak evidence):** W′ = O(1) in F/2m·m units, i.e. stronger than R′; bulk = RMT; all deviation from explicit families.

## 2. Failed routes and why
1. Large sieve / Kloosterman / Weil: ℓ¹ mass of Φ̂ over words ~2.36^m vs modulus h~2.414^m; savings √h are eaten,
   bound is exponentially worse than trivial-needed.
2. Random-phase / Gaussian kick model: entropy H(|J_n(1.8)|²)≈1.52 > log√λ≈0.881 ⇒ E F exponentially large — the model
   diverges, so no "average over kicks" proof.
3. Averaging over k (Cauchy–Schwarz) gives nothing for primitive residues.
4. Per-operator spectral gap: Weyl constants b^A ≫ λ^{m/4} (lineH §1.2 obstruction) — same obstruction here.
5. Halo is NOT a generalized 1/d′² dilation law (halo4: normalized excess grows with d′); no closed formula found.
6. η-window averaging needs fine joint equidistribution of (P mod 2h) — equivalent to (E″).
7. Full-kick m=9,15 not decomposed (virtual primaries not handled in base.py).

## 3. Referee files (/workspace/bgs-lineI)
NOTES.md (chronological log); code/base.py (data, frozen TRACE-206 mask), strat.py, dil.py, halo*.py, theta.py,
shape.py, verify_coset.py, twist.py, dilpred.py; logs/*.log/json; lean/LineI.lean + logs/lean_LineI.out.
Lean compile: cd /workspace/bgs-int/BGS/formalization && lake env lean /workspace/bgs-lineI/lean/LineI.lean (~75 s).

## 4. What R′ would give / what next
R′ would say: the mean of |Z_ν|² over units equals the RMT value up to an explicit finite resonance sum and o(m),
i.e. all departures from random-matrix (BGS) behaviour of this map at time m are the explicit arithmetic resonances
(dilations of P*), and generic residues are RMT. Next steps: (1) finish dilpred m=15,21,27 to test whether frozen
dilation error decays faster than 1.52^{-m} (decides whether frozen R′ must be redefined with actual dilation
members); (2) bound r_tw for twisted operators (d=7: ord_7 λ=3, verified) — a computable, provable target; (3) attack (E″)
on compacta as an off-diagonal problem, using Lemma I5.

---
# Session 3 (2026-10-30, 20:36–22:xx UTC+5): steps (1) dilation decay verdict, (2) certified twisted radii, (3) (E″)

## S3.0 Bottom line
1. **Frozen R′ (TRACE-206) [heuristic, B9]: it is expected (heuristically) not to survive asymptotically; we propose an amendment.** For d = 7, the relative error of
   the dilation members decays like (r_tw/μ)^m = (1.28371/1.915473)^m = 0.6702^m, which is SLOWER than the required 1.52^{-m}
   (0.6579^m). Hence the frozen d = 7 remainder is expected to contribute Dev/(mφ) ~ C·1.0187^m/m to W′/m (B9b: /m, not /m²) along m ≡ 3 (mod 6), with oscillating sign:
   numerically |·| up to 0.021 for m = 21..45 (larger ρ; (−2,8) gives 0.0007 at m=33, 0.003 at m=45), Dev/(m²h) envelope ≈ 1–4·10⁻⁴ flat on m = 33..123.
   The data m ≤ 123 do NOT show the growth (predicted change over 21..123 only ×1.1); the extrapolation (≈ 0.2–0.3 at m ≈ 300, ≈ 1 at 400,
   ≈ 6–8 at 500; referee envelope fit e^{0.0190}) rests entirely on r_tw = 1.2837 > 1.26038 (1.9% margin). Session 4: the counting
   statement r_tw > R is being certified (dom/, see S4.2); the coefficient is NOT certified. If it holds, frozen R′ would be expected to FAIL
   (W′/m not → 0) at m of a few hundred. Not a proof, and NOT a disproof under TRACE-206's closure condition: missing are (i) c(β) ≠ 0,
   (ii) the (±2,16) d = 7 members and all other levels (only (±2,8) at d = 7 modelled), (iii) partial cancellation of the two ρ
   (seen e.g. at m = 33, 51, 105), (iv) no compensation by the bulk / W′_A.  TRACE-206 stays OPEN; R′_A is a proposal for the maintainers.
   **Amendment R′_A (precise).** Keep P*, levels, inclusion rule and members M_d(ρ) as frozen, but replace the main term by the
   actual member values:
     Res^A_m = (1/φ) Σ_ρ [ (|Z_ρ|² − RMT_m) + Σ_{d incl.} Σ_{ν∈M_d(ρ)} (|Z_ν|² − RMT_m) ],  W′^A_m = F_m − RMT_m − Res^A_m,
   Conjecture R′_A: W′^A_m = o(m). It is equivalent to an explicit statement: by Prop I2′ (below), for every member
     |Z_ν|² = |Z_ρ|²/d² + 2Re(conj(ω_t Z_ρ/d) Δ_t) + |Δ_t|²,  Δ_t = d^{-2} Σ_{β≢0 (d)} Ẑ_d(β) G_t(β),
   where Ẑ_d(β) are twisted transfer-operator traces (kick translated by Tr(βλ^i)/d, period ord_d λ). So Res^A is explicit
   through d²−1 twisted traces per level. Equivalent to W′_act of Line G. (The frozen version = dropping the Δ terms.)
2. **Certified [CA] (all 8 classes done 00:04 UTC+5 Oct 31; Theorem I6 in S3.4).** Twisted operators for ρ = (2,8), d = 7, m ≡ 9 (mod 24):
   spectra of the lifted V lattice in |z| < 1.45 and E lattice in |z| < 1.0 (Session 4: all m ≡ 3 (mod 6), ρ = (±2,8), by exact symmetry). Consequence: the dilation SQUARE term is
   exponentially small relative to φ(2h) (rate (1.45²/√λ)^m ≤ 0.87089^m). The CROSS-term condition r_tw < 1.26038 is FALSE
   numerically (1.2837), so it cannot be certified. Lower-bound (counting) certification: Session 4, S4.2.
3. **(E″): no rigorous result.** Three routes analysed; each shows a specific inequality chain fails [assessment]. Halo: O(1) in F units [N].

## S3.1 Step (1) details [N]
* Fast predictor `code/zpred.py` on the 16 reachable automaton states (`code/reach.py`: reachable = co-reachable = 16 of 64, invariant).
  Matches exact class sums at m = 9 (2.6e-8) and m = 15 (8e-9). Output `logs/zpred_K40.log`, `logs/zpred_d7_K40_r2.6_L10.json`.
* `code/twrad2.py`, `code/twradq.py`: 3-step twisted products Q_β (single disc). All 8 operator cases (m = 9, 15, 21, 27; ±) have
  IDENTICAL spectra. μ = 1.915473 (×2), next untwisted 1.053852 (the 1.2517 seen on 64 states is outside the reachable subspace).
  r_tw over the 8 classes (β mod ±λ): 1.28371 (1:3), 1.28360 (2:1), 1.26243 (0:1), 1.16712 (1:2, 1:5), 1.11353 (0:3),
  0.99735 (1:0), 0.89666 (0:2). Stable in K (30/40/50) and ρ (2.2/2.6/2.9). Warning: L = 12 in a single disc gives ARTEFACTS
  (radius 26); use the lift.
* maxβ |Ẑ(β)|^{1/m}: 1.208 (m=9) → 1.2765 (m=123), converging to 1.2837.
* Symmetries [P] (B4): λ^m = x_m + 2y_m√2 with x_m = 2h²+1, 2y_m = 2hy′, so λ^m ≡ 1 (mod 2h); hence x_{m−d} ≡ x_d (mod 2h) and P is a
  cyclic quadratic form mod 2h (Φ̂ is cyclic too). With λ^m ≡ 1 (mod 7) (3 | m) the cyclic shift multiplies α_n by λ: Ẑ(λβ) = Ẑ(β).
  Ẑ(−β) = Ẑ(β): ĝ(−n) = ĝ(n) (iⁿJ_n even), P(−n) = P(n), α_{−n} = −α_n.  ⇒ 8 classes (referee: 8 orbits of size 6, union 48).
  The norm-zero lines x ≡ ±3y (mod 7) are self-dual; the top classes are off the cone (so they enter δ₀ with weight −1/d²).
* Prop I2′ (per member, exact) [P]: d odd, d | h, gcd(t,d) = 1:
  Z_t = ω_t Z₀/d + Δ_t with |ω_t| = 1 (ω_t = G_t(0)/d) and |Δ_t| ≤ d^{-1} Σ_{β≠0}|Ẑ(β)|, because the 2-variable Gauss sums
  G_t(β) = Σ_γ e(−(t Nmγ + Tr βγ)/d) all have |G_t(β)| = d (Nm nondegenerate, d coprime to 8). This holds for composite d (287) too.
* Barrier note [assessment] (B9): uniform-in-d control of (D) via operator bounds needs square-root cancellation in Ẑ_d for d up to ≈ |Z_ρ|/√(4m); the diagonal
  alone gives Σ_β|Ẑ_d(β)|² ≈ d². Fixed-d theorems are feasible; uniform ones are not reachable by operator bounds.

## S3.2 Step (2): certificates [CA]
* Builder `cert/certG_build.py` adapts Line H `cert49_build.py` (sha 2b5d693f…): letters x = n; multiplier C = −4a c₀/b (= −c₀ for (2,8));
  k1 kick ĝ(n) = iⁿJ_n(1.8) in arb with the Line F Bessel tail; finite factor = exact monomial matrices (`cert/gstates.py`) on the
  16 reachable states × 3-cycle carrying the twist e(n·τ_i), τ_i = Tr(βλ^i)/7; full alphabet (|n| ≤ 150 explicit + analytic tail).
* Spectral step: Line H `rig_spec.py` v4 UNCHANGED (sha f346e22c…, identical to the referee-fixed archived version: zgemm constant
  √2·γ_{2n+2}, upward padding (1+2⁻⁴⁰) of JSON-read bounds, per-run provenance/code sha256 in each output JSON).
  Hashes of this run: `cert/logs/SHA256_run_sq.txt`.
* Validation: lifted float operators reproduce Ẑ: Ẑ = Tr(B V^m) − Tr(B E^m), B = I⊗|e_(0,0)⟩⟨1_{i=0}| (`code/liftchk.py`, 1e-6 at m = 9,
  5 classes + untwisted). The rigorous core (K = 16) partial trace reproduces Ẑ(2,0) at m = 9 to 1e-4; top |eig| 1.28371 (×3, cube roots).
* Case reduction [P] (R4): h + y′√2 = (1+√2)^m and k ≡ 3h⁻¹ (mod 8); the finite factor depends on m only through (k, ψ₀, ψ₁) mod 8 (ψ₁ = 3y′ − 2h),
  which are functions of (h, y′) mod 8; so the operator depends only on (1+√2)^m mod 8 (period 8 in m since (1+√2)^8 ≡ 1 mod 8). E.g. m ≡ 9 (24) ⇒ m ≡ 1 (8) ⇒ (h,y′) ≡ (1,1)
  (mod 8) ⇒ k ≡ 3, ψ₀ = 1, ψ₁ ≡ 1.  7 | h ⟺ m ≡ 3 (mod 6): (1+√2)³ ≡ 5√2 (mod 7), so (1+√2)⁶ ≡ 1 and the rational part h_m ≡ 0 (mod 7)
  exactly for m ≡ 3 (mod 6) (check of the 6 residues).  Verified for m < 700 (referee code/cases.py).
* Bound chain (`cert/bounds_sq.py`, arb): sup_{|z|=R}‖(z−L)⁻¹‖ ≤ G/(1−F); ‖L^n‖ ≤ R^{n+1}G/(1−F); |Tr(BL^m)| ≤ 4‖L‖₁R^mG/(1−F);
  d Σ_u|δ_u|² ≤ ((2d−1)/d)·Σ_{β≠0}|Ẑ(β)|² ≤ (13/7)·48·max|Ẑ|²; φ(h) ≥ h/(e^γ lnln h + 2.50637/lnln h) (Rosser–Schoenfeld).
* Status per class: see `cert/logs/run_sq.progress` and S3.4.

## S3.3 Step (3): (E″) as an off-diagonal problem — see `theory_E2.md` (Routes A/B/C, Prop I8, halo numbers).

## S3.4 Theorem I6 (d = 7 square term) [CA], all 8 classes certified (00:04 UTC+5, 2026-10-31)
**Setting.** k1 kick (ĝ(n) = iⁿJ_n(1.8), full alphabet), ρ = (2,8), m ≡ 9 (mod 24) (so 7 | h_m and the G2 operator case is fixed),
d = 7, Ẑ(β) = Σ_n Φ̂(n)e(−ν_ρP(n)/2h)e(Tr(βα_n)/7), δ_u as in Prop I2.
**Certificates** (`cert/logs/{V,E}_<class>_rest.json`, rig_spec v4 sha f346e22c…, builder sha in `cert/logs/SHA256_run_sq.txt`):
for every class β ∈ {1:3, 2:1, 0:1, 1:2, 1:5, 0:3, 1:0, 0:2} (representatives of (Z/7)²∖0 mod ±λ),
the lifted cyclic V operator has spectrum in |z| < 1.45 (rig_spec quantity F (at radius R) ≤ 0.357 < 1, decided in arb; also at R = 1.5, 1.55),
and the E operator has spectrum in |z| < 1.0 (F = 0.0138 at R = 1.0).  (R7: "F·R" in v1 meant F evaluated at radius R, Line H notation F_R.)
**Theorem I6 (v2).** For all m ≡ 3 (mod 6), ρ ∈ {(2,8), (−2,8)} (Session 4: exact intertwiners, sym/) and all β ≢ 0 (mod 7):
  |Ẑ(β)| ≤ 6.769·10⁶ · 1.45^m + 6.859·10⁴     (outward rounded; exact CV = 6 768 179.601…, CE = 68 586.18…; B1),
and the dilation square term of level 7 satisfies
  7 Σ_u |δ_u|² / φ(2h_m) ≤ (13/7)·48·(6.769·10⁶·1.45^m + 6.859·10⁴)² · (e^γ lnln h + 2.50637/lnln h)/h ,
which is ≤ 0.01 for every such m ≥ 321 (0.004574 at 321; 0.01046 at 315) and decays like (1.45²/√λ)^m ≤ 0.87089^m (exact 0.8708840…).
(Table m ≡ 3 (mod 6), m ≤ 1425: cert_v2/logs/bounds_sq_v2.json; v1 table cert/logs/bounds_sq.json.) R1 tail, m ≥ 1425: (CV·1.45^m+CE)²
≤ (CV+CE)²·1.45^{2m}, h_m ≥ (1+√2)^m/3, lnln h ≤ ln m, 1/lnln h ≤ 1/lnln h_1425, and q^m(e^γ ln m + c) is decreasing since ln q + 1/(m ln m) < 0;
the resulting bound at m = 1425 is ≤ 4.7·10⁻⁶⁹ (arb, bounds_sq_v2.py).
**Proof chain.**
1. The certified resolvent bound gives ‖L^n‖ ≤ R^{n+1}G/(1−F).
2. Then |Tr(BL^m)| ≤ 4‖L‖₁R^mG/(1−F).
3. The lifted partial-trace identity Ẑ = c_m(Tr BV^m − Tr BE^m), c_m = 1 − λ^{−m} (|c_m| ≤ 1), by TRACE-197 (Line F F1) [P, cited]: its
   hypotheses hold (ρ = 0.85 > 0.6036 (V), > 0.1036 (E); β > 0; ĝ superexponential; |C| = c₀ exactly so the α-condition is identical);
   the state factor is a finite monomial matrix and B is rank one in state space, so the identity holds termwise per word (as in TRACE-207).
   Checks (B8): referee brute force over all 5⁹ words at Nmax = 2: agreement 1e−12…5e−14; full alphabet at m = 9: rel 1.1e−8.
4b. Relevance to Dev: Σ_{t∈M}|Δ_t|² ≤ Σ_{t≠0}|Δ_t|² = dΣ|δ_u|² (Parseval, Δ₀ = 0).
4. Class invariance [P] covers all 48 nonzero β.
5. Parseval plus N(u) ≤ 2d−1 bounds the square term by the Ẑ's.
6. Rosser–Schoenfeld bounds φ.

Arithmetic is done in arb (`cert/bounds_sq.py` v1; `cert_v2/bounds_sq_v2.py` v2 with outward-rounded printing, sha in cert_v2/logs/SHA256_v2.txt), with JSON inputs padded by (1+2⁻⁴⁰).
**Scope / caveats.**
* Only the SQUARE part of the d = 7 remainder is covered, for ρ = (±2,8) and m ≡ 3 (mod 6), and it is < 0.01 only for m ≥ 321.
* The other 7 operator cases are covered by EXACT symmetry (Session 4, S4.1); a direct certificate of the transferred case m = 15, a = −2,
  class 1:3 reproduces F = 0.356981 (V) and 0.013833 (E) (cert2/).
* The CROSS term 2εRe(Z̄_ρδ₀) is NOT controlled. Its required radius 1.26038 is below the true value 1.2837 [N; counting cert S4.2].
* Trusted components: arb/python-flint, IEEE binary64, classical OpenBLAS zgemm (same as Line H), Line F F1.
* The .npy Galerkin matrices were deleted after each run. R6: the referee's byte-identical regenerated V_1_3/E_1_3 matrices in
  /workspace/audit/lineI/data/ are the designated stored copy (sha == provenance: cert_v2/logs/R6_stored_matrices.txt). Others regenerate deterministically: run
  `certG_build.py V 9 2 2 0.85 30 3.5 150 40 <class> data/V_<c> 128 24` and `certG_build.py E 9 2 2 0.85 22 3.5 150 40 <class> data/E_<c> 128 18`,
  then check their sha256 against the provenance block of each rest JSON.

## S3.5 Proposed amendment of TRACE-206: Conjecture R′_A
**Reason.** Under the frozen definition, the level-d term uses the main term n_d|Z_ρ|²/d². Its error is Dev_d(ρ) = Σ_{ν∈M_d(ρ)}(|Z_ν|² − |Z_ρ|²/d²).
For d = 7 its cross part grows relative to φ like (μ·r_tw/√λ)^m = (1.915473·1.28371/2.414214)^m = 1.0187^m [float rates]. Numerically (zpred, m = 9..123):
* |Dev_7|/(mφ) is up to 0.021 for m = 21..45 (larger ρ; (−2,8): 0.0007 at m = 33, 0.003 at m = 45), with oscillating sign.
* The Dev_7/(m²h) envelope is 1–4·10⁻⁴ on m = 33..123 (flat: the data do NOT show the growth; predicted ×1.1 over 21..123).
* Extrapolated (contribution to W′/m ~ 1.0187^m/m): ≈ 0.2–0.3 at m ≈ 300, ≈ 1 at 400, ≈ 6–8 at m ≈ 500.

So frozen R′ is expected (heuristically) to fail (W′/m not → 0) along m ≡ 3 (mod 6) from about m ≈ 300–400 on. **Status: heuristic.**
It relies on: no compensation by the bulk, by W′_A or by other levels/the (±2,16) members (not modelled); no systematic cancellation between
the two ρ (partial cancellation seen at m = 33, 51, 105); a nonvanishing leading twisted coefficient (plausible: max|Ẑ|^{1/m} → 1.2837 observed;
not certified).  This is NOT a disproof under TRACE-206's closure condition; TRACE-206 stays OPEN, R′_A is a proposal for the maintainers.
**Amendment (precise, proposal).** Keep the frozen P*, Z_ρ, levels d | h with 1 < d ≤ √h, the members M_d(ρ), n_d, the inclusion rule
|Z_ρ|²/d² ≥ 4m and RMT_m. Replace Res_m by
  Res^A_m = (1/φ) Σ_ρ [ (|Z_ρ|² − RMT_m) + Σ_{d incl.} Σ_{ν∈M_d(ρ)} (|Z_ν|² − RMT_m) ],
and set W′^A_m = F_m − RMT_m − Res^A_m.
**Conjecture R′_A (conjectured):** W′^A_m = o(m).

R′_A is explicit: by Prop I2′, each member value is |ω_tZ_ρ/d + Δ_t|² with Δ_t = d⁻²Σ_{β≢0}Ẑ_d(β)G_t(β), and the Ẑ_d(β) are
twisted transfer-operator traces. It coincides with Line G's W′_act. Frozen R′ and R′_A differ exactly by Σ_{ρ,d}Dev_d(ρ)/φ.
**Weaker alternative (R′_B).** Keep the main term, but add the explicit twisted correction for each fixed prime d ≤ D₀. This is
equivalent to R′_A whenever the remaining large levels are negligible, which is not proved.

## S3.6 Classification summary (session 3)
* [P] Prop I2′ per-member Gauss-sum formula; Ẑ symmetries (±λ) with the cyclic-invariance proof; case reduction; P ≡ y′Nm mod 2h; Prop I8 (one-sided, hypotheses explicit);
  Lemma I5′ (corrected). [assessment] Routes A/B/C, barrier note.
* [CA] Theorem I6 v2 (square term for d = 7, ρ = (±2,8), m ≡ 3 (mod 6); < 0.01 for m ≥ 321).
* [N] r_tw ≈ 1.28371 (float); certified (Session 4, Theorem I9): r_tw > 1.262 > 1.260376 ≥ √λ/μ₀ with μ₀ ≥ 1.9154712 from Line F (BGS-TRACE-198) (DF3); zpred table m ≤ 123; lifted identity (referee 1e−14 / 1.1e−8); halo O(1) in F units.
* [C]/heuristic: frozen R′ expected to fail for m ≳ 300–400 (extrapolation; TRACE-206 open). Conjectured: R′_A; W′^A = O(1) (weak evidence).

## S3.7 Referee files (session 3)
* code/: zpred.py, twrad2.py, twradq.py, twrad2_lib.py, reach.py, params.py, liftchk.py, gstates.py
* cert/: certG_build.py, gstates.py, law.py, rig_spec.py (= Line H v4), bounds_sq.py, trchk.py, run_sq.sh
* cert/logs/: build*, *_rest.{log,json}, bounds_sq.{log,json}, SHA256_run_sq.txt, run_sq.progress
* logs/: zpred_K40.log, zpred_d7_K40_r2.6_L10.json, twrad2_*.log/json, twradq.log
* theory_E2.md; NOTES.md
