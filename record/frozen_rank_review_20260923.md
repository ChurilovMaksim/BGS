# Self-review of the frozen-kick rank boundary

Base: `c56c9db3f985872206501e1545678da940dad89c`, 23 September 2026.
Claim `BGS-FM-005`, source `mathematics/frozen_kick_rank_boundary.md`.
Verdict: correct conditional on the classical Hermite–Lindemann theorem in
the exact form checked below. This is a self-review, not a fresh independent
referee report or a priority assessment.

1. In the raw modular Weyl convention the only `p` harmonics shift by one.
   Their coefficient has magnitude `r((x+2^{-1})/N)/200`; the exact zero
   condition is `7(x+2^{-1})=0 mod N`. The other factor of `r` cannot vanish
   at an odd-grid point. Therefore there are exactly `gcd(N,7)` broken bonds,
   equally spaced; each component is a path of length `N/gcd(N,7)`.
2. Every internal Jacobi bond is nonzero. The recurrence of an eigenvector
   from its first coordinate shows each block has simple spectrum; repeated
   eigenvalues across different blocks can occur at most `gcd(N,7)` times.
   The edge case `N=7` has seven one-dimensional components and `A_7=0.9 I`.
3. The entries of `A_N` and its eigenvalues are algebraic. Evertse's
   [*Transcendence results*, Theorem 4.8](https://pub.math.leidenuniv.nl/~evertsejh/dio15-4.pdf)
   gives, with distinct exponents `0` and `i tau N(lambda-mu)` and algebraic
   coefficients `-1,1`, that `exp(i tau N lambda) != exp(i tau N mu)` for
   distinct eigenvalues when nonzero `tau` is algebraic. This exact-source
   implication is valid; it gives no lower bound on their separation.
   Unitary right multiplication by `M_N` preserves rank.
4. For odd `N>=19`, the `q` Fourier radius at most 9 and `p` radius 1
   exclude nonzero aliases in the *square*, yielding `Tr A_N=0` and
   `Tr A_N²/N=66033/160000`. Row sums bound `||A_N||<=79/50`.
   If `|tau N|(79/50)<=pi`, the elementary sine bound and the sum of
   squares left after removing at most `r` singular directions give exactly
   the stated Hilbert–Schmidt inequality. The hypothesis ceases to hold
   eventually at the prescribed fixed `tau=10^-80`; no fixed-strength
   asymptotic approximation conclusion follows.

The finite `computations/verification/frozen_kick_rank.py` independently
compares Fourier and Jacobi assembly in 12 odd dimensions and samples 28
best-rank bounds at moderate `t=0.4`; floating arithmetic neither proves
algebraic noncollision nor the all-`N` statement. The single-chain case for
coprime dimensions was already in
`supplement/fixed_map/weighted-secular/attempt.md`; the rank formulation
uses that known structure. This result does not control mixed quantum traces,
principal-minor weights, approximate rank beyond the pre-wrap range, or BGS.
