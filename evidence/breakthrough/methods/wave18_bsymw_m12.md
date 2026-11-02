# Wave 18, task 1 — Bsym_w(supp) at m=12, exact, and the corrected limit comparison

## Definitions (all averages over supp, |supp| = 96,049,800 = D/16)

- `Bsym_Γ = (1/|supp|)·Σ|Γy|` (orbit-size average; wave 17 value, reproduced here).
- `Bsym_w = (1/|supp|)·Σ|C_w|²`, `C_w` = (fiber, w)-class (same sorted y and sorted w).
- `Bsym_fiber = (1/|supp|)·Σ|F∩supp|²`, `F` = fiber (same sorted y).
- `R = Σ_F |Σ_{ξ∈F} φ̂|² / Σ_ξ |φ̂|²`, the pair-sum ratio (D1a target).

## Method

CRT enumeration over supported component seeds only: 8 × 81 × 25 × 49 × 121
= 96,049,800 points (only the 2-component restricts support). C++ grouping
by sorted(y) and by (sorted(y), sorted(w)), w = (Hy)/D, y ∈ [0,D).
Validations: independent Python check on a 2,381,400-point subset matches
exactly (829,839 fibers; 22,755,930; 830,454 w-classes; 22,065,882);
orbit census (dihedral stabilizers) reproduces wave 17's Σ|Γy| exactly;
φ̂ via wave-16 CRT machinery reproduces wave16_m12_phi.json exactly (diff 0).

## Exact results at m=12

| quantity | exact value | float |
|---|---|---|
| n_fibers / n_wclasses / n_orbits | 4,010,394 / 4,011,009 / 4,011,161 | — |
| Σ\|F\|² → Bsym_fiber | 76782059/3201660 | 23.98195280 |
| Σ\|C_w\|² → Bsym_w | 383795287/16008300 | 23.97476853 |
| Σ\|Γy\| → Bsym_Γ | 383766967/16008300 | 23.97299944 |
| R (s=1 and s=13 identical) | 383907271/16008300 | 23.98176390 |

Ordering: **Bsym_Γ < Bsym_w < R < Bsym_fiber**, all within 0.009 of each other.
Gaps: w−Γ = 0.001769, R−w = 0.006995, fiber−R = 0.000189.

## Cancellation, quantified

- Split fibers in support: 762, mass 35,952 points, Σ|F|² = 1,713,888,
  Σ|O|² = 853,920. Census-only bounds were R ∈ [23.96411, 23.98195].
- φ̂ is constant on Γ-orbits (proven by reindexing; numerically 2e-19) and
  |φ̂|² = 16/D on all 35,952 split points (maxerr 7e-23).
- Coherent total over split fibers = 1,695,744 exactly (integer, s-independent);
  deficit vs aligned = 18,144 (1.06% of split aligned total).
- Only 5 split fibers fully cancel (sizes 72, 36, 72, 72, 36, incl. the wave-16
  fiber); the rest are nearly aligned. Hence R sits 0.00019 below Bsym_fiber.

## Side facts

- P_w failure on support is tiny: 152 excess orbits beyond w-classes
  (n_orbits − n_wclasses); Bsym_w − Bsym_Γ = 169,920/96,049,800.
- Multi-w fibers: 610, mass 28,800 — confined to q=121 SNF rows 0,1,2
  (zero sequence + two 11-multiples); a rotated q=121 slice gives 0,
  so this is structural, not a code artifact.
- 99.74% of support points live in size-24 fibers; max fiber 72, max w-class 48.

## Answer: which does the pair sum track?

**None of the three exactly.** The pair sum tracks R = 23.98176390, a fourth
quantity: closest to Bsym_fiber (deficit 0.00019 from cancellation), above
Bsym_w by 0.0070 and above Bsym_Γ by 0.0088. Route (b)'s claimed limit value
Bsym_w is wrong in D1a/D1b form (wave 17 showed it on one fiber; now quantified
globally); a corrected derivation must subtract the cancellation deficit
18,144/|supp| from Bsym_fiber, not replace the value by Bsym_w.

## Caveats

- Bsym_fiber uses F∩supp sizes; equals the full-fiber version if supp is a union
  of fibers (evidence: wave 15 exhaustive to m=10, wave 16 lifts FULL/EMPTY).
- R computed at s=1 and s=13 (identical per fiber to 1.7e-11); other s not tested.
- Γ = dihedral group on 12 positions (24 perms); w from representatives y ∈ [0,D).

## Files

- `wave18_bsymw.cpp`, `wave18_orbits.cpp`, `wave18_splitpts.cpp`,
  `wave18_phi_split.py`, `wave18_comp_data.txt`
- `wave18_full.json` (Bsym_w, Bsym_fiber), `wave18_orb.json` (orbit census),
  `wave18_R.json` (R), `wave18_splitpts.bin` (35,952 split points)
