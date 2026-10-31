# REPORT_N7b: gap (b) of Ω♯ (levels other than h_p) for the refutation of frozen R′ along m = 3p

*2026-10-31, ~22:30 Asia/Yekaterinburg (UTC+5). Dir `/workspace/bgs-lineN/N7b`; running log NOTES_N7b.md. Nothing pushed; N–N7 files only read.*

Labels: **[P]** proved (mod the named standing inputs); **[CA]** arb ball arithmetic (python-flint 0.9.0); **[N]** floating-point numerics,
no error control; **[H]** heuristic. "Standing inputs" = those of N6 Theorem R♯ (Line F/J/J3/L16 trace representation, TRACE-197/207 twisted
identity at an arbitrary conductor, TRACE-212/213, Lemma O1/Prop E, Lemma I, the N4 Λ certificates).

## 0. Verdict

**Gap (b) is not closed, and R′ is not refuted.** What is new:

| # | Result | Label |
|---|---|---|
| B0 | **Bookkeeping.** At non-h_p levels, Lin splits into conductor-c pieces carried to every level d = ce with weight n_e/e². Each conductor splits further into CRT *patterns* (c, 𝔞), where 𝔞 ∣ c is the isotropic ideal part. A pattern has weight ≤ 2^{ω(c)}·N𝔞 per point and *effective index* ι(c,𝔞) := c²/N𝔞, with c ≤ ι ≤ c². Prime powers fit the same scheme. | [P] |
| B1 | **8E at every level: done.** The sup bound \|Ẑ_E\| ≤ C·Λ_E^m with Λ_E ≤ 0.4915932 < T′ = 1.4278537 removes 8E from all of Ω♯, for (a) as well as (b). Together with N7's (±2,16) floor, **only 8V remains**. | [P + CA] |
| B2 | **Block-split Bowen bound (Prop. B1).** Fix η > 0. For p ≥ p_η (effective, not computed), every 8V pattern with ι(c,𝔞) ≥ λ^{(κ+η)p}, where **κ ≤ 0.7375915**, contributes ≤ e^{−η′p}F_m in total. So unit points at **any** conductor c ≥ λ^{0.36880p} (rank p or 3p, prime or composite, K_p-type and mixed included) are done. For c ∣ h_p this means log_λ(h_p/c) < 0.1312p. Theorem C plus index loss at the relaxed target only reaches 0.0968p, and at the old target 0.0061p. This partly removes the N2 "2.617 barrier" for unit points at K_p levels. | [P + CA] |
| B3 | **Barrier.** Any bound of the form (lattice points per Bowen ball) × (Lebesgue integral of a majorant ≥ the cocycle norm) needs ι ≥ λ^{p/2 − o(p)}. A **fully isotropic** pattern has ι = c ≤ L* = h_p·e^{o(p)}, so it lies at or below this barrier at every admissible level. Unit patterns are blocked below c ≈ λ^{p/4}. | [P] (about the majorant, not about the sums) |
| B4 | **Floor refinements.** A single level d is absorbed by Dev_d ≥ −n_d\|Z\|²/d² iff d ≳ 858·h_p/(δ′p). Hence: (i) the level 7h_p costs ≤ 105/p of F_m (≤ 9% at p = 1165), so it can be floored, which also removes the 7h_p isotropic and mixed classes from gap (a); (ii) every level h_p·e (e ∣ K_p, e > 7) costs ≤ 143/p² of F_m; (iii) **no** proper divisor of h_p can ever be floored (deficit factor ≥ 1716). Counting divisors in the window therefore cannot help. | [P] |
| B5 | **Theorem W at the relaxed target.** c_W: 10^{−25.62} → **10^{−18.62}** (k = 10, q₀ = 10^{9.3}). Non-vacuous for p ≳ 10^{18.9}. W⁺ constants follow: c_N ≈ 10^{−82.3}, beating Weil only for p > 10^{191}; isotropic (Cochrane–Pinner) ≈ 10^{−73.5}p³. Still polynomial in p, so the window hardly shrinks. | [CA] (W⁺: same conditional status as before) |
| B6 | **Residual set R(b), stated exactly** (§6). If h_p is prime, R(b) consists only of divisors e of K_p/7 with e < D₀ and ι < λ^{0.7376p}. The fully isotropic pattern at every prime Q ∣ K_p/7 with c_W′p² < Q < D₀ is always in it. | [P] |
| B7 | **Subsequence route (idea 1) fails heuristically.** It needs h_p prime **and** K_p/7 free of prime factors below D₀ ≈ h_p/p. Heuristically that holds for only finitely many p (Σ(log p/p)² < ∞). Census for p ≤ 3989: h_p is BPSW-PRP 13 times (heuristic 14.8), K_p/7 11 times (9.1), **both only at p = 7** (2.2). Infinitude of either is open. | [N] + [H] |
| B8 | **Numerics** (o_levels-type, beyond p = 5). All conductors c ≤ √h_m with c ∉ {1, 7, h_p, 7h_p}, all patterns, at p = 5, 7, 11, 13, 19, plus exact isotropic lines at rank-3p primes for p = 19, 29, 37, 41. The largest pattern-to-family ratio falls from 0.45 (p = 5) and 3·10⁻² (p = 11, unit points at 353 ∣ h_11) to 6·10⁻⁴ (p = 13) and < 10⁻⁸ (p = 19). At rank-3p primes for p = 29–41 it is 10⁻¹⁷–10⁻²⁶. Max per-point rate \|Ẑ\|^{1/m}: ≤ 1.02 for p = 19, 0.87–0.97 at the rank-3p iso lines (target 1.428). | [N] |
| B9 | **Slow-time reformulation and data.** Visits of a level-c orbit to the box around z₄ correspond to small-norm elements in one multiplicative coset α⟨ε⟩ ⊂ (O/2√2cO)^×. [N]: max slow time ≤ 2.06·log_λ c (units, per 2log_λ c), ≤ 1.85·log_λ c (iso), over p ≤ 79 and c ≤ 3·10⁶. This supports a pointwise route at rank-3p levels (§8). | [P] reformulation, [N] data, [H] route |

**Plain terms.** Every non-h_p piece of 8V is now one of two things. It is either done (unit-like patterns with ι ≥ λ^{0.738p}, all of 8E, floored levels, Weil-range primes), or it is a pattern with small effective index. The small-index patterns are chiefly the fully isotropic points at every conductor below D₀ ≈ h_p/p, and everything at conductors below λ^{0.369p}. For the first class, B3 proves that no averaging (Bowen/Lebesgue) argument can work. They need a **pointwise** input: per-orbit growth along deterministic cat-map orbits, i.e. the same kind of input gap (a) needs. Numerically they are negligible by 8–26 orders of magnitude from p = 19 on.

## 1. Bookkeeping (B0) [P]

- **Conductor decomposition.** Lin_d(ρ) = (2/d²)Re(Z̄_ρ Σ_{β≢0} κ_d(Nβ)Ẑ(β)) (N6). A β mod d has exact conductor c ∣ d, i.e. β = eβ′ with d = ce. For squarefree d with gcd(c,e) = 1, the J3/Ramanujan factorisation κ_d(e²u) = κ_c(u)·κ_e(e²u) and κ_e(e²u) = κ_e(0) = n_e give:
  Lin_d = Σ_{c∣d} (n_e/e²)·Λ_c, with Λ_c := (2/c²)Re(Z̄ Σ_{β exact cond c} κ_c(Nβ)Ẑ(β)).
  This is the TRACE-228 inheritance. The multiplier Σ_{e} n_e/e² ≤ Π_{q∣h_m}(1 + 1/q) = 1 + o(1), since every q ≠ 7 is ≥ 2p+1. So (b) amounts to one-sided bounds on |Λ_c| for the relevant c. Levels above the floor threshold use Dev instead (B4).
- **Patterns.** For squarefree c, write β by CRT. At each q ∣ c, β_q is either isotropic (Nβ ≡ 0 mod q: it lies on one of the two lines 𝔮, 𝔮̄) or a unit. Let 𝔞 = Π_{q iso}(chosen prime above q). Then β ∈ 𝔞 and |κ_c(Nβ)| ≤ Π_{iso}(q−1+1)·Π_{unit}2 ≤ 2^{ω(c)}N𝔞. Here "+1" is the excluded label t_b; J3: |W| ≤ 2/q² (unit) and (q−2)/q² (iso).
- **Prime powers** (N6 §6). At q^a ∥ c, κ is supported on q^{a−1} ∣ Nβ. With β ∉ qO this means β ∈ 𝔮^{i} (or 𝔮̄^{i}), i ≥ a−1, and |κ| ≤ 2q^{i} = 2N(𝔮^{i}). So the same "weight ≤ 2^ω N𝔞" holds with 𝔞 = 𝔮^{i}.
- **The pattern point set** P(c,𝔞) ⊂ T² = (K⊗R)/O^∨ is λ-invariant (λ𝔞 = 𝔞) and lies in the lattice L_𝔞 := (1/c)𝔞 + O^∨ = (2√2c)^{−1}𝔞, using gcd(c,8) = 1. Its size is ≤ ι(c,𝔞) = c²/N𝔞. Every v ∈ L_𝔞∖0 has |N(v)| ≥ N𝔞/(8c²).
- **What belongs to (b).** All (c,𝔞) with c ∉ {1, 7, h_p}. Patterns at c = 7h_p and h_p·e are floored (B4) and so leave Ω♯. The N6-F7 mixed classes at h_p (isotropic at some q_i ∣ h_p, unit at others) have c = h_p and stay with gap (a). For composite h_p they have ι = h_p²/N𝔞 ≥ h_p·q_min, so B1 removes those with ι ≥ λ^{0.7376p}.

## 2. Removals

**2.1 (±2,16).** Removed at all levels by N7 (NOTES_N7 21:10): |Z_(±2,16)| ≤ 2.273·10⁵·1.6355^m [CA], plus the floor and σ(h)/h. Not redone here.

**2.2 8E by the sup bound (B1) [P + CA].**
- The cross term at any level is 2Re(Z̄_ρ·κ·Ẑ(β)), with Ẑ = Ẑ_V + Ẑ_E.
- |Ẑ_E(y)| ≤ ‖J‖·‖L_{τ_0}‖₁·‖Π_{i≥1}L_{τ_i}‖ ≤ C·0.4915932^{m} for every y. This uses the N4 Schur certificate, uniform over all twists, plus Lemma I.
- Σ_β|κ_c(Nβ)| ≤ 3^{ω(c)}c², and Σ_c 3^{ω(c)} ≤ e^{O(p/log p)}.
- So the total over all (b) and (a) points is ≤ e^{o(p)}·|Z|·0.4916^m, compared with F_m ≥ c₀p|Z|·1.4278^m.
- Arb check: `logs/b1_const.out`.

**2.3 Floor (B4) [P].**
- Σ_ρ Dev_d(ρ) ≥ −2n_d|Z₈|²/d² ≥ −2|Z₈|²/d, and F_m ≥ 2.330·10⁻³·p|Z₈|²/h_p (N6 constant after N6-F5).
- So any set D of levels with Σ_{d∈D} 1/d ≤ 1.165·10⁻³·δ′p/h_p costs ≤ δ′F_m.
- 7h_p: n ≤ 6h_p, cost = (12/49)/(2.330·10⁻³p) = 105.1/p of F_m.
- h_p·e: cost ≤ 858/(ep) ≤ 143/p² each, so the whole family (with the 7·h_p·e levels) costs ≤ δ′F_m if τ(K_p) ≤ 3.5·10⁻³δ′p².
- A proper divisor d ≤ h_p/(2p+1) costs ≥ (2p+1)/(1.165·10⁻³p) ≥ 1716× budget. **[P] negative:** proper divisors of h_p, and K_p-divisors below ~858h_p/p, are out of reach of any floor or divisor-counting argument, whatever ω or τ of Lucas numbers is.

## 3. Proposition B1 (block-split Bowen bound) [P + CA]

**Lemma B1.1 (lattice Bowen) [P].**
- Let S ⊂ T² be λ-invariant and contained in a lattice L ⊃ O^∨ with |N(v)| ≥ ν > 0 for v ∈ L∖0. Let φ be continuous with modulus ω, and n ≥ 1.
- Then for every ε ∈ (0, ε₀):
  Σ_{y∈S} e^{S_nφ(y)} ≤ C_ε·(1 + 4ε²λ^{−n}/ν)·λ^{n}·e^{nω(2ε)}·∫e^{S_nφ} dLeb.
- *Proof.*
  1. On the Bowen ball B_n(y,ε) ⊇ y + {|v_u| ≤ ελ^{−n+1}, |v_s| ≤ ε}, of measure ≍ ε²λ^{−n}, we have S_nφ ≥ S_nφ(y) − nω(2ε). Average over the ball.
  2. A point z lies in B_n(y,ε) for at most #{v ∈ L : |v_u| ≤ 2ελ^{−n+1}, |v_s| ≤ 2ε} points y ∈ S.
  3. For L = (2√2c)^{−1}𝔞, this count is ≤ 1 + C·8c²XY/N𝔞. Scale to α ∈ 𝔞. A nonzero α in the box has (α) = 𝔞𝔠 with N𝔠 ≤ M := 8c²XY/N𝔞, so none exist if M < 1. For each 𝔠, the generators ±αε^k in the box form a run of length ≤ 1 + log_ε(M/N𝔠), and Σ_{N𝔠≤M}(1 + log(M/N𝔠)) ≤ C·M. ∎

**Proposition B1.**
- *Statement.* Let κ := 3(ln Λ − ln T′)/(2 ln Λ − ln r₂), with Λ = Λ_free^{8V} ≤ 1.9656353, r₂ = r₂^{8V}(4000) ≤ 1.0529012 and T′ = μ*_lo·λ^{−1/6} ≥ 1.4278537. Then κ ≤ 0.7375915 [CA]. κ is increasing in Λ and r₂, because 2ln T′ − ln r₂ > 0, so upper inputs are valid.
- For every η > 0 there is p_η (effective, not computed) such that for p ≥ p_η:
  Σ_{c∣h_m, 𝔞: ι(c,𝔞) ≥ λ^{(κ+η)p}} |Λ^{V}_{(c,𝔞)}| ≤ e^{−η′p}·F_m.
- *Proof.*
  1. **Trace identity.** Ẑ_V(y) = Σ a_F Tr(J_F X(y)), with X(y) = Π_{i<m}L_{τ_i(y)} (standing input; N2 Theorem B and N2-F2 for c = h_p, the same identity at any conductor).
  2. **Split.** Write X = X₄X₃X₂X₁, where X₁ and X₃ are n-step blocks starting at steps 0 and n′. Then |Tr(JX)| ≤ ‖J‖·‖X₁‖_HS‖X₂‖‖X₃‖_HS‖X₄‖ (Schatten–Hölder). The op-norm blocks are ≤ C_Iκ_F·Λ^{len} (Lemma I + N4 [CA]). Also ‖X₁(y)‖²_HS ≤ C·e^{2S_nψ^{HS}_k(y)}, the Theorem C potential with boundary constants.
  3. **Sum over the pattern.** 2‖X₁‖‖X₃‖ ≤ ‖X₁(y)‖² + ‖X₁(T^{n′}y)‖², and S is T-invariant, so Σ_y|Ẑ_V| ≤ C·Λ^{m−2n}·Σ_y e^{2S_nψ(y)}.
  4. **Bowen.** Lemma B1.1 with ν = N𝔞/(8c²), together with Prop E (∫e^{2S_nψ} ≤ C·r₂^n·e^{ηn}), gives Σ_y|Ẑ_V| ≤ C_η·Λ^{m−2n}·max(λ^n, ι)·r₂^n·e^{2ηn}.
  5. **Weights.** With weight ≤ 2^ω N𝔞, normalisation 2/c² and n = ⌈log_λ ι⌉ ≤ m/2 (if ι > λ^{m/2}, take n = m/2):
     |Λ^V_{(c,𝔞)}| ≤ C_η·2^{ω}|Z|·Λ^{m−2n}·r₂^{n}·e^{2ηn}.
  6. **Compare with F_m.** F_m ≥ c₀p|Z|T′^m. The exponent condition (1−2ν)ln Λ + ν ln r₂ < ln T′ − η″, with ν = n/m, is n > (κ+η)p. Summing over ≤ τ(h_m)·3^{ω} = e^{O(p/log p)} patterns costs a subexponential factor. ∎
- **Consequences.**
  - **Unit patterns** (ι = c²): every conductor c ≥ λ^{(0.36880+η)p} is done, whatever its rank or factorisation. This includes K_p primes, mixed c₁c₂, and 7×.
  - **c ∣ h_p:** done iff log_λ(h_p/c) < 0.13120p (using h_p ≤ λ^{p/2}). By comparison, Theorem C's periodic form with Bowen at n = p and index loss (h_p/c)² gives 0.09677p at the relaxed target.
  - **Partially isotropic patterns** need c²/N𝔞 ≥ λ^{0.7376p}.
  - **Fully isotropic patterns** need c ≥ λ^{0.7376p} > D₀, so **never**.
  - **Possible refinement [H].** Using J-th Schatten moments (a 2J-letter collision automaton, as in Prop E) instead of HS: if r_J were at its slow-point lower bound μ*^J/λ, the threshold would drop to 0.514p (J = 4) and 0.474p (J = 10). The true r_J are larger and uncertified. B3 shows the limit of this whole family of methods is p/2 for ι.

## 4. Barrier B3 [P, about the majorant]

- Any bound of the form Σ_{y∈S}|Ẑ| ≤ N_ball·λ^{n}·∫G, with G ≥ Π(block norms) and G ≥ μ*^{(·)} near the fixed point z₄, satisfies (normalised by the pattern weight 1/ι) ≥ Λ^{m−2n}μ*^{2n}/ι ≥ μ*^m/ι.
  - Reason: the n-Bowen ball at z₄ has measure ≍ λ^{−n}, and on it the HS blocks are ≥ μ*^{n}.
- Against the target T′^m = μ*^mλ^{−m/6}, this forces ι > λ^{m/6} = λ^{p/2}.
- A fully isotropic pattern has ι = c. For c ≤ L* = h_p·e^{o(p)} ≤ λ^{p/2}e^{o(p)}/2 this is at or below the barrier.
- The h_p family itself (ι = h_p, true rate exactly μ*λ^{−1/6}) shows the barrier is **sharp**: an averaging majorant cannot tell the generic isotropic points apart from the family.
- This is the precise form of the referee's "Bowen-ball coset averaging loses λ^{1/3} per step".

## 5. Theorem W at the relaxed target (B5) [CA]

- `code/w_relaxed.py` is Line L's `l4_const.py` with exactly one change: the target is set to μ*_lo·λ^{−1/6} (diff in NOTES).
- 8V results (`logs/w_relaxed_8V.jsonl`):
  - OP is certified from k = 10. At k = 9 the rate is 1.45098 > T′.
  - log₁₀c_k: −18.62 (k = 10, q₀ = 10^{9.3}), −18.95 (11), −19.71 (12), −22.53 (15).
  - A (ρ, β) scan at k = 9, 10 (`logs/w_relaxed_8V_scan.jsonl`) gives nothing better.
- Neither 8E (sup bound) nor (±2,16) (floor) is needed any more, so **c_W′ = 10^{−18.62}**.
- Per β the conclusion reads |Ẑ_β^{8V}| ≤ C′((1−δ/2)T′)^m. This gives |Λ_c| ≤ e^{o(p)}|Z|((1−δ/2)T′)^m ≪ F_m, for prime q and 7q with q ≤ c_W′p², isotropic points included. m₁ is effective but not computed.
- **W⁺ (N1 method) with ε′ = 2√c_W′ = 10^{−9.01}:**
  - (3,3) gives c_N′ = ε′⁹/17.31 = 10^{−82.3}, which beats Weil only for p > 10^{191} (was 10^{264.5});
  - isotropic (Cochrane–Pinner) gives 10^{−73.5}r³.
  - Status unchanged: P-cite plus the conditional items listed in N1.
- **Intrinsic limit [P, from N3].** At any prime Q with log_λ Q ≳ ε_F·r, the central ~log_λ Q terms of an isotropic orbit sum are uncancelled, so sup|S| ≥ (log_λ Q)/r. No exponential-sum bound can carry Theorem W past Q ≈ λ^{ε_F r}.

## 6. The residual set R(b) [P]

Fix δ′ and put D₀ := 858·N_D·h_p/(δ′p), with N_D the number of levels below it (in practice D₀ = h_p·p^{−1+o(1)}). After §2–§5, the part of gap (b) still open is

R(b) = { (c, 𝔞) : c ∣ h_m, c ∉ {1, 7, h_p}, c < D₀, c not a prime (or 7×prime) ≤ c_W′p², and ι(c,𝔞) = c²/N𝔞 < λ^{(0.7376+η)p} }  (8V only).

- It always contains the fully isotropic pattern at every conductor in (c_W′p², D₀). It also contains every pattern at conductors c < λ^{0.3688p} outside the Weil range.
- **If h_p is prime:** the conductors below D₀ are divisors e of K′ := K_p/7 (rank 3p), and 7e. The h_p·e levels and 7h_p are floored, and h_p has no proper divisors. So R(b) involves **only rank-3p conductors**, and it is empty iff K′ has no divisor in (c_W′p², D₀) other than Weil-range primes. Roughly: the smallest prime factor of K′ exceeds ≈ √K′/p.
- **If h_p is composite:** each prime q ∣ h_p contributes its fully isotropic pattern below D₀. The same holds for each proper divisor.

## 7. Subsequences (idea 1) and divisor structure (B7)

- **[P]** Zsigmondy and Bilu–Hanrot–Voutier give primitive prime factors, and here every prime factor is primitive and ≥ 2p+1 (≥ 6p+1 for K′). That bounds τ and ω but cannot help: by B4 a single level below ~858h_p/p already exceeds the budget.
- **[H] Heuristic.** P(h_p prime) ≈ e^γ log(2p)/((p/2)log λ) and P(K′ prime) ≈ e^γ log(6p)/(p log λ) (Wagstaff-type, factors restricted to 1 mod 2p or 6p). The event "smallest prime factor of K′ > √K′/p" has the same order, log p/p.
  - So "h_p prime" alone is expected infinitely often (Σ log p/p diverges, as for Mersenne primes).
  - The joint condition needed for R(b) = ∅ is expected only **finitely** often (Σ(log p)²/p² < ∞).
- **[N] BPSW census, all primes 5 ≤ p ≤ 3989** (`logs/c_prp_census_4000.jsonl`):
  - h_p PRP at p = 5, 7, 19, 29, 47, 59, 163, 257, 421, 937, 947, 1493, 1901: 13 cases (heuristic 14.8);
  - K′ PRP at 7, 11, 23, 83, 97, 127, 197, 283, 859, 1913, 3931: 11 cases (heuristic 9.1);
  - **both: p = 7 only** (heuristic 2.2, almost all of it from small p).
- **Conclusion.** Restricting to a subsequence cannot empty gap (b), even conditionally on standard prime-production conjectures. Its best use is conditional on "h_p prime infinitely often" (expected, unproved). That removes the rank-p part, i.e. proper divisors, and leaves only the rank-3p conductors of K′ (§6).

## 8. Numerics (B8, B9) [N] and the pointwise route [H]

**8.1 All (b) conductors** (`code/b_levels.py`, logs `b_levels_p*.{out,json}`).
- Conductors c ∣ h_m, c ≤ √h_m, c ∉ {1, 7, h_p, 7h_p}.
- Exact orbit-reduced enumeration when c² ≤ 6·10⁴ or c is a prime power; otherwise 100–200 random points per pattern.
- rel = (h_p²/c²)·w_g·Σ|Ẑ/Z|/((h_p−2)Re X_{h_p}). This is the absolute (one-sided) pattern bound divided by the family Lin; rel < 1 means the pattern sits below the family term.

| p (m) | conductors | largest rel (where) | max \|Ẑ\|^{1/m} over all (b) points |
|---|---|---|---|
| 5 (15) | 31, 217 (31² ∥ h) | 0.45 (31, units) | 1.03 |
| 7 (21) | 49, 4663 | 1.7·10⁻² (4663, units) | 1.07 |
| 11 (33) | 23, 161, 353, 2471 | 3.0·10⁻² (353 ∣ h_11, units) | 1.30 |
| 13 (39) | 12 conductors (79, 599 ∣ h_p; 313, 4088137 ∣ K′; mixed) | 5.8·10⁻⁴ (79 ∣ h_13, units) | 1.19 |
| 19 (57) | 12 conductors (457, 14593, 7521721 ∣ K′; mixed incl. 457·h_p) | 7.2·10⁻⁹ | 1.02 |

- Exact Ramanujan-signed Lin/Lin_fam: 0.157 (p = 5, c = 31), 7.7·10⁻⁴ (p = 7, c = 49), −5.5·10⁻⁴ (p = 11, c = 23), 2.5·10⁻⁴ (p = 13, c = 79).
- Sampled sums of heavy-tailed |Ẑ| are rough estimates.
- Sampling at the mixed conductor 457·h_p misses the h_p family by design (the family points are inherited copies there and positive).

**8.2 Exact isotropic lines at rank-3p primes** (`code/e_iso.py`, `logs/e_iso.jsonl`): rel_abs and per-point rate.

| p | Q | rel_abs | per-point rate |
|---|---|---|---|
| 19 | 457 | 1.0·10⁻¹¹ | 0.868 |
| 19 | 14593 | 7.5·10⁻¹¹ | 0.930 |
| 29 | 13921 | 2.0·10⁻¹⁷ | 0.908 |
| 37 | 6217 | 3.8·10⁻²³ | 0.894 |
| 41 | 9103 | 4.1·10⁻²⁶ | 0.882 |

- Rank-p primes: p = 37, Q = 223: 3.4·10⁻²³; p = 41, Q = 2297: 3.1·10⁻²¹.
- These agree with the N5 referee (457: 2·10⁻¹¹; 14593: −5·10⁻¹¹ in W′/m units).

**8.3 Slow time** (`code/d_slow.py`, `logs/d_slow_P80_Q3000000.jsonl`; ε = 1/16; p ≤ 79, all prime factors ≤ 3·10⁶).
- Per period, the max over all points (isotropic lines exact; units exact for c ≤ 1500, else 10⁵ samples) of #{i : (τ_i, τ_{i+1}) within ε of (½,½)}:
  - iso: ≤ 1.55·log_λ c (rank p) and ≤ 1.85·log_λ c (rank 3p);
  - units: ≤ 1.23·(2log_λ c) (rank p) and ≤ 2.06·(2log_λ c) (rank 3p).
- The number of windows grows with the rank (short random visits ≈ r·O(ε²)).

**8.4 Reformulation [P].**
- With α = 8cδ̃ ∈ O (δ̃ the small representative of λ^iy − z₄), visits of the orbit of y to the ε-box are exactly the elements γ of the coset α_y⟨ε⟩ mod 2√2cO that have a box representative |γ|, |γ′| ≤ 8cε.
  - The box meets each residue class at most O(1) times, because 11.3ε² < 1.
- A visit through γ lasts ≈ log_λ(64c²ε²/|Nγ|) steps. The norm-±1 elements ε^k form a **single** window.
- So "deep windows" means "small norms in a multiplicative coset of size 2r inside (O/2√2cO)^×". This is a BGK-type question with r ≍ log c, open beyond c ≤ r^C.

**8.5 Pointwise route for rank-3p conductors [H].**
- At a rank-3p conductor Q, Lemma H (with p → m) gives two windows per period m. If, as the data suggest, the deep slow time per period is ≤ 2log_λ Q + o(p) (Conjecture S), then the slow fraction is ≤ 1/3, since Q ≤ λ^{p/2}e^{o(p)}.
- A per-point bound |Ẑ(y)| ≤ e^{o(p)}μ*^{s(y)}Γ^{m−s(y)} would then suffice if the cat-map-constrained growth off the z₄-window satisfies **Γ ≤ 1.233** ((1/3)ln μ* + (2/3)ln Γ < ln T′).
- Observed per-point rates at these levels are 0.87–0.97.
- For rank-p conductors the same route only covers c ≤ λ^{0.167p} (if Γ = 1.233), because there are windows every winding. So proper divisors of h_p in (λ^{0.167p}, λ^{0.369p}) (units) and (λ^{0.167p}, h_p) (iso) would remain. This is why "h_p prime" matters.

## 9. What is proved, what remains, best route

- **Proved here:**
  - B0 bookkeeping;
  - 8E removed from Ω♯ entirely;
  - Prop B1 (unit-like patterns with ι ≥ λ^{0.7376p}, any conductor), with constants [CA];
  - the barrier B3 for all averaging majorants;
  - floor refinements B4 (7h_p and h_p·e removable; proper divisors provably not floorable);
  - relaxed Theorem W c_W′ = 10^{−18.62} [CA];
  - the exact residual set R(b).
- **Remains (8V only):** the patterns of R(b). Chiefly:
  - (i) fully and heavily isotropic patterns at every conductor in (c_W′p², D₀);
  - (ii) all patterns at conductors in (c_W′p², λ^{0.369p}).
  - By B3 both need **pointwise** (per-orbit) growth bounds. That is also the nature of gap (a), so (a) and (b) share one missing tool.
- **Best route [assessment]:**
  1. Work conditionally on "h_p prime for infinitely many p". This is a standard Mersenne-type expectation (13 cases ≤ 3989) and is unprovable today. It removes all rank-p conductors from (b).
  2. For rank-3p conductors, prove:
     - (α) a cat-map-constrained growth bound Γ ≤ 1.233 away from the z₄ window. This is an extremal-norm certificate over twist sequences obeying τ_{i+1} = 6τ_i − τ_{i−1} (mod 1), which is feasible in principle like the N3/N4 free-family certificate;
     - (β) Conjecture S (deep slow time ≤ 2log_λ Q + o(p) per period), via the §8.4 coset formulation.
  3. Unit patterns at rank-3p conductors ≥ λ^{0.369p} are already covered by B1. (β) is the hard arithmetic part: open, BGK-type.
- **Without (1),** proper divisors of composite h_p need the same pointwise machinery on rank-p orbits, where the slow fraction can approach 1. That looks as hard as gap (a).

## 10. Ledger and files

- **[P]:** B0, Lemma B1.1, Prop B1 (as an implication from the certified inputs), B3, B4, §6, §8.4. Lemma I and Bowen constants are finite and not computed; p_η and m₁ are effective and not computed.
- **[CA]:** `code/b1_const.py` → `logs/b1_const.out` (κ ≤ 0.7375915, T′ ≥ 1.4278537, thresholds); `code/w_relaxed.py` → `logs/w_relaxed_8V.jsonl`, `logs/w_relaxed_8V_scan.jsonl` (c_W′).
- **[N]:** `code/b_levels.py` → `logs/b_levels_p{5,7,11,13,19}.{out,json}` (p = 19 json written at the end of its run); `code/e_iso.py` → `logs/e_iso*.{out,jsonl}`; `code/d_slow.py` → `logs/d_slow_P80_Q3000000.jsonl`; `code/c_prp_census.py` → `logs/c_prp_census_4000.jsonl`; `code/t_time.py`.
- **[H]:** §7 heuristic counts; §8.5 route; J-moment thresholds in §3.
- **Inputs used, not re-derived:** N4 Λ certificates, N2 Prop E r₂, N6 F_m constant 2.330·10⁻³ and Prop X (P-sketch, with N7's pattern lemma), N7 (±2,16) removal, Line L OP machinery, TRACE-197/207/212/213/228.
- **Manifest:** `SHA256_N7b.txt`, with its own hash in `SHA256_N7b.txt.sha256`.
