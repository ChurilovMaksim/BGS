# P_w kill-test: m=9 (exhaustive) and m=12 component-derived bad fibers

Not a proof, not a Lean theorem. Exact integer arithmetic only.
Conventions as in wave 6 task 2 / sep_m8_test.py: `Fix_m = ker(H_m mod D_m)`,
`H = 6I - C - C^T`, fiber = `sorted(y)` class, Gamma = dihedral perms
`p[j] = (j+k) % m` or `(k-j) % m` acting by `(p.y)_j = y_{p[j]}`,
`w = (H y)/D` (integer, entries in -1..5), `P_w`: equal sorted(y) and
equal sorted(w) imply same Gamma-orbit.

## (a) m=9: P_w survives VACUOUSLY — there are no Gamma-bad fibers at all

Exhaustive over all `Fix_9`, `D = 7761796 = 4 * 49 * 39601`, 7,761,796 points
(CRT from component kernels of sizes 4, 49, 39601; every generated point
asserted to satisfy `H y = 0 mod D`):

- fibers: 434,020; Gamma-orbits: 434,020; Gamma-bad fibers: 0
- P_w failures: 0; orbits with more than one distinct sorted(w): 0
  (sorted(w) is constant on Gamma-orbits, as theory requires)
- fiber-size distribution: 1:4, 3:24, 6:20, 9:5544, 18:428428
  (sums to 7,761,796 points, cross-checked)

Independent cross-check with a different code path (Python `fix_mod` from
`gluing_components.py` + numpy CRT + lex-min Gamma canon + `np.unique`):
fibers = 434,020, Gamma-orbits = 434,020, bad fibers = 0 — identical.

Consequence: m=9 adds NO evidence for P_w as a separator, because there
was nothing to separate. The non-vacuous evidence stays at m=8 (perfect
separation over 39 bad fibers) and the m=12 component lifts below.
A first C++ draft of this test had two unsigned-`%` bugs (negative
recurrence values wrapping); both were found because the component
counts came out 31/37 instead of 49, fixed to signed arithmetic, and
the final counts were then confirmed by the independent Python run.

## (b) m=12 component-derived bad fibers: P_w survives (0 kills)

Component Gamma-bad fibers (exact, per prime power):

| q | n_fix | fibers | Gamma-bad |
|---|---|---|---|
| 128 | 128 | 39 | 0 |
| 81 | 81 | 7 | 1 |
| 25 | 25 | 5 | 0 |
| 49 | 49 | 12 | 0 |
| 121 | 121 | 11 | 0 |

The single bad fiber, mod 81, sorted class
`(9, 9, 18, 18, 36, 36, 45, 45, 63, 63, 72, 72)`, 36 vectors, 3 Gamma-orbits
of 12 (the same fiber as the wave-4 O* kill). All 3 orbit-pairs were
lifted to global vectors (other components 0, CRT embedding phi, as in
`gluing_m12_counterexample.py`); each lift was asserted to satisfy
`H y = 0 mod D`, equal sorted multisets, and distinct global Gamma
canons. Their global sorted(w) are all different:

- orbit 1: `[0, 0, 0, 0, 1, 1, 3, 3, 4, 4, 4, 4]`
- orbit 2: `[0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4]`
- orbit 3: `[-1, -1, 0, 0, 2, 2, 2, 2, 4, 4, 5, 5]`

so 3 lift tests, 0 P_w kills. Since sorted(w) is constant on a
Gamma-orbit, one example per orbit decides this fiber completely.

Scope caveat: (b) is NOT an exhaustive global m=12 test (1,536,796,800
points, infeasible here). Global Gamma-bad fibers arising by gluing
across components, rather than from a component bad fiber, were not
tested, so global P_w at m=12 remains open. The m=12 pair from wave 6
is the orbit-1 vs orbit-2 lift above.
