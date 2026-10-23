#!/usr/bin/env python3
"""Bounded portable replay of the independently reviewed odd-newest controls.

Runs exact frozen originals and the portable controls, checks all scientific
fields in normal and optimized modes, and verifies silent, file-free imports.
Only elapsed_seconds is excluded from scientific equality. No finite replay
asserts the all-depth proof, literal-time transfer, gap bounds, or BGS.
"""
import argparse
import ast
import base64
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time
from datetime import datetime, timezone

CONTROLS = ('check_gauss_packets', 'check_intersections', 'check_finite_matrices')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')


def scientific(data):
    result = dict(data)
    if 'elapsed_seconds' not in result:
        raise RuntimeError('Missing explicitly declared runtime field')
    del result['elapsed_seconds']
    return result


def apply_limits():
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    # Preserve caps without forcing all concurrent workers onto the same core.


def invoke(argv, directory, environment):
    started = time.monotonic()
    result = subprocess.run(argv, cwd=directory, env=environment,
                            capture_output=True, text=True, timeout=180,
                            preexec_fn=apply_limits)
    if result.returncode:
        raise RuntimeError('Verification failed: ' + repr(argv) + '\n' + result.stderr)
    if len(result.stdout.encode()) + len(result.stderr.encode()) > 1024**2:
        raise RuntimeError('Captured output exceeds the declared 1 MiB limit')
    return result, time.monotonic() - started


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args(argv)
    code = Path(__file__).resolve().parent
    root = code.parents[2]
    evidence = root / 'archive/evidence/odd_newest_20261007'
    output = args.output_dir.resolve()
    if output == root or root in output.parents:
        raise RuntimeError('Output must be outside the overlay or repository')
    if output.exists() and any(output.iterdir()):
        raise RuntimeError('Use a new or empty scratch output directory')
    output.mkdir(parents=True, exist_ok=True)
    started_at = datetime.now(timezone.utc).isoformat()
    started = time.monotonic()
    tracked = list(code.glob('*.py')) + list(evidence.glob('*_expected.json')) + [evidence / 'original_index.json']
    tracked += sorted((evidence / 'originals').glob('*.json'))
    before = {str(p.relative_to(root)): sha(p) for p in tracked}
    original_index = json.loads((evidence / 'original_index.json').read_text())
    originals = {}
    for entry in original_index:
        envelope = json.loads((root / entry['envelope']).read_text())
        data = base64.b64decode(envelope['content_base64'], validate=True)
        if hashlib.sha256(data).hexdigest() != entry['sha256'] or len(data) != entry['bytes']:
            raise RuntimeError('Lossless source envelope verification failed')
        if envelope['sha256'] != entry['sha256'] or envelope['bytes'] != entry['bytes']:
            raise RuntimeError('Source envelope header disagrees with its index')
        originals[entry['role']] = data
    original_root = output / 'frozen_originals'
    required = [name + '.py' for name in CONTROLS]
    required += ['inputs/17_frozen_antireversor.py', 'inputs/23_odd_newest_discriminator.json']
    for relative in required:
        target = original_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(originals['odd-review/' + relative])
    env = os.environ.copy()
    env.pop('PYTHONOPTIMIZE', None)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    for variable in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS']:
        env[variable] = '1'
    executions = []
    comparisons = []
    import_directory = output / 'import_sandbox'
    import_directory.mkdir()
    for script in sorted(code.glob('*.py')):
        tree = ast.parse(script.read_text())
        if any(isinstance(node, ast.Assert) for node in ast.walk(tree)):
            raise RuntimeError('Optimizable assertion remains in ' + script.name)
        for flag in [[], ['-O']]:
            command = [sys.executable, '-B'] + flag + ['-c', "import importlib.util,sys; s=importlib.util.spec_from_file_location('control',sys.argv[1]); m=importlib.util.module_from_spec(s); sys.modules[s.name]=m; s.loader.exec_module(m)", str(script)]
            result, seconds = invoke(command, import_directory, env)
            if result.stdout or result.stderr or any(import_directory.iterdir()):
                raise RuntimeError('Import produced output or files: ' + script.name)
    for name in CONTROLS:
        expected_full = json.loads((evidence / (name + '_expected.json')).read_text())
        expected = scientific(expected_full)
        for mode, script, flags in [('frozen-original', original_root / (name + '.py'), []), ('normal', code / (name + '.py'), []), ('optimized', code / (name + '.py'), ['-O'])]:
            mode_output = output / mode
            mode_output.mkdir(exist_ok=True)
            command = [sys.executable, '-B'] + flags + [str(script)]
            current_env = env.copy()
            if mode == 'frozen-original':
                current_env['AUDIT_OUTPUT_DIR'] = str(mode_output)
            else:
                command += ['--output-dir', str(mode_output)]
            result, seconds = invoke(command, output, current_env)
            if result.stderr:
                raise RuntimeError('Unexpected verification stderr')
            actual_path = mode_output / (name + '.json')
            actual = json.loads(actual_path.read_text())
            if scientific(actual) != expected:
                raise RuntimeError('Scientific output disagreement: ' + name + '/' + mode)
            (mode_output / (name + '.stdout.txt')).write_text(result.stdout.rstrip() + '\n')
            executions.append({'control': name, 'mode': mode, 'argv': command,
                               'exit_status': result.returncode, 'runtime_seconds': seconds,
                               'output_sha256': sha(actual_path), 'script_sha256': sha(script)})
        comparisons.append({'control': name, 'original_and_normal_and_optimized_agree': True,
                            'excluded_fields': ['elapsed_seconds'],
                            'scientific_output': expected})
    after = {str(p.relative_to(root)): sha(p) for p in tracked}
    if before != after:
        raise RuntimeError('A pinned replay input changed during execution')
    record = {'status': 'PASS', 'started_at_utc': started_at,
              'runtime_seconds': time.monotonic() - started,
              'python': platform.python_version(), 'platform': platform.platform(),
              'bounds': {'wall_seconds_per_process': 180, 'cpu_seconds_per_process': 180,
                         'address_space_bytes_per_process': 2 * 1024**3,
                         'cpu_affinity_count': None, 'conventional_library_threads': 1,
                         'captured_output_bytes_checked_after_process': 1024**2},
              'scope': 'Exact bounded replay; the uniform argument and inherited rank-transfer theorem are separate proofs.',
              'imports': {'all_five_public_modules': 'silent and file-free in normal and optimized modes'},
              'lossless_originals_verified': len(original_index),
              'input_hashes_before': before, 'input_hashes_after': after,
              'executions': executions, 'comparisons': comparisons}
    write_json(output / 'portability_receipt.json', record)
    print(json.dumps({'status': 'PASS', 'controls': len(CONTROLS),
                      'executions': len(executions), 'output_agreement': 'all scientific fields exact',
                      'receipt': str(output / 'portability_receipt.json')}, indent=2))


if __name__ == '__main__':
    main()
