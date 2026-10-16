# Finite controls for the 16 October Abel/Gaussian continuation

The mathematical authorities are TRACE-092, TRACE-093 and the subsequent
TRACE-094 in `mathematics/`.
These programs test dangerous finite normalizations and tensor contractions;
they do not prove universal quantifiers or a physical semiclassical limit.

From the repository root, with the repository Python requirements installed:

```bash
python3 computations/verification/research_20261016/run_checks.py \
  --output evidence/executions/20261016/abel-gaussian
```

The runner uses isolated temporary directories, explicit failure checks,
`python -O`, fixed input seeds and per-task time caps. It saves actual JSON
output, stderr, elapsed time, commands and source/dependency hashes.

| Program | Arithmetic and discriminating coverage |
|---|---|
| `verify_abel.py` | mpmath, 60 decimal digits; geometric trace sum versus finite positive identity, Fourier convolution including its support edge, direct periodization with an analytic tail bound. Includes N=1, both parities and repeated eigenvalues. |
| `verify_rigidity.py` | 60-digit alternating-spectrum identity, chord coercivity, exact rational phasewise test of the optimality witness, and CUE integral normalization. Imports the pinned `verify_abel.py`. |
| `verify_gaussian_factorial.py` | Exact integers and rational fractions; rooted words, edge tables, weighted collisions, Ewens deletion consistency, one-circuit reconnection and the weaker factorial bound. |
| `verify_gaussian_hessian.py` | Exact coefficient polynomials and Gaussian factorial norms; degree energy, hook signs, partial swap, all 24 eighth-sphere pairings, all six sixth-sphere pairings and all-m bounds. |
| `verify_generic_tensors.py` | Fresh independent integer-complex tensor controls, testing pair-symmetric tensors beyond the special trace-Hessian fixtures. |
| `derive_collision_mean.py` | Exact SymPy rational simplification of the finite mean and its constant and inverse-dimension expansion coefficients. |
| `verify_wick_poisson.py` | Integer monomial norms versus directed contraction graphs/hook overlaps for all partial matchings in the stated finite cases; exact rational Haar Gram inversion, higher swaps, indicator and vertex identities. The separate Wick packet records its actual run. |

`abel_identity.wl` is the source actually evaluated by the Wolfram connector;
its returned output is in the execution record. It is not a Lean proof.

`sample_conditioned_ewens.cpp` samples an exact finite probability model by
integer-weight permutation insertion and one-circuit rejection. The trace-word
measure identity is proved in the dated factorial-route review. For positive
N,m,target within available memory, an example bounded exploratory run is:

```bash
g++ -std=c++20 -O3 computations/verification/research_20261016/sample_conditioned_ewens.cpp -o /tmp/bgs-ewens
/tmp/bgs-ewens 100 100 20000 20261016
```

The source reports the seed, rejection count, sample moments and empirical
standard errors. It provides neither certified tail probabilities nor a
Poisson limit. Platform C++ random-distribution implementations can differ.
The executable is temporary and is not committed.

The preceding metadata audit was run against its recorded Abel/Gaussian source
revision. Its source pins are historical; later theorem/status edits are not
expected to retain those old hashes:

```bash
python3 computations/verification/research_20261016/verify_integration.py \
  --output evidence/executions/20261016/abel-gaussian/integration_checks.json
```

The optional `--baseline-tree` is only for a disclosed partial snapshot. It
supplies path existence, while mathematical sources and pinned data must still
be actual local bytes. The local receipts do not certify remote CI: the
scientific commit's workflows failed without recorded code steps; see
`evidence/executions/20261016/abel-gaussian/remote_ci.json`.

For the subsequent complete collision proof, run the bounded exact program:

```bash
python3 computations/verification/research_20261016/verify_wick_poisson.py
```

Its maintained contract is `wick_poisson_contract.json`; the executed version-2
manifest records the actual runner, input hashes, integer arithmetic and caps.
Use the new `verify_wick_integration.py` for the later scientific source state.
The previous packet remains immutable provenance for its own revision.
