# Numerical strengthening, phase-7 В.3 (2026-10-25, staging record)

## Status of this document

This is a **supplement**, not a claim amendment. It changes **no** claim
state, source, id or title in `record/claims.json`, and it does not touch
the approved literal (93). It records, for the numerical checks that claim
statuses rest on, (a) what the original tolerance and grid were,
(b) what was re-run with rigorous interval arithmetic (FLINT/Arb) or
high-precision arithmetic, and (c) what remains heuristic finite evidence.
Heuristic evidence is labelled as such throughout and is **never**
relabeled "verified".

Base: live main HEAD `5f23406`. Every verifier script re-run below was
SHA-verified against live main before use (frozen_kick_rank
`9c8aa294…`, gram_resolvent_normalization `0fdc55ae…`,
pell_harmonic_returns `237c9ee6…`, phase_channel_jet `74ede2b6…`,
exact_coefficients `7721515f…`, exact_structure_checks `b6dc70d1…`).
The interval/high-precision scripts and their full logs are preserved
with the phase-7 В.3 work record; the machine-readable interval results
are in `evidence/numerical_strengthening_v3/interval_results.json`.

## How the scope was identified

- **Level A (14 claims):** every claim whose `boundary` in live
  `record/claims.json` (199 claims: 173 proved, 12 verification-pending,
  9 conditional, 5 open) explicitly scopes float/complex128/finite
  diagnostics (13 claims), plus BGS-TRACE-008, which names the same
  Gram verifier as BGS-RES-006 but whose boundary carries no float
  keyword (found by the verifier-sharing check below). All 14 are
  dispositioned.
- **Level B (53 scripts):** distinct verifier paths named anywhere in
  `record/claims.json` (165 total, 0 missing) whose files use
  floating-point libraries, by keyword classification (heuristic, not a
  proof of arithmetic): 50 mixed exact+float, 3 float-based. The other
  92 are exact/symbolic, 7 int-C++, 5 Wolfram symbolic, 3 mixed-C++,
  3 C++-unclassified, 2 other.
- **Seeds:** no unseeded RNG was found anywhere under `computations/`
  (no `default_rng()` without an argument, no bare `np.random.*`
  calls). Every sampled seed is a literal constant (e.g.
  phase_channel_jet `SEED = 20261008`, schur `20261011`) or fixed
  arithmetic of constants (e.g. `20260905+k`). Seeds fix diagnostic
  examples, not probability laws, exactly as the scripts' own docstrings
  state.

## Strengthened checks (re-run in this stream)

### G-1. Gram / Abel normalization — BGS-RES-006, BGS-TRACE-008
- Original: float64, N in {10, 11, 20, 21}, s in {1.3, 2.5}, tolerance
  2e-12 (3e-11 for the Poisson/resolvent pair), 700-term Abel sum with
  analytic tail bound q^701/(1-q); odd-N inserted phase 0.21374.
- Strengthened: **Arb interval arithmetic, precision 128**, grid refined
  to N in {10, 11, 12, 20, 21, 30, 31}, s in {0.7, 1.3, 2.5, 4.0}
  (28 cases). Gram-minus-lag-Gram enclosures: max absolute upper
  **2.4e-34** (vs 2e-12 float tolerance). Even-N CUE Gram
  (4/3 − 1/(3N²)) and two-clock Abel identities hold inside the Abel
  tail interval in all 16 even-N cases. Original float script
  re-run: PASS (8 finite cases).
- Verdict: **PASS, interval-certified on the refined grid.**
- Remaining limitation: finite N only; no asymptotic claim (as the
  original scope already states). The s = 0.7, N = 30/31 tail bounds
  are the loosest (≤ 4.1e-13) but still contain the two-clock value.

### P-1. Phase-channel identities — BGS-TRACE-053, BGS-TRACE-054, BGS-TRACE-056
- Original: float64/complex128, SEED 20261008, ATOL 2e-9, RTOL 3e-9,
  numpy-QR random unitaries, m in (3, 4), degrees 1–4.
- Strengthened: **Arb interval arithmetic, precision 128**,
  deterministic unitaries (DFT, identity, cyclic-shift × DFT — no RNG),
  m in (3, 4). Degree-1 and degree-2 identities hold entrywise with
  max absolute enclosure upper **5.4e-37** (vs 2e-9 float ATOL).
  Channel upper bounds (degrees 2, 3, 4 at m = 3; 2, 3 at m = 4) hold
  with the Frobenius norm, which dominates the spectral norm, so the
  spectral bound follows. The degree-2 spectral-norm identity itself
  follows analytically: the exact matrix's rows are scaled rows of the
  unitary kron(s, conj(s)), each used once, so its spectral norm is
  exactly max |s_ij · conj(s_ji)|. Original float script re-run:
  PASS (channel, 1800 cascade cases with max relative cubic error
  1.1e-13, 48 jet cases, 32 scalar-flow cases).
- Verdict: **PASS for the channel identities, interval-certified.**
  The m = 4 degree-4 channel bound was not interval-checked (5^4 = 625
  Kronecker terms; cost, not load-bearing) and remains float-only.
- Remaining limitations (honest, not softened): the jet controls and
  scalar-flow controls of the same script (TRACE-054's 4/3 optimality
  and TRACE-056's scalar-flow bounds) were **not** interval re-run;
  they remain float64 finite controls. TRACE-054's optimality rests on
  the analytic proof only, per its own boundary. The interval run
  replaces the random unitaries by deterministic ones; the original
  random samples remain float-only evidence.

### F-1. Frozen-kick rank — BGS-FM-005
- Original: float64 SVD of expm(i·0.4·a) − I, tolerance 1e-12, grid
  N in {3, 5, 7, 9, 15, 19, 21, 23, 35, 49, 63, 77}, bound checks only
  for N ≥ 19 at ranks [0, 1, N//20, N//10], variance constant
  66033/160000, B = 79/50.
- Strengthened: **Arb interval arithmetic, precision 128.** The frozen
  matrix is rebuilt from the exact rational coefficients of
  `exact_coefficients.py` times exact roots of unity, symmetrized;
  kick via `acb_mat.exp`; singular values from eigenvalue enclosures
  of kick^H kick. All bound checks for N in {19, 21, 23, 27, 35, 49, 63,
  77} pass with residual-norm intervals entirely above the analytic
  lower bounds; minimum margin **0.092** (interval widths ~1e-37).
  The variance interval contains 66033/160000 exactly at every N.
  Original float script re-run: PASS (12 cases, max assembly error
  7.2e-15, 28 bound checks).
- Verdict: **PASS, interval-certified on the full bound-check grid.**
- Remaining limitation (unchanged from the boundary): these are
  diagnostics at t = 0.4, **not** numerics at the frozen-model value
  τ = 10^-80, and they do not by themselves establish exact rank.
  The exact rank bound is the analytic statement; the numerics are
  finite controls for it.

### R-1. Pell return matrices — BGS-RET-001
- Original: complex128 matrices, ε = 0.23 only, cases
  (K, m, cutoff) in {(3,1,7), (3,2,7), (5,1,5)}, a in {1, 2},
  assertion |matrix − expanded| ≤ analytic truncation bound + 3e-12.
- Strengthened: **mpmath at 50 decimal digits** (matrix construction,
  eigendecomposition, Bessel series, analytic bound), slack tightened
  to 1e-40, grid refined with (5,2,5) and ε in {0.11, 0.31} for
  (3,1,7): 12 cases, all PASS, worst error/bound ratio **0.113**
  (ε = 0.11). The dominant error is the analytic Bessel truncation
  itself, not rounding: the 50-digit errors agree with the float64
  errors to ~7 digits, so float64 was not misleading here.
- Verdict: **PASS at 50 digits (high-precision recomputation, NOT an
  Arb interval enclosure — no interval certificate is claimed).**
- Original full script re-run: PASS (exact diagrams: 191304 ordered
  Weyl words, 144 rational recurrence checks; exact lattice: 2457
  cyclic integer vectors; exact cliques: 17812 subsets; 6 floating
  matrix cases).
- Remaining limitation (unchanged from the boundary): finite K and a
  single vanishing-kick scale in the controls; no asymptotic phase
  averaging or BGS conclusion follows from these checks.

## Dispositions for the remaining Level-A claims (no interval re-run)

- **BGS-TRACE-060 (conditional)** — verifier mixes exact
  energy/clock-word controls with separate floating feedback checks
  (seed 20261011, deterministic fixtures). The float feedback part was
  not interval re-run in this stream (Schur replay cost and
  basis-dependent split representations). **Float-only; limitation
  stands. No strengthened bound claimed.**
- **BGS-TRACE-080 (proved)** — verifier: size-16 exact, size-64
  complex128, 90 s wall. Not interval re-run in this stream.
  **Float-only for the size-64 part; limitation stands.**
- **BGS-CAYLEY-009 (proved)** — verifier mixes exact integer
  histograms/pairing polynomials with floating matrix checks
  (tolerances 1e-10, 1e-8, 1e-9). The float matrix part was not
  interval re-run in this stream. **Float-only for the matrix part;
  limitation stands.** The general theorem is analytic; neither type
  of finite check replaces it, per the script's own docstring.
- **BGS-RES-016 (proved)** — verifiers are **exact**: complex
  arithmetic as pairs of Fractions, orbit equivalence by exact
  Euclidean-norm descent (no iteration cutoff). Both scripts re-run
  in this stream: exit 0. **No float strengthening needed.**
- **BGS-RET-004 (proved)** — the load-bearing certificate is the
  exact-rational disjointness check (30 separation obligations,
  base-lobe margin 37/528; C++ integer verifier + Python verifier).
  The same script's floating unitary/ODE falsifiers (solve_ivp
  rtol 2e-11, atol 2e-13; gauge errors < 2e-14; negative controls
  > 1e-3) are auxiliary and were not interval re-run.
  **Exact part stands; float falsifiers remain float-only.**
- **BGS-CUE-002 (proved)** — the named verifier is **exact**
  (Fraction reference-cumulant checks). The boundary's "proxy
  computations are diagnostics" refers to proxy computations outside
  the named verifier; they are not a physical limit or a p-value.
  **No float strengthening needed; limitation stands as written.**
- **BGS-CAYLEY-011 (proved)** — verifier header states bounded
  resultant checks and the K = 131 computation are finite exact.
  **No float strengthening needed.** (The Lean module certifies only
  the bounded 1..12 residue; the general case is conditional on the
  cited classical theorem, per the boundary.)

## Failures

**None.** No strengthened bound contradicts any claimed bound. Every
interval/high-precision re-run passed. The items listed above as
"not interval re-run" are coverage gaps for a later В.3 pass, not
contradictions, and are recorded as limitations rather than failures.

## Coverage (honest counts)

- Level-A claims dispositioned: **14 / 14**.
- Level-A claims with an interval or high-precision re-run of a
  load-bearing numeric check: **7 / 14** (FM-005, RES-006, TRACE-008,
  RET-001, TRACE-053, TRACE-054, TRACE-056 — the last two via the
  shared channel identities only; see limitations).
- Level-A claims whose numeric content is exact (no float to
  strengthen): **3 / 14** (RES-016, CUE-002, CAYLEY-011).
- Level-A claims remaining float-only for their numeric part:
  **4 / 14** (TRACE-060, TRACE-080, CAYLEY-009, RET-004 falsifiers).
- Level-B scripts classified: 53 float-involving of 165 named
  verifiers; interval/high-precision coverage of Level B as a whole
  is **not** claimed — this pass covers the Level-A load-bearing
  checks plus the seed/tolerance audit across Level B.
- Claims covered in any form (dispositioned): **14 / 199**.
- Verifier-sharing check: the four strengthened scripts are named by
  exactly these 7 claims (FM-005, RES-006, TRACE-008, RET-001,
  TRACE-053, TRACE-054, TRACE-056) — no further claim shares them, so
  no disposition was missed through the strengthened scripts.
- No claim state, source, id or title changed; approved literal
  unchanged (93).
