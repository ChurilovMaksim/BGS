set -x
cd /tmp/lj/rerun/pkt
T(){ timeout 1200 nice -n 10 "$@"; echo "exit $?"; }
(cd code && T /workspace/bgs-derand/phase3/venv/bin/python sectors_exact.py) > /tmp/lj/rerun/sectors_exact.out 2>&1
T /workspace/bgs-derand/phase3/venv/bin/python code/exact_B.py > /tmp/lj/rerun/exact_B.out 2>&1
T /workspace/bgs-derand/phase3/venv/bin/python code/fixes_checks.py > /tmp/lj/rerun/fixes_checks.out 2>&1
T /workspace/bgs-derand/phase3/venv/bin/python code/assemble_v2.py > /tmp/lj/rerun/assemble_v2.out 2>&1
cd J3
T /workspace/bgs-derand/phase3/venv/bin/python code/rat_excl.py > /tmp/lj/rerun/rat_excl.out 2>&1
T /workspace/bgs-derand/phase3/venv/bin/python code/ranks.py > /tmp/lj/rerun/ranks.out 2>&1
T /workspace/bgs-derand/phase3/venv/bin/python code/inherit_proof_check.py > /tmp/lj/rerun/inherit.out 2>&1
T /workspace/bgs-derand/phase3/venv/bin/python code/assemble16.py > /tmp/lj/rerun/assemble16.out 2>&1
echo DONE
