"""Independent arithmetic check: hand-transcribed table and a degree-three identity."""
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

table={
    3:(0,0,8,0),4:(44,0,0,9),5:(-65,-40,0,0),
    6:(-72,-174,-16,0),7:(168,0,-140,0),8:(288,120,0,-36),
    9:(54,270,18,0),10:(0,150,90,0),11:(66,0,99,0),12:(0,0,0,27)
}
delta={6:-180,7:-84,8:240,9:108}
result=json.loads(Path('universal_open_second_run/result.json').read_text())
checks=[]
for p in result['primes']:
    rows=[r for r in result['open_core_histograms'] if r['p']==p]
    for row in rows:
        expected=list(table[row['q']])
        if p==3:expected[0]+=delta.get(row['q'],0)
        actual=row['histogram12'][1:]+[0]*4
        assert actual[:4]==expected
        assert not any(row['histogram12'][5:])
    # b_2(m)/m has degree <=3, since every surviving e is at most four.
    # Four distinct exact zeros therefore prove the rational polynomial identity.
    for m in (17,18,19,20):
        value=F(0)
        for row in rows:
            for e,v in enumerate(row['histogram12']):
                if e:value+=F(v,12*row['q'])*math.comb(m-row['q']+e-1,e-1)
        assert value==0
        checks.append({'p':p,'m':m,'b2_divided_by_m':str(value)})
path=Path(sys.argv[1])
path.write_text(json.dumps({'status':'passed','table_matches_all_nine_fields':True,
                           'degree_bound_for_b2_over_m':3,'exact_zeros':checks,
                           'scope':'Independent arithmetic implementation, same author; does not independently rederive the cycle counts or support bound'},indent=2)+'\n')
print(json.dumps({'status':'passed','table_fields':len(result['primes']),'exact_zeros':len(checks)}))
