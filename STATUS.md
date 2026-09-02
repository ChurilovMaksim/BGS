# Canonical research status

Status date: **2026-09-03**.  This file is the authoritative present-tense claim index for the repository.  Historical theorem labels, `PASS` fields in old JSON, compiled-paper titles, run ledgers, and manuscript words such as `PROVEN` do not override it.

## Best non-error line

| Layer | Current status | Canonical evidence |
|---|---|---|
| Twisted-Jacobi computational representation / R82 baseline | **REPRODUCED** | `code/verification/baseline_r82.py`, `results/verified/baseline_r82.json` |
| Exact H3 `k=2` reduction | **REPRODUCED / exact finite identity check** | `code/verification/h3_k2_exact_reduction.py`, `results/verified/h3_k2_exact_reduction.json`, `formal/Bgs/K2Reduction.lean` |
| Twisted-Jacobi matrix-element regression at new split primes | **REPRODUCED** | `code/verification/theorem_ii_new_primes.py`, `results/verified/theorem_ii_new_primes.json` |
| GOE nearest-neighbour spacing at audited split-prime designs | **NUMERICAL EVIDENCE** | `code/experiments/goe_spacing.py`, `results/numerical/bgs_spacing_goe.json` |
| Matched GOE number variance at `N=19489,K=29` | **NUMERICAL EVIDENCE / freshly rerun** | `code/experiments/number_variance_goe_control.py`, `results/numerical/number_variance_goe_control.json` |
| Historical M1 / Möbius-fiber asymptotic claim | **OPEN GAP** | `research/M1.md` |
| R86/R87 trace-fluctuation lemma route | **INVALID AS STATED / SUPERSEDED** | `docs/trace_fluctuation_lemma.md` plus this audit |
| Rank-2 / Sp4 corpus | **FINITE-N EXACT IDENTITIES + EXPERIMENTAL CONTINUATION** | `data/rank2_sp4/README.md`, `code/sp4/` |
| General BGS | **NOT PROVED** | downstream analytic steps remain open |

## Audited computational anchors

The R82 baseline was rerun during the 2026-09-03 full sync.  The stored fourth-moment curve is reproduced with maximum absolute deviation `6.039613253960852e-14` at `N=199,K=11` and `2.353672812205332e-13` at `N=3571,K=17`.

The exact `k=2` check was rerun and gives `|P|=132=12*11` at `N=53,K=13` with identity deviation about `1.25e-12`, and `|P|=90=10*9` at `N=199,K=11` with identity deviation about `3.64e-10`.

The new-prime regression was rerun using a genuinely independent direct scalar character-sum path.  At `N=461,K=23` it checks all 100 matrix entries for each of five `q` values and has maximum relative deviation `1.4166352564530244e-11`.  At `N=19489,K=29` it checks a deterministic 32-entry sample for each `q` and has maximum relative deviation `1.2714969482034705e-10`.  Both are below the explicit `5e-10` regression tolerance.

The matched number-variance experiment was rerun at `N=19489,K=29`: every `L in {1,2,3,5,8,12}` remains within `|z|<2` of the matched finite-dimensional GOE control.  This is numerical evidence, not an analytic local-law theorem.

The spacing experiment was freshly reproduced for the bounded `N=3571,K=17` design (`KS D=0.0139959 < 0.0210549`, `chi2/dof=1.297`).  The existing `N=19489,K=29` row remains a retained prior numerical result; a complete fresh rerun was not finished inside the bounded audit execution window.  The file records this provenance explicitly.

## M1 is open

The archived Möbius-fiber proof attempt does not establish the advertised asymptotic conclusion.  The load-bearing problems are:

1. it identifies an `O(1/K^2)` bound with `o(1)` while simultaneously describing fixed `K` and `N -> infinity`;
2. its own `K=17` numerical row gives `|delta|=6.9%`, above the displayed `16/K^2=5.5%` envelope;
3. the squared norm of a sum over twist pairs is effectively replaced by a sum of individual squared norms without a proved orthogonality/cancellation theorem for cross-twist terms;
4. Fourier/Parseval normalisations are not kept consistent through the bound;
5. the perfect-power exclusion for nontrivial character products needs a separate divisor/character proof.

Any downstream argument that imports the historical M1 theorem is therefore conditional until it supplies an independent replacement estimate.  The repair target is stated in `research/M1.md` and root `THEORY.md`.

## Superseded trace-fluctuation route

`docs/trace_fluctuation_lemma.md` is not a valid reduction as written.  Its Step 1 uses

`(C_q + C_q^*)^k = sum_j binom(k,j) C_q^j (C_q^*)^(k-j)`

without proving that `C_q` and `C_q^*` commute.  The scalar binomial formula is false in general for noncommuting matrices.  Step 2 additionally asserts an independence/factorisation of adjacent-pair factors that is not proved.  Consequently the additive Cycle-2 toy and the finite-N Cycle-3 measurements may remain useful experiments but cannot promote this lemma.

## Rank-2 / Sp4 boundary

The restored rank-2 corpus contains useful exact finite-design identities, especially at `N=53`: the diagonal identity, coset-sector identity, coset flatness, hyperbolic period-4 structure, and a negative result for a naive product kernel.  These are retained as finite-N exact research results.  They do **not** prove a uniform rank-2 theorem, a higher-genus Weil estimate, M4d, or general BGS.  Numerical `G0`, edge-mass, and trace-fluctuation measurements remain experimental.

## Formal boundary

`formal/Bgs/` is retained as source.  `K2Reduction.lean` and the other finite certificates are distinct from `OpLocal.lean`: `OpLocal.lean` deliberately contains `sorry` obligations and an opaque spectral bound, so it is a specification of an open analytic target rather than a proof.  The 2026-09-03 audit environment did not contain Lean/Lake, so no new full Lean build is claimed in this status file.

## Explicit quarantine

- `results/historical-numerical/bgs_spacing_N95419.json`: the historical driver computes consecutive-gap **ratios** but compares the reported KS statistic with the ordinary Wigner spacing CDF.  The statistic/reference pair is mismatched.
- `data/proof/word_trace_proof.json` and the associated word-trace engine: useful partial algebra, but the rewriter remains unresolved for higher words; not a proof certificate.
- `paper/final/mobius_fiber_theorem.*` and historical `M4D_PROOF.*`: failed M1 proof route, retained for exact identities and provenance.
- `data/proof/cycle2_toy_subweyl.json` and `cycle3_trace_fluctuation.json`: exploratory finite computations only; they do not cure the algebraic defect in the R86 lemma.

For the full file-by-file audit, duplicate map, producer-path migration map, and execution matrix, see `docs/audit/full_repository_sync_2026-09-03.md` and `docs/audit/FILE_INVENTORY_SUMMARY.json`.
