---

**Stable claim IDs:** BGS-RES-022, BGS-RES-023.
title: "Certified multiorbit resonance and an invariant Hessian obstruction"
author: "BGS research programme"
date: "6 September 2026"
---

# Abstract and status

We study the second-order cohomological variance
$\Gamma_A(g)=\sigma_A^2(\{g,g\circ A^{\mathsf T}\}/(4\pi))$ for hyperbolic
two-torus automorphisms. For the fixed Pell matrix we give a finite,
independently replayable proof that it is positive for every nonconstant real
trigonometric polynomial of frequency radius at most eight. All 288 real
parameters are arbitrary: evenness and Fourier-phase alignment are not assumed.
An exact finite quantum variance identity connects this certificate to a
period-averaged observable, with an explicit non-aliasing hypothesis.
A separate analytic theorem detects nonzero variance from the two hyperbolic
curvatures at a fixed critical point. It implies nondegeneracy, without a
bandwidth restriction, on the cone of even symbols with one-sign cosine
coefficients, for every hyperbolic integral determinant-one matrix.

These are project proofs and exact finite certificates, not a claim of world
priority or positive BGS universality. The Fourier-orbit formula for asymptotic
variance is established theory; we prove the specialized identities needed here.
The certificate is stronger than sampling real coefficients but is not a Lean
formalization. The unbounded-radius mixed-sign problem remains unresolved by
these arguments. No uniform long-time quantum comparison is inferred from a
positive classical variance alone.

# 1. Normalization and the cohomological question

Let $A\in\mathrm{SL}(2,\mathbb Z)$ be hyperbolic, $S=A^{\mathsf T}$, and
$\mathcal C_A f=f\circ S$. On the unit torus put
\[
 e_v(x)=e^{2\pi i v\cdot x},\qquad b_v=e_v+e_{-v},\qquad
 \{f,h\}=f_{x_1}h_{x_2}-f_{x_2}h_{x_1}.
\]
For a real smooth mean-zero function $h$, define
\[
 \sigma_A^2(h)=\sum_{\mathcal O}
       \left|\sum_{v\in\mathcal O}\widehat h(v)\right|^2,
 \qquad
 \Gamma_A(g)=\sigma_A^2\!\left(\frac{\{g,\mathcal C_Ag\}}{4\pi}\right),
 \tag{1}
\]
where $\mathcal O$ ranges over **oriented** $A$-orbits in
$\mathbb Z^2\setminus\{0\}$. An orbit and its negative are distinct: a
nonzero integer vector cannot be periodic under $-A^j$ for a hyperbolic $A$.
For real $h$ they contribute conjugate sums. For even $h=\sum a_v b_v$,
(1) therefore reduces to twice the sum of the squared cosine sums on signed
orbits. Constants in $g$ affect neither the bracket nor $\Gamma_A$.

For finite Fourier support, character orthogonality gives exactly
\[
 \sum_{n\in\mathbb Z}\int h(x)h(S^n x)\,dx
   =\sum_{\mathcal O}\left|\sum_{v\in\mathcal O}\widehat h(v)\right|^2.
 \tag{2}
\]
The double absolute sum is bounded by $\|\widehat h\|_1^2$, so the same
identity holds for smooth $h$ by absolute convergence. This is the usual
Green--Kubo/orbit-sum variance, not the instantaneous $L^2$ norm. Such spectral
and orbit-sum descriptions are prior theory, including Cohen--Conze [1].

For a finite polynomial $h$, $\sigma_A^2(h)=0$ if and only if $h=u-\mathcal C_Au$
for a finite polynomial $u$. Indeed, on each orbit, let $h_j$ be the finite
coefficient sequence. If its sum is zero, the partial sums
$u_j=\sum_{k\leq j}h_k$ have finite support and $h_j=u_j-u_{j-1}$.
Conversely a finite difference has zero sum. Consequently proving only
$\{g,\mathcal C_Ag\}\ne0$ does not settle the nondegeneracy question.

For Sections 2--3 fix
\[
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad
 \lambda=3+2\sqrt2.
\]
Let $\mathcal P_R$ be the real mean-zero trigonometric polynomials supported
in $\|v\|_\infty\leq R$. Its real dimension is $4R(R+1)$.

# 2. An exact finite theorem for arbitrary Fourier phases

**Theorem 1 (the full radius-eight box).** For every nonzero
$g\in\mathcal P_8$,
\[
                         \boxed{\Gamma_T(g)>0.}             \tag{3}
\]
In particular (3) holds at every smaller integer radius. There is no restriction
on the signs or phases of the Fourier coefficients. This proves that the
second-order bracket is not a finite Fourier coboundary throughout this
288-dimensional real space. The assertion is not extrapolated to all radii.

## 2.1 Exact polynomial equations

Choose
\[
 V_R=\{(a,b):0\leq a\leq R,\ -R\leq b\leq R,
                         \ a>0\text{ or }b>0\}.
\]
Write, uniquely,
\[
 g=\sum_{v\in V_R}(z_v e_v+\overline{z_v}e_{-v}),\qquad
 z_v\in\mathbb C,\qquad \|g\|_2^2=2\sum_v|z_v|^2.          \tag{4}
\]
There are $n_R=2R(R+1)$ complex variables. The exact Fourier bracket is
\[
 \widehat{\{g,\mathcal C_Tg\}/(4\pi)}(k)
       =-\pi\sum_{u+Tv=k}\det(u,Tv)\widehat g(u)\widehat g(v).
 \tag{5}
\]
Combining the coefficients along one of the two orientations of each signed
orbit gives integer-coefficient quadratic polynomials $Q_j(z,\bar z)$ with
\[
                   \Gamma_T(g)=2\pi^2\sum_j|Q_j(z,\bar z)|^2. \tag{6}
\]
Thus (3) is the assertion that all the equations $Q_j=0$ have only the zero
solution subject to the genuine complex-conjugation relation. The latter is
not replaced by treating $z$ and $\bar z$ as independent complex variables.

## 2.2 Why the orbit classification terminates and preserves phases

For $v=(a,b)$ put $\beta=b+\sqrt2 a$, $\beta'=b-\sqrt2 a$. Then
\[
 E(T^jv):=2(T^jv)_1^2+(T^jv)_2^2
       =\tfrac12(\beta^2\lambda^{2j}+\beta'^2\lambda^{-2j}). \tag{7}
\]
Both coefficients are positive for $v\ne0$. This is strictly convex as a
function of real $j$, tends to infinity at both ends, and has at most two
adjacent integer minimizers. Integer neighbour descent reaches the global
minimum. At equal energies we use a fixed lexicographic rule, including the
choice of a sign for the vector. Energy decreases in the non-tie steps, so the
algorithm cannot loop indefinitely.

Crucially, the program records the orientation bit $\epsilon$ in
$w=\epsilon T^jv$. A negative orientation contributes to the conjugate orbit,
not a second independent copy of the same complex coefficient. Adjacent
minimum ties, for example the orbit containing $(1,-2)$, are retained as
explicit normalization tests. Omitting this bit can produce an incorrect
arbitrary-phase variance even when all even-symbol tests pass.

The independent C++ constructor works in the quadratic ring with vector
$b+a\sqrt2$ and enumerates an orbit window $-16\leq j\leq16$. It fails if
a minimizer is at the boundary. Interior minimizers have the global meaning
just established by (7); the finite window is not an unproved coverage
assumption. All 1,475 nonzero radius-eight equations agree exactly, term by
term, with the independently constructed Python equations.

## 2.3 A small proof language and its soundness

The proof records known zero coefficients, known zero products, and temporary
nonzero assumptions. Only the following four rules are admitted.

**P (product).** After terms killed by established facts are deleted, an equation
has one cross monomial $a z_i^{\epsilon}z_j^{\eta}=0$, with $a\ne0$ and
$i\ne j$. Record $z_i z_j=0$, equivalently that at least one factor is zero.
Here the exponent sign denotes the variable or its conjugate, not an inverse.

**S (squares).** A sole nonzero multiple of $z_i^2$, $\bar z_i^2$, or
$|z_i|^2$ implies $z_i=0$. A sum $\sum_i a_i|z_i|^2=0$ with all nonzero
$a_i$ of one sign implies that every listed variable vanishes. A sum of
ordinary complex squares is *not* admitted by the second rule.

**D (nonzero division).** A recorded zero product and a currently assumed
nonzero factor imply that the other factor is zero. Division without this
explicit assumption is rejected.

**F (refutation).** Temporarily assume $z_i\ne0$, replay the supplied child
proof with inherited established facts, and require an actual contradiction.
If the child succeeds, conclude $z_i=0$ outside the branch. An empty child or
a branch that merely makes partial progress is rejected.

Each rule is an elementary implication over $\mathbb C$ with its usual
conjugation. Induction on the sequential deductions and refutations proves
soundness of a complete certificate. The search need not be complete: failure
to eliminate all variables is reported as UNKNOWN, never as a counterexample.
The validator replays the proof and does not trust the generator's status.

The radius-eight certificate contains 5,704 elementary deductions:
3,293 P rules, 1,077 S rules, 1,229 D rules and 105 F rules. Every one of
its 144 complex variables is eliminated. Refutations in this particular
certificate have depth one. Both Python and C++ independently reconstruct the
coefficient system and replay the deductions. Four malformed Python objects
and two malformed C++ instruction streams are required to fail closed.
This completes a finite computer-assisted proof of (3), with the analytic
normalization (5)--(7) and logical soundness above as explicit dependencies.

| Radius | Real dimension | Equations | P | S | D | F |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 23 | 0 | 3 | 0 | 0 |
| 3 | 48 | 212 | 81 | 35 | 16 | 4 |
| 8 | 288 | 1,475 | 3,293 | 1,077 | 1,229 | 105 |

The radius-eight coefficient table has SHA-256
`7462bc1a522a57741028efd6642710fa50aa271b27f21bfc6a683f578aee53f4`.
The plain-text proof has SHA-256
`ed26c33904551e11a5185d55702d781b4f2555d7a14153ceaf6e8a0b5f71d94a`.
The delivered manifest provides all source and result hashes. Hash agreement
identifies a proof object; it does not by itself prove that object sound.

# 3. A human-readable arbitrary-phase example and a quantitative margin

For $R=1$, in the order $(0,1),(1,-1),(1,0),(1,1)$, three of the exact
chosen orbit coefficients are
\[
 Q_{(-4,-4)}=-4\bar z_2^2,\quad
 Q_{(-2,-4)}=2\bar z_0^2+4|z_2|^2,\quad
 Q_{(0,-2)}=2|z_1|^2+2|z_3|^2.                              \tag{8}
\]
Their successive vanishing immediately forces all four variables to vanish.
This is not restricted to a real coefficient vector.

A useful, though not sharp, bound follows without the larger certificate:
\[
              \Gamma_T(g)\geq\frac{8\pi^2}{17}\|g\|_2^4,
                         \qquad g\in\mathcal P_1.          \tag{9}
\]
Indeed, put $x=|z_0|^2$, $y=|z_2|^2$, $w=|z_1|^2+|z_3|^2$.
Equation (8) and the reverse triangle inequality give
$\Gamma_T(g)\geq8\pi^2[(x-2y)^2+4y^2+w^2]$.
Cauchy--Schwarz gives
$(x+y+w)^2\leq(17/4)[(x-2y)^2+4y^2+w^2]$, and (4) proves (9).
The sharper even-symbol constant from the earlier project is not silently
transferred to arbitrary Fourier phases.

## A constructive margin for the radius-eight certificate

Compactness already gives some $c_8>0$ with $\Gamma_T(g)\geq c_8\|g\|_2^4$.
There is also a completely explicit, deliberately very poor lower bound:
\[
 \boxed{\displaystyle
 \Gamma_T(g)\geq \frac{\pi^2}{41472}\,2^{-2^{715}}\|g\|_2^4,
                         \qquad g\in\mathcal P_8.}          \tag{10}
\]
This number has no useful interpretation as a physical crossover estimate;
its purpose is to remove an unspecified compactness constant. It is not
claimed to approximate the sharp minimum.

Here is the quantitative compilation rule. Normalize $\max_i|z_i|=1$ and
suppose $|Q_j|\leq\delta$. Replace an exact zero fact by an upper bound
$2^L\delta^{p-kb}$ for its absolute value. The symbol $b$ appears only under
a temporary assumption $|z_i|\geq\delta^b$. Every deleted monomial is bounded
by a known coefficient bound times $|z_j|\leq1$, or by a known product bound.
In the residual row, use the triangle inequality, the minimum of the base
exponents, the maximum of their $b$ slopes, and a power-of-two upper bound on
the sum of absolute integer coefficients. P records the resulting product
bound. S takes a square root, rounding its power-of-two coefficient upward.
D subtracts $b$ from the exponent using the explicit nonzero lower bound.

At the end of a refutation child, the pivot has bound
$2^L\delta^{p-kb}$ with $p>0$. Choose $b=p/[2(k+1)]$ and require
$\delta\leq2^{-B}$ with $B\geq2(L+1)/p$. Then this bound is strictly less
than $\delta^b$, contradicting the temporary assumption. Therefore the pivot
has the unconditional bound $|z_i|<\delta^b$. Proceed through the root proof
and finally enlarge $B$ so that every coefficient is at most $1/2$.
This contradicts the normalization. All exponents and comparisons in the
compiler are exact rational arithmetic; there is no numerical interval test
on the coefficients of $g$.

For the maintained radius-eight proof the generated integer $B$ has 714 binary
digits, so the simple upper bound $B\leq2^{714}$ suffices. The preceding
argument gives $\max_j|Q_j|>2^{-B}$ on $\max_i|z_i|=1$. Since
$\|g\|_2^4\leq4n_R^2(\max_i|z_i|)^4$, (6) yields
$\Gamma_T(g)\geq[\pi^2/(2n_R^2)]2^{-2B}\|g\|_2^4$; with $n_8=144$ this
implies (10). The exact, much less conveniently printed integer and every intermediate rational bound are retained in the margin report. The original margin report was not deposited; it was reconstructed on 2026-10-21 from the deposited certificate by an exact-rational-arithmetic implementation of the compilation rule above (`computations/verification/resonance_nondegeneracy_margin.py`), and the reconstructed report is deposited at `evidence/executions/20261006/corpus-revision/final/checks/certificates-mpuvq_28/resonance_nondegeneracy_margin.json`. The reconstructed integer has 712 binary digits, confirming $B\leq2^{714}$ and hence (10) from deposited materials; two independent implementations of the compiler agree on the reconstructed integer.

# 4. An invariant Hessian obstruction for every hyperbolic matrix

The finite certificate settles a large but fixed frequency box. A separate
analytic criterion has no bandwidth restriction and is not specific to T.
Write
\[
 A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad t=a+d,\quad
 \Delta=t^2-4>0,\quad
 B_A=\begin{pmatrix}c&(d-a)/2\\(d-a)/2&-b\end{pmatrix}.
\]
The integral quadratic form
\[
 q_A(v)=v^{\mathsf T}B_Av=\det(v,Av)
\]
is A-invariant. Define, for a symmetric matrix H,
\[
 \mathcal E_A(H)=(\operatorname{tr}(B_AH))^2+\Delta\det H,
 \qquad
 \mathcal L_A=c\partial_{x_1}^2+(d-a)\partial_{x_1}\partial_{x_2}
                                  -b\partial_{x_2}^2.       \tag{11}
\]

**Theorem 2 (fixed critical-point obstruction).** Let $g$ be real smooth.
If $x_0$ is a fixed point of $S=A^{\mathsf T}$ and $dg(x_0)=0$, then
\[
 \boxed{\Gamma_A(g)=0\quad\Longrightarrow\quad
                   \mathcal E_A(\operatorname{Hess}g(x_0))=0.} \tag{12}
\]
In particular, if the two pure second derivatives in the stable and unstable
coordinate directions are both nonzero at that point, $\Gamma_A(g)>0$.
Every even $g$ is critical at the fixed point zero, but evenness is not a
hypothesis of Theorem 2. A nondegenerate extremum at a fixed point is a
sufficient condition, not a necessary one.

**Proof.** Put $h=\{g,\mathcal C_Ag\}/(4\pi)$. At a fixed point,
$e_{Av}(x_0)=e_v(x_0)$, and $q_A(Av)=q_A(v)$. Grouping the absolutely
convergent twice-differentiated Fourier series by oriented orbits gives
\[
 \mathcal L_Ah(x_0)
 =-4\pi^2\sum_{\mathcal O}q_A(v_{\mathcal O})e_{v_{\mathcal O}}(x_0)
                       \sum_{v\in\mathcal O}\widehat h(v).
 \tag{13}
\]
If the variance is zero, every orbit sum is zero, so (13) vanishes. No
regularity of a putative transfer function has been assumed.

Only the quadratic Taylor jet of g contributes to the second derivative of
its bracket at a critical point. For
$g_2=(H_{11}x_1^2+2H_{12}x_1x_2+H_{22}x_2^2)/2$, direct differentiation yields
\[
 \mathcal L_A\{g_2,g_2\circ A^{\mathsf T}\}
                         =t\mathcal E_A(H).                \tag{14}
\]
Equivalently, diagonalize S in an area-one eigenbasis. If its eigenvalues are
$\mu,\mu^{-1}$, set $\gamma=\mu-\mu^{-1}$; then $\gamma^2=\Delta$,
$\mathcal L_A=-\gamma\partial_u\partial_s$, and
\[
 \mathcal E_A(H)=\Delta H_{uu}H_{ss}.
 \tag{15}
\]
The mixed quadratic coefficient of the bracket is
$(\mu^{-2}-\mu^2)H_{uu}H_{ss}$, giving (14). This remains true for either
sign of the trace. Since $t\ne0$, (13)--(14) prove (12). End of proof.

The identity (14) was also checked as a polynomial identity with formal
matrix entries and Hessian entries. Before the determinant-one specialization,
its discriminant is $t^2-4\det A$. Two hundred integer instances provide a
separate regression, not the general proof.

The converse of (12) is false. For the Pell matrix,
\[
 g=4b_{(1,0)}-b_{(2,0)},\qquad \operatorname{Hess}g(0)=0,
 \qquad \Gamma_T(g)=25600\pi^2>0.                            \tag{16}
\]
The exact Fourier computation is retained as a negative control. A vanishing
Hessian obstruction is therefore not reported as a zero of the variance.

## A quantitative smooth version

The same obstruction has an explicit lower bound when one controls a weighted
Fourier tail. Put $C_A=|c|+|d-a|+|b|>0$, let $s>0$, and set
\[
 \mathcal H_s(h)=\sum_v|\widehat h(v)|(1+|v|_\infty)^{s+2},
 \qquad
 J=\frac{|\mathcal L_Ah(x_0)|}{4\pi^2}
   =\frac{|t\mathcal E_A(H)|}{16\pi^3}.
\]
If $J>0$, choose an integer
\[
 R\geq\max\{1,(2C_A\mathcal H_s(h)/J)^{1/s}\}.
\]
Then
\[
                  \Gamma_A(g)\geq\frac{J^2}{32C_A^2R^6}>0. \tag{17}
\]
To prove it, choose each orbit's representative of minimum frequency radius.
There are at most $8R^2$ oriented orbits meeting the radius-R box, each with
$|q_A|\leq C_AR^2$. Cauchy--Schwarz bounds their part of (13) divided by
$4\pi^2$ by $\sqrt8 C_AR^3\sqrt\Gamma$. For all other orbits, every
frequency has radius greater than R, and the sum is bounded by
$C_AR^{-s}\mathcal H_s(h)\leq J/2$. Rearranging proves (17).
This bound is for a fixed regular symbol with a nonzero obstruction. It is
not uniform over all mixed-sign Fourier polynomials.

# 5. A one-sign Fourier theorem without a bandwidth restriction

**Theorem 3.** Let $A\in\mathrm{SL}(2,\mathbb Z)$ be hyperbolic. If the
nonconstant coefficients of a real even smooth mean-zero function
$g=\sum_v c_vb_v$ all have the same sign and at least one is nonzero, then
\[
                             \Gamma_A(g)>0.                 \tag{18}
\]
This is a statement about cosine coefficients, not pointwise nonnegativity of
a mean-zero function. There is no restriction on the number of signed orbits.

**Proof.** Change the overall sign if necessary, so $c_v\geq0$, and put
\[
 M=\sum_v c_vvv^{\mathsf T}=-\operatorname{Hess}g(0)/(8\pi^2).
\]
Polarization of $q_A$ gives the exact discriminant identity
\[
 B_A(u,v)^2-q_A(u)q_A(v)=\frac\Delta4\det(u,v)^2.            \tag{19}
\]
Expanding $\mathcal E_A(M)$ and $\det M$ shows
\[
       \mathcal E_A(M)\geq\left(\sum_v c_v|q_A(v)|\right)^2>0.
 \tag{20}
\]
For clarity, each cross coefficient in the difference between the two sides
is zero or positive: if $q_A(u)q_A(v)\geq0$, its extra term is
$\Delta\det(u,v)^2$; if the signs differ, it is
$4B_A(u,v)^2$ by (19). The diagonal terms agree.
Also $q_A(v)\ne0$ for a nonzero integer v: otherwise A would have a rational
eigenline and a rational algebraic-unit eigenvalue, hence eigenvalue $1$ or
$-1$, contrary to hyperbolicity. Absolute smooth convergence justifies the
sums. Equation (12), or (14), now proves (18). End of proof.

For an even finite Fourier polynomial, there is a useful exact identity behind
this criterion. If $a_{\mathcal O}$ denotes the cosine sum of h on a signed
orbit, then
\[
 \boxed{\sum_{\mathcal O}q_A(v_{\mathcal O})a_{\mathcal O}(h)
                         =-2\pi t\mathcal E_A(M).}          \tag{21}
\]
It follows from (13)--(14) using
$\mathcal L_A b_v(0)=-8\pi^2q_A(v)$ and
$\mathcal E_A(-8\pi^2M)=64\pi^4\mathcal E_A(M)$.
Thus this test excludes a *nonzero coboundary bracket*, not just an
identically zero bracket.

A coarse finite-bandwidth constant is explicit. Define
\[
 m_A=\gcd(|c|,|d-a|,|b|),\quad C_A=|c|+|d-a|+|b|,\quad
 D_A=1+\max\{|a|+|b|,|c|+|d|\}.
\]
For the one-sign class supported in $\|v\|_\infty\leq R$,
\[
 \boxed{\displaystyle
 \Gamma_A(g)\geq
 \frac{\pi^2t^2m_A^4}{2C_A^2D_A^6}\,R^{-6}\|g\|_2^4.}      \tag{22}
\]
Indeed, all generated frequencies lie in the radius-$D_AR$ box. Choosing
representatives from those generated frequencies gives
$\sum_{\mathcal O}q_A(v_{\mathcal O})^2\leq4C_A^2(D_AR)^6$.
Cauchy--Schwarz in (21), (1), (20), and
$|q_A(v)|\geq m_A$, $\|g\|_2^2=2\sum c_v^2$, prove (22).
For the Pell matrix this specializes to
\[
                \Gamma_T(g)\geq\frac{\pi^2}{32768R^6}\|g\|_2^4.
 \tag{23}
\]
No sharpness is claimed. There is no conflict with superpolynomially small
positive variances of general Fourier approximations to smooth flat symbols:
those approximations need not have one-sign coefficients.

# 6. An exact finite quantum variance consequence

The elementary second-moment bridge already occurs in earlier project notes.
We reprove it here with an explicit integer sufficient bound so its application
to Theorem 1 is auditable without a Gaussian-limit theorem. Let K be any odd positive integer greater
than one, write
\[
 N+F\sqrt2=(1+\sqrt2)^K,
 \qquad T=\begin{pmatrix}3&2\\4&3\end{pmatrix},
\]
and use the physical Weyl operators
\[
 Q_N(a,b)=(-1)^{ab}W_N(a,b),\qquad
 Q_N(v)Q_N(w)=e^{\pi i\det(v,w)/N}Q_N(v+w).
\]
Here $W_N$ uses modular division by two and is an orthonormal operator basis
in normalized full-space Hilbert--Schmidt norm. Take $U_N$ with the exact
covariance $U_NQ_N(v)U_N^*=Q_N(Tv)$. Such a unitary is explicitly furnished
by the cat kernel in the earlier project; its phase is immaterial here.
Primality of K is not needed in this section.

Put $H=(K-1)/2$ and let $r_1,r_2$ be the absolute row sums of $T^H$.
For a real mean-zero polynomial h supported in $\|v\|_\infty\leq M$, assume
\[
                    N^2>M^2(4+4r_1+2r_2).                  \tag{24}
\]
Define
\[
 X_{K,N}(h)=\frac1{\sqrt K}\sum_{j=0}^{K-1}
                    U_N^j\operatorname{Op}_N(h)U_N^{-j}.
\]
Then the following equality is **exact at finite N** on the full space:
\[
             \boxed{\frac1N\operatorname{Tr}X_{K,N}(h)^2
                                  =\sigma_T^2(h).}          \tag{25}
\]
No parity assumption is made. The equality is not an assertion about individual
eigenphase spacings of a kicked propagator.

**Proof.** The Pell norm gives $N^2-2F^2=-1$, whence
\[
 T^K=\begin{pmatrix}2N^2+1&2NF\\4NF&2N^2+1\end{pmatrix}
                           \equiv I\pmod{2N}.               \tag{26}
\]
Thus $Q_N(T^Kv)=Q_N(v)$, including its physical sign, and adjoint covariance
has period K. Differences of times can be reduced to $-H\leq s\leq H$.

Let $u,v$ lie in the frequency box and suppose $u+T^sv\equiv0\pmod N$.
Use the indefinite integral norm $q(a,b)=b^2-2a^2$, invariant under T and
nonzero on every nonzero integer vector. Since the row absolute sums of
$T^s$ are bounded by those of $T^H$,
\[
 |q(u+T^sv)|
 \leq |q(u)|+|q(v)|+2|u_2(T^sv)_2-2u_1(T^sv)_1|
 \leq M^2(4+4r_1+2r_2).
\]
If $u+T^sv$ were nonzero, its norm would be a nonzero integer multiple of
$N^2$, contradicting (24). Hence the congruence lifts to the exact relation
$u=-T^sv$ in $\mathbb Z^2$.

Expand the square in (25). Cyclicity of trace and covariance reduce its
normalized value to
\[
 \sum_{s=0}^{K-1}\frac1N\operatorname{Tr}
        \bigl(\operatorname{Op}_N(h)\operatorname{Op}_N(\mathcal C_T^s h)\bigr).
\]
Weyl traces vanish except at the zero modular frequency. Every surviving
relation lifts as above; its two Weyl factors are adjoints and have product I,
with no residual phase. There is no double counting of an integer relation
since a nonzero integer vector has no nontrivial T-period. Conversely, any
integer orbit relation between supported frequencies reduces modulo K and
lifts back to the same centered relation. Thus the sum is exactly the
oriented-orbit expression (1). End of proof.

For $g\in\mathcal P_8$, its symbol $h_g=\{g,\mathcal C_Tg\}/(4\pi)$ is
supported in the radius-64 box. At $K=13$, $N=47321$, the two sides of the
sufficient inequality (24) are the exact integers
\[
 N^2=2239277041>935895040=64^2(4+4r_1+2r_2).
\]
Therefore (25) and Theorem 1 give a strictly positive quantum averaged-symbol
variance for **every nonzero** such $g$ at that module, not just the sampled
coefficients. The same conclusion holds at every odd K satisfying (24);
for each fixed M the condition holds eventually because its right side grows
like $\lambda^{K/2}$ and $N^2$ grows like $\lambda^K$.

The actual finite quantum commutator differs from that symbol by a controlled
remainder. Put $G_N=\operatorname{Op}_N(g)$,
$D_N=U_NG_NU_N^*$ and $R_N=(iN/2)[G_N,D_N]$. The sine remainder gives
\[
 \|R_N-\operatorname{Op}_N(h_g)\|_{\rm op}
     \leq\frac{\pi^3}{6N^2}M_3(g)M_3(\mathcal C_Tg),
 \qquad M_3(a)=\sum_v|\widehat a(v)|\,|v|_2^3.
\]
Consequently, with normalized Hilbert--Schmidt norm,
\[
 \left|\left\|\frac1{\sqrt K}\sum_{j=0}^{K-1}U_N^jR_NU_N^{-j}\right\|_{2,N}
                      -\sqrt{\Gamma_T(g)}\right|
 \leq\frac{\pi^3\sqrt K}{6N^2}M_3(g)M_3(\mathcal C_Tg).      \tag{27}
\]
This proves nonvanishing of the averaged commutator for each fixed nonzero
radius-eight symbol for all sufficiently large admissible N. It does not
assert exact equality between the commutator variance and the classical
variance at finite N.

Twelve exact Gaussian-integer coefficient checks compare (25) with a direct
modular Weyl-coefficient squared norm, including dimensions 47321 and 1607521.
No dense matrices of those sizes are constructed. A small-module negative
control, $K=3,N=7$, violates the non-aliasing condition and gives different
finite quantum and classical values; this mismatch is retained rather than
removing hypothesis (24).

# 7. Verification boundaries and relation to spectral universality

The exact verification has four distinct layers: independent integer orbit
construction, proof replay over complex variables with conjugation, symbolic
Hessian identities, and Gaussian-integer Fourier normalization checks. No
floating-point optimization is used in the promoted results. In particular,
36 arbitrary-phase instances are recomputed by a separate full oriented-orbit
Fourier convolution. They confirm the normalization in (6) but do not replace
the universal coefficient certificate.

The proof-search algorithm is intentionally incomplete. Its success at R=8
is not an induction theorem for all R. A larger even-only exploratory run was
interrupted and is not a result. The associated files are kept outside the
canonical evidence directory. No new Lean compilation was possible in the
available runtime. The auxiliary Wolfram service returned an endpoint error;
the successful symbolic check is the separately executed local SymPy check,
not an attributed Wolfram computation.

The motivating second-order residual mechanism has prior physics literature
[2]. A positive $\Gamma_A(g)$ gives a nonzero effective classical variance in
that mechanism. It does not prove the required quantum normal-form error,
Heisenberg-scale trace comparison, symmetry reduction, or random-matrix local
statistics. Moreover, arbitrary-phase symbols do not in general preserve the
odd parity sector used in earlier project spectral statements. Theorem 1
must not be inserted into an odd-sector theorem without checking its parity
hypotheses. The present analytic results concern the variance itself.

The arbitrary-radius finite mixed-sign problem was subsequently closed by
`extremal_resonance_nondegeneracy.md`; the radius-eight certificate here remains
a separate finite proof. `finite_orbit_resonance_rigidity.md` further covers
smooth symbols supported on finitely many signed Fourier orbits. Positivity
for every nonconstant real-analytic symbol with infinitely many such orbits
remains open. The separate BGS target is a positive local-statistics theorem
for fixed nonarithmetic chaotic dynamics; it is not solved by these results.

# Primary references

[1] G. Cohen and J.-P. Conze, *Central limit theorem for commutative semigroups
of toral endomorphisms*, arXiv:1304.4556, especially the orbit-sum spectral
density and degeneracy discussion. The primary HTML text was inspected.

[2] T. Prosen and M. Znidaric, *Quantum freeze of fidelity decay for chaotic
dynamics*, Physical Review Letters **94** (2005), 044101,
arXiv:quant-ph/0401142. Residual perturbations and second-order effects are
prior mechanisms. Only the primary abstract was retrieved anew in this pass.

Targeted searches did not establish whether the exact Hessian obstruction or
this particular finite-box certificate has appeared elsewhere. Failure to
find a matching paper is not a world-priority certificate.
