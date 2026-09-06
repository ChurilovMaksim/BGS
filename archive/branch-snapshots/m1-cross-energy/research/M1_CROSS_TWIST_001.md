# M1 cycle 001 — exact cross-twist assembly and singular-fiber split

Status: **ACTIVE / exact finite-N structure established; asymptotic M1 still OPEN**.

## 1. Why this cycle exists

The historical Möbius-fiber argument bounded individual nontrivial fiber sums and then treated the energy as though different twist pairs were orthogonal. They are not. The new computation reconstructs the object before applying any inequality and keeps every cross term.

The starting set is all ordered pairs

`x,y in F_N \ {0,1}`.

Define

`u = x/y`, `v = (x-1)/(y-1)`, `d = x-y`.

For `x != y`, the map to `(u,v,d)` is one-to-one and its inverse is

`y = (1-v)/(u-v)`, `x = u y`.

For `x=y`, all `N-2` choices collapse to the single key `(u,v,d)=(1,1,0)`. Therefore the correct key table is weighted: the singular key has multiplicity `N-2`; every regular key has multiplicity one. This is why the old note saying the pair-key map is globally injective is false even though its reported `V4` count was correct.

## 2. Exact quotient-coset formulation

Let `H=<a>` have order `K`, let `m=(N-1)/K`, and let `c(u) in Z/mZ` be the coset of `u` modulo `H`. Define the exact integer tensor

`W[c_u,c_v,d] = # {(x,y): key(x,y) has these cosets and difference d}`.

The subgroup constraints `u_1 u_2 in H`, `v_1 v_2 in H` are equivalent to

`c(u_2)=-c(u_1)`, `c(v_2)=-c(v_1)`.

Hence the count entering the coupled energy is exactly

`B(t) = sum_c (W_c * W_{-c})(t)`,

with cyclic convolution in `d`.

Taking the two-dimensional DFT in quotient-coset variables gives the annihilator characters `tau=(r,s)` and

`A_tau(d) = sum_c chi_tau(c) W_c(d)`.

Character orthogonality then gives the exact projector identity

`B(t) = m^{-2} sum_tau (A_tau * A_tau)(t)`.

This identity is now checked against the integer coset count by two independent implementations.

## 3. Cross terms are real and dense

Write `F_tau=A_tau*A_tau`. The exact energy is

`E = sum_t B(t)^2 = m^{-4} ||sum_tau F_tau||_2^2`.

Thus

`E = m^{-4} [sum_tau ||F_tau||_2^2 + sum_{tau != sigma} <F_tau,F_sigma>]`

with the appropriate Hermitian pairing when the real total is represented complexly. The second sum cannot be discarded.

Anchor results:

| N | K | m | historical/full delta vs trivial | cross fraction of full energy |
|---:|---:|---:|---:|---:|
| 53 | 13 | 4 | 0.0110502665 | 0.0097197205 |
| 199 | 11 | 18 | 0.0644657332 | 0.0600530579 |
| 461 | 23 | 20 | 0.0093650107 | 0.0092252431 |

At `N=53` every ordered off-diagonal Gram entry is non-negligible at the suite threshold. At `N=199` the Gram matrix is again dense; there is no exact twist-pair orthogonality hiding behind the historical decomposition.

The first two deltas reproduce the old `+1.1%` and `+6.4%` values, so this is the same object, not a replacement statistic.

## 4. The singular fiber was mixed into the old Weil discussion

Let `c=N-2` and split

`W = c delta_(0,0,0) + R`,

where `R` is the regular table (`d != 0`, equivalently `x != y`). Then there is an exact integer identity

`B = c^2 delta_0 + 2 c R_(0,0) + sum_q R_q * R_{-q}`.

It holds with zero integer error on every case in the current sweep.

The regular quotient-coset total masses are also elementary and exact:

- `(0,0)`: `(K-1)(K-2)`;
- one coset zero, or equal nonzero cosets: `K(K-1)`;
- distinct nonzero cosets: `K^2`.

In particular

`sum_d R_(0,0)(d) = (K-1)(K-2)`.

This is exactly the same `k=2` counting object already isolated in `K2Reduction.lean`. The M1 singular correction is therefore connected to an existing exact part of the programme rather than being an unrelated nuisance term.

For every quotient twist,

`A_tau(0)=N-2`.

So the historical statement that the nontrivial-twist fiber sums satisfy a `4 sqrt(N)` envelope on **all** fibers cannot be correct with the weighted key table. The old reported maxima `15` at `N=53` and `29` at `N=199` are reproduced exactly only after restricting to the regular fibers `d != 0`.

This does not disprove a regular-fiber Weil bound. It says the singular fiber must be split off before invoking one.

## 5. Regular character sum and the next analytic lemma

For `d != 0`, using `x=y+d`, the regular twist has the direct one-variable form

`A_{r,s}(d) = sum_y chi_r((y+d)/y) chi_s((y+d-1)/(y-1))`,

with the inadmissible points removed in the usual character-sum convention.

If `omega` generates the annihilator-character group of order `m`, this is the character of the rational function

`f_{r,s,d}(y) = (y+d)^r y^{-r} (y+d-1)^s (y-1)^{-s}`.

For generic `d`, the divisor is supported at four linear points. At `d=1` or `d=-1` two support points merge. The perfect-power exclusion must therefore be proved from the divisor valuations modulo the **order of the character** (a divisor of `m`), not by merely saying “not a K-th power.” That historical wording confuses the subgroup order `K` with the annihilator-character order.

The current 14-case sweep has

`max_{nontrivial tau, d!=0} |A_tau(d)| < 3 sqrt(N)`

in every sampled case, with observed maxima about `2.0 sqrt(N)` once N is moderate. This is only a falsifier result until the exact finite-field theorem and all exceptional-character cases are written carefully.

## 6. Raw energy has an exact scaling obstruction

Because `B(t)` is a nonnegative count and the diagonal-diagonal key pair contributes `(N-2)^2` at `t=0`,

`E = sum_t B(t)^2 >= (N-2)^4`.

Therefore a raw estimate of the form

`E = O(N^3 K^4)`

cannot hold uniformly unless the regime satisfies at least `K^4 = Omega(N)`, or unless the diagonal/singular contribution is removed by an exact centering step justified upstream in the trace-moment reduction.

This gives a clean fork for M1:

1. prove that the spectral fluctuation object is the **regular/centered** energy after the deterministic diagonal term is removed exactly; or
2. retain the raw energy and state/prove a growth regime strong enough to absorb the `(N-2)^4` lower bound.

No future M1 proof should hide this choice.

## 7. Correct order regime for the fixed trace-3 cat map

For a genuine trace-3 split prime, an eigenvalue `a` satisfies

`a + a^{-1} = 3 (mod N)`.

Let `L_0=2`, `L_1=3`, `L_{n+1}=3L_n-L_{n-1}`. Then

`L_n = a^n + a^{-n} (mod N)`.

If `ord_N(a)=K`, then `a^K=1`, hence

`N | (L_K-2)`.

For fixed `K`, `L_K-2` is a fixed nonzero integer, so only finitely many primes N can occur. Therefore along any infinite prime sequence for the fixed cat map,

`K(N) -> infinity`.

Writing `lambda=(3+sqrt(5))/2`, one also has `L_K-2 < lambda^K`, hence any such prime obeys the elementary logarithmic constraint

`K > log N / log lambda`.

The old phrase “K fixed, N -> infinity along the design scaling” is therefore not the correct asymptotic regime for the fixed trace-3 map. This observation does **not** rescue the old proof; it only fixes the regime that a new proof must use.

`N=53,a=10,K=13` is retained as a historical subgroup calibration, but `a=10` is not a root of `x^2-3x+1 mod 53`, so it must not be cited as a trace-3 split-prime example.

## 8. Reproducible evidence

The executable suite is

`python code/research/m1/run_suite.py`.

It compiles the independent C++17 implementation in a temporary directory. On anchors `N=53,199,461`, Python and C++ agree exactly on integer counts/energy and to floating precision on the character representation. The result is written to

`results/research/m1/cross_twist_suite.json`.

The sweep currently covers 14 subgroup designs through `N=1009`. It is a falsifier set, not an asymptotic dataset.

## 9. Next proof obligations

1. Write the key-table regular/singular decomposition as a general lemma independent of numerical designs.
2. Connect the singular term to the already exact `k=2` reduction and determine whether the spectral observable centers it away.
3. Prove the quotient-character projector identity with fixed Fourier normalization.
4. Classify the divisor of `f_{r,s,d}` for `d != 0`, including `d=±1` and characters with one trivial coordinate.
5. Apply the correct multiplicative-character theorem only after the order/perfect-power hypotheses are checked.
6. Bound the **assembled** regular quadratic energy, not the sum of isolated twist energies.
7. Reproduce the large `N=3571,K=17,m=210` case with a memory-aware implementation and use it as a stress test, not as proof.

Promotion rule remains unchanged: M1 stays `OPEN GAP` until the assembled remainder is proved to vanish in a valid arithmetic regime.
