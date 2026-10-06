# Exact first-seven replay

Run the maintained entry point from any working directory:

    python3 computations/verification/first_seven_commutant.py
    python3 -O computations/verification/first_seven_commutant.py

Requires an installed C++17 compiler (default g++, or CXX/--compiler) and SymPy
for the six dictionary controls. Compiled executables live in a temporary
external directory and are removed after the run. Optional --output DIRECTORY
writes logs and a receipt; source-tree destinations outside build/ are rejected.
No output directory is created by import. The optimized Python run also compiles
C++ with -DNDEBUG; all certificate checks remain explicit exceptions.

## Data and execution bounds

One 241,060-byte, hash-pinned certificate.txt reproduces the independently
reviewed serialization. It contains all data needed for the 18 minors and
exact polynomial identities. The 29 original candidate hashes and the review
artifact manifest are retained in evidence. Large duplicate development JSON
files are deliberately not required by replay.

- Six residue classes; three 48-by-48 minors from a 63-by-48 matrix per class
- 937 distinct interpolation nodes and 10 extra nodes per minor: 17,046 exact
  determinants, of which 16,866 prove polynomial identities using degree <=936
- Field GF(5^6), base-five coefficient codes 0..15624; full 15,624-element
  multiplicative orbit and 156,250 direct polynomial product comparisons
- Gcd, Bezout, quotient/reconstruction identities and degree-6/34 root exclusions
  use exact polynomial operations and binary digits of exponents through 5^102
- Actual residue controls N=7,21,63; largest system 3969-by-440
- Six split-prime dictionary controls through N=203, prime <=2437
- Each compilation/execution command has a 180-second timeout. No additional
  OS memory cap is claimed; the recorded runtime receipts state actual times.

C++ performs field operations by certified lookup tables and bounded coefficient
arithmetic. Field-code indices stay below 15625 and log sums below 31248.
Direct six-term convolution/reduction coefficients are small signed integers;
raw phases for N<=63 are below 8*N^3 in magnitude. Exponentiation reduces
ordinary exponents modulo15624 using long long, while enormous Frobenius/order
exponents use exact binary vectors. All are well inside the relevant machine
integer bounds. The Python split-prime controls use arbitrary-precision ints.
No floating-point number participates in a mathematical certificate.

The strengthened portable C++ parser requires exactly six cases, validates
input extraction and excluded-factor bounds, and rejects trailing tokens.
The wrapper additionally rejects any changed certificate by SHA-256 before
compilation. This is a pinned certificate replay, not an arbitrary-input API.

The interpolation argument plus the reviewed algebra proves a uniform
common-commutant theorem in the stated family. The actual small-N and six
split-prime controls alone do not prove universal rank. None of this formalizes
Lean semantics, proves seven-divisible spectral simplicity, makes the complex
commutant of U scalar, or proves BGS.
