import json
import subprocess
import sys
from pathlib import Path

target=Path(sys.argv[1])
compiler=subprocess.run(['g++','--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]
binary=target.parent/'pivot_search'
subprocess.run(['g++','-O2','-std=c++20','pivot_search.cpp','-o',str(binary)],check=True)
result=subprocess.run([str(binary.resolve())],capture_output=True,text=True,check=True)
data=json.loads(result.stdout)
assert data['cycles']==409112
assert data['field_cases']==3*data['cycles']
data['compiler']=compiler
data['status']='completed_search_not_a_universal_proof'
(target.parent/'engine_stderr.txt').write_text(result.stderr)
target.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data))
