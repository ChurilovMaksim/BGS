# Wave 32, task 5 — COH at m=60: FAILS (exact counterexample)

## Verdict

COH is FALSE in general: at m=60 there is an exact pair (A, A')
sharing the joint global multiset via σ(i) = 11i+9 (a multiplier
map, not dihedral) for which NO single dihedral τ works across all
components, up to the validated shadows. The R**+COH route to JBL
is therefore dead in general. JBL itself remains open (another
route would be needed). COH held at m=12 and m=36; m=60 is the
first failure. Repository untouched; no Lean built.

## Setup

D_60 = 8·P_60² = 2^7·3^4·5^4·7^2·11^2·19^2·29^2·31^4·41^2·59^2·
269^2·601^2·2281^2, so 13 components:
{128, 81, 625, 49, 121, 361, 841, 923521, 1681, 3481, 72361, 361201,
5202961}. Genuine sets verified exactly: G_128 = {(16a,8b)} by
brute-force kernel equality, and for odd q = p^{2e},
α^60 − 1 = p^e·(unit·√2) mod q forces ker = p^e·(R/p^e R).
Trace window Z/60, α = 3+2√2, S(A) = (Tr(Aα^i)).

## Step A: classes vs dihedral images (exact, C++)

Classes equal dihedral images at every component EXCEPT two:
- q=81: 24 non-dihedral sequences (big class 36, classes
  36,12,12,12,4,4,1).
- q=625: 240 non-dihedral sequences (classes 150,150,30×15;
  size 150 > 120 proves collapse alone). Sequences here are
  30-periodic (α^30 ≡ 1 mod 25 on genuine A).
All other components clean (nondih=0), including the huge ones
(923521: 31265 classes; 5202961: 44499 classes, top size 120).
Pattern/PQ counts (for the DFS): 128: 3/5, 49: 13/55, 121: 121/1441,
361: 361/7201, 841: 671/11901, 1681: 151/1351, 3481: 3461/115601,
72361: 72331/4099501, 361201: 361201/41184001,
923521: 921121/27436051, 5202961: 5202961/616147201.

## Shadows pinned by coverage (Python, exact)

Ann(128) = 16 elements, Ann(odd) = {0} at m=60.
- (128,81): 200 signature groups; orbit+Ann alone escapes 32;
  +{27D : D ∈ R/3R} escapes 0/200.
- (128,625): 232 signature groups; orbit+Ann alone escapes 16;
  +{125D : D ∈ R/5R} escapes 0/232.
Mechanism (wave-25 §3 logic): the odd data sees exactly one
p-adic digit (A₁ mod p, A = p^e·A₁), so the invisible shifts are
p·(R/pR) in A₁, i.e. {27D : R/3R} at 81 and {125D : R/5R} at 625.
Shift sequences: 9 at 81, 25 at 625.

## DFS (C++, collapsed options, shadow-aware)

Raw PQ counts up to 616M collapse by (mask, allow) identity to
≤3721 per component (e.g. 5202961: 616147201 → 3721; 361201:
41184001 → 3721; 923521 → 256). Collapse keys: 81: 305,
625: 2737. The DFS found a failure in 3092 nodes with matching
σ(i) = 11i+9 mod 60 (from the printed matching, inverted).

## Value-level confirmation (independent Python + C++ paths)

For σ(i) = 11i+9, per-component σ-compatible genuine pairs
(S' = σ(S)) exist everywhere: all of G at 128, 81, 49, 121, 841,
1681; only S = 0 at 361, 923521, 3481, 72361, 361201, 5202961;
25 pairs at 625. Their τ-masks (validated shadows) intersect to
∅. The explicit pair (A → A' per component, rest (0,0)):

| q | A | A' |
|---|---|---|
| 128 | (0,8) | (32,8) |
| 81 | (9,18) | (72,63) |
| 625 | (0,0) | (0,0) |
| 49 | (0,7) | (0,42) |
| 121 | (11,77) | (110,44) |
| 841 | (29,435) | (29,406) |
| 1681 | (41,861) | (41,820) |

Independent Python check recomputes every mask from these pairs
(all match), the intersection is 0:0, and the direct check over
all 120 τ finds none passing. The pair shares the joint multiset
via σ (S'_q = σ(S_q) at every component, CRT gives global
A, A'), and no τ works: 128, 81, 49 alone already force ∅.

## Why the superset shadows do not save it

With superset shifts (multiples of 9 at 81, multiples of 25 at
625) the σ-masks stop intersecting to ∅. But those shifts are
NOT shadow: they change the visible digit A₁ mod p, which the
signature determines (at 81 via the class triples (2a, 2a+3b,
2a+6b) mod 9; at 625 via the injective trace triple mod 5).
The true shadow is the kernel of the visible map, i.e. exactly
the validated sets. The superset check was over-permissive.

## Files

- This note: `methods/wave32_COH_m60.md`
- `methods/wave32_COH_m60_stepA.cpp` (+ `wave32_stepA.log`,
  `wave32_COH_m60_patterns_q*.bin`)
- `methods/wave32_COH_m60_shadow.py` (+ `wave32_shadow81.log`,
  `wave32_shadow625.log`)
- `methods/wave32_COH_m60_dfs.cpp` (+ `wave32_dfs.log`)
- `methods/wave32_COH_m60_sigma_analysis.cpp` (+
  `wave32_sigma_analysis2.log`,
  `wave32_COH_m60_sigma_examples_q*.txt`)
- `methods/wave32_COH_m60_verify.py` (independent confirmation)
- `methods/wave32_shift81.bin` (9 seqs), `wave32_shift625.bin`
  (25 seqs)
- Discarded: `methods/wave32_COH_m60_shadow_direct.cpp` — it
  tested single-component exact signature preservation, which
  is NOT the R** shadow property; the coverage test is.
