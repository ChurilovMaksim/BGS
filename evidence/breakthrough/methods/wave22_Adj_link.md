# Wave 22, task 4 — Adj(y) beyond m=12, and the mode-sum link for 152

## Verdicts

1. **m=8: Adj separates 39/39 split fibers — all off-support.**
   Full census (D_8 = 1331712 = 512·9·289): 85,106 fibers, 85,145
   orbits, exactly the wave-14 numbers; 39 split fibers (2 orbits
   each, sizes 16 or 32), all EMPTY under the s=1 support criterion,
   Adj distinct on the two orbits in every one. On support, Adj
   separation is vacuous at m=8: no split fiber meets support.
2. **m=16: Adj separates 10/10 lifted component splits — all
   off-support; no on-support split fiber is known, so on-support
   Adj separation at m=16 is untested.**
   D_16 = 1773462177792 = 2048·9·289·332929. Component splits exist
   only at q=2048 (10 fibers); all other components are unsplit and
   fully supported, and component support is fiber-constant at every
   component (verified). Lifting the 10 q=2048 splits with supported
   points elsewhere gives 10 global split fibers (2 or 4 orbits),
   all EMPTY, Adj separating all 10. A wave-18-style normalized
   census would need ~1.7e11 representatives and is infeasible.
   Gluing-split search instead: 20,000 sampled supported points ×
   6 component pairs × 32×32 relative dihedral shifts =
   122,880,000 checks, **0 gluing splits found**. At m=12-like
   split mass (3.7e-4 of supported points) ~7.5 hits would be
   expected, so this bounds the pair-shift-detectable on-support
   split mass at m=16 below ~1.5e-4 (95% Poisson bound 3/20000) —
   conditional on pair shifts capturing the gluing mechanism.
3. **Mode sums do NOT determine Adj — refuted by an explicit pair,
   and by principle.** The separation step hSep sees only the mode
   sums S_k(ξ) = Σ_j e(kξ_j), which are symmetric in the
   coordinates, hence constant on fibers. Adj varies inside fibers
   (wave 21: 762/762 at m=12), so no function of mode sums can equal
   Adj. Explicit pair (wave-18 exhibit, fiber combo [1,6,0,1,0],
   both reps confirmed in the census, pw_ok=False):
   - y1 = [1024531200, 475675200, 292723200, 1280664000, 1244073600,
     36590400, 512265600, 1500206400, 804988800, 256132800, 731808000,
     1061121600]
   - y2 = [1244073600, 256132800, 292723200, 1500206400, 1024531200,
     36590400, 731808000, 1280664000, 804988800, 475675200, 512265600,
     1061121600]
   Same sorted multiset (same fiber ⇒ same S_k for every k; power
   sums k=1,2,3 checked equal), same sorted(w) = (−1,0,0,1,1,2,2,3,
   3,4,4,5), 0 dihedral perms map y1 to y2 (distinct Γ-orbits), but
   Adj(y1) ≠ Adj(y2) (differ at 10 of 12 positions; e.g. y1 has
   edge (36590400,512265600), y2 has (36590400,731808000) instead).

## Consequence for 152

Adj cannot repair hSep in its original form: the step's input
(mode sums) is strictly coarser than Adj, so no conclusion drawn
from mode sums alone can recover Adj. Any future 152 use of Adj
must change what the separation step sees — it cannot be a
same-input repair. (The corrected route (B2′), R = Bsym_fiber − Δ,
does not use separation at all; Adj's remaining value for 152 is
as a per-m certificate tool for orbit structure, not as a
mode-sum-derived separator.) Note Adj is also not needed for Δ:
Δ needs orbit phases, not adjacency data.

## Methods (exact integers throughout)

- m=8: full CRT enumeration of Fix_8 (1,331,712 points), sorted
  fibers, dihedral canons (16 perms), global s=1 support test.
- m=16: SNF component kernels (snf_kernel), CRT lifts of the 10
  q=2048 splits, sampled supported points (2048-component drawn
  from its 128 supported points), pair-component relative shifts
  y' = y + K1(γ(c1)−c1) + K2(δ(c2)−c2) mod D, multiset + canon
  comparison. Int64-safe: K·c ≤ ~5.9e17.
- Adj uses canon rows as orbit representatives (Adj is
  Γ-invariant: shifts preserve cyclic edges, reflections reverse
  them), so no global-point storage was needed at m=8.

## Scope limits (honest)

- m=16 gluing search covers pair-component shifts only; splits
  needing 3+ component shifts, or partners not pair-shift
  reachable, would be missed. Off-support gluing splits at m=16
  were not searched (only supported samples + component lifts).
- The m=16 bound is a sampling bound, not a theorem; a full
  census is infeasible at this scale.
- The mode-sum refutation is a theorem given wave-21 Adj data
  plus the symmetry of S_k; it does not depend on sampling.

## Files

- This note: wave22_Adj_link.md
- Scripts: wave22_Adj_m8.py, wave22_Adj_m16.py,
  wave22_Adj_m16_sample.py (sample-only rerun; its final JSON dump
  failed on a removed variable name, numbers preserved from its
  DONE line)
- Data: wave22_Adj_m8.json (39 split fibers),
  wave22_Adj_m16.json (10 lifts, 2,000-point search),
  wave22_Adj_m16_sample.json (20,000-point search totals)
- Repository untouched; no Lean build.
