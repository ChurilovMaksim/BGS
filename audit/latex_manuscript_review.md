# BGS manuscript LaTeX audit

## Initial pass

Branch: `latex-refactor-audit`

This audit records the structural and typographic refactoring of the BGS manuscript.

## Current main document

`manuscript/BGS_unified.tex` is the current entry point.

Observed baseline:

- document class: `article`
- geometry, font encoding, AMS mathematics, microtype, graphics and table packages are already used
- theorem environments are manually declared
- hyperref is present
- fancy headers are present

## Planned improvements

### Mathematical typography

Evaluate integration of:

- `thmtools` for theorem management
- `cleveref` for intelligent cross references
- `braket` and `physics` where notation is repeated manually
- `nicematrix` for operator and block matrix presentation

### Visual presentation

Evaluate:

- `tcolorbox` for main results and important statements
- `pgfplots` for reproducible scientific plots
- TikZ diagrams for proof architecture and conceptual maps
- improved font configuration

### Structural cleanup

The manuscript folder contains the main document and auxiliary standalone sections. Every file will be classified as:

1. active dependency of the final PDF;
2. useful but currently unused research material;
3. obsolete draft material.

No research material will be deleted without archival preservation.

## Next steps

- trace all `\\input` dependencies;
- audit `manuscript/unified_sections`;
- check unused sections;
- prepare controlled LaTeX modernization commits;
- perform consistency review of notation and claims.
