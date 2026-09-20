"""Rebuild and run the independent verifier, including a rejected mutation."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

folder = Path(__file__).resolve().parent
started = time.monotonic()
subprocess.run([sys.executable, str(folder/'export_certificates.py')], check=True)
command = ['g++', '-std=c++20', '-O3', '-Wall', '-Wextra', '-Werror',
           str(folder/'replay.cpp'), '-o', str(folder/'replay')]
build = subprocess.run(command, capture_output=True, text=True)
assert build.returncode == 0, build.stderr
run = subprocess.run([str(folder/'replay'), str(folder/'certificates.txt')],
                     capture_output=True, text=True)
assert run.returncode == 0, run.stderr
rows = [json.loads(line) for line in run.stdout.splitlines()]
certs = json.loads((folder/'certificates.json').read_text())['certificates']
assert [(x['N'], bool(x['ordinary_midpoint'])) for x in rows] == [
       (x['N'], x['ordinary_midpoint']) for x in certs]
assert all(x['independent_replay'] == 'passed' for x in rows)
lines = (folder/'certificates.txt').read_text().splitlines()
coefficient_count = int(lines[0].split()[0])
polynomial_line = coefficient_count+5
parts = lines[polynomial_line].split()
parts[-1] = str((int(parts[-1])+1) % certs[0]['p'])
lines[polynomial_line] = ' '.join(parts)
corrupt = folder/'corrupt_certificate.tmp'
try:
    corrupt.write_text('\n'.join(lines)+'\n')
    bad = subprocess.run([str(folder/'replay'), str(corrupt)], capture_output=True, text=True)
finally:
    corrupt.unlink(missing_ok=True)
assert bad.returncode != 0 and 'q(B)v != 0' in bad.stderr
version = subprocess.run(['g++', '--version'], capture_output=True, text=True, check=True).stdout.splitlines()[0]
result = {'status': 'completed', 'compiler': version, 'compiler_arguments': command[1:-3],
          'compiler_exit': build.returncode, 'verifier_exit': run.returncode,
          'results': rows, 'corrupt_certificate_exit': bad.returncode,
          'corrupt_certificate_stderr': bad.stderr.strip(),
          'elapsed_seconds': time.monotonic()-started,
          'input_sha256': {name: hashlib.sha256((folder/name).read_bytes()).hexdigest()
                           for name in ('replay.cpp', 'certificates.txt', 'certificates.json')},
          'scope': 'Exact finite C++ verification; not a formal proof assistant or asymptotic theorem'}
(folder/'cpp_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': 'completed', 'cases': len(rows), 'mutation': 'rejected',
                  'elapsed_seconds': result['elapsed_seconds']}))
