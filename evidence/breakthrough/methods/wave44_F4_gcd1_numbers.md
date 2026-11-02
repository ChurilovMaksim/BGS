# Wave 44, task 4 (retry 2) — locked periods d_a on the 9t line: numbers only

Method: wave-38 `split_fibers`/`period`/`recover_C`; locked = split
full prime-power component of D_m (≠ free 3-component), fiber-0 rep.
Validated by reproducing the known cases exactly.

| m | locked component | d_a | gcd(d_a,36) |
|---|---|---|---|
| 36 | none (see below) | undefined | — |
| 72 | 512 (full 2-component, 5 split fibers, fiber-0 rep injective on its period) | 8 | 4 |
| 108 | undetermined (non-standard: 3\|t) | — | — |
| 144 | 2048 (full 2-component, 10 split fibers, fiber-0 rep injective) | 16 | 4 |
| 180 | 625, fiber-0 rep C=(0,550) | 30 | 6 |
| 252 | 2401, fiber-0 rep C=(0,2107) | 21 | 3 |

Details. m=36: odd component list is complete (odd cofactor 1:
729, 25, 49, 121, 5329, 32041, 38809, 39601 — only 729 split)
and full 2-component 128 has no split fibers: no locked
component exists. m=108: 3|t, so the full 3-component is 6561,
not 729, and the 729-based section does not apply as stated;
no non-3 locked component found among tested moduli.
m=72/144: odd large components untested (72: 1009², 1153²,
1523089²; 144: cofactor unfactored) — possible alternative
locked components there are not excluded.

Verdict: no locked period coprime to 36 occurs at any of the
six values. Moreover lcm(d_a,36)=M alone forces gcd>1 for
m=36, 72, 144 (any admissible d_a≥3); for m=180/252, gcd=1
would require d_a=5/7 respectively — observed are 30, 21.
