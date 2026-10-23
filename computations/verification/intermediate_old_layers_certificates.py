#!/usr/bin/env python3
"""Six bounded, exact, independent replays supporting the scoped FM-026 extension.

Run with Python or Python -O. Every input is decoded and SHA256 verified before
use; all arithmetic/output work stays in temporary storage. The all-depth
statements require the separately reviewed mathematical reductions, not finite
extrapolation. Requires NumPy and SymPy; no external network or project imports.
"""
from pathlib import Path
import argparse
import base64
import contextlib
import hashlib
import importlib.util
import io
import json
import math
import os
import resource
import shutil
import subprocess
import sys
import tempfile
import time


EVIDENCE = Path('archive/evidence/intermediate_old_layers_20261007')
RUNTIME_FIELDS = {
    'first_cancellation': ('elapsed_seconds',),
    'return_operator': ('seconds',),
    'return_nonprimitive': ('seconds',),
    'residual25_projectors': ('seconds',),
    'residual25_coherent': ('seconds',),
}
ENVIRONMENT_FIELDS = {
    'return_operator': ('python', 'numpy', 'sympy'),
    'residual25_projectors': ('python', 'numpy', 'sympy'),
    'residual25_coherent': ('python',),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def environment_metadata(value, step):
    fields = ENVIRONMENT_FIELDS.get(step, ())
    require(isinstance(value, dict), 'Expected a result object')
    for key in fields:
        require(key in value and isinstance(value[key], str) and bool(value[key]),
                'Missing or invalid top-level environment field: ' + key)
    return {key: value[key] for key in fields}


def scientific(value, step):
    excluded = set(environment_metadata(value, step))
    for key in RUNTIME_FIELDS.get(step, ()):
        require(key in value and isinstance(value[key], (int, float))
                and not isinstance(value[key], bool) and math.isfinite(value[key]) and value[key] >= 0,
                'Missing or invalid top-level runtime field: ' + key)
        excluded.add(key)
    return {key: item for key, item in value.items() if key not in excluded}


def differing_paths(actual, expected, path='$', limit=17):
    paths = []

    def visit(a, b, current):
        if len(paths) >= limit:
            return
        if type(a) is not type(b):
            paths.append(current + ' (type)')
        elif isinstance(a, dict):
            for key in sorted(set(a) | set(b)):
                child = current + '[' + json.dumps(key) + ']'
                if key not in a or key not in b:
                    paths.append(child + (' (missing)' if key not in a else ' (unexpected)'))
                else:
                    visit(a[key], b[key], child)
                if len(paths) >= limit:
                    break
        elif isinstance(a, list):
            if len(a) != len(b):
                paths.append(current + ' (length)')
            for index, (left, right) in enumerate(zip(a, b)):
                visit(left, right, current + '[' + str(index) + ']')
        elif a != b:
            paths.append(current)

    visit(actual, expected, path)
    return paths


def record_mismatch(name, actual, expected, paths, actual_bytes, expected_bytes):
    directory = Path(tempfile.mkdtemp(prefix='bgs-intermediate-mismatch-'))
    (directory / 'actual.json').write_bytes(actual_bytes)
    (directory / 'expected.json').write_bytes(expected_bytes)
    record = {'status': 'SCIENTIFIC_OUTPUT_MISMATCH', 'step': name,
              'actual_result_sha256': sha(actual_bytes),
              'expected_result_sha256': sha(expected_bytes),
              'original_environment': {k: expected.get(k) for k in ENVIRONMENT_FIELDS.get(name, ())} if isinstance(expected, dict) else {},
              'replay_environment': {k: actual.get(k) for k in ENVIRONMENT_FIELDS.get(name, ())} if isinstance(actual, dict) else {},
              'differing_json_paths': paths[:16], 'paths_truncated': len(paths) > 16,
              'diagnostics_directory': str(directory)}
    (directory / 'receipt.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, sort_keys=True), file=sys.stderr, flush=True)
    raise RuntimeError('Reviewed original scientific output mismatch: ' + name
                       + '; preserved diagnostics: ' + str(directory))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def scientific_sha(value, step):
    return sha(json.dumps(scientific(value, step), sort_keys=True, separators=(',', ':')).encode())


def load_module(path):
    spec = importlib.util.spec_from_file_location('intermediate_check', path)
    module = importlib.util.module_from_spec(spec)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
        exec(compile(path.read_bytes(), str(path), 'exec'), module.__dict__)
    require(capture.getvalue() == '', 'Import produced output: ' + str(path))
    return module


def worker(module_path, scratch):
    for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS']:
        os.environ[key] = '1'
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (300, 300))
    # Let the OS schedule independent workers; do not pin all concurrent checks to one shared core.
    require(625 * (420001 - 1)**2 < 2**63, 'Dense independent int64 bound')
    require(175 * (2625001 - 1)**2 < 2**63, 'Supplied reduced int64 bound')
    require(420001**3 < 2**63, 'Supplied first-order triple-product bound')
    load_module(module_path).run(scratch)


def isolated_step_workspace(staged_group, destination, result_relative):
    """Copy replay inputs into a new workspace, never staging its output.

    Original expected bytes remain cached outside the worker workspace. Each
    step has a private directory, so omitting an output cannot delete an input
    needed by a different step. The six maintained workers do not read their
    own declared output; this contract is exercised by real replays.
    """
    relative = Path(result_relative)
    require(not relative.is_absolute() and relative.parts
            and '..' not in relative.parts and relative != Path('.'),
            'Invalid replay output path: ' + str(relative))
    require(not destination.exists(), 'Replay workspace must be new')
    destination.mkdir(parents=True)
    for source in staged_group.rglob('*'):
        rel = source.relative_to(staged_group)
        if rel == relative:
            continue
        require(not source.is_symlink(), 'Replay input cannot be a symlink')
        target = destination / rel
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            require(source.is_file(), 'Replay input must be a regular file')
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    result_path = destination / relative
    result_path.parent.mkdir(parents=True, exist_ok=True)
    require(not result_path.exists() and not result_path.is_symlink(),
            'Replay output must be absent before execution')
    return result_path


def verify_replay_inputs(workspace, input_hashes):
    """Detect accidental modification of the copied original inputs."""
    for relative, expected_sha in input_hashes.items():
        path = workspace / relative
        require(path.is_file() and not path.is_symlink()
                and path.resolve().is_relative_to(workspace.resolve())
                and sha(path.read_bytes()) == expected_sha,
                'Replay modified an original input: ' + relative)


def read_fresh_result(workspace, result_path):
    require(result_path.is_file() and not result_path.is_symlink(),
            'Replay did not create a fresh regular result: ' + str(result_path))
    require(result_path.resolve().is_relative_to(workspace.resolve()),
            'Replay result escapes its private workspace')
    return result_path.read_bytes()


def run(root, inherited_root=None, replay_output_dir=None):
    config = json.loads((root / EVIDENCE / 'input_map.json').read_text())
    receipts = []
    if replay_output_dir is not None:
        replay_output_dir = Path(replay_output_dir)
        require(not replay_output_dir.exists(), 'Replay evidence directory must be new')
        replay_output_dir.mkdir(parents=True)
    with tempfile.TemporaryDirectory(prefix='bgs-intermediate-replay-') as directory:
        scratch = Path(directory)
        for group, files in config['groups'].items():
            for rel, h in files.items():
                relative = Path(config['blobs'][h])
                blob_path = root / relative
                if not blob_path.is_file() and inherited_root is not None:
                    blob_path = inherited_root / relative
                envelope = json.loads(blob_path.read_text())
                data = base64.b64decode(envelope['payload'], validate=True)
                require(sha(data) == h, 'Original input identity failed: ' + rel)
                target = scratch / group / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
        expected_bytes = {step['name']: (scratch / step['group'] / step['expected']).read_bytes()
                          for step in config['steps']}
        expected = {name: json.loads(data) for name, data in expected_bytes.items()}
        for step_index, step in enumerate(config['steps']):
            workspace = scratch / '_executions' / str(step_index)
            result_path = isolated_step_workspace(scratch / step['group'], workspace, step['result'])
            input_hashes = {str(path.relative_to(workspace)): sha(path.read_bytes())
                            for path in workspace.rglob('*') if path.is_file()}
            evidence_dir = None
            if replay_output_dir is not None:
                evidence_dir = replay_output_dir / str(step_index)
                evidence_dir.mkdir()
                (evidence_dir / 'expected.json').write_bytes(expected_bytes[step['name']])
                (evidence_dir / 'inputs.json').write_text(json.dumps(input_hashes, indent=2) + '\n')
                (evidence_dir / 'step.json').write_text(json.dumps(step, indent=2) + '\n')
            module_path = root / step['module']
            load_module(module_path)
            command = [sys.executable] + (['-O'] if not __debug__ else [])
            command += [str(Path(__file__).resolve()), '--worker', str(module_path.resolve()),
                        str(workspace)]
            start = time.monotonic()
            process = subprocess.run(command, capture_output=True, text=True, timeout=360)
            elapsed = time.monotonic() - start
            if evidence_dir is not None:
                (evidence_dir / 'stdout.log').write_text(process.stdout)
                (evidence_dir / 'stderr.log').write_text(process.stderr)
                (evidence_dir / 'process.json').write_text(json.dumps({
                    'command': command, 'exit_status': process.returncode,
                    'elapsed_seconds': elapsed}, indent=2) + '\n')
            require(process.returncode == 0, 'Replay failed: ' + step['name'] + '\n' + process.stderr)
            require(len(process.stdout.encode()) + len(process.stderr.encode()) <= 1024**2,
                    'Replay log exceeds cap: ' + step['name'])
            actual_bytes = read_fresh_result(workspace, result_path)
            if evidence_dir is not None:
                (evidence_dir / 'actual.json').write_bytes(actual_bytes)
            verify_replay_inputs(workspace, input_hashes)
            result = json.loads(actual_bytes)
            try:
                differences = differing_paths(scientific(result, step['name']),
                                              scientific(expected[step['name']], step['name']))
            except RuntimeError as error:
                key = str(error).rsplit(': ', 1)[-1]
                differences = ['$[' + json.dumps(key) + '] (invalid metadata)']
            if differences:
                record_mismatch(step['name'], result, expected[step['name']], differences,
                                actual_bytes,
                                expected_bytes[step['name']])
            receipts.append({'name': step['name'], 'exit_status': process.returncode,
                             'elapsed_seconds': elapsed, 'module_sha256': sha(module_path.read_bytes()),
                             'original_source_sha256': step['source_sha256'],
                             'original_scientific_sha256': scientific_sha(expected[step['name']], step['name']),
                             'replay_scientific_sha256': scientific_sha(result, step['name']),
                             'all_scientific_fields_equal': True, 'silent_import': True,
                             'fresh_result_created': True, 'private_step_workspace': True,
                             'copied_original_inputs_unchanged': True,
                             'original_result_sha256': sha(expected_bytes[step['name']]),
                             'replay_result_sha256': sha(actual_bytes),
                             'original_environment': environment_metadata(expected[step['name']], step['name']),
                             'replay_environment': environment_metadata(result, step['name']),
                             'stdout_sha256': sha(process.stdout.encode()),
                             'stderr_sha256': sha(process.stderr.encode())})
            print('PASS ' + step['name'], file=sys.stderr, flush=True)
    return {'status': 'PASS', 'claim_id': 'BGS-FM-026', 'optimized': not __debug__,
            'replay_evidence_directory': str(replay_output_dir) if replay_output_dir is not None else None,
            'scope': 'Six exact finite reviewer replays; all-depth statements require separately accepted proof bridges.',
            'resource_caps_per_worker': {'wall_seconds': 360, 'cpu_seconds': 300,
                                         'address_space_bytes': 2 * 1024**3,
                                         'cpu_affinity_cores': None, 'library_threads_cooperative': 1,
                                         'log_bytes_after_capture': 1024**2},
            'top_level_runtime_fields_excluded': RUNTIME_FIELDS,
            'top_level_environment_fields_excluded': ENVIRONMENT_FIELDS, 'runs': receipts,
            'nonclaims': ['No full U simplicity, gap estimate, or BGS result.',
                          'No rerun of the original author full rotated-return generator.',
                          'The frozen author matrices are independently checked by reviewed raw identities, phases, and characteristic algorithms.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--inherited-root', type=Path)
    parser.add_argument('--replay-output-dir', type=Path,
                        help='Preserve fresh outputs, frozen expectations, and logs in a new directory')
    parser.add_argument('--worker', nargs=2, metavar=('MODULE', 'SCRATCH'))
    args = parser.parse_args()
    if args.worker:
        worker(Path(args.worker[0]), Path(args.worker[1]))
    else:
        print(json.dumps(run(args.root, args.inherited_root, args.replay_output_dir), indent=2))


if __name__ == '__main__':
    main()
