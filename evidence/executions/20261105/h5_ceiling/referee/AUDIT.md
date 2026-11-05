# Hostile referee audit: H5 structural-ceiling arithmetic (PR #91, BGS-TRACE-348..351)

Repo `ChurilovMaksim/BGS`, branch `h5-ceiling-arith`, audited head `e7e819bb` (base origin/main `3995d691`), 5 November 2026.
One reader. Internal project review, not external refereeing. The referee fix commit sits on top of `e7e819bb`.
`/workspace/audit/pr91/AUDIT.md` records the final head sha.

## Verdict: FIX-FIRST (one remaining wording item in a hash-pinned file, see §6)

The mathematics of TRACE-348..351 is correct, the Lean statements match `record/claims.json` with no hidden extra
hypotheses, the Lean module rebuilds, every numeric script reproduces its committed log, and all renderers and checkers
pass. One overstatement remains in `REPORT_H5_CEILING.md` §3. That file is sha256-pinned in `receipt.json`, so under the
audit rules I did not edit it. Its fix and the receipt refresh are left to the owner (§6). Once those two edits are in,
the verdict is MERGE.

## (a) Proofs, re-derived

Write ε^n = a_n + b_n√2. Then a_n = h_n, a_n² − 2b_n² = (−1)^n, and a_n is odd.

- **348.** Let q | h_p. Then q is odd. The norm relation gives 2b_p² ≡ 1, so s = 2b_p has s² ≡ 2 and q ≡ ±1 (mod 8). This
  step needs only that n is odd. Take any root s and set e = 1 + s, a unit because e(1 − s) = −1. Then e^p = b_p s,
  e^{2p} = 2b_p² = 1, and e² − 1 = 2e ≠ 0. So ord(e²) = p, p | q − 1, and since both are odd, 2p | q − 1. **CONFIRMED.**
- **349.** Fix one root s for a common prime q. Then ord((1+s)²) = p = p′. **CONFIRMED.**
- **350.** (i) Take p ≡ 3 (mod 4) and q = 2p + 1 prime. Then q ≡ 7 (mod 8), so s exists, and e^{2p} = e^{q−1} = 1. Also
  e^{2p} − 1 is the image of λ^p − 1 = ε^p(ε^p + ε̄^p) = 2h_pε^p, because ε^pε̄^p = −1. Hence 2h_p e^p ≡ 0 and q | h_p.
  (ii) Converse: q | h_p forces q ≡ ±1 (mod 8). For odd p, p ≡ 1 (mod 4) gives q ≡ 3 (mod 8), which is impossible.
  (iii) Least prime factor: every prime factor is ≡ 1 (mod 2p), so it is at least 2p + 1, and 2p + 1 is attained by (i).
  So P⁻(h_p) = 2p + 1 exactly. Since h_n ≥ 2^{n−1}, h_p > 2p + 1 for p ≥ 5, and h_p is composite. "Exactly the p with
  P⁻ = 2p + 1" holds for every p, not only up to 1500: if P⁻ = 2p + 1, then 2p + 1 is prime and divides h_p, and (ii)
  applies. **CONFIRMED.**
- **351.** (λ^n − 1)/(λ − 1) = h_nλ^{(n−1)/2}, since λ − 1 = 2ε. Pair k with n − k and use λ + λ⁻¹ = 6. For n = 1 the
  product is empty and h_1 = 1. **CONFIRMED.**
- I checked θ_B = 0.26236 against lineN14/referee/logs/ref_arith.json: 1 − 2θ_B = 0.4753 is correct.

## (b) Lean

`Bgs.H5CeilingArith` statements compared with the claims:

| Lean theorem | Hypotheses and conclusion | Claim text |
|---|---|---|
| `prime_dvd_mod8` | `[Fact q.Prime]`, `Odd n`, `↑q ∣ a n` ⊢ `q % 8 = 1 ∨ q % 8 = 7` | 348, every odd n |
| `prime_dvd_mod2p` | `[Fact p.Prime]`, `p ≠ 2`, q prime, `↑q ∣ a p` ⊢ `q % (2p) = 1` | 348 |
| `orderOf_lambda` | ⊢ `orderOf ((1+s)^2) = p` for every root s | 348, 349 |
| `coprime_h` | p, p′ prime, ≠ 2, p ≠ p′ ⊢ `Int.gcd (a p) (a p') = 1` | 349 |
| `sg_dvd` | `n % 4 = 3`, `(2n+1).Prime` ⊢ `↑(2n+1) ∣ a n` | 350 (i), n need not be prime |
| `sg_iff` | `Odd n`, `(2n+1).Prime` ⊢ `(2n+1) ∣ a n ↔ n % 4 = 3` | 350 converse |
| `sg_minFac` | p prime, `p % 4 = 3`, `(2p+1).Prime` ⊢ `minFac |a p| = 2p+1 ∧ (5 ≤ p → 2p+1 < |a p|)` | 350 (iii) |

There are no hidden or weaker hypotheses. `a` is defined by the ε-multiplication recurrence, and `a_eq_h6` identifies
it with `Bgs.H6LemmaW.h`. The closed form (ε^n + ε̄^n)/2 itself is paper-level, which is standard and harmless. The file
contains no `sorry` and no `native_decide`. TRACE-351 is not formalized, as the claim states. I rebuilt the module with
its artefacts moved aside first (`lake build Bgs.H5CeilingArith`, packages linked, no new cache). The build ended with
"Build completed successfully (2841 jobs)" (`lake_build_H5CeilingArith_referee.log`). `#print axioms` gives
[propext, Classical.choice, Quot.sound] for all theorems except `a_eq_h6`, which uses [propext] only.

## (c) Numerics, rerun

`h5_arith.py`, `h5_density.py` and `thmL_sanity.py` (Python 3.13.5, 1 thread) reproduce the committed logs byte for
byte, apart from the `seconds` field: 664,579 primes, 207 hits, 0 violations, 28,203 coprime pairs, 25 family members,
maximum relative error 3.2831e-80, 90/237 good below 10⁸, histogram {0: 87, 1: 88, 2: 43, 3: 16, 4: 3}. I also wrote an
independent check from scratch (`indep_check.py`, output `indep_check.out`). It covers full factorisations for p ≤ 61,
q < 2·10⁵ against every p ≤ 1000, all pairwise gcds for p ≤ 1000, 350 (i)–(iii) with trial division, and 351 at 60
digits. Everything passes, and the family for p ≤ 1000 is the first 18 of the 25.

## (d) Registry and renderers

The counts are 434 total and 350 proved; 179 non-open claims link Lean files; there are 194 modules and 2479
theorem/lemma lines (2458 + 21). The claims.json boundaries agree with the logs. All 18 checkers in `checks_after.log`
exit 0, after the referee edits. The unittest suite ran 266 tests, OK (1 skipped).

## (e) Edits made (fix commit)

- `NOTE.md`: Theorem L is retagged from [P] to **[P-sketch]** (one reader, non-explicit error terms, not formalized,
  no independent referee). The tag legend now covers single-reader sketches, and "Theorem L shows" becomes
  "If the sketch is correct, Theorem L shows". The BYPASS Prop A3 bullet now carries an explicit [P-sketch] tag.
- `README.md` / `README.ru.md` abstract: "Three integrations" becomes "Four integrations", and the sentence now names
  this integration (BGS-TRACE-348..351; H5 stays open). `README.ru.md` Lean paragraph: it now also mentions the separate
  build of `Bgs.H5CeilingArith`, which the English version already did.

## (f) Exaggerations and factual errors found

1. **Fixed (NOTE §2): factual error.** The note said "147 of the 237 p are certified bad (a proper factor ≤ 10⁸)".
   That is wrong for p = 31. h_31 = 424577·865087, and P⁻ = 424577 > h_31^{0.4753} ≈ 3.1·10⁵, so p = 31 is good by the
   note's own criterion; it is lineN14's `p31_cover`. The correct count is 146 certified bad: every other one of the 147
   has min factor ≤ h_p^{0.406}. The log key `certified_bad = 147` in `h5_density.json` really counts "has a proper
   factor ≤ 10⁸". The table column and the heuristic comparison are unaffected.
2. **Fixed (NOTE §2): overstatement.** The note said the TRACE-350 family "fails every condition P⁻(h_p) > h_p^α,
   α > 0". That holds only for members with h_p^α ≥ 2p + 1. Counterexample: p = 11 and α = 0.3, where 8119^{0.3} ≈ 14.9
   < 23. The sentence is reworded.
3. **Not fixed, because the file is hash-pinned (REPORT_H5_CEILING.md §3, line 77):** "So these p are never 'good' …
   for any positive exponent" is the same overstatement as item 2. Proposed text: "So for each fixed α > 0 these p fail
   P⁻(h_p) > h_p^α as soon as h_p^α ≥ 2p + 1, i.e. for all but finitely many members of the family."
4. **Receipt consistency:** `receipt.json` pins the sha256 of `NOTE.md` (b9c13722…, the e7e819bb version). After this
   fix NOTE.md has sha256 99300018000597310499508521980d53a7bb2713b2b6920e5fd511dd6dee4f2b. The owner should refresh
   the receipt with `mk_receipt.py` after item 3.
5. Not verifiable: "reproduces the research log row by row" (receipt `agrees_with_research1105_s7_row_by_row`), because
   research1105 is not committed.
6. Ledger text: "NO INDEPENDENT REFEREE" is now out of date in substance (this audit). I left the registry unchanged.
7. Pre-existing and outside the diff: RESULTS.md says "seven phases", while the README says eight.

Nothing else in the diff is false or overstated: the CHANGELOG, the counts, the TRACE-342 relation and the non-claims
about H5, R♯-mod v5 and R′ all check out.
