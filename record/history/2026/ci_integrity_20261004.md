# Publication integrity completion, 4 October 2026

This operational review supplements the
[research proof audit](../../expansion_wavepacket_review_20261004.md).
It changes no theorem, claim status, mathematical assumption or verifier
acceptance condition.

## Observed remote failure

The first scientific CI run for the research publication at commit
90a08af25405a75bf42ab4fe6cb4ca22e4c6576c is
[run 37188008404](https://github.com/ChurilovMaksim/BGS/actions/runs/37188008404).
The registry, repository-structure, finite Lean formalization and manuscript
jobs passed. All 146 maintained Python/C++ verifier exit rows were zero,
including the newly added packet/expansion finite controls and the two
sequential certificate replays. The computation job then failed in the
supplement integrity check, before any supplement replay could execute.

`supplement/fixed_map/resolvent-flow/loop_bridge.md` had SHA-256
a85aec3d223ea8d0c85ae8e5062b03c458eb633679873432428c85012255c448 and size
13394 bytes, whereas the supplement inventory retained the previous hash
636c63a912053a60a653ade651c6c45329d421acacd307ad0e9438ecec183fa4 and size
13390 bytes. Both the corrected text and the stale inventory were unchanged
from canonical base 34d682096f03bd4b7bd033d99755a02d921eb79a.
The repair updates only that current-edition inventory row and clarifies
the supplement's provenance wording. Historical checkpoint and execution
records are preserved.

## Fresh local replay

The first complete local replay after the inventory correction ran 28 checks:
23 passed and five exited on missing `sympy` or `mpmath` imports. This was
an environment failure, not a failed mathematical assertion. SymPy 1.14.0
and mpmath 1.3.0, matching the repository requirements, were installed in a
separate scratch dependency directory. A fresh isolated complete replay
then passed all 28 checks, including the high-precision gap identity,
variance reviews and fixed-map classical checks. Generated outputs stayed
in private replay copies; the maintained supplement was not rewritten.

Every one of the 115 inventoried files was additionally checked for both
its declared SHA-256 and byte count. There were no remaining mismatches.
The [replay evidence](../../../evidence/20261004/supplement_replay_completion.json)
retains all per-check commands, source hashes, elapsed times and log hashes.
The [completion record](../../../evidence/20261004/publication_ci_completion.json)
retains the failed remote job's exact scope and the local environment failure.

The original targeted evidence describes its dated research snapshot;
this later operational overlay does not retroactively alter those hashes.
The resulting commit's remote CI status is reported by its GitHub checks,
not assumed in this pre-publication record. Finite executions and compiled
Lean certificates do not prove the new analytic packet theorem or BGS.
