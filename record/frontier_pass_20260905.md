# Frontier pass — 2026-09-05

## Objective

The unchanged closure target is a rigorous microscopic BGS/RMT theorem for a
natural deterministic chaotic quantum system after all genuine symmetries are
resolved.  No finite-moment, eigenfunction, or numerical resemblance statement
is accepted as a substitute for a mean-spacing local-statistics theorem.

This pass produced two mathematically distinct advances and one literature lead.
It did **not** solve the full BGS conjecture.

## A. Frobenius amplification over minimal finite extensions

New file:

- `mathematics/cayley_frobenius_amplification.md`

New exact regression:

- `computations/verification/cayley_frobenius_extension.py`

For odd prime `K` and rational prime `p!=2,K`, put

```text
f=ord_K(p), q=p^f,
H=mu_K(F_q), A=c(H\{1}).
```

The non-forced Cayley-collision set is Frobenius-stable and every Frobenius
orbit has exactly `f` elements.  Therefore

```text
f | Delta_K^ext(p),
Delta_K^ext(p)>0 => Delta_K^ext(p)>=f.
```

The normalized collision-resultant argument extends from completely split
primes to every rational prime `p!=2,K` in the minimal extension:

```text
sum_p Delta_K^ext(p) log p
 <= (K^3-5K^2+6K+1)((K-1)log12-3logK).
```

The canonical difference-discriminant classification extends in the same
model:

```text
Delta_K^ext(p)>0 iff p | Disc(S_K),
Delta_K^ext(p)<=4 v_p(Disc(S_K)).
```

Combining the `O(K^4)` mass budget with Frobenius orbit size and the scarcity
of residue classes of multiplicative order at most `K^beta` gives:

> For every fixed `theta<1/3`, among unrestricted prime pairs
> `K~X^theta`, `p~X`, asymptotically almost every minimal-extension Cayley set
> has the exact baseline
> `E_+(A)=3(K-1)(K-2)`.

The proof uses only PNT, Brun--Titchmarsh, and `tau(n)=n^(o(1))` externally.
The exponent `1/3` is natural for this mechanism: the global mass is `K^4` and
Frobenius amplification is at most `K-1`, so a new saving in the global budget
is needed to go beyond it by this route.

### Independent finite checks

Two exact implementations were compared:

1. direct polynomial-basis arithmetic in `F_(p^f)`, explicit Cayley differences,
   and Frobenius-orbit decomposition;
2. factorization of `Phi_K` modulo `p` and independent sparse reduction of the
   collision polynomial modulo an irreducible degree-`f` factor.

They agree on

```text
(K,p,f,Delta)
=(7,13,2,32),
 (11,43,2,128),
 (13,3,3,432),
 (13,5,4,496).
```

For `K=7`, exhausting every odd `p!=7` below the universal resultant cutoff
`94` gives only `(13,2,32)`, matching the exact factorization
`Disc(S_7)=2^348 7^63 13^12`.

GitHub Actions run 115 executed the new regression and the full repository
Python/C++/Lean/TeX verification stack successfully.

### Scope warning

This is not an improvement of the original **split-prime** theorem: when
`p==1 (mod K)`, `ord_K(p)=1`, so Frobenius amplification disappears.  It is a
new exact theorem for the natural minimal-extension family and a structural
probe of what the split condition destroys.

## B. Exact trace-to-local-statistics bridge

New file:

- `mathematics/trace_to_local_statistics_bridge.md`

For an `N x N` unitary matrix `U` with eigenangles `theta_j`, define the
translation-invariant factorial microscopic `k`-point statistic by periodizing
a Schwartz test at scale `1/N`.

For every zero-sum integer tuple `m_1+...+m_k=0`, the distinct-index exponential
sum is exactly

```text
D_U(m_1,...,m_k)
 = sum_(pi in Pi_k) mu(pi)
   product_(B in pi) Tr(U^(sum_(a in B)m_a)),
```

where

```text
mu(pi)=product_(B in pi)(-1)^(|B|-1)(|B|-1)!.
```

Poisson summation then gives the exact microscopic identity

```text
C_(k,N)(U;phi)
 =N^(-k) sum_(m in Z^(k-1))
   phihat(m/N) D_U(m_1,...,m_k).
```

For compact Fourier support, only powers `|m|=O(N)` occur.  Thus the remaining
local-statistics closure can be stated precisely as a weighted joint-trace
comparison at **Heisenberg scale**, plus a high-frequency tail bound if the
band-limit is to be removed.

For `k=2`,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr(U^m)|^2-N).
```

Hence fixed trace moments or fixed fourth moments are mathematically
insufficient for microscopic BGS unless supplemented by a mechanism controlling
`Theta(N)` trace powers.  This closes the deterministic Fourier bridge itself;
it does not prove the required arithmetic trace estimates.

A direct finite numerical red-team of the partition-Mobius identity for
`k=2,3,4` on a five-point rational eigenangle spectrum agreed to floating error
`<1.1e-14`; the proof in the note is exact and does not depend on that test.

## C. Concurrent main-branch refinement: coefficient ideals

While this pass was running, `main` advanced with

- `mathematics/cayley_product_row_coefficient_ideal.md`,
- `computations/verification/cayley_product_row_coefficient_ideal.py`.

That refinement replaces the gcd of separate coefficient norms by the actual
subresultant coefficient ideal `J_(K,r)^(3)` and its contraction
`D_(K,r)^(3) Z=J intersect Z`.  This is arithmetically sharper because one
realized finite-field row intersection forces a **single** prime ideal above
`p` to contain all relevant coefficients.  The surviving split-prime closure
problem is to bound the split rational prime divisors of `D'_K^(3)` (or prove a
subpolynomial row-intersection bound on its support).

The Frobenius theorem and the coefficient-ideal theorem are complementary:

- coefficient ideals sharpen the residue-degree-one (`split`) exceptional
  support;
- Frobenius amplification exploits residue degree away from the split slice.

Neither currently implies the other.

## D. Literature lead: short root-of-unity congruences

A targeted search identified R. Dvornicich and U. Zannier,
*Sums of roots of unity vanishing modulo a prime*, Arch. Math. 79 (2002),
104--108, DOI `10.1007/s00013-002-8291-4`.

Its abstract states that it extends the Conway--Jones classification inequality
from characteristic-zero linear relations among roots of unity to congruences
modulo a prime.  This is potentially relevant because three product-row
intersections yield simultaneous sparse cyclotomic-unit / root-of-unity
congruences.

**Status: lead only.**  The exact theorem hypotheses and inequality have not yet
been matched to the product-row equations, so no consequence for `D'_K^(3)` is
claimed here.

## E. Current frontier after this pass

### Established

1. The maintained split-prime Cayley/resultant/discriminant/Jacobi chain remains
   intact under the full CI regression stack.
2. Minimal-extension Frobenius amplification gives a new density-one exact
   quadratic-energy theorem for every `theta<1/3` in the unrestricted-prime
   family.
3. The deterministic local-statistics bridge is now explicit: the missing BGS
   input is a weighted Heisenberg-scale joint-trace comparison, not merely an
   unspecified `local law`.
4. The newest split-prime arithmetic obstruction is the canonical
   coefficient-ideal divisor problem from current `main`.

### Open

1. **Split pointwise Cayley energy.**  Prove
   `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))`, or enough of it on the actual exceptional
   support.
2. **Coefficient-ideal divisor problem.**  Control split prime divisors of
   `D'_K^(3)` strongly enough for growing `K`.
3. **Heisenberg trace problem.**  Prove the weighted trace criterion from
   `trace_to_local_statistics_bridge.md` for the desymmetrized quantum spectrum
   at powers `Theta(N)`.
4. **Symmetry resolution.**  State and verify the exact quantum-map symmetry
   class before any GOE/COE/GUE/CUE comparison.
5. **General BGS.**  No theorem for all chaotic systems has been proved here;
   extra arithmetic symmetries and known counterexample mechanisms show that a
   universal statement without hypotheses is not mathematically well posed.

## F. Repository state

Research branch:

```text
frontier/frobenius-bgs-20260905
```

Draft PR:

```text
#12 Frobenius amplification for minimal-extension Cayley collisions
```

The PR is intentionally draft.  `main` advanced concurrently after the branch
was cut, so the branch currently diverges from `main`; no merge should occur
until the new `main` changes are reconciled and the final PR-head CI run passes.
