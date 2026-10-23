import json
import subprocess
import sys
from pathlib import Path

target=Path(sys.argv[1]); binary=target.parent/'cluster_check'
build=subprocess.run(['g++','-O2','-std=c++20','cluster_check.cpp','-o',str(binary)],capture_output=True,text=True)
(target.parent/'compiler_stderr.txt').write_text(build.stderr)
assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True)
(target.parent/'engine_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
data=json.loads(run.stdout)
assert data['cycles']==872 and data['cycle_partition_pairs']==657148 and data['field_cases']==1971444
assert data['empty_leading_cases']==15
target.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data))
