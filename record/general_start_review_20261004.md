# Research checkpoint: actual-start comparison and circular relaxation

Checkpoint: `general-start-20261004`; base main
`4982f8fc3d6303cc2cf7840e608f07d41ba2783e`.
The unchanged terminal target is BGS-BGS-001 at fixed $\tau=10^{-80}$,
with BGS-TRACE-005's signed weighted factorial joint traces at $m\asymp N$
for every fixed order. Four scoped project implications are proved below.
The random chain is an auxiliary route; deterministic BGS remains open.

## 1. Executed portfolio and evolution of the routes

| Route | Central move and first uncertain implication | Outcome / continuation |
|---|---|---|
| Retain the original initial spectrum | Sum the fast first-trace transient and check frozen stopped Lyapunov control before any union bound. | FLOW-012 proved: exact centered reference start and additional $N^9\varepsilon^2$ cost. |
| Import real-line relaxation | Check the exact initial regularity, polynomial scales, geometry and unfolding. | No import: the verified theorem does not apply to this circular logarithmic-scale setup. |
| Falsify prescribed-time low-trace relaxation | Balanced narrow clusters, exact Brownian HS displacement and uniform-origin geometry. | FLOW-013 proved: schedule-dependent empty noisy limits, preserving global uniformity and fixed trace bounds. |
| Use the longer maintained trace window | Inspect FM-007's actual $c\log N$ estimate. | FM-017 proved: logarithmic initial Poisson regularity, local stationary points and unweighted phase tails. It does not select $N^{-2/3}$. |
| Resummed circular kernel | Recover the prior finite formula, sum interpolation before taking absolute values, retain crossing residues and all windings. | FLOW-014 proved: gap-independent global bound, confluence and full Fredholm limit; sharpened actual time $t=8g$. |

FM-007 already owned the logarithmic trace input, and FM-013 owned bounded
unnormalized fixed traces. The initial family in FLOW-013 depends on the
selected time. An obstruction to a universal prescribed schedule does
not rule out a slower schedule selected for a given family. At
$t=N^{-2/3}$ its falsifier even satisfies the whole FM-007-type logarithmic
upper bound; it is not a realization of the actual frozen map.
Earlier intensity-loss examples, the clock noise-removal obstruction and
the algebraic perturbation mechanism are prior inputs. No priority is asserted.

## 2. General-start proof and exact new dependence

[FLOW-012](../mathematics/coboundary_general_start.md) starts the original
uncentered normalized-GUE chain at any odd $A_N$ with $|p_1|+|p_2|\le K$.
Its Brownian reference starts at **exactly** $\Pi(A_N)$. For
$h=\varepsilon^4/2$, $n=\lfloor t/h\rfloor$, $1/N\le t\le1/12$,

$$
|\mathbb E\Phi_{N,f}(U_n^\varepsilon)
-\mathbb E\Phi_{N,f}(D_t[\Pi A_N])|
\le C_{f,K}[\sqrt t+N^{-1}+N^4\varepsilon+N^9\varepsilon^2
+tN^9\varepsilon+tN^{10}\varepsilon^2].
$$

The killed moment recurrence has the inherited stationary scale
$\rho=\varepsilon/N+\varepsilon^4$ and a decaying initial term.
Its summed contribution is $C\varepsilon^2|x_0|+Ct\rho$.
The frozen stopped sixth moment gives $|x_0|^6+
C(t+1)(\varepsilon^4/N^6+\varepsilon^{22})$, with no inverse-step
initial exit loss. Centered initial $p_2=O_K(1)$ retains a $C_K/N^2$
exit budget. The inherited whole-chart derivative and positive-test
bounds yield the new $N^9\varepsilon^2$ transient cost.

At $t=N^{-2/3}$, $\varepsilon=N^{-26/3}$, exactly $2N^{34}$ steps give
$O_{f,K}(N^{-1/3})$ comparison. FM-013 supplies K=20 for the unchanged
map eventually, with an ineffective threshold. The actual-start reference
law at that faster time is still not identified as Sine$_2$.

## 3. Prescribed-time obstruction and the actual regularity input

[FLOW-013](../mathematics/dyson_relaxation_obstruction.md) combines Brownian
scalar decay, doubly stochastic eigenbasis overlaps and permutation
matching. Narrow cluster neighborhoods occupy a vanishing fraction of
origins; the HS displacement bounds outliers. Balanced remainders retain
bounded fixed unnormalized traces in every odd dimension. One algebraic-
exponent perturbation destroys every power-trace zero using the existing
EXT-POPESCU-2023. Unit finite intensity and the empty weak local limit
coexist because counts are not uniformly integrable. FLOW-012 transfers
the empty limit to the chain when $Nt_N\to\infty$ and $\varepsilon=N^{-10}$.

[FM-017](../mathematics/frozen_mesoscopic_regularity.md) uses FM-007's
existing bound $|p_j|\le CN^{39/40}$ up to $J_N=\lfloor c\log N\rfloor$.
The absolutely convergent Herglotz series controls the initial transform
beyond $g_N=4\log J_N/J_N$. Exact centering costs $O(1/(Ng_N^2))$.
Each fixed angular derivative converges at $J_N^{-1/2}$.
At $t_N=\sqrt{g_N}$ it proves local stationary points near
$\theta\pm it_N/2$, with controlled nonzero Hessians. Its real potential
and positive radial derivative give the central barrier and uniform
unweighted vertical tails. Repeated initial levels cause no difficulty.
This first phase step left amplitudes and joint contours unresolved;
the next section records their closure separately.

## 4. Closed resummed kernel and sharpened actual-chain law

[FLOW-014](../mathematics/circular_dyson_actual_start.md) states nonnegative
moment parameters and explicit strip/potential errors $E_N,v_N$.
Its sufficient conditions are $g_N\le t_N/8$, $E_N\to0$,
$v_N/t_N\to0$ and $Nt_N\to\infty$.
The load-bearing external input is the prior finite arbitrary-start
kernel of Kieburg--Li--Zhang--Forrester, Proposition 21; no asymptotic
universality theorem is imported.

Exact sine interpolation and two Gaussian heat operators give the
prefactor $N/t$. On a period rectangle, the crossing pole has residue
$-Q$, so the nodal sum receives a full positive crossing term.
The two odd-N sine signs cancel under period shifts; every winding is
retained. Resummation eliminates the separate initial-node denominators.

The function bound begins at $t/8$, so each radius-$t/16$ Cauchy disk
beyond $t/4$ lies in the controlled strip. This fixes the unjustified
edge-derivative estimate that a narrower strip would leave.
Global horizontal convexity, vertical concavity and the central FM-017
barrier control the complete phase. Contour intersections leave an
ordinary two-dimensional $1/r$ singularity. Splitting a radius-$w$ disk,
$w=\sqrt{t/N}$, bounds its Gaussian-weighted integral by $Cw$, even when
saddle and pole coincide. Period-cell summation gives the complete
remainder $C_R\sqrt{N/t}$, independently of initial gaps.

The explicit crossing integral gives the sine kernel after division by
$N$ and unfolding by $N/(2\pi)$; other windings are exponentially small.
Hadamard and column telescoping control the entire Fredholm series.
Finite-N continuity passes the gap-independent Laplace bound to repeated
initial levels. The reference Brownian error is
$C_f[E_N+(Nt_N)^{-1/2}]$. Full and traceless processes are equated only
for the exactly rotation-invariant, uniform-origin observable.

The general estimates sharpen the actual time to $t_N=8g_N$.
Then $E_N=O(d_N/g_N+J_N^{-4}/g_N+1/(Ng_N^2))$ and
$E_N+(Nt_N)^{-1/2}=o(\sqrt{g_N})$. Balancing FLOW-012 gives

$$
\varepsilon_N=N^{-9}/\sqrt{t_N},\qquad
n_N=\lfloor2t_N^3N^{36}\rfloor,
$$

$$
\mathbb E\Phi_{N,f}(U_{n_N}^{\varepsilon_N})
=\mathcal L_{\mathrm{Sine}_2}(f)+O_f(\sqrt{g_N}),
\qquad 0\le f\in C_c^\infty.
$$

The six comparison errors become $\sqrt t,N^{-1},N^{-5}/\sqrt t,
N^{-9}/t,\sqrt t,N^{-8}$, all $O(\sqrt t)$ for $t\ge1/N$.
The original uncentered chain still starts at the unchanged frozen $U_N$.
The startup threshold remains ineffective; no practical-complexity or
priority claim follows.

## 5. Independent internal checking and its trust boundary

One independent internal reviewer read the raw new derivations and
maintained inputs, without reading this narrative or editing files.
Five successive checks covered FLOW-012/013, FM-017 M1--M6, M7--M8,
M9--M11, and FLOW-014 U1--U24 with its sharpened substitution.
All new implications were found proved as stated. This is an internal
audit, not an external referee report, priority assessment or fresh
certification of every inherited proof.

| Obligation | Checked boundary |
|---|---|
| General initial recurrence and exits | Summed transient, frozen stopping, initial $p_2$ and $N^{-2}$ budget. |
| Weak comparison | Whole-chart derivatives, rounding, positive-test norm and reference from exactly $\Pi(A_N)$. |
| Falsifier | Brownian normalization, multiplicities, wrapping, balanced remainders, transcendence and quantifier order. |
| Logarithmic corollary | Conjugated trace series, centering stability, derivative tails and growing-$j$ obstruction. |
| Local phase and unweighted tails | Cotangent sign, reflection, Cauchy disk, potential series, monotonicity, barrier and Gaussian complement. |
| Resummed kernel | Full residue, all windings, integrable crossings, wider-strip derivatives and uniform Gaussian-pole bound. |
| Microscopic passage | Sine scaling and diagonal, all-k determinant majorant, confluence, averaged traceless equivalence and parameter balance. |

FLOW-012 was audited at
`d7bde14dd102eccf5fbbbbbb45781de28c693f664833f0fa2a6a343830d14542`.
Only final scope prose was then updated to cite the separately checked
FM-017/FLOW-014; G1--G9 and the theorem are unchanged. Final hash:
`a1827a51b718032cfa79b9664ef02dfe546c499974a89d8e69728c088e8eebfc`.
FLOW-013's reviewed and final hash is
`27adc1e5d4aa663b1952777abab903c25f5e6e5f8254c9f24d386cb15a52b337`.
FM-017 M1--M11 was audited at
`3c673a99d438f9ea6dbb17576ae42b2cace42478cb871d56f492d4cf8409aaae`.
Only route-scope prose subsequently linked FLOW-014; M1--M11 are unchanged.
Final hash: `d9d1135d6a40d1209aee452ae97fd05bd66660a9e3bdf6eb47084d6e118b5c74`.
FLOW-014 was audited at
`7165938d3a5c71d490612c7e4157ae5b8c517ffcceea3fb7b5ccb76d62f0255a`.
After changing only its introductory assessment, the reviewer independently
confirmed the unchanged mathematical body and final hash
`148d2daf09c8d77f4580a0f6d17b304ed76dcdcb3f7475c7cf81442568d959f3`.
The execution manifests independently pin the promoted input bytes.

## 6. Finite evidence and reproducibility

The [general contract](../evidence/20261004/general_start_contract.json),
[run manifest](../evidence/executions/20261004/general-start/manifest.json)
and [checks](../evidence/executions/20261004/general-start/checks.json)
pin five inputs. The final bounded run completed with exit zero and
unchanged inputs in 1.069 seconds. Both packets use 55 seconds wall cap,
50 seconds CPU, 2 GiB memory, one core/thread and 1 MiB captured-log cap.

- Exact Fraction controls check comparison exponents, Brownian basis
  normalization and floor-time rounding.
- 332 cluster trace cases at 120 digits cover every remainder for six
  cluster counts; the largest tested first-two sum is 2.247, below 20.
  Sampled nonzero traces do not certify infinitely many powers.
- 20 complex128 perturbations check independent Hungarian matching,
  angular concentration and exact wrapped-origin unions; 15 geometry
  bounds are below one. They are not Brownian endpoint samples.
- Direct rational transforms check Poisson/Mobius bounds; 90 direct clock
  potential cases check barrier constants. 24 clock/warped kernel cases
  check the bilinear Gram matrix, trace and aliases. The largest Gram
  discrepancy is $2.00\times10^{-15}$ against $2\times10^{-12}$.

The [circular contract](../evidence/20261004/circular_dyson_contract.json),
[run manifest](../evidence/executions/20261004/circular-dyson/manifest.json)
and [checks](../evidence/executions/20261004/circular-dyson/checks.json)
pin two inputs. This bounded run completed with exit zero and unchanged
inputs in 0.518 seconds. It checks 144 rectangle/residue cases on both
sides of the contours, 32 shifted backward-heat cases, sine interpolation,
wrapped Gaussian versus Fourier heat, and exact balanced exponents.
The largest residue discrepancy is $2.90\times10^{-14}$ against
$5\times10^{-11}$. Neither packet proves asymptotic saddle bounds,
confluence, Fredholm convergence, all dimensions or deterministic BGS.
Those mathematical implications are justified by the separate proofs.

A first contract-list mismatch was caught before execution. An earlier
focused regression passed its executables but failed source immutability
because metadata was edited concurrently; it is not promoted as a
successful run. Final focused checks run after source editing finishes.
Superseded unpublished packets are retained only as ignored checkpoints;
no published historical evidence is overwritten. Both final manifests
passed validation.

Direct replay with the pinned requirements installed:

```bash
python3 computations/verification/coboundary_general_start.py \
  --output build/general-start-replay.json
python3 computations/verification/circular_dyson_relaxation.py \
  --output build/circular-dyson-replay.json
```

The standard `verify_workspace.py` accepts either check through `--only`
and supplies its output argument. The [integration packet](../evidence/20261004/general_start_integration.json)
records five successful focused checks with immutable inputs, repository
gates, the complete 248-page build and visual inspection of pages 237--238.
CI and finite checks do
not strengthen the mathematical claim or imply an analytic Lean certificate.

## 7. End state and next executable attack

The maintained proofs, claim IDs, dependency closure, exact-source mapping,
topic navigation and generated chapter form one result set. Stable paths
and historical evidence are preserved. Direct main work is authorized;
synchronization does not force history.

The stochastic contour/Fredholm obligation is closed at the stated time.
The first remaining deterministic implication is microscopic noise removal
for the actual family. The clock theorem already refutes deriving it from
low traces and global uniformity alone. Spectral rounding under weak
Egorov axioms is also a prior ledger obstruction, not an additional new
result. No small-matrix-perturbation continuity argument is promoted to
microscopic comparison. Actual-map information or the direct signed
Heisenberg hierarchy is still needed.

Faster actual-start relaxation and unbounded-correlation transfer for the
original chain remain separate open problems. **BGS-BGS-001 and
BGS-TRACE-005 remain OPEN. No complete BGS proof, external referee
certification, first-in-literature claim or prize-level result is asserted.**
