cd /workspace/audit/lineN2
P=/workspace/bgs-derand/phase3/venv/bin/python
for f in 8V 8E 16V 16E; do $P code/ref_e_cert.py $f 4000 40 20; done
$P code/ref_e_cert.py 8V 1000 40 20
$P code/ref_e_cert.py 8V 1000 40 20 12
$P code/ref_e_cert.py 8V 1000 48 20
