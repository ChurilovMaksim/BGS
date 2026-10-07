# Independent audit: two auxiliary half-Hamming-radius witnesses

## Verdict and pinned targets

**Primary verdict: proved as written**, for the two auxiliary witness claims and their explicitly stated boundaries. This is an independent internal mathematical audit, with separately bounded exact computation; it is not external referee certification.

The audited Fourier source is `inputs/half_radius_obstruction.md`, SHA-256 `ab8fadd21110f11be5713489ae8b61c890ad242657e422afa7a6af21d7d566bb`. Its claim is for every N >= 2 and every positive m divisible by 4: at r=m/2 the ordinary full endomorphism-space offcharge cyclic trace is real and at least 2(N-1)(1-1/N), with equality when m=4, although ||P_F-J||=0.

The audited symplectic source is `inputs/symplectic_half_radius_obstruction.md`, SHA-256 `9da9dc1f548f1bb716942a8d15bccbbf1f105bf02b8bc786c87177d2cdd3255d`. Its claim is for every odd n>=3, N=n², and every even m>=4: the same lower bound holds for the stated H; the m=4 value is exactly 2(N-1); H is a flat Hermitian involution and its reversed-kernel norm is N^(-1/2).

The inherited *definitions*, not the main fixed-fraction theorem, are pinned in `inputs/candidate_v1.md`, SHA-256 `8feb1a9a402c679299fe060c3903f6d783a6e9939ad175bbf6a79dc0f9dde041`. This review does not audit that theorem's Gram inverse, Haar tail, asymptotic entropy estimates, or inherited actual quantizer estimates. No canonical files were edited or publication attempted. `input_manifest.json` records the separate canonical checkpoint and all source hashes.

## 1. Objects, grading, and exact physical interpretation

Let W=(C^N)^(tensor m), E=End(W), with its ordinary unnormalized Hilbert-Schmidt inner product and trace. Let C_m be one full cyclic permutation of the m slots, R=Ad(C_m), and C_U=Ad(U^(tensor m)). In the physical matrix-unit basis |x><y|, with x,y in {0,...,N-1}^m, define:

- F_r: diagonal projector selecting #{i:x_i != y_i} <= r;
- Pi: diagonal projector selecting equal total coordinate occupation of x and y;
- O_r=(I-Pi)F_r: their literal offcharge Hamming mask.

These are commuting orthogonal masks; O_r has no Haar denominator and is not a Haar-centered range projection. For a consistent direction of the full cycle its trace is the literal signed path sum

Tr_E(R O_r C_U) = sum_{x,y: d_H(x,y)<=r, occ(x)!=occ(y)} product_i U[x_i,x_(i+1)] conjugate(U[y_i,y_(i+1)]),

with indices cyclic. Reversing the chosen cycle just reverses the corresponding product order. All witness results below hold for either convention.

Locally write End(C^N)=C e direct-sum V, where e=I/sqrt(N) and V is traceless. Let D0 be traceless diagonal matrices, O the offdiagonal matrix units, V=D0 direct-sum O, and p,q their orthogonal projections. Let A=Ad(U)|_V.

For each S subset {1,...,m}, E_S has V in slots S and C e in the other slots. F_r preserves every E_S: locally the diagonal projector is P_e+p and the offdiagonal projector is q. Pi and C_U preserve E_S because they are diagonal-unitary and unitary conjugation averages/actions. Thus O_r preserves E_S. R maps E_S to E_(C_m S). A proper nonempty S cannot be invariant under a full cycle, so its diagonal block in R O_r C_U is zero. The empty support is killed by I-Pi. Therefore the full offcharge trace equals the top-support V^(tensor m) trace exactly.

For the raw F_r and balanced Pi F_r traces separately, the empty support contributes **+1 to each**. Proper nonempty supports contribute zero. Hence

full raw = 1 + top raw; full balanced = 1 + top balanced; full offcharge = top raw - top balanced.

This scalar correction is essential when checking physical-word sums. It does not alter either published witness formula, whose intermediate raw equalities are on top support.

## 2. Standalone positional reduction, including every nonalternating pattern

On top support, F_r is the sum of tensor products of p and q with at most r q slots. Flatness P_U=J gives pAp=0. The full-cycle tensor trace identity turns the contribution of a positional word into one local cyclic product of factors pA or qA. If two p slots are cyclically adjacent, this local product contains pAp, and its trace vanishes.

For m=2h and r=h, the allowed words have at least h p slots. If no p's are adjacent on the circle, each p must be followed by a distinct q, so there are at most as many p's as q's. Equality is forced. Every gap between consecutive p's therefore has exactly one q. There are precisely two survivors: the alternating words. This excludes all nonalternating patterns, including those with fewer than h q's; it is not a restriction to a selected convenient family.

Because Ap lies in ran q, pAqAp=pA²p. Cyclicity equates the two alternating traces. Their total is

T_raw = 2 Tr_D0[(p A² p)^h].                                              (1)

To impose exact occupation balance, take independent uniform unit phases z_j, Z=diag(z_j), and D_z=Ad(Z)|_V. Each E_ab has torus character z_a conjugate(z_b); D0 has trivial character. Consequently

Pi|_(V tensor m)=integral D_z^(tensor m) dz.                              (2)

The same z is used in every slot of this integral. Integration selects equality of the complete occupation vectors, including repeated labels. It is neither a per-slot balance condition nor an added ensemble assumption on U.

Both p,q commute with D_z and pD_z=D_zp=p. Thus a p,p adjacency in the balanced integrand still produces pAp=0. The two alternating patterns yield

T_bal = 2 integral Tr_D0[(p A D_z A p)^h] dz.                             (3)

One can first write pAqD_zAp; since Ap is in q and D_z preserves q, that q is removable. The compression in (3) is exactly

p Ad(U Z U) p = (P_(U Z U)-J)|_(constants perpendicular),                 (4)

under diagonal-coordinate identification. All matrices are finite dimensional, so sums, traces, and compact torus integration can be interchanged without convergence assumptions.

## 3. Fourier witness: reflection is indispensable

Take F[a,b]=N^(-1/2) exp(2 pi i ab/N). Direct finite-character summation proves F² is the permutation reflection a -> -a. Thus p A² p is reflection on D0. If m is divisible by 4, h=m/2 is even, and (1) is 2(N-1).

Set

w_s = |N^(-1) sum_j z_j exp(2 pi i sj/N)|²,
c_k = N^(-1) sum_j z_j conjugate(z_(j-k)).

Then P_(F Z F)[a,b]=w_(a+b). This is **C R0**, where C[a,b]=w_(a-b) is convolution and R0 is reflection. On Fourier characters f_k(a)=exp(2 pi i ka/N), C f_k=c_k f_k and R0 f_k=f_(-k). Hence (C R0)² f_k=|c_k|² f_k. The constant character has eigenvalue 1, and for even h

Tr_D0[(P_(F Z F)-J)^h] = sum_(k != 0) |c_k|^h.                          (5)

This also handles even N: the self-opposite mode k=N/2 has real c_k and its even power equals |c_k|^h. There is no exceptional extra mode or factor of two.

The individual torus characters z_j conjugate(z_(j-k)) are distinct for k != 0. Their L² orthogonality gives integral |c_k|² dz=1/N. Equivalently the expanded exponent multisets {j,l-k}={j-k,l} force j=l. For a self-opposite k, the reversed edge is the complex conjugate character, not an additional equal character. Therefore no additional cross term survives.

Since |c_k|<=1 and h>=2 is even, (3)-(5) give

0 <= T_bal <= 2(N-1)/N.

Subtracting from T_raw=2(N-1) gives the asserted full offcharge lower bound 2(N-1)(1-1/N), with real nonnegative sign. For m=4, h=2, the upper bound for T_bal is exact, so the asserted lower bound is equality.

## 4. Symplectic witness: all odd composite moduli are included

Let G=(Z/nZ)^2, N=n², and omega(x,y)=x_1 y_2-x_2 y_1. Define H[x,y]=N^(-1/2) exp(2 pi i omega(x,y)/n). Alternation makes conjugate(H[y,x])=H[x,y], so H*=H. Furthermore

(H²)[x,z]=N^(-1) sum_y exp(2 pi i omega(x-z,y)/n)=1_(x=z).

The last sum factors into two ordinary complete cyclic-group character sums. No field structure or primality is needed. For any nonzero difference, at least one cyclic character is nontrivial and sums to zero, even when n is composite. Flatness is immediate.

Let K[x,y]=N^(-1/2) exp(2 pi i 2 omega(x,y)/n). Since n is odd, multiplication by 2 is invertible, so the same character argument gives K*=K and K²=I. The literal reversed-entry kernel is

Q_H[x,y]=H[x,y] conjugate(H[y,x])=N^(-1) exp(2 pi i 2 omega(x,y)/n)=N^(-1/2)K[x,y].

Thus ||Q_H||op=N^(-1/2) exactly. This is not the position kernel |H[x,y]|²=1/N. Oddness is load-bearing here; for even n the doubled character is degenerate. Finally Tr H=N/sqrt(N)=n, so the +1 and -1 multiplicities are (N+n)/2 and (N-n)/2, respectively.

For A=Ad(H)|_V, A²=I. Equation (1) is therefore T_raw=2(N-1) for every even m, including h odd.

Direct multiplication now gives

(H Z H)[x,y]=N^(-1) sum_u z_u exp(2 pi i omega(x-y,u)/n).

Its squared-entry kernel is convolution by a function of x-y, **without reflection**. On the group characters f_k(x)=exp(2 pi i omega(x,k)/n), the convolution eigenvalue is

a_k=N^(-1) sum_u z_u conjugate(z_(u-k)).

Nondegeneracy of omega labels all N characters bijectively for composite n as well. Removing the constant mode yields

Tr_D0[(P_(H Z H)-J)^h] = sum_(k != 0) a_k^h.                            (6)

Replacing the right side by sum |a_k|^h would generally be false. In particular h=2 has different phase expectation from the Fourier expression.

The distinct-edge-character argument gives integral |a_k|² dz=1/N for every k != 0, regardless of its order. With |a_k|<=1 and h>=2,

|integral a_k^h dz| <= integral |a_k|^h dz <= 1/N.

Moreover integral a_k^h is a nonnegative real number: the expansion has nonnegative coefficients N^(-h), and torus integration retains exactly the monomials with zero exponent vector. Thus (3) lies in [0,2(N-1)/N]. Subtracting proves the claimed real lower bound for every even m>=4.

For h=2, two directed translation edges cannot have zero total incidence unless they form a 2-cycle (or a loop). This requires 2k=0 (or k=0). In an odd-order group there is no such nonzero k. Therefore integral a_k²=0 for every k != 0, T_bal=0, and the m=4 offcharge trace is exactly 2(N-1).

A useful independent composite-order audit is the full constant-coefficient formula. If k has order L, translation decomposes G into N/L cycles. A zero-incidence selection must use every edge of each cycle with the same multiplicity. Consequently the ordinary h-th moment is zero unless L divides h; when it does, it equals

(h! / N^h) [t^(h/L)] (sum_(a=0)^(h/L) t^a/(a!)^L)^(N/L).                (7)

This proves positivity and the special h=2 vanishing directly, while distinguishing elements of different orders at composite n. Formula (7) is an auxiliary verification identity, not an imported assumption.

## 5. Normalization and what the obstruction actually says

The raw quantity is an **ordinary unnormalized trace**. The lower bound is asymptotic to 2N; it is not itself divided by N². For any positive compact Heisenberg band, permitted m can be chosen in that band with the required parity/divisibility, so no exponentially decaying uniform half-radius trace bound can follow from the listed coarse kernel data alone.

A precise normalized consequence, if desired, uses a nonnegative smooth compactly supported weight w on (0,infinity):

- Fourier: N^(-2) sum_(m divisible by 4) w(m/N) Tr(R O_(m/2) C_F) has liminf at least (1/2) integral w, as N -> infinity (also along odd N).
- Symplectic: N^(-2) sum_(m even) w(m/N) Tr(R O_(m/2) C_H) has liminf at least integral w, as odd n -> infinity and N=n².

These are Riemann-sum consequences for the stated restricted sector sums. No claim about an arbitrary signed weight follows from a positive lower bound; no conclusion for the complete pair statistic follows without controlling its complementary sectors. They are not assertions that a single O(N) summand survives N^(-2) normalization.

For symplectic H, the omitted odd-m half-floor sectors are in fact zero: with at most floor(m/2) q positions, there must be adjacent p positions in every cyclic word, and this kills both raw and balanced top traces. This observation permits the same normalized lower bound if the displayed symplectic sum is written over all m with radius floor(m/2); it is an elementary corollary, not needed for either pinned claim.

Both witnesses have maximal two-step diagonal compression: ||p Ad(U)^2 p||=1, although P_U=J and every Markov power P_U^k is J. In the Fourier case the compression is coordinate reflection; in the symplectic case it is the identity. A proposed actual-map discriminator must concern |U^k|² (quantum powers), not (|U|²)^k (Markov powers). No such actual-map estimate is supplied here.

## 6. Prior ownership, dependency graph, and obligation matrix

The broad insufficiency of coordinate flatness, position contraction, and reverse-kernel decay as abstract universality criteria is **prior project work** in the pinned `microscopic_rounding_control.md`, sections 1, 5, and 6. That result also preserves specified unnormalized sub-cubic-root low-trace windows and coarse Egorov estimates while changing the operator and violating a fixed pair target. Its source in turn credits earlier project spectral-rounding work. `isospectral_clock_moment_control.md` supplies a different all-copy channel boundary. Neither result is reclassified as a new outcome of this audit, and no global literature-priority claim is made.

The additional scoped outcome audited here is the explicit half-Hamming sector witness, and the fact that a symplectic Fourier involution retains it even under reverse-kernel norm decay.

Dependency graph:

Definitions of F_r, Pi, R, Hilbert-Schmidt trace -> support grading -> top p/q positional expansion -> pAp=0 plus cyclic-word exclusion -> two alternating traces -> torus integral and compression (4) -> witness-specific Fourier/reflection or symplectic/convolution identities -> character moments and sign -> offcharge subtraction -> pointwise obstruction. Optional normalized consequences use only elementary Riemann sums after that point.

Every analytic leaf of this graph is proved above by finite-dimensional algebra, character orthogonality, or the elementary bound |mean of phases|<=1. There is no external theorem, actual FM021/FM022 asymptotic, Haar estimate, or pending fixed-fraction audit in the proof dependency closure. Prior rounding is scope/ownership context, not a load-bearing witness lemma.

Obligation outcomes:

- Exact quantified claims, dimensions, parity, and normalizations: passed.
- Full tensor trace and proper-support vanishing: passed; scalar +1 recorded separately.
- Exclusion of every nonalternating allowed p/q pattern: passed.
- Shared-torus total charge projector and all repeated labels: passed.
- Removal of q in alternating compression: passed.
- Fourier convolution times reflection versus symplectic convolution: passed.
- Fourier even-N self-opposite mode: passed.
- Composite n and nonprimitive translations: passed.
- Ordinary versus absolute character moments and real lower-bound sign: passed.
- Exact m=4 values and physical-word interpretation: passed.
- Reversed-entry kernel, its norm, and spectrum multiplicities: passed.
- Normalized Heisenberg implications: passed in the restricted forms stated above.
- Actual quantizer/BGS refutation, full universality, novelty priority: out of scope and not claimed.
- Main fixed-fraction theorem and actual parametrix/Haar dependencies: out of scope.

## 7. Exact finite controls and residual gap

`independent_checks.py` is a fresh implementation; it imports no author verifier or result file. Author boundary outputs were inspected for comparison, so independence means independent derivation and implementation, not an information-blind experiment. The physical-word enumerator visits every pair inside the literal Hamming ball by changing chosen coordinates and excludes only identically zero mask entries. A separate full double-index calculation uses integer-scaled scalar/traceless projectors. Character tests use exact cyclotomic reduction and Laurent constant coefficients, with no random sampling, quadrature, or floating-point roots of unity.

`contract.json` states all finite ranges, exclusions, and non-claims. `run_final/manifest.json` is the bounded-run provenance record; `run_final/results.json` gives exact rational values and actual enumeration counts. The run is capped at 180 wall seconds, 160 CPU seconds, 2 GiB address space, one CPU affinity, and one requested library thread; thread limits are cooperative. Commands and completed-run results are summarized in `FINAL.md`.

There is no remaining mathematical gap in the two pinned auxiliary claims identified by this audit. The relevant unresolved problem is controlling the actual unchanged quantizer's higher-Hamming signed sectors; these witnesses neither answer it nor provide a theorem beyond half radius. The cheapest next substantive check for a proposed stronger hypothesis is whether it excludes the exact two-step compression already displayed here, before undertaking any large-N numerical test.
