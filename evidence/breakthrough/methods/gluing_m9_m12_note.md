# O* gluing search at m=9 and m=12 — working note (not a proof, not for main)

Conventions (as in the wave-3 O* test): `Fix_m = ker(H_m mod D_m)`,
`H_m = 6I - C - C^T`, i.e. `y_{i+1} = 6 y_i - y_{i-1}` with period `m`;
a fiber is a `sorted(y)` class; the affine group is `p(j) = a*j + b mod m`,
`a in (Z/m)^x`, acting by `(p.y)_j = y_{p(j)}`; separation reading (R) is:
every fiber is contained in a single affine orbit (equivalently, two vectors
in one fiber have the same affine canonical form, the lexicographic minimum
over Aff). Strict reading (fiber = full affine orbit) is already false at
m=8 and is not the claim tested here. Enumeration is exact integer
arithmetic; it is a verifier artefact, not a Lean theorem.
Caveat on grounding: this note reuses the H_m / Fix / affine conventions of
the wave-3 O* test (verified against main `6dbcc7a`); it does not itself
re-fetch main, and a HEAD move reported by another wave-4 branch
(`d87dce0`, PR #76) was not checked here.

## m=12: O* (separation) is KILLED — no gluing needed

Per-component separation already fails at m=12, mod 81:

- `Fix_12 mod 81`: 81 vectors, 7 fibers, exactly 1 aff-bad fiber.
- Bad sorted class mod 81: `(9, 9, 18, 18, 36, 36, 45, 45, 63, 63, 72, 72)`,
  36 vectors, split into 3 affine canons of 12 vectors each.
  (All values are multiples of 9: this is a lift of a mod-9 kernel vector,
  the same torsion-lift mechanism as the m=8 bad fibers.)

Lift to a global counterexample by putting every other prime-power
component to 0 (0 is in every kernel) and embedding `Z/81` into `Z/D`
by CRT, `phi(t) = t*M*inv(M mod 81) mod D`, `D = 1536796800`, `M = D/81`.
Since `phi` is injective, equal sorted multisets mod 81 give equal sorted
multisets globally; a global affine perm would reduce mod 81 to an affine
perm of the mod-81 vectors, contradicting distinct canons. Explicit pair,
verified by `gluing_m12_counterexample.py` (`H y = 0 mod D`, `H y' = 0 mod D`,
`sorted(y) = sorted(y')`, global affine canons distinct):

- `y  = (1366041600, 1366041600, 683020800, 1195286400, 341510400, 853776000, 170755200, 170755200, 853776000, 341510400, 1195286400, 683020800)`
- `y' = (1366041600, 1195286400, 1195286400, 1366041600, 853776000, 683020800, 170755200, 341510400, 341510400, 170755200, 683020800, 853776000)`
- mod 81 reductions: `y mod 81 = (9, 9, 45, 18, 63, 36, 72, 72, 36, 63, 18, 45)`,
  `y' mod 81 = (9, 18, 18, 9, 36, 45, 72, 63, 63, 72, 45, 36)`, different
  affine canons (see script output).

Consequence: O* in the separation sense is false at m=12, hence false in
general. The m=12 gluing question is moot: O* does not survive to m=12 at
all. (O' — restriction to the support of φ̂ — is a separate, weaker claim
and is untouched by this counterexample, which has no reason to lie in
that support.)

## m=9: per-component separation HOLDS; genuine non-dihedral gluing impossible

`D_9 = 7761796 = 4 * 49 * 39601` (prime powers `2^2, 7^2, 199^2`).
Fix mod q was enumerated by solving `(A^m - I) v = 0 mod q`,
`A = [[0,1],[-1,6]]`, iterating `a` and solving the linear congruence for
`b` (no `q^2` scan); `|Fix mod q| = q` in every case.

| component q | |Fix| | fibers | aff-bad fibers |
|---|---|---|---|
| 4 | 4 | 4 | 0 (all vectors constant) |
| 49 | 49 | 12 | 0 (all vectors period 3) |
| 39601 | 39601 | 2300 | 0 |

Multiplier/effect analysis (exact, over all component vectors):

- mod 49: every affine perm landing in Fix has the same *effect* as some
  dihedral perm (a = ±1). All 49 vectors are period 3, so `a mod 3 = ±1`
  already collapses every affine action to a dihedral action on the
  3-pattern. Multiplier sets are all of `(Z/9)^x`, effects are dihedral.
- mod 39601: for 39600 vectors the only multipliers occurring are `a = ±1`;
  the remaining vector is 0, where every perm acts trivially. No vector
  has a non-dihedral affine perm landing in Fix with a new effect.
- mod 4: constants, every perm acts trivially.

Hence any global pair with equal multisets at m=9 must, per component, be
related by a *dihedral* perm in effect. (The mod-4 component is constant
and drops out of both the multiset and the canon comparisons: it tags
every position with the same value, so the search over
`(v49, v39601)` pairs is the full search.) The only possible gluing failure
left is "dihedral gluing": per-component dihedral perms `d49, d39601`
differing, whose mixed CRT pair has the same multiset as the original but
is not one global dihedral perm.

## m=9: dihedral gluing does not occur

Split on the large component `v39601`:

1. **Distinct values (37818 vectors, all 9 values distinct).** Argument:
   let the candidate be `(d49.v49, d39601.v39601)`. Multiset equality gives
   a position permutation `sigma` with
   `(v49_{d49(j)}, v39601_{d39601(j)}) = (v49_{sigma(j)}, v39601_{sigma(j)})`
   for all `j`. Distinctness of `v39601` forces `sigma(j) = d39601(j)`;
   then `v49_{d49(j)} = v49_{d39601(j)}` for all `j`, so the candidate is
   exactly `d39601` applied globally to the original pair. It is globally
   affine, not a counterexample. This covers 37818/39601 large-component
   vectors for every choice of the other components.
2. **Repeated values (1782 vectors with exactly 5 distinct values, plus
   the zero vector).** These are exactly the vectors with `|A| = 9`
   (dihedral stabiliser of order 2; the zero vector has `|A| = 1`).
   Exhaustive pair search over all of them against all 49 mod-49 vectors:
   `asize9`: 87318 pairs, 3768930 A-combinations, 0 hits;
   `period3` (zero vector): 49 pairs, 235 combinations, 0 hits.
   A candidate here would have to be an A-combination, and none passes
   both the multiset test and the global-canon test.

Targeted random search as a cross-check (generic vectors):
`random` (seed 0): 20000 pairs, 1683333 A-combinations, 0 hits.

Total m=9 gluing search: 107367 pairs, 5452498 A-combinations, 0 hits,
plus the distinct-values argument covering the 37818 generic
large-component vectors outright.

## Verdict

- **m=12: O* (separation) is false**, explicit counterexample above
  (lift of the mod-81 aff-bad fiber). No gluing construction is needed,
  and no O* claim at general m can be maintained.
- **m=9: no gluing counterexample exists.** Genuine non-dihedral gluing is
  impossible by the component multiplier/effect enumeration; dihedral
  gluing is excluded by the distinct-values argument for generic vectors
  and by exhaustive pair search for the 1782 + 1 repeated-value vectors.
  This is an exact finite check plus a short mathematical argument, not a
  Lean proof and not a proof for general m.
- **What this means for 152:** at m=8, separation survives with Aff (and
  O' is redundant there); at m=9 it still survives (this note); at m=12
  it fails even with Aff. Any use of O* in 152 must therefore be
  m-restricted (m ≤ 9 on current evidence, and m=10, 11 unchecked) or
  replaced by a different separation principle; it cannot be asserted
  for general m. The next informative cases are m=10 and m=11 (and, for
  the 152 application, whether the m=12 counterexample meets the support
  of φ̂_12, i.e. the O'-style restriction at m=12).

## Files

- `gluing_components.py` — Fix mod q enumeration + per-component
  affine-separation test; output `gluing_components_result.json`.
- `gluing_m12_counterexample.py` — explicit m=12 counterexample, verified.
- `gluing_m9_search.py` — m=9 gluing search (random / asize9 / period3);
  outputs `gluing_m9_random.json`, `gluing_m9_asize9.json`,
  `gluing_m9_period3.json`.
