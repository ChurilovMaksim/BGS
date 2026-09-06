# Locality packet: final source, verification and integration status

Date: 2026-09-05. Scientific source head before this status-only record:
`bce32afac587ffed0e36d8f105adcbc953a62e72`.

## Executed source versus final editorial source

The completed local targeted manifest reports 20/20 commands and 124 input
science/configuration files. Its SHA256 is
`5e6ee3160a9f31c64ef9050c78016a411cec2d174add029b7126404623a06167`.
The recorded source fingerprint is
`9991eed91f0ab49de0d228f7d43b39d32c480e6b3bef1161c066e0dbcb2f7581`.

Only `mathematics/fixed_strength_locality.md` differs among those scientific
inputs after the recorded run: two wording corrections clarify the existence
of a linear subspace containing nonzero supported generators, rather than
claiming that all disjoint-support generators form a vector space. The
frozen-run proof SHA256 was
`b75eaa46cdfb26505f70b32b31faaf0275f3a5147efac3de7f54e4e296bfc5a6`.
Its final SHA256 is
`6c6c683daa7bd7528cd6272bedeaeec2a4b530a4c76ccbd2f68d95e9dace9a26`,
and its Git blob is `9fb8418f138a239612069ddc5639b09985eee897`.
No verification code changed. Both PDFs were regenerated from final sources.

The robustness proof has SHA256
`0d21e4588db6b73809f7475a7aeb395594a1b99a1ed929630c469bbf568b3050`
and Git blob `3512790cf5578dfef76c66545598cf8abc038278`.
The executed publisher was rechecked after upload against Git blob
`7be76b0be195d720c2b62534d3efc24bd74e9a6d`.

## Concurrent main and overlap of research claims

At the final comparison, main was
`4a29eae00d6a5394a89211a23d7367bf6277940e`, with 17 concurrent commits from
the common base `ea46a93f9ca09141a83fe784d22119776f5fe2e9`.
It already contains `mathematics/pell_all_orders_conjugacy.md`, an independently
developed proof of the same fixed-strength locality mechanism. These are not
two separate discoveries. The two notes use classical parameters differing
by a factor of 2*pi: exp(i*kappa*N*Op(f)) here versus exp(i*kappa*Op(f)/hbar)
in that note. No numerical constants should be transferred without converting.

The present addendum contributes the explicit covering/occupancy estimates,
stability under arbitrary unitary errors o(1/K), and necessary unfolding
distortion, with independent recorded finite checks. Its generic BGS and
priority limitations remain unchanged.

Pull request #15 records the source integration. It was not automatically
mergeable at the final check. No force update or replacement of concurrent
main work was performed. The root README/CMake changes must be reconciled
with the general-hyperbolic and analytic-rigidity additions before merging.
The local research packet is a verified reconstruction over baseline
3e702064d6500c2d87588a1a382899a61e654d46, not a mirror of that newer main.

## What is not certified

The complete historical Python run was interrupted. Lean was not compiled
in this runtime. Remote workflow failure occurred before execution steps;
its cause was not established. The 20-command local pass does not certify
all of current remote main. Successful source upload does not certify a
remote build or publication of binary PDFs.

The eleven-page locality/robustness PDF, nineteen-page local main PDF, complete
command logs, numeric data and source-hashed delivery manifest are provided
as conversation artifacts. The publisher can regenerate root index/ledger
and article inclusions; that is distinct from their remote execution.
