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
remain small. The inverse structural-associate theorem strengthens this
warning: for every sufficiently large prime conductor there are explicit
characteristic-zero associate edge pairs whose simultaneous reduction is
forced at every prime ideal dividing one common principal ideal.

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

The **intended pointwise regime is explicitly**

`K=o(p^(1/4))`.

In this regime the density term is negligible at the quadratic collision
scale. Statements about all split primes, including `p=O(K)`, are stronger
than the actual closure condition and must not be silently substituted for it.

[`cayley_centered_energy.md`](cayley_centered_energy.md) gives the exact
character Gram matrix, torus-versus-unipotent PGL2 intersection formulation,
and shifted-product formulation. The trace identity additionally identifies
the same Fourier transform with the ordinary trace of the full annihilator
Twisted-Jacobi matrix.

Generic pointwise Stepanov gives the current `8/3` exponent. The audited
Möbius-incidence and shifted-subgroup multiplicative-energy theorems do not, by
themselves, remove the remaining `K^(2/3)` pointwise loss. Termwise square-root
bounds on the trace functions also discard the joint character-family
cancellation required by the fourth moment.

### New inverse-row quotient route

The exact fixed-product-row inequality is

`Delta_K(p)<=4 I_K(p)(K-1)(K-2)`.

Hence one does not need to prove `I_K<=2`. In the intended regime it is enough
to prove

`I_K(p)=K^o(1)`,

and `I_K(p)=O(1)` would already give a genuinely quadratic row contribution.

For the inverse ratio there is now a sharper exact reduction. With

`w_(a,b)=2-v_a-v_b`, `v_n=(t_n-2)/(tau-2)`,

define characteristic-zero edge association by

`e~f iff w_e/w_f is a unit of Z[tau]`.

Discard unit edges and let `B_K` be the largest remaining associate-class
size. For nonassociate edges define

`(w_e,w_f) cap Z = D_(K;e,f) Z`.

Then for a split embedding prime `q|p`, if `p` divides no cross-class
`D_(K;e,f)`, every zero edge at `q` lies in one associate class and

`I_-1(q)<=2 B_K`.

See [`cayley_inverse_associate_quotient.md`](cayley_inverse_associate_quotient.md).

This splits the inverse closure into two materially different tasks:

1. **Characteristic-zero class size:** prove `B_K=K^o(1)`, ideally `O(1)`.
2. **Cross-class arithmetic:** in the intended `K=o(p^(1/4))` regime, exclude
   `p` from the split divisors of every `D_(K;e,f)` with `e!~f`; a sufficient
   form is a largest-split-divisor bound `K^(4+o(1))` for the product of these
   cross-class contractions.

This is strictly weaker than bounding the largest divisor of the full inverse
order-three support, because the universal structural associate classes are
removed before the cross-class problem is formed.

The range restriction is load-bearing. Direct exact finite controls include

`K=83, p=167=2K+1: I_-1=14`,

`K=89, p=179=2K+1: I_-1=16`.

Thus a global `I_-1=O(1)` assertion over **all** split primes is not an active
hypothesis. Those examples lie far outside `K=o(p^(1/4))`. Conversely the
large-prime structural controls

`K=139, p=3596704231>K^4: I_-1=4`,

`K=229, p=966684838398077>>K^4: I_-1=4`

show why bounded structural multiplicity, rather than absence of order-three
support, is the correct compatible target.

Finite data also contain genuine nonassociate same-embedding events, for
example

`K=59, p=21713`,

where exact ideal contraction gives

`(w_(8,26),w_(9,10)) cap Z = 21713 Z`.

This calibrates the cross-class problem: it is nonempty and must be bounded,
not wished away. Current finite data suggest many nonassociate factors lie on
an `O(K^2)` scale, but **no exponent-two theorem is claimed**.

The inverse quotient route is not yet a solution of the general row problem.
One must either obtain analogous multiplicity control for every normalized
ratio class or prove a theorem reducing the worst ratio to the inverse class.

**Pointwise closure condition:** prove the centered bound above, or any explicit
`K^(2+delta)` bound with `delta<2/3` that materially enlarges the pointwise
fourth-moment regime after complete propagation through `B(t)` and the variance
identity. For the row route, a sufficient intermediate theorem is uniform
`I_K(p)=K^o(1)` in the explicit regime `K=o(p^(1/4))`.

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

The deterministic Fourier bridge is now exact: band-limited microscopic
factorial statistics are weighted sums of joint traces at powers
`|m|=Theta(N)`. What remains is not the Fourier conversion but the arithmetic /
spectral estimate on the correct desymmetrized block, followed by uniform
high-frequency tail control for arbitrary Schwartz tests.

**Closure condition:** prove a weighted Heisenberg-scale joint-trace comparison
with the target RMT ensemble for the actual desymmetrized block, with all
symmetry and uniformity assumptions explicit, and control the Fourier tail
needed to remove the band limit. Only then can one promote a microscopic
BGS/GOE/COE local eigenphase law.

## Engineering status

The historical Julia migration is complete: the current branch tracks no
`.jl` sources, and all 31 historical paths have a final disposition in
[`../record/julia_migration.md`](../record/julia_migration.md). Language
migration is therefore **not** an open mathematical task. Future language
choices are driven by the scientific kernel: Python/SymPy for transparent CAS
and orchestration, C++20 for exact/exhaustive hot paths including arbitrary-
precision certificates, Lean for kernel-checked finite residues and algebraic
lemmas, and TeX for the publication-facing proof record.
