#!/usr/bin/env python3
"""Run five exact higher-ramified finite controls under explicit child limits."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import resource
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent / 'ramified_higher'
MODES = ('bases', 'unit_bases', 'dictionary', 'poles', 'grades')

def limits():
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = args.output.resolve() if args.output else None
    if output and output.is_relative_to(ROOT) and not output.is_relative_to(ROOT / 'build'):
        raise ValueError('Output inside maintained source is forbidden')
    if output:
        output.mkdir(parents=True, exist_ok=True)
        if any((output / (mode + '_results.json')).exists() for mode in MODES):
            raise ValueError('Refusing to overwrite existing results')
    files = [SOURCE / 'checks.py', SOURCE / 'data/pole_dictionary.json']
    before = {str(p.relative_to(SOURCE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    records = []
    with tempfile.TemporaryDirectory(prefix='bgs-higher-ramified-') as tmp:
        directory = output or Path(tmp)
        for mode in MODES:
            target = directory / (mode + '_results.json')
            command = [sys.executable] + (['-O'] if sys.flags.optimize else [])
            command += [str(SOURCE / 'checks.py'), mode, '--output', str(target)]
            start = time.monotonic()
            proc = subprocess.run(command, text=True, capture_output=True, env=env,
                                  timeout=240, preexec_fn=limits)
            if output:
                (output / (mode + '.log')).write_text(proc.stdout)
                (output / (mode + '.stderr')).write_text(proc.stderr)
            print(proc.stdout, end='')
            if proc.stderr:
                print(proc.stderr, end='', file=sys.stderr)
            if proc.returncode or not target.is_file():
                raise RuntimeError('Exact child failed: ' + mode)
            result = json.loads(target.read_text())
            if result['mode'] != mode or result['source_sha256'] != before['checks.py']:
                raise RuntimeError('Mode/source result identity mismatch')
            records.append({'mode':mode,'exit_status':proc.returncode,'seconds':time.monotonic()-start,
                            'command':command,'result_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                            'stdout_sha256':hashlib.sha256(proc.stdout.encode()).hexdigest()})
    after = {str(p.relative_to(SOURCE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    if before != after:
        raise RuntimeError('Execution source changed')
    record = {'status':'PASS','python_optimized':bool(sys.flags.optimize),'source_hashes':before,
              'sources_unchanged':True,'runs':records,
              'limits':{'per_child_memory_bytes':2*1024**3,'per_child_cpu_seconds':180,'per_child_wall_seconds':240,'cooperative_threads':1},
              'scope':'Exact finite bases, dictionaries, pole separation and recurrence controls. Uniform normalized-lattice proof and inherited polynomial theorem remain separately reviewed mathematics, not finite sampling or Lean formalization.'}
    if output:
        (output / 'receipt.json').write_text(json.dumps(record,indent=2)+'\n')
    print('ramified-higher-commutant: all five exact modes passed')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
