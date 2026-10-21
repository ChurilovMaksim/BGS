> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_original_every_power_minors_audit.md`. Embedded SHA256: `e8fb0c39dea826c97e2358eead00d46657f9ad8d6151e936277e139a6df3ecea`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/algebra.md).

# Independent audit of every-power physical minors

21 October 2026. This audit checks the complete written source
`root_original_every_power_minors.md` at SHA-256
`9d3503703b5a5b0df580bb1a2a42e58a0617c7de94c3b340ac26d9ec93d54a48`.
The original-family theorem in Sections 1–7 is accepted without a
requested mathematical correction. The auxiliary countermodel
mentioned in its final paragraph is outside this audit's scope.

## 1. Fixed physical columns are the decisive distinction

For $C=Q^*M_N$, the Cauchy--Binet expansion of
$\det C[E,J]$ has only one variable coordinate set, $S$.
Its extreme is $S_0=\{N-k,\ldots,N-1\}$. The physical
column set $J$ stays fixed. After transposing, all Fourier
alternants therefore use the same distinct root-of-unity nodes.
Their common Vandermonde cancels in the ratio even when its
valuation is positive. The consecutive exponents at $S_0$
leave a unit monomial, while every other Schur quotient is
integral. This verifies the ratio inequality in the source's
equation (3.3) for arbitrary composite $N$ and arbitrary $J$.

Combining it with the endpoint Jacobi minor bound costs at most
half of the positive index-sum defect; the gauge contributes
the full defect. Hence the $S_0$ term uniquely dominates.
The claimed total nonsingularity of $Q^*M_N$ follows. There
is no replacement of an arbitrary mixed-component Fourier minor
by a presumed Vandermonde.

## 2. Exterior evolution of a power

The source's equation (5.1) follows exactly from multiplication
of the exterior matrices of
$$
Q\operatorname{diag}(e^{sa_j})
B\operatorname{diag}(e^{sa_j})\cdots
B\operatorname{diag}(e^{sa_j})C.
$$
There are $r$ diagonal exponential factors and $r-1$
intermediate factors $B=Q^*M_NQ$. Each exterior state has a
sum of $k$ distinct $A_N$-eigenvalues. The maximum is
unique at the top $k$ state. Therefore the unique largest
frequency in a power minor is $r(a_1+\cdots+a_k)$, with
coefficient
$$
\det Q[I,E_k],
\det B[E_k,E_k]^{r-1},
\det C[E_k,J].
$$
The first factor is nonzero by the positive connected additive
compound of the Jacobi path; the second by the frozen two-sided
valuation theorem; the third by Section 1 above. All factors,
all frequencies, and the prescribed nonzero specialization are
algebraic. The qualitative Lindemann--Weierstrass theorem applies
after equal lower frequencies have been collected. This verifies
every positive integer power without a uniformity claim in the
power or dimension.

## 3. Inversion and support assertions

The source proves the complementary-minor inverse identity by
a block Schur-complement calculation and polynomial continuation.
Applying it to a positive power proves every negative power,
including nonreal algebraic parameters. The empty complementary
minor is handled as 1.

The support inequality follows by choosing as many zero output
rows as there are nonzero input columns and applying a nonzero
square minor. Its sharpness argument also checks: an
$(s-1)$-by-$s$ restriction has a one-dimensional nullspace;
every coordinate of its null vector is nonzero because deleting
any column gives a nonzero minor, and any additional output zero
would give a singular $s$-square minor. This covers the boundary
cases $s=1$ and $s=N$.

## 4. Scope

The theorem requires $7\nmid N$. The independent companion
`r7_original_all_odd_component_minors.md` extends the one-step
argument to every odd dimension for row sets lying in a single
Jacobi component, without claiming arbitrary mixed-component rows
or higher powers there.

All results in this audit concern exact nonvanishing and supports.
They do not give lower bounds for minors, eigenvector coordinates,
or the weighted signed trace sums required in $H_{\rm diag}$.
