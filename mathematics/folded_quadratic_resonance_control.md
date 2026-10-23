# Resonant cubic control by the folded square of the density

**Claim ID:** `BGS-TRACE-012`. **Status:** elementary project proof,
author self-review and finite controls. Work dated 1 October 2026,
without subagents; no external referee, formal analytic certificate,
priority claim or solution of BGS. The actual frozen-map asymptotic
inputs identified in Section 7 remain open. Final author audit:
4 October 2026; the common scalar phase convention is explicit below.

This refines [TRACE-011](resonant_cubic_density_control.md), rather than
replacing its critical-tail counterexample. The prior
[folded-spectrum control](../supplement/fixed_map/report-audit/folded_spectrum_control.md)
already shows that bounded local counts and short traces do not imply
small resonant pair mass. The new object here is the arithmetic projection
of the **square** of the microscopic density. It retains information about
which roots of the block eigenvalues occur in the original spectrum.

## 1. Statements and the exact factorial budget

Use the notation of TRACE-011: an arbitrary unitary of dimension N has
phases $x_j\in\mathbb T$ and $T_m=\sum_j e^{2\pi i m x_j}$; fix
$0<a<b$, $2b<1$, $I_N=[aN,bN]\cap\mathbb Z$ and
$J_N=[aN,2bN]\cap\mathbb Z$. For a positive integer d put

$$
E=N^{-2}\sum_{j\in J_N,\ d\mid j}|T_j|^2,\qquad
Q=N^{-2}\sum_{j\in J_N}|T_j|^2.
$$

Let $\eta(u)=\sqrt\pi e^{-\pi^2u^2}$ and define

$$
\rho(x)=\sum_j\sum_{v\in\mathbb Z}\eta(N(x+x_j+v)),\qquad
P_df(x)=d^{-1}\sum_{h=0}^{d-1}f(x+h/d),\qquad
G_d=\|P_d(\rho^2)\|_2^2.                              \tag{1}
$$

All circle integrals use normalized Lebesgue measure. In particular
$\int\rho=1$. For $W\in C_c^\infty((a,b)^2)$ set

$$
Z(W)=N^{-3}\sum_{\substack{m,n\in I_N\\
d\mid m\text{ or }d\mid n\text{ or }d\mid(m+n)}}
W(m/N,n/N)T_mT_n\overline{T_{m+n}}.
$$

**Theorem 1.** There is a constant depending only on W and its fixed
support such that, for every N, d and spectrum,

$$
\boxed{|Z(W)|\le C_W\sqrt{E G_d}.}                    \tag{2}
$$

The modulus is outside the entire signed sum. Moreover,

$$
1\le\|\rho\|_2^4\le G_d\le\|\rho\|_4^4,\qquad
Q\le e^{8b^2}\sqrt{G_d}.                              \tag{3}
$$

For the full factorial discrepancy write $A_m=|T_m|^2$,
$D_3=T_mT_n\overline{T_{m+n}}-A_m-A_n-A_{m+n}+2N$,
$\Delta_3=D_3-2(N-m-n)$, and let Y be the same sector sum
with $\Delta_3$ in place of the triple trace. With
$\ell=|I_N|/N$, the already proved exact budget remains

$$
|Y-Z|\le\|W\|_\infty\left[3\ell E+
6(\ell/d+1/N)Q+12b\ell(\ell/d+1/N)\right].             \tag{4}
$$

Thus $EG_d\to0$, $d\to\infty$ and
$(1/d+1/N)Q\to0$ delete the factorial sector. A condition involving
only the new density statistic is

$$
EG_d\to0,\qquad (1/d+1/N)\sqrt{G_d}\to0.              \tag{5}
$$

Indeed (3) makes E tend to zero and supplies (4). For prime cat orders,
$d\le N+1$, a simpler sufficient version is $EG_d\to0$ and
$G_d=o(d^2)$. These are sufficient conditions, not necessary conditions
for signed comparison. The improvement over $EM_4\to0$ is strict;
Section 4 gives a realizable example.

## 2. Proof by projection of a product

For $w\in C_c^\infty(\mathbb R)$ let
$F_w=N^{-1}\sum_m w(m/N)T_me^{2\pi i mx}$. As in TRACE-011,
$F_w=K_w*\rho$, where K_w is the periodization at scale N
of the inverse Fourier transform of $w(\xi)e^{\xi^2}$.
Its L1 norm is bounded by a constant $c_w$ independent of N.
If it vanishes, the relevant integral vanishes. Otherwise put
$\nu_w=|K_w|/\|K_w\|_1$, a probability kernel. Positivity and
Cauchy--Schwarz give

$$
|F_w|\le c_w\nu_w*\rho,\qquad
|F_w|^2\le c_w^2\nu_w*(\rho^2).                        \tag{6}
$$

Consequently

$$
|F_uF_v|\le\frac{c_uc_v}{2}
\left[\nu_u*(\rho^2)+\nu_v*(\rho^2)\right],
\quad\|P_d(F_uF_v)\|_2\le c_uc_v\sqrt{G_d}.            \tag{7}
$$

Here $P_d$ is positive, commutes with convolution, and probability
convolution contracts L2. If one or both F factors in the product are
already projected, replace the corresponding probability kernel by
$P_d\nu_w$ and use $(P_d\rho)^2\le P_d(\rho^2)$.
In particular,

$$
\|(P_dF_u)(P_dF_v)\|_2\le c_uc_v\sqrt{G_d}.            \tag{8}
$$

For a separable Fourier weight use three filters supported in $J_N/N$.
The first strip equals $\int(P_dF_1)F_2\overline{F_3}$.
Self-adjointness of $P_d$ moves it onto $F_2\overline{F_3}$.
Equations (7) and Parseval bound this integral by
$\|w_1\|_\infty c_2c_3\sqrt{EG_d}$. The second strip is identical
with 1 and 2 exchanged. The sum strip uses
$\int P_d(F_1F_2)\overline{P_dF_3}$ and has the same type of bound.

Any two divisibility conditions force the third. The union indicator
is therefore the sum of the three single-strip indicators minus twice
their common intersection. The latter integral is
$\int(P_dF_1)(P_dF_2)\overline{P_dF_3}$, controlled by (8).
No noncommuting quantum operators have been rearranged in this proof.

For general W choose smooth compact cutoffs $w_1,w_2$ equal to one
on its coordinate supports and $w_3$ equal to one on their sum support,
all inside the appropriate bands. Fourier inversion expresses W as
an L1 superposition of the first two cutoffs multiplied by
$e^{2\pi it\xi}$ and $e^{2\pi is\xi}$. These modulations translate
K_w and preserve its L1 bound. Integrating the preceding uniform
estimates against $|\widehat W(t,s)|$ proves (2).

Finally $P_d$ is an orthogonal projection on L2 and an averaging
operator. Its contraction and its preservation of the mean give
$G_d\le\int\rho^4$ and $G_d\ge(\int\rho^2)^2\ge1$.
Since $\widehat\rho(m)=e^{-(m/N)^2}T_m/N$, Parseval gives
$Q\le e^{8b^2}\|\rho\|_2^2\le e^{8b^2}\sqrt{G_d}$.
Equation (4) is precisely TRACE-011, equation (6), with unchanged
normalization and finite CUE counterterm. This proves the assertions.

## 3. Exact block interpretation and root allocation

In this section take $C=U^d$, with phases $y_j=dx_j\pmod1$.
If the maintained block is $\zeta^{-1}U^d$, first rotate all original
phases by a d-th-root phase of $\zeta^{-1}$. This translates rho and
leaves E, Q and G_d unchanged; the formulas then apply exactly to that
block and the rotated phases. Put R=N/d and

$$
f_{C,R}(u)=\frac1d\sum_j\sum_{v\in\mathbb Z}
\eta(R(u+y_j+v)).
$$

The factor $1/d=R/N$ makes its integral one. Direct reindexing gives
$P_d\rho(x)=f_{C,R}(dx)$. Set $g_h(u)=\rho((u+h)/d)$ and

$$
B_d(u)=\frac{d\sum_hg_h(u)^2}{(\sum_hg_h(u))^2}.
$$

The Gaussian is strictly positive, so this ratio is defined everywhere.
Cauchy--Schwarz and positivity give $1\le B_d\le d$; in fact

$$
\boxed{G_d=\int_{\mathbb T}B_d(u)^2 f_{C,R}(u)^4\,du.} \tag{9}
$$

The block spectrum determines f, but it generally does not determine
B: assigning a d-th root to each block eigenvalue changes the original
spectrum while leaving C fixed. Thus $\|f\|_4^4\le G_d\le d^2\|f\|_4^4$;
discarding B in (2) is unjustified.

For a sharp illustration assume d divides N and N/d tends to infinity.
Both the spectrum with all N phases zero and the spectrum with N/d
copies of each point of a d-clock have $C=I$. Gaussian separation gives

$$
G_d^{\rm concentrated}\sim c_4N^3/d,\qquad
G_d^{\rm balanced}\sim c_4N^3/d^3,\qquad
c_4=\int\eta^4=\pi^{3/2}/2.                            \tag{10}
$$

Their ratio is asymptotic to $d^2$. This example refutes an estimate
of the folded-square statistic by the block fourth density with a
constant independent of d. It is not a small-E example.

Two further exact representations are

$$
G_d=\frac1d\sum_{h=0}^{d-1}\int\rho(x)^2\rho(x+h/d)^2dx
=\sum_{r\in\mathbb Z}|\widehat{\rho^2}(rd)|^2.          \tag{11}
$$

They follow from self-adjointness/Parseval. This is a positive
four-point quantity with shifted pair centers, rather than a single
trace or an assumption of independent eigenphases.
An explicit trace form, with absolutely convergent Gaussian sums, is

$$
G_d=N^{-4}\sum_{r\in\mathbb Z}\left|
\sum_{m\in\mathbb Z}e^{-[(m/N)^2+((rd-m)/N)^2]}
T_mT_{rd-m}\right|^2.                                 \tag{11a}
$$

In particular this exposes the required fourth joint-trace energy;
no pointwise CUE prediction for any one resonant mode is inserted.

## 4. A strict improvement over the global fourth moment

Let integer L tend to infinity and put $N=L^4$, $d=L^3$, $K=L^2$.
Take the union of an $(N-K)$-clock with K phases at zero. For every
positive $m<N-K$, $T_m=K$. In the fixed band $J_N$ this gives

$$
E\sim(2b-a)L^{-3},\qquad Q\longrightarrow2b-a,
M_4\ge K^4/N=L^4.                                    \tag{12}
$$

In particular $EM_4$ diverges at least linearly in L. Nevertheless

$$
G_d=O(L),\qquad EG_d=O(L^{-2}),\qquad Y(W)\to0.         \tag{13}
$$

Here is a uniform proof of the density bound, including Gaussian tails.
Put $k_N(x)=\sum_v\eta(N(x+v))$. The clock contribution to rho is
bounded by an absolute constant because its scaled spacing is N/(N-K)>1.
Hence $\rho\le C+Kk_N$ and
$P_d(\rho^2)\le2C^2+2K^2P_d(k_N^2)$.
For $a=1,2$ Gaussian decay and completing the square give

$$
\int k_N(x)^a k_N(x+t)^a dx
\le\frac{C_a}{N}\exp[-c_aN^2\operatorname{dist}(t,\mathbb Z)^2].
$$

This also follows by domination by a periodized Gaussian; the Gaussian
image tails are uniformly summable. Therefore, when $d\le N$,

$$
\|P_d(k_N^2)\|_2^2\le\frac{C}{Nd}
\sum_{h=0}^{d-1}e^{-c(N/d)^2\min(h,d-h)^2}
\le\frac{C'}{Nd}.
$$

It follows that $G_d\le C(1+K^4/(Nd))=O(L)$.
The bound (4) proves the factorial conclusion. Direct counting also
gives $Z=O(K^3/(Nd))=O(1/L)$ for bounded W.

The example can be made simple: perturb every phase by less than
$N^{-9}$, splitting coincident labels and retaining the other gaps.
The trace changes at times O(N) are $O(N^{-7})$; the uniform change
of rho is $O(N^{-7})$ since $\|k_N'\|_\infty=O(N)$ and there are N
phases. Since $\|\rho\|_\infty=O(N)$, the change of G_d is o(1).
The K clustered phases meet at most two microscopic bins, so their
fourth occupancy contribution is still at least $K^4/(8N)$.
Thus the separation of criteria persists. For odd L the dimensions
are odd. No claim is made that this spectrum satisfies the CUE pair law
or comes from the frozen map.

## 5. Crowding of the block forces microscopic factorial mass

This obstruction does not need root-allocation information. For a fixed
integer $r\ge2$ define the positive anchored factorial measure

$$
\mu_{N,r}=\frac1N\sum_{j_1,\ldots,j_r\ {\mathrm{distinct}}}
\sum_{v\in\mathbb Z^{r-1}}
\delta_{\left(N(x_{j_a}-x_{j_r}+v_a)\right)_{a<r}}.
$$

**Theorem 2.** If K eigenvalues of C lie in an arc of turn-coordinate
length $\varepsilon d/N<1$, then

$$
\mu_{N,r}([-\varepsilon,\varepsilon]^{r-1})
\ge\frac{(d-s)(t)_r+s(t+1)_r}{N}
\ge\frac{(K-(r-1)d)_+^r}{Nd^{r-1}},                  \tag{14}
$$

where $K=dt+s$, $0\le s<d$, and $(k)_r=k(k-1)\cdots(k-r+1)$,
with value zero for nonnegative integers $k<r$.

The arc lifts to d disjoint original arcs of length $\varepsilon/N$.
Assign the K labels to them, with counts $k_h$. Every ordered distinct
r-tuple in one such arc gives relative coordinates in the displayed
cube, after consistent integer lifts, even if the arc crosses zero.
The resulting lower count is $N^{-1}\sum_h(k_h)_r$.
The discrete second difference of $(k)_r$ is
$r(r-1)(k)_{r-2}\ge0$. Pairwise balancing minimizes the sum at
counts t and t+1, proving the first inequality. For the second use
$(k)_r\ge(k-r+1)_+^r$ and Jensen. Background levels or cross-arc
tuples only increase this positive statistic.

Suppose now $d=o(N)$, $\varepsilon_N\to0$, and along a subsequence

$$
K\ge c(Nd^{r-1})^{1/r},\qquad c>0.                    \tag{15}
$$

Equation (14) gives shrinking-cube factorial mass with liminf at least
$c^r$. Consequently these factorial measures cannot converge against
all compact smooth tests to the Sine_2 r-point measure, whose density
is continuous and has no atom at the origin. To see the contradiction
without exchanging moving tests, take a fixed nonnegative smooth cutoff
equal to one in a small neighborhood of zero; then decrease that fixed
neighborhood after taking the lower limit. This is a factorial-correlation
obstruction. It alone does not refute weak convergence of local point
processes without uniform integrability.

For r=3 the threshold is $N^{1/3}d^{2/3}$, smaller than the pair threshold
$\sqrt{Nd}$ when $d=o(N)$. The balanced clusters from TRACE-011 attain
this cubic scale with vanishing pair contribution. They therefore remain
a sharp warning: proving E->0 does not settle cubic comparison.

## 6. Elementary Sine_2 reference estimate

For completeness a direct bound makes the reference mass quantitative:

$$
\int_{[-\varepsilon,\varepsilon]^2}
\det[K(x_i-x_j)]_{i,j=0}^2\,du\,dv
\le\frac{3\pi^6}{5}\varepsilon^8,
\quad(x_0,x_1,x_2)=(0,u,v),\quad
K(z)=\frac{\sin\pi z}{\pi z}.                          \tag{16}
$$

Indeed K is the Gram kernel of $e^{2\pi ixt}$ on $[-1/2,1/2]$.
Expanding both determinants and integrating proves the identity
$\det[K(x_i-x_j)]=(3!)^{-1}\int|\det[e^{2\pi ix_it_j}]|^2dt$.
Newton divided differences factor the latter determinant as
$uv(v-u)$ times a determinant whose rows have norms at most
$\sqrt3$, $\sqrt3\pi$, $\sqrt3\pi^2/2$.
The divided-difference bounds follow by the simplex integral formula
and $|\partial_x^j e^{2\pi ixt}|\le\pi^j$, including complex values.
Hadamard gives density at most $(9/8)\pi^6u^2v^2(u-v)^2$.
Its cube integral is $8\varepsilon^8/15$, proving (16).
Repeated arguments follow by continuity. The same bound holds for the
**finite CUE_N expectation** of the anchored measure: its normalized
kernel is the Gram kernel for the probability measure with equal atoms
at $(j-(N-1)/2)/N$, $0\le j<N$. All frequencies have modulus at most
1/2, so the identical divided-difference proof applies. Normalization
agrees with the factor 1/N in the definition of $\mu_{N,3}$ after
integrating the anchor and changing the other coordinates by N.
This is not an optimal constant. The checked leading Sine_2 density is
$\pi^6u^2v^2(u-v)^2/135$; the global argument needs only the larger
proved constant.

## 7. Actual frozen-map scope and failed dynamical shortcuts

Keep $U_p=e^{i\tau pA_p}M_p$, $\tau=10^{-80}$ and the ordered block
$C_{p,d}=\prod_{j=0}^{d-1}e^{i\tau pM_p^jA_pM_p^{-j}}$ in increasing j.
TRACE-009 proves $U_p^d=\zeta_pC_{p,d}$ and identifies its resonant E.
Theorem 1 deletes this map's resonant factorial cubic if (5), or the
weaker E/G/Q conditions after (4), are proved for its actual spectrum.
Theorem 2 identifies an alternative concrete obstruction to look for.
Neither asymptotic input has been established.

There is a certified finite coherence application. With $B_p=A_p+I/10$
the frozen symbol satisfies $\|B_p\|\le26/25$. To check the bound put
$u=1-\cos14\pi q\in[0,2]$: its diagonal is
$1-u[1-(1+\cos2\pi q)(1/10+\sin2\pi q/100)]\in[-1,1]$.
Each of the two off-diagonal moduli is at most $4/200$.
The row-sum bound proves the assertion. After the harmless common phase
shift, the block differs from I in operator norm by at most
$\delta=(26/25)|\tau|pd$ by telescoping. If $\delta<2$ its eigenphases
fit in a closed arc of turn length at most
$2\arcsin(\delta/2)/\pi\le\delta/2$.
Thus (14) applies with all K=p and

$$
\varepsilon=(13/25)|\tau|p^2.                         \tag{17}
$$

For example 239 is prime, $d_{239}=7$ because
$S^7=\left(\begin{smallmatrix}114243&161564\\80782&114243\end{smallmatrix}\right)
\equiv I\pmod{239}$ and S is not the identity. For r=3,
the exact balanced count is $254694/239$; the simpler lower bound is
$11390625/11711$. Equation (17) gives
$\varepsilon=742573/(25\cdot10^{80})<3\cdot10^{-76}$.
The finite CUE_239 expected mass in that cube is less than $10^{-600}$
by (16), whereas the actual factorial mass is at least $254694/239$.
This statement concerns the analytically certified actual kick, not a
floating point kick rounded to I. It is a finite-dimensional comparison;
fixed tau does not make tau*p^2 small along unbounded primes. Previous
finite-coherence and Pell controls are credited, not rediscovered as a
BGS counterexample.

The following possible shortcuts were rejected in this pass:

- Collapsing the ordered product to the exponential of its orbit average
  drops noncommutative terms. The available telescoping error grows on
  the fixed-tau Heisenberg scale; it cannot prove E=o(1).
- The block density alone discards B_d, with a demonstrable d^2 loss.
  A bound on that density does not automatically prove (5).
- Short-time mixing, positive gaps and bounded local counts do not force
  E=o(1), as the prior folded-spectrum countercontrol proves.
- The seven-cut approximation retains M_p; it is not a direct sum of
  independent propagators, and it supplies no branch-balance estimate.
- Scalar-power exclusion and trace nonvanishing give no upper estimate
  on E or on the shifted four-point energy (11).

There is also a quantitative obstruction to using a fixed Taylor degree
of the ordered product as a Heisenberg certificate. For a product with
m conjugate kicks, $t=\tau N$ and $\|B_N\|\le26/25$, the unitary
time-ordered Duhamel expansion through degree L has norm remainder at
most $H^{L+1}/(L+1)!$, where $H=(26/25)|\tau|Nm$. This follows by
iterating the Volterra equation and retaining the last exact unitary
factor in the remainder. At $m\asymp N$, H grows as $|\tau|N^2$.
The available fixed-degree certificate therefore does not decay;
obtaining a small error from this certificate requires a degree growing
with H. Existing fixed-degree orbit/energy identities do not control
that many ordered words. This is a limitation of this certificate,
not a proof that every possible nonperturbative method must use it.

The next load-bearing work is a dynamical estimate of E and of the
shifted energy (11), or a cancellation argument avoiding that sufficient
energy condition. Root allocation must remain explicit if only the
block spectrum is analyzed. Nonresonant signed cancellation, other
cones, composite dimensions and higher factorial orders remain separate
open parts of TRACE-005. BGS-BGS-001 remains open.
