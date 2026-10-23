# Independent C++ replay of the radius-eight resonance certificate (BGS-RES-022)

Date: 2026-10-23. This directory deposits the first run of the independent
C++ leg of the two-validator standard stated in
`mathematics/resonance_nondegeneracy_and_hessian.md`, Sections 2.2--2.3.
The 2026-10-06 receipt (`independent_cpp_coefficients: NOT_RUN`) is a
historical record and is not modified by this deposit.

## What was run

The maintained checker, with the C++ program supplied:

```sh
cd computations/verification
python3 check_resonance_certificate.py \
  evidence/executions/20261006/corpus-revision/final/checks/certificates-mpuvq_28/resonance_nondegeneracy_radius8.json \
  --cpp <build>/resonance_complex_replay \
  --output evidence/executions/20261023/resonance-cpp-replay/resonance_certificate_replay_cpp.json
```

Result (`resonance_certificate_replay_cpp.json` in this directory):
status PASS; `independent_cpp_coefficients: "PASS"`;
`independent_cpp_proof_replay` PASS with rule counters
{P 3293, S 1077, D 1229, F 105} identical to the Python replay;
`negative_controls_rejected: 6` -- the four Python mutation controls and
the two C++ instruction-stream controls (an empty refutation child,
`F 0 / E`; a division without an assumed nonzero pivot, `D 0 1`), each
rejected with a nonzero exit. The equation hash of the reconstructed
system is the deposited `7462bc1a522a57741028efd6642710fa50aa271b27f21bfc6a683f578aee53f4`.
Wall time for the full checker run was about 2 s; each C++ invocation
takes about 0.3 s against the checker's 40 s cap.

## The implementation and its independence

`computations/cpp/resonance_complex_replay.cpp` (SHA-256
`1921ad4dd6b966885c3cd30823b92b0a2d57f064e048d215c93b2c7dafd1abc5`) was
written from Sections 2.1--2.3 of the source text. Its canonicalization
is the text's C++ method -- exact arithmetic in Q(sqrt(2)) with
eigenbasis window enumeration over -16 <= j <= 16 and boundary failure --
not the Python generator's greedy neighbour descent; its replay engine
implements the four rules from the Section 2.3 prose over the
RESONANCE_COMPLEX_V1 text serialization. The only interface taken from
the Python checker is its I/O contract (command line, JSON shapes,
pass criteria, the two control streams). One representation convention
was fixed by the contract, not by the mathematics: a monomial's two
factors are serialized in nondecreasing (variable, exponent) order and
the two spellings of a monomial merge; the reconstructed polynomials
are identical under either spelling.

## Build record

- Source registered in `CMakeLists.txt` as target
  `resonance_complex_replay`; the full CMake build (all 27 C++
  verifiers) is green.
- Compiler: g++ 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1), C++20,
  Release; Boost 1.89 headers (`boost::multiprecision::cpp_int`).
- Binary of this run: SHA-256
  `7d79ee94ecb5e64f6ba91faca5787edb80858e303003b3d75c1cc418196371ab`
  (a build artefact; the source and this record are the durable
  deposit).

## Scope

This deposit closes an implementation-independence gap: the coefficient
system and the deduction stream are now reconstructed and replayed by
two independent implementations under two different canonicalization
algorithms. It does not change the state of BGS-RES-022, which remains
verification-pending pending a separate status review; it makes no
statement about radii above 8, about the analytic parts of the source
text, or about BGS universality.
