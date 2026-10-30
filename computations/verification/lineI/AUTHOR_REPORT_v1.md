# Line I — averaging across residues for Conjecture R′ (kicked quantized cat map S=[[3,4],[2,3]])
Status 2026-10-30 ~20:35 UTC+5. Numbers are double-precision floats (NOT interval-certified) unless marked;
quoted values are rounded outward / to the displayed digits. Python: /workspace/bgs-derand/phase3/venv/bin/python.

## 0. Bottom line
* An unconditional proof of R′ (W′ = o(m)) was NOT obtained. I believe it is equivalent in difficulty to a bulk
  off-diagonal / weighted-equidistribution statement that current tools (large sieve, Kloosterman/Weil) do not reach
  (§4 explains why each route fails quantitatively).
* Obtained: (i) an exact, proved and Lean-checked dilation-coset L² law (Prop I2) that converts the frozen-R′
  dilation term into explicit twisted transfer-operator traces, closed numerically to 2.6e-8; (ii) a precise
  reduction R′ ⇐ (E″)+(T″)+(D) (Thm I4) with a diagonal-invisibility lemma (I5); (iii) a full empirical
  decomposition of W′ at m=17 showing the bulk (85% of residues) is RMT to 0.1% and W′ lives on explicit
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
Tr(βλ^i)/d (period ord_d λ | m).  Uses P(n)≡y′Nm(α_n) mod h [N: 0 failures, m=9,15,17].
 - Paper proof: finite Fourier analysis on (Z/d)², norm counts of a split/inert prime.
 - Lean: lean/LineI.lean (cross_term, sum_N_sq, coset_decomp, norm_count_7, norm_count_23_zero), 0 errors,
   no sorry/native_decide, axioms propext/Classical.choice/Quot.sound only (logs/lean_LineI.out). The Fourier step
   (a) and the identification Z_t=Z(ν0+2hj/d) are paper+numerics, not Lean.
 - Numerics: code/verify_coset.py → logs/verify_coset.log (m=5 d=41, m=9 d=7, m=11 d=23, m=7 d=239; max err 1.5e-12).
 - Twisted-trace closure: code/dilpred.py → logs/dilpred_d7.log. m=9, ρ=(2,8): predicted members from 49 twisted
   G2 traces agree with class sums to 2.6e-8 relative; |Z_0|²=30042.05, main/member 613.10, cross 877.61, square
   319.51, relative excess +0.2937 (matches dil.log).  m=15,21,27 still running (pid 1544180) at report time.
 - Heuristic corollary [C]: frozen dilation term is o(1) relative iff r_tw<√λ/μ≈1.2603 (cross) and r_tw<λ^{1/4}
   ≈1.5538 (square), r_tw = spectral radius of the twisted operators.

**Thm I4 (reduction) [P, elementary].** If (E″) weighted Hecke equidistribution: for each compact K⊂SL2(Z)\SL2(R),
(1/φ(2h))Σ_{ν: Λ_ν∈K}(|Z_ν|²−RMT_m) = o(m); (T″) cusp control: the same over Λ_ν in the cusp y≥Y(m) minus the
explicit resonance sum is o(m); (D) the dilation remainder (Prop I2 cross+square terms, summed over levels) is o(m),
then R′ holds.  (Trivial partition of residues by shape; stated to isolate what must be proved.)

**Lemma I5 (diagonal invisibility) [P].** Σ_ν|Z_ν|² f(Λ_ν) = 2h Σ_{n,n′}Φ̂(n)Φ̂(n′)‾ c_{[P(n′)−P(n)]}(1/2h) for f
on shape space with Fourier coefficients c_k; diagonal pairs (P=P′) only meet c_0. Hence for cusp forms f
(c_0=0) the diagonal drops out and (E″) is purely an off-diagonal statement — that is the real content of R′.

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
1. **Verdict on frozen R′ (TRACE-206) [N + heuristic]: it does not survive asymptotically; amend.** For d = 7, the relative error of
   the dilation members decays like (r_tw/μ)^m = (1.28371/1.915473)^m = 0.6702^m, which is SLOWER than the required 1.52^{-m}
   (0.6579^m). Hence the frozen d = 7 remainder contributes ≈ C·1.0187^m/m² to W′/m along m ≡ 3 (mod 6), with oscillating sign:
   numerically |·| ≈ 0.007–0.021 for m = 21..45, Dev/(m²h) envelope ≈ 1–4·10⁻⁴ flat on m = 33..123 (the minimum of 1.0187^m/m²
   is near m ≈ 108), extrapolating to ≈ 0.3 at m ≈ 300 and ≈ 8 at m ≈ 500. The frozen R′ is therefore expected to FAIL
   (W′/m not → 0) from the d = 7 level alone, at m of order a few hundred. Not a proof: it needs the bulk to not cancel it and a
   rigorous lower bound on the leading twisted coefficient.
   **Amendment R′_A (precise).** Keep P*, levels, inclusion rule and members M_d(ρ) as frozen, but replace the main term by the
   actual member values:
     Res^A_m = (1/φ) Σ_ρ [ (|Z_ρ|² − RMT_m) + Σ_{d incl.} Σ_{ν∈M_d(ρ)} (|Z_ν|² − RMT_m) ],  W′^A_m = F_m − RMT_m − Res^A_m,
   Conjecture R′_A: W′^A_m = o(m). It is equivalent to an explicit statement: by Prop I2′ (below), for every member
     |Z_ν|² = |Z_ρ|²/d² + 2Re(conj(ω_t Z_ρ/d) Δ_t) + |Δ_t|²,  Δ_t = d^{-2} Σ_{β≢0 (d)} Ẑ_d(β) G_t(β),
   where Ẑ_d(β) are twisted transfer-operator traces (kick translated by Tr(βλ^i)/d, period ord_d λ). So Res^A is explicit
   through d²−1 twisted traces per level. Equivalent to W′_act of Line G. (The frozen version = dropping the Δ terms.)
2. **Certified [CA] (all 8 classes done 00:04 UTC+5 Oct 31; Theorem I6 in S3.4).** Twisted operators for ρ = (2,8), d = 7, m ≡ 9 (mod 24):
   spectra of the lifted V lattice in |z| < 1.45 and E lattice in |z| < 1.0. Consequence: the dilation SQUARE term is
   exponentially small relative to φ(2h) (rate (1.45²/√λ)^m = 0.8709^m). The CROSS-term condition r_tw < 1.2603 is FALSE
   numerically (1.2837), so it cannot be certified. Lower-bound certification (dom mode) was not attempted.
3. **(E″): no rigorous result.** Three routes analysed, with explicit barriers (S3.3). Halo quantified: O(1) in F units.

## S3.1 Step (1) details [N]
* Fast predictor `code/zpred.py` on the 16 reachable automaton states (`code/reach.py`: reachable = co-reachable = 16 of 64, invariant).
  Matches exact class sums at m = 9 (2.6e-8) and m = 15 (8e-9). Output `logs/zpred_K40.log`, `logs/zpred_d7_K40_r2.6_L10.json`.
* `code/twrad2.py`, `code/twradq.py`: 3-step twisted products Q_β (single disc). All 8 operator cases (m = 9, 15, 21, 27; ±) have
  IDENTICAL spectra. μ = 1.915473 (×2), next untwisted 1.053852 (the 1.2517 seen on 64 states is outside the reachable subspace).
  r_tw over the 8 classes (β mod ±λ): 1.28371 (1:3), 1.28360 (2:1), 1.26243 (0:1), 1.16712 (1:2, 1:5), 1.11353 (0:3),
  0.99735 (1:0), 0.89666 (0:2). Stable in K (30/40/50) and ρ (2.2/2.6/2.9). Warning: L = 12 in a single disc gives ARTEFACTS
  (radius 26); use the lift.
* maxβ |Ẑ(β)|^{1/m}: 1.208 (m=9) → 1.2765 (m=123), converging to 1.2837.
* Symmetries [P]: Ẑ(λβ) = Ẑ(β) (cyclic shift; λ^m ≡ 1 mod 7), Ẑ(−β) = Ẑ(β) (ĝ even, P quadratic) ⇒ 8 classes.
  The norm-zero lines x ≡ ±3y (mod 7) are self-dual; the top classes are off the cone (so they enter δ₀ with weight −1/d²).
* Prop I2′ (per member, exact) [P]: d odd, d | h, gcd(t,d) = 1:
  Z_t = ω_t Z₀/d + Δ_t with |ω_t| = 1 (ω_t = G_t(0)/d) and |Δ_t| ≤ d^{-1} Σ_{β≠0}|Ẑ(β)|, because the 2-variable Gauss sums
  G_t(β) = Σ_γ e(−(t Nmγ + Tr βγ)/d) all have |G_t(β)| = d (Nm nondegenerate, d coprime to 8). This holds for composite d (287) too.
* Barrier note [P]: uniform-in-d control of (D) needs square-root cancellation in Ẑ_d for d up to ≈ |Z_ρ|/√(4m); the diagonal
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
* Case reduction [P]: h + y′√2 = (1+√2)^m and k ≡ 3h⁻¹ (mod 8), so the operator depends only on (1+√2)^m mod 8 (period 8 in m).
  7 | h iff m ≡ 3 (mod 6). The case m ≡ 9 (mod 24) is one fixed operator family (checked m < 80).
* Bound chain (`cert/bounds_sq.py`, arb): sup_{|z|=R}‖(z−L)⁻¹‖ ≤ G/(1−F); ‖L^n‖ ≤ R^{n+1}G/(1−F); |Tr(BL^m)| ≤ 4‖L‖₁R^mG/(1−F);
  d Σ_u|δ_u|² ≤ ((2d−1)/d)·Σ_{β≠0}|Ẑ(β)|² ≤ (13/7)·48·max|Ẑ|²; φ(h) ≥ h/(e^γ lnln h + 2.50637/lnln h) (Rosser–Schoenfeld).
* Status per class: see `cert/logs/run_sq.progress` and S3.4.

## S3.3 Step (3): (E″) as an off-diagonal problem — see `theory_E2.md` (Routes A/B/C, Prop I8, halo numbers).

## S3.4 Theorem I6 (d = 7 square term) [CA], all 8 classes certified (00:04 UTC+5, 2026-10-31)
**Setting.** k1 kick (ĝ(n) = iⁿJ_n(1.8), full alphabet), ρ = (2,8), m ≡ 9 (mod 24) (so 7 | h_m and the G2 operator case is fixed),
d = 7, Ẑ(β) = Σ_n Φ̂(n)e(−ν_ρP(n)/2h)e(Tr(βα_n)/7), δ_u as in Prop I2.
**Certificates** (`cert/logs/{V,E}_<class>_rest.json`, rig_spec v4 sha f346e22c…, builder sha in `cert/logs/SHA256_run_sq.txt`):
for every class β ∈ {1:3, 2:1, 0:1, 1:2, 1:5, 0:3, 1:0, 0:2} (representatives of (Z/7)²∖0 mod ±λ),
the lifted cyclic V operator has spectrum in |z| < 1.45 (F·R ≤ 0.357 < 1, decided in arb; also at R = 1.5, 1.55),
and the E operator has spectrum in |z| < 1.0 (F·R = 0.0138).
**Theorem I6.** For all m ≡ 9 (mod 24) and all β ≢ 0 (mod 7):
  |Ẑ(β)| ≤ 6.768·10⁶ · 1.45^m + 6.859·10⁴     (constants rounded up),
and the dilation square term of level 7 satisfies
  7 Σ_u |δ_u|² / φ(2h_m) ≤ (13/7)·48·(6.768·10⁶·1.45^m + 6.859·10⁴)² · (e^γ lnln h + 2.50637/lnln h)/h ,
which is ≤ 0.01 for every such m ≥ 321 and decays like (1.45²/√λ)^m = 0.87088^m. (The table up to m = 1425 is in
`cert/logs/bounds_sq.json`. Beyond that the bound is monotone decreasing, because 0.871^m·lnln-factor decreases.)
**Proof chain.**
1. The certified resolvent bound gives ‖L^n‖ ≤ R^{n+1}G/(1−F).
2. Then |Tr(BL^m)| ≤ 4‖L‖₁R^mG/(1−F).
3. The lifted partial-trace identity Ẑ = c_m(Tr BV^m − Tr BE^m) with |c_m| ≤ 1 holds termwise per word from Line F F1 [P, cited],
   and is checked numerically to 1e-6.
4. Class invariance [P] covers all 48 nonzero β.
5. Parseval plus N(u) ≤ 2d−1 bounds the square term by the Ẑ's.
6. Rosser–Schoenfeld bounds φ.

Arithmetic is done in arb (`cert/bounds_sq.py`, sha in SHA256_run_sq.txt), with JSON inputs padded by (1+2⁻⁴⁰).
**Scope / caveats.**
* Only the SQUARE part of the d = 7 remainder is covered, only for ρ = (2,8) and only for m ≡ 9 (mod 24).
* The other 7 operator cases (m mod 24, and ρ = (−2,8)) have numerically identical spectra and run with the same pipeline
  (`run_sq.sh` with m, a changed). They were not run.
* The CROSS term 2εRe(Z̄_ρδ₀) is NOT controlled. Its required radius 1.2603 is below the true value 1.2837 [N].
* Trusted components: arb/python-flint, IEEE binary64, classical OpenBLAS zgemm (same as Line H), Line F F1.
* The .npy Galerkin matrices were deleted after each run to save disk. They regenerate deterministically: run
  `certG_build.py V 9 2 2 0.85 30 3.5 150 40 <class> data/V_<c> 128 24` and `certG_build.py E 9 2 2 0.85 22 3.5 150 40 <class> data/E_<c> 128 18`,
  then check their sha256 against the provenance block of each rest JSON.

## S3.5 Proposed amendment of TRACE-206: Conjecture R′_A
**Reason.** Under the frozen definition, the level-d term uses the main term n_d|Z_ρ|²/d². Its error is Dev_d(ρ) = Σ_{ν∈M_d(ρ)}(|Z_ν|² − |Z_ρ|²/d²).
For d = 7 its cross part grows relative to φ like (μ·r_tw/√λ)^m = (1.915473·1.28371/2.414214)^m = 1.0187^m. Numerically (zpred, m = 9..123):
* Dev_7/(mφ) is 0.007–0.021 in absolute value for m = 21..45, with oscillating sign.
* The Dev_7/(m²h) envelope is 1–4·10⁻⁴ on m = 33..123.
* Extrapolated: ≈ 0.3 at m ≈ 300 and ≈ 8 at m ≈ 500.

So frozen R′ is expected to fail (W′/m not → 0) along m ≡ 3 (mod 6) from about m ≈ 300–400 on. **Status: heuristic.**
It relies on two things: no compensation by the bulk or by other levels, and a nonvanishing leading twisted coefficient
(this is plausible, since max|Ẑ|^{1/m} → 1.2837 is observed).
**Amendment (precise).** Keep the frozen P*, Z_ρ, levels d | h with 1 < d ≤ √h, the members M_d(ρ), n_d, the inclusion rule
|Z_ρ|²/d² ≥ 4m and RMT_m. Replace Res_m by
  Res^A_m = (1/φ) Σ_ρ [ (|Z_ρ|² − RMT_m) + Σ_{d incl.} Σ_{ν∈M_d(ρ)} (|Z_ν|² − RMT_m) ],
and set W′^A_m = F_m − RMT_m − Res^A_m.
**Conjecture R′_A:** W′^A_m = o(m).

R′_A is explicit: by Prop I2′, each member value is |ω_tZ_ρ/d + Δ_t|² with Δ_t = d⁻²Σ_{β≢0}Ẑ_d(β)G_t(β), and the Ẑ_d(β) are
twisted transfer-operator traces. It coincides with Line G's W′_act. Frozen R′ and R′_A differ exactly by Σ_{ρ,d}Dev_d(ρ)/φ.
**Weaker alternative (R′_B).** Keep the main term, but add the explicit twisted correction for each fixed prime d ≤ D₀. This is
equivalent to R′_A whenever the remaining large levels are negligible, which is not proved.

## S3.6 Classification summary (session 3)
* [P] Prop I2′ per-member Gauss-sum formula; Ẑ symmetries (±λ); case reduction (1+√2)^m mod 8, k ≡ 3h⁻¹ (mod 8); Prop I8 (one-sided);
  barrier statements for Routes A/B (theory_E2.md).
* [CA] Theorem I6 (all 8 classes; square term for d = 7, ρ = (2,8), m ≡ 9 (mod 24)).
* [N] r_tw = 1.28371 > 1.2603; zpred table m ≤ 123; the lifted identity at 1e-6; halo O(1) in F units.
* [C] Frozen R′ fails for m ≳ 300–400 (extrapolation); R′_A holds; W′^A = O(1).

## S3.7 Referee files (session 3)
* code/: zpred.py, twrad2.py, twradq.py, twrad2_lib.py, reach.py, params.py, liftchk.py, gstates.py
* cert/: certG_build.py, gstates.py, law.py, rig_spec.py (= Line H v4), bounds_sq.py, trchk.py, run_sq.sh
* cert/logs/: build*, *_rest.{log,json}, bounds_sq.{log,json}, SHA256_run_sq.txt, run_sq.progress
* logs/: zpred_K40.log, zpred_d7_K40_r2.6_L10.json, twrad2_*.log/json, twradq.log
* theory_E2.md; NOTES.md
