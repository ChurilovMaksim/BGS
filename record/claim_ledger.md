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
| normalized row coefficients satisfy `alpha=U_(r-1)(tau/2)`, `beta=-2U_(r-2)(tau/2)` and the sparse row relation has a universal `(X-1)^3` factor | **EXACT** | `cayley_product_row_coefficient_ideal.md` |
| norm-gcd order-three obstruction: `I_(i,j)(p)>=3 ==> p|G'_(K,r)^(3)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `cayley_product_row_subresultants.md`; Brown--Traub; exact SymPy anchors |
| coefficient ideal `J_(K,r)^(3)=(S_0,S_1,S_2)` has contraction `J cap Z=D_(K,r)^(3) Z`, the additive exponent of `O_L/J` | **EXACT + FINITE-REGRESSION** | `cayley_product_row_coefficient_ideal.md`; Smith-normal-form CI gate |
| `p|D_(K,r)^(3)` iff some prime ideal `P|p` gives fixed-degree row gcd at least `3` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | coefficient-ideal contraction lemma + Brown--Traub subresultant criterion |
| `rad(D_(K,r)^(3)) | rad(G_(K,r)^(3))`; the coefficient-ideal obstruction has no rational false positives from different primes above `p` | **EXACT + FINITE-REGRESSION** | `cayley_product_row_coefficient_ideal.md`; exact finite anchors |
| if split `p` does not divide `D'_K^(3)`, then `I_K(p)<=2`, `Delta_K(p)<=8(K-1)(K-2)`, and `E_+(A)<=11(K-1)(K-2)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | coefficient-ideal obstruction + exact row-energy theorem |
| bound `P_split^+(D'_K^(3))<=K^(4+o(1))`, or equivalent growing-`K` control of its split support | **OPEN** | this would close the pointwise centered Cayley target in `K=o(p^(1/4))`; no proof yet |
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
| sharp centered pointwise target `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` for all intended split designs | **OPEN** | closed outside `p|D'_K^(3)`; exceptional split support remains unresolved |
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

## Product-row / coefficient-ideal frontier

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

After Galois normalization `w=zeta`, `q=zeta^r`, with
`tau=zeta+zeta^(-1)`, this becomes the exact Chebyshev pair

```text
alpha=U_(r-1)(tau/2),
beta=-2U_(r-2)(tau/2).
```

Each row supports at most one unordered subgroup pair at a fixed nonzero
parameter. Hence, with `I_K(p)` the maximum number of common parameters between
two distinct rows,

```text
Delta_K(p)<=4I_K(p)(K-1)(K-2).
```

The projective row form

```text
R_i(U,V)=prod_a(D_(i,a)U-N_iV)
```

encodes all row parameters, including `t=2` as the point at infinity. After
normalizing a row pair to `(1,r)`, let `J_(K,r)^(3)` be the `O_L`-ideal generated
by all coefficients of the first three fixed-degree subresultants
`S_0,S_1,S_2`, and write

```text
J_(K,r)^(3) cap Z = D_(K,r)^(3) Z.
```

The positive generator `D` is exactly the additive exponent of `O_L/J`.
Moreover

```text
p|D_(K,r)^(3)
iff
some prime ideal P|p has deg gcd(R_1,R_r mod P)>=3.
```

This is the canonical simultaneous-congruence support. The earlier integer
`G_(K,r)^(3)`, defined as a gcd of individual coefficient norms, remains a
valid sufficient obstruction, but it can contain rational false positives from
different prime ideals above the same `p`; exactly

```text
rad(D_(K,r)^(3)) | rad(G_(K,r)^(3)).
```

Therefore outside

```text
D'_K^(3)=product_[r]D'_(K,r)^(3)
```

one has pointwise

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

This closes the quadratic centered-energy scale on an explicit arithmetic
subfamily. The remaining arithmetic lemma on this route is to control the
**split prime divisors** of `D'_K^(3)` as `K` grows. A bound

```text
P_split^+(D'_K^(3))<=K^(4+o(1))
```

would close the pointwise Cayley-energy bottleneck throughout
`K=o(p^(1/4))`. It is **OPEN**.

A common trace pair also satisfies the sparse cyclotomic relation

```text
s_r t_a-s_1 t_b-2s_(r-1)=0,
s_n=zeta^n-zeta^(-n),
t_a=zeta^a+zeta^(-a),
```

whose Laurent polynomial has a universal `(X-1)^3` factor. Subtracting two
such relations expresses the common slope as a quotient of products of
cyclotomic units. Three row intersections therefore impose two simultaneous
cyclotomic-unit congruences. This is the active mechanism-level route toward
the open split-divisor bound; no generic subgroup incidence theorem currently
supplies the needed `O(1)` estimate.

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

The older norm-gcd subresultant anchors include

```text
G'_(7,2)^(3)=1,
G'_(11,2)^(3)=1,
G'_(13,3)^(3)=3^3,
G'_(13,12)^(3)=5^8,
G'_(17,10)^(3)=103^2,
G'_(23,18)^(3)=47^20*139^2.
```

The sharper coefficient-ideal contractions give

```text
D'_(7,2)^(3)=1,
D'_(11,2)^(3)=1,
D'_(13,3)^(3)=3,
D'_(13,12)^(3)=5^2,
D'_(17,10)^(3)=103,
D'_(23,18)^(3)=47^3*139.
```

The split prime `103` is realized by a three-intersection row pair at `K=17`;
for `K=23,r=18`, row intersections have sizes `5` at `p=47` and `3` at
`p=139`. These are finite mechanism checks, not asymptotic evidence promoted to
proof.

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
