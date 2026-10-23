"""Driver; used only inside the recorded bounded experiment."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(sys.argv[1]).resolve()
OUT.mkdir(parents=True,exist_ok=True)
binary=OUT/"schur_ssyt_control"
commands=[]
def execute(argv):
    proc=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True,check=False,timeout=45)
    commands.append({"argv":argv,"stdout":proc.stdout,"stderr":proc.stderr})
    (OUT/"subcommands.json").write_text(json.dumps(commands,indent=2)+"\n")
    proc.check_returncode()
    return proc.stdout
execute(["g++","-O2","-std=c++17","-Wall","-Wextra","-Wpedantic",
    str(ROOT.parents[2]/"computations/cpp/circular_phase_ssyt_verifier.cpp"),"-o",str(binary)])
cpp=execute([str(binary)])
parsed=json.loads(cpp)
assert parsed["all_passed"]
(OUT/"cpp_results.json").write_text(json.dumps(parsed,indent=2)+"\n")
execute([sys.executable,str(ROOT/"scripts/exact_checks.py"),
    str(OUT/"cpp_results.json"),str(OUT/"results.json")])
(OUT/"subcommands.json").write_text(json.dumps(commands,indent=2)+"\n")

