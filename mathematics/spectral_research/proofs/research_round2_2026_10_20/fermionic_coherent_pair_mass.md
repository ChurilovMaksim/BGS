> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_coherent_pair_mass.md`. Embedded SHA256: `dc6ff71218f427c6d4dc0da4d7c3b833d641cd7107eb43e65d9f11da4e498816`.
> [Thematic guide](../../topics/histories.md).

# A nonvanishing class of coherent off-diagonal pairs for the actual map

Research continuation, 20 October 2026. The quantum family, the
fixed value `tau=10^-80`, and the restriction to all odd dimensions
are unchanged.

## The result and its exact scope

For every sufficiently large odd N and every integer
`N<=m<=3N/2`, this note constructs a finite set of pairs of
**different primitive geometric orbits** of the actual nonlinear
map, both of period m. In the exact principal trace formula let
`a_(p,N)` be the weight of one point of a primitive orbit p. Define
the sum of the selected ordered cross terms by

$$
 E_{m,N}=\sum_{(p,p')\in\mathcal A_{m,N}}
               2m^2\operatorname{Re}(a_{p,N}\overline{a_{p',N}}),
 \tag{T.1}
$$

where the construction below takes each unordered orbit pair
exactly once. There are constants c,C>0, independent of m,N, such
that

$$
 \boxed{cN\le E_{m,N}\le CN
       \qquad(N\le m\le3N/2, N\text{ sufficiently large odd}).}
 \tag{T.2}
$$

Every summand in (T.1) is positive. For the fixed admissible test
`b_*` used in the previous pair calculation, with
`w=|bhat_*|^2>0` on `(-2,2)`, it follows that

$$
 \boxed{\displaystyle
 \liminf_{N\to\infty\atop N\text{ odd}}
  \frac1{N^2}\sum_{N\le m\le3N/2}w(m/N)E_{m,N}>0.}
 \tag{T.3}
$$

Thus this particular class has nonvanishing mass at the requested
pair-statistic scale. It is a **subsum** of the full signed
off-diagonal expression. It is not a lower bound for that full
expression: the omitted terms have no established sign. Neither
`H_diag` nor its negation is proved here.

The proof uses three ingredients specific to the already established
representation of the actual family: its exact local prequantum
phase, uniform concavity of the exact generating function, and the
explicit positive transfer operator for the actual unstable
Jacobian. No random phases or parameter averages are inserted.

## 1. Frozen inputs and notation

| Input | SHA-256 |
|---|---|
| `fermionic_homoclinic_and_doubled_transfer.md` | `85e74eda0116dbbda1e3ba7a1028fbeb36da97072b7a92b3addc5d3004024168` |
| `fermionic_quantitative_pressure.md` | `d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2` |
| `fermionic_deck_action_differencing.md` | `8202c59cbe0b9eb69a022ac1997dccaf00b1ae99fc611cf95308a926f7b2b140` |
| `../research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` |
| `../research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |

The first input has been independently audited by the root agent.
The other inputs carry their previously recorded independent
audits. We use their actual statements, summarized precisely here.

Let `S=[[3,4],[2,3]]`, `L=S^(-1)`, and
`lambda=3+2sqrt(2)`. The twelve-edge shift Sigma has incidence

$$
 \begin{pmatrix}3&2\\4&3\end{pmatrix}
$$

and a factor map pi with `pi sigma=S pi`. The actual conjugacy H
gives `Psi H pi=H pi sigma^(-1)`. If central words agree for n
edges in each direction, then

$$
 d(H\pi x,H\pi y)\le C\lambda^{-n/2}.
 \tag{1.1}
$$

The periodic point `(1/2,0)` of S is interior to the Berg
partition and has a constant loop itinerary 0, at a vertex i.
Fix a different i-to-i loop a. Write `z_*=(q_*,p_*)` for a chosen
lift of its actual image `H(1/2,0)`, and write

$$
 \Lambda>5
 \tag{1.2}
$$

for the positive unstable multiplier of Psi at this fixed point.
The stable multiplier is `Lambda^(-1)` by area preservation.
All these choices are fixed independently of N,m.

The exact real generating function is

$$
 F(Q,q)=-(3Q^2-2Qq+3q^2)/8+G(Q,q),\qquad
 p=-F_q,\quad P=F_Q.
 \tag{1.3}
$$

All second derivatives of G are smaller than `10^-70` in absolute
value, uniformly on the real plane. The scalar trace cocycle is
globally defined and satisfies

$$
 \sup_{0<h<h_0}\|\log\gamma_h\|_{C^{1/2}}<\infty,
 \qquad h=(2\pi N)^{-1}.
 \tag{1.4}
$$

For a primitive orbit p of period m,

$$
 a_{p,N}=\zeta_N^m\lambda^{-m/2}\omega_{p,N}\Gamma_h(p,m),
 \qquad\Gamma_h(p,m)=\prod_{j<m}\gamma_h(\Psi^j p).
 \tag{1.5}
$$

The exact modulus comparison is

$$
 \left|\log\bigl(|a_{p,N}|^2\Lambda_p\bigr)\right|
       \le Cmh^2,
 \tag{1.6}
$$

where Lambda_p is its positive unstable multiplier. In particular
`|a_(p,N)|^2=(1+O(N^-1)) Lambda_p^(-1)` uniformly for `m<=2N`.

Finally, the quantitative-pressure input supplies a real one-sided
Holder potential v on the future edge space, with parameter
`theta=2/3`, and an operator

$$
 (\mathcal T f)(x)=
  \sum_{e:j\to i(x)}\frac{l_j}{\lambda l_{i(x)}}
                  e^{v(ex)}f(ex),
 \qquad l=(\sqrt2,1).
 \tag{1.7}
$$

It has spectral radius one and an explicitly isolated positive
rank-one part:

$$
 \mathcal T^n=\mathfrak h\nu+O_{C_\theta\to C_\theta}((9/10)^n),
 \qquad \mathfrak h>0,\quad\nu(1)=\nu(\mathfrak h)=1.
 \tag{1.8}
$$

The function `mathfrak h` is distinct from the Planck parameter h
in (1.4)--(1.6). The functional nu is positive. Indeed T is positive,
its powers converge to `mathfrak h nu`, and that eigenfunction is
strictly positive. This also proves
`sup_n||T^n||<infinity`. The small perturbation bound in the input
ensures positive nu mass for both vertex cylinders. This last
fact also follows directly from invariance and the positive
incidence matrix.

For every periodic code x of period m, the exactly checked
coboundary relation gives

$$
 \lambda^{-m}\exp\left(\sum_{j<m}v(\sigma^jx)\right)
 =\Lambda_{H\pi x}^{-1}.
 \tag{1.9}
$$

The right side is for the inverse map Psi; in dimension two its
periodic unstable multiplier equals that of the forward map
Xi_tau on the same periodic orbit. At the fixed code `o=000...`,

$$
 \lambda^{-1}e^{v(o)}=\Lambda^{-1}.
 \tag{1.10}
$$

## 2. Sharp homoclinic tails with the exact multiplier Lambda

We need a tail rate `Lambda^(-R)`, not a weakened fixed rate such
as `5^(-R)`. The latter would lose a power of N in the count.
Here is an elementary proof with uniform constants over all the
finite excursion words used below.

For any finite i-to-i word u, consider the two-sided code
`0^infinity a u a 0^infinity`. Its linear image is homoclinic to
`(1/2,0)`, and its actual image is homoclinic to z_*. Equation
(1.1) gives a common bound `C lambda^(-j/2)` on both tails,
independent of the word and its length. After a common number of
tail steps every one of these points is inside any fixed small
neighborhood of z_*.

We improve this bound locally. Subtract the fixed winding of z_*
from the lift of Psi and use its real eigen coordinates. The
resulting local map is

$$
 F_*(y)=Dy+R(y),\qquad
 D=\operatorname{diag}(\Lambda,\Lambda^{-1}),
 \quad R(0)=DR(0)=0.
 \tag{2.1}
$$

All local derivatives required here are bounded, since the
actual map is analytic. For clarity, a local unstable curve can
be constructed without invoking a smooth structural conjugacy.
Use the Banach space of backward sequences
`x_n=(u_n,v_n)`, n>=0, with norm `sup_n 2^n|x_n|`.
Fix the first unstable coordinate u_0. A backward orbit converging
to zero satisfies, and is characterized by,

$$
 u_n=\Lambda^{-n}u_0
       -\sum_{j=1}^n\Lambda^{-(n-j+1)}R_u(x_j),
 \qquad
 v_n=\sum_{j\ge1}\Lambda^{-(j-1)}R_v(x_{n+j}).
 \tag{2.2}
$$

Substitution into `F_*(x_n)=x_(n-1)` verifies both formulas and
their converse. The two convolution norms are at most
`1/(Lambda-2)` and `1/(2-Lambda^(-1))`. On a sufficiently small
ball the Lipschitz constant of R makes (2.2) a strict contraction,
uniformly for u_0 in a fixed small interval. It preserves a fixed
multiple of that interval in the sequence norm. Its solution is
C^2 in u_0: differentiate the contraction equation, invert its
linearized operator by the uniformly convergent Neumann series,
and differentiate once more. The bounded second derivative of R
makes the second differentiated equation bounded in the same
weighted space. At u_0=0 the derivative is
`x_n'=(Lambda^(-n),0)`, since DR(0)=0.

Thus the selected curve is `v_0=b(u_0)`, with b(0)=b'(0)=0 and
`b(u)=O(u^2)`. Every sufficiently small backward orbit with the
previous `lambda^(-n/2)` bound belongs to this curve by uniqueness
in the weighted space, because `2<sqrt(lambda)`.

On this curve the backward scalar map consequently has the form

$$
 u_{n+1}=\Lambda^{-1}u_n+O(u_n^2).
 \tag{2.3}
$$

Shrink the neighborhood so that also
`|u_(n+1)|<=|u_n|/2`. The ratios in (2.3), whenever u_n is
nonzero, give

$$
 |u_n|\le\Lambda^{-n}|u_0|
             \exp\left(C\sum_{j<n}|u_j|\right)
       \le C\Lambda^{-n}|u_0|.
 \tag{2.4}
$$

If one u_j is zero the same conclusion is immediate. Since
`v_n=b(u_n)=O(u_n^2)`, this is also a bound for the full vector.
Apply the same construction to the inverse map for the stable
tail. The common entry time into the small neighborhood is
absorbed into the constant. We have proved

$$
 \boxed{\text{both endpoint distances of }
       0^R a u a0^R\text{ from }z_*
       \text{ are at most }C\Lambda^{-R}.}
 \tag{2.5}
$$

The endpoints here are those of its homoclinic extension. The
constant is independent of u, its length, and R. This argument
uses smoothness only near one fixed point, where it is available.

## 3. The exact block action and its quadratic order error

### 3.1. Boundary functions, including the deck gauge

A cell e is a word `0^R a u a0^R`, with length d. The physical map
Psi traverses this S-coded cell **backwards**, because
`Psi H pi=H pi sigma^(-1)`. Its input is the right coded endpoint
and its output is the left coded endpoint. In particular q_in
below is the right endpoint position and q_out the left endpoint
position. A whole coded cyclic concatenation is also traversed in
reverse order. Two permutations of coded cells are still two
permutations of exactly the same backward physical branches; all
the comparisons below concern those physical branches.

Assign to e the deck displacement n_e of this actual lifted branch
from its chosen initial chart near z_* to its final chart near z_*.
This integer is fixed by the finite edge word: the exact lift
conjugacy transports the constant deck labels of the linear
rectangular coding. It is the same integer for the homoclinic
extension and for any periodic concatenation of that cell.

For boundary position coordinates q_in,q_out, let

$$
 W_e(q_{\rm out},q_{\rm in})
 =\operatorname*{crit}_{q_1,\ldots,q_{d-1}}
       \sum_{j=0}^{d-1}F(q_{j+1},q_j)
        -(n_e)_p q_{\rm out},
 \quad q_0=q_{\rm in},\quad
 q_d=q_{\rm out}+(n_e)_q.
 \tag{3.1}
$$

The critical point is unique. Indeed the negative Hessian of the
full open-chain action is bounded below by a fixed positive
multiple of the identity: the unperturbed endpoint diagonal
entries are 3/4, internal entries are 3/2, and neighboring
off-diagonal entries have magnitude 1/4. The perturbations from
G are less than `10^-69` in each row sum. Gershgorin's inequality,
or the direct quadratic form bound, gives

$$
 (0.49)I\le- D^2\!\left(\sum F\right)\le(2.01)I.
 \tag{3.2}
$$

The action is coercive toward minus infinity in the internal
positions because G is bounded. Smooth dependence and elimination
of the internal variables therefore give a global boundary
function W_e. Its negative Hessian is the Schur complement of
the open-chain negative Hessian. For a positive matrix between
cI and CI, that Schur complement is also between cI and CI:
its inverse is the corresponding principal block of the full
inverse. Consequently

$$
 0.49I\le-D^2W_e\le2.01I,
 \tag{3.3}
$$

uniformly in the cell length and the deck displacement. This
also covers a one-edge cell directly, although our cells are long.
The linear deck term in (3.1) has no effect on these Hessians.
The endpoint derivatives are exactly

$$
 \partial_{q_{\rm out}}W_e=p_{\rm out},\qquad
 -\partial_{q_{\rm in}}W_e=p_{\rm in},
 \tag{3.4}
$$

where the output momentum has been reduced by `(n_e)_p` into
the final chart.

For odd N the full prequantum phase of this branch is
`exp(i W_e/h)`. To check that this retains every constant, the
previous audited Landau gauge is

$$
 (z,u)\sim(z+n,e^{i n_pq/h}u),\qquad
 (z,u)\longmapsto(\Psi z,e^{iF(Q,q)/h}u).
 \tag{3.5}
$$

Its equivariance is the exact phase deck identity, whose remaining
constant `(ca-db)/2` is an integer because `L=I mod2`. Reducing
only after d steps gives precisely (3.1). Reducing at intermediate
steps gives the same scalar. On a closed orbit the original
half-winding term and `(-1)^(n_q n_p)` cancel exactly for odd N.
Thus concatenating and permuting cells introduces no unrecorded
half phase, deck sign, or Maslov scalar. The common scalar
`zeta_N^m` is separate and identical for the two full orbits.

### 3.2. Stationarity makes the error quadratic

On the homoclinic extension of e, both endpoint states are within
`C Lambda^(-R)` of z_* by (2.5). Comparing their boundary positions
with `(q_*,q_*)` and using (3.3)--(3.4) proves

$$
 \big|\partial_{q_{\rm out}}W_e(q_*,q_*)-p_*\big|
 +\big|\partial_{q_{\rm in}}W_e(q_*,q_*)+p_*\big|
       \le C\Lambda^{-R}.
 \tag{3.6}
$$

Take any n cells, and put their boundary positions around a cycle.
The sum of their functions (3.1) has negative Hessian at least
`0.98 I`: each cut coordinate occurs at two cell endpoints, and
(3.3) applies to every pair of endpoints. Its gradient at the
constant cut vector `(q_*,...,q_*)` has each component at most
`C Lambda^(-R)`, because the p_* terms in (3.6) cancel. Thus its
gradient squared is at most `C n Lambda^(-2R)`.

For a differentiable function S with `D^2S<=-cI`, the exact
inequality

$$
 0\le\max S-S(x_0)\le\frac{|DS(x_0)|^2}{2c}
 \tag{3.7}
$$

follows by maximizing
`S(x_0)+DS(x_0)(x-x_0)-c|x-x_0|^2/2`. Apply this with the actual
critical cut vector. To identify it, first take the known periodic
point of the concatenated code and traverse its cells in the
physical reverse order. The two-sided zero buffers and (1.1)
place every cut in the same fixed chart near z_* for all large R.
The inverse edge labels are constant on each coded strip and are
transported by the exact equivariant lift conjugacy, so each
finite cell word has exactly the same total n_e as its homoclinic
extension. Hence its physical lifted segment is the stationary
internal path in (3.1), with precisely that branch and those
endpoints. Its endpoint momenta agree by (3.4), so the cut vector
is critical for the sum of the W_e. Uniqueness of the eliminated
paths and of the critical cut vector now gives the required
identification.

The value at the constant cut vector is
`sum_e W_e(q_*,q_*)`, independent of the order of the cells.
Therefore any two permutations give exact orbit actions with

$$
 \boxed{|\mathcal S_w-\mathcal S_{w'}|
                \le C_{\rm act} n\Lambda^{-2R}.}
 \tag{3.8}
$$

Here the actions mean the sums of the exact local Landau boundary
functions. Their exponentials are the full orbit phases by (3.5).
This is the quadratic error used below. It has no factor equal
to the lengths of the cells.

## 4. The scalar amplitude has a localized boundary error

The first frozen input proves a two-sided coded variation bound

$$
 |\log\gamma_h(H\pi x)-\log\gamma_h(H\pi y)|
       \le C\theta^k,\qquad\theta=2/3,
 \tag{4.1}
$$

when the central k edges agree, uniformly for all sufficiently
small h. This uses the genuine fractional regularity (1.4), not
spatial analyticity of an invariant section.

Match equal cells between two permutations, and match positions
of equal offset inside each cell. If a cell has length d and the
offset is j, its two coded sequences agree on a central block of
radius at least

$$
 R+\min(j,d-1-j),
$$

up to one fixed indexing adjustment. Inside the matched cell
they coincide. Beyond either boundary the neighboring cell has
R zero edges, regardless of its interior word. The adjustment
is absorbed in the variation constant. Summing (4.1) over one
cell consequently costs at most

$$
 C\theta^R\sum_{j=0}^{d-1}\theta^{\min(j,d-1-j)}
       \le\frac{2C}{1-\theta}\theta^R.
$$

For n cells this proves the uniform, length-independent estimate

$$
 \boxed{\displaystyle
 \left|\log\frac{\Gamma_h(w)}{\Gamma_h(w')}\right|
                   \le C_\gamma n\theta^R.}
 \tag{4.2}
$$

The logarithm denotes the difference of sums of the fixed local
branches of `log gamma_h`; exponentiation is exact. Multiplication
of scalar factors permits the matching permutation. It does not
require the sequence order of the two trajectories to agree.

For n=3 choose, once and for all, an integer R_0 large enough
that the action error below is less than 1/20, and set

$$
 R=R_N=\left\lceil\frac{\log N}{2\log\Lambda}\right\rceil+R_0.
 \tag{4.3}
$$

Equation (3.8) gives
`|omega_w/omega_(w')-1|<=6 pi C_act N Lambda^(-2R)`.
Increasing R_0 if needed makes this at most 1/20, uniformly in N.
Equation (4.2) tends to zero uniformly in the cell lengths.
Thus for all sufficiently large odd N,

$$
 \left|a_{w,N}/a_{w',N}-1\right|<1/4.
 \tag{4.4}
$$

In particular their ordered pair of cross terms is positive and,
with harmless fixed bounds,

$$
 \tfrac12 m^2\Lambda_w^{-1}
 \le2m^2\operatorname{Re}(a_{w,N}\overline{a_{w',N}})
 \le8m^2\Lambda_w^{-1}
 \qquad(m\le2N).
 \tag{4.5}
$$

We used (1.6) to replace the exact modulus by the actual unstable
Jacobian weight. All errors here are uniform over every word in
the class to be counted.

## 5. A positive transfer calculation for long zero markers

For an individual edge e define its prefix operator on the future
Holder space by

$$
 (J_e f)(x)=\mathbf1_{i(x)=t(e)}
        \frac{l_{s(e)}}{\lambda l_{t(e)}}e^{v(ex)}f(ex).
 \tag{5.1}
$$

Then `T=sum_e J_e`. In products the rightmost operator supplies
the earliest edge of the prefixed word; this convention follows
by applying (5.1) twice. Put `J=J_0`, `A=J_a`, and `o=000...`.

### 5.1. The normalized zero branch has a rank-one limit

For x in vertex i,

$$
 \Lambda^k(J^k f)(x)
 =g_k(x)f(0^kx),\qquad
 g_k(x)=\exp\left(\sum_{j=1}^k[v(0^jx)-v(o)]\right).
 \tag{5.2}
$$

Outside that vertex cylinder both sides are zero. The Holder norm
of the jth summand in the exponent is at most `C theta^j`, on
the vertex cylinder; extension by zero to the other vertex costs
only a fixed constant. This follows directly by prefixing j equal
edges in the variation seminorm. Thus g_k converges in the Holder
norm to a function g, strictly positive and bounded away from
zero on vertex i. Also `g(o)=1`.

The function `f(0^kx)-f(o)` has Holder norm at most
`C theta^k||f||_theta` on this vertex cylinder. Hence, with
`delta_o f=f(o)` and g extended by zero,

$$
 \boxed{\displaystyle
 \|\Lambda^kJ^k-g\delta_o\|_{C_\theta\to C_\theta}
                    \le C\theta^k,\qquad k\ge1.}
 \tag{5.3}
$$

In particular the norms of all normalized zero-branch powers are
uniformly bounded. Evaluation at o gives the exact identity
`(J^k f)(o)=Lambda^(-k)f(o)`.

### 5.2. Open words and periodic weights differ by a vanishing factor

Consider the word

$$
 w=0^R a u_1 a0^{2R}a u_2 a0^{2R}a u_3 a0^R,
 \tag{5.4}
$$

where each u_j is an arbitrary i-to-i path of length ell_j.
Its length is

$$
 m=6R+6+\ell_1+\ell_2+\ell_3.
 \tag{5.5}
$$

The periodic future `www...` and the open future `w000...` agree
for at least m+R edges. At their jth shifts they therefore agree
for at least m+R-j edges. The difference of their v sums over
one word is at most

$$
 C\sum_{j=0}^{m-1}\theta^{m+R-j}\le C'\theta^R.
 \tag{5.6}
$$

The Perron-vector factors of the branch weight telescope to
`lambda^(-m)` because the word starts and ends at i. Equations
(1.9) and (5.6) show that its open branch weight differs from its
actual periodic multiplier weight `Lambda_w^(-1)` by a factor
between `exp(-C theta^R)` and `exp(C theta^R)`. This comparison
is uniform over all interiors u_j and all their lengths.

The sum of these open weights, at fixed ell_1,ell_2,ell_3, is
exactly

$$
 Z^{\rm open}_{R,\boldsymbol\ell}=
 [J^R A\mathcal T^{\ell_3}A J^{2R}
       A\mathcal T^{\ell_2}A J^{2R}
       A\mathcal T^{\ell_1}A J^R1](o).
 \tag{5.7}
$$

The A factors force each unrestricted interior path to start and
end at vertex i. This formula also specifies the order of every
prefix operator in the count.

### 5.3. Uniform upper bound and the long-gap lower bound

From (1.8), (5.3), and the boundedness of A,

$$
 Z^{\rm open}_{R,\boldsymbol\ell}\le C\Lambda^{-6R}
 \quad\text{for every }\ell_j\ge0.
 \tag{5.8}
$$

If each ell_j is at least epsilon m for a fixed epsilon>0, insert
the rank-one limits (1.8) and (5.3) into (5.7). Normalizing each
J power first keeps all factors uniformly bounded, so the
replacement errors are bounded by
`C(theta^R+(9/10)^(epsilon m)) Lambda^(-6R)`.
The leading constant is explicitly

$$
 c_*=[\nu(A g)\,(A\mathfrak h)(o)]^3>0.
 \tag{5.9}
$$

To see the cube, start at the right of (5.7), replace `J^R1` by
`Lambda^(-R)g`, every long T power by `mathfrak h nu`, and each middle
zero branch by `Lambda^(-2R)g delta_o`; the leftmost evaluation
of J^R supplies its exact final factor. Positivity of every factor
and the positive vertex mass of nu prove the strict inequality.
Thus the sum Z of actual periodic multiplier weights satisfies

$$
 \boxed{\displaystyle
 Z_{R,\boldsymbol\ell}
 =\Lambda^{-6R}
  [c_*+O(\theta^R+(9/10)^{\varepsilon m})],
 \qquad \min\ell_j\ge\varepsilon m.}
 \tag{5.10}
$$

This is a weighted count for the actual nonlinear unstable
Jacobian. It is not a count with unperturbed amplitudes.

### 5.4. Excluding additional markers without losing the mass

Call a word in (5.4) good when its only cyclic occurrences of a
run of at least 2R zero edges are its three displayed runs.
Each displayed run is exactly 2R long and is flanked by the
nonzero edge a. Any additional run must therefore lie wholly
inside an interior u_j. For a specified possible start of a
length-2R run inside that interior, replace the corresponding
T power in (5.7) by a product

$$
 \mathcal T^b J^{2R}\mathcal T^c,\qquad b,c\ge0.
$$

There is one extra normalized zero branch. Uniform bounds for all
T powers and (5.3) therefore bound the total open weight for that
event by `C Lambda^(-8R)`. The same bound holds for periodic
weights by (5.6). There are at most m possible starts, and all
weights are positive. The elementary union bound consequently
gives

$$
 Z^{\rm bad}_{R,\boldsymbol\ell}\le C m\Lambda^{-8R}.
 \tag{5.11}
$$

Increase the fixed R_0 in (4.3), if necessary, so that
`C(3/2) Lambda^(-2R_0)<c_*/4`. Since
`m<=3N/2` and `N Lambda^(-2R)<=Lambda^(-2R_0)`, equations
(5.10)--(5.11) now show, for all sufficiently large N,

$$
 \boxed{\displaystyle
 c_1\Lambda^{-6R}
  \le Z^{\rm good}_{R,\boldsymbol\ell}
  \le C_1\Lambda^{-6R},
 \qquad \min\ell_j\ge\varepsilon m.}
 \tag{5.12}
$$

The constants are strictly positive and independent of m,N and
the chosen lengths. This choice of R_0 is compatible with the
earlier phase condition: both require only that the same fixed
integer be sufficiently large.

## 6. Counting primitive pairs without cyclic overcounting

For each m in the specified interval, choose integer lengths in
the bands

$$
 \frac m8\le\ell_1\le\frac m6,\qquad
 \frac m4\le\ell_2\le\frac m3,\qquad
 \ell_3=m-6R-6-\ell_1-\ell_2.
 \tag{6.1}
$$

Since R=O(log N) and m is comparable to N, the third length lies
between `m/2-o(m)` and `5m/8-o(m)`. In particular, for all large
N the three bands are disjoint, all lengths exceed m/9, and the
number of admissible length triples is between `c_2 m^2` and
`C_2 m^2`, with c_2,C_2>0. The two displayed independent intervals
have fixed positive lengths proportional to m; their integer
rounding affects only lower-order terms.

For each good word w in (5.4), form its partner by permuting the
three equal-buffer cells

$$
 (0^R a u_1 a0^R),\ (0^R a u_2 a0^R),\
 (0^R a u_3 a0^R)
$$

from the cyclic order `(1,2,3)` to `(1,3,2)`. Call the resulting
word w'. It is good as well: a run of zeros cannot cross a
nonzero a, and the internal words and their zero runs are
unchanged by the permutation.

There are exactly three marked zero runs on either cyclic word.
If one were a proper repetition, its repetition number would
divide three. The only possible number other than one is three,
which would force the three consecutive gaps between marked
runs to have equal lengths. Their lengths are different by
(6.1). Thus both words have primitive symbolic period m.
Their geometric orbits are primitive too: a periodic point other
than the origin has a unique itinerary, and the origin has at
most four itineraries. A primitive code of period m>4 cannot lie
in that fiber. These are exactly the coding facts established in
the first frozen input.

The orbits are different. With three distinct gap lengths, the
cyclic order `(short,medium,long)` cannot be a cyclic shift of
`(short,long,medium)`. This argument uses lengths and does not
require the internal edge words themselves to be distinct by
any further test.

Finally there is no overcount in the following assignment. On
the first orbit select the unique zero run immediately preceding
the short cell; its central cut, R edges from either end, fixes
the starting code. This reconstructs w and all three u_j
uniquely from that geometric orbit. The short-medium-long
orientation distinguishes it from every second orbit in the
class. Thus a different good word counted in (5.12), including
a word with different chosen lengths, cannot give the same
unordered pair. Each is a pair of primitive geometric orbits,
and (T.1) contains exactly its two ordered pointwise cross
directions, each with m^2 point choices.

Combining (5.12) and the number of length triples proves that
the sum of the periodic weights of the first orbit of every
selected pair satisfies

$$
 c_3 m^2\Lambda^{-6R}
 \le\sum_{(p,p')\in\mathcal A_{m,N}}\Lambda_p^{-1}
 \le C_3 m^2\Lambda^{-6R}.
 \tag{6.2}
$$

The count in (5.12) was a count of codes at the specified cut,
and the argument just given is why it is exactly this sum over
geometric orbits, without an extra factor m or 1/m.

## 7. The nonvanishing pair-scale mass

Multiply (6.2) by the uniform positive cross-weight comparison
(4.5). This gives

$$
 c_4 m^4\Lambda^{-6R}\le E_{m,N}
                 \le C_4 m^4\Lambda^{-6R}.
 \tag{7.1}
$$

The chosen integer rounding in (4.3) gives exactly

$$
 \frac{\Lambda^{-2R_0-2}}N
     \le\Lambda^{-2R}
     \le\frac{\Lambda^{-2R_0}}N.
 \tag{7.2}
$$

For `N<=m<=3N/2`, equations (7.1)--(7.2) prove (T.2).
All constants, including R_0 and the eventual threshold in N,
are fixed once for the original map. The proof does not send
tau to zero or select a subsequence of dimensions.

For completeness the fixed test is

$$
 \phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
 I=\int\phi,\quad g=\mathcal F^{-1}\phi,\quad
 b_* =|g|^2/(2I^2).
$$

It is nonnegative Schwartz, `sup b_*<=1/2`, and its Fourier
transform is a positive scalar multiple of the convolution of
phi with its reflection. That convolution is strictly positive
on `(-2,2)` and vanishes outside `[-2,2]`. Thus
`w=|bhat_*|^2` has a strictly positive minimum on `[1,3/2]`.
There are order N integers in this interval after scaling, so
(T.2) proves (T.3). The same argument gives a positive lower
bound with the Abel weight `exp(-2sm/N)` for every fixed s>0.

## 8. The still missing signed cancellation

In the exact deck expansion, different points on the same
geometric orbit make the previously evaluated diagonal terms.
The pairs here belong to different geometric orbits, so all
the terms of E_(m,N) belong to the full off-diagonal O_(m,N).
Their complete odd-dimensional phases and exact scalar
amplitudes were retained throughout.

For the fixed test b_*, the preceding frozen pair calculation
gives

$$
 \Delta_{2,N}(b_*)
 =\frac1{N^2}\sum_{1\le m<2N}w(m/N)O_{m,N}
       +\eta_*+O(N^{-1}),\qquad \eta_*>0.
 \tag{8.1}
$$

Define E_(m,N)=0 outside the selected interval, and define the
remaining signed sum by `O_rest=O-E`. The new theorem proves a
strictly positive lower bound for

$$
 A_N^{\rm selected}
  =\frac1{N^2}\sum_m w(m/N)E_{m,N}.
$$

To complete even this pair test one would still have to prove

$$
 \frac1{N^2}\sum_{m<2N}w(m/N)O^{\rm rest}_{m,N}
     =-\eta_*-A_N^{\rm selected}+o(1).
 \tag{8.2}
$$

No estimate of (8.2) is established in this note. It is not a
hypothesis used above. The complement can contain negative
terms and can cancel the displayed positive class; nothing in
the proof supplies a lower bound for the total signed sum.
The result isolates genuine contributions at the Heisenberg
pair scale and quantifies the further cancellation the original
problem requires. It does not settle that cancellation or any
of the higher-order conditions in H_diag.
