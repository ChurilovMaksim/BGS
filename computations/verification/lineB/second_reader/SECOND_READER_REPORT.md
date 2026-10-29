# Second-reader report, Line B (BGS-TRACE-163..182), 2026-10-29

Independent second reader (not the author). Scope: blocker B1 (directed-rounding re-certification of all 93 intervals of TRACE-173) and blocker B2 (proof check of TRACE-167 and TRACE-169). Times Europe/Berlin (CET).

## Summary of verdicts

- **TRACE-167 (automatic admissibility):** statement confirmed; the written proof needed a one-line fix (part (b), split case O/hO ≅ F_h×F_h: the two-roots argument must be replaced by the norm-1 argument). Fix applied to the texts. Status → proved (owner may revert if the fix is not accepted).
- **TRACE-169 (Prop C, all odd m):** confirmed, including p² | h. No fix needed. Status → proved.
- **TRACE-170, 178** (proved, depend on 169): consistent; stay proved.
- **TRACE-173 (Theorem D_cert):** B1 complete, 93/93 valid, contiguous coverage [1.0, 81.57406988332305]. Rest of the argument (framework 172, lower bound 171, box/outside-box bound, ball coverage, coefficient envelopes) re-checked. Status → proved (computer-assisted) **with the directed-rounding constants** (max ρ' = 0.99981969, max C' = 1.4296e+07), not with the authors' float constants.

## B1. Directed-rounding re-certification of TRACE-173

- Certifier: referee `t9_cert.py`, unmodified (sha256 2dee8e5490d0ebff3a0793ffbdc8dae11281ef6396394c1a7b72a49b9d118947; core.py bbd6895f25fe0dac045e3c798424d6a0b974cb54d14af8a4ef0764a93ce489dc, re-hashed after the run). arb balls in η (24 sub-balls per interval), nextafter outward rounding after each float operation, sparse mat-vec bound (1+(k+1)u)/(1−(k+1)u), arb for the outside-box region and lattice tail, libm exp only in the Edrop term with 1e-6 margins.
- Intervals: the 93 exact float endpoints of grid_v2 (`b1_intervals.json`), neighbours share endpoints exactly; coverage [1, 81.57406988332305].
- Provenance: idx 0, 33, 48 imported from the referee's runs (same code, exact endpoints). The referee's runs for idx 6, 17, 92 used rounded endpoints (≈1e-5 gaps), so they were rerun. 90 intervals run by the second reader.
- Run: `runner.py` (resumable; mkdir claims, per-interval jsonl written atomically, memory guard), two nohup workers (`H1 heavy 1200` descending, `L1 any 1200` ascending), started 21:11 CET, finished 22:50 CET (1 h 39 min wall-clock; ≈ 3.3 h summed worker time; ≈ 3.2–3.4 GB RSS per heavy worker). The box was shared (load 17–20); the run survived two agent interruptions. A third worker was not added because of CPU saturation.
- Result: **93/93 valid, 0 failures**, contiguous_closed = True. max_I ρ'_I = 0.99981969 (at η ∈ [1, 1.1]); min_I ρ'_I = 0.9 (t9 floors ρ' at 0.9 for a ≠ 0, so this is the floor, weaker than the float grid's 0.8527); max_I C'_I = 1.429630e+07 (C'_I = Σ_a C_I,a); m⁺(η=1) for bound ≤ 0.01: 116570.
- Ball coverage (`sr173_ballcover.log`): 14 of 2232 sub-balls individually miss slivers ≤ 1.7e-15 relative to neighbours' nominal splits, but within each interval the union of its own balls covers the interval; no gaps.
- Coefficient envelopes (`sr173_coefcheck.log`): FFT |ŵ|/b ≤ 0.99999999 (FFT noise threshold 1e-14); envelopes dominate.
- Framework re-checked: u' = λu, t' = t/λ; L-cycle inequality with γ0 = 1 − 1/λ, c = 2; the box covers all N ≤ R; the outside-box bound is valid.
- Hypotheses of the proved statement: IEEE-754 binary64 round-to-nearest; correctness of arb/python-flint; libm exp accurate to 1e-6 relative inside the Edrop term (Edrop ≤ 1e-29). The float grid's libm ≤ 4 ulp hypothesis is not used.
- Not claimed: the authors' float constants (C_I ≤ 3.64e6, ρ_I from grid_v2) are not directed-rounding certified; non-claims 4 and 8 still stand as written (8 for the float grid).

| idx | η0 | η1 | ρ' | C' | m⁺(0.01) | source |
|---|---|---|---|---|---|---|
| 0 | 1.000000 | 1.100000 | 0.99981969 | 1.3460e+07 | 116570 | referee |
| 1 | 1.100000 | 1.240000 | 0.99978218 | 1.3128e+07 | 96380 | second reader |
| 2 | 1.240000 | 1.436000 | 0.99972385 | 1.3298e+07 | 76068 | second reader |
| 3 | 1.436000 | 1.710400 | 0.99963090 | 1.3538e+07 | 56957 | second reader |
| 4 | 1.710400 | 2.094560 | 0.99947890 | 1.2493e+07 | 40187 | second reader |
| 5 | 2.094560 | 2.632384 | 0.99922400 | 1.2923e+07 | 27027 | second reader |
| 6 | 2.632384 | 3.385338 | 0.99878671 | 1.3017e+07 | 17289 | second reader |
| 7 | 3.385338 | 3.912405 | 0.99798931 | 1.3427e+07 | 10444 | second reader |
| 8 | 3.912405 | 4.650300 | 0.99734078 | 1.4016e+07 | 7911 | second reader |
| 9 | 4.650300 | 5.000000 | 0.99622523 | 1.4289e+07 | 5575 | second reader |
| 10 | 5.000000 | 5.300000 | 0.99564331 | 1.3968e+07 | 4824 | second reader |
| 11 | 5.300000 | 5.720000 | 0.99513111 | 1.4296e+07 | 4321 | second reader |
| 12 | 5.720000 | 6.308000 | 0.99437291 | 1.3222e+07 | 3723 | second reader |
| 13 | 6.308000 | 7.131200 | 0.99323398 | 1.3304e+07 | 3096 | second reader |
| 14 | 7.131200 | 8.283680 | 0.99149657 | 1.4106e+07 | 2468 | second reader |
| 15 | 8.283680 | 9.090416 | 0.98853488 | 1.4069e+07 | 1828 | second reader |
| 16 | 9.090416 | 10.219846 | 0.98642538 | 1.3235e+07 | 1538 | second reader |
| 17 | 10.219846 | 11.010448 | 0.98287848 | 1.3136e+07 | 1217 | second reader |
| 18 | 11.010448 | 12.117289 | 0.98046810 | 1.3790e+07 | 1068 | second reader |
| 19 | 12.117289 | 13.666868 | 0.97694329 | 1.4152e+07 | 905 | second reader |
| 20 | 13.666868 | 15.000000 | 0.97101656 | 1.2672e+07 | 714 | second reader |
| 21 | 15.000000 | 15.500000 | 0.96485300 | 1.2879e+07 | 588 | second reader |
| 22 | 15.500000 | 16.200000 | 0.96291757 | 1.3221e+07 | 557 | second reader |
| 23 | 16.200000 | 17.180000 | 0.96018979 | 1.3162e+07 | 518 | second reader |
| 24 | 17.180000 | 18.552000 | 0.95635352 | 1.2224e+07 | 470 | second reader |
| 25 | 18.552000 | 19.512400 | 0.94950442 | 1.2045e+07 | 405 | second reader |
| 26 | 19.512400 | 20.856960 | 0.94560466 | 1.2577e+07 | 376 | second reader |
| 27 | 20.856960 | 22.739344 | 0.94025320 | 1.1251e+07 | 340 | second reader |
| 28 | 22.739344 | 24.057013 | 0.92999802 | 1.1170e+07 | 289 | second reader |
| 29 | 24.057013 | 25.901749 | 0.92488522 | 1.1231e+07 | 268 | second reader |
| 30 | 25.901749 | 27.193065 | 0.91447061 | 9.7256e+06 | 233 | second reader |
| 31 | 27.193065 | 29.000906 | 0.90991514 | 9.7604e+06 | 221 | second reader |
| 32 | 29.000906 | 30.000000 | 0.90000000 | 8.7413e+06 | 197 | second reader |
| 33 | 30.000000 | 30.500000 | 0.90000000 | 8.8116e+06 | 197 | referee |
| 34 | 30.500000 | 31.200000 | 0.90000000 | 8.5441e+06 | 197 | second reader |
| 35 | 31.200000 | 32.180000 | 0.90000000 | 8.7358e+06 | 197 | second reader |
| 36 | 32.180000 | 33.552000 | 0.90000000 | 8.5865e+06 | 197 | second reader |
| 37 | 33.552000 | 35.472800 | 0.90000000 | 7.5063e+06 | 195 | second reader |
| 38 | 35.472800 | 36.817360 | 0.90000000 | 7.6629e+06 | 196 | second reader |
| 39 | 36.817360 | 38.699744 | 0.90000000 | 6.6577e+06 | 194 | second reader |
| 40 | 38.699744 | 40.017413 | 0.90000000 | 6.4730e+06 | 194 | second reader |
| 41 | 40.017413 | 41.862149 | 0.90000000 | 6.4191e+06 | 194 | second reader |
| 42 | 41.862149 | 43.153465 | 0.90000000 | 5.4519e+06 | 192 | second reader |
| 43 | 43.153465 | 44.961306 | 0.90000000 | 5.6382e+06 | 193 | second reader |
| 44 | 44.961306 | 46.226795 | 0.90000000 | 4.7882e+06 | 191 | second reader |
| 45 | 46.226795 | 47.998480 | 0.90000000 | 4.6990e+06 | 191 | second reader |
| 46 | 47.998480 | 50.000000 | 0.90000000 | 4.6078e+06 | 191 | second reader |
| 47 | 50.000000 | 50.500000 | 0.90000000 | 4.5746e+06 | 191 | second reader |
| 48 | 50.500000 | 51.200000 | 0.90000000 | 4.6229e+06 | 191 | referee |
| 49 | 51.200000 | 52.180000 | 0.90000000 | 4.6931e+06 | 191 | second reader |
| 50 | 52.180000 | 53.552000 | 0.90000000 | 4.7957e+06 | 191 | second reader |
| 51 | 53.552000 | 55.472800 | 0.90000000 | 4.9408e+06 | 191 | second reader |
| 52 | 55.472800 | 56.817360 | 0.90000000 | 5.0284e+06 | 192 | second reader |
| 53 | 56.817360 | 58.699744 | 0.90000000 | 5.2046e+06 | 192 | second reader |
| 54 | 58.699744 | 60.017413 | 0.90000000 | 5.2849e+06 | 192 | second reader |
| 55 | 60.017413 | 60.939781 | 0.90000000 | 5.3390e+06 | 192 | second reader |
| 56 | 60.939781 | 62.231096 | 0.90000000 | 5.4605e+06 | 192 | second reader |
| 57 | 62.231096 | 63.135017 | 0.90162730 | 5.5103e+06 | 196 | second reader |
| 58 | 63.135017 | 64.400506 | 0.91276032 | 5.6269e+06 | 222 | second reader |
| 59 | 64.400506 | 65.286349 | 0.91451597 | 5.6693e+06 | 227 | second reader |
| 60 | 65.286349 | 65.906438 | 0.91547717 | 5.6966e+06 | 230 | second reader |
| 61 | 65.906438 | 66.774564 | 0.92276552 | 5.7728e+06 | 252 | second reader |
| 62 | 66.774564 | 67.382252 | 0.92343980 | 5.7976e+06 | 255 | second reader |
| 63 | 67.382252 | 68.233015 | 0.93047485 | 5.8725e+06 | 282 | second reader |
| 64 | 68.233015 | 68.828549 | 0.93075319 | 5.8937e+06 | 283 | second reader |
| 65 | 68.828549 | 69.662297 | 0.93745105 | 5.9656e+06 | 314 | second reader |
| 66 | 69.662297 | 70.000000 | 0.93338317 | 5.9486e+06 | 295 | second reader |
| 67 | 70.000000 | 70.300000 | 0.93429338 | 5.9643e+06 | 299 | second reader |
| 68 | 70.300000 | 70.720000 | 0.93753881 | 5.9997e+06 | 315 | second reader |
| 69 | 70.720000 | 71.308000 | 0.94207002 | 6.0491e+06 | 340 | second reader |
| 70 | 71.308000 | 72.131200 | 0.94833990 | 6.1177e+06 | 383 | second reader |
| 71 | 72.131200 | 72.707440 | 0.94752490 | 6.1301e+06 | 377 | second reader |
| 72 | 72.707440 | 73.514176 | 0.95414971 | 6.2021e+06 | 433 | second reader |
| 73 | 73.514176 | 74.078891 | 0.95406996 | 6.2216e+06 | 432 | second reader |
| 74 | 74.078891 | 74.474192 | 0.95387117 | 6.2340e+06 | 430 | second reader |
| 75 | 74.474192 | 75.027613 | 0.95846862 | 6.2842e+06 | 479 | second reader |
| 76 | 75.027613 | 75.415007 | 0.95808201 | 6.2949e+06 | 475 | second reader |
| 77 | 75.415007 | 75.957360 | 0.96247611 | 6.3431e+06 | 531 | second reader |
| 78 | 75.957360 | 76.337007 | 0.96190624 | 6.3521e+06 | 523 | second reader |
| 79 | 76.337007 | 76.868512 | 0.96609635 | 6.3985e+06 | 589 | second reader |
| 80 | 76.868512 | 77.240566 | 0.96534980 | 6.4058e+06 | 577 | second reader |
| 81 | 77.240566 | 77.761441 | 0.96943134 | 6.4515e+06 | 655 | second reader |
| 82 | 77.761441 | 78.126054 | 0.96864865 | 6.4590e+06 | 638 | second reader |
| 83 | 78.126054 | 78.636512 | 0.97258046 | 6.5036e+06 | 731 | second reader |
| 84 | 78.636512 | 78.993832 | 0.97164632 | 6.5097e+06 | 707 | second reader |
| 85 | 78.993832 | 79.494081 | 0.97616968 | 6.5568e+06 | 843 | second reader |
| 86 | 79.494081 | 79.844255 | 0.97604854 | 6.5665e+06 | 839 | second reader |
| 87 | 79.844255 | 80.089377 | 0.97590727 | 6.5730e+06 | 834 | second reader |
| 88 | 80.089377 | 80.432547 | 0.97925089 | 6.6069e+06 | 970 | second reader |
| 89 | 80.432547 | 80.672767 | 0.97957733 | 6.6167e+06 | 986 | second reader |
| 90 | 80.672767 | 81.009074 | 0.98327370 | 6.6529e+06 | 1206 | second reader |
| 91 | 81.009074 | 81.244489 | 0.98381063 | 6.6636e+06 | 1246 | second reader |
| 92 | 81.244489 | 81.574070 | 0.98755162 | 6.6997e+06 | 1624 | second reader |

## B2. Independent proof check of BGS-TRACE-167 and BGS-TRACE-169

Texts read: `mathematics/fixed-map/derandomized_fixed_kick.md` (#claim-167, #claim-169), `phase2_kernel_ramp_nd.md` §C4 (Lemma [ref23-fix]), `phase3_parity_decomposition.md` §1 (Prop C, self-duality), `phase1_trace_formula.md` §1–§4 (definitions of V, 𝒬, ℬ, k_ν, Prop R), the referee report §2.2 and §3.1–§3.2. I derived each step again from the phase-1 definitions. All code here is new: `code/sr167_admissibility.py`, `code/sr169_propC.py`, `code/sr169_selfdual.py`. The only shared input is the 14 rational kick coefficients c_k. No project code and no referee code was used.

### B2.1 TRACE-167 (automatic admissibility). Verdict: **the statement is confirmed; the written proof needed a one-line fix, which is now applied.**

**Setting.** m is odd, h = h_m is prime and h > 18. O = Z[λ] = Z[√8], with λ = 3 + √8. R := O/hO = F_h[t]/(t² − 6t + 1). The discriminant is 32, a unit mod h. σ: √8 ↦ −√8 is the non-trivial automorphism of R. It satisfies σ(λ) = λ⁻¹, because Nm λ = 1, and its fixed ring is F_h. K = {±1, ±2, ±5, ±6, ±7, ±8, ±9}; 0 ∉ K.

**Step 0: ord_h(λ) = m.** λ^m − 1 = h·2ρ^m with 2ρ^m ∈ O, so λ^m ≡ 1. Suppose λ^d ≡ 1 for some d | m with d < m. Then h² | Nm(λ^d − 1) = 2 − 2x_d = −D_d = −4h_d². So h | h_d with 0 < h_d < h, which is impossible. ✔ (This is the referee's argument; the Lemma text should state it, since (a) needs it.)

**(a).** Suppose λ^d = r ∈ F_h. Applying σ gives λ^{−d} = r, so r² = 1 and r = ±1, because F_h is a field.
- r = −1 would give λ^{2d} = 1, so m | 2d, so m | d (m is odd), so λ^d = 1 ≠ −1. Hence r = 1.
- So k′/k ≡ 1, i.e. k ≡ k′ mod h. With |k − k′| ≤ 18 < h this forces k = k′. ✔

No gap here.

**(b), the gap.** Put u = λ^a and v = λ^b with u + v = 6. Applying σ gives u⁻¹ + v⁻¹ = 6, so (u + v)/uv = 6, and therefore uv = 1 (6 is a unit). So u and v are roots of t² − 6t + 1. The written proof (referee §2.2, and the Lemma in phase-2 §C4) concludes "so {u, v} = {λ, λ⁻¹}". **That step holds only if R is a field. R is never a field here.**
- 2 is a square mod every prime p | h_m. Write ρ^m = h + B√2 (ρ = 1 + √2, m odd). Then Nm ρ^m = h² − 2B² = −1, so 2B² ≡ 1 (mod h).
- Hence R ≅ F_h × F_h is always split. The "inert / Frobenius" branch of the referee's argument is vacuous.
- In F_h × F_h, t² − 6t + 1 has **four** roots: (λ₁, λ₂) = λ, (λ₂, λ₁) = λ⁻¹, (λ₁, λ₁) and (λ₂, λ₂). Here λ₁, λ₂ = 3 ± √8 ∈ F_h.

**Repair (one line).** Every power u = λ^a has norm u·σ(u) = 1. The two extra roots have norm λ₁² and λ₂². These are ≠ 1, because λ_i = ±1 would give 1 ∓ 6 + 1 ∈ {−4, 8} ≡ 0 mod h, which is impossible for h > 18. Hence u ∈ {λ, λ⁻¹} and v = 6 − u = u⁻¹.
- u = λ gives λ^{a−1} = 1, so a ≡ 1 (mod m) and b ≡ −1. The case u = λ⁻¹ is symmetric.
- If a = b, then u = λ = λ⁻¹, which forces λ² = 1 and contradicts ord λ = m ≥ 3.

So (b) holds. ✔

**Use in Theorem N (TRACE-168).** TRACE-168 does not use the Lemma: its eleven instances are checked directly. With the Lemma, Theorem N holds for every odd m with h_m prime and h_m > 28m.

**Numerical edge cases (exhaustive in d and a; `logs/sr167_admissibility.log`).** I checked every NSW-prime m listed in the packet with h > 18: m = 5, 7, 19, 29, 47, 59, 163, 257, 421, 937, 947, 1493. The largest h has 572 digits. For each:
- ord_h λ = m;
- the only diagonal powers λ^d ∈ F_h are 1;
- (a) has no violations;
- (b) has exactly the solutions {(1, m−1), (m−1, 1)};
- of the four roots of t² − 6t + 1, exactly λ and λ⁻¹ have norm 1.

Controls:
- m = 3 (h = 7 < 18): (a) fails at d = 0, e.g. k′ = 8, k = 1 ≡ 8 mod 7. This is as expected, and the Lemma excludes it.
- 2 is a quadratic residue mod every prime factor of h_m for all odd m ≤ 61 (the split case is universal). Composite h_m (m = 9, 11, 13, 15, 21) are listed for reference; no claim is made there.

**Applied fix.** In the TRACE-167 boundary, the canonical note, phase-2 §C4 and the manuscript remark, I replaced "λ^a + λ^b = λ + λ⁻¹ forces {λ^a, λ^b} = {λ, λ⁻¹}" with the norm-1 argument above. I also added the ord_h λ = m step and the remark that O/hO ≅ F_h × F_h is always split.

**Status recommendation: proved** (analytic proof, with the second-reader repair, plus an exhaustive check for all 12 listed NSW-prime m with h > 18). If the owner wants the repaired line read by a third person, revert to verification-pending. The repair is elementary.

### B2.2 TRACE-169 (Prop C). Verdict: **confirmed (correct for every odd m, including p² | h); no fix needed.**

**Re-derivation from the definitions.** For odd m, phase 1 gives the following, and the table checks them:
- D = 4h²;
- g′ = 2h;
- V = O/(λ^m − 1) ≅ Z/h × Z/4h;
- Rad = V[4] = V₂ ≅ Z/4;
- 𝒮 = ½𝟙 + V^_odd (TRACE-165).

1. **Splitting.** V = V₂ ⊕ V_odd. Since gcd(4, h) = 1, ℬ(V₂, V_odd) = 0 and ⟨V₂, (V_odd)^⟩ = 0, and 𝒬 is additive across the sum. Hence k_ν(½𝟙 + x) = k^{(2)}_ν · k^{odd}_ν(x). ✔
2. **𝒬 on V_odd takes values in (1/h)Z/Z.** For β ∈ V_odd, h·β = 0 gives h²𝒬(β) = 𝒬(hβ) = 0, and 2h𝒬 ∈ Z. Since gcd(h², 2h) = h, h𝒬(β) ∈ Z. Write 𝒬 = Q_o/h with Q_o a binary quadratic form mod h. ℬ is nondegenerate on V_odd because Rad ⊂ V₂, so the Gram determinant of Q_o is a unit mod h.
3. **Gauss sum.** h is odd and ν is a unit. Completing the square in Σ_{β∈V_odd} e((−νQ_o(β) − L_x(β))/h) gives G(ν)·e(ν̄ Q_o^∨(x)/h), where Q_o^∨ is the inverse form. |G(ν)| = h for a nondegenerate binary form mod an odd h (multiply over the p^e ∥ h). So k^{odd}_ν(x) = (ε_ν/h) e(ν̄𝒬^∨(x)) with |ε_ν| = 1. Consequently k_ν(ξ)·conj k_ν(ξ′) = h⁻² e(ν̄[𝒬^∨(x) − 𝒬^∨(x′)]): the factors ε_ν and k^{(2)}_ν cancel, because |k_ν|² = h⁻² on 𝒮 (Prop R) and |k^{odd}_ν|² = h⁻², so |k^{(2)}_ν| = 1 on 𝒮. ✔
4. **Invariance.** k_ν is invariant under the shift (phase 1, Symmetry [P]: β ↦ λβ preserves Nm). With ν = 1 this gives 𝒬^∨(Tx) = 𝒬^∨(x) for T(x₀, x₁) = (x₁, 6x₁ − x₀), the shift in q-sequence coordinates. ✔
5. **The invariant forms are multiples of q.** Instead of the eigenvalue argument (μ² − 1 a unit), here is a direct computation that needs only 2 invertible. Let G = [[a, b], [b, c]] with TᵗGT = G and T = [[0, 1], [−1, 6]]. Then TᵗGT = [[c, −b − 6c], [−b − 6c, a + 12b + 36c]], so c = a and b = −3a. Hence 𝒬^∨ = c·(x₀² − 6x₀x₁ + x₁²)/h for one c ∈ Z/h. Nondegeneracy (disc = −8c², with 2 ∤ h) makes c a unit. This holds over Z/h for any odd h, so the case p² | h needs no separate treatment. ✔ (The text's eigenvalue argument is also correct.)
6. **Average.** ν̄ = ν⁻¹ mod 2h runs over the units mod 2h, which reduce bijectively to the units mod h. So E_ν e(ν̄c(r − r′)/h) = c_h(r − r′)/φ(h) = μ(q)/φ(q) with q = h/gcd(r − r′, h) (Ramanujan, Hölder). Summing Φ(ξ)Φ̄(ξ′) over the classes q(x) = r gives exactly Prop C. ✔

**Self-duality remark (part of the TRACE-169 boundary).** I checked it for prime h, which is always the split case R = F_h × F_h, with y = (y₁, y₂), Nm = y₁y₂ and Tr = y₁ + y₂.
- Σ_y e((A·Nm y + Tr y)/h) = h·e(−Ā/h). The sum over y₁ forces y₂ = −Ā. The sign is always +, so the "±" in the text is harmless.
- Orthogonality: Σ_r Kl_T(rs) conj Kl_T(rs′) = h⁻¹ Σ_t G_t(s′)·Ḡ_t(s) = h(h[s = s′] − 1) for s, s′ ∈ (Z/h)^×. Here t = 0 contributes 0 and t ≠ 0 contributes h² e(t̄(s̄ − s̄′)/h). ✔ It needs s, s′ ≠ 0 and h prime, as stated.

**Fresh numerics (`logs/sr169_propC.log`, `logs/sr169_selfdual.log`).**
- **DIRECT for m = 3, 5, 7.** I computed k_ν on all of G (D points) by a 2-D DFT over β = a e₀ + b e₁, (a, b) ∈ (Z/4h)², using **all** units ν mod g′ (6, 40, 238).
  - supp k_ν = ½𝟙 + V^_odd exactly;
  - |h·k_ν| = 1 to 4·10⁻¹⁵;
  - F_direct and F_PropC agree to ≤ 1.1·10⁻¹⁵ (relative) at η = 0.5, 2, 10, 50.
- **Kernel identity.** h²k_ν(½ + x/h)·conj k_ν(½) = e(ν̄ c q(x)/h) with one unit c:
  - c = 2, 22, 188 for m = 3, 5, 7, holding for all units, max deviation 1·10⁻¹⁰;
  - **m = 9** (composite h = 7·199): 24 random units, c = 51, max deviation 8.6·10⁻¹¹, support exact.
- **p² | h** (outside the reach of any full computation): I checked the Gauss sum on the p-primary component V_(p) ≅ (Z/p^e)² directly. For all units mod p^e:
  - **m = 15, 31² | h₁₅ = 7·31²·41**: |k| = 31⁻² to 5·10⁻¹⁴, phase e(ν̄ c_p q(y)/961) with c_p = 399 (a unit mod 31), max deviation 8.5·10⁻¹⁰, 930 units;
  - **m = 21, 7² | h₂₁ = 7²·239·4663**: c_p = 30, deviation 2.7·10⁻¹²;
  - also (15, 7), (9, 7), (9, 199).
- **Self-duality.** The Gauss-sum evaluation holds to 8·10⁻¹² and orthogonality on units to 1.5·10⁻¹¹ for h = 7, 41, 239. The s = 0 row is not covered, as stated: there Kl_T(0) = −1 and the row sums to 0, not −h. Control h = 1393 (composite): orthogonality fails (deviation 2.8·10⁵) and Kl_T(0) = +1, consistent with "h prime" in the statement.

**Status recommendation: proved.**

### B2.3 Consequences for dependants
- **TRACE-170** (Theorem W, Theorem T) and **TRACE-178** (torsion split) depend on 169. With 169 proved, their `proved` state is consistent and no downgrade is needed.
  - Theorem W regroups the pairs of Prop C by Γξ, Γ(−ξ) and the rest, using Lemma P.
  - Theorem T expresses χ_m, defined directly as h⁻²Σ_x exp(iη[S(½ + x/h) − S(½ − x/h)]), as Σ(−1)^a Tr M_a^m. It does not itself use Prop C.
  - TRACE-178 is a regrouping of Prop C by r ≡ 0 mod p.
- **TRACE-168** is unaffected: it never relied on 167.


## Final statuses after the second reading

| ID | Status |
|---|---|
| BGS-TRACE-163 | proved |
| BGS-TRACE-164 | conditional |
| BGS-TRACE-165 | proved |
| BGS-TRACE-166 | proved |
| BGS-TRACE-167 | proved (upgraded by second reader; proof fix applied) |
| BGS-TRACE-168 | proved |
| BGS-TRACE-169 | proved (upgraded by second reader) |
| BGS-TRACE-170 | proved |
| BGS-TRACE-171 | proved |
| BGS-TRACE-172 | proved |
| BGS-TRACE-173 | proved, computer-assisted, directed-rounding constants (upgraded by second reader, B1 93/93) |
| BGS-TRACE-174 | conditional |
| BGS-TRACE-175 | proved |
| BGS-TRACE-176 | conditional |
| BGS-TRACE-177 | open (numerical-only) |
| BGS-TRACE-178 | proved |
| BGS-TRACE-179 | open |
| BGS-TRACE-180 | open |
| BGS-TRACE-181 | open |
| BGS-TRACE-182 | open |

Statuses are cross-checked against the claims JSON after regeneration (see the deposit).
