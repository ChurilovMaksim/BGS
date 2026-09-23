# Independent internal adversarial review: full-lag uniform resonance gap

Reviewed source: `uniform_resonance_attempt.md`, 23 September 2026. This review reconstructs the argument rather than accepting its status label. It is a separate internal agent review, not external referee acceptance, formal verification, or a literature-priority assessment.

**Verdict: the stated inequalities (1) and (6) are supported by the proof. No fatal gap or incorrect constant was found.** The result is confined to the classical observable lattice transported by the linear map S. It supplies no quantum trace estimate and no nonlinear-transport theorem.

## 1. Matrix and normalization reconstruction

The physical-space matrix is S=[[3,4],[2,3]], so the Fourier action of C:f→f∘S is A=Sᵀ=[[3,2],[4,3]]. For λ=3+2√2, the stated covectors ξ=(1,1/√2), η=(-1/√2,1/2) satisfy ξA=λξ, ηA=λ⁻¹η and det[[ξ],[η]]=1. Thus det(u,v)=ξ(u)η(v)−η(u)ξ(v) exactly, without an additional √2 factor.

For the convention {f,k}=f_q k_p−f_p k_q, the Fourier coefficient contributed by (u,v) to {f,Cʳk}/(4π) is **−π det(u,Aʳv) f̂(u) k̂(v)**. The proof only uses its magnitude; the suppressed overall minus sign has no effect on any operator or lower bound. If the bracket convention is reversed, the sign reverses throughout and the same estimates hold.

With Jω(f)_O=Σ_j f̂(Aʲv_O)e^{ijω}, the coefficient identity (Cf)̂(Aʲv_O)=f̂(A^{j−1}v_O) gives Jω(Cf)=e^{iω}Jω(f). The translation phase and subsequent Parseval step therefore have the correct direction.

## 2. One-visit lemma

Every nonzero integer vector has both eigen-coordinates nonzero, since √2 is irrational. For horizontal-cone frequencies set t=y/x∈[−1,1]. Then ρ=(1+t/√2)/(1−t/√2) is positive, increasing in t, and lies in [λ⁻¹,λ]. Vertical frequencies have ρ=−1. The actual ratio E₀/D₀ equals ρ(u)/ρ(v): the common factor −√2 in ξ/η cancels. Therefore the ratio is negative or is in (0,λ²].

Expanding q(u+Aʳv), with q(k)=det(k,Ak), gives q(u)+q(v)+(λ⁻¹−λ)[D₀λʳ+E₀λ⁻ʳ], where D₀=η(u)ξ(v)≠0. Its discrete derivative, after dropping the fixed nonzero multiplier, is D₀λʳ(λ−1)[1−(E₀/D₀)λ^{−2r−1}]. The bracket is strictly positive for every r≥1, including cone-boundary pairs where E₀/D₀=λ². Hence q-values are strictly monotone. Since q is A-invariant, no oriented orbit can recur. A zero frequency, if present, has zero determinant contribution and causes no problem.

For a fixed ordered Fourier pair, the synthesis matrix consequently has exactly one possible row per lag and no repeated rows. Its columns are orthogonal even after the dynamical phases are inserted. Its norm is the supremum of its coefficient magnitudes. The bound π[Y(f)X(k)+λ⁻²X(f)Y(k)] follows by the triangle inequality in bounded-operator norm. This is an all-lag proof, not a finite collision search.

## 3. Physical symbol and Fourier moments

I expanded the physical symbol directly as a product of Fourier series. The q-only factor r has coefficients r₀=1, r_{±1}=1/2, r_{±7}=−1/2, r_{±6}=r_{±8}=−1/4. The shifted factor multiplies these coefficients by (−1)^k. The p=+1 coefficient of cos(2πp−α) is (−3−4i)/10. These identities reproduce every row of the attempted proof's coefficient table, including the easily reversed imaginary signs in the p-dependent rows and at k=8,9.

The dominant coefficients are exactly ĝ(±7,0)=9/20 and the constant is zero. For the remainder, the q-only X contribution is 2√101/25+9/200; mixed nonvertical modes contribute 3/20; vertical modes contribute √2/200. Consequently E=2√101/25+(39+√2)/200 and Y(e)=E/√2. The latter identity follows by pairing x with −x at fixed nonzero y, not from an assumed symmetry of complex coefficients themselves. The exact weighted real/imaginary second moment is 51451/1000.

A separate elementary floating-point convolution reproduced the 32 nonzero Fourier coefficients, E=1.0060611175015368, Y/E=1/√2, and the second moment 51.451. These numerical checks supplement the algebra above and are not used as proof. SymPy was unavailable in this runtime; no symbolic-software verification is claimed.

## 4. Dominant harmonic lower bound

For v=(7,0), q(v)=196. The four outputs are ±(v+Aʳv) and ±(v−Aʳv). Their q-values are q(v)(2±(λʳ+λ⁻ʳ)). The plus family is positive and strictly increasing in r; the minus family is negative and strictly decreasing. This separates every lag and the two types. The remaining opposite vectors cannot be A-iterates of one another: ξ(Aⁿk)=λⁿξ(k) cannot equal −ξ(k). Hence every output row across all columns is distinct.

Each column has four entries of equal magnitude π(9/20)²λ⁻ʳ|det(v,Aʳv)|. Its norm is twice that magnitude. Since ξ(v)η(v)=−49/√2, λ⁻ʳ det(v,Aʳv)=(49/√2)(1−λ⁻²ʳ), so the minimum is at r=1. Using det(v,Av)=196 gives s_b/π=2(9/20)²·196/λ=3969/(50λ)>68/5. No factor of two is lost from the two orientations.

## 5. Perturbation constants and direct integral

Bilinearity gives S_g−S_b=B_{b,e}+B_{e,b}+B_{e,e}; applying the one-visit estimate yields exactly π(1+λ⁻²)[(63/5)E+E²]/√2. The rational majorants in the source bound its coefficient by 10.024205964<401/40. The lower bound is therefore (68/5−401/40)π=(143/40)π, which is larger than 7π/2. The same bounds give the upper coefficient below 40. Direct numerical evaluations, for orientation only, are s_b/π≈13.61945484, perturbation bound/π≈9.96418228, and upper bound/π≈38.85540890.

The operators extend from finite lag sequences by their uniform upper bound; the lower bound extends by continuity. For finite translated arrays, a_r(ω)=Σ_l a_{r,l}e^{ilω}. Applying the pointwise operator inequalities and integrating with normalized circle measure is valid. Fourier Parseval first along oriented A-orbits and then in l gives exactly inequality (1), including complex arrays and arbitrary finite translation windows.

## 6. Unrestricted infinite-support neighborhood

For arbitrary M1 perturbations the one-visit geometry need not persist. The source correctly switches to the unrestricted two-visit estimate. Its proof uses a quadratic equation in λʳ for an invariant q-value, so at most two inputs occupy each row; phases do not affect the √2 norm bound. Absolute convergence in M1 permits summing pair operators uniformly in ω and proves the estimate for infinite supports.

With D=diag(1,√2), D⁻¹AD is symmetric with eigenvalues λ,λ⁻¹. Therefore ||Aʳ||≤||D||||D⁻¹||λʳ=√2λʳ, proving κ_A≤√2. Also M1(g)≤Σ(|Re ĝ|+|Im ĝ|)|v|²<52, because nonzero integer |v|≥1. For M1(w)≤1/100, the perturbation norm is at most 2π(1/100)(104+1/100)=(10401/5000)π. Thus the lower coefficient remains at least 1.4198π>π and the upper coefficient at most 42.0802π<43π. Squaring gives (6).

Constants in w disappear from brackets, as required by the definition of M1. The M1 regularity implies continuously differentiable observables and absolutely convergent bracket Fourier series, so no unstated smoothness assumption is needed. Real perturbations suffice as stated.

## 7. Editorial clarifications recommended

1. Define Jω explicitly in the note, including normalized measure and orbit representatives, or cite the definition with its precise source section.
2. State the bracket's global Fourier sign once; the magnitude-only proof remains unchanged.
3. Write the similarity as D⁻¹AD with D=diag(1,√2) to remove the convention ambiguity in “conjugating by”.
4. Describe this as a verified internal project result and preserve the stated separation from nonlinear transport, quantum traces, and BGS. No assertion about external novelty follows from this review.
