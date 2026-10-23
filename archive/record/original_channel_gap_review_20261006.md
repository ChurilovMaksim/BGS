# Independent audit: original ordered two-pair channel

## Claim and verdict

For every odd integer N>=3, u>=0, and unitary U, let A,B,Q be precisely D1/D5 of `mathematics/collective_diffusion_gap.md` and ell=1+log N, lambda=(1024 ell)^(-2). The claimed estimate is

||exp(-uA) exp(-uB) Q|| <= 1-(1-exp(-2u lambda))/50.

**Verdict: proved as written.** The displayed contraction and singular-gap lower bound are valid. The first draft said the actual gap “is asymptotic to” the stated expression; the author has now corrected this to **the displayed lower bound**. No actual-gap upper bound has been proved. This was a wording/scope correction, not a failure of the lower-bound proof.

Audited candidate: the pre-promotion version of `mathematics/original_channel_gap.md` (initial read SHA256 3ffec4ec9b5ea210ba36d5e0a91ebbe3f6444ec795836a20f723ca341421190a). Base proof read from the supplied local snapshot, SHA256 601a0acb28d07d940b5f3479954dcc560191f2c96a2bfbd22d4bbf0f56e2afbf, identified by the assignment as revision fa007c498fe116a814a90aa3215cfd65b1f2a154. At the time of the independent audit the supplied files were a partial source snapshot; no repository files were edited by the reviewer. The later acquisition verified all 999 files against the pinned Git blobs and restored the exact shallow commit.

## Dependency graph

Raw modular Weyl commutator -> D6 total-label blocks -> translated D8 eigenvalues -> low-positive-eigenvalue count -> unbiased partial-Fourier basis overlaps + exact D19 kernel angle -> low-spectral angle on Q -> two positive contraction losses -> ordered product contraction -> unit-circle singular lower bound.

No annular Poincare estimate, uniform gap D2, Trotter approximation, external theorem, or refined noise law enters this proof. D19 is an internal finite-dimensional calculation, reconstructed below rather than accepted from its status label.

## Obligation matrix and decisive evidence

- **Passed: diagonalization/parity.** D6 has fixed-a ordinary Fourier eigenvectors in b. Translating y=a-k/2 and sign gauging produces twisted eta in the same integer or half-integer parity class as y. D8 gives exactly the two nonnegative terms in (2). The endpoint -N/2 in a half-integer grid is included once and causes no missed zero: neither y nor eta is zero. Multiplicity of eigenvalues causes no difficulty since spectral projections include full eigenspaces.
- **Passed: nonaxis counting.** First-term positivity gives E>=64 y² eta²/N², hence |y eta|<=N sqrt(lambda)/8. For either centered grid, the count of nonzero eta with |eta|<=t is <=4t, including t<1/2 where it vanishes. The reciprocal sum is <=4(1+log N), for N>=3, yielding 2N sqrt(lambda)(1+log N). A fully explicit half-integer harmonic estimate is sum <=4+2H_((N-1)/2) <=6+2log((N-1)/2) <=4(1+log N); the last inequality holds already at N=3 and then improves. Integral grids have the stronger twice-harmonic estimate.
- **Passed: axes.** If k=0 the two axes are exactly the kernel and are excluded. If k is even and nonzero, |k|>=2 and sin²(theta)>=k²/N². Along an axis d=N/2-|eta| is a positive half-integer, so E>=32k²d²/N². Each endpoint contributes at most D+1/2<=2D when D>=1/2, and contributes zero otherwise. Two axes cost <=8D=sqrt(2)N sqrt(lambda)/|k|<=N sqrt(lambda). Thus the claimed total 4N sqrt(lambda)(1+log N) is conservative with no hidden additive count.
- **Passed: exact kernels.** In D17 zero requires equal sine magnitudes. For odd N this means residue indices equal up to sign. The equal-index, equal-sign alternative requires cos=-1, impossible on an odd ordinary Fourier grid unless both sine values vanish. Thus A has a kernel only when kappa_a=0, of dimension 2N-1. B is transposed. Their product is supported only at total label zero.
- **Passed: D19 including N=3/composites.** At total label zero, remove the isolated origin. The normalized row/column overlap matrix has zero-sum singular values N^(-1/2) and constant-sector eigenvalues 1 and -1/N. Removing the common punctured constant removes the singular value 1. Restoring then removing the origin removes the other common invariant. This is a combinatorial computation on N points; primality is never used.
- **Passed: basis overlap.** Original D6 eigenbases are delta_a times normalized ordinary Fourier_j(b), versus normalized Fourier_i(a) times delta_b. Every scalar overlap has modulus 1/N. Consequently the Hilbert-Schmidt product norm is exactly sqrt(rs)/N for spectral-subset projections of ranks r,s. This estimate is applied blockwise, never to the full N^4 space with the wrong denominator.
- **Passed: Q reduction and cross terms.** Both invariant vectors are killed by A and B. Every spectral projection commutes with their projection P and Q=I-P. Positive-low projections annihilate P; kernel projections act as identity on P. Consequently restricting the product expansion to Q is legitimate. With each extra rank <=N/256 and kernel rank <=2N-1, the three extra terms cost at most sqrt(2)/8+1/256. Together with N^(-1/2)<=1/sqrt(3), the sum is <4/5. The common-invariant angle 1 never contaminates this estimate.
- **Passed: projection angle to form.** For projections E,F on reduced Q with ||EF||<=4/5, the row-map Gram operator gives E+F<=9I/5. Hence 2I-E-F>=I/5. This also covers blocks with zero kernels and zero low ranks.
- **Passed: ordered product.** Let a=1-exp(-2u lambda). Spectral calculus gives (I-F²)+(I-G²)>=aI/5. For unit x, beta=1-||FGx||² controls both G's loss and F's loss on Gx. Since ||(I-G)x||²<=beta, F's loss on x is <=4beta. Thus a/5<=5beta and ||FGQ||<=sqrt(1-a/25)<=1-a/50. No commutativity or normality is assumed.
- **Passed: U and spectral parameter.** Collective conjugation fixes I and swap and is unitary/reducing on Q, preserving the product norm. Reverse triangle proves the stated lower bound uniformly for unit-circle spectral parameter, and for I-zC with |z|<=1.
- **Passed with wording correction: asymptotic.** For u=N^(-alpha), 0<alpha<1, the explicit lower bound is asymptotic to u/[25*1024²*(1+log N)²], and its ratio to N^(-1) tends to infinity. This does not determine the actual gap asymptotically.

## Computation checks

Command at review time: `python3 check.py`, using the separately preserved independent diagnostic source below.

Float64 diagnostics compared sorted raw D6 eigenvalues against gauged D8 eigenvalues for every centered k and all odd N=3,...,65 (1,088 complete spectra). Maximum absolute error divided by 1+N² was 3.14e-13. For each spectrum, 61 logarithmically spaced lambda values from 1e-10 to 1e5 checked the positive-low count against the proposed universal bound, with no violation. The maximal observed count/bound ratio was 0.07534. These are numerical diagnostics only, not exact arithmetic or a proof of all N; they include N=3 and many composite N and test nontrivial positive counts by varying lambda.

Results: `evidence/executions/20261006/original-channel-gap/independent_checks.json`; reproducible source: `computations/experiments/original_channel_gap_independent.py`.

## Remaining gap and safe scope

No missing mathematical implication found for the stated lower bound. The single actual-gap asymptotic sentence was corrected by the author during review. The result closes an auxiliary two-copy microscopic-mass issue for the original m=1 common-noise law. It does not imply quenched-power estimates, nonlinear determinant control, higher-copy gaps, noise removal, signed Heisenberg trace cancellation, or deterministic BGS.

## Promotion pin

Accepted candidate SHA256: `3ffec4ec9b5ea210ba36d5e0a91ebbe3f6444ec795836a20f723ca341421190a`. Promotion changes the introductory status/links removes the word “proposed” and adds the bounded source-comparison link in the attribution paragraph; equations and mathematical arguments are unchanged.
