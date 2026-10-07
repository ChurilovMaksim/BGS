# Odd newest-sector exact controls

Use Python 3.10 or later on POSIX/Linux, with no third-party packages:

    python3 -B computations/verification/odd_newest/run_checks.py --output-dir /absolute/fresh/scratch/path

The path to the script may be absolute and the current directory arbitrary.
Output must be a new or empty directory outside the checkout/overlay. A full
replay reconstructs pinned original source bytes in that scratch directory,
runs three original controls, then runs their portable versions normally and
with -O. All scientific fields are compared to the independent review's frozen
JSON; only elapsed_seconds is excluded. All five public Python modules are
also imported in both modes and must be silent and create no files.

The exact output assertions cover:

- 1,500 rational-cyclotomic fiber overlaps, including 500 parallel cases;
- 391,250 raw covariance entries, 393,750 packet-carry entries, and 16,250
  raw oldform-intertwining entries;
- holonomy valuations at l=1,...,8 and all primitive circles at l=1,2,3;
- 5,616 intersection root cases through h=625, including 1,116 direct
  full-circle comparisons through h=125;
- all 32 actual coefficients, with exactly nine surviving upper modes;
- all 24 norm/tame degree-seven characteristic polynomials, gcd degree zero,
  Cayley-Hamilton identities, and exact serialized author polynomial matches.

Arithmetic is exact over Q(zeta_5), modular integers and F5[z]/Phi_7. The
finite matrices use a division-free permutation-subset determinant. The
all-depth implication is in mathematics/odd_newest_sector_first_jet.md and
its independent review, not in the finite bounds above.

Each subprocess is limited to 180 wall seconds, 180 CPU seconds, 2 GiB address
space and one CPU affinity slot. Conventional numerical-library thread caps
are one; the code uses no numerical library. Captured output is checked against
1 MiB after termination. These are per-process caps, not aggregate budgets.

The original source assertions and optimization prohibition are preserved in
lossless envelopes. Portable checks use explicit AssertionError branches that
remain active under -O. The unchanged coefficient function is extracted into
coefficients.py, with the same explicit-assertion conversion. All original
execution statements now run inside main(argv), so imports do no verification.
The author's stale even-layer docstring and identification-unproved serialized
status remain historical and are not silently rewritten.
