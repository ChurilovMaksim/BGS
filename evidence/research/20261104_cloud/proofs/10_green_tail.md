# The lambda-carry tail is empty past |e| = 14

Status: the cutoff and the geometric Green bound are **[P]**. The numerical constants that appear as balls are **[CA]**, computed in `numerics/green_tail.py` at flint precision 200 and recorded in `numerics/logs/green_tail.json`. They match the closed forms below to a radius under 10^{-57}.

This is the single-window lambda carry, the recurrence

e_t − 6 e_{t−1} + e_{t−2} = v_t, |v_t| ≤ 60.

It is not the joint ε-carry. That system stops at |e| ≤ 51 by a different Green function, ||g_ε||_1 = (2+√2)/4, already recorded in N20. Nothing here shrinks 6145.

## The kernel

Let λ = 3+2√2, μ = 3−2√2. Then λμ = 1, λ+μ = 6 and λ−μ = 4√2. In particular μ = (√2−1)^2 < 1/5.

Write (Tx)_t = x_t − 6 x_{t−1} + x_{t−2}. The even sequence G_t = α μ^{|t|} with α = −1/(4√2) satisfies

(TG)_t = 0 for t ≠ 1, (TG)_1 = 1.

Indeed, μ^2 − 6μ + 1 = 0, so the stencil vanishes off the kink, and the kink computation is

G_1 − 6 G_0 + G_{−1} = 2α(μ−3) = −4√2 α = 1.

Shift by one index and set g_t = G_{t+1} = α μ^{|t+1|}. Then Tg = δ_0. The ℓ^1 norm is independent of the shift:

||g||_1 = |α| (1 + 2μ/(1−μ)) = |α| √2 = 1/4.

(The identity 1 + 2μ/(1−μ) = √2 is μ/(1−μ) = (√2−1)/2, which is the square (√2−1)^2 = μ.) Both evaluations are enclosed in `green_tail.json`: ||g||_1 − 1/4 and 60||g||_1 − 15 are balls about 0.

## Bounded solutions

On bi-infinite bounded sequences the homogeneous equation Tx = 0 has only the zero solution: the general term is A λ^t + B μ^t, and |λ| > 1 forces A = B = 0 if the sequence is bounded in both directions. Therefore a bounded solution of Tx = v is exactly the convolution

e = g ∗ v, e_t = Σ_k g_k v_{t−k},

and

|e_t| ≤ ||g||_1 ||v||_∞ ≤ 60/4 = 15.

Equality holds at a fixed t if and only if v_{t−k} = −60 for every k, because g_k is strictly negative for every k. The letter sequence is then the constant −60, and the carry is the constant 15:

e_t − 6 e_{t−1} + e_{t−2} = 15 − 90 + 15 = −60.

The constant +60 produces the constant carry −15. Both are bounded solutions. Neither visits 0.

So if a bounded solution visits 0, it is not one of these two constants, the equality |e_t| = 15 is impossible at every site, and |e_t| < 15. An integer strictly inside (−15, 15) satisfies |e| ≤ 14. This is the same integer step as Lean `carry_strict` in `formalization/Bgs/LineN20Arith.lean`: |e| < 15 implies |e| ≤ 14. The closed 633-state set of N20 sits inside that range and contains the state (−14, −14).

## Geometric tail

The tail of the kernel is geometric with ratio μ:

Σ_{|k| > L} |g_k| = 2 |α| μ^{L+1} / (1−μ).

A change in the letters outside lag L, of size at most 60, moves any carry by at most 60 times this tail. The ball arithmetic gives:

| L | 60 × tail, upper bound |
|---|---|
| 1 | < 0.754 |
| 9 | < 10^{-6} |
| 14 | far below 10^{-6}; the log is in `green_tail.json` |
| 30 | the same, smaller by another factor μ^{16} |

Thus a window of nine lags already determines the integer carry up to an error that cannot cross an integer. Past |e| = 14 there is nothing left to determine: the tail of the state space is the empty set, not a small positive operator.

## What this does to the prefactor

Let T be the single-window carry operator on bounded trajectories, and let T^{(E)} be the same operator with every state of carry larger than E deleted. For every E ≥ 14,

T^{(E)} = T

on the states reachable from (0,0). The constant solutions ±15 are invariant and do not meet (0,0), so they do not contribute to the orbit of a matrix supported at (0,0).

Consequently the orbit prefactor at rate 0.28, if it is finite for the sharp box, is exactly the full-carry prefactor. It does not grow as E → ∞ past 14. There is no geometric series of omitted boxes to sum. The ratio μ bounds the scalar reconstruction of e, not a remainder of the phased operator.

The same conclusion fails for the joint ε-system. There the cutoff is 51, and this note does not iterate that graph.

## What is not claimed

The identity T^{(14)} = T does not bound the spectral radius. A finite matrix can have a large radius. The radius of the phased operator is a separate computation, in `11_ball_orbit.md`. The (0,0) share produced by that computation is still the proxy N15 refused to identify with the shell constant C. Multiplying a shell constant by 1/share is not a step in this argument. H1 stays open.
