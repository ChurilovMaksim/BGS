# Editorial register — Phase 4 Pass 0 (staging)

Source: manuscript/ at live main HEAD e18abe3 (snapshot bgs_live_e18abe3; live
manuscript/BGS_unified.tex SHA verified identical before execution).
All operations are moves / renames / merges only — no content cut
(compendium mode R4). Final gate: 324 pages, same 14 underfull boxes,
0 undefined refs/citations, .aux byte-identical to baseline.

## 1. Renames (12, old -> new; references updated in BGS_unified.tex only — verified tree-wide)

- unified_sections/research_20260921.tex -> unified_sections/fixed_map_symmetry_crossover_coercivity.tex
- unified_sections/phase_channel_jet_20261008.tex -> unified_sections/phase_channel_jets.tex
- unified_sections/chat_research_20261011.tex -> unified_sections/microscopic_paths_and_phase_laws.tex
- unified_sections/chat_integration_20261016.tex -> unified_sections/spectral_functionals_integration.tex
- unified_sections/abel_gaussian_20261016.tex -> unified_sections/abel_gaussian_rigidity.tex
- unified_sections/phase_cluster_continuation_20261019.tex -> unified_sections/circular_phase_trace_schemes.tex
- unified_sections/physical_kick_20261021.tex -> unified_sections/physical_kick_decay.tex
- unified_sections/spectral_final_20261021.tex -> unified_sections/spectral_corpus_one_step_returns.tex
- unified_sections/spectral_trace_closure_20261022.tex -> unified_sections/inserted_trace_closure.tex
- unified_sections/checked_phase_trace_checkpoint.tex -> unified_sections/reviewed_phase_signed_trace.tex
- unified_sections/checked_unmasked_pinch_checkpoint.tex -> unified_sections/unmasked_insertion_closure.tex
- final_delivery_note.tex -> consolidation_addendum.tex (addendum part only; the 8 math inputs were lifted to root inputs)

Not renamed (per staging report): finite_orbit_note.tex (immutable wrapper);
borderline actual_*/cobfourth names were NOT applied (not mandatory).

## 2. Moves / merges

- BGS_unified.tex lines 92-917 (826 lines, 3 tomography sections, byte-identical)
  -> unified_sections/ch13_tomography_and_discrimination.tex; root keeps one
  \input at the same position (after the aperture prerequisites).
- final_delivery_note.tex lines 2-9 (8 Wiener \inputs, in order) -> 8 direct root
  \inputs at the wrapper's position; lines 11-90 (consolidation addendum) stay
  compiled via consolidation_addendum.tex at the same position.
- arithmetic_core_part1-5 (1,118 lines) -> unified_sections/ch02_arithmetic_core.tex
- floquet_part1-4 (267 lines) -> unified_sections/ch07_floquet_resonance.tex
- coboundary_part1-3 (200 lines) -> unified_sections/ch07_coboundary_resonance.tex
- locality_part1-7 (197 lines) -> unified_sections/ch09_locality_fixed_strength.tex
  (part7 single closing sentence appended to part6 as a paragraph, never a section)
- nondegeneracy_part1-8 (279 lines) -> unified_sections/ch10_resonance_rigidity.tex
- intermediate_old_layers.tex (32 lines) -> inlined into
  unified_sections/literal_time_multiplicity_bounds.tex at its former \input line
- audit_and_frontier.tex: NOT moved in Pass 0 (stays compiled in place).
  Staged, not wired: unified_sections/appendix_b_provenance_and_verification.tex
  (skeleton: section/subsection heads + Pass 2/3 compression note),
  unified_sections/ch15_conclusion_seed.tex (verbatim lines 141-160),
  record_staging/audit_and_frontier_full_text.md (full text for record/).
- manuscript/README.md: "excluded from the build" table corrected (both files are
  compiled; see §3), plus the Wiener-block passage updated (direct root inputs
  since Pass 0; addendum file renamed).

## 3. Line ledger (compiled closure, newline-counted)

Baseline 21,641 (109 files) -> s1 tomography +1 = 21,642 (110 files)
-> s2 Wiener lift -1 = 21,641 (110 files) -> s3 audit drafts 0 = 21,641
-> s4 merges -23 = 21,618 (87 files) -> s5 renames/README 0 = 21,618.
Deltas accounted: +1 added \input line (tomography); -1 blank wrapper line
removed (Wiener); -22 removed duplicate part \input lines + -1 removed nested
\input line (merges + inlining). Final: 87 compiled files, 21,618 lines.
Disk .tex files: 90 (87 compiled + appendix skeleton + Ch15 seed +
finite_orbit_note wrapper).
