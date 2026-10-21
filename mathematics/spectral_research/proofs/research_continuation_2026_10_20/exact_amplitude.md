> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_continuation_2026_10_20/exact_amplitude.md`. Embedded SHA256: `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e`.
> [Thematic guide](../../topics/classical_trace.md).

# Independent audit and proof of the exact analytic amplitude

Date: 2026-10-20.

## Verdict and scope

The exact amplitude construction is valid for the stated fixed, extremely short Hamiltonian time. It produces the exact plane propagator kernel, not merely a formal semiclassical expansion. Real Weyl shifts preserve every horizontal spatial strip; after the Hamilton–Jacobi term is subtracted, the remaining operator loses one spatial derivative uniformly as real h tends to zero. Differentiating its convergent Dyson series gives genuine uniform C-infinity dependence on real h, including h = 0. In particular, the first two h derivatives have explicit bounds below.

This lemma concerns the one-step propagator at the fixed time t_* = 10^(-80)/(2 pi). It does not by itself establish a trace formula for arbitrarily many iterates, nor does it assert that one Hamilton–Jacobi phase remains nondegenerate for arbitrary Hamiltonian time.

No external theorem about exact WKB amplitudes is needed: the proof below consists of finite Fourier identities, a small-time characteristic construction, Cauchy estimates, a convergent Dyson series, and uniqueness for a bounded operator equation at each fixed nonzero real h.

## 1. Symbol, normalization, and midpoint convention

Write

$$
a(x,p)=\sum_{(k,l)\in\Lambda}a_{kl}e^{2\pi i(kx+lp)},\qquad
|k|+|l|\le9,\qquad \sum|a_{kl}|<2.
$$

The assertion that a is real on the real plane means

$$
a_{-k,-l}=\overline{a_{kl}}.
$$

All estimates below hold for this full frequency set. Additional restrictions such as |l| <= 1 and |k| <= 8 only improve the constants.

For P = -ih partial_Q, the correct Weyl action is

$$
(A_h\psi)(Q)=\sum a_{kl}
e^{2\pi ik(Q+\pi hl)}\psi(Q+2\pi hl).
\tag{1}
$$

The midpoint factor in (1) is essential. Each summand without its coefficient is unitary on L^2(R), and its adjoint is the summand with (-k,-l). Thus A_h is bounded, has norm less than 2, and is self-adjoint for real h and real a.

The metaplectic phase and prefactor are

$$
F_0(Q,q)=-\frac{3Q^2-2Qq+3q^2}{8},\qquad
C_h=\frac{e^{i\pi/4}}{\sqrt{8\pi h}},\quad h>0.
$$

Indeed, p = -partial_q F_0 and P = partial_Q F_0 give

$$
\binom QP=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}\binom qp.
$$

We use the Hamilton–Jacobi convention

$$
\partial_t F=a(Q,\partial_Q F),\qquad F(0)=F_0.
\tag{2}
$$

Accordingly its characteristic vector field is (-a_p,a_x), equivalently the Hamiltonian vector field of -a. This is the convention appropriate to exp(+it A_h/h).

Throughout, T = 10^(-12) is the auxiliary interval of Hamiltonian times. The actual time is

$$
\tau=10^{-80},\qquad t_*=\frac{\tau}{2\pi}
=1.5915494309\ldots\times10^{-81}.
$$

## 2. The phase and the reserved strips

Let

$$
S_\rho=\{(Q,q)\in\mathbb C^2:|\operatorname{Im}Q|<\rho,
\ |\operatorname{Im}q|<\rho\},
$$

and let H_rho be the Banach space of bounded holomorphic functions on S_rho, with the supremum norm. Strips always extend over the whole real plane.

Here is a direct small-time justification of the phase input used below. On the phase-space strip |Im x|, |Im p| < 0.01, the finite Fourier assumptions imply

$$
\|a\|<4,\qquad \|X_{-a}\|_\infty<300,
\qquad \|DX_{-a}\|_{\infty\to\infty}<20000.
\tag{3}
$$

For example, the derivative-row bound follows from

$$
(2\pi)^2\sum|a_{kl}|\,|l|(|k|+|l|)
e^{2\pi\cdot0.01(|k|+|l|)}<20000,
$$

and the other row is identical with k replacing l.

Start the characteristic flow at

$$
(Q_0,P_0)=(Q_0,-3Q_0/4+q/4).
$$

For (Q_0,q) in S_0.005 and |t| <= T, the displacement is less than 300T = 3 times 10^(-10), and the derivative of the flow differs from the identity by less than

$$
e^{20000T}-1<2.1\times10^{-8}.
$$

Consequently the equation Q(t;Q_0,q) = Q has a unique solution near Q_0 = Q for every (Q,q) in S_0.004. This follows directly by contracting the equation Q_0 = Q - [Q(t;Q_0,q)-Q_0] on the disk |Q_0-Q| <= 4 times 10^(-10). The solution depends holomorphically on (Q,q).

The characteristic action

$$
F(t,Q,q)=F_0(Q_0,q)+\int_0^t
\big(P(s)\dot Q(s)+a(Q(s),P(s))\big)\,ds
$$

therefore defines a holomorphic generating function on S_0.004 satisfying (2). Its reality follows from the real coefficients in the equations and the real initial phase. Although F_0 and the action separately need not be bounded over the real plane, their difference G = F-F_0 is bounded: at fixed (Q,q), equation (2), the phase-space strip estimate, and G(0)=0 give |G| <= 4|t|. We will use only the weaker bound

$$
\|G(t)\|_{0.003}\le10|t|,\qquad |t|\le T.
\tag{4}
$$

Reserve the gap from 0.003 to 0.002 for the phase. Cauchy's estimate then gives, in particular,

$$
\|\partial_Q^mG(t)\|_{0.002}
\le m!\,10^{3m+1}|t|.
\tag{5}
$$

Mixed derivatives satisfy the analogous product-factorial estimate. At |t| <= T, convenient bounds for the first four Q derivatives are

$$
M_1=10^{-8},\quad M_2=2\times10^{-5},\quad
M_3=0.06,\quad M_4=240.
\tag{6}
$$

Amplitude strip widths will never exceed R = 0.002. This fixed phase margin is substantive: taking two phase derivatives out of the same shrinking strip gap as the amplitude would obscure, or invalidate, the claimed first-order analytic-scale bound.

## 3. Exact amplitude equation and removal of the h denominators

For one Fourier index put

$$
c=2\pi l,\qquad
\kappa=2\pi^2kl-\frac32\pi^2l^2,
$$

and define

$$
\theta_h=2\pi k(Q+\pi hl)
+\frac{F(t,Q+ch,q)-F(t,Q,q)}h,\qquad
E_h=e^{i\theta_h}.
$$

At h = 0 the smooth extension is

$$
\theta_0=2\pi(kQ+lF_Q),\qquad E_0=e^{2\pi i(kQ+lF_Q)}.
$$

The exact identity that removes all problematic affine real parts is

$$
\theta_h=2\pi\left((k-3l/4)Q+(l/4)q\right)
+h\kappa+c\int_0^1G_Q(t,Q+uch,q)\,du.
\tag{7}
$$

For real h, every point Q+uch remains in the same horizontal strip, regardless of the size of the real shift. Thus (7) is bounded after exponentiation, uniformly over the entire real plane and uniformly for all real h. Neither an assumption |ch| < delta nor a restriction of the real parts of Q and q is needed.

Substitution of K_h = C_h exp(iF/h) B_h into partial_t K_h = (i/h) A_h K_h, followed by (2), gives exactly

$$
\partial_t B_h=L_h(t)B_h,\qquad B_h(0)=1,
$$

$$
L_hf=i\sum a_{kl}\left[
E_h\frac{f(Q+ch,q)-f(Q,q)}h
+\frac{E_h-E_0}h f(Q,q)\right].
\tag{8}
$$

Both quotients are removable at real h = 0. Their useful exact integral formulas are

$$
\frac{f(Q+ch)-f(Q)}h
=c\int_0^1f_Q(Q+uch)\,du,
\tag{9}
$$

$$
\frac{E_h-E_0}h=\int_0^1(\partial_hE)_{uh}\,du.
\tag{10}
$$

These formulas, not a formal power series in h, define the extension at h = 0.

## 4. Uniform exponent estimates, including the cubic term

For the full allowed frequency set,

$$
|c|<57,\qquad |\kappa|<1200.
\tag{11}
$$

For the second inequality, with m = |l|,

$$
|\kappa|/\pi^2\le 2(9-m)m+\tfrac32m^2
=18m-\tfrac12m^2\le121.5.
$$

On every S_rho with rho <= R = 0.002, (7) gives

$$
|\operatorname{Im}\theta_h|\le2\pi\cdot9R+57M_1,
\qquad |E_h|\le M:=1.13.
\tag{12}
$$

The elementary complex exponential estimate must be used in its correct form. Namely,

$$
E_h-E_0=i(\theta_h-\theta_0)
\int_0^1e^{i((1-v)\theta_0+v\theta_h)}\,dv.
$$

Both endpoint imaginary parts are bounded by (12); their convex interpolates have the same bound. Since

$$
\theta_h-\theta_0=h\left[\kappa+c^2\int_0^1
(1-u)G_{QQ}(Q+uch)\,du\right],
$$

we obtain

$$
\left|\frac{E_h-E_0}h\right|
\le M\left(1200+\frac{57^2M_2}{2}\right).
\tag{13}
$$

In particular one must not use |exp(iz)-exp(iw)| <= |z-w| without the imaginary-part factor. Formula (13) is the correct uniform replacement.

For each j >= 1, differentiation of (7) gives

$$
\partial_h^j\theta_h=
\mathbf1_{j=1}\kappa+c^{j+1}\int_0^1u^j
G_{Q^{j+1}}(Q+uch)\,du.
\tag{14}
$$

For j = 1,2,3, upper bounds are

$$
U_1=1200.03249,\quad U_2=3703.86,\quad
U_3=633360060.
$$

Therefore

$$
\|E'_h\|\le MU_1<1360,
$$

$$
\|E''_h\|\le M(U_1^2+U_2)<1.64\times10^6,
$$

$$
\|E'''_h\|\le M(U_1^3+3U_1U_2+U_3)<2.7\times10^9.
\tag{15}
$$

The potentially large cubic term kappa^3 is expressly included in the last estimate. All bounds are uniform in real h and |t| <= T.

## 5. The operator estimates, including two h derivatives

For 0 < rho < rho+delta <= R, Cauchy's estimate and (9) imply

$$
\left\|\partial_h^j
\frac{f(Q+ch)-f(Q)}h\right\|_\rho
\le |c|^{j+1}j!\,\delta^{-j-1}\|f\|_{\rho+\delta}.
\tag{16}
$$

Equation (10) gives

$$
\left\|\partial_h^j\frac{E_h-E_0}h\right\|_\rho
\le\frac{\|E_h^{(j+1)}\|_\rho}{j+1}.
\tag{17}
$$

Let V_1 = 1360, V_2 = 1.64 times 10^6, V_3 = 2.7 times 10^9. Apply the product rule in (8), use sum|a_kl| < 2, and convert lower powers of delta^(-1) to the desired power with delta <= R. This gives

$$
\|\partial_h^rL_h\|_{H_{\rho+\delta}\to H_\rho}
\le D_r\delta^{-r-1},\qquad r=0,1,2,
\tag{18}
$$

where one may take

$$
D_0=2(M57+RV_1)<135,
$$

$$
D_1=2(RV_1\,57+M57^2+R^2V_2/2)<7700,
$$

$$
D_2=2\left(R^2V_2\,57+2RV_1\,57^2
+2M57^3+R^3V_3/3\right)<874000.
\tag{19}
$$

Thus the single convenient constant C = 10^6 is valid for all r = 0,1,2:

$$
\boxed{\quad
\|\partial_h^rL_h\|_{\rho+\delta\to\rho}
\le10^6\delta^{-r-1},\qquad r=0,1,2.
\quad}
\tag{20}
$$

For every fixed higher r there is likewise a finite D_r in (18), by (5), (14), the finite-order chain rule for exp(i theta), and (16)-(17). These constants may grow rapidly with r. Their finiteness and independence of h are what the C-infinity argument requires.

## 6. Convergent Dyson series and genuine real-h smoothness

Let Bcal_0 = 1 and, for n >= 1, let Bcal_n be the time-ordered n-fold integral of L_h(t_1)...L_h(t_n) applied to 1. Define

$$
B_h(t)=1+\sum_{n\ge1}\mathcal B_n(t,h).
\tag{21}
$$

Take input width R = 0.002, final width rho_* = 0.001, and Delta = R-rho_* = 0.001. In the n-fold product allocate delta = Delta/n to each factor. From (20),

$$
\|\mathcal B_n\|_{\rho_*}
\le\frac{|t|^n}{n!}\left(\frac{Cn}{\Delta}\right)^n
\le q^n,\qquad q=\frac{eC|t|}{\Delta}.
\tag{22}
$$

Since e C T/Delta < 0.002719, the series converges uniformly on this entire time interval and uniformly in real h.

There is a direct estimate for actual derivatives of this series. Differentiating an n-fold product r times makes at most n^r ordered choices of the differentiated factors. The sum of their derivative orders is r; (20) therefore adds delta^(-r). For r = 1,2 this yields

$$
\boxed{\quad
\|\partial_h^r\mathcal B_n\|_{\rho_*}
\le\Delta^{-r}n^{2r}q^n,\qquad r=1,2.
\quad}
\tag{23}
$$

The two powers n^r have different origins: n^r from choosing factors, and n^r from the additional Cauchy derivative loss. There is no new geometric factor depending on n. In particular the second derivative produces n^4 q^n, a summable sequence.

For a general fixed r, choose K_r >= 1 such that D_j <= C K_r^j for 1 <= j <= r. The identical argument gives

$$
\|\partial_h^r\mathcal B_n\|_{\rho_*}
\le(K_r/\Delta)^r n^{2r}q^n.
\tag{24}
$$

Consequently every real-h derivative series converges uniformly, including across h = 0. Thus (21) defines a C-infinity map of real h into H_0.001. This proves smooth dependence, as opposed to merely supplying coefficients of a formal expansion. It does not assert convergence of the Taylor series in h, nor holomorphy in a fixed complex-h disk.

At the actual time t_*,

$$
q_*=4.3262798971\ldots\times10^{-72}.
$$

Summing (22)-(23) gives the convenient rigorous bounds

$$
\|B_h(t_*)-1\|_{0.001}<6\times10^{-72}<10^{-69},
$$

$$
\|\partial_hB_h(t_*)\|_{0.001}<6\times10^{-69},
\qquad
\|\partial_h^2B_h(t_*)\|_{0.001}<6\times10^{-66}.
\tag{25}
$$

These bounds are uniform in all real h; in particular they apply to h = (2 pi N)^(-1).

## 7. Exact identification with the plane propagator

Fix any nonzero real h. Define

$$
D_h(t,Q,q)=e^{iG(t,Q,q)/h}B_h(t,Q,q).
$$

Since G is bounded on the strip, D_h belongs to the same H_rho for this fixed h. It is not necessary for its norm to be uniform as h tends to zero.

The exact amplitude equation, with the Hamilton–Jacobi term cancelled, gives

$$
\partial_t D_h=P_hD_h,\qquad D_h(0)=1,
$$

$$
P_hf=\frac ih\sum a_{kl}
\exp\left(i\left[2\pi((k-3l/4)Q+(l/4)q)+h\kappa\right]\right)
f(Q+2\pi hl,q).
\tag{26}
$$

This is a bounded operator on each fixed H_rho:

$$
\|P_h\|_{H_\rho\to H_\rho}
\le\frac{2e^{2\pi\cdot9\rho}}{|h|}.
\tag{27}
$$

Thus its initial-value problem has the unique solution exp(tP_h)1. Equivalently, for fixed nonzero h, L_h itself is a bounded operator on each fixed strip, with a bound of order 1/|h|, so its ordinary bounded-operator Dyson series proves that (21) solves the exact equation. The analytic-scale estimates are needed for uniformity in h, not for this fixed-h uniqueness.

The kernel of A_h^n mu_L is obtained by applying the same finite shifts and multipliers n times to C_h exp(iF_0/h). Factoring out this initial quadratic kernel gives exactly P_h^n1, including the factors i/h in the exponential series. The kernel series is absolutely convergent against Schwartz test functions: its n-th coefficient is bounded by |C_h| 2^n before the time and factorial factors are applied. It therefore agrees, as a tempered-distribution kernel, with the bounded-L^2 operator series for exp(itA_h/h)mu_L.

Uniqueness in (26) now gives

$$
\boxed{\quad
K_{\exp(itA_h/h)\mu_L}(Q,q)
=C_h e^{iF(t,Q,q)/h}B_h(t,Q,q),\qquad h>0.
\quad}
\tag{28}
$$

No O(h-infinity) remainder, microlocal restriction, or asymptotic identification occurs in this argument.

## 8. The h = 0 amplitude

The h = 0 limit of (8) is the first-order transport operator

$$
L_0f=a_p(Q,F_Q)f_Q
+\frac12\left(a_{xp}(Q,F_Q)+a_{pp}(Q,F_Q)F_{QQ}\right)f.
\tag{29}
$$

Let J = F_Qq. Differentiating (2) gives

$$
J_t=a_pJ_Q+(a_{xp}+a_{pp}F_{QQ})J,
\qquad J(0)=1/4.
$$

By (5), J remains close to 1/4 on the reserved strip. Choose the analytic square root through sqrt(1/4)=1/2. Then 2 sqrt(J) solves (29) with initial value 1. Uniqueness follows either by the characteristic equation or by the same small-time analytic-scale uniqueness. Therefore

$$
\boxed{B_{h=0}(t,Q,q)=2\sqrt{F_{Qq}(t,Q,q)}.}
\tag{30}
$$

This uses the positive branch on the real plane. It also reconciles the fixed prefactor C_h with the usual varying leading Jacobian amplitude.

## 9. Reality and parity in h

Let C denote analytic conjugation: (Cf)(Q,q) = overline(f(overline(Q),overline(q))). For real Q,q this is ordinary complex conjugation. Because F is real there and a_-k,-l = overline(a_kl), the exact midpoint phase satisfies

$$
E_{kl,-h}=\overline{E_{-k,-l,h}}
\quad\text{on the real plane}.
$$

The associated shift with (-k,-l) at h is precisely the shift with (k,l) at -h. Changing the summation index (k,l) to (-k,-l) in (8), including the conjugation of i/h, gives

$$
L_{-h}\mathcal C=\mathcal C L_h.
$$

Apply this identity term by term to the convergent Dyson series and use the real initial value 1. It follows that

$$
\boxed{B_{-h}(t,Q,q)=\overline{B_h(t,Q,q)}
\quad\text{for real }Q,q.}
\tag{31}
$$

Consequently B_0 and the even h derivatives at zero are real, while odd h derivatives at zero are purely imaginary. This identity is for the amplitude and does not require choosing a negative-h branch of the metaplectic prefactor.

## 10. What the bounds provide for a rescaled kernel expansion

Cauchy estimates on any smaller strip, for example S_0.0005, turn (25) into uniform bounds for all fixed spatial derivatives of B, partial_h B, and partial_h^2 B. Thus joint spatial analyticity and C_h^2 regularity are genuinely available.

For clarity, consider the generic factor

$$
\mathcal A(s,z)=B_{\alpha s^2}(t_*,z_0+sz),
$$

where alpha is fixed, z_0 ranges over the real plane, and z ranges over a fixed bounded complex set fitting inside the strip for small s. Put B_0 = B_{h=0}, B_1 = (partial_hB_h)_{h=0}. Taylor's theorem in h with a bounded second derivative gives

$$
B_{\alpha s^2}(w)=B_0(w)+\alpha s^2B_1(w)+O(s^4)
$$

uniformly in the spatial analytic norm. Spatial Taylor expansion then yields

$$
\mathcal A(s,z)=B_0(z_0)+s\,DB_0(z_0)z
$$

$$
\quad+s^2\left(\tfrac12D^2B_0(z_0)[z,z]+\alpha B_1(z_0)\right)
$$

$$
\quad+s^3\left(\tfrac16D^3B_0(z_0)[z,z,z]
+\alpha DB_1(z_0)z\right)+O(s^4).
\tag{32}
$$

The remainder is uniform on that complex set, and hence in the corresponding H-infinity or S_1 supremum norm used in a local rescaling. Spatially analytic phase and prefactor factors can be expanded and multiplied with (32), provided their own stated uniform bounds hold. This is the route to a statement K_0+sK_1+s^2K_2+s^3K_3+O_{S_1}(s^4). It does not require, and this audit does not claim, a uniform C_s^4 bound for the full rescaled kernel.

## 11. Explicit audit cautions

The proof succeeds with the following distinctions kept explicit:

1. Real h gives horizontal shifts. The argument must not silently replace this by unrestricted complex h in a fixed disk common to arbitrarily many compositions.
2. The phase has its own reserved strip gap. Its second and higher derivatives do not consume the amplitude's shrinking gap.
3. Complex exponential differences require control of imaginary parts. The interpolation preceding (13) supplies that control uniformly over the unbounded real plane.
4. Removable quotients alone do not establish a uniform exact amplitude. The convergent estimates (22)-(24) do, and in particular prove the required actual h derivatives.
5. Exact identification uses a bounded fixed-h equation after factoring the original quadratic phase. It does not follow merely from matching a formal expansion.
6. This is an exact one-step lemma at the specified short time. Claims for all iterates require their own finite-trace and composition arguments.

Within this scope, the proposed amplitude lemma has no remaining analytic obstruction identified by this audit.
