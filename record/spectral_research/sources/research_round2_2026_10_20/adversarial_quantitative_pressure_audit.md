> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_quantitative_pressure_audit.md`. Embedded SHA256: `4a0276a9ccd8874779c0b886b3abd8b723d746327d881fe40088b3f0fec01e7e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit of the quantitative pressure gap

## Scope, immutable inputs, and verdict

This audit checks the proof in `fermionic_quantitative_pressure.md`,
SHA-256
`d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2`.
The input was read in full. The mathematical verdict is **PASS** for
the stated pressure estimate and its stated quantum consequence.
No assertion about `H_diag` is obtained from this verdict.

The underlying analytic-potential input is
`arithmetic_pressure_analytic_potential.md`, SHA-256
`44da5eefab7cce7d7eb222fa54f027eec8a1a545b8ca0c4fd3fcf1fc7520637f`.
It was previously checked independently, including the corrected ordinary
Weyl symbol, in `adversarial_pressure_potential_audit.md`, SHA-256
`b0f2bed058af3a88a56122a3d73d64263296666b58f293ca846a023a58282e19`.
The quantum consequence uses `fermionic_twisted_pressure.md`, SHA-256
`9bfc9b4a27e8cd7d23bc1693d439f7cb0be31321fbe1947875d9bb8271649bd5`.

The result being checked is

$$
 \frac12\log(3+2\sqrt2)-P_*
 \ge 2000\tau^2=2\cdot10^{-157},\qquad \tau=10^{-80}.
$$

The new substantive step is an explicit analytic disk for the pressure,
not just for its underlying potential. The audit does not infer that
analyticity merely from a qualitative perturbation theorem.

## 1. Independent verification of the published coding input

I opened and read the primary full text of Siemaszko--Wojtkowski,
*Counting Berg partitions*, arXiv:1007.3984,
<https://arxiv.org/pdf/1007.3984>, particularly Section 2 (preprint
pp. 2--3), Theorem 4.1 and its proof (pp. 8--9), and Theorem 4.2 and
the positive-eigenvalue placement statement (pp. 9--11).

The orientation in the audited proof is consistent throughout:

$$
 B(q,p)=(q-\sqrt2p,q+\sqrt2p),\qquad
 BSB^{-1}=\operatorname{diag}(\lambda^{-1},\lambda),
 \qquad \lambda=3+2\sqrt2.
$$

The horizontal coordinate is stable. The lattice basis is
$e=(1,1), f=(-\sqrt2,\sqrt2)$, and the matrix of the toral map in
this basis is exactly $S$. The primary construction gives rectangle
side lengths $(u,p),(v,q)$ from a basis $(v,p),(-u,q)$. Here this
is $(\sqrt2,1),(1,\sqrt2)$. Theorem 4.1 defines its connectivity
matrix using translates of the destination rectangle crossed by the
image of the source rectangle, and gives the transpose of the lattice
matrix when the expanding eigenvalue is positive. Thus

$$
 C=S^T=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$

Both eigenvalues are positive and the chosen spine intersection can be
placed at the fixed origin, precisely as required by the published
positive-eigenvalue application of Theorem 4.2. No result for an
unspecified placement of rectangles is being substituted.

The use of twelve distinct edges is essential and is present. The
two-vertex itinerary alone need not be generating; the primary paper
explicitly warns of this. Here each edge records an actual full crossing
strip. Full-height image crossings have full-width horizontal preimages.
Iterating the two kinds of strips gives nonempty rectangular cylinders
for every admissible edge word. Past and future conditions contract the
two respective side lengths geometrically. Consequently the centered
edge coding has diameter at most $10\lambda^{-n}$ in the specified
input metric. The possible fourfold boundary coding is harmless. The
quadrant-germ argument for the claimed fiber bound is valid, although
the pressure calculation does not need that bound.

The pushforward of the Markov measure is also checked directly. The
Perron vectors are $r=(1,\sqrt2)$, $l=(\sqrt2,1)$, so both
stationary vertex probabilities are $1/2$. An individual edge
$i\to j$ has forward probability $r_j/(\lambda r_i)$. An
$n$-edge cylinder with initial tile $i$ and final tile $j$
has normalized area

$$
 \frac{w_i h_j}{2\sqrt2\lambda^n}
 =\frac12\frac{r_j}{\lambda^n r_i}.
$$

This is exactly its Markov probability. The same statement for centered
words follows by invariance; shrinking cylinders and zero-area
boundaries then prove that the coding pushes the Markov measure to
Haar area. Neither an unchecked finite-extension entropy assertion nor
an unquantified symbolic spectral gap is needed.

## 2. The one-sided cohomology, including the finite endpoint

Write $a_0=\lambda^{-1/2}=\sqrt2-1$ and $\theta=2/3$. For a
two-sided function $F$, let $V$ denote its centered variation
constant at rate $a_0$. Fix one past loop at each initial vertex,
and let $\bar x$ retain the nonnegative edges of $x$ and use
this chosen loop in its negative coordinates.

With

$$
 u_M(x)=\sum_{n=0}^{M}
 [F(\sigma^n x)-F(\sigma^n\bar x)],
$$

an exact finite rearrangement gives

$$
\begin{split}
 F-u_M+u_M\circ\sigma
 ={}&F(\bar x)+\sum_{n=0}^{M}
 [F(\sigma^{n+1}\bar x)-F(\sigma^n\overline{\sigma x})]\\
 &+F(\sigma^{M+1}x)-F(\sigma^{M+1}\bar x).
\end{split}
$$

The final difference is bounded by $Va_0^{M+1}$. Each difference
inside the infinite limiting sum is bounded by $Va_0^n$. Thus all
the limiting rearrangements are justified by uniform convergence and
the resulting $F^+$ depends only on the future.

For two futures sharing their first $k\ge2$ edges, the initial
term varies by at most $Va_0^{k-1}$. The summand numbered
$n\le k-2$ varies by at most

$$
 2V\min(a_0^n,a_0^{k-n-2}).
$$

After splitting at $J=\lfloor(k-2)/2\rfloor$, the displayed
bound (2.4) of the input follows. To check its constant explicitly,
for $k=2r$ its right-hand side before division by $\theta^k$
is

$$
 V\left[a_0^{2r-1}+
 \frac{2(1+a_0)}{1-a_0}a_0^{r-1}\right].
$$

The ratio decreases with $r$, since $a_0<\theta^2$, and is
less than 12 already at $r=1$. For $k=2r+1$, $r\ge1$,
the corresponding expression is

$$
 V\left[a_0^{2r}+\frac{4}{1-a_0}a_0^r\right],
$$

whose ratio also decreases and is less than 11 at $r=1$. Hence
16 is safe. The $k=1$ bound follows from twice the supremum norm.
This proves the stated bounded linear map with norm at most 32.
Together with the coding diameter estimate and the potential input,
$\|v_t(s)\|_\theta\le10^{14}|s|$ is valid. The map is fixed,
linear, and bounded, so it preserves holomorphic parameter dependence.

## 3. The spectral gap is quantitatively proved

For the incoming-edge transfer operator, the backward vertex chain is

$$
 P=\begin{pmatrix}
 3/\lambda&2\sqrt2/\lambda\\
 2\sqrt2/\lambda&3/\lambda
 \end{pmatrix}.
$$

The off-diagonal entries correctly incorporate the multiplicities
$C_{21}=4$ and $C_{12}=2$ together with the left Perron
weights. Its nontrivial eigenvalue is $q_0=\lambda^{-2}$. Starting
at either vertex, its total variation distance from the stationary
law after $j$ steps is exactly $q_0^j/2$.

Approximating a function by one depending on its first $k$ edges
costs $\theta^k|g|_\theta$ in supremum norm. After $n\ge k$
backward steps, the initial block law is a Markov-kernel image of the
vertex law after $n-k$ steps. This proves

$$
 \|L_0^ng-\mu g\|_\infty
 \le2\theta^k|g|_\theta+q_0^{n-k}\|g\|_\infty.
$$

Separately, pairing incoming edges for futures sharing a prefix proves
$|L_0^ng|_\theta\le\theta^n|g|_\theta$. Taking
$k=\lfloor n/2\rfloor$, with $n=0,1$ treated directly,
gives the advertised operator norm bound

$$
 \|L_0^n-\Pi\|_\theta\le6(5/6)^n.
$$

In particular, the otherwise problematic initial-vertex variation is
controlled by the two-state chain; it has not been silently omitted
from the norm estimate.

## 4. The analytic radius and Cauchy remainder

The Banach algebra product inequality gives
$\|L_v-L_0\|\le2\|v\|_\theta<4\cdot10^{-10}$ on
$|s|<2\cdot10^{-24}$. Summing the proved gap gives

$$
 \|(z-L_0)^{-1}\|
 \le |z-1|^{-1}+\frac6{|z|-5/6}.
$$

On $|z-1|=1/24$ the bound is 72, because the minimum modulus is
23/24. On $|z|=9/10$ it is 100. On the region exterior to both
disks it is at most 114. The product of any of these constants with
the perturbation norm is much less than one. Thus the Neumann
resolvent exists on both circles and outside the two disks.

The rank-one contour projection differs from $\Pi$ by at most

$$
 \frac{72^2}{24}
 \frac{4\cdot10^{-10}}{1-72(4\cdot10^{-10})}<10^{-6}.
$$

Injectivity of the restrictions of projections at distance less than
one proves equality of ranks, including excluding an infinite-rank
perturbed range. The eigenvalue quotient using $\Pi_v1$ has a
nonzero denominator and is holomorphic. Its logarithm has modulus at
most $-\log(23/24)<1/12$. For real parameters the eigenfunction
is within $10^{-6}$ of 1 and hence positive. The complement
contributes $O((9/10)^n)$, while the positive leading eigenvalue
exceeds 23/24. These facts establish the claimed logarithmic integral
limit without cancellation of its leading coefficient.

The pressure identification is also direct. In the stated small
eigen-coordinate metric, consecutive short orbit differences cannot
acquire a nonzero lattice jump, since $(1+\lambda)\epsilon<1/2$.
An $n$-step Bowen ball therefore has exactly the rectangular side
constraints stated in the input, and volume $c_\epsilon\lambda^{-n}$.
The variation of a Hölder Birkhoff sum on that rectangle is bounded
independently of $n$. Disjoint small balls and covering maximal
separated sets yield the two-sided comparison between the separated
partition sum and $\lambda^n\int e^{S_nf}\,dx$. Haar pushforward,
the bounded cohomology endpoint, and conditional backward Markov
averaging then give

$$
 P_S(-t\psi_s)=(1-t)\log\lambda+q_t(s)
$$

for real $s$ in the entire small disk. Thus the analytically
constructed eigenvalue is the required pressure, with its explicit
complex bound; this identification is not assumed.

## 5. Independent derivative and numerical coefficient check

Normalize the eigenfunction by $\mu h(s)=1$. For a general
analytic potential curve with $w=v'(0)$, differentiation yields

$$
 z'(0)=\mu w,\qquad
 h'(0)=\sum_{n\ge1}L_0^n(w-\mu w).
$$

Differentiating again and subtracting $z'(0)^2$ gives

$$
 (\log z)''(0)=\mu v''(0)+\mu(w-\mu w)^2
 +2\sum_{n\ge1}\mu[(w-\mu w)L_0^n(w-\mu w)].
$$

All series converge absolutely by the proved gap. The adjoint identity
for the backward Markov operator turns this into the asymptotic
variance. The bounded coboundary changes centered Birkhoff sums by
$O(1)$, and hence changes their second moments divided by $n$
by $O(n^{-1/2})$; means agree exactly by invariance. This verifies
the coefficient transfer to the torus observable $\xi$.

The geometric-pressure-zero input applies for every real parameter in
this disk: the derivative estimates give invariant hyperbolic cones,
the parameter conjugacy is a homeomorphism, area is preserved, and the
unit-roof suspension satisfies the same explicitly checked
Bowen--Ruelle hypotheses as the earlier pressure proof. Thus
$q_1(s)=0$ on a real interval and therefore as a holomorphic
function. It follows that

$$
 \int\psi''_0\,dx=\sigma^2(\xi),\qquad
 q_{1/2}''(0)=-\tfrac14\sigma^2(\xi).
$$

Cauchy's coefficient estimate on $R_p=10^{-24}$, using the
bound $1/12$, gives

$$
 \left|\Delta(s)-\frac{\sigma^2(\xi)}8s^2\right|
 \le\frac{|s|^3}{12R_p^3(1-|s|/R_p)}
 \le10^{72}|s|^3
 \quad (|s|\le R_p/2).
$$

This is a remainder for the pressure itself.

The two isolated Fourier orbits used in the input give an independent
exact lower bound without reliance on the separate full variance
certificate. The form $2k^2-l^2$ is invariant under $S^T$.
In the support $|l|\le1$, its value 98 permits only
$(\pm7,0)$, which cannot belong to the same orbit because no
integer power of $S^T$ has eigenvalue $-1$. The corrected
ordinary symbol has $\widehat a(7,0)=9/20$: the coefficients of
$r$ at 6 and 8 agree, so the $r\sin(2\pi q)$ contribution
at 7 vanishes. Hence

$$
 \widehat\xi(7,0)=\frac{441\pi}{10\sqrt2},\qquad
 \sigma^2(\xi)\ge\frac{194481\pi^2}{100}.
$$

Grouping the finite Fourier correlations by $S^T$-orbits produces
nonnegative squares. Each pair of nonzero support vectors is related
by at most one iterate, so no convergence issue is hidden in this
grouping. The displayed contribution alone gives
$\sigma^2(\xi)/8>2187$. At $\tau=10^{-80}$, the pressure
remainder is at most $10^{-8}\tau^2$, proving the weaker,
convenient numerical constant 2000.

For comparison, my independent Gaussian-rational Fourier calculation,
recorded in the earlier potential audit, gives the exact value

$$
 \sigma^2(\xi)=\frac{7834656061\pi^2}{4000000}.
$$

That additional calculation is not needed for the numerical theorem
audited here.

## 6. The inverse map convention and the quantum implication

The original physical map is the inverse of the arithmetic-coordinate
map $\Xi_\tau$. The area determinant and the angle between the
stable and unstable bundles imply

$$
 \log J_{F^{-1}}^u(Fx)
 =\log J_F^u(x)+c(Fx)-c(x),\qquad
 c(x)=\log\sin\alpha(x).
$$

Here $c$ is continuous and bounded. This verifies the input's
argument using invariant measures and inverse entropy. One can also
avoid any additional variational-principle invocation: reversing an
$n$-orbit by $x\mapsto F^{-(n-1)}x$ gives exactly the same
separated partition sums for $F^{-1}$ and $F$, for any fixed
potential. Moreover, if $\phi=\log J_F^u$ and
$\widetilde\phi=\log J_{F^{-1}}^u$, the identity above gives

$$
 \widetilde\phi-\phi=d-d\circ F,
 \qquad d=(\phi-c)\circ F^{-1}.
$$

Thus the two geometric pressures agree directly by bounded endpoint
terms in the separated-set definition. The convention change causes
no sign or coefficient loss in the quantitative gap.

Finally choose the fixed positive slack $\eta=1000\tau^2$ in
the previously audited all-time, all-Weyl pressure transfer. Its common
threshold may depend on this slack, but not on time or Weyl indices.
The estimate $P_*\le\frac12\log\lambda-2000\tau^2$ therefore
gives exactly

$$
 \sup_{a,b}|\operatorname{Tr}(T_N(a,b)U_N^m)|
 \le C\exp[(\tfrac12\log\lambda-1000\tau^2)m]
 +2q_*^m
$$

for all $m\ge1$ and all sufficiently large odd $N$. No
assumption that $m/N^2$ is small is introduced at this step; the
earlier all-time transfer absorbed that quantity into a fixed
exponential slack after imposing one common threshold on $N$.

The right-hand side remains exponentially growing in $m$. This
audit consequently does not certify a bounded weighted power-trace
sum at $m\asymp N$, the pair criterion, or any higher-order
factorial cancellation. Those remain separate missing estimates.
