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

## B. Determine the useful growth regime in K

The current fixed-`K` mixed-term result does not control the number or size of
cyclotomic bad primes uniformly in `K`, and `(461,23)` is an explicit warning
against naive extrapolation.

**Closure condition:** either a rigorous growing-`K` exceptional-prime
bound/average theorem, or a proof that the intended moment regime can avoid
needing such a uniform statement.

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
migration is therefore **not** an open mathematical task. Any future
C++/Fortran/Python change should be justified by a current scientific need or
profiling result, not by repository language percentages.
