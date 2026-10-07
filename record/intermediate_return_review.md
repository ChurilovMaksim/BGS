# Source-bound accepted review: intermediate_return_operator.md

This is the historical independent internal review, with its original scope
and verdict. Its frozen SHA256 is `a09a00af80ef779fc1e5354b294c4869f9eb7cd8e3d1dc35f4aebf601680d6dc`.
The [maintained proof](../mathematics/intermediate_return_operator.md) makes only the status, navigation,
and disclosed nonblocking exposition changes recorded in the promotion map.
Original outside paths and commands in the report identify historical
artifacts; their exact bytes are recoverable through the
[archive map](../evidence/intermediate_old_layers_20261007/input_map.json).
The [portable replay](../computations/verification/intermediate_old_layers_certificates.py)
replaces historical execution paths and retains all arithmetic checks under
Python optimization. This is independent internal review, not external peer
review or formal certification.

# Independent audit: intermediate old-layer return operators

## Normalized claim and verdict

**Primary verdict: proved as written**, within the explicitly declared oldform, cat-spectrum, exact-order, and coherent-basis inputs and the pre-character-compression scope. The bounded controls are independently verified in precisely the ranges recorded below. No mathematical counterexample or load-bearing missing implication was found. Two endpoint/coverage clarifications below are nonblocking.

For integers `j>=1`, `s=e-2j>=0`, put `h=5^j`, `m=5^s`, `n=h^2 m`, `L=6*5^(j-1)`, and `R=6*5^(e-1)`. On the unchanged raw-Weyl quantization, the translated oldspace has return operator

`B_u=q^(-omega(u,S^L u)/2) T_m((S^L-I)u/h) M_m^L`,

and the full cat-character block uses `X_u=mu^(-L) B_u`. For primitive modes, `X_u^m=z_m I` with `z_m` of exact order `h`; hence `1` is absent and every eigenvalue has exact order `D=hm`. For content-five modes, the declared alternate periods and resonant exception are necessary. At even residual depth `m=H^2`, the inherited coherent lattice has affine cycles of length `H`, primitive cycle holonomies of order `hH`, and the entry valuations and affine-orbit-sum residue claimed in equations (11)--(14). This blocks the specified deepest-core scalar normalization on that lattice; it does not block every lattice or subsequent cancellation.

## Target, identity, and independence

- Frozen proof: `/workspace/shared/bgs_intermediate_return_test/intermediate_return_operator.md`, SHA-256 `3f42c4f41f448c221e4dc92495a11caa3b2cd661168f8cd888abd35971ed1932`.
- Frozen source manifest: SHA-256 `3b344f4180717e6b22087c1a4e373a36ef8bc8a190a243c42be2a9abc79b7272`.
- Canonical base inspected: BGS commit `157277eeca8d8318976ea26bdbb1d3b1aa0d438a`, clean worktree at inspection. Canonical files were read only.
- This review was performed by a fresh sibling task, outside the author's working directory, with fresh raw-matrix, modular-phase, coherent-monodromy, and characteristic-polynomial implementations. It is independent internal review, not external peer review or formal certification.
- The separate `residual25_affine_residue.py/.json` continuation was not read or audited. No conclusion about that continuation is included.
- All three declared output hashes and all ten declared source hashes matched before review. Byte-preserving snapshots and the comparisons are in `frozen/` and `input_hashes.json`.

The actual centered symbol is `A=4000^(-1) sum_v d_v T_7(v) tensor T_n(v)`, using precisely the 32 Gaussian-integer coefficients in the pinned `frozen_antireversor.py`. The cat kernel is `q^(-(3x^2-2xy+3y^2)/8)/sqrt(n)`, with the prescribed induced CRT primitive roots. No scalar renormalization of the five-primary cat, replacement perturbation, averaged model, or generic matrix surrogate is introduced. The seven-primary scalar is immaterial to the projectors only after explicitly retaining its cubic eigenvalue ratios. This audit makes no inference at literal nonzero coupling.

## Dependency graph

1. Raw Weyl multiplication and exact cat covariance (convention; independently checked at raw-matrix level) + accepted oldform intertwining/compression -> return identity (1) and reduced initial factor.
2. Exact order and invertible five-adic leading matrix for `S^6-I` + anisotropy of `2b^2-a^2` modulo 5 -> primitive return classes, scalar monodromy, nonresonance, and affine-cycle lengths.
3. Accepted normalized `M_1=1`, `M_5^6=I`, and oldform restriction + scalar cat return -> normalized five-primary cat order. The odd-core source supplies the phase-safe `M_5^6` argument.
4. Accepted simple residual cat spectrum and complete-oldspace isolation + cubic seven-primary ratios -> a well-defined common `rho=mu^(-L)` on each full product-cat block.
5. Finite geometric algebra -> primitive inverse term, general projector term, and exact `k=0` subtraction.
6. Accepted even coherent basis + raw Weyl multiplication -> monomial affine action, exact holonomy, entrywise valuations, and residue (14).
7. Actual 32-mode dictionary + literal finite rotated-return enumeration + finite-field linear algebra -> the two bounded second-order control results only.

The accepted spectrum, full-oldspace isolation, and coherent-basis results are named internal inputs, not newly promoted theorems of this review. The proof under audit derives the new return/lattice consequences from them. No new external theorem is used by this checkpoint, and no new literature leaf is required.

## Critical independent derivations

### Return formula and character placement

Write `S^L u=u+h b`. Covariance, the inverse Weyl cocycle, and the oldform relations give

`M_n^L T_n(u) J = T_n(S^L u) J M_m^L = T_n(u) J [q^(-omega(u,S^L u)/2) T_m(b) M_m^L]`.

In particular the sign is negative. Iteration is valid because this is an intertwining identity on the translated oldspace, not a commutativity assertion about `T_m(b)` and `M_m^L`.

For `k=a+Lt`, reduction before replacing any character gives the exact five-primary identity

`J* T_n(v) T_n(S^k u) J = D_a M_m^a B_u^t M_m^(-a) M_m^(-Lt)`.

On the right of `P_lambda`, the final factor is the common scalar `mu^(-Lt)`: all residual characters occurring in a product block differ by cube roots, and `3|L`. This yields equation (6), including the conjugation `X_(u,a)=M_m^a X_u M_m^(-a)`. The seven factor is unchanged along the class because `S^L=I mod 7`, but it remains the full Weyl product `T_7(v)T_7(S^a u)`. Neither its cocycle nor the five-primary initial phase is discarded.

For `s>=1`, the normalized residual cat has order dividing `6*5^(s-1)`, so `rho` has order dividing `5^max(s-j,0)`. The same conclusion at `s=0` is immediate from `M_1=1`. Thus `e<=3j` kills both the residual cat power and the wild scalar, but not the residual translation for `m>1`.

### Primitive scalar return and eigenvalue order

At `t=m`, `(S^(Lm)-I)u/h` is divisible by `m`, and both `M_m^(Lm)` and `rho^m` are identity. With `S^(Lm)=[[a,2c],[c,a]]`,

`omega(u,S^(Lm)u)=-c Q(u)`, `v5(c)=j+s`, and `Q(u)` is a unit.

The raw exponent therefore has valuation exactly `j+s` at modulus `n=5^(2j+s)`, giving `z_m` exact order `5^j`. The implication to eigenvalue order is sound: if `x^m=z_m`, then `x^(hm)=1`, and the order of this five-power root must be `hm` because raising to `m=5^s` leaves exact order `h=5^j>1`. In particular `I-X_u` is invertible. This includes `m=1`.

### Weighted finite sum and the resonant branch

Since `X^D=I` in characteristic zero, `X` is semisimple. On an eigenvalue `x!=1`,

`sum_t t x^t = -D/(1-x)`,

so the weighted sum is `2LD/(1-x)=2R/(1-x)`. On `x=1`, summing the arithmetic progression gives `D(L-2a)`. These two calculations prove (7) with the stated generalized inverse. The sign and factor `2R` are correct.

When `a=0`, `k=0` is not present in the original resolvent polynomial. The removed term is `R` times the actual initial operator, not an unconditional identity. This matters for actual pairs with `v+u` a nonzero element of `h Z^2`.

For `u=5u_0` and `j>=2`, using `L'=6*5^(j-2)` gives a scalar return of exact order `5^(j-1)`, eigenvalue order `5^(j+s-1)`, and full summation length `D'=5^(j+s+1)`. A nonminimal summation length is permitted in (7). At `j=1`, Weyl conjugation gives `B=T_m(u_0)^(-1) M_m^6 T_m(u_0)`, so the eigenspace at 1 is exactly the conjugate of the sum of residual eigenspaces with `nu^6=mu^6`. For `m=25`, its rank is 1 at the tame old label and 6 at each nontrivial wild label, as claimed. At `m=1`, the entire one-dimensional operator is resonant. Mixed primitive/content-five pairs cannot meet the return condition modulo `h`.

### Coherent affine cycles, holonomy, and valuation obstruction

For `m=H^2`, `H=5^ell>=5`, all coherent phases and `rho` are five-power roots. Reducing at the chosen prime over 5 gives the affine map `F(y)=S^L y+b_u`. Iterating this affine map yields (10) exactly. The matrix factor `(S^(Lt)-I)/h` is `5^v5(t)` times a matrix invertible modulo 5. Multiplication by the primitive vector `hy+u` keeps that valuation. Consequently `F^t(y)=y mod H` if and only if `H|t`. There are exactly `H` cycles, each of length `H`.

The geometric numerator `sum_(t=0)^(H^2-1) X^t` reduces to `H` copies of the length-`H` orbit sum and is zero in the residue field. Thus equation (11) cannot yield a nonzero scalar residue.

On each cycle, `X^H=eta_O`, and `eta_O^H=z_m` forces `eta_O` to have exact order `hH`. The powers from 0 through `H-1` have disjoint matrix-entry supports, so there is no hidden cancellation in (12). Every nonzero inverse entry has valuation

`-a* = -1/(4*5^(j+ell-1))`.

The proposed deepest-core extension `delta_j=1-q^h` instead has valuation `a_j=1/(4*5^(j+2ell-1))`. Since `a*=H a_j`, every nonzero entry after that normalization has valuation `(1-H)a_j<0`. This is an actual entrywise nonintegrality statement in the inherited coherent basis.

For the leading holonomy coefficient, the global packet label is `x=u+hy`. Its holonomy, before character normalization, is `q^(-omega(x,S^(LH)x)/2)`. The relevant off-diagonal coefficient divided by `hH` is 2 modulo 5, while `Q(x)=Q(u) mod 5`. The character factor contributes a root of order at most `5^max(ell-j,0)`, strictly below `hH`. Therefore the exponent relative to `q^(hH)` is `Q(u) mod 5`, independent of the cycle, proving (14). Here “mod 5” means reduction at the specified prime above 5, not coefficientwise arithmetic in the nonreduced quotient by the ideal `(5)`.

The primitive pair coefficient in `4000^2 delta* H2` is consequently `i d_v d_u/Q(u)` times the initial seven operator and the initial/conjugated affine orbit sum. At `i -> 2`, this becomes `2 d_v d_u/Q(u)`. The upper/upper coefficient filter for `j>=2` is sound. For content-five pairs the corresponding coherent holonomy denominator has valuation `5a*`; their two coefficients contribute valuation 2, giving `2-4a*>0`. The 17 equal-integer-norm upper pairs then follow because their distinct norm values are already distinct modulo 25. No cat-character compression or division by residual cat-cycle length is performed in this reasoning.

## Obligation matrix

| Obligation | Status | Evidence |
|---|---|---|
| Actual raw cat, Weyl sign, CRT symbol | Passed | Pinned definitions; fresh dense raw checks |
| Return identity, residual cat power, common wild character | Passed | Derivation above; all-term phase controls |
| Primitive nonresonance and exact eigenvalue order | Passed | Uniform valuation/order argument |
| General geometric sum and initial-factor subtraction | Passed | Eigenvalue calculation; finite checks |
| Content-five alternate period and j=1 resonance | Passed | Uniform argument and added correct-period controls |
| Affine cycle length and exact holonomy | Passed | Uniform argument; 64 independent monomial models |
| Entrywise negative valuation under naive scale | Passed | Disjoint supports and exact cyclotomic valuations |
| Correct scale and pre-compression orbit-sum residue | Passed | Leading holonomy coefficient calculation |
| All 27 second-order finite compressions in each case | Passed in stated range | Replay and independent characteristic computation |
| Uniform cat-character-compressed simplicity | Out of scope / not established | Explicit stopping boundary |
| Residual25 continuation, full U simplicity, BGS | Out of scope | No inference made |

## Computation audit and exact coverage

The original author script was copied byte-for-byte into this review directory and rerun. It imports the declared pinned helpers and unchanged coefficient file; those hashes were checked. Its output matches the frozen JSON after removing only per-case runtime fields. Python is 3.12.14, NumPy 2.3.5, and SymPy 1.14.0.

1. Original finite cases: `(e,j,m,p)=(4,1,25,420001)` and `(6,2,25,2625001)`. All 54 second-order blocks are squarefree. The first case has 9 zero first-order reductions, and the second has 27. The original maximum matrix dimension is 175.
2. Independent characteristic computation: exact integer SymPy characteristic polynomials reduced modulo `p`, orthogonal to the author's Newton-sum routine, reproduce every coefficient of all 54 compressed polynomials and each derivative gcd.
3. Raw parent-cat control: `n=625`, `m=25`; the actual 625-dimensional kernel, unnormalized old embedding, raw Weyl matrices, and six repeated cat applications verify the return identity for `(1,0),(1,1),(0,1),(0,5)`. The common omitted normalization of the embedding cancels on both sides. The raw oldform intertwining, Weyl cocycle, and covariance signs are checked directly.
4. Exhaustive modular-phase control: all 40,426 and 89,968 nonzero-`k` actual returning terms, respectively, satisfy the independent class-phase factorization and translation identity. This comprises 300 and 124 ordered primitive return pairs respectively, plus all four ordered content-five pairs in each case. All actual modes are included, not just the upper/upper filter.
5. Independent coherent monomial construction: 64 mode/character models over `(j,ell)=(1,1),(2,1),(1,2),(2,2),(3,2),(1,3)`; actual coherent representative-change phases are built from raw Weyl multiplication. Every affine cycle, holonomy, leading coefficient, and asserted valuation is checked. The largest coherent label set has 15,625 elements; these are monomial dictionaries, not dense matrices. Allowed wild labels 0, 1, and 2 are tested where the wild order is nontrivial. This is finite testing, not exhaustive coverage of all characters/depths.
6. Additional content-five control: both signs `(0,±5)` and all 25 residual eigenvalues in both source cases, using `L=6` at `j=1` and the correct `L'=6` at `j=2`. It verifies the complete weighted identity, projector ranks 1/6 at `j=1`, and nonresonance plus primitive fifth-root scalar return at `j=2`.

All matrix arithmetic is exact integer arithmetic modulo the recorded prime; no floating-point decisions are used. The original int64 bound is safe: `175*(2625001-1)^2 < 2^63`; the only potentially triple scalar/Kronecker product in the first-order construction occurs for `j=1`, where `420001^3 < 2^63`. In the fresh dense check, `625*(420001-1)^2 < 2^63`. Modular phase computations outside those dense matrices use arbitrary-precision Python integers.

The authoritative replay and independent-run commands, before/after input hashes, result hashes, run status, caps, and stdout/stderr are recorded in the accompanying manifests. The independent bounded run uses one CPU-affinity slot, cooperative numerical-library thread cap 1, a 2 GiB address-space limit, 180-second per-process CPU limit, and 240-second wall timeout. These controls do not upgrade finite evidence into a uniform proof.

## Nonblocking clarifications

1. At `s=0`, `m=1`, the phrase “b_u is primitive” is best understood as the divided integer lift being primitive, since its reduction is the sole vector over the trivial residual ring. Write “primitive when m>1; trivial residual translation when m=1” for clearer exposition. The return and eigenvalue-order assertions themselves remain valid at this endpoint.
2. In the affine argument, the exact valuation `v5(t)` is an assertion about the lifted vector over the five-adic integers. Modulo `H`, only its truncation at `ell` is visible. The fixed-point iff `H|t` conclusion is correct.
3. The source script tests `(0,5)` with the common primitive period `L` in both cases; its `j=2` branch therefore does not separately exercise the declared alternate period `L'`. This is a coverage precision, not a false operator calculation. The full actual rotated-return sum already includes those terms, and the added independent correct-period tests close the focused coverage gap.

No source edits are required for the central claim. These optional clarifications should not be represented as a new theorem revision without binding its changed bytes.

## Remaining boundary and cheapest next check

The exact unresolved object is the actual cat-character compression of the initial-factor-weighted, character-normalized affine orbit sums, with every residual cat-cycle denominator retained. This audit authorizes no reduction of those denominators modulo 5 and no extrapolation from the two finite cases. The strongest safe new statement is the exact return formula plus the inherited-coherent-lattice obstruction and pre-compression affine residue.

A separate source-bound proof of the character-compression step is the next mathematical obligation. The residual25 continuation is one possible distinct checkpoint, but its evidence and verdict are intentionally excluded from this report. Nothing here establishes full uniform U simplicity, a full propagator commutant theorem, Heisenberg-scale statistics, or BGS.
