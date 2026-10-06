#!/usr/bin/env python3
"""Portable, fail-closed exact controls. No assertions; no silently skipped builds.

Default: Python and optimized Python, independently compiled C++ (-DNDEBUG).
--lean additionally requires Lean on PATH and compiles the pinned module.
Output/evidence and binaries stay outside maintained sources.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def validate_output(output):
    """Reject source overlap before creating a directory or writing a log."""
    output = output.resolve()
    require(output != ROOT and not ROOT.is_relative_to(output),
            'Output overlaps maintained source')
    if output.is_relative_to(ROOT):
        require(output.relative_to(ROOT).parts[0] == 'build',
                'Output must be outside source or under its build/ directory')
    require(not output.exists() or output.is_dir(), 'Output must be a directory')
    return output

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--lean', action='store_true')
    args = parser.parse_args()
    output = args.output.resolve() if args.output else Path(tempfile.mkdtemp(prefix='bgs-four-cut-'))
    output = validate_output(output)
    output.mkdir(parents=True, exist_ok=True)
    py = ROOT / 'computations/verification/four_cut_rank_two_kernel.py'
    cpp = ROOT / 'computations/cpp/four_cut_rank_two_kernel.cpp'
    lean = ROOT / 'formalization/Bgs/FourCutKernel.lean'
    sources = [Path(__file__).resolve(), py, cpp, lean, ROOT / 'formalization/lean-toolchain']
    hashes = lambda: {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    receipt = {'scope': 'Exact bounded rank-two kernel only; no abstract reduction or analytic formalization.', 'input_hashes_before': hashes(), 'commands': [], 'lean_requested': args.lean}
    def run(name, argv, cwd=ROOT, timeout=180):
        start = time.monotonic()
        with (output / (name + '.log')).open('w') as log:
            result = subprocess.run(argv, cwd=cwd, text=True, stdout=log, stderr=subprocess.STDOUT, timeout=timeout)
        receipt['commands'].append({'name': name, 'argv': [str(x) for x in argv], 'cwd': str(cwd), 'exit_code': result.returncode, 'elapsed_seconds': time.monotonic()-start})
        require(result.returncode == 0, name + ' failed; inspect ' + str(output))
        return (output / (name + '.log')).read_text()
    try:
        normal = json.loads(run('python', [sys.executable, str(py)]))
        optimized = json.loads(run('python_optimized', [sys.executable, '-O', str(py)]))
        require(normal == optimized, 'optimized Python changed output')
        compiler = shutil.which(os.environ.get('CXX', 'c++'))
        require(compiler is not None, 'C++ compiler required; set CXX to compiler executable')
        executable = output / 'four_cut_rank_two_kernel'
        run('cpp_compile', [compiler, '-std=c++17', '-O2', '-DNDEBUG', '-Wall', '-Wextra', '-pedantic', str(cpp), '-o', str(executable)])
        control = json.loads(run('cpp', [str(executable)]))
        for kind, key in [('pairs', 'partitions'), ('triple', 'oriented_cycles')]:
            require(normal[kind][key] == control[kind][key], 'configuration totals differ')
            require(normal[kind].get('directed_matches', 0) == control[kind]['directed_matches'], 'match totals differ')
        receipt['results'] = normal
        if args.lean:
            lean_command = shutil.which('lean')
            require(lean_command is not None, '--lean requested but Lean is not on PATH')
            receipt['lean_version'] = run('lean_version', [lean_command, '--version'], ROOT/'formalization')
            pin = (ROOT/'formalization/lean-toolchain').read_text().strip().split(':v')[-1]
            require('version ' + pin + ',' in receipt['lean_version'], 'Lean version does not match pinned toolchain')
            run('lean', [lean_command, '-j1', '-M4096', '-o', str(output/'FourCutKernel.olean'), 'Bgs/FourCutKernel.lean'], ROOT/'formalization', 210)
        require(receipt['input_hashes_before'] == hashes(), 'source changed during execution')
        receipt['status'] = 'passed'
    except Exception as error:
        receipt['status'] = 'failed'
        receipt['error'] = str(error)
        raise
    finally:
        receipt['input_hashes_after'] = hashes()
        receipt['log_hashes'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in output.glob('*.log')}
        (output/'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    require(receipt['input_hashes_before'] == receipt['input_hashes_after'], 'source changed during execution')
    print(json.dumps(receipt, indent=2))

if __name__ == '__main__':
    main()
