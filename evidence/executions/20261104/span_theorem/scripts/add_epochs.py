#!/usr/bin/env python3
"""Append after_wave3 rows for BGS-TRACE-337..341 to record/claim_integration_epochs.json (no sealed row is touched)."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[5]
P = ROOT / 'record/claim_integration_epochs.json'; raw = P.read_text(encoding='utf-8'); d = json.loads(raw)
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
C = {c['id']: c for c in json.loads((ROOT / 'record/claims.json').read_text(encoding='utf-8'))['claims']}
T = ' Does not close TRACE-206, TRACE-148 or BGS-001; frozen R\' is not refuted; registered 3307 / 1409 unchanged.'
H = '4 November 2026 (span theorem integration; PR #85, PR #83, P2; independent referee audit CONFIRMED after fixes): '
disp = {
 '337': 'proved [P]; Theorem A, L + 1 < span < L + 3, digits in {-1,0,1}, exact span formula; Corollary B only as near-sharpness (no improvement by more than 3.4e-4).',
 '338': 'proved [P] + finite comparison with the production files; Lemma 8, project word = digit word.',
 '339': 'proved [P] (exact integer computation, Lean finite checks); examples 116, 82 sqrt2, 118.',
 '340': 'conditional on hypothesis (M) and the per-site normalisation of A_M; Lemma BI; H1 => H3 needs only H1-bad and is proved modulo (M).',
 '341': 'conditional on H1-bad (and on (M) for the BI rows); sharp-span crossover rows 3067 (bare majorant), 3389 / 3407 (BI), 1409.'}
ids = {r['id'] for r in d['after_wave3']}
for k, t in disp.items():
    i = 'BGS-TRACE-' + k; assert i not in ids
    d['after_wave3'].append({'id': i, 'state': C[i]['state'], 'source': C[i]['source'], 'disposition': H + t + T})
P.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8'); print(len(d['after_wave3']))
