# Referee status table (Line D)

Source: independent referee audit (`REFEREE_AUDIT_REPORT.md`, §0 and §6). The packet's provisional IDs were BGS-TRACE-149…162 (a Line B packet also starts at 149). On main d6fa6e2a the highest registered TRACE id was BGS-TRACE-148, so 149 was the next free id. Line B had not merged, and these IDs were kept.

| item | referee verdict | referee-recommended state | provisional ID | state in claims fragment | fix status |
|---|---|---|---|---|---|
| D1 exact bridge | confirmed, needs fix (wording) | proved | 149 | proved | applied: odd N, gcd(N,D_m)=1; C^∞; V→−V evenness; Line B Thm 1 / Boasman–Keating credited |
| D2 1/p expansion | confirmed, needs fix (scope) | proved | 150 | proved | applied: g' period [P] (upper bound); non-uniformity in η, K with m=3, p=101 counterexample; regime condition [C] |
| D3 orbit-pair formula | confirmed, needs fix | proved | 151 | proved | applied: Fix_m wording; support facts [P] via Prop R argument; Kluyver average credited to TRACE-133 |
| D4 implication | confirmed | proved | 152 | proved | applied: a_k ≠ 0 hypothesis; false corollary withdrawn |
| D4 instances m≤7; D5(a) Γ-part; D5(c) | needs fix | verification-pending | 153 | verification-pending | applied: exact rationals; gaps 0.753 (support) vs 0.247 (all Fix_3); 'necessary not sufficient' |
| B^sym<2m, odd m | — | proved (odd m) | 154 | proved | applied: referee's odd-size support argument |
| B^sym<2m, even m | — | open beyond computed range | 155 | open | applied |
| D5(a) multiset; D5(b) | needs fix | proved | 156 | proved | applied: Newton ⇒ multisets only |
| D6(a) (+ oddness) | confirmed | proved | 157 | proved | applied: 'never −2m²' → oddness statement |
| D6(b) G ensemble | needs fix | conditional | 158 | conditional | applied: b degree 4 in η; G ensemble only |
| D6 J0 at large η | wrong in v1 | open | 159 | open | applied: referee data reported (c₁ grows ~η^1.5) |
| D7 full band | confirmed (minor fixes) | proved (transfer from TRACE-146) | 160 | proved | applied: i.i.d. up to global phase; p>4^m carried; J0 exponent caveat |
| K = κp | — | open (sketch) | 161 | open | unchanged |
| D8 R-scaling | downgrade wording | open (conjecture) | 162 | open | applied: four caveats; d8_spot (finished) incorporated |
| D9 χ²≈967 | downgrade to 'consistent with' | numerical record | — (in 162 boundary) | not a claim | applied |
| Lean Bgs.LineDCerts | confirmed; wording fix | finite certificates | evidence for 149/151/153/156 | — | applied: coll4/coll6 certify listed sequences only; Python checks cited; rebuilt (exit 0) |
| Novelty / literature | overstated | — | — | — | applied: referee novelty wording; Keating 1991 (309–341; 277–307 verified); Degli Esposti–Winn 2005; Hecke attribution removed; Boasman–Keating §5; Nonnenmacher 2003 |

All 11 non-claims of audit §5 appear verbatim in `mathematics/fixed-map/band_limited_kick_bridge.md` §0.

Replay: scripts in this directory are the referee's files; each now starts with the repository assertion-entry guard (a no-op under ordinary Python). They originally read two absolute paths of the research box: `/workspace/bgs-lineD/logs/linec_exact_values.json` (in the repo: `../logs/linec_exact_values.json`) and `/workspace/bgs-lineD/lean/LineDCerts.lean` (in the repo: `formalization/Bgs/LineDCerts.lean`). Those two lines, in `d8_spot.py` and `lean_semantics.py`, now resolve both paths from this script's directory. Logs of the referee run are in `logs/` here.
