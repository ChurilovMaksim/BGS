# Canonical manuscript

The current article has exactly one TeX source and one built PDF:

- `main.tex` - the only editable manuscript source;
- `main.pdf` - the corresponding rendered manuscript.

No section-level `.tex` files or competing `proof/final/complete` manuscripts belong in the active `paper/` tree. Historical manuscripts remain only in `archive/legacy-workspace/paper/` and Git history.

Build locally with:

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript is intentionally explicit about status: exact finite identities are separated from theorem drafts, numerical evidence, and the still-open general BGS/local-spacing problem.
