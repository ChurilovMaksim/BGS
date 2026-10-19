import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

target=Path(sys.argv[1]);binary=target.parent/'direct_p42'
build=subprocess.run(['g++','-O2','-std=c++20','direct_p42.cpp','-o',str(binary)],capture_output=True,text=True)
(target.parent/'compiler_stderr.txt').write_text(build.stderr);assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True)
(target.parent/'engine_stderr.txt').write_text(run.stderr);assert run.returncode==0,run.stderr
rows=[json.loads(line) for line in run.stdout.splitlines()]
pred=json.loads(Path('dependencies/gluing_reference.json').read_text())['P42']
assert len(rows)==12 and sum(r['cycles'] for r in rows if r['p']==3)==46200
for row in rows:assert F(row['weight720'],720*row['q'])==F(pred.get(str(row['q']),0)),row
data={'status':'passed_direct_cycle_partition_check','rows':rows,'scope':'Direct finite prefix through q=9, not a substitute for the structural gluing proof.'}
target.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data))
