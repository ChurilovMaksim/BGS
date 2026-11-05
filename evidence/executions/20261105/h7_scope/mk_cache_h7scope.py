"""Integrator script: metadata snapshot for the H7* scope integration (BGS-TRACE-344..347). Carries registry_metadata_20261104_h6p0.json
forward and refreshes only the transitive impact sets changed by the new claims (no new external reference, no field change)."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, hashlib, copy, subprocess
OLD = 'evidence/source_metadata/registry_metadata_20261104_h6p0.json'
NEW = 'evidence/source_metadata/registry_metadata_20261105_h7scope.json'
REPORT = 'record/audits/metadata_cache_refresh_20261105_h7scope/report.md'
raw = open(OLD, encoding='utf-8').read(); a = json.loads(raw)
assert json.dumps(a, indent=2, ensure_ascii=False) + '\n' == raw
oldsha = hashlib.sha256(raw.encode()).hexdigest(); assert oldsha == open(OLD.replace('.json', '.sha256')).read().split()[0]
reg = {x['id']: x for x in json.load(open('literature/external_dependencies.json'))['dependencies']}
claims = json.load(open('record/claims.json'))['claims']
mclaims = json.loads(subprocess.check_output(['git', 'show', 'origin/main:record/claims.json']))['claims']
def graph(eid, cl):
    direct = {c['id'] for c in cl if eid in c.get('external_dependencies', [])}
    closure = set(direct)
    while True:
        new = {c['id'] for c in cl if closure.intersection(c.get('dependencies', []))} - closure
        if not new: break
        closure.update(new)
    return sorted(direct), sorted(closure - direct)
FIELDS = ('title', 'authors', 'identifier', 'pinned_version', 'locator', 'dependency_role', 'mapping', 'project_sources', 'additional_uses')
assert {r['id'] for r in a['records']} == set(reg)
b = copy.deepcopy(a); changes = []
for rec in b['records']:
    eid = rec['id']; dep = reg[eid]
    assert not [k for k in FIELDS if dep.get(k) != rec['accepted_registry_fields'].get(k)], eid
    cur = graph(eid, claims); main = graph(eid, mclaims)
    stored = (sorted(rec['direct_claim_dependencies']), sorted(rec['transitive_claim_dependencies']))
    assert stored == main, ('pre-existing drift', eid)
    if cur != main:
        add_d = sorted(set(cur[0]) - set(main[0])); rem_d = sorted(set(main[0]) - set(cur[0]))
        add_t = sorted(set(cur[1]) - set(main[1])); rem_t = sorted(set(main[1]) - set(cur[1]))
        assert not add_d and not rem_d and not rem_t, eid
        rec['direct_claim_dependencies'], rec['transitive_claim_dependencies'] = cur
        changes.append({'id': eid, 'direct_added': [], 'direct_removed': [], 'transitive_added': add_t, 'transitive_removed': []})
n = len(a['records'])
b['scope'] = (f"{n} registered references: the {n} records of registry_metadata_20261104_h6p0.json carried forward (transitive impact "
              "sets refreshed only where the H7* scope integration changed them, listed in current_review.older_record_impact_changes); "
              "no new record (H7* scope integration, 2026-11-05). Earlier scope: " + a['scope'])
prev = dict(a['current_review']); prev['previous_snapshot_sha256_of_this_review'] = prev.pop('previous_snapshot_sha256')
b['supplemental_review_provenance']['metadata_cache_refresh_20261104_h6p0_carried_forward'] = prev
b['current_review'] = {'record': REPORT, 'previous_snapshot_sha256': oldsha, 'new_source_reviews': [],
  'scope': 'H7* scope integration (new BGS-TRACE-344..347): no new external reference, no registry-field change, no source observation changed; only transitive claim impact sets of older records change.',
  'older_record_impact_changes': changes}
out = json.dumps(b, indent=2, ensure_ascii=False) + '\n'
open(NEW, 'w', encoding='utf-8').write(out)
h = hashlib.sha256(out.encode()).hexdigest()
open(NEW.replace('.json', '.sha256'), 'w').write(f"{h}  registry_metadata_20261105_h7scope.json\n")
P = 'literature/metadata_audit.json'; praw = open(P).read(); p = json.loads(praw)
assert json.dumps(p, indent=2, ensure_ascii=False) + '\n' == praw
p['cache'] = NEW; p['digest'] = NEW.replace('.json', '.sha256'); p['review'] = REPORT
open(P, 'w').write(json.dumps(p, indent=2, ensure_ascii=False) + '\n')
P = 'computations/maintenance/v4_negative_controls.py'; t = open(P).read()
o = OLD; assert t.count(o) == 1
open(P, 'w').write(t.replace(o, NEW))
print(h, oldsha); [print(json.dumps(c)) for c in changes]
