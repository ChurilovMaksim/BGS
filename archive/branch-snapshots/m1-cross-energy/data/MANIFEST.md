# Data / result corpus manifest

`data/` is the broad restored research corpus.  It is intentionally much larger than the status-controlled `results/` tree.

**Important:** `data/proof/` is a historical directory name.  Presence there does **not** mean a statement is currently proved.  Current claim status is governed by root `STATUS.md`; current audited outputs live in `results/verified/`.

## Directory roles

| Directory | Role | Trust level |
|---|---|---|
| `diagnostics/` | scans, logs, falsifiers, calibrations, intermediate outputs | research corpus |
| `legacy/` | preserved theorem/run inputs and old artifact layout | reference / provenance |
| `moments/` | higher-moment calculations, design sweeps, surface terms | research corpus |
| `proof/` | historical proof-oriented numerical outputs | mixed; inspect per-file status |
| `rank2_sp4/` | rank-2/Sp4 exact finite-design results and numerical probes | finite-N research / experimental |
| `spectral/` | spectral-law, toy-model, convergence outputs | numerical research corpus |
| `LEGACY_MANIFEST.md` | original pre-rebuild manifest with old paths/status | historical only |

The bundled Tectonic binaries are intentionally absent: they are tools, not scientific results, and the pre-rebuild raw workspace remains recoverable through history/archive.

## Canonical audited outputs

Prefer these over similarly named historical files:

- `results/verified/baseline_r82.json`;
- `results/verified/h3_k2_exact_reduction.json`;
- `results/verified/theorem_ii_new_primes.json`.

Current numerical evidence is under `results/numerical/`; quarantine/superseded measurements are under `results/historical-numerical/`.

## Historical proof-oriented outputs: interpretation

- `baseline_check.json` — same reproduced R82 baseline line; canonical copy is under `results/verified/`.
- `h3_k2_exact_reduction.json` — finite exact check; canonical rerun is under `results/verified/`.
- `cycle1_hecke_basis.json` — useful historical new-prime computational regression, including very large designs; not the current bounded certificate.
- `h3_k4_factorization.json` — finite factorisation identity plus numerical fluctuation evidence; does not by itself prove an asymptotic k=4 law.
- `h3_even_k_template.json` — exact only at the explicitly tested `k=6,N=23` point; the general template remains unproved.
- `sigma4_second_moment.json` — exact at the stated `N=53` design; scaling remains open.
- `sigma4_two_point_scaling.json`, `std4_fluctuation_decay.json`, `m1_killer_test.json`, `m2_killer_test.json` — numerical scaling evidence only.
- `cycle2_toy_subweyl.json` — additive toy experiment.  Its historical `PASS` is about the toy; it does not prove multiplicative H3 and cannot repair the R86 noncommutative-algebra defect.
- `cycle3_trace_fluctuation.json` — finite-N threshold experiment; exploratory evidence only.
- `word_trace_proof.json` — partial algebra/trace identities with an explicitly unresolved rewrite engine; not a proof certificate.
- `bgs_spacing_N95419.json` — historical output of the quarantined ratio-vs-spacing test.
- `number_variance_goe_control.json`, spacing outputs, and spectral-convergence files — numerical evidence only.

## Rank-2 / Sp4 interpretation

Several files record exact finite-design identities, especially at `N=53`: `rank2_diagonal_identity.json`, `rank2_coset_flatness.json`, `rank2_coset_sector.json`, `rank2_hyperbolic_period4.json`, and the negative result `product_kernel_negative.json`.  Preserve and use these as calibration lemmas for those finite designs.  They do not establish a uniform higher-genus Weil estimate, M4d, or general BGS.  `g0_*`, `edge_mass.json`, and trace/fluctuation measurements are experimental numerical evidence.

See `data/proof/README.md` and `data/rank2_sp4/README.md` for compact directory-level boundaries.

## Producer paths and provenance

Historical JSON deliberately retains producer names such as `src/r82k_bgs_large_m.py` and inline ledger descriptions.  Do not rewrite those records merely to make paths look current.  Resolve recoverable names through `docs/audit/PRODUCER_PATH_MAP.md`; then rerun a cleaned producer into `results/` if the result is promoted.

## Preservation rule

Do not delete a data file merely because a later interpretation changed.  Preserve the raw output, record why it is superseded, and keep current truth/status in `STATUS.md` and the manifests.  Never silently overwrite a historical measurement with a new run.

## Known incomplete diagnostic logs

Some diagnostic logs contain useful measurements followed by a producer/runtime failure.  Preserve the measurements, but do not treat the run as a completed certificate:

- `diagnostics/inert_torus.log` ends with `NameError: c2 is not defined` after several earlier checks;
- `diagnostics/k4_surface_family.log` ends with `NameError: json is not defined` after printing the surface-family statistics;
- `diagnostics/twisted_moment.log` ends with `NameError: json is not defined`; its printed values also visibly contradict the displayed `pred 4` target for the twisted quantity, so it is a falsifying/incomplete diagnostic rather than supporting evidence.
