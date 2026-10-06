# Fifth supplied review: code contracts and certificate safety

The supplied review targets `0ffb20cc152d0ddd2620887e46d21d1120b95fd8`. All five reported defects were independently reproduced against the affected source bytes, which remained unchanged in the later research batch where relevant. None refutes FM-019/FM-020 or invalidates the normal aggregate runs within their recorded scope.

## Repairs

1. **Standalone assertion removal.** The false `51451/1000` → `51452/1000` expectation in a temporary frozen-full-lag copy failed normally but produced a passed certificate under optimized Python before repair. A uniform, explicit module-entry refusal now protects all assertion-bearing maintained modules and statically resolved local import dependents. The current protected set is 167 modules: 166 containing assertions and one import dependent. Historical evidence is unchanged. Explicit-check-only verifiers remain optimized-compatible. See [the policy](../computations/maintenance/ASSERTION_POLICY.md), which states its dynamic-import and programmatic-compilation boundaries. These counts are policy coverage, not counts of independently discovered false mathematical results.

2. **Large additive parameter.** Jacobi and Hermitian constructors now require exact integer scalars and reduce q modulo the prime before vectorized multiplication. The Jacobi path checks the safe int64 product bound before allocation. Public finite-field scalar helpers normalize Python/NumPy integer inputs and reject floats and booleans. Supplied discrete-log arrays are checked for shape/type/range; their group-log identity remains a documented input requirement.

3. **Zero in a multiplicative subgroup.** Validation now excludes zero, invalid types/shapes, duplicate residues and failure of multiplicative closure over an odd prime.

4. **Inconsistent residue representatives.** The subgroup validator returns canonical residues and both fast/direct consumers use them. Independent original-quadruple enumeration, not merely mutual agreement of the two implementations, checks every subgroup at primes 3,5,7,11 across six representative/order/dtype variants. The 156 comparisons include negative and arbitrarily large integer representatives.

5. **Repeated spectral levels.** Forward windows now count all points in the geometric half-open interval [x_i,x_i+width), retaining multiplicities and repeated anchors. An independent full-scan oracle covers tied levels, boundaries, all-tied cases and KDE-preserved ties. The reported [0,0,1,2], width1 case now gives variance0.25.

## Impact and evidence boundary

Both corrected v2 diagnostic reports reproduce every numerical field exactly across all 168 spectra. The checked inputs contain no exact raw/unfolded ties and no q-product overflow; the maximum product is 5,748,960. Thus the committed v2 numerical values are preserved. Historical polynomial diagnostics remain historical for their separately documented defects.

The merged maintenance suite passes 33 tests both normally and under an optimized parent. Its optimized-entry, import, guard-removal and synthetic false-predicate controls distinguish infrastructure checks from mathematical proof. The maintained numerical edge verifier and subgroup oracle checks pass independently. The final merged source manifest and aggregate execution are recorded in [the round-five receipt](../evidence/executions/20261006/round5-code/README.md); earlier receipts retain their original hashes and provenance.

No new theorem, global priority, full-code-domain certification or BGS conclusion is asserted by these repairs.
