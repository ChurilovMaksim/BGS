# Ramified first-seven exact controls

Run the top-level ramified_first_seven_trace.py with ordinary Python and -O.
Requires Python3 and SymPy; no candidate code, network, compiler or canonical
project helper is imported. Imports are silent and explicit failures remain
active under optimization. Output defaults to stdout; --output FILE accepts
only a fresh file outside maintained source or below build/.

The only runtime data is the reviewed, hash-pinned 5,510-byte certificate.json.
All six original candidate hashes are separately verified in preparation and
retained for lineage. The independent verifier reconstructs the raw Laurent
model, rather than trusting a saved success flag or importing the author code.

Exact scope:
- Polynomial identities over F5, including Phi7-square normalization and Bezout
- Independent low-first six-tuples in F5[w]/Phi7; arbitrary-precision Python ints
- All21 collision pairs and all 9 exceptional partitions
- All49,441,1225 Fourier minors of sizes1,2,3 for one primitive seventh root;
  the tested Frobenius orbit and mathematical conjugacy cover the other roots
- All900 normalized exponent quadruples
- Direct complete chain sums for e=1,...,6 and N=7*5^e through 109375

Every loop is bounded by these fixed inputs. No OS memory or CPU cap is claimed.
Runtime is measured separately; no floating-point arithmetic participates in
mathematical comparisons. Negative/tampered input, zero inverse and source-output
controls are checked separately by the portable unittest regression.

The finite program is not a formal proof assistant and is not alone a proof
for every N or every e. Uniformity comes from the separately reviewed valuation,
partial-trace and augmented-rank argument. No theorem for 245|N, no scalar full
complex U commutant, no seven-divisible spectral simplicity and no BGS result
is certified by this program.
