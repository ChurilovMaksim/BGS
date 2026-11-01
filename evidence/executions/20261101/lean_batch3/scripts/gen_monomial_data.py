"""Generator of the data block of formalization/Bgs/LineIMonomial.lean (Lean batch 3). Run from anywhere; prints the witness
summary and writes data.json and data.lean in the working directory. Reuses fam/search of
computations/verification/lineI/sym_v3/monomial_intertw.py verbatim (exec of its definitions)."""
import sys, os, json
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','..','..','computations','verification','lineI')
sys.path.insert(0,os.path.join(R,'cert_v2'))
from gstates import g2params, reach, finite
src=open(os.path.join(R,'sym_v3','monomial_intertw.py')).read()
# reuse fam/search definitions only
code=src.split('base=fam(9,2)')[0].split("from gstates import g2params, reach, finite")[1]
exec(code)
out={}
for m in (9,15,21,27):
  for a in (2,-2):
    out[f'{m},{a}']={n:[[fam(m,a)[n][0][s] for s in range(16)],[fam(m,a)[n][1][s] for s in range(16)]] for n in range(8)}
out['conj92']={n:[[fam(9,2,'conj')[n][0][s] for s in range(16)],[fam(9,2,'conj')[n][1][s] for s in range(16)]] for n in range(8)}
out['neg92']={n:[[fam(9,2,'neg')[n][0][s] for s in range(16)],[fam(9,2,'neg')[n][1][s] for s in range(16)]] for n in range(8)}
w={}
base=fam(9,2)
for m in (9,15,21,27):
  for a in (2,-2):
    G=fam(m,a); w[f'{m},{a}']=dict(lin=search(base,G),conj=search(fam(9,2,'conj'),G))
w['neg']=search(fam(9,2,'neg'),base)
json.dump(dict(tables=out,wit=w),open('data.json','w'))
for k,v in w.items(): print(k, v if k=='neg' else {kk:(vv is not None) for kk,vv in v.items()})
D=json.loads(json.dumps(dict(tables=out,wit=w))); T=D['tables']; W=D['wit']
def vec(l): return '![' + ', '.join(str(x) for x in l) + ']'
def famlean(name,tb):
    t=vec([vec(tb[str(n)][0]) for n in range(8)]); p=vec([vec([x%8 for x in tb[str(n)][1]]) for n in range(8)])
    return f"/-- family `{name}`: targets `t n s`. -/\ndef t_{name} : Fin 8 → Fin 16 → Fin 16 :=\n  {t}\n\n/-- family `{name}`: phase exponents `p n s` (mod 8). -/\ndef p_{name} : Fin 8 → Fin 16 → ZMod 8 :=\n  {p}\n\n"
out=[]
keys={'9,2':'m9p','9,-2':'m9n','15,2':'m15p','15,-2':'m15n','21,2':'m21p','21,-2':'m21n','27,2':'m27p','27,-2':'m27n'}
for k,nm in keys.items(): out.append(famlean(nm,T[k]))
out.append(famlean("conj9",T["conj92"])); out.append(famlean("neg9",T["neg92"]))
wits=[]
for k,nm in keys.items():
    if k=='9,2': continue
    mode='lin' if k.endswith(',2') else 'conj'
    w=W[k][mode]
    wits.append((nm,mode,w))
w=W['neg']; wits.append(('refl','neg',w))
for nm,mode,w in wits:
    out.append(f"def pi_{nm} : Fin 16 → Fin 16 := {vec(w['pi'])}\ndef c_{nm} : Fin 16 → ZMod 8 := {vec(w['c'])}\n\n")
open('data.lean','w').write(''.join(out))
print([ (nm,mode) for nm,mode,_ in wits])
