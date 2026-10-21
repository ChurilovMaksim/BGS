#!/usr/bin/env python3
"""Render the thematic imported-source index and proof review matrix."""
import argparse
import json
import posixpath
from pathlib import Path
from rebuild_spectral_corpus import reconstruct

ROOT=Path(__file__).resolve().parents[2]
def esc(s):return str(s).replace('|',r'\|').replace('\n',' ')
def projections():
    c=json.loads((ROOT/'record/spectral_research/catalog.json').read_text());out={}
    raw=reconstruct(c)
    for topic,label in c['topics'].items():
        rel=f'mathematics/spectral_research/topics/{topic}.md'
        s=f'# {label}\n\n'+c['topic_overviews'][topic].strip()+'\n\n'
        s+='[Research hub](../README.md) · [Review matrix](../../../record/spectral_research/review_matrix.md)\n\n'
        for cl,name in [('author-proof-or-attempt','Proofs and research attempts'),('review-record','Internal reviews and outcome records'),('reference-code','Reference computations'),('author-evidence','Author execution evidence'),('expanded-container','Historical synthesis')]:
            es=[e for e in c['entries'] if e['topic']==topic and e['classification']==cl]
            if not es:continue
            s+=f'## {name}\n\n| Source | Current review scope |\n|---|---|\n'
            for e in es:
                title=e.get('title',e['original_path']);link=posixpath.relpath(e['target'],posixpath.dirname(rel))
                status=e.get('review_status','Historical synthesis, expanded into separate sources')
                s+=f'| [{esc(title)}]({link}) | {esc(status)} |\n'
            s+='\n'
        out[rel]=s
    rel='record/spectral_research/review_matrix.md'
    s=('# Imported proof and attempt review matrix\n\n'
       'Generated from [catalog.json](catalog.json). All source units are preserved, but preservation, '
       'an author audit and a finite PASS are different from an independently closed proof. '
       'The [current integration review](../spectral_final_integration_20261021.md) controls adoption. '
       'The historical six declared-hash differences are version qualifications, not a proof verdict.\n\n'
       '| Proof / attempt | Topic | Review scope | Historical declared hash |\n|---|---|---|---|\n')
    for e in c['entries']:
        if e['classification']!='author-proof-or-attempt':continue
        link=posixpath.relpath(e['target'],posixpath.dirname(rel))
        s+=f'| [{esc(e["title"])}]({link}) | {e["topic"]} | {esc(e["review_status"])} | '+('matches' if e['verified'] else 'uploaded revision differs')+' |\n'
    out[rel]=s
    section_index=['# Source section inventories','','Each thematic JSON file lists all Markdown headings outside fenced code in','its individual sources. Headings are retrieval locators, not proof verdicts.','The catalog records raw source hashes and exact preservation/review status.','',
                   '| Branch | Source units | Sections |','|---|---:|---:|']
    for topic,label in c['topics'].items():
        units=[]
        for e in c['entries']:
            if not e['original_path'].endswith('.md') or e['topic']!=topic:continue
            body=raw[e['raw_offset']:e['raw_offset']+e['raw_bytes']].decode()
            if e['classification']=='expanded-container':
                import re
                m=re.search(r'^# (?:Источник:|Приложение \d+[:.])',body,re.M)
                if m:body=body[:m.start()]
            sections=[];fence=None
            import re
            for i,line in enumerate(body.splitlines(),1):
                f=re.match(r'^\s*(`{3,}|~{3,})',line)
                if fence:
                    if f and f[1][0]==fence[0] and len(f[1])>=len(fence):fence=None
                    continue
                if f:fence=f[1];continue
                h=re.match(r'^(#{1,6})\s+(.+)',line)
                if h:sections.append({'line':i,'level':len(h[1]),'heading':h[2]})
            units.append({'original_path':e['original_path'],'target':e['target'],
                          'source_sha256':e['sha256'],'sections':sections})
        rel=f'record/spectral_research/sections/{topic}.json'
        out[rel]=json.dumps({'topic':topic,'units':units},indent=2,ensure_ascii=False)+'\n'
        section_index.append(f'| [{label}]({topic}.json) | {len(units)} | {sum(len(u["sections"]) for u in units)} |')
    out['record/spectral_research/sections/README.md']='\n'.join(section_index)+'\n'
    return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();bad=[]
    for rel,s in projections().items():
        p=ROOT/rel
        if args.check:
            if not p.exists() or p.read_text()!=s:bad.append(rel)
        else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
    if bad:raise SystemExit('Stale views: '+', '.join(bad))
    print('PASS: spectral thematic views and review matrix')
if __name__=='__main__':main()
