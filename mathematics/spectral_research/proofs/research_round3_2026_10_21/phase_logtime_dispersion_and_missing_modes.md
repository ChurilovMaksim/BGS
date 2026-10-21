> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/phase_logtime_dispersion_and_missing_modes.md`. Embedded SHA256: `40dd41555520f712b99f7467ed14fd41ff0369db4b44a9b78f21c7f5a8314b4b`.
> [Thematic guide](../../topics/dephasing.md).

# Logarithmic-time dispersion and the quantum modes lost by position-diagonal transfer

Research continuation, 21 October 2026.

**Status.** The propositions below concern the exact family
$U_N=e^{i\tau N A_N}M_N$, with $\tau=10^{-80}$, over all sufficiently large odd $N$. They prove logarithmic-time dispersion, uniform coordinate delocalization of every eigenvector, and a quantitative obstruction to replacing the full doubled quantum resolvent by an operator with position-diagonal range. They do **not** prove $H_{\rm diag}$, its negation, a Heisenberg-time form factor, or cancellation between different interior words.

The proof is independent of the all-time scalar orbit formula in the earlier report. In particular, it does not infer a long-time estimate from an unquantified fixed-time WKB remainder.

## 1. Statements

Write $h=N^{-1}$. There are finite constants $C>0$, $A\ge2$, and $N_0$, depending only on the given finite Fourier polynomial and the fixed number $\tau$, such that

$$
\boxed{\displaystyle
\max_{x,y\in\mathbb Z/N\mathbb Z}|(U_N^m)_{xy}|
 \le \frac{C A^m}{\sqrt N}
\qquad(m\ge1,\ N\ge N_0\text{ odd}).}
\tag{1}
$$

The estimate becomes trivial for sufficiently large $m$. Its content is the single exponential budget, with no $m$-dependence in $A$. Consequently

$$
\boxed{\displaystyle
\mu_N:=
\sup_{\substack{U_N\psi=\lambda\psi\\\|\psi\|_2=1}}
 \max_x|\psi(x)|^2
=O((\log N)^{-1}).}
\tag{2}
$$

The supremum includes every unit vector in each eigenspace, whether or not the spectrum is simple. No restriction $7\nmid N$ is imposed.

For the final assertion let
$\mathcal V_N=M_N(\mathbb C)$, with its Hilbert--Schmidt inner product. Let
$\mathcal C_N:X\mapsto U_N XU_N^*$;
let $\mathcal P_N$ be the orthogonal projection onto its fixed space, the full commutant of $U_N$; and let $\mathcal D_N$ be the orthogonal projection onto matrices diagonal in the coordinate basis. If $\Pi_\lambda$ are the spectral projections of $U_N$, put

$$
d_N=\operatorname{rank}\mathcal P_N
=\sum_\lambda(\operatorname{rank}\Pi_\lambda)^2\ge N.
$$

Then

$$
\operatorname{Tr}_{\mathcal V_N}(\mathcal P_N\mathcal D_N)
=\sum_{\lambda,x}(\Pi_{\lambda,xx})^2
\le N\mu_N=O(N/\log N),
\tag{3}
$$

and therefore

$$
\boxed{\displaystyle
\operatorname{Tr}_{\mathcal V_N}
  \big(\mathcal P_N(I-\mathcal D_N)\big)
=d_N-O(N/\log N)\ge N-O(N/\log N).}
\tag{4}
$$

For fixed $s>0$, set $r_N=e^{-2s/N}$ and
$\mathcal R_N=(I-r_N\mathcal C_N)^{-1}$.
Every linear map $\mathcal T_N:\mathcal V_N\to\mathcal V_N$ whose range consists of position-diagonal matrices satisfies

$$
\boxed{\displaystyle
\|\mathcal R_N-\mathcal T_N\|_{\mathrm{HS}(\mathcal V_N)}^2
\ge\frac{d_N-N\mu_N}{(1-r_N)^2},\qquad
\liminf_{\substack{N\to\infty\\N\ {\rm odd}}}
 N^{-3}\|\mathcal R_N-\mathcal T_N\|_{\mathrm{HS}(\mathcal V_N)}^2
\ge \frac1{4s^2}.}
\tag{5}
$$

Here $\mathrm{HS}(\mathcal V_N)$ is the Hilbert--Schmidt norm of a superoperator on the $N^2$-dimensional Hilbert space $\mathcal V_N$. The result concerns approximation error in that norm. It does not assert the same lower bound for the difference of the two squared norms.

## 2. The ordinary finite-shift operator forced by modular half-integers

Let $c_{kl}$ be the coefficients in the question and set
$d_{kl}=(-1)^{kl}c_{kl}$. For every integer representative $x$,

$$
(-1)^{kl}T_N(l,k)\psi(x)
=e^{2\pi i k(xh+lh/2)}\psi(x+l).
$$

Indeed the representative $(N+1)/2$ of $2^{-1}$ differs from the ordinary half by $N/2$. Thus the exact matrix is

$$
A_N\psi(x)
=\sum_{k,l}d_{kl}e^{2\pi i k(xh+lh/2)}\psi(x+l).
\tag{6}
$$

All nonzero coefficients have $|k|\le9$, $|l|\le1$, and

$$
\sum_{k,l}|d_{kl}|<2.
\tag{7}
$$

For (7), the Fourier coefficient $\ell^1$ norm of $r$ is at most $4$. The five displayed contributions to $f-1/10$ are bounded respectively by $1,0.4,0.04,0.04,0.1$. Their sum is $1.58<2$. The largest frequency in $r\sin(2\pi q)$ is $9$.

The real ordinary symbol of (6) is

$$
a(q,p)=V(q)+\frac{r(q+1/2)}{100}
              \cos(2\pi p-\alpha_0),
\quad
V(q)=\cos(14\pi q)+\frac{r(q)}{10}
 +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}.
\tag{8}
$$

This half-period correction is necessary. Omitting it would change the classical flow used below. The Hamiltonian vector field for $e^{+itA_N/h}$ in the conventions of this note is

$$
Y(q,p)=\frac1{2\pi}(-a_p,a_q).
\tag{9}
$$

For example the real coordinate row-sum derivative bound obtained directly from (7) is

$$
\|DY\|_\infty
\le2\pi\sum|d_{kl}|
 \max\{|l|(|k|+|l|),\,|k|(|k|+|l|)\}
<360\pi<2000.
\tag{10}
$$

## 3. A global analytic graph class with a uniform budget

This is the step needed to make the constants in (1) exponential in the number of iterates.

Fix

$$
\rho=10^{-3},\qquad \eta=100\tau.
$$

Consider real graphs

$$
p(q)=r q+b+w(q),\qquad
-1\le r\le-1/2,\quad b\in\mathbb R,
\tag{11}
$$

where $w$ is holomorphic on the full horizontal strip
$|\operatorname{Im}q|<\rho$, is real on the real axis, and
$\|w\|_\rho\le\eta$. There is no bound on the real intercept $b$ in this analytic assertion. Its integer part can be normalized separately at the sampled level.

### 3.1. The linear graph transform doubles the available strip

The canonical transformation generated by

$$
S(Q,q)=-\frac\pi4(3Q^2-2Qq+3q^2)
\tag{12}
$$

is

$$
(Q,P)=(3q-4p,-2q+3p).
\tag{13}
$$

For a graph (11), set $B=3-4r\ge5$. The input point associated with the output $Q$ is the unique solution of

$$
q(Q)=\frac{Q+4b+4w(q(Q))}{B}.
\tag{14}
$$

For $|\operatorname{Im}Q|<2\rho$, the unperturbed center
$(Q+4b)/B$ has imaginary part at most $2\rho/5$.
On the disk of radius $\rho/4$ about this center, (14) maps into itself because $4\eta/B<\rho/4$. The disk stays within
$|\operatorname{Im}q|<3\rho/4$, where Cauchy's bound gives
$|w'|\le4\eta/\rho$. The contraction factor is at most
$16\eta/(B\rho)<1/2$. The contraction solution is unique, holomorphic in $Q$, and real for real $Q$.

A direct substitution into (13) gives

$$
P(Q)=r_1Q+b_1+w_1(Q),
\quad
r_1=\frac{-2+3r}{3-4r},\quad
b_1=\frac bB,\quad
w_1(Q)=\frac{w(q(Q))}{B}.
\tag{15}
$$

Thus

$$
-\frac57\le r_1\le-\frac7{10},\qquad
\|w_1\|_{2\rho}\le\eta/5.
\tag{16}
$$

Adding a constant to input or output momentum changes only $b$, and does not affect this assertion.

### 3.2. The exact short kick preserves the original class

Start from any graph on the strip $2\rho$ satisfying (16). For initial points with $|\operatorname{Im}q_0|<3\rho/2$, the initial momentum has
$|\operatorname{Im}p_0|<2\rho$. On the larger complex tube

$$
|\operatorname{Im}q|\le3\rho,\qquad
|\operatorname{Im}p|\le4\rho,
$$

the finite Fourier expression and (7) give

$$
|Y_q|\le2e^{2\pi(27\rho+4\rho)}<3,\qquad
|Y_p|\le18e^{2\pi(27\rho+4\rho)}<30.
\tag{17}
$$

The holomorphic flow of (9) therefore exists through time $\tau$ on the smaller initial strip, remains within the displayed tube, and has

$$
q=q_0+\delta q(q_0),\quad p=p_0+\delta p(q_0),
\qquad
\|\delta q\|_{3\rho/2}\le3\tau,\quad
\|\delta p\|_{3\rho/2}\le30\tau.
\tag{18}
$$

One can obtain this directly by Picard iteration on the complex tube: its derivative bounds are finite by the same finite Fourier expression, and the displacement bounds (17) are much smaller than the available margins. Thus no real-to-complex flow extension is being assumed without control.

For $|\operatorname{Im}q|<\rho$, the equation
$q_0=q-\delta q(q_0)$ is a contraction on the radius-$\rho/4$ disk about $q$. On that disk Cauchy's estimate bounds
$|\delta q'|\le12\tau/\rho<1/2$. Hence the inverse is holomorphic, and
$|q_0-q|\le3\tau$. The new graph is

$$
p(q)=r_1 q+b_1+w_{\rm new}(q),
\quad
w_{\rm new}=w_1(q_0)+\delta p-r_1\delta q.
$$

It obeys

$$
\|w_{\rm new}\|_\rho
\le\eta/5+33\tau=53\tau<\eta.
\tag{19}
$$

Thus one linear step followed by the actual kick preserves (11), while it restores all the analytic width needed for the next step. This width restoration is why the derivative bounds do not accumulate a loss with the number of steps.

For every fixed derivative order $j$, all graphs obtained in this way satisfy on the real axis

$$
|w^{(j)}(q)|\le j!(2/\rho)^j\eta.
\tag{20}
$$

Only finitely many orders, at most eight, are used below. In particular their bounds are independent of the number of previous branches and iterates.

## 4. Localized sampled WKB vectors and the exact kick

Use a fixed smooth partition of unity on the circle, consisting of four lifted functions $\chi_j$ supported on intervals of length $2/5$, with lifts lying in $(-1,2)$. For definiteness, one may take

$$
\zeta(t)=
\begin{cases}
\exp[-1/(1-25t^2)],& |t|<1/5,\\
0,& |t|\ge1/5,
\end{cases}
$$

$$
D(q)=\sum_{n\in\mathbb Z}\zeta(q-n/4),\qquad
\chi_j(q)=\zeta(q-j/4)/D(q),\quad j=0,1,2,3.
\tag{21}
$$

The denominator is positive, smooth, and $1/4$-periodic; the integer periodizations of the four $\chi_j$'s sum to $1$.
All their required derivatives are fixed finite constants.

A lifted WKB piece with amplitude $b$, supported in an interval of length less than $1/2$, means the sampled periodic vector

$$
v_h(x)=\sqrt h\sum_{n\in\mathbb Z}
 b(xh+n)\exp(iF(xh+n)/h),\qquad
F'=2\pi p,
\tag{22}
$$

where $p$ belongs to (11). There is at most one nonzero term per piece and coordinate. All actual supports considered below stay in a fixed bounded family of the charts $(-1,2)$. A kick moves each support by less than $3\tau$, and the next linear step reapplies (21).

The integer part of $b$ in the graph intercept, as opposed to the amplitude bearing the same conventional letter in (22), can be reduced modulo $\mathbb Z$ at every stage: replacing $F(q)$ by $F(q)-2\pi n q$ changes (22) by the factor $e^{-2\pi i n x}=1$. This exact sampled identity also respects the kick, because (8) is periodic in momentum. Below, whenever a bound on the real momentum is used, the graph intercept has first been so normalized to $[-1/2,1/2]$.

To avoid this temporary notational overlap in the calculation, denote the amplitude by $B(t,q)$. Solve

$$
F_t=a(q,F_q/(2\pi)),\qquad
B_t=vB_q+\frac12\frac d{dq}v\,B,\qquad
v=\frac{a_p(q,F_q/(2\pi))}{2\pi}.
\tag{23}
$$

The characteristic map for (23) is precisely (9). If $J=\partial q(t,q_0)/\partial q_0$, then

$$
B(t,q(t,q_0))=B(0,q_0)\,J^{-1/2}.
\tag{24}
$$

All needed derivatives of the characteristic inverse and $J^{-1/2}$, through order four, are uniformly bounded, by (17)--(20) and Cauchy's estimates on a fixed smaller strip. Consequently there is a fixed finite $C_{\rm kick}$ such that

$$
\|B(\tau)\|_{C^4}\le C_{\rm kick}\|B(0)\|_{C^4}.
\tag{25}
$$

Here and below $C^4$ denotes the maximum of the suprema of derivatives of orders zero through four on the full real line.

The approximation to the **actual** matrix exponential has a direct finite-shift proof. Taylor expansion in (6), uniformly over all the graphs in (11), gives

$$
A_N(Be^{iF/h})
=e^{iF/h}\left[
 a(q,p)B
 -ih\left(vB_q+\tfrac12v'B\right)
 +h^2 E_h\right],
\quad
\|E_h\|_\infty\le C_{\rm Tay}\|B\|_{C^2}.
\tag{26}
$$

For clarity the coefficient before rewriting the $h$-term is

$$
\sum_{k,l}d_{kl}e^{2\pi i(kq+lp)}
 \left(lB_q+i\pi klB+\tfrac i2l^2F_{qq}B\right),
$$

which equals $-i(vB_q+\tfrac12v'B)$. The finite number of shifts, (20), and the real nature of the phase give the remainder in (26); it is not an expansion in $\tau/h$.

After the factor $\sqrt h$ in (22), the residual in
$h\partial_t v_h=iA_Nv_h$ is $O(h^{5/2}\|B(0)\|_{C^4})$ at each sample, hence $O(h^2\|B(0)\|_{C^4})$ in $\ell^2$. Duhamel's identity and the exact unitarity of $e^{itA_N/h}$ now give

$$
\|e^{i\tau A_N/h}v_h-v_h^{\rm WKB}(\tau)\|_2
 \le C_{\rm err,kick}\,h\,\|B(0)\|_{C^4}.
\tag{27}
$$

All constants in (25)--(27) are independent of $N$, the graph, and the number of prior iterates. Periodizing the lifted calculation causes no additional boundary term: the coefficient in (6) is periodic in $q$, and the shifted periodic sum in (22) is exact.

## 5. Exact eight-character decomposition of $M_N$

Choose the integer representative $\bar8$ of $8^{-1}\pmod N$ with $0\le\bar8<N$. Then

$$
8\bar8=1+s_NN,\qquad s_N\in\{1,3,5,7\}.
$$

For any integer lifts $x,y$, (12) gives the exact identity

$$
(M_N)_{xy}
=\sqrt h\,e^{iS(xh,yh)/h}\,
 \chi_{s_N}(x,y),
\tag{28}
$$

$$
\chi_s(x,y)=
\exp[-2\pi i s(3x^2-2xy+3y^2)/8].
$$

The last factor is periodic modulo $8$ in both variables. Write its finite Fourier expansion as

$$
\chi_s(x,y)=
\sum_{u,v=0}^7\beta^{(s)}_{uv}
  e^{2\pi i(ux+vy)/8}.
\tag{29}
$$

Parseval gives $\sum|\beta_{uv}^{(s)}|^2=1$, so
$\sum|\beta_{uv}^{(s)}|\le8$. At a fixed source $y$, the one-variable expansion uses eight characters with coefficient $\ell^1$ norm at most $\sqrt8$.

Applying (21) to $M_Ne_y$, therefore, gives an **exact** family of at most $32$ pieces (22), with phases

$$
F(q)=S(q,yh)+2\pi u q/8,\qquad
p(q)=-\frac34q+\frac{yh}{4}+\frac u8.
\tag{30}
$$

These initial graphs have $w=0$ and extend to every strip. Their amplitudes have a uniformly bounded sum of $C^4$ norms. By Section 4 their first kicks obey the same fixed budget as every later kick.

## 6. One linear step: a finite leading family with an $O(h)$ vector error

Apply $M_N$ to a piece (22). After inserting (28)--(29), each character term is of the form

$$
h\sum_{n\in\mathbb Z}B(nh)
 \exp\!\left(\frac{i}{h}
   [S(Q,nh)+F(nh)+2\pi vnh/8]\right).
$$

Poisson summation gives exactly

$$
\sum_{k\in\mathbb Z}
 \int_{\mathbb R}B(y)e^{i\Phi_{v,k}(Q,y)/h}\,dy,
\qquad
\Phi_{v,k}=S(Q,y)+F(y)+2\pi(v/8-k)y.
\tag{31}
$$

This is a finite-dimensional matrix identity followed by ordinary Poisson summation of a compactly supported smooth function. The output character subsequently adds $2\pi uQ/8$ to the phase.

For every real $Q,y$,

$$
\partial_y^2\Phi_{v,k}
=2\pi(r+w'(y)-3/4).
\tag{32}
$$

By (20), this is bounded between two fixed negative constants. Thus $\Phi_{v,k}$ has a unique real critical point $y_c(Q)$. Its graph transform is exactly (14)--(15), with the input intercept shifted by $v/8-k$, and with the output character shift $u/8$.

All input and output chart coordinates lie in $(-1,2)$, and the input intercept is normalized to $[-1/2,1/2]$. The bounds in Sections 2--3 give a fixed upper bound, less than $12\pi$, on
$|S_y+F_y+2\pi v/8|$ on these supports. In particular for $|k|>20$ the derivative $\partial_y\Phi_{v,k}$ is bounded below by a fixed positive constant times $1+|k|$ on the amplitude support. Four integrations by parts, using the uniform bounds on phase derivatives and the compact smooth amplitude, yield

$$
\left|\int B(y)e^{i\Phi_{v,k}/h}\,dy\right|
\le C_{\rm tail}\,
 h^4(1+|k|)^{-4}\|B\|_{C^4}
\qquad(|k|>20).
\tag{33}
$$

The large $|k|$ tails are summable. No number of retained Poisson modes grows with $N$ or the iteration count.

For $|k|\le20$, uniform one-dimensional stationary phase gives

$$
\int B(y)e^{i\Phi_{v,k}(Q,y)/h}\,dy
=
\sqrt{2\pi h}\,e^{-i\pi/4}
 \frac{B(y_c(Q))}
      {\sqrt{-\Phi_{yy}(Q,y_c(Q))}}\,
 e^{i\Phi_{v,k}(Q,y_c(Q))/h}
+O(h^{3/2}\|B\|_{C^4}).
\tag{34}
$$

A proof and its constant dependence are useful here. By (32), the global change of variable
$\Phi(y)-\Phi(y_c)=-z^2/2$, with $z$ increasing with $y$, is smooth and invertible. Its derivatives and inverse derivatives to the orders used below are uniformly bounded on the relevant supports: strict concavity, the uniform phase bounds (20), and the fixed bound $|k|\le20$ give this directly by differentiating the defining equation, or by writing
$-2(\Phi(y)-\Phi(y_c))/(y-y_c)^2$ as the integral of
$-2(1-t)\Phi''(y_c+t(y-y_c))$.
The transformed amplitude $\widetilde B(z)$ has fixed bounded support length and a $C^4$ norm at most a constant times $\|B\|_{C^4}$.
With the Fourier convention
$\widetilde B(z)=(2\pi)^{-1}\int\widehat B(t)e^{itz}\,dt$,
the damped Gaussian integral and then its damping limit give

$$
\int e^{-iz^2/(2h)}\widetilde B(z)\,dz
=\sqrt{2\pi h}e^{-i\pi/4}
 (2\pi)^{-1}\int\widehat B(t)e^{iht^2/2}\,dt.
$$

Subtract $\widetilde B(0)$ and use
$|e^{iht^2/2}-1|\le ht^2/2$.
Four integrations by parts in the Fourier transform show
$\int t^2|\widehat B(t)|\,dt
 \le C\|\widetilde B\|_{C^4}$, since its support length is uniformly bounded.
This proves the error in (34), including the case in which the critical point lies outside the amplitude support.

Multiply each leading term by each output cutoff in (21). The resulting phase is real and its momentum graph belongs to the class in Section 3 before the next kick. Its amplitude, including the factor
$\sqrt{2\pi}e^{-i\pi/4}\beta_{uv}^{(s_N)}$, is

$$
\chi_j(Q)\,
\frac{\sqrt{2\pi}e^{-i\pi/4}\beta_{uv}^{(s_N)}
       B(y_c(Q))}
     {\sqrt{-\Phi_{yy}(Q,y_c(Q))}}.
\tag{35}
$$

All graph derivatives required to differentiate (35) four times are uniformly bounded by (20). The inverse critical map has uniformly bounded derivatives, and its first derivative is uniformly separated from zero. Hence there is a fixed finite $C_{\rm lin}$ such that the sum of the $C^4$ norms of all these leading amplitudes is at most
$C_{\rm lin}\|B\|_{C^4}$.

There are at most $64\cdot41\cdot4=10496$ terms for each input piece, a fixed number. The total pointwise error from (33)--(34) is
$O(h^{3/2}\|B\|_{C^4})$. Since there are $N=h^{-1}$ output samples, it has $\ell^2$ norm

$$
\|M_Nv_h-v_h^{\rm lead}\|_2
 \le C_{\rm err,lin}\,h\,\|B\|_{C^4}.
\tag{36}
$$

The finite torus and lifted formulas agree exactly even for charts crossing the coordinate origin. In (28) the full product of the ordinary quadratic exponential and the eight-periodic character equals the original modular kernel for every integer lift. Thus no single character is required to be separately periodic under a lift by $N$.

## 7. Exponential iteration budget and proof of (1)

Let $S_m$ be the sum of the $C^4$ amplitude norms in the leading family after $m$ applications of $U_N$. Sections 4--6 show that a fixed finite $A_0$ exists such that

$$
S_{m+1}\le A_0S_m,
\qquad
\|\text{new vector error at step }m+1\|_2
 \le C_0 h S_m.
\tag{37}
$$

For example $A_0=C_{\rm kick}C_{\rm lin}$; $C_0$ may be taken as
$C_{\rm err,lin}+C_{\rm err,kick}C_{\rm lin}$.
These are suprema of the explicitly bounded amplitude maps in
(25), (35), and their remainder bounds. Their finiteness follows from the fixed strip $\rho$, the finite character and Poisson sets, and the fixed cutoff (21). They are not unproved estimates on long orbit sums.

The first step uses (30) and one kick, so $S_1$ and its error coefficient are bounded by fixed constants. Old errors are propagated by the **exact** unitary $U_N$, so their $\ell^2$ norms do not grow. Taking a fixed $A>\max(2,A_0)$ and summing the geometric series in (37) gives

$$
U_N^m e_y
=\sqrt h\sum_{\beta}B_\beta(q)e^{iF_\beta(q)/h}
   +e_{m,N,y},
\qquad
\sum_\beta\|B_\beta\|_{C^4}\le C A^m,\quad
\|e_{m,N,y}\|_2\le C h A^m.
\tag{38}
$$

Periodization as in (22) is implicit in the first term. Its pointwise norm is at most $C\sqrt h A^m$, and
$\|e\|_\infty\le\|e\|_2\le ChA^m$. This proves (1).

This proof provides the dependence $A^m$, not a convenient numerical value of $A$. A numerical value could be extracted by inserting derivative bounds for (21) into (25) and (35), but no such value is needed in the logarithmic argument. Crucially, the analytic graph class is reset at every step by (15)--(19); a generic repeated $C^r$ estimate without that reset would not establish (37).

## 8. The temporal frame and proof of (2)

Let

$$
L_N=\left\lfloor\frac{\log N}{4\log A}\right\rfloor.
$$

For a fixed coordinate $x$, form the frame
$v_j=U_N^{-j}e_x$, $j=0,\ldots,L_N-1$.
Its Gram matrix has diagonal entries $1$; by (1), every off-diagonal entry has modulus at most

$$
C A^{L_N}N^{-1/2}\le C N^{-1/4}.
$$

The matrix row-sum bound therefore gives

$$
\left\|\sum_{j=0}^{L_N-1}|v_j\rangle\langle v_j|\right\|
=\|(\langle v_j,v_k\rangle)_{jk}\|
\le1+(L_N-1)C N^{-1/4}.
$$

For any normalized eigenvector $\psi$,
$|\langle v_j,\psi\rangle|=|\psi(x)|$, including when $\psi$ belongs to a degenerate eigenspace. Hence

$$
L_N|\psi(x)|^2
\le1+(L_N-1)C N^{-1/4},
\quad
\mu_N\le L_N^{-1}+C N^{-1/4}.
\tag{39}
$$

This proves (2).

## 9. The exact missing quantum modes and proof of (3)--(5)

The full commutant projection is

$$
\mathcal P_N(X)=\sum_\lambda\Pi_\lambda X\Pi_\lambda.
$$

Using the coordinate-diagonal orthonormal basis $E_{xx}$ for the range of $\mathcal D_N$ gives

$$
\operatorname{Tr}_{\mathcal V_N}(\mathcal P_N\mathcal D_N)
=\sum_x\langle E_{xx},\mathcal P_N(E_{xx})\rangle_{\rm HS}
=\sum_{\lambda,x}(\Pi_{\lambda,xx})^2.
$$

For every eigenspace,

$$
\Pi_{\lambda,xx}
=\sup_{\substack{\psi\in\operatorname{Ran}\Pi_\lambda\\\|\psi\|=1}}
 |\psi(x)|^2
\le\mu_N.
$$

Since $\sum_{\lambda,x}\Pi_{\lambda,xx}=N$, (3) follows. Subtract it from $\operatorname{Tr}\mathcal P_N=d_N$ to obtain (4).

If $\operatorname{Ran}\mathcal T_N\subset\operatorname{Ran}\mathcal D_N$, then
$(I-\mathcal D_N)\mathcal T_N=0$. Since
$\mathcal R_N\mathcal P_N=(1-r_N)^{-1}\mathcal P_N$,

$$
(I-\mathcal D_N)(\mathcal R_N-\mathcal T_N)\mathcal P_N
=(1-r_N)^{-1}(I-\mathcal D_N)\mathcal P_N.
$$

Multiplication on either side by an orthogonal projection is a contraction in the superoperator Hilbert--Schmidt norm. Thus

$$
\|\mathcal R_N-\mathcal T_N\|_{\mathrm{HS}(\mathcal V_N)}^2
\ge(1-r_N)^{-2}
 \|(I-\mathcal D_N)\mathcal P_N\|_{\mathrm{HS}(\mathcal V_N)}^2
=(1-r_N)^{-2}
 \operatorname{Tr}(\mathcal P_N(I-\mathcal D_N)).
$$

Equations (2)--(4) and
$N(1-e^{-2s/N})\to2s$ prove (5).

## 10. Scope for the phase-transfer route

The operator in (5) is the full quantum doubled transfer. Its fixed space contains all spectral projectors and, in a degenerate eigenspace, every matrix on that eigenspace. The estimate shows quantitatively for the specified $U_N$ that its massless sector is almost entirely invisible to position-diagonal fields. It rules out an $o(N^3)$ squared-Hilbert--Schmidt approximation of its resolvent by maps with position-diagonal range.

It does not rule out a construction which retains the exact commutant term

$$
(1-r_N)^{-1}\mathcal P_N
$$

and then treats the complementary quantum modes. After retaining that term the remaining resolvent is

$$
(I-\mathcal P_N)(I-r_N\mathcal C_N)^{-1}.
$$

Its eigenvalues are the factors
$(1-r_Ne^{i(\vartheta_\lambda-\vartheta_\nu)})^{-1}$ for unequal spectral phases. Bounding their aggregate at $r_N=e^{-2s/N}$ requires the microscopic phase-gap information sought in the original problem. The logarithmic-time argument above does not provide that information.

For reference, direct geometric-series expansion gives the exact identity

$$
\|\mathcal R_N\|_{\mathrm{HS}(\mathcal V_N)}^2
=\frac{N^2+2\sum_{m\ge1}r_N^m|\operatorname{Tr}U_N^m|^2}
       {1-r_N^2}.
\tag{40}
$$

Thus (5) is at the scale relevant to the smoothed pair form factor. It is not itself a value of that form factor, because a lower bound on approximation error is not a lower bound on the difference of the squared norms, and because the exact commutant contribution can be retained explicitly.

The first unresolved fixed compact-Fourier pair test remains precisely the one in the main report. Nothing in (1)--(40) establishes its required signed cancellation. No claim that position-diagonal replacement is the only possible supersymmetric or matrix-valued approach is made.

## 11. Primary-literature discriminator

The exact global-phase supersymmetric transformation for an individual quantum map retains full matrix-valued fields. Its quadratic operator is $I-z\,\operatorname{Ad}_U$, not a Markov operator built from $|U_{xy}|^2$. Zirnbauer's extended treatment explicitly distinguishes its exact identity from the stochastic Hamiltonian-flow averaging used to justify a simpler effective action. The present calculation explains one concrete obstruction to collapsing the individual-map field space.

By contrast, the quantum-graph transformation of Pluhař--Weidenmüller includes separate phase integrations for separate bonds. Those integrations have no counterpart in the problem's single global angle $\alpha$. No graph universality theorem is transferred to the specified $U_N$ here.

Primary texts inspected:

- M. R. Zirnbauer, *The Color-Flavor Transformation and a New Approach to Quantum Chaotic Maps*, https://arxiv.org/pdf/chao-dyn/9810016 .
- M. R. Zirnbauer, *Pair Correlations of Quantum Chaotic Maps from Supersymmetry*, https://arxiv.org/pdf/chao-dyn/9812023 , especially the exact matrix-field action and the later stochastic averaging discussion.
- Z. Pluhař and H. A. Weidenmüller, *Quantum Graphs and Random-Matrix Theory*, https://arxiv.org/pdf/1407.1148 , Section 3.2 and its independent bond-phase integrations.

These sources motivate and discriminate the proposed transfer routes. The family-specific estimates (1)--(5) are proved above from the definitions, not inferred from those sources.

