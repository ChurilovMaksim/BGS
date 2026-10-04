# Research route log

## 2026-10-04 — Uniform derivatives close the random-chain polynomial regime

The [research and proof review](polynomial_coboundary_review_20261004.md)
records the frozen full BGS target and three routes. A direct fixed-time
extension and an arbitrary-analytic orbit truncation supply no missing
uniform estimate. The random-chain route yields FLOW-011: dimension-uniform
coefficient derivatives, positive microscopic Laplace test norm $C_fN^6$,
and exactly $2N^{34}$ original steps at error $O_f(N^{-1/3})$.
FLOW-010's slow-time polynomial corollary also repairs its earlier
scope statement. Heisenberg signed traces and deterministic noise removal
remain the explicit continuation targets; no full BGS proof is claimed.

## 2026-10-01 — Density-controlled resonant deletion and critical clusters

The [review](resonant_density_review_20261001.md) closes the generic
three-strip cubic question under local density control, with budget
$C_W\sqrt{E_N M_4(N)}$. Realizable rare clusters refute the critical
bounded-third-moment strengthening, even after every signed CUE pair
test is preserved. The actual block mass and density hypotheses remain
open; the fixed map and complete goal are unchanged.

## 2026-09-30 — Excluding the unaveraged absolute route; retaining the signed cubic

The [continuation](signed_heisenberg_review_20260930.md) proves the
universal pair-to-higher absolute-norm obstruction (TRACE-010). Exact CUE
variance calibrates a signed joint-resonant test. A formal quadratic-phase
mechanism cancels on positive cones but fails moment positivity at N=3.
The next actual-map target is the signed factorial cubic, with its exact
counterterms and all three resonant strips. That estimate remains open.

This file records only substantive bounded research routes that materially changed the current theorem set or identified a durable obstruction. It is not a command transcript. Current claim status remains authoritative in [`claim_ledger.md`](claim_ledger.md).

## 2026-09-04 — Direct and resultant control of the mixed Cayley term

**Target.** Replace the failed strategy “exclude every non-forced Cayley collision at polynomial scale” by a quantitative energy theorem strong enough to propagate through the exact fourth-moment variance identity.

**Pointwise route — proved.** For `A=c(H\{1})`, the sum fiber `c(x)+c(y)=t` is

`(2-t)xy+t(x+y)-(2+t)=0`.

Its bilinear determinant is `-4`, so it is absolutely irreducible in odd characteristic. After checking the exact hypotheses of Vyugin--Makarychev Theorem 2 in the primary arXiv PDF, the subgroup-curve estimate gives

`E_+(A)<34K^(8/3)`

for `100<K<p^(3/4)/3`, hence mixed centered variance `<136 p K^(8/3)` in the repository normalization. An independent C++20 verifier checks five finite designs.

**Centered reformulation — exact, pointwise target open.** Parseval shows the unavoidable density term

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

**Remaining pointwise gap.** `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` remains open.

## 2026-09-04 — Full Jacobi trace and double-averaged quadratic mixed energy

**Target.** Determine whether the centered Cayley fourth moment is already encoded in the maintained twisted-Jacobi operator and whether the global resultant mass budget can be normalized over a genuine varying split-prime family without assuming a pointwise prime number theorem in arithmetic progressions.

**Trace identity — proved.** For the full annihilator matrix

`J_S(q)_(chi,psi)=sum_x chi^(-1)(x) psi(x-1)e_p(qx)`

and normalized

`M_S(q)=e_p(-q/2)J_S(q)/(p-1)`,

a direct diagonal calculation gives

`1_Ahat(r)=K Tr M_S(2r)`.

Hence

`sum_q|Tr M_S(q)|^2=p(K-1)/K^2`,

`sum_q|Tr M_S(q)|^4=pE_+(A)/K^4`.

This is an ordinary trace identity. It uses no cyclic rewrite of noncommutative matrix words and does not revive the retracted historical R86/R87 trace shortcut. A finite complex128 regression compares the maintained Jacobi implementation against an independent direct Cayley Fourier transform at `(53,13)`, `(199,11)` and sampled `(461,23)`; it is explicitly not the proof.

**Dyadic normalization — proved.** Fix `0<theta<1/3`, put `Q=X^theta`, and average over prime pairs

`Q/2<K<=Q`, `X/2<p<=X`, `p==1 mod K`.

Bombieri--Vinogradov, used only after summing over the varying prime moduli `K`, gives

`|D_theta(X)| ~ [log2/(2theta)]X/(logX)^2`.

Combining this with the exact global resultant budget gives

`average_(K,p) Delta_K(p)/K^2 <<_theta X^(3theta-1) -> 0`.

Therefore for every fixed `eta>0`, the proportion of split pairs with `Delta_K(p)>=eta K^2` tends to zero. The theorem holds in the larger double-average range `theta<1/3`; the BGS-moment subrange `theta<1/4` is contained in it.

**Trace fourth-moment consequence — proved with narrow semantics.** The exact nonzero-frequency kurtosis `kappa=mu4/mu2^2` satisfies

`|kappa-3| << Delta_K(p)/K^2 + 1/K + K^2/p`.

Thus its double-average absolute deviation from `3` tends to zero. This is only a real-Gaussian second/fourth moment ratio for the **ordinary full trace**. It is not a CLT, not a parity/desymmetrized-block theorem, and not microscopic BGS.

**External inputs.** The varying-modulus denominator uses the classical Bombieri--Vinogradov theorem in the standard Iwaniec--Kowalski Theorem 17.1 range and the ordinary prime number theorem. The fixed `theta<1/2` dyadic moduli lie inside the Bombieri--Vinogradov modulus range at both endpoints `X` and `X/2`; the energy theorem then imposes the stricter threshold `theta<1/3`.

**Remaining gap.** The pointwise centered `K^(2+o(1))` theorem remains open. Any future averaged statement must specify a different averaging measure explicitly rather than silently upgrading this dyadic pair-density result.
