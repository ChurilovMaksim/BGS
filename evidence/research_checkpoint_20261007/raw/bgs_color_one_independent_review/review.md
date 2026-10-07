# Independent audit: one-color type-A CFT and its surface functional

Date: 7 October 2026. Canonical base observed: `d37c92e563d10d25bb1d6ab85bedffc1f160f773`; the existing working-tree overlays were left untouched. This is a fresh calculation from the raw supermatrices and pinned primary sources, not a reuse of the earlier worker's executable or acceptance decision. The source packet supplied the proposed discriminator, so this is not described as a blinded review.

## 1. Normalized claim and primary verdict

Let ζ be uniform on U(1), and let a,b,c,d be complex with |a|,|b|<1. Write

\[
\mathcal F(a,b,c,d)=\mathbb E\frac{(1-c\zeta)(1-d\zeta^{-1})}{(1-a\zeta)(1-b\zeta^{-1})}.
\]

Set

\[
Z=\begin{pmatrix}z&\alpha\\\beta&w\end{pmatrix},\quad
\widetilde Z=\begin{pmatrix}\bar z&\gamma\\\delta&-\bar w\end{pmatrix},\quad
A=\operatorname{diag}(a,c),\quad B=\operatorname{diag}(b,d),
\]

where α,β,γ,δ are independent odd variables. The proposed ordinary coordinate integral is

\[
I_{\rm bulk}[f]=\pi^{-2}\int_{|z|<1}\!d^2z\int_\mathbb C\!d^2w\,
\partial_\alpha\partial_\delta\partial_\gamma\partial_\beta
\{\operatorname{SDet}(1-\widetilde ZZ)f\},\qquad
f=\operatorname{SDet}^{-1}(1-\widetilde ZAZB).
\]

**Primary verdict: refuted, with the smallest valid counterexample.** The claim \(\mathcal F=I_{\rm bulk}[f]\), when the right side means this ordinary disk/plane coordinate integral without a boundary prescription, fails even at a=b=c=d=0: 1≠0. For c=d=0 and every |a|,|b|<1 it gives 0 instead of 1/(1−ab). These integrals converge absolutely after odd extraction, so this particular counterexample does not rely on assigning a value to a divergent integral.

The precise replacement verified below is

\[
\mathcal F=\lim_{T\to\infty}(I_{{\rm bulk},T}+I_{{\rm surf},T})[f],
\]

with the same cutoff |w|²≤T and Zirnbauer's operator (4.29). For cd≠0 the two summands generally do not exist separately. This is a failure of a specified integral identity, not of the exact phase average, graph universality, or the deterministic BGS conjecture.

## 2. Parameters, domains and conventions

- `N_color` is the dimension of the group being Haar averaged. One independent phase is U(1), so N_color=1.
- `M` is the physical site/coordinate count. Independent coordinate phases form U(1)^M and require M separate color-one transformations. Increasing M does not increase the color number of any factor.
- Here m₀=n₀=m₁=n₁=1: one retarded and one advanced bosonic flavor and the corresponding fermionic flavors. The matrices Z are 1|1, not M-color matrices.
- Zirnbauer 2021 §2.4, printed pp.12–13, (2.55)–(2.58), states the standard square-flavor stable range N_color≥2n₀. The present point 1<2 is outside it. The inequality alone is not the counterexample; §3 below supplies one directly.
- The even body is the Poincaré disk in z times the sphere in the stereographic coordinate w. The ordinary chart covers |z|<1 and w∈C. The sphere's w=∞ chart boundary and the noncompact disk edge must not be confused with independent extra colors.
- In a body-coordinate/retraction interpretation, the disk inequality does not itself encode nilpotent boundary corrections. A locally flat Berezinian and a body domain do not determine a global noncompact superintegral on these non-compactly-supported test functions. Under changes of coordinates, nilpotent shifts of the boundary can contribute a differential surface functional.
- The source ordering is (4.8). With left odd derivatives its top monomial is G=γβαδ and ∂G=1. The verifier checks this explicitly rather than inferring a sign from a positive-measure analogy.
- All source parameters are fixed during a cutoff limit. The formulas extend polynomially in c,d, including any apparent zero of the FF Schur block: using the BB-pivot expression for the inverse Berezinian introduces only powers of 1−ab|z|² in denominators. This is the regular determinant-ratio continuation, not a new singularity in the numerator sources.

The 1998 chaotic-map construction is different again: it averages one common phase, and explicitly switches to one color and M physical flavors (printed p.4 preceding (1)). Its growing physical dimension likewise does not put its standard CFT in the many-color stable range.

## 3. Exact phase average and the decisive bulk test

The uniformly absolutely convergent Fourier series give

\[
\frac{1-c\zeta}{1-a\zeta}=1+(a-c)\sum_{n\ge1}a^{n-1}\zeta^n,
\quad
\mathcal F=1+\frac{(a-c)(b-d)}{1-ab}
=\frac{1+cd-ad-bc}{1-ab}.
\]

Put x=|z|² and y=|w|². Direct 1|1 Berezinian algebra gives

\[
S:=\operatorname{SDet}(1-\widetilde ZZ)
=\frac{1-x}{1+y}-\frac{Q}{(1+y)^2}+G\frac{1-y}{(1+y)^3},
\]

\[
Q=\gamma\beta+\alpha\delta+\gamma w\delta z+\alpha(-\bar w)\beta\bar z,
\quad Q^2=2(1+xy)G.
\]

This agrees with source (4.16), but was also derived independently from the matrix Schur formula. At c=d=0, AZB has only its BB entry ab z, the product with tilde Z is lower triangular, and f=(1−abx)⁻¹ has no odd part. Hence

\[
I_{\rm bulk}[f]
=\int_0^1\frac{dx}{1-abx}\int_0^\infty\frac{1-y}{(1+y)^3}\,dy=0,
\]

because \(\int_0^T(1-y)(1+y)^{-3}dy=T/(1+T)^2\to0\). A finite nonzero normalization constant cannot convert this zero into one. Changing the odd orientation only changes an overall sign and also cannot repair it.

This also rules out dismissing the problem as a source-independent additive normalization: for c=d=0 the missing answer is the whole function 1/(1−ab), including its source derivatives.

## 4. Independent surface evaluation

In the notation above, source (4.29) is exactly

\[
\Omega=-\frac{Q}{2(1+y)}+
G\left[\frac1{2(1+y)^2}+\frac1{4(1+y)}\partial_{|z|}\right].
\]

The derivative acts before |z|=1 is imposed. The surface integral is (4.28), with z=e^{iθ}, tilde z=e^{-iθ} and normalized prefactor π⁻².

Only the degree-2 part of Ω times the degree-2 part of Sf, and the degree-4 part of Ω times the degree-0 part of Sf, contribute. The factor S₀=(1−x)/(1+y) vanishes at x=1. Thus terms involving the odd part of f disappear on this surface, and the derivative of f₀ is killed by S₀=0. However the derivative of S₀ is −2/(1+y) and must be retained.

Writing p=ab and q=cd, f₀=(1+qy)/(1−px). The Ω₂S₂ term contributes f₀/(1+y)² before angular reduction; the normal-derivative term contributes −f₀/[2(1+y)²]. The angular reduction π⁻²(2π)(πdy) contributes a factor of 2. Therefore

\[
I_{{\rm surf},T}[f]=\int_0^T\frac{1+qy}{(1-p)(1+y)^2}\,dy.
\]

For c=d=0 this tends to 1/(1−p), exactly the missing phase answer. At f=1 the two source contributions are 2 and −1, giving I_surf[1]=1. Restricting to the boundary before differentiating would incorrectly lose the −1 and produce 2; it is not an equivalent convention.

## 5. General sources and the common-cutoff requirement

Also set r=ad+bc and

\[
L(p)=\int_0^1\frac{dx}{1-px}=-\frac{\log(1-p)}p,\quad L(0)=1.
\]

The branch is the analytic one on |p|<1. A fresh exterior-algebra calculation yields the bulk density

\[
\begin{split}
\mathcal B(x,y)={}&\frac{(1-y)(1+qy)}{(1+y)^3(1-px)}
-\frac{r+2pqxy}{(1+y)^2(1-px)^2}\\
&+\frac{pq(1-x)(1+px)}{(1+y)(1-px)^3}.
\end{split}
\]

Integrating x first, at finite T so that no infinity is separated, gives

\[
\overline{\mathcal B}(y)=L(p)(1-q)\frac{1-y}{(1+y)^3}
+\frac{q(1-y)-r}{(1-p)(1+y)^2}.
\]

The exact finite-cutoff answers are

\[
\begin{split}
I_{{\rm bulk},T}[f]
&=L(p)(1-q)\frac{T}{(1+T)^2}
+\frac{(2q-r)T/(1+T)-q\log(1+T)}{1-p},\\
I_{{\rm surf},T}[f]
&=\frac{(1-q)T/(1+T)+q\log(1+T)}{1-p},\\
(I_{{\rm bulk},T}+I_{{\rm surf},T})[f]
&=L(p)(1-q)\frac{T}{(1+T)^2}
+\frac{1+q-r}{1-p}\frac{T}{1+T}.
\end{split}
\]

The limit is precisely the phase result from §3. In particular:

- For q=0 both terms converge individually, but the surface is still essential. If only one of c,d is zero, the bulk limit is −r/(1−p) and the surface limit is 1/(1−p).
- For q≠0 the bulk has leading divergence −q log T/(1−p), and the surface has the opposite divergence. For complex sources these are complex logarithmic divergences, not an assertion that each is ordered ±∞.
- Independent cutoffs T_b,T_s with T_s/T_b→λ>0 shift the answer by q log λ/(1−p). Thus an uncoordinated pair of finite parts is not enough. A common cutoff, or an explicitly equivalent calibrated prescription, is required.
- Even at the supersymmetric source choice a=c,b=d, where the phase ratio is identically 1, the two pieces separately diverge for ab≠0. Their coordinated sum is 1.
- For c=d=0 and p=e^{−s/M}, real s>0, the surface answer is asymptotic to M/s. No smallness in physical site count follows from the fact that a surface is being integrated. Normalized graph observables may have further cancellations, but they need their own proof.

No step here removes a cutoff uniformly in growing M or differentiates an unregulated divergent summand separately.

## 6. Audit of the corrected reproducing-kernel argument

Table 1 in Zirnbauer 2021 p.32 contains four families of color-neutral sections. Their diagonal products in the present notation are

\[
\begin{array}{ll}
F_1=x^k,&k\ge0,\\
F_2=-k\alpha\delta x^{k-1},&k\ge1,\\
F_3=k\beta\gamma x^{k-1},&k\ge1,\\
F_4=-(zw-l\alpha\beta)(\widetilde w\widetilde z-l\gamma\delta)x^{l-1},&l\ge0.
\end{array}
\]

At l=0, F₄ is read by cancellation as −w tilde w=y. All four were rechecked from the matrix-derived S and the surface operator:

- F₁ has bulk 0 and surface 1.
- F₂ and F₃ have bulk density kx^{k−1}/(1+y)² and zero surface, giving 1.
- After x integration, F₄ has bulk density [l+y−(l+1)y²]/[(l+1)(1+y)³] and surface density y/(1+y)². Their sum is [l+(l+2)y]/[(l+1)(1+y)³], whose integral is 1 for every l≥0.

Distinct sections have distinct U(1)^4 weights under the diagonal K_L×K_R action. The circular cutoffs preserve those weights, so off-diagonal pairings vanish already before their limit. This independently checks the orthogonality step used in (4.39)–(4.54) and the finite-span projector identity. It also corroborates the determinant-ratio calculation. No claim is made here about extending the functional to every arbitrary smooth superfunction without decay hypotheses.

**Verified source typo:** Table 1 pairs Z^{01} with tilde Z_{10}, as above. In the pinned v1 PDF, (4.43), (4.44) and (4.45) instead print tilde Z_{01}. The literal printed product −kαγx^{k−1} has zero integral, not one. The required correction to those displayed indices is forced by Table 1; with the table's dual section, the calculation is correct. This was visually checked in `page32.png` and `page33.png`. It is not a reason to reject Ω or the corrected identity, both independently verified here. The review does not silently assert that every printed line in the source is correct.

## 7. Does the graph literature already specify the repair?

### Weidenmüller, arXiv:1812.00655v1

Printed p.3 explicitly averages phases φ_bd separately and independently. Its Z_bd is one 1|1 matrix per directed bond. Equations (7)–(9), p.4, give the same BB disk/FF plane body, source terms and a stated flat superintegral. The following sentence calls the representation exact. This local color-one step is the directly relevant comparison.

The paper does recognize that the coordinates are not globally defined: §3.1 after (16) and §3.2 following (22), printed pp.5–6, discuss coordinate charts and linearizing fluctuations. **That recognition is real and must not be omitted from the source assessment.** It does not specify a color-one surface functional, nilpotent boundary prescription, or a regulator that implements the cancellation above for the original source integral. No such explicit completion was found in a full-text search followed by reading the indicated passages.

Reference [8] is Zirnbauer 1996. That reference contains a global-anomaly caveat, so an intended globally invariant meaning of “flat measure” is plausible. Under such a meaning the integral symbol need not equal our ordinary bulk integral; the counterexample cannot be used to refute an unspecified, already boundary-completed global integration convention. Conversely, the caveat does not justify evaluating the displayed expression as the ordinary flat bulk, nor establish asymptotic control of the missing completion. **Safe source conclusion: the literal bulk interpretation fails; a repaired global reading requires an explicit prescription and its compatibility with subsequent changes of variables and estimates.**

The same 2018 paper, pp.14–15, itself calls the massive-mode estimates heuristic/rough and conditions its conclusion on their validity. It should not be described, on the strength of this source, as a complete rigorous all-orders universality proof.

### Other checked primary sources

- Gnutzmann–Altland, arXiv:nlin/0508009v1, p.6 (41)–(42): explicitly one color and F flavors; actual application has F=4 from direction/time reversal. Appendix C, pp.12–14, invokes a normalized invariant projector. No explicit low-color surface correction was found. The present explicit one-flavor Ω must not simply be reused for F=4 without a new theorem.
- Pluhař–Weidenmüller, arXiv:1407.1148v2, p.10 (31)–(35): independent bond phases, direction/replica flavor indices, SDet power one and flat Berezinian, followed by exactness wording. No explicit completion was found at this step. The sentence after (33) restricts the FF rather than the intended BB block. This review records that mismatch instead of silently treating it as the domain used in the one-flavor proof.
- Zirnbauer 1996, J. Phys. A 29, printed p.7116, (3) and its footnote: flatness is only local, and a global anomaly is explicitly acknowledged. Printed p.7122 (discussion after the polar measure (13)) discusses other boundary contributions in a particular circular-ensemble calculation and says they do not contribute to its R_n. That is not a demonstrated cancellation of the color-one graph boundary functional considered here. The source's observable, coordinates and hypotheses must be translated before importing such a cancellation.
- Zirnbauer, arXiv:chao-dyn/9810016v1, printed pp.4–5, (1): one common phase/one color with physical-M flavors, and the measure explicitly includes “+ ...” for global anomalies. Thus this source is **not** a source for a bulk-only identity. A citation to its exact invariant formula is compatible with a completed measure, while dropping its dots is not justified.

Search boundary: these six pinned primary sources and the packet's canonical dependency scan; not every cited graph paper, later revision, erratum or global superintegration theorem. No claim is made that a correct prescription is unknown in the broader literature.

## 8. Dependency graph, obligations and canonical impact

The tested dependency chain is:

1. ordinary U(1) Fourier average → exact ratio formula: **passed**, internal elementary proof;
2. local supermatrix definition → (4.16) and the bulk density: **passed**, direct exterior algebra;
3. flat bulk → U(1) identity at color one: **failed**, convergent 1-versus-0 test;
4. Ω plus coordinated cutoff → ratio identity: **passed**, exact formulas above;
5. corrected coherent-state pairings → finite-span projector: **passed**, four norm families and weights; the source's displayed-index typo is corrected explicitly;
6. graph's notation → a particular completed global integral: **conditional**, no explicit operative prescription verified in the graph text;
7. completed finite-M graph integral → uniform microscopic/large-M estimates: **not addressed/open**;
8. integral identity → ordinary scalar/block matrix coercivity: **no dependency arrow**.

The authority hierarchy in BGS/AGENTS.md and SOURCE_OF_TRUTH.md was respected. The path-by-path packet `canonical_impact.md` was checked against the following raw files rather than accepted solely as a status summary:

- `mathematics/frozen_operator_transfer_coercivity.md` §8, O21–O23: finite matrix/commutator identities, Gaussian characteristic functions, and singular-value bounds. None uses the disputed integral equality. §10 O25 compares explicitly defined ordinary determinant functions and also survives.
- Its lines 413–419 and `literature/frozen_operator_transfer_sources_20261006.md` discuss a quadratic block in the 1998 formalism and already leave the full nonlinear action/zero-mode step open. Exposition should retain the 1998 global-anomaly convention and avoid presenting it as flat-bulk exactness.
- `record/claims.json` lists FM-018's external input as EXT-PP-1990, not CFT; FM-019/FM-020 inherit elementary channel results. This finding supplies no reason to downgrade their mathematical status.
- `literature/frontier_2026.md` (the rigorous graph model-class paragraph) and `literature/bibliography.md` items 10–11 contain stronger rigorous-proof wording than this audit can support. A future correction should qualify the source bridge, rather than claim graph universality false. Historical wording should be superseded by an appended correction, not overwritten as if the caveat had always been known.
- `literature/all_order_sources_20261005.md`, “Quantum-graph route: no imported arrow,” already declines to import the graph theorem into the deterministic project; no theorem-status repair is needed there.
- Scalar and block coercivity of a separately defined determinant action are standalone finite-dimensional matrix inequalities. They do not acquire a false premise merely because a route from that action to a source-averaged superintegral needs additional terms.

The full canonical corpus was not re-audited. The sealed dependency conclusion is bounded to these inspected arrows and the supplied path scan. BGS and TRACE-005 were already open and remain so.

## 9. Sources and reproduction

Primary version locators:

1. Martin R. Zirnbauer, *Color-Flavor Transformation Revisited*, arXiv:2109.10272v1, 21 September 2021. https://arxiv.org/pdf/2109.10272v1 . §§2.4,4.1–4.4, printed pp.12–13 and 26–34. Critical (4.21), (4.28)–(4.31) and Table 1 were checked; p.30,32,33 formulas were visually inspected.
2. H. A. Weidenmüller, *Massive Modes for Quantum Graphs*, arXiv:1812.00655v1, arXiv stamp 3 December 2018 (title date 4 December). https://arxiv.org/pdf/1812.00655v1 . §2 (3)–(9), §3.1–3.2, §5.
3. Gnutzmann–Altland, arXiv:nlin/0508009v1. https://arxiv.org/pdf/nlin/0508009v1 . (41)–(42), Appendix C.
4. Pluhař–Weidenmüller, arXiv:1407.1148v2. https://arxiv.org/pdf/1407.1148v2 . (30)–(35).
5. Zirnbauer 1996, *Supersymmetry for systems with unitary disorder: circular ensembles*, J. Phys. A 29, 7113–7136. Author-hosted primary PDF URL and hash in `source_hash_verification.json`.
6. Zirnbauer 1998, *The Color-Flavor Transformation and a New Approach to Quantum Chaotic Maps*, arXiv:chao-dyn/9810016v1. https://arxiv.org/pdf/chao-dyn/9810016v1 . (1), printed pp.4–5.

The local PDF hashes were independently recomputed and matched the frozen source manifest; version/title stamps were checked for the two central sources. This pass reused the authorized local primary PDFs, not a new network download. Their neighboring extracted texts were used for searching and read together with the formula images where exact typography mattered.

Run:

```sh
python /workspace/shared/bgs_color_one_independent_review/verify_independent.py
```

It reconstructs both Berezinians via distinct block-pivot formulas, verifies the odd derivative orientation, radial primitives, cutoff identities and all four norm families symbolically. Its separate finite Fourier-coefficient check covers total bosonic degree 0 through 9. Five 45-digit numerical phase-quadrature examples include p=0, c=d=0, supersymmetric sources and complex sources; these are diagnostics, not the proof of the unrestricted formulas.

## 10. Strongest safe statement and next gate

The one-color, one-retarded/advanced-boson-plus-fermion phase identity has a verified boundary-completed realization on the stated determinant-ratio family. The ordinary flat bulk is not that realization. For cd≠0 the bulk/surface decomposition has to be regulated together.

The cheapest next source-to-project gate is to specify the intended completed functional for the actual graph or common-phase flavor count, prove its equality to the original generating function, and retain all boundary terms through source differentiation and the relevant coordinate change. Only then can a uniform microscopic remainder estimate be formulated. Rechecking scalar/block coercivity cannot by itself close that gate. No canonical edits, status changes, commit, push or publication are part of this review.
