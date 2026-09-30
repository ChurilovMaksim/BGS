# Literature and external theorem dependencies

[signed_heisenberg_sources.md](signed_heisenberg_sources.md) pins the
corrected Diaconis--Evans stable moment range and credits prior
non-self-averaging and project cubic calibrations.

`literature/` records the external mathematical boundary of the BGS research
programme. A citation is not treated as a proof merely because its title or
abstract resembles the needed statement.

Start with:

- [bibliography.md](bibliography.md) — curated theorem-level bibliography and source checks;
- [external_dependencies.json](external_dependencies.json) — machine-readable
  load-bearing theorem locators, pinned versions/editions, dates checked,
  hypothesis mappings, and project sources;
- the specialized source notes in this directory for return laws, local
  limits, temporal resonance, and other theorem families.

## Load-bearing citation rule

A publication-grade external dependency records authors, title, persistent
identifier, pinned version/edition, exact theorem/lemma locator, date checked,
project-specific hypothesis mapping, and affected claims. Search snippets and
abstract-level similarity are not sufficient.

The scientific registry audit verifies that registered external dependency IDs
resolve and that claims marked with an external-theorem status actually name
their dependencies.

Historical literature notes remain useful audit records, but the current
machine registry is the normalization layer for load-bearing dependencies.
