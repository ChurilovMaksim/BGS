# Fixed-factorial-order reduction to a high-order one-step WKB kernel

Project proof, independently internally reviewed on 6 October 2026.
Publication overlay against base `300d99270d11c87d0aa84e9d8f624491788629ba`.
Core claim: **BGS-TRACE-017**. TRACE-005 and deterministic BGS remain OPEN.

**Result.** For each fixed correlation order `k >= 2`, each fixed smooth
compactly supported Fourier weight `W`, and a one-step approximation

    ||U_N - V_(N,J)||op <= delta_N := C_J N^(-J-1/2),

with `U_N` unitary and integer `J >= 1`, replacing the exact signed traces in
the complete partition–Möbius transform by either of the two precisely defined
WKB trace tables below changes the normalized transform by

    O_(k,W,J)(N^(k-J-1/2)).                              (R)

Thus **J >= k suffices** to make this error vanish, at least as `N^(-1/2)`.
The approximation order may depend on the fixed correlation order. This is a
reduction of TRACE-005, not an estimate of its still-open oscillatory WKB sum.
It does not assert a local spectral law for a nonunitary matrix. For the
path-expansion application, the adjoint signed trace table (6) is the preferred
convention; the genuine-inverse Laurent statement is a separate optional
algebraic interpretation.

## 1. Exact target and prior scope

The normalization is exactly that of
`mathematics/trace_to_local_statistics_bridge.md`, equations (5), (7), (9),
(10) and (15S). Fix `k`, put `d=k-1`, and for `m in Z^d` append

    m_k = -sum_(a<k) m_a.

For a set partition `pi` of `{1,...,k}`, write

    mu(pi) = product_(B in pi) (-1)^(|B|-1)(|B|-1)!,
    n_B = sum_(a in B) m_a.

For the unitary matrix `U_N`, `T_U(n)=Tr(U_N^n)` for all integers `n`, with
`T_U(0)=N`, and

    D_U(m) = sum_pi mu(pi) product_(B in pi) T_U(n_B),
    F_(k,N)(U;W) = N^(-k) sum_(m in Z^d) W(m/N) D_U(m).  (1)

For `W=phihat`, (1) is exactly the factorial local statistic of the source.
The complete signed TRACE-005 discrepancy subtracts the specified ensemble's
corresponding `D` within (1). That reference subtraction cancels when comparing
`U` and a surrogate. This note neither changes the unfolding nor selects a
new symmetry class or averaging procedure. `N` is the actual matrix dimension
of the spectral block being compared. For the maintained full frozen family,
retain odd `N` and the literal fixed coupling.

The prior canonical [Heisenberg trace-support theorem](../trace-bridge/heisenberg_trace_support.md),
Section 3, already proves the general near-unitary integer-power bound and the
complete partition–Möbius error O(N^k epsilon), without any microscopic
correlation hypothesis and without assuming the approximant is unitary.
Sections 3–5 below rederive that existing perturbation mechanism for the two
explicit signed-table conventions; they are not a new general perturbation
lemma. The bridge's separate Section 8 concerns positive unitary spectral
measures and a bounded reference-correlation hypothesis.

The contribution here is the actual arbitrary-fixed-J one-step WKB
construction and its instantiation of that prior theorem, with explicit
adjoint-table bookkeeping and the subsequent exact-reciprocity route.
The four-branch source displays amplitudes through h a_1; Section 6 extends
that construction to every fixed finite order. No global-priority claim is made.

## 2. Two consistent signed trace conventions

Assume for now `delta=||U-V||op < 1`. Then

    ||V||op <= 1+delta,
    ||V^(-1)||op <= (1-delta)^(-1).                     (2)

Indeed `V=U(I+U*(V-U))`, and the second factor is invertible by its convergent
Neumann series. In particular every sufficiently large `V_(N,J)` is invertible.

### A. Laurent convention: exact distinct-index algebra

Define

    T_V^L(n) = Tr(V^n), n in Z,                         (3)

where negative powers are genuine inverses and `T_V^L(0)=N`. Let `D_V^L`
and `F^L(V;W)` be precisely the same partition polynomial and normalized sum
as (1), with this table substituted. If `lambda_1,...,lambda_N` are the
nonzero eigenvalues of `V`, with algebraic multiplicity, then exactly

    D_V^L(m) = sum_(j_1,...,j_k distinct)
                  product_(a=1)^k lambda_(j_a)^(m_a).  (4)

Triangularization gives `Tr V^n=sum_j lambda_j^n` for every integer `n`,
including negative `n`; Jordan blocks introduce no correction to this trace.
Ordinary partition inversion then proves (4). Neither normality nor
diagonalizability is required. This is a Laurent-polynomial identity. Since
the eigenvalues need not lie on the unit circle, it is not the source's
positive finite-circle factorial measure. In particular the pair expression is

    D_V^L(m,-m) = Tr(V^m) Tr(V^(-m)) - N,               (5)

and need not be real or positive after adding `N`.

### B. Adjoint convention: path-friendly signed trace surrogate

Alternatively set

    T_V^A(n) = Tr(V^n)                  if n > 0,
             = N                      if n = 0,
             = Tr((V*)^(-n))           if n < 0.       (6)

Use (6) only after forming each block sum `n_B` in the same polynomial (1).
This table satisfies `T_V^A(-n)=conjugate(T_V^A(n))` and gives

    D_V^A(m,-m) = |Tr(V^m)|^2 - N.                     (7)

It is convenient for expanding positive powers of the explicit WKB kernel
and conjugating the negative traces. However, it is **not** an exact
factorial eigenvalue formula for nonunitary `V`: signed exponents no longer
form a multiplicative character on each eigenvalue. For example, with `N=1`,
`V=[r]`, real `r != 1`, the distinct-index pair sum is zero whereas the
polynomial (7) equals `r^2-1`. For a legitimate Laurent table it is zero.

Thus (3) and (6) are two different, explicitly named surrogates. Do not write
`V^(-m)=(V*)^m`, and do not invoke positive-measure results for either surrogate.
Both agree with the exact table when `V=U` is unitary, and both satisfy (R).
Their complete transforms differ by at most twice the bound (R).

## 3. Positive and negative powers, with growth accounted for

Put `q=(1-delta)^(-1)`. For every integer `n`, either convention `bullet=L,A`
satisfies

    |T_V^bullet(n)| <= N q^(|n|),
    |T_V^bullet(n)-T_U(n)| <= N |n| delta q^(|n|).      (8)

At `n=0` the second expression is exactly zero. For `p>=1`, positive
powers telescope without any commutativity assumption:

    ||V^p-U^p|| <= delta sum_(j=0)^(p-1) ||V||^j
                <= p delta (1+delta)^(p-1)
                <= p delta q^p.                       (9)

For adjoint negative powers apply (9) to `V*` and `U*`.
For genuine inverses, an exact useful telescoping identity is

    V^(-p)-U^(-p)
      = sum_(j=0)^(p-1) V^(-(j+1)) (U-V) U^(-(p-j)).   (10)

Consequently its norm is at most
`delta sum_(j=1)^p q^j <= p delta q^p`. The operator bounds for the powers
follow from (2). Taking `|Tr X|<=N||X||op` proves (8).
This avoids assuming that the nonunitary matrix is power bounded for all
times. Only the displayed finite-time exponential growth is used.

## 4. Partition estimate and the exact normalization loss

For a partition `pi` with `ell` blocks let

    s_pi(m)=sum_(B in pi) |n_B|,
    s(m)=sum_(a=1)^k |m_a|.

Then `s_pi<=s`. Telescoping a product of `ell` scalar traces, using (8) and
`|T_U(n)|<=N`, gives the precise uniform bound

    |product_B T_V^bullet(n_B)-product_B T_U(n_B)|
        <= delta N^ell s_pi q^(s_pi).                 (11)

Each telescope term uses one trace difference, and all remaining `V` trace
factors contribute at most their corresponding powers of `q`; replacing the
remaining `U` factors by that same bound only enlarges the estimate. Zero-mode
blocks cause no error. In particular the one-block partition has `n_B=0`
and contributes exactly zero to the discrepancy.

The case `W=0` is immediate. Otherwise let `K=supp W` and set

    A_K = sup_(x in K) (sum_(a<k)|x_a| + |sum_(a<k)x_a|),
    M_N(W) = N^(-d) sum_(m in Z^d) |W(m/N)|.            (12)

Both are bounded for a fixed compact weight, with `M_N(W)<=C_W`. For example,
if `K subset [-sigma,sigma]^d`, then `A_K<=2d sigma` and the number of
frequency vectors is at most `(2 floor(sigma N)+1)^d`. Every included tuple
has `s(m)<=A_K N`. Thus (11), summed with the actual `N^(-k)` normalization,
gives

    N^(-k) sum_m |W(m/N)| |D_V^bullet(m)-D_U(m)|
      <= A_K delta M_N(W) q^(A_K N)
                    sum_pi |mu(pi)| N^(|pi|)
      = A_K delta M_N(W) q^(A_K N) N(N+1)...(N+k-1).   (13)

For the equality, permutations with cycle partition `pi` are counted by
`product_B (|B|-1)!=|mu(pi)|`; weighting every cycle by `N` gives the rising
factorial. Alternatively the standard insertion of the largest label proves
the recurrence `P_(k+1)(N)=(N+k)P_k(N)`, with `P_1(N)=N`.

In particular, for `delta<1`,

    |F_(k,N)^bullet(V;W)-F_(k,N)(U;W)|
      <= C_(k,W) N^k delta exp(A_K N delta/(1-delta)).  (14)

The signed difference is bounded by the left side of (13). The normalization
bookkeeping is worth recording separately:

- a worst trace-product difference has `k` traces, of size `O(N^(k+1)delta)`;
- the Fourier support has `O(N^(k-1))` lattice points;
- the bridge normalization is `N^(-k)`;
- the resulting error is `O(N^k delta)`, not `O(N delta)`.

For `k=1` (outside the microscopic-correlation target here), the only mode is
zero and the statistic is identical, so its error is exactly zero. When
`k>N`, the Laurent factorial identity vanishes on both matrices; the bound
remains true. The adjoint polynomial need not vanish for `k>N`, another reason
not to identify it with a factorial measure. The asymptotic theorem fixes `k`
first, so eventually `N>=k`.

## 5. WKB order, quantifiers, and TRACE-005 equivalence

Take `delta_N=C_J N^(-J-1/2)` for fixed integer `J>=1`. Then

    N delta_N = C_J N^(1/2-J) -> 0,

and the exponential in (14) is bounded and tends to one for every fixed
compact support. Formula (14) proves (R). A prescribed error `O(N^(-A))`,
with `A>0`, follows whenever

    J >= ceil(k+A-1/2).                               (15)

In particular `J=k` gives `O(N^(-1/2))`. The canonical displayed `J=1`
parametrix alone gives only `O(N^(1/2))` for pairs by this estimate and does
not suffice. This is not a proof of a nonvanishing error at `J=1`.

Let `R_(k,N)(W)` be the correctly selected finite-ensemble reference transform.
For every fixed `k,W`, choose any fixed integer `J>=k`. Then exactly

    F_(k,N)(U;W)-R_(k,N)(W) -> 0
        if and only if
    F_(k,N)^bullet(V_(N,J);W)-R_(k,N)(W) -> 0.          (16)

This holds separately for `bullet=L` and `bullet=A`. One fixed WKB order
`J=k` works for all individually fixed compact weights at that fixed `k`;
the constants and startup dimension may depend on the weight/support.
There is no uniform statement as `k`, bandwidth, or `J` grows with `N`.
No one fixed finite `J` gives the all-order conclusion from (14) alone.
If normalized positive averages are used and the norm estimate is uniform
in their parameter, the same error integrates unchanged. A general signed
averaging functional costs its total-variation/operator norm and needs a
separate bound.

The absolute estimate (13) compares two very close deterministic matrices or
trace tables. It does not assert the forbidden all-order absolute comparison
to CUE in TRACE-010. The remaining ensemble comparison in (16) must still
retain the full signed Fourier sum, including every partition counterterm.
If that signed comparison is proved for every compact support, apply the
repository's every-bandwidth extension to the **actual unitary spectra** of
`U_N`, whose positive factorial measures are available. Do not apply it
directly to a WKB surrogate.

## 6. Lemma: arbitrary fixed-order transport and Duhamel bound

This section records the finite-order extension needed if it is not supplied
by a companion. In `four_branch_parametrix.md`, replace `a_0+h a_1` by
`sum_(j=0)^J h^j a_j`. With that note's finite-shift coefficients `D_n=iP_n`,
solve successively

    (partial_t-D_1)a_j = sum_(n=2)^(j+1) D_n a_(j+1-n),
    a_0(0)=1,    a_j(0)=0 for j>=1.                   (17)

The right side contains only previous amplitudes. The same fixed-time
characteristic graph and gluing identities apply. For every fixed `J`, all
finitely many derivatives needed in the transport equations and Taylor
remainders are bounded on the fixed compact time interval and enlarged
fundamental charts. They may depend on `J` and the prescribed fixed coupling.
The source proves existence of the global analytic characteristic graph, so
higher finite derivatives are bounded on these compact charts; no growing-J
analytic estimate is asserted.

Expand the factored finite-shift operator through order J+1 with a Taylor
remainder O_J(h^(J+2)) before dividing by h in the generator. This gives
the required O_J(h^(J+1)) amplitude residual after division.
After Hamilton–Jacobi cancellation, the coefficient at order `h^j` is exactly
(17). The factored residual is therefore `O_J(h^(J+1))`. Including the kernel
prefactor `sqrt h` makes the entrywise residual `O_J(h^(J+3/2))`. The elementary
matrix bound `||R||op<=N max|R_ab|` gives `O_J(h^(J+1/2))`; unitary Duhamel on
the fixed time interval and the exact initial Gauss identity yield

    ||U_N(t)-V_(N,J)(t)||op <= C_J h^(J+1/2).           (18)

This is a finite-order extension of the existing one-step construction, not
a new long-time WKB construction. Long Heisenberg powers are controlled only
by the telescoping argument above. The general-amplitude expansion must
retain the same raw quantization, phases, gluing and initial conditions.

## 7. Decisive boundary and cheapest remaining test

The norm-level step is now reduced to explicit finite-order transport and
(R); it creates no model-specific cancellation. The remaining concrete
problem is to estimate the full signed transform in the right side of (16),
using **all** paths and Möbius counterterms. With convention A, all negative
traces are conjugates of positive WKB path sums, so this is often the cleaner
path-expansion target. With convention L, preserve inverse powers rather than
silently replacing them by conjugates; (R) justifies a separately declared
change to convention A if desired.

A useful immediate algebra check is the scalar `N=1`, `V=[r]` example in
Section 2; it catches the tempting but false adjoint-factorial identity.
Finite exact tests, when supplied alongside this note, test only partition
algebra and finite inequalities, not asymptotics, classical dynamics or
TRACE-005 itself. The analytic proof has independent internal review; no external-referee
or analytic formalization certificate is asserted.

Pinned source SHA-256 values:

- `mathematics/trace_to_local_statistics_bridge.md`:
  `8de10ab48a068363110753165a09a7a569111a04d743e575eed9f669bc8a64fd`
- `mathematics/signed_heisenberg_comparison.md`:
  `450e9c98720f4a6793b361611f2dee9d34531442efc521dacdcd902e1cc14313`
- `mathematics/fixed-map/four_branch_parametrix.md`:
  `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`

## 8. Verification and companion scopes

The portable exact rational controls are `computations/verification/heisenberg_wkb/check_independent.py`
and `check_raw_gauss.py`; the execution receipt records their bounded cases.
They do not prove analytic limits. [Exact reciprocity](exact_gaussian_reciprocity.md)
represents finite positive powers, with negative adjoint traces obtained by conjugation.
The [formal cluster lemma](uniform_cluster_lemma.md) and
[rotated-box theorem](rotated_local_first_loop.md) are local analytic dependencies,
not a global saddle decomposition or signed cancellation theorem.
