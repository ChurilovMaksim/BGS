# Independent bounded audit: hook, Eulerian tree, and phase-current regrouping

Date: 7 October 2026. No source/repository edits or publication. No BGS or asymptotic-universality claim.

## Claim and primary verdict

**Primary verdict: correct only after a stated restriction.** The literal cycle-by-cycle cancellation of the *truncated* finite-dimensional Koszul expansion is valid directly for `m <= N`; for arbitrary `m`, the proof must explicitly append the zero characters `e_j(A)=0` for `j>N` before applying (K2).

This is a local proof correction, not a counterexample to the finite trace/hook identity or to (K3), (T1), (T2), (P6), (F2), or the stated (B3)→(B4)→(B5) reduction. With that zero-extension, the all-`N,m` finite equalities have a valid proof. The phase-current asymptotic (B5) remains unproved, exactly as the author says.

Reviewed claim: for an arbitrary complex `N x N` unitary, independent Haar diagonal phases, and every integer `m>=1`, the signed hook covariance equals the completed Eulerian-edge-type sum, with rooted-word tree coefficients and exact once-counted cyclic/reverse subtraction. Under eventual fixed-constant flatness and operator gaps (B3), the removed Abel-normalized contribution is the ramp, so the remaining Abel identification is equivalent to the negative plateau transform.

Reviewed files and hashes:

- `hook_tree_current_identity.md`: `d5e2a1fe38d4e384387063bb86c99cd2f5b1f56ab4599dc3a4bdecf78fdb30e4`
- `computation_manifest.json`: `bf2c54bcfc23b0c62844614a008d4dd012b0e3f32ec22bc925ff149b8c367530`
- Pinned checked source manifest: `d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba`

## 1. Required correction to marked Koszul cancellation

The finite complex is exact because `d delta + delta d=mI` for positive total degree. Both operators are natural, and the character decomposition and alternating hook signs in (K1) are correct, including `j=m`, `j=N`, and `m>N` endpoints. Unweighted exactness does not bound the exterior-number-inserted character or its covariance.

For the cycle index of `e_j h_(m-j)`, the exterior permutation sign is `(-1)^(j-|F|)`, where `F` is the chosen set of exterior cycles. Multiplying by the insertion sign `(-1)^(j-1)` gives `(-1)^(|F|+1)`. Thus the displayed unrestricted marking identity is correct:

`sum_F (-1)^(|F|+1) sum_(a in F) ell_a = m` for one cycle and `0` for two or more cycles.

However, (K1) includes only `j<=min(m,N)`. Its literal permutation-level expansion therefore permits only selections satisfying `sum_(a in F) ell_a<=N`. The displayed (K2) sums all subsets and is not the same termwise expansion when `m>N`.

Smallest witness: `N=1,m=2`. For the identity permutation with lengths `(1,1)`, the allowed singleton selections contribute `1+1=2`; the excluded size-two selection would contribute `-2`. For the transposition with length `(2)`, the only nonzero unrestricted selection has exterior degree two and is excluded. The truncated weights are therefore `(2,0)`, while (K2)'s unrestricted weights are `(0,2)`. The finite character identity still holds: with a scalar `A`, `e_1 h_1=A^2`, and `e_2=0`.

**Minimal repair:** after (K1), explicitly write

`sum_(j=1)^min(m,N) (-1)^(j-1) j e_j h_(m-j)`
`= sum_(j=1)^m (-1)^(j-1) j e_j h_(m-j)`,

using the dimension identity `e_j(A)=0` for `j>N`. Expand the latter, dimension-independent symmetric-function expression in slot permutations, and then apply (K2). These added zero characters have nonzero individual cycle-index terms, so their presence must not be suppressed in the explanation of pre-site-label cancellation. After the extension, every multi-cycle permutation cancels, equal site labels cause no problem, and the single cycles give `Tr(A^m)` with the correct normalization `m/m!` per permutation.

Consequently the “compulsory top-fermion cancellation” is valid as cancellation in this zero-extended algebraic expansion, followed by specialization to dimension `N`. It should not be described as literal termwise cancellation inside the original truncated complex. For `m=N`, single-cycle pieces can remain; only the disconnected-cycle pieces are claimed to cancel. The overall large top sector cannot be estimated separately by this argument.

The 873 permutation checks verify the unrestricted (K2), not the missing truncation bridge. The independent review checker records the `N=1,m=2` witness and the repaired marking explicitly.

## 2. Dependency closure and obligation findings

Dependency chain:

1. Hook/elementary character identity + zero-extension + unrestricted marking → `Tr(A^m)`.
2. Haar coordinate-phase orthogonality → (K3), grouping by source-row occupation.
3. Directed last-exit queue bijection → (T1); stochastic cofactors and a rank-one determinant → (T2).
4. Primitive-word Möbius inversion, actual rotation orbit sizes, and reflection overlap → (P5) and (P6).
5. Amplitude/phase factorization → nonnegative current weights (F1) and real Fourier sum (F2).
6. (B3) + global periodicity/overlap bounds + geometric gap sums → (B4).
7. Exact CUE Abel benchmark → equivalence (B5), with the negative sign fixed.
8. Accepted positive all-time Abel bound → near-zero tightness and exponential tails. This supports the compact/Abel passage; it does not identify the limit.

Obligations:

- Hook endpoints and signs: **passed**.
- Literal truncated permutation cancellation for `m>N`: **failed as phrased; repaired by the explicit zero-extension above**.
- Rooted-word count, loops, singleton support, periodicity, disconnected support: **passed**.
- Determinant factor and its range: **passed**.
- Cyclic/reverse once-counting and overlap: **passed**.
- Current weights, symmetry, gauge invariance: **passed**, with the sparse-support clarification below.
- Global Abel ramp and negative plateau residual: **passed under exactly (B3)**.
- All-time and near-zero passage: **passed using the cited accepted phase-ensemble bound**, as detailed below.
- 35-case/873-permutation computational claim: **reproduced in that bounded range only**.
- Asymptotic phase-current identification: **not addressed by the finite proof; open**.

## 3. Directed-tree count and stochastic determinant

For a balanced edge matrix, the positive-degree support is a union of strongly connected components: a weakly connected balanced directed graph cannot have a nontrivial acyclic condensation with intercomponent edges. Thus a disconnected support admits no complete Euler word and has zero cofactor. The Eulerian Laplacian has both row and column sums zero, giving equal principal cofactors.

Fix a root `a` and temporarily label all parallel edges. The final outgoing edge at each nonroot vertex is an arborescence toward `a`; conversely, tree edges placed last in nonroot outgoing queues force a tour using all edges. The number of queue orders is `n_a! product_(i!=a)(n_i-1)!` per labelled arborescence. A fixed ordered vertex word has exactly `product_ij E_ij!` assignments of parallel-edge labels to its ordered occurrences. This remains true for a periodic word: its root position is retained, so no primitive-period division is permitted. Summing `n_a` over roots produces

`c(E)=m tau(E) product_i(n_i-1)! / product_ij E_ij!`.

Loops cancel from the Laplacian diagonal and remain in the queue factorials. For singleton support, the empty cofactor is one and the expression is `m(m-1)!/m!=1`. For disconnected support with two or more vertices, it is zero. These are correct edge cases, not removable negligible sets.

For `R_ij=E_ij/n_i`, the principal cofactor at root `a` is `tau(E)/product_(i!=a)n_i`. Their sum is `m tau(E)/product_i n_i`. The adjugate identity gives

`det(I-R+1 pi^T)=sum_a cofactor_a(I-R)`.

This is also valid when `I-R` has nullity greater than one: every cofactor and the rank-one perturbed determinant are then zero. Each stochastic cofactor is the probability that independent outgoing-neighbor choices at nonroot vertices form a tree to the root. Loops or functional directed cycles contribute zero. Consequently `0<=theta(E)<=r`, including reducible cases and `theta=1` for singleton support. Multiplying by the row multinomials yields (T2) exactly.

The bound controls one type's multiplicity. It does not bound the number of types, the aggregate row multinomials, or the oscillatory sum.

## 4. Periodicity, reversal, and overlap

An `a`-fold repeated word of type `E` is uniquely the repetition of a rooted word of type `E/a`. Thus primitive counts satisfy `c(E)=sum_(a|g(E))p(E/a)`, and Möbius inversion gives (P1). A rooted word with minimal period `d` has exactly `d`, not `m`, distinct rotations. Partitioning by `d=m/a` gives (P2).

Reversal sends type `E` to `E^T` while preserving occupation. It is a bijection, so `kappa(E)=kappa(E^T)`. For a fixed first word, its reverse-rotation orbit also contains exactly `d` words. Cyclic and reverse-cyclic pair sets intersect precisely when the first word is achiral. That intersection has `d` second words and necessarily `E=E^T`. Hence subtraction by `kappa` on the diagonal and transpose-diagonal, with addition of `alpha` on the diagonal, is exact inclusion-exclusion. (P5) is a nonnegative integer count; no pair is removed twice after the correction.

For reflection inversion, each primitive achiral word is fixed by one reflection. An `a`-fold repetition is fixed by `a` reflections, so `F(E)=sum_(a|g(E)) a a_prim(E/a)`. The Dirichlet inverse of `a` is `mu(a)a`, giving the stated formula. For the nonfaithful small dihedral actions at `m=1,2`, counting reflection parameters rather than distinct transformations gives the same formulas and the correct overlap.

The independent review checks actually enumerate ordered word pairs and compare the unmatched counts to (P5). This supplements the authored checker, which verifies the formula's nonnegativity and covariance reconstruction but does not itself enumerate the individual unmatched ordered pairs.

## 5. Fourier currents and sparse-support clarification

If `E,F` have equal row occupation, balance makes their column occupations equal as well. Therefore `Gamma=E-F` has zero row and column sums. Every nonzero term uses only nonzero matrix entries. Pair interchange gives `W_(m,-Gamma)=W_(m,Gamma)>=0`; separate left/right diagonal rephasing multiplies terms by one. Zero current occurs once and must remain.

The formal full `N x N` integer zero-row/zero-column lattice is generated by four-entry rectangles. If the support has zero entries, decomposition into rectangles can introduce entries outside that support. To interpret the resulting rectangle phase combinations, extend the undefined zero-entry phases arbitrarily; they cancel from the final supported current. Alternatively use supported bipartite cycle phases directly. The text should not imply that every supported current necessarily decomposes into rectangles containing only actual nonzero entries. This qualification does not change (F1)–(F2).

## 6. Exact assumptions, all-time summation, and plateau sign

The conditional reduction requires eventual constants independent of dimension:

`max P_ij<=C/N`, `||P-J||op<=gamma<1`, `||Q||op<=rho<1`.

No normality of `P` is required. Since `P` is doubly stochastic, constants reduce it and `P^m-J=(P-J)^m`; the trace error is bounded by `(N-1)gamma^m`. For `Q`, `|Tr Q^m|<=N rho^m`. The accepted actual odd-dimensional fixed-coupling results give precisely eventual entrywise flatness, a fixed `P` gap, and the stronger reverse conclusion `||Q||op→0`. The same-`P,Q` Hadamards have `||Q||op=1` and do not satisfy the reverse hypothesis.

A repeated word with proper period `d|m`, `d<=m/2`, has absolute total weight at most `N eta^(m-d)`. For the reverse contribution, use `|Q_ij|<=eta` and `sum_j|Q_ij|<=1`; the same estimate applies. Summing at most `m` divisor choices with discrepancy at most `m` proves (B1), including all repeated words. Reflection-fixed words have at most `floor(m/2)+1` free labels; the `m` reflection choices and weight at most `m` prove (B2).

For every fixed `s>0`, these are bounds on the complete sum `m>=1`, not only a compact microscopic band:

- `sum m N gamma^m` and `sum m N rho^m` are `O(N)`.
- `N sum_(m>=2) m^2 (C/N)^(m/2)` is `O_C(1)` eventually.
- The reflection bound is `O_C(1)` after splitting `m=2k` and `m=2k+1`: respectively its weights are at most `m^2 C^(2k)N^(1-k)` and `m^2 C^(2k+1)N^(-k)`.

All remain bounds after multiplication by `q^m<=1`. The leading term is exactly `sum m q^m=q/(1-q)^2`, so (B4) follows. The exact target is `q(1-q^N)/(1-q)^2`. Subtracting the removed ramp and dividing by `N^2` gives

`-q^(N+1)/(N^2(1-q)^2) → -exp(-2s)/(4s^2)`.

The negative plateau correction is compulsory; asserting that the whole current residual is small would contradict the target. No pointwise statement in `m` follows from this Abel equivalence.

At fixed `N`, complete the finite current sum before summing in degree. Since `S_m<=N^2` and `|R_m|,A_m<=C_m<=mN`, `|H_m|<=N^2+3mN` gives convergence for every `q<1`. This provides no absolute convergence over the uncompleted current weights.

### Near zero and the full tail

The accepted uniform phase-ensemble Abel bound gives, for the positive measure `mu_N=N^-2 sum S_m delta_(m/N)`,

`F_N(s)<=1/(2s)+1/(2N)`.

Consequently `limsup mu_N([0,epsilon])<=e epsilon`, by `s=1/(2epsilon)`, and

`integral_(t>R) exp(-2st) dmu_N <= exp(-sR) F_N(s/2)`.

These establish both endpoint tightness and a uniform exponential tail. They do not follow from convergence only on positive bands bounded away from zero.

For the signed current measure `nu_N=N^-2 sum H_m delta_(m/N)`, inclusion-exclusion gives pointwise `|H_m|<=S_m+3C_m`; the gap gives `C_m<=m+Nm gamma^m`. Therefore

`limsup |nu_N|([0,epsilon]) <= e epsilon + (3/2)epsilon^2`.

Its exponentially weighted tail has limiting upper bound

`exp(-sR)/s + 3 exp(-2sR)[R/(2s)+1/(4s^2)]`,

because the summed `Nm gamma^m/N^2` contribution is `O(1/N)`. This tends to zero as `R→infinity`. Thus no mass near zero or degree `m>N` is silently lost in the compact/Abel passage. One can also apply the cited positive-measure moment argument to `mu_N` and then subtract the controlled sectors, without treating the signed current weights as a positive measure.

The deterministic-source converse uses a smooth compact majorant that crosses frequency zero and the Fejer estimate. Its `a_0=N^2` term contributes exactly one after normalization; it must not be replaced by the CUE `min(0,N)=0`. The phase-ensemble bounds above provide a direct endpoint/tail route in the present setting. Neither route licenses vague convergence away from zero alone.

## 7. Computational audit, exact scope, and provenance

Every SHA-256 declared in the authored manifest's eight output entries and seven input entries matches the actual file. The pinned source-manifest hash also matches. No external manifest schema-validation claim was made or added.

The authored checker uses exact rational Gaussian arithmetic. Its fixture counts are `6+5+8+6+5+5=35`. Its permutation loop covers `sum_(m=1)^6 m!=873`, exactly. It compares all occupation-polynomial coefficients from principal-minor/hooks, rooted words, and Eulerian type counts; it includes all compositions of total edge count, not just a random sample. Its determinant-range test skips types with zero count, although the count itself is tested on those types.

The checker was copied without modifications into the review directory and replayed normally and with `-O`. All scientific output lines agree, all 35 rows agree with the authored JSON, and all 873 unrestricted marking checks pass. The replay writes only into the review directory. The authored historical caps and run receipt were inspected; they are not claimed as newly applied to the copied replay.

An independently authored standard-library review checker, without importing the original implementation, additionally checked:

- `N=2,m=1..6` and `N=3,m=1..4`: 246 rooted words, 127 balanced integer edge types, including 49 zero-count disconnected types with determinant zero;
- 2,024 ordered equal-occupation word pairs against the exact unmatched dihedral count;
- the `N=1,m=2` truncated-marking witness and repaired marking;
- direct exact `Q(i)` Hadamard amplitudes at `m=4`, obtaining `295/64` and `279/64`.

The same-`P,Q` discriminator establishes only finite exact non-identifiability of `S_4` or `H_4` as a function of `P,Q` alone. Its removable pieces agree, while its residuals differ by `1/4`. It is not an asymptotic universality counterexample, and it does not evaluate the actual BGS family.

The Whittle bibliographic entry is a priority/context remark, not a load-bearing imported theorem. No new external theorem or broader novelty/source search was required by this bounded audit.

Reproduction:

`PYTHONDONTWRITEBYTECODE=1 python3 independent_boundary_checks.py`

Review evidence is in `independent_check_results.json`, `independent_checks.log`, `replay_normal.json`, `replay_normal.log`, and `replay_optimized.log`. The copied checker is byte-identical to the authored `check_grouping.py`. The receipt records both reviewed target hashes and all declared input/output hashes.

## 8. First unresolved estimate and research value

The first unresolved phase-current estimate is the full signed weighted identity

`N^-2 sum_(m>=1) exp(-2sm/N) sum_Gamma W_(m,Gamma)(P_N) exp(i<Gamma,phi_N>)`
`→ -exp(-2s)/(4s^2)`, for every `s>0`,

for the actual phases of the actual unchanged family. A justified smaller-current reduction could replace this target only if its discarded contribution is controlled at the same scale. Neither stochastic determinant bounds, a positive Markov interpretation of the complex weights, nor fixed-current tests supply that estimate.

The regrouping adds genuine finite structural information: explicit repeated-edge multiplicities, a bounded scalar tree factor, exact periodic orbit sizes, once-counted reversal overlap, and nonnegative current coefficients. It fixes the required signed plateau magnitude and localizes where phase information enters. It is nevertheless an exact re-expression of `B_N(m)` and an equivalence of the original Abel identification. It proves no new dimension-uniform cancellation of arbitrary currents and does not close the balanced microscopic problem.

Strongest safe disposition: accept the finite equalities and the conditional controlled-sector reduction, insert the explicit zero-extension in the marking proof, qualify rectangular phases for sparse support, and retain (B5) as open. The cheapest next audit check is to incorporate the `N=1,m=2` truncation-bridge witness into the author's marking explanation or checker. No new exploratory route, repository modification, or publication is recommended by this bounded review.
