import json
import subprocess
import sys
from pathlib import Path
target=Path(sys.argv[1]);binary=target.parent/'incidence_check'
compiler=subprocess.run(['g++','--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]
build=subprocess.run(['g++','-O2','-std=c++20','incidence_check.cpp','-o',str(binary)],capture_output=True,text=True)
(target.parent/'compiler_stderr.txt').write_text(build.stderr)
assert build.returncode==0,build.stderr
run=subprocess.run([str(binary.resolve())],capture_output=True,text=True,check=True)
data=json.loads(run.stdout);assert data['cycles']==409112 and data['field_cases']==1227336
data.update(status='passed_finite_check',compiler=compiler)
(target.parent/'engine_stderr.txt').write_text(run.stderr)
target.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data))
