# Exact ordinary centering of the completed compact source

7 October 2026. Independent reconstruction of the frozen centering candidate; new finite-N consequences are author derivations with self-review. No canonical file is changed. The source snapshot and exact inputs are pinned in `input_manifest.json`.

## Claim and verdict

**Primary verdict on the candidate: proved as written**, on its intended almost-everywhere finite-N domain, with the precise delta/coarea normalization supplied below. The candidate does not need a missing factor of π, an extra rotation quotient, or a super-Jacobian. The result holds for every odd N≥3 and each of the 4^N compact coefficient sectors of the accepted source identity. The source parameters remain in |a|,|b|<1, with arbitrary complex c,d; fixed-N continuation of the compact expression is also valid on |ab|<1, without reinterpreting that continuation as a raw phase integral on another component.

There is also a new measurable consequence for the **actual completed signed source representation**: an explicit finite-N error bound when its conformal-center integral is cut off at |p|≤1−ε. This is not just a coordinate identity, but it is not a dimension-uniform microscopic or normalized tail theorem. All coefficient norms, all signs and all sectors remain present.

## 1. Normalized objects

Write D={z∈C:|z|<1} and T={z∈C:|z|=1}. Fix a labelled boundary set B⊆{1,…,N}, k=|B|, and let

X_B = T^B × D^(Bᶜ),
μ_B(dz) = ∏_(i∈B) dθ_i/(2π) ∏_(i∉B) d²z_i/π,
n_B = dim_R X_B = 2N−k.

All coordinates are labelled; there is no permutation quotient. The disk factors are strictly interior. Taking their closures when bounding continuous coefficient functions does not add a surface term to their area integrals.

For p∈D set

m_p(z)=(z−p)/(1−p̄z),       ψ_p(y)=(p+y)/(1+p̄y).

Here p is a collective ordinary complex coordinate and has no relation to the source parameter a. The centered BB coordinates are y_i. The commuting fermion-flavor chart coordinates in the original supermatrix are different variables and are not being renamed y_i.

A tuple z is stable if every point of T occurs among its coordinates with multiplicity strictly less than N/2. Define X_B^st by this condition. For N≥3, μ_B(X_B\X_B^st)=0: failure requires repeated circle coordinates, contained in a finite union of pair-equality sets of product Haar measure zero. Disk coordinates cannot equal a boundary point. If k<N/2, every point of X_B is stable.

For odd N, put

Σ_B={y∈X_B:Σ_i y_i=0},        Δ(y)=N²−|Σ_i y_i²|².

All points of Σ_B are automatically stable. Indeed if h>N/2 coordinates equal v∈T, the real part of v̄Σy is at least h−(N−h)>0. For odd N there is no h=N/2 equality case.

The centering map is a diffeomorphism

Φ_B : D × Σ_B → X_B^st,       (p,y)↦(ψ_p(y_i))_i.             (1)

The slice has real dimension n_B−2=2N−k−2. Its rotation remains a genuine shape coordinate; no additional U(1) division is made.

## 2. Existence, uniqueness and the exact exceptional set

Consider the real potential

F_z(p)=Σ_i log|1−p̄z_i|²−N log(1−|p|²).

### Properness on the stable domain

Fix z. Near a boundary point η occurring h times, all factors from coordinates unequal to η are bounded below by a positive constant, while |1−p̄η|≥1−|p|. Therefore, writing δ=1−|p|,

F_z(p) ≥ (N−2h) log(1/δ)−C_z

in a sufficiently small neighborhood of η. Away from the finitely many occupied boundary points, every numerator factor is bounded below, giving the same estimate with h=0. The finite cover proves F_z→+∞ as |p|→1 whenever h<N/2 everywhere. This controls tangential approaches as well as radial ones.

The covariance identity

F_(m_b z)(m_b p)=F_z(p)+N log(1−|b|²)−Σ_i log|1−b̄z_i|²

is an elementary consequence of the disk Möbius identity, and its added term is independent of p. Rotations give the analogous exact covariance.

At p=0 along the geodesic p(t)=e^(iθ)tanh t,

d²F_z(p(t))/dt² at t=0 = 2Σ_i[1−Re(e^(−2iθ)z_i²)].           (2)

Every summand is nonnegative on the closed disk. Equality requires every coordinate to be a boundary point in the same antipodal pair ±e^(iθ). The covariance transfers this criterion to every point of every geodesic. A stable tuple cannot have all coordinates in such a pair: one of the two multiplicities would be at least N/2. Thus F_z is strictly geodesically convex on D. Properness gives a minimizer and strict convexity gives uniqueness.

Wirtinger differentiation gives

∂_(p̄) F_z(p)=−Σ_i m_p(z_i)/(1−|p|²).

The unique minimizer therefore is exactly the unique center p(z) satisfying Σm_p(z_i)=0.

### Classification at and beyond the multiplicity threshold

An interior center cannot exist if any boundary multiplicity h>N/2, by the same real-projection argument in centered coordinates. If h=N/2, that argument can vanish only if every other coordinate is the opposite boundary point after transformation. Hence the only unstable tuples admitting centers consist of two distinct boundary points, each with multiplicity N/2. Their centers form the disk geodesic joining those points, and uniqueness fails. This equality case occurs only at even N.

Consequently stability is the precise domain for a unique interior center, not merely a sufficient almost-everywhere condition.

### N=1 and N=2

- N=1, disk: p=z_1, y_1=0. The ordinary formula remains valid.
- N=1, circle: no interior center.
- N=2, two disks: a unique center for every tuple, including coincident points.
- N=2, one circle and one strict disk: no interior center; their transformed moduli cannot cancel.
- N=2, two distinct circles: a one-parameter family of centers; the centered antipodal slice is singular for the two-dimensional sum map. Identical circle points have no center.

Thus the complete N=1 and N=2 compact sources must retain their non-centerable sectors in the original compact form. The odd-N≥3 theorem has no such omitted positive-measure stratum.

## 3. Uniform nondegeneracy at odd N

For every odd N and every centered tuple with |y_i|≤1,

|Σ_i y_i²|≤N−1,        Δ(y)≥2N−1.                            (3)

Proof: rotate all y_i so that Σy_i² is nonnegative real, and write y_i=x_i+it_i. Then Σx_i=0, |x_i|≤1, and

|Σ y_i²|=Σx_i²−Σt_i²≤Σx_i².

The convex function Σx_i² attains its maximum on a vertex of {x∈[−1,1]^N:Σx=0}. At a vertex at least N−1 coordinates are endpoints; otherwise two interior coordinates can be perturbed oppositely. Because N−1 is even, their sum is an even integer, and the remaining coordinate in [−1,1] must be zero. Thus the maximum is N−1. The argument also covers N=1.

The bound is sharp on the closed centered polydisk, at (1,−1,…,1,−1,0). In strict all-disk strata it can be approached by radial contraction. No assertion is made that it is sharp within each fixed boundary stratum.

This quantitative fact rules out a hidden singular Faddeev–Popov factor anywhere on an odd-N slice. It is stronger than simply excluding a null set after centering.

## 4. The delta measure and both distinct Jacobians

Use the ordinary Euclidean delta on C=R²:

∫_(R²) δ²(u) h(u) d²u=h(0).

The expression δ²(Σy_i) μ_B(dy) is shorthand for its coarea measure on Σ_B. Let dH^(n_B−2) be Euclidean induced Hausdorff measure, where each circle has its usual arc-length metric. Then

δ²(Σy_i) μ_B(dy)
 = [(2π)^k π^(N−k)]^(−1) dH^(n_B−2)(y)/J_B(y),               (4)

where

J_B(y)=½√((2N−k)²−|Σ_(i∈B)y_i²|²).                         (5)

Indeed a disk tangent contributes I₂ to DS·DSᵀ, and a circle tangent contributes (iy_i)(iy_i)ᵀ in real coordinates. Thus DS·DSᵀ=(N−k)I₂+Σ_(i∈B)t_i t_iᵀ, whose determinant is the displayed square. This calculation proves regularity when there is a disk factor. If k=N, J_B=√Δ/2, positive by (3). More quantitatively,

J_B²≥N(N−k) when k<N;        J_B²≥(2N−1)/4 when k=N.          (6)

The coarea factor J_B is **not** the gauge factor Δ. Confusing them would change the measure.

Now hold the original z fixed and differentiate T_z(p)=Σm_p(z_i) at its center. Writing y_i=m_p(z_i), direct differentiation gives

D_p T_z[dp]=[−N dp+(Σy_i²)d p̄]/(1−|p|²).

Therefore the positive real determinant is

|det_R D_p T_z|=Δ(y)/(1−|p|²)².                              (7)

It is nonsingular by (3), so p(z) is smooth by the real implicit-function theorem. This proves smoothness of the inverse in (1).

At fixed p, the map ψ_p has Jacobian

j_i(p,y_i)= (1−|p|²)/|1+p̄y_i|²     for i∈B,
j_i(p,y_i)= (1−|p|²)²/|1+p̄y_i|⁴   for i∉B.                 (8)

The first is a positive circle arc-length derivative; the second is the modulus square of a holomorphic derivative. The constants 1/(2π) and 1/π in the original measures are retained.

## 5. Exact finite-N formula and its proof

For odd N≥3, every B, and every nonnegative measurable g on X_B,

∫_(X_B) g(z) μ_B(dz)
 =∫_D d²p ∫_(X_B) δ²(Σy_i) g(ψ_p(y)) W_B(p,y) μ_B(dy),      (9)

where

W_B(p,y)= Δ(y)(1−|p|²)^(2N−k−2)
 /[∏_(i∉B)|1+p̄y_i|⁴ ∏_(i∈B)|1+p̄y_i|²].                 (10)

Both sides may be infinite for nonnegative g. If g∈L¹(μ_B), the equality holds absolutely, separately for its real and imaginary parts. In particular g≡1 makes the right side exactly one.

To prove it, on the stable domain insert the ordinary change-of-variables identity

1=∫_D δ²(T_z(p)) |det_R D_pT_z| d²p.

There is exactly one zero, of positive determinant, by Sections 2–4. In local coordinates this is simply the two-dimensional delta formula, so there is no orbit-volume ambiguity. A partition of unity and an exhaustion by compact sets justify the noncompact identity; nonnegative integrands allow monotone convergence. At each fixed p, substitute z_i=ψ_p(y_i), using (8). Then T_z(p)=Σy_i and (7) multiplies the product of (8), producing exactly (10). Formula (4) is the resulting delta measure. Null unstable configurations on the original side do not contribute. This is also a direct proof of the corresponding coarea change of variables, rather than an appeal to a formal gauge integral.

For k=0 one may eliminate y_N=−Σ_(i<N)y_i. Integrating its Euclidean delta removes d²y_N with factor one, but retains its measure normalization 1/π. Thus the prefactor is π^(−N), not π^(−N+1). The remaining Jacobian is exactly the accepted interior Jacobian. At N=1 this gives d²p/π, as it must.

## 6. Application to the completed signed source

Let F be the inverse Berezinian in the accepted compact identity. For each site choose one of four local operations:

- circle: evaluate its body at its commuting fermion coordinates zero;
- circle: take the mixed derivative in those two commuting fermion coordinates, then set them to zero;
- disk: extract its γβ coefficient, then set the commuting fermion coordinates to zero;
- disk: extract its αδ coefficient, then set the commuting fermion coordinates to zero.

Use the fixed local odd order γ,β,α,δ and the accepted tensor convention. Denote the resulting ordinary coefficient function by g_σ(z;a,b,c,d), the set of its circle choices by B_σ, and η_σ=(−1)^(N−|B_σ|), the explicit signs from the compact functional. Signs already present within g_σ are not altered. Then the accepted theorem says

G_U(a,b;c,d)=Σ_(σ∈{0,2,γβ,αδ}^N) η_σ ∫g_σ(z;a,b,c,d) μ_(B_σ)(dz).    (11)

All odd extraction and all commuting-fermion derivatives are taken **before** setting their variables to zero, and before applying (9) to the resulting coefficient functions. No fermion or odd coordinate is being centered. There is no claim that (10) is a super-Berezinian or a transformed invariant supermeasure.

The accepted theorem proves that, at fixed N, g_σ and every fixed source derivative extend continuously to the closed BB polydisk, and are bounded uniformly for source parameters in a compact subset K of |a|,|b|<1, c,d∈C. One can also use compact subsets of |ab|<1 for the continued compact expression. This follows from the BB inverse (I−ab Z̄UZU*)^(−1), its norm bound (1−|ab|)^(−1), and finiteness of the extracted odd algebra and polynomial numerator-source dependence.

Apply (9) to each g_σ in (11). The transformed coefficient, every source factor and its explicit sector sign are retained. The resulting 4^N-term expression is an exact centered representation of the completed source. The Jacobian and center do not depend on source parameters, so fixed-N locally uniform source differentiation remains valid. This includes the matched mixed numerator derivative producing the Abel pair observable, but gives no new estimate of its large-N limit by itself.

## 7. An actual finite-N center-cutoff estimate

This section is new relative to the candidate. It concerns the complete signed expression (11), not the auxiliary positive scalar integral from the body-coercivity notes.

Let N=2m−1 be odd, N≥3, 0<ε≤1/(N+3), and τ=(N+3)ε. For z∈X_B^st let p(z) be its center. Define

P_(N,k)(ε)=μ_B{|p(z)|>1−ε}.

It depends only on N,k. Define the explicit polynomial

Q_(N,k)(τ)= Σ_(j=max(0,m−N+k))^(min(k,m)) binom(k,j)binom(N−k,m−j) A_(m,j) τ^(N−j),

where A_(m,0)=2·4^(m−1), and A_(m,j)=4^(m−j) for j≥1. Then

P_(N,k)(ε)≤min{1,Q_(N,k)((N+3)ε)}.                           (12)

In particular P_(N,k)(ε)=O_(N,k)(ε^(N−min(k,m))) as ε↓0. The worst exponent among the compact strata is m−1=(N−1)/2.

### Geometric cap lemma

Write p=rη, |η|=1, δ=1−r. After a rotation take η=1 and set y_i=m_r(z_i). If |z_i−1|>(N+3)δ, then

|y_i+1|=δ|1+z_i|/|1−rz_i| ≤2δ/(|1−z_i|−δ)<2/(N+2),

so Re y_i<−1+2/(N+2). Every other y_i has Re y_i≤1. If at most m−1 coordinates lie in the cap |z_i−η|≤(N+3)δ, their real sum is at most

(m−1)−m[1−2/(N+2)] =−1+(N+1)/(N+2)<0,

contradicting Σy_i=0. Thus at least m original coordinates lie in that cap. When |p|>1−ε they lie in a cap of radius τ.

### Product-measure estimate without a hidden angular covering factor

Choose any m labels in the cap, of which j are circles. If j≥1, fix one of those circle labels as anchor. Each other selected circle is within chordal distance 2τ of the anchor and has Haar probability

2 arcsin(τ)/π≤τ,       0≤τ≤1.

Each selected disk point is within distance 2τ and has normalized-area probability at most 4τ². Conditional independence, uniformly in the anchor, gives 4^(m−j)τ^(2m−j−1)=A_(m,j)τ^(N−j).

If j=0, select one disk anchor. It must lie in the boundary shell 1−|z|≤τ, of probability 2τ−τ²≤2τ. Every other selected disk is within distance 2τ of it, giving 2·4^(m−1)τ^(2m−1). Summing over the possible labelled subsets proves (12). This is a union bound, not a disjoint partition.

### Completed-source truncation

Let G_U^[ε] be (11) with each ordinary integral restricted to |p(z)|≤1−ε, equivalently its centered representation restricted to |p|≤1−ε. For a fixed source derivative multi-index ν and compact source set K, put

M_(σ,ν,K)=sup_(z in closed polydisk, sources in K)|∂^ν g_σ(z;sources)|<∞.

Then the exact, effective-in-these-norms inequality is

sup_K |∂^ν(G_U−G_U^[ε])|
 ≤Σ_σ M_(σ,ν,K) min{1,Q_(N,|B_σ|)((N+3)ε)}.                 (13)

This proves a quantitative cutoff approximation for the **complete signed source and its fixed source derivatives**. In particular it is O_(N,U,ν,K)(ε^((N−1)/2)). If coefficient norms are explicitly bounded, (13) gives an explicit numerical truncation error. The inequality does not assume that the signed summands form a positive probability density, nor that their absolute sum is bounded uniformly in N.

### A crude explicit coefficient majorant

The norms in (13) need not remain implicit. For a compact source set K put q₀=sup_K|ab|<1, u₀=sup_K|bc|, v₀=sup_K|ad| and r₀=sup_K|cd|. Set

h=(1−q₀)^(−1),
H=h Σ_(j=0)^N (u₀N²h)^j,
L=1+(v₀+r₀)N²+(q₀N+u₀N²)H(v₀N+r₀N²),
M_N(K)=(N!)²(HL)^N.                                         (16)

Then M_(σ,0,K)≤M_N(K), simultaneously for all σ and all U∈U(N).

Here is a direct finite algebra proof. In site-block notation write the original local matrix as Z_super=[[Z,Α],[Β,V]], Ztilde_super=[[Z̄,Γ],[Δ,−V̄]], with each capital letter diagonal and Γ,Β,Α,Δ the corresponding odd variables. The four blocks of I−Ztilde_super diag(aU,cU) Z_super diag(bU*,dU*) are

A=I−ab Z̄UZU*−bc ΓUΒU*,
B=−ad Z̄UΑU*−cd ΓUVU*,
C=−ab ΔUZU*+bc V̄UΒU*,
D=I−ad ΔUΑU*+cd V̄UVU*.

Work in the Grassmann algebra, tensored with the finite commuting algebra in which each V_i² and V̄_i² is zero. This quotient is exact for the selected coefficients: a higher power of any commuting fermion coordinate cannot contribute to a functional that differentiates that coordinate at most once and then evaluates at zero. All variables are still extracted before being set to zero.

For a matrix over this algebra, take the sum over coefficient monomials of the matrix operator norm. This norm is submultiplicative, including after the quotient. Every diagonal odd or formal commuting field has norm N; Z and Z̄ have norm at most one. The body inverse A₀^(−1)=(I−ab Z̄UZU*)^(−1) has norm at most h. The perturbation bc ΓUΒU* has norm at most u₀N² and uses only 2N odd generators, so its body-resolvent Neumann series stops after power N. Consequently ||A^(−1)||≤H. The displayed blocks give ||D−CA^(−1)B||≤L.

The BB-pivot identity gives F=det(D−CA^(−1)B)det(A^(−1)). Its two determinants are over even, hence commuting, entries. The Leibniz formula bounds their coefficient norms by N! L^N and N! H^N, respectively. Every selected coefficient is bounded by their product, proving (16). This majorant is deliberately crude but completely explicit; it uses no source cancellation or body coercivity.

If the closed complex polydisc neighborhood K_δ of radius δ about K remains inside the source domain, Cauchy's estimate gives

M_(σ,ν,K)≤ν! δ^(−|ν|) M_N(K_δ).

Since there are 4^N sectors and at most binom(N,m) subsets in the cap argument, one convenient fully explicit bound is

sup_K|∂^ν(G_U−G_U^[ε])|
 ≤4^N ν!δ^(−|ν|) M_N(K_δ)
   ·min{1, 2·4^(m−1) binom(N,m) [(N+3)ε]^(m−1)}.             (17)

For ν=0 one may use M_N(K) directly and omit the δ factors. The sharper stratum-dependent inequality remains (13). Bound (17) proves an effective fixed-N approximation of the actual complete source and its derivatives, with all constants specified.

At microscopic sources ab→1 as N grows, both the coefficient norms and the sector count can grow. Formula (13) has no hidden normalization lower bound, no uniform-in-N conclusion and no implication that a prescribed ε_N makes the normalized microscopic error vanish. Obtaining those controls, or exploiting signed cancellation instead of the absolute coefficient sum, is the missing next implication.

## 8. Independent small-N normalization controls

The exact checker `checks/verify_centering.py` uses independently written ordinary differential/Jacobian algebra, not the source author's superalgebra checker.

### N=2, two disks

Set y=(u,−u), x=|p|² and t=|u|². After both normalized angular integrations, the claimed total mass becomes

∫_0^1∫_0^1 4(1−t²)(1−x)² (1+x²t²)/(1−x²t²)³ dx dt.

The angular identity comes from the nonnegative Fourier series of |1−xt e^(iθ)|^(−4). Expanding gives a nonnegative series whose n-th integrated term is

8(n+1)/[(2n+1)²(2n+3)²]
 =1/(2n+1)²−1/(2n+3)².

It telescopes to one. This catches both the missing disk normalization and a possible factor-four error in Δ.

### N=3, three circles

Every centered labelled unit triple is equilateral. There are two labelled components,

y=(e^(iφ),ωe^(iφ),ω²e^(iφ)) and (e^(iφ),ω²e^(iφ),ωe^(iφ)),

where ω=e^(2πi/3). Here Δ=9, J=3/2 and dH=√3 dφ on each component. Their distinct two orientations must both be counted. The product denominator is |1+(p̄e^(iφ))³|². Integrating φ exactly yields the center density with respect to d²p:

f_3(p)=3√3/[π²(1+|p|²+|p|⁴)].                              (14)

Its total mass is

(3√3/π)∫_0^1 dx/(1+x+x²)=1.

A direct angular-coordinate Jacobian gives 6√3(1−|p|²)/|1+(p̄e^(iφ))³|² on each component, independently confirming (4), (7), and (10). The checker also compares direct real Jacobians in all four N=3 strata k=0,1,2,3 at p=0 and at p=1/5+i/7, with exact rational/algebraic centered configurations.

At a=b=c=d=0 the actual completed source has only its all-circle body sector, equal to one for every U. Thus (14) gives an exact completed-source cutoff loss at N=3:

G_U−G_U^[ε]
 = (6/π)[π/3−arctan((2(1−ε)²+1)/√3)]
 = (2√3/π)ε+O(ε²).                                         (15)

This proves the worst-stratum exponent in (13) is already sharp at N=3. It also shows that a nontrivial collective-coordinate cutoff breaks the exact matched-source identity even at zero sources until its cutoff error is restored; it cannot be silently imposed as an exact gauge normalization.

The checker additionally validates the gauge derivative at N=1,2,3,5,7,9, the elementary odd-N vertex conclusion through N=31, and a factorized nonzero-source control for U=I_3. These bounded computations support normalization and signs; Sections 1–7 give the all-N proof.

## 9. Dependency and boundary against the accepted body theorem

The logical chain is:

1. accepted compact pair identity → bounded extracted ordinary coefficient functions with circle/disk supports;
2. elementary disk potential and multiplicity classification → unique almost-everywhere ordinary center;
3. ordinary implicit-function and coarea calculations → exact formula (9);
4. centered cap lemma plus product probabilities → genuine completed-source error bound (13).

The centering theorem imports no new external mathematical leaf. Its compact-source application inherits the already accepted four-family projector/source theorem, including the authenticated Zirnbauer convention and the exact boundary correction. It does not re-prove or strengthen those external-source claims.

The scalar/body coercivity inequality concerns S_U(z)=log|det(I−UZU*Z*)|−log det(I−ZZ*) on strictly interior centered fields. Its bare Möbius invariance agrees with the ordinary map above. However, compact sectors with k≥1 include boundary coordinates exactly; their H is infinite and their extracted source density is not exp(−S_U) times an already bounded positive factor. Applying the strict-interior inequality directly to them would discard the completed functional's load-bearing boundary contributions. Even the k=0 coefficients include Grassmann-generated inverse factors and signs not controlled by that inequality alone.

No super-coordinate theorem, super-Berezinian, positive full supermeasure, dimension-uniform absolute sector estimate, normalized large-N tail, balanced microscopic law, deterministic off-charge cancellation, higher-factorial statement, or BGS conclusion is obtained here.

**Next missing implication:** derive a uniform estimate for the actual signed, source-differentiated coefficient combination after this centering, including its boundary strata, strong enough at ab=e^(−2s/N) to compare the N^(−2)-normalized microscopic observable. Formula (13) isolates a well-defined finite-N collective-center cutoff error; it does not supply that uniform coefficient/cancellation estimate. The independent boundary/body synthesis can use (9), (3), and (13), but cannot replace its missing coefficient analysis by the ordinary scalar action bound.
