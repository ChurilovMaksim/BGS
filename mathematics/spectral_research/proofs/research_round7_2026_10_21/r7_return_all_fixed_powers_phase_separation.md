> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md`. Embedded SHA256: `46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527`.
> [Thematic guide](../../topics/dephasing.md).

# All fixed physical powers: global twist, nonseparated sheet phases, and the full alias sum

21 October 2026. This note concerns the **exact original** matrices
$U_N=e^{i\tau N A_N}M_N$, $\tau=10^{-80}$, along all odd dimensions.
It extends the finite-range physical-power theorem from round 6 to every
fixed positive power. No parameter of the original matrix is changed.

The new argument replaces the growing first-order comparison of individual
sheet actions by a geometric implication: if a pair of sheet actions were
separable in the two endpoints, an iterate of the classical map would
intertwine two nontrivial literal torus translations. A previously proved
discounted-coordinate argument excludes that possibility for every iterate;
its proof is repeated below. Positive Jacobians prevent caustics at every
intermediate stage. A sampled oscillatory-matrix lemma with all aliases
retained removes the small-gradient restriction from the fourth-moment step.

These results do not control trace times proportional to $N$ and do not
prove $H_{\rm diag}$.

## 1. Statement

Write
$$
 \mathsf S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
 \mathsf S^R=\begin{pmatrix}a_R&b_R\\c_R&a_R\end{pmatrix},
 \qquad \epsilon=14000\tau.
 \tag{1.1}
$$
Thus $a_R^2-b_Rc_R=1$, $a_R$ is odd, $b_R,c_R$ are even,
and $b_R>0$ for $R\ge1$.

**Theorem.** For every fixed positive integer $R$, there is a positive
real-analytic kernel $k_R$ on $(\mathbb R/\mathbb Z)^2$, independent
of $N$, such that
$$
 \left\||U_N^R|^{\circ2}
       -\left[N^{-1}k_R(x/N,y/N)\right]_{x,y=0}^{N-1}\right\|_{\rm op}
 \longrightarrow0
 \tag{1.2}
$$
along all odd $N$. Its two marginals are one, and
$$
 (1+\epsilon)^{-R}\le k_R(q,s)\le(1-\epsilon)^{-R}.
 \tag{1.3}
$$
In particular,
$$
 \limsup_{\substack{N\to\infty\\N\ {\rm odd}}}
 \bigl\||U_N^R|^{\circ2}-J_N\bigr\|_{\rm op}
 \le(1-\epsilon)^{-R}-1.
 \tag{1.4}
$$
For all sufficiently large odd $N$, depending on the fixed $R$,
$$
 \max_{x,y}|U_N^R(x,y)|
 \le\frac{C_R}{\sqrt N},\qquad
 C_R=2\sqrt{b_R}(1-\epsilon)^{-R/2}.
 \tag{1.5}
$$
Neither (1.2) nor its error term is asserted uniformly for $R$ growing
with $N$. The bound (1.4) is useful when $R\epsilon$ is small;
(1.2), (1.3), and (1.5) hold for every fixed $R$, including larger ones.

An immediate actual-family consequence, proved in Section 9, is that for
the diagonal-pair first returns at the original phase vector,
$$
 \frac1N\sum_{r>L}\|F_r(U_N)\|_{\rm HS}^2\longrightarrow1
 \quad\text{for every fixed }L\ge1.
 \tag{1.6}
$$
This extends the former physical conclusion through 49 to every fixed
cutoff, without an auxiliary phase average.

## 2. Exact symbol and the physical classical convention

Use ordinary Weyl operators
$$
 (W_N(k,l)\psi)(x)
   =e^{2\pi ikx/N+\pi ikl/N}\psi(x+l),\qquad
 Q_N(H)=\sum_{k,l}\widehat H(k,l)W_N(k,l).
$$
For odd $N$, the modular half in the question gives exactly
$T_N(l,k)=(-1)^{kl}W_N(k,l)$. Consequently $A_N=Q_N(a)$, where
$$
 a(q,p)=\cos(14\pi q)+\frac{r(q)}{10}
       +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}
       +\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0).
 \tag{2.1}
$$
It has Fourier support $|k|+|l|\le9$, $|l|\le1$, and
$\sum|\widehat a(k,l)|<2$. The last bound follows, for example,
by expanding the cosine part with total coefficient norm $11/10$,
bounding $r\sin(2\pi q)/100$ by $4/100$, and the final term by
$4/100$. Two coefficients used later are exactly
$$
 \widehat a(1,0)=\frac1{20}-\frac{i}{200},\qquad
 \widehat a(0,1)=\frac{e^{-i\alpha_0}}{200}.
 \tag{2.2}
$$

Let $\Phi_u$ be the flow of
$$
 X=\frac1{2\pi}(a_p,-a_q),\qquad
 \Psi=\mathsf S\circ\Phi_\tau.
 \tag{2.3}
$$
The physical map of the kernel, in the convention with outgoing momentum
equal to the derivative of its phase in the outgoing coordinate, is
$$
 F=\Psi^{-1}=\Phi_{-\tau}\circ\mathsf S^{-1}.
 \tag{2.4}
$$
The sign follows directly from the quadratic kernel: if
$\Theta(q,s)=-(3q^2-2qs+3s^2)/8$, then outgoing momentum is
$\Theta_q$ and incoming momentum is $-\Theta_s$, which gives
the linear map $\mathsf S^{-1}$.

The support and coefficient bound imply, in either the Euclidean operator
norm or the maximum row-sum norm where appropriate,
$$
 \|X\|_\infty\le20,\qquad \|DX\|_\infty\le2000.
 \tag{2.5}
$$
Indeed a vector Fourier coefficient of $X$ has size at most
$(|k|+|l|)|\widehat a(k,l)|$; one derivative adds at most
$2\pi(|k|+|l|)$. Thus the derivative bound is less than
$2\pi\cdot81\cdot2<2000$. The same bounds hold after reversing
momentum and the sign of the vector field.

All these flows are globally defined and real analytic. Existence for
real times follows from the bounded periodic vector field. For analytic
dependence, complex Picard iteration applies on sufficiently small tubes
for short time intervals. A finite composition of such intervals covers
each fixed finite time; compactness of the real torus gives a positive
local complex tube after shrinking. No tube width uniform in $R$ will
be needed.

## 3. Every intermediate sheet is a global graph

Set $C(q,p)=(q,-p)$. In the coordinate $(q,r)=C(q,p)$, define
$$
 \kappa_u=C\Phi_{-u}C,\qquad F_+=CFC=\kappa_\tau\mathsf S.
 \tag{3.1}
$$
The derivative of $\kappa_u$ obeys, for $0\le u\le\tau$,
$$
 \|D\kappa_u-I\|_{\infty\to\infty}
 \le e^{2000u}-1\le4000\tau.
 \tag{3.2}
$$
Since the smallest entry of $\mathsf S$ is two and
$\|\mathsf S\|_{\infty\to\infty}=7$, it follows entrywise that
$$
 (1-\epsilon)\mathsf S
 \le D\kappa_u\,\mathsf S
 \le(1+\epsilon)\mathsf S,
 \qquad\epsilon=14000\tau<1/2.
 \tag{3.3}
$$
Every entry in the middle matrix is positive. Products preserve these
entrywise inequalities, so
$$
 (1-\epsilon)^R\mathsf S^R
 \le D(F_+^R)
 \le(1+\epsilon)^R\mathsf S^R.
 \tag{3.4}
$$
In particular the derivative of the final position with respect to the
initial $r$ is strictly positive, uniformly on the real torus.

One must also check the intermediate stages in the exact quantum
factorization; positivity only at the endpoint would not suffice. Exact
ordinary Weyl covariance gives
$$
 M_N^jQ_N(a)M_N^{-j}=Q_N(H_j),\quad H_j=a\circ\mathsf S^j,
$$
and therefore
$$
 U_N^R=e^{i\tau NQ_N(H_0)}\cdots
       e^{i\tau NQ_N(H_{R-1})}M_N^R.
 \tag{3.5}
$$
For the covariance, the finite shift and multiplication generators give
$M_NT_N(l,k)M_N^*=T_N(3l+4k,2l+3k)$. The parity identity
$(3l+4k)(2l+3k)-lk\in2\mathbb Z$ removes the ordinary-half sign.
Iteration proves the stated exact identity.

The classical flow in the $j$-th exponential is
$\mathsf S^{-j}\Phi_{-u}\mathsf S^j$, because the Hamiltonian is
$H_j/(2\pi)$ with the negative Hamiltonian-vector-field sign.
The stages in (3.5) act from right to left. After $k$ complete stages,
the positive-coordinate map is exactly
$$
 \mathsf S^{R-k}F_+^k,\qquad0\le k\le R.
 \tag{3.6}
$$
At time $u$ in the next stage it is
$$
 \mathsf S^{R-k-1}\kappa_u\mathsf S F_+^k.
 \tag{3.7}
$$
Equations (3.3) and (3.4) show that the derivative in (3.7) is bounded
entrywise between $(1-\epsilon)^{k+1}\mathsf S^R$ and
$(1+\epsilon)^{k+1}\mathsf S^R$. This proves positivity throughout
every stage, without any $\tau\lambda^{2R}$ smallness assumption.

Put $a=a_R,b=b_R,c=c_R$. Every map in (3.6) or (3.7) is a lift with
deck transformation $\mathsf S^R$. If its first component is
$Q(s,r)$, then
$$
 Q(s,r+1)=Q(s,r)+b,
\quad
 (1-\epsilon)^R b\le\partial_rQ(s,r)\le(1+\epsilon)^R b.
 \tag{3.8}
$$
For every fixed $s$, the map $r\mapsto Q(s,r)$ is therefore a
strictly increasing bijection of $\mathbb R$ onto $\mathbb R$.
Its inverse is real analytic by the implicit function theorem. The
positive lower bound and compactness in the endpoint deck lattice give
uniform local analytic neighborhoods for each fixed $R$.

## 4. Exact initial sheets, actions, and their amplitudes

The finite Gaussian matrix power has the exact image representation
$$
 M_N^R(x,y)=\frac{\eta_{R,N}}{\sqrt{bN}}
 \sum_{m=0}^{b-1}
 \exp\left[-\frac{2\pi i}{2bN}
 \{ax^2-2x(y+mN)+a(y+mN)^2\}\right],
 \quad|\eta_{R,N}|=1.
 \tag{4.1}
$$
A direct finite-dimensional proof, including non-coprime $N,b$, is
given in Appendix A. The initial real phases are
$$
 \Theta_m(q,s)=-\frac{aq^2-2q(s+m)+a(s+m)^2}{2b}.
 \tag{4.2}
$$
Fix $s+m$ as the input position. The initial output coordinate $u$
corresponds in the positive coordinates to input momentum
$r_{\rm in}=(u-a(s+m))/b$. By (3.8), the derivative of the evolving
output position with respect to $u$ is bounded between
$(1-\epsilon)^R$ and $(1+\epsilon)^R$. It is always positive.

The action along these characteristics, starting at $\Theta_m$, gives
globally defined real-analytic phases $\Phi_m(q,s)$ at the end of
all stages. At the $j$-th stage they solve
$$
 \partial_u\Phi=H_j(q,\Phi_q)/(2\pi).
 \tag{4.3}
$$
The amplitude starts at one and is
$$
 B_m(q,s)=(\partial_uQ)^{-1/2}>0.
$$
Here $u$ in $\partial_uQ$ denotes the initial output-coordinate
parameter, not stage time. Equivalently, if $Q_R(s,r)$ is the first
component of $F_+^R$, then
$$
 B_m(q,s)^2=
 \frac{b}{\partial_r Q_R(s+m,r_{\rm in}(q,s+m))}.
 \tag{4.4}
$$
The variational formulas for the action are
$\Phi_q=p_{\rm out}$ and $\Phi_s=-p_{\rm in}$. They follow by
differentiating the characteristic action
$\Theta+\int(p\,\dot q+H_j/(2\pi))\,du$, with the endpoint held
fixed; the Hamilton equations cancel the interior variation. The transport
equation for $B$ is also verified directly in Appendix B.

The bounds in Section 3 prove
$$
 (1+\epsilon)^{-R}\le B_m(q,s)^2\le(1-\epsilon)^{-R}
 \tag{4.5}
$$
at the final time and corresponding bounds at every earlier stage.
Every fixed derivative of every phase and amplitude is bounded on the
compact endpoint region and its finitely many sheet translates. These
bounds may depend on $R$; finiteness, rather than a uniform estimate,
is what is required below.

Write $S_m=\Phi_m-\Theta_m$. The exact initial identities
$$
\begin{aligned}
 \Theta_{m+b}(q,s)&=\Theta_m(q,s)+q-a(s+m)-ab/2,\\
 \Theta_m(q+1,s)&=\Theta_{m-a}(q,s)-c(s+m)+ac/2,\\
 \Theta_m(q,s+1)&=\Theta_{m+1}(q,s)
\end{aligned}
 \tag{4.6}
$$
persist for $\Phi$, because every Hamiltonian is periodic and its
characteristic solution is unique. The amplitude obeys the same identities
without additive terms. Also the literal equality of the initial data
with $s$ replaced by $s+m$ gives
$$
 S_m(q,s)=S_0(q,s+m).
 \tag{4.7}
$$
Thus $S=S_0$ is periodic under $(1,a)$ and $(0,b)$, and hence
also under $(b,0)$ and $(a,1)$. To check the last lattice generator,
$(a,1)=a(1,a)-c(0,b)$, since $a^2-bc=1$.

Two additional estimates follow without a growing-frequency Taylor
comparison. Since $\|H_j\|_\infty<2$, integrating (4.3) at fixed
endpoints over the $R$ stages gives
$$
 \|S_m\|_\infty\le R\tau/\pi.
 \tag{4.8}
$$
Also $\Phi_s=r_{\rm in}$ in the positive coordinates, so differentiating
the inverse twist relation gives $\Phi_{qs}=B_m^2/b$. Therefore
$$
 S_{m,qs}=\frac{B_m^2-1}{b},\qquad
 \|S_{m,qs}\|_\infty
 \le\frac{(1-\epsilon)^{-R}-1}{b}.
 \tag{4.9}
$$
These are upper bounds for individual corrections. They do not replace
a quantitative lower bound for the mixed derivative of a sheet difference.

## 5. The iterated map has no nontrivial translation intertwiner

This section repeats the discounted-coordinate proof from
`research_round2_2026_10_20/arithmetic_iterated_sector_covariance.md`,
Sections 3–6. Its hypotheses are precisely the corrected symbol (2.1),
not a different uncorrected classical symbol.

Let
$$
 \lambda=3+2\sqrt2>5,\qquad
 \ell=(1,\sqrt2)/\sqrt3,\qquad
 \delta=\Phi_\tau-I.
$$
Then $\ell\mathsf S=\lambda\ell$, $\|\ell\|_2=1$. For the lift
$\Psi(x)=\mathsf Sx+\mathsf S\delta(x)$, define the periodic scalar
function
$$
 v_R(x)=\lambda^{-R}\ell\Psi^R(x)-\ell x
       =\sum_{j=0}^{R-1}\lambda^{-j}\ell\delta(\Psi^j x).
 \tag{5.1}
$$
The equality follows by telescoping. Set
$$
 w_R(x)=\tau\sum_{j=0}^{R-1}\lambda^{-j}\ell X(\mathsf S^j x).
$$
Bounds (2.5) give
$\|\delta\|_\infty\le20\tau$ and
$\|\delta-\tau X\|_\infty\le20000\tau^2$.
The similarity $\operatorname{diag}(\sqrt2,1)^{-1}\mathsf S
\operatorname{diag}(\sqrt2,1)$ is symmetric, so
$\|\mathsf S^j\|_2\le\sqrt2\lambda^j$. The lifted recursion then
gives
$$
 \|\Psi^j-\mathsf S^j\|_\infty\le50\tau\lambda^j,
\quad
 \|X\circ\Psi^j-X\circ\mathsf S^j\|_\infty
 \le\min(10^5\tau\lambda^j,40).
$$
It follows, uniformly over all integers $R\ge1$, that
$$
 \|v_R-w_R\|_\infty
 \le\sum_{j\ge0}\left[20000\tau^2\lambda^{-j}
       +\min(10^5\tau^2,40\tau\lambda^{-j})\right]
 <3\cdot10^7\tau^2.
 \tag{5.2}
$$
For the numerical constant, split at $j=200$. Since
$5^{200}>10^{80}=\tau^{-1}$, $\lambda^{-200}<\tau$, and
$(1-\lambda^{-1})^{-1}<5/4$, the sum is at most
$(20000\cdot5/4+200\cdot10^5+40\cdot5/4)\tau^2
=20025050\tau^2$.

For $j\ge1$, the two labels $\mathsf S^{-Tj}e_1$ and
$\mathsf S^{-Tj}e_2$ have second coordinate of absolute value at
least three. This follows immediately from the positive recurrence for
$a_j,b_j,c_j$: the labels are $(a_j,-b_j)$ and $(-c_j,a_j)$.
They lie outside the original strip $|l|\le1$. Thus only $j=0$
contributes to the two Fourier coefficients of $w_R$ at $e_1,e_2$.
Using (2.2),
$$
 |\ell\widehat X(e_1)|^2=101/60000,\qquad
 |\ell\widehat X(e_2)|^2=1/120000.
$$
Both magnitudes exceed $1/400$. Equations (5.2) and the exact
$\tau=10^{-80}$ imply
$$
 |\widehat v_R(e_i)|\ge\tau/800>0,
 \qquad i=1,2,\quad R\ge1.
 \tag{5.3}
$$

Suppose $\Psi^R t_h\Psi^{-R}=t_k$ on the torus. For lifts this gives
$\Psi^R(x+h)=\Psi^R(x)+k+n$, with a constant integer vector $n$.
Iterating this translation $L$ times, dividing by $L$, and using
the bounded periodic remainder in the lift of $\Psi^R$, shows
$k+n=\mathsf S^Rh$. Hence $v_R(x+h)=v_R(x)$. By (5.3), its two
Fourier coefficients force $e^{2\pi i h_1}=e^{2\pi i h_2}=1$.
Thus $h=k=0$ on the torus. This includes irrational translations.
Reversing the relation proves the same statement for negative iterates.
In particular,
$$
 F^R t_hF^{-R}=t_k\quad\Longrightarrow\quad h=k=0
 \qquad(R\ne0).
 \tag{5.4}
$$

## 6. Separation of every pair of nonlinear sheet actions

Fix distinct labels $m,n\pmod b$. Suppose, to obtain a contradiction,
that $\partial_q\partial_s(\Phi_m-\Phi_n)$ vanishes identically.
The difference of the initial phases (4.2) is separable, so the same is
true of $S_m-S_n$. By (4.7), after a translation in $s$, this says
$$
 S(q,s+d)-S(q,s)=u(q)+v(s),\qquad 0<d<b,
 \tag{6.1}
$$
for some smooth functions $u,v$. The representation follows by
integrating the vanishing mixed derivative on $\mathbb R^2$.

Let $L=b/\gcd(b,d)$. Sum (6.1) at $s,s+d,\ldots,s+(L-1)d$.
The left side telescopes to zero, since $S$ is $b$-periodic in
$s$. Hence $Lu(q)+\sum_{j=0}^{L-1}v(s+jd)=0$, forcing $u$
to be constant. The difference in (6.1) is therefore independent of
$q$.

There is a second integration constant to remove. Define
$\overline S(s)=b^{-1}\int_0^bS(q,s)\,dq$. The period lattice
$(b,0),(a,1)$ makes $\overline S$ one-periodic in $s$.
Averaging (6.1) in $q$, and using the integer $d$, therefore gives
$$
 S(q,s+d)-S(q,s)=\overline S(s+d)-\overline S(s)=0.
 \tag{6.2}
$$
This exact equality, not just separability, is essential.

It follows from (4.2) that
$$
 \Phi_0(q,s+d)-\Phi_0(q,s)
 =\frac{dq-ad s-ad^2/2}{b}.
 \tag{6.3}
$$
The phase generates the physical map $F^R$, with input momentum
$-\Phi_s$ and output momentum $\Phi_q$. Differentiating (6.3)
and observing that $s+d=s$ on the torus yields
$$
 F^R t_{(0,ad/b)}=t_{(0,d/b)}F^R.
 \tag{6.4}
$$
Both translations are nontrivial because $0<d<b$ and
$\gcd(a,b)=1$. This contradicts (5.4). Therefore, for every fixed
$R$ and every distinct pair of its sheets,
$$
 \boxed{\quad
 \partial_q\partial_s(\Phi_m-\Phi_n)\not\equiv0.
 \quad}
 \tag{6.5}
$$
There is no first-order expansion of the individual sheet action in this
argument, and no $R$-dependent smallness condition on $\tau$.

## 7. A sampled oscillatory-matrix lemma with unrestricted aliases

**Lemma.** Let $a$ be smooth and $\phi$ real analytic on a connected
open neighborhood of $[0,1]^2$. Suppose
$\partial_x\partial_y\phi\not\equiv0$. Define
$$
 A_N(x,y)=N^{-1}a(x/N,y/N)e^{2\pi iN\phi(x/N,y/N)},
 \quad0\le x,y<N.
$$
Then $\|A_N\|_{\rm op}\to0$. There is no restriction on the size
of the derivatives of $\phi$.

**Proof.** The fourth Schatten power is
$$
 \operatorname{Tr}[(A_NA_N^*)^2]
 =N^{-4}\sum_{x,x',y,y'}\mathcal A(x/N,x'/N,y/N,y'/N)
 e^{2\pi iN\mathcal P(x/N,x'/N,y/N,y'/N)},
 \tag{7.1}
$$
where $\mathcal A$ is the corresponding product of four amplitudes and
$$
 \mathcal P(x,x',y,y')
 =\phi(x,y)-\phi(x',y)+\phi(x',y')-\phi(x,y').
$$
For any fixed real vector $\xi\in\mathbb R^4$, the analytic function
$\mathcal P(z)-\xi\cdot z$ is nonconstant. Otherwise $\mathcal P$
would be affine. Its vanishing when $x=x'$ and when $y=y'$ would
force that affine function to be zero; differentiation would then give
$\phi_{xy}\equiv0$, a contradiction.

Insert a smooth cutoff equal to one away from a boundary strip of width
$\delta$ in $[0,1]^4$, and supported in its interior. The normalized
sum changes by at most $C(\delta+N^{-1})$, by counting grid points in
that strip. For the cut-off smooth compactly supported amplitude
$\mathcal A_\delta$, Poisson summation gives exactly
$$
 \sum_{k\in\mathbb Z^4}
 \int\mathcal A_\delta(z)
 e^{2\pi iN(\mathcal P(z)-k\cdot z)}\,dz.
 \tag{7.2}
$$
Every fixed alias tends to zero. Indeed a nonconstant real-analytic phase
has a critical set of measure zero: some first derivative is not
identically zero, and the zero set of a nonzero real-analytic function
has measure zero. The latter fact follows by induction on dimension,
expanding in one coordinate, discarding the zero set of a nonzero analytic
coefficient in the other coordinates, and using isolated zeros on the
remaining one-dimensional fibers. On the complement of a small
neighborhood of the critical set, integration by parts using
$\nabla f/|\nabla f|^2$ makes the integral tend to zero; the neighborhood
has arbitrarily small volume and bounded amplitude.

The infinitely many distant aliases are uniform. For
$|k|>2\sup|\nabla\mathcal P|+2$, the phase gradient has size at least
$|k|/2$. Repeated integration by parts, with the compact cutoff, gives
for any fixed $M$
$$
 \left|\int\mathcal A_\delta(z)
 e^{2\pi iN(\mathcal P(z)-k\cdot z)}\,dz\right|
 \le C_{M,\delta}N^{-M}(1+|k|)^{-M}.
$$
All derivatives of $\mathcal P$ are fixed and bounded on the support.
Choose $M>4$; the distant-alias sum tends to zero. The remaining aliases
are finite in number and were already treated. Sending $N\to\infty$
and then $\delta\to0$ makes (7.1) tend to zero. Since
$\|A_N\|_{\rm op}^4\le\operatorname{Tr}[(A_NA_N^*)^2]$, the lemma
follows. The same argument accommodates any fixed row and column residue
classes, whose aliases are rescaled by fixed rational factors. $\square$

## 8. The actual quantum kernel and the positive limiting kernel

Let $h=(2\pi N)^{-1}$ and define
$$
 V_{R,N}(x,y)=\frac{\eta_{R,N}}{\sqrt{bN}}
 \sum_{m=0}^{b-1}B_m(x/N,y/N)e^{i\Phi_m(x/N,y/N)/h}.
 \tag{8.1}
$$
Appendix B gives the finite-shift calculation of its residual under each
exact exponential in (3.5). The bounds proved above are sufficient for
that calculation for every fixed $R$, and (4.6) gives the exact
periodicity needed at wrapped grid shifts. The resulting comparison is
$$
 \|(U_N^R-V_{R,N})e_y\|_2=O_R(N^{-1}),\qquad
 \|U_N^R-V_{R,N}\|_{\rm HS}=O_R(N^{-1/2}).
 \tag{8.2}
$$
By (4.5),
$\max|V_{R,N}|\le\sqrt b(1-\epsilon)^{-R/2}/\sqrt N$.
The column bound in (8.2) proves (1.5) after increasing the fixed-
$R$ threshold for $N$. It also gives
$$
 \bigl\||U_N^R|^{\circ2}-|V_{R,N}|^{\circ2}\bigr\|_{\rm HS}
 =O_R(N^{-1}).
 \tag{8.3}
$$

Define
$$
 k_R(q,s)=\frac1b\sum_{m=0}^{b-1}B_m(q,s)^2.
 \tag{8.4}
$$
The deck identities permute the summands under unit changes in either
endpoint, so this is a real-analytic kernel on the ordinary endpoint
torus. Bounds (1.3) follow from (4.5).

The equal-sheet part of $|V_{R,N}|^{\circ2}$ is exactly
$N^{-1}k_R(x/N,y/N)$. Each unequal-sheet term has the form in Section 7,
with smooth amplitude $B_mB_n/b$ and analytic phase $\Phi_m-\Phi_n$.
Its mixed derivative is not identically zero by (6.5). Every such term
therefore tends to zero in operator norm. For each fixed $R$, there
are only $b(b-1)$ terms, so their sum also tends to zero. Combining with
(8.3) proves (1.2).

For the marginals, let $r(q,s)$ be the inverse of $Q_R(s,r)$, and put
$K(q,s)=\partial_qr(q,s)>0$. Equation (4.4) says that the summands in
(8.4) are $K(q,s+m)$. The deck law implies
$K(q,s+m)=K(q-am,s)$, and $K$ is $b$-periodic in $q$.
Since multiplication by $a$ permutes the residues modulo $b$,
$$
 k_R(q,s)=\sum_{j=0}^{b-1}K(q+j,s).
$$
Integrating in $q$ over $[0,1]$ gives
$r(b,s)-r(0,s)=1$. This proves the column marginal. Equivalently this
is the position density of the image under $F_+^R$ of uniform initial
momentum at fixed initial position. Integrating also over uniform initial
position and using preservation of area on the torus proves the other
marginal. Positivity and analyticity make these pointwise marginal
identities.

Finally, the maximum absolute entry of
$[N^{-1}k_R(x/N,y/N)]-J_N$ is at most
$N^{-1}[(1-\epsilon)^{-R}-1]$. To see that this also dominates the
lower deviation, use convexity to obtain
$(1-\epsilon)^{-R}+(1+\epsilon)^{-R}\ge2$.
The elementary row-column norm bound now proves (1.4).

## 9. Physical first-return mass after every fixed cutoff

For completeness, the normalization used here does not require absence
of dark states for the original family. For $W=U\otimes\overline U$,
decompose along the diagonal-pair projection as
$W=\left(\begin{smallmatrix}P&B\\C&S\end{smallmatrix}\right)$, and let
$F_1=P$, $F_r=BS^{r-2}C$ for $r\ge2$.
Unitarity gives
$$
 \sum_{r=1}^{m+1}F_r^*F_r=I-C^*S^{*m}S^mC.
$$
Put $a_m=\|S^m\|_{\rm HS}^2$. Since $S$ is a contraction,
$a_m$ is nonincreasing and convergent, and
$\|S^mC\|_{\rm HS}^2=a_m-a_{m+1}\to0$, using
$CC^*=I-SS^*$. Thus
$$
 \sum_{r\ge1}\|F_r(U)\|_{\rm HS}^2=N
 \tag{9.1}
$$
for every finite unitary.

The unrestricted returns are $R_j=|U^j|^{\circ2}$; splitting at the
first return gives $R_n=\sum_{r=1}^nF_rR_{n-r}$. Bistochasticity shows
that $F_r$ annihilates the constant vector on both sides for $r\ge2$.
Writing $E_j=R_j-J_N$ and using that every $F_r$ is a contraction
gives
$$
 \|F_r\|_{\rm HS}\le\sum_{j=1}^r\|E_j\|_{\rm HS}\quad(r\ge2).
$$
By (1.5), for each fixed $j$ and all sufficiently large odd $N$,
$$
 \|E_j\|_{\rm HS}^2
 =\sum_{x,y}|U_N^j(x,y)|^4-1\le C_j^2-1.
$$
Thus for every fixed $L$,
$$
 \sum_{r=1}^L\|F_r(U_N)\|_{\rm HS}^2
 \le K_L:=C_1^2+\sum_{r=2}^Lr\sum_{j=1}^r(C_j^2-1)<\infty
$$
eventually along all odd $N$. Equation (9.1) now gives
$N-K_L\le\sum_{r>L}\|F_r(U_N)\|_{\rm HS}^2\le N$, proving (1.6).
No auxiliary phase average occurs in this argument.

## 10. What the theorem still does not provide

The new separation statement is exact for every iterate, and the quantum
consequence is proved for every fixed iterate. This removes the earlier
artificial cutoff at 49 in this particular physical-power construction.
It supplies more phase information than a bound on $|U_N^R|^{\circ2}$
alone: every unequal-sheet rectangular-cycle phase is nonaffine, so every
fixed Poisson alias has a nonconstant phase.

The proof does not quantify how the oscillatory constants deteriorate
with $R$. For $R=R(N)$, one would need bounds on the analytic sheet
derivatives, the sizes of sublevel sets for all relevant aliased cycle
gradients, and the sum over the growing number $b_R(b_R-1)$ of sheet
pairs, together with a uniform kernel residual. None is established here
at logarithmic times, much less at the times proportional to $N$
required by $H_{\rm diag}$.

Even a logarithmic-time extension of (1.2) would not itself evaluate the
full signed long-time trace functional. The first unresolved pair estimate
for the original family remains
$$
 N^{-2}\sum_{n\ge1}|\widehat b(n/N)|^2
 \bigl(|\operatorname{Tr}U_N^n|^2-\min(n,N)\bigr)\longrightarrow0
$$
for every fixed admissible $b$; all higher orders are also still required.

## Appendix A. Direct proof of the image formula

Let $L_N(x,y)$ be the right side of (4.1) with $\eta_{R,N}=1$, and
let $Q(x,Y)=ax^2-2xY+aY^2$. The phase is periodic under $m\mapsto m+b$
when $x,y$ are integers, because $ab$ is even. It is periodic in
$y\pmod N$ by reindexing $m$. The identity
$$
 Q(x+N,Y+aN)-Q(x,Y)=bc(2YN+aN^2)
$$
and evenness of $ac$ also give periodicity in $x\pmod N$.

The two polynomial identities
$$
\begin{aligned}
 Q(x+a,Y)-Q(x,Y-1)&=bc(2x+a),\\
 Q(x+b,Y)-Q(x,Y)&=2b(ax+ab/2-Y)
\end{aligned}
$$
give exactly
$L_NT_N(1,0)=T_N(a,c)L_N$ and
$L_NT_N(0,1)=T_N(b,a)L_N$. Ordinary half factors agree with modular
ones because $ac,ab$ are even. The same identities hold for $M_N^R$
by exact Weyl covariance. Therefore $M_N^{-R}L_N$ commutes with the
shift and multiplication generators. Commuting with the multiplication
generator makes a matrix diagonal; commuting with the shift makes all
its diagonal entries equal. Thus $L_N$ is a scalar multiple of $M_N^R$.

To determine the scalar modulus without assuming $\gcd(N,b)=1$, put
$g=\gcd(N,b)$. The image sum, apart from its unit-modulus factor, is
$$
 \sum_{m=0}^{b-1}
 \exp\left[\frac{2\pi i}{b}
       \left(m(x-ay)-\frac{aN m^2}{2}\right)\right].
$$
In its squared modulus the inner sum over $m$, after differencing by
$h$, vanishes unless $b\mid Nh$. Since $\gcd(a,b)=1$, the surviving
differences are $h=(b/g)j$, $0\le j<g$. Here $g$ is odd and
$b/g$ is even. The remaining quadratic phase is
$\exp[-\pi i a(N/g)(b/g)j^2]=1$, so the squared modulus is
$bg\mathbf1_{\{g\mid x-ay\}}$. Consequently
$$
 |L_N(x,y)|^2=\frac gN\mathbf1_{\{g\mid x-ay\}}.
$$
For each row there are exactly $N/g$ allowed columns, so every row
norm is one. The scalar multiple therefore has modulus one. Absorbing
its inverse into $\eta_{R,N}$ proves (4.1) for every odd $N$.

## Appendix B. The finite-shift parametrix error

For a fixed finite Fourier symbol $H$, apply its exact ordinary Weyl
formula to $B(q)e^{i\Phi(q)/h}$. Each shift is $l/N=2\pi lh$.
Taylor expansion through first order after factoring out the oscillatory
phase gives
$$
 Q_N(H)(Be^{i\Phi/h})=e^{i\Phi/h}
 \left[H(q,\Phi_q)B-ih\left(H_pB_q
       +\tfrac12(H_{qp}+H_{pp}\Phi_{qq})B\right)+O(h^2)\right].
 \tag{B.1}
$$
For example the three first-order Fourier factors are
$2\pi lB_q$, $2\pi^2iklB$, and
$2\pi^2il^2\Phi_{qq}B$, which are exactly the derivatives displayed
in (B.1). There are finitely many Fourier labels, and phase and amplitude
derivatives are bounded on fixed compact neighborhoods, so the remainder
is uniform on the required endpoint region.

The exact evolution for stage time $u$ is
$\partial_u\psi=iQ_N(H)\psi/(2\pi h)$. The leading and next terms
in (B.1) cancel if
$$
 \Phi_u=H(q,\Phi_q)/(2\pi),\quad
 B_u=\frac1{2\pi}\left(H_pB_q
       +\tfrac12(H_{qp}+H_{pp}\Phi_{qq})B\right).
$$
Along $\dot q=-H_p/(2\pi)$, the Jacobian $Q_u$ of the graph
coordinate obeys the opposite logarithmic derivative, proving precisely
$B=(Q_u)^{-1/2}$. The uncancelled residual in the evolution equation
is $O(h)$ times the initial amplitude normalization.

For the sum (8.1), that normalization is $1/\sqrt{bN}$, there are
$b$ fixed branches and $R$ fixed stages, and thus each residual
entry is $O_R(h/\sqrt N)$. At a grid wrap the phase changes in (4.6),
after multiplication by $N$, are integers: the relevant expressions are
$-cy-cNm+acN/2$ and $x-ay-aNm-abN/2$. The parity already checked
ensures this. Therefore the global branch extensions give exactly the
same values as wrapped finite shifts, and (B.1) is legitimate for the
finite matrix at every grid point.

Each residual column has Euclidean norm $O_R(h)$. The initial kernel is
exactly (4.1); at stage boundaries the constructed phases and amplitudes
match. Duhamel's formula and unitarity of every exact stage therefore give
column error $O_R(h)$. Summing its squared norm over the $N$ columns
gives Hilbert--Schmidt error $O_R(h\sqrt N)$, which is (8.2). No
long-time Egorov theorem is used in this comparison.
