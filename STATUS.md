# Canonical research status

Status date: **2026-09-02**.

This file overrides historical theorem labels, old compiled papers and archived run notes when they disagree with it.

## Best non-error line

| Layer | Current status | Evidence |
|---|---|---|
| Twisted-Jacobi computational representation / R82 baseline | **REPRODUCED** | `code/verification/baseline_r82.py`, `results/verified/baseline_r82.json` |
| Exact H3 `k=2` reduction | **REPRODUCED / exact identity check** | `code/verification/h3_k2_exact_reduction.py`, `results/verified/h3_k2_exact_reduction.json`, Lean source `formal/Bgs/K2Reduction.lean` |
| Twisted-Jacobi matrix-element regression at new split primes | **REPRODUCED** | `code/verification/theorem_ii_new_primes.py`, `results/verified/theorem_ii_new_primes.json` |
| GOE spacing / matched number variance | **NUMERICAL EVIDENCE** | `code/experiments/`, `results/numerical/` |
| Historical M1 / Möbius-fiber asymptotic claim | **OPEN GAP** | `research/M1.md` |
| Rank-2 / Sp4 continuation | **EXPERIMENTAL / archived working material** | `archive/legacy-workspace/` |
| General BGS | **NOT PROVED** | downstream of unresolved analytic steps |

## Audited computational anchors

The R82 baseline reproduces the stored fourth-moment curve with maximum absolute deviation `6.039613253960852e-14` at `N=199,K=11` and `2.353672812205332e-13` at `N=3571,K=17`.

The exact `k=2` check gives `|P|=132=12*11` at `N=53,K=13` with identity deviation about `1.25e-12`, and `|P|=90=10*9` at `N=199,K=11` with identity deviation about `3.64e-10`.

The new-prime matrix-element regression compares the production matrix contraction with direct scalar character sums at five q values. At `N=461,K=23` it checks all 100 entries per q and has maximum relative deviation `1.4166352564530244e-11`. At `N=19489,K=29` it checks a deterministic 32-entry sample per q and has maximum relative deviation `1.2714969482034705e-10`. Both are below the explicit `5e-10` regression tolerance.

These checks are finite-N computational certificates. They do not prove the limiting spectral law and are independent of the failed M1 promotion.

## M1 is open

The archived proof attempt does not establish the advertised conclusion. The load-bearing issues are:

1. it identifies an `O(1/K^2)` bound with `o(1)` while also describing a regime with fixed `K` and `N -> infinity`;
2. its own `K=17` numerical row gives `|delta|=6.9%`, above the displayed `16/K^2=5.5%` envelope;
3. the squared norm of a sum over twist pairs was effectively replaced by a sum of individual squared norms without a proved orthogonality/cancellation statement for cross-twist terms;
4. Fourier/Parseval normalisations are not kept consistent through the archived bound;
5. the perfect-power exclusion for nontrivial character products needs a separate divisor/character argument.

Therefore any downstream result that uses M1 as an analytic theorem is not active as a theorem in this rebuild.

## Quarantined material

The old word-trace proof engine is preserved only in `archive/legacy-workspace/`. In the audit it reached the rewrite engine but failed with an unresolved `('V','V')` word; it is not a certificate.

The historical `N=95419` GOE driver is also quarantined: it formed consecutive-gap ratio statistics and then compared them with the ordinary spacing CDF, so its reported KS statistic does not test the named GOE spacing distribution. The original remains in the legacy workspace and a short quarantine record is in `results/historical-numerical/`.

The old `mobius_fiber_theorem` paper is historical provenance, not an active proof.
