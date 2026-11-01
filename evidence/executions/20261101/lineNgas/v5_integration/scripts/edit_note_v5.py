"""Integrator script: adds the v5 section and refreshes the claim index of the Line N gas note from record/claims.json."""
import json
P = 'mathematics/fixed-map/lineN5N18_gas_conditional.md'
s = open(P, encoding='utf-8').read()
C = {c['id']: c for c in json.load(open('record/claims.json', encoding='utf-8'))['claims']}
T = lambda k: f'BGS-TRACE-{k}'
V5 = """## v5 update: THEOREM_DRAFT_v5, N20 v2, N21 v2 and referee lineN22 (1 November 2026)
**Canonical statement now:** `computations/verification/lineN_theorem_draft/THEOREM_DRAFT_v5.md` (repo copy with referee lineN22 edits
E1–E8 applied verbatim; author original, the author v4 → v5 diff and the edit diff are next to it). v1–v4 are kept as history.
**Theorem R♯-mod v5 is BGS-TRACE-325 (conditional)**; it supersedes BGS-TRACE-299 (v4, still conditional, ledger "superseded").
Frozen R′ (BGS-TRACE-206) is **not** refuted.

* **Sources.** The N20 v2 and N21 v2 author packets and the referee reports lineN20, lineN21, lineN21b and lineN22 are in
  `evidence/executions/20261101/lineNgas/` (`N20/`, `N21/`, `referee/lineN2*/`), byte-identical to the box originals, with their SHA256
  manifests. Final referee: lineN22, GO after E1–E12 (E1–E8 in the draft, E9–E12 in the registry).
* **Exponent correction (v5 §2).** B_p carries e^{−p(δ + A_bad^KP)}: the KP log → modulus step charges the weighted S₀(a), not a
  [P-sketch, background interplay as for H3]; lineN22 found it correct and necessary.
* **State changes.**
  * BGS-TRACE-302 (H4) open → **proved** [P] + [CA-fp]; dependencies 307, 322, 326, 327, 328; the title parenthetical
    "(open, no working route)" now reads "(met: BGS-TRACE-326)" (ID and statement unchanged).
  * BGS-TRACE-322 verification-pending → **proved a fortiori** via BGS-TRACE-335 (N21 Lemma C, δ_true(G ≤ 15) ≤ 2.2102e-6); the N16
    method named in its title had defects F21-1/F21-3 and is not the proof.
  * BGS-TRACE-323 verification-pending → **proved** [CA-fp] (values recomputed independently by lineN21b).
* **Unchanged states, new ledger/boundary text.** BGS-TRACE-301 (H3) stays **open** (superseded in substance by 332; its a = 5.93e-6
  used the withdrawn tail placeholder). BGS-TRACE-300 (H1) stays open, re-scoped as BGS-TRACE-336. BGS-TRACE-318 stays proved as an
  arithmetic implication in the input δ; its 1386/1390/1399 charge δ only and are not the theorem's p₁.
* **New claims.**
  * Conditional: BGS-TRACE-325 (Theorem R♯-mod v5; inputs H0, H1 = 336, H5–H8 = 303..306; uses 326, 332, 333), BGS-TRACE-332
    (Prop. K: H1-shell ⇒ H3 with a = a(C)), BGS-TRACE-333 (crossover with all rate budgets: first prime 3307 at C ≤ 0.082, fragile;
    1409 at C ≤ 8.8e-4, robust; additive budgets open).
  * Proved: BGS-TRACE-326 (δ_true ≤ 5.0313e-6, all G), 327 (Lemma D^T), 328 (Lemma Q), 329 (Prop. F, lower bound only; the ratio
    statement is [N]), 330 (Lemma J, ε-carries, λ-carry graph, Lemma R), 331 (Thm A, shells j ≤ 14, core functional), 335 (Lemma C).
  * Open: BGS-TRACE-336 (H1 re-scoped: H1-bad joint (A,B) second moment + H1-ali).
  * The proposed claim 334 (N14 digits.py mp.dps = 34 erratum, N21 F21-2) is recorded as erratum ERR-065, not as a claim; no ID 334 is
    registered.
* **Lean.** `formalization/Bgs/LineN20Arith.lean`, `LineN20TailArith.lean` and `LineN21Arith.lean` (namespaces `Bgs.LineN20`,
  `Bgs.LineN20Tail`, `Bgs.LineN21`): the author/referee files verbatim, 54 theorems with `#print axioms`, `norm_num`/`decide +kernel`
  only, no `sorry`, no `native_decide`. Finite arithmetic and finite graph facts only.
* **Gate.** `computations/verification/lineN_theorem_draft/integration_checks/proved_deps_gate_v5.py`, strict for 244..336.

"""
anchor = '## Registered claims\n'
assert s.count(anchor) == 1 and '## v5 update' not in s
s = s.replace(anchor, V5 + anchor)
for old, new in [
    ('  * 322: δ_true(G ≤ 15) ≤ 2.470e-6. The numerics are reproduced (lineN16); the conversion lemma is [P-sketch].\n',
     '  * 322: δ_true(G ≤ 15) ≤ 2.470e-6. The numerics are reproduced (lineN16); the conversion lemma is [P-sketch]. *(Since v5: proved\n    a fortiori via BGS-TRACE-335; see the v5 update.)*\n'),
    ('  * 323: the step-norm table for |t| > 1/256. The method is refereed, but the values were not recomputed.\n',
     '  * 323: the step-norm table for |t| > 1/256. The method is refereed, but the values were not recomputed. *(Since v5: proved,\n    values recomputed by lineN21b.)*\n')]:
    assert s.count(old) == 1, old
    s = s.replace(old, new)
# claim index rows from the registry
head, sep, tail = s.partition('## Claim index\n')
lines = tail.split('\n')
keep = [l for l in lines if not l.startswith('| BGS-TRACE-')]
rows = [f"| {i} | {C[i]['state']} | {C[i]['title'].replace('|', chr(92) + '|')} |" for i in sorted(C) if i.startswith('BGS-TRACE-') and 299 <= int(i[-3:]) <= 336]
hdr_end = keep.index('|---|---|---|') + 1
out = keep[:hdr_end] + rows + keep[hdr_end:]
s = head + sep + '\n'.join(out)
open(P, 'w', encoding='utf-8').write(s)
print(len(rows))
