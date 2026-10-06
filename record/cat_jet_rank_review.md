# Independent audit: algebraic-time rank transfer

Date: 6 October 2026. Review workspace: `bgs_rank_transfer_review`.

## Normalized claim and primary verdict

**Primary verdict: proved as written.** The frozen v2 source correctly proves the general rank-transfer theorem and the derivative-stack interpretation, with the registered Lindemann–Weierstrass theorem as an explicitly inherited external input. Its actual-family multiplicity bound and deepest-core simplicity counts follow from the individually accepted dependencies. The frozen source correctly states the newest-even-sector conclusion conditionally. During this review, the separate source-bound newest-sector audit was completed with verdict “proved as written.” Its premise is therefore now satisfied, so the combined even-depth count is available. The frozen proof source has not been edited.

Reviewed target: `inputs/algebraic_time_rank_transfer_v2.md`, SHA-256 `673f0831080263e6d28b85ce91ae4a5fa705d637aa34fb9fd6d54700cda3b62d`. No correction or restriction to its mathematical statement is required.

Precisely, let A be an N-by-N Hermitian matrix with algebraic entries, M an N-by-N unitary matrix with algebraic entries, and U(t)=exp(itA)M. For every finite matrix F whose entries are polynomials over the algebraic numbers in the entries of U(t), every nonzero real algebraic t has rank F(t)=max_(s in C) rank F(s). The same applies to the evaluated characteristic derivatives and their vertical stacks. Consequently the spectral multiplicity partition of U(t) is identical at all nonzero real algebraic times and equals its generic real-time partition. These statements do not assert that this partition is simple.

For the prescribed actual N=7·5^e family, e≥1, at every nonzero real algebraic t, including t=10^(−80)N:

- every eigenvalue has multiplicity at most seven;
- for even e≥4, at least seven eigenvalues are simple, using the accepted deepest-even-core theorem;
- for odd e≥5, at least 35 eigenvalues are simple, using the accepted deepest-odd-core theorem;
- for even e≥4 there are at least 24N/25+7 simple eigenvalues, and the total dimension of repeated eigenspaces is at most N/25−7, using the newly accepted newest-even-sector input together with the accepted deepest core.

The first three conclusions do not use the newest-sector candidate. All retain the named external LW input. There is no quantitative gap estimate, full-simplicity theorem for this infinite family, classification of the full complex U commutant, or BGS conclusion.

## Provenance and dependency graph

Canonical `BGS` was read-only. Its observed HEAD was `801de3ab760cab4349e68b9843dcd67955314e62`, and the observed Git status was clean. Those observations do not claim that a concurrently maintained repository stayed immutable. All reviewed mathematical inputs were copied into this workspace and individually hashed in `source_manifest.json`, including the newest-sector acceptance report added when it became available. No canonical `.mathbox` directory was found. Canonical instructions, source-of-truth hierarchy, relevant claim/status records and conventions were inspected.

The implication graph is:

1. Algebraic Hermitian A → algebraic eigenvalues and algebraic spectral projectors → entries of exp(itA)M are finite exponential polynomials with algebraic coefficients and real algebraic frequencies.
2. Closure under addition and multiplication → characteristic coefficients, evaluated characteristic derivatives, stacks and every minor are in the same class.
3. Registered EXT-POPESCU-2023 → a minor vanishing at a nonzero algebraic time is identically zero → maximal rank at every such time.
4. Real-time unitarity → derivative stacks are scalar maps on orthogonal eigenspaces → ranks recover the complete multiplicity partition.
5. Accepted cat multiplicity ≤7 at t=0 → one nonzero N-by-N minor of F_7(0) → F_7 has full column rank at every nonzero algebraic real time → actual U multiplicity ≤7.
6. Accepted complete-core eigenjet splitting → a local real-time simple-eigenvalue count → one nonzero minor of χ′(U) → the same lower bound at every nonzero algebraic real time.
7. Accepted complete oldform tower + now-accepted newest-sector splitting premise → disjoint complete groups of dimensions 7 and 24N/25 → combined bound. The frozen source’s conditional implication is applied only after the new premise was accepted.

Leaves 1, 2, 4 and the applications in 5–7 are reconstructed below. The prior cat/tower/core proofs are accepted, source-bound inputs; their finite arithmetic is not represented as freshly rerun here. The sole external theorem leaf is inherited LW. No common-commutant theorem, simple-A theorem, numerical CRT experiment, torus multiplicity theorem or full exponential discriminant is used.

## Obligation matrix

| Obligation | Status | Decisive reason |
|---|---|---|
| Algebraicity despite repeated A eigenvalues | Passed | Lagrange formula for projectors over distinct eigenvalues |
| Actual A and M fit the coefficient domain | Passed | Gaussian-rational Fourier coefficients, roots of unity, algebraic square roots |
| Characteristic coefficients and substitution | Passed | Universal integer-coefficient polynomials in matrix entries |
| Every minor is a collected finite exponential polynomial | Passed | Polynomial closure; equal frequencies collected before LW |
| Exact LW hypothesis mapping | Passed, inherited external input | α_β=itβ are distinct algebraic numbers for nonzero algebraic t |
| Maximum rank over C versus over R | Passed | Nonzero entire minor cannot vanish on a real interval |
| χ′(U) counts simple eigenvalues | Passed at real time | Unitary diagonalization; multiplicity-one eigenspaces have dimension one |
| Higher derivative-stack rank and partition | Passed at real time | A root of multiplicity m is detected first by derivative m |
| gcd equivalence | Passed in the stated full-rank form | gcd exponent at λ is max(m_λ−k,0) |
| t=0 rank witness versus nonzero target | Passed | The witness proves a minor is not identically zero; no LW assertion at t=0 |
| F_7 gives uniform actual multiplicity ≤7 | Passed with accepted cat input | Full column rank at t=0 transfers |
| Complete local branches are simple in the full U | Passed | Positive separation of distinct initial cat eigenvalues |
| Core/new-sector disjointness | Passed | Deepest even oldspace is contained in W_1 |
| Newest-even-sector splitting itself | Passed, accepted input | Newly available report accepts exactly the frozen source revision; its finite checks are inherited |
| Quantitative spacing/full simplicity/BGS | Out of scope | No corresponding implication in the reviewed argument |

## Independent proof reconstruction

### 1. Every coefficient really is algebraic

Let a_1,…,a_d be the distinct eigenvalues of A. They are real algebraic numbers: the characteristic polynomial has algebraic coefficients, and A is Hermitian. Without choosing eigenvectors, define

    P_j = product_(l≠j) (A−a_l I)/(a_j−a_l).

Each entry of P_j is algebraic, even if a_j is repeated. The spectral theorem gives

    exp(itA)M = sum_j exp(it a_j) P_j M.

Thus every entry is a finite exponential polynomial over the algebraic numbers. Multiplying such entries adds frequencies, which remain real algebraic. Addition and determinant expansion preserve the class. Frequency repetitions cause no problem: combine equal frequencies exactly before applying LW.

Write χ_t(z)=z^N+c_1(t)z^(N−1)+…+c_N(t). Every c_l(t) is a polynomial with integer coefficients in the entries of U(t). Differentiating in z introduces only integer falling-factorial coefficients. Substitution of U(t) into χ_t^(j) uses finite sums and products. Consequently each entry of χ_t^(j)(U(t)), each stacked entry, and every minor have the required algebraic exponential-polynomial form. There is no division by a characteristic discriminant, no choice of U(t) eigenvectors, and no claim that the values U(t) themselves are algebraic.

For the actual model, Section 1 of the frozen raw-kernel source displays M_N as N^(−1/2) times roots of unity. The Weyl matrices have root-of-unity entries. The centered symbol has Gaussian-rational Fourier coefficients because cos α=−3/5 and sin α=4/5, independently of whether α itself is algebraic. Thus A_N and M_N have algebraic entries, with the already prescribed Hermiticity/unitarity. This covers the actual family at every fixed N.

### 2. LW gives maximal rank, with the correct real/complex boundary

Write a minor as f(t)=sum_β c_β exp(itβ), where the β are now distinct and c_β are algebraic. For nonzero algebraic t_*, the numbers it_*β are distinct algebraic numbers, including a possible zero exponent. Registered LW says their exponentials are linearly independent over all algebraic numbers. Hence f(t_*)=0 forces every c_β=0. Conversely, identically zero plainly vanishes at t_*.

Let r=max_(t in C) rank F(t); this maximum exists because matrix ranks take values in a finite set. If r>0, a nonzero r-by-r minor exists at some witness time, so it is not identically zero and is nonzero at every nonzero algebraic target time. All (r+1)-minors are identically zero by definition of r. Thus the target rank is exactly r. If r=0 the conclusion is immediate.

A chosen nonzero entire minor has isolated zeros, so its restriction cannot vanish on a real interval. It is nonzero at real times arbitrarily near zero, and indeed on a sufficiently small punctured real interval, with an interval depending on F. Thus the maximum complex rank equals the maximum real rank. This argument does not identify complex-time rank with eigenvalue multiplicities: U(t) need not be unitary for nonreal t.

For the finitely many stacks k=1,…,N, choose one maximal-rank minor for each nonzero rank and multiply these minors. The product is not identically zero. Off its discrete zero set all the stack ranks are simultaneously maximal. This supplies a single generic real-time multiplicity partition and justifies the word “generic.” No uniform-in-N exceptional neighborhood is asserted or needed.

### 3. Exact rank and gcd formulas

For real t, write the unitary eigenspace decomposition as a direct sum of spaces E_λ of dimension m_λ, where m_λ is the algebraic root multiplicity in χ_t. For

    F_k = vertical stack of χ_t^(j)(U(t)), j=1,…,k,

the restriction to E_λ sends x to

    (χ_t′(λ)x, …, χ_t^(k)(λ)x).

If m_λ>k, all these scalars vanish. If m_λ≤k, the m_λ-th scalar is

    m_λ! product_(μ≠λ) (λ−μ)^(m_μ),

which is nonzero. In the latter case the restriction is injective with rank m_λ. Contributions from distinct eigenspaces are independent, giving

    r_k := rank F_k = sum_(λ: m_λ≤k) m_λ.

With r_0=0, (r_k−r_(k−1))/k is exactly the number of distinct eigenvalues of multiplicity k. In particular r_1 is the number of simple eigenvalues, not the total number of distinct eigenvalues. The same rank maxima at all nonzero algebraic real times therefore give the same partition.

Separately, in characteristic zero,

    gcd(χ,χ′,…,χ^(k)) = product_λ (z−λ)^max(m_λ−k,0),

with monic gcd. Hence gcd=1 iff all multiplicities are at most k, equivalently F_k has full column rank in this unitary setting. The source uses exactly this equivalence. One must not strengthen it to r_k=N−deg gcd: those quantities need not agree. No invertibility of χ^(7)(U) alone is assumed or needed.

### 4. The t=0 witness proves the actual uniform multiplicity bound

The accepted cat theorem gives m_λ(M_(7·5^e))≤7 for every e≥1. Applying the preceding stack formula at the perfectly valid unitary time t=0 gives rank F_7(0)=N. Thus at least one N-by-N minor selected from the 7N rows is nonzero at zero.

This is a witness that the minor is not identically zero, not an invocation of LW at zero. LW then makes that same minor nonzero at every nonzero algebraic target t. Therefore F_7(t) is injective and every U(t) eigenvalue has multiplicity ≤7. The actual t=10^(−80)N is positive rational for every N; it satisfies the hypothesis even when it lies outside the small perturbative neighborhood for that N.

This argument is independent of first-order or higher-order splitting, simplicity of A, newest-sector evidence, and any numerical choice of a target coupling. It is unconditional with respect to the newer sector candidates, while retaining the accepted cat theorem and registered external LW dependency.

### 5. Why a local count transfers as a full-matrix count

Fix N and finitely many distinct cat eigenvalues whose entire eigenspaces are in the collection. Their initial eigenvalues are positively separated from one another and from every other cat eigenvalue. Spectral continuity gives disjoint small neighborhoods containing exactly the corresponding number of U(t) eigenvalues for sufficiently small real |t|.

Within a group whose accepted effective Hermitian phase matrix first has a simple nonscalar jet at order q, subtract the scalar phase terms and divide by t^q. The resulting Hermitian matrix tends to its simple leading matrix as t→0. Eigenvalue continuity therefore separates all branches in that group for sufficiently small nonzero real t. This uses the full eigenspace: a proper subspace of a repeated cat eigenspace would not suffice. In the sources used here the even/odd cores have zero first order and simple second order; the now-accepted new sector has simple first order.

Take the minimum of the finitely many local neighborhoods and separation thresholds at this fixed N. Every one of the D branches is then a simple eigenvalue of the full U(t), regardless of collisions confined to other initial groups. Thus rank χ_t′(U(t))≥D at a real witness time. Its maximal rank is at least D, so LW gives that lower bound at every nonzero algebraic real time. The witness time need not be algebraic, and no explicit radius is needed.

The even-core review supplies three complete groups of sizes 3,2,2 for N=7·5^(2r), r≥2: D=7. The odd-core review supplies six complete groups of sizes 7,7,7,4,5,5 for N=7·5^(2r+1), r≥2: D=35. Their accepted report statements are exactly the needed complete-group hypotheses.

### 6. Addition of the newest even sector after its acceptance

For even e=2r≥4, the deepest core is W_r=H_7⊗J_r H_1 and has dimension seven. The oldform maps satisfy the nesting J_1 J_(r−1)=J_r with the appropriately lowered ambient space, directly from their support formula and normalization. Hence W_r⊂W_1. The accepted tower theorem says both oldform spaces are sums of complete cat eigenspaces. Their orthogonal complements therefore contain different complete cat eigenspaces, not other portions of the same repeated group.

The newest sector is exactly W_1-perpendicular, of dimension N−N/25=24N/25. Its stated first-order theorem has now been accepted by the independently source-bound report listed below. Thus all its branches and the seven deepest-core branches are disjoint in the complete-group argument above. Their lower bounds add to 24N/25+7. Since every eigenvalue has either multiplicity one or at least two, the dimension carried by repeated eigenspaces is N minus the number of simple eigenvalues, giving at most N/25−7. This is a dimension bound, not a claim to locate or count individual repeated roots.

The disjointness implication is established here; the new-sector finite packets and uniform reduction are inherited from their separate audit, not freshly re-audited here. Its report `ee5bf38c202fa9094fbae66666a8b2564874316258865928542d1c405500fb2e` accepts source `7e043149e73445cdd0f413f8ce9460b4c1de9690355c83d992e88ad3fbb2ad39` for every even e≥2. That exact scope includes the required even e≥4. The source's own phrase restricting it to local splitting is respected: the present rank theorem supplies the separate transfer to arbitrary nonzero real algebraic times. At nonzero times these are branches originating in cat subspaces, not an assertion that those subspaces remain invariant under U(t).

## Exact small/adversarial controls

These are direct algebraic checks, not numerical spectral experiments or an exhaustive computation claim.

1. For U=diag(1,1,−1), χ=(z−1)^2(z+1). The first derivative takes values 0,0,4 on the diagonal, so r_1=1 although there are two distinct eigenvalues. The second derivative is 6z−2, nonzero at both roots, so r_2=3. Thus (r_2−r_1)/2=1 repeated root of multiplicity two. Meanwhile gcd(χ,χ′)=z−1 has degree one, so N−deg gcd=2≠r_1. This verifies the critical distinction in the source's rank language.
2. For the nonunitary Jordan matrix U=[[1,1],[0,1]], χ=(z−1)^2 and χ′(U)=2(U−I) has rank one despite there being no simple eigenvalue. This confirms why the multiplicity interpretation is restricted to real unitary times; the complex-time rank maximum itself remains valid.
3. A=diag(0,1), M=I gives U(t)=diag(1,e^(it)). At zero it is repeated, at every nonzero real algebraic time it is simple by LW, and at t=2π it is repeated again. Thus zero can be an exceptional witness time and an arbitrary transcendental real time is not covered by the target claim.
4. A=aI, M=I_N with algebraic real a gives a persistent multiplicity-N eigenvalue. All rank claims still hold, so the general theorem cannot by itself force a simple generic partition.

## Exact external-source boundary

The frozen registry entry EXT-POPESCU-2023 pins Sever Angel Popescu, *A simple and self-contained proof for the Lindemann–Weierstrass theorem*, arXiv:2306.14352v2, 17 September 2023, Theorem 3.2. The registered statement is linear independence over all algebraic numbers of exponentials of distinct algebraic exponents. The project's retained fresh statement check in `trace_variance_review.md` locates the theorem on printed page 14 and its proof on pages 15–16 of the exact v2 PDF, https://arxiv.org/pdf/2306.14352v2.

This audit inherits that source verification and checks the application independently with α_β=itβ. It does not claim a new download, new primary-source audit, or proof of the external transcendence theorem. No rational independence of frequencies, nonzero requirement on every individual frequency, simple generator spectrum, effective LW inequality or lower bound is required. The sole nonzero requirement is on t when distinct frequencies are separated. The accepted source is reused, so no new external theorem leaf is introduced.

## Input bindings and reproducibility

`source_manifest.json` records original paths, snapshot paths, byte lengths and SHA-256 hashes for all 17 inputs. The key mathematical bindings are:

- Reviewed transfer v2: `673f0831080263e6d28b85ce91ae4a5fa705d637aa34fb9fd6d54700cda3b62d`.
- Registered identity-principle proof: `0b12ac9254845c2ac2bc95dc149dcd4a19116f447d2bce1a2c530c3f204ca1b2`.
- Raw actual model: `32b2302c2567eebb75ff2231345e3336495ba8719517be6b5ce8734b416920c2`.
- External registry snapshot: `f6108898169e5a0d4879085f4c356f26cd0f7bb875787db362babe2f04ad9218`.
- Cat v2 source: `b6e219832f094136f0ca80201ae61f80a9d2435bebc59dd2f18163e3444c8e1e`; acceptance binding: `dbe6d39858060fa0540dc551cb2ecf227bf476821ddff306dcb673a86f6ec2be`.
- Accepted even-core report: `c3a98ad153737e4cdac381bf6318eff2d3c44e073a81a7387dbee785ab6a172c`; its source: `c504620ef3111c7cf40af636eb7d00a1b4103463986c3ff3f7d8e3f01fee0e3a`.
- Accepted odd-core report: `2b8f451ebca20251be2dec5864e8d8a6497eabeb4259cc5edcbc28da33ede101`; its source: `38b1e1b442f942a81a3ea7f89c9bd6a91f4a6ed39f12beb644d0c44064d0b46e`.
- Accepted tower report: `f3d142204ed6d10015e70595633c714acaf097fa1b0e6f19fdf6a51d4e663be5`; its source: `d359482763667a6707ed9a060a3874e951f95336561a4ac645df453022b085ae`.
- Accepted newest-even-sector source: `7e043149e73445cdd0f413f8ce9460b4c1de9690355c83d992e88ad3fbb2ad39`; its newly available acceptance report: `ee5bf38c202fa9094fbae66666a8b2564874316258865928542d1c405500fb2e`.

The source snapshot target hash was checked against the assigned frozen hash. The prior reports' accepted-source hashes agree with the frozen current sources. No prior finite checker was rerun; the new transfer argument has no computation-dependent step. `validate_sources.py` only verifies the provenance bindings and emits `source_validation.json`.

## Remaining gap and strongest safe conclusion

No missing implication was found in the stated transfer theorem, the multiplicity-seven corollary, the accepted-core lower bounds, or the combined 24N/25+7 even-depth bound after receipt of the exact newest-sector acceptance. The only pending premise in the frozen source is now satisfied by that source-bound report. Full simplicity of the remaining old sectors and any quantitative spectral spacing estimate remain separate problems.

The cheapest next integration check is to preserve these exact source bindings, list the inherited LW dependency explicitly, and retain the newest-sector acceptance beside the stronger 24N/25+7 conclusion. Do not replace the derivative-stack rank formula by a distinct-root count or by N minus the degree of a characteristic-polynomial gcd.

## Publication mapping

Exact original proof/review bytes and dependency maps are preserved in
record/cat_jet_promotion_mapping.json. Portable replays retain all exact
mathematical outputs; execution path/timing hashes are reported separately.
Each component keeps its independently reviewed scope; diagnostics in the
author handoff are not promoted as further literal-U cases.
