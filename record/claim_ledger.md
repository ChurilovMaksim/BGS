# Claim ledger

This file is the repository-wide status authority.  Historical commits, old
manuscript text and exploratory notes may contain stronger claims; this file
wins.

## Status vocabulary

- **EXACT** — current project derivation with explicit hypotheses.
- **EXACT + EXTERNAL-THEOREM** — exact project reduction whose remaining named
  input is a verified published theorem with its hypotheses checked in project
  notation.
- **FINITE-CERTIFICATE** — exact exhaustive or kernel-checked statement at
  explicit finite parameters.
- **FINITE-REGRESSION** — finite implementation/reference agreement; useful
  for reproducibility, not a universal proof.
- **NUMERICAL** — descriptive floating-point evidence only.
- **DRAFT** — proof route with named unresolved obligations.
- **OPEN** — closure condition not achieved.
- **SCOPED-HISTORICAL** — useful earlier result whose safe present scope is
  narrower than its historical label.
- **NOT-PROMOTED** — retained evidence/conjectural structure, not accepted into
  the current theorem set.
- **RETRACTED** — false or superseded.

## Active claim table

| Claim | Status | Current support |
|---|---|---|
| pair-key bijection; diagonal multiplicity `p-2` | **EXACT** | `mathematics/fourth_moment_reduction.md` |
| constrained off-diagonal count `(K-1)(K-2)` | **EXACT + FINITE-CERTIFICATE** | pair-key proof; Lean finite certificate |
| exact `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE-CERTIFICATE** | current derivation + Python/C++/Lean finite checks |
| corrected `B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}` and Fourier mean/variance | **EXACT + FINITE-REGRESSION** | `fourth_moment_reduction.md` |
| Cayley identity and additive-energy reduction | **EXACT** | `cayley_additive_energy.md` |
| odd-prime-order characteristic-zero additive collision rigidity | **EXACT** | Chowla cotangent independence + cross-polytope argument |
| `Res(Phi_K,P)=K^3M^2` | **EXACT + FINITE-REGRESSION** | `cayley_resultant_structure.md` |
| `K^3p^2>12^(K-1)` implies exact nonzero Cayley baseline | **EXACT + FINITE-REGRESSION** | square resultant + coefficient norm |
| Fibonacci slice `Res(Phi_K,X^2+3X+1)=F_K^2` | **EXACT + FINITE-REGRESSION** | exact Binet/Lucas derivation |
| `S_N={+-L_n/F_n}` has nonzero difference energy `2N(4N-3)+32` for `N>=3` | **EXACT + FINITE-CERTIFICATE** | `fibonacci_ratio_energy_proof.md`; external primitive-divisor theorem + bounded Lean residue |
| `(K,p)=(131,F_131)` has energy `33442`, baseline `33410`, excess `32` | **FINITE-CERTIFICATE** | Lucas primality certificate + independent Python/C++ multiprecision checks |
| for `100<K<p^(3/4)/3`, `E_+(c(H\{1}))<34K^(8/3)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `cayley_direct_energy.md`; Vyugin--Makarychev Theorem 2 |
| corresponding mixed centered variance `<136pK^(8/3)` | **EXACT** | direct theorem + exact coefficient `2(p-2)` |
| centered Fourier identity and Cayley character/Gram formulations | **EXACT** | `cayley_centered_energy.md` |
| shifted-energy orbit inequality `sum_{t in T_(lambda H)}r(t)^2<=2(E_x(H+lambda)-(2K^2-K))` | **EXACT + FINITE-REGRESSION** | `cayley_shifted_energy_orbits.md`; CI regression |
| for `K^2<p`, every nonzero parameter orbit has `L^2` mass `<<K^2 log K` | **EXACT + EXTERNAL-THEOREM** | preceding reduction + Shkredov, arXiv:1504.04522v1, Theorem 6 |
| global shifted-energy identity `sum_lambda(E_x(H+lambda)-(2K^2-K))=K^4-E_+(H)` | **EXACT + FINITE-REGRESSION** | `cayley_shifted_energy_orbits.md`; full finite lambda-sums at `(199,11)`, `(461,23)` |
| shifted-energy orbit route alone yields only global `O(K^3)` and does not improve `K^(8/3)` | **EXACT LIMITATION** | exact global identity + orbit partition |
| weighted split-prime excess budget `sum_{p==1 mod K}Delta_K(p)log p <= (K^3-5K^2+6K+1)((K-1)log12-3logK)` | **EXACT + FINITE-REGRESSION** | `cayley_resultant_mass_budget.md` |
| canonical difference discriminant: `Delta_K(p)>0 iff p|Disc(S_K)` and `Delta_K(p)<=4v_p(Disc(S_K))` | **EXACT + FINITE-REGRESSION** | `cayley_difference_discriminant.md` |
| ratio-orbit factorization and one-factor fourth-power discriminants | **EXACT + FINITE-REGRESSION** | `cayley_ratio_orbit_factorization.md` |
| global `|Disc(S_K)|=2^((K-1)^4/4)K^((K-1)(K^2-7)/4)J_K^4` | **EXACT + FINITE-REGRESSION** | ratio-orbit theorem + product-discriminant identity |
| characteristic-zero multiplicative Cayley rigidity; `E_x(A_K)=4(K-1)(K-2)` | **EXACT + FINITE-REGRESSION** | `cayley_multiplicative_rigidity.md` |
| canonical product discriminant classification and `Delta_K^x(p)<=16v_p(Disc(S_K^x))` | **EXACT + FINITE-REGRESSION** | `cayley_product_discriminant.md` |
| full ordinary Jacobi trace `1_Ahat(r)=K Tr M_S(2r)` and exact second/fourth trace moments | **EXACT + FINITE-REGRESSION** | `cayley_jacobi_trace_average.md` |
| for fixed `0<theta<1/3`, double-average `Delta_K(p)/K^2<<_theta X^(3theta-1)` | **EXACT + EXTERNAL-THEOREM** | mass budget + Bombieri--Vinogradov + PNT |
| full normalized ordinary Jacobi-trace kurtosis tends to `3` in the same double average | **EXACT** | exact trace moments + preceding theorem; not a CLT |
| for fixed `0<theta<1/5`, density-one split pairs satisfy `Delta_K(p)=0` exactly | **EXACT + EXTERNAL-THEOREM** | `cayley_exact_baseline_density.md` |
| generic off/off reducible spike `O_lambda(2/(alpha-beta))=2p-8`; remaining singular support recovers parameters up to involution | **EXACT + FINITE-REGRESSION** | `offoff_elliptic_spike_theorem.md` |
| corrected off/off variance `Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | spike extraction + Igusa + Grothendieck--Lefschetz/Deligne |
| in `K=o(p^(1/4))` and direct-theorem range, `Var O<<pK^(8/3)` | **EXACT + EXTERNAL-THEOREM** | corrected off/off theorem + direct Cayley energy |
| sharp centered pointwise target `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` | **OPEN** | no verified theorem removes the `K^(2/3)` loss |
| product-row `O(1)` intersection theorem in the polynomial split-prime regime | **OPEN / NOT-PROMOTED** | exact affine trace-set reduction; finite evidence only; stronger tentative `<=1` bound is false |
| microscopic BGS/GOE local eigenphase law | **OPEN** | no mean-spacing local-law/comparison mechanism |

## Current obstruction architecture

The exact fourth-moment decomposition is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

Both nontrivial layers are now controlled by the same arithmetic object

```text
A=c(H\{1}),
E_+(A).
```

The mixed layer is exactly Cayley additive energy.  The corrected off/off layer
contains coherent reducible spikes whose second moment is bounded by
`pE_+(A)`; after spike extraction the residual elliptic trace functions are
square-root quasi-orthogonal.  Thus the former elliptic draft is no longer an
independent pointwise bottleneck.

The best uniform pointwise estimate is still

```text
E_+(A)<34K^(8/3)
```

in `100<K<p^(3/4)/3`.  The target is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

The new shifted-energy orbit theorem shows that one entire multiplicative
parameter block already has near-quadratic square mass `O(K^2 log K)`, but the
exact sum over all blocks is only an `O(K^3)` argument.  Therefore the remaining
information must be cross-block: sparsity/cancellation in the distribution of
shifted multiplicative excess, or a direct bound on intersections of distinct
product rows.

## Product-row frontier

For a noncentral product row write `xy=w^2`, `x=wz`, `y=wz^(-1)`.  For two
rows `w^2` and `q^2`, a common finite Cayley parameter reduces exactly to

```text
Y=alpha X+beta,
X=z+z^(-1),
Y=y+y^(-1),
alpha=w(1-q^2)/(q(1-w^2)),
beta=2(q^2-w^2)/(q(1-w^2)).
```

Each row contributes at most one unordered subgroup pair to a fixed parameter.
Hence an `O(1)` bound on the number of common parameters for every two distinct
rows would force non-forced Cayley energy `O(K^2)` in the sparse regime.

This is currently **OPEN**.  Finite sweeps above `p>K^4` support a small
intersection phenomenon, but computation is not promoted.  In particular, the
stronger exploratory claim “at most one” has an explicit counterexample:
`(K,p)=(41,2908049)` has a row pair with two common parameters.

## Finite negative controls

The active regression corpus includes large split-prime exceptions

```text
(K,p)=(29,728017),
(K,p)=(31,1042903),
```

both with `p>K^4` and additive Cayley excess `48`.  Therefore no theorem of the
form “`p>K^4` implies exact baseline” is active or plausible without additional
structure.

Complete fixed-order finite certificates remain

```text
E_11={23,67,89},
E_13={53,79,131,157,313},
```

and `(p,K)=(461,23)` has energy `1190` versus forced baseline `902`.

## Evidence boundaries

- finite computation never proves a growing-parameter theorem;
- the Jacobi kurtosis theorem is not a Gaussian distribution theorem;
- ordinary full trace is not a parity/desymmetrized spectral block;
- fourth-moment control is not a mean-spacing local eigenvalue law;
- multiplicative Cayley rigidity is not silently transferred to additive
  rigidity after reduction.

## Retractions and superseded routes

See [`retractions.md`](retractions.md) for mechanisms.  The historical
Möbius/M4D M1 proof, one-sided mixed counting, ESY-to-BGS shortcut,
noncommutative trace shortcut, Hecke-centering Julia line, `cdense_transfer`,
`sol6`, unsupported higher-rank/Sp(2g) promotion, temporary real-projection
spectral bug, unresolved all-orders word-trace promotion, the spike-free
off/off theorem, and the residual discriminant-height `O(K^3 log K)` heuristic
are not active results.

Microscopic BGS/GOE universality remains open even if the entire present
fourth-moment programme is completed.
