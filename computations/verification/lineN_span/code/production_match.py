#!/usr/bin/env python3
"""Lemma 8 finite check (BGS-TRACE-338): compare the exact census with the production artifacts.

Inputs (committed, read-only): computations/verification/lineN14/logs/a_enum.jsonl (N14 exact
enumeration, j <= 12, span/zr/word from digits.eps_digits at mp.dps 34, KK = 6) and
evidence/executions/20261101/lineNgas/N20/logs/a_cert_ext*.jsonl (j = 13, 14).
Requires logs/span_census_J16.jsonl (run span_census.py 16 first).
Also recomputes the exact words for the a_enum classes to count the stored `word` entries that
are int()-truncated floats (span and zr are compared; the stored word is not used by Thm A).
"""
import json, glob, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(pathlib.Path(__file__).parent))
L = ROOT / 'computations/verification/lineN_span/logs'
mine = {(r['a'], r['b']): r for r in map(json.loads, open(L / 'span_census_J16.jsonl'))}
import importlib.util
spec = importlib.util.spec_from_file_location('sc', pathlib.Path(__file__).parent / 'span_census.py')
out = {}
enum = [json.loads(l) for l in open(ROOT / 'computations/verification/lineN14/logs/a_enum.jsonl')]
mm = [r for r in enum if (r['span'], r['zr']) != (mine[(r['a'], r['b'])]['span'], mine[(r['a'], r['b'])]['zr'])]
out['a_enum'] = dict(classes=len(enum), census_classes_j_le_12=sum(1 for r in mine.values() if r['j'] <= 12),
                     span_zr_mismatches=len(mm))
# stored word vs exact word (exact words recomputed with the census routine, imported without running main)
src = open(pathlib.Path(__file__).parent / 'span_census.py').read().split('def defect')[0]
ns = {'__file__': str(pathlib.Path(__file__).parent / 'span_census.py')}; exec(src.replace('J = int(sys.argv[1]) if len(sys.argv) > 1 else 16', 'J = 16'), ns)
wmm = 0; pattern_ok = 0
for r in enum:
    w = ns['word'](r['a'], r['b'])[0]
    if r['word'] != w:
        wmm += 1
        if len(r['word']) == len(w) and all(s == e or s == e - (1 if e > 0 else -1) for s, e in zip(r['word'], w)): pattern_ok += 1
out['a_enum_stored_word'] = dict(classes_with_word_mismatch=wmm, mismatch_letters_equal_exact_minus_sign_exact=pattern_ok)
ext = rows = coded = coded_bad = 0
for f in sorted(glob.glob(str(ROOT / 'evidence/executions/20261101/lineNgas/N20/logs/a_cert_ext*.jsonl'))):
    for l in open(f):
        r = json.loads(l); m = mine[(r['a'], r['b'])]
        if r.get('coded'):
            coded += 1; coded_bad += m['zr'] < 6; continue
        rows += 1; ext += (r['span'], r['zr']) != (m['span'], m['zr'])
out['a_cert_ext'] = dict(rows_with_span=rows, span_zr_mismatches=ext, coded_rows=coded, coded_rows_with_exact_zr_lt_6=coded_bad)
(L / 'production_match.json').write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out, indent=1))
