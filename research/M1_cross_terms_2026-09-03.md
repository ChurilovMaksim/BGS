# M1 cross-term audit — 2026-09-03

## Scope

This note starts the repaired M1 programme from the historical Möbius-fiber assembly, not from the invalid diagonal-only energy decomposition. The object audited here is the one stated in `paper/final/mobius_fiber_theorem.tex`:

`A_(psi1,psi2)(d) = sum_(u,v in C_d) psi1(u) psi2(v)`

with Möbius graph

`v(u) = (u(d-1)+1)/(d-u+1)`.

Define `F_tau = A_tau * A_tau` using cyclic convolution in `d`. Then the exact energy of the twist sum is

`E = ||sum_tau F_tau||_2^2 = sum_tau ||F_tau||_2^2 + sum_(tau != sigma) <F_tau,F_sigma>`.

The second term is load-bearing. It cannot be dropped without an orthogonality or cancellation theorem.

## First exact computational finding: cross terms are nonzero

Two independent implementations were run:

- Python/NumPy: `code/experiments/m1_cross_terms.py`;
- C++20 direct implementation: `code/cpp/m1_cross_terms.cpp`.

For `N=53, K=13, m=4`:

- diagonal raw energy: `934952569968`;
- cross raw energy: `7805905040`;
- cross / diagonal: `0.00834898506163491`;
- trivial ↔ nontrivial cross contribution: about `6.7164e9`;
- nontrivial ↔ nontrivial cross contribution: about `1.0895e9`.

For `N=199, K=11, m=18`:

- diagonal raw energy: about `1.163501213495166e16`;
- cross raw energy: about `3.17523876170438e14`;
- cross / diagonal: `0.0272903777398387`;
- trivial ↔ nontrivial cross contribution: about `1.75011861227666e14`;
- nontrivial ↔ nontrivial cross contribution: about `1.42512014942771e14`.

Python and C++ agree to floating-point precision. Therefore the historical diagonal-only energy identity is false for this implemented assembly.

## Second finding: the stated uniform Weil bound misses a degenerate fiber

The historical proof claimed that every nontrivial twist pair obeys

`|A_tau(d)| <= 4 sqrt(N)`

and that the rational function can be a perfect `K`-th power only for the fully trivial twist pair.

This is false as stated.

At `d=0`,

`v(u) = (1-u)/(1-u) = 1`

for every admissible `u != 1`. Hence for `psi1 = 1` and any nontrivial `psi2`,

`A_(1,psi2)(0) = sum_(u != 0,1) 1 = N-2`.

Numerically:

- at `N=53`, the maximum nontrivial `|A|` is exactly `51`, while `4 sqrt(53) ≈ 29.12`;
- at `N=199`, the maximum nontrivial `|A|` is exactly `197`, while `4 sqrt(199) ≈ 56.43`.

The violations occur precisely at `d=0` for pairs `(psi1=1, psi2 != 1)` in the two tested designs.

This is an algebraic degeneracy, not a numerical anomaly.

## Consequence for the proof architecture

A repaired M1 proof must not apply a generic rational-character-sum theorem before classifying the fibers. The next analytic decomposition should be:

1. derive the exact twist identity from the current character convention;
2. classify all exceptional `d` for which the Möbius map drops degree, becomes constant, or makes the combined character rational function a perfect power;
3. classify exceptional twist pairs for each exceptional fiber;
4. write the energy as diagonal + trivial/nontrivial cross + nontrivial/nontrivial cross;
5. isolate all exceptional-fiber contributions exactly;
6. only then apply Weil/Deligne-type bounds to the genuinely generic layer;
7. seek cancellation in the summed cross-Gram matrix rather than bounding every entry independently;
8. state the asymptotic regime in `(N,K,m)` before claiming any `o(1)` result.

## Immediate next mathematical targets

### M1-A — exact degeneracy classification

For the Möbius map

`v_d(u) = (u(d-1)+1)/(d-u+1)`,

classify all `d` where numerator/denominator share roots, the map is constant, or the divisor of `u^r v_d(u)^s` becomes divisible by the character order. This should produce a finite exceptional set plus explicit twist congruence conditions.

### M1-B — exact cross-Gram formula

Write

`G_(tau,sigma) = <A_tau*A_tau, A_sigma*A_sigma>`

in Fourier variables with one fixed normalization. The target is an exact character-sum representation suitable for algebraic-geometric cancellation, not a triangle-inequality bound on every entry.

### M1-C — scaling falsifiers

Extend the computation to more split-prime designs. For large `m`, use C++ and exploit FFT/character symmetries; do not attempt the `O(m^2 N^2)` Python construction blindly at `N=3571`.

## Status

`M1 = OPEN GAP`.

This cycle makes genuine progress by identifying a concrete exceptional fiber and quantifying the missing cross energy, but it does not yet establish the correct asymptotic estimate or the exact equivalence of the historical Möbius-fiber assembly with the full current `k=4` coupled-energy object.
