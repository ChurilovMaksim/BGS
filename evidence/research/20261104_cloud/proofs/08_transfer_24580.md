# The 24 580-vertex carry transfer: spectral radius and prefactor

Status of the radius bounds: **[CA]** for the matrices that were actually built. Status of the letter weights fed to those matrices: **[N]**, taken from the N14 float table. H1-bad at C ≤ 8.8×10^{-4} is not closed. The norm majorant on this graph is obstructed at rate 0.28.

## What was built

The carry states are the 6145 pairs (e_{k−1}, e_k) that lie on a closed path through (0, 0) in the box |e| ≤ 51, with a step (a, b) → (b, c) if and only if |a − 2b − c| ≤ 60. An independent breadth-first search reproduces the N20 count: 8377 forward, 8377 backward, 6145 closed.

A vertex of the transfer is a pair together with a trailing-zero count z ∈ {0, 1, 2, 3}. That is 6145 × 4 = 24 580 vertices. The step carries the Fourier letter

u = a − 2b − c.

If u = 0 and z = 3, the step is deleted: it would be a fourth consecutive zero letter. Otherwise the new count is z+1 when u = 0, and 0 when u ≠ 0. The bad restriction removes 2547 continuations and leaves 496 265 weighted edges. The same graph with the restriction turned off has 498 812 edges and the same leading radius, recorded below.

This zero test is the Fourier letter u, not the twist digit E_k of the alphabet theorem. The two sequences are not the same. The state space is the one named in the previous note.

## The matrix

The sesquilinear operator would put a 495×495 block on each edge. One complex block is about 3.7 MB, and 24 580 of them are about 92 GB. That operator was not stored and not iterated. N15’s phased iteration, which did keep the blocks, was run only up to carry box E ≤ 4 (81 states, one window, no trailing-zero coordinate).

What was built instead is the norm majorant on the same vertices. The edge u is given a nonnegative scalar W(u):

- W(0) = 0.28,
- W(u) = κ_{|u|} for 1 ≤ |u| ≤ 24, the letterwise CP weights in `computations/verification/lineN14/logs/b_cp2_0.28.json`,
- W(u) = 0 for |u| > 24.

Dropping |u| > 24 deletes edges. For a nonnegative matrix that can only lower the spectral radius, so a lower bound obtained after the deletion remains a lower bound for the matrix that restores those edges at any nonnegative weight.

The weights are float64 values of that table. They are not interval enclosures of ||T_u||. The radius statements below are exact for this float matrix, not for an interval around the table.

## Collatz–Wielandt

Let M be nonnegative and let v ≥ 0 be nonzero. If (Mv)_i ≥ λ v_i whenever v_i > 0, then Mv ≥ λ v and ρ(M) ≥ λ. The vector v is the L1 power iterate, cut off below 10^{-12} of its maximum; discarded mass only decreases the computed (Mv)_i, so the inequality remains a lower bound. The quotients are summed in flint balls at precision 128.

The lower bounds are Collatz–Wielandt on the power vector cut off at 10^{-12} of its maximum. The one upper bound uses a strictly positive vector, the power vector plus 10^{-12}, so the maximum quotient is a genuine upper bound.

| Model | Bad-run ban | Bound | Tag |
|---|---|---|---|
| κ table | yes | ρ ≥ 571.903581000 | [CA] |
| κ table | no | ρ ≥ 571.903581000 | [CA] |
| κ table / 2 | yes | ρ ≥ 286.009781243 | [CA] |
| κ table / 10 | yes | ρ ≥ 57.294741413 | [CA] |
| every u ≠ 0 weighted 0.0034 | yes | ρ ≥ 0.280004577 | [CA] |
| every u ≠ 0 weighted 0.0035 | yes | ρ ≥ 0.285191292 | [CA] |
| every u ≠ 0 weighted 0.003 | yes | ρ ≤ 0.25911138182 | [CA] |

## Prefactor at rate 0.28

Write C_*(0.28) for the infimum of C such that ||M^n|| ≤ C · (0.28)^n for every n ≥ 0. If ρ(M) > 0.28, no such finite C exists.

For the κ-table majorant, ρ ≥ 571.90 > 0.28, and the same is true after dividing every off-diagonal weight by 10 (ρ ≥ 57.29). Therefore

C_*(0.28) = ∞

for this model. It does not certify C ≤ 8.8×10^{-4}. It certifies the opposite: the norm majorant on the 24 580 vertices does not have rate 0.28 at any finite prefactor.

The largest uniform off-diagonal weight that might still have rate ≤ 0.28 lies in (0.003, 0.0034). At 0.003 the radius is < 0.28. At 0.0034 it is > 0.28. A float bisection places the crossing at 0.00339991, inside that certified bracket. The N14 table is far above this gate: κ_1 = 0.90, and the entries from |u| = 2 through |u| = 21 all exceed 1.

## What does not obstruct

On the subgraph that keeps only u ∈ {−1, 0, +1}, with the zero-run ban, Kahn’s algorithm eliminates all 24 580 vertices (28 009 edges). The subgraph is a directed acyclic graph, so its spectral radius is 0 for every positive edge weight. The single weight κ_1 = 0.90 does not, by itself, force rate above 0.28. The excess radius of the full table is carried by the heavier letters, which do close cycles.

## What this does not decide

N15 kept the blocks T_u for carry boxes E ≤ 4 and saw growth 0.27255, equal to ρ(𝒦), while the norm majorant on those letters is large. Phase cancellation inside the blocks can destroy the 571 growth. The present radius is an upper-model radius. It obstructs any proof of H1-bad that passes through this norm majorant. It does not obstruct a genuinely sesquilinear iteration on the same 24 580 vertices, and that iteration was not run.

H1-bad at C ≤ 8.8×10^{-4} stays open. The best prefactor of the operator that was actually built, at rate 0.28, is infinite.
