# Wave 15, task 3 — first real D1a test: NOT FOUND up to m = 10

**Verdict: no split fiber is partially in support for any m ≤ 10.**
Stronger: apart from m = 8, there are no split fibers at all up to
m = 10, and at m = 8 all 39 split fibers are off-support. So D1a's
phase question (coherent sums across Γ-orbits inside one fiber, with
some orbits in support and others out) is vacuous at every m ≤ 10,
exactly as at m = 8. Support is a union of whole fibers everywhere
checked. No coherent-sum computation was needed: there is no fiber
to compute it on. Repository untouched, no Lean built.

## Scan (full Fix_m enumeration, exact integer arithmetic)

Fiber = same sorted multiset; Γ-orbit = dihedral action on positions;
split = fiber with > 1 orbit; partial = 0 < #(fiber ∩ supp) < |fiber|.
Support by the s = 1 torsion criterion: y ∈ supp iff
(2·Qnum(z) − z·y) ≡ 0 (mod D) for every torsion representative
z = (Hv)/4, v ∈ ker(H mod 4). Fix_m enumerated via the SNF kernel of
M^m − I (avoids the q² seed problem for large prime-power factors).

| m | D_m | fibers | Γ-orbits | split | supp size | partial |
|---|-----|--------|----------|-------|-----------|---------|
| 1 | 4 | 4 | 4 | 0 | 1 | 0 |
| 2 | 32 | 18 | 18 | 0 | 4 | 0 |
| 3 | 196 | 48 | 48 | 0 | 49 | 0 |
| 4 | 1152 | 203 | 203 | 0 | 72 | 0 |
| 5 | 6724 | 756 | 756 | 0 | 1681 | 0 |
| 6 | 39200 | 3604 | 3604 | 0 | 4900 | 0 |
| 7 | 228484 | 16800 | 16800 | 0 | 57121 | 0 |
| 8 | 1331712 | 85106 | 85145 | 39 | 83232 | 0 |
| 9 | 7761796 | 434020 | 434020 | 0 | 1940449 | 0 |
| 10 | 45239072 | 2272998 | 2272998 | 0 | 5654884 | 0 |

## Validation

- At every m, |supp| = D/|V4| exactly (Parseval + modulus dichotomy).
- Direct φ̂ spot-checks (definition sum over Fix) at m ≤ 6: support
  membership and |φ̂|² = |V4|/D agree on all sampled points.
- m = 8 reproduces wave 14 exactly (85106/85145/39/83232);
  m = 9 reproduces wave 7 (434020 fibers = 434020 orbits).
- m = 10 grouped fibers/orbits by 128-bit row hashes (collision
  probability ~10⁻²¹); a 20000-point sample validates hash grouping
  by direct row comparison, and global fiber ids agree on the sample.

## Engineering notes (m = 10, 45.2M points)

- First attempt died silently in `np.unique` orbit grouping (the
  pipeline exit code masked it); retry used lexsort grouping and
  chunked row hashing, peak memory ~3 GB.
- /tmp is a 512 MB tmpfs: a checkpoint write there failed with
  "No space left"; checkpoint moved to the workspace, then deleted.
  Final numbers are in `wave15_scan_10.json`.

## Limit and pattern

- m = 11 full enumeration is infeasible (D ≈ 2.6×10⁸ points, > 10 GB
  for the point array alone). m = 12's known glued split fiber is
  off-support (wave 10), so it is not a partial test either.
- Pattern so far: split fibers appear only at m divisible by 4 with
  m ≥ 8 (m = 8: 39, all off-support; m = 12: glued, off-support),
  and no fiber at m ≤ 10 is partial. The first real D1a phase test
  needs either a split fiber meeting support at m ≥ 11 (targeted
  component-lift search, not full enumeration) or a proof that
  split fibers never meet support.

## Files

- Scan: [wave15_d1a_partial_scan.py](wave15_d1a_partial_scan.py) (m ≤ 9)
- m = 10 scan: [wave15_d1a_partial_m10b.py](wave15_d1a_partial_m10b.py), `wave15_scan_10.json` (not in repository)
- First m = 10 attempt (OOM in grouping, superseded): [wave15_d1a_partial_m10.py](wave15_d1a_partial_m10.py)
