# MANIFEST — Package A-data (phase 1): ten evidence data trees → archive/evidence/

Ten `evidence/<tree>` directories that live verifiers read as data at path
constants are archived to `archive/evidence/<tree>` with same-commit consumer
migration. No file content is changed by the move itself; the only archival
copies that differ from their originals are five live configuration files
whose values are themselves repo-relative paths into the trees (listed with
both hashes below).

## Composition

| tree | files | bytes |
|---|---:|---:|
| intermediate_old_layers_20261007 | 68 | 1,569,454 |
| charge_strengthening_20261007 | 154 | 1,398,408 |
| fractional_hamming_20261007 | 100 | 1,274,064 |
| residual125_20261007 | 33 | 1,261,078 |
| spectral_extension_20261006 | 27 | 698,482 |
| central_residual_20261007 | 70 | 613,024 |
| half_radius_20261007 | 38 | 586,966 |
| cat_jet_20261006 | 44 | 542,438 |
| odd_newest_20261007 | 41 | 388,114 |
| homoclinic_20261006 | 4 | 106,325 |
| **total** | **579** | **8,438,353** |

## Reconciliation method

Per-file comparison of every original (pre-package tree) against its archival
copy: **574 of 579 byte-identical**. The five exceptions are the live
configuration files below — their archived copies carry the same path
migration as every other consumer, because other archived/live code resolves
the paths inside them at run time; all content they pin by SHA-256 is
unchanged, so every pinned hash remains valid. Tree-level confirmation uses
a SHA-256 digest over the sorted sequence of (relative path, NUL, bytes, NUL)
per tree: the five trees without a configuration file match exactly; the five
with one differ by exactly that file.

| tree | original digest | archive digest |
|---|---|---|
| intermediate_old_layers_20261007 | b926b65270f8ad30809f2c369eccf86ac61b66ceb804012a1d4210e96c025743 | cbc9c06f99b185a2721b0838632215692619cba23409d42dbdedcd2425653bb8 (input_map.json edited) |
| charge_strengthening_20261007 | ba6c28986b68fc95cc365707839ff8c64053a18450b8204de0c569d06bc05e52 | identical |
| fractional_hamming_20261007 | f753e177eb14c91ba940dbf2d1c3cb6a68300ae23e4fc2b5f86f35b792008655 | identical |
| residual125_20261007 | 4d90d8c067a7a3ddaf66c21b4967701db0d161a8d61b43899f98352bf6c963df | identical |
| spectral_extension_20261006 | 3b8cbbb6372dfa4ba4cbb29c139a770bf9ddfeecc5d9e6b9d836a711e12a6ef6 | 9def91e733d959ab4b2363dc401d9a9aaa5950c89f01be4694912f34d93e715c (input_hashes.json edited) |
| central_residual_20261007 | f966ccdf998821e9bbc85cd2564f40b2e5df03f96792ec5f7c03c5a9180395f2 | identical |
| half_radius_20261007 | 28c6addcb212b224241f7ac6e26952c3d503081a80f79c9a1d96e75df12c06b1 | identical |
| cat_jet_20261006 | 4a5c3a41c4fd9187e53361ab74ad435f630492524460ae01de931b39be6daa84 | c420a57c4434d2f2393deaee0a390bdc6701e97bc359cc7fa8cd2e0ae9ac9c9d (input_map.json edited) |
| odd_newest_20261007 | 700c6d3011ce81b5ac54f24b60337e1b484cf9489156737e3f28bbb4e38de22d | 4805bf0991a299186703e69a39c28e82c14e5aee1394248530fa8dbb99e4bf01 (original_index.json edited) |
| homoclinic_20261006 | 6f54860f0bd317061bb9e647b685d2f5bc5d8c520db8720253322dc57dafab93 | 8fa778bff3f3580c6fbf4fb40babc94b5ba438a76e597833b6f5d399ad8594d1 (source_binding.json edited, rider) |

### The five edited configuration copies

Values changed are repo-relative paths only (`evidence/<tree>/…` →
`archive/evidence/<tree>/…`), except the homoclinic rider noted separately.
Blob = git blob SHA-1; both hashes are given for the original file and for
the archival copy.

| file | values migrated | original blob / sha256 | archived blob / sha256 |
|---|---|---|---|
| cat_jet_20261006/input_map.json | 42 | 07b1f3e2e9049b9bfab073df9a5097f2296959f3 / 0e47a22a81c966634f37d451415aa9e3ad7a490dac29d289b242792a058eeaff | 7b7d0dcc713ce81c96b0f91ff03a4f6ee60e8e6b / a2c656a548b42b4b7ddd8fab6ba8692247f56128c936757cb9e9f8cf7706da2b |
| intermediate_old_layers_20261007/input_map.json | 158 (72 blob paths, 85 `original_paths` blob fields, `inherited_cat_blob_root`) | 520a56637d9cd46c22103ade2a68d61b520308b3 / 44d894b64e254db56b9102a39b5fc24458127d4b318b7749b9f5cbefb22115a5 | ef3ae779bce307c7b60c6c3b0a6e4c87c2b4c009 / 30018195f861abbb67513788c5ef8976e9c40b9ceea886da4c2e46f0cebd0617 |
| spectral_extension_20261006/input_hashes.json | 11 keys | e1b75641cc5adab6af676b67584f656a775043b4 / d1ae2297851848dedb5e5e0fe7378fc429540e092d99835d3805d2eab7997dca | 5a1a43ec8bce8c47ac29e8cf0fdaca3878cf4175 / ee35be9e28135e16604d4f91b30afaae26e7cac1c46abfd0117be30313009cbf |
| odd_newest_20261007/original_index.json | 32 envelopes | 68765c15dcab9a46b2c7602620efa311ea854a2a / a2be8ad1270d2304b01b57e35810aee6879dc67718993c9e4f0dd7beb9b41f3a | 55772f6cf3abdf6ad93c28784d9a5503c0f751f3 / ef6c8c19cd6e064f11639425a2f50f7812a7662cc5059f5e0907fb462a45bef2 |
| homoclinic_20261006/source_binding.json | 6 (rider below) | a3964f02ed78ca043e31c5efc18bb3032ca1655d / af38b38242c1129a2990276e440f61304c229e6f9fcddf31c2bcaf9feff2b3ef | b9335a6baf4b279e8cb49ba1d65d1f05af14f64b / af0fa2fc95d0cecc6086efd13f4376028b00348427361cfb7e280ab65a142692 |

### Rider: homoclinic source binding (package-D leftover)

`exact_homoclinic.py` failed on the pre-package tree with
`FileNotFoundError: record/history/2026/homoclinic_20261006/proof_original.md`:
package D archived `record/history/` to `archive/history/`, but the six
`record/history/2026/…` `public_path` values inside
`evidence/homoclinic_20261006/source_binding.json` were never migrated, so the
verifier could not resolve them. This package migrates those six values to
`archive/history/2026/…` in the archival copy; all six targets exist there and
hash-verify against the binding, as do four of the five unchanged
`mathematics/` targets.

One further pre-existing defect is recorded, not absorbed: the binding's
pinned hash for `mathematics/periodic_point_trace_comparison.md` no longer
matches that maintained file's current bytes, so on the post-package tree the
verifier progresses through every other binding and fails only at that stale
pin (`source hash: BGS/mathematics/periodic_point_trace_comparison.md`). The
pin is deliberately NOT rotated here — rotating it would silently re-pin a
scientific input to unreviewed current bytes. It is a phase-7 disposition
item; the A-data migration for this consumer (the binding-path constant in
`exact_homoclinic.py` and the six path values above) is complete.

### Rider addendum (2026-10-25 redfix, phase-7 red-checker package)

The phase-7 disposition item recorded above is now closed. The binding's
five `mathematics/` `public_path` values were stale after the phase-2
relocations (the verifier died with `FileNotFoundError` on the first of
them); they are refreshed to the relocated files, and the two drifted
pins are rotated to reviewed current bytes. The six `archive/history/`
entries are untouched, as are all other hashes.

| `public_path` before | `public_path` now | `sha256` before → now |
|---|---|---|
| `mathematics/four_branch_parametrix.md` | `mathematics/fixed-map/four_branch_parametrix.md` | `c696ebd…` unchanged (byte-identical relocation) |
| `mathematics/fixed_map_path_model.md` | `mathematics/fixed-map/fixed_map_path_model.md` | `d5365063…` unchanged (byte-identical relocation) |
| `mathematics/pell_smooth_resonance.md` | `mathematics/pell/pell_smooth_resonance.md` | `1e560706…` unchanged (byte-identical relocation) |
| `mathematics/periodic_point_trace_comparison.md` | `mathematics/returns/periodic_point_trace_comparison.md` | `8d42ade3…` → `b465af1e…` (rotated: phase-2 link-translated move per `MANIFEST-P2MATH4.md`, then stable since the phase-2 close in every snapshot; current note reviewed coherent, Theorems 1/2/4/5) |
| `mathematics/extremal_resonance_nondegeneracy.md` | `mathematics/resonance-cohomology/extremal_resonance_nondegeneracy.md` | `76b66aeb…` → `fd65a519…` (rotated: move-documented change per `MANIFEST-P2MATH2.md` code-span update and `MANIFEST-P2MATH7.md` post-move hash, which equals the current bytes) |

The check keeps its full strength: every binding hash must still match
exactly, and any future change to any bound file fails it again.

## Same-commit migrations

- Consumer path constants: `charge_strengthening_replay.py` (RAW tree),
  `fractional_hamming_replay.py` and `fractional_hamming/full_replay.py`
  (RAW tree), `intermediate_old_layers_certificates.py` (input-map tree),
  `central_residual_extension.py`, `residual125_certificates.py` +
  `residual125/residue.py`, `half_radius_obstructions.py` (results file),
  `odd_newest/run_checks.py` + `odd_newest/check_finite_matrices.py`,
  `cat_jet_certificates.py` (input-map path), `exact_homoclinic.py`
  (binding path), `spectral_extensions.py` (tree prefix — a plain data read;
  the spectral integration scripts do not consume this tree).
- Test consumers: `test_charge_strengthening_portability.py` (the cloned
  corruption target path), `test_fractional_provenance.py` (RAW tree), and
  `test_intermediate_replay_freshness.py` (the fixture `EVIDENCE` path —
  fixture-coupled to the verifier's constant; found by the post-tree test
  delta, not by the coupling analysis).
- Maps outside the trees: charge replay sources 102 values, fractional
  adapter mapping 4, central promotion map 24, residual125 promotion map 5,
  half_radius promotion map 7.
- Pin rotations (package-E pattern; only where a pin covers a file this
  package itself edits): the charge sources map's pins in
  `charge_strengthening_replay.py` and in
  `test_charge_strengthening_portability.py`; the residual125 map's pin in
  `residual125/residue.py`. Central and half_radius maps needed none (their
  pins re-verify unchanged); the fractional adapter's three port pins were
  verified against the migrated adapter map.
- Registry: 7 `evidence[]` values on 5 sealed claims (BGS-FM-010, BGS-FM-025,
  BGS-FM-026, BGS-FM-027, BGS-TRACE-021), pure prefix migrations; epoch
  amendments: 1 new (BGS-FM-027) + 4 extended, approved set 61 → 62.
- Navigation: 4 link targets in live documents
  (`mathematics/first_old_layer_classification.md`,
  `mathematics/intermediate_return_operator.md`,
  `mathematics/residual25_affine_dictionary.md`,
  `record/intermediate_old_layers_promotion.md`).

## Deliberately not edited

Links into these trees inside wave2-hash-pinned inputs
(`mathematics/fractional_hamming_cancellation.md`,
`mathematics/global_switch_transfer.md`, `mathematics/onestep_charge_gap.md`)
and inside the held `record/charge_strengthening_promotion.md` are left
byte-identical; they resolve through this manifest. Frozen provenance maps
of the charge promotion (hash-pinned as files, never read as path maps) keep
their historical path strings, as do the archived artifacts themselves.
