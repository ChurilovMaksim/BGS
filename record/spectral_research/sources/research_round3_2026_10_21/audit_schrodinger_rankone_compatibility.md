> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/audit_schrodinger_rankone_compatibility.md`. Embedded SHA256: `76acb4983385655f4629a17dbefa5212f293e2c58c4ecd3fd5a520a41b5ca193`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: the actual Schrödinger exponential and the rank-one cocycle

Date: 2026-10-21. Auditor: `/root/trace_foundation_audit_20261021/schrodinger_rankone_check`.

## Claim and verdict

**Primary verdict for the complete trace reduction: conditional on the exact sector-to-contour identity and the stated uniform trace-norm neighborhood.** This report checks a narrower possible obstruction: whether the rank-one cocycle is attached to a merely formal semiclassical surrogate instead of the actual operator

$$
U_N=e^{i\tau N A_N}M_N,\qquad \tau=10^{-80},\quad N\text{ odd}.
$$

I reconstructed the midpoint correction, the exact plane exponential equation, and the rank-one graph identities from the definitions. On these points I found **no incompatibility**. In particular, the exact amplitude argument can identify its one-step kernel with the actual Schrödinger exponential without assuming convergence of a semiclassical Taylor series. The rank-one splitting, once the operator-norm neighborhood has been established, is an exact splitting of an orbit-dependent contour cocycle. It is not a rank-one approximation of the finite unitary matrix itself.

This is not a pass of the complete trace estimate, its all-time quantifier, or its modulus estimate. The finite coherent-sector to full multi-variable Fresnel conversion is a separate input being audited by the parent. The trace-norm contour estimates are recorded here as named inputs rather than inferred from the correctness of the exponential identification.

## Exact source revisions

| Source | SHA-256 |
|---|---|
| `Spectral_partial_results_2026-10-20.md` | `b8c5e2071d49394270006853ee8316f3900e84f1a7ae9b03e58e5c4eaf29a7cc` |
| `research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` |
| `research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` |

The main statement is at main-report lines 160–210. The raw definitions of the finite operator are odd-trace lines 25–68; the plane correction and descent are lines 234–272. The exact amplitude identification is amplitude lines 403–448. The rank-one construction is Gaussian lines 394–557. No previous PASS file or earlier audit verdict was used as evidence.

## 1. Reconstruction from the finite definition

The finite Weyl operator is

$$
(T_N(l,k)u)(x)=e_N\bigl(k(x+\overline2 l)\bigr)u(x+l),
\quad \overline2=(N+1)/2\pmod N.
$$

Let $h=(2\pi N)^{-1}$. Physical Weyl quantization of a plane Fourier mode has the exact action

$$
\operatorname{Op}_h^W(e^{2\pi i(kq+lp)})\psi(Q)
=e^{2\pi ik(Q+\pi hl)}\psi(Q+2\pi hl).
$$

At $Q=x/N$, the ordinary midpoint in this formula contributes the phase $e_N(kl/2)$, while the modular midpoint contributes $e_N(kl(N+1)/2)$. Their ratio is $(-1)^{kl}$. Therefore the ordinary plane symbol descending to $A_N=\sum c_{kl}T_N(l,k)$ has Fourier coefficients

$$
a_{kl}=(-1)^{kl}c_{kl}.
$$

The only modes of the specified symbol with $l\ne0$ have $l=\pm1$. For them this coefficient change is exactly the shift $q\mapsto q+1/2$ in the mixed term. Consequently the corrected symbol in odd-trace equation (5.2) is the symbol of the stated finite matrix, rather than an unannounced change of quantization.

The real coefficient symmetry is preserved by $(-1)^{kl}$. Thus $A_h=\operatorname{Op}_h^W(a)$ is a bounded self-adjoint finite sum of translations on $L^2(\mathbb R)$. Its norm is at most $\sum|a_{kl}|<2$. It commutes with the integer lattice representation because every commutator phase between one Fourier Weyl mode and an integer translation is an integer multiple of $2\pi$.

The finite quotient of the chosen metaplectic kernel is $\zeta_N^{-1}M_N$, with $\zeta_N=e_8(3N-1)$, as computed in the odd-trace source. Assuming that independently stated scalar computation, descent commutes with the exponential series:

$$
\left.e^{itA_h/h}\mu_L\right|_{\mathrm{comb}}
=e^{itA_N/h}\zeta_N^{-1}M_N
=\zeta_N^{-1}e^{i\tau N A_N}M_N.
$$

Here $t=\tau/(2\pi)$, so $t/h=\tau N$. There is no sign or factor-of-$2\pi$ mismatch. The Hamilton–Jacobi equation $F_t=a(Q,F_Q)$ has characteristic field $(-a_p,a_q)$, which is also consistent with the main report's $\Phi_{-\tau}S^{-1}$ convention.

## 2. The exact amplitude equation is the equation of the actual exponential

Write

$$
F=F_0+G,
\qquad F_0(Q,q)=-\frac{3Q^2-2Qq+3q^2}{8},
$$

and consider $K=C_h e^{iF/h}B_h$. For a Fourier mode put $c=2\pi l$ and

$$
E_{kl,h}=
\exp\left(i2\pi k(Q+\pi hl)
+i\frac{F(Q+ch,q)-F(Q,q)}h\right).
$$

Substituting the exact finite-shift action above into $K_t=(i/h)A_hK$ gives

$$
\partial_tB_h
=\frac ih\sum_{kl}a_{kl}
\left[E_{kl,h}B_h(Q+ch,q)-E_{kl,0}B_h(Q,q)\right].
$$

This is precisely amplitude equation (8), since $F_t=a(Q,F_Q)=\sum a_{kl}E_{kl,0}$. It is an algebraic identity for every fixed nonzero real $h$, not a Taylor approximation of a shift operator.

To check exact identification independently, set

$$
D_h=e^{iG/h}B_h.
$$

Then the nonlinear-looking eikonal terms cancel, leaving

$$
\partial_tD_h=P_hD_h,\qquad D_h(0)=1,
$$

where

$$
P_hf=
\frac ih\sum_{kl}a_{kl}
e^{i[2\pi((k-3l/4)Q+(l/4)q)+h\kappa_{kl}]}
f(Q+2\pi hl,q),
$$

$$
\kappa_{kl}=2\pi^2kl-\frac32\pi^2l^2.
$$

The phase in this formula is obtained directly by subtracting the two quadratic values of $F_0$. For real $h$, all shifts are horizontal. Thus $P_h$ is bounded on each fixed space of bounded holomorphic functions in a horizontal strip. Its bound is of order $|h|^{-1}$, which is sufficient for uniqueness at that fixed $h$.

For each $n$, direct application of $A_h$ to the quadratic kernel gives

$$
\left(\frac ih A_h\right)^n
\left(C_h e^{iF_0/h}\right)
=C_h e^{iF_0/h}P_h^n1.
$$

This identity follows by induction from the exact Weyl shift formula. The left-hand kernel series is dominated on the real plane by

$$
|C_h|\sum_{n\ge0}\frac{(|t|\sum|a_{kl}|/|h|)^n}{n!},
$$

so it converges against every Schwartz test function. It is the distribution kernel of the norm-convergent bounded-operator exponential $e^{itA_h/h}\mu_L$. On the right, the unique strip-space solution is $e^{tP_h}1$. Therefore any amplitude constructed as a genuine solution of equation (8) has exactly the kernel of the actual exponential.

The source's convergent analytic-scale Dyson construction supplies that solution: each factor loses one strip derivative with a fixed coefficient, and an $n$-fold product with equal strip allocation has majorant

$$
\frac{|t|^n}{n!}\left(\frac{Cn}{\Delta}\right)^n
\le\left(\frac{eC|t|}{\Delta}\right)^n.
$$

At $C=10^6$, $\Delta=10^{-3}$, and $|t|\le10^{-12}$, its ratio is less than $0.002719$. Differentiating twice in the real parameter $h$ adds at most $\Delta^{-2}n^4$, preserving summability. This identifies a convergent family of actual amplitudes, not an infinite formal power series in $h$.

The argument does **not** provide holomorphy in a fixed complex $h$ disk. The source does not need such a statement for the exact exponential identity at $h=(2\pi N)^{-1}>0$.

## 3. Independent algebra of the rank-one splitting

Let $K_G$ be the normalized Gaussian operator in Gaussian equation (4.4). Direct Gaussian integration on the stated ground state gives its largest eigenvalue $1$; Mehler expansion gives the remaining eigenvalues $\rho^j$, $\rho=3-2\sqrt2$. With $P=e_0e_0^*$, suppose that the separately justified contour operators satisfy

$$
\sup_x\|K_h(x)-K_G\|_1\le\varepsilon=10^{-4}.
$$

In particular the same bound holds in operator norm. Relative to $\mathbb Ce_0\oplus e_0^\perp$, write

$$
K_h(x)=\begin{pmatrix}a&b\\c&D\end{pmatrix}.
$$

Then $|a-1|,\|b\|,\|c\|\le\varepsilon$ and $\|D\|\le\rho+\varepsilon$. On $\|w\|\le r=0.00025$, the projective graph map is

$$
g_x(w)=\frac{c+Dw}{a+bw}.
$$

The denominator is at least $1-\varepsilon(1+r)$, and

$$
\|g_x(w)\|
\le\frac{\rho r+\varepsilon(1+r)}{1-\varepsilon(1+r)}<r.
$$

For two arguments, subtracting the fractions gives

$$
g_x(w_1)-g_x(w_2)
=\frac{[D-g_x(w_2)b](w_1-w_2)}{a+bw_1}.
$$

This proves a Lipschitz bound less than $0.172$. Composing with the inverse base map therefore produces a global fixed section $v(x)=e_0+w(x)$, and

$$
K(x)v(x)=\gamma(x)v(\Psi x),
\qquad |\gamma-1|\le\varepsilon(1+r).
$$

The future graph construction on complex-linear row functionals gives $u(x)=e_0^*+z(x)$. Since $u(x)v(x)=1+z(x)w(x)$ has distance at most $r^2$ from $1$, one may normalize $\ell(x)=u(x)/(u(x)v(x))$. Evaluating the dual recurrence on $v(x)$ forces the same scalar $\gamma$:

$$
\ell(x)v(x)=1,
\qquad \ell(\Psi x)K(x)=\gamma(x)\ell(x).
$$

Hence, for

$$
R(x)=\gamma(x)v(\Psi x)\ell(x),\qquad
\mathcal B(x)=K(x)-R(x),
$$

one has exactly

$$
\mathcal B(x)v(x)=0,
\quad \ell(\Psi x)\mathcal B(x)=0,
$$

and therefore

$$
R(\Psi x)\mathcal B(x)=0,
\qquad \mathcal B(\Psi x)R(x)=0.
$$

Every nonconstant word in the two letters $R$ and $\mathcal B$, along a consecutive orbit product, has an adjacent change of letter and consequently vanishes. For a periodic base point, the trace of the pure $R$ word is exactly $\prod\gamma$. This derivation contains no formal truncation in $h$, no finite-time boundary choice, and no unproved scalar matching between the left and right sections.

## 4. Why unitarity itself supplies no counterexample to this construction

The operator $K_h(x)$ is a centered complex-contour edge operator on an auxiliary $L^2(\mathbb R)$. Its dependence on the classical base point $x$ is essential. Neither the source's formulas nor the derivation above assert

$$
U_N=\text{one rank-one matrix}+\text{a small matrix}.
$$

There is consequently no immediate contradiction with the $N$ unimodular eigenvalues of $U_N$. The global quantum trace is obtained, if the exact sector input holds, by summing the scalar cocycle trace over all classical periodic points, with oscillatory action phases. The number of such points grows with the iterate. An individual dominant contour direction is not a dominant quantum eigenvector.

Likewise, an Euler product whose primitive weights have modulus below $1$ can have zeros on $|z|=1$ after analytic continuation. Its initial disk of absolute convergence and its continuation must not be conflated. No contradiction can be inferred solely by inspecting the primitive moduli.

## Obligation matrix and surviving claims

| Obligation | Audit status |
|---|---|
| Corrected ordinary symbol descends to the stated modular Weyl Hamiltonian | Passed by the direct midpoint calculation |
| Correct sign and time normalization of the plane Schrödinger exponential | Passed |
| Exact one-step amplitude equation, rather than formal shift expansion | Passed by exact substitution |
| Actual exponential identification at positive real $h$ | Passed by bounded strip-space uniqueness and the convergent kernel series |
| Uniform trace-norm proximity of contour operators to $K_G$ | Named input; not certified by this subaudit |
| Exact invariant rank-one splitting given that proximity | Passed by the block-operator graph calculation |
| Complete coherent-sector to multi-variable Fresnel identity | Not addressed here; parent audit |
| Periodic-point count and all-time sum for actual finite traces | Conditional on the preceding trace input and counting input |
| $|u_{p,N}|^2=\Lambda_p^{-1}e^{O(d_p/N^2)}$ | Not addressed by this subaudit |
| Full $H_{\rm diag}$ | Not implied by any result in this report |

The strongest safe result from this subaudit is the exact one-step identification with the specified finite Schrödinger family, together with the exact algebraic dominated-cocycle reduction under its stated analytic hypotheses. I have not found a counterexample at this stage. The cheapest decisive remaining check for the complete trace claim is the passage from the coherent-sector definition to the single full $m$-variable kernel integral, preserving the regularization, all deck multiplicities, and the actual exponential.

## Provenance and checks

This was a fresh child-agent reconstruction requested without any prior audit verdict as evidence. The source revision was checked with `sha256sum`; definitions and proof steps were read with `nl -ba` and `sed`. No finite numerical test was substituted for a universal mathematical implication. This new report is the only written artifact of the subaudit; no earlier source was changed.
