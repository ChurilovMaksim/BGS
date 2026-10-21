> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round12_2026_10_21/r12_full_product_audit_kick_recurrence.md`. Embedded SHA256: `3adbcfce53afb2f80a5de60dc88c1db51b087a21394c850ba6350aa4e5900ac5`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/approximation.md).

# Independent audit of the Round 12 bounded-time kick theorem

Date: 21 October 2026. Auditor: r12_full_product.

## Scope and outcome

Audited source, read completely with the clipped middle recovered by a
separate read of lines 285--450:

research_round12_2026_10_21/r12_countersequence_kick_recurrence.md

SHA-256:
7bb8b677cdee6f7a0a94f1d20833aec3069200056de5d6c587c365bbb89e8e1e.

The companion exact-coefficient script was read, not re-executed here:

research_round12_2026_10_21/r12_countersequence_exact_check.py

SHA-256:
1b55b94e3ccad1b4494516dc1db012402f82216eca19739222b4517b6bd20268.

**Outcome:** the displayed proof establishes, for every fixed finite
$T>0$, constants $C_T,c_T>0$ such that

$$
|\operatorname{tr}_N e^{itNA_N}|
\le C_T(N|t|)^{-c_T},
\quad 0<|t|\le T,\quad N|t|\ge1,
$$

for every odd dimension. The spectral Haar convergence and the limiting
minimal operator-norm distance $2$ from scalar unitaries follow as stated.
No proof of the original $H_{\rm diag}$ or admissible countersequence is
contained in this result. The source expressly identifies the general
method and nilpotent shear as earlier work; that restriction is appropriate.

## 1. Quantization and signs

The modular-half correction is essential and is retained. Passing to
ordinary-half Weyl operators multiplies the original coefficient at
$(k,l)$ by $(-1)^{kl}$. It leaves the $l=0$ part unchanged and replaces
$r(q)$ by $r(q+1/2)$ in the $l=\pm1$ part. Thus the source uses the
actual matrix $A_N$, not a different symbol.

For
$\Omega(v,w)=lk'-kl'$, multiplication gives

$$
[W_v,W_w]=2i\sin(\pi\Omega(v,w)/N)W_{v+w}.
$$

Also $\{e_v,e_w\}=4\pi^2\Omega(v,w)e_{v+w}$ with the source's
$\{a,b\}=a_qb_p-a_pb_q$. Therefore

$$
iN[Q_N(a),Q_N(b)]+\frac1{2\pi}Q_N(\{a,b\})
$$

has Fourier coefficients bounded by a constant times
$N^{-2}|\widehat a(v)\widehat b(w)|\,|\Omega(v,w)|^3$.
The stated $O(N^{-2}|b|_3)$ commutator error is valid. It corresponds
to the vector field $(a_p,-a_q)/(2\pi)$, hence to the stated
$E_N(t)Q_N(b)E_N(t)^*$ convention.

The scalar inequality for $\sin x-x$ holds on the whole real line,
so this argument does not discard large integer labels or assume that
the Weyl phases are small for every Fourier mode.

## 2. Fixed points and uniform finite order

At $q=0$ the original corrected symbol has

$$
a=9/10,\quad da=0,\quad a_{pp}=a_{pq}=0,\quad
a_{qq}=-\frac{2\pi^2}{25}(1960-\cos(2\pi p-\alpha_0))<0.
$$

These expressions can also be checked without the script:
$r''(0)=392\pi^2$, $(r(q+1/2))''|_{q=0}=8\pi^2$, and
$(\cos14\pi q)''|_{q=0}=-196\pi^2$; the $r(q)\sin2\pi q$
term has zero second derivative at zero.

Every point on this critical circle is fixed. The linearized
Hamiltonian vector field has a nonzero square-zero matrix $L(p)$,
so its flow derivative is exactly $I+tL(p)$. Consequently
$\kappa_t\ne I$ for every nonzero $t$, without a small-time truncation.

For the two coordinate characters, the divided displacement
$d_j(t,z)=(b_j(z)-b_j(\kappa_tz))/t$ extends analytically to $t=0$.
The function $v_t=\sum_j|d_j|^2$ is real analytic. No fiber $v_t$
is identically zero, including the fiber at zero.

At each zero $(t,z)$ some finite **spatial** derivative of $v_t$ is
nonzero. Otherwise the convergent spatial Taylor series and connectedness
of the torus force $v_t\equiv0$. Taking a directional value of the first
nonzero homogeneous derivative gives a direction with a derivative
bounded away from zero on a product neighborhood. A finite such cover
of the compact zero set is valid uniformly for $|t|\le T$.
The one-dimensional divided-difference proof in the source yields the
claimed sublevel power on each spatial slice. This justifies the
uniform exponent $\beta_T>0$; no derivative in $t$ is substituted
for the required spatial derivative.

## 3. Quantum error and variable cutoffs

The Hilbert--Schmidt alias estimate is valid. Terms off the diagonal
$v=w$ in the squared normalized Hilbert--Schmidt norm require
$v-w\in N\mathbb Z^2$. At least one label then has length at least
$N/2$. Its Fourier coefficient tail is bounded by
$4N^{-2}|b|_2$. Taking both possible large-label cases gives
$8N^{-2}|b|_2^2$ for the off-diagonal absolute sum. Hence

$$
\|Q_N(b)\|_{\rm HS}/\sqrt N
\le\|b\|_{L^2}+\sqrt8\,N^{-1}|b|_2.
$$

Ordinary-half alias signs do not affect this upper bound. It covers
composite as well as prime odd dimensions.

Egorov is used only for the two fixed characters, with an error
$O_T(|t|N^{-2})$. For a variable $u$, write
$R_j=FB_jF^*-C_j$, where $F=E_N(t)$,
$B_j=Q_N(b_j)$, and $C_j=Q_N(b_j\circ\kappa_t)$. Cyclicity gives
exactly

$$
\operatorname{tr}_N Q_N(u)(B_j-C_j)F
=\operatorname{tr}_N[Q_N(u),B_j]F+
 \operatorname{tr}_NQ_N(u)R_jF.
$$

Thus the source obtains its estimate for $\mu_{N,t}(u d_j)$ without
applying Egorov to an $N$-dependent cutoff. The product error and
commutator error are $O_T(N^{-1}|u|_1)$ before division by $t$,
which proves the stated $O_T((N|t|)^{-1}|u|_1)$ bound.

For $u_j=(1-\chi(v_t/\delta))\overline{d_j}/v_t$, five spatial
derivatives cost at most $\delta^{-6}$, because $v_t\ge\delta$
where this expression is nonzero. Six derivatives of
$\chi(v_t/\delta)$ also cost at most $\delta^{-6}$.
The respective Fourier norms $|u_j|_1$ and $|\chi|_2$ are therefore
bounded as claimed.

The final estimate is

$$
|\operatorname{tr}_NF|
\le C_T\left(\delta^{\beta_T/2}+
                   (N|t|)^{-1}\delta^{-6}\right).
$$

Choosing $\delta=(N|t|)^{-2/(12+\beta_T)}$ gives
$c_T=\beta_T/(12+\beta_T)>0$. The remaining bounded range of
$N|t|$ is absorbed by the constant. The exceptional finite
dimension $N=7$, where the kick is scalar, does not contradict
the theorem: on $|t|\le T$ it has $N|t|\le7T$, a bounded range.

## 4. Spectral consequences and limits of the assertion

For every fixed integer $m\ne0$, the identity
$E_N(t_N)^m=E_N(mt_N)$ allows the trace theorem on the fixed
interval $|m|T$. All nonzero Fourier coefficients of the
empirical spectral measure tend to zero. Approximation by Fejér
polynomials proves Haar convergence.

Haar convergence implies that every fixed positive-length arc has an
eigenvalue eventually. Taking a finite mesh of arc centers makes this
uniform in the scalar phase $z$. There is then an eigenvalue arbitrarily
close to $-z$, proving
$\inf_{|z|=1}\|E_N(t_N)-zI\|\to2$. This argument is valid even though
$z$ may vary arbitrarily with $N$.

This conclusion concerns one autonomous kick. It does not estimate
the trace of the noncommuting product of its conjugates, and does not
control times of order $N$ for the full $U_N$. Nothing in this audit
asserts otherwise.
