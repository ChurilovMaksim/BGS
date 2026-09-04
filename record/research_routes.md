# Research route log

This file records only substantive bounded research routes that materially changed the current theorem set or identified a durable obstruction. It is not a command transcript. Current claim status remains authoritative in [`claim_ledger.md`](claim_ledger.md).

## 2026-09-04 — Direct and averaged control of the mixed Cayley term

**Target.** Replace the failed strategy “exclude every non-forced Cayley collision at polynomial scale” by a quantitative energy theorem strong enough to propagate through the exact fourth-moment variance identity.

**Pointwise route — proved.** For `A=c(H\{1})`, the sum fiber `c(x)+c(y)=t` is

`(2-t)xy+t(x+y)-(2+t)=0`.

Its bilinear determinant is `-4`, so it is absolutely irreducible in odd characteristic. After checking the exact hypotheses of Vyugin--Makarychev Theorem 2 in the primary arXiv PDF, the subgroup-curve estimate gives

`E_+(A)<34K^(8/3)`

for `100<K<p^(3/4)/3`, hence mixed centered variance `<136 p K^(8/3)` in the repository normalization. An independent C++20 verifier checks five finite designs.

**Centered reformulation — exact, target open.** Parseval shows the unavoidable density term

`E_+(A)=|A|^4/p + p^(-1) sum_{q!=0}|1_Ahat(q)|^4`.

Thus the sharp pointwise target is the nonzero Fourier fourth moment `<<pK^(2+o(1))`, not a raw global `O(K^2)` energy statement. The exact annihilator-character decomposition, Gram matrix, conjugated-unipotent PGL2 family, and shifted-product formulation are recorded in `../mathematics/cayley_centered_energy.md`.

**Resultant-mass route — proved average/sparsity theorem.** For odd prime `K`, simultaneous exponent scaling partitions non-forced collision quadruples into

`N_K=K^3-5K^2+6K+1`

Galois orbits. For one normalized orbit, the number of scaled collisions at a split prime is at most the `p`-adic valuation of its resultant. Combining this with

`Res(Phi_K,P)=K^3 M^2`

and `|Res(Phi_K,P)|<=12^(K-1)` gives

`sum_{p==1 mod K} Delta_K(p) log p`
`<=N_K((K-1)log12-3logK)`.

The complete `K=11,13` regression verifies the orbit/common-root/valuation mechanism and the exact integer product form of the bound.

**Discarded shortcuts.** Generic Möbius rich-transform estimates, generic rational-function energy decompositions, and near-quadratic total multiplicative energy of shifted subgroups do not, in their checked forms, control the moving distinguished product class with only quadratic loss. Termwise Weil bounds on the Fourier trace functions also discard the joint character-family cancellation needed for the fourth moment.

**Remaining gap.** Pointwise centered energy `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` remains open. A prime-averaged continuation additionally needs a source-exact lower bound for split primes in the relevant varying-modulus interval; no unsupported prime-number-theorem-in-progressions uniformity is assumed.
