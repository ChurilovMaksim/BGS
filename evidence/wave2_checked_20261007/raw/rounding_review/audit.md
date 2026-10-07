# Independent audit: microscopic rounding and simple-spectrum endpoint barriers

## Normalized claims and verdict

**Primary verdict: correct only after a stated restriction.** The rounding construction and all its displayed mathematical bounds are proved; its final strategy sentence is accepted only as insufficiency of the enumerated stable hypotheses, not as a theorem that a successful proof must specifically use exact raw-Weyl/all-order quantization. With that restriction the rounding companion is accepted. The simple-spectrum companion is **proved as written**, relative to its reviewed inherited inputs. No correction to a displayed formula or construction was found. The explicit eventual-dimension convention, switch-cutoff choices, and conditional meaning of Schatten preservation below prevent stronger interpretations.

1. `rounding_offcharge_upgrade.md`, SHA256 `d4bae7595a4a0787105c429384d82af70ef7f7968e4cda2f0c9e78635d637a92`: for each fixed nonzero nonnegative smooth weight supported in a fixed positive compact time band, a fixed sufficiently fine microscopic root grid gives an altered unitary family at operator distance O(1/N) from the actual one. It preserves the stated coarse data while its **real signed**, occupation-mismatched, high-Hamming/high-switch normalized aggregate has strictly positive liminf, in fact greater than one with the displayed choice. Its corresponding damped endpoint vanishes, so the signed boundary target fails for that altered family.
2. `simple_spectrum_companion.md`, SHA256 `6f163c8e3c9acf0a01818443763986cc85aea2ababd44fbe701b646d7a28ce58`: the prescribed O(N^-3) spectral split of the reviewed growing-period family has simple spectrum, no root-of-unity ratio between different eigenvalues, and no scalar positive power. The genuine offcharge residual still grows at least as (sqrt(N)/2) times the integral of the weight, minus O(1), along N=p², p prime congruent to 2 modulo 3.

This is a new independent internal audit of the short implications, not an external referee certificate, a new rounding mechanism, or a re-audit of every earlier semiclassical theorem. Both constructions change the quantizer. Literal BGS, the actual signed endpoint, the full balanced law, and the higher factorial target remain open. No actual Schatten theorem is asserted.

The read-only source root is `/workspace/shared/bgs_checked_checkpoint_validation/source_snapshot`. Its parent source-manifest SHA256 is `d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba`, verified against the supplied pin. All 24 specifically consumed source files were checked against that manifest. The source snapshot has no Git metadata; its pinned base is `d37c92e563d10d25bb1d6ab85bedffc1f160f773`, with staged checkpoint additions retained. No repository editing, status promotion, or publication was performed.

## 1. Objects, normalization, and dependency graph

For a unitary U on C^N and a rooted cyclic coordinate word x of length m, set A_U(x)=product_j U[x_j,x_(j+1)]. Every ordered rooted pair (x,y) is counted once. Define c=y-x in (Z/N)^m, h(c)=number of nonzero c_j, and s(c)=number of changes c_j!=c_(j+1). Occupation mismatch means inequality of the **integer** coordinate-count vectors, not merely nonzero checksum modulo N.

The full pair sum is |Tr U^m|². With normalized Haar measure on all independent coordinate phases,

    B_m(U) = integral |Tr((Z_theta U)^m)|² dtheta

is exactly the occupation-balanced sum. Thus O_m(U)=|Tr U^m|²-B_m(U) is exactly the deterministic offcharge sum. Phase integration is a projector in this identity, not a replacement random model. Its positivity is used only for B_m and the full squared trace. The individual offcharge summands and residual are not nonnegative measures. Swapping x and y conjugates the summand and preserves all masks, so each masked sum is real.

Use ordinary matrix traces and the original N^-2 time-sum normalization. On End(C^N), multiplying the Hilbert–Schmidt norm by N^-1/2 changes no induced operator norm. The superoperator dimension is N², which matters for Schatten estimates and trace prefactors.

Dependency graph:

- Reviewed universal phase-Abel theorem → dimension-uniform balanced compact-band upper bound.
- Root-grid rounding → microscopic norm proximity and exact macroscopic return times → full weighted trace lower bound.
- Exact occupation identity → full signed offcharge lower bound.
- Adjoint/charge compression continuity + inherited actual P and nonzero-charge gaps → exact low-Hamming and checksum-free low-switch removal.
- The same one-step centered pinch gap → damped all-switch endpoint → failure of the exact signed boundary integral.
- Adjoint continuity + inherited ordinary-Weyl compact/strong limits → unchanged principal classical dynamics and compact charge-pinch limit.
- Unitary-word telescoping → fixed-word laws and the reviewed triple-log window survive.
- O(N^-3) rational phase split of roots of unity → exact simplicity/non-root-of-unity ratios; microscopic trace continuity → unchanged lower bounds.

The Abel theorem and the growing-period construction are source-matched accepted inputs. Their exact acceptance receipts are pinned in `source_pins.json`. Current checkpoint acceptance, rather than historical candidate headings inside copied proofs, determines their status. No new external theorem is needed beyond these inherited leaves and elementary irrationality of pi.

## 2. Rounding, fixed positive band, and the Abel constant

Fix w>=0, w not identically zero, smooth and supported in [a,b] with 0<a<b<infinity. The support and w are fixed independently of N. The reviewed Abel input states, for every unitary W and every s>0,

    N^-2 sum_(m>=1) exp(-2sm/N) B_m(W) <= 1/(2s)+1/(2N).

For s=1 and N>=3, positivity and m/N<=b on the support give

    N^-2 sum_m w(m/N) B_m(W)
       <= ||w||_infinity exp(2b)(1/2+1/(2N))
       <= C_w := (2/3)||w||_infinity exp(2b).

The 1/6 finite-size term is valid because N>=3. There is no missing N from a normalized trace. This estimate does not identify the CUE limit.

For a positive integer L, write S_L=sum_(r>=1)w(r/L). The ordinary compactly supported Riemann-sum theorem gives S_L/L→integral w>0. Choose **one fixed L**, allowed to depend on w, such that S_L>C_w+1. First fix L, then let N tend to infinity. The argument does not take L growing with N or choose a shrinking band.

For N>=L put K_N=floor(N/L). Round every eigenangle of U_N to a nearest 2pi/K_N grid point in a chosen orthonormal eigenbasis. Circular angular distance is at most pi/K_N, hence

    epsilon_N := ||Uhat_N-U_N|| <= 2 sin(pi/(2K_N)) <= pi/K_N,
    Uhat_N^K_N = I.

At the finitely many N<L, define any unitary; this only makes the asymptotic sequence fully specified. Since K_N/N→1/L and is at least 1/(2L) for N>=2L, at most 2bL return indices r contribute eventually. Consequently this is a finite, uniformly bounded-index limit:

    sum_(r>=1) w(rK_N/N) → S_L.

At m=rK_N the normalized squared trace N^-2|Tr Uhat_N^m|² equals one. Every other full squared-trace term is nonnegative. Therefore

    liminf N^-2 sum_m w(m/N)|Tr Uhat_N^m|² >= S_L,
    liminf N^-2 sum_m w(m/N)O_m(Uhat_N) >= S_L-C_w > 1.

This completes the missing balanced/offcharge separation in the older full-pair rounding obstruction. The conclusion is weight-by-weight: the rounding family can depend on the chosen w and L. It does not claim a single rounded family defeats every positive compact weight simultaneously.

## 3. Perturbation bounds and inherited coarse data

Let U,W be arbitrary unitaries and epsilon=||W-U||. With T_U=Ad(U),

    T_W(X)-T_U(X)=(W-U)XW*+UX(W*-U*),
    ||T_W-T_U||_(HS→HS) <= 2epsilon.

Every fixed charge block is a compression of T_U, including zero charge P_U=|U|². The charge pinching D_U=sum_c P_c T_U P_c is a block direct sum; equivalently it is a contractive operator pinching. Thus

    ||P_W-P_U|| <= 2epsilon,
    sup_c ||B_c(W)-B_c(U)|| <= 2epsilon,
    ||D_W-D_U|| <= 2epsilon.

The dimension is not multiplied into these estimates. Both U and W remain exactly unitary, so P remains doubly stochastic and the identity direction remains reducing. Every inherited strict eventual gap survives with an arbitrarily slightly enlarged fixed bound below one. A strict-margin limsup bound also survives unchanged as a limsup.

### Reverse kernel: the submitted bound and the sharper prior result

To avoid confusing the reverse kernel with the kick factor, write R(U)[j,k]=U[j,k] conjugate(U[k,j]). If max|U[j,k]|<=C/sqrt(N), Delta=W-U, and ||Delta||_HS<=sqrt(N)epsilon, the submitted Hadamard expansion gives

    ||R(W)-R(U)|| <= ||R(W)-R(U)||_HS
       <= 2C epsilon + sqrt(N)epsilon².

Indeed the two linear terms each have HS norm at most C epsilon, while the quadratic term is at most max|Delta| times ||Delta||_HS. For the exact flat growing-period V, C=1; epsilon=N^-3 yields exactly 2N^-3+N^-11/2. The source arithmetic is correct.

There is already a stronger **preexisting** bound in `mathematics/microscopic_rounding_control.md`, lines 155–165. For the isometry J:e_j↦e_j⊗e_j,

    A⊙B=J*(A⊗B)J,       ||A⊙B||<=||A||||B||.

Since R(U)=U⊙U*,

    R(W)-R(U)=(W-U)⊙W*+U⊙(W*-U*),
    ||R(W)-R(U)|| <= 2epsilon.

Thus reverse-norm continuity needs no flatness hypothesis. This is credited, not presented as a new result or silently substituted into the frozen companions. Entrywise flatness separately survives because max|W[j,k]|<=C/sqrt(N)+epsilon. For epsilon=O_L(N^-1) it stays O_L(N^-1/2).

### Principal dynamics, compact pinching, and the conditional Schatten assertion

For each uniformly bounded fixed-symbol observable A,

    ||W*AW-U*AU|| <= 2||A||epsilon.

Hence the actual fixed-symbol one-step O_A(1/N) Egorov law retains the same principal classical map under rounding, with changed constants. The smooth-symbol quantization map and classical dynamics have not been redefined.

In the **same** ordinary-Weyl embedding I_N as the accepted radial source,

    ||I_N D_What I_N* - I_N D_U I_N*|| <= 2epsilon_N →0.

Therefore the compact limit K is unchanged. Similarly the extended adjoint transfer and its adjoint keep their strong limits C_G and C_G*. Classical mixing remains a property of that same G. Thus the compactness/centered-quasimode arguments can be reused in their original q=1,theta=0 scope. This supplies no arbitrary occupation-twist compactness, no power-norm bound from spectral radius, and no signed endpoint estimate.

As an operator on the N²-dimensional HS space, the difference has rank at most N². For every fixed finite p>2,

    ||D_What-D_U||_(S_p) <= (N²)^(1/p)·2epsilon_N
                          = O_L(N^(2/p-1)) →0.

If a uniform S_p bound on D_U is separately given, boundedness and its limsup bound therefore transfer. This is **conditional preservation only**. Neither compactness nor this inequality proves any such bound for D_U. It also does not preserve an identical finite-N numerical constant without slack. The audit does not promote the held-out Schatten sketch or infer regularity from it.

## 4. Fixed words and the reviewed triple-log window

Keep the actual cat M_N unchanged. Distinguish kick factors K_N^kick=U_N M_N* and Khat_N^kick=Uhat_N M_N*. Their difference has norm epsilon_N; the same holds for the inverse factors. For every free word v with letter length ell, unitary telescoping gives

    ||v(Khat_N^kick,M_N)-v(K_N^kick,M_N)|| <= ell epsilon_N,
    |tr_N v(Khat_N^kick,M_N)-tr_N v(K_N^kick,M_N)| <= ell epsilon_N.

This is uniform over all words of length at most ell; **no word-count factor appears**. It proves the fixed normalized *-moment limits in the frozen companion.

It also proves a separate extension not explicitly stated there. Let

    ell_N=floor(log log log N/(4 log 8)).

The exact accepted growing-word source proves uniform normalized trace decay on its nonidentity words. The perturbation error is at most ell_N epsilon_N=O_L(ell_N/N)→0, so the same uniform decay survives. More generally the continuity statement transfers any independently proved normalized-word window ell_N with ell_N epsilon_N→0; it does not establish any new actual-model window by itself.

This nearest-root construction is not the special unbiased rounding used to preserve an unnormalized trace vector with o(1) error. Here elementary telescoping gives only |Tr(Uhat^m)-Tr(U^m)|<=Nm epsilon_N=O_L(m). Do not attach the stronger unnormalized low-trace conclusion to this construction without its separate argument. The original explicit all-order word-Egorov formula is not preserved verbatim; the normalized trace conclusion is.

## 5. Exact removal of the small-Hamming and small-switch parts

### Hamming

The universal raw-offcharge Hamming inequality in `fractional_hamming_cancellation.md`, equation (3), uses only unitarity and t=||P-J||:

    |low-Hamming offcharge sum| <= 2(N²-1) M t^(m-2r),
    M=sum_(s=0)^r binom(m,s),       r=floor(.49m).

It is an estimate for the exact occupation-mismatched signed trace, established by the torus projector, not an estimate inferred from subset inclusion. There is no Haar-tail prerequisite for this offcharge inequality. It is distinct from the source's balanced centered-range theorem.

The actual eventual t_N<=10^-63 and O_L(N^-1) perturbation give, for sufficiently large N, t_hat<=2·10^-63. With d=.49, M<=exp(m h(d)) and m-2r>=.02m. The required margin is

    eta=.02 log(1/(2·10^-63))-h(.49)>0.

For example h(.49)<log 2, and 63 log 10>51 log 2 proves the strict inequality without a numerical rounding issue. Thus the small-Hamming aggregate is exponentially negligible on m>=aN. Startup may be extraordinarily large and is not made effective.

### Switches and occupation source

Let rho<1 be an eventual bound for the **whole centered pinch**, taking the maximum of the centered zero-charge P bound and all nonzero diagonal charge blocks. The accepted global-switch proof is universal once these bounds hold. Its occupation phases multiply charge rows by unitaries; zero-charge phases are exactly one. Row/column orthogonality gives the exact annihilation identities linking zero and nonzero charge runs. Accordingly every nonzero difference word has

    |F_off(c)| <= 2N rho^(m-s(c)),

including checksum-zero occupation-mismatched fibers. A constant zero word is exactly balanced. This is a bound on each complete occupation-projected c-fiber, so further restrictions depending on c, such as Hamming or switch conditions, are legitimate. It is **not** permission for arbitrary restrictions on x inside an already signed fiber.

For fixed 0<kappa<=a log(1/rho)/8 and R_N=floor(kappa N/log N), the displayed T12 counting estimate makes the low-switch sum exponentially small uniformly for aN<=m<=bN. The small-switch part is removed only within high Hamming after removing low Hamming, so the decomposition is disjoint. The exact remaining mask is

    occupation mismatch, h(y-x)>floor(.49m), s(y-x)>R_N.

Both of these literal removals use the inherited P/charge norms and unitarity. The reverse kernel and flatness are other preserved data, but are not extra prerequisites of these two universal inequalities. Thus their normalization and source-mask assumptions do not leak actual raw-Weyl identities into the changed-family argument.

The full offcharge lower bound from Section 2 loses only o(1) after these two removals. Consequently the high-Hamming/high-switch aggregate has liminf at least S_L-C_w>1. For rounding, the admissible fixed kappa may shrink when rho is enlarged. The theorem does not say every arbitrary kappa works for that family.

### Damped endpoint and boundary

The same centered-pinch bound yields, uniformly in occupation phases and Hamming marker, the global transfer contraction. For

    z_N=1-A log N/N,       A>2/[a(1-rho)],

the high-Hamming offcharge normalized aggregate is bounded by O(N² exp(-(1-rho)aN(1-z_N)))→0. The subtracted low-switch/high-Hamming part is uniformly exponentially small for 0<=z<=1. Thus the **same** residual has negligible z_N endpoint.

The exact finite-polynomial identity in T15 identifies the undamped residual minus its damped value with the signed marked-switch integral. The positive liminf therefore proves failure of T16 for the rounded family. It does not derive a trace bound from a radial eigenvalue shell or interchange a modulus with the full signed sum.

## 6. Simple-spectrum companion

The accepted growing-period V_N is defined only along N=p², p>=5 prime with p=2 modulo 3, and satisfies V_N^(2p)=I. Choose any orthonormal eigenbasis v_j. Its eigenvalues omega_j are 2p-th roots, including repetitions. Define

    W_N v_j=omega_j exp(i j/N^4)v_j,       1<=j<=N.

Then ||W_N-V_N||<=N^-3. For j!=k, a ratio of eigenvalues is a root of unity times exp(i(j-k)/N^4). If this ratio were a root of unity, the nonzero rational number (j-k)/N^4 would belong to 2pi Q. This contradicts irrationality of pi. Every ratio is therefore non-root-of-unity, so eigenvalues are distinct and no positive power is scalar. This is exact and does not depend on a numerical separation tolerance.

The continuity bounds give t_W<=2N^-3 and sup_(c!=0)||B_c(W)||≤sup_c||B_c(V)||+2N^-3→0. The submitted reverse estimate and flatness follow as in Section 3, with the sharper prior 2epsilon bound also available. The phrase “charge gap tends to one” means that 1-rho_N→1; the charge-block norms tend to zero.

For m<=bN, telescoping yields

    |Tr W_N^m-Tr V_N^m| <= mN·N^-3 <= b/N.

At all m divisible by 2p in the band, |Tr W_N^m|>=N-b/N. Each normalized return loses at most 2b/N², up to a still smaller term. There are O_w(p)=O_w(sqrt(N)) such terms; hence the return lower bound has additional error O_w(N^-3/2)=o(1). The accepted Riemann sum therefore retains

    N^-2 sum_m w(m/N)|Tr W_N^m|²
       >= (sqrt(N)/2) integral w - O_w(1).

The universal Abel theorem applies directly to W_N, so the full offcharge sum has the same divergent lower bound. No separate transfer estimate for B_m is assumed.

With t_W<=2N^-3, the small-Hamming bound is

    2(N²-1) exp{-m[.06 log N-.02 log 2-h(.49)]},

which is exp(-.06 a N log N+O_w(N)) up to polynomial factors. For any prescribed fixed kappa>0, choose a fixed rho<1 with log(1/rho)>8kappa/a, then use convergence of the centered pinch norm to zero. T12 removes the low-switch part. Thus **every fixed kappa** is allowed here, in contrast with rounding's fixed inherited gap. Taking rho<=1/2 eventually makes any fixed A>4/a sufficient for the damped endpoint. The same boundary identity gives a divergent signed integral.

Finally, for 1<=m<2sqrt(N), the normalized trace perturbation is at most mN^-3<2N^-5/2. This verifies the source's uniform short-power correction and preserves all fixed nonzero normalized moments. It does not create actual kick/cat two-generator freeness for this growing-period model.

## 7. Separate combined corollary: exact recurrence is not needed even in the rounded actual-data barrier

This is a derived corollary, not an unmarked alteration to either frozen companion. Apply the very same rational phase split to the K_N-th root eigenvalues of Uhat_N. Call the result Utilde_N. Then

    ||Utilde_N-Uhat_N||<=N^-3,
    ||Utilde_N-U_N||=O_L(N^-1).

The root-of-unity argument proves simple spectrum and non-root-of-unity eigenvalue ratios. All continuity-based inherited properties from Sections 3–5 survive. For any two unitaries at distance epsilon, the squared-trace difference is at most 2mN²epsilon. Consequently the normalized compact-band full-trace aggregate changes by at most

    2epsilon sum_m |w(m/N)|m = O_w(epsilon N²).

For epsilon=N^-3 this is O_w(N^-1). Alternatively the finite O_w(L) rounded return indices give an even smaller return-only loss. The same universal Abel upper bound and exact mask removals therefore yield the same strictly positive offcharge liminf for Utilde_N. It retains the actual principal dynamics, compact pinch limit, reviewed triple-log word conclusion, and any **given** S_p bound, together with simplicity and absence of exact scalar recurrence.

This does not force divergence for the fixed-L rounding family; its proved conclusion is a positive lower bound. Divergence belongs to the distinct growing-period family.

## 8. Precisely what exact quantization information is not retained

“Lost” here means no longer available as a certified hypothesis of the constructed family; norm closeness alone does not prove that every individual identity is false in every finite dimension.

- The prescribed kick identity Q_N=exp(i tau N A_N), with tau=10^-80 and the same A_N=sum c_kl W_N(l,k), is not established for Qhat=Uhat M_N*. Defining this factor does not identify it with the original kick.
- The exact finite-support lattice action A_N u(x)=sum c_kl e(k(x+hl/2))u(x+hl), with l in {-1,0,1} and the fixed coefficients of g, is an identity for the original generator. No generator of the rounded/split kick with those coefficients and shifts is constructed. A generic finite-dimensional logarithm would not supply that property.
- The exact time-dependent equation partial_t U_N(t)=iN A_N U_N(t), its U_N(0)=M_N condition, and the prescribed fixed-generator evolution are not inherited by rounding performed at one time.
- Therefore the raw finite-difference derivation of all transport operators P_j/D_j, higher amplitudes, exact kick-controlled lattice gluing, and uniform all-order smooth-symbol/parametrix remainders cannot be reused for the altered unitary merely from ||Delta U||=O(1/N). Fixed-observable first-order Egorov survives; exact subprincipal data and arbitrary higher-order remainders do not follow.
- Arithmetic consequences tied to the literal kick's exact algebraic coefficients or its exact commutant hypotheses cannot be imported solely by perturbation. No claim about those exclusions is made here.

Important retained identities must not be mislabeled as lost: the Weyl matrix algebra and coordinate charge projections are unchanged ambient objects; the cat M_N is unchanged in the rounding construction, so its own exact Gauss and Egorov identities remain true. The formal factorization Uhat=Qhat M_N is tautologically exact. Generic unitary identities, exact occupation projection, and the generating-transfer dictionary remain exact. What is missing is the actual prescribed kick and its link to those ambient identities at all orders.

For the split growing-period family there was never an identification with the literal raw symbol, cat factor, or Anosov dynamics in the first place. Its perturbation cannot be said to preserve an identification that was never made.

## 9. Obligation matrix, finite controls, and strongest safe use

| Obligation | Status | Scope |
|---|---|---|
| Original N^-2 normalization and rooted masks | Passed | Ordinary traces; exact integer occupation counts |
| Universal Abel constant | Passed as imported reviewed theorem | Every unitary, N>=3 for the stated C_w |
| Fixed band and fixed large L | Passed | Weight chosen first; L independent of N |
| Floor, rounding distance, and return sum | Passed | Eventual N>=L; small dimensions irrelevant |
| P and all charge blocks/pinching | Passed | Dimension-free 2epsilon continuity |
| Reverse-kernel Hadamard estimate | Passed | Submitted bound valid; prior 2epsilon stronger |
| Principal dynamics and compact limit | Passed relative to reviewed inputs | Fixed-symbol, q=1/theta=0 compactness scope |
| Schatten regularity | Conditional preservation only | A supplied fixed p>2 bound transfers; none established |
| Fixed words and triple-log extension | Passed | Normalized traces, uniform telescoping, no word count |
| Literal Hamming/switch removal | Passed | Exact source projector retained; admissible kappa stated |
| Damped-to-undamped boundary identity | Passed | Failure asserted only for changed families |
| Simple spectrum/non-root-of-unity ratios | Passed | Exact irrationality argument |
| Growing-period divergence after split | Passed | N=p², p=2 mod3; any fixed kappa |
| Combined simple rounded family | Passed as separate corollary | Positive liminf, not divergence |
| Exact actual-model quantization/BGS | Out of scope | Not preserved or refuted |

`check_companions.py` independently enumerates all 66,429 ordered rooted path pairs for N=3, m=1,...,5, using an exactly checked Gaussian-rational unitary and Gaussian-integer numerators. It verifies full=balanced+offcharge and the disjoint low-Hamming/high-Hamming-low-switch/residual identities for switch cutoffs 0,1,2. This finite check certifies that implementation and those finite identities, not the universal Hamming/switch estimates.

Floating diagnostics check rounding/charge/reverse/word continuity at N=3,5,9, and the prescribed split at p=5,11 (N=25,121), with powers through 2N. They use disclosed tolerances and are not interval certificates or a numerical proof of non-root-of-unity ratios. A fixed smooth bump on (1,2), max w=1, with L=256 gives S_L≈98.2572 and C_w≈36.3988; this illustrates the strict constant margin without proving the Riemann-sum theorem numerically. The actual minuscule-tau matrix was not numerically evaluated.

Reproduction:

    python /workspace/shared/bgs_wave2_rounding_barriers/run_controls.py
    python /workspace/shared/bgs_wave2_rounding_barriers/validate_manifest.py /workspace/shared/bgs_wave2_rounding_barriers/computation_manifest.json --root /workspace/shared/bgs_wave2_rounding_barriers

The version-1 manifest validates, with its reported legacy provenance limitations. Exact source pins and execution-input hashes are recorded; BLAS/OpenMP threads were cooperatively capped at one and subprocess runtime at 60 seconds. `controls.json`, stdout/stderr, and the completed manifest preserve the actual finite ranges. A successful bounded execution supplies no asymptotic theorem.

**Remaining gap for the mathematical constructions: none within the audited scopes.** The literal necessity claim in rounding line 34 is stronger than the implication proved and must remain narrowed to the discriminator just stated. The next useful check for any proposed Work proof is to identify the first precise estimate whose hypotheses distinguish the actual quantizer from the rounded-and-split family. A proof using only the preserved data cannot establish the signed endpoint. This is a necessary discriminator, not a theorem that one particular exact-Weyl strategy is the only possible successful route.
