# Open mathematical obligations

Only unresolved obligations belong here. Superseded proof attempts and false
historical statements belong in
[`../record/retractions.md`](../record/retractions.md).

## A. Complete the off/off elliptic correlation theorem

Close every obligation listed in
[`elliptic_pencil.md`](elliptic_pencil.md) for the actual family: projective
model, discriminant, bad fibers, twists/isogenies, sheaf irreducibility and
conductor, affine boundary, and the exact hypotheses of the chosen correlation
theorem.

**Closure condition:** a theorem with explicit `(p,K)` hypotheses and a
uniform proved error bound; no CAS-only or unnamed “Katz-style” step.

## B. Improve the proved direct mixed-energy exponent to the centered quadratic scale

The old question “eliminate every exceptional collision” is no longer the
right closure condition. The square-resultant/Fibonacci analysis shows that
very large exceptional split primes exist, while their total excess energy can
remain small.

### What is already closed

There is now a genuine uniform polynomial-scale theorem. For every odd prime
`p`, every subgroup `H<=F_p^*` of order

`100<K<p^(3/4)/3`,

and `A=c(H\{1})`, the bilinear-fiber argument in
[`cayley_direct_energy.md`](cayley_direct_energy.md) gives

`E_+(A)<34 K^(8/3)`

and hence

`sum_t C_H(t)^2<34 K^(8/3)`.

After the exact coefficient `2(p-2)` is propagated through the repository
variance normalization, the mixed centered variance is

`<136 p K^(8/3)`.

So a pointwise polynomial-scale mixed theorem is **proved**; the remaining
pointwise issue is the exponent gap.

There is also a new exact prime-averaged arithmetic theorem for odd prime `K`.
If

`Delta_K(p)=sum_{d!=0}r_{A-A}(d)^2-(K-1)(2K-5)`

for split primes `p==1 mod K`, then

`sum_{p==1 mod K} Delta_K(p) log p`

is at most

`(K^3-5K^2+6K+1)((K-1)log12-3logK)`.

See [`cayley_resultant_mass_budget.md`](cayley_resultant_mass_budget.md).
This gives a deterministic `O(K^4)` budget for the total non-forced collision
mass over **all** split primes and corresponding tail/sparsity bounds. It is a
real averaged result, but it is not yet a normalized average in a prescribed
`p`-interval; such a statement needs an independent lower bound for the number
of split primes in that interval.

### The remaining sharp target

For every set `A subset F_p`,

`E_+(A)=|A|^4/p + 1/p sum_{q!=0}|1_Ahat(q)|^4`.

Thus a global raw bound `E_+(A)=O(K^2)` is not the correct statement in dense
regimes. The sharp pointwise target is

`E_+(A)=(K-1)^4/p + O(K^(2+o(1)))`,

or equivalently

`sum_{q!=0}|1_Ahat(q)|^4 << p K^(2+o(1))`.

In the intended regime `K=o(p^(1/4))`, the density term is negligible at the
quadratic collision scale.

[`cayley_centered_energy.md`](cayley_centered_energy.md) gives two exact
reformulations exposing the highest-value routes:

1. a character decomposition
   `1_Ahat(q)=e_p(q)/|H^perp| * sum_chi T_chi(q)` with an exactly computed Gram
   matrix for the `T_chi` family;
2. a torus-versus-unipotent PGL2 intersection formulation, equivalently a
   moving distinguished-product class in shifted subgroups `H+lambda`.

Generic pointwise Stepanov gives the current `8/3` exponent. The audited
Möbius-incidence and shifted-subgroup multiplicative-energy theorems do not, by
themselves, sum the moving distinguished classes with only quadratic loss.
Termwise square-root bounds on the trace functions also discard the joint
character-family cancellation required by the fourth moment.

**Pointwise closure condition:** prove the centered bound above, or any explicit
`K^(2+delta)` bound with `delta<2/3` that materially enlarges the fourth-moment
regime after complete propagation through `B(t)` and the variance identity.

**Prime-averaged closure condition:** combine the exact resultant mass budget
with a source-exact lower bound for split primes in the relevant varying-modulus
interval and show that the resulting normalized average is strong enough for
the intended averaged moment statement. Do not assume a prime number theorem
in arithmetic progressions in a range where its uniformity is unavailable.

## C. Re-audit global symmetry statements if they become load-bearing

The finite/operator identities in
[`earlier_foundations.md`](earlier_foundations.md) are useful, but a complete
blockwise symmetry-class theorem should be re-derived with every kernel chart,
desymmetrization convention and antiunitary action stated explicitly if it is
needed in a future local-statistics argument.

**Closure condition:** one convention-consistent theorem covering exactly the
spectral blocks used in the BGS statement.

## D. Build the microscopic BGS bridge

Even a completed moment estimate does not imply microscopic GOE spacing.

**Closure condition:** identify and verify a theorem or new argument that
transfers the available arithmetic information to a local eigenphase
correlation law for this structured deterministic family at the mean-spacing
scale, with all symmetry and uniformity assumptions explicit.

## Engineering status

The historical Julia migration is complete: the current branch tracks no
`.jl` sources, and all 31 historical paths have a final disposition in
[`../record/julia_migration.md`](../record/julia_migration.md). Language
migration is therefore **not** an open mathematical task. Future language
choices are driven by the scientific kernel: Python/SymPy for transparent CAS
and orchestration, C++20 for exact/exhaustive hot paths including arbitrary-
precision certificates, Lean for kernel-checked finite residues and algebraic
lemmas, and TeX for the publication-facing proof record.
