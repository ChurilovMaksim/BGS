# Stopped two-step concentration: analytic and finite scope

**Claim:** BGS-TRACE-079. Reviewed base main:
`53d60cbb4b51d64b3ff82d396ab74e21f704f3a9`.

The frozen [candidate](candidate_reviewed.md), [independent reconstruction](independent_review.md)
and [maintained transfer check](transfer_review.md) are separate artifacts.
Candidate SHA256:
`47e365b06fa460e6d503b771b9b336403ee9a6e918e81d4a17b6c6be9a60aec7`.
Reviewed maintained proof SHA256:
`d215b3ac0aacb6243db40a61a6bb9530f0375c63cddcb6b5f9194667ceffc0ea`.
Only the startup event wording was clarified to include both barriers;
the quantitative theorem and stopping boundary are unchanged.

Root controls in [root_executed_source.py](root_executed_source.py) and
[actual output](root_controls.json) checked three exact rational unitary
pair phase integrals at size 16, including two diagonals. They also checked
15 exact deterministic telescoping targets across no-stop, endpoint-stop
and global-crossing bookkeeping examples, and factorial domination through
order 50. The first implementation attempt failed because a SymPy index
was not converted to a Python integer before `bit_count`; no result from
that attempt was accepted. The corrected source produced the preserved
output and log.

The reviewer's [independent code](independent_control_source.py) and
[output](independent_controls.json) instead use exact rational controls at
size 64, four ordered pairs and 1,250 direct phase/Schur comparisons.
These were run by the reviewer and are not relabelled as a root execution.

Maintained reproduction:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 90 \
python3 computations/verification/stopped_two_step_concentration.py
```

Finite controls do not prove asymptotic probabilities or BGS. The analytic
theorem controls all retained pairs through the full first crossing;
it does not estimate the chance of reaching the deep range. TRACE-080
provides a separate stronger global trajectory result under its explicit
initial small-gap conditions. No new Lean/C++ certificate is claimed.

The maintained verifier's resource-capped
[bounded execution](bounded/manifest.json) completed with exit zero,
unchanged declared inputs and a passing manifest validation. The shared
[8/8 focused receipt](../global-feedback-flatness/workspace.json),
[236-test maintenance receipt](../global-feedback-flatness/maintenance_full.log)
and [298-page manuscript receipt](../global-feedback-flatness/manuscript_build_manifest.json)
are preserved with their exact scopes in the companion packet. Parent
CI success is recorded separately there; it is not a new-head replay.
[source_manifest.json](source_manifest.json) binds the frozen evidence
and checked canonical-source checkpoint.
