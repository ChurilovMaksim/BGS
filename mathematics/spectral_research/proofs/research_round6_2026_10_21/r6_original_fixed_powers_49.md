> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_original_fixed_powers_49.md`. Embedded SHA256: `3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019`.
> [Thematic guide](../../topics/arithmetic.md).

# Exact sheet characters and physical mixing of the first 49 powers

21 October 2026. This note extends the new two-step physical kernel argument to a proved finite range of powers of the exact original matrix. Its main structural observation is an exact translation law for the nonlinear sheet actions. Consequently, separation of all sheets reduces to one Fourier coefficient, with no loss from the possibly enormous number of sheets in the perturbative comparison.

The original kick remains $t=10^{-80}/(2\pi)$. No uniform claim for unbounded powers is made. The explicit quantitative criterion below is verified for every $1\le R\le49$ and fails for $R\ge50$. Failure of this sufficient criterion is not failure of the corresponding physical mixing statement.

## 1. Statement and explicit constants

Let
$$
 \mathsf S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
 \mathsf S^j=\begin{pmatrix}a_j&b_j\\c_j&a_j\end{pmatrix},
 \qquad j\ge0.
 \tag{1.1}
$$
Here $a_0=1,b_0=c_0=0$, and
$$
 a_{j+1}=3a_j+2b_j,\qquad
 b_{j+1}=4a_j+3b_j,\qquad
 c_{j+1}=2a_j+3c_j.
 \tag{1.2}
$$
For $j\ge1$, $b_j=2c_j>0$, $a_j$ is odd, $b_j,c_j$ are even, and
$$
 a_j^2-b_jc_j=1,\qquad 0<a_j/b_j<1.
 \tag{1.3}
$$
All of these statements follow by induction from (1.1)--(1.2).

Define
$$
 L_j=9(a_j+b_j),\qquad
 \Sigma_R=\sum_{j=0}^{R-1}L_j,\qquad
 \Lambda_R=\sum_{j=0}^{R-1}L_j^2.
 \tag{1.4}
$$
The convenient closed formula
$$
 \boxed{\Sigma_R=\frac92(a_R-1)}
 \tag{1.5}
$$
follows by summing the first coordinate of
$$
 \sum_{j=0}^{R-1}\mathsf S^j\binom11
 =(\mathsf S^R-I)\binom{1/2}{0}.
$$
Indeed $(\mathsf S-I)(1/2,0)^T=(1,1)^T$.

**Theorem.** Fix $R\ge1$. If
$$
 \boxed{51200t\Sigma_R^2\le1,}
 \tag{1.6}
$$
then, along every odd $N\to\infty$, the exact original matrices satisfy
$$
 \boxed{
 \bigl\||U_N^R|^2-J_N\bigr\|_{\rm op}
 \le256t\Lambda_R+o_R(1).
 }
 \tag{1.7}
$$
For every sufficiently large odd $N$, they also satisfy
$$
 \boxed{
 \max_{x,y}|U_N^R(x,y)|\le
 \frac{2\sqrt{b_R}}{\sqrt N}.
 }
 \tag{1.8}
$$
The constants and threshold in (1.8) may depend on the fixed $R$. The absolute squares in (1.7) are entrywise.

At the prescribed $t$, condition (1.6) holds for every $1\le R\le49$. Since $\Lambda_R\le\Sigma_R^2$, (1.7) has limiting upper bound at most $1/200$. Therefore there is a single threshold $N_*$ such that, simultaneously for this finite set of powers and every odd $N\ge N_*$,
$$
 \boxed{
 \max_{1\le R\le49}
 \bigl\||U_N^R|^2-J_N\bigr\|_{\rm op}\le1/100.
 }
 \tag{1.9}
$$
The finite maximum in (1.9) does not assert uniformity over all positive powers.

For example, the next new power $R=3$ has $a_3=99,b_3=140$, $\Sigma_3=441$, and $\Lambda_3=140211$. Thus the explicit conclusion includes
$$
 \bigl\||U_N^3|^2-J_N\bigr\|
 \le35894016t+o(1),\qquad
 \max_{x,y}|U_N^3(x,y)|\le2\sqrt{140}/\sqrt N
$$
for every sufficiently large odd $N$, including multiples of five or seven.

## 2. The sharper Fourier majorant

Use the corrected ordinary-half symbol $a(q,p)$ in the two-step note, with exact quantization $A_N=Q_N(a)$. Its coefficients satisfy the explicit majorant
$$
 \boxed{
 \sum_{k,l}|\widehat a(k,l)|\le593/500<2.
 }
 \tag{2.1}
$$
Here is a direct derivation without relying on numerical coefficient evaluation. The real, $p$-independent part is
$$
 \frac9{10}\cos14\pi q+\frac1{10}\cos2\pi q
 -\frac1{20}\cos12\pi q-\frac1{20}\cos16\pi q.
$$
Its coefficient one-norm is $11/10$. Writing $u=2\pi q$, the remaining $p$-independent sine numerator is
$$
 r(q)\sin u
 =\sin u+\tfrac12\sin2u+\tfrac14\sin5u
 +\tfrac12\sin6u-\tfrac12\sin8u-\tfrac14\sin9u.
$$
Its coefficient one-norm after division by 100 is $3/100$.

Finally the $p$-dependent term is
$$
 \frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0).
$$
The coefficient one-norm of $r$ is four. The sum of the absolute real and imaginary parts of $e^{i\alpha_0}=(-3+4i)/5$ is $7/5$. Thus the sum of absolute real and imaginary coefficient parts for this term is at most $4(7/5)/100=7/125$. Bounding each complex modulus by that sum and adding the three contributions gives
$$
 11/10+3/100+7/125=593/500.
$$
Overlaps can only lower the coefficient one-norm. The Fourier support still has $|k|+|l|\le9$ and $|l|\le1$.

The exact ordinary-half covariance, proved in Section 1 of the two-step note, gives
$$
 M_N^jA_NM_N^{-j}=Q_N(H_j),\qquad
 H_j(q,p)=a(a_jq+b_jp,c_jq+a_jp).
 \tag{2.2}
$$
The integer Fourier label map is
$$
 (k,l)\mapsto(a_jk+c_jl,b_jk+a_jl).
$$
It is invertible and preserves both label parities, since $\mathsf S^j\equiv I\pmod2$. Hence (2.2) has no hidden ordinary-half sign. It preserves the coefficient one-norm, and its support obeys
$$
 |k|+|l|\le L_j.
 \tag{2.3}
$$

Let $L_{\max}=L_{R-1}$ and $\delta=(100L_{\max})^{-1}$. On the complex tube of width $\delta$, every $H_j$, $j<R$, satisfies
$$
 |H_{j,q}|,|H_{j,p}|\le8L_j,\qquad
 \|D(-H_{j,p},H_{j,q})\|_{\infty\to\infty}\le64L_j^2.
 \tag{2.4}
$$
Indeed the Fourier exponential factor is at most
$$
 e^{2\pi\delta L_j}\le e^{\pi/50}
 <e^{1/15}\le15/14.
$$
The last inequality follows directly from $e^x\le(1-x)^{-1}$ for $0\le x<1$, by comparison of their positive power series. With $\pi<22/7$, the respective coefficient factors are bounded by
$$
 \frac{593}{500}\frac{44}{7}\frac{15}{14}
 =\frac{19569}{2450}<8,
$$
$$
 \frac{593}{500}\left(\frac{44}{7}\right)^2\frac{15}{14}
 =\frac{430518}{8575}<64.
$$
Every fixed higher derivative has a finite bound on a smaller tube.

## 3. Exact images of $M_N^R$ and the evolution order

The original power factorizes exactly as
$$
 U_N^R=
 e^{itQ_N(H_0)/h}
 e^{itQ_N(H_1)/h}\cdots
 e^{itQ_N(H_{R-1})/h}M_N^R,
 \qquad h=(2\pi N)^{-1}.
 \tag{3.1}
$$
Thus the initial kernel is evolved first under $H_{R-1}$, then under $H_{R-2}$, and finally under $H_0$, for time $t$ at each stage.

Put $a=a_R,b=b_R,c=c_R$. The same direct polynomial proof as in Section 3 of the two-step note gives
$$
 M_N^R(x,y)=
 \frac{\eta_{R,N}}{\sqrt{bN}}
 \sum_{m=0}^{b-1}
 \exp\left[
 -\frac{2\pi i}{2bN}
 \{ax^2-2x(y+mN)+a(y+mN)^2\}
 \right],
 \qquad|\eta_{R,N}|=1.
 \tag{3.2}
$$
Here all conditions used in that proof are checked in (1.3): $a^2-bc=1$, $b,c$ are even, and $a$ is odd. In detail, the polynomial
$$
 Q(x,Y)=ax^2-2xY+aY^2
$$
intertwines the shift and multiplication generators with the labels $(a,c)$ and $(b,a)$. Their commutant consists only of scalars. Periodicity follows from
$$
 Q(x+N,Y+aN)-Q(x,Y)=bc(2YN+aN^2)
$$
and $m\mapsto m+b$. For $g=\gcd(N,b)$, squaring the finite $m$-Gauss sum gives
$$
 \frac gN{\bf1}_{\{g\mid x-ay\}}.
 \tag{3.3}
$$
Since $N$ is odd, $g$ is odd and $b/g$ is even, which is the only parity needed to eliminate its remaining quadratic phase. Row norms equal one, so the scalar has modulus one. No assumption that $b$ is invertible modulo $N$ is used.

Use image phases
$$
 \Theta_m(q,s)=
 -\frac{aq^2-2q(s+m)+a(s+m)^2}{2b},
 \qquad
 p_m(q,s)=\frac{-aq+s+m}{b}.
 \tag{3.4}
$$
The letter $s$ here is the initial coordinate, not evolution time.

## 4. Quantitative characteristic construction under (1.6)

Evolve the initial graph $(u,p_m(u,s))$ through the $R$ stages in (3.1), using
$$
 \dot Q=-H_{j,p}(Q,P),\qquad \dot P=H_{j,q}(Q,P)
$$
on its stage. Define the total gradient and derivative majorants
$$
 \mathcal G=8t\Sigma_R,\qquad
 \mathcal L=64t\Lambda_R.
 \tag{4.1}
$$
Condition (1.6) gives
$$
 \mathcal L\le1/800,\qquad
 \frac{\mathcal G}{\delta}
 =800tL_{\max}\Sigma_R
 \le800t\Sigma_R^2\le1/64.
 \tag{4.2}
$$
Start the initial coordinate parameters in a sufficiently small fixed fraction of the tube of width $\delta$. The initial slope $-a/b$ has magnitude less than one. The displacement estimate in (4.2) keeps every characteristic in the larger tube throughout all stages. Picard iteration for the integral equations, with the integrated derivative bound $\mathcal L<1$, gives unique analytic dependence on the initial parameters.

The integrated variational equation gives
$$
 \|D(Q,P)-I\|_{\infty\to\infty}
 \le e^{\mathcal L}-1\le2\mathcal L.
 \tag{4.3}
$$
Along the initial tangent $(1,-a/b)$, this implies
$$
 |\partial_uQ-1|\le2\mathcal L<1/2.
$$
Thus $u\mapsto Q$ has a global increasing real inverse and a uniformly defined analytic local inverse. The same contraction argument as in the two-step construction applies, with the integrated bounds in place of a constant vector-field bound.

The characteristic action and the amplitude $B_m=(\partial_uQ)^{-1/2}$ define final functions $\Phi_m(q,s)$, $B_m(q,s)>0$. Their intermediate versions satisfy the Hamilton--Jacobi and transport equations on each stage and join continuously. The variations of the action give
$$
 \Phi_q=P,\qquad
 \Phi_s=(u-a(s+m))/b.
 \tag{4.4}
$$
Write $S_m=\Phi_m-\Theta_m$. The momentum and inverse-coordinate displacements give
$$
 |S_{m,q}|\le2\mathcal G=16t\Sigma_R,\qquad
 |S_{m,s}|\le\mathcal G/b=8t\Sigma_R/b.
 \tag{4.5}
$$
The amplitude bound is
$$
 \boxed{|B_m^2-1|\le4\mathcal L=256t\Lambda_R.}
 \tag{4.6}
$$

For the first-order phase comparison define
$$
 \beta_m(q,s)=\sum_{j=0}^{R-1}H_j(q,p_m(q,s)).
 \tag{4.7}
$$
Let $G(v)$ be $8L_j$ on the stage where $H_j$ is active. Up to time $v$, the momentum correction at a fixed endpoint is at most $2\int_0^vG(w)\,dw$, by the same argument as (4.5). Integrating the Hamilton--Jacobi equation at fixed endpoints therefore gives
$$
 \begin{aligned}
 |S_m-t\beta_m|
 &\le2\int_0^{Rt}G(v)\int_0^vG(w)\,dw\,dv\\
 &=\left(\int_0^{Rt}G(v)\,dv\right)^2
 =64t^2\Sigma_R^2.
 \end{aligned}
 \tag{4.8}
$$
This estimate uses the sum of the stage derivative bounds. Replacing it by the number of stages times the largest bound would unnecessarily lose a factor of order $R^2$.

## 5. Exact nonlinear sheet characters

The initial phases satisfy, for all integers $m$,
$$
 \begin{split}
 \Theta_{m+b}(q,s)&=\Theta_m(q,s)+q-a(s+m)-ab/2,\\
 \Theta_m(q+1,s)&=\Theta_{m-a}(q,s)-c(s+m)+ac/2,\\
 \Theta_m(q,s+1)&=\Theta_{m+1}(q,s).
 \end{split}
 \tag{5.1}
$$
All evolution symbols are periodic in both phase-space coordinates. Their characteristic uniqueness therefore propagates these identities to the nonlinear phases, with the corresponding identities for amplitudes. Subtracting the initial phases shows that $S_m,B_m$ are $b$-periodic in each endpoint coordinate.

More specifically, there is the exact identity
$$
 \boxed{S_m(q,s)=S_0(q,s+m).}
 \tag{5.2}
$$
It follows from the literal equality of the initial phase and initial graph with $s$ replaced by $s+m$; every evolution symbol is independent of the endpoint parameter $s$. This identity does not truncate the dynamics in $t$.

Fourier coefficients below are those of the $b$-periodic endpoint functions. Choose
$$
 \nu_R=\left(7-\frac ab,\frac1b\right).
 \tag{5.3}
$$
Both components are nonzero. The original symbol has $\widehat a(7,1)=e^{-i\alpha_0}/400$.

The $j=0$ summand in (4.7) contributes exactly this original mode at $\nu_R$. There is no collision with any $j\ge1$. To see this without enumerating the growing Fourier support, observe that a transformed label would have to equal $(7,1)$. The unique candidate original label is
$$
 (k,l)=
 \begin{pmatrix}a_j&-c_j\\-b_j&a_j\end{pmatrix}
 \binom71
 =(7a_j-c_j,a_j-7b_j).
 \tag{5.4}
$$
For $j\ge1$, $a_j<b_j$ and $b_j\ge4$, so $l=a_j-7b_j<-6b_j\le-24$. This is outside the original support $|l|\le1$. Thus
$$
 \widehat{\beta_0}(\nu_R)=e^{-i\alpha_0}/400.
 \tag{5.5}
$$

Set $C_R(t)=\widehat S_0(\nu_R)$. By (4.8) and (1.6),
$$
 \left|C_R(t)-\frac{te^{-i\alpha_0}}{400}\right|
 \le64t^2\Sigma_R^2\le t/800,
$$
and therefore
$$
 \boxed{|C_R(t)|\ge t/800>0.}
 \tag{5.6}
$$
Exact translation (5.2) now gives, for any two distinct sheet labels $m,n\pmod b$,
$$
 \boxed{
 \widehat{S_m-S_n}(\nu_R)
 =C_R(t)\bigl(e^{2\pi im/b}-e^{2\pi in/b}\bigr)\ne0.
 }
 \tag{5.7}
$$
This is the exact sheet-character factorization. In particular no factor $b$ appears in the sufficient smallness condition (1.6).

The initial phase difference $\Theta_m-\Theta_n$ is separable in the endpoints. Hence (5.7) proves that $\Phi_m-\Phi_n$ has a mixed derivative that is not identically zero. Its rectangular-cycle phase loses the entire initial part; (4.5) bounds every component of its gradient by
$$
 64t\Sigma_R
 \le\frac1{800\Sigma_R}<1/8.
 \tag{5.8}
$$

## 6. Kernel error and the physical operator limit

At every intermediate time, the $b$-image kernel
$$
 V_{R,N}(x,y)=
 \frac{\eta_{R,N}}{\sqrt{bN}}
 \sum_{m=0}^{b-1}B_m(x/N,y/N)e^{i\Phi_m(x/N,y/N)/h}
 \tag{6.1}
$$
has exactly periodic columns. To check the boundary, the second identity in (5.1) adds
$$
 -cy-cNm+acN/2\in\mathbb Z
$$
to the exponent after multiplying by $N$; reducing $m$ modulo $b$ adds
$$
 x-ay-aNm-abN/2\in\mathbb Z.
$$
Here $ac,ab$ are even. Thus the exact finite-shift formula may be applied to the smooth branch extensions at every wrapped shift.

Each of the finitely many symbols $H_j$ has a fixed finite Fourier support. Taylor expansion of its finite shifts gives precisely the phase and transport equations, with residual $O_R(h/\sqrt N)$ on each entry. The explicit first-order expansion and its sign are proved in Section 6.1 of the two-step note; it uses only a real finite Fourier symbol and bounded phase and amplitude derivatives, both established here. There are $R$ fixed stages and $b$ fixed branches, so the residual constant may depend on $R$ but not on $N$ or the column. The unitarity of each exact stage and Duhamel's formula give
$$
 \|(U_N^R-V_{R,N})e_y\|_2=O_R(h),\qquad
 \|U_N^R-V_{R,N}\|_{\rm HS}=O_R(h\sqrt N).
 \tag{6.2}
$$
No long-time Egorov theorem is invoked.

The amplitude bound (4.6) is at most $1/200$. Hence
$$
 |V_{R,N}(x,y)|\le\sqrt{b(1+1/200)}/\sqrt N.
$$
Combining this with the column error proves (1.8) for all sufficiently large odd $N$. It also proves
$$
 \bigl\||U_N^R|^2-|V_{R,N}|^2\bigr\|_{\rm HS}=O_R(N^{-1}).
 \tag{6.3}
$$

The equal-sheet terms in the entrywise square are
$$
 \frac1{bN}\sum_{m=0}^{b-1}B_m(x/N,y/N)^2.
$$
Their difference from $J_N$ has operator norm at most $256t\Lambda_R$ by (4.6) and the row-column bound. For every pair of distinct sheets, the corresponding matrix has smooth amplitude, analytic phase with a nonzero mixed derivative by (5.7), and rectangular-cycle gradient less than $1/8$ by (5.8). The proved sampled oscillatory matrix lemma from round 5 therefore gives operator norm $o_R(1)$ for each term. One can apply its original formulation by splitting each term into the 16 row-column residue blocks modulo four. The number of sheets and terms is finite for each fixed $R$; no uniform rate in $R$ is needed.

Combining the equal-sheet bound, the vanishing cross-sheet norms, and (6.3) proves (1.7).

## 7. Exact certification of the range through 49

Recurrence (1.2), or the closed formula (1.5), gives exactly
$$
 a_{49}=16255007246704249599863612909970798723,
$$
$$
 \Sigma_{49}=73147532610169123199386258094868594249
 <74\cdot10^{36}.
$$
Using $t<10^{-80}/6$,
$$
 51200t\Sigma_{49}^2
 <\frac{51200\cdot74^2}{6\cdot10^8}
 =\frac{280371200}{600000000}<\frac12<1.
 \tag{7.1}
$$
The positive sequence $\Sigma_R$ is increasing, so (1.6) holds for every $R\le49$. This is an integer comparison, not a floating-point test of a very small parameter.

For comparison,
$$
 \Sigma_{50}=426335063173366200380428859644050080712
 >426\cdot10^{36}.
$$
The lower bound $t>10^{-80}/7$, from $2\pi<7$, gives
$$
 51200t\Sigma_{50}^2
 >\frac{51200\cdot426^2}{7\cdot10^8}>1.
 \tag{7.2}
$$
Thus the stated sufficient criterion does fail for $R=50$, and by monotonicity for every larger $R$. This is a limit of this explicit estimate, not a counterexample to mixing of those powers.

The companion exact-arithmetic script verifies the recurrences, formula (1.5), the Fourier coefficient majorants, the noncollision formula, all parity and determinant conditions, and the rational comparisons (7.1)--(7.2).

It completed successfully, including 2700 exact rational polynomial identities for the deck transformations and intermediate endpoint coordinates. It verifies the threshold using both a rational upper bound and a rational lower bound for the actual $t$; its conclusion that (1.6) fails at 50 does not follow merely from failure of an upper bound to certify it.

## 8. Scope for long trajectory sums

The estimate concerns the actual fixed powers $U_N^R$, along all odd dimensions and without random phases. The exact nonlinear sheet character (5.7) is valid for every power whenever its characteristic construction exists; the nonzero coefficient is quantitatively proved here only under (1.6).

The entry bounds (1.8) provide proved physical input for finite first-return or finite-block decompositions. They do not justify sending the permitted block length to infinity at fixed $\tau$, nor do they evaluate trajectories with mismatch runs of order $N$. The much longer trace times occurring in $H_{\rm diag}$ are still a separate problem. No full local spectral limit or countersequence is asserted by this theorem.
