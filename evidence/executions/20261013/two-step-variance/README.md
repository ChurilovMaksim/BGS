# Complete two-step increment: review and finite scope

**Claim:** BGS-TRACE-078. Frozen base:
`9fc5d03865d0262c300062170654742c1ea76d38`.

[Candidate](candidate_reviewed.md) SHA256:
`a9dc3382474c53e0d01db3cc81719f573b7638b5760b0d54ba5699a57ca140c4`.
[Independent reconstruction](independent_review.md) SHA256:
`be9e33eebb0ee3c92f373e380354a9bfecf70ea220fff01ef4b165290a4c40b3`.
The maintained proof changes only status/context and replaces the request
for audit with its completed disposition; the expansion, inequalities,
constants and hypotheses retain the reviewed bytes.

The root [executed control source](executed_control_source.py) was run
outside the repository with SymPy rational/complex exact arithmetic and
NumPy complex128, one BLAS thread and a 90-second timeout. Its actual
[output](controls.json) covers 16 exact Walsh transitions (two pairs,
four phases, two surviving ports), and nine arbitrary-port-phase sums
at size 64. The independent reviewer's different finite controls are
described separately in its report and are not this execution.

Maintained reproduction:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 90 \
python3 computations/verification/two_step_increment_variance.py
```

Neither finite execution proves the universal raw second-moment theorem,
concentration, survival of an entry-stopped trajectory or BGS. The proof
uses complete coordinate Parseval sums before absolute-value bounds;
its averaging factor requires a conditionally uniform port. Phases
themselves need not be uniform or independent for this bound.
No new external theorem leaf, Lean kernel or C++ certificate is asserted.

## Final repository validation and preserved failures

The maintained verifier was rerun through the workspace runner after the
assertion-entry message correction. Six selected checks passed with source
bytes unchanged. Full local maintenance regression: 236 tests passed; the
separate seven-test entry-policy suite also passed. These are not a full
Python/C++ workspace execution or analytic formal certification.

The previous Green head's CI failed its maintenance gate because the
new script's optimization rejection message differed from the mandated
repository text. The actual decoded log is retained in
`preceding_green_ci_failure.log`; mathematical verifier execution did not
begin in that failed job. Both new verifiers now use the exact message.
The six other jobs of that previous head succeeded, including formalization.

The first manuscript attempt failed because a split environment had
multiple alignment columns; its log is retained. The corrected aligned
layout passed all three LaTeX passes: 296 pages, no overflow or unresolved
references. Every page was parsed; pages 291–292 were visually inspected,
and all final TeX source hashes were rechecked. PDF SHA256:
`6cc17442ebcb19d8b9ce7f7276f001c2739b04e8ce42d6a6c6daa826ddf0fbf8`.

The mechanical [transfer record](maintained_transfer.json) compares the
complete mathematical body byte for byte with the independently reviewed
candidate. Only context/status and audit disposition differ.
