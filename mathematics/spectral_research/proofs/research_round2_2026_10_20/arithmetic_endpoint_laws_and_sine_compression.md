> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_endpoint_laws_and_sine_compression.md`. Embedded SHA256: `8307e8bed074727caee3788adca79a44cab2fdf2627bbbfdcb2058a50863dfe1`.
> [Thematic guide](../../topics/dephasing.md).

# Exact homoclinic endpoint laws and a sine-compression identity

Research continuation, 20 October 2026. The map and quantum family are
the exact ones in the question, at the unchanged parameter
`tau=10^-80`. No averaging or replacement of that parameter occurs.

## 1. Result and scope

The probability measures in the full signed three-cell calculation
are exactly uniform in the scattering coordinates used in its phase.
Their densities need not be guessed from an informal identification
of a Gibbs state with area. A single shrinking-cylinder comparison
establishes both densities and the normalization of the resulting
integral operator.

Use the conventions of `fermionic_signed_three_cell_profile.md`.
Thus the physical map is `Psi`, the coding runs in the opposite
direction, `Psi H pi = H pi sigma^(-1)`, and the constant loop `0`
codes an interior fixed point `z_*`. The different loop `a:i->i`
is fixed. Write
$$
o=000\cdots,\qquad J=J_0,\quad A=J_a,\qquad
\mathcal T^n=\mathfrak h\nu+O((9/10)^n),
$$
with the exact positive geometric weights, and
$$
\Lambda^nJ^n\longrightarrow g\delta_o,
\quad g(o)=1,\qquad
c=\nu(Ag)(A\mathfrak h)(o)>0.
\tag{1.1}
$$
The two endpoint laws are defined on finite chronological words by
$$
P_K(w)=\frac{\nu(J_wAg)}{\nu(Ag)},\qquad
Q_K(v)=\frac{(AJ_v\mathfrak h)(o)}{(A\mathfrak h)(o)}.
\tag{1.2}
$$
The corresponding scattering coordinates are exactly the limits
specified in Section 2.1 of the signed-profile input: `S` is the
rescaled physical stable/output position and `U` the rescaled
unstable/input position, with `q-q_*` as their local coordinate.

**Theorem 1.** There are nondegenerate compact intervals
`I_S,I_U` such that
$$
\boxed{\displaystyle
\sigma=S_*P=\frac{\mathbf1_{I_S}(s)}{|I_S|}\,ds,
\qquad
\upsilon=U_*Q=\frac{\mathbf1_{I_U}(u)}{|I_U|}\,du.}
\tag{1.3}
$$
If `s_s,s_u` are the physical stable and unstable slopes at `z_*`
and `chi=s_s-s_u>0`, then
$$
\boxed{c=\chi |I_S||I_U|.}
\tag{1.4}
$$
These intervals are the images of the actual `a`-edge subarcs of the
two fixed-point leaves under their actual linearizing limits. They
are not defined by the linear cat-map lengths or by a smoothness
assumption on its topological conjugacy.

For `x>0`, let `K_(2 pi chi x)` be the operator from the signed-profile
input. Define the sine compression on a centered interval of length
`L` by
$$
(\mathsf S_L f)(y)=\int_{-L/2}^{L/2}
 \frac{\sin\pi(y-y')}{\pi(y-y')}f(y')\,dy'.
\tag{1.5}
$$
Then Theorem 1 implies the exact unitary equivalence
$$
\boxed{K_{2\pi\chi x}\simeq L^{-1}\mathsf S_L,
\qquad L=cx.}
\tag{1.6}
$$
In particular this identifies every power trace, not only the cubic
one: `Tr K^j=L^(-j) Tr S_L^j` for all integers `j>=1`.

Combining (1.6) with the full signed three-cell theorem gives, with
its `epsilon=Lambda^(-2R)`, `x_N=N epsilon` and escape constant
`kappa_esc`,
$$
\boxed{\displaystyle
E^{\rm full}_{m,N}
=\frac{m^4}{144N^3}\,
 e^{-\kappa_{\rm esc}m\varepsilon}
 \operatorname{Tr}\bigl(\mathsf S_{cN\varepsilon}^{\,3}\bigr)
+o(N),\qquad N\le m\le3N/2.}
\tag{1.7}
$$
The error is uniform in that interval, along all odd `N`.
This is an actual sine-kernel identity in one complete signed orbit
family. The complementary families in the full spectral statistic
remain unevaluated; (1.7) is not a proof of `H_diag`.

## 2. Inputs, including the geometric equilibrium theorem

The following input texts were read for this proof.

| Input | SHA-256 |
|---|---|
| `fermionic_signed_three_cell_profile.md` | `edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5` |
| `fermionic_coherent_pair_mass.md` | `dc6ff71218f427c6d4dc0da4d7c3b833d641cd7107eb43e65d9f11da4e498816` |
| `fermionic_quantitative_pressure.md` | `d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2` |
| `fermionic_pressure_transfer.md` | `90ebc84c3c9fb7c049a1a9d11e0d5dcb72c4fc89b362da3f848521a7bca79756` |
| `root_uniform_translation_contact.md` | `257afa4511da2fae8bd9260cc33a654bf045115f80aa0861bb8eae6a4f92347e` |

The geometric facts used are precise. The actual map is a smooth
area-preserving Anosov diffeomorphism, topologically conjugate to
the specified cat map. The twelve-edge Berg coding is onto, has
fibers of cardinality at most four, and codes each finite word by
one curvilinear Markov rectangle. An edge is an individual connected
crossing strip, so an edge condition on a fixed transverse plaque
cuts one interval. The loop `0` has its fixed point in the interior.
The one-sided potential `v` is the specified coboundary transform
of the negative unstable logarithm, and the positive transfer
operator has spectral radius one and the rank-one limits in (1.1).

We use the published geometric equilibrium theorem in exactly the
form already checked in Sections 3--4 of the pressure-transfer input.
The original primary article is R. Bowen and D. Ruelle, *The Ergodic
Theory of Axiom A Flows*, Invent. Math. **29** (1975), 181--202,
DOI `10.1007/BF01389848`, available at
<https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B42%5D.pdf>.
Theorem 3.3, p.187, gives uniqueness of a Hölder equilibrium state
on a basic hyperbolic set. Proposition 4.4(b), pp.189--190, gives
zero pressure for the geometric potential on an attractor. Theorem
5.1 and Remark 5.2, pp.191--192, identify this state with invariant
smooth volume for an Anosov flow. These statements were checked in
the primary PDF for this note as well.

For clarity, the map-to-flow hypotheses do not require a mixing
suspension. Its constant-roof mapping torus is smooth and compact;
the flow has no zeros and has the stable and unstable bundles of
the Anosov map together with its flow direction. Dense periodic
orbits and a dense orbit transfer from the conjugate cat map. The
whole mapping torus is a locally maximal basic set and an attractor.
The form `dq wedge dp wedge ds` glues because the map preserves
area and is flow-invariant. The input proves that invariant measures
are precisely `mu times ds`, their time-one entropies equal the base
entropies, and the integrated infinitesimal geometric potential
equals the negative base unstable logarithm up to a metric
coboundary. Thus normalized area is the unique base equilibrium
state for the negative unstable logarithm, and its pressure is zero.

The remainder of the identification of the particular transfer
measure with that area measure is proved next. Merely knowing the
periodic weights would not suffice for the endpoint normalization.

## 3. The actual transfer measure pushes forward to area

### 3.1. The normalized backward kernel

Let `Sigma^+` be the future edge space and write its left shift as
`sigma_+`. On an allowed one-sided sequence `y=e x`, put
$$
w(y)=\frac{l_{s(e)}}{\lambda l_{t(e)}}e^{v(y)},
\qquad
p(y)=w(y)\frac{\mathfrak h(y)}{\mathfrak h(x)}.
\tag{3.1}
$$
Then `sum_(sigma_+ y=x) p(y)=1`, since `T h=h`.
The probability measure
$$
d\mu^+=\mathfrak h\,d\nu
\tag{3.2}
$$
is invariant for the kernel
`Rf(x)=sum_(sigma_+y=x)p(y)f(y)`: its integral is
`nu(T(h f))=nu(h f)`.
Moreover `R(f composed with sigma_+)=f`; hence `mu^+` is
shift-invariant. For bounded functions the identity
$$
\int f(\sigma_+y)g(y)\,d\mu^+(y)
=\int f(x)(Rg)(x)\,d\mu^+(x)
\tag{3.3}
$$
follows by moving the factor `f(x)` outside the branch sum. Thus
`p` is exactly the conditional probability of the preceding edge
given the entire future.

The stationary finite word distributions give a two-sided measure
`widehat mu` by consistency. Iterating (3.3), the eigenfunction
factors telescope, so for each chronological word `w` one has
$$
\boxed{\widehat\mu([w])=\nu(J_w\mathfrak h).}
\tag{3.4}
$$
All edge weights are positive, and the logarithms in (3.1) are
bounded on each of the finitely many allowed branches.

The entropy of this stationary finite-alphabet process is
$$
h_{\widehat\mu}(\sigma)=-\int\log p\,d\widehat\mu
=-\int\log w\,d\widehat\mu.
\tag{3.5}
$$
Indeed the reverse chain rule expresses the entropy of an `n`-edge
word as the sum of the conditional entropies of each edge given
its following edges. Stationarity makes these a Cesaro average of
a decreasing sequence, converging to conditioning on the full
future. Equation (3.3) identifies that conditional law. In the
second equality of (3.5), the two `log h` terms have equal
integrals by invariance.

The `log l` part of `log w` is another shift coboundary. The
specified construction `v=-((psi_tau-log lambda) composed with pi)^+`
in the quantitative-pressure input therefore gives
$$
-\int\log w\,d\widehat\mu
=\int\psi_\tau\circ\pi\,d\widehat\mu
=\int\log J^u_{\Xi_\tau}\,d\mu_0,
\quad \mu_0=(H\pi)_*\widehat\mu,
\tag{3.6}
$$
where `Xi_tau=Psi^(-1)`. The last equality uses the already
constructed bounded metric/section coboundary for `psi_tau`.

### 3.2. No entropy is lost through the finite coding fibers

Here is an elementary entropy verification. Suppose a measurable
factor `Gamma:X->Y` of invariant probability systems has fibers
of cardinality at most `D`. For any finite partition `A` of `X`
and integer `n`, the conditional distribution of the `n`-name
given `Gamma(x)` has at most `D` possibilities. Hence
$$
H(A^{(n)}\mid\Gamma^{-1}\mathcal B_Y)\le\log D.
\tag{3.7}
$$
Choose a finite partition `B` of `Y` whose conditional entropy
is within `eta>0` of this one. Such partitions exist by increasing
finite measurable partitions generating the Borel sigma algebra
and convergence of conditional probabilities; there are only
finitely many atoms of `A^(n)`.

For `k` consecutive `n`-blocks, the entropy chain rule and the
fact that extra conditioning reduces entropy give
$$
H(A^{(kn)})\le H(B^{(kn)})
+kH(A^{(n)}\mid\Gamma^{-1}B)
\le H(B^{(kn)})+k(\log D+\eta).
\tag{3.8}
$$
After division by `kn` and passage to the limit,
`h(T,A)<=h(S)+(log D+eta)/n`. Let `n` tend to infinity
and then take the supremum over `A`. The reverse inequality
comes from pulling back finite partitions of the factor. Thus
the two entropies are equal.

Apply this argument with `Gamma=H pi`, `D=4`. Equations
(3.5)--(3.6) show
$$
h_{\mu_0}(\Xi_\tau)-\int\log J^u_{\Xi_\tau}\,d\mu_0=0.
\tag{3.9}
$$
For a two-dimensional area-preserving map the unstable logarithms
of the map and its inverse have the same invariant integrals.
To see this directly, if `alpha(x)` is the angle between unit
stable and unstable vectors, the determinant identity is
$$
J^u_F(x)J^s_F(x)\sin\alpha(Fx)=\sin\alpha(x).
$$
Also `J^u_(F^-1)(Fx)=1/J^s_F(x)`. Taking logarithms and invariant
integrals gives the assertion. Entropy likewise agrees with
that of the inverse, by shifting finite forward names to backward
names. The zero-pressure and uniqueness statement from Section 2
now applies to (3.9), and proves
$$
\boxed{(H\pi)_*\widehat\mu=dq\,dp.}
\tag{3.10}
$$

Finite cylinder images can consequently be measured by their
ordinary area. Possible coding multiplicities cause no correction:
they occur on the countable union of iterates of the Markov
spines. Each actual spine is a finite stable or unstable arc,
and each of its iterates has area zero. The preimage of this
null set has `widehat mu` measure zero by (3.10).

## 4. The endpoint coordinate intervals

### 4.1. One connected arc for each edge condition

In the linear Berg rectangle at vertex `i`, fixing all negative
edges to `0` selects the unstable plaque through the interior
fixed point. Requiring the next edge to be the individual edge
`a` selects one nondegenerate closed subinterval of this plaque:
an edge is one connected full crossing strip. Each further
finite future word cuts one closed subinterval, and intervals
for distinct words have disjoint interiors and cover the
original interval, up to their common endpoints.

Transport these arcs by `H`. A topological conjugacy sends stable
and unstable leaves to the corresponding actual leaves, since
the convergence defining them is preserved by uniform continuity
of `H` and `H^(-1)`. It also preserves the local product: an
intersection of one leaf of each kind is carried to the
corresponding unique intersection. Thus the arcs just described
are actual physical stable subarcs. Similarly, fixing the
nonnegative future to `0` and putting an edge `a` immediately
before it selects one actual physical unstable subarc. The
opposite names here reflect the inverse relation (1.1) of the
signed-profile input, not an exchange of the endpoint measures.

The actual invariant cones keep both curves nonvertical, so each
lifted compact subarc has a one-to-one `q` coordinate. The choice
of lift is the one used for the homoclinic tails; after enough
zero iterates every point is in the common chart of `z_*`.

### 4.2. Strictly monotone linearizing limits

For either curve, in the time direction toward `z_*`, its local
`q-q_*` map is
$$
f(t)=\Lambda^{-1}t+O(t^2),\qquad
f'(t)=\Lambda^{-1}+O(t).
\tag{4.1}
$$
The tail calculation in the input gives
`|f^n(t)|<=C Lambda^(-n)|t|` uniformly on a sufficiently small
interval. Therefore the functions `Lambda^n f^n(t)` converge
uniformly, and their derivatives are the products
$$
\Lambda^n(f^n)'(t)
=\prod_{j=0}^{n-1}\Lambda f'(f^j(t)).
\tag{4.2}
$$
Shrink the interval once so these factors are positive and
bounded away from zero. The sums of their logarithms converge
uniformly because their deviations from one are bounded by
`C Lambda^(-j)|t|`. The derivative products converge uniformly
to a continuous, strictly positive function. Consequently the
limit is `C^1`, strictly increasing, and has derivative one at
zero. The already proved common finite entry time extends this
conclusion to each compact edge subarc, by composing with a fixed
diffeomorphism and multiplying by a fixed power of `Lambda`.

The images of the stable and unstable `a`-subarcs under these
limits are the nondegenerate intervals `I_S,I_U`. By the exact
indexing in the signed-profile input, these are precisely the
ranges of its `S,U`, with no additional one-step scaling.
For fixed finite words write their subintervals as
`I_S(w),I_U(v)`. Their maximum diameter tends to zero as the
word length tends to infinity, using the input estimate
`C lambda^(-K/2)` for the scattering functions.

## 5. A shrinking-cylinder calculation fixes both densities

### 5.1. Exact centered word and its transfer mass

Let `C_R(w,v)` be the two-sided cylinder whose chronological
central block is
$$
v\ a\ 0^{2R}\ a\ w,
\tag{5.1}
$$
viewed at the midpoint of its `2R` zeros. There are exactly `R`
zero edges on either side of the cut. The word `w` is the fixed
future prefix after the right `a`, and `v` is the fixed past
suffix before the left `a`. Write `C_R` if both refinements
are empty.

Since `J_word` reverses the chronological factor order, (3.4)
gives the exact formula
$$
\widehat\mu(C_R(w,v))
=\nu(J_w A J^{2R} A J_v\mathfrak h).
\tag{5.2}
$$
The normalized zero-branch limit in (1.1), at these fixed words,
then proves
$$
\begin{split}
\Lambda^{2R}\widehat\mu(C_R)&\longrightarrow c,\\
\Lambda^{2R}\widehat\mu(C_R(w,v))
&\longrightarrow
\nu(J_wAg)(A J_v\mathfrak h)(o)\\
&=cP_K(w)Q_K(v).
\end{split}
\tag{5.3}
$$
The left and right refinements can also have different fixed
lengths; the same formula applies. This step displays all
boundary factors, rather than absorbing any into a proportionality
constant.

### 5.2. The actual local product has the required area Jacobian

The actual stable and unstable foliations have `C^1` local
product charts here. This does not assert that `H` is `C^1`.
For the stable foliation of `Xi_tau` (the physical unstable one),
the graph construction in Section 2 of
`root_uniform_translation_contact.md` gives a `C^1` base-dependent
family of graphs in one fixed holomorphic disk: its graph
contraction is less than `1/25` and its differentiated contraction
less than `6/25`. The same construction applies after interchanging
the eigendirections and replacing the map by its inverse. The
inverse is again an analytic perturbation of the inverse cat map,
its first derivative has norm less than six in the same swapped
coordinates, and the perturbation derivatives remain much smaller
than the reserved graph-transform bounds. These follow directly
from `Xi_tau=S Phi_tau`, `Xi_tau^(-1)=Phi_(-tau) S^(-1)` and the
flow bounds already used in that input. Thus both needed graph
families are `C^1` in their real base points.

Let `z_s(t)` and `z_u(u)` denote the two local fixed-point curves,
parametrized by their horizontal displacement, so
$$
z_s(0)=z_u(0)=z_*,\qquad
z_s'(0)=(1,s_s),\quad z_u'(0)=(1,s_u).
$$
Define `B(t,u)` to be the intersection of the local unstable
leaf through `z_s(t)` with the local stable leaf through
`z_u(u)`. The `C^1` graph families and the nonparallel tangent
vectors give a `C^1` map by the two-variable implicit-function
argument. It obeys
$$
B(t,0)=z_s(t),\qquad B(0,u)=z_u(u),\qquad
|\det DB(0,0)|=s_s-s_u=\chi.
\tag{5.4}
$$
In particular its absolute Jacobian converges uniformly to `chi`
as `(t,u)` tends to zero.

The image of `C_R(w,v)` is exactly a product rectangle in this
chart. Its projection onto the fixed stable curve is obtained
by replacing the past of the middle cut by all zeros. The
remaining future is `0^R a w ...`, so its projected horizontal
coordinates are exactly the stable-tail coordinates used to
define `S`. Its projection onto the unstable curve is obtained
by replacing the future by all zeros; the remaining past is
`... v a 0^R`, giving exactly `U`. This is also immediate in
the linear coding by concatenating past and future, and is
transported to the actual product by `H`.

Let `I_(S,R)(w)` be `Lambda^R` times the horizontal-coordinate
interval of the first projection, and define `I_(U,R)(v)`
similarly. Section 4 gives convergence of their endpoints to
those of `I_S(w),I_U(v)`. They remain in one fixed bounded
interval. Therefore, using (3.10), the ordinary change of
variables in the `C^1` chart gives
$$
\begin{split}
\Lambda^{2R}\widehat\mu(C_R(w,v))
={}&\int_{I_{S,R}(w)\times I_{U,R}(v)}
 |\det DB(\Lambda^{-R}s,\Lambda^{-R}u)|\,ds\,du\\
\longrightarrow{}&\chi |I_S(w)||I_U(v)|.
\end{split}
\tag{5.5}
$$
Boundaries are null by Section 3, so using closed rectangles
does not change this equality. No conditional measure on a
null infinite-tail event has been invoked.

### 5.3. Comparison and passage to the full endpoint measures

Comparing (5.3) and (5.5) first with empty refinements proves
$$
c=\chi |I_S||I_U|.
\tag{5.6}
$$
Refining only one side then gives
$$
P_K(w)=\frac{|I_S(w)|}{|I_S|},\qquad
Q_K(v)=\frac{|I_U(v)|}{|I_U|}.
\tag{5.7}
$$
For each `K`, these intervals partition the corresponding full
interval up to endpoints. Their mesh tends to zero. Approximate
a continuous function of `S` by one selected value in each
prefix cylinder. The integral error is bounded by its modulus
of continuity at that mesh, both for `P` and for normalized
Lebesgue measure on `I_S`. Equation (5.7) makes the approximating
integrals identical. Let the mesh tend to zero. The same
argument for `U` proves (1.3).

This completes the proof of Theorem 1, including all multipliers
in (1.4). In particular the factors `g` and `h` in (1.2) do not
produce an additional density tilt in these scattering coordinates.

## 6. Exact sine compression and cancellation of the density constants

Put `a_S=|I_S|`, `a_U=|I_U|`, and let `bar s,bar u` be the interval
midpoints. From (1.3), the kernel relative to `d sigma=ds/a_S` is
$$
\begin{split}
k_{2\pi\chi x}(s,s')
&=\frac1{a_U}\int_{I_U}e^{2\pi i\chi x(s-s')u}\,du\\
&=e^{2\pi i\chi x\bar u(s-s')}
 \frac{\sin\bigl(\pi\chi x a_U(s-s')\bigr)}
      {\pi\chi x a_U(s-s')}.
\end{split}
\tag{6.1}
$$
Multiplication by `exp(-2 pi i chi x bar u s)` removes the
first phase by unitary conjugation. Set
$$
d=\chi x a_U>0,\qquad y=d(s-\bar s),\qquad
L=d a_S=\chi x a_Sa_U=cx.
\tag{6.2}
$$
The map `f(s) -> L^(-1/2) f(bar s+y/d)` is unitary from
`L^2(I_S,ds/a_S)` to `L^2([-L/2,L/2],dy)`. Under this change,
the remaining kernel is exactly `L^(-1)` times (1.5). This
proves (1.6), with no factor of `2 pi` remaining in the interval
length.

The sine compression is positive and trace class. One direct
verification is to write it as `B_L^*B_L`, where
$$
(B_L f)(\xi)=\int_{-L/2}^{L/2}e^{-2\pi i\xi y}f(y)\,dy,
\qquad -1/2\le\xi\le1/2.
$$
This is Hilbert--Schmidt, with squared norm `L`, so
`Tr S_L=L`. The power-trace identities in Section 1 follow
from unitary equivalence.

The prefactor in the signed-profile theorem is `c_*=c^3`.
Using `L=cN epsilon` gives the exact cancellation
$$
c^3m^4\varepsilon^3\operatorname{Tr}(K^3)
=\frac{m^4}{N^3}\operatorname{Tr}(\mathsf S_{cN\varepsilon}^3).
\tag{6.3}
$$
Thus (1.7) follows with precisely its coefficient `1/144`.
For a fixed continuous weight `w` on `[1,3/2]`, the corresponding
pair-scale formula is
$$
\boxed{\begin{aligned}
\frac1{N^2}\sum_{N\le m\le3N/2}w(m/N)E^{\rm full}_{m,N}
={}&\frac1{144}\operatorname{Tr}
       (\mathsf S_{c x_N}^{\,3})\\
&\quad\times\int_1^{3/2}w(v)v^4
       e^{-\kappa_{\rm esc}x_Nv}\,dv+o(1).
\end{aligned}}
\tag{6.4}
$$
The bounded rounding parameter `x_N` remains in this expression;
it need not converge.

## 7. The remaining spectral task

Theorem 1 identifies the actual endpoint densities and produces
an actual sine compression in a signed family at times of order
`N`. It does not rely on a smooth conjugacy to the cat map, on
random phases, or on replacing the geometric potential by a
constant potential. Its normalization comes from equality of
two computations of the same finite symbolic cylinders.

The first unproved spectral step is still the cancellation in
the complete weighted off-diagonal trace sum, including the
complement of this three-cell family, and then the analogous
all-order factorial expressions. The positive term (6.4) must
be included in that calculation. The identity of its integral
kernel with a sine compression does not evaluate the other
terms and does not by itself imply convergence of the full
point process.
