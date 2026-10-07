#!/usr/bin/env python3
"""Read-only, source-bound exact charge replay. Silent on successful default run.

Preserves this interpreter's -O mode; outputs only to an external directory.
Explicit resource caps are POSIX per-child limits, not a process-tree budget.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import importlib.util
import json
import math
import os
import platform
import resource
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
MODULES = ROOT / 'computations/verification/charge_strengthening'
RAW = ROOT / 'evidence/charge_strengthening_20261007/raw'
SOURCE_MAP = ROOT / 'record/charge_strengthening_replay_sources.json'
MEMORY_BYTES = 512 * 1024 ** 2
CPU_SECONDS = 60
WALL_SECONDS = 70
OUTPUT_BYTES = 1024 ** 2


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def comparator():
    spec = importlib.util.spec_from_file_location('bgs_charge_comparison', MODULES / 'comparison.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sources():
    mapping = json.loads(SOURCE_MAP.read_text())
    require(set(mapping) == {'schema', 'files'}, 'Unexpected source-map schema fields')
    require(mapping['schema'] == 'bgs-charge-replay-sources-v1', 'Unknown source-map schema')
    pinned = {}
    for row in mapping['files']:
        require(set(row) == {'path', 'sha256'}, 'Unexpected source row fields')
        path = Path(row['path'])
        require(not path.is_absolute() and '..' not in path.parts,
                'Nonportable source path')
        require(row['path'] not in pinned, 'Duplicate source path')
        full = ROOT / path
        require(full.is_file() and not full.is_symlink(), 'Missing regular source: ' + row['path'])
        require(sha(full) == row['sha256'], 'Source SHA256 mismatch: ' + row['path'])
        pinned[row['path']] = row['sha256']
    return pinned


def runtime():
    libraries = {}
    for name in ['numpy', 'sympy']:
        try:
            libraries[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            libraries[name] = 'not installed'
    return {'python': platform.python_version(), 'python_full': sys.version,
            'executable': sys.executable, 'optimization': sys.flags.optimize,
            'platform': platform.platform(), 'installed_but_unused_libraries': libraries,
            'arithmetic': 'Python exact integers and fractions; no third-party imports'}


def expected_provenance(family, result):
    if family == 'author':
        manifest = RAW / 'author/control_manifest.json'
        original = json.loads(manifest.read_text())
        environment = {'python': original['python'], 'platform': original['platform']}
        duration = original['jobs'][0]['elapsed_seconds']
        source = RAW / 'author/check_exact.py'
    else:
        directory = 'normal' if family == 'core' else 'switch_normal'
        manifest = RAW / 'review' / directory / 'manifest.json'
        original = json.loads(manifest.read_text())
        environment = original['environment']
        duration = original['run']['runtime_seconds']
        source = RAW / 'review' / ('independent_checks.py' if family == 'core' else 'switch_checks.py')
    return {'result_sha256': sha(result), 'source_sha256': sha(source),
            'runtime_seconds': duration,
            'manifest_sha256': sha(manifest), 'environment': environment,
            'original_manifest': str(manifest.relative_to(ROOT)),
            'original_result': str(result.relative_to(ROOT))}


def cache_expected(families):
    return {family: {'bytes': expected_file.read_bytes(),
                     'provenance': expected_provenance(family, expected_file)}
            for family, name, expected_file, schema in families}


def run(work, inject_failure=False):
    require(work != ROOT and ROOT not in work.parents, 'Output directory must be outside repository')
    work.mkdir(parents=True, exist_ok=True)
    require(not any(work.iterdir()), 'Output directory must be empty; stale results are rejected')
    before = sources()
    source_map_hash = sha(SOURCE_MAP)
    comp = comparator()
    env = os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1',
               OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    prefix = [sys.executable, '-B'] + (['-O'] if sys.flags.optimize else [])

    def limits():
        resource.setrlimit(resource.RLIMIT_AS, (MEMORY_BYTES, MEMORY_BYTES))
        resource.setrlimit(resource.RLIMIT_CPU, (CPU_SECONDS, CPU_SECONDS))

    execution = runtime()
    comparisons = []
    jobs = []
    families = [
        ('author', 'author_checks.py', RAW / 'author/exact_results.json', 'author-exact-v1'),
        ('core', 'independent_checks.py', RAW / 'review/normal/checks.json', 'independent-core-v1'),
        ('switch', 'switch_checks.py', RAW / 'review/switch_normal/checks.json', 'independent-switch-v1'),
    ]
    # Freeze raw expected bytes and their provenance BEFORE any worker starts.
    frozen_expected = cache_expected(families)
    for family, name, expected_file, schema in families:
        output = work / (family + '.json')
        command = prefix + [str(MODULES / name)]
        if family != 'author':
            command += ['--output', str(output)]
        if inject_failure:
            command += ['--inject-failure']
        started = time.monotonic()
        proc = subprocess.run(command, cwd=work, env=env, preexec_fn=limits,
                              capture_output=True, timeout=WALL_SECONDS)
        (work / (family + '.stdout')).write_bytes(proc.stdout)
        (work / (family + '.stderr')).write_bytes(proc.stderr)
        require(len(proc.stdout) <= OUTPUT_BYTES and len(proc.stderr) <= OUTPUT_BYTES,
                'Captured log exceeds declared output cap')
        require(proc.returncode == 0, family + ' exact control failed: ' + proc.stderr.decode(errors='replace')[-2000:])
        require(not proc.stderr, family + ' emitted unexpected stderr')
        if family == 'author':
            output.write_bytes(proc.stdout)
        else:
            require(output.read_bytes() == proc.stdout, family + ' output/stdout byte mismatch')
        expected = comp.loads_json(frozen_expected[family]['bytes'])
        require(hashlib.sha256(frozen_expected[family]['bytes']).hexdigest()
                == frozen_expected[family]['provenance']['result_sha256'],
                'Cached expected bytes/provenance binding failed')
        observed = comp.load_json(output)
        elapsed = time.monotonic() - started
        require(math.isfinite(elapsed) and elapsed >= 0, 'Invalid observed runtime')
        current = {'runtime_seconds': elapsed, 'result_sha256': sha(output), 'source_sha256': sha(MODULES / name),
                   'environment': execution, 'command': command}
        result = comp.compare(schema, expected, observed,
                              frozen_expected[family]['provenance'], current)
        require(result['scientific_comparison']['equal'],
                family + ' scientific JSON mismatch: ' + json.dumps(result['scientific_comparison']))
        # The author's output embeds source identity as a scientific-contract field.
        if family == 'author':
            require(observed['sha256_source'] == sha(MODULES / name), 'Author result/source binding failed')
        comparisons.append(result)
        jobs.append({'family': family, 'command': command, 'exit_status': proc.returncode,
                     'runtime_seconds': elapsed,
                     'source_sha256': sha(MODULES / name), 'result': output.name,
                     'result_sha256': sha(output),
                     'stdout_sha256': sha(work / (family + '.stdout')),
                     'stderr_sha256': sha(work / (family + '.stderr'))})
    require(sha(SOURCE_MAP) == source_map_hash, 'Source map changed during replay')
    after = sources()
    require(before == after, 'Source set changed during replay')
    report = {'schema': 'bgs-charge-replay-v1', 'status': 'passed',
              'environment': execution, 'source_map_sha256': source_map_hash,
              'source_hashes_before': before, 'source_hashes_after': after,
              'resource_caps': {'per_child_memory_bytes': MEMORY_BYTES,
                                'per_child_cpu_seconds': CPU_SECONDS,
                                'per_child_wall_seconds': WALL_SECONDS,
                                'post_capture_log_bytes': OUTPUT_BYTES,
                                'cpu_affinity': 'not forced', 'cooperative_threads': 1},
              'jobs': jobs, 'comparisons': comparisons,
              'non_claim': 'Bounded exact controls only; no analytic limit, full undamped residual or BGS proof.'}
    (work / 'replay_manifest.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--inject-failure', action='store_true')
    args = parser.parse_args()
    if args.output_dir is None:
        with tempfile.TemporaryDirectory(prefix='bgs_charge_', dir='/tmp') as directory:
            run(Path(directory), args.inject_failure)
    else:
        run(args.output_dir.resolve(), args.inject_failure)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
