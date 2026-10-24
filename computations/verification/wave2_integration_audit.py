#!/usr/bin/env python3
"""Fail-closed mapping/status/link check, not an independent proof audit."""
from pathlib import Path
import hashlib
import json
import re
from wave2_checked_replay import require, safe_path, strict_json, source_bytes
from wave2_portable_replay import sealed_source_bytes

ROOT=Path(__file__).resolve().parents[2]

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def check_external_epoch(root, epoch):
    """Preserve the sealed 39-row leaf while admitting explicitly reviewed later sources."""
    extension=epoch.get('external_dependency_extension',{})
    snapshot=safe_path(root,extension.get('historical_registry',''))
    require(snapshot.is_file() and
            sha(snapshot)=='e55207391ff6df4870e53d81a875b267f5e848a2be38bee058843df5e350bcbb',
            'historical external leaf changed')
    previous=strict_json(snapshot.read_bytes())
    current=strict_json((root/'literature/external_dependencies.json').read_bytes())
    require(current['schema']==previous['schema'],'external registry schema changed')
    rows=current['dependencies']; active={row['id']:row for row in rows}
    old={row['id']:row for row in previous['dependencies']}
    allowed={'EXT-OO-1997','EXT-MATSUMOTO-2007','EXT-VV-2017','EXT-JM-2015',
             'EXT-HSW-1999','EXT-TROPP-2011','EXT-AGG-1989','EXT-PITTEL-2016','EXT-KPSS-2002','EXT-BF-2023','EXT-CS-2006','EXT-STANLEY-1981',
             'EXT-BR-1975','EXT-WANG-1982','EXT-FI-1980','EXT-ZAGIER-1997',
             'EXT-BORDA-2020','EXT-BT-1971'}
    declared=extension.get('added_ids',[])
    require(len(declared)==len(allowed) and set(declared)==allowed,
            'external extension requires explicit epoch review')
    require(len(active)==len(rows) and set(active)==set(old)|allowed,
            'duplicate or undeclared external dependency')
    for identifier,row in old.items():
        # A later cache pointer is provenance, not a theorem-contract change.
        # bibliographic_metadata_audit.py independently checks the selected
        # cache and all load-bearing identity/mapping fields.
        contract=lambda entry:{k:v for k,v in entry.items() if k!='metadata_audit'}
        require(contract(active[identifier])==contract(row),
                'historical external contract changed: '+identifier)
    return len(old),len(allowed)

def check_prior_claims(previous, current, epoch):
    """Apply only explicitly documented amendments to immutable old rows."""
    rows=epoch.get('historical_claim_amendments',[])
    amendments={row['id']:row for row in rows}
    approved={'BGS-CAYLEY-001','BGS-CAYLEY-003','BGS-FM-005','BGS-FM-008',
              'BGS-FM-010','BGS-FORMAL-001','BGS-FORMAL-003','BGS-RES-006',
              'BGS-RET-001','BGS-TRACE-008','BGS-FLOW-011','BGS-FLOW-021',
              'BGS-FM-013','BGS-FM-016','BGS-FM-019','BGS-TRACE-011',
              'BGS-TRACE-012','BGS-TRACE-013',
              'BGS-LOOP-001','BGS-FLOW-016','BGS-FLOW-017','BGS-FLOW-018',
              'BGS-FLOW-019','BGS-FLOW-020','BGS-FM-018','BGS-FM-020',
              'BGS-TRACE-014','BGS-FM-021','BGS-FM-022','BGS-TRACE-015',
              'BGS-FM-023','BGS-TRACE-016','BGS-FORMAL-002','BGS-TRACE-017',
              'BGS-FM-024','BGS-TRACE-018','BGS-FM-025','BGS-TRACE-019',
              'BGS-TRACE-020','BGS-FM-026','BGS-TRACE-021','BGS-TRACE-022',
              'BGS-FLOW-003','BGS-FLOW-004','BGS-FLOW-005','BGS-FLOW-006',
              'BGS-FLOW-007','BGS-FLOW-008','BGS-FLOW-009','BGS-FLOW-010',
              'BGS-FM-006','BGS-FM-007','BGS-FM-009','BGS-FM-012',
              'BGS-FM-014','BGS-FM-015','BGS-FUP-001','BGS-RES-004',
              'BGS-RES-005','BGS-TRACE-009','BGS-TRACE-010','BGS-FM-027',
              'BGS-FLOW-012','BGS-FLOW-013','BGS-FLOW-014','BGS-FLOW-015',
              'BGS-FM-017','BGS-RES-001','BGS-RES-002'}
    require(len(amendments)==len(rows) and set(amendments)==approved,
            'historical claim amendments require explicit epoch review')
    for old in previous:
        expected=dict(old)
        if old['id'] in amendments:
            row=amendments[old['id']]
            digest=hashlib.sha256(json.dumps(old,sort_keys=True,separators=(',',':'),
                                             ensure_ascii=False).encode()).hexdigest()
            require(row.get('historical_row_sha256')==digest and row.get('disposition')
                    and row.get('review'), 'historical claim amendment provenance differs')
            require(isinstance(row.get('fields'),dict) and row['fields']
                    and set(row['fields'])<=set(old) and 'id' not in row['fields'],
                    'invalid historical claim amendment fields')
            expected.update(row['fields'])
        require(current.get(old['id'])==expected,
                'old claim contract changed outside reviewed amendment: '+old['id'])

def run(root=ROOT):
    mapping=strict_json((root/'record/wave2_promotion_mapping.json').read_bytes())
    require(mapping['base_commit']=='129c676b8e6457e7e5f1bd6f786b3939cbd84653','base changed')
    require(mapping['preparation_seal']=='342a585d20134a12100053d16af767d03a07dc18e50cabbe8ff5105330b4f7e8','preparation seal changed')
    require(len(mapping['cards'])==6,'missing/extra scoped cards')
    require(len(mapping['immutable_copies'])==85,'prepared immutable closure changed')
    immutable=[]
    for row in mapping['immutable_copies']:
        immutable.append((row['proposed_repository_path'],row['sha256'],row['bytes']))
    ward=next(c for c in mapping['cards'] if c['claim_id']=='BGS-TRACE-027')
    for row in ward['immutable_copies']:immutable.append((row['path'],row['sha256'],row['bytes']))
    require(len(ward['immutable_copies'])==7,'Ward copied closure changed')
    for rel,digest,size in immutable:
        p=safe_path(root,rel);require(sha(p)==digest and p.stat().st_size==size,'immutable copy changed: '+rel)
    require(not list((root/'evidence/wave2_checked_20261007').rglob('*.xml')),'private source extracts copied')
    registry=strict_json((root/'record/claims.json').read_bytes())
    current={c['id']:c for c in registry['claims']}
    previous=strict_json((root/'evidence/wave2_checked_20261007/raw/provenance/base_navigation/record/claims.json').read_bytes())
    epoch=strict_json((root/'record/claim_integration_epochs.json').read_bytes())
    check_prior_claims(previous['claims'],current,epoch)
    ids={'BGS-TRACE-024','BGS-FM-031','BGS-TRACE-025','BGS-TRACE-026','BGS-TRACE-027'}
    later=set()
    continuation=root/'record/wave3_promotion_mapping.json'
    if continuation.is_file():
        later={c['id'] for c in strict_json(continuation.read_bytes())['cards']}
        require(later=={'BGS-TRACE-028','BGS-TRACE-029'},'undeclared later ID set')
    # Future registrations are explicitly reviewed as a separate epoch. This
    # preserves the historical Wave2 delta and rejects undeclared new IDs.
    epoch=strict_json((root/'record/claim_integration_epochs.json').read_bytes())
    require(epoch['schema']=='bgs-follow-on-claim-epoch-v1' and
            epoch['base_epoch']=='2026-10-07-wave3','claim epoch schema/base changed')
    rows=epoch['after_wave3']
    follow_on={row['id'] for row in rows}
    require(len(follow_on)==len(rows) and follow_on and
            not follow_on.intersection(ids|later|{c['id'] for c in previous['claims']}),
            'duplicate, empty or historically overlapping follow-on epoch')
    for row in rows:
        active=current.get(row['id'],{})
        require(active.get('state')==row['state'] and
                active.get('source')==row['source'] and row.get('disposition'),
                'follow-on ID/state/source requires explicit epoch review: '+row['id'])
    require(set(current)-{c['id'] for c in previous['claims']}==ids|later|follow_on,
            'new stable ID set differs from explicitly reviewed epochs')
    require(current['BGS-BGS-001']['state']=='open' and current['BGS-TRACE-005']['state']=='open','BGS/TRACE005 strengthened')
    require({c['claim_id'] for c in mapping['cards']}==ids|{None},'card mapping duplicate or theorem/audit confused')
    for c in mapping['cards']:
        path=safe_path(root,c['source'])
        if c['claim_id']:
            require(c['claim_id'] in path.read_text(),'ID missing from wrapper')
            require(sha(path)==c['integrated_wrapper_sha256'],'integrated wrapper mapping changed')
            require(current[c['claim_id']]['formalization']==[],'uncompiled formalization claimed')
    words={cid:(root/current[cid]['source']).read_text() for cid in ids}
    require('no aggregate rate' in words['BGS-TRACE-024'].lower(),'one-pinch rate exclusion lost')
    require('smooth' in words['BGS-TRACE-024'] and 'bounded' in words['BGS-TRACE-024'],'weight distinction lost')
    require('fixed-N' in words['BGS-FM-031'] and 'N>=3' in words['BGS-FM-031'],'centering fixed-N boundary lost')
    require('no particular proof method' in words['BGS-TRACE-025'],'rounding strategy strengthened')
    require('e_j(A)=0 for j>N' in words['BGS-TRACE-026'] and '-exp(-2s)/(4s^2)' in words['BGS-TRACE-026'],'hook extension/plateau sign lost')
    require('ceil(T_N/2)<=m<=T_N' in words['BGS-TRACE-027'] and 'full-prefix' in words['BGS-TRACE-027'] and '403' in words['BGS-TRACE-027'],'Ward window/export scope lost')
    # Source pins are historical inputs, not silently refreshed current statuses.
    inputs=sealed_source_bytes(root)
    scoped=strict_json(inputs['record/wave2_scoped_input_bindings.json']);require(len(scoped['files'])==50,'targeted closure changed')
    for rel,row in scoped['files'].items():require(hashlib.sha256(inputs[row['source']]).hexdigest()==row['sha256'],'reviewed pin changed: '+rel)
    contract=strict_json(inputs['record/wave2_replay_contract.json']);require(len(contract['tasks'])==8 and len({t['domain'] for t in contract['tasks']})==6,'replay domain closure differs')
    links=0
    for rel in [c['source'] for c in mapping['cards']]+['record/wave2_checked_integration_20261007.md']:
        p=root/rel
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if '://' not in link:
                require((p.parent/link.split('#')[0]).resolve().is_file(),'broken wrapper/integration link: '+rel+' -> '+link);links+=1
    manuscript=root/'manuscript/unified_sections/checked_phase_trace_checkpoint.tex';text=manuscript.read_text()
    mm=strict_json((root/'record/wave2_manuscript_mapping.json').read_bytes())
    require(sha(root/mm['section'])==mm['section_sha256'],'manuscript mapping changed')
    require(set(mm['authoritative_wrappers'])=={c['source'] for c in mapping['cards']},'manuscript source closure differs')
    for rel,digest in mm['authoritative_wrappers'].items():require(sha(root/rel)==digest,'manuscript source binding changed')
    for cid in ids:require(cid.removeprefix('BGS-') in text,'missing manuscript scope '+cid)
    require('upper-half' in text and 'negative plateau' in text and 'remain open' in text,'manuscript scope exclusions lost')
    check_external_epoch(root,epoch)
    return {'status':'passed','immutable_copies':len(immutable),'prepared_copies':85,'ward_sealed_files':7,'reviewed_input_pins':50,'scoped_cards':6,'new_theorem_ids':5,'historical_prior_claims':len(previous['claims']),'unchanged_prior_claims':len(previous['claims'])-len(epoch['historical_claim_amendments']),'explicitly_amended_prior_claims':len(epoch['historical_claim_amendments']),'wrapper_links':links,'replay_tasks':8,'bounded_domains':6,'private_XML_extracts':0,'unavailable_Ward_archive_replayed':False,'scope':'Mapping, bytes, status and links; not proof audit or aggregate suite.'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
