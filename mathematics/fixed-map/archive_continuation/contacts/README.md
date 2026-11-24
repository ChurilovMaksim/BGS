# Fixed-time contact inputs for the alignment proof

**Status:** analytic inputs from the [22 November chapter](BGS_Contacts.tex),
retained with their proof dependencies and finite-check boundary. The
independently maintained [position-chain estimate](../../position_chain_mixing.md)
and [reversed-path decay](../../reversed_path_decay.md) give the corresponding
one-step controls, not these summable all-fixed-time limits. This note
isolates only the portion of the packet used in the
[high-overlap theorem](../alignment/README.md). The remaining marked
contact, eigenvector, and Abel calculations in the TeX are archival.

For the exact [frozen map](../../fixed_map_resolvent_frontier.md), define
`P_j(x,y)=|(U_N^j)_{xy}|^2`, `Q_j(x,y)=(U_N^j)_{xy} conj((U_N^j)_{yx})`,
and `J_N(x,y)=1/N`. The analytic inputs asserted in the chapter are

```math
\max_{x,y}|(U_N^j)_{xy}|\le C_j N^{-1/2},
\qquad \lim_{N\to\infty\text{ odd}}\|Q_j\|=0
\quad (j\ge1\ \text{fixed}),
```

and

```math
\sum_{j\ge1}\limsup_{N\to\infty\text{ odd}}\|P_j-J_N\| < 10^{-5}.
```

The limit in dimension is taken at **each fixed** `j`, before
summing over `j`. No uniform-in-`j` stationary-phase error or
estimate of the full long-time propagator is asserted.

## Why the fixed-time norms converge

In physical coordinates the quantized map is `F=phi^tau B` with
`B=((3,-4),(-2,3))`. The physical momentum term is
`r(q+1/2) cos(2 pi p-alpha0)/100`, not `r(q)` times that cosine.
After reversing the momentum coordinate, every derivative matrix
of `F` has positive entries by the tiny fixed kick. Hence the
projection of the image of a vertical fibre under `F^j` has
no folds on the plane. On the torus there are finitely many
branches, the winding number being `|(B^j)_{12}|` for that
fixed time. Each branch contributes a generating-function phase
`S_n(x,y)` and a transport half-density with squared modulus
`|partial_x p_in(y,x+n)|`.

The proof uses the exact four-branch Gauss formula for the odd
cat-map kernel, finite-difference WKB for the Jacobi kick and
discrete stationary phase (Poisson summation) for a fixed number
of compositions. The chapter §§4–4a gives the construction, the
nondegeneracy of each composition, and the uniform-in-grid
fixed-`j` error budget for the kernel
`N^(-1/2) sum_n c_(n,N) a_n exp(2 pi i N S_n)+O_j(N^(-3/2))`.
Equal-branch products converge to the classical coordinate
transfer `L_j` with kernel `sum_n |partial_x p_in(y,x+n)|`.

A different-branch term and every reverse term is a discrete
oscillatory matrix of size `N^(-1)` per element. For a
nonseparable analytic phase `Phi(x,y)`, use
`||T||^4 <= Tr((T*T)^2)`. Its four-variable phase is
`Phi(x,y)-Phi(x,y')-Phi(x',y)+Phi(x',y')`. The locus
where every derivative is integral has measure zero by
analyticity and nonseparability. Off a small neighborhood of
that locus, a discrete summation by parts yields decay.
Neighborhoods and patch boundaries are removed in the
Hilbert–Schmidt bound, and their volume tends to zero.
Thus `P_j` converges to `L_j` in norm on embedded mesh
spaces, while `Q_j` converges to zero.

Two distinct geometric exclusions are essential in this step.

- A separable phase for two distinct **direct** branches forces
  `p_in(y,x+n)-p_in(y,x+l)` to be independent of `x`;
  iterating the shift until it is a whole winding makes the
  difference a nonzero rational constant. Its conjugate under
  `F^j` fixes position and is finite order. By area preservation
  it must itself be a translation. This contradicts the
  classical no-translation-to-translation rigidity in the
  [packet's Weyl chapter](../earlier_routes/BGS_Weyl.tex), §10, equation (14). It needs rigidity
  for possibly **different** input/output translations, not
  merely the absence of a commuting translation. One proof
  conjugates to the linear map, bounds the oscillation of
  the unstable displacement using the two independent Fourier
  probes of the inverse conjugacy, and thereby reduces to
  `j<=10`; a first-order lift with explicit `O(10^20 tau^2)`
  error excludes those times too because the two probe
  frequencies give a unimodular lattice basis.
- A separable phase for a **reversed** branch would give
  `F^j R_v F^j=R_w` with position-preserving reflections
  `R_v(q,p)=(q,v(q)-p)`. Thus `R_v` would reverse `F^(2j)`.
  In linearizing coordinates a position-preserving reversor
  with the given homology must be a translation followed by
  `(q,p)->(q,-p)`: a bounded periodic part commuting with the
  hyperbolic linear map is constant. The first component of
  the conjugacy then forces two incompatible Fourier
  conditions on the momentum displacement; the explicit
  incompatibility and error margin are proved in the source
  §2, and match the one-step proof noted above.

## The summable direct return bound

The [Weyl chapter](../earlier_routes/BGS_Weyl.tex) §§1–2 gives explicit lifted adjoint estimates,
which can be applied before reduction modulo `N`. With
`v=(a,b)`, `n(v)=|a|+sqrt(2)|b|`,
`g_0(v)=|a-sqrt(2)b|-|a+sqrt(2)b|`, and
`S=((3,4),(2,3))`, write `E` for the lifted adjoint kick and
`L=E S` for one lifted step (here `S` acts by label permutation).
The finite Fourier support and the Weyl commutator yield

```math
\sum_w |E_{wz}|e^{2n(w-z)}\le e^{10^{-64}n(z)}.
```

Indeed a generator column has absolute sum at most
`80 tau n(z)`, each generator step grows `n` by less than
14, and summing the exponential series is bounded by
`(1-1120 tau e^28)^(-n(z)/14)`. Since
`g_0(Sv)-g_0(v)<=-(1-(3+2 sqrt(2))^(-1))n(v)`,
the weighted column sum of `L` is at most `e^(-0.8 n(v))`.
The weight is one on the position-axis Weyl labels `(0,b)`.
The limit for any fixed `j` and fixed entries is obtained
by truncating the lifted paths inside growing balls of radius
`O_j(sqrt(N))`. Escape and nonzero-period quotient terms
are negligible by the exponential tail, so truncation
does not change the fixed-mode limit. Consequently

```math
\sum_{b'\ne0}|\widehat L_j(b',b)|
\le e^{-0.8\sqrt 2|b|}e^{-0.8(j-1)}\qquad (b\ne0).
```

For `1<=j<=20` and `1<=|b|<=30` a sharper estimate is
obtained by telescoping the actual kick against the bare cat
along the single bare Weyl orbit. The bare orbit is off the
position axis after every such time. The projected column
norm is bounded by `80 tau (2|b|) 6^21`. For the
complementary ranges the preceding exponential bound
is summable; using `e^(-0.8)<1/2` and
`e^(-0.8 sqrt(2))<1/3` gives the stated `10^-5` bound
on the sum of operator norms.

## Verification boundary

The [packet checks](../../../../computations/verification/bgs_f_november/contacts/recheck.py)
test exact finite Gauss/word identities and numerical diagnostics.
Neither these checks nor the one-step repository lemmas substitute
for the analytic branch separation, stationary phase, and weighted
all-fixed-time return argument above. No whole Heisenberg-scale
signed sum, factorial hierarchy, or microscopic limit follows.
