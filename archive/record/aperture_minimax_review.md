# Aperture-minimax review and integration

The inherited baseline is commit 05590eff0613b4a0f7c56d891e258ea41a45c0f0.
The master TeX, bibliography, claim ledger, CMake and requirements were
matched to their remote Git blob hashes before editing. Existing research
is preserved; new sections are included in the canonical master. No parallel
maintained article entrypoint or copied historical source tree is added.

## Mathematical review

The review separates four quantities: complete-ball sup-norm data error,
adaptive binary-projector risk, continuous-outcome heterodyne risk, and
finite-shell exact identifiability. Only the first three receive matching
rates here. Their common expression is not an identification of their
statistical experiments. Outside heterodyne outcomes are retained as one
flag, not postselected away. All copies are counted.

The upper proof has two independent cutoffs: an occupation cutoff K controls
trace norm via the moment, while a much larger analytic degree L controls
Taylor leakage before inversion. Applying a low-cutoff inverse to the whole
uncontrolled tail would be invalid. The proof instead truncates the entire
coherent kernel at L=128sK and proves an exponentially small amplified tail.
The positivity correction returns a normalized density matrix even when the
raw inverse is indefinite. An explicit fallback covers a zero positive part.

The lower proof bounds Hellinger distance, not only differences of means.
Uniformity in the amplitude permits adaptive transcript bounds. The
heterodyne proof separately integrates the full density and handles the
outside flag. The states in the lower bounds are positive, normalized and
of moment exactly E. Rank one suffices. The effective-scale inversion and
uniformity for radii varying with the budget are proved, not inferred from
two endpoint asymptotics.

## Execution and evidence

Two expanded Python runs use distinct seeds and 110/140 decimal digits.
Independent C++ integer arithmetic replays both scalar packets; its default
self-tests also run. Existing holomorphic-shell, Husimi, instability and
spectral-resolution controls were rerun. An attempted radius-instability
run to M=48 was interrupted by the enclosing command time limit and is not
reported as passed; the completed rerun reaches M=24.

The PDF build covers the two new proof sections and their three preceding
tomography sections, not the entire historical manuscript. Three pdfTeX
passes complete without unresolved references or overfull boxes; every page
is rendered and visually inspected. Source and log hashes and the actual
finite test counts are in the certificate. The tests support implementation
correctness; they are not the proof of the universal rates.

The local integration script is temporary tooling, not maintained research.
Generated binaries, caches, replay packets and PDFs stay out of main.
mpmath is made an explicit pinned dependency rather than relying on its
transitive installation through SymPy. CMake builds the new independent
checker. Lean compilation and remote CI success are not asserted.

Wolfram was retried and returned HTTP 404. Literature was checked with
primary documents and connected research search tools; no Wolfram result is
used as evidence. Priority and independent referee acceptance remain open.
