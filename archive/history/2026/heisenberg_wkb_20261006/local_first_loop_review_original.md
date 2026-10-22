# Independent audit of the rotated-box first-loop theorem

Date: 6 October 2026. Read-only review of the author's sources; no canonical edits.

## Claim and primary verdict

**Verdict: proved as written, for the explicitly defined rotated, Gaussian-conditioned box integral.** The conclusion does not require an additional contour theorem or a zero-free-logarithm theorem for the original trace. Those would be additional results about a different object. The proof's analytic estimates can be reconstructed with constants independent of the dimension. There are several omitted conventions/estimates that should be made explicit before promotion; they are listed below and proved here from the existing hypotheses. In particular, this verdict is not based on a central-limit heuristic or on the accompanying finite computations.

The normalized claim is the following. Fix the WKB truncation order (J), the specified physical coupling, and (b<\infty). For every positive integer (m), every real stationary class of the stated actual local phase, and sufficiently small (h=(2\pi N)^{-1}) with (mh\le b), set (G=K^{-1}), (B_h=[-\rho/\sqrt h,\rho/\sqrt h]^m), and

\[
Z_{m,h}=\mathbb E[\exp(R_h(Y))\mid Y\in B_h],\qquad Y\sim N(0,G).
\]

Here (R_h) is the exact exponent obtained by evaluating the fixed finite-(J) analytic local amplitude and phase on the specified rotated box. Then

\[
Z_{m,h}=e^{h\ell_{1,m}}+
O_b\bigl(mh^{3/2}+h\sqrt m+e^{-c/h}\bigr),
\qquad |h\ell_{1,m}|\le Cmh.
\]

Thus the stated relative (O_b(\sqrt h)) follows. Constants may depend on fixed (J), the fixed coupling, local analytic bounds, and (b), but not on (m), the stationary class, or sufficiently small (h). The box radius is fixed before taking (h\to0).

### Exact reviewed revisions

- `rotated_local_first_loop.md`: SHA-256 `7550e19989ba9efe41bf5f2b3daf5199a2952d6e144fb8e1b95f2fc0da4602b3`
- `uniform_cluster_lemma.md`: SHA-256 `c027ac2df67f3c25a46cdd4970f984a1d50fbd5f3aa74432ebee433ba52e4c67`
- `literature/convex_box_poincare_check.md`: SHA-256 `f3068ce4bb3bac06151224ffe1f59535aa2504a7411aecc5c6a8797b315a95a4`
- Actual-model source `/workspace/shared/BGS/mathematics/four_branch_parametrix.md`: SHA-256 `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`, matching the author's source-hash record.

## Corrections and clarifications to make explicit

1. **Row sums of suprema.** Lines 71–73 give a pointwise off-diagonal row bound. Line 86 subsequently uses the stronger statement
   (\sum_{k\ne j}\sup_{B_h}|V_{jk}|\le0.7).
   A pointwise row bound alone does not imply this. In this model each row has bounded local support, and (L4) bounds every perturbation entry uniformly. Hence the sum of entrywise suprema is bounded by a fixed local-degree factor times (C\rho+Ch). Decreasing (\rho) again gives the stronger statement, simultaneously for the finite family of required tilts. This supplies the missing justification without changing the theorem.
2. **Upper diagonal curvature.** The assertion (q_j''\le2), line 188, requires (V_{jj}\le2). It is not a consequence of the stated lower-curvature inequalities alone. The actual Hessian has (K_{jj}=3/2+O(\epsilon)) for (m\ge2), and the same small perturbation bound supplies (V_{jj}<2). For (m=1), (K_{11}=1+O(\epsilon)). Record this upper bound explicitly.
3. **Flux norm.** At line 194, the correct statement is
   (\|G\nabla P\|_\infty\le C(1+\rho^2/h)), or the corresponding bound on each normal component. A Euclidean norm need not obey a dimension-free bound. For example, a local linear polynomial with all gradient coordinates equal to one produces a Euclidean norm of order (\sqrt m). The face estimate only uses one component and is valid as stated after specifying the norm.
4. **Signed boundary term.** The boundary contribution in Gaussian integration by parts is **minus** the outward flux displayed in the text. Writing “+ boundary” in (L10) is harmless if the signed boundary term is defined accordingly. An exact formula is given below.
5. **Tilt family.** Include the pure cubic/linear exponents (t\sqrt hW), and the exponents (c\sqrt hW+\mu), in the family covered by (L4)–(L7). They are used later but are not literally among “the exact exponent, its truncation, and their convex interpolants.” The same estimates prove their inclusion immediately; constants added to an exponent do not affect curvature.
6. **Precise Poincare locator.** Theorem 3.1 is on printed p. 13 of the retained source, while equation (3.2) is on printed p. 14, not p. 13.
7. **Normalization.** The authoritative object is the displayed conditional expectation. Merely dividing an unnormalized rotated-box integral by the full Gaussian determinant would give (\mathbb P(B_h)Z_{m,h}), not exactly (Z_{m,h}). This distinction costs only an exponentially small term in the stated regime, but should not be blurred in an eventual contour application.

None of these repairs changes the claimed object, rate, or parameter range.

## Dependency graph and obligation matrix

The actual phase/transport construction supplies local real analyticity, positive leading amplitude, bounded local jets, and the near-(K_0) Hessian. These give the normal form and uniform convex tilted potentials. Conditional one-dimensional mode estimates give raw moments. The checked convex-domain Brascamp–Lieb theorem gives Poincare, which combines with those raw moments to give exponential weights and marginal curvature. Separately, Gaussian Wick contraction plus the covariance row bound gives the extensive polynomial and Stein-factor variances. Gaussian integration by parts on the box, with explicitly controlled faces, gives the complex MGF comparison. Two weighted (L^2) replacements finish the result.

| Obligation | Status | Basis |
|---|---|---|
| Actual massive cyclic Hessian, including (m=1,2) | Passed | Direct quadratic form and actual source's (C^2) perturbation bound |
| Positive leading amplitude and real (W) | Passed | Real scalar transport with initial value one |
| Fixed-(J) analytic local logarithm and uniform Taylor bounds | Passed | Finite analytic transport construction and compact/glued local charts |
| Raw coordinate moments under all required real tilts | Passed | Conditional clipped-mode contraction; details below |
| Poincare on a hard box | Passed | Exact primary theorem plus checked convex exhaustion |
| Exponential moment control | Passed | Poincare plus fourth raw moments and parity |
| Gaussian polynomial and Stein-factor variances | Passed | Connected contractions, including the two deterministic covariance edges |
| Complex IBP identity and exponentially small faces | Passed | Exact identity and marginal-density argument below |
| First-coefficient identification and final relative error | Passed | Formal covariance rotation and bounded exponential factor |
| Entire all-order formal bound (B3) | Passed as a formal statement | Its combinatorial proof does not assert convergence; not needed in full for this theorem |
| Uniform original trace/saddle decomposition | Out of scope and unresolved | No contour deformation or gluing provided |
| Absolute summation over exponentially many classes | Out of scope and unresolved | An algebraic local error does not overcome exponential orbit mass |

## Reconstruction of the load-bearing estimates

### 1. Actual-model input and the rotation

From the actual one-step quadratic phase, the cyclic Hessian satisfies

\[
v^TH_0v=-\tfrac32\sum_jv_j^2+\tfrac12\sum_jv_jv_{j+1}.
\]

Thus (K_0=-H_0) has spectrum in ([1,2]). At (m=1) the repeated coordinate gives (K_0=1), and at (m=2) the off-diagonal entries are (-1/2), rather than (-1/4). For (m\ge3) the two off-diagonal entries are (-1/4). The actual per-edge perturbation produces operator norm at most (4\epsilon), uniformly in (m). The claimed diagonal dominance and (\sup_j\sum_k|G_{jk}|\le5/4) follow by the indicated Neumann series. Finite propagation also proves the stated cyclic-distance decay; the weaker row-sum bound alone suffices for this local theorem.

The leading transport equation has real coefficients on real charts. Along its real characteristics, its solution is the exponential of an integral of a real scalar coefficient, with initial value one. Hence (a_0>0). The finite-order transports are analytic by induction along the analytic characteristic flow. For fixed (J), shrink the common local complex neighborhoods so that the leading amplitude, and then the finite amplitude polynomial for small (h), remain nonzero. A local analytic logarithm follows. No estimate uniform as (J\to\infty) is used.

With (c=e^{-i\pi/4}), one has (c^2=-i) and (ic^3=c). Therefore the quadratic phase becomes (-y^TKy/2), and both the phase-cubic and leading-log-amplitude-linear terms have coefficient (c\sqrt h). Their sum (W) has real coefficients. The quartic phase and quadratic leading-log-amplitude enter (Q), as does the symbol-order-(h) constant. When converting the original WKB powers (N^{-r}), use (N^{-r}=(2\pi h)^r); this affects coefficients, not the grading or estimates.

Every local phase remainder has degree at least five and contributes (h^{3/2}) times a bounded fifth-degree majorant on the scaled box. The log-amplitude remainders have lower powers of (y) and are bounded by the same majorant. This proves (L3). Locality and analytic derivative estimates prove (L4), including the sum-of-entrywise-suprema version after the finite local-degree factor is included.

### 2. Conditional raw moments really are uniform

For a real tilted potential (V), use the strengthened bounds

\[
V_{jj}\ge a=1.3,\quad
\sum_{k\ne j}c_{jk}\le d=0.7,\quad
c_{jk}=\sup|V_{jk}|,\quad |V_j(0)|\le C\sqrt h.
\]

Condition on all other coordinates; conditioning on the neighboring coordinates is equivalent for the local interaction. Since the interval contains zero, the conditional clipped minimizer (a_j) satisfies

\[
|a_j|\le a^{-1}\Bigl(C\sqrt h+\sum_{k\ne j}c_{jk}|y_k|\Bigr).
\]

This remains true when the minimizer lies on the boundary. For a one-dimensional potential (U''\ge a), on either nonempty side of its clipped minimizer the ratio of its radial density to (e^{-at^2/2}) is decreasing. Normalizing that side therefore gives stochastic domination by a half-Gaussian. Consequently

\[
\mathbb E[|Y_j-a_j|^p\mid Y_{-j}]^{1/p}\le C_{p,a}
\]

for every fixed (p\ge1). This argument does not require an upper curvature bound, a uniformly bounded conditional mean, or an unbounded conditional domain.

Taking unconditional (L^p) norms and their maximum gives

\[
M_p\le(d/a)M_p+C_{p,a}+C\sqrt h/a.
\]

Because (d/a<1), (M_p) is bounded independently of dimension and radius. At (m=1), there is no neighbor term and curvature at least (0.8) suffices. This genuinely controls raw moments, not only centered variances.

### 3. Exact external Poincare input

I checked the retained primary-source text against the cited statement. Kolesnikov–Milman, arXiv:1310.2526v7, Theorem 3.1(1), gives the locally-convex-boundary Brascamp–Lieb inequality for every (C^1) test function. Taking generalized dimension infinity and Euclidean metric gives the inverse-Hessian form. Equation (3.2) then gives constant (1/\lambda) for Hessian lower bound (\lambda I). No Neumann condition on the tested observable is required.

The approximation (\sum_j(y_j/R_j)^{2k}\le1) is smooth at its boundary, convex, increasing in (k), and exhausts the box interior. Its defining gradient cannot vanish on level one. Normalized measures, variances, and gradient energies converge by dominated convergence for each fixed finite dimension. The constant remains (1/\lambda); the exhaustion need not converge uniformly in dimension. The same argument applies to each conditional lower-dimensional box used later.

This validates (\operatorname{Var}_\mu f\le2\mathbb E_\mu|\nabla f|^2) at the exact strength required.

### 4. Exponential weights

For each required real exponent (H), including pure multiples of (\sqrt hW), define

\[
f(s)=\log\mathbb E_Be^{sH}.
\]

Its tilted law has the moment and curvature bounds just proved. Locality and the gradient estimate yield

\[
f''(s)\le2\mathbb E_s|\nabla H|^2
\le Ch\sum_j\mathbb E_s(1+\textstyle\sum_{k\sim j}|Y_k|^4)
\le Cmh.
\]

At (s=0), the term of order (\sqrt h) is globally odd, and the centered Gaussian and symmetric box are invariant under (Y\mapsto-Y). Thus it has exactly zero expectation. The remaining terms have expectation (O(mh)). Integrating over a fixed bounded (s)-interval yields (f(s)\le Cmh). Only a finite bounded tilt range is needed, so the single small choice of radius suffices. For (c\sqrt hW+\mu), the additional constant satisfies (|\mu|\le Cmh).

### 5. The Stein-factor variance has only one volume factor

Gaussian Wick ordering preserves the local support of each degree-one/three summand of (W). The coefficients introduced by Wick ordering use only covariance entries bounded by (5/4). Hence (P=W_1+W_3/3) is again a sum of bounded local degree-one/three polynomials, and (-LP=W) for (L=\operatorname{Tr}(G\nabla^2)-y\cdot\nabla).

Set (A_i=\partial_iW), (B_k=\partial_kP). These have degree at most two and uniformly bounded local support. Then

\[
\Gamma/h=\sum_{i,k}G_{ik}A_iB_k.
\]

In its variance, each term contains the deterministic edges (G_{ik}) and (G_{pq}), multiplying
(\operatorname{Cov}(A_iB_k,A_pB_q)). Subtracting the product of expectations removes exactly the Wick pairings with no edge between the two products. Every surviving graph is connected **after adjoining the two deterministic edges**. It has at most four local vertices and finitely many legs. A spanning-tree summation using the absolute row bound leaves one root label, hence a factor (m), while all remaining factors are uniformly bounded. This proves

\[
\operatorname{Var}(\Gamma)\le Cmh^2.
\]

Full Gaussian integration by parts gives (\mathbb E\Gamma=h\mathbb EW^2=\beta). The same simpler two-vertex argument proves the variances of (W) and (Q). No stationarity of the site coefficients or limiting covariance profile is required.

Conditioning causes no difficulty for these specific estimates: whenever (\mathbb P(B_h)\ge1/2),

\[
\mathbb E_B|\Gamma-\beta|^2\le2Cmh^2,
\qquad
\mathbb E_B|hQ-\mu|^2\le2Cmh^2.
\]

This direct nonnegative-integral comparison avoids needing a separate tail-polynomial expansion for either estimate.

### 6. Boundary density and exact complex IBP

Write (p_G) for the full Gaussian density. The exact identity is

\[
F'(t)=t\mathbb E_B[\Gamma e^{tX}]
-\frac{\sqrt h}{\mathbb P(B_h)}
\int_{\partial B_h} e^{tX}(n\cdot G\nabla P)p_G\,d\sigma,
\quad X=\sqrt hW.
\]

It follows by integrating (\operatorname{div}(p_GG\nabla P)=p_GLP). The box corners have surface measure zero; no boundary condition on (P) or on the exponential is asserted.

For the real tilt (uX), (u=\operatorname{Re}t), let (q_j) be the negative log of its normalized coordinate marginal. Differentiation at fixed coordinate, on an integration domain independent of that coordinate, gives

\[
q_j''=\mathbb E[V_{jj}\mid Y_j]-\operatorname{Var}(V_j\mid Y_j).
\]

Conditional Poincare and the strengthened row-supremum bound give

\[
\operatorname{Var}(V_j\mid Y_j)
\le2\sum_{k\ne j}c_{jk}^2\le0.98.
\]

Together with (1.3\le V_{jj}\le2), this gives (0.32\le q_j''\le2). The mean of this marginal is bounded by the raw-moment result. The one-dimensional mode-distance argument then bounds its clipped mode. For small (h), that mode is an interior point a uniformly bounded distance from zero and far from both endpoints. On a unit neighborhood of the mode, the upper curvature bound bounds the loss in density, so normalization bounds its peak by a dimension-free constant. The lower curvature bound then gives

\[
p_j(\pm\rho/\sqrt h)\le Ce^{-c/h}.
\]

This step is valid even though conditioning on a coordinate at the face can shift neighboring coordinates substantially: conditional Poincare uses curvature, not conditional raw moments.

Finally,

\[
\max_j|(G\nabla P)_j|\le C(1+\rho^2/h).
\]

For each face, the absolute tilted face integral is the real tilt normalization times the corresponding marginal density. The normalization is at most (e^{Cmh}). Summing the (2m) faces gives (C_bmh^{-1/2}e^{-c/h}). Gaussian tail bounds give (\mathbb P(B_h^c)\le2m e^{-c_0/h}), so all denominators are harmless uniformly for (mh\le b). Polynomial factors in (h^{-1}) can be absorbed by decreasing the exponential constant.

Cauchy–Schwarz and the exponential weights bound the bulk error by (C_bh\sqrt m). Solving the resulting scalar differential equation along the complex segment (0\to c), with bounded integrating factor since (\beta=O_b(1)), gives (L11). No real MGF of an uncut cubic polynomial is used.

### 7. Final replacement and coefficient identity

Minkowski and fixed Gaussian moments give (\|T_h\|_{L^2(B_h)}\le Cmh^{3/2}). The inequality

\[
|e^A-e^B|\le |A-B|(e^{\operatorname{Re}A}+e^{\operatorname{Re}B})
\]

follows directly by integrating along the straight segment from (A) to (B). Applied with the proven exponential weights, it removes (T_h) at cost (C_bmh^{3/2}), then replaces (hQ) by (\mu) at cost (C_bh\sqrt m).

The first connected coefficient is exactly

\[
\ell_{1,m}=\mathbb E_GQ+\frac{c^2}{2}\mathbb E_GW^2.
\]

This agrees with (B2)'s unrotated Fresnel convention because every contraction transforms from (G) to (c^2G=-iG), while the rotated vertex factors transform consistently. Consequently the leading exponential is (e^{\mu+c^2\beta/2}=e^{h\ell_{1,m}}). Its inverse modulus is at most (e^{Cmh}), completing the relative estimate.

## Audit of the needed formal-cluster dependency

The proof of (B3) is sound as a formal coefficient statement. At total grade (2k), there are at most (2k) vertices and at most (6k) legs. Rooting an already chosen connected pairing at a deterministic spanning tree adds no count of possible trees. Summing labels contributes only (m(5/4)^E). The estimate

\[
(2E-1)!!/r!\le2^{k+r}(3k)^k\le C^kk!
\]

is valid for (E\le k+r), (r\le2k), separately treating (E<r). Ordered grade compositions, phase/amplitude types, symbol orders, and local monomial choices contribute only an exponential factor in (k). Degree-zero vertices occur only as isolated connected components and are handled separately. None of this proves convergence of the formal series, but convergence is not used by the first-loop box theorem.

The auxiliary one-step operator-error claims (A1)–(A3) are not needed for the local-integral conclusion; this audit does not promote those separate claims on the basis of the local proof.

## Evidence, remaining gap, and safest use

The work consisted of direct reconstruction of the inequalities, checking the retained primary-source theorem and its hypotheses, reading the actual phase/transport source, and hashing the reviewed files. No numerical experiment was used as evidence for an infinite-dimensional or uniform asymptotic statement.

**There is no remaining analytic gap in this defined-box theorem after the explicit elementary clarifications above.** The cheapest next step is to insert those clarifications, especially the supremum-row condition, the componentwise flux norm, and the complete tilt family, into the author proof and pin the resulting revision for review/promotion.

The strongest safe use is a dimension-uniform local first-loop resummation for this deliberately defined Gaussian-conditioned rotated integral. It does not establish that the original lattice trace equals a sum of these local integrals, that side contours cancel, that the global logarithm is zero-free, that all-order remainders are exponentially small, or that absolute saddle summation is entropy-compatible. Those unresolved implications cannot be supplied by rephrasing this theorem or by its successful local audit.
