# The ε-digit span of a norm shell

Status: **[P]**. The constant is sharp [P], by an explicit class. The census through shell 16 is a check of the same statement [P-computation], not the proof.

This is the length that Prop. K (BGS-TRACE-332) used as a sketch: a bad cluster in shell j has digit span ≤ 2j for j ≥ 5, hence exclusion length ℓ ≤ 2j + g_0. The argument below replaces that sketch.

## 1. The word

Let ε = 1 + √2 and ε′ = 1 − √2. Then ε + ε′ = 2, εε′ = −1, and ε² = 2ε + 1 = 3 + 2√2 =: λ. In particular |ε′| = ε^{-1}, and the sequence u_k = ε^k obeys

u_k = 2 u_{k−1} + u_{k−2}.

Write α = a + b√2 ∈ ℤ[√2], N(α) = a² − 2b², and μ = (√2/4) α = b/2 + (a/4)√2. Let ε^k = p_k + q_k √2 with p_k, q_k ∈ ℤ, p_0 = 1, q_0 = 0, and

p_{k+1} = p_k + 2 q_k, q_{k+1} = p_k + q_k.

The archimedean orbit and its conjugate are

ξ_k = σ₁(μ ε^k) = (U_k + V_k √2)/4, ξ′_k = (U_k − V_k √2)/4,

U_k = 2(b p_k + a q_k), V_k = a p_k + 2 b q_k.

Their sum T_k = ξ_k + ξ′_k = b p_k + a q_k is an integer, and |ξ_k ξ′_k| = |N(α)|/8. Both sequences satisfy the linear recurrence, so T_k = 2 T_{k−1} + T_{k−2}.

The balanced representative is red(x) = x − ⌊x + 1/2⌋ ∈ (−1/2, 1/2]. The code twists, which are the coordinates fed to the digit word in `computations/verification/lineN14/code/digits.py`, are

τ_k = red(ξ_k) if k is even, τ_k = −red(−ξ_k) if k is odd.

Set n_k = ξ_k − τ_k. Then n_k = ⌊ξ_k + 1/2⌋ for even k, and n_k = −⌊1/2 − ξ_k⌋ for odd k. In both cases n_k ∈ ℤ. The odd formula equals the even one unless red(ξ_k) = −1/2, in which case the odd twist is larger by 1 and lands in [−1/2, 1/2).

Define

E_k = −(τ_k − 2 τ_{k−1} − τ_{k−2}) = n_k − 2 n_{k−1} − n_{k−2}.

The second equality is the recurrence for ξ. The span is the inclusive length of the support: if every E_k vanishes, the span is 0; otherwise

span(α) = max{k : E_k ≠ 0} − min{k : E_k ≠ 0} + 1.

Internal zeros count. This is `len(w)` in the N14 enumerator. Multiplying α by ε shifts k by one and preserves the span.

## 2. Where the letters can be nonzero

Assume N(α) ≠ 0, so neither embedding of μ vanishes. The map k ↦ |ξ_k| = |σ₁(μ)| ε^k is strictly increasing, and k ↦ |ξ′_k| is strictly decreasing.

Let k_L be the real number with |ξ_{k_L}| = 1/2, and k_R the real number with |ξ′_{k_R}| = 1/2. Then

k_R − k_L = log_ε(4 |ξ_0 ξ′_0|) = log_ε(|N(α)|/2).

**Left.** If k < k_L, then |ξ_k| < 1/2, so red(ξ_k) = ξ_k and ⌊ξ_k + 1/2⌋ = 0. A half-integer has absolute value at least 1/2, so red(ξ_k) ≠ −1/2 and the odd branch agrees: −red(−ξ_k) = red(ξ_k). Thus n_k = 0 for every integer k < k_L, even or odd. If k ≤ ⌈k_L⌉ − 1, the three indices k, k−1, k−2 are all strictly less than k_L, so E_k = 0.

**Right.** If k > k_R, then |ξ′_k| < 1/2. Hence red(ξ_k) = red(−ξ′_k) = −ξ′_k, because −ξ′_k lies in (−1/2, 1/2), and n^{ideal}_k = T_k. The odd branch differs from red only when red(ξ_k) = −1/2. Here red(ξ_k) = −ξ′_k has absolute value strictly less than 1/2, so the two branches agree and n_k = T_k for both parities. If k ≥ ⌊k_R⌋ + 3, the three indices k, k−1, k−2 are all strictly greater than k_R, so n equals T on them. The integer sequence T satisfies the recurrence, and E_k = 0.

**Support.** Every nonzero letter lies in the integer interval [⌈k_L⌉, ⌊k_R⌋ + 2], when that interval is nonempty. Its length is at most

⌊k_R⌋ − ⌈k_L⌉ + 3.

The quantity ⌊k_R⌋ − ⌈k_L⌉ is an integer and is at most k_R − k_L, hence at most ⌊k_R − k_L⌋. Therefore

span(α) ≤ ⌊log_ε(|N(α)|/2)⌋ + 3.

If the interval is empty the span is 0, and the same upper bound holds whenever the right-hand side is nonnegative. If |N| = 1, then |N|/2 = 1/2 < 1 and the logarithm is negative; the right-hand side is at least 2, and the census below records span 1 for α = 1.

## 3. Shells

Let 2^j ≤ |N(α)| < 2^{j+1} with j ≥ 0. Then |N|/2 < 2^j, so

log_ε(|N|/2) < j log_ε 2

and, because the inequality is strict,

span(α) ≤ ⌊j log_ε 2⌋ + 3.

**Comparison with 2j.** Expand (1+√2)^4 = 17 + 12√2. Then 8 < 17 + 12√2 if and only if 15 < 12√2 if and only if 225 < 288, which is true. So 2^3 < ε^4 and log_ε 2 < 4/3. For an integer j ≥ 3 one has 2 − 2/j ≥ 4/3 > log_ε 2, hence

j log_ε 2 < 2j − 2.

Any real x < 2j − 2 satisfies ⌊x⌋ ≤ 2j − 3, so ⌊j log_ε 2⌋ + 3 ≤ 2j. This is the inequality the sketch quoted for j ≥ 5. It holds for every j ≥ 3.

**A rational slope.** The same expansion gives 32 < 17 + 12√2, because 15 < 12√2 is the same comparison 225 < 288. So 2^5 < ε^4 and log_ε 2 < 4/5. Therefore j log_ε 2 < (4/5) j and

span(α) ≤ ⌊4j/5⌋ + 3.

(The floor drops by at least one extra unit when 4j/5 is an integer, which only helps the bound.)

## 4. The constant 3 is achieved

Take α = 2, so a = 2, b = 0, N = 4. Then μ = √2/2 and 4ξ_k = V_k √2 with the powers below. Direct evaluation of n_k:

| k | (p_k, q_k) | 4ξ_k | n_k | E_k |
|---|---|---|---|---|
| −2 | (3, −2) | −8 + 6√2 | 0 | 0 |
| −1 | (−1, 1) | 4 − 2√2 | 0 | 0 |
| 0 | (1, 0) | 2√2 | 1 | 1 |
| 1 | (1, 1) | 4 + 2√2 | 2 | 0 |
| 2 | (3, 2) | 8 + 6√2 | 4 | −1 |
| 3 | (7, 5) | 20 + 14√2 | 10 | 0 |

The support is {0, 1, 2}, so the word is (1, 0, −1) and the span is 3. Since ε > 2 > 1, one has 0 < log_ε 2 < 1, and ⌊log_ε(4/2)⌋ + 3 = 3. Equality holds.

The same arithmetic gives the endpoints predicted by §2. |ξ_{−1}| = |4 − 2√2|/4 < 1/2 and |ξ_0| = √2/2 > 1/2, so ⌈k_L⌉ = 0. |ξ′_0| = √2/2 > 1/2 and |ξ′_1| = |N|/(8|ξ_1|) < 1/2, so ⌊k_R⌋ = 0 and the proved interval is exactly {0, 1, 2}.

## 5. What the census checks, and what it does not

`numerics/span_exact.py` evaluates E_k by integer comparisons only (the predicate m ≤ U + V√2 is a comparison of squares, and it is never an equality for V ≠ 0). It was cross-checked against mpmath at 80 decimal places on 200 random linear forms, on 300 absolute-value tests, and on the carries n_k for 40 random (a, b) and k ∈ [−12, 16).

On every one of the 5109 fundamental-domain classes in `computations/verification/lineN14/logs/a_enum.jsonl` (shells j ≤ 12):

- the exact span equals the stored `span`;
- the exact maximal internal zero-run equals the stored `zr`;
- the stored integer `word` differs on 2182 classes.

The word mismatch is the binary64 letter passed through `int()`, which truncates. High-precision mpmath reproduces the exact integers, including the word (1, 1, −1) for α = 3 where the file stores (1, 1, 0). Bad-set membership at g_0 ∈ {2, 3, 4, 5, 6} uses `zr`, which matches, so this audit does not move the finite bad set of Thm A. The stored words are not exact digits.

The same program re-enumerated the fundamental domain through shell j = 16 (40 845 classes at j = 16; the j ≤ 12 list reproduces `a_enum.jsonl` exactly) and extended the inequality to every such class. The difference span − ⌊log_ε(|N|/2)⌋ takes only the values 2 and 3 (43 304 and 38 405 classes). No class exceeds +3. Forty random classes were multiplied by ε and by ε²; the span was unchanged.

The census is finite. The proof in §2–§3 is the general statement. The census is the check that the support cut, the odd branch, and the floor arithmetic were implemented as the proof describes, on every class that the existing finite KP sum actually uses and on four further shells.

## 6. Boundary

The theorem bounds the digit span of this code. It does not bound |r_A r_B|, it does not prove H1, and it does not choose the background renormalisation. Those are separate. The way the length enters the Kotecký–Preiss tail is `04_propK_sharp.md`.
