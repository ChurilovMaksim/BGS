# BGS-TRACE-133, BGS-TRACE-134, BGS-TRACE-135 certificate

This certificate checks `mathematics/fixed-map/revival_closure_law.md`, for the position-diagonal kick only. It covers:
* the twisted closure formula, in floating point against brute-force traces;
* the closure count, the norm-lemma boxes, the dichotomy and the families, exactly in integers;
* the half-period parity reduction.

The Monte Carlo rows are diagnostics. On the family, the explicit bound of BGS-TRACE-134 gives no information at these dimensions. For BGS-TRACE-136 and BGS-TRACE-137, which are **open**, the rows test conjectures and prove nothing. A pass does not prove BGS-TRACE-005 or BGS-BGS-001.

```sh
python3 computations/verification/revival_closure_law.py        # about 40 s, prints PASS
python3 computations/verification/revival_half_period_parity.py # about 70 s, prints PASS
cmake -S . -B build && cmake --build build --target revival_closure_law revival_half_period_parity
./build/revival_closure_law                                       # C++ twin, prints PASS
./build/revival_half_period_parity                                # C++ twin, prints PASS
python3 computations/verification/scientific_registry_audit.py    # OK
```

Lean, toolchain `leanprover/lean4:v4.33.1`:

```sh
lean formalization/Bgs/RevivalClosureRational.lean
cd formalization && lake exe cache get && lake build Bgs
```

Logs in this directory:
* `revival_closure_law.log` and `revival_half_period_parity.log` are the Python runs.
* `revival_closure_law_cpp.log` and `revival_half_period_parity_cpp.log` are the C++ runs; `scientific_registry_audit.log` is the registry audit.
* `lake_build_Bgs.log` was regenerated at integration (8793 jobs) and replaces the packet's build log.
* `lean_axioms.log` shows that no theorem depends on any axiom.
* `lean_controls.log` records seven false variants, all rejected by `decide`. The script that produced it is `lean_controls.sh`.
