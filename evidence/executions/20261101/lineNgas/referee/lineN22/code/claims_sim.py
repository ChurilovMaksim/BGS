# simulate the referee-recommended v5 mapping on a COPY of claims.json and check: no proved claim depends on a non-proved one (except TRACE-206)
import json,copy
d=json.load(open('/workspace/lineNgas/repo/record/claims.json')); cl={c['id']:c for c in d['claims']}
T=lambda n:f'BGS-TRACE-{n}'
pre=[(c['id'],x) for c in cl.values() if c['state']=='proved' for x in c['dependencies'] if cl.get(x,{}).get('state')!='proved' and x!=T(206)]
def setc(n,state,deps=None):
    c=cl.setdefault(T(n),{'id':T(n),'dependencies':[]}); c['state']=state
    if deps is not None: c['dependencies']=[T(x) for x in deps]
for variant in ['referee','author']:
    cl={c['id']:copy.deepcopy(c) for c in d['claims']}
    if variant=='referee':
        setc(335,'proved',[307,311,323,198]); setc(322,'proved',[307,335]); setc(323,'proved',[311])
        setc(327,'proved',[323,328,335]); setc(328,'proved',[310,311]); setc(326,'proved',[198,307,311,322,323,327,328,335])
        setc(302,'proved',[307,322,326,327,328]); setc(301,'open'); setc(329,'proved',[311,312]); setc(330,'proved',[312])
        setc(331,'proved',[307,311,321]); setc(332,'conditional',[300,321,326,331]); setc(333,'conditional',[300,318,326,332])
        setc(325,'conditional',[206,213,271,273,300,303,304,305,306,307,326,332,333])
    else:
        setc(322,'proved'); setc(323,'proved'); setc(302,'proved'); setc(301,'conditional')
        setc(326,'proved',[307,311,322,323,327,328]); setc(327,'proved',[322,328]); setc(328,'proved',[310,311])
        setc(329,'proved',[311,312]); setc(330,'proved',[312]); setc(331,'proved',[307,311]); setc(332,'conditional',[300,321,326])
        setc(333,'conditional',[300,318,326,332]); setc(334,'proved',[]); setc(325,'conditional',[206,213,271,273,300,301,303,304,305,306,307,326,333])
    viol=[(c['id'],x,cl.get(x,{}).get('state')) for c in cl.values() if c['state']=='proved' for x in c['dependencies'] if cl.get(x,{}).get('state')!='proved' and x!=T(206)]
    new=[v for v in viol if (v[0],v[1]) not in pre]
    print(variant,'new violations:',new, '| 302 deps:',cl[T(302)]['dependencies'])
print('pre-existing violations (not ours):',len(pre))
