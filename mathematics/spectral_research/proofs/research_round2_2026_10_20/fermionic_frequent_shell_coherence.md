> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_frequent_shell_coherence.md`. Embedded SHA256: `21c536cdcb9c8f5dc43aa5c7e74300865b0152f7187b8358b68832b2ae21e285`.
> [Thematic guide](../../topics/histories.md).

# Frequent variable-run shells: a logarithm-squared coherence term

Research continuation, 20 October 2026. This note concerns the exact
fixed-point scattering intervals already constructed for the specified
map at the fixed parameter $\tau=10^{-80}$. It does not prove
$H_{\rm diag}$. Its new result is a quantitative test of the proposal
to handle frequent markers by summing all zero-run lengths independently.

## 1. Inputs, theorem, and scope

The only dynamical input to the operator theorem is:

| Input | SHA-256 |
|---|---|
| arithmetic_all_marker_domains_and_renewal_barrier.md | dc8bef986cae11bc1917805a02746cd0861ee06f74da1d853bcc82e25ba7deba |

For the discussion of the phase which is still missing, we also use:

| Input | SHA-256 |
|---|---|
| fermionic_signed_three_cell_profile.md | edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5 |

The first input constructs two fixed intervals $J_S,J_U$, containing
zero in their interiors, in the actual stable and unstable scattering
coordinates. Put
$$
 J_S=[-A,B],\qquad |J_U|=C,\qquad A,B,C>0,\qquad
 \rho=\Lambda^{-1}\in(0,1/5),\qquad h=\log\Lambda.
 \tag{1.1}
$$
The intervals need not be centered at zero. All these quantities are
fixed independently of $N$ and of the Fourier parameter below.

Let $P_r$ be multiplication by the indicator of $\rho^rJ_S$,
and let $Q_s$ be multiplication by the indicator of $\rho^sJ_U$.
Set
$$
 E_r=P_r-P_{r+1},\qquad F_s=Q_s-Q_{s+1},\qquad r,s\ge0.
 \tag{1.2}
$$
Thus each input shell consists of one positive interval and one negative
interval, with a common shell index. Endpoints and the limiting point
zero have measure zero.

For $\beta>0$, define the unitary scaled Fourier transform
$$
 (\mathcal F_\beta f)(u)
 =\sqrt\beta\int_{\mathbb R}e^{-2\pi i\beta su}f(s)\,ds.
 \tag{1.3}
$$
The full restricted amplitude and its Gram operator are
$$
 \mathcal A_\beta=Q_0\mathcal F_\beta P_0,\qquad
 G_\beta=\mathcal A_\beta^*\mathcal A_\beta.
 \tag{1.4}
$$
The operator obtained by summing the separate block Grams is
$$
 D_\beta=\sum_{r,s\ge0}
    (F_s\mathcal F_\beta E_r)^*(F_s\mathcal F_\beta E_r)
 =\sum_{r\ge0}E_rG_\beta E_r.
 \tag{1.5}
$$
The series in (1.5) converges in trace norm.

**Theorem.** The two operators in (1.4)--(1.5) are positive
trace-class contractions with the same trace
$$
 L_\beta=\beta C(A+B).
 \tag{1.6}
$$
Their omitted coherence satisfies
$$
 \boxed{\begin{aligned}
 \Delta_\beta
 &:=\operatorname{Tr}G_\beta^2-\operatorname{Tr}D_\beta^2\\
 &=\|G_\beta-D_\beta\|_{\rm HS}^2
   =\sum_{r\ne r'}\|E_rG_\beta E_{r'}\|_{\rm HS}^2\\
 &=\frac{(\log\beta)^2}{\pi^2\log\Lambda}+O(\log\beta),
       \qquad \beta\longrightarrow\infty .
 \end{aligned}}
 \tag{1.7}
$$
The constant in the remainder depends only on the fixed intervals
and $\rho$.

For every fixed $0<t<1$,
$$
 \boxed{
 -\frac{t^2}{2(1-t)^2}\Delta_\beta
 \le
 \log\frac{\det(I-tG_\beta)}{\det(I-tD_\beta)}
 \le
 -\frac{t^2}{2}\Delta_\beta.}
 \tag{1.8}
$$
In particular, the full coherent determinant divided by the product of
the independent-shell determinants is
$$
 \frac{\det(I-tG_\beta)}
 {\displaystyle\prod_{r\ge0}\det(I-tE_rG_\beta E_r)}
 =\exp\{-\Theta_t((\log\beta)^2)\}.
 \tag{1.9}
$$
This is an exact operator statement, with no random phases and no
semiclassical approximation.

There is a useful qualification. At fixed $t>0$, both determinants
in (1.8) tend to zero. Hence their large relative discrepancy does
not by itself rule out an absolute $o(1)$ difference. A precise
unbounded coefficient discrepancy, for which that qualification is
irrelevant, is
$$
 \boxed{
 e_2(G_\beta)-e_2(D_\beta)
 =-\frac12\Delta_\beta
 =-\frac{(\log\beta)^2}{2\pi^2\log\Lambda}
      +O(\log\beta).}
 \tag{1.10}
$$

## 2. Exact coherent reconstruction and reduction to the sine kernel

The restrictions of the kernel in (1.3) to the rectangles
$$
 (\rho^rJ_S\setminus\rho^{r+1}J_S)
 \times
 (\rho^sJ_U\setminus\rho^{s+1}J_U)
$$
are mutually orthogonal in Hilbert--Schmidt space. They partition the
full rectangle, up to sets of measure zero. Consequently
$$
 \mathcal A_\beta
   =\sum_{r,s\ge0}F_s\mathcal F_\beta E_r
       \quad\hbox{in Hilbert--Schmidt norm},\qquad
 \sum_{r,s}\|F_s\mathcal F_\beta E_r\|_{\rm HS}^2
   =L_\beta.
 \tag{2.1}
$$
The convergence is unconditional because the summands are orthogonal
in that Hilbert space. Thus summing all shells coherently recovers
the full restricted Fourier transform exactly.

Positivity and the trace formula for $G_\beta$ follow by taking
the Gram of the Hilbert--Schmidt amplitude. Its norm is at most one
because the Fourier transform is unitary. The diagonal shell blocks
in (1.5) are positive, and their traces sum to $L_\beta$, so the
positive partial sums converge in trace norm. For every $v$,
$$
 \langle v,D_\beta v\rangle
 =\sum_r\langle E_rv,G_\beta E_rv\rangle
 \le\sum_r\|E_rv\|^2=\|P_0v\|^2.
 \tag{2.2}
$$
This proves the contraction assertion for $D_\beta$.

Let $\bar u$ be the midpoint of $J_U$. The integral kernel of
$G_\beta$, on $J_S\times J_S$, is
$$
 e^{2\pi i\beta\bar u(s-s')}
 \frac{\sin(\pi\beta C(s-s'))}{\pi(s-s')}.
 \tag{2.3}
$$
The phase is removed by unitary multiplication. The change of
variable $x=\beta Cs$, with its unitary $L^2$ normalization,
then turns (2.3) into
$$
 k(x-y)=\frac{\sin\pi(x-y)}{\pi(x-y)}
 \tag{2.4}
$$
on the interval $[-T_-,T_+]$, where
$$
 T_-=A\beta C,\qquad T_+=B\beta C.
 \tag{2.5}
$$
This is the ordinary sine compression on an interval of length
$L_\beta$; a translation can identify it with any other interval
of the same length.

The positive and negative pieces of the rescaled shell $r$ are
$$
 I_r^+=(T_+\rho^{r+1},T_+\rho^r),\qquad
 I_r^-=(-T_-\rho^r,-T_-\rho^{r+1}).
 \tag{2.6}
$$
The Hilbert--Schmidt kernel decomposes into disjoint rectangles.
Deleting the diagonal shell rectangles gives
$$
 \Delta_\beta
 =\sum_{r\ne r'}
   \int_{I_r^+\cup I_r^-}
   \int_{I_{r'}^+\cup I_{r'}^-}
       k(x-y)^2\,dy\,dx.
 \tag{2.7}
$$
It also gives the Hilbert--Schmidt orthogonality identity
$\Delta_\beta=\|G_\beta-D_\beta\|_{\rm HS}^2$.
The difference between the two second power traces is the same
quantity, because $G_\beta,D_\beta$ are self-adjoint and their
diagonal and off-diagonal block kernels are orthogonal.

## 3. The contribution of adjacent shells

The two shells on one side of zero have adjacent intervals with
lengths $a$ and $b=\rho a$. After translating their common
endpoint, their interaction is
$$
 H(a,b)=\int_0^a\int_0^b k(u+v)^2\,dv\,du.
 \tag{3.1}
$$
Assume $a\ge b>0$. The convolution weight of the two indicator
functions equals $t$ for $0<t<b$, equals $b$ for $b<t<a$,
and equals $a+b-t$ for $a<t<a+b$. Thus
$$
 H(a,b)
 =\frac1{\pi^2}\int_0^b\frac{\sin^2\pi t}{t}\,dt+O(1),
 \qquad b\ge1,
 \tag{3.2}
$$
uniformly in $a\ge b$. Indeed the contribution for $t\ge b$
is bounded by
$$
 \frac1{\pi^2}\int_b^\infty\frac b{t^2}\,dt
 =\frac1{\pi^2}.
$$
For the first integral, use $\sin^2\pi t=(1-\cos2\pi t)/2$.
The integral on $(0,1)$ is finite; integration by parts bounds
$\int_1^b\cos(2\pi t)\,dt/t$ uniformly. Therefore
$$
 H(a,b)=\frac{1}{2\pi^2}\log b+O(1),
       \qquad b\ge1.
 \tag{3.3}
$$
When $b<1$ and $b=\rho a$, the bound $|k|\le1$ gives
$$
 H(a,\rho a)\le a(\rho a)=b^2/\rho.
 \tag{3.4}
$$

For one side of length $T$, the adjacent intervals at indices
$r,r+1$ have lengths
$$
 a_r=(1-\rho)T\rho^r,\qquad b_r=\rho a_r.
 \tag{3.5}
$$
Write $v=\log(\rho(1-\rho)T)$. For large $T$, the indices
with $b_r\ge1$ are $0\le r\le\lfloor v/h\rfloor$, and
$$
 \begin{aligned}
 \sum_{b_r\ge1}\log b_r
 &=\sum_{r=0}^{\lfloor v/h\rfloor}(v-rh)\\
 &=\frac{v^2}{2h}+O(v)
  =\frac{(\log T)^2}{2h}+O(\log T).
 \end{aligned}
 \tag{3.6}
$$
There are $O(\log T)$ such indices, so the sum of the uniform
remainders in (3.3) is $O(\log T)$. By (3.4), the sum over
$b_r<1$ is bounded by a convergent geometric series, uniformly
in $T$. It follows that
$$
 \sum_{r\ge0}H(a_r,\rho a_r)
 =\frac{(\log T)^2}{4\pi^2h}+O(\log T).
 \tag{3.7}
$$

Both orders $(r,r+1)$ and $(r+1,r)$ occur in (2.7).
Applying (3.7) separately to $T_+$ and $T_-$, the total
same-side adjacent contribution is
$$
 \begin{aligned}
 2\sum_{r\ge0}H(a_r^+,\rho a_r^+)
 +2\sum_{r\ge0}H(a_r^-,\rho a_r^-)
 &=\frac{(\log T_+)^2+(\log T_-)^2}{2\pi^2h}
      +O(\log\beta)\\
 &=\frac{(\log\beta)^2}{\pi^2h}+O(\log\beta).
 \end{aligned}
 \tag{3.8}
$$
This accounts for the leading term, including both sides of
the fixed point and both ordered directions.

## 4. All remaining shell interactions are $O(\log\beta)$

We give bounds for the full remaining sum, rather than using
a cutoff with an uncontrolled infinite tail.

### 4.1. Nonadjacent intervals on the same side

Suppose the outer interval has index $r$, outer endpoint
$X=T\rho^r$, and the inner one has index $r+d$, $d\ge2$.
The inner outer endpoint is $Y=X\rho^d$. The distance between
the two intervals is at least
$$
 \rho X-Y\ge\rho(1-\rho)X.
$$
Their lengths are $(1-\rho)X$ and $(1-\rho)Y$.
Using $|k(t)|\le1/(\pi|t|)$ gives
$$
 \int_{I_r}\int_{I_{r+d}}k(x-y)^2\,dy\,dx
 \le C_\rho\rho^d.
 \tag{4.1}
$$
When $X\ge1$, summing over $d\ge2$ costs a fixed constant.
There are $O(\log T)$ such outer intervals.

When $X<1$, use $|k|\le1$ instead:
$$
 \int_{I_r}\int_{I_{r+d}}k(x-y)^2\,dy\,dx
 \le(1-\rho)^2X^2\rho^d.
 \tag{4.2}
$$
Summing over all $d\ge2$ and then all unresolved outer
intervals $X<1$ costs $O(1)$. Including both ordered
directions, all nonadjacent same-side terms are $O(\log T)$.

### 4.2. Opposite sides of zero

For an interval on the positive side let $X=T_+\rho^r$;
for one on the negative side let $Y=T_-\rho^{r'}$.
Their distance is at least $\rho(X+Y)$, and the product of
their lengths is $(1-\rho)^2XY$. Consequently their
interaction is at most
$$
 C_\rho\min\left\{XY,\frac{XY}{(X+Y)^2}\right\}
 \le C_\rho\min\{XY,X/Y,Y/X\}.
 \tag{4.3}
$$
For fixed $X>0$, the geometric sequence $Y=T_-\rho^{r'}$
satisfies
$$
 \sum_{r'\ge0}\min\{X/Y,Y/X\}\le C_\rho.
 \tag{4.4}
$$
To verify this, divide the sequence at the last index with
$Y\ge X$; on either side the summands are a geometric
sequence with ratio $\rho$. The bound is uniform in the
position of the dividing index, including the case that it
lies before index zero.

Summing (4.3)--(4.4) over the $O(\log\beta)$ positive
intervals with $X\ge1$ costs $O(\log\beta)$. The remaining
pairs with $Y\ge1$ have the same bound after reversing the
roles. Finally, for $X<1,Y<1$, the first bound in (4.3) gives
$$
 \sum_{X<1}\sum_{Y<1}C_\rho XY=O(1),
 \tag{4.5}
$$
again by geometric series. Thus all opposite-side interactions
are $O(\log\beta)$.

Equation (2.7) excludes the opposite-side terms with $r=r'$.
For the upper bound just proved we included these as well;
all terms are nonnegative, so doing so is harmless. The
adjacent same-side terms in (3.8) are all present in (2.7).
Combining the resulting lower and upper bounds proves (1.7).

## 5. A full determinant bound, including all orders

Put $G=G_\beta$, $D=D_\beta$, $X=G-D$, and
$$
 G_u=D+uX,\qquad 0\le u\le1.
$$
Each $G_u$ is a positive trace-class contraction, by convexity.
For fixed $0<t<1$, the real function
$$
 F(u)=\log\det(I-tG_u)
$$
is twice differentiable. This follows directly by differentiating
the absolutely convergent trace series
$$
 \log\det(I-tG_u)
 =-\sum_{j\ge1}\frac{t^j}{j}\operatorname{Tr}(G_u^j).
$$
For example, a differentiated term is bounded in trace norm
using the single trace-class factor $X$, while all the
remaining operator factors have norm at most one. The factors
$j$ or $j^2$ caused by differentiation are dominated by the
geometric powers $t^j$. With
$$
 R_u=(I-tG_u)^{-1}
$$
the derivatives are therefore
$$
 \begin{aligned}
 F'(u)&=-t\operatorname{Tr}(R_uX),\\
 F''(u)&=-t^2\operatorname{Tr}(R_uXR_uX)
        =-t^2\|R_u^{1/2}XR_u^{1/2}\|_{\rm HS}^2.
 \end{aligned}
 \tag{5.1}
$$

The inverse $R_0=(I-tD)^{-1}$ is block diagonal in the
shell decomposition, whereas $E_rXE_r=0$ for every $r$.
Consequently $F'(0)=0$. For a trace-class justification with
infinitely many blocks, compress $R_0X$ onto the finite sum
$\sum_{r=0}^M E_r$. Its trace is zero. Those compressions
converge to $R_0X$ in trace norm, since the projections tend
strongly to the identity on $L^2(J_S)$.

The spectral bounds on $G_u$ imply
$$
 I\le R_u\le(1-t)^{-1}I.
$$
It follows that
$$
 \|X\|_{\rm HS}
 \le\|R_u^{1/2}XR_u^{1/2}\|_{\rm HS}
 \le(1-t)^{-1}\|X\|_{\rm HS}.
 \tag{5.2}
$$
The left inequality does not require $X\ge0$: recover $X$
by multiplying the middle operator on both sides by
$R_u^{-1/2}$, whose operator norm is at most one.

Since $F'(0)=0$,
$$
 F(1)-F(0)=\int_0^1(1-u)F''(u)\,du.
 \tag{5.3}
$$
Equations (5.1)--(5.3), together with
$\|X\|_{\rm HS}^2=\Delta_\beta$, prove (1.8).

The determinant of $I-tD$ is the product of its block
determinants. The logarithms converge absolutely because
$$
 0\le-\log\det(I-tE_rGE_r)
 \le\frac{t}{1-t}\operatorname{Tr}(E_rGE_r),
$$
and the traces sum to $L_\beta$. This proves (1.9).

Finally, for a positive trace-class operator $T$,
$$
 e_2(T)=\frac12\big((\operatorname{Tr}T)^2-\operatorname{Tr}T^2\big).
$$
The common trace in (1.6) therefore proves (1.10).

## 6. The frequent-marker scale

For any fixed integer offset $R_0$, let
$$
 R_N=\left\lceil\frac{\log\log N}{2\log\Lambda}\right\rceil+R_0,
 \qquad \beta_N=\chi N\rho^{2R_N},
 \tag{6.1}
$$
where $\chi>0$ is the fixed actual endpoint area factor.
For all sufficiently large $N$, $R_N\ge0$, and
$\beta_N$ is bounded above and below by fixed positive
multiples of $N/\log N$. Hence (1.7) gives
$$
 \boxed{
 \Delta_{\beta_N}
 =\frac{(\log(N/\log N))^2}{\pi^2\log\Lambda}
      +O(\log N).}
 \tag{6.2}
$$
There is no subsequence restriction and no limiting phase
parameter in this formula. The rounding in (6.1) changes
$\log\beta_N$ by a bounded amount and is included in the
displayed remainder.

The exact common trace is of order $N/\log N$. In
particular,
$$
 \frac{\Delta_{\beta_N}}{\operatorname{Tr}G_{\beta_N}}\to0,
 \qquad
 \Delta_{\beta_N}\to\infty.
 \tag{6.3}
$$
Thus small relative loss of the second trace does not justify
replacing the full operator by its independent-shell Gram
when estimating connected determinant coefficients. The
second coefficient changes by $-\Delta_{\beta_N}/2$;
the logarithm of the determinant ratio at fixed $t$ changes
by order $(\log N)^2$.

This result supplies the exact full-shell endpoint operator
and quantifies a specific incorrect simplification of it.
It does not say that every coherent variable-run expansion
must fail. Equation (2.1) is already a valid coherent
reconstruction if its full phases and all cross blocks are
retained.

There is a separate uniformity issue. The periodic-orbit
endpoint approximation in the signed-profile input was
proved with $N\rho^{2R}$ in a fixed compact interval.
It has not been proved uniformly at the frequent-marker
scale (6.1), where that parameter tends to infinity.
For example, a cubic endpoint remainder bounded by
$N\rho^{3R}$ is small at the critical scale but its bound
grows like $N/(\log N)^{3/2}$ at (6.1). This observation
does not assert that the actual remainder has that size;
it shows why the previous bound cannot justify the new
substitution. The operator theorem here is exact, and
does not make that substitution. Transferring it to a
periodic trace approximation in the frequent regime
requires a new uniform error estimate.

It also does not count distinct periodic orbits. An
independent pair of incoming and outgoing shell indices can
describe a different cut within the same zero run. Nothing
in (2.1) inserts those cuts as distinct terms in an orbit
pair sum.

## 7. The remaining phase and one exact unproved estimate

For a cell $e$, the signed-profile input defines the
boundary action with its exact deck term by
$$
 W_e(q_{\rm out},q_{\rm in})
 =\operatorname*{crit}_{q_1,\ldots,q_{d-1}}
       \sum_jF(q_{j+1},q_j)-(n_e)_p q_{\rm out}.
 \tag{7.1}
$$
When the same collection of cells is reconnected, the sum
of their constants $W_e(q_*,q_*)$ cancels in an action
difference. The remaining endpoint phases are precisely
the type represented by the Fourier kernel in (1.3).

When different interior collections are paired, the
remaining phase includes instead
$$
 \exp\left\{2\pi iN
 \left[
   \sum_{e\in\mathcal C}W_e(q_*,q_*)
  -\sum_{e'\in\mathcal C'}W_{e'}(q_*,q_*)
 \right]\right\}.
 \tag{7.2}
$$
The full-shell identity (2.1) does not sum (7.2). Its kernel
has no label for either interior collection. In particular,
recovering a sine compression for the endpoint operator
does not identify the eigenphase statistics of $U_N$.

For a completely explicit remaining target, let
$$
 \phi(\xi)=
 \begin{cases}
  \exp[-1/(1-\xi^2)],&|\xi|<1,\\
  0,&|\xi|\ge1,
 \end{cases}
 \qquad c_\phi=\int_{\mathbb R}\phi(\xi)\,d\xi,
 \qquad g=\mathcal F^{-1}\phi,
$$
and put
$$
 b_*(x)=\frac{|g(x)|^2}{2c_\phi^2}.
 \tag{7.3}
$$
This is a fixed admissible test in the original problem:
it is nonnegative and Schwartz,
$\sup b_*\le1/2<1$, and
$$
 \widehat b_*=\frac{\phi*\phi}{2c_\phi^2}
       \in C_c^\infty([-2,2]).
 \tag{7.4}
$$
Here $\phi$ is real and even, so the reflected conjugate in
the Fourier transform of $|g|^2$ is again $\phi$.

Writing $p_{m,N}=\operatorname{Tr}(U_N^m)$, the exact
finite-dimensional $k=2$ formula gives
$$
 \boxed{
 \Delta_{2,N}(b_*)
 =\frac1{N^2}\sum_{m=1}^{2N}
     |\widehat b_*(m/N)|^2
       \bigl(|p_{m,N}|^2-\min(m,N)\bigr).
 }
 \tag{7.5}
$$
Indeed the diagonal exclusion subtracts $N$ for both the
given matrix and CUE, and the zero Fourier mode agrees
exactly. The nonzero CUE trace moment is
$\mathbb E|\operatorname{Tr}V_N^m|^2=\min(m,N)$.
For completeness, this last identity follows from the CUE
two-point kernel: its squared modulus has Fourier
coefficient $(N-m)_+$ at positive integer $m$, giving
$N-(N-m)_+$ after adding the diagonal term.

No proof that (7.5) tends to zero, and no fixed positive
lower bound for its modulus on an infinite subsequence,
has been obtained here. This is the first unresolved
original spectral estimate in this last branch. The new
calculation proves that summing scalar renewal masses and
then discarding the cross-shell blocks cannot supply it;
retaining all those blocks recovers the endpoint operator
but still leaves the different-interior actions (7.2).

The result of this attempt is therefore the fully proved
coherence asymptotic (1.7), its all-orders determinant
bounds (1.8), and the explicit failure of an independent-shell
coefficient replacement (1.10). The original $H_{\rm diag}$
remains open in this analysis.

