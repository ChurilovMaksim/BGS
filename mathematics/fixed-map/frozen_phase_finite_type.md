# Uniform finite type of translated physical-symbol differences

**Claim ID:** `BGS-FM-014`

Date: 30 September 2026.

Status: project proof and author check; exact algebra and finite controls.
This completes and strengthens Section 14 of the submitted Heisenberg note.
No priority or quantum FUP claim is made.

## 1. Statement for the unchanged physical symbol

Use the ordinary midpoint symbol of [FM-001](fixed_model_symmetry_theorem.md):
$$
r(q)=(1-\cos14\pi q)(1+\cos2\pi q),\qquad
g(q,p)=\cos14\pi q+r(q)/10+r(q)\sin2\pi q/100-1/10
+r(q+1/2)\cos(2\pi p-\alpha)/100,
$$
where $e^{i\alpha}=(-3+4i)/5$. Put $D=(2\pi)^{-1}\partial_q$ and
$\phi_\delta(q,p)=g(q+\delta_q,p+\delta_p)-g(q,p)$.
The hypothesis is the actual circle distance
$d_{\mathbb T}(\delta_q,0)\ge1/7$, with arbitrary $p,\delta_p$.
Define
$$
c_0=\frac{\sqrt{101}\sin(\pi/7)-1}{100}>0,\quad
L_0=\frac{6409325}{2286144},\quad
\kappa_0=\frac{4c_0}{3L_0}.
$$
Then, at every $(q,p)$,
$$
\max_{1\le j\le14}|D^j\phi_\delta|\ge\kappa_0,
\qquad
\max_{2\le j\le15}|D^j\phi_\delta|\ge\kappa_0.                 \tag{1}
$$
The second inequality also holds for $\phi_\delta+\ell q$, for every
real $\ell$, on a lifted interval. For $a\in W^{1,1}([0,1])$ and
$\lambda\ge1$, uniformly in the stated parameters,
$$
\left|\int_0^1 a(q)e^{i\lambda\phi_\delta(q,p)}dq\right|
\le C\|a\|_{W^{1,1}}\lambda^{-1/14},                         \tag{2}
$$
and the same integral with phase $\phi_\delta+\ell q$ is bounded by
$C\|a\|_{W^{1,1}}\lambda^{-1/15}$, uniformly also in $\ell$.
Constants are not optimized. Numerically, only for orientation,
$c_0\simeq0.03360477612$, $\kappa_0\simeq0.01598199650$.

## 2. Exact coefficient isolation

The $q$ frequencies are $0,\pm1,\pm2,\pm5,\pm6,\pm7,\pm8,\pm9$.
At $q$ frequency $-1$ the $p$-independent coefficient is
$1/20+i/200$, of modulus $\sqrt{101}/200$.
Each of the two $p$-dependent coefficients has modulus $1/400$.
Thus the coefficient $C_{-1}(p;\delta)$ of $e^{-2\pi iq}$ in
$\phi_\delta$ obeys
$$
|C_{-1}|\ge \frac{\sqrt{101}}{200}|e^{-2\pi i\delta_q}-1|
-\frac1{100}\ge c_0.                                      \tag{3}
$$
Positivity follows already from $\sin(\pi/7)>2/7$ and $\sqrt{101}>10$.

Let
$$
R(z)=\prod_{n\in\{2,5,6,7,8,9\}}(1+z^2/n^2),\qquad
P_{14}(z)=z(z-i)R(z),\quad P_{15}(z)=z^2(z-i)R(z).
$$
Both annihilate all the listed frequencies except $-1$.
Since $R$ has positive real coefficients in even degrees, the two
interlaced coefficient sequences of $(z-i)R$ have no cancellations, so
$$
\|P_{14}\|_{\ell^1}=\|P_{15}\|_{\ell^1}
=2\prod_n(1+n^{-2})=L_0,
\qquad |P_{14}(-i)|=|P_{15}(-i)|=2\prod_n(1-n^{-2})=4/3.
$$
Consequently $|P_j(D)\phi_\delta|\ge4c_0/3$ pointwise.
The triangle inequality proves (1). The extra zero at $z=0$ in $P_{15}$
annihilates the linear addition as well. This is why the order-15
statement is retained rather than replaced by the order-14 statement.

## 3. Uniform scalar cancellation, including partition control

Here the scalar phase really is the displayed trigonometric polynomial;
this proof does not identify it with a quantum matrix element.
All its derivatives of order at least two are trigonometric polynomials
of degree at most 9. A nonzero such polynomial has at most 18 zeros
on one circle. Threshold equations for any derivative have at most
18 zeros each, unless the equation is identically satisfied, in which
case it needs no partition boundary.

Partition at the solutions of $\phi^{(j)}=\pm\kappa_0/2$ for
$1\le j\le14$. There are uniformly finitely many intervals. On each,
one derivative stays of modulus at least $\kappa_0/2$: (1), and
$(2\pi)^j\ge1$, give such a derivative at an interior point, and the
threshold boundaries prevent it crossing below the threshold.
For $0<u<\kappa_0/4$, intervals with $j=1$ contain no point of
$E_u=\{|\phi'|\le u\}$; the others have
$| (\phi')^{(j-1)}|\ge\kappa_0/2$ with $1\le j-1\le13$.

We use the elementary sublevel lemma: if $|f^{(r)}|\ge b>0$
on an interval, then $|\{|f|\le u\}|\le C_r(u/b)^{1/r}$.
To see it, select $r+1$ points of the sublevel set separated by
at least a constant times its measure divided by $r+1$ (use measure
quantiles and an arbitrarily small slack). The divided-difference formula
bounds the $r$th divided difference by $C_r u/|E|^r$.
The repeated mean-value theorem makes it $f^{(r)}(\xi)/r!$.
This proves the lemma, also for a disconnected measurable sublevel set.
Summing gives $|E_u|\le C u^{1/13}$.

On its complement, additionally partition at zeros of $\phi''$ and
at $\phi'=\pm u$. There are uniformly finitely many intervals;
$\phi'$ is monotone and $|\phi'|>u$ on each. Integration by parts bounds
their total integral by
$C(\lambda u)^{-1}(\|a\|_\infty+\|a'\|_1)$, since the total variation
of $1/\phi'$ on each monotonic interval is at most $2/u$.
The sublevel part is at most $C\|a\|_\infty u^{1/13}$.
Take $u=\lambda^{-13/14}$ for sufficiently large $\lambda$;
bounded smaller $\lambda$ are absorbed into $C$. This proves (2).

For $\phi+\ell q$, partition using only orders $2,\ldots,15$.
The same argument has sublevel exponent $1/14$ and hence cancellation
$\lambda^{-1/15}$. All root counts remain uniform in $\ell$;
$\phi'+\ell=\pm u$ is still a degree-9 trigonometric equation.

## 4. Robustness and the precise missing quantum implication

If a real perturbation $E$ satisfies
$\max_{1\le j\le14}\|D^jE\|_\infty\le |t|\kappa_0/2$, then
$t\phi+E$ has the first lower bound (1) with $|t|\kappa_0/2$.
The analogous hypothesis for orders $2,\ldots,15$ gives the second
bound, also with a linear addition. This is a derivative statement;
uniform scalar constants for arbitrary perturbations need additional
upper derivative/partition control.

For the actual propagator, the Hamiltonian time is $\tau/(2\pi)$,
not $\tau$ when $X_g=(g_p,-g_q)$. A generating function for the full
canonical commutator loop has not been constructed here. Neither
$e^{i\tau N A_\delta}e^{-i\tau N A}$ nor its kernel may be replaced by
$e^{i\tau N\phi_\delta}$: the operators do not commute.
Small fixed $\tau$ alone is not a quantitative $C^{15}$ remainder bound.
Thus (1)--(2) give no one-kick operator norm gap, no long-time FUP,
and no microscopic CUE law.

Different seven-strip labels do not imply the hypothesis:
$q=1/7-\eta$, $q'=1/7+\eta$ have different labels but distance $2\eta$.
Boundary and adjacent-strip channels require a separate argument.

## 5. Half-translation local check

For $\delta=(1/2,0)$, both circles $q=0,1/2$ are critical for
$\phi_\delta$ in both coordinates. Direct differentiation gives
$$
\partial_q^2\phi_\delta(0,p)
=\frac{\pi^2}{25}[8840+96\cos(2\pi p-\alpha)],\qquad
\partial_q^2\phi_\delta(1/2,p)=-\partial_q^2\phi_\delta(0,p).
$$
This yields the submitted interval $[8744,8936]\pi^2/25$ and its
negative. Compactness and the uniform nonzero Hessian give local
Morse--Bott neighborhoods and scalar $O(\lambda^{-1/2})$ cancellation
with cutoffs supported there. Other critical points were not classified;
a global order-$1/2$ bound does not follow from these two circles.

The [audited verifier](../../computations/verification/heisenberg_note_audit.py)
reconstructs all 32 coefficients, isolates the mode exactly, checks the
half-shift derivatives, and tests the physical matrix dictionary separately.
