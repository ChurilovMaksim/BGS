# Independent referee replay of the random-phase expansion

Deposited 2026-10-29 with the Line C integration. The sources in this directory are the referee's from-scratch C++/Python engine. They share no code with `computations/verification/lineC/engine.cpp` or `symbolic.py`. Compiled binaries and `__pycache__` are not stored.

The run logs are `evidence/executions/20261029/lineC-random-phase/independent_replay/`. `compare_theirs.log` records that every Theorem 7 coefficient agrees at 171 primes in `[101,1200]`: all orders for `m=3..10`, and through `p^{-5/2}` for `m=11,12`.

`compare_theirs.py` still names the referee's original absolute paths (`/workspace/bgs-lineC/logs` and `/workspace/audit/lineC/code`). Those paths are not rewritten here, so the deposited log is the record of that run. The report is `REPORT.md`.

This replay is the record named in the closure note for BGS-TRACE-147. The claim stays verification-pending. Promotion is a separate status decision, as for BGS-RES-022. The replay does not prove BGS-TRACE-005 or BGS-BGS-001.
