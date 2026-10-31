# Lines M and N integration (31 October 2026, UTC+5)

Base: `origin/main` e4042ef2 (merge of PR #64). Branch: `line-MN`. Source note: `mathematics/fixed-map/lineMN_conductor_structure.md`.

## Packets
* `computations/verification/lineM/`: author reports `REPORT_M.md` (v1) and `REPORT_M_v2.md` (fixes M-F1–M-F12 applied by the author),
  `NOTES_M.md`, `claims_extract.txt`, code, logs, `lean/LineMArith.lean`, manifest `SHA256_M.txt` (+ `.sha256`), and the referee files
  under `referee/`. All manifest entries verify. The author's `repo/` snapshot (a copy of this repository) is not copied.
* `computations/verification/lineN/`: the author's `REPORT_N.md` (unchanged, sha256 b740bc39…), **`REPORT_N_v2.md`** (written at
  integration, see below), `NOTES_N.md`, code, logs, manifest `SHA256_N.txt` (+ `.sha256`), the referee files under `referee/`, and
  `integration_checks/` (`lineMN_checks.py` and its log, `proved_deps_gate_MN.py` and its log).
* **Excluded** (third-party literature or unrelated files; listed in the manifests, hence the only `FAILED open` lines in `manifests.log`):
  * the author's `logs/cp.{pdf,txt}`, `logs/mss1701.{pdf,txt}`, `logs/osv2110.{pdf,txt}` and `logs/wss2211.{pdf,txt}` (published papers);
  * `logs/voloch.pdf`, an unrelated paper (N-F5);
  * the referee's `lit/bourgain2005.{pdf,txt}` and `lit/voloch1989.pdf` (`lit/` was empty when copied).

  Not copied either:
  * the author's later `N2/` directory (not in the manifest; it contains `.npy` files);
  * the `.venv`;
  * `__pycache__`.

## Line N errata written at integration (REPORT_N_v2.md §12)
The referee's verdict was READY-after-fixes N-F1–N-F10, and the brief asked the integrator to write the errata. `REPORT_N_v2.md` is
`REPORT_N.md` with each fix applied in place and listed in §12:
* N-F1: N3 credited as the composite-c extension of Prop S (TRACE-258).
* N-F2: N3 sourced to the per-family TRACE-198 [CA] bound; r > 2(N + k) added.
* N-F3: t_F and p₀ effective, not computed, with the estimate ≈ 40 / p ≳ 110 [H].
* N-F4: the J₃ hypothesis is q ≥ c_W p², τ ≥ 10⁴⁵, and the W⁺ hypothesis is restated.
* N-F5: voloch.pdf; Voloch is cited via OSV.
* N-F6: "ineffective" → "effective, constants not computed".
* N-F7: m₁ effective, not computed.
* N-F8: the index is 4, not 32.
* N-F9: the table matches the body.
* N-F10: N1′ supersedes K2 lines 134–137.

Integration notes in the same section:
* I-1: the Cochrane–Pinner Thm 1.1 ranges (3q^{1/3} < τ ≤ q^{1/2} and q^{1/2} < τ ≤ q^{2/3}/3), all three isotropic branches, and the
  constant 2/3^{1/4} = 1.519671… (amended after the owner audit of PR #65; iso_coverage.py).
* I-5: owner audit of PR #65, registry wording R3 (278 budget), S1–S3 (family scope, named statements, annotational 283 edge).
* I-2: isotropic sums via Bourgain Thm 1 with r = 1; BGK is context only.
* I-3: only F = (±2,8)V is used, because TRACE-198 puts the spectrum of L_E in |z| < 1, so the author's (8E) θ is dropped.
* I-4: "unconditionally" → "without assuming frozen R′" (PR #64 R2 wording).

## Repository wording fixes (N-F6, N-F10)
* `computations/verification/lineK/K2/REPORT_K2_v2.md`: lines 20 and 132 (and §5, §6) now read "effective, constants not computed". A
  pointer to Line N1′ is added at lines 134–137, and a new §9 errata table explains both changes. As with §8, `SHA256_K2.txt` records the
  author's pre-polish file.
* `mathematics/fixed-map/lineK_harg_removal.md:249` and `literature/lineK_sources_20261031.md` (lines 34–37): the same wording fix.

## Claims (record/claims.json, hand-edited by `edit_claims_MN.py`)
* New ids 269–285: 14 proved, 3 open with closure conditions (274 M4c, 276 M6, 282 composite c ≤ p^C).
* To avoid a dependency cycle (246 → 283), N3 (283) is split from Corollary N3′ (284). 283 credits Prop S (258) and M3 (271) in text
  only. 284 depends on 246, 271 and 283.
* Annotations (states unchanged):
  * 246 and 258: the [H] caveat "covers all or most m" is replaced by N3's proved statement, and 283 is added as a dependency.
  * 247: the unweighted Line L §6 target is false on c ≥ λ^{θr/2+t}, and it is restated β-weighted.
  * 238: refined by M5.
  * 206: stays open.
* Line L note §6 has a "Later work" pointer. README.md line 23 (and README.ru.md) now name the proved standing inputs, as in the PR #64
  R1 wording.
* Kurlberg–Rudnick: the publisher page gives Commun. Math. Phys. **222** (2001) 201–227, DOI 10.1007/s002200100501. The referee's 221 is
  a slip. It is used in the M7b annotation of 277 only, with no registry row.
* Rounding (integration): the M3 bases 1.13288 and 1.11239 in REPORT_M_v2 are rounded to nearest (1.1328794, 1.1123866). They are
  registered as the lower bounds 1.13287 and 1.11238. The Lean θ check uses 1.278387, which is at least (1 − δ_F/2)·1.28359 =
  1.2783866…
* REPORT_M_v2 §6 (M7b) and §8.3 still say "ineffectively" for Bourgain/BGK. That author file is in its manifest and was not edited; the
  registry and the note use "effective, constants not computed".

## External dependencies
* Four new rows: EXT-OSV-2023, EXT-OSV-2024, EXT-CP-2011, EXT-BOURGAIN-2005. The review record is
  `literature/lineMN_sources_20261031.md`.
* The epoch `external_dependency_extension` lists them, and the scope now says twenty-nine.
* Data lists only: the wave2 `allowed` set (docstring count 25 → 29) and the test expectation (39, 25) → (39, 29).
* The metadata snapshot is `registry_metadata_20261031_lineMN.json`, with the report `record/audits/metadata_cache_refresh_20261031_lineMN/`,
  the pointer, and the v4 negative-control path (a data string).

## Gate
* `proved_deps_gate_MN.py` runs strict for 244–285. No proved claim depends on a non-proved claim except 206. It also checks that the
  graph is acyclic, that every dependency id exists, and that open claims have closure conditions.
* The PR #64 gate still passes.
* The pre-existing main violations are listed, unchanged: 076, 077, 080, RES-015, RES-023, 236.
