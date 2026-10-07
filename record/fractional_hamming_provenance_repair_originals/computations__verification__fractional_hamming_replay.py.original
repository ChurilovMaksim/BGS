#!/usr/bin/env python3
"""Read-only bounded exact Hamming checks in this interpreter's optimization mode.

The no-argument entry point runs author and synthesis adapters; eight separate
workspace entries run the five independent families (full-End split four ways) in an external temporary
directory, compares every scientific field with frozen results, and verifies
source hashes before and after. It is silent on success and never writes to
the repository. Run normally and with -O for the two separate modes.
"""
from pathlib import Path
import hashlib
import json
import os
import resource
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
PORTS = ROOT / 'computations/verification/fractional_hamming'
RAW = ROOT / 'evidence/fractional_hamming_20261007/raw'


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(case=None):
    mapping = json.loads((ROOT / 'record/fractional_hamming_adapter_mapping.json').read_text())
    paths = [Path(__file__).resolve(), ROOT / 'record/fractional_hamming_adapter_mapping.json']
    for row in mapping['ports']:
        original = ROOT / row['frozen_source']
        port = ROOT / row['port']
        require(sha(original) == row['source_sha256'], 'Frozen adapter source mismatch')
        require(sha(port) == row['port_sha256'], 'Maintained adapter source mismatch')
        paths.extend([original, port])
    expected_paths = {
        'author': RAW / 'author/results.json',
        'independent': RAW / 'review/results/verified/all_results.json',
        'synthesis': RAW / 'review/synthesis_results.json',
    }
    paths.extend(expected_paths.values())
    paths.append(PORTS / 'case_runner.py')
    for version in ['results', 'results/verified']:
        for name in ['full_end', 'top_gram', 'torus', 'network', 'offcharge_bound']:
            paths.append(RAW / 'review' / version / (name + '.json'))
    before = {p: sha(p) for p in paths}
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')

    def limits():
        resource.setrlimit(resource.RLIMIT_AS, (3 * 1024 ** 3, 3 * 1024 ** 3))
        resource.setrlimit(resource.RLIMIT_CPU, (320, 320))

    prefix = [sys.executable, '-B'] + (['-O'] if sys.flags.optimize else [])
    deadline = time.monotonic() + 350
    with tempfile.TemporaryDirectory(prefix='bgs_fractional_hamming_', dir='/tmp') as directory:
        work = Path(directory)
        require(ROOT not in work.parents and work != ROOT, 'Temporary output must be external')
        for family in (['author', 'synthesis'] if case is None else ['independent']):
            output = work / (family + '.json')
            remaining = deadline - time.monotonic()
            require(remaining > 0, 'Overall 350-second replay budget exhausted')
            command = prefix + [str(PORTS / (family + '_checks.py')), '--output', str(output)]
            if case is not None:
                command = prefix + [str(PORTS / 'case_runner.py'), '--case', case, '--output', str(output)]
            run = subprocess.run(
                command,
                cwd=work, env=env, preexec_fn=limits, timeout=min(340, remaining),
                capture_output=True, text=True)
            require(run.returncode == 0 and not run.stdout and not run.stderr,
                    family + ' exact replay failed or was not silent: ' + run.stderr)
            actual = json.loads(output.read_text())
            expected = json.loads(expected_paths[family].read_text())
            for key in {'author': ['elapsed_seconds'],
                        'independent': ['runtime_seconds'], 'synthesis': []}[family]:
                expected.pop(key, None)
            if case is not None:
                original_case = 'full_end' if case.startswith('full_end_') else case
                expected = expected[original_case]
                if case.startswith('full_end_'):
                    n, m = map(int, case.removeprefix('full_end_').split('_'))
                    expected = [row for row in expected if (row['N'], row['m']) == (n, m)]
            require(actual == expected, family + ' differs from frozen scientific output')
            if family == 'independent':
                for version in ['results', 'results/verified']:
                    for name in ['full_end', 'top_gram', 'torus', 'network', 'offcharge_bound']:
                        frozen = RAW / 'review' / version / (name + '.json')
                        require(json.loads(expected_paths['independent'].read_text())[name] == json.loads(frozen.read_text()),
                                'Initial or authoritative independent subresult differs')
            if family == 'synthesis':
                require(len(actual['mask_cases']) == 108 and len(actual['pair_families']) == 8,
                        'Synthesis coverage changed')
    require(before == {p: sha(p) for p in paths}, 'Input bytes changed during replay')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
