# Independent audit: entire centered pair-quadratic occupation sector

Date: 6 October 2026. Audit only; no candidate or canonical source edits.

## Normalized claim and primary verdict

**Proved as written.** For every integer N>=3, every m>=2, and every
U in U(N), the true orthogonal projector onto the full-Haar-removed
collective pair-quadratic sector in End((C^N)^(tensor m)) has trace

    Tr(R_m P_quad Ad(U^(tensor m)))
      = ((Tr T)^2+Tr(T^2))/2 + ||T||_HS^2/[N(N-1)] - 1/N,

where T=(|U|^2-J)|_(1-perp) and R_m is conjugation by the SAME slot cycle
on ket and bra. The proof covers m>N without modification. The stated
odd-N metaplectic source singular spectrum is correct, including N=3 and
odd composite N. The maintained actual-flatness input yields the stated
O(1) trace and O_w(N^-1) normalized aggregate at literal tau=10^-80.

Audited statements:

- report.md SHA256
  ff310670a6ccc467ca2f910b68279ae1e5f099559a5c1ecef5009a4d62cc20f7
- cycle_interface.md SHA256
  dcd43142cc2bd284b699d591fcdfd36a6b5d9bfa5069b5036ec3f54fe50d3666

Both are under
/workspace/shared/bgs_weighted_plateau_independent/quadratic_sector/.
This is an independent derivation and implementation, not the candidate's
self-review. Numerical controls support finite identities only.

## Claim card and exact boundary

The coefficient space is the complexification of Sym^2 D_0, where D_0 is
the real Hilbert space of traceless diagonal N-by-N matrices. The domain
metric before Haar removal is ordinary two-copy Hilbert--Schmidt. The
ambient space remains the full ordered tensor operator space of dimension
N^(2m), with ordinary unnormalized Hilbert--Schmidt metric. The sector
dimension is N(N-1)/2. The projector uses the inverse of the full induced
Gram matrix, rather than an unnormalized frame sum.

"Pair-quadratic" means the image of the two-slot centered coefficient
space, after full collective Haar subtraction. "Degree at most two"
additionally includes the orthogonal additive traceless occupation sector
of dimension N-1; its trace is Tr T. The raw constants vanish under Haar
subtraction. These are different statements, both correctly distinguished
in the candidate. Neither sector is the whole balanced occupation space.
Neither has been shown to be a K_m-invariant spectral subspace, so no
spectral cutoff, all-degree memory closure, or full signed trace follows.

## Dependency graph

1. Full ordered tensor definition and ordinary HS metric -> distinct
   zero-partial-trace pair insertions are orthogonal.
2. Elementary two-copy unitary commutant -> exact local Haar twirl.
3. Identity spectators and linearity of the twirl -> FULL collective Haar
   subtraction, with no assumption m<=N.
4. The two preceding facts -> positive Gram matrix G, injectivity, and
   true projector F G^-1 F^*.
5. Local compression of Ad U to D_0 -> Sym^2 T block, corrected by the
   fixed Haar component -> exact sector trace.
6. Collective slot symmetry and same-cycle conjugation -> cyclic insertion
   acts identically on the sector; full ambient trace is |Tr U^m|^2.
7. Actual four-branch finite-shift parametrix -> max |U_ij|^2<=C/N ->
   elementary trace bounds -> O(1) and O_w(N^-1).
8. Literal odd-N metaplectic chirp -> nonzero invertible Fourier shifts ->
   two-slot balanced source Gram -> true-metric source singular spectrum.
9. Self-adjoint H_m and unitary spectral theorem -> stated Duhamel bound.

Items 1--6 and 8--9 are exact algebra/finite-dimensional functional
calculus. Item 7 uses the expressly identified maintained analytic input;
no mixing-gap estimate, noisified model, or rescaled-time numerical test is
needed for this sector theorem.

## Reconstructed decisive algebra

### Full Haar correction and every m>=2

Let b=binomial(m,2), d=N-1, and let r=sum_alpha D_alpha tensor D_alpha.
Every A in Sym^2 D_0 has zero partial traces. For two different slot pairs,
there is a slot occurring in only one of them; tracing that slot kills
their inner product. Consequently

    J_m^* J_m = b N^(m-2) I.

For completeness, the two-copy commutant is span{I,S}, without an external
asymptotic theorem: commuting with all diagonal unitaries preserves each
weight space span{|ij>,|ji>} and each |ii>; commuting with coordinate
permutations makes all diagonal blocks have the same coefficients; a
two-coordinate unitary rotation forces the |ii> coefficient to be the
sum of the identity and swap coefficients. Thus an invariant operator is
a I+b S. Solving its two traces against I and S gives

    P_0^(2) A = <r,A>(S-I/N)/(N^2-1).

The operator S-I/N also has zero partial traces. Its squared HS norm is
N^2-1. Since U^(tensor m) leaves each spectator identity unchanged, twirling
A inserted in one pair is exactly its two-copy twirl inserted in that
same pair. Linearity therefore computes the full m-copy Haar projection
of J_m A; it does not approximate that projection by a chosen subset of
invariants. Cross-pair orthogonality remains valid for the twirled terms.

After dividing by sqrt(b N^(m-2)),

    G = F^*F = I - |r><r|/(N^2-1),
    G^-1 = I + |r><r|/[N(N-1)].

On span{r}, ||r||^2=d and G has eigenvalue N/(N+1); on its orthogonal
complement it is identity. This proves positivity, injectivity and the
dimension formula for ALL m>=2. Relations among permutation operators
when m>N cannot change this calculation. In particular it is not relying
on linear independence of m! invariants. The projector is precisely
F G^-1 F^*.

Every slot-permutation operator preserves the ket/bra occupation counts,
so Haar-subtracted terms remain in ran Pi. Equivalently the explicit
sum of S_rs-I/N is balanced. Haar invariants are fixed under every Ad U,
and this invariant subspace reduces the unitary Ad U. Therefore

    F^* Ad(U^(tensor m)) F = Sym^2 T - |r><r|/(N^2-1).

The raw pair contraction is Sym^2 T; all other-pair contractions vanish
by zero partial traces after conjugation too. This proves the exact
block before taking a trace.

### Correct contractions and same-cycle interface

In a real orthonormal diagonal basis T is real, even for complex U and
nonsymmetric/nonnormal P. The three exact contractions are

    Tr(Sym^2 T) = ((Tr T)^2+Tr(T^2))/2,
    <r,(T tensor T)r> = sum_ab T_ab^2 = ||T||_HS^2,
    <r,G^-1 r>/(N^2-1) = 1/N.

The second contraction is generally different from Tr(T^2). Substitution
into Tr(G^-1 F^* Ad U F) proves the claimed formula. As immediate exact
checks: U=I gives N(N-1)/2, the full sector dimension; flat P=J gives -1/N.

J_m A commutes with EVERY slot permutation because A is symmetric in its
two slots. The Haar projection commutes with those permutations too.
Thus R_m fixes ran F pointwise, and unitarity of R_m also fixes the dual
projection: R_m P_quad=P_quad R_m=P_quad.

For the ambient identity, let C be the cycle on W and V=U^(tensor m).
The matrix-unit diagonal of Ad(CV) sums to Tr(CV) conjugate(Tr(CV)). The
ordered tensor index contraction gives Tr(CV)=Tr(U^m). Hence the ambient
trace is |Tr U^m|^2. This is simultaneous ket/bra conjugation. A one-sided
cycle or Sym^m(C^N) ambient is a different problem and was not substituted.

### Source spectrum, including composite N and N=3

For D_k=N^-1/2 diag(e_N(kx)), direct substitution into the literal chirp
M_ax=N^-1/2 e_N(-inv8(3a^2-2ax+3x^2)) gives

    (M D_k M^*)_ab = N^-1/2 e_N(-3 inv8(a^2-b^2))
                     times 1_{a-b=-4k}.

The adjoint direction reverses the corresponding sign. Multiplication by
4 is invertible for every odd N, including composite N. Each k!=0 thus
has a nonzero coordinate shift. On an active pair, balanced occupation
requires inverse shifts, and for {k,-k} leaves exactly N entries in each
of its two disjoint orientation supports. Each entry has magnitude
1/(sqrt(2)N). Thus each normalized paired Fourier tensor has squared
source norm 1/N. Distinct pairs have disjoint difference supports.

Spectator occupation counts cancel, so global Pi restricts each pair in
exactly this local fashion for every m. The resulting raw source remains
zero-partial-trace, and embeddings at different slot pairs are orthogonal.
There is no combinatorial loss as m grows.

Writing E for the span of the h=(N-1)/2 inverse Fourier pairs, the raw
source Gram is P_E/N. The contraction vector r is in E and has norm
squared N-1; in the normalized paired basis it is sqrt(2) times the sum
of those basis vectors. Since Pi fixes the Haar component, subtraction
gives source Gram

    B = P_E/N - |r><r|/(N^2-1).

The true input metric is G, so squared singular values are those of
G^-1/2 B G^-1/2. They are 1/N on E intersect r-perp, 1/N^2 on r, and
zero on E-perp. Taking square roots yields exactly

    N^-1/2 with multiplicity (N-3)/2,
    N^-1   with multiplicity 1,
    0      with multiplicity (N-1)^2/2.

For N=3 the first multiplicity is zero and the exact norm is 1/3, as
the candidate explicitly notes. The additive source is zero: a single
nonzero shift cannot preserve occupations. Finally, contraction of Pi
and the unitary source map, followed by
||(exp(-itNH)-I)Y||<=|t|N||HY||, proves the stated finite-t inequality.
No small-t expansion and no positivity of signed memory is asserted.

### Degree <=2 and actual-flatness aggregation

Every occupation number is a sum of one-slot coordinate indicators. A
product of two occupation numbers splits into same-slot and distinct-slot
terms. Decomposing coordinate diagonals into constants plus D_0 therefore
spans constants, collective additive D_0, and J_m(Sym^2 D_0). Their zero
partial-trace degrees are mutually orthogonal; the Gram proof shows there
are no further dependencies for m>=2. Haar subtraction removes constants,
leaves the additive sector unchanged, and transforms the last summand into
ran F. The additive normalized compression is T, so its trace is Tr T.

The maintained position_chain_mixing.md is hash-identical to the pinned
input (3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09).
I inspected its Sections 2--4 and the underlying four_branch_parametrix.md
Sections 1--2 and specified-time bounds. The latter gives four terms of
size O(N^-1/2) with bounded amplitudes and entry error O(N^-3/2) on a fixed
time interval containing tau=10^-80. This directly supplies P_ij<=C/N.
The more difficult oscillatory mixing assertion is not a leaf of this
sector proof. The finite-shift residual, exact initial Gauss identity,
bounded transports, and unitary Duhamel provide the stated flatness; the
source already records the independent analytic audit.

For any doubly stochastic P with this entry bound and C>=1,

    0<=Tr P<=C,
    0<=Tr(P^2)<=C,
    0<=||P-J||_HS^2<=C-1.

The middle estimate uses P_ij P_ji<=C P_ji/N followed by the sum of all
entries of P; it assumes neither symmetry nor normality. Since
Tr T=Tr P-1 and Tr(T^2)=Tr(P^2)-1, the displayed candidate constant
C^2+C+1 safely bounds the pair-quadratic trace. The additive sector costs
at most C more. The trace is independent of m, and a fixed smooth weight
supported in a positive compact interval has O_w(N) nonzero integer
replica orders. Multiplication by N^-2 proves O_w(N^-1). No effective
startup N is extracted, no N-dependent weight is claimed, and no estimate
on the complementary signed trace is supplied by this argument.

## Obligation matrix

| Obligation | Status | Decisive point |
|---|---|---|
| Full ordered End(W) and same ket/bra cycle | Passed | Matrix-unit and cyclic index contractions |
| True Haar removal at every m | Passed | Local twirl with identity spectators |
| m>N | Passed | G positive independent of m; no permutation independence |
| True projector and Gram correction | Passed | Positive G and explicit inverse |
| Nonnormal/nonsymmetric U compression | Passed | Real T; distinct Tr(T^2) and HS contractions |
| Entire pair-quadratic sector | Passed | Injective Sym^2 D_0 construction and dimension |
| Degree <=2 extension | Passed | Orthogonal constants/additive/pair decomposition |
| Source singular values and multiplicities | Passed | Inverse Fourier shift pairs and true input metric |
| N=3 and composite odd N source | Passed | Vanishing first multiplicity; invertibility of 4 |
| Literal actual-flatness input | Passed, inherited analytic input inspected | Fixed-time finite-shift parametrix |
| O(1) pointwise and O_w(N^-1) | Passed | Elementary stochastic bounds and O_w(N) terms |
| Whole balanced space or K spectral sector | Out of scope | Neither established nor needed |
| Full signed plateau/BGS | Out of scope/open | Complementary sectors unestimated |

## Computation and frozen-source checks

All 39 input, output, and review-hash comparisons across the parent,
nonlinear-source, signed-pairing, and quadratic-sector manifests passed.
The complete per-file record is hash_checks.json. Candidate replay passed
unchanged and is saved in candidate_replay.json; its runtime field is
naturally a new observation, not a byte comparison with the frozen run.

The independent_check.py implementation imports no candidate code. It:

- Builds the full ordered tensor matrices.
- Computes the full invariant span from all slot permutations by SVD,
  subtracting its projection without the candidate's rank-one twirl formula.
- Orthonormalizes the resulting sector independently by SVD, without G^-1/2.
- Tests the candidate Gram and trace only after this construction.
- Uses identity, cyclic-permutation, and two reproducible complex QR
  unitary controls per (N,m), including nonsymmetric/nonnormal P.
- Checks the additive sector, balanced containment, full ambient cycle
  identity, and direct literal-chirp metaplectic source spectrum.

Pairs tested: (3,2), (3,3), (3,4), (4,2), (4,3), (5,2), (5,3), (9,2).
At N=3,m=4, all 24 slot permutations have span rank 23; the independent
construction handles that dependency explicitly. Even-N cases check only
the general-unitary trace theorem, not the odd-N chirp source assertion.

Maximum residuals in float64/complex128:

- Quadratic trace: 1.43e-14.
- Additive trace: 8.89e-16.
- Full ambient cycle: 3.56e-15.
- Source squared singular spectrum: 3.89e-16.

Commands:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python independent_check.py > independent_checks.json
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python /workspace/shared/bgs_weighted_plateau_independent/quadratic_sector/check_sector.py > candidate_replay.json

These finite controls are not interval certification and do not establish
the universal identities or the actual asymptotic limit on their own.

## Remaining gap and strongest safe conclusion

No missing implication was found inside the expressly stated pair-quadratic
or degree-at-most-two claim. This audit licenses the exact trace identity,
true-metric source spectrum, and vanishing normalized contribution under
the stated actual-flatness input. It does not license treating this sector
as a spectral subspace of K, multiplying one vector's coefficient by its
dimension, replacing the full ambient trace by a symmetric-power trace,
or concluding the needed signed plateau correction from this sector.

The next substantive problem is an explicitly defined complementary sector
or a sum over higher occupation degrees with a uniform signed estimate.
Repeating low-degree tests will not close that missing full-trace bound.
