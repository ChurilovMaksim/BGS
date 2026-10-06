# Publication evidence policy

Review records and location-bearing execution records are curated representations,
not byte-for-byte copies. `publication_provenance.json` pairs original and public
SHA256 values and defines every execution-location placeholder. Placeholder paths
were not literal execution paths. No recompilation was needed for this curation;
all maintained executable predicates and source files are unchanged.

`compile.py.txt` and `fault-controls/fault_controls.py.txt` are historical wrapper
snapshots with named location placeholders, not portable runnable entry points.
Use the maintained `computations/verification/run_four_cut_kernel.py` for reproduction.
The original failed-root invocation remains a failure record; the corrected
invocation's successful result is separately recorded. Inherited hash fields in
receipts identify original artifacts; public file hashes are authoritative in the
publication map and overlay manifest.
