# BGS research programme

## North-star standard

The programme is aimed at a result strong enough to survive the highest level of mathematical scrutiny. A prize cannot be planned or promised; what can be planned is the standard of evidence: a genuinely new theorem, exact assumptions, no hidden asymptotic regime, reproducible computation, independent implementations, machine-checked sublemmas where practical, and a paper that can be audited line by line.

The active theorem status is governed by `STATUS.md`. This document governs how new work is produced.

## Scientific objective

Resolve the BGS-type spectral-statistics problem for the desymmetrised quantised cat-map setting represented by this repository, starting from the exact finite arithmetic reduction and advancing only through proved load-bearing estimates.

The present bottleneck is `M1` in `research/M1.md`.

## Evidence ladder

Every claim must live at exactly one level.

1. `OBSERVED`: numerical pattern only.
2. `EXPERIMENTAL EXACT-AS-IMPLEMENTED`: finite computation exactly reproduces a stated implemented object, but equivalence to the target theorem object may still be open.
3. `FINITE-N EXACT`: mathematical finite identity or exhaustive finite certificate.
4. `LEMMA`: symbolic proof with all hypotheses stated.
5. `FORMALLY CHECKED`: Lean build succeeds and axiom/dependency status is recorded.
6. `THEOREM`: complete paper-level proof independent of numerical evidence.

No file name such as `proof`, `theorem`, `final`, or `PASS` overrides this ladder.

## Language and execution policy

### Python

Use for transparent reference implementations, algebra exploration, data generation, small/medium finite-field sweeps, symbolic checks, and result serialization. Prefer readable code over micro-optimisation.

### C++20

Use for expensive finite-field sweeps, large Gram/correlation computations, exhaustive enumerations, memory-sensitive kernels, and independent reimplementation of load-bearing Python experiments. Compile with warnings enabled. Whenever a C++ result matters mathematically, compare it with Python on overlapping designs.

### Lean

Use for exact finite certificates and symbolic lemmas after their mathematical statements are stable. A Lean file that has not been built must carry `UNVERIFIED BUILD`. Formalisation is evidence amplification, not a substitute for finding the proof.

### Julia

Julia is not required by the active programme. Historical Julia material is preserved as provenance. New computational work should normally be implemented in Python and/or C++ unless Julia provides a specific indispensable capability.

## Workstream A — exact rank-1 arithmetic core

Goal: maintain a minimal, trusted set of exact reductions connecting the cat-map problem to twisted Jacobi / character-sum objects.

Deliverables:

- fixed additive and multiplicative Fourier conventions;
- exact character indexing and subgroup/coset conventions;
- exact `k=2` reduction;
- independent twisted-Jacobi matrix-element regression;
- explicit map from every paper-level quantity to executable code;
- Lean certificates for finite combinatorial identities where useful.

Promotion condition: two independent implementations agree on calibration designs and the symbolic reduction is written without hidden normalisation changes.

## Workstream B — M1 cross-twist fluctuation theorem

Current priority.

### B1. Exact assembly

Derive the exact twist-pair representation of the full target `k=4` coupled energy. Prove equivalence before estimating it.

### B2. Exceptional-fiber classification

For the Möbius map

`v_d(u) = (u(d-1)+1)/(d-u+1)`,

classify every `d` and twist exponent pair for which degree drops, zeros/poles cancel, the map becomes constant, or the combined rational character becomes a perfect power.

The first exact exception is already known: `d=0` gives `v_0(u)=1` and produces `A_(1,psi)(0)=N-2` for nontrivial `psi`.

### B3. Cross-Gram structure

For `F_tau=A_tau*A_tau`, derive

`G_(tau,sigma)=<F_tau,F_sigma>`

exactly. Seek symmetry, rank reduction, orthogonality, representation-theoretic structure, or cancellation after summing `tau,sigma`. Do not replace the Gram sum by diagonal energy.

### B4. Generic finite-field bound

Apply Weil/Deligne-type estimates only to the generic divisor classes whose hypotheses have been checked explicitly.

### B5. Exceptional contribution

Evaluate or bound the finite exceptional layer separately and prove its normalised contribution is compatible with the chosen scaling regime.

### B6. Asymptotic theorem

State the regime in `(N,K,m)` before taking limits. The final error term must tend to zero in that regime by an explicit inequality.

## Workstream C — scalable falsification

Purpose: destroy wrong conjectures quickly; never substitute numerics for proof.

Required design ladder:

- `N=53, K=13` — tiny exact calibration;
- `N=199, K=11` — medium exact calibration;
- `N=461, K=23` — independent twisted-Jacobi calibration;
- `N=3571, K=17` — first large historical design;
- `N=19489, K=29` — larger independent design;
- additional split primes chosen to vary `K`, `m`, and `N` independently enough to distinguish real decay from a `K`-dependent constant.

For each new load-bearing statistic:

1. Python reference on the smallest feasible designs;
2. C++ implementation on the overlap;
3. cross-language tolerance recorded in JSON;
4. larger C++ sweep;
5. negative examples and counterexamples retained.

## Workstream D — alternative routes

The higher-moment, shape-automaton, word, Kloosterman, large-`m`, rank-2/Sp4, and spectral corpora remain active idea libraries.

An alternative route may replace M1 only if it proves its own load-bearing estimate and does not import:

- the failed diagonal-only Möbius-fiber energy decomposition;
- the false unrestricted `4 sqrt(N)` fiber bound;
- the invalid noncommutative-binomial R86/R87 reduction;
- numerical GOE agreement as a theorem premise.

## Workstream E — formalisation

Formalise in this order:

1. finite set/counting identities;
2. exceptional-fiber algebra;
3. exact convolution/Gram identities;
4. character orthogonality;
5. generic divisor classification;
6. asymptotic bookkeeping after the analytic estimate is settled.

Every formal file must state whether it has been built, the Lean version if known, and its axioms/dependencies.

## Workstream F — reproducibility and repository discipline

Canonical active directories:

- `research/` — current proof workstreams and open obligations;
- `code/math/` — small trusted mathematical kernels;
- `code/verification/` — theorem-adjacent regression/certification;
- `code/experiments/` — active falsifiers and exploratory computations;
- `code/cpp/` — high-performance independent implementations;
- `results/verified/` — reproducible current certificates;
- `results/experimental/` — current experiments with explicit scope;
- `results/numerical/` — current numerical spectral evidence;
- `results/historical-numerical/` — superseded/quarantined numerical results;
- `formal/` — Lean source;
- `paper/` — manuscript material;
- `archive/` — full provenance snapshots.

Rules:

- never delete a scientifically informative negative result solely because it failed;
- quarantine wrong interpretations, not the underlying evidence;
- generated build caches and duplicate binaries do not belong in Git;
- every current result must identify its producer;
- every expensive result should include parameters, environment, and precision/tolerance;
- historical metadata must not be silently rewritten to look current.

## Workstream G — publication-grade validation

Before claiming a main theorem:

1. adversarial internal proof audit;
2. independent implementation of every computationally load-bearing identity;
3. formal verification of selected exact bottlenecks;
4. independent human replication of the main derivation;
5. clean-room reproduction from the paper plus public code/data;
6. comparison with the strongest relevant literature and precise novelty statement;
7. removal of every theorem claim that still depends on an experimental or unbuilt step.

## Immediate queue

1. `M1-A`: symbolically classify all degenerate Möbius fibers and twist exponents.
2. `M1-B`: derive the exact cross-Gram Fourier formula with one normalization.
3. `M1-C`: implement a symmetry-aware C++ kernel that scales beyond `N=199`.
4. Prove the exact equivalence between the historical Möbius-fiber assembly and the intended current `k=4` target, or replace the assembly if it is not equivalent.
5. Formalise the general `d=0` degeneracy lemma once a buildable Lean environment is available.
6. Only after 1–5, attempt a repaired asymptotic bound.

## Stop conditions

The programme must stop or change route if a counterexample invalidates the target statement, if the exact assembly does not match the intended spectral quantity, or if the best possible exceptional/cross contribution cannot vanish in any relevant scaling regime. Such a result is scientifically valuable and must be recorded rather than hidden.
