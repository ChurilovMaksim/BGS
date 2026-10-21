> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/adversarial_pair_sector_windows.md`. Embedded SHA256: `9c399a682a20067cc502c58893f61b13145d3b3e8782be0da5ab71dd0aca569f`.
> [Thematic guide](../../topics/arithmetic.md).

# Moving spectral windows: what actual sector covariance proves, and the remaining pair estimate

Research continuation, 20 October 2026. This report concerns the exact family
in the question at the fixed rational parameter `tau=10^-80`. It contains a
new consequence for its matrix elements, an independent check of the
all-iterate sector argument, and an exact test of the proposed passage to
unweighted close-pair counts. It does not prove `H_diag`.

## 1. The next target, stated before the reductions

Even the following bound is not established here:

$$
\sup_{N\ {\rm odd}}\frac1{N^2}
 \sum_{1\le m<2N}w(m/N)|\operatorname{Tr}U_N^m|^2<\infty,
\tag{1.1}
$$

for each fixed bounded nonnegative weight `w` supported in `[0,2]`.
An initial finite range of N is immaterial. The bound would be weaker than
the pair asymptotic in `H_diag`, which in turn would still be weaker than
`H_diag` at all orders.

The useful new actual-family conclusion is a statement about **weighted**
phase-difference measures. Fix an odd `d>=3`, let `N=d^2 m` tend to infinity
through all odd `m`, and put

$$
k=d^2,\qquad c=k^{-1},\qquad
A_\chi=P_\chi-cI,\qquad \chi\in\widehat G,
\quad G=(\mathbb Z/d\mathbb Z)^2.
\tag{1.2}
$$

The exact rank-`N/k` sector projections `P_chi` are those in the audited
all-iterate report. For **every** sequence `epsilon_N>=0` tending to zero,

$$
\boxed{\sup_{\omega\in\mathbb R/\mathbb Z}
 \frac1N\sum_{\|\theta_{j,N}-\theta_{i,N}-\omega\|\le\epsilon_N}
 |\langle\psi_{i,N},A_\chi\psi_{j,N}\rangle|^2
 \longrightarrow0.}
\tag{1.3}
$$

Here `psi_(j,N)` is **any** orthonormal eigenbasis. The statement is
independent of its choice inside a degenerate eigenspace. The center
`omega` can depend on N, and the interval can shrink faster than `1/N`.
There is no rate in (1.3). A joint matrix-valued version is proved below.

## 2. Frozen input and its independent check

The direct input is

`arithmetic_iterated_sector_covariance.md`

with SHA-256
`c8e02b81819350ab52e7bc3dd791ffbeb1ae1a2192a9a99f1168c4c56d7123e2`.

Its preceding Weyl and trace lemmas are in
`arithmetic_oldspace_escape.md`, SHA-256
`596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a`.
The latter was independently checked in `adversarial_oldspace_audit.md`.

The all-iterate input is

$$
\frac1N\operatorname{Tr}(P_\chi U_N^{-r}P_\eta U_N^r)
 \longrightarrow c^2
 \qquad(r\ne0\text{ fixed}).
\tag{2.1}
$$

I checked the new proof rather than taking (2.1) on trust. Its critical
points are as follows.

* The exact ordinary symbol has the shift `r(q+1/2)` in the p-dependent
  term. With `S=((3,4),(2,3))`, `X=(a_p,-a_q)/(2 pi)`, and
  `Psi=S composed with Phi_tau`, the convention is
  `U Op(b) U*=Op(b composed with Psi)+O_b(N^-2)`.
* If `ell=(1,sqrt(2))/sqrt(3)` and `lambda=3+2sqrt(2)`, then

  $$
  v_r(x)=\lambda^{-r}\ell\Psi^r(x)-\ell x
  =\sum_{j<r}\lambda^{-j}\ell\delta(\Psi^j x),
  \quad\delta=\Phi_\tau-\operatorname{Id},
  $$

  exactly. The bounded displacement, rather than a derivative of the
  nonlinear iterate, gives
  `||Psi^j-S^j||_infinity<=50 tau lambda^j`.
* Comparing with
  `w_r=tau sum_(j<r) lambda^-j ell X(S^j x)`, the error is at most

  $$
  \sum_{j\ge0}\left[20000\tau^2\lambda^{-j}
      +\min(10^5\tau^2,40\tau\lambda^{-j})\right]
  <3\cdot10^7\tau^2.
  $$

  Splitting at the fixed integer 200 proves this uniformly for all r.
  The full undiscounted iterate is not asserted to have a uniform
  first-order expansion.
* The two frequencies `S^(-Tj)e_1` and `S^(-Tj)e_2` leave `|l|<=1`
  for every `j>=1`. Thus the two basic Fourier coefficients of `w_r`
  have magnitudes at least `tau/400`, and those of `v_r` are at least
  `tau/800`, for every r.
* A lifted relation `Psi^r t_h Psi^-r=t_g` gives
  `Psi^r(x+h)-Psi^r(x)=g+n`. Averaging the difference of the periodic
  part `Psi^r(x)-S^r x` over the torus gives `g+n=S^r h`. Equivalently,
  one may iterate the translation and divide by its iteration number.
  Hence `v_r(x+h)=v_r(x)`. Its two basic nonzero Fourier coefficients
  force both coordinates of h to be integers. This excludes arbitrary
  nontrivial translations, not only rational ones.
* The word `T_g U^-r T_h U^r` quantizes
  `Psi^r t_h Psi^-r t_g`, which is a nonidentity analytic map unless
  `g=h=0`. The normalized trace lemma applies separately for each fixed
  r. The finite group expansion gives (2.1), with all characters and
  with negative r obtained by cyclicity.

Sections 7 and 8 of the input, including the projection onto the **full**
spectral commutant, therefore pass the independent check. No uniform
Egorov bound for r depending on N has entered this audit.

## 3. A joint weighted spectral measure

Write `a_(chi,ij)=<psi_i,A_chi psi_j>` and
`Delta_ij=theta_j-theta_i` in the circle. Define a matrix of finite measures

$$
\mu_N^{\chi\eta}
 =\frac1N\sum_{i,j}
  \overline{a_{\chi,ij}}a_{\eta,ij}\,\delta_{\Delta_{ij}}.
\tag{3.1}
$$

For any coefficient vector z, the measure
`sum_(chi,eta) conjugate(z_chi) z_eta mu_N^(chi eta)` is nonnegative:
it is the measure for the single operator `A_z=sum z_chi A_chi`.
The total variation of each entry is bounded by Cauchy--Schwarz and the
fixed normalized Hilbert--Schmidt norms of the two operators.

The r-th Fourier coefficient, with a positive sign in the character, is

$$
\int e^{2\pi ir\omega}\,d\mu_N^{\chi\eta}(\omega)
 =\frac1N\operatorname{Tr}
 (A_\chi^*U_N^{-r}A_\eta U_N^r).
\tag{3.2}
$$

At `r=0`, orthogonality and exact ranks of the projections give exactly

$$
\frac1N\operatorname{Tr}(A_\chi A_\eta)
 =c\,\mathbf 1_{\chi=\eta}-c^2.
\tag{3.3}
$$

For every fixed nonzero r, expansion of the centered operators and (2.1)
make (3.2) tend to zero. Consequently

$$
\boxed{\mu_N^{\chi\eta}\Longrightarrow
       (c\,\mathbf 1_{\chi=\eta}-c^2)\,d\omega.}
\tag{3.4}
$$

To justify this directly, approximate a continuous function on the circle
uniformly by a trigonometric polynomial. Convergence for that polynomial
is exactly (3.2)--(3.3); the uniform total-variation bound controls both
approximation errors. No spectral-gap or simplicity assumption is used.

For the scalar positive measure associated with `A_z`, its limiting total
mass is

$$
v_z=c\sum_\chi|z_\chi|^2-c^2\left|\sum_\chi z_\chi\right|^2.
\tag{3.5}
$$

The matrix in (3.4) is positive semidefinite, with the expected null vector
consisting of all ones because `sum A_chi=0`.

## 4. A finite Fejer inequality proves moving-window suppression

Let A be any fixed linear combination of the `A_chi`, and put

$$
C_{r,N}(A)=\frac1N\operatorname{Tr}(A^*U_N^{-r}AU_N^r),
\qquad C_{0,N}(A)=v_A.
$$

For positive integer T and a circle parameter omega, define

$$
\mathcal A_{T,N}^{\omega}(A)
 =\frac1T\sum_{r=0}^{T-1}e^{-2\pi ir\omega}U_N^{-r}AU_N^r.
\tag{4.1}
$$

Its `(i,j)` entry is `a_ij D_T(Delta_ij-omega)`, where
`D_T(u)=T^-1 sum_(r=0)^(T-1) e^(2 pi i r u)`. Thus

$$
\begin{aligned}
E_{T,N}(A,\omega)
&:=\frac1N\|\mathcal A_{T,N}^{\omega}(A)\|_{\rm HS}^2\\
&=\frac{v_A}{T}
 +\frac2{T^2}\operatorname{Re}\sum_{r=1}^{T-1}
   (T-r)e^{-2\pi ir\omega}C_{r,N}(A).
\end{aligned}
\tag{4.2}
$$

In particular

$$
\sup_\omega E_{T,N}(A,\omega)
 \le\frac{v_A}{T}+R_{T,N}(A),\qquad
R_{T,N}(A)=\frac2{T^2}\sum_{r=1}^{T-1}(T-r)|C_{r,N}(A)|.
\tag{4.3}
$$

For fixed T, (2.1) proves `R_(T,N)(A)->0`.
For `||u||<=epsilon`, the elementary bound `|exp(ix)-1|<=|x|` gives

$$
|D_T(u)-1|\le\pi(T-1)\epsilon.
$$

Therefore, whenever `pi(T-1)epsilon<1`, the following is an **exact
finite-N inequality**:

$$
\boxed{\sup_\omega\frac1N
 \sum_{\|\Delta_{ij}-\omega\|\le\epsilon}|a_{ij}|^2
 \le
 \frac{v_A/T+R_{T,N}(A)}{(1-\pi(T-1)\epsilon)^2}.}
\tag{4.4}
$$

Apply (4.4) with `epsilon=epsilon_N`. First hold T fixed and send N to
infinity. The denominator tends to one and the remainder tends to zero.
Then let T tend to infinity. This proves (1.3), and its version for every
fixed linear combination A. Because there are finitely many characters,
the sum of their left sides also tends to zero.

One can alternatively deduce uniform convergence over all circle arcs
from the positive weak limit `v_A d omega`: subdivide the circle into a
fixed fine grid, use weak convergence at its finitely many endpoints,
and sandwich an arbitrary arc between two such grid unions. The finite
Fejer bound records more explicitly which finite-time errors would need
to be improved for a rate.

## 5. Basis-independent form, including moving centers

For a circle set I define the orthogonal projection on Hilbert--Schmidt
matrix space

$$
\mathcal Q_{I,N}(B)=
 \sum_{\arg(\mu/\lambda)/(2\pi)\in I}
       \Pi_\lambda B\Pi_\mu,
\tag{5.1}
$$

where the sum uses the distinct spectral values of U. The argument is
understood in the circle, so representatives do not matter. The matrix
blocks are mutually Hilbert--Schmidt orthogonal. In any eigenbasis,
the squared Hilbert--Schmidt norm of (5.1) is exactly the sum of the
corresponding squared entries. Hence (1.3) is equivalent to

$$
\sup_\omega\frac1N
 \|\mathcal Q_{\omega+[-\epsilon_N,\epsilon_N],N}(A_\chi)\|_{\rm HS}^2
 \longrightarrow0.
\tag{5.2}
$$

At zero width and center zero this is the full commutant result. For
positive width it controls all blocks with close eigenvalues, including
off-diagonal blocks between distinct eigenvalues. It does not use a
particular basis to discard entries within a multiple eigenvalue.

## 6. The exact rank bound supplied by the full character family

Let Q be any orthogonal projection of rank r, and let the `P_chi` be any
orthogonal resolution of the identity into k equal ranks `m=N/k`.
Set `K_chi=Q P_chi Q` on the range of Q. It is positive, its rank is at
most m, and `sum Tr K_chi=r`. Cauchy--Schwarz on its nonnegative
eigenvalues, followed by Cauchy--Schwarz over the characters, gives

$$
\sum_\chi\operatorname{Tr}K_\chi^2
 \ge\frac1m\sum_\chi(\operatorname{Tr}K_\chi)^2
 \ge\frac{r^2}{km}=\frac{r^2}{N}.
\tag{6.1}
$$

Expanding the centered squared norms gives the exact identity and bound

$$
\boxed{\sum_\chi\|Q A_\chi Q\|_{\rm HS}^2
 =\sum_\chi\operatorname{Tr}K_\chi^2-cr
 \ge\frac{r^2}{N}-cr.}
\tag{6.2}
$$

Now let Q be the spectral projection of an arc of length at most
`epsilon_N`. All its matrix entries are among the close-phase blocks
in (5.2). If `eta_N` denotes the sum of their normalized squared norms,
then `eta_N->0`, and

$$
\frac rN\le
 \frac{c+\sqrt{c^2+4\eta_N}}2=c+o(1).
\tag{6.3}
$$

For disjoint arcs `I_l` of length at most `epsilon_N`, with occupancies
`r_l`, summing (6.2) counts disjoint matrix blocks. If the arcs form a
partition of the circle, one obtains

$$
\boxed{\sum_l r_l^2\le cN^2+\eta_N N^2.}
\tag{6.4}
$$

These are the consequences of positivity and rank alone. In particular,
their scale is `N^2/d^2`, not the `O(N)` scale needed to bound
microscopic pair counts. For a fixed d the distinction persists as
N tends to infinity.

### 6.1 Why no entrywise lower bound follows from the projector algebra

This is an exact sharpness check of (6.2), not a new dynamical matrix
family. Identify `C^N=C^k tensor C^m` and write
`P_chi=|e_chi><e_chi| tensor I_m`. Let
`u=k^-1/2 sum e_chi`, and let W be any r-dimensional subspace of
`u tensor C^m`, with `1<=r<=m`. If Q projects onto W, then

$$
Q P_\chi Q=cQ,\qquad Q A_\chi Q=0
\quad\text{for every character.}
\tag{6.5}
$$

Thus two different orthogonal vectors can have zero off-diagonal matrix
element for every sector projector, while their centered diagonal
elements also vanish. At `r=m`, equality holds in (6.2). The exact rank
limit for a subspace invisible to all centered sector compressions is
m: if `Q P_chi Q=cQ`, its rank r cannot exceed `rank P_chi=m`.

For finitely many fixed odd denominators dividing N in the required
square sense, put D equal to their least common multiple. If `D^2|N`,
the corresponding commuting Weyl groups are subgroups of the group
with denominator D. Its character resolution refines all of them,
and the same calculation has rank `N/D^2`. Hence taking any fixed
finite collection of denominators does not supply a microscopic
entrywise lower bound. Passing to D depending on N requires a new
uniform estimate; the all-fixed-d theorem does not assert one.

Equation (6.5) is not claimed to occur for the actual U. It proves the
precise limitation of deductions that use only the projector resolution,
the weighted suppression, and positivity. A property particular to U
would have to exclude an approximate version of (6.5) at a quantified
scale before it could count close eigenvalues.

## 7. An exact complete-frame identity locates the missing information

Let `T_v`, `v in (Z/NZ)^2`, be the **full** Weyl family from the question.
The matrices `T_v/sqrt(N)` are an orthonormal basis of the N-by-N
matrix space for the Hilbert--Schmidt inner product. Applying Parseval
to a rank-one matrix in any orthonormal eigenbasis gives

$$
\sum_v|\langle\psi_i,T_v\psi_j\rangle|^2=N
\qquad\text{for every }i,j.
\tag{7.1}
$$

Define the ordered close-pair count, including the diagonal, by

$$
C_N(\epsilon)=
 \#\{(i,j):\|\theta_i-\theta_j\|\le\epsilon\}.
$$

Summing (7.1) over those pairs gives the exact identity

$$
\boxed{\frac{C_N(\epsilon)}N
 =\frac1{N^2}\sum_{v\in(\mathbb Z/N\mathbb Z)^2}
   \|\mathcal Q_{[-\epsilon,\epsilon],N}(T_v)\|_{\rm HS}^2.}
\tag{7.2}
$$

There is no unknown lower bound in (7.2). It replaces that lower bound
by a complete sum over N squared observables. The sufficient estimate
for the next pair-count target is therefore exactly

$$
\boxed{\frac1{N^2}\sum_v
  \|\mathcal Q_{[-a/N,a/N],N}(T_v)\|_{\rm HS}^2=O_a(1).}
\tag{7.3}
$$

This has **not** been proved. The sector theorem concerns a fixed
number of macroscopic Weyl observables and bounds each centered
quantity by `o(N)`. In the full sum a typical contributing scale would
be bounded Hilbert--Schmidt norm squared, not merely `o(N)`. Both the
size of the observable family and the scale of the estimate change
in (7.3). Neither change is justified by a fixed-parameter limit.

For the fixed group alone, finite character Parseval and `Tr A_chi=0`
give

$$
\sum_{g\in G}
 \|\mathcal Q_{[-\epsilon_N,\epsilon_N],N}(T_g)\|_{\rm HS}^2
 =N+o(N).
\tag{7.4}
$$

The term `g=0` is exactly N. Formula (7.4) is another useful way to
state the actual result, but it cannot be substituted for (7.3).

## 8. The close-pair scale really implies the weak power-trace target

This section checks that the missing scale in (7.3) is relevant to
(1.1), rather than an artificially stronger condition. Define the
nonnegative Fejer kernel

$$
F_T(t)=\frac1T\left|\sum_{r=0}^{T-1}e^{2\pi irt}\right|^2
 =\sum_{|r|<T}(1-|r|/T)e^{2\pi irt}.
$$

For every unitary matrix,

$$
\frac1{N^2}\sum_{i,j}F_T(\theta_i-\theta_j)
 =1+\frac2{N^2}\sum_{r=1}^{T-1}(1-r/T)|p_r|^2.
\tag{8.1}
$$

Partition the circle into T equal half-open arcs, with occupancies n_l,
and let `S=sum n_l^2`. If two arcs have cyclic index distance r, then
`F_T<=T` for r=0,1; for `r>=2`, the distance between their points is at
least `(r-1)/T`, and `|sin pi t|>=2||t||` gives

$$
F_T(t)\le\frac{T}{4(r-1)^2}.
$$

For every cyclic shift r, Cauchy--Schwarz gives
`sum_l n_l n_(l+r)<=S`. Counting at most two shifts of each distance
and summing the convergent square tail yields

$$
\sum_{i,j}F_T(\theta_i-\theta_j)
 \le T S\left(3+\frac{\pi^2}{12}\right)<4T S
 \le4T C_N(1/T).
\tag{8.2}
$$

The same bound works for even T; the single antipodal shift only reduces
the counting bound. With `T=4N`, (8.1)--(8.2) imply, for any bounded
nonnegative w supported in `[0,2]`,

$$
\frac1{N^2}\sum_{1\le r<2N}w(r/N)|p_r|^2
 \le16\|w\|_\infty\frac{C_N(1/N)}N.
\tag{8.3}
$$

Thus `C_N(1/N)=O(N)`, equivalently (7.3) at a=1, would prove (1.1).
Conversely, on `||t||<=1/(2T)` one has
`F_T(t)>=4T/pi^2`. A bounded Fejer statistic with T proportional to N
therefore bounds close pairs at a fixed multiple of `1/N`. There is no
claim that an arbitrary weight vanishing near zero has this converse.

For reference, the exact pair identity for an admissible b in the
question is

$$
\Delta_{2,N}(b)=\frac1{N^2}\sum_{r\ge1}
  |\widehat b(r/N)|^2\bigl(|p_r|^2-\min(r,N)\bigr).
\tag{8.4}
$$

The stronger required conclusion is a limit for (8.4), not just the
boundedness in (1.1).

## 9. Attempts to remove the actual-family gap

The exact arithmetic escape theorem and the generator's positive escape
lower bound concern vectors supported in a sector. The subspaces in
(6.5) are evenly spread over the sectors. Accordingly those theorems do
not contradict the compression pattern that makes close pairs invisible
to the centered sector observables. Applying them here would change
their hypotheses.

Likewise, the exact mean escape and all-fixed-time covariance distribute
the **weights** `|a_ij|^2` over the phase differences. Formula (4.2)
shows the remaining time-scale issue explicitly: to obtain a bound of
order `1/N` on such a normalized weighted window from the Fejer estimate,
one would need a time average of order N with a suitably controlled
remainder. Knowing every fixed correlation tends to zero permits
`T->infinity` only after the N limit. It does not produce that rate.

The exact all-time orbit formula improves the description of `p_r`,
but has not provided the complete-frame estimate (7.3) or a lower
matrix-element bound particular to a microscopic spectral subspace.
The proved signed pseudo-orbit cancellation controls coefficients of
the characteristic determinant. Passing to its logarithmic derivative
or reciprocal still requires the cross terms already isolated in the
fermionic report. No positivity argument here bounds those cross terms.

Actual variation, and even nonlattice behavior, of marked unstable
multipliers excludes a smooth cat-conjugacy mechanism. It concerns
classical orbit amplitudes. A bound for the oscillating action
differences at quantum frequency N is an additional statement; it
does not follow by replacing the action phase with the logarithm of an
unstable multiplier. No such replacement is made here.

The new theorem is consequently (1.3)--(5.2), with its full joint and
basis-independent form. The first missing estimate on the proposed
complete-observable route is (7.3). The first missing estimate on the
original orbit route remains the signed weighted power-trace sum in
(8.4), already at order two. Neither is inserted as a hidden assumption.

