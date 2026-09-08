# Exact trace-to-local-statistics bridge at Heisenberg scale

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
far stronger than necessary; cancellation in the frequency sum or a weighted
`L^1` estimate such as (15) may be much more attainable.

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
> Fourier support, prove (15) for the desymmetrized quantum-map spectrum against
> the correct COE/CUE/CSE symmetry class. For positive normalized averages and
> a reference Schwartz limit, comparison on every compact Fourier support
> automatically extends to all Schwartz tests. Hamiltonian energy-window
> formulations require their own unfolding and boundary treatment.

For the finite-circle model the remaining tasks are:

1. arithmetic/dynamical control of the joint traces at powers `Theta(N)`;
2. the deterministic conversion to local correlations, including removal of
   the band-limit under the positive-average hypotheses, which is now closed.

No claim is made here that the required Heisenberg-scale trace comparison has
been proved for the arithmetic cat maps in this repository.
