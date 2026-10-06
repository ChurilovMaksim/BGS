#!/usr/bin/env python3
"""Replay the exact first-seven certificate; no universal conclusion from sampling.

Requires a C++17 compiler and SymPy for the six dictionary controls. Temporary
binaries are never written into maintained source. Python -O uses C++ NDEBUG;
all load-bearing checks are explicit exceptions in either mode.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shlex
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent / 'first_seven'
PINNED_CERTIFICATE = '3e155b5de58a46cb60235c16913ba7cb06c704ec6673537fa77ad27c5512c6c8'

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def verify_input(path):
    require(path.is_file() and not path.is_symlink(), 'certificate must be a regular file')
    require(digest(path) == PINNED_CERTIFICATE, 'reviewed certificate identity mismatch')

def output_directory(path):
    path = path.resolve()
    if path.is_relative_to(ROOT) and not path.is_relative_to(ROOT / 'build'):
        raise ValueError('Output inside maintained source is forbidden; use build/ or an external directory')
    path.mkdir(parents=True, exist_ok=True)
    return path

def run(output=None, compiler=None):
    data = SOURCE / 'certificate.txt'
    verify_input(data)
    before = {p.name: digest(p) for p in SOURCE.iterdir() if p.is_file()}
    command = shlex.split(compiler or os.environ.get('CXX', 'g++'))
    require(bool(command), 'empty compiler command')
    version = subprocess.check_output(command + ['--version'], text=True).splitlines()[0]
    records = []
    def execute(name, argv):
        start = time.monotonic()
        proc = subprocess.run(argv, capture_output=True, text=True, timeout=180)
        elapsed = time.monotonic() - start
        print(proc.stdout, end='')
        if proc.stderr:
            print(proc.stderr, end='', file=sys.stderr)
        row = {'name': name, 'argv': argv, 'exit_code': proc.returncode,
               'seconds': elapsed, 'stdout_sha256': hashlib.sha256(proc.stdout.encode()).hexdigest(),
               'stderr_sha256': hashlib.sha256(proc.stderr.encode()).hexdigest()}
        records.append(row)
        if output:
            (output / (name + '.log')).write_text(proc.stdout)
            (output / (name + '.stderr')).write_text(proc.stderr)
        require(proc.returncode == 0, name + ' failed')
        return proc.stdout
    with tempfile.TemporaryDirectory(prefix='bgs-first-seven-') as temporary:
        directory = Path(temporary)
        flags = ['-std=c++17', '-O3'] + (['-DNDEBUG'] if sys.flags.optimize else [])
        for stem in ('first_seven_exact', 'actual_small'):
            binary = directory / stem
            execute('compile_' + stem, command + flags + [str(SOURCE / (stem + '.cpp')), '-o', str(binary)])
            log = execute(stem, [str(binary)] + ([str(data)] if stem == 'first_seven_exact' else []))
            records[-1]['binary_sha256'] = digest(binary)
            if stem == 'first_seven_exact':
                require(log.count('2841 independent determinant evaluations PASS') == 6,
                        'six full determinant classes not completed')
                require('ALL INDEPENDENT CHECKS PASS' in log, 'polynomial replay completion missing')
            else:
                require(all(('N=' + str(n) + ' ') in log for n in (7, 21, 63)), 'actual residue controls incomplete')
        python = [sys.executable] + (['-O'] if sys.flags.optimize else [])
        execute('dictionary', python + [str(SOURCE / 'dictionary.py')])
    after = {p.name: digest(p) for p in SOURCE.iterdir() if p.is_file()}
    require(before == after, 'maintained replay sources changed during execution')
    result = {'status': 'PASS', 'scope': '17046 exact determinant evaluations, including 16866 identity nodes; exact field/gcd/Bezout/root-order checks plus finite raw-model controls. No Lean, spectral-simplicity or BGS claim.',
              'arithmetic': 'GF(5^6) base-five codes and exact binary exponent vectors; no floating-point mathematical checks',
              'compiler': version, 'python_optimized': bool(sys.flags.optimize),
              'source_sha256': before, 'sources_unchanged': True, 'runs': records}
    if output:
        (output / 'receipt.json').write_text(json.dumps(result, indent=2) + '\n')
    print('first-seven-commutant: all exact certificate replays passed')
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--compiler')
    args = parser.parse_args()
    run(output_directory(args.output) if args.output else None, args.compiler)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
