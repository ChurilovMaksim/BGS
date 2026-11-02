# Wave 21, task 1 — P_w replacement separator: FOUND at m=12

## Verdict

**Sorted unordered cyclic adjacent pairs separate every split fiber
on support at m=12 — including all 152 P_w-failing fibers.**
For a point `y` of length 12, let

    Adj(y) = sorted multiset of {y_i, y_{i+1}} over i ∈ ℤ/12
    (unordered pairs, cyclic).

`Adj` is Γ-invariant (shifts preserve cyclic adjacency; reversal maps
each edge to an edge), and on the wave-18 census data it takes
distinct values on distinct Γ-orbits of every split fiber meeting
support. This is a genuine P_w replacement at m=12: where `sorted(w)`
collides, `Adj` does not.

## Test setup (exact integers, no floating point)

- Data: `wave18_Pw_m12_census.json` — all 762 split fibers meeting
  support at m=12, with one representative per Γ-orbit. The 152
  P_w-failing fibers contribute exactly 152 failing groups, each
  with exactly 2 orbits sharing `sorted(w)`.
- Candidates were computed from the representatives (`w = Hy/D`,
  exact division; `sorted(y)` and `sorted(w)` re-verified against
  the census) and checked for distinctness across the orbits of
  each failing group. Scripts: `wave21_separator_hunt.py`,
  `wave21_separator_extend.py`.

## Results on the 152 P_w-failing groups (separated / 152)

| candidate | result |
|---|---|
| `sorted_w`, `p2_w`, `p3_w` (controls) | 0 |
| `pair_sorted` (torsion dots, sorted) | 0 |
| `pair_qnum` (joint `(Qnum(z), z·y)`) | 0 |
| `Y_canon` (class sums up to D_4) | 0 |
| `wclass_canon` (per-class w-multisets up to D_4) | 1 |
| `pair_by_type` (pair dots per torsion type) | 2 |
| `joint_yw` (sorted `(y_i, w_i)` pairs) | 71 |
| `adj_w` (adjacent w-pairs) | 147 |
| **`adj_y` (adjacent y-pairs)** | **152** |
| `neigh_y`, `neigh_w` (neighbour-symmetric triples) | 152 |

## Extension: all 762 split fibers on support

`adj_y`, `neigh_y`, and `neigh_w` each separate **762/762** split
fibers on support — not just the P_w-failing ones. So at m=12,
`Adj` is a complete separator of Γ-orbits within fibers on support.
Γ-invariance was also checked empirically: 101 representatives ×
24 dihedral perms, 0 violations (as the edge argument predicts).

## Why the other classes die

- Symmetric functions / moments of `w` are functions of `sorted(w)`
  by definition, so they cannot separate anything `sorted(w)` does
  not — 0/152 is a theorem, not a numerical accident.
- `pair_sorted` and `pair_qnum` at 0/152 are consistent with
  pair-sum fiber-constancy (wave 7, modulo Lemma Y): pair data is
  a fiber function, so it cannot separate inside a fiber.
- `Y_canon` at 0/152 is consistent with the Lemma Y sketch
  (class sums are D_4-related within a fiber).
- `joint_yw` at only 71/152 is the interesting negative: the
  (value, w-value) pairing survives gluing on 81 failing fibers,
  but cyclic adjacency never does. Gluing permutations preserve
  the fiber multiset and often the `(y, w)` pairing, but they break
  which values sit next to each other — and `Adj` records exactly
  that.

## Honest scope limits

- This is **m=12, on support only**. No claim is made for general
  m, for off-support fibers, or for m=8 split fibers (untested
  here; they are off-support).
- `Adj` separates orbits within a fiber; whether mode sums (or
  φ̂-data) determine `Adj` is a separate, open question — the
  separator exists, the route from mode sums to it is not shown.
- The 610 split fibers that P_w already separated were not
  re-examined for finer structure; `Adj` separates them too.

## Next steps suggested

1. Test `Adj` on m=8 split fibers (off-support) and on m=16
   component splits — if it holds there, it is a candidate general
   separator, not just an m=12 accident.
2. Ask whether mode sums determine `Adj` (or a coarsening of it):
   without that link, `Adj` does not by itself repair 152's
   separation step.
