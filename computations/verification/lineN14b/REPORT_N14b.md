# REPORT_N14b — subgroup-C′ lemma: what is proved, what is not

**Target.** E_{y∈H_d}|r(y)| ≤ e^{o(p)}·d^c·(1.2744/μ*)^{3p}, uniformly in d | h_p, with c < c* = 0.387.
Write d = λ^{θp}. The mixed-class budget then needs c·θ·ln λ < −ln(ε·0.2945) = 0.3411.

**Outcome.** The lemma is **not proved** for c < 0.387. The best rigorous-type exponent is
**c_B = 0.7375 [P-sketch on C′'s [CA] inputs]**. This extends the C′ range from d ≤ 1.4065^p to d ≤ 1.588^p.
The remaining input is isolated in §3.

## 1. Pre-flight: the c each argument gives

Sources: code/a_cvalues.py, code/b_g0.py, logs/*.json.

| arg | idea | c | d covered | status |
|---|---|---|---|---|
| A | trivial index loss | 1 | ≤1.4065^p | [P] (= C′) |
| B | H is (p−log_λ d)-separated; C′ on that window; leftover by sup | **0.7375** | ≤1.588^p | [P-sketch] |
| B′ | B, with the Prop-E majorant sup on the leftover | 0.95 | ≤1.43^p | worse |
| C | min-shift + restricted pressure | ≥0.826 at θ=½ (slow fixed point μ*⁶/λ vs R₃=1.4055) | — | dead near θ=½ |
| D | Poisson/collision automaton with target ideal 𝔟 = Ann H | c_D = 0.899 (g(0) = (Σ\|J_a(1.8)\|)² = 5.614 > threshold 3.58) | — | dead [N] |
| E | stay counting on H (geometry of numbers) | no stay excess for s ≤ p−log_λ d | — | needs H-equidistribution of non-stay segments (D1-type; dead per N12b) |

**Why (D) cannot become a finite certificate.**
- The Prop-E majorant g is a tied-to-twist product with average 1, but its sup is g(0) = 5.61. That is within 4% of λ = 5.83, so it is far too peaked at the slow twist.
- Nonzero targets b ∈ 𝔟 satisfy |b′| ≥ 1/(40dV). Integer carries therefore grow like λ^p/(dV), so no bounded-carry automaton exists.
- The congruence automaton mod 𝔟 is exactly the H-average restated, so it is circular. [P]

## 2. What is proved

**Lemma 1 (separation) [P].**
- H_d = (1/h)𝔡 with N𝔡 = d (admissible: N(γ) ≥ d for γ ∈ 𝔡∖0).
- If x ≠ y ∈ H_d are δ-close for n steps, the lifted difference γ/h satisfies |N γ| ≤ Cδ²h²λ^{−n}. Hence λ^n ≤ Cδ²h²/d.
- So H_d is (n,δ)-separated for n = p − log_λ d + O(1), uniformly in d.
- Also #(H_d ∩ B_n(z)) ≤ 1 + Cλ^{p−n}/d for every n, uniformly over translates z.

**Lemma 2 (B) [P-sketch].** E_{H_d}|r| ≤ e^{o(p)}·d^{0.7376}·(1.2744/μ*)^{3p}.
- *Split.* |Ẑ| ≤ ‖P_p‖_op‖P_p‖²_HS and P_p = P_ℓ∘F^n · P_n with ℓ = log_λ d. This gives |Ẑ| ≤ ‖P_ℓ‖³_op·‖P_n‖_op‖P_n‖²_HS.
- *Leftover.* sup‖P_ℓ‖ ≤ CΛ_free^ℓ, with Λ_free ≤ 1.9656 [CA].
- *Window.* Lemma 1 plus C′'s Bowen-ball, Hölder and Prop-E steps on the time-n window give E_{H_d}(…) ≤ e^{o(p)}(Λr₂)^n. This uses |H_d|·vol B_n ≍ 1.
- *Exponent.* The ratio is Λ_free³/(Λr₂) = 3.669 per leftover step, so c = ln 3.669/ln λ = 0.7375.
- Not written line-by-line: re-running C′'s residue-class Hölder on a window of length n < p (routine).

**Consequence [P-sketch, asymptotic].** The mixed classes are controlled whenever every proper divisor of h_p is ≤ 1.588^p·e^{−o(p)}. That means h_p is prime or a balanced semiprime (q_min ≥ h_p/1.588^p).
- For p ≤ 89 [N, constants ignored], the only newly covered composite is p = 31 (424577·865087, θ_max = 0.250 < 0.262).
- 11, 13, 17, 23, 37, … are not covered (θ_max between 0.279 and 0.460).

## 3. Remaining input (stated exactly)

**(H-eq) [H].** For the C′ potentials, a full-time Bowen-ball comparison on H_d,
E_{H_d} e^{S_pφ} ≤ e^{o(p)}·d^{c}·∫e^{S_pφ}, with c < 0.387,
must hold beyond the separation time p − log_λ d (Ehrenfest-type equidistribution of the S-invariant sublattice).

- Numerically c_est ≈ 0.1–0.27 (N13b) [N].
- Every argument above loses on the slow fixed point inside the last log_λ d steps. Lemma 1 shows that region is geometrically unavoidable for d ≥ 1.588^p unless equidistribution beyond separation is used.

Nothing pushed. Jobs ran at nice 19, sequentially (each < 2 s).
