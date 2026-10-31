"""Gate (owner audit of PR #64): a proved claim may depend on a non-proved claim only on BGS-TRACE-206
(frozen definition). Strict for the Line L range BGS-TRACE-244..268. Claims outside that range that already
violated the gate on main e9e1550a are listed explicitly (out of scope of Line L); any other violation fails."""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
claims = json.loads((ROOT / 'record/claims.json').read_text(encoding='utf-8'))['claims']
by = {c['id']: c for c in claims}
ALLOWED_DEFINITIONAL = {'BGS-TRACE-206'}
PRE_EXISTING_ON_MAIN = {  # (claim, non-proved dependency) pairs present on main e9e1550a; not touched by Line L
    ('BGS-TRACE-076', 'BGS-TRACE-060'), ('BGS-TRACE-077', 'BGS-TRACE-073'),
    ('BGS-TRACE-080', 'BGS-TRACE-060'), ('BGS-TRACE-080', 'BGS-TRACE-073'),
    ('BGS-RES-015', 'BGS-RES-014'), ('BGS-RES-023', 'BGS-RES-022'),
    ('BGS-TRACE-236', 'BGS-TRACE-231')}
found = set()
for c in claims:
    if c['state'] != 'proved':
        continue
    for d in c.get('dependencies', []):
        if by[d]['state'] != 'proved' and d not in ALLOWED_DEFINITIONAL:
            found.add((c['id'], d))
line_l = sorted(p for p in found if p[0].startswith('BGS-TRACE-') and 244 <= int(p[0].split('-')[-1]) <= 268)
other = sorted(found - PRE_EXISTING_ON_MAIN - set(line_l))
print('proved claims:', sum(c['state'] == 'proved' for c in claims))
print('Line L (244..268) violations:', line_l)
print('new violations outside Line L:', other)
print('pre-existing on main (listed, out of scope):', sorted(found & PRE_EXISTING_ON_MAIN))
print('pre-existing pairs no longer present:', sorted(PRE_EXISTING_ON_MAIN - found))
ok = not line_l and not other
print('GATE_OK' if ok else 'GATE_FAIL')
sys.exit(0 if ok else 1)
