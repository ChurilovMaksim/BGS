# MANIFEST — Package B-rest (phase 1): older execution runs → archive/evidence/executions/

The remaining dated execution runs inside `evidence/executions/` — the dates
20261004, 20261005, 20261007, 20261008, 20261012, 20261013, 20261014, 20261020,
the non-chat remainder of 20261011 (`cavity-continuation`, `clock-universality`,
`fourth-delay`, `reversal-gap`) and `20261019/repository-integration` — are
archived byte-for-byte to `archive/evidence/executions/<same path>`. No file
content is changed by the move. 546 of the 548 files move; the two `.gz`
payloads of `20261020/repository-reconciliation` are held in place (see the
dedicated section below). Same-commit migrations: `record/claims.json`
(47 path values on 28 claims, pure `archive/` prefixes, all in `evidence[]`),
`evidence/index.json` (9 `current_paths` values), epoch amendments in
`record/claim_integration_epochs.json` (5 new rows, 8 extended rows; the
`approved` set in `computations/verification/wave2_integration_audit.py` grows
62 → 67), navigation URL targets (50 occurrences in 29 live documents) and
relative links in the four evidence-root documents (12 links, incl. one
B-chat residual healed in `evidence/executions/README.md`), and
`.gitattributes` (2 whitespace-exemption patterns keyed to
`20261012/haar-feedback` log directories, repointed to the archive paths;
attribute values unchanged). Keep-set untouched: `20261006`, `20261021`,
`20261022`, `20261016` (separate micro-package), `evidence/index.json`'s
other classes and the executions root README's keep-set links.

## Composition

| tree | files | bytes | tree digest (SHA-256) |
|---|---:|---:|---|
| evidence/executions/20261004 | 12 | 109084 | 38732514a1303d0fd52234415fa163dbff90c4630bbbe067dc6f5240a8f983c7 |
| evidence/executions/20261005 | 20 | 87513 | 366bf16c52cd057b4d449ee447ee914b1703586e06cf293b9827e8d6f1f30c1a |
| evidence/executions/20261007 | 62 | 1474382 | cab75144f9a05c64f4009f6c8c9f65b1b34b6fc767148e101f5d6e7bdaf06692 |
| evidence/executions/20261008 | 12 | 71559 | 112e9b5fbbf34427aafb6f72b86d4d2673df8c8ab34ac9be55ab8a8cd69f38ae |
| evidence/executions/20261011/cavity-continuation | 36 | 891482 | 5108b9a9a85c9a28f04c69ee5119f930f411f3c61b8029196f900f1f45b8774d |
| evidence/executions/20261011/clock-universality | 22 | 136548 | 128cc3cc6737aab910360c58c5bbce2aa63f1a2b82d2070806d815edee35a7d5 |
| evidence/executions/20261011/fourth-delay | 12 | 168760 | 13da1623ab5281fc799f4d7f76ff418f9b95982c206e0f1790fd82df9c7ac15c |
| evidence/executions/20261011/reversal-gap | 15 | 266081 | 23d4b48df7f1807d9f277dba77f0af45b9aca7b9fdd6842611e382c6a881effc |
| evidence/executions/20261012 | 171 | 1732053 | bedd2aa82518725a6208f4f9888d91c4cbdf6dbacc3b349d9d46e318ecdcac41 |
| evidence/executions/20261013 | 88 | 3291707 | 962650a38717fd3ad06513578417f81876396eba2b659fa9d6e89aa2c879488d |
| evidence/executions/20261014 | 47 | 1143788 | 79b114ac58d1ce89ed87884779fb39ec74c4dc1f3b07ea5ffc9e3d52c42c5877 |
| evidence/executions/20261019/repository-integration | 18 | 878356 | 0fe12cdf3c29e9a8ab1e144986d8195a83ea61dfe33f628b95b0b283928464ca |
| evidence/executions/20261020/repository-reconciliation | 20 | 1120510 | 99e1add3039f360b9c3208f1c4fd1a82ddeee0b638377f8a6084c0e1d49907ba |
| evidence/executions/20261020/toolchain-followup | 11 | 71854 | a224327241da5306d7ec81368525fbe9f072d966b56db00998c3196fb88e47e7 |
| **total moved** | **546** | **11443677** | |
| held in place (2 .gz, see below) | 2 | 878,896 | |
| **package total** | **548** | **12,322,573** | |

Tree digest method: SHA-256 over the sorted sequence of
(path relative to the tree root, NUL, file bytes, NUL). Original and
archival digests are identical for every tree (per-file table below).
For `20261020/repository-reconciliation` the digest covers the 20 moved
files only; the two held `.gz` files are listed separately below.

## Held in place: the two `.gz` payloads of 20261020/repository-reconciliation

`push-files` carries UTF-8 text only, so the run's two gzip payloads cannot
travel through the archival channel. They stay at their original paths
under a recorded disposition:

| file | bytes | SHA-256 | content (verified by decompression) |
|---|---:|---|---|
| `evidence/executions/20261020/repository-reconciliation/execution_archive.tar.gz` | 587,260 | `3e8bc23f8a8c25d8f0806a9b2111c1c1bd0f77b61f16434b7b81c4abce70cc9c` | tar archive of 557 execution `.log` files (4,741,120 B decompressed); every member verifies (bytes + SHA-256) against the run's own `archive_members.json` (557/557) |
| `evidence/executions/20261020/repository-reconciliation/workspace.json.gz` | 291,636 | `0b1e74820fb1811afdf38de2b333015ffbd554ddc1937b0931ba51623a8a6902` | gzip of a single JSON document (1,053,192 B): the `verify_workspace.py` run report (toolchain/source fingerprints, replay results) |

Nothing outside the run's own directory references either file: zero claims
values, zero code consumers, zero navigation links, zero external hash pins
(measured over the whole tree). Inside the run, `receipt.json` pins **both**
payloads by SHA-256 — the receipt and the other 19 records move to the
archive, so the run's record set stays internally consistent through this
manifest: the payloads remain exactly where the receipt's pins resolve
historically, and this section records the split. Carrying decompressed
text instead was evaluated and NOT adopted: it would change the deposited
bytes the receipt pins (a re-formed record, not a relocation), and for the
tar it would explode one deposited artifact into 557 loose files while
losing tar-level metadata. Holding the whole 22-file subdirectory was also
considered; it was not chosen because all 20 readable records can archive
now and only the two opaque payloads need to wait for a binary-capable
channel or a later phase disposition. Note: `evidence/index.json`
`current_paths` entry for `repository-reconciliation/` is migrated to the
archive path together with the run's records; if the whole-subdirectory
hold is preferred instead, that single index value reverts together with
the 20 copies.

## Epoch claim amendments

13 sealed (wave2 snapshot) claims are affected — the full B-package sealed
set (B-chat measured zero). Amendments were generated mechanically from
the sealed-row ↔ staged-row diff with fail-closed assertions (only the
`evidence` field changes; every changed value is a pure `archive/` prefix
relocation; `historical_row_sha256` values unchanged).

New rows (5): BGS-FLOW-012, BGS-FLOW-013, BGS-FLOW-014, BGS-FLOW-015, BGS-FM-017.
Extended rows (8): BGS-FLOW-011, BGS-FLOW-016, BGS-FLOW-017, BGS-FLOW-018, BGS-FLOW-019, BGS-FLOW-020, BGS-FLOW-021, BGS-FORMAL-001.
For extended rows the disposition gains one appended sentence and the
review one appended manifest reference, per the established pattern;
`BGS-FORMAL-001`'s pre-existing `boundary` field passes through unchanged.
The `approved` set in `wave2_integration_audit.py` is extended by exactly
the 5 new IDs (62 → 67). Post-package `wave2_integration_audit.run()`:
PASS, unchanged 29 / amended 67 (base: 34 / 62).

## Navigation rider

`evidence/executions/README.md` also carried one relative link into
`20261011/chat-research/README.md`, left stale when package B-chat moved
that tree (B-chat's URL scan was token-based and this link is relative).
It is retargeted to the archive path in this package — same file, same
edit class — so the live executions index has no stale links left.

## Per-file table (546 moved files)

| original path | bytes | blob SHA-1 | SHA-256 |
|---|---:|---|---|
| evidence/executions/20261004/circular-dyson/checks.json | 44712 | ab2706fa50cbfaf858a600f8941362bc1584dd43 | c4cc8841cedbf4d409dc016bca536ab4f34c0debd8cd8586f3980f77814ce81d |
| evidence/executions/20261004/circular-dyson/manifest.json | 5154 | fabe026156464cd668f62565527700c5cfe375af | e27363fdf1e967008bc3f07116c66d77108654515e6eb22c347613d12fd0a993 |
| evidence/executions/20261004/circular-dyson/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261004/circular-dyson/stdout.txt | 83 | 7eedc20649ab223851106c1e83c0a9f1e7841a49 | a9415c766e211f2357c2ee1a3b310aef868f0084cdcd7de0cd799f23d0ed72fb |
| evidence/executions/20261004/general-start/checks.json | 29467 | 030a30859b9ab69a4e97ad96653dd7fe31d45f8f | 348f31d148d50ba494d88a5eb3d2a53fd6ed7119d98090abf472d48866689883 |
| evidence/executions/20261004/general-start/manifest.json | 6684 | 83991741f6392d146fe09053b851dbe8a0d35702 | a2fb9df0dc6ba3bc43d6d3307edd53f6506dec9a7271ab7a38a5fb1bae76c6d2 |
| evidence/executions/20261004/general-start/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261004/general-start/stdout.txt | 76 | fd8efa2f7a490ebdfbf3387ac55d5a9627d011ef | ef99f826e6950ae47841975d8aa29526dd609bca7ce49cb3b481c0755c0eed50 |
| evidence/executions/20261004/polynomial-coboundary/checks.json | 18557 | f6310367d40ad9b357dae86c0d193073393fd99e | 82caf1088e28a09060b132ee6d414c62c49d22abfe59fa6e9d263573a6290096 |
| evidence/executions/20261004/polynomial-coboundary/manifest.json | 4241 | fe55627b3f0742620b5769c57d0f29a0efabbb5d | b5086ee44ef3c638400c39062c86bf08bf54574b71e68050b33197ddf4620f74 |
| evidence/executions/20261004/polynomial-coboundary/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261004/polynomial-coboundary/stdout.txt | 110 | 999b5d9f98dfc27a8b455eefd37e6ed9ad1393fd | 1a7847fe9d9cac893415b6407094c109d8ba4c16230a8a87afbecee638aa1b53 |
| evidence/executions/20261005/all-order/checks.json | 10111 | d8cd76c6bdb8871faa4481e313a4854fbadbf168 | 9966cf6e5ff693e066994c7ada885e00e4307ea26b8568dde7e62fce6ea8628a |
| evidence/executions/20261005/all-order/manifest.json | 9823 | 933fa3f973b0733395634abdb92ddf58248fd5ea | 8335b12b32f4c8289e06625d4abbe389dfee26c12020e2308297f8d6d23affcc |
| evidence/executions/20261005/all-order/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261005/all-order/stdout.txt | 141 | 7f279c854e8d3d7219c2a37267e131fb6838f585 | 986cece9098424b87e406c62176041eebbbc15535eb8594595f61578f2b275df |
| evidence/executions/20261005/critical-noise/checks.json | 8052 | fedbc4732a08ced7b43c250f97a5cbad4e6457d7 | 63f6adc7392334775a2ed17e848badd5a89a7d0458b6ed17fbbf0a9d2a1581fa |
| evidence/executions/20261005/critical-noise/manifest.json | 11567 | b2fc45ab667d1b88b2f019ea2d4edea141bec96c | 4b29f89380648ac63f08fe884dbba3577a63d8485663962dadb27564a94a5e0d |
| evidence/executions/20261005/critical-noise/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261005/critical-noise/stdout.txt | 8052 | fedbc4732a08ced7b43c250f97a5cbad4e6457d7 | 63f6adc7392334775a2ed17e848badd5a89a7d0458b6ed17fbbf0a9d2a1581fa |
| evidence/executions/20261005/degree-growth/checks.json | 3136 | 3706175abff18fdf8a1428491b658501c8def429 | 4efcae9c8ee573442eeb33ffb3bf6270ef587d5589a6fd6a010991a1b7e4e9e1 |
| evidence/executions/20261005/degree-growth/manifest.json | 9763 | c35ec09a95e5dfed03650f58c79efeb6607c4696 | 8f1795c8b603bc9425375099724a34ffc8c17086f17b6f6fed6995de5ae7b7b5 |
| evidence/executions/20261005/degree-growth/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261005/degree-growth/stdout.txt | 3136 | 3706175abff18fdf8a1428491b658501c8def429 | 4efcae9c8ee573442eeb33ffb3bf6270ef587d5589a6fd6a010991a1b7e4e9e1 |
| evidence/executions/20261005/noise-removal/checks.json | 6218 | 16a73b6cea1b0544c60454ff7ce1a181c3eb1ce1 | f451d254f2212dcad62cd611b666dcc5f4243440c40d953d57411d720f7d64e7 |
| evidence/executions/20261005/noise-removal/manifest.json | 7426 | 7c3b219e75cd66dd86cc8e1783297626a8e69d88 | a82f2785b35583f5cbb1ea86082cfe65037ee6b25ec726e04060b2032a6a08d8 |
| evidence/executions/20261005/noise-removal/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261005/noise-removal/stdout.txt | 125 | a728443b54176f40b478490f45aeb097b1a04449 | 38d3ec4d3256c392aa034c77eff130ccf5ac21dd1810b25e47665db07e3e8682 |
| evidence/executions/20261005/pair-heat/checks.json | 1200 | cb4f539c5c7ccb2fec09213dc7d14b8ad42624bd | 5cd3d442fb9a2101dc3274b12f78de9fcd4cb6edc8be773c1feedadde99ea0a7 |
| evidence/executions/20261005/pair-heat/manifest.json | 8345 | 0c34d05ac9788665a5510b4db098375967d26ffa | 23e02e503f94ac14d3319e0e60f643390a1e35568dd2b003779caf5152a8fbfb |
| evidence/executions/20261005/pair-heat/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261005/pair-heat/stdout.txt | 418 | e2f6e2c5a5a4086dfff5dcbd35fac37abf1b192c | bd495e49f103051c0588723b61196f9d11e06f85c4c722f2371e9c9842403b57 |
| evidence/executions/20261007/factorial-intermediate-validation/README.md | 792 | dcb57781b096fb22cd5fa6d8421b91c1f595e35a | 61e868bdf6b90bc844bd6159262a47a71887c5722c0a84252bd8569eaf96f9c1 |
| evidence/executions/20261007/factorial-intermediate-validation/SHA256SUMS | 1798 | 22cfd13b543df4d677c03ee3472f04e370dffb54 | 57985657be69094e7d29c446557fe222d39eec0d6a50e3b96445cee09a4a310a |
| evidence/executions/20261007/factorial-intermediate-validation/archive-manifest.json | 358011 | 2932fad91eefce2d9e9be9730ad1b54570d2ceb9 | 4903d1b319f995ea3233139d12a7b5a818a4c918a9e607943dab5659ab98bce0 |
| evidence/executions/20261007/factorial-intermediate-validation/cpp-reuse-binding.json | 8743 | c037c65bbb2afc01879268a0686ad211c8c1a762 | 2d05f872bbc18a03fa550e1081789d94b8bd4a9d7d3f5b25d469e51180bf7ef0 |
| evidence/executions/20261007/factorial-intermediate-validation/execution-log-hashes.json | 34647 | 2f57c391519c0f99f112bcc1a8bc24ea03fa74ea | 78e60d8934f8035bef40ded8816399ec9ce689f0fe2341e68159bdff4cf7efde |
| evidence/executions/20261007/factorial-intermediate-validation/lean-unchanged-binding.json | 3753 | ca83a273617e3ea9aeea4457de87b3fe4957fcec | 629c374b7d2f83d1065a19e6824b47ec9882c32b35758bb3f771e053b123ac7a |
| evidence/executions/20261007/factorial-intermediate-validation/maintenance-normal.log | 166 | 7dc0b71cfc4bd1c48447b575494955c45285b086 | a9cca1cdc9afe578ac64553acf77cfa4f50a1da8902400c95ea38f9820c2b635 |
| evidence/executions/20261007/factorial-intermediate-validation/maintenance-optimized.log | 166 | b05c15885077fc99285184d891b794c67786f2a1 | d21e9e488c24eaa994ce671a43d1ff68ef4d50af39ee1e4276a22e28ee46a923 |
| evidence/executions/20261007/factorial-intermediate-validation/manuscript-visual.json | 1343 | 578c8e0228f47442ea0754c47b553c45faca7f74 | f4cc1d06995532bf944e9944424dbc61acb1810453bc413b797363a9f942a009 |
| evidence/executions/20261007/factorial-intermediate-validation/manuscript.json | 13939 | 16339f17205b0e6eb10ac2aa53e2eb13ed0b28b9 | e68aa38d1d137bf99bf693f5baae3295940a787211a272b1ddff445221463b46 |
| evidence/executions/20261007/factorial-intermediate-validation/new-checks/factorial_diagonal_extension.log | 45137 | e9551d324fe0a1c8aca10357775bb8fe92ab4018 | 17a6d13a2778847233b5a2054d40fc24a78b7949c0e4434b9f046ce7824fb5a1 |
| evidence/executions/20261007/factorial-intermediate-validation/new-checks/intermediate_old_layers_certificates.log | 5552 | 689e75b2d8ed05185975b6e804024de95afdcfa8 | 1d9a435ce2ce7b36c5a7de056d460999086b672aec5be94b220101bedcb68b1a |
| evidence/executions/20261007/factorial-intermediate-validation/path-roles.json | 551 | 012b8690c1fbe576334aa3e69955f05917d6ba40 | dd497d12825689b9058ee152e665846832221404ed3b57103f879cd7896293e1 |
| evidence/executions/20261007/factorial-intermediate-validation/pre-freeze-guards.json | 2464 | 12850c83848ad42957f0efd41869e964bb215e87 | 8f56a5e68b7cae57923481ef2aac85104077a4093bf2d3bdd84a6b80f3575957 |
| evidence/executions/20261007/factorial-intermediate-validation/pre-freeze-integration-failure.json | 735 | 8f2555d3e78d931dbbdf2e226b779ca05fb45be4 | 7e5fef55fec2856327d003e6745b32fec792bdf7ebf5362fafc7562a0bf2e15c |
| evidence/executions/20261007/factorial-intermediate-validation/raw-public-hashes.json | 5418 | d6978e650faf6396bebc5ff703abbf55b8302852 | 857bbd08ac7fec1dc31e2bafb3a7608f36bb620ca9255ee3ae5bec4981ebf285 |
| evidence/executions/20261007/factorial-intermediate-validation/receipt.json | 1756 | 2a62bc4a8e366415f926db05a83460ac3a8036c8 | 891aee4cc0e471eb2c547b9b62a4b32ee3ccf1be1224d4a694098f1fd52329dc |
| evidence/executions/20261007/factorial-intermediate-validation/supplement.json | 11924 | 68b22a95c460d36c768eeca7399e117665b90349 | c71266bdbc15fe2f9cbd6d4c50f7116f7475f25cfcf0504fae2b33e44764afe7 |
| evidence/executions/20261007/factorial-intermediate-validation/targeted-replay.json | 4019 | 0462f8b987f6322d8c9d1e4d47f3a4ef51207124 | 6b0b85acf31870a49beaaac57545dcbe504ffd8ed0bad5134472852699815c1c |
| evidence/executions/20261007/factorial-intermediate-validation/whitespace-check.json | 23305 | ced06aca44aca5216b2bae735cd5b45e90d94171 | c12ef4843029d6e28dadbc82e532d56941222804ad4b599ca1b8bbce717d3513 |
| evidence/executions/20261007/factorial-intermediate-validation/workspace.json | 140727 | 1a349544caf815ad69348955229dba7dc23bf7bc | 29797b344336fc5cf22069dffdfafd5363812e475c225cc6b6ffdcb8539321b7 |
| evidence/executions/20261007/residual-batch-validation/README.md | 1213 | e2087b44285f1acd5dd884d213cd2cfad64c6947 | 820c46ce36e039295235c48075657e436256959507797d87ac694ce61d09bf62 |
| evidence/executions/20261007/residual-batch-validation/SHA256SUMS | 3734 | fe69663e172fe104c6d3518f813c34fdd07c5f03 | ab25bb6eabe4dcfc8c5460297895743b513eab3f1c592b9d695c9996e3250d40 |
| evidence/executions/20261007/residual-batch-validation/corrected-archive-metadata.json | 442 | f16445b385dfed1c506bb6f9209f59509ec111e7 | 27a9e45ab2ecef34ee91f2331cc0d2a54e7319b0b7b3a93e8b9a45a9bd4f3d1a |
| evidence/executions/20261007/residual-batch-validation/cpp-reuse-binding.json | 8743 | c037c65bbb2afc01879268a0686ad211c8c1a762 | 2d05f872bbc18a03fa550e1081789d94b8bd4a9d7d3f5b25d469e51180bf7ef0 |
| evidence/executions/20261007/residual-batch-validation/cross-runtime-comparison.json | 2183 | 828792b276101548d3e02881ff86795cde9d503b | 651479089eb25f0e40e5ac99ec417ce907d834c402f50077138b506e44931d7f |
| evidence/executions/20261007/residual-batch-validation/execution-log-hashes.json | 36707 | 538e4803255453dc98a82f18ea65b20a0a357bf7 | 33ce28ae9a4654b0b28570147dec51da47866bdc5b6c51891815f122a6281c86 |
| evidence/executions/20261007/residual-batch-validation/failed-manuscript-first.json | 13839 | 7fe6578300e3a8298406e8887144a7d628da1514 | 1ee74f83a2dbb9f53f5b7fadeb1c4b83f76c8413648b2493693f5a9a49558542 |
| evidence/executions/20261007/residual-batch-validation/failed-manuscript-second.json | 13866 | f22ebf39da0e6be1556a96e0e4d14973af7c25ec | 29bea0186359e58b50e67268c7e020983874b9fee30b6c1926a2d8730b84d720 |
| evidence/executions/20261007/residual-batch-validation/final-source-archive-metadata.json | 606 | 847eddc5ae1708a3e2526b3259a66a4a454b7824 | a051c0a63b7a6b3bc101d97ef5b272621b11171213b828522fedf7849e4163e1 |
| evidence/executions/20261007/residual-batch-validation/fractional-resource-profile.json | 5325 | 4eb4010bd4a3e2de9d2b7c0a250665c2a0441c79 | c9f3d587a559ef009d58b068c2e8dcd50fd694fb991172245ba704ae78b931d1 |
| evidence/executions/20261007/residual-batch-validation/interrupted-maintenance-normal.log | 44 | 33d39af5a8f5e54c3aea6a6204a1e177baca85e1 | 8238ec8f2b16a7b51b1cf9b18a709dae60249101c12e711a8c78978171a09063 |
| evidence/executions/20261007/residual-batch-validation/interrupted-maintenance-optimized.log | 44 | 33d39af5a8f5e54c3aea6a6204a1e177baca85e1 | 8238ec8f2b16a7b51b1cf9b18a709dae60249101c12e711a8c78978171a09063 |
| evidence/executions/20261007/residual-batch-validation/interrupted-maintenance.json | 615 | 444473e3aa2b3a551cae914b3d68e7a483412bf3 | b92441265f781318d3184804d22be4be1cf573b8b2784dd3adf41b83224586f3 |
| evidence/executions/20261007/residual-batch-validation/lean-unchanged-binding.json | 3753 | ca83a273617e3ea9aeea4457de87b3fe4957fcec | 629c374b7d2f83d1065a19e6824b47ec9882c32b35758bb3f771e053b123ac7a |
| evidence/executions/20261007/residual-batch-validation/maintenance-normal.log | 171 | 0ef3fe959643c382a67f491a9e23470c82fc4fb6 | 4f4e53ab156be5ffed237319adb8154e25e8a5979341c8256210e9348d52d4d4 |
| evidence/executions/20261007/residual-batch-validation/maintenance-optimized.log | 171 | 4a70b92d94931b88174f03fec15ba803962c5dec | afd6ae4029cfab933dfbfba9895ebd98e97df01060c14d4338800de7272044dc |
| evidence/executions/20261007/residual-batch-validation/manuscript-format-delta.json | 854 | 15f0c6bcf61c8f108c39e89af9081cac3f3e70d7 | bdbabca8e4183bcb8e054580b7d4c715001447110244a8b08b51a0bfe8b25265 |
| evidence/executions/20261007/residual-batch-validation/manuscript-visual.json | 1568 | 5ae7f81031883cca2d3c16a4e2c7214f547253dc | 938e5290421d4ff5204568e66d4e105b671285f02cb6ccd11e9420ef60a7fa45 |
| evidence/executions/20261007/residual-batch-validation/manuscript.json | 14083 | a8505495ac75ff2892c38eb0dea5b10688b828e8 | aede826c94319c3753ffed327270f0b3e352ffa43b3b1a650210b370650104c7 |
| evidence/executions/20261007/residual-batch-validation/new-checks/central_residual_extension.log | 493 | d6faac7112943c63354a647bb88babe8d294a93b | 0da7d6af5c612d3b06ed87380e9790ea3d469d9b99c6e5432cf0333c3057a8be |
| evidence/executions/20261007/residual-batch-validation/new-checks/half_radius_obstructions.log | 171 | a3d3f8c84ee5cf18aa72e24e4c28915511137ec6 | 5d52245edae278138b13b0b24d1ad5798813a476e23e61fe3ff0e4f02f59af87 |
| evidence/executions/20261007/residual-batch-validation/new-checks/intermediate_old_layers_certificates.log | 6847 | 7847038004da5e22690fc87c8ec0a863eaa5a8bf | d411c4ae994d7eb8894cb00c7a250683ce3e71c494ead2adfd35c14f79104810 |
| evidence/executions/20261007/residual-batch-validation/new-checks/odd_newest_certificates.log | 163 | 9494426b22174b11bf9282d5cc7a37834e90bc4a | 79d1ae72a9bcaba4f63e0493585597a385d615c5d209247bceea0b4616e4f228 |
| evidence/executions/20261007/residual-batch-validation/new-checks/residual125_certificates.log | 979 | 409d7eb5fe6b5c1b5135b8c610017d6545855d1a | 194aa9881eb3f4f852a0385e8c01b8002303040c980b8b3eb8c717d5ffe00788 |
| evidence/executions/20261007/residual-batch-validation/path-roles.json | 373 | 43cb2386e239a336881763a66cd043758e14e92c | 6df3ee2ae8a6df6c4eaa434d93a39aa2c04f7f2fa8635e44fa78a5f2552642a5 |
| evidence/executions/20261007/residual-batch-validation/post-format-guards.json | 3332 | e38dec162a76cf1800ec92ee7588e1bf20db2cb8 | 5aa1d52c695cd616ab4dd1cfa57778bc518fa3b997c741ba96cb9adb84d89e36 |
| evidence/executions/20261007/residual-batch-validation/post-routing-guards.json | 3332 | e38dec162a76cf1800ec92ee7588e1bf20db2cb8 | 5aa1d52c695cd616ab4dd1cfa57778bc518fa3b997c741ba96cb9adb84d89e36 |
| evidence/executions/20261007/residual-batch-validation/post-scientific-source-deltas.json | 1155 | 5ee550d625926a19c4f11f48f0ff4392507c6d10 | d426f5019b7747405102ac099e1c49020a8606cefc15433a763d0115ecdb1e4d |
| evidence/executions/20261007/residual-batch-validation/pre-freeze-failures.json | 3006 | bd88f698ca20fd3786bc3508dbddbcf185f75169 | bcc9926e28d349b264d8a3384691bcded5f3050278be7b554f4cc5707efc60d4 |
| evidence/executions/20261007/residual-batch-validation/raw-public-hashes.json | 12247 | 032cd7bede0eaec7ebdb7f4eab12279cd3a33bd2 | 16db8e9eaaef1baf9e3622a7708b5c61e90a0eb78a6ba66c6ccf2d8ea8593c01 |
| evidence/executions/20261007/residual-batch-validation/receipt.json | 3551 | 735d2fcab5c4a3a6da00c24499e25b530a21aed2 | 89143fedd39eb0bb421c6d21861a33088164c7e4659df5239890eb0e1998023d |
| evidence/executions/20261007/residual-batch-validation/routing-before.txt | 5014 | 7fd1fd11e744cdcb18e461e43e0822a70fd38cce | 641584017128473999d53b145186b5af7f06695f3857e5c8111bb4f63d155f31 |
| evidence/executions/20261007/residual-batch-validation/routing-failure-original.json | 1267 | 38dc10079ad74830b9a79b6a8fa8c70ccb61b2f2 | 733d37d03455e0c6e724c88dbaa965d35084ec5703bcdbb8a5773a497168449a |
| evidence/executions/20261007/residual-batch-validation/routing-normal.json | 5204 | f6f9a72186ff99ac7fdaf36030fd7b5bbec9c8eb | 9cfc263ebd2db41e6e489fc18c68cbe38803d7ffa79b053823414705d4d7a7c7 |
| evidence/executions/20261007/residual-batch-validation/routing-optimized.json | 5344 | 2840abef340d08d9915acfcc9ded3be639082c40 | e71fac6f3eaea5bcfb728fd2f97c2ec11ea66521f2de83813ea425e6cedafa47 |
| evidence/executions/20261007/residual-batch-validation/routing-source-delta.json | 855 | a9c244a904b3e45579ef1f7ee629e7a035592564 | 16b25a3f727e1287e6aacd66e373d035c9e414c62badcc4a7c11905d7e694c50 |
| evidence/executions/20261007/residual-batch-validation/scientific-archive-manifest.json | 418167 | cc30ed1cf9731f3588912223fab357ba1b8b77b9 | c6df374f3d8086744ed188d4e187e8cca9e87ee2977e46b0cf0d9b359a21e19e |
| evidence/executions/20261007/residual-batch-validation/supplement.json | 11920 | 087839540342494bf88ed939d7b579fa8af01400 | c1c607f2c1016b02fd395a18914044c06e247227d73051aa1bad4ede29ce375f |
| evidence/executions/20261007/residual-batch-validation/targeted-replay.json | 10418 | a65cab2779e988a9586d9228507b2e769663c85a | f4192a7f46bd20071f7b758a940a3ae1bf2fd862f6e850e10662a2b350b1ffc0 |
| evidence/executions/20261007/residual-batch-validation/whitespace-check.json | 56585 | b3504d1aab8883ac1c8603eaabb5e766c36fc57f | 2a00d4e06446720b5200ca74fdf9bc9545b5ba2693d4ebd0b533aacbf5a973a7 |
| evidence/executions/20261007/residual-batch-validation/workspace.json | 151052 | 34dfeff5ae7b9441f88639bb6db4659ca4d7f21e | c189d4eceaa8290884219068c81f5d3a9116a02eb976677116a37fe5915090ca |
| evidence/executions/20261008/phase-channel-jet/README.md | 3873 | 2bde21432e805eb600641184f9a77b579fa4e08f | 0f2e3123509b9a685d648a0d87a171752c2fe005c11e3f281fcfa54449dc2c0f |
| evidence/executions/20261008/phase-channel-jet/channel_review.md | 8729 | ac89fd7d87f06a8fef2d98475fe13b7f0b26c536 | 801280b18afd418bf35ebf4a07606878a34cee8059a8648235b7af685dab6b64 |
| evidence/executions/20261008/phase-channel-jet/cpp_verification.json | 139 | 0df73dd48661590d31f3c7a7640a4202a7a00b2e | b055d80bc16c2124dcb86f4e5362a85ff09a797c390c4494611324e3e4be69ce |
| evidence/executions/20261008/phase-channel-jet/flow_scalar_review.md | 6239 | 919b59dde69132f71680eb0def7ace30d1e07041 | 11798a32b960e35bfe8c17d6f873224865ba028c1df7a77d0ebae2fe0c609728 |
| evidence/executions/20261008/phase-channel-jet/lean.log | 14029 | cc8c1ded956d34224fa671b1dccc7e667431d843 | 89cf7aacce57a21426dd829a6c43a338ca2be0b295b8acb04bce65d5cddb969c |
| evidence/executions/20261008/phase-channel-jet/manuscript_build.json | 14488 | b42b57a50c300dacfa87cb8a8cf30d3941e560e0 | d5e6dd37ae9350c6ff7cb8d3d84e64140a89b191685111c0ab9707c2de4dc316 |
| evidence/executions/20261008/phase-channel-jet/matrix_review.md | 11143 | a9c503448deb9c504bfb9310b5fcb82d92b78f97 | cf9e2998f0b243c4587bf257911614e80fa150b8dd46b708b6421e89096cea20 |
| evidence/executions/20261008/phase-channel-jet/metadata_validation.json | 722 | 35f0073e88e6edbb7a088353f6dec5906c447520 | 12432b05a41651f10a72dcdc2590423d37f49b12b56f94f2eb0ee59d1ceb3074 |
| evidence/executions/20261008/phase-channel-jet/python_verification.json | 1915 | 8edf93da49039eb3f9204f43462222cfa3a0e435 | 55bc06220cf59d40b3d1278a0869f1300b93caa277010319f4b4813e28e9bf04 |
| evidence/executions/20261008/phase-channel-jet/run_manifest.json | 9638 | f8571cd457db34b5792013a64ba55e2db5d93430 | 6e3b010acea40b1f89279823d4221a0e063fd4a1006082fbc1593357a7782687 |
| evidence/executions/20261008/phase-channel-jet/visual_review.json | 496 | 099911e297cded1ef4aceea257e327b5ab5ac090 | 98190644b27958a9ff1a1b5c384bf02213fc81439a7e853204269f229e71e554 |
| evidence/executions/20261008/phase-channel-jet/wolfram_receipt.json | 148 | 05fd3d32073944cf6d155b8f34bf5f322e2c8de7 | fd50f298bc2b182eefe1616c3c5e42e7c8616c7512f0e89da89cf8e3126877a7 |
| evidence/executions/20261011/cavity-continuation/README.md | 5026 | c12b3b20a3245d8e159116b53aa72d7e7f999e58 | 82be96692c3b5c47aa90b2f01919b4068de0c50be8f6810e9438d5b1e26ff071 |
| evidence/executions/20261011/cavity-continuation/cpp-controls/compile.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/cavity-continuation/cpp-controls/compile.stdout | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/cavity-continuation/cpp-controls/execution.json | 2396 | c57ff8544c3214256a74cbebfe2bb37a5677fb59 | 5ce7f83ec9b2a48119c15edd6d701f1e9f460644a1c0b4b9873f9f6c549ccafb |
| evidence/executions/20261011/cavity-continuation/cpp-controls/results.json | 190 | 21c7c9e27c7ce5c8b452e44665ef693032867c9f | e8a8ecd2a19e12719ebb11a74b443367ccd52960b75041ca9b3302e13d4f5cdd |
| evidence/executions/20261011/cavity-continuation/cpp-controls/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/cavity-continuation/cpp-controls/stdout.txt | 143 | 843da85c0539aed1e9f3e4a0b5f1a465db8634f5 | 9be67fa9776b6aacd8674f1116959f383b98f79369f8435ab0720ccfb4869237 |
| evidence/executions/20261011/cavity-continuation/inputs/all_moment_delay_bootstrap_candidate.md | 9412 | ba0140cc203702669279b98c0a57656b5aa17e28 | 2b0f8c651ed6e15d803e6af3b0a32c9f712bcb1a28653a74b2ef56afb2be8019 |
| evidence/executions/20261011/cavity-continuation/inputs/python_before_guard_policy.py | 8534 | bae9b28b39de10c3474b2d627a2d3c78a7928527 | 21f3f9b6f8fd028823cd063d8f3f4808e150098197ab8bcbc2ac86d00fbd04ae |
| evidence/executions/20261011/cavity-continuation/inputs/schur_censoring_gap_review_input.md | 7644 | 460ad2c4f9b42fa71cbb9fdf339e4d93947d7397 | 73cc587de1bfaf5d724fcbbe93c3a236da721fe0e05623f4f20d448177082ea7 |
| evidence/executions/20261011/cavity-continuation/inputs/second_third_delay_review_input.md | 15188 | 8ce73fc9025ed21d5681740167bf53d923e7f21e | 34602f2fca944cc45f4e7d91c081ff30dba837f5b2391e59bfe1f6357362b2cd |
| evidence/executions/20261011/cavity-continuation/maintenance/final.stderr | 337 | 2acf493d64301f8ec936f8adda9916c0970d0fc2 | c3eaaa30362b3377988a0e7ad057a059eb938c6798c316f4b643e323310b80f3 |
| evidence/executions/20261011/cavity-continuation/maintenance/final.stdout | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/cavity-continuation/maintenance/initial.stderr | 1197 | 955f9c3c2edadfbe83cfd88bf98b2e4e0fafc4b3 | 48fec6086a503ad77140cc432e38f8eb53e30ff9c226f80ffd161fffa68aaa1d |
| evidence/executions/20261011/cavity-continuation/maintenance/initial.stdout | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/cavity-continuation/maintenance/result.json | 959 | 494465a40bfb372f9592c5d17fab9a9dfbaf919b | 5b9e8d32807913b358ed7232359099db9f9a217b02b44305e05277c558dff977 |
| evidence/executions/20261011/cavity-continuation/manuscript/BGS_unified.log | 41705 | 7e431355de957e304a58ba1fbbf90050f02c78f7 | cdeaebfbc85b327ac37f03b56a7e9062da5751faf154922a6f425cef6f7045de |
| evidence/executions/20261011/cavity-continuation/manuscript/build_manifest.json | 14737 | 0b51e28e481909343c962d013af6003f484e10e1 | 1dd3d8925a4b28509b1be638a5cc6a150c188f7e127a9967f0eed159755264ea |
| evidence/executions/20261011/cavity-continuation/manuscript/pass-1.log | 29476 | 199d1b24a3146bb5ab05537f888292a5fa697270 | 85762b5e09ddb91ad5e62abfb744b01b07b970e01c794e35eb4d7c63b089a9c3 |
| evidence/executions/20261011/cavity-continuation/manuscript/pass-2.log | 18501 | a54f4b1c364b764b4869bce05e033922ee6897ef | c11442d3f120661c166b2f5a29f98b246221037a7acdaf8e628e7d09d4c195c0 |
| evidence/executions/20261011/cavity-continuation/manuscript/pass-3.log | 18419 | aabee8c5a058f664d8c23e08a4e2c190a08f3fc5 | 07a16af0057eee4df8a9d9f3d04209d2e932f25a17c28b87db8a59125bc1a9a4 |
| evidence/executions/20261011/cavity-continuation/manuscript/visual_review.json | 696 | bd827a561d4deb1b12a8a0e617d333820f0a6e4b | e162865013172018ff6e17a8263edc882457f4a461815df85f76a0b9ab8eddce |
| evidence/executions/20261011/cavity-continuation/python-controls/manifest.json | 5468 | 4683e819ce44deaf134f5c7b1646984d8c762f9f | 51c33c2b8119de9e72f46c8760bc483ab9e9b4fe0f6ec71d572a811c67dd5372 |
| evidence/executions/20261011/cavity-continuation/python-controls/results.json | 678 | 57d03be91eac6a041aacf3f63dfe0814cb382cc7 | f22881962b755b98c7571d1389dd273271ea945c7b2c33c259cacbc7aa46c7a8 |
| evidence/executions/20261011/cavity-continuation/python-controls/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/cavity-continuation/python-controls/stdout.txt | 678 | 57d03be91eac6a041aacf3f63dfe0814cb382cc7 | f22881962b755b98c7571d1389dd273271ea945c7b2c33c259cacbc7aa46c7a8 |
| evidence/executions/20261011/cavity-continuation/python-controls-guarded/manifest.json | 5516 | 8e581f53cb66650eda104e5985d71c78143ee3b3 | b903e85971788154a1d5618f7619ebdcb5a2307fe3dd023e6c65eed697e2bde2 |
| evidence/executions/20261011/cavity-continuation/python-controls-guarded/results.json | 678 | 57d03be91eac6a041aacf3f63dfe0814cb382cc7 | f22881962b755b98c7571d1389dd273271ea945c7b2c33c259cacbc7aa46c7a8 |
| evidence/executions/20261011/cavity-continuation/python-controls-guarded/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/cavity-continuation/python-controls-guarded/stdout.txt | 678 | 57d03be91eac6a041aacf3f63dfe0814cb382cc7 | f22881962b755b98c7571d1389dd273271ea945c7b2c33c259cacbc7aa46c7a8 |
| evidence/executions/20261011/cavity-continuation/repository_check.json | 1486 | 9ece8df8c2a4beb65336417a4c719864216165bb | ebbcd15612caa9ed50c59db3dab3131774b074e69ae8599888329ef282fb8c67 |
| evidence/executions/20261011/cavity-continuation/review.json | 2146 | cea6060afdfed7c699dea593bcfd9f1a78ba0695 | ee174a029c2fe109369c3840ce797cbd2ca84bda8c00ddc1ab7201edf2fcca93 |
| evidence/executions/20261011/cavity-continuation/wolfram_execution.json | 1129 | ecc46b182e14cb02fd5735aee8b75767d1699635 | 0cb1c6e116e020626677b3811ba8614734e2ccfd941d4e9a521267c2d63c00e5 |
| evidence/executions/20261011/cavity-continuation/workspace/cpp_schur_censoring_energy_verifier.log | 143 | 843da85c0539aed1e9f3e4a0b5f1a465db8634f5 | 9be67fa9776b6aacd8674f1116959f383b98f79369f8435ab0720ccfb4869237 |
| evidence/executions/20261011/cavity-continuation/workspace/focused_outcomes.json | 697644 | 198ea6ffc1b8152fef92cf85908fe323a35e80e8 | 2d7fd78f5ad7d38835484e54568acae21b80b9157e8db8de0c074b54e9e80bfc |
| evidence/executions/20261011/cavity-continuation/workspace/schur_censoring_and_clock.log | 678 | 57d03be91eac6a041aacf3f63dfe0814cb382cc7 | f22881962b755b98c7571d1389dd273271ea945c7b2c33c259cacbc7aa46c7a8 |
| evidence/executions/20261011/clock-universality/README.md | 4684 | 4ab5328f4775d7226a7fa4c558cd0aac31e4e1a8 | f775ac48eb2eac5a4df0ac9405c13a27be0f10a127e4dd029842eae0c47ac8e4 |
| evidence/executions/20261011/clock-universality/initial_control_disposition.json | 670 | aafb7f3a07941cc2d72fd43926e7088efb5a03be | 8a242d7106148f8f3a8bb35530a9c1c0fd682ac60cacdca121e1821b7100595c |
| evidence/executions/20261011/clock-universality/inputs/conditional_clock_review_input.md | 13890 | 0f162bc7645f0192ef3f4432a413c04c46f4c259 | c30e1f4dd75e98091343cf864737aacde75b2c502f2abfb82f08618372c8eee9 |
| evidence/executions/20261011/clock-universality/inputs/full_depth_review_input.md | 4675 | 14afae07a7716b15b696c207f29f73afadccf554 | bfa8f7e7a621fd7f13718183593092af755bc60ddbfd76af4d681277b097fe1f |
| evidence/executions/20261011/clock-universality/inputs/reference_verifier_before_guard_alignment.py | 4511 | 1d36e3c404b6b8fa2affea247a7e96c5da9443f9 | 848aa88148e364bbcda26767b7cd1e93d3f13870a28e5e5d65df6f47f4d9034d |
| evidence/executions/20261011/clock-universality/local-regression/accepted-entry-policy.log | 1337 | 27eea153915a3fd66a32fdaa71d5c20d5ba3b41b | 036375b86710a9a5dced00382bd67acea3c961ad8ada7d6134ddf2b1a0909460 |
| evidence/executions/20261011/clock-universality/local-regression/initial-full-maintenance.log | 52822 | b9310511ff9628c38b955c314733e151c07e93b2 | c3d68c637bb65d54de48c2ec041cae2faff7ef9368b34b33423b0b7cd93d0d9d |
| evidence/executions/20261011/clock-universality/local-regression/receipt.json | 1593 | 761740ed18941b7c8b8a5da93778ca5b1400f454 | 6c07d7e92340ecf3d49be50072178cf72103e057b917434772785c3cccc38ba1 |
| evidence/executions/20261011/clock-universality/maintained_transfer_review.json | 964 | b381299bc9d196b0b778d62bc945cddb51a24bba | 7b9da4449d69cff8732fc472f8e8d2393894411436382081fe6ac772c486d3c4 |
| evidence/executions/20261011/clock-universality/manuscript-build.json | 14769 | 05bcd55dc56baf410244f895037ef2f440509e17 | 61227fa2deff0ec7a42d256f125626cbec05b2d4674fbe3b9ed3b5962820bfe2 |
| evidence/executions/20261011/clock-universality/manuscript-initial-build.json | 14525 | 557ad910997e89bc1fb64ff68a3ab112eaabd958 | 75f0d7da954382dfa49f0b33a31836186b899c9249c9781eb5e190d6863924f5 |
| evidence/executions/20261011/clock-universality/manuscript-visual-review.json | 1664 | 9bfe797d73d264337904267e8167d8f4609f6042 | 3bf6a7a1b51c6ee83340c81cdf511d7db5996356452d5316352239e568b23a1f |
| evidence/executions/20261011/clock-universality/reference-controls/manifest.json | 5720 | 639b4d3b0a713d428c3381cdd9cfeaf386d21259 | 63496983383ce59e95de77fd633c9011d93a071224e8a3716d0416f7938e3bb4 |
| evidence/executions/20261011/clock-universality/reference-controls/results.json | 1155 | 5791316d907512dfba893700dc0edf69ea6df613 | c1996aaeb86c4b560afb1c473c3c5ed5af63ffd8c2fe4124aa608667bcfffdb8 |
| evidence/executions/20261011/clock-universality/reference-controls/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/clock-universality/reference-controls/stdout.txt | 1155 | 5791316d907512dfba893700dc0edf69ea6df613 | c1996aaeb86c4b560afb1c473c3c5ed5af63ffd8c2fe4124aa608667bcfffdb8 |
| evidence/executions/20261011/clock-universality/reference-controls-final/manifest.json | 5757 | f669e7b7d4a3ab4869913efaf5d3808d0105dd0c | e2d08ca85ece10ac6309788a8e92164ebe8ab5537b85cbc4fbab4ac2ebd22103 |
| evidence/executions/20261011/clock-universality/reference-controls-final/results.json | 1155 | 5791316d907512dfba893700dc0edf69ea6df613 | c1996aaeb86c4b560afb1c473c3c5ed5af63ffd8c2fe4124aa608667bcfffdb8 |
| evidence/executions/20261011/clock-universality/reference-controls-final/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/clock-universality/reference-controls-final/stdout.txt | 1155 | 5791316d907512dfba893700dc0edf69ea6df613 | c1996aaeb86c4b560afb1c473c3c5ed5af63ffd8c2fe4124aa608667bcfffdb8 |
| evidence/executions/20261011/clock-universality/reference_review.json | 1487 | 2d786c5cd26a8fe22279c49671cb106eea8453d7 | caae2353bbe97103c4ecff1fc1be364c6f5233c03650b3073cfef9833ae979d5 |
| evidence/executions/20261011/clock-universality/review.json | 2860 | 03d6f49868ee4e98ead614005c83bc3227bd0373 | 79aaef96b87c608eab36195a5ae13b31bf52b4e8c8a24b5f91459c04a11d139e |
| evidence/executions/20261011/fourth-delay/README.md | 2605 | fb6b22b206f4cdded755dcf0eb36f440abc6b658 | 3e767d92bf5bb5d2b53b4a8c1df66df75498e11be989e78aedc20dfa28bd7286 |
| evidence/executions/20261011/fourth-delay/cpp_zero_diagonal_execution.json | 1351 | 9146e502907911ae812c24fe8e77131803b9fe3a | 2407a073532bd3b776cdc2dde51e238d2792ba0aee5c6ba213033527f153092d |
| evidence/executions/20261011/fourth-delay/inputs/fourth_delay_review_input.md | 10361 | 6946180bdd51469c199550bd1bbf23450e599ecf | 3449208ac78c54ce16a06a2dc3e9769183158ab793754eb6e68b1986a8ef83ff |
| evidence/executions/20261011/fourth-delay/preceding-ci/computation.log | 108817 | a1cb16f57f6608939adb6fe92bca73d8fd719190 | 11a713f0aeb0477b27862f97f532336c5d82e8688a15b558240bee560ba1c82e |
| evidence/executions/20261011/fourth-delay/preceding-ci/formalization.log | 32542 | c0138ff352cd6b1f890b50533b00d00b0ea1b06a | b8bf66cf68e7eef2e92746b009b37c934d6d0cad36b3a786ea67c0c0e6a520b0 |
| evidence/executions/20261011/fourth-delay/preceding_commit_ci.json | 2575 | e220e52280db019b83b282393da38df59ff0aa12 | 028c89b2e1d59d0b9a37fd9d41443c8355015230e1965cad853f5ec2cf65ab84 |
| evidence/executions/20261011/fourth-delay/python-controls/manifest.json | 5930 | e3ed0912dac1e2feb55ec413ed3683f84478e10e | 6dbde2995081da48106adc553b419593e2412b5bf3ec554a5a6dc9194707324a |
| evidence/executions/20261011/fourth-delay/python-controls/results.json | 1068 | aee71466fa06dc5fe32004f4c5a2c5da042bae81 | 7cb67e772e502f9b2489d11f0366e053728b162171be0ad51922a034848f9e5d |
| evidence/executions/20261011/fourth-delay/python-controls/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261011/fourth-delay/python-controls/stdout.txt | 1068 | aee71466fa06dc5fe32004f4c5a2c5da042bae81 | 7cb67e772e502f9b2489d11f0366e053728b162171be0ad51922a034848f9e5d |
| evidence/executions/20261011/fourth-delay/review.json | 1510 | 6e853c2311a62407e6f8b2b7bc205428ade929a7 | a455c43f965c90a261de319b55db149a25be79e3641fd675e42cd2c6459a56d9 |
| evidence/executions/20261011/fourth-delay/wolfram_execution.json | 933 | da6bc5cb727efd95759007a54202b7ad7fccebee | 69a3d526846f116bab6a7b43248caa938ecb3d217aded8a7cecb0e5b72aac3de |
| evidence/executions/20261011/reversal-gap/README.md | 2754 | 32c24929822e3eda85e7996f826afad9ff77c7f3 | 3e9d6757508a8f58b84ddb293cd2e70ebecb5c402ffbe4f814e1c4e17141b7ac |
| evidence/executions/20261011/reversal-gap/inputs/reversal_review_input.md | 2622 | 7ee9d655fbc12d717a04a8f04d4b94f91415cd29 | fb77ad79121e77f0c723ebd1bbde5fa5ede3db0a6e2ca7ddb6dc4680c28f67b3 |
| evidence/executions/20261011/reversal-gap/manuscript/artifact_check.json | 1020 | 82b92a1a392ffcf1c5fff2b189e1e480ef04ab0f | 643587f88531339ff54ad812cdf910b65bf9f2f2092011b563757216b9c45440 |
| evidence/executions/20261011/reversal-gap/manuscript/build_manifest.json | 14729 | 62dfaba8c15f89632ca0f6f452934e38cd73d918 | 1318e9ccf058d37ff9ed3f5b3fc2221e53250a686f0de3f02f65ad6d81e46da8 |
| evidence/executions/20261011/reversal-gap/manuscript/pass-1.log | 37659 | d2e3b5cc7be6bfc30e4e83a0f621a3340dc58230 | fcd36532183ba777f71783b966c7af0d459cd3a0747c7d00564cbff4aa61a703 |
| evidence/executions/20261011/reversal-gap/manuscript/pass-2.log | 18480 | 8ee2ea5d2409f78ed079a409a861ce3461ae5ed4 | bda5981a1c58ca0952740a48ebc257834a564257241d6d6523a11c19778a61e9 |
| evidence/executions/20261011/reversal-gap/manuscript/pass-3.log | 18398 | 60795b806653732ed9014c6699ada88290ebd60f | 9bd15bd08662735deb75d561e9eee551424266147bbf205fe0bc9668d94fa488 |
| evidence/executions/20261011/reversal-gap/manuscript/visual_review.json | 613 | 4d6a6d4831c17026e4c20187bb3509fa11e8df56 | 7c3f4cf9b45a50969a1d1bd1f001fd81823004a802a8a7e5db488ad61f62ed44 |
| evidence/executions/20261011/reversal-gap/predecessor-ci/computation.log | 108812 | e572f2f523697b0198eb9302f8cac56908b3668a | 84fedad51afdc536f476dbd9626f77c4d2e5d4ab939e91d76104e38ca87ecbdf |
| evidence/executions/20261011/reversal-gap/predecessor-ci/formalization.log | 32538 | dbb9503566ed60aab4ffc4b26035ea15c144dafd | 75f222ab4651987fabef9440f797c80ada613e0aa2622d917201024cb17b4b14 |
| evidence/executions/20261011/reversal-gap/predecessor-ci/jobs.json | 22412 | 2c9ec45a59c22e17caf0334aaf87e418f18a72e0 | 6e4b3757d34bc78cc88225647d9d96d36355d8449302f6635c23595425b78bfc |
| evidence/executions/20261011/reversal-gap/predecessor-ci/result.json | 2845 | 0e1e417b3f867a39adaefda77901c131a303da01 | 1d52b931e843f6279f6463f654abf2cc84d4775dc1e0143807f0fcf48cefe431 |
| evidence/executions/20261011/reversal-gap/repository_check.json | 1103 | 824bcf82b045e942d2b7209a24ae1ed9bbff531b | dcd2e070e1e06584c25844e6b43f6f29921a9e25490c2fc42603dafaaf61fc0c |
| evidence/executions/20261011/reversal-gap/review.json | 1128 | d4587fb6e305a222f7260868699de44f0ca66705 | de9fcc5c685450972a85fadcc4b0d76fafb5e33cbc1df2957cbef4ce59193c78 |
| evidence/executions/20261011/reversal-gap/wolfram_execution.json | 968 | 214a5aa8791952ec7c60491d6a1e9c51d0543b01 | 8a71ba7e806987f9260a71bd721c90bfcb09540550eb9ff57b31f12b201d25bf |
| evidence/executions/20261012/haar-feedback/README.md | 4406 | 2594c01eafc0ad2de566575063d26d840316441a | f55206256e9fe5308b9f8b24f2bc4bb4df43eff1356d5863f2e1b4186125946c |
| evidence/executions/20261012/haar-feedback/comparison_failure.json | 830 | 6638ed59201034fcadabf7130b322055519491e2 | e2b9e1ea7cd14b264cd7d86f0a722a1c680bb41bfbc5cfacdb05fd559d011508 |
| evidence/executions/20261012/haar-feedback/editorial_clarifications.diff | 1406 | 15be261c1dc50da3eda11cbe2b16efe5048a4f0e | 31dfd5a9d27034add539418a2959a207cbd720e4da06e822f3349d42206818ac |
| evidence/executions/20261012/haar-feedback/finite-controls/manifest.json | 5983 | b6d07c8be6b64d524f8b4ca499b3c9045f3ce1ba | 1c5cdd75b2026cb63eb0d59d5a1f8b2ea60efea8cb46bf30816d4373e31f68d0 |
| evidence/executions/20261012/haar-feedback/finite-controls/results.json | 2471 | 82b0fe491d8ac200183155665384e33fd3f28e09 | 6a73b5dc1a76af5b2082ea25c350a1b45f3cfa2eda3d8053b4dd6bd93e46781b |
| evidence/executions/20261012/haar-feedback/finite-controls/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/finite-controls/stdout.txt | 2471 | 82b0fe491d8ac200183155665384e33fd3f28e09 | 6a73b5dc1a76af5b2082ea25c350a1b45f3cfa2eda3d8053b4dd6bd93e46781b |
| evidence/executions/20261012/haar-feedback/haar_feedback_independent_review_20261012.md | 21072 | 5108e1527bbb7030b957d6f13bd94b721f56d8c3 | 5e2e6eb96019c68233c60690a5476261520a3e506227861407656032235dbfb1 |
| evidence/executions/20261012/haar-feedback/haar_feedback_maintained_transfer_review_20261012.md | 7504 | 328bcee6d2c0aa250661033bb1c669af59bccea2 | 4776f4afc0ba66797f3f80a3888d0f02724cc140d873c1cb1808050d9f4699f1 |
| evidence/executions/20261012/haar-feedback/inputs/haar_feedback_review_input.md | 11704 | ef0f736d1236422c902dced460ccb94372ac2b20 | 7a717c01207e12cf8c7ac6c2cc2f0ac95b625d36a0b3e5bdfd30ae72554b8c22 |
| evidence/executions/20261012/haar-feedback/inputs/maintained_proof_before_editorial_clarifications.md | 15700 | e54f331e7de80723fb02b906194e0fdf63ea78e7 | 41015612e954913ea1fcc8b2a44962b9143bbcf0ae990da503e9d42baa1e8857 |
| evidence/executions/20261012/haar-feedback/inputs/manuscript_before_linebreak_fix.tex | 39509 | 48f5e5ef4ec5e079e8778f52bd8a29a8002def84 | 5f53b59a26dfeea933c6b239de37d1b6746c496a7263d04e2ca33153c4dce576 |
| evidence/executions/20261012/haar-feedback/inputs/verifier_before_comparison_fix.py | 7285 | 466cbe715d61c3190661afe649c12518c957490a | f3951111e3e2dff29f7ec3b40c579fbd69c497e8a19ce92dd6e4bedab728c332 |
| evidence/executions/20261012/haar-feedback/integration.json | 2250 | 9ff18147f6587b6fd8cc540ac8e92f8bee334fe4 | 9d6950e02acac142b7f9e8f4de71dace5b40d2d4885e5a78d88ce7a467452b18 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/actual_one_pinch.actual.raw | 5905 | e229580f63b734cfe84f219a7200926a7d246362 | 381d51b6e1e24bcba7eda561a38507a9c002539bedd68cea52f556abe2633400 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/actual_one_pinch.adapter.json | 379 | d0e9eeeb80323e27eec81cc7f7c595f1e3a25020 | 1c34b8cb17e2123d855c31a4e990577bf791a25ab123e5fb87aebc3cf396c7f6 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/actual_one_pinch.expected.raw | 5905 | fa5b1b51c3cf3412785fa3b2b0f4017dc25096e0 | b8c0d149119923a3bb330d9194188a35c27bf805afbc15960cae9f7901f0341f |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/actual_one_pinch.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/actual_one_pinch.stdout | 326 | 56a545b43fb2ca3483e7ece5687ffdca97c0636c | 294ba427ac6142362498f38959fff30e173fbbe68d3e59658cf7e7dad889637f |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/centering.actual.raw | 4451 | 85d32102509dba87ffe306defcb028679290dc20 | b6f20ae45b8a62bb1df7c8a9134536e8ae23a221595f0426d619040b4bcd60f1 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/centering.adapter.json | 383 | 62c0e1bee12934b4b78a8918387814fe3eea9ed4 | bb1da8dfd565c2c467eea0c2802b4e7b4b2760db08d9fb0e63683e77c0c6d89d |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/centering.expected.raw | 4451 | 85d32102509dba87ffe306defcb028679290dc20 | b6f20ae45b8a62bb1df7c8a9134536e8ae23a221595f0426d619040b4bcd60f1 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/centering.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/centering.stdout | 4451 | 85d32102509dba87ffe306defcb028679290dc20 | b6f20ae45b8a62bb1df7c8a9134536e8ae23a221595f0426d619040b4bcd60f1 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/echo.actual.raw | 7591 | b0cb2a0a522b83423ecf8d0ae9bc9b4e5fb5b592 | f7ef02b66f20392430f03362590339f8d2797df5033c03500c87c46a8df79bd9 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/echo.adapter.json | 386 | 63d7e9aed04b6da26142b968d2ec64d1b3d3fa96 | 668b8d85b39a90e39364c5b0a565a77f36e22c1ae9c2dc37119749ba1061d7e0 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/echo.expected.raw | 7591 | b0cb2a0a522b83423ecf8d0ae9bc9b4e5fb5b592 | f7ef02b66f20392430f03362590339f8d2797df5033c03500c87c46a8df79bd9 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/echo.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/echo.stdout | 216 | fb22b8a4564436c2229a13f417579585e72c3baf | f7331c6d02bfbb28d30b08e8eb85e4cfcf65b793558e8fa3aab39a2bc4fac7eb |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_bridge.actual.raw | 4687 | d0f5da5a7a87625b3f7cf30ce7b2bfbe541a099e | 41a65e5a047e1d0c5c7e1de8a3519868c66ba2d30a7557014c07a10c84560e86 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_bridge.adapter.json | 735 | cab964820b1c970ba373e8d7ee485cd89fc7be20 | d8bca6cd2a090030caa7a2b4567ed5c342c5709c73240bd374bc4a1a47895ceb |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_bridge.expected.raw | 4688 | 99716ef538047aad940833ec1df0dd6502299c59 | b0441b56e8414034cbdbb207f017f77767776fb24d76a67261ea44ea4bcbb2bb |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_bridge.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_bridge.stdout | 4687 | d0f5da5a7a87625b3f7cf30ce7b2bfbe541a099e | 41a65e5a047e1d0c5c7e1de8a3519868c66ba2d30a7557014c07a10c84560e86 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_downstream.actual.raw | 13981 | 5b014f5783b7f6ec9ba2e2a8a1ffc836f6bf434b | ef5c13f417eb80724c2363e96ab6f4f0b37449d72ef042a77768a833fd84eae2 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_downstream.adapter.json | 392 | 6a728d68f9ba08b4a104e2b73aa7051260cfd10a | 287afd63f9a922c4e7c57412f8eef8f057510da725ad86df254a82440029474e |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_downstream.expected.raw | 13982 | 19954035c044ee1e9ba627769c07cf434e025c7e | 10d96c5dff633d03a1f3984db9bd896ce0c62b3ef7e45b081971ecea7eb849e3 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_downstream.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/hook_downstream.stdout | 10028 | 3f4d8a363e4b0497e22ea3d977a52578567243e3 | d022bca6423b0d92666bc8dc2be0c45c89eabd6672caed4c600c98d5bd80100d |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/replay_contract.original.json | 16686 | f3ec042044f58cf16aefffc7448bb0c949a3b3bf | 429f939c7b7336fd184fc81d883bad47c5849d143ecb1e9e39a23d082ee8aa73 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/replay_manifest.json | 60056 | ecee9567b3b0fc1efdeb87abfe71d8a4532e8fbd | 08fd2f0d2dddcbcb9e4f49cb31fa6a02d47810e9f366972e9501b1a2b1bfbdfd |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/rounding.actual.raw | 6930 | 0b3c8b33fedf3f08c7573f9b36446178b28c5d79 | 81ea08c54e6afaf2b11ad7bd2a0ac4074c1c69317f727355544d5a578ee743ad |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/rounding.adapter.json | 383 | 20dd428e7626743f8efdfbc9bb7ac7bdbf2b83de | ae925e984fb291b284dea2ca9408bdf49804da4ba871c78b331c2988102b9414 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/rounding.expected.raw | 6930 | bd592ecb17ef5e6a315603d95a92aed2ae1da451 | 53c1e4df13309d046e211cee460bc73464d08f114ad2c06efd943a9a5e50cc63 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/rounding.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/rounding.stdout | 263 | 4d23cd2cafdf50cc5c493eaa28bd901d6c7f6405 | 07f720095ed57976d1f5e9e82375760fcabd69d1f1d49d8aeb7180f0670534dd |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/runtime_scoped_snapshot_manifest.json | 7018 | 0c7c9f1f6ec7db1b546df524d56c89efb18c5bac | 7b5509cbfdc3a53d95ce18883fb54c1022809895efa52ccc3a2d95298dc07988 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/scoped_input_bindings.original.json | 18009 | 0513c7ea0b3a80a30aff92170f4df15d7a719dcc | a76cec5e74703f260d4529b7eb46c071efc993fcec3fe6ce633b1bb4499bbfde |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/source_bindings.original.json | 10482 | b690574f106922c10ff82a454679e5ad2dae8efe | 78436b05df152c1e62c98b16b381e09915018b1ad46078530ac35eae0ec28a6c |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_covariance.actual.raw | 2577 | e4ea4285d6de3b1ddd1d20fc2fc0dde60cc99a5b | fe0565457e0f18173e9fa787070d532a44d3ebd1b149925a92c4b592f8b927f9 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_covariance.adapter.json | 395 | 68a3774f48988d7bc0b4f0b73b35c5c555ffefb7 | 0da022c72989f30006314d706dceabaca9269c48d35fe53d1ada6d3a4331f01e |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_covariance.expected.raw | 2577 | e4ea4285d6de3b1ddd1d20fc2fc0dde60cc99a5b | fe0565457e0f18173e9fa787070d532a44d3ebd1b149925a92c4b592f8b927f9 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_covariance.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_covariance.stdout | 2577 | e4ea4285d6de3b1ddd1d20fc2fc0dde60cc99a5b | fe0565457e0f18173e9fa787070d532a44d3ebd1b149925a92c4b592f8b927f9 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_permutations.actual.raw | 1078 | 4739aba5944b7705f07b590fe1e7c1a141f559e8 | 225c1d15889ea85576bc949dde241b0aabbdff017c03c9861b05663ebf327ff7 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_permutations.adapter.json | 395 | e2e1de41c3a9c4e8ca8d634a2855e5e7d01f049b | f82d1a61e6298105a476270f1fa0a25e3a52b4559f3deb045510c616b837048f |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_permutations.expected.raw | 1078 | 4739aba5944b7705f07b590fe1e7c1a141f559e8 | 225c1d15889ea85576bc949dde241b0aabbdff017c03c9861b05663ebf327ff7 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_permutations.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave2_portable_replay/ward_permutations.stdout | 1078 | 4739aba5944b7705f07b590fe1e7c1a141f559e8 | 225c1d15889ea85576bc949dde241b0aabbdff017c03c9861b05663ebf327ff7 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_exact.actual.raw | 705 | 360925b367299fc7b2e2356a539b974aa1a47b71 | 13c635af35d07502abf4153ca59ef20ef8f5ea2dc659562906f99ef33becfafa |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_exact.adapter.json | 380 | e441048c327bdae3ad2a4f5f9b60162521b20d8d | 8598939b41568d5f987561361fc45fdb35dfc995892d91f6be084cb2bb706979 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_exact.expected.raw | 705 | 360925b367299fc7b2e2356a539b974aa1a47b71 | 13c635af35d07502abf4153ca59ef20ef8f5ea2dc659562906f99ef33becfafa |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_exact.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_exact.stdout | 705 | 360925b367299fc7b2e2356a539b974aa1a47b71 | 13c635af35d07502abf4153ca59ef20ef8f5ea2dc659562906f99ef33becfafa |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_independent_float.actual.raw | 434 | 96562b59231464a7741f1f7d82d7b1e7b87e6811 | 3db91588656b681318d0b6f489a3c7d7efd8d27d68280a51b7829b6df2b84df4 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_independent_float.adapter.json | 394 | 0b2c5731f6657ab50406358149ceda57b2e3a0aa | af66193f0eb8eb8eb67c662e8550c7153bf116bb409002a4bbce18d0260091fc |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_independent_float.expected.raw | 434 | 96562b59231464a7741f1f7d82d7b1e7b87e6811 | 3db91588656b681318d0b6f489a3c7d7efd8d27d68280a51b7829b6df2b84df4 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_independent_float.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/convex_independent_float.stdout | 434 | 96562b59231464a7741f1f7d82d7b1e7b87e6811 | 3db91588656b681318d0b6f489a3c7d7efd8d27d68280a51b7829b6df2b84df4 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/replay_contract.original.json | 3882 | 6a4d97ee5331b9c2770add07b3e7b287cb057771 | 36922db684054a0ac061778231dcfad377752690bbd2e6b0d8a57e85e75e8b68 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/replay_manifest.json | 13477 | d616fe362b729c1b53d7768b26f3da51b5759990 | d9506b883cee5d5cde5386a9a8ab6210d7ea224d898e2fcf156b3df8443be4f3 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/right_frame.actual.raw | 7262 | a680b1b63d5d9c788e310e384ece9febdeaa2fb7 | 63327044439d36894735df945f8e296a04f63cf81667da1c498fe89db1ed7c4e |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/right_frame.adapter.json | 381 | 655cd3464ba0fb9cb29ce8e6da7e4c1195a1e0d1 | ec9067626da95ec6546f1846029244e4f1862899057746a9eb4cf423f6ee1b77 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/right_frame.expected.raw | 7261 | 7a9d3ea72d33d0ad51caa251e7876ce1b4d3d188 | 72e86c793201c8b3d307442421f3d5a5f4140bd73138c6bafa910ce723b13a34 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/right_frame.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/right_frame.stdout | 342 | 2d341b19f884beaef6185de166a478e67661acd7 | ee70e6f51fb75c806c158097dd4ebbc6e1a753b23ab32e99ad5b0d82c858b04b |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/separated_S2.actual.raw | 10123 | a3474ebcd63a94f884fe6d00cac4366d00f5cd89 | fa8e2a31615abb99310510b7de7b35d79beec3f242f0f089f75a4aacc53efbc2 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/separated_S2.adapter.json | 393 | ec97b16ab00f79a2d7e6aa2fdb233f96fe8e134d | 81f5fad2825f65f9847f37b36ca1b315cf95854f2b667a88b10cce1593a72079 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/separated_S2.expected.raw | 10123 | 448d44c8b2aa877a5b6f03a9f9083d510986fee9 | 1f6422b91f3532f084cab0567a1f4f2a752ecfe646244f6237078a8c156c39fd |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/separated_S2.stderr | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/separated_S2.stdout | 310 | a39e283fc0280a229bac50d491c02cc2a347eefe | 9c7bf14ba3e2c1a7db06484c4f6d648a6da01f0ee4b79329266c2ddee5824de6 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/certificates-pien_nz3/wave3_checked_replay/source_bindings.original.json | 1811 | 3273daf2bc7f2f1e97b6ec0305e296a25cc93cc9 | 7c1d9ce7e9194f4c9768b82c6bc05cf386fa53211911eb73744644d2db46f0dd |
| evidence/executions/20261012/haar-feedback/local-regression/logs/chat_research_20261011.log | 2177 | 91fe201b27bb21b478e6d5f582e834a4bda33981 | 3824d6a93c6027a361703f6fec1960e6f9a70419f85e8507a5b593f1de588f93 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/clock_reference_measure.log | 1155 | 5791316d907512dfba893700dc0edf69ea6df613 | c1996aaeb86c4b560afb1c473c3c5ed5af63ffd8c2fe4124aa608667bcfffdb8 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/haar_feedback_law.log | 2471 | 82b0fe491d8ac200183155665384e33fd3f28e09 | 6a73b5dc1a76af5b2082ea25c350a1b45f3cfa2eda3d8053b4dd6bd93e46781b |
| evidence/executions/20261012/haar-feedback/local-regression/logs/two_step_restoring_drift.log | 1321 | b92e0837d7ccdb93425d3dd0ad22d8489609605e | 62a7143adb43d03ed218a4b4b534b15dd57568a6c7bd9a2299644745efa2a40a |
| evidence/executions/20261012/haar-feedback/local-regression/logs/unitary_two_step_obstruction.log | 3008 | c97194743ee902771ecc02c123ed1804c225ffce | e0aa4e1a97e72d3fa2c82063ce1459d32d16111bdb3af36546fc564d9d5b9d10 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/wave2_integration_audit.log | 435 | 3c782568fab4fec802cec1004055e3606a382711 | f5285c60610f2fbfcaa5b2aca5363a2c9a71b460e9d0bb84a95d846df812ee45 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/wave2_portable_replay.log | 68 | c74e3cbfb6df86b373cca80bf43f1e25630d615d | 80a97eac99637c32768345b20381468d0925134cf68056d8b6a6d7dbc662cf9c |
| evidence/executions/20261012/haar-feedback/local-regression/logs/wave3_checked_replay.log | 54 | 999f1ccab6237070aa98fc4206d39f33e50176fa | 2802003805a7be2e9c4c481d871a19e6ae8100761f4903013ec6d644af89f584 |
| evidence/executions/20261012/haar-feedback/local-regression/logs/wave3_integration_audit.log | 497 | 1a1a5597c01580fe930bf51def02f850e82a3711 | 2a134ffb5d28863e3096706c5e4b9c50b4443842222a13131accaae1db6303e0 |
| evidence/executions/20261012/haar-feedback/local-regression/workspace.json | 723246 | 377593790903d75862d4bc953596299ca17ec038 | 386c1441334a0ceca35dff8a7c51df5b3cf96ea092cfd3524369328781f0f7d9 |
| evidence/executions/20261012/haar-feedback/manuscript-build.json | 14753 | 8e1e4f04d6604a5be9e3b39e20867bca17b167c8 | 2142ba3eae5448451ae7c16d097cb4af128397535f25ba1910c3be03b76da912 |
| evidence/executions/20261012/haar-feedback/manuscript-parse.json | 714 | 97e97f6731ec9c6740d8ee5d4184665899fd414d | 534d561add321f1c45afb66a34480beea50442500fc1c416e2ec9dd786060e3c |
| evidence/executions/20261012/haar-feedback/manuscript-visual-review.json | 1657 | 2578bd99a195e57f96d5fd5d391bec39eef5ab27 | d5129acdd0e3b49257f1f829b2121b83c50f014ad4a39d99a1d8c4903c7c0e31 |
| evidence/executions/20261012/haar-feedback/policy-tests/01.log | 1336 | 9c8e3886d4a69fd444c4092e4f163cee3ffff571 | babe2efe1281bd405e15d9685fd1f1ccd3c5efd64fba6b5ffc70f9bd7a6acc53 |
| evidence/executions/20261012/haar-feedback/policy-tests/02.log | 1237 | 83cbf643c66ad2bd85726ccae7dd7a7091db32c6 | 68263996980170a30e40580ed780edb014ac939b0829bfaa35d51ad3d8e04433 |
| evidence/executions/20261012/haar-feedback/policy-tests/03.log | 818 | a54ffbacc037ef4eff0f01ed6f50f8351f07b488 | e352355cc1d283cc8124ba10d58818dfeacb30730cc4beeac042370d531da36a |
| evidence/executions/20261012/haar-feedback/policy-tests/04.log | 185 | 9fafcc335d19bc0c06c5e13fc70985ab3d26a7d2 | 1db6ded051f3cf60a21fbffd485c3537dd808398706ead1931f3067e9deb7934 |
| evidence/executions/20261012/haar-feedback/policy-tests/05.log | 766 | 07c40e569681eca8f1f0410e1e9cd9dec6a09201 | 74ff2243773f2a38f438b84f4376cf745406a3c17bca7381155b55ce763b1dc3 |
| evidence/executions/20261012/haar-feedback/policy-tests/receipt.json | 2867 | d190f9e3bb905316372f13fe19b8edff24a0be40 | 5315d6a375390e903f3d6465d86e2b1f0f3a560155fff0931bd328fe1028b7e8 |
| evidence/executions/20261012/haar-feedback/preceding-ci/computation-failure.log | 100967 | 475ca1626304039f73a039940984f4125c87aa44 | d322037d9ffccd88cfe8773e9d3e3cdfd6c54c68b4698a41f74efb54a295bfc2 |
| evidence/executions/20261012/haar-feedback/preceding-ci/formalization-success.log | 32538 | 1eab51effe71ec5a67dec2b67028221705021efe | 7544d655723c0c6f009aba39ed118d33fad89d5cf963c987d4e12cea565a399a |
| evidence/executions/20261012/haar-feedback/preceding-typesetting-v2/manuscript-build.json | 14753 | f89f137cdff82fb5ba00100d00ab23586ed3fc91 | 5517657e62c68d256a2f1f64efc421c4e8f9dce37e6183dfccbeaa51aa236088 |
| evidence/executions/20261012/haar-feedback/preceding-typesetting-v2/manuscript-parse.json | 604 | 5049eada30798e11518bcf392dcc29c0bbc94088 | ac3a52461bcbd19f508b2bf40826ff56b1e916de1bf08367c5a0e9cad7be7236 |
| evidence/executions/20261012/haar-feedback/preceding-typesetting-v2/manuscript-visual-review.json | 787 | 833c1b29ec559ee48b598b5707a04c143d55ba9f | dc3d5faa7340548fc2979ed440836465a85b1a2f3062384136ed6861ab956976 |
| evidence/executions/20261012/haar-feedback/preceding_commit_ci_failure.json | 2178 | d1f0cc66efdfc7d90dfa9654e85f6b7110baebde | 002bfb5483e1e64a8ae4a18db8d685cfa4352122d5795a6a49d0ffe36afffc4a |
| evidence/executions/20261012/haar-feedback/review.json | 1882 | 39eb78af97aa65a63ed0d8ccd69c57de0a8a835c | 0bfe6d3d22623e10ec3aa9d44482e886ccd3bcc6287b9a91f644aaeaecf250b6 |
| evidence/executions/20261012/haar-feedback/static-checks/01.log | 318 | e16f4e764a10b2acf393d13f9f2b297470e9c4b5 | 197d1403b25a79462793357cd5700c87217b146eb72d193c7bf74f810018461c |
| evidence/executions/20261012/haar-feedback/static-checks/02.log | 69 | c1efc1228f7000245d9d63a5172f1675c9b1366f | 3e7922491d521bc82ed897b6868f1898977946a2da88be3d66fc4991779ae9f3 |
| evidence/executions/20261012/haar-feedback/static-checks/03.log | 75 | 1d60f362bf91f51aa9bb3e42c2dedb19f834ee24 | f8dc620e3f91255fe0fcf917ddbe7240cf94f13366d26abe29c56e34b2326d5e |
| evidence/executions/20261012/haar-feedback/static-checks/04.log | 26 | a2dfebaeff71155f36e4eaf9e9dfc71a9fd8875a | ca57b079e313b85e314f167b8b2784cc10aadcdf7ec672b35a78d9065ad3dc5a |
| evidence/executions/20261012/haar-feedback/static-checks/05.log | 18 | bdf754c73628b6b0c7a00c21af9008cf98ffdc64 | 4c0cee0495ac114569d0dc29c4b2d2ffec590d0b532696fa296de85e50e96efc |
| evidence/executions/20261012/haar-feedback/static-checks/06.log | 39 | fc41337527dc984f493c11ada3559672a03c42e1 | 510e138fd96540afbb7dcaca2b463e0490b0757a525d36a49838e0868273f776 |
| evidence/executions/20261012/haar-feedback/static-checks/07.log | 38 | f118ecd5e272b875a63d29d37cdd6591d2cfe962 | 539493b621d37764da4373e4ce51f17f00bc1c365d1e6eee2c560c2a35fe4f25 |
| evidence/executions/20261012/haar-feedback/static-checks/08.log | 59 | cfab2a06c3684fd44ec6e27fb53b7c7f19f7c901 | 8681480c083c449f330b3b20bf3bf2ee681cc806b313c474dd583c1f888529d0 |
| evidence/executions/20261012/haar-feedback/static-checks/09.log | 243 | 2b0ea6e66b65ff58d14e282cb389fcdcdcf0b132 | e0a66be66204a1d284f72c05401bef6974ded06e82cfdae997b5786dec39ffa9 |
| evidence/executions/20261012/haar-feedback/static-checks/10.log | 67 | aeb8cf9a639916db0e9526035a72b5d0cc99f3e7 | 7dff7e6b1c5539ccc5797b5eb3a0ae844ca66753e8eef40a208024fbc6f688f6 |
| evidence/executions/20261012/haar-feedback/static-checks/11.log | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/static-checks/receipt.json | 5051 | 717118152c11758e69932883ef414b2f2c25c61b | 51c3038fad7f102b60d2421afa09c7b36e3080f3dabdc22c0be6d7f17fa92964 |
| evidence/executions/20261012/haar-feedback/static-checks-v2/01.log | 318 | e16f4e764a10b2acf393d13f9f2b297470e9c4b5 | 197d1403b25a79462793357cd5700c87217b146eb72d193c7bf74f810018461c |
| evidence/executions/20261012/haar-feedback/static-checks-v2/02.log | 69 | c1efc1228f7000245d9d63a5172f1675c9b1366f | 3e7922491d521bc82ed897b6868f1898977946a2da88be3d66fc4991779ae9f3 |
| evidence/executions/20261012/haar-feedback/static-checks-v2/03.log | 980 | 9579985114220a9db632a348a1afc0b712427be9 | f74217414ce9194ff8e12e1d092c98ffc5c819488d5b137e48d5abe35aa43d7f |
| evidence/executions/20261012/haar-feedback/static-checks-v2/04.log | 26 | a2dfebaeff71155f36e4eaf9e9dfc71a9fd8875a | ca57b079e313b85e314f167b8b2784cc10aadcdf7ec672b35a78d9065ad3dc5a |
| evidence/executions/20261012/haar-feedback/static-checks-v2/05.log | 18 | bdf754c73628b6b0c7a00c21af9008cf98ffdc64 | 4c0cee0495ac114569d0dc29c4b2d2ffec590d0b532696fa296de85e50e96efc |
| evidence/executions/20261012/haar-feedback/static-checks-v2/06.log | 39 | fc41337527dc984f493c11ada3559672a03c42e1 | 510e138fd96540afbb7dcaca2b463e0490b0757a525d36a49838e0868273f776 |
| evidence/executions/20261012/haar-feedback/static-checks-v2/07.log | 38 | f118ecd5e272b875a63d29d37cdd6591d2cfe962 | 539493b621d37764da4373e4ce51f17f00bc1c365d1e6eee2c560c2a35fe4f25 |
| evidence/executions/20261012/haar-feedback/static-checks-v2/08.log | 59 | cfab2a06c3684fd44ec6e27fb53b7c7f19f7c901 | 8681480c083c449f330b3b20bf3bf2ee681cc806b313c474dd583c1f888529d0 |
| evidence/executions/20261012/haar-feedback/static-checks-v2/09.log | 243 | 2b0ea6e66b65ff58d14e282cb389fcdcdcf0b132 | e0a66be66204a1d284f72c05401bef6974ded06e82cfdae997b5786dec39ffa9 |
| evidence/executions/20261012/haar-feedback/static-checks-v2/10.log | 67 | aeb8cf9a639916db0e9526035a72b5d0cc99f3e7 | 7dff7e6b1c5539ccc5797b5eb3a0ae844ca66753e8eef40a208024fbc6f688f6 |
| evidence/executions/20261012/haar-feedback/static-checks-v2/11.log | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/haar-feedback/static-checks-v2/receipt.json | 5214 | 78c7de170e60c1e0cf9af9f093666dc90cfae76c | 8495da876d78b1532a02756416ec98e539ccdd2b3a54d5131cefef7492d3eddf |
| evidence/executions/20261012/haar-feedback/typesetting-failure-v1/BGS_unified.log | 42343 | 98dc6a630d8677f5437945f304e4355170be1c2a | ba1091a9de905f5a05703296de020207ba26b76250b1d596d2726758ea727676 |
| evidence/executions/20261012/haar-feedback/typesetting-failure-v1/build_manifest.json | 14510 | a1b272237743365d80d8b1853d4250659ef01ecd | 5e1dc486861cb1c47f2ffb2301314454d23d36946d85435b7ea7d00050f104ef |
| evidence/executions/20261012/haar-feedback/typesetting-failure-v1/pass-1.log | 38801 | 44510737c213db8d16938c73cc1119f74a1370f1 | 463cfeb668acc1af8d0188602b079d51017d1ea5618d1c9c0aea559dad4d47db |
| evidence/executions/20261012/haar-feedback/typesetting-failure-v1/pass-2.log | 19136 | c87f477c56de1c4f7d19d75e6264ecd9e2bd9ac1 | 2fdba9317e3743dadaf1411f31b0462fa9dd1795a3c0e740542ef8cf2db51415 |
| evidence/executions/20261012/haar-feedback/typesetting-failure-v1/pass-3.log | 19054 | 8ba56c38b128e88b6e86573458e54f3462d7cdec | 8f320f6c3765bf5b9d3d2ecffac1c5df3e41681e0adff5ca067beb539a1eb518 |
| evidence/executions/20261012/haar-feedback/typesetting_failure.json | 681 | 4194ab174c7795a385aff1d092cd493ffd9ecc9a | 2479df50a0578001035a2d725240ab6da7cba42ec2554dada534d8c682732350 |
| evidence/executions/20261012/haar-feedback/wolfram_result.json | 500 | e71bc839b81231855b06f1fa4f62cdecc43e0c3c | 92d3c94fb27ba84418af6d2421919c8f9e7179922cd7c9030e7e1a8789d12076 |
| evidence/executions/20261012/two-step-drift/README.md | 2880 | 122288f7a6bfb77188bde89cc294d8ed1e89b830 | accb44fcc675bc6e08e4846c68065c48d283bcc383f78e30dbb95cf0c7cc04f7 |
| evidence/executions/20261012/two-step-drift/finite-controls/manifest.json | 5915 | dec3ffc991cbba1857336156490c0a0865193e9b | 587e884b8bf9f7c6803389448f795f26ad43d3862c5f22c22a5b82cb63801161 |
| evidence/executions/20261012/two-step-drift/finite-controls/results.json | 1321 | b92e0837d7ccdb93425d3dd0ad22d8489609605e | 62a7143adb43d03ed218a4b4b534b15dd57568a6c7bd9a2299644745efa2a40a |
| evidence/executions/20261012/two-step-drift/finite-controls/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/two-step-drift/finite-controls/stdout.txt | 1321 | b92e0837d7ccdb93425d3dd0ad22d8489609605e | 62a7143adb43d03ed218a4b4b534b15dd57568a6c7bd9a2299644745efa2a40a |
| evidence/executions/20261012/two-step-drift/inputs/two_step_drift_review_input.md | 3289 | 7d08746ac98bd7b8004b552a800ab2fcf8b28619 | ef9bc8eb3c0c2c09f6d1d571dd87f73f94090f6047ab5e788ef78dcaece180dc |
| evidence/executions/20261012/two-step-drift/local-regression/clock_reference_measure.log | 1155 | 5791316d907512dfba893700dc0edf69ea6df613 | c1996aaeb86c4b560afb1c473c3c5ed5af63ffd8c2fe4124aa608667bcfffdb8 |
| evidence/executions/20261012/two-step-drift/local-regression/entry-policy.log | 1336 | 1ba6b5de46e3264a2527cdafb6582fd50a7d0935 | 8d056d2b065ad254f090d492b12dd6fb6fe7222655c7638ba0451459b3ee9603 |
| evidence/executions/20261012/two-step-drift/local-regression/receipt.json | 3190 | 2a8e3e6a3a7db7cd9b8831c06c95ec36ef99df72 | 3651b10c251734a7c1b47de2912d62c7e3a7465d66079f9fa1288dec2b86a79f |
| evidence/executions/20261012/two-step-drift/local-regression/two_step_restoring_drift.log | 1321 | b92e0837d7ccdb93425d3dd0ad22d8489609605e | 62a7143adb43d03ed218a4b4b534b15dd57568a6c7bd9a2299644745efa2a40a |
| evidence/executions/20261012/two-step-drift/local-regression/unitary_two_step_obstruction.log | 3008 | c97194743ee902771ecc02c123ed1804c225ffce | e0aa4e1a97e72d3fa2c82063ce1459d32d16111bdb3af36546fc564d9d5b9d10 |
| evidence/executions/20261012/two-step-drift/maintained_transfer_review.json | 649 | e739023bd7178784919c3d6dad18983a553703f4 | c4810299f155bbf924350fa1f07d4f0068d23a7d376f854823a2fd0ebf223fba |
| evidence/executions/20261012/two-step-drift/manuscript-build.json | 14792 | 53bbf1243ed2c2e29f8a23c4385a87ded0705c9f | 01ca5db9e73327dbe7a0ab5ef6e405c663d21f026fb164722c5a5a9c87295ccb |
| evidence/executions/20261012/two-step-drift/manuscript-initial-build.json | 14531 | 1f8bb5ec046447f7fb26567bf4e95a29962ecef3 | 996250bd186141ad9e6e05097c5ac76d2f86abf2866a54451917537b9f9b5334 |
| evidence/executions/20261012/two-step-drift/manuscript-postbuild-artifact-failure.json | 15629 | 072ba69581f3483b6c89fb1bdfe7795ad63bf065 | 971f05261345c8ff45960cd7eedd285ea26851e5c72b8348c4db0adba5d985f4 |
| evidence/executions/20261012/two-step-drift/manuscript-second-build.json | 14549 | 164775986fc542794981e68e19726dbc726083ef | f338fdc7bbd960e767f0ac70313349effe67e52dc912d4ef812920364607661c |
| evidence/executions/20261012/two-step-drift/manuscript-visual-review.json | 1111 | 32af3426e97eecac3c92e7a8e50219e1033783e8 | 21e83c2afee931213b24a9c97334b56d1f30cfde7bd790572b5830cb96f212c1 |
| evidence/executions/20261012/two-step-drift/preceding-ci/computation.log | 108863 | 9e02da2d2555288e041c36df90841ac86e71e31e | fb4f03180e8c040712139b68bd24abde2ec3964f431f96578510c22a5361c733 |
| evidence/executions/20261012/two-step-drift/preceding-ci/formalization.log | 32540 | 0ec81be18f37b3929353d787089d0fef23b11011 | 7a6e2ed0fb825b35fbbbd444ae9634361d54ac6e449ba96dae94302a1925e182 |
| evidence/executions/20261012/two-step-drift/preceding_commit_ci.json | 2033 | 25d18e2ad3195865826da628b8c98255aab2881e | ea25edae53c73863c4679b6861a484b317f9a312125fae2d0f672aa1452f09d9 |
| evidence/executions/20261012/two-step-drift/review.json | 1263 | d9057e00ead467d18cfa48e0386b6b97d9f9abfd | 417b77f5d6523b075a5d936f1cc0fb0218fc5c887db31ee27edeb8619406baf9 |
| evidence/executions/20261012/unitary-two-step/README.md | 2131 | 3061ab21852b4abe9a53b77fb37b1c5124c44b37 | 0ecdff2218c93e71b5257b4d94f05d927e56e0179c844ba2345fd451d258d8c6 |
| evidence/executions/20261012/unitary-two-step/finite-controls/manifest.json | 5878 | a083ee8c7574593e798e6b2c9dccf69b1efcc5c9 | 09cc530c77353671b2daf29f3442c2ee9a18066e8b62e6cd5dbd9fbff07351e7 |
| evidence/executions/20261012/unitary-two-step/finite-controls/results.json | 3008 | c97194743ee902771ecc02c123ed1804c225ffce | e0aa4e1a97e72d3fa2c82063ce1459d32d16111bdb3af36546fc564d9d5b9d10 |
| evidence/executions/20261012/unitary-two-step/finite-controls/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/unitary-two-step/finite-controls/stdout.txt | 3008 | c97194743ee902771ecc02c123ed1804c225ffce | e0aa4e1a97e72d3fa2c82063ce1459d32d16111bdb3af36546fc564d9d5b9d10 |
| evidence/executions/20261012/unitary-two-step/initial_control_disposition.json | 658 | ed5b3616fa58036111fc9417c26ac6e6c316fada | f16c217a8faa54e41e57140ddad2bf5d805d672138306b1d0e5be881cdcccd3e |
| evidence/executions/20261012/unitary-two-step/inputs/initial_timed_out_stdout.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261012/unitary-two-step/inputs/initial_timed_out_verifier.py | 4069 | 81af051e81d66f38dc3a19ff84b780dc2cc01752 | a64d956ac42301b17f50038813a326054685613f3cb5d0915ab83b57c1eca0e8 |
| evidence/executions/20261012/unitary-two-step/inputs/unitary_obstruction_review_input.md | 4123 | f8646ce37567a116114abe970395e2e0bc070921 | c0b024469d84b91ae92e74b4d04b15cf259c9f11d55b2071d5422562da45a5f1 |
| evidence/executions/20261012/unitary-two-step/maintained_transfer_review.json | 721 | a40c0dfd9b617077aeaf27005f7d3442d39b0c21 | 5ad99edd77bac8d4fb0bbfb7b36ca8445b920516540badccdc7d3b9b5b7add42 |
| evidence/executions/20261012/unitary-two-step/review.json | 1314 | 5bdc312e2611a96b5424b8622d1728d0c4451fce | 903283a0c7f644e6fc1cde4e7073b7415c941a32125018579c274b2d9970869d |
| evidence/executions/20261013/global-feedback-flatness/README.md | 4970 | b040b7dc53fc0ecc9eb59466f1a9b47ad673a3a1 | c3b831132348bd00801a7fd4134de87668d6289ff44045a8023b09ff03e95c8b |
| evidence/executions/20261013/global-feedback-flatness/bounded/manifest.json | 5773 | f370a3f3f7400b8f9b7948ccb0441f907b18c70d | 070acbcffe4a4b41e22e71d2b7546b0e8507af1d6e1af236bc176a2f5685793d |
| evidence/executions/20261013/global-feedback-flatness/bounded/result.json | 2482 | 149dff77c3f6b003e539bf14bd114d765d89138e | a679e78ea3e943f478475ba8cf40571180b99d19d51303f2fd6232995b8fdcc8 |
| evidence/executions/20261013/global-feedback-flatness/bounded/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261013/global-feedback-flatness/bounded/stdout.txt | 2482 | 149dff77c3f6b003e539bf14bd114d765d89138e | a679e78ea3e943f478475ba8cf40571180b99d19d51303f2fd6232995b8fdcc8 |
| evidence/executions/20261013/global-feedback-flatness/candidate_reviewed.md | 12553 | 75cd0154b3237e92629c17451e85ebf6538b0380 | 1264e43e74652b814fef953def70eb64702e287eb06e2dd3d7d0f86ee41b2d1c |
| evidence/executions/20261013/global-feedback-flatness/independent_control_source.py | 12414 | 665ee9ff14cf457fdda3426ec53f2dcc9fad7314 | c107c417faa44b0d605227e63abbf67ac507766ddc2de01038dba6a63f6f6bcd |
| evidence/executions/20261013/global-feedback-flatness/independent_controls.json | 10429 | 88b0102589a49c7a89cdb4ef2971daf1af3b4e39 | f0e53281e9094eace6209ab48ad229a18df73ad8332739b468ea63fd0f8ce8b3 |
| evidence/executions/20261013/global-feedback-flatness/independent_review.md | 28772 | a4dd1fb4c5abec894ca99d97e580784cedebb621 | 52467495bd3dcac810198ebabf3380f8ba2bdc6eb37cf4764d3576575dd96122 |
| evidence/executions/20261013/global-feedback-flatness/logs/bibliographic_metadata_audit.log | 924 | 19ef9c68cb6271b3658ed133e056539138eafc12 | dccdcc0abba14d534b54ee176733212080930d7249d38d097340c916fb6fde42 |
| evidence/executions/20261013/global-feedback-flatness/logs/feedback_row_energy.log | 2482 | 149dff77c3f6b003e539bf14bd114d765d89138e | a679e78ea3e943f478475ba8cf40571180b99d19d51303f2fd6232995b8fdcc8 |
| evidence/executions/20261013/global-feedback-flatness/logs/green_compression.log | 1142 | 573706aa43203b7da6836d88b05ff6ca3ff2de31 | a40d6386c08f04dc203306d8f8cfc42e7c06bcf3088a5490558d1c4c558cf8b9 |
| evidence/executions/20261013/global-feedback-flatness/logs/repository_audit.log | 318 | e16f4e764a10b2acf393d13f9f2b297470e9c4b5 | 197d1403b25a79462793357cd5700c87217b146eb72d193c7bf74f810018461c |
| evidence/executions/20261013/global-feedback-flatness/logs/scientific_registry_audit.log | 69 | 578d0fd842d3316516c60425c7fc44cb03b26517 | 75fb7441c1a56c6cf24cf4e8d84e26e20ac194eb170475bf7b38c07a32e8440e |
| evidence/executions/20261013/global-feedback-flatness/logs/stopped_two_step_concentration.log | 1318 | d3693973772a478dc860e8e77dded0c0bacefd6d | 1cd4c8986e908e8c02009bf84f6bca07286e5d47aab03a9016bd480dc135a055 |
| evidence/executions/20261013/global-feedback-flatness/logs/two_step_increment_variance.log | 1848 | 0b786f2dbb0327064b78bdb1d3145464445b6425 | 1382aeb4de702519a485c10ab9728631394e217d30d2093c1b6c648fd26e4b17 |
| evidence/executions/20261013/global-feedback-flatness/logs/two_step_restoring_drift.log | 1321 | b92e0837d7ccdb93425d3dd0ad22d8489609605e | 62a7143adb43d03ed218a4b4b534b15dd57568a6c7bd9a2299644745efa2a40a |
| evidence/executions/20261013/global-feedback-flatness/maintenance_full.log | 35051 | be17858e175d551286c77df72742acb14b7df5f8 | d5bc7efcd5275ed5223a8dd23a6cded33289247bd3d4f5abf4f0eb7d5d177779 |
| evidence/executions/20261013/global-feedback-flatness/manuscript_build_manifest.json | 14792 | e9b4ea559f0ecdc22e9a399fddf9f74e9613c731 | 78ba7b5af367f0c6cf7088fd0dc3d72cef6362c84daa06074abda8c6e2e938e4 |
| evidence/executions/20261013/global-feedback-flatness/manuscript_pass1.log | 38306 | bc082addea48a4b8af20eadce0c05fcf63aee47e | 90998d1bbfbe224dc01819a4b888f54bcb0c41a3bea154922ce3e2e9653609c3 |
| evidence/executions/20261013/global-feedback-flatness/manuscript_pass2.log | 15774 | 7f6b1b522a0d1843be1d11b3a03bab34ed4f2e7d | f427b9c00d79ebec5d1228d5fe0b4117abfa736b65989d35b10e73700aa07f6a |
| evidence/executions/20261013/global-feedback-flatness/manuscript_pass3.log | 18623 | b97e555ff7606df5c141bc07d60c19f923b23747 | 4e58d41fd4aa467cd918729b9f33ca35e16a4eaba40699d381d27858c948ddc3 |
| evidence/executions/20261013/global-feedback-flatness/preceding_ci_run.json | 12207 | 7064dcdf0edf9f23a6908f3f18dda22b85da722b | 51b70a08190473d70536c025fb8f2faa891a0e274eb09aad2e0c35dc02f614c2 |
| evidence/executions/20261013/global-feedback-flatness/preceding_computation.log | 109271 | 9532e617e950b1d414da6d8567e2d7a19650c05b | 7c6b8cf3501bf313f2243a2d198ed6027827c319f949f5709b030a044cfda641 |
| evidence/executions/20261013/global-feedback-flatness/preceding_formalization.log | 32545 | 38e1b7c376a6c8f8d3c7dc6a2c264583856b6c1b | 615ff0e525c623475180b0549f87998596da85ff2ce4b4eb95c8d58cf8c157f8 |
| evidence/executions/20261013/global-feedback-flatness/root_controls.json | 2454 | b31f19e7ede285beceb6c342b49310b7fda3540f | ac462bddaa0ebdc67c8e938b0b29488d99151afba6ba54beb81a7e1d6c88121e |
| evidence/executions/20261013/global-feedback-flatness/root_controls.log | 2454 | b31f19e7ede285beceb6c342b49310b7fda3540f | ac462bddaa0ebdc67c8e938b0b29488d99151afba6ba54beb81a7e1d6c88121e |
| evidence/executions/20261013/global-feedback-flatness/root_executed_source.py | 5089 | 85bf65955f9658397124a5937d733612e826ad57 | def07462dd18361a7167a0e5049be6ff01cca844791be6c8ba29a9c3b8bb6c1c |
| evidence/executions/20261013/global-feedback-flatness/root_failed_fixture.log | 746 | 1e3b88a271c9b29de61c06430ae5838c7252d888 | b03e4ef984e20492015ea401cfe7d4af520adbb10de1cab85e05009368230441 |
| evidence/executions/20261013/global-feedback-flatness/source_manifest.json | 3559 | 79b1d5711c5b8bd990e68135f1e14616f3d5e688 | 6072124566af4ef5443a15644757f716bac05a17cbd366667f90d8c14d7b16a9 |
| evidence/executions/20261013/global-feedback-flatness/transfer_review.md | 5888 | 5762479d7d5f73ed1ca7f5db677866a04d3c89ee | 3a2201b981589d74c8775efcbb83865afe2b9c7a2ae6d89d0bb8b8fffe9c7212 |
| evidence/executions/20261013/global-feedback-flatness/workspace.json | 754501 | bbdf07f2cdbf08867ac48e57a835f11f0cc0c11e | 89479a6f26abcd8fad0dc04c0017a99aa8fa82cf666558398ba4b4076fbf28b6 |
| evidence/executions/20261013/green-compression/README.md | 3130 | 66fc6571a6fbb93d92c542a28f75c4ed396a4ce5 | 0038ced0043be1daa101c821aae0f058b9dcc295692a80b8ccd044eb8fd1b39c |
| evidence/executions/20261013/green-compression/candidate_reviewed.md | 7345 | b81fea2e398fb42b3d3616dfeb7d005e5b268ec8 | 4ca12a1de53fd141ab0ff60cf36644ae7bd985a6e0c4e957bbf4c6bcd0a4d8d8 |
| evidence/executions/20261013/green-compression/controls.json | 1142 | 573706aa43203b7da6836d88b05ff6ca3ff2de31 | a40d6386c08f04dc203306d8f8cfc42e7c06bcf3088a5490558d1c4c558cf8b9 |
| evidence/executions/20261013/green-compression/independent_review.md | 31800 | 5a3b0ee3fdc95ce62c29bf235b0263135c2e3a3d | ea00ace98859aa7df92ffcb0bce080721dcf89f5775f1b5cb6fef9c5150c4b37 |
| evidence/executions/20261013/green-compression/manuscript_build_manifest.json | 14771 | 90f573c6ec6271e748bb4788a12c6673da72a120 | 7244078ca30493e2a648b3687797659ed02451ad4b8eebdbf692c355626211b6 |
| evidence/executions/20261013/green-compression/manuscript_pass-1.log | 38267 | fa346666ff5facd9844bd2281ed45a04966e8140 | 8ea77568497356e65dbcaf68c093db327bb31b59b58d04a432f32ae916d8231d |
| evidence/executions/20261013/green-compression/manuscript_pass-2.log | 18639 | 661c6ff35f0187245adf28e900ed14cb339c9ec9 | e557f0582a6a329b53a3533d0df3e4f252234284f690b2ae164575daf96833f2 |
| evidence/executions/20261013/green-compression/manuscript_pass-3.log | 18557 | 82fbe95a87d9ef12819639f8129cd3d60b842bb0 | efea843968df9b35d029442945316cb41ad506a81de7f070720fbd273db53b40 |
| evidence/executions/20261013/green-compression/preceding_ci_run.json | 12193 | 61b2c9baae16a71a1eb310856a6efba43090fd45 | 892bc58825268686eeba6d7870982485aa13bc13a8b890cc9cecdf34a207242e |
| evidence/executions/20261013/green-compression/preceding_computation.log | 109025 | b2e07289dd53e9d98756b7ee299c529e8ce6377a | d3d0f4d15bd208bd9f38d6df9652321bcb3a2a8e3c33c4ee0c8c6c52997a5e2d |
| evidence/executions/20261013/green-compression/preceding_formalization.log | 32538 | e905f989813c3863575e7b41751bb25ff4ba4612 | 3f76a52a5965512567134d00c493b6b5c49abcad6b524bf7712e481f89d8a746 |
| evidence/executions/20261013/green-compression/source_manifest.json | 3462 | 46986b020ae3ecbf15ac4203ad1572da18c55d8c | a4f51f1ae426e38f4ba5c3168eea2e40e87c5bd9692538ea7f7a26b5081b9f09 |
| evidence/executions/20261013/green-compression/transfer_review.md | 6955 | f407fef5ba9983990c369eb91e2a0433528edcc4 | 1364162b8fdf382e52ed0bebddefef07f1284bc4facbea287e207018c1fa2a3f |
| evidence/executions/20261013/green-compression/workspace-logs/bibliographic_metadata_audit.log | 924 | 19ef9c68cb6271b3658ed133e056539138eafc12 | dccdcc0abba14d534b54ee176733212080930d7249d38d097340c916fb6fde42 |
| evidence/executions/20261013/green-compression/workspace-logs/green_compression.log | 1142 | 573706aa43203b7da6836d88b05ff6ca3ff2de31 | a40d6386c08f04dc203306d8f8cfc42e7c06bcf3088a5490558d1c4c558cf8b9 |
| evidence/executions/20261013/green-compression/workspace-logs/repository_audit.log | 318 | e16f4e764a10b2acf393d13f9f2b297470e9c4b5 | 197d1403b25a79462793357cd5700c87217b146eb72d193c7bf74f810018461c |
| evidence/executions/20261013/green-compression/workspace-logs/scientific_registry_audit.log | 69 | 2fbed31865e5f85fca7869a9a3b2878d8987d3b6 | 3876fd5362e50ef44e728d491df2e4340036d68be64ad1dc63113671f9513691 |
| evidence/executions/20261013/green-compression/workspace-logs/two_step_restoring_drift.log | 1321 | b92e0837d7ccdb93425d3dd0ad22d8489609605e | 62a7143adb43d03ed218a4b4b534b15dd57568a6c7bd9a2299644745efa2a40a |
| evidence/executions/20261013/green-compression/workspace-logs/unitary_two_step_obstruction.log | 3008 | c97194743ee902771ecc02c123ed1804c225ffce | e0aa4e1a97e72d3fa2c82063ce1459d32d16111bdb3af36546fc564d9d5b9d10 |
| evidence/executions/20261013/green-compression/workspace.json | 736471 | 42af4112be7c0eac93deff801074e4aef991f01b | 351826f4df3447f5603f5c22ed8d5659dd64bf645059925ffced604f92383514 |
| evidence/executions/20261013/stopped-concentration/README.md | 2735 | 1aba74273662c2117194ba68f72b8dbe44628f04 | c449f4d9a59f9b2e0cbfb9a0a9556fc6d1c1b1e19c5cce648584387e3cf25c1d |
| evidence/executions/20261013/stopped-concentration/bounded/manifest.json | 5779 | 9f22e14ec26da8752be20304fea8a89998ad82e7 | a66e58f2d553aec53abe28eefe51ed3c326de3b2c1ce13a39a46e81548cd76f6 |
| evidence/executions/20261013/stopped-concentration/bounded/result.json | 1318 | d3693973772a478dc860e8e77dded0c0bacefd6d | 1cd4c8986e908e8c02009bf84f6bca07286e5d47aab03a9016bd480dc135a055 |
| evidence/executions/20261013/stopped-concentration/bounded/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261013/stopped-concentration/bounded/stdout.txt | 1318 | d3693973772a478dc860e8e77dded0c0bacefd6d | 1cd4c8986e908e8c02009bf84f6bca07286e5d47aab03a9016bd480dc135a055 |
| evidence/executions/20261013/stopped-concentration/candidate_reviewed.md | 10170 | 41bc29fc762f96bbb89821fe6ccedf7b1d91dfc9 | 47e365b06fa460e6d503b771b9b336403ee9a6e918e81d4a17b6c6be9a60aec7 |
| evidence/executions/20261013/stopped-concentration/independent_control_source.py | 8353 | 087c0ab701206d3e15623fb911455b7380e86647 | eea97f1ce168dbdc57480da91937e205e425f0268779629657634684ea24007a |
| evidence/executions/20261013/stopped-concentration/independent_controls.json | 4267 | 57ee7346437139139eefe46dff72bb5fd674a8f0 | 7668e98955b8e65d7aeabaa99b029174cd50afd6c65e765d046b290ff3044cc8 |
| evidence/executions/20261013/stopped-concentration/independent_review.md | 23218 | 4bceddc81577f1030110461e715248b734748cc3 | ac08090b2bd4d2dec0aaf81e9c367ba363b3e632428ef8a7494f6c5d52475e95 |
| evidence/executions/20261013/stopped-concentration/root_controls.json | 1290 | fc81688bb5ce4c9f6e09d6fdcc8ff8f3697de7ff | 01d43b1264458c1948415cb29eb01d0bea6ddb2a05d3591e95d3078ef2bf8766 |
| evidence/executions/20261013/stopped-concentration/root_controls.log | 1290 | fc81688bb5ce4c9f6e09d6fdcc8ff8f3697de7ff | 01d43b1264458c1948415cb29eb01d0bea6ddb2a05d3591e95d3078ef2bf8766 |
| evidence/executions/20261013/stopped-concentration/root_executed_source.py | 3988 | e81611fb0dfab1fd2d47d4a5797a879259988705 | 380daa53c2ccb4af390b87eaac6b117e5a3d85d46ed2aed7310eb5a74bf4428b |
| evidence/executions/20261013/stopped-concentration/source_manifest.json | 1723 | 76498a5123df92b279961c25710b29be9b4f0862 | ee6db26671eb5c7205b87f2192d903de431003ed2d236a5af5a4c3115c97af90 |
| evidence/executions/20261013/stopped-concentration/transfer_review.md | 3971 | f1903e16b716bc22a2107790b1d9491aa200b792 | 3712c630755f86852d035130e22808797136948f895ed3ead555c38ba83ad1a7 |
| evidence/executions/20261013/two-step-variance/README.md | 3098 | adf3b5c53fcaca50ae5668b665479f34370d745b | 3ecf69e77a9cb5645443edd90b5b9e615dd1e6a0b926d7ea45f153b2b301f492 |
| evidence/executions/20261013/two-step-variance/assertion_entry_policy.log | 1336 | 3590baae8898cd8407489076dc9b8804e6c7473e | 3a46a099a43b2ea611322238304e243064ff69f8876de52f58d33c29440a6591 |
| evidence/executions/20261013/two-step-variance/candidate_reviewed.md | 3611 | 8e788304786145a02cb4872433fafce1314a458f | a9dc3382474c53e0d01db3cc81719f573b7638b5760b0d54ba5699a57ca140c4 |
| evidence/executions/20261013/two-step-variance/controls.json | 1820 | 3e27e7e82f23c9e74d3e91a523407a44a57ddedc | c680b927f954aacf8ed137f2365956902181e3c30c8a95855c16fce0d86d9aea |
| evidence/executions/20261013/two-step-variance/executed_control_source.py | 2944 | 6258e75d912947e2a8abbdd36d153178f9af1300 | 69eaff7deaaae69be2fc818ab819f9c80c882ecbf34f4eb496b06b3abecae734 |
| evidence/executions/20261013/two-step-variance/independent_review.md | 15527 | ec348097238a8d3c209eda806eba133ac6fb3338 | be9e33eebb0ee3c92f373e380354a9bfecf70ea220fff01ef4b165290a4c40b3 |
| evidence/executions/20261013/two-step-variance/maintained_transfer.json | 353 | 31aa9a15e1d1c6d79dc106974fad01846a6adb22 | c8d9b3a9b68df149a2e8c57c334326d9117fce3f5e62879060b98a7b692f3feb |
| evidence/executions/20261013/two-step-variance/maintenance_full.log | 35050 | c614e0ef9f956b6e9f3bed1e3cd21eb5bac92f6a | f83114032343e0bbd62f84345740a62afaa80b4f426e01705b09365226881e97 |
| evidence/executions/20261013/two-step-variance/manuscript_build_manifest.json | 14780 | ee04be2dd3ea108ceb4af8251fd2b66dd10778b5 | eb941f852cd04274baa96c6e84602d80901fa4963f0dcd2ed5156f0ec63c4743 |
| evidence/executions/20261013/two-step-variance/manuscript_failed_pass-1.log | 35959 | 4bb3665f82dc4855d6c66d0441a6659a1f8467a5 | d9a63a4031c1f6515edb8698c639e1be1d6fa6300303dcbcab95b9e213ca0c37 |
| evidence/executions/20261013/two-step-variance/manuscript_pass-1.log | 30473 | b20f239bddb5a861c08ebca83eb92092649c02c8 | a72d2b3bf0a45893da79c2e1eb51f3dce7545bd9758c26186a4ed1c845619346 |
| evidence/executions/20261013/two-step-variance/manuscript_pass-2.log | 18665 | c7fe9a7cb4f64ba9498f7f18d1511c7062be6f79 | b02e46c11790fc0c5a95a2dd3346ebb2440eb116de50c5e840e2bf0c2ecc2b24 |
| evidence/executions/20261013/two-step-variance/manuscript_pass-3.log | 18583 | d0cea1d75cb9344581653f9f4a15a6cd30a72d27 | bf3ce94aaa8012a52c1e1035f5b420c6d77bec5dc24fa24f7aaf4c5da4dcefc9 |
| evidence/executions/20261013/two-step-variance/preceding_green_ci_failure.log | 108793 | c2b1db7979a5224154984497b7200dcb91802f38 | b0c9caf1f56a69d64072373ecea0dff5884a218e3d434c168e3b4dd2342be143 |
| evidence/executions/20261013/two-step-variance/source_manifest.json | 3948 | db3e45261f5c0fb7d54d051653fda7285e0b3cbd | d0fd7ff17ff7b6e94fd64e4394b8bf63550dfb6cda8d289ff23e115ce609d796 |
| evidence/executions/20261013/two-step-variance/workspace-logs/bibliographic_metadata_audit.log | 924 | 19ef9c68cb6271b3658ed133e056539138eafc12 | dccdcc0abba14d534b54ee176733212080930d7249d38d097340c916fb6fde42 |
| evidence/executions/20261013/two-step-variance/workspace-logs/green_compression.log | 1142 | 573706aa43203b7da6836d88b05ff6ca3ff2de31 | a40d6386c08f04dc203306d8f8cfc42e7c06bcf3088a5490558d1c4c558cf8b9 |
| evidence/executions/20261013/two-step-variance/workspace-logs/repository_audit.log | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261013/two-step-variance/workspace-logs/scientific_registry_audit.log | 69 | a3eef3868550369dcbd5c626a4d6adf30d4c0947 | 5511fc71b50bdb6bc379e0b8646f796f0c850818eedfb50e02236473ec716263 |
| evidence/executions/20261013/two-step-variance/workspace-logs/two_step_increment_variance.log | 1848 | 0b786f2dbb0327064b78bdb1d3145464445b6425 | 1382aeb4de702519a485c10ab9728631394e217d30d2093c1b6c648fd26e4b17 |
| evidence/executions/20261013/two-step-variance/workspace-logs/two_step_restoring_drift.log | 1321 | b92e0837d7ccdb93425d3dd0ad22d8489609605e | 62a7143adb43d03ed218a4b4b534b15dd57568a6c7bd9a2299644745efa2a40a |
| evidence/executions/20261013/two-step-variance/workspace.json | 740409 | 120f719ae9ca478cf3103c14507022beecadb721 | 78cec50cf13539d70f10c6317f7e64f41d630fa63f706938a24e7fc0f631dd88 |
| evidence/executions/20261014/first-return/README.md | 3997 | a10d4fac23e1dd738cc831585ce6fc4f33da8981 | ad494689467d2e3d62f76c84b937d66352f7602504ce6404f8e34d3aaa83c820 |
| evidence/executions/20261014/first-return/candidate_reviewed.md | 9693 | bbb8fc78e5405ada148fadbe52da9d95eaff0096 | c79a75933760de94f73f610c79af0e9c6a5f7bb59bbd78828a5df398fe1d9a7c |
| evidence/executions/20261014/first-return/ci_observation.json | 4347 | 374cee6e78dd2939bd12347104c8a5dd51ad3e70 | 217f3d0f6515547e6d85ac35e63602a2b7eadcad9f85685298d7cf6e6e54fa30 |
| evidence/executions/20261014/first-return/controls.mjs | 2337 | d0742f934d366fea1956bd17457290b26b08f61f | 6fe9cea0dcd6ff77c94713fa450dae7530fa87540c27d22d3e539dd5ee5f633c |
| evidence/executions/20261014/first-return/controls_result.json | 615 | 54d67235168d1c30100eded1c8c14e72ad149463 | 41e50d7c2e459cb0424c76002227674f425405ec788fde1bb912d19f441c5a51 |
| evidence/executions/20261014/first-return/independent_controls.mjs | 6556 | d1aa12b62f8aef9d97bf1892090f6c616722e6c2 | d2219c7f5a2680188d783ccd92c2206f8ad7791dc790af08195982199e8b9b62 |
| evidence/executions/20261014/first-return/independent_controls_result.json | 5429 | b944717e2e05db63aba952418d84e8cae47e33f2 | 258f2fd565ec1013fd21667e368087869682f1e4f25a2726fcc4349ffa638eb5 |
| evidence/executions/20261014/first-return/independent_review.md | 27479 | 6f3cc3b4ede6e36cfc53c7bb2b65e3a2340a8164 | 8720ecfd31e2f4a2a0e78df29a15fd82c923012d3d718989293f1df4c556cb19 |
| evidence/executions/20261014/first-return/source_check_scope.json | 676 | 318464d297f2942f8d613d3dabeec6d48825ef87 | 8e9da03a3f0ae420a452d1e0eb60214385e12d26917aefa90443b37a5af616c8 |
| evidence/executions/20261014/first-return/survival_controls.mjs | 2515 | e0fab1ad0ec7e0fc36f492268af408585788801f | 0a1b053824b776673982972fdde4bef6f0f882615336e2a26b0d1863b3faf124 |
| evidence/executions/20261014/first-return/survival_result.json | 685 | 87f03cbd6524ebf9ac1dfa2892802ceb20f4c6ef | 82d48c1241acbd2e5e6938c68cc269538fe587535f673d9b59ad8ee4938bdddf |
| evidence/executions/20261014/first-return/transfer_receipt.json | 1466 | 401a91c50104523ab624c123e07cd9c0d1059f2a | 11f9cef389cff79368a66d903d51afedab1eb043e79782910d27d0eabe4dbd2a |
| evidence/executions/20261014/first-return/wolfram_controls.wl | 1079 | 712d31f2c4aade0cf8a0ddcfe25ff19cfa531d8d | 347bf590e7aae065b649ce2e2ec65c7952740fff254f8d384be44cef7183c988 |
| evidence/executions/20261014/first-return/wolfram_result.json | 663 | 4c2c2e0a27f47773b61a927a87dee044f95574e6 | b9c10d8c3dec5bd3e97243c27282963bae8f134ac2fffcd844e27d5fbc6e7e6b |
| evidence/executions/20261014/spectrum-coherence/README.md | 5439 | ed115e182a32f13240889961e3cf0ae9e631a167 | abb898278aed66ae17a6e03df46162b8f65efe5655bf6ea12e009b21ef5e14ac |
| evidence/executions/20261014/spectrum-coherence/archived_js_result.json | 12571 | 766829a73bd9cdd604f271459381df1ecef4887d | e8e0403afaa03970c803d51b9162230ea7ca9cfe725e8099fd49bba941b25dd1 |
| evidence/executions/20261014/spectrum-coherence/archived_js_source.mjs | 3388 | 81220c5349e744d0981a7f5b96de563ba27124cd | 4b7aec7bee16305afb391854f620eacf02d0533af29f9d2874e3223f914201e9 |
| evidence/executions/20261014/spectrum-coherence/bounded/manifest.json | 6163 | e751c9db3041afdf4299d03906edd8b5bfd37c00 | c3e576e69ca8f997b77b1fa73af4584ded014003bf79ee1c4f0d8c480db45c2c |
| evidence/executions/20261014/spectrum-coherence/bounded/result.json | 5867 | ec9f79df563140a13cf8c265bfc1279edee1376a | bcf4a4af268d2f5729eb784305c0a3371d2bac57d75672663f9823158fded3d2 |
| evidence/executions/20261014/spectrum-coherence/bounded/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261014/spectrum-coherence/bounded/stdout.txt | 5867 | ec9f79df563140a13cf8c265bfc1279edee1376a | bcf4a4af268d2f5729eb784305c0a3371d2bac57d75672663f9823158fded3d2 |
| evidence/executions/20261014/spectrum-coherence/candidate_reviewed.md | 14450 | 666e8a9ab551e945936198638ebb4d4286a67454 | 08de07484be6e6a8fb2612ac9abbbb12ecdeb6660c23b3cb57ba158de62c1030 |
| evidence/executions/20261014/spectrum-coherence/focused_logs/bibliographic_metadata_audit.log | 924 | 19ef9c68cb6271b3658ed133e056539138eafc12 | dccdcc0abba14d534b54ee176733212080930d7249d38d097340c916fb6fde42 |
| evidence/executions/20261014/spectrum-coherence/focused_logs/cpp_coherence_memory_verifier.log | 217 | 90b94ac03c90563489f35725c8d99c3a4f77ba0a | 86c4e3afc2f7a81d7102469a8c05f7794d5558fa9b31b4b8e1531011ccdaad0e |
| evidence/executions/20261014/spectrum-coherence/focused_logs/repository_audit.log | 318 | e16f4e764a10b2acf393d13f9f2b297470e9c4b5 | 197d1403b25a79462793357cd5700c87217b146eb72d193c7bf74f810018461c |
| evidence/executions/20261014/spectrum-coherence/focused_logs/scientific_registry_audit.log | 69 | 433321cde570c63921eacd0fb4dde472bb83e2aa | 785b676dc5b0e45fee27c5217df855178c1af116a1223c626bd6fe0b0f747519 |
| evidence/executions/20261014/spectrum-coherence/focused_logs/spectrum_coherence_controls.log | 5867 | ec9f79df563140a13cf8c265bfc1279edee1376a | bcf4a4af268d2f5729eb784305c0a3371d2bac57d75672663f9823158fded3d2 |
| evidence/executions/20261014/spectrum-coherence/focused_workspace.json | 757083 | fd7000d0619aa86b5946ec32fd6b2510dc358ca6 | 35988108961c63c38ce26b3b242915d669e7adb484d49344496f5e89a32f2765 |
| evidence/executions/20261014/spectrum-coherence/independent_memory_controls.json | 5043 | 5fb5d66b21e7daa79d9419a49a46ec0ef7a93a25 | d43f47d01435246a9bf172512cd80023307746eb6be21304217a69a0d0a35c85 |
| evidence/executions/20261014/spectrum-coherence/independent_memory_controls.py | 10082 | 4ee02e2731beb5eb1c3b16e4b85c55db0087698e | 97f83543efbdf2cf10002e0821aff11edbf8f55abee67aa6097b5bdf1d296e12 |
| evidence/executions/20261014/spectrum-coherence/independent_memory_review.md | 19703 | 6d6e96fb66cb2af1a45666ba69428d93bd956a3a | ea0416ff94dc03fc18295cbf44b74370dc44ac3eaaf5c72a2b0c6c6b6d253063 |
| evidence/executions/20261014/spectrum-coherence/independent_spectrum_controls.json | 27419 | c6167b12c426456e13ebde12d853cb5c6a3a2b69 | 2f01be30eec2fbad43b96aeb2e745f01e4272e0ebcdc8bae0feecd41a1b923e8 |
| evidence/executions/20261014/spectrum-coherence/independent_spectrum_controls.py | 10315 | 0b2af9cd427ee6ea9e075dd5fad754b1506deaf6 | fe63c99ad591207dd29a307642579b90f0544c25669cf0759323547bd4679327 |
| evidence/executions/20261014/spectrum-coherence/independent_spectrum_review.md | 34865 | 08faf01afbd6a4ff8a36fe9c7e29458039c892eb | 1b0fca70d10031c01f78117c14840b2a48b305c87de46d0b5ee52b3fd6ed804c |
| evidence/executions/20261014/spectrum-coherence/maintained_transfer_review.md | 12269 | 883f2906970b19cc07b370f51bcf4f0f8a47af4c | fab06d97d01742c62a378d7d692adc6d8e7c0e6ea92f69c1a7a503f027a15103 |
| evidence/executions/20261014/spectrum-coherence/maintenance_full.log | 35051 | dba6a742ce334c663de06c68d7ed79af83b7c574 | be7789d58a0a9ad63e180b719715b56fb5d41d6e78610dc0050ee4766d25bb74 |
| evidence/executions/20261014/spectrum-coherence/manuscript_build_manifest.json | 14783 | 1ef7a13d8428ed15fec9241438a9aeb82a316e8e | 63f3502a4ffce12a0f8136034dd8b1711b2ee0b751bef9ec47552bd9641531e8 |
| evidence/executions/20261014/spectrum-coherence/manuscript_pass1.log | 34484 | b22686164632a9549ba4dd48e5781d80f2457d59 | 212bd472f1de9d51ad032442199bdce78c94af1e55a0c2c420df3bf4a5477350 |
| evidence/executions/20261014/spectrum-coherence/manuscript_pass2.log | 18928 | 0eafe5ad5d5e303b188b5c32d72768b0822b9b87 | e83710193a2277b37bd084e2910d71f4da86c01059b79e2877d93c2a42eab914 |
| evidence/executions/20261014/spectrum-coherence/manuscript_pass3.log | 18846 | a5a8f4262423cb04a727b2c97de5717576832f72 | b5d0190a31af23a07393d63dea3df1528b3cb37617b54e7e7f5dfddf57a813e8 |
| evidence/executions/20261014/spectrum-coherence/manuscript_visual_review.json | 840 | ec19ce3ed9502f33ca43cc3886784860ee14f40c | 2b72e5662a15e257eb3ebcdff3e0610808ad571d66f03d3f48cb4a2f200103fd |
| evidence/executions/20261014/spectrum-coherence/memory_candidate_reviewed.md | 3615 | 61268c845f5782dd2c04947240dcf043feefe642 | b7b90c31b51f5cca32c1ef189d064f6896fcb38a232a740e8dccc05b995afb09 |
| evidence/executions/20261014/spectrum-coherence/memory_corrected_reviewed.md | 4861 | 9cfcbeb8be245fa727ab4b79cc3718f82305c03d | 39cc445b963d4b8a3fa6868a66a0300be48b661791ea34c3c9ad7c3d240cd1a0 |
| evidence/executions/20261014/spectrum-coherence/preceding_ci_summary.json | 1506 | 45edf1ae7836d09e8e8cf5a190ff95af62a22ebf | 54284475f78dfa289e2967772c32fab947930370493da301026642ea2b3d19ac |
| evidence/executions/20261014/spectrum-coherence/root_cpp_receipt.json | 709 | 441a11e98ad680f2f7e3343fe5971d22692e593c | 23d06b3b3195362499afc14b40c85894b59b8324ae0d94465a3ea46906ddf709 |
| evidence/executions/20261014/spectrum-coherence/root_cpp_result.json | 217 | 90b94ac03c90563489f35725c8d99c3a4f77ba0a | 86c4e3afc2f7a81d7102469a8c05f7794d5558fa9b31b4b8e1531011ccdaad0e |
| evidence/executions/20261014/spectrum-coherence/source_manifest.json | 4492 | caaff2b92a2786e8fe7e8bdd8a7decc0f557a992 | 25e5f6c89f510402c65f38baf3aff45db02fbd0c439db7494c2dcbee12c2e4b5 |
| evidence/executions/20261019/repository-integration/base_objects.json | 669240 | fdc3d8c8b107a9e6e6c6fca53afcfdbe03467ccf | 4148c1fe920f59160abea11f3b7dc5d80e3c234d1f5166b191ce167665edaba3 |
| evidence/executions/20261019/repository-integration/check_run/manifest.json | 10131 | a8d4617f2b2f266eb31a61ef2a3c3ef891568279 | e9dc4314cf36589bc2208338f33503c905f932d2135108990ad5119994418576 |
| evidence/executions/20261019/repository-integration/check_run/result.json | 1570 | ea2a077185e7b2e59ced0a1415a494b9083ceece | 4b20878594937e424c5975c36adfaac646dab0ec0e19b8da69704566f92683bf |
| evidence/executions/20261019/repository-integration/check_run/stderr.txt | 0 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| evidence/executions/20261019/repository-integration/check_run/stdout.txt | 200 | c296186da0d6e862a2d71d84179acf104ce77a7f | 6303e2186b26ba4d243dd9ed4150cdb429a4ebbfed4aceb96854378b33d5c77a |
| evidence/executions/20261019/repository-integration/diff_review.json | 2557 | 33c137f2eba6b726f7297e7e965763e37ce183bc | 7f4a881df0f3082f26b2e75be0b3fb1bedc510ed4d4ac23e297f38174b8601b3 |
| evidence/executions/20261019/repository-integration/manuscript_build_accepted.json | 15099 | 5c2a8e0e9bb936c4b67e717727c9ad2c0cbb827f | 2c9aaab2c845ab3ce14d83595338ab6df530c63412609bbadd25584895920218 |
| evidence/executions/20261019/repository-integration/manuscript_build_accepted_pass-1.log | 39597 | ebb3d91b87f5f3d7cd9a7430c506cb061cf240ba | 9bcb4c3924b2ba872e58893b4d0906a2c6bc5f4fec44651806b57d073ca1e28d |
| evidence/executions/20261019/repository-integration/manuscript_build_accepted_pass-2.log | 18933 | e787905d83cad0396b2982d392058d8dbed92268 | 31fc70600593abf1ec664bc278d6e85fe1132a9198a496277f0076a8e7e4d684 |
| evidence/executions/20261019/repository-integration/manuscript_build_accepted_pass-3.log | 18852 | 6e2317694f5697b2596f06796333a84bdb5b7b49 | 0eaebfd81c4f44863c04641205b94beaf8ded5191578bb9117ea64d6169e65f4 |
| evidence/executions/20261019/repository-integration/manuscript_build_failed.json | 14856 | 1e2ce9418a4da4b9cc0d4cd98c1d0adb5aeb4203 | 6e8a565d765d29dc5cbdd7c8fabf4defbbf3c868a9179e02268534c77aa044a6 |
| evidence/executions/20261019/repository-integration/manuscript_build_failed_pass-1.log | 39850 | 6da3ae99837a04ef2489aa41f1eae727952cb865 | 3ed9f5020ed037327e0a1c57ec529e2a6e1f38bcd29b9f70c9712c1204098a1f |
| evidence/executions/20261019/repository-integration/manuscript_build_failed_pass-2.log | 19173 | f06902ea699457c303e9f99f7af9e631f28306f9 | afb95f41bd84eb37f35b8cae0d201b6113c459b5905364a712d77f666ebf1d20 |
| evidence/executions/20261019/repository-integration/manuscript_build_failed_pass-3.log | 19091 | 9adf9c1b210cb707d651fd3ae093659e9f96bec3 | 7717a116aa776dd85ed8078e422f4b1320f76a209bea5ee1dbc7f8b3d7e6b6dd |
| evidence/executions/20261019/repository-integration/pdf_qa.json | 857 | 179efff80c157560ab0817a864900dc99bbecd84 | 716a7c85554c52b0ae0b5e83bf741ce86d26766bdb0f0102d203971a5d673e63 |
| evidence/executions/20261019/repository-integration/postpublication_check.json | 1570 | ea2a077185e7b2e59ced0a1415a494b9083ceece | 4b20878594937e424c5975c36adfaac646dab0ec0e19b8da69704566f92683bf |
| evidence/executions/20261019/repository-integration/publication_c49e351.json | 5041 | e0b29bdedaac2c89cb80700a9f7ffac0998d5922 | 03333943c80583f69ec25b9effe9cec70bc6ef3e7dff7cab87268243a18fd934 |
| evidence/executions/20261019/repository-integration/source_revisions.json | 1739 | a94a93c7c8c5dbde5601afea949c7db0723d0186 | 8c4f1bccf1c782a31eb64034e3ed136f1726bd455eb0d72a4bd708c418e8980f |
| evidence/executions/20261020/repository-reconciliation/README.md | 3550 | d27faf339fe24f939f095e35709fa6f1f2098e1b | 0ce1acd528d38d6e81286a176e8e9d8ebaa3324267a55426ab159bbf9dc38a67 |
| evidence/executions/20261020/repository-reconciliation/archive_members.json | 97858 | a6b03c233b9facb33240ae9870be66e8eb7fc405 | a5270ca297203e595cd050afb50700c68d6c0900c4f3903298e2bfa03119768a |
| evidence/executions/20261020/repository-reconciliation/baseline_integrity.json | 902 | 687ec95a360adcf8b301306913a7a7549929c1ae | 2c1282c3782083dbe9a0b01bf6447ac9379bfd2267f1730ff309e0ab242bab52 |
| evidence/executions/20261020/repository-reconciliation/checked_source_delta.json | 12764 | 87057ec79aa483976610aa1805c6ef1034279f02 | ad5ddb8729e2dd883eb600089c3d507b8ec053bad0c3843b4c8c46b6daef3a74 |
| evidence/executions/20261020/repository-reconciliation/consistency_gates.json | 5088 | 7dfd0a026718ad1021baf11bf62d7c0280e3a836 | 6e76b55455031ae82e889eab348756536f154e662dfd0ff23d1f4e91f74ad81b |
| evidence/executions/20261020/repository-reconciliation/cpp_compile.json | 11741 | 966af837418334aac36fdfed922300efc906da4f | 15a1ce8df5798a96daadf84135d38d5004a97f5e009af7bad300fbfcd7a3d63b |
| evidence/executions/20261020/repository-reconciliation/final_consistency.json | 5431 | 0b847d0dc11f56d12c2c4d87c423bdefd79826cd | 131f1d840997cc3b4b9dfdee67d0c3f24d6b1eef35cc7b6dac0253008a6c9e75 |
| evidence/executions/20261020/repository-reconciliation/final_gate_logs.json | 3339 | 5de0448b2750268bcf48f7cc6da91e8c3d0a8e18 | c21b9f5a75f888d1f7f244598a17ddedb96894663c573d185645d5d5f9435a7a |
| evidence/executions/20261020/repository-reconciliation/integrity.json | 2449 | 4c23a0a4ba99ca724776ca679fb8dc34094b6c1f | 01be851491cba0b9665fcfa5a92f5d1933af83f46b56368f0500f8b9a7ad14c6 |
| evidence/executions/20261020/repository-reconciliation/interrupted_proposal_manifest.json | 22437 | 044637210dae6c6a3960509bb24359ddb14ed5ac | 3e9bbf7dc5652b25dae84d57583e2eaaceb2cd31c7f0686d5a51690dfaacf285 |
| evidence/executions/20261020/repository-reconciliation/manuscript_build.json | 15141 | 2ca4b41ed706d985d5251e6f4bd9d543a65af832 | ae4b6bf4f9e13aef8f3efc72a6c571e1c044904895d80476ea3b9bb17f599cb2 |
| evidence/executions/20261020/repository-reconciliation/manuscript_references.json | 243 | bb1c5cace30b8f506a9bfdd32936b59ec6564504 | c4dd77d7a6351608096747d23ddf89881f70d4e9e0d727f664429f5b855606f5 |
| evidence/executions/20261020/repository-reconciliation/pdf_qa.json | 982 | e4495b75836f1e59efca9a13bcbe08ff8ce14222 | b467cde8b3bedf40717cc0e241b5e4356ec222debae1396381fc0c8686655049 |
| evidence/executions/20261020/repository-reconciliation/pdfinfo.txt | 888 | 6e1bb66828f4448a448ff055cddabbad8f20d704 | b47e0db3c39a11c29a00f378361ace8f8ee68f549215ba8f4d8b5c3f6913dcab |
| evidence/executions/20261020/repository-reconciliation/receipt.json | 3058 | 0639789e76ac8b8144d77f0d8f5582a33d42c3d9 | 387096e743b7d4fb010b1294ac828319781cbd36049077119ddf81f63fafd4ac |
| evidence/executions/20261020/repository-reconciliation/selected_checks.json | 6947 | 4873a007f19ec3669ecf0bdeb2d5495607cad2e4 | 144b167899131e8fb2bb607beb8c96cc16de6548655c42b66f915d2b51fce8b2 |
| evidence/executions/20261020/repository-reconciliation/semantic_preservation.json | 214 | 823a58c5d479e1f4b06989a790e9e237682895e9 | 043a75d335360d8193d6ad7d025b47ab357eaa4aadb0fa96a6589cfdce3c82a5 |
| evidence/executions/20261020/repository-reconciliation/source_manifest.json | 882927 | f93cbfcc7163f6fb1fc2bb6178a02e988872bb77 | 7c04b874a966be6b51dfe2f1863053bcbb01c6217ab3f32fa55743cdb5348473 |
| evidence/executions/20261020/repository-reconciliation/tests.log | 35541 | 6766951a67468d7ea83f3139c9500f79b77bbe72 | 5cbdaa770c1c59d288ee8cf066f3642e026bc68a924de7e2dd0e30f9c97d5a4f |
| evidence/executions/20261020/repository-reconciliation/workspace_command.json | 9010 | 9d805438c05dbefa91702fd522af02219a635d9a | 056acf6de0d6c0aa09c3be1893af6e9083250e29ccc1f13b5c9719edd0f71f7d |
| evidence/executions/20261020/toolchain-followup/README.md | 2723 | a7e50a5ba2d054c098a465b7847482e4f1ac2dcd | a74cc775dbbc79cac29959809ff14607185399631cacb655d8a118996a2690d0 |
| evidence/executions/20261020/toolchain-followup/boost_bootstrap.log | 1823 | 0cdc4c904d1820c1401e6034f9f2de086396c29b | c4627348347dba12cfbfc0f7ae5e7da4422f5624ca182d022e7e662d291c0bbd |
| evidence/executions/20261020/toolchain-followup/boost_install_excerpt.log | 10056 | c2c8e0f4e7d7108ac2c4ea099b3b534750733a52 | 5fb3d1ceed58db2854bbe7da93f5ebe0560ac9454849d90ded5e081a3999b833 |
| evidence/executions/20261020/toolchain-followup/cmake329_configure.log | 1116 | 7fd31f9d95da225fb967b0b06a2c38158b3f026e | d1b4a90552ce3b51f71f6b4ef8719d521c37ddb09623f6f20222f43f25d42024 |
| evidence/executions/20261020/toolchain-followup/cmake_configure.log | 935 | d500edb9a1c068521499d8ab31e22a48b769b460 | 173d0a635761d93ede5d94884444d18880a01ae53b90f13af09490fb2df67eec |
| evidence/executions/20261020/toolchain-followup/cpp_build.log | 5746 | 26347c148a424dec6b216a2b93198b51b76c7e0b | 438625d52ee77c019fd7fadc714d98bfd14158ab3aa8965607833450217d2a02 |
| evidence/executions/20261020/toolchain-followup/lean_build.log | 14811 | 93b7fbc20f08c0c61700a91b2213160114aed7e2 | d03b50ffdaf2fbdaa043edc366d1f76a7b0032c9e9416a2521a314ec52f93070 |
| evidence/executions/20261020/toolchain-followup/lean_build_stdout.log | 14873 | d1af75673b3ab778669c309a6ef6d1f91a5a6742 | 78857959f28cdb58d1390cee8b37cc992aab350a663c8ced2ec290717c244e10 |
| evidence/executions/20261020/toolchain-followup/lean_native.log | 67 | d0f276a3566ef35e4a35f16be5f98c39fd0c949b | dfce1e7d6849bcb01696e698fae3345a66f15495d7e36f99ac1293476a5bd045 |
| evidence/executions/20261020/toolchain-followup/receipt.json | 5131 | 863bdb9654af10d3fd857d88c6c5103f7cddd4d4 | 38620de836b727168cb99d83805bbeff710901df1f19d019a496b49b46f5dd32 |
| evidence/executions/20261020/toolchain-followup/verified_sources.json | 14573 | 95cecf12d46dff9bae7004e349e8422c814a5672 | 1a18740b1ed9ee31d2a5d2bf553de15b2ef6dacb3c38c8640f903bd9935ec674 |
