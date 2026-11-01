"""N20: emit the Collatz-Wielandt certificate (integer Perron-vector rounding on the 633 states) as a Lean 31x31 table."""
import json
c=json.load(open('../logs/carry_graph_cert.json')); X=[[0]*31 for _ in range(31)]
for (a,b),x in zip(c['states'],c['x']): X[a+15][b+15]=x
rows=',\n  '.join('['+','.join(map(str,r))+']' for r in X)
open('../lean/cw_table.lean.inc','w').write('def Xcw : List (List Nat) := [\n  '+rows+']\n')
print('ok',sum(1 for r in X for v in r if v>0))
