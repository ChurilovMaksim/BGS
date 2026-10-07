# Initial promotion-harness attempt

The four author/independent scientific runs completed with exact frozen-output
agreement and normal/-O byte equality. The staging harness then stopped on its
synthesis negative-control fixture: the AST selector chose the module main
guard, so it exited successfully rather than exercising a mathematical check.
This was a harness-selection failure, not a mathematical counterexample or a
failure of any assertion in the original sources. No synthesis scientific run
had started. The original runner, comparison, failed execution manifest and
completed outputs are retained byte-exact here.

Recovery narrows the AST selector to the actual Hamming equality check. The
mathematical adapters and frozen sources are unchanged. The entire bounded
suite is rerun from scratch for the final authoritative promotion record.
Historical output paths in the failed manifest point to the original replay
location; the corresponding byte-exact retained files are now in this directory.
The original runner is retained as fractional_hamming_replay.py.
