#!/usr/bin/env python3
"""Offline guard against bibliographic drift, not a theorem applicability test.

Standard library only. Uses reviewed metadata observations, never a live network
lookup or automatic cache refresh. --self-test checks rejection of mutations.
An observed source hash identifies bytes seen during review; original publisher
PDFs are not redistributed and cannot be rehashed by this offline command.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

FIELDS = ('title', 'authors', 'identifier', 'pinned_version', 'locator',
          'dependency_role', 'mapping', 'project_sources', 'additional_uses')


def validate(registry, audit):
    errors = []
    deps = registry.get('dependencies', [])
    records = audit.get('records', [])
    ids = [r['id'] for r in deps]
    aids = [r['id'] for r in records]
    if len(ids) != len(set(ids)) or len(aids) != len(set(aids)):
        errors.append('duplicate reference ID')
    if set(ids) != set(aids):
        errors.append('registry/cache coverage differs; new references require review')
    by_id = {r['id']: r for r in records}
    for dep in deps:
        rec = by_id.get(dep['id'])
        if not rec:
            continue
        for field in FIELDS:
            if dep.get(field) != rec['accepted_registry_fields'].get(field):
                errors.append(f"{dep['id']}: {field} differs from reviewed cache")
        if not rec.get('source_observations'):
            errors.append(f"{dep['id']}: missing source observations")
        if not rec.get('application_status') or not rec.get('field_coverage'):
            errors.append(f"{dep['id']}: missing coverage/non-applicability accounting")
    return errors


def self_test(registry, audit):
    assert not validate(registry, audit)
    count = 0
    for n, _ in enumerate(registry['dependencies']):
        for field in FIELDS:
            changed = copy.deepcopy(registry)
            changed['dependencies'][n][field] = ['unrelated author'] if field == 'authors' else 'unrelated replacement'
            assert validate(changed, audit), (n, field)
            count += 1
    missing = copy.deepcopy(audit)
    missing['records'].pop()
    assert validate(registry, missing)
    duplicate = copy.deepcopy(registry)
    duplicate['dependencies'].append(copy.deepcopy(duplicate['dependencies'][0]))
    assert validate(duplicate, audit)
    print(f'bibliographic-metadata-audit: {count + 2} mutation tests passed')


def load_audit(root):
    pointer=json.loads((root/'literature/metadata_audit.json').read_text())
    if pointer.get('schema')!='bgs-metadata-audit-pointer-v1':
        raise ValueError('Unknown metadata-audit pointer schema')
    paths=[(root/pointer[k]).resolve() for k in ('cache','digest')]
    if any(not p.is_relative_to(root.resolve()) for p in paths):
        raise ValueError('Metadata-audit pointer escapes repository')
    path,digest_path=paths
    expected=digest_path.read_text().split()[0]
    if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
        raise ValueError('Cached metadata digest mismatch')
    return json.loads(path.read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    try:
        audit=load_audit(args.root)
    except (OSError,ValueError,KeyError,IndexError) as exc:
        print('bibliographic-metadata-audit: FAIL: '+str(exc),file=sys.stderr)
        return 1
    registry=json.loads((args.root/'literature/external_dependencies.json').read_text())
    errors = validate(registry, audit)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    # Exact graph coverage is regenerated at run time, so adding/removing a claim
    # never silently changes the recorded impact set.
    claims = json.loads((args.root / 'record/claims.json').read_text())['claims']
    for rec in audit['records']:
        direct = {c['id'] for c in claims if rec['id'] in c.get('external_dependencies', [])}
        closure = set(direct)
        while True:
            new = {c['id'] for c in claims if closure.intersection(c.get('dependencies', []))} - closure
            if not new:
                break
            closure.update(new)
        if direct != set(rec['direct_claim_dependencies']) or closure - direct != set(rec['transitive_claim_dependencies']):
            errors.append(f"{rec['id']}: dependency graph changed; refresh impact review explicitly")
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    if args.self_test:
        self_test(registry, audit)
    statuses = {}
    for rec in audit['records']:
        key = rec['application_status']
        statuses[key] = statuses.get(key, 0) + 1
    print(f"bibliographic-metadata-audit: OK: {len(audit['records'])} cached identities match; application coverage={statuses}")
    print('NON-CLAIM: metadata agreement and locator hits do not establish theorem applicability.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
