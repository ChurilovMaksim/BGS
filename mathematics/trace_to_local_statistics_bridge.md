# Exact trace-to-local-statistics bridge at Heisenberg scale

**Claim IDs:** `BGS-TRACE-001`, `BGS-TRACE-002`, `BGS-TRACE-003`

**Status: EXACT.**  This note is a deterministic Fourier/partition identity for
finite unitary spectra.  It isolates a sufficient trace-comparison closure
condition for microscopic `k`-point statistics.  It does **not** prove that the
required trace estimates hold for arithmetic cat maps or any other unresolved
BGS family.

The main point is quantitative: microscopic local statistics require joint
trace information for powers of order the matrix dimension.  Fixed moments or
trace information only for `n=o(N)` cannot be silently promoted to BGS.

## 1. Periodized microscopic test

Let `U` be an `N x N` unitary matrix with eigenvalues

```text
exp(2 pi i theta_1),...,exp(2 pi i theta_N),
theta_j in R/Z.
```

Fix `k>=2` and a Schwartz function

```text
phi:R^(k-1)->C.
```

Use the Fourier convention

```text
phihat(xi)=integral phi(x) exp(-2 pi i x dot xi) dx.
```

Define the `N`-scale periodization

```text
Phi_N(t_1,...,t_(k-1))
 =sum_(n in Z^(k-1))
   phi(N(t_1+n_1),...,N(t_(k-1)+n_(k-1))).              (1)
```

Poisson summation gives exactly

```text
Phi_N(t)
 =N^(-(k-1)) sum_(m in Z^(k-1))
   phihat(m/N) exp(2 pi i m dot t).                      (2)
```

The translation-invariant factorial local statistic is

```text
C_(k,N)(U;phi)
 =(1/N) sum_(j_1,...,j_k distinct)
 Phi_N(theta_(j_1)-theta_(j_k),...,
       theta_(j_(k-1))-theta_(j_k)).                    (3)
```

The normalization is chosen so that a unit-density microscopic point process
has an `O(1)` limit.

## 2. Distinct-index exponential sums from traces

For integers

```text
m_1+...+m_k=0,
```

put

```text
D_U(m_1,...,m_k)
 =sum_(j_1,...,j_k distinct)
   exp(2 pi i sum_(a=1)^k m_a theta_(j_a)).              (4)
```

Let `Pi_k` be the lattice of set partitions of `{1,...,k}`.  For
`pi in Pi_k`, define its partition-lattice Mobius coefficient

```text
mu(pi)=prod_(B in pi) (-1)^(|B|-1)(|B|-1)!.             (5)
```

Write

```text
T_U(n)=Tr(U^n),     T_U(0)=N.                            (6)
```

### Theorem 1 (exact factorial trace identity)

For every integer zero-sum `k`-tuple `m`,

```text
D_U(m_1,...,m_k)
 =sum_(pi in Pi_k) mu(pi)
   prod_(B in pi) T_U(sum_(a in B)m_a).                  (7)
```

### Proof

Without the distinctness restriction, summing independently over every index
`j_a` gives

```text
prod_(a=1)^k T_U(m_a).
```

For a set partition `pi`, impose equality of indices inside every block.  The
corresponding unrestricted block sum is

```text
prod_(B in pi) T_U(sum_(a in B)m_a).
```

The condition that all `k` indices are distinct is the minimal partition in
the partition lattice.  Mobius inversion on that lattice has coefficient (5),
which gives (7).  No asymptotics enter. `□`

For `k=2`, (7) reduces to the familiar exact identity

```text
D_U(m,-m)=|Tr(U^m)|^2-N.                                (8)
```

## 3. Exact Fourier representation of local correlations

Set

```text
m_k=-(m_1+...+m_(k-1)).                                 (9)
```

### Theorem 2 (trace-to-local-statistics identity)

For every Schwartz `phi`,

```text
C_(k,N)(U;phi)
 =N^(-k) sum_(m in Z^(k-1))
    phihat(m/N)
    D_U(m_1,...,m_(k-1),m_k).                           (10)
```

Combining (7) and (10) expresses the full factorial microscopic statistic as
an explicit sum of products of traces.

### Proof

Insert Poisson summation (2) into (3), interchange the absolutely convergent
Schwartz sum with the finite eigenvalue sum, and use (4) with (9).  The factor
`N^(-k)` is `(1/N)N^(-(k-1))`. `□`

## 4. Heisenberg-scale consequence

Suppose

```text
supp(phihat) subset [-sigma,sigma]^(k-1).                (11)
```

Then only frequencies

```text
|m_a|<=sigma N,                 a<k,
|m_k|<=(k-1)sigma N                                 (12)
```

occur in (10).  Every block sum in (7) is therefore `O_(k,sigma)(N)`.

Thus microscopic band-limited `k`-point statistics are controlled by joint
trace products at powers **of order `N`**, i.e. at Heisenberg scale.  This is
an exact obstruction to any argument that only controls finitely many fixed
powers as `N->infinity`.

For `k=2`,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_(m in Z)
   phihat(m/N)(|Tr(U^m)|^2-N).                           (13)
```

If `phihat` is supported in `[-sigma,sigma]`, the sum still contains `Theta(N)`
trace powers.

### A concrete failure of reconstruction from short traces

The insufficiency can be proved independently of the Fourier identity. Let
N=2M. Compare the spectrum consisting of all N-th roots once with the
spectrum consisting of all M-th roots twice. For both unitary matrices,

```text
T_U(n)=0,                       1<=|n|<M,
T_U(0)=N.
```

Nevertheless, for any smooth test phi supported in (-1/2,1/2) with phi(0)=1,
their C_(2,N) statistics are respectively 0 and 1. In the first spectrum
every distinct unfolded difference is a nonzero integer. In the second,
the only contributing pairs are the two ordered distinct-label pairs at
each repeated root: there are 2M=N of them, all at difference zero.
Periodization introduces no further term in that support. Thus even exact
agreement of all traces throughout this linear window does not determine
the microscopic pair statistic. In particular it rules out reconstruction
from only fixed powers or an o(N) window without additional assumptions.

## 5. A precise RMT-comparison closure criterion

Let `E_N` be any averaging functional appropriate to the deterministic quantum
system: for example an energy-window average, a parameter average, or an
arithmetic design average.  Let `E_N^RMT` be the target random-matrix average
in the matching symmetry class.

Define

```text
Delta_D,N(m)
 =E_N D_U(m_1,...,m_k)
  -E_N^RMT D_V(m_1,...,m_k),                             (14)
```

where `V` denotes the target ensemble and `m_k` is given by (9).

### Corollary 3 (weighted Heisenberg trace criterion)

For one fixed band-limited Schwartz test `phi`, if

```text
N^(-k) sum_(m in Z^(k-1))
 |phihat(m/N)| |Delta_D,N(m)| -> 0,                      (15)
```

then

```text
E_N C_(k,N)(U;phi)
 -E_N^RMT C_(k,N)(V;phi) -> 0.                           (16)
```

This follows immediately from (10) and the triangle inequality.

A stronger but simpler sufficient condition is

```text
sup_(m in Heisenberg support) |Delta_D,N(m)|=o(N),       (17)
```

because a fixed compact Fourier support contains `O(N^(k-1))` lattice points,
and then (15) is `o(1)`.

Condition (17) is deliberately stated only as a sufficient condition.  It is
far stronger than necessary. For an unaveraged deterministic spectrum,
one must retain cancellation in the frequency sum: the
[absolute-norm obstruction](signed_heisenberg_comparison.md) (`BGS-TRACE-010`)
proves that absolute pair CUE comparison on every compact support forces
absolute cubic error to grow at least as sqrt(N) on a fixed positive box.
Thus (15) cannot hold simultaneously at every order in that unaveraged
CUE setting. The implication above remains correct, including comparisons
averaged before taking the modulus.

For one fixed test, the weaker signed condition

```text
N^(-k) sum_m phihat(m/N) Delta_D,N(m) -> 0              (15S)
```

is exactly equivalent to (16), by identity (10). A modulus may be placed
outside the entire sum in (15S). This is the viable deterministic
`BGS-TRACE-005` closure condition; it has not been proved for the frozen map.

## 6. Extension from all compact Fourier supports — corrected 2026-09-08

For positive normalized averages of the factorial spectral measures, convergence
against **every** band-limited Schwartz test, with no common bound on its
Fourier support, implies convergence against every Schwartz test. There is no
additional independent high-frequency-tail hypothesis in this setting.

The complete proof is in `bandlimited_correlation_extension.md`. Its key
estimate, for `d=k-1`, `N>2` and the lifted anchored factorial measure `mu_N`, is

```text
sup_a mu_N(a+[0,1)^d) <= 2 k^k (1+mu_N([-2,2]^d)).
```

A single nonnegative band-limited Schwartz majorant of `[-2,2]^d` bounds the
right side. Periodic occupation counts, Holder's inequality and factorial
moment expansion then give uniform bounds on translated cubes. These bounds
make Schwartz Fourier-cutoff approximation uniform in `N`.

This corrects the earlier assertion that the tail was necessarily a separate
open obligation. It does **not** imply an absolute-value bound on the Fourier
trace tail. A comparison restricted to one fixed Fourier cap still does not
determine all local correlations; the extension note gives an exact clock /
period-two counterexample. Signed averaging functionals also fall outside this
positive-measure argument.

## 7. Relation to the current arithmetic-cat-map programme

The current repository proves several exact finite-field second/fourth moment
identities and a sharp arithmetic reduction for one Cayley-energy bottleneck.
Those are useful inputs to trace information, but Theorem 2 shows exactly why
they are not microscopic BGS:

```text
finite/fixed moment information
      !=
weighted joint trace comparison for |n|=Theta(N).
```

The local-statistics gap can now be stated as an explicit theorem target:

> **Heisenberg trace comparison problem.**  For each fixed `k` and each compact
> smooth Fourier weight, prove the signed comparison (15S) for the
> desymmetrized quantum-map spectrum against the correct COE/CUE/CSE
> symmetry class. Any modulus is outside the complete frequency sum.
> For unaveraged deterministic CUE comparison, do not replace this target
> by the all-order absolute criterion (15), which TRACE-010 excludes.
> Comparisons averaged before taking a modulus have a different scope.
> For positive normalized averages and
> a reference Schwartz limit, comparison on every compact Fourier support
> automatically extends to all Schwartz tests. Hamiltonian energy-window
> formulations require their own unfolding and boundary treatment.

For the finite-circle model the remaining tasks are:

1. arithmetic/dynamical control of the joint traces at powers `Theta(N)`;
2. the deterministic conversion to local correlations, including removal of
   the band-limit under the positive-average hypotheses, which is now closed.

No claim is made here that the required Heisenberg-scale trace comparison has
been proved for the arithmetic cat maps in this repository.

## 8. Stability under perturbations below one level spacing — 2026-09-16

**Status: internal proof, not a BGS theorem or a priority claim.**
This addresses the operator-comparison route proposed in the uploaded
`BGS_verified_state(1).md`, §21.5o. Its unconditional `o(N^-2)` criterion
is sufficient but is not a necessary accuracy threshold.

### Theorem 4 (all fixed correlation orders)

Let `U_N,V_N` be unitary matrices of the same dimension `N`, and put
`epsilon_N=||U_N-V_N||op`. Fix `k>=2`. Suppose the factorial statistics
`C_(k,N)(V_N;psi)` are bounded for every nonnegative Schwartz function `psi`.
If `N epsilon_N -> 0`, then for every Schwartz test `phi`,

```text
C_(k,N)(U_N;phi)-C_(k,N)(V_N;phi) -> 0.
```

In particular, convergence of the reference correlations transfers at every
fixed order for which this hypothesis holds. No averaging is needed. A scalar
phase rotation or a unitary conjugation of the reference can be performed
before applying the norm criterion, since neither changes these statistics.

**Proof.** For `epsilon<2`, let `H` be the principal Hermitian logarithm of
`UV*`, so `U=exp(iH)V` and

```text
||H||op <= 2 arcsin(epsilon/2).
```

Follow the eigenvalues along the analytic unitary path `exp(itH)V`,
`0<=t<=1`. Continuous eigenangle lifts can be chosen piecewise analytically;
at a multiple eigenvalue their one-sided angle derivatives are the eigenvalues
of the compression of `H` to its eigenspace. At a simple eigenvalue the
angle derivative is the expectation of `H` in the normalized eigenvector.
In both cases its absolute value is at most `||H||op`. Integrating gives a
bijection of eigenvalues, with multiplicities, and real phase lifts such that

```text
max_j |theta_j(U)-theta_j(V)| <= eta := arcsin(epsilon/2)/pi.
```

One can justify the piecewise analytic choice directly by applying analytic
Hermitian perturbation theory to a local Cayley transform of the unitary path;
finitely many overlapping spectral arcs cover the compact path. Relabeling at
crossings does not change the bound. Integer changes of the final lifts are
absorbed by the periodizing lattice in (1).

For any anchored distinct-index tuple, every coordinate of its unfolded
argument therefore moves by at most `d_N=2N eta`. Choose a nonnegative Schwartz
function `psi` majorizing

```text
sup_{||h||infinity<=1} sum_l |partial_l phi(x+h)|.
```

Such a majorant exists: the displayed nonnegative function decays faster than
any polynomial, and a smooth locally finite unit-cube partition gives a
Schwartz majorant with the same decay property. For `d_N<=1`, the mean-value
formula, followed by summation of the positive periodized measures, yields

```text
|C_(k,N)(U;phi)-C_(k,N)(V;phi)| <= d_N C_(k,N)(V;psi).   (18)
```

The right side tends to zero under the stated hypotheses. Absolute
convergence of the periodizations follows from Schwartz decay. This proves
the theorem, including multiple spectra. `□`

The hypothesis on the reference measure matters. This is not an unconditional
bound on the absolute Fourier trace discrepancy, and it does not apply to
nonunitary, merely power-bounded reference operators.

### Sharpness of the scale for general spectra

Fix `0<a<1/4` and take even `N`. Let `V_N` be the diagonal clock with phases
`j/N`, and let `U_N` have phases `(j+(-1)^j a)/N`. Both spectra are simple,
and

```text
||U_N-V_N||op = 2 sin(pi a/N).
```

Choose `phi` smooth, supported in `(1-a,1+a)`, with `phi(1)=1`. Then exactly

```text
C_(2,N)(V_N;phi)=1,       C_(2,N)(U_N;phi)=0.
```

Indeed, clock differences in this interval equal 1. The perturbed differences
are even integers or odd integers shifted by `+2a` or `-2a`, so none is in
that interval; periodic lifts have the same property because `N` is even.
Thus `O(1/N)` cannot replace `o(1/N)` in a general stability theorem. This is
not a counterexample to CUE universality for a fixed nonlinear map.

### A separate improvement for absolute Fourier comparisons

For a nonnegative bounded weight `w` supported in `[-sigma,sigma]`, assume

```text
Q_V := N^-2 sum_m w(m/N) |Tr V_N^m|^2 = O(1).
```

Writing `d_m=Tr U_N^m-Tr V_N^m`, telescoping gives
`|d_m|<=N |m| epsilon_N`, and therefore

```text
E := N^-2 sum_m w(m/N)|d_m|^2 = O(N^3 epsilon_N^2).
```

Cauchy--Schwarz gives the actual absolute Fourier bound

```text
N^-2 sum_m w(m/N) ||Tr U_N^m|^2-|Tr V_N^m|^2|
 <= 2 sqrt(Q_V E)+E
 = O(N^(3/2) epsilon_N + N^3 epsilon_N^2).             (19)
```

So `o(N^-3/2)` suffices in this stronger norm under the additional reference
bound. Equations (18) and (19) control different quantities. Neither supplies
a reference ensemble theorem, a comparison operator, or the required
comparison accuracy for the proposed nonlinear map.

## 9. Coherent summation rather than a per-time bound

`heisenberg_time_insertion.md` proves a complementary deterministic mechanism:
a small operator-valued Wiener budget in the time variable controls a
Liouville insertion after summing over a Heisenberg window. A positive-window
absorption argument can supply the required local pair bound. Exact
counterexamples show why an unspecified positive-power per-time saving or
small operator norm alone is insufficient. Its model-specific representation
hypothesis remains open for the proposed fixed nonlinear map.
