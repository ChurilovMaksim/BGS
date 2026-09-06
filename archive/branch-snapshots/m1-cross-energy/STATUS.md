# Canonical research status

Status date: **2026-09-03**. This file is the authoritative present-tense claim index for the repository. Historical theorem labels, `PASS` fields in old JSON, compiled-paper titles, run ledgers, and manuscript words such as `PROVEN` do not override it.

## Best non-error line

| Layer | Current status | Canonical evidence |
|---|---|---|
| Twisted-Jacobi computational representation / R82 baseline | **REPRODUCED** | `code/verification/baseline_r82.py`, `results/verified/baseline_r82.json` |
| Exact H3 `k=2` reduction | **REPRODUCED / exact finite identity check** | `code/verification/h3_k2_exact_reduction.py`, `results/verified/h3_k2_exact_reduction.json`, `formal/Bgs/K2Reduction.lean` |
| Twisted-Jacobi matrix-element regression at new split primes | **REPRODUCED** | `code/verification/theorem_ii_new_primes.py`, `results/verified/theorem_ii_new_primes.json` |
| M1 weighted key/projector/singular decomposition | **REPRODUCED / exact finite structure; dual Python+C++** | `research/M1_CROSS_TWIST_001.md`, `code/research/m1/`, `results/research/m1/cross_twist_suite.json` |
| M1 regular single-twist character bound | **ANALYTIC LEMMA: `<=3 sqrt(N)` for `d!=0`** | `research/M1_WEIL_002.md`, Lidl--Niederreiter Thm. 5.41; dual classifier regression |
| M1 assembled asymptotic energy bound | **OPEN GAP** | `research/M1.md` |
| GOE nearest-neighbour spacing at audited split-prime designs | **NUMERICAL EVIDENCE** | `code/experiments/goe_spacing.py`, `results/numerical/bgs_spacing_goe.json` |
| Matched GOE number variance at `N=19489,K=29` | **NUMERICAL EVIDENCE / freshly rerun** | `code/experiments/number_variance_goe_control.py`, `results/numerical/number_variance_goe_control.json` |
| R86/R87 trace-fluctuation lemma route | **INVALID AS STATED / SUPERSEDED** | `docs/trace_fluctuation_lemma.md` plus this audit |
| Rank-2 / Sp4 corpus | **FINITE-N EXACT IDENTITIES + EXPERIMENTAL CONTINUATION** | `data/rank2_sp4/README.md`, `code/sp4/` |
| General BGS | **NOT PROVED** | downstream analytic steps remain open |

## Audited computational anchors

The R82 baseline was rerun during the 2026-09-03 full sync. The stored fourth-moment curve is reproduced with maximum absolute deviation `6.039613253960852e-14` at `N=199,K=11` and `2.353672812205332e-13` at `N=3571,K=17`.

The exact `k=2` check was rerun and gives `|P|=132=12*11` at `N=53,K=13` with identity deviation about `1.25e-12`, and `|P|=90=10*9` at `N=199,K=11` with identity deviation about `3.64e-10`.

The new-prime regression was rerun using a genuinely independent direct scalar character-sum path. At `N=461,K=23` it checks all 100 matrix entries for each of five `q` values and has maximum relative deviation `1.4166352564530244e-11`. At `N=19489,K=29` it checks a deterministic 32-entry sample for each `q` and has maximum relative deviation `1.2714969482034705e-10`. Both are below the explicit `5e-10` regression tolerance.

The matched number-variance experiment was rerun at `N=19489,K=29`: every `L in {1,2,3,5,8,12}` remains within `|z|<2` of the matched finite-dimensional GOE control. This is numerical evidence, not an analytic local-law theorem.

The spacing experiment was freshly reproduced for the bounded `N=3571,K=17` design (`KS D=0.0139959 < 0.0210549`, `chi2/dof=1.297`). The existing `N=19489,K=29` row remains a retained prior numerical result; a complete fresh rerun was not finished inside the bounded audit execution window. The file records this provenance explicitly.

## M1 cycle 001 — exact assembly repaired

The active workstream reconstructs the historical coupled-energy object from the weighted finite-field key table before applying any inequality. Python and an independent C++17 implementation agree on `N=53,199,461`, including exact integer counts/energies and floating character-projector diagnostics. The first two anchors reproduce the historical `+1.1%` and `+6.4%` corrections, showing that the reconstructed object is the historical one rather than a replacement statistic.

For `x!=y` the key map is regular; all `N-2` pairs `x=y` collapse to `(1,1,0)` with multiplicity `N-2`. With `c=N-2`,

`W = c delta_(0,0,0) + R`

and exactly

`B = c^2 delta_0 + 2 c R_(0,0) + sum_q R_q * R_{-q}`.

This has zero integer error throughout the current 14-case sweep. The regular `(H,H)` mass is `(K-1)(K-2)`, directly linking the singular correction to the existing exact `k=2` object.

The quotient-character projector is reproduced, but its energy expansion has nonzero cross-twist terms. At `N=53` the cross contribution is about `0.972%` of full energy; at `N=199` about `6.005%`. The off-diagonal Gram data at these small anchors are dense. Therefore the historical diagonal-only energy decomposition is not an exact orthogonality identity.

For every quotient twist the singular fiber gives `A_tau(0)=N-2`, so a square-root regular-fiber estimate can only be invoked after the singular split.

There is also an exact raw-energy obstruction: since `B(0)` contains `(N-2)^2`,

`E=sum_t B(t)^2 >= (N-2)^4`.

Hence a raw bound `E=O(N^3 K^4)` requires at least `K^4=Omega(N)` unless an upstream centering identity removes the deterministic singular contribution exactly.

For the fixed trace-3 map, “fixed K, N->infinity” is not a valid infinite regime. If `L_0=2`, `L_1=3`, `L_{n+1}=3L_n-L_{n-1}` and a split eigenvalue has order `K`, then `N | (L_K-2)`. Fixed `K` therefore allows only finitely many `N`; along an infinite split-prime sequence `K(N)->infinity`, with the elementary lower constraint `K>log(N)/log((3+sqrt(5))/2)`.

`N=53,a=10,K=13` is retained only as a historical subgroup calibration: `a=10` is not a trace-3 eigenvalue modulo 53.

## M1 cycle 002 — regular single-twist bound

The old individual-fiber issue is now repaired cleanly. For `d!=0`, choose a primitive annihilator character `omega` of exact order `m=(N-1)/K`. Let

`Q_d(Y)=Y(Y-1)(Y+d)(Y+d-1)`

and define the monic polynomial

`P_{r,s,d}(Y)=Q_d(Y)^m (Y+d)^r Y^{(-r mod m)} (Y+d-1)^s (Y-1)^{(-s mod m)}`.

The factor `Q_d^m` is an exact domain mask: on admissible points its character is one and at every excluded point the extended character value is zero. Thus the restricted rational sum is exactly a complete polynomial character sum.

For generic `d`, the root-multiplicity residues modulo `m` are `r,-r,s,-s`; for `d=1` they are `r,s-r,-s`; for `d=-1` they are `-r,r-s,s`. Simultaneous divisibility by `m` forces `r=s=0`. Therefore every nontrivial regular twist satisfies the non-`m`-th-power hypothesis.

Lidl--Niederreiter, *Finite Fields*, Theorem 5.41 then yields

`|A_{r,s}(d)| <= 3 sqrt(N)` for every nontrivial twist and every `d!=0`,

with the sharper `2 sqrt(N)` at `d=±1`.

This is an analytic lemma, not merely the previous numerical envelope. Independent Python/C++ classifiers at `m=4,18,20,210` are retained as regression checks of the residue bookkeeping. They are not the logical basis of the proof.

## Why M1 remains open

The historical Möbius-fiber theorem still does not establish the advertised asymptotic conclusion. After cycles 001–002, the unresolved load-bearing issues are narrower:

1. cross-twist terms are nonzero and can be quantitatively material; no assembled covariance/cancellation theorem is proved;
2. the `d=0` singular fiber has multiplicity `N-2`, so the spectral reduction must either center it away exactly or retain a regime strong enough for the raw lower bound;
3. Fourier/Parseval normalization must be fixed once through the exact projector and final assembled energy;
4. the final error must be summed with the true number and geometry of twist pairs, not by replacing `||sum F_tau||^2` with `sum ||F_tau||^2`;
5. the resulting normalized remainder must be shown to vanish in the actual arithmetic regime `K=K(N)`.

The previously open perfect-power / individual regular-fiber checkpoint is now closed by cycle 002. The primary analytic target is the **assembled regular cross-twist energy**, together with the centering decision.

Any downstream argument that imports the historical M1 theorem remains conditional until those steps are proved.

## Superseded trace-fluctuation route

`docs/trace_fluctuation_lemma.md` is not a valid reduction as written. Its Step 1 uses

`(C_q + C_q^*)^k = sum_j binom(k,j) C_q^j (C_q^*)^(k-j)`

without proving that `C_q` and `C_q^*` commute. The scalar binomial formula is false in general for noncommuting matrices. Step 2 additionally asserts an independence/factorisation of adjacent-pair factors that is not proved. Consequently the additive Cycle-2 toy and finite-N Cycle-3 measurements remain experiments only.

## Rank-2 / Sp4 boundary

The restored rank-2 corpus contains useful exact finite-design identities, especially at `N=53`: the diagonal identity, coset-sector identity, coset flatness, hyperbolic period-4 structure, and a negative result for a naive product kernel. These are finite-N exact research results, not a uniform rank-2 theorem, higher-genus Weil estimate, M4d proof, or general BGS theorem.

## Formal boundary

`formal/Bgs/` is retained as source. `K2Reduction.lean` and the other finite certificates are distinct from `OpLocal.lean`: `OpLocal.lean` deliberately contains `sorry` obligations and an opaque spectral bound, so it is a specification of an open analytic target rather than a proof.

`formal/Bgs/M1CrossEnergy.lean` tracks cycles 001–002. It contains trace-3 arithmetic certificates and finite residue-classifier targets, but is explicitly **UNVERIFIED** because the current runtime does not contain Lean/Lake. It must not be cited as machine-checked until a real `lake build` succeeds.

## Explicit quarantine

- `results/historical-numerical/bgs_spacing_N95419.json`: the historical driver computes consecutive-gap **ratios** but compares the reported KS statistic with the ordinary Wigner spacing CDF. The statistic/reference pair is mismatched.
- `data/proof/word_trace_proof.json` and the associated word-trace engine: useful partial algebra, but the rewriter remains unresolved for higher words; not a proof certificate.
- `paper/final/mobius_fiber_theorem.*` and historical `M4D_PROOF.*`: failed M1 proof route, retained for exact identities and provenance.
- `data/proof/cycle2_toy_subweyl.json` and `cycle3_trace_fluctuation.json`: exploratory finite computations only; they do not cure the algebraic defect in the R86 lemma.

For the full file-by-file audit, duplicate map, producer-path migration map, and execution matrix, see `docs/audit/full_repository_sync_2026-09-03.md` and `docs/audit/FILE_INVENTORY_SUMMARY.json`. The active execution programme is `docs/roadmap.md`.
