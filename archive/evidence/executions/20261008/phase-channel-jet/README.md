# Phase-channel and sharp-jet execution packet, 8 October 2026

This packet accompanies three reconstructed project proofs: TRACE-053,
TRACE-054 and TRACE-056. Independent review means a separate internal
reconstruction; it is not external journal refereeing or a priority verdict.
The submitted TRACE-055 remains verification-pending.

## Contents and evidence scopes

| File | Actual scope |
|---|---|
| channel_review.md | Independent complete occupation-path reconstruction, both collision corrections, exact degree-two channel and Fejer pinching argument |
| flow_scalar_review.md | Independent scalar sharpness and normally absorbed real-flow L1 transport; the former scalar-only matrix boundary is superseded by matrix_review.md |
| matrix_review.md | Independent noncommuting cascade proof, localized correction and adversarial checklist; the scalar factorization is reconstructed directly |
| python_verification.json | Complex128 phase-character quadrature, 1800 matrix cascade controls, 48 finite inner products at 8192 circle points, 32 common-phase scalar-flow controls at 16384 points |
| cpp_verification.json | Exact uint64 occupation multiplicities: 76 degree/dimension cases, 694526 enumerated words, m=3..40 |
| wolfram_receipt.json | Actual symbolic evaluator output {0,0,0} for the maintained Poisson and count identities |
| lean.log | Complete 20-module pinned Lean build and printed axiom lists; analytic statements remain unformalized |
| manuscript_build.json | Three-pass 280-page TeX build, immutable source hashes and fail-closed warning gate |
| visual_review.json | Title and all four new section pages rendered and inspected, plus a bibliography page; no full historical-page certification |
| run_manifest.json | Commands, versions, source digests and finite coverage; not a theorem or complete remote acceptance suite |
| metadata_validation.json | Selected registry/dependency/topic/new-link checks against the pinned remote inventory and local new files |

## Commands actually used

Run from the repository root unless specified otherwise:

```sh
python computations/verification/phase_channel_jet.py --output evidence/executions/20261008/phase-channel-jet/python_verification.json
c++ -std=c++20 -O2 -Wall -Wextra -Werror computations/cpp/phase_occupation_jet_verifier.cpp -o /tmp/bgs-phase-occupation
/tmp/bgs-phase-occupation
python computations/maintenance/render_claim_registry.py --check
python computations/maintenance/sync_finite_orbit_section.py --check
python computations/maintenance/build_unified_manuscript.py --output-dir /tmp/bgs-manuscript-20261008
```

The full Lean command was issued in formalization/ using the unchanged pinned
Lean 4.33.1 release and the maintained optional proc-self compatibility shim:

```sh
LD_PRELOAD=/tmp/bgs-lean/compat.so /tmp/bgs-lean/lean-4.33.1-linux/bin/lake build
```

Ordinary environments use `lake build` directly. The release archive SHA-256
is 890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235.
The shim redirects only the runtime's missing exact self-executable lookup;
it does not change Lean proof checking. The new module uses no sorry or
native_decide; its four printed axiom lists are propext and Quot.sound.

Wolfram evaluated computations/wolfram/phase_channel_jet.wl through the
symbolic evaluator. The output is retained, including its final Null from
Print; it is not evidence that a local Wolfram kernel was installed.

The Python quadrature reproduces finite phase integrals algebraically via
roots of unity, but evaluates them in complex128. Circle quadratures and
random matrix samples are numerical controls with explicit tolerances and
seed, not exhaustive matrix proofs or certified asymptotic estimates.
C++ uses integer counts throughout. The full CMake target set and all prior
Python verifiers were not rebuilt/re-run on this partial overlay.
