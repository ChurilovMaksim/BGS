# M4 SCOPE — the Sp(2g) theta-quantization project

Written 2026-09-02 after the RUN 102-103 scoping passes.

## What M4 needs (and why it is a project, not a task)

The G0 hypothesis asserts the H-coupling closure for any kernel whose
difference fibers are rational-function orbits of bounded degree.  The
cat map realizes D = 4 (the twisted Jacobi kernel).  The genuine
higher-rank test — the Sp(2g) theta-quantized cat map — has:

1. **A theta kernel that entangles the factors.**  The RUN 102.3
   negative result shows the naive product-character kernel is trivially
   reducible; the genuine coupling comes from the shared q-deformation
   (the theta structure).  The fiber sums become higher-genus
   character sums (rank-2 Kloosterman-type twisted by subgroups).

2. **The rank-1 fibers are trivially bounded.**  The twisted
   Kloosterman fibers u + c/u = d are quadratic equations (≤ 2
   solutions per fiber) — no Weil content.  The genuine content is at
   rank 2: fibers of (u₁, u₂) with u₁u₂ = const and twisted second
   coordinates — curve genus ~ 5, bound ~ 8√N.

3. **Implementation surface**: Sp₄(Z/N) generators, the Weil
   representation on (Z/N)⁴, the Hecke ring of Sp₄, and the theta
   kernel — none of this exists in the workspace (theorem_e has 3
   functions).  Estimate: 1500–3000 lines + validation.

## Sub-milestones

M4a — Sp₄ Weil representation at small N (generators + exact Egorov
certificate, mirroring catmap_independent.py).
M4b — the Hecke operator for a diagonal Sp₄ element; the character-sum
kernel extraction.
M4c — the coupled-energy computation at g=2 (the G0 test).
M4d — the higher-genus Weil range (the RH application to the fiber
curves).

## Reference points

- Kelmer: quantized cat maps on the torus × torus (the closest
  published sibling).
- Gurevich–Hadani: the Sp(2g) Weil representation and Ramanujan
  property (the MAximal monodromy statement that G0's Weil part
  becomes at higher rank).
- Furstenberg-style × the arithmetic progression structure.

## Honest timeline

M4a–b: 2–3 sessions.  M4c: 1–2 sessions after M4b.  M4d: the analytic
core — 1 paper.  The full M4 closes G0 and with it the prize-track
statement (a general arithmetic-chaos mechanism, not just a family).
