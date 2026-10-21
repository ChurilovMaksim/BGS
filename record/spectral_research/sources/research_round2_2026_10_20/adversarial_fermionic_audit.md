> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_fermionic_audit.md`. Embedded SHA256: `77cc1c98db6ea50e46d1a0792a856f1abc3f742fa9aa1081aec5fd0987469948`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the new pseudo-orbit cancellation

Date: 20 October 2026. Auditor: `/root/all_time_adversarial`.

## Frozen claim and verdict

Audited file:
`research_round2_2026_10_20/fermionic_pseudoorbit_cutoff.md`.

SHA256:
`03173e53d1a10e2c1afad517c48943a5330d43fc4059b80fc0e37d5b1598a9eb`.

**Verdict: proved as written.** I independently reconstructed the repetition phase, Euler multiplicities, exterior coefficient estimate, positive diagonal limit, perturbation bound for its constant, reciprocal diagonal tail, and finite hook identity. No assertion of H_diag or its negation follows, and the audited file expressly makes that distinction.

The strongest newly audited statement is this. For the exact matrices, write c_{n,N} for the coefficient of the exact scalar dynamical determinant and U_N(S) for its finite primitive-subset terms. If

$$
X_{n,N}=\sum_{S\ne T,\ |S|_{\rm length}=|T|_{\rm length}=n}
U_N(S)\overline{U_N(T)},
$$

then, for every fixed B>1, uniformly over integers N+N^{1/50}≤n≤BN,

$$
X_{n,N}=-C_F(\Psi)+O_B(N^{-1})+O(R_1^{-n})
+O(e^{-cN^{1/50}}),
$$

where C_F(Ψ)>0 and

$$
\left|\log\frac{C_F(\Psi)}{7\sqrt2/16}\right|<10^{-51}.
$$

The paired objects are finite subsets of primitive orbits. They are not the single periodic-orbit terms in a power trace. In particular, this is a genuine signed cancellation for a different functional, not a proof of the original pair statistic.

## 1. The odd-lattice character is compatible with repetition

Let n be the winding of one primitive block of length d. If w_r is the winding after r blocks, the next total winding is n+v, where v=L^d w_r. Direct summation of the generating-function deck law gives the change of the uncorrected edge sum

$$
v_p(q_0+n_q)-(w_r)_p q_0+
\frac{v_pv_q-(w_r)_p(w_r)_q}{2}.
$$

Subtracting the boundary terms of the old, added, and new paths leaves

$$
S_{r+1}=S_r+S_1+\frac{n_qv_p-n_pv_q}{2}.
$$

Put χ(w)=(-1)^{w_qw_p}, σ(n,v)=n_qv_p−n_pv_q. Then

$$
\chi(n+v)=\chi(n)\chi(v)(-1)^{\sigma(n,v)},
\qquad\chi(v)=\chi(w_r)
$$

because L≡I mod 2. The action contributes (-1)^{Nσ(n,v)}. Since N is odd, the two signs cancel. Thus the complete phase satisfies ω_{rd}=ω_d^r. The metaplectic factor ζ_N^{rd}, the λ^{-rd/2} factor, and the scalar cocycle cycle also multiply under repetition. This proves the exact primitive weight identity, with no missing sign or square root.

Every primitive orbit of period d gives exactly d points in Fix Ψ^{rd}. Therefore

$$
\mathcal P_{m,N}=\sum_{d_p\mid m}d_p u_{p,N}^{m/d_p},
$$

and consequently

$$
\mathcal Z_N(z)=\prod_p(1-u_{p,N}z^{d_p})
$$

in its initial absolute-convergence disk and as a formal coefficient identity. Every fixed coefficient is a finite sum. No convergence of that infinite product at the exterior radius used below is asserted or needed; its analytic continuation comes from the exact determinant identity.

## 2. The exterior estimate genuinely beats the binomial bound

The established all-time estimates imply

$$
|p_{m,N}|\le3\min(N,a^m),\qquad
a=\sqrt\lambda\,1.0002,
$$

and

$$
\mathcal Z_N(z)=D_N(z)e^{G_N(z)},\quad
D_N(z)=\det(I-zU_N),\quad
|e^{G_N(z)}|\le(1-q|z|)^{-2},\quad q=0.421.
$$

A bound by (1+|z|)^N for D_N would leave an exponential-in-N factor, and would not prove a cutoff only N^{1/50} beyond N. The audited argument instead uses unitarity to factor the polynomial outside the unit circle:

$$
D_N(z)=(-z)^N\det(U_N)\det(I-z^{-1}U_N^*).
$$

For |z|=R>1, the logarithm of the last determinant has an absolutely convergent trace series. Hence

$$
|D_N(z)|\le R^N\exp\left(\sum_{m\ge1}\frac{|p_{m,N}|}{mR^m}\right).
$$

For 1<R<q^{-1}<a, split this sum at J=floor(log_a N). The part m≤J is a geometrically increasing sum of (a/R)^m/m and is bounded by C_R(a/R)^J/J. The tail is bounded by C_R N R^{-J}/J. Both are at most

$$
C_R\frac{N^{\kappa_R}}{\log N},\qquad
\kappa_R=1-\frac{\log R}{\log a}.
$$

Cauchy's coefficient estimate now gives

$$
|c_{N+s,N}|\le(1-qR)^{-2}R^{-s}
\exp(C_RN^{\kappa_R}/\log N).
$$

For R=19/8, qR=7999/8000<1. Moreover a<483/200 and the exact rational comparison

$$
(19/8)^{50}>(483/200)^{49}
$$

gives κ_R<1/50. That comparison was independently checked in exact rational arithmetic; it is only a check of a displayed fixed numerical inequality. Since N^{κ_R}/log N=o(N^{1/50}), the asserted exponential decay follows uniformly for every s≥N^{1/50}. The prefactor (1−qR)^{-2}=64,000,000 is fixed and is harmless after increasing the common N threshold.

The sharper replacement estimate for squared power traces is valid for the same reason: the error is bounded by a constant times

$$
N^{-2}\sum_mq^m\min(N,a^m)+O(N^{-2}),
$$

which is O(N^{-2+κ_*}), κ_*=1+log q/log a<1/50. This is a replacement-error estimate, not an estimate of the principal power-trace correlations.

## 3. The positive diagonal and its analytic radius

Let

$$
A_m=\sum_{\operatorname{Fix}\Psi^m}\Lambda_m^{-1},\qquad
B_m=\sum_{\operatorname{Fix}\Psi^m}\Lambda_m^{-2}.
$$

I additionally reread the proof of the classical trace input. Its analytic Fourier-weighted operator is trace class, the nonconstant block has operator norm at most θ=1−1/8000, and its trace is rigorously identified with

$$
Q_m=\sum_{\operatorname{Fix}\Psi^m}
\frac{\Lambda_m^{-1}}{(1-\Lambda_m^{-1})^2}.
$$

The identification is made through finite Fourier projections and then a positive heat kernel; it does not rely on a formal unbounded similarity. Thus Q_m=1+O(θ^m) is available. Since Λ_m≥5^m,

$$
0\le Q_m-A_m\le C5^{-m}Q_m,
\qquad 0\le B_m\le5^{-m}A_m.
$$

It follows that A_m−1=O(θ^m) and B_m=O(5^{-m}).

The identical-subset generating function at h=0 is

$$
F_0(t)=\prod_p(1+\Lambda_p^{-1}t^{d_p}).
$$

Applying 1+x=(1−x²)/(1−x) primitive orbit by primitive orbit gives

$$
\log F_0(t)=\sum_{m\ge1}\frac{A_m}{m}t^m
-\sum_{m\ge1}\frac{B_m}{m}t^{2m}.
$$

In particular, the second series is evaluated at t^{2m}; replacing it by t^m before extracting coefficients would be wrong. Factoring the pole yields

$$
F_0(t)=\frac{e^{H_F(t)}}{1-t},\quad
H_F(t)=\sum\frac{A_m-1}{m}t^m-\sum\frac{B_m}{m}t^{2m}.
$$

The available analytic radius is exactly any disk strictly inside
min(θ^{-1},√5), which is larger than one. This suffices for

$$
[t^n]F_0(t)=e^{H_F(1)}+O(R_1^{-n})
$$

for each fixed 1<R_1<min(θ^{-1},√5). It does not require regularity in the base variable of the exact quantum scalar γ_h.

The exact finite-h primitive modulus differs by an exponent of absolute value at most C d_p h². For any subset of total length n, its total exponent is therefore at most Cnh². Since diagonal coefficients are nonnegative, coefficientwise comparison gives

$$
e^{-Cnh^2}[t^n]F_0\le F_{n,N}\le e^{Cnh^2}[t^n]F_0.
$$

This proves the uniform n≤BN estimate directly. No Fourier-window uniformity or sign cancellation is used in this positive comparison.

## 4. The value and stability of C_F

For the unperturbed map, A_m=(1−ρ^m)² and B_m=ρ^m(1−ρ^m)². Hence

$$
\log C_F(L)=\sum_{m\ge1}\frac{3\rho^{2m}-3\rho^m-\rho^{3m}}m
$$

and

$$
C_F(L)=\frac{1-\rho^3}{(1+\rho)^3}=\frac{7\sqrt2}{16}.
$$

One can check the last simplification without approximations: 1+ρ+ρ²=7ρ, (1+ρ)²=8ρ, and (1−ρ)/(1+ρ)=1/√2.

For the actual map, the claimed relative logarithmic error also passes the audit. The trace-class perturbation has norm below η=10^{-56}. On the complement of constants both old and new operators have norm at most θ. Telescoping their powers gives

$$
|Q_m-1|\le m\eta\vartheta^{m-1},\qquad
\sum_m |Q_m-1|/m<8000\eta.
$$

The invariant slope cone of width δ=10^{-70} gives an unstable first-coordinate factor between λ−2δ and λ+2δ. On a closed orbit these coordinate factors multiply to the unstable eigenvalue, so |logΛ_m−m logλ|≤δm.

Put c(x)=x/(1−x)²−x+x². On [0,1/5], c'(x)≤10x. The identity

$$
A_m-1-B_m=Q_m-1-\sum_{\operatorname{Fix}\Psi^m}c(\Lambda_m^{-1})
$$

is exact. It is the useful cancellation in the comparison: a direct comparison of A_m and its unperturbed value with no decay would not be summable. The multiplier estimate and equal fixed-point counts give a summable bound

$$
10\delta m\lambda^{-m}e^{2\delta m}
$$

for the difference of the c-sums. After division by m and summation this is below 3δ. Therefore

$$
|\log(C_F(\Psi)/C_F(L))|
<8000\cdot10^{-56}+3\cdot10^{-70}<10^{-51}.
$$

This verifies both the numerical comparison and the absence of a hidden nonsummable perturbation series.

## 5. What the signed cancellation proves

The elementary finite identity

$$
|c_{n,N}|^2=F_{n,N}+X_{n,N}
$$

combined with the coefficient cutoff proves the stated full different-subset cancellation. This genuinely takes the modulus after the complete subset sum. It does not take the modulus term by term and it does not assume independence of orbit phases.

Its limit is a negative constant because the positive identical-subset contribution has a nonzero limit while the full coefficient tends to zero. This is an actual deterministic identity plus estimates. However, finite-dimensional unitary determinant truncation is itself compatible with many non-CUE spectra, so this cancellation alone cannot distinguish the desired local process.

## 6. Reciprocal coefficients and the correctly exposed remaining gap

The reciprocal Euler expansion is over multisets. Its identical-multiset generating series is

$$
\prod_p(1-|u_{p,N}|^2t^{d_p})^{-1}.
$$

At h=0 its logarithm is Σ A_m t^m/m. The same analytic and positive-coefficient arguments give C_B(L)=(1−ρ)/(1+ρ)=1/√2 and the stated perturbation bound for C_B(Ψ).

The whole diagonal sum at radius e^{-s/N} is also controlled. The coefficientwise upper bound remains valid for every n, with a factor e^{Cnh²}. For large N,

$$
e^{-2sn/N}e^{Cnh^2}\le e^{-sn/N}.
$$

Since the limiting positive coefficients are bounded, the normalized tail after BN is O_s(e^{-sB}). This justifies the full-diagonal limit, including its infinite tail.

None of this estimates the actual reciprocal Parseval sum: different multisets have cross terms. The reciprocal has poles precisely at the quantum spectral points on the unit circle, because its remaining factor is nonzero analytic. Thus applying exterior Cauchy estimates to the reciprocal would be invalid. The audited note explicitly stops before making that error.

Finally, the hook identity is algebraically correct. Summing its finite alternating definition produces the logarithmic derivative of D_N; coefficients with r≥N vanish by D_ND_N^{-1}=1. This yields exactly min(m,N) terms but supplies no orthogonality of those terms. A common angular shift multiplies all degree-m terms by one common scalar and cannot provide the missing covariance estimate.

## Remaining original assertion

No new hypothesis is being inserted into the original problem. The first unresolved original estimate is still the weighted pair form factor for a fixed admissible b, and all higher H_diag statements remain beyond what is established here.
