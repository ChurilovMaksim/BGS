# Quantitative exclusion of arithmetic translation algebras

**Proposed claim ID: BGS-FM-023.** Date: 6 October 2026.

**Status:** project analytic proof with independent internal review of the accepted quantitative derivation, portable exact coefficient/filter controls, and an editorial consolidation. No external referee certification, priority claim or analytic formalization. The independent review and source hashes are recorded in [the review](../../archive/record/arithmetic_translation_review_20261006.md).

The fixed-divisor assertion is a corollary of the stronger quantitative estimate, not a separately maintained theorem. It does not establish microscopic CUE comparison or a scalar full commutant.

## 0. Unchanged operator, conventions and prior inputs

For every odd N≥3, write h=2^(−1) modulo N and e_N(x)=exp(2πix/N). Keep exactly

(T_N(a,b)ψ)(x)=e_N(b(x+h a))ψ(x+a),
(M_N)_(xy)=N^(−1/2)e_N(−8^(−1)(3x²−2xy+3y²)),
U_N=exp(iτN A_N)M_N,   τ=10^(−80).

All modular inverses are modulo N. No parity or seven-path symmetry reduction is performed. Let W_N(a,b)=(−1)^(ab)T_N(a,b), and for smooth a(q,p) use

Op_N(a)=Σ_(k,l) a_hat(k,l) W_N(l,k).

The physical midpoint symbol of the unchanged generator A_N=Op_N(g) is

r(q)=(1−cos(14πq))(1+cos(2πq)),
g(q,p)=cos(14πq)+r(q)/10+r(q)sin(2πq)/100−1/10
       +r(q+1/2)cos(2πp−α)/100,
cos α=−3/5,   sin α=4/5.

The shift r(q+1/2) is essential. This exact dictionary and its finite Fourier coefficients belong to [FM-001](../fixed-map/fixed_model_symmetry_theorem.md). The classical kick map in the Q_N*Op(a)Q_N convention is Ψ=Φ_g^(−κ), κ=τ/(2π), with X_g=(g_p,−g_q).

All matrix norms on operators below use the Hilbert space with inner product ⟨X,Y⟩_N=N^(−1)Tr(X*Y), unless explicitly labeled as ordinary operator norms. Raw Weyl modes with distinct residues are exactly orthonormal. Direct substitution in the quadratic kernel gives

M_N T_N(v) M_N*=T_N(Sv),   S=[[3,4],[2,3]].

The proof reuses the quantitative kick Egorov mechanism of [FM-018](../fixed-map/frozen_operator_transfer_coercivity.md) and the overlap architecture of [FM-016](../fixed-map/egorov_overlap_rigidity.md); their needed estimates are derived in Section 5 below. Their mixing, channel-gap and classical centralizer theorems are not required. No auxiliary ensemble is substituted for U_N.

## 1. Theorem and exact range

Use the unchanged odd-dimensional U_N=Q_N M_N, Q_N=exp(iτN A_N), τ=10^(-80), A_N=Op_N(g), and κ=τ/(2π). For any odd d≥3 dividing N, let

E_(d,N)^0=span{T_N((N/d)v): v∈(Z/dZ)^2, v≠0},

and Π_(d,N)^0 its orthogonal projection in normalized Hilbert–Schmidt norm. The dimension is exactly m=d²−1, including when d and N/d are not coprime. No CRT factorization is assumed.

There exists C_τ>0, independent of N,d and grid labels, such that

||Π_(d,N)^0 Ad(U_N) Π_(d,N)^0|| ≤ min{1, C_τ (d^262/N)^(1/129)}.    (T)

Consequently, for d≤N^(1/524),

||Π_(d,N)^0 Ad(U_N) Π_(d,N)^0|| ≤ C_τ N^(−1/258),                 (T1)

and uniformly over X in this span with ||X||_N=1,

| ||U_N X U_N*−X||_N²−2 | ≤ 2 C_τ N^(−1/258).                   (T2)

More generally any exponent δ<1/262 gives decay N^(−(1−262δ)/129). Constants are enormous and no practical startup is provided. The limit is N→∞ at the literal fixed τ; no smallness assumption on τN appears.

This is an actual high-frequency operator-norm statement on the whole selected span. It excludes approximate spectral sectors or arithmetic cat orbit sums lying there at both the o(1/log N) and o(1/N) residual scales. It does not exclude structures outside these translation algebras or with faster-growing divisor.

### Fixed-divisor and sector corollaries

For every fixed odd d≥3, (T) tends to zero as N→∞ through odd multiples of d. Since Ad(M_N) permutes the d-grid labels, every normalized cat orbit sum in E_(d,N)^0 has residual tending to √2 for the actual U_N. In fact the convergence is uniform over all unit vectors in that span.

For the sector interpretation, let P_N be an orthogonal projection lying in span{I}⊕E_(d,N)^0. Require its centered part to be nonzero: equivalently 0<α_N=rank(P_N)/N<1. Then

X_N=(P_N−α_N I)/sqrt(α_N(1−α_N))

is a unit vector in E_(d,N)^0, and (T2) applies whenever d≤N^(1/524), or with the corresponding rate for any fixed δ<1/262. Consequently

||[U_N,P_N]||_N / sqrt(α_N(1−α_N)) → √2.

The projections 0 and I are excluded; their centered parts vanish and cannot be normalized. Projectors merely close to, rather than lying in, the indicated algebra require an additional approximation estimate. No assertion about arbitrary spectral projectors follows.

## 2. Quantitative analytic flow remainder, including translation distance

Let X=X_g=(g_p,−g_q) and Ψ=Φ_g^(−κ). Write its periodic lift as Ψ(x)=x+u(x).

The actual physical symbol has Fourier support |k|+|l|≤10, and FM-001's exact coefficient bound gives

Σ |g_hat(k,l)| (k²+l²) <52.

On the complex strip |Im q|,|Im p|≤ρ=1/100, each Fourier exponential is at most exp(2πρ·10)<2. Consequently

sup |X| <1000=:B_c,    sup ||DX|| <5000=:D_c.                 (2.1)

For example the bounds are at most 4π·52 and 8π²·52 respectively, and these are below the displayed integers. The mean contributes no vector field.

Starting in the half-strip, the complex flow over |t|≤|κ|<10^(−80) remains in the full strip: displacement ≤1000|κ|<ρ/2. The integral equation gives the holomorphic remainder

u=−κX+R,   ||R||_(half-strip)≤B_c D_c κ²/2=2,500,000 κ².       (2.2)

Cauchy's estimate on polydiscs of radius ρ/4 gives, at real points,

||∂^α R||_∞≤2,500,000 κ² α! 400^|α|.                         (2.3)

Choose the representative ξ∈[−1/2,1/2]^2 of a translation and put r=||ξ||_∞. Let D_q=(2π)^(-1)∂_q and D_p=(2π)^(-1)∂_p. Integrating one extra derivative along the real segment from x to x+ξ proves, for |α|≤16,

||D^α(R(·+ξ)−R)||_∞
≤2r · 2,500,000 κ² · 17! 400^17 / 6^16.                      (2.4)

The use of 2π>6 and of the maximum order 16 only enlarges this bound. In particular the error retains the essential factor r. It is not replaced by an O(κ²) error independent of translation distance.

The two degree-16 filters below have coefficient l1 norm less than 6. Their remainder after translation therefore has magnitude below

10^55 κ² r.                                                  (2.5)

This is an exact rational inequality checked in arithmetic_translation_exclusion.py. Since |κ|<10^(−80), it is less than 10^(−25)|κ|r. Thus the estimate remains smaller than the primitive |κ|/d signal for arbitrarily large d. There is no hidden restriction d≪1/κ.

For later finite-type upper bounds, the same argument through ordinary order 17 uses the 18th derivative and gives a remainder-difference bound below 10^70 κ²r. The finite Fourier support of X gives ||∂^α X||∞≤1000·100^|α| for |α|≤18. It follows that all derivatives of orders 1 through 17 of

[u_j(x+ξ)−u_j(x)]/(|κ|r)

are bounded by 10^40, for either component j. Only finiteness and uniformity of this generous bound are used.

## 3. Uniform finite type of translated displacement, order 16

The q frequencies are 0,±1,±2,±5,±6,±7,±8,±9 and p frequencies are 0,±1. Define

R_0(z)=∏_(n∈{2,5,6,7,8,9})(1+z²/n²),
P_q(z,w)=z(z−i)R_0(z)(1+w²),
P_p(z,w)=[∏_(n∈{1,2,5,6,7,8,9})(1+z²/n²)] w(w−i).

Both have total degree 16, no constant term, and coefficient l1 norm

6409325/1143072 <6.                                           (3.1)

On the entire displayed rectangular frequency set, P_q(D_q,D_p) isolates only (−1,0), with multiplier of modulus 4/3; P_p isolates only (0,−1), with multiplier of modulus 2. These exact polynomial identities are checked independently by rational symbolic evaluation.

The physical symbol's two primitive coefficient moduli are sqrt(101)/200 and 1/200. Consequently the corresponding nonzero components of X have primitive coefficient moduli at least π/100. If r=|ξ_q|, use P_q on the p-component of X; if r=|ξ_p|, use P_p on the q-component. The elementary inequality

|exp(2πit)−1|≥4|t|   for |t|≤1/2

and the smaller filter multiplier 4/3 show that the isolated leading flow term has magnitude at least

(4π/75)|κ|r > (4/25)|κ|r                                     (3.2)

at every point x. The error (2.5) is negligible compared with this explicit lower bound. The constant vector ξ−η and any integer vector are annihilated by either filter.

Therefore, for every ξ≠0, every η, and every integer n, one of the two scalar components

f(x)=ξ_j−η_j+u_j(x+ξ)−u_j(x)−n

has the pointwise finite-type bound

max_(1≤|α|≤16) |D^α f(x)| ≥ |κ|r/100    for all x.             (3.3)

The selected component depends on ξ, not on x,η,n. Since (2π)^|α|≥1, the same lower bound holds with ordinary mixed partial derivatives. After dividing f by |κ|r, its derivatives of orders 1,…,17 have a uniform bound, independent of the constant term involving η,n.

### Elementary sublevel consequence

If a real C^17 function on the two-torus has max_(1≤|α|≤16)|∂^α f|≥a>0 everywhere and derivatives of orders 1,…,17 bounded by A, then

area{|f|≤s} ≤ C_(a,A) s^(1/16),   0<s≤1.                      (3.4)

Here is a direct justification sufficient for this application. Polarization (or interpolation of the polynomial D_(e_1+t e_2)^j f at t=0,…,j) expresses each mixed order-j derivative as a fixed linear combination of directional order-j derivatives. For each j≤16 there is therefore a finite fixed set of directions and a uniform positive lower bound on at least one corresponding derivative. The C^17 upper bound makes that directional derivative stay above half its lower bound on a ball of a fixed radius. Cover the torus by finitely many sufficiently small convex patches. On each patch select the direction and order at its center; the lower bound holds throughout that patch. Slice along this direction and apply the one-dimensional divided-difference sublevel lemma to each interval. Integrating the slice bounds and summing over the uniformly bounded number of patches gives s^(1/j)≤s^(1/16). Constants depend on a,A, not on f's unrestricted additive constant.

Applying this argument to f/(|κ|r) gives

area{|f|≤ε} ≤ C min{1,(ε/(|κ|r))^(1/16)},                    (3.5)

with the convention that C can be enlarged so the bound holds also when ε/(|κ|r)>1.

## 4. Uniform coincidence-sublevel bound for the canonical maps

Let H_ξ=Ψ t_ξ Ψ^(−1) and compare it with t_η. Composing on the right with the area-preserving Ψ gives the lifted displacement

H_ξ(Ψ(x))−t_η(Ψ(x))=ξ−η+u(x+ξ)−u(x).

Take the four real embedding coordinates a_j=cos(2πq),sin(2πq),cos(2πp),sin(2πp), and put

b_j=a_j∘H_ξ−a_j∘t_η,    B(x)=(b_1(x),…,b_4(x)).

When |B|≤2ε, each torus coordinate displacement is within Cε of an integer. The scalar component selected in (3.3) therefore lies within Cε of one of a bounded number of integers. The number is bounded independently of ξ,η because representatives lie in [−1/2,1/2]^2 and ||u||∞ is tiny. Equation (3.5), area preservation, and r≥1/d for a nonzero d-grid translation imply

area{|B|≤2ε} ≤ C_τ min{1,(dε)^(1/16)}.                      (4.1)

All derivatives of H_ξ,t_η, hence of B, of any fixed required order are uniformly bounded in ξ,η. They are translations composed with the one fixed smooth map Ψ and its inverse. No compactness argument without a quantitative lower bound is being used: (2.4), (3.3) and (4.1) provide the shrinking-separation dependence.

## 5. Quantitative Egorov overlap: the square-root loss is retained

### 5.0. The actual kick estimate from exact Weyl multiplication

For integer Weyl labels v,w, with ω(v,w)=v_a w_b−v_b w_a, direct multiplication gives

W_N(v)W_N(w)=exp(πiω(v,w)/N) W_N(v+w).

All integer labels and their alias signs are retained. Write g=Σ_v c_v e_v with e_(a,b)(q,p)=exp(2πi(bq+ap)). For one mode,

iN[A_N,W_N(ν)]=−2N Σ_v c_v sin(πω(v,ν)/N) W_N(v+ν),
(X_g e_ν)/(2π)=−2π Σ_v c_v ω(v,ν)e_(v+ν).

The inequality |sin x−x|≤|x|³/6 and Fourier triangle inequality give

||iN[A_N,Op_N(a)]−Op_N(X_g a/(2π))||_op
≤ C_g N^(−2) Σ_ν |a_hat(ν)||ν|³
≤ C'_g N^(−2)||a||_(H5).

The last step is Cauchy–Schwarz; in two dimensions Σ |ν|^6(1+|ν|²)^(−5) converges. The finite support of g makes C_g finite. This estimate applies to every smooth a, without a Fourier-band restriction.

Integrate by Duhamel over the fixed real time interval between 0 and ±τ, comparing quantum conjugation by exp(itNA_N) with classical composition by Φ_g^(t/(2π)). Classical composition has bounded H5 norm on this fixed compact interval, by the chain rule, bounded derivatives of the fixed smooth flow, and its area-preserving change of variables. This gives

||Q_N*Op_N(a)Q_N−Op_N(a∘Ψ)||_op ≤ C_τ N^(−2)||a||_(H5),

and the inverse-kick version. This is the same actual-symbol estimate previously proved in FM-018(O7), reconstructed here so the rate used below has an explicit dependency. Translation Egorov is exact for every grid label, including labels of order N. Applying the kick estimate twice and exact translation Egorov between them gives the conjugated-translation estimate uniformly in the translation parameter. The intermediate symbols remain in a uniformly bounded H5 family.

### 5.1. Trace intertwining, cutoff and alias estimates

Let K_N=Q_N T_N((N/d)v)Q_N*, L_N=T_N((N/d)w), with v≠0. Their Egorov maps are H_ξ,t_η for the corresponding grid translations. Raw/midpoint scalar signs do not change these maps. Put D_N=K_N*L_N and t_N(c)=N^(−1)Tr(D_N Op_N(c)).

The actual finite-Fourier sine expansion in FM-018(O7) gives the Q_N Egorov remainder O(N^(−2)||a||_(H5)) at the fixed Hamiltonian time. Translation Egorov is exact, and composition by Ψ and translations has uniform H5 bounds. Thus, for the four fixed embedding coordinates,

Op(u_j)D_N−D_N Op(v_j)=O_op(N^(−2)),                         (5.1)

uniformly over grid labels and d, where u_j=a_j∘H_ξ, v_j=a_j∘t_η. It would also suffice to retain an O(N^(−1)) remainder here; the principal cutoff loss below is larger.

The exact Weyl multiplication phase and |e^(it)−1|≤|t| give

||Op(c)Op(b)−Op(cb)||_op
≤(C/N)(Σ_k |k||c_hat(k)|)(Σ_l |l||b_hat(l)|)
≤(C_b/N)||c||_(H3),                                         (5.2)

for b in a fixed uniformly smooth family. Aliases are retained in this inequality; no band truncation is implicit. Also ||Op(c)||_op≤C||c||_(H2).

Multiplying (5.1) by Op(c), taking cyclic normalized traces, and applying (5.2) gives

|t_N(c b_j)| ≤ C[N^(−1)||c||_(H3)+N^(−2)||c||_(H2)].         (5.3)

Choose a fixed smooth χ equal to one on [0,1], zero on [4,∞), with 0≤χ≤1. Set

χ_ε(x)=χ(|B(x)|²/ε²),
c_(j,ε)(x)=(1−χ_ε(x)) b_j(x)/|B(x)|²,

extending the second expression smoothly by zero near B=0. Then Σ_j c_(j,ε)b_j=1−χ_ε. For 0<ε≤1, chain rule bounds give

||χ_ε||_(C3)≤Cε^(−3),
||c_(j,ε)||_(C3)≤Cε^(−4),  ||c_(j,ε)||_(C2)≤Cε^(−3).       (5.4)

These are costs ε^(−s) and ε^(−s−1), respectively, not derivative-free cutoffs. To see the second, the derivatives of the smooth function z↦(1−χ(|z|²/ε²))z_j/|z|² are bounded by C_s ε^(−s−1); derivatives of B are uniformly bounded.

Equations (5.3)–(5.4) imply

|t_N(1−χ_ε)| ≤ C[N^(−1)ε^(−4)+N^(−2)ε^(−3)].              (5.5)

For the bad-set term use Hilbert–Schmidt Cauchy–Schwarz, not positivity of Weyl quantization:

|t_N(χ_ε)| ≤ ||Op_N(χ_ε)||_N.

Truncate χ_ε to the centered N×N Fourier box. Those Weyl modes are exactly orthonormal. The remaining Fourier tail has l1 norm at most C N^(−2)||χ_ε||_(H3), by weighted Cauchy–Schwarz in two dimensions. Consequently

||Op_N(χ_ε)||_N ≤ ||χ_ε||_L2+C N^(−2)||χ_ε||_(H3)
≤ area{|B|≤2ε}^(1/2)+C N^(−2)ε^(−3).                      (5.6)

**The square root of area is essential and is explicitly retained.** Combining (4.1), (5.5), (5.6) gives the uniform overlap bound

|N^(−1)Tr(K_N*L_N)|
≤ C_τ[(dε)^(1/32)+N^(−1)ε^(−4)+N^(−2)ε^(−3)].             (5.7)

No positive-quantization shortcut or area-instead-of-square-root substitution is made.

## 6. Optimization and the whole-span dimension loss

Choose

ε=N^(−32/129)d^(−1/129).

The first two terms in (5.7) become exactly the same scale:

(dε)^(1/32)=N^(−1/129)d^(4/129),
N^(−1)ε^(−4)=N^(−1/129)d^(4/129).

The remaining term N^(−2)ε^(−3)=N^(−162/129)d^(3/129) is smaller for N,d≥1. Hence each matrix overlap is bounded by

C_τ (d^4/N)^(1/129).                                        (6.1)

The d²−1 raw Weyl modes are exactly orthonormal, and Ad(M_N) merely permutes their labels by the invertible S modulo d. Therefore (6.1) bounds every entry of the compression matrix of Ad(U_N) in this basis. For an m×m matrix E, ||E||≤||E||_HS≤m max|E_ij|. Using m=d²−1≤d² gives

||Π_(d,N)^0 Ad(U_N) Π_(d,N)^0||
≤ C_τ d²·d^(4/129)N^(−1/129)
= C_τ (d^262/N)^(1/129).

This includes the full d²-dimensional loss; it does not mistake pointwise matrix-entry control for a dimension-free bound. Compression of a unitary superoperator also has norm at most one. This proves (T), and elementary exponent substitution gives (T1)–(T2).

## 7. Verification, provenance and exact boundaries

The portable standard-library verifier [arithmetic_translation_exclusion.py](../../computations/verification/arithmetic_translation_exclusion.py) independently assembles the physical Laurent symbol over rational Gaussian coefficients. It checks all 32 coefficients, centering/reality and primitive values, the exact Fourier moment, both filters on the complete 45-point rectangular support, their coefficient norms and selected multipliers, all translated-remainder orders, and the exponent algebra. It runs without NumPy or SymPy; checks remain active under Python optimization. Its deliberate fault-injection mode must fail. The bounded execution receipt is in [the evidence directory](../../evidence/executions/20261006/divisor-exclusion/receipt.json).

These exact finite controls do not certify the analytic sublevel theorem or quantum limit. The independent internal review reconstructed those analytic steps at the accepted source hash; [the curated review](../../archive/record/arithmetic_translation_review_20261006.md) records the scope and the editorial consolidation mapping. The earlier fixed-divisor review and the accepted quantitative source retain their original hashes in the provenance record.

The constant C_τ depends on the literal fixed coupling, analytic flow bounds and finite-type constants; it is independent of N,d and grid labels. No usable numerical startup, uniformity as τ→0, exponent optimality or control for unrestricted d_N is claimed. For any fixed δ<1/262 the rate is N^(−(1−262δ)/129); the endpoint δ=1/262 yields only a bounded estimate by this proof. The displayed δ=1/524 is a convenient strict interior example, not a critical threshold.

This theorem excludes a defined family of arithmetic high-frequency quasimodes. It does not classify the full algebraic commutant, rule out arbitrary spectral projections, prove near-return cancellation beyond the logarithmic window, or establish the signed Heisenberg joint-trace hierarchy. TRACE-005 and the fixed-map microscopic BGS target remain open. Finite common-commutant certificates at selected dimensions are separate bounded evidence and are not premises of this universal statement.
