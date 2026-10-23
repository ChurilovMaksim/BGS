import json
import subprocess
import sys
from pathlib import Path
target=Path(sys.argv[1]);binary=target.parent/'primitive_defect'
compiler=subprocess.run(['g++','--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]
build=subprocess.run(['g++','-O2','-std=c++20','primitive_defect.cpp','-o',str(binary)],capture_output=True,text=True)
(target.parent/'compiler_stderr.txt').write_text(build.stderr);assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True,check=True)
rows=[json.loads(x) for x in run.stdout.splitlines()]
old=json.loads(Path('dependencies/h2_core_table.json').read_text());ref={(r['q'],r['p']):r['histogram12'][3] for r in old['open_core_histograms']}
expected={3:8,6:2,7:-119,9:18,10:60,11:66}
assert len(rows)==90
for row in rows:
    assert row['all12']==ref[row['q'],row['p']]
    assert row['primitive12']==expected.get(row['q'],0),(row,expected)
assert sum(r['coverage'] for r in rows if r['p']==3)==43954712
data={'status':'passed_exact_primitive_peeling','compiler':compiler,'rows':rows,'primitive12':expected,
      'coverage':43954712,'fields':old['primes'],
      'scope':'Exact h=2,e=3 raw and primitive sums. General decoration theorem is separate; shared prior enumeration helpers are explicitly reused.'}
(target.parent/'engine_stderr.txt').write_text(run.stderr)
target.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({k:v for k,v in data.items() if k!='rows'}))
