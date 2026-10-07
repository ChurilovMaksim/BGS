# Hook cancellation, Eulerian types, and the exact phase-current remainder

Date: 7 October 2026. Status: **exact finite-dimensional lemma, self-reviewed; independent exact implementations agree in the bounded ranges below. The balanced microscopic identification remains open.**

Read-only input: `/workspace/shared/bgs_checked_checkpoint_validation/source_snapshot`.
Its external source manifest SHA-256 is
`d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba`.
All new files are confined to `/workspace/shared/bgs_wave2_hook_identity`.

## Result and scope

The full signed growing-degree hook covariance can be reorganized in three exact steps:

1. A marked Koszul/cycle-selection identity cancels every disconnected permutation-cycle configuration **before any absolute value or phase average**. This includes the top exterior-power sector responsible for the artificial `N^2 q^N Z_B(q)` term.
2. The surviving connected coefficients have an explicit directed-tree formula on **edge occupation matrices**, retaining every repeated coordinate, repeated edge and periodic word. Their combinatorial coefficient is a product of row multinomials times a scalar determinant in `[0, |supp n|]`.
3. Cyclic and reverse-cyclic pairs, with exact periodicity and overlap corrections, can be removed. The remaining expression is a Fourier sum with nonnegative weights over **integer edge currents with zero row and column sums**. Thus its oscillation depends only on actual gauge-invariant entry phases, not on unexpanded hook covariances.

Under the existing `P` gap, reverse `Q` gap and entrywise flatness hypotheses, the removed part contributes the full ramp `1/(4s^2)`. Therefore the residual current sum must converge to

`-exp(-2s)/(4s^2)`

after Abel summation and `N^-2` normalization. Showing that residual is small would be wrong: it must supply the plateau correction.

This is a concrete algebraic input and a compressed phase-sensitive target, **not** an estimate of that target. In particular the tree factor bound is not a bound on the absolute current sum. No priority claim is made for Koszul exactness, cycle indices, last-exit trees, or the underlying BEST/Markov-type enumeration.

## 1. Definitions and exact contract

Let `U` be an `N x N` unitary, `D=diag(d_1,...,d_N)` with independent Haar circle variables, and `m>=1` an integer with no restriction relative to `N`. Put

`lambda_(m,k)=(m-k,1^k)`, `0<=k<min(m,N)`.

The object to reorganize is

`S_m(U)=sum_(k,l) (-1)^(k+l) E[s_lambda(m,k)(DU) conjugate(s_lambda(m,l)(DU))]`.

Use `U_ij` for the directed edge `i -> j`; a rooted closed word is the ordered tuple `w=(i_1,...,i_m)`, with `i_(m+1)=i_1`. Its amplitude is

`a_U(w)=product_(t=1)^m U_(i_t,i_(t+1))`.

For a nonnegative integer matrix `E=(E_ij)`, let `|E|=sum E_ij`. Define the finite Eulerian-type set

`E_m={E>=0 integral: |E|=m, sum_j E_ij=sum_j E_ji=:n_i}`.

Write `S={i:n_i>0}`, `r=|S|`, and define `U^E=product_ij U_ij^E_ij`, with `0^0=1`. Matrices outside the positive support are harmless zeros. All products and sums at a fixed `m` are finite.

The new theorem will express `S_m` solely through `E_m`, its rooted-tree cofactors, periodicity divisors, and entry phases. There is no replacement of trace products by Hilbert--Schmidt norms.

## 2. What the Koszul complex actually cancels

For a complex vector space `V=C^N`, at total degree `m` use

`C_j=Sym^(m-j)(V) tensor exterior^j(V)`, `0<=j<=min(m,N)`.

The differentials

`d=sum_i x_i contraction_(e_i*)`,
`delta=sum_i partial_(x_i) exterior_multiplication_(e_i)`

satisfy `d delta + delta d=m I`. These operators are basis-independent and equivariant for linear maps of `V`. Hence the complex is exact for `m>0`.

Its hook kernels give the character identity

`Tr(C_j(A))=h_(m-j)(A)e_j(A)=s_(m-j,1^j)(A)+s_(m-j+1,1^(j-1))(A)`,

with nonexistent endpoint hooks zero. Equivalently this follows directly from the elementary hook Jacobi--Trudi formula; no irreducible decomposition is needed for the subsequent proof. Telescoping gives

`sum_k (-1)^k s_(m-k,1^k)(A)`
` = sum_(j=1)^min(m,N) (-1)^(j-1) j e_j(A)h_(m-j)(A)`.       (K1)

Exactness alone only proves the *unweighted* alternating trace is zero. It does not make (K1) zero, small, or governed by a one-particle gap: the exterior-number insertion `j` does not commute with the differential. This is the first missing implication in a bare “Koszul localization gives universality” argument.

There is nevertheless a useful explicit cancellation. Expand the right side of (K1) using the symmetric/exterior cycle indices. For any permutation of the `m` abstract slots with cycle lengths `ell_1,...,ell_c`, choose which cycles are assigned to the exterior factor. Its marked signed weight is

`sum_(F subset {1,...,c}) (-1)^(|F|+1) sum_(a in F) ell_a`
` = m` if `c=1`, and `=0` if `c>=2`.                       (K2)

Indeed, mark a particular cycle `a` and sum over the other cycles: its contribution is `ell_a (1-1)^(c-1)`. Thus all configurations with two or more permutation cycles cancel exactly. Only single cycles remain, and (K1) equals `Tr(A^m)`.

This argument is on abstract slots, **before assigning site labels**. Equal site labels therefore do not spoil it. It may be applied independently to the retarded and advanced copies before their phase pairing. Consequently

`S_m(U)=sum_(n:sum n_i=m) |sum_(E in E_m, row E=n) c(E) U^E|^2`,          (K3)

where `c(E)` is the number of rooted closed words with edge counts `E`.

### The compulsory top-fermion cancellation

The `j=l=N` term in the square of (K1), when `m>=N`, is

`N^2 E |e_N(DU) h_(m-N)(DU)|^2=N^2 E |h_(m-N)(DU)|^2`.

Its Abel sum is exactly `N^2 q^N Z_B,U(q)`, the top compact sector in the pinned frontier note. Equation (K2) cancels its disconnected-cycle configurations together with the other exterior choices at each finite degree. No bound on that sector is used. The result is (K3), not a sum of absolute exterior-sector estimates.

For illustration, the exact check for `U=I_3`, `m=5` has top-sector value `54` and completed value `3`. This is a finite cancellation control, not a replacement for the Haar `N^3` comparison in the source note.

## 3. A directed-tree formula for every repeated occupation

Let `L_E=diag(n_i)_(i in S)-E_(S,S)`. All its principal cofactors agree because `E` is Eulerian. Call their common value `tau(E)`; for `r=1`, use the empty cofactor `tau(E)=1`. If the support is disconnected, the cofactor is zero. Then

`c(E)=m tau(E) [product_(i in S)(n_i-1)!] / [product_ij E_ij!]`.        (T1)

In particular this rational-looking expression is a nonnegative integer.

### Proof, including loops and repeated edges

Temporarily label each of the `E_ij` parallel edges individually. Fix a starting vertex `a`. The last departure edge at each vertex other than `a` forms a directed arborescence toward `a`: a directed cycle of last departures would prevent the walk from finally leaving that cycle and returning to `a`.

Conversely choose such a last-exit arborescence, order the outgoing edges at each vertex with its tree edge last when `i!=a`, and follow the resulting queues from `a`. The walk cannot become trapped before all edges are used: balance plus the still-unused tree edges would provide an exit toward `a`. This gives a bijection.

For each arborescence there are `n_a! product_(i!=a)(n_i-1)!` queue orders. Thus the number of labelled-edge tours beginning at `a` is

`tau(E) n_a product_i(n_i-1)!`.

Every rooted *vertex* word has exactly `product E_ij!` ways of assigning the parallel edge labels to its ordered uses, even when the word is periodic. Divide by this number and sum over `a`; `sum_a n_a=m` proves (T1). No division by a presumed primitive period is made.

Loops contribute to the factorials but cancel from the Laplacian diagonal, as they should. When the support has one vertex the formula gives `c(E)=1` for every `m`; discarding repeated occupations would fail this case immediately.

### A bounded stochastic determinant, not a high-degree representation block

On `S`, put

`R_E(i,j)=E_ij/n_i`, `pi_E(i)=n_i/m`.

Then `R_E` is stochastic and `pi_E` is stationary. Define

`theta(E)=det(I-R_E+1 pi_E^T)`.

The equivalent formula is

`c(E)=theta(E) product_(i in S) [n_i! / product_j E_ij!]`,
`0<=theta(E)<=r<=min(m,N)`.                                (T2)

To verify this, each principal cofactor of `I-R_E` is

`tau(E)/product_(i!=a)n_i`.

Their sum is `m tau(E)/product_i n_i`, which is the rank-one-perturbed determinant above. For a stochastic matrix each such cofactor is at most one: choose one outgoing neighbor independently at every nonroot vertex; the cofactor is exactly the probability that these choices form a tree to the root. Thus their sum lies in `[0,r]`.

For completeness, the tree/cofactor assertion follows by writing a Laplacian row as `sum_j R_ij(e_i-e_j)` and expanding the determinant multilinearly. A selected functional digraph with a directed cycle has determinant zero, while a tree oriented toward the removed root has determinant one after a leaf ordering. This supplies the needed matrix-tree identity without importing an unverified theorem.

The rank-one determinant identity follows from the adjugate formula. If `I-R_E` has nullity one, its adjugate is a scalar multiple of `1 pi_E^T`; if it has larger nullity both the adjugate and the rank-one-perturbed determinant vanish.

The simplification is exact: factorially many Euler tours of a fixed transition type have been summed, and their remaining multiplicity is one cofactor of order at most `N-1`, or one scalar determinant of order at most `N`. It does **not** say that the remaining number of types, the row multinomials, or their phase-weighted total is small.

## 4. Remove the controlled cyclic and reversed sectors exactly

Let `g(E)` be the gcd of the entries of `E`, including zeros in the usual gcd convention; `g(E)>=1` for `|E|>0`. The number of rooted words of edge type `E` with primitive period `m` is

`p(E)=sum_(a|g(E)) mu(a)c(E/a)`,                            (P1)

where `mu` is the integer Möbius function. This is inclusion-exclusion over proper repetition. The number of ordered pairs of words of type `E` related by a cyclic rotation is

`kappa(E)=sum_(a|g(E)) (m/a) p(E/a)`.                       (P2)

A word of minimal period `m/a` has exactly `m/a` distinct rotations. These formulas retain all periodic words; replacing `kappa(E)` by `m c(E)` is incorrect.

Call a word *achiral* when its reversal is one of its rotations, and let

`alpha(E)=sum_(w of type E, achiral) minimal_period(w)`.     (P3)

It is zero unless `E=E^T`. This finite overlap can be computed by reflection-fixed words, rather than by treating all paired paths independently. An exact arithmetic version is available if desired: let `F(E)` be the sum, over the `m` reflections, of the number of words of edge type `E` fixed by that reflection; then

`a_prim(E)=sum_(a|g(E)) mu(a) a F(E/a)`,
`alpha(E)=sum_(a|g(E)) (m/a) a_prim(E/a)`.

A primitive achiral word is fixed by exactly one reflection; its `a`-fold repetition is fixed by exactly `a` reflections. This proves the displayed inversion. The bounded checker computes (P3) directly and separately checks the reflection inversion against it.

Set

`P_ij=|U_ij|^2`, `Q_ij=U_ij conjugate(U_ji)`.

Define the three explicitly removable pieces

`C_m=sum_E kappa(E) P^E`,
`R_m=sum_E kappa(E) Q^E`,
`A_m=sum_E alpha(E) P^E`.                                  (P4)

Here `C_m` is cyclic, `R_m` is reverse-cyclic, and `A_m` is their intersection. For `E,F` with the same row sums define

`t(E,F)=c(E)c(F) - 1_(E=F) kappa(E)`
`        - 1_(F=E^T) kappa(E) + 1_(E=F) alpha(E)`.          (P5)

Then `t(E,F)` is a **nonnegative integer**: it counts exactly the ordered word pairs with these edge types that are related by neither a cyclic rotation nor a reversal followed by a rotation. Inclusion-exclusion proves this even in the repeated/achiral cases.

The exact grouped identity is

`S_m(U)=C_m+R_m-A_m+H_m(U)`,

`H_m(U)=sum_(E,F in E_m, row E=row F) t(E,F) U^E conjugate(U^F)`.       (P6)

This does not estimate each compact sector and does not replace a trace product by a Hilbert--Schmidt norm. The exterior sectors have already canceled in (K2), and (P5) then removes the two controlled path equivalences *once*, including their exact intersection.

## 5. The remaining signs are actual rectangular phase currents

Write `U_ij=sqrt(P_ij) exp(i phi_ij)` on its nonzero entries. A zero entry kills every term using it, so its phase need not be defined. In (P6) set

`Gamma=E-F`.

Both its row sums and its column sums are zero. Define

`W_(m,Gamma)(P)=sum_(E-F=Gamma, row E=row F)`
`                t(E,F) product_ij P_ij^((E_ij+F_ij)/2)`.    (F1)

Thus `W>=0`, `W_(m,-Gamma)=W_(m,Gamma)`, and

`H_m(U)=sum_Gamma W_(m,Gamma)(P) exp(i sum_ij Gamma_ij phi_ij)`.         (F2)

Equivalently pair `Gamma` and `-Gamma` into cosines, keeping `Gamma=0` once. This is a concrete Fourier sum over the integer cycle lattice of the bipartite row/column graph. Its phases are invariant under separate left and right diagonal rephasing of `U`. Every integer matrix with zero row and column sums is generated by rectangular four-entry currents, so only gauge-invariant rectangular entry-phase combinations are needed.

The zero-current part must remain. Distinct Euler tours with identical transition counts already make `t(E,E)>0` at small sizes. It is a genuine coherent contribution, not an error due to repeated occupations. The exact `N=2,m=6` test has

`W_(6,0)=382205952/244140625 > 0`,
`H_6=-1018331136/244140625 < 0`.

Therefore nonzero currents have to cancel a positive same-edge-type contribution even in this tiny exact example. Bounding their absolute sum cannot capture that mechanism.

## 6. Quantitative reduction using the accepted P/Q inputs

Assume `eta=max_ij P_ij<1`. Since `P` is doubly stochastic, and `|Q_ij|=sqrt(P_ij P_ji)` has row sums at most one, periodic words give the rigorous bounds, for `m>=2`,

`0 <= m Tr(P^m)-C_m <= m^2 N eta^(m/2)`,
`|m Tr(Q^m)-R_m| <= m^2 N eta^(m/2)`.                       (B1)

For `m=1` these differences vanish. Proof: a proper repetition has period `d|m`, `d<=m/2`; its total absolute weight is bounded by

`Tr[(P^(entrywise m/d))^d] <= N eta^(m-d)`

for the cyclic part, and the same row-sum argument with `|Q|` works for the reverse part. Each discrepancy is at most `m` per rooted word, and there are at most `m` divisor choices. This overcounts safely and does not assert primitive words dominate without a bound.

A word fixed by a reflection has at most `floor(m/2)+1` free site labels. There are `m` reflections and each achiral word contributes at most `m` to (P3). Therefore

`0<=A_m<=m^2 N^(floor(m/2)+1) eta^m`.                      (B2)

This bound is deliberately rough but adequate for the full Abel transform, including small powers.

Now suppose along a sequence of dimensions

`eta_N<=C/N`, `||P_N-J_N||<=gamma<1`, `||Q_N||<=rho<1`        (B3)

for fixed constants eventually. The actual accepted hypotheses are stronger than the last requirement because `||Q_N|| -> 0`.

Since `P J=J P=J`,

`|Tr(P^m)-1| <= (N-1) gamma^m`,
`|Tr(Q^m)| <= N rho^m`.

Summing (B1)-(B2), with `q=exp(-2s/N)`, proves for every fixed `s>0`

`N^-2 sum_(m>=1) q^m [C_m+R_m-A_m] -> 1/(4s^2)`.          (B4)

In more detail: the gap errors have absolute sums `O(N)`; the periodic corrections have absolute sums `O_C(1)` because
`N sum_(m>=2) m^2(C/N)^(m/2)=O_C(1)`; and (B2), split into even and odd powers, also has total sum `O_C(1)`. The sole leading term is `sum_m m q^m=q/(1-q)^2`.

The exact Haar benchmark is

`sum_m q^m min(m,N)=q(1-q^N)/(1-q)^2`.

It follows that, under (B3), the original balanced Abel identification is **equivalent** to

`N^-2 sum_(m>=1) exp(-2sm/N) H_m(U_N)`
`       -> -exp(-2s)/(4s^2)` for every `s>0`.               (B5)

The fixed-degree target is correspondingly the signed plateau correction `-(m-N)_+`, after summing on the microscopic scale; no pointwise-in-`m` asymptotic is asserted.

The Abel series in (B5) is interpreted by completing each finite-degree current sum first. It converges for each fixed `N`: (P6), `S_m<=N^2`, and `|R_m|, A_m<=C_m<=mN` give `|H_m|<=N^2+3mN`. There is **no** assertion that the double series of absolute current weights converges at a microscopic radius.

## 7. Exact discriminator and computational scope

`check_grouping.py` uses `fractions.Fraction` and a small explicit Gaussian-rational class. It has three independent constructions:

1. principal-minor determinants, complete-symmetric recursion, and hook Jacobi--Trudi polynomials;
2. direct enumeration of all rooted words, their occupation vectors, primitive periods and dihedral overlaps;
3. enumeration of every nonnegative edge matrix of total `m`, row/column balance, Laplacian cofactors, and the Möbius formulas (T1), (P1)-(P2).

It checks the *complete multivariate phase coefficient polynomials*, not only their final squared norms. It also checks the stochastic determinant in (T2), the nonnegative residual counts (P5), the full covariance split, the reflection inversion for the overlap, and cycle-selection identity (K2) on every permutation through degree six.

The input families are:

- `N=1`, `U=i`, powers 1 through 6;
- `N=3`, `U=I`, powers 1 through 5, exposing large top-fermion cancellation;
- the rational 2-by-2 rotation with rows `(3/5,4/5)` and `(-4/5,3/5)`, powers 1 through 8;
- an explicit three-Givens complex rational unitary, powers 1 through 6;
- each of the following two 4-by-4 Hadamards, powers 1 through 5.

For `|a|=1`, let

`U(a)=1/2 [[1,1,1,1], [1,a,-1,-a], [1,-1,1,-1], [1,-a,-1,a]]`.

It is symmetric and unitary; hence for both `a=1` and `a=i`,

`P=Q=J_4` exactly.

Nevertheless the complete exact computations give

`S_4(U(1))=295/64`, `S_4(U(i))=279/64`,
`H_4(U(1))=-9/8`, `H_4(U(i))=-11/8`.

Their removable pieces agree: `C_4=R_4=247/64`, `A_4=127/64`. Thus a replacement of the phase-current sum by a function of `P,Q` alone fails already here. These matrices have `||Q||=1`; they are **not** an asymptotic counterexample under the actual reverse-gap assumptions.

Run:

`python3 /workspace/shared/bgs_wave2_hook_identity/check_grouping.py`

The script writes `check_results.json`; `check_run.log` preserves the normal run. Exact checked ranges, interpreter version, script checksum, source-manifest checksum and elapsed execution time are in that JSON. Bounded exact agreement tests the identity and its implementation; the all-`N,m` justification is the proof above, and no finite extrapolation is used.

## 8. Research disposition and first missing implication

The natural Koszul route was executed: its equivariant contraction cancels unmarked Euler characteristics, but the required marked character is an Adams operation, so no gap estimate follows. The first uncertain implication there is false as a general principle: acyclicity does not control the weighted character covariance.

The scalar Schur-complement/martingale route was checked against the pinned corpus and **already exists** in `mathematics/balanced_pair_schur_reduction.md`; it is not claimed here as a new route or result.

The second executed regrouping is (K2), (T1)-(T2), (P5)-(F2), with the quantitative controlled-sector removal (B4). It leaves the explicit current target (B5). The next mathematical input must estimate that full weighted oscillatory sum for the actual phases, or establish a justified reduction of it to a smaller class of currents. The scalar determinant bound `theta(E)<=r` supplies exact multiplicity control but does not justify taking absolute values in (F2). The diagonal current is positive; the required limit is negative.

In particular, the following steps remain **unproved**:

- a dimension-uniform comparison of the complete weights/phase sum in (F2) to its CUE counterpart at `m` of order `N`;
- concentration of the empirical stochastic matrices `R_E` under the complex amplitude weights near the original `P` (these are not a positive Markov sampling law);
- propagation of the initial `P/Q` estimates to unrestricted phase currents or higher rectangular coherences;
- control by a fixed number of current/encounter classes at the plateau scale.

No claim is made that tree enumeration alone solves any of these. What has changed is the exact algebraic object on which a phase estimate would act: compulsory exterior-sector cancellations and once-counted cyclic/reverse subtractions are completed, repeated occupations are explicit, and the residual's necessary sign and Abel magnitude are fixed.

### Provenance / sources

Load-bearing inputs from the checked snapshot are the definitions and target in `mathematics/compact_phase_pair_identity.md`, `mathematics/complex_microscopic_phase_source_bounds.md`, and `evidence/research_checkpoint_20261007/raw/bgs_astra_corrected_integral/frontier/exact_identification_target.md`. The existing Schur route and its boundary are credited above. No new external analytic theorem is invoked.

The enumeration mechanism is classical. A narrow bibliographic check located P. Whittle, *Some Distribution and Moment Formulae for the Markov Chain*, JRSS B 17 (1955), 235–242, DOI `10.1111/j.2517-6161.1955.tb00197.x`, whose original-paper record identifies its transition-total formula (8): <https://academic.oup.com/jrsssb/article/17/2/235/7026736>. The full theorem is not imported from that abstract; the specific closed-word normalization, loop conventions and periodic-word factors used here were proved directly above. No broad novelty search was performed.
