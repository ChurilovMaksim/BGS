# Claim ledger

This file is the repository-wide status authority. Historical commits, old
manuscript text and exploratory notes may contain stronger claims; this file
wins.

## Status vocabulary

- **EXACT** — current project derivation with explicit hypotheses.
- **EXACT + EXTERNAL-THEOREM** — exact project reduction whose remaining named
  input is a verified published theorem with its hypotheses checked in project
  notation.
- **FINITE-CERTIFICATE** — exact exhaustive or kernel-checked statement at
  explicit finite parameters.
- **FINITE-REGRESSION** — finite implementation/reference agreement; useful for
  reproducibility, not a universal proof.
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
| shifted-energy orbit summation alone yields only global `O(K^3)` | **EXACT** | exact global identity + orbit partition; documented limitation |
| fixed-product row uniqueness: one unordered pair per row and nonzero Cayley parameter | **EXACT + FINITE-REGRESSION** | `cayley_product_row_intersections.md`; CI regression |
| exact cross-row excess identity `Delta_K(p)=2 sum_{u<v} sum_{t in T_u cap T_v} omega_u(t)omega_v(t)` | **EXACT + FINITE-REGRESSION** | `cayley_product_row_intersections.md`; generic and exceptional checks |
| `Delta_K(p)<=4 I_K(p)(K-1)(K-2)` for maximum row intersection `I_K(p)` | **EXACT** | immediate from the cross-row identity |
| product-row intersection is the constrained affine trace-set equation `Y=alpha X+beta`, `X=z+z^-1`, with explicit `alpha,beta` | **EXACT + FINITE-REGRESSION** | `cayley_product_row_intersections.md` |
| order-three row form obstruction: if `I_(i,j)(p)>=3`, then `p|G'_(K,r)^(3)` for the normalized ratio class `r=j/i` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `cayley_product_row_subresultants.md`; Brown--Traub subresultant theorem; exact SymPy anchors |
| if split `p` does not divide `G'_K^(3)`, then `I_K(p)<=2`, `Delta_K(p)<=8(K-1)(K-2)`, and `E_+(A)<=11(K-1)(K-2)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | preceding coarse obstruction + exact row-energy theorem |
| universal row polynomial `P_K(Y)=sum_j binom(K,2j)Y^j`, `|Disc(P_K)|=2^((K-1)(K-3)/2)K^((K-3)/2)`, and its second-order ODE/row-coefficient recurrence | **EXACT + FINITE-REGRESSION** | `cayley_product_row_projective_bezout.md`; CI universal-row checks |
| projective Bezout nullity equals projective row intersection degree, including roots at infinity | **EXACT + FINITE-REGRESSION** | self-contained Bezout proof + direct finite-field nullity/intersection regression |
| exact determinantal support: for split `p`, `p|B'_K^(3)` iff `I_K(p)>=3` | **EXACT + FINITE-REGRESSION** | `(m-2)`-minor Fitting ideal in `cayley_product_row_projective_bezout.md`; CI negative/positive controls |
| local exact valuation `v_P(B_(K,r)^(3))` is the sum of all cross-evaluation valuations after discarding the two largest | **EXACT** | local Lagrange diagonalization of the Bezoutian |
| `B'_11^(3)=1`, hence `I_11(p)<=2` for every split `p==1 mod 11` | **FINITE-CERTIFICATE** | exact HNF norms for all five unordered ratio classes; optional deterministic verifier |
| bound `P_split^+(B'_K^(3))<=K^(4+o(1))`, or equivalent growing-`K` control of the exact projective support | **OPEN** | strictly sharper closure target; would close pointwise centered Cayley scale in `K=o(p^(1/4))` |
| coarse bound `P_split^+(G'_K^(3))<=K^(4+o(1))` | **OPEN** | still sufficient but superseded as the preferred divisor target by the exact `B'_K^(3)` support |
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
| sharp centered pointwise target `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` for all intended split designs | **OPEN** | quadratic scale closed outside `p|B'_K^(3)`; exact exceptional split support remains unresolved |
| microscopic BGS/GOE local eigenphase law | **OPEN** | no mean-spacing local-law/comparison mechanism |

## Current obstruction architecture

The exact fourth-moment decomposition is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

Both nontrivial layers are controlled by

```text
A=c(H\{1}),
E_+(A).
```

The mixed layer is exactly Cayley additive energy. The corrected off/off layer
contains coherent reducible spikes whose second moment is bounded by
`pE_+(A)`; after spike extraction the residual elliptic trace functions are
square-root quasi-orthogonal. Thus the former elliptic draft is no longer an
independent pointwise bottleneck.

The best theorem with no arithmetic exclusion on the split prime remains

```text
E_+(A)<34K^(8/3)
```

in `100<K<p^(3/4)/3`. The sharp target is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

The shifted-energy orbit theorem already puts one multiplicative parameter block
at `O(K^2 log K)` square mass, but summing all blocks loses to `O(K^3)`.
The fixed-product decomposition then isolates the genuinely non-forced part:
all excess is interference between **different product rows**.

## Product-row / projective-Bezout frontier

For a noncentral row `xy=w^2`, write `x=wz`, `y=wz^(-1)`. For two rows
`w^2,q^2`, a common Cayley parameter is exactly a constrained affine
intersection

```text
Y=alpha X+beta,
X=z+z^(-1),
Y=y+y^(-1),
alpha=(q-q^(-1))/(w-w^(-1)),
beta=2(w/q-q/w)/(w-w^(-1)).
```

Each row supports at most one unordered subgroup pair at a fixed nonzero
parameter. Hence

```text
Delta_K(p)<=4I_K(p)(K-1)(K-2).
```

The earlier projective row form

```text
R_i(U,V)=prod_a(D_(i,a)U-N_iV)
```

encodes all row parameters, including `t=2` at infinity.  The fixed-degree
subresultant integer `G'_K^(3)` is a correct safe obstruction but can have false
positive split factors when dehomogenization loses leading degree.

The exact refinement uses the ambient degree-`m` Bezout matrix of a normalized
row pair.  Its nullity is exactly the homogeneous projective gcd degree.  The
ideal generated by all `(m-2)x(m-2)` minors therefore has exact support:

```text
p|B'_K^(3)  <=>  I_K(p)>=3
```

for split primes.  Outside this smaller integer one has pointwise

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

The strictness is real: `G'_(11,7)^(3)=23`, but the exact projective nullity in
that ratio class at `p=23` is at most one and globally `I_11(23)=2`. Exact HNF
calculation over all `K=11` ratio classes gives

```text
B'_11^(3)=1.
```

The universal polynomial

```text
P_K(Y)=sum_j binom(K,2j)Y^j
```

has only `2,K` in its discriminant and generates every row by a Mobius
substitution plus a second-order derivative recurrence.  Locally at a split
prime the Bezoutian diagonalizes in a Lagrange basis; the exact ideal valuation
is the total cross-evaluation valuation after the two largest entries are
removed.  This identifies the precise remaining mass as the **third and later
row collisions**.

The preferred closure lemma is now

```text
P_split^+(B'_K^(3))<=K^(4+o(1)).
```

It is **OPEN**.  The older analogous statement for `G'_K^(3)` remains sufficient
but is no longer the sharp arithmetic target.

## Adversarial finite controls

The active regression corpus contains large split exceptions

```text
(K,p)=(29,728017),
(K,p)=(31,1042903),
```

both with `p>K^4` and additive Cayley excess `48`; therefore `p>K^4` alone does
not imply exact baseline.

The stronger exploratory row claim `I_K(p)<=1` is false:

```text
(K,p)=(41,2908049)
```

has a row pair with two common parameters.

The coarse order-three subresultant regression includes

```text
G'_(7,2)^(3)=1,
G'_(11,2)^(3)=1,
G'_(13,3)^(3)=3^3,
G'_(13,12)^(3)=5^8,
G'_(17,10)^(3)=103^2,
G'_(23,18)^(3)=47^20*139^2.
```

The split prime `103` is realized by a three-intersection row pair at `K=17`;
for `K=23`, intersections of sizes `5` and `3` occur at `p=47,139`.

The exact projective regression additionally contains the false-positive control
`(K,p,r)=(11,23,7)` and reproduces the genuine `K=17,23` projective nullities.
Exact HNF norms at `K=11` remove every split factor from the order-three support.
These are finite mechanism checks, not asymptotic evidence promoted to proof.

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

See [`retractions.md`](retractions.md) for mechanisms. The historical
Möbius/M4D M1 proof, one-sided mixed counting, ESY-to-BGS shortcut,
noncommutative trace shortcut, Hecke-centering Julia line, `cdense_transfer`,
`sol6`, unsupported higher-rank/Sp(2g) promotion, temporary real-projection
spectral bug, unresolved all-orders word-trace promotion, the spike-free
off/off theorem, and the residual discriminant-height `O(K^3 log K)` heuristic
are not active results.

Microscopic BGS/GOE universality remains open even if the entire present
fourth-moment programme is completed.
