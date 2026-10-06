# Round-five code-repair execution evidence

This package records finite code-contract checks, not a mathematical proof audit
or a proof of BGS. The integrated snapshot passed 164/164 workspace checks with
unchanged source bytes; the integrated maintenance suites passed 33/33 normally
and 33/33 under an optimized parent. Their seven assertion-policy tests include
the reviewed scanner regression. The archive is a local 1,332-file byte snapshot;
its upstream commit is null. The integration base f285ba510732edd9ee3679b12316df9b12e0dfcb
is context, not authenticated provenance for that archive.

## Receipts and boundaries

- `workspace.json` retains commands, source hashes, check outcomes, toolchain,
  and executed binary/log hashes. Its duplicate source manifest is factored into
  `archive-manifest.json`. C++ executables were prebuilt; this run alone does not
  establish fresh source-to-binary correspondence. Lean and TeX are separate.
- `raw-public-hashes.json` maps original receipt hashes to public receipt hashes.
  Machine-local paths use role placeholders. This is disclosed curation, not a
  claim that transformed receipt bytes equal raw bytes.
- `guard-normal-ast-equivalence.json` independently checks all 167 guarded modules
  against the integration base: stripping only the added module-level guard
  leaves identical normal Python ASTs. There are 166 assertion-bearing modules
  and one static import dependent. Optimized entry intentionally changes.
- The earlier 161/161 and 163/163 runs remain historical and retain their original
  source hashes. Inclusion in a manifest alone is not direct algorithm validation.

## Assertion entry: distinguish the snapshots

The original 51451 -> 51452 frozen-identity mutation fails normally but produced
false-PASS certificates in four optimized modes before repair (`reproduction.json`).
This is a confirmed entry-contract defect, not evidence that the correct theorem
or constant is false. The 835 injected false-predicate controls are synthetic,
not 167 separate discoveries of invalid mathematical identities.

`assertion/result.json` describes the isolated repair and distinguishes its
pre-review full aggregate (163/163) and six-test -OO policy suite from the later
scanner review. The retained -OO log is explicitly pre-review. Post-review
isolated maintenance logs pass 27/27, with seven policy tests; the scanner fixes
cover repository-relative exclusions, package initializers and dotted imports.
The final merged 33-test logs are newer and include the six subgroup groups.
Every policy-suite run exercises 1,336 optimized script/runpy entries and 835
synthetic false predicates. A separately hashed raw import experiment checked
668 actual importlib rejections on the pre-review guarded sources, which did not
change during scanner review. This does not exhaust arbitrary dynamic imports.

## Subgroup domains and integer contracts

The p=5 zero-containing and noncanonical arrays are reproduced in
`subgroup/baseline.txt`. The repaired six-group suite passes normal, -O and -OO;
it compares both implementations with independent ordered-quadruple enumeration
for 13 small-prime subgroups and six representative variants (156 comparisons).
Zero, duplicate residues, missing identity, nonclosure, shape/type and invalid
prime domains are rejected. Accepted NumPy integer scalars are normalized to
Python integers. No global counting-overflow or large-allocation guarantee is made.

## Spectral overflow and tied windows

`spectral_edge/before.json` records the original large-q residue-equivalence
failure and tied-window result 0.1875 instead of 0.25. The regression passes
normal, -O and -OO; all three independent restored-bug mutation controls fail.
The strict shared integer helper accepts NumPy integers but rejects booleans and
coercible nonintegers. The discrete-log table validator checks shape/type/range,
not logarithm identities; callers must supply a genuine table.

The bounded impact audit covers 168 exact spectrum inputs, with zero exact raw
or unfolded ties and zero q-product overflows (largest product 5,748,960).
Both active v2 tables reproduce with exactly zero maximum numeric difference:
`evidence/numerical/goe_spacing_monotone_v2.json` and
`evidence/numerical/matched_window_count_variance_monotone_v2.json`.
Their existing numeric bytes need no replacement for these defects. This does
not audit every historical table. The isolated spectral receipt's finite_field
hash precedes integration with subgroup changes; current integrated source
hashes are in the archive manifest and its execution is in the merged receipt.

## Historical coverage reconciliation

`record/audits/20261006/coverage.json` preserves all old reviewed/validated hashes
and the original acceptance record, while current hashes and match flags are
explicitly reconciled. Its 162-file baseline is still 159 scoped proof readings
plus three indexes. Later FM-021, FM-022 and TRACE-014 research promoted at f285ba5
has its own review records; changed results/open-questions indexes and manuscript
integration do not retroactively expand the older proof reading.

These reporting-only files were written after the immutable run. Their current
bytes are not claimed to have been present in that tested snapshot.

## Separate supplement gate after workspace execution

The 164-check workspace snapshot preceded reconciliation of the supplement
inventory for 31 guard-only source edits. Previous hashes and sizes remain as
historical editions. The updated 115-file inventory passes the separate
audit-only gate (`supplement-audit.json`) and the full selected 28/28 isolated
finite replay gate (`supplement-replay.json`). Every replay source hash and raw
log hash was checked. The compact receipt retains log fingerprints without
duplicating full replay logs. Wolfram scripts, echo Monte Carlo exploration and
the redesigned-symbol monodromy experiment were not rerun. This separate gate
is not included in the 164 workspace total and proves no asymptotic claim.

Post-workspace source-manifest differences at curation were the audit coverage
report and supplement inventory/README only; no executable or mathematical
source changed. Later reporting additions are not covered by the earlier
unchanged-source snapshot.
