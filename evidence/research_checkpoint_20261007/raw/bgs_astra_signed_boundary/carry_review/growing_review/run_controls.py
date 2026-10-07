import json, pathlib, subprocess, sys
out = pathlib.Path(sys.argv[1])
cmd=['g++','-std=c++17','-O2','-Wall','-Wextra','-pedantic','carry_review/growing_review/check_growing.cpp','-o',str(out/'check_growing')]
subprocess.run(cmd,check=True)
p=subprocess.run([str(out/'check_growing')],text=True,capture_output=True,check=True)
result=json.loads(p.stdout)
injected=subprocess.run([str(out/'check_growing'),'--inject-bad-carry'],text=True,capture_output=True)
if injected.returncode != 2 or 'literal cyclic carry identity' not in injected.stderr:
 raise RuntimeError('Injected missing-carry defect did not fail as expected')
result['negative_control']={'fault':'omit low-digit carry into high digit','returncode':injected.returncode,'diagnostic':injected.stderr.strip()}
result['compiler_command']=cmd
(out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
