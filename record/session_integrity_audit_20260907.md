# Repeated cross-layer integrity audit — 2026-09-07

This audit was performed after the first late-session synchronization because the user explicitly requested a second pass for omissions across **all** layers rather than a commit-presence check. The starting synchronized head was `322de8a06af85bb251675e2d6de8c93abbfe5207`. Immediately before writing this record the audited head was `78ad209426dc9579de01bde5840ce542161dfa55`, which is ahead of the starting head by 14 commits and behind by zero.

## 1. Real omissions/defects found and repaired

### Extremal-resonance proof prose

`mathematics/extremal_resonance_nondegeneracy.md` still contained an invalid orbit-escape paragraph: it attempted to propagate both eigencoordinate rectangle bounds through the same time direction. The theorem statement, manuscript temporal theorem and exact witness checkers were not affected. Commit

`08a4a5d33d631b81abd6083c55187f1840c87660`

rewrote the load-bearing step correctly. From `L(k)>t+2` and the support rectangle one separately obtains

```text
xi(k) > (1+lambda^-1)X
```

for forward escape and

```text
sigma eta(k) > (lambda^-1+lambda^-2)Y
```

for backward escape. Therefore all nonzero positive and negative iterates leave `V+AV`.

### Global Corvaja--Zannier Cayley result

A stronger result derived and checked during the session had remained local rather than entering `main`. It has been restored as

- `mathematics/cayley_curve_uniform.md`;
- `computations/verification/cayley_curve_uniform.py`;
- `evidence/certificates/cayley_curve_uniform_20260907.json`.

For every odd prime `p` and every subgroup order `K>=2`, the project specialization of Corvaja--Zannier yields

```text
N(rho,sigma)
 <= max(3*cuberoot(32) K^(2/3), 48 K^2/p),
E_+(c(H\{1})) << K^(8/3)+K^4/p.
```

The exponent is not improved, but parity and subgroup-size restrictions of the older project curve route are removed. External priority for this specialization is not claimed.

The exact verifier was rerun with `p<=257`, all subgroup orders `3<=K<=256`: **PASS**, 338 designs = 114 odd-order + 224 even-order, maximum `K=256`. Local source SHA-256 is

`d9799af9d770d769b3d1e716ea465e1fdac995093d6435df14d4d80be3b3bf1c`.

Its Git blob is `286ca2cbeb6f37bfff7f36aff5e52b8181f9f3fc`, exactly equal to `git hash-object` of the rerun local source. The full rerun JSON SHA-256 is

`a04e44a71202fbbd93590ef418bb4fd2210c918ce81f2f485706c582cf2aa124`.

### Status/index drift

The base `claim_ledger.md`, `results.md`, `open_questions.md`, formalization README and evidence provenance had not all been advanced to the late September 7 state. This could make proved results appear absent or make a closed route appear open even though the source files were present.

Repairs:

- added authoritative `record/claim_ledger_addendum_20260907.md`;
- added `mathematics/results_20260907_addendum.md`;
- rewrote `mathematics/open_questions.md` so the corrected off/off elliptic theorem is no longer listed as unfinished;
- updated root/mathematics/record/evidence README authority pointers;
- updated `formalization/README.md` from a stale six-module table to the complete 15-module active import surface;
- updated `evidence/provenance.md` to enumerate all 20 currently committed certificate files;
- aligned `record/bosonic_information_claims_20260907.md` with the authoritative dated ledger.

## 2. Suspected problems checked and cleared

### Extremal C++ workspace orchestration

At first inspection `verify_workspace.py` appeared to run `extremal_resonance_replay` twice, once without a packet. Source inspection showed this is intentional:

1. the no-argument C++ invocation performs an independent self-test;
2. after the Python producer completes, a second invocation replays its exact packet.

Thus this was **not** a verifier bug. The CMake target is present.

### Nested manuscript source segments

Several continuation TeX files looked orphaned from the top-level master. They are in fact reached through nested inputs in `manuscript/final_delivery_note.tex`, and the manuscript builder resolves inputs recursively. No continuation section was lost by this mechanism.

### Lean import graph

`formalization/Bgs.lean` imports exactly all 15 `.lean` files under `formalization/Bgs/`. The draft `formalization/drafts/TemporalCancellation.lean` is intentionally outside the active import graph. The previous README table was incomplete documentation, not a missing import.

## 3. Late-session science retained in `main`

The earlier byte/readback audit remains valid for the late rare-phase, fixed-noisy-Gaussian and pure-loss sources/certificates. In particular the project retains:

- exact rare-phase balance/radial-transition results and the certified interval `2.9086102383180<C_*<2.9086102383183`;
- the explicit `n=128` known-pair copy-complexity separation;
- fixed strictly noisy phase-insensitive Gaussian input-tomography minimax risk `Theta((log B)^(-beta/2))` and deterministic inverse modulus;
- the 50% pure-loss `3e39<B_75<=4e39` finite certificate;
- the uniform pure-loss binary theorem with `t=Bu eta^n` and asymptotic penalty `eta^{-n}`;
- independent Python/C++ verification surfaces and dated review files.

The unrestricted finite-Fourier temporal theorem is present in both the mathematical layer and `manuscript/unified_sections/temporal_resonance.tex`. The older radius-eight certificate remains an independent finite control, not the general theorem's hypothesis.

## 4. Evidence inventory

`evidence/provenance.md` now accounts for every current file in `evidence/certificates/`, including aperture, Cayley, Floquet, fourth moment, holomorphic/Husimi, locality, magnetic, Pell, pure-loss, rare-phase, temporal and twisted-Jacobi surfaces.

There is intentionally no committed `extremal_resonance.json`: the maintained producer writes exact witness/replay artifacts to the verification log directory and the workspace runner performs the independent C++ packet replay. This is not data loss.

## 5. PDF/publication audit

The retained locally verified PDF is

`/mnt/data/WoW_unified_final.pdf`

with SHA-256

`55f759c1d4205d76b6499cbf52e52d2caf0273eac18aa0eaa990cbab94c73edd`,

146 A4 pages, unencrypted, file size 1,230,586 bytes. It was re-preflighted during this audit. The earlier PDF-skill render/visual inspection covered representative beginning/late/final pages and found no layout defect. Text extraction confirms the rare-phase and pure-loss continuations are present.

The word `Corvaja` is absent from this PDF, so the PDF predates restoration of the global Cayley theorem. This is now recorded as a **publication freshness boundary**, not hidden as a synchronization success. The new theorem is authoritative in the mathematical/evidence/status layers until a fresh full manuscript build incorporates it.

The local recovery source directories were also inspected. Their top-level masters are older snapshots (3–4.5 KB versus the current remote master of roughly 40.9 KB and different Git blobs), so they were not used to overwrite or reconstruct the canonical remote article. Doing so would risk reverting late corrections.

## 6. CI and compiler boundary

The contemporary GitHub Scientific verification run for head `78ad209426dc9579de01bde5840ce542161dfa55` created `computation`, `manuscript` and `formalization` jobs, but all have no executed steps (`steps=null`/empty in the connector result). The audit therefore treats the workflow conclusion as an infrastructure non-run, not a scientific failure or pass.

The available local container does not expose `lean` or `lake`. No fresh Lean compilation is claimed by this repeat audit. Static import-graph completeness was checked separately.

## 7. Current scientific frontier

The repeated audit did **not** uncover a hidden proof of microscopic BGS universality. Positive generic microscopic BGS/GOE/COE remains **OPEN**. The principal positive bridge still requires

```text
Heisenberg-scale desymmetrized joint traces
 -> band-limited microscopic RMT correlations
 -> uniform high-frequency tail
 -> full local law.
```

The sharp pointwise Cayley frontier remains the centered `K^(2+o(1))` energy scale; the restored global curve theorem remains at exponent `8/3`. Infinite-support analytic resonance nondegeneracy and the full vanishing-noise tomography minimax transition are additional logically separate open questions.

## 8. Audit verdict

The second pass did find genuine omissions, so a blanket earlier statement that absolutely nothing was missing would have been too strong. Those omissions have now been repaired in `main`: one proof-text defect, one uncommitted but verified Cayley theorem/verifier/certificate, and several stale status/provenance indexes.

No other concrete loss was identified in the audited Git history, late-session code/certificates, CMake verifier surface, active Lean import graph, manuscript input reachability, retained PDF scope, or status hierarchy. Remaining limitations are explicitly classified as open mathematics, unavailable execution infrastructure, or publication freshness rather than silently counted as completed work.