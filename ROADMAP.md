# Research roadmap

The ambition is to produce work that can survive expert scrutiny at the highest level of mathematical physics.  That is a quality standard, not a promise of a prize or of a predetermined theorem.

## Track A — exact arithmetic reduction

1. Keep one character convention and one Fourier normalization.
2. Prove the general even-moment factorization in written mathematics and then formalize its finite/combinatorial core in Lean.
3. Recheck the best late-archive finite identities (`k=4`, selected rank-2 statements) with independent Python/C++ implementations before promotion.

## Track B — M1: the load-bearing asymptotic estimate

1. Derive the exact ordered twist-pair assembly from the current Jacobi convention.
2. Classify generic and degenerate Möbius fibers, including semi-trivial twists.
3. Derive the exact cross-Gram matrix rather than summing per-twist energies.
4. Use finite-field character-sum bounds only after divisor/perfect-power hypotheses are proved.
5. Identify cancellation at the summed Gram-matrix level.
6. State a precise scaling regime and prove a vanishing remainder.
7. Use `N=53,199,3571` and larger split primes as falsifiers, never as substitutes for proof.

## Track C — local spectral statistics

1. Cleanly rerun the archived layer-scaling and Stieltjes experiments.
2. Separate finite-size surface terms from genuine asymptotic decay using designs that vary `K` and `N` independently as far as the arithmetic permits.
3. Replace informal “ESY-style” analogies with an exact theorem statement whose hypotheses can be checked for this deterministic arithmetic ensemble.
4. Only after the required local-law hypotheses are proved, connect them to spacing/rigidity observables.

## Track D — rank 2 / general mechanism

Rebuild the Sp4 experiment from definitions, not from old projector code.  First certify the representation and basis conventions, then the diagonal identities, then a genuinely non-diagonal kernel.  The archived `archive/legacy-workspace/data/rank2_sp4` directory is evidence-generating archaeology, not an active theorem set.

## Track E — reproducibility and formalization

- Python is the transparent reference implementation.
- C++20 is used for independent/high-throughput checks and is always committed as source.
- Lean is used for exact finite/combinatorial statements and later general lemmas.  Unbuilt Lean is labelled as such.
- Julia is not a required dependency; useful old Julia experiments are preserved in the archive and reimplemented in Python/C++ when needed.
- Every promoted result records its producer, parameters, status and independent cross-check where practical.
