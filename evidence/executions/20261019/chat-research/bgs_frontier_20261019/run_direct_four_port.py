import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

target=Path(sys.argv[1]);folder=target.parent;binary=folder/'direct_four_port'
build=subprocess.run(['g++','-O2','-std=c++20','-Wall','-Wextra','direct_four_port.cpp','-o',str(binary)],capture_output=True,text=True)
(folder/'compiler_stderr.txt').write_text(build.stderr);assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True)
(folder/'engine_stdout.txt').write_text(run.stdout);(folder/'engine_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
rows=[json.loads(line) for line in run.stdout.splitlines()]
reference=json.loads(Path('kernel_run/result.json').read_text())
assert len(rows)==18
for row in rows:
    summary=next(a for a in reference['summary'] if a['p']==row['p'])
    for channel,value in enumerate(row['boundary_weight24_rotations']):
        direct=F(value,24*4*row['q'])
        expected=F(summary['four_port_polynomials'][channel].get(str(row['q']),0))
        assert direct==expected,(row['q'],row['p'],channel,direct,expected)
data={'status':'passed_original_cycle_partition_prefix_check','rows':rows,
      'coefficient_comparisons':len(rows)*24,
      'scope':'All cycle-cover candidates with exactly four common edges and all partitions of codimension <=3 at q=4..9, without using the graph classification. Shares elementary modular-rank ideas; this is an alternative enumeration, not independent review.'}
target.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({'status':data['status'],'coefficient_comparisons':data['coefficient_comparisons']}))
