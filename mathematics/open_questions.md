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
right closure condition.  The square-resultant/Fibonacci analysis shows that
very large exceptional split primes exist, while their total excess energy can
remain small.

There is now a genuine uniform polynomial-scale theorem.  For every odd prime
`p`, every subgroup `H<=F_p^*` of order

`100<K<p^(3/4)/3`,

and `A=c(H\{1})`, the bilinear-fiber argument in
[`cayley_direct_energy.md`](cayley_direct_energy.md) gives

`E_+(A)<34 K^(8/3)`

and hence

`sum_t C_H(t)^2<34 K^(8/3)`.

After the exact coefficient `2(p-2)` is propagated through the repository
variance normalization, the mixed centered variance is bounded by

`<136 p K^(8/3)`.

So a polynomial-scale mixed theorem is **proved**; what remains is the exponent
gap.

For every set `A subset F_p`, however,

`E_+(A)=|A|^4/p + 1/p sum_{q!=0}|1_Ahat(q)|^4`.

Thus a global raw bound `E_+(A)=O(K^2)` is not even the correct statement in
dense regimes.  The sharp target is the centered estimate

`E_+(A)=(K-1)^4/p + O(K^(2+o(1)))`,

or equivalently

`sum_{q!=0}|1_Ahat(q)|^4 << p K^(2+o(1))`.

In the intended regime `K=o(p^(1/4))`, the density term is negligible at the
quadratic collision scale, so this is the natural mixed-term closure.

[`cayley_centered_energy.md`](cayley_centered_energy.md) gives two exact
reformulations which currently expose the highest-value routes:

1. a character decomposition
   `1_Ahat(q)=e_p(q)/|H^perp| * sum_chi T_chi(q)` with an exactly computed Gram
   matrix for the `T_chi` family;
2. a torus-versus-unipotent PGL2 intersection formulation, equivalently a
   moving distinguished-product class in shifted subgroups `H+lambda`.

Generic pointwise Stepanov gives the current `8/3` exponent.  The audited
Möbius-incidence and shifted-subgroup multiplicative-energy theorems do not, by
themselves, sum the moving distinguished classes with only quadratic loss.
Likewise, termwise square-root bounds on the trace functions discard the
character-family cancellation required by the fourth moment.

**Closure condition:** prove the centered bound above, or any explicit
`K^(2+delta)` bound with `delta<2/3` that materially enlarges the fourth-moment
regime after complete propagation through `B(t)` and the variance identity.

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
