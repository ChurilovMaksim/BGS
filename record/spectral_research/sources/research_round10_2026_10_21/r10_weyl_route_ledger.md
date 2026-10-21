> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round10_2026_10_21/r10_weyl_route_ledger.md`. Embedded SHA256: `c3c8d7b3bd9d3fdfe2a3390f8cc793ed6ad48b57ff84bbd98ea4cbb904586a2d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Round 10 Weyl branch: actual results, failed contractions, and remaining estimate

21 October 2026. Branch `/root/r10_weyl`.

Base master SHA-256:
`e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777`.
No historical proof or master file was edited. Branch writes are confined
to the Round 10 `r10_weyl_*` files.

## 1. Target retained exactly

The original matrices, fixed `tau=10^(-80)`, and every odd dimension
remain the target. The first specific undecided observable remains

$$
\phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
b_*(x)=\frac{|\mathcal F^{-1}\phi(x)|^2}{2(\int\phi)^2},
\quad w=|\widehat b_*|^2,
$$

$$
\boxed{
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)
\stackrel{?}{\longrightarrow}0.
}
\tag{1.1}
$$

This branch has neither proved (1.1) nor produced a positive fixed
discrepancy along an infinite subsequence of the prescribed matrices.
There is no claim that the target is false or impossible. The new
theorems below concern logical consequences and stability of a full
fixed-order hypothesis; they are not estimates establishing that
hypothesis for this family.

## 2. The full signed Weyl resummation was read before trying to extend it

The two raw Round 8 proofs were read in full. In the original modular
Weyl convention, they already prove

$$
\mathcal S_m(\Gamma)
=\sum_{v:(S^m-I)v=\Gamma}((\operatorname{Ad}U_N)^m)_{v,v}
\tag{2.1}
$$

for every odd modulus and every time, including all singular fibers.
Their positive endpoint-preserving sector is

$$
\mathcal S_m(0)=|\ker(S^m-I)|\,
\|\mathsf P_{\ker(S^m-I)}(U_N^mM_N^{-m})\|_{2,N}^2.
\tag{2.2}
$$

When `S^m-I` is invertible, this one sector equals one. Other
sectors remain the diagonal entries of the coherent adjoint power.
The exact relative-path cancellation does not replace that unitary
matrix by the modulus square of its entries.

The attempted improvement by inserting a large-label one-step
entry bound fails at a precise point: Cauchy--Schwarz in one
intermediate Weyl index gives only

$$
|((\operatorname{Ad}U_N)^m)_{v,v}|
\le\|\text{row}_v(\operatorname{Ad}U_N)\|_2
\|\text{column}_v((\operatorname{Ad}U_N)^{m-1})\|_2=1.
$$

Using a maximum-entry estimate instead multiplies it by the
column `l^1` norm, bounded only by `N` on an `N^2`-dimensional
Weyl space. The existing weak power decay of a single entry
does not survive that loss. This calculation was already present
in the raw proof and is not relabeled as a Round 10 advance.

## 3. Positive full-time weighting: a genuine discriminator, not a solution

The next proposal was to take the complete time weight before
attempting a positive decomposition. This does give a positive
operator, but its unresolved component retains all unequal phase
gaps. The following elementary calculation makes the issue explicit.

For a real nonnegative Schwartz `b`, let

$$
w=|\widehat b|^2,\qquad
c(x)=\int_{\mathbb R}b(y)b(y-x)\,dy\ge0,
$$

so that `c` is even and is the inverse Fourier transform of `w`.
If `b` is admissible, define the finite Laurent polynomial

$$
F_{N,w}(z)=\sum_{m\in\mathbb Z}w(m/N)z^m.
\tag{3.1}
$$

Its values on the unit circle are nonnegative:

$$
F_{N,w}(e^{2\pi it})
=N\sum_{\ell\in\mathbb Z}c(N(t+\ell))\ge0.
\tag{3.2}
$$

For a direct verification without an unexamined Poisson formula,
the smooth periodic function on the right has Fourier coefficient

$$
\int_0^1N\sum_\ell c(N(t+\ell))e^{-2\pi imt}dt
=\int_{\mathbb R}c(x)e^{-2\pi imx/N}dx=w(m/N).
$$

The Fourier series is finite because `w` has compact support;
uniformly convergent periodization and Fourier inversion prove
(3.2). Functional calculus for the unitary `C_N=Ad U_N` now gives
`F_(N,w)(C_N)>=0`, and the exact trace identity is

$$
\frac1{N^2}\sum_{m\ge1}w(m/N)|\operatorname{Tr}U_N^m|^2
=\frac{\operatorname{Tr}F_{N,w}(C_N)-N^2w(0)}{2N^2}.
\tag{3.3}
$$

If `d_N` denotes the rank of the full commutant of `U_N`, its
exact contribution to the trace on the right is `d_N F_(N,w)(1)`.
The remaining contribution is

$$
\sum_{\lambda_a\ne\lambda_b}
F_{N,w}(\lambda_a/\lambda_b),
\tag{3.4}
$$

with the eigenvalues counted with multiplicity. Positivity of (3.4)
does not determine its value. It contains the original microscopic
gap statistic through (3.2). In particular, the universal lower
bound `d_N>=N` gives only

$$
\frac1{N^2}\sum_{m\ge1}w(m/N)|\operatorname{Tr}U_N^m|^2
\ge\frac{N F_{N,w}(1)-N^2w(0)}{2N^2},
\tag{3.5}
$$

besides the trivial nonnegative lower bound. No CUE matching upper
bound follows from it.

The raw Round 3 commutant/resolvent proof was then read. It already
identifies this obstruction for the exponential time weight, and
proves that retaining the true commutant leaves every unequal gap
denominator. The compact-band calculation (3.1)--(3.5) is recorded
as the outcome of the proposed discriminator, not as a new mechanism
for evaluating (1.1). No phase-gap information was manufactured by
renaming the same spectral functional.

The complementary coordinate-field inverse in that old proof also
has many slow singular directions for the actual family. Thus no
uniform operator contraction of that complement was assumed here.
The separately read classical/prequantum scope discussion likewise
does not convert a classical weighted transfer gap into an estimate
of the full quantum adjoint trace.

## 4. New theorem: fixed-order repulsion supplies fixed-order uniform integrability

The real change from Round 9 is the moment-transfer argument.
The old raw proof was read, including its eigenangle matching and
its use of order `k+1` to transfer order `k`. The question was
whether the target's own same-order repulsion removes that extra
moment requirement.

Let `H_k` denote the complete order-`k` part of the criterion:
every admissible nonnegative bandlimited Schwartz test, with each
band fixed before the limit. The new note
`r10_weyl_orderwise_repulsion_stability.md` proves that `H_k`
implies uniform integrability of the `k`-th power of every fixed
local count. More precisely, for every length-`L` interval and
every positive integer `M`,

$$
\limsup_N\mathbb E[
X_N(I)^k\mathbf1_{X_N(I)>2kM}]
\le C_{k,\beta}L^{k^2}M^{-k(k-1)}.
\tag{4.1}
$$

The proof has no hidden higher moment. It constructs an explicit
positive bandlimited majorant for a small interval and uses the
finite CUE bound

$$
M^{\mathrm{CUE}}_{k,N}(\beta(\cdot/\delta))
\le A_{k,\beta}\delta^{k^2}.
$$

That bound is obtained from an exact Gram representation and a
Vandermonde estimate proved by divided differences of exponential
Hilbert-space vectors. A pigeonhole inequality then gives (4.1).
The order of limits is fixed `M`, then dimension, then `M->infinity`.
The estimate is not improperly integrated over growing truncation
scales to assert uniform higher prelimit moments.

Consequently, under the actual Round 9 type of matching

$$
\max_a N|\varepsilon_{a,N}|\le C,
\qquad\sum_a|\varepsilon_{a,N}|\to0,
$$

after the common scalar rotation, the theorem proves

$$
\boxed{H_k(U_N)\iff H_k(V_N)}
\tag{4.2}
$$

for each fixed `k` separately. Local count domination transfers
uniform integrability to the second endpoint; summable unit-cell
Schwartz tails and the exact origin-integrated displacement estimate
finish the factorial-moment comparison.

This strengthens the previous equivalence requiring a complete
all-order hypothesis at the source. It does not transfer an isolated
test merely from convergence for that test. In particular, it does
not yet transfer a solution of (1.1) alone from a normalized endpoint.

## 5. New theorem: one complete order contains every lower order

The parent suggested testing whether the same-order result implies
downward consistency of the whole criterion. The new note
`r10_weyl_downward_moment_heredity.md` proves

$$
\boxed{H_k\Longrightarrow H_j\quad(1\le j\le k).}
\tag{5.1}
$$

It works directly on the prelimit processes, with no ergodicity or
assumed weak point-process limit. Its distinct substantive steps are:

1. Same-order uniform local `L^k` control makes approximation in
   the summable unit-cell supremum norm valid for factorial moments.
   This extends bandlimited diagonal tests to smooth compact tests.
   Positive rescaled polarization gives all compact mixed tests.
   Boundary-strip approximation uses exact intensity and uniform
   integrability to include interval indicators.
2. For `Y_(N,R)=X_N([0,R])/R`, an exact map-counting inequality
   and the limiting `k`-th factorial density bounded by one give

   $$
   \limsup_N\mathbb E|Y_{N,R}-1|^k\le C_k/R.
   $$

   The linear term in `x^k-1-k(x-1)` cancels because intensity
   is exactly one. No ergodic theorem is invoked.
3. Normalize a mixed `k`-th moment with `k-j` count variables
   in `[0,R]` by `R^(k-j)`. Given the selected local tuple,
   the exact number of additional allowed choices is
   `(X_N([0,R])-d)_(k-j)`, with its selected-point count
   `0<=d<=j` explicitly removed. Hölder gives a comparison
   error `O_(h,k)(R^(-1/k))` with the local `j`-th moment.
4. A direct sine-determinant permutation expansion contracts the
   free variables, with error bounded by `sqrt(3) k! R^(-1/2)`.
   Finally, Schwartz tails return to the exact distinct-label
   criterion rather than accidentally allowing distant periodic
   copies of one eigenvalue label in its factorial sum.

An unbounded collection of complete orders is therefore equivalent
to the all-order criterion. This is a statement about the quantifiers
of a proved hypothesis, not a method for proving that hypothesis
for the original matrices. It does not determine any higher order
from a fixed finite order, or start from the one test `b_*`.

## 6. Independent checking and exact outcome

Both mathematical proofs received independent arithmetic-branch
audits with passing verdicts. The parent also read the full descent
proof and accepted its mathematical chain. Corrections before the
hashes were frozen were limited to LaTeX escapes, restoration of
one raw carriage return to the intended literal backslash-r in
`\\rm distinct`, and a tightening of the displayed Fourier-support
containment of `beta(x)=|g(x/8)|^2/(2I^2)` to `[-1/4,1/4]`.
The final branch files were also checked for unexpected control bytes;
none remain.

No finite computation at machine-zero `tau` was performed or offered
as asymptotic evidence. The two mathematical proofs are elementary
and self-contained given their explicitly proved companion inputs;
no external literature claim of historical novelty is made.

The exact first missing family-specific estimate is still (1.1).
Neither a coherent weighted contraction at Heisenberg time nor an
original fixed-test obstruction was found in this branch. The
new results remove a same-order integrability gap and prove a
downward logical implication in the criterion, while leaving its
unproved original-matrix premise visible.

## 7. Actual inputs and output hashes

Hashes below were computed on the actual file bytes. The two Round 8
proofs, Round 9 stability proof and route ledger, Round 10 checkpoint,
and Round 3 commutant proof were read in full. For the prequantum
scope discussion, Sections covered by lines 1--245 were read; no
claim of a full-file read is made for that one input. An attempted
read of `research_round4_2026_10_21/dual_coherent_fejers.md` found
no such file and supplies no input.

| File | SHA-256 |
|---|---|
| `research_round10_2026_10_21/round10_target_checkpoint.md` | `a35e09d5678b1f718f7deaa1c726afa5c692886010eb41f748e8f9f1624378f0` |
| `research_round9_2026_10_21/r9_sector_route_ledger.md` | `ad07baa0fae652ea65f15e41dc931840a7d6046ebf30abac9a62d819e80b41e2` |
| `research_round9_2026_10_21/r9_sector_continuous_symbol_stability.md` | `0145256f03ad92f70a5852ecb11280dc3b1bccfa54b74af8b70e459b2e6577df` |
| `research_round8_2026_10_21/r8_weyl_full_weight_relative_path_cancellation.md` | `038d6c03710c38829fba3d96367d271f5c33cdeacf94889d32cc3d7a22070109` |
| `research_round8_2026_10_21/r8_weyl_all_odd_endpoint_fiber_identity.md` | `ec36b997ef3a38dd464d468833f78a3934b45bdc57dbc36f54987aa42a649b70` |
| `research_round3_2026_10_21/phase_commutant_integration_discriminator.md` | `df3c9b16210c64341f804ff28a0dd30beb366a0610016168edcb72fab5f0052a` |
| `research_round3_2026_10_21/phase_prequantum_dolgopyat_scope.md` | `91215713938e76debb628149d578fca00e3f22a872d98e8e02a42628876640cb` |
| `research_round10_2026_10_21/r10_weyl_orderwise_repulsion_stability.md` | `63ddeba5e72b200bf3dd16bed795423d4ed7e070a0b0e3f55fa30b93d3bc53d2` |
| `research_round10_2026_10_21/r10_weyl_downward_moment_heredity.md` | `ba5e5fb7b2d812c8b9a9f28f2f555412399d0e749d941af2723137be206c65dd` |

