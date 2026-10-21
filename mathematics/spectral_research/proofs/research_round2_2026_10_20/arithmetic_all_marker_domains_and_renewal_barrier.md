> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_all_marker_domains_and_renewal_barrier.md`. Embedded SHA256: `dc8bef986cae11bc1917805a02746cd0861ee06f74da1d853bcc82e25ba7deba`.
> [Thematic guide](../../topics/dephasing.md).

# All marker edges, exact renewal masses, and the missing Fourier coherences

Research continuation, 20 October 2026. All dynamical objects below
belong to the exact map at the fixed parameter `tau=10^-80`.

## 1. Result and inputs

This note removes the restriction to one nonzero loop edge from the
endpoint geometry. It identifies the endpoint domains for every
nonzero incoming and outgoing edge, proves an exact scalar
telescoping identity over zero-run lengths, and then checks precisely
why that scalar identity does not telescope the relevant Fourier
Gram operators. The failure is an exact nonzero coherence term for
the actual geometric domains; it is not a counterexample to the
original spectral conjecture.

The proof inputs are:

| Input | SHA-256 |
|---|---|
| `arithmetic_endpoint_laws_and_sine_compression.md` | `8307e8bed074727caee3788adca79a44cab2fdf2627bbbfdcb2058a50863dfe1` |
| `fermionic_signed_three_cell_profile.md` | `edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5` |
| `adversarial_endpoint_symbols_and_renewal.md` | `561efce86a8aa2cab0c49fa05236e64f420ce26919ae0342dee2566e552ec32a` |

Use the notation of those files. In particular
$$
\rho=\Lambda^{-1}\in(0,1/5),\qquad B=\mathcal T-J,
\qquad \mathcal T\mathfrak h=\mathfrak h,
\quad \nu\mathcal T=\nu,
$$
and `J^j=rho^j(g delta_o+O(theta^j))`, with `theta=2/3`.
Set
$$
c_0=\nu(g)\mathfrak h(o)>0,\qquad
\kappa=(1-\rho)c_0.
\tag{1.1}
$$
This `kappa` is the escape constant in the signed-profile input.

The new geometric statement is that there are full fixed-point
axis intervals `J_S,J_U`, both containing zero in their interiors,
whose nonzero-edge domains are exactly
$$
\boxed{D_S=J_S\setminus\rho J_S,\qquad
D_U=J_U\setminus\rho J_U.}
\tag{1.2}
$$
Endpoints have zero measure, so any consistent endpoint convention
is harmless. Each domain is the union of two nondegenerate intervals.
The all-nonzero-edge endpoint laws are uniform on these domains, and
$$
\boxed{c_0=\chi|J_S||J_U|,\qquad
c_B:=\nu(Bg)(B\mathfrak h)(o)
=(1-\rho)^2c_0=\chi|D_S||D_U|=(1-\rho)\kappa.}
\tag{1.3}
$$

For each `beta>0`, let the scaled Fourier transform be
$$
(\mathcal F_\beta f)(u)
=\sqrt\beta\int_{\mathbb R}e^{-2\pi i\beta su}f(s)\,ds.
\tag{1.4}
$$
This is unitary, by the ordinary Fourier isometry and the change
of variable `xi=beta u`. If `P_D` denotes multiplication by the
indicator of `D`, define
$$
G_{\beta,D_S,D_U}
=P_{D_S}\mathcal F_\beta^*P_{D_U}
                       \mathcal F_\beta P_{D_S}.
\tag{1.5}
$$
It is a genuine compression of an orthogonal Fourier projection,
positive and trace class, with
$$
\operatorname{Tr}G_{\beta,D_S,D_U}=\beta|D_S||D_U|.
\tag{1.6}
$$
The all-marker probability-kernel operator at encounter parameter
`x=N rho^(2R)>0` is unitarily equivalent to
$$
\boxed{K^{B}_{2\pi\chi x}\simeq
\frac1{c_Bx}\,G_{\chi x,D_S,D_U}.}
\tag{1.7}
$$

Thus summing the nonzero edge labels gives an explicit position
interval with an inner interval removed, together with the analogous
removed frequency interval. Removing the labels does not turn this
operator into a single unperforated sine compression.

## 2. Full-axis coordinates and arbitrary edge labels

### 2.1. Full intervals

Define the stable scattering coordinate on every future starting
at vertex `i`, with all negative edges equal to `0`, without putting
a prescribed `a` in front. Likewise define the unstable coordinate
on all pasts ending at `i`, with future `0^infinity`, without putting
a prescribed edge at position `-1`. The rescalings and local
`q-q_*` normalizations are exactly those of the first input.

Their ranges are `J_S,J_U`. The proof that they are single compact
intervals is the same finite geometric fact already checked in
that input: before the edge restriction, a fixed past or future
cuts the full transverse plaque in the one Berg rectangle at
vertex `i`. Its actual image is one subarc of the appropriate
fixed-point leaf. The strictly monotone linearizing limit takes
that arc onto an interval. The fixed point is interior to both
plaques, so zero is interior to both resulting intervals.

For the centered cylinder `0^(2R)`, the two local-product
projections are exactly `rho^R` times convergent approximations
to these full intervals. Its stationary measure is
`nu(J^(2R) h)`. The area calculation of the first input, with
neither finite `a` edge imposed, gives
$$
\rho^{-2R}\nu(J^{2R}\mathfrak h)
\longrightarrow\chi|J_S||J_U|.
$$
The zero-branch limit gives `c_0` on the same left side. This
proves the first identity in (1.3).

### 2.2. Edge subintervals and their probabilities

Let `a:i->j` be any outgoing edge and `b:k->i` any incoming edge;
they need not be loops and may initially equal `0`. Denote the
corresponding stable and unstable subintervals by `I_S(a)` and
`I_U(b)`. For fixed additional chronological words `w` after `a`
and `v` before `b`, the exact centered-cylinder formula is
$$
\widehat\mu([v\ b\ 0^{2R}\ a\ w])
=\nu(J_wJ_aJ^{2R}J_bJ_v\mathfrak h).
\tag{2.1}
$$
Its rescaled transfer limit is
$$
\nu(J_wJ_ag)(J_bJ_v\mathfrak h)(o).
\tag{2.2}
$$
Its rescaled area limit is `chi` times the lengths of the two
actual refined intervals. Consequently, with no refinement,
$$
\boxed{\nu(J_ag)(J_b\mathfrak h)(o)
=\chi|I_S(a)||I_U(b)|.}
\tag{2.3}
$$
Summing over all incoming or outgoing edges in this identity
gives the individual length normalizations
$$
\frac{\nu(J_ag)}{\nu(g)}=\frac{|I_S(a)|}{|J_S|},
\qquad
\frac{(J_b\mathfrak h)(o)}{\mathfrak h(o)}
=\frac{|I_U(b)|}{|J_U|}.
\tag{2.4}
$$
Indeed only edges with the displayed compatible vertices survive
when these operators act on `g` or are evaluated at `o`.

The refined version of (2.3), followed by the vanishing-mesh
argument in the first input, proves uniform endpoint laws on
each of these intervals. Mixtures over edge labels have weights
proportional to their lengths, by (2.4).

### 2.3. The zero edge is exactly a homothetic inner interval

Prepending a zero edge to a future inserts one more contraction
step before that future. Directly from the defining limit,
$$
S_{\rm full}(0x)=\rho S_{\rm full}(x).
\tag{2.5}
$$
Appending a zero edge to a past gives the identical formula for
`U_full`. Hence
$$
\boxed{I_S(0)=\rho J_S,\qquad I_U(0)=\rho J_U.}
\tag{2.6}
$$
All individual outgoing edge strips partition the full stable
plaque, and all incoming strips partition the unstable one.
Their actual images have the same property. Removing exactly
the edge `0` therefore gives (1.2). In particular the inner
interval is scaled about the fixed-point coordinate zero; it
need not be centered at the midpoint of the outer interval.

By (2.4), summing all nonzero incoming and outgoing labels
gives the uniform laws on `D_S,D_U`. Since `Jg=rho g` and
`(J h)(o)=rho h(o)`, the identities for `c_B` in (1.3) follow.

## 3. The scalar zero-run sum really does telescope

For `j>=0`, put
$$
a_j=\nu(J^j\mathfrak h)=\widehat\mu([0^j]),
\qquad a_0=1.
\tag{3.1}
$$
The mass of the event consisting of a nonzero edge, exactly
`j` zeros, and a nonzero edge is
$$
p_j=\nu(BJ^jB\mathfrak h).
\tag{3.2}
$$
Using only `nu T=nu`, `T h=h` and associativity, one obtains
the exact second difference
$$
\boxed{p_j=a_j-2a_{j+1}+a_{j+2}.}
\tag{3.3}
$$
No commutation of `T` with `J` is needed: first expand the
left `B`, apply `nu T=nu`, then expand the right one and apply
`T h=h`.

The zero-branch limit implies `a_j->0`. Therefore
$$
\boxed{\sum_{j=k}^{\infty}p_j=a_k-a_{k+1}.}
\tag{3.4}
$$
Equivalently this sums over the first following nonzero edge;
the event of an infinite future zero tail has measure zero.
The same limit gives the asymptotics with fixed, actual constants
$$
\begin{split}
a_j&=c_0\rho^j+O((\rho\theta)^j),\\
p_j&=c_B\rho^j+O((\rho\theta)^j),\\
\sum_{j\ge k}p_j&=\kappa\rho^k+O((\rho\theta)^k).
\end{split}
\tag{3.5}
$$
Thus the scalar renewal normalization and the escape constant
have an exact geometric interpretation. The next section tests
the stronger operator telescoping that would be needed to use
these identities for signed quantum correlations.

## 4. The all-edge kernel is a compressed Fourier projection

Under the uniform laws just proved, the probability kernel is
$$
k^B_t(s,s')=\frac1{|D_U|}\int_{D_U}e^{it(s-s')u}\,du,
\qquad d\sigma_B(s)=\frac{ds}{|D_S|}.
\tag{4.1}
$$
The unitary map from this probability `L^2` space to ordinary
`L^2(D_S,ds)` divides functions by `sqrt(|D_S|)`. With
`beta=chi x` and `t=2 pi beta`, its transformed kernel is
$$
\frac1{|D_S||D_U|}\int_{D_U}
                        e^{2\pi i\beta(s-s')u}\,du.
$$
The kernel of (1.5) is `beta` times the integral. This proves
(1.7), because `beta|D_S||D_U|=c_Bx`.

The operator from `L^2(D_S)` to `L^2(D_U)` with kernel
`sqrt(beta) exp(-2 pi i beta su)` is Hilbert--Schmidt; its
squared norm is `beta|D_S||D_U|`. Its Gram operator is (1.5),
proving positivity and the trace formula. It is a contraction
because it is a restriction of the unitary Fourier transform.

More explicitly, if `b_U=|J_U|` and `bar u` is its midpoint,
the uncompressed Fourier-projection difference has kernel
$$
\begin{split}
q_\beta(s,s')={}&\beta b_U
 e^{2\pi i\beta\bar u(s-s')}
 \frac{\sin(\pi\beta b_U(s-s'))}{\pi\beta b_U(s-s')}\\
&-\beta\rho b_U
 e^{2\pi i\beta\rho\bar u(s-s')}
 \frac{\sin(\pi\beta\rho b_U(s-s'))}
      {\pi\beta\rho b_U(s-s')}.
\end{split}
\tag{4.2}
$$
Equation (1.5) compresses this difference onto
`J_S minus rho J_S`. This is the exact geometry after all
nonzero edge labels are included.

## 5. Nested projections: an exact obstruction to incoherent telescoping

### 5.1. Amplitude blocks do form an exact orthogonal partition

Fix `beta>0` and the actual intervals `J_S,J_U`. On the input
space put
$$
P_r=P_{\rho^rJ_S},\qquad E_r=P_r-P_{r+1},\quad r\ge0.
$$
On the Fourier output space put
$$
Q_s=P_{\rho^sJ_U},\qquad F_s=Q_s-Q_{s+1},\quad s\ge0.
\tag{5.1}
$$
Here the letter `F_s` denotes a multiplication projection, not
the classical map. Within each family these difference
projections are mutually orthogonal, and their sums are
`P_0,Q_0` strongly. The missing limiting point `{0}` has
Lebesgue measure zero.

Consider the full restricted Fourier amplitude
$$
\mathcal A=Q_0\mathcal F_\beta P_0,
\qquad \mathcal A_{sr}=F_s\mathcal F_\beta E_r.
\tag{5.2}
$$
Their integral kernels are restrictions of the same Fourier
kernel to pairwise disjoint rectangles. Hence
$$
\mathcal A=\sum_{r,s\ge0}\mathcal A_{sr}
\quad\hbox{in Hilbert--Schmidt norm},
\qquad
\sum_{r,s}\|\mathcal A_{sr}\|_{\rm HS}^2
=\beta|J_S||J_U|.
\tag{5.3}
$$
This is an exact coherent amplitude decomposition. It is the
most favorable version of an interval-partition telescoping
argument: all incoming and outgoing shells have been included.

### 5.2. Their separate Gram operators omit nonzero cross blocks

Let
$$
G=\mathcal A^*\mathcal A
=P_0\mathcal F_\beta^*Q_0\mathcal F_\beta P_0.
$$
The sum of the Gram operators of the separate blocks is
$$
\begin{split}
\mathcal D(G)
&:=\sum_{r,s}\mathcal A_{sr}^*\mathcal A_{sr}\\
&=\sum_r E_rGE_r.
\end{split}
\tag{5.4}
$$
The series is well defined in trace norm by positivity and
(5.3). It has the same trace as `G`, but it is not `G`.
The omitted terms are
$$
E_rGE_{r'},\qquad r\ne r'.
\tag{5.5}
$$
They arise from pairs of amplitude blocks with the same Fourier
output shell and different input shells. Orthogonality of the
output shells does not remove them.

Here is a strictly positive quantitative test of the difference:
$$
\boxed{\operatorname{Tr}(G^2)-\operatorname{Tr}(\mathcal D(G)^2)
=\sum_{r\ne r'}\|E_rGE_{r'}\|_{\rm HS}^2>0.}
\tag{5.6}
$$
For the equality, split the Hilbert--Schmidt kernel of `G` into
its disjoint input rectangles. Its squared norm is the sum of
the squared norms of these blocks. The diagonal blocks are
exactly the kernel of `D(G)`. Since the operators are positive,
their squared Hilbert--Schmidt norms are their second power
traces.

For strictness it suffices to take `r=0,r'=1`. Both shells
have nonempty interiors. On their product the kernel of `G` is
$$
\beta\int_{J_U}e^{2\pi i\beta(s-s')u}\,du.
\tag{5.7}
$$
As a function of the real difference `s-s'`, this is real
analytic and not identically zero; at difference zero it equals
`beta|J_U|>0`. It cannot vanish on an open difference interval.
The integral of its squared modulus over the product of these
two shells is therefore positive.

The term
$$
d(\beta)=\|E_0GE_1\|_{\rm HS}^2
\tag{5.8}
$$
is continuous and strictly positive for every `beta>0`, by
the same bounded integral formula. Thus it has a positive
minimum on every compact subinterval of `(0,infinity)`.
For the actual fixed-offset encounter scales,
`beta_N=chi N rho^(2R_N)` stays in just such a compact interval.
Consequently this omitted coherence is bounded below uniformly
in `N` in the rescaled operator problem. It is not an `o(1)`
error at that scale.

### 5.3. What the obstruction does and does not say

The scalar traces in (5.3)--(5.4) telescope exactly, just as the
scalar renewal masses in (3.4) do. Already their second power
traces do not. It is therefore invalid to recover a full
sine-compression determinant merely by summing the determinants
or Gram moments of independently treated run-length blocks.

This statement is stronger than noting that two projections
need not commute: (5.6) proves a definite nonzero missing term
for the actual intervals, at the actual rescaled parameters.
It is not a proof that every possible coherent renewal scheme
must fail. Equation (5.3) itself is a perfectly valid coherent
scheme if all cross blocks can be supplied with their correct
phases. Establishing those phases and their quantitative sum
is precisely the next issue for the original trace problem.

There is also a counting distinction. Independent input/output
shell labels correspond to choices of cut within a zero run.
For a fixed total number of zeros, moving the cut does not
create a different periodic orbit. Thus (5.3) is a geometric
amplitude identity, not by itself a formula that counts
distinct orbit pairs. No extra summation over cut locations
has been inserted into the actual signed-family theorem.

## 6. The first uncontrolled original phase term

For an exact cell `e`, the input defines its real boundary
action, including its deck term,
$$
W_e(q_{\rm out},q_{\rm in})
=\operatorname*{crit}_{q_1,\ldots,q_{d-1}}
 \sum_jF(q_{j+1},q_j)-(n_e)_p q_{\rm out}.
\tag{6.1}
$$
The signed three-cell calculation compares permutations of
exactly the same cells. Therefore the sums of
`W_e(q_*,q_*)` cancel before the local quadratic comparison;
the remaining phases are the bilinear endpoint phases used
in the Fourier operators above.

If interiors are unpaired, say `e` and `e'` contain different
return words, the exact phase contains instead
$$
\boxed{\exp\{2\pi iN[
 W_e(q_*,q_*)-W_{e'}(q_*,q_*)]\}.}
\tag{6.2}
$$
This scalar is present in addition to the endpoint quadratic
form. The uniform endpoint derivative estimates do not bound
the difference of these constant jets. The positive transfer
operator `T` computes geometric weights and their endpoint
distributions; it does not sum (6.2) for different interior
words. The scalar telescoping (3.4) supplies no such sum.

Thus a proof that removes the marker from the original quantum
pair functional must control the contributions of (6.2), with
the actual scalar cocycles, for all the unpaired return words
at total times of order `N`. In the proposed operator formulation it
must recover the cross-shell coherences represented by (5.5),
not silently replace the full Gram operator by its diagonal
block part. Neither a decay estimate nor the required signed
value for this unpaired-word sum has been proved here.

The completed results are (1.2)--(1.7), the exact renewal mass
identity (3.4), and the strict coherence test (5.6). They locate
a real obstruction to the proposed simple telescoping route
without asserting an obstruction to `H_diag` itself.
