# Referee audit and deterministic extensions — 8 September 2026

The full BGS objective remains open. This pass establishes two internal
improvements, corrects a signed-orbit statement, and restores reproducibility.
It does not establish global novelty or a solution for a new chaotic family.

## Reviewed input and coverage

The input is `6224ecef882ba8d198dc1981d839259834d9765c`, tree
`bb7b180a43062635635d877654039ff4e41430f6`. All 406 files were obtained at that
immutable ref, their Git-blob hashes verified, and the exact original commit
reconstructed locally. There were no AGENTS.md files. The repository protocol,
both status ledgers, current results, open questions and retractions were read.

The inventory and executable checks cover the whole main-branch snapshot.
**The mathematical line-by-line audit does not cover the whole manuscript.**
Its actual proof scope is the following table. Other proofs retain their
previous status; successful execution is not a new proof review of them.

| Claim | Dependency/obligation checked | Verdict |
|---|---|---|
| Second-bracket finite-Fourier positivity | exposed support pair, unique decomposition, determinant bound, two-sided escape, negative trace, reality | proved as written in `extremal_resonance_nondegeneracy.md`; higher-lag manuscript theorem not independently re-audited here |
| Analytic pointwise-bracket rigidity | full-measure regular set, line equivariance, recurrence, projective dynamics, analytic continuation, irrational flow | proved as written |
| Analytic orbit-sum transfer | signed A-orbits, bilateral tails, uniform decay, reality, uniqueness | Markdown valid; strengthened to full adapted exponent; TeX convention corrected |
| Factorial trace bridge | normalization, partition Mobius identity, absolute convergence, Heisenberg support | identities valid; separate-tail assertion corrected under the stated positive-average hypotheses |
| Global Cayley curve estimate | quartic discriminant, boundary geometry, independent coordinate functions, restoration and diagonal counts; exact Corvaja–Zannier specialization | valid with the named external theorem |
| Dense Cayley Fourier estimate | annihilator expansion, trivial character, conductor count, Parseval normalization | internal algebra valid; mixed Weil/Deligne input retained as external, not newly reconstructed from a source-exact proof here |

Two independent reviewers checked the analytic proofs and the positive-measure
extension respectively. The primary review also checked the resulting proofs
and regression implementations. No independent review of the full bosonic
minimax or remaining arithmetic corpus is claimed.

## Mathematical changes

### 1. Correct signed frequency action

In the TeX regularity section, replacing A by sign(tr A)A while retaining the
original composition operator was invalid. With B=[[2,1],[1,1]], A=-B, and
h=sin(2 pi x_1)-sin(2 pi (2x_1+x_2)), every B-orbit sum vanishes but the
A-orbit sums are ±i. The new exact verifier checks complete support-orbit
intersections with a proved stopping rule. A is now retained; B is used only
to choose eigen-covectors.

### 2. Lossless adapted coefficient decay

For N_A(k)=|xi(k)|+|eta(k)|, let m_A=inf_(k!=0)N_A(k)>0 and
 d=(lambda+lambda^-1)/2-1>0. On the outward orbit tail,

```text
N_A(A^(±n)k) >= (1+n d)N_A(k).
```

Consequently the analytic transfer satisfies

```text
|uhat(k)| <= M/[1-exp(-rho d m_A)] exp(-rho N_A(k)).
```

The earlier factor-two exponent loss was unnecessary. This concerns Fourier
coefficient decay, not a boundary holomorphic supremum norm. The proof is in
`mathematics/analytic_coboundary_regularization.md`; the all-members analytic
nonlinear coboundary problem remains open.

### 3. All-bandwidth comparison already implies Schwartz comparison

For fixed k and positive normalized averages of finite-circle spectra,

```text
sup_a mu_N(a+[0,1)^(k-1)) <= 2 k^k[1+mu_N([-2,2]^(k-1))].
```

A positive band-limited majorant bounds the right side. Occupation counts and
Holder's inequality give the translated-cube estimate, which makes Schwartz
Fourier-cutoff approximation uniform. Comparison for every compact Fourier
support, against a reference with a Schwartz limit, therefore needs no
independent high-frequency-tail hypothesis. A fixed Fourier cap is
insufficient, and signed averages do not meet the positivity requirement.
The proof and explicit counterexamples are in
`mathematics/bandlimited_correlation_extension.md`.

This closes an unnecessarily separate deterministic obligation in the previous
research plan. It does not prove Heisenberg-scale trace comparison. Correlation
convergence is also not silently promoted to a spacing or full process law.

## Reproducibility and corrections

All 21 C++ targets compiled. The maintained Python/C++ suite, followed by the
new analytic regression, passed 106/106 checks. Two original failures were
fixed and rerun individually: the gamma certificate unnecessarily required a
README literal; the weighted-echo verifier imported removed names and expected
four return values from a three-value design function. The latter now uses
the maintained Hermitian exponential, an explicitly normalized odd basis,
and a normalized Hilbert–Schmidt norm. Its full finite operator checks passed.

The new correlation regression passed 48 configuration/order cases, 96 exact
identities and 480 inequalities. The analytic regression passed 1,950 integer
Chebyshev cases, 65 formal Laurent identities, 780 rational inequalities,
16 transfer reconstructions and the signed-orbit counterexample.

Lean 4.33.1 compiled all 16 active modules (19 Lake jobs). The official archive
SHA-256 is `890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235`.
This container lacks `/proc/<pid>/exe` resolution used by Lean, while
`/proc/self/exe` works. The optional `lean_proc_self_compat.c` redirects only
the exact current-process lookup. It changes no theorem or Lean evaluator.
The local commands after installing the pinned distribution were:

```sh
cc -shared -fPIC -O2 computations/maintenance/lean_proc_self_compat.c \
  -ldl -o build/lean-proc-self-compat.so
# In this affected runtime only; normal installations omit LD_PRELOAD.
export LD_PRELOAD="$PWD/build/lean-proc-self-compat.so"
(cd formalization && lake build)
```

Native-decide certificates explicitly depend on native-evaluation axioms.
The new `AnalyticOrbitKernels` module uses ordinary proofs: its growth lemma
has only propext/Quot.sound dependencies, and its three concrete checks have
none. The full analytic theorems are not claimed to be Lean-formalized.

Both manuscript workflows and reproduction instructions passed unsupported
`--repo-root`/`--runs` arguments; these were removed. Official v7 action tags
and the pinned Lean release were checked, so their versions were retained.
The complete article builds in 153 pages with three pdfTeX passes, immutable
source hashes, no horizontal overflow, and no unresolved references/citations.
The contents and changed proof pages were visually inspected; this is not a
visual inspection of all 153 pages. The exact figure
`assets/figures/correlation_bandwidth.svg` is regenerated by
`computations/analysis/correlation_bandwidth_figure.py`.

Compact execution evidence is in
`evidence/certificates/research_audit_20260908.json`. Regenerable build products,
logs and downloaded toolchains remain outside tracked source. No cloud-CI
success is inferred from local execution. Wolfram context and evaluation
calls both failed with the service's HTTP 404; no Wolfram result was used.

## Continuing research tree

1. Keep a fixed natural chaotic family, quantization, symmetry block and
   positive averaging convention explicit. A change of these data is a new
   claim, not a silent relaxation.
2. Attack weighted joint traces at |m|=Theta(N), at every compact Fourier
   support. This is the missing positive BGS implication. Existing resonance
   positivity is not evidence that it holds.
3. For each candidate trace argument, first test known arithmetic/conjugacy
   obstructions and the fixed-bandwidth counterexample. If it survives,
   isolate the uniform-in-N estimate and compare exact hypotheses with sources.
4. The nonlinear analytic coboundary question and sparse centered Cayley
   energy remain parallel mathematical branches. They may yield useful
   theorems, but neither is a substitute for step 2.

The 40 listed remote branch names were inspected as an inventory only. No
branch was deleted: their unique scientific content was not compared in this
pass. Main's existing source organization is retained, with concrete stale
commands and contradictory current claims corrected.
