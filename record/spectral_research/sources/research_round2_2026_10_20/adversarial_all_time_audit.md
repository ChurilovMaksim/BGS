> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_all_time_audit.md`. Embedded SHA256: `dbc1070d04c238213138b5eb433776d3ce0dfb6e9c07fca7eb90ebd9b42c7c25`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent adversarial audit of the all-time trace input

Date: 20 October 2026. Auditor: `/root/all_time_adversarial`.

## Verdict and exact scope

**The all-time transition is proved as written, with its stated small-h threshold.** After reconstructing the arguments from their formulas, I did not find a mathematical gap in the assertion

$$
\operatorname{Tr}U_N^m=\mathcal P_{m,N}+R_{m,N},\qquad
|R_{m,N}|<2(0.421)^m,
$$

for every sufficiently large odd N and every integer m≥1, with one N threshold independent of m. This does not assert this numerical estimate for every small odd dimension. The threshold comes from one edge operator, not from an iteration argument.

The audit does not prove H_diag. In particular, it does not treat an all-time periodic-orbit representation as an estimate for the oscillatory principal sum. The numerical calculations used below only check two low-dimensional normalizations and rounded constants; they are not evidence for an asymptotic claim.

### Frozen inputs

The following three files were read as proofs, without using their verdicts as premises:

| File | SHA256 |
|---|---|
| `odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` |
| `exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` |
| `gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` |

The fixed-point count was additionally checked from the strictly concave sector action in `classical_trace_and_pair_diagonal.md`, §§1–2. No external theorem on exact WKB amplitudes, all-time trace expansions, or Ruelle spectra is used in this audit.

## 1. The quantization convention cannot be skipped

The physical Weyl operator

$$
(\mathcal T_{(u,v)}\psi)(q)
=e^{iv(q-u/2)/h}\psi(q-u)
$$

at h=(2πN)^{-1} descends on the periodic comb to

$$
\mathcal T_{(-l/N,k/N)}=(-1)^{kl}T_N(l,k).
$$

Indeed, the real midpoint contributes exp(πikl/N), whereas the modular midpoint contributes exp(2πi kl(N+1)/(2N)); their ratio is (-1)^{kl}. Thus the actual plane symbol has r(q+1/2) in its l=±1 term. The source uses this corrected symbol consistently.

For integer n=(n_q,n_p), the choice R_n=(-1)^{n_qn_p}T_n removes the physical Weyl cocycle when N is odd. Hence R_nR_w=R_{n+w}. Since L≡I mod 2, the covariance μ_L R_n=R_{Ln}μ_L preserves this honest lattice representation. These signs are needed when identifying sector representatives.

The source's direct eight-residue Gauss-sum computation gives

$$
(\mu_L)_N=e_8(1-3N)M_N,
\qquad \zeta_N=e_8(3N-1).
$$

The distributional factor 1/(2N), the cancellation of odd half-lattice sites, and the remaining square-completion phase are all retained. No phase ambiguity remains in the comparison with the prescribed finite matrix.

## 2. Why the amplitude construction is exact and uniform in real h

Let

$$
F=F_0+G,\quad F_0=-(3Q^2-2Qq+3q^2)/8,
\quad F_t=a(Q,F_Q).
$$

The characteristic construction uses a bounded analytic vector field on a fixed complex strip. Although F_0 is unbounded in its real variables, its evolving momentum remains in the controlled imaginary strip. At fixed (Q,q), integrating F_t=a(Q,F_Q) bounds G by a constant times |t| over the whole real plane. The separate strip gap reserved for derivatives of G is essential.

For a Fourier index (k,l), put c=2πl. The exact identity

$$
\theta_h=2\pi((k-3l/4)Q+(l/4)q)
+h\kappa+c\int_0^1G_Q(Q+uch,q)\,du
$$

has κ=2π²kl−(3/2)π²l². For real h all shifts are horizontal, so they preserve every spatial strip even when |h| is not small. The imaginary part of θ_h has a bound independent of h and of Re Q, Re q. This is the reason the construction does not suffer an uncontrolled 1/h exponential after removing the Hamilton–Jacobi phase.

The exact amplitude equation is

$$
\partial_tB_h=L_hB_h,
$$

$$
L_h f=i\sum a_{kl}\left[
E_h\frac{f(Q+ch)-f(Q)}h+
\frac{E_h-E_0}h f(Q)\right].
$$

The difference quotients are represented by actual integrals of derivatives. Cauchy estimates, the independent phase margin, and the finite Fourier support therefore give

$$
\|\partial_h^jL_h\|_{H_{\rho+\delta}\to H_\rho}
\le10^6\delta^{-j-1},\quad j=0,1,2.
$$

For an n-fold Dyson term allocate δ=Δ/n to every factor. Its time simplex has volume |t|^n/n!, and n^n/n!≤e^n. Thus

$$
\|\mathcal B_n\|\le q^n,
\quad q=e10^6|t|/\Delta<1.
$$

After j derivatives in h, ordered choices of differentiated factors contribute at most n^j; the extra loss δ^{-j} contributes another n^j. Consequently

$$
\|\partial_h^j\mathcal B_n\|
\le\Delta^{-j}n^{2j}q^n,
\quad j=1,2.
$$

These series converge uniformly, including at h=0. They prove derivatives of the exact amplitude, not only formal coefficients. At the specified t_* the source's q is less than 4.327·10^{-72}; its displayed bounds on B_h−1 and its first two h derivatives follow.

For each fixed h≠0, L_h is also a bounded operator on one fixed strip, with a bound of order |h|^{-1}. Factoring the original quadratic phase gives the bounded equation for D_h=e^{iG/h}B_h. Its series is the same word series as that of exp(itA_h/h)μ_L. Each word kernel has a common absolute prefactor on the real plane, so this identification is valid against Schwartz test functions. This proves equality of tempered-distribution kernels; it does not rely on matching an asymptotic expansion.

The h=0 transport equation gives B_0=2√F_Qq with the positive real branch. Replacing h by −h and Fourier indices by their negatives gives B_{−h}=overline(B_h) on the real plane. Hence B_h=B_0+ihb_1+O(h²), where B_0 and b_1 are real.

### An explicit check of the amplitude deck law

The needed identity is not an extra quantization hypothesis. If (a,c)=L(b,d), the phase deck law is

$$
F(Q+a,q+b)-F(Q,q)=cQ-dq+(ca-db)/2.
$$

Under this translation the Fourier exponent θ_{kl,h} changes by 2π(ka+lc), an integer multiple of 2π. Thus every E_{kl,h} is invariant. Horizontal shifts commute with this deck translation, so L_h preserves invariant functions. Starting the convergent Dyson series at 1 proves B_h(Q+a,q+b)=B_h(Q,q). This argument works for every real h for which B_h is constructed.

## 3. The exact full-sector integral survives the Abel limit

For each fixed m,N, expand V^m into translated metaplectic words:

$$
V^m=\sum_\nu d_\nu\mathcal T_{w_\nu}\mu_L^m,
\qquad \sum_\nu|d_\nu|<\infty.
$$

The stronger exponential displacement bound in the source justifies Schwartz-space operations and lattice/coherent-state sums. The integral of the absolute coherent diagonal of one word is independent of its translation: changing variables by (L^m−I)z+w proves this directly. The lattice Gaussian has a uniformly bounded sum as its center varies. This legitimizes grouping lattice vectors into classes modulo (L^m−I)Z² and unfolding each class to one full plane integral. There is no missing determinant multiplier.

For the path-kernel form, the exact one-step word expansion gives quadratic integrands in the m position variables. Every word has the same Hessian

$$
H_m=-\tfrac14(6I-R-R^{-1}),
$$

whose eigenvalues lie in [-2,-1]. This includes m=1 and m=2; at these lengths coincident cyclic edges must be added, rather than discarded. The word-dependent term is real and linear, and its constant phase has modulus one.

For ε>0, integrating exp(−ε|q|²+i(q^TH_mq/2+ℓ·q+c)/h) gives a determinant prefactor times a completed-square factor of modulus at most one. The determinant prefactor is bounded by its ε=0 value. This bound is uniform in the real vector ℓ, and thus in the word translation. Since the absolute word coefficient mass is summable, dominated convergence permits passage to the common Abel limit term by term. Gaussian composition gives precisely the same translated operator as in the coherent expansion.

This is the substantive justification for the full R^m sector formula. It would not follow from an unregulated pointwise kernel composition alone. The source supplies the requisite common Gaussian regulator and uniform word bound.

## 4. The bounded contour has enough decay

Choose smooth odd ψ, equal to the identity near zero, monotone with 0≤ψ'≤1, and constant on each sufficiently far tail. Put z=u−iψ(u). For two consecutive coordinates let U=(u',u), V=(ψ(u'),ψ(u)) and D=U·V≥0.

Direct expansion of the unperturbed quadratic phase gives

$$
\Re(iF_0(U-iV))
=-[3D-u'\psi(u)-u\psi(u')]/4\le-D/2.
$$

The last inequality follows from (u'−u)(ψ(u')−ψ(u))≥0. For the centered perturbation, the uniform Hessian bound η and its reality on the real plane give

$$
|\Im\widetilde G(U-iV)|
\le\eta(|U|_1+|V|_1)|V|_1\le4\eta D.
$$

The final inequality uses |ψ(u)|≤|u| and the same-order property of |u| and |ψ(u)|. Thus the full centered phase has real exponential part at most −D/(4h).

Near the origin, D/h is quadratic in the rescaled coordinates y=u/√h. In a saturated tail it is bounded below by a constant times |y|/√h. This exponential tail remains integrable with every polynomial weight. A global Gaussian estimate in y would be false; the source uses the correct piecewise estimate.

For the contour deformation, keep the entire regulator exp(−ε∑q_j²). On the sides of an m-dimensional box the imaginary coordinates stay bounded. The oscillatory phase can grow at most like exp(C_{m,h}R), whereas the regulator supplies exp(−εR²). Side integrals therefore vanish for every fixed ε,h,m. On the final contour the regulator has modulus at most one in centered coordinates, and the preceding coercivity is an ε-independent integrable majorant. Its removal is an application of dominated convergence. Uniformity in m is not needed for this equality at each fixed m.

## 5. The trace-class reduction is dimension independent

On L²(R), let A=1−∂_y²+y². Its eigenvalues are 2(n+1), so ||A^{-1}||²_HS=π²/24. If S has kernel A_{y'}A_y k, then K=A^{-1}SA^{-1}. Hence

$$
\|K\|_1\le(\pi^2/24)\|A_{y'}A_yk\|_{L^2(R^2)}.
$$

The contour kernel and the required weighted derivatives decay rapidly. This proves trace class. On the straight portion z=(1−i)√h y, Taylor expansion gives the limiting real Gaussian with Hessian D²F at the edge. The complementary tails begin at |y|≥a/√h, where their weighted norms are O(exp(−c/h)) times a fixed power of h^{-1}; they vanish faster than every fixed power.

For the unperturbed edge the Gaussian operator has eigenvalues 1,ρ,ρ²,… with ρ=3−2√2. Direct integration against its Gaussian ground state verifies the leading eigenvalue and normalization; the Hermite generating identity supplies the remaining geometric sequence. Therefore

$$
\|K_G-P\|=\rho,\qquad
\|K_G-P\|_1=\frac{\rho}{1-\rho}
=\frac{\sqrt2-1}{2}.
$$

The perturbation at h=0 is bounded in trace norm by a constant times the uniform second-derivative bound for G. The actual fixed time is small enough by many orders of magnitude. Uniform convergence in h then gives one h_0>0 such that

$$
\sup_x\|K_h(x)-K_G\|_1\le10^{-4},\qquad 0<h<h_0.
$$

This estimate concerns one edge and hence has no dependence on m. The cyclic integral is exactly the trace of the product, because all involved kernels are smooth and rapidly decreasing. Factoring out C_h√h(1−i)λ_0=λ^{-1/2} gives the claimed external scalar per edge.

## 6. Exact graph splitting and the numerical all-time remainder

Write P=e_0e_0^*. On the radius-r ball in e_0^⊥, with r=0.00025, the normalized graph map is

$$
g_x(w)=\frac{(I-P)K_h(x)(e_0+w)}{e_0^*K_h(x)(e_0+w)}.
$$

The denominator is at least 1−δ, where δ=10^{-4}(1+r)=0.000100025. Differentiating the quotient and using ||g_x(w)||≤r bounds its Lipschitz constant by

$$
\frac{\rho+10^{-4}(1+r)}{1-\delta}
=0.17169007355\ldots<0.172.
$$

The fixed section exists by a contraction on bounded continuous sections over the invertible base map. The dual construction is on complex-linear functionals; no conjugation of the variable section enters. After compatible normalization,

$$
K_h(x)=R_h(x)+\mathcal B_h(x),\quad
R_h(x)=\gamma_h(x)v_h(\Psi x)\ell_h(x),
$$

and both consecutive mixed products vanish exactly. Thus on a period-m point the trace of the product is the scalar cycle Γ_h plus the trace of the residual product. The source's bounds imply

$$
\|\mathcal B_h\|<0.174,\qquad
\|\mathcal B_h\|_1<0.209.
$$

One trace-norm factor and m−1 operator-norm factors give

$$
|\operatorname{Tr}\mathcal B_{m-1}\cdots\mathcal B_0|
\le0.209(0.174)^{m-1}.
$$

The sector action has Hessian H_m plus a uniformly small nearest-neighbor perturbation. The negative quadratic form is coercive uniformly in m, and the perturbation of its gradient is bounded for each fixed sector. It is strongly concave, tends to −∞ at infinity, and has exactly one critical point. Deck covariance identifies its sectors with Fix Ψ^m. Consequently

$$
\#\operatorname{Fix}\Psi^m
=|\det(L^m-I)|=\lambda^m+\lambda^{-m}-2<\lambda^m.
$$

Summing absolute residuals now gives

$$
|R_{m,N}|\le\lambda^{m/2}0.209(0.174)^{m-1}
=\frac{0.209}{0.174}(0.174\sqrt\lambda)^m.
$$

Here 0.209/0.174<1.202 and 0.174√λ=0.42007315985…<0.421. This proves the stated bound for every m, including m=1, with the same h threshold.

## 7. Uniform finite jets: why the modulus estimate is valid

The full edge family need not be differentiable in h at zero; it has odd powers of s=√h. The correct expansion is in s. On the straight contour, write its centered phase as a Taylor series at the real edge. Since i(1−i)^{j+2}=2(1−i)^j and the phase Taylor coefficients are real, the coefficient at s^j has the form (1−i)^j times a real kernel. The same holds for the amplitude because B_h=B_0+ihb_1+O(h²) and i=−(1−i)²/2.

To justify the remainder, differentiate the entire local exponential as a function of the intermediate Taylor parameter. Its real part remains bounded above by a negative quadratic form, uniformly for that parameter. The derivatives therefore have a polynomial times a Gaussian majorant. This is stronger than merely treating the cubic Taylor term as uniformly small, which would fail for y growing with h^{-1/2}. The tail estimate handles the nonstraight portion. Applying the trace-norm criterion proves an actual O(s⁴) remainder, uniformly in the base point.

Finite jets pass through the graph contraction by solving (I−T)w_j=known_j at each order; ||T||<0.172. The polynomial approximate section has an O(s⁴) defect, and its distance from the true fixed section is at most the defect divided by 1−0.172. Reflection of y proves K_{−s}=RK_sR and thus γ_{−s}=γ_s. Reality of the coefficient recursion then gives

$$
\gamma_h=\gamma_0+h\gamma_1+O(h^2),
\quad \gamma_0>0,\quad\gamma_1\in i\mathbb R,
$$

uniformly in x. Therefore log|γ_h|²=2logγ_0+O(h²).

The Gaussian Hill identity identifies the exact zeroth-order cycle normalization. It follows either by the cyclic Jacobi recurrence or by the twisted determinant argument in the source. As a check against the coincident-edge mistake, m=1 gives det(−H_1)=1 and m=2 gives det(−H_2)=2; both equal 4^{-m}|det(I−L^m)|. Repeating a fixed cycle and taking positive roots of the exact Gaussian formula removes the residual geometrically and gives

$$
\lambda^{-m}\Gamma_0(x,m)^2\Lambda_m(x)=1.
$$

Thus the source's O(mh²) logarithmic modulus estimate follows. Neither the repetition argument nor the finite-jet proof requires a dimension-uniform stationary-phase remainder.

## 8. A real limitation for any next argument

The contraction acts on continuous sections over the base. It proves continuous dependence on x and uniform finite jets in h. It does **not** prove that γ_h is smooth or analytic in x. Differentiating n past iterates of the base introduces roughly λ^n, whereas the transverse contraction is roughly ρ^n; ρλ=1 is a genuine borderline. This issue does not affect any step above, but it matters if one tries to invoke an analytic scalar transfer-operator theorem for γ_h.

An explicit counterexample to that automatic regularity inference is given in the separate file `adversarial_graph_regularity.md`. It is not a counterexample to H_diag or to the actual family's all-time trace representation.

The remaining unproved statistical estimate is still the cancellation of the fully weighted principal periodic sums at m proportional to N, already for a fixed admissible pair test. Positivity, unitarity, and the all-time remainder bound alone do not supply that estimate.
