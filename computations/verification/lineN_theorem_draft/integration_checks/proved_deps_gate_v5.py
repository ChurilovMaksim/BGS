"""Gate (THEOREM_DRAFT_v5 integration, Lines N20/N21, referee lineN22; copy of proved_deps_gate_Ngas.py with the strict range
extended to 244..336. Original header: Lines N5-N18b integration; same rule as the PR #64 gate computations/verification/lineL/integration_checks/proved_deps_gate.py):
a proved claim may depend on a non-proved claim only on BGS-TRACE-206 (frozen definition). Strict for BGS-TRACE-244..324
(Lines K/L/L2/L3/M/N and Lines N2-N4 ids 286..298 and the new Lines N5-N18b ids 299..324). Pairs that already violated the gate on main
(listed in the PR #64 gate) are listed explicitly; any other violation fails. Also checks that the dependency graph is acyclic,
that every dependency id exists, and that every non-proved new claim has a closure_condition."""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
claims = json.loads((ROOT / 'record/claims.json').read_text(encoding='utf-8'))['claims']
by = {c['id']: c for c in claims}
ALLOWED_DEFINITIONAL = {'BGS-TRACE-206'}
PRE_EXISTING_ON_MAIN = {
    ('BGS-TRACE-076', 'BGS-TRACE-060'), ('BGS-TRACE-077', 'BGS-TRACE-073'),
    ('BGS-TRACE-080', 'BGS-TRACE-060'), ('BGS-TRACE-080', 'BGS-TRACE-073'),
    ('BGS-RES-015', 'BGS-RES-014'), ('BGS-RES-023', 'BGS-RES-022'),
    ('BGS-TRACE-236', 'BGS-TRACE-231')}
LO, HI = 244, 336
num = lambda i: int(i.split('-')[-1]) if i.startswith('BGS-TRACE-') else None
missing = sorted((c['id'], d) for c in claims for d in c.get('dependencies', []) if d not in by)
found = set()
for c in claims:
    if c['state'] != 'proved':
        continue
    for d in c.get('dependencies', []):
        if d in by and by[d]['state'] != 'proved' and d not in ALLOWED_DEFINITIONAL:
            found.add((c['id'], d))
strict = sorted(p for p in found if num(p[0]) is not None and LO <= num(p[0]) <= HI)
other = sorted(found - PRE_EXISTING_ON_MAIN - set(strict))
# cycle check (iterative DFS)
state, cycles = {}, []
for root in by:
    if state.get(root):
        continue
    stack = [(root, iter(by[root].get('dependencies', [])))]; state[root] = 1; path = [root]
    while stack:
        node, it = stack[-1]
        nxt = next((d for d in it if d in by), None)
        if nxt is None:
            state[node] = 2; stack.pop(); path.pop(); continue
        if state.get(nxt) == 1:
            cycles.append(path[path.index(nxt):] + [nxt])
        elif not state.get(nxt):
            state[nxt] = 1; stack.append((nxt, iter(by[nxt].get('dependencies', [])))); path.append(nxt)
no_closure = sorted(c['id'] for c in claims if num(c['id']) is not None and 299 <= num(c['id']) <= HI
                    and c['state'] != 'proved' and not c.get('closure_condition'))
new = [c for c in claims if num(c['id']) is not None and 299 <= num(c['id']) <= HI]
print('Line N ids 299..336:', len(new), {s: sum(c['state'] == s for c in new) for s in sorted({c['state'] for c in new})})
print('proved claims:', sum(c['state'] == 'proved' for c in claims))
print('missing dependency ids:', missing)
print('strict range 244..336 violations:', strict)
print('new violations outside the strict range:', other)
print('pre-existing on main (listed, out of scope):', sorted(found & PRE_EXISTING_ON_MAIN))
print('cycles:', cycles[:5])
print('open/conditional new ids without closure_condition:', no_closure)
ok = not strict and not other and not missing and not cycles and not no_closure
print('GATE_OK' if ok else 'GATE_FAIL')
sys.exit(0 if ok else 1)
