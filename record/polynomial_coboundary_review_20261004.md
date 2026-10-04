# Research and proof review: polynomial original-coboundary limits

Date: 4 October 2026. Repository base:
`a25c0d2573b5232a676cfccf1dc79da8e4cd2956`.
Claim: **BGS-FLOW-011**. Correction: **ERR-026**.
Current status authority remains [the claim ledger](claim_ledger.md).

## 1. Frozen target and extent of this pass

The overarching target remains the full microscopic BGS programme, with
the quantization, unfolding, symmetry sector and averaging convention
specified. For the maintained odd-dimensional family it is BGS-BGS-001;
the load-bearing open estimate is BGS-TRACE-005, the signed weighted
factorial joint-trace comparison at Heisenberg times, for **every fixed
order** and compact smooth Fourier weight. The coupling remains fixed at
$\tau=10^{-80}$. No ensemble replacement or varying-coupling limit is
accepted as a solution of that target.

The structural audit covered the maintained repository, its references,
generated sources, topic map and scientific dependency graph. Detailed
proof reading covered the Gaussian covariance, Möbius diffusion,
joint-limit chain and quantitative inputs, and the fixed-time/Heisenberg
and finite-orbit/analytic boundaries. This is not a fresh complete referee
audit of every inherited proof. Material was kept at stable paths; no
unread proof or historical promoted evidence was discarded for appearance.

An unqualified theorem for all classically chaotic quantizations needs
additional hypotheses: arithmetic quantum symmetries and degeneracies
already occur in hyperbolic torus maps. The
[bounded primary-source check](../literature/bgs_scope_and_polynomial_flow_20261004.md)
records this issue and the prior Dyson clock mechanism. This clarification
does not turn a known exception into a new BGS result.

## 2. Research tree and actual outcomes

| Route and attempted continuation | Outcome of this pass | Missing input / next step |
|---|---|---|
| Extend fixed-time packet traces or small fixed-coupling perturbation to $m\asymp N$ | No Heisenberg estimate. Fixed-time constants and localization orders are not uniform in $m$. Telescoping only gives $\|U_N^m-M_N^m\|_{\rm op}\le\min(2,C|\tau|Nm)$ for the bounded finite-Fourier generator; at $m\asymp N$ and fixed $\tau$ this becomes trivial. | Prove cancellation for the actual signed weighted factorial sum, keeping counterterms. Scalar finite type or an auxiliary mixing gap does not supply this estimate. |
| Extend finite Fourier-orbit resonance rigidity to every analytic observable by truncation | No arbitrary-analytic theorem. The isolation threshold depends on the finite family; FO.17 introduces arbitrarily late new-family collisions. Positivity for each truncation supplies no uniform positive lower bound. | Obtain quantitative coercivity stable under adding infinitely many analytic Fourier orbits, or an exact all-orbit cancellation classification. RES-003 stays open. |
| Remove dimension growth from the original random-coboundary weak comparison | **Closed scoped subproblem.** Normalized covariance derivatives, explicit contracted drift and positive Laplace tests give FLOW-011. The original steps, independence and clock start are preserved. | Optimize the polynomial exponent; prove relaxation from the actual spectrum and a separate noise-removal theorem. Neither follows from the clock result. |

These outcomes do not exhaust approaches to BGS. A growing subprincipal
transfer idea was checked against the earlier
[transfer note](../mathematics/fixed_map_moment_control_and_transfer.md)
and not presented as new: that note already contains the relevant
quantum-ergodic small-displacement argument.

**Continuation after resumption.** A spectral transplantation route was
examined: sort the actual equidistributed eigenangles and replace them by
a simple, slightly perturbed clock in the same eigenbasis. The quantile
matching error tends to zero, so leading operator-norm Egorov survives,
while the local law becomes rigid. This cannot prove universality.
The decisive limitation is already in
[the maintained spectral-resolution proof](../manuscript/unified_sections/spectral_resolution.tex):
even an $O(N^{-1})$ Egorov-preserving spectral rounding permits collapsed
spacings with simple spectrum. The proposed route therefore receives
no new claim ID or priority assertion. A fixed smooth microlocal symbol
class must remain part of any meaningful quantization contract.

## 3. The closed polynomial subproblem

The original chain is

$$
U_{j+1}^\varepsilon=
e^{i\varepsilon(G_j-U_j^\varepsilon G_jU_j^{\varepsilon *})}
U_j^\varepsilon,\qquad U_0=C_N,
\quad \mathbb E(G_j)_{ab}(G_j)_{cd}
=N^{-1}\delta_{ad}\delta_{bc}.
$$

For odd $N\ge3$, $h=\varepsilon^4/2$, $n=\lfloor t/h\rfloor$,
$1/N\le t\le1/12$, sufficiently small $\varepsilon$ and a nonnegative
$f\in C_c^\infty(\mathbb R)$, the
[proof](../mathematics/coboundary_polynomial_limit.md) gives

$$
\left|\mathbb E\Phi_{N,f}(U_n^\varepsilon)
-\Phi_{\mathrm{Sine}_2}(f)\right|
\le C_f\left[\sqrt t+(Nt)^{-1}+N^{-2}
+N^4\varepsilon+tN^9\varepsilon+tN^{10}\varepsilon^2\right].
$$

The observation origin is independently uniform. Thus $t=N^{-2/3}$,
$\varepsilon=N^{-26/3}$ and **exactly $n=2N^{34}$** give
$O_f(N^{-1/3})$. The discretization contributions are $N^{-14/3}$,
$N^{-1/3}$ and $N^{-8}$. Approximation gives the weak limit for
nonnegative $C_c^1$ tests without asserting the rate at that regularity.

The exponent is a conservative proof bound, not a practical simulation
claim. This is a stochastic weak local law; unbounded factorial
correlations require separate uniform integrability.

The elementary bounded-counting corollary P19 gives, for a fixed interval
$I$, $\mathbb E z^{X_N(I)}\to\det(I-(1-z)K_I)$, $0\le z\le1$.
In particular hole probabilities converge to the Sine$_2$ hole law.
Its proof uses uniform-origin unit intensity and smooth $L^1$ approximation;
it asserts no rate for indicators or higher moment control.

## 4. Proof obligations and checking boundary

| Obligation | Resolution and scope |
|---|---|
| Preserve the uncentered chain | P1 and retained P4–P6 use FLOW-010's chain. No centering or covariance whitening is inserted into the random algorithm. |
| Fixed noise space and norm | Real traceless Hermitian Hilbert space with a fixed orthonormal basis; distinguish matrix HS and superoperator HS norms. |
| Square-root derivatives | P7 bounds $D^r(N\mathcal C_U)$ by $C_r$ in operator norm and $C_r\sqrt N$ in superoperator HS norm. A differentiated square-root resolvent places one factor in the latter norm; exterior $N^{-1/2}$ cancels $\sqrt N$. |
| Projected noise derivatives | The rank-two projection and right multiplication by a direction give $\big(\sum_a\|D^r(iL_aU)\|_{\rm HS}^2\big)^{1/2}\le C_r$ for positive fixed orders. |
| Contracted drift and off-slice extension | P11–P12 give exact contractions for every unitary. Residual coefficients are $N^{-2}$ rational combinations with denominators uniformly separated from zero. |
| Cutoffs and stochastic flow | Normalized-trace cutoff derivatives pay $N^{-1/2}$ against zeroth-order $\sqrt N$ coefficients. A unitary-preserving full-group extension bounds variations along unitary base paths. Even-moment induction yields $\|S_sF\|_6\le Ce^{Cs}\|F\|_6$. No global ambient elliptic-regularity assertion is used. |
| Fast coordinate | Preserve $\rho=\varepsilon/N+\varepsilon^4$ in the stopped sum, obtaining $\varepsilon/N+\varepsilon^2$ instead of $O(\varepsilon)$. P4–P6 remain inherited inputs. |
| Time remainders | Relative to $tN^4\varepsilon^2\|F\|_6$, the ratios are $\varepsilon^2/(2N^2)$ and $\varepsilon^2/(2tN^3)$; both are absorbed when $t\ge1/N$. |
| Microscopic sixth derivative | Positivity gives first trace derivative $C_fN\sqrt A$, $A=\operatorname{Tr}f_N(U)\ge0$. Higher traces use two Schatten-2 direction factors. Partition differentiation of $e^{-A}$ gives $\|\Phi_{N,f}\|_6\le C_fN^6$, including collisions and high local occupancy. |
| Relaxation and terminal centering | FLOW-009 and FLOW-007 supply the inherited inputs. The equispaced Dyson kernel is credited prior work, with the project's time normalization and alias bound. |

One separately tasked internal reviewer read the proof and stated inputs
without editing the derivation, and independently checked new P7–P18
and the final calibration. It found no load-bearing gap in these estimates.
It did **not** independently re-prove all inherited P4–P6 inputs or the
external Dyson kernel. This is an independent internal check, not an
external referee report or Lean certificate. Author review additionally
checked the retained inequalities and stopped telescoping in FLOW-010.

## 5. Scope correction

FLOW-010 already bounded the error by
$C_f[\sqrt t+(Nt)^{-1}+N^{-2}+N^{20}e^{CNt}\varepsilon]$.
Set $t=L_N/N$, $L_N\to\infty$, $L_N=o(\log N)$,
$\varepsilon=N^{-a}$, $a>20$. Its last term is $N^{20-a+o(1)}$,
and all others vanish. For example $L_N=\log N/\log\log N$ suffices
eventually. Thus the former “no polynomial-step regime” interpretation
was false. This corollary uses none of the new derivative estimates.

ERR-026 distinguishes this immediate corollary from rate-preserving
FLOW-011. The dated 30 September audit and immutable evidence remain
historical. The previous quantitative theorem is not retracted.

## 6. Reproducible finite evidence

The [verifier](../computations/verification/coboundary_polynomial_limit.py)
and [bounded execution manifest](../evidence/executions/20261004/polynomial-coboundary/manifest.json)
pin final source, software versions, seed and resource limits.
The [result](../evidence/executions/20261004/polynomial-coboundary/checks.json)
contains **40 matrix-direction cases** at $N=3,5,7,9,13$: clock and
warped spectra, two trace-aligned and two seeded Hermitian directions.
It compares analytic covariance and Sylvester square-root derivatives
with central differences and checks exact noise/drift contractions.
Maximum projected-noise derivative discrepancy is $2.540\times10^{-10}$,
against tolerance $2\times10^{-7}$. These are complex128 diagnostics,
not uniform derivative certificates. The drift derivative is only a
central-difference diagnostic.

Exact rational arithmetic checks exponent identities and all 278 set
partitions in orders one through six. The
[Wolfram code](../computations/wolfram/polynomial_coboundary_controls.wl)
was evaluated; its
[response](../evidence/20261004/polynomial_coboundary_wolfram.json)
checks exponents, the slow-time substitution and a sixth scalar Gaussian
derivative. It does not certify the stochastic theorem. A preliminary
conservative calibration was sharpened before promotion; only the final
source and run are promoted.

Direct replay:

```bash
python3 computations/verification/coboundary_polynomial_limit.py \
  --output build/polynomial-coboundary-replay.json
```

The standard `verify_workspace.py --only coboundary_polynomial_limit`
entry supplies the output argument. Focused inherited verifiers and
publication checks are recorded in the
[integration execution record](../evidence/executions/20261004-polynomial-integration.json).
Execution coverage and source stability are not proof of mathematical truth.

## 7. End state and continuation

Proof, claim metadata, dependencies, topic navigation, current scope
statements and the generated manuscript chapter are synchronized.
Temporary builds and preliminary runs are outside promoted source.
The user explicitly requested work on `main`; synchronization is performed
without forcing history.

The full BGS goal has not been reached. FLOW-011 closes a named
quantitative stochastic subproblem. External priority and Fields/Poincaré
significance are unestablished. The next inputs remain actual-map signed
Heisenberg factorial cancellation, quantitative relaxation for its starting
spectrum, and a noise-removal argument not contradicted by the clock example.
