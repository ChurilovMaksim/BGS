> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round14_2026_10_21/obstruction/r14_original_spectral_orbit_barrier.md`. Embedded SHA256: `610c0e62b64834687b91db54a1cb5e584a2ad16035e0290c54506ffa6608de7e`.
> [Thematic guide](../../../topics/classical_trace.md).

# Round 14: spectral distance from the bare cat after arbitrary conjugation

Date: 21 October 2026. Branch: /root/r14_original_obstruction.

## 1. Scope, status, and exact ancestry

The original matrices throughout this note are
$$
U_N=\exp(i10^{-80}NA_N)M_N,\qquad N\ge3\ \text{odd}.
$$
The parameter and symbol are unchanged. No averaging over dimensions,
symbols, phases, or kicks is used.

**No counterexample to the original $H_{\rm diag}$ is proved here.**
The new result concerns how closely the complete original spectrum can
resemble the bare cat spectrum after any relabeling and unitary change
of basis. It excludes a particular recurrence mechanism, including on
an infinite sequence whose 7-adic valuations tend to infinity. It does
not give a microscopic pair-correlation limit.

The initial master has SHA-256
ef38464d8e2b6ad3e917547e3437dcd53ed7c28dd39c4818faa29e5eb7cf6d43,
8,162,410 bytes. Exact input hashes and sizes are in input_hashes.json.
The master and other branches were not modified.

Write
$$
\lambda=3+2\sqrt2,\qquad
N_r=\frac{\lambda^r-\lambda^{-r}}{4\sqrt2},\qquad
d_N=\inf_{\substack{W\in U(N)\\|z|=1}}
\|U_N-zWM_NW^*\|_{\rm op}.
\tag{1.1}
$$
The following conclusions are proved.

1. For every sufficiently large original odd dimension,
   $$
   d_N=O(1/\log N).
   \tag{1.2}
   $$
2. Along odd $r\to\infty$,
   $$
   \liminf (\log N_r)d_{N_r}\ge\frac{\pi\log\lambda}{4}>0.
   \tag{1.3}
   $$
   In particular $d_{N_r}$ has order $1/\log N_r$, not order $1/N_r$.
3. If $r_s=3\cdot7^s$, then $N_{r_s}$ is odd and
   $$
   v_7(N_{r_s})=s+1.
   \tag{1.4}
   $$
   Thus (1.3) also holds through arbitrarily deep powers of 7 dividing
   the dimension.
4. Put $m_r=2r$. For any angular radius $0<a<\pi/2$, and every
   rotated $m_r$-clock, the fraction of the eigenvalues of $U_{N_r}$
   lying within angular distance $a/m_r$ of that clock is at most
   $$
   \frac{1+o(1)}{1+\cos a}.
   \tag{1.5}
   $$
   The estimate is uniform over the rotation of the clock. In a
   neighborhood of width $o(1/r)$, the upper bound is
   $1/2+o(1)$.

The estimate imported from older work is explicitly audited next.
All transitions from that estimate to (1.2)--(1.5) are proved here.

## 2. The old physical trace estimate and its raw dependency audit

The required old result is the following statement about the **actual
finite matrices**:
$$
\exists\, C,N_0,\ a_*\in(1,\sqrt\lambda):
\quad
|\operatorname{Tr}U_N^m|\le C a_*^m
\quad(N\ge N_0\ \text{odd},\ m\ge1).
\tag{2.1}
$$
The constants are fixed for the prescribed $\tau=10^{-80}$.
The quantifier over $m$ is simultaneous; no threshold depending on
$m$ is being inserted.

The raw proof of (2.1), rather than merely its label, was checked in
the following files and sections:

| Input | Sections used and checked |
|---|---|
| research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md | §§3--9, through the exact sector action and deck identity |
| research_continuation_2026_10_20/exact_amplitude.md | Entire proof |
| research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md | §§1--9 |
| research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md | §§1--2; its later pair claims are not needed here |
| research_round2_2026_10_20/fermionic_pressure_transfer.md | §§1--8 |

The quantitative pressure file was also inspected, but its numerical
lower bound $\Delta\ge2000\tau^2$ is **not needed or imported** for
the new conclusions. The qualitative strict inequality $\Delta>0$
suffices. This avoids treating additional coding and analytic-pressure
inputs as established merely because their conclusions are quoted.

Here is the exact chain used in the audit.

### 2.1. Exact finite-to-plane identification

Because modular halves differ from ordinary halves at odd $N$, the
ordinary plane symbol is
$$
\begin{split}
a(q,p)={}&\cos(14\pi q)+r(q)/10
+r(q)\sin(2\pi q)/100-1/10\\
&+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
\end{split}
\tag{2.2}
$$
The half-period shift is substantive. The finite matrix is the comb
quotient of the exact plane propagator, up to
$\zeta_N=e_8(3N-1)$, a scalar of modulus one.

The proof in odd_trace_and_algebraic_rigidity.md first expands the
propagator into translated metaplectic words at each fixed $m,N$.
The absolute coefficient mass is finite. Their coherent diagonals
have translation-independent integrable Gaussian bounds. Grouping
integer translations by
$\mathbb Z^2/(L^m-I)\mathbb Z^2$, where
$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
$$
tiles the plane once per class and introduces no additional determinant
factor. Translation-independent bounds for the Gaussian Abel integrals
justify the corresponding path-kernel formula. Thus the input to the
contour calculation is an identity for the actual finite trace.

### 2.2. Exact amplitude and a single all-time threshold

At $t_*=\tau/(2\pi)$, exact_amplitude.md constructs
$$
K_V(Q,q)=\frac{e^{i\pi/4}}{\sqrt{8\pi h}}\,
e^{iF(Q,q)/h}B_h(Q,q),\qquad h=(2\pi N)^{-1}.
\tag{2.3}
$$
This is the exact kernel. The analytic-scale Dyson series for the
amplitude converges at the stated time, uniformly for real $h$.
The bounds for its first two actual $h$-derivatives are uniform on a
fixed spatial strip. Its leading amplitude is
$B_0=2\sqrt{F_{Qq}}$, and its first $h$-coefficient is imaginary on
the real domain.

The bounded contour $u-i\psi(u)$ in the Gaussian file has linear
tails in its decay exponent, which is sufficient. The proof retains a
Gaussian regulator during deformation and removes it by dominated
convergence on the final contour. Its normalized one-edge operators
satisfy, at a single small-$h$ threshold,
$$
\sup_x\|K_h(x)-K_G\|_1\le10^{-4}.
\tag{2.4}
$$
Here $K_G$ has eigenvalues $1,\lambda^{-1},\lambda^{-2},\ldots$.
The global graph contraction on a fixed Hilbert space yields
$$
K_h(x)=\gamma_h(x)v_h(\Psi x)\ell_h(x)+\mathcal B_h(x),
$$
with consecutive mixed products exactly zero and
$$
\|\mathcal B_h(x)\|<0.174,\quad
\|\mathcal B_h(x)\|_1<0.209,\quad
|\gamma_h(x)-1|<0.0002.
\tag{2.5}
$$
The critical points of each path action are unique by its uniformly
negative Hessian. Consequently
$$
\#\operatorname{Fix}\Psi^m
=\lambda^m+\lambda^{-m}-2<\lambda^m.
$$
Summing the full residual therefore gives
$$
p_{m,N}=\zeta_N^m
\sum_{x\in\operatorname{Fix}\Psi^m}
\omega_{m,N}(x)\lambda^{-m/2}\Gamma_h(x,m)+E_{m,N},
\quad |E_{m,N}|\le2(0.421)^m,
\tag{2.6}
$$
where $|\omega_{m,N}(x)|=1$. No estimate in this step imposes
$m=O(\log N)$.

### 2.3. Uniform modulus and the classical pressure gap

The exact real Gaussian cycle calculation, including the discrete Hill
determinant, gives
$$
\lambda^{-m}\Gamma_0(x,m)^2\Lambda_m(x)=1.
$$
The graph scalar is even in $s=\sqrt h$, and its first coefficient in
$h$ is imaginary. The finite Taylor remainder is uniform. Therefore
$$
\left|\log\{\lambda^{-m}|\Gamma_h(x,m)|^2
\Lambda_m(x)\}\right|\le C_{\rm mod}mh^2.
\tag{2.7}
$$
This is precisely the uniform statement needed for (2.1); an
uncontrolled stationary-phase remainder depending on the period would
not suffice.

The classical map $\Psi=\phi_a^{-t_*}\circ L$ is analytic, preserves
area, and has stable and unstable cones with unstable expansion at
least 5. The explicit contraction with the two-sided Green operator
constructs a topological conjugacy with $L$. It gives expansivity,
topological mixing, dense periodic points and entropy $\log\lambda$.

The one published thermodynamic input is Bowen--Ruelle,
*The Ergodic Theory of Axiom A Flows*, Invent. Math. 29 (1975),
181--202, DOI 10.1007/BF01389848:
<https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B42%5D.pdf>.
The author PDF was reopened in this pass. The exact cited results are
Theorem 3.3, Lemmas 4.1--4.2, Proposition 4.4(b), and Remark 5.2.
They supply uniqueness and the lower Gibbs estimate for Hölder
potentials, the volume estimate, zero geometric pressure, and the
identification of the invariant smooth volume. Their basic-set
hypotheses are checked using the smooth constant-roof mapping torus
of $\Psi$. Its whole manifold is a hyperbolic basic attractor; the
vertical flow has no zeros. A mixing suspension is not required.

To explain the strictness without importing a genericity assumption,
the actual point $x_0=(0,0)$ is fixed and
$$
\operatorname{Tr}D\Psi(x_0)
=6+\frac{39212\pi}{125}\tau>6.
\tag{2.8}
$$
This follows from
$D^2a(x_0)=\operatorname{diag}(-19606\pi^2/125,0)$;
the derivative of the kick is exactly a shear there. Thus its
unstable multiplier $\Lambda_0$ exceeds $\lambda$.

Let $\varphi=\log J_\Psi^u$ and
$$
P_*=P_\Psi(-\varphi/2).
$$
On the suspension, the endpoint pressures are $P(0)=\log\lambda$
and $P(1)=0$. If the midpoint pressure were their average, its
equilibrium state would maximize both endpoint functionals, hence would
be both smooth volume and the measure of maximal entropy. At the fixed
orbit, the lower zero-potential Gibbs estimate and the upper volume
estimate would then give
$$
c_\epsilon\lambda^{-m}
\le \operatorname{vol}B_m(x_0,\epsilon)
\le C_\epsilon\Lambda_0^{-m}
\quad\text{for every }m,
$$
contradicting $\Lambda_0>\lambda$. Therefore
$$
\Delta:=\tfrac12\log\lambda-P_*>0.
\tag{2.9}
$$
The same variational formula and expansion at least 5 give $P_*>0$.

Distinct $m$-periodic points are separated at a fixed expansivity
scale, so the separated-set definition of pressure gives, for each
fixed $\eta>0$,
$$
\sum_{\operatorname{Fix}\Psi^m}\Lambda_m(x)^{-1/2}
\le C_\eta e^{(P_*+\eta)m}.
\tag{2.10}
$$
Take square roots in (2.7), insert (2.10) into (2.6), and choose one
threshold $N_\eta$ with $C_{\rm mod}h^2/2\le\eta/2$. This proves
$$
|p_{m,N}|\le C_\eta e^{(P_*+\eta)m}+2(0.421)^m
\quad\text{simultaneously for all }m.
$$
Taking $\eta=\Delta/2$ and absorbing the decaying term proves (2.1),
with
$$
a_*=\sqrt\lambda e^{-\Delta/2}<\sqrt\lambda.
\tag{2.11}
$$
This audit uses the old proof for its actual fixed parameter, and does
not manufacture a Heisenberg-time cancellation estimate from pressure.

## 3. Elementary Pell identities and the actual short-time suppression

Put
$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix}=3I+2J,\qquad
J=\begin{pmatrix}0&2\\1&0\end{pmatrix},\quad J^2=2I.
$$
Then
$$
S^r=t_rI+2N_rJ,\qquad t_r^2-8N_r^2=1.
\tag{3.1}
$$
For example this follows by diagonalizing $J$, or inductively by
multiplication. The recurrence
$$
N_0=0,\quad N_1=1,\quad N_{r+1}=6N_r-N_{r-1}
\tag{3.2}
$$
proves that $N_r$ is integral and has parity $r$. Thus every odd
$r\ge3$ supplies an allowed dimension, and
$$
\log N_r=r\log\lambda-\log(4\sqrt2)+o(1).
\tag{3.3}
$$
Modulo $N_r$, equation (3.1) implies $S^{2r}=I$.

The finite Egorov identity in the conventions of the question is
$$
M_NT_N(a,b)M_N^{-1}
=T_N(3a+4b,\,2a+3b).
\tag{3.4}
$$
It is checked by comparing the kernels of $MT(a,b)$ and
$T(a',b')M$. The coefficients of $x,y$ give
$a'=3a+4b,\ b'=2a+3b$; the constant coefficients both equal
$-3a^2/8-ab/2$ modulo $N$. All fractions are modular.

Therefore $M_{N_r}^{2r}$ commutes with every finite Weyl operator.
Commuting with diagonal characters forces a matrix to be diagonal,
and commuting with the cyclic shift makes its diagonal constant.
Hence
$$
M_{N_r}^{2r}=\gamma_r I,\qquad|\gamma_r|=1.
\tag{3.5}
$$

Applying (2.1) to the **perturbed** matrices and putting
$\delta_*=\Delta/\log\lambda>0$ gives
$$
A_r:=\frac{|\operatorname{Tr}U_{N_r}^{2r}|}{N_r}
\le C\frac{\lambda^r e^{-\Delta r}}{N_r}
=O(N_r^{-\delta_*})\longrightarrow0.
\tag{3.6}
$$
The equality $\lambda^r=4\sqrt2 N_r+\lambda^{-r}$ proves the last
estimate. This is the old physical short-Pell suppression, now used
without restricting a conjugating matrix.

## 4. A quantitative geometric lemma for arbitrary conjugation

### Lemma 4.1

Let $U,V$ be $N$-dimensional unitaries, $V^m=\omega I$, and
$$
A=|\operatorname{Tr}U^m|/N,\qquad0\le A\le1.
$$
Then
$$
\|U-V\|_{\rm op}\ge
2\sin\left(\frac{\arccos A}{2m}\right).
\tag{4.1}
$$
Also
$$
\frac{\|U-V\|_{\rm HS}}{\sqrt N}
\ge\frac{\sqrt{2-2A}}m.
\tag{4.2}
$$

**Proof.** Write $d=\|U-V\|_{\rm op}$. If $d=2$, (4.1) is
immediate. Otherwise put $\eta=2\arcsin(d/2)$. For an eigenvalue
$u$ of $U$, choose a unit eigenvector $v$. Normality of $V$
gives
$$
\operatorname{dist}(u,\operatorname{spec}V)
\le\|(V-u)v\|=\|(V-U)v\|\le d.
$$
Consequently $u$ has angular distance at most $\eta$ from some
eigenvalue of $V$. Each eigenvalue of $V$ has $m$-th power
$\omega$.

If $m\eta\ge\pi/2$, then $m\eta\ge\arccos A$. If
$m\eta<\pi/2$, all eigenvalues $u^m$ of $U^m$, after rotation by
$\overline\omega$, have arguments of absolute value at most
$m\eta$. Thus
$$
A\ge\operatorname{Re}
\{\overline\omega\,\operatorname{Tr}U^m/N\}
\ge\cos(m\eta),
$$
which again gives $m\eta\ge\arccos A$. Solving for $d$ proves
(4.1). No eigenvalue-matching theorem is needed.

For (4.2), expand the Hilbert--Schmidt norm:
$$
\|U^m-\omega I\|_{\rm HS}^2
=2N-2\operatorname{Re}(\overline\omega\operatorname{Tr}U^m)
\ge N(2-2A).
$$
The exact telescoping identity
$$
U^m-V^m=\sum_{j=0}^{m-1}U^{m-1-j}(U-V)V^j
$$
and unitary invariance of the Hilbert--Schmidt norm give
$\|U^m-V^m\|_{\rm HS}\le m\|U-V\|_{\rm HS}$.
This proves (4.2). $\square$

Apply the lemma with
$V=zWM_{N_r}W^*$ and $m=2r$. Its $m$-th power is a scalar
for every $z,W$, so
$$
d_{N_r}\ge2\sin\left(\frac{\arccos A_r}{4r}\right)
=\frac{\pi}{4r}+o(r^{-1}).
\tag{4.3}
$$
Equations (3.3) and (3.6) prove (1.3). Likewise
$$
\inf_{W,z}
\frac{\|U_{N_r}-zWM_{N_r}W^*\|_{\rm HS}}{\sqrt{N_r}}
\ge\frac{\sqrt2+o(1)}{2r}.
\tag{4.4}
$$
These estimates concern the complete spectrum, even though the
conjugating matrix is entirely unrestricted.

### Lemma 4.2: a positive fraction cannot follow the bare clock

For a unitary $U$, a positive integer $m$, and $|\omega|=1$,
let $F(a)$ be the fraction of its eigenvalues $u$ such that
$$
|\operatorname{Arg}(\overline\omega u^m)|\le a,
\quad 0<a<\pi.
$$
For $A=|\operatorname{Tr}U^m|/N$,
$$
F(a)\le\frac{1+A}{1+\cos a}.
\tag{4.5}
$$
Indeed, the real part of each term inside that arc is at least
$\cos a$, and outside it is at least $-1$. Hence
$$
A\ge \operatorname{Re}
\{\overline\omega\,\operatorname{Tr}U^m/N\}
\ge F(a)\cos a-(1-F(a)).
$$
Rearrangement proves (4.5), uniformly in $\omega$.

The set in this lemma is exactly the union of $m$ arcs of angular
radius $a/m$ about the $m$-th roots of $\omega$.
Equations (3.6) and (4.5) prove (1.5). At $a=\pi/3$, at least
$1/3-o(1)$ of the original eigenvalues lie outside this union.
For any $a_r\to0$, at most $1/2+o(1)$ lie inside it.
Replacing the full clock by the actual subset carrying the eigenvalues
of a rotated $M_{N_r}$ can only decrease the fraction inside.

## 5. A self-contained upper bound after arbitrary conjugation

This section proves (1.2). It is included to identify the actual scale
of the obstruction, rather than only saying that microscopic closeness
fails. It uses no conjecture about spacings.

### 5.1. Elementary short-moment bounds for the bare cat

The $N^2$ Weyl matrices form an orthonormal basis of the matrix space
for the normalized Hilbert--Schmidt inner product. Equation (3.4)
shows that conjugation by $M_N^m$ permutes this basis with no phases.
Therefore
$$
|\operatorname{Tr}M_N^m|^2
=\#\ker(S^m-I:\ (\mathbb Z/N\mathbb Z)^2
\longrightarrow(\mathbb Z/N\mathbb Z)^2).
\tag{5.1}
$$
For any nonsingular integral matrix $B$, this kernel has size at most
$|\det B|$. To see this without a divisibility assumption on $N$,
send a representative $x$ with $Bx=Ny$ to
$[y]\in\mathbb Z^2/B\mathbb Z^2$.
Changing $x$ by $Nz$ changes $y$ by $Bz$, and if the output
class is zero then $Bx=NBz$, so $x=Nz$. The map is injective.
The index of the full-rank lattice $B\mathbb Z^2$ is
$|\det B|$, as follows from a fundamental parallelogram or elementary
integer row and column reduction.
For $B=S^m-I$,
$$
|\operatorname{Tr}M_N^m|
\le\sqrt{\lambda^m+\lambda^{-m}-2}<\lambda^{m/2}.
\tag{5.2}
$$

In particular (2.1) and (5.2) imply, after increasing a constant,
$$
|\operatorname{Tr}X_N^m|\le C_0\,3^m,\qquad
X_N\in\{U_N,M_N\},\quad m\ge1,\quad N\ge N_0.
\tag{5.3}
$$

### 5.2. An elementary discrepancy estimate using squared Fejér kernels

Let $\mu$ be any probability measure on $\mathbb R/\mathbb Z$.
Suppose
$$
|\widehat\mu(j)|\le\epsilon,\qquad1\le j\le2H,\quad H\ge2.
\tag{5.4}
$$
We prove that, when $H\epsilon\le1$, every circular arc $I$
satisfies
$$
|\mu(I)-|I||\le C_1/H+4H\epsilon
\tag{5.5}
$$
with an absolute constant. Endpoints can be included or excluded; the
same bound holds after increasing $C_1$.

The Fejér kernel
$$
F_H(t)=\frac1H
\left(\frac{\sin(\pi Ht)}{\sin(\pi t)}\right)^2
=\sum_{|j|<H}(1-|j|/H)e^{2\pi ijt}
$$
is nonnegative and has integral one. Thus
$$
\mu*F_H\le1+2H\epsilon\le3.
$$
For $|t|\le1/(2H)$, the inequalities
$\sin(\pi H|t|)\ge2H|t|$ and
$\sin(\pi|t|)\le\pi|t|$ give $F_H(t)\ge4H/\pi^2$.
Every arc of length $1/H$ therefore has mass at most
$3\pi^2/(4H)$. Covering a longer arc by such arcs gives
$$
\mu(J)\le C_2(|J|+1/H)
\tag{5.6}
$$
with one absolute $C_2$.

Define
$$
J_H(t)=\frac{F_H(t)^2}{Z_H},\qquad
Z_H=\int F_H^2=\frac{2H^2+1}{3H}\ge\frac{2H}{3}.
$$
For the representative $|t|\le1/2$,
$$
J_H(t)\le
\min\left\{\frac{3H}{2},\frac{3}{32H^3|t|^4}\right\}.
$$
Splitting the integral at $1/H$ gives
$$
\int_{\mathbb R/\mathbb Z}|t|J_H(t)\,dt
\le\frac{3}{2H}+\frac{3}{32H}<\frac2H.
\tag{5.7}
$$
For a translate $I+t$, the symmetric difference with $I$ consists
of at most two arcs of total length at most $2|t|$. Equation (5.6)
therefore bounds
$$
|\mu(I+t)-\mu(I)|\le C_3(|t|+1/H).
$$
Integrate against $J_H(t)$ and use (5.7):
$$
\left|\mu(I)-\int_I(\mu*J_H)(x)\,dx\right|\le C_4/H.
\tag{5.8}
$$
Finally $J_H$ has Fourier degree $2H-2$, integral one, and every
Fourier coefficient has modulus at most one, by nonnegativity. Thus
(5.4) gives
$$
\|\mu*J_H-1\|_\infty\le4H\epsilon.
$$
Together with (5.8) this proves (5.5). Possible endpoint masses are
already bounded by $O(1/H)$ using the short-arc bound.

### 5.3. Applying discrepancy and matching sorted phases

For either empirical spectral measure
$$
\mu_N^X=N^{-1}\sum_j\delta_{\theta_{j,N}^X},
$$
equation (5.3) gives (5.4) with
$$
H=\left\lfloor\frac{\log N}{4\log3}\right\rfloor,\qquad
\epsilon=C_0N^{-1/2}.
$$
Indeed $3^{2H}\le N^{1/2}$. Then
$H\epsilon=o(H^{-1})$, so (5.5) yields
$$
\sup_I|\mu_N^X(I)-|I||=O(1/\log N).
\tag{5.9}
$$

Order representatives in $[0,1)$:
$\theta_1^X\le\cdots\le\theta_N^X$.
If the discrepancy is $D_X$, the distribution function at and just
before $\theta_j^X$ gives
$$
|\theta_j^X-j/N|\le D_X+1/N.
$$
Consequently
$$
\max_j|\theta_j^U-\theta_j^M|
\le D_U+D_M+2/N=O(1/\log N).
$$
Choose orthonormal eigenbases and let $W$ map the $j$-th
eigenvector of $M_N$ to the $j$-th eigenvector of $U_N$.
In this basis both $U_N$ and $WM_NW^*$ are diagonal, and
$$
\|U_N-WM_NW^*\|_{\rm op}
\le2\pi\max_j|\theta_j^U-\theta_j^M|
=O(1/\log N).
$$
This proves (1.2), already with $z=1$.

## 6. Arbitrarily deep divisibility by seven

The Pell estimate is not confined to $7\nmid N$. Directly,
$$
S^3=\begin{pmatrix}99&140\\70&99\end{pmatrix}
=I+7C,\qquad
C=\begin{pmatrix}14&20\\10&14\end{pmatrix}.
\tag{6.1}
$$
Induction gives
$$
S^{3\cdot7^s}=I+7^{s+1}C_s,\qquad C_s\equiv C\pmod7.
\tag{6.2}
$$
For the inductive step, expand the seventh power. After dividing by
$7^{s+2}$, its linear term is $C_s$; every term of degree at least
two has an additional factor 7. This also holds for degree seven,
whose remaining valuation is at least five.

The upper right entry of $S^r$ is $4N_r$ by (3.1). Since
$(C_s)_{12}\equiv20\not\equiv0\pmod7$, equation (6.2) proves
$$
v_7(N_{3\cdot7^s})=s+1.
$$
These are odd indices and hence odd dimensions. Thus all conclusions
of §§3--4 apply on this sequence, including $49\mid N$ once $s\ge1$.

This calculation does not turn a 7-adic minor valuation into an
Archimedean eigenvalue bound. It only shows that the already proved
physical trace suppression persists through that arithmetically
degenerate regime.

## 7. What was tested in the seven-path and hidden-symmetry route

The actual remaining counterexample possibility was checked against
the raw seven-component records, rather than against simple-spectrum
intuition.

1. The one-path total-minor argument at $7\nmid N$ is already in
   arithmetic_padic_jacobi_simplicity.md. It gives qualitative
   nonvanishing and a scalar algebraic commutant in those dimensions.
   No microscopic gap estimate follows from it.
2. For $N=7n$, the exact endpoint cat block between different paths
   is rank one when $7\mid n$. The mixed leading two-by-two endpoint
   minor can therefore vanish. This is a genuine failure of a
   one-leading-term argument, not evidence of a repeated eigenvalue
   of $U_N$.
3. The next proposed 5-adic dominant coefficient also has genuine
   cancellations: arithmetic_seven_chain_mod5_obstruction.md proves
   that its required valuation bound fails at $N=49$, with the
   displayed reversed-path congruences. Its residue calculation does
   not prove that the complete overlap minor is zero, and in fact that
   dimension is already covered by a separate simplicity certificate.
4. The all-odd one-component physical-minor theorem permits a mixed
   column set but keeps its row set inside one Jacobi component.
   It does not control a fully mixed determinant, nor its
   Archimedean size.
5. The old cross-block identity
   $\|P_tU_NP_s\|_{\rm HS}^2=n^2/N$ remains a one-step statement.
   It precludes treating the seven coordinate paths as independent
   spectra. It does not exclude a nonmonomial spectral subspace.

No actual approximate invariant subspace, multiplicity, or cluster at
width $O(1/N)$ was derived from these inputs. The calculations in
§§3--6 close a different, quantitative loophole: even an unrestricted
conjugation cannot restore the global bare-cat spectrum to microscopic
accuracy on the indicated Pell dimensions. Partial clusters and
different recurrence times remain possible.

## 8. A weaker all-odd corollary of the preceding pass

For completeness, the exact one-step calculation in Round 13 gives
$$
\liminf_{N\ {\rm odd}}|\operatorname{Tr}U_N|
\ge1+\frac{12297\pi}{250}\tau,
\quad|\operatorname{Tr}M_N|=1.
$$
The latter identity also follows from (5.1) at $m=1$, since
$\det(S-I)=-4$ is coprime to odd $N$.
For every $W,z$,
$$
N\|U_N-zWM_NW^*\|_{\rm op}
\ge\left||\operatorname{Tr}U_N|-|\operatorname{Tr}M_N|\right|.
$$
Thus
$$
\liminf_{N\ {\rm odd}}N d_N
\ge\frac{12297\pi}{250}\tau.
\tag{8.1}
$$
This is only a consequence of an older fixed-time result. The stronger
Pell conclusion above uses growing times and gives the logarithmic
scale. Neither estimate determines $H_2$.

## 9. Exact unresolved original spectral estimate

Define one fixed admissible function by
$$
\phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
I=\int_{\mathbb R}\phi,\quad
b_*=\frac{|\mathcal F^{-1}\phi|^2}{2I^2},\quad
w=|\widehat b_*|^2.
$$
Then $b_*\ge0$, $\sup b_*\le1/2<1$, $b_*$ is Schwartz, and
$\widehat b_*$ is smooth with support in $[-2,2]$.
The exact original pair deficit is
$$
\Delta_{2,N}(b_*)=
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left(
\left|\operatorname{Tr}
[(e^{i10^{-80}NA_N}M_N)^m]\right|^2-\min(m,N)
\right).
\tag{9.1}
$$
Its convergence to zero is still unproved. A fixed positive lower
bound for its absolute value on an infinite sequence of the original
odd dimensions is also unproved.

The new spectral-distance theorem does not insert an estimate for
(9.1). Its lower bound has scale $1/\log N$, much larger than
$1/N$, and controls comparison with a particular arithmetic
reference spectrum. Its upper bound is global discrepancy. Neither
one provides the signed Heisenberg-time sum in (9.1), and neither
controls all fixed orders required by $H_{\rm diag}$.

The actual new theorem is therefore a rigorous exclusion of global
bare-cat spectral inheritance after arbitrary conjugation. It is
not the requested negative or positive solution of the full problem.
