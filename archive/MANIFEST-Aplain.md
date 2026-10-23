# MANIFEST — package A-plain (phase 1)

Archival relocation of the "plain" class of package A: dated evidence trees whose only live coupling was the claim registry, `evidence/index.json`, and document navigation. Every file below was copied byte-for-byte from `evidence/<path>` to `archive/evidence/<path>`; the originals are removed by the follow-up deletion commits of the same package. Blob SHA = git blob id of the file content (identical for the original and the archival copy; verified for all 639 files).

Base state: main after package F-2 (archive commit 03c19c1) and the F-2 deletions; registry at 197 claims.

Same-commit migrations carried by this package (not file moves):
- `record/claims.json`: 74 path values (all `evidence[]`) for 37 claims migrated `evidence/...` -> `archive/evidence/...`; no status, state, source or other field changed.
- Epoch registration (standing recipe): 19 new `historical_claim_amendments` rows (BGS-FLOW-003..010, BGS-FM-006, BGS-FM-007, BGS-FM-009, BGS-FM-012, BGS-FM-014, BGS-FM-015, BGS-FUP-001, BGS-RES-004, BGS-RES-005, BGS-TRACE-009, BGS-TRACE-010) and 18 extended rows (BGS-FLOW-011, BGS-FLOW-021, BGS-FM-005, BGS-FM-008, BGS-FM-010, BGS-FM-013, BGS-FM-016, BGS-FM-018, BGS-FM-019, BGS-FM-020, BGS-FM-024, BGS-LOOP-001, BGS-TRACE-011, BGS-TRACE-012, BGS-TRACE-013, BGS-TRACE-018, BGS-TRACE-019, BGS-TRACE-020); the `approved` literal in `computations/verification/wave2_integration_audit.py` grows 42 -> 61 by exactly the 19 new IDs; this manifest is the `review` record of every new and extended row.
- `evidence/index.json`: 13 values migrated (the 11 dated-packet prefixes of class `dated-research-packets` and the 2 `recovery_*` legacy paths of class `executions`).
- Navigation: 9 link targets in 8 live documents migrated (URL targets only; link text and prose unchanged). One further link, in `supplement/fixed_map/resolvent-flow/loop_test_reductions.md` -> `evidence/loop_reductions_20261006/provenance.json`, was deliberately NOT migrated: that document is a hash-pinned input of the live fixed-map supplement inventory, and pinned inputs are not edited; the link resolves through this manifest.
- Rider: `record/wave2_checked_integration_20261007.md` — one relative link retargeted from the F-1-archived `wave2_inherited_replay_compatibility.json` to `../archive/record/wave2_inherited_replay_compatibility.json`, restoring the final link stage of `wave2_integration_audit.run()` (pre-existing F-1 casualty, unrelated to the trees moved here).
- Not in this package: the one `external_dependencies.json` project_sources value pointing into package A targets `evidence/research_checkpoint_20261007/...` (class A-complex) and is left untouched for that sub-package. Classes A-data (579 files) and A-complex (550 files) stay in place. The 12 historical path records inside `record/schur_replay_freshness_repair_receipt.json` are a frozen provenance record (no live consumer reads it) and resolve through this manifest.

## Composition by tree

| Tree | Files | Bytes |
|---|---:|---:|
| evidence/20260922 | 6 | 26703 |
| evidence/20260923 | 3 | 7984 |
| evidence/20260924 | 6 | 30026 |
| evidence/20260927 | 4 | 21270 |
| evidence/20260928 | 2 | 7427 |
| evidence/20260929 | 7 | 32573 |
| evidence/20260930 | 13 | 167764 |
| evidence/20261001 | 5 | 45870 |
| evidence/20261004 | 14 | 115851 |
| evidence/20261005 | 6 | 22518 |
| evidence/20261006 | 6 | 14777 |
| evidence/actual_commutant_20261006 | 25 | 72946 |
| evidence/cayley_inverse_pair_sum_factorization_20260905.txt | 1 | 3416 |
| evidence/cayley_psc_transversality_20260905.txt | 1 | 2064 |
| evidence/cayley_trace_intercept_rigidity_20260905.txt | 1 | 3015 |
| evidence/checked_checkpoint_acceptance_20261007 | 49 | 1725579 |
| evidence/collective_20261006 | 7 | 58365 |
| evidence/combined_wave3_v4_acceptance_20261007 | 48 | 2559738 |
| evidence/factorial_diagonal_20261007 | 6 | 55509 |
| evidence/first_seven_20261006 | 35 | 29086 |
| evidence/fm008_fresh_audit_20261006 | 2 | 5971 |
| evidence/hamming_ci_repair_acceptance_20261007 | 40 | 2722678 |
| evidence/loop_reductions_20261006 | 16 | 53581 |
| evidence/ordered_diagonal_20261006 | 3 | 8620 |
| evidence/paired_phase_20261006 | 15 | 74258 |
| evidence/r6_repair_checkpoint_20261007 | 197 | 3672500 |
| evidence/ramified_first_seven_20261006 | 11 | 41762 |
| evidence/ramified_higher_20261006 | 25 | 97916 |
| evidence/recovery_20260920 | 6 | 21631 |
| evidence/recovery_20260921 | 1 | 2303 |
| evidence/research_checkpoint_protocol_20261007 | 33 | 532401 |
| evidence/schur_replay_freshness_20261007 | 35 | 191799 |
| evidence/weighted_support_20261006 | 10 | 63828 |
| **Total** | **639** | **12491729** |

## Files

### evidence/20260922 -> archive/evidence/20260922

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20260922/finite_orbit_cpp.json | archive/evidence/20260922/finite_orbit_cpp.json | db9a12b157b3f715ca020e1c104827c0d41e629c | 323 |
| evidence/20260922/finite_orbit_exact.json | archive/evidence/20260922/finite_orbit_exact.json | 120dfeab39b4c0e9d2888ba7d48b0fad7fe3619e | 22377 |
| evidence/20260922/installer_tests.txt | archive/evidence/20260922/installer_tests.txt | 5dc82d76f60db22b68ecc8a0f26e5ec102e20ded | 585 |
| evidence/20260922/run_manifest.json | archive/evidence/20260922/run_manifest.json | b0ecd8775e7f483a36137744ff45a5b24d8b8471 | 2657 |
| evidence/20260922/tex_sync.txt | archive/evidence/20260922/tex_sync.txt | cfab2a06c3684fd44ec6e27fb53b7c7f19f7c901 | 59 |
| evidence/20260922/wolfram_output.txt | archive/evidence/20260922/wolfram_output.txt | 7a368f9bb9102a9cb38e00dcea04d584e14ba1f2 | 702 |

### evidence/20260923 -> archive/evidence/20260923

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20260923/frozen_full_lag_gap.json | archive/evidence/20260923/frozen_full_lag_gap.json | 86e7f15304f34d16b407ddad9b0be195d2a1bf20 | 361 |
| evidence/20260923/frozen_kick_rank.json | archive/evidence/20260923/frozen_kick_rank.json | bf9cdeb9438bc864bd70be8bdfbb7c3bcd84777c | 7051 |
| evidence/20260923/nonlinear_pressure_variance.json | archive/evidence/20260923/nonlinear_pressure_variance.json | 42f02b89f68a76f3c893868812c049d1bc12410c | 572 |

### evidence/20260924 -> archive/evidence/20260924

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20260924/antireversor/certificate_polynomial.csv | archive/evidence/20260924/antireversor/certificate_polynomial.csv | 8b745d4757b2b5f0c76ba0ee91dc44d8fca32b84 | 24033 |
| evidence/20260924/antireversor/certificate_polynomial_7.csv | archive/evidence/20260924/antireversor/certificate_polynomial_7.csv | cba9b19a0f7cff5259a69d22ecec0c8c85420d1b | 1182 |
| evidence/20260924/antireversor/certificate_result.json | archive/evidence/20260924/antireversor/certificate_result.json | 2b94c35e8fc84b6e55a998d97e97749dbb80a846 | 2314 |
| evidence/20260924/frozen_arithmetic_traces.json | archive/evidence/20260924/frozen_arithmetic_traces.json | 0f4bcdb4c350c8f664dfe5832efcc039f609e738 | 742 |
| evidence/20260924/frozen_seven_cut.json | archive/evidence/20260924/frozen_seven_cut.json | b34d5d6602d965ef25ee62ce6bf1137a290c5abd | 1253 |
| evidence/20260924/frozen_total_minors.json | archive/evidence/20260924/frozen_total_minors.json | e68d9e3f478d068f5b50adf21839462400cd7cc0 | 502 |

### evidence/20260927 -> archive/evidence/20260927

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20260927/cue_original_suite.log | archive/evidence/20260927/cue_original_suite.log | 1bcf39159b2c1cd9e6aa44e63cc3defe597fde95 | 1835 |
| evidence/20260927/cue_upload_audit.json | archive/evidence/20260927/cue_upload_audit.json | d466caa336303bb6ebda055a7b6fda12c4565947 | 4272 |
| evidence/20260927/cue_upload_manifest.json | archive/evidence/20260927/cue_upload_manifest.json | 69307afae79e5bd6a93d545d48c6345f593b9fde | 13840 |
| evidence/20260927/integration_checks.json | archive/evidence/20260927/integration_checks.json | f9c6f75c9a18ed60d1c38b1c1bd773b0143c3a9b | 1323 |

### evidence/20260928 -> archive/evidence/20260928

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20260928/quadratic_coboundary_noise.json | archive/evidence/20260928/quadratic_coboundary_noise.json | 7d660e474f263cf57e43998a5062843b1da01ce4 | 5654 |
| evidence/20260928/quadratic_noise_manifest.json | archive/evidence/20260928/quadratic_noise_manifest.json | 80ac3859614f8078dc599bafbac8dc726f92e61b | 1773 |

### evidence/20260929 -> archive/evidence/20260929

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20260929/coboundary_mobius_diffusion.json | archive/evidence/20260929/coboundary_mobius_diffusion.json | c323f0c0617235b52d76fadf544e4fff9ce78894 | 2226 |
| evidence/20260929/coboundary_mobius_integration.json | archive/evidence/20260929/coboundary_mobius_integration.json | 8909ecda1c49f3aa085712356d1ddc85dfe5ffd9 | 11887 |
| evidence/20260929/coboundary_mobius_manifest.json | archive/evidence/20260929/coboundary_mobius_manifest.json | c3d132d39413eb15a0018b5cf709476aef77a710 | 1275 |
| evidence/20260929/quadratic_noise_clock.json | archive/evidence/20260929/quadratic_noise_clock.json | 834306090a6d441466f5c68e3e50ce2b02983aab | 1466 |
| evidence/20260929/quadratic_noise_dynamics.json | archive/evidence/20260929/quadratic_noise_dynamics.json | 80de7643173207020f6c8217bb9205ef4a2e0b67 | 1484 |
| evidence/20260929/quadratic_noise_integration.json | archive/evidence/20260929/quadratic_noise_integration.json | 338fd2f5b1a3febfb8da90b352cf8092af64fb0c | 12063 |
| evidence/20260929/quadratic_noise_manifest.json | archive/evidence/20260929/quadratic_noise_manifest.json | e3c8df5554aaae6df60facdf606cf8ab1185e1c6 | 2172 |

### evidence/20260930 -> archive/evidence/20260930

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20260930/coboundary_joint_integration.json | archive/evidence/20260930/coboundary_joint_integration.json | 64f7561fe2e826754198e80bd5701379eb06c05e | 2507 |
| evidence/20260930/coboundary_joint_limit.json | archive/evidence/20260930/coboundary_joint_limit.json | d7798f5917ecf83172f1ae7c4e82352f3f3f2ea0 | 7558 |
| evidence/20260930/coboundary_joint_manifest.json | archive/evidence/20260930/coboundary_joint_manifest.json | 59287e246f2333c21a1bf15ff7142d33c3e9517a | 2144 |
| evidence/20260930/coboundary_mobius_rerun.json | archive/evidence/20260930/coboundary_mobius_rerun.json | c323f0c0617235b52d76fadf544e4fff9ce78894 | 2226 |
| evidence/20260930/heisenberg_note_checks.json | archive/evidence/20260930/heisenberg_note_checks.json | f5471764d6cf31593aa47a5ad6f45ddfa6554464 | 13160 |
| evidence/20260930/heisenberg_note_execution.json | archive/evidence/20260930/heisenberg_note_execution.json | 692c654c660fcf4be8be2be77703ea5da75c6243 | 16681 |
| evidence/20260930/heisenberg_note_manifest.json | archive/evidence/20260930/heisenberg_note_manifest.json | f9d2a958d32b1ab39b7e06a56504e3cbba8ee115 | 2296 |
| evidence/20260930/prime_resonant_checks.json | archive/evidence/20260930/prime_resonant_checks.json | ed2632642852c0d8c77718b3eec7b803b71e48bb | 76932 |
| evidence/20260930/prime_resonant_execution.json | archive/evidence/20260930/prime_resonant_execution.json | 2009716d5b9877666cfa3bbcc59e80443f8005ea | 19021 |
| evidence/20260930/prime_resonant_manifest.json | archive/evidence/20260930/prime_resonant_manifest.json | aa58e1a69c3befe4e218b00afc98e5cf23afa841 | 2289 |
| evidence/20260930/signed_heisenberg_checks.json | archive/evidence/20260930/signed_heisenberg_checks.json | 4dd1b607fcb4365b224203dfdeee146b2fc39be2 | 19666 |
| evidence/20260930/signed_heisenberg_manifest.json | archive/evidence/20260930/signed_heisenberg_manifest.json | ffcfbffaf495705d94a1e73a9ae274b3954ab179 | 2431 |
| evidence/20260930/signed_heisenberg_wolfram.json | archive/evidence/20260930/signed_heisenberg_wolfram.json | f7c3c470df0b686c68f04bfcdc8bf2451585b15c | 853 |

### evidence/20261001 -> archive/evidence/20261001

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20261001/folded_quadratic_checks.json | archive/evidence/20261001/folded_quadratic_checks.json | ed8ed675af5b43302ba4468bc51d87b6c4ef79db | 19256 |
| evidence/20261001/folded_quadratic_wolfram.json | archive/evidence/20261001/folded_quadratic_wolfram.json | 03295b1d07f50c2ed120c29eccdb38bc85055a97 | 1519 |
| evidence/20261001/resonant_density_checks.json | archive/evidence/20261001/resonant_density_checks.json | 2e629f68525d32af3b68fa978ad7ddb04c4aaf25 | 21931 |
| evidence/20261001/resonant_density_manifest.json | archive/evidence/20261001/resonant_density_manifest.json | a1966337dfaa9b0bce40aed9a51ee4fcda96f002 | 1233 |
| evidence/20261001/resonant_density_wolfram.json | archive/evidence/20261001/resonant_density_wolfram.json | 720b88c3c98b51e2d507c137fdb78233657af131 | 1931 |

### evidence/20261004 -> archive/evidence/20261004

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20261004/circular_dyson_contract.json | archive/evidence/20261004/circular_dyson_contract.json | ea6e1ff47b42c579832a703caa8010e29dcad3eb | 1961 |
| evidence/20261004/expansion_wavepacket_checks.json | archive/evidence/20261004/expansion_wavepacket_checks.json | ac47716cbbddf102e9ccb4559e98ba3e257cb7de | 9043 |
| evidence/20261004/expansion_wavepacket_completion_checks.json | archive/evidence/20261004/expansion_wavepacket_completion_checks.json | 972700eb040ce8043ab6dbe86a5e5ffc7baf2b7c | 9849 |
| evidence/20261004/expansion_wavepacket_wolfram.json | archive/evidence/20261004/expansion_wavepacket_wolfram.json | 72e53dce5874a3f1526d3d4f105395a03d0e76c8 | 438 |
| evidence/20261004/expansion_wavepacket_wolfram_completion.json | archive/evidence/20261004/expansion_wavepacket_wolfram_completion.json | 9597ab305ccd05c165f42f599b439a8b3e824d8a | 6919 |
| evidence/20261004/folded_quadratic_checks_corrected.json | archive/evidence/20261004/folded_quadratic_checks_corrected.json | 7d99db8e34d63646698566abb6d6264c33677761 | 19256 |
| evidence/20261004/folded_quadratic_manifest.json | archive/evidence/20261004/folded_quadratic_manifest.json | e1b9d3a0655cf4dded728a65e4ee1bc9b5d721ce | 2234 |
| evidence/20261004/folded_quadratic_manifest_corrected.json | archive/evidence/20261004/folded_quadratic_manifest_corrected.json | 6469a3ed192ca041011b900e833dbbe1777d418e | 2623 |
| evidence/20261004/general_start_contract.json | archive/evidence/20261004/general_start_contract.json | 9a05e09dda1e1f131bd0a59fd4aba4685a611c3e | 2694 |
| evidence/20261004/general_start_integration.json | archive/evidence/20261004/general_start_integration.json | 4d5ea6a2bbef0a6daa253c7219348308b4545d58 | 18209 |
| evidence/20261004/polynomial_coboundary_contract.json | archive/evidence/20261004/polynomial_coboundary_contract.json | 92836b0f7c74dd0412135f06251eb5416ebe76db | 1518 |
| evidence/20261004/polynomial_coboundary_wolfram.json | archive/evidence/20261004/polynomial_coboundary_wolfram.json | 6cda143cc2658e7ecca684d2d0b578d2f01bb353 | 1005 |
| evidence/20261004/publication_ci_completion.json | archive/evidence/20261004/publication_ci_completion.json | e3281fa0ea7bc080f4d96fd0ba1bb314c1342269 | 27226 |
| evidence/20261004/supplement_replay_completion.json | archive/evidence/20261004/supplement_replay_completion.json | 970a8acc89dcbe99da688ac247276474b123bf6d | 12876 |

### evidence/20261005 -> archive/evidence/20261005

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20261005/all_order_contract.json | archive/evidence/20261005/all_order_contract.json | 8f93fa8aef3fe11bf008ef8215360998e87c5904 | 4523 |
| evidence/20261005/critical_noise_contract.json | archive/evidence/20261005/critical_noise_contract.json | 8f86537e7dda61811243bf1081b45b8a4ab39a45 | 4979 |
| evidence/20261005/growing_degree_contract.json | archive/evidence/20261005/growing_degree_contract.json | ea4f9447cd04e38a2e6c87bc7a968153e9459adc | 4576 |
| evidence/20261005/heisenberg_pair_heat_contract.json | archive/evidence/20261005/heisenberg_pair_heat_contract.json | 76ea57334dfe62560d5217771d22cab9f390af95 | 3661 |
| evidence/20261005/heisenberg_pair_heat_wolfram.json | archive/evidence/20261005/heisenberg_pair_heat_wolfram.json | c1e74e3b0f1aaccebed4ba9633614a0eafcd4f95 | 1355 |
| evidence/20261005/noise_removal_contract.json | archive/evidence/20261005/noise_removal_contract.json | b5595f8e34a3c9d97b7d492ceef195fe9ccb1fe5 | 3424 |

### evidence/20261006 -> archive/evidence/20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/20261006/collective_diffusion_contract.json | archive/evidence/20261006/collective_diffusion_contract.json | f3f10bd85b9a2e62a4a9286cb2d2390e104b3ff6 | 2709 |
| evidence/20261006/collective_diffusion_contract_v2.json | archive/evidence/20261006/collective_diffusion_contract_v2.json | 6bf1c703ecc97ee62a5ef8b6e68ec625473ed572 | 3562 |
| evidence/20261006/collective_diffusion_spectrum_contract.json | archive/evidence/20261006/collective_diffusion_spectrum_contract.json | fbd733ac38d77ab10b0ff6c21b3d33e552190cce | 1779 |
| evidence/20261006/frozen_operator_transfer_contract.json | archive/evidence/20261006/frozen_operator_transfer_contract.json | c30bd62a2a26cad426a7ecf127bdfb03a20f5821 | 3412 |
| evidence/20261006/frozen_operator_transfer_wolfram.json | archive/evidence/20261006/frozen_operator_transfer_wolfram.json | 623fb33e445951ba227b9acdcd6cca7bcae6ff51 | 2160 |
| evidence/20261006/original_channel_gap_contract.json | archive/evidence/20261006/original_channel_gap_contract.json | 2b1ee24419e994d175e8e24c3ee4f8e1921e9aeb | 1155 |

### evidence/actual_commutant_20261006 -> archive/evidence/actual_commutant_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/actual_commutant_20261006/actual_algebra_check.log | archive/evidence/actual_commutant_20261006/actual_algebra_check.log | eae91785e9336f11e42c77e2c4ab3e6b9a46841a | 274 |
| evidence/actual_commutant_20261006/actual_algebra_results.json | archive/evidence/actual_commutant_20261006/actual_algebra_results.json | 53f1dece5beab3cfe9261d19490e2e67dce85f0e | 199 |
| evidence/actual_commutant_20261006/actual_factor_check.log | archive/evidence/actual_commutant_20261006/actual_factor_check.log | 05a2d158967a950c1e3972965f71f70ee2bd9bb3 | 707 |
| evidence/actual_commutant_20261006/actual_factor_results.json | archive/evidence/actual_commutant_20261006/actual_factor_results.json | 1cd09e4290fec497a585290ce83db1ed7f7e69fa | 7754 |
| evidence/actual_commutant_20261006/actual_family_review.md | archive/evidence/actual_commutant_20261006/actual_family_review.md | 54c3bb76c41c542f8c8aedbb1bb06645f141eec2 | 13929 |
| evidence/actual_commutant_20261006/actual_field_check.log | archive/evidence/actual_commutant_20261006/actual_field_check.log | f3e96e2bbecbed54cb9207a374a1377568665565 | 210 |
| evidence/actual_commutant_20261006/actual_field_results.json | archive/evidence/actual_commutant_20261006/actual_field_results.json | dbf3fced84c79ae4dc8edcd0da63080a19a8f802 | 202 |
| evidence/actual_commutant_20261006/actual_review_manifest.json | archive/evidence/actual_commutant_20261006/actual_review_manifest.json | 1eb5ce29a4fa914648f15f16983923c2f08e8529 | 1585 |
| evidence/actual_commutant_20261006/promotion_receipt.json | archive/evidence/actual_commutant_20261006/promotion_receipt.json | 6d734af9ed2f0a9d697ab424196f6628d3350233 | 30036 |
| evidence/actual_commutant_20261006/replay_normal/actual_algebra_check.log | archive/evidence/actual_commutant_20261006/replay_normal/actual_algebra_check.log | 11cb532ed9cad71346bedbf1a6207013af346f27 | 274 |
| evidence/actual_commutant_20261006/replay_normal/actual_algebra_results.json | archive/evidence/actual_commutant_20261006/replay_normal/actual_algebra_results.json | cd4503f69b6a0433188d237684e00b500aea2993 | 199 |
| evidence/actual_commutant_20261006/replay_normal/actual_casoratian_check.log | archive/evidence/actual_commutant_20261006/replay_normal/actual_casoratian_check.log | e7158eed7b1d909ae24e424e76c6f006d1303b80 | 86 |
| evidence/actual_commutant_20261006/replay_normal/actual_casoratian_results.json | archive/evidence/actual_commutant_20261006/replay_normal/actual_casoratian_results.json | c5253bd36d758f8c57c23734f14d891febb72ff9 | 98 |
| evidence/actual_commutant_20261006/replay_normal/actual_factor_check.log | archive/evidence/actual_commutant_20261006/replay_normal/actual_factor_check.log | ca9c7aa6b4bae5e60233876ddfdefaf89683c98c | 200 |
| evidence/actual_commutant_20261006/replay_normal/actual_factor_results.json | archive/evidence/actual_commutant_20261006/replay_normal/actual_factor_results.json | 7a127dd4eca28f634fa96773348a188eabea09bf | 7754 |
| evidence/actual_commutant_20261006/replay_normal/actual_field_check.log | archive/evidence/actual_commutant_20261006/replay_normal/actual_field_check.log | e6c3ae9a3b49b2e469d8e97057762da2059129bd | 210 |
| evidence/actual_commutant_20261006/replay_normal/actual_field_results.json | archive/evidence/actual_commutant_20261006/replay_normal/actual_field_results.json | 77b26e8e071ab95dfe2f85176a558abd5217f987 | 202 |
| evidence/actual_commutant_20261006/replay_optimized/actual_algebra_check.log | archive/evidence/actual_commutant_20261006/replay_optimized/actual_algebra_check.log | 32c40da34c81079b3628c56575df24788a91a9e5 | 275 |
| evidence/actual_commutant_20261006/replay_optimized/actual_algebra_results.json | archive/evidence/actual_commutant_20261006/replay_optimized/actual_algebra_results.json | 5e6c147c473631144293819793c215d029cd823a | 200 |
| evidence/actual_commutant_20261006/replay_optimized/actual_casoratian_check.log | archive/evidence/actual_commutant_20261006/replay_optimized/actual_casoratian_check.log | e7158eed7b1d909ae24e424e76c6f006d1303b80 | 86 |
| evidence/actual_commutant_20261006/replay_optimized/actual_casoratian_results.json | archive/evidence/actual_commutant_20261006/replay_optimized/actual_casoratian_results.json | c5253bd36d758f8c57c23734f14d891febb72ff9 | 98 |
| evidence/actual_commutant_20261006/replay_optimized/actual_factor_check.log | archive/evidence/actual_commutant_20261006/replay_optimized/actual_factor_check.log | c264f18af66a85b1fe15fe6cc54d6f88ad61bb6c | 201 |
| evidence/actual_commutant_20261006/replay_optimized/actual_factor_results.json | archive/evidence/actual_commutant_20261006/replay_optimized/actual_factor_results.json | e8cde72bebd71e9496862c3fa97fdfbbdbbc80e2 | 7755 |
| evidence/actual_commutant_20261006/replay_optimized/actual_field_check.log | archive/evidence/actual_commutant_20261006/replay_optimized/actual_field_check.log | a338c945fe6d1e610d65b1cbe201c6813704454b | 210 |
| evidence/actual_commutant_20261006/replay_optimized/actual_field_results.json | archive/evidence/actual_commutant_20261006/replay_optimized/actual_field_results.json | ecfd5768967c5605d6222175bd351de0bb5c8241 | 202 |

### evidence/cayley_inverse_pair_sum_factorization_20260905.txt -> archive/evidence/cayley_inverse_pair_sum_factorization_20260905.txt

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/cayley_inverse_pair_sum_factorization_20260905.txt | archive/evidence/cayley_inverse_pair_sum_factorization_20260905.txt | c12e673a38aaba44b9da7c38dfbbc3e2af96eece | 3416 |

### evidence/cayley_psc_transversality_20260905.txt -> archive/evidence/cayley_psc_transversality_20260905.txt

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/cayley_psc_transversality_20260905.txt | archive/evidence/cayley_psc_transversality_20260905.txt | 3237abfde3dd35ef087824d6e68043217505cd3c | 2064 |

### evidence/cayley_trace_intercept_rigidity_20260905.txt -> archive/evidence/cayley_trace_intercept_rigidity_20260905.txt

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/cayley_trace_intercept_rigidity_20260905.txt | archive/evidence/cayley_trace_intercept_rigidity_20260905.txt | a0e36f36ac456fc3a9d8072eb35b0082b216cc52 | 3015 |

### evidence/checked_checkpoint_acceptance_20261007 -> archive/evidence/checked_checkpoint_acceptance_20261007

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/checked_checkpoint_acceptance_20261007/SHA256SUMS.json | archive/evidence/checked_checkpoint_acceptance_20261007/SHA256SUMS.json | aed932a9e35fcb11dad77690ee9cda8815c6b000 | 4356 |
| evidence/checked_checkpoint_acceptance_20261007/acceptance.json | archive/evidence/checked_checkpoint_acceptance_20261007/acceptance.json | 978a2d265a257a93804e6f5ca72185c708127593 | 1753 |
| evidence/checked_checkpoint_acceptance_20261007/capture_receipt.json | archive/evidence/checked_checkpoint_acceptance_20261007/capture_receipt.json | f0fd8e533a4a781be8bf048c4aceead509d89198 | 331 |
| evidence/checked_checkpoint_acceptance_20261007/cpp_build_summary.log | archive/evidence/checked_checkpoint_acceptance_20261007/cpp_build_summary.log | 7550fc47cf7e6b0db3ec46e869478ecdcc112729 | 59 |
| evidence/checked_checkpoint_acceptance_20261007/fixed_map_supplement/verification.json | archive/evidence/checked_checkpoint_acceptance_20261007/fixed_map_supplement/verification.json | f7860fe57af0ab62d2f9801842a33bc3804b862f | 11921 |
| evidence/checked_checkpoint_acceptance_20261007/fresh_cpp_build.json | archive/evidence/checked_checkpoint_acceptance_20261007/fresh_cpp_build.json | 367d33b89f723e37577129448aec5cf33b56fe41 | 16617 |
| evidence/checked_checkpoint_acceptance_20261007/lean.log | archive/evidence/checked_checkpoint_acceptance_20261007/lean.log | 4e8fe9ca07130118ae9217c4dea1bf4c9b6bb431 | 13450 |
| evidence/checked_checkpoint_acceptance_20261007/lean_build_receipt.json | archive/evidence/checked_checkpoint_acceptance_20261007/lean_build_receipt.json | a36318f7fdf0da14e57fdf0ac88299ad284af444 | 5011 |
| evidence/checked_checkpoint_acceptance_20261007/maintenance_exit.json | archive/evidence/checked_checkpoint_acceptance_20261007/maintenance_exit.json | 0e78a3bd1bceddb9566beecc94ea19254aa7f7e3 | 47 |
| evidence/checked_checkpoint_acceptance_20261007/maintenance_normal.log | archive/evidence/checked_checkpoint_acceptance_20261007/maintenance_normal.log | e45fabafa32c6df11bdeef18a98f1d815df9bfea | 22271 |
| evidence/checked_checkpoint_acceptance_20261007/maintenance_optimized.log | archive/evidence/checked_checkpoint_acceptance_20261007/maintenance_optimized.log | ffa55c9924eda551a4fe0a57c6d29e778f34db81 | 22271 |
| evidence/checked_checkpoint_acceptance_20261007/manuscript/build_manifest.json | archive/evidence/checked_checkpoint_acceptance_20261007/manuscript/build_manifest.json | e12ed07436e112f28c5a57fbd67019f5fa8e0e14 | 14319 |
| evidence/checked_checkpoint_acceptance_20261007/manuscript/visual_review.json | archive/evidence/checked_checkpoint_acceptance_20261007/manuscript/visual_review.json | ee4d79c70fb9663e804add8712595b275925616d | 1560 |
| evidence/checked_checkpoint_acceptance_20261007/manuscript_run.log | archive/evidence/checked_checkpoint_acceptance_20261007/manuscript_run.log | 60796913565ef3aec6d52626f451c7aef5420d2f | 168 |
| evidence/checked_checkpoint_acceptance_20261007/publication_preflight/independent_gate_validation.json | archive/evidence/checked_checkpoint_acceptance_20261007/publication_preflight/independent_gate_validation.json | fef0c153ca17f6638cd70c6b8a859e82cfc6858d | 1558 |
| evidence/checked_checkpoint_acceptance_20261007/r6_review/REVIEW.md | archive/evidence/checked_checkpoint_acceptance_20261007/r6_review/REVIEW.md | 8bc9a6d3a26d6c9538543ae392fc18e800f2f867 | 8832 |
| evidence/checked_checkpoint_acceptance_20261007/r6_review/artifact_sha256.json | archive/evidence/checked_checkpoint_acceptance_20261007/r6_review/artifact_sha256.json | cd0038111146d36a2d97b41599d18dc631642ee2 | 22758 |
| evidence/checked_checkpoint_acceptance_20261007/r6_review/final_seal.json | archive/evidence/checked_checkpoint_acceptance_20261007/r6_review/final_seal.json | bc71fc2d239385ccd0a80b493ef613f92626c2a7 | 2628 |
| evidence/checked_checkpoint_acceptance_20261007/raw_whitespace_exceptions.json | archive/evidence/checked_checkpoint_acceptance_20261007/raw_whitespace_exceptions.json | 4742f1594e26b76d98ce7413034953c498096d9c | 13485 |
| evidence/checked_checkpoint_acceptance_20261007/release_review/closing_source_validation.json | archive/evidence/checked_checkpoint_acceptance_20261007/release_review/closing_source_validation.json | e5b675fe7a877c1b562b124b8db4648994da28d5 | 297 |
| evidence/checked_checkpoint_acceptance_20261007/release_review/final_durable_replay_validation.json | archive/evidence/checked_checkpoint_acceptance_20261007/release_review/final_durable_replay_validation.json | e70674d8d6753f79e31a60545a4b281647cd9be8 | 178980 |
| evidence/checked_checkpoint_acceptance_20261007/release_review/final_graph_validation.json | archive/evidence/checked_checkpoint_acceptance_20261007/release_review/final_graph_validation.json | 013fe88601d26e5fa7d679023bf7bd40d6ff2da9 | 295 |
| evidence/checked_checkpoint_acceptance_20261007/release_review/final_repair_binding_validation.json | archive/evidence/checked_checkpoint_acceptance_20261007/release_review/final_repair_binding_validation.json | 697a28263be16b413a077e89775d14a7586a7480 | 10619 |
| evidence/checked_checkpoint_acceptance_20261007/release_review/release_review_manifest.json | archive/evidence/checked_checkpoint_acceptance_20261007/release_review/release_review_manifest.json | 73f1cc2f6bff6b729d99cebd3de7476466609186 | 25169 |
| evidence/checked_checkpoint_acceptance_20261007/release_review/root_archive_validation.json | archive/evidence/checked_checkpoint_acceptance_20261007/release_review/root_archive_validation.json | aa2186e4bbfeaa4542d456f9c5c0ca5f92770d82 | 795 |
| evidence/checked_checkpoint_acceptance_20261007/release_review/scope_review.md | archive/evidence/checked_checkpoint_acceptance_20261007/release_review/scope_review.md | 34e02907eb3d8f8543fe5eb0dae86b62173b52a9 | 13043 |
| evidence/checked_checkpoint_acceptance_20261007/source_manifest.json | archive/evidence/checked_checkpoint_acceptance_20261007/source_manifest.json | 91414b200fe55f6e32b2ca40521c87ee900ae3ba | 573819 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/0.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/0.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/0.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/0.stdout | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/1.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/1.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/1.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/1.stdout | b3f2a16a6963d0e629560fe4d38b5c121ac7fd19 | 68 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/2.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/2.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/2.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/2.stdout | e16f4e764a10b2acf393d13f9f2b297470e9c4b5 | 318 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/3.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/3.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/3.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/3.stdout | 07f2f2f27ad26bbdf0894fd22c56b44a59e3f960 | 935 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/4.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/4.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/4.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/4.stdout | a2dfebaeff71155f36e4eaf9e9dfc71a9fd8875a | 26 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/5.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/5.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/5.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/5.stdout | bdf754c73628b6b0c7a00c21af9008cf98ffdc64 | 18 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/6.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/6.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/6.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/6.stdout | fc41337527dc984f493c11ada3559672a03c42e1 | 39 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/7.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/7.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/7.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/7.stdout | cfab2a06c3684fd44ec6e27fb53b7c7f19f7c901 | 59 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/8.stderr | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/8.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/8.stdout | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/8.stdout | f118ecd5e272b875a63d29d37cdd6591d2cfe962 | 38 |
| evidence/checked_checkpoint_acceptance_20261007/static_gates/results.json | archive/evidence/checked_checkpoint_acceptance_20261007/static_gates/results.json | 3e58726d7d3b55916624e6ffa5dea9451de064fe | 2368 |
| evidence/checked_checkpoint_acceptance_20261007/supplement_run.log | archive/evidence/checked_checkpoint_acceptance_20261007/supplement_run.log | b4293661253363d5c4e2aa7de3f9a8c7783ea972 | 9804 |
| evidence/checked_checkpoint_acceptance_20261007/workspace.json | archive/evidence/checked_checkpoint_acceptance_20261007/workspace.json | e7b9be32553240bf4941b378699eb6a088dbed76 | 739604 |
| evidence/checked_checkpoint_acceptance_20261007/workspace_run.log | archive/evidence/checked_checkpoint_acceptance_20261007/workspace_run.log | e0d9117415af453874329db273367c0cf50a4fbb | 5890 |

### evidence/collective_20261006 -> archive/evidence/collective_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/collective_20261006/original_results/kostka.json | archive/evidence/collective_20261006/original_results/kostka.json | ceb142ef05a5779846b0cf9b1c14c30f334afc7e | 12527 |
| evidence/collective_20261006/original_results/ordered.json | archive/evidence/collective_20261006/original_results/ordered.json | 9b4af92459fdaf4f1a8b56b90da2b5ce8d54105a | 9220 |
| evidence/collective_20261006/original_results/quadratic_diagnostic.json | archive/evidence/collective_20261006/original_results/quadratic_diagnostic.json | 495886ce019873e27906d4a464b0f718fa876414 | 21349 |
| evidence/collective_20261006/original_results/slow_diagnostic.json | archive/evidence/collective_20261006/original_results/slow_diagnostic.json | d1ff6a1175c1779a393c2d82a4ac2927aad8b02d | 6281 |
| evidence/collective_20261006/original_results/trace.json | archive/evidence/collective_20261006/original_results/trace.json | c5ccfff71b1213d80ed41789c2c1d5e7f9bbea05 | 3769 |
| evidence/collective_20261006/promotion_receipt.json | archive/evidence/collective_20261006/promotion_receipt.json | c112f65afa076d05cb5b914a0664d3af4c6b4b42 | 1577 |
| evidence/collective_20261006/source_binding.json | archive/evidence/collective_20261006/source_binding.json | adb6f9971cfec5dcbaa7193372bea42d5ed0b86c | 3642 |

### evidence/combined_wave3_v4_acceptance_20261007 -> archive/evidence/combined_wave3_v4_acceptance_20261007

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/combined_wave3_v4_acceptance_20261007/README.md | archive/evidence/combined_wave3_v4_acceptance_20261007/README.md | a8c9f897851e5fa76f8094a3dfec758992f21d6f | 1430 |
| evidence/combined_wave3_v4_acceptance_20261007/SHA256SUMS.json | archive/evidence/combined_wave3_v4_acceptance_20261007/SHA256SUMS.json | 416f842291ecde5c125c0490c5fe8445e4dafde4 | 5468 |
| evidence/combined_wave3_v4_acceptance_20261007/VALIDATION_SCOPE.txt | archive/evidence/combined_wave3_v4_acceptance_20261007/VALIDATION_SCOPE.txt | da0f3f72a02157e10758d9f2a6c60383eefe1293 | 1640 |
| evidence/combined_wave3_v4_acceptance_20261007/acceptance.json | archive/evidence/combined_wave3_v4_acceptance_20261007/acceptance.json | 4673b9707a87a4e0671581582ad03b7c9737076d | 4601 |
| evidence/combined_wave3_v4_acceptance_20261007/artifact_manifest.json | archive/evidence/combined_wave3_v4_acceptance_20261007/artifact_manifest.json | 64c57596c2bf291309757ecc7c3693544e781395 | 116922 |
| evidence/combined_wave3_v4_acceptance_20261007/budget_coherence.json | archive/evidence/combined_wave3_v4_acceptance_20261007/budget_coherence.json | 9957164a2f0c7151da5133c4608a36cdeb416737 | 1542 |
| evidence/combined_wave3_v4_acceptance_20261007/cpp_source_equivalent_closure.json | archive/evidence/combined_wave3_v4_acceptance_20261007/cpp_source_equivalent_closure.json | f50f4e3ad62d22756e190026f7c49d1d702c23f3 | 3406 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_full_end_2_1/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_full_end_2_1/execution_receipt.json | a3ded53d09d824f61f758ad78e42ad5aac10a971 | 5714 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_full_end_2_2/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_full_end_2_2/execution_receipt.json | 9bd65496c49c1b3810f6ccaf5a9963ab72c87172 | 5714 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_full_end_2_3/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_full_end_2_3/execution_receipt.json | 17c4c5c4a88fe33f9f746fb0e826a4e3395a0be1 | 5714 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_full_end_3_2/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_full_end_3_2/execution_receipt.json | 9855fca42b1ca3496fea73a2217792d6b62abda5 | 5714 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_network/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_network/execution_receipt.json | 55d43f389938ccc073dee118cc2dc844784d363c | 5689 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_offcharge_bound/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_offcharge_bound/execution_receipt.json | cc0947d1370ce471428a77d1b7f2d91b005780b6 | 5729 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_replay/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_replay/execution_receipt.json | 9e176c778bdc345f579ce960dc4bac855c7469d2 | 7784 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_top_gram/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_top_gram/execution_receipt.json | 6bf819439f1baef121fe734411787224792e2d38 | 5694 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_torus/execution_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/fractional_hamming_torus/execution_receipt.json | 0e5f097f87af9a86d14362474a46b6f8a60ab9a2 | 5679 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/research_checkpoint_replay/replay_manifest.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/research_checkpoint_replay/replay_manifest.json | f9279f39fcdef4e66a3f4e5c31f6f99d1458e0c8 | 79797 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/wave2_checked_replay/replay_manifest.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/wave2_checked_replay/replay_manifest.json | 0dd820a4b8c0f1ca968a19a776235ae05ce1ad1c | 57851 |
| evidence/combined_wave3_v4_acceptance_20261007/durable_routes/wave3_checked_replay/replay_manifest.json | archive/evidence/combined_wave3_v4_acceptance_20261007/durable_routes/wave3_checked_replay/replay_manifest.json | a33561a87cf655d493a29b18b8872ffc92030518 | 13443 |
| evidence/combined_wave3_v4_acceptance_20261007/execution_status.json | archive/evidence/combined_wave3_v4_acceptance_20261007/execution_status.json | 6ed280ac4efc26528da9e9fc7589cce152477e3c | 36770 |
| evidence/combined_wave3_v4_acceptance_20261007/final_gate_acceptance.json | archive/evidence/combined_wave3_v4_acceptance_20261007/final_gate_acceptance.json | 46585f8e7863827cde72a896d028e8f5d540f38f | 10573 |
| evidence/combined_wave3_v4_acceptance_20261007/fixed_map_supplement_source_equivalent_closure.json | archive/evidence/combined_wave3_v4_acceptance_20261007/fixed_map_supplement_source_equivalent_closure.json | 51ac79bd2474bfbb3e349a2978d7d7dfd1b5032c | 16530 |
| evidence/combined_wave3_v4_acceptance_20261007/historical/f9680ac_hosted_ci_terminal_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/historical/f9680ac_hosted_ci_terminal_receipt.json | 66c3b3c8ca844e74dc90fb8e13a37ea87952d713 | 1414 |
| evidence/combined_wave3_v4_acceptance_20261007/historical/v1_review_hold.json | archive/evidence/combined_wave3_v4_acceptance_20261007/historical/v1_review_hold.json | 194bf41f3d71bc5f78985f0c838db3a056153723 | 1503 |
| evidence/combined_wave3_v4_acceptance_20261007/historical/v3/artifact_manifest.json | archive/evidence/combined_wave3_v4_acceptance_20261007/historical/v3/artifact_manifest.json | 9712aaedf28d625f279dfc47c6c18bb3fce10a0a | 117308 |
| evidence/combined_wave3_v4_acceptance_20261007/historical/v3/final_gate_acceptance.json | archive/evidence/combined_wave3_v4_acceptance_20261007/historical/v3/final_gate_acceptance.json | 104830207fd663b1b0d2788a36a2486b70bb9808 | 10214 |
| evidence/combined_wave3_v4_acceptance_20261007/independent_receipt_recheck.json | archive/evidence/combined_wave3_v4_acceptance_20261007/independent_receipt_recheck.json | dbe4a1e8d1c61a9ec31de5cbdc2c2e23941776c5 | 766 |
| evidence/combined_wave3_v4_acceptance_20261007/lean_source_equivalent_closure.json | archive/evidence/combined_wave3_v4_acceptance_20261007/lean_source_equivalent_closure.json | f3e5402a7f06bad33d9b585baeebcca7ca361603 | 4053 |
| evidence/combined_wave3_v4_acceptance_20261007/legacy_durable_acceptance.json | archive/evidence/combined_wave3_v4_acceptance_20261007/legacy_durable_acceptance.json | 4019e9f388455c2440ac4ba8b1c6270bf1a048ea | 7999 |
| evidence/combined_wave3_v4_acceptance_20261007/maintenance_python312_normal.log | archive/evidence/combined_wave3_v4_acceptance_20261007/maintenance_python312_normal.log | 8d3d15427fde45def8753128aa55808b30a6fec0 | 32524 |
| evidence/combined_wave3_v4_acceptance_20261007/maintenance_python312_optimized.log | archive/evidence/combined_wave3_v4_acceptance_20261007/maintenance_python312_optimized.log | f2478b4f45d188b0858639021e5cbceed3a628df | 32524 |
| evidence/combined_wave3_v4_acceptance_20261007/maintenance_python313_normal.log | archive/evidence/combined_wave3_v4_acceptance_20261007/maintenance_python313_normal.log | 854d987306c641da0bdff676c3aabac23ef3e34e | 32524 |
| evidence/combined_wave3_v4_acceptance_20261007/maintenance_python313_optimized.log | archive/evidence/combined_wave3_v4_acceptance_20261007/maintenance_python313_optimized.log | 9a360be1922f88df0dd231f80bf110768b3b128a | 32524 |
| evidence/combined_wave3_v4_acceptance_20261007/manuscript_source_equivalent_closure.json | archive/evidence/combined_wave3_v4_acceptance_20261007/manuscript_source_equivalent_closure.json | 683551d579a42e19fa11bdd5ff926a76e96dd58a | 13490 |
| evidence/combined_wave3_v4_acceptance_20261007/numeric_durable_acceptance.json | archive/evidence/combined_wave3_v4_acceptance_20261007/numeric_durable_acceptance.json | 21fa9e2dc9a8cda1c1e265ac8b3ceb07919b8878 | 6970 |
| evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/fixed_map_supplement/verification.json | archive/evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/fixed_map_supplement/verification.json | 91669ce2fc7a38f3267877c38d4d4116a2c1a0c3 | 11921 |
| evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/fresh_cpp_build.json | archive/evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/fresh_cpp_build.json | 87dc81e08e96d24968121c02eb6f00c79d11d75a | 20163 |
| evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/lean_complete.log | archive/evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/lean_complete.log | d142ebea6fb0fb761878b0cba2c4edee7ea1a680 | 13450 |
| evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/manuscript/build_manifest.json | archive/evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/manuscript/build_manifest.json | 1bb13ec3ca56d7844b2cc70029e49f7c9731923b | 14446 |
| evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/v1_partial_gate_acceptance.json | archive/evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/v1_partial_gate_acceptance.json | f6a2266589d1fc831d9bb48805f097fd52e871eb | 2253 |
| evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/visual_qa/acceptance.json | archive/evidence/combined_wave3_v4_acceptance_20261007/original_source_equivalent_gates/visual_qa/acceptance.json | 6f0137be21314439cb4d3c0e13113810b7571d58 | 1432 |
| evidence/combined_wave3_v4_acceptance_20261007/runtime_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/runtime_receipt.json | 8872df37ae6126e0cefc6b744fe3dbcb5b21c93a | 984 |
| evidence/combined_wave3_v4_acceptance_20261007/science_and_focused_execution.json | archive/evidence/combined_wave3_v4_acceptance_20261007/science_and_focused_execution.json | f7cf5fc896272ee734071b9b739638f52af1f496 | 1298 |
| evidence/combined_wave3_v4_acceptance_20261007/snapshot_receipt.json | archive/evidence/combined_wave3_v4_acceptance_20261007/snapshot_receipt.json | f91f655fbd50254f07187e681f600b2e75789302 | 1680 |
| evidence/combined_wave3_v4_acceptance_20261007/source_manifest.json | archive/evidence/combined_wave3_v4_acceptance_20261007/source_manifest.json | 514aa12703643d910fad1de4e3eb612832e31ada | 616931 |
| evidence/combined_wave3_v4_acceptance_20261007/source_mode_manifest.json | archive/evidence/combined_wave3_v4_acceptance_20261007/source_mode_manifest.json | 14ce97464b45a96a9d3d790c183a5cb90717720e | 351430 |
| evidence/combined_wave3_v4_acceptance_20261007/static_focused_acceptance.json | archive/evidence/combined_wave3_v4_acceptance_20261007/static_focused_acceptance.json | dc410806b931b9c1e0532ffde236c39f2433cfeb | 31837 |
| evidence/combined_wave3_v4_acceptance_20261007/workspace_python313.json | archive/evidence/combined_wave3_v4_acceptance_20261007/workspace_python313.json | c1ec7ae2174ae73013a4a8497cd48f5a6b2970b0 | 794696 |

### evidence/factorial_diagonal_20261007 -> archive/evidence/factorial_diagonal_20261007

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/factorial_diagonal_20261007/original_results/general.json | archive/evidence/factorial_diagonal_20261007/original_results/general.json | 953d0ece42464c1bad6793ac7ba7579778a84a51 | 34908 |
| evidence/factorial_diagonal_20261007/original_results/n2_m4.json | archive/evidence/factorial_diagonal_20261007/original_results/n2_m4.json | a90da4c24fd05cb26d5eb08e1af29fa35ae5ee03 | 1490 |
| evidence/factorial_diagonal_20261007/original_results/ports.json | archive/evidence/factorial_diagonal_20261007/original_results/ports.json | 3acb21ab65155bb330e1e4a7cae4157bfd66fffd | 2408 |
| evidence/factorial_diagonal_20261007/original_results/small.json | archive/evidence/factorial_diagonal_20261007/original_results/small.json | 3a0192b535a4b877af10489e565ec2a67ee69b22 | 1950 |
| evidence/factorial_diagonal_20261007/promotion_receipt.json | archive/evidence/factorial_diagonal_20261007/promotion_receipt.json | 81630580bdc14ef2decc9d1b12d6d13271602e1a | 983 |
| evidence/factorial_diagonal_20261007/source_binding.json | archive/evidence/factorial_diagonal_20261007/source_binding.json | 09107858cfac5db8c6b2171c21f34a52f6eb7e9f | 13770 |

### evidence/first_seven_20261006 -> archive/evidence/first_seven_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/first_seven_20261006/normal/actual_small.log | archive/evidence/first_seven_20261006/normal/actual_small.log | af8b99888c757144679219f9c971c29477c8bae1 | 437 |
| evidence/first_seven_20261006/normal/actual_small.stderr | archive/evidence/first_seven_20261006/normal/actual_small.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/normal/compile_actual_small.log | archive/evidence/first_seven_20261006/normal/compile_actual_small.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/normal/compile_actual_small.stderr | archive/evidence/first_seven_20261006/normal/compile_actual_small.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/normal/compile_first_seven_exact.log | archive/evidence/first_seven_20261006/normal/compile_first_seven_exact.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/normal/compile_first_seven_exact.stderr | archive/evidence/first_seven_20261006/normal/compile_first_seven_exact.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/normal/dictionary.log | archive/evidence/first_seven_20261006/normal/dictionary.log | 47581b6a0398c59e5008468fb4b5f4c218bfd63a | 1903 |
| evidence/first_seven_20261006/normal/dictionary.stderr | archive/evidence/first_seven_20261006/normal/dictionary.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/normal/first_seven_exact.log | archive/evidence/first_seven_20261006/normal/first_seven_exact.log | 00fb51458ea244130c03a8f4197c7dfb79378e38 | 1046 |
| evidence/first_seven_20261006/normal/first_seven_exact.stderr | archive/evidence/first_seven_20261006/normal/first_seven_exact.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/normal/receipt.json | archive/evidence/first_seven_20261006/normal/receipt.json | 1c01868c8c589f8f5a83fd899cbf999c74102122 | 3506 |
| evidence/first_seven_20261006/optimized/actual_small.log | archive/evidence/first_seven_20261006/optimized/actual_small.log | af8b99888c757144679219f9c971c29477c8bae1 | 437 |
| evidence/first_seven_20261006/optimized/actual_small.stderr | archive/evidence/first_seven_20261006/optimized/actual_small.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/optimized/compile_actual_small.log | archive/evidence/first_seven_20261006/optimized/compile_actual_small.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/optimized/compile_actual_small.stderr | archive/evidence/first_seven_20261006/optimized/compile_actual_small.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/optimized/compile_first_seven_exact.log | archive/evidence/first_seven_20261006/optimized/compile_first_seven_exact.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/optimized/compile_first_seven_exact.stderr | archive/evidence/first_seven_20261006/optimized/compile_first_seven_exact.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/optimized/dictionary.log | archive/evidence/first_seven_20261006/optimized/dictionary.log | 47581b6a0398c59e5008468fb4b5f4c218bfd63a | 1903 |
| evidence/first_seven_20261006/optimized/dictionary.stderr | archive/evidence/first_seven_20261006/optimized/dictionary.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/optimized/first_seven_exact.log | archive/evidence/first_seven_20261006/optimized/first_seven_exact.log | 00fb51458ea244130c03a8f4197c7dfb79378e38 | 1046 |
| evidence/first_seven_20261006/optimized/first_seven_exact.stderr | archive/evidence/first_seven_20261006/optimized/first_seven_exact.stderr | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/first_seven_20261006/optimized/receipt.json | archive/evidence/first_seven_20261006/optimized/receipt.json | 1a0416e655c63770b70c0617a11efd7abc126c76 | 3558 |
| evidence/first_seven_20261006/original/actual_small.log | archive/evidence/first_seven_20261006/original/actual_small.log | af8b99888c757144679219f9c971c29477c8bae1 | 437 |
| evidence/first_seven_20261006/original/actual_small_receipt.json | archive/evidence/first_seven_20261006/original/actual_small_receipt.json | 481ca46d1337b0ec056d28762b0728626b3b7b77 | 77 |
| evidence/first_seven_20261006/original/authority_snapshot.json | archive/evidence/first_seven_20261006/original/authority_snapshot.json | 3780825601cbaae4823e40a4c89c56371e24f7ca | 1754 |
| evidence/first_seven_20261006/original/candidate_manifest.json | archive/evidence/first_seven_20261006/original/candidate_manifest.json | 8b31da157539b96df732bb9e6cb62355431bfb5b | 3354 |
| evidence/first_seven_20261006/original/dictionary_results.json | archive/evidence/first_seven_20261006/original/dictionary_results.json | 5b53d5caa56d63084b68a7289b75e3fb3053aa65 | 1046 |
| evidence/first_seven_20261006/original/independent_check.log | archive/evidence/first_seven_20261006/original/independent_check.log | 00fb51458ea244130c03a8f4197c7dfb79378e38 | 1046 |
| evidence/first_seven_20261006/original/independent_check_receipt.json | archive/evidence/first_seven_20261006/original/independent_check_receipt.json | e7d8a376eec4046bc18834b54b4c0a222099e054 | 76 |
| evidence/first_seven_20261006/original/review_artifact_manifest.json | archive/evidence/first_seven_20261006/original/review_artifact_manifest.json | cc086ff5000795f891290633070304c69626e1f4 | 2035 |
| evidence/first_seven_20261006/original/verified_input_hashes.json | archive/evidence/first_seven_20261006/original/verified_input_hashes.json | 0e4c11188a03204e229fb0707c12b2ff2e7ee98d | 3033 |
| evidence/first_seven_20261006/parser_negative_receipt.json | archive/evidence/first_seven_20261006/parser_negative_receipt.json | a068c3e905e51b6e35494815d04d1e73df3bc5fa | 481 |
| evidence/first_seven_20261006/portability_normal.log | archive/evidence/first_seven_20261006/portability_normal.log | 9b756516135aa1a4d023b30be7df9f12728a4bff | 101 |
| evidence/first_seven_20261006/portability_optimized.log | archive/evidence/first_seven_20261006/portability_optimized.log | 54941f4c1bb0e19cc74bf1a8201b832f0770e5f6 | 101 |
| evidence/first_seven_20261006/promotion_receipt.json | archive/evidence/first_seven_20261006/promotion_receipt.json | dcfcd033fa29e1dfec6f9b65631128811fc4d4f0 | 1709 |

### evidence/fm008_fresh_audit_20261006 -> archive/evidence/fm008_fresh_audit_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/fm008_fresh_audit_20261006/independent_original.json | archive/evidence/fm008_fresh_audit_20261006/independent_original.json | f634f87b9154131972fdd99790edd2ae45974a87 | 5528 |
| evidence/fm008_fresh_audit_20261006/promotion_receipt.json | archive/evidence/fm008_fresh_audit_20261006/promotion_receipt.json | e5554c14bcd028557a7ea00c630fc10c132906d7 | 443 |

### evidence/hamming_ci_repair_acceptance_20261007 -> archive/evidence/hamming_ci_repair_acceptance_20261007

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/hamming_ci_repair_acceptance_20261007/SHA256SUMS.json | archive/evidence/hamming_ci_repair_acceptance_20261007/SHA256SUMS.json | 530882bb003dd44ede73af519ccf6be83f4fa1f6 | 4688 |
| evidence/hamming_ci_repair_acceptance_20261007/acceptance.json | archive/evidence/hamming_ci_repair_acceptance_20261007/acceptance.json | 4416655719ffd570b1162f11e4043fa0c9c63b1f | 2302 |
| evidence/hamming_ci_repair_acceptance_20261007/cpp_build_summary.log | archive/evidence/hamming_ci_repair_acceptance_20261007/cpp_build_summary.log | 2468eaa1401cec6412f123c670c75110c720c054 | 58 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_full_end_2_1/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_full_end_2_1/execution_receipt.json | 56a776a717649cbef236fb2fd540f46e7f96d917 | 5722 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_full_end_2_2/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_full_end_2_2/execution_receipt.json | cae1ed6c55cf09469a3cfa1ae69846ae3dc24ef0 | 5722 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_full_end_2_3/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_full_end_2_3/execution_receipt.json | dcd1073179752f74890aedd342c6c27def038119 | 5722 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_full_end_3_2/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_full_end_3_2/execution_receipt.json | 32b049ab4861e88718f51b82e2515736b0fa2513 | 5722 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_network/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_network/execution_receipt.json | 198e2a4c4cb0220e5429c3dafdf8a6ead0aa97d6 | 5697 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_offcharge_bound/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_offcharge_bound/execution_receipt.json | 4b95c5b6d86d4bd34e8de17352be77d4c59b9a73 | 5737 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/author.actual.raw | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/author.actual.raw | ed2a52effa3f74d1ff536462e363337600543c36 | 5572 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/author.comparison.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/author.comparison.json | 05e0e5ee43cdd492dae5c4e0c3e625f7d0860760 | 787 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/author.expected.raw | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/author.expected.raw | ae28dd504266c30a4d5284c8d2bc21f58f69baca | 5617 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/execution_receipt.json | b6e14e55da67fe97ede6d64c6516656066419d04 | 7800 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/synthesis.actual.raw | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/synthesis.actual.raw | 4e40481e799a928881a8748aa55711326ea9bc2d | 23167 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/synthesis.comparison.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/synthesis.comparison.json | eb00499b7c29e414c667dfec7b4f20bfe15e6412 | 504 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/synthesis.expected.raw | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_replay/synthesis.expected.raw | 4e40481e799a928881a8748aa55711326ea9bc2d | 23167 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_top_gram/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_top_gram/execution_receipt.json | b1d859f9ecf699f7fcfcd87b6ce3609e097ed258 | 5702 |
| evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_torus/execution_receipt.json | archive/evidence/hamming_ci_repair_acceptance_20261007/durable_hamming/fractional_hamming_torus/execution_receipt.json | edec9c595f120a440f88b496d39c4cc20b99cc0e | 5687 |
| evidence/hamming_ci_repair_acceptance_20261007/failed_hosted_129c676/fractional_hamming_replay.log | archive/evidence/hamming_ci_repair_acceptance_20261007/failed_hosted_129c676/fractional_hamming_replay.log | 1d2649c80338bc6c0f3ee24ae7c20e07fa0a8247 | 685 |
| evidence/hamming_ci_repair_acceptance_20261007/failed_hosted_129c676/local_pinned_dependency_diagnosis.json | archive/evidence/hamming_ci_repair_acceptance_20261007/failed_hosted_129c676/local_pinned_dependency_diagnosis.json | 273ed301c30c71bb9f8cc5bb9313ee4e9d8f70d3 | 588 |
| evidence/hamming_ci_repair_acceptance_20261007/failed_hosted_129c676/workspace.json | archive/evidence/hamming_ci_repair_acceptance_20261007/failed_hosted_129c676/workspace.json | 1529904b44450132fa82bba1a2b170e43f478c04 | 732122 |
| evidence/hamming_ci_repair_acceptance_20261007/final_gate_acceptance.json | archive/evidence/hamming_ci_repair_acceptance_20261007/final_gate_acceptance.json | da6f3938fc3b0999aaf5c339b691fa23fef3a0af | 6590 |
| evidence/hamming_ci_repair_acceptance_20261007/final_static_gates/results.json | archive/evidence/hamming_ci_repair_acceptance_20261007/final_static_gates/results.json | 08016ab60823f4235bfbc8c4e0b667d056b2741f | 3756 |
| evidence/hamming_ci_repair_acceptance_20261007/fixed_map_supplement/verification.json | archive/evidence/hamming_ci_repair_acceptance_20261007/fixed_map_supplement/verification.json | e5eecb66f8e8c7a72f5b333f31aa8cec3117afbe | 11929 |
| evidence/hamming_ci_repair_acceptance_20261007/fresh_cpp_build.json | archive/evidence/hamming_ci_repair_acceptance_20261007/fresh_cpp_build.json | eb82ae1ec09f2dbfafb42cadcc6496918c8ace43 | 17305 |
| evidence/hamming_ci_repair_acceptance_20261007/full_hamming_python312/comparison.json | archive/evidence/hamming_ci_repair_acceptance_20261007/full_hamming_python312/comparison.json | 77ccc60dc9b8f3f2fa1f31dd1cbb7e17d9fcd0c3 | 24008 |
| evidence/hamming_ci_repair_acceptance_20261007/full_hamming_python312/execution_manifest.json | archive/evidence/hamming_ci_repair_acceptance_20261007/full_hamming_python312/execution_manifest.json | 38f52c7df0e4969e82a6cab562152c78d17e0d7a | 51480 |
| evidence/hamming_ci_repair_acceptance_20261007/full_hamming_python313/comparison.json | archive/evidence/hamming_ci_repair_acceptance_20261007/full_hamming_python313/comparison.json | e91040c908af6b6015429aee57024cc02f2eb8cd | 28707 |
| evidence/hamming_ci_repair_acceptance_20261007/full_hamming_python313/execution_manifest.json | archive/evidence/hamming_ci_repair_acceptance_20261007/full_hamming_python313/execution_manifest.json | 65006c371583ceae8de7066c24c5ce98b873576f | 51469 |
| evidence/hamming_ci_repair_acceptance_20261007/independent_review/REVIEW.md | archive/evidence/hamming_ci_repair_acceptance_20261007/independent_review/REVIEW.md | 85ddd6454c7f21e9aca73a966b5e253f3225910c | 6438 |
| evidence/hamming_ci_repair_acceptance_20261007/independent_review/review_artifact_manifest.json | archive/evidence/hamming_ci_repair_acceptance_20261007/independent_review/review_artifact_manifest.json | 655582f43623c00fa5b2b764dcefc4f6c8512049 | 214853 |
| evidence/hamming_ci_repair_acceptance_20261007/maintenance_python312_normal.log | archive/evidence/hamming_ci_repair_acceptance_20261007/maintenance_python312_normal.log | 7becab76f45d67a154ddbef4aeb31742e90efc2b | 24938 |
| evidence/hamming_ci_repair_acceptance_20261007/maintenance_python312_optimized.log | archive/evidence/hamming_ci_repair_acceptance_20261007/maintenance_python312_optimized.log | 2fab47a02f8e5879615af5c34fc0530d6e7f1a83 | 24938 |
| evidence/hamming_ci_repair_acceptance_20261007/maintenance_python313_normal.log | archive/evidence/hamming_ci_repair_acceptance_20261007/maintenance_python313_normal.log | f780d8b8329f2f3c808aedbb16f4ae28acdb95a7 | 24938 |
| evidence/hamming_ci_repair_acceptance_20261007/maintenance_python313_optimized.log | archive/evidence/hamming_ci_repair_acceptance_20261007/maintenance_python313_optimized.log | 5583ecb4ff000d7a79acfecdf44769849e0cac16 | 24938 |
| evidence/hamming_ci_repair_acceptance_20261007/sibling_audit/AUDIT.md | archive/evidence/hamming_ci_repair_acceptance_20261007/sibling_audit/AUDIT.md | 39e3d1befe76bd3ab111a7887b518e7167c7d4db | 12032 |
| evidence/hamming_ci_repair_acceptance_20261007/sibling_audit/SHA256SUMS.json | archive/evidence/hamming_ci_repair_acceptance_20261007/sibling_audit/SHA256SUMS.json | 51cbc66164838bc2ab4168be4cd20996674f4f08 | 1948 |
| evidence/hamming_ci_repair_acceptance_20261007/targeted_cross_version_tests.json | archive/evidence/hamming_ci_repair_acceptance_20261007/targeted_cross_version_tests.json | eb55b2dba1863d4aacb622876db7a1666fbfc168 | 4207 |
| evidence/hamming_ci_repair_acceptance_20261007/tested_source_manifest.json | archive/evidence/hamming_ci_repair_acceptance_20261007/tested_source_manifest.json | d4a86c8fe1164cb323106ed7234ad4cd1cd54f5f | 584515 |
| evidence/hamming_ci_repair_acceptance_20261007/workspace_python313.json | archive/evidence/hamming_ci_repair_acceptance_20261007/workspace_python313.json | 0d0f4c6594b0dab2bd5fecc29c1cd11896201715 | 750921 |

### evidence/loop_reductions_20261006 -> archive/evidence/loop_reductions_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/loop_reductions_20261006/accepted_hash_receipt_curated.json | archive/evidence/loop_reductions_20261006/accepted_hash_receipt_curated.json | 7f1bf9f841233291215546083615915a7ea98f44 | 5217 |
| evidence/loop_reductions_20261006/author_deductions.md | archive/evidence/loop_reductions_20261006/author_deductions.md | d9c509fc0e2dbeeaadde1cf1b0a65750f325b021 | 6514 |
| evidence/loop_reductions_20261006/editorial_self_review.md | archive/evidence/loop_reductions_20261006/editorial_self_review.md | c649370123ed1aaf00e8b278359ee91c1850a050 | 2437 |
| evidence/loop_reductions_20261006/independent_review.md | archive/evidence/loop_reductions_20261006/independent_review.md | a8c36732cf54515d643478101e3824e29eae974e | 18541 |
| evidence/loop_reductions_20261006/input_reconciliation.json | archive/evidence/loop_reductions_20261006/input_reconciliation.json | 789090f3cff874f20653dc4cb0f452839281fbc1 | 5938 |
| evidence/loop_reductions_20261006/integrated_exact_normal.json | archive/evidence/loop_reductions_20261006/integrated_exact_normal.json | 0424568e827f2baced9986a7d7b1b0a22d5e51d4 | 329 |
| evidence/loop_reductions_20261006/integrated_exact_optimized.json | archive/evidence/loop_reductions_20261006/integrated_exact_optimized.json | 0424568e827f2baced9986a7d7b1b0a22d5e51d4 | 329 |
| evidence/loop_reductions_20261006/integrated_unit_normal.log | archive/evidence/loop_reductions_20261006/integrated_unit_normal.log | e812d1b3bbec38f2225613c74fb76d160ccf47ad | 587 |
| evidence/loop_reductions_20261006/integrated_unit_optimized.log | archive/evidence/loop_reductions_20261006/integrated_unit_optimized.log | 1098665470f1ad9a8378222c36215d185ce572db | 587 |
| evidence/loop_reductions_20261006/integration_validation.json | archive/evidence/loop_reductions_20261006/integration_validation.json | 888445e8e25f3686337b92737a621fac52d28d35 | 6014 |
| evidence/loop_reductions_20261006/prepared_editorial_mapping.json | archive/evidence/loop_reductions_20261006/prepared_editorial_mapping.json | b84e964a98c28265cd99528d7b3bbfa4ce34c523 | 903 |
| evidence/loop_reductions_20261006/prepared_exact_normal.json | archive/evidence/loop_reductions_20261006/prepared_exact_normal.json | 0424568e827f2baced9986a7d7b1b0a22d5e51d4 | 329 |
| evidence/loop_reductions_20261006/prepared_exact_optimized.json | archive/evidence/loop_reductions_20261006/prepared_exact_optimized.json | 0424568e827f2baced9986a7d7b1b0a22d5e51d4 | 329 |
| evidence/loop_reductions_20261006/prepared_unittest_normal.log | archive/evidence/loop_reductions_20261006/prepared_unittest_normal.log | b275bf8ce2c3fb9604e4218d6fa43d939c33a401 | 587 |
| evidence/loop_reductions_20261006/prepared_unittest_optimized.log | archive/evidence/loop_reductions_20261006/prepared_unittest_optimized.log | 20bbb8fd4482d812d0b2aebcc6874874b1ceaa2e | 587 |
| evidence/loop_reductions_20261006/provenance.json | archive/evidence/loop_reductions_20261006/provenance.json | 41405c60d859d90f3fa49a16dbc04b3e0ffb672c | 4353 |

### evidence/ordered_diagonal_20261006 -> archive/evidence/ordered_diagonal_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/ordered_diagonal_20261006/independent_original.json | archive/evidence/ordered_diagonal_20261006/independent_original.json | 396c567af52bad911de890fd9a023daf38193536 | 5673 |
| evidence/ordered_diagonal_20261006/original_floating_diagnostic.json | archive/evidence/ordered_diagonal_20261006/original_floating_diagnostic.json | 8d28a91ac77f1eab7511d10d6424f8135b597ee7 | 2301 |
| evidence/ordered_diagonal_20261006/promotion_receipt.json | archive/evidence/ordered_diagonal_20261006/promotion_receipt.json | b7588f51da952234a6f6592e21553c1fcbdf90e2 | 646 |

### evidence/paired_phase_20261006 -> archive/evidence/paired_phase_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/paired_phase_20261006/normal/branch_quotient.json | archive/evidence/paired_phase_20261006/normal/branch_quotient.json | 2fe56deac66a8b8cfcf347642286fbe5b086f0d3 | 2476 |
| evidence/paired_phase_20261006/normal/frostman_constants.json | archive/evidence/paired_phase_20261006/normal/frostman_constants.json | e2698ade4711cff8651739ffcc93b4752a73a244 | 4897 |
| evidence/paired_phase_20261006/normal/locality_constants.json | archive/evidence/paired_phase_20261006/normal/locality_constants.json | 1ba920d38d31e6563b45318b7bd54964bfb06647 | 4416 |
| evidence/paired_phase_20261006/normal/receipt.json | archive/evidence/paired_phase_20261006/normal/receipt.json | 6f8cd0c9b6d9d4829a50e0dcad0ddeb43a6954eb | 15843 |
| evidence/paired_phase_20261006/optimized/branch_quotient.json | archive/evidence/paired_phase_20261006/optimized/branch_quotient.json | 2fe56deac66a8b8cfcf347642286fbe5b086f0d3 | 2476 |
| evidence/paired_phase_20261006/optimized/frostman_constants.json | archive/evidence/paired_phase_20261006/optimized/frostman_constants.json | e2698ade4711cff8651739ffcc93b4752a73a244 | 4897 |
| evidence/paired_phase_20261006/optimized/locality_constants.json | archive/evidence/paired_phase_20261006/optimized/locality_constants.json | 1ba920d38d31e6563b45318b7bd54964bfb06647 | 4416 |
| evidence/paired_phase_20261006/optimized/receipt.json | archive/evidence/paired_phase_20261006/optimized/receipt.json | d5efe06259d493dadc3e9d3b7fff57fba6c6ce8d | 15840 |
| evidence/paired_phase_20261006/original/frostman_independent_results.json | archive/evidence/paired_phase_20261006/original/frostman_independent_results.json | 2f0cb783164cf328d36878d0d28287738497cae0 | 5691 |
| evidence/paired_phase_20261006/original/original_source_manifest.json | archive/evidence/paired_phase_20261006/original/original_source_manifest.json | a2d6630703e43a5d4bc952999d2d32344f1e5cfd | 2507 |
| evidence/paired_phase_20261006/original/paired_independent_results.json | archive/evidence/paired_phase_20261006/original/paired_independent_results.json | 7f8cdab1316a99d76769147a10dbb96caf37f5a5 | 8815 |
| evidence/paired_phase_20261006/original/paired_review_pins.json | archive/evidence/paired_phase_20261006/original/paired_review_pins.json | da071a8f7bef3f23e6111da8542b47113f730054 | 812 |
| evidence/paired_phase_20261006/portability_normal.log | archive/evidence/paired_phase_20261006/portability_normal.log | dcd92a540ce00549db33759576b216e53f19ef9d | 100 |
| evidence/paired_phase_20261006/portability_optimized.log | archive/evidence/paired_phase_20261006/portability_optimized.log | a1400ac44600d4859a0cf62db637f9a89c8edf14 | 100 |
| evidence/paired_phase_20261006/promotion_receipt.json | archive/evidence/paired_phase_20261006/promotion_receipt.json | aac6faab0d67a15754054a4f2f45b449f96acba7 | 972 |

### evidence/r6_repair_checkpoint_20261007 -> archive/evidence/r6_repair_checkpoint_20261007

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/r6_repair_checkpoint_20261007/bgs_checked_checkpoint_validation/cpp_build_summary.log.envelope.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_checked_checkpoint_validation/cpp_build_summary.log.envelope.json | d63ece69af57b653a5cdeec87bf2d51d079bf25e | 311 |
| evidence/r6_repair_checkpoint_20261007/bgs_checked_checkpoint_validation/fresh_cpp_build.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_checked_checkpoint_validation/fresh_cpp_build.json | 367d33b89f723e37577129448aec5cf33b56fe41 | 16617 |
| evidence/r6_repair_checkpoint_20261007/bgs_checked_checkpoint_validation/lean.log.envelope.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_checked_checkpoint_validation/lean.log.envelope.json | e993630c249ceed60028874dab55b808ee5ac6b9 | 18157 |
| evidence/r6_repair_checkpoint_20261007/bgs_checked_checkpoint_validation/lean_build_receipt.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_checked_checkpoint_validation/lean_build_receipt.json | a36318f7fdf0da14e57fdf0ac88299ad284af444 | 5011 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/ARITHMETIC_REPAIR_REPORT.md | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/ARITHMETIC_REPAIR_REPORT.md | af31e560c6bf9ca763c7cb02a850a26c677257dc | 9798 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/arithmetic_repair.patch | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/arithmetic_repair.patch | eb6876058f1fd19e3326a28f9999dbc96c014ab9 | 28572 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/baseline_contract_control.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/baseline_contract_control.json | 699214b91bbd3d8e3d53b0d6ee757ebf7c50f4c4 | 726 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/before.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/before.json | e66191880485bb80b1d2949413a38fa3994b8145 | 394 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/bounded_coverage.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/bounded_coverage.json | 79f4e26359ffacd1c8bfd5f645d5bd72203d3097 | 1597 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/cpp_build_receipt.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/cpp_build_receipt.json | cf6ae39827495f8d945d791360581f5b8217ccbe | 696 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/execution_receipt.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/execution_receipt.json | 4ad28280b056009e8e994501e9378041d9b3a343 | 12818 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/python3.12_normal_after.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/python3.12_normal_after.json | ed1af72410b1ecaddd7405ed06bf9e448a10db72 | 2061 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/python3.12_optimized_after.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/python3.12_optimized_after.json | 1b1b5c8707c59d7b1dd8c7a0dc36d1f4bfba7c2c | 2060 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/python3.13_normal_after.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/python3.13_normal_after.json | 7f955838f93e377380cdf158db23ca8d5fd8235a | 2057 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/python3.13_optimized_after.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/python3.13_optimized_after.json | 5d55f089db684bcf69b147f8db51f0e346aa6027 | 2056 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/repair_manifest.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/repair_manifest.json | a5591f6250083c6d0eb78a5cbd52d44d59951dc6 | 2790 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/supplementary_receipt.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_arithmetic_repair/supplementary_receipt.json | 61b024c7d7443c191d9e246a0df1dafb1d1e44b6 | 8565 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_independent_review/REVIEW.md | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_independent_review/REVIEW.md | 8bc9a6d3a26d6c9538543ae392fc18e800f2f867 | 8832 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_independent_review/final_seal.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_independent_review/final_seal.json | bc71fc2d239385ccd0a80b493ef613f92626c2a7 | 2628 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/stale_noop_baseline_and_repair.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/stale_noop_baseline_and_repair.json | 427f07775f9aa702bf19e21e58defc71dc75d0b0 | 7945 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/execution.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/execution.json | 776ef5751152a5346a2fa32bd05f7554bfb6bda6 | 1745 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal.json | 642986ed65ec9da81eb8a4bf83ccd8c9034c3bbd | 8714 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal.log | e17c52df50542abc6d1d6ddf7e8e6f5c465ba3a3 | 142 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/actual.json | e5b6b80854d8ffbad07383a0f3a3a15ba6a065b2 | 78048 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/expected.json | e5b6b80854d8ffbad07383a0f3a3a15ba6a065b2 | 78048 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/inputs.json | b760aee020a3b758635c1be9a7d6083d4165d03b | 530 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/process.json | 1250f412b07620d9b3f631d49d93be8a7382d0b2 | 469 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/stdout.log | 549c8913f25d598e6b4a5826dc6741dfdcbf3a66 | 177 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/0/step.json | 138d9dbe1d9b84978d618e31449c097df6056713 | 320 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/actual.json | e0a9d1d619996800b33cc7487e00684c550f3fc3 | 110787 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/expected.json | b71e0e44abbea3d56798235daf03bc02d0b69ae3 | 110788 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/inputs.json | 0d502ca0f2f4cf2474c7576b6dc7a310cb77db80 | 524 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/process.json | 702de4d98148ef45077f4a618783cf88c4ed79ff | 473 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/stdout.log | dffefc8ffebd9cffafa9b4400afc617c088259ad | 748 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/1/step.json | 874a1ad53c16aea2862d571c5b295065720672f2 | 340 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/actual.json | ace5f479e719045893b1ac8a0626822c9b228bca | 32320 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/expected.json | 3b3a5d4107828be4a0d75faf2201e7311911893d | 32321 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/inputs.json | e06829e00819e703fd1d491a70588789f6e0b507 | 700 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/process.json | a99e275ea1efe72fe506f660a04cfee73baa7157 | 469 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/stdout.log | 17748d782bfd05eb95ac60d0339ca73815f4ab9b | 242 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/2/step.json | ca9d1b6096c3ab2e7b3d4ffde565167643f8cd85 | 324 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/actual.json | 31684e23e264d25da47b7d111d8d5f03387fc03b | 2271 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/expected.json | 3d7746768d05395600f14873b91115bfe14aa43e | 2270 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/inputs.json | e06829e00819e703fd1d491a70588789f6e0b507 | 700 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/process.json | 7adbb7eb9580715c632d3e558deefb4aa507c37c | 473 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/stdout.log | 4471d767f818d5f6d61432aaf95e6fb1bd891aaf | 64 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/3/step.json | 6e52f6853755ca972690075ac9b50d576da38caa | 364 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/actual.json | 96dc3802bbc45ea498faffc2cc245b78519bbe70 | 186904 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/expected.json | d60c9575f3f0af7cdb3f8a4d651c370c328b2467 | 186903 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/inputs.json | ad6b436a00c55be40db017d94f947142cbc53315 | 402 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/process.json | 37aee94f58d764e688141cf80d1fc5596a3c2f72 | 475 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/stdout.log | 181e3fde4b8fbb634b4021a6fdb0c11bb5914a66 | 269 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/4/step.json | 9c2a2c63d61125cb9d8b89dd77f2529e64906016 | 327 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/actual.json | 3343c48c01134944cadfb358edca40eadffd2d0e | 22590 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/expected.json | a629ff57ec0d2d8d8e18ebcd6b41ce4ce824cb8f | 22591 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/inputs.json | f1052bfb844d80e7b0a44e5addb0ee768ffe57f6 | 403 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/process.json | ed7d7884dd1d5555b93e4faf630b843af4c937fc | 474 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/stdout.log | 37dbc255c88d56714e27529918655c3743fbf84f | 111 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/normal_outputs/5/step.json | 0b978fad15028d457b57a5720e90add3a4cd826b | 321 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized.json | 8bfb8d7aa55e04c69d76a8fdefd1d8f81a91f9c1 | 8716 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized.log | e17c52df50542abc6d1d6ddf7e8e6f5c465ba3a3 | 142 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/actual.json | e5b6b80854d8ffbad07383a0f3a3a15ba6a065b2 | 78048 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/expected.json | e5b6b80854d8ffbad07383a0f3a3a15ba6a065b2 | 78048 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/inputs.json | b760aee020a3b758635c1be9a7d6083d4165d03b | 530 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/process.json | c592176d6b28f39933345affd5642fff410d3864 | 479 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/stdout.log | 549c8913f25d598e6b4a5826dc6741dfdcbf3a66 | 177 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/0/step.json | 138d9dbe1d9b84978d618e31449c097df6056713 | 320 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/actual.json | cae14f8d86d953c5ca151bb6c40250332fad335a | 110788 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/expected.json | b71e0e44abbea3d56798235daf03bc02d0b69ae3 | 110788 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/inputs.json | 0d502ca0f2f4cf2474c7576b6dc7a310cb77db80 | 524 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/process.json | 1a8915b86da1f014171f9802aafc2743b2ee5fe9 | 483 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/stdout.log | f37afc59235af6b3c789230f2105ac2d6841282d | 749 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/1/step.json | 874a1ad53c16aea2862d571c5b295065720672f2 | 340 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/actual.json | f724a510973347721f65763fbc01600d727674cb | 32320 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/expected.json | 3b3a5d4107828be4a0d75faf2201e7311911893d | 32321 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/inputs.json | e06829e00819e703fd1d491a70588789f6e0b507 | 700 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/process.json | db251e484547efcc7d654cbda20ed91834e2c137 | 479 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/stdout.log | d6a216bf9d07cfcf3b2710d896515945573ba00c | 242 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/2/step.json | ca9d1b6096c3ab2e7b3d4ffde565167643f8cd85 | 324 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/actual.json | f6e3e9ac6ad5a07f8728a5fbdfad9813cf4294f5 | 2270 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/expected.json | 3d7746768d05395600f14873b91115bfe14aa43e | 2270 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/inputs.json | e06829e00819e703fd1d491a70588789f6e0b507 | 700 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/process.json | f7f062c0754907d479d96fd20a569adb4aad7ed2 | 483 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/stdout.log | 83ee09a042f5b4b63e47031020e408b19bc59590 | 63 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/3/step.json | 6e52f6853755ca972690075ac9b50d576da38caa | 364 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/actual.json | b0d27cd345efa87623f0a57eb41c2d96c7345336 | 186903 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/expected.json | d60c9575f3f0af7cdb3f8a4d651c370c328b2467 | 186903 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/inputs.json | ad6b436a00c55be40db017d94f947142cbc53315 | 402 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/process.json | 044c54ba4ff8b366dbb011b26534670b317a7f36 | 485 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/stdout.log | 1d82d7498b1448349a92acb4a971b4fc6d8c138a | 268 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/4/step.json | 9c2a2c63d61125cb9d8b89dd77f2529e64906016 | 327 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/actual.json | ba54b29df78e133c05d6dee5b26971762591b8d9 | 22589 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/expected.json | a629ff57ec0d2d8d8e18ebcd6b41ce4ce824cb8f | 22591 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/inputs.json | f1052bfb844d80e7b0a44e5addb0ee768ffe57f6 | 403 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/process.json | 3dc2b31789f02c45dd0226adb1b4087bf484b05f | 484 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/stdout.log | 5703813026dd914fe5523c7ba543c826a2cbb360 | 110 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/optimized_outputs/5/step.json | 0b978fad15028d457b57a5720e90add3a4cd826b | 321 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313.json | 841ce10722de9105b901551e8353a2e1d3c193a8 | 8715 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313.log | e17c52df50542abc6d1d6ddf7e8e6f5c465ba3a3 | 142 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized.json | e563842c6905f41a1df0310b9546e1be23931de4 | 8724 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized.log | e17c52df50542abc6d1d6ddf7e8e6f5c465ba3a3 | 142 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/actual.json | e5b6b80854d8ffbad07383a0f3a3a15ba6a065b2 | 78048 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/expected.json | e5b6b80854d8ffbad07383a0f3a3a15ba6a065b2 | 78048 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/inputs.json | b760aee020a3b758635c1be9a7d6083d4165d03b | 530 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/process.json | 8245046c34666b9c0ebff2bdcc5689b91f1b2426 | 425 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/stdout.log | 549c8913f25d598e6b4a5826dc6741dfdcbf3a66 | 177 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/0/step.json | 138d9dbe1d9b84978d618e31449c097df6056713 | 320 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/actual.json | d282d9605a783e1ad154be4d21a8ee75bbbc42fd | 110788 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/expected.json | b71e0e44abbea3d56798235daf03bc02d0b69ae3 | 110788 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/inputs.json | 0d502ca0f2f4cf2474c7576b6dc7a310cb77db80 | 524 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/process.json | c99cf821cf6c65507351bcfb27e73343914b73cf | 429 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/stdout.log | 54f8e71c855271d7e86aaf02de93736c2a29d2dc | 749 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/1/step.json | 874a1ad53c16aea2862d571c5b295065720672f2 | 340 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/actual.json | 0343817a3af08aeb74632d699b7da1a6e4210ef2 | 32320 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/expected.json | 3b3a5d4107828be4a0d75faf2201e7311911893d | 32321 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/inputs.json | e06829e00819e703fd1d491a70588789f6e0b507 | 700 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/process.json | 47da92f13351106392e15ae8f87ff769936a574b | 425 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/stdout.log | 73253d21b1b3c9281dc20a76006bc0e85b3bc57d | 243 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/2/step.json | ca9d1b6096c3ab2e7b3d4ffde565167643f8cd85 | 324 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/actual.json | e7bac6ad924c2af96c1b9508b65b9b0e96c5636e | 2271 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/expected.json | 3d7746768d05395600f14873b91115bfe14aa43e | 2270 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/inputs.json | e06829e00819e703fd1d491a70588789f6e0b507 | 700 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/process.json | c155831dedc0f453914379b90f96c47264f4a7f1 | 430 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/stdout.log | be914a5893df2a0ec5126ea18502d6887c807d55 | 64 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/3/step.json | 6e52f6853755ca972690075ac9b50d576da38caa | 364 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/actual.json | d692344b16a1bb483aec2b0d0bb9109bb684682a | 186902 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/expected.json | d60c9575f3f0af7cdb3f8a4d651c370c328b2467 | 186903 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/inputs.json | ad6b436a00c55be40db017d94f947142cbc53315 | 402 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/process.json | 0a3be81959028d5a194c21004c917d41a2fc6ab6 | 431 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/stdout.log | 7e80801923945df9ecab628ce555e378ed6d5fd8 | 269 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/4/step.json | 9c2a2c63d61125cb9d8b89dd77f2529e64906016 | 327 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/actual.json | 165c316d24d85405a6d1dafd715a6124ca7ebd94 | 22589 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/expected.json | a629ff57ec0d2d8d8e18ebcd6b41ce4ce824cb8f | 22591 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/inputs.json | f1052bfb844d80e7b0a44e5addb0ee768ffe57f6 | 403 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/process.json | b9f4bfab2e159f7f60360093f3f0192a49223eeb | 430 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/stdout.log | 8c3236ea77ca4a9b0f4ff3c0e6d36d06fcf50ba0 | 111 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_optimized_outputs/5/step.json | 0b978fad15028d457b57a5720e90add3a4cd826b | 321 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/actual.json | e5b6b80854d8ffbad07383a0f3a3a15ba6a065b2 | 78048 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/expected.json | e5b6b80854d8ffbad07383a0f3a3a15ba6a065b2 | 78048 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/inputs.json | b760aee020a3b758635c1be9a7d6083d4165d03b | 530 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/process.json | 97f34d2a7fe6afcc0cef11ff8d9bfa1c3ca8be26 | 414 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/stdout.log | 549c8913f25d598e6b4a5826dc6741dfdcbf3a66 | 177 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/0/step.json | 138d9dbe1d9b84978d618e31449c097df6056713 | 320 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/actual.json | 92bc264e6bb318ee5dc50a001dc8099fc1ddf19a | 110788 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/expected.json | b71e0e44abbea3d56798235daf03bc02d0b69ae3 | 110788 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/inputs.json | 0d502ca0f2f4cf2474c7576b6dc7a310cb77db80 | 524 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/process.json | 256db33db7b8f0ed2a9435ef4d4716f565b294db | 419 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/stdout.log | 1c17eddabb08a02c8ab97b98965937293b90de0b | 749 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/1/step.json | 874a1ad53c16aea2862d571c5b295065720672f2 | 340 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/actual.json | dcc59065816c7a2aaf4208be06cd78bbb8609761 | 32320 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/expected.json | 3b3a5d4107828be4a0d75faf2201e7311911893d | 32321 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/inputs.json | e06829e00819e703fd1d491a70588789f6e0b507 | 700 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/process.json | dd6880569bd67a2edc3f261e4d4439ec35296e88 | 416 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/stdout.log | 1e569bf25b6d8cf90239a2882dd694426ea278d5 | 243 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/2/step.json | ca9d1b6096c3ab2e7b3d4ffde565167643f8cd85 | 324 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/actual.json | f8f7b06a3a391662ecbacf2df0634a41d465d499 | 2270 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/expected.json | 3d7746768d05395600f14873b91115bfe14aa43e | 2270 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/inputs.json | e06829e00819e703fd1d491a70588789f6e0b507 | 700 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/process.json | 6618c5472af45a9d7ebc3c21d6a86e9835e26192 | 419 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/stdout.log | 5ac14498f38864da05009e5de09656a102e682e9 | 63 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/3/step.json | 6e52f6853755ca972690075ac9b50d576da38caa | 364 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/actual.json | fa3ac200ec42cce40fdbff1695cd04b5f9727b97 | 186902 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/expected.json | d60c9575f3f0af7cdb3f8a4d651c370c328b2467 | 186903 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/inputs.json | ad6b436a00c55be40db017d94f947142cbc53315 | 402 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/process.json | 7f5f3cca8d73036225a782488d2549d69a06e40a | 421 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/stdout.log | e1afe3325494e32681c6106ba3a50847efa71bcf | 268 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/4/step.json | 9c2a2c63d61125cb9d8b89dd77f2529e64906016 | 327 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/actual.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/actual.json | fc4517b9073b076d9f6ffe8976f66f1fb56f4c50 | 22589 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/expected.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/expected.json | a629ff57ec0d2d8d8e18ebcd6b41ce4ce824cb8f | 22591 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/inputs.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/inputs.json | f1052bfb844d80e7b0a44e5addb0ee768ffe57f6 | 403 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/process.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/process.json | 0f62eaea9435a3b94eb02b54593f2e9c1b91140c | 421 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/stderr.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/stderr.log | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | 0 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/stdout.log | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/stdout.log | ea56d977f74fcebf667b5242f25788a8bf47039f | 111 |
| evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/step.json | archive/evidence/r6_repair_checkpoint_20261007/bgs_r6_replay_repair/v3/python313_outputs/5/step.json | 0b978fad15028d457b57a5720e90add3a4cd826b | 321 |

### evidence/ramified_first_seven_20261006 -> archive/evidence/ramified_first_seven_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/ramified_first_seven_20261006/final_normal.json | archive/evidence/ramified_first_seven_20261006/final_normal.json | 613f4954fa1c0437b599561d723b0e0977748d6d | 10965 |
| evidence/ramified_first_seven_20261006/final_optimized.json | archive/evidence/ramified_first_seven_20261006/final_optimized.json | a5558bf46f110273c1e68fd02d8d3e2625575405 | 10964 |
| evidence/ramified_first_seven_20261006/final_portability_normal.log | archive/evidence/ramified_first_seven_20261006/final_portability_normal.log | bbd0161787f3ad793b453489fcb4f8f631543513 | 101 |
| evidence/ramified_first_seven_20261006/final_portability_optimized.log | archive/evidence/ramified_first_seven_20261006/final_portability_optimized.log | 160a348b3e39669c11b87bfd8b90fb8d553810c5 | 101 |
| evidence/ramified_first_seven_20261006/metadata_clarification.json | archive/evidence/ramified_first_seven_20261006/metadata_clarification.json | 71e0d6ae57e6c6f3f70ad5a2521d142446fa4882 | 556 |
| evidence/ramified_first_seven_20261006/original/candidate_manifest.json | archive/evidence/ramified_first_seven_20261006/original/candidate_manifest.json | 46b3c54ebf3e7520fbc380c3223fff01819b03d1 | 904 |
| evidence/ramified_first_seven_20261006/original/computation_manifest.json | archive/evidence/ramified_first_seven_20261006/original/computation_manifest.json | 95b7729f596d1c384194a4e6327103eed895b940 | 4091 |
| evidence/ramified_first_seven_20261006/original/independent_check.log | archive/evidence/ramified_first_seven_20261006/original/independent_check.log | da3cadf03885a40522fb1a9010131b630545912f | 268 |
| evidence/ramified_first_seven_20261006/original/independent_results.json | archive/evidence/ramified_first_seven_20261006/original/independent_results.json | c1c5e4e4cb4315da62001624dd3558e679bab38b | 11208 |
| evidence/ramified_first_seven_20261006/original/review_manifest.json | archive/evidence/ramified_first_seven_20261006/original/review_manifest.json | 0c67dd757ed4cbd0f158ae19531388b71176fdcf | 1369 |
| evidence/ramified_first_seven_20261006/promotion_receipt.json | archive/evidence/ramified_first_seven_20261006/promotion_receipt.json | 3e5cba332c7dce7eef5ee296e4ae6e9b78a668c0 | 1235 |

### evidence/ramified_higher_20261006 -> archive/evidence/ramified_higher_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/ramified_higher_20261006/normal/bases_results.json | archive/evidence/ramified_higher_20261006/normal/bases_results.json | ec01782b91f3bef8c073253421a995fc1de64426 | 9619 |
| evidence/ramified_higher_20261006/normal/dictionary_results.json | archive/evidence/ramified_higher_20261006/normal/dictionary_results.json | be89775ec56d0013f171c94635a1a033cfba24cf | 1207 |
| evidence/ramified_higher_20261006/normal/grades_results.json | archive/evidence/ramified_higher_20261006/normal/grades_results.json | f73acc7a6a17c983c1d3b32b50b10f1e812ac9da | 1362 |
| evidence/ramified_higher_20261006/normal/poles_results.json | archive/evidence/ramified_higher_20261006/normal/poles_results.json | 5f66c22fed886345533a9be54947486c970a18f5 | 1061 |
| evidence/ramified_higher_20261006/normal/receipt.json | archive/evidence/ramified_higher_20261006/normal/receipt.json | 218fb8051981794c3f6e682f7cd64706bcf8a4d5 | 3914 |
| evidence/ramified_higher_20261006/normal/unit_bases_results.json | archive/evidence/ramified_higher_20261006/normal/unit_bases_results.json | f61a73a7d69a1a0e703b6dd5515dbeb85a80e1db | 9630 |
| evidence/ramified_higher_20261006/optimized/bases_results.json | archive/evidence/ramified_higher_20261006/optimized/bases_results.json | 09239d715ee45c9f5aaec86c32d5a6ce633e3b85 | 9619 |
| evidence/ramified_higher_20261006/optimized/dictionary_results.json | archive/evidence/ramified_higher_20261006/optimized/dictionary_results.json | e65483d17633697da568c1650b40c3717607dcc7 | 1205 |
| evidence/ramified_higher_20261006/optimized/grades_results.json | archive/evidence/ramified_higher_20261006/optimized/grades_results.json | 2021aa8c151bb668469405b6fa10b2f9e82460c6 | 1362 |
| evidence/ramified_higher_20261006/optimized/poles_results.json | archive/evidence/ramified_higher_20261006/optimized/poles_results.json | 3ec1c7fce254aa572200beaf9a4f4f90246c0260 | 1061 |
| evidence/ramified_higher_20261006/optimized/receipt.json | archive/evidence/ramified_higher_20261006/optimized/receipt.json | ac38cc4cbecfde9fde7dd0c11844a4457b80fcae | 3998 |
| evidence/ramified_higher_20261006/optimized/unit_bases_results.json | archive/evidence/ramified_higher_20261006/optimized/unit_bases_results.json | 0bd4136175aa1e6f152fd4efb703eeabb705e069 | 9630 |
| evidence/ramified_higher_20261006/original/bases_results.json | archive/evidence/ramified_higher_20261006/original/bases_results.json | 407d2c43e06b61b7e5414e0011ad4d3d2a173208 | 9498 |
| evidence/ramified_higher_20261006/original/candidate_manifest_v2.json | archive/evidence/ramified_higher_20261006/original/candidate_manifest_v2.json | 7bd3adb30b79289ee71d5f9ead76ff7465ab2b7b | 1560 |
| evidence/ramified_higher_20261006/original/dictionary_results.json | archive/evidence/ramified_higher_20261006/original/dictionary_results.json | b732ea336370bf1cfd14cbdbf839db69988a5874 | 1086 |
| evidence/ramified_higher_20261006/original/execution_manifest.json | archive/evidence/ramified_higher_20261006/original/execution_manifest.json | c35b42caf658e502c610da5be09cea60a7967578 | 13519 |
| evidence/ramified_higher_20261006/original/grades_results.json | archive/evidence/ramified_higher_20261006/original/grades_results.json | 926ef2f5b7ba684d24b60d5cf78a46543dd90a4a | 1241 |
| evidence/ramified_higher_20261006/original/manifest_validation.log | archive/evidence/ramified_higher_20261006/original/manifest_validation.log | aeb8cf9a639916db0e9526035a72b5d0cc99f3e7 | 67 |
| evidence/ramified_higher_20261006/original/poles_results.json | archive/evidence/ramified_higher_20261006/original/poles_results.json | f175355208fcb474822cdd45fb4e644bcbbc6b70 | 940 |
| evidence/ramified_higher_20261006/original/review_manifest.json | archive/evidence/ramified_higher_20261006/original/review_manifest.json | c0e0d48093114bf03039ad01d09d457868b57ac8 | 5275 |
| evidence/ramified_higher_20261006/original/run_checks.log | archive/evidence/ramified_higher_20261006/original/run_checks.log | 664b935164d79cb57047b62d8cf411fba6d9edc7 | 344 |
| evidence/ramified_higher_20261006/original/unit_bases_results.json | archive/evidence/ramified_higher_20261006/original/unit_bases_results.json | 3d7011c2bacfe259dd90fbd39df653bd162fc491 | 9510 |
| evidence/ramified_higher_20261006/portability_normal.log | archive/evidence/ramified_higher_20261006/portability_normal.log | 403725899722c18e86c796d53702aa1c507dedca | 101 |
| evidence/ramified_higher_20261006/portability_optimized.log | archive/evidence/ramified_higher_20261006/portability_optimized.log | 1ecda141d33ebc5b28ea8885b5b06abfd2b8f685 | 101 |
| evidence/ramified_higher_20261006/promotion_receipt.json | archive/evidence/ramified_higher_20261006/promotion_receipt.json | cff602ac1a9009ce4cff81c80facd7e6a9e31e8e | 1006 |

### evidence/recovery_20260920 -> archive/evidence/recovery_20260920

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/recovery_20260920/compensated_trace_window.json | archive/evidence/recovery_20260920/compensated_trace_window.json | b178d808b4aed3f72297b4f3ffcde8336e5fe07c | 15723 |
| evidence/recovery_20260920/elliptic_regression.log | archive/evidence/recovery_20260920/elliptic_regression.log | e1b252b05c90786f0d49317854d11cb612f90274 | 139 |
| evidence/recovery_20260920/mixed_loop_replay.json | archive/evidence/recovery_20260920/mixed_loop_replay.json | fa260131af664d7c22f39c5ac72b9f59833f6ac3 | 1222 |
| evidence/recovery_20260920/recovery_manifest.json | archive/evidence/recovery_20260920/recovery_manifest.json | 19697880e49f76541e6a381c1da2ecb8ffe789ed | 4080 |
| evidence/recovery_20260920/runs/resolvent-flow__checks/execution.log | archive/evidence/recovery_20260920/runs/resolvent-flow__checks/execution.log | 884fb3ac7458c0dd2306e38a9138a651eadd4ae5 | 395 |
| evidence/recovery_20260920/runs/resolvent-flow__low_order/execution.log | archive/evidence/recovery_20260920/runs/resolvent-flow__low_order/execution.log | b34b84fba3b9b737311437103650abeee4683b7c | 72 |

### evidence/recovery_20260921 -> archive/evidence/recovery_20260921

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/recovery_20260921/replay_summary.json | archive/evidence/recovery_20260921/replay_summary.json | 4857c94d6082b95b10434506c63a8296ff3ca2a4 | 2303 |

### evidence/research_checkpoint_protocol_20261007 -> archive/evidence/research_checkpoint_protocol_20261007

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/research_checkpoint_protocol_20261007/checkpoint_gaps_normal.json | archive/evidence/research_checkpoint_protocol_20261007/checkpoint_gaps_normal.json | 9e8feeb074cfc3888c73ad91c8e685eb89cecc6d | 745 |
| evidence/research_checkpoint_protocol_20261007/checkpoint_gaps_optimized.json | archive/evidence/research_checkpoint_protocol_20261007/checkpoint_gaps_optimized.json | 1419d1da431209f161d0ab49f6262e6c4667938d | 745 |
| evidence/research_checkpoint_protocol_20261007/checkpoint_repair_regression_normal.json | archive/evidence/research_checkpoint_protocol_20261007/checkpoint_repair_regression_normal.json | b10810e64fd3468d2f5e2a551d060fd3325feee3 | 1232 |
| evidence/research_checkpoint_protocol_20261007/checkpoint_repair_regression_optimized.json | archive/evidence/research_checkpoint_protocol_20261007/checkpoint_repair_regression_optimized.json | aec532d9890add66be95b150d9c120ab96d185f1 | 1232 |
| evidence/research_checkpoint_protocol_20261007/maintenance_normal.stderr.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/maintenance_normal.stderr.envelope.json | 1d2ed542b1a010c7b12d696912884bb9df3a756a | 3386 |
| evidence/research_checkpoint_protocol_20261007/maintenance_normal.stdout.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/maintenance_normal.stdout.envelope.json | 5deb2d170ce149b17d43ff1050b2f69045e87dec | 243 |
| evidence/research_checkpoint_protocol_20261007/maintenance_optimized.stderr.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/maintenance_optimized.stderr.envelope.json | 32e53df449867ca57070d5b923dbc14ca20befc4 | 3389 |
| evidence/research_checkpoint_protocol_20261007/maintenance_optimized.stdout.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/maintenance_optimized.stdout.envelope.json | 8a84faa2c4f9655b4566f60a464f789698a91568 | 246 |
| evidence/research_checkpoint_protocol_20261007/maintenance_py313_normal.stderr.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/maintenance_py313_normal.stderr.envelope.json | 56c8f4b1cd26c570fb0e31373d30dfe4dab905f9 | 3392 |
| evidence/research_checkpoint_protocol_20261007/maintenance_py313_normal.stdout.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/maintenance_py313_normal.stdout.envelope.json | 68f400305a6c9abbfd7f8f983db42b68edd27001 | 249 |
| evidence/research_checkpoint_protocol_20261007/maintenance_py313_optimized.stderr.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/maintenance_py313_optimized.stderr.envelope.json | 088413c37091637dd7af8eb29206f7f0eeab8ec7 | 3395 |
| evidence/research_checkpoint_protocol_20261007/maintenance_py313_optimized.stdout.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/maintenance_py313_optimized.stdout.envelope.json | 8a4bcee3f16292f04d18536432e028dac4c6acd8 | 252 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/cft_actual_freshness.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/cft_actual_freshness.json | d2fb24e8c08a8f8edd1242d67f7b841391ff09b4 | 3085 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/charge_pyc_normal.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/charge_pyc_normal.json | 729dc66469ef5778769fb781e674b0a8433f16cb | 474 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/charge_pyc_optimized.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/charge_pyc_optimized.json | fc0042a32c94b455b40ed3844a1a829436950208 | 474 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/checkpoint_gaps_normal.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/checkpoint_gaps_normal.json | 9e8feeb074cfc3888c73ad91c8e685eb89cecc6d | 745 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/checkpoint_gaps_optimized.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/checkpoint_gaps_optimized.json | 1419d1da431209f161d0ab49f6262e6c4667938d | 745 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/checkpoint_repair_regression_normal.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/checkpoint_repair_regression_normal.json | b10810e64fd3468d2f5e2a551d060fd3325feee3 | 1232 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/checkpoint_repair_regression_optimized.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/checkpoint_repair_regression_optimized.json | aec532d9890add66be95b150d9c120ab96d185f1 | 1232 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/schur_repair_regression_normal.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/schur_repair_regression_normal.json | d4acadfa37a1c9150e6724f4bfbe7e60bbf4b287 | 485 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/schur_repair_regression_optimized.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/schur_repair_regression_optimized.json | e907e25c4c1b2b5ba935638f8df2a507c3b6ba1f | 485 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/schur_stale_normal.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/schur_stale_normal.json | 03dc01a44f5a28b6c1d91aaad5f20ac1880d03c3 | 342 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/schur_stale_optimized.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/schur_stale_optimized.json | 3176e337a9b56afb08a5b8e608a3bf9665609fbe | 342 |
| evidence/research_checkpoint_protocol_20261007/partial_source_review/source_identity_pre_freeze.json | archive/evidence/research_checkpoint_protocol_20261007/partial_source_review/source_identity_pre_freeze.json | f68ef830f94890b967f893bd57917a31b58f5f84 | 488371 |
| evidence/research_checkpoint_protocol_20261007/receipt.json | archive/evidence/research_checkpoint_protocol_20261007/receipt.json | 3ed325a2cb608157216624f4f6b3ccdc17deb1de | 7724 |
| evidence/research_checkpoint_protocol_20261007/replay_v2_normal.stderr.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/replay_v2_normal.stderr.envelope.json | 795cf27945308795da26e432feae7da91f99b803 | 241 |
| evidence/research_checkpoint_protocol_20261007/replay_v2_normal.stdout.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/replay_v2_normal.stdout.envelope.json | 13447b5e74881515d85af57b5b4f5847b187850e | 241 |
| evidence/research_checkpoint_protocol_20261007/replay_v2_py313_optimized.stderr.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/replay_v2_py313_optimized.stderr.envelope.json | fbe61632750ff7e387db9b88a475301fac9bc0eb | 250 |
| evidence/research_checkpoint_protocol_20261007/replay_v2_py313_optimized.stdout.envelope.json | archive/evidence/research_checkpoint_protocol_20261007/replay_v2_py313_optimized.stdout.envelope.json | 3f51f068696e419f3dc2847dd4a868f0e650604b | 250 |
| evidence/research_checkpoint_protocol_20261007/reproduce_checkpoint_gaps.py | archive/evidence/research_checkpoint_protocol_20261007/reproduce_checkpoint_gaps.py | b9c46eb5f0a9755efbc69da66c1ac2f6cca2adfc | 4622 |
| evidence/research_checkpoint_protocol_20261007/reproduce_schur_stale.py | archive/evidence/research_checkpoint_protocol_20261007/reproduce_schur_stale.py | 6cccdef1b77cbdc1294d13705158419de6328307 | 1871 |
| evidence/research_checkpoint_protocol_20261007/schur_stale_normal.json | archive/evidence/research_checkpoint_protocol_20261007/schur_stale_normal.json | 03dc01a44f5a28b6c1d91aaad5f20ac1880d03c3 | 342 |
| evidence/research_checkpoint_protocol_20261007/schur_stale_optimized.json | archive/evidence/research_checkpoint_protocol_20261007/schur_stale_optimized.json | 3176e337a9b56afb08a5b8e608a3bf9665609fbe | 342 |

### evidence/schur_replay_freshness_20261007 -> archive/evidence/schur_replay_freshness_20261007

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/schur_replay_freshness_20261007/checks/manifest312_validation.log | archive/evidence/schur_replay_freshness_20261007/checks/manifest312_validation.log | aeb8cf9a639916db0e9526035a72b5d0cc99f3e7 | 67 |
| evidence/schur_replay_freshness_20261007/checks/manifest313_validation.log | archive/evidence/schur_replay_freshness_20261007/checks/manifest313_validation.log | aeb8cf9a639916db0e9526035a72b5d0cc99f3e7 | 67 |
| evidence/schur_replay_freshness_20261007/checks/portability_normal.log | archive/evidence/schur_replay_freshness_20261007/checks/portability_normal.log | e9cd3162da3a47da8378d33aa43e3021434b7fb2 | 1337 |
| evidence/schur_replay_freshness_20261007/checks/portability_optimized.log | archive/evidence/schur_replay_freshness_20261007/checks/portability_optimized.log | a856464486e2d393787773eae61cdd53e6381b8e | 1337 |
| evidence/schur_replay_freshness_20261007/checks/portability_python313_normal.log | archive/evidence/schur_replay_freshness_20261007/checks/portability_python313_normal.log | 042622689314abc8ba3e5a453906db5a24da7853 | 1337 |
| evidence/schur_replay_freshness_20261007/checks/portability_python313_optimized.log | archive/evidence/schur_replay_freshness_20261007/checks/portability_python313_optimized.log | 10275a87ee61ce7b71a7c0874d100f71451be5d4 | 1337 |
| evidence/schur_replay_freshness_20261007/checks/tests_normal.log | archive/evidence/schur_replay_freshness_20261007/checks/tests_normal.log | e866eac0f0527fe77c4bf0202c4bc4f62238fa7e | 2195 |
| evidence/schur_replay_freshness_20261007/checks/tests_optimized.log | archive/evidence/schur_replay_freshness_20261007/checks/tests_optimized.log | 1df80a40e99d49f47c16f194cf163b3d4ad6f3c6 | 2195 |
| evidence/schur_replay_freshness_20261007/checks/tests_python313_normal.log | archive/evidence/schur_replay_freshness_20261007/checks/tests_python313_normal.log | db9f0dd0da028f05297af819e99957122ed3d6b7 | 2195 |
| evidence/schur_replay_freshness_20261007/checks/tests_python313_optimized.log | archive/evidence/schur_replay_freshness_20261007/checks/tests_python313_optimized.log | 66e751522476b7d913fdad8e384ecc361657d942 | 2195 |
| evidence/schur_replay_freshness_20261007/final_hash_manifest.json | archive/evidence/schur_replay_freshness_20261007/final_hash_manifest.json | ef35d0ee72a86df92627c672328236556c1ec485 | 5148 |
| evidence/schur_replay_freshness_20261007/independent_review_regression_normal.json | archive/evidence/schur_replay_freshness_20261007/independent_review_regression_normal.json | d4acadfa37a1c9150e6724f4bfbe7e60bbf4b287 | 485 |
| evidence/schur_replay_freshness_20261007/independent_review_regression_optimized.json | archive/evidence/schur_replay_freshness_20261007/independent_review_regression_optimized.json | e907e25c4c1b2b5ba935638f8df2a507c3b6ba1f | 485 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/author_normal.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/author_normal.json | 9c022b8bf62a24c9827d779ec5bf154e6d383773 | 1604 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/author_normal_scientific.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/author_normal_scientific.json | 654ada612a94f710903d2afc5623c601fb540805 | 1150 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/author_optimized.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/author_optimized.json | aae53e00e92fdc048724d14a1dc847e75d76ab26 | 1604 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/author_optimized_scientific.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/author_optimized_scientific.json | 654ada612a94f710903d2afc5623c601fb540805 | 1150 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/comparison.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/comparison.json | a0f34350b829d54a7a7afd47ac864f29baf3e67e | 20154 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/execution_manifest.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/execution_manifest.json | 7eab92ee0ba7b8fc7c9957b8998a271b62ceb827 | 41353 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/independent_normal.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/independent_normal.json | e303a918df305d29576ae121973c73c54f627d4b | 5253 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/independent_normal_scientific.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/independent_normal_scientific.json | 4da4a4e77b94b36abdee03030243ad0b586ef07b | 3127 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/independent_optimized.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/independent_optimized.json | a96dc39087d0d15ea55b90199d30ba1f7fefd71e | 5254 |
| evidence/schur_replay_freshness_20261007/raw/final_python312/independent_optimized_scientific.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python312/independent_optimized_scientific.json | 4da4a4e77b94b36abdee03030243ad0b586ef07b | 3127 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/author_normal.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/author_normal.json | 336c12147d8e8a464947ba4e080162e0cd57b80f | 1599 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/author_normal_scientific.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/author_normal_scientific.json | 654ada612a94f710903d2afc5623c601fb540805 | 1150 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/author_optimized.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/author_optimized.json | be637949a466d435a212ee8cc0e46da6d4267937 | 1600 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/author_optimized_scientific.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/author_optimized_scientific.json | 654ada612a94f710903d2afc5623c601fb540805 | 1150 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/comparison.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/comparison.json | a2cc2eba9029db2dd744cf0c880d41e99357d130 | 23412 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/execution_manifest.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/execution_manifest.json | ec482e3e400a2d95197d3b892c62711c3006bec8 | 41295 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/independent_normal.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/independent_normal.json | 85c8b8cfab5a0c39712752e5f0153709bcf36ca4 | 5250 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/independent_normal_scientific.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/independent_normal_scientific.json | 4da4a4e77b94b36abdee03030243ad0b586ef07b | 3127 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/independent_optimized.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/independent_optimized.json | c8ae2f311c48a5c72476cba574d98b892c2629ed | 5249 |
| evidence/schur_replay_freshness_20261007/raw/final_python313/independent_optimized_scientific.json | archive/evidence/schur_replay_freshness_20261007/raw/final_python313/independent_optimized_scientific.json | 4da4a4e77b94b36abdee03030243ad0b586ef07b | 3127 |
| evidence/schur_replay_freshness_20261007/schur_stale_normal.json | archive/evidence/schur_replay_freshness_20261007/schur_stale_normal.json | 03dc01a44f5a28b6c1d91aaad5f20ac1880d03c3 | 342 |
| evidence/schur_replay_freshness_20261007/schur_stale_optimized.json | archive/evidence/schur_replay_freshness_20261007/schur_stale_optimized.json | 3176e337a9b56afb08a5b8e608a3bf9665609fbe | 342 |

### evidence/weighted_support_20261006 -> archive/evidence/weighted_support_20261006

| Old path | New path | Git blob SHA | Bytes |
|---|---|---|---:|
| evidence/weighted_support_20261006/combined_source_binding.json | archive/evidence/weighted_support_20261006/combined_source_binding.json | 28e46d4fdec26f65422686e2b86b1a9589221cfa | 3551 |
| evidence/weighted_support_20261006/original_results/combined.json | archive/evidence/weighted_support_20261006/original_results/combined.json | 48e6eeede392e39a26be7f51a62bf385be031411 | 12959 |
| evidence/weighted_support_20261006/original_results/equidistribution.json | archive/evidence/weighted_support_20261006/original_results/equidistribution.json | ba17f7f5ea9783497e9607892d9dcc00e7e037bf | 358 |
| evidence/weighted_support_20261006/original_results/physical.json | archive/evidence/weighted_support_20261006/original_results/physical.json | e166a894332723fd9d04684a7713d87763158400 | 4366 |
| evidence/weighted_support_20261006/original_results/quantum.json | archive/evidence/weighted_support_20261006/original_results/quantum.json | efed1203638694c608a50e8e1826081c8df53e0f | 3251 |
| evidence/weighted_support_20261006/original_results/stationary.json | archive/evidence/weighted_support_20261006/original_results/stationary.json | 7cb97e9ca7b2d35cb086a9163e75ace54b635138 | 1616 |
| evidence/weighted_support_20261006/portable_exact_results.json | archive/evidence/weighted_support_20261006/portable_exact_results.json | e85aff14a4e02201cadc3ea800924d3377e97b5b | 26590 |
| evidence/weighted_support_20261006/promotion_receipt.json | archive/evidence/weighted_support_20261006/promotion_receipt.json | 9519b73b1ace9fc0cbf0638ee11f5b41e2129c77 | 2010 |
| evidence/weighted_support_20261006/source_binding.json | archive/evidence/weighted_support_20261006/source_binding.json | c12baae11cffcfd0522f739f664cbeaac7639354 | 8092 |
| evidence/weighted_support_20261006/stationary_source_binding.json | archive/evidence/weighted_support_20261006/stationary_source_binding.json | 3010bd2b780c0a233973bc3fce42d68c921eefe6 | 1035 |
