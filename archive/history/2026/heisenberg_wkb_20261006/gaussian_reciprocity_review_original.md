# Independent audit: exact global Gaussian reciprocity

## Claim and primary verdict

**Proved as written**, for the exact finite-dimensional identities (G3)–(G7), with the finite-order WKB amplitudes and fixed physical time specified by the cited construction. This verdict is about an exact representation of `Tr V_(N,J)^m` for each finite `J,m,N`, with odd `N`; it is not a uniform analytic estimate in `m,N`, a trace formula for the exact `U_N` with zero error, or a BGS cancellation result. The associated unique real stationary point assertion also follows from the canonical specified-time bounds.

Audit target: `exact_gaussian_reciprocity.md`, SHA-256 `6cbbc685bfa5956736ee980180b1dc74f5afb5ea43a5e4a753a047bdb357f4f0`, matching the frozen copy. Canonical repository inspected read-only at `300d99270d11c87d0aa84e9d8f624491788629ba`; its working tree was clean at inspection. No canonical edits were made.

The primary dependency leaves checked directly were:

- `mathematics/fixed_map_path_model.md`, raw `W_N`, ordinary midpoint action, fixed `tau=10^-80`, and ordinary matrix trace; SHA-256 `d5365063f0967dabcac741a93c6f411d6402c913074944e1f9e383b2b5149b08`.
- `mathematics/four_branch_parametrix.md`, Sections 1–2, Section 4 and the dependency-boundary paragraph; SHA-256 `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`.
- Companion `factorial_wkb_reduction.md`, Section 6, finite-order recursive transports; SHA-256 `6487183ba4359319fa3def390025e75f33655be4876eca7cea2eced3b56eabcd`.

The companion's entire factorial perturbation theorem is not re-audited here; its finite-order transport definition is sufficient to type and prove the present identity. Governing status/conventions were checked in `AGENTS.md`, `SOURCE_OF_TRUTH.md`, `record/repository_conventions.md`, `RESEARCH.md`, and the relevant claim ledger, registry, results and open-question entries. They leave TRACE-005 and deterministic BGS open.

## Dependency graph and obligations

Raw finite-shift action → real analytic characteristic graph → finite-order scalar transport amplitudes and gluing → finite four-branch matrix path sum → extension of the complete branch sum to the `4N` lattice → positive rational quadratic reciprocity → absolutely convergent Fourier multiplier identity → Abel/Fresnel integral interpretation.

Every arrow above passes. The separate arrows from this representation to uniformly controlled complex deformation, uniformly summed saddle remainders, and the signed TRACE-005 hierarchy are **not addressed** by this identity and remain open. The target explicitly keeps them open.

| Obligation | Result | Reason |
|---|---|---|
| Raw versus midpoint convention | Passed | Ordinary half-shift is derived from `(-1)^(kl) T_N(l,k)`, not substituted |
| Four-branch initial identity and sampling gluing | Passed | Exact phase identities, with integer phase jumps after multiplication by `N` |
| `m=1,2` multiplicities | Passed | `B_1=4`, `B_2=[[6,-2],[-2,6]]` |
| `N` to `4N` extension | Passed | Only the complete branch sum is extended; factor is exactly `4^-m` |
| Positive quadratic reciprocity and winding quotient | Passed | Poisson derivation over `Z^m/BZ^m`, real/rational inverse |
| Normalization and Maslov phase | Passed | Positive quadratic form with negative chirp gives `exp(-i*pi*m/4)` |
| Fourier class and Abel interchange | Passed | Actual factors are periodic real analytic, hence in the Wiener algebra at fixed parameters |
| Resonances | Passed | No coprimality hypothesis; independent exact checks include all requested cases |
| Uniform stationary equation | Passed | Local edge Hessians give an `m`-independent row-sum bound |
| Uniform norm of sampled winding sum | Not addressed | `L^2` unitarity is insufficient even for point evaluation at a fixed center |
| Global strip-limited contour deformation and summed tails | Not addressed | Explicitly left open |

## 1. Reconstructing the actual sampled kernel

The canonical convention is

`M_jk=N^-1/2 e_N(-inv8*(3j²-2jk+3k²))`,

`A_N u(x)=sum c_kl e(k*(x+h*l/2)) u(x+h*l)`.

Indeed `inv2=(N+1)/2` modulo odd `N`, so the two factors `(-1)^(kl)` cancel between the raw Weyl sign and `e(kl/2)`. Thus the ordinary Hamilton–Jacobi equation is genuinely the equation of the given raw quantizer.

For arbitrary integer sampling indices, set `P=3j²-2jk+3k²` and `t=j-3k`. The initial branch sum is

`e(3N/8)e(-P/(8N)) sum_(r mod4)e((-3Nr²+2tr)/8)/(2sqrt(N))`.

The four-term sum is `2e((-3N+3Nt²)/8)`. Since `3t²-P` is divisible by 8, the result is exactly the raw modular kernel, including odd composite dimensions. This calculation fixes the absolute phase used later.

At time `tau`, canonical HJ uniqueness supplies

- `S_(r+4)-S_r=x-3y-3r-6`;
- `S_r(x+1,y)-S_(r-3)(x,y)=-2r-2y+3`;
- `S_r(x,y+1)=S_(r+1)(x,y)`.

The amplitude transports carry the corresponding identities without phase factors. On `x=j/N,y=k/N`, every displayed polynomial phase correction multiplied by `N` is an integer. Reducing branch labels modulo 4 therefore preserves the *summed sampled kernel* under either coordinate translation by 1.

The path branch sum is a product of these summed kernels. It is consequently 1-periodic on the sampling lattice in every cyclic vertex, also for self-neighbours (`m=1`) and repeated neighbours (`m=2`). Its sum over a `4N` box is `4^m` times its sum over an `N` box. No individual branch, and no off-lattice function, has been assigned this 1-periodicity.

## 2. Quadratic form, determinant, and quotient

Summing the initial edge phases gives

`Phi_r^0 = -x^T(6I-P-P^T)x/8 + (r-3P^T r)^T x/4 -3|r|²/8`,

with the cyclic-index convention equivalent to `t_j=r_j-3r_(j-1)`. The edge expansion itself fixes this index orientation. The eigenvalues of `B_m` are `6-2cos(2*pi*k/m)`, lying in `[4,8]`. Their product is `lambda^m+lambda^-m-2`, where `lambda=3+2sqrt(2)`. In particular the determinants at `m=1,2,3,4` are `4,32,196,1152`.

The quotient is the full integer lattice quotient `Z^m/B_m Z^m`, of cardinality `D_m`. It has no dependence on modular invertibility at `N`. At the requested resonances, `gcd(D_m,N)` is respectively `7,3,9`. Every occurrence of `B^-1` is the rational matrix `adj(B)/det(B)`. Shifting a representative by `Bz` shifts its center by `4z` and changes `A^0` by `z·(t+4nu)+2z^TBz`, an integer. The identity is representative-independent.

## 3. Reciprocity derived independently

Let `B` be explicitly symmetric positive-definite integral, `L` even, and `a` integral. The finite chirp is well-defined because translation by `Lz` changes its exponent by

`-z^TBj -(L/2)z^TBz+a·z`,

an integer. Apply Poisson summation to

`exp(-pi*(epsilon+i/L)*x^TBx +2pi*i*a·x/L)`.

On the original side, each `LZ^m` coset contributes its chirp value times asymptotic mass

`epsilon^(-m/2)/(L^m sqrt(det B))`.

On the dual side the prefactor converges to

`L^(m/2) exp(-i*pi*m/4)/sqrt(det B)`.

The inverse complex coefficient is

`epsilon*L²/(1+epsilon²L²) - i*L/(1+epsilon²L²)`.

Grouping dual lattice points by `BZ^m` gives the limiting phase

`e((L/2)*(nu-a/L)^TB^-1*(nu-a/L))`

and exactly the same divergent coset mass as on the original side. After rescaling the coset variable by `sqrt(epsilon)`, the difference of quadratic phase coefficients contributes `O(epsilon)`; the real Gaussian gives integrable domination. Fixed shifts of the coset do not change the limiting Gaussian mass. Dividing by the common mass and replacing `nu` with `-nu` proves G4. All constants here can depend on fixed `B,L,m`; no simultaneous limit is used.

This proof is valid at every requested resonance. It uses no inverse of `B` modulo `N`, no nonresonance removal, and no cancellation estimate beyond the exact finite identity.

## 4. Exact Fourier-mode control and normalization

For one 4-periodic mode `F(x)=e(ell·x/4)`, substitute `a=N*t+ell`, `L=4N` in the reciprocity just proved. Writing `v=t+4nu`, the dual exponent expands exactly into

`N*v^TB^-1*v/8 + ell·B^-1*v/4 + ell^TB^-1*ell/(8N)`.

After retaining the constant `-3N|r|²/8`, this is precisely the G6 summand for that mode. This identity holds for *every* integer `ell`; no restriction to multiples of 4 is needed on the extended lattice. Summing absolutely over modes proves G6 for each actual `F_r`.

The normalization is independently

`(2sqrt(N))^-m × 4^-m × (4N)^(m/2) = 4^-m`,

with the remaining factors `e(3mN/8)`, `exp(-i*pi*m/4)` and `D_m^-1/2` unchanged. No branch or winding count is absorbed in a constant.

There is an additional clean full-branch algebraic control: if *all* branch factors are the common mode `e(n·x)` with integer `n`, it is 1-periodic and preserves the full sampling gluing. G6 must then equal

`Tr[D(n_0)M_N ... D(n_(m-1))M_N]`

with `D(n)_jj=e(n*j/N)`. Directly, this trace is

`N^-m/2 sum_(j modN) e((-inv8*j^TB_m*j+n·j)/N)`.

This last formula uses the canonical raw modular phase and is independent of the branch construction. By contrast, a common mode `e(ell·x/4)` with `ell` not divisible by 4 generally does *not* preserve gluing, so applying G3 to it would be an invalid control. The independent tests below distinguish the two cases.

## 5. Actual amplitudes are in the required function class

The required class can be weakened from analytic functions to the periodic Wiener algebra `sum |Fhat(ell)|<infinity`.

The canonical graph is globally real analytic: the characteristic vector field is analytic, periodic and bounded, the real projection derivative stays away from zero, and the projection is onto. For each fixed finite transport order, the amplitudes solve finite linear analytic transport equations with analytic coefficients and analytic initial data. Integrating along these characteristics preserves real analyticity. The extra higher-order operators differentiate only finitely many times at any fixed order.

Under `x→x+4`, the initial phase changes by a polynomial linear in `x`, with integer derivative `-3`; under `y→y+4`, the derivative change is the integer `1`. Periodicity of `g` in its two arguments preserves those changes under HJ uniqueness. Consequently `S_r-S_r^0` is separately 4-periodic. In each transport operator, phase derivatives of order at least 2 are unchanged, and the first derivative occurs through periodic symbol derivatives; hence the transport coefficients and all amplitudes inherit 4-periodicity from their initial conditions.

A finite product of these analytic periodic edge factors, including the exponential of the finite sum of phase corrections, is analytic periodic on the compact `m`-torus. It has a holomorphic extension to some positive strip and exponentially summable Fourier coefficients. The repeated-variable cases `m=1,2` remain analytic by composition. Thus the exact actual nonlinear `F_r`, not a linearized substitute, belongs to the needed class.

Uniformity boundary: a common edge strip can be chosen at each fixed `J`, but on a complex strip the exponential nonlinear factor can grow like `exp(C*N*m)`, and the amplitude product can grow exponentially in `m`. Neither a dimension-uniform Wiener norm nor a useful bound on sampled transformed values follows. Smoothness alone would suffice at fixed dimension via sufficiently many derivatives; it would likewise not give dimension-uniform constants. No unproved global entire extension is needed or supplied.

## 6. Abel/Fresnel operator

For `K=B/4`, put `C_epsilon=epsilon I+i N K` and `q=ell/4`. The Gaussian integral on a single mode, after multiplying by the G7 normalization, has multiplier

`exp(i*pi*m/4) sqrt(det(NK)) det(C_epsilon)^(-1/2) exp(-pi*q^T C_epsilon^-1 q)`.

Use the square-root branch continuous from positive real damping. In the limit this is

`exp(pi*i*q^T(NK)^-1 q)=e(ell^TB^-1ell/(8N))`.

The determinant factor has modulus at most 1, since each positive eigenvalue `lambda` of `NK` contributes `(lambda²/(epsilon²+lambda²))^(1/4)`. The last exponential also has modulus at most 1, because `Re(C_epsilon^-1)` is positive semidefinite. Therefore these regularized mode multipliers are dominated by 1, uniformly in the frequency and in positive damping. Absolute Fourier summability justifies dominated convergence and even uniform convergence in the real center `x`, for each fixed `F`.

For fixed positive damping, Fourier interchange with the integral is also justified by `sum|Fhat|` times the integrable damping Gaussian. These are two distinct interchanges; both are valid.

The multiplier extends unitarily to periodic `L²`, but pointwise sampling is asserted here only for the Wiener/analytic class. It is not a bounded evaluation functional on arbitrary `L²` input. This distinction prevents using the unitary statement as an orbit-sum estimate.

At a center `x=B^-1(t+4nu)`, direct completion of the square gives

`Phi_r^0(x+y)+nu·(x+y)=A^0-y^TKy/2`.

Adding the *full* nonlinear correction gives exactly the nonlinear lifted phase in the note. The regularization remains an Abel Gaussian about the chosen center; no unproved cutoff-independent improper integral or contour rotation has been introduced.

## 7. Unique real stationary point: the uniform part that is justified

Write the phase correction as a sum of edge functions `f_j(x_j,x_(j+1))`. The canonical specified-time C² estimates imply each edge Hessian entry is `O(tau)`, with explicit finite constants and an `O(10^50*tau²)` remainder. The initial linear relation for `p` has coefficients bounded by 1, so a conservative edge Hessian bound `10^10|tau|+10^50*tau²` suffices.

Each row of the cyclic total Hessian receives at most four such entries counted with multiplicity. This remains true for `m=1` (`f_xx+2f_xy+f_yy`) and `m=2`. Therefore its maximum row-sum norm is less than `10^-60` at the specified `tau=10^-80`, uniformly in `m,r,x`.

The inverse `K^-1` is entrywise nonnegative: use the convergent series for `B^-1=(1/6) sum_{j>=0}((P+P^T)/6)^j`. Since `K 1=1`, its row sums equal 1, giving `||K^-1||_infinity=1`. The stationary equation is consequently a contraction of all `R^m`, with a bounded `O(tau)` displacement. This gives one real stationary point per lifted phase, not distinctness of all listed physical periodic orbits and not uniform stationary-phase error bounds.

## 8. Independent executed exact controls

Two new scripts were written without importing or copying the author's verification code:

- `exact_controls.py`: 10 complete branch/winding identities against the raw modular trace with common integer-frequency insertions.
- `exact_branch_modes.py`: 10 individual-branch, genuinely 4-periodic Fourier-mode reciprocity identities on the extended lattice. These include frequencies not divisible by 4.

Both cover `(m,N)=(1,3),(2,3),(3,7),(4,3),(4,9)`, with two nonconstant frequency vectors each. All 20 remainders are exactly zero. The largest extended lattice enumerated has `36^4=1,679,616` points. Quotient representatives use column Hermite normal form; their exact distinct rational residue signatures are additionally checked in the complete-branch script. Winding counts are `4,32,196,1152`.

Arithmetic: integer phase histograms and exact integer polynomial division by the relevant cyclotomic polynomial; no floating-point roots. The largest cyclotomic conductor is `82944`. Rational inverses are `adj(B)/D`. Square roots use `sqrt(2)=zeta_8+zeta_8^-1` and quadratic Gauss sums for `sqrt(3),sqrt(7)`. NumPy int64 is used for the finite histograms and phase numerators; the concrete input ranges keep these well below its bound, and polynomial reduction uses Python arbitrary-precision integers. No asymptotic proposition is inferred from these finite checks.

Commands executed successfully:

`python3 /workspace/shared/bgs_global_reciprocity_review/exact_controls.py`

`python3 /workspace/shared/bgs_global_reciprocity_review/exact_branch_modes.py`

Results: `exact_controls.json`, `exact_branch_modes.json` in this review directory. Both scripts were also rerun under `python3 -O`; all checks use explicit exception-raising guards and remain active under optimization. All runs passed.

## 9. Precise editorial clarifications and strongest safe conclusion

No formula repair is required. Three clarifications would make the proof easier to reuse without overstatement:

1. At G4, spell out “symmetric positive-definite integral matrix” rather than the abbreviated “positive integral B.”
2. Insert the amplitude-periodicity/analyticity argument from Section 5 above and state the Wiener-algebra hypothesis explicitly. Distinguish pointwise definition on this class from the abstract unitary `L²` extension.
3. State explicitly that G7 uses the indicated center-based Abel regularization, and that the actual-`U` comparison comes from a separate finite-order operator error, not from equality `U=V`.

The representation really does bypass an unresolved plane-to-odd-torus trace theorem for this *initial conversion*: it starts with a concrete finite matrix, expands its finite trace exactly, uses exact sampled gluing, and applies an elementary lattice identity. No torus FIO trace theorem is hidden in an arrow. The only analytic construction required is the already specified one-step direct discrete WKB construction and its finite-order transports.

The strongest safe conclusion is an exact all-finite-`m` Gaussian/Fresnel representation for the complete nonlinear finite-order WKB trace, including every branch and every winding class, even at noncoprime resonances. It does not establish a useful Heisenberg-scale winding-sum bound, a strip-limited global deformation, a summed optimal remainder, or signed spectral cancellation. No BGS conclusion follows.
