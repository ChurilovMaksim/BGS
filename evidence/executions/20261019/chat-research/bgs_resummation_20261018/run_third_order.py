import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path
from first_defect_verification import primitive_numerator

target=Path(sys.argv[1]);binary=target.parent/'third_order_check'
build=subprocess.run(['g++','-O2','-std=c++20','third_order_check.cpp','-o',str(binary)],capture_output=True,text=True)
(target.parent/'compiler_stderr.txt').write_text(build.stderr);assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True,check=True)
rows=[json.loads(x) for x in run.stdout.splitlines()];expected=primitive_numerator(3)
for row in rows:
    q=row['q'];assert F(row['e5_weight24'],24*q)==expected.get(q,F(0)),row
    expected_max={6:F(-15,8),10:F(75,8)}.get(q,F(0))
    assert F(row['e6_weight24'],24)==expected_max,row
assert len(rows)==24 and sum(row['coverage'] for row in rows if row['p']==3)==409112
data={'status':'passed_direct_third_order_diagrams','coverage':409112,'fields':[3,5,13],'rows':rows,
      'scope':'All cycles and all partitions of codimension <=3 at q<=10; tests e=5,6 sectors at h=3, not a full higher-order theorem.'}
(target.parent/'engine_stderr.txt').write_text(run.stderr)
target.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data))
