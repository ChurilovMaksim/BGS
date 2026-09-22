# Scientific release policy

A Git tag or GitHub release is a frozen scientific state, not merely a software
version.

Recommended tags use `research-YYYY.MM.N`. Each release should record:

- commit SHA and source-tree hash;
- claim-registry schema/version;
- list of new, strengthened, corrected, retracted, and still-open claims;
- pinned external dependency versions/editions;
- environment manifest;
- commands actually executed and their outcomes;
- manuscript build hash when a PDF was successfully built;
- known unavailable checks;
- archive/DOI identifier only after it has actually been issued.

A release must never state “verified” solely because source files are present.
A GitHub Actions pre-execution failure is recorded as unavailable verification.

The manual release workflow under `.github/workflows/research-release.yml`
packages the research-state metadata and source tree. External archival DOI
minting remains an external action; repository metadata is prepared in
`.zenodo.json`.
