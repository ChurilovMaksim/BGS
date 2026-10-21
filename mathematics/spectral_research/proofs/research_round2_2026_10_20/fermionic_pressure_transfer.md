> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_pressure_transfer.md`. Embedded SHA256: `90ebc84c3c9fb7c049a1a9d11e0d5dcb72c4fc89b362da3f848521a7bca79756`.
> [Thematic guide](../../topics/classical_trace.md).

# A strict classical pressure gap and actual quantum suppression of cat returns

Research continuation, 20 October 2026. The parameter is exactly
`tau=10^-80`; it is independent of N. Every quantum assertion below
concerns the specified matrices `U_N`, through all sufficiently large
odd N. The result is a strict improvement of the all-time exponential
trace bound, and a polynomial upper bound at the bare cat's logarithmic
return times. It does not establish a microscopic pair limit or `H_diag`.

## 1. Frozen mathematical inputs

Write

$$
\lambda=3+2\sqrt2,\quad \rho=\lambda^{-1},\quad
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},\quad
h=(2\pi N)^{-1},\quad t_*={\tau\over2\pi}.
$$

The ordinary Weyl symbol of the matrix in the question is

$$
a(q,p)=\cos(14\pi q)+{r(q)\over10}
 +{r(q)\sin(2\pi q)\over100}-{1\over10}
 +{r(q+1/2)\cos(2\pi p-\alpha_0)\over100}.
$$

Its classical map is `Psi=phi_a^(-t_*) composed with L`.
The previously proved analytic and cone estimates give a real analytic,
area-preserving diffeomorphism with an equivariant lift

$$
\Psi(x)=Lx+v(x),\qquad v(x+n)=v(x),\quad n\in\mathbb Z^2.
\tag{1.1}
$$

In fixed eigen-coordinates for L, `L=diag(lambda,rho)`, and
`||Dv||<10^-69`; using this relaxed bound absorbs row sums. The forward
and backward invariant cones construct the unstable and stable line
bundles. An unstable vector whose first coordinate is one is multiplied
in that coordinate by a positive factor greater than 5. In particular,
for every period m the unstable multiplier satisfies `Lambda_m>=5^m`.
These assertions, including the correct shifted symbol, are proved in

`../research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md`,
SHA-256
`355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c`.

The actual quantum trace has the exact all-time decomposition

$$
p_{m,N}=\operatorname{Tr}U_N^m=\mathcal P_{m,N}+E_{m,N},\qquad
|E_{m,N}|\le2q_*^m,\quad q_*=0.421,
\tag{1.2}
$$

$$
\mathcal P_{m,N}
=\zeta_N^m\sum_{x\in\operatorname{Fix}\Psi^m}
 \omega_{m,N}(x)\lambda^{-m/2}\Gamma_h(x,m),
\qquad |\zeta_N|=|\omega_{m,N}(x)|=1.
\tag{1.3}
$$

There are constants `C_mod` and `h_0>0` such that, simultaneously for
all `0<h<h_0`, all periods m and all their periodic points,

$$
\left|\log\left(\lambda^{-m}|\Gamma_h(x,m)|^2
                                      \Lambda_m(x)\right)\right|
\le C_{\rm mod}mh^2.
\tag{1.4}
$$

The uniformity in (1.4) is essential. It is exactly equation (9.6) of
`../research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md`,
SHA-256
`c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1`.
The preceding exact sector and amplitude input is combined into
`../research_continuation_2026_10_20/exact_dynamical_determinant.md`,
SHA-256
`e75d4e7477246e189ba56f0b6bbbda4d806ad1e8bb114e1f4b7d07613b8f0035`.

Finally `x_0=(0,0)` is an actual fixed point and

$$
\operatorname{Tr}D\Psi(x_0)
=6+{39212\pi\over125}\tau>6.
\tag{1.5}
$$

For completeness the local calculation behind (1.5) is short.
`grad a(0,0)=0` and

$$
D^2a(0,0)=\operatorname{diag}(c_0,0),\qquad
c_0=-{19606\pi^2\over125}.
$$

Indeed `r''(0)=392 pi^2`, `r''(1/2)=8 pi^2`, and
`cos alpha_0=-3/5`; the term containing `r(q) sin(2 pi q)` has zero
second derivative there. Hence
`DX_a(0,0)=((0,0),(-c_0,0))`, whose square is zero, and
`D phi_a^(-t_*)(0,0)=((1,0),(t_*c_0,1))`. Multiplication by L gives
`Tr D Psi=6-4t_*c_0`, which is (1.5). This also appears in the frozen
`fermionic_root_trace_audit.md`, SHA-256
`449aa3d72f26a6b3b195395f5ef714ecebcd3a42071718b569f8d7658c0712eb`.

Let `Lambda_0>1` be the unstable eigenvalue at `x_0`. Since
`Lambda_0+Lambda_0^-1>6=lambda+lambda^-1` and `u+u^-1` increases on
`u>1`,

$$
\boxed{\Lambda_0>\lambda.}
\tag{1.6}
$$

No comparison of two unknown periodic points is needed for this strict
inequality.

## 2. An explicit topological conjugacy, with a checked smallness bound

This section supplies transitivity, dense periodic points, expansivity
and entropy for the actual map without an unspecified structural
stability threshold.

Use the maximum norm in the eigen-coordinates of L. For a homeomorphism
`F` of the torus and continuous vector-valued g define

$$
(\mathcal G_Fg)^u(x)
 =-\sum_{j=0}^{\infty}\lambda^{-j-1}g^u(F^j x),
\qquad
(\mathcal G_Fg)^s(x)
 =\sum_{j=1}^{\infty}\rho^{j-1}g^s(F^{-j}x).
\tag{2.1}
$$

The two series converge uniformly and define continuous functions.
Shifting their indices proves

$$
(\mathcal G_Fg)(Fx)-L(\mathcal G_Fg)(x)=g(x),\qquad
\|\mathcal G_Fg\|_\infty\le K\|g\|_\infty,
\quad K=(1-\rho)^{-1}<1.21.
\tag{2.2}
$$

The same formulas apply to bounded two-sided sequences, with F replaced
by the index shift. They give the unique bounded solution of
`u_(n+1)-Lu_n=g_n`. Uniqueness follows because a nonzero homogeneous
solution `L^n u_0` is unbounded in at least one time direction.

The map

$$
w\longmapsto\mathcal G_L\bigl[v\circ(\operatorname{Id}+w)\bigr]
$$

is a contraction on the complete space of continuous periodic
vector-valued functions: its Lipschitz constant is at most
`K ||Dv||<1`. Iterating it from zero converges uniformly to a unique w.
For the equivariant lift `H(x)=x+w(x)`, equation (2.2) gives

$$
H\circ L=\Psi\circ H,\qquad \|w\|_\infty\le K\|v\|_\infty.
\tag{2.3}
$$

This use of a contraction requires no differentiability of w.

Set `u=G_Psi(-v)` and `G(y)=y+u(y)`. Then

$$
G\circ\Psi=L\circ G.
\tag{2.4}
$$

To verify that H and G are inverse homeomorphisms, first note that
`G H` commutes with L. Its displacement from the identity is a bounded
periodic function e, and therefore
`e(L^n x)=L^n e(x)` for every integer n. Boundedness in both time
directions implies `e(x)=0`. Hence `G H=Id`.

For any lift y put `z=H G(y)`. Equations (2.3)--(2.4) imply
`G Psi^n(z)=G Psi^n(y)` for every integer n. Thus

`delta_n=Psi^n(z)-Psi^n(y)`

is bounded by `2||u||_infinity`. It satisfies

$$
\delta_{n+1}-L\delta_n
=v(\Psi^n z)-v(\Psi^n y).
$$

Apply the bounded-sequence version of (2.2):

$$
\|\delta\|_\infty
\le K\|Dv\|\,\|\delta\|_\infty.
$$

The coefficient is less than one, so `delta=0`, whence `H G=Id`.
The continuous equivariant maps H and G descend to inverse torus
homeomorphisms. Consequently

$$
\boxed{\Psi=H L H^{-1}\quad\hbox{topologically}.}
\tag{2.5}
$$

There is no claim that H is differentiable. Formula (1.6) in fact
precludes a `C^1` conjugacy.

### 2.1 The properties transported through (2.5)

The linear torus map L is expansive. To see this, choose a radius e
smaller than the shortest nonzero lattice norm divided by `1+||L||`.
If the lifted differences `d_n` of two torus orbits have norms at most
e, then `d_(n+1)-L d_n` is an integer vector of norm less than the
shortest nonzero lattice norm, and is zero. Thus `d_n=L^n d_0` is
bounded for all integers n, implying `d_0=0`. Uniform continuity of
H and its inverse transfers expansivity to Psi.

Every rational torus point is periodic for L, since L acts bijectively
on every finite denominator grid. Hence periodic points are dense.
For two fixed nonconstant Fourier characters, their correlation under
`L^n` is zero for all sufficiently large n: the only obstruction is
the equality `(L^T)^n k+l=0`, which eventually fails. A nonzero integer
vector cannot lie in the irrational stable eigendirection, so its
forward images escape every finite set. Trigonometric approximation
then gives mixing of Haar measure. Nonempty open sets have positive
Haar measure, so L is topologically mixing. Thus Psi is topologically
mixing and has dense periodic points as well.

Here is also a direct entropy computation. At a sufficiently small
fixed radius e, the length-m Bowen ball for L lifts to

$$
|d_u|\le e\lambda^{-(m-1)},\qquad |d_s|\le e.
$$

The absence of integer jumps follows by the preceding expansivity
calculation, restricted to `0<=j<m`. Its area is a fixed positive
constant times `e^2 lambda^(-m)`. Bowen balls of radius `e/2` around
an `(m,e)`-separated set are disjoint. A maximal such set has radius-e
Bowen balls covering the torus. Comparing areas in these two statements
bounds its maximal cardinality above and below by constant multiples
of `lambda^m`. This proves

$$
h_{\rm top}(L)=\log\lambda.
$$

Conjugacy transfers entropy because uniform continuity turns separated
or spanning sets at one fixed radius into such sets at another radius;
taking logarithmic growth and then the radius tending to zero gives
equality. Therefore

$$
\boxed{h_{\rm top}(\Psi)=\log\lambda.}
\tag{2.6}
$$

## 3. Exact published inputs and their hypotheses

The only thermodynamic theorem used here is from R. Bowen and D. Ruelle,
*The Ergodic Theory of Axiom A Flows*, Invent. Math. **29** (1975),
181--202, DOI `10.1007/BF01389848`:
[complete author-hosted article](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B42%5D.pdf).

For a `C^2` flow on a compact smooth Riemannian manifold and a basic
hyperbolic set:

* Theorem 3.3, p.187: every real Hölder potential has a unique equilibrium
  state `mu_b`, with the lower bound
  `mu_b(B_T(x,e))>=c_e exp(integral_0^T b(F^t x)dt-T P(b))`.
* Lemmas 4.1--4.2, p.189: the negative infinitesimal unstable Jacobian
  `chi` is Hölder, and
  `c_e^-1 <= vol(B_T(x,e)) J_T^u(x) <= c_e`.
* Proposition 4.4(b), p.190: `P(chi)=0` on an attractor.
* Theorem 5.1 and Remark 5.2, pp.191--192: for an Anosov flow preserving
  a smooth probability volume, that volume is `mu_chi`.

We also use the variational principle stated on pp.185--186, for both
maps and flows. No mixing hypothesis is required in these cited
statements. Their basic-set hypotheses are checked next, rather than
being transferred without verification from a map to a flow.

## 4. The constant-roof suspension and the pressure identity

Form the smooth compact mapping torus

$$
\mathcal M=(\mathbb T^2\times\mathbb R)/
                  \bigl((x,s+1)\sim(\Psi x,s)\bigr),
\qquad F^t[x,s]=[x,s+t].
\tag{4.1}
$$

Smoothness follows from the smooth gluing diffeomorphism Psi. The
vertical vector field is everywhere nonzero. The stable and unstable
line bundles of Psi suspend to invariant line bundles of the flow;
the vertical line is its central bundle. Uniform expansion and
contraction of Psi, and bounded distortion during fractional times on
the compact mapping torus, give the required exponential hyperbolicity.

The whole manifold is a basic hyperbolic set. It is locally maximal
by taking its neighborhood to be itself. Dense periodic points of
Psi give dense closed flow orbits. A dense orbit of Psi, together with
the fractional flow times, gives a dense orbit of F. The entire
manifold is also an attractor in the cited definition. Thus no proper
attractor or boundary condition is needed. The flow need not be mixing;
constant roof one generally prevents mixing, and no cited theorem here
requires it.

The top form `dq wedge dp wedge ds` glues smoothly because Psi preserves
area, and is invariant under F. Normalize it to a probability volume
`m_F`. Choose a smooth Riemannian metric having this volume: starting
from any smooth metric, a smooth scalar rescaling adjusts its volume
density to this prescribed positive top form. This choice lets the
volume in the cited volume lemma be exactly `m_F`.

Let

$$
\chi(z)=-\left.{d\over dt}\log J_t^u(z)\right|_{t=0},
\qquad
\varphi(x)=\log J_\Psi^u(x),
\tag{4.2}
$$

where the norm in the second definition is the restriction of the
chosen metric to the cross section `s=0`. The chain rule for Jacobians
and the gluing give

$$
\int_0^1\chi(F^t[x,0])\,dt=-\varphi(x),\qquad
\sum_{j=0}^{m-1}\varphi(\Psi^j x)=\log\Lambda_m(x)
\quad(x\in\operatorname{Fix}\Psi^m).
\tag{4.3}
$$

If a different norm on the unstable line is chosen, its ratio is a
positive continuous function `exp u(x)`, and `varphi` changes by
`u composed with Psi-u`. Its integrals against invariant measures
and its periodic sums therefore remain the same. This checks the
metric convention in (4.3) against the multipliers in (1.4).

Every F-invariant probability measure is `mu times ds` on the
measurable fundamental domain `0<=s<1`, with mu Psi-invariant.
Indeed invariance under small vertical translations makes the measure
of `E times I`, with I inside `(0,1)`, proportional to the length of I.
The proportionality constants define a probability measure mu;
invariance across the gluing gives `Psi_*mu=mu`. The section has zero
measure, since otherwise its distinct time translates would yield
arbitrarily large total mass. Conversely each such product measure
is F-invariant, including across the gluing.

On this fundamental domain `F^1=(Psi,Id)`. For finite product
partitions, the entropy of their n-fold join is the entropy of the
base n-fold join plus the fixed entropy of the vertical partition.
For the upper bound with an arbitrary finite measurable partition P,
choose a finite product-grid partition Q so that `H(P|Q)<epsilon`.
Such approximations exist because finite unions of measurable
rectangles approximate measurable sets in the product probability
space. The conditional-entropy inequality gives

`H(join_(j=0)^(n-1) (F^1)^(-j) P)`
`<=H(join_(j=0)^(n-1) (F^1)^(-j) Q)+n H(P|Q)`.

After division by n and passage to the limit this yields
`h(F^1,P)<=h_mu(Psi)+epsilon`. Let epsilon decrease to zero and take
the supremum over P. Conversely base partitions, with the vertical
factor unsplit, give the reverse inequality. Thus, without asserting
a finite generator for the identity map on the vertical interval,

$$
h_{\mu\times ds}(F^1)=h_\mu(\Psi).
\tag{4.4}
$$

Integrating (4.3) and using the cited variational principles consequently
gives, for every real t,

$$
\boxed{P_F(t\chi)=P_\Psi(-t\varphi)
=\sup_{\mu\in\mathcal M(\Psi)}
       \left(h_\mu(\Psi)-t\int\varphi\,d\mu\right).}
\tag{4.5}
$$

In particular, with `P(t)=P_Psi(-t varphi)`, equations (2.6), (4.5)
and Proposition 4.4(b) give

$$
P(0)=\log\lambda,\qquad P(1)=0.
\tag{4.6}
$$

## 5. Strict midpoint gap from the actual fixed point

### Theorem 5.1

For the fixed map specified in Section 1,

$$
\boxed{0<P_*:=P_\Psi(-\varphi/2)<{1\over2}\log\lambda.}
\tag{5.1}
$$

**Proof of the strict upper inequality.** For any invariant measure the
functional at the midpoint is the average of the two endpoint
functionals in (4.5). Thus `P_*<=log(lambda)/2`. If equality held, the
equilibrium state for `chi/2` on the suspension, which exists by
Theorem 3.3, would maximize both endpoint functionals: each endpoint
deficit is nonnegative, and their average is zero. By uniqueness it
would be the equilibrium state for chi and for zero simultaneously.
By Theorem 5.1 and Remark 5.2 of Bowen--Ruelle the former is exactly
the smooth invariant volume `m_F`.

Apply the zero-potential lower Gibbs bound at the closed flow orbit
through `[x_0,0]`, with integer `T=m`. It gives

$$
m_F(B_m([x_0,0],e))\ge c_e e^{-m\log\lambda}.
\tag{5.2}
$$

At a sufficiently small fixed e, the upper volume lemma and (4.3) give

$$
m_F(B_m([x_0,0],e))\le C_e\Lambda_0^{-m}.
\tag{5.3}
$$

Together these imply `(Lambda_0/lambda)^m<=C_e/c_e` for every m,
contrary to (1.6). Therefore the upper inequality in (5.1) is strict.
Only the one-sided Gibbs estimate actually provided by Theorem 3.3
has been used.

**Proof of positivity.** Normalize an unstable vector by first
eigen-coordinate one. Its coordinate expansion factor is greater
than 5. The chosen Riemannian norm differs from this normalization by
a bounded positive function, so

`varphi=log(coordinate expansion)+u composed with Psi-u`.

Every invariant measure therefore satisfies `integral varphi>=log 5`.
Let `mu_1` be the base measure of the equilibrium state for chi. By
`P(1)=0`, `h_(mu_1)=integral varphi dmu_1`. Evaluating the midpoint
variational functional on this measure gives `P_*>=log(5)/2>0`.
This proves (5.1). QED.

Define the positive, fixed classical number

$$
\Delta={1\over2}\log\lambda-P_*>0.
\tag{5.4}
$$

No explicit lower numerical bound on Delta is claimed here. Positivity
is strict for the exact fixed `tau`, and no limit in tau has entered
the argument.

## 6. From pressure to the complete periodic amplitude sum

Fix an expansivity constant `e_0>0` for Psi. Distinct points in
`Fix Psi^m` form an `(m,e_0)`-separated set after decreasing e_0 if
necessary: closeness for `0<=j<m` would extend by m-periodicity to
every integer j, contradicting expansivity.

The separated-set definition of topological pressure therefore gives

$$
\limsup_{m\to\infty}{1\over m}\log
\sum_{x\in\operatorname{Fix}\Psi^m}\Lambda_m(x)^{-1/2}
\le P_*.
\tag{6.1}
$$

To justify the inequality direction, the sum over these particular
separated sets is at most the supremum defining the partition sum at
radius e_0. Its logarithmic limsup is at most the pressure, which is
the limit as the radius decreases to zero. The potential sum is
`-log Lambda_m/2` by (4.3).

For each `eta>0`, definition of the limsup in (6.1), with its finite
initial range absorbed into a constant, yields

$$
\sum_{x\in\operatorname{Fix}\Psi^m}\Lambda_m(x)^{-1/2}
\le C_\eta e^{(P_*+\eta)m}
\quad\text{for every integer }m\ge1.
\tag{6.2}
$$

No periodic-orbit asymptotic, prefactor estimate, uniform spectral gap
for a varying transfer operator, or Markov coding multiplicity is
required for this upper bound.

## 7. The actual all-time quantum improvement

### Theorem 7.1

For every fixed `eta>0` there exist constants `C_eta,N_eta` such that
for all odd `N>=N_eta` and every positive integer m,

$$
\boxed{
|\operatorname{Tr}U_N^m|
\le C_\eta e^{(P_*+\eta)m}+2q_*^m.
}
\tag{7.1}
$$

**Proof.** Take square roots in (1.4), obtaining for every periodic
point the uniform bound

$$
\lambda^{-m/2}|\Gamma_h(x,m)|
\le e^{C_{\rm mod}mh^2/2}\Lambda_m(x)^{-1/2}.
\tag{7.2}
$$

Insert it into the complete exact sum (1.3), take the triangle
inequality, and use (6.2) with `eta/2`. Choose a single threshold
`N_eta` such that the original all-time formula is valid and
`C_mod h^2/2<=eta/2`. This threshold is independent of m. Then

`|P_(m,N)|<=C_(eta/2) exp((P_*+eta)m)`.

Adding the exact residual bound (1.2) proves (7.1). QED.

In particular, choosing `eta=Delta/2`, there are fixed constants
`C,N_0` and

$$
a_{\rm eff}=e^{P_*+\Delta/2}
=\sqrt\lambda\,e^{-\Delta/2}<\sqrt\lambda
\tag{7.3}
$$

such that

$$
\boxed{|\operatorname{Tr}U_N^m|\le C a_{\rm eff}^m
\quad(N\ge N_0\text{ odd},\ m\ge1).}
\tag{7.4}
$$

Here the residual is absorbed because `P_*>0` and `q_*<1`.
Unitarity may additionally replace the right side by its minimum with N.
This strict improvement below `sqrt(lambda)` is unavailable for a
smooth conjugate of the cat map: its periodic unstable multiplier is
identically `lambda^m`, and its corresponding Delta is zero.

## 8. Quantitative destruction of the bare Pell return

Let

$$
N_r={\lambda^r-\lambda^{-r}\over4\sqrt2}.
\tag{8.1}
$$

These are integers satisfying `N_0=0,N_1=1` and
`N_(r+1)=6N_r-N_(r-1)`. Modulo two this recurrence gives `N_r=r mod 2`.
Hence every odd `r>=3` gives an allowed odd dimension. Also
`log N_r/r -> log lambda`.

For context, write `S=((3,4),(2,3))=3I+2J`, where
`J=((0,2),(1,0))` and `J^2=2I`. The elementary identity
`S^r=t_r I+2N_r J`, with `t_r^2-8N_r^2=1`, implies
`S^(2r)=I mod N_r`. Exact Weyl Egorov and irreducibility then make
`M_(N_r)^(2r)` a scalar. Irreducibility here is immediate: a matrix
commuting with all diagonal characters is diagonal, and if it also
commutes with the cyclic shift then it is scalar. This explains the
bare reference time; no such return is assumed for the perturbed U.

Applying (7.4) to the actual `U_(N_r)` gives

$$
|\operatorname{Tr}U_{N_r}^{2r}|
\le C\lambda^r e^{-\Delta r}.
$$

Using `lambda^r=4sqrt(2)N_r+lambda^(-r)` and (8.1), we conclude

$$
\boxed{
{1\over N_r}|\operatorname{Tr}U_{N_r}^{2r}|
=O\left(N_r^{-\delta}\right),\qquad
\delta={\Delta\over\log\lambda}>0,
\quad r\to\infty\text{ odd}.
}
\tag{8.2}
$$

More precisely (7.1), with an arbitrarily small fixed eta, permits
every exponent `delta<2 Delta/log lambda` in (8.2), with constants
depending on delta.

This is a quantitative norm statement as well. For any unitary V,
direct expansion of the Hilbert--Schmidt norm gives

$$
\min_{|\omega|=1}{1\over N}\|V-\omega I\|_{\rm HS}^2
=2-2{|\operatorname{Tr}V|\over N}.
$$

Consequently the actual return-time matrices satisfy

$$
\boxed{
\min_{|\omega|=1}{1\over N_r}
 \|U_{N_r}^{2r}-\omega I\|_{\rm HS}^2
=2-O(N_r^{-\delta}).
}
\tag{8.3}
$$

Thus these logarithmic-time matrices are separated from every scalar
by a fixed normalized Hilbert--Schmidt distance. This is stronger than
proving that they are not exactly scalar.

## 9. The full exponential trace sum: a strict constant improvement

The positive finite frame inequality proved in
`fermionic_resolvent_frame.md`, SHA-256
`1e88189aa0192786ad4947091079efa93079aad8fe9a7194a00692c0fccb184f`,
states that any all-time bound `|p_m|<=C a^m`, `a>1`, implies

$$
\limsup_{N\to\infty\atop N\ {\rm odd}}
 {\log N\over N}
 \left[{1\over N^2}\sum_{m\ge1}e^{-2sm/N}|p_m|^2\right]
\le{\log a\over2s}\qquad(s>0).
\tag{9.1}
$$

Apply (9.1) to (7.1), with `a=exp(P_*+eta)` and its fixed threshold
`N_eta`. Since eta is arbitrary and `P_*>0`, taking eta down to zero
after the N limsup gives the actual strict inequality

$$
\boxed{
\limsup_{N\to\infty\atop N\ {\rm odd}}
 {\log N\over N}
 \left[{1\over N^2}\sum_{m\ge1}e^{-2sm/N}
                           |\operatorname{Tr}U_N^m|^2\right]
\le{P_*\over2s}<{\log\lambda\over4s}.
}
\tag{9.2}
$$

The complete infinite tail is included because the frame proof uses
the resolvent at `exp(-s/N)` strictly inside the unit disk. No tail
limit interchange is implicit here.

## 10. The first remaining estimate

The exponential pressure bound is nontrivial relative to unitarity
only for times of order `log N`. Its strict improvement does not
reach a positive fraction of the Heisenberg time. In (9.2) the bound
still allows the normalized sum to grow as `N/log N`.

The following weaker-than-universality assertion therefore remains
unproved even after the pressure argument:

$$
\sup_{N\ {\rm odd}}{1\over N^2}
\sum_{m\ge1}e^{-2sm/N}|\operatorname{Tr}U_N^m|^2<\infty
\quad\text{for one fixed }s>0.
$$

The full original goal additionally requires signed sums with every
fixed factorial order and every fixed Fourier support. None of those
long-time cancellations is inserted into the pressure proof. The new
actual conclusions are (5.1), (7.1)--(7.4), (8.2)--(8.3), and the
strict constant improvement (9.2), with their stated time ranges.

