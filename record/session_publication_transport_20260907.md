# Session publication transport note — 2026-09-07

Verified local publication candidate: one self-contained `WoW_unified.tex` and matching 146-page `WoW_unified.pdf`, SHA-256 respectively `e7e0ddcee9d4ee96683b9e7640b509e283b8011582dac28fe0e7b3937b81f583` and `55f759c1d4205d76b6499cbf52e52d2caf0273eac18aa0eaa990cbab94c73edd`.

The available GitHub connector exposes repository blob/tree/commit writes but no local-file parameter for these large generated files. GitHub Actions reruns failed before any step executed (`runner_id=0`). To keep `main` valid, old split manuscript sources are not removed until these exact replacement bytes can be installed atomically. This is a publication-transport limitation, not an unresolved mathematical result.
