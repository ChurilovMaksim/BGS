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
import os
import resource
import subprocess
import sys
import tempfile
import time


EVIDENCE = Path('evidence/intermediate_old_layers_20261007')
VOLATILE_KEYS = {'seconds', 'elapsed_seconds'}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def scientific(value):
    if isinstance(value, dict):
        return {k: scientific(v) for k, v in value.items() if k not in VOLATILE_KEYS}
    if isinstance(value, list):
        return [scientific(v) for v in value]
    return value


def sha(data):
    return hashlib.sha256(data).hexdigest()


def scientific_sha(value):
    return sha(json.dumps(scientific(value), sort_keys=True, separators=(',', ':')).encode())


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
    if hasattr(os, 'sched_getaffinity'):
        available = os.sched_getaffinity(0)
        os.sched_setaffinity(0, {min(available)})
    require(625 * (420001 - 1)**2 < 2**63, 'Dense independent int64 bound')
    require(175 * (2625001 - 1)**2 < 2**63, 'Supplied reduced int64 bound')
    require(420001**3 < 2**63, 'Supplied first-order triple-product bound')
    load_module(module_path).run(scratch)


def run(root, inherited_root=None):
    config = json.loads((root / EVIDENCE / 'input_map.json').read_text())
    receipts = []
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
        expected = {step['name']: json.loads((scratch / step['group'] / step['expected']).read_text())
                    for step in config['steps']}
        for step in config['steps']:
            module_path = root / step['module']
            load_module(module_path)
            command = [sys.executable] + (['-O'] if not __debug__ else [])
            command += [str(Path(__file__).resolve()), '--worker', str(module_path.resolve()),
                        str(scratch / step['group'])]
            start = time.monotonic()
            process = subprocess.run(command, capture_output=True, text=True, timeout=360)
            elapsed = time.monotonic() - start
            require(process.returncode == 0, 'Replay failed: ' + step['name'] + '\n' + process.stderr)
            require(len(process.stdout.encode()) + len(process.stderr.encode()) <= 1024**2,
                    'Replay log exceeds cap: ' + step['name'])
            result = json.loads((scratch / step['group'] / step['result']).read_text())
            require(scientific(result) == scientific(expected[step['name']]),
                    'Reviewed original scientific output mismatch: ' + step['name'])
            receipts.append({'name': step['name'], 'exit_status': process.returncode,
                             'elapsed_seconds': elapsed, 'module_sha256': sha(module_path.read_bytes()),
                             'original_source_sha256': step['source_sha256'],
                             'original_scientific_sha256': scientific_sha(expected[step['name']]),
                             'replay_scientific_sha256': scientific_sha(result),
                             'all_fields_except_runtime_equal': True, 'silent_import': True,
                             'stdout_sha256': sha(process.stdout.encode()),
                             'stderr_sha256': sha(process.stderr.encode())})
            print('PASS ' + step['name'], file=sys.stderr, flush=True)
    return {'status': 'PASS', 'claim_id': 'BGS-FM-026', 'optimized': not __debug__,
            'scope': 'Six exact finite reviewer replays; all-depth statements require separately accepted proof bridges.',
            'resource_caps_per_worker': {'wall_seconds': 360, 'cpu_seconds': 300,
                                         'address_space_bytes': 2 * 1024**3,
                                         'cpu_affinity_cores': 1, 'library_threads_cooperative': 1,
                                         'log_bytes_after_capture': 1024**2},
            'volatile_fields_excluded': sorted(VOLATILE_KEYS), 'runs': receipts,
            'nonclaims': ['No full U simplicity, gap estimate, or BGS result.',
                          'No rerun of the original author full rotated-return generator.',
                          'The frozen author matrices are independently checked by reviewed raw identities, phases, and characteristic algorithms.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--inherited-root', type=Path)
    parser.add_argument('--worker', nargs=2, metavar=('MODULE', 'SCRATCH'))
    args = parser.parse_args()
    if args.worker:
        worker(Path(args.worker[0]), Path(args.worker[1]))
    else:
        print(json.dumps(run(args.root, args.inherited_root), indent=2))


if __name__ == '__main__':
    main()
