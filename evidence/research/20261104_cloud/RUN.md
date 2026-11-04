# Execution record

Date: 4 November 2026. Host Python 3.12.3, python-flint 0.9.0, mpmath 1.4.1. No GPU, no Lean build, no change to `record/claims.json`.

## Commands

From `evidence/research/20261104_cloud/numerics/`:

```text
python3 span_exact.py
python3 kp_sharp.py
```

The sensitivity file was written by importing `kp_sharp.crossover` and scaling S_0 by 0.99, 1, 1.01, 1.03, 1.10. Wall time was about 13 s for the span census through shell 16 and about 6 s for the tail.

## Arithmetic and coverage

- Digit letters, carries, domain membership, and the span comparison are exact integer arithmetic. A square comparison decides m ≤ U + V√2. It is never an equality for V ≠ 0.
- mpmath at 50–80 decimals cross-checks the floor, the absolute-value predicate, the carries, and the powers of ε. It is not the decision procedure.
- Flint balls at precision 200 evaluate β, q, θ, the Kotecký–Preiss tails, and the uniform-norm ratio. Finite-part weights are the existing `a_cert3.jsonl` upper bounds, inflated by an extra 10^{-9}.
- The crossover is the v5 convention: IEEE gas factor, exact NSW integer K_p, Robin’s bound, primes up to 5000. Additive budgets are set to zero.

Inputs read and not modified:

- `computations/verification/lineN14/logs/a_enum.jsonl` (5109 classes, j ≤ 12)
- `computations/verification/lineN15/logs/a_cert3.jsonl` (certified |w| upper bounds)

Coverage of the span census: every fundamental-domain class with 1 ≤ |N| < 2^{17}. That is shells j = 0 through 16. The inequality for larger shells is the proof in `proofs/01_span_bound.md`, not the census.

## Hashes

```text
db740a604a9f75c6a316ec3debba5ef3f1c9b813eb2b31a7c1db2c9d7bec6fb6  numerics/span_exact.py
04f0f5dec238469826dee51b568bec08846e88ce49ad318b4ce0d9f93cc52163  numerics/kp_sharp.py
6f07eaadc46b00510ffaf6a8c4b1b9efdd7e18cf3fce5f7382f73f951e222abb  numerics/logs/span_exact.json
09f86a1d1f06f590d4791aa649e60371e7b0bd2c25d6f710bc205aeb208f5dca  numerics/logs/kp_sharp.json
2f98046d7d8cd13e2a9b22c02ab1ba7d8f5ab1df1fd1ccaca386154a3749ba53  numerics/logs/crossover_sensitivity_sharp.json
```

## Continuation (same day)

A second exact pass walked shells j ≤ 16 and recorded letters: 81 709 classes, every letter in {−1, 0, 1}. An independent BFS on |a − 2b − c| ≤ 60 inside |e| ≤ 51 returned 8377 forward, 8377 backward, and 6145 closed states.

The constant c = log(1+6.234×10^{-4}) − 5.0313×10^{-6} and exp(−4c) were computed in flint at precision 200. The crossover script was rerun with the sharp S_0 scaled by 1.001 (prime 3067), 1.002 (3079), 1.005 (3083) and 1.01 (3109).

## Non-claims

The run does not prove H1, H3, frozen R′, or BGS-BGS-001. It does not certify B_p > 0 at any prime. The primes 3067 and 1409 are conditional on H1 and on the idealised additive budgets. Shell 16 is the end of the span and alphabet census. The background factor is proved inside the point-insertion model only.

## Transfer operator (same day, later)

From `evidence/research/20261104_cloud/numerics/`:

```text
python3 transfer_24580.py
```

Python 3.12.3, numpy 1.26.4, scipy 1.18.1, python-flint 0.9.0, flint precision 128. Runtime about 110 s. The script rebuilds the 6145 closed carry states, forms the 24 580-vertex graph, and certifies Collatz–Wielandt bounds. A separate Kahn pass on the letters u ∈ {−1, 0, +1} eliminated all 24 580 vertices (`logs/dag_u01.json`). A strictly positive perturbation certifies ρ ≤ 0.25911138182 at uniform off-diagonal weight 0.003 (`logs/transfer_upper_0.003.json`).

The norm-majorant blocks were not the sesquilinear factors. Those were built separately, below.

## Phase-keeping carry boxes

`numerics/phase_carry.py` rebuilds the sector-4 blocks in binary64 and runs the N14/N15 carry map. Boxes E = 0, 1, 2, 4, 6, 8 (eight steps) and E = 10 (six steps). E = 1 and E = 4 match `g_carry_E1.json` and `g_carry_E4.json` to the printed digits. Peak resident memory at E = 10 was 4.4 GB. Logs: `numerics/logs/phase_carry_E*.json` and `phase_carry_summary.json`. Tag [N].

```text
e079cb4fc94b3a1d44ce6093b68ab4a4b3765d26b48560b55c30666b1b8d608f  numerics/transfer_24580.py
ca7967187136fc3ba8890127c9fe98e083ff0fc5b9f25ef722f92a55732e2292  numerics/logs/transfer_24580.json
31325ab6c1c6ab1d6cbe8b637bf27c3b5327a734efdbc367e25e78d9cd8cff25  numerics/logs/dag_u01.json
c05d29a7aac8b2f41b59dce347dc8d21ec028b548d31b1a48c2b02e1ec99c37d  numerics/logs/transfer_upper_0.003.json
```
