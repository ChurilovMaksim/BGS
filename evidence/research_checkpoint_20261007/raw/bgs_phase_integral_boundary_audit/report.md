# Exact one-color phase-integral boundary audit

7 October 2026. Canonical base observed at d37c92e563d10d25bb1d6ab85bedffc1f160f773, with pre-existing integration overlays. All artifacts here are outside canonical BGS; no canonical edits or publication. This is an exact-source audit plus direct algebra, not a BGS counterexample.

## Verdict and immediate consequence

**Refuted, with the smallest valid counterexample:** the literal flat-measure, bulk-only type-A color-flavor transformation (CFT) at one color and one retarded/advanced boson–fermion flavor does not reproduce the one-site determinant ratio. This is exactly the color count of each independent coordinate phase.

For |a|,|b|<1 and arbitrary c,d,

R(a,b;c,d) = E[(1-cζ)(1-dζ^-1)/((1-aζ)(1-bζ^-1))]
           = 1+(a-c)(b-d)/(1-ab).

The uncorrected superintegral gives zero when c=d=0, whereas R=1/(1-ab). The discrepancy persists strictly inside the source domain, already at all four sources zero. For generic cd≠0, the uncorrected integral is not even a convergent improper integral.

A correct pair replacement is known and explicit: Zirnbauer's 2021 bulk-plus-boundary functional. Our independent exterior-algebra calculation verifies that it yields R for every source in the stated domain, provided bulk and boundary use a common cutoff. The graph formulations examined do not supply this completion or its microscopic source estimates. Thus the first missing bridge is a valid finite-size integral with its boundary prescription, before any use of global bosonic coercivity in that integral.

For fixed higher flavors, the standard theorem's stable-range hypothesis excludes color one. The pair correction does not constitute a general higher-flavor formula. The checked sources do not supply the required replacement and source bounds there. This is an identified missing implication, not a claim that no such formula can exist.

## 1. Claim, notation and dependency closure

Let M be the physical matrix dimension, V_θ=D_θ U_M with M independent phases, and k be a fixed number of retarded and advanced denominator factors. Each factor of the disorder group U(1)^M is separately integrated. Its CFT color number is N_c=1. In a balanced supersymmetric k-ratio representation, each such site has k bosonic and k fermionic flavors in each direction. Neither M→∞ nor keeping k fixed raises N_c.

The original 1998 chaotic-map paper uses a different arrangement: one common U(1) phase, one color, and physical-M flavors. It says this explicitly on printed p.4. Its color number also remains one. The familiar CUE calculation with Haar U(M), by contrast, has M colors and fixed flavors. These are different disorder groups.

Dependency chain required by the proposed annealed route:

1. Exact determinant-ratio phase average and holomorphic regulator domain.
2. Exact CFT or substitute, including its complete global integration functional.
3. Exact collective-coordinate/gauge change with its Berezinian and images of boundary strata.
4. Estimates on the differentiated, Grassmann-integrated observable at microscopic sources.
5. Uniform signed massive-mode reduction, including all orders and noncompact regions.
6. Zero-mode identification and the target annealed law.

The scalar coercivity theorem is a useful input inside steps 3–5, not a replacement for step 2. This audit proves failure of the bulk-only version of step 2, checks a repaired pair formula in the smallest source-complete example, and supplies a correct general finite-size fallback.

## 2. Exact primary-source contracts

All equation numbers below refer to the pinned PDFs. The arXiv HTML conversion renumbers equations and must not be mixed with these locators. Source bytes and hashes are in sources.json.

- **Zirnbauer 2021**, *Color-Flavor Transformation Revisited*, arXiv:2109.10272v1, https://arxiv.org/pdf/2109.10272v1. Section 2.4, (2.55)–(2.58), printed pp.12–13: type-A super-CFT, with the square-flavor stable range N_c≥2n_b. Sections 4.1–4.2, (4.21), (4.27), pp.28–29: the N_c=1, n_b=n_f=1 normalization is zero and a fermionic moment diverges. Section 4.3, (4.28)–(4.31), p.30: explicit corrected functional. Section 4.4, (4.39)–(4.54), pp.32–34: proof by kernel reproduction. This is the decisive primary mathematical source, not a conclusion drawn from its title. Its p.34 warns that the explicit calculation does not readily supply higher-flavor corrections.
- **Zirnbauer 1996**, *Supersymmetry for systems with unitary disorder: circular ensembles*, J. Phys. A 29, 7113–7136, https://www.thp.uni-koeln.de/zirn/011_Website_Martin_Zirnbauer/4_Publications/PDF_publications/09ColorFlavor.pdf. Equation (3) and footnote, p.7116, explicitly qualify flatness as local and mention the global anomaly. Appendix, pp.7133–7134, uses invariant-projector and normalization arguments. That caveat cannot be discarded, and does not give the needed explicit one-color boundary bounds.
- **Zirnbauer 1998**, arXiv:chao-dyn/9810016v1, https://arxiv.org/pdf/chao-dyn/9810016v1. Equation (1), pp.4–5, has one color and physical-dimension flavors. Its measure includes unspecified global-anomaly terms; §5's zero-mode approximation is expressly heuristic. The Hessian can still be extracted algebraically from the displayed determinant function. That extraction does not prove a global integral identity with the dots omitted.
- **Weidenmüller 2018**, arXiv:1812.00655v1, https://arxiv.org/pdf/1812.00655v1. Equations (3)–(9), pp.3–4, average directed-coordinate phases independently, use one 1|1 supermatrix per phase, and state disk/plane body and flat measure. The text immediately after (9) calls this exact. No boundary functional or boundary-source bound occurs in this step; the later source rescaling with nominal Berezinian one does not specify the transformed boundary. Its nonlinear estimates were already scoped as heuristic by the prior balanced-phase audit.
- **Gnutzmann–Altland 2005**, arXiv:nlin/0508009v1, https://arxiv.org/pdf/nlin/0508009v1. Equations (41)–(42), p.6, specify one color and F flavors and impose normalized standard measure. The graph application there has F=4 from direction and time reversal. Appendix C, pp.12–14, argues via a coherent-state projector. It does not calculate the missing small-color completion.
- **Pluhař–Weidenmüller 2015**, arXiv:1407.1148v2, https://arxiv.org/pdf/1407.1148v2. Equations (30)–(35), pp.10–11, use one phase per bond, with directions and replicas as flavor labels, SDet power one and explicitly flat Berezinian. No applicable boundary prescription is supplied. The domain sentence following (33) bounds the FF block; this cannot be silently treated as a correct BB-domain statement.

In particular, balance n_b=n_f makes the local invariant Berezin form flat. It does not remove the color threshold N_c≥2n_b: the 2021 one-flavor counterexample is itself balanced. For unequal retarded/advanced counts, the checked 2021 theorem explicitly restricts to square flavor blocks; no unstated rectangular extension is imported.

If a graph paper's integral notation is intended as shorthand for an invariant, boundary-completed functional, the literal bulk counterexample does not refute that interpretation. It instead identifies the indispensable missing specification and estimates. Neither an abstract measure name nor declaring its normalization supplies those data.

## 3. Reconstructed superintegral and boundary functional

Use four independent odd generators α,β,γ,δ and

Z=[[z,α],[β,w]],  tilde Z=[[bar z,γ],[δ,-bar w]],
|z|<1, w∈C, ∂_odd=∂α∂δ∂γ∂β.

Let G=γβαδ, so ∂_odd G=1; x=|z|², y=|w|², H=1+y, and

L=γβ+αδ+γwδz−α bar(w)β bar(z).

Then direct Berezinian algebra gives

S=SDet(1−tilde Z Z)=(1−x)/H−L/H²+G(1−y)/H³.

The source insertion is F=SDet^-1(1−tilde Z A Z B), A=diag(a,c), B=diag(b,d), with consistent advanced/retarded assignment. Interchanging the two whole sectors leaves the resulting scalar ratio unchanged.

The standard bulk is

I_bulk[F]=π^-2∫_{|z|<1,w∈C} d²z d²w ∂_odd(SF).

The correct pair completion adds the source's boundary differential functional

I_surface[F]=π^-2∫_{w∈C}d²w∫₀²πdθ ∂_odd(Ω SF)|_{z=e^(iθ)},

Ω=−L/(2H)+G[1/(2H²)+(1/(4H))∂/∂|z|].

The normal derivative acts before restriction to |z|=1. This is a distributional boundary completion, not an extra positive bulk density. It is related to the global Berezin-measure anomaly; it should not be confused without proof with every term customarily called an Efetov–Wegner term in other radial coordinates.

## 4. Exact full-source one-site computation

Write q=ab, r=cd, u=bc, v=ad, J=1−qx. The independent computation gives the bulk radial coefficient

C_bulk(x,y) = (1−y)(1+ry)/(H³J)
              −(u+v+2qrxy)/(H²J²)
              +qr(1−x)(1+qx)/(HJ³).

All angular factors are included: the bulk integrates this against dx dy. The boundary integrates

C_surface(y)=(1+ry)/[(1+y)²(1−q)].

No artificial pole at 1+cd|w|² remains: the inverse Berezinian is polynomial in c,d after proper cancellation. The only bosonic-source pole is 1−ab|z|², nonzero on the closed disk for |a|,|b|<1.

With the common cutoff |w|²≤T and ℓ(q)=−log(1−q)/q, ℓ(0)=1,

I_bulk(T)=(1−r)ℓ(q)T/(1+T)²
          +[(2r−u−v)T/(1+T)−r log(1+T)]/(1−q),

I_surface(T)=[(1−r)T/(1+T)+r log(1+T)]/(1−q).

Adding before taking the limit yields

I_bulk(T)+I_surface(T)
 =(1−r)ℓ(q)T/(1+T)² + [(1+r−u−v)/(1−q)] T/(1+T)
 →(1+cd−bc−ad)/(1−ab)=R.

Consequences:

1. At c=d=0 the bulk vanishes in the limit and the boundary supplies all of 1/(1−ab).
2. At cd≠0 the two pieces contain opposite logarithmic divergences. An absolute estimate of each piece separately can be meaningless even though their corrected sum is finite.
3. Matching c=a,d=b makes the physical ratio one but does not repair the raw measure; the separate bulk still diverges when ab≠0.
4. This matters for differentiated sources, not only normalization. With a=A(1+j), c=A(1−j), b=B(1+k), d=B(1−k), q₀=AB, the physical mixed derivative is 4q₀/(1−q₀). The coefficient of the surface log(1+T) has mixed derivative q₀(1−3q₀+4q₀²)/(1−q₀)³, nonzero for 0<q₀<1. Opposite boson/fermion source differentiation therefore does not automatically kill the missing term.

The full derivation, source ordering, independent exterior algebra, and exact antiderivative checks are in reviewer/one_site_boundary_audit.md and reviewer/verify_one_site.py. These are finite algebra checks, not a proof for interacting M-site superintegrals.

## 5. Why analytic continuation is not the original bulk measure

The normalization integral is one for integer N_c≥2, but zero when N_c=1 is substituted directly. The nonuniform factor responsible is of the form

ε(1−x)^(ε−1), ε=N_c−1>0.

As measures on [0,1], these converge weakly to δ₁. Evaluating the integrand at ε=0 before integration loses this boundary mass. The moment identity

ε∫₀¹x^m(1−x)^(ε−1)dx = m!/[(ε+1)…(ε+m)] →1

exhibits the mechanism exactly. Thus a properly defined distributional continuation may encode boundary terms; the naive exponent-one flat bulk does not. No graph-source prescription reviewed here defines the required continuation, proves interchange of its limits with source differentiation, and controls it at the microscopic radius.

## 6. Correct finite-size fallback for every fixed flavor count

There is an elementary exact representation that avoids the disputed change of variables. For V_θ=D_θU, define the finite determinant-ratio average directly, with all denominator-source moduli below one. Represent each denominator by a complex Gaussian and each numerator by a finite Grassmann Gaussian. Their bosonic quadratic forms have real part at least (1−r) times the Euclidean norm, where r is the largest denominator-source modulus.

For retarded/advanced fields collect the phase-coupled even bilinears at site i into X_i and Y_i. Then use the entire function

B(t)=Σ_{m≥0}t^m/(m!)²,

and the exact scalar identity

∫₀²π exp(e^(iθ)X+e^(−iθ)Y)dθ/(2π)=B(XY).

The disorder average is therefore the original Gaussian/Grassmann integral with ∏_{i=1}^M B(X_iY_i). For example the bosonic retarded part is X_i=Σ_α a_α bar(φ_{iα})(Uφ_α)_i; the advanced part is Y_i=Σ_β b_β(bar(ψ_β)U*)_i ψ_{iβ}, with the analogous fermionic bilinears included. The base weight is exp(−Σ||φ_α||²−Σ||ψ_β||²) times the Grassmann base weight.

Unitarity and Cauchy–Schwarz give Σ_i|X_i,bos|≤rΣ_α||φ_α||² and similarly for Y. Expanding the finite Grassmann algebra introduces only polynomial factors. Thus the phase integration, the entire series and the Gaussian integrals are absolutely controlled at each fixed M, flavor count and r<1. This proves an exact finite-size representation for arbitrary fixed higher flavors without claiming an effective collective-field theory or a uniform microscopic bound.

For one site, an equally simple flavor-complete form is obtained by expanding

∏_α(1−c_αt)/(1−a_αt)=Σ_{m≥0}p_m t^m,
∏_β(1−d_βt)/(1−b_βt)=Σ_{m≥0}q_m t^m.

The phase ratio is Σ_m p_mq_m, absolutely convergent for denominator sources inside the disk. Here p_m=Σ_j(−1)^j e_j(c)h_{m−j}(a), with negative-index h set to zero. This retains all occupation multiplicities. It does not identify a general higher-flavor boundary functional.

For the pair, one may alternatively apply the verified color-one corrected functional locally before further field manipulations. Doing so creates products of bulk and boundary distributions. Transferring this to a closed coupled superdeterminant integral, changing its gauge, or passing to growing M requires a consistent common regularization and justified limit interchange. None of those operations is supplied by merely writing a product of formal measures.

## 7. Exact remaining microscopic obligation

Let

G_M(a,b;c,d)=E det(I−cV_θ)det(I−dV_θ*)/[det(I−aV_θ)det(I−bV_θ*)].

Common-rotation invariance of the phase ensemble gives exactly

ab ∂c∂d G_M(a,b;c,d)|_{c=a,d=b}
 =Σ_{m≥1}(ab)^m B_M(m),
B_M(m)=E|Tr(V_θ^m)|².

At a=b=e^(−s/M), s>0, the requested annealed pair bridge is therefore

M^-2 ab ∂c∂d G_M|_{c=a,d=b} → (1−e^(−2s))/(4s²).

A usable superintegral proof must establish this for the completed, differentiated functional, with enough source uniformity for the desired compact-weight/Abel bridge. At microscopic radius 1−ab≈2s/M, the one-site boundary 1/(1−ab) is order M, and source derivatives can have higher poles. This calculation does not predict the complete M-site asymptotic size; it rules out dismissing the terms from their boundary support alone.

Beyond scalar S_U≥H/(2K²), the concrete remaining requirements are:

- complete local color-one functionals and their tensor-product regularization, including higher-flavor strata if that route is used;
- an admissible super-coordinate/gauge map carrying those distributions and their normal derivatives, with its full Berezinian;
- bounds on the full Grassmann coefficients and differentiated sources, including boundary traces, as the radius approaches one at order M^-1;
- a signed estimate after necessary bulk–boundary cancellations, with dimension, diagram counts and all interaction orders controlled.

The scalar estimate controls a function in the strict bosonic interior. A normal derivative of a vanishing factor need not vanish at the boundary, and divergent pieces cannot be bounded separately. The source rescaling with local Berezinian one also moves a bosonic boundary and must transform its functional. These are exact analytic obstacles, not an asserted failure of the universality prediction.

Even a repaired and bounded annealed integral leaves the original deterministic off-charge defect unestimated. TRACE-005 and BGS remain open.

## 8. Canonical impact, execution and search boundary

The path-by-path canonical assessment is in canonical_impact.md. No registered proved BGS theorem was identified as depending on the false bulk-only identity. FM-018's finite matrix/channel statements and the scalar/block coercivity statements remain valid as independently defined mathematics. Source-exactness exposition and generic claims of a rigorous graph template require qualification; historical records should receive appended corrections through the normal process.

Executed controls:

- python3 checks.py > checks.json: exact residue derivation of the requested ratio; N_c=1,…,6 normalization values; boundary-concentration moments m=0,…,6; one-site flavor-cancellation controls k=1,…,4; graph-type opposite-source curvature. Python 3.12.14, SymPy 1.14.0, 60-second timeout, one BLAS/OpenMP thread. All passed.
- python3 reviewer/verify_one_site.py: independently implemented four-generator exterior algebra, inverse Berezinian, bulk and surface coefficients, and cutoff antiderivatives. All passed. No external CAS numerical integration was used.
- The decisive correction page (printed p.30) was rendered and visually inspected. Sources are primary PDFs with version headers retained. A failed guessed v2 download returned 404; the actual source is v1 and no v2 claim is made.

Search covered the prior balanced-phase/coercivity reports, current canonical authorities and relevant source discussions, the original CFT papers and their graph applications, the 2021 correction, and bounded exact-term searches for later higher-flavor/boundary developments through 7 October 2026. No exhaustive literature absence or novelty claim is made. This obstruction and its pair repair were already known in the 2021 source; the present output applies and explicitly checks them for the proposed bridge.
