# Referee and internal review protocol

This repository is designed to support review at three different levels:
mathematical reading, independent verification, and historical audit.

## Theorem review

For a theorem-level claim:

1. resolve its stable ID in `record/claims.json`;
2. read the authoritative proof source listed there;
3. verify every assumption and normalization against the statement;
4. inspect every external dependency and its exact locator in
   `literature/external_dependencies.json`;
5. check that the dependency is used only in the scope mapped by the project;
6. inspect counterexamples and retractions that touch the route;
7. run the listed verifier/formalization surfaces when feasible;
8. compare the result with the claim ledger and manuscript wording;
9. record unresolved objections as proof obligations, not as vague review
   comments.

A successful finite computation certifies only its explicit finite statement.
A successful Lean build certifies only the formalized kernel and its stated
trust boundary.

## Fixed-map BGS review order

For the central programme, review in this order:

- `BGS-FM-001` through `BGS-FM-004`;
- `BGS-TRACE-001` through `BGS-TRACE-004`;
- the open closure claim `BGS-BGS-001`.

The final positive BGS claim may not be promoted until the open
Heisenberg-scale model estimate is proved for the correctly desymmetrized
fixed propagator.

## External theorem review

A load-bearing citation must record authors, title, persistent identifier,
pinned version/edition, exact theorem/lemma locator, date checked, project
hypothesis mapping, and the claims that depend on it.

Search snippets, abstracts, titles, and similarity of wording are not theorem
verification.

## Computational review

Prefer exact arithmetic for exact claims. For delicate finite claims, use
mechanistically independent implementations where feasible. Reviewers should
inspect invariants and negative controls rather than only the final scalar
output.

## Publication review

A publication candidate should contain one coherent theorem family. Its
`papers/<slug>/paper.json` manifest lists included claims, authoritative
sources, external dependencies, verification commit, and explicitly excluded
open questions.

## Review verdict vocabulary

Use: **verified in stated scope**, **verified conditional on named input**,
**finite evidence only**, **needs revision**, **open obligation**, or
**retracted**. Avoid unqualified labels such as “proved by numerics” or
“BGS-like”.
