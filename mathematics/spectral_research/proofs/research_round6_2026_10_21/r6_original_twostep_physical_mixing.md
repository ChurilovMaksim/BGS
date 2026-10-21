> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_original_twostep_physical_mixing.md`. Embedded SHA256: `7d502a881f133743cd3d28afd6ac373351fd4a12f23e8292c59895358f1e747b`.
> [Thematic guide](../../topics/classical_trace.md).

# Two-step physical probability mixing for the exact original family

21 October 2026. This note proves a new estimate for the actual square of the prescribed matrix:
$$
 \boxed{
 \bigl\||U_N^2|^2-J_N\bigr\|_{\rm op}
 \le8\cdot10^6t+o(1),\qquad t=\frac{10^{-80}}{2\pi}.
 }
 \tag{0.1}
$$
Absolute squares in (0.1) are entrywise. The limit is over every odd $N$, including dimensions divisible by three. The kick remains the exact fixed kick in the question.

The proof propagates an exact 24-image representation of $M_N^2$ through two finite-shift Schrödinger evolutions. It then applies the sampled oscillatory matrix lemma proved and independently audited in round 5, with all its hypotheses verified for the new phases. Neither $P(U_N^2)$ nor its phase cancellations are inferred from $P(U_N)^2$.

An immediate consequence is an all-time signed estimate for every actual rooted pair whose nonempty literal mismatch set has no adjacent positions, with arbitrary changed labels and no occupation restriction. This consequence is given in Section 9. It is not the full unequal-occupation sum or $H_{\rm diag}$.

## 1. Exact symbols and the two evolution stages

Put
$$
 h=(2\pi N)^{-1},\qquad t=\tau/(2\pi),\qquad
 E_N(s)=e^{isA_N/h}.
$$
For a finite Fourier polynomial $H$, use the ordinary-half notation
$$
 Q_N(H)=\sum_{k,l}\widehat H(k,l)(-1)^{kl}T_N(l,k).
$$
The original modular-half quantization is exactly
$$
 A_N=Q_N(a),
$$
where
$$
 \begin{split}
 a(q,p)={}&\cos(14\pi q)+r(q)/10
 +r(q)\sin(2\pi q)/100-1/10\\
 &+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
 \end{split}
 \tag{1.1}
$$
This follows directly from
$$
 e_N(k2^{-1}l)=(-1)^{kl}e^{\pi ikl/N}.
 \tag{1.2}
$$
In particular, on every periodic sequence on $\mathbb Z$,
$$
 (Q_N(H)\psi)(x)
 =\sum_{k,l}\widehat H(k,l)
 e^{2\pi ik(x/N+l/(2N))}\psi(x+l).
 \tag{1.3}
$$
Thus wrapped shifts cause no change of convention.

The elementary Gaussian kernel calculation gives the exact Weyl covariance
$$
 M_NT_N(l,k)M_N^*=T_N(3l+4k,2l+3k).
 \tag{1.4}
$$
For completeness it can be verified on the two generators. Writing $L=T_N(1,0)$, $D=T_N(0,1)$, direct subtraction of the quadratic kernel phases gives
$$
 M_NL=T_N(3,2)M_N,\qquad M_ND=T_N(4,3)M_N.
$$
The Weyl multiplication law then gives (1.4) for all integer labels. No inverse of three is involved.

The transformed Fourier label of $(k,l)$ is $(3k+2l,4k+3l)$. These two components have the same parities as $k,l$, respectively. Thus the signs in the ordinary-half basis cancel exactly, and
$$
 A_N^M:=M_NA_NM_N^*=Q_N(a^M),
 \qquad a^M(q,p)=a(3q+4p,2q+3p).
 \tag{1.5}
$$
All labels in this argument are the raw integer labels before reduction modulo $N$.

The desired square therefore has the exact factorization
$$
 \boxed{
 U_N^2=e^{itA_N/h}e^{itA_N^M/h}M_N^2.
 }
 \tag{1.6}
$$
We evolve the initial kernel first under $a^M$ for time $t$, and then under $a$ for time $t$.

## 2. Uniform elementary derivative bounds

The Fourier support of $a$ satisfies $|k|+|l|\le9$ and $\sum|\widehat a(k,l)|<2$. These facts follow by expanding the finite products in (1.1); they were also checked in the round-5 physical kernel proof. The integer transformation in (1.5) shows that the support of $a^M$ satisfies
$$
 |k|+|l|\le63,\qquad \sum|\widehat {a^M}(k,l)|<2.
 \tag{2.1}
$$
The latter coefficient norm is unchanged by the invertible label transformation.

On the complex tube
$$
 \max(|\operatorname{Im}q|,|\operatorname{Im}p|)\le2\cdot10^{-3},
$$
both $H=a$ and $H=a^M$ consequently satisfy
$$
 |H_q|,|H_p|<2000,\qquad
 \|D(-H_p,H_q)\|_{\infty\to\infty}<10^6.
 \tag{2.2}
$$
Sufficient upper bounds are
$$
 2(2\pi)63e^{2\pi(2\cdot10^{-3})63}<2000,
$$
and
$$
 2(2\pi)^2 63^2e^{2\pi(2\cdot10^{-3})63}<10^6.
$$
For an entirely rational margin, $\pi<22/7$ and $e^{4/5}<9/4$ bound these by $1782$ and $705672$, respectively. The exponential inequality follows, for example, by summing its Taylor series through degree six and bounding the remaining positive tail by a geometric series.

Every fixed higher derivative also has a finite uniform bound on a smaller tube, since both symbols are fixed trigonometric polynomials. On the real torus, $|H|<2$.

The following construction is valid for $0<t\le t_*:=10^{-12}$. The actual fixed $t=10^{-80}/(2\pi)$ satisfies this explicit margin. We do not take $t$ to zero with $N$.

## 3. The exact 24-image initial kernel

Here is a direct all-odd proof, which also records the normalization needed below. Set
$$
 A=17,\qquad B=24,\qquad C_0=12,\qquad A^2-BC_0=1.
$$
Define
$$
 K_N(x,y)=\frac1{\sqrt{BN}}
 \sum_{m=0}^{B-1}
 \exp\left[
 -\frac{2\pi i}{2BN}
 \{A x^2-2x(y+mN)+A(y+mN)^2\}
 \right].
 \tag{3.1}
$$
There is a unit scalar $\eta_N$ such that
$$
 \boxed{M_N^2=\eta_NK_N.}
 \tag{3.2}
$$

### 3.1. Periodicity and covariance

Let $Q(x,Y)=Ax^2-2xY+AY^2$. The summand in (3.1) is periodic under $m\mapsto m+B$, since
$$
 \frac{Q(x,Y+BN)-Q(x,Y)}{2BN}
 =-x+AY+ABN/2
$$
is an integer. Reindexing $m$ proves periodicity under $y\mapsto y+N$. For the $x$-periodicity use
$$
 \frac{Q(x+N,Y+AN)-Q(x,Y)}{2BN}
 =C_0Y+AC_0N/2\in\mathbb Z
 \tag{3.3}
$$
and reindex $m\mapsto m+A$. Both $B,C_0$ are even.

The polynomial identities
$$
 Q(x+A,Y)-Q(x,Y-1)=BC_0(2x+A),
$$
$$
 Q(x+B,Y)-Q(x,Y)=2B\{A(x+B/2)-Y\}
$$
give exactly
$$
 K_NL=T_N(A,C_0)K_N,\qquad
 K_ND=T_N(B,A)K_N.
 \tag{3.4}
$$
The ordinary halves in these identities agree with modular halves because $AC_0$ and $AB$ are even.

Squaring (1.4) shows that $M_N^2$ has the same covariance. Therefore $(M_N^2)^*K_N$ commutes with $L,D$. A matrix commuting with $D$, whose diagonal entries are the distinct $N$-th roots of unity, must be diagonal. Commuting also with the cyclic shift $L$ forces all its diagonal entries to agree. Hence $K_N$ is a scalar multiple of $M_N^2$.

### 3.2. The scalar has modulus one, including $3\mid N$

Let $g=\gcd(N,B)$, so $g=1$ or $3$ for odd $N$. After factoring out the unit quadratic phase independent of $m$, the finite sum in (3.1) is
$$
 G=\sum_{m=0}^{B-1}
 \exp\left[-\frac{\pi iANm^2}{B}
 +\frac{2\pi i(x-Ay)m}{B}\right].
$$
Square its modulus and put $d=m-n$ modulo $B$. The sum over $n$ vanishes unless $ANd=0\pmod B$. Since $\gcd(A,B)=1$, this means $d=(B/g)r$, $0\le r<g$. Its remaining quadratic phase equals
$$
 \exp[-\pi i(AN/g)(B/g)r^2]=1,
$$
because $B/g$ is even. The remaining linear sum is $g$ if $g\mid x-Ay$, and zero otherwise. Thus
$$
 \boxed{
 |K_N(x,y)|^2=\frac gN{\bf1}_{\{g\mid x-Ay\}}.
 }
 \tag{3.5}
$$
For each fixed $x$, there are exactly $N/g$ values of $y$ satisfying the congruence, since $g\mid N$ and $A$ is invertible modulo $g$. Every row has norm one. The scalar relation with the unitary $M_N^2$ therefore has scalar of modulus one, proving (3.2).

In particular, no use was made of $24^{-1}$ or $48^{-1}$ modulo $N$. The kernel includes the exact support restriction when $3\mid N$.

## 4. The two Hamilton--Jacobi evolutions

For all integer $m$, put
$$
 \Theta_m(q,r)=
 -\frac{17q^2-2q(r+m)+17(r+m)^2}{48},
 \qquad
 p_m(q,r)=\partial_q\Theta_m(q,r)=\frac{-17q+r+m}{24}.
 \tag{4.1}
$$
Let the time-dependent symbol be
$$
 H_\sigma=
 \begin{cases}
 a^M,&0\le\sigma<t,\\
 a,&t<\sigma\le2t.
 \end{cases}
 \tag{4.2}
$$
The values at the single joining time do not matter. Starting from
$$
 Q_0=u,\qquad P_0=p_m(u,r),
$$
solve the piecewise Hamiltonian equations
$$
 \dot Q_\sigma=-H_{\sigma,p}(Q_\sigma,P_\sigma),\qquad
 \dot P_\sigma=H_{\sigma,q}(Q_\sigma,P_\sigma).
 \tag{4.3}
$$

The bounds (2.2) give existence on the full interval and analytic dependence on the initial variables. More explicitly, on a fixed complex tube around each real initial graph, the integral equation is a contraction on the displacement ball because $2t\,10^6<1$; the displacement is at most $4000t$. It remains inside the larger tube in (2.2). Differentiating that integral equation and summing the elementary exponential majorant gives
$$
 |Q_\sigma-u|,\ |P_\sigma-p_m(u,r)|\le2000\sigma,
$$
$$
 \|D(Q_\sigma,P_\sigma)-I\|_{\infty\to\infty}
 \le e^{10^6\sigma}-1\le2\cdot10^6\sigma.
 \tag{4.4}
$$
The derivative here is with respect to the two initial phase-space coordinates. These estimates also hold on a fixed smaller complex neighborhood, independently of all real $u,r$ and integer $m$.

The tangent to the initial graph is $(1,-17/24)$, of maximum norm one. Hence
$$
 J_\sigma:=\partial_uQ_\sigma(u,r,m),\qquad
 |J_\sigma-1|\le2\cdot10^6\sigma\le4\cdot10^6t<1/2.
 \tag{4.5}
$$
For real $r$, the map $u\mapsto Q_\sigma(u,r,m)$ is increasing and differs from $u$ by a bounded function; it is a global bijection. On the complex neighborhood its inverse follows from the contraction $u=q-(Q_\sigma(u)-u)$, using (4.5) and the displacement bound. The neighborhoods can be chosen uniformly. This also proves uniform bounds for every fixed derivative of the resulting periodic corrections.

With $q=Q_\sigma(u,r,m)$, define
$$
 \Phi_m(\sigma,q,r)=
 \Theta_m(u,r)+
 \int_0^\sigma\{P_v\dot Q_v+H_v(Q_v,P_v)\}\,dv,
$$
$$
 B_m(\sigma,q,r)=J_\sigma(u,r,m)^{-1/2}.
 \tag{4.6}
$$
The positive square root is used for real coordinates. The phase is real analytic in $q,r$; the amplitude is positive and real analytic there. Both are continuous at the joining time.

Variation of the action, followed by integration by parts and (4.3), cancels its interior terms. The endpoint terms give
$$
 \Phi_{m,q}=P_\sigma,\qquad
 \Phi_{m,\sigma}=H_\sigma(q,\Phi_{m,q}),\qquad
 \Phi_{m,r}=\frac{u-17(r+m)}{24}.
 \tag{4.7}
$$
These hold on each open time segment. The Jacobian equation also gives the transport equation
$$
 B_{m,\sigma}
 =H_{\sigma,p}B_{m,q}
 +\frac12(H_{\sigma,pq}+H_{\sigma,pp}\Phi_{m,qq})B_m,
 \tag{4.8}
$$
where symbol derivatives are evaluated at $(q,\Phi_{m,q})$.

## 5. Explicit phase and amplitude estimates

Write $S_m(\sigma,q,r)=\Phi_m(\sigma,q,r)-\Theta_m(q,r)$. Equations (4.4) and (4.7) imply
$$
 |S_{m,q}(\sigma)|\le
 (1+17/24)2000\sigma\le4000\sigma,
$$
$$
 |S_{m,r}(\sigma)|\le2000\sigma/24\le100\sigma.
 \tag{5.1}
$$
The last equation uses the cancellation of the common $-17(r+m)/24$ in (4.7) and the initial phase. Integrating the time equation at a fixed endpoint also gives $|S_m(\sigma)|\le2\sigma$.

The Jacobian bound yields
$$
 |B_m(\sigma)^2-1|
 \le\frac{2\cdot10^6\sigma}{1-2\cdot10^6\sigma}
 \le4\cdot10^6\sigma.
 \tag{5.2}
$$
In particular, at time $2t$,
$$
 |S_{m,q}|\le8000t,\qquad
 |S_{m,r}|\le200t,\qquad
 |B_m^2-1|\le8\cdot10^6t.
 \tag{5.3}
$$

Put
$$
 b_m(q,r)=a^M(q,p_m(q,r))+a(q,p_m(q,r)).
 \tag{5.4}
$$
By (2.2), (5.1), and the time equation in (4.7),
$$
 \begin{aligned}
 |S_m(2t,q,r)-t b_m(q,r)|
 &\le\int_0^{2t}
 2000\,|\Phi_{m,q}(\sigma,q,r)-p_m(q,r)|\,d\sigma\\
 &\le2000\cdot4000\int_0^{2t}\sigma\,d\sigma\\
 &=16\cdot10^6t^2.
 \end{aligned}
 \tag{5.5}
$$
This uniform estimate is valid on the whole real parameter plane, not just on a selected compact set.

## 6. Exact deck identities and the finite-shift error

The image-phase convention in (4.1) absorbs all $y$-dependent coefficients of the 24-image sum into the phases. Its deck identities are
$$
 \begin{split}
 \Theta_{m+24}(q,r)&=\Theta_m(q,r)+q-17(r+m)-204,\\
 \Theta_m(q+1,r)&=\Theta_{m-17}(q,r)-12(r+m)+102,\\
 \Theta_m(q,r+1)&=\Theta_{m+1}(q,r).
 \end{split}
 \tag{6.1}
$$
They follow by direct expansion. Both symbols in (4.2) are periodic in $q,p$ with period one. Adding $q$ shifts the momentum by one, and translating $q$ by one leaves the Hamilton--Jacobi equation unchanged. Uniqueness of the characteristic solutions thus propagates all three identities to $\Phi_m$. The amplitudes obey their versions with no additive terms.

Subtracting the initial identities shows
$$
 S_{m+24}=S_m,\quad
 S_m(q+1,r)=S_{m-17}(q,r),\quad
 S_m(q,r+1)=S_{m+1}(q,r),
 \tag{6.2}
$$
and similarly for $B_m$. In particular all corrections and amplitudes have period 24 in each real coordinate.

Define
$$
 V_N(\sigma)_{xy}=
 \frac{\eta_N}{\sqrt{24N}}
 \sum_{m=0}^{23}
 B_m(\sigma,x/N,y/N)
 e^{i\Phi_m(\sigma,x/N,y/N)/h}.
 \tag{6.3}
$$
At $\sigma=0$, (3.2) gives $V_N(0)=M_N^2$ exactly.

For $x\mapsto x+N$, use the second identity in (6.1) and reindex $m\mapsto m-17$. The additional exponent, after multiplication by $N$, is
$$
 -12y-12Nm+102N\in\mathbb Z.
$$
Reducing a branch index modulo 24 uses the first identity, whose added exponent at the grid is
$$
 x-17y-17Nm-204N\in\mathbb Z.
$$
Thus $V_N(\sigma)_{x+N,y}=V_N(\sigma)_{xy}$ at every time. The third identity gives $y$-periodicity as well. Individual branches need not be periodic; the full finite sum is exactly periodic. This proves the boundary compatibility needed for (1.3).

For clarity, the same construction can be written with phases
$$
 \widetilde\Theta_m(q,r)
 =-(17q^2-2qr+17r^2)/48+mq/24
$$
and coefficients
$$
 24^{-1/2}
 \exp[-2\pi i(17my/24+17Nm^2/48)].
$$
Equation (6.3) simply includes these separable phases in $\Theta_m$, leaving one global scalar and the constant amplitude factor $24^{-1/2}$.

### 6.1. Direct residual

For either fixed symbol $H=H_\sigma$, expansion of the exact finite-shift formula gives
$$
 \begin{aligned}
 Q_N(H)\bigl(B e^{i\Phi/h}\bigr)
 =e^{i\Phi/h}\bigl\{&
 H(q,\Phi_q)B\\
 &-ih[H_pB_q+\tfrac12(H_{pq}+H_{pp}\Phi_{qq})B]
 +O(h^2)\bigr\}.
 \end{aligned}
 \tag{6.4}
$$
The remainder is uniformly bounded by a finite constant times $h^2$. The symbol has fixed finite support, and the required phase and amplitude derivatives are bounded uniformly. To check the normalization, the shift in $q$ is $l/N=2\pi hl$. The three first-order expansions are
$$
 e^{2\pi ik(q+\pi hl)}
 =e^{2\pi ikq}(1+2\pi^2ihkl+O(h^2)),
$$
$$
 B(q+2\pi hl)=B+2\pi hlB_q+O(h^2),
$$
$$
 e^{i[\Phi(q+2\pi hl)-\Phi(q)]/h}
 =e^{2\pi il\Phi_q}
 (1+2\pi^2ihl^2\Phi_{qq}+O(h^2)).
$$
Collecting them with the Fourier formulas for $H_p,H_{pq},H_{pp}$ proves (6.4), including its sign. Exact periodic gluing permits these smooth branch extensions at every wrapped shift.

The phase and transport equations cancel the two displayed terms in
$$
 (\partial_\sigma-iQ_N(H_\sigma)/h)V_N.
$$
The residual therefore has entrywise bound $Ch/\sqrt N$ and Euclidean norm at most $Ch$ in every column. Constants may depend on the fixed symbols and the construction interval, but not on $N$ or the column.

Both exact evolutions are unitary, and the phase and amplitude are continuous at their joining time. Applying Duhamel's formula on the two successive intervals gives
$$
 \boxed{
 \|(U_N^2-V_N(2t))e_y\|_2\le Cth,\qquad
 \|U_N^2-V_N(2t)\|_{\rm HS}\le Cth\sqrt N.
 }
 \tag{6.5}
$$
The constant absorbs the factor two from the total time. No composition through a discretized stationary-phase integral is being assumed.

By (5.3),
$$
 |V_N(2t)_{xy}|
 \le\frac{\sqrt{24}\sqrt{1+8\cdot10^6t}}{\sqrt N}
 <\frac5{\sqrt N}.
$$
The column error is $O(N^{-1})$; hence for every sufficiently large odd $N$,
$$
 \max_{x,y}|U_N^2(x,y)|\le6/\sqrt N.
 \tag{6.6}
$$
The exact difference-of-squares inequality and (6.5) then give
$$
 \boxed{
 \bigl\||U_N^2|^2-|V_N(2t)|^2\bigr\|_{\rm HS}=O(N^{-1}).
 }
 \tag{6.7}
$$

## 7. A nonzero mixed coefficient for every pair of distinct sheets

The first-order function in (5.4) has the explicit form
$$
 b_m(q,r)=
 a\left(q,\frac{-17q+r+m}{24}\right)
 +a\left(\frac{q+r+m}{6},\frac{-q+r+m}{8}\right).
 \tag{7.1}
$$
The second argument pair is obtained by applying $(q,p)\mapsto(3q+4p,2q+3p)$ to the first endpoint pair.

Fourier coefficients in this section are on the 24-periodic $(q,r)$-torus, with exponential $e^{2\pi i(\xi q+\zeta r)}$. The corrected symbol (1.1) has
$$
 \widehat a(7,1)=e^{-i\alpha_0}/400.
 \tag{7.2}
$$
Indeed $r(q+1/2)=(1+\cos14\pi q)(1-\cos2\pi q)$ has coefficient $1/2$ at frequency seven, and the positive $p$-frequency of its cosine is $e^{-i\alpha_0}/2$.

In the first term of (7.1), the original Fourier mode $(k,l)$ has frequency
$$
 (k-17l/24,l/24)
$$
and coefficient factor $e^{2\pi ilm/24}$. In the second term its frequency is
$$
 ((4k-3l)/24,(4k+3l)/24).
$$
The marked frequency
$$
 \nu=(151/24,1/24)
 \tag{7.3}
$$
comes from $(k,l)=(7,1)$ in the first term. It cannot come from the second: equality of both components would force $k=19,l=-25$, whereas every original mode has $|l|\le1$. Therefore
$$
 \boxed{
 \widehat b_m(\nu)=\frac{e^{-i\alpha_0}}{400}e^{2\pi im/24}.
 }
 \tag{7.4}
$$
For distinct $m,n\in\{0,\ldots,23\}$, concavity of sine gives
$$
 |e^{2\pi im/24}-e^{2\pi in/24}|
 \ge2\sin(\pi/24)\ge1/6.
$$
Thus $|\widehat b_m(\nu)-\widehat b_n(\nu)|\ge1/2400$.

Equation (5.5), together with periodicity (6.2), implies
$$
 \left|
 \widehat{S_m(2t)-S_n(2t)}(\nu)
 \right|
 \ge\frac{t}{2400}-32\cdot10^6t^2
 \ge\frac{t}{4800}>0.
 \tag{7.5}
$$
The last inequality holds throughout $0<t\le10^{-12}$.

Set
$$
 \phi_{mn}(q,r)=\Phi_m(2t,q,r)-\Phi_n(2t,q,r).
$$
The initial difference $\Theta_m-\Theta_n$ is a sum of a function of $q$, a function of $r$, and a constant. Its mixed derivative is zero. The marked nonzero coefficient (7.5), whose two frequency components are both nonzero, therefore proves
$$
 \partial_q\partial_r\phi_{mn}\not\equiv0.
 \tag{7.6}
$$
For example, integrating the periodic correction twice by parts multiplies its marked coefficient by $-(2\pi)^2(151/24)(1/24)$, which is nonzero.

Define the rectangular-cycle phase
$$
 \mathcal R_{mn}(q,q',r,r')
 =\phi_{mn}(q,r)-\phi_{mn}(q',r)
 +\phi_{mn}(q',r')-\phi_{mn}(q,r').
$$
Its entire initial separable part cancels. From (5.3), each of its four partial derivatives has magnitude at most $32000t$. In particular,
$$
 \max_j\|\partial_j\mathcal R_{mn}\|_\infty
 \le32000t<1/48.
 \tag{7.7}
$$
This margin suffices both for the existing step-four residue version of the sampled-matrix lemma, whose threshold is $1/8$, and for a step-24 version. The present image-phase representation has constant branch coefficients, so no step-24 splitting is actually required.

## 8. Operator cancellation and the proof of (0.1)

Expand the entrywise square of (6.3), at time $2t$. Its diagonal sheet terms give
$$
 P_{\rm self}(x,y)=
 \frac1{24N}\sum_{m=0}^{23}B_m(2t,x/N,y/N)^2.
 \tag{8.1}
$$
By (5.3), every entry of $P_{\rm self}-J_N$ has absolute value at most $8\cdot10^6t/N$. Its operator norm is therefore at most $8\cdot10^6t$, using row and column absolute sums.

Every one of the remaining 552 ordered sheet pairs is the matrix
$$
 \frac1{24N}
 B_m(2t,x/N,y/N)B_n(2t,x/N,y/N)
 e^{2\pi iN\phi_{mn}(x/N,y/N)}.
 \tag{8.2}
$$
Its amplitude is smooth with fixed bounded derivatives; its phase is real analytic on a connected neighborhood of the real square. Equations (7.6)--(7.7) verify the two substantive hypotheses of the sampled oscillatory matrix lemma in Section 1 of the round-5 source
$$
 \text{root\_oscillatory\_matrix\_cancellation.md}.
$$
That lemma was independently audited in
$$
 \text{audit\_sampled\_oscillatory\_matrix.md}.
$$
It proves norm convergence to zero for each pair of row and column residue classes modulo four. Splitting (8.2) into its 16 such blocks and summing them proves norm convergence to zero for (8.2) itself, along all integers $N$. This step uses a fixed finite number of phases and blocks.

To recall why the lemma applies without an unstated stationary-phase assumption: its fourth Schatten power has precisely the rectangular-cycle phase $\mathcal R_{mn}$. After a smooth boundary cutoff, Poisson summation separates the aliases. Every nonzero alias has a phase derivative bounded away from zero by (7.7), and six integrations by parts give an absolutely summable vanishing bound in four dimensions. The zero alias has nonconstant real analytic phase by (7.6). Its critical set has measure zero; deleting a small neighborhood of that set and integrating by parts proves convergence to zero. The removed boundary and critical neighborhoods are controlled before their cutoffs are sent to zero. No uniform rate in $t$ is required, since $t$ is fixed.

Combining the vanishing cross-sheet norms with (8.1) and the proved physical error (6.7) gives (0.1).

In particular, writing
$$
 P_N=|U_N|^2,\qquad
 D_N=|U_N^2|^2-P_N^2,
$$
the original round-5 bound $\|P_N-J_N\|\le40000t+o(1)$ gives
$$
 \boxed{
 \|D_N\|_{\rm op}
 \le8\cdot10^6t+(40000t)^2+o(1).
 }
 \tag{8.3}
$$
Here $P_N^2=J_N+(P_N-J_N)^2$ exactly, because $P_N$ is doubly stochastic. The right side of (8.3) is much smaller than $1/4$ at the fixed original parameter. Thus
$$
 \|P_N-J_N\|\le1/4,\qquad \|D_N\|\le1/4
 \tag{8.4}
$$
for every sufficiently large odd $N$.

## 9. Removal of the whole signed class of isolated substitutions

For two actual rooted words $x,y$ of length $n$, define their literal mismatch set
$$
 I(x,y)=\{j\in\mathbb Z/n\mathbb Z:x_j\ne y_j\}.
$$
Let $\mathcal C_n^{(2)}$ be the class for which this set is nonempty and every cyclic gap is at least two. No occupation condition is imposed. Write
$$
 F_n^{(2)}(U)=
 \sum_{(x,y)\in\mathcal C_n^{(2)}}a_U(x)\overline{a_U(y)}.
 \tag{9.1}
$$
Every such pair occurs once. Defects may occupy up to half the positions, their labels are arbitrary, and repeated or periodic words are allowed.

The exact defect contraction proved in the companion isolated-sector note gives, for a fixed mismatch set of size $r$, with cyclic gaps $g_i\ge2$,
$$
 \sum_{I(x,y)=I}a_U(x)\overline{a_U(y)}
 =\operatorname{Tr}\bigl(D P^{g_1-2}\cdots D P^{g_r-2}\bigr),
 \quad D=|U^2|^2-P^2.
 \tag{9.2}
$$
Since both matrices in the difference defining $D$ are doubly stochastic, $DJ=JD=0$. Every positive-length $P$ arc can therefore be replaced by $E=P-J$; zero-length arcs remain the identity.

The entry bound (6.6) and the previously proved original entry bound $|U_N(x,y)|\le3/\sqrt N$ remove a potential dimension factor in this contraction. Indeed, every nonnegative doubly stochastic matrix $R$ with $R_{ab}\le C/N$ satisfies
$$
 \|R-J\|_{\rm HS}^2=\sum_{a,b}R_{ab}^2-1\le C-1.
$$
Consequently, with $E=P_N-J_N$ and $D=D_N$,
$$
 \|E\|_{\rm HS}\le\sqrt8,\qquad
 \|D\|_{\rm HS}
 \le\bigl\||U_N^2|^2-J_N\bigr\|_{\rm HS}
       +\|E^2\|_{\rm HS}
 \le\sqrt{35}+\frac{\sqrt8}{4}<7.
 \tag{9.3}
$$
Both operator norms are at most $q_0=1/4$ by (8.4). A pattern with $r$ defects has exactly $f=r+(n-2r)=n-r$ factors after writing every common arc as a product of individual $E$'s. When $n\ge3$, the spacing restriction implies $f\ge2$. Split the cyclic trace at any two such factors, apply Hilbert--Schmidt Cauchy--Schwarz to those two, and bound all remaining factors in operator norm. The fully contracted pattern sum has modulus at most
$$
 49q_0^{\,n-r-2}=784q_0^{\,n-r}.
 \tag{9.4}
$$
Thus no factor $N$ is needed.
The exact number of literal cyclic $r$-point mismatch sets is
$$
 c_{n,r}=\frac nr\binom{n-r-1}{r-1},\qquad n\ge2r.
$$
Equivalently, their weighted sum is
$$
 Z_n(q,d)=
 \operatorname{Tr}\begin{pmatrix}q&d\\1&0\end{pmatrix}^{n}-q^n.
 \tag{9.5}
$$
These counts, including zero-length arcs and singleton mismatch sets, are proved in the companion note and checked there by exact enumeration.

The two eigenvalues in (9.4) are
$$
 \lambda_\pm=(q\pm\sqrt{q^2+4d})/2.
$$
Since $q_0^{n-r}=d^r q^{n-2r}$ with $q=d=q_0=1/4$, summing (9.4) uses exactly this scalar partition function. The positive eigenvalue is $(1+\sqrt{17})/8<2/3$. Hence, for $n\ge3$,
$$
 \boxed{
 |F_n^{(2)}(U_N)|
 \le1568\left(\frac{1+\sqrt{17}}8\right)^n
 \le1568(2/3)^n.
 }
 \tag{9.6}
$$
The term at $n=1$ is empty. At $n=2$, there are two singleton mismatch sets, and
$$
 F_2^{(2)}=2\operatorname{Tr}D.
$$
Both terms in $\operatorname{Tr}D=\operatorname{Tr}|U_N^2|^2-\operatorname{Tr}P_N^2$ are nonnegative. The first is at most $36$ by (6.6), and the second is at most $9$, because
$$
 \sum_{a,b}P_{ab}P_{ba}
 \le(9/N)\sum_{a,b}P_{ba}=9.
$$
Therefore $|F_2^{(2)}|\le72$.

The exact scalar generating sum gives a sharper all-time estimate:
$$
 \sum_{n\ge1}Z_n(q,d)
 =\frac{d(2-q)}{(1-q-d)(1-q)}
 =\frac76.
$$
Here $Z_1=0$ and $Z_2=2d=1/2$, so $\sum_{n\ge3}Z_n=2/3$. Combining this with (9.4), for any bounded weights $|w_{n,N}|\le W$,
$$
 \boxed{
 \sum_{n\ge1}|F_n^{(2)}(U_N)|
 \le72+784\frac23=\frac{1784}{3}<600,
 }
 \tag{9.7}
$$
$$
 \boxed{
 \frac1{N^2}\left|\sum_{n\ge1}w_{n,N}F_n^{(2)}(U_N)\right|
 <\frac{600W}{N^2}.
 }
 \tag{9.8}
$$
The modulus in this argument is taken after summing all labels for a fixed literal mismatch set. The essential cancellation $DJ=JD=0$ and the new bound (8.3) are applied before that modulus.

The class in (9.1) includes both equal and unequal occupations. Formulas (9.7)--(9.8) are therefore not bounds on its unequal-occupation part alone. In particular they do not supersede the different gap-three result in the companion note, where the equal occupations were removed by an exact phase coefficient extraction. Nor can signed estimates for overlapping classes be combined by a monotone union bound.

The rest of the original double-trajectory sum still includes pairs with adjacent mismatches and extended changed runs. Its required weighted asymptotic has not been evaluated, and the higher factorial orders in $H_{\rm diag}$ remain separate requirements.

## 10. Verification boundary

All new kernel identities, normalizations, flow bounds, phase coefficients, deck relations, and the residual estimate are proved above. The sole longer analytic input imported from the prior round is its explicitly stated and already proved sampled oscillatory matrix lemma; its hypotheses have been checked for every new sheet pair. This is a theorem about a new physical two-step operator for the fixed original family, not a small-$N$ experiment or a generic unitary implication. Independent audit of this new note is still appropriate before treating it as frozen research output.
