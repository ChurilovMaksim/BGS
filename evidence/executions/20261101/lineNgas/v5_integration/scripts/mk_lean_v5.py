import re, hashlib
E='evidence/executions/20261101/lineNgas'
jobs=[  # (src, old namespace, new namespace, target, description)
 (f'{E}/N20/lean/LineN20.lean','LineN20','Bgs.LineN20','formalization/Bgs/LineN20Arith.lean',
  'Line N20 v2 (λ-carry graph, Collatz–Wielandt, Green kernel; referee lineN20)'),
 (f'{E}/N20/lean/LineN20Tail.lean','LineN20T','Bgs.LineN20Tail','formalization/Bgs/LineN20TailArith.lean',
  'Line N20 v2 (renewal lemma, joint-carry bound, conditional H1 ⇒ H3 arithmetic; referee lineN20 fixes 1/5)'),
 (f'{E}/N21/lean/LineN21Arith_v2.lean',None,'Bgs.LineN21','formalization/Bgs/LineN21Arith.lean',
  'Line N21 v2 (H4 core→true conversion: Lemmas C, Q, D^T arithmetic; referees lineN21, lineN21b)'),
]
for src,old,new,tgt,desc in jobs:
    s=open(src,encoding='utf-8').read(); sha=hashlib.sha256(s.encode()).hexdigest()
    lines=s.split('\n'); assert lines[0].strip()=='import Mathlib'
    drop={f'namespace {old}',f'end {old}'} if old else set()
    assert not old or sum(l.strip()==f'namespace {old}' for l in lines)==1
    body='\n'.join(l for l in lines[1:] if l.strip() not in drop).strip('\n')
    names=re.findall(r'^(?:theorem|lemma)\s+([^\s:({\[]+)', body, re.M)
    code=re.sub(r'/-.*?-/|--[^\n]*','',body,flags=re.S)
    assert not re.search(r'\bsorry\b|native_decide|\badmit\b|\baxiom\b', code), src
    hdr=(f'import Mathlib\n/-! {desc}: author/referee arithmetic for THEOREM_DRAFT v5 (`computations/verification/lineN_theorem_draft/THEOREM_DRAFT_v5.md`).\n'
         f'Source file `{src}` (sha256 {sha[:8]}…), integrated verbatim inside the namespace `{new}`'
         + (f' (author namespace `{old}`)' if old else ' (author file had no namespace)') +
         f';\nonly `#print axioms` lines were added (one per theorem, {len(names)}). No sorry, no native_decide. -/\n')
    out=hdr+f'namespace {new}\n\n'+body+'\n\n'+'\n'.join(f'#print axioms {n}' for n in names)+f'\n\nend {new}\n'
    open(tgt,'w',encoding='utf-8').write(out); print(tgt,len(names),sha)
