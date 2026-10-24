# 20--21 September fixed-map continuation

This directory is a provenance/index layer for the late conversation handoff. The maintained theorem statements and proofs are promoted to the top-level mathematics directory rather than duplicated here.

Promoted sources:

- [moment controls, reduced-loop falsifier, and growing transfer](../../../mathematics/fixed_map_moment_control_and_transfer.md)
- [three-orientation barrier](../../../mathematics/three_orientation_resolvent_barrier.md)
- [actual frozen-model symmetry theorem](../../../mathematics/fixed_model_symmetry_theorem.md)
- [full-symbol odd-Pell crossover](../../../mathematics/fixed_model_pell_crossover.md)
- [Fourier-line resonance coercivity](../../../mathematics/resonance-cohomology/fourier_line_resonance_coercivity.md)
- [local jet obstruction](../../../mathematics/resonance-cohomology/local_jet_resonance_obstruction.md)

The exact recovery/integration disposition is recorded in
[the final handoff audit](../../../record/final_research_handoff_20260921.md), and the fresh replay summary is
[evidence/recovery_20260921/replay_summary.json](../../../archive/evidence/recovery_20260921/replay_summary.json).

The original conversation archive had SHA-256
032e965cd39a12d2a19f5520fad84fdb305043ef2717e8e8adeac79a34e02c01
and a 54-file root manifest. The archive itself is not vendored into main: source packages are represented by their maintained proofs, checks, evidence hashes, and Git history rather than by a second zip copy.

The original saved Wolfram checks were manifest-verified but were not freshly executed during this integration. The maintained Python regression
[computations/verification/bgs_20260921_regression.py](../../../computations/verification/bgs_20260921_regression.py)
checks the load-bearing exact algebra used by the promoted statements.
