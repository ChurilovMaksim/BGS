> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round13_2026_10_21/orbit_correlations/protected_actions_and_one_step_trace.md`. Embedded SHA256: `6bbde35d4fb3873976d6182b3fb6d9cc969349a3a6ce78e7b9dc48cf480c9fe6`.
> [Thematic guide](../../../topics/classical_trace.md).

# Protected action coincidences and the actual one-step quantum trace

21 October 2026. Round 13, orbit-correlation branch.

## 0. Status and provenance

The original all-odd-dimensional, fixed-parameter `H_diag` is not proved or disproved here. This note tests action nonresonance for the original map and follows the protected cycles into an actual quantum trace calculation. The two equilibrium lines, marked Hessians and multiplier nonlattice results are old Round 2 results. The present additions are the complete sixteen-point action table, an explicit one-step trace asymptotic, and an estimate removing this particular protected principal-orbit set from the pair functional. No literature priority is asserted.

Base master SHA-256: `10b90c7d12668cd7327bcc08bda292f4c7d6cf82218ee95d5d4f7603fac86cef`.

| Internal proved input | SHA-256 | Material used |
|---|---|---|
| `research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` | Hamilton–Jacobi construction; exact one-step kernel; uniform real-h derivatives; principal amplitude, §§2–8 |
| `research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` | Exact modular normalization and symbol, §§2–5; sector identity and Abel interpretation, §§7–9 |
| `research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` | Previously proved uniform modulus formula (9.6), used only in §7 |
| `research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` | Positive unstable multipliers at least 5^m; exact fixed-point count; principal orbit weights |
| `research_round2_2026_10_20/root_fixed_point_multipliers.md` | `42e52ff202f56182f1ac8314fcca9d668d207c59217738a06eb2f162e9d6824a` | Marked Hessians, independently recomputed below |
| `research_round2_2026_10_20/root_exact_marker_fixed_point.md` | `d1a584f17360ed6067a402249b3835efdfee5c5b8efb2b49d3229c3b0e5e799d` | Nearest old marker result, not claimed new |
| `research_round2_2026_10_20/root_fixed_multiplier_nonlattice.md` | `256352cb8b82452d7346345ab0345fd46b795e04935ecf9389940ac920c25e62` | Nearest old nonlattice result; it concerns multipliers, not actions |

The raw one-step amplitude proof and sector calculations were inspected at the cited steps. The new stationary-phase argument, action table and trace coefficient are derived below. The all-time Gaussian-cocycle proof is not claimed to have been independently reaudited in full in this branch: §7 explicitly applies its already established theorem, whose complete proof is retained in the master. Sections 1–6 do not use that all-time theorem. This read-scope distinction must not be removed in a downstream report.

## 1. Exact conventions

Throughout

$$
\tau=10^{-80},\quad h=(2\pi N)^{-1},\quad t_*={\tau\over2\pi},
\quad L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
\quad\zeta_N=e^{2\pi i(3N-1)/8}.
$$

The ordinary Weyl symbol forced by the modular half in the question is

$$
a(q,p)=V(q)+{r(q+1/2)\over100}\cos(2\pi p-\alpha_0),
\quad V(q)=\cos14\pi q+{r(q)\over10}
+{r(q)\sin2\pi q\over100}-{1\over10}.
\tag{1.1}
$$

Indeed the ordinary Fourier mode quantizes to `(-1)^(kl)T_N(l,k)`. In the mixed terms l=±1, shifting q by 1/2 exactly supplies this sign. The physical map is

$$
\Psi=\phi_{-a}^{t_*}\circ L,\qquad X_{-a}=(-a_p,a_q).
\tag{1.2}
$$

Interpolation in Hamiltonian time below only evaluates the fixed endpoint t_*; the quantum family and its prescribed tau never change.

## 2. Exactly sixteen protected points

Let

$$
\mathcal L=\{(q,p):q=0\text{ or }q=1/2\},\qquad
\mathcal P=\{0,1/2\}\times\{j/8:0\le j<8\}.
$$

**Proposition 2.1.** The maximal invariant subset of mathcal L for the actual map Psi is exactly mathcal P. On that set Psi=L, and every point has period dividing two.

**Proof.** At q=0,1/2 both r(q) and r(q+1/2), and their first derivatives, vanish. The first derivatives of the remaining cosine also vanish. Thus da=0 on mathcal L, and its points are fixed by the Hamiltonian flow at every time.

If z and Psi z both belong to mathcal L, applying the inverse kick to Psi z leaves that point unchanged. Hence Lz=Psi z belongs to mathcal L. For q=0,1/2, the condition `3q-4p in (1/2)Z mod 1` is equivalent to `p in (1/8)Z mod 1`. Every full invariant subset of mathcal L is therefore contained in mathcal P.

Conversely, modulo one,

$$
L(q,j/8)=(q-j/2,3j/8).
\tag{2.1}
$$

This belongs to mathcal P. After two steps the first coordinate changes by -2j and the second is 9j/8=j/8 modulo one. The kick fixes each image, proving invariance and Psi²=I on mathcal P. Fixed points have j=0,4, giving four fixed points. The twelve others form six two-cycles. QED.

This does not classify periodic points outside mathcal L or supply a symmetry of the full nonlinear map.

## 3. Exact action phases with the odd-dimensional deck factor

For the graph Psi, use the Hamilton–Jacobi normalization

$$
F_t(Q,q)=F_0(Q,q)+G_t(Q,q),\quad
F_0(Q,q)=-{3Q^2-2Qq+3q^2\over8},
$$
$$
\partial_tF_t=a(Q,\partial_QF_t),\qquad
p=-\partial_qF_t,\quad P=\partial_QF_t.
\tag{3.1}
$$

Suppose an edge starts at a protected lifted point z=(q,p), with Lz=(Q,P). The entire Hamiltonian characteristic from this image is constant, since its image is on an equilibrium line. The characteristic action integral is the integral of `P dot Q+a`, and therefore

$$
F_{t_*}(Q,q)=F_0(Q,q)+t_*a(Q,P)
\tag{3.2}
$$

exactly, with no discarded tau² term.

For a protected primitive orbit of period d, lift its successive points as z_j=L^j z_0 and write z_d=z_0+n, with integral n=(n_q,n_p). The exact sector factor is

$$
(-1)^{n_qn_p}\exp\!\left[{i\over h}
\left(\sum_{j=0}^{d-1}F_{t_*}(q_{j+1},q_j)
-n_p(q_0+n_q/2)\right)\right].
\tag{3.3}
$$

For odd N,

$$
(-1)^{n_qn_p}e^{-in_pn_q/(2h)}
=e^{i\pi(1-N)n_qn_p}=1.
$$

Combining with (3.2), this factor is

$$
\boxed{\omega_{d,N}=e^{2\pi iNB}e^{i\tau NC}},
\tag{3.4}
$$
$$
B=\sum_{j=0}^{d-1}F_0(q_{j+1},q_j)-n_pq_0\pmod1,
\qquad C=\sum_{j=0}^{d-1}a(q_{j+1},p_{j+1}).
\tag{3.5}
$$

The two constant values are

$$
a(0,p)=9/10,\qquad a(1/2,p)=-11/10.
\tag{3.6}
$$

The complete orbit table is:

| Primitive orbit, torus representatives | d | B mod 1 | C |
|---|---:|---:|---:|
| (0,0) | 1 | 0 | 9/10 |
| (0,1/2) | 1 | 1/2 | 9/10 |
| (1/2,0) | 1 | 3/4 | -11/10 |
| (1/2,1/2) | 1 | 3/4 | -11/10 |
| (0,1/8) → (1/2,3/8) | 2 | 13/16 | -1/5 |
| (0,7/8) → (1/2,5/8) | 2 | 13/16 | -1/5 |
| (0,3/8) → (1/2,1/8) | 2 | 5/16 | -1/5 |
| (0,5/8) → (1/2,7/8) | 2 | 5/16 | -1/5 |
| (0,1/4) → (0,3/4) | 2 | 1/4 | 9/5 |
| (1/2,1/4) → (1/2,3/4) | 2 | 3/4 | -11/5 |

Each entry follows from the explicit rational polynomial (3.5). For z=(1/2,0), Lz=(3/2,-1), n=(1,-1), F_0(3/2,1/2)=-3/4, and B=-3/4+1/2=-1/4. For z=(1/2,1/2), Lz=(-1/2,1/2), n=(-1,0), and B=F_0(-1/2,1/2)=-1/4. Thus this equality holds before reducing modulo one.

For the two-cycle starting at (0,1/8), the lifted successive points are (-1/2,3/8) and (-3,17/8). The winding is (-3,2). The two F_0 terms sum to -51/16, of residue 13/16, and C=-11/10+9/10=-1/5. The other rows follow by the same two explicit substitutions; the companion exact-rational enumerator records the full calculation for all sixteen points and every choice of their starting points.

**Consequence.** Distinct primitive orbits have identical classical action holonomy for every odd N at the original fixed tau. A blanket assumption of pairwise independent primitive action phases is false for this family. Their full h-dependent amplitudes have not been identified with one another: the monodromy and scalar cocycle must still be retained.

## 4. The global one-dimensional stationary-phase step

**Lemma 4.1.** Let s be a strictly concave quadratic plus a bounded smooth function with bounded fixed derivatives, with s''≤-c<0, and critical point q_*. Let b_h have uniformly bounded fixed spatial derivatives and satisfy b_h=b_0+O(h) in those norms. Then

$$
\lim_{\epsilon\downarrow0}\int e^{-\epsilon q^2}
 e^{is(q)/h}b_h(q)dq
=e^{is(q_*)/h-i\pi/4}\sqrt{2\pi h\over|s''(q_*)|}
\bigl(b_0(q_*)+O(h)\bigr).
\tag{4.1}
$$

**Proof.** Choose a smooth compact cutoff equal to one near q_*. Off its support, s' is bounded away from zero and grows linearly at infinity. Twice integrating by parts with `(h/(is'))d/dq` gives an O(h²) tail. After two adjoint derivatives the worst decay is a bounded derivative of b_h times O((1+|q|)^-2), so every term is integrable. First use expanding compact cutoffs; their differentiated tails tend to zero. Gaussian damping gives the same limit: its differentiated terms contain epsilon or epsilon²q² multiplied by inverse powers of s', and a split at |q|=epsilon^-1/2 shows that the resulting integrals tend to zero. Thus the Abel interpretation has the same tail estimate.

In the fixed neighborhood use the smooth Morse coordinate

$$
u=\operatorname{sgn}(q-q_*)\sqrt{2(s(q_*)-s(q))}.
$$

Its derivative at q_* is sqrt(|s''(q_*)|). The localized integral is a compactly supported smooth amplitude g_h(u) times exp(-iu²/(2h)). Fourier inversion and the damped Gaussian integral give

$$
\int e^{-iu^2/(2h)}g_h(u)du
=e^{-i\pi/4}\sqrt{2\pi h}\bigl(g_h(0)+O(h)\bigr).
$$

Indeed the transformed Gaussian multiplier differs from its value at zero by at most a constant times h xi², and the error is bounded by `Ch ∫xi² |g_hat_h(xi)| dxi`. Four bounded derivatives and fixed compact support make this integral uniformly finite. Finally `g_h(0)=b_0(q_*)/sqrt(|s''(q_*)|)+O(h)`. The O(h²) tail is smaller than the O(h^(3/2)) local error. QED.

This lemma is used only for one iterate. It does not give a growing-dimensional stationary-phase estimate.

## 5. Complete asymptotic formula for the original one-step trace

Set

$$
v={\pi\tau\over125}>0,
\quad T_{00}=6+39212v,\quad T_{01}=6+39188v,
\quad T_{10}=6-48612v,\quad T_{11}=6-49788v,
\tag{5.1}
$$

and the fixed constants

$$
\mathsf A=(T_{00}-2)^{-1/2}-(T_{01}-2)^{-1/2}<0,
\quad\mathsf B=(T_{10}-2)^{-1/2}+(T_{11}-2)^{-1/2}>1.
\tag{5.2}
$$

**Theorem 5.1.** Through all odd dimensions for the specified original matrices,

$$
\boxed{\operatorname{Tr}U_N
=\zeta_N\left[\mathsf A e^{i(9/10)\tau N}
+\mathsf B e^{-i\pi N/2}e^{-i(11/10)\tau N}\right]+O(N^{-1}).}
\tag{5.3}
$$

The error constant is finite and independent of N, at the fixed prescribed tau.

**Proof.** The exact plane kernel and principal amplitude are

$$
K_V(Q,q)={e^{i\pi/4}\over\sqrt{8\pi h}}e^{iF(Q,q)/h}B_h(Q,q),
\qquad B_h=2\sqrt{F_{Qq}}+O(h)
\tag{5.4}
$$

in every fixed derivative norm needed in Lemma 4.1. This is the exact amplitude theorem, not an identification modulo an unknown quantum remainder. The ordinary symbol (1.1) descends exactly to A_N, and the plane metaplectic operator descends to zeta_N^-1 M_N; the descended V is therefore zeta_N^-1 U_N.

There are exactly four classes in Z²/(L-I)Z². The exact finite-sector identity and its Abel interpretation give

$$
\zeta_N^{-1}\operatorname{Tr}U_N
=\sum_{[n]}(-1)^{n_qn_p}{e^{i\pi/4}\over\sqrt{8\pi h}}
\int_{\rm Abel}e^{i\psi_n(q)/h}B_h(q+n_q,q)dq,
\tag{5.5}
$$
$$
\psi_n(q)=F(q+n_q,q)-n_p(q+n_q/2).
$$

For clarity about (5.5), its proof precedes use of the amplitude representation. Expand exp(it_*A_h/h) into translated metaplectic words. Their coefficient sum is finite for each fixed h. Each translated word has an absolutely integrable coherent Gaussian diagonal, with integral independent of the translation. Grouping the integer lattice into cosets of (L-I)Z² tiles the plane once per coset, with no determinant multiplier. Gaussian integration then identifies each coherent sector with its Abel diagonal integral, uniformly bounded in each translation, permitting the word series to be summed. The complete normalization and all these exchanges are proved in the cited internal source §§7–8. No assertion for a growing iterate is used here.

The unperturbed second derivative of psi_n is -1. The second derivatives of G are much smaller than 1/2; hence every sector is strictly concave and has one critical point. The four known fixed points represent different sectors: otherwise an integer change of lift would give two critical points in one strictly concave sector. Consequently they account for all four stationary points of (5.5).

Write J=F_Qq>0 and D=D Psi at a critical point. Differentiating the two generating equations gives

$$
Q_p=-J^{-1},\quad Q_q=-F_{qq}/J,\quad P_p=-F_{QQ}/J,
\quad\operatorname{Tr}D=-{F_{qq}+F_{QQ}\over J}.
$$

It follows that

$$
\psi_n''=F_{QQ}+2F_{Qq}+F_{qq}=J(2-\operatorname{Tr}D)<0.
\tag{5.6}
$$

The kernel prefactor, stationary-phase factor and amplitude combine to

$$
{e^{i\pi/4}\over\sqrt{8\pi h}}e^{-i\pi/4}
\sqrt{2\pi h\over|\psi_n''|}\,2\sqrt J
=(\operatorname{Tr}D-2)^{-1/2}.
\tag{5.7}
$$

Thus the four coefficients are positive, with their relative Maslov factors explicitly computed.

Here are the exact derivative traces. Direct differentiation gives

$$
r''(0)=392\pi^2,\quad r''(1/2)=8\pi^2,
\quad V''(0)=-784\pi^2/5,\quad V''(1/2)=984\pi^2/5.
$$

At each of the four fixed points a_pp=a_qp=0. Inserting cos(alpha_0)=-3/5 and cos(pi-alpha_0)=3/5 into (1.1),

$$
a_{qq}(z_{00},z_{01},z_{10},z_{11})
={\pi^2\over125}(-19606,-19594,24306,24894).
$$

The linearized kick is exactly I+t_*DX_-a, since DX_-a is square-zero and the trajectory is constant. Therefore

$$
D\Psi(z)=\begin{pmatrix}1&0\\t_*a_{qq}(z)&1\end{pmatrix}L,
\qquad\operatorname{Tr}D\Psi(z)=6-4t_*a_{qq}(z),
$$

giving (5.1) without a tau² remainder. Section 3 gives the corresponding phase factors

$$
e^{i(9/10)\tau N},\quad -e^{i(9/10)\tau N},\quad
 e^{-i\pi N/2}e^{-i(11/10)\tau N},\quad
 e^{-i\pi N/2}e^{-i(11/10)\tau N}.
$$

The equality e^(2 pi i N·3/4)=e^(-i pi N/2) uses integral N. Summing (5.7) with these phases proves (5.3). Each of the four sectors has an O(h) error after its prefactor by Lemma 4.1 and (5.4), giving O(N^-1) in total. QED.

As a normalization check, at tau=0 the expression reduces to `Tr M_N=zeta_N exp(-i pi N/2)`, exactly agreeing with the odd quadratic Gauss sum. This check is not a substitution of tau=0 in the argument for the prescribed nonzero parameter.

## 6. Strict fixed-time lower bound and its limited scope

The mean-value theorem on [4,infinity) gives

$$
|\mathsf A|\le24v/16=3v/2.
$$

Convexity of (4-x)^(-1/2) for 0≤x<4 gives

$$
\mathsf B\ge1+(48612+49788)v/16=1+6150v.
$$

The required inequality 49788v<4 follows directly from tau=10^-80 and pi<4. Thus (5.3) implies

$$
\boxed{\liminf_{\substack{N\to\infty\\N\ {\rm odd}}}
|\operatorname{Tr}U_N|\ge\mathsf B-|\mathsf A|
\ge1+{12297\pi\over250}\tau>1.}
\tag{6.1}
$$

No density theorem for an irrational rotation is needed for this lower bound. The normalized trace still tends to zero. More importantly, the single m=1 term in the original pair functional is

$$
N^{-2}w(1/N)(|\operatorname{Tr}U_N|^2-1)=O_w(N^{-2}),
\tag{6.2}
$$

since (5.3) bounds the unnormalized trace. The strict excess in (6.1) disappears under the required normalization and does not give the fixed epsilon or infinite countersequence required by the problem.

## 7. Removing the complete protected principal-orbit family

This section uses the previously proved all-time theorem, not the fixed-time lemma of §4. For its exact principal weights write

$$
\mathcal A_{m,N}(x)=\zeta_N^m\omega_{m,N}(x)
\lambda^{-m/2}\Gamma_h(x,m),\qquad\lambda=3+2\sqrt2.
$$

The established modulus formula (9.6) of the Gaussian-cocycle input and the cone bound Lambda_m≥5^m give

$$
|\mathcal A_{m,N}(x)|\le e^{Cmh^2/2}5^{-m/2}.
\tag{7.1}
$$

Define

$$
Q_{m,N}=\sum_{x\in\mathcal P\cap\operatorname{Fix}\Psi^m}
\mathcal A_{m,N}(x).
\tag{7.2}
$$

This retains the full h-dependent scalar cocycle, rather than identifying it with the classical holonomy of §3. There are at most sixteen starting points, including every point on each eligible orbit. For any fixed B_0<infinity, (7.1) therefore gives

$$
|Q_{m,N}|\le C_{B_0}5^{-m/2},\qquad1\le m\le B_0N,
\tag{7.3}
$$

through all sufficiently large odd N. Put R_m=p_m-Q_m, where p_m=Tr U_N^m. This is an exact definition, and unitarity gives |p_m|≤N. Hence

$$
\bigl||p_m|^2-|p_m-Q_m|^2\bigr|
\le2N|Q_m|+|Q_m|^2.
\tag{7.4}
$$

For any fixed bounded weight w supported in [0,B_0], summing the geometric bounds in (7.3) proves

$$
\boxed{N^{-2}\left|\sum_{1\le m\le B_0N}w(m/N)
\bigl(|p_m|^2-|p_m-Q_m|^2\bigr)\right|=O_{w,B_0}(N^{-1}).}
\tag{7.5}
$$

Every cross term with all other principal orbits and with the trace residual is included in (7.4). No phase separation or independence of the complement is assumed. This closes the particular counterexample mechanism supplied by the exact protected action coincidences. It does not estimate the remaining full signed sum.

## 8. Exact unresolved original obligation

For the specified fixed admissible b_*, the remaining estimate is still

$$
{1\over N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
\left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)\longrightarrow0.
\tag{8.1}
$$

Equation (7.5) permits replacing p_m by p_m-Q_m in this one test, but no bound giving its limit is proved. Even (8.1) would not replace all orders k and all allowed fixed Fourier bands. This is a concrete obstruction check and a fixed-time original calculation, not a resolution of H_diag or a proof that its resolution is impossible.
