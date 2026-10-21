> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_physical_fixed_powers49.md`. Embedded SHA256: `faf5712f14b5dd4a569627c3271ed58b87667d1955df12a140c302c3dac145eb`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the physical fixed-power theorem through 49

Date: 21 October 2026. Audit task: `/root/r7_physical_audit`.

## 0. Normalized claim and primary verdict

**Primary verdict: proved as written.** This verdict concerns the two fixed-power conclusions below, at the prescribed positive fixed kick, for all odd dimensions tending to infinity. No restriction to coprime dimensions or a subsequence is needed. No gap was found in the raw proof or in its sampled oscillatory dependency.

The authoritative definition is `research_round6_2026_10_21/round6_main_report.md`, §1. For odd integers $N\ge3$, the original operators are

$$
(T_N(l,k)\psi)(x)=e_N\bigl(k(x+2^{-1}l)\bigr)\psi(x+l),
\qquad
(M_N)_{xy}=N^{-1/2}e_N\bigl(-8^{-1}(3x^2-2xy+3y^2)\bigr),
$$

where both inverses are modular. The matrix $A_N$ is the stated modular Weyl quantization of $f-1/10$, and

$$
U_N=e^{i\tau N A_N}M_N,
\qquad \tau=10^{-80},\qquad
t=\frac{10^{-80}}{2\pi}>0,
\qquad h=\frac1{2\pi N}.
$$

Write

$$
\mathsf S^j=
\begin{pmatrix}3&4\\2&3\end{pmatrix}^{j}
=\begin{pmatrix}a_j&b_j\\c_j&a_j\end{pmatrix},
\quad
L_j=9(a_j+b_j),\quad
\Sigma_R=\sum_{j<R}L_j,\quad
\Lambda_R=\sum_{j<R}L_j^2.
$$

For each **fixed** $R\ge1$ satisfying $51200t\Sigma_R^2\le1$, the audited conclusion is

$$
\bigl\||U_N^R|^{\circ2}-J_N\bigr\|_{\ell^2\to\ell^2}
\le256t\Lambda_R+o_R(1),\qquad N\to\infty\text{ through all odd integers},
\tag{A}
$$

and, for every sufficiently large odd $N$,

$$
\max_{x,y}|U_N^R(x,y)|\le\frac{2\sqrt{b_R}}{\sqrt N}.
\tag{B}
$$

Here the squares are entrywise and $J_N(x,y)=1/N$. The smallness condition holds for every $1\le R\le49$. The finite collection therefore has a common large-$N$ threshold for the bounds in the source, including operator distance at most $1/100$.

The kick is fixed before taking $N\to\infty$. Neither $R=0$, $t=0$, growing $R$, nor an effective value of the large-$N$ threshold is included in this verdict. In particular, setting $t=0$ would remove the nonzero mixed coefficient used below and would not be an admissible reading of this claim.

## 1. Independence, evidence, and dependency graph

The proof was reconstructed from the original matrix definitions, the raw fixed-power note, the raw two-step note, and §1 of the raw round-5 sampled oscillatory proof. Earlier auditor files and their verdicts were not used. The independent check script was written from these definitions and the identities derived in this report; no earlier checker was imported or executed.

The base master SHA-256 was checked and equals the requested value

`3534e4d7aa97c2f8621050248652363c639aeedf723f8b7fe7a971dc01ac2302`.

The dependency chain is:

$$
\begin{gathered}
\text{original modular matrices}
\Longrightarrow \text{exact ordinary-half symbol and covariance}
\Longrightarrow \text{exact staged factorization and image kernel},\\
\text{explicit Fourier bounds and smallness}
\Longrightarrow \text{analytic noncaustic characteristics}
\Longrightarrow \text{full phases, amplitudes, and finite-shift residual},\\
\text{exact sheet translation and one marked Fourier coefficient}
\Longrightarrow \text{nonzero mixed phase for every distinct pair},\\
\text{small rectangular-cycle gradient and sampled }S_4\text{ lemma}
\Longrightarrow \text{cross-sheet operator norms tend to zero},\\
\text{amplitude bound and probability-kernel error}
\Longrightarrow \text{(A) and (B)}.
\end{gathered}
$$

| Obligation | Status | Evidence or implication checked |
| --- | --- | --- |
| Original modular $2^{-1}$, $8^{-1}$ conventions | Passed | Direct generator calculations and the raw ordinary-half phase identity |
| Corrected symbol $a$ and covariance | Passed | Fourier coefficient calculation, raw label parity, exact conjugation |
| Exact image kernel for composite $N$ | Passed | Polynomial intertwiners, scalar commutant, complete Gauss norm |
| Evolution order and Hamiltonian signs | Passed | Exact factorization, direct finite-shift expansion |
| Analytic flow and global inverse graph | Passed | Explicit displacement and variational bounds |
| Full nonlinear deck and translation laws | Passed | Uniqueness with exact additive constants |
| Every distinct sheet has nonzero mixed derivative | Passed | Injective frequency map and exact sheet character |
| Finite-torus wrapped shifts | Passed | Added phases are integers after multiplication by $N$ |
| Column and probability errors without a lost power of $N$ | Passed | Residual, unitary Duhamel, difference of squares |
| Sampled $S_4$ oscillation implication | Passed | Boundary cutoff, exact Poisson factors, summable aliases, analytic zero alias |
| Range through 49 at fixed $t$ | Passed | Exact recurrence and rational upper/lower enclosures of $t$ |
| Uniformity in unbounded $R$, full long-time spectral claim | Out of scope | Neither is an implication of the audited theorem |

The leaves are internal elementary proofs or exact finite arithmetic checks. No unverified external theorem is needed: the analytic zero-set fact and the Poisson identity are both proved in the raw oscillatory source and reconstructed below.

## 2. Reconstruction of the original covariance

Let $L=T_N(1,0)$, $D=T_N(0,1)$, and put

$$
Q_1(x,y)=3x^2-2xy+3y^2.
$$

Direct polynomial subtraction gives

$$
Q_1(x+3,y)-Q_1(x,y-1)=16x+24,
$$

$$
Q_1(x+4,y)-Q_1(x,y)=24x+48-8y.
$$

The first identity says exactly

$$
M_NL=T_N(3,2)M_N,
$$

because multiplying $16x+24$ by the modular $8^{-1}$ gives $2x+3$, while the centered phase of $T_N(3,2)$ is $2x+3$ modulo $N$. The second similarly gives

$$
M_ND=T_N(4,3)M_N.
$$

The finite Gaussian matrix is unitary: the scalar product of two different rows reduces to the complete character sum with coefficient $4^{-1}(x-x')$, which vanishes unless $x=x'\pmod N$. This uses only that $N$ is odd.

The Weyl law is

$$
T_N(l,k)T_N(l',k')
=e_N\bigl(2^{-1}(lk'-kl')\bigr)
T_N(l+l',k+k').
$$

The matrix $\mathsf S$ has determinant one and preserves this alternating form. Since $L,D$ generate all Weyl operators, the two generator identities prove, with these signs and this direction of conjugation,

$$
M_NT_N(l,k)M_N^*
=T_N(3l+4k,2l+3k).
\tag{2.1}
$$

No inverse of three occurs. The ordinary rational $1/8$ has not replaced the modular inverse in this calculation.

For raw integer labels, $2^{-1}=(N+1)/2\pmod N$, so

$$
e_N(k2^{-1}l)=(-1)^{kl}e^{\pi ikl/N}.
\tag{2.2}
$$

Therefore

$$
Q_N(H):=\sum_{k,l}\widehat H(k,l)(-1)^{kl}T_N(l,k)
$$

has the exact ordinary-half shift formula

$$
(Q_N(H)\psi)(x)=
\sum_{k,l}\widehat H(k,l)
e^{2\pi ik(x/N+l/(2N))}\psi(x+l).
\tag{2.3}
$$

All $l=0$ coefficients of the original symbol remain unchanged; the $l=\pm1$ coefficients acquire $(-1)^k$. Thus the actual matrix is $A_N=Q_N(a)$, with

$$
\begin{aligned}
a(q,p)={}&\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}-\frac1{10}\\
&+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0),
\qquad r(q)=(1-\cos14\pi q)(1+\cos2\pi q).
\end{aligned}
\tag{2.4}
$$

The half-period shift is essential. Its omission would change $A_N$.

For the $j$-th conjugation the Fourier label map is

$$
(k,l)\longmapsto(k',l')=(a_jk+c_jl,b_jk+a_jl).
$$

The recurrence gives $a_j$ odd and $b_j,c_j$ even. Consequently $k'\equiv k$ and $l'\equiv l\pmod2$; the ordinary-half signs are identical even when raw labels are much larger than $N$. This proves

$$
M_N^jA_NM_N^{-j}=Q_N(H_j),
\qquad
H_j(q,p)=a(a_jq+b_jp,c_jq+a_jp).
\tag{2.5}
$$

In particular,

$$
U_N^R=e^{itQ_N(H_0)/h}\cdots e^{itQ_N(H_{R-1})/h}M_N^R.
\tag{2.6}
$$

The order in the raw proof is correct: the initial image kernel is acted on first by $H_{R-1}$, then successively down to $H_0$. A classical interpretation with a reversed covariance convention is unnecessary; (2.1)–(2.6) fix the convention directly from the matrices.

## 3. Exact initial image kernel, including noninvertible $b_R\pmod N$

Set $a=a_R,b=b_R,c=c_R$. For $R\ge1$,

$$
a^2-bc=1,\quad b,c\text{ even},\quad a\text{ odd},\quad b>0.
$$

Consider

$$
K_N(x,y)=\frac1{\sqrt{bN}}
\sum_{m=0}^{b-1}
\exp\left[-\frac{2\pi i}{2bN}
\{ax^2-2x(y+mN)+a(y+mN)^2\}\right].
\tag{3.1}
$$

This is an independently defined ordinary exponential sum. Its identification with $M_N^R$ is proved, rather than assumed by changing the original modular denominator.

For $Q(x,Y)=ax^2-2xY+aY^2$, the required polynomial identities are

$$
Q(x+a,Y)-Q(x,Y-1)=bc(2x+a),
$$

$$
Q(x+b,Y)-Q(x,Y)=2b\{a(x+b/2)-Y\},
$$

$$
Q(x+N,Y+aN)-Q(x,Y)=bc(2YN+aN^2).
\tag{3.2}
$$

The first two give $K_NL=T_N(a,c)K_N$ and $K_ND=T_N(b,a)K_N$. The ordinary halves agree with the modular phases here because $ac$ and $ab$ are even. The third gives periodicity in $x$ after reindexing the images. Periodicity under $m\mapsto m+b$, and hence in $y$, follows from

$$
\frac{Q(x,Y+bN)-Q(x,Y)}{2bN}=-x+aY+abN/2\in\mathbb Z.
$$

By (2.1), $M_N^R$ has exactly the same intertwiners. Hence $(M_N^R)^*K_N$ commutes with $L,D$. Commuting with $D$, whose $N$ diagonal roots are distinct, makes it diagonal; commuting with the cyclic shift $L$ makes it scalar. It remains to determine the scalar's modulus.

After removing the unit factor independent of $m$, the sum in (3.1) is

$$
G(C)=\sum_{m=0}^{b-1}
e^{-\pi iaNm^2/b+2\pi iCm/b},\qquad C=x-ay.
$$

In $|G(C)|^2$, set $d=m-n\pmod b$. The sum over $n$ is zero unless $b\mid aNd$. Since $a^2-bc=1$ implies $\gcd(a,b)=1$, this means $d=(b/g)r$, where $g=\gcd(N,b)$ and $0\le r<g$. The remaining quadratic factor is

$$
\exp\bigl[-\pi ia(N/g)(b/g)r^2\bigr]=1.
$$

Indeed $g$ is odd and $b/g$ is even. Thus

$$
|G(C)|^2=b\sum_{r=0}^{g-1}e^{2\pi iCr/g}
=bg\,\mathbf1_{g\mid C},
$$

and therefore

$$
|K_N(x,y)|^2=\frac gN\mathbf1_{g\mid x-ay}.
\tag{3.3}
$$

Each row has exactly $N/g$ permitted columns, because $a$ is invertible modulo $g$. Its squared norm is one. The scalar relating $K_N$ to $M_N^R$ consequently has modulus one, so $M_N^R=\eta_{R,N}K_N$, $|\eta_{R,N}|=1$.

This argument covers every odd $N$, including $N$ divisible by any odd factor of $b_R$. The Gauss support restriction is retained exactly at time zero.

## 4. Quantitative bounds and the fixed range

Expand $r$ with $u=2\pi q$:

$$
r=1+\cos u-\cos7u-\tfrac12\cos6u-\tfrac12\cos8u.
$$

The real $q$-only part of (2.4) has coefficient one-norm $11/10$. Direct multiplication gives

$$
r\sin u=\sin u+\tfrac12\sin2u+\tfrac14\sin5u
+\tfrac12\sin6u-\tfrac12\sin8u-\tfrac14\sin9u,
$$

so its contribution is $3/100$. The Fourier one-norm of $r$ is four. Bounding the modulus of a Gaussian rational by the sum of the absolute values of its real and imaginary parts gives $7/125$ for the $p$-dependent contribution, since $e^{i\alpha_0}=(-3+4i)/5$. Consequently

$$
\sum|\widehat a|\le\frac{11}{10}+\frac3{100}+\frac7{125}
=\frac{593}{500},\qquad |k|+|l|\le9,\quad |l|\le1.
\tag{4.1}
$$

The label map is injective, so it preserves the coefficient one-norm. Since $c_j\le b_j$, transformed labels have $|k'|+|l'|\le9(a_j+b_j)=L_j$.

Put $\delta=(100L_{R-1})^{-1}$. On the phase-space complex tube of width $\delta$, the Fourier exponential is bounded by

$$
e^{2\pi\delta L_j}\le e^{\pi/50}<e^{1/15}\le15/14.
$$

Using $\pi<22/7$, the coefficient factors for the gradient and the row-sum norm of the Hamiltonian Hessian are respectively bounded by

$$
\frac{593}{500}\frac{44}{7}\frac{15}{14}<8,
\qquad
\frac{593}{500}\left(\frac{44}{7}\right)^2\frac{15}{14}<64.
$$

Thus, for every stage,

$$
|H_{j,q}|,|H_{j,p}|\le8L_j,
\qquad \|D(-H_{j,p},H_{j,q})\|_{\infty\to\infty}\le64L_j^2.
\tag{4.2}
$$

The recurrence of $\mathsf S^j$ gives

$$
\Sigma_R=\frac92(a_R-1).
$$

The exact values at the range endpoint are

$$
\Sigma_{49}=73147532610169123199386258094868594249<74\cdot10^{36},
$$

$$
\Sigma_{50}=426335063173366200380428859644050080712>426\cdot10^{36}.
$$

The positive fixed $t$ satisfies

$$
\frac{10^{-80}}7<t<\frac{10^{-80}}6.
$$

The rational upper bound proves

$$
51200t\Sigma_{49}^2
<\frac{51200\cdot74^2}{6\cdot10^8}<\frac12<1.
$$

Monotonicity proves the condition for all earlier powers. The rational lower bound gives

$$
51200t\Sigma_{50}^2
>\frac{51200\cdot426^2}{7\cdot10^8}>1.
$$

Thus 50 is excluded from this sufficient criterion by a genuine lower bound, rather than by failure of an upper-bound test. This does not disprove its physical mixing conclusion.

## 5. The full characteristic construction and its errors

The initial phases and outgoing momenta are

$$
\Theta_m(q,s)=-\frac{aq^2-2q(s+m)+a(s+m)^2}{2b},
\qquad p_m(q,s)=\frac{-aq+s+m}{b}.
$$

On each stage, in the order fixed by (2.6), solve

$$
\dot Q=-H_p(Q,P),\qquad \dot P=H_q(Q,P),
\quad Q(0)=u,\quad P(0)=p_m(u,s).
\tag{5.1}
$$

Define the integrated bounds

$$
\mathcal G=8t\Sigma_R,\qquad \mathcal L=64t\Lambda_R.
$$

The hypothesis and $\Lambda_R\le\Sigma_R^2$ imply

$$
\mathcal L\le1/800,
\qquad \mathcal G/\delta\le1/64.
\tag{5.2}
$$

For complex initial parameters in a sufficiently small fixed fraction of the tube, the initial graph is inside the larger tube because $a/b<1$. The integral equation maps the displacement ball of radius $\mathcal G$ to itself and is a contraction with integrated Lipschitz constant $\mathcal L<1$. Picard iteration therefore supplies the analytic flow uniformly in all real initial coordinates. The piecewise time dependence does not affect analyticity in these parameters.

Differentiating the integral equation, or its finite sequence of stage flows, yields

$$
\|D(Q,P)-I\|_{\infty\to\infty}\le e^{\mathcal L}-1\le2\mathcal L.
$$

The initial graph tangent is $(1,-a/b)$, of maximum norm one. Its position Jacobian $J=\partial_u Q$ consequently satisfies

$$
|J-1|\le2\mathcal L<1/2.
\tag{5.3}
$$

For real $s$, $u\mapsto Q$ is increasing and differs from $u$ by a bounded amount, so it is a global real bijection. The same small derivative gives a local analytic inverse with a uniform complex neighborhood. Uniform periodicity and the finite analytic bounds give every fixed derivative needed later.

At the inverse coordinate $u=u(q,s,m)$, define the full real action and amplitude by

$$
\Phi_m=\Theta_m(u,s)+\int(P\dot Q+H)\,dv,
\qquad B_m=J^{-1/2}>0.
\tag{5.4}
$$

Variation of the action cancels the interior terms using (5.1), giving

$$
\Phi_q=P,\qquad \Phi_v=H(q,\Phi_q),\qquad
\Phi_s=\frac{u-a(s+m)}b.
\tag{5.5}
$$

The first equation in (5.1) and (5.5) have the sign appropriate to the positive quantum exponential $e^{itQ_N(H)/h}$. The amplitude obeys

$$
B_v=H_pB_q+\tfrac12(H_{pq}+H_{pp}\Phi_{qq})B.
\tag{5.6}
$$

Let $S_m=\Phi_m-\Theta_m$. At the final endpoint, $|u-q|\le\mathcal G$ and $|P-p_m(u,s)|\le\mathcal G$, so

$$
|S_{m,q}|\le2\mathcal G=16t\Sigma_R,
\qquad |S_{m,s}|\le\mathcal G/b=8t\Sigma_R/b.
\tag{5.7}
$$

Since $B_m^2=1/J$, (5.3) gives

$$
|B_m^2-1|\le\frac{2\mathcal L}{1-2\mathcal L}
\le4\mathcal L=256t\Lambda_R.
\tag{5.8}
$$

These are estimates on the full nonlinear action and amplitude. The first-order phase estimate is used only to certify one coefficient. At time $v$, let $G(v)=8L_j$ on its active stage and put $g(v)=\int_0^vG(w)\,dw$. The same endpoint argument gives $|\Phi_q(v)-p_m(q,s)|\le2g(v)$. From the Hamilton–Jacobi equation at a fixed endpoint,

$$
\begin{aligned}
\left|S_m-t\sum_{j<R}H_j(q,p_m(q,s))\right|
&\le2\int_0^{Rt}G(v)g(v)\,dv\\
&=\left(\int_0^{Rt}G(v)\,dv\right)^2
=64t^2\Sigma_R^2.
\end{aligned}
\tag{5.9}
$$

This estimate has no extra factor $R$, no factor $b_R$, and no $N$. It is valid at the prescribed positive fixed $t$.

## 6. Exact nonlinear sheet law and separation of every pair

The initial polynomial phases satisfy

$$
\begin{aligned}
\Theta_{m+b}(q,s)&=\Theta_m(q,s)+q-a(s+m)-ab/2,\\
\Theta_m(q+1,s)&=\Theta_{m-a}(q,s)-c(s+m)+ac/2,\\
\Theta_m(q,s+1)&=\Theta_{m+1}(q,s).
\end{aligned}
\tag{6.1}
$$

These identities preserve the full evolutions. For the first, adding $q$ shifts momentum by one; every $H_j$ is periodic in momentum. For the second, translating position by one leaves each symbol unchanged; its additive term depends only on $s$. The third literally changes the initial parameter. The action formula (5.4), or uniqueness of (5.5), preserves the displayed additive constants exactly. The amplitude identities have no additive terms.

Subtracting the initial identities proves

$$
S_{m+b}=S_m,\qquad S_m(q+1,s)=S_{m-a}(q,s),
\qquad S_m(q,s+1)=S_{m+1}(q,s).
$$

Thus $S_m,B_m$ have period $b$ in both endpoint coordinates. More strongly, the initial action and graph for label $m$ are literally those for label zero with parameter $s+m$. Since the evolution symbols do not depend on $s$,

$$
S_m(q,s)=S_0(q,s+m)
\tag{6.2}
$$

as real analytic functions, not just as sampled exponentials or first-order series.

Use Fourier frequencies on this $b$-periodic parameter torus. The marked frequency is

$$
\nu=(7-a/b,1/b).
$$

Both components are nonzero. From (2.4),

$$
\widehat a(7,1)=e^{-i\alpha_0}/400.
$$

For a transformed label $(k',l')$, substitution of $p_0=(-aq+s)/b$ produces frequency $(k'-al'/b,l'/b)$. This map is injective. Producing $\nu$ therefore requires $(k',l')=(7,1)$. At stage $j\ge1$, its unique original preimage would be

$$
(k,l)=(7a_j-c_j,a_j-7b_j).
$$

Its second coordinate is less than $-6b_j\le-24$, outside the original $|l|\le1$ support. Hence the coefficient of $\sum_{j<R}H_j(q,p_0)$ at $\nu$ is exactly $e^{-i\alpha_0}/400$.

Let $C_R(t)=\widehat S_0(\nu)$. Taking the normalized Fourier coefficient of (5.9) and using the smallness condition gives

$$
\left|C_R(t)-te^{-i\alpha_0}/400\right|
\le64t^2\Sigma_R^2\le t/800,
\qquad |C_R(t)|\ge t/800>0.
\tag{6.3}
$$

Equation (6.2) then gives the exact nonlinear coefficient for any two labels:

$$
\widehat{S_m-S_n}(\nu)
=C_R(t)\left(e^{2\pi im/b}-e^{2\pi in/b}\right).
\tag{6.4}
$$

It is nonzero for every distinct $m,n\pmod b$. The possibly very small distance between adjacent roots of unity multiplies the full nonlinear coefficient; it never divides the nonlinear error estimate. This validates the absence of a sheet-count factor in the sufficient smallness condition.

Explicitly,

$$
\Theta_m-\Theta_n
=\frac{m-n}{b}(q-as)-\frac{a(m^2-n^2)}{2b},
$$

which is separable in the endpoints. The nonzero coefficient (6.4) therefore implies

$$
\partial_q\partial_s(\Phi_m-\Phi_n)\not\equiv0.
\tag{6.5}
$$

For clarity, differentiating the periodic correction multiplies that coefficient by $-(2\pi)^2\nu_q\nu_s\ne0$. Since the phase is analytic on the whole real parameter plane, its mixed derivative cannot vanish on an open neighborhood of the unit square while being nonzero elsewhere on the $b$-periodic torus. This verifies the precise local analytic hypothesis of the sampled lemma.

For $\phi_{mn}=\Phi_m-\Phi_n$, form its rectangular-cycle phase

$$
\Omega=\phi_{mn}(q,s)-\phi_{mn}(q',s)
+\phi_{mn}(q',s')-\phi_{mn}(q,s').
$$

The entire initial separable part cancels. Each $q$ or $q'$ derivative has four $S_q$ terms; each $s$ or $s'$ derivative has four $S_s$ terms. Therefore

$$
\max_j\|\partial_j\Omega\|_\infty
\le64t\Sigma_R
\le\frac1{800\Sigma_R}<\frac18.
\tag{6.6}
$$

Large individual separable phase slopes, especially in the $s$ coordinate when $b_R$ is large, do not enter this bound. The raw sampled lemma requires the cycle gradient, precisely as used here.

## 7. Wrapped finite shifts and the actual matrix error

At every intermediate time define

$$
V_N(x,y)=\frac{\eta_{R,N}}{\sqrt{bN}}
\sum_{m=0}^{b-1}B_m(x/N,y/N)e^{i\Phi_m(x/N,y/N)/h}.
\tag{7.1}
$$

Initially $V_N=M_N^R$ exactly. Under $x\mapsto x+N$, the second deck identity in (6.1) adds, after multiplication by $N$,

$$
-cy-cNm+acN/2\in\mathbb Z.
$$

Reducing an image label by a multiple of $b$ uses the first identity and adds multiples of phases of the form

$$
x-ay-aNm-abN/2\in\mathbb Z.
$$

Both expressions are integral because $ab,ac$ are even. The same argument with $s\mapsto s+1$ proves column-parameter periodicity. Hence the **full sum**, sampled at integer indices, is exactly $N$-periodic at every time. Individual branches need not be periodic.

This is sufficient for (2.3): the sampled vector at a wrapped shift $x+l\pmod N$ equals the full branch sum evaluated at the unreduced integer $x+l$. Smooth branch extensions can therefore be Taylor expanded before summing. No edge discrepancy is discarded.

For a fixed raw Fourier term, the shift in $q$ is $2\pi hl$. With $p=\Phi_q$, direct expansion gives

$$
\begin{aligned}
e^{2\pi ik(q+\pi hl)}&=e^{2\pi ikq}(1+2\pi^2ihkl+O(h^2)),\\
B(q+2\pi hl)&=B+2\pi hlB_q+O(h^2),\\
e^{i[\Phi(q+2\pi hl)-\Phi(q)]/h}
&=e^{2\pi ilp}(1+2\pi^2ihl^2\Phi_{qq}+O(h^2)).
\end{aligned}
$$

Summing the fixed finite Fourier support yields

$$
Q_N(H)(Be^{i\Phi/h})
=e^{i\Phi/h}\left\{HB
-ih\left[H_pB_q+\tfrac12(H_{pq}+H_{pp}\Phi_{qq})B\right]
+O_R(h^2)\right\}.
\tag{7.2}
$$

The coefficient of $B_q$ follows from $H_p=\sum 2\pi il\widehat H e^{2\pi i(kq+lp)}$; the two other coefficients follow from $H_{pq}$ and $H_{pp}$, each contributing $-4\pi^2$ times its Fourier monomial. Thus the minus sign in front of $ih$ is checked directly.

The Hamilton–Jacobi and transport equations cancel the two displayed orders in $(\partial_v-iQ_N(H)/h)V_N$. Its residual is $O_R(h/\sqrt N)$ in each entry and $O_R(h)$ in each column's Euclidean norm. For fixed $R$, the finite number of stages, branches, and raw shifts merely changes the constant. Eventually every fixed raw shift is small relative to $N$; no bound uniform in unbounded $R$ is asserted.

Every $H_j$ is real on the real torus and $Q_N(H_j)$ is Hermitian. Exact stage propagation is consequently unitary. Applying Duhamel across the continuous joins gives

$$
\|(U_N^R-V_N)e_y\|_2=O_R(h),\qquad
\|U_N^R-V_N\|_{\rm HS}=O_R(h\sqrt N).
\tag{7.3}
$$

The unitary estimate is essential: no $e^{C/h}$ stability factor appears.

By (5.8), the amplitude error is at most $1/200$, so

$$
\max_{x,y}|V_N(x,y)|\le\frac{\sqrt{b(1+1/200)}}{\sqrt N}.
$$

The column error controls each entry by $O_R(N^{-1})=o_R(N^{-1/2})$. This proves (B). It also gives a uniform $O_R(N^{-1/2})$ entry bound for $U_N^R$. Therefore

$$
\begin{aligned}
\bigl\||U_N^R|^{\circ2}-|V_N|^{\circ2}\bigr\|_{\rm HS}
&\le \bigl(\|U_N^R\|_{\max}+\|V_N\|_{\max}\bigr)
\|U_N^R-V_N\|_{\rm HS}\\
&=O_R(N^{-1/2})\,O_R(h\sqrt N)
=O_R(N^{-1}).
\end{aligned}
\tag{7.4}
$$

This explicitly checks the dimension factors in the passage from a WKB column error to the probability operator.

## 8. Independent reconstruction of the sampled $S_4$ lemma

The exact dependency is §1 of `research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md`, not an earlier audit summary. It considers

$$
T_N(x,y)=\frac1N\mathbf1_{x\equiv\rho\ (4)}\mathbf1_{y\equiv\sigma\ (4)}
w(x/N,y/N)e^{2\pi iN\phi(x/N,y/N)},
$$

with smooth $w$, real analytic $\phi$ on a connected neighborhood of the square, $\phi_{qr}\not\equiv0$, and cycle gradient less than $1/8$. The conclusion is $\|T_N\|_{\rm op}\to0$ along all integers $N$.

First replace $w$ by $\chi(q)\chi(r)w$, with a fixed interior cutoff equal to one on $[\varepsilon,1-\varepsilon]$. At most $4\varepsilon N^2+O(N)$ entries are altered, each by at most $\|w\|_\infty/N$. Thus the limiting operator error is at most $2\|w\|_\infty\sqrt\varepsilon$, by the Hilbert–Schmidt bound.

For this compactly supported amplitude, exact multiplication gives

$$
\|T_N\|_{S_4}^4=\frac1{N^4}
\sum_{\substack{x,x'\equiv\rho\ (4)\\y,y'\equiv\sigma\ (4)}}
W(x/N,x'/N,y/N,y'/N)e^{2\pi iN\Omega(x/N,x'/N,y/N,y'/N)},
\tag{8.1}
$$

where $W=w(q,r)\overline{w(q',r)}w(q',r')\overline{w(q,r')}$, with all cutoffs included. This is exactly a four-variable sum; it is neither a trace of the original unitary nor an integral substituted for the discrete matrix norm.

For a Schwartz function $F$, periodization at spacing $4/N$ gives

$$
\frac1N\sum_{x\equiv\rho\ (4)}F(x/N)
=\frac14\sum_{k\in\mathbb Z}e^{2\pi ik\rho/4}\widehat F(Nk/4).
$$

Applying this identity in all four coordinates of (8.1) gives

$$
\frac1{4^4}\sum_{k\in\mathbb Z^4}
e^{2\pi ik\cdot(\rho,\rho,\sigma,\sigma)/4}
\int W(z)e^{2\pi iN[\Omega(z)-k\cdot z/4]}\,dz.
\tag{8.2}
$$

The prefactor, alias scale $k/4$, and positive residue character are thus correct.

For $k\ne0$, choose $j$ with $|k_j|=|k|_\infty$. The cycle-gradient hypothesis gives

$$
|\partial_j(\Omega-k\cdot z/4)|
\ge |k_j|/4-1/8\ge |k_j|/8.
$$

Six integrations by parts in that coordinate bound the integral by

$$
C_\varepsilon N^{-6}(1+|k|_\infty)^{-6}.
\tag{8.3}
$$

All derivatives of order at least two of the aliased phase are derivatives of $\Omega$, independent of $k$. Differentiated reciprocals of its first derivative therefore retain at least the required six total powers of $|k|_\infty$ in the denominator. The constants can be chosen uniformly across the four choices of $j$. The lattice shell has $O((1+|k|_\infty)^3)$ points, so (8.3) is summable in four dimensions. The aggregate nonzero-alias contribution tends to zero.

For $k=0$, the phase is nonconstant because

$$
\partial_q\partial_r\Omega=\partial_q\partial_r\phi(q,r)\not\equiv0.
$$

A nonzero real analytic function on a connected open set has a zero set of measure zero: locally expand in one variable; at least one coefficient is a nonzero analytic function of one fewer variables; outside its zero set each one-variable slice has isolated zeros; induction and Fubini complete the argument. Analytic continuation prevents an identically zero open box in a connected domain. Applying this fact to a nonzero partial derivative of $\Omega$ shows that its critical set has measure zero.

Cut off a small neighborhood of this critical set. On the remaining support,

$$
\int W\eta_\delta e^{2\pi iN\Omega}
=-\frac1{2\pi iN}\int
\operatorname{div}\left(W\eta_\delta\frac{\nabla\Omega}{|\nabla\Omega|^2}\right)
e^{2\pi iN\Omega},
$$

whose modulus is $O_\delta(N^{-1})$. The removed integral is bounded by the integral of $|W|$ on a set shrinking to the measure-zero critical set. Take $N\to\infty$, then the critical cutoff to zero. Finally send the earlier boundary width $\varepsilon\to0$. This proves $\|T_N\|_{S_4}\to0$ and hence $\|T_N\|_{\rm op}\to0$.

The argument applies to every positive integer $N$; it has no prime, coprimality, equidistribution, or subsequence hypothesis. Its constants and the eventual onset of decay may depend very badly on the fixed analytic phase. That is permitted by the claim being audited.

## 9. Assembly of the physical probability bound

The equal-sheet part of $|V_N|^{\circ2}$ is

$$
P_{\rm self}(x,y)=\frac1{bN}\sum_{m=0}^{b-1}B_m(x/N,y/N)^2.
$$

By (5.8), every entry of $P_{\rm self}-J_N$ is bounded in modulus by $256t\Lambda_R/N$. Both its absolute row sums and its absolute column sums are at most $256t\Lambda_R$, so

$$
\|P_{\rm self}-J_N\|_{\rm op}\le256t\Lambda_R.
$$

Each ordered pair $m\ne n$ contributes

$$
\frac1{bN}B_m(x/N,y/N)B_n(x/N,y/N)
e^{2\pi iN\phi_{mn}(x/N,y/N)}.
$$

The amplitude is smooth and independent of $N$, the phase is analytic, (6.5) verifies its nonzero mixed derivative, and (6.6) verifies the precise small cycle-gradient condition. Split the matrix into its sixteen row-column residue blocks modulo four and apply the exact lemma above to each. This is the lemma's stated form; no alteration of it is needed.

For each fixed $R$, there are finitely many branches, ordered pairs, and blocks. A finite sum of terms with norm tending to zero still tends to zero even when the fixed number of terms is enormous. Combining these cross-sheet limits, the self bound, and (7.4) proves (A).

Finally $256t\Lambda_R\le1/200$ under the smallness condition. For the finite set $1\le R\le49$, choose the maximum of the finitely many thresholds at which the $o_R(1)$ error is at most $1/200$. This proves the stated common operator-distance bound $1/100$. The same finite-maximum argument applies to the entry thresholds.

## 10. Adversarial checks of the scope

| Potential obstruction | Audit conclusion |
| --- | --- |
| Replacing modular $2^{-1}$ by $1/2$ | The proof does not do this; it introduces the necessary coefficient sign and $q+1/2$ shift. |
| Replacing modular $8^{-1}$ by an ordinary denominator | The image formula is independently proved by covariance and normalization. |
| $\gcd(N,b_R)>1$ or $N$ divisible by 3, 5, 7, or larger factors | The complete Gauss norm retains the exact support condition; all subsequent identities and the sampled lemma cover these dimensions. |
| Full nonlinear action replaced by a first-order approximation | The phases remain exact characteristic solutions. First order is used only with a uniform quadratic remainder to show $C_R(t)\ne0$. |
| Comparing tiny adjacent sheet characters to an unfactored remainder | Exact translation factors the nonlinear coefficient itself, so no division by a root separation occurs. |
| Large separable phase slopes causing sampling aliases | They cancel from the rectangular cycle, which is the phase actually subjected to Poisson summation. |
| A nonzero Fourier coefficient outside the unit square | Analytic continuation ensures the mixed derivative is nonzero as a function on every open neighborhood of the unit square. |
| Nonperiodic individual WKB branches at the matrix boundary | The finite branch sum is exactly periodic on the grid, with all added phases integral after multiplication by $N$. |
| A hidden factor $N$ in residual or entrywise probabilities | The explicit chain is residual column $O_R(h)$, total HS error $O_R(h\sqrt N)$, and probability HS error $O_R(N^{-1})$. |
| Sending $t\to0$ to justify decay | The sampled limit is taken with this positive $t$ fixed. The coefficient can be extremely small but is nonzero. |
| Persistent resonant subsequence | The nonzero-alias bound and zero-alias limit hold for all $N$, so none survives within these hypotheses. |
| A small-$N$ computation close to the unperturbed metaplectic matrix | It cannot test the eventual fixed-$t$ limit. The proof gives no useful finite threshold at $t=10^{-80}/(2\pi)$. |
| Extending to growing powers or all long mismatch runs | This is outside the theorem; constants, sheet count, analytic neighborhoods, and decay onset may depend on the fixed $R$. |

The $t=0$ comparison is a useful scope check. For example, the unperturbed two-step probability kernel has a nontrivial congruence support when $3\mid N$. The proof needs a strictly positive fixed $t$, as specified. It does not derive the positive-$t$ limit by a uniform passage through $t=0$.

## 11. Independent computation and provenance

The companion script is

`research_round7_2026_10_21/r7_audit_physical_fixed_powers49_checks.py`.

It completed successfully with **594,433 exact assertions**, including:

- six symbolic polynomial identities, reduced exactly modulo $a^2-bc-1$;
- the corrected symbol and its marked Gaussian-rational coefficient, Fourier support, and rational majorants;
- original modular covariance for every coordinate pair in each odd dimension $3\le N\le101$, and additional raw-label tests including labels of magnitude 41;
- recurrence, parity, support separation, and marked-frequency noncollision through power 50;
- all-odd Gauss parity checks through $N=301$, together with 282 direct cyclotomic evaluations of $|G|^2$ for powers 1, 2, 3 and dimensions $3,5,7,9,15,21,25,35$;
- exact rational certification of powers 1 through 49 and exclusion of 50 from the stated sufficient condition.

The direct cyclotomic tests include common divisors $3,5,7,35$. They supplement the general proof in §3, which covers all allowed dimensions and fixed powers. They do not purport to exhaust an asymptotic sequence. No floating-point value of the kick, numerical diagonalization, fitted decay rate, or tolerance-dependent equality was used.

Reproduction:

```bash
python research_round7_2026_10_21/r7_audit_physical_fixed_powers49_checks.py
```

The resulting full check record is

`research_round7_2026_10_21/r7_audit_physical_fixed_powers49_checks.md`.

The independent script SHA-256 at this audit is

`76155ec26d0675f8d9b773d60d991a7fb580aac09fd602f34b577f28442721b1`.

| Source | Scope inspected | SHA-256 |
| --- | --- | --- |
| `Spectral_research_master.md` | Base hash verified; not used as a proof substitute | `3534e4d7aa97c2f8621050248652363c639aeedf723f8b7fe7a971dc01ac2302` |
| `research_round6_2026_10_21/round6_main_report.md` | Original definitions in §1 and local fixed-power notation | `473b7b5b700a8ff17801eb9ca422c5949be15d0551c252e0b4035997db54b2bf` |
| `research_round6_2026_10_21/r6_original_fixed_powers_49.md` | Complete raw target proof | `3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019` |
| `research_round6_2026_10_21/r6_original_twostep_physical_mixing.md` | Complete raw note; especially §§1, 3–8 | `7d502a881f133743cd3d28afd6ac373351fd4a12f23e8292c59895358f1e747b` |
| `research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md` | Actual sampled lemma and proof in §1 | `ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d` |

## 12. Remaining gap and strongest safe statement

**Remaining gap for (A) and (B): none identified.** The exact matrix conventions, nonlinear evolution, boundary compatibility, dimension scaling, and oscillatory implication all close under the stated positive fixed kick and fixed-power condition. The supplied proof did not need a new repair or a changed convention to reach this verdict.

The strongest safe statement from this audit is the stated fixed-power theorem, and hence its simultaneous specialization to $1\le R\le49$ along all odd dimensions. It provides physical input for arguments that use only this finite range. It supplies no rate uniform as $t\downarrow0$, no quantitative usable threshold in $N$, no control over $R\to\infty$, and no completion of the full long-trajectory or spectral claim.

The cheapest useful downstream check is to verify that any later application actually keeps the physical power in this finite range and does not replace $o_R(1)$ by an estimate uniform in growing $R$. Repeating small-dimensional numerical experiments would not strengthen the asymptotic conclusion established here.
