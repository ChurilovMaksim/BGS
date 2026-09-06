#!/usr/bin/env python3
"""Idempotently index the audited consolidation without deleting prior work.

This script only appends marked blocks to existing project indices/CMake and
creates missing plain-text index files. It does not push, rewrite history,
alter old theorems, or infer CI status. Use --check for a preview.
"""
from __future__ import annotations
import argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MARKER='<!-- WoW consolidated manuscript 2026-09-06 -->'

def additions()->dict[str,str]:
    return {
      'README.md':f'''{MARKER}\n## Consolidated research manuscript (6 September 2026)\n\nThe authoritative combined source is [WoW_unified.tex](manuscript/WoW_unified.tex),\nwith the [audit](record/final_consolidation_audit_20260906.md). Historical\nsources are retained. The manuscript combines exact arithmetic reductions,\nPell and smooth resonance laws, locality, sharpness, the arbitrary-phase\nradius-eight certificate, and the noncommuting return-word construction.\n\nNo positive generic BGS, world-priority, full external referee approval, or\nnew Lean verification is claimed. Build with\n`python computations/maintenance/build_unified_manuscript.py --publish`.\n''',
      'mathematics/results.md':f'''{MARKER}\n## Consolidated article and noncommuting return words\n\n[Noncommuting return-word theorem](noncommuting_return_words.md): for a fixed\nfinite separated support tower, an exact anti-palindromic return word gives\nall-orders operator-norm conjugacy of the natural single kick at fixed classical\nstrength, uniformly on fixed polynomial time windows. The four-site bracket is\nnonzero but a coboundary, so its Green--Kubo variance is zero. This is not\ngeneric BGS. See `manuscript/WoW_unified.tex`.\n''',
      'record/claim_ledger.md':f'''{MARKER}\n## Consolidation and return-word status, 6 September 2026\n\nPROJECT PROOF: `mathematics/noncommuting_return_words.md`. Exact noncommuting\nreturn words on a finite support tower yield fixed-strength all-orders quantum\nconjugacy with a product gauge. The four-site bracket is nonzero but an explicit\ncoboundary.\n\nAUDITED FINITE EVIDENCE: the radius-eight arbitrary-phase proof was regenerated\nand independently replayed; historical component commands and new controls have\nseparately recorded scope. No positive BGS, priority certification or new Lean\nbuild is inferred.\n''',
      'RESEARCH_LOG.md':f'''{MARKER}\n- 2026-09-06: Audited consolidation and noncommuting return words integrated.\n'''
    }

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    required=['manuscript/WoW_unified.tex','mathematics/noncommuting_return_words.md']
    for name in required:
        if not (ROOT/name).is_file():raise SystemExit(f'Missing input: {name}')
    changes=[]
    for name,block in additions().items():
        path=ROOT/name;old=path.read_text(encoding='utf-8') if path.exists() else ''
        if MARKER in old:continue
        changes.append(name)
        if not args.check:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(old.rstrip()+'\n\n'+block.strip()+'\n',encoding='utf-8')
    print(('Would update: ' if args.check else 'Updated: ')+(', '.join(changes) if changes else 'none'))

if __name__=='__main__':main()
