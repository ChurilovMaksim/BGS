# Independent source-bound audit of loop-transfer reductions

## Verdict and normalized claim

**Primary verdict: proved as written, in the stated reduction scope.** The single-anchor/countable-test implication, normalized short-leg excision, tensor-resolvent identities, and their normalizations pass. This does **not** prove any actual-map mixed-loop hypothesis. The final BGS implication remains conditional on the full mixed hierarchy and the named external characterization theorem.

This audit reconstructs the deductions rather than accepting the author's verdict or the finite SymPy example. It uses the report in the accepted author report, pinned manifest, and canonical sources at HEAD `d4132ccee82849b644520d88c953cb9b33382a59`. The retained hash receipt records input mismatches caused by concurrent repository changes; see input_reconciliation.json for the integration-base reconciliation. The author's report and manifest are additionally hashed in the accepted hash receipt. No canonical files were edited. The canonical worktree already contains unrelated four-cut changes; this review makes no clean-worktree or entire-corpus-audit claim.

The exact claim is: for arbitrary deterministic unitary spectra of size N, the report's conditions (A) and (B), at every fixed order, imply the compact-uniform relative beta=2 loop condition (H). For the prescribed odd-dimensional map, assuming the published-in-repository FM-007 logarithmic trace bound, the short legs of the first mixed equation can be removed at relative error O(N^(-1/40) log N), uniformly over any fixed compact positive height interval, without any local-moment assumption. The resulting long expression has the exact finite-dimensional partial-trace representation stated in the report.

## 1. Evidence and dependency graph

Governance read: AGENTS, SOURCE_OF_TRUTH, repository conventions, RESEARCH, REVIEWING, current relevant claim registry/ledger entries, results and open-obligation views. Relevant claims: FM-007 is a project proof; LOOP-001 is conditional; TRACE-005/BGS-001 remain open.

The dependency arrows checked are:

1. Cotangent resolvent and uniform origin -> particle-generated Nevanlinna function, reflection, finite-N moments, intensity 1/pi.
2. Nevanlinna derivative/divided-difference bounds + anchor residual (A) -> all anchor moments.
3. Anchor moments + deterministic path comparison -> all compact-supremum moments.
4. Compact-supremum moments + dense mixed tests (B) + same-half-plane identities -> locally uniform residual convergence -> (H).
5. (H) + Bourgade–Huang Theorem 1.9 -> vague point-process convergence; whole-space moment bounds -> compactly tested factorial correlations and anchored normalization 1/N.
6. FM-007 logarithmic trace bound + weighted Cauchy–Schwarz + Lyapunov -> normalized short-leg excision.
7. Operator geometric series + unnormalized partial trace -> exact long pair/cubic expressions.

Steps 1–4 and 6–7 are reconstructed below. Step 5 uses the external characterization as a named input, not an independently re-proved 147-page theorem. The complete upstream semiclassical proof chain of FM-007 is not newly certified here: its explicit trace-bound statement and the noncircular scaling argument in its displayed (9)–(12) were inspected. The claim is source-bound to that input.

## 2. External source authentication and exact contract

Source: Paul Bourgade and Jiaoyang Huang, *Loop Equations Characterize Random Matrix Statistics*, arXiv:2607.07617v2, 9 September 2026. Official primary record independently opened on 6 October 2026:
https://arxiv.org/abs/2607.07617v2

The record identifies v2 and the 147-page paper. The pinned local PDF has SHA-256 `9ae676c7e1161d100244080dae040c5bbce8b0ddb829c9ab1326ec8c3e3ec223`. Fresh `pdftotext -layout` extraction agrees byte-for-byte with the supplied text, SHA-256 `863e51d873390d060256600a7c04c529f42d03bf611649aa719fd36cadf42b1b`. A PDF font warning did not prevent extraction; equality of text was explicitly checked.

Inspected source locators: intensity convention in the introduction (printed p.4); Definitions 1.1–1.3 and Assumption 1.4 (pp.5–6); Theorem 1.9 (p.6); estimates (2.1)–(2.4) and Lemma 2.1 (pp.11–12); proof of Theorem 1.9, (2.14)–(2.24) (pp.13–15).

The exact theorem contract has rational beta>0, random particle-generated Nevanlinna functions, events Omega_N of probability 1-o(1), every finite moment on these events, and for each fixed p and off-real compact K, an error uniformly o(1) relative to 1+E[1_Omega max_j|s_N(w_j)|^(p+1)]. It concludes vague convergence in distribution. There is no additional assumed local law, moment rate, or preliminary tightness. At beta=2 the derivative coefficient is zero and the divided-difference coefficient is one. Taking Omega_N to be the whole origin space is legitimate and supplies the uniform integrability needed for the stronger project correlation conclusion.

The source's claim of positive complex residues conflicts with its own representation 1/(x-w): that residue is negative. The project explicitly uses positive integer atom masses and negative residues, so this source wording defect does not invalidate the application.

## 3. Reconstructed anchor bootstrap, with quantifiers

Let N run through the intended sequence (odd N for the actual map). For each N let alpha be uniform on the circle, let

s_N(w)=N^(-1) sum_j cot((theta_j-alpha)/2-w/N),

and let E_{p,N} be exactly equation (3) of the project's loop_bridge.md. All expectations in this review use the entire alpha space. Fix one countable dense D subset of C\R, independently of N.

(A) means: for every integer r>=2, at the one fixed tuple consisting of w_1=i, r-2 additional i's, and r copies of -i, there exists epsilon_{r,N}->0 such that

|E_{2r-1,N}| <= epsilon_{r,N}(1+E|s_N(i)|^(2r)).

No uniformity in r is assumed or obtained. (B) means: for every integer p>=1 and every fixed tuple in D^p that has both signs, its relative residual tends to zero. No simultaneous or uniform convergence over D^p is assumed.

Set Z=s_N(i), M_t=E|Z|^t. For a Nevanlinna representation with measure mu and c>=0,

|s'(z)| <= Im s(z)/Im z <= |s(z)|/Im z,  Im z>0.

The differentiated divided difference is

T(z,w)=partial_w[(s(z)-s(w))/(z-w)]
      =integral [(x-z)^(-1)(x-w)^(-2)] dmu(x).

The linear coefficient c disappears. At z=i and w either i or -i, |T(i,w)|<=integral (1+x^2)^(-1)dmu(x)<=Im Z<=|Z|. The formula includes the diagonal value s''(i)/2. Reflection gives s(-i)=conjugate Z.

For the anchor tuple, the quadratic leading product is exactly Z^r conjugate(Z)^r=|Z|^(2r). The +1 term has absolute value |Z|^(2r-2). Each of the 2r-2 derivative terms has one factor bounded by |Z| and 2r-3 remaining resolvent factors. Hence, with no cancellation assumption,

M_(2r) <= |E_{2r-1,N}|+(2r-1)M_(2r-2).

Consequently (1-epsilon_{r,N})M_(2r) <= (2r-1)M_(2r-2)+epsilon_{r,N}. Young's inequality t^(2r-2)<=delta t^(2r)+C_{r,delta}, with delta chosen after r and before N, absorbs the lower moment. This directly gives sup_N M_(2r)<infinity, after including the finitely many early N whose moments are finite. No prior bound on M_(2r-2) is needed; there is no circular induction. Every positive finite moment follows by choosing 2r at least that exponent. The base r=2 is valid: it is the tuple (i,-i,-i) and yields a fourth-moment bound.

## 4. Compact comparison and dense-test/Montel step

For an upper-half-plane compact K, let eta=min(1,inf_K Im z)>0 and R=sup_K|z-i|. Along gamma_z(t)=i+t(z-i), the derivative inequality and Gronwall imply the deterministic bound

sup_(z in K)|s_N(z)| <= exp(R/eta)|s_N(i)|.

All segments remain in the upper half-plane. Reflection handles the lower half-plane, so the same assertion with a K-dependent constant holds for any compact K subset C\R. It follows that for every fixed t>0,

sup_N E sup_(z in K)|s_N(z)|^t < infinity.

These constants may depend on K and t; neither K approaching the real line nor growing order is covered.

Now fix p. The denominator in (B) is bounded at each fixed tuple (indeed uniformly on compact sets), so (B) implies ordinary residual convergence to zero on the mixed dense tuples. For finite N the expected residual is jointly holomorphic on each product sign component of (C\R)^p. Differentiation under expectation is justified locally by finite-N boundedness in alpha. Same-sign coincidences are removable analytic diagonals; opposite signs never coincide.

The residuals are uniformly locally bounded in N: bound products by compact suprema, and derivatives/divided differences by Cauchy estimates on a slightly enlarged compact subset of the same half-planes. For opposite-sign arguments the separation is bounded below. The resulting integrands are controlled by constants times compact-supremum powers of degrees p+1 and p-1. The moment estimates just established apply.

Montel's theorem in several complex variables now gives, on each of the finitely many sign components, locally uniformly convergent subsubsequences of any subsequence. In a mixed component, the limit vanishes at every point of D^p in that component, hence everywhere by continuity and density. No several-variable identity theorem for a thin set is being assumed: the test set is genuinely dense in the whole component. Every subsequential limit is therefore zero, implying locally uniform convergence of the full residual sequence.

On all-upper/all-lower components the residual is identically zero already at finite N. In the upper half-plane the Fourier expansion has constant i and strictly positive nonconstant alpha frequencies; s_N^2+1 and every differentiated divided difference have no constant term. Products cannot return to frequency zero. The lower argument is the reflected one. This includes p=1.

For any fixed K subset C\R, K^p meets finitely many components in compact sets, giving sup_(K^p)|E_{p,N}|->0. Since the relative denominator is >=1, (H) follows. This proves the claimed quantifier reduction. It does not supply (A) or (B) for the actual map, nor any convergence rate.

## 5. Exact normalization and correlation transfer

Each cotangent term has local expansion 1/(x-w), with atom x=N(theta_j-alpha)/2+pi N ell. Thus masses are one, merged masses are positive integers, and the complex residues are -1 per label. The representing measure has N atoms per period pi N, so the random shift has stationary intensity 1/pi. At fixed N, cotangent tends to i as Im w->infinity and the Herglotz linear coefficient vanishes. Finite-N off-real compact moments exist even for repeated eigenangles.

Dividing positions by pi gives unit intensity. In those coordinates y_j=N theta_j/(2pi), t=N alpha/(2pi) is uniform over a period of length N. Integrating an anchored test h(u_k) phi(u_1-u_k,...), with integral h=1, and summing anchor-period lifts gives exactly the prefactor 1/N. For large N fixed compact support excludes different period lifts of one label within a tested tuple. Distinct eigenvalue labels at the same position remain correctly counted by factorial measures.

The local-count inequality mu_N([-B,B]) <= (1+B^2) Im s_N(i) gives every uniform count moment. Continuous compactly tested factorial functionals are continuous under vague convergence of integer-valued Radon measures, including multiplicities; one may see this by the finite partition/inclusion-exclusion formula in products of measures and diagonal identifications. Their magnitudes are bounded by fixed powers of local counts, hence are uniformly integrable. Thus the source's weak conclusion upgrades to the asserted compactly tested factorial convergence on the whole origin space. It gives neither pointwise densities nor a fixed deterministic-origin assertion.

## 6. Short-cubic-leg excision without local-moment circularity

Fix 0<s_0<=s<=s_1<infinity, q=exp(-2s/N), K=floor(c log N), with c within FM-007's permissible constant. Put p_m=Tr U_N^m and

L=N^(-2) sum_(m>=1) q^m |p_m|^2,
C=N^(-3) sum_(a,b>=1) q^(a+b) p_(-a)p_(-b)p_(a+b),
B=N^(-1) sum_(a=1)^K q^(a/2)|p_a|.

For any unitary, p_(-m)=conjugate p_m and all these series converge absolutely for q<1. Set x_b=q^(b/2)p_b. Then for each a>=1,

sum_(b>=1) q^(a+b)|p_b p_(a+b)|
=q^(a/2) sum_(b>=1)|x_b x_(a+b)|
<=q^(a/2)(sum_(b>=1)|x_b|^2)^(1/2)(sum_(b>=1)|x_(a+b)|^2)^(1/2)
<=q^(a/2) N^2 L.

Triangle inequality over the union {a<=K or b<=K} yields |C-C_long|<=2BL. Counting the overlap twice in this upper bound is harmless; it is not an erroneous algebraic decomposition. Also 0<=L-L_long<=N^(-2) sum_(m=1)^K |p_m|^2.

FM-007 supplies |p_m|<=C N^(39/40) uniformly for all 1<=m<=K and all sufficiently large odd N, not merely fixed m. Therefore B<=C K N^(-1/40) and L-L_long<=C^2 K N^(-1/20). Its proof's choice delta=N^(-1/20) in (12) produces powers N^(-1/20), N^(-1/10), N^(-1/2) before the e^(Cm) loss; sufficiently small logarithmic c makes the final N^(-1/40) estimate valid. This step uses the logarithmic Egorov input, not a local spectral law.

With Z_s=s_N(is/2), the upper Fourier series is i+(2i/N) sum_(m>=1) p_(-m)e^(im alpha)e^(-ms/N). Parseval gives exactly E|Z_s|^2=1+4L. Reflection makes the two-argument maximum exactly |Z_s|. Thus D=1+E|Z_s|^3 and Lyapunov gives

D>=1+(1+4L)^(3/2).

As L>=0, L/[1+(1+4L)^(3/2)] is globally bounded. Consequently

| (L+C)-(L_long+C_long) |/D
<= C^2 K N^(-1/20)+2C K N^(-1/40) L/[1+(1+4L)^(3/2)]
=O(N^(-1/40) log N).

Nothing here bounds or assumes bounded L. All constants are uniform in the fixed positive compact height interval, and even the displayed deletion inequality only uses 0<q<1. The denominator remains the ORIGINAL full resolvent denominator. Replacing it with a truncated object would require another argument and is not claimed.

Direct Fourier multiplication gives E[(Z_s^2+1)conjugate Z_s]=8i(L+C). The expected differentiated quotient is -2i/s^2, since E s_N(w)=i above and -i below. Thus the exact residual is 8i[L+C-1/(4s^2)], confirming the normalization, sign, factor eight, and retained possible imaginary part of C.

## 7. Tensor-resolvent algebra for every unitary

All traces below are ordinary unnormalized traces. Let X=U tensor conjugate(U). Since U is unitary, ||X||=1 and q<1, the norm-convergent operator identity is

(qX)^(K+1)(I-qX)^(-1)=sum_(a>K)q^a(U^a tensor conjugate(U^a)).

The finite-dimensional partial trace is continuous and satisfies Tr_2(A tensor B)=A Tr B. Hence

F_K=Tr_2[(qX)^(K+1)(I-qX)^(-1)]
   =sum_(a>K)q^a p_(-a)U^a.

Tracing once gives Tr F_K=sum_(a>K)q^a|p_a|^2=N^2 L_long. Multiplying the two norm-convergent sums and using U^a U^b=U^(a+b) gives

Tr(F_K^2)=sum_(a,b>K)q^(a+b)p_(-a)p_(-b)p_(a+b)=N^3 C_long.

This is an algebraic square, not an adjoint square, and there is no missing factor N in the partial trace. It holds for arbitrary multiplicities and every N, not just a diagonal three-point example. It also explains why the cubic trace may be complex even though Tr F_K is nonnegative real.

For real t=tau N and U=exp(it A)M, complex conjugation gives conjugate U=exp(-it conjugate A)conjugate M. The tensor-factor generators commute, so exactly

X=exp(it[A tensor I-I tensor conjugate A])(M tensor conjugate M).

The order of the kick and metaplectic factor is retained. No commutation between those two factors, nor replacement of iterated ordered products by one transported-generator exponential, follows.

## 8. Obligation matrix and remaining implication

| Obligation | Result |
|---|---|
| All pinned inputs and report identity | Passed; hashes retained |
| Exact external theorem contract and beta=2 dictionary | Passed as named external input |
| Entire external uniqueness proof | Out of scope |
| Single-anchor positive coercive moment inequality | Passed |
| Compact-supremum propagation and dense-test normal families | Passed |
| Whole-space uniform integrability and 1/N anchoring | Passed |
| FM-007 growing logarithmic trace statement and exponent use | Passed as source-bound input |
| Full inherited FM-007 semiclassical proof chain | Not independently recertified |
| Short-leg relative error without bounded L | Passed |
| Universal tensor-resolvent identities and signs | Passed |
| Actual-map vanishing of any requisite mixed anchor/dense hierarchy | Open |
| Rounded-spectrum and exact-hopping obstruction reports | Not independently audited here |
| Numerical or formal certification of asymptotic limits | Not claimed |

No mathematical correction to report sections 2–5 is needed. For integration, retain the full-space, fixed-order, fixed-compact, original-denominator and unnormalized-partial-trace qualifications, and label the two new deductions separately from their unproved actual hypotheses. The general independence/nonclosure assertions about other route reports should not be promoted on the basis of this scoped audit alone.

The first explicit unresolved implication in this route is a model-specific signed bound proving, for each fixed s>0 (uniformly on compact s intervals if that variant is intended),

[ N^(-2)Tr F_K + N^(-3)Tr(F_K^2) - 1/(4s^2) ] / [1+E|s_N(is/2)|^3] -> 0.

This is a necessary first mixed leaf of the proposed sufficient hierarchy, not itself a sufficient BGS theorem. The r=2 anchor is a separate useful first target: it would give fourth moments and hence bounded first-mixed denominators, but is unproved. To finish this route one still needs every fixed anchor order and every fixed dense mixed tuple, or another input strong enough to imply (H). FM-007, path controls, source metadata and the exact resolvent representation do not supply that signed Heisenberg-scale estimate.

## 9. Executed checks and safe continuation

Executed: independent manifest hash verification; git HEAD/status inspection; official versioned arXiv metadata lookup; fresh PDF text extraction and byte comparison; direct analytic reconstruction of the inequalities and all-N operator algebra. The author's SymPy script was inspected but not rerun, because it writes outside the authorized review directory. Its finite sample is not used as evidence for the universal identities or asymptotic deletion bound.

Strongest safe conclusion: the proposed testing reduction and normalized short-leg deletion are valid and worth retaining as exact conditional tools. Deterministic BGS remains open. The cheapest scientifically meaningful next check is to formulate and attack a signed bound on the actual F_K expression or the r=2 anchor with exact quantization retained; no finite algebra rerun establishes either limit.
