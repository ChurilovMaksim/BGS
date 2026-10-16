# Complete Wick collision proof: actual execution scope

Base main: `f78ec82ffe8c6535c961abc969a719704bf3e942`.
Local workspace: partial pinned source snapshot, without a Git checkout.
The runner correctly records local Git revision as unavailable; the pinned
remote base and current source hashes are recorded separately.

The analytic authority is [TRACE-094](../../../../mathematics/wick_collision_poisson_20261016.md).
[Internal review](../../../../record/reviews/wick_poisson_20261016.md) distinguishes
the independent core reconstruction from author-derived corollaries.

## Executed exact audit

[Version-2 manifest](exact/manifest.json) and [actual JSON result](exact/result.json)
record Python 3.12.14, integer polynomial Fock norms, exact Fraction rationals,
source/dependency hashes, command, actual elapsed time and exit code zero.
The run used a 120-second wall cap, 100-second per-process CPU cap, 2 GiB address
space, one CPU core and cooperative one-thread library limits. No randomness.

The scientific child command, from the repository root, was:

```bash
python3 computations/verification/research_20261016/verify_wick_poisson.py \
  --output evidence/executions/20261016/wick-poisson/exact/result.json
```

The Mathbox bounded runner created the fresh `exact/` directory and captured
stdout, stderr and the manifest. Its separately run validator reported a valid
evidence record with current input and result hashes.

| Exact finite assertion | Actual coverage |
|---|---|
| Partial-contraction norms: monomials versus graph/hook evaluation | 928, in the explicit N=2,3 and m=4,...,7 families, k<=4 |
| Higher upper-index swap identity | 17 |
| Hook trace-product overlaps versus direct polynomial products | 86 |
| Directed cycle covers and gap/creation partition | 38,435 graph/order pairs, all partial matchings and cyclic orders through k=5 |
| Haar input/output dictionary via exact Gram inverse | 7 cases, degree 2k with k=1,2 in N=3,4 |
| Collision factorial indicator comparison | 12 |
| Row-occupation derivative identities | 20 |
| Bounded radial-weight versus collision transform inequality | 12 |

The abstract graph enumeration checks finite indexing patterns through k=5,
not all k. The analytic graph proof supplies the universal quantifier.
The mathematical Poisson law, spatial version and geometric occupations do
not follow merely from the pass flags.

## Integration and non-claims

The current source manifest and integration result pin the later maintained
proof/status surfaces. Earlier Abel/Gaussian execution records and their hashes
are preserved at their original revision; they are not rewritten to appear
as if they had run the new proof. The existing Hessian verification dependency
has unchanged bytes and its executed SHA is recorded in the new manifest.

The new source/metadata and active TeX reference checks are local and scoped.
No full-workspace regression, complete PDF build, analytic Lean compilation or
successful remote CI execution is claimed here. Remote publishing is reported
separately after the guarded main update. No non-flat physical transfer,
signed Heisenberg evaluation, full BGS theorem or external priority assessment
is supplied by this packet.
