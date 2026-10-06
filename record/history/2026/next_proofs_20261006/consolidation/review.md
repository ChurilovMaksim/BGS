# Fresh consolidation audit: TRACE-015, FM-023, TRACE-016

## Normalized claim and primary verdict

**Correct only after a stated restriction.** The TRACE-016 proof's auxiliary term “K-unique” must explicitly require that the cyclic length-K vertex substrings at different starts have different VALUES. Its current two definition sentences instead require different starting positions. With the intended nonrepetition definition, no implication gap was found in the consolidated three theorems or their manuscript claims. TRACE-015 and FM-023 are accepted at the canonical hashes below without a mathematical change.

The claims reviewed are precisely: (1) once-counted distinct-port three-block signed band cancellation, error O_w((log N)^5/N) plus the displayed negligible terms; (2) actual fixed-tau d-grid compression at most min(1,C_tau(d^262/N)^(1/129)), for every odd d>=3 dividing odd N; (3) once-counted reduced distinct-port four-block signed band cancellation, error O_w((log N)^10/N) plus the displayed negligible terms. The path claims retain eventual flatness and simultaneous-in-L mixing as input, supplied for the actual model by FM-021. None implies deterministic BGS.

This is a fresh consolidation review, not a rerun of every source audit or finite certificate. I read BGS/AGENTS.md and the proof-audit instructions. No shared repository or input artifact was edited. All new files are confined to this review directory.

## Exact repair before promotion

In bgs_four_block_promotion/mathematics/four_block_unmarking.md:

- Line 53: “A cyclic word x is K-unique when its m cyclic length-K substrings have different starting positions.”
- Line 63: “K-unique in the sense that all cyclic K-substrings have distinct starting positions.”

Replace each definition by: “the m cyclic length-K vertex substrings are pairwise distinct,” or the equivalent injectivity statement that equal K-substrings have equal start indices modulo m. Indexed substring occurrences always have distinct starts; the literal current criterion does not imply primitivity or the long-interval alignment step. A periodic word is the immediate diagnostic. The needed injectivity is evident from every subsequent use and from the manuscript's correct phrase “distinct length-K cyclic substrings.” The second sentence is inherited verbatim from the accepted symbolic source; consolidation newly repeats the ambiguous/tautological version in Section 3. This is a definition cleanup, not a changed theorem, new hypothesis on U_N, or missing estimate. Do not alter the pinned historical sources; correct the canonical exposition and regenerate its hash.

## Dependency graph and obligations

### FM-023: passed

Physical fixed symbol -> translated analytic remainder retaining r -> degree-16 finite type -> area sublevel estimate -> fixed-symbol quantum intertwining -> cutoff/alias estimates -> per-entry bound -> d^2 span loss.

The added Section 5.0 was checked directly rather than accepted because its source hash agrees. With integer labels, W(v)W(w)=exp(pi i omega(v,w)/N)W(v+w); the midpoint signs cancel the extra odd-N sign in raw T multiplication. The commutator is -2N sin(pi omega/N), and X_g/(2pi) gives -2pi omega in the same frequency ordering. Hence |sin t-t|<=|t|^3/6 gives N^-2 times the third Fourier moment. Cauchy--Schwarz with H5 is sufficient in dimension two: the squared weight behaves radially like r^-4, whose shell sum is summable. Fixed-time smooth area-preserving flow composition is bounded on H5, so Duhamel gives the asserted kick estimate and its inverse. Integer aliases are retained, not discarded.

There is no hidden H5 cutoff cost. Egorov is applied to the four fixed embedding coordinates and their uniformly smooth conjugated-translation family. The epsilon-dependent cutoff enters only AFTER this intertwining, where product calculus uses H3 and the operator bound uses H2. The N^-1 epsilon^-4, N^-2 epsilon^-3, square-root area, and d^2 costs are unchanged from the accepted derivation. Section 1's centered-projector extension is immediate since ||P-alpha I||_N^2=alpha(1-alpha); the explicit exclusion of alpha=0,1 is correct. Fixed d and delta<1/262 quantifiers are unchanged, including fixed tau and N-independent constants.

### TRACE-015: passed

FM-021 flatness/mixing + unitarity -> full marked contraction -> two-long uniqueness -> short-cluster localization -> rank>=2 -> start-first equality payment -> exceptional mass -> exact multiplicity three on the good set.

The existential set of ROOTED ORDERED pairs, all positive block lengths, and every compactly supported positive-band smooth weight agree with the accepted source. Consolidation adds explicit definitions and reproduces inherited marked and repeated-substring estimates rather than imposing a minimum block length. The two independent m root factors remain in the marked sum only. Localization eliminates an additional cyclic-shift factor. The good pair has exactly three block labelings; the exceptional unmarked mass is dominated by marked absolute mass rather than divided by three. The new explicit O(N^5 2^(-(aN-3)/3)) term is a safe polynomial overestimate. Generic-family wording merely identifies the hypotheses actually used; it does not strengthen the spectral conclusion.

### TRACE-016: passed after the definition repair above

Generic matrix inputs -> marked/local-overlap contractions; nonrepetition -> localization and three-anchor rigidity; rank-two classification + rank-one exclusion -> triangle-free representation graph; rank>=3 payment -> bad-multiplicity error; M/4-O -> once-counted result.

I reconstructed the new source/output orders in Cases U and V. Case U puts E in the final Y-to-X output segment, giving u1 A v2=p1 q2, w1 u2=r1 p2, v1 w2=q1 E r2. Case V puts E in the Z-to-Y segment, giving u1 A v2=p1 q2, w1 u2=r1 E p2, v1 w2=q1 r2. Both canonical cases match the corrected accepted source and handle empty prefixes/equal lengths. The old incorrect placement is not an active input.

The canonical classification retains the accepted compression set S union succ(S) union H, genuine-head preservation, and endpoint-preserving lift. Its old local-overlap contraction was moved into TRACE-016 Section 2 rather than lost: all eight connector factors and the q^2 short-chain factor are present. The rank-two dependency is the UNIVERSAL computer-assisted classification, consisting of the reviewed reduction plus its bounded kernel. The Lean artifact alone is not substituted for it. Local edges are counted once in O, good pairs have one or two representations, and bad marked mass receives the additional O(K^4) multiplicity cost. No universal division by four is asserted.

### Formal/manuscript boundary: passed

The merged FourCutKernel.lean executable definitions are unchanged from audited FourCut.lean except for the namespace; the four theorem declarations are the original Certificate/Endpoint declarations relocated into that namespace. The manuscript and canonical classification explicitly retain native_decide trust for sizes 5..12 and 5..10, ordinary decide for m=4, and the lack of formalized contraction/lifting, cyclic-word correspondence, analytic cancellation, or BGS. No semantic reason to repeat the 55-second Lean build was found, and no such rerun is claimed here.

## Hash acceptance and evidence

All source/preserved-copy hashes in the three source manifests and all enumerated artifact hashes matched. Full checks are in hash_checks.json; exact canonical and manuscript hashes are in accepted_canonical_hashes.json. That JSON records the reviewed bytes; TRACE-016's current hash is a reviewed-but-needs-definition-repair hash, not unconditional acceptance.

Accepted canonical mathematical hashes:

- TRACE-015: 7fd5b03f4cbc28e8daa30518e223b35f8962d9cae9a8309f9c43704f31390893
- FM-023: 4aa4da166331c02d0e527b68b1354827ef7011b67ec7d178ed1c3d71703f9881
- Four-cut classification: eaf320908a6229eaf2206598c122cd64b73e8ee42e0cc971febcbed885a2597d
- Bounded Lean source (semantic consolidation acceptance, not new build): 242c4ca40e839fbb2f298f70d1b7b3233607f2ef7c1d759f9cb8303eb8cf8429
- TRACE-016 reviewed pre-repair: 0953f512784c2ac7c640f2417f9b9441ebd441c9eaf794f72801303601ad60d8

Source-to-canonical diffs are saved for FM-023, TRACE-015, and classification. No newly performed finite computation is used to establish an analytic theorem. Prior independent reviews were read at the exact paths supplied in the assignment, including repaired_source_acceptance.md and the Lean semantic review.

## Collateral file/link issues, separate from mathematics

1. The three explicit FM-023 Markdown links to fixed_model_symmetry_theorem.md, frozen_operator_transfer_coercivity.md, and egorov_overlap_rigidity.md are absent in the partial overlay but exist at the intended BGS mathematics destinations. This is expected overlay incompleteness, not a broken integration link.
2. Curated FM-023 record references provenance/accepted_inputs.json and provenance/quantitative_source_accepted.md as root-relative code paths. The integration instructions do not explicitly list a destination for that top-level provenance directory. Preserve those artifacts in the promoted tree or update those references to a durable evidence location; do not leave an accepted-source hash without a retrievable pinned copy.
3. The curated FM-023 review's final computation paragraph mentions the new standard-library portable reconstruction, then says “The script ... uses SymPy 1.14.0.” This latter sentence belongs to the historical independent check_filters.py. Name that historical script explicitly to avoid conflating its dependency with the new standard-library verifier. The canonical proof itself distinguishes them correctly.
4. Full repository build, current stable-ID availability, registry propagation, manuscript inclusion and post-relocation provenance remain integration obligations; this review has not performed or certified them.

## Strongest safe statement and next check

Accept TRACE-015 and FM-023 at the listed hashes. Make the two local TRACE-016 definition replacements, check the resulting diff contains only that repair, and pin the new hash. The intended TRACE-016 theorem and all substantive consolidation steps pass. Continue to label the classification as computer-assisted and its Lean component as bounded native-evaluation certification; keep BGS and the complete signed hierarchy open.
