# Independent audit of the collective occupation hierarchy

Audit date: 6 October 2026. Read-only with respect to canonical BGS and the author route. The audit was performed in a fresh isolated reviewer context; it is an internal mathematical review, not an external referee certificate or formal proof.

## Verdict and normalized claim

**Primary verdict: correct only after a stated restriction.** State `N >= 2` for the finite-dimensional discussion, or at least for the assertion `A_(m,N) >= 1/N`. At `N=1`, every traceless diagonal space is zero and `A_(m,1)=0`, so that isolated lower bound is false for `m>=2`. If Section 4's `N>=20` is intended to govern that lower-bound sentence too, this is simply a scope clarification. This is the only correction identified. It has no effect on the actual unchanged odd-dimensional family, whose asymptotic application is through odd `N>=3`.

For `N>=2`, the exact identities and inequalities C1–C15 pass the reconstruction below. In particular, using the inherited FM-021 estimates for the actual unchanged family, for every fixed `b>0` and `epsilon>0`, uniformly for integer `2<=m<=bN`,

    S_(m,N)(U_N) = det_(D0)(I-T_N)^(-1) - 1
                  + O_(b,epsilon)(N^(-1+epsilon) + (2/3)^m).

Here `S` is exactly the orthogonally normalized trace on the specified Haar-removed, slot-conjugation-invariant diagonal collective hierarchy in the full ordered `End((C^N)^tensor m)`. It is not a trace on `End(Sym^m C^N)`, a projected spectral test, or the whole balanced space. The original `N^-2` compact-time aggregate is `O_w(N^-1)`.

The actual-family conclusion imports precisely two FM-021 estimates: eventual `||P_N-J||<=1/2` and `max_ab |U_N(a,b)|^2<=C/N`. This audit verifies their interface with the new proof; it does not re-certify the inherited analytic parametrix and oscillatory-kernel proof establishing them. No additional source-dependent analytic input is needed by the new hierarchy argument.

## 1. Frozen target, inputs, and dependency graph

The authoritative target is

- `bgs_weighted_plateau_route/collective_hierarchy.md`
- SHA-256 `8c68dacb6a9480c0805d8caf0d7b0af427be7bc7f767eaf1ab9c746e3aa7a8e0`

Its supplied source manifest is `collective_hierarchy_sources.json`, SHA-256 `2cd490915b803ab67789904cafce6545bfb17dbaaee19ee258b9aef453fdb3d0`. All eleven hashes in that manifest matched actual source bytes when frozen. The local canonical BGS checkout was clean at `801de3ab760cab4349e68b9843dcd67955314e62`. This is newer than some historical source base labels; file hashes, rather than those historical labels, bind this review.

`input_manifest.json` records the full frozen set, including instructions, status authorities, prior projection/source-control documents, the actual-model dependency closure, exact finite code/results, and the separately audited residual interface. Every file is copied under `frozen/` with its relative source path.

Load-bearing dependencies and roles:

1. Full ordered End-space tensor algebra, ordinary HS inner product, and Haar averaging as an orthogonal projector. These are reconstructed in Sections 2–3 below.
2. Elementary spectral diagonalization and symmetric-polynomial invariant theory. The precise rank implication is reconstructed below, rather than inferred from finite counts.
3. Elementary exponential/Gamma/Bernoulli concentration. All constants needed in C9 are checked below.
4. FM-021, `BGS/mathematics/position_chain_mixing.md`, SHA-256 `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`. Only its two stated actual-matrix estimates enter C12–C14. Its model source `fixed_map_path_model.md` is `d5365063f0967dabcac741a93c6f411d6402c913074944e1f9e383b2b5149b08`; its direct parametrix dependency is `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`. Existing review/receipt files are frozen as provenance, not treated as new proofs in this audit.
5. Standard finite-dimensional Schur–Weyl, hook-character, Schur-dimension and Kostka identities already used in the pinned project sources. Their exact normalization and application to C15 and the residual are reconstructed here. No growing-degree Haar trace CLT or stable-range approximation is imported.
6. The quadratic predecessor and FLOW-019/020/TRACE-014 provide history and boundary controls. They do not supply the new all-degree estimate by analogy.

Dependency chain:

    ordered support grading + Haar projection
      -> C1/C2 -> true Gram inverse -> C3 and exact dimension
    fourth moments + tensor-leg contraction
      -> C5, all q, no q<N condition
    invariant-polynomial restriction -> C6 rank
    conditional Haar-row overlap -> C9
      -> finite log-squared degree split -> C11
    actual FM-021 flatness + singular gap
      -> trace/HS determinant bound -> C12/C13
      -> C14 -> original N^-2 aggregate
    Schur central restriction -> C15 (finite exact representation)

There is no circular dependence on the desired asymptotic spectral law.

## 2. Ambient space, grading, action, and true Gram matrix

Write the local real Hermitian operator space as the orthogonal sum `R I ⊕ V0`, where `V0` is traceless Hermitian, then complexify for operator traces. The ordered m-fold tensor operator space splits orthogonally by subsets `S` of slots carrying `V0`; all other slots carry `I`. Each local diagonal coefficient in `D0` is traceless.

Conjugation by `U^tensor m`, and therefore its Haar average, preserves every support subset. Thus orthogonality between distinct subsets and distinct degrees survives Haar projection. For a symmetric local coefficient `B`, its insertions on the `binom(m,q)` subsets all have squared HS scale `N^(m-q)`. This gives exactly `L_(m,q)=binom(m,q)N^(m-q)`, with no extra `q!` or ordered-word multiplicity.

Let `i_q:Sym^q(D0)->Sym^q(V0)` be the inclusion and `A_q` the Haar projector on the latter. Compression of local conjugation to `D0` is the real bistochastic operator `T_U=P_U-J`. Consequently

    H_q = i_q* A_q i_q = E Sym^q(T_V),
    G_q = I-H_q.

This establishes positivity/self-adjointness of `H_q`; it does not presume that any individual `Sym^q(T_V)` is positive or normal. Since Haar-invariant operators are fixed by every actual conjugation, expanding both centered vectors yields exactly one net subtraction:

    Y*Y = L G_q,
    Y* Ad(U^tensor m) Y = L [Sym^q(T_U)-H_q].

In an arbitrary coefficient basis the compressed trace is the inverse metric times the bilinear matrix. In an orthonormal `Sym^q(D0)` basis this is exactly C3. Replacing `G_q^-1` by the identity would be wrong.

The slot action is `R_m(X)=C_m X C_m*`. It is not `X->C_m X`. Because collective tensors are invariant under conjugation by every slot permutation, `R_m Y=Y`; Haar projection commutes with those conjugations. Independently,

    Tr_End(R_m Ad(U^tensor m))
      = |Tr_W(C_m U^tensor m)|^2 = |Tr U^m|^2.

No symmetric-power restriction of `W` is used. Once C5 supplies injectivity, the hierarchy dimension is

    sum_(q=1)^m dim Sym^q(C^(N-1))
      = binom(N+m-1,m)-1.

These statements hold beyond `m=N` without a stable-degree assumption.

## 3. Uniform conditioning and exact rank

For a Haar row, the stated fourth moments give diagonal entries `2/(N+1)` and off-diagonal entries `1/(N+1)` in `E(P*P)`. Subtracting the constant projection and restricting to `D0` gives `E(T*T)=I/(N+1)`. The same calculation with columns gives `E(T T*)=I/(N+1)`. Every bistochastic `P` is an l2 contraction and constants reduce it, so `||T||<=1`.

For any vector in the full ordered local tensor space, move one tensor factor to the left in its quadratic form and retain a different factor on the right. All remaining factors are contractions. Cauchy–Schwarz over Haar measure then gives

    |E <v,T^tensor q v>| <= ||v||^2/(N+1),  q>=2.

Restriction to the symmetric local tensors is legitimate, and positivity of the averaged compression gives `0<=H_q<=I/(N+1)`. Thus `G_q>=N/(N+1) I`, uniformly in every integer degree `q>=2`. `H_1=0` separately. There is no conditioning singularity at `q=N`.

For the rank, invariant symmetric tensors on real `V0` identify with homogeneous conjugation-invariant polynomials. Restriction to diagonal matrices is injective because every Hermitian matrix is unitarily diagonalizable. The restriction is precisely a symmetric polynomial in N eigenvalues with zero sum. Conversely every such polynomial extends by the characteristic coefficients. Its graded algebra is freely generated in degrees `2,...,N`. The adjoint restriction has the same rank; since `H_q=i_q* A_q i_q`, its rank equals this restriction rank. Therefore

    rank H_q = [z^q] product_(j=2)^N (1-z^j)^(-1) <= p(q).

This argument concerns invariance under simultaneous conjugation of operator slots, not one-sided invariance of quantum vectors. The partition estimate follows from

    log product_(j>=1)(1-e^(-tj))^(-1)
      = sum_(k>=1) 1/[k(e^(tk)-1)] <= pi^2/(6t),

and optimizing `t`, which gives a constant strictly smaller than 3 in `exp(3 sqrt(q))`.

## 4. Generating function and Haar tail

For fixed N and `|z|<1`, the dominating sum of dimensions is `(1-|z|)^(-(N-1))`, so termwise Haar integration in C7 is justified. Coefficients `Tr H_q` are nonnegative. This is not uniform integrability at `z=1`.

At N=2 the scalar centered bistochastic entry is uniform on `[-1,1]`. Hence `H_(2k,2)=1/(2k+1)`, `H_(2k+1,2)=0`, and each even resolvent term is `1/(2k)`. C8 is exact and demonstrates that an infinite-degree negative-moment assertion cannot be substituted for C11.

The C9 constants check as follows:

- `Pr(1<=X<=2)=e^-1-e^-2>1/5`. A Bernoulli Chernoff half-mean bound gives failure probability at most `e^(-N/40)` for at least `N/10` successful coordinates.
- The exponential-sum upper tail at `2N` has exponent `1-log 2>1/4`, giving `e^(-N/4)`.
- Conditional on the first row u, the second row is uniform on the complex unit sphere in `u^perp`, of dimension `N-1`; no independent-row assumption is made.
- For the good coordinate set I, the subspace `C^I ∩ u^perp` has complex dimension `k>=|I|-1>=N/20` when `N>=20`. Its Gaussian squared norm is Gamma(k,1), regardless of its orientation or its dependence on u.
- The lower event `Gamma(k,1)>=N/40` follows from the half-mean tail with failure at most `e^(-k/8)<=e^(-N/160)`. The entire Gaussian squared norm is Gamma(N-1,1), whose upper tail at `2N` is bounded by `e^(-N/8)`.
- On the simultaneous event, `sum_I |v_j|^2>=1/80` and `sum_j |u_j|^2 |v_j|^2>=1/(160N)`. Dependence between numerator and denominator is harmless: only a union bound is used.

Each distinct row pair therefore fails with probability at most `4e^(-N/160)`; a union bound over at most N² ordered pairs gives C9. Diagonal row overlaps are always at least `1/N` by Cauchy–Schwarz. Hence `P P*=J/160+(159/160)R` with symmetric nonnegative bistochastic R. Its eigenvalues have modulus at most 1, and positivity of `P P*` gives the claimed centered singular bound `rho=sqrt(159/160)`. The displayed probability bound can exceed 1 for startup N; that does not invalidate it.

## 5. Finite-degree trace bound and actual determinant resummation

Since `H_q` is positive,

    Tr H_q <= r_N(q) min(1/(N+1), rho^q+4N²e^(-N/160)).

The second term bounds its norm using `||E Sym^q T||<=E||T||^q`; positivity is needed for trace-to-rank conversion. For `L=floor((epsilon log N/6)^2)`,

- degrees `q<=L` cost at most `L exp(3 sqrt(L))/(N+1)=O_epsilon(N^(-1+epsilon))`;
- the good-event tail is `sum_(q>L) exp(3 sqrt(q)+q log rho)`, bounded by `exp(-c_epsilon(log N)^2)` eventually, hence superpolynomially small;
- only degrees `q<=bN` are summed on the bad event, costing at most `4bN³ exp(3 sqrt(bN)-N/160)`, exponentially small.

Multiplication by `(N+1)/N` yields C11. Small N and small L are absorbed into the constant for fixed b and epsilon. Extending the bad-event sum to infinite degree would destroy the argument and is not done. The exact quadratic eigenvalue is `1/(N+1)`, contributing `1/N` to A for `N>=2`.

For the actual family, flatness gives both `||T_N||_HS²=sum P_ab²-1<=C` and `|Tr T_N|<=C+1`. The first-power trace needs this separate trace estimate; an operator-norm bound alone would introduce a factor N. For every `k>=2`, Schatten Cauchy–Schwarz gives

    |Tr T_N^k| <= ||T_N||_HS ||T_N^(k-1)||_HS
                 <= C 2^(-(k-2)).

This does not require normality. On `|z|=3/2`, the logarithmic determinant series therefore has uniformly bounded absolute value, for example by

    (3/2)(C+1) + 4C(log 4-3/4).

The chosen logarithm is the analytic branch at z=0; `||zT_N||<1` makes the determinant nonzero. Cauchy bounds every coefficient by a uniform constant times `(2/3)^q`. Evaluating the absolutely convergent series at z=1 proves C12, including its uniform exponential tail.

For C13, `H_q(I-H_q)^-1` is positive of rank `r_N(q)` and operator norm at most `1/N`. Therefore its product trace with the possibly nonnormal `Sym^q T_N` has absolute value at most `r_N(q)2^-q/N`. Summation is bounded by the finite partition product at z=1/2. This is a genuine rank estimate, not a bound using the exponentially larger full coefficient-space dimension.

Writing `G^-1=I+H(I-H)^-1` in C3 separates exactly the actual symmetric-power trace, its Gram correction, and the negative A term. C11–C13 give C14. Choosing, for example, epsilon=1/2 yields an N-uniform O(1) sector bound. For `supp w subset [a,b]`, `0<a<b`, there are O_w(N) relevant integers m, so

    |N^-2 sum_m w(m/N) S_(m,N)(U_N)| <= O_w(N^-1).

There is no division by replica dimension, no extra factor m, and no replacement of the actual U_N by Haar, metaplectic, noisy, or phase-averaged matrices. Haar measure is confined to the invariant Gram subtraction.

## 6. C15 and the exact orthogonal residual

For each content n, let `E_n` be the diagonal projector onto the full ordered-word weight space, of rank `M_n`. These projectors span the entire slot-conjugation-invariant diagonal space. Its orthonormal basis is `E_n/sqrt(M_n)`.

Under Schur–Weyl, the central invariant projector for lambda has norm `sqrt(f_lambda d_lambda)`. Its trace on the n-weight space is `f_lambda K_(lambda,n)`. Since it commutes with slot permutations, its diagonal entry is constant on each ordered-word content class. The inner product of these two normalized objects is exactly C15:

    R_(n,lambda)=sqrt(f_lambda/d_lambda) K_(lambda,n)/sqrt(M_n).

Haar projection of a slot-conjugation-invariant operator lies in the center of the permutation commutant. Thus the occupation compression is `R R*`; its nonzero spectrum equals that of `R*R`. The orthogonal degree decomposition already proved identifies it with `H_0=1`, `H_1=0`, and all `H_q` through m. C5 makes the eigenvalue 1 simple. The normalized constant vector on the Schur side is `sqrt(f_lambda d_lambda/N^m)`, by the decomposition of the identity. This establishes C15 with full finite-N cutoff and no stable-range approximation.

The separately supplied `collective_residual_interface.md`, SHA-256 `c4b47fd176673c56824e924218a21158343652020c70fdcf500f3803d02dc139`, also passes. Let `P_coll` be the orthogonal projector on the centered hierarchy and Pi the equal-content ket/bra projector. Then

    P_H P_coll=0,     P_H+P_coll<=Pi,
    Q=I-P_H-P_coll=(Pi-P_H-P_coll)+(I-Pi).

Both summands are orthogonal projectors. These projections commute with the two-sided cycle R. No commutation with actual `C_U` is assumed. The Haar-invariant space is `direct sum_lambda End(Specht_lambda)`; cycle conjugation has trace `sum_lambda |chi_lambda(c_m)|²`. Only hooks contribute and their permitted lengths give exactly `min(m,N)`. Since `C_U` is identity on this invariant space,

    |Tr U^m|² = min(m,N) + S_(m,N)(U) + Tr(R Q C_U).

The ranks are exactly

    rank P_H = sum_(lambda partition m, length<=N) f_lambda²,
    rank P_coll = binom(N+m-1,m)-1,
    rank Q = N^(2m) - rank P_H - rank P_coll,
    rank Pi = sum_(|n|=m) M_n²,
    rank(Pi-P_H-P_coll) = rank Pi-rank P_H-rank P_coll,
    rank(I-Pi) = N^(2m)-rank Pi.

The complement contains other cycle-fixed vectors. At m=1, every off-diagonal matrix is in Q while R is the identity. Therefore it is incorrect to relabel the whole complement as only nontrivial permutation sectors. The exact projector formulas, rather than such a slogan, describe what has actually been removed. No identification with stationary-label path masks or low-energy K spectral projectors is proved.

## 7. Obligation matrix

| Obligation | Status | Decisive check |
| --- | --- | --- |
| Full ordered End-space and two-sided cycle | Passed | Tensor trace identity and direct finite cycle matrices |
| Support and degree orthogonality after Haar | Passed | `CI ⊕ V0` grading preserved per slot |
| Exact subtraction, true Gram, dimension | Passed | C2 derivation, positive G, stars-and-bars |
| All-degree Gram conditioning | Passed | Two tensor legs plus exact row/column fourth moments |
| Invariant rank and partitions | Passed | Spectral restriction and degrees 2 through N |
| C7 and N=2 infinite-degree failure | Passed | Absolute convergence below 1 and scalar exact integral |
| Conditional Haar-row concentration | Passed | Conditioned complex dimension N-1; intersection rank at least N/20 |
| q<=bN logarithm-squared split | Passed | Bad-event sum is finite; good tail superpolynomial |
| Lower bound A>=1/N at N=1 | Failed if included | D0=0, A=0; state N>=2 |
| Actual symmetric-power determinant | Passed relative to FM-021 | Both first trace and HS bound retained; nonnormal estimate valid |
| Original N^-2 normalization | Passed | O(N) time samples times O(1) sector contribution |
| C15 finite Kostka representation | Passed | Normalized central weight-space overlap and independent exact matrix tests |
| Exact remaining orthogonal complement | Passed | Orthogonal projector subtraction and exact ranks |
| Re-proof of inherited FM-021 analytic chain | Not addressed | Hash-pinned named project input, not a new certification |
| Full balanced trace, complete complement, higher factorial orders, BGS | Out of scope | No estimate for `Tr(R Q C_U)` |

## 8. Executed finite controls and provenance

`checks/ordered_space_check.py` independently constructs actual ordered-word slot-permutation operators and their central class sums. Exact Gram inversion gives Haar compression without using Kostka to construct it. It checks the full degree decomposition, PSD of H, exact bound H<=I/(N+1), ranks r_N(q), N=2 scalar controls, invertibility of every centered Gram, and agreement of the full characteristic polynomial with C15. The exact range is

- N=2, m=1,...,5;
- N=3, m=1,...,4;
- N=4, m=2,3.

`checks/actual_trace_check.py` directly builds centered operator matrices, their ordinary HS Gram matrices, and actual conjugation by products of rational Householder unitaries. It independently constructs the symmetric-power action by polynomial substitution. It checks C2/C3, the quadratic formula, the same cycle on both sides, the invariant contribution min(m,N), and complement ranks for N=2, m=1,...,4 and N=3, m=1,...,3. The N=3 bistochastic examples are nonnormal, so the test does not silently reduce every case to a symmetric matrix.

The frozen author `kostka_resolvent.py` uses exact rational Schur/Kostka matrices. Its horizontal-strip recursion, hooks, orbit multiplicities, rational similarity, and removal of the one constant direction were inspected. All 36 rows for N=3,5,7,9 and m=2,...,10 reproduce exactly against the frozen output. This larger range is replayed author evidence; the smaller permutation-operator tests are a genuinely different construction. Neither finite range proves C11 or any asymptotic theorem.

The consolidated rerun and machine-checkable provenance are in `checks/provenance_run/`, produced by the installed computation-audit bounded runner using `checks/contract.json`. It records input hashes before/after, software, exact arguments, results, elapsed time and effective caps: 90 seconds wall time, 1 GiB per-process virtual memory, 60 seconds per-process CPU, one core, one cooperative numerical-library thread, and 1 MiB combined logs. The main input/operator tests are exact integer/rational; NumPy is used only for bounded integer permutation-Gram products, with maximal possible entries safely below signed 64-bit overflow. No random sampling occurs. The run is validated with the skill's manifest validator and root hash checks.

## 9. Remaining implication and safe next use

There is no missing implication in the stated new analytic sector argument for N>=2. Correct or clarify the isolated lower-dimensional bound, then the safe result is an actual-U signed trace estimate for this entire diagonal collective hierarchy through every fixed Heisenberg band.

The exact unresolved pair target is the original N^-2 weighted trace on Q. Neither small Haar operator norms, the finite Kostka data, the hierarchy's large dimension, nor actual position-chain mixing alone bounds it. The cheapest logically necessary continuation is to specify and estimate a genuinely additional portion of `Pi-P_H-P_coll` or `I-Pi` while retaining its actual cyclic trace and projector normalization. Merely increasing the finite Kostka cap does not close that implication.

## Accepted domain-only v2

The separate [confirmation](history/2026/collective_20261006/v2_confirmation.md)
accepts exactly the added N>=2 qualification, with no other source change.
The original review and source bytes remain immutable in the promotion map.
Portable execution uses explicit failures under optimization and stdout output;
exact mathematical fields are compared with all independent frozen outputs.
The separate numerical diagnostics remain explicitly floating controls.
