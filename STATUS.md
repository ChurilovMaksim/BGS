# Canonical research status

Status date: **2026-09-03**. This file is the authoritative present-tense claim index for the repository. Historical theorem labels, `PASS` fields in old JSON, compiled-paper titles, run ledgers, and manuscript words such as `PROVEN` do not override it.

## Best non-error line

| Layer | Current status | Canonical evidence |
|---|---|---|
| Twisted-Jacobi computational representation / R82 baseline | **REPRODUCED** | `code/verification/baseline_r82.py`, `results/verified/baseline_r82.json` |
| Exact H3 `k=2` reduction | **REPRODUCED / exact finite identity check** | `code/verification/h3_k2_exact_reduction.py`, `results/verified/h3_k2_exact_reduction.json`, `formal/Bgs/K2Reduction.lean` |
| Twisted-Jacobi matrix-element regression at new split primes | **REPRODUCED** | `code/verification/theorem_ii_new_primes.py`, `results/verified/theorem_ii_new_primes.json` |
| M1 weighted key/projector/singular decomposition | **REPRODUCED / exact finite structure; dual Python+C++** | `code/research/m1/`, `results/research/m1/cross_twist_suite.json`, `research/M1_CROSS_TWIST_001.md` |
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

## M1 cycle 001 — exact assembly repaired, asymptotics still open

A new executable workstream reconstructs the historical coupled-energy object from the weighted finite-field key table before applying any inequality. The Python implementation and an independent C++17 implementation agree on the finite anchors `N=53,199,461`, including exact integer counts/energies and floating character-projector diagnostics. The first two anchors reproduce the historical `+1.1%` and `+6.4%` corrections, showing that the reconstructed object is the historical one rather than a replacement statistic.

The key map has a singular fiber that the historical prose obscured. For `x!=y` the map to `(u,v,d)` is regular; all `N-2` pairs `x=y` collapse to `(1,1,0)` with multiplicity `N-2`. With `c=N-2`, the weighted table has the exact decomposition

`W = c delta_(0,0,0) + R`

and the count satisfies

`B = c^2 delta_0 + 2 c R_(0,0) + sum_q R_q * R_{-q}`.

This is verified with zero integer error throughout the current 14-case sweep. The regular `(H,H)` mass is exactly `(K-1)(K-2)`, linking the M1 singular correction to the existing exact `k=2` object.

The quotient-character projector itself is reproduced, but its energy expansion has nonzero cross-twist terms. At `N=53` the cross contribution is about `0.972%` of full energy; at `N=199` about `6.005%`. The off-diagonal Gram data at these anchors are dense. Therefore the historical replacement of the squared norm of a twist sum by the sum of individual twist energies is not an exact orthogonality identity.

For every quotient twist, the singular fiber gives `A_tau(0)=N-2`. Consequently the historical claim that nontrivial fibers obey `4 sqrt(N)` on **all** fibers is false for the correctly weighted table. The old maxima `15` at `N=53` and `29` at `N=199` are reproduced only after restricting to `d!=0`. A regular-fiber Weil estimate remains a viable target but must be stated after the singular split.

There is also an exact raw-energy obstruction: since `B(0)` contains `(N-2)^2`, `E=sum_t B(t)^2 >= (N-2)^4`. Hence a raw bound `E=O(N^3 K^4)` requires at least `K^4=Omega(N)` unless an upstream centering identity removes the deterministic singular contribution exactly.

For the fixed trace-3 map, the old phrase “fixed K, N->infinity” is not the right arithmetic regime. If `L_0=2`, `L_1=3`, `L_{n+1}=3L_n-L_{n-1}` and a split eigenvalue has order `K`, then `N | (L_K-2)`. Fixed `K` therefore allows only finitely many `N`; along an infinite split-prime sequence `K(N)->infinity`, with the elementary lower constraint `K>log(N)/log((3+sqrt(5))/2)`.

`N=53,a=10,K=13` is retained only as a historical subgroup calibration: `a=10` is not a trace-3 eigenvalue modulo 53 and must not be cited as a trace-3 split-prime design.

The regular character sum is now isolated as

`A_{r,s}(d)=sum_y chi_r((y+d)/y) chi_s((y+d-1)/(y-1))`, `d!=0`.

The associated rational function is `(y+d)^r y^{-r}(y+d-1)^s(y-1)^{-s}`. Its perfect-power exclusion must be formulated using the **order of the character** (dividing the annihilator order `m`), not the subgroup order `K`, and must treat divisor collisions at `d=±1` explicitly.

The 14-case regular-fiber sweep through `N=1009` stays below `3 sqrt(N)`, but this is explicitly falsifier evidence and not a theorem. Full details and the next proof obligations are in `research/M1_CROSS_TWIST_001.md` and `research/M1.md`.

## Why M1 remains open

The archived Möbius-fiber proof attempt still does not establish the advertised asymptotic conclusion. The load-bearing issues are now more precisely classified:

1. the historical proof used `O(1/K^2)=o(1)` while describing an impossible fixed-`K`, `N->infinity` trace-3 regime;
2. its own `K=17` numerical row gives `|delta|=6.9%`, above the displayed `16/K^2=5.5%` envelope;
3. cross-twist terms are not zero and can be quantitatively material;
4. the `d=0` singular fiber has multiplicity `N-2` and must be removed or handled exactly before any square-root fiber estimate;
5. the raw energy has the lower bound `(N-2)^4`, forcing either exact centering or a sufficiently strong growth regime for `K`;
6. Fourier/Parseval normalisations must be fixed once through the projector and assembled energy;
7. the perfect-power hypothesis must be proved using character order/divisor valuations, with exceptional `d=±1` cases;
8. no assembled regular cross-twist cancellation theorem has yet been proved.

Any downstream argument that imports the historical M1 theorem is conditional until it supplies an independent replacement estimate.

## Superseded trace-fluctuation route

`docs/trace_fluctuation_lemma.md` is not a valid reduction as written. Its Step 1 uses

`(C_q + C_q^*)^k = sum_j binom(k,j) C_q^j (C_q^*)^(k-j)`

without proving that `C_q` and `C_q^*` commute. The scalar binomial formula is false in general for noncommuting matrices. Step 2 additionally asserts an independence/factorisation of adjacent-pair factors that is not proved. Consequently the additive Cycle-2 toy and the finite-N Cycle-3 measurements may remain useful experiments but cannot promote this lemma.

## Rank-2 / Sp4 boundary

The restored rank-2 corpus contains useful exact finite-design identities, especially at `N=53`: the diagonal identity, coset-sector identity, coset flatness, hyperbolic period-4 structure, and a negative result for a naive product kernel. These are retained as finite-N exact research results. They do **not** prove a uniform rank-2 theorem, a higher-genus Weil estimate, M4d, or general BGS. Numerical `G0`, edge-mass, and trace-fluctuation measurements remain experimental.

## Formal boundary

`formal/Bgs/` is retained as source. `K2Reduction.lean` and the other finite certificates are distinct from `OpLocal.lean`: `OpLocal.lean` deliberately contains `sorry` obligations and an opaque spectral bound, so it is a specification of an open analytic target rather than a proof.

`formal/Bgs/M1CrossEnergy.lean` has now been added as the formal track for cycle 001. It records small trace-3 arithmetic certificates and the general formalisation targets, but is explicitly **UNVERIFIED** because the current runtime does not contain Lean/Lake. It must not be cited as machine-checked until a real `lake build` succeeds.

## Explicit quarantine

- `results/historical-numerical/bgs_spacing_N95419.json`: the historical driver computes consecutive-gap **ratios** but compares the reported KS statistic with the ordinary Wigner spacing CDF. The statistic/reference pair is mismatched.
- `data/proof/word_trace_proof.json` and the associated word-trace engine: useful partial algebra, but the rewriter remains unresolved for higher words; not a proof certificate.
- `paper/final/mobius_fiber_theorem.*` and historical `M4D_PROOF.*`: failed M1 proof route, retained for exact identities and provenance.
- `data/proof/cycle2_toy_subweyl.json` and `cycle3_trace_fluctuation.json`: exploratory finite computations only; they do not cure the algebraic defect in the R86 lemma.

For the full file-by-file audit, duplicate map, producer-path migration map, and execution matrix, see `docs/audit/full_repository_sync_2026-09-03.md` and `docs/audit/FILE_INVENTORY_SUMMARY.json`.
