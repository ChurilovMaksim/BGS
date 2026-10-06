# Independent audit of the physical homoclinic weight dictionary

6 October 2026. This is a fresh internal mathematical audit, not external refereeing or formal verification. The frozen candidate and canonical repository were not edited.

## Normalized claim and primary verdict

**Primary verdict: proved as written.**

At the literal coupling τ=10⁻⁸⁰, the candidate correctly identifies the actual leading periodic-orbit weight, constructs a C^{1,1/2} physical unit-homoclinic map and nonstationary physical phase, and identifies the limiting geometric-mean weight with the square root of that map's area Jacobian. Its physical-area oscillatory integral is O(N⁻¹/²). W14–W15 retain the exact finite-h box factors.

This verdict respects the candidate's explicit scope: its passage from finite weighted periodic sums to area integrals remains conditional on the separate norm-uniform estimate EQ. This review does not approve the new EQ candidate and does not turn W15 into a harmless factor. The separately reviewed quantum first-loop argument, the full displacement sum, torsion sectors, TRACE-005, and BGS are not conclusions of this audit.

Frozen target: `bgs_paired_box_cancellation/physical_homoclinic_weight_dictionary.md`, SHA-256 `5bee8e6b45ae785d8fa14c4caf40e959cd49c79cbbd97e319a9ff4eb1b9037ff`.

Additional graph-transform expansion read: `physical_graph_transform_details.md`, SHA-256 `aaa8d335a6f4068accf5ec75762007b454339d928fda6b1fda25f2a8cda2c1fb`. This is separately pinned, not silently treated as part of the frozen target or its eleven-entry source manifest. The estimates below reconstruct the needed argument.

## Claim card and dependency graph

- Physical map: F=S∘Φ_g^{τ/(2π)}, S=[[3,4],[2,3]], with the unchanged ordinary-midpoint symbol and quantizer. It is the forward generating map p=S_x, P=−S_y; it is not the inverse Egorov convention used in some other sources.
- Labels: G_m=Fix(S^m), D_m=|G_m|. Actual periodic points are χ(G_m).
- Regularity: χ is the bounded near-identity structural homeomorphism, only Hölder as used here. C^{1,1/2} assertions concern the physical invariant slope fields, bounded lifted leaf segments, B, and Ψ_d.
- Homoclinic displacement: d=(1/√2,−1/2) mod Z². Its finite counterpart is d_m=(S^m−I)⁻¹(0,1).
- Weight: ρ_m(z)=|det(I−DF^m(χz))|⁻¹. The paired coefficient uses the geometric mean of two such weights, with an outer sum over z, rather than Haar-normalized labels.
- Quantum scale: h=(2πN)⁻¹ in W14–W15; the original one-step WKB coefficients remain powers of N⁻¹=(2πh).

Dependency arrows:

1. Actual generating phase and transport → W1–W3 (Hill and Van Vleck normalization).
2. Accepted bounded stationary equation and gluing → W4 (physical conjugacy).
3. Actual C³ perturbation bounds + explicit bundle graph transform → C^{1,1/2} physical slopes.
4. Finite-interval leaf ODEs + scalar implicit function theorem → W6–W8 (physical phase and selected homoclinic map).
5. Exact P7/P8 pairing + W3 → W9; area preservation → W10.
6. Centered homoclinic sums + both leaf Jacobian products + bundle-angle cancellation → W11–W12.
7. W7 nonstationarity + Hölder Jacobian → W13.
8. Definition of the conditioned rotated-box integral → W14–W15, with its probability factors intact.
9. A separate EQ theorem would be needed for finite-sum transfer. No arrow to EQ is supplied by W1–W15.

## Obligation matrix

| Obligation | Status | Reason |
|---|---|---|
| W1 generating-map differential and determinant | Passed | Direct differentiation, det M_j=1 |
| W2 cyclic Hill identity including m=1,2 | Passed | Twisted determinant reconstructed below |
| W3 actual a₀ and all scalar prefactors | Passed | HJ derivative, exact transport uniqueness, P7 normalization |
| W4 χ is a homeomorphism conjugating the actual map | Passed | Bounded corrections, exact lift relation, hyperbolicity and degree |
| W5 C^{1,1/2} invariant slope fields | Passed | A strict graph-transform contraction with numerical margin |
| Finite lifted-leaf initial-point dependence | Passed | Bounded-time ODE variational equations; no global-holonomy shortcut |
| W6 selected root | Passed | Difference slope uniformly near √2 and a fixed interval |
| W7 physical phase and ∂qB≥1/2 | Passed | Exact source identification and implicit-function derivative bound |
| W8 exact unit branch and positive Jacobian | Passed | Integer momentum jump and gluing; regularity from finite leaves |
| W9 geometric mean and normalization | Passed | D_m cancels exactly in the P8 autocorrelation |
| W10 determinant weight | Passed | Positive reciprocal periodic multipliers |
| W11 ratio, sign and angle factor | Passed | Explicit future/past products below |
| W12 half-density interpretation | Passed | Change of variables for the actual Jacobian |
| W13 Fourier-decay bound | Passed | Degree-one change of variable and translation difference |
| Finite weighted periodic estimate EQ | Conditional, separately reviewed | Not asserted proved in the frozen target |
| W14–W15 exact finite-h factor | Passed | Conditional expectation and full Gaussian normalization are distinct |
| Harmlessness/locality of W15 | Not addressed in this target | No inference from the per-class first-loop error |
| Full displacement sum, torsion, TRACE-005, BGS | Out of scope | A selected coefficient is not the full signed sum |

## 1. Hill identity and exact leading transport

Writing a=−S_xx, b=S_xy, c=−S_yy gives

dp=−a dx+b dy,  dP=−b dx+c dy.

Solving for dy produces exactly W1, with determinant one. The cyclic negative Hessian has diagonal a_j+c_{j−1} and the two indicated edge entries. At m=1 both endpoints are the same variable, so the entry is a+c−2b. At m=2 the two edges occupy the same off-diagonal pair and add.

For a twist z≠0, use x_m=z x_0 and x_{−1}=z⁻¹x_{m−1}. Let K(z) denote the resulting Jacobi matrix. Its determinant is

C−(∏b_j)(z+z⁻¹).

For m≥3 the coefficients of z and z⁻¹ are the two cyclic permutations, each with sign −∏b_j. The exceptional matrices give the same formula directly:

- m=1: K(z)=a+c−b(z+z⁻¹).
- m=2: the off-diagonal entries are −b₀−b₁z⁻¹ and −b₀−b₁z.

The recurrence K(z)x=0 is precisely the W1 transfer recurrence with monodromy multiplier z. Thus, first for generic coefficients and then by the polynomial identity principle for all b_j≠0,

det K(z)=−(∏b_j) z⁻¹ det(M−zI).

At z=1 this is W2. Positivity of the actual Hessian and b_j>0 give tr M>2. In particular det(I−M)=2−tr M is negative; the absolute value in W3 is required.

Differentiating S_t=g(x,S_x)/(2π) first in y and then x gives exactly

b_t=(g_p/2π)b_x+(g_qp+g_pp S_xx)b/(2π).

Therefore 2√b solves the actual leading amplitude transport and equals one initially, since b(0)=1/4. Uniqueness gives a₀=2√b. This uses the real leading transport of the actual Weyl convention; no subprincipal correction is inserted into a₀.

The Gaussian integral contributes e^{−iπm/4}N^{−m/2}/√det K. P7's e^{iπm/4}√D_m N^{m/2}2⁻ᵐ cancels its phase and N powers. Since ∏a₀=2ᵐ√(∏b), the remaining factor is

√D_m √(∏b)/√det K=√(D_m/|det(I−DF^m)|).

No residual branch multiplicity, power of 2, or factor of 2π remains.

## 2. The actual physical conjugacy and its C³ perturbation input

For s=0, the bounded stationary correction u_j(z)=u(S^jz) and the Euler equation imply Fχ=χS with W4's momentum convention. Integer gluing gives a lift χ̃(z)=z+r(z), where r is bounded and periodic. The exact lift conjugacy follows by continuity and the near-identity normalization (and differences would cancel any common integer constant).

If χz=χw on the torus, choose corresponding lifts with χ̃z=χ̃w. Iterating the lift relation in both directions makes S^j(z−w) bounded for every integer j, since r is bounded. Hyperbolicity forces z=w. The continuous map χ is homotopic to the identity, so degree one gives surjectivity. This proves the homeomorphism claim without a differentiability assumption on χ.

The actual ODE sources bound the characteristic vector field through order three by 10¹². Its sign reversal has the same bounds. The variational equations give C³ difference from the identity O(10¹²τ), with harmless fixed constants, at the literal τ. Composing with S or S⁻¹ and changing by fixed cat eigen-coordinates costs only fixed powers of matrices of norm below 10. Consequently 10³⁰τ=δ=10⁻⁵⁰ safely bounds both F−diag(λ,λ⁻¹) and its inverse counterpart in C³. This is a global real bound because the nonlinear remainders and all coefficient derivatives are periodic.

## 3. Actual C^{1,1/2} graph transform

In fixed eigen-coordinates write DF=[[a,b],[c,d]], H=F⁻¹, and

M(x,t)=(c(x)+d(x)t)/(a(x)+b(x)t),  Tv=M(Hx,v(Hx)).

Take R=10⁸δ. Throughout |t|≤R, a+bt>5.8, and area preservation gives

M_t=1/(a+bt)²<0.03,  |M_tt|<δ.

Every nonconstant coefficient derivative through order two is bounded by δ. Two direct differentiations of the quotient bound the needed M_x, M_xx, M_xt and M_xxt by a fixed constant times δ; even 10⁴δ is ample. Only a supremum bound on M_xxt is needed: it controls the Hölder difference of M_xt. No unprovided Hölder bound on the highest spatial derivative is being assumed.

Also ||DH||≤6 and ||D²H||=O(δ). The highest Hölder term in the difference derivative is bounded by

0.03·6^{3/2}[D(v₁−v₂)]_{1/2}<0.441[D(v₁−v₂)]_{1/2}.

Terms involving variation of M_t, M_x, or DH have a factor O(δ), or M_tt times the small C¹ ball radius. Standard product and composition inequalities bound their sum by 10¹²δ times the full C^{1,1/2} difference norm. One can use either the maximum of the three component norms or their sum: the constant-map part acts diagonally on the derivative orders and does not acquire a factor of three merely from changing these norms.

The useful exact identity

Tv−Tw=((v−w)∘H)/[((a+bv)(a+bw))∘H]

provides a second direct way to see that no nonlinear composition derivative loss occurs. The base map H is fixed.

Thus the contraction constant is below 0.441+10¹²δ<1/2. The forcing norm is at most 10⁶δ, and 10⁶δ+R/2<R. The closed C^{1,1/2} ball is invariant and complete, so the transform has the asserted unique fixed point. Iterating the inverse map with interchanged coordinates gives the stable field. Cone invariance and expansion identify these invariant fields with the actual hyperbolic bundles.

Converting an unstable graph vector (1,v) to physical coordinates gives slope

(1−v)/(√2(1+v)).

The denominator is uniformly separated from zero, so the physical C^{1,1/2} bound 10¹⁰δ is safe. The stable calculation is identical. This proves regularity of the fields, not of χ and not automatically of an arbitrarily long holonomy map.

## 4. Finite lifted leaf graphs and the physical phase

Let v_± be the physical slope fields and write a lifted leaf through (q,p) in moving coordinates as

w_±(t;q,p)=p_±(q+t;(q,p)),  ∂_t w_±=v_±(q+t,w_±),  w_±(0)=p.

On |t|≤2, v_± is C^{1,1/2}-close to ±1/√2. For example, differentiating with respect to the initial coordinates gives

∂_t(w_±)_q=(v_±)_q+(v_±)_p(w_±)_q,  (w_±)_q(0)=0,
∂_t(w_±)_p=(v_±)_p(w_±)_p,  (w_±)_p(0)=1.

Gronwall on this fixed interval bounds these derivatives and their differences from the constant-field values. Taking half-Hölder differences in the same integral equations supplies the C^{1,1/2} dependence on (t,q,p). Since the derivative perturbations are at most 10¹⁰δ, the candidate's bound 10²²δ is very conservative. Returning to Q=q+t is a fixed linear parameter change.

The difference w_u−w_s has t derivative √2+O(δ). Hence the equation w_u−w_s=s has one root near t=s/√2, for every 0≤s≤1, safely inside |t|<2. Differentiation of this scalar equation gives the initial-point derivatives of t_s, and the same product/reciprocal Hölder estimates give the stated 10²⁵δ norm bound for Q_s=q+t_s. This is a finite implicit-function argument.

The infinite source-s stationary orbit differs exponentially from the zero-source orbit in the past and future. The weighted inverse bounds give this in positions; evaluating the smooth generating derivatives gives it also in momenta. The past segment therefore belongs to the lifted unstable leaf through χz, the future segment to its stable leaf. At the distinguished site the Euler equation is p⁻−p⁺=s. The already selected root is consequently exactly Q_s(χz), not merely a perturbative approximation.

In the original stationary coordinates the central position is

q_label+s/√2+u_{s,0}(z).

Integrating in s proves

∫₀¹Q_s(χz)ds=q_label+1/(2√2)+D_∞(z).

This is W7's exact identity B=H_τ∘χ⁻¹. The C^{1,1/2} norm bound follows from the finite leaf calculation, not by differentiating χ⁻¹. In particular

∂q B≥1−10²⁵δ=1−10⁻²⁵>1/2.

At s=1 the momentum discrepancy is exactly the integer one, so the broken lifted orbit projects to an actual torus orbit. Its cat source has forward displacement λ⁻ʲd and the past congruent representatives λ^{−|j|}(1/√2,+1/2). Integer gluing and uniqueness of the bounded correction identify it with χ(z+d). Choosing the stable-side momentum therefore gives exactly W8. Equivalently, it is the selected stable/unstable intersection prescribed by χR_dχ⁻¹.

The formula using Q₁ and the finite stable leaf graph is C^{1,1/2} and close to (q,p)↦(q+1/√2,p−1/2). Its derivative is close to the identity. Thus its area Jacobian J_d is positive, C^{0,1/2}, and uniformly close to one. The conjugacy formula supplies global invertibility. No global-all-time derivative bound for χ or its leaf parametrizations is used.

## 5. Finite periodic weights and the limiting Jacobian ratio

In the P8 autocorrelation, the product of leading coefficients is

D_m√(ρ_m(z+d_m)ρ_m(z)).

Its D_m cancels exactly against the normalized character transform. W9 follows, including its q-character and the constant Q_m(d_m). There is neither an extra factor D_m nor division by the positive mass Z_m.

The unstable bundle is orientable and its one-step orientation is preserved by the small perturbation. The periodic unstable multiplier is therefore positive, Λ_m=exp(S_mφ)>1, and the stable multiplier is Λ_m⁻¹. Hence

|det(I−DF^m)|=Λ_m(1−Λ_m⁻¹)²,

which gives W10 exactly.

Put y=Ψ_dx and a=φ∘χ. Since a is Hölder, its homoclinic difference series is absolutely and uniformly convergent. On a centered m-window the error from replacing d_m by d is at most C m λ^{−αm/2}, and the omitted tails have the same exponential scale without the factor m. Indeed d_m−d=O(λ⁻ᵐ), ||S^j||≤Cλ^{|j|}, and homoclinic representatives decay like λ^{−|j|}. W10's denominator corrections are uniformly exponential as well. It follows that

ρ_m(z+d_m)/ρ_m(z) → exp(−Σ_{j∈Z}[φ(F^jy)−φ(F^jx)])

uniformly on the periodic labels. The square-root factor in W9 tends to the square root of this limit.

Here is the determinant calculation, including the often-missed angle factor. Let e_u,e_s be oriented unit bundle fields, let θ(x)=|det(e_u(x),e_s(x))|, and let ψ=log J^sF. Area preservation implies

φ(x)+ψ(x)=log θ(x)−log θ(Fx).

Because Ψ_d preserves both foliations, write its positive directional expansion factors as h_u(x) and h_s(x). Stable holonomy differentiated along unstable leaves yields

h_u(x)=exp(−Σ_{j≥0}[φ(F^jy)−φ(F^jx)]).

For the stable direction, differentiating unstable holonomy and iterating backward yields

h_s(x)=exp(Σ_{j<0}[ψ(F^jy)−ψ(F^jx)])
      =exp(−Σ_{j<0}[φ(F^jy)−φ(F^jx)]) θ(x)/θ(y).

These products can be derived directly from F^nΨ_dF^{−n}=χR_{S^nd}χ⁻¹. In the relevant forward or backward direction the homoclinic displacement tends to zero, so the corresponding terminal local holonomy derivative tends to one. This last fact follows from the C¹ dependence of the bounded local leaf ODEs. It does not assume a uniform derivative estimate for long global holonomies. Absolute convergence follows from the same homoclinic Hölder estimate used above.

The determinant in physical area coordinates is

J_d(x)=h_u(x)h_s(x) θ(y)/θ(x).

The two angle factors cancel, leaving exactly W11 with its negative sign. There is no surviving metric-dependent density factor. The ratio is J_d, not J_d⁻¹; the paired geometric mean is √J_d, not J_d.

For an additional check on the constant phase, Q_m(d_m)=q(d_m)/2 and q(d_m)=(1/√2)(1+λ⁻ᵐ)/(1−λ⁻ᵐ). Its limit is 1/(2√2). This is the constant in W12, with error O(Nλ⁻ᵐ) after exponentiation.

## 6. The half-density integral and exact scope of EQ

Since Ψ_d is a degree-one diffeomorphism with positive Jacobian,

∫ J_d(x)|f(Ψ_dx)|²dx=∫|f(y)|²dy.

This proves the stated half-density interpretation. It does not permit dropping √J_d.

The lift B satisfies B(q+1,p)=B(q,p)+1 and is periodic in p. For each p, t=B(q,p) is a degree-one C^{1,1/2} circle diffeomorphism with derivative at least 1/2. The transformed density is

r_p(t)=√J_d(q(t,p),p)/B_q(q(t,p),p).

It is periodic and has a uniform C^{0,1/2} bound. Integrating it in p preserves that bound. Translating t by 1/(2N) changes e(Nt) by −1, so twice its N-th Fourier coefficient is bounded by the half-Hölder modulus at that shift. This proves W13 for every positive integer N. The constant phase in A has modulus one and does not affect the bound.

The prior equilibrium identification of physical area uses the exact inherited entropy/pressure input recorded in `nonlinear_bracket_pressure.md`, its dated review, and the external-dependency registry. It does not identify χ⁻¹_*area with label Haar, and it does not supply a norm-uniform periodic-point estimate.

If EQ holds for a Hölder exponent at most 1/2, applying it to a_N=√J_d e(NA) is legitimate: its norm grows only polynomially in N. EQ applied to 1 also gives the needed uniform bound on Σρ_m when replacing finite ratio and defect factors by their limiting values. Combining those replacements would give the stated O(N^C e^{−c'm}) finite-to-integral error. This is an explicitly conditional implication. Mere weak convergence would not imply it. The new weighted-periodic source candidate was not used as a proved input here.

## 7. Exact finite-h factors and stopping boundary

The rotated integral divided by its full Gaussian prefactor is

P_{G_z}(B_h)·Z_{m,h,J}(z),

because Z is an expectation conditioned on B_h. Including the actual leading factor gives W14. Multiplying two such coefficients gives exactly W15, including both Gaussian probabilities and the complex conjugation of the unshifted Z. The original finite-order amplitudes use (2πh)^ℓ throughout.

The accepted first-loop theorem by itself supplies only a per-class approximation to Z. This review makes no absolute-summability inference over the full orbit or displacement family. A separate quantum argument may exploit localized first-loop differences inside one normalized weighted autocorrelation, but that is not an assertion made or needed by the frozen physical dictionary.

There is no missing load-bearing implication in W1–W15 at their stated scope. The next independent leaf is EQ for the norm and measure asserted, plus any separate treatment of W15. Even success there would control one selected unit-pulse coefficient, not the original unnormalized outer sum over all displacements.

## Source binding and computation record

All eleven entries in `physical_quantum_sources.json` matched their stated hashes. `source_binding.json` records those checks and the separately read graph-transform, pairing, locality, and external-input records. The accepted H1–H10 review was read as an inherited scope boundary; the stationary and transport sources needed above were also inspected directly.

Commands executed:

- `python3 /workspace/shared/bgs_paired_box_cancellation/check_hill_weight.py` → `hill_replay.json`: 84 exact rational W1–W2 cases, m=1,…,12.
- `python3 /workspace/shared/bgs_physical_weight_review/independent_checks.py` → `independent_checks.json`: symbolic m=1 twisted identity, 40 independent signed rational twisted identities for m=2,…,9, and exact rational contraction/phase margins.

The independent arrays intentionally include signed coefficients to test the general algebra beyond the candidate's positive physical arrays. This is not a physical counterexample search. The all-m identity, bundle regularity, finite-leaf ODE dependence, and Jacobian products are proved mathematically above; finite checks do not establish them or EQ. No floating-point evaluation at τ=10⁻⁸⁰ was used as evidence.
