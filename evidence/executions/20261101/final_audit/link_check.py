import re,sys,pathlib,unicodedata
def slug(h):
  h=h.strip().lower(); h=re.sub(r'[^\w\- ]','',h); return h.replace(' ','-')
bad=0
for f in sys.argv[1:]:
  p=pathlib.Path(f); s=p.read_text()
  s_nocode=re.sub(r'```.*?```','',s,flags=re.S)
  for m in re.finditer(r'\]\(([^)\s]+)\)',s_nocode):
    u=m.group(1)
    if re.match(r'[a-z]+:',u): continue
    path,_,anc=u.partition('#')
    tgt=(p.parent/path) if path else p
    if not tgt.exists(): print(f,'MISSING',u); bad+=1; continue
    if anc and tgt.suffix=='.md':
      hs={slug(re.sub(r'^#+','',l)) for l in tgt.read_text().splitlines() if l.startswith('#')}
      if anc not in hs: print(f,'ANCHOR?',u); bad+=1
print('bad',bad)
