# Reproducible environment

The repository separates source pinning from evidence that an environment
actually executed.

## Maintained targets

- Python: 3.13 in GitHub Actions; package versions are exactly pinned in
  `requirements.txt`.
- C++: C++20; the maintained CI target installs the distribution Boost
  development package and configures CMake in Release mode.
- Lean: pinned by `formalization/lean-toolchain` and the Lake manifest.
- TeX/Pandoc: installed by the manuscript workflows; exact distribution build
  metadata should be captured in release execution manifests when a release
  PDF is produced.

`environment/runtime-manifest.json` is the machine-readable contract.
It records intended toolchain constraints, not a claim that the current
GitHub-hosted runner executed successfully.

## Release provenance

For a scientific release, record:
`python --version`, `pip freeze`, compiler/CMake/Boost versions,
`lake env lean --version`, Pandoc version, TeX engine/version, operating
system image, commit SHA, and source hashes.

The maintained workspace runner now requires a clean Git worktree by default,
hashes every tracked file before and after execution, records a canonical
whole-tree fingerprint, and captures Python package, compiler, CMake, Git, and
Boost version information in its execution manifest.

The current Python dependency file is version-pinned but not wheel-hash-locked.
Do not claim supply-chain hash locking until a generated lock with actual
package artifact hashes is committed and independently replayed.
