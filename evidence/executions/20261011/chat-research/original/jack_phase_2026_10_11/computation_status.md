# Computation and formalization status

## Successful exact controls

The authoritative runs are:

- runs/exact003/manifest.json: schema-v2 bounded execution, validated against
  current immutable execution inputs. Python 3.12.14 and g++ 13.3.0.
  190 Jack cases; 1180 pair identities after clearing denominators;
  13 independent C++ SSYT cases; 87 Weyl-dimension/variance controls.
- runs/pfaffian001/manifest.json: schema-v2 bounded execution, validated
  against current immutable execution inputs.
  27 direct-density/Pfaffian comparisons (N=2,3,4, n=1..3N);
  48 larger exact weighted-shift cases (N up to 128), including n=N,
  n=2N-1, n=2N and n=3N.
- runs/cumulant001/manifest.json: schema-v2 bounded execution, validated
  against current immutable execution inputs. 1581 exact CSE fourth
  cumulants and 1581 independent unweighted CUE trace-log cases;
  45 critical CSE block coefficients at balanced orders r=1,2,3;
  9 independent direct-density sixth moments; 272 finite closed-word
  multiplicity controls (24 at r=2, 248 at r=3).
- runs/wolfram_controls_receipt.json: remote evaluator receipt, submitted
  source and timestamps. Wolfram Language 15.0.1, Linux x86, 2 July 2026.
  Four symbolic Boolean groups passed: dimensions, N=2 Dyson gap moments,
  N=2 CSE trace moments and coefficient mass 13/4.

The WL kernel performed exact arithmetic before exporting RawJSON.
Some rational outputs are serialized as decimals; the exact local Fraction
results supply the corresponding rational values. This serialization is
not treated as an exact numerical certificate.

## Failed development runs retained

The first two runs are retained as history, not successful evidence.

- exact001: the script discarded zero coefficients and then attempted to
  index the absent diagonal coefficient of the constant monomial.
  The corrected lookup uses the mathematical zero. The original script
  snapshot is stored in that run directory.
- exact002: a variance control wrongly used a symmetric-space norm formula
  for a CUE character. The human theorem already distinguished these
  normalizations. The control was corrected: CUE characters have norm one.
  The original script snapshot is stored in that run directory.

The successful exact003 run was fresh. Neither failure was hidden or
overwritten. The historical failed manifests hash the earlier code;
current-input validation is asserted only for the successful runs.

Before cumulant001, contract validation rejected a configuration typo:
`mathematics.inputs` needed an array and `bounds` a range object. No
experiment was launched by that rejected attempt. The corrected contract
and the resulting successful run are included; no rejected attempt is
counted as a scientific check.

## Reproduction

From this directory, choose new output-directory names and run the commands
in the authoritative manifests, or use the readable examples in
reproduce_controls.md. The bounded runner checks hashes before and after
execution and records the actual command, software versions, logs and
effective memory/CPU/affinity/thread caps.

The experiment inputs and local scripts need only Python's standard
library and a C++17 compiler. No network, BGS checkout or mutable prior
result is required. Numerical thread limits are cooperative environment
caps; process memory/CPU limits are POSIX limits, not an aggregate
process-tree accounting guarantee.

## Lean 4

formal/ArithmeticCore.lean is an UNCOMPILED Mathlib draft of the final real
arithmetic implication. Lean, lake and Mathlib are not installed here.
It contains no sorry or imported assertion of the research theorem, but
its elaboration has not been checked. No formal certificate is claimed,
and it does not formalize the group-theoretic or point-process argument.

## Mathematical interpretation

The general conclusions rest on the written proofs and named standard
source theorems, independently audited as documented in sources_and_audit.md.
Finite execution successes do not prove arbitrary N, all signatures,
point-process convergence, scientific novelty or general BGS.

