# BGS research continuation, 17 October 2026

Start with [progress_ru.md](progress_ru.md). The BGS and two-port universality
goals remain open. Repository writes are forbidden in this continuation and
none were made.

Main new proof: [uniform_heisenberg_path_current.md](uniform_heisenberg_path_current.md)
under fixed-level TV compactness [TC], with the general fixed-colligation
kernel proved in [tensor_path_current_limit.md](tensor_path_current_limit.md).
The full normalized positive path clock is covered at any K_N->infinity.

Independent auxiliary result: [rare_star_heisenberg.md](rare_star_heisenberg.md)
counts a rare circuit sector exactly and exhibits bounded iid-entry failures
of unrestricted Heisenberg Gaussian comparison. It is not a unitary/BGS
counterexample. [self_review.md](self_review.md) states audit boundaries.

The exact remaining two-port problem is [remaining_task_ru.md](remaining_task_ru.md).
Prior inputs and their original hashes are in proof_inputs.json and inputs/.
Classical source scope is recorded in literature_scope.md.

Exact reproducible checks: verify_star_sector.py with star_contract.json and
star_run/; verify_tensor_current.py with current_contract.json and current_run/.
The contracts specify ranges and non-claims. Scientific outputs are result.json;
each execution directory also contains a bounded-run manifest and stdout/stderr.
Python 3.12.14 and SymPy 1.14.0 were used. Set PYTHONDONTWRITEBYTECODE=1.

The proof source files have not been compiled in Lean. Computations validate
the declared finite assertions, not BGS or the entire analytic proofs.
