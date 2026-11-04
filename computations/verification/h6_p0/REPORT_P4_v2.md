# P4 v2 — round 4 after referee audit/p4 (fixes 1–6 applied) (2026-11-04/05, Europe/Berlin): H6 explicit p0, Lemma W, H1-bad obstruction
Tags: [P] proved here (given cited registry inputs) · [P-sketch] · [N] numerics · [C] conjecture/plan · [CA] arb ball arithmetic.
v2 changes vs v1: (1) e^{βRc} added to log K (βRc = 10 for 8V, 8.75 for 8E); (2) A_J ≤ 4/3; (3) Lemma I one-step structure [P]; (4) robust-variant wording corrected, u-normalisation stated in (C1); (5) unit renamed ε_u (ε = Bowen radius); (6) H1-bad labels. All p0 values below are from the v2 rerun (`logs/h6_p0.json`), restart-on-failure kept. Code `code/`, logs `logs/`. python-flint 0.9.0 (arb), 128-bit balls; every decision is a certified ball comparison.

## 0. Summary
- **(1) H6 / Theorem C' (8V, the binding family): one explicit p0 = 28,424,695** [P + CA, mod inherited N4 Λ, κ_F, N2 r_2, the u-normalisation of (C1) and h_p squarefree, §1.7].
  For every prime p ≥ 28,424,695 with h_p squarefree (Theorem C' assumes this), the 8V unit-point cross part at c = h_p is < T^{3p}.
  - Every constant is computed:
    - C_I ≤ 5.2535e8;
    - sup‖L_τ‖_{O1} ≤ 61.002;
    - Bowen modulus ω(ε) ≤ 2π·e^{6909.80}·ε/k at k = 4000;
    - log K(p) ≤ 31804.6 + 2 log p (includes log A_J ≤ log(4/3) and βRc = 10).
  - "Holds for all p ≥ p0" is proved by interval covering plus an analytic tail, not by a grid check.
  - Best k in [1000, 4000]: k = 4000. p0 decreases monotonically in k on the 7-point grid.
  - 8E: p0 = 3,934 (k = 1000). 16V/16E: **not done**.
- **(2) Lemma W [P]**: clean proof in §2.
  - [N, exact] For all 94 odd primes p < 500, every prime q < 10^8 dividing h_p (108 factors found by testing *all* 5,761,454 odd primes < 10^8) satisfies q ≡ ±1 (mod 2p). **0 violations.**
  - Full factorisations for 47 primes p ≤ 233: 0 violations, all h_p squarefree, ω ≤ 6.
- **(3) H1-bad:** no concrete decoupling was found, so the second-moment transfer operator was **not** attempted. The obstruction is stated precisely in §3.
- **Correction to P3:** P3 paired κ_F = 2966 with Λ = 1.9656353.
  - 2966 belongs to the N3 norm (Λ ≤ 1.965736). The N4 norm, which gives 1.9656353, has κ_F = 4036 (REPORT_N4_v2 l.52).
  - P4 uses 4036. The effect on p0 is about +130, since log(4036/2966) = 0.31 (§1.6).

## 1. H6 — explicit p0 for Theorem C' (unit points at h_p)
Registry: **BGS-TRACE-338** (conditional; record/claims.json).

### 1.1 The certified chain
Notation follows N2 Thm B/C, N3 Lemma I, Line L Lemma O1/OP_abs, and N2 Prop E. Fix F, k and the clamp a = 1:
- M = M_F(y) is the p-step cocycle;
- f_k = ‖P_k(y)‖²_HS (O1 space);
- φ = (1/k)log(1+f_k);
- Ŝφ = Σ_{0≤i≤p−k} φ∘T^i.

Steps, each [P]:
1. **Unit weights.** By Thm B, with |W| ≤ 2^{ω(h_p)}/h_p² for squarefree h_p:
   |unit part| ≤ 2^{ω(h_p)}·A_J·E_{G_p}|Tr(J M³)|, where A_J = Σ_F|a_F|‖J_F‖ ≤ 4/3 (§1.2b).
   Line F weight: Λ is certified in the Line F norm with weights e^{−β(|c|−Rc)_+}; P4 works with e^{−β|c|}. The two differ by ≤ e^{βRc} (Rc = K0 = 4 for V, K0 − ½ = 3.5 for E, `lineF/code/cert_lift.py` l.20; β = 2.5), and nothing in N3/N4 shows κ_F contains this factor, so it is charged explicitly: +10 (8V), +8.75 (8E) in log K.
2. **Schatten–Hölder.** |Tr(J M³)| ≤ ‖J‖·‖M‖_op·‖M‖²_HS.
3. **Operator norm.** ‖M‖_op ≤ C_Iκ_FΛ^{p−4} (Lemma I + N4 [CA]).
4. **Block split.** For each residue r < k, write M = Tail·B_{Q_r−1}⋯B_0·Head, with k-blocks starting at r + jk ≤ p − k. Then
   ‖M‖²_HS ≤ H_max⁴·Π_j f_k(T^{r+jk}y),
   where H_max = max_{ℓ<k} min(max(1,S)^ℓ, C_Iκ_FΛ^{ℓ−4} (ℓ ≥ 5)) and S = sup_τ‖L_τ‖_{O1}.
   The geometric mean over r gives ‖M‖²_HS ≤ H_max⁴·e^{Ŝφ}.
5. **Bowen step (new, §1.3).** E_{G_p}e^{Ŝφ} ≤ B_ε·e^{pω(ε)}·∫e^{Ŝφ}.
6. **Hölder over the k residues, T-invariance, Prop E.**
   ∫e^{Ŝφ} ≤ Π_r(∫Π_j(1+f_k∘T^{jk}))^{1/k} ≤ (x_max/x_0)·r_2^{p−k+1} ≤ r_2^p.
   - x_max/x_0 = 1 exactly: the rerun `code/r2_cert_x0.py` logs the Collatz–Wielandt vector at carry state (0,0).
   - The r_2 values equal N2's to every printed digit.
   - P3's "(1+sup f_k) Hölder leftover" is not needed, because positions i > p−k are dropped from Ŝφ.

So the unit part is ≤ T^{3p}·2^{ω(h_p)}·K(p)·κ^{−p}, where
- κ = T³/(r_2(k)Λ);
- log K(p) = log A_J + βRc + log(C_Iκ_F) − 4log Λ + 4log H_max + log B_ε + pω(ε), with log A_J ≤ log(4/3).

**Requirement:** ω(h_p)·log 2 + log K(p) < p·log κ.

### 1.2 Lemma I constant C_I [P]
**One-step bound.** It applies to any pair of spaces H(ρ_a,β_a) → H(ρ_b,β_b) and uses the structure stated in TRACE-294 / N3 §2.1:
- the multiplier is ≤ e^{2πκ_m|n|ρ_b};
- the sub-disc composition has θ = (ρ_b/λ + off)/ρ_a < 1 and costs (1−θ²)^{−1/2}, with off = ½ for V and 1/(2λ) for E. Both offsets are fixed by TRACE-197's radius conditions (quoted verbatim in TRACE-249: 1/(2ρ_V) + 1/λ = 0.838, 1/(2λρ_E) + 1/λ = 0.6005) and by TRACE-249's k-step dev values λ/(2(λ−1)) = Σ_{j≥0}½λ^{−j} (V), 1/(2(λ−1)) = Σ_{j≥1}½λ^{−j} (E); the multiplier has real disc centres (TRACE-222) and κ = C0 = 1/(λ−λ^{−1}) (TRACE-249);
- the weight ratio is ≤ e^{β_a/2 + (β_a/λ)|n|}, which needs β_a/λ ≤ β_b and uses |c_in| ≤ (|c_out|+|n|)/λ + ½ (`lineF/code/cert_lift.py` l.90);
- the Schur test gives the factor √6: rows have 1 entry per letter, columns ≤ ⌈λ⌉ = 6 (TRACE-294).
- H² composition: the image disc lies in D(c′, θρ_a) and sup_{θ-disc}|f| ≤ (1−θ²)^{−1/2}‖f‖_{H²}; all grid mids have θ < 1 and β_a/λ ≤ β_b (8V: θ = 0.850, 0.882, 0.524, 0.838). Verified by referee audit/p4 §3a.

Result:

  ‖L_τ‖_{a→b} ≤ √6·(1−θ²)^{−1/2}·e^{β_a/2}·Σ_n|J_n(1.8)|e^{(2πκ_mρ_b + β_a/λ)|n|},

uniformly in τ. The Bessel tail is bounded by (x/2)^n/n!.

**Two steps.** Factor through any admissible intermediate H(ρ_m,β_m); this is submultiplicative. Minimise over a 79×59 grid; every grid point is a valid bound.

**Lemma I.** ‖L_{k′−1}⋯L_0‖_{O1} ≤ N_2(F→O1)·‖L_{k′−3}⋯L_2‖_F·N_2(O1→F), so C_I := N_2(O1→F)·N_2(F→O1).

| family | N_2(O1→F) (mid ρ,β) | N_2(F→O1) (mid) | **C_I** | S |
|---|---|---|---|---|
| 8V | 19137.89 (0.80,0.05) | 27450.46 (0.75,0.45) | **5.2534398e8** | 61.00157 |
| 8E | 834.849 (0.30,0.10) | 880.082 (0.20,0.45) | **7.347355e5** | 12.65914 |

### 1.3 Bowen-ball modulus (Lipschitz in y) [P, given convention (C1)]
**(C1) [P, except the u-normalisation].**
- y ∈ K_ℝ/O^∨, with K = ℚ(√2) and the Tr-pairing.
- T is multiplication by λ, so the embedding coordinates (σ₁y, σ₂y) scale by (λ, λ^{−1}).
- f_k(y) = Σ_γ c_γ e(Tr γy), with γ = α_n − α_{n′} and α_n = Σ_j n_jλ^j.
- *Consistency checks.*
  - λ^p − 1 = ε^p·2h_p, so Fix(T^p) = (1/2h_p)O^∨/O^∨ and G_p = (1/h_p)O^∨/O^∨ has index 4, as in N2 Thm B.
  - On ℤ², take √2 ↦ [[0,2],[1,0]]. Then S = (1+√2)², and min|u·s| = 1/8 against covolume 1/(2√2).
- **Assumed (not verified): u = 1.** The word frequency is γ = Σ n_jλ^j·u, where u is the image of e_q in O^∨ (N2: Σ(A^T)^i k_i, k_i = n_i e_q). We take u = 1. A u ≠ 1 multiplies L′ by ≤ max|σ_i u|, i.e. changes log K by ≈ 2 log max|σ_i u| = O(1).

**(a) Lipschitz bound.**
- |Δe(Tr γ·)| ≤ 2π(|σ₁γ||Δ₁| + |σ₂γ||Δ₂|).
- |σ₁γ| ≤ Σ|v_j|λ^j and |σ₂γ| ≤ Σ|v_j|λ^{−j}, with |v_j| ≤ |n_j| + |n′_j|.
- Combine with |c_γ| ≤ Σ‖M_n‖_HS‖M_{n′}‖_HS and Lemma O1:
  - Σ_γ|c_γ|(|σ₁γ|λ^{−k} + |σ₂γ|) ≤ L′ := C_pair·Π_jA(τ_j)²·Σ_j 2(A₁(τ_j)/A(τ_j))(λ^{j−k} + λ^{−j}), where A₁(s) = Σ|n||J_n|e^{s|n|}.
  - |Δlog(1+f)| ≤ |Δf|.

**(b) Ball.** B_y = y + {|v₁| ≤ ελ^{−(p−1+k)}, |v₂| ≤ ε}.
- For 0 ≤ i < p: |Δ₁| ≤ ελ^{−k} and |Δ₂| ≤ ε.
- So ω(ε) ≤ 2πL′ε/k =: c₁ε. The λ^{−k} in the ball cancels the λ^k size of σ₁γ.

**(c) Disjointness.** If y ≠ y′ ∈ G_p have overlapping balls, then h_p(y − y′) ∈ O^∨ \ 0, so its norm is ≥ 1/8 in absolute value. But that norm is ≤ h_p²·4ε²λ^{−(p−1+k)} ≤ ε²λ^{2−k} < 1/8 for ε ≤ 0.14. Contradiction.

**(d) Constant.** covol(O^∨) = 1/(2√2) and λ^p/h_p² = 4/(1−λ^{−p})², so B_ε = λ^{k−1}/(2√2·ε²(1−λ^{−p})²).

**(e) Choice of ε.** Take ε* = 2/(pc₁), which is ≤ 0.14. Then
  log B_ε + pc₁ε* = (k−1)log λ − log 2√2 − 2log(1−λ^{−p}) + 2log(pc₁/2) + 2.
- **The Bowen loss is logarithmic in p**, so P3's "margin share for the Bowen term" disappears.
- 8V, k = 4000: log L′ ≤ 6909.80, log c₁ ≤ 6903.34, log sup f_k ≤ 6908.0, log H_max ≤ 2728.27.

### 1.4 The all-p proof [P] (`code/h6_p0.py`, `certify`)
**Lemma W (§2) bound.** ω(h_p) ≤ w_max(p) = max{w : (p−1)^w w! ≤ ε_u^p}, ε_u = 1+√2 (renamed from ε_0/ε to avoid the Bowen radius ε).

**Intervals.** For p ∈ [P₁, P₂]:
- w_max(p) ≤ w̄ = max{w : (P₁−1)^w w! ≤ ε_u^{P₂}}. This is computed by bisection on certified comparisons and is an upper bound.
- log K(p) ≤ K₁ + 2log P₂ − 2log(1−λ^{−P₁}).
- p log κ ≥ P₁ log κ.

**Covering.** [p0, 10^10] is covered by adaptive bisection: 389 intervals for 8V at k = 4000, with no failure. The pointwise test is not monotone near p0: `certify` takes the bisection point, and restarts from bad+1 whenever any point of the cover fails, until a full cover succeeds. The 8V bisection point is 28,424,535 (referee audit/p4 §2), but the final certified p0 is 28,424,695.

**Tail p ≥ X = 10^10.**
1. Suppose the requirement fails at some p ≥ X. Since K₁ > 0, (K₁ + 2log p)/p is decreasing, so ω ≥ c′p, where c′ = (log κ − (K₁ + 2log X − 2log(1−λ^{−X}))/X)/log 2 > 0.
2. Then w! ≥ (w/e)^w and Lemma W give log(p−1) + log(c′p) − 1 ≤ log ε_u/c′.
3. The left side is increasing in p, and it is certified to be > log ε_u/c′ already at X. Contradiction.

`tail_ok = true` in every row.

### 1.5 Results [P + CA, mod §1.7] (`logs/h6_p0.json`)
| k | r_2^{8V}(k) [CA] | log κ (lower) | log L′ | K₁ | **p0 (8V)** | w̄(p0) | p0 (8E) |
|---|---|---|---|---|---|---|---|
| 1000 | 1.0582753 | 0.0165265 | 1733.98 | 8057.6 | 1,145,752,970 | 27,306,195 | **3,934** |
| 1500 | 1.0558834 | 0.0187893 | 2596.62 | 12015.1 | 125,436,857 | 3,382,849 | 5,837 |
| 2000 | 1.0546895 | 0.0199206 | 3459.25 | 15972.8 | 55,920,993 | 1,584,039 | 7,738 |
| 2500 | 1.0539738 | 0.0205994 | 4321.89 | 19930.6 | 38,944,608 | 1,128,579 | 9,638 |
| 3000 | 1.0534969 | 0.0210520 | 5184.52 | 23888.5 | 32,577,677 | 954,922 | 11,537 |
| 3500 | 1.0531564 | 0.0213752 | 6047.16 | 27846.5 | 29,737,226 | 876,811 | 13,434 |
| **4000** | 1.0529012 | 0.0216177 | 6909.80 | 31804.5 | **28,424,695** | 840,567 | 15,331 |

- r_2 at k = 1500, 2500, 3000 and 3500 are new [CA] runs of the unchanged N2 certificate (`logs/r2_cert_x0.jsonl`).
- **Final (v2):** p0^{8V} = 28,424,695 (k = 4000) and p0^{8E} = 3,934 (k = 1000), confirming referee audit/p4 §2. v1 values (28,420,500 / 3,928) omitted e^{βRc} and used A_J ≤ 1. The bound holds for every prime p ≥ 28,424,695 (8V) and p ≥ 3,934 (8E) with h_p squarefree; 16V/16E are not covered.
- **Why p0 is this large.**
  - At p0, w̄·log 2 ≈ 582,500 against p0·log κ ≈ 614,400, while log K ≈ 31,800. So 95% of the margin is used by the worst-case 2^{ω(h_p)} from Lemma W (ω ≲ 0.03p).
  - With log K = 0, p0 would be ≈ 1.28e7 (P3).
  - Each +1 in log K moves p0 by about +400.
  - On 𝒫 (h_p prime, ω = 1), p0 ≈ 31,800/0.0216 ≈ 1.47e6 [P-arith from K₁ and log κ; not run separately].

### 1.6 Sensitivity (`logs/h6_variants.json`, 8V, k = 4000, each row fully certified)
| variant | Δlog K | p0 |
|---|---|---|
| base (v2) | 0 | 28,424,695 |
| κ_F × 1000 | 6.9 | 28,427,516 |
| robust Bowen ball (|v1| ≤ ελ^{−(p−1+k)}, |v2| ≤ ελ^{−k}) | 7051 | 31,238,038 |
| log K + 10^5 | 10^5 | 62,331,649 |

The robust ball removes the question of which embedding carries λ^j in the frequency γ (the frequency-embedding convention), not the direction of T: if T were ×λ^{−1}, one would swap v1 and v2 at the same cost. Its Lipschitz weight is ≤ the base weight (referee audit/p4 §3c).

### 1.7 Honest gaps in (1)
1. **[P] The one-step structure of Lemma I** follows from TRACE-197/249/294 and `cert_lift.py` (§1.2; referee audit/p4 §3a). V matches all three N3 numbers (θ = 0.9412, 0.507, e^{0.125+0.043|n|}); the E offset 1/(2λ) is fixed by TRACE-197/249.
2. **[P] A_J ≤ 4/3.** TRACE-266 and Lines I/J give Ẑ_ρ = c_m Σ_a c_a(case, ρ)·⅓[Tr V^m − Tr E^m], c_m = 1 − λ^{−m} ≤ 1, |c_a| = ½, 4 sectors; the read-out I_K ⊗ |0⟩⟨1| has norm 1 and commutes with ω-conjugation. So A_J ≤ 2/3 per sign ρ and ≤ 4/3 when ρ = (±2,8) are summed. log(4/3) is charged.
3. **Convention (C1)** is verified except the normalisation u = 1 of the image of e_q (assumed; O(1) in log K). The robust variant removes the frequency-embedding convention at a cost of +10% in p0.
4. **Not covered:**
   - 16V/16E: they need the I16 constants (multiplier c0/2, NS = 64), and their κ_F was not located;
   - squarefreeness of h_p, which is still open (Wieferich-type);
   - the other additive budgets of p_thr.
5. **The whole margin κ is used.** A margin fraction < 1 raises p0. It is one parameter in the code but was not run.
6. **Inherited [CA], not re-run:** Λ^{8V} ≤ 1.9656353, κ_F = 4036, Λ^{8E} ≤ 0.4915932, κ = 4.3e4 (N4). r_2 *was* re-run.

## 2. Lemma W
Registry: **BGS-TRACE-337** (proved; record/claims.json). Lean finite check: `formalization/Bgs/H6LemmaW.lean`.

### 2.1 Statement and proof [P]
**Lemma W.** Let ε = 1+√2, ε̄ = 1−√2, O = ℤ[√2], p an odd prime, and h_p = (ε^p + ε̄^p)/2.
If a prime q divides h_p, then q is odd and q ≡ ±1 (mod 2p). Hence:
- p ∤ h_p;
- the j-th smallest prime factor of h_p is ≥ pj − 1 ≥ (p−1)j;
- ω(h_p) ≤ w_max(p) := max{w : (p−1)^w·w! ≤ ε^p}.

*Proof.*
1. **q is odd.** h_0 = h_1 = 1 and h_n = 2h_{n−1} + h_{n−2}, so every h_n is odd.
2. **Unramified.** Let R = O/qO. Since q is odd and prime to the discriminant 8, R is F_q × F_q (q split) or F_{q²} (q inert).
3. **ε^{2p} = 1.** q | h_p gives ε^p = −ε̄^p in R. Multiplying by ε^p gives ε^{2p} = −(εε̄)^p = −(−1)^p = 1.
4. **ord(ε) ∈ {p, 2p}.** ε − 1 = √2 has norm −2 and ε² − 1 = 2ε has norm −4, both prime to q. So ε ≢ 1 and ε² ≢ 1, and ord(ε) | 2p is therefore p or 2p.
5. **p divides q ∓ 1.**
   - Split: R^× has exponent q − 1, so p | q − 1.
   - Inert: Frobenius x ↦ x^q is conjugation, so ε^{q+1} = εε̄ = −1. Then ord(ε) | 2(q+1), and since p is odd, p | q + 1.
6. **Conclusion for q.** q ∓ 1 is even and divisible by the odd prime p, so 2p | q ∓ 1. In particular q ≠ p.
7. **j-th factor.** The integers > 1 that are ≡ ±1 (mod 2p) are 2p−1, 2p+1, 4p−1, …. The j-th one is (j+1)p − 1 (j odd) or jp + 1 (j even), so it is ≥ pj − 1 ≥ (p−1)j. Distinct primes occupy distinct such slots.
8. **ω bound.** Π_{j≤w}(p−1)j ≤ h_p < ε^p, because |ε̄^p| < 1. ∎

(N9b's sharper q ≥ 2pj+1 is neither needed nor claimed.)

### 2.2 Trial division over all primes < 10^8 [N, exact] (`code/lemmaW_trial.py`, `logs/lemmaW_trial.json`)
- For each of the 94 primes 3 ≤ p < 500, h_p is reduced modulo **every** odd prime q < 10^8 (5,761,454 primes).
  - There is no residue-class presieve, so the test does not presuppose the lemma.
  - Arithmetic is in ℤ[√2]/q with int64, products < 10^16.
  - Every hit is re-confirmed with exact big-integer h_p mod q.
- Results:
  - 108 prime factors < 10^8 were found;
  - 26 of the p have none below 10^8;
  - at most 4 per p (e.g. p = 419: 839, 17599, 211177, 54054353);
  - **0 violations**.
- Run time: 1087 s.

### 2.3 Complete factorisations [N] (`code/lemmaW_full.py`, `logs/lemmaW_full_partial.out`)
- Method: sympy `factorint` with ECM, 120 s per p.
- Each product is re-multiplied and checked to equal h_p exactly.
- Factor primality is by BPSW: [N], with no certificates for large factors.
- **47 complete factorisations:** every prime p ≤ 233 except 197, 211 and 229, which timed out; p > 233 was not completed. The job was stopped after its pool stalled.
- In these 47: **0 violations**, all h_p **squarefree**, max ω = 6 (p = 181, 199, 223). This fits the P3 remark that actual ω is tiny.

## 3. H1-bad: second-moment transfer operator — not attempted; the obstruction
**Condition for attempting it.** A concrete decoupling of the A and B sectors in the bad weight:
- |r_A r_B|² in H1 as registered;
- |w| = |r_A r_B|³ in the KP activity.

None was found, so nothing was run.

**The obstruction, stated precisely.**
1. **Degree [P].** The target is homogeneous of degree 4 (H1) or 6 (KP) in the entries of r_A, r_B ∈ ℂ^D (D = 495), and both are driven by the **same** letter word.
   - An exact positive transfer operator must act on a space carrying that degree.
   - For the second moment this is the space spanned by r_A⊗r̄_A⊗r_B⊗r̄_B, of dimension D⁴ ≈ 6·10^10. Symmetries can reduce it to ≳ D⁴/4.
   - It must also be tensored with the 6145 carry states (Lemma J). The total is ≳ 10^14.
2. **No splitting helps [assessment of methods, not a theorem].** AM–GM (|r_A r_B|² ≤ ½(|r_A|⁴ + |r_B|⁴)), Cauchy–Schwarz over words, and general Hölder all leave a single-sector 4th moment.
   - That moment lives on Sym²(ℂ^D⊗ℂ̄^D), of dimension ≈ D⁴/2.
   - Separating the sectors trades the A/B coupling for an object of the same dimension.
   - For the cubic KP weight the degree rises to 6.
3. **Degree-2 surrogates lose the cancellation [assessment + N].**
   - The surrogate is (sup_bad|r_B|²)·|r_A|², which needs only D².
   - But sup|r_B| is controlled only by per-letter norms > 1 (Λ_free ≈ 1.97), while the observed |w|^{1/j} ≈ 0.12 [N, O1].
   - The loss is ≈ (1.97/0.12)^j, which exceeds the H1 slack of ≈ 4·10^5 (P3) by j ≈ 5.
4. **The restriction must be visible (Prop F, TRACE-329).** The operator must also carry the bad-polymer/zero-run automaton and the whole-word Green twist d_t = −(h∗E)_t, which decays like 0.414^{|t|}.
   - A finite twist window R needs a rigorous perturbation term, which is again a degree-4 object.
5. **The only visible escape [C]:** a certified low-rank compression of ℂ^D to rank r ≲ 10, making the dimension r⁴·6145 feasible.
   - It is unknown whether such a subspace dominates the bad shells.
   - Bounding the complement rigorously is again degree 4.

**Status:** H1-bad is open. The dimension and degree count is arithmetic about the routes considered (direct, AM–GM, Hölder, Cauchy–Schwarz), not an impossibility theorem; the 0.12 rate and the 4e5 slack are [N]. J0: the registry (TRACE-336) states H1-bad with J0 = 12, C ≤ 0.082; P3/P4's J0 = 14, C3 ≤ 1e−3 refer to the finite-part certification range (Thm A, j ≤ 14). The registered hypothesis is the J0 = 12 one.

## 4. Self-referee
- ✓ The r_2 reruns reproduce N2 exactly at k = 1000, 2000 and 4000 (8V: 1.058275287962231, 1.0546894903794668, 1.0529011503787689).
- ✓ A bug was caught and fixed: a module-level `X` (the Bessel argument 1.8) was overwritten by the range bound, which corrupted every row after the first. All rows in `logs/h6_p0.json` come from the clean rerun.
- ✓ Every decision is an arb comparison (true only if certified). w̄ is a certified upper bound. The tail is analytic.
- p0 is a certified threshold for *this* bound, not the optimal p0 for Theorem C'.
- v2: the Lemma I one-step structure and A_J ≤ 4/3 are [P]; (C1) is [P] except u = 1. Remaining conditions: u = 1, h_p squarefree, inherited N4 Λ, κ_F and N2 r_2 [CA], 8V/8E only.
- Not run: 16V/16E, a margin fraction < 1, the 𝒫-only p0, and k > 4000. p0 was still decreasing at k = 4000, but r_2 is certified only on 1000–4000 here.
