# Integration and verification — 23 September 2026

This continuation was developed against `main` at
`c56c9db3f985872206501e1545678da940dad89c` (root tree
`2f113f87a0b6680f7943357526634fc700ccef0d`). The checkout was
reconstructed from the remote tree and every one of its 718 Git blobs was
checked against its Git object hash before editing. The two new claims are
separate partial results; `BGS-BGS-001` remains **OPEN**.

| Claim and source | Scope and proof review |
|---|---|
| `BGS-RES-005`, `mathematics/frozen_full_lag_resonance.md` (SHA256 `80d416507287d1acf826b1b6f8fe4199635f67842352e22be3ed75f9a6cb592f`) | All positive lag/translation combinations for the *actual physical symbol under the linear cat map*. The internal separate-agent reconstruction in `record/frozen_full_lag_review_20260923.md` independently checked the orientation, Fourier signs, one-visit geometry and constants. No external referee or priority claim. |
| `BGS-FM-005`, `mathematics/frozen_kick_rank_boundary.md` (SHA256 `fcbc96473a964bd5272dab7676a2da5dcffd4f3afe1e8df5768b8e2356770e17`) | The actual frozen generator has `gcd(N,7)` irreducible Jacobi chains. Exact kick rank follows using the classical Hermite–Lindemann theorem for algebraic parameters. The already known single-chain case is credited to `supplement/fixed_map/weighted-secular/attempt.md`. The approximate-rank result is explicitly restricted to pre-wrapping dimensions. `record/frozen_rank_review_20260923.md` is a root self-review, not an independent referee assessment. |

The external input is pinned as `EXT-EV-2015` in
`literature/external_dependencies.json`: Evertse, *Transcendence results*,
Theorem 4.8, author-hosted PDF. This input only rules out **exact**
collisions of distinct algebraic exponents; it provides no quantitative
eigenphase spacing. The rank proof does not produce mixed traces or local
random-matrix statistics. The Riesz gap does not cover nonlinear classical
transport. Neither claim closes `BGS-TRACE-005` or `BGS-RES-003`.

## Executed verification

| Command | Result and interpretation |
|---|---|
| `python3 computations/verification/frozen_full_lag_gap.py --output build/frozen_full_lag_gap.json` | Passed with rational/integer arithmetic: 32 independently expanded symbol frequencies, 1,024 ordered pairs, 12 sampled lags per pair, exact second moment `51451/1000`. The finite sample is **not** a proof of the all-lag inequality; that is the analytic source above. Copied output: `evidence/20260923/frozen_full_lag_gap.json` (SHA256 `ef536f1d2e5bb0cbf4b887292156b6e6c57e7cb63b836eb5da9cd85665c9730f`). |
| `python3 computations/verification/frozen_kick_rank.py --output build/frozen_kick_rank.json` | Passed 12 odd dimensions, 7 finite variance checks, and 28 best-rank lower-bound comparisons; largest assembly difference `7.21e-15`. Floating diagnostics do not prove algebraic noncollision or a large-dimension result. Copied output: `evidence/20260923/frozen_kick_rank.json` (SHA256 `e6f6adba58ec665546cee18f3f684162c52f6f74cb122169af882b15abc56d35`). |
| `python3 computations/verification/scientific_registry_audit.py` | Passed: 27 registered claims and 7 external dependencies. |
| `python3 computations/verification/repository_audit.py` | All repository structural, link and source-surface checks passed. |
| `python3 computations/maintenance/render_claim_registry.py --check` and `python3 computations/maintenance/sync_fixed_map_section.py --check` | Both generated publication surfaces matched their authoritative sources. |
| `python3 computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper` | Three pdfLaTeX passes passed the source-hash and layout/reference warning gate; 233 pages, ignored PDF SHA256 `0ddb727c7556ce9514de6151b34f01b469353f32e8ff4e053e72ebce24693995`. Typesetting does not validate the mathematics. |

The two evidence files were compared byte-for-byte with their regenerated
outputs. The fixed-map source, manuscript section, results index, claim
ledger, dependency graph, paper outlines and topic maps were synchronized.
No Lean formalization, Wolfram execution, external referee acceptance or
general BGS solution is asserted by this integration.
