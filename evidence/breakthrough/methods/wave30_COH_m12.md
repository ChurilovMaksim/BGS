# Wave 30, task 3 — COH at m=12 across ALL components: HOLDS

## Verdict

COH holds at m=12, exactly and exhaustively over all joint-global
groups: for every pair sharing the joint global multiset, a single
(j, c) works across all components simultaneously. No COH
counterexample exists at m=12, so the R**+COH route to JBL is NOT
killed here. COH in general remains open; this is m=12 only.
Repository untouched; no Lean built.

## Scope correction

Wave 29's two-component test covered only (128, 81). But
D_12 = 2·768398401 − 2 = 1536796800 = 2^7·3^4·5^2·7^2·11^2, so the
full component set is {128, 81, 25, 49, 121} and genuine parameters
number 1,536,796,800 — direct grouping is infeasible. This test
covers all five components via an exact reduction, not enumeration.

## Setup and criterion

For genuine A, S(A) = (Tr(Aα^i))_{i∈Z/12}. A pair shares the joint
global multiset iff some permutation σ of Z/12 sends S(A) to S(A′).
With τ the dihedral map of (j, c), COH holds for the pair iff for
some τ: S′_q − τ(S_q) ∈ ShiftSeq_q for every q, where ShiftSeq_q =
{0} except q=81, where it is the 9 sequences Tr(27Dα^i), D∈R/3R
(Ann is trace-preserving; Ann(odd)={0}). The Shadow-aware form is
essential: Shadow shifts change mod-81 traces by multiples of 27.

## Key structural facts (all verified exactly)

- Classes equal dihedral images at q≠81 (0 non-dihedral class
  sequences at 128, 25, 49, 121). Hence validity of σ at q≠81
  depends only on S_q's value pattern.
- At q=81, the big class (36 sequences) has 24 non-dihedral images,
  but ALL 24 are Shadow-equivalent to dihedral images (difference
  in the 9 shift sequences). So the big class does not break COH.
- Patterns per component: 128: 2, 81: 17, 25: 7, 49: 5, 121: 13.

## The test (C++)

With alive_q(σ, pattern) = {τ : pattern[σ(i)] = pattern[τ(i)] ∀i}
and T_81 = {τ : S′_81 − τ(S_81) ∈ ShiftSet}, a pair fails iff all
alive_q are nonempty and (AND alive_q) ∩ T_81 = ∅.
- Phase 1 (mixed, T_81 full): 257,520 (pattern, dihedral-image)
  tuples; 0 with empty mask-intersection and a matching σ.
- Phase 2 (81-constrained, T_81 proper): 1728 class pairs,
  207,360 matchings, 30,600 distinct σ, 159,312 valid
  pattern-tuple checks; 0 failures. (The 17 huge-matching pairs
  all have T_81 full, hence belong to Phase 1; no enumeration
  explosion: the naive valid-σ enumeration OOMs on the all-zero
  sequence, 12! matchings.)

## Independent cross-check (Python, no patterns)

Brute-force σ-backtracking per sampled joint A (joint recurrence +
per-component genuine-sequence membership + Shadow-aware τ check):
1200 random + 600 big-class-81 + 300 big-class with zeroed
components = 2100 A's, 0 failing. Agrees with the C++ result.

## Counts, honestly

Failing joint-global groups at m=12: 0 (exhaustive over the failure
condition, not by enumerating groups). Total number of joint-global
groups was NOT enumerated (infeasible at 1.5B parameters); the
claim is "every group admits a single (j, c)", not a group census.

## Files

- `methods/wave30_COH_m12.cpp` (+ `wave30_COH_m12.log`, ~6 s),
  `methods/wave30_COH_m12_crosscheck.py`.
- Prior: `methods/wave29_JBL_global_step.md` (COH defined, §4).
