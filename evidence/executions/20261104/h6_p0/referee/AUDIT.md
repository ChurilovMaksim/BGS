# Hostile referee audit of research1104/P4 (with P3)
Date: 2026-11-04, Europe/Berlin. Repo: ChurilovMaksim/BGS origin/main 6440a447 (committed 2026-11-04 11:24 Europe/Berlin), read via `git show` from the existing clone /workspace/audit/BGS. No checkout, no Lean build, nothing pushed.
My code: `code/indep.py` (mpmath, 60 digits; independent of P4's flint code), `code/indep_shift.py`, `code/shift.py`, `code/pt.py`, `code/lw.py`. Logs: `code/indep.out`.
My recomputation is high-precision floating point [N-hp], not ball arithmetic. It agrees with P4's arb output to every printed digit.

## Verdicts
| # | Item | Verdict |
|---|---|---|
| 1 | Lemma W (q ≡ ±1 mod 2p, p ∤ h_p, ω bound) | **CONFIRMED** |
| 2a | 8V p0 = 28,420,500 (k=4000) | **NEEDS FIX**: missing constant e^{βRc}. Corrected p0 = **28,424,695** |
| 2b | 8E p0 = 3,928 (k=1000) | **NEEDS FIX**: same missing constant. Corrected p0 = **3,934** |
| 3a | [P-sketch] Lemma I one-step structure | **CONFIRMED**: provable from repo text (TRACE-197/249/294, cert_lift.py) plus standard H² facts. Upgrade to [P] |
| 3b | [P-sketch] A_J ≤ 1 | **NEEDS FIX**: proved A_J ≤ 2/3 per sign ρ, but ≤ 4/3 if both signs (±2,8) are summed. Use log A_J ≤ log(4/3) |
| 3c | [P-sketch] torus convention (C1) | **NEEDS FIX**: the main structure is verified. The robust-variant wording is wrong (it is the frequency-embedding convention that it removes, not the direction of T). One normalisation (the image u of e_q in O) is unverified |
| 4 | H1-bad obstruction | **NEEDS FIX (labels)**: the numbers are correct. "[P] no splitting helps" is an assessment of methods, not a theorem. The J0 value conflicts with the registry |

## 1. Lemma W: CONFIRMED
I checked the proof line by line (§2.1):
- h_n = 2h_{n−1} + h_{n−2} with h_0 = h_1 = 1, so every h_n is odd. q odd and q ∤ 8, so O/q is unramified.
- ε^p ≡ −ε̄^p in O/q. Multiplying by ε^p gives ε^{2p} ≡ −(−1)^p = 1.
- N(ε−1) = −2 and N(ε²−1) = N(2ε) = −4, both prime to q. So ord(ε) ∈ {p, 2p}.
- Split case: p | q−1. Inert case: ε^{q+1} = εε̄ = −1, so ord(ε) | 2(q+1) and p | q+1 (p odd).
- Hence 2p | q∓1, and so q ≠ p.
- The j-th integer > 1 that is ≡ ±1 (mod 2p) is ≥ pj−1 ≥ (p−1)j.
- (p−1)^w·w! ≤ h_p < ε^p, because ε̄^p ∈ (−1, 0).

All steps are correct. Cosmetic: §1.4 calls the unit ε_0 while §1.3 uses ε for the Bowen radius. Rename one of them.

Independent numerics (`code/lw.py`, plain big-integer recurrence, no presieve):
- All primes 3 ≤ p < 300 against all primes q < 3·10^5: 53 hits, 0 violations.
- The four factors claimed for p = 419 (839, 17599, 211177, 54054353) all divide h_419, and each is ≡ 1 (mod 838).
- sympy factorint of h_p for every prime p < 110: every factor is ≡ ±1 (mod 2p), every h_p is squarefree, and max ω = 4. This is consistent with P4's ω ≤ 6 for p ≤ 233.

## 2. Explicit p0
I recomputed the full chain independently, using the same inputs: N4 Λ and κ_F, and N2/P4 r_2.

| quantity | P4 | mine [N-hp] |
|---|---|---|
| C_I (8V), mids (0.80,0.05) / (0.75,0.45) | 5.2534398e8 | 525343975.94, same mids |
| S = sup‖L‖_{O1} (8V) | 61.00157 | 61.0015661 |
| C_pair (8V) | 25.8317 | 25.8317084 |
| log L′ (8V, k=4000) | 6909.80 | 6909.79657 |
| log H_max | 2728.27 | 2728.26550 |
| K1 (8V, k=4000) | 31794.22 | 31794.22204 |
| log κ (8V, k=4000) | 0.0216177 | 0.02161766 |
| p0 pointwise (8V) | 28,420,500 | fails at 28,420,499, passes at 28,420,500 (w_max = 840,451) |
| C_I, S, K1, log κ (8E, k=1000) | 7.347355e5, 12.659, 5319.70, 1.40616 | 734735.52, 12.6591, 5319.70065, 1.40616 |
| p0 (8E) | 3,928 | fails at 3,927, passes at 3,928 (w_max = 268) |

**Cover and tail.** I used my own greedy doubling cover with w̄(P1, P2) = max{w : (P1−1)^w·w! ≤ ε^{P2}}.
- 8V: [p0, 10^10] is covered by 186 intervals. 8E: 34 intervals. There are no failures.
- Pointwise scan of [p0, p0+3000): 0 failures.
- Tail at X = 10^10: c′ = 0.031183 (8V). LHS 41.584 > RHS 28.264, so the tail closes.
- I checked the tail argument itself:
  - ((K1 + 2 log p) − 2 log(1−λ^{−p}))/p is decreasing.
  - ω ≥ c′p together with monotonicity of (p−1)^w·w! gives the stated inequality.
  - The left side is increasing in p.

  The argument is correct.

**Chain checked against the repo:**
- Theorem B/C (N2 §3–4, TRACE-289), Prop E (N2 §4): Collatz–Wielandt gives ⟨0|B^Q|0⟩ ≤ R^Q directly, so x_max/x_0 is not needed. Σ_r Q_r = p−k+1. Correct.
- κ_F = 4036 and Λ^{8V} = 1.9656353: N4_v2 l.52–53. κ = 4.3e4 and Λ^{8E} = 0.4915932: N4_v2 l.35. The P3 correction (2966 → 4036) is right.
- Bowen ball:
  - Area 4ε²λ^{−(p−1+k)}.
  - covol O^∨ = 1/(2√2).
  - |G_p| = h_p², which agrees with N2's ((1/h_p)O + O^∨)/O^∨. That group equals (1/h_p)O^∨/O^∨ because gcd(h_p, 8) = 1.
  - λ^p/h_p² = 4/(1−λ^{−p})², because (ε̄/ε)^p = −λ^{−p}.

  So B_ε is correct. Disjointness: the min |N| on O^∨ \ 0 is 1/8. P4's bound ε²λ^{2−k} is weaker than the actual ε²λ^{1−k}, but still valid. Correct.
- C_pair, dev, τ_j and A(s) match TRACE-249/250 exactly, including j = 0 as the outermost letter.

**Error found: a missing constant.**
- N3_v2 §2.1 [N3-F5(iii)] and TRACE-294 say that Line F's weights e^{−β(|c|−Rc)_+} are equivalent to e^{−β|c|} "within e^{βRc}, absorbed into κ_F".
- But κ_F = 4036 (and 4.3e4) is the |||·||| ↔ Line F norm equivalence constant of N4 §1. Nothing in N3/N4 shows that it contains e^{βRc}.
- Here Rc = K0 = 4 (V) and K0 − ½ = 3.5 (E), by `lineF/code/cert_lift.py` l.20, with β = 2.5. That gives +10 (8V) and +8.75 (8E) in log K.
- P4's Lemma I works in H(1.2, 2.5) with weight e^{−β|c|}, but Λ is certified in the Line F (om) norm. P4 does not account for this factor.

**Corrected thresholds.** Applying this, plus log(4/3) for A_J (§3b), gives:
- 8V: pointwise least p0 = 28,424,535, but the test fails again up to **28,424,694**. From **28,424,695** it holds on all of [28,424,695, 10^10] (186-interval cover) and the tail closes.
- 8E: **3,934**, with cover and tail OK.

**Non-monotonicity warning.** The pointwise test is not monotone in p near p0. The shifted 8V case has 586 failures above the bisection point, so a bisection value alone is never a certified p0. P4's `certify` restarts on failure and is fine. Any rerun must keep that restart.

**Other remarks:**
- The k-optimisation stops at k = 4000, where p0 is still decreasing (P4 says so).
- p0 is a threshold for this bound only.
- Squarefreeness of h_p remains a hypothesis.
- The robust (orientation-free) variant becomes ≈ 31.24e6 + ~4e3 after the same fix. I did not rerun it.

## 3. The three [P-sketch] inputs
**(a) Lemma I one-step structure: proved from repo sources.**
- Sub-disc θ = (ρ_b/λ + off)/ρ_a with off = ½ (V) and 1/(2λ) (E). TRACE-197's radius conditions, quoted verbatim in TRACE-249, are exactly this formula at a = b = O1:
  - 1/(2ρ_V) + 1/λ = 0.838;
  - 1/(2λρ_E) + 1/λ = 0.6005.
- TRACE-249's k-step dev values λ/(2(λ−1)) = Σ_{j≥0}½λ^{−j} (V) and 1/(2(λ−1)) = Σ_{j≥1}½λ^{−j} (E) confirm the per-step offsets. So the E offset is not merely inferred.
- The multiplier e(κns) has real disc centres (lineJ, TRACE-222), so |·| ≤ e^{2πκ|n|ρ_b}. κ = C0 = 1/(λ−λ^{−1}) (TRACE-249).
- The weight ratio uses |c′| ≤ (|c|+|n|)/λ + ½ (cert_lift.py l.90).
- The Schur factor √6 comes from column multiplicity ⌈λ⌉ (TRACE-294).
- H² composition: the image disc lies in D(c′, θρ_a), and sup_{θ-disc}|f| ≤ (1−θ²)^{−1/2}‖f‖_{H²}.
- Composing through an intermediate space is submultiplicative. All grid mids satisfy θ < 1 and β_a/λ ≤ β_b (checked: θ = 0.850, 0.882, 0.524, 0.838 for 8V).
- Every V figure from N3 is reproduced: 0.9412, 0.507, e^{0.125+0.043|n|}.

**(b) A_J ≤ 1: proved per sign, ≤ 4/3 overall.**
- TRACE-266 and lineI/lineJ give Ẑ_ρ = c_m Σ_a c_a(case, ρ)·⅓[Tr V^m − Tr E^m], with c_m = 1 − λ^{−m} ≤ 1 and |c_a| = ½ exactly, for 4 sectors.
- The read-out is I_K ⊗ |0⟩⟨1|, with norm 1. It commutes with the ω-conjugation (TRACE-249, referee F4).
- So for the V family at one sign ρ, A_J ≤ 4·½·⅓ = 2/3. If the 8V cross part sums over ρ = (2,8) and (−2,8), then A_J ≤ 4/3.
- Effect: < +120 on p0. This is included in the corrected values above.

**(c) Convention (C1).** Verified:
- √2 ↦ [[0,2],[1,0]] gives (1+√2)² ↦ [[3,4],[2,3]] = S. So T is multiplication by λ on K_ℝ/O^∨ under the Tr pairing (λ is self-adjoint for Tr).
- Fix(T^p) = (1/2h_p)O^∨/O^∨ matches N2's (4√2·h_p·ε^p)^{−1}O/O^∨.
- G_p and index 4 are as in N2.

Not verified: that the frequency of a word is exactly γ = Σ n_jλ^j·u with u = 1. N2 writes Σ(A^T)^i k_i with k_i = n_i e_q, so u is the image of e_q in O^∨ (or O). A u ≠ 1 multiplies L′ by at most max|σ_i u|, which changes log K by about 2 log max|σ_i u|. That is negligible but should be stated.

The robust variant (ball |v1| ≤ ελ^{−(p−1+k)}, |v2| ≤ ελ^{−k}, cost +k log λ = 7051) is valid and removes the question of which embedding carries λ^j. I checked that its Lipschitz weight is ≤ the base weight. But §1.6/§1.7 describe it as "dropping the T = ×λ orientation", and that is wrong: if T were ×λ^{−1}, you would swap v1 and v2, at the same cost.

## 4. H1-bad obstruction: NEEDS FIX (labels only)
- Arithmetic is correct: D⁴ = 495⁴ = 6.0e10; D⁴·6145 = 3.7e14; Sym² ≈ D⁴/2 = 3.0e10; (1.97/0.12)^j > 4e5 for j ≥ 5.
- "No splitting helps" and "degree-2 surrogates lose the cancellation" are statements about AM–GM, Cauchy–Schwarz and Hölder routes. They are not theorems excluding every decoupling, so they must not carry [P].
- The 0.12 rate and the 4e5 slack (P3) are [N].
- Registry TRACE-336 states H1-bad with **J0 = 12** (C ≤ 0.082). P3/P4 use J0 = 14 and C3 ≤ 1e−3. Make them consistent or say which is meant.
- Status "H1-bad open" is correct.

## Safe registry wording
- **Lemma W [P]:** "For odd primes p and q with q | h_p = (ε^p + ε̄^p)/2, ε = 1+√2: q ≡ ±1 (mod 2p). Hence p ∤ h_p, the j-th smallest prime factor of h_p is ≥ pj−1, and ω(h_p) ≤ w_max(p) := max{w : (p−1)^w·w! ≤ ε^p}. [N] 0 violations for all primes q < 10^8 dividing h_p, 3 ≤ p < 500 (P4). Complete factorisations (BPSW primality, uncertified for large factors) for 47 p ≤ 233 are squarefree with ω ≤ 6."
- **H6 / Theorem C′ explicit threshold [P + CA, mod inherited N4 Λ, κ_F and N2 r_2; given h_p squarefree]:** "For the 8V family (k = 4000), the unit-point cross part at c = h_p is < T^{3p} = 1.28359^{3p} for every prime p ≥ 28,424,695 with h_p squarefree. For 8E (k = 1000) this holds for p ≥ 3,934. Proof: interval cover of [p0, 10^10] plus an analytic tail. The constants are C_I ≤ 5.2535e8, S ≤ 61.002, log L′ ≤ 6909.80 and log K(p) ≤ 31804.6 + 2 log p, including e^{βRc} = e^{10} and A_J ≤ 4/3. The frequency normalisation u = 1 in (C1) is assumed (its effect is O(1) in log K). The threshold is for this bound only, not optimal; 16V/16E are not covered." The 28,424,695 and 3,934 figures are conditional on P4's arb rerun confirming them.
- **H1-bad:** "Open. No decoupling of the A/B sectors was found. Every exact positive transfer-operator route considered (direct, AM–GM, Hölder, Cauchy–Schwarz) needs a degree-4 object of dimension ≳ D⁴·6145 ≈ 3.7e14 (D = 495) [arithmetic; assessment of methods, not an impossibility theorem]. Norm-based degree-2 surrogates lose a factor ≈ (1.97/0.12)^j [N]."

## Required fixes to P4
1. Add βRc (10 for V, 8.75 for E) to log K, or prove that κ_F already contains it, and rerun `h6_p0.py`. Expected: 28,424,695 and 3,934.
2. Replace A_J ≤ 1 with the derivation in §3b (A_J ≤ 4/3, or 2/3 per sign).
3. Relabel the Lemma I one-step structure [P], citing TRACE-197/249 for the offsets.
4. Correct the robust-variant wording, and state the u-normalisation in (C1).
5. Rename ε_0 / ε.
6. Relabel the H1-bad "[P]" items as [assessment]. Fix J0 (12 vs 14).
