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

## B. Improve the proved pointwise mixed-energy exponent to the centered quadratic scale

The old question “eliminate every exceptional collision” is no longer the
right closure condition. The square-resultant/Fibonacci analysis shows that
very large exceptional split primes exist, while their total excess energy can
remain small.

### What is already closed

There is a uniform pointwise polynomial-scale theorem. For every odd prime
`p`, every subgroup `H<=F_p^*` of order

`100<K<p^(3/4)/3`,

and `A=c(H\{1})`,

`E_+(A)<34 K^(8/3)`,

`sum_t C_H(t)^2<34 K^(8/3)`,

and the mixed centered variance in the repository normalization is

`<136 p K^(8/3)`.

See [`cayley_direct_energy.md`](cayley_direct_energy.md).

For odd prime `K`, the exact resultant theorem also gives the global split-prime budget

`sum_{p==1 mod K} Delta_K(p) log p`

`<= (K^3-5K^2+6K+1)((K-1)log12-3logK)`,

where

`Delta_K(p)=sum_{d!=0}r_{A-A}(d)^2-(K-1)(2K-5)`.

See [`cayley_resultant_mass_budget.md`](cayley_resultant_mass_budget.md).

The previously open normalization step over a varying split-prime interval is
now also closed in a two-parameter dyadic average. For every fixed

`0<theta<1/3`,

let `D_theta(X)` consist of prime pairs

`K in (X^theta/2,X^theta]`,

`p in (X/2,X]`,

`p==1 mod K`.

Bombieri--Vinogradov plus the ordinary prime number theorem gives

`|D_theta(X)| ~ [log2/(2theta)] X/(log X)^2`,

and the resultant mass budget gives

`1/|D_theta(X)| sum_(K,p in D_theta(X)) Delta_K(p)/K^2`

`<<_theta X^(3theta-1) -> 0`.

Thus for every fixed `eta>0` the proportion of split pairs with
`Delta_K(p)>=eta K^2` tends to zero. In particular, for `theta<1/4` this is an
almost-all quadratic mixed-energy theorem strictly inside the intended
`K=o(p^(1/4))` regime. The result actually holds as a double average up to
`theta<1/3`.

The same theorem has an exact full-annihilator twisted-Jacobi formulation:

`1_Ahat(r)=K Tr M_S(2r)`.

Its nonzero-frequency trace second/fourth moment ratio tends to the
real-Gaussian value `3` in the same double average. This is not a CLT and not a
local eigenvalue-statistics statement.

See [`cayley_jacobi_trace_average.md`](cayley_jacobi_trace_average.md).

### The remaining sharp pointwise target

For every set `A subset F_p`,

`E_+(A)=|A|^4/p + 1/p sum_{q!=0}|1_Ahat(q)|^4`.

The density term is unavoidable. The sharp pointwise target is

`E_+(A)=(K-1)^4/p + O(K^(2+o(1)))`,

or equivalently

`sum_{q!=0}|1_Ahat(q)|^4 << p K^(2+o(1))`.

In the intended regime `K=o(p^(1/4))`, the density term is negligible at the
quadratic collision scale.

[`cayley_centered_energy.md`](cayley_centered_energy.md) gives the exact
character Gram matrix, torus-versus-unipotent PGL2 intersection formulation,
and shifted-product formulation. The new trace identity additionally identifies
the same Fourier transform with the ordinary trace of the full annihilator
Twisted-Jacobi matrix.

Generic pointwise Stepanov gives the current `8/3` exponent. The audited
Möbius-incidence and shifted-subgroup multiplicative-energy theorems do not, by
themselves, remove the remaining `K^(2/3)` pointwise loss. Termwise square-root
bounds on the trace functions also discard the joint character-family
cancellation required by the fourth moment.

**Pointwise closure condition:** prove the centered bound above, or any explicit
`K^(2+delta)` bound with `delta<2/3` that materially enlarges the pointwise
fourth-moment regime after complete propagation through `B(t)` and the variance
identity.

**Averaged continuation condition:** if a stronger average is pursued, specify
its averaging measure and parameters explicitly. The dyadic prime-pair average
above is already closed; do not silently relabel it as a pointwise theorem or
as an average over a fixed `K`.

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
