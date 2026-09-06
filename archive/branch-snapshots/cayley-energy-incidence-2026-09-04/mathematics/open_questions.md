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

## B. Prove a polynomial-scale mixed-term **energy** bound

The earlier formulation asked for a growing-`K` exceptional-prime cutoff. That
is now known to be the wrong closure condition.

For odd prime `K`, characteristic-zero Cayley collisions are completely
classified.  The cleared collision resultant has the exact form

`Res(Phi_K,P)=K^3 M^2`,

which improves the no-collision cutoff to

`K^3 p^2 > 12^(K-1)`.

However the explicit Fibonacci slice satisfies

`M=F_K`,

and therefore has exponentially large total norm.  More importantly, at

`K=131`, `p=F_131=1066340417491710595814572169`,

there is an exact non-forced collision even though `p` is enormous relative to
`K`.  The zero-excess strategy cannot be the primary growing-`K` mechanism.

The same example points to the right invariant: its collision energy is only

`33442 = 33410 + 32`,

and the underlying rational Fibonacci/Lucas model has forced-baseline excess
exactly `32` for every size.  Thus a large exceptional prime need not be a
large-energy obstruction.

**New closure condition:** prove a uniform or sufficiently averaged bound on

`sum_t C_H(t)^2`

for the Cayley image `A=c(H\{1})`, at a strength compatible with the fourth-
moment argument in the desired polynomial-scale regime.  The proof may use
incidence/sum-product methods, multiplicative-subgroup structure, arithmetic
classification of high-multiplicity differences, or a decomposition into
structured Lucas-type slices plus a pseudorandom remainder.  Exact elimination
of every non-forced collision is no longer required.

A useful next decision point is to determine the weakest exponent in an energy
bound that actually closes the mixed contribution after the factor
`2(p-2)C_H(t)` in `B(t)` is propagated through the variance identity.  This
must be derived explicitly before importing a generic additive-energy theorem.

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
