# Independent audit: constant position-chain gap and marked three-link cancellation

## Normalized claim and primary verdict

**Proved as written, for the expressly defined marked expression.** At fixed tau=10^-80, for every sufficiently large odd N in the actual raw model U_N=exp(i tau N A_N)M_N, P=|U|^2 and J_ab=1/N satisfy ||P-J||<=1/2, and hence ||P^L-J||<=2^-L for every integer L>=0. More precisely limsup ||P-J||<=10^-64. For the exact distinct-port expression E_dist in Section 3, |E_dist(L)|<=C^3 N 2^-max(L_i), uniformly over all nonnegative link lengths. Its polynomially weighted compact positive Heisenberg-band sums vanish exponentially. This does not establish a once-counted trace-pair family or deterministic BGS.

Audited candidate SHA256: 156808b1febd7b61a8aff4e4756314934e5cb6b471c7e5a2f15a6f5f64f216af. Base checked: main 0ffb20cc152d0ddd2620887e46d21d1120b95fd8. No repository or remote edits were made.

## Dependency closure and inherited versus new work

Raw model definition -> exact ordinary finite-shift dictionary -> four-term Gauss identity for M -> analytic short-time HJ graphs with exact lattice gluing -> finite transport hierarchy -> unitary Duhamel approximation -> sixteen terms for P -> new diagonal transport estimate and new same-coordinate mixed-phase nonvanishing -> inherited local alias-safe discrete TT* argument -> constant singular gap -> elementary stochastic powers -> new exact marked cancellation and count.

The entire four-branch construction remains load-bearing: not merely its headline result. Its raw quantizer identity, initial phases, phase/amplitude gluing, finite residual estimate, and uniform derivative bounds are essential. The numerical constants through C² time Taylor remainder and the local discrete TT* lemma are also essential inherited analytic inputs. I reconstructed the relevant steps, rather than accepting the previous review's verdict. The Q(j,k)=U(j,k) conjugate(U(k,j)) nonvanishing calculation does NOT by itself imply the needed P nonvanishing; the new difference factor between r and s must be computed. No reversal-family multiplicity estimate, seven-cut confinement, earlier N-scaled diagonal gap, continuous FIO theorem, external BGS theorem, or noisy-channel result is used here.

Comparing source base fa007c498fe116a814a90aa3215cfd65b1f2a154 to the pinned base shows that FM-001 Sections 1–2, including the quantum model and ordinary symbol, are unchanged; Section 3 was expanded. The reviewed four-branch source itself was unchanged. Exact source hashes are recorded in the dated evidence, so this dependency reconciliation remains reproducible.

## Reconstructed analytic obligations

### Raw dictionary and finite WKB: passed

For odd N, (-1)^(kl)e_N(k(j+inv2*l))=exp(2 pi i k(j/N+l/(2N))), exactly. Substitution into the raw Fourier quantizer gives the finite shifts in the shared parametrix source with the required half-position shift in the momentum-dependent coefficient. The four-term quadratic Gauss identity supplies the exact initial kernel for every odd N, and the stated phase shifts have integer multiples of 1/N on the sampling lattice. Their gradient changes are integral, preserving g and all its derivatives, so transport glues as well.

Expansion after removing exp(2 pi i S/h) gives the first amplitude operator
D_1 a=(g_p/(2 pi))a_x+(g_xp+g_pp S_xx)a/(4 pi).
The HJ sign is S_t=g/(2 pi), with characteristic velocity -g_p/(2 pi). Solving a_0 and a_1 transports already leaves entry residual O(h^(5/2)); N times its maximum is O(h^(3/2)) in operator norm. Unitary Duhamel then supplies entry error O(h^(3/2)). Higher amplitudes are not required for the displayed leading-amplitude statement. The canonical shared parametrix makes this two-amplitude hierarchy explicit.

Characteristic derivatives and global graph invertibility on |t|<=10^-20 follow from the bounded periodic vector field and X_a>=1-2*10^-8, with bounded X-a. Derivatives of p=S_x through third order can indeed be bounded by 10^4. Differentiating HJ gives S_tt=(g_p g_x+g_p^2 p_x)/(4 pi²). Its C² bound is safely below 10^50 using the supplied |D^j g|<10^9 and p-derivative bounds. This reconstructs the fixed-time rather than merely formal nonvanishing input.

### Branch-diagonal amplitude: passed

Along an amplitude characteristic, da_0/dt=b a_0 with b real and |b|<10^14. Therefore a_0=exp(integral b), starting at 1, and |a_0-1|<=exp(10^14|t|)-1<2*10^-66 at tau. With epsilon=2*10^-66,
|d-1|<=2 epsilon+epsilon²<10^-64,
where d=(1/4)sum_r |a_r|². The sampled kernel h(d-1) has row and column absolute sums at most 10^-64; its l² norm has the same bound. The omitted higher amplitudes and Duhamel error produce O(h²) per entry in P, hence O(h) in norm. Their constants may depend on fixed tau, which is sufficient.

### New same-coordinate nonvanishing: passed

Expanding B(x)=r(x+1/2)/100 gives B_7=1/200. The positive-momentum term has coefficient B_7 exp(-i alpha)/2. Since p_r(0)=(y+r-3x)/4, the HJ derivative at frequency (25/4,1/4) has coefficient exp(i pi r/2-i alpha)/(800 pi). No momentum-independent or negative-momentum term has this frequency. Multiplication by -(2 pi)²(25/4)(1/4), then subtraction between r and s, gives exactly
-(pi/128) exp(-i alpha) [exp(i pi r/2)-exp(i pi s/2)].
For distinct r,s in {0,1,2,3}, its magnitude is at least sqrt(2) pi/128. Each correction is separately four-periodic, so the normalized Fourier coefficient is legitimate. The difference Taylor remainder is bounded by 10^50 tau²=10^-110, strictly below its linear term. Also S_r(0)-S_s(0) is separable, hence has zero mixed derivative. Thus all twelve off-diagonal mixed derivatives are analytically nonzero at the exact prescribed tau.

### Discrete sampling and global norm decay: passed

After separating the initial row/column phase factors, the mixed derivative is bounded by C<1/4, from the same C² Taylor estimates. On a small good rectangle, c<=|phi_xy|<=C with fixed sign. For two supported rows x,x', let d=|x-x'| and psi(y)=phi(x,y)-phi(x',y). Then c d<=|psi_y|<=C d and psi_yy=O(d). The phase increments of exp(2 pi i N psi(j/N)) lie strictly between c d and C d in absolute value, never near a nonzero integer. Summation by parts gives an unnormalized weighted exponential sum O(1/d): the reciprocal increment denominator is O(1/d), and its total variation is O(1/d). This requires the rectangle to contain the horizontal segments between the rows and a slight enlargement in y; finite smooth local cutoffs provide both.

Consequently diagonal TT* entries are O(1/N), off-diagonal entries are O(1/(N|i-i'|)), and the Schur bound is ||T||²=O(log N/N). Constants depend on the fixed rectangle and tau. Nonzero real analyticity gives a zero set of area zero. A smooth bad-region cutoff of arbitrarily small area has limiting unnormalized Hilbert–Schmidt norm at most bounded amplitude times square root of its area, by Riemann sums. A finite smooth partition of the remaining compact set into good rectangles proves norm o(1). This is an alias-safe discrete argument, not an unjustified transfer of a continuum oscillatory estimate.

Combining twelve o(1) kernels, the diagonal estimate, and O(h) remainder yields the claimed limsup. P is doubly stochastic by unitarity; PJ=JP=J. Thus P^L-J=(P-J)^L for L>=1, without any normality assumption. L=0 gives I-J, whose norm is <=1. One eventual threshold works for all link lengths.

## Exact marked algebra and boundary lengths

### Any-one-J cancellation: passed

Fix the ports a and all endpoints except b_k. When the kth link is J, its entire endpoint-dependent sum is
(1/N)sum_b U_(b,a_(k+1)) conjugate(U_(b,a_(k-1)))
=delta_(a_(k+1),a_(k-1))/N=0.
The other ports are distinct, and no other factor depends on b_k. This works regardless of the other link lengths, even if they are zero. It uses complex column orthogonality, not symmetry or realness of U. Without the distinct-port restriction it is false.

Replace the longest link by Delta=P^L-J. Its entries have magnitude <=||Delta||<=2^-L, also for L=0. Set q=max|U_ab|²<=C/N from WKB. The six U factors cost q³. Each of the other endpoint sums against a stochastic row costs 1. There are at most N³ choices of a and N choices of b_k. The resulting bound is q³ N^4 2^-L<=C³N2^-L. In particular no positive minimum length was assumed.

For m>=3, the exact number of nonnegative triples with sum m-3 is binom(m-1,2), and max L_i>=(m-3)/3. Thus the written all-triple bound follows. For a fixed bounded smooth weight supported in [a,b] with a>0, N^-2 summation over m costs only a polynomial; the exponential factor is at most 2^(-(aN-3)/3). At m<3 the triple sum is empty. This estimate controls exactly this marked expression; additional history filters or a once-counted family require their own algebra.

## Independent finite checks and unmarking scope

The independent script uses sorted cyclic cut triples for each fixed rooted first word, then all roots of the second word, with a factor 3 for the three block labels. This differs from the author's implementation using a block-rooted first word and two independently enumerated roots. Exhausting N=3,m=6 reproduces 17,568 ordered pairs of multiplicity 3 and 936 of multiplicity 6. The two stated examples are primitive and have respectively one and two cyclic-label-quotiented cut triples. Thus periodic-word degeneracy does not explain the discrepancy.

The separate cut-enumeration check reproduces all three m=7 examples and precisely the mask (1,1,0). For U=I-vv^T/7, v=(1,2,3), the omitted row product is U_20 U_21=18/49; hence the masked uniform sum is -6/49. The index order (U* D_I U)_(a2,a1) is correct for complex U. A further exact Gaussian-rational unitary test checks the distinct-column identity without restricting to real symmetric matrices. Arithmetic is Fraction-based; finite tests are not used to prove the asymptotic analytic claims.

The multiplicity and mask examples refute a universal unmarking prefactor and this particular free-endpoint-preserving canonicalization mechanism. They do not refute every possible canonicalization, prove a nonzero actual asymptotic residual, or settle the actual model's unmarked sum. Inclusion–exclusion and integral weights 1/r are exact identities, but introduce coupled history constraints; estimating their whole hierarchy is still missing.

## Obligation summary and remaining gap

Passed: raw-model matching; finite WKB; diagonal transport estimate; specified-time same-coordinate phase nonvanishing; alias-safe discrete norm decay; simultaneous all-length power bound; exact any-one-J contraction; all-length marked estimate; stated finite multiplicity and canonical-mask counterexamples.

Out of scope/open: exact once-counted unmarking with controlled signed weights; arbitrary noncyclic trace pairs; higher joint-trace orders; full TRACE-005/BGS. No missing implication remains inside the scoped marked theorem. The cheapest next substantive check is a concrete proposed unmarking/canonical rule tested for endpoint independence before attempting any norm estimate. Rechecking the already-proved isolated marked diagram cannot close that gap.

## Reproduction and source records

Canonical proofs: `../mathematics/position_chain_mixing.md` and the common
`../mathematics/four_branch_parametrix.md`. The accepted source SHA256 is
156808b1febd7b61a8aff4e4756314934e5cb6b471c7e5a2f15a6f5f64f216af.
The portable maintained verifier is
`../computations/verification/actual_path_theorems.py`.
The original independent finite checker and source checks were executed
read-only; their hashes, precise commands, ranges, and results belong to
`../evidence/executions/20261006/path-theorems/receipt.json` and its source
manifest. This audit reconstructs the listed analytic implications; no finite
run, source hash, or agreement of implementations proves the limit by itself.
