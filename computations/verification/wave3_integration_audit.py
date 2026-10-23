#!/usr/bin/env python3
"""Wave3 bytes, scope, lineage and links; not an independent proof audit."""
from pathlib import Path
import hashlib,json,re
from wave2_checked_replay import require,safe_path,strict_json
from wave3_checked_replay import source_bytes
ROOT=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(root=ROOT):
    m=strict_json((root/'record/wave3_promotion_mapping.json').read_bytes());require(m['right_final_receipt_status']=='passed final sealed closure','right final seal missing')
    require(m['v1_candidate_snapshot_sha256']=='8f16d97d6b4db441b3f9cee3adfa5daff2aa062ae86976fdff1d9b46339a15a3','v1 lineage changed')
    require(sha(root/m['v1_claims_artifact'])==m['v1_claims_sha256'],'v1 registry bytes changed')
    for row in m['immutable_copies']:
        p=safe_path(root,row['path']);require(sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],'Wave3 immutable copy changed: '+row['path'])
    rr=root/'archive/evidence/wave3_checked_20261007/raw/right_overlap';receipt=strict_json((rr/'review_receipt.json').read_bytes());require(sha(rr/'review_receipt.json')==m['right_receipt_sha256'],'right receipt identity')
    require(receipt['candidate_222_controls_reproduced'] is False and receipt['authorized_markdown_exports_read_and_hash_verified'] is True,'archive/export distinction lost')
    require(receipt['Schatten_tail'].startswith('passed') and receipt['full_unmasked_binomial_correction'].startswith('passed'),'accepted full hierarchy scope lost')
    for rel,r in receipt['files'].items():require(sha(safe_path(rr,rel))==r['sha256'],'right final receipt closure '+rel)
    cv=root/'archive/evidence/wave3_checked_20261007/raw/convex_review';cm=strict_json((cv/'review_manifest.json').read_bytes())
    for rel,digest in cm['files'].items():require(sha(safe_path(cv,rel))==digest,'convex final receipt closure '+rel)
    proof={'right':rr/'authorized_exports/right_overlap_and_unmasked_insertions.md','core':cv/'author_snapshot/conditional_convex_pinch_resummation.md','annealed':cv/'author_snapshot/annealed_compact_pinch_stability.md'}
    for name,p in proof.items():require(sha(p)==m['accepted_proof_hashes'][name],'accepted proof changed '+name)
    prior=strict_json((root/m['v1_claims_artifact']).read_bytes())['claims'];current={c['id']:c for c in strict_json((root/'record/claims.json').read_bytes())['claims']}
    for c in prior:
        v=dict(current[c['id']]);old=dict(c)
        if c['id']=='BGS-TRACE-024':
            v.pop('follow_on_result',None);v.pop('remaining_obligation',None);old.pop('remaining_obligation',None)
        require(v==old,'earlier theorem contract changed: '+c['id'])
    # The Wave3 promoted delta is immutable. Later claims belong to an
    # explicitly recorded follow-on epoch, never to the original Wave3 review.
    wave3_ids={'BGS-TRACE-028','BGS-TRACE-029'}
    epoch=strict_json((root/'record/claim_integration_epochs.json').read_bytes())
    require(epoch['schema']=='bgs-follow-on-claim-epoch-v1' and
            epoch['base_epoch']=='2026-10-07-wave3','claim epoch schema/base changed')
    rows=epoch['after_wave3']
    follow_on={row['id'] for row in rows}
    require(len(follow_on)==len(rows) and follow_on and
            not follow_on.intersection(wave3_ids|{c['id'] for c in prior}),
            'duplicate, empty or historically overlapping follow-on epoch')
    for row in rows:
        active=current.get(row['id'],{})
        require(active.get('state')==row['state'] and
                active.get('source')==row['source'] and row.get('disposition'),
                'follow-on ID/state/source requires explicit epoch review: '+row['id'])
    require(set(current)-{c['id'] for c in prior}==wave3_ids|follow_on,
            'Wave3/follow-on stable IDs differ from explicitly reviewed epochs')
    require(current['BGS-BGS-001']['state']==current['BGS-TRACE-005']['state']=='open','BGS target strengthened')
    links=0
    for c in m['cards']:
        p=safe_path(root,c['source']);text=p.read_text();require(c['id'] in text and current[c['id']]['formalization']==[],'ID/formalization scope')
        for rel in re.findall(r'\]\(([^)]+)\)',text):
            if '://' not in rel:require((p.parent/rel.split('#')[0]).resolve().is_file(),'broken scope wrapper link');links+=1
    right_text=(root/current['BGS-TRACE-028']['source']).read_text();convex_text=(root/current['BGS-TRACE-029']['source']).read_text()
    for phrase in ['||D0||_(S3)^3=o(N)','EVERY j>=3','z_N in [0,1]','B_n','N^(-(j+1))','222']:
        require(phrase in right_text,'right scope lost: '+phrase)
    for phrase in ['bounded u_N','UNWEIGHTED','1-z^m','DOES NOT refute T16','N^(b A0-1)/(A0 log N)']:
        require(phrase in convex_text,'convex scope lost: '+phrase)
    require(not list((root/'archive/evidence/wave3_checked_20261007').rglob('*.xml')),'primary extracts copied')
    mm=strict_json((root/'record/wave3_manuscript_mapping.json').read_bytes());require(sha(root/mm['section'])==mm['section_sha256'],'Wave3 section mapping changed')
    for rel,digest in mm['wrappers'].items():require(sha(root/rel)==digest,'Wave3 wrapper mapping changed')
    require('\\input{unified_sections/checked_unmasked_pinch_checkpoint.tex}' in (root/mm['entrypoint']).read_text(),'manuscript continuation unlinked')
    oldmm=strict_json((root/'record/wave2_manuscript_mapping.json').read_bytes());require(sha(root/oldmm['section'])==oldmm['section_sha256'],'Wave2 section bytes changed')
    inputs=source_bytes(root);contract=strict_json(inputs['record/wave3_replay_contract.json']);require([t['declared_check_count'] for t in contract['tasks']]==[72,227,1486,8708],'bounded controls differ')
    return {'status':'passed','new_theorem_ids':2,'immutable_Wave3_rows':len(m['immutable_copies']),'right_receipt_files':len(receipt['files']),'convex_receipt_files':len(cm['files']),'earlier_claims_preserved':101,'wrapper_links':links,'right_frame_controls':72,'separated_controls':227,'exact_convex_controls':1486,'independent_floating_controls':8708,'Wave2_section_unchanged':True,'unavailable_author222_replayed':False,'scope':'Byte/lineage/scope/link checks; no additional proof audit or aggregate build.'}
if __name__=='__main__':print(json.dumps(run(),indent=2))
