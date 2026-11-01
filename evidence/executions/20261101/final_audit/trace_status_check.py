#!/usr/bin/env python3
"""Cross-check TRACE/claim ids and adjacent status words against record/claims.json.
Usage: trace_status_check.py REPO FILE...
For each id occurrence, look at (a) the markdown table row cell(s) or (b) a short
window of text right after the id (up to the next id / sentence end) for a status
word. Report mismatches and ids not in registry. Range ids (BGS-TRACE-098..105) are
expanded and must all share the word's status."""
import json,re,sys,pathlib
repo=pathlib.Path(sys.argv[1]); reg={c['id']:c['state'] for c in json.load(open(repo/'record/claims.json'))['claims']}
W={'proved':'proved','доказан':'proved','open':'open','открыт':'open','conditional':'conditional','условн':'conditional',
   'refuted':'refuted','опроверг':'refuted','verification-pending':'verification-pending','pending':'verification-pending',
   'ожидает':'verification-pending','проверк':None}
SW=re.compile(r'\b(verification-pending|proved|open|conditional|refuted|pending)\b|(доказан|открыт|условн|опроверг|ожидает)',re.I)
IDR=re.compile(r'BGS-([A-Z]+)-(\d{3})(?:\.\.(\d{3})|/(\d{3}))?')
bad=0;unknown=set();n=0
for f in sys.argv[2:]:
  txt=pathlib.Path(f).read_text()
  for ln,line in enumerate(txt.splitlines(),1):
    for m in IDR.finditer(line):
      fam,a,b,c2=m.groups(); ids=[f'BGS-{fam}-{a}']
      if b: ids=[f'BGS-{fam}-{i:03d}' for i in range(int(a),int(b)+1)]
      if c2: ids.append(f'BGS-{fam}-{c2}')
      ids=[i for i in ids if i in reg or unknown.add((f,ln,i))]
      if not ids: continue
      n+=1
      if line.lstrip().startswith('|'):
        cells=[x.strip().strip('*').lower() for x in line.split('|')]
        idcell=[k for k,x in enumerate(cells) if m.group(0).lower() in x]
        st=None
        for x in cells[(idcell[0]+1 if idcell else 0):]:
          mm=SW.fullmatch(x) or (SW.match(x) if len(x)<40 else None)
          if mm: st=mm.group(0).lower(); break
        window=None
      else:
        rest=line[m.end():m.end()+45]; rest=re.split(r'BGS-[A-Z]+-\d|[.;]\s',rest)[0]
        mm=SW.search(rest); st=mm.group(0).lower() if mm else None
      if not st: continue
      key=next(k for k in W if st.startswith(k) or k in st); want=W[key]
      if want is None: continue
      for i in ids:
        if reg[i]!=want:
          # 'open' is ambiguous in prose ("open inputs"); report as candidate
          print(f'{f}:{ln}: {i} near "{st}" but registry={reg[i]} :: {line.strip()[:160]}'); bad+=1
for u in sorted(unknown): print('UNREGISTERED',*u)
print(f'checked {n} id occurrences, {bad} candidate mismatches, {len(unknown)} unregistered ids')
